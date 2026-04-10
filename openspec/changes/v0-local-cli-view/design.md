## 上下文

当前仓库已经有项目定位、技术栈和 OpenSpec 基础设施，也已经有一个最小 workspace 骨架，但还没有正式进入真实功能实现。问题不在于“怎么尽快把依赖图代码写出来”，而在于先把 GraphSpec 的上位定位和演进路径钉住，否则它很容易退化成一个孤立的可视化 demo。

GraphSpec 的合理位置，不是和 OpenSpec 竞争同一层职责，而是成为它的互补层：

- **OpenSpec** 更适合承载 proposal、design、tasks、acceptance、change history 这些文本化和流程化资产。
- **GraphSpec** 更适合承载结构关系、影响半径、架构草稿、图级变更和空间化浏览。

如果把两者放在一起看，理想链路不是 `Issue -> Code`，也不是 `Spec -> Code`，而是：

`Issue -> Spec -> Graph -> Code -> Validation`

其中 `Graph` 不是文档附图，而是一份可查询、可演化、未来还能被 AI 调用的工程资产。

这意味着 Phase 1 不能只考虑“先做个图”。它还必须为后续两件事留出生长路径：

1. Graph 能被显式编辑，而不是永远只能被代码扫描结果覆盖。
2. AI 能通过低噪声、可治理的执行入口使用 GraphSpec，而不是靠 prompt 描述去“想象架构”。

## 目标 / 非目标

**Goals:**

- 固定 GraphSpec 与 OpenSpec 的职责分层，避免产品定位从一开始就发虚。
- 用一个足够小的 Phase 1 起点打通第一条真实闭环：本地生成 graph、查看 graph、回答基本影响半径问题。
- 保留后续演进路径：从 read-only graph 走向 writable CLI，再走向 Skill 封装和更深的 OpenSpec 桥接。
- 保持规划粗粒度，让后续 issue-driven / spec-driven 工作流可以按阶段继续细化，而不是现在一次性写死所有细节。

**Non-Goals:**

- 不在这次 change 里细化 Phase 2 以后的完整命令协议、数据模型和交互细节。
- 不在这次 change 里把 GraphSpec 直接扩成 MCP Server、桌面端或云服务。
- 不把 GraphSpec 规划成 OpenSpec 的替代品，也不要求它在 Phase 1 就承担 spec 编排职责。
- 不在 Phase 1 引入复杂语义架构理解、业务域自动识别或多语言统一图模型。

## 关键决策

### 1. GraphSpec 被定义为 OpenSpec 的互补控制面，而不是替代品

- 决定：GraphSpec 的主要职责是承载架构上下文、结构浏览和可操作 graph；OpenSpec 继续负责变更提案、设计推演、任务分解和验收口径。
- 原因：如果两者职责重叠，项目会同时维护两套半吊子的规格系统；分层清楚后，GraphSpec 才能专注解决 OpenSpec 难以覆盖的结构认知问题。
- 备选方案：
  - 让 GraphSpec 直接替代 OpenSpec：会把项目拖回“重新造一个 spec framework”的方向。
  - 完全切断两者关系：会失去 `Issue -> Spec -> Graph -> Code` 这条更完整的控制链路。

### 2. 演进路径采用 CLI-first，而不是直接跳到 MCP 或 Agent 写入

- 决定：产品路线按 `read-only CLI/view -> writable CLI -> Skill 封装 -> MCP/更多 AI 接入` 递进。
- 原因：CLI 是最低噪声、最低开发成本、最容易验证和治理的执行面。先把 CLI 做稳，再让 Skill 调 CLI，比一开始就上 MCP 或直接做 agent 写入更稳妥。
- 备选方案：
  - 直接上 MCP：长期正确，但起步成本高，调试面更复杂。
  - 直接让 Skill 写文件：短期快，但会绕过稳定命令面，后续很难治理。

### 3. Phase 1 只交付只读 graph 闭环，但必须为“可写 graph”预留边界

- 决定：当前 change 仍然只规格化 Phase 1，也就是 `graphspec init [path]`、`graphspec view` 和 `.graphspec/graph.json` 这条只读链路。
- 原因：GraphSpec 的第一价值必须是“把结构看清楚”，否则后续写入和 AI 操作都没有可靠对象可依赖。
- 额外约束：Phase 1 的快照、ID、API 设计必须避免把未来 graph edit 路径完全堵死。

### 4. Graph 的“可写”不等于直接改源码，而是先引入独立的 graph 操作面

