# Advanced prompts

So you've started to use an LLM tool like ChatGPT or perhaps GitHUb Copilot. You've seen the power of the tool, but you're not quite sure how to get the most out of it.

To be really efficient with AI tools you need to learn how to prompt them efficiently. Prompting is it's own thing referred to as prompt engineering. We've covered prompt engineering somewhat in previous chapters but let's go at depth in this chapter.

## Introduction

- Prompt engineering.
- Best practices.
- Templated prompts.

## Learning goals

After completing this lesson, you will:

- Understand Prompt engineering and how this effects the outcome of your prompts.
- Apply different types of prompts and see how the outcome differs.
- Learn best practices for prompt engineering.

## Prompt engineering

Prompt engineering is the process of creating prompts that will produce the desired outcome. There's more to prompt engineering than just writing a text prompt. Prompt engineering is not an engineering discipline, it's more a set of techniques that you can apply to get the desired outcome.

### An example of a prompt

Let's take a basic prompt like this one:

> Generate 10 questions on geography.

In this prompt, you are actually applying a set of different prompt techniques.

Let's break this down.

- **Context**, you specify it should be about "geography".
- **Limiting the output**, you want no more than 10 questions.

### Limitations of simple prompting

You may or may not get the desired outcome. You will get your questions generated, but geography is a big topic and you may not get what you want to due the following reasons:

- **Big topic**, you don' know if it's going to be about countries, capitals, rivers and so on.
- **Format**, what if you wanted the questions to be formatted in a certain way?

As you can see, there's a lot to consider when creating prompts.

So far, we've seen a simple prompt example, but generative AI is capable of much more to help people in a variety of roles and industries. Let's explore some basic techniques next.

### Techniques for prompting

First, we need to understand that prompting is an *emergent* property of an LLM meaning that this is not a feature that is built into the model but rather something we discover as we use the model.

There are some basic techniques that we can use to prompt an LLM. Let's explore them.

- **Few shot prompting**, this is the most basic form of prompting. It's a single prompt with a few examples.
- **Chain-of-thought**, this type of prompting tells the LLM how to break down a problem into steps.
- **Generated knowledge**, to improve the response of a prompt, you can provide generated facts or knowledge additionally to your prompt.
- **Least to most**, like chain-of-though, this technique is about breaking down a problem in series of steps and then ask these steps to be performed in order.
- **Self-refine**, this technique is about critiquing the LLM's output and then asking it to improve.
- **Maieutic prompting**. What you want here is to ensure the LLM answer is correct and you ask it to explain various parts of the answer. This is a form of self-refine.

### Few-shot prompting

This style of prompting is very simple, it may consist of a single prompt and possibly a few examples. This technique is probably what you're using as you're starting to learn about LLMs. Here's an example:

- Prompt: "What is Algebra?"
- Answer: "Algebra is a branch of mathematics that studies mathematical symbols and the rules for manipulating these symbols."

### Chain-of-thought

Chain-of-thought is a very interesting technique as it's about taking the LLM through a series of steps. The idea is to instruct the LLM in such a way that it understands how to do something. Consider the following example, with and without chain-of-thought:

    - Prompt: "Alice has 5 apples, throws 3 apples, gives 2 to Bob and Bob gives one back, how many apples does Alice have?"
    - Answer: 5

LLM answers with 5, which is incorrect. Correct answer is 1 apple, given the calculation (5 -3 -2 + 1 = 1).

So how can we teach the LLM to do this correctly?

Let's try chain-of-thought. Applying chain-of-thought means: 

1. Give the LLM a similar example. 
1. Show the calculation, and how to calculate it correctly.
1. Provide the original prompt.

Here's how:

- Prompt: "Lisa has 7 apples, throws 1 apple, gives 4 apples to Bart and Bart gives one back:
  7 -1 = 6
  6 -4 = 2
  2 +1 = 3  
  Alice has 5 apples, throws 3 apples, gives 2 to Bob and Bob gives one back, how many apples does Alice have?"
  Answer: 1

Not how we write a substantially longer prompts with another example, a calculation and then the original prompt and we arrive at the correct answer 1.  

As you can see chain-of-thought is a very powerful technique.

### Generated knowledge

Many times when you want to construct a prompt, you want to do so using your own company's data. You want part of the prompt to be from the company and the other part should be the actual prompt you're interested in. 

As an example, this is what your prompt then can look like if you're in the insurance business:

```text
{{company}}: {{company_name}}
{{products}}: 
{{products_list}}
Please suggest an insurance given the following budget and requirements:
Budget: {{budget}}
Requirements: {{requirements}}
```

Above, you see how the prompt is constructed using a template. In the template there's a number of variables, denoted by `{{variable}}`, that will be replaced with actual values from a company API.

Here's an example of how the prompt could look like once the variables have been replaced: 

```text
Insurance company: ACME Insurance
Insurance products (cost per month): 
- Car, cheap, 500 USD
- Car, expensive, 1100 USD 
- Home, cheap, 600 USD
- Home, expensive, 1200 USD
- Life, cheap, 100 USD

Please suggest an insurance given the following budget and requirements:
Budget: $1000
Requirements: Car, Home
```

### Least to most

