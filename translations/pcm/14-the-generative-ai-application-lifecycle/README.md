[![Integrating with function calling](../../../translated_images/pcm/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Di Generative AI Application Lifecycle

One kain important question for all AI applications na how relevant AI features dey, as AI na field wey dey change quick quick. To sure say your application go remain relevant, reliable, and strong, you go need dey monitor, evaluate, and improve am sharp sharp. Na dia di generative AI lifecycle come enter.

Di generative AI lifecycle na framework wey dey guide you through the stages of how to develop, deploy, and maintain generative AI application. E go help you define your goals, measure how you dey perform, find your wahala dem, and put your solution dem for ground. E go also help you make sure say your application dey follow ethical and legal standard of your area and the people wey get interest. If you follow di generative AI lifecycle, you fit sure say your application go always dey give value and make your users happy.

## Introduction

For dis chapter, you go:

- Understand di Paradigm Shift from MLOps go LLMOps
- Di LLM Lifecycle
- Lifecycle Tooling
- Lifecycle Metrification and Evaluation

## Understand di Paradigm Shift from MLOps go LLMOps

LLMs na new tool for Artificial Intelligence arsenal, dem strong well well for analysis and generation tasks for applications, but dis power get how e change how we dey do AI and Classic Machine Learning tasks.

Because of dis, we need new Paradigm to adapt dis tool proper proper, we fit call old AI apps as "ML Apps" and new AI Apps as "GenAI Apps" or just "AI Apps", wey show di mainstream technology and techniques wey dem dey use that time. Dis one change our talk for plenty ways, check di comparison below.

![LLMOps vs. MLOps comparison](../../../translated_images/pcm/01-llmops-shift.29bc933cb3bb0080.webp)

Notice say for LLMOps, we dey focus more on App Developers, we dey use integrations as key point, we dey use "Models-as-a-Service" and dey reason these points for metrics.

- Quality: How di response quality be
- Harm: Responsible AI
- Honesty: If di response get grounding (E make sense? E correct?)
- Cost: How much di Solution go cost
- Latency: How long e dey take to respond average

## Di LLM Lifecycle

First, to understand di lifecycle and how e don change, make we look di infographic next.

![LLMOps infographic](../../../translated_images/pcm/02-llmops.70a942ead05a7645.webp)

As you fit notice, dis one different from di normal Lifecycles wey di MLOps get. LLMs get plenty new requirements like Prompting, different ways to improve quality (Fine-Tuning, RAG, Meta-Prompts), different way to check and responsibility with responsible AI, plus new evaluation metrics (Quality, Harm, Honesty, Cost and Latency).

For example, look how we dey come up with ideas. We dey use prompt engineering to try different LLMs to see which one fit test if their Hypothesis correct.

Note say dis no be linear process, but na loops wey dey integrated, iterative with one big overall cycle.

How we fit explore those steps? Make we look detail on how we fit build lifecycle.

![LLMOps Workflow](../../../translated_images/pcm/03-llm-stage-flows.3a1e1c401235a6cf.webp)

This one fit look small complicated, but make we start to focus on di three big steps first.

1. Ideating/Exploring: Dis na exploration, here we fit explore based on our business needs. We dey prototype, create [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) and test if e dey efficient for our Hypothesis.
1. Building/Augmenting: Implementation, now, we start to evaluate for bigger datasets, apply techniques like Fine-tuning and RAG, to check how strong our solution be. If e no work, we fit re-implement am, add new steps, or restructure di data. After testing, if e work well and di Metrics dey okay, e ready for next step.
1. Operationalizing: Integration, now we dey add Monitoring and Alerts system to our system, deployment and application integration inside our Application.

Then, we get the big managing cycle, we dey focus on security, compliance and governance.

Congrats, now your AI App ready to run and dey operational. If you want try am yourself, check di [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)

Now, which tools we fit use?

## Lifecycle Tooling

For tooling, Microsoft provide [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) and [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) wey make your cycle easy to implement and ready sharp sharp.

[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst), allow you to use [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst). Microsoft Foundry (wey before dem dey call Azure AI Studio) na web portal wey let you explore models, samples and tools, manage your resources, and use UI development flows plus SDK/CLI options for Code-First development.

![Azure AI possibilities](../../../translated_images/pcm/04-azure-ai-platform.80203baf03a12fa8.webp)

Azure AI, allow you manage multiple resources, operations, services, projects, vector search and databases wey you need.

![LLMOps with Azure AI](../../../translated_images/pcm/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

Build from Proof-of-Concept (POC) go big scale applications with PromptFlow:

- Design and Build apps from VS Code, using visual and functional tools
- Test and fine-tune your apps for quality AI, quick and easy.
- Use Microsoft Foundry to Integrate and Iterate with cloud, Push and Deploy fast fast for quick integration.

![LLMOps with PromptFlow](../../../translated_images/pcm/06-llm-promptflow.a183eba07a3a7fdf.webp)

## Correct! Continue your Learning!

Nice one, now learn more about how we fit structure application to use the concepts with [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), to see how Cloud Advocacy add those concepts for demonstrations. For more content, check our [Ignite breakout session!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Now, check Lesson 15, to sabi how [Retrieval Augmented Generation and Vector Databases](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) take affect Generative AI and how you fit make Applications dey more interesting!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->