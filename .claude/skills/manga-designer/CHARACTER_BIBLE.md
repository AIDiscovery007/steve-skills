# 角色圣经 (Character Bible)

角色管理系统，用于维护漫画项目中的角色档案、视觉一致性和AI生成参数。

> **深度角色开发**: 如需完整的角色心理架构（Want/Need/Flaw框架）、角色化学反应测试、详细的角色弧线设计，请使用 `/manga-story-bible` 的 Phase 2 角色炼金术系统。
>
> 本文档专注于**分镜制作阶段**所需的角色视觉管理和AI生成参数。

---

## 角色档案模板

### 完整角色档案

```yaml
# ============================================
# 角色档案 - [角色名]
# ============================================

# 基础信息
character_id: "[类型]_[编号]"  # 例: hero_001, heroine_001, rival_001
name: "[中文名]"
name_reading: "[日语读音]"  # 可选，如 "リン・ハオ"
nickname: "[昵称/外号]"  # 可选

# ============================================
# 视觉特征 (Visual Traits)
# ============================================

visual_traits:
  # 面部特征
  face:
    cn: "[中文描述]"
    en: "[English description]"

  # 体型
  build:
    cn: "[中文描述]"
    en: "[English description]"

  # 服装
  clothing:
    default:
      cn: "[默认服装-中文]"
      en: "[Default outfit-English]"
    casual:
      cn: "[便装-中文]"
      en: "[Casual outfit-English]"
    special:
      cn: "[特殊服装-中文]"
      en: "[Special outfit-English]"

  # 标志性特征（重要！用于角色辨识）
  distinctive:
    cn: "[独特记号-中文]"
    en: "[Distinctive features-English]"

# ============================================
# 日漫视觉风格 (Manga Visual Style)
# ============================================

manga_visual:
  # 眼睛风格
  eye_style: "[眼型描述]"
  # 少年漫画: 锐利型、坚定型、热血型
  # 少女漫画: 大眼睛型、闪亮型、温柔型

  # 发型
  hair_style: "[发型描述]"
  # 动态特性: 飘动、刺猬、双马尾等

  # 表情库
  expression_range: "[表情类型范围]"
  # 热血型: 决心、愤怒、惊讶、友情、搞笑
  # 温柔型: 微笑、害羞、惊讶、感动、难过

  # 常用特效
  common_effects:
    - "[效果1]"  # 如: 汗滴、愤怒青筋、感动泪光
    - "[效果2]"

# ============================================
# AI 生成参考 (AI Reference)
# ============================================

ai_reference:
  # 角色参考图URL（生成后填入）
  cref_url: "[Character Reference URL]"

  # 角色权重（建议值）
  cw: 85  # 日漫风格建议 80-90

  # 视觉特征参考URL（跨场景一致性）
  oref_url: "[Object Reference URL]"

  # 风格关键词
  style_keywords: "manga style, black and white, screentone, [shounen/shoujo]"

  # 负面提示词（避免的元素）
  negative: "photorealistic, 3D render, western comic style"

# ============================================
# 角色内核 (Character Core)
# ============================================

personality:
  traits:
    - "[性格特点1]"
    - "[性格特点2]"
    - "[性格特点3]"

  speaking_style: "[说话风格]"
  # 例: 热血、冷静、毒舌、元气、敬语

role: "[故事角色]"  # 主角、女主角、对手、伙伴、导师等

archetype: "[角色原型]"
# 少年漫画原型:
#   - 热血主角（鸣人、路飞型）
#   - 天才主角（夜神月、L型）
#   - 成长主角（炭治郎型）
#   - 宿敌（贝吉塔、佐助型）
#   - 导师（卡卡西型）
#
# 少女漫画原型:
#   - 平凡少女（真�的、透型）
#   - 王子型男主（道明寺型）
#   - 温柔系男主（花�的、由希型）
#   - 青梅竹马
#   - 闺蜜

goal: "[角色目标]"
weakness: "[性格弱点]"
fear: "[恐惧/弱点]"

# ============================================
# 关系网络 (Relationships)
# ============================================

relationships:
  - target: "[角色ID]"
    type: "[关系类型]"  # 朋友、恋人、对手、家人、仇敌
    description: "[关系描述]"
```

---

## 角色原型库

### 少年漫画角色原型

#### 热血型主角

