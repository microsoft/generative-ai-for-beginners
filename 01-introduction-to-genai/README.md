# Introduction to Generative AI and Large Language Models

[![Introduction to Generative AI and Large Language Models](./images/01-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://youtu.be/lFXQkBvEe0o?si=6ZBcQTwLJJDpnX0K)

_(Click the image above to view the video for this lesson)_

Generative AI is artificial intelligence capable of generating text, images, and other types of content. What makes it such powerful technology is that it democratizes AI—anyone can use it with minimal technical knowledge. In this curriculum, we'll explore how startups can leverage generative AI to unlock new possibilities in education while addressing the social and ethical challenges that accompany this powerful technology.

## Introduction

This lesson covers:

- Introduction to the business scenario: our startup's idea and mission
- Generative AI and how we arrived at the current technological landscape
- How large language models work internally
- The main capabilities and practical use cases of large language models

## Learning Goals

After completing this lesson, you will understand:

- What generative AI is and how large language models function
- How to leverage large language models for different use cases, with a focus on education

## Scenario: Our Educational Startup

Generative AI represents the cutting edge of artificial intelligence, pushing the boundaries of what was once thought impossible. Generative AI models possess several powerful capabilities and applications. Our startup's mission is:

> _Improving accessibility to learning on a global scale, ensuring equitable access to education, and providing personalized learning experiences for every learner based on their individual needs._

Our startup team recognizes that we cannot achieve this mission without leveraging one of the most powerful technologies of our time—Large Language Models (LLMs).

Generative AI is poised to revolutionize how we learn and teach. Students will have access to virtual teachers available 24/7, providing vast amounts of information and instant feedback on assignments. Teachers will have valuable tools to create personalized lessons and assessments tailored to each student's needs.

![Five young students looking at a monitor - image by DALLE2](./images/students-by-DALLE2.png?WT.mc_id=academic-105485-koreyst)

To begin, let's define some fundamental concepts and terminology we'll use throughout this course.

## How Did We Get Generative AI?

Despite the recent hype surrounding generative AI announcements, this technology has been decades in development, with initial research efforts dating back to the 1960s. Let's trace this journey.

The earliest AI prototypes were typewritten chatbots that relied on knowledge bases extracted from domain experts and stored in computers. Responses were retrieved from predefined answers in these knowledge bases. However, this approach didn't scale well and quickly showed its limitations.

### A Statistical Approach to AI: Machine Learning

A breakthrough came during the 1990s with the application of statistical methods to text analysis. This led to new algorithms—known as machine learning—capable of learning patterns from data rather than relying on pre-programmed rules.

### Neural Networks and Modern Virtual Assistants

In recent years, advances in hardware capable of processing larger datasets and performing more complex computations fueled AI research, leading to the development of sophisticated neural networks.

Neural networks, particularly Recurrent Neural Networks (RNNs), significantly improved natural language processing by enabling more meaningful representations of text. This technology powered the virtual assistants that emerged in the 2000s—systems proficient in understanding human language, identifying user needs, and taking appropriate actions.

### Present Day: Generative AI

Today's generative AI can be viewed as a subset of deep learning.

![AI, ML, DL and Generative AI](./images/AI-diagram.png?WT.mc_id=academic-105485-koreyst)

After decades of AI research, a new model architecture called the _Transformer_ overcame the limitations of RNNs by handling much longer sequences of text as input. Transformers revolutionized natural language processing and formed the foundation for modern generative AI.

Most recent generative AI models—known as Large Language Models (LLMs) because they work with text inputs and outputs—are based on this architecture. These models are trained on vast amounts of text data, enabling them to generate coherent, contextually relevant responses.

## How Do Large Language Models Work?

Let's explore how large language models function, focusing on OpenAI's GPT (Generative Pre-trained Transformer) architecture.

- **Tokenizer (text to numbers)**: Large Language Models receive text input and generate text output. However, as statistical models, they work far better with numbers than with text sequences. A tokenizer converts text into numerical tokens—small pieces of text represented as numbers. This numerical representation allows the model to process information mathematically.

![Example of tokenization](./images/tokenizer-example.png?WT.mc_id=academic-105485-koreyst)

- **Predicting output tokens**: Given n input tokens (with the maximum varying by model), the model predicts one output token. This token is then added to the input sequence, and the process repeats, predicting the next token based on all previous tokens. This iterative process continues until a complete response is generated.

- **Selection process using probability distribution**: The model selects the output token based on its probability of appearing after the current text sequence. Since the model predicts probabilities for all possible next tokens, we can control output diversity using a "temperature" parameter. Lower temperatures produce more predictable outputs, while higher temperatures introduce more creativity and variation.

## How Can Our Startup Leverage Large Language Models?

Now that we understand how large language models work, let's explore practical examples of common tasks they perform well, with applications for education.

The primary capability of a Large Language Model is _generating text from scratch, starting with a text input written in natural language._

But what kinds of text inputs and outputs are possible? The input to a large language model is called a **prompt**, while the output is called a **completion**—referring to the model's mechanism of generating tokens to complete the current input sequence.

Large Language Models can handle various types of prompts:

- An **instruction** specifying the desired output type. This might include examples or additional context.

  1. **Summarization** of articles, books, product reviews, and extraction of insights from unstructured data.
    
     ![Example of summarization](./images/summarization-example.png?WT.mc_id=academic-105485-koreyst)
  
  2. **Creative writing** including articles, essays, assignments, and more.
       
      ![Example of creative writing](./images/creative-writing-example.png?WT.mc_id=academic-105485-koreyst)

- A **question**, posed conversationally with the AI system.
  
  ![Example of conversation](./images/conversation-example.png?WT.mc_id=academic-105485-koreyst)

- A **text excerpt to complete**, which implicitly requests writing assistance.
  
  ![Example of text completion](./images/text-completion-example.png?WT.mc_id=academic-105485-koreyst)

- A **code snippet** with a request to explain and document it, or a comment asking the model to generate code for a specific task.
  
  ![Coding example](./images/coding-example.png?WT.mc_id=academic-105485-koreyst)

These examples, while straightforward, illustrate the potential of generative AI for education scenarios. However, it's important to understand that generative AI output isn't always perfect. Sometimes the model's creativity can work against us, producing grammatically correct but contextually nonsensical responses. This limitation—sometimes called "hallucination"—is something users should be aware of.

## Assignment

Your assignment is to read more about [generative AI](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) and identify an area where generative AI could solve a real-world problem. Consider how you might build an application to address this problem.

If you complete this task, you might be ready to apply to Microsoft's incubator, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst)!

## Knowledge Check

What's true about large language models?

1. You always get identical responses when using the same prompt
2. They perform perfectly at everything—excellent at math, producing working code, etc.
3. Responses may vary even with identical prompts. They excel at generating first drafts of text or code, but human refinement is typically needed

**Answer:** 3. An LLM is non-deterministic—responses vary depending on the temperature setting. You shouldn't expect perfect results; LLMs are best used to generate initial drafts that you then refine.

## Congratulations! Continue Your Journey

After completing this lesson, explore our [Generative AI Learning Collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue advancing your knowledge.

Next, head to Lesson 2 to [explore and compare different LLM types](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)!
