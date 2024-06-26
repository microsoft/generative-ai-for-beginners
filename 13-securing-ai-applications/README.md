# Securing Your Generative AI Applications

[![Securing Your Generative AI Applications](./images/13-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson13-gh?WT.mc_id=academic-105485-koreyst)

## Introduction

This lesson will cover:

- Security within the context of AI systems.
- Common risks and threats to AI systems.
- Methods and considerations for securing AI systems.

## Learning Goals

After completing this lesson, you will have an understanding of:

- The threats and risks to AI systems.
- Common methods and practices for securing AI systems.
- How implementing security testing can prevent unexpected results and erosion of user trust.

## What does security mean within the context of generative AI?

As Artificial Intelligence (AI) and Machine Learning (ML) technologies increasingly shape our lives, it’s crucial to protect not only customer data but also the AI systems themselves. AI/ML is increasingly used in support of high-value decision-making processes in industries where the wrong decision may result in serious consequences.

Here are key points to consider:

- **Impact of AI/ML**: AI/ML have significant impacts on daily life and as such safeguarding them has become essential.
- **Security Challenges**: This impact that AI/ML has needs proper attention in order to address the need to protect AI-based products from sophisticated attacks, whether by trolls or organized groups.
- **Strategic Problems**: The tech industry must proactively address strategic challenges to ensure long-term customer safety and data security.

Additionally, Machine Learning models are largely unable to discern between malicious input and benign anomalous data. A significant source of training data is derived from uncurated, unmoderated, public datasets, which are open to 3rd-party contributions. Attackers don’t need to compromise datasets when they're free to contribute to them. Over time, low-confidence malicious data becomes high-confidence trusted data, if the data structure/formatting remains correct.

This is why it is critical to ensure the integrity and protection of the data stores your models use to make decisions with.

## Understanding the threats and risks of AI

In terms of AI and related systems, data poisoning stands out as the most significant security threat today. Data poisoning is when someone intentionally changes the information used to train an AI, causing it to make mistakes. This is due to the absence of standardized detection and mitigation methods, coupled with our reliance on untrusted or uncurated public datasets for training. To maintain data integrity and prevent a flawed training process, it is crucial to track the origin and lineage of your data. Otherwise, the old adage “garbage in, garbage out” holds true, leading to compromised model performance.

Here are examples of how data poisoning can affect your models:

1. **Label Flipping**: In a binary classification task, an adversary intentionally flips the labels of a small subset of training data. For instance, benign samples are labeled as malicious, leading the model to learn incorrect associations.\
   **Example**: A spam filter misclassifying legitimate emails as spam due to manipulated labels.
2. **Feature Poisoning**: An attacker subtly modifies features in the training data to introduce bias or mislead the model.\
   **Example**: Adding irrelevant keywords to product descriptions to manipulate recommendation systems.
3. **Data Injection**: Injecting malicious data into the training set to influence the model’s behavior.\
   **Example**: Introducing fake user reviews to skew sentiment analysis results.
4. **Backdoor Attacks**: An adversary inserts a hidden pattern (backdoor) into the training data. The model learns to recognize this pattern and behaves maliciously when triggered.\
   **Example**: A face recognition system trained with backdoored images that misidentifies a specific person.

The MITRE Corporation has created [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), a knowledgebase of tactics and techniques employed by adversaries in real-world attacks on AI systems.

> There are a growing number of vulnerabilities in AI-enabled systems, as the incorporation of AI increases the attack surface of existing systems beyond those of traditional cyber-attacks. We developed ATLAS to raise awareness of these unique and evolving vulnerabilities, as the global community increasingly incorporates AI into various systems. ATLAS is modeled after the MITRE ATT&CK® framework and its tactics, techniques, and procedures (TTPs) are complementary to those in ATT&CK.

Much like the MITRE ATT&CK® framework, which is extensively used in traditional cybersecurity for planning advanced threat emulation scenarios, ATLAS provides an easily searchable set TTPs that can help to better understand and prepare for defending against emerging attacks.

Additionally, the Open Web Application Security Project (OWASP) has created a "[Top 10 list](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" of the most critical vulnerabilities found in applications utilizing LLMs. The list highlights the risks of threats such as the aforementioned data poisoning along with others such as:

- **Prompt Injection**: a technique where attackers manipulate a Large Language Model (LLM) through carefully crafted inputs, causing it to behave outside of its intended behavior.
- **Supply Chain Vulnerabilities**: The components and software that make up the applications used by an LLM, such as Python modules or external datasets, can themselves be compromised leading to unexpected results, introduced biases and even vulnerabilities in the underlying infrastructure.
- **Overreliance**: LLMs are fallible and have been prone to hallucinate, providing inaccurate or unsafe results. In several documented circumstances, people have taken the results at face value leading to unintended real-world negative consequences.

Microsoft Cloud Advocate Rod Trent has written a free ebook, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), that dives deeply into these and other emerging AI threats and provides extensive guidance on how to best tackle these scenarios.

