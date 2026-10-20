# 给 Codex：接手我的个人数字文档系统

你接手的是一个已经填入历史资料、可以运行的个人上下文仓库，不是空白PRD。默认保留现有结构，先把我提供的新资料整理好。无需为了“AI时代”重建一个网站、RAG系统或数据库。

## 第一次进入

1. 读 `AGENTS.md`、`README.md`、`CURRENT.md`。
2. 读 `data/facts.json`、`data/sources.json`、`data/projects.json`，了解事实ID与来源边界。
3. 只加载当前任务所需的 `contexts/` 文件；完整历史见 `docs/`。
4. 跑校验，确认当前仓库可用，再开始更新。

```bash
python3 scripts/context.py validate
python3 -m unittest discover -s tests -v
```

## 收到“更新我的资料”

假设我说：“OfficeFlow Mac版完成首次运行测试，还没正式发布。”应这样处理：

- 新增来源S015，写明本次用户陈述及实际日期。
- 新增事实，例如OF036：“Mac版完成首次运行测试，尚未正式发布”。
- 原OF021“Mac版尚未完成”的确切含义需要结合新陈述处理：首次运行并不一定推翻“整体未完成”，可以先补进展，而不是直接把它改为“正式发布”。
- 若我明确说已正式发布，再新增状态并用 `supersedes` 关联旧状态，保留历史。
- 不能把这句话扩写为已支持WPS、已通过签名公证、已收费或已全球发布。

维护顺序：

1. 新建 `context/update-YYYYMMDD` 功能分支（已有任务分支则继续使用）。
2. 分类本次输入：事实、偏好、约束、目标、要求、推断、未知。
3. 追加来源，最小粒度新增或修正事实。用户明确纠错时，保留旧记录并说明修正。
4. 更新 `data/facts.json` 的 `as_of` 和 `dataset_version`，必要时更新项目事实引用。
5. 运行校验、生成与测试；查看差异。
6. 更新 `CHANGELOG.md`，报告修改与未决项，按本次用户授权提交/推送。

```bash
python3 scripts/context.py validate
python3 scripts/context.py build --as-of YYYY-MM-DD
python3 -m unittest discover -s tests -v
git diff --check
```

## 补齐多年历史

先处理 [待确认清单](docs/unknowns.md)，再按 [历史补录提示](prompts/BACKFILL.md) 接收我导出的对话、已有PRD和证据。每一批记录可追踪，不能把助手过去的夸赞、平台推荐邮件或我问过的问题改写成现实成果。已存在的文件优先读取当前版本。

## 给其他产品准备背景

```bash
python3 scripts/context.py export --profile general --output exports/about-me.md
python3 scripts/context.py export --profile officeflow --format json --output exports/officeflow.json
python3 scripts/context.py export --profile english --output exports/english.md
```

默认 `private` 范围不含限制级财务和姓名线索。只有明确需要完整内部档案时才使用：

```bash
python3 scripts/context.py export --profile full --audience restricted --history --output exports/internal-full.md
```

公开分享只导出逐项批准的记录：

```bash
python3 scripts/context.py export --profile full --audience public --output exports/public.md
```

首版公开文件为空是预期行为。不要把主仓库直接改公开，也不要向外部产品自动上传文件。先按该产品实际读取权限选最小范围，再由当前任务授权发送。

## 本版完成条件

- 不遗漏来源引用和观察日期，不把旧状态冒充当前。
- 日常背景、OfficeFlow、工程资料、英语、商业等上下文可分别生成。
- 不含API Key和登录凭据；运行不调用外部服务。
- 校验与测试通过，派生文档与事实源一致。
- 能清楚说明这批更新改变了什么，哪些仍需我补充。
