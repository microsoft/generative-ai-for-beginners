# Building Generative AI-Powered Chat Applications

[![Building Generative AI-Powered Chat Applications](./images/07-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lessons7-gh?WT.mc_id=academic-105485-koreyst)

> _(Click the image above to view video of this lesson)_

Now that we've seen how we can build text-generation apps, let's look into chat applications.

Chat applications have become integrated into our daily lives, offering more than just a means of casual conversation. They're integral parts of customer service, technical support, and even sophisticated advisory systems. It's likely that you've gotten some help from a chat application not too long ago. As we integrate more advanced technologies like generative AI into these platforms, the complexity increases and so does the challenges.

Some questions we need to be answered are:

- **Building the app**. How do we efficiently build and seamlessly integrate these AI-powered applications for specific use cases?
- **Monitoring**. Once deployed, how can we monitor and ensure that the applications are operating at the highest level of quality, both in terms of functionality and adhering to the [six principles of responsible AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

As we move further into an age defined by automation and seamless human-machine interactions, understanding how generative AI transforms the scope, depth, and adaptability of chat applications becomes essential. This lesson will investigate the aspects of architecture that support these intricate systems, delve into the methodologies for fine-tuning them for domain-specific tasks, and evaluate the metrics and considerations pertinent to ensuring responsible AI deployment.

## Introduction

This lesson covers:

- Techniques for efficiently building and integrating chat applications.
- How to apply customization and fine-tuning to applications.
- Strategies and considerations to effectively monitor chat applications.

## Learning Goals

By the end of this lesson, you'll be able to:

- Describe considerations for building and integrating chat applications into existing systems.
- Customize chat applications for specific use-cases.
- Identify key metrics and considerations to effectively monitor and maintain the quality of AI-powered chat applications.
- Ensure chat applications leverage AI responsibly.

## Integrating Generative AI into Chat Applications

Elevating chat applications through generative AI isn't only centered around making them smarter; it's about optimizing their architecture, performance, and user interface to deliver a quality user experience. This involves investigating the architectural foundations, API integrations, and user interface considerations. This section aims to offer you a comprehensive roadmap for navigating these complex landscapes, whether you're plugging them into existing systems or building them as stand-alone platforms.

By the end of this section, you'll be equipped with the expertise needed to efficiently construct and incorporate chat applications.

### Chatbot or Chat application?

Before we dive into building chat applications, let's compare 'chatbots' against 'AI-powered chat applications,' which serve distinct roles and functionalities. A chatbot's main purpose is to automate specific conversational tasks, such as answering frequently asked questions or tracking a package. It's typically governed by rule-based logic or complex AI algorithms. In contrast, an AI-powered chat application is a far more expansive environment designed to facilitate various forms of digital communication, such as text, voice, and video chats among human users. Its defining feature is the integration of a generative AI model that simulates nuanced, human-like conversations, generating responses based on a wide variety of input and contextual cues. A generative AI powered chat application can engage in open-domain discussions, adapt to evolving conversational contexts, and even produce creative or complex dialogue.

The table below outlines the key differences and similarities to help us understand their unique roles in digital communication.

| Chatbot                               | Generative AI-Powered Chat Application |
| ------------------------------------- | -------------------------------------- |
| Task-Focused and rule based           | Context-aware                          |
| Often integrated into larger systems  | May host one or multiple chatbots      |
| Limited to programmed functions       | Incorporates generative AI models      |
| Specialized & structured interactions | Capable of open-domain discussions     |

### Leveraging pre-built functionalities with SDKs and APIs

When building a chat application, a great first step is to assess what is already out there. Using SDKs and APIs to build chat applications is an advantageous strategy for a variety of reasons. By integrating well-documented SDKs and APIs, you're strategically positioning your application for long-term success, addressing scalability and maintenance concerns.

- **Expedites the development process and reduces overhead**: Relying on pre-built functionalities instead of the expensive process of building them yourself allows you to focus on other aspects of your application that you may find more important, such as business logic.
- **Better performance**: When building functionality from scratch, you'll eventually ask yourself "How does it scale? Is this application capable of handling a sudden influx of users?" Well maintained SDK and APIs often have built in solutions for these concerns.
- **Easier maintenance**: Updates and improvements are easier to manage as most APIs and SDKs simply require an update to a library when a newer version is released.
- **Access to cutting edge technology**: Leveraging models that have been fined tuned and trained on extensive datasets provides your application with natural language capabilities.

Accessing functionality of an SDK or API typically involves obtaining permission to use the provided services, which is often through the use of a unique key or authentication token. We'll use the OpenAI Python Library to explore what this looks like. You can also try it out on your own in the following [notebook for OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) or [notebook for Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) for this lesson.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

chat_completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Suggest two titles for an instructional lesson on chat applications for generative AI."}])
```

The above example uses the GPT-3.5 Turbo model to complete the prompt, but notice that the API key is set prior to doing so. You'd receive an error if you didn't set the key.

## User Experience (UX)

General UX principles apply to chat applications, but here are some additional considerations that become particularly important due to the machine learning components involved.

- **Mechanism for addressing ambiguity**: Generative AI models occasionally generate ambiguous answers. A feature that allows users to ask for clarification can be helpful should they come across this problem.
- **Context retention**: Advanced generative AI models have the ability to remember context within a conversation, which can be a necessary asset to the user experience. Giving users the ability to control and manage context improves the user experience, but introduces the risk of retaining sensitive user information. Considerations for how long this information is stored, such as introducing a retention policy, can balance the need for context against privacy.
- **Personalization**: With the ability to learn and adapt, AI models offer an individualized experience for a user. Tailoring the user experience through features like user profiles not only makes the user feel understood, but it also helps their pursuit of finding specific answers, creating a more efficient and satisfying interaction.

One such example of personalization is the "Custom instructions" settings in OpenAI's ChatGPT. It allows you to provide information about yourself that may be important context for your prompts. Here's an example of a custom instruction.

![Custom Instructions Settings in ChatGPT](./images/custom-instructions.png?WT.mc_id=academic-105485-koreyst)

This "profile" prompts ChatGPT to create a lesson plan on linked lists. Notice that ChatGPT takes into account that the user may want a more in depth lesson plan based on her experience.

![A prompt in ChatGPT for a lesson plan about linked lists](./images/lesson-plan-prompt.png?WT.mc_id=academic-105485-koreyst)

### Microsoft's System Message Framework for Large Language Models

[Microsoft has provided guidance](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) for writing effective system messages when generating responses from LLMs broken down into 4 areas:

1. Defining who the model is for, as well as its capabilities and limitations.
2. Defining the model's output format.
3. Providing specific examples that demonstrate intended behavior of the model.
4. Providing additional behavioral guardrails.

### Accessibility

Whether a user has visual, auditory, motor, or cognitive impairments, a well-designed chat application should be usable by all. The following list breaks down specific features aimed at enhancing accessibility for various user impairments.

- **Features for Visual Impairment**: High contrast themes and resizable text, screen reader compatibility.
- **Features for Auditory Impairment**: Text-to-speech and speech-to-text functions, visual cues for audio notifications.
- **Features for Motor Impairment**: Keyboard navigation support, voice commands.
- **Features for Cognitive Impairment**: Simplified language options.

## Customization and Fine-tuning for Domain-Specific Language Models

Imagine a chat application that understands your company's jargon and anticipates the specific queries its user base commonly has. There are a couple of approaches worth mentioning:

- **Leveraging DSL models**. DSL stands for domain specific language. You can leverage a so called DSL model trained on a specific domain to understand it's concepts and scenarios.
- **Apply fine-tuning**. Fine-tuning is the process of further training your model with specific data.

## Customization: Using a DSL

Leveraging a domain-specific language models (DSL Models) can enhance user engagement and by providing specialized, contextually relevant interactions. It's a model that is trained or fine-tuned to understand and generate text related to a specific field, industry, or subject. Options for using a DSL model can vary from training one from scratch, to using pre-existing ones through SDKs and APIs. Another option is fine-tuning, which involves taking an existing pre-trained model and adapting it for a specific domain.

## Customization: Apply fine-tuning

Fine-tuning is often considered when a pre-trained model falls short in a specialized domain or specific task.

For instance, medical queries are complex and require a lot of context. When a medical professional diagnoses a patient it's based on a variety of factors such as lifestyle or pre-existing conditions, and may even rely on recent medical journals to validate their diagnosis. In such nuanced scenarios, a general-purpose AI chat application cannot be a reliable source.

### Scenario: a medical application

Consider a chat application designed to assist medical practitioners by providing quick references to treatment guidelines, drug interactions, or recent research findings.

A general-purpose model might be adequate for answering basic medical questions or providing general advice, but it may struggle with the following:

- **Highly specific or complex cases**. For example, a neurologist might ask the application, "What are the current best practices for managing drug-resistant epilepsy in pediatric patients?"
- **Lacking recent advancements**. A general-purpose model could struggle to provide a current answer that incorporates the most recent advancements in neurology and pharmacology.

In instances such as these, fine-tuning the model with a specialized medical dataset can significantly improve its ability to handle these intricate medical inquiries more accurately and reliably. This requires access to a large and relevant dataset that represents the domain-specific challenges and questions that need to be addressed.

## Considerations for a High Quality AI-Driven Chat Experience

This section outlines the criteria for "high-quality" chat applications, which include the capture of actionable metrics and adherence to a framework that responsibly leverages AI technology.

### Key Metrics

To maintain the high-quality performance an application, it's essential to keep track of key metrics and considerations. These measurements not only ensure the functionality of the application but also assess the quality of the AI model and user experience. Below is a list that covers basic, AI, and user experience metrics to consider.

| Metric                        | Definition                                                                                                             | Considerations for Chat Developer                                         |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Uptime**                    | Measures the time the application is operational and accessible by users.                                              | How will you minimize downtime?                                           |
| **Response Time**             | The time taken by the application to reply to a user's query.                                                          | How can you optimize query processing to improve response time?           |
| **Precision**                 | The ratio of true positive predictions to the total number of positive predictions                                     | How will you validate the precision of your model?                        |
| **Recall (Sensitivity)**      | The ratio of true positive predictions to the actual number of positives                                               | How will you measure and improve recall?                                  |
| **F1 Score**                  | The harmonic mean of precision and recall, that balances the trade-off between both.                                   | What is your target F1 Score? How will you balance precision and recall?  |
| **Perplexity**                | Measures how well the probability distribution predicted by the model aligns with the actual distribution of the data. | How will you minimize perplexity?                                         |
| **User Satisfaction Metrics** | Measures the user's perception of the application. Often captured through surveys.                                     | How often will you collect user feedback? How will you adapt based on it? |
| **Error Rate**                | The rate at which the model makes mistakes in understanding or output.                                                 | What strategies do you have in place to reduce error rates?               |
| **Retraining Cycles**         | The frequency with which the model is updated to incorporate new data and insights.                                    | How often will you retrain the model? What triggers a retraining cycle?   |
| **Anomaly Detection**         | Tools and techniques for identifying unusual patterns that do not conform to expected behavior.                        | How will you respond to anomalies?                                        |

### Implementing Responsible AI Practices in Chat Applications

Microsoft's approach to Responsible AI has identified six principles that should guide AI development and use. Below are the principles, their definition, and things a chat developer should consider and why they should take them seriously.

| Principles             | Microsoft's Definition                                | Considerations for Chat Developer                                      | Why It's Important                                                                     |
| ---------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Fairness               | AI systems should treat all people fairly.            | Ensure the chat application does not discriminate based on user data.  | To build trust and inclusivity among users; avoids legal ramifications.                |
| Reliability and Safety | AI systems should perform reliably and safely.        | Implement testing and fail-safes to minimize errors and risks.         | Ensures user satisfaction and prevents potential harm.                                 |
| Privacy and Security   | AI systems should be secure and respect privacy.      | Implement strong encryption and data protection measures.              | To safeguard sensitive user data and comply with privacy laws.                         |
| Inclusiveness          | AI systems should empower everyone and engage people. | Design UI/UX that is accessible and easy-to-use for diverse audiences. | Ensures a wider range of people can use the application effectively.                   |
| Transparency           | AI systems should be understandable.                  | Provide clear documentation and reasoning for AI responses.            | Users are more likely to trust a system if they can understand how decisions are made. |
| Accountability         | People should be accountable for AI systems.          | Establish a clear process for auditing and improving AI decisions.     | Enables ongoing improvement and corrective measures in case of mistakes.               |

## Assignment

See [assignment](./python?WT.mc_id=academic-105485-koreyst) it will take you through a series of exercises from running your first chat prompts, to classifying and summarizing text and more. Notice that the assignments are available in different programming languages!

## Great Work! Continue the Journey

After completing this lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue leveling up your Generative AI knowledge!

Head over to Lesson 8 to see how you can start [building search applications](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!
