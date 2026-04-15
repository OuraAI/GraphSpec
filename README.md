# GraphSpec

> 可交互的架构态势感知工具 —— 让 AI 和开发者都能从宏观全貌逐步下钻到微观细节

这不是又一个"代码可视化工具"，也不是把依赖关系画成图就完事的花架子。

GraphSpec 想解决的是一个很具体的痛点：**AI 的上下文有限，改一个功能的时候它看不到全貌。**

开发者需要一种方式，让自己和 AI 都能从一个宏观全貌逐步下钻到微观细节——不是暴力地把所有信息塞进去，而是**按需加载、渐进披露**。

## 这个项目到底在做什么

GraphSpec 想做的，是把"架构态势感知"从"人脑记住项目结构"这种不可靠的状态，变成一套可交互、可查询、可喂给 AI 的工程资产。

具体来说：

- **对人**：启动一个本地可视化服务，把项目架构渲染成可交互的图表，支持从模块到文件、从依赖到调用链的逐层下钻
- **对 AI**：提供一套 MCP Server，让 AI 能按需读取架构信息，而不是盲猜或者把整个仓库塞进上下文

## 当前进度

**V0.1** - 起盘阶段（规范已立，代码仍是骨架）

| 模块 | 当前状态 | 说明 |
| --- | --- | --- |
| CLI | 骨架占位 | 仅保留可执行入口与 hello world 级别占位输出 |
| Core | 骨架占位 | 仅保留包入口与最小占位 API |
| Web | 骨架占位 | 仅保留包入口与最小占位 API |
| 项目基建 | 已完成 | GitHub 配置、AGENTS.md、README.md、OpenSpec change、workspace 骨架 |

如果只看仓库现状，可以把它理解成：**规范和仓库骨架已经搭好，真实功能开发还没有开始。**

## 技术栈

- **运行时**: Bun
- **语言**: TypeScript
- **Lint/Format**: OXC

## 仓库结构

```
GraphSpec/
├── .github/                    # GitHub 配置
│   ├── ISSUE_TEMPLATE/         # Issue 模板
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── labels.yml              # 标签配置
├── .graphspec/                 # [待实现] 架构数据目录
├── openspec/                   # OpenSpec 规范目录
│   ├── config.yaml             # 项目配置
│   ├── specs/                  # 规范源
│   ├── changes/                # 变更提案
│   └── explorations/           # 探索性规范
├── packages/                   # [待实现] 代码包
│   ├── cli/                    # CLI 工具
│   ├── core/                   # 核心引擎
│   └── web/                    # Web 可视化
├── AGENTS.md                   # AI Agent 协作指南
├── README.md                   # 本文件
└── LICENSE                     # MIT License
```

## 本地开发

```bash
# 克隆仓库
git clone https://github.com/OuraAI/GraphSpec.git
cd GraphSpec

# 安装依赖
bun install

# 验证命令
bun test      # 运行测试
bun run lint      # 运行 lint 检查
bun run typecheck # 类型检查

# 占位入口
bun run graphspec
```

## 模块说明

### CLI (`packages/cli/`)
- **职责**: 命令行入口，用户交互
- **当前状态**: 仅占位入口
- **依赖**: `@graphspec/core`、`@graphspec/web`

### Core (`packages/core/`)
- **职责**: 核心解析和数据处理
- **当前状态**: 仅占位 API
- **接口**: TypeScript API

### Web (`packages/web/`)
- **职责**: 本地可视化服务
- **当前状态**: 仅占位 API

## 开发路线

GraphSpec 遵循渐进式起盘方式，从最小起点开始，根据实际需求逐步扩展。

### 近期目标
- [x] OpenSpec change 与实现任务拆解
- [x] workspace / package 骨架搭建
- [ ] `init` 命令实现
- [ ] `view` 命令实现
- [ ] 本地可视化页面

### 中期方向
- 架构图的 AI 读写能力（MCP Server）
- 渐进式披露策略设计
- 护栏机制（人类确认、变更审计）

### 远期愿景
- 云端服务支持
- 多端 AI 接入形态
- Issue → Spec → 架构 → 代码 的完整链路

## 协作说明

如果准备直接改仓库内容，先看这几个文件：

- `AGENTS.md`：最重要，里面有 AI 协作规范、护栏机制、Local Instruction Precedence
- `README.md`：项目说明与当前进度

另外有几个约定最好别漏：

- Commit message 使用 Angular 规范，Scope: `cli`, `core`, `web`, `docs`
- 架构层面的变更需要人工确认
- 删除代码超过 100 行需要人工确认
- 创建 GitHub 开发 issue 时，优先使用 `.github/ISSUE_TEMPLATE/dev_task.md`
- 如果由 AI 代创建 issue，优先使用 `.agents/skills/gh-issue-driven/SKILL.md`
- 如果由 AI 接手解决 issue，优先使用 `.agents/skills/gh-issue-delivery/SKILL.md`
- 创建 GitHub 开发 issue 前，先同步 `.github/labels.yml`，并确保 issue 至少带上 `type`、`priority`、`status`
- 仓库脚本默认用 `python`；只有薄胶水才用 `shell`，强依赖仓库 TS 逻辑时才用 `bun/ts`

## 相关链接

- [Issue 模板](./.github/ISSUE_TEMPLATE/) - Bug 报告、功能请求等
- [开发 issue skill](./.agents/skills/gh-issue-driven/SKILL.md) - 用 gh CLI 按 IssueDriven 方式创建开发 issue
- [issue 解决 skill](./.agents/skills/gh-issue-delivery/SKILL.md) - 先在规划模式收敛 issue、产出可审核 spec、审核后再实现
- [脚本选型 skill](./.agents/skills/script-strategy/SKILL.md) - 决定脚本该用 shell、python 还是 bun/ts
- [标签配置](./.github/labels.yml) - GitHub issue / PR 标签定义
- [PR 模板](./.github/PULL_REQUEST_TEMPLATE.md) - Pull Request 规范

## License

MIT License - 详见 [LICENSE](./LICENSE)
