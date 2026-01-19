# 输出格式与联动接口 (Output Formats)

本文档定义 manga-story-bible 的标准输出格式，以及与其他 Skill 的对接接口。

---

## 故事圣经编译格式

### 完整故事圣经文档

Phase 5 完成后输出的完整文档格式：

```markdown
# 故事圣经: 《[作品标题]》

## 文档信息
- 创建日期: [日期]
- 版本: v1.0
- 状态: [草案/待审/定稿]

---

# 第一部分: 执行摘要

## 基本信息
- **类型**: [少年漫画/少女漫画/四格漫画/同人志]
- **格式**: [読み切り/连载/同人志]
- **页数**: [X页]
- **目标读者**: [读者画像]

## 一句话概念
「[用一句话概括整个故事]」

## 核心主题
[用2-3句话描述故事想要表达的核心]

## 情感基调
[故事的整体情感氛围]

## 独特卖点
- [与同类型作品的差异化点1]
- [与同类型作品的差异化点2]

---

# 第二部分: 故事结构

## 结构类型
[起承転結 / 三幕式 / 混合式]

## 高潮场景
### 视觉描述
[最精彩场景的画面描述]

### 情感目标
[这个场景要达到的情感效果]

### 技法计划
[计划使用的特殊技法: 跨页/破格/大格等]

## 节拍表

| 节拍 | 页码 | 场景# | 内容概述 | 情感目标 |
|------|------|-------|----------|----------|
| Hook | P1 | S1 | [概述] | [情感] |
| Setup | P2-3 | S1-S2 | [概述] | [情感] |
| ... | ... | ... | ... | ... |

## 场景列表

### S1: [场景标题]
- **位置**: [结构位置]
- **页码**: P[X]-P[Y]
- **POV角色**: [角色ID]
- **出场角色**: [角色ID列表]
- **内容概述**: [2-3句]
- **情绪**: [开始情绪] → [结束情绪]
- **节奏**: [快/中/慢]
- **翻页钩子**: [最后一格的悬念]

### S2: [场景标题]
...

---

# 第三部分: 角色系统

## 角色一览

| ID | 名字 | 角色 | 原型 | 一句话描述 |
|----|------|------|------|------------|
| hero_001 | [名] | 主角 | [原型] | [描述] |
| heroine_001 | [名] | 女主角 | [原型] | [描述] |
| ... | ... | ... | ... | ... |

## 核心角色档案

### [hero_001] [角色名]

#### 心理架构
- **Want**: [表面欲望]
- **Need**: [内心需要]
- **Flaw**: [性格缺陷]
- **Ghost**: [过去创伤]
- **内部冲突**: [want vs need]
- **外部冲突**: [外部障碍]

#### 表达特征
- **性格特点**: [特点1], [特点2], [特点3]
- **说话风格**: [风格描述]
- **口头禅**: 「[台词]」

#### 视觉设定
- **面部**: [描述]
- **体型**: [描述]
- **服装**: [描述]
- **标志性特征**: [描述]

#### 角色弧线
- **开始状态**: [描述]
- **结束状态**: [描述]
- **关键转变**: [描述]

### [heroine_001] [角色名]
...

## 角色关系图

```
[文字关系图]
```

## 关系详解

| 角色A | 角色B | 关系类型 | 关系动态 |
|-------|-------|----------|----------|
| hero_001 | heroine_001 | 恋爱 | [动态描述] |
| hero_001 | rival_001 | 竞争 | [动态描述] |
| ... | ... | ... | ... |

---

# 第四部分: 世界设定

## 深度等级
[等级X: 名称] - [理由]

## 物理规则

### 能力系统 (如适用)
- **名称**: [系统名]
- **来源**: [能力来源]
- **规则**:
  - [规则1]
  - [规则2]
- **限制**:
  - [限制1]
  - [限制2]

### 技术水平
[时代/技术水平描述]

## 社会结构 (如适用)

### 权力体系
[简述]

### 组织势力
| 势力名 | 类型 | 与主角关系 | 故事作用 |
|--------|------|------------|----------|
| [势力1] | [类型] | [关系] | [作用] |

## 关键场景设定

### [场景1名称]
- **类型**: [室内/室外]
- **氛围**: [氛围描述]
- **视觉记忆点**: [标志性元素]
- **出现场景**: [S#列表]

### [场景2名称]
...

---

# 第五部分: 冲突架构

## 主角冲突矩阵

### 内部冲突
| 冲突类型 | 内容 | 解决时机 |
|----------|------|----------|
| Want vs Need | [描述] | S[#] |
| [其他] | [描述] | S[#] |

### 外部冲突
| 冲突类型 | 对立方 | 内容 | 解决时机 |
|----------|--------|------|----------|
| 人vs人 | [角色] | [描述] | S[#] |
| [其他] | [对象] | [描述] | S[#] |

## 障碍层级

```
主角目标: [目标]
├─ L1: [障碍] → [克服方式]
├─ L2: [障碍] → [所需成长]
├─ L3: [障碍] → [帮助来源]
├─ L4: [障碍] → [需要改变]
└─ Final: [最终障碍]
```

## 伏笔管理

| 编号 | 伏笔内容 | 埋设 | 回收 |
|------|----------|------|------|
| F01 | [内容] | S[#] P[#] | S[#] P[#] |
| F02 | [内容] | S[#] P[#] | S[#] P[#] |

---

# 第六部分: 附录

## 参考作品
- [作品1] - [参考了什么]
- [作品2] - [参考了什么]

## 待定事项
- [ ] [需要进一步确定的内容1]
- [ ] [需要进一步确定的内容2]

## 修订记录
| 版本 | 日期 | 修改内容 |
|------|------|----------|
| v1.0 | [日期] | 初版 |

---

# 附: 快速参考卡片

## 角色快速参考
| 角色 | 外貌关键词 | 性格关键词 | 口头禅 |
|------|------------|------------|--------|
| [名] | [关键词] | [关键词] | 「...」 |

## 世界规则速查
- [规则1要点]
- [规则2要点]

## 场景氛围速查
| 场景 | 氛围 | 色调 |
|------|------|------|
| [场景] | [氛围] | [色调] |
```

