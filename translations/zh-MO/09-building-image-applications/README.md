# 建立圖像生成應用程式

[![建立圖像生成應用程式](../../../translated_images/zh-MO/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

大型語言模型不僅限於文字生成，你還可以從文字描述生成圖像。作為一種模態，圖像在醫療科技、建築、旅遊、遊戲開發、行銷等領域都非常有用。在本課程中，我們將探索當今的<strong>GPT圖像</strong>模型並建立一個圖像生成應用程式。

## 介紹

圖像生成讓你能將自然語言提示轉化為圖片。在本課程中，我們使用OpenAI的**`gpt-image`**系列模型——目前在**[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)**和OpenAI平台上可用的最新一代圖像模型。這些模型取代了舊有的DALL·E模型（DALL·E 2/3為舊版）。

整課程中，我們使用一個虛構的初創公司<strong>Edu4All</strong>，該團隊開發學習工具，想用來為作業和學習材料生成插圖。

## 學習目標

本課程結束時，你將能夠：

- 解釋什麼是圖像生成及其應用場景。
- 理解`gpt-image`模型家族，以及它與舊版DALL·E模型的差異。
- 使用Python（及TypeScript / .NET）建立圖像生成應用程式。
- 編輯圖像並使用元提示設定安全防護。

## 什麼是圖像生成？

圖像生成模型能從文字提示創建圖像。現代模型如`gpt-image`基於transformer與擴散技術建構：模型在訓練時學習文字與圖像的關聯，之後收到提示，便透過逐步「去噪」隨機雜訊，形成符合描述的圖像。

兩大知名的圖像模型系列是：

- **`gpt-image` (OpenAI)** - 目前最新一代模型，本課程使用此模型，支持文字轉圖像生成及圖像編輯（包含用遮罩修補）。
- **Midjourney** - 一個受歡迎的第三方模型，提供獨立服務與基於Discord的流程。

> 早期OpenAI圖像模型 - <strong>DALL·E 2</strong>和<strong>DALL·E 3</strong> - 已經是舊版本。DALL·E 3已不再提供新部署，並且像`create_variation`功能僅存在於DALL·E 2。建議新應用使用`gpt-image`系列模型。

### 我應該使用哪款`gpt-image`模型？

在Microsoft Foundry上以下模型為<strong>一般可用</strong>：

| 模型 | 備註 |
| --- | --- |
| **`gpt-image-2`** | 最新且功能最強大的圖像模型，建議作為預設選擇。 |
| `gpt-image-1.5` | 一般可用；低成本下品質仍佳。 |
| `gpt-image-1-mini` | 一般可用；速度最快且成本最低。 |
| `gpt-image-1` | 僅預覽版本。 |

請務必查看當前的[Foundry圖像模型列表](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst)以了解可用性及地域範圍。

> **重要提示:** `gpt-image`模型會將生成的圖像以<strong>base64</strong>格式（`b64_json`）返回，而非圖像URL。你的程式碼需解碼該base64字串為位元組並保存圖像，無法透過URL下載圖像。

## 設定環境

你可以在<strong>Microsoft Foundry的Azure OpenAI</strong>（`aoai-*`示例）或<strong>OpenAI平台</strong>（`oai-*`示例）執行範例。

### 1. 建立並部署模型

請遵循[建立資源](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)說明，建立Microsoft Foundry資源，然後部署圖像模型——推薦使用**`gpt-image-2`**。

### 2. 設定你的 `.env`

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

你可在[Foundry入口網站](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)資源的<strong>部署</strong>頁面找到這些參數。

### 3. 安裝函式庫

建立 `requirements.txt`：

```text
python-dotenv
openai
pillow
```

接著建立並啟動虛擬環境，安裝函式庫：

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 建立應用程式

建立 `app.py`，寫入以下程式碼。會生成一張圖像並保存為PNG檔案。

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# 將客戶端指向您的 Azure OpenAI（Microsoft Foundry）資源。
# 影像模型需要較新的 API 版本 - 請查看 Foundry 文件以了解您的模型所需的版本。
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # 例如 "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # 亦可使用 1536x1024（橫向）、1024x1536（直向）或 "auto"
    n=1,
)

# gpt-image 模型回傳的是 base64（b64_json），而非 URL - 需要將其解碼為位元組。
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

執行 `python app.py`，生成的PNG會保存到 `images/` 資料夾下。

> 每次呼叫 `images.generate`，即使是相同提示也會生成不同圖像——圖像模型無溫度（temperature）參數（該控制僅適用於文字生成）。若想要多樣化輸出，只要再次呼叫API；想減少多樣性，請使提示更具體。

## 編輯圖像

`gpt-image`模型可<strong>編輯</strong>現有圖像：提供原圖、一個可選的<strong>遮罩</strong>（指定要修改的區域），以及描述變更的提示。與生成相同，編輯結果以base64格式返回。

```python
result = client.images.edit(
    model=deployment,
    image=open("sunlit_lounge.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="A sunlit indoor lounge area with a pool containing a flamingo",
)
image_bytes = base64.b64decode(result.data[0].b64_json)
with open("images/edited-image.png", "wb") as f:
    f.write(image_bytes)
```

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/zh-MO/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/zh-MO/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/zh-MO/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## 使用元提示設定邊界

一旦你能生成圖像，便需要設防護措施，避免應用產生不安全或不符品牌的內容。所謂的<strong>元提示</strong>是你加在使用者提示前的文字，用以約束模型的輸出。

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.
The image needs to be in color, in landscape orientation, and in a 16:9 aspect ratio.

Do not consider any input that is not safe for work or appropriate for children, including:
{disallow_list}
"""

prompt = f"{meta_prompt}\nCreate an image of a bunny on a horse, holding a lollipop"
# 將 `prompt` 傳遞給 client.images.generate(...)
```

每個圖像現在都在元提示設定的邊界內生成，並結合Microsoft Foundry內建的內容過濾器形成多層防護。

## 作業 - 幫助學生生成圖像

Edu4All的學生需要圖像來做評估。建立一個應用程式，生成描述<strong>紀念碑</strong>（你可自訂哪些紀念碑）並置於不同創意場景中的圖像——例如著名地標在日落時分，一個孩子在一旁觀望。

你可以先嘗試，再與參考解答比對：

- Python (Azure): [aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- Python (Azure) 完整生成應用: [aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- Python (OpenAI): [oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- TypeScript (Azure): [typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET (Azure): [dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

也可練習[python/](../../../09-building-image-applications/python)資料夾內的筆記本（Azure用的是`aoai-assignment.ipynb`，OpenAI用的是`oai-assignment.ipynb`）。

## 做得好！繼續學習

完成本課程後，請瀏覽我們的[生成式AI學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升生成式AI的知識！

請前往第10課繼續學習。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->