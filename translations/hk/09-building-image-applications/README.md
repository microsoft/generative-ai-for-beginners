<<<<<<< HEAD
<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "063a2ac57d6b71bea0eaa880c68770d2",
  "translation_date": "2025-09-29T21:32:02+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "hk"
}
-->
# 建立圖像生成應用程式

[![建立圖像生成應用程式](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.hk.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

大型語言模型（LLM）不僅僅能生成文字，還可以根據文字描述生成圖像。圖像作為一種模態在許多領域都非常有用，例如醫療技術、建築、旅遊、遊戲開發等。在本章中，我們將探討兩個最受歡迎的圖像生成模型：DALL-E 和 Midjourney。

## 簡介

在本課程中，我們將涵蓋以下內容：

- 圖像生成及其重要性。
- DALL-E 和 Midjourney 的介紹及其工作原理。
- 如何建立一個圖像生成應用程式。

## 學習目標

完成本課程後，您將能夠：

- 建立一個圖像生成應用程式。
- 使用元提示（meta prompts）為您的應用程式定義邊界。
- 使用 DALL-E 和 Midjourney。

## 為什麼要建立圖像生成應用程式？

圖像生成應用程式是一個探索生成式 AI 能力的絕佳方式。它們可以用於以下用途，例如：

- **圖像編輯和合成**。您可以生成各種用途的圖像，例如圖像編輯和合成。

- **應用於多個行業**。它們還可以用於生成適用於多個行業的圖像，例如醫療技術、旅遊、遊戲開發等。

## 情境：Edu4All

在本課程中，我們將繼續與我們的初創公司 Edu4All 合作。學生將為他們的作業創建圖像，具體創建什麼圖像由學生決定，例如可以是他們自己童話故事的插圖，或者創建故事中的新角色，幫助他們將想法和概念可視化。

以下是 Edu4All 的學生在課堂上學習紀念碑時可能生成的示例：

![Edu4All 初創公司，課堂上的紀念碑，艾菲爾鐵塔](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.hk.png)

使用以下提示：

> 「清晨陽光下，狗站在艾菲爾鐵塔旁」

## DALL-E 和 Midjourney 是什麼？

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) 和 [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) 是兩個最受歡迎的圖像生成模型，它們允許您使用提示生成圖像。

### DALL-E

首先介紹 DALL-E，它是一個生成式 AI 模型，可以根據文字描述生成圖像。

> [DALL-E 是兩個模型的結合：CLIP 和擴散注意力](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)。

- **CLIP** 是一個模型，可以從圖像和文字生成嵌入（數據的數字表示）。

- **擴散注意力** 是一個模型，可以根據嵌入生成圖像。DALL-E 是基於圖像和文字數據集訓練的，可以用於根據文字描述生成圖像。例如，DALL-E 可以生成戴帽子的貓或有莫霍克髮型的狗的圖像。

### Midjourney

Midjourney 的工作方式與 DALL-E 類似，它根據文字提示生成圖像。Midjourney 也可以使用像「戴帽子的貓」或「有莫霍克髮型的狗」這樣的提示生成圖像。

![由 Midjourney 生成的圖像，機械鴿子](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_圖片來源：維基百科，由 Midjourney 生成_

## DALL-E 和 Midjourney 的工作原理

首先，[DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)。DALL-E 是基於 Transformer 架構的生成式 AI 模型，使用 _自回歸 Transformer_。

自回歸 Transformer 定義了模型如何根據文字描述生成圖像，它一次生成一個像素，然後使用生成的像素生成下一個像素。通過神經網絡的多層處理，直到圖像完成。

通過這個過程，DALL-E 可以控制生成圖像中的屬性、物件、特徵等。然而，DALL-E 2 和 3 對生成的圖像有更多的控制。

## 建立您的第一個圖像生成應用程式

那麼建立一個圖像生成應用程式需要什麼呢？您需要以下庫：

- **python-dotenv**，強烈建議使用此庫將您的密鑰保存在 _.env_ 文件中，遠離代碼。
- **openai**，此庫用於與 OpenAI API 交互。
- **pillow**，用於在 Python 中處理圖像。
- **requests**，幫助您發送 HTTP 請求。

## 創建並部署 Azure OpenAI 模型

如果尚未完成，請按照 [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) 頁面的指示創建 Azure OpenAI 資源和模型。選擇 DALL-E 3 作為模型。

## 創建應用程式

1. 創建一個名為 _.env_ 的文件，內容如下：

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   在 Azure OpenAI Foundry Portal 的「部署」部分找到此信息。

1. 將上述庫收集到一個名為 _requirements.txt_ 的文件中，如下所示：

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. 接下來，創建虛擬環境並安裝這些庫：

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   對於 Windows，用以下命令創建並激活虛擬環境：

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

- 接著，我們從 _.env_ 文件中加載環境變數。

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

- 接下來，我們生成圖像：

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  上述代碼返回一個包含生成圖像 URL 的 JSON 對象。我們可以使用該 URL 下載圖像並保存到文件中。

- 最後，我們打開圖像並使用標準圖像查看器顯示它：

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### 更詳細的圖像生成代碼

讓我們更詳細地看看生成圖像的代碼：

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt** 是用於生成圖像的文字提示。在此例中，我們使用的提示是「兔子騎在馬上，拿著棒棒糖，站在霧氣瀰漫的長滿水仙花的草地上」。
- **size** 是生成圖像的大小。在此例中，我們生成的圖像大小為 1024x1024 像素。
- **n** 是生成的圖像數量。在此例中，我們生成了兩張圖像。
- **temperature** 是控制生成式 AI 模型輸出隨機性的參數。溫度值介於 0 到 1 之間，其中 0 表示輸出是確定性的，1 表示輸出是隨機的。默認值為 0.7。

還有更多可以對圖像進行的操作，我們將在下一部分中介紹。

## 圖像生成的其他功能

到目前為止，您已經看到如何使用幾行 Python 代碼生成圖像。然而，您還可以對圖像進行更多操作。

您還可以執行以下操作：

- **進行編輯**。通過提供現有圖像、遮罩和提示，您可以修改圖像。例如，您可以在圖像的一部分添加某些內容。想像一下我們的兔子圖像，您可以給兔子添加一頂帽子。您可以通過提供圖像、遮罩（識別需要更改的部分區域）和文字提示來完成此操作。
> 注意：這在 DALL-E 3 中不支持。

以下是使用 GPT 圖像的示例：

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  基礎圖像僅包含泳池旁的休息室，但最終圖像會有一隻火烈鳥：

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.hk.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.hk.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.hk.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **創建變體**。這個想法是您可以基於現有圖像生成變體。要創建變體，您需要提供一張圖像和文字提示，並使用如下代碼：

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > 注意：這僅在 OpenAI 中支持。

## 溫度

溫度是一個控制生成式 AI 模型輸出隨機性的參數。溫度值介於 0 到 1 之間，其中 0 表示輸出是確定性的，1 表示輸出是隨機的。默認值為 0.7。

讓我們通過兩次運行以下提示來看看溫度的作用：

> 提示：「兔子騎在馬上，拿著棒棒糖，站在霧氣瀰漫的長滿水仙花的草地上」

![兔子騎在馬上，拿著棒棒糖，版本 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.hk.png)

現在再次運行相同的提示，看看是否會生成不同的圖像：

![生成的兔子騎在馬上的圖像](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.hk.png)

如您所見，圖像相似但不完全相同。現在嘗試將溫度值更改為 0.1，看看會發生什麼：

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### 更改溫度

讓我們嘗試使輸出更具確定性。我們可以從生成的兩張圖像中觀察到，第一張圖像中有兔子，第二張圖像中有馬，因此圖像差異很大。

因此，我們將代碼更改為將溫度設置為 0，如下所示：

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

現在運行此代碼，您將獲得以下兩張圖像：

- ![溫度 0，版本 1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.hk.png)
- ![溫度 0，版本 2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.hk.png)

在這裡，您可以清楚地看到圖像更加相似。

## 如何使用元提示為您的應用程式定義邊界

通過我們的演示，我們已經可以為客戶生成圖像。然而，我們需要為應用程式設置一些邊界。

例如，我們不希望生成不適合工作環境或不適合兒童的圖像。

我們可以使用 _元提示_ 來實現這一點。元提示是用於控制生成式 AI 模型輸出的文字提示。例如，我們可以使用元提示來控制輸出，確保生成的圖像適合工作環境或適合兒童。

### 它是如何工作的？

那麼，元提示是如何工作的呢？

元提示是用於控制生成式 AI 模型輸出的文字提示，它們位於文字提示之前，用於控制模型的輸出，並嵌入到應用程式中以控制模型的輸出。將提示輸入和元提示輸入封裝在一個文字提示中。

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

從上述提示中，您可以看到所有生成的圖像都考慮了元提示。

## 作業 - 讓學生參與

我們在本課程開始時介紹了 Edu4All。現在是時候讓學生為他們的作業生成圖像了。

學生將為他們的作業生成包含紀念碑的圖像，具體選擇哪些紀念碑由學生決定。學生被要求在這項任務中發揮創意，將這些紀念碑置於不同的背景中。

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

完成這節課後，請查看我們的[生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，繼續提升你的生成式 AI 知識！

前往第10課，我們將探討如何[使用低代碼構建 AI 應用程式](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。
=======
<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef74ad58fc01f7ad80788f79505f9816",
  "translation_date": "2025-08-26T14:53:21+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "hk"
}
-->
# 建立圖像生成應用程式

[![建立圖像生成應用程式](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.hk.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

大型語言模型（LLM）唔止可以用嚟生產文字，仲可以根據文字描述生成圖像。圖像呢個媒介喺好多領域都好有用，例如醫療科技、建築、旅遊、遊戲開發等等。今章我哋會介紹兩個最受歡迎嘅圖像生成模型：DALL-E 同 Midjourney。

## 前言

今堂會講：

- 圖像生成同佢嘅用途
- DALL-E 同 Midjourney 係咩、點運作
- 點樣建立一個圖像生成應用程式

## 學習目標

完成今堂之後，你會識得：

- 建立一個圖像生成應用程式
- 用 meta prompt 為你嘅應用程式設定界線
- 操作 DALL-E 同 Midjourney

## 點解要建立圖像生成應用程式？

圖像生成應用程式係探索生成式 AI 能力嘅好方法。佢哋可以用嚟：

- **圖像編輯同合成**。你可以根據唔同用途生成圖像，例如圖像編輯或者合成。

- **應用喺唔同產業**。仲可以用嚟為唔同產業生成圖像，例如醫療科技、旅遊、遊戲開發等等。

## 情景：Edu4All

今堂我哋會繼續用我哋嘅初創公司 Edu4All。學生可以為佢哋嘅評估創作圖像，畫咩圖就由學生自己決定，可以係自己童話故事嘅插圖、創造新角色、或者幫助佢哋將想法同概念視覺化。

例如，如果學生喺課堂上學緊名勝古蹟，佢哋可以生成以下圖像：

![Edu4All startup, class on monuments, Eiffel Tower](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.hk.png)

用呢個 prompt：

> 「狗喺清晨陽光下企喺巴黎鐵塔旁邊」

## DALL-E 同 Midjourney 係咩？

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) 同 [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) 係目前最受歡迎嘅兩個圖像生成模型，佢哋可以用 prompt 生成圖像。

### DALL-E

先講 DALL-E，佢係一個生成式 AI 模型，可以根據文字描述生成圖像。

> [DALL-E 其實係由兩個模型組成，CLIP 同 diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)。

- **CLIP** 係一個模型，可以根據圖像同文字產生 embedding（即數值表示）。

- **Diffused attention** 係一個模型，可以根據 embedding 生成圖像。DALL-E 係用大量圖像同文字訓練出嚟，可以根據文字描述生成圖像。例如，DALL-E 可以生成戴帽嘅貓，或者有莫霍克頭嘅狗。

### Midjourney

Midjourney 嘅運作方式同 DALL-E 差唔多，佢都係根據文字 prompt 生成圖像。你可以用 prompt 例如「戴帽嘅貓」或者「有莫霍克頭嘅狗」嚟生成圖像。

![Midjourney 生成嘅圖像，機械鴿子](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_圖片來源 Wikipedia，圖像由 Midjourney 生成_

## DALL-E 同 Midjourney 點運作

首先，[DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)。DALL-E 係一個基於 transformer 架構嘅生成式 AI 模型，採用 _自回歸 transformer_。

自回歸 transformer 係指模型點樣根據文字描述逐個像素生成圖像，每次生成一個像素，再用已生成嘅像素去生成下一個像素。經過神經網絡多層處理，直到成個圖像完成。

透過呢個過程，DALL-E 可以控制圖像入面嘅屬性、物件、特徵等等。而 DALL-E 2 同 3 對生成圖像嘅控制力更高。

## 建立你第一個圖像生成應用程式

咁要建立一個圖像生成應用程式需要啲咩？你要用以下幾個 library：

- **python-dotenv**，建議用呢個 library 將敏感資料放喺 _.env_ 檔案，唔好直接寫喺程式碼入面。
- **openai**，用嚟同 OpenAI API 溝通。
- **pillow**，用嚟喺 Python 處理圖像。
- **requests**，用嚟發 HTTP 請求。

## 建立同部署 Azure OpenAI 模型

如果你未做過，可以跟住 [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) 嘅指引
建立一個 Azure OpenAI 資源同模型。記得揀 DALL-E 3 做模型。  

## 建立應用程式

1. 建立一個 _.env_ 檔案，內容如下：

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   呢啲資料可以喺 Azure OpenAI Foundry Portal 嘅 "Deployments" 部分搵到。

1. 將以上 library 寫入 _requirements.txt_ 檔案：

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. 然後，建立虛擬環境並安裝 library：

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   如果你用 Windows，可以用以下指令建立同啟動虛擬環境：

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. 喺 _app.py_ 檔案加入以下程式碼：

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

解釋一下呢段程式碼：

- 首先，我哋 import 需要用嘅 library，包括 OpenAI、dotenv、requests、Pillow。

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- 然後，從 _.env_ 檔案讀取環境變數。

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- 之後，設定 Azure OpenAI 服務 client 

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- 跟住，生成圖像：

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  上面嘅程式碼會回傳一個 JSON 物件，入面有生成圖像嘅 URL。我哋可以用呢個 URL 下載圖像並儲存成檔案。

- 最後，打開圖像，用標準圖像檢視器顯示出嚟：

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### 更詳細解釋生成圖像嘅程式碼

睇下生成圖像嘅程式碼詳情：

    ```python
      generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                            )
    ```

- **prompt**，就係用嚟生成圖像嘅文字提示。呢度用咗「兔仔騎馬，手拎住棒棒糖，喺長滿水仙花嘅霧氣草原上」。
- **size**，係生成圖像嘅尺寸。呢度係 1024x1024 像素。
- **n**，係生成圖像嘅數量。呢度係生成兩張圖。
- **temperature**，係控制生成式 AI 模型輸出隨機性嘅參數。值介乎 0 到 1，0 代表輸出固定，1 代表輸出好隨機。預設值係 0.7。

仲有更多圖像相關功能，下一節會再講。

## 圖像生成嘅其他功能

你見到我哋只用幾行 Python 就可以生成圖像。不過，其實仲有其他功能：

你仲可以做到：

- **編輯圖像**。只要提供一張現有圖像、一個遮罩同一個 prompt，就可以改變圖像某部分。例如，可以幫兔仔加頂帽。做法係提供原圖、遮罩（標示要改嘅部分）同文字 prompt，講明要加啲咩。
> 注意：DALL-E 3 暫時唔支援呢個功能。
 
以下係用 GPT Image 嘅例子：

    ```python
    response = client.images.edit(
        model="gpt-image-1",
        image=open("sunlit_lounge.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt="A sunlit indoor lounge area with a pool containing a flamingo"
    )
    image_url = response.data[0].url
    ```

  原本嘅圖只係有泳池同休息室，最後生成嘅圖就會有隻火烈鳥：

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="./images/sunlit_lounge.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/mask.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/sunlit_lounge_result.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **創建變化版本**。即係用一張現有圖像，要求生成唔同變化。做法係提供原圖同 prompt，再用以下程式碼：

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > 注意，呢個功能只支援 OpenAI

## Temperature（溫度）

Temperature 係控制生成式 AI 模型輸出隨機性嘅參數。值介乎 0 到 1，0 代表輸出固定，1 代表輸出好隨機。預設值係 0.7。

睇下 temperature 點運作，試下用同一個 prompt 生成兩次：

> Prompt : 「兔仔騎馬，手拎住棒棒糖，喺長滿水仙花嘅霧氣草原上」

![兔仔騎馬拎棒棒糖，第一版](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.hk.png)

再用同一個 prompt 生成一次，睇下會唔會一樣：

![生成嘅兔仔騎馬圖像](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.hk.png)

你見到，兩張圖雖然相似，但唔完全一樣。試下將 temperature 改做 0.1，睇下效果：

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### 改變 temperature

試下令輸出更固定。頭兩張圖，一張有兔仔，一張有馬，變化都幾大。

所以我哋改程式碼，將 temperature 設為 0：

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

再執行，就會見到以下兩張圖：

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.hk.png)
- ![Temperature 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.hk.png)

你會見到兩張圖更加相似。

## 用 metaprompt 為應用程式設定界線

用我哋嘅 demo，已經可以幫客戶生成圖像。不過，我哋要為應用程式設定界線。

例如，我哋唔想生成唔適合工作場合或者唔適合小朋友嘅圖像。

可以用 _metaprompt_（元提示）做到。Metaprompt 係用嚟控制生成式 AI 模型輸出嘅文字提示。例如，可以用 metaprompt 控制輸出，確保生成嘅圖像適合工作場合或者小朋友。

### 點運作？

咁 metaprompt 點用？

Metaprompt 係用嚟控制生成式 AI 模型輸出嘅文字提示，佢會放喺主 prompt 前面，嵌入應用程式入面，控制模型嘅輸出。即係將主 prompt 同 metaprompt 合併成一個文字提示。

例如以下呢個 metaprompt：

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

而家睇下點用 metaprompt 喺我哋嘅 demo 入面。

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

你會見到，所有生成嘅圖像都會考慮 metaprompt 嘅要求。

## 任務 - 讓學生動手

我哋喺今堂一開始介紹咗 Edu4All。依家就讓學生自己生成評估用嘅圖像。

學生要為評估創作包含名勝古蹟嘅圖像，畫咩名勝就由學生自己決定。鼓勵學生發揮創意，將名勝放喺唔同情境。

## 參考答案

以下係一個可能嘅答案：

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
完成呢課之後，可以去睇下我哋嘅 [生成式 AI 學習專區](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，繼續提升你對生成式 AI 嘅認識！

去到第 10 課，我哋會一齊探討下點樣用低代碼去 [建立 AI 應用程式](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**免責聲明**：
本文件經由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能會有錯誤或不準確之處。原始語言的文件應被視為具權威性的來源。對於重要資訊，建議使用專業人工翻譯。我們不會對因使用本翻譯而產生的任何誤解或錯誤負責。
>>>>>>> 584a21c5 (Please enter the commit message for your changes. Lines starting)
