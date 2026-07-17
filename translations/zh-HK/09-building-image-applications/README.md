# 建立影像生成應用程式

[![建立影像生成應用程式](../../../translated_images/zh-HK/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM 不僅僅是文本生成，您還可以根據文字描述生成影像。影像作為一種模態，在醫療科技、建築、旅遊、遊戲開發、市場營銷等多個領域都非常有用。在本課程中，我們會了解當今的 **GPT 影像** 模型並建立一個影像生成應用程式。

## 介紹

影像生成能讓您將自然語言提示轉換為圖片。在本課程中，我們將使用來自 OpenAI 的 **`gpt-image`** 系列模型——目前 Microsoft Foundry（**[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)**）和 OpenAI 平台上可用的最新一代影像模型。這些模型取代了較舊的 DALL·E 模型（DALL·E 2/3 已屬於舊版）。

在整個課程中，我們使用一個虛構的初創公司 **Edu4All**，該公司開發學習工具。團隊希望為作業及學習材料生成插圖。

## 學習目標

完成本課程後，您將能夠：

- 解釋什麼是影像生成及其應用場景。
- 理解 `gpt-image` 模型系列，以及它與舊版 DALL·E 模型的不同。
- 使用 Python（以及 TypeScript / .NET）建立影像生成應用程式。
- 編輯影像並使用元提示套用安全防護。

## 什麼是影像生成？

影像生成模型從文字提示創建影像。現代模型如 `gpt-image` 是基於 Transformer + 擴散技術：模型在訓練階段學習文字與影像的關聯，隨後根據提示，通過迭代“去噪”隨機噪聲，生成符合描述的圖像。

兩個知名的影像模型系列是：

- **`gpt-image` (OpenAI)** — 本課使用的最新一代，支持文本生成影像及影像編輯（使用遮罩進行塗抹）。
- **Midjourney** — 一個流行的第三方模型，具有自己的服務和基於 Discord 的工作流程。

> 舊版 OpenAI 影像模型 - **DALL·E 2** 和 **DALL·E 3** - 皆為舊有版本。DALL·E 3 不再提供新部署，而類似 `create_variation` 的功能僅存在於 DALL·E 2。新的應用請使用 `gpt-image` 模型。

### 我應該使用哪個 `gpt-image` 模型？

在 Microsoft Foundry 上，以下模型為<strong>一般可用</strong>：

| 模型 | 備註 |
| --- | --- |
| **`gpt-image-2`** | 最新且最強大的影像模型 — 推薦的預設選擇。 |
| `gpt-image-1.5` | 一般可用；成本較低但品質仍佳。 |
| `gpt-image-1-mini` | 一般可用；速度最快 / 成本最低。 |
| `gpt-image-1` | 僅供預覽。 |

請隨時查看目前的 [Foundry 影像模型列表](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst) 以確認可用性與區域。

> **重要提示：** `gpt-image` 模型以 **base64** 格式（`b64_json`）返回生成的影像，而非影像網址。您的程式需要將 base64 字串解碼為位元組並保存——沒有可下載的影像 URL。

## 設定

您可以針對 **Microsoft Foundry 中的 Azure OpenAI**（`aoai-*` 範例）或 **OpenAI 平台**（`oai-*` 範例）來執行範例程式碼。

### 1. 建立並部署模型

請依照 [建立資源](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) 指南在 Microsoft Foundry 中建立資源，然後部署影像模型 — 建議使用 **`gpt-image-2`**。

### 2. 配置 `.env`

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

在您資源的 [Foundry 入口網站](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)的<strong>部署</strong>頁面找到這些數值。

### 3. 安裝函式庫

建立 `requirements.txt`：

```text
python-dotenv
openai
pillow
```

接著建立並啟動虛擬環境，然後安裝：

```bash
python3 -m venv venv
source venv/bin/activate        # Windows：venv\Scripts\activate
pip install -r requirements.txt
```

## 建立應用程式

建立 `app.py`，寫入以下程式碼。它會生成影像並保存為 PNG 格式。

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# 將客戶端指向你的 Azure OpenAI（Microsoft Foundry）資源。
# 影像模型需要最新的 API 版本－請查看 Foundry 文件以了解你的模型所需的版本。
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # 例如 "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # 亦支援 1536x1024（橫向）、1024x1536（直向）或「自動」
    n=1,
)

# gpt-image 模型會返回 base64（b64_json），不是 URL－須將其解碼成位元組。
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

使用 `python app.py` 執行。影像將儲存在 `images/` 目錄下。

> 每次呼叫 `images.generate`，即使是相同提示也會生成不同的影像 - 影像模型沒有 `temperature` 參數（這是文本生成用的控制參數）。若想取得多樣變化，只需再次呼叫 API；若想減少變化，請使提示更具體。

## 編輯影像

`gpt-image` 模型可以 <strong>編輯</strong> 現有影像：提供影像、可選的<strong>遮罩</strong>（標記要改變的區域）以及描述變更的提示。與生成一樣，編輯結果以 base64 格式返回。

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
  <img src="../../../translated_images/zh-HK/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/zh-HK/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/zh-HK/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## 以元提示設定界限

一旦可以生成影像，您需要設置防護措施，防止應用程式產生不安全或不符品牌形象的內容。<strong>元提示</strong>是在用戶提示前置加上的文字，用以限制模型的輸出。

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

現在每張影像都會在元提示所設定的界限下生成。結合 Microsoft Foundry 內建的內容過濾器，能實現深度防禦。

## 作業 - 讓學生能使用影像生成

Edu4All 的學生需要影像來做評量。建立一個應用程式，生成<strong>紀念碑</strong>的影像（紀念碑種類由你決定），並將它們放置於不同且有創意的場景中——例如夕陽下的著名地標旁有一個孩童觀望。

請自行嘗試，然後參考以下範例解決方案：

- Python (Azure)：[aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- Python (Azure) 全功能生成應用程式：[aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- Python (OpenAI)：[oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- TypeScript (Azure)：[typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET (Azure)：[dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

也可以操作在 [python/](../../../09-building-image-applications/python) 的 Notebook（Azure 版本為 `aoai-assignment.ipynb`，OpenAI 版本為 `oai-assignment.ipynb`）。

## 做得好！繼續學習

完成本課後，請查看我們的 [生成式 AI 學習系列](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升您的生成式 AI 知識！

前往第 10 課繼續學習。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->