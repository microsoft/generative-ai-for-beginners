# Prompt Engineering Fundamentals

[![Prompt Engineering Fundamentals](../../../translated_images/pcm/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Introduction
Dis module dey cover beta mata dem and ways wey you fit take create correct prompts for generative AI models. Di way wey you write your prompt give LLM still matter. If you craft di prompt well well, e fit bring better answer. But wetin di word _prompt_ and _prompt engineering_ mean exactly? And how I fit better di prompt _input_ wey I dey send go LLM? Na dis kain question we go try answer for dis chapter and di next one.

_Generative AI_ fit create new tins (like text, images, audio, code dem) based on wetin pesin ask. E dey do dis one using _Large Language Models_ like OpenAI GPT ("Generative Pre-trained Transformer") series wey dem train for natural language and code use.

Now people fit yarn with these models using normal talk like chat, no need to be tech guru or get training. Di models dey _prompt-based_ - pesin go send text input (prompt) then e go bring AI answer (completion). Dem fit still dey "chat with AI" many times, dey change prompt till di answer sweet dem.

"Prompts" don be main _programming interface_ for generative AI apps, wey dey tell di models wetin dem gats do and fit affect how better di answer go be. "Prompt Engineering" na field wey dey grow fast wey focus on _design and optimization_ of prompts to give constant and better answers for many people.

## Learning Goals

For dis lesson, we go learn wetin Prompt Engineering be, why e important, and how we fit create better prompts for a model and application wey we want use am for. We go sabi main ideas and beta ways for prompt engineering - and we go see one Jupyter Notebooks "sandbox" place wey we fit test these things for real life examples.

By di end of dis lesson, we go fit:

1. Talk wetin prompt engineering be and why e dey important.
2. Explain di parts of prompt and how dem dey use am.
3. Learn beta ways and techniques for prompt engineering.
4. Use di techniques we learn for real examples, using OpenAI endpoint.

## Key Terms

Prompt Engineering: Di work of designing and improving inputs to guide AI models make dem give correct output.
Tokenization: Di way wey dem dey turn text into small small parts, wey model fit understand and work with.
Instruction-Tuned LLMs: Big Language Models (LLMs) wey dem don train finish with special instructions to make dem answer better and correct.

## Learning Sandbox

Prompt engineering still dey more like art pass science for this time. Beta way to improve na to _practice more_ and use trial-and-error wey join application knowledge with correct techniques and model tweaks.

Di Jupyter Notebook wey come with dis lesson dey give one _sandbox_ place wey you fit try wetin you learn - as you dey do am or as part of code challenge at di end. To run di exercise, you go need:

1. **Azure OpenAI API key** - di service link for deployed LLM.
2. **Python Runtime** - to run di Notebook.
3. **Local Env Variables** - _finish di [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) steps now make you ready_.

Di notebook get _starter_ exercises - but you fit add your own _Markdown_ (description) and _Code_ (prompt requests) parts to try more examples or ideas - and make your sense about prompt design better.

## Illustrated Guide

You wan see the full koko of wetin dis lesson go teach before you start? Look this illustrated guide, e go give you beta understanding of main topic dem and wetin you suppose keep for mind. Di lesson roadmap go carry you from to sabi di main ideas and challenges till we fix dem with correct prompt engineering ways and beta practice. Make you know say "Advanced Techniques" section for this guide na about contents wey dey di _next_ chapter inside dis course.

![Illustrated Guide to Prompt Engineering](../../../translated_images/pcm/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Our Startup

Now, make we talk how _dis topic_ dey relate to our startup mission of [bring AI innovation to education](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). We want build AI-powered apps for _personalized learning_ - so make we think how different people wey go use di app fit "design" prompts:

- **Administrators** fit ask AI to _check curriculum data find where dem never cover well_. AI fit summarize or show result with code.
- **Educators** fit ask AI to _create lesson plan for particular audience and topic_. AI fit build the correct plan for given format.
- **Students** fit ask AI to _teach dem hard subject_. AI fit direct students with lessons, hints & examples wey fit their level.

Na just small part be dat. Check [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - na open-source prompt library wey education experts arrange - to get more idea of wetin fit happen! _Try run some of dem for sandbox or OpenAI Playground make you see wetin go happen!_

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #1:
Prompt Engineering.
Define it and explain why it is needed.
-->

## Wetin be Prompt Engineering?

We start dis lesson by to define **Prompt Engineering** as di work of _designing and optimizing_ text inputs (prompts) to give constant and beta answers (completions) for one application goal and model. We fit see am like 2-step process:

- _designing_ di first prompt for one model and goal
- _refining_ di prompt many times to improve di answer quality

Dis one na trial-and-error wey need user sense and wahala to get best results. So why e important? Before we fit answer, make we first understand three tins:

- _Tokenization_ = how model dey "see" di prompt
- _Base LLMs_ = how di foundation model "process" di prompt
- _Instruction-Tuned LLMs_ = how di model fit now see "tasks"

### Tokenization

One LLM dey see prompts as _sequence of tokens_ where different models (or model versions) fit tokenize di same prompt different different ways. Since LLMs dey train with tokens (no be raw text), how dem tokenize prompt go affect how better di generated answer go be.

To sabi how tokenization take work, try tools like [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) wey dem show below. Copy your prompt come - then see how e turn tokens, watch how whitespace and punctuation dem dey handle. Note say dis one show older LLM (GPT-3) - so if you try with new model e fit be different.

![Tokenization](../../../translated_images/pcm/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Idea: Foundation Models

Once prompt don tokenize, main work for ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (or Foundation model) na to predict di next token for dat sequence. Since LLMs train for plenty text data, dem sabi well how tokens dey relate and fit predict wit confidence. But dem no understand di _meaning_ of words inside prompt or token; dem just see pattern wey dem fit "complete" with next prediction. Dem fit continue predict till user stop am or condition reach.

You want see how prompt-based completion dey work? Put di prompt up for [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) with default settings. Di system go treat prompt as request for info - so you go see completion wey match di context.

But if user want see something wey follow specific criteria or task? Na there _instruction-tuned_ LLMs enter matter.

![Base LLM Chat Completion](../../../translated_images/pcm/04-playground-chat-base.65b76fcfde0caa67.webp)

### Idea: Instruction Tuned LLMs

[Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) start with foundation model, then dem fine-tune am with examples or input/output pairs (like many-turn "messages") wey get instruction clear - and AI response try follow dat instruction.

E use techniques like Reinforcement Learning with Human Feedback (RLHF) wey fit train model to _follow instructions_ and _learn from feedback_ so dat response go better fit real application and user need.

Make we try am - go back to prompt up, but change _system message_ to dis instruction:

> _Summarize content wey you get for second-grade student. Make result one paragraph wit 3-5 bullet points._

See how result now aligned with di goal and format? Educator fit use dis answer direct for slides for that class.

![Instruction Tuned LLM Chat Completion](../../../translated_images/pcm/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Why we need Prompt Engineering?

Now we sabi how LLMs dey process prompts, make we talk why prompt engineering matter. Di answer na say current LLMs get plenty wahala wey dey make _reliable and constant completions_ hard to achieve if person no try for prompt design and optimization. Like for example:

1. **Model responses no dey sure sure.** Di _same prompt_ fit produce different answers with different models or versions. E fit even bring different results for _same model_ anytime. _Prompt engineering fit help reduce these differences with better protection_.

1. **Models fit make up answers.** Models train with _big but limited_ data, so dem no get info on tins wey no dey di training. So dem fit create answers wey no true, make up, or even contradict facts. _Prompt engineering fit help users find and stop those fake tori, by for example asking AI for citations or reasoning_.

1. **Model ability go different.** Newer model or generation get better ability but e still get own kain wahala and cost. _Prompt engineering fit help make best practice and workflow wey go hide these differences and fit model one by one well without stress_.

Make we see am for OpenAI or Azure OpenAI Playground:

- Use same prompt with different LLM deployments (OpenAI, Azure OpenAI, Hugging Face) - yu see differences?
- Use same prompt many times with _same_ LLM deployment (Azure OpenAI playground) - how those differences them change?

### Fabrications Example

For dis course, we dey use **"fabrication"** to mean when LLMs sometimes produce wrong info because of their training or other limit. You fit don hear people dey call am _"hallucinations"_ for popular article or research papers. But we like make dem call am _"fabrication"_ to no make person think say machine dey get human feeling or trait. E still support [Responsible AI guidelines](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) with better term wey no offends or no fit exclude anybody.

You wan understand how fabrication dey work? Think prompt wey tell AI to generate content for topic wey no dey (make sure e no dey training data). For example - I try dis prompt:

> **Prompt:** generate lesson plan on di Martian War of 2076.

I search web, I see say fictional tori (like TV series or books) dey about Martian wars - but none for 2076. Common sense too talk say 2076 na _future_ so e no possible to really happen.


So wetin dey happen when we run dis prompt wit different LLM providers?

> **Response 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/pcm/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Response 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/pcm/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Response 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/pcm/04-fabrication-huggingchat.faf82a0a51278956.webp)

As we expect, each model (or version of model) dey produce small small different responses because of stochastic behavior and variation for how model fit do tins. For example, one model dey target 8th grade porpople while the other dey think say e be high-school student. But all the three models generate responses wey fit make person wey no sabi believe say the event really happen.

Prompt engineering techniques like _metaprompting_ and _temperature configuration_ fit reduce model fabrication small small. New prompt engineering _architectures_ still dey add new tools and techniques well well inside the prompt flow, to help reduce or stop some of these effects.

## Case Study: GitHub Copilot

Make we close dis section by reason how prompt engineering dey used for real-life solutions by looking one Case Study: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot na your "AI Pair Programmer" - e dey convert text prompts go code completions and e dey inside your development environment (like Visual Studio Code) to make user experience smooth. As e dey inside the series of blogs below, the first version na based on the OpenAI Codex model - but engineers quickly know say dem need to fine-tune the model and develop beta prompt engineering techniques to improve code quality. For July, dem [unveil better AI model wey pass Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) to give faster suggestions.

Read the posts in order, to follow their learning journey.

- **May 2023** | [GitHub Copilot dey improve for how e dey understand your Code](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **May 2023** | [Inside GitHub: How dem dey work wit di LLMs behind GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jun 2023** | [How to write better prompts for GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jul 2023** | [.. GitHub Copilot go beyond Codex wit better AI model](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [Developer Guide to Prompt Engineering and LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [How to build enterprise LLM app: Lessons from GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

You fit still browse their [Engineering blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) for more posts like [this one](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) wey show how dem dey _apply_ these models and techniques to drive real-world apps.

---

<!--
LESSON TEMPLATE:
This unit go cover core concept #2.
Reinforce the concept wit examples and references.

CONCEPT #2:
Prompt Design.
Illustrated wit examples.
-->

## Prompt Construction

We don see why prompt engineering important - now make we understand how people dey _construct_ prompts so we fit check different techniques to make prompt design beta.

### Basic Prompt

Make we start wit basic prompt: na text wey you send to model without any other context. Here na example – wen we send first few words of US national anthem to OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) e quickly _complete_ the response wit next few lines, to show basic prediction behaviour.

| Prompt (Input)     | Completion (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | E dey sound like say you dey start sing the lyrics to "The Star-Spangled Banner," wey be national anthem of United States. The full lyrics be ... |

### Complex Prompt

Now make we add context and instructions to that basic prompt. The [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) give us chance to build complex prompt like collection of _messages_ with:

- Input/output pairs wey represent _user_ input and _assistant_ response.
- System message wey provide context for how assistant go behave or e personality.

The request now dey for form wey _tokenization_ fit catch better info from context and conversation. So, to change system context fit really affect how good the completions be, as user inputs wey you give.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Instruction Prompt

For examples wey dey above, user prompt na simple text wey fit be request for info. Wit _instruction_ prompts, we fit use dat text to explain task well well, so AI go get beta guide. Here na example:

| Prompt (Input)                                                                                                                                                                                                                         | Completion (Output)                                                                                                        | Instruction Type    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Write description of Civil War                                                                                                                                                                                                   | _dem return simple paragraph_                                                                                              | Simple              |
| Write description of Civil War. Give key dates and events and explain why dem important                                                                                                                                     | _dem return paragraph plus list of key dates with explanation_                                             | Complex             |
| Write description of Civil War in 1 paragraph. Give 3 bullet points wit key dates and why dem important. Give 3 more bullet points wit key historical figures and wetin dem do. Return output as JSON file | _dem return plenty details inside text box, format as JSON wey you fit copy-paste to file and check am_ | Complex. Formatted. |

## Primary Content

For examples wey dey above, prompt still dey open ended well well, so LLM fit choose which part of e pre-trained data e go use. Wit _primary content_ design pattern, input text dey divide into two parts:

- instruction (action)
- important content (wey go affect action)

Here na example wey instruction na "summarize dis in 2 sentences".

| Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completion (Output)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter na fifth planet from the Sun and e be di largest for Solar System. E be gas giant wey get mass wey be one-thousandth of Sun, but two-and-a-half times dat of all other planets for Solar System join. Jupiter be one of di brightest tins wey person fit see for night sky, and people don sabi am since long before. E get name after Roman god Jupiter.[19] Wen you dey look am from Earth, Jupiter fit dey bright to cast shadow, and e be di third-brightest natural tin for night sky after Moon and Venus. <br/> **Summarize this in 2 short sentences** | Jupiter, di fifth planet from Sun, na di largest for Solar System and e dey known as one of di brightest tins inside the night sky. E name after Roman god Jupiter, na gas giant wey mass na two-and-a-half times that of all other planets for Solar System join. |

The primary content fit dey use different ways to give beta instructions:

- **Examples** - instead of to tell model wetin to do wit direct instruction, give am examples make e fit know the pattern.
- **Cues** - after instruction, put "cue" wey go prepare the completion, guide model go beta response.
- **Templates** - na repeatable 'recipes' for prompts wit placeholders (variables) wey you fit change wit specific data for particular use case.

Make we check dis tins for action.

### Using Examples

Dis na way wey you use primary content to "feed model" some examples of output you want for instruction, then make e sabi the pattern for the output. Based on how many examples you give, you fit do zero-shot prompting, one-shot prompting, few-shot prompting etc.

The prompt now get three parts:

- Task description
- Some examples of output wey you want
- The start of new example (wey become implied task description)

| Learning Type | Prompt (Input)                                                                                                                                        | Completion (Output)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "The Sun is Shining". Translate to Spanish                                                                                                            | "El Sol está brillando".    |
| One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot      | Player run bases => Baseball <br/> Player hit an ace => Tennis <br/> Player hit six => Cricket <br/> Player make slam-dunk => | Basketball                  |
|               |                                                                                                                                                       |                             |

Note say for zero-shot prompting, we need put instruction clearly ("Translate to Spanish"), but for one-shot prompting example, e dey implied. The few-shot example show say if you add more examples, model fit get better guess without extra instructions.

### Prompt Cues

Another way to use primary content na to give _cues_ instead of examples. For this one, you dey push model small bit to better direction by _starting am off_ wit part wey show how the response suppose be format. Model go then "take the cue" to continue like dat.

| Number of Cues | Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completion (Output)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter na fifth planet from Sun and e largest for Solar System. E be gas giant wey mass na one-thousandth of Sun, but two-and-a-half times all other planets join. Jupiter na one of brightest tins wey naked eye fit see for night sky, dem sabi am since before history. <br/>**Summarize This**                                       | Jupiter na biggest planet for our Solar System and e dey fifth from Sun. E be gas giant wey mass na 1/1000 of Sun own, but e heavy pass all other planets join. Ancient people don sabi Jupiter long time, and e dey easy to see for night sky. |
| 1              | Jupiter na fifth planet from Sun and e largest for Solar System. E be gas giant wey mass na one-thousandth of Sun, but two-and-a-half times all other planets join. Jupiter na one of brightest tins wey naked eye fit see for night sky, dem sabi am since before history. <br/>**Summarize This** <br/> Wetin we learn be say Jupiter | na fifth planet from Sun and biggest for Solar System. E be gas giant wey mass na one-thousandth of Sun but two-and-a-half times all other planets join. E easy to see with naked eye and people don sabi am since ancient times. |

| 2              | Jupiter na di fif pikin wey dey from di Sun and di biggest for di Solar System. E be gas giant wey get mass one-thousandth wey be sun, but e get two and haaf times wey all di oda planets for di Solar System join. Jupiter na one of di brightest tins wey person fit see with naked eye for night sky, and e don dey known since ancient civilization before history begin record. <br/>**Summarize This** <br/> Top 3 Facts We Learn:         | 1. Jupiter na di fif pikin wey dey from di Sun and di biggest for di Solar System. <br/> 2. E be gas giant wey get mass one-thousandth wey be sun...<br/> 3. Jupiter don dey visible to naked eye since ancient times ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompt Templates

Prompt template na _pre-defined recipe for prompt_ wey fit store and reuse anytime, to make user experience consistent for big plenty. For ground ground, na collection of prompt example like [this one from OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) wey get interactive prompt parts (user and system messages) and API-driven request format - to support reuse.

For im more complex form like [this example from LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), e get _placeholders_ wey fit replace with data from different sources (user input, system context, external data sources etc.) to make prompt dynamically. Dis one allow us create library of reusable prompts wey fit drive consistent user experiences **programmatically** for big scale.

Last last, real value for templates dey for the ability to create and publish _prompt libraries_ for vertical application domains - where di prompt template don now _optimized_ to reflect application-specific context or examples wey go make di responses more correct and sharp for the special user audience. The [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) repository na good example for dis approach, wey dey gather library of prompt for education domain with focus on key objectives like lesson planning, curriculum design, student tutoring etc.

## Supporting Content

If we think about prompt construction as instruction (task) and target (main content), then _secondary content_ na like extra context wey we provide to **influence output in some way**. E fit be tuning parameters, formatting instructions, topic taxonomies etc. wey fit help model _tailor_ im response to fit the wanted user objectives or expectations.

For example: If we get course catalog with plenty metadata (name, description, level, metadata tags, instructor etc.) on all di courses wey dey for curriculum:

- we fit define instruction to "summarize the course catalog for Fall 2023"
- we fit use di main content to give some examples of di wanted output
- we fit use di secondary content to show di top 5 "tags" wey dey important.

Now, di model fit provide summary for the format wey di examples show - but if result get many tags, e fit put priority for di 5 tags wey secondary content talk.

---

<!--
LESSON TEMPLATE:
Dis unit suppose cover core concept #1.
Make concept strong with examples and references.

CONCEPT #3:
Prompt Engineering Techniques.
Wetin be some basic techniques for prompt engineering?
Show am with some exercises.
-->

## Prompting Best Practices

Now we sabi how prompts fit _constructed_, we fit start to think how to _design_ dem to show best practices. We fit divide am for two parts - get correct _mindset_ and apply correct _techniques_.

### Prompt Engineering Mindset

Prompt Engineering na trial-and-error process so keep three big guiding tins for mind:

1. **Domain Understanding Matters.** Response accuracy and relevance depend on di _domain_ wey di application or user dey operate. Use your intuition and domain expertise to **customize techniques** well well. For example, define _domain-specific personalities_ for your system prompts, or use _domain-specific templates_ for your user prompts. Give secondary content wey reflect domain-specific contexts, or use _domain-specific cues and examples_ to lead model to familiar usage patterns.

2. **Model Understanding Matters.** We sabi say models dey stochastic by nature. But model fit get difference based on training data dem use (pre-trained knowledge), di capabilities dem get (e.g., via API or SDK) and di kind content dem optimized for (e.g, code vs. images vs. text). Understand strengths and limits of di model wey you dey use, and use that knowledge to _prioritize tasks_ or build _customized templates_ wey fit di model capability well well.

3. **Iteration & Validation Matters.** Models dey improve fast, plus techniques for prompt engineering dey improve. As domain expert, you fit get your own context or criteria _your_ specific application, wey no fit apply to general community. Use prompt engineering tools & techniques to "jump start" prompt construction, then iterate and validate results with your own intuition and domain expertise. Record your insights and build **knowledge base** (e.g, prompt libraries) wey others fit use as baseline for faster improvements later.

## Best Practices

Now make we look common best practices wey [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) and [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) practitioners recommend.

| Wetin                              | Why                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Check latest models.               | New generation models fit get better features and quality - but dem fit charge more. Check dem to see impact before decision to migrate.                                                                                                       |
| Separate instructions & context   | Check if your model/provider get _delimiters_ to show instructions, main and secondary content clear. This fit help models put weights correct for tokens.                                                                                       |
| Be specific and clear             | Give plenty details about context, outcome, length, format, style etc. This go improve quality and consistency of responses. Keep recipes for reusable templates.                                                                              |
| Be descriptive, use examples      | Models fit respond better if you "show and tell". Start with `zero-shot` where you give instruction (no examples) then try `few-shot` to improve, give small examples of wanted output. Use analogies.                                        |
| Use cues to jumpstart completions | Make e head to desired outcome by giving some beginning words or phrases to start response.                                                                                                                |
| Double Down                       | Sometimes you go need repeat your matter to model. Give instruction before and after main content, use instruction plus cue etc. Iterate and validate to see wetin work.                                                                       |
| Order Matters                     | How you arrange information for model fit change output, even for learning examples, because of recency bias. Try different way to find best.                                                                                                   |
| Give model “out”                  | Make model get _fallback_ completion response if e no fit complete task for any reason. This kin reduce chances say model go create wrong or fake responses.                                                                                        |
|                                   |                                                                                                                                                                                                                                                   |

As with any best practice, remember say _your mileage fit differ_ based on model, task and domain. Use these as beginning, then improve to find wetin work best for you. Always check your prompt engineering process as new models and tools show, focus on scalability and quality.

<!--
LESSON TEMPLATE:
Dis unit suppose get code challenge if e fit happen

CHALLENGE:
Link to Jupyter Notebook wey get code comments only for instructions (code sections empty).

SOLUTION:
Link to copy of dat Notebook with filled prompts and run, showing one example output.
-->

## Assignment

Congrats! You reach end of lesson! Na time to test some of those concepts and techniques with real examples!

For our assignment, we go use Jupyter Notebook with exercises wey you fit do interactive. You fit also add your own Markdown and Code cells to explore ideas and techniques by yourself.

### For start, fork the repo, then

- (Recommended) Launch GitHub Codespaces
- (Alternatively) Clone the repo to your local device and use am with Docker Desktop
- (Alternatively) Open the Notebook for your preferred runtime environment.

### Next, set your environment variables

- Copy `.env.copy` file for repo root to `.env` and fill `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` values. Come back to [Learning Sandbox section](#learning-sandbox) to learn how.

### Next, open Jupyter Notebook

- Choose runtime kernel. If you use option 1 or 2, just pick default Python 3.10.x kernel wey dev container get.

You ready to run exercises. No _right or wrong_ answer here - na trial and error and build intuition for wetin work for given model and application domain.

_Because of dis reason, no Code Solution segments dey for lesson. Instead, the Notebook go get Markdown cells called "My Solution:" wey show one example output as reference._

 <!--
LESSON TEMPLATE:
Wrap section with summary and resources for self-guided learning.
-->

## Knowledge check

Which one be good prompt wey follow reasonable best practices?

1. Show me image of red car
2. Show me image of red car wey be make Volvo and model XC90 parked by cliff with sun setting
3. Show me image of red car wey be make Volvo and model XC90

A: 2 na di best prompt because e give details on "wetin" and get specifics (no be any car but specific make and model) and e still describe where e dey. 3 na next best because e still get plenty description.

## 🚀 Challenge

Try use "cue" technique with prompt: Complete di sentence "Show me an image of red car of make Volvo and ". Wetin e go respond? How you go improve am?

## Great Work! Continue Your Learning

Want learn more about different Prompt Engineering concepts? Go [continued learning page](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to find other better resources on this.

Go Lesson 5 where we go dey look [advanced prompting techniques](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->