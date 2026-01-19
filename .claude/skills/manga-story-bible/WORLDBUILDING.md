# 世界观设定框架 (Worldbuilding)

本文档是世界观构建的完整指南，是 SKILL.md Phase 3 的深度参考。涵盖深度评估、三层框架、一致性检查。

---

## 深度评估指南

### 为什么要评估深度？

不是每个故事都需要完整的世界观。过度设定会：
- 浪费创作时间
- 增加记忆负担
- 分散故事焦点
- 导致信息过载

正确的做法是**根据故事需求选择合适的深度**。

### 深度等级

| 等级 | 名称 | 适用类型 | 世界观比重 | 设定工作量 |
|------|------|----------|------------|------------|
| 1 | 最小化 | 日常/校园 | 10% | 1-2页 |
| 2 | 轻度 | 都市奇幻/异能 | 20% | 3-5页 |
| 3 | 中等 | 轻幻想/超能力 | 30% | 6-10页 |
| 4 | 深度 | 异世界/史诗 | 40%+ | 10+页 |

### 深度选择流程图

```
你的故事发生在哪里？
│
├─ 现实世界（基本不变）
│   └─ 深度 1-2：最小化/轻度
│       适用: 恋爱喜剧、日常、校园
│
├─ 现实世界 + 特殊元素
│   └─ 深度 2-3：轻度/中等
│       适用: 异能、都市奇幻、灵异
│
├─ 魔改现实/平行世界
│   └─ 深度 3：中等
│       适用: 近未来、历史if、平行时空
│
└─ 完全架空世界
    └─ 深度 4：深度
        适用: 异世界、魔法世界、遥远未来
```

### 各深度详解

#### 深度 1: 最小化

**适用场景**:
- 高中恋爱喜剧
- 日常系
- 纯人际关系故事

**需要设定**:
```yaml
minimal_worldbuilding:
  # 基本背景
  setting: "[城市/学校名]"
  time_period: "[现代/某年代]"

  # 关键场景
  key_locations:
    - name: "[场景名]"
      atmosphere: "[氛围描述]"

  # 就这些！
```

**不需要设定**: 政治、经济、历史、魔法系统等

#### 深度 2: 轻度

**适用场景**:
- 都市异能
- 学园异能
- 轻度奇幻

**需要设定**:
```yaml
light_worldbuilding:
  # 基本背景
  setting: "[地点]"
  time_period: "[时间]"

  # 特殊元素规则
  special_element:
    name: "[异能/魔法/怪物]"
    source: "[能力来源]"
    basic_rules:
      - "[规则1]"
      - "[规则2]"
    limitations:
      - "[限制1]"

  # 社会认知
  public_awareness: "[知道/不知道/部分知道]"

  # 关键组织（如有）
  organizations:
    - name: "[组织名]"
      role: "[作用]"
```

#### 深度 3: 中等

**适用场景**:
- 超能力战斗
- 魔法学园
- 近未来科幻

**需要设定**: 三层框架的部分内容（见下文）

#### 深度 4: 深度

**适用场景**:
- 异世界冒险
- 史诗奇幻
- 复杂科幻

**需要设定**: 三层框架的完整内容（见下文）

---

## 三层框架

### 框架概述

```
┌─────────────────────────────────────────────────────────────┐
│  Layer 3: 文化细节 (Culture Layer)                          │
│  风俗习惯、语言特点、视觉文化、日常生活                        │
├─────────────────────────────────────────────────────────────┤
│  Layer 2: 社会结构 (Society Layer)                          │
│  权力体系、经济系统、社会阶层、组织势力                        │
├─────────────────────────────────────────────────────────────┤
│  Layer 1: 物理规则 (Physics Layer)                          │
│  能力系统、技术水平、地理环境、生物/种族                       │
└─────────────────────────────────────────────────────────────┘
```

### Layer 1: 物理规则

物理规则是世界的基础，决定"什么是可能的"。

#### 能力系统模板

