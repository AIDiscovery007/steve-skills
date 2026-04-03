# Plugin Publishing Know-How

这份文档沉淀 `steve-skills` 的 plugin 发布经验，目标是让下次发布时直接照着做，不再重复踩坑。

## 当前发布对象

- Marketplace repo: `AIDiscovery007/steve-skills`
- Marketplace name: `skent-skills`
- Plugin name: `skent-skills`
- Canonical skills path: `skills/skent-*`
- 用户安装后调用方式：`/skent-skills:<skill-name>`

示例：

```text
/skent-skills:skent-gold-analyst
/skent-skills:skent-session-reflect
```

## 必备文件

发布前必须同时存在以下两个文件：

1. `.claude-plugin/marketplace.json`
2. `.claude-plugin/plugin.json`

缺少 `plugin.json` 时，用户可能会遇到下面这种假成功：

- marketplace 能添加
- plugin 能安装
- 但 skills 不会注册出来

这是这次发布里踩到的最关键的坑。

## 版本规则

- `.claude-plugin/plugin.json` 的 `version` 要更新
- `.claude-plugin/marketplace.json` 的 `metadata.version` 要更新
- `.claude-plugin/marketplace.json` 里对应 plugin entry 的 `version` 也要更新

建议三处始终保持一致。

## 发布前 Checklist

### 1. 确认 skill 边界

- 只有第一方 `skills/skent-*` 进入 marketplace
- 第三方 skill 不进入 marketplace
- `.claude/skills/` 可以保留兼容层，但不是发布清单来源

### 2. 确认 manifest 完整

检查：

```text
.claude-plugin/plugin.json
.claude-plugin/marketplace.json
```

重点检查：

- plugin 名称是否仍是 `skent-skills`
- `skills` 列表是否只包含 `./skills/skent-*`
- 版本号是否同步 bump

### 3. 校验 manifest

```bash
claude plugin validate .
```

必须通过后再继续。

### 4. 本地隔离安装验证

不要只看文件结构，要真的装一次。

```bash
TMP_HOME="$(mktemp -d)"
XDG_DIR="$TMP_HOME/.config"
mkdir -p "$XDG_DIR"

HOME="$TMP_HOME" XDG_CONFIG_HOME="$XDG_DIR" \
  claude plugin marketplace add "/absolute/path/to/steve-skills" --scope user

HOME="$TMP_HOME" XDG_CONFIG_HOME="$XDG_DIR" \
  claude plugin install "skent-skills@skent-skills"
```

至少验证：

- 安装成功
- 版本号符合预期
- 缓存目录里存在 `.claude-plugin/plugin.json`

### 5. 技能注册验证

直接调用一个 plugin skill，确认不再是 “plugin 装了但 skill 不存在”。

```bash
claude --plugin-dir "/absolute/path/to/steve-skills" \
  -p "/skent-skills:skent-session-reflect" \
  --permission-mode bypassPermissions
```

只要不报 `Unknown skill`，说明 plugin skill 已经注册成功。

### 6. 推送到 GitHub

```bash
git push origin main
```

如果远端分叉：

- 先 `git fetch origin`
- 再 `git rebase origin/main`
- 解决冲突后继续
- 不要强推 `main`

### 7. 远端安装验证

推送后，再用 GitHub 源做一次真验证。

推荐用 HTTPS：

```bash
TMP_HOME="$(mktemp -d)"
XDG_DIR="$TMP_HOME/.config"
mkdir -p "$XDG_DIR"

HOME="$TMP_HOME" XDG_CONFIG_HOME="$XDG_DIR" \
  claude plugin marketplace add "https://github.com/AIDiscovery007/steve-skills.git" --scope user

HOME="$TMP_HOME" XDG_CONFIG_HOME="$XDG_DIR" \
  claude plugin install "skent-skills@skent-skills"
```

## 用户安装说明

如果用户机器上没有配置 GitHub SSH，优先让用户用 HTTPS 添加 marketplace：

```text
/plugin marketplace add https://github.com/AIDiscovery007/steve-skills.git
/plugin install skent-skills@skent-skills
```

注意：

- 两条命令要分开执行
- 不要把 `/plugin marketplace add ...` 和 `/plugin install ...` 粘成一条

## 常见故障

### 1. Plugin 安装成功，但看不到 skills

优先检查：

- `.claude-plugin/plugin.json` 是否存在
- marketplace 和 plugin 版本是否已经 bump
- 用户是否执行了 `plugin update` 或重新安装
- 用户是否在用 namespaced skill 名称

正确调用方式：

```text
/skent-skills:skent-gold-analyst
```

不是：

```text
/skent-gold-analyst
```

### 2. `owner/repo` 安装时报 SSH 权限错误

报错通常类似：

```text
Permission denied (publickey)
```

原因：当前 Claude / git 环境把 `owner/repo` 解析成了 SSH。

解决：改用 HTTPS。

```text
/plugin marketplace add https://github.com/AIDiscovery007/steve-skills.git
```

### 3. Plugin 版本没有更新

检查三处版本是否一致：

- `.claude-plugin/plugin.json`
- `.claude-plugin/marketplace.json` -> `metadata.version`
- `.claude-plugin/marketplace.json` -> `plugins[0].version`

### 4. 本地测试能用，远端安装不行

优先排查：

- 有没有忘记 `git push`
- 远端默认分支是不是 `main`
- 本地测试用的是目录源，远端测试要再用 GitHub 源复验一次

## 推荐发布流程

```text
改 skill / 改 manifest
  -> bump version
  -> claude plugin validate .
  -> 本地隔离安装测试
  -> skill 注册测试
  -> git push origin main
  -> 远端 HTTPS 安装测试
  -> 通知用户 update / install
```

## 这次发布的关键经验

- 只有 `marketplace.json` 不够，`plugin.json` 也必须有
- plugin 安装成功不等于 skills 已注册成功
- 一定要做“真实安装 + 真实调用”验证，而不是只看仓库文件
- 用户侧最稳妥的 marketplace 添加方式是 HTTPS
- plugin skill 默认带命名空间，调用格式是 `/skent-skills:<skill-name>`
