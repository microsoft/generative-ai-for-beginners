<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2faf8ee7a0b851efa647a19788f1e5b",
  "translation_date": "2025-10-17T23:21:17+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "zh"
}
-->
# 保护您的生成式 AI 应用程序

[![保护您的生成式 AI 应用程序](../../../translated_images/13-lesson-banner.14103e36b4bbf17398b64ed2b0531f6f2c6549e7f7342f797c40bcae5a11862e.zh.png)](https://youtu.be/m0vXwsx5DNg?si=TYkr936GMKz15K0L)

## 介绍

本课程将涵盖以下内容：

- AI 系统中的安全性。
- AI 系统面临的常见风险和威胁。
- 保护 AI 系统的方法和注意事项。

## 学习目标

完成本课程后，您将了解：

- AI 系统面临的威胁和风险。
- 保护 AI 系统的常见方法和实践。
- 如何通过实施安全测试来防止意外结果以及用户信任的流失。

## 在生成式 AI 的背景下，安全性意味着什么？

随着人工智能（AI）和机器学习（ML）技术越来越多地影响我们的生活，保护客户数据以及 AI 系统本身变得至关重要。AI/ML 在支持高价值决策过程中被广泛应用，而错误的决策可能会导致严重后果。

以下是需要考虑的关键点：

- **AI/ML 的影响**：AI/ML 对日常生活产生了重大影响，因此保护它们变得至关重要。
- **安全挑战**：AI/ML 的影响需要适当关注，以解决保护基于 AI 的产品免受复杂攻击的需求，无论是来自恶意用户还是有组织的团体。
- **战略问题**：科技行业必须主动解决战略性挑战，以确保长期的客户安全和数据安全。

此外，机器学习模型通常无法区分恶意输入和良性异常数据。大量训练数据来源于未经筛选、未经过滤的公共数据集，这些数据集允许第三方贡献。攻击者无需破坏数据集，因为他们可以自由地向其中添加数据。随着时间的推移，如果数据结构/格式保持正确，低置信度的恶意数据可能会变成高置信度的可信数据。

因此，确保模型用于决策的数据存储的完整性和保护至关重要。

## 理解 AI 的威胁和风险

在 AI 及相关系统方面，数据投毒是当今最显著的安全威胁之一。数据投毒是指有人故意更改用于训练 AI 的信息，导致其做出错误的决策。这种情况的发生是由于缺乏标准化的检测和缓解方法，同时我们依赖于不可信或未经筛选的公共数据集进行训练。为了维护数据的完整性并防止训练过程出现问题，追踪数据的来源和传承至关重要。否则，“垃圾进，垃圾出”的老话将会应验，导致模型性能受损。

以下是数据投毒可能对您的模型产生影响的一些示例：

1. **标签翻转**：在二分类任务中，攻击者故意翻转一小部分训练数据的标签。例如，将正常样本标记为恶意样本，导致模型学习错误的关联。\
   **示例**：由于标签被操纵，垃圾邮件过滤器将合法邮件误分类为垃圾邮件。
2. **特征投毒**：攻击者微妙地修改训练数据中的特征，以引入偏差或误导模型。\
   **示例**：在产品描述中添加无关的关键词以操纵推荐系统。
3. **数据注入**：将恶意数据注入训练集以影响模型的行为。\
   **示例**：引入虚假的用户评论以扭曲情感分析结果。
4. **后门攻击**：攻击者在训练数据中插入隐藏模式（后门）。模型学习识别该模式，并在触发时表现出恶意行为。\
   **示例**：面部识别系统通过后门图像训练后错误识别特定人物。

MITRE 公司创建了 [ATLAS（人工智能系统对抗性威胁景观）](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst)，这是一个关于现实世界中针对 AI 系统攻击的战术和技术知识库。

> 随着 AI 的应用增加，AI 系统中的漏洞数量也在不断增加，因为 AI 的整合扩展了现有系统的攻击面，超出了传统网络攻击的范围。我们开发了 ATLAS，以提高对这些独特且不断发展的漏洞的认识，因为全球社区越来越多地将 AI 集成到各种系统中。ATLAS 模仿了 MITRE ATT&CK® 框架，其战术、技术和程序（TTPs）与 ATT&CK 中的内容互为补充。

与广泛用于传统网络安全的 MITRE ATT&CK® 框架类似，ATLAS 提供了一组易于搜索的 TTPs，有助于更好地理解和准备应对新兴攻击。

此外，开放 Web 应用程序安全项目（OWASP）创建了一个 "[十大列表](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)"，列出了使用 LLM 的应用程序中最关键的漏洞。该列表突出了数据投毒等威胁的风险，以及其他问题，例如：

- **提示注入**：一种技术，攻击者通过精心设计的输入操纵大型语言模型（LLM），使其行为超出预期。
- **供应链漏洞**：构成 LLM 应用程序的组件和软件（如 Python 模块或外部数据集）本身可能被破坏，导致意外结果、引入偏差，甚至影响底层基础设施的安全性。
- **过度依赖**：LLM 是不完美的，容易出现幻觉，提供不准确或不安全的结果。在一些记录的情况下，人们直接接受结果，导致意外的现实世界负面后果。

微软云倡导者 Rod Trent 撰写了一本免费电子书 [必须学习 AI 安全](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst)，深入探讨了这些和其他新兴的 AI 威胁，并提供了广泛的指导，帮助应对这些场景。

## AI 系统和 LLM 的安全测试

人工智能（AI）正在改变各个领域和行业，为社会带来新的可能性和益处。然而，AI 也带来了显著的挑战和风险，例如数据隐私、偏见、缺乏可解释性以及潜在的滥用。因此，确保 AI 系统安全且负责任至关重要，这意味着它们遵守伦理和法律标准，并能被用户和利益相关者信任。

安全测试是评估 AI 系统或 LLM 安全性的一种过程，通过识别和利用其漏洞来进行测试。这可以由开发人员、用户或第三方审计员根据测试的目的和范围进行。以下是 AI 系统和 LLM 的一些常见安全测试方法：

- **数据清理**：这是从 AI 系统或 LLM 的训练数据或输入中删除或匿名化敏感或私人信息的过程。数据清理可以通过减少机密或个人数据的暴露来防止数据泄漏和恶意操纵。
- **对抗性测试**：这是生成和应用对抗性样本到 AI 系统或 LLM 的输入或输出，以评估其对抗攻击的鲁棒性和弹性。对抗性测试可以帮助识别和缓解 AI 系统或 LLM 的漏洞和弱点，这些漏洞可能被攻击者利用。
- **模型验证**：这是验证 AI 系统或 LLM 的模型参数或架构的正确性和完整性的过程。模型验证可以通过确保模型受到保护和认证来帮助检测和防止模型被盗。
- **输出验证**：这是验证 AI 系统或 LLM 输出的质量和可靠性的过程。输出验证可以通过确保输出的一致性和准确性来帮助检测和纠正恶意操纵。

OpenAI 作为 AI 系统的领导者，已经建立了一系列 _安全评估_，作为其红队网络计划的一部分，旨在测试 AI 系统的输出，以促进 AI 安全。

> 评估可以从简单的问答测试到更复杂的模拟。例如，以下是 OpenAI 开发的样本评估，用于从多个角度评估 AI 行为：

#### 说服力

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst)：AI 系统能多好地诱骗另一个 AI 系统说出一个秘密词？
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst)：AI 系统能多好地说服另一个 AI 系统捐款？
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst)：AI 系统能多好地影响另一个 AI 系统对政治提案的支持？

