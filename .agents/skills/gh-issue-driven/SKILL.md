---
name: gh-issue-driven
description: Use when the user wants to create, refine, or batch-create GitHub development issues for GraphSpec with gh CLI. This skill turns OpenSpec seeds, discussions, or rough requests into IssueDriven issues with background, why-now, scope, unresolved questions, subtasks, acceptance, and phase-appropriate harness, using the repo's dedicated developer issue template instead of generic user-facing templates.
---

这个 skill 服务的是 GraphSpec 自己的开发 issue 工作流，不是普通用户的功能建议模板。

## 先读什么

开始起草前，只读当前任务真正需要的上下文：

1. `AGENTS.md`
2. `README.md`
3. `.github/ISSUE_TEMPLATE/dev_task.md`
4. 用户点名的仓库内 OpenSpec 上下文，例如：
   - `openspec/changes/<change>/proposal.md`
   - `openspec/changes/<change>/design.md`
   - `openspec/changes/<change>/tasks.md`
5. 如果需要再看一遍原则，读取 `references/issue_principles.md`
6. 如果要创建或修正 issue 标签，读取 `references/label_strategy.md`

不要批量读取无关文件。

## 核心立场

- 开发 issue 是一个“可收敛的不确定性”，不是功能篮子，也不是施工顺序单。
- issue 必须解释“为什么现在做”，而不是只列待办事项。
- 如果背景、非目标、验收口径、未决点还很模糊，就不要假装它已经可以直接实现。
- OpenSpec seed 和 discussion 是来源上下文，但 GitHub issue 必须重写成适合接手协作的工作文档。

## 创建前检查

创建 issue 前，先确认下面五件事都能回答：

1. 你能说清这个 issue 想收住的单一问题是什么。
2. 你能解释为什么它现在重要，以及它在阻止哪种后续漂移。
3. 你能写出明确非目标。
4. 你能把验收口径写成“什么必须成立 / 什么明确不成立 / 什么算失败信号”。
5. 你能点名那些实现者不允许自行脑补的未决点。

如果过不了这道检查，只能做两件事之一：

- 问用户一个聚焦的收窄问题。
- 或明确说明：现在还不该把它创建成 `status:ready` 的开发 issue。

不要硬造一个看起来完整、实际上很空的 issue。

## Issue 正文要求

正文必须遵循 `.github/ISSUE_TEMPLATE/dev_task.md`。

正文必须写中文，而且每个段落都要有实质内容：

- `背景 / 为什么现在做`：写清卡住的链路和漂移风险。
- `当前想收住的不确定性`：点名真正的问题，不要写成宽泛功能。
- `本 issue 想解决什么`：写 3-5 条明确边界。
- `明确不解决什么`：写死这次不进入的内容。
- `当前已知上下文`：链接 OpenSpec、文档、discussion 或已有 issue。
- `前置依赖`：说清楚它是不是被阻塞。
- `需要先讨论或确认的问题`：列出实现者不能擅自补完的点。
- `子任务树`：拆成明确的小任务，服务收敛，不是堆施工动作。
- `验收口径`：必须有“成立 / 不成立 / 失败信号”三类判断。
- `Harness / 验证要求`：只写当前 phase 真正需要的验证。

## 标签规则

标签来源以 `.github/labels.yml` 为准，不要只看远端当前“已经存在什么”。

### 创建前必须做标签预检

在创建或修正 issue 前，先检查远端仓库是否已经同步了 `.github/labels.yml`。

推荐流程：

1. 读取 `.github/labels.yml`
2. 读取远端 labels 列表
3. 如果发现预期标签不存在，先同步标签，再创建 issue

优先使用这个脚本：

```bash
python3 .agents/skills/gh-issue-driven/scripts/sync_repo_labels.py --repo OuraAI/GraphSpec
```

如果脚本不可用，也必须用 `gh label create <name> --force` 把缺失标签补齐。不要明知仓库定义了更细标签，却退化成只挂 GitHub 默认的 `enhancement` / `documentation`。

### 创建 issue 时的最小标签集合

