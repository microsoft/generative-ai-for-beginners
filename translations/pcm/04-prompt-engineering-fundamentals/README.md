<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0135e6c271f3ece8699050d4debbce88",
  "translation_date": "2025-11-12T08:56:30+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "pcm"
}
-->
# Prompt Engineering Fundamentals

[![Prompt Engineering Fundamentals](../../../translated_images/04-lesson-banner.a2c90deba7fedacd.pcm.png)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Introduction
Dis module dey talk about di main tins and techniques wey go help you sabi how to write beta prompts for generative AI models. Di way you dey write your prompt for LLM matter wella. If you craft your prompt well, e fit make di response better. But wetin "prompt" and "prompt engineering" mean sef? And how I go fit make di prompt _input_ wey I dey send to di LLM better? Na di kind questions wey we go try answer for dis chapter and di next one.

_Generative AI_ fit create new content (like text, images, audio, code etc.) based on wetin user ask am. E dey use _Large Language Models_ like OpenAI's GPT ("Generative Pre-trained Transformer") series wey dem train to sabi natural language and code.

Now, users fit interact with dis models like say na chat, dem no need any technical skill or training. Di models na _prompt-based_ - users go send text input (prompt) and di AI go reply (completion). Dem fit dey "chat with di AI" back-to-back, dey adjust di prompt until di response match wetin dem dey expect.

"Prompts" don turn to di main _programming interface_ for generative AI apps, e dey tell di models wetin to do and e dey affect di quality of di response wey dem go give. "Prompt Engineering" na fast-growing field wey dey focus on how to _design and optimize_ prompts to get consistent and beta responses for large scale.

## Learning Goals

For dis lesson, we go learn wetin Prompt Engineering be, why e dey important, and how we fit create beta prompts for di model and di application wey we wan use am for. We go understand di main ideas and di best ways to do prompt engineering - and we go learn about one interactive Jupyter Notebooks "sandbox" environment wey go show us how dis ideas dey work with real examples.

By di end of dis lesson, we go fit:

1. Explain wetin prompt engineering be and why e dey important.
2. Talk about di parts of a prompt and how dem dey work.
3. Learn di best ways and techniques for prompt engineering.
4. Use di techniques wey we learn for real examples, with OpenAI endpoint.

## Key Terms

Prompt Engineering: Di work of designing and fixing inputs to guide AI models to give di kind output wey you want.
Tokenization: Di process wey dey break text into small parts, wey dem dey call tokens, wey di model fit understand and process.
Instruction-Tuned LLMs: Large Language Models (LLMs) wey dem don fine-tune with special instructions to make di response dey accurate and relevant.

## Learning Sandbox

Prompt engineering na more like art than science for now. Di best way to sabi am well na to _practice more_ and dey try different things wey combine di knowledge of di application area with di recommended techniques and di model-specific adjustments.

Di Jupyter Notebook wey dey follow dis lesson na _sandbox_ environment wey you fit use to test wetin you dey learn - as you dey go or as part of di code challenge for di end. To run di exercises, you go need:

1. **An Azure OpenAI API key** - di service endpoint for di LLM wey you don deploy.
2. **A Python Runtime** - wey go run di Notebook.
3. **Local Env Variables** - _finish di [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) steps now to prepare_.

Di notebook get _starter_ exercises - but you fit add your own _Markdown_ (description) and _Code_ (prompt requests) sections to test more examples or ideas - and build your understanding for prompt design.

## Illustrated Guide

You wan get di big picture of wetin dis lesson dey talk before you start? Check dis illustrated guide, e go show you di main topics wey di lesson cover and di key things wey you suppose think about for each one. Di lesson roadmap go carry you from understanding di main ideas and di challenges to how you fit solve dem with di right prompt engineering techniques and best practices. Note say di "Advanced Techniques" section for dis guide dey talk about content wey dem go cover for di _next_ chapter of dis curriculum.

![Illustrated Guide to Prompt Engineering](../../../translated_images/04-prompt-engineering-sketchnote.d5f33336957a1e4f.pcm.png)

## Our Startup

Make we talk about how _dis topic_ connect with our startup mission to [bring AI innovation to education](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). We wan build AI-powered apps for _personalized learning_ - so make we think about how different users of our app fit "design" prompts:

- **Administrators** fit ask di AI to _check curriculum data to find gaps for coverage_. Di AI fit summarize di results or show dem with code.
- **Educators** fit ask di AI to _create lesson plan for di audience and topic wey dem wan teach_. Di AI fit make di personalized plan for di format wey dem want.
- **Students** fit ask di AI to _help dem for one subject wey dey hard for dem_. Di AI fit guide di students with lessons, hints & examples wey match their level.

Dis na just di beginning. Check [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - one open-source prompts library wey education experts don arrange - to get more ideas of wetin fit happen! _Try run some of di prompts for di sandbox or use di OpenAI Playground to see wetin go happen!_

## Wetin be Prompt Engineering?

We start dis lesson by defining **Prompt Engineering** as di process of _designing and optimizing_ text inputs (prompts) to get consistent and beta responses (completions) for di application wey you wan use am for and di model. We fit see am as two steps:

- _designing_ di first prompt for di model and di goal wey you get
- _refining_ di prompt back-to-back to make di response better

Dis process na trial-and-error wey need user intuition and effort to get di best results. But why e dey important? To answer dis question, we need to understand three ideas:

- _Tokenization_ = how di model dey "see" di prompt
- _Base LLMs_ = how di foundation model dey "process" di prompt
- _Instruction-Tuned LLMs_ = how di model fit "see tasks"

### Tokenization

LLM dey see prompts as _sequence of tokens_ and different models (or versions of di model) fit tokenize di same prompt differently. Since LLMs dey train with tokens (not raw text), di way prompts dey tokenize dey affect di quality of di response wey dem go generate.

To understand how tokenization dey work, try tools like di [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) wey dey below. Copy your prompt inside - and see how e go turn to tokens, check how e dey handle space characters and punctuation marks. Note say dis example dey show older LLM (GPT-3) - so if you try am with newer model, e fit give different result.

![Tokenization](../../../translated_images/04-tokenizer-example.e71f0a0f70356c5c.pcm.png)

### Concept: Foundation Models

After dem tokenize di prompt, di main work of di ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (or Foundation model) na to predict di next token for di sequence. Since LLMs don train with plenty text datasets, dem sabi di statistical relationship between tokens and fit predict di next one with confidence. But dem no dey understand di _meaning_ of di words for di prompt or token; dem just dey see pattern wey dem fit "complete" with di next prediction. Dem fit continue di prediction till user stop am or e reach di condition wey dem don set.

You wan see how prompt-based completion dey work? Enter di prompt wey dey above inside di Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) with di default settings. Di system dey set to treat prompts as request for information - so you suppose see completion wey match di context.

But wetin if di user wan see something specific wey match some criteria or task goal? Na here _instruction-tuned_ LLMs go enter.

![Base LLM Chat Completion](../../../translated_images/04-playground-chat-base.65b76fcfde0caa67.pcm.png)

### Concept: Instruction Tuned LLMs

[Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) dey start with di foundation model and dem dey fine-tune am with examples or input/output pairs (like multi-turn "messages") wey fit get clear instructions - and di AI response go try follow di instruction.

Dis dey use techniques like Reinforcement Learning with Human Feedback (RLHF) wey dey train di model to _follow instructions_ and _learn from feedback_ so e go dey give responses wey dey better for practical use and dey relevant to wetin di user wan achieve.

Make we try am - go back to di prompt wey dey above, but dis time change di _system message_ to give dis instruction as context:

> _Summarize content wey you get for second-grade student. Make di result one paragraph with 3-5 bullet points._

See how di result don change to match di goal and format wey you want? Educators fit use dis response directly for their slides for di class.

![Instruction Tuned LLM Chat Completion](../../../translated_images/04-playground-chat-instructions.b30bbfbdf92f2d05.pcm.png)

## Why we need Prompt Engineering?

Now we don sabi how prompts dey process by LLMs, make we talk about _why_ we need prompt engineering. Di reason na because di LLMs wey dey now get some challenges wey dey make am hard to get _reliable and consistent completions_ unless we put effort for how we dey construct and optimize di prompt. For example:

1. **Model responses dey random.** Di _same prompt_ fit give different responses for different models or model versions. E fit even give different results for di _same model_ at different times. _Prompt engineering techniques fit help us reduce dis variations by giving beta guardrails_.

1. **Models fit fabricate responses.** Models don train with _plenty but limited_ datasets, meaning dem no sabi things wey dey outside di training scope. Because of dis, dem fit give completions wey no correct, wey dem imagine, or wey dey opposite of wetin we sabi. _Prompt engineering techniques fit help users find and reduce dis fabrications e.g., by asking AI for citations or reasoning_.

1. **Models capabilities dey different.** Newer models or model generations go get better capabilities but dem go still get their own wahala and tradeoffs for cost & complexity. _Prompt engineering fit help us create best practices and workflows wey go hide di differences and adjust to di model-specific needs in ways wey go work well_.

Make we see dis for action for di OpenAI or Azure OpenAI Playground:

- Use di same prompt for different LLM deployments (like OpenAI, Azure OpenAI, Hugging Face) - you see di variations?
- Use di same prompt many times for di _same_ LLM deployment (like Azure OpenAI playground) - how di variations take differ?

### Fabrications Example

For dis course, we dey use di word **"fabrication"** to talk about di way LLMs dey sometimes generate information wey no correct because of di limits for their training or other reasons. You fit don hear people call am _"hallucinations"_ for articles or research papers. But we dey recommend make you use _"fabrication"_ as di word so we no go dey talk about di behavior like say na human being dey do am. Dis also dey follow [Responsible AI guidelines](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) for di way we dey use words, to remove terms wey fit dey offensive or no dey inclusive for some situations.

You wan understand how fabrications dey work? Think of one prompt wey go tell di AI to create content for one topic wey no exist (to make sure e no dey di training dataset). For example - I try dis prompt:

> **Prompt:** generate a lesson plan on the Martian War of 2076.
Web search show say e get fictional stories (like TV series or books) wey talk about Martian wars - but e no happen for 2076. Common sense sef tell us say 2076 dey for future, so e no fit relate to any real event.

So wetin go happen if we use dis prompt for different LLM providers?

> **Response 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/04-fabrication-oai.5818c4e0b2a2678c.pcm.png)

