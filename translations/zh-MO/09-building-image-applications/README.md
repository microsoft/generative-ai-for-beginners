# 建立圖像生成應用程式

[![建立圖像生成應用程式](../../../translated_images/zh-MO/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

大型語言模型不只限於文本生成，同時也可以從文字描述中生成圖像。將圖像作為一種模態，在醫療科技、建築、旅遊、遊戲開發等多個領域非常有用。在本章中，我們將探討兩種最受歡迎的圖像生成模型，DALL-E 與 Midjourney。

## 介紹

在本課程中，我們將涵蓋：

- 圖像生成及其重要性。
- DALL-E 和 Midjourney 是什麼以及它們如何運作。
- 如何構建圖像生成應用程式。

## 學習目標

完成本課程後，你將能夠：

- 建立一個圖像生成應用程式。
- 使用元提示定義應用程式的邊界。
- 操作 DALL-E 和 Midjourney。

## 為什麼要建構圖像生成應用程式？

圖像生成應用程式是探索生成式人工智能能力的絕佳方式。它們可用於例如：

- <strong>圖像編輯與合成</strong>。可為多種用途生成圖像，如圖像編輯與圖像合成。

- <strong>應用於多個產業</strong>。亦可用於醫療科技、旅遊、遊戲開發等多種產業的圖像生成。

## 情境範例：Edu4All

作為本課程的一部分，我們將繼續與我們的初創企業 Edu4All 合作。學生們會為評估創建圖像，圖像內容由學生決定，但可作為自己的童話插圖、創造故事角色，或幫助他們將想法與概念可視化。

以下是若學生在課堂上研究紀念碑，他們可能生成的圖像範例：

![Edu4All 初創企業，關於紀念碑的課堂，艾菲爾鐵塔](../../../translated_images/zh-MO/startup.94d6b79cc4bb3f5a.webp)

使用如下一個提示詞

> "清晨陽光中艾菲爾鐵塔旁的狗"

## 什麼是 DALL-E 和 Midjourney？

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) 和 [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) 是兩款最受歡迎的圖像生成模型，它們允許通過提示詞生成圖像。

### DALL-E

先從 DALL-E 開始，它是一種從文字描述生成圖像的生成式人工智能模型。

> [DALL-E 是兩種模型結合：CLIP 與擴散注意力 (diffused attention)](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)。

- **CLIP** 是一個能從圖像與文字產生數值表示（詞嵌入）的模型。

- <strong>擴散注意力</strong> 是一個從詞嵌入生成圖像的模型。DALL-E 訓練於圖像與文字的數據集上，可用於從文字敘述生成圖像。例如，DALL-E 可以生成戴帽子的貓或有莫霍克髮型的狗的圖像。

### Midjourney

Midjourney 運作方式與 DALL-E 類似，同樣從文字提示生成圖像。Midjourney 也可以使用像“戴帽子的貓”或“有莫霍克髮型的狗”這類提示生成圖像。

![由 Midjourney 生成的機械鴿子圖像](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_圖片來源 Wikipedia，由 Midjourney 生成_

## DALL-E 與 Midjourney 的運作方式

先來看看 [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)。DALL-E 是基於 Transformer 架構的生成式人工智能模型，使用 _自回歸 Transformer_。

_自回歸 Transformer_ 定義了模型如何從文字描述生成圖像，採用逐像素生成，一次生成一個像素，並使用已生成的像素來生成下一個像素，通過神經網絡多層處理，直到圖像完成。

透過此過程，DALL-E 能控制生成圖像中的屬性、物體、特徵等。不過，DALL-E 2 與 3 對生成圖像有更強的控制能力。

## 建立你的第一個圖像生成應用程式

那麼，建立圖像生成應用程式需要什麼呢？你需要以下函式庫：

- **python-dotenv**，強烈推薦使用這個函式庫，將你的秘密資訊保存在 _.env_ 檔案中，避免放在程式碼內。
- **openai**，此函式庫可用於與 OpenAI API 互動。
- **pillow**，用於在 Python 中處理圖像。
- **requests**，幫助你發出 HTTP 請求。

## 建立並部署 Azure OpenAI 模型

若尚未完成，請依照 [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) 頁面指示
建立 Azure OpenAI 資源與模型。選擇 **gpt-image-1** 作為模型（目前世代的 Azure OpenAI 圖像模型；DALL-E 3 已為舊版，不再對新部署提供）。

## 建立應用程式

1. 建立一個 _.env_ 檔案，內容如下：

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   這些資訊可在 Azure OpenAI Foundry 入口網站中，於你的資源的「部署 (Deployments)」區段找到。

1. 將上述函式庫收集到一個名為 _requirements.txt_ 的檔案，內容如下：

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. 接著，建立虛擬環境並安裝函式庫：

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows 使用者可用以下指令建立並啟動虛擬環境：

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. 在名為 _app.py_ 的檔案中加入以下程式碼：


    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # import dotenv
    dotenv.load_dotenv()
    
    # 配置 Azure OpenAI 服務客戶端
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # 使用影像生成 API 創建影像
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # 設定存放影像的目錄
        image_dir = os.path.join(os.curdir, 'images')

        # 如果目錄不存在，則建立它
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # 初始化影像路徑（注意檔案類型應為 png）
        image_path = os.path.join(image_dir, 'generated-image.png')

        # 取得生成的影像
        image_url = generation_response.data[0].url  # 從回應中擷取影像 URL
        generated_image = requests.get(image_url).content  # 下載影像
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # 在預設的影像檢視器中顯示影像
        image = Image.open(image_path)
        image.show()

    # 捕捉例外狀況
    except openai.BadRequestError as err:
        print(err)
   ```

讓我們解釋這段代碼：

- 首先，我們匯入所需的函式庫，包括 OpenAI 函式庫、dotenv 函式庫、requests 函式庫和 Pillow 函式庫。

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- 然後，我們從 _.env_ 檔案載入環境變數。

  ```python
  # 匯入 dotenv
  dotenv.load_dotenv()
  ```

- 接著，我們設定 Azure OpenAI 服務客戶端 

  ```python
  # 從環境變數中獲取端點和密鑰
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- 接著，我們生成圖片：

  ```python
  # 使用圖像生成 API 建立圖像
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  上述代碼會回應一個包含生成圖片 URL 的 JSON 物件。我們可以使用該網址來下載圖片並保存到檔案中。

- 最後，我們開啟圖片並使用標準圖像檢視器顯示它：

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### 關於生成圖片的更多細節

讓我們更詳細地看看生成圖片的程式碼：

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**，是用來生成圖片的文字提示。在這個例子中，我們使用了提示 "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"。
- **size**，是生成圖片的大小。本例中，我們生成了 1024x1024 像素的圖片。
- **n**，是生成圖片的數量。本例中，我們生成兩張圖片。
- **temperature**，是一個控制生成式 AI 模型輸出隨機性的參數。值介於 0 和 1 之間，0 表示輸出是確定性的，1 表示輸出是隨機的。預設值是 0.7。

在下一節中，我們會介紹更多可以對圖片做的操作。

## 圖片產生的額外功能

到目前為止，你已經看到我們如何使用幾行 Python 代碼生成圖片。然而，對圖片你還可以做更多事情。

你還可以做以下事情：

- <strong>進行編輯</strong>。通過提供現有圖片、一個遮罩以及一個提示，你可以修改圖片。例如，你可以給圖片的一部分加上一些東西。想像我們的兔子圖片，你可以給兔子加一頂帽子。做法是提供圖片、一個遮罩（識別要更改的區域部分）和一段文字提示說明應該做什麼。 
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

  基本圖片只包含有泳池的休息室，但最後的圖片會有一隻火烈鳥：

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/zh-MO/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/zh-MO/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/zh-MO/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- <strong>創建變體</strong>。這個概念是你拿一張現有圖片，並要求系統創建該圖片的變體。要創建變體，你提供一張圖片和一個文字提示，像這樣：

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > 注意，這只支援 OpenAI 的 DALL-E 2 模型，不支援 gpt-image-1

## 溫度參數

溫度是一個控制生成式 AI 模型輸出隨機性的參數。值介於 0 和 1 之間，0 表示輸出是確定性的，1 表示輸出是隨機的。預設值是 0.7。

讓我們透過執行同一提示兩次，看看溫度如何影響結果：

> 提示 : "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![Bunny on a horse holding a lollipop, version 1](../../../translated_images/zh-MO/v1-generated-image.a295cfcffa3c13c2.webp)

現在我們執行同樣的提示，看看是否會得到兩張不同的圖片：

![Generated image of bunny on horse](../../../translated_images/zh-MO/v2-generated-image.33f55a3714efe61d.webp)

你可以看到圖片相似，但不相同。現在嘗試把溫度改為 0.1，看看結果如何：

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # 在此輸入您的提示文字
        size='1024x1024',
        n=2
    )
```

### 更改溫度

我們嘗試讓輸出更確定性。從剛剛產生的兩張圖片中可以觀察到，第一張有兔子，第二張有馬，圖片差異很大。

因此讓我們更改程式碼，設定溫度為 0，像這樣：

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # 在這裡輸入您的提示文本
        size='1024x1024',
        n=2,
        temperature=0
    )
```

現在當你執行此代碼，會得到以下兩張圖片：

- ![Temperature 0, v1](../../../translated_images/zh-MO/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![Temperature 0 , v2](../../../translated_images/zh-MO/v2-temp-generated-image.871d0c920dbfb0f1.webp)

你可以清楚看到這兩張圖片的相似度更高。

## 如何用元提示定義應用範圍邊界

透過我們的示範，我們已能為客戶生成圖片。但我們需要為應用程式建立一些邊界。

例如，我們不希望生成不適合工作場合或兒童觀看的圖片。

我們可以使用 _元提示_ （metaprompts）來做到這點。元提示是用來控制生成式 AI 輸出的文字提示。例如，我們可以使用元提示來控制輸出，確保生成的圖片是適合工作的，或者是適合兒童的。

### 它是怎麼運作的？

那麼，元提示如何運作？

元提示是用來控制生成式 AI 輸出的文字提示，它位於文本提示之前，用來控制模型的輸出，並被嵌入到應用程式中以控制模型的輸出。將提示輸入和元提示輸入封裝成一個單一的文本提示。

一個元提示的範例如下：

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

現在，讓我們看看如何在示範中使用元提示。

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

# 待辦事項 新增請求以生成圖像
```

從上述提示中可以看到，所有創建的圖片都考慮了元提示。

## 作業 - 讓學生能夠使用

我們在本課開始時介紹了 Edu4All。現在是時候讓學生能夠為他們的評估生成圖片。


學生將為他們的評估創作包含紀念碑的圖片，紀念碑的具體內容由學生自行決定。學生被要求在此任務中發揮創意，將這些紀念碑置於不同的情境中。

## 解決方案

這是一個可能的解決方案：

```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# import dotenv
dotenv.load_dotenv()

# 從環境變量取得端點和金鑰
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
  api_key=os.environ['AZURE_OPENAI_API_KEY'],
  api_version = "2024-10-21"
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
"""

try:
    # 使用圖像生成 API 建立圖像
    generation_response = client.images.generate(
        prompt=prompt,    # 在此輸入你的提示文字
        size='1024x1024',
        n=1,
    )
    # 設定儲存圖像的目錄
    image_dir = os.path.join(os.curdir, 'images')

    # 若目錄不存在，則建立它
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # 初始化圖像路徑（請注意檔案類型應為 png）
    image_path = os.path.join(image_dir, 'generated-image.png')

    # 取得生成的圖像
    image_url = generation_response.data[0].url  # 從回應中提取圖像 URL
    generated_image = requests.get(image_url).content  # 下載圖片
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # 在預設圖像檢視器中顯示圖片
    image = Image.open(image_path)
    image.show()

# 捕捉異常
except openai.BadRequestError as err:
    print(err)
```

## 幹得好！繼續您的學習旅程

完成本課程後，請查看我們的 [生成式 AI 學習收藏](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升您的生成式 AI 知識！

前往第10課，我們將探討如何 [使用低代碼構建 AI 應用程式](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->