```yaml
power_system:
  # 系统名称
  name: "[能力系统名称]"

  # 能力来源
  source:
    origin: "[能力从何而来？]"
    # 例: 天生、后天觉醒、获得道具、签订契约
    inheritance: "[能否遗传？]"
    acquisition: "[如何获得？]"

  # 能力类型
  types:
    classification: "[分类方式]"
    # 例: 元素系/强化系/操作系
    categories:
      - name: "[类型1]"
        description: "[描述]"
        examples: ["[例子]"]

  # 能力规则
  rules:
    activation: "[如何发动？]"
    # 例: 咏唱、手势、意念
    fuel: "[消耗什么？]"
    # 例: 魔力、体力、寿命
    recovery: "[如何恢复？]"

  # 限制与代价（重要！）
  limitations:
    hard_limits:
      - "[绝对不能做的事]"
    costs:
      - "[使用能力的代价]"
    weaknesses:
      - "[弱点]"

  # 强弱等级（如有）
  power_levels:
    scale: "[评级系统]"
    # 例: F-S级、1-100等级
    protagonist_level: "[主角初始等级]"
    antagonist_level: "[对手等级]"

  # 故事相关
  story_relevance:
    main_conflict: "[这个系统如何服务于主冲突？]"
    protagonist_power: "[主角的能力是什么？]"
    limitation_for_plot: "[什么限制创造了剧情张力？]"
```

#### 技术水平模板

```yaml
technology:
  # 整体水平
  era: "[技术时代]"
  # 例: 中世纪、蒸汽朋克、现代、近未来

  # 与现实的差异
  differences:
    advanced: ["[比现实先进的技术]"]
    absent: ["[不存在的技术]"]
    unique: ["[独有的技术]"]

  # 日常生活影响
  daily_life:
    transportation: "[交通方式]"
    communication: "[通讯方式]"
    information: "[信息获取方式]"

  # 故事相关
  story_relevance:
    key_technology: "[剧情关键技术]"
    limitation: "[技术限制如何影响剧情]"
```

#### 地理环境模板

```yaml
geography:
  # 世界类型
  world_type: "[单一大陆/多大陆/群岛/...]"

  # 主要区域
  regions:
    - name: "[区域名]"
      climate: "[气候]"
      terrain: "[地形]"
      resources: "[资源]"
      inhabitants: "[居民]"
      story_role: "[在故事中的作用]"

  # 关键地点
  key_locations:
    - name: "[地点名]"
      type: "[类型: 城市/村庄/遗迹/自然]"
      description: "[简述]"
      atmosphere: "[氛围]"
      story_scenes: ["[在这里发生的场景]"]

  # 特殊地理
  special_features:
    - name: "[特殊地点/现象]"
      effect: "[效果/影响]"
```

---

### Layer 2: 社会结构

社会结构决定人们如何组织生活，是角色行为的背景。

#### 权力体系模板

```yaml
power_structure:
  # 政体类型
  government_type: "[君主制/共和/城邦/无政府/...]"

  # 权力层级
  hierarchy:
    - level: 1
      title: "[最高权力者]"
      power: "[权力范围]"
    - level: 2
      title: "[次级权力]"
      power: "[权力范围]"

  # 权力来源
  legitimacy: "[权力合法性来源]"
  # 例: 血统、选举、实力、神授

  # 当前状态
  stability: "[稳定/动荡/内战]"
  current_ruler: "[当前统治者]"
  conflicts: ["[权力斗争]"]

  # 故事相关
  story_relevance:
    protagonist_position: "[主角在权力结构中的位置]"
    conflict_source: "[权力结构如何产生冲突]"
```

#### 社会阶层模板

```yaml
social_classes:
  # 阶层划分
  classes:
    - name: "[阶层名]"
      percentage: "[人口比例]"
      characteristics: "[特征]"
      lifestyle: "[生活方式]"
      mobility: "[能否跨越？]"

  # 阶层关系
  class_dynamics:
    tensions: ["[阶层间的矛盾]"]
    interactions: ["[阶层间如何互动]"]

  # 故事相关
  protagonist_class: "[主角所属阶层]"
  class_conflict: "[阶层如何影响剧情]"
```

#### 组织势力模板

```yaml
factions:
  - name: "[势力名]"

    # 基本信息
    type: "[类型: 国家/组织/秘密结社/...]"
    size: "[规模]"
    influence: "[影响力范围]"

    # 核心
    ideology: "[核心理念/目标]"
    methods: "[行动方式]"
    symbol: "[标志/象征]"

    # 结构
    leadership: "[领导形式]"
    key_figures:
      - name: "[重要人物]"
        role: "[职位]"
        character_id: "[如是故事角色]"

    # 关系
    allies: ["[盟友]"]
    enemies: ["[敌人]"]
    neutral: ["[中立关系]"]

    # 故事相关
    role_in_story: "[在故事中的作用]"
    protagonist_relation: "[与主角的关系]"
```

