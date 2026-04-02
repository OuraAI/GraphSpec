# GraphSpec

> 可交互的架构态势感知工具 —— 让 AI 和开发者都能从宏观全貌逐步下钻到微观细节

## 项目定位

GraphSpec 解决的核心痛点：**AI 的上下文有限，改一个功能的时候它看不到全貌。**

开发者需要一种方式，让自己和 AI 都能从一个宏观全貌逐步下钻到微观细节——不是暴力地把所有信息塞进去，而是**按需加载、渐进披露**。

## 当前版本

**V0.1** - 最小可用起点

目标功能：
- `graphspec init`：在项目里创建一个 `.graphspec/` 目录，初始化架构数据
- `graphspec view`：启动一个本地前端服务，把架构数据渲染成可交互的可视化图表

## 技术栈

> 待定盘 - 将在开发过程中逐步收敛

## 项目结构

```
GraphSpec/
├── .github/              # GitHub 配置（Issue/PR 模板、Labels）
├── .graphspec/           # 架构数据目录（待实现）
├── AGENTS.md             # AI Agent 协作指南
├── README.md             # 本文件
└── LICENSE               # 开源协议
```

## 快速开始

```bash
# 克隆仓库
git clone https://github.com/your-org/GraphSpec.git
cd GraphSpec

# TODO: 待补充安装和使用说明
```

## 开发路线

GraphSpec 遵循 AI Native 开发模式，从最小起点开始，根据实际需求逐步扩展：

### 近期目标
- [ ] CLI 基础框架搭建
- [ ] `init` 命令实现
- [ ] `view` 命令实现
- [ ] 本地可视化页面

### 中期方向
- 架构图的 AI 读写能力（MCP Server）
- 渐进式披露策略设计
- 护栏机制（人类确认、变更审计）

### 远期愿景
- 云端服务支持
- 多端 AI 接入形态
- Issue → Spec → 架构 → 代码 的完整链路

## 贡献指南

1. 查看 [Issue](../../issues) 找到感兴趣的任务
2. 阅读 [AGENTS.md](./AGENTS.md) 了解项目结构和 AI 协作规范
3. 提交 PR 前请确保代码通过检查

## 相关链接

- [AI 原生工程](https://ai-native-engineering.netlify.app/) - 本项目的理论基础
- [Issue 模板](./.github/ISSUE_TEMPLATE/) - Bug 报告、功能请求等
- [PR 模板](./.github/PULL_REQUEST_TEMPLATE.md) - Pull Request 规范

## License

MIT License - 详见 [LICENSE](./LICENSE)

---

> 本项目是《AI 原生工程》一书的主线实践项目，用于展示如何在真实大型项目中应用 AI Native 开发方法论。
