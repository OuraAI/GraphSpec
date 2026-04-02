# CLAUDE.md - Claude Code 配置

> Claude Code (cc) 专属配置。通用规范请参阅 AGENTS.md。

@AGENTS.md

## Claude Code 特定指令

### 工具使用偏好

- **文件操作**: 优先使用 Read/Edit/Write 工具，避免 cat/sed/awk
- **搜索**: 使用 Glob 和 Grep 工具，避免 find/grep 命令
- **并行执行**: 无依赖的操作应并行调用

### 上下文管理

- 使用 `@file` 语法引用文件时，优先引用最相关的文件
- 大文件使用 offset/limit 分段读取
- 复杂搜索任务使用 Task 工具委托给子代理

### 输出规范

- 代码引用格式: `file_path:line_number`
- 不使用 emoji，除非用户明确要求
- 输出简洁，适配 CLI 环境
