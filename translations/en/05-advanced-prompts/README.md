<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b2651fb16bcfbc62b8e518751ed90fdb",
  "translation_date": "2025-10-17T22:28:53+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "en"
}
-->
# Creating Advanced Prompts

[![Creating Advanced Prompts](../../../translated_images/05-lesson-banner.522610fd4a2cd82dbed66bb7e6fe104ed6da172e085dbb4d9100b28dc73ed435.en.png)](https://youtu.be/BAjzkaCdRok?si=NmUIyRf7-cDgbjtt)

Let's revisit some key points from the previous chapter:

> Prompt _engineering_ is the process of **guiding the model to produce more relevant responses** by providing better instructions or context.

Writing prompts involves two main steps: constructing the prompt by providing relevant context, and _optimization_, which is the process of refining the prompt for better results.

At this stage, we have a basic understanding of how to write prompts, but it's time to delve deeper. In this chapter, you'll move from experimenting with different prompts to understanding why one prompt works better than another. You'll learn how to create prompts using fundamental techniques that can be applied to any LLM.

## Introduction

In this chapter, we will explore the following topics:

- Expanding your knowledge of prompt engineering by applying various techniques to your prompts.
- Configuring your prompts to produce different types of outputs.

## Learning Goals

By the end of this lesson, you will be able to:

- Use prompt engineering techniques to improve the quality of your prompts.
- Create prompts that produce either varied or deterministic outputs.

## Prompt Engineering

Prompt engineering involves crafting prompts that yield the desired results. It's not just about writing a text prompt; it's about applying specific techniques to achieve the intended outcome.

### An Example of a Prompt

Consider this simple prompt:

> Generate 10 questions on geography.

This prompt already incorporates several prompt techniques.

Let's break it down:

- **Context**: You specify that the questions should be about "geography."
- **Limiting the output**: You request no more than 10 questions.

### Limitations of Simple Prompting

You might not always get the exact outcome you want. While the model will generate questions, geography is a broad subject, and the results might not align with your expectations due to the following reasons:

- **Broad topic**: The questions could be about countries, capitals, rivers, etc., without focusing on a specific area.
- **Format**: The questions might not be presented in the format you desire.

As you can see, there are many factors to consider when creating prompts.

So far, we've looked at a simple example, but generative AI can do much more to assist people across various roles and industries. Let's explore some fundamental techniques next.

### Techniques for Prompting

First, it's important to understand that prompting is an _emergent_ property of an LLM. This means it's not a built-in feature of the model but something we discover through usage.

Here are some basic techniques for prompting an LLM:

- **Zero-shot prompting**: The simplest form of prompting, where a single prompt requests a response based solely on the model's training data.
- **Few-shot prompting**: This technique provides one or more examples to guide the LLM in generating its response.
- **Chain-of-thought**: This technique instructs the LLM to break down a problem into steps.
- **Generated knowledge**: To enhance the response, you can include additional facts or knowledge in your prompt.
- **Least-to-most**: Similar to chain-of-thought, this technique involves breaking down a problem into smaller steps and asking the LLM to address them sequentially.
- **Self-refine**: This technique involves critiquing the LLM's output and asking it to improve.
- **Maieutic prompting**: This technique ensures the LLM's answer is correct by asking it to explain various parts of its response. It's a form of self-refinement.

### Zero-shot Prompting

This is the most straightforward style of prompting, consisting of a single prompt. It's likely the technique you're using as you begin exploring LLMs. Here's an example:

- Prompt: "What is Algebra?"
- Answer: "Algebra is a branch of mathematics that studies mathematical symbols and the rules for manipulating these symbols."

### Few-shot Prompting

Few-shot prompting helps the model by providing a few examples along with the request. It consists of a single prompt with additional task-specific examples. Here's an example:

- Prompt: "Write a poem in the style of Shakespeare. Here are a few examples of Shakespearean sonnets:
  Sonnet 18: 'Shall I compare thee to a summer's day? Thou art more lovely and more temperate...'
  Sonnet 116: 'Let me not to the marriage of true minds Admit impediments. Love is not love Which alters when it alteration finds...'
  Sonnet 132: 'Thine eyes I love, and they, as pitying me, Knowing thy heart torment me with disdain,...'
  Now, write a sonnet about the beauty of the moon."
- Answer: "U
As you can see, the results couldn't be more varied.

> Note, there are additional parameters you can adjust to vary the output, such as top-k, top-p, repetition penalty, length penalty, and diversity penalty, but these are beyond the scope of this curriculum.

## Good practices

There are many strategies you can use to achieve the desired results. As you continue to use prompting, you'll develop your own style.

In addition to the techniques we've covered, there are some best practices to keep in mind when prompting an LLM.

Here are some good practices to consider:

- **Specify context**. Context is important; the more details you can provide, such as domain, topic, etc., the better.
- Limit the output. If you need a specific number of items or a particular length, make sure to specify it.
- **Specify both what and how**. Clearly state both what you want and how you want it, for example, "Create a Python Web API with routes for products and customers, divide it into 3 files."
- **Use templates**. Often, you'll want to enhance your prompts with data specific to your company. Use templates to achieve this. Templates can include variables that you replace with actual data.
- **Spell correctly**. While LLMs may still provide a correct response, accurate spelling will yield better results.

## Assignment

Below is Python code demonstrating how to create a simple API using Flask:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run()
```

Use an AI assistant like GitHub Copilot or ChatGPT and apply the "self-refine" technique to improve the code.

## Solution

Please try to solve the assignment by adding appropriate prompts to the code.

> [!TIP]
> When asking for improvements, it's a good idea to limit the number of changes. You can also specify the type of improvement you want, such as architecture, performance, security, etc.

[Solution](../../../05-advanced-prompts/python/aoai-solution.py)

## Knowledge check

Why would I use chain-of-thought prompting? Provide 1 correct response and 2 incorrect responses.

1. To teach the LLM how to solve a problem.
1. B, To teach the LLM to find errors in code.
1. C, To instruct the LLM to come up with different solutions.

A: 1, because chain-of-thought is about showing the LLM how to solve a problem by providing it with a series of steps, along with similar problems and their solutions.

## 🚀 Challenge

You just applied the self-refine technique in the assignment. Take any program you've created and think about the improvements you'd like to make. Now use the self-refine technique to implement the proposed changes. What do you think of the result—was it better or worse?

## Great Work! Continue Your Learning

After completing this lesson, explore our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to further enhance your knowledge of Generative AI!

Proceed to Lesson 6, where we'll apply our Prompt Engineering skills to [build text generation apps](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst).

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.