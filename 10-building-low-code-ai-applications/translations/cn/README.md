# 第十章：创建低代码的人工智能应用

[![Building Low Code AI Applications](../../images/10-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson10-gh?WT.mc_id=academic-105485-koreyst)

> _(点击该图片看本章导学视频)_

## 本章概述

现在我们已经学习了如何构建图像生成应用程序，让我们来谈谈低代码。 生成式人工智能可用于包括低代码在内的各种不同领域，但什么是低代码以及我们如何将人工智能添加到其中？

通过使用低代码开发平台，传统开发人员和非开发人员构建应用程序和解决方案变得更加容易。 低代码开发平台使您能够使用很少的代码甚至零代码来构建应用程序和解决方案。 这是通过提供可视化开发环境来实现的，该环境使您能够拖放组件来构建应用程序和解决方案。 这使您能够使用更少的资源更快地构建应用程序和解决方案。 在本章中，我们将深入探讨如何使用低代码以及如何利用 Power Platform 通过 AI 增强低代码开发。

Power Platform 为企业提供了让其团队能够通过直观的低代码或无代码环境构建自己的解决方案的方法。 此环境有助于简化构建解决方案的过程。 借助 Power Platform，可以在几天或几周内构建解决方案，而不是几个月或几年。 Power Platform 包含五个关键产品：Power Apps、Power Automate、Power BI、Power Pages 和 Power Virtual Agent。

在本章中，您将学习到：

- Power Platform 中的生成式 AI 简介
- Copilot 简介及其使用方法
- 使用生成式人工智能在 Power Platform 中构建应用程序和流程
- 使用 AI Builder 了解 Power Platform 中的 AI 模型

## 学习目标

在完成本章的学习，您将能够：

- 了解 Copilot 在 Power Platform 中的工作原理。

- 为“Our Startup”公司构建学生作业跟踪应用程序。

- 构建使用人工智能从发票中提取信息的发票处理流程。

- 使用 GPT AI 模型创建文本时应用最佳实践。

您将在本课程中使用的工具和技术是：

- **Power Apps**，用于学生作业跟踪器应用程序，它提供了一个低代码开发环境，用于构建用于跟踪、管理数据并与数据交互的应用程序。

- **Dataverse**，用于存储学生作业跟踪器应用程序的数据，其中 Dataverse 将提供一个低代码数据平台来存储应用程序的数据。

- **Power Automate**，用于发票处理流程，您将拥有用于构建工作流程以自动化发票处理流程的低代码开发环境。

- **AI Builder**，用于发票处理 AI 模型，您将使用预构建的 AI 模型来处理“Our Startup”的发票。

## Power Platform 中的生成式 AI

通过生成式 AI 增强低代码开发和应用是 Power Platform 的重点关注领域。 目标是让每个人都能够构建人工智能驱动的应用程序、网站、仪表板并利用人工智能实现流程自动化，_无需任何数据科学专业知识_。 这一目标是通过将生成式 AI 以 Copilot 和 AI Builder 的形式集成到 Power Platform 的低代码开发体验中来实现的。

### 这是如何运作的？

Copilot 是一款 AI 助手，可让您使用自然语言以一系列对话步骤描述您的需求，从而构建 Power Platform 解决方案。 例如，您可以指示 AI 助手说明您的应用程序将使用哪些字段，它将创建应用程序和底层数据模型，或者您可以指定如何在 Power Automate 中设置流程。

您可以使用 Copilot 驱动的功能作为应用程序屏幕中的一项功能，使用户能够通过对话交互发现见解。

AI Builder 是 Power Platform 中提供的低代码 AI 功能，使您能够使用 AI 模型来帮助您自动化流程并预测结果。 借助 AI Builder，您可以将 AI 引入连接到 Dataverse 或各种云数据源（例如 SharePoint、OneDrive 或 Azure）中的数据的应用程序和流程。

Copilot 适用于所有 Power Platform 产品：Power Apps、Power Automate、Power BI、Power Pages 和 Power Virtual Agent。 AI Builder 可在 Power Apps 和 Power Automate 中使用。 在本课程中，我们将重点介绍如何在 Power Apps 和 Power Automate 中使用 Copilot 和 AI Builder 为我们的教育初创公司构建解决方案。

### Power Apps 中的 Copilot

作为 Power Platform 的一部分，Power Apps 提供了一个低代码开发环境，用于构建应用程序来跟踪、管理数据并与数据交互。 它是一套应用程序开发服务，具有可扩展的数据平台以及连接到云服务和本地数据的能力。 Power Apps 允许您构建在浏览器、平板电脑和手机上运行并可以与同事共享的应用程序。 Power Apps 通过简单的界面让用户轻松进行应用程序开发，以便每个业务用户或专业开发人员都可以构建自定义应用程序。 通过 Copilot 的生成式 AI 也增强了应用程序开发体验。

Power Apps 中的 Copilot AI 助手功能使您能够描述您需要哪种类型的应用程序以及您希望应用程序跟踪、收集或显示哪些信息。 然后，Copilot 根据您的描述生成响应式 Canvas 应用程序。 然后，您可以自定义应用程序以满足您的需求。 AI Copilot 还会生成并建议一个 Dataverse 表，其中包含存储要跟踪的数据和一些示例数据所需的字段。 稍后我们将在本章中了解什么是 Dataverse 以及如何在 Power Apps 中使用它。 然后，您可以通过对话步骤使用 AI Copilot 助手功能自定义表格以满足您的需求。 通过 Power Apps 主屏幕轻松使用此功能。

### Power Automate 中的 Copilot

作为 Power Platform 的一部分，Power Automate 允许用户在应用程序和服务之间创建自动化工作流程。 它有助于自动化重复的业务流程，例如通信、数据收集和决策批准。 其简单的界面允许具有各种技术能力的用户（从初学者到经验丰富的开发人员）自动执行工作任务。 通过 Copilot 的生成式 AI 也增强了工作流程开发体验。

Power Automate 中的 Copilot AI 助手功能使您能够描述您需要哪种流程以及您希望流程执行哪些操作。 然后 Copilot 根据您的描述生成流程。 然后，您可以自定义流程以满足您的需求。 AI Copilot 还会生成并建议您执行想要自动化的任务所需的操作。 我们将在本章中稍后介绍什么是流以及如何在 Power Automate 中使用它们。 然后，您可以通过对话步骤使用 AI Copilot 助手功能自定义操作以满足您的需求。 通过 Power Automate 主屏幕轻松使用此功能。

## 作业：使用 Copilot 管理 “Our Startup” 的学生作业和发票

“Our Startup” 为学生提供在线课程。 这家初创公司发展迅速，目前正在努力满足其课程的需求。 该初创公司聘请您作为 Power Platform 开发人员，帮助他们构建低代码解决方案，以帮助他们管理学生作业和发票。 他们的解决方案应该能够帮助他们通过应用程序跟踪和管理学生作业，并通过工作流程自动化发票处理过程。 您被要求使用生成式人工智能来开发解决方案。

当您开始使用 Copilot 时，可以使用 [Power Platform Copilot Prompt 库](https://pnp.github.io/powerplatform-prompts/?WT.mc_id=academic-109639-somelezediko) 作为提示词。 该库包含一系列提示，您可以使用这些提示与 Copilot 一起构建应用程序和流程。 您还可以使用库中的提示来了解如何向 Copilot 描述您的需求。

### 为 “Our Startup” 构建学生作业跟踪应用程序

“Our Startup” 的教育工作者一直在努力跟踪学生的作业。 他们一直使用电子表格来跟踪作业，但随着学生数量的增加，这变得难以管理。 他们要求您构建一个应用程序来帮助他们跟踪和管理学生作业。 该应用程序应使他们能够添加新作业、查看作业、更新作业和删除作业。 该应用程序还应该使教育工作者和学生能够查看已评分和未评分的作业。

您将按照以下步骤使用 Power Apps 中的 Copilot 构建应用程序：

1. 导航到 [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) 主屏幕。

1. 使用主屏幕上的文本区域描述您要构建的应用程序。 例如，**_我想构建一个应用程序来跟踪和管理学生作业_**。 单击 **发送** 按钮将提示发送到 AI Copilot。

![描述您要构建的应用程序](../../images/copilot-chat-prompt-powerapps.png?WT.mc_id=academic-105485-koreyst)

1. AI Copilot 将建议一个 Dataverse 表，其中包含存储要跟踪的数据所需的字段以及一些示例数据。 然后，您可以通过对话步骤使用 AI Copilot 助手功能自定义表格以满足您的需求。

   > **重点事项**：Dataverse 是 Power Platform 的底层数据平台。 它是一个用于存储应用程序数据的低代码数据平台。 它是一项完全托管的服务，可将数据安全地存储在 Microsoft 云中，并在您的 Power Platform 环境中进行配置。 它具有内置的数据治理功能，例如数据分类、数据沿袭、细粒度访问控制等。 您可以在[此处](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko)了解有关 Dataverse 的更多信息。

   ![新表中的建议字段](../../images/copilot-dataverse-table-powerapps.png?WT.mc_id=academic-105485-koreyst)

2. 教育工作者希望向已提交作业的学生发送电子邮件，以便让他们了解作业的最新进度。 您可以使用 Copilot 向表中添加新字段来存储学生电子邮件。 例如，您可以使用以下提示向表中添加新字段：**_我想添加一列来存储学生电子邮件_**。 单击 **发送** 按钮将提示发送到 AI Copilot。

![添加新字段](../../images/copilot-new-column.png?WT.mc_id=academic-105485-koreyst)

1. AI Copilot 将生成一个新字段，您可以自定义该字段以满足您的需求。

1. 完成表格后，单击 **创建应用程序** 按钮来创建应用程序。

1. AI Copilot 将根据您的描述生成响应式 Canvas 应用程序。 然后，您可以自定义应用程序以满足您的需求。

1. 对于要向学生发送电子邮件的教育工作者，您可以使用 Copilot 向应用程序添加新屏幕。 例如，您可以使用以下提示向应用程序添加新屏幕：**_我想添加一个屏幕来向学生发送电子邮件_**。 单击 **发送** 按钮将提示发送到 AI Copilot。

![Describe the app you want to build](../../images/copilot-new-screen.png?WT.mc_id=academic-105485-koreyst)

1. AI Copilot 将生成一个新屏幕，然后您可以自定义屏幕以满足您的需求。

1. 完成应用程序后，单击 **保存** 按钮保存应用程序。

1. 要与教育工作者共享应用程序，请单击 **共享** 按钮，然后再次单击 **共享** 按钮。 然后，您可以通过输入教育工作者的电子邮件地址与他们共享该应用程序。

> **提升**：你刚刚构建的应用程序是一个良好的开端，但还可以改进。 通过电子邮件功能，教育工作者只能通过键入电子邮件来手动向学生发送电子邮件。 您能否使用 Copilot 构建一个自动化系统，使教育工作者能够在学生提交作业时自动向他们发送电子邮件？ 您的提示是正确的提示，您可以

### 为 “Our Startup” 构建发票信息表

“Our Startup” 的财务团队一直在努力跟踪发票。 他们一直使用电子表格来跟踪发票，但随着发票数量的增加，这变得难以管理。 他们要求您构建一个表来帮助他们存储、跟踪和管理收到的发票信息。 该表应用于构建一个自动化程序，提取所有发票信息并将其存储在表中。 该表还应使财务团队能够查看已支付和未支付的发票。

Power Platform 有一个名为 Dataverse 的底层数据平台，使您能够存储应用程序和解决方案的数据。 Dataverse 提供了一个低代码数据平台来存储应用程序的数据。 它是一项完全托管的服务，可将数据安全地存储在 Microsoft 云中，并在您的 Power Platform 环境中进行配置。 它具有内置的数据治理功能，例如数据分类、数据沿袭、细粒度访问控制等。 您可以在此处了解[有关 Dataverse 的更多信息](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko)。

为什么我们的初创公司应该使用 Dataverse？ Dataverse 中的标准和自定义表为您的数据提供安全且基于云的存储选项。 表可让您存储不同类型的数据，类似于在单个 Excel 工作簿中使用多个工作表的方式。 您可以使用表来存储特定于您的组织或业务需求的数据。 我们的初创公司将从使用 Dataverse 中获得的一些好处包括但不限于：

- **易于管理**：元数据和数据都存储在云端，因此您不必担心它们如何存储或管理的细节。 您可以专注于构建您的应用程序和解决方案。

- **安全**：Dataverse 为您的数据提供安全且基于云的存储选项。 您可以使用基于角色的安全性来控制谁有权访问表中的数据以及他们如何访问数据。

- **丰富的元数据**：数据类型和关系直接在 Power Apps 中使用

- **逻辑和验证**：您可以使用业务规则、计算字段和验证规则来强制执行业务逻辑并保持数据准确性。

现在您已经了解了 Dataverse 是什么以及为什么应该使用它，让我们看看如何使用 Copilot 在 Dataverse 中创建表来满足我们财务团队的要求。

> **注意**：您将在下面内容中使用此表来构建自动化，该自动化将提取所有发票信息并将其存储在表中。

要使用 Copilot 在 Dataverse 中创建表，请按照以下步骤操作：

1. 导航到 [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) 主屏幕。

2. 在左侧导航栏上，选择 **表** ，然后单击 **描述新表** 。

![选择新表](../../images/describe-new-table.png?WT.mc_id=academic-105485-koreyst)

1. 在 **描述新表** 屏幕上，使用文本区域描述您要创建的表。 例如，**_我想创建一个表来存储发票信息_**。 单击 **发送** 按钮将提示发送到 AI Copilot。

![描述表格](../../images/copilot-chat-prompt-dataverse.png?WT.mc_id=academic-105485-koreyst)

1. AI Copilot 将建议一个 Dataverse 表，其中包含存储要跟踪的数据所需的字段以及一些示例数据。 然后，您可以通过对话步骤使用 AI Copilot 助手功能自定义表格以满足您的需求。

![建议的 Dataverse 表](../../images/copilot-dataverse-table.png?WT.mc_id=academic-105485-koreyst)

1. 财务团队希望向供应商发送电子邮件，以更新其发票的当前状态。 您可以使用 Copilot 向表中添加新字段来存储供应商电子邮件。 例如，您可以使用以下提示向表中添加新字段：**_我想添加一列来存储供应商电子邮件_**。 单击 **发送** 按钮将提示发送到 AI Copilot。

1. AI Copilot 将生成一个新字段，您可以自定义该字段以满足您的需求。

1. 完成表后，单击 **创建** 按钮创建表。

## Power Platform 中的 AI 模型与 AI Builder

AI Builder 是 Power Platform 中提供的低代码 AI 功能，使您能够使用 AI 模型来帮助您自动化流程并预测结果。 借助 AI Builder，您可以将 AI 引入连接到 Dataverse 或各种云数据源（例如 SharePoint、OneDrive 或 Azure）中的数据的应用程序和流程。

## 预定义 AI 模型与自定义 AI 模型

AI Builder 提供两种类型的 AI 模型：预构建 AI 模型和自定义 AI 模型。 预构建的 AI 模型是即用型 AI 模型，由 Microsoft 训练并在 Power Platform 中提供。 这些可以帮助您为应用程序和流程添加智能，而无需收集数据，然后构建、训练和发布您自己的模型。 您可以使用这些模型来自动化流程并预测结果。

Power Platform 中提供的一些预构建 AI 模型包括：

- **关键短语提取**：该模型从文本中提取关键短语。
- **语言检测**：此模型检测文本的语言。
- **情绪分析**：此模型检测文本中的积极、消极、中性或混合情绪。
- **名片阅读器**：此模型从名片中提取信息。
- **文本识别**：该模型从图像中提取文本。
- **对象检测**：该模型从图像中检测并提取对象。
- **表单处理**：该模型从表单中提取信息。
- **发票处理**：此模型从发票中提取信息。

通过自定义 AI 模型，您可以将自己的模型引入 AI Builder，以便它可以像任何 AI Builder 自定义模型一样运行，从而允许您使用自己的数据训练模型。 您可以使用这些模型来自动化流程并预测 Power Apps 和 Power Automate 中的结果。 使用您自己的模型时存在一些限制。 了解有关这些[限制](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst)的更多信息

![AI 构建器模型](../../images/ai-builder-models.png?WT.mc_id=academic-105485-koreyst)

## 作业 - 为 “Our Startup” 构建发票处理流程

财务团队一直在努力处理发票。 他们一直使用电子表格来跟踪发票，但随着发票数量的增加，这变得难以管理。 他们要求您构建一个工作流程，帮助他们使用人工智能处理发票。 该工作流程应使他们能够从发票中提取信息并将信息存储在 Dataverse 表中。 该工作流程还应该使他们能够向财务团队发送包含提取信息的电子邮件。

现在您已经了解了 AI Builder 是什么以及为什么应该使用它，让我们看看如何使用我们之前介绍过的 AI Builder 中的发票处理 AI 模型来构建帮助财务团队处理发票的工作流程。

要构建一个工作流程来帮助财务团队使用 AI Builder 中的发票处理 AI 模型处理发票，请按照以下步骤操作：

1. 导航至 [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst) 主屏幕。

2. 使用主屏幕上的文本区域描述您要构建的工作流程。 例如，**_当发票到达我的邮箱时对其进行处理_**。 单击 **发送** 按钮将提示发送到 AI Copilot。

   ![副驾驶电源自动化](../../images/copilot-chat-prompt-powerautomate.png?WT.mc_id=academic-105485-koreyst)

3. AI Copilot 将建议您执行想要自动化的任务所需的操作。 您可以单击 **下一步** 按钮来完成后续步骤。

4. 在下一步中，Power Automate 将提示您设置流程所需的连接。 完成后，单击 **创建流** 按钮来创建流。

5. AI Copilot 将生成流程，然后您可以自定义流程以满足您的需求。

6. 更新流程的触发器并将 **文件夹** 设置为将存储发票的文件夹。 例如，您可以将文件夹设置为**收件箱**。 单击“**显示高级选项**”并将“**仅包含附件**”设置为“**是**”。 这将确保该流程仅在文件夹中收到带有附件的电子邮件时运行。

7. 从流程中删除以下操作：**HTML 到文本**、**Compose**、**Compose 2**、**Compose 3** 和 **Compose 4**，因为您不会使用 他们。

8. 从流程中删除 **Condition** 操作，因为您不会使用它。 它应该类似于以下屏幕截图：

   ![电源自动化，删除操作](../../images/powerautomate-remove-actions.png?WT.mc_id=academic-105485-koreyst)

9. 单击 **添加操作** 按钮并搜索 **Dataverse**。 选择 **添加新行** 操作。

10. 在 **从发票中提取信息** 操作中，更新 **发票文件** 以指向电子邮件中的 **附件内容**。 这将确保流程从发票附件中提取信息。

11. 选择您之前创建的 **表**。 例如，您可以选择 **发票信息** 表。 从上一个操作中选择动态内容以填充以下字段：

    - ID
    - 数量
    - 日期
    - 姓名
    - 状态 - 将 **状态** 设置为 **待处理**。
    - 供应商电子邮件 - 使用 **新电子邮件到达时** 触发器中的 **发件人** 动态内容。

    ![电源自动添加行](../../images/powerautomate-add-row.png?WT.mc_id=academic-105485-koreyst)

12. 完成流程后，单击 **保存** 按钮保存流程。 然后，您可以通过将带有发票的电子邮件发送到您在触发器中指定的文件夹来测试流程。

> **提升**：你刚刚构建的流程是一个好的开始，现在你需要考虑如何构建一个自动化系统，使我们的财务团队能够向供应商发送电子邮件以更新他们的当前状态 他们的发票。 您的提示：当发票状态发生变化时，流程必须运行。

## 在 Power Automate 中使用文本生成 AI 模型

AI Builder 中的使用 GPT AI 模型创建文本使您能够根据提示生成文本，并由 Microsoft Azure OpenAI Service 提供支持。 借助此功能，您可以将 GPT 技术合并到您的应用程序和流程中，以构建各种自动化流程和富有洞察力的应用程序。

GPT 模型经过大量数据的广泛训练，使它们能够在有提示时生成与人类语言非常相似的文本。 当与工作流程自动化集成时，可以利用 GPT 等人工智能模型来简化和自动化各种任务。

例如，您可以构建流程来自动生成各种用例的文本，如：电子邮件草稿、产品描述等。 您还可以使用该模型为各种应用程序生成文本，如聊天机器人和客户服务应用程序，使客户服务代理能够有效且高效地响应客户查询。

![创建提示](../../images/create-prompt-gpt.png?WT.mc_id=academic-105485-koreyst)

要了解如何在 Power Automate 中使用此 AI 模型，请浏览[使用 AI Builder 和 GPT 添加智能](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko) 模块。

## 继续学习

想要了解有关创建低代码的人工智能应用的更多信息？ 转至[进阶学习的页面](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) 查找有关此主章节的其他学习资源。

前往第十一章，我们将学习[为生成式 AI 添加 function calling](../../../11-integrating-with-function-calling/translations/cn/README.md?WT.mc_id=academic-105485-koreyst)
