## 背景与动机

GraphSpec 不能只被规划成一个“本地依赖图查看器”。如果只是这样，它顶多解决一个局部可视化问题，撑不起后续的 Skill、CLI、MCP、IssueDriven、SpecDriven 这些主线能力，也无法解释它为什么值得作为这本书和这个仓库的实战项目。

更准确的定位是：**OpenSpec 解决“需求、设计、任务如何被收敛并持续推进”，GraphSpec 解决“系统架构上下文如何被可视化、可查询、可编辑、可供 AI 调用”。** 它不是 OpenSpec 的替代品，而是和 OpenSpec 互补的一层架构控制面。OpenSpec 偏文本化、变更化、规格化；GraphSpec 偏结构化、空间化、可操作化。GraphSpec 要解决的，正是 OpenSpec 和纯文本 spec 流程里天然存在的几个痛点：

- 规格是线性的，但系统结构是网状的，跨模块影响半径很难在文字里稳定呈现。
- 需求、Spec、架构、代码容易各自演化，缺少一个可以被人和 AI 共同读取的中间结构层。
- AI 即使拿到了 proposal/design/tasks，也仍然不天然具备“当前系统长什么样、改哪里会波及谁”的空间认知。
- 文本规范更适合定义意图和边界，但不适合承载持续演进的架构态势、依赖拓扑和变更草稿。

因此，这次 proposal 需要先把 **GraphSpec 从项目起盘到 AI 能通过 Skill 调用 CLI 去读写 graph** 的粗粒度路线图钉住。后续每一阶段再用 issue-driven 和 spec-driven 方式逐步细化，而不是一开始就把所有阶段写成巨细无遗的大规格。

## 本次变更

- 明确 GraphSpec 的产品定位：它是 OpenSpec 的互补层，不负责替代 spec 流程，而是把“架构上下文”变成一等工程资产。
- 明确 GraphSpec 主要解决的痛点：
  - 让人和 AI 都能从宏观结构逐步下钻，而不是靠人脑记项目全貌。
  - 让影响半径、依赖关系、架构草稿和结构差异成为可浏览、可审查、可操作的对象。
  - 在 Issue / Spec / Graph / Code 之间建立更稳定的中间层，降低文字和实现之间的漂移。
- 定义分阶段演进路径，但只保持粗粒度，不展开成每个阶段的细规格：
  - **Phase 0 - 起盘与规范底板**：仓库骨架、OpenSpec change、README、包边界、最小占位实现。
  - **Phase 1 - 只读 Graph**：本地 CLI 扫描项目，生成轻量 graph 快照，并提供基础 graph 查看能力。
  - **Phase 2 - 可写 Graph 操作面**：引入本地 graph 编辑命令和变更草稿能力，让 graph 不只是可看，还能被显式修改和审查。
  - **Phase 3 - Skill + CLI 驱动的 AI Graph 编辑**：把稳定的 CLI 能力封装成 Skill / agent workflow，让 AI 可以查询 graph、提交 graph 修改请求，并走护栏流程。
  - **Phase 4 - OpenSpec / IssueDriven / SpecDriven 桥接**：让 GraphSpec 不只是图工具，而是能参与 Issue、Spec、Graph、Code 一致性检查与同步的控制面。
- 明确这份 change 的用途更接近 **program seed / roadmap anchor**：后续开发应以 issue-driven 方式逐项切分，每个重要 issue 再通过多轮 AI 对话产出自己的 proposal / design / tasks，而不是直接拿当前 change 全量开工。
- 明确当前这个 change 的职责：**只正式规格化 Phase 1 的最小闭环**，也就是本地 CLI + 本地只读视图 + 轻量 graph 快照；Phase 2 及以后只在 proposal/design 中保留方向，不在这次 change 里细化为可直接实现的 requirements。
- 明确当前阶段的非目标：本 change 不定义云端、MCP Server、桌面宿主、多语言扫描、复杂语义推断，也不在现在就锁定未来 graph edit 命令的完整协议。

## 能力范围

### 新增 Capabilities
- `cli-init-view`：覆盖 Phase 1 的本地 CLI 命令面与只读 graph 查看流程。
- `graph-schema`：覆盖 Phase 1 的 `.graphspec/` 快照契约、图元实体与 cluster 聚合规则。

### 修改中的 Capabilities

无。

## 影响面

- Proposal 层影响：`proposal.md` 不再是一份单点功能说明，而是后续 issues / changes 可以复用的产品路线图锚点。
- Design 层影响：`design.md` 不只解释 Phase 1 的实现形态，还要说明 GraphSpec 为什么沿着 `CLI-first -> writable CLI -> Skill -> OpenSpec bridge` 这条路线演进。
- Tasks 层影响：`tasks.md` 应当充当 issue 拆分种子，帮助团队创建多个聚焦 issue，而不是形成一条巨型实现线程。
- Spec 层影响：当前 change 依旧只创建 Phase 1 的 capability specs，刻意保持当前实现范围收紧。
- 后续工作流影响：graph editing、Skill 集成、OpenSpec bridge 都应该以新的 issues / changes 独立落地，而不是被悄悄塞进这次 Phase 1 实现。
