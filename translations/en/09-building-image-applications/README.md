<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T18:56:51+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "en"
}
-->
# Building Image Generation Applications

There's more to LLMs than text generation. It's also possible to generate images from text descriptions. Having images as a modality can be highly useful in a number of areas from MedTech, architecture, tourism, game development, and more. In this chapter, we will look into the two most popular image generation models, DALL-E and Midjourney.

## Introduction

In this lesson, we will cover:

- Image generation and why it's useful.
- DALL-E and Midjourney, what they are, and how they work.
- How you would build an image generation app.

## Learning Goals

After completing this lesson, you will be able to:

- Build an image generation application.
- Define boundaries for your application with meta prompts.
- Work with DALL-E and Midjourney.

## Why build an image generation application?

Image generation applications are a great way to explore the capabilities of Generative AI. They can be used for, for example:

- **Image editing and synthesis**. You can generate images for a variety of use cases, such as image editing and image synthesis.

- **Applied to a variety of industries**. They can also be used to generate images for a variety of industries like Medtech, Tourism, Game development, and more.

## Scenario: Edu4All

As part of this lesson, we will continue to work with our startup, Edu4All. The students will create images for their assessments; exactly what images is up to the students, but they could be illustrations for their own fairytale, create a new character for their story, or help them visualize their ideas and concepts.

Here's what Edu4All's students could generate, for example, if they're working in class on monuments:

using a prompt like

> "Dog next to Eiffel Tower in early morning sunlight"

## What is DALL-E and Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) and [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) are two of the most popular image generation models. They allow you to use prompts to generate images.

### DALL-E

Let's start with DALL-E, which is a Generative AI model that generates images from text descriptions.

- **CLIP** is a model that generates embeddings, which are numerical representations of data, from images and text.

- **Diffused attention** is a model that generates images from embeddings. DALL-E is trained on a dataset of images and text and can be used to generate images from text descriptions. For example, DALL-E can be used to generate images of a cat in a hat, or a dog with a mohawk.

### Midjourney

Midjourney works in a similar way to DALL-E; it generates images from text prompts. Midjourney can also be used to generate images using prompts like “a cat in a hat”, or a “dog with a mohawk”.

## How does DALL-E and Midjourney Work

First, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E is a Generative AI model based on the transformer architecture with an _autoregressive transformer_.

An _autoregressive transformer_ defines how a model generates images from text descriptions. It generates one pixel at a time and then uses the generated pixels to generate the next pixel, passing through multiple layers in a neural network until the image is complete.

With this process, DALL-E controls attributes, objects, characteristics, and more in the image it generates. However, DALL-E 2 and 3 have more control over the generated image.

## Building your first image generation application

So what does it take to build an image generation application? You need the following libraries:

- **python-dotenv**, you're highly recommended to use this library to keep your secrets in a _.env_ file away from the code.
- **openai**, this library is what you will use to interact with the OpenAI API.
- **pillow**, to work with images in Python.
- **requests**, to help you make HTTP requests.

1. Create a file _.env_ with the following content:

   Locate this information in Azure Portal for your resource in the "Keys and Endpoint" section.

1. Collect the above libraries in a file called _requirements.txt_ like so:

1. Next, create a virtual environment and install the libraries:

   For Windows, use the following commands to create and activate your virtual environment:

1. Add the following code in a file called _app.py_:

Let's explain this code:

- First, we import the libraries we need, including the OpenAI library, the dotenv library, the requests library, and the Pillow library.

- Next, we load the environment variables from the _.env_ file.

- After that, we set the endpoint, key for the OpenAI API, version, and type.

- Next, we generate the image:

  The above code responds with a JSON object that contains the URL of the generated image. We can use the URL to download the image and save it to a file.

- Lastly, we open the image and use the standard image viewer to display it:

### More details on generating the image

Let's look at the code that generates the image in more detail:

- **prompt** is the text prompt that is used to generate the image. In this case, we're using the prompt "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils".
- **size** is the size of the image that is generated. In this case, we're generating an image that is 1024x1024 pixels.
- **n** is the number of images that are generated. In this case, we're generating two images.
- **temperature** is a parameter that controls the randomness of the output of a Generative AI model. The temperature is a value between 0 and 1 where 0 means that the output is deterministic and 1 means that the output is random. The default value is 0.7.

There are more things you can do with images that we will cover in the next section.

## Additional capabilities of image generation

You've seen so far how we were able to generate an image using a few lines in Python. However, there are more things you can do with images.

You can also do the following:

- **Perform edits**. By providing an existing image, a mask, and a prompt, you can alter an image. For example, you can add something to a portion of an image. Imagine our bunny image; you can add a hat to the bunny. How you would do that is by providing the image, a mask (identifying the part of the area for the change), and a text prompt to say what should be done.

  The base image would only contain the rabbit, but the final image would have the hat on the rabbit.

- **Create variations**. The idea is that you take an existing image and ask that variations are created. To create a variation, you provide an image and a text prompt and code like so:

  > Note, this is only supported on OpenAI

## Temperature

Temperature is a parameter that controls the randomness of the output of a Generative AI model. The temperature is a value between 0 and 1 where 0 means that the output is deterministic and 1 means that the output is random. The default value is 0.7.

Let's look at an example of how temperature works by running this prompt twice:

> Prompt: "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

Now let's run that same prompt just to see that we won't get the same image twice:

As you can see, the images are similar, but not the same. Let's try changing the temperature value to 0.1 and see what happens:

### Changing the temperature

So let's try to make the response more deterministic. We could observe from the two images we generated that in the first image, there's a bunny, and in the second image, there's a horse, so the images vary greatly.

Let's therefore change our code and set the temperature to 0, like so:

Now when you run this code, you get these two images:

Here you can clearly see how the images resemble each other more.

## How to define boundaries for your application with metaprompts

With our demo, we can already generate images for our clients. However, we need to create some boundaries for our application.

For example, we don't want to generate images that are not safe for work, or that are not appropriate for children.

We can do this with _metaprompts_. Metaprompts are text prompts that are used to control the output of a Generative AI model. For example, we can use metaprompts to control the output and ensure that the generated images are safe for work or appropriate for children.

### How does it work?

Now, how do meta prompts work?

Meta prompts are text prompts that are used to control the output of a Generative AI model. They are positioned before the text prompt and are used to control the output of the model, embedded in applications to control the output of the model. Encapsulating the prompt input and the meta prompt input in a single text prompt.

One example of a meta prompt would be the following:

Now, let's see how we can use meta prompts in our demo.

From the above prompt, you can see how all images being created consider the metaprompt.

## Assignment - let's enable students

We introduced Edu4All at the beginning of this lesson. Now it's time to enable the students to generate images for their assessments.

The students will create images for their assessments containing monuments; exactly what monuments is up to the students. The students are asked to use their creativity in this task to place these monuments in different contexts.

## Solution

Here's one possible solution:

## Great Work! Continue Your Learning

After completing this lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue leveling up your Generative AI knowledge!

Head over to Lesson 10 where we will look at how to [build AI applications with low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Disclaimer**:  
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.