<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b2651fb16bcfbc62b8e518751ed90fdb",
  "translation_date": "2025-11-12T09:00:13+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "pcm"
}
-->
# How to Take Advanced Steps for Prompts

[![How to Take Advanced Steps for Prompts](../../../translated_images/05-lesson-banner.522610fd4a2cd82dbed66bb7e6fe104ed6da172e085dbb4d9100b28dc73ed435.pcm.png)](https://youtu.be/BAjzkaCdRok?si=NmUIyRf7-cDgbjtt)

Make we look back wetin we don learn for di last chapter:

> Prompt _engineering_ na di way wey we **dey guide di model make e give beta answer** by giving am beta instructions or context.

To write prompt, e get two steps: di first one na to build di prompt by giving di right context, di second one na _optimization_, wey be how to dey make di prompt beta small small.

For dis stage, we don sabi small small how to write prompt, but we need to sabi am well well. For dis chapter, you go move from just dey try different prompts to sabi why one prompt beta pass di other one. You go learn how to build prompts wey follow some simple techniques wey fit work for any LLM.

## Introduction

For dis chapter, we go talk about di following topics:

- Add more sabi for prompt engineering by using different techniques for your prompts.
- Arrange your prompts make e fit give different kain output.

## Wetin You Go Learn

After you finish dis lesson, you go fit:

- Use prompt engineering techniques wey go make di result of your prompts beta.
- Do prompting wey fit dey different or wey go dey sure.

## Prompt Engineering

Prompt engineering na di process of creating prompts wey go give di result wey you want. E no be just to write text prompt. Prompt engineering no be engineering work, e be set of techniques wey you fit use to get di result wey you want.

### Example of Prompt

Make we look one simple prompt like dis one:

> Generate 10 questions on geography.

For dis prompt, you dey actually use different prompt techniques.

Make we break am down.

- **Context**, you talk say e suppose dey about "geography".
- **Limit di output**, you talk say you no want pass 10 questions.

### Di Wahala of Simple Prompting

You fit get wetin you want or you fit no get am. You go get di questions wey dem generate, but geography na big topic and you fit no get wetin you dey find because of di following reasons:

- **Big topic**, you no sabi if e go dey about countries, capitals, rivers and so on.
- **Format**, wetin go happen if you want make di questions dey arranged in one kain way?

As you fit see, e get plenty things to think about when you dey create prompts.

So far, we don see one simple prompt example, but generative AI fit do plenty things to help people for different work and industries. Make we look some simple techniques next.

### Techniques for Prompting

First, we need to sabi say prompting na _emergent_ property of LLM, e mean say e no be feature wey dem build inside di model but na something wey we dey discover as we dey use di model.

E get some simple techniques wey we fit use to prompt LLM. Make we look dem.

- **Zero-shot prompting**, na di most simple way to prompt. E be one prompt wey dey ask di LLM to give answer based on wetin e don learn before.
- **Few-shot prompting**, dis kain prompting dey guide di LLM by giving am 1 or more examples wey e fit use to generate di answer.
- **Chain-of-thought**, dis kain prompting dey tell di LLM how to break problem into steps.
- **Generated knowledge**, to make di answer beta, you fit add generated facts or knowledge join di prompt.
- **Least to most**, like chain-of-thought, dis technique na to break problem into steps and then ask di steps to dey follow one by one.
- **Self-refine**, dis technique na to check di LLM answer and then ask am to make am beta.
- **Maieutic prompting**, for here, you go make sure say di LLM answer dey correct by asking am to explain different parts of di answer. E be one type of self-refine.

### Zero-shot Prompting

Dis style of prompting dey very simple, e be just one prompt. Dis technique na wetin you go dey use as you dey start to learn about LLMs. Example:

- Prompt: "Wetin be Algebra?"
- Answer: "Algebra na one part of mathematics wey dey study mathematical symbols and di rules wey dey control how we go use di symbols."

#
As you fit see, di results no fit dey more different.

> Note say, e get more parameters wey you fit change to make di output different, like top-k, top-p, repetition penalty, length penalty and diversity penalty but all dis one no dey inside di scope of dis curriculum.

## Beta practices

E get plenty beta practices wey you fit use to get wetin you want. As you dey use prompting more and more, you go find your own style.

Apart from di techniques wey we don talk about, e get some beta practices wey you fit consider when you dey prompt LLM.

Dis na some beta practices wey you fit consider:

- **Talk di context well**. Context dey important, di more you fit talk am well like di domain, topic, etc., di better.
- Limit di output. If you want specific number of items or specific length, talk am.
- **Talk wetin you want and how you want am**. Make sure you talk both wetin you want and how you want am, example "Create a Python Web API with routes products and customers, divide am into 3 files".
- **Use templates**. Many times, you go want add data from your company join your prompts. Use templates do am. Templates fit get variables wey you go replace with di real data.
- **Spell well**. LLMs fit give you correct response, but if you spell well, you go get better response.

## Assignment

Dis na code for Python wey dey show how to build simple API with Flask:

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

Use AI assistant like GitHub Copilot or ChatGPT and use di "self-refine" technique to make di code better.

## Solution

Try solve di assignment by adding correct prompts to di code.

> [!TIP]
> Write prompt wey go ask am to make di code better, e good to limit how many improvement you want. You fit also ask am to make am better for one specific way, example architecture, performance, security, etc.

[Solution](../../../05-advanced-prompts/python/aoai-solution.py)

## Knowledge check

Why I go use chain-of-thought prompting? Show me 1 correct answer and 2 wrong answers.

1. To teach di LLM how to solve one problem.
1. B, To teach di LLM to find errors for code.
1. C, To tell di LLM to bring different solutions.

A: 1, because chain-of-thought na about showing di LLM how to solve one problem by giving am steps, and similar problems and how dem solve am.

## 🚀 Challenge

You just use di self-refine technique for di assignment. Take any program wey you don build and think about di improvements wey you go like apply to am. Now use di self-refine technique to apply di changes wey you suggest. Wetin you think about di result, e beta or e no beta?

## Great Work! Continue Your Learning

After you don finish dis lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue dey learn more about Generative AI!

Go Lesson 6 where we go use wetin we don learn about Prompt Engineering to [build text generation apps](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transle-shon service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transle-shon. Even as we dey try make am correct, abeg make you sabi say machine transle-shon fit get mistake or no dey accurate well. Di original dokyument wey dey for im native language na di one wey you go take as di correct source. For important mata, e good make professional human transle-shon dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transle-shon.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->