---

## manga-designer 对接格式

### 标准输入格式

当 Phase 5 选择"启动 manga-designer"时，输出以下格式：

```yaml
# ============================================
# manga-designer 输入文件
# 由 manga-story-bible 生成
# ============================================

# 项目元数据
project_meta:
  title: "[作品标题]"
  genre: "[少年/少女/四格/同人]"
  format: "[読み切り/连载章节/同人志]"
  page_count: [页数]
  style_direction:
    genre_style: "[少年/少女]"
    reference_works:
      - "[参考作品1]"
      - "[参考作品2]"
    mood_keywords:
      - "[关键词1]"
      - "[关键词2]"
      - "[关键词3]"

# 场景列表
scene_list:
  - scene_id: "S1"
    beat: "[节拍名]"
    structure_position: "[起/承/転/結]"
    page_range: "P1-P2"
    page_budget: 2
    location: "[场景地点]"
    characters:
      - "hero_001"
      - "heroine_001"
    summary: "[场景概要]"
    emotion_start: "[开始情绪]"
    emotion_end: "[结束情绪]"
    pace: "[快/中/慢]"
    key_moment: "[这个场景最重要的画面]"
    page_turner: "[翻页钩子]"
    dialogue_hints:
      - speaker: "hero_001"
        line: "「[关键台词]」"

  - scene_id: "S2"
    # ... 同上格式

# 角色参考
character_references:
  - id: "hero_001"
    name: "[角色名]"
    role: "[主角/女主角/...]"

    # 视觉简述 (用于分镜描述)
    visual_summary:
      face: "[面部关键特征]"
      build: "[体型]"
      clothing: "[常用服装]"
      distinctive: "[标志性特征]"

    # 表情范围 (用于面板情绪指示)
    expression_range:
      - "[表情1]"
      - "[表情2]"
      - "[表情3]"

    # 说话风格 (用于台词设计)
    speech_style: "[说话风格]"
    signature_phrase: "「[口头禅]」"

    # AI 生成关键词 (用于 prompt-generator)
    ai_keywords: "[manga style keywords]"

  - id: "heroine_001"
    # ... 同上格式

# 世界设定摘要 (用于背景描述)
world_summary:
  setting_type: "[现实/奇幻/科幻]"
  technology_level: "[技术水平]"
  special_rules:
    - "[如有特殊规则]"

  # 关键场景设定 (用于背景绘制)
  key_locations:
    - id: "loc_001"
      name: "[场景名]"
      type: "[室内/室外]"
      atmosphere: "[氛围]"
      visual_keywords:
        - "[关键词1]"
        - "[关键词2]"
      appears_in: ["S1", "S3"]

# 冲突提示 (用于张力设计)
conflict_hints:
  climax_scene: "S[#]"
  climax_description: "[高潮场景描述]"
  tension_curve:
    - scene: "S1"
      tension: 2
    - scene: "S2"
      tension: 4
    # ...

# 伏笔提示 (用于分镜埋设)
foreshadowing:
  - id: "F01"
    content: "[伏笔内容]"
    plant_scene: "S[#]"
    payoff_scene: "S[#]"
```

