# Elvis Context OS · general

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

