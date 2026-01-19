#!/usr/bin/env node
"use strict";
/**
 * Tuzi API Client - Zero-dependency TypeScript implementation
 * Integrates tuzi platform image generation API with prompt-generator skill
 */
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g = Object.create((typeof Iterator === "function" ? Iterator : Object).prototype);
    return g.next = verb(0), g["throw"] = verb(1), g["return"] = verb(2), typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.generateImage = generateImage;
var https = require("https");
var fs = require("fs");
var path = require("path");
// ============================================================================
// Environment Configuration
// ============================================================================
function loadEnvFile() {
    var envPath = path.join(__dirname, '../../../.env.local');
    if (!fs.existsSync(envPath)) {
        throw new Error('ENV_NOT_FOUND');
    }
    var envContent = fs.readFileSync(envPath, 'utf-8');
    var config = {};
    envContent.split('\n').forEach(function (line) {
        var trimmed = line.trim();
        if (trimmed && !trimmed.startsWith('#')) {
            var _a = trimmed.split('='), key = _a[0], valueParts = _a.slice(1);
            var value = valueParts.join('=').trim();
            if (key && value) {
                config[key] = value;
            }
        }
    });
    if (!config.TUZI_API_KEY || !config.TUZI_API_BASE || !config.TUZI_MODEL) {
        throw new Error('ENV_INCOMPLETE');
    }
    return config;
}
// ============================================================================
// Parameter Mapping
// ============================================================================
var ASPECT_RATIO_MAP = {
    '16:9': '1792x1024',
    '9:16': '1024x1792',
    '1:1': '1024x1024',
    '2:3': '1024x1536',
    '3:2': '1536x1024',
    '4:5': '1024x1280',
    '5:4': '1280x1024'
};
var QUALITY_MAP = {
    '0.25': 'standard',
    '0.5': 'standard',
    '1': 'standard',
    '2': 'hd'
};
function extractMidjourneyParams(prompt) {
    var cleanPrompt = prompt;
    var size = '1024x1024'; // Default
    var quality = 'standard'; // Default
    var style;
    // Extract --ar parameter
    var arMatch = prompt.match(/--ar\s+(\d+:\d+)/i);
    if (arMatch) {
        var ratio = arMatch[1];
        size = ASPECT_RATIO_MAP[ratio] || size;
        cleanPrompt = cleanPrompt.replace(/--ar\s+\d+:\d+/gi, '').trim();
    }
    // Extract --q parameter
    var qMatch = prompt.match(/--q\s+([\d.]+)/i);
    if (qMatch) {
        var qualityValue = qMatch[1];
        quality = QUALITY_MAP[qualityValue] || quality;
        cleanPrompt = cleanPrompt.replace(/--q\s+[\d.]+/gi, '').trim();
    }
    // Extract --style parameter
    var styleMatch = prompt.match(/--style\s+(\w+)/i);
    if (styleMatch) {
        var styleValue = styleMatch[1].toLowerCase();
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
    return { cleanPrompt: cleanPrompt, size: size, quality: quality, style: style };
}
// ============================================================================
// HTTP Client (Native https module)
// ============================================================================
function httpsRequest(url, options, body, timeout) {
    if (timeout === void 0) { timeout = 60000; }
    return new Promise(function (resolve, reject) {
        var req = https.request(url, options, function (res) {
            var data = '';
            res.on('data', function (chunk) {
                data += chunk;
            });
            res.on('end', function () {
                if (res.statusCode && res.statusCode >= 200 && res.statusCode < 300) {
                    resolve(data);
                }
                else {
                    reject({
                        statusCode: res.statusCode,
                        body: data
                    });
                }
            });
        });
        req.on('error', function (err) {
            reject(err);
        });
        req.on('timeout', function () {
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
function sleep(ms) {
    return __awaiter(this, void 0, void 0, function () {
        return __generator(this, function (_a) {
            return [2 /*return*/, new Promise(function (resolve) { return setTimeout(resolve, ms); })];
        });
    });
}
function retryWithBackoff(fn_1) {
    return __awaiter(this, arguments, void 0, function (fn, maxRetries, baseDelay) {
        var lastError, attempt, error_1, delay;
        if (maxRetries === void 0) { maxRetries = 3; }
        if (baseDelay === void 0) { baseDelay = 2000; }
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    attempt = 1;
                    _a.label = 1;
                case 1:
                    if (!(attempt <= maxRetries)) return [3 /*break*/, 7];
                    _a.label = 2;
                case 2:
                    _a.trys.push([2, 4, , 6]);
                    return [4 /*yield*/, fn()];
                case 3: return [2 /*return*/, _a.sent()];
                case 4:
                    error_1 = _a.sent();
                    lastError = error_1;
                    // Don't retry on auth errors or client errors
                    if (error_1.statusCode && (error_1.statusCode === 401 || error_1.statusCode === 403 || error_1.statusCode === 400 || error_1.statusCode === 422)) {
                        throw error_1;
                    }
                    // Don't retry on the last attempt
                    if (attempt === maxRetries) {
                        throw error_1;
                    }
                    delay = baseDelay * Math.pow(2, attempt - 1);
                    return [4 /*yield*/, sleep(delay)];
                case 5:
                    _a.sent();
                    return [3 /*break*/, 6];
                case 6:
                    attempt++;
                    return [3 /*break*/, 1];
                case 7: throw lastError;
            }
        });
    });
}
// ============================================================================
// API Client
// ============================================================================
function generateImage(prompt) {
    return __awaiter(this, void 0, void 0, function () {
        var config_1, _a, cleanPrompt, size, quality, style, requestBody, bodyJson_1, responseData, response, error_2, errorMessage, errorBody;
        var _this = this;
        var _b;
        return __generator(this, function (_c) {
            switch (_c.label) {
                case 0:
                    _c.trys.push([0, 2, , 3]);
                    config_1 = loadEnvFile();
                    _a = extractMidjourneyParams(prompt), cleanPrompt = _a.cleanPrompt, size = _a.size, quality = _a.quality, style = _a.style;
                    requestBody = {
                        model: config_1.TUZI_MODEL,
                        prompt: cleanPrompt,
                        n: 1,
                        size: size,
                        quality: quality,
                        response_format: 'url'
                    };
                    bodyJson_1 = JSON.stringify(requestBody);
                    return [4 /*yield*/, retryWithBackoff(function () { return __awaiter(_this, void 0, void 0, function () {
                            return __generator(this, function (_a) {
                                switch (_a.label) {
                                    case 0: return [4 /*yield*/, httpsRequest("".concat(config_1.TUZI_API_BASE, "/v1/images/generations"), {
                                            method: 'POST',
                                            headers: {
                                                'Authorization': "Bearer ".concat(config_1.TUZI_API_KEY),
                                                'Content-Type': 'application/json',
                                                'Content-Length': Buffer.byteLength(bodyJson_1)
                                            }
                                        }, bodyJson_1)];
                                    case 1: return [2 /*return*/, _a.sent()];
                                }
                            });
                        }); })];
                case 1:
                    responseData = _c.sent();
                    response = JSON.parse(responseData);
                    if (response.data && response.data.length > 0) {
                        return [2 /*return*/, {
                                success: true,
                                imageUrl: response.data[0].url
                            }];
                    }
                    else {
                        return [2 /*return*/, {
                                success: false,
                                error: 'No image data returned from API',
                                category: 'GENERATION_ERROR',
                                suggestion: 'The API returned an empty response. Please try again or check the tuzi service status.'
                            }];
                    }
                    return [3 /*break*/, 3];
                case 2:
                    error_2 = _c.sent();
                    // Error categorization
                    if (error_2.message === 'ENV_NOT_FOUND') {
                        return [2 /*return*/, {
                                success: false,
                                error: 'API credentials not configured',
                                category: 'AUTH_ERROR',
                                suggestion: 'Please create a .env.local file in the repository root with TUZI_API_KEY, TUZI_API_BASE, and TUZI_MODEL.'
                            }];
                    }
                    if (error_2.message === 'ENV_INCOMPLETE') {
                        return [2 /*return*/, {
                                success: false,
                                error: 'Incomplete API configuration',
                                category: 'AUTH_ERROR',
                                suggestion: 'Please ensure .env.local contains all required fields: TUZI_API_KEY, TUZI_API_BASE, TUZI_MODEL.'
                            }];
                    }
                    if (error_2.statusCode === 401 || error_2.statusCode === 403) {
                        return [2 /*return*/, {
                                success: false,
                                error: 'Authentication failed',
                                category: 'AUTH_ERROR',
                                suggestion: 'Please verify your TUZI_API_KEY in .env.local. Check for extra spaces or quotes, and ensure the key is active.'
                            }];
                    }
                    if (error_2.statusCode === 400 || error_2.statusCode === 422) {
                        errorMessage = 'Invalid request parameters';
                        try {
                            errorBody = JSON.parse(error_2.body);
                            errorMessage = ((_b = errorBody.error) === null || _b === void 0 ? void 0 : _b.message) || errorMessage;
                        }
                        catch (_d) { }
                        return [2 /*return*/, {
                                success: false,
                                error: errorMessage,
                                category: 'VALIDATION_ERROR',
                                suggestion: 'The prompt or parameters may be invalid. Please check the prompt format and try again.'
                            }];
                    }
                    if (error_2.statusCode === 429) {
                        return [2 /*return*/, {
                                success: false,
                                error: 'Rate limit exceeded',
                                category: 'NETWORK_ERROR',
                                suggestion: 'Too many requests. Please wait a moment and try again.'
                            }];
                    }
                    if (error_2.message === 'ETIMEDOUT' || error_2.code === 'ETIMEDOUT' || error_2.code === 'ECONNRESET') {
                        return [2 /*return*/, {
                                success: false,
                                error: 'Network timeout',
                                category: 'NETWORK_ERROR',
                                suggestion: 'The request timed out. Please check your network connection and try again.'
                            }];
                    }
                    // Generic error
                    return [2 /*return*/, {
                            success: false,
                            error: error_2.message || 'Unknown error occurred',
                            category: 'GENERATION_ERROR',
                            suggestion: 'An unexpected error occurred. Please try again or use the prompt manually in Midjourney.'
                        }];
                case 3: return [2 /*return*/];
            }
        });
    });
}
// ============================================================================
// CLI Interface
// ============================================================================
function main() {
    return __awaiter(this, void 0, void 0, function () {
        var args, prompt, result;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    args = process.argv.slice(2);
                    if (args.length === 0) {
                        console.error(JSON.stringify({
                            success: false,
                            error: 'No prompt provided',
                            category: 'VALIDATION_ERROR',
                            suggestion: 'Usage: node tuzi-client.js "your prompt here"'
                        }));
                        process.exit(1);
                    }
                    prompt = args.join(' ');
                    return [4 /*yield*/, generateImage(prompt)];
                case 1:
                    result = _a.sent();
                    console.log(JSON.stringify(result, null, 2));
                    process.exit(result.success ? 0 : 1);
                    return [2 /*return*/];
            }
        });
    });
}
// Run if executed directly
if (require.main === module) {
    main().catch(function (err) {
        console.error(JSON.stringify({
            success: false,
            error: err.message,
            category: 'GENERATION_ERROR'
        }));
        process.exit(1);
    });
}
