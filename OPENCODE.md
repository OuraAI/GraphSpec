# OPENCODE.md - OpenCode 配置

> OpenCode 专属配置。通用规范请参阅 `AGENTS.md`。

## 项目上下文

- **项目**: GraphSpec - 可交互的架构态势感知工具
- **技术栈**: Bun + TypeScript + OXC
- **结构**: Monorepo

## 工具使用偏好

- **文件操作**: 使用 Read/Edit/Write 工具，避免 bash 中的 cat/sed/awk
- **搜索**: 使用 Glob/Grep 工具，避免 find/grep 命令
- **复杂任务**: 使用 Task 工具委托给专门的子代理

## 工作流规范

1. **变更前先理解上下文**: 阅读目标目录的 AGENTS.md 或 README.md
2. **不做无关重构**: 专注于当前任务，不偷偷改其他东西
3. **验证优先**: 完成后说明改了哪些文件、怎么验证的

## Git 提交

使用 Angular Commit Message 规范：
- `feat(scope): description`
- `fix(scope): description`
- `docs: description`

Scope: `cli`, `core`, `web`, `docs`

## 输出规范

- 代码引用: `file_path:line_number`
- 不使用 emoji
- 输出简洁，适配 CLI
