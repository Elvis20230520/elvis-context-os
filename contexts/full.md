# Elvis Context OS · full

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

## 价值观与习惯

- **VA001** 自述对困难的承受能力较高，野心大且实干。
  记录：2026-09-01；preference / current / memory_summary；dated_record；来源 S001
- **VA002** 强调自己把控和设计人生方向，希望在已有能力基础上继续变强。
  记录：2026-09-26；preference / current / user_quote；dated_record；来源 S002
- **VA003** 希望把工作系统化以释放时间，集中推进OfficeFlow商业化。
  记录：2026-09-26；preference / current / user_quote；dated_record；来源 S002
- **VA004** 持续关心AI、AGI、ASI时代的适应能力、技术、英语、财富和个人竞争力。
  记录：2026-10-05；preference / current / user_quote；dated_record；来源 S002
- **VA005** 希望1–2年后处在与现在不同的位置；这是一项成长愿望，不是已达成结果。
  记录：2026-09-03；preference / current / memory_summary；dated_record；来源 S001
- **VA006** 有冥想、跑步、学习与复盘习惯；实际频率未提供。
  记录：日期未知；preference / current / memory_summary；undated；来源 S001
- **VA007** 希望将个人习惯可视化。
  记录：2026-07-20；preference / current / memory_summary；dated_record；来源 S001
- **VA008** 认同通过实际场景应用来学习：把新知识变成做法，再根据结果判断价值。
  记录：2026-09-15；preference / current / user_quote；dated_record；来源 S002
- **VA009** 承认工程资料文档自动化系统仍不成熟，需要持续优化。
  记录：2026-10-11；preference / current / user_quote；dated_record；来源 S002
- **VA010** 历史对话中接受过“先现金流、后资本化”的稳健成长路线，并表达未来战略与生态统筹的CEO愿景。
  记录：2025-10-11；goal / historical / retrieved_user_statement；historical；来源 S003

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

## 英语与认知学习

- **LE005** 英语水平本人自评B2；不是本轮标准化测试结论。
  记录：2026-09-06；goal / current / user_quote；dated_record；来源 S002
- **LE006** 设定IELTS General Training总分至少6.5的目标，准备期三个月，计划每天2–3小时；没有已考分数。
  记录：2026-10-01；goal / current / memory_summary；dated_record；来源 S001
- **LE007** 要求每周进行技术英语练习，语境包括Python、AI工具、软件项目和国际协作，含口语或写作小练习、纠错及更自然的职业表达。
  记录：2026-08-24；goal / current / user_quote；dated_record；来源 S002
- **LE008** 再次提出每周技术英语练习要求；是否存在有效自动化日程需单独检查。
  记录：2026-10-19；goal / current / user_quote；dated_record；来源 S002
- **LE009** 英语对其国际技术协作和个人方向非常重要，希望持续提高。
  记录：2026-09-06；goal / current / user_quote；dated_record；来源 S002
- **LE010** 希望明确选择学什么、投入多深、什么时候先停下来应用。
  记录：2026-09-15；goal / current / user_quote；dated_record；来源 S002
- **LE011** 持续构建认知与知识体系，推荐书籍需要避免重复，并连接实际应用。
  记录：2026-10-15；goal / current / user_quote；dated_record；来源 S002
- **LE001** 历史记录：英语流利说8级、坚持507天、累计约427小时；这些数值只对应当时，不外推为今天。
  记录：2026-05-18；fact / historical / memory_summary；historical；来源 S001
- **LE002** 历史摘要记录Google IT Automation with Python六门课程已完成；本轮未查验证书。
  记录：2026-05-13；fact / historical / memory_summary；historical；来源 S001
- **LE003** 历史摘要提到使用Codex和Claude Code做过32个项目；检索片段多为助手转述，项目数量未逐项核验。
  记录：2026-06-21；fact / historical / memory_summary；historical；来源 S001
- **LE004** 历史记录有Python level 3认证或测试经历；平台、证书编号与具体含义待补。
  记录：2025-10-02；fact / historical / memory_summary；historical；来源 S001
- **LE012** 九月技能树目标为按一致口径总体达到75%以上；没有依据把九月目标写成今天已达到。
  记录：2026-09-08；fact / historical / document_record；historical；来源 S005
- **LE013** 旧截图四分支为后端74%、数据工程59%、AI/ML73%、云原生与DevOps62%，等权均值67%；均为历史规划参照。
  记录：2026-09-08；fact / historical / document_record；historical；来源 S005