```yaml
archetype: "热血型主角"
personality:
  traits: ["正义感强", "重视伙伴", "永不放弃", "有点笨但努力"]
  speaking_style: "热血、直接、喜欢喊必杀技"
manga_visual:
  eye_style: "锐利型，充满决心"
  expression_range: "决心、愤怒、惊讶、友情感动、搞笑脸"
  common_effects: ["热血背景", "集中线", "青筋"]
goal: "成为最强 / 保护重要的人"
weakness: "冲动、不擅长动脑"
```

**代表**: 孙悟空《龙珠》、路飞《海贼王》、�的鸣人《火影忍者》

#### 天才型主角

```yaml
archetype: "天才型主角"
personality:
  traits: ["聪明绝顶", "冷静", "傲慢或内敛", "有原则"]
  speaking_style: "冷静、分析性、偶尔毒舌"
manga_visual:
  eye_style: "锐利型，洞察一切"
  expression_range: "冷笑、分析、惊讶（少见）、决心"
  common_effects: ["黑暗背景", "智慧光芒"]
goal: "证明自己 / 解决谜题 / 改变世界"
weakness: "过度自信、人际关系"
```

**代表**: 夜神月《死亡笔记》、L《死亡笔记》、工藤新一《名侦探柯南》

#### 成长型主角

```yaml
archetype: "成长型主角"
personality:
  traits: ["善良", "坚韧", "不断成长", "重视家人"]
  speaking_style: "温和但坚定"
manga_visual:
  eye_style: "温和但有力"
  expression_range: "善良、决心、悲伤、愤怒、成长蜕变"
  common_effects: ["成长光芒", "回忆闪回"]
goal: "保护家人 / 达成使命"
weakness: "初期能力不足、过于善良"
```

**代表**: �的炭治郎《鬼灭之刃》、绿谷出久《我的英雄学院》

#### 宿敌/对手

```yaml
archetype: "宿敌型"
personality:
  traits: ["骄傲", "实力强", "有自己的正义", "不服输"]
  speaking_style: "傲慢、挑衅、后期可能温和"
manga_visual:
  eye_style: "锐利、挑衅"
  expression_range: "傲慢、愤怒、惊讶、(隐藏的)尊重"
  common_effects: ["对峙分割线", "力量对比"]
goal: "超越主角 / 证明自己"
weakness: "骄傲、孤独"
```

**代表**: 贝吉塔《龙珠》、佐助《火影忍者》、爆豪《我的英雄学院》

### 少女漫画角色原型

#### 平凡少女主角

```yaml
archetype: "平凡少女主角"
personality:
  traits: ["善良", "普通但努力", "内心坚强", "有点笨拙"]
  speaking_style: "元气、真诚、偶尔紧张结巴"
manga_visual:
  eye_style: "大而闪亮、纯真型"
  expression_range: "元气、害羞、惊讶、感动落泪、生气可爱"
  common_effects: ["花瓣飘落", "脸红", "心形效果"]
goal: "找到自我 / 获得真爱"
weakness: "不够自信、容易误会"
```

**代表**: 真琴《水果篮子》、园子《邻家怪物同学》

#### 王子型男主

```yaml
archetype: "王子型男主"
personality:
  traits: ["傲慢(表面)", "专一", "家世好", "有温柔一面"]
  speaking_style: "命令式、毒舌、偶尔温柔(反差)"
manga_visual:
  eye_style: "锐利、帅气"
  expression_range: "傲慢、温柔(反差)、吃醋、保护欲"
  common_effects: ["闪光背景", "玫瑰花瓣"]
goal: "得到真爱 / 突破家族束缚"
weakness: "傲慢、不善表达"
```

**代表**: 道明寺《花样男子》、夜天《守护甜心》

#### 温柔系男主

```yaml
archetype: "温柔系男主"
personality:
  traits: ["温柔", "体贴", "有秘密", "默默守护"]
  speaking_style: "温和、体贴、有礼貌"
manga_visual:
  eye_style: "温柔、柔和"
  expression_range: "微笑、温柔、偶尔认真、隐藏的痛苦"
  common_effects: ["柔和光芒", "花朵背景"]
goal: "守护重要的人 / 获得救赎"
weakness: "过于压抑自己、有黑暗过去"
```

**代表**: 由希《水果篮子》、花�的（花沢類）《花样男子》

---

## 角色视觉一致性管理

### 使用 --cref (Character Reference)

