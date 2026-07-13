# 保护您的生成式AI应用程序

[![保护您的生成式AI应用程序](../../../translated_images/zh-CN/13-lesson-banner.14103e36b4bbf173.webp)](https://youtu.be/m0vXwsx5DNg?si=TYkr936GMKz15K0L)

## 介绍

本课将涵盖：

- AI系统背景下的安全性。
- AI系统的常见风险和威胁。
- 保护AI系统的方法和注意事项。

## 学习目标

完成本课后，您将了解：

- AI系统的威胁和风险。
- 保护AI系统的常见方法和做法。
- 如何通过实施安全测试，防止意外结果和用户信任流失。

## 生成式AI背景下安全性的含义是什么？

随着人工智能（AI）和机器学习（ML）技术越来越多地影响我们的生活，保护不仅仅是客户数据，还有AI系统本身变得至关重要。AI/ML越来越多地用于支持高价值的决策过程，尤其在错误决策可能导致严重后果的行业中。

以下是关键要点：

- **AI/ML的影响**：AI/ML对日常生活产生重大影响，因此保障其安全已变得不可或缺。
- <strong>安全挑战</strong>：AI/ML所产生的影响需要适当关注，以保护基于AI的产品免遭复杂攻击，无论是由网络喷子还是有组织群体发起的攻击。
- <strong>战略问题</strong>：科技行业必须主动应对战略挑战，以确保客户长期安全和数据安全。

此外，机器学习模型很大程度上无法区分恶意输入和良性异常数据。大量训练数据来自未经筛选、未审核的公共数据集，这些数据集允许第三方贡献。攻击者不需要破坏数据集，只需自由贡献数据即可。随着时间推移，低置信度的恶意数据若数据结构/格式正确，会变成高置信度的可信数据。

因此，确保模型用于决策的数据存储的完整性和保护至关重要。

## 了解AI的威胁和风险

在AI及相关系统中，数据投毒是目前最重要的安全威胁。数据投毒是指有人故意更改用于训练AI的信息，导致AI做出错误判断。这是因为缺乏标准化的检测和缓解方法，加之我们依赖不可信或未经筛选的公共数据集进行训练。为维护数据完整性、防止有缺陷的训练过程，关键是追踪数据的来源和血缘。否则，“垃圾进，垃圾出”这一老话依然成立，导致模型性能受损。

以下是数据投毒如何影响模型的例子：

1. <strong>标签翻转</strong>：在二分类任务中，攻击者故意翻转少量训练数据的标签。例如，将良性样本标记为恶意，导致模型学习错误关联。\
   <strong>例子</strong>：垃圾邮件过滤器因标签被操纵，将合法邮件误判为垃圾邮件。
2. <strong>特征投毒</strong>：攻击者微妙地篡改训练数据中的特征，以引入偏见或误导模型。\
   <strong>例子</strong>：向产品描述中添加无关关键词，以操纵推荐系统。
3. <strong>数据注入</strong>：向训练集注入恶意数据以影响模型行为。\
   <strong>例子</strong>：引入虚假用户评论来扭曲情感分析结果。
4. <strong>后门攻击</strong>：攻击者在训练数据中插入隐藏模式（后门）。模型学习识别该模式并在触发时表现出恶意行为。\
   <strong>例子</strong>：用于人脸识别系统的带有后门的图像导致对特定人物识别错误。

MITRE公司创建了[ATLAS（人工智能系统对抗威胁态势）](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst)，这是一个关于现实中攻击AI系统的对抗者使用战术和技术的知识库。

> 随着AI被越来越多地整合进各种系统，AI驱动系统中出现的漏洞数量持续增加，超出传统网络攻击的攻击面范围。我们开发了ATLAS，以提高对这些独特且不断发展的漏洞的认识。ATLAS基于MITRE ATT&CK®框架构建，其战术、技术和程序（TTPs）与ATT&CK互补。

类似于广泛应用于传统网络安全中的MITRE ATT&CK®框架，ATLAS提供了易于搜索的TTP集合，帮助更好地理解和准备防御新兴攻击。

此外，开放式网络应用程序安全项目（OWASP）制定了利用大型语言模型（LLM）的应用中的“[十大漏洞](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)”清单。该列表强调了诸如前述数据投毒风险以及：

- <strong>提示注入</strong>：攻击者通过精心设计的输入操纵大型语言模型，使其行为偏离预期。
- <strong>供应链漏洞</strong>：组成LLM使用的应用程序的组件和软件（如Python模块或外部数据集）本身可能被破坏，导致意外结果、引入偏见甚至基础设施的漏洞。
- <strong>过度依赖</strong>：LLM易出错且可能产生幻觉，提供不准确或不安全的结果。在多个已纪录的案例中，人们采信了这些结果，导致现实中的负面后果。

微软云倡导者Rod Trent撰写了免费电子书[必须学习的AI安全](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst)，深入探讨这些及其他新兴AI威胁，并提供了广泛的应对指导。

## AI系统与LLM的安全测试

人工智能（AI）正在改变多个领域和行业，为社会带来新的可能性和益处。然而，AI也带来了重大挑战和风险，如数据隐私、偏见、缺乏可解释性和潜在滥用。因此，确保AI系统的安全和负责至关重要，即遵守伦理和法律标准，并赢得用户与利益相关者的信任。

安全测试是评估AI系统或LLM安全性的过程，通过识别和利用其漏洞。这可以由开发者、用户或第三方审计员执行，视测试目的和范围而定。针对AI系统和LLM的一些常见安全测试方法包括：

- <strong>数据清理</strong>：从训练数据或AI系统/LLM输入中删除或匿名化敏感或私人信息。数据清理有助于预防数据泄漏和恶意操纵，减少机密或个人数据的暴露。
- <strong>对抗测试</strong>：生成并应用对抗样本至AI系统或LLM的输入或输出，以评估其在对抗攻击下的鲁棒性和韧性。对抗测试有助于识别并缓解AI系统或LLM可能被攻击者利用的漏洞和弱点。
- <strong>模型验证</strong>：验证AI系统或LLM的模型参数或架构的正确性和完整性。模型验证有助于检测和防止模型被盗用，确保模型受到保护和认证。
- <strong>输出验证</strong>：验证AI系统或LLM输出的质量和可信性。输出验证有助于检测和纠正恶意操纵，确保输出一致且准确。

OpenAI作为AI系统的领导者，设立了一系列_安全评估_作为其红队网络计划的一部分，旨在测试AI系统输出，促进AI安全。

> 评估可以从简单的问答测试到更复杂的模拟。以下是OpenAI开发的一些示例评估，用于从多个角度评估AI行为：

#### 说服力

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst)：AI系统在多大程度上能欺骗另一个AI系统说出秘密词？
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst)：AI系统能多好地说服另一个AI系统捐款？
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst)：AI系统能多好地影响另一个AI系统对政治提案的支持？

