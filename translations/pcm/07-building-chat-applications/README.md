<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5308963a56cfbad2d73b0fa99fe84b3",
  "translation_date": "2025-11-12T09:01:20+00:00",
  "source_file": "07-building-chat-applications/README.md",
  "language_code": "pcm"
}
-->
# How to Build Chat App Wey Use Generative AI

[![How to Build Chat App Wey Use Generative AI](../../../translated_images/07-lesson-banner.a279b937f2843833.pcm.png)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Click di image wey dey up to watch di video for dis lesson)_

Now wey we don see how we fit build app wey dey generate text, make we look how we fit build chat app.

Chat app don become part of our everyday life, e no be just for casual talk. Dem dey use am for customer service, technical support, and even advanced advisory systems. E fit be say you don use chat app get help recently. As we dey add better technology like generative AI into dis platforms, di wahala wey dey come with am go dey increase.

Some questions wey we go need answer na:

- **How to build di app**. How we go fit build and join dis AI-powered app for di kind work wey we wan use am do?
- **Monitoring**. After we don deploy am, how we go fit dey check say di app dey work well, both for di way e dey function and di [six principles of responsible AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

As we dey enter di time wey automation and smooth human-machine interaction dey lead, e dey important to sabi how generative AI dey change di way chat app dey work, di kind work e fit do, and how e dey adapt. Dis lesson go show di architecture wey dey support dis kind system, how we fit fine-tune am for di work wey we wan use am do, and di metrics wey we go use make sure say di AI dey work responsibly.

## Introduction

Dis lesson go cover:

- How to build and join chat app well.
- How to customize and fine-tune di app.
- Di strategies and things wey we go consider to dey monitor chat app well.

## Learning Goals

By di end of dis lesson, you go sabi:

- Di things wey you go think about when you dey build and join chat app for di system wey dey already.
- How to customize chat app for di work wey you wan use am do.
- Di main metrics and things wey you go consider to dey monitor and make sure say di AI-powered chat app dey work well.
- How to make sure say di chat app dey use AI responsibly.

## How to Add Generative AI into Chat App

To make chat app better with generative AI no be just to make dem smart; e dey about how to make di architecture, performance, and user interface better so dat di user go enjoy am. Dis one mean say we go look di foundation, API integration, and di user interface. Dis section go give you di roadmap wey you need to sabi how to handle dis wahala, whether you dey join am for di system wey dey already or you dey build am as standalone platform.

By di end of dis section, you go sabi how to build and join chat app well.

### Chatbot or Chat App?

Before we start to build chat app, make we compare 'chatbots' and 'AI-powered chat app,' wey dey do different work. Chatbot dey automate specific talk like answering FAQ or tracking package. E dey use rule-based logic or complex AI algorithms. AI-powered chat app na bigger environment wey dey allow different kind digital communication like text, voice, and video chat between people. Di main thing wey dey make am different na di generative AI model wey dey simulate human-like talk, dey give answer based on di input and di context. AI-powered chat app fit talk about anything, dey adapt to di way di talk dey go, and even dey create creative or complex talk.

Di table wey dey below go show di difference and similarity to help us sabi di work wey dem dey do for digital communication.

| Chatbot                               | Generative AI-Powered Chat App         |
| ------------------------------------- | -------------------------------------- |
| Task-Focused and rule based           | E dey understand context               |
| E dey join bigger systems             | E fit host one or many chatbots        |
| E dey limited to programmed functions | E dey use generative AI models         |
| E dey do structured interactions      | E fit talk about anything              |

### How to Use SDKs and APIs Weh Don Ready-Made

When you dey build chat app, one better step na to check wetin dey already. To use SDKs and APIs to build chat app na better strategy for many reasons. If you use SDKs and APIs wey dem don document well, you dey position your app for long-term success, dey handle scalability and maintenance wahala.

- **E dey make development fast and reduce wahala**: If you use ready-made functionalities instead of dey build am yourself, you go fit focus on di other parts of your app wey dey important, like di business logic.
- **Better performance**: If you dey build functionality from scratch, you go ask yourself "How e go scale? E fit handle plenty users at once?" SDKs and APIs wey dem dey maintain well dey get solution for dis kind wahala.
- **E dey easy to maintain**: Updates and improvements dey easy to manage because most APIs and SDKs just need you to update di library when new version come out.
- **Access to better technology**: If you use models wey dem don train well, e go give your app natural language capabilities.

To use SDK or API functionality, you go need permission to use di service, and dis one dey usually through unique key or authentication token. We go use OpenAI Python Library to show how e dey look. You fit try am yourself for dis [notebook for OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) or [notebook for Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) for dis lesson.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

chat_completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Suggest two titles for an instructional lesson on chat applications for generative AI."}])
```

Di example wey dey up dey use GPT-3.5 Turbo model to complete di prompt, but you go notice say di API key dey set before e run. If you no set di key, e go show error.

## User Experience (UX)

General UX principles dey apply to chat app, but some extra things dey important because of di machine learning wey dey involved.

- **How to handle ambiguity**: Generative AI models fit sometimes give answer wey no clear. Feature wey go allow users ask for clarification go help if dem see dis kind problem.
- **Context retention**: Advanced generative AI models fit remember di context of di talk, and dis one fit help di user experience. If you give users di ability to control and manage di context, e go make di experience better, but e fit also keep sensitive user information. You go need to think about how long you go store dis information, like retention policy, to balance di need for context and privacy.
- **Personalization**: AI models fit learn and adapt, so e fit give di user personalized experience. If you use features like user profiles, e go make di user feel understood and help dem find di answer wey dem dey look for fast.

One example of personalization na di "Custom instructions" settings for OpenAI's ChatGPT. E dey allow you provide information about yourself wey fit be important for di prompts. See example of custom instruction.

![Custom Instructions Settings in ChatGPT](../../../translated_images/custom-instructions.b96f59aa69356fcf.pcm.png)

Dis "profile" dey prompt ChatGPT to create lesson plan on linked lists. You go notice say ChatGPT dey consider say di user fit want more detailed lesson plan based on her experience.

![A prompt in ChatGPT for a lesson plan about linked lists](../../../translated_images/lesson-plan-prompt.cc47c488cf1343df.pcm.png)

### Microsoft's System Message Framework for Large Language Models

[Microsoft don give guidance](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) on how to write better system messages when you dey generate response from LLMs. Dem break am down into 4 areas:

1. Define who di model dey for, di things e fit do, and di things e no fit do.
2. Define di format wey di model go use for output.
3. Provide examples wey show di behavior wey you want for di model.
4. Provide extra rules wey go guide di behavior.

### Accessibility

Whether di user get visual, auditory, motor, or cognitive impairment, di chat app wey dem design well suppose dey easy for everybody to use. Di list wey dey below show di features wey go help make di app accessible for different kind impairment.

- **For Visual Impairment**: High contrast themes, resizable text, screen reader compatibility.
- **For Auditory Impairment**: Text-to-speech and speech-to-text functions, visual cues for audio notifications.
- **For Motor Impairment**: Keyboard navigation support, voice commands.
- **For Cognitive Impairment**: Simplified language options.

## How to Customize and Fine-tune for Domain-Specific Language Models

Imagine chat app wey sabi your company language and fit predict di kind question wey di users dey always ask. Two approaches dey wey you fit use:

- **Use DSL models**. DSL mean domain specific language. You fit use DSL model wey dem don train for specific domain to sabi di concepts and scenarios.
- **Fine-tuning**. Fine-tuning na di process wey you go use train di model more with specific data.

## Customization: Use DSL

To use domain-specific language models (DSL Models) fit make users enjoy di app more because e dey give special and relevant talk. Dis model dey train or fine-tune to sabi and generate text wey relate to di specific field, industry, or topic. You fit train one from scratch, use pre-existing ones through SDKs and APIs, or fine-tune existing pre-trained model for di domain.

## Customization: Fine-tuning

Fine-tuning dey important when di pre-trained model no dey do well for di specific domain or task.

For example, medical questions dey complex and need plenty context. When doctor dey diagnose patient, e dey based on many things like lifestyle, pre-existing conditions, and even recent medical journals. For dis kind case, general-purpose AI chat app no go fit give reliable answer.

### Scenario: Medical App

Imagine chat app wey dey help doctors quick check treatment guidelines, drug interactions, or recent research.

General-purpose model fit answer basic medical questions or give general advice, but e go struggle for di following:

- **Complex cases**. For example, neurologist fit ask di app, "Wetin be di best way to manage drug-resistant epilepsy for children?"
- **Recent advancements**. General-purpose model fit no sabi di latest update for neurology and pharmacology.

For dis kind case, fine-tuning di model with medical dataset go make am better to handle di complex medical questions well. You go need big and relevant dataset wey represent di domain-specific wahala and questions.

## Things to Consider for Better AI Chat Experience

Dis section go show di things wey make chat app better, including di metrics wey you go track and di framework wey go make sure say di AI dey work responsibly.

### Key Metrics

To make sure say di app dey perform well, you go need to dey track di key metrics and considerations. Dis measurements dey help you check di functionality of di app, di quality of di AI model, and di user experience. Di list wey dey below show di basic, AI, and user experience metrics wey you go consider.

| Metric                        | Wetin e mean                                                                                                         | Wetin di Chat Developer go consider                                       |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Uptime**                    | Di time wey di app dey work and users fit access am.                                                                 | How you go reduce downtime?                                               |
| **Response Time**             | Di time wey di app dey take reply user question.                                                                     | How you go make query processing fast?                                    |
| **Precision**                 | Di ratio of true positive predictions to di total number of positive predictions.                                    | How you go check di precision of your model?                              |
| **Recall (Sensitivity)**      | Di ratio of true positive predictions to di actual number of positives.                                              | How you go measure and improve recall?                                    |
| **F1 Score**                  | Di harmonic mean of precision and recall, wey dey balance di two.                                                    | Wetin be your target F1 Score? How you go balance precision and recall?   |
| **Perplexity**                | E dey measure how di probability distribution wey di model predict dey match di actual distribution of di data.       | How you go reduce perplexity?                                             |
| **User Satisfaction Metrics** | E dey measure how users dey feel about di app. Dem dey usually collect am through survey.                            | How often you go collect user feedback? How you go use am improve?        |
| **Error Rate**                | Di rate wey di model dey make mistake for understanding or output.                                                   | Wetin be your plan to reduce error rate?                                  |
| **Retraining Cycles**         | How often di model dey update to add new data and insights.                                                          | How often you go retrain di model? Wetin go trigger retraining cycle?     |
| **Anomaly Detection**         | Tools and techniques wey dey help find patterns wey no follow wetin we expect.                        | How you go take handle anomalies?                                        |

### How to Use Responsible AI Practices for Chat Apps

Microsoft don talk say dem get six principles wey go guide how AI go dey develop and how we go use am. Below na the principles, wetin dem mean, wetin chat app developers suppose think about, and why e dey important.

| Principles             | Wetin Microsoft Talk About Am                                | Wetin Chat Developer Suppose Do                                      | Why E Matter                                                                     |
| ---------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Fairness               | AI systems suppose dey treat everybody well.            | Make sure say the chat app no dey do discrimination based on user data.  | To make users trust am and make everybody feel welcome; e go also help avoid wahala for law.                |
| Reliability and Safety | AI systems suppose dey work well and dey safe.        | Do testing and put things wey go stop errors and risks.         | E go make users happy and stop any harm wey fit happen.                                 |
| Privacy and Security   | AI systems suppose dey secure and respect privacy.      | Use strong encryption and protect user data well.              | To keep user data safe and follow privacy laws.                         |
| Inclusiveness          | AI systems suppose dey help everybody and involve people. | Design UI/UX wey everybody fit use, no matter who dem be. | E go make sure say plenty people fit use the app well.                   |
| Transparency           | AI systems suppose dey easy to understand.                  | Give clear documentation and explain how AI dey give answers.            | Users go trust the system more if dem sabi how e dey work. |
| Accountability         | People suppose dey responsible for AI systems.          | Put process wey go dey check and improve AI decisions.     | E go help make the system better and correct mistakes if dem happen.               |

## Assignment

Check [assignment](../../../07-building-chat-applications/python). E go carry you go through different exercises from how to run your first chat prompts, to how to classify and summarize text and more. You go see say the assignments dey available for different programming languages!

## Good Job! Continue to Learn More

After you finish this lesson, go check our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue to sabi more about Generative AI!

Go Lesson 8 to see how you fit start [building search applications](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transle-shon service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transle-shon. Even as we dey try make am correct, abeg make you sabi say transle-shon wey machine do fit get mistake or no dey accurate well. Di original dokyument for di language wey dem write am first na di one wey you go take as di correct one. For any important mata, e good make you use professional human transle-shon. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transle-shon.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->