## Security Testing for AI Systems and LLMs

Artificial intelligence (AI) is transforming various domains and industries, offering new possibilities and benefits for society. However, AI also poses significant challenges and risks, such as data privacy, bias, lack of explainability, and potential misuse. Therefore, it is crucial to ensure that AI systems are secure and responsible, meaning that they adhere to ethical and legal standards and can be trusted by users and stakeholders.

Security testing is the process of evaluating the security of an AI system or LLM, by identifying and exploiting their vulnerabilities. This can be performed by developers, users, or third-party auditors, depending on the purpose and scope of the testing. Some of the most common security testing methods for AI systems and LLMs are:

- **Data sanitization**: This is the process of removing or anonymizing sensitive or private information from the training data or the input of an AI system or LLM. Data sanitization can help prevent data leakage and malicious manipulation by reducing the exposure of confidential or personal data.
- **Adversarial testing**: This is the process of generating and applying adversarial examples to the input or output of an AI system or LLM to evaluate its robustness and resilience against adversarial attacks. Adversarial testing can help identify and mitigate the vulnerabilities and weaknesses of an AI system or LLM that may be exploited by attackers.
- **Model verification**: This is the process of verifying the correctness and completeness of the model parameters or architecture of an AI system or LLM. Model verification can help detect and prevent model stealing by ensuring that the model is protected and authenticated.
- **Output validation**: This is the process of validating the quality and reliability of the output of an AI system or LLM. Output validation can help detect and correct malicious manipulation by ensuring that the output is consistent and accurate.

OpenAI, a leader in AI systems, has setup a series of _safety evaluations_ as part of their red teaming network initiative, aimed at testing the output AI systems in the hopes of contributing to AI safety.

> Evaluations can range from simple Q&A tests to more-complex simulations. As concrete examples, here are sample evaluations developed by OpenAI for evaluating AI behaviors from a number of angles:

#### Persuasion

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): How well can an AI system trick another AI system into saying a secret word?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): How well can an AI system convince another AI system to donate money?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): How well can an AI system influence another AI system’s support of a political proposition?

#### Steganography (hidden messaging)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): How well can an AI system ​​pass secret messages without being caught by another AI system?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): How well can an AI system compress and decompress messages, to enable hiding secret messages?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): How well can an AI system coordinate with another AI system, without direct communication?

### AI Security

It's imperative that we aim to protect AI systems from malicious attacks, misuse, or unintended consequences. This includes taking steps to ensure the safety, reliability, and trustworthiness of AI systems, such as:

- Securing the data and algorithms that are used to train and run AI models
- Preventing unauthorized access, manipulation, or sabotage of AI systems
- Detecting and mitigating bias, discrimination, or ethical issues in AI systems
- Ensuring the accountability, transparency, and explainability of AI decisions and actions
- Aligning the goals and values of AI systems with those of humans and society

AI security is important for ensuring the integrity, availability, and confidentiality of AI systems and data. Some of the challenges and opportunities of AI security are:

- Opportunity: Incorporating AI in cybersecurity strategies since it can play a crucial role in identifying threats and improving response times. AI can help automate and augment the detection and mitigation of cyberattacks, such as phishing, malware, or ransomware.
- Challenge: AI can also be used by adversaries to launch sophisticated attacks, such as generating fake or misleading content, impersonating users, or exploiting vulnerabilities in AI systems. Therefore, AI developers have a unique responsibility to design systems that are robust and resilient against misuse.

### Data Protection

LLMs can pose risks to the privacy and security of the data that they use. For example, LLMs can potentially memorize and leak sensitive information from their training data, such as personal names, addresses, passwords, or credit card numbers. They can also be manipulated or attacked by malicious actors who want to exploit their vulnerabilities or biases. Therefore, it is important to be aware of these risks and take appropriate measures to protect the data used with LLMs. There are several steps that you can take to protect the data that is used with LLMs. These steps include:

- **Limiting the amount and type of data that they share with LLMs**: Only share the data that is necessary and relevant for the intended purposes, and avoid sharing any data that is sensitive, confidential, or personal. Users should also anonymize or encrypt the data that they share with LLMs, such as by removing or masking any identifying information, or using secure communication channels.
- **Verifying the data that LLMs generate**: Always check the accuracy and quality of the output generated by LLMs to ensure they don't contain any unwanted or inappropriate information.
- **Reporting and alerting any data breaches or incidents**: Be vigilant of any suspicious or abnormal activities or behaviors from LLMs, such as generating texts that are irrelevant, inaccurate, offensive, or harmful. This could be an indication of a data breach or security incident.

