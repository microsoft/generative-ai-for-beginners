<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-06-25T17:07:19+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "zh"
}
-->
# 构建图像生成应用程序

生成式AI不仅限于文本生成，还可以从文本描述中生成图像。拥有图像作为一种模式在许多领域中非常有用，如医疗技术、建筑、旅游、游戏开发等。在本章中，我们将研究两个最流行的图像生成模型，DALL-E和Midjourney。

## 介绍

在本课中，我们将涵盖：

- 图像生成及其重要性。
- DALL-E和Midjourney，它们是什么以及如何工作。
- 如何构建一个图像生成应用程序。

## 学习目标

完成本课后，你将能够：

- 构建一个图像生成应用程序。
- 使用元提示为你的应用程序定义边界。
- 使用DALL-E和Midjourney。

## 为什么构建图像生成应用程序？

图像生成应用程序是探索生成式AI能力的绝佳方式。它们可以用于以下方面：

- **图像编辑和合成**。你可以为各种用例生成图像，例如图像编辑和图像合成。

- **应用于多个行业**。它们还可以用于生成医疗技术、旅游、游戏开发等多个行业的图像。

## 场景：Edu4All

作为本课的一部分，我们将继续与我们的初创公司Edu4All合作。学生们将为他们的评估创建图像，具体图像由学生决定，他们可以为自己的童话故事创作插图，或为他们的故事创建新角色，或帮助他们可视化他们的想法和概念。

例如，如果Edu4All的学生在课堂上学习纪念碑，他们可以生成以下内容：

![Edu4All 初创公司，纪念碑课程，埃菲尔铁塔](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.zh.png)

使用类似这样的提示：

> "清晨阳光下，埃菲尔铁塔旁边的狗"

## 什么是DALL-E和Midjourney？

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst)和[Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst)是两个最流行的图像生成模型，它们允许你使用提示生成图像。

### DALL-E

让我们从DALL-E开始，它是一个从文本描述生成图像的生成式AI模型。

> [DALL-E是两个模型的组合，CLIP和扩散注意力](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)。

- **CLIP**，是一个生成嵌入的模型，嵌入是数据的数值表示，来自图像和文本。

- **扩散注意力**，是一个从嵌入生成图像的模型。DALL-E经过一组图像和文本的数据集训练，可以用来从文本描述中生成图像。例如，DALL-E可以用来生成戴帽子的猫或莫霍克发型的狗的图像。

### Midjourney

Midjourney的工作方式与DALL-E类似，它从文本提示生成图像。Midjourney也可以使用类似“戴帽子的猫”或“莫霍克发型的狗”的提示来生成图像。