每个开发 issue 至少要有：

- 一个 `type:*`
- 一个 `priority:*`
- 一个 `status:*`

如果影响范围明确，再补：

- 一个或多个 `area:*`

如果复杂度能比较稳地判断，再补：

- 一个 `complexity:*`

- `type:enhancement`：默认用于产品、架构、CLI、Web、Infra 等开发切片。
- `type:docs`：只涉及文档的工作。
- `type:test`：以 Harness 或验证为主的问题。
- `type:chore`：工具链或仓库维护类工作。
- `type:discussion`：只有用户明确要创建偏讨论型 issue 时才用。

- `priority:medium`：默认值。
- `priority:high`：当前 phase 的阻塞项，或会卡住多个后续 issue。
- `priority:low`：有价值，但不在当前关键路径上。

- `status:needs-review`：新建 issue 的默认状态，表示还需要维护者确认。
- `status:ready`：只有目标、非目标、验收和未决点都收得足够紧时才用。
- `status:blocked`：存在明确上游决策或依赖阻塞时才用。

如果影响范围很明确，补充 `area:*` 标签：`area:cli`、`area:core`、`area:web`、`area:docs`、`area:infra`。

复杂度标签建议：

- `complexity:small`：单 area、小范围切片
- `complexity:medium`：默认用于 3-5 个子任务或跨 1-2 个 area 的 issue
- `complexity:large`：跨多个 area、明显需要更多协调

## Harness 规则

Harness 必须按阶段递增：

- Phase 0: `format / lint / typecheck / smoke`
- Phase 1: graph asset validation, sample fixtures, CLI behavior checks, node-related-content consistency
- Phase 2: graph edit guardrails, rollback, audit
- Phase 3: Skill to CLI input/output stability, failure paths, low-noise command surface
- Phase 4: only then consider heavy UI E2E such as Playwright

不要为了“看起来完整”就把重型 Harness 提前塞进早期 issue。

## gh 命令模式

优先使用非交互式 `gh` 命令。

1. 先把正文写进一个临时 markdown 文件，结构跟模板保持一致。
2. 同步或补齐远端标签。
3. 再显式带上完整 labels 创建 issue。
4. 创建后回读 issue，核对标签是否完整；如果只挂上了默认标签，立即修正。

示例：

```bash
gh issue create \
  --repo OuraAI/GraphSpec \
  --title "[DEV] your issue title" \
  --body-file graphspec-issue.md \
  --label type:enhancement \
  --label priority:medium \
  --label status:needs-review \
  --label area:core \
  --label complexity:medium
```

可以用 `--template "Issue-Driven Development Task"` 作为起点，但不要依赖 GitHub 的默认提示流；最终 body 必须是完整写好的正文。

创建后建议立即校验：

```bash
gh issue view <number> --repo OuraAI/GraphSpec --json labels,title,url
```

如果发现 issue 仍只有 `enhancement`、`documentation` 这类默认标签，而 repo 标签已存在，应立刻：

```bash
gh issue edit <number> \
  --repo OuraAI/GraphSpec \
  --add-label type:enhancement \
  --add-label priority:medium \
  --add-label status:needs-review \
  --add-label area:core \
  --remove-label enhancement
```

## 护栏

- 不要创建一个把多个架构决策糊在一起的大 issue。
- 不要把 OpenSpec task 标题直接翻成 GitHub issue，而不补背景和验收。
- 不要写“功能基本可用”“支持后续扩展”这种空洞验收。
- 如果还存在关键架构未决点，不要标记 `status:ready`。
- 如果源上下文明确没有进入当前 phase，就不要偷偷把 scanner、AI 分析或重型 Harness 升级进来。
- 不要在仓库已定义完整标签体系时，只挂 GitHub 默认标签。
- 不要创建完 issue 后不回读标签结果；标签不完整必须修正。

## 创建后返回什么

创建完成后，至少返回：

- issue 标题
- label 集合
- issue URL
- 这个 issue 现在是否可以接手，还是仍在等待 review / 上游决策
