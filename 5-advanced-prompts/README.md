# Advanced prompts

So you've started to use an LLM tool like ChatGPT or perhaps GitHUb Copilot. You've seen the power of the tool, but you're not quite sure how to get the most out of it.

To be really efficient with AI tools you need to learn how to prompt them efficiently. Prompting is it's own thing referred to as prompt engineering. We've covered prompt engineering somewhat in previous chapters but let's go at depth in this chapter.

## Introduction

In this chapter, we will:

- Better understand prompt engineering and how this effects the outcome of your prompts.
- Apply different types of prompts and see how the outcome differs.
- Learn best practices for prompt engineering.

## Prompt engineering

Prompt engineering is the process of creating prompts that will produce the desired outcome. There's more to prompt engineering than just writing a text prompt. 

Let's take a basic prompt like this one:

> Generate 10 questions on geography.

In this prompt, you are actually applying a set of different techniques to get the desired outcome. Let's break this down.

- Context, you specify it should be about "geography".
- Limiting the output, you state you want no more than 10 questions.

You may or may not get the desired outcome. You will get your questions but geography is a big topic, you don' know if it's going to be about countries, capitals, rivers and so on. What if you wanted the questions to be formatted in a certain way? 

As you can see, there's a lot to consider when creating prompts.

So far, we've seen a simple prompt example, but generative AI is capable of much more to help people in a variety of roles and industries. Let's explore some basic techniques next.

### Techniques 

First, we need to understand that prompting is an emergent property of an LLM meaning that this is not a feature that is built into the model but rather something we discover as we use the model.

There are some basic techniques that we can use to prompt an LLM. Let's explore them.

- **Few shot prompting**, this is the most basic form of prompting. It's a single prompt with a few examples.
- **Chain-of-thought**, this type of prompting tells the LLM how to break down a problem into steps.
- **Generated knowledge**, to improve the response of a prompt, you can provide generated facts or knowledge additionally to your prompt.
- **Least to most**, like chain-of-though, this technique is about breaking down a problem in series of steps and then ask these steps to be performed in order.
- **Self-refine**, this technique is about critiquing the LLM's output and then asking it to improve.
- **Maieutic prompting**. What you want here is to ensure the LLM answer is correct and you ask it to explain various parts of the answer. This is a form of self-refine.

### Few-shot prompting. 

This style of prompting is very simple, it may consist of a single prompt and possibly a few examples. This technique is probably what you're using as you're starting to learn about LLMs. Here's an example:

- Prompt: "What is Algebra?"
- A: "Algebra is a branch of mathematics that studies mathematical symbols and the rules for manipulating these symbols."

### Chain-of-thought

Chain-of-thought is a very interesting technique as it's about taking the LLM through a series of steps. The idea is to instruct the LLM in such a way that it understands how to do something. Consider the following example, with and without chain-of-thought:

    - Prompt: "Alice has 5 apples, throws 3 apples, gives 2 to Bob and Bob gives one back, how many apples does Alice have?"
    
LLM answers with 5, which is incorrect. Correct answer is 1 apple, given the calculation (5 -3 -2 + 1 = 1). 

So how can we teach the LLM to do this correctly, let's try chain-of-thought. Apply chain-of-thought means: 

1. give the LLM a similar example. 
1. show the calculation.
1. then give the original prompt.

Here's how:

- Prompt: "Lisa has 7 apples, throws 1 apple, gives 4 apples to Bart and Bart gives one back:
  7 -1 = 6
  6 -4 = 2
  2 +1 = 3  
  Alice has 5 apples, throws 3 apples, gives 2 to Bob and Bob gives one back, how many apples does Alice have?"
  A: 1

Not how we write a substantially longer prompts with another example, a calculation and then the original prompt and we arrive at the correct answer 1.  

As you can see chain-of-thought is a very powerful technique.

### Generated knowledge

### Least to most
### Self-refine
### Maieutic prompting

## Best practices

## Templated prompts

## Embedding prompts

## Assignment

## Solution

## Knowledge check