角色参考图用于保持同一角色在不同场景中的视觉一致性。

**生成角色参考图流程**:

1. **设计角色设定图**
   ```
   调用 prompt-generator:
   输入: 角色档案 visual_traits + manga_visual
   添加: "manga character sheet, multiple views, front view, side view,
          3/4 view, expression sheet, black and white, clean lineart"
   参数: --ar 3:2 --v 7 --style raw
   ```

2. **生成并选择最佳参考**
   ```
   生成 4 张变体
   选择最符合角色设定的图像
   保存 URL 至角色档案 ai_reference.cref_url
   ```

3. **在面板生成中使用**
   ```
   每个包含该角色的面板提示词添加:
   --cref [cref_url] --cw [weight]
   ```

**--cw 权重建议**:

| 权重范围 | 效果 | 适用场景 |
|----------|------|----------|
| 90-100 | 极高一致性 | 特写镜头、角色识别关键帧 |
| 80-90 | 高一致性 | 标准场景、对话镜头 |
| 60-80 | 中等一致性 | 动作场景（允许动态变形） |
| 40-60 | 低一致性 | 远景、剪影、特殊效果 |

### 使用 --oref (Object Reference)

用于保持非面部视觉特征的一致性（服装、道具、标志等）。

**适用场景**:
- 角色标志性服装
- 魔法道具/武器
- 徽章/标志

**使用方法**:
```
--oref [object_url] --ow [weight]
```

---

## 角色关系图模板

### 文字描述格式

```markdown
## 角色关系图

### 核心三角
[hero_001] 林浩 ←──恋爱──→ [heroine_001] 苏雨晴
                    │
                    │ 竞争/宿敌
                    ↓
            [rival_001] 陈志远

### 伙伴关系
[hero_001] ←──挚友──→ [friend_001] 王磊
[heroine_001] ←──闺蜜──→ [friend_002] 小雪

### 导师关系
[hero_001] ←──师生──→ [mentor_001] 老师
```

### 视觉关系图

```
           [mentor_001]
              │ 师生
              ↓
[rival_001] ←竞争→ [hero_001] ←挚友→ [friend_001]
    │               │
    │ 暗恋?         │ 恋爱
    └─────────→[heroine_001]←闺蜜→ [friend_002]
```

---

## 角色档案示例

### 少年漫画主角示例

```yaml
character_id: hero_001
name: "林浩"
name_reading: "リン・ハオ"
nickname: "阿浩"

visual_traits:
  face:
    cn: "锐利眼神, 浓眉, 坚定表情, 下巴有小伤疤"
    en: "sharp eyes, thick eyebrows, determined expression, small scar on chin"
  build:
    cn: "精瘦运动型, 175cm, 肌肉线条明显"
    en: "lean athletic build, 175cm, visible muscle definition"
  clothing:
    default:
      cn: "黑色校服西装外套, 白衬衫, 领带松散, 运动鞋"
      en: "black school blazer, white shirt, loosened tie, sneakers"
    casual:
      cn: "连帽卫衣, 牛仔裤"
      en: "hoodie, jeans"
  distinctive:
    cn: "右手腕总是戴着红色手环, 下巴小伤疤"
    en: "always wears red wristband on right wrist, small chin scar"

manga_visual:
  eye_style: "锐利型，充满决心，瞳孔较小"
  hair_style: "黑色刺猬头，向上刺起，战斗时随风飘动"
  expression_range: "决心、愤怒、惊讶、友情感动、搞笑脸（被打脸时）"
  common_effects:
    - "热血时：集中线 + 背景燃烧"
    - "愤怒时：青筋 + 黑暗阴影"
    - "搞笑时：简笔脸 + 汗滴"

ai_reference:
  cref_url: "[待生成]"
  cw: 85
  oref_url: "[待生成 - 红色手环]"
  style_keywords: "manga style, black and white, screentone, shounen, dynamic"
  negative: "photorealistic, 3D, soft"

personality:
  traits:
    - "正义感极强"
    - "重视伙伴超过一切"
    - "永不放弃"
    - "有点笨但非常努力"
  speaking_style: "热血直接，喜欢用「绝对」「一定」，激动时会大喊"

role: "主角"
archetype: "热血型主角"
goal: "保护青梅竹马，打败威胁城市的黑暗组织"
weakness: "冲动，不擅长动脑，容易被激将"
fear: "失去重要的人"

relationships:
  - target: "heroine_001"
    type: "青梅竹马/恋爱对象"
    description: "从小一起长大，互相喜欢但没说破"
  - target: "rival_001"
    type: "宿敌/竞争"
    description: "能力相当的对手，互相看不顺眼但内心尊重"
  - target: "friend_001"
    type: "挚友"
    description: "最好的朋友，搞笑担当，总是支持主角"
```

