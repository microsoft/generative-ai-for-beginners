<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5308963a56cfbad2d73b0fa99fe84b3",
  "translation_date": "2025-10-17T22:33:38+00:00",
  "source_file": "07-building-chat-applications/README.md",
  "language_code": "en"
}
-->
# Building Generative AI-Powered Chat Applications

[![Building Generative AI-Powered Chat Applications](../../../translated_images/07-lesson-banner.a279b937f2843833fe28b4597f51bdef92d0ad03efee7ba52d0f166dea7574e5.en.png)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Click the image above to view video of this lesson)_

Now that we've explored how to create text-generation applications, let's dive into chat applications.

Chat applications have become a fundamental part of our daily lives, serving purposes beyond casual conversation. They play key roles in customer service, technical support, and even advanced advisory systems. Chances are, you've interacted with a chat application recently. As we incorporate advanced technologies like generative AI into these platforms, the complexity grows, along with the challenges.

Some questions we need to address include:

- **Building the app**. How can we efficiently develop and seamlessly integrate these AI-powered applications for specific use cases?
- **Monitoring**. Once deployed, how can we ensure these applications operate at peak quality, both in functionality and in alignment with the [six principles of responsible AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

As we progress into an era defined by automation and seamless human-machine interactions, understanding how generative AI reshapes the scope, depth, and adaptability of chat applications becomes crucial. This lesson will explore the architectural elements that support these complex systems, examine methods for fine-tuning them for specific tasks, and assess the metrics and considerations necessary for responsible AI deployment.

## Introduction

This lesson covers:

- Techniques for efficiently building and integrating chat applications.
- How to apply customization and fine-tuning to applications.
- Strategies and considerations for effectively monitoring chat applications.

## Learning Goals

By the end of this lesson, you'll be able to:

- Explain considerations for building and integrating chat applications into existing systems.
- Customize chat applications for specific use cases.
- Identify key metrics and strategies to effectively monitor and maintain the quality of AI-powered chat applications.
- Ensure chat applications use AI responsibly.

## Integrating Generative AI into Chat Applications

Enhancing chat applications with generative AI isn't just about making them smarter; it's about optimizing their architecture, performance, and user interface to deliver a superior user experience. This involves examining architectural foundations, API integrations, and user interface design. This section provides a comprehensive roadmap for navigating these complexities, whether you're integrating them into existing systems or building standalone platforms.

By the end of this section, you'll have the expertise to efficiently design and integrate chat applications.

### Chatbot or Chat Application?

Before we delve into building chat applications, let's distinguish between 'chatbots' and 'AI-powered chat applications,' which serve different roles and functionalities. A chatbot primarily automates specific conversational tasks, such as answering FAQs or tracking packages, often using rule-based logic or advanced AI algorithms. On the other hand, an AI-powered chat application is a broader platform designed for various forms of digital communication, including text, voice, and video chats among human users. Its standout feature is the integration of a generative AI model that simulates nuanced, human-like conversations, generating responses based on diverse inputs and contextual cues. Generative AI-powered chat applications can engage in open-ended discussions, adapt to evolving conversational contexts, and even produce creative or complex dialogue.

The table below highlights the key differences and similarities to help clarify their unique roles in digital communication.

| Chatbot                               | Generative AI-Powered Chat Application |
| ------------------------------------- | -------------------------------------- |
| Task-focused and rule-based           | Context-aware                          |
| Often integrated into larger systems  | May host one or multiple chatbots      |
| Limited to programmed functions       | Incorporates generative AI models      |
| Specialized & structured interactions | Capable of open-domain discussions     |

### Leveraging Pre-Built Functionalities with SDKs and APIs

When developing a chat application, a good starting point is to evaluate existing resources. Using SDKs and APIs to build chat applications offers several advantages. By integrating well-documented SDKs and APIs, you set your application up for long-term success, addressing scalability and maintenance challenges.

- **Speeds up development and reduces overhead**: Utilizing pre-built functionalities instead of creating them from scratch allows you to focus on other critical aspects of your application, such as business logic.
- **Improved performance**: Building functionality from scratch often raises questions like "How does it scale? Can this application handle a sudden surge in users?" Well-maintained SDKs and APIs often include built-in solutions for these concerns.
- **Simplified maintenance**: Updates and improvements are easier to manage, as most APIs and SDKs only require updating a library when a new version is released.
- **Access to cutting-edge technology**: Using models that have been fine-tuned and trained on extensive datasets equips your application with advanced natural language capabilities.

Accessing the functionality of an SDK or API typically involves obtaining permission to use the provided services, often through a unique key or authentication token. We'll use the OpenAI Python Library to demonstrate this process. You can also try it yourself using the following [notebook for OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) or [notebook for Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) for this lesson.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

chat_completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Suggest two titles for an instructional lesson on chat applications for generative AI."}])
```

The example above uses the GPT-3.5 Turbo model to complete the prompt, but note that the API key must be set beforehand. Without setting the key, you'd encounter an error.

## User Experience (UX)

General UX principles apply to chat applications, but there are additional considerations that become particularly important due to the machine learning components involved.

- **Mechanism for addressing ambiguity**: Generative AI models sometimes produce ambiguous answers. A feature allowing users to request clarification can be helpful in such cases.
- **Context retention**: Advanced generative AI models can remember context within a conversation, which can be a valuable asset for user experience. Allowing users to control and manage context enhances the experience but introduces risks related to retaining sensitive user information. Considerations like retention policies can balance the need for context with privacy concerns.
- **Personalization**: AI models can learn and adapt, offering a personalized experience for users. Features like user profiles not only make users feel understood but also help them find specific answers more efficiently, creating a more satisfying interaction.

An example of personalization is the "Custom instructions" feature in OpenAI's ChatGPT. It lets users provide information about themselves that may be relevant to their prompts. Here's an example of a custom instruction.

![Custom Instructions Settings in ChatGPT](../../../translated_images/custom-instructions.b96f59aa69356fcfed456414221919e8996f93c90c20d0d58d1bc0221e3c909f.en.png)

This "profile" prompts ChatGPT to create a lesson plan on linked lists. Notice how ChatGPT considers the user's experience level to provide a more detailed lesson plan.

![A prompt in ChatGPT for a lesson plan about linked lists](../../../translated_images/lesson-plan-prompt.cc47c488cf1343df5d67aa796a1acabca32c380e5b782971e289f6ab8b21cf5a.en.png)

### Microsoft's System Message Framework for Large Language Models

[Microsoft offers guidance](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) for crafting effective system messages when generating responses from LLMs, broken down into four areas:

1. Defining the intended audience, capabilities, and limitations of the model.
2. Specifying the model's output format.
3. Providing examples that illustrate the desired behavior of the model.
4. Establishing additional behavioral guardrails.

### Accessibility

A well-designed chat application should be accessible to all users, including those with visual, auditory, motor, or cognitive impairments. Below are features aimed at improving accessibility for various user needs.

- **Features for Visual Impairment**: High-contrast themes, resizable text, screen reader compatibility.
- **Features for Auditory Impairment**: Text-to-speech and speech-to-text functions, visual indicators for audio notifications.
- **Features for Motor Impairment**: Keyboard navigation support, voice commands.
- **Features for Cognitive Impairment**: Simplified language options.

## Customization and Fine-Tuning for Domain-Specific Language Models

Imagine a chat application that understands your company's terminology and anticipates the specific queries its users commonly have. There are two approaches worth considering:

- **Using DSL models**. DSL stands for domain-specific language. You can use a DSL model trained on a specific domain to understand its concepts and scenarios.
- **Applying fine-tuning**. Fine-tuning involves further training your model with specific data.

## Customization: Using a DSL

Domain-specific language models (DSL models) enhance user engagement by providing specialized, contextually relevant interactions. These models are trained or fine-tuned to understand and generate text related to a specific field, industry, or subject. Options for using a DSL model range from training one from scratch to utilizing pre-existing models through SDKs and APIs. Another option is fine-tuning, which adapts an existing pre-trained model for a specific domain.

## Customization: Apply Fine-Tuning

Fine-tuning is often necessary when a pre-trained model falls short in handling specialized domains or tasks.

For example, medical queries are complex and require significant context. When diagnosing a patient, medical professionals consider various factors like lifestyle, pre-existing conditions, and even recent medical research. In such nuanced scenarios, a general-purpose AI chat application may not be reliable.

### Scenario: A Medical Application

Consider a chat application designed to assist medical professionals by providing quick references to treatment guidelines, drug interactions, or recent research findings.

A general-purpose model might suffice for basic medical questions or general advice, but it may struggle with:

- **Highly specific or complex cases**. For instance, a neurologist might ask, "What are the current best practices for managing drug-resistant epilepsy in pediatric patients?"
- **Incorporating recent advancements**. A general-purpose model might fail to provide answers that include the latest developments in neurology and pharmacology.

In such cases, fine-tuning the model with a specialized medical dataset can greatly enhance its ability to address complex medical queries accurately and reliably. This requires access to a large, relevant dataset that represents the domain-specific challenges and questions.

## Considerations for a High-Quality AI-Driven Chat Experience

This section outlines the criteria for "high-quality" chat applications, including tracking actionable metrics and adhering to a framework for responsibly utilizing AI technology.

### Key Metrics

To ensure high-quality performance, it's essential to monitor key metrics and considerations. These measurements not only ensure the application's functionality but also evaluate the AI model's quality and user experience. Below is a list of basic, AI, and user experience metrics to consider.

| Metric                        | Definition                                                                                                             | Considerations for Chat Developer                                         |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Uptime**                    | Measures the time the application is operational and accessible by users.                                              | How will you minimize downtime?                                           |
| **Response Time**             | The time taken by the application to reply to a user's query.                                                          | How can you optimize query processing to improve response time?           |
| **Precision**                 | The ratio of true positive predictions to the total number of positive predictions                                     | How will you validate the precision of your model?                        |
| **Recall (Sensitivity)**      | The ratio of true positive predictions to the actual number of positives                                               | How will you measure and improve recall?                                  |
| **F1 Score**                  | The harmonic mean of precision and recall, balancing the trade-off between both.                                       | What is your target F1 Score? How will you balance precision and recall?  |
| **Perplexity**                | Measures how well the probability distribution predicted by the model aligns with the actual distribution of the data. | How will you minimize perplexity?                                         |
| **User Satisfaction Metrics** | Measures the user's perception of the application, often captured through surveys.                                     | How often will you collect user feedback? How will you adapt based on it? |
| **Error Rate**                | The rate at which the model makes mistakes in understanding or output.                                                 | What strategies do you have in place to reduce error rates?               |
| **Retraining Cycles**         | The frequency with which the model is updated to incorporate new data and insights.                                    | How often will you retrain the model? What triggers a retraining cycle?   |
| **Anomaly Detection**         | Tools and techniques for identifying unusual patterns that deviate from expected behavior.                        | How will you address anomalies?                                        |

### Implementing Responsible AI Practices in Chat Applications

Microsoft's approach to Responsible AI has outlined six principles that should guide the development and use of AI. Below are the principles, their definitions, and considerations for chat developers, along with reasons why they are important.

| Principles             | Microsoft's Definition                                | Considerations for Chat Developer                                      | Why It's Important                                                                     |
| ---------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Fairness               | AI systems should treat all people fairly.            | Ensure the chat application does not discriminate based on user data.  | Builds trust and inclusivity among users; avoids legal consequences.                   |
| Reliability and Safety | AI systems should perform reliably and safely.        | Implement testing and fail-safes to minimize errors and risks.         | Ensures user satisfaction and prevents potential harm.                                 |
| Privacy and Security   | AI systems should be secure and respect privacy.      | Implement strong encryption and data protection measures.              | Protects sensitive user data and ensures compliance with privacy regulations.          |
| Inclusiveness          | AI systems should empower everyone and engage people. | Design UI/UX that is accessible and user-friendly for diverse audiences. | Ensures a broader range of people can effectively use the application.                 |
| Transparency           | AI systems should be understandable.                  | Provide clear documentation and explanations for AI responses.         | Users are more likely to trust a system if they understand how decisions are made.     |
| Accountability         | People should be accountable for AI systems.          | Establish a clear process for auditing and improving AI decisions.     | Facilitates ongoing improvement and corrective actions in case of errors.              |

## Assignment

See [assignment](../../../07-building-chat-applications/python). It will guide you through a series of exercises, from running your first chat prompts to classifying and summarizing text, and more. Note that the assignments are available in various programming languages!

## Great Work! Continue the Journey

After completing this lesson, explore our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to further enhance your knowledge of Generative AI!

Proceed to Lesson 8 to learn how to start [building search applications](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.