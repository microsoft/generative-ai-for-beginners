<<<<<<< HEAD
<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "063a2ac57d6b71bea0eaa880c68770d2",
  "translation_date": "2025-09-29T21:32:42+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "tw"
}
-->
# 建立影像生成應用程式

[![建立影像生成應用程式](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.tw.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

大型語言模型（LLM）的應用不僅限於文字生成，還可以根據文字描述生成影像。影像作為一種模態在許多領域中非常有用，例如醫療科技、建築、旅遊、遊戲開發等。在本章中，我們將探討兩個最受歡迎的影像生成模型：DALL-E 和 Midjourney。

## 簡介

在本課程中，我們將涵蓋以下內容：

- 影像生成及其重要性。
- DALL-E 和 Midjourney 的介紹及其運作方式。
- 如何建立影像生成應用程式。

## 學習目標

完成本課程後，您將能夠：

- 建立影像生成應用程式。
- 使用元提示（meta prompts）為您的應用程式定義界限。
- 使用 DALL-E 和 Midjourney。

## 為什麼要建立影像生成應用程式？

影像生成應用程式是一種探索生成式 AI 能力的絕佳方式。它們可以用於以下用途，例如：

- **影像編輯與合成**。您可以生成各種用途的影像，例如影像編輯和影像合成。

- **應用於多種行業**。它們還可以用於生成適用於多種行業的影像，例如醫療科技、旅遊、遊戲開發等。

## 情境：Edu4All

在本課程中，我們將繼續與我們的初創公司 Edu4All 合作。學生將為他們的評估創建影像，具體創建什麼影像由學生決定，例如可以是他們自己童話故事的插圖，或者創建故事中的新角色，幫助他們將想法和概念可視化。

以下是 Edu4All 的學生在課堂上學習紀念碑時可能生成的影像示例：

![Edu4All 初創公司，課堂上的紀念碑，艾菲爾鐵塔](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.tw.png)

使用以下提示：

> 「清晨陽光下，狗站在艾菲爾鐵塔旁」

## DALL-E 和 Midjourney 是什麼？

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) 和 [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) 是兩個最受歡迎的影像生成模型，它們允許您使用提示生成影像。

### DALL-E

首先介紹 DALL-E，它是一種生成式 AI 模型，可以根據文字描述生成影像。

> [DALL-E 是兩個模型的結合：CLIP 和擴散注意力](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)。

- **CLIP** 是一個模型，可以從影像和文字生成嵌入（數據的數值表示）。

- **擴散注意力** 是一個模型，可以根據嵌入生成影像。DALL-E 是在影像和文字數據集上訓練的，可以用於根據文字描述生成影像。例如，DALL-E 可以生成戴著帽子的貓或有莫霍克髮型的狗的影像。

### Midjourney

Midjourney 的工作方式與 DALL-E 類似，它根據文字提示生成影像。Midjourney 也可以使用像「戴著帽子的貓」或「有莫霍克髮型的狗」這樣的提示生成影像。

![由 Midjourney 生成的影像，機械鴿子](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_圖片來源：維基百科，由 Midjourney 生成的影像_

## DALL-E 和 Midjourney 的運作方式

首先，[DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)。DALL-E 是基於 Transformer 架構的生成式 AI 模型，使用 _自回歸 Transformer_。

自回歸 Transformer 定義了模型如何根據文字描述生成影像，它一次生成一個像素，然後使用生成的像素生成下一個像素。通過神經網絡的多層處理，直到影像完成。

通過這個過程，DALL-E 可以控制生成影像中的屬性、物件、特徵等。然而，DALL-E 2 和 3 對生成影像的控制能力更強。

## 建立您的第一個影像生成應用程式

那麼建立影像生成應用程式需要什麼呢？您需要以下庫：

- **python-dotenv**，強烈建議使用此庫將您的機密保存在 _.env_ 文件中，遠離代碼。
- **openai**，此庫用於與 OpenAI API 交互。
- **pillow**，用於在 Python 中處理影像。
- **requests**，幫助您發送 HTTP 請求。

## 建立並部署 Azure OpenAI 模型

如果尚未完成，請按照 [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) 頁面的指示建立 Azure OpenAI 資源和模型。選擇 DALL-E 3 作為模型。

## 建立應用程式

1. 建立一個名為 _.env_ 的文件，內容如下：

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   在 Azure OpenAI Foundry Portal 的「部署」部分找到此信息。

1. 將上述庫收集到名為 _requirements.txt_ 的文件中，如下所示：

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. 接下來，建立虛擬環境並安裝這些庫：

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   對於 Windows，用以下命令建立並啟用虛擬環境：

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

以下是代碼的解釋：

- 首先，我們導入所需的庫，包括 OpenAI 庫、dotenv 庫、requests 庫和 Pillow 庫。

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- 接下來，我們從 _.env_ 文件中加載環境變數。

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- 然後，我們配置 Azure OpenAI 服務客戶端。

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- 接下來，我們生成影像：

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  上述代碼返回一個包含生成影像 URL 的 JSON 對象。我們可以使用該 URL 下載影像並保存到文件中。

- 最後，我們打開影像並使用標準影像查看器顯示它：

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### 更詳細的影像生成

讓我們更詳細地看看生成影像的代碼：

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt** 是用於生成影像的文字提示。在此例中，我們使用的提示是「兔子騎在馬上，手拿棒棒糖，站在霧氣瀰漫的長滿水仙花的草地上」。
- **size** 是生成影像的大小。在此例中，我們生成的影像大小為 1024x1024 像素。
- **n** 是生成影像的數量。在此例中，我們生成了兩張影像。
- **temperature** 是控制生成式 AI 模型輸出隨機性的參數。溫度值介於 0 到 1 之間，其中 0 表示輸出是確定性的，1 表示輸出是隨機的。默認值為 0.7。

還有更多可以對影像進行的操作，我們將在下一部分中介紹。

## 影像生成的其他功能

到目前為止，您已看到如何使用幾行 Python 代碼生成影像。然而，影像生成還有更多功能。

您還可以執行以下操作：

- **進行編輯**。通過提供現有影像、遮罩和提示，您可以修改影像。例如，您可以在影像的一部分添加某些內容。想像一下我們的兔子影像，您可以給兔子添加一頂帽子。您可以通過提供影像、遮罩（識別需要更改的區域）和文字提示來完成此操作。
> 注意：這在 DALL-E 3 中不支持。

以下是使用 GPT Image 的示例：

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  基礎影像僅包含帶泳池的休息室，但最終影像會有一隻火烈鳥：

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.tw.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.tw.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.tw.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **創建變化**。這個想法是您可以使用現有影像並要求生成變化。要創建變化，您需要提供影像和文字提示，並使用如下代碼：

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > 注意：這僅在 OpenAI 上支持。

## 溫度

溫度是控制生成式 AI 模型輸出隨機性的參數。溫度值介於 0 到 1 之間，其中 0 表示輸出是確定性的，1 表示輸出是隨機的。默認值為 0.7。

讓我們通過兩次運行以下提示來看看溫度的作用：

> 提示：「兔子騎在馬上，手拿棒棒糖，站在霧氣瀰漫的長滿水仙花的草地上」

![兔子騎在馬上，手拿棒棒糖，版本 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.tw.png)

現在再次運行相同的提示，看看是否會生成不同的影像：

![生成的兔子騎在馬上的影像](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.tw.png)

如您所見，影像相似但不完全相同。讓我們嘗試將溫度值更改為 0.1，看看會發生什麼：

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### 更改溫度

讓我們嘗試使輸出更具確定性。我們可以從生成的兩張影像中觀察到，第一張影像中有兔子，第二張影像中有馬，因此影像差異很大。

因此，讓我們更改代碼並將溫度設置為 0，如下所示：

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

現在運行此代碼，您將得到以下兩張影像：

- ![溫度 0，版本 1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.tw.png)
- ![溫度 0，版本 2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.tw.png)

在這裡，您可以清楚地看到影像更相似。

## 如何使用元提示為您的應用程式定義界限

通過我們的演示，我們已經可以為客戶生成影像。然而，我們需要為應用程式創建一些界限。

例如，我們不希望生成不適合工作環境或不適合兒童的影像。

我們可以使用 _元提示_ 來實現這一點。元提示是用於控制生成式 AI 模型輸出的文字提示。例如，我們可以使用元提示來控制輸出，確保生成的影像適合工作環境或適合兒童。

### 它如何運作？

那麼，元提示如何運作？

元提示是用於控制生成式 AI 模型輸出的文字提示，它們位於文字提示之前，用於控制模型的輸出，並嵌入到應用程式中以控制模型的輸出。將提示輸入和元提示輸入封裝在單一文字提示中。

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

從上述提示中，您可以看到所有生成的影像都考慮了元提示。

## 作業 - 讓學生參與

我們在本課程開始時介紹了 Edu4All。現在是時候讓學生為他們的評估生成影像了。

學生將為他們的評估創建包含紀念碑的影像，具體選擇哪些紀念碑由學生決定。學生被要求在此任務中發揮創意，將這些紀念碑置於不同的背景中。

## 解決方案

以下是一個可能的解決方案：
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

## 做得好！繼續學習

完成本課程後，請查看我們的[生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，繼續提升您的生成式 AI 知識！

前往第 10 課，我們將探討如何[使用低代碼構建 AI 應用程式](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不精確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。
=======
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
>>>>>>> 584a21c5 (Please enter the commit message for your changes. Lines starting)