![Midjourney生成的图像，机械鸽子](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_图片来源 Wikipedia，图像由Midjourney生成_

## DALL-E和Midjourney如何工作

首先，[DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)。DALL-E是基于变压器架构的生成式AI模型，具有_自回归变压器_。

_自回归变压器_定义了模型如何从文本描述中生成图像，它一次生成一个像素，然后使用生成的像素生成下一个像素。通过神经网络的多个层，直到图像完成。

通过这个过程，DALL-E可以控制其生成图像中的属性、对象、特征等。然而，DALL-E 2和3对生成的图像有更多的控制。

## 构建你的第一个图像生成应用程序

那么构建一个图像生成应用程序需要什么？你需要以下库：

- **python-dotenv**，强烈建议使用这个库将你的密钥保存在代码之外的_.env_文件中。
- **openai**，这个库用于与OpenAI API交互。
- **pillow**，用于在Python中处理图像。
- **requests**，帮助你发出HTTP请求。

1. 创建一个_.env_文件，内容如下：

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   在Azure Portal中为你的资源找到这些信息，位于“Keys and Endpoint”部分。

1. 将上述库收集在一个名为_requirements.txt_的文件中，如下所示：

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

   对于Windows，使用以下命令创建和激活虚拟环境：

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. 在名为_app.py_的文件中添加以下代码：

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

让我们解释一下这段代码：

- 首先，我们导入需要的库，包括OpenAI库、dotenv库、requests库和Pillow库。

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- 接下来，我们从_.env_文件加载环境变量。

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- 然后，我们设置OpenAI API的端点、密钥、版本和类型。

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

  上述代码返回一个包含生成图像URL的JSON对象。我们可以使用该URL下载图像并保存到文件中。

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

- **prompt**，是用于生成图像的文本提示。在这种情况下，我们使用的提示是“骑马的小兔子，手拿棒棒糖，在长满水仙花的雾气弥漫的草地上”。
- **size**，是生成图像的尺寸。在这种情况下，我们生成的图像是1024x1024像素。
- **n**，是生成的图像数量。在这种情况下，我们生成两个图像。
- **temperature**，是一个参数，用于控制生成式AI模型输出的随机性。温度是介于0和1之间的值，其中0表示输出是确定性的，1表示输出是随机的。默认值是0.7。

在下一节中，我们将介绍更多可以对图像进行的操作。

## 图像生成的附加功能

到目前为止，你已经看到我们如何使用Python的几行代码生成图像。然而，你还可以对图像进行更多操作。

你还可以进行以下操作：

- **执行编辑**。通过提供现有图像、一个蒙版和一个提示，你可以更改图像。例如，你可以在图像的一部分添加一些东西。想象一下我们的小兔子图像，你可以给小兔子加上一顶帽子。你可以通过提供图像、一个蒙版（标识要更改的部分）和一个文本提示来实现。

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

  基础图像只包含兔子，但最终图像会在兔子上加上帽子。

- **创建变体**。这个想法是你可以采用现有图像并要求创建变体。要创建变体，你提供一个图像和一个文本提示，并像这样编写代码：

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

温度是一个参数，用于控制生成式AI模型输出的随机性。温度是介于0和1之间的值，其中0表示输出是确定性的，1表示输出是随机的。默认值是0.7。

让我们通过两次运行此提示来看看温度是如何工作的：

> 提示： "骑马的小兔子，手拿棒棒糖，在长满水仙花的雾气弥漫的草地上"

![骑马的小兔子，手拿棒棒糖，版本1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.zh.png)

现在让我们运行相同的提示，以确保我们不会得到两次相同的图像：

![生成的骑马小兔子图像](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.zh.png)

正如你所看到的，图像相似但不相同。让我们尝试将温度值更改为0.1，看看会发生什么：

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### 改变温度

让我们尝试使响应更具确定性。从我们生成的两个图像中可以观察到，第一个图像中有一个兔子，第二个图像中有一匹马，所以图像差异很大。

因此，让我们更改代码并将温度设置为0，如下所示：

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

现在当你运行此代码时，你会得到这两个图像：

- ![温度0，v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.zh.png)
- ![温度0，v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.zh.png)

在这里你可以清楚地看到图像彼此更加相似。

## 如何使用元提示为你的应用程序定义边界

通过我们的演示，我们已经可以为客户生成图像。然而，我们需要为我们的应用程序创建一些边界。

例如，我们不希望生成不适合工作的图像，或者不适合儿童的图像。

我们可以通过_元提示_来实现这一点。元提示是用于控制生成式AI模型输出的文本提示。例如，我们可以使用元提示来控制输出，并确保生成的图像适合工作或适合儿童。

### 如何运作？

那么，元提示是如何工作的？

元提示是用于控制生成式AI模型输出的文本提示，它们位于文本提示之前，用于控制模型的输出，并嵌入到应用程序中以控制模型的输出。将提示输入和元提示输入封装在一个文本提示中。

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

从上面的提示中，你可以看到所有创建的图像都考虑了元提示。

## 作业 - 让学生参与

我们在本课开始时介绍了Edu4All。现在是时候让学生们为他们的评估生成图像了。

学生们将为他们的评估创建包含纪念碑的图像，具体的纪念碑由学生决定。学生们被要求在这个任务中发挥他们的创造力，将这些纪念碑置于不同的背景中。

## 解决方案

以下是一个可能的解决方案：

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

完成本课后，请查看我们的[生成式AI学习集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)以继续提升你的生成式AI知识！

前往第10课，我们将探讨如何[使用低代码构建AI应用程序](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**免责声明**：
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原始语言的文档视为权威来源。对于关键信息，建议进行专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们概不负责。