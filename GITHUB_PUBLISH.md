# GitHub同步与恢复指南

私有主仓库：

https://github.com/Elvis20230520/elvis-context-os

## Codex在本机接手

使用本人现有GitHub登录状态克隆仓库，再读 `CODEX_START_HERE.md` 和 `AGENTS.md`。不需要把Token、密码或登录文件贴到聊天中。

```bash
git clone https://github.com/Elvis20230520/elvis-context-os.git
cd elvis-context-os
python3 scripts/context.py validate
python3 -m unittest discover -s tests -v
```

## 日常更新

1. 拉取最新版本并检查本地未提交改动，不覆盖未知工作。
2. 按AGENTS.md在功能分支更新事实台账与来源。
3. 按实际复核日期重建文档，运行测试，检查差异。
4. 根据本次授权提交和推送，不强推、不更改私有状态。

```bash
git switch -c context/update-YYYYMMDD
python3 scripts/context.py validate
python3 scripts/context.py build --as-of YYYY-MM-DD
python3 -m unittest discover -s tests -v
git diff --check
```

## 使用离线压缩包恢复

解压后先与远端比较。早期压缩包可能包含当时的上传受阻说明；以当前仓库状态为准。保留点开头文件和目录，勿把旧包整批覆盖到已有新进展的仓库。

主数据在 `data/facts.json` 与 `data/sources.json`；派生档案可用build命令重新生成。恢复后重新校验，再报告实际提交SHA与Actions结果。权限或网络阻塞时说明准确状态，不能把本地文件存在说成远端上传完成。
