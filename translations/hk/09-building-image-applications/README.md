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