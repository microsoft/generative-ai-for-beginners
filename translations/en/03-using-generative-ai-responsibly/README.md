<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-06-25T11:09:47+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "en"
}
-->
# Using Generative AI Responsibly

It's easy to be fascinated with AI, especially generative AI, but it's important to consider how to use it responsibly. You need to think about ensuring the output is fair, non-harmful, and more. This chapter aims to provide you with the context, considerations, and steps to improve your AI usage.

## Introduction

This lesson will cover:

- Why Responsible AI should be a priority when building Generative AI applications.
- Core principles of Responsible AI and their relation to Generative AI.
- How to apply these Responsible AI principles through strategy and tools.

## Learning Goals

After completing this lesson, you will understand:

- The importance of Responsible AI in building Generative AI applications.
- When to consider and apply the core principles of Responsible AI in Generative AI development.
- Available tools and strategies to implement Responsible AI.

## Responsible AI Principles

The excitement around Generative AI is at an all-time high, attracting new developers, attention, and funding. While this is positive for building products and companies with Generative AI, it's crucial to proceed responsibly.

Throughout this course, we focus on building our startup and AI education product using Responsible AI principles: Fairness, Inclusiveness, Reliability/Safety, Security & Privacy, Transparency, and Accountability. We'll explore how these principles relate to our use of Generative AI in our products.

## Why Should You Prioritize Responsible AI

When creating a product, taking a human-centric approach that prioritizes users' best interests leads to the best outcomes.

Generative AI's uniqueness lies in its ability to generate helpful answers, information, guidance, and content for users with minimal manual steps, often yielding impressive results. However, without proper planning and strategies, it can also result in harmful outcomes for users, your product, and society.

Let's examine some of these potentially harmful outcomes:

### Hallucinations

Hallucinations occur when an LLM produces content that is either nonsensical or factually incorrect based on other information sources.

For example, if we build a feature for our startup that allows students to ask historical questions to a model, a student might ask `Who was the sole survivor of Titanic?`.

The model produces a response like the one below:

![Prompt saying "Who was the sole survivor of the Titanic"](../../../03-using-generative-ai-responsibly/images/ChatGPT-titanic-survivor-prompt.webp)

This is a confident and thorough answer, but it's incorrect. Even minimal research would reveal that there was more than one survivor of the Titanic disaster. For a student just beginning to research this topic, this answer could be persuasive enough to be taken as fact, leading to an unreliable AI system and damaging our startup's reputation.

Despite performance improvements in minimizing hallucinations with each LLM iteration, application builders and users must remain aware of these limitations.

### Harmful Content

We've discussed how an LLM can produce incorrect or nonsensical responses. Another risk is when a model generates harmful content.

Harmful content includes:

- Encouraging or instructing self-harm or harm to specific groups.
- Hateful or demeaning content.
- Guiding the planning of attacks or violent acts.
- Providing instructions for finding illegal content or committing illegal acts.
- Displaying sexually explicit content.

For our startup, we need the right tools and strategies to prevent this type of content from reaching students.

### Lack of Fairness

Fairness is defined as “ensuring an AI system is free from bias and discrimination, treating everyone fairly and equally.” In Generative AI, we want to avoid reinforcing exclusionary worldviews of marginalized groups in the model’s output.

These outputs not only damage positive product experiences for users but also cause societal harm. As application builders, we should always consider a wide and diverse user base when developing Generative AI solutions.

## How to Use Generative AI Responsibly

Having identified the importance of Responsible Generative AI, let's look at four steps to build our AI solutions responsibly:

### Measure Potential Harms

In software testing, we test expected user actions on an application. Similarly, testing a diverse set of prompts users are likely to use helps measure potential harm.

Since our startup is developing an education product, preparing a list of education-related prompts is beneficial. This could cover specific subjects, historical facts, and student life prompts.

### Mitigate Potential Harms

It's time to find ways to prevent or limit potential harm caused by the model and its responses. We can approach this in four layers:

- **Model**. Choose the right model for the use case. Larger and more complex models like GPT-4 pose more risk of harmful content when applied to smaller, specific use cases. Fine-tuning with your training data reduces the risk of harmful content.

- **Safety System**. A safety system comprises tools and configurations on the platform serving the model to mitigate harm. For example, the content filtering system on Azure OpenAI service. Systems should also detect jailbreak attacks and unwanted activity like bot requests.

- **Metaprompt**. Metaprompts and grounding direct or limit the model based on behaviors and information. This could involve using system inputs to define model limits and providing outputs relevant to the system's scope or domain.

It could also involve techniques like Retrieval Augmented Generation (RAG) to pull information only from trusted sources. A later lesson in this course covers [building search applications](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst).

- **User Experience**. The final layer is user interaction with the model through the application interface. Design the UI/UX to limit input types users can send to the model and the text or images displayed to users. Be transparent about what the Generative AI application can and can’t do when deploying it.

We have an entire lesson on [Designing UX for AI Applications](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst).

- **Evaluate model**. Working with LLMs can be challenging due to limited control over the training data. Nonetheless, evaluate the model’s performance and outputs. Measure accuracy, similarity, groundedness, and output relevance to provide transparency and trust to stakeholders and users.

### Operate a Responsible Generative AI solution

Building an operational practice around AI applications is the final stage. This includes partnering with other startup departments like Legal and Security to ensure compliance with regulatory policies. Before launching, build plans around delivery, incident handling, and rollback to prevent user harm.

## Tools

Developing Responsible AI solutions may seem like a lot of work, but it's worth the effort. As Generative AI grows, more tools will help developers efficiently integrate responsibility into workflows. For example, [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) can detect harmful content and images via an API request.

## Knowledge check

What should you care about to ensure responsible AI usage?

1. That the answer is correct.
2. Harmful usage, ensuring AI isn't used for criminal purposes.
3. Ensuring AI is free from bias and discrimination.

A: 2 and 3 are correct. Responsible AI helps you consider how to mitigate harmful effects and biases and more.

## 🚀 Challenge

Read up on [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) and see what you can adopt for your usage.

## Great Work, Continue Your Learning

After completing this lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue enhancing your Generative AI knowledge!

Proceed to Lesson 4 to explore [Prompt Engineering Fundamentals](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

Certainly! Here is the translation:

**Disclaimer**:  
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.