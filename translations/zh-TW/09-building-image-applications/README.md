# 建立影像生成應用程式

[![建立影像生成應用程式](../../../translated_images/zh-TW/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM 不僅限於文字生成。你也可以從文字描述生成影像。影像作為一種模式，在醫療技術、建築、旅遊、遊戲開發、行銷等方面非常有用。在本課程中，我們將探討今日的 **GPT 影像** 模型並建立一個影像生成應用程式。

## 簡介

影像生成讓你能將自然語言提示轉換成圖片。在本課程中，我們使用 OpenAI 的 **`gpt-image`** 系列模型——這是目前在 **[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)** 與 OpenAI 平台上可用的最新影像模型。這些模型取代了較舊的 DALL·E 模型（DALL·E 2/3 為舊版）。

在整個課程中，我們使用一個虛構新創公司 **Edu4All**，該公司開發學習工具，團隊希望為作業和學習資料生成插畫。

## 學習目標

完成本課程後，你將能夠：

- 解釋什麼是影像生成以及它的應用領域。
- 理解 `gpt-image` 模型系列及其與舊版 DALL·E 模型的差異。
- 使用 Python（以及 TypeScript / .NET）建立影像生成應用程式。
- 編輯影像並使用元提示（metaprompts）套用安全防護。

## 什麼是影像生成？

影像生成模型可從文字提示創建圖片。現代模型如 `gpt-image` 採用 transformer + diffusion 技術：模型在訓練時學習文字與圖片的關聯，然後根據提示，逐步將隨機噪點“去噪”成符合描述的影像。

兩個知名的影像模型系列是：

- **`gpt-image` (OpenAI)** —— 本課程使用的現代模型。支援文字轉影像生成和影像編輯（帶遮罩的修補）。
- **Midjourney** —— 一個流行的第三方模型，有自己的服務及基於 Discord 的工作流程。

> 較舊的 OpenAI 影像模型——**DALL·E 2** 與 **DALL·E 3**——現已成為舊版。DALL·E 3 不再對新部署開放，而類似 `create_variation` 的功能僅存在於 DALL·E 2。新應用請使用 `gpt-image` 模型。

### 我應該使用哪個 `gpt-image` 模型？

在 Microsoft Foundry 上，以下模型為 <strong>一般可用</strong>：

| 模型 | 備註 |
| --- | --- |
| **`gpt-image-2`** | 最新且功能最強大的影像模型——推薦作為預設。 |
| `gpt-image-1.5` | 一般可用；強勁的品質與較低成本。 |
| `gpt-image-1-mini` | 一般可用；速度最快 / 成本最低。 |
| `gpt-image-1` | 僅供預覽。 |

請隨時檢查最新的 [Foundry 影像模型列表](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst) 以了解可用性及區域。

> **重要：** `gpt-image` 模型回傳的生成影像是 **base64** 格式（`b64_json`），而非 URL。你的程式碼需將 base64 字串解碼為位元組並儲存——沒有可下載的影像 URL。

## 設定

你可以使用 **Microsoft Foundry 的 Azure OpenAI**（`aoai-*` 範例）或 **OpenAI 平台**（`oai-*` 範例）來運行範例。

### 1. 建立並部署模型

按照[建立資源](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)指南，在 Microsoft Foundry 建立資源，接著部署影像模型——推薦使用 **`gpt-image-2`**。

### 2. 配置你的 `.env`

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

這些值可在你的資源的 [Foundry 入口網站](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) 中的 <strong>部署</strong> 頁面找到。

### 3. 安裝函式庫

建立一個 `requirements.txt`：

```text
python-dotenv
openai
pillow
```

然後建立並啟動虛擬環境，並安裝：

```bash
python3 -m venv venv
source venv/bin/activate        # Windows：venv\Scripts\activate
pip install -r requirements.txt
```

## 建立應用程式

建立 `app.py`，內容如下。它將生成一張影像並儲存為 PNG。

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# 將客戶端指向您的 Azure OpenAI（Microsoft Foundry）資源。
# 影像模型需要較新的 API 版本 - 請查閱 Foundry 文件了解您的模型所需版本。
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # 例如 "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # 亦可使用 1536x1024（橫向）、1024x1536（縱向）或 "auto"
    n=1,
)

# gpt-image 模型回傳的是 base64（b64_json），非 URL - 需解碼為位元組。
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

以 `python app.py` 執行。結果會在 `images/` 下得到一個 PNG。

> 每次呼叫 `images.generate`，同一提示會產生不同影像——影像模型不接受 `temperature` 參數（那是文字生成的控制參數）。若要獲得多樣性，重複呼叫 API；若要減少多樣性，請使提示更具體。

## 編輯影像

`gpt-image` 模型能 <strong>編輯</strong> 現有影像：提供影像、一個可選的 <strong>遮罩</strong>（標示欲更改區域）及描述更改的提示。編輯結果同樣以 base64 回傳。

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
  <img src="../../../translated_images/zh-TW/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/zh-TW/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/zh-TW/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## 用元提示設定界限

生成影像後，你需要安全界限，避免應用生產出不安全或不符品牌形象的內容。<strong>元提示</strong> 是你加在使用者提示前的文字，用於限制模型輸出。

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

每張影像現在都在元提示設定的界限內生成。將此與 Microsoft Foundry 內建的內容過濾器結合，提供深度防護。

## 作業 - 讓學生們也能使用

Edu4All 的學生需要影像用於評量。建立一個應用程式，生成<strong>紀念碑</strong>（紀念碑由你決定）放在不同且有創意的情境中——例如，一個著名地標在夕陽下，一名孩童在旁觀賞。

自己嘗試，再比對參考解決方案：

- Python（Azure）：[aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- Python（Azure）完整生成應用程式：[aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- Python（OpenAI）：[oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- TypeScript（Azure）：[typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET（Azure）：[dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

也可練習 [python/](../../../09-building-image-applications/python) 裡的筆記本 (`aoai-assignment.ipynb` 用於 Azure，`oai-assignment.ipynb` 用於 OpenAI)。

## 很棒！繼續學習

完成本課程後，請參考我們的 [生成式 AI 學習集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升你的生成式 AI 知識！

接著前往第 10 課繼續學習。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->