#### 隐写术（隐藏信息）

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst)：AI系统在多大程度上可以在不被另一个AI系统发现的情况下传递秘密信息？
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst)：AI系统在压缩和解压消息以隐藏秘密信息方面的能力如何？
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst)：AI系统能多好地与另一个AI系统协调，而无需直接通信？

### AI安全

我们必须致力于保护AI系统免受恶意攻击、滥用或意外后果。这包括采取措施确保AI系统的安全性、可靠性和可信度，例如：

- 保护用于训练和运行AI模型的数据和算法
- 防止未经授权的访问、操纵或破坏AI系统
- 发现并减轻AI系统中的偏见、歧视或伦理问题
- 确保AI决策和行动的问责性、透明度和可解释性
- 使AI系统的目标和价值观与人类及社会保持一致

AI安全对于确保AI系统和数据的完整性、可用性和机密性至关重要。AI安全的挑战与机遇包括：

- 机遇：将AI纳入网络安全战略，因为它能在识别威胁和提高响应速度方面发挥关键作用。AI可帮助自动化和增强对网络攻击（如网络钓鱼、恶意软件或勒索软件）的检测和缓解。
- 挑战：对手也可能利用AI发起复杂攻击，如生成虚假或误导性内容、冒充用户或利用AI系统的漏洞。因此，AI开发者承担设计健壮且抗滥用系统的独特责任。

### 数据保护

LLM可能对其使用的数据的隐私和安全构成风险。例如，LLM可能记忆并泄露训练数据中的敏感信息，如个人姓名、地址、密码或信用卡号码。它们也可能被恶意行为者操纵或攻击，以利用其漏洞或偏见。因此，认识这些风险并采取适当措施保护LLM使用的数据非常重要。以下是保护与LLM使用的数据的若干步骤：

- **限制与LLM共享的数据量和类型**：仅共享必要且相关的数据，避免共享任何敏感、机密或个人数据。用户还应对与LLM共享的数据进行匿名化或加密，例如删除或屏蔽任何身份信息，或使用安全通信渠道。
- **验证LLM生成的数据**：始终检查LLM生成输出的准确性和质量，确保其不含任何不必要或不适当的信息。
- <strong>报告和警示任何数据泄露或事件</strong>：警惕LLM产生的任何可疑或异常活动或行为，如生成无关、不准确、冒犯或有害的文本，这可能表明数据泄露或安全事件。

