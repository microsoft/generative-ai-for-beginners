<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T10:33:32+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "tw"
}
-->
# 建立圖像生成應用程式

[![建立圖像生成應用程式](../../../translated_images/09-lesson-banner.d0229c79fda6596b8a678478e20301b74964cb8161e0c2e4a7c203655c623330.tw.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

大型語言模型（LLM）不僅僅是用於文字生成，還可以從文字描述中生成圖像。擁有圖像作為一種表達形式在許多領域中非常有用，如醫療技術、建築、旅遊、遊戲開發等。在本章中，我們將探討兩個最受歡迎的圖像生成模型：DALL-E和Midjourney。

## 介紹

在本課程中，我們將涵蓋：

- 圖像生成及其用途。
- DALL-E和Midjourney，它們是什麼以及如何運作。
- 如何建立圖像生成應用程式。

## 學習目標

完成本課程後，你將能夠：

- 建立圖像生成應用程式。
- 使用元提示為你的應用程式定義界限。
- 使用DALL-E和Midjourney。

## 為什麼要建立圖像生成應用程式？

圖像生成應用程式是探索生成式AI能力的一種好方法。它們可以用於，例如：

- **圖像編輯和合成**。你可以生成各種用途的圖像，例如圖像編輯和合成。

- **應用於各行各業**。它們也可以用於生成各行各業的圖像，如醫療技術、旅遊、遊戲開發等。

## 情境：Edu4All

作為本課程的一部分，我們將繼續與我們的初創公司Edu4All合作。學生將為他們的評估創建圖像，具體創作什麼圖像由學生決定，但他們可以為自己的童話故事創作插圖，或創造一個新角色，或幫助他們視覺化自己的想法和概念。

例如，如果他們在課堂上研究紀念碑，Edu4All的學生可以生成以下內容：

![Edu4All初創公司，紀念碑課堂，艾菲爾鐵塔](../../../translated_images/startup.ec211d74fef9f4175010c3334942b715514230415744b9dd0a69a19f4ad68786.tw.png)

使用以下提示

> "早晨陽光下艾菲爾鐵塔旁的狗"

## DALL-E和Midjourney是什麼？

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst)和[Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst)是兩個最受歡迎的圖像生成模型，它們允許你使用提示生成圖像。

### DALL-E

讓我們從DALL-E開始，它是一種生成式AI模型，能從文字描述中生成圖像。

> [DALL-E是兩個模型的結合，CLIP和擴散注意力](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)。

- **CLIP**，是一個生成嵌入的模型，嵌入是數據的數值表示，來自圖像和文字。

- **擴散注意力**，是一個從嵌入生成圖像的模型。DALL-E在一組圖像和文字數據上進行訓練，並可用於從文字描述生成圖像。例如，DALL-E可以用來生成戴帽子的貓或留莫霍克髮型的狗的圖像。

### Midjourney

Midjourney的工作方式與DALL-E相似，它從文字提示生成圖像。Midjourney也可以用來生成像“戴帽子的貓”或“留莫霍克髮型的狗”這樣的提示的圖像。

![由Midjourney生成的圖像，機械鴿子](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_圖片來源：維基百科，由Midjourney生成的圖像_

## DALL-E和Midjourney如何運作

首先，[DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)。DALL-E是一種基於transformer架構的生成式AI模型，使用自回歸transformer。

自回歸transformer定義了模型如何從文字描述中生成圖像，它一次生成一個像素，然後使用生成的像素生成下一個像素。經過神經網絡的多層傳遞，直到圖像完成。

通過這個過程，DALL-E控制生成圖像中的屬性、物件、特徵等。然而，DALL-E 2和3對生成的圖像有更多的控制。

## 建立你的第一個圖像生成應用程式

那麼建立一個圖像生成應用程式需要什麼？你需要以下庫：

- **python-dotenv**，強烈建議使用這個庫將你的機密信息保存在_.env_文件中，遠離代碼。
- **openai**，這個庫是你用來與OpenAI API互動的。
- **pillow**，用於在Python中處理圖像。
- **requests**，幫助你發送HTTP請求。

1. 創建一個_.env_文件，內容如下：

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   在Azure Portal中為你的資源的“密鑰和端點”部分找到此信息。

1. 將上述庫收集在名為_requirements.txt_的文件中，如下所示：

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

   對於Windows，使用以下命令創建並激活你的虛擬環境：

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. 在名為_app.py_的文件中添加以下代碼：

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

- 首先，我們導入所需的庫，包括OpenAI庫、dotenv庫、requests庫和Pillow庫。

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- 接下來，我們從_.env_文件中加載環境變量。

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- 然後，我們設置OpenAI API的端點、密鑰、版本和類型。

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

  上述代碼返回一個包含生成圖像URL的JSON對象。我們可以使用URL下載圖像並保存到文件中。

- 最後，我們打開圖像並使用標準圖像查看器顯示它：

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### 更多生成圖像的細節

讓我們更詳細地看一下生成圖像的代碼：

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**，是用來生成圖像的文字提示。在這個例子中，我們使用的提示是“騎馬的兔子，手拿棒棒糖，在長滿水仙花的霧濛濛的草地上”。
- **size**，是生成的圖像的大小。在這個例子中，我們生成的是1024x1024像素的圖像。
- **n**，是生成的圖像數量。在這個例子中，我們生成兩張圖像。
- **temperature**，是一個控制生成式AI模型輸出隨機性的參數。溫度是0到1之間的值，其中0表示輸出是確定性的，1表示輸出是隨機的。默認值是0.7。

還有更多可以對圖像進行的操作，我們將在下一節中涵蓋。

## 圖像生成的額外功能

到目前為止，你已經看到我們如何使用Python的幾行代碼生成圖像。然而，還有更多可以對圖像進行的操作。

你還可以進行以下操作：

- **進行編輯**。通過提供現有圖像的遮罩和提示，你可以更改圖像。例如，你可以在圖像的一部分添加一些東西。想像一下我們的兔子圖像，你可以給兔子加上帽子。你可以通過提供圖像、遮罩（識別更改的區域部分）和文字提示來說明應該進行什麼操作。

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

  基礎圖像只包含兔子，但最終圖像會在兔子上加上帽子。

- **創建變體**。其想法是你採用現有圖像並要求創建變體。要創建變體，你需要提供圖像和文字提示，代碼如下：

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > 注意，這僅在OpenAI上支持

## 溫度

溫度是一個控制生成式AI模型輸出隨機性的參數。溫度是0到1之間的值，其中0表示輸出是確定性的，1表示輸出是隨機的。默認值是0.7。

讓我們通過兩次運行這個提示來看一下溫度如何運作：

> 提示 : "騎馬的兔子，手拿棒棒糖，在長滿水仙花的霧濛濛的草地上"

![騎馬的兔子，手拿棒棒糖，版本1](../../../translated_images/v1-generated-image.208ba0525ed6ae505504aa852e28d334c0440e9931b7c97f9508176a22d2dd54.tw.png)

現在讓我們再次運行相同的提示來看看我們不會得到相同的圖像：

![生成的騎馬兔子圖像](../../../translated_images/v2-generated-image.f0a88c05ef476e95f3682d4b21c9ba2f4807ae71cc29e9c05b42ebbf497cf61b.tw.png)

如你所見，這些圖像相似，但不相同。讓我們嘗試將溫度值更改為0.1看看會發生什麼：

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### 改變溫度

因此，讓我們嘗試使回應更具確定性。我們可以從生成的兩張圖像中觀察到，在第一張圖像中有一隻兔子，而在第二張圖像中有一匹馬，因此這些圖像差異很大。

因此，讓我們改變代碼並將溫度設置為0，如下所示：

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

現在運行此代碼，你將得到以下兩張圖像：

- ![溫度0，v1](../../../translated_images/v1-temp-generated-image.d8557be792b5c81c2c6d2804cb7b210fe8b340106fe4ffcadf9cf7de1cd7b991.tw.png)
- ![溫度0，v2](../../../translated_images/v2-temp-generated-image.bd412fcfbd43379312b1382212a332aa311ca1a80ea692dea50a8b876a487c61.tw.png)

在這裡，你可以清楚地看到這些圖像更相似。

## 如何使用元提示為你的應用程式定義界限

通過我們的演示，我們已經可以為客戶生成圖像。然而，我們需要為應用程式創建一些界限。

例如，我們不希望生成不適合工作的圖像，或者不適合兒童的圖像。

我們可以使用_元提示_來做到這一點。元提示是用來控制生成式AI模型輸出的文字提示。例如，我們可以使用元提示來控制輸出，並確保生成的圖像適合工作或適合兒童。

### 它是如何運作的？

那麼，元提示如何運作？

元提示是用來控制生成式AI模型輸出的文字提示，它們位於文字提示之前，用於控制模型的輸出，並嵌入應用程式中以控制模型的輸出。將提示輸入和元提示輸入封裝在單一的文字提示中。

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

從上述提示中，你可以看到所有創建的圖像都考慮了元提示。

## 作業 - 讓我們啟發學生

我們在本課程開始時介紹了Edu4All。現在是時候讓學生為他們的評估生成圖像了。

學生將為他們的評估創建包含紀念碑的圖像，具體紀念碑由學生決定。學生被要求在這項任務中發揮創意，將這些紀念碑放置在不同的背景中。

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

完成本課程後，請查看我們的[生成式AI學習系列](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，繼續提升你的生成式AI知識！

前往第10課，我們將探索如何[使用低代碼建立AI應用程式](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**免責聲明**：

本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用本翻譯而產生的任何誤解或誤讀不承擔責任。