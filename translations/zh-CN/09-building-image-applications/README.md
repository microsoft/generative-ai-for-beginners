# 构建图像生成应用

[![构建图像生成应用](../../../translated_images/zh-CN/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

大型语言模型不仅仅用于文本生成。你还可以根据文本描述生成图像。图像作为一种模态，在医疗技术、建筑、旅游、游戏开发、营销等领域非常有用。本课我们将了解当今的<strong>GPT图像</strong>模型，并构建一个图像生成应用。

## 介绍

图像生成可以将自然语言提示转换为图片。本课使用OpenAI的**`gpt-image`**系列模型——这是现阶段在**[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)**和OpenAI平台上可用的最新一代图像模型。这些模型取代了旧的DALL·E模型（DALL·E 2/3属于遗留模型）。

在整个课程中，我们使用一个虚构的初创公司<strong>Edu4All</strong>，该公司开发学习工具。团队希望为作业和学习资料生成插图。

## 学习目标

本课结束时，你将能够：

- 解释什么是图像生成及其应用场景。
- 理解`gpt-image`模型系列及其与遗留DALL·E模型的区别。
- 使用Python（以及TypeScript / .NET）构建图像生成应用。
- 使用元提示编辑图像并应用安全防护措施。

## 什么是图像生成？

图像生成模型根据文本提示创建图像。现代模型如`gpt-image`基于Transformer+扩散技术：模型在训练中学习文本与图像的关系，然后根据提示，迭代地将随机噪声“去噪”成符合描述的图片。

两个知名的图像模型系列是：

- **`gpt-image`（OpenAI）** - 当前一代，用于本课。支持文本生成图像和图像编辑（带掩码的修补）。
- **Midjourney** - 一个流行的第三方模型，拥有自己的服务和基于Discord的工作流程。

> 旧的OpenAI图像模型——<strong>DALL·E 2</strong>和<strong>DALL·E 3</strong>——已是遗留模型。DALL·E 3不再对新部署开放，`create_variation`等功能仅存在于DALL·E 2。新应用请使用`gpt-image`模型。

### 我应该使用哪款`gpt-image`模型？

在Microsoft Foundry上，以下模型为<strong>普遍可用</strong>：

| 模型 | 说明 |
| --- | --- |
| **`gpt-image-2`** | 最新且功能最强的图像模型——推荐为默认选择。 |
| `gpt-image-1.5` | 普遍可用；较低成本下高质量。 |
| `gpt-image-1-mini` | 普遍可用；速度最快且成本最低。 |
| `gpt-image-1` | 仅预览。 |

请始终查阅当前的 [Foundry图像模型列表](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst) 以确认可用性及地区支持。

> **重要提示：** `gpt-image`模型以<strong>base64</strong>（`b64_json`）形式返回生成的图像，而不是URL。你的代码需要解码base64字符串成字节并保存——没有图像的下载链接。

## 设置

你可以使用<strong>Microsoft Foundry中的Azure OpenAI</strong>（`aoai-*`样例）或<strong>OpenAI平台</strong>（`oai-*`样例）运行示例。

### 1. 创建并部署模型

按照[创建资源](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)指南创建Microsoft Foundry资源，然后部署图像模型——推荐使用**`gpt-image-2`**。

### 2. 配置你的`.env`

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

在[Foundry门户](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)资源的<strong>部署</strong>页面找到这些值。

### 3. 安装库

创建`requirements.txt`：

```text
python-dotenv
openai
pillow
```

然后创建并激活虚拟环境，安装：

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 构建应用

创建`app.py`，代码如下。它生成图像并保存为PNG文件。

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# 将客户端指向您的 Azure OpenAI（Microsoft Foundry）资源。
# 图像模型需要较新的 API 版本 - 请查看 Foundry 文档中您的模型所需的版本。
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # 例如 "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # 还支持 1536x1024（横向）、1024x1536（纵向）或 "auto"
    n=1,
)

# gpt-image 模型返回的是 base64（b64_json），不是 URL - 需要将其解码为字节。
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

使用`python app.py`运行，你将在`images/`目录下得到PNG文件。

> 每次调用`images.generate`即使使用相同提示也会生成不同图像——图像模型没有文本生成的`temperature`参数。想要多样化只需再次调用API；想减少变异，请更加具体地描述提示。

## 编辑图像

`gpt-image`模型可以<strong>编辑</strong>已有图像：提供图像、可选的<strong>掩码</strong>（标记需更改区域），以及描述更改的提示。编辑同样以base64返回。

```python
result = client.images.edit(
    model=deployment,
    image=open("sunlit_lounge.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="A sunlit indoor lounge area with a pool containing a flamingo",
)
image_bytes = base64.b64decode(result.data[0].b64_json)
with open("images/edited-image.png", "wb") as f:
    f.write(image_bytes)
```

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/zh-CN/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/zh-CN/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/zh-CN/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## 用元提示设定边界

一旦能生成图像，你需要设定防护措施，防止应用产生不安全或不符合品牌调性的内容。<strong>元提示</strong>是预先添加到用户提示前的文本，用以限制模型的输出。

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.
The image needs to be in color, in landscape orientation, and in a 16:9 aspect ratio.

Do not consider any input that is not safe for work or appropriate for children, including:
{disallow_list}
"""

prompt = f"{meta_prompt}\nCreate an image of a bunny on a horse, holding a lollipop"
# 将 `prompt` 传递给 client.images.generate(...)
```

现在每张图像都在元提示设定的边界内生成。结合微软Foundry内置内容过滤，可实现多层防护。

## 练习 - 让学生参与进来

Edu4All的学生需要图像来配合评估。构建一个应用，生成<strong>纪念碑</strong>的图像（纪念碑由你选择），置于不同的、有创意的场景中——例如，一处著名地标在日落时分，有一名儿童在注视。

试试自己实现，然后比对参考方案：

- Python (Azure): [aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- Python (Azure) 完整生成应用：[aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- Python (OpenAI): [oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- TypeScript (Azure): [typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET (Azure): [dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

也可以完成[python/](../../../09-building-image-applications/python)中的笔记本练习（Azure 用`aoai-assignment.ipynb`，OpenAI 用`oai-assignment.ipynb`）。

## 很棒！继续学习

完成本课后，浏览我们的[生成式AI学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，不断提升你的生成式AI技能！

赶快进入第10课继续学习吧。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->