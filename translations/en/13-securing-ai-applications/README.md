<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2faf8ee7a0b851efa647a19788f1e5b",
  "translation_date": "2025-10-17T22:30:35+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "en"
}
-->
# Securing Your Generative AI Applications

[![Securing Your Generative AI Applications](../../../translated_images/13-lesson-banner.14103e36b4bbf17398b64ed2b0531f6f2c6549e7f7342f797c40bcae5a11862e.en.png)](https://youtu.be/m0vXwsx5DNg?si=TYkr936GMKz15K0L)

## Introduction

This lesson will cover:

- Security in the context of AI systems.
- Common risks and threats to AI systems.
- Methods and considerations for securing AI systems.

## Learning Goals

After completing this lesson, you will understand:

- The threats and risks to AI systems.
- Common methods and practices for securing AI systems.
- How implementing security testing can prevent unexpected outcomes and loss of user trust.

## What does security mean within the context of generative AI?

As Artificial Intelligence (AI) and Machine Learning (ML) technologies increasingly influence our lives, it’s essential to protect not only customer data but also the AI systems themselves. AI/ML is increasingly used to support high-stakes decision-making in industries where errors can have serious consequences.

Key points to consider:

- **Impact of AI/ML**: AI/ML significantly affect daily life, making their protection essential.
- **Security Challenges**: The influence of AI/ML requires attention to safeguard AI-based products from sophisticated attacks, whether from trolls or organized groups.
- **Strategic Problems**: The tech industry must proactively address strategic challenges to ensure long-term customer safety and data security.

Additionally, Machine Learning models often cannot distinguish between malicious input and benign anomalous data. A significant portion of training data comes from uncurated, unmoderated, public datasets, which are open to third-party contributions. Attackers don’t need to compromise datasets when they can freely contribute to them. Over time, low-confidence malicious data can become high-confidence trusted data if the data structure/formatting remains correct.

This is why ensuring the integrity and protection of the data stores your models rely on is critical.

## Understanding the threats and risks of AI

In the realm of AI and related systems, data poisoning is currently the most significant security threat. Data poisoning occurs when someone deliberately alters the information used to train an AI, causing it to make errors. This threat is exacerbated by the lack of standardized detection and mitigation methods and the reliance on untrusted or uncurated public datasets for training. To maintain data integrity and prevent flawed training processes, it is essential to track the origin and lineage of your data. Otherwise, the saying “garbage in, garbage out” applies, leading to compromised model performance.

Examples of how data poisoning can impact your models:

1. **Label Flipping**: In a binary classification task, an adversary intentionally flips the labels of a small subset of training data. For example, benign samples are labeled as malicious, causing the model to learn incorrect associations.\
   **Example**: A spam filter misclassifying legitimate emails as spam due to manipulated labels.
2. **Feature Poisoning**: An attacker subtly alters features in the training data to introduce bias or mislead the model.\
   **Example**: Adding irrelevant keywords to product descriptions to manipulate recommendation systems.
3. **Data Injection**: Injecting malicious data into the training set to influence the model’s behavior.\
   **Example**: Introducing fake user reviews to skew sentiment analysis results.
4. **Backdoor Attacks**: An adversary embeds a hidden pattern (backdoor) into the training data. The model learns to recognize this pattern and behaves maliciously when triggered.\
   **Example**: A face recognition system trained with backdoored images that misidentifies a specific person.

The MITRE Corporation has developed [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), a knowledge base of tactics and techniques used by adversaries in real-world attacks on AI systems.

> There are increasing vulnerabilities in AI-enabled systems, as incorporating AI expands the attack surface of existing systems beyond traditional cyber-attacks. ATLAS was developed to raise awareness of these unique and evolving vulnerabilities as the global community increasingly integrates AI into various systems. Modeled after the MITRE ATT&CK® framework, ATLAS’s tactics, techniques, and procedures (TTPs) complement those in ATT&CK.

Similar to the MITRE ATT&CK® framework, widely used in traditional cybersecurity for planning advanced threat emulation scenarios, ATLAS provides an easily searchable set of TTPs to better understand and prepare for defending against emerging attacks.

Additionally, the Open Web Application Security Project (OWASP) has created a "[Top 10 list](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" of the most critical vulnerabilities in applications using LLMs. This list highlights risks such as data poisoning and other threats, including:

- **Prompt Injection**: A technique where attackers manipulate a Large Language Model (LLM) through carefully crafted inputs, causing it to act outside its intended behavior.
- **Supply Chain Vulnerabilities**: The components and software that make up applications using an LLM, such as Python modules or external datasets, can be compromised, leading to unexpected results, introduced biases, and vulnerabilities in the underlying infrastructure.
- **Overreliance**: LLMs are fallible and prone to hallucinations, providing inaccurate or unsafe results. In documented cases, people have accepted these results at face value, leading to unintended negative consequences in the real world.

Microsoft Cloud Advocate Rod Trent has authored a free ebook, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), which explores these and other emerging AI threats in depth and offers extensive guidance on addressing these scenarios.

