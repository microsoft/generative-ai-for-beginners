<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T10:33:00+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "zh"
}
-->
# 构建图像生成应用程序

除了文本生成，LLM还可以从文本描述中生成图像。图像作为一种模式在许多领域中都非常有用，如医疗技术、建筑、旅游、游戏开发等。在本章中，我们将探讨两个最受欢迎的图像生成模型，DALL-E和Midjourney。

## 介绍

在这节课中，我们将涵盖：

- 图像生成及其用途。
- DALL-E和Midjourney是什么，以及它们如何工作。
- 如何构建一个图像生成应用程序。

## 学习目标

完成本课程后，您将能够：

- 构建图像生成应用程序。
- 用元提示为您的应用程序定义边界。
- 使用DALL-E和Midjourney。

## 为什么要构建图像生成应用程序？

图像生成应用程序是探索生成式AI功能的绝佳方式。它们可以用于以下用途，例如：

- **图像编辑和合成**。您可以为各种用例生成图像，如图像编辑和图像合成。

- **应用于各种行业**。它们还可以用于生成各种行业的图像，如医疗技术、旅游、游戏开发等。

## 场景：Edu4All

作为本课程的一部分，我们将在本课中继续与我们的初创公司Edu4All合作。学生将为他们的评估创建图像，具体生成什么图像由学生决定，但他们可以为自己的童话故事创作插图，或为他们的故事创建新角色，或帮助他们可视化他们的想法和概念。

例如，如果Edu4All的学生正在课堂上学习纪念碑，他们可以生成如下内容：

使用类似这样的提示：

> “狗在清晨阳光下的埃菲尔铁塔旁”

## 什么是DALL-E和Midjourney？

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst)和[Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst)是两个最受欢迎的图像生成模型，它们允许您使用提示生成图像。

### DALL-E

让我们从DALL-E开始，它是一个生成式AI模型，可以从文本描述中生成图像。

> [DALL-E是两个模型的组合，CLIP和扩散注意力](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)。

- **CLIP**是一个生成嵌入的模型，即数据的数值表示，可以从图像和文本中生成。

- **扩散注意力**是一个从嵌入生成图像的模型。DALL-E在一个包含图像和文本的数据集上进行训练，可以用于从文本描述中生成图像。例如，DALL-E可以用于生成戴帽子的猫或莫霍克发型的狗的图像。

### Midjourney

Midjourney的工作方式与DALL-E类似，它从文本提示中生成图像。Midjourney也可以使用提示生成图像，如“戴帽子的猫”或“莫霍克发型的狗”。

## DALL-E和Midjourney如何工作

首先，[DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)。DALL-E是基于变压器架构的生成式AI模型，具有_自回归变压器_。

_自回归变压器_定义了模型如何从文本描述中生成图像，它一次生成一个像素，然后使用生成的像素生成下一个像素。通过神经网络中的多个层，直到图像完成。

通过这个过程，DALL-E控制生成图像中的属性、对象、特征等。然而，DALL-E 2和3对生成图像有更多的控制。

## 构建您的第一个图像生成应用程序

那么构建一个图像生成应用程序需要什么呢？您需要以下库：

- **python-dotenv**，强烈建议您使用此库将您的机密信息保存在_.env_文件中，远离代码。
- **openai**，这是您将用于与OpenAI API交互的库。
- **pillow**，用于在Python中处理图像。
- **requests**，帮助您进行HTTP请求。

1. 创建一个文件_.env_，内容如下：

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   在Azure门户中定位此信息，在“密钥和终结点”部分为您的资源找到。

1. 在一个名为_requirements.txt_的文件中收集上述库，如下所示：

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. 接下来，创建虚拟环境并安装库：

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   对于Windows，使用以下命令创建和激活您的虚拟环境：

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. 在一个名为_app.py_的文件中添加以下代码：

   ```python
   import openai
   import os
   import requests
   from PIL import Image
   import dotenv

   # import dotenv
   dotenv.load_dotenv()

   # Get endpoint and key from environment variables
   openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
   openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

   # Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
   openai.api_version = '2023-06-01-preview'
   openai.api_type = 'azure'


   try:
       # Create an image by using the image generation API
       generation_response = openai.Image.create(
           prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
           size='1024x1024',
           n=2,
           temperature=0,
       )
       # Set the directory for the stored image
       image_dir = os.path.join(os.curdir, 'images')

       # If the directory doesn't exist, create it
       if not os.path.isdir(image_dir):
           os.mkdir(image_dir)

       # Initialize the image path (note the filetype should be png)
       image_path = os.path.join(image_dir, 'generated-image.png')

       # Retrieve the generated image
       image_url = generation_response["data"][0]["url"]  # extract image URL from response
       generated_image = requests.get(image_url).content  # download the image
       with open(image_path, "wb") as image_file:
           image_file.write(generated_image)

       # Display the image in the default image viewer
       image = Image.open(image_path)
       image.show()

   # catch exceptions
   except openai.InvalidRequestError as err:
       print(err)

   ```

让我们解释这段代码：