### 少女漫画女主角示例

```yaml
character_id: heroine_001
name: "苏雨晴"
name_reading: "スー・ユーチン"
nickname: "小晴"

visual_traits:
  face:
    cn: "圆脸, 大眼睛, 柔和表情, 嘴角有小痣"
    en: "round face, large eyes, gentle expression, small mole near mouth"
  build:
    cn: "娇小可爱型, 158cm, 纤细"
    en: "petite cute type, 158cm, slender"
  clothing:
    default:
      cn: "白色水手服, 红色蝴蝶结, 百褶裙, 白色袜子"
      en: "white sailor uniform, red ribbon, pleated skirt, white socks"
    casual:
      cn: "碎花连衣裙, 小外套"
      en: "floral dress, cardigan"
  distinctive:
    cn: "粉色发卡（母亲遗物）, 总是带着的小熊挂件"
    en: "pink hair clip (mother's memento), teddy bear charm always carried"

manga_visual:
  eye_style: "大而闪亮型，多重高光，眼睛占脸部比例大"
  hair_style: "及肩黑色长发，微波浪卷，刘海柔软"
  expression_range: "元气微笑、害羞脸红、惊讶（眼睛更大）、感动落泪、生气（可爱型）"
  common_effects:
    - "心动时：花瓣飘落 + 脸红"
    - "害羞时：冒蒸汽 + 心形"
    - "感动时：闪亮泪光 + 柔光背景"

ai_reference:
  cref_url: "[待生成]"
  cw: 85
  oref_url: "[待生成 - 粉色发卡]"
  style_keywords: "manga style, black and white, shoujo, soft, sparkles"
  negative: "photorealistic, harsh shadows, masculine"

personality:
  traits:
    - "善良体贴"
    - "外表温柔内心坚强"
    - "有点笨拙但很努力"
    - "喜欢照顾人"
  speaking_style: "温柔有礼，紧张时说话会结巴，喜欢用「嗯...」「那个...」"

role: "女主角"
archetype: "平凡少女主角"
goal: "找到真爱，成为能够帮助他人的人"
weakness: "不够自信，容易误会，太在意他人看法"
fear: "被抛弃，失去母亲的遗物"

relationships:
  - target: "hero_001"
    type: "恋爱对象"
    description: "暗恋对方多年，不敢表白"
  - target: "rival_001"
    type: "被追求"
    description: "被对方追求但没有心动"
  - target: "friend_002"
    type: "闺蜜"
    description: "最好的朋友，什么都聊"
```

---

## 角色管理最佳实践

### 命名约定

| 角色类型 | ID格式 | 示例 |
|----------|--------|------|
| 主角 | hero_XXX | hero_001, hero_002 |
| 女主角 | heroine_XXX | heroine_001 |
| 对手/宿敌 | rival_XXX | rival_001 |
| 伙伴 | friend_XXX | friend_001, friend_002 |
| 导师 | mentor_XXX | mentor_001 |
| 反派 | villain_XXX | villain_001 |
| 配角 | support_XXX | support_001 |

### 视觉一致性检查清单

```markdown
□ 发型在所有场景保持一致
□ 标志性特征（伤疤、饰品等）始终存在
□ 服装与设定匹配
□ 眼睛风格统一
□ 身材比例一致
□ 表情与角色性格匹配
```

### 提示词生成规则

角色面板提示词构成：

```
[基础画面描述] +
[角色 visual_traits.en] +
[manga_visual 效果] +
[场景适配调整] +
--cref [cref_url] --cw [weight]
```

示例：
```
manga panel, medium shot, angry expression,
young man with spiky black hair, sharp determined eyes,
small scar on chin, red wristband on right wrist,
school blazer with loosened tie, clenched fist,
speed lines, focus lines, dramatic shading,
shounen manga style, black and white, high contrast
--ar 3:4 --v 7 --cref [hero_001_cref_url] --cw 85 --style raw
```
