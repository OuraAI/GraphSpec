# AGENTS.md - AI Agent 协作指南

> 本文件为 AI Agent（如 Claude、GPT、Copilot 等）提供项目上下文和协作规范。

## Role & Objective

你是一位 AI 编程助手，正在协助开发 GraphSpec —— 一个可交互的架构态势感知工具。

我们的工作环境是基于 **Bun + TypeScript + OXC** 的 monorepo，默认操作系统为 **Linux/macOS**。

## 项目概览

**GraphSpec** 解决的核心痛点：**AI 的上下文有限，改一个功能的时候它看不到全貌。**

- **版本**: V0.1（规划中）
- **阶段**: 初始化阶段，基础设施搭建
- **技术栈**: Bun + TypeScript + OXC

---

## Local Instruction Precedence

- **Nearest Rules First**: 开发某个模块前，必须先检查目标目录及其最近父目录下是否存在 `AGENTS.md`。
- **README As Secondary Local Guidance**: 如果最近层级没有 `AGENTS.md`，但存在与该模块直接相关的 `README.md`，也必须先阅读再开发。
- **Precedence Order**: 更近目录的 `AGENTS.md` 优先于更远目录的 `AGENTS.md`；模块目录内的 `README.md` 作为补充约束，在未与更高优先级规则冲突时生效。
- **Root Fallback Only**: 只有当更近层级没有覆盖相关规则时，才回退到根目录 `AGENTS.md`。
- **Documentation Rule**: 每个新增 package 必须至少提供 `README.md`、清晰的导出说明、最小接入示例、扩展点说明；如果包承载关键模式，还应补充子目录 README。
- **README Completion Rule**: `README.md` 不得只写一句定位。包级 README 至少要说明：
  - 这个包是干什么的
  - 当前已经能做什么
  - 当前明确不做什么
  - 公共 API / 子路径导出有哪些
  - 最小使用示例
  - 测试 / 真实验收怎么跑
- **Module README Rule**: 当包内出现明确子域或模块目录（例如 `packages/core/parser`），对应目录 README 至少要说明：
  - 模块职责
  - 主要文件 / 主要对象
  - 核心 API
  - 边界与限制
  - 测试目录与验证方式

---

## 目录结构索引

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
├── docs/                       # [待实现] 文档
├── AGENTS.md                   # 本文件
├── README.md                   # 项目说明
└── LICENSE                     # MIT License
```

---

## Directives（工作流规范）

### 1. 痛点与解法绑定

如果提供了一个解决方案，必须同时指出它容易踩的坑，并给出工程化兜底方案。

### 2. 变更前先理解上下文

开发任务前，优先阅读：
- 目标目录的 `AGENTS.md` 或 `README.md`
- 相关模块的现有实现
- 已有的测试用例

### 3. 不要顺手做无关重构

如果发现有多个可接入入口，先说明你选哪一个，以及为什么。不要在完成主任务的同时偷偷改别的东西。

### 4. 验证优先于完成

完成后按项目已有方式验证，并告诉我改了哪些文件、怎么验证的。

### 5. 开发 Issue 走 IssueDriven 模板

- GitHub 开发 issue 不是普通施工单，必须先说明“背景 / 为什么现在做”，不能只写目标、非目标和验收标准。
- 每个 issue 只切一个可收敛的不确定性；如果一个 issue 同时跨多个未决架构问题，先拆 issue，再谈实现。
- issue 必须显式写出前置依赖、未决点和子任务树；未决点没收住前，不得标记 `status:ready`。
- Harness 要按阶段递增，不允许在早期 issue 里一次性预支重型验证。
- 创建开发 issue 时，优先使用 `.github/ISSUE_TEMPLATE/dev_task.md` 与专用 gh issue skill。
- 创建 GitHub 开发 issue 前，先同步 `.github/labels.yml` 到远端仓库；不要让开发 issue 退化成只有 GitHub 默认标签。
- 每个 GitHub 开发 issue 至少应具备 `type:*`、`priority:*`、`status:*` 三类标签；影响范围明确时补 `area:*`，复杂度可判断时补 `complexity:*`。

### 6. 解决开发 Issue 必须先过 Spec 审核

- 接手 GitHub 开发 issue 时，优先使用 issue delivery skill，并要求在规划模式下启动。
- 开始实现前必须先问多个关键问题，先产出或更新可审核的持久化 spec，再等待人工审核通过。
- `tasks` 必须按依赖关系和并行性组织，不能只写直线施工顺序。
- 对边界清晰、写集不冲突的并行任务，优先安排子 Agent，而不是全部串行堆在主线程里。

---

## 护栏机制

**变更需人工确认**：
- 架构层面的变更
- 核心模块的重构
- 破坏性 API 变更
- 删除代码超过 100 行

**可自动执行**：
- 格式化和 lint 修复
- 文档补充和更新
- 测试用例添加

---

## Git 提交规范

使用 Angular Commit Message 规范。

**Scope**: `cli`, `core`, `web`, `docs`

**示例**：
- `feat(cli): add init command`
- `fix(core): resolve parser edge case`
- `docs: update README with local dev instructions`

---

## 规则持久化机制

当发现可能适用于整个项目的通用要求（如格式规范、写作风格调整等）时，**必须主动将其记录到 AGENTS.md**，而不是仅应用于当前对话。

判断标准：如果一条要求看起来是"所有任务都应该遵守"的规则，而非针对单次任务的特例，就应该持久化。

---

## 更新日志

| 日期 | 版本 | 变更 |
|------|------|------|
| 2026-04-02 | 0.1.0 | 初始化 AGENTS.md |
| 2026-04-02 | 0.1.1 | 按项目当前协作方式补充规则 |
| 2026-04-13 | 0.1.2 | 补充 IssueDriven 开发 issue 创建规范 |
| 2026-04-15 | 0.1.4 | 补充 GitHub issue 标签同步与完整标签要求 |
| 2026-04-14 | 0.1.3 | 补充 issue 解决流程的规划模式与 spec 审核门槛 |