#### 隐写术（隐藏信息）

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst)：AI 系统能多好地在不被另一个 AI 系统发现的情况下传递秘密信息？
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst)：AI 系统能多好地压缩和解压缩信息，以实现隐藏秘密信息？
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst)：AI 系统能多好地在没有直接通信的情况下与另一个 AI 系统协调？

### AI 安全

保护 AI 系统免受恶
模拟现实世界的威胁已成为构建具有韧性的人工智能系统的标准实践，通过使用类似的工具、策略和程序来识别系统风险并测试防御者的响应能力。

> AI红队实践的意义已经扩展：它不仅涵盖了对安全漏洞的探测，还包括对其他系统故障的探测，例如生成潜在有害内容。AI系统带来了新的风险，而红队测试是理解这些新风险的核心，例如提示注入和生成无依据内容。 - [微软AI红队构建更安全的AI未来](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

[![红队测试的指导和资源](../../../translated_images/13-AI-red-team.642ed54689d7e8a4d83bdf0635768c4fd8aa41ea539d8e3ffe17514aec4b4824.zh.png)]()

以下是塑造微软AI红队计划的关键见解。

1. **AI红队测试的广泛范围：**  
   AI红队测试现在涵盖了安全和负责任AI（RAI）的结果。传统上，红队测试专注于安全方面，将模型视为一个攻击向量（例如，窃取底层模型）。然而，AI系统引入了新的安全漏洞（例如提示注入、数据污染），需要特别关注。除了安全性之外，AI红队测试还探讨公平性问题（例如刻板印象）和有害内容（例如美化暴力）。及早识别这些问题可以帮助优先投资防御措施。

2. **恶意和非恶意故障：**  
   AI红队测试从恶意和非恶意的角度考虑故障。例如，在对新Bing进行红队测试时，我们不仅探讨恶意攻击者如何颠覆系统，还研究普通用户可能遇到的问题或有害内容。与传统安全红队测试主要关注恶意行为者不同，AI红队测试涵盖了更广泛的用户角色和潜在故障。

3. **AI系统的动态特性：**  
   AI应用程序不断发展。在大型语言模型应用中，开发者会根据不断变化的需求进行调整。持续的红队测试确保对不断演变的风险保持警惕并适应。

AI红队测试并非包罗万象，应作为其他控制措施的补充，例如[基于角色的访问控制（RBAC）](https://learn.microsoft.com/azure/ai-services/openai/how-to/role-based-access-control?WT.mc_id=academic-105485-koreyst)和全面的数据管理解决方案。它旨在补充安全策略，专注于采用安全和负责任的AI解决方案，同时考虑隐私和安全，努力减少偏见、有害内容和错误信息，这些因素可能会削弱用户信心。

以下是一些额外的阅读资源，可以帮助您更好地了解红队测试如何帮助识别和缓解AI系统中的风险：

- [规划大型语言模型（LLMs）及其应用的红队测试](https://learn.microsoft.com/azure/ai-services/openai/concepts/red-teaming?WT.mc_id=academic-105485-koreyst)  
- [什么是OpenAI红队网络？](https://openai.com/blog/red-teaming-network?WT.mc_id=academic-105485-koreyst)  
- [AI红队测试——构建更安全、更负责任AI解决方案的关键实践](https://rodtrent.substack.com/p/ai-red-teaming?WT.mc_id=academic-105485-koreyst)  
- MITRE [ATLAS（人工智能系统的对抗性威胁景观）](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst)，一个关于现实世界中针对AI系统攻击的战术和技术知识库。

## 知识检查

什么是维护数据完整性和防止滥用的良好方法？

1. 对数据访问和数据管理实施强有力的基于角色的控制  
1. 实施并审核数据标注以防止数据误表示或滥用  
1. 确保您的AI基础设施支持内容过滤  

A:1，虽然以上三项建议都很优秀，但确保为用户分配适当的数据访问权限将极大地防止数据被操纵和误表示，这些数据被LLMs使用。

## 🚀 挑战

阅读更多关于如何在AI时代[管理和保护敏感信息](https://learn.microsoft.com/training/paths/purview-protect-govern-ai/?WT.mc_id=academic-105485-koreyst)。

## 出色的工作，继续学习

完成本课后，请查看我们的[生成式AI学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，继续提升您的生成式AI知识！

前往第14课，我们将探讨[生成式AI应用生命周期](../14-the-generative-ai-application-lifecycle/README.md?WT.mc_id=academic-105485-koreyst)！

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。