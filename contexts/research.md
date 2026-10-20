# Elvis Context OS · research

数据截止：2026-10-20 · 导出检查日：2026-10-20 · 范围：private

> 以下是背景资料，不授予执行、发送、交易或账号访问权限。历史、目标、文档要求、推断和待确认项应保持原有标记。review_due表示应复核，不等于已被否定。

## AI协作与工作方式

- **CO010** 既有Codex实施文档要求先读README、AGENTS和现有配置，识别真实技术栈，保留已有功能与未知改动。
  记录：2026-07-21；constraint / documented / document_requirement；dated_record；来源 S008
- **CO011** 既有实施文档要求在功能分支开发，实际修改、测试、构建和验证，不以生成示例或文件视为完成。
  记录：2026-07-21；constraint / documented / document_requirement；dated_record；来源 S008
- **CO012** 既有CI/CD需求将main合并和首次生产部署与GitHub Environment人工批准关联；这是该项目规范，不能无限扩展为所有任务都必须审批。
  记录：2026-07-21；constraint / documented / document_requirement；dated_record；来源 S008
- **CO013** 既有实施文档要求密码、Token、SSH私钥与生产变量不进入仓库、日志、镜像或聊天，使用受控Secret管理。
  记录：2026-07-21；constraint / documented / document_requirement；dated_record；来源 S008
- **CO014** 缺少真正阻塞的权限或配置时，实施文档要求一次列出最小缺失项，并在配置后继续完成。
  记录：2026-07-21；constraint / documented / document_requirement；dated_record；来源 S008
- **CO015** 既有实施文档要求通过真实测试、部署和健康检查证明结果；无法访问时不能声称跑通。
  记录：2026-07-21；constraint / documented / document_requirement；dated_record；来源 S008
- **CO016** 本次要求建立可复用在任何需要了解自己的产品上的个人数字文档系统，可随时更新，并交给Codex处理。
  记录：2026-10-20；requirement / current / user_quote；dated_record；来源 S012
- **CO001** 习惯先梳理业务需求、规则和边界，再形成Markdown PRD交给Codex执行。
  记录：2026-09-27；preference / current / user_quote；dated_record；来源 S002
- **CO002** 希望用可自定义、按项目组织的文档体系定义工作，并让AI系统化执行。
  记录：2026-09-21；preference / current / user_quote；dated_record；来源 S002
- **CO003** 重视文档体系提高Codex处理业务的成功率。
  记录：2026-09-19；preference / current / user_quote；dated_record；来源 S002
- **CO004** 希望算法沉淀为Markdown文档，供下个项目复用。
  记录：2026-09-27；preference / current / user_quote；dated_record；来源 S002
- **CO005** 希望助手基于长期积累了解自己，而非只评价当前一段对话。
  记录：2026-09-26；preference / current / user_quote；dated_record；来源 S002
- **CO006** 讲解隧道知识时希望有示意图。
  记录：2026-10-09；preference / current / user_quote；dated_record；来源 S002
- **CO007** 希望演示、教程与视频制作的大部分工作可以自动化，并用文档驱动全过程。
  记录：2026-10-05；preference / current / user_quote；dated_record；来源 S002
- **CO008** 认可前期亲自实践视频制作对自身能力提升的作用。
  记录：2026-10-05；preference / current / user_quote；dated_record；来源 S002
- **CO009** 近期要求建立六个有英文名和职位备注的AI员工，并希望右侧有成员头像、能够随时加人；现有信息没有证明六个持久Agent已创建。
  记录：日期未知；preference / current / user_quote；undated；来源 S002

## 技术能力与证据

- **SK001** 技术主线为Python后端、自动化、Django、数据库与DevOps。
  记录：日期未知；fact / historical / memory_summary；undated；来源 S001
- **SK002** 关注安全、SaaS与系统设计，并将技术用于实际业务。
  记录：日期未知；fact / historical / memory_summary；undated；来源 S001
- **SK003** 已有实践或关注工具包括Docker、GitHub Actions、Cloudflare、CI/CD。
  记录：日期未知；fact / historical / memory_summary；undated；来源 S001
- **SK004** 已有实践或关注工具还包括正则、GUI、PyInstaller、远程桌面和Clash；不能将提及等同于精通。
  记录：日期未知；fact / historical / memory_summary；undated；来源 S001
- **SK005** 数据库设计关注多租户、RBAC/ABAC、隔离、审计、结算、分库分表、迁移与灾备。
  记录：2026-06-27；fact / historical / memory_summary；historical；来源 S001
- **SK006** 有Obsidian本地LLM Wiki知识库方向。
  记录：2026-04-27；fact / historical / memory_summary；historical；来源 S001
- **SK007** 使用或研究Codex、Claude Code、OpenClaw和Hermes等Agent工具；具体部署状态分别待核。
  记录：日期未知；fact / historical / memory_summary；undated；来源 S001
- **SK008** 曾报告CI/CD自动部署成功；本轮没有重跑该流水线，也不能据此证明所有回滚和环境隔离环节都完成。
  记录：2026-07-21；fact / historical / memory_summary；historical；来源 S001