Data security, governance, and compliance are critical for any organization that wants to leverage the power of data and AI in a multi-cloud environment. Securing and governing all your data is a complex and multifaceted undertaking. You need to secure and govern different types of data (structured, unstructured, and data generated by AI) in different locations across multiple clouds, and you need to account for existing and future data security, governance, and AI regulations. To protect your data, you need to adopt some best practices and precautions, such as:

- Use cloud services or platforms that offer data protection and privacy features.
- Use data quality and validation tools to check your data for errors, inconsistencies, or anomalies.
- Use data governance and ethics frameworks to ensure your data is used in a responsible and transparent manner.

### Emulating real-world threats - AI red teaming

Emulating real-world threats is now considered a standard practice in building resilient AI systems by employing similar tools, tactics, procedures to identify the risks to systems and test the response of defenders.

> The practice of AI red teaming has evolved to take on a more expanded meaning: it not only covers probing for security vulnerabilities, but also includes probing for other system failures, such as the generation of potentially harmful content. AI systems come with new risks, and red teaming is core to understanding those novel risks, such as prompt injection and producing ungrounded content. - [Microsoft AI Red Team building future of safer AI](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

[![Guidance and resources for red teaming](./images/13-AI-red-team.png?WT.mc_id=academic-105485-koreyst)]()

Below are key insights that have shaped Microsoft’s AI Red Team program.

1. **Expansive Scope of AI Red Teaming:**
   AI red teaming now encompasses both security and Responsible AI (RAI) outcomes. Traditionally, red teaming focused on security aspects, treating the model as a vector (e.g., stealing the underlying model). However, AI systems introduce novel security vulnerabilities (e.g., prompt injection, poisoning), necessitating special attention. Beyond security, AI red teaming also probes fairness issues (e.g., stereotyping) and harmful content (e.g., glorification of violence). Early identification of these issues allows prioritization of defense investments.
2. **Malicious and Benign Failures:**
   AI red teaming considers failures from both malicious and benign perspectives. For example, when red teaming the new Bing, we explore not only how malicious adversaries can subvert the system but also how regular users may encounter problematic or harmful content. Unlike traditional security red teaming, which focuses mainly on malicious actors, AI red teaming accounts for a broader range of personas and potential failures.
3. **Dynamic Nature of AI Systems:**
   AI applications constantly evolve. In large language model applications, developers adapt to changing requirements. Continuous red teaming ensures ongoing vigilance and adaptation to evolving risks.

AI red teaming is not all encompassing and should be considered a complementary motion to additional controls such as [role-based access control (RBAC)](https://learn.microsoft.com/azure/ai-services/openai/how-to/role-based-access-control?WT.mc_id=academic-105485-koreyst) and comprehensive data management solutions. It's meant to supplement a security strategy that focuses on employing safe and responsible AI solutions that account for privacy and security while aspiring to minimize biases, harmful content and misinformation that can erode user confidence.

Here's a list of additional reading that can help you better understand how red teaming can help identify and mitigate risks in your AI systems:

- [Planning red teaming for large language models (LLMs) and their applications](https://learn.microsoft.com/azure/ai-services/openai/concepts/red-teaming?WT.mc_id=academic-105485-koreyst)
- [What is the OpenAI Red Teaming Network?](https://openai.com/blog/red-teaming-network?WT.mc_id=academic-105485-koreyst)
- [AI Red Teaming - A Key Practice for Building Safer and More Responsible AI Solutions](https://rodtrent.substack.com/p/ai-red-teaming?WT.mc_id=academic-105485-koreyst)
- MITRE [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), a knowledgebase of tactics and techniques employed by adversaries in real-world attacks on AI systems.

## Knowledge check

What could be a good approach to maintaining data integrity and preventing misuse?

1. Have strong role-based controls for data access and data management
1. Implement and audit data labeling to prevent data misrepresentation or misuse
1. Ensure your AI infrastructure supports content filtering

A:1, While all three are great recommendations, ensuring that you're assigning the proper data access privileges to users will go a long way to preventing manipulation and misrepresentation of the data used by LLMs.

## 🚀 Challenge

Read up more on how you can [govern and protect sensitive information](https://learn.microsoft.com/training/paths/purview-protect-govern-ai/?WT.mc_id=academic-105485-koreyst) in the age of AI.

## Great Work, Continue Your Learning

After completing this lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue leveling up your Generative AI knowledge!

Head over to Lesson 14 where we will look at [the Generative AI Application Lifecycle](../14-the-generative-ai-application-lifecycle/README.md?WT.mc_id=academic-105485-koreyst)!
