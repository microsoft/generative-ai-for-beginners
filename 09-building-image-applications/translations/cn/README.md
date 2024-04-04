# 第九章：构建图像生成应用

[![Building Image Generation Applications](../../images/09-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](TBD)

> **导学视频敬请期待**

LLMs 不仅仅是文本生成。 还可以根据文本描述生成图像。 将图像作为一种模式在医疗科技、建筑、旅游、游戏开发等许多领域非常有用。 在本章中，我们将研究两种最流行的图像生成模型：DALL-E 和 Midjourney。

## 本章概述

在本章中，您将学习到：

- 图像生成及其有用的原因。
- DALL-E 和 Midjourney，它们是什么以及它们如何工作。
- 如何构建图像生成应用程序。

## 学习目标

在完成本章的学习，您将能够：

- 构建图像生成应用程序。
- 使用元提示定义应用程序的边界。
- 使用 DALL-E 和 Midjourney

## 为什么要构建图像生成应用程序？

图像生成应用程序是探索生成式人工智能功能的好方法。 它们可用于，例如：

- **图像编辑和合成**。 您可以为各种用例生成图像，例如图像编辑和图像合成。

- **适用于多种行业**。 它们还可以用于为医疗科技、旅游、游戏开发等各种行业生成图像。

## 场景 Edu4All

作为本章的一部分，我们将在本章中继续与 "Our Startup" Edu4All 合作。 学生将为他们的评估创建图像，具体图像由学生决定，但它们可以是他们自己的童话故事的插图，或者为他们的故事创建一个新角色，或者帮助他们形象化他们的想法和概念。

例如，如果 Edu4All 的学生在课堂上研究纪念碑，他们可以生成以下内容：

![Edu4All startup, class on monuments, Eiffel Tower](../../images/startup.png?WT.mc_id=academic-105485-koreyst)

提示词如下

> "Dog next to Eiffel Tower in early morning sunlight"

## 什么是 DALL-E 和 Midjourney？

[DALL-E](https://openai.com/dall-e-2) 和 [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) 是两种最流行的图像生成模型，它们允许您使用提示词生成图像。

### DALL-E

让我们从 DALL-E 开始，它是一种生成式 AI 模型，可以根据文本描述生成图像。

> [DALL-E 是 CLIP 和 diffused attention 两种模型的组合]
> (https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e)。

- **CLIP**，是一种从图像和文本生成嵌入的模型，嵌入是数据的数字表示。

- **diffused attention**，是一种从嵌入生成图像的模型。 DALL-E 在图像和文本数据集上进行训练，可用于从文本描述生成图像。 例如，DALL-E 可用于生成戴帽子的猫或留着莫霍克发型的狗的图像。

### Midjourney

Midjourney 的工作方式与 DALL-E 类似，它根据文本提示生成图像。 Midjourney 还可以用于使用“戴帽子的猫”或“莫西干狗”等提示来生成图像。

![图像由 Midjourney生成，机械鸽子](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)

_图片来源维基百科，图片由 Midjourney 生成_

## DALL-E 和 Midjourney 如何运作

首先，[DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)。 DALL-E 是一种基于带有 _autoregressive transformer_ 的 transformer 架构的生成式人工智能模型。

“autoregressive transformer”定义了模型如何根据文本描述生成图像，它一次生成一个像素，然后使用生成的像素生成下一个像素。 经过神经网络中的多个层，直到图像完整。

通过此过程，DALL-E 可以控制其生成的图像中的属性、对象、特征等。 DALL-E 2 和 3 对生成的图像有更多的控制权，

## 构建您的第一个图像生成应用程序

那么构建图像生成应用程序需要什么？ 您需要以下 Library：

- **python-dotenv**，强烈建议您使用此库将您的秘密保存在远离代码的 _.env_ 文件中。
- **openai**，您将使用该库与 OpenAI API 进行交互。
- **pillow**，用于在 Python 中处理图像。
- **requests**，发出 HTTP 请求。

1. 创建一个包含以下内容的文件 _.env_：

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_KEY=<your key>
   ```

   在 Azure 门户中的 "Keys and Endpoint" 部分中找到资源的此信息。

2. 将上述库收集到名为 _requirements.txt_ 的文件中，如下所示：

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

3. 接下来，创建虚拟环境并安装库：

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   对于 Windows，使用以下命令创建并激活虚拟环境：

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

4. 在名为 _app.py_ 的文件中添加以下代码：

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
   openai.api_key = os.environ['AZURE_OPENAI_KEY']

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
   except openai.error.InvalidRequestError as err:
       print(err)

   ```

我们来解释一下这段代码：

- 首先，我们导入我们需要的 Library ，包括 OpenAI 、dotenv 、requests 和 Pillow。

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- 接下来，我们从 _.env_ 文件加载环境变量。

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- 之后，我们设置 OpenAI API 的 endpoint 、 key 、版本和类型。

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_KEY']

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

  上面的代码返回一个 JSON 对象，其中包含生成图像的 URL。 我们可以使用 URL 下载图像并将其保存到文件中。

- 最后，我们打开图像并使用标准图像查看器来显示它：

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### 有关生成图像的更多详细信息

让我们更详细地看一下生成图像的代码：

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**，是用于生成图像的文本提示。 在本例中，我们使用提示"Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"。
- **size**，是生成的图像的尺寸。 在本例中，我们生成一个 1024x1024 像素的图像。
- **n**，是生成的图像数量。 在本例中，我们生成两个图像。
- **temperature**，是控制生成人工智能模型输出随机性的参数。 temperature 是 0 到 1 之间的值，其中 0 表示输出是确定性的，1 表示输出是随机的。 默认值为 0.7。

您可以对图像执行更多操作，我们将在下面中介绍这些操作。

## 图像生成的附加功能

到目前为止，您已经了解了如何使用 Python 中的几行代码来生成图像。 但是，您还可以对图像执行更多操作。

您还可以执行以下操作：

- **执行编辑**。 通过为现有图像提供遮罩和提示，您可以更改图像。 例如，您可以向图像的一部分添加某些内容。 想象一下我们的兔子图像，您可以给兔子添加一顶帽子。 您将如何做到这一点，方法是提供图像、遮罩（标识要更改的区域的部分）和文本提示来说明应该做什么。

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

  The base image would only contain the rabbit but the final image would have the hat on the rabbit.

  基本图像仅包含兔子，但最终图像将在兔子上戴上帽子。

- **创建变体**。 这个想法是，你采用现有的图像并要求创建变体。 要创建变体，您需要提供图像和文本提示以及代码，如下所示：

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > 注意，这仅在 OpenAI 上支持

## Temperature

Temperature 是控制生成式 AI 模型输出随机性的参数。 Temperature 是 0 到 1 之间的值，其中 0 表示输出是确定性的，1 表示输出是随机的。 默认值为 0.7。

让我们通过运行此提示两次来看看 temperature 如何工作的示例：

> Prompt : "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![Bunny on a horse holding a lollipop, version 1](../../images/v1-generated-image.png?WT.mc_id=academic-105485-koreyst)

现在让我们运行相同的提示，我们不会两次获得相同的图像：

![Generated image of bunny on horse](../../images/v2-generated-image.png?WT.mc_id=academic-105485-koreyst)

正如您所看到的，图像相似，但不相同。 让我们尝试将 temperature 值更改为 0.1，看看会发生什么：

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### 改变 temperature

因此，让我们尝试使响应更加确定。 我们可以从生成的两张图像中观察到，在第一张图像中，有一只兔子，在第二张图像中，有一匹马，因此图像差异很大。

因此，让我们更改代码并 temperature 设置为 0，如下所示：

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

现在，当您运行此代码时，您会得到这两个图像：

- ![Temperature 0, v1](../../images/v1-temp-generated-image.png?WT.mc_id=academic-105485-koreyst)
- ![Temperature 0 , v2](../../images/v2-temp-generated-image.png?WT.mc_id=academic-105485-koreyst)

在这里您可以清楚地看到图像彼此之间的相似程度。

## 如何使用元提示定义应用程序的边界

通过我们的演示，我们已经可以为客户生成图像。 然而，我们需要为我们的应用程序创建一些边界。

例如，我们不想生成不适合工作或不适合儿童的图像。

我们可以通过 _元提示_ 来做到这一点。 元提示是用于控制生成式 AI 模型的输出的文本提示。 例如，我们可以使用元提示来控制输出，并确保生成的图像对于工作来说是安全的，或者适合儿童。

### 它是如何工作的？

现在，元提示如何工作？

元提示是用于控制生成式 AI 模型的输出的文本提示，它们位于文本提示之前，用于控制模型的输出并嵌入到应用程序中以控制模型的输出。 将提示输入和元提示输入封装在单个文本提示中。

元提示的一个示例如下：

````text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```text

现在，让我们看看如何在例子中使用元提示。

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
````

从上面的提示中，您可以看到正在创建的所有图像如何考虑元提示。

## 作业 - 让我们帮助学生

我们在本课开始时介绍了 Edu4All。 现在是时候让学生生成用于评估的图像了。

学生们将为他们的评估创建包含纪念碑的图像，而纪念碑到底是什么由学生决定。 学生们被要求在这项任务中发挥他们的创造力，将这些纪念碑放置在不同的环境中。

## 解决方案

这是一种可能的解决方案：

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
except openai.error.InvalidRequestError as err:
    print(err)
```

## 继续学习

想要了解有关构建图像生成应用的更多信息？ 转至[进阶学习的页面](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) 查找有关此主章节的其他学习资源。

前往第十章，我们将学习[创建低代码的人工智能应用](../../../10-building-low-code-ai-applications/translations/cn/README.md?WT.mc_id=academic-105485-koreyst)
