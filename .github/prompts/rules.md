# GraphSpec AI Agent Rules

> 本文件为 AI Agent 提供项目级别的开发规则和约束。

## 代码风格规则

### TypeScript
- 使用 TypeScript strict 模式
- 优先使用 `const` 而非 `let`
- 使用命名导出而非默认导出
- 函数参数超过 3 个时使用对象参数
- 避免使用 `any` 类型，使用 `unknown` 代替

### 命名规范
- 文件名: kebab-case (e.g., `my-component.ts`)
- 类名: PascalCase (e.g., `MyComponent`)
- 函数/变量: camelCase (e.g., `myFunction`)
- 常量: UPPER_SNAKE_CASE (e.g., `MAX_RETRIES`)
- 类型/接口: PascalCase with `I` prefix optional (e.g., `UserConfig`)

### 错误处理
- 使用自定义错误类而非通用 Error
- 始终处理 Promise rejection
- 避免静默吞没错误

## 架构规则

### 模块边界
- `packages/core` 不应依赖 `packages/cli` 或 `packages/web`
- 共享类型定义放在 `packages/core/types`
- 每个 package 有独立的 `package.json`

### 依赖管理
- 优先使用 Bun 内置 API
- 谨慎添加新依赖，评估包大小和维护状态
- devDependencies 和 dependencies 严格区分

## 文档规则

### 代码注释
- 公共 API 必须有 JSDoc 注释
- 复杂逻辑需要解释 "为什么" 而非 "是什么"
- TODO 注释格式: `// TODO(author): description`

### AGENTS.md 更新
- 新增模块时更新目录结构
- 新增命令时更新 CLI 命令列表
- 架构变更时更新模块索引

## 测试规则

- 新功能必须有对应测试
- 测试文件放在 `__tests__` 目录或 `*.test.ts`
- 使用 `bun test` 运行测试
- Mock 外部依赖，不要真实调用网络

## Git 规则

- 提交信息遵循 Angular Commit Message 规范
- Type: feat, fix, docs, style, refactor, perf, test, build, ci
- Scope: cli, core, web, docs（可选）
- Subject: 首字母小写，不加句号，祈使语气
- Body: 解释 what 和 why
- 单个提交专注于一件事
- PR 标题简洁明了
- 破坏性变更必须在 footer 添加 `BREAKING CHANGE:`

## 安全规则

- 不要提交敏感信息 (API keys, passwords)
- 使用环境变量管理配置
- 依赖包需要审查安全性
