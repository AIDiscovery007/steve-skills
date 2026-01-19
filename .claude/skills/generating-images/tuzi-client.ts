#!/usr/bin/env node
/**
 * Tuzi API Client - Zero-dependency TypeScript implementation
 * Integrates tuzi platform image generation API with prompt-generator skill
 */

import * as https from 'https';
import * as fs from 'fs';
import * as path from 'path';

// ============================================================================
// Type Definitions
// ============================================================================

interface GenerationResult {
  success: boolean;
  imageUrl?: string;
  error?: string;
  category?: 'AUTH_ERROR' | 'NETWORK_ERROR' | 'GENERATION_ERROR' | 'VALIDATION_ERROR';
  suggestion?: string;
}

interface TuziApiRequest {
  model: string;
  prompt: string;
  n: number;
  size: string;
  quality: string;
  response_format: string;
}

interface TuziApiResponse {
  data?: Array<{ url: string }>;
  error?: {
    message: string;
    type: string;
    code: string;
  };
}

interface EnvConfig {
  TUZI_API_KEY: string;
  TUZI_API_BASE: string;
  TUZI_MODEL: string;
}

// ============================================================================
// Environment Configuration
// ============================================================================

function loadEnvFile(): EnvConfig {
  const envPath = path.join(__dirname, '../../../.env.local');

  if (!fs.existsSync(envPath)) {
    throw new Error('ENV_NOT_FOUND');
  }

  const envContent = fs.readFileSync(envPath, 'utf-8');
  const config: Partial<EnvConfig> = {};

  envContent.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const [key, ...valueParts] = trimmed.split('=');
      const value = valueParts.join('=').trim();
      if (key && value) {
        config[key as keyof EnvConfig] = value;
      }
    }
  });

  if (!config.TUZI_API_KEY || !config.TUZI_API_BASE || !config.TUZI_MODEL) {
    throw new Error('ENV_INCOMPLETE');
  }

  return config as EnvConfig;
}

// ============================================================================
// Parameter Mapping
// ============================================================================

const ASPECT_RATIO_MAP: Record<string, string> = {
  '16:9': '1792x1024',
  '9:16': '1024x1792',
  '1:1': '1024x1024',
  '2:3': '1024x1536',
  '3:2': '1536x1024',
  '4:5': '1024x1280',
  '5:4': '1280x1024'
};

const QUALITY_MAP: Record<string, string> = {
  '0.25': 'standard',
  '0.5': 'standard',
  '1': 'standard',
  '2': 'hd'
};

function extractMidjourneyParams(prompt: string): {
  cleanPrompt: string;
  size: string;
  quality: string;
  style?: string;
} {
  let cleanPrompt = prompt;
  let size = '1024x1024'; // Default
  let quality = 'standard'; // Default
  let style: string | undefined;

  // Extract --ar parameter
  const arMatch = prompt.match(/--ar\s+(\d+:\d+)/i);
  if (arMatch) {
    const ratio = arMatch[1];
    size = ASPECT_RATIO_MAP[ratio] || size;
    cleanPrompt = cleanPrompt.replace(/--ar\s+\d+:\d+/gi, '').trim();
  }

  // Extract --q parameter
  const qMatch = prompt.match(/--q\s+([\d.]+)/i);
  if (qMatch) {
    const qualityValue = qMatch[1];
    quality = QUALITY_MAP[qualityValue] || quality;
    cleanPrompt = cleanPrompt.replace(/--q\s+[\d.]+/gi, '').trim();
  }

  // Extract --style parameter
  const styleMatch = prompt.match(/--style\s+(\w+)/i);
  if (styleMatch) {
    const styleValue = styleMatch[1].toLowerCase();
    if (styleValue === 'raw') {
      style = 'natural';
    }
    cleanPrompt = cleanPrompt.replace(/--style\s+\w+/gi, '').trim();
  }

  // Remove other Midjourney-specific parameters
  cleanPrompt = cleanPrompt
    .replace(/--v\s+\d+/gi, '')
    .replace(/--stylize\s+\d+/gi, '')
    .replace(/--chaos\s+\d+/gi, '')
    .replace(/--weird\s+\d+/gi, '')
    .replace(/--draft/gi, '')
    .replace(/--oref\s+\S+/gi, '')
    .replace(/--cref\s+\S+/gi, '')
    .replace(/--cw\s+\d+/gi, '')
    .replace(/--sref\s+\S+/gi, '')
    .replace(/--personalize/gi, '')
    .replace(/--p\s+\S+/gi, '')
    .replace(/--niji\s+\d+/gi, '')
    .replace(/--no\s+[^-]+/gi, '')
    .replace(/\s+/g, ' ')
    .trim();

  return { cleanPrompt, size, quality, style };
}

// ============================================================================
// HTTP Client (Native https module)
// ============================================================================

function httpsRequest(
  url: string,
  options: https.RequestOptions,
  body: string,
  timeout: number = 60000
): Promise<string> {
  return new Promise((resolve, reject) => {
    const req = https.request(url, options, (res) => {
      let data = '';

      res.on('data', (chunk) => {
        data += chunk;
      });

      res.on('end', () => {
        if (res.statusCode && res.statusCode >= 200 && res.statusCode < 300) {
          resolve(data);
        } else {
          reject({
            statusCode: res.statusCode,
            body: data
          });
        }
      });
    });

    req.on('error', (err) => {
      reject(err);
    });

    req.on('timeout', () => {
      req.destroy();
      reject(new Error('ETIMEDOUT'));
    });

    req.setTimeout(timeout);
    req.write(body);
    req.end();
  });
}

