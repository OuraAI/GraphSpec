## ADDED Requirements

### Requirement: init 命令生成或刷新本地快照
CLI 必须提供 `graphspec init [path]` 命令，用于扫描目标 JS/TS 项目根目录，并创建或刷新合法的 GraphSpec V1 `.graphspec/graph.json` 快照。

#### Scenario: 在默认目录生成快照
- **WHEN** 用户在受支持的 JS/TS 项目根目录中执行 `graphspec init`
- **THEN** 命令会在当前项目根目录下生成 `.graphspec/graph.json`

#### Scenario: 在指定目录刷新快照
- **WHEN** 用户对一个已经包含 `.graphspec/graph.json` 的项目执行 `graphspec init /path/to/project`
- **THEN** 命令会刷新目标项目中的快照，而不是把它当成一次性初始化命令

### Requirement: init 只承诺 JS/TS 静态依赖扫描
`graphspec init` 命令在 V0.1 中必须只分析 JavaScript / TypeScript 源文件，并且只产出来自静态 `import` 或 `export ... from` 语法的依赖关系。

#### Scenario: 遇到非 JS/TS 文件
- **WHEN** 扫描器遇到 Rust、Python、Go 或其他非 JS/TS 文件
- **THEN** 这些文件会被排除在快照生成之外，不会把 graph 契约扩展到 V0.1 范围之外

#### Scenario: 遇到静态依赖语法
- **WHEN** 某个 JS/TS 源文件中包含相对路径静态 import 或 re-export
- **THEN** 生成的快照中会包含一条 `static-import` 边，把导入方文件节点连接到解析后的目标文件节点

### Requirement: view 命令只渲染已有快照
CLI 必须提供 `graphspec view` 命令，该命令基于现有 `.graphspec/graph.json` 快照启动本地只读可视化服务，并且不能隐式触发重新扫描。

#### Scenario: 快照存在时启动本地服务
- **WHEN** 用户在已经存在 `.graphspec/graph.json` 的项目根目录中执行 `graphspec view`
- **THEN** 命令会启动本地 HTTP 服务，并基于该快照渲染浏览器可访问的可视化页面

#### Scenario: 快照缺失时返回可操作错误
- **WHEN** 用户在不存在 `.graphspec/graph.json` 的项目根目录中执行 `graphspec view`
- **THEN** 命令会以可操作错误退出，并明确提示用户先执行 `graphspec init`

### Requirement: view 提供只读的 cluster-first blast radius 浏览
`graphspec view` 的默认体验必须先展示顶层 cluster 概览，必须允许继续下钻到 file 节点，并且必须为被查看的 file 节点展示直接入边与出边。

#### Scenario: 打开页面先看到 cluster 概览
- **WHEN** `graphspec view` 成功启动后浏览器页面完成加载
- **THEN** 页面初始状态展示的是顶层 cluster 概览，而不是平铺的文件图

#### Scenario: 下钻后查看文件直接影响范围
- **WHEN** 用户下钻进入某个 cluster 并选中一个 file 节点
- **THEN** 页面会展示该 file 节点直接相关的入边和出边 `static-import`，以支持 blast radius review

### Requirement: view 通过本地 API 暴露只读图查询
由 `graphspec view` 启动的本地服务必须提供只读 HTTP 接口，用于概览查询、cluster 下钻和 node blast radius 查询；Web 客户端必须消费这些接口，而不是直接读取快照文件。

#### Scenario: 请求概览数据
- **WHEN** Web 客户端请求 `GET /api/overview`
- **THEN** 服务会返回基于当前快照生成的顶层 cluster 概览

#### Scenario: 请求 cluster 子项
- **WHEN** Web 客户端请求 `GET /api/clusters/:clusterId`
- **THEN** 服务会返回该 cluster 的直接子 cluster、file 节点以及边摘要

#### Scenario: 请求 node 直接依赖
- **WHEN** Web 客户端请求 `GET /api/nodes/:nodeId`
- **THEN** 服务会返回当前快照中该节点的直接入边和出边
