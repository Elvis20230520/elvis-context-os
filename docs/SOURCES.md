# 来源目录

原始文件不在此仓库复制。以下定位用于复查；账号、用户自述、方案文档和助手分析证明力不同。

## S001 · 本会话提供的跨会话记忆摘要

- 类型：conversation_summary
- 来源日期：2026-10-20
- 定位：2026-10-20 会话上下文 MEMORY_SUMMARY
- 边界：二次摘要，不是完整聊天记录；除另有原话来源外，均按历史记录而非独立核验处理。

## S002 · 本会话提供的近期用户原话摘录

- 类型：conversation_excerpt
- 来源日期：2026-10-20
- 定位：2026-10-20 会话 Recent Conversation Content
- 边界：只覆盖可见摘录；日期使用摘录日期；用户的提问不等于已实施。

## S003 · 历史对话检索补充

- 类型：personal_context_retrieval
- 来源日期：2026-10-20
- 定位：2026-10-20 个人上下文检索，convo search c0–c16
- 边界：检索摘要区分 U 用户原话与 A 助手输出；不能视为完整导出。

## S004 · DocumentFlow_AI_Gateway_Codex_Integration_PRD_v1.0.md

- 类型：document
- 来源日期：2026-09-20
- 定位：Library: libfile_a1beccef7e988191ae07fcab44e55451；本轮读第1–180行
- 边界：可执行草案；文档要求不等于已经实现；本轮只读用于定位与边界的部分。

## S005 · 2026-09_综合能力提升与IT技能树冲刺计划.md

- 类型：document
- 来源日期：2026-09-08
- 定位：Library: libfile_1e3ab1fa8df88191bc491000c3cf9447，version 2；本轮全文188行
- 边界：9月修订计划及历史实现记录的二次汇总；不是10月重新运行测试的结果。

## S006 · OfficeFlow_产品使用说明书_v1.0_客户版.docx

- 类型：document
- 来源日期：2026-09-03
- 定位：Library: libfile_05d464feac1081918d0aed4c305fe29f；本轮读取开头160行
- 边界：说明书列明中文版4.5.3/Global4.5.7；是2026-09-03文档基线，不能称为今天最新发布版本。

## S007 · Polymarket_Event_Probability_Engine_PRD_v1.2.md

- 类型：document
- 来源日期：2026-10-15
- 定位：Library: libfile_13afc85311988191ab41d3d3bdad0023；本轮读取第1–110行
- 边界：研究与概率引擎设计，引用主交易PRD但本轮未读取主PRD；不证明系统已上线或盈利。

## S008 · CI_CD_Docker_Automation_Deployment_Requirement.md

- 类型：document
- 来源日期：2026-07-21
- 定位：Library: libfile_3fef4acc04548191abeafd9e5b044288；本轮读取第1–90行
- 边界：实施需求中的协作规范；实际部署成功另有用户历史陈述。

## S009 · hk_company_website_requirements.md

- 类型：document
- 来源日期：2026-05-08
- 定位：Library: libfile_9fb20687f9648191b86853acec7ce3f8；本轮读取第1–85行
- 边界：网站需求中的业务定位和推荐技术栈，不证明官网实现/结算账号激活。

## S010 · 开源软件工具箱与产品化路线图.md

- 类型：document
- 来源日期：2026-07-26
- 定位：Library: libfile_9a544293ac688191a7c15bcdb3a2ebb6；本轮读取第1–90行
- 边界：产品化路线和能力叙述含助手归纳；工具推荐不能当作已安装使用清单。

## S011 · 已连接 GitHub 账号身份

- 类型：authenticated_account
- 来源日期：2026-10-20
- 定位：本轮 GitHub get_profile；浏览器新仓库页面 Owner
- 边界：账号登录名 Elvis20230520；不用于证明法定姓名或其他账号所有权。

## S012 · 个人数字文档系统本次建设要求

- 类型：user_message
- 来源日期：2026-10-20
- 定位：本会话用户请求
- 边界：建设要求，不能据此反推未提供的个人事实。

## S013 · 历史检索中的邮件/平台称呼线索

- 类型：external_profile_signal
- 来源日期：2026-10-20
- 定位：个人上下文检索 gmail g1/g4/g42 与 Freelancer 称呼摘要
- 边界：第三方平台称呼“邹明/Ming/Ming Zou”；未由用户在本轮确认，不作法定姓名。

## S014 · 本次系统设计中的分析与建议

- 类型：assistant_analysis
- 来源日期：2026-10-20
- 定位：2026-10-20 仓库建设过程
- 边界：用于明确标注助手建议；不能当作用户已经承诺的事项。
