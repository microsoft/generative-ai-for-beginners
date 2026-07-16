# 建立圖像生成應用程式

[![建立圖像生成應用程式](../../../translated_images/zh-HK/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

大型語言模型（LLM）不僅限於文字生成，也能根據文字描述生成圖像。在醫療科技、建築、旅遊、遊戲開發等多個領域，圖像作為一種媒介非常有用。在本章中，我們將了解兩個最受歡迎的圖像生成模型：DALL-E 和 Midjourney。

## 介紹

在本課程中，我們將涵蓋：

- 圖像生成及其用途。
- 什麼是 DALL-E 和 Midjourney，以及它們的運作方式。
- 如何建立一個圖像生成應用程式。

## 學習目標

完成本課程後，你將能夠：

- 建立圖像生成應用程式。
- 利用元提示（meta prompts）為應用程式設定範圍。
- 使用 DALL-E 和 Midjourney。

## 為什麼要建立圖像生成應用程式？

圖像生成應用程式是探索生成式 AI 能力的好方法。它們可用於例如：

- <strong>圖像編輯與合成</strong>。你可以根據不同用途生成圖像，如圖像編輯和圖像合成。

- <strong>應用於多個產業</strong>。也可用於生成醫療科技、旅遊、遊戲開發等不同產業的圖像。

## 情境範例：Edu4All

本課程中，我們將繼續與我們的初創企業 Edu4All 合作。學生將為他們的評估創作圖像，具體圖像內容由學生決定，可以是他們自己的童話故事插圖，或者為故事創造新角色，幫助他們將想法和概念視覺化。

若學生在課堂上探討古蹟，Edu4All 的學生可能會生成如下圖所示的圖像：

![Edu4All startup, class on monuments, Eiffel Tower](../../../translated_images/zh-HK/startup.94d6b79cc4bb3f5a.webp)

使用類似以下提示詞

> 「早晨陽光下埃菲爾鐵塔旁的狗」

## 什麼是 DALL-E 和 Midjourney？

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) 和 [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) 是兩個最流行的圖像生成模型，允許你用提示詞生成圖像。

### DALL-E

讓我們先從 DALL-E 開始，這是一個根據文字描述生成圖像的生成式 AI 模型。

> [DALL-E 是兩個模型 CLIP 與擴散注意力 （diffused attention）的結合](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)。

- **CLIP**，是一個從圖像和文字中生成嵌入向量（數字表示）的模型。


- <strong>擴散注意力</strong>，是一種從嵌入向量生成圖像的模型。DALL-E 經過圖像和文本數據集的訓練，可以用來根據文本描述生成圖像。例如，DALL-E 可以用來生成戴帽子的貓，或是帶莫霍克髮型的狗的圖像。

### Midjourney

Midjourney 的運作方式與 DALL-E 類似，它是根據文字提示生成圖像。Midjourney 也可以使用類似「戴帽子的貓」或「帶莫霍克髮型的狗」這樣的提示來生成圖像。

![由 Midjourney 生成的機械鴿子圖像](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_圖片來源 Wikipedia，由 Midjourney 生成的圖像_

## DALL-E 和 Midjourney 是如何工作的

首先，[DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)。DALL-E 是基於變壓器架構的生成式 AI 模型，具有 _自回歸變壓器_。

_自回歸變壓器_ 定義了模型如何根據文本描述生成圖像，該模型一次生成一個像素，然後利用已生成的像素來生成下一個像素。圖像通過神經網絡中的多層進行傳遞，直到圖像完成。

透過這個過程，DALL-E 可以控制生成圖像中的屬性、物體、特徵等。然而，DALL-E 2 和 3 對生成圖像的控制能力更強。

## 建立您的第一個圖像生成應用程式

那麼，要建立一個圖像生成應用程式需要什麼？你需要以下的庫：

- **python-dotenv**，強烈建議使用這個庫將您的憑證存放在 _.env_ 文件中，並且與程式碼分離。
- **openai**，這是您與 OpenAI API 互動所需使用的庫。
- **pillow**，用於在 Python 中處理圖像。
- **requests**，幫助您進行 HTTP 請求。

## 建立並部署 Azure OpenAI 模型

如果尚未完成，請依照 [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) 頁面上的指引
建立 Azure OpenAI 資源和模型。選擇 **gpt-image-1** 作為模型（目前世代的 Azure OpenAI 圖像模型；DALL-E 3 已屬於舊版，且不再對新部署開放）。

## 建立應用程式

1. 創建一個 _.env_ 文件，並填入以下內容：

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   可在 Azure OpenAI Foundry 入口網站為您的資源的「Deployments」部分找到這些資訊。

1. 在一個名為 _requirements.txt_ 的檔案中收集上述庫，內容如下：

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. 接著，建立虛擬環境並安裝這些庫：

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```


   對於 Windows，請使用以下命令來建立並啟用您的虛擬環境：

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
        # 使用圖像生成 API 創建圖像
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # 設定存放圖像的目錄
        image_dir = os.path.join(os.curdir, 'images')

        # 如果目錄不存在，則建立它
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # 初始化圖像路徑（注意檔案類型應為 png）
        image_path = os.path.join(image_dir, 'generated-image.png')

        # 取得生成的圖像
        image_url = generation_response.data[0].url  # 從回應中擷取圖像 URL
        generated_image = requests.get(image_url).content  # 下載圖像
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # 在預設的圖像檢視器中顯示圖像
        image = Image.open(image_path)
        image.show()

    # 捕捉例外狀況
    except openai.BadRequestError as err:
        print(err)
   ```

讓我們解釋這段程式碼：

- 首先，我們匯入所需的函式庫，包括 OpenAI 函式庫、dotenv 函式庫、requests 函式庫和 Pillow 函式庫。

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- 接著，我們從 _.env_ 檔案載入環境變數。

  ```python
  # 引入 dotenv
  dotenv.load_dotenv()
  ```

- 之後，我們設定 Azure OpenAI 服務客戶端

  ```python
  # 從環境變量獲取端點和密鑰
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- 接下來，我們生成圖片：

  ```python
  # 使用圖像生成 API 創建圖像
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  上述程式碼會回應一個包含生成圖片 URL 的 JSON 物件。我們可以利用該 URL 下載圖片並儲存至檔案。

- 最後，我們開啟圖片並使用標準圖片檢視器顯示它：

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### 更多生成圖片的細節

讓我們更詳細地看看生成圖片的程式碼：

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt** 是用來生成圖片的文字提示。在本例中，我們使用的提示是「Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils」。
- **size** 是生成圖片的尺寸。在本例中，我們生成的圖片尺寸是 1024x1024 像素。
- **n** 是生成的圖片數量。在本例中，我們生成兩張圖片。
- **temperature** 是一個控制生成式 AI 模型輸出隨機性的參數。溫度值介於 0 到 1 之間，其中 0 表示輸出是確定性的，1 表示輸出是隨機的。預設值為 0.7。

還有更多你可以對圖片做的操作，我們將在下一章節中介紹。

## 圖像生成的額外功能

到目前為止，你已經看到我們如何用幾行 Python 生成一張圖片。然而，你還可以對圖片執行更多操作。

你還可以做到以下事情：

- <strong>執行編輯</strong>。通過提供一張現有圖片、一個遮罩和一個提示詞，你可以修改圖片。例如，你可以在圖片的某一部分新增元素。想像我們的兔子圖片，你可以給兔子加一頂帽子。你做法是提供原圖、一個遮罩（標示出要修改的區域）和一段文字提示說明該怎麼做。
> 注意：這在 DALL-E 3 中尚不支援。
 
這裡有一個 GPT Image 的範例：

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  原始圖片只包含帶泳池的休閒區，但最後的圖片會有一隻火烈鳥：

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/zh-HK/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/zh-HK/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/zh-HK/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- <strong>創建變體</strong>。基本概念是你拿一張現有的圖片，讓模型產生不同的變體。要創建變體，你提供一張圖片和一段文字提示，並用程式碼像下面這樣呼叫：

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > 注意，此功能僅支援 OpenAI 的 DALL-E 2 模型，不支援 gpt-image-1

## 溫度參數

溫度是控制生成式 AI 模型輸出隨機性的參數。溫度值介於 0 與 1 之間，0 表示輸出是確定性的，1 表示輸出是隨機的。預設值是 0.7。

讓我們看個範例，透過這段提示詞連續執行兩次：

> 提示： "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![Bunny on a horse holding a lollipop, version 1](../../../translated_images/zh-HK/v1-generated-image.a295cfcffa3c13c2.webp)

現在我們再次執行相同提示，看看是否會產生完全相同的圖片：

![Generated image of bunny on horse](../../../translated_images/zh-HK/v2-generated-image.33f55a3714efe61d.webp)

如你所見，圖片相似但並不完全相同。讓我們嘗試將溫度設為 0.1，看看結果如何：

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # 在這裡輸入你的提示文字
        size='1024x1024',
        n=2
    )
```

### 變更溫度參數

讓我們試著讓回應更確定性。我們可以從兩張生成的圖片觀察到，第一張是兔子，第二張是馬，圖片差異很大。

因此，我們改變程式碼，將溫度設為 0，像這樣：

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # 輸入你的提示文字於此
        size='1024x1024',
        n=2,
        temperature=0
    )
```

現在執行此程式碼，你會得到以下兩張圖片：

- ![Temperature 0, v1](../../../translated_images/zh-HK/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![Temperature 0 , v2](../../../translated_images/zh-HK/v2-temp-generated-image.871d0c920dbfb0f1.webp)

你可以清楚看出兩張圖片更為相似。

## 如何用元提示定義應用程式的邊界

透過我們的示範，我們已能為客戶產生圖片。但我們需要為應用設定一些邊界。

例如，我們不希望生成不適合工作場合的圖片，或不適合兒童觀看的圖片。

我們可以用 _元提示_（metaprompts）來達成。元提示是用來控制生成式 AI 模型輸出的文字提示。例如，我們可以用元提示控制輸出，確保所生成的圖片在工作場合安全或兒童適宜。

### 它如何運作？

那麼，元提示是怎麼運作的？

元提示是用來控制生成式 AI 模型輸出的文字提示，它會置於文字提示之前，用來控制模型的輸出，並嵌入應用中以控管模型輸出。將提示輸入和元提示輸入封裝成單一文字提示。

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

# TODO 添加請求以生成圖像
```

從上述提示中，你可以看到所有產生的圖片都考慮到了元提示。

## 作業 - 讓學生啟用此功能

我們在本課開始時介紹了 Edu4All。現在，是時候讓學生能為他們的評量生成圖片。


學生將為他們的評估創建包含紀念碑的圖像，具體是哪些紀念碑由學生決定。學生被要求在此任務中運用創意，將這些紀念碑置於不同的場景中。

## 解決方案

以下是一個可能的解決方案：

```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# 載入 dotenv
dotenv.load_dotenv()

# 從環境變數取得端點和金鑰
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
    # 使用影像生成 API 建立圖片
    generation_response = client.images.generate(
        prompt=prompt,    # 在此輸入你的提示文字
        size='1024x1024',
        n=1,
    )
    # 設定儲存圖片的目錄
    image_dir = os.path.join(os.curdir, 'images')

    # 若目錄不存在，則建立它
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # 初始化圖片路徑（注意檔案類型應為 png）
    image_path = os.path.join(image_dir, 'generated-image.png')

    # 取得生成的圖片
    image_url = generation_response.data[0].url  # 從回應中提取圖片網址
    generated_image = requests.get(image_url).content  # 下載圖片
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # 在預設圖片檢視器中顯示圖片
    image = Image.open(image_path)
    image.show()

# 捕捉例外狀況
except openai.BadRequestError as err:
    print(err)
```

## 做得好！繼續你的學習

完成本課程後，查看我們的[生成式 AI 學習收藏](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)以繼續提升你的生成式 AI 知識！

前往第10課，我們將探討如何[使用低代碼構建 AI 應用程式](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->