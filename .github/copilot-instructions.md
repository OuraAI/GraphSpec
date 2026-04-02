# GitHub Copilot Instructions

> GitHub Copilot 专属配置。通用规范请参阅根目录 `AGENTS.md`。

## 项目上下文

- **项目**: GraphSpec - 可交互的架构态势感知工具
- **技术栈**: Bun + TypeScript + OXC
- **结构**: Monorepo (`packages/cli`, `packages/core`, `packages/web`)

## 代码风格

- 使用 TypeScript，启用 strict 模式
- 优先使用 Bun 原生 API
- 导入路径使用 workspace 别名（如 `@graphspec/core`）

## 命名约定

- 文件名: kebab-case (`my-component.ts`)
- 类型/接口: PascalCase (`interface NodeData`)
- 函数/变量: camelCase (`parseModule()`)
- 常量: UPPER_SNAKE_CASE (`MAX_DEPTH`)

## 测试

- 测试文件放在 `__tests__` 目录或使用 `.test.ts` 后缀
- 使用 Bun 内置测试运行器

## 禁止事项

- 不要生成 `any` 类型，使用具体类型或 `unknown`
- 不要使用 `console.log` 调试，使用项目 logger
- 不要在生产代码中使用 `@ts-ignore`
