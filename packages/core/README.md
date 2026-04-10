# @graphspec/core

`@graphspec/core` 现在只承担最小骨架角色，用来占住 GraphSpec 核心引擎包的位置，并给后续真实实现留出明确入口。

## 这个包是干什么的

- 提供核心包入口
- 暴露一个最小 `hello world` 级别占位 API
- 为后续图扫描和快照逻辑预留包边界

## 当前已经能做什么

- 暴露 `coreHello()` 作为骨架验证入口
- 支持 workspace 级 lint、typecheck、test

## 当前明确不做什么

- 不做依赖扫描
- 不做快照生成
- 不做图查询或数据存储
- 不做任何运行时产品能力

## 公共 API / 子路径导出

- `@graphspec/core`
  - `coreHello()`
  - `CORE_PLACEHOLDER_MESSAGE`

## 最小使用示例

```ts
import { coreHello } from "@graphspec/core";

console.log(coreHello());
```

## 测试 / 真实验收怎么跑

```bash
bun test
bun run typecheck
```
