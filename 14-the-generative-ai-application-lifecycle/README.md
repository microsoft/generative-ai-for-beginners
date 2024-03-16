# The Generative AI Application Lifecycle

An important question for all AI applications is the relevance of AI features, as AI is a fast evolving field, to ensure that your application remains relevant, reliable, and robust, you need to monitor, evaluate, and improve it continuously. This is where the generative AI lifecycle comes in.

The generative AI lifecycle is a framework that guides you through the stages of developing, deploying, and maintaining a generative AI application. It helps you to define your goals, measure your performance, identify your challenges, and implement your solutions. It also helps you to align your application with the ethical and legal standards of your domain and your stakeholders. By following the generative AI lifecycle, you can ensure that your application is always delivering value and satisfying your users.

## Introduction

In this chapter, you will:

- Understand the Paradigm Shift from MLOps to LLMOps
- The LLM Lifecycle
- Lifecycle Tooling
- Lifecycle Metrification and Evaluation

## Understand the Paradigm Shift from MLOps to LLMOps

LLMs are a new tool in the Artificial Intelligence arsenal, they are incredibly powerful in analysis and generation tasks for applications, however this power has some consequences in how we streamline AI and Classic Machine Learning tasks.

With this, we need a new Paradigm to adapt this tool in a dynamic, with the correct incentives. We can categorize older AI apps as "ML Apps" and newer AI Apps as "GenAI Apps" or just "AI Apps", reflecting the mainstream technology and techniques used at the time. This shifts our narrative in multiple ways, look at the following comparison.

![LLMOps vs. MLOps comparison](./images/01-llmops-shift.png?WT.mc_id=academic-105485-koreys)

Notice that in LLMOps, we are more focused in the App Developers, using integrations as a key point, using "Models-as-a-Service" and thinking in the following points for metrics.

- Quality: Response quality
- Harm: Responsible AI
- Honesty: Response groundness (Makes sense? It is correct?)
- Cost: Solution Budget
- Latency: Avg. time for token response

## The LLM Lifecycle

First, to understand the lifecycle and the modifications, let's note the next infographic.

![LLMOps infographic](./images/02-llmops.png?WT.mc_id=academic-105485-koreys)

As you may note, this is different from the usual Lifecycles from MLOps. LLMs have many new requirements, as Prompting, different tecniques to improve quality (Fine-Tuning, RAG, Meta-Prompts), different assessment and responsability with responsible AI, lastly, new evaluation metrics (Quality, Harm, Honesty, Cost and Latency).

For instance, take a look how we ideate. Using prompt engineering to experiment with various LLMs to explore possibilities to tests if their Hypothesis could be correct.

Note that this is not linear, but integrated loops, iterative and with an overacrching cycle.

How could we explore those steps? Let's step into detail in how could we build a lifecycle.

![LLMOps Workflow](./images/03-llm-stage-flows.png?WT.mc_id=academic-105485-koreys)

This may look a bit complicated, lets focus on the three big steps first.

1. Ideating/Exploring: Exploration, here we can explore according to our business needs. Prototyping, creating a [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) and test if is efficient enough for our Hypothesis.
1. Building/Augmenting: Implementation, now, we start to evaluate for bigger datasets implement techniques, like Fine-tuning and RAG, to check the robustness of out solution. If it does not, re-implementing it, adding new steps in our flow or restructuring the data, might help. After testing our flow and our scale, if it works and check our Metrics, it is ready for the next step.
1. Operationalizing: Integration, now adding Monitoring and Alerts Systems to our system, deployment and application integration to our Application.

Then, we have the overarching cycle of Management, focusing on security, compliance and governance.

Congratulations, now you have your AI App ready to go and operational. For a hands on experience, take a look on the [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

Now, what tools could we use?

## Lifecycle Tooling

For Tooling, Microsoft provides the [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) and [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) facilitate and make your cycle easy to implement and ready to go.

The [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys), allows you to use [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys). AI Studio is a web portal allows you to Explore models, samples and tools. Managing your resources, UI development flows and SDK/CLI options for Code-First development.

![Azure AI possibilities](./images/04-azure-ai-platform.png?WT.mc_id=academic-105485-koreys)

Azure AI, allows you to use multiple resources, to manage your operations, services, projects, vector search and databases needs.

![LLMOps with Azure AI](./images/05-llm-azure-ai-prompt.png?WT.mc_id=academic-105485-koreys)

Construct, from Proof-of-Concept(POC) until large scale applications with PromptFlow:

- Design and Build apps from VS Code, with visual and functional tools
- Test and fine-tune your apps for quality AI, with ease.
- Use Azure AI Studio to Integrate and Iterate with cloud, Push and Deploy for quick integration.

![LLMOps with PromptFlow](./images/06-llm-promptflow.png?WT.mc_id=academic-105485-koreys)

## Great! Continue your Learning!

Amazing, now learn more how we structure an application to use the concepts with the [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), to check how Cloud Advocacy adds those concepts in demonstations. For more content, check our [Ignite breakout session!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Now, check Lesson 15, to understand how [Retrieval Augmented Generation and Vector Databases](#) impact Generative AI and to make more engaging Applications!
