# Building Low Code AI Applications

[![Building Low Code AI Applications](../../../translated_images/pcm/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(Click di image for up so you fit watch video of dis lesson)_

## Introduction

Now we don learn how to build app wey fit generate image, make we yarn about low code. Generative AI fit use for plenty different tin dem, e include low code, but wetin be low code and how we fit add AI inside am?

Building apps and solution don easy for traditional developers and non-developers through how dem dey use Low Code Development Platforms. Low Code Development Platforms dey make you fit build apps and solution wit small code or no code at all. Dem do dis by giving you visual development environment wey make you drag and drop components take build apps and solutions. Dis one go help make building apps and solutions quick and e no go need plenty resource. For dis lesson, we go dive deep on how to use Low Code and how to take improve low code development with AI by using Power Platform.

Power Platform dey give organizations chance to make their teams build their own solutions through an easy low-code or no-code environment. Dis environment dey help make the process to build solutions simple. Wit Power Platform, solution fit ready for days or weeks instead of months or years. Power Platform get five main products: Power Apps, Power Automate, Power BI, Power Pages and Copilot Studio.

Dis lesson go cover:

- Introduction to Generative AI for Power Platform
- Introduction to Copilot and how to use am
- How to use Generative AI to build apps and flows for Power Platform
- Understand AI Models for Power Platform wit AI Builder
- Build intelligent agents with Microsoft Copilot Studio

## Learning Goals

By the end of dis lesson, you go fit:

- Understand how Copilot dey work for Power Platform.

- Build Student Assignment Tracker App for our education startup.

- Build Invoice Processing Flow wey go use AI take extract information from invoices.

- Use best practices when you dey use Create Text with GPT AI Model.

- Understand wetin Microsoft Copilot Studio be and how to build intelligent agents with am.

The tools and technologies wey you go use for dis lesson na:

- **Power Apps**, for Student Assignment Tracker app, wey dey provide low-code development environment for building apps to track, manage and interact with data.

- **Dataverse**, for store data for Student Assignment Tracker app where Dataverse go provide low-code data platform to hold the app data.

- **Power Automate**, for Invoice Processing flow wey go be low-code development environment for building workflow to automate Invoice Processing process.

- **AI Builder**, for Invoice Processing AI Model where you go use prebuilt AI Models to handle invoices for our startup.

## Generative AI for Power Platform

To improve low-code development and application with generative AI na big focus for Power Platform. Di goal na to make everybody fit build AI-powered apps, sites, dashboards and automate processes with AI, _without to need any data science expertise_. Dis goal dey happen by putting generative AI inside low-code development experience for Power Platform as Copilot and AI Builder.

### How dis one dey work?

Copilot na AI assistant wey make you fit build Power Platform solution by describing wetin you want for a series of conversational steps using natural language. For example, you fit tell your AI assistant to talk wetin fields your app go use and e go create both the app and the underlying data model or you fit tell how make flow for Power Automate.

You fit use Copilot functionalities as feature for your app screens to allow users uncover insights through conversational interactions.

AI Builder na low-code AI tool for Power Platform wey make you fit use AI Models to help automate processes and predict results. Wit AI Builder you fit add AI to your apps and flows wey connect to your data for Dataverse or for plenty cloud data sources like SharePoint, OneDrive or Azure.

Copilot dey available for all Power Platform products: Power Apps, Power Automate, Power BI, Power Pages and Copilot Studio (wey dem use to call Power Virtual Agents). AI Builder dey available for Power Apps and Power Automate. For dis lesson, we go focus on how to use Copilot and AI Builder for Power Apps and Power Automate to build solution for our education startup.

### Copilot for Power Apps

As part of Power Platform, Power Apps dey provide low-code development environment to build apps to track, manage and interact with data. E be suite of app development services with a scalable data platform and e fit connect to cloud services and on-premises data. Power Apps make you fit build apps wey fit run for browsers, tablets, and phones, and fit share dem with co-workers. Power Apps dey make app development easy with simple interface, so every business user or pro developer fit build custom apps. App development experience also improve with Generative AI through Copilot.

The copilot AI assistant feature for Power Apps make you fit talk wetin kind app you want and wetin information you want your app to track, collect, or show. Copilot go then generate responsive Canvas app base on your talk. You fit customize the app to fit your needs. AI Copilot also go generate and suggest Dataverse Table with the fields wey you need to store data you want track and some sample data. We go look wetin Dataverse be and how you fit use am inside Power Apps for dis lesson later. You fit customize the table to fit your needs using AI Copilot assistant feature through conversational steps. Dis feature dey ready for Power Apps home screen.

### Copilot for Power Automate

As part of Power Platform, Power Automate let users create automated workflow between applications and services. E help make repetitive business processes like communication, data collection, and decision approvals automatic. E get simple interface wey allow users of different technical skills (from beginners to seasoned developers) to automate work tasks. Workflow development experience also improve with Generative AI through Copilot.

The copilot AI assistant feature for Power Automate make you fit describe wetin kind flow you want and wetin actions you want your flow to perform. Copilot go then generate flow based on your talk. You fit customize the flow to fit your needs. AI Copilot also go suggest actions wey you go need take perform the task you wan automate. We go see wetin flows be and how you fit use dem for Power Automate later for dis lesson. You fit customize actions to fit your need using AI Copilot assistant feature through conversational steps. Dis feature dey ready for Power Automate home screen.

## Building Intelligent Agents with Microsoft Copilot Studio

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst) (wey dem use to call Power Virtual Agents) na low-code part of Power Platform for building **AI agents** — conversational copilots wey fit answer questions, do actions, and automate tasks for your users. Just like the rest of Power Platform, you build these agents for visual, natural-language-first way: you describe wetin you want the agent to do, and Copilot Studio go help plan e instructions, knowledge, and actions.

For our education startup, you fit build agent wey dey answer student questions about courses, check assignment deadlines, and even send email to instructor — all dis without you write any code.

Here na some of latest capabilities wey make Copilot Studio powerful:

- **Generative answers from your knowledge**. Instead of hand write every conversation, you fit connect **knowledge sources** — public websites, SharePoint, OneDrive, Dataverse, uploaded files, or enterprise data through connectors — and the agent go generate grounded answers from them.

- **Generative orchestration**. Instead of rely on fixed trigger phrases, the agent go use AI to understand request and decide dynamically which knowledge, topics, and actions to join to complete am, including link several steps together.

- **Actions and connectors**. Agents fit *do* things, no be only chat. You fit give agent actions supported by 1,500+ prebuilt Power Platform connectors, Power Automate flows, custom REST APIs, prompts, or **Model Context Protocol (MCP)** servers.

- **Autonomous agents**. Agents no limited to respond only for chat window. You fit build **autonomous agents** wey fit trigger by events — like new email, new record for Dataverse, or file wey dem upload — then dem go act for background to finish task.

- **Multi-agent orchestration**. Agents fit call other agents. One Copilot Studio agent fit hand over to or extend by other agents, including agents wey dem publish to Microsoft 365 Copilot and agents wey dem build for Microsoft Foundry.

- **Model choice**. Apart from built-in models, you fit bring models from Microsoft Foundry model catalog to adjust how your agent go reason and respond.

- **Publish anywhere**. Once you don build am, agent fit publish to plenty channels — Microsoft Teams, Microsoft 365 Copilot, website or custom app, and more — with security, authentication, and analytics managed through Power Platform admin experience.

You fit start to build your first agent for [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst) and learn more for [Microsoft Copilot Studio documentation](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst).

## Assignment: Manage student assignments and invoices for our startup, using Copilot

Our startup dey provide online courses to students. The startup don grow quick and now e dey struggle to meet demand for the courses. The startup don hire you as Power Platform developer to help dem build low code solution to help manage their student assignments and invoices. Their solution suppose fit help track and manage student assignments through app and automate invoice processing process through workflow. You don request to use Generative AI to develop the solution.

When you want start to use Copilot, you fit use [Power Platform Copilot Prompt Library](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) to start with prompts. Dis library get list of prompts wey you fit use to build apps and flows with Copilot. You fit also use the prompts inside the library to get idea of how to describe your requirements to Copilot.

### Build Student Assignment Tracker App for Our Startup

Our educators for the startup don dey struggle to keep track of student assignments. Them dey use spreadsheet to track assignments but e don hard to manage as number of students don increase. Them don ask you to build app wey go help dem track and manage student assignments. Di app suppose make dem fit add new assignments, view assignments, update assignments and delete assignments. Di app suppose also allow educators and students view assignments wey dem don grade and the ones wey dem no don grade.

You go build the app using Copilot for Power Apps follow these steps below:

1. Go to [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) home screen.

1. Use di text area for di home screen take describe the app wey you want build. Example, **_I want build app to track and manage student assignments_**. Click on di **Send** button to send prompt to AI Copilot.

![Describe the app you want to build](../../../translated_images/pcm/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. AI Copilot go suggest Dataverse Table with fields wey you need to store data wey you wan track and sample data. You fit customize the table to fit your needs using AI Copilot assistant feature through conversational steps.

   > **Important**: Dataverse na the underlying data platform for Power Platform. E be low-code data platform for store app data. E be fully managed service wey dey secure data for Microsoft Cloud and e dey provision inside your Power Platform environment. E get built-in data governance features like data classification, data lineage, fine-grained access control and more. You fit learn more about Dataverse [here](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Suggested fields in your new table](../../../translated_images/pcm/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. Educators want send emails to students wey don submit their assignments to keep dem updated on progress. You fit use Copilot to add new field to table to store student email. Example, fit use this prompt: **_I want to add a column to store student email_**. Click on di **Send** button to send prompt to AI Copilot.

![Adding a new field](../../../translated_images/pcm/copilot-new-column.35e15ff21acaf274.webp)

1. AI Copilot go generate new field and you fit customize the field to fit your needs.


1. Once you don finish wit the table, click di **Create app** button to create di app.

1. Di AI Copilot go generate correct Canvas app wey go responsive based on wetin you talk. You fit then customize di app make e fit your needs.

1. For teachers wey want send email go students, you fit use Copilot add new screen go inside di app. For example, you fit use dis prompt to add new screen for di app: **_I want to add a screen to send emails to students_**. Click di **Send** button to send di prompt go AI Copilot.

![Adding a new screen via a prompt instruction](../../../translated_images/pcm/copilot-new-screen.2e0bef7132a17392.webp)

1. Di AI Copilot go generate new screen and you fit then customize di screen make e fit your needs.

1. Once you don finish wit di app, click di **Save** button to save di app.

1. To share di app wit di teachers, click di **Share** button then click di **Share** button again. You fit then share di app wit di teachers by putting their email addresses.

> **Your homework**: Di app wey you build just now good start but e fit better. Wit di email feature, teachers fit only manually send email go students by typing their email addresses. You fit use Copilot build automation wey go make teachers fit send email go students automatically when dem submit their assignments? Hint na say wit correct prompt you fit use Copilot for Power Automate build dis.

### Build Invoice Information Table for Our Startup

Our startup finance team don dey find am hard to track invoices. Dem dey use spreadsheet track invoices but as invoices plenty, e don hard to manage. Dem request you build table wey fit help dem store, track, and manage info about invoices. The table go also fit build automation wey go extract all invoice info store am for di table. The table go still allow finance team see invoices wey dem don pay and ones wey dem never pay.

Power Platform get data platform wey dem dey call Dataverse wey fit help you store data for your apps and solutions. Dataverse na low-code data platform to store app data. E be fully managed service wey dey secure data for Microsoft Cloud and e dey inside your Power Platform environment. E come wit things like data governance, data classification, data lineage, fine-grained access control plus plus. You fit learn more [about Dataverse here](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Why we suppose use Dataverse for our startup? Standard and custom tables inside Dataverse dey give you secure and cloud-based storage for your data. Tables fit store different kain data, like how you fit use many worksheet for one Excel workbook. You fit store data specific to your company or business needs. Some benefits wey our startup go get from Dataverse include:

- **Easy to manage**: Both metadata and data dey stored for cloud, so you no need worry how dem store am or manage am. You fit focus on building your apps and solutions.

- **Secure**: Dataverse dey give secure cloud storage for your data. You fit control who fit see di data for your tables and how by using role-based security.

- **Rich metadata**: Data types and relationships fit dey used directly for Power Apps

- **Logic and validation**: You fit use business rules, calculated fields, and validation rules to force business logic and keep data correct.

Now you sabi wetin Dataverse be and why you suppose use am, make we see how you fit use Copilot create table inside Dataverse wey go meet finance team needs.

> **Note** : You go use this table for next section to build automation wey go extract all invoice information and store am for table.

To create table for Dataverse with Copilot, follow dis steps:

1. Go to [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) home screen.

2. For left side navigation bar, select **Tables** then click **Describe the new Table**.

![Select new table](../../../translated_images/pcm/describe-new-table.0792373eb757281e.webp)

1. For **Describe the new Table** screen, use text area to describe di table you want create. For example, **_I want to create a table to store invoice information_**. Click di **Send** button to send prompt to AI Copilot.

![Describe the table](../../../translated_images/pcm/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. AI Copilot go suggest Dataverse Table wey get di fields you need to store data you want track plus sample data. You fit customize di table to fit your needs using AI Copilot assistant feature for conversation steps.

![Suggested Dataverse table](../../../translated_images/pcm/copilot-dataverse-table.b3bc936091324d9d.webp)

1. Finance team wan send email go supplier to update dem about current status of their invoice. You fit use Copilot add new field to table to store supplier email. For example, use dis prompt to add new field: **_I want to add a column to store supplier email_**. Click di **Send** button send prompt go AI Copilot.

1. AI Copilot go create new field and you fit customize di field make e fit your needs.

1. Once you finish wit di table, click di **Create** button to create di table.

## AI Models inside Power Platform wit AI Builder

AI Builder na low-code AI wey dey inside Power Platform wey fit help you use AI Models to automate things and predict tins. Wit AI Builder you fit bring AI enter your apps and flows wey connect to your data for Dataverse or other cloud data like SharePoint, OneDrive or Azure.

## Prebuilt AI Models vs Custom AI Models

AI Builder get two kain AI Models: Prebuilt AI Models and Custom AI Models. Prebuilt AI Models na AI models wey Microsoft don train and ready to use inside Power Platform. Dem go help you add intelligence to your apps and flows without you to gather data, build, train or publish your own models. You fit use dem automate things and predict tins.

Some Prebuilt AI Models wey dey inside Power Platform be:

- **Key Phrase Extraction**: Dis one dey extract key phrases from text.
- **Language Detection**: Dis one dey detect di language of text.
- **Sentiment Analysis**: Dis one dey find if text positive, negative, neutral, or mixed feelings.
- **Business Card Reader**: Dis one dey extract info from business cards.
- **Text Recognition**: Dis one dey extract text from images.
- **Object Detection**: Dis one dey detect and extract objects for images.
- **Document processing**: Dis one dey extract info from forms.
- **Invoice Processing**: Dis one dey extract info from invoices.

Wit Custom AI Models, you fit bring your own model into AI Builder so e fit work like any AI Builder custom model, and you fit train am wit your own data. You fit use dem automate and predict tins for Power Apps and Power Automate. But when you dey use your own model, some rules go apply. Read more on these [limitations](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

![AI builder models](../../../translated_images/pcm/ai-builder-models.8069423b84cfc47f.webp)

## Assignment #2 - Build Invoice Processing Flow for Our Startup

Finance team dey find am hard to process invoices. Dem dey use spreadsheet track invoices but e don hard as invoice plenty. Dem ask you build workflow to help dem process invoices using AI. Workflow go make dem fit extract info from invoices and store info inside Dataverse table. E go also make dem send email to finance team wit di extracted info.

Now wey you sabi AI Builder and why you suppose use am, make we see how you fit use Invoice Processing AI Model in AI Builder, wey we talk before, to build workflow to help finance team process invoices.

To build workflow to help finance team process invoices with Invoice Processing AI Model in AI Builder, follow di steps:

1. Go to [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst) home screen.

2. Use text area for home screen to describe workflow you want build. For example, **_Process an invoice when it arrives in my mailbox_**. Click di **Send** button to send prompt go AI Copilot.

   ![Copilot power automate](../../../translated_images/pcm/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. AI Copilot go suggest actions wey you need do di task you wan automate. You fit click **Next** button to enter next steps.

4. For next step, Power Automate go ask you set up connections wey flow need. When you don finish, click **Create flow** button to create flow.

5. AI Copilot go generate flow and you fit customize am make e fit your needs.

6. Update flow trigger and set **Folder** to folder wey invoices go dey. For example, set am to **Inbox**. Click **Show advanced options** and set **Only with Attachments** to **Yes**. Dis one go make sure flow run only when email with attachment enter folder.

7. Remove these actions from flow: **HTML to text**, **Compose**, **Compose 2**, **Compose 3** and **Compose 4** because you no go use dem.

8. Remove **Condition** action from flow because you no go use am. E suppose look like dis screenshot:

   ![power automate, remove actions](../../../translated_images/pcm/powerautomate-remove-actions.7216392fe684ceba.webp)

9. Click di **Add an action** button then search **Dataverse**. Select **Add a new row** action.

10. For **Extract Information from invoices** action, update **Invoice File** to point to **Attachment Content** from email. Dis one go make flow extract info from invoice attachment.

11. Select di **Table** wey you create before. For example, select **Invoice Information** table. Choose dynamic content from previous action to fill these fields:

    - ID
    - Amount
    - Date
    - Name
    - Status - Set **Status** to **Pending**.
    - Supplier Email - Use **From** dynamic content from **When a new email arrives** trigger.

    ![power automate add row](../../../translated_images/pcm/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. When you don finish wit flow, click **Save** button to save flow. You fit test flow by sending email wit invoice to folder wey you put for trigger.

> **Your homework**: Di flow wey you build just now na good start, now you need think how you fit build automation to enable finance team send email to supplier to update dem about current status of their invoice. Hint: flow must run when invoice status change.

## Use Text Generation AI Model inside Power Automate

Create Text with GPT AI Model inside AI Builder fit generate text based on prompt, e dey powered by Microsoft Azure OpenAI Service. With dis, you fit add GPT (Generative Pre-Trained Transformer) technology inside your apps and flows to build many automated flows and smart applications.

GPT models dey go through plenty training on big data, so dem fit produce text wey dey like human language when you give dem prompt. When you combine am with workflow automation, AI models like GPT fit help you streamline and automate many tasks.

For example, you fit build flows to auto generate text for tins like: drafts of emails, product descriptions, and more. You fit also use dis model generate text for apps like chatbots and customer service apps wey help service agents respond well and quick to customer questions.

![create a prompt](../../../translated_images/pcm/create-prompt-gpt.69d429300c2e870a.webp)


To sabi how to use dis AI Model for Power Automate, waka through di [Add intelligence with AI Builder and GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko) module.

## Beta Work! Continue Your Learning

After you finish dis lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) make you continue to improve your Generative AI knowledge!

You want to customize and gain more from Copilot? Explore [Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) — na community wey join hand collect instructions, agents, skills, and configurations wey go help you enjoy GitHub Copilot well well.

Comot go Lesson 11 where we go see how to [integrate Generative AI with Function Calling](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->