### 精简输入格式

对于简单项目，可以使用精简格式：

```yaml
# manga-designer 精简输入

project:
  title: "[标题]"
  genre: "[类型]"
  pages: [页数]

scenes:
  - id: "S1"
    pages: "P1-2"
    summary: "[概要]"
    characters: ["hero_001"]
    emotion: "[情绪]"

characters:
  - id: "hero_001"
    name: "[名]"
    look: "[外貌简述]"
    personality: "[性格简述]"

style: "[少年/少女]"
```

---

## prompt-generator 对接格式

### 角色设定图请求

```yaml
# prompt-generator 角色设定图请求
# 由 manga-story-bible Phase 2 生成

request_type: character_design
source: manga-story-bible

character_info:
  character_id: "[角色ID]"
  character_name: "[角色名]"
  role: "[主角/女主角/对手/...]"
  archetype: "[角色原型]"

visual_description:
  # 从角色档案提取的英文描述
  face:
    cn: "[中文面部描述]"
    en: "[English face description]"

  build:
    cn: "[中文体型描述]"
    en: "[English build description]"

  clothing:
    default:
      cn: "[中文服装描述]"
      en: "[English clothing description]"

  distinctive_features:
    cn: "[中文标志特征]"
    en: "[English distinctive features]"

manga_style:
  genre: "[shounen/shoujo]"
  eye_style: "[眼型描述]"
  hair_style: "[发型描述]"
  expression_range:
    - "[表情1]"
    - "[表情2]"
    - "[表情3]"

output_request:
  types:
    - type: "character_sheet"
      description: "三视图: 正面、侧面、背面"
      priority: 1

    - type: "expression_sheet"
      description: "表情集: 6-9种常用表情"
      priority: 2

    - type: "pose_reference"
      description: "动作参考: 3-5个代表性姿势"
      priority: 3

  style_keywords:
    - "manga character sheet"
    - "black and white"
    - "clean lineart"
    - "[shounen/shoujo] style"
    - "multiple views"

  parameters:
    ar: "3:2"
    version: "v7"
    style: "raw"
```

### 世界观概念图请求

```yaml
# prompt-generator 世界观概念图请求
# 由 manga-story-bible Phase 3 生成

request_type: environment_concept
source: manga-story-bible

location_info:
  location_id: "[场景ID]"
  location_name: "[场景名]"
  type: "[室内/室外/自然/人造]"

atmosphere:
  mood: "[氛围描述]"
  lighting: "[光线特点]"
  time_of_day: "[时间]"
  weather: "[天气/条件]"
  colors:
    main: "[主色调]"
    accent: "[强调色]"

visual_elements:
  architecture_style: "[建筑风格]"
  key_elements:
    - "[元素1]"
    - "[元素2]"
  details:
    - "[细节1]"
    - "[细节2]"

emotional_association: "[这个场景与什么情感关联]"
story_scenes: ["S1", "S3", "S5"]

output_request:
  types:
    - type: "exterior_view"
      description: "外景全貌"
      priority: 1

    - type: "interior_view"
      description: "内景"
      priority: 2

    - type: "detail_shot"
      description: "标志性细节特写"
      priority: 3

    - type: "atmosphere_shot"
      description: "氛围图/光影图"
      priority: 4

  style_keywords:
    - "manga background"
    - "[genre] style"
    - "detailed environment"
    - "[氛围关键词]"

  parameters:
    ar: "16:9"  # 背景图常用宽幅
    version: "v7"
```

