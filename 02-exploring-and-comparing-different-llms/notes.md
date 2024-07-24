## Types of Large Language Models (LLMs) for Use

**Text Generation Models** Most LLMs are designed for text generation, with a variety of options available, including GPT-3.5 and GPT-4. These models differ in capabilities and costs, with GPT-4 being the most expensive. Evaluating models through platforms like the Azure OpenAI Playground can help determine which model best fits your needs regarding capability and cost.

**Open Source LLMs**
We will be using open-source LLM models. Some popular examples include:
- Alpaca
- Bloom
- LLaMA

**Text and Code Generation Models**
These models can generate both text and code, often used for tasks such as text summarization, translation, and question answering. Text generation models are typically trained on large datasets like BookCorpus and can generate new text or answer questions. Code generation models, like CodeParrot, are trained on datasets from sources like GitHub and can generate new code or fix existing bugs.

**Future Considerations | Services for Production Use**
Services optimized for production use often provide a graphical user interface (GUI) and ease of use. However, they may not always be free and might require a subscription or payment, leveraging the service owner's resources. For example, Azure OpenAI Service offers a pay-as-you-go rate plan, providing enterprise-grade security and a responsible AI framework.

**Exploring the LLM Landscape | Testing and Iteration**
Once potential models are identified, the next step involves testing them on specific data and workloads. This is an iterative process involving experiments and measurements. Models such as OpenAI’s offerings, open-source models like LLaMA2, and Hugging Face transformers are available in the Model Catalog in Azure AI Studio.

**Azure AI Studio**
Azure AI Studio is a cloud platform designed for developers to build generative AI applications and manage the entire development lifecycle, from experimentation to evaluation, through a single hub. The Model Catalog in Azure AI Studio offers:
- A comprehensive GUI
- Integration of all Azure AI services

Approaches to Deploying LLMs

Prompt Engineering with Context
Pre-trained LLMs are effective for generalized natural language tasks with minimal input, known as “zero-shot” learning. More accurate results can be achieved by providing detailed requests and examples:

One-shot learning: Includes one example in the prompt
Few-shot learning: Includes multiple examples in the prompt
Prompt engineering with context is the most cost-effective approach to start with.

Retrieval Augmented Generation (RAG)
LLMs are limited to the data used during training, lacking knowledge of events post-training or non-public information. RAG overcomes this by augmenting prompts with external data, such as document chunks, supported by vector database tools like Azure Vector Search. This technique is useful when:
- There is insufficient data to fine-tune an LLM
- There is limited time or resources
- The goal is to improve performance on specific tasks and reduce risks of generating false or harmful content