The idea with Least-to-most prompting is to break down a bigger problem into sub problems. That way, you help guide the LLM on how to "conquer" the bigger problem. A good example could be for data science where you can ask the LLM to divide up a problem like so:

> Prompt: How to perform data science in 5 steps?

With your AI assistant answering with: 

1. Collect data
1. Clean data
1. Analyze data
1. Plot data
1. Present data

### Self-refine, critique the results

With generative AIs and LLMs, you can't trust the output. You need to verify it. After all, the LLM is just presenting you what's the next most likely thing to say, not what's correct. Therefore, a good idea is to ask the LLM to critique itself, which leads us to the self-refine technique.

How it works is that you follow the following steps:

1. Initial prompt asking the LLM to solve a problem
1. LLM answers
1. You critique the answer and ask the AI to improve
1. LLM answers again, this time considering the critique and suggest solutions it came up with

You can repeat this process as many times as you want.

Here's an example using this technique:

> Prompt: "Create a Python Web API with routes products and customers"

AI Answer:

```python
import flask
app = Flask(__name__)

@app.route('/products')
def products():
    return 'Products'

@app.route('/customers')
def customers():
    return 'Customers'
```

> Prompt: suggest 3 improvements of the above code

AI Answer:

```text
Sure, here are three suggestions to improve the code:

Import the correct module: The first line should import Flask instead of flask. The correct import statement should be from flask import Flask.

Add a main function: Add a if __name__ == '__main__': block to the end of the file to run the application when the file is executed.

Use f-strings: Use f-strings to format the return statements in the route functions. For example, return 'Products' can be changed to return f'This is the {request.path} page'.
```

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/products')
def products():
    return f'This is the {request.path} page'

@app.route('/customers')
def customers():
    return f'This is the {request.path} page'

if __name__ == '__main__':
    app.run()
```

As you can see, the above AI response is improving the first suggested code thanks to critiquing the first answer.
 
### Maieutic prompting

Maieutic prompting is a technique that is similar to self-refine but it's more about asking the LLM to explain itself. The goal is to reduce inconsistencies in the LLM's output so to ensure it arrives at the correct answer. The workflow to follow is:

1. Ask the LLM to answer a question
1. For each part of the answer, ask the LLM to explain it more in depth.
1. If there are inconsistencies, discard the parts that are inconsistent.

Repeat 2 and 3 until you've gone through all the parts and you're satisfied with the answer.

Here's an example prompt:

> prompt: How can I create a crisis plan to mitigate for a pandemic in 5 steps?
LLM answer: 

```text
1. Identify the risks
1. Identify the stakeholders
1. Identify the resources
1. Identify the actions
1. Identify the communication channels
```

It's identified 5 steps, but can we determine if this is correct? Let's ask the LLM to explain each step:

> prompt: Explain the first step in more detail, what are the risks in detail with a pandemic?

```text
The risks are the following:

- Loss of life
- Loss of business
- Loss of reputation
- Loss of customers
- Loss of employees
```

At this point, we want to make sure the LLM is correct so we ask it to explain the first risk in more detail and hope it's consistent with the answer above:

> prompt: In a Pandemic, which is the biggest risk and why?

```text
The biggest risk is loss of life because it's the most important thing to protect.
```

> What are the two biggest risks in a pandemic?

```text
The two biggest risks are loss of life and loss of business.
```

At this point, the LLM is consistent and mentions "life" and "business" as top two risks. We can now continue to the next step and feel fairly confident. However, we shouldn't trust the LLM blindly, we should always verify the output.

## Good practices

There are many practices you can apply to try getting what you want. You will find your own style as you use prompting more and more. 

Additionally to the techniques we've covered, there are some good practices to consider when prompting an LLM.

Here are some good practices to consider:

- **Specify context**. Context matters, the more you can specify like domain, topic, etc. the better.
- Limit the output. If you want a specific number of items or a specific length, specify it.
- **Specify both what and how**. Remember to mention both what you want and how you want it, for example "Create a Python Web API with routes products and customers, divide it into 3 files".
- **Use templates**. Often, you will want to enrich your prompts with data from your company. Use templates to do this. Templates can have variables that you replace with actual data.
- **Spell correctly**. LLMs might provide you with a correct response, but if you spell correctly, you will get a better response.  

## Assignment

Here's code in JavaScript showing how to build a simple API using Express.js:

```javascript
const express = require('express')

const app = express()

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(3000, () => {
  console.log('Example app listening on port 3000!')
})
```

Use an AI assistant like GitHUb Copilot or ChatGPt and apply the "self-refine" technique to improve the code.

## Solution

Please attempt to solve the assignment by adding suitable prompts to the code.

> [!TIP]
> Phrase a prompt to ask it to improve, it's a good idea to limit how many improvements. You can also ask to improve it in a certain way, for example architecture, performance, security, etc. 

[Solution](./solution.js)

## Knowledge check

Why would I use chain-of-thought prompting? Show me 1 correct response and 2 incorrect responses.

- A, To teach the LLM how to solve a problem.
- B, To teach the LLM to find errors in code.
- C, To instruct the LLM to come up with different solutions.

Answer: A, because chain-of-thought is about showing the LLM how to solve a problem by providing it with a series of steps, and similar problems and how they were solved.