---

### Layer 3: 文化细节

文化细节让世界有血有肉，但也是最容易过度设定的部分。

#### 核心原则: 只设定会出现的

```
问自己:
□ 这个设定会在故事中出现吗？
□ 角色会提到/体验这个吗？
□ 删除它会影响故事吗？

如果三个都是否 → 不需要设定
如果有一个是 → 简要设定
如果都是是 → 详细设定
```

#### 文化设定模板

```yaml
culture:
  # 风俗习惯（只列与故事相关的）
  customs:
    - name: "[习俗名]"
      description: "[简述]"
      story_appearance: "[在哪个场景出现]"

  # 语言特点（如有特殊设定）
  language:
    unique_terms:
      - term: "[特殊用语]"
        meaning: "[含义]"
        usage: "[使用场景]"
    speech_patterns: "[说话方式特点]"

  # 视觉文化（重要！影响画面）
  visual_culture:
    fashion:
      general_style: "[整体服装风格]"
      class_differences: "[阶层差异]"
      key_items: ["[标志性服饰]"]

    architecture:
      general_style: "[建筑风格]"
      materials: "[主要材料]"
      key_buildings: ["[标志性建筑]"]

    symbols:
      - symbol: "[符号]"
        meaning: "[含义]"
        usage: "[在哪里出现]"

  # 日常生活（选择性设定）
  daily_life:
    food: "[饮食特点]"
    entertainment: "[娱乐方式]"
    education: "[教育方式]"
```

---

## 故事相关性过滤

### 冰山原则

```
呈现给读者的 (10%)
─────────────────────────────────── 水面
创作者知道的 (100%)

原则:
- 创作者应该知道世界的全貌
- 但只呈现故事需要的部分
- 隐藏的设定提供深度感
- 不需要把所有设定都写出来
```

### 相关性检查清单

对每个设定元素问：

```markdown
## 设定相关性检查: [设定名称]

### 出现检查
□ 这个设定在故事中直接出现吗？
  如是 → 需要设定
  如否 → 继续下一个问题

### 影响检查
□ 这个设定影响角色的行为/决策吗？
  如是 → 需要设定
  如否 → 继续下一个问题

### 理解检查
□ 读者需要知道这个才能理解故事吗？
  如是 → 需要设定
  如否 → 可以不设定或极简设定

### 决定
[ ] 详细设定（频繁出现/关键影响）
[ ] 简要设定（偶尔出现/背景影响）
[ ] 不设定（不出现/无影响）
[ ] 脑内设定（创作者知道但不写出）
```

### 设定优先级

| 优先级 | 类型 | 设定深度 | 示例 |
|--------|------|----------|------|
| **必须** | 剧情关键 | 详细 | 主角的能力规则 |
| **重要** | 经常出现 | 中等 | 学校/城市设定 |
| **次要** | 偶尔出现 | 简要 | 次要地点 |
| **背景** | 氛围需要 | 极简 | 大世界背景 |
| **脑内** | 不出现 | 不写 | 你知道就好 |

---

## 一致性检查器

### 物理规则检查

```markdown
## 物理规则一致性检查

### 能力系统检查
□ 主角的能力有明确限制吗？
□ 限制在故事中被遵守了吗？
□ 如果能力可以解决问题，为什么不用？
□ 敌人的能力与主角有差距但可被克服吗？
□ 能力升级有合理的条件吗？

### 技术水平检查
□ 技术水平前后一致吗？
□ 角色的知识符合这个技术水平吗？
□ 有没有"为了方便"出现的超时代技术？

### 地理检查
□ 角色的移动时间合理吗？
□ 地理对剧情有影响吗？
□ 关键场景的地理描述一致吗？
```

### 时间线检查

```markdown
## 时间线一致性检查

### 故事内时间
□ 事件发生的顺序合理吗？
□ 角色的年龄与时间线匹配吗？
□ 季节/时间的描述一致吗？

### 历史时间
□ 过去的事件形成了合理的因果链吗？
□ 历史事件对现在的影响合理吗？
□ 角色对历史的了解符合其背景吗？
```

### 角色知识检查

