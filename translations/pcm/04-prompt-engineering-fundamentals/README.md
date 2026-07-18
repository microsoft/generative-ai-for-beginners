# Prompt Engineering Fundamentals

[![Prompt Engineering Fundamentals](../../../translated_images/pcm/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Introduction
Dis module dey cover beta ideas and methods wey you fit use create correct prompts for generative AI models. How you write your prompt to LLM matter too. If you sabi arrange prompt well, e go bring better answer. But wetin prompt and prompt engineering mean? How I fit improve di prompt input wey I dey send go LLM? Dem na di questions wey we go try answer for dis chapter plus di next one.

_Generative AI_ fit create new content (e.g., text, pictures, audio, code etc.) wen person ask am. E dey do dis with _Large Language Models_ like OpenAI GPT ("Generative Pre-trained Transformer") series wey dem train to sabi natural language plus code.

People fit now use these models like for chat, no need technical skill or training. Di models na _prompt-based_ - people send text input (prompt) then dem go get AI answer (completion). Dem fit still talk with AI many times, dey change prompt make answer match wetin dem want.

"Prompts" don become main _programming interface_ for generative AI apps, wey dey tell models wetin dem go do and fit affect how correct the answers go be. "Prompt Engineering" na field wey dey grow quick wey dey focus on _design and optimization_ of prompts to bring better and steady answers.

## Learning Goals

For dis lesson, we go sabi wetin Prompt Engineering be, why e important, and how we fit do better prompts for one model plus purpose. We go understand core ideas and beta ways for prompt engineering - plus see interactive Jupyter Notebooks "sandbox" where we fit try use these ideas for real examples.

By end of dis lesson we go fit:

1. Explain wetin prompt engineering be and why e matter.
2. Talk di parts of prompt and how dem dey use am.
3. Learn beta ways and techniques for prompt engineering.
4. Use di techniques for real examples, with OpenAI endpoint.

## Key Terms

Prompt Engineering: Na how person dey design and fine-tune inputs to make AI models give correct output.
Tokenization: Na how text dey break into small parts (tokens) wey model fit understand and process.
Instruction-Tuned LLMs: Large Language Models (LLMs) wey dem don fine-tune with instructions to make dem answer better and correct.

## Learning Sandbox

Prompt engineering still be more like art than science. Best way to sabi am na to _practice more_ and try anyhow combination of your experience with di codes and methods.

The Jupyter Notebook wey join dis lesson na _sandbox_ place wey you fit try wetin you dey learn - anytime or for di code challenge at end. To run di exercises, you need:

1. **An Azure OpenAI API key** - na di service endpoint for deployed LLM.
2. **A Python Runtime** - wey go run di Notebook.
3. **Local Env Variables** - _finish di [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) steps make you ready_.

Di notebook get _starter_ exercises - but you fit add your own _Markdown_ (description) and _Code_ (prompt requests) parts to try more ideas and sabi prompt design more.

## Illustrated Guide

You want first see di whole idea wey dis lesson go talk before you start? Look this illustrated guide, e go show you di main topics plus important takeaways to think about. Di lesson roadmap go carry you from core ideas and wahala to how to use prompt engineering techniques to solve am. Note say "Advanced Techniques" for dis guide na for di _next_ chapter.

![Illustrated Guide to Prompt Engineering](../../../translated_images/pcm/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Our Startup

Now, make we yarn how _dis topic_ relate to our startup aim to [bring AI innovation to education](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). We wan build AI apps for _personalized learning_ - so make we think how different people wey dey use our app fit "design" prompts:

- **Administrators** fit ask AI to _analyze curriculum data to find coverage gaps_. AI fit summarize or draw am with code.
- **Educators** fit ask AI to _make lesson plan for certain audience and topic_. AI fit build personalized plan with correct format.
- **Students** fit ask AI to _teach dem difficult subject_. AI fit guide students with lessons, hints & examples based on their level.

Na just small part of wetin AI fit do. Check [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - na open source prompts library wey education experts prepare - to get better idea of wetin e fit do! _Try run some for di sandbox or OpenAI Playground to see wetin go happen!_

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #1:
Prompt Engineering.
Define it and explain why it is needed.
-->

## Wetin be Prompt Engineering?

We start dis lesson by talk say **Prompt Engineering** na how person dey _design and optimize_ text inputs (prompts) to get steady and correct responses (completions) wey fit di application aim and model. We fit see am as 2-step process:

- _designing_ di first prompt for model and aim
- _refining_ di prompt many times to make answer better

Dis na trial-and-error way wey need person sense and work to get best results. So why e dey important? To answer dis, we first need sabi 3 concepts:

- _Tokenization_ = how model "see" di prompt
- _Base LLMs_ = how di foundation model "process" prompt
- _Instruction-Tuned LLMs_ = how model fit see "tasks"

### Tokenization

One LLM dey see prompts as _sequence of tokens_ where different models fit tokenize same prompt different ways. Since LLMs train on tokens, how prompt get tokenize fit affect answer quality.

To sabi tokenization, try tools like [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) wey e show below. Copy your prompt - and see how e turn to tokens, notice how whitespace and punctuation dey handled. Dis example show older LLM (GPT-3) - so newer model fit show difference.

![Tokenization](../../../translated_images/pcm/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Idea: Foundation Models

Once prompt tokenize, main job of ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (Foundation model) na to predict next token for dat sequence. Since LLMs train on big text data, dem sabi beta the relation between tokens and fit predict them well. Dem no too sabi di _meaning_ of prompt; na pattern dem dey complete. Dem go continue till user stop am or other condition reach.

You want see how prompt-based completion dey work? Put di prompt for [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) with default settings. System treat prompt as information request - so you go see completion wey fit dis context.

But if user want see something specific wey meet criteria or goal? Na here _instruction-tuned_ LLMs enter.

![Base LLM Chat Completion](../../../translated_images/pcm/04-playground-chat-base.65b76fcfde0caa67.webp)

### Idea: Instruction Tuned LLMs

[Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) start with foundation model then fine-tune am using examples or input/output pairs (like multi-turn "messages") wey get clear instructions and AI reply dey try follow instruction.

E use Reinforcement Learning with Human Feedback (RLHF) to train model to _follow instructions_ and _learn from feedback_ so e go give better answers for real use, plus match user goals.

Make we try am - use di first prompt but change _system message_ to:

> _Summarize content you get for second-grade student. Make answer one paragraph with 3-5 bullet points._

See how answer dey follow wetin dem want? Teacher fit just use am for class slides.

![Instruction Tuned LLM Chat Completion](../../../translated_images/pcm/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Why we need Prompt Engineering?

Now we sabi how LLMs dey process prompts, make we talk why we need prompt engineering. E good because current LLMs get challenges wey make _steady correct answers_ hard without good prompt build and tune. For example:

1. **Model answers fit dey random.** _Same prompt_ fit get different answers with different models or model versions. E fit even give different answers with _same model_ anytime. _Prompt engineering fit help reduce these wahala with better guardrails_.

1. **Models fit make up answers.** Dem train with _big but limited_ data, so dem no sabi everything. Sometimes dem go give wrong, imaginary, or contradictory answer. _Prompt engineering fit help check and reduce dis, like dey ask AI for sources or logic_.

1. **Model abilities fit change.** New models get better skills but also new wahala and cost. _Prompt engineering fit help make best ways that fit any model, hide differences, and work well as e large_.

Make we try for OpenAI or Azure OpenAI Playground:

- Use same prompt for different LLM deployments (OpenAI, Azure OpenAI, Hugging Face) - you see differences?
- Use same prompt many times with _same_ LLM (Azure OpenAI playground) - how e differ?

### Fabrications Example

For dis course, we dey use **"fabrication"** to mean say sometimes LLMs dey produce wrong info because dem training or other limits. Some people dey call am _"hallucinations"_, but we prefer _"fabrication"_ to no make am look like machine get human feelings. E also fit help follow [Responsible AI guidelines](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) plus remove offensive or no-inclusive words.

You want try understand how fabrication dey work? Imagine prompt wey tell AI make e create content on topic wey no dey for training data. I try dis prompt:

> **Prompt:** generate a lesson plan on the Martian War of 2076.

Web search show say people get fake stories for Martian wars (like TV shows, books) but no one talk about 2076. Common sense tell us 2076 na future so e no fit be real event.


So wetin dey happen wen we run dis prompt wit different LLM providers?

> **Response 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/pcm/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Response 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/pcm/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Response 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/pcm/04-fabrication-huggingchat.faf82a0a51278956.webp)

As we bin expect, each model (or model version) dey produce small different response because of stochastic behavior and model capability variations. For example, one model dey target 8th grade audience while di other dey assume say na high-school student. But all di three models generate response wey fit convince pesin wey no sabi anything sef say the event na real.

Prompt engineering techniques like _metaprompting_ and _temperature configuration_ fit reduce model fabrication small. New prompt engineering _architectures_ sef dey add new tools and teknik join the prompt flow well well, to help stop or reduce some of dis wahala dem.

## Case Study: GitHub Copilot

Make we con close dis section by feel how prompt engineering dey used for real-world solution by looking one Case Study: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot na your "AI Pair Programmer" - e dey convert text prompts to code completions and e dey inside your development environment (like Visual Studio Code) to make user experience smooth. As e dey show for di blog series below, di first version based on OpenAI Codex model - engineers quick quick sabi say dem gats fine-tune the model and create better prompt engineering teknik to make code better. For July, dem [comot one better AI model wey pass Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) for even faster suggestion dem.

Read di posts dem for order, so you fit follow how dem learn.

- **May 2023** | [GitHub Copilot dey better for understanding your code](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **May 2023** | [Inside GitHub: How di LLMs behind GitHub Copilot dey work](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jun 2023** | [How to write better prompt for GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jul 2023** | [.. GitHub Copilot go beyond Codex wit improved AI model](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [Developer Guide to Prompt Engineering and LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [How to build enterprise LLM app: Lessons from GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

You fit still waka go their [Engineering blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) for more post like [dis one](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) wey show how these models and teknik dem dey _apply_ for real-world application dem.

---

<!--
LESSON TEMPLATE:
This unit suppose cover core concept #2.
Reinforce di concept wit examples and references.

CONCEPT #2:
Prompt Design.
Illustrated wit example.
-->

## Prompt Construction

We don see why prompt engineering important - now make we understand how prompts dey _construct_ so we fit evaluate different teknik dem to design prompt wey go work well well.

### Basic Prompt

Make we start with basic prompt: na text input wey you send to the model without any other context. Example be say - wen we send di first few words of US national anthem to OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) e go instantly _complete_ the response wit di next few lines, to show basic prediction behavior.

| Prompt (Input)     | Completion (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | E sound like you dey start the lyrics to "The Star-Spangled Banner," di national anthem of United States. The full lyrics na ...             |

### Complex Prompt

Now make we add context and instructions to dat basic prompt. Di [Chat Completion API](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) make we build complex prompt as collection of _messages_ wit:

- Input/output pairs wey show _user_ input and _assistant_ response.
- System message wey set the context for assistant behavior or personality.

Di request now dey form wey be like dis, where _tokenization_ dey catch relevant info from context and conversation. Now, if you change system context e fit affect how good di completions go be, just like di user inputs wey you provide.

```python
response = client.responses.create(
    model="gpt-5-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Instruction Prompt

For di example wey dey top, di user prompt na simple text query wey fit mean say na request for information. But wit _instruction_ prompts, we fit use dat text come talk the task well well to guide AI better. Example like dis:

| Prompt (Input)                                                                                                                                                                                                                         | Completion (Output)                                                                                                        | Instruction Type    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Write a description of the Civil War                                                                                                                                                                                                   | _e return simple paragraph_                                                                                               | Simple              |
| Write a description of the Civil War. Provide key dates and events and describe their significance                                                                                                                                     | _e return paragraph follow by list of key event dates with descriptions_                                                  | Complex             |
| Write a description of the Civil War in 1 paragraph. Provide 3 bullet points with key dates and their significance. Provide 3 more bullet points with key historical figures and their contributions. Return the output as a JSON file | _e return more details body inside text box, wey dem format as JSON so you fit copy-paste put for file and validate_       | Complex. Formatted. |

## Primary Content

For di example dem wey dey top, di prompt still dey open-ended, make LLM decide which part of im pre-trained dataset suppose relate. Wit _primary content_ design pattern, input text dey chop into two parts:

- instruction (action)
- relevant content (wey go affect di action)

Example be say instruction na "summarize this in 2 sentences".

| Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completion (Output)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter na fifth planet from Sun and di largest for Solar System. E be gas giant wey mass na one-thousandth of Sun, but e heavy pass all other planets for Solar System put together two-and-a-half times. Jupiter na one of di brightest objects wey person fit see with eye for night sky, and ancient people sabi am since before dem start record history. E get name from Roman god Jupiter.[19] Wen person dey look am from Earth, e fit dey bright wella so e fit cast shadow wey you fit see,[20] and on average e be di third-brightest natural object for night sky after Moon and Venus. <br/> **Summarize this in 2 short sentences** | Jupiter, di fifth planet from Sun, na di largest for Solar System and e dey known as one of di brightest thing for night sky. E get name from Roman god Jupiter, e be gas giant wey get mass wey pass all other planets for Solar System put together two-and-a-half times.                    |

Di primary content segment fit use in plenty different way to make instruction dem strong:

- **Examples** - instead of telling model wetin to do wit clear instruction, give am examples of wetin to do make e fit find di pattern.
- **Cues** - follow instruction wit "cue" wey go prime di completion, to guide model go better response.
- **Templates** - na repeatable 'recipes' for prompts wit placeholders (variables) wey you fit customize wit data for specific case dem.

Make we try dem for action.

### Using Examples

Dis na way wey you dey use primary content to "feed the model" some examples of di output wey you want for one instruction, and make e find di pattern for di output you want. Based on how many examples we provide, we fit do zero-shot prompting, one-shot prompting, few-shot prompting and others.

Di prompt now get three parts:

- Task description
- Some examples of di output wey dem want
- Di start of new example (wey fit be implicit task description)

| Learning Type | Prompt (Input)                                                                                                                                        | Completion (Output)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "The Sun is Shining". Translate to Spanish                                                                                                            | "El Sol está brillando".    |
| One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot      | The player ran the bases => Baseball <br/> The player hit an ace => Tennis <br/> The player hit a six => Cricket <br/> The player made a slam-dunk => | Basketball                  |
|               |                                                                                                                                                       |                             |

See how for zero-shot prompting we gats give clear instruction ("Translate to Spanish"), but for one-shot prompting example e just dey inferred. Di few-shot example show how if you add more examples e help model make better inference without any instruction again.

### Prompt Cues

Another way to use primary content na to give _cues_ no be examples. For dis one, we dey give model small push to di correct direction by _starting am_ wit small part wey show di response format wey we want. Model go "take di cue" go continue like dat.

| Number of Cues | Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completion (Output)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter na fifth planet from Sun and di largest for Solar System. E be gas giant wey mass na one-thousandth of Sun, but e heavy pass all other planets for Solar System put together two-and-a-half times. Jupiter na one of di brightest objects wey person fit see with eye for night sky, and ancient people sabi am since before dem start record history. <br/>**Summarize This**                                       | Jupiter na di largest planet for our Solar System and di fifth one from Sun. E be gas giant wey get mass 1/1000th of Sun, but e heavy pass all other planets totol. Ancient people don sabi Jupiter for long time, and e easy to see for night sky..                   |
| 1              | Jupiter na fifth planet from Sun and di largest for Solar System. E be gas giant wey mass na one-thousandth of Sun, but e heavy pass all other planets for Solar System put together two-and-a-half times. Jupiter na one of di brightest objects wey person fit see with eye for night sky, and ancient people sabi am since before dem start record history. <br/>**Summarize This** <br/> Wetin we learn be say Jupiter | na fifth planet from Sun and di largest for Solar System. E be gas giant wey mass na one-thousandth of Sun, but e heavy pass all planets join. E dey easy to see with eye and people don sabi am since long time.                                      |

| 2              | Jupiter na di fifth planet from Sun an di biggest for Solar System. E be gas giant with mass wey be one-thousandth dat of di Sun, but e big pass two-an-half times all di oda planets for di Solar System put together. Jupiter na one of di brightest tins we fit see with naked eye for night sky, an ancient people don sabi am since before recorded history. <br/>**Summarize This** <br/> Top 3 Facts We Learn:         | 1. Jupiter na di fifth planet from Sun an di biggest for di Solar System. <br/> 2. E be gas giant with mass wey be one-thousandth dat of di Sun...<br/> 3. Jupiter don dey visible to naked eye since ancient times ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompt Templates

Prompt template na _pre-defined recipe for prompt_ wey fit store an use again anytime, to help make user experience good well well for big scale. For simple form, e just be collection of prompt examples like [dis one from OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) wey get both interactive prompt parts (user and system messages) and di API-driven request format - to support reuse.

For more complex form like [dis example from LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) e get _placeholders_ wey fit change with data from different sources (user input, system context, external data sources etc.) to create prompt on di go. Dis let us build library of reusable prompts wey fit help make user experience **programmatically** good well well for big scale.

At last, di true value of templates na di power to create and share _prompt libraries_ for specific application areas - wey di prompt template now _optimized_ to match di application-specific context or examples wey make di responses relevant and correct for di user target. Di [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) repository na beta example for dis approach, wey dey collect library of prompts for education area with focus on main goals like lesson planning, curriculum design, student tutoring etc.

## Supporting Content

If we think prompt construction get instruction (task) and target (main content), then _secondary content_ na like extra context wey we give to **influence di output somehow**. E fit be tuning parameters, formatting instructions, topic taxonomies etc. wey fit help model _tailor_ im response to match wetin user want or expect.

For example: Given course catalog with plenty metadata (name, description, level, metadata tags, instructor etc.) for all courses wey dey curriculum:

- we fit define instruction to "summarize course catalog for Fall 2023"
- we fit use primary content to show some examples of wetin output suppose be
- we fit use secondary content to identify top 5 "tags" wey matter.

Now, di model fit provide summary in di format wey di examples show - but if result get many tags, e fit put first 5 tags wey secondary content identify.

---

<!--
LESSON TEMPLATE:
Dis unit suppose cover core concept #1.
Reinforce di concept with examples and references.

CONCEPT #3:
Prompt Engineering Techniques.
Wetin be some basic techniques for prompt engineering?
Show am with some exercises.
-->

## Prompting Best Practices

Now we sabi how prompts fit _constructed_, we fit start dey think how to _design_ dem to show best practices. We fit break am into two parts - get correct _mindset_ and use correct _techniques_.

### Prompt Engineering Mindset

Prompt Engineering na trial-and-error process so keep three big guiding factors for mind:

1. **Domain Understanding Matter.** Response accuracy and relevance na function of _domain_ wey di application or user dey operate. Use your intuition and domain knowledge to **customize techniques** well well. For example, define _domain-specific personalities_ for your system prompts, or use _domain-specific templates_ for user prompts. Provide secondary content wey show domain-specific context, or use _domain-specific cues and examples_ to guide model to familiar usage.

2. **Model Understanding Matter.** We sabi say models dey stochastic by nature. But model fit differ based on training dataset (pre-trained knowledge), capabilities wey e get (like API or SDK) and content type e optimize for (code vs images vs text). Understand model strength and limits wey you dey use, and use dat knowledge to _prioritize tasks_ or make _custom templates_ wey optimize model ability.

3. **Iteration & Validation Matter.** Models dey change fast, so techniques for prompt engineering too. As domain expert, you fit get other context or criteria for _your_ specific app, wey no fit work for broader community. Use prompt engineering tools & techniques to quick start prompt building, then iterate and check results with your own intuition and knowledge. Write down your insights and make **knowledge base** (like prompt libraries) wey other people fit use as new base for faster work later.

## Best Practices

Now make we look common best practices wey [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) and [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) people recommend.

| Wetin                              | Why                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Evaluate latest models.           | New model generations fit get better features and quality - but e fit also cost pass before. Check dem well, then decide if you wan migrate.                                                                                                    |
| Separate instructions & context   | Check if model/provider get _delimiters_ to separate instructions, primary and secondary content clear. Dis fit help models assign correct weight to tokens.                                                                                 |
| Be specific and clear             | Give more detail about context, outcome, length, format, style etc. Dis go make response better and consistent. Keep recipes safe in reusable templates.                                                                                      |
| Be descriptive, use examples      | Models fit respond well if you "show and tell" style. Start with `zero-shot` where you just give instruction (no examples), then try `few-shot` to improve with small examples of output wey you want. Use analogies.                           |
| Use cues to jumpstart completions | Push am to desired output by giving some first words or phrases wey e fit use as start point for response.                                                                                                                                    |
| Double Down                       | Sometimes you need to repeat to model. Put instructions before and after primary content, use instruction and cue, etc. Check and test to see which one work.                                                                                 |
| Order Matters                     | Order wey you show info to model fit affect output, even for learning examples, because model remember recent info better. Try different ways to see which one best.                                                                          |
| Give model “out”                   | Give model fallback response if e no fit do task. Dis fit reduce chance say model go lie or make up answer.                                                                                                                                     |
|                                   |                                                                                                                                                                                                                                                   |

Like any best practice, remember say _your mileage fit differ_ based on model, task and domain. Use these as start point, then try and find wetin best for you. Always check prompt engineering process again when new models and tools show, make sure process fit scale and answer pass well.

<!--
LESSON TEMPLATE:
Dis unit suppose get code challenge if e fit

CHALLENGE:
Link to Jupyter Notebook wey get only code comments for instruction (code sections empty).

SOLUTION:
Link to copy of dat Notebook wey prompts don fill and run, show how one example fit be.
-->

## Assignment

Congrats! You reach end of lesson! Time don come to test some of those concepts and techniques with real examples!

For our assignment, we go use Jupyter Notebook with exercises wey you fit work on interactively. You fit also add your own Markdown and Code cells for Notebook to explore ideas and techniques on your own.

### To start, fork di repo, then

- (Recommended) Start GitHub Codespaces
- (Alternatively) Clone repo down to your local device and use with Docker Desktop
- (Alternatively) Open Notebook with your preferred Notebook runtime.

### Next, set your environment variables

- Copy `.env.copy` file for repo root to `.env` and fill `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`. Come back to [Learning Sandbox section](#learning-sandbox) to learn how.

### Then, open Jupyter Notebook

- Pick runtime kernel. If you dey use option 1 or 2, just select default Python 3.10.x kernel wey dev container provide.

You ready to run exercises now. Note say no _right or wrong_ answer here - na just to explore options by trial-and-error and build intuition for wetin work for model and app domain.

_Because of dis, no Code Solution part dey for dis lesson. Instead, Notebook go get Markdown cells named "My Solution:" wey go show one example output for reference._

 <!--
LESSON TEMPLATE:
Wrap section with summary and resources for self-guided learning.
-->

## Knowledge check

Which of these prompt be good one wey follow correct best practices?

1. Show me image of red car
2. Show me image of red car wey be make Volvo an model XC90 wey park near cliff with sun dey set
3. Show me image of red car wey be make Volvo and model XC90

A: 2, e best prompt because e give details on "wetin" and e go into specifics (no be any car but specific make and model) an e still describe overall setting. 3 na next best because e still get plenty description.

## 🚀 Challenge

Try use "cue" technique with prompt: Complete sentence "Show me image of red car wey be make Volvo and ". Wetin e go respond? How you go make am better?

## Great Work! Continue your Learning

Want learn more about different Prompt Engineering concepts? Go [continued learning page](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) find other beta resources about dis topic.

Go Lesson 5 where we go see [advanced prompting techniques](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->