## ADDED Requirements

### Requirement: 快照采用轻量 GraphSpec V1 结构
系统必须将 GraphSpec V1 快照持久化到 `.graphspec/graph.json`，并且每个快照顶层都必须包含 `schemaVersion`、`generatedAt`、`projectRoot`、`nodes`、`edges` 和 `clusters`。

#### Scenario: 生成合法的顶层结构
- **WHEN** `graphspec init` 成功完成
- **THEN** `.graphspec/graph.json` 会包含 GraphSpec V1 所要求的全部顶层字段

### Requirement: 快照中的图元类型必须受限且稳定
快照必须将节点类型限制为 `file`、`external`、`cluster`，必须将边类型限制为 `static-import`，并且必须使用以下稳定格式生成 ID：`file:<relative-posix-path>`、`external:<package-or-specifier>`、`cluster:<cluster-key>`、`static-import:<from-id>-><to-id>`。

#### Scenario: 为文件和外部依赖分配稳定 ID
- **WHEN** 扫描器对同一个项目重复产出 file 与 external 节点
- **THEN** 只要相对路径和依赖 specifier 没有变化，这些节点的 ID 就保持稳定

#### Scenario: 不引入额外图元类型
- **WHEN** 扫描器遇到 V0.1 范围之外的信息，例如路由、API 调用或运行期 wiring
- **THEN** 快照仍然只产出 GraphSpec V1 允许的节点和边类型

### Requirement: cluster 必须按既定路径启发式生成
快照必须按固定的路径启发式生成顶层 cluster，顺序为：优先按 `apps/*` 或 `packages/*` 的 workspace package 聚合；否则按 `src/` 下一级目录聚合；再否则按顶层源码目录聚合。

#### Scenario: monorepo 按 workspace package 聚合
- **WHEN** 项目中的源码文件位于 `apps/*` 或 `packages/*` 之下
- **THEN** 顶层 cluster 会按对应的 workspace package 聚合，而不是按单个文件平铺

#### Scenario: 单包项目按 src 一级目录聚合
- **WHEN** 项目中不存在 `apps/*` 或 `packages/*`，但存在 `src/`
- **THEN** 顶层 cluster 会按 `src/` 下的一级目录生成

#### Scenario: 无 src 时回退到顶层源码目录
- **WHEN** 项目既没有 workspace packages，也没有 `src/` 容器目录
- **THEN** 顶层 cluster 会回退为按包含被扫描 JS/TS 文件的顶层源码目录生成

### Requirement: clusters 必须支持两层浏览所需的成员关系
`clusters` 集合必须记录足够的成员关系信息，以支持顶层概览和下钻，包括每个 cluster 的稳定 ID、展示标签、父 cluster 引用（如果存在）、直接子 cluster ID 和直接子 file 节点 ID。

#### Scenario: 顶层 cluster 可直接渲染概览
- **WHEN** Web 客户端加载 overview
- **THEN** 快照能够直接提供足够的 cluster 元数据，无需再从文件路径重新推导成员关系就能渲染顶层 cluster 列表

#### Scenario: 下钻 cluster 时可读取直接成员
- **WHEN** Web 客户端请求某个具体的 cluster
- **THEN** 快照能够提供该 cluster 的直接子 cluster 和 file 节点 ID，以支持下钻渲染

### Requirement: 循环依赖不会阻塞快照生成
快照生成器必须能够容忍静态 import 形成的循环依赖，并将其表示为普通的有向 `static-import` 边，而不会导致快照生成失败。

#### Scenario: 存在循环依赖
- **WHEN** 两个或多个 JS/TS 文件通过静态 import 相互引用
- **THEN** `graphspec init` 仍然会成功完成，并且快照中会包含对应的有向边