- 决定：未来 Phase 2/3 的 graph editing 优先面向 GraphSpec 自己的 graph 资产和命令面，而不是一上来就承诺“改 graph 就同步改源码”。
- 原因：如果 graph write 一开始就绑定代码改写，复杂度会陡增，护栏和回滚也会一起失控。先让 graph 成为可编辑草稿和架构意图层，更符合 GraphSpec 的定位。
- 备选方案：
  - graph edit 直接联动代码改写：吸引人，但风险和歧义都太高。
  - 永远只做只读图：无法承接“AI 通过 Skill 调用 CLI 编辑 graph”的产品方向。

### 5. GraphSpec 与 OpenSpec 的第一桥接目标是“一致性与校验”，不是“文档替代”

- 决定：后续 GraphSpec 接入 OpenSpec 时，优先做的是结构一致性检查、架构草稿辅助和 issue/spec/graph/code 对照，而不是把 proposal/design/tasks 本身搬到 graph 里。
- 原因：文本约束和图结构是两种不同资产。最有价值的桥接方式，是让它们互相校验和互相增信，而不是互相吞并。
- 备选方案：
  - 把 spec 全图化：表达能力会下降，维护成本更高。
  - 让 graph 与 spec 完全无关：会失去项目主线价值。

### 6. 当前 change 主要服务于后续 issue 切分，而不是直接全量实施

- 决定：当前 change 的 `tasks.md` 采用“issue backlog seed”写法，优先帮助团队后续创建多个聚焦 issue，而不是把全部实现步骤线性排成一张施工单。
- 原因：你已经明确不会直接把一份 proposal 交给 AI 大推实现，而是会通过多轮 AI 对话、多人接手和 issue-driven 的方式逐步推进。那这份 change 最有价值的产出，就应该是“好切 issue 的上位结构”。
- 备选方案：
  - 把 tasks 写成完整实现分解：适合单线程执行，但不适合当前工作流。
  - 完全不写 tasks：后续 issue 创建会失去统一骨架。

### 7. Phase 1 仍然采用三包骨架与本地快照契约

- 决定：Phase 1 的实现边界仍固定为 `packages/cli`、`packages/core`、`packages/web` 三包，以及 `.graphspec/graph.json` 作为唯一持久化契约。
- 原因：这条边界既支持当前最小闭环，也能承接后续 writable CLI 和 Skill 封装。

### 8. Phase 1 的 graph 查看能力仍坚持 cluster-first 的最小体验

- 决定：第一版 graph 查看仍从 cluster 视图开始，再下钻到 file，并查看直接影响边。
- 原因：这仍然是最小的用户价值闭环，而且能直接服务后续“AI 查询 blast radius”和“人类审查 graph 变更”的场景。

## 风险 / 权衡

- [Risk] Proposal 一旦写得太大，团队会误以为现在就要一次性做完全部阶段。 → Mitigation: 在 proposal 和 design 中明确“只规格化 Phase 1，后续阶段通过新的 issues / changes 细化”。
- [Risk] 把 GraphSpec 和 OpenSpec 关系写得太近，会让职责边界重新混淆。 → Mitigation: 明确 OpenSpec 管文本化 change，GraphSpec 管结构化 graph，并把桥接重点放在一致性而不是替代。
- [Risk] 过早讨论 Skill / MCP 会把实现节奏拉散。 → Mitigation: 只写演进顺序和边界，不在当前 change 中定义它们的具体协议。
- [Risk] 如果 Phase 1 只做只读图，团队可能低估“可写 graph”对产品价值的重要性。 → Mitigation: 在 proposal 中把 writable graph 和 AI 调用 CLI 明确列为后续主线，而不是可有可无的增强项。

## 推进与迁移计划

- 当前仓库已经保留了占位 workspace 和 OpenSpec 资产，因此迁移策略不是直接冲实现，而是按 phase 逐步推进。
- 当前 change 只承接 Phase 1 的最小闭环；完成后，再分别为 writable graph、Skill/CLI、OpenSpec bridge 创建新的 issues 和 changes。
- 每个后续 issue 都应只切一个薄 slice，并在需要时生成自己的 proposal / design / tasks，而不是复用当前 change 直接承载所有后续阶段。
- 如果后续发现产品定位发生变化，应优先更新 proposal/design 的 phase map，而不是让实现先跑、文档后补。

## 待后续 issue 细化的问题

- 后续的 graph editing 应优先以本地 CLI 命令落地，但具体命令面与 graph draft 模型，刻意留到后续 change 再细化。
- 第一条 OpenSpec bridge 可以是结构一致性检查、架构草稿生成或 proposal/design 审查辅助，但到底先做哪一条，应在 Phase 1 稳定后通过独立 issue 再决定。
