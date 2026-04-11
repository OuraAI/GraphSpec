# @graphspec/web

`@graphspec/web` 现在只保留最小占位包，用来占住本地可视化服务的位置，并验证 web 包的导出边界已建立。

## 这个包是干什么的

- 提供 web 包入口
- 暴露一个 hello world 级别占位 API
- 为后续本地可视化服务预留包结构

## 当前已经能做什么

- 暴露 `webHello()` 占位函数
- 支持 workspace 级 lint、typecheck、test

## 当前明确不做什么

- 不启动 HTTP 服务
- 不渲染页面
- 不提供 HTTP/Web 服务 API
- 不读写任何项目数据

## 公共 API / 子路径导出

- `@graphspec/web`
  - `webHello()`
  - `WEB_PLACEHOLDER_MESSAGE`

## 最小使用示例

```ts
import { webHello } from "@graphspec/web";

console.log(webHello());
```

## 测试 / 真实验收怎么跑

```bash
bun test
bun run --cwd packages/web dev
```