```markdown
## 角色知识一致性检查

### 信息传播
□ 角色怎么知道这个信息的？
□ 角色应该知道这个信息吗？
□ 信息的传播速度合理吗？

### 技能匹配
□ 角色的技能与其背景匹配吗？
□ 角色学会新技能的过程合理吗？
□ 有"突然会了"的情况吗？

### 世界观认知
□ 角色对世界的理解符合其位置吗？
□ 普通人知道的和秘密组织知道的有区分吗？
□ 角色有不应该知道的信息吗？
```

### 整体一致性检查

```markdown
## 世界观整体一致性检查

### 内部逻辑
□ A规则和B规则不矛盾吗？
□ 社会结构与能力系统匹配吗？
□ 文化与生存环境匹配吗？

### 与角色交叉
□ 世界规则支持角色目标吗？
□ 世界为冲突提供空间吗？
□ 角色背景与世界设定一致吗？

### 与剧情交叉
□ 世界设定不会让剧情变得不可能吗？
□ 世界设定为剧情提供了必要支持吗？
□ 有没有"为了剧情而违反设定"的情况？
```

---

## 场景设计指南

### 关键场景氛围设定

每个重要场景需要视觉记忆点：

```yaml
scene_design:
  name: "[场景名]"

  # 基本信息
  type: "[室内/室外/自然/人造]"
  size: "[规模]"
  function: "[功能/用途]"

  # 氛围设定
  atmosphere:
    mood: "[氛围关键词]"
    lighting: "[光线特点]"
    colors: "[主色调]"
    sounds: "[声音特点]"
    smells: "[气味特点]"

  # 视觉记忆点
  visual_anchors:
    - element: "[标志性元素]"
      description: "[描述]"
      story_meaning: "[故事意义]"

  # 故事功能
  story_scenes: ["[在这里发生的场景]"]
  emotional_association: "[这个场景与什么情感关联]"

  # prompt-generator 对接
  concept_art_keywords:
    - "[关键词1]"
    - "[关键词2]"
```

### 场景类型建议

| 场景类型 | 氛围设定重点 | 视觉记忆点建议 |
|----------|--------------|----------------|
| 学校 | 青春、日常 | 樱花、教室、屋顶 |
| 战场 | 紧张、危险 | 特殊地形、战损痕迹 |
| 秘密基地 | 神秘、安全 | 入口机关、标志性物品 |
| 异世界城市 | 奇幻、壮观 | 独特建筑、魔法元素 |
| 日常场所 | 温馨、平凡 | 生活细节、个人物品 |

---

## prompt-generator 对接

完成世界观设定后，可以生成概念图：

### 世界观概念图请求格式

```yaml
type: environment_concept
location_id: "[场景ID]"
location_name: "[场景名]"

visual_input:
  atmosphere: "[氛围描述]"
  lighting: "[光线]"
  colors: "[色调]"
  key_elements: ["[关键元素]"]
  architectural_style: "[建筑风格]"

mood_keywords:
  - "[关键词1]"
  - "[关键词2]"

output_types:
  - exterior_view    # 外景全貌
  - interior_view    # 内景
  - detail_shot      # 细节特写
  - atmosphere_shot  # 氛围图

style: "manga background, [genre]"
```

---

## 常见世界观模式

### 校园异能

```yaml
pattern: "校园异能"
physics:
  power_system: "觉醒型异能"
  public_awareness: "秘密存在"
  school_role: "培养/管理能力者"
society:
  normal_life: "表面正常的学校生活"
  hidden_layer: "能力者的秘密世界"
  organizations: "学校管理层/敌对组织"
culture:
  dual_identity: "普通学生/能力者"
```

### 异世界转生

```yaml
pattern: "异世界转生"
physics:
  magic_system: "需要完整设计"
  technology: "通常中世纪水平"
  protagonist_cheat: "转生者特权"
society:
  kingdoms: "多国设定常见"
  adventurer_guild: "冒险者公会"
  social_mobility: "通过实力上升"
culture:
  isekai_tropes: "地位系统/技能系统"
```

### 都市奇幻

```yaml
pattern: "都市奇幻"
physics:
  modern_base: "现代社会为基础"
  supernatural: "超自然元素隐藏"
  masquerade: "维持正常表象"
society:
  hidden_world: "裏世界"
  enforcement: "维持秩序的组织"
  balance: "势力平衡"
culture:
  double_life: "日常与非日常"
```

---

## 参考资源

- Brandon Sanderson's Laws of Magic - 能力系统设计
- N.K. Jemisin 世界观构建课程 - 整体框架
- 《Writing Excuses》Worldbuilding 系列 - 实践技巧