- 首先，我们导入所需的库，包括OpenAI库、dotenv库、requests库和Pillow库。

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- 接下来，我们从_.env_文件中加载环境变量。

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- 然后，我们设置OpenAI API的终结点、密钥、版本和类型。

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- 接下来，我们生成图像：

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  上述代码响应一个包含生成图像URL的JSON对象。我们可以使用该URL下载图像并保存到文件中。

- 最后，我们打开图像并使用标准图像查看器显示它：

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### 生成图像的更多细节

让我们更详细地看一下生成图像的代码：

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**是用于生成图像的文本提示。在这种情况下，我们使用的提示是“骑马的兔子，拿着棒棒糖，在长满水仙花的雾蒙蒙的草地上”。
- **size**是生成图像的大小。在这种情况下，我们生成的图像是1024x1024像素。
- **n**是生成的图像数量。在这种情况下，我们生成两张图像。
- **temperature**是一个控制生成式AI模型输出随机性的参数。温度是一个介于0和1之间的值，其中0表示输出是确定性的，1表示输出是随机的。默认值是0.7。

在下一节中，我们将介绍更多您可以用图像做的事情。

## 图像生成的附加功能

到目前为止，您已经看到了如何使用几行Python代码生成图像。然而，您可以用图像做更多的事情。

您还可以执行以下操作：

- **进行编辑**。通过提供现有图像的蒙版和提示，您可以更改图像。例如，您可以向图像的一部分添加内容。想象一下我们的兔子图像，您可以给兔子加上帽子。您可以通过提供图像、蒙版（识别更改的部分区域）和文本提示来说明应该做什么来实现。

  ```python
  response = openai.Image.create_edit(
    image=open("base_image.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="An image of a rabbit with a hat on its head.",
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  基础图像只包含兔子，但最终图像将兔子戴上帽子。

- **创建变体**。这个想法是您获取现有图像并要求创建变体。要创建变体，您提供图像和文本提示，并编写代码如下：

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > 注意，这仅在OpenAI上支持

## 温度

温度是一个控制生成式AI模型输出随机性的参数。温度是一个介于0和1之间的值，其中0表示输出是确定性的，1表示输出是随机的。默认值是0.7。

让我们看一个温度如何工作的例子，通过运行这个提示两次：

> 提示：“骑马的兔子，拿着棒棒糖，在长满水仙花的雾蒙蒙的草地上”

现在让我们运行相同的提示，看看我们不会两次得到相同的图像：

正如您所见，图像相似，但不完全相同。让我们尝试将温度值更改为0.1，看看会发生什么：

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### 更改温度

让我们尝试使响应更确定。我们可以从生成的两个图像中观察到，在第一张图像中有兔子，在第二张图像中有马，因此图像变化很大。

因此，让我们更改代码并将温度设置为0，如下所示：

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

现在，当您运行此代码时，您会得到这两张图像：

在这里，您可以清楚地看到图像更相似。

## 如何用元提示为您的应用程序定义边界

通过我们的演示，我们已经可以为客户生成图像。然而，我们需要为我们的应用程序创建一些边界。

例如，我们不希望生成不适合工作的图像，或不适合儿童的图像。

我们可以使用_元提示_来实现这一点。元提示是用于控制生成式AI模型输出的文本提示。例如，我们可以使用元提示来控制输出，并确保生成的图像适合工作或适合儿童。

### 它是如何工作的？

那么，元提示是如何工作的？

元提示是用于控制生成式AI模型输出的文本提示，它们放置在文本提示之前，用于控制模型的输出，并嵌入应用程序中以控制模型的输出。将提示输入和元提示输入封装在一个文本提示中。

元提示的一个例子如下：

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

现在，让我们看看如何在我们的演示中使用元提示。

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt =f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"{meta_prompt}
Create an image of a bunny on a horse, holding a lollipop"

# TODO add request to generate image
```

从上述提示中，您可以看到所有创建的图像都考虑了元提示。

## 作业 - 让学生参与

我们在本课程开始时介绍了Edu4All。现在是时候让学生生成他们评估所需的图像了。

学生将为他们的评估创建包含纪念碑的图像，具体的纪念碑由学生决定。学生被要求在这项任务中发挥创造力，将这些纪念碑放在不同的背景中。

## 解决方案

这是一个可能的解决方案：

```python
import openai
import os
import requests
from PIL import Image
import dotenv

# import dotenv
dotenv.load_dotenv()

# Get endpoint and key from environment variables
openai.api_base = "<replace with endpoint>"
openai.api_key = "<replace with api key>"

# Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
openai.api_version = '2023-06-01-preview'
openai.api_type = 'azure'

disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}"""

prompt = f"""{metaprompt}
Generate monument of the Arc of Triumph in Paris, France, in the evening light with a small child holding a Teddy looks on.
""""

try:
    # Create an image by using the image generation API
    generation_response = openai.Image.create(
        prompt=prompt,    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    image_url = generation_response["data"][0]["url"]  # extract image URL from response
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
except openai.InvalidRequestError as err:
    print(err)
```

## 干得好！继续学习

完成本课程后，请查看我们的[生成式AI学习集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，继续提升您的生成式AI知识！

前往第10课，我们将探讨如何[使用低代码构建AI应用程序](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**免责声明**：
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。应将原始文档视为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用此翻译而产生的任何误解或误读，我们不承担责任。