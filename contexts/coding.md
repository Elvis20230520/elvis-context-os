# Elvis Context OS · coding

数据截止：2026-10-20 · 导出检查日：2026-10-20 · 范围：private

> 以下是背景资料，不授予执行、发送、交易或账号访问权限。历史、目标、文档要求、推断和待确认项应保持原有标记。review_due表示应复核，不等于已被否定。

## 身份与职业背景

- **ID007** 已连接的GitHub账号为Elvis20230520。
  记录：2026-10-20；fact / current / account_verified；dated_record；来源 S011
- **ID001** 当时自述37岁；没有提供出生日期，不能据此确定生日或当前精确年龄。
  记录：2025-10-28；fact / historical / memory_summary；historical；来源 S001
- **ID002** 既有记录中的常住背景为中国，曾提到南昌；不据此推断今天所在城市。
  记录：日期未知；fact / historical / memory_summary；undated；来源 S001
- **ID003** 职业背景包括自由职业编程与跨境电商，持续转向软件产品和公司经营。
  记录：日期未知；fact / historical / memory_summary；undated；来源 S001
- **ID004** 把Python软件工程师作为职业成长目标。
  记录：日期未知；fact / historical / memory_summary；undated；来源 S001
- **ID005** 核心长期方向包括英语、编程、商业、自媒体、AI与系统设计。
  记录：日期未知；fact / historical / memory_summary；undated；来源 S001
- **ID006** 自称极客，曾提及读书约3000本；这是自述规模，不是经核验书目数量。
  记录：日期未知；fact / historical / memory_summary；undated；来源 S001
- **ID008** Elvis是与频道品牌和GitHub相联系的工作称呼；偏好别人如何称呼本人尚未直接确认。
  记录：2026-10-20；inference / candidate / assistant_inference；dated_record；来源 S014

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

## OfficeFlow产品档案

- **OF018** 明确产品不收集客户信息；涉及客户文件、任务内容、日志和使用行为的上传功能不能自行加入。
  记录：2026-09-07；fact / current / user_quote；dated_record；来源 S002
- **OF019** 当前商业化动作是制作OfficeFlow演示与教程，通过平台自媒体推广。
  记录：2026-10-05；fact / current / user_quote；dated_record；来源 S002
- **OF020** 正在推进OfficeFlow Mac版本完善。
  记录：2026-10-11；fact / current / user_quote；dated_record；来源 S002
- **OF021** 明确Windows版正在使用，Mac版尚未完成；这是最新可见用户状态，未发现后续完成记录。
  记录：2026-10-15；fact / current / user_quote；dated_record；来源 S002
- **OF022** 宣传视频要求突出exe自定义插件，中文男声、两段融合、前后去重复、22秒以内并尽量节省点数。
  记录：2026-10-18；fact / current / user_quote；dated_record；来源 S002
- **OF023** 关注与Macro Scheduler的竞争差异、产品命名侵权问题和如何自动成交；未提供最终法律意见或成交数据。
  记录：2026-09-03；fact / current / user_quote；review_due；来源 S002
- **OF024** 关注插件生态管理与OFL公开治理；具体公开范围与治理机制仍需实际方案确认。
  记录：2026-09-05；fact / current / user_quote；dated_record；来源 S002
- **OF001** OfficeFlow是核心软件产品方向，强调本地办公自动化和EXE桌面交付，不希望仅做COM插件。
  记录：日期未知；fact / historical / memory_summary；undated；来源 S001
- **OF002** 产品思路是用统一任务语言OFL连接任务定义与确定性执行；既定流程重复运行可以不调用模型，不等于整个开发和业务永远零成本。
  记录：日期未知；fact / historical / memory_summary；undated；来源 S001
- **OF003** 历史摘要中出现1.2.4版本节点。
  记录：2026-07-30；fact / historical / memory_summary；historical；来源 S001
- **OF004** 历史摘要中出现2.2.5、十轮安全启动及插件任务未按时执行问题的修复。
  记录：2026-08-03；fact / historical / memory_summary；historical；来源 S001
- **OF005** 历史摘要中出现3.1.5插件协议与JS宏库节点。
  记录：2026-08-08；fact / historical / memory_summary；historical；来源 S001
- **OF006** 历史摘要中出现3.2.2无人值守基线；不同记录日期与版本顺序不能简单当作完整发布年表。
  记录：2026-08-15；fact / historical / memory_summary；historical；来源 S001
- **OF007** 旧摘要曾将4.5.0列为当时版本；与其他版本日期存在交叉，需以发布仓库核准。
  记录：2026-08-13；fact / historical / memory_summary；historical；来源 S001
