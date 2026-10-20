# Elvis Context OS · full

数据截止：2026-10-20 · 导出检查日：2026-10-20 · 范围：restricted

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