- **LE014** 修订计划要求承认已完成部署与产品进展，不为重复证明已有成果重学CI/CD或重搭Docker。
  记录：2026-09-08；fact / historical / document_record；historical；来源 S005
- **LE015** 技能进阶的判断包括能解释、主导变更、定位故障和验证结果；可查文档并使用AI。
  记录：2026-09-08；fact / historical / document_record；historical；来源 S005
- **LE016** 九月计划补强重点为PostgreSQL事务与查询、数据一致性、备份恢复和迁移兼容，不把SQLite/D1经验等同于PostgreSQL精通。
  记录：2026-09-08；fact / historical / document_record；historical；来源 S005
- **LE017** 九月计划将产品首次使用、演示、商业化和销售与技术补强一起推进。
  记录：2026-09-08；fact / historical / document_record；historical；来源 S005
- **LE018** 能力评分只能在相同口径下基于新增证据更新，不能凭项目名称另造精确百分比。
  记录：2026-09-08；fact / historical / document_record；historical；来源 S005
- **LE019** 讨论领域驱动设计与OfficeFlow领域地图，涉及任务、OFL、CORA、Worker、插件、授权、更新和CRM边界。
  记录：2026-09-12；interest / historical / conversation_topic；historical；来源 S002
- **LE020** 近期阅读讨论证据如何支持主张，把点赞、成功试用、愿意付费和持续使用分别对应不同判断。
  记录：2026-10-05；interest / historical / conversation_topic；historical；来源 S002
- **LE021** 近期阅读讨论根据证据修正判断，记录原判断、预期、实际结果、其他解释和修正决定。
  记录：2026-10-10；interest / historical / conversation_topic；historical；来源 S002
- **LE022** 近期阅读讨论知识来源、提取过程、计算规则和经验判断的可追溯性。
  记录：2026-10-11；interest / historical / conversation_topic；historical；来源 S002
- **LE023** 近期阅读讨论不同视角和模型的适用前提、盲区，以及开发者、使用者、购买者的不同关注点。
  记录：2026-10-15；interest / historical / conversation_topic；historical；来源 S002

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

## 公司与业务经营

- **BU001** 已明确拥有内地与香港两家公司，并表示认真创业、长期经营。
  记录：2026-08-28；fact / historical / memory_summary；historical；来源 S001
- **BU002** 内地公司业务方向历史记录含技术服务、研发、AI与系统集成；法定经营范围未核对。
  记录：2025-09-29；fact / historical / memory_summary；historical；来源 S001
- **BU003** 曾报告内地ICP与EDI认证或许可相关工作完成；本轮未核验证照及其有效期。
  记录：2026-08-28；fact / historical / memory_summary；historical；来源 S001
- **BU004** 曾报告已建立中英文双域名；域名对应产品见说明书，当前解析状态未查。
  记录：2026-09-01；fact / historical / memory_summary；historical；来源 S001
- **BU005** 经营需承担两家公司、财税、域名服务器、代码签名、开发与推广等持续成本。
  记录：2026-08-28；fact / historical / memory_summary；historical；来源 S001
- **BU007** 历史上选择香港公司作为Stripe与海外业务结算路径；不代表Stripe账户已开通。
  记录：2025-10-01；fact / historical / retrieved_user_statement；historical；来源 S003
- **BU008** “内地负责研发交付、香港负责全球市场品牌与收款”是历史助手的组织分工建议，未见用户逐项确认已实施。
  记录：2026-07-18；inference / candidate / assistant_inference；dated_record；来源 S003
- **BU009** 香港公司官网需求定位为面向全球企业的AI自动化与软件解决方案，覆盖定制开发、电商自动化、SaaS和流程集成；第一版英文优先。
  记录：2026-05-08；requirement / documented / document_requirement；dated_record；来源 S009
- **BU010** 香港公司官网需求聚焦高价值技术服务，要求不虚构客户和成果；不把需求中的Next.js/TypeScript/Tailwind/Vercel推荐栈当作已上线技术栈。
  记录：2026-05-08；constraint / documented / document_requirement；dated_record；来源 S009

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

## 其他产品项目

- **PR001** 工程资料线上平台方向包含注册、项目发布/上传、初审终审、状态跟踪、广告和结算。
  记录：2026-04-25；fact / historical / memory_summary；historical；来源 S001
