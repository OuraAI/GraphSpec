---
name: gh-issue-delivery
description: Use when the user wants to pick up and solve a GitHub development issue through a spec-first workflow. This skill requires the agent's planning mode, forces a structured multi-question clarification round, produces a durable spec artifact for human review, and only after explicit approval implements the work with dependency-aware tasks and delegated parallel slices.
license: Proprietary
compatibility:
  planning_mode_required: true
  structured_questioning_required: true
metadata:
  language: zh-CN
  scope: github-issue-delivery
---

这个 skill 用来解决开发 issue，但它是 spec-first 的，不是“拿到 issue 直接写代码”。

## 硬门槛：只在规划模式下使用

- 如果当前不在代理的规划模式下，先停下，明确要求用户切到规划模式后再继续。
- 不要在普通聊天里假装完成提问环节；这个 skill 必须使用代理提供的结构化提问机制。
- 至少发起一轮结构化提问，一次问 `2-3` 个短问题。
- 如果关键边界仍然模糊，可以再发起第二轮，但不要无限追问。
- 如果当前代理没有“规划模式 + 结构化提问”这类能力，就不要跳过流程硬做；应先说明当前环境不满足这套工作流。

## 先读什么

开始前，只读当前 issue 真正需要的上下文：

1. 项目的协作规则文件，例如 `AGENTS.md`、`README.md` 或同类文件
2. 项目的开发 issue 模板或工作流说明，如果仓库里有
3. 用当前 issue 跟踪器读取 issue 本体，例如在 GitHub 中可用 `gh issue view <id> --json title,body,labels,url,state`
4. issue 正文里提到的设计文档、spec、tasks、ADR 或其他局部上下文
5. 项目当前已经存在的 spec 体系；如果仓库有 OpenSpec、ADR、RFC 或其他约定，遵循现有约定
6. 如果需要并行执行规则或审核清单，再读 `references/workflow.md`

不要批量扫仓库，不要假设所有项目都长成同一套目录。

## 工作流

### 1. 读取 issue，判断是不是可收敛的问题

- 先确认 issue 是一个可收敛的不确定性，而不是一包大功能。
- 提炼出：
  - 当前要解决的单一问题
  - 背景 / 为什么现在做
  - 已写明的非目标
  - 验收口径
  - 仍未决的问题
- 如果 issue 本身还很散，不要直接实现；后面的提问和 spec 要先把它收紧。

### 2. 必须先问多个问题

使用代理的结构化提问机制发起至少一轮 `2-3` 个问题。问题必须覆盖：

- 这次到底先收哪一刀
- 哪些内容明确不进这轮
- 审核通过前允许走到哪一步

优先问能改变实现路径的问题，不要问低价值偏好题。

### 3. 先产出 spec，再谈实现

在任何代码改动之前，先产出或更新与该 issue 对应的持久化 spec 资产。优先顺序：

1. 如果 issue 已明确挂在现有 spec/change 体系下，就更新对应的 artifact
2. 如果 issue 还没有承载 spec，就先补一个最小 spec 包，至少收住：
   - 目标
   - 非目标
   - 验收口径
   - 未决点
   - 依赖关系
   - 任务拆分

这里的“spec 资产”必须是可被人工审核的持久化完成物，例如仓库文件、spec 文档、ADR、RFC 或项目已有的等价物；不能只是聊天摘要。

不要跳过这一步。

### 4. tasks 必须按依赖图来写

`tasks` 不能是“先做 A，再做 B，再做 C”的直线施工表。

必须显式区分：

- 串行阻塞项：不先完成，后面的工作会漂
- 可并行项：彼此写集不冲突，可以同时推进
- 审核点：哪些任务完成后需要再看一次 spec 或结果
- 每个任务的输入、输出、负责人和写入边界

如果任务天然可以并行，就不要故意把它们压成单线程清单。

### 5. spec 必须先过人工审核

- 产出 spec 后，先把 spec 位置、关键变更和待确认点发给用户。
- 明确等待人工审核。
- 在用户没有明确批准前，不要实现，不要偷偷改代码，不要把任务往前推。
- 不允许只拿口头摘要请用户审核；审核对象必须是已经落地的 spec 完成物。

### 6. 审核通过后再进入实现

一旦用户明确批准：

- 用代理自带的计划跟踪机制把任务图更新成可执行计划
- 标出关键路径和并行分支
- 先处理当前最阻塞的本地任务
- 对独立、边界清晰、写集不冲突的任务，安排子 Agent 或等价的并行代理机制处理

### 7. 实现阶段合理使用子 Agent

在当前环境支持委派的前提下，只要下面条件成立，就必须显式拆出并行切片，并至少委派一个子任务给子 Agent：

- 至少有 `2` 个独立任务可以并行
- 子任务边界清晰
- 写入文件集合互不重叠
- 当前本地步骤不会被该子任务结果立即阻塞

如果最后没有委派，必须明确写出原因，例如：

- 当前环境不支持子 Agent
- 所有任务都在关键路径上
- 写集高度重叠，强行并行会制造集成风险

合适的委派对象：

- 不同 package 的独立改动
- 文档 / 测试 / 非阻塞实现的并行切片
- 明确输入输出的局部实现

不合适的委派对象：

- 还没收住的设计问题
- 需要立刻得到答案才能继续的阻塞项
- 会改到同一批文件的并行任务

### 8. 验证和收口

- 只做当前阶段真正需要的 Harness
- 实现完成后，同步更新 tasks 状态
- 汇总：
  - 改了什么
  - 哪些任务是本地完成的
  - 哪些任务是子 Agent 完成的
  - 跑了什么验证
  - 还剩哪些未决点

## 提问轮次建议

第一轮结构化提问优先覆盖这三类：

1. 当前聚焦哪一刀
2. 哪类内容明确不进入本轮
3. spec 审核通过前，最多推进到哪里

如果 issue 涉及多个 package 或多个能力面，可以在第二轮补问：

1. 哪些切片允许并行
2. 哪些部分必须共用同一份局部 spec
3. 当前阶段最值钱的验证层是哪一层

## 护栏

- 不要在未进入规划模式时使用这个 skill
- 不要跳过结构化提问
- 不要跳过 spec 审核门槛
- 不要用聊天摘要替代持久化 spec 完成物
- 不要把任务写成单线程施工清单
- 不要把会改到同一批文件的任务分给不同子 Agent
- 不要在设计仍未收住时提前进入实现

## 交付结果

每次使用这个 skill，至少要给出：

- 当前 issue 的问题定义
- 本轮提问结果
- 产出的 spec 位置
- 是否已通过人工审核
- 如果进入实现：任务图、并行策略、子 Agent 分工、验证结果
