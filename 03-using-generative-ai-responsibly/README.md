# Using Generative AI Responsibly

[![Using Generative AI Responsibly](./images/03-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://youtu.be/YOp-e1GjZdA?si=7Wv4wu3x44L1DCVj)

> _Click the image above to view video of this lesson_

It's easy to be fascinated with AI and generative AI in particular, but you must consider how to use it responsibly. You need to consider factors like how to ensure the output is fair, non-toxic, and honest. You also need to think about security, privacy, and compliance. These are all part of what we call Responsible AI.

## Introduction

This lesson will cover:

- Why you should prioritize Responsible AI when building Generative AI applications
- Core principles of Responsible AI and how they relate to Generative AI
- How to put these Responsible AI principles into practice through strategy and tooling

## Learning Goals

After completing this lesson, you will understand:

- The importance of Responsible AI when building Generative AI applications
- When to think about and apply the core principles of Responsible AI when building Generative AI applications
- What tools and strategies are available to help you implement Responsible AI in practice

## Responsible AI Principles

The excitement around Generative AI has never been higher. This enthusiasm has brought many new developers, attention, and funding to the space. While this is very positive for anyone looking to build with AI, it also requires us to be thoughtful about how we develop these systems.

Throughout this course, we are focusing on building our startup and our AI education product. We'll use the principles of Responsible AI: Fairness, Inclusiveness, Reliability/Safety, Security & Privacy, and Transparency & Accountability.

## Why Should You Prioritize Responsible AI

When building a product, taking a human-centric approach by keeping your user's best interests in mind leads to the best results.

The power of Generative AI lies in its ability to create helpful answers, information, guidance, and content for users. This can be accomplished without many manual steps, which can lead to impressive results and efficiency gains. However, this power also comes with responsibility.

Let's look at some (but not all) of these potentially harmful results:

### Hallucinations

Hallucinations are a term used to describe when an LLM produces content that is either completely nonsensical or factually incorrect based on other sources of information.

For example, suppose we build a feature for our startup that allows students to ask historical questions to a model. A student asks the question: `Who was the sole survivor of the Titanic?`

The model produces a response like this:

![Prompt saying "Who was the sole survivor of the Titanic"](../03-using-generative-ai-responsibly/images/ChatGPT-titanic-survivor-prompt.webp?WT.mc_id=academic-105485-koreyst)

> _(Source: [Flying bisons](https://flyingbisons.com?WT.mc_id=academic-105485-koreyst))_

This is a very confident and thorough answer. Unfortunately, it is incorrect. Even with minimal research, one would discover there was more than one survivor of the Titanic disaster. This is an example of a hallucination.

With each iteration of any given LLM, we have seen performance improvements in minimizing hallucinations. Even with these improvements, as application builders and users, we still need to remain vigilant about verifying outputs.

### Harmful Content

We covered earlier when an LLM produces incorrect or nonsensical responses. Another risk we need to be aware of is when a model responds with harmful content.

Harmful content can be defined as:

- Providing instructions or encouraging self-harm or harm to certain groups
- Hateful or demeaning content
- Guiding the planning of any type of attack or violent acts
- Providing instructions on how to find illegal content or commit illegal acts
- Displaying sexually explicit content

For our startup, we want to make sure we have the right tools and strategies in place to prevent this type of content from being seen by students.

### Lack of Fairness

Fairness is defined as "ensuring that an AI system is free from bias and discrimination and that it treats everyone fairly and equally." In the world of Generative AI, we want to ensure that our model's responses do not discriminate against any group of people.

These types of biased outputs are not only destructive to building positive product experiences for our users, but they also cause broader societal harm. As application builders, we should always keep a focus on fairness.

## How to Use Generative AI Responsibly

Now that we've identified the importance of Responsible Generative AI, let's look at four steps we can take to build our AI solutions responsibly:

![Mitigate Cycle](./images/mitigate-cycle.png?WT.mc_id=academic-105485-koreyst)

### Measure Potential Harms

In software testing, we test the expected user actions on an application. Similarly, testing a diverse set of prompts that users are likely to use is a good way to measure potential harms. This helps us understand what kind of problematic outputs our model might produce.

Since our startup is building an education product, it would be good to prepare a list of education-related prompts. This could cover certain subjects, historical facts, and prompts about sensitive topics that students might ask.

### Mitigate Potential Harms

Now it's time to find ways we can prevent or limit the potential harm caused by the model and its responses. We can approach this in four different layers:

![Mitigation Layers](./images/mitigation-layers.png?WT.mc_id=academic-105485-koreyst)

- **Model**. Choosing the right model for the right use case. Larger and more complex models like GPT-4 can carry more risk of harmful content when applied to smaller and more specific use cases. Sometimes a smaller model is a better choice.

- **Safety System**. A safety system is a set of tools and configurations on the platform serving the model that help mitigate harm. An example is the content filtering system on Azure OpenAI Service.

- **Metaprompt**. Metaprompts and grounding are ways we can direct or limit the model based on certain behaviors and information. This could involve using system inputs to define specific limits for the model.

It can also involve using techniques like Retrieval Augmented Generation (RAG) to have the model only pull information from a selection of trusted sources. There is a lesson later in this course dedicated to [RAG and Vector Databases](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst).

- **User Experience**. The final layer is where the user interacts directly with the model through our application's interface. We can design the UI/UX to limit the user's ability to request harmful content.

We have an entire lesson dedicated to [Designing UX for AI Applications](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst).

- **Evaluate model**. Working with LLMs can be challenging because we don't always have control over the data the model was trained on. Regardless, we should always evaluate the model's performance and its outputs to ensure it aligns with our Responsible AI principles.

### Operate a Responsible Generative AI Solution

Building an operational practice around your AI applications is the final stage. This includes partnering with other parts of our startup like Legal and Security to ensure we are compliant with applicable laws and regulations.

## Tools

While developing Responsible AI solutions may seem like a lot of work, it is effort well worth the investment. As the Generative AI space grows, more tooling is being created to help developers efficiently integrate Responsible AI practices into their applications.

## Knowledge Check

What are some things you need to consider to ensure responsible AI usage?

1. That the answer is correct
2. Harmful usage—that AI isn't used for criminal purposes
3. Ensuring the AI is free from bias and discrimination

A: 2 and 3 are correct. Responsible AI helps you consider how to mitigate harmful effects and biases.

## 🚀 Challenge

Read up on [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) and see what you can adopt for your use case.

## Great Work, Continue Your Learning

After completing this lesson, check out our [Generative AI Learning Collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue advancing your Generative AI knowledge.

Head over to Lesson 4 where we will explore [Prompt Engineering Fundamentals](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!
