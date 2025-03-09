# 构建图像生成应用程序

[![构建图像生成应用程序](../../../translated_images/09-lesson-banner.png?WT.d9f0561bfac2f22fe149efecb3524eaf381a4aa260ba334f49b1fd215bd59d75.zh.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

大型语言模型（LLM）的应用不仅限于文本生成。通过文本描述生成图像也是可行的。将图像作为一种模态可以在许多领域发挥重要作用，如医疗技术、建筑、旅游、游戏开发等。在本章中，我们将研究两个最流行的图像生成模型，DALL-E 和 Midjourney。

## 介绍

在本课中，我们将涵盖：

- 图像生成及其重要性。
- DALL-E 和 Midjourney，它们是什么以及如何工作。
- 如何构建图像生成应用程序。

## 学习目标

完成本课后，您将能够：

- 构建一个图像生成应用程序。
- 使用元提示为您的应用程序定义边界。
- 使用 DALL-E 和 Midjourney。

## 为什么要构建图像生成应用程序？

图像生成应用程序是探索生成式 AI 能力的绝佳方式。它们可以用于以下用途：

- **图像编辑和合成**。您可以为各种用例生成图像，例如图像编辑和图像合成。

- **应用于多个行业**。它们还可以用于为多个行业生成图像，如医疗技术、旅游、游戏开发等。

## 场景：Edu4All

作为本课的一部分，我们将继续与我们的初创公司 Edu4All 合作。在本课中，学生将为他们的评估创建图像，具体的图像由学生决定，但他们可以为自己的童话故事绘制插图，或为他们的故事创建新角色，或帮助他们可视化他们的想法和概念。

例如，如果学生在课堂上研究纪念碑，Edu4All 的学生可以生成如下内容：

![Edu4All 初创公司，纪念碑课堂，埃菲尔铁塔](../../../translated_images/startup.png?WT.da6453984b26f46f3e26925e20877c740be4f328afdfce9fe36b23e7b434c7b5.zh.mc_id=academic-105485-koreyst)

使用类似的提示

> "清晨阳光下，埃菲尔铁塔旁的一只狗"

## 什么是 DALL-E 和 Midjourney？

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) 和 [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) 是两个最受欢迎的图像生成模型，它们允许您使用提示生成图像。

### DALL-E

让我们从 DALL-E 开始，这是一个从文本描述生成图像的生成式 AI 模型。

> [DALL-E 是两个模型的组合，CLIP 和扩散注意力](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)。

- **CLIP** 是一个从图像和文本生成嵌入的模型，这些嵌入是数据的数值表示。

- **扩散注意力** 是一个从嵌入生成图像的模型。DALL-E 是在图像和文本数据集上训练的，可以用于从文本描述生成图像。例如，DALL-E 可以用来生成戴帽子的猫或有莫霍克发型的狗的图像。

### Midjourney

Midjourney 的工作方式与 DALL-E 类似，它从文本提示生成图像。Midjourney 也可以用来生成图像，使用类似“戴帽子的猫”或“有莫霍克发型的狗”的提示。

![由 Midjourney 生成的图像，机械鸽子](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_图片来源 Wikipedia，由 Midjourney 生成的图像_

## DALL-E 和 Midjourney 如何工作

首先，[DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)。DALL-E 是基于变压器架构的生成式 AI 模型，具有自回归变压器。

自回归变压器定义了模型如何从文本描述生成图像，它一次生成一个像素，然后使用生成的像素生成下一个像素。通过神经网络中的多个层，直到图像完成。

通过这个过程，DALL-E 控制图像中生成的属性、对象、特征等。然而，DALL-E 2 和 3 对生成的图像有更多控制。

## 构建您的第一个图像生成应用程序

那么构建一个图像生成应用程序需要什么呢？您需要以下库：

- **python-dotenv**，强烈推荐您使用此库将您的密钥保存在代码之外的_.env_文件中。
- **openai**，这个库是您用来与 OpenAI API 交互的。
- **pillow**，用于在 Python 中处理图像。
- **requests**，帮助您进行 HTTP 请求。

1. 创建一个文件_.env_，内容如下：

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   在 Azure Portal 中为您的资源找到此信息，位于“密钥和终端”部分。

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

   对于 Windows，使用以下命令创建和激活您的虚拟环境：

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

让我们解释一下这段代码：

- 首先，我们导入所需的库，包括 OpenAI 库、dotenv 库、requests 库和 Pillow 库。

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

- 然后，我们设置 OpenAI API 的终端、密钥、版本和类型。

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

  上述代码响应一个包含生成图像 URL 的 JSON 对象。我们可以使用该 URL 下载图像并保存到文件中。

- 最后，我们打开图像并使用标准图像查看器显示它：

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### 生成图像的更多细节

让我们更详细地看看生成图像的代码：

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**，是用于生成图像的文本提示。在这个例子中，我们使用的提示是“骑在马上、拿着棒棒糖的小兔子，在长满水仙花的雾气草地上”。
- **size**，是生成的图像的大小。在这个例子中，我们生成的图像大小为1024x1024像素。
- **n**，是生成的图像数量。在这个例子中，我们生成了两个图像。
- **temperature**，是一个参数，用于控制生成式 AI 模型输出的随机性。温度是介于0和1之间的值，其中0表示输出是确定性的，1表示输出是随机的。默认值为0.7。

在下一节中，我们将介绍更多您可以用图像做的事情。

## 图像生成的附加功能

到目前为止，您已经看到我们如何使用几行 Python 代码生成图像。然而，您还可以用图像做更多的事情。

您还可以执行以下操作：

- **进行编辑**。通过提供现有图像的蒙版和提示，您可以更改图像。例如，您可以在图像的某个部分添加一些内容。想象一下我们的兔子图像，您可以给兔子加上一顶帽子。您可以通过提供图像、蒙版（标识要更改的部分）和文本提示来说明应该做什么。

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

  基础图像可能只包含兔子，但最终图像会在兔子上加上帽子。

- **创建变体**。想法是您可以获取现有图像并要求创建变体。要创建变体，您需要提供图像和文本提示，代码如下：

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > 注意，这仅在 OpenAI 上支持

## 温度

温度是一个参数，用于控制生成式 AI 模型输出的随机性。温度是介于0和1之间的值，其中0表示输出是确定性的，1表示输出是随机的。默认值为0.7。

让我们看一个关于温度如何工作的例子，通过运行这个提示两次：

> 提示： "骑在马上、拿着棒棒糖的小兔子，在长满水仙花的雾气草地上"

![骑在马上拿着棒棒糖的小兔子，版本1](../../../translated_images/v1-generated-image.png?WT.e88fb2d10c6d1ae1c198e2959629a4737a139b457fed4b2f325b2ea8d2c7bca6.zh.mc_id=academic-105485-koreyst)

现在让我们运行相同的提示，看看我们不会得到相同的图像两次：

![生成的骑在马上的兔子图像](../../../translated_images/v2-generated-image.png?WT.10df7dd739ff1f669b915523632a51ade0346b30603d8bf996872ac629f3dcd7.zh.mc_id=academic-105485-koreyst)

如您所见，图像相似，但不相同。让我们尝试将温度值更改为0.1，看看会发生什么：

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### 更改温度

让我们尝试使响应更加确定。我们可以从生成的两个图像中观察到，在第一幅图像中有一只兔子，而在第二幅图像中有一匹马，因此图像变化很大。

因此，让我们更改我们的代码，将温度设置为0，如下所示：

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

现在，当您运行此代码时，您将获得这两幅图像：

- ![温度0，版本1](../../../translated_images/v1-temp-generated-image.png?WT.27c4ce8ff113ce11a5a45b5c74e319c5115b0b832a3697bc91fc653d0a5f7609.zh.mc_id=academic-105485-koreyst)
- ![温度0，版本2](../../../translated_images/v2-temp-generated-image.png?WT.04d52c2aa6ef41f4d67040329ca204ef927512f46bb9dfef035e02098f45d0f7.zh.mc_id=academic-105485-koreyst)

在这里，您可以清楚地看到图像更加相似。

## 如何使用元提示为应用程序定义边界

通过我们的演示，我们已经可以为客户生成图像。然而，我们需要为我们的应用程序创建一些边界。

例如，我们不希望生成不适合工作场所或不适合儿童的图像。

我们可以通过_元提示_来实现这一点。元提示是用于控制生成式 AI 模型输出的文本提示。例如，我们可以使用元提示来控制输出，确保生成的图像适合工作场所或适合儿童。

### 它是如何工作的？

那么，元提示是如何工作的呢？

元提示是用于控制生成式 AI 模型输出的文本提示，它们位于文本提示之前，用于控制模型的输出，并嵌入应用程序中以控制模型的输出。将提示输入和元提示输入封装在一个文本提示中。

一个元提示的例子如下：

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

从上面的提示中，您可以看到所有被创建的图像都考虑了元提示。

## 作业 - 让学生参与

我们在本课开始时介绍了 Edu4All。现在是时候让学生为他们的评估生成图像了。

学生将为他们的评估创建包含纪念碑的图像，具体的纪念碑由学生决定。学生被要求在这项任务中发挥创造力，将这些纪念碑放置在不同的背景中。

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

完成本课后，请查看我们的[生成式 AI 学习集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，继续提升您的生成式 AI 知识！

前往第10课，我们将研究如何[使用低代码构建 AI 应用程序](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**免责声明**：  
本文件通过机器翻译服务翻译而成。虽然我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原始文件的母语版本视为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用此翻译而引起的任何误解或误读，我们不承担责任。