## Security Testing for AI Systems and LLMs

Artificial intelligence (AI) is transforming various domains and industries, offering new possibilities and benefits for society. However, AI also presents significant challenges and risks, such as data privacy, bias, lack of explainability, and potential misuse. Therefore, it is crucial to ensure that AI systems are secure and responsible, meaning they adhere to ethical and legal standards and can be trusted by users and stakeholders.

Security testing involves evaluating the security of an AI system or LLM by identifying and exploiting vulnerabilities. This can be conducted by developers, users, or third-party auditors, depending on the purpose and scope of the testing. Common security testing methods for AI systems and LLMs include:

- **Data sanitization**: Removing or anonymizing sensitive or private information from the training data or input of an AI system or LLM. This helps prevent data leakage and malicious manipulation by reducing exposure to confidential or personal data.
- **Adversarial testing**: Generating and applying adversarial examples to the input or output of an AI system or LLM to evaluate its robustness and resilience against adversarial attacks. This helps identify and mitigate vulnerabilities and weaknesses that attackers might exploit.
- **Model verification**: Verifying the correctness and completeness of the model parameters or architecture of an AI system or LLM. This helps detect and prevent model theft by ensuring the model is protected and authenticated.
- **Output validation**: Validating the quality and reliability of the output of an AI system or LLM. This helps detect and correct malicious manipulation by ensuring the output is consistent and accurate.

OpenAI, a leader in AI systems, has established a series of _safety evaluations_ as part of their red teaming network initiative, aimed at testing AI system outputs to contribute to AI safety.

> Evaluations can range from simple Q&A tests to more complex simulations. Here are sample evaluations developed by OpenAI to assess AI behaviors from various perspectives:

#### Persuasion

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): How well can an AI system trick another AI system into saying a secret word?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): How well can an AI system convince another AI system to donate money?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): How well can an AI system influence another AI system’s support of a political proposition?

#### Steganography (hidden messaging)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): How well can an AI system pass secret messages without being detected by another AI system?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): How well can an AI system compress and decompress messages to enable hidden communication?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): How well can an AI system coordinate with another AI system without direct communication?

### AI Security

It is crucial to protect AI systems from malicious attacks, misuse, or unintended consequences. This includes ensuring the safety, reliability, and trustworthiness of AI systems by:

- Securing the data and algorithms used to train and operate AI models.
- Preventing unauthorized access, manipulation, or sabotage of AI systems.
- Detecting and mitigating bias, discrimination, or ethical issues in AI systems.
- Ensuring accountability, transparency, and explainability of AI decisions and actions.
- Aligning the goals and values of AI systems with those of humans and society.

AI security is essential for maintaining the integrity, availability, and confidentiality of AI systems and data. Some challenges and opportunities in AI security include:

- Opportunity: Integrating AI into cybersecurity strategies, as it can help identify threats and improve response times. AI can automate and enhance the detection and mitigation of cyberattacks, such as phishing, malware, or ransomware.
- Challenge: Adversaries can also use AI to launch sophisticated attacks, such as generating fake or misleading content, impersonating users, or exploiting vulnerabilities in AI systems. Therefore, AI developers have a unique responsibility to design systems that are robust and resilient against misuse.

### Data Protection

LLMs can pose risks to the privacy and security of the data they use. For example, LLMs may memorize and leak sensitive information from their training data, such as personal names, addresses, passwords, or credit card numbers. They can also be manipulated or attacked by malicious actors seeking to exploit their vulnerabilities or biases. It is essential to recognize these risks and take measures to protect the data used with LLMs. Steps to safeguard data include:

- **Limiting the amount and type of data shared with LLMs**: Share only necessary and relevant data for the intended purposes, and avoid sharing sensitive, confidential, or personal data. Users should also anonymize or encrypt the data they share with LLMs, such as by removing or masking identifying information or using secure communication channels.
- **Verifying the data generated by LLMs**: Always check the accuracy and quality of the output generated by LLMs to ensure it does not contain unwanted or inappropriate information.
- **Reporting and alerting any data breaches or incidents**: Be vigilant for any suspicious or abnormal activities or behaviors from LLMs, such as generating irrelevant, inaccurate, offensive, or harmful texts. These could indicate a data breach or security incident.

