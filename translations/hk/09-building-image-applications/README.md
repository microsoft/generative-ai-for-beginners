<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-06-25T17:08:40+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "hk"
}
-->
# 建立圖像生成應用程式

[![建立圖像生成應用程式](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.hk.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM 不僅僅用於文本生成，它還可以從文本描述中生成圖像。圖像作為一種模式在許多領域中非常有用，例如醫療科技、建築、旅遊、遊戲開發等。在本章中，我們將探討兩個最受歡迎的圖像生成模型，DALL-E 和 Midjourney。

## 簡介

在本課中，我們將涵蓋：

- 圖像生成及其重要性。
- DALL-E 和 Midjourney，它們是什麼以及如何運作。
- 如何建立圖像生成應用程式。

## 學習目標

完成本課後，你將能夠：

- 建立圖像生成應用程式。
- 使用元提示定義應用程式的界限。
- 使用 DALL-E 和 Midjourney。

## 為什麼要建立圖像生成應用程式？

圖像生成應用程式是一個探索生成式 AI 能力的好方法。它們可以用於以下用途：

- **圖像編輯和合成**。你可以生成各種用途的圖像，例如圖像編輯和合成。

- **應用於多個行業**。它們也可以用於生成多個行業的圖像，例如醫療科技、旅遊、遊戲開發等。

## 情境：Edu4All

作為本課的一部分，我們將繼續與我們的初創公司 Edu4All 合作。學生們將為他們的評估創建圖像，具體創建什麼圖像由學生決定，但可以是他們自己童話故事的插圖，或者為他們的故事創建新角色，或幫助他們視覺化他們的想法和概念。

例如，如果他們在課堂上研究紀念碑，Edu4All 的學生可以生成如下：

![Edu4All 初創公司，紀念碑課堂，艾菲爾鐵塔](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.hk.png)

使用類似以下的提示

> "清晨陽光下狗在艾菲爾鐵塔旁邊"

## DALL-E 和 Midjourney 是什麼？

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) 和 [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) 是兩個最受歡迎的圖像生成模型，它們允許你使用提示生成圖像。

### DALL-E

讓我們從 DALL-E 開始，它是一個生成式 AI 模型，從文本描述生成圖像。

> [DALL-E 是兩個模型，CLIP 和擴散注意力的組合](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)。

- **CLIP**，是一個從圖像和文本生成嵌入的模型，嵌入是數據的數值表示。

- **擴散注意力**，是一個從嵌入生成圖像的模型。DALL-E 是在圖像和文本數據集上訓練的，可以用於從文本描述生成圖像。例如，DALL-E 可以用於生成戴帽子的貓或莫霍克髮型的狗的圖像。

### Midjourney

Midjourney 的工作方式與 DALL-E 類似，它從文本提示生成圖像。Midjourney 也可以用於使用提示生成圖像，例如“戴帽子的貓”或“莫霍克髮型的狗”。

![由 Midjourney 生成的圖像，機械鴿子](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_圖片來源 Wikipedia，由 Midjourney 生成的圖像_

## DALL-E 和 Midjourney 如何運作

首先，[DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)。DALL-E 是基於轉換器架構的生成式 AI 模型，具有 _自回歸轉換器_。

自回歸轉換器定義了模型如何從文本描述生成圖像，它一次生成一個像素，然後使用生成的像素生成下一個像素。經過神經網絡的多層，直到圖像完成。

通過這個過程，DALL-E 控制生成圖像中的屬性、物件、特徵等。然而，DALL-E 2 和 3 對生成的圖像有更多控制。

## 建立你的第一個圖像生成應用程式

那麼建立圖像生成應用程式需要什麼呢？你需要以下庫：

- **python-dotenv**，強烈建議使用此庫將你的秘密保存在 _.env_ 文件中，遠離代碼。
- **openai**，此庫用於與 OpenAI API 互動。
- **pillow**，在 Python 中處理圖像。
- **requests**，幫助你發送 HTTP 請求。

1. 創建一個名為 _.env_ 的文件，內容如下：

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   在 Azure Portal 中的 "Keys and Endpoint" 部分找到此信息。

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

   對於 Windows，使用以下命令創建和激活虛擬環境：

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

讓我們解釋一下這段代碼：

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

- 然後，我們設置 OpenAI API 的端點、密鑰、版本和類型。

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

  上述代碼返回一個包含生成圖像 URL 的 JSON 對象。我們可以使用該 URL 下載圖像並保存到文件中。

- 最後，我們打開圖像並使用標準圖像查看器顯示它：

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### 更詳細的圖像生成

讓我們更詳細地看看生成圖像的代碼：

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**，是用於生成圖像的文本提示。在此例中，我們使用的提示是“兔子騎在馬上，拿著棒棒糖，在生長著水仙花的霧霾草地上”。
- **size**，是生成圖像的大小。在此例中，我們生成的圖像大小為 1024x1024 像素。
- **n**，是生成的圖像數量。在此例中，我們生成了兩張圖像。
- **temperature**，是一個控制生成式 AI 模型輸出隨機性的參數。溫度值介於 0 到 1 之間，0 表示輸出是確定性的，1 表示輸出是隨機的。默認值為 0.7。

在下一節中，我們將介紹更多可以用圖像做的事情。

## 圖像生成的額外功能

到目前為止，你已經看到如何用幾行 Python 代碼生成圖像。然而，還有更多可以用圖像做的事情。

你還可以進行以下操作：

- **進行編輯**。通過提供現有圖像的遮罩和提示，你可以更改圖像。例如，你可以在圖像的某個部分添加一些東西。想像一下我們的兔子圖像，你可以給兔子加上一頂帽子。你可以通過提供圖像、遮罩（識別需要更改的部分）和文本提示來說明應該做什麼。

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

  基本圖像僅包含兔子，但最終圖像將兔子戴上帽子。

- **創建變化**。這個想法是你採取現有圖像並要求創建變化。要創建變化，你提供一張圖像和一個文本提示，代碼如下：

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > 注意，這僅在 OpenAI 上支持

## 溫度

溫度是一個控制生成式 AI 模型輸出隨機性的參數。溫度值介於 0 到 1 之間，0 表示輸出是確定性的，1 表示輸出是隨機的。默認值為 0.7。

讓我們看看溫度如何運作的示例，通過兩次運行這個提示：

> 提示 : "兔子騎在馬上，拿著棒棒糖，在生長著水仙花的霧霾草地上"

![兔子騎在馬上拿著棒棒糖，版本 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.hk.png)

現在讓我們再次運行相同的提示，看看我們不會得到相同的圖像兩次：

![兔子騎在馬上生成的圖像](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.hk.png)

如你所見，圖像相似，但不相同。讓我們嘗試將溫度值更改為 0.1，看看會發生什麼：

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### 更改溫度

因此，讓我們嘗試使響應更具確定性。我們可以從生成的兩張圖像中觀察到第一張圖像中有一隻兔子，而第二張圖像中有一匹馬，因此圖像差異很大。

因此，讓我們更改代碼並將溫度設置為 0，如下所示：

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

現在當你運行此代碼時，你會得到這兩張圖像：

- ![溫度 0，版本 1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.hk.png)
- ![溫度 0，版本 2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.hk.png)

在這裡，你可以清楚地看到圖像更相似。

## 如何使用元提示定義應用程式的界限

使用我們的演示，我們已經可以為客戶生成圖像。然而，我們需要為應用程式創建一些界限。

例如，我們不希望生成不適合工作的圖像，或不適合兒童的圖像。

我們可以使用 _元提示_ 來做到這一點。元提示是用於控制生成式 AI 模型輸出的文本提示。例如，我們可以使用元提示來控制輸出，並確保生成的圖像是適合工作的，或適合兒童的。

### 它是如何運作的？

那麼，元提示如何運作？

元提示是用於控制生成式 AI 模型輸出的文本提示，它們放置在文本提示之前，用於控制模型的輸出並嵌入到應用程式中以控制模型的輸出。將提示輸入和元提示輸入封裝在一個文本提示中。

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

現在，讓我們看看如何在演示中使用元提示。

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

從上述提示中，你可以看到所有生成的圖像都考慮到了元提示。

## 作業 - 讓學生能夠生成圖像

我們在本課開始時介紹了 Edu4All。現在是時候讓學生能夠為他們的評估生成圖像。

學生們將為他們的評估創建包含紀念碑的圖像，具體紀念碑由學生決定。學生們被要求在這項任務中發揮創意，將這些紀念碑置於不同的背景中。

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

## 幹得好！繼續學習

完成本課後，請查看我們的[生成式 AI 學習集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，繼續提升你的生成式 AI 知識！

前往第 10 課，我們將探討如何[使用低代碼構建 AI 應用程式](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**免責聲明**：  
此文件已使用AI翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)進行翻譯。我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應將原始文件的母語版本視為權威來源。對於關鍵信息，建議尋求專業人工翻譯。對於因使用此翻譯而產生的任何誤解或誤釋，我們不承擔責任。