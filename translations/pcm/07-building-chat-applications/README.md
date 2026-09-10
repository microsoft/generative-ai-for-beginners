# Di Build Generative AI-Powered Chat Applications

[![Di Build Generative AI-Powered Chat Applications](../../../translated_images/pcm/07-lesson-banner.a279b937f2843833.webp)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Click di pikshua we dey above to watch video of dis lesson)_

Now we don see how we fit build text-generation apps, make we look chat applications.

Chat applications don enter for our everyday life, e no just be to yarn anyhow. Dem dey part of customer service, technical support, and even better advisory systems. Maybe you don get help from chat application before. As we dey put better tecnology like generative AI for these platform dem, di wahala go increase.

Some questions we need make dem answer be:

- **Build di app**. How we go fit quickly build and join these AI-powered apps for correct use cases?
- **Monitor**. When we deploy am, how we go take dey watch and make sure say di apps dey work well, for how e dey work and e follow [six principles of responsible AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

As we dey go further into dis level wey automation and human-machine interaction dey easy, to sabi how generative AI dey change how chat applications dey work and adapt na important. Dis lesson go talk about di way we fit build di system, how we fit fine-tune am for different task, and how to check for responsible AI use.

## Introduction

Dis lesson go cover:

- How we go fit quickly build and add chat applications.
- How to customize and fine-tune di apps.
- How to monitor chat applications well well.

## Learning Goals

By di time you finish dis lesson, you go fit:

- Talk about wetin you go reason for build and join chat apps inside systems.
- Customize chat apps for particular purposes.
- Know key metrics and wetin to consider to watch and maintain AI chat apps quality.
- Make sure say chat apps dey use AI in responsible way.

## Join Generative AI for Chat Applications

Make chat apps better with generative AI no mean just to make dem smarter; e be to make their design, performance, and user experience better. Dis one include checking architecture, APIs and how user interface suppose be. Dis part go give you road map for these tori, whether you wan add to existing systems or build stand-alone platform.

By di time you finish this section, you go get di skills to build and add chat applications well.

### Chatbot or Chat application?

Before we come talk about build chat applications, make we compare 'chatbots' with 'AI-powered chat applications,' dem get different jobs and functionalities. Chatbot main work na to automate some small talk task like answer common questions or track package. Dem dey follow rule-based or complex AI algorithm. AI-powered chat applications get broader work, dem fit do text, voice, video chat for human users. Dem use generative AI model wey fit talk like human, respond based on many input and context. Generative AI chat fit do open talks, change with conversation, and even create complex tori.

Table below show key difference and similarities to help us understand their special role for digital communication.

| Chatbot                               | Generative AI-Powered Chat Application |
| ------------------------------------- | -------------------------------------- |
| Task-Focused and rule based           | Context-aware                          |
| Often integrated into larger systems  | Fit host one or many chatbots          |
| Limited to programmed functions       | Get generative AI models               |
| Specialized & structured interactions | Fit do open-domain discussions        |

### Use pre-built functions with SDKs and APIs

When you dey build chat application, good move na check wetin dem already get. Use SDKs and APIs dey better for many reasons. By join well-made SDKs and APIs, you go put your app for success long time, solve problem of growth and maintenance.

- **Faster development and less wahala**: Use pre-built functions no need to build by yourself, so you fit focus on other part of your app wey important, like business logic.
- **Better performance**: When you build from scratch, you go ask "How e go scale? App fit handle plenty users?" Well maintained SDKs and APIs get built-in solution for these matter.
- **Easy maintenance**: Updates and improve easy because most APIs and SDKs only need update library when new version come.
- **Access to latest technology**: Use models wey dey fine-tuned and trained well on plenty data give your app natural language powers.

To fit use SDK or API, normally you go need get permission with one unique key or token. We go use OpenAI Python Library to see how dis one dey work. You fit also try am yourself for [notebook for OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) or [notebook for Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) for dis lesson.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

response = client.responses.create(model="gpt-5-mini", input="Suggest two titles for an instructional lesson on chat applications for generative AI.", store=False)
print(response.output_text)
```

Di example up dey use GPT-5 mini model with Responses API to finish prompt, but see say API key don set already. If you no set key, error go happen.

## User Experience (UX)

Normal UX rules dey apply to chat apps, but here some extra things wey important because of machine learning.

- **Way to fix ambiguity**: Generative AI models sometimes go give unclear answer. Feature wey let user ask to clear things fit help if dis one happen.
- **Keep context well**: Advanced generative AI fit remember context inside talk, dis one fit make user experience beta. Let user control context go better, but e get risk if sensitive info still dey. You fit think how long to keep info by policy to balance context and privacy.
- **Personalization**: Because AI fit learn and adapt, e dey give personal experience for user. Make user experience different with user profiles no just make user feel understood, e also help make answer find easier and interaction smooth.

One example personalization na the "Custom instructions" inside OpenAI ChatGPT. E allow you put info about yourself wey fit help for your prompts. Here na example custom instruction.

![Custom Instructions Settings in ChatGPT](../../../translated_images/pcm/custom-instructions.b96f59aa69356fcf.webp)

Dis "profile" make ChatGPT create lesson plan on linked lists. See how ChatGPT consider say user fit want deep lesson based on her experience.

![A prompt in ChatGPT for a lesson plan about linked lists](../../../translated_images/pcm/lesson-plan-prompt.cc47c488cf1343df.webp)

### Microsoft's System Message Framework for Large Language Models

[Microsoft don give guide](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) for write better system messages when you wan generate response from LLMs, e get 4 parts:

1. Define who di model dey serve, and wetin e fit do or no fit do.
2. Define how model go show output.
3. Give example wey show how model suppose behave.
4. Give extra rules to control behavior.

### Accessibility

Whether user get problem with eye, ear, motor or brain, good chat app suppose fit make all dem use am. List below dey show features wey dey help users wey get different impairments.

- **For visual impairment**: High contrast themes and text wey fit resize, screen reader support.
- **For auditory impairment**: Text-to-speech and speech-to-text, visual señales for audio alert.
- **For motor impairment**: Keyboard navigation, voice commands.
- **For cognitive impairment**: Use simple language options.

## Customization and Fine-tuning for Domain-Specific Language Models

Imagine chat app wey sabi your company talk and fit guess wetin user fit ask. Two main ways to take do am:

- **Use DSL models**. DSL mean domain-specific language. You fit use model wey train on specific domain to understand e concepts.
- **Fine-tune**. Fine-tuning na training di model more with specific data.

## Customization: Use DSL

Using domain-specific language models (DSL Models) fit make user enjoy more when interaction dey special and correct for context. E mean model train or fine-tune to understand and create text for particular field or subject. You fit train DSL model from scratch or use SDKs and APIs for ready ones. Another way na fine-tune already trained model for specific domain.

## Customization: Fine-tuning

Fine-tuning common when pre-trained model no too good for special domain or task.

For example, medical questions complex and need plenty context. When doctor diagnoses patient, e dey based on lifestyle, past sickness, and recent medical journals to confirm diagnosis. For such one, general AI chat app no fit dey reliable.

### Example: Medical application

Think of chat app wey help medical workers to get quick info on treatment guide, drug interactions, or new research.

General model fit good to answer basic medical questions or give general advice, but e fit waka struggle with:

- **Very specific or complex cases**. For example, neurologist fit ask, "Wetin be best practice to manage drug-resistant epilepsy for pikin?"
- **No recent updates**. General model fit no fit give up-to-date answer wey include latest medicine and neurology discoveries.

For cases like dis, fine-tune model with medical data go make am better for dis kind complex medical questions. Dis one need plenty correct data wey show domain challenges and questions.

## Considerations for High-Quality AI-Driven Chat

Dis part go talk about criteria for "high-quality" chat apps, including how to measure performance and use AI responsibly.

### Key Metrics

To keep app performance high, you need to check key metrics and things to consider. These go help check app dey work well and AI and user experience quality. Below na list of basic, AI, and user experience metrics to think about.

| Metric                        | Meaning                                                                                                             | Wetin chat developer suppose consider                                         |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Uptime**                    | How long app dey work and users fit use am.                                              | How you go keep downtime reduce?                                           |
| **Response Time**             | How fast app go answer user question.                                                          | How you go make processing faster to get quick answer?           |
| **Precision**                 | Ratio of correct positive answer to total positive answer                                     | How you go check model precision?                        |
| **Recall (Sensitivity)**      | Ratio of true positive answer to actual positive cases                                               | How you go measure and improve recall?                                  |
| **F1 Score**                  | Balance between precision and recall                                   | Wetin be your target F1 Score? How you go balance precision and recall?  |
| **Perplexity**                | How well model probability fit real data distribution | How you go reduce perplexity?                                         |
| **User Satisfaction Metrics** | How users see the app. You fit collect this through surveys                                     | How often you go collect user feedback? How you go take adjust? |
| **Error Rate**                | How much model dey make mistakes for understanding or generating output                                                 | What ways you get to reduce error?               |
| **Retraining Cycles**         | How often model dey update with new data and knowledge                                    | How often you go retrain model? Wetin go make you start retrain?   |

| **Anomaly Detection**         | Tools and techniques for identifying unusual patterns wey no follow wetin dem expect.                        | How you go take respond to anomalies?                                        |

### How to Take Put Responsible AI Practices for Chat Applications

Microsoft way to Responsible AI don find six principles wey suppose guide AI development and use. Below na the principles, their meaning, and tins wey chat developer suppose consider and why dem suppose take am serious.

| Principles             | Microsoft Meaning                                | Things for Chat Developer to Consider                                      | Why E Important                                                                     |
| ---------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Fairness               | AI systems suppose treat all people fair.            | Make sure say the chat app no dey discriminate base on user data.  | To build trust and make everybody feel say dem dey included; no go cause wahala with law.                |
| Reliability and Safety | AI systems suppose dey reliable and safe.        | Make testing and fail-safes to reduce errors and risks.         | Make sure users dey satisfied and to prevent any gbege.                                 |
| Privacy and Security   | AI systems suppose dey secure and respect privacy.      | Put strong encryption and ways to protect data.              | To protect sensitive user data and follow privacy laws.                         |
| Inclusiveness          | AI systems suppose empower everybody and involve people. | Design UI/UX wey everybody fit use easy for different kinds of people. | Make sure more people fit use the app well.                   |
| Transparency           | AI systems suppose dey easy to understand.                  | Provide clear documentation and explanation for AI responses.            | Users go trust system more if dem fit understand how decisions dey happen. |
| Accountability         | People suppose dey responsible for AI systems.          | Make clear process to check and improve AI decisions.     | Make the system fit dey improve and fix mistake when e happen.               |

## Assignment

See [assignment](../../../07-building-chat-applications/python). E go carry you go through exercise dem from to run your first chat prompts, to classify and summarize text and more. Notice say assignments dey available for different programming languages!

## Good Work! Make You Continue

After you finish this lesson, check our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue improve your Generative AI knowledge!

Go Lesson 8 to see how you fit start [build search applications](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->