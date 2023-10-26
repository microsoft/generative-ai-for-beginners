# Using Generative AI Responsibly 

[![Using Generative AI Responsibly ](./images/genai_course_3[77].png)]() 

**Video Coming Soon** 


## Learning Goals 

After completing this lesson you will know: 
- The importance of Responsible AI when building Generative AI applications. 
- When to think and apply the core principles of Responsible AI during your application building process. 
- What tools and strategies are available to you to put the concept of Responsible AI into practice. 


## Responsible AI Principles 

The excitement of Generative AI has never been higher. This excitement has brought a lot of new developers, attention and funding to this space. While this is very positive for anyone looking to build products and companies using Generative AI, it is also important we proceed responsibly. 

Throughout this course we are focusing on building our startup and our AI education product. Let's look at the principles of Responsible AI and how they relate to our use of Generative AI in our products. 


## Why Should You Prioritise Responsible AI 

When building product, taking a human centric approach by keeping your users best interest in mind leads to the best results. 

The uniqueness of Generative AI is its power to create helpful answers, information, guidance and content for users. This can be done without many manual steps which can lead to very impressive results. Without proper planning and strategies, it can also unfortunately lead to some harmful results both for your users, your product and society as a whole. 

Let's look at some (but not all) of these potentially harmful results: 

### Hallucinations 

Hallucinations are a term used to describe when an LLM produces content that is either completely nonsensical or something we know is factually wrong based on other sources of information. 

Let's take for example we build a feature for our startup that allows students to ask historical questions to a model. A student asks the question `Who was the sole surivor of Titanic?`

The model produces a a response like the one below:


![](/03-using-generative-ai-responsibly%20/images/2135-ChatGPT(1)_11zon.webp)

*(Source: https://flyingbisons.com)*

This is a very confident and thorough answer. Unfortunately, it is incorrect. Even with a minimal amount of research, one would discover there was more than one survivor of the Titantic survivor. For a student that is just starting to research this topic, this answer can be persuasive enough to not be questioned and treated as fact. 

With each iteration of any given LLM we have seen performance improvements around minimising hallucinations. Even with this improvement,  we as applications builders and users still need to remain aware of these limitations. 


### Harmful Content 

We covered in the earlier section when a LLM produces incorrect or nonsensical responses.  Another risk we need to be aware of is when a model responds with harmful content. 

Harmful content can be defined as: 
- Providing instructions or encouraging self harm or harm to certain groups 
- Hateful or demeaning content 
- Providing guidance on planning any type of attack or violent acts
- Providing instructions on how to find illegal content or commit illegal acts 

For our startup, we want to make sure we have the right tools and strategies in place to prevent this type of content from being seen to students. 

### Lack of Fairness 

Fairness is defined as "ensuring that an AI system is free from bias and discrimination and that they treat everyone fairly and equally."  In the world of Generative AI, that exclusionary worldviews of marginalised groups are not reinforced by the model's output. 

These type of outputs are not only harmful to build positive product experiences for our users, they also cause further societal harm. As application builders, we should always keep a wide and diverse user base in mind when building solutions with Generative AI. 

## How to Use Generative AI Responsibly 

Now that we have identified the importance of Responsible Generative AI, let's look at 4 steps we can do to build our AI solutions responsibly: 

![Mitigate Cycle](./images/mitigate-cycle.png)



### Identify Potential Harms 

In the earlier section we discussed some of the potential harms when building a Generative AI Solution. These harms can change based on the services and the models you are using. Using techniques such as fine-tuning or grounding your data that provides a higher level control on the model's output should also be considered when listing potential harms. 

In this course, we will be building applications for our startups that generates images, text, chat responses and API calls to external services. Each of these applications come with their own unique set of potential harms.


### Measure Potential Harms 


### Mitigate Potential Harms 


### Operate a responsible generative AI solution

You will see as we build our startup we can use Generative AI to create text applications, new images,  improve search results, create better chat experiences and integrate it with other parts of our application.



## Tools and Strategies for Responsible AI 


### Creating Mitigation Layers
![Mitigation Layers](./images/mitigation-layers.png)



**Model**


**Safety System**


**Metaprompt**


**User Experience**

### Adversarial Testing 



### Azure AI Content Safety 


https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview  


```python 
# Create an Content Safety client
    client = ContentSafetyClient(endpoint, AzureKeyCredential(key))

    # Build request
    with open(image_path, "rb") as file:
        request = AnalyzeImageOptions(image=ImageData(content=file.read()))

    # Analyze image
    try:
        response = client.analyze_image(request)
    except HttpResponseError as e:
        print("Analyze image failed.")
        if e.error:
            print(f"Error code: {e.error.code}")
            print(f"Error message: {e.error.message}")
            raise
        print(e)
        raise

    if response.hate_result:
        print(f"Hate severity: {response.hate_result.severity}")
    if response.self_harm_result:
        print(f"SelfHarm severity: {response.self_harm_result.severity}")
    if response.sexual_result:
        print(f"Sexual severity: {response.sexual_result.severity}")
    if response.violence_result:
        print(f"Violence severity: {response.violence_result.severity}")

    # [END analyze_image]

```


## Great Work, Continue Your Learning! 


Want to learn more about how to build with Generative AI responsibly? Go to the [contiuned learning page](../13-continued-learning/README.md) to find other great resources on this topic.


Head over to the Lesson 4 where we will look at [Prompt Engineering Fundamentals](/4-prompt-engineering-fundamentals/README.md)!

