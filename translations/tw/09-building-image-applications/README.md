<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-06-25T17:09:18+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "tw"
}
-->
# 建立影像生成應用程式

除了文字生成，LLM 還有更多功能。它也可以從文字描述中生成影像。擁有影像作為一種模式在許多領域中都非常有用，例如醫療技術、建築、旅遊、遊戲開發等。在本章中，我們將探討兩個最受歡迎的影像生成模型，DALL-E 和 Midjourney。

## 介紹

在本課中，我們將涵蓋：

- 影像生成及其用途。
- DALL-E 和 Midjourney，它們是什麼以及如何運作。
- 如何建立影像生成應用程式。

## 學習目標

完成本課後，您將能夠：

- 建立影像生成應用程式。
- 使用元提示為您的應用程式定義界限。
- 使用 DALL-E 和 Midjourney。

## 為什麼要建立影像生成應用程式？

影像生成應用程式是探索生成 AI 功能的好方法。它們可以用於，例如：

- **影像編輯和合成**。您可以生成各種用途的影像，例如影像編輯和影像合成。

- **應用於各種行業**。它們還可以用於生成各種行業的影像，如醫療技術、旅遊、遊戲開發等。

## 情境：Edu4All

作為本課的一部分，我們將繼續與我們的初創公司 Edu4All 合作。在本課中，學生將為他們的評估創建影像，具體的影像內容由學生決定，但它們可以是自己的童話故事插圖，或創建新角色，或幫助他們視覺化自己的想法和概念。

以下是 Edu4All 的學生在課堂上研究紀念碑時可能生成的內容示例：

![Edu4All 初創公司，紀念碑課程，艾菲爾鐵塔](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.tw.png)

使用以下提示

> "狗在艾菲爾鐵塔旁邊，清晨陽光下"

## DALL-E 和 Midjourney 是什麼？

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) 和 [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) 是兩個最受歡迎的影像生成模型，它們允許您使用提示來生成影像。

### DALL-E

讓我們從 DALL-E 開始，它是一個生成 AI 模型，能夠從文字描述生成影像。

> [DALL-E 是兩個模型的組合，CLIP 和擴散注意力](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)。

- **CLIP**，是一個生成嵌入的模型，嵌入是數據的數值表示，來自影像和文字。

- **擴散注意力**，是一個從嵌入生成影像的模型。DALL-E 是在影像和文字數據集上訓練的，可以用於從文字描述生成影像。例如，DALL-E 可以用於生成戴帽子的貓或有莫霍克髮型的狗的影像。

### Midjourney

Midjourney 的工作方式與 DALL-E 類似，它從文字提示生成影像。Midjourney 也可以用來生成影像，使用類似於“戴帽子的貓”或“有莫霍克髮型的狗”的提示。

