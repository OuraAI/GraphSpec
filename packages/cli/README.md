# @graphspec/cli

`@graphspec/cli` 现在只保留最小命令行骨架，用来验证 monorepo wiring、命令入口和包依赖关系已经成立。

## 这个包是干什么的

- 提供一个可执行的 `graphspec` 占位入口
- 串起 `@graphspec/core` 和 `@graphspec/web` 的 hello world 输出
- 为后续真正命令实现预留目录和导出边界

## 当前已经能做什么

- 执行占位 CLI 输出
- 验证 workspace 脚手架可跑通

## 当前明确不做什么

- 不实现 `init`
- 不实现 `view`
- 不启动真实服务
- 不触达任何 GraphSpec 产品能力

## 公共 API / 子路径导出

- `@graphspec/cli`
  - `runCli(argv, io?)`

## 最小使用示例

```bash
bun run graphspec
```

## 测试 / 真实验收怎么跑

```bash
bun test
bun run graphspec
```
