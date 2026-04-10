## 1. 总纲与 Issue 约束

- [ ] 1.1 把当前 change 作为 GraphSpec 的 program seed，后续创建 issue 时统一引用这份 phase map，而不是每次重新定义产品方向
- [ ] 1.2 约定后续每个重要 issue 都只承载一个薄 slice，并在必要时产出自己的 proposal / design / tasks，而不是直接复用当前 change 全量开发
- [ ] 1.3 约定 issue 至少要标明：所属 phase、要解决的痛点、明确非目标、验收口径，以及是否涉及 OpenSpec 桥接 / Skill / CLI / graph schema

## 2. Phase 0 Issue 种子：起盘与底板

- [ ] 2.1 创建 Phase 0 issue：仓库骨架、workspace、基础命令入口与包边界
- [ ] 2.2 创建 Phase 0 issue：README、AGENTS、OpenSpec 资产与项目协作底板补齐
- [ ] 2.3 创建 Phase 0 issue：占位实现、lint、typecheck、test 基线与最小开发约束

## 3. Phase 1 Issue 种子：只读 Graph

- [ ] 3.1 创建 Phase 1 issue：GraphSpec V1 快照契约与 `.graphspec/graph.json` 的最小 schema
- [ ] 3.2 创建 Phase 1 issue：JS/TS 静态依赖扫描与基础图构建
- [ ] 3.3 创建 Phase 1 issue：cluster 聚合规则与 blast radius 所需的最小视图模型
- [ ] 3.4 创建 Phase 1 issue：`graphspec init [path]` 命令与快照生成流程
- [ ] 3.5 创建 Phase 1 issue：`graphspec view` 本地服务与只读 graph API
- [ ] 3.6 创建 Phase 1 issue：cluster-first 查看界面与 file 级直接影响范围展示
- [ ] 3.7 创建 Phase 1 issue：验收测试、fixture、README 用法与错误路径验证

## 4. Phase 2 Issue 种子：可写 Graph 操作面

- [ ] 4.1 创建 Phase 2 issue：graph draft / graph edit 的产品边界，明确“编辑 graph”不等于直接改源码
- [ ] 4.2 创建 Phase 2 issue：本地 graph 变更命令面，明确哪些编辑操作要先支持
- [ ] 4.3 创建 Phase 2 issue：graph 变更草稿、审查、回滚与人类确认护栏

## 5. Phase 3 Issue 种子：Skill + CLI 驱动的 AI Graph 编辑

- [ ] 5.1 创建 Phase 3 issue：把稳定 CLI 能力封装成 Skill 的输入输出契约
- [ ] 5.2 创建 Phase 3 issue：AI 查询 graph、提交 graph 修改请求、查看执行结果的工作流设计
- [ ] 5.3 创建 Phase 3 issue：Skill 调 CLI 的低噪声约束、失败处理与审计要求

## 6. Phase 4 Issue 种子：OpenSpec Bridge

- [ ] 6.1 创建 Phase 4 issue：Issue / Spec / Graph / Code 一致性检查的第一条桥接链路
- [ ] 6.2 创建 Phase 4 issue：GraphSpec 如何辅助 proposal / design 审查，而不是替代 OpenSpec 文本资产
- [ ] 6.3 创建 Phase 4 issue：后续是否需要 MCP 或更多 AI 接入形态，并基于 CLI-first 成熟度再决定是否立项