// ============================================================================
// Retry Logic
// ============================================================================

async function sleep(ms: number): Promise<void> {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function retryWithBackoff<T>(
  fn: () => Promise<T>,
  maxRetries: number = 3,
  baseDelay: number = 2000
): Promise<T> {
  let lastError: any;

  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      return await fn();
    } catch (error: any) {
      lastError = error;

      // Don't retry on auth errors or client errors
      if (error.statusCode && (error.statusCode === 401 || error.statusCode === 403 || error.statusCode === 400 || error.statusCode === 422)) {
        throw error;
      }

      // Don't retry on the last attempt
      if (attempt === maxRetries) {
        throw error;
      }

      // Exponential backoff: 2s, 4s, 8s
      const delay = baseDelay * Math.pow(2, attempt - 1);
      await sleep(delay);
    }
  }

  throw lastError;
}

// ============================================================================
// API Client
// ============================================================================

async function generateImage(prompt: string): Promise<GenerationResult> {
  try {
    // Load environment configuration
    const config = loadEnvFile();

    // Extract and map Midjourney parameters
    const { cleanPrompt, size, quality, style } = extractMidjourneyParams(prompt);

    // Prepare API request
    const requestBody: TuziApiRequest = {
      model: config.TUZI_MODEL,
      prompt: cleanPrompt,
      n: 1,
      size,
      quality,
      response_format: 'url'
    };

    const bodyJson = JSON.stringify(requestBody);

    // Make API request with retry logic
    const responseData = await retryWithBackoff(async () => {
      return await httpsRequest(
        `${config.TUZI_API_BASE}/v1/images/generations`,
        {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${config.TUZI_API_KEY}`,
            'Content-Type': 'application/json',
            'Content-Length': Buffer.byteLength(bodyJson)
          }
        },
        bodyJson
      );
    });

    // Parse response
    const response: TuziApiResponse = JSON.parse(responseData);

    if (response.data && response.data.length > 0) {
      return {
        success: true,
        imageUrl: response.data[0].url
      };
    } else {
      return {
        success: false,
        error: 'No image data returned from API',
        category: 'GENERATION_ERROR',
        suggestion: 'The API returned an empty response. Please try again or check the tuzi service status.'
      };
    }

  } catch (error: any) {
    // Error categorization
    if (error.message === 'ENV_NOT_FOUND') {
      return {
        success: false,
        error: 'API credentials not configured',
        category: 'AUTH_ERROR',
        suggestion: 'Please create a .env.local file in the repository root with TUZI_API_KEY, TUZI_API_BASE, and TUZI_MODEL.'
      };
    }

    if (error.message === 'ENV_INCOMPLETE') {
      return {
        success: false,
        error: 'Incomplete API configuration',
        category: 'AUTH_ERROR',
        suggestion: 'Please ensure .env.local contains all required fields: TUZI_API_KEY, TUZI_API_BASE, TUZI_MODEL.'
      };
    }

    if (error.statusCode === 401 || error.statusCode === 403) {
      return {
        success: false,
        error: 'Authentication failed',
        category: 'AUTH_ERROR',
        suggestion: 'Please verify your TUZI_API_KEY in .env.local. Check for extra spaces or quotes, and ensure the key is active.'
      };
    }

    if (error.statusCode === 400 || error.statusCode === 422) {
      let errorMessage = 'Invalid request parameters';
      try {
        const errorBody = JSON.parse(error.body);
        errorMessage = errorBody.error?.message || errorMessage;
      } catch {}

      return {
        success: false,
        error: errorMessage,
        category: 'VALIDATION_ERROR',
        suggestion: 'The prompt or parameters may be invalid. Please check the prompt format and try again.'
      };
    }

    if (error.statusCode === 429) {
      return {
        success: false,
        error: 'Rate limit exceeded',
        category: 'NETWORK_ERROR',
        suggestion: 'Too many requests. Please wait a moment and try again.'
      };
    }

    if (error.message === 'ETIMEDOUT' || error.code === 'ETIMEDOUT' || error.code === 'ECONNRESET') {
      return {
        success: false,
        error: 'Network timeout',
        category: 'NETWORK_ERROR',
        suggestion: 'The request timed out. Please check your network connection and try again.'
      };
    }

    // Generic error
    return {
      success: false,
      error: error.message || 'Unknown error occurred',
      category: 'GENERATION_ERROR',
      suggestion: 'An unexpected error occurred. Please try again or use the prompt manually in Midjourney.'
    };
  }
}

// ============================================================================
// CLI Interface
// ============================================================================

async function main() {
  const args = process.argv.slice(2);

  if (args.length === 0) {
    console.error(JSON.stringify({
      success: false,
      error: 'No prompt provided',
      category: 'VALIDATION_ERROR',
      suggestion: 'Usage: node tuzi-client.js "your prompt here"'
    }));
    process.exit(1);
  }

  const prompt = args.join(' ');
  const result = await generateImage(prompt);

  console.log(JSON.stringify(result, null, 2));
  process.exit(result.success ? 0 : 1);
}

// Run if executed directly
if (require.main === module) {
  main().catch(err => {
    console.error(JSON.stringify({
      success: false,
      error: err.message,
      category: 'GENERATION_ERROR'
    }));
    process.exit(1);
  });
}

export { generateImage, GenerationResult };
