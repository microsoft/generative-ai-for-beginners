# 构建低代码AI应用程序

[![构建低代码AI应用程序](../../../translated_images/10-lesson-banner.png?WT.03212fed0693cf8837c727edc800942dbc5ef3a3036a8f7f399c6c08f6f59b92.zh.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson10-gh?WT.mc_id=academic-105485-koreyst)

> _(点击上方图片查看本课视频)_

## 介绍

既然我们已经学习了如何构建图像生成应用程序，那么让我们来谈谈低代码。生成式AI可以用于包括低代码在内的多种领域，但什么是低代码，我们如何将AI添加到其中呢？

通过使用低代码开发平台，构建应用和解决方案变得更加容易，不仅对传统开发者如此，对非开发者也是如此。低代码开发平台让你可以用很少甚至不需要代码来构建应用和解决方案。这是通过提供一个可视化开发环境实现的，该环境允许你拖放组件以构建应用和解决方案。这使你能够更快地构建应用和解决方案，并使用更少的资源。在本课中，我们将深入探讨如何使用低代码，以及如何通过Power Platform使用AI增强低代码开发。

Power Platform为组织提供了一个机会，通过直观的低代码或无代码环境，赋能团队构建他们自己的解决方案。这个环境帮助简化了构建解决方案的过程。使用Power Platform，解决方案可以在几天或几周内构建，而不是几个月或几年。Power Platform由五个关键产品组成：Power Apps、Power Automate、Power BI、Power Pages和Copilot Studio。

本课涵盖：

- Power Platform中的生成式AI简介
- Copilot的介绍及其使用方法
- 使用生成式AI在Power Platform中构建应用和流程
- 使用AI Builder了解Power Platform中的AI模型

## 学习目标

在本课结束时，你将能够：

- 了解Copilot在Power Platform中的工作原理。

- 为我们的教育初创公司构建一个学生作业跟踪应用。

- 构建一个使用AI从发票中提取信息的发票处理流程。

- 在使用Create Text with GPT AI Model时应用最佳实践。

在本课中你将使用的工具和技术有：

- **Power Apps**，用于学生作业跟踪应用，它提供了一个低代码开发环境，用于构建应用以跟踪、管理和与数据交互。

- **Dataverse**，用于存储学生作业跟踪应用的数据，Dataverse将提供一个低代码数据平台来存储应用的数据。

- **Power Automate**，用于发票处理流程，你将有一个低代码开发环境，用于构建工作流以自动化发票处理过程。

- **AI Builder**，用于发票处理AI模型，你将使用预构建的AI模型来处理我们初创公司的发票。

## Power Platform中的生成式AI

增强低代码开发和应用程序与生成式AI是Power Platform的一个关键关注领域。目标是让每个人都能够构建AI驱动的应用、网站、仪表板，并通过AI自动化流程，_而不需要任何数据科学专业知识_。通过在Power Platform的低代码开发体验中集成生成式AI，以Copilot和AI Builder的形式实现这一目标。

### 这是如何工作的？

Copilot是一个AI助手，它允许你通过使用自然语言描述你的需求的一系列对话步骤来构建Power Platform解决方案。例如，你可以指示你的AI助手说明你的应用将使用哪些字段，它将创建应用和底层数据模型，或者你可以指定如何在Power Automate中设置一个流程。

你可以在你的应用屏幕中使用Copilot驱动的功能，以便用户通过对话交互发现见解。

AI Builder是Power Platform中的一种低代码AI功能，它允许你使用AI模型来帮助自动化流程和预测结果。使用AI Builder，你可以将AI引入到连接到Dataverse或各种云数据源（如SharePoint、OneDrive或Azure）的应用和流程中。

Copilot在所有Power Platform产品中可用：Power Apps、Power Automate、Power BI、Power Pages和Power Virtual Agents。AI Builder在Power Apps和Power Automate中可用。在本课中，我们将重点介绍如何在Power Apps和Power Automate中使用Copilot和AI Builder为我们的教育初创公司构建解决方案。

### Power Apps中的Copilot

作为Power Platform的一部分，Power Apps提供了一个低代码开发环境，用于构建应用以跟踪、管理和与数据交互。它是一个应用开发服务套件，具有可扩展的数据平台，并能够连接到云服务和本地数据。Power Apps允许你构建可以在浏览器、平板电脑和手机上运行的应用，并可以与同事共享。Power Apps通过简单的界面让用户轻松进入应用开发，因此每个业务用户或专业开发人员都可以构建自定义应用。通过Copilot，生成式AI进一步增强了应用开发体验。

Power Apps中的Copilot AI助手功能允许你描述你需要的应用类型以及你希望应用跟踪、收集或显示的信息。Copilot根据你的描述生成一个响应式Canvas应用。然后，你可以根据需要自定义应用。AI Copilot还会生成并建议一个Dataverse表，包含你需要存储的数据字段和一些示例数据。在本课后面，我们将了解Dataverse是什么以及如何在Power Apps中使用它。然后，你可以通过对话步骤使用AI Copilot助手功能自定义表。这个功能可以从Power Apps主屏幕上轻松获得。

### Power Automate中的Copilot

作为Power Platform的一部分，Power Automate让用户可以在应用程序和服务之间创建自动化工作流。它帮助自动化重复的业务流程，如通信、数据收集和决策审批。其简单的界面允许每个技术能力水平的用户（从初学者到经验丰富的开发人员）自动化工作任务。通过Copilot，生成式AI进一步增强了工作流开发体验。

Power Automate中的Copilot AI助手功能允许你描述你需要的流程类型以及希望流程执行的操作。Copilot根据你的描述生成一个流程。然后，你可以根据需要自定义流程。AI Copilot还会生成并建议你需要执行的任务的操作。在本课后面，我们将了解什么是流程以及如何在Power Automate中使用它们。然后，你可以通过对话步骤使用AI Copilot助手功能自定义操作。这个功能可以从Power Automate主屏幕上轻松获得。

## 任务：使用Copilot管理我们的初创公司的学生作业和发票

我们的初创公司为学生提供在线课程。公司发展迅速，现在难以应对课程需求。公司聘请你作为Power Platform开发人员，帮助他们构建一个低代码解决方案，以帮助他们管理学生作业和发票。他们的解决方案应该能够通过一个应用程序帮助他们跟踪和管理学生作业，并通过一个工作流自动化发票处理过程。你被要求使用生成式AI开发该解决方案。

当你开始使用Copilot时，你可以使用[Power Platform Copilot Prompt Library](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko)来开始使用提示。这个库包含一系列提示，你可以使用这些提示与Copilot一起构建应用和流程。你也可以使用库中的提示来了解如何向Copilot描述你的需求。

### 为我们的初创公司构建一个学生作业跟踪应用

我们的初创公司的教育工作者一直在努力跟踪学生作业。他们一直在使用电子表格来跟踪作业，但随着学生人数的增加，这变得难以管理。他们要求你构建一个应用程序，以帮助他们跟踪和管理学生作业。该应用应允许他们添加新作业、查看作业、更新作业和删除作业。应用还应允许教育工作者和学生查看已评分和未评分的作业。

你将按照以下步骤使用Power Apps中的Copilot构建该应用：

1. 导航到[Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst)主屏幕。

2. 使用主屏幕上的文本区域描述你想要构建的应用。例如，**_我想构建一个用于跟踪和管理学生作业的应用_**。点击**发送**按钮，将提示发送给AI Copilot。

![描述你想构建的应用](../../../translated_images/copilot-chat-prompt-powerapps.png?WT.30e5da1eee18fc179cbbe27b088aaa20d89624eaaed11a7750372ee8feb61af6.zh.mc_id=academic-105485-koreyst)

3. AI Copilot将建议一个包含你需要存储的数据字段和一些示例数据的Dataverse表。然后，你可以通过对话步骤使用AI Copilot助手功能自定义表。

   > **重要**: Dataverse是Power Platform的底层数据平台。它是一个低代码数据平台，用于存储应用的数据。它是一个完全托管的服务，安全地在Microsoft Cloud中存储数据，并在你的Power Platform环境中进行配置。它带有内置的数据治理功能，如数据分类、数据沿袭、细粒度访问控制等。你可以在[这里](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko)了解更多关于Dataverse的信息。

   ![新表中的建议字段](../../../translated_images/copilot-dataverse-table-powerapps.png?WT.d0158f12f6f02fdf31b4a056b0efbf5a64f49a2c2b6b9ea09b0f3a17d1189579.zh.mc_id=academic-105485-koreyst)

4. 教育工作者希望向已提交作业的学生发送电子邮件，以便随时更新他们的作业进度。你可以使用Copilot向表中添加一个新字段来存储学生的电子邮件。例如，你可以使用以下提示向表中添加一个新字段：**_我想添加一列来存储学生电子邮件_**。点击**发送**按钮，将提示发送给AI Copilot。

![添加新字段](../../../translated_images/copilot-new-column.png?WT.18e16fce13f73236f484dc1b59e3d8e83a80c1cdf40854077a3dc800df76c560.zh.mc_id=academic-105485-koreyst)

5. AI Copilot将生成一个新字段，然后你可以根据需要自定义该字段。

6. 完成表后，点击**创建应用**按钮创建应用。

7. AI Copilot将根据你的描述生成一个响应式Canvas应用。然后，你可以根据需要自定义应用。

8. 为了让教育工作者能够向学生发送电子邮件，你可以使用Copilot向应用添加一个新屏幕。例如，你可以使用以下提示向应用添加一个新屏幕：**_我想添加一个屏幕来向学生发送电子邮件_**。点击**发送**按钮，将提示发送给AI Copilot。

![通过提示指令添加新屏幕](../../../translated_images/copilot-new-screen.png?WT.afdf65429e4ef7b2eb58038fe91de6a3ebe7ca1d85e89c584efcb6da12abfdeb.zh.mc_id=academic-105485-koreyst)

9. AI Copilot将生成一个新屏幕，然后你可以根据需要自定义屏幕。

10. 完成应用后，点击**保存**按钮保存应用。

11. 要与教育工作者共享应用，点击**共享**按钮，然后再次点击**共享**按钮。你可以通过输入他们的电子邮件地址与教育工作者共享应用。

> **你的作业**：你刚刚构建的应用是一个良好的开始，但可以改进。通过电子邮件功能，教育工作者只能手动输入学生的电子邮件来发送邮件。你能否使用Copilot构建一个自动化功能，使教育工作者在学生提交作业时自动向他们发送电子邮件？提示：使用正确的提示，你可以在Power Automate中使用Copilot来构建这个功能。

### 为我们的初创公司构建发票信息表

我们的初创公司的财务团队一直在努力跟踪发票。他们一直在使用电子表格来跟踪发票，但随着发票数量的增加，这变得难以管理。他们要求你构建一个表，以帮助他们存储、跟踪和管理收到的发票信息。该表应用于构建一个自动化功能，提取所有发票信息并将其存储在表中。该表还应允许财务团队查看已支付和未支付的发票。

Power Platform有一个底层数据平台，称为Dataverse，它允许你存储应用和解决方案的数据。Dataverse提供了一个低代码数据平台，用于存储应用的数据。它是一个完全托管的服务，安全地在Microsoft Cloud中存储数据，并在你的Power Platform环境中进行配置。它带有内置的数据治理功能，如数据分类、数据沿袭、细粒度访问控制等。你可以在[这里](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko)了解更多关于Dataverse的信息。

为什么我们应该为我们的初创公司使用Dataverse？Dataverse中的标准和自定义表为你的数据提供了一个安全的云存储选项。表允许你存储不同类型的数据，类似于你在单个Excel工作簿中使用多个工作表的方式。你可以使用表来存储特定于你的组织或业务需求的数据。我们的初创公司使用Dataverse将获得的一些好处包括但不限于：

- **易于管理**：元数据和数据都存储在云中，因此你不必担心它们的存储或管理细节。你可以专注于构建应用和解决方案。

- **安全**：Dataverse为你的数据提供了一个安全的云存储选项。你可以使用基于角色的安全性控制谁可以访问表中的数据以及他们如何访问这些数据。

- **丰富的元数据**：数据类型和关系直接在Power Apps中使用。

- **逻辑和验证**：你可以使用业务规则、计算字段和验证规则来实施业务逻辑和保持数据准确性。

现在你已经了解了什么是Dataverse以及为什么应该使用它，让我们来看看如何使用Copilot在Dataverse中创建一个表，以满足我们的财务团队的要求。

> **注意**：你将在下一节中使用此表构建一个自动化功能，以提取所有发票信息并将其存储在表中。要使用Copilot在Dataverse中创建一个表，请按照以下步骤操作： 1. 导航到[Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst)主屏幕。 2. 在左侧导航栏上，选择**表**，然后点击**描述新表**。 ![选择新表](../../../translated_images/describe-new-table.png?WT.1934e0de36f3fb613a023df3dcca89ba55f5d8d118e59b997d3f58e346f9e5db.zh.mc_id=academic-105485-koreyst) 1. 在**描述新表**屏幕上，使用文本区域描述你想要创建的表。例如，**_我想创建一个用于存储发票信息的表_**。点击**发送**按钮，将提示发送给AI Copilot。 ![描述表](../../../translated_images/copilot-chat-prompt-dataverse.png?WT.07979e2dd2a5c59cdd535f61e0dc2e0ce9d964189f70230e2a39ebb574a877cd.zh.mc_id=academic-105485-koreyst) 1. AI Copilot将建议一个包含你需要存储的数据字段和一些示例数据的Dataverse表。然后，你可以通过对话步骤使用AI Copilot助手功能自定义表。 ![建议的Dataverse表](../../../translated_images/copilot-dataverse-table.png?WT.45e9dc11cec7f53431fef3c849a45a5a0e52bdd3d621de57ff591f9af23aae38.zh.mc_id=academic-105485-koreyst) 1. 财务团队希望向供应商发送电子邮件，以更新他们的发票当前状态。你可以使用Copilot向表中添加一个新字段来存储供应商的电子邮件。例如，你可以使用以下提示向表中添加一个新字段：**_我想添加一列来存储供应商电子邮件_**。点击**发送**按钮，将提示发送给AI Copilot。 1. AI Copilot将生成一个新字段，然后你可以根据需要自定义该字段。 1. 完成表后，点击**创建**按钮创建表。 ## Power Platform中的AI模型与AI Builder AI Builder是Power Platform中的一种低代码AI功能，它允许你使用AI模型来帮助自动化流程和预测结果。使用AI Builder，你可以将AI引入到连接到Dataverse或各种云数据源（如SharePoint、OneDrive或Azure）的应用和流程中。 ## 预构建AI模型与自定义AI模型 AI Builder提供两种类型的AI模型：预构建AI模型和自定义AI模型。预构建AI模型是由Microsoft训练并在Power Platform中可用的现成AI模型。这些模型帮助你为应用和流程添加智能，而无需收集数据然后构建、训练和发布你自己的模型。你可以使用这些模型来自动化流程和预测结果。Power Platform中可用的一些预构建AI模型包括： - **关键短语提取**：此模型从文本中提取关键短语。 - **语言检测**：此模型检测语言。
## 文本分析

- **情感分析**：该模型检测文本中的积极、消极、中立或混合情感。
- **名片读取器**：该模型从名片中提取信息。
- **文本识别**：该模型从图像中提取文本。
- **对象检测**：该模型检测并提取图像中的对象。
- **文档处理**：该模型从表单中提取信息。
- **发票处理**：该模型从发票中提取信息。

通过自定义 AI 模型，您可以将自己的模型引入 AI Builder，使其像任何 AI Builder 自定义模型一样工作，允许您使用自己的数据训练模型。您可以使用这些模型在 Power Apps 和 Power Automate 中自动化流程和预测结果。使用您自己的模型时会有一些限制。阅读更多关于这些[限制](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst)的信息。

![AI builder models](../../../translated_images/ai-builder-models.png?WT.6c2f6abc64cc07d27103364f2cd8c4689956e168da9f58cf75e6ca3fb459ec20.zh.mc_id=academic-105485-koreyst)

## 任务 #2 - 为我们的初创公司构建发票处理流程

财务团队一直在努力处理发票。他们一直使用电子表格来跟踪发票，但随着发票数量的增加，这变得难以管理。他们要求您构建一个工作流，帮助他们使用 AI 处理发票。该工作流应使他们能够从发票中提取信息并将信息存储在 Dataverse 表中。工作流还应使他们能够通过电子邮件将提取的信息发送给财务团队。

现在您知道了 AI Builder 是什么以及为什么要使用它，让我们来看看如何使用之前介绍过的 AI Builder 中的发票处理 AI 模型来构建一个帮助财务团队处理发票的工作流。

要使用 AI Builder 中的发票处理 AI 模型构建一个帮助财务团队处理发票的工作流，请按照以下步骤操作：

1. 进入 [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst) 主屏幕。
2. 使用主屏幕上的文本区域描述您要构建的工作流。例如，**_当发票到达我的邮箱时处理发票_**。点击 **发送** 按钮将提示发送给 AI Copilot。
   ![Copilot power automate](../../../translated_images/copilot-chat-prompt-powerautomate.png?WT.f6341b68d42f7c600e636c97f6874ec548ea3575906434e5caa9b7fbabd1c284.zh.mc_id=academic-105485-koreyst)
3. AI Copilot 将建议您执行任务所需的操作。您可以点击 **下一步** 按钮继续下一步。
4. 在下一步中，Power Automate 将提示您设置流所需的连接。完成后，点击 **创建流** 按钮创建流。
5. AI Copilot 将生成一个流，然后您可以自定义流以满足您的需求。
6. 更新流的触发器，并将 **文件夹** 设置为存储发票的文件夹。例如，您可以将文件夹设置为 **收件箱**。点击 **显示高级选项**，将 **仅限附件** 设置为 **是**。这将确保流仅在收到带附件的电子邮件时运行。
7. 从流中删除以下操作：**HTML to text**、**Compose**、**Compose 2**、**Compose 3** 和 **Compose 4**，因为您不会使用它们。
8. 从流中删除 **Condition** 操作，因为您不会使用它。它应该看起来像以下截图：
   ![power automate, remove actions](../../../translated_images/powerautomate-remove-actions.png?WT.b7f06c5f7f24ed173de29f405e580c0bb414655560859cdbdf97b8c1803fe4c7.zh.mc_id=academic-105485-koreyst)
9. 点击 **添加操作** 按钮并搜索 **Dataverse**。选择 **添加新行** 操作。
10. 在 **从发票中提取信息** 操作中，将 **发票文件** 更新为指向电子邮件中的 **附件内容**。这将确保流从发票附件中提取信息。
11. 选择您之前创建的 **表**。例如，您可以选择 **发票信息** 表。从先前的操作中选择动态内容以填充以下字段：
    - ID
    - 金额
    - 日期
    - 名称
    - 状态
    - 将 **状态** 设置为 **待处理**。
    - 供应商电子邮件
    - 使用 **来自** 动态内容从 **当新邮件到达时** 触发器。
    ![power automate add row](../../../translated_images/powerautomate-add-row.png?WT.05f8f2c79ce95248eb173d6644436a1220f143991a5f0e647e15b922a0e1a290.zh.mc_id=academic-105485-koreyst)
12. 完成流后，点击 **保存** 按钮保存流。然后您可以通过向您在触发器中指定的文件夹发送带有发票的电子邮件来测试流。

> **你的作业**：您刚刚构建的流是一个很好的开始，现在您需要考虑如何构建一个自动化流程，使我们的财务团队能够向供应商发送电子邮件，更新他们当前的发票状态。提示：当发票状态发生变化时，流必须运行。

## 在 Power Automate 中使用文本生成 AI 模型

AI Builder 中的 GPT AI 模型创建文本功能使您能够基于提示生成文本，并由 Microsoft Azure OpenAI 服务提供支持。借助这一功能，您可以将 GPT（生成式预训练变换器）技术集成到您的应用和流程中，以构建各种自动化流程和有见地的应用程序。

GPT 模型经过海量数据的广泛训练，能够在给出提示时生成类似人类语言的文本。与工作流自动化集成时，像 GPT 这样的 AI 模型可以被利用来简化和自动化广泛的任务。

例如，您可以构建流程以自动生成各种用例的文本，如：电子邮件草稿、产品描述等。您还可以使用该模型为各种应用生成文本，例如聊天机器人和客户服务应用，使客户服务代理能够有效和高效地响应客户查询。

![create a prompt](../../../translated_images/create-prompt-gpt.png?WT.7838e7bf32dee9636286569283c29f2a7cd58f2e2e093cee611dfa66db61a6ca.zh.mc_id=academic-105485-koreyst)

要了解如何在 Power Automate 中使用此 AI 模型，请查看 [Add intelligence with AI Builder and GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko) 模块。

## 做得好！继续学习

完成本课程后，查看我们的 [生成式 AI 学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，继续提升您的生成式 AI 知识！

前往第 11 课，我们将看看如何[将生成式 AI 与功能调用集成](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)！

**免责声明**：  
本文档是使用基于机器的人工智能翻译服务翻译的。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原文档的母语版本视为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用本翻译而引起的任何误解或误读，我们不承担责任。