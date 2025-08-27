<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "747668e4c53d067369f06e9ec2e6313e",
  "translation_date": "2025-08-26T13:24:07+00:00",
  "source_file": "12-designing-ux-for-ai-applications/README.md",
  "language_code": "en"
}
-->
# Designing UX for AI Applications

[![Designing UX for AI Applications](../../../translated_images/12-lesson-banner.c53c3c7c802e8f563953ce388f6a987ca493472c724d924b060be470951c53c8.en.png)](https://aka.ms/gen-ai-lesson12-gh?WT.mc_id=academic-105485-koreyst)

> _(Click the image above to view video of this lesson)_

User experience is a crucial part of building apps. Users need to be able to use your app efficiently to get things done. Efficiency is important, but you also need to design apps so that everyone can use them, making them _accessible_. This chapter focuses on this area so you can design an app that people can and want to use.

## Introduction

User experience is how a user interacts with and uses a specific product or service, whether it's a system, tool, or design. When developing AI applications, developers focus not only on making the user experience effective but also ethical. In this lesson, we cover how to build Artificial Intelligence (AI) applications that address user needs.

The lesson will cover the following areas:

- Introduction to User Experience and Understanding User Needs
- Designing AI Applications for Trust and Transparency
- Designing AI Applications for Collaboration and Feedback

## Learning goals

After taking this lesson, you'll be able to:

- Understand how to build AI applications that meet user needs.
- Design AI applications that promote trust and collaboration.

### Prerequisite

Take some time to read more about [user experience and design thinking.](https://learn.microsoft.com/training/modules/ux-design?WT.mc_id=academic-105485-koreyst)

## Introduction to User Experience and Understanding User Needs

In our fictional education startup, we have two main users: teachers and students. Each of these users has unique needs. A user-centered design puts the user first, making sure the products are relevant and helpful for those they're meant for.

The application should be **useful, reliable, accessible, and pleasant** to provide a good user experience.

### Usability

Being useful means the application has features that match its intended purpose, like automating grading or generating flashcards for studying. An app that automates grading should accurately and efficiently assign scores to students' work based on set criteria. Similarly, an app that creates revision flashcards should be able to generate relevant and varied questions from its data.

### Reliability

Being reliable means the application can do its job consistently and without errors. However, AI, like humans, isn't perfect and can make mistakes. The applications might run into errors or unexpected situations that need human help or correction. How do you handle errors? In the last section of this lesson, we'll cover how AI systems and applications are designed for collaboration and feedback.

### Accessibility

Being accessible means making the user experience available to users with different abilities, including those with disabilities, so no one is left out. By following accessibility guidelines and principles, AI solutions become more inclusive, usable, and helpful for all users.

### Pleasant

Being pleasant means the application is enjoyable to use. A good user experience can have a positive effect on the user, encouraging them to come back to the app and increasing business revenue.

![image illustrating UX considerations in AI](../../../translated_images/uxinai.d5b4ed690f5cefff0c53ffcc01b480cdc1828402e1fdbc980490013a3c50935a.en.png)

Not every problem can be solved with AI. AI is there to enhance your user experience, whether by automating manual tasks or personalizing user experiences.

## Designing AI Applications for Trust and Transparency

Building trust is essential when designing AI applications. Trust makes sure a user feels confident that the app will get the job done, deliver results consistently, and that the results are what the user needs. A risk here is mistrust and overtrust. Mistrust happens when a user has little or no trust in an AI system, leading them to reject your app. Overtrust happens when a user overestimates what an AI system can do, leading them to trust the AI too much. For example, with an automated grading system, overtrust might cause a teacher not to double-check some papers to make sure the grading system is working well. This could lead to unfair or inaccurate grades for students, or missed chances for feedback and improvement.

Two ways to make sure trust is central to your design are explainability and control.

### Explainability

When AI helps make decisions, like teaching future generations, it's important for teachers and parents to understand how AI decisions are made. This is explainability—understanding how AI applications make decisions. Designing for explainability means adding details that show how AI arrived at its output. The audience should know that the output is generated by AI, not a human. For example, instead of saying "Start chatting with your tutor now," say "Use an AI tutor that adapts to your needs and helps you learn at your pace."

![an app landing page with clear illustration of explainability in AI applications](../../../translated_images/explanability-in-ai.134426a96b498fbfdc80c75ae0090aedc0fc97424ae0734fccf7fb00a59a20d9.en.png)

Another example is how AI uses user and personal data. For instance, a user with the student persona may have limits based on their persona. The AI might not be able to reveal answers to questions but can help guide the user to think about how to solve a problem.

![AI replying to questions based on persona](../../../translated_images/solving-questions.b7dea1604de0cbd2e9c5fa00b1a68a0ed77178a035b94b9213196b9d125d0be8.en.png)

Another key part of explainability is making explanations simple. Students and teachers may not be AI experts, so explanations of what the app can or can't do should be simple and easy to understand.

![simplified explanations on AI capabilities](../../../translated_images/simplified-explanations.4679508a406c3621fa22bad4673e717fbff02f8b8d58afcab8cb6f1aa893a82f.en.png)

### Control

Generative AI creates a partnership between AI and the user, where, for example, a user can change prompts for different results. Also, once an output is generated, users should be able to change the results, giving them a sense of control. For example, when using Bing, you can adjust your prompt based on format, tone, and length. You can also make changes to your output and edit it as shown below:

![Bing search results with options to modify the prompt and output](../../../translated_images/bing1.293ae8527dbe2789b675c8591c9fb3cb1aa2ada75c2877f9aa9edc059f7a8b1c.en.png)

Another feature in Bing that gives users control over the app is the ability to opt in and out of the data AI uses. For a school app, a student might want to use their notes as well as the teacher's resources for studying.

![Bing search results with options to modify the prompt and output](../../../translated_images/bing2.309f4845528a88c28c1c9739fb61d91fd993dc35ebe6fc92c66791fb04fceb4d.en.png)

> When designing AI applications, being intentional is key to making sure users don't overtrust and set unrealistic expectations for what AI can do. One way to do this is by creating some friction between prompts and results. Remind the user that this is AI, not another human being.

## Designing AI Applications for Collaboration and Feedback

As mentioned earlier, generative AI creates a partnership between the user and AI. Most interactions involve a user entering a prompt and the AI generating an output. What if the output is wrong? How does the app handle errors if they happen? Does the AI blame the user or take time to explain the error?

AI applications should be built to receive and give feedback. This not only helps the AI system improve but also builds trust with users. A feedback loop should be included in the design; for example, a simple thumbs up or down on the output.

Another way to handle this is to clearly communicate the system's abilities and limitations. When a user makes a request that's beyond what the AI can do, there should be a way to handle this, as shown below.

![Giving feedback and handling errors](../../../translated_images/feedback-loops.7955c134429a94663443ad74d59044f8dc4ce354577f5b79b4bd2533f2cafc6f.en.png)

System errors are common in applications where the user might need help with information outside the AI's scope, or the app might limit how many questions or subjects a user can generate summaries for. For example, an AI app trained only on History and Math may not be able to answer questions about Geography. To handle this, the AI system can respond with something like: "Sorry, our product has been trained with data in the following subjects....., I can't answer the question you asked."

AI applications aren't perfect, so they're bound to make mistakes. When designing your apps, make sure you allow for user feedback and error handling in a way that's simple and easy to explain.

## Assignment

Take any AI apps you've built so far and consider adding the following steps to your app:

- **Pleasant:** Think about how you can make your app more enjoyable. Are you adding explanations everywhere? Are you encouraging users to explore? How are you writing your error messages?

- **Usability:** If you're building a web app, make sure your app can be navigated by both mouse and keyboard.

- **Trust and transparency:** Don't trust the AI and its output completely; think about how you could add a human to the process to verify the output. Also, consider and implement other ways to achieve trust and transparency.

- **Control:** Give users control over the data they provide to the app. Add a way for users to opt in and out of data collection in the AI application.

## Continue Your Learning!

After finishing this lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to keep building your Generative AI knowledge!

Head over to Lesson 13, where we'll look at how to [secure AI applications](../13-securing-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Disclaimer**:
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.