<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b9d32511b27373a1b21b5789d4fda057",
  "translation_date": "2025-10-17T22:33:11+00:00",
  "source_file": "14-the-generative-ai-application-lifecycle/README.md",
  "language_code": "en"
}
-->
[![Integrating with function calling](../../../translated_images/14-lesson-banner.066d74a31727ac121eeac06376a068a397d8e335281e63ce94130d11f516e46b.en.png)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# The Generative AI Application Lifecycle

A key question for all AI applications is the relevance of AI features, especially in a rapidly evolving field. To ensure your application remains relevant, reliable, and robust, you need to continuously monitor, evaluate, and improve it. This is where the generative AI lifecycle comes into play.

The generative AI lifecycle is a framework that guides you through the stages of developing, deploying, and maintaining a generative AI application. It helps you define your goals, measure performance, identify challenges, and implement solutions. It also ensures your application aligns with the ethical and legal standards of your domain and stakeholders. By following the generative AI lifecycle, you can ensure your application consistently delivers value and meets user expectations.

## Introduction

In this chapter, you will:

- Understand the Paradigm Shift from MLOps to LLMOps
- Learn about the LLM Lifecycle
- Explore Lifecycle Tooling
- Dive into Lifecycle Metrics and Evaluation

## Understand the Paradigm Shift from MLOps to LLMOps

LLMs are a powerful addition to the Artificial Intelligence toolkit, excelling in analysis and generation tasks for applications. However, this power brings changes to how we approach AI and traditional machine learning tasks.

To adapt to this new tool, we need a fresh paradigm with appropriate incentives. Older AI applications can be categorized as "ML Apps," while newer ones can be referred to as "GenAI Apps" or simply "AI Apps," reflecting the prevailing technologies and techniques of the time. This shift changes the narrative in several ways, as illustrated in the comparison below.

![LLMOps vs. MLOps comparison](../../../translated_images/01-llmops-shift.29bc933cb3bb0080a562e1655c0c719b71a72c3be6252d5c564b7f598987e602.en.png)

In LLMOps, the focus shifts more towards app developers, emphasizing integrations, "Models-as-a-Service," and metrics such as:

- Quality: Response quality
- Harm: Responsible AI
- Honesty: Response accuracy and reliability
- Cost: Budget for the solution
- Latency: Average response time per token

## The LLM Lifecycle

To understand the lifecycle and its modifications, take a look at the infographic below.

![LLMOps infographic](../../../translated_images/02-llmops.70a942ead05a7645db740f68727d90160cb438ab71f0fb20548bc7fe5cad83ff.en.png)

As you can see, this differs from traditional MLOps lifecycles. LLMs introduce new requirements, such as prompt engineering, techniques to enhance quality (e.g., fine-tuning, RAG, meta-prompts), responsible AI considerations, and new evaluation metrics (quality, harm, honesty, cost, and latency).

For example, during the ideation phase, prompt engineering is used to experiment with various LLMs to test hypotheses and explore possibilities.

This process is not linear but involves integrated loops, iterative steps, and an overarching cycle.

How can we explore these steps? Let’s break down the lifecycle into detailed stages.

![LLMOps Workflow](../../../translated_images/03-llm-stage-flows.3a1e1c401235a6cfa886ed6ba04aa52a096a545e1bc44fa54d7d5983a7201892.en.png)

While this may seem complex, we can simplify it into three main steps:

1. Ideating/Exploring: This is the exploration phase, where you identify business needs, prototype, create a [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst), and test the efficiency of your hypothesis.
2. Building/Augmenting: This is the implementation phase, where you evaluate larger datasets and apply techniques like fine-tuning and RAG to ensure the robustness of your solution. If the solution doesn’t meet expectations, you can re-implement, add new steps to your flow, or restructure the data. Once the flow and scale are tested and metrics are validated, the solution is ready for the next step.
3. Operationalizing: This is the integration phase, where you add monitoring and alert systems, deploy the solution, and integrate it into your application.

Finally, there is an overarching management cycle focused on security, compliance, and governance.

Congratulations! Your AI app is now ready to be operational. For hands-on experience, check out the [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

Now, let’s explore the tools you can use.

## Lifecycle Tooling

For tooling, Microsoft offers the [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) and [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) to simplify and streamline the implementation of your lifecycle.

The [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) includes [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys), a web portal that allows you to explore models, samples, and tools, manage resources, develop user interfaces, and use SDK/CLI options for code-first development.

![Azure AI possibilities](../../../translated_images/04-azure-ai-platform.80203baf03a12fa8b166e194928f057074843d1955177baf0f5b53d50d7b6153.en.png)

Azure AI provides various resources to manage operations, services, projects, vector searches, and database needs.

![LLMOps with Azure AI](../../../translated_images/05-llm-azure-ai-prompt.a5ce85cdbb494bdf95420668e3464aae70d8b22275a744254e941dd5e73ae0d2.en.png)

From proof-of-concept (POC) to large-scale applications, PromptFlow enables you to:

- Design and build apps directly from VS Code using visual and functional tools
- Test and fine-tune your apps for high-quality AI with ease
- Use Azure AI Studio to integrate and iterate with the cloud, push updates, and deploy for quick integration

![LLMOps with PromptFlow](../../../translated_images/06-llm-promptflow.a183eba07a3a7fdf4aa74db92a318b8cbbf4a608671f6b166216358d3203d8d4.en.png)

## Great! Continue your Learning!

Fantastic! Now, dive deeper into how to structure an application using these concepts with the [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst) and see how Cloud Advocacy incorporates these ideas into demonstrations. For more content, check out our [Ignite breakout session!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Next, proceed to Lesson 15 to learn about [Retrieval Augmented Generation and Vector Databases](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) and how they can enhance Generative AI applications!

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.