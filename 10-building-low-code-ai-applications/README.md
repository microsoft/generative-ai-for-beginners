# Building Low Code AI Applications

[![Building Low Code AI Applications](./images/10-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://learn.microsoft.com/_themes/docs.theme/master/en-us/_themes/global/video-embed.html?id=170c6cb7-3c96-40f2-a354-b6f0ec523de7?WT.mc_id=academic-105485-koreyst)

> _(Click the image above to view video of this lesson)_

## Introduction

Now that we've learned how to build image generating applications, let's talk about low code. Generative AI can be used for a variety of different areas including low code, but what is low code and how can we add AI to it?

Building apps and solutions has become more easier for traditional developers and non-developers through the use of Low Code Development Platforms. Low Code Development Platforms enable you to build apps and solutions with little to no code. This is achieved by providing a visual development environment that enables you to drag and drop components to build apps and solutions. This enables you to build apps and solutions faster and with less resources. In this lesson, we dive deep into how to use Low Code and how to enhance low code development with AI using Power Platform.

The Power Platform provides organizations with the opportunity to empower their teams to build their own solutions through an intuitive low-code or no-code environment. This environment helps simplify the process of building solutions. With Power Platform, solutions can be built in days or weeks instead of months or years. Power Platform consists of five key products: Power Apps, Power Automate, Power BI, Power Pages and Copilot Studio.

This lesson covers:

- Introduction to Generative AI in Power Platform
- Introduction to Copilot and how to use it
- Using Generative AI to build apps and flows in Power Platform
- Understanding the AI Models in Power Platform with AI Builder

## Learning Goals

By the end of this lesson, you will be able to:

- Understand how Copilot works in Power Platform.

- Build a Student Assignment Tracker App for our education startup.

- Build an Invoice Processing Flow that uses AI to extract information from invoices.

- Apply best practices when using the Create Text with GPT AI Model.

The tools and technologies that you will use in this lesson are:

- **Power Apps**, for the Student Assignment Tracker app, which provides a low-code development environment for building apps to track, manage and interact with data.

- **Dataverse**, for storing the data for the Student Assignment Tracker app where Dataverse will provide a low-code data platform for storing the app's data.

- **Power Automate**, for the Invoice Processing flow where you will have low-code development environment for building workflows to automate the Invoice Processing process.

- **AI Builder**, for the Invoice Processing AI Model where you will use prebuilt AI Models to process the invoices for our startup.

## Generative AI in Power Platform

Enhancing low-code development and application with generative AI is a key focus area for Power Platform. The goal is to enable everyone to build AI-powered apps, sites, dashboards and automate processes with AI, _without requiring any data science expertise_. This goal is achieved by integrating generative AI into the low-code development experience in Power Platform in the form of Copilot and AI Builder.

### How does this work?

Copilot is an AI assistant that enables you to build Power Platform solutions by describing your requirements in a series of conversational steps using natural language. You can for example instruct your AI assistant to state what fields your app will use and it will create both the app and the underlying data model or you could specify how to set up a flow in Power Automate.

You can use Copilot driven functionalities as a feature in your app screens to enable users to uncover insights through conversational interactions.

AI Builder is a low-code AI capability available in Power Platform that enables you to use AI Models to help you to automate processes and predict outcomes. With AI Builder you can bring AI to your apps and flows that connect to your data in Dataverse or in various cloud data sources, such as SharePoint, OneDrive or Azure.

Copilot is available in all of the Power Platform products: Power Apps, Power Automate, Power BI, Power Pages and Power Virtual Agents. AI Builder is available in Power Apps and Power Automate. In this lesson, we will focus on how to use Copilot and AI Builder in Power Apps and Power Automate to build a solution for our education startup.

### Copilot in Power Apps

As part of the Power Platform, Power Apps provides a low-code development environment for building apps to track, manage and interact with data. It's a suite of app development services with a scalable data platform and the ability to connect to cloud services and on-premises data. Power Apps allows you to build apps that run on browsers, tablets, and phones, and can be shared with co-workers. Power Apps eases users into app development with a simple interface, so that every business user or pro developer can build custom apps. The app development experience is also enhanced with Generative AI through Copilot.

The copilot AI assistant feature in Power Apps enables you to describe what kind of app you need and what information you want your app to track, collect, or show. Copilot then generates a responsive Canvas app based on your description. You can then customize the app to meet your needs. The AI Copilot also generates and suggests a Dataverse Table with the fields you need to store the data you want to track and some sample data. We will look at what Dataverse is and how you can use it in Power Apps in this lesson later. You can then customize the table to meet your needs using the AI Copilot assistant feature through conversational steps. This feature is readily available from the Power Apps home screen.

### Copilot in Power Automate

As part of the Power Platform, Power Automate lets users create automated workflows between applications and services. It helps automate repetitive business processes such as communication, data collection, and decision approvals. Its simple interface allows users with every technical competence (from beginners to seasoned developers) to automate work tasks. The workflow development experience is also enhanced with Generative AI through Copilot.

The copilot AI assistant feature in Power Automate enables you to describe what kind of flow you need and what actions you want your flow to perform. Copilot then generates a flow based on your description. You can then customize the flow to meet your needs. The AI Copilot also generates and suggests the actions you need to perform the task you want to automate. We will look at what flows are and how you can use them in Power Automate in this lesson later. You can then customize the actions to meet your needs using the AI Copilot assistant feature through conversational steps. This feature is readily available from the Power Automate home screen.

## Assignment: manage student assignments and invoices for our startup, using Copilot

Our startup provides online courses to students. The startup has grown rapidly and is now struggling to keep up with the demand for its courses. The startup has hired you as a Power Platform developer to help them build a low code solution to help them manage their student assignments and invoices. Their solution should be able to help them track and manage student assignments through an app and automate the invoice processing process through a workflow. You have been asked to use Generative AI to develop the solution.

When you are getting started with using Copilot, you can use the [Power Platform Copilot Prompt Library](https://pnp.github.io/powerplatform-prompts/?WT.mc_id=academic-109639-somelezediko) to get started with the prompts. This library contains a list of prompts that you can use to build apps and flows with Copilot. You can also use the prompts in the library to get an idea of how to describe your requirements to Copilot.

### Build a Student Assignment Tracker App for Our Startup

The educators at our startup have been struggling to keep track of student assignments. They have been using a spreadsheet to track the assignments but this has become difficult to manage as the number of students has increased. They have asked you to build an app that will help them track and manage student assignments. The app should enable them to add new assignments, view assignments, update assignments and delete assignments. The app should also enable educators and students to view the assignments that have been graded and those that have not been graded.

You will build the app using Copilot in Power Apps following the steps below:

1. Navigate to the [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) home screen.

1. Use the text area on the home screen to describe the app you want to build. For example, **_I want to build an app to track and manage student assignments_**. Click on the **Send** button to send the prompt to the AI Copilot.

![Describe the app you want to build](./images/copilot-chat-prompt-powerapps.png?WT.mc_id=academic-105485-koreyst)

1. The AI Copilot will suggest a Dataverse Table with the fields you need to store the data you want to track and some sample data. You can then customize the table to meet your needs using the AI Copilot assistant feature through conversational steps.

   > **Important**: Dataverse is the underlying data platform for Power Platform. It is a low-code data platform for storing the app's data. It is a fully managed service that securely stores data in the Microsoft Cloud and is provisioned within your Power Platform environment. It comes with built-in data governance capabilities, such as data classification, data lineage, fine-grained access control, and more. You can learn more about Dataverse [here](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Suggested fields in your new table](./images/copilot-dataverse-table-powerapps.png?WT.mc_id=academic-105485-koreyst)

1. Educators want to send emails to the students who have submitted their assignments to keep them updated on the progress of their assignments. You can use Copilot to add a new field to the table to store the student email. For example, you can use the following prompt to add a new field to the table: **_I want to add a column to store student email_**. Click on the **Send** button to send the prompt to the AI Copilot.

![Adding a new field](./images/copilot-new-column.png?WT.mc_id=academic-105485-koreyst)

1. The AI Copilot will generate a new field and you can then customize the field to meet your needs.

1. Once you are done with the table, click on the **Create app** button to create the app.

1. The AI Copilot will generate a responsive Canvas app based on your description. You can then customize the app to meet your needs.

1. For educators to send emails to students, you can use Copilot to add a new screen to the app. For example, you can use the following prompt to add a new screen to the app: **_I want to add a screen to send emails to students_**. Click on the **Send** button to send the prompt to the AI Copilot.

![Adding a new screen via a prompt instruction](./images/copilot-new-screen.png?WT.mc_id=academic-105485-koreyst)

1. The AI Copilot will generate a new screen and you can then customize the screen to meet your needs.

1. Once you are done with the app, click on the **Save** button to save the app.

1. To share the app with the educators, click on the **Share** button and then click on the **Share** button again. You can then share the app with the educators by entering their email addresses.

> **Your homework**: The app you just built is a good start but can be improved. With the email feature, educators can only send emails to students manually by having to type their emails. Can you use Copilot to build an automation that will enable educators to send emails to students automatically when they submit their assignments? Your hint is with the right prompt you can use Copilot in Power Automate to build this.

### Build an Invoices Information Table for Our Startup

The finance team of our startup has been struggling to keep track of invoices. They have been using a spreadsheet to track the invoices but this has become difficult to manage as the number of invoices has increased. They have asked you to build a table that will help them store, track and manage the information of the invoices they received. The table should be used to build an automation that will extract all the invoice information and store it in the table. The table should also enable the finance team to view the invoices that have been paid and those that have not been paid.

The Power Platform has an underlying data platform called Dataverse that enables you to store the data for your apps and solutions. Dataverse provides a low-code data platform for storing the app's data. It is a fully managed service that securely stores data in the Microsoft Cloud and is provisioned within your Power Platform environment. It comes with built-in data governance capabilities, such as data classification, data lineage, fine-grained access control, and more. You can learn more [about Dataverse here](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Why should we use Dataverse for our startup? The standard and custom tables within Dataverse provide a secure and cloud-based storage option for your data. Tables let you store different types of data, similar to how you might use multiple worksheets in a single Excel workbook. You can use tables to store data that is specific to your organization or business need. Some of the benefits our startup will get from using Dataverse include but are not limited to:

- **Easy to manage**: Both the metadata and data are stored in the cloud, so you don't have to worry about the details of how they are stored or managed. You can focus on building your apps and solutions.

- **Secure**: Dataverse provides a secure and cloud-based storage option for your data. You can control who has access to the data in your tables and how they can access it using role based security.

- **Rich metadata**: Data types and relationships are used directly within Power Apps

- **Logic and validation**: You can use business rules, calculated fields, and validation rules to enforce business logic and maintain data accuracy.

Now that you know what Dataverse is and why you should use it, let's look at how you can use Copilot to create a table in Dataverse to meet the requirements of our finance team.

> **Note** : You will use this table in the next section to build an automation that will extract all the invoice information and store it in the table.

To create a table in Dataverse using Copilot, follow the steps below:

1. Navigate to the [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) home screen.

2. On the left navigation bar, select on **Tables** and then click on **Describe the new Table**.

![Select new table](./images/describe-new-table.png?WT.mc_id=academic-105485-koreyst)

1. On the **Describe the new Table** screen, use the text area to describe the table you want to create. For example, **_I want to create a table to store invoice information_**. Click on the **Send** button to send the prompt to the AI Copilot.

![Describe the table](./images/copilot-chat-prompt-dataverse.png?WT.mc_id=academic-105485-koreyst)

1. The AI Copilot will suggest a Dataverse Table with the fields you need to store the data you want to track and some sample data. You can then customize the table to meet your needs using the AI Copilot assistant feature through conversational steps.

![Suggested Dataverse table](./images/copilot-dataverse-table.png?WT.mc_id=academic-105485-koreyst)

1. The finance team wants to send an email to the supplier to update them with the current status of their invoice. You can use Copilot to add a new field to the table to store the supplier email. For example, you can use the following prompt to add a new field to the table: **_I want to add a column to store supplier email_**. Click on the **Send** button to send the prompt to the AI Copilot.

1. The AI Copilot will generate a new field and you can then customize the field to meet your needs.

1. Once you are done with the table, click on the **Create** button to create the table.

## AI Models in Power Platform with AI Builder

AI Builder is a low-code AI capability available in Power Platform that enables you to use AI Models to help you to automate processes and predict outcomes. With AI Builder you can bring AI to your apps and flows that connect to your data in Dataverse or in various cloud data sources, such as SharePoint, OneDrive or Azure.

## Prebuilt AI Models vs Custom AI Models

AI Builder provides two types of AI Models: Prebuilt AI Models and Custom AI Models. Prebuilt AI Models are ready-to-use AI Models that are trained by Microsoft and available in Power Platform. These help you add intelligence to your apps and flows without having to gather data and then build, train and publish your own models. You can use these models to automate processes and predict outcomes.

Some of the Prebuilt AI Models available in Power Platform include:

- **Key Phrase Extraction**: This model extracts key phrases from text.
- **Language Detection**: This model detects the language of a text.
- **Sentiment Analysis**: This model detects positive, negative, neutral, or mixed sentiment in text.
- **Business Card Reader**: This model extracts information from business cards.
- **Text Recognition**: This model extracts text from images.
- **Object Detection**: This model detects and extracts objects from images.
- **Document processing**: This model extracts information from forms.
- **Invoice Processing**: This model extracts information from invoices.

With Custom AI Models you can bring your own model into AI Builder so that it can function like any AI Builder custom model, allowing you to train the model using your own data. You can use these models to automate processes and predict outcomes in both Power Apps and Power Automate. When using your own model there are limitations that apply. Read more on these [limitations](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

![AI builder models](./images/ai-builder-models.png?WT.mc_id=academic-105485-koreyst)

## Assignment #2 - Build an Invoice Processing Flow for Our Startup

The finance team has been struggling to process invoices. They have been using a spreadsheet to track the invoices but this has become difficult to manage as the number of invoices has increased. They have asked you to build a workflow that will help them process invoices using AI. The workflow should enable them to extract information from invoices and store the information in a Dataverse table. The workflow should also enable them to send an email to the finance team with the extracted information.

Now that you know what AI Builder is and why you should use it, let's look at how you can use the Invoice Processing AI Model in AI Builder, that we covered earlier on, to build a workflow that will help the finance team process invoices.

To build a workflow that will help the finance team process invoices using the Invoice Processing AI Model in AI Builder, follow the steps below:

1. Navigate to the [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst) home screen.

2. Use the text area on the home screen to describe the workflow you want to build. For example, **_Process an invoice when it arrives in my mailbox_**. Click on the **Send** button to send the prompt to the AI Copilot.

   ![Copilot power automate](./images/copilot-chat-prompt-powerautomate.png?WT.mc_id=academic-105485-koreyst)

3. The AI Copilot will suggest the actions you need to perform the task you want to automate. You can click on the **Next** button to go through the next steps.

4. On the next step, Power Automate will prompt you to set up the connections required for the flow. Once you are done, click on the **Create flow** button to create the flow.

5. The AI Copilot will generate a flow and you can then customize the flow to meet your needs.

6. Update the trigger of the flow and set the **Folder** to the folder where the invoices will be stored. For example, you can set the folder to **Inbox**. Click on **Show advanced options** and set the **Only with Attachments** to **Yes**. This will ensure that the flow only runs when an email with an attachment is received in the folder.

7. Remove the following actions from the flow: **HTML to text**, **Compose**, **Compose 2**, **Compose 3** and **Compose 4** because you will not be using them.

8. Remove the **Condition** action from the flow because you will not be using it. It should look like the following screenshot:

   ![power automate, remove actions](./images/powerautomate-remove-actions.png?WT.mc_id=academic-105485-koreyst)

9. Click on the **Add an action** button and search for **Dataverse**. Select the **Add a new row** action.

10. On the **Extract Information from invoices** action, update the **Invoice File** to point to the **Attachment Content** from the email. This will ensure that the flow extracts information from the invoice attachment.

11. Select the **Table** you created earlier on. For example, you can select the **Invoice Information** table. Choose the dynamic content from the previous action to populate the following fields:

    - ID
    - Amount
    - Date
    - Name
    - Status - Set the **Status** to **Pending**.
    - Supplier Email - Use the **From** dynamic content from the **When a new email arrives** trigger.

    ![power automate add row](./images/powerautomate-add-row.png?WT.mc_id=academic-105485-koreyst)

12. Once you are done with the flow, click on the **Save** button to save the flow. You can then test the flow by sending an email with an invoice to the folder you specified in the trigger.

> **Your homework**: The flow you just built is a good start, now you need to think of how you can build an automation that will enable our finance team to send an email to the supplier to update them with the current status of their invoice. Your hint: the flow must run when the status of the invoice changes.

## Use a Text Generation AI Model in Power Automate

The Create Text with GPT AI Model in AI Builder enables you to generate text based on a prompt and is powered by the Microsoft Azure OpenAI Service. With this capability, you can incorporate GPT (Generative Pre-Trained Transformer) technology into your apps and flows to build a variety of automated flows and insightful applications.

GPT models undergo extensive training on vast amounts of data, enabling them to produce text that closely resembles human language when provided with a prompt. When integrated with workflow automation, AI models like GPT can be harnessed to streamline and automate a wide range of tasks.

For example, you can build flows to automatically generate text for a variety of use cases, such as: drafts of emails, product descriptions, and more. You can also use the model to generate text for a variety of apps, such as chatbots and customer service apps that enable customer service agents to respond effectively and efficiently to customer inquiries.

![create a prompt](./images/create-prompt-gpt.png?WT.mc_id=academic-105485-koreyst)

To learn how to use this AI Model in Power Automate, go through the [Add intelligence with AI Builder and GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko) module.

## Great Work! Continue Your Learning

After completing this lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue leveling up your Generative AI knowledge!

Head over to Lesson 11 where we will look at how to [integrate Generative AI with Function Calling](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!