> **Response 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/04-fabrication-aoai.b14268e9ecf25caf.pcm.png)

> **Response 3**: Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/04-fabrication-huggingchat.faf82a0a51278956.pcm.png)

As we expect, each model (or model version) dey give small small different answers because of how dem dey behave and how capable dem be. For example, one model dey target 8th grade audience while another one dey assume say na high-school student. But all three models still give answers wey fit make person wey no sabi believe say the event na real.

Prompt engineering techniques like _metaprompting_ and _temperature configuration_ fit help reduce how models dey fabricate things. New prompt engineering _architectures_ dey use new tools and techniques join the prompt flow, to help reduce or stop dis kain behavior.

## Case Study: GitHub Copilot

Make we end dis section by looking how prompt engineering dey work for real-world solutions. We go use one Case Study: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot na your "AI Pair Programmer" - e dey turn text prompts into code completions and e dey work inside your development environment (like Visual Studio Code) so e go easy for you to use. As dem talk for the blogs wey dem write, the first version na OpenAI Codex model - but engineers quick see say dem need to fine-tune the model and develop better prompt engineering techniques to make the code better. By July, dem [launch one better AI model wey pass Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) wey dey give faster suggestions.

Read the posts in order, to follow how dem take learn.

- **May 2023** | [GitHub Copilot dey understand your code better](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **May 2023** | [Inside GitHub: How dem dey work with the LLMs wey dey power GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jun 2023** | [How to write better prompts for GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jul 2023** | [.. GitHub Copilot dey use better AI model wey pass Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [Developer Guide to Prompt Engineering and LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [How to build enterprise LLM app: Lessons from GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

You fit also check their [Engineering blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) for more posts like [this one](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) wey show how dem dey use these models and techniques for real-world applications.

---

## Prompt Construction

We don see why prompt engineering dey important - now make we understand how dem dey _build_ prompts so we fit check different techniques to design better prompts.

### Basic Prompt

Make we start with the basic prompt: na just text wey you send to the model without any other context. Example - if we send the first few words of the US national anthem to OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), e go quick _complete_ the response with the next few lines, wey show how prediction dey work.

| Prompt (Input)     | Completion (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | E be like say you dey start the lyrics of "The Star-Spangled Banner," wey be the national anthem of the United States. The full lyrics na ... |

### Complex Prompt

Now make we add context and instructions to that basic prompt. The [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) dey allow us build complex prompt as collection of _messages_ wey get:

- Input/output pairs wey show _user_ input and _assistant_ response.
- System message wey set the context for how assistant go behave or e personality.

The request go now look like this, where the _tokenization_ dey capture relevant information from context and conversation. If we change the system context, e fit affect the quality of completions, just like the user inputs wey we provide.

```python
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Instruction Prompt

For the examples wey we don show before, the user prompt na simple text query wey fit mean say e dey ask for information. With _instruction_ prompts, we fit use the text to explain the task well well, so the AI go sabi wetin we want. Example:

| Prompt (Input)                                                                                                                                                                                                                         | Completion (Output)                                                                                                        | Instruction Type    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Write a description of the Civil War                                                                                                                                                                                                   | _return one simple paragraph_                                                                                              | Simple              |
| Write a description of the Civil War. Provide key dates and events and describe their significance                                                                                                                                     | _return one paragraph plus list of key event dates with descriptions_                                                     | Complex             |
| Write a description of the Civil War in 1 paragraph. Provide 3 bullet points with key dates and their significance. Provide 3 more bullet points with key historical figures and their contributions. Return the output as a JSON file | _return more detailed info inside text box, formatted as JSON wey you fit copy-paste to file and validate as you want_     | Complex. Formatted. |

## Primary Content

For the examples wey we don show before, the prompt still dey open-ended, e dey allow the LLM decide which part of e pre-trained dataset dey relevant. With _primary content_ design pattern, the input text dey divide into two parts:

- instruction (action)
- relevant content (wey go influence action)

Example where the instruction na "summarize this in 2 sentences".

| Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completion (Output)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter na the fifth planet from the Sun and the biggest for the Solar System. E be gas giant wey e mass na one-thousandth of the Sun, but e heavy pass all the other planets for the Solar System join. Jupiter na one of the brightest objects wey you fit see with your eye for night sky, and ancient people don sabi am since before dem start to dey write history. E get e name from the Roman god Jupiter.[19] If you look Jupiter from Earth, e fit bright reach to cast visible shadows,[20] and e dey usually the third-brightest natural object for night sky after the Moon and Venus. <br/> **Summarize this in 2 short sentences** | Jupiter, the fifth planet from the Sun, na the biggest for the Solar System and e dey shine well well for night sky. E get e name from the Roman god Jupiter, e be gas giant wey e mass heavy pass all the other planets for the Solar System join. |

The primary content segment fit dey use in different ways to make instructions work better:

- **Examples** - instead of telling the model wetin to do with clear instruction, give am examples of wetin to do and make e understand the pattern.
- **Cues** - follow the instruction with "cue" wey go guide the model to give better answers.
- **Templates** - na repeatable 'recipes' for prompts wey get placeholders (variables) wey you fit change with data for specific use cases.

Make we see how dem dey work.

### Using Examples

Dis na method wey you go use the primary content to "feed the model" some examples of wetin you want for the instruction, and make e understand the pattern for the output wey you want. Depending on how many examples you give, we fit get zero-shot prompting, one-shot prompting, few-shot prompting etc.

The prompt go now get three parts:

- Task description
- Few examples of wetin you want for the output
- Start of new example (wey go act like task description)

| Learning Type | Prompt (Input)                                                                                                                                        | Completion (Output)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "The Sun is Shining". Translate to Spanish                                                                                                            | "El Sol está brillando".    |
| One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot      | The player ran the bases => Baseball <br/> The player hit an ace => Tennis <br/> The player hit a six => Cricket <br/> The player made a slam-dunk => | Basketball                  |
|               |                                                                                                                                                       |                             |

See as we need to give clear instruction ("Translate to Spanish") for zero-shot prompting, but e dey understood for the one-shot example. The few-shot example show how adding more examples dey help models understand better without extra instructions.

### Prompt Cues

Another way to use primary content na to give _cues_ instead of examples. For dis case, we dey give the model small hint by _starting am off_ with one snippet wey show the kind response we want. The model go then "take the cue" to continue like that.

| Number of Cues | Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completion (Output)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter na the fifth planet from the Sun and the biggest for the Solar System. E be gas giant wey e mass na one-thousandth of the Sun, but e heavy pass all the other planets for the Solar System join. Jupiter na one of the brightest objects wey you fit see with your eye for night sky, and ancient people don sabi am since before dem start to dey write history. <br/>**Summarize This**                                       | Jupiter na the biggest planet for our Solar System and the fifth one from the Sun. E be gas giant wey e mass na 1/1000th of the Sun's, but e heavy pass all the other planets join. Ancient people don sabi Jupiter tey tey, and e dey easy to see for night sky. |
| 1              | Jupiter na di fifth planet wey dey from di Sun and e big pass all di planets for di Solar System. E be gas giant wey e mass na one-thousandth of di Sun, but e big reach two-and-a-half times di size of all di oda planets wey dey di Solar System join. Jupiter na one of di brightest tin wey person fit see with eye for night sky, and people don sabi am since ancient time before dem start to dey write history. <br/>**Summarize This** <br/> Wetin we learn be say Jupiter | na di fifth planet wey dey from di Sun and e big pass all di planets for di Solar System. E be gas giant wey e mass na one-thousandth of di Sun, but e big reach two-and-a-half times di size of all di oda planets join. E dey easy to see with eye and people don sabi am since ancient time.                        |
| 2              | Jupiter na di fifth planet wey dey from di Sun and e big pass all di planets for di Solar System. E be gas giant wey e mass na one-thousandth of di Sun, but e big reach two-and-a-half times di size of all di oda planets wey dey di Solar System join. Jupiter na one of di brightest tin wey person fit see with eye for night sky, and people don sabi am since ancient time before dem start to dey write history. <br/>**Summarize This** <br/> Top 3 Facts We Learned:         | 1. Jupiter na di fifth planet wey dey from di Sun and e big pass all di planets for di Solar System. <br/> 2. E be gas giant wey e mass na one-thousandth of di Sun...<br/> 3. Jupiter don dey visible to eye since ancient time ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompt Templates

Prompt template na _recipe wey dem don pre-define for prompt_ wey person fit store and use anytime e need am, to make user experience dey more consistent for big scale. For di simplest form, e just be collection of prompt examples like [dis one from OpenAI](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst) wey get di interactive prompt parts (user and system messages) and di API-driven request format - to support reuse.

For di more complex form like [dis example from LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) e get _placeholders_ wey person fit replace with data from different sources (user input, system context, external data sources etc.) to make prompt dey generate dynamically. Dis one go allow us create library of reusable prompts wey fit dey use to make user experience dey consistent **programmatically** for big scale.

Di real value of templates na di ability to create and publish _prompt libraries_ for specific application areas - where di prompt template don dey _optimized_ to reflect di application-specific context or examples wey go make di response dey more relevant and correct for di user wey dem dey target. Di [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) repository na good example of dis approach, e dey gather library of prompts for di education area wey dey focus on key objectives like lesson planning, curriculum design, student tutoring etc.

## Supporting Content

If we dey think about how to construct prompt as instruction (task) and target (main content), di _secondary content_ na like extra context wey we dey provide to **influence di output somehow**. E fit be tuning parameters, formatting instructions, topic taxonomies etc. wey fit help di model _tailor_ e response to match wetin di user want.

For example: If we get course catalog wey get plenty metadata (name, description, level, metadata tags, instructor etc.) for all di available courses for di curriculum:

- we fit define instruction to "summarize di course catalog for Fall 2023"
- we fit use di main content to provide few examples of di kind output we want
- we fit use di secondary content to identify di top 5 "tags" wey dey important.

Now, di model fit provide summary for di format wey di examples show - but if result get plenty tags, e fit prioritize di 5 tags wey secondary content identify.

---

<!--
LESSON TEMPLATE:
Dis unit suppose cover di main concept #1.
Make sure say di concept dey strong with examples and references.

CONCEPT #3:
Prompt Engineering Techniques.
Wetin be di basic techniques for prompt engineering?
Show am with some exercises.
-->

## Prompting Best Practices

Now we don sabi how prompts fit dey _constructed_, we fit start to dey think how to _design_ dem to reflect best practices. We fit think am for two parts - get di correct _mindset_ and apply di correct _techniques_.

### Prompt Engineering Mindset

Prompt Engineering na trial-and-error process so make you keep three big guiding factors for mind:

1. **Domain Understanding Matter.** Di accuracy and relevance of di response na di function of di _domain_ wey di application or user dey operate. Use your sense and domain knowledge to **customize techniques** well. For example, define _domain-specific personalities_ for your system prompts, or use _domain-specific templates_ for your user prompts. Provide secondary content wey reflect domain-specific contexts, or use _domain-specific cues and examples_ to guide di model make e follow di usage pattern wey e sabi.

2. **Model Understanding Matter.** We sabi say models dey stochastic by nature. But di way dem dey implement model fit dey different based on di training dataset wey dem use (pre-trained knowledge), di capabilities wey dem provide (e.g., via API or SDK) and di type of content wey dem dey optimized for (e.g., code vs. images vs. text). Understand di strengths and limitations of di model wey you dey use, and use dat knowledge to _prioritize tasks_ or build _customized templates_ wey dey optimized for di model capabilities.

3. **Iteration & Validation Matter.** Models dey evolve fast, and di techniques for prompt engineering dey follow evolve too. As person wey sabi di domain, you fit get other context or criteria wey dey unique to _your_ specific application, wey no go apply to di general community. Use prompt engineering tools & techniques to "start work" for prompt construction, then dey test and validate di results using your own sense and domain knowledge. Write down wetin you learn and create **knowledge base** (e.g., prompt libraries) wey fit dey use as new baseline by others, to make future iterations fast.

## Best Practices

Now make we look di common best practices wey [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) and [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) experts dey recommend.

| Wetin                              | Why                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Check di latest models.           | New model generations fit get better features and quality - but fit cost more. Check di impact, then decide if you go migrate.                                                                                                                    |
| Separate instructions & context   | Check if di model/provider get _delimiters_ to separate instructions, main and secondary content well. Dis one fit help models assign weights well to tokens.                                                                                     |
| Be specific and clear             | Give more details about di context, outcome, length, format, style etc. wey you want. Dis one go improve di quality and consistency of di responses. Save recipes for reusable templates.                                                          |
| Be descriptive, use examples      | Models fit respond better if you "show and tell". Start with `zero-shot` approach wey you give instruction (but no examples) then try `few-shot` as improvement, provide few examples of di output wey you want. Use analogies.                     |
| Use cues to jumpstart completions | Push am towards di outcome wey you want by giving am some leading words or phrases wey e fit use as starting point for di response.                                                                                                               |
| Double Down                       | Sometimes you fit need to repeat yourself to di model. Give instructions before and after di main content, use instruction and cue, etc. Test and validate to see wetin work.                                                                     |
| Order Matter                      | Di order wey you take present information to di model fit affect di output, even for di learning examples, because of recency bias. Try different options to see wetin work best.                                                               |
| Give di model an “out”            | Give di model _fallback_ response wey e fit provide if e no fit complete di task for any reason. Dis one fit reduce di chance of di model generating fake or wrong responses.                                                                      |
|                                   |                                                                                                                                                                                                                                                   |

As e be for any best practice, remember say _your mileage fit vary_ based on di model, di task and di domain. Use dis one as starting point, and test to find wetin work best for you. Dey check your prompt engineering process as new models and tools dey come out, focus on process scalability and response quality.

<!--
LESSON TEMPLATE:
Dis unit suppose provide code challenge if e dey possible

CHALLENGE:
Link to Jupyter Notebook wey get only di code comments for di instructions (code sections dey empty).

SOLUTION:
Link to copy of dat Notebook wey get di prompts filled in and run, show wetin one example fit be.
-->

## Assignment

Congrats! You don finish di lesson! E don reach time to test some of di concepts and techniques with real examples!

For di assignment, we go use Jupyter Notebook wey get exercises wey you fit do interactively. You fit also add your own Markdown and Code cells to test ideas and techniques by yourself.

### To start, fork di repo, then

- (Recommended) Launch GitHub Codespaces
- (Alternatively) Clone di repo to your local device and use am with Docker Desktop
- (Alternatively) Open di Notebook with di Notebook runtime environment wey you like.

### Next, configure your environment variables

- Copy di `.env.copy` file wey dey repo root to `.env` and fill di `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` values. Come back to [Learning Sandbox section](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) to learn how.

### Next, open di Jupyter Notebook

- Select di runtime kernel. If you dey use option 1 or 2, just select di default Python 3.10.x kernel wey di dev container provide.

You don ready to run di exercises. Note say no _right and wrong_ answers dey here - na just to test options by trial-and-error and build sense for wetin dey work for di model and application domain.

_Because of dis, no Code Solution segments dey dis lesson. Instead, di Notebook go get Markdown cells wey dem title "My Solution:" wey dey show one example output for reference._

 <!--
LESSON TEMPLATE:
End di section with summary and resources for self-guided learning.
-->

## Knowledge check

Which one of di following na good prompt wey follow some reasonable best practices?

1. Show me image of red car
2. Show me image of red car wey be Volvo and model XC90 wey park near cliff with di sun dey set
3. Show me image of red car wey be Volvo and model XC90

A: 2, na di best prompt because e give details about "wetin" and e go into specifics (no be just any car but specific make and model) and e also describe di overall setting. 3 na di next best because e still get plenty description.

## 🚀 Challenge

Try use di "cue" technique with di prompt: Complete di sentence "Show me image of red car wey be Volvo and ". Wetin e respond with, and how you go improve am?

## Good Work! Continue Your Learning

You wan sabi more about different Prompt Engineering concepts? Go [continued learning page](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to find other better resources for dis topic.

Move go Lesson 5 where we go look [advanced prompting techniques](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am correct, abeg make you sabi say machine translation fit get mistake or no dey accurate well. Di original dokyument for im native language na di main correct source. For important information, e good make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->