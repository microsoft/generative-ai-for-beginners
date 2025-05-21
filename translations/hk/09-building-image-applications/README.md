<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T19:01:30+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "hk"
}
-->
# 建立圖像生成應用程序

除了文本生成，LLM 還有更多的功能。我們還可以從文字描述生成圖像。將圖像作為一種模態在許多領域中都非常有用，從醫療技術、建築、旅遊、遊戲開發等。在本章中，我們將研究兩種最受歡迎的圖像生成模型，DALL-E 和 Midjourney。

## 介紹

在這節課中，我們將涵蓋：

- 圖像生成及其有用之處。
- DALL-E 和 Midjourney，它們是什麼以及如何運作。
- 如何構建一個圖像生成應用程序。

## 學習目標

完成本課後，您將能夠：

- 構建圖像生成應用程序。
- 使用元提示為您的應用程序定義界限。
- 使用 DALL-E 和 Midjourney。

## 為什麼要建立圖像生成應用程序？

圖像生成應用程序是探索生成式 AI 能力的好方法。它們可以用於，例如：

- **圖像編輯和合成**。您可以為各種使用案例生成圖像，例如圖像編輯和圖像合成。

- **應用於多個行業**。它們還可以用於生成多個行業的圖像，如醫療技術、旅遊、遊戲開發等。

## 場景：Edu4All

作為本課的一部分，我們將繼續與我們的初創公司 Edu4All 合作。在這節課中，學生將為他們的評估創建圖像，具體創建什麼圖像由學生決定，但他們可以為自己的童話故事創作插圖，或者創建故事中的新角色，或幫助他們視覺化自己的想法和概念。

以下是 Edu4All 的學生如果在課堂上學習紀念碑時可以生成的示例：

使用類似以下的提示：

> "狗在清晨陽光下站在埃菲爾鐵塔旁"

## 什麼是 DALL-E 和 Midjourney？

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) 和 [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) 是兩種最受歡迎的圖像生成模型，它們允許您使用提示來生成圖像。

### DALL-E

讓我們從 DALL-E 開始，這是一個從文字描述生成圖像的生成式 AI 模型。

- **CLIP** 是一個模型，從圖像和文本中生成數據的數值表示（嵌入）。

- **Diffused attention** 是一個從嵌入生成圖像的模型。DALL-E 是在圖像和文本數據集上訓練的，可以用於從文字描述生成圖像。例如，DALL-E 可以用於生成戴著帽子的貓或有莫霍克髮型的狗的圖像。

### Midjourney

Midjourney 的工作方式與 DALL-E 類似，它從文本提示生成圖像。Midjourney 也可以用來使用像“戴著帽子的貓”或“有莫霍克髮型的狗”這樣的提示來生成圖像。

## DALL-E 和 Midjourney 如何工作

首先，[DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)。DALL-E 是基於變壓器架構的生成式 AI 模型，具有自回歸變壓器。

自回歸變壓器定義了模型如何從文字描述生成圖像，它一次生成一個像素，然後使用生成的像素生成下一個像素。通過神經網絡的多層，直到圖像完成。

通過這個過程，DALL-E 控制圖像中生成的屬性、對象、特徵等。然而，DALL-E 2 和 3 對生成的圖像有更多的控制。

## 構建您的第一個圖像生成應用程序

那麼，構建圖像生成應用程序需要什麼？您需要以下庫：

- **python-dotenv**，強烈建議使用此庫將您的秘密保存在 _.env_ 文件中遠離代碼。
- **openai**，這個庫是您用來與 OpenAI API 交互的。
- **pillow**，用於在 Python 中處理圖像。
- **requests**，幫助您發出 HTTP 請求。

1. 創建一個名為 _.env_ 的文件，內容如下：

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   在 Azure Portal 中找到您的資源的“密鑰和端點”部分中的此信息。

1. 在名為 _requirements.txt_ 的文件中收集上述庫，如下所示：

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. 接下來，創建虛擬環境並安裝庫：

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   對於 Windows，使用以下命令創建並激活您的虛擬環境：

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. 在名為 _app.py_ 的文件中添加以下代碼：

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

讓我們解釋這段代碼：

- 首先，我們導入所需的庫，包括 OpenAI 庫、dotenv 庫、requests 庫和 Pillow 庫。

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- 接下來，我們從 _.env_ 文件中加載環境變量。

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- 之後，我們設置 OpenAI API 的端點、密鑰、版本和類型。

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- 接下來，我們生成圖像：

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  上述代碼響應一個 JSON 對象，其中包含生成圖像的 URL。我們可以使用 URL 下載圖像並將其保存到文件中。