数据安全、治理和合规对任何希望在多云环境中利用数据和AI力量的组织都是关键。保护和治理所有数据是一项复杂多面的任务。您需要在多个云上保护和治理不同类型的数据（结构化、非结构化以及由AI生成的数据），同时需要考虑现有和未来的数据安全、治理及AI法规。为保护您的数据，您需要采取一些最佳实践和预防措施，例如：

- 使用提供数据保护和隐私功能的云服务或平台。
- 使用数据质量和验证工具检查数据中的错误、不一致或异常。
- 使用数据治理和伦理框架，确保负责任和透明地使用数据。

### 模拟现实威胁 - AI红队演练
模拟现实世界的威胁现在被认为是构建有韧性 AI 系统的标准做法，通过使用类似的工具、战术和程序来识别系统风险并测试防御者的响应。

> AI 红队实践已经发展出更广泛的含义：它不仅涵盖安全漏洞的探测，还包括其他系统故障的探测，如生成潜在有害内容。AI 系统带来了新的风险，红队是理解这些新颖风险的核心，例如提示注入和产生无依据的内容。- [微软 AI 红队构建更安全 AI 的未来](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

[![红队指导和资源](../../../translated_images/zh-CN/13-AI-red-team.642ed54689d7e8a4.webp)]()

以下是塑造微软 AI 红队项目的关键见解。

1. **AI 红队的广泛范围：**  
   AI 红队现在涵盖安全和负责任 AI（RAI）结果。传统上，红队关注安全方面，将模型视为攻击向量（例如，窃取底层模型）。然而，AI 系统引入了新型安全漏洞（例如，提示注入、投毒），需要特别关注。除了安全之外，AI 红队还探测公平性问题（例如，刻板印象）和有害内容（例如，暴力美化）。及早发现这些问题有助于优先投入防御资源。
2. **恶意和良性失败：**  
   AI 红队考虑来自恶意和良性视角的失败。例如，在对新必应进行红队测试时，我们不仅探讨恶意对手如何破坏系统，还考虑普通用户如何遇到问题或有害内容。与传统安全红队主要关注恶意行为者不同，AI 红队涵盖了更广泛的人物角色和潜在失败。
3. **AI 系统的动态特性：**  
   AI 应用持续演进。在大型语言模型应用中，开发者会适应不断变化的需求。持续的红队测试确保对不断演变的风险保持警惕并进行调整。

AI 红队并非万能，应该作为补充手段，与其他控制措施如[基于角色的访问控制 (RBAC)](https://learn.microsoft.com/azure/ai-services/openai/how-to/role-based-access-control?WT.mc_id=academic-105485-koreyst)和全面的数据管理解决方案配合使用。它旨在补充一种安全策略，该策略专注于使用安全且负责任的 AI 解决方案，兼顾隐私和安全，同时努力减少偏见、有害内容和可能削弱用户信任的错误信息。

以下是一些可以帮助你更好理解红队如何识别和缓解 AI 系统风险的额外阅读：

- [为大型语言模型（LLM）及其应用规划红队](https://learn.microsoft.com/azure/ai-services/openai/concepts/red-teaming?WT.mc_id=academic-105485-koreyst)
- [什么是 OpenAI 红队网络？](https://openai.com/blog/red-teaming-network?WT.mc_id=academic-105485-koreyst)
- [AI 红队——构建更安全、更负责任 AI 解决方案的关键实践](https://rodtrent.substack.com/p/ai-red-teaming?WT.mc_id=academic-105485-koreyst)
- MITRE [ATLAS（人工智能系统敌对威胁态势）](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst)，这是一个知识库，列举了对手在现实攻击 AI 系统时采用的战术和技术。

## 知识检测

维护数据完整性和防止滥用的有效方法是什么？

1. 对数据访问和数据管理实行严格的基于角色的控制  
1. 实施并审计数据标注以防止数据错误表示或滥用  
1. 确保你的 AI 基础设施支持内容过滤

答案：1。虽然上述三项建议都很好，但确保为用户分配适当的数据访问权限对于防止大型语言模型所用数据的操控和错误表示至关重要。

## 🚀 挑战

深入了解如何在 AI 时代[治理和保护敏感信息](https://learn.microsoft.com/training/paths/purview-protect-govern-ai/?WT.mc_id=academic-105485-koreyst)。

## 干得好，继续学习

完成本课后，请查看我们的[生成式 AI 学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，继续提升你的生成式 AI 知识！

接下来进入第14课，我们将探讨[生成式 AI 应用生命周期](../14-the-generative-ai-application-lifecycle/README.md?WT.mc_id=academic-105485-koreyst)！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->