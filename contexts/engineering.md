# Elvis Context OS · engineering

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

## 工程资料与DocumentFlow

- **EN001** 工程资料文档体系自动化是独立项目，与OfficeFlow没有直接依赖，成熟后再考虑接入。
  记录：2026-09-19；fact / current / user_quote；dated_record；来源 S002
- **EN002** 目标是把工程资料工作整体系统化：项目图纸、台账、参数、知识经验与生成流程组织在一起。
  记录：2026-09-21；fact / current / user_quote；dated_record；来源 S002
- **EN003** 希望能新建自定义项目、不同类型的文档系统，并调用不同线上数据库或存储。
  记录：2026-09-21；fact / current / user_quote；dated_record；来源 S002
- **EN004** 现阶段先自己使用，因为需要接入自己的Codex；不将个人账号直接开放给他人。
  记录：2026-09-22；fact / current / user_quote；dated_record；来源 S002
- **EN005** 隧道资料自动化希望按WBS完成整套分项资料，每个分项形成参数文件，参数导入后可以产出资料。
  记录：2026-09-27；fact / current / user_quote；dated_record；来源 S002
- **EN006** 不同开挖方式改变资料结构与部位名称：用户给定的双侧壁导坑场景需6次测量及对应开挖资料，二分部场景需3次。
  记录：2026-09-27；fact / current / user_quote；dated_record；来源 S002
- **EN007** 具体隧道采用的开挖方式由用户告诉系统，再由内置规则判断资料结构。
  记录：2026-09-27；fact / current / user_quote；dated_record；来源 S002
- **EN008** 希望用规则明细表替代复杂合并单元格，便于自动读取和维护。
  记录：2026-09-27；fact / current / memory_summary；dated_record；来源 S001
- **EN009** 曾明确某次偏距算法任务中不能参考所附开挖方式与各断面图的数据，改按经验与开挖方式建模；该限制仅适用于那次任务，不能普遍拒绝正式图纸。
  记录：2026-09-27；fact / current / user_quote；dated_record；来源 S002
- **EN010** 要求偏距算法写成Markdown文档供下一个项目复用；经验估算应与正式设计参数分开。
  记录：2026-09-27；fact / current / user_quote；dated_record；来源 S002
- **EN011** 具体讨论场景：上台阶钢架间距1.2m、每循环不超过1榀；下台阶不超过2榀。不能把1.2m/2.4m作为所有隧道统一标准。
  记录：2026-10-09；fact / current / user_quote；dated_record；来源 S002
- **EN012** 对“5榀”的追问是举例说明，不能转成实际施工批准参数。
  记录：2026-10-09；fact / current / user_quote；dated_record；来源 S002
- **EN013** 希望系统学习隧道细节工程知识，并理解段方位角等术语，最好配示意图。
  记录：2026-10-09；fact / current / user_quote；dated_record；来源 S002
- **EN014** 本人明确工程资料自动化系统尚不成熟，需要不断优化。
  记录：2026-10-11；fact / current / user_quote；dated_record；来源 S002
- **EN015** 曾报告文档系统第一版已完成；没有本轮源码或端到端测试证据证明生产成熟度。
  记录：2026-09-22；fact / current / user_quote；dated_record；来源 S002
- **EN016** DocumentFlow是工作名称，可更名；首个任务包为隧道WBS智能划分，本期PRD范围为AI Gateway核心、Codex个人账号Provider与最小验证闭环。
  记录：2026-09-20；requirement / documented / document_requirement；dated_record；来源 S004
- **EN017** Gateway设计负责标准任务、最小上下文、Provider路由、工作目录、输出Schema、运行记录、有限重试和人工审核。
  记录：2026-09-20；requirement / documented / document_requirement；dated_record；来源 S004
- **EN018** Gateway设计规定AI只生成候选事实；桩号、区段、长度、编码、重复、缺口和总量校验由Python确定性规则处理。
  记录：2026-09-20；requirement / documented / document_requirement；dated_record；来源 S004
- **EN019** Gateway设计要求结论附文档、页码或Sheet、单元格/片段/图像区域、提取方法及不确定项，失败不能污染正式事实。
  记录：2026-09-20；requirement / documented / document_requirement；dated_record；来源 S004
- **EN020** Gateway设计不读取复制或上传Codex认证文件；认证由本机运行时负责，Provider应可替换。
  记录：2026-09-20；requirement / documented / document_requirement；dated_record；来源 S004
- **EN021** Gateway本期非目标包括完整OCR、完整WBS业务、微服务、多Agent、向量库和OfficeFlow集成；这是该版本边界，不是永久产品禁令。
  记录：2026-09-20；requirement / documented / document_requirement；dated_record；来源 S004
- **EN022** 曾把OSS理解为线上数据库；仓库术语应明确对象存储用于文件，结构化业务事实与索引需要相应数据库或元数据层。
  记录：2026-09-22；inference / historical / conversation_topic；historical；来源 S002

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