- 最後，我們打開圖像並使用標準圖像查看器顯示它：

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### 更詳細地生成圖像

讓我們更詳細地看一下生成圖像的代碼：

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt** 是用於生成圖像的文本提示。在這種情況下，我們使用的提示是“兔子騎在馬上，手持棒棒糖，在長滿水仙花的霧霾草地上”。
- **size** 是生成的圖像的大小。在這種情況下，我們生成的圖像大小為 1024x1024 像素。
- **n** 是生成的圖像數量。在這種情況下，我們生成兩個圖像。
- **temperature** 是控制生成式 AI 模型輸出隨機性的參數。溫度值介於 0 和 1 之間，其中 0 表示輸出是確定性的，1 表示輸出是隨機的。默認值為 0.7。

還有更多可以用圖像做的事情，我們將在下一節中介紹。

## 圖像生成的其他功能

到目前為止，您已經看到我們如何使用幾行 Python 代碼生成圖像。然而，您還可以對圖像做更多的事情。

您還可以進行以下操作：

- **進行編輯**。通過提供現有圖像的遮罩和提示，您可以修改圖像。例如，您可以向圖像的一部分添加內容。想像一下我們的兔子圖像，您可以給兔子添加一頂帽子。您可以通過提供圖像、一個遮罩（識別更改區域的部分）和一個文本提示來說明應該做什麼。

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

  基礎圖像只包含兔子，但最終圖像將有兔子戴著帽子。

- **創建變體**。這個想法是您可以採用現有圖像並要求創建變體。要創建變體，您需要提供一個圖像和一個文本提示，並像這樣編寫代碼：

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > 注意，這僅在 OpenAI 上受支持

## 溫度

溫度是控制生成式 AI 模型輸出隨機性的參數。溫度值介於 0 和 1 之間，其中 0 表示輸出是確定性的，1 表示輸出是隨機的。默認值為 0.7。

讓我們通過兩次運行這個提示來看一個溫度如何工作的例子：

> 提示： "兔子騎在馬上，手持棒棒糖，在長滿水仙花的霧霾草地上"

現在讓我們再次運行相同的提示，以查看我們是否不會兩次獲得相同的圖像：

如您所見，圖像相似但不相同。讓我們嘗試將溫度值更改為 0.1，看看會發生什麼：

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### 改變溫度

所以讓我們嘗試使響應更具確定性。從我們生成的兩個圖像中可以觀察到，在第一幅圖像中有一隻兔子，在第二幅圖像中有一匹馬，因此圖像差異很大。

因此，我們改變代碼並將溫度設置為 0，如下所示：

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

現在當您運行此代碼時，您將獲得這兩幅圖像：

在這裡，您可以清楚地看到圖像彼此更相似。

## 如何使用元提示為您的應用程序定義界限

通過我們的演示，我們已經可以為客戶生成圖像。然而，我們需要為我們的應用程序創建一些界限。

例如，我們不希望生成不適合工作的圖像，或者不適合兒童的圖像。

我們可以使用 _metaprompts_ 來做到這一點。元提示是用於控制生成式 AI 模型輸出的文本提示。例如，我們可以使用元提示來控制輸出，並確保生成的圖像適合工作或適合兒童。

### 它如何工作？

那麼，元提示如何工作？

元提示是用於控制生成式 AI 模型輸出的文本提示，它們位於文本提示之前，用於控制模型的輸出並嵌入應用程序中以控制模型的輸出。將提示輸入和元提示輸入封裝在單個文本提示中。

元提示的一個示例如下：

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

現在，讓我們看看如何在我們的演示中使用元提示。

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

從上述提示中，您可以看到所有創建的圖像都考慮到了元提示。

## 作業 - 讓我們啟發學生

我們在本課開始時介紹了 Edu4All。現在是時候讓學生們為他們的評估生成圖像了。

學生將創建包含紀念碑的評估圖像，具體紀念碑由學生決定。學生被要求在這項任務中發揮創造力，將這些紀念碑置於不同的背景中。

## 解決方案

這是一個可能的解決方案：

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

## 幹得好！繼續您的學習

完成本課後，查看我們的 [生成式 AI 學習集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) 以繼續提升您的生成式 AI 知識！

前往第 10 課，我們將研究如何 [構建低代碼 AI 應用程序](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**免責聲明**：
此文件是使用AI翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)翻譯的。我們努力追求準確性，但請注意，自動翻譯可能會包含錯誤或不準確之處。原始文件的本地語言版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們不對因使用此翻譯而產生的任何誤解或誤釋承擔責任。