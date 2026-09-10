# 构建低代码 AI 应用程序

[![构建低代码 AI 应用程序](../../../translated_images/zh-CN/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(点击上方图片查看本课视频)_

## 介绍

既然我们已经学习了如何构建图像生成应用程序，让我们来讲讲低代码。生成式 AI 可以用于包括低代码在内的多种不同领域，但什么是低代码，我们又如何将 AI 添加到低代码中呢？

通过低代码开发平台，传统开发者和非开发者构建应用程序和解决方案变得更加容易。低代码开发平台使您几乎不需要编码即可构建应用程序和解决方案。这是通过提供可视化开发环境实现的，该环境允许您通过拖放组件构建应用程序和解决方案。这使您能够更快、更省资源地构建应用程序和解决方案。在本课中，我们将深入探讨如何使用低代码以及如何使用 Power Platform 利用 AI 增强低代码开发。

Power Platform 为组织提供了通过直观的低代码或无代码环境赋能其团队构建自有解决方案的机会。该环境简化了构建解决方案的过程。借助 Power Platform，解决方案可以在几天或几周内完成，而非几个月或几年。Power Platform 由五个关键产品组成：Power Apps、Power Automate、Power BI、Power Pages 和 Copilot Studio。

本课内容包括：

- 介绍 Power Platform 中的生成式 AI
- 介绍 Copilot 及其使用方法
- 使用生成式 AI 构建 Power Platform 中的应用和流程
- 了解 Power Platform 中 AI Builder 的 AI 模型
- 使用 Microsoft Copilot Studio 构建智能代理

## 学习目标

本课结束时，您将能够：

- 了解 Copilot 在 Power Platform 中的工作原理。

- 为我们的教育创业公司构建一个学生作业跟踪应用。

- 构建一个使用 AI 提取发票信息的发票处理流程。

- 在使用 GPT 创建文本 AI 模型时应用最佳实践。

- 了解 Microsoft Copilot Studio 是什么以及如何用它构建智能代理。

本课中您将使用的工具和技术有：

- **Power Apps**，用于学生作业跟踪应用，提供低代码开发环境来构建用于跟踪、管理和交互数据的应用。

- **Dataverse**，用于存储学生作业跟踪应用的数据，Dataverse 提供一个低代码数据平台来存储应用的数据。

- **Power Automate**，用于发票处理流程，提供低代码开发环境构建自动化处理发票的工作流。

- **AI Builder**，用于发票处理 AI 模型，您将使用预构建的 AI 模型来处理我们创业公司的发票。

## Power Platform 中的生成式 AI

利用生成式 AI 增强低代码开发和应用是 Power Platform 的核心焦点。目标是让每个人都能构建 AI 驱动的应用、网站、仪表板并自动化流程，_无需具备任何数据科学专业知识_。这一目标通过将生成式 AI 集成到 Power Platform 低代码开发体验中，以 Copilot 和 AI Builder 的形式实现。

### 这是如何工作的？

Copilot 是一个 AI 助手，您可以通过自然语言以一系列对话步骤描述您的要求，从而构建 Power Platform 解决方案。例如，您可以指示 AI 助手说明您的应用将使用哪些字段，它会创建应用及其底层数据模型；您还可以指定如何设置 Power Automate 流程。

您还可以在您的应用屏幕中使用 Copilot 驱动的功能，允许用户通过对话交互发现洞见。

AI Builder 是 Power Platform 中可用的低代码 AI 功能，允许您使用 AI 模型帮助自动化流程和预测结果。借助 AI Builder，您可以将 AI 应用到连接了 Dataverse 或各种云数据源（如 SharePoint、OneDrive 或 Azure）的应用和流程中。

Copilot 在所有 Power Platform 产品中均可用：Power Apps、Power Automate、Power BI、Power Pages 和 Copilot Studio（前身为 Power Virtual Agents）。AI Builder 可在 Power Apps 和 Power Automate 中使用。本课重点讲解如何在 Power Apps 和 Power Automate 中使用 Copilot 和 AI Builder，构建我们教育创业公司的解决方案。

### Power Apps 中的 Copilot

作为 Power Platform 的一部分，Power Apps 提供低代码开发环境，用于构建跟踪、管理和交互数据的应用。它是一套应用开发服务，拥有可扩展的数据平台，并能连接云服务和本地数据。Power Apps 允许您构建在浏览器、平板和手机上运行的应用，并能与同事共享。Power Apps 通过简单界面降低用户应用开发门槛，使每个业务用户或专业开发者都能构建定制应用。通过 Copilot，应用开发体验得到生成式 AI 的增强。

Power Apps 中的 Copilot AI 助手功能允许您描述需要什么样的应用、应用需要跟踪、收集或展示哪些信息。Copilot 会根据您的描述生成响应式 Canvas 应用，您之后可以自定义该应用以满足需求。AI Copilot 还会生成并建议一个 Dataverse 表，包含用于存储所需跟踪数据的字段和一些示例数据。本课稍后将介绍 Dataverse 及其在 Power Apps 中的使用。您可通过对话步骤使用 AI Copilot 助手功能自定义该表以满足需求。此功能可从 Power Apps 主页轻松访问。

### Power Automate 中的 Copilot

作为 Power Platform 的一部分，Power Automate 让用户能够创建应用和服务间的自动化工作流。它帮助自动化重复的业务流程，如沟通、数据收集和决策审批。其简洁的界面使各种技术水平的用户（从初学者到资深开发者）都能自动化工作任务。通过 Copilot，工作流开发体验也得到生成式 AI 加持。

Power Automate 中的 Copilot AI 助手功能允许您描述需要什么样的流程以及流程需执行哪些操作。Copilot 会根据您的描述生成流程，您可以自定义该流程以满足需求。AI Copilot 还会生成并建议执行所需任务的操作。本课稍后将介绍工作流及其在 Power Automate 中的使用。您可以通过对话步骤使用 AI Copilot 助手功能自定义操作以满足需求。此功能可从 Power Automate 主页轻松访问。

## 使用 Microsoft Copilot Studio 构建智能代理

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst)（前身为 Power Virtual Agents）是 Power Platform 的低代码成员，用于构建<strong>AI 代理</strong>——对话式 Copilot，能够回答问题、执行操作并代表用户自动化任务。与 Power Platform 其他部分一样，您在一个以视觉和自然语言为先的体验中构建这些代理：您描述代理所需做的事情，Copilot Studio 帮助搭建其指令、知识和操作框架。

对于我们的教育创业公司，您可以构建一个代理，回答学生关于课程的问题，检查作业截止日期，甚至给讲师发送电子邮件——所有这些都无需编写代码。

以下是使 Copilot Studio 功能强大的部分最新能力：

- <strong>从您的知识生成答案</strong>。无需手动撰写每段对话，您可以连接<strong>知识源</strong>——公共网站、SharePoint、OneDrive、Dataverse、上传的文件或通过连接器接入的企业数据——代理将从中生成有根据的答案。

- <strong>生成式协调</strong>。代理不依赖严格的触发短语，而是使用 AI 理解请求，并动态决定组合哪些知识、主题和操作来满足请求，包括串联多个步骤。

- <strong>操作和连接器</strong>。代理不仅仅是聊天，还能“做”事情。您可以为代理提供支持 1500 多个预构建 Power Platform 连接器、Power Automate 流程、自定义 REST API、提示语或<strong>模型上下文协议 (MCP)</strong> 服务器的操作。

- <strong>自治代理</strong>。代理不限于聊天窗口响应。您可以构建<strong>自治代理</strong>，由事件触发（如新邮件、Dataverse 中新记录或文件上传），然后在后台执行任务。

- <strong>多代理协调</strong>。代理可以调用其他代理。Copilot Studio 代理可以交接给其他代理，或通过其他代理扩展，包括发布到 Microsoft 365 Copilot 的代理和在 Microsoft Foundry 中构建的代理。

- <strong>模型选择</strong>。除了内置模型，您还可以从 Microsoft Foundry 模型目录引入模型，定制代理的推理和响应方式。

- <strong>多渠道发布</strong>。构建完成后，代理可以发布到多个渠道——Microsoft Teams、Microsoft 365 Copilot、网站或自定义应用等，安全性、身份验证和分析通过 Power Platform 管理体验管理。

您可以在 [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst) 开始构建您的第一个代理，并在[Microsoft Copilot Studio 文档](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst)了解更多。

## 作业：使用 Copilot 管理我们创业公司的学生作业和发票

我们的创业公司为学生提供在线课程。创业公司业务迅速增长，现正努力应对课程需求。创业公司聘请您作为 Power Platform 开发者，帮助构建低代码解决方案以管理学生作业和发票。解决方案应能帮助他们通过应用跟踪和管理学生作业，并通过工作流自动化发票处理过程。要求您使用生成式 AI 开发该解决方案。

在开始使用 Copilot 时，您可以使用 [Power Platform Copilot 提示库](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko)入门。此库包含您可用于构建 Copilot 应用和流程的提示列表。您也可以使用库中的提示，了解如何向 Copilot 描述您的需求。

### 为我们的创业公司构建学生作业跟踪应用

我们创业公司的教育者一直难以跟踪学生作业。他们一直使用电子表格记录作业，但随着学生数量增加，管理变得困难。他们请您构建一个应用，帮助跟踪和管理学生作业。该应用应允许他们添加新作业、查看作业、更新作业和删除作业。应用还应使教育者和学生能够查看已评分和未评分作业。

您将按以下步骤使用 Power Apps 中的 Copilot 构建该应用：

1. 进入 [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) 主页。

1. 在主页的文本区描述您想构建的应用。例如，**_我想构建一个用于跟踪和管理学生作业的应用_**。点击<strong>发送</strong>按钮将提示发送给 AI Copilot。

![描述您想构建的应用](../../../translated_images/zh-CN/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. AI Copilot 会建议一个 Dataverse 表，包含您需要的字段来存储所需跟踪的数据和一些示例数据。您可以随后通过对话式步骤使用 AI Copilot 助手功能自定义该表以满足您的需求。

   > <strong>重要</strong>：Dataverse 是 Power Platform 的底层数据平台。它是一个低代码数据平台，用于存储应用的数据。它是一个完全托管的服务，安全地在微软云中存储数据，并在您的 Power Platform 环境中配置。它内置了数据治理功能，如数据分类、数据血缘、细粒度访问控制等。您可以在[这里](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko)了解有关 Dataverse 的更多信息。

   ![新表中建议的字段](../../../translated_images/zh-CN/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. 教育者想给提交作业的学生发送电子邮件，通知他们作业的进度。您可以使用 Copilot 向表中添加新字段以存储学生电子邮件。例如，可以使用以下提示添加新字段：**_我想添加一列来存储学生电子邮件_**。点击<strong>发送</strong>按钮将提示发送给 AI Copilot。

![添加新字段](../../../translated_images/zh-CN/copilot-new-column.35e15ff21acaf274.webp)

1. AI Copilot 会生成一个新字段，您可随后自定义该字段以满足需求。


1. 完成表格后，点击 <strong>创建应用</strong> 按钮以创建应用。

1. AI 助理将根据您的描述生成一个响应式 Canvas 应用。然后您可以自定义该应用以满足您的需求。

1. 对于教育工作者向学生发送电子邮件，您可以使用助理向应用添加新屏幕。例如，您可以使用以下提示向应用添加新屏幕：**_我想添加一个发送电子邮件给学生的屏幕_**。点击 <strong>发送</strong> 按钮将提示发送给 AI 助理。

![通过提示指令添加新屏幕](../../../translated_images/zh-CN/copilot-new-screen.2e0bef7132a17392.webp)

1. AI 助理将生成一个新屏幕，您可以根据需要自定义该屏幕。

1. 完成应用后，点击 <strong>保存</strong> 按钮保存应用。

1. 若要与教育工作者共享应用，点击 <strong>共享</strong> 按钮，然后再次点击 <strong>共享</strong> 按钮。您可以通过输入他们的电子邮件地址来分享应用。

> <strong>你的作业</strong>：您刚刚构建的应用是一个良好的开始，但还可以改进。通过电子邮件功能，教育工作者只能手动输入学生的电子邮件来发送邮件。您能否利用助理构建一个自动化，使教育工作者在学生提交作业时自动向学生发送电子邮件？提示是，通过合适的提示，您可以在 Power Automate 中使用助理来实现这一点。

### 为我们的初创公司构建发票信息表

我们初创公司的财务团队一直在努力跟踪发票。他们一直使用电子表格来跟踪发票，但随着发票数量的增加，管理变得越来越困难。他们请您构建一个表格，帮助他们存储、跟踪和管理收到的发票信息。该表格应用于构建一个自动化流程，以提取所有发票信息并存储在表格中。该表格还应使财务团队能够查看已付款和未付款的发票。

Power Platform 基于一个叫 Dataverse 的底层数据平台，使您能够为应用和解决方案存储数据。Dataverse 提供了一个低代码数据平台，用于存储应用的数据。它是一个完全托管的服务，安全地在 Microsoft 云中存储数据，并在您的 Power Platform 环境中进行配置。它带有内置的数据治理功能，如数据分类、数据血缘、细粒度访问控制等。您可以在这里了解更多 [关于 Dataverse 的信息](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko)。

为什么我们的初创公司应使用 Dataverse？Dataverse 中的标准和自定义表为您的数据提供安全的云端存储选项。表允许您存储不同类型的数据，类似于您在一个 Excel 工作簿中使用多个工作表。您可以使用表来存储特定于组织或业务需求的数据。我们初创公司使用 Dataverse 可获得的部分优势包括但不限于：

- <strong>易于管理</strong>：元数据和数据均存储在云端，您无需担心它们的存储或管理细节。您可以专注于构建应用和解决方案。

- <strong>安全</strong>：Dataverse 为您的数据提供安全的云存储选项。您可以使用基于角色的安全性控制谁可以访问表中的数据以及如何访问。

- <strong>丰富的元数据</strong>：数据类型和关系可直接在 Power Apps 中使用。

- <strong>逻辑和验证</strong>：您可以使用业务规则、计算字段和验证规则来执行业务逻辑并保持数据准确性。

现在您知道了 Dataverse 是什么以及为什么要使用它，我们来看如何利用助理在 Dataverse 中创建一个表格，以满足我们财务团队的需求。

> <strong>注意</strong>：您将在下一节中使用此表，构建一个提取所有发票信息并将其存储到表格中的自动化流程。

使用助理在 Dataverse 中创建表格，请按照以下步骤操作：

1. 进入 [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) 主页。

2. 在左侧导航栏选择 <strong>表</strong>，然后点击 <strong>描述新表</strong>。

![选择新表](../../../translated_images/zh-CN/describe-new-table.0792373eb757281e.webp)

1. 在 <strong>描述新表</strong> 屏幕的文本区描述要创建的表。例如，**_我想创建一个用于存储发票信息的表_**。点击 <strong>发送</strong> 按钮将提示发送给 AI 助理。

![描述表格](../../../translated_images/zh-CN/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. AI 助理将建议一个 Dataverse 表，包含存储您想跟踪的数据所需的字段和一些示例数据。然后，您可以通过助理的对话式步骤功能，自定义表格以满足需求。

![建议的 Dataverse 表](../../../translated_images/zh-CN/copilot-dataverse-table.b3bc936091324d9d.webp)

1. 财务团队希望向供应商发送电子邮件，更新其发票的当前状态。您可以使用助理向表中添加一个新字段以存储供应商邮箱。例如，可以使用以下提示添加新字段：**_我想添加一个用于存储供应商邮箱的列_**。点击 <strong>发送</strong> 按钮将提示发送给 AI 助理。

1. AI 助理将生成一个新字段，您可以根据需求自定义字段。

1. 完成表格后，点击 <strong>创建</strong> 按钮创建表格。

## Power Platform 中的 AI 模型与 AI Builder

AI Builder 是 Power Platform 中的低代码 AI 功能，帮助您使用 AI 模型自动化流程和预测结果。通过 AI Builder，您可以将 AI 引入连接 Dataverse 或各种云数据源（如 SharePoint、OneDrive 或 Azure）中的数据的应用和流程。

## 预构建 AI 模型与自定义 AI 模型

AI Builder 提供两种 AI 模型：预构建 AI 模型和自定义 AI 模型。预构建 AI 模型是微软训练好并可在 Power Platform 中直接使用的模型，帮助您无需收集数据、构建、训练和发布自己的模型即可为应用和流程添加智能，实现自动化和预测。

Power Platform 中的一些预构建 AI 模型包括：

- <strong>关键短语提取</strong>：从文本中提取关键短语。
- <strong>语言检测</strong>：检测文本的语言。
- <strong>情感分析</strong>：检测文本的积极、消极、中性或混合情感。
- <strong>名片识别</strong>：从名片中提取信息。
- <strong>文本识别</strong>：从图像中提取文本。
- <strong>对象检测</strong>：检测并提取图像中的对象。
- <strong>文档处理</strong>：从表单中提取信息。
- <strong>发票处理</strong>：从发票中提取信息。

使用自定义 AI 模型，您可以将自己的模型导入 AI Builder，使其像任何 AI Builder 自定义模型一样使用，允许您用自己的数据训练模型。您可以在 Power Apps 和 Power Automate 中使用这些模型实现自动化和预测。使用自定义模型时存在一些限制。您可以查看这些[限制](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst)了解更多。

![AI Builder 模型](../../../translated_images/zh-CN/ai-builder-models.8069423b84cfc47f.webp)

## 任务 #2 - 为我们的初创公司构建发票处理流程

财务团队在处理发票方面遇到困难。他们一直使用电子表格跟踪发票，但随着发票数量增加，管理变得困难。他们要求您构建一个工作流，利用 AI 帮助处理发票。该工作流应能提取发票信息并存储到 Dataverse 表中，同时能够向财务团队发送包含提取信息的电子邮件。

现在您已经了解 AI Builder 及其使用原因，我们来看如何使用之前提到的发票处理 AI 模型，构建一个帮助财务团队处理发票的工作流。

使用 AI Builder 中的发票处理 AI 模型构建帮助财务团队处理发票的工作流，请按以下步骤操作：

1. 进入 [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst) 主页。

2. 在主页的文本区描述您想构建的工作流。例如，**_当发票到达邮箱时处理发票_**。点击 <strong>发送</strong> 按钮将提示发送给 AI 助理。

   ![Copilot Power Automate](../../../translated_images/zh-CN/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. AI 助理将建议执行任务所需的操作。您可以点击 <strong>下一步</strong> 按钮查看后续步骤。

4. 在下一步，Power Automate 会提示您设置流程所需的连接。完成后，点击 <strong>创建流程</strong> 按钮来创建该流程。

5. AI 助理将生成一个流程，您可以根据需求自定义此流程。

6. 更新流程触发器，将 <strong>文件夹</strong> 设置为存储发票的文件夹。例如，可以设置为 <strong>收件箱</strong>。点击 <strong>显示高级选项</strong>，将 <strong>仅包含附件</strong> 设置为 <strong>是</strong>。这样可以确保仅当该文件夹接收到带有附件的邮件时，流程才会运行。

7. 从流程中移除以下操作：**HTML 转文本**、<strong>组合</strong>、**组合 2**、**组合 3** 和 **组合 4**，因为您不需要使用它们。

8. 从流程中移除 <strong>条件</strong> 操作，因为您不需要使用它。流程应如以下截图所示：

   ![Power Automate 移除操作](../../../translated_images/zh-CN/powerautomate-remove-actions.7216392fe684ceba.webp)

9. 点击 <strong>添加操作</strong> 按钮，搜索 **Dataverse**，选择 <strong>添加新行</strong> 操作。

10. 在 <strong>从发票中提取信息</strong> 操作中，将 <strong>发票文件</strong> 设置为指向电子邮件中的 <strong>附件内容</strong>。这样能确保流程从发票附件中提取信息。

11. 选择您之前创建的表格。例如，选择 <strong>发票信息</strong> 表。使用上一步操作中的动态内容填写以下字段：

    - ID
    - 金额
    - 日期
    - 名称
    - 状态 - 将 <strong>状态</strong> 设为 <strong>待处理</strong>。
    - 供应商邮箱 - 使用 <strong>新邮件到达</strong> 触发器中的 <strong>发件人</strong> 动态内容。

    ![Power Automate 添加行](../../../translated_images/zh-CN/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. 完成流程后，点击 <strong>保存</strong> 按钮保存流程。然后，您可以通过向触发器指定的文件夹发送带有发票的电子邮件来测试流程。

> <strong>您的作业</strong>：您刚刚构建的流程是一个良好的开始，现在您需要思考如何构建一个自动化流程，使我们财务团队能够在发票状态变更时，向供应商发送电子邮件，更新其发票的当前状态。提示：流程必须在发票状态变化时运行。

## 在 Power Automate 中使用文本生成 AI 模型

AI Builder 中的 “使用 GPT 创建文本” AI 模型基于提示生成文本，由微软 Azure OpenAI 服务支持。借助此功能，您可以将 GPT（生成式预训练变换器）技术整合到您的应用和流程中，构建各种自动流程和智能应用。

GPT 模型经过海量数据的广泛训练，能够根据提示生成近似人类语言的文本。将其与工作流自动化集成后，像 GPT 这样的 AI 模型可以简化并自动化广泛的任务。

例如，您可以构建流程自动生成各种用例的文本，如电子邮件草稿、产品描述等。您还可以将该模型用于生成各种应用中的文本，例如支持客服代表有效高效回应客户咨询的聊天机器人和客户服务应用。

![创建提示](../../../translated_images/zh-CN/create-prompt-gpt.69d429300c2e870a.webp)


要了解如何在 Power Automate 中使用此 AI 模型，请浏览 [使用 AI Builder 和 GPT 增强智能](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko) 模块。

## 干得好！继续学习

完成本课程后，请查看我们的 [生成式 AI 学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，继续提升您的生成式 AI 知识！

想要自定义并充分利用 Copilot 吗？探索 [Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) — 一个社区贡献的指令、代理、技能和配置集合，助您最大化利用 GitHub Copilot。

前往第 11 课，我们将学习如何 [将生成式 AI 与函数调用集成](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->