- **PR002** 工程资料平台要求防外部私下交易，沟通、文件、审核、验收和结算留痕。
  记录：2026-04-25；fact / historical / memory_summary；historical；来源 S001
- **PR003** 人员标签记录含年限、A–D等级、ZZ/LZ状态、GS/DFGL/FJ/SZ/TL方向，以及路基、桥梁、隧道、路面、房建、市政等专业；缩写确切释义待确认。
  记录：2026-04-25；fact / historical / memory_summary；historical；来源 S001
- **PR004** U盘绑定项目方向涉及全国项目、权限分级及工程平台对接；不能推定已商业交付。
  记录：2026-06-20；fact / historical / memory_summary；historical；来源 S001
- **PR005** 国际技术人员协作平台方向希望统一业务、代码与人员管理，对标Monday。
  记录：2026-06-18；fact / historical / memory_summary；historical；来源 S001
- **PR006** 企业知识管理系统方向包含审核入库、Dashboard与接入LLM Wiki。
  记录：2026-05-15；fact / historical / memory_summary；historical；来源 S001
- **PR007** 有Python脚本按工程部位/用途拆分PDF的任务。
  记录：2026-09-03；fact / historical / memory_summary；historical；来源 S001
- **PR008** 曾询问企业版Teams注册与登录，不据此认定已部署企业租户。
  记录：2026-10-01；fact / historical / memory_summary；historical；来源 S001
- **PR009** 曾讨论WorkBuddy安装、观察其工作与用其开发微信小程序；没有结果证明这些流程已运行。
  记录：日期未知；fact / historical / memory_summary；undated；来源 S001
- **PR010** 工程资料平台允许用户选择或同时拥有甲乙双方身份，但同一项目交易角色固定；这是历史用户提出的规则。
  记录：2026-04-25；requirement / documented / retrieved_user_statement；dated_record；来源 S003

## 内容与个人品牌

- **CT001** 英文技术自媒体频道品牌为Elvis Builds AI。
  记录：2026-05-04；fact / historical / memory_summary；historical；来源 S001
- **CT002** 个人品牌与全球合作渠道方向包括YouTube、Twitter/X、Facebook、GitHub和自建网站。
  记录：日期未知；fact / historical / memory_summary；undated；来源 S001
- **CT003** 视频工具实践或关注包括Descript、OBS与ElevenLabs；近期也使用Pika生成宣传视频。
  记录：日期未知；fact / historical / memory_summary；undated；来源 S001
- **CT004** 国内推广渠道方向包括抖音、视频号和小红书。
  记录：日期未知；fact / historical / memory_summary；undated；来源 S001
- **CT005** OfficeFlow中文短宣传希望使用一致男声，减少重复并控制在22秒以内。
  记录：2026-10-18；fact / historical / memory_summary；historical；来源 S001
- **CT006** 曾要求制作Windows、Android、iOS、macOS、Linux五大系统宣传图；不能由此认定已有跨五系统产品。
  记录：2026-10-15；fact / historical / memory_summary；historical；来源 S001
- **CT007** 曾请求日落海边骑车、铁路道口和小火车场景的唯美日常系动漫短片，并要求蝉鸣、车铃和柔和钢琴。
  记录：2026-10-18；fact / historical / memory_summary；historical；来源 S001
- **CT008** 为YouTube频道Elvis Builds AI要求过视频水印，文件小于1MB；EBA与具体视觉尺寸是当时助手建议，未获逐项确认。
  记录：2026-05-05；preference / historical / retrieved_user_statement；historical；来源 S003
- **CT009** 关注guoer.xyz工程自动化工具展示与个人品牌、SaaS产品矩阵、Newsletter及转化漏斗的结合；本轮没有核验该域名现有内容。
  记录：2026-05-07；interest / historical / retrieved_user_statement；historical；来源 S003

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

## 设备与工具使用

- **DE001** 自述已购买MacBook Pro。
  记录：2026-10-14；fact / historical / user_quote；historical；来源 S002
- **DE002** 曾询问是否有必要购买Mac mini；没有已购买Mac mini的证据。
  记录：2026-10-14；fact / historical / user_quote；historical；来源 S002
- **DE003** 在学习macOS日常操作，询问当前文件夹打开终端和不用鼠标滚动的方法。
  记录：2026-10-09；fact / historical / user_quote；historical；来源 S002
- **DE004** 曾要求用Desktop Commander Remote查找Downloads中最大的5个文件。
  记录：2026-10-18；fact / historical / user_quote；historical；来源 S002

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

