<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef74ad58fc01f7ad80788f79505f9816",
  "translation_date": "2025-08-26T15:02:20+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "tw"
}
-->
# 建立影像生成應用程式

[![建立影像生成應用程式](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.tw.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

大型語言模型（LLM）不只可以產生文字，也能根據文字描述生成影像。影像作為一種媒介，在醫療科技、建築、旅遊、遊戲開發等領域都非常有用。本章將介紹目前最受歡迎的兩種影像生成模型：DALL-E 和 Midjourney。

## 前言

本課程將涵蓋：

- 影像生成及其用途。
- DALL-E 和 Midjourney 的介紹與運作方式。
- 如何建立影像生成應用程式。

## 學習目標

完成本課程後，你將能夠：

- 建立影像生成應用程式。
- 透過 meta prompt 為你的應用程式設定界限。
- 實際操作 DALL-E 和 Midjourney。

## 為什麼要建立影像生成應用程式？

影像生成應用程式是探索生成式 AI 能力的絕佳方式。它們可以用於：

- **影像編輯與合成**。你可以根據不同需求產生各式各樣的影像，像是影像編輯或合成。

- **應用於多元產業**。也能為醫療科技、旅遊、遊戲開發等產業生成專屬影像。

## 情境範例：Edu4All

在本課程中，我們會繼續以新創團隊 Edu4All 為例。學生可以為他們的作業創作影像，內容由學生自行決定，可能是童話故事插圖、角色設計，或是幫助他們將想法和概念具象化。

例如，Edu4All 的學生在課堂上學習世界知名地標時，可以生成如下影像：

![Edu4All 新創團隊，地標課程，艾菲爾鐵塔](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.tw.png)

使用如下提示詞：

> 「清晨陽光下，狗狗在艾菲爾鐵塔旁」

## 什麼是 DALL-E 和 Midjourney？

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) 和 [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) 是目前最受歡迎的影像生成模型之一，能夠根據提示詞生成影像。

### DALL-E

先來介紹 DALL-E，它是一種生成式 AI 模型，可以根據文字描述生成影像。

> [DALL-E 是由兩個模型組成，CLIP 和 diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)。

- **CLIP** 是一個能將影像和文字轉換成數值向量（embedding）的模型。

- **Diffused attention** 則是根據 embedding 生成影像的模型。DALL-E 以大量影像和文字資料訓練，可以根據文字描述生成影像。例如，DALL-E 能生成戴帽子的貓或莫霍克髮型的狗。

### Midjourney

Midjourney 的運作方式與 DALL-E 類似，也是根據文字提示生成影像。你可以用像「戴帽子的貓」或「莫霍克髮型的狗」這樣的提示詞來生成影像。

![Midjourney 生成的機械鴿子](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_圖片來源：維基百科，影像由 Midjourney 生成_

## DALL-E 和 Midjourney 的運作方式

首先，[DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)。DALL-E 是一種基於 transformer 架構的生成式 AI 模型，採用 _自回歸 transformer_。

自回歸 transformer 決定模型如何根據文字描述生成影像，它會一次生成一個像素，然後利用已生成的像素來產生下一個像素。這個過程會經過多層神經網路，直到整張影像完成。

透過這個流程，DALL-E 能控制影像中的屬性、物件、特徵等。不過，DALL-E 2 和 3 對生成影像的掌控度更高。

## 建立你的第一個影像生成應用程式

那麼，要建立一個影像生成應用程式需要哪些套件呢？

- **python-dotenv**，強烈建議用這個套件把機密資訊存放在 _.env_ 檔案，避免直接寫在程式碼裡。
- **openai**，用來與 OpenAI API 互動。
- **pillow**，在 Python 中處理影像。
- **requests**，協助你發送 HTTP 請求。

## 建立並部署 Azure OpenAI 模型

如果還沒設定，請依照 [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) 的指示
建立 Azure OpenAI 資源與模型，並選擇 DALL-E 3 作為模型。  

## 建立應用程式

1. 建立 _.env_ 檔案，內容如下：

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   這些資訊可以在 Azure OpenAI Foundry Portal 的「Deployments」區段找到。

1. 把上述套件整理到 _requirements.txt_ 檔案，格式如下：

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. 接著，建立虛擬環境並安裝套件：

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows 系統請用以下指令建立並啟動虛擬環境：

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. 在 _app.py_ 檔案中加入以下程式碼：

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # import dotenv
    dotenv.load_dotenv()
    
    # configure Azure OpenAI service client 
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
    try:
        # Create an image by using the image generation API
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # Set the directory for the stored image
        image_dir = os.path.join(os.curdir, 'images')

        # If the directory doesn't exist, create it
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Initialize the image path (note the filetype should be png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Retrieve the generated image
        image_url = generation_response.data[0].url  # extract image URL from response
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

程式碼說明如下：

- 首先，我們匯入所需的套件，包括 OpenAI、dotenv、requests 及 Pillow。

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- 接著，從 _.env_ 檔案載入環境變數。

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- 然後，設定 Azure OpenAI 服務的 client。

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- 接下來，生成影像：

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  上述程式會回傳一個 JSON 物件，裡面包含生成影像的 URL。我們可以用這個 URL 下載影像並儲存成檔案。

- 最後，開啟影像並用標準影像檢視器顯示：

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### 影像生成程式碼詳解

來看看生成影像的程式碼細節：

    ```python
      generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                            )
    ```

- **prompt** 是用來生成影像的文字提示。這裡我們用「兔子騎在馬上，手拿棒棒糖，霧氣瀰漫的草地上長著水仙花」。
- **size** 是生成影像的尺寸，這裡是 1024x1024 像素。
- **n** 是生成影像的數量，這裡是兩張。
- **temperature** 是控制生成式 AI 輸出隨機性的參數。值介於 0 到 1，0 代表結果固定，1 代表結果隨機。預設值是 0.7。

影像還有更多進階應用，下一節會介紹。

## 影像生成的進階功能

你已經看到只需幾行 Python 程式就能生成影像。不過，影像還有更多玩法。

你還可以：

- **編輯影像**。提供現有影像、遮罩和提示詞，就能修改影像。例如，你可以幫兔子加頂帽子。做法是提供原始影像、遮罩（標示要修改的區域）和文字提示說明要做什麼。
> 注意：DALL-E 3 不支援此功能。
 
以下是使用 GPT Image 的範例：

    ```python
    response = client.images.edit(
        model="gpt-image-1",
        image=open("sunlit_lounge.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt="A sunlit indoor lounge area with a pool containing a flamingo"
    )
    image_url = response.data[0].url
    ```

  原始影像只有泳池休息室，最終影像則多了隻火鶴：

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="./images/sunlit_lounge.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/mask.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/sunlit_lounge_result.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **產生變化版本**。你可以用現有影像和提示詞，要求模型產生不同版本。做法如下：

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > 注意，此功能僅支援 OpenAI

## 溫度（Temperature）

溫度是控制生成式 AI 輸出隨機性的參數。值介於 0 到 1，0 代表結果固定，1 代表結果隨機。預設值是 0.7。

來看個例子，將同一個提示詞執行兩次：

> 提示詞：「兔子騎在馬上，手拿棒棒糖，霧氣瀰漫的草地上長著水仙花」

![兔子騎馬拿棒棒糖，版本 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.tw.png)

再執行一次同樣的提示詞，看看結果是否一樣：

![生成的兔子騎馬影像](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.tw.png)

可以看到，影像雖然類似，但並不完全相同。現在把溫度值改成 0.1，看看會發生什麼事：

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### 調整溫度

我們來讓結果更一致。從前面兩張影像可以發現，一張有兔子，一張有馬，差異很大。

所以我們把程式碼改成溫度設為 0：

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

執行後會得到這兩張影像：

- ![溫度 0，版本 1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.tw.png)
- ![溫度 0，版本 2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.tw.png)

可以明顯看出兩張影像更相似。

## 如何用 metaprompt 為應用程式設定界限

我們的範例已經能為客戶生成影像，但還需要設定一些界限。

例如，我們不希望生成不適合工作場合或兒童的影像。

這時可以用 _metaprompt_。Metaprompt 是用來控制生成式 AI 輸出的文字提示。例如，可以用 metaprompt 來確保生成的影像適合工作場合或兒童。

### 運作方式

那麼，metaprompt 怎麼運作？

Metaprompt 是用來控制生成式 AI 輸出的文字提示，會放在主要提示詞前面，嵌入應用程式中，控制模型的輸出。把 metaprompt 和主要提示詞合併成一個完整的提示。

舉例來說，metaprompt 可以是：

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

現在來看看如何在範例中使用 metaprompt。

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

從上述提示詞可以看到，所有生成的影像都會考慮 metaprompt 的內容。

## 作業－讓學生動手試試

我們在本課程一開始介紹了 Edu4All。現在是時候讓學生自己為作業生成影像了。

學生將為自己的作業創作包含地標的影像，具體地標由學生自行決定。鼓勵學生發揮創意，將地標放在不同情境中。

## 解答

以下是一種可能的解法：

```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# import dotenv
dotenv.load_dotenv()

# Get endpoint and key from environment variables
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
  api_key=os.environ['AZURE_OPENAI_API_KEY'],
  api_version = "2024-02-01"
  )


disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"""{meta_prompt}
Generate monument of the Arc of Triumph in Paris, France, in the evening light with a small child holding a Teddy looks on.
""""

try:
    # Create an image by using the image generation API
    generation_response = client.images.generate(
        prompt=prompt,    # Enter your prompt text here
        size='1024x1024',
        n=1,
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    image_url = generation_response.data[0].url  # extract image URL from response
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
except openai.BadRequestError as err:
    print(err)
```

## 做得很好！繼續學習吧
完成本課程後，歡迎前往我們的 [生成式 AI 學習專區](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升你對生成式 AI 的知識！

接下來請前往第 10 課，我們將一起了解如何[用低程式碼打造 AI 應用程式](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**免責聲明**：  
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意自動翻譯可能會包含錯誤或不精確之處。原始語言的文件應被視為具權威性的來源。對於重要資訊，建議採用專業人工翻譯。因使用本翻譯而產生的任何誤解或誤釋，我們概不負責。