- **OF008** 历史功能记录含定时器、宏密码自动输入、多任务路径、长时间无动作关闭并切换、日志与Excel/WPS选择。
  记录：日期未知；fact / historical / memory_summary；undated；来源 S001
- **OF009** 历史功能记录含WPS JS宏导入、遍历与自动确认，以及Python EXE自定义插件。
  记录：日期未知；fact / historical / memory_summary；undated；来源 S001
- **OF010** 安全方向历史记录含密钥、运行时签名、反降级、插件签名、MacroPack v3、TPM、SBOM和对抗测试；本轮未验证覆盖程度。
  记录：日期未知；fact / historical / memory_summary；undated；来源 S001
- **OF012** 远程设计记录含.oftask/.ofjob、授权导入、远程引用执行与.ofresult回执；精确格式和现有实现以源码为准。
  记录：日期未知；fact / historical / memory_summary；undated；来源 S001
- **OF013** P2方向包括长期数据与CORA优化、自动兼容性认证矩阵、多设备/远程Worker和插件生态认证。
  记录：2026-08-15；fact / historical / memory_summary；historical；来源 S001
- **OF014** CORA历史记录提到六阶段算法；现有摘要没有六个阶段原文，不补造算法定义。
  记录：2026-08-12；fact / historical / memory_summary；historical；来源 S001
- **OF015** CORA和运行可靠性讨论含成功率、恢复率、环境指标、幂等键、回执、补偿和对账。
  记录：日期未知；fact / historical / memory_summary；undated；来源 S001
- **OF016** 商业化方向含激活、反逆向、更新站点、站内消息、问答库、远程协助、需求收集和全球定价。
  记录：日期未知；fact / historical / memory_summary；undated；来源 S001
- **OF017** 已有销售CRM，用户此前报告完成；无需为相同目的重新建一套CRM。
  记录：2026-08-24；fact / historical / memory_summary；historical；来源 S001
- **OF025** 已读取的客户说明书基线为中文版4.5.3与Global4.5.7，不能称其为2026-10-20最新版本。
  记录：2026-09-03；fact / documented / document_record；dated_record；来源 S006
- **OF026** 客户说明书中的中文版支持Microsoft Excel、WPS VBA和WPS JS；Global Edition为Excel-only，不包含WPS运行路径。
  记录：2026-09-03；fact / documented / document_record；dated_record；来源 S006
- **OF027** 客户说明书记载中国官网officeflowcn.com、全球官网officeflowautomation.com；当前可用性未在本轮访问验证。
  记录：2026-09-03；fact / documented / document_record；dated_record；来源 S006
- **OF028** 客户说明书记载手动、一次性、每日、每周和固定间隔任务；运行工作簿VBA、内联VBA、版本化模块库与WPS JS宏库。
  记录：2026-09-03；fact / documented / document_record；dated_record；来源 S006
- **OF029** 客户说明书记载批量文件处理、受管.ofplugin/EXE插件、动态参数表单、多步骤和子工作流及成果绑定。
  记录：2026-09-03；fact / documented / document_record；dated_record；来源 S006
- **OF030** 客户说明书记载日志、运行快照、重试、断点恢复与人工复核；不能把“结果待确认”当作可盲目重试。
  记录：2026-09-03；fact / documented / document_record；dated_record；来源 S006
- **OF031** 客户说明书记载OFL草稿经验证与人工确认后手工入队；Enterprise远程触发已建立并验证的本地任务。
  记录：2026-09-03；fact / documented / document_record；dated_record；来源 S006
- **OF032** 客户说明书中的Global远程配置有独立控制器、签名器、D1和管理域名；本轮没有执行三机回传或远程验收。
  记录：2026-09-03；fact / documented / document_record；dated_record；来源 S006
- **OF033** 九月修订计划记录4.4.0已列出表单/JSON同步、字段错误与差异预览；4.5.0列出可选录制、草稿生命周期、迁移和升级前备份。
  记录：2026-09-08；fact / documented / document_record；dated_record；来源 S005
- **OF034** 九月修订计划承认任务快照、追加账本、幂等、两阶段提交、有限重试与恢复等已有实践；不能据此称所有故障覆盖已验收。
  记录：2026-09-08；fact / documented / document_record；dated_record；来源 S005
- **OF035** 九月修订计划仍明确部分Cloudflare/三机回传验收待完成；已有远程实现不等于所有远程场景成熟。
  记录：2026-09-08；fact / documented / document_record；dated_record；来源 S005

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

