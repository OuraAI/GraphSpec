---
name: script-strategy
description: Use when the user wants to add, update, or choose an implementation approach for repository scripts, automation helpers, or maintenance tooling. This skill decides whether to use shell, Python, Bun/TypeScript, or another option, with Python as the default for non-trivial scripts, shell for thin command glue, and Bun/TypeScript when the script must share repository types or runtime logic.
license: See repository license
compatibility:
  agents: "*"
metadata:
  category: repository-maintenance
  tags:
    - scripting
    - automation
    - tooling
    - python
    - shell
    - bun
---

这个 skill 用来决定“仓库脚本该用什么写”，避免脚本语言随手扩散。

## 核心结论

- 默认脚本语言：`python`
- 很薄的命令胶水：`shell`
- 需要直接复用仓库内部类型、模块或 Bun 运行时能力：`bun/ts`
- `ruby` 不作为默认选项，只在有非常明确理由时使用

不要把这条规则理解成“所有脚本都必须用同一种语言”，而是理解成一套稳定的选型顺序。

## 先看什么

在决定脚本语言前，先确认：

1. 这个脚本到底是在做“命令拼接”，还是在做“结构化处理”
2. 它是否需要解析 `yaml/json/md`、批量改文件、生成内容、处理路径或文本
3. 它是否需要直接调用仓库里的 TypeScript 模块、类型或 Bun 运行时
4. 它会不会演变成长期维护的工具，而不是一次性命令

如果需要更细的判断，再读 `references/decision-matrix.md`。

## 选型顺序

### 1. 先问：能不能只是薄 shell

如果脚本只是：

- 顺序调用 1-3 个现成命令
- 不需要解析结构化数据
- 不需要复杂错误处理
- 不需要跨平台复杂兼容

那么可以用 `shell`。

典型例子：

- 包一层 `gh`、`git`、`bun` 命令
- 本地开发辅助别名
- 很短的 glue logic

一旦开始出现复杂分支、结构化数据解析、批量文件改写，就不要继续硬用 shell。

### 2. 默认落到 Python

只要脚本开始承担下面任一类责任，优先用 `python`：

- 解析和生成结构化数据
- 批量读写文件
- 生成代码、文档、配置
- 做内容转换、批处理、文本清洗
- 需要比 shell 更稳定的流程控制和错误处理
- 这个脚本大概率会长期存在并被反复修改

这类场景里，Python 是默认解。

### 3. 只有在强耦合仓库逻辑时才用 Bun/TypeScript

如果脚本需要：

- 直接复用仓库已有 TypeScript 模块
- 共用现有类型定义
- 直接运行仓库内部业务逻辑
- 明显受益于 Bun 运行时能力

才优先用 `bun/ts`。

不要为了“统一技术栈”就把所有脚本都写成 TypeScript。对很多纯自动化任务来说，这只会增加重量。

### 4. Ruby 不是默认解

`ruby` 可以用，但默认不选。

只有在下面这种情况才考虑：

- 环境已经明确有稳定 Ruby 依赖
- 现有脚本体系已经是 Ruby
- 某个已有 Ruby 工具链能显著降低成本

否则不要继续扩张 Ruby 脚本数量。

## 快速判断表

- 命令胶水、很短、无结构化解析：`shell`
- 结构化处理、批量文件、内容生成、长期维护：`python`
- 强依赖仓库 TS 类型或内部模块：`bun/ts`
- 只有明显外部收益时才考虑：`ruby`

## 护栏

- 不要因为脚本很短就默认写 shell；先判断它会不会继续长
- 不要为了统一技术栈，把所有脚本都写成 Bun/TypeScript
- 不要新增 Ruby 作为常规脚本语言
- 一旦脚本需要解析结构化数据，优先退出 shell
- 如果一个脚本以后大概率还会继续改，优先选可维护性更好的语言

## 输出要求

在给出建议时，至少说明：

- 这次推荐的脚本语言
- 为什么不是 shell
- 为什么不是 bun/ts
- 如果选择的是例外方案，例外理由是什么