### 道具设定图请求

```yaml
# prompt-generator 道具设定图请求
# 由 manga-story-bible 生成

request_type: prop_design
source: manga-story-bible

item_info:
  item_id: "[道具ID]"
  item_name: "[道具名]"
  type: "[武器/工具/饰品/...]"
  owner: "[所属角色ID]"

description:
  cn: "[中文描述]"
  en: "[English description]"

visual_details:
  shape: "[形状]"
  size: "[尺寸]"
  material: "[材质]"
  colors: "[颜色]"
  special_features: "[特殊特征]"

story_significance: "[在故事中的意义]"

output_request:
  types:
    - type: "full_view"
      description: "全景多角度"
      priority: 1

    - type: "detail_view"
      description: "细节特写"
      priority: 2

    - type: "scale_reference"
      description: "尺寸参照"
      priority: 3

  style_keywords:
    - "manga prop design"
    - "black and white"
    - "detailed illustration"
    - "multiple angles"

  parameters:
    ar: "1:1"
    version: "v7"
```

---

## 交接流程

### Phase 5 完成后的选项处理

```
用户选择 → 系统响应

1. "启动 /manga-designer"
   → 生成 manga-designer 输入格式
   → 调用 /manga-designer
   → 传入格式化数据
   → manga-designer 从 Phase 3 开始

2. "生成角色设定图"
   → 询问要生成哪个角色
   → 生成 prompt-generator 角色请求格式
   → 调用 /prompt-generator
   → 可选: 继续调用 /generating-images

3. "生成世界观概念图"
   → 询问要生成哪个场景
   → 生成 prompt-generator 场景请求格式
   → 调用 /prompt-generator
   → 可选: 继续调用 /generating-images

4. "生成道具设定图"
   → 询问要生成哪个道具
   → 生成 prompt-generator 道具请求格式
   → 调用 /prompt-generator
   → 可选: 继续调用 /generating-images

5. "导出故事圣经文档"
   → 生成完整故事圣经 Markdown
   → 输出给用户保存
```

### 跨 Skill 调用示例

**调用 prompt-generator**:
```
用户: 我想生成 hero_001 的角色设定图

系统:
1. 从角色档案提取信息
2. 格式化为 prompt-generator 请求
3. 调用 /prompt-generator
4. 传入请求数据
5. prompt-generator 生成提示词
6. 询问是否继续生成图像
```

**调用 manga-designer**:
```
用户: 开始分镜设计

系统:
1. 编译 manga-designer 输入格式
2. 调用 /manga-designer
3. 传入格式化数据
4. manga-designer 加载数据
5. 从 Phase 3 (ネーム制作) 开始
6. 自动加载场景列表和角色档案
```

---

## 版本控制

### 文档版本格式

```markdown
## 版本信息

- 文档版本: v[主版本].[次版本]
- 创建日期: [YYYY-MM-DD]
- 最后修改: [YYYY-MM-DD]
- 状态: [草案/待审/定稿/已弃用]

## 修订历史

| 版本 | 日期 | 修改者 | 修改内容 |
|------|------|--------|----------|
| v1.0 | [日期] | [用户] | 初版创建 |
| v1.1 | [日期] | [用户] | [修改内容] |
```

### 兼容性说明

- manga-designer 输入格式: v1.0 兼容
- prompt-generator 请求格式: v1.0 兼容
- 故事圣经文档: 纯 Markdown，通用兼容

---

## 导出选项

### Markdown 导出
- 默认格式
- 可在任何 Markdown 编辑器查看
- 推荐用于存档和分享

### YAML 导出
- 结构化数据格式
- 用于程序处理
- 用于与其他工具集成

### 打印友好格式
- 简化版本
- 适合打印参考
- 隐藏技术细节
