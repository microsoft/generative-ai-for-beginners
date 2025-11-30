<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "78bbeed50fd4dc9fdee931f5daf98cb3",
  "translation_date": "2025-10-17T22:29:42+00:00",
  "source_file": "12-designing-ux-for-ai-applications/README.md",
  "language_code": "en"
}
-->
# Designing UX for AI Applications

[![Designing UX for AI Applications](../../../translated_images/12-lesson-banner.c53c3c7c802e8f563953ce388f6a987ca493472c724d924b060be470951c53c8.en.png)](https://youtu.be/VKbCejSICA8?si=MKj7GQYHfXRZyWW6)

> _(Click the image above to view the video of this lesson)_

User experience is a crucial aspect of app development. Users need to be able to use your app efficiently to complete tasks. Efficiency is important, but it's equally vital to design apps that are accessible to everyone. This chapter focuses on this area, aiming to help you design an app that people can and want to use.

## Introduction

User experience refers to how a user interacts with and utilizes a specific product or service, whether it's a system, tool, or design. When developing AI applications, developers must focus not only on creating an effective user experience but also on ensuring it is ethical. In this lesson, we explore how to build Artificial Intelligence (AI) applications that address user needs.

The lesson will cover the following topics:

- Introduction to User Experience and Understanding User Needs
- Designing AI Applications for Trust and Transparency
- Designing AI Applications for Collaboration and Feedback

## Learning Goals

After completing this lesson, you will be able to:

- Understand how to create AI applications that meet user needs.
- Design AI applications that foster trust and collaboration.

### Prerequisite

Take some time to read more about [user experience and design thinking.](https://learn.microsoft.com/training/modules/ux-design?WT.mc_id=academic-105485-koreyst)

## Introduction to User Experience and Understanding User Needs

In our fictional education startup, we have two primary users: teachers and students. Each of these users has unique needs. A user-centered design prioritizes the user, ensuring the products are relevant and beneficial for their intended audience.

The application should be **useful, reliable, accessible, and pleasant** to deliver a good user experience.

### Usability

Being useful means the application has functionality that aligns with its intended purpose, such as automating the grading process or generating flashcards for revision. For example, an application designed to automate grading should accurately and efficiently assign scores to students' work based on predefined criteria. Similarly, an application that generates revision flashcards should create relevant and diverse questions based on its data.

### Reliability

Being reliable means the application can consistently perform its tasks without errors. However, like humans, AI is not perfect and may encounter errors. Applications may face unexpected situations requiring human intervention or correction. How do you handle errors? In the final section of this lesson, we will discuss designing AI systems and applications for collaboration and feedback.

### Accessibility

Being accessible means extending the user experience to individuals with diverse abilities, including those with disabilities, ensuring inclusivity. By adhering to accessibility guidelines and principles, AI solutions become more inclusive, usable, and beneficial for all users.

### Pleasant

Being pleasant means the application is enjoyable to use. A positive user experience can encourage users to return to the application, ultimately boosting business revenue.

![image illustrating UX considerations in AI](../../../translated_images/uxinai.d5b4ed690f5cefff0c53ffcc01b480cdc1828402e1fdbc980490013a3c50935a.en.png)

Not every challenge can be solved with AI. AI enhances user experience, whether by automating manual tasks or personalizing user interactions.

## Designing AI Applications for Trust and Transparency

Building trust is essential when designing AI applications. Trust ensures users feel confident that the application will perform tasks effectively, deliver consistent results, and meet their needs. However, there are risks of mistrust and overtrust. Mistrust occurs when users lack confidence in an AI system, leading them to reject the application. Overtrust happens when users overestimate the capabilities of an AI system, potentially relying on it too much. For instance, in the case of an automated grading system, overtrust might lead a teacher to skip reviewing some papers, which could result in unfair or inaccurate grades for students or missed opportunities for feedback and improvement.

Two key ways to prioritize trust in design are explainability and control.

### Explainability

When AI informs decisions, such as imparting knowledge to future generations, it is crucial for teachers and parents to understand how AI decisions are made. Explainability refers to understanding how AI applications arrive at their decisions. Designing for explainability involves providing details that clarify how AI generates its output. Users must be aware that the output is produced by AI, not a human. For example, instead of saying "Start chatting with your tutor now," you could say, "Use an AI tutor that adapts to your needs and helps you learn at your pace."

![an app landing page with clear illustration of explainability in AI applications](../../../translated_images/explanability-in-ai.134426a96b498fbfdc80c75ae0090aedc0fc97424ae0734fccf7fb00a59a20d9.en.png)

Another example is how AI uses user and personal data. For instance, a student persona may have limitations based on their role. The AI might not reveal answers to questions but could guide the user in thinking through how to solve a problem.

![AI replying to questions based on persona](../../../translated_images/solving-questions.b7dea1604de0cbd2e9c5fa00b1a68a0ed77178a035b94b9213196b9d125d0be8.en.png)

A crucial aspect of explainability is simplifying explanations. Since students and teachers may not be AI experts, explanations of the application's capabilities and limitations should be clear and easy to understand.

![simplified explanations on AI capabilities](../../../translated_images/simplified-explanations.4679508a406c3621fa22bad4673e717fbff02f8b8d58afcab8cb6f1aa893a82f.en.png)

### Control

Generative AI fosters collaboration between AI and users, allowing users to modify prompts for different results. Additionally, once an output is generated, users should be able to adjust the results, giving them a sense of control. For example, when using Bing, users can tailor their prompts based on format, tone, and length. They can also make changes to the output, as shown below:

![Bing search results with options to modify the prompt and output](../../../translated_images/bing1.293ae8527dbe2789b675c8591c9fb3cb1aa2ada75c2877f9aa9edc059f7a8b1c.en.png)

Another feature in Bing that provides users control over the application is the ability to opt in and opt out of the data AI uses. For instance, a student might want to use their notes along with the teacher's resources as study material.

![Bing search results with options to modify the prompt and output](../../../translated_images/bing2.309f4845528a88c28c1c9739fb61d91fd993dc35ebe6fc92c66791fb04fceb4d.en.png)

> When designing AI applications, intentionality is key to ensuring users do not overtrust the system and set unrealistic expectations of its capabilities. One way to achieve this is by creating friction between prompts and results, reminding users that the system is AI, not a human.

## Designing AI Applications for Collaboration and Feedback

As mentioned earlier, generative AI fosters collaboration between users and AI. Most interactions involve users providing prompts and AI generating outputs. But what happens if the output is incorrect? How does the application handle errors? Does the AI blame the user or explain the error?

AI applications should be designed to receive and provide feedback. This not only helps the AI system improve but also builds trust with users. A feedback loop should be integrated into the design, such as a simple thumbs-up or thumbs-down option for the output.

Another way to address this is by clearly communicating the system's capabilities and limitations. If a user makes an error by requesting something beyond the AI's capabilities, the application should handle this appropriately, as shown below.

![Giving feedback and handling errors](../../../translated_images/feedback-loops.7955c134429a94663443ad74d59044f8dc4ce354577f5b79b4bd2533f2cafc6f.en.png)

System errors are common in applications, especially when users need information outside the AI's scope or when the application has limitations on the number of questions or subjects it can handle. For example, an AI application trained on limited subjects like History and Math may not be able to answer questions about Geography. To address this, the AI system could respond with: "Sorry, our product has been trained with data in the following subjects... I cannot respond to the question you asked."

AI applications are not perfect, so they are bound to make mistakes. When designing your applications, ensure you create opportunities for user feedback and implement error handling in a simple and understandable way.

## Assignment

Take any AI apps you've built so far and consider implementing the following steps in your app:

- **Pleasant:** Think about how you can make your app more enjoyable to use. Are you providing clear explanations? Are you encouraging users to explore? How are you phrasing your error messages?

- **Usability:** If you're building a web app, ensure it is navigable using both a mouse and a keyboard.

- **Trust and transparency:** Avoid relying entirely on AI and its output. Consider how you can incorporate human verification into the process. Also, explore and implement other ways to build trust and transparency.

- **Control:** Allow users to control the data they provide to the application. Implement options for users to opt in and opt out of data collection in the AI application.

<!-- ## [Post-lecture quiz](../../../12-designing-ux-for-ai-applications/quiz-url) -->

## Continue Your Learning!

After completing this lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue enhancing your knowledge of Generative AI!

Head over to Lesson 13, where we will explore [securing AI applications](../13-securing-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.