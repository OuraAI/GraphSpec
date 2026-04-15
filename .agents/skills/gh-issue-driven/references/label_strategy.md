# GraphSpec Issue 标签策略

这份 reference 只回答一件事：开发 issue 应该如何打出完整标签，而不是只挂一个 `enhancement` 或 `documentation`。

## 基本原则

开发 issue 至少应显式表达四类信息：

- 它是什么类型的问题
- 它现在有多重要
- 它当前处于什么状态
- 它主要影响哪个区域

如果仓库定义了更细的标签体系，就不要退化成 GitHub 默认标签。

## 必选标签

每个开发 issue 至少要有：

- 一个 `type:*`
- 一个 `priority:*`
- 一个 `status:*`

如果影响范围明确，再补：

- 一个或多个 `area:*`

如果复杂度能大致判断，再补：

- 一个 `complexity:*`

## type 标签怎么选

- `type:enhancement`
  - 默认用于产品、架构、CLI、core、web、infra 的开发切片
- `type:docs`
  - 只涉及文档、模板、规则、说明资产
- `type:test`
  - 主要在补 Harness、验证策略、测试资产
- `type:chore`
  - 工具链、仓库维护、脚手架整理
- `type:bug`
  - 明确是现有行为错误
- `type:discussion`
  - 用户明确要讨论型 issue，而不是可直接接手的开发 issue

## priority 标签怎么选

- `priority:high`
  - 当前 phase 的阻塞项
  - 会卡住多个后续 issue
- `priority:medium`
  - 默认值
- `priority:low`
  - 有价值，但不在当前关键路径
- `priority:critical`
  - 只有明确紧急、需要立即处理时才用

## status 标签怎么选

- `status:needs-review`
  - 新建 issue 的默认状态
  - 说明它还需要维护者再看一遍
- `status:ready`
  - 边界、非目标、验收、未决点都已足够清楚
  - 已经适合接手
- `status:blocked`
  - 还被明确的上游决策或依赖卡住
- `status:in-progress`
  - 已有人接手
- `status:in-review`
  - 已进入 review

## area 标签怎么选

- `area:cli`
- `area:core`
- `area:web`
- `area:docs`
- `area:infra`

可以多个同时存在，但不要为了“看起来全”把所有 area 都打上。

## complexity 标签怎么选

- `complexity:small`
  - 单包、小范围、1-2 个清晰子任务
- `complexity:medium`
  - 默认用于跨 1-2 个 area，或有 3-5 个明确子任务
- `complexity:large`
  - 跨多个 area，依赖更多协调，或者明显不是一个短平快切片

## 创建和修正标签的流程

1. 先读 `.github/labels.yml`
2. 再看远端是否已有这些标签
3. 如果缺失，先同步标签，再创建 issue
4. 创建后回读 issue，核对标签是否完整
5. 如果 issue 还挂着默认 `enhancement` / `documentation`，而仓库已有 `type:*` 标签，应补 repo 标签并移除默认标签
