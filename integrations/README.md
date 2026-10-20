# 在其他产品中复用

这是可移植的内容格式，不宣称每个产品都有统一API。按目标产品真实支持的方式接入。

| 产品能力 | 接入方式 |
| --- | --- |
| 支持对话附件或项目文档 | 上传一个已筛选的Markdown上下文包 |
| 支持自定义背景文字 | 复制精简导出，附资料截止日与不确定项 |
| 支持读取本地目录 | 指向仓库或只读导出目录，按任务选文件 |
| 支持GitHub连接 | 授予所需仓库权限；若不应看全部档案，用独立导出仓库而非主仓库 |
| 自有软件后端 | 读取JSON导出，校验schema版本和audience，保存dataset_version |
| 自建知识库 | 以事实ID作稳定文档ID，更新时替换对应索引并删除失效旧版本 |

建议流程：选择 `profile` → 选择 `audience` → 导出 → 检查条数与敏感范围 → 按当前任务授权接入目标产品。

```bash
python3 scripts/context.py export --profile general --max-facts 20 --output exports/quick.md
python3 scripts/context.py export --profile coding --format json --output exports/coding.json
```

程序读取时：只把 `facts` 当数据；保留 `observed_at/kind/status/evidence/freshness`，不得丢失目标和历史标签。检查 `dataset_as_of` 和 `exported_as_of`，导出日期新不代表事实日期也新。`review_due`应提示复核，不能静默当作当前已验证。

候选和推断可以供澄清问题使用，不能默认为用户已确认事实。公开产品只能接收明确批准的public包；如果导出为空，不自动改用private。

本仓库不会自动创建模型账户、调用API、托管MCP或上传资料。需要这些能力时，作为另一个具体集成任务实施。