Data security, governance, and compliance are critical for organizations leveraging the power of data and AI in a multi-cloud environment. Securing and governing all data is a complex and multifaceted task. Organizations must secure and govern various types of data (structured, unstructured, and AI-generated) across multiple locations and clouds, while accounting for current and future data security, governance, and AI regulations. Best practices for data protection include:

- Using cloud services or platforms with data protection and privacy features.
- Employing data quality and validation tools to identify errors, inconsistencies, or anomalies in data.
- Adopting data governance and ethics frameworks to ensure responsible and transparent data usage.

### Emulating real-world threats - AI red teaming
Emulating real-world threats is now considered a standard practice in building resilient AI systems by using similar tools, tactics, and procedures to identify system risks and test defenders' responses.

> The practice of AI red teaming has evolved to take on a broader meaning: it not only involves probing for security vulnerabilities but also includes identifying other system failures, such as generating potentially harmful content. AI systems bring new risks, and red teaming is essential for understanding these novel risks, such as prompt injection and producing ungrounded content. - [Microsoft AI Red Team building future of safer AI](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

[![Guidance and resources for red teaming](../../../translated_images/13-AI-red-team.642ed54689d7e8a4d83bdf0635768c4fd8aa41ea539d8e3ffe17514aec4b4824.en.png)]()

Below are key insights that have shaped Microsoft’s AI Red Team program.

1. **Expanded Scope of AI Red Teaming:**
   AI red teaming now addresses both security and Responsible AI (RAI) outcomes. Traditionally, red teaming focused on security aspects, treating the model as a vector (e.g., stealing the underlying model). However, AI systems introduce new security vulnerabilities (e.g., prompt injection, poisoning), requiring special attention. Beyond security, AI red teaming also examines fairness issues (e.g., stereotyping) and harmful content (e.g., glorification of violence). Identifying these issues early helps prioritize defense investments.

2. **Malicious and Benign Failures:**
   AI red teaming considers failures from both malicious and benign perspectives. For instance, when red teaming the new Bing, we investigate not only how malicious actors might exploit the system but also how regular users might encounter problematic or harmful content. Unlike traditional security red teaming, which primarily focuses on malicious actors, AI red teaming takes into account a wider range of personas and potential failures.

3. **Dynamic Nature of AI Systems:**
   AI applications are constantly evolving. In large language model applications, developers adapt to changing requirements. Continuous red teaming ensures ongoing vigilance and adaptation to emerging risks.

AI red teaming is not a standalone solution and should be viewed as a complementary approach alongside other controls such as [role-based access control (RBAC)](https://learn.microsoft.com/azure/ai-services/openai/how-to/role-based-access-control?WT.mc_id=academic-105485-koreyst) and comprehensive data management solutions. It is designed to supplement a security strategy that prioritizes safe and responsible AI solutions, addressing privacy and security while aiming to reduce biases, harmful content, and misinformation that could undermine user trust.

Here’s a list of additional resources to help you better understand how red teaming can identify and mitigate risks in your AI systems:

- [Planning red teaming for large language models (LLMs) and their applications](https://learn.microsoft.com/azure/ai-services/openai/concepts/red-teaming?WT.mc_id=academic-105485-koreyst)
- [What is the OpenAI Red Teaming Network?](https://openai.com/blog/red-teaming-network?WT.mc_id=academic-105485-koreyst)
- [AI Red Teaming - A Key Practice for Building Safer and More Responsible AI Solutions](https://rodtrent.substack.com/p/ai-red-teaming?WT.mc_id=academic-105485-koreyst)
- MITRE [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), a knowledge base of tactics and techniques used by adversaries in real-world attacks on AI systems.

## Knowledge check

What could be a good approach to maintaining data integrity and preventing misuse?

1. Have strong role-based controls for data access and data management  
1. Implement and audit data labeling to prevent data misrepresentation or misuse  
1. Ensure your AI infrastructure supports content filtering  

A:1, While all three are great recommendations, ensuring that you're assigning the proper data access privileges to users will go a long way in preventing manipulation and misrepresentation of the data used by LLMs.

## 🚀 Challenge

Learn more about how you can [govern and protect sensitive information](https://learn.microsoft.com/training/paths/purview-protect-govern-ai/?WT.mc_id=academic-105485-koreyst) in the age of AI.

## Great Work, Continue Your Learning

After completing this lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue enhancing your knowledge of Generative AI!

Move on to Lesson 14, where we will explore [the Generative AI Application Lifecycle](../14-the-generative-ai-application-lifecycle/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.