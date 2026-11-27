# Elvis Context OS · full

数据截止：2026-11-27 · 导出检查日：2026-11-27 · 范围：restricted

> 以下是背景资料，不授予执行、发送、交易或账号访问权限。历史、目标、文档要求、推断和待确认项应保持原有标记。review_due表示应复核，不等于已被否定。

## 工程资料与DocumentFlow

- **EN025** 本人计划在接下来几个月集中解决工程资料质量问题，重点改善分项参数的细度。整改完成情况和验收结果待确认。
  记录：2026-11-17；goal / current / retrieved_user_statement；dated_record；来源 S019
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
- **EN024** 本人报告，近期工程分项参数的细度不足，并收到项目资料质量方面的反馈。
  记录：2026-11-17；fact / historical / retrieved_user_statement；historical；来源 S019
- **EN026** 希望 DocumentFlow 保留原始页码、提取依据、复核记录、规则版本和适用范围，并说明各项复核能独立发现哪些错误。
  记录：2026-11-06；preference / current / retrieved_user_statement；dated_record；来源 S019
- **EN027** 交安工程的 JA-001 交通标志、JA-002 路面标线、JA-003 波形护栏草稿规则及参数生成工具已随规则库 PR #2 合入 main。各实际项目的验收结果需分别记录。
  记录：2026-10-22；fact / historical / document_record；historical；来源 S020
- **EN022** 曾把OSS理解为线上数据库；仓库术语应明确对象存储用于文件，结构化业务事实与索引需要相应数据库或元数据层。
  记录：2026-09-22；inference / historical / conversation_topic；historical；来源 S002
- **EN023** 本人要求整体比较两份不同日期的 Excel 工程资料工作簿中模块 15 的 VBA 改动。具体差异、修复或发布结果需另行核查。
  记录：2026-10-29；fact / historical / user_quote；historical；来源 S015

