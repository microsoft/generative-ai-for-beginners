# 建立影像生成應用程式

[![建立影像生成應用程式](../../../translated_images/zh-TW/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLM 不只限於文字生成，也能從文字描述生成影像。在醫療科技、建築、旅遊、遊戲開發等多個領域中，影像作為一種媒介非常有用。在本章節，我們將探討兩種最受歡迎的影像生成模型，DALL-E 與 Midjourney。

## 介紹

本課程將涵蓋：

- 影像生成及其應用價值。
- DALL-E 和 Midjourney 是什麼，以及它們的工作原理。
- 如何建置一個影像生成應用程式。

## 學習目標

完成本課程後，你將能夠：

- 建立影像生成應用程式。
- 利用 meta prompt 定義應用程式範圍。
- 使用 DALL-E 與 Midjourney。

## 為何要建立影像生成應用程式？

影像生成應用程式是探索生成式 AI 能力的好方法。它們可以用於例如：

- <strong>影像編輯和合成</strong>。你可以生成影像以應用於多種用途，如影像編輯和影像合成。

- <strong>應用於多種產業</strong>。也可以用於醫療科技、旅遊、遊戲開發等多個產業生成影像。

## 情境：Edu4All

在本課程中，我們將持續與新創企業 Edu4All 合作。學生將為自己的評量製作影像，影像內容由學生決定，可能是他們故事中的插畫，或是創造故事新角色，亦或幫助他們視覺化理念和概念。

以下是 Edu4All 學生在課堂上研究紀念碑時，可能會產出的影像範例：

![Edu4All 新創企業，紀念碑課堂，艾菲爾鐵塔](../../../translated_images/zh-TW/startup.94d6b79cc4bb3f5a.webp)

使用類似以下的提示字串

> "黎明晨光下，艾菲爾鐵塔旁的一隻狗"

## 什麼是 DALL-E 和 Midjourney？

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) 和 [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) 是兩款最受歡迎的影像生成模型，它們可以使用提示字串來生成影像。

### DALL-E

先從 DALL-E 講起，它是一款從文字描述生成影像的生成式 AI 模型。

> [DALL-E 結合了兩個模型，CLIP 與 diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)。

- **CLIP**，是一個從影像與文字中產生嵌入向量（數值化表示）的模型。

- **Diffused attention**，是一個從嵌入向量中生成影像的模型。DALL-E 經過影像與文字資料集訓練，可以根據文字描述生成影像。例如，DALL-E 可用來生成戴帽的貓咪，或是有莫霍克髮型的狗狗影像。

### Midjourney

Midjourney 的運作方式與 DALL-E 類似，也是從文字提示生成影像。Midjourney 也能使用類似「戴帽的貓咪」或「有莫霍克髮型的狗」的提示字串來生成影像。

![由 Midjourney 生成的影像，機械鴿子](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_圖片來源 Wikipedia，由 Midjourney 生成_

## DALL-E 與 Midjourney 的運作原理

首先介紹 [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)。DALL-E 是基於轉換器架構的生成式 AI 模型，採用_自回歸轉換器_。

_自回歸轉換器_定義了模型如何從文字描述生成影像：模型一次生成一個像素，並使用已生成的像素生成下一個像素。影像在神經網絡的多層處理後完成。

透過此過程，DALL-E 可以控制生成影像中的屬性、物體、特徵等。DALL-E 2 與 3 版本對生成影像有更多掌控力。

## 建立你的第一個影像生成應用程式

那麼，建立影像生成應用程式需要什麼呢？你需要以下函式庫：

- **python-dotenv**，強烈建議用此函式庫將密鑰保存在 _.env_ 檔案中，避免放在程式碼裡。
- **openai**，用於與 OpenAI API 互動的函式庫。
- **pillow**，用於 Python 的影像處理函式庫。
- **requests**，協助發送 HTTP 請求。

## 建立並部署 Azure OpenAI 模型

如果尚未建立，請參考 [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) 頁面，
建立 Azure OpenAI 資源和模型，選擇 **gpt-image-1** 作為模型（目前 Azure OpenAI 影像模型；DALL-E 3 為舊版，不再提供新部署）。

## 建立應用程式

1. 建立一個名為 _.env_ 的檔案，內容如下：

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   你可以在 Azure OpenAI Foundry 入口網站的「部署」區段找到這些資訊。

1. 將上述函式庫列在名為 _requirements.txt_ 的檔案中，內容如下：

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

   Windows 使用者可用以下命令建立並啟用虛擬環境：

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

        # 設定儲存圖像的目錄
        image_dir = os.path.join(os.curdir, 'images')

        # 如果目錄不存在，則創建它
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # 初始化圖像路徑（注意檔案類型應為 png）
        image_path = os.path.join(image_dir, 'generated-image.png')

        # 擷取生成的圖像
        image_url = generation_response.data[0].url  # 從回應中提取圖像 URL
        generated_image = requests.get(image_url).content  # 下載圖像
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # 在預設圖像檢視器中顯示圖像
        image = Image.open(image_path)
        image.show()

    # 捕捉異常
    except openai.BadRequestError as err:
        print(err)
   ```

讓我們來說明這段程式碼：

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
  # 載入 dotenv
  dotenv.load_dotenv()
  ```

- 之後，我們配置 Azure OpenAI 服務客戶端

  ```python
  # 從環境變數取得端點和金鑰
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- 接下來，我們產生圖片：

  ```python
  # 使用影像生成 API 創建一張圖片
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  上述程式碼會回傳一個 JSON 物件，裡面包含產生的圖片的 URL。我們可以使用這個 URL 來下載圖片並將其儲存成檔案。

- 最後，我們打開圖片並使用標準的影像檢視器來顯示它：

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### 關於生成圖片的更多細節

讓我們更詳細地看看用於生成圖片的程式碼：

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt** 是用來生成圖片的文字提示。在此例中，我們使用的提示是「Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils」。
- **size** 是產生圖片的尺寸。在此例中，我們產生的圖片大小為 1024x1024 像素。
- **n** 是要產生的圖片數量。在此例中，我們產生兩張圖片。
- **temperature** 是控制生成式 AI 模型輸出隨機性的參數。溫度是一個介於 0 和 1 之間的數值，0 代表輸出是決定性的，1 代表輸出是隨機的。預設值是 0.7。

接下來我們會介紹更多你可以對圖片做的操作。

## 影像生成的其他功能

到目前為止你已看到我們如何用少量 Python 程式碼產生一張圖片，然而你還能對圖片做更多事情。

你還可以做到以下操作：

- <strong>執行編輯</strong>。透過提供一張現有圖片、一個遮罩和一段提示文字，你可以修改圖片。例如，可以在圖片的某個部分添加物件。想像我們兔子圖片，你可以幫兔子加頂帽子。做法是提供圖片、一個遮罩（指出要更改的區域）和一段描述要做什麼的文字提示。
> 注意：DALL-E 3 不支援此功能。
 
這裡是一個使用 GPT Image 的範例：

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  基本圖片只包含帶泳池的休息區，但最終圖片會包含一隻火烈鳥：

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/zh-TW/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/zh-TW/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/zh-TW/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- <strong>建立變體</strong>。這是指你將一張現有圖片輸入並請求生成多個變體。要建立變體，你需提供圖片、文字提示及如下的程式碼：

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > 注意，此功能僅支援 OpenAI 的 DALL-E 2 模型，不支援 gpt-image-1。

## 溫度

溫度是控制生成式 AI 模型輸出隨機性的參數。溫度範圍在 0 到 1 之間，0 代表輸出為確定性，1 表示輸出為隨機。預設值是 0.7。

讓我們看一個溫度如何運作的範例，這裡執行相同提示兩次：

> 提示 : "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![Bunny on a horse holding a lollipop, version 1](../../../translated_images/zh-TW/v1-generated-image.a295cfcffa3c13c2.webp)

現在再執行一次相同的提示，看看是否會得到相同的圖片：

![Generated image of bunny on horse](../../../translated_images/zh-TW/v2-generated-image.33f55a3714efe61d.webp)

如你所見，圖像相似但不是完全相同。我們試著把溫度值改成 0.1，看看會發生什麼：

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # 在此輸入您的提示文字
        size='1024x1024',
        n=2
    )
```

### 改變溫度設定

因此我們嘗試讓回應更決定性一些。我們從兩張生成的圖像中可以觀察到，第一張有兔子，第二張是馬，兩張圖有很大差異。

所以我們將程式碼中的溫度設為 0，像這樣：

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # 在此輸入您的提示文字
        size='1024x1024',
        n=2,
        temperature=0
    )
```

執行此程式後，將得到以下兩張圖：

- ![溫度 0，版本 1](../../../translated_images/zh-TW/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![溫度 0，版本 2](../../../translated_images/zh-TW/v2-temp-generated-image.871d0c920dbfb0f1.webp)

你可以明顯看到兩張圖片更加相似。

## 如何用元提示來定義應用程式的邊界

利用我們的示範應用，已經可以為客戶產生圖片。然而，我們需要為應用程式設置一些界限。

例如，我們不希望產生不適合工作的圖片或兒童不宜的圖片。

我們可以使用 _元提示_ 來做到這點。元提示是用來控制生成式 AI 模型輸出的文字提示。例如，我們可以利用元提示來控制生成內容，確保圖片適合工作環境或兒童觀看。

### 它是怎麼運作的？

那么，元提示是如何運作的呢？

元提示是用來控制生成式 AI 模型輸出的文字提示，它放在文字提示之前，用於控制模型的輸出，並嵌入應用程式中以控制模型輸出。將提示輸入和元提示輸入封裝成一個單一的文字提示。

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

現在，我們來看看怎麼在示範中使用元提示。

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

# TODO 新增請求以生成圖像
```

從上述提示可以看出，所有生成的圖片都考慮了元提示。

## 練習 - 讓學生能夠使用

我們在本課程一開始介紹了 Edu4All，現在是時候讓學生能為他們的作業產生圖片了。


學生們將為他們的評量創作包含紀念碑的影像，具體是哪些紀念碑由學生決定。學生們被要求在此任務中發揮創意，將這些紀念碑置於不同的情境中。

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
    # 使用影像生成 API 創建影像
    generation_response = client.images.generate(
        prompt=prompt,    # 在此輸入您的提示文字
        size='1024x1024',
        n=1,
    )
    # 設定存放影像的目錄
    image_dir = os.path.join(os.curdir, 'images')

    # 若目錄不存在，則建立它
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # 初始化影像路徑（注意檔案類型應為 png）
    image_path = os.path.join(image_dir, 'generated-image.png')

    # 取得生成的影像
    image_url = generation_response.data[0].url  # 從回應中提取影像 URL
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

## 太棒了！繼續你的學習之路

完成本課程後，請參考我們的 [生成式 AI 學習收藏](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)， 持續提升你的生成式 AI 知識！

接著前往第 10 課，我們將探討如何[使用低程式碼開發 AI 應用程式](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->