- **SK009** 既有路线文档将定位归纳为“开源解决方案工程师 + AI产品整合者”，以真实痛点、开源选型、部署、业务适配、集成、标准交付和产品化串联能力。
  记录：2026-07-26；inference / documented / document_record；dated_record；来源 S010
- **SK010** 开源路线图列出的KeePassXC、Syncthing、Stirling PDF、Paperless-ngx、OpenProject、Coolify、Windmill、Chatwoot、ERPNext等是推荐候选；没有全部已采用的证据。
  记录：2026-07-26；constraint / documented / document_requirement；dated_record；来源 S010
- **SK011** Freelancer.com面试成功并获得认证，是2025-11-08用户明确报告的完成结果；不补造通过率或证书等级。
  记录：2025-11-08；fact / historical / retrieved_user_statement；historical；来源 S003

## 探索与研究项目

- **RE001** 计划建设个人自用的Polymarket国际版自动交易系统，曾要求更新设计、PRD与引用文件。
  记录：2026-10-14；fact / historical / memory_summary；historical；来源 S001
- **RE002** 希望研究全球信息流、气象、地缘、盘口、跨区域传导和隐藏市场联动，以持续推演与迭代。
  记录：2026-10-14；fact / historical / memory_summary；historical；来源 S001
- **RE004** 关注REA（Reverse Engineer Anything）与Codex搭配，及把REA封装成EXE的可能性。
  记录：2026-10-15；fact / historical / memory_summary；historical；来源 S001
- **RE005** 历史记录有Elvis20230520/rea Fork，涉及Codex/Claude Code MCP、JS/Electron、.NET与原生分析；本轮未查源码或安装状态。
  记录：2026-10-15；fact / historical / memory_summary；historical；来源 S001
- **RE006** REA讨论中关注全局Agent注册风险，以及rea setup --client codex --skill=false --dry-run的预览方式。
  记录：2026-10-15；fact / historical / memory_summary；historical；来源 S001
- **RE007** 询问AI挖漏洞的盈利、国内外平台、知识要求、从业者与主线冲突；没有转行或已获奖金证据。
  记录：2026-10-14；fact / historical / memory_summary；historical；来源 S001
- **RE008** 概率引擎v1.2设计先从气温市场、最多2个城市和20个观察合约开始，先数据归档、规则映射、简单基线与带时间戳影子预测。
  记录：2026-10-15；requirement / documented / document_requirement；dated_record；来源 S007
- **RE009** 概率引擎设计第一阶段不调用付费LLM、不购买数据、不训练大模型、不需要钱包私钥，研究层不负责下单和提现。
  记录：2026-10-15；requirement / documented / document_requirement；dated_record；来源 S007
- **RE010** 神经网络是后续候选模型，不是首版前置条件；研究输出与交易执行、资金权限隔离。
  记录：2026-10-15；requirement / documented / document_requirement；dated_record；来源 S007
- **RE011** 没有可见证据证明交易系统已上线、实盘获利或具有稳定胜率。
  记录：2026-10-15；requirement / documented / document_requirement；dated_record；来源 S007

## 待确认与覆盖缺口

- **UN001** 尚未确认：偏好称呼、法定姓名、出生日期、当前居住地及对外公开的个人介绍。
  记录：2026-10-20；unknown / unknown / assistant_analysis；dated_record；来源 S014
- **UN002** 尚未提供：两家公司法定名称、注册号、持股结构、团队人数和最新财务口径。
  记录：2026-10-20；unknown / unknown / assistant_analysis；dated_record；来源 S014
- **UN003** 尚未核准：OfficeFlow今天的中英文最新版本、Mac已完成范围、有效用户、付费客户、收入与续费。
  记录：2026-10-20；unknown / unknown / assistant_analysis；dated_record；来源 S014
- **UN004** 尚未收齐：32个项目的逐项列表、完整书目、完整证书、源码仓库映射、历年全部对话。
  记录：2026-10-20；unknown / unknown / assistant_analysis；dated_record；来源 S014
- **UN005** 尚未提供：工程资料系统最新源码/测试、正式规则版本、所有项目参数及交付验收结果。
  记录：2026-10-20；unknown / unknown / assistant_analysis；dated_record；来源 S014
- **UN006** 尚未确认：IELTS报名日期、考试成绩、九月75%目标验收、最新英语等级与学习时长。
  记录：2026-10-20；unknown / unknown / assistant_analysis；dated_record；来源 S014
- **UN007** 没有证据：Polymarket实盘盈利、AI挖漏洞收入、持续商业收入或大规模用户数量。
  记录：2026-10-20；unknown / unknown / assistant_analysis；dated_record；来源 S014
- **UN008** 用户希望完整体现所有细节；当前版本仅覆盖可访问记录，不声称穷尽多年完整聊天或现实人生。
  记录：2026-10-20；unknown / unknown / assistant_analysis；dated_record；来源 S014