![由 Midjourney 生成的影像，機械鴿子](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_圖片來源 Wikipedia，由 Midjourney 生成的影像_

## DALL-E 和 Midjourney 如何運作

首先，[DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)。DALL-E 是一個基於 transformer 架構的生成 AI 模型，具有自回歸 transformer。

自回歸 transformer 定義了模型如何從文字描述生成影像，它一次生成一個像素，然後使用生成的像素生成下一個像素。通過神經網絡的多層傳遞，直到影像完成。

通過這個過程，DALL-E 控制它生成的影像中的屬性、物件、特徵等。然而，DALL-E 2 和 3 對生成的影像有更多控制。

## 建立您的第一個影像生成應用程式

那麼建立影像生成應用程式需要什麼呢？您需要以下庫：

- **python-dotenv**，強烈建議使用此庫將您的秘密保存在 _.env_ 文件中，遠離代碼。
- **openai**，此庫是您用來與 OpenAI API 互動的。
- **pillow**，用於在 Python 中處理影像。
- **requests**，幫助您發送 HTTP 請求。

1. 創建一個 _.env_ 文件，內容如下：

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   在 Azure Portal 中的“Keys and Endpoint”部分查找此信息。

1. 將上述庫收集在名為 _requirements.txt_ 的文件中，如下所示：

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

- 接下來，我們生成影像：

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
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
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**，是用來生成影像的文字提示。在這種情況下，我們使用的提示是“兔子騎馬，拿著棒棒糖，在長滿水仙花的霧霾草地上”。
- **size**，是生成影像的大小。在這種情況下，我們生成的影像大小為 1024x1024 像素。
- **n**，是生成的影像數量。在這種情況下，我們生成兩個影像。
- **temperature**，是控制生成 AI 模型輸出隨機性的參數。temperature 是介於 0 和 1 之間的值，其中 0 表示輸出是確定性的，1 表示輸出是隨機的。默認值是 0.7。

還有更多影像操作功能，我們將在下一節中介紹。

## 影像生成的附加功能

到目前為止，您已經看到我們如何使用幾行 Python 代碼生成影像。然而，您還可以對影像進行更多操作。

您還可以執行以下操作：

- **進行編輯**。通過提供現有影像、遮罩和提示，您可以更改影像。例如，您可以在影像的一部分添加內容。想像一下我們的兔子影像，您可以在兔子上添加帽子。您可以通過提供影像、遮罩（識別更改區域的一部分）和文字提示來指定應執行的操作。

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

  基礎影像僅包含兔子，但最終影像會在兔子上添加帽子。

- **創建變體**。這個想法是您可以使用現有影像並要求創建變體。要創建變體，您需要提供影像和文字提示，並像這樣編寫代碼：

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > 注意，這僅在 OpenAI 上支持

## Temperature

Temperature 是控制生成 AI 模型輸出隨機性的參數。temperature 是介於 0 和 1 之間的值，其中 0 表示輸出是確定性的，1 表示輸出是隨機的。默認值是 0.7。

讓我們看一個例子，看看 temperature 如何運作，通過兩次運行此提示：

> 提示 : "兔子騎馬，拿著棒棒糖，在長滿水仙花的霧霾草地上"

![兔子騎馬拿著棒棒糖，版本 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.tw.png)

現在讓我們再次運行相同的提示，看看我們是否能得到相同的影像：

![生成的兔子騎馬影像](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.tw.png)

如您所見，影像相似，但並不相同。讓我們嘗試將 temperature 值更改為 0.1，看看會發生什麼：

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### 改變 temperature

讓我們嘗試使響應更加確定性。我們可以從生成的兩個影像中觀察到，第一個影像中有一隻兔子，第二個影像中有一匹馬，所以影像差異很大。

因此，讓我們更改代碼並將 temperature 設置為 0，如下所示：

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

現在當您運行此代碼時，您會得到這兩個影像：

- ![Temperature 0，版本 1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.tw.png)
- ![Temperature 0，版本 2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.tw.png)

在這裡您可以清楚地看到影像更加相似。

## 如何使用元提示為您的應用程式定義界限

通過我們的演示，我們已經可以為客戶生成影像。然而，我們需要為應用程式創建一些界限。

例如，我們不希望生成不適合工作的影像，或不適合兒童的影像。

我們可以使用 _元提示_ 來做到這一點。元提示是用來控制生成 AI 模型輸出的文字提示。例如，我們可以使用元提示來控制輸出，並確保生成的影像適合工作，或適合兒童。

### 它是如何工作的？

那麼，元提示如何運作？

元提示是用來控制生成 AI 模型輸出的文字提示，它們位於文字提示之前，用於控制模型的輸出，並嵌入到應用程式中以控制模型的輸出。將提示輸入和元提示輸入封裝在一個文字提示中。

元提示的一個例子如下：

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

## 作業 - 讓我們啟發學生

我們在本課開始時介紹了 Edu4All。現在是時候啟發學生為他們的評估生成影像了。

學生將創建包含紀念碑的影像，具體的紀念碑由學生決定。學生被要求在這項任務中發揮創意，將這些紀念碑置於不同的背景中。

## 解決方案

以下是一種可能的解決方案：

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

完成本課後，請查看我們的 [生成 AI 學習集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) 以繼續提升您的生成 AI 知識！

前往第 10 課，我們將探討如何 [使用低代碼構建 AI 應用程式](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**免責聲明**：  
本文檔已使用AI翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)進行翻譯。我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。應將原始語言的文件視為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或誤讀不承擔責任。