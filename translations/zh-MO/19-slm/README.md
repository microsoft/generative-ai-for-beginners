# 為初學者介紹生成式 AI 的小型語言模型
生成式 AI 是人工智能中一個令人著迷的領域，專注於創建能生成新內容的系統。這些內容可涵蓋文字、圖像、音樂甚至整個虛擬環境。生成式 AI 最激動人心的應用之一就是語言模型的領域。

## 甚麼是小型語言模型？

小型語言模型（SLM）是大型語言模型（LLM）的縮小版本，利用了很多大型模型的架構原則和技術，但計算需求明顯降低。

SLM 是一類旨在產生類人文本的語言模型子集。不同於 GPT-4 這類大型模型，SLM 體積更小、效率更高，非常適合計算資源有限的應用。儘管體型較小，它們仍能執行多種任務。通常，SLM 是通過壓縮或蒸餾大型模型而建成，目標是在保留原始模型的大部分功能和語言能力的同時，縮小模型規模。模型規模縮小後，整體複雜度下降，使得 SLM 在記憶體使用和計算要求上更為高效。儘管經過優化，SLM 仍能執行廣泛的自然語言處理（NLP）任務：

- 文本生成：創建連貫且符合語境的句子或段落。
- 文本補全：根據給定提示預測並完成句子。
- 翻譯：將文本從一種語言轉換為另一種語言。
- 摘要：將冗長文本濃縮為更短、更易理解的摘要。

當然，相較於大型模型，它們在性能或理解深度上有所取捨。

## 小型語言模型如何運作？
SLM 通過大量文本數據進行訓練。在訓練過程中，它們學習語言的規律和結構，使其能生成語法正確且語境貼切的文字。訓練流程包括：

- 數據收集：從各種來源收集大量文本數據。
- 預處理：清理並組織數據，使其適合訓練。
- 訓練：利用機器學習算法教模型理解和生成文本。
- 微調：調整模型以提升其在特定任務上的表現。

SLM 的發展滿足了對可於資源受限環境（如移動設備或邊緣計算平台）部署模型日益增長的需求，而全規模大型語言模型因資源要求昂貴而難以應用。通過強調效率，SLM 在性能與可及性間取得平衡，促進其在不同領域的廣泛應用。

![slm](../../../translated_images/zh-MO/slm.4058842744d0444a.webp)

## 學習目標

本課程旨在介紹 SLM 的知識，並結合 Microsoft Phi-3，學習文本、視覺和 MoE 的不同場景。

課程結束時，您應能回答以下問題：

- 甚麼是 SLM？
- SLM 與 LLM 有甚麼區別？
- 甚麼是 Microsoft Phi-3/3.5 家族？
- 如何使用 Microsoft Phi-3/3.5 家族進行推理？

準備好了嗎？讓我們開始吧。

## 大型語言模型（LLM）與小型語言模型（SLM）的區別

LLM 與 SLM 均基於概率機器學習的基礎原理，架構設計、訓練方法、數據生成及模型評估技術相似。但兩者之間存在若干重要差異。

## 小型語言模型的應用

SLM 廣泛應用於：

- 聊天機器人：提供客戶支持並以對話形式與用戶互動。
- 內容創作：協助作者生成靈感，甚至撰寫整篇文章。
- 教育：幫助學生完成寫作作業或學習新語言。
- 輔助功能：為殘障人士創建工具，如文字轉語音系統。

<strong>規模</strong>
  
LLM 與 SLM 的一大主要區別在於模型規模。LLM 如 ChatGPT（GPT-4）可包含約 1.76 萬億參數，而開源 SLM 如 Mistral 7B 僅約 70 億參數。這種差異主要源於模型架構和訓練過程的不同。例如，ChatGPT 採用編碼器-解碼器結構中的自注意力機制，而 Mistral 7B 使用滑動窗口注意力，允許在僅解碼器的模型中更高效地訓練。該架構差異對模型複雜度和性能影響深遠。

<strong>理解能力</strong>

SLM 通常針對特定領域優化，在該領域內非常專精，但可能限制於跨多領域的廣泛語境理解。相反，LLM 旨在模擬較全面的人類智慧。透過訓練於大量且多樣化數據集，LLM 設計為在多領域表現優異，提供更強的多用途性及適應性。因此，LLM 更適用於廣泛下游任務，如自然語言處理和編程。

<strong>計算需求</strong>

LLM 的訓練與部署需求龐大資源，經常需大型 GPU 叢集支援。例如，從零開始訓練 ChatGPT 可能需要成千上萬 GPU 長時間運算。相比之下，SLM 由於參數量較少，在計算資源上的需求較為親民。如 Mistral 7B 可在配備中等 GPU 的本地機器上訓練和運行，雖然仍需多 GPU 幾小時訓練。

<strong>偏見</strong>

偏見是 LLM 中已知的問題，主要源於訓練數據的特性。這些模型常依賴來自互聯網的原始公開數據，可能對某些群體不足或誤解、帶有標籤錯誤，或反映方言、地區差異及語法規則所致的語言偏見。此外，LLM 複雜架構可能無意中加劇偏見，且若未精心微調，可能不易察覺。相較之下，SLM 受訓於更受限、領域特定的數據集，固有地較不易受此類偏見影響，但並非完全免疫。

<strong>推理速度</strong>

SLM 由於體積更小，在推理速度上具有顯著優勢，可在本地硬體上高效生成結果，無需大規模並行運算。反之，LLM 因規模龐大和結構複雜，往往需龐大的並行計算資源才能獲得可接受的推理時間。多個同時用戶使用時，尤其於大規模部署時，LLM 響應速度進一步下降。

總結而言，LLM 和 SLM 雖都基於機器學習的根底，但在模型大小、資源需求、語境理解、偏見敏感度及推理速度等方面有顯著差異。這些差異反映了各自適用的場景，LLM 較為通用但資源消耗大，SLM 則提供特定領域的效率與較低計算需求。

***注意：本課程以 Microsoft Phi-3 / 3.5 為例介紹 SLM。***

## 介紹 Phi-3 / Phi-3.5 家族

Phi-3 / 3.5 家族主要針對文本、視覺以及 Agent（MoE）應用場景：

### Phi-3 / 3.5 指令模型

主要應用於文本生成、聊天補全及內容信息提取等。

**Phi-3-mini**

這款 38 億參數語言模型可於 Microsoft Azure AI Studio、Hugging Face 和 Ollama 上取得。Phi-3 在主要基準測試中顯著超越相同或更大規模的語言模型（見以下基準數字，數值越高越好）。Phi-3-mini 表現優於兩倍大小的模型，而 Phi-3-small 與 Phi-3-medium 則勝過更大模型，包括 GPT-3.5。

**Phi-3-small 與 medium**

Phi-3-small 僅有 70 億參數，在多種語言、推理、編碼與數學基準測試中打敗 GPT-3.5T。

Phi-3-medium 配備 140 億參數，延續此趨勢，優於 Gemini 1.0 Pro。

**Phi-3.5-mini**

可視為 Phi-3-mini 的升級版。參數量不變，但強化了多語言支持（支持 20 多種語言：阿拉伯語、中文、捷克語、丹麥語、荷蘭語、英語、芬蘭語、法語、德語、希伯來語、匈牙利語、意大利語、日語、韓語、挪威語、波蘭語、葡萄牙語、俄語、西班牙語、瑞典語、泰語、土耳其語、烏克蘭語）並增強對長上下文的支持。

配備 38 億參數的 Phi-3.5-mini 表現超越同規模語言模型，並媲美兩倍規模模型。

### Phi-3 / 3.5 視覺模型

我們可將 Phi-3/3.5 的 Instruct 模型視為 Phi 理解能力，而 Vision 賦予 Phi 眼睛去理解世界。


**Phi-3-Vision**

Phi-3-vision 擁有僅 42 億參數，持續這一優勢，在一般視覺推理任務、OCR、表格和圖表理解方面表現超越較大模型如 Claude-3 Haiku 和 Gemini 1.0 Pro V。


**Phi-3.5-Vision**

Phi-3.5-Vision 是 Phi-3-Vision 的升級版，新增多圖像支持。您可將其視為視覺能力提升，不僅能看圖，還可看視頻。

Phi-3.5-vision 在 OCR、表格和圖表理解任務中超越較大模型如 Claude-3.5 Sonnet 和 Gemini 1.5 Flash，並在一般視覺知識推理任務上與其不相上下。支持多幀輸入，即對多張圖像進行推理。


### Phi-3.5-MoE

***專家混合模型（MoE）*** 使模型能以更低的計算量進行預訓練，意味著可在相同計算資源下大幅擴展模型或數據集大小。尤其是 MoE 模型可在預訓練期間更快達到與密集模型相當的品質。

Phi-3.5-MoE 包含 16 個 38 億參數的專家模塊。Phi-3.5-MoE 以僅 66 億主動參數實現了與更大型模型相似的推理、語言理解和數學能力。

我們可根據場景使用 Phi-3/3.5 家族模型。不同於 LLM，Phi-3/3.5-mini 或 Phi-3/3.5-Vision 可在邊緣設備上部署。


## 如何使用 Phi-3/3.5 家族模型

我們希望在不同場景下運用 Phi-3/3.5。接下來將基於不同場景示範。

![phi3](../../../translated_images/zh-MO/phi3.655208c3186ae381.webp)

### 透過雲端 API 進行推理

**GitHub Models**

GitHub Models 是最直接的方式。您可透過 GitHub Models 快速訪問 Phi-3/3.5-Instruct 模型。結合 Azure AI Inference SDK / OpenAI SDK，您可透過程式碼調用 API 來完成 Phi-3/3.5-Instruct 調用。也可透過 Playground 測試不同效果。

- 示範：Phi-3-mini 和 Phi-3.5-mini 在中文場景中的效果比較

![phi3](../../../translated_images/zh-MO/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/zh-MO/gh2.07d7985af66f178d.webp)


**Azure AI Studio**

若想使用視覺和 MoE 模型，可使用 Azure AI Studio 完成調用。如感興趣，可閱讀 Phi-3 Cookbook，學習如何透過 Azure AI Studio 調用 Phi-3/3.5 指令、視覺及 MoE [點此連結](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

除了 Azure 和 GitHub 提供的雲端模型目錄解決方案外，您也可使用 [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) 完成相關調用。您可以訪問 NVIDIA NIM，以完成 Phi-3/3.5 家族的 API 調用。NVIDIA NIM（NVIDIA 推理微服務）是一組加速推理微服務，旨在協助開發者在雲端、數據中心及工作站等多種環境中高效部署 AI 模型。

以下是 NVIDIA NIM 的一些關鍵特點：

- **部署簡易：** NIM 可通過一條命令部署 AI 模型，方便集成至現有工作流程。
- **優化性能：** 利用 NVIDIA 預優化推理引擎，如 TensorRT 和 TensorRT-LLM，確保低延遲和高吞吐量。
- **可擴展性：** NIM 支持 Kubernetes 自動擴展，能有效應對變化的工作負載。

- **安全性與控制：** 組織可以透過自我託管 NIM 微服務於其自主管理的基礎設施上，保持對其數據和應用程序的控制權。
- **標準 API：** NIM 提供業界標準的 API，讓構建與整合 AI 應用程式（如聊天機械人、AI 助理等）變得簡單。

NIM 是 NVIDIA AI Enterprise 的一部分，旨在簡化 AI 模型的部署和運行，確保它們能高效地在 NVIDIA GPU 上運行。

- 範例演示：使用 NVIDIA NIM 調用 Phi-3.5-Vision-API [[點擊此連結](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### 在本地運行 Phi-3/3.5
關於 Phi-3 或任何類似 GPT-3 的語言模型，推理指的是根據所接收的輸入生成回應或預測的過程。當您向 Phi-3 提供提示或問題時，它會利用其訓練的神經網絡，通過分析所訓練數據中的模式和關聯，推斷出最可能且相關的回應。

**Hugging Face Transformer**
Hugging Face Transformers 是一個強大的庫，專為自然語言處理（NLP）及其他機器學習任務設計。以下是一些重點：

1. <strong>預訓練模型</strong>：它提供數千個預訓練模型，可用於文本分類、命名實體識別、問答、摘要、翻譯和文本生成等多種任務。

2. <strong>框架互通性</strong>：該庫支持多個深度學習框架，包括 PyTorch、TensorFlow 和 JAX。這使您可以在一個框架中訓練模型，並在另一框架中使用。

3. <strong>多模態能力</strong>：除了 NLP，Hugging Face Transformers 還支持計算機視覺（例如圖像分類、物體檢測）和音頻處理（如語音識別、音頻分類）等任務。

4. <strong>易用性</strong>：該庫提供便利的 API 和工具，用於輕鬆下載和微調模型，讓初學者和專家都能輕鬆使用。

5. <strong>社群與資源</strong>：Hugging Face 擁有活躍的社群以及豐富的文件、教程和指南，幫助用戶快速入門並充分利用該庫。
[官方文件](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) 或其 [GitHub 倉庫](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst)。

這是最常用的方法，但它也需 GPU 加速。畢竟像 Vision 和 MoE 這類場景需要大量計算，若未量化，在 CPU 上會非常緩慢。


- 範例演示：使用 Transformer 調用 Phi-3.5-Instruct [點擊此連結](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- 範例演示：使用 Transformer 調用 Phi-3.5-Vision [點擊此連結](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- 範例演示：使用 Transformer 調用 Phi-3.5-MoE [點擊此連結](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) 是一個旨在讓您更容易在本機運行大型語言模型 (LLM) 的平台。它支持多種模型，如 Llama 3.1、Phi 3、Mistral 和 Gemma 2 等。此平台將模型權重、配置和數據打包成一體，簡化流程，讓用戶更容易自定義和創建自己的模型。Ollama 支援 macOS、Linux 和 Windows。如果您想在不依賴雲端服務的情況下試驗或部署 LLM，這是一個非常好的工具。Ollama 是最直接的方法，只需執行以下命令即可。


```bash

ollama run phi3.5

```


**ONNX Runtime for GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) 是一個跨平台的推理和訓練機器學習加速器。ONNX Runtime for Generative AI（GENAI）是一個強大的工具，幫助您高效地在各種平台上運行生成式 AI 模型。

## 什麼是 ONNX Runtime？
ONNX Runtime 是一個開源項目，使機器學習模型的推理性能達到高效。它支持 Open Neural Network Exchange（ONNX）格式的模型，該格式是表示機器學習模型的標準。ONNX Runtime 推理可加速用戶體驗並降低成本，支持來自 PyTorch 和 TensorFlow/Keras 等深度學習框架以及 scikit-learn、LightGBM、XGBoost 等經典機器學習庫的模型。ONNX Runtime 與不同硬體、驅動及作業系統相容，通過結合硬體加速器以及圖形優化和轉換來提供最佳性能。

## 什麼是生成式 AI？
生成式 AI 指能根據所訓練數據產生新內容的 AI 系統，如文本、圖像或音樂。例子包括 GPT-3 類語言模型和 Stable Diffusion 類圖像生成模型。ONNX Runtime for GenAI 庫提供 ONNX 模型的生成式 AI 迴圈功能，包括使用 ONNX Runtime 進行推理、對 logits 的處理、搜索與採樣，以及 KV 快取管理。

## ONNX Runtime for GENAI
ONNX Runtime for GENAI 擴展了 ONNX Runtime 的功能，以支持生成式 AI 模型。以下是一些主要功能：

- **廣泛的平台支持：** 可在 Windows、Linux、macOS、Android 及 iOS 等多種平台運行。
- **模型支持：** 支持多種熱門的生成式 AI 模型，如 LLaMA、GPT-Neo、BLOOM 等。
- **效能優化：** 包含針對 NVIDIA GPU、AMD GPU 等硬體加速器的優化。
- **易用性：** 提供 API 方便應用程式集成，讓您能以最少的程式碼生成文本、圖像及其他內容。
- 用戶可調用高階的 generate() 方法，或在迴圈中逐步運行模型，每次生成一個標記，並可選擇在迴圈內更新生成參數。
- ONNX Runtime 還支援貪婪/束搜尋以及 TopP、TopK 採樣來生成標記序列，內建 logits 處理如重複懲罰，也可以方便地添加自訂評分機制。

## 開始使用
您可以透過以下步驟開始使用 ONNX Runtime for GENAI：

### 安裝 ONNX Runtime：
```Python
pip install onnxruntime
```
### 安裝生成式 AI 擴展：
```Python
pip install onnxruntime-genai
```

### 運行模型：以下是一個簡單的 Python 範例：
```Python
import onnxruntime_genai as og

model = og.Model('path_to_your_model.onnx')

tokenizer = og.Tokenizer(model)

input_text = "Hello, how are you?"

input_tokens = tokenizer.encode(input_text)

output_tokens = model.generate(input_tokens)

output_text = tokenizer.decode(output_tokens)

print(output_text) 
```
### 範例演示：使用 ONNX Runtime GenAI 調用 Phi-3.5-Vision


```python

import onnxruntime_genai as og

model_path = './Your Phi-3.5-vision-instruct ONNX Path'

img_path = './Your Image Path'

model = og.Model(model_path)

processor = model.create_multimodal_processor()

tokenizer_stream = processor.create_stream()

text = "Your Prompt"

prompt = "<|user|>\n"

prompt += "<|image_1|>\n"

prompt += f"{text}<|end|>\n"

prompt += "<|assistant|>\n"

image = og.Images.open(img_path)

inputs = processor(prompt, images=image)

params = og.GeneratorParams(model)

params.set_inputs(inputs)

params.set_search_options(max_length=3072)

generator = og.Generator(model, params)

while not generator.is_done():

    generator.compute_logits()
    
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    
    output = tokenizer_stream.decode(new_token)
    
    print(tokenizer_stream.decode(new_token), end='', flush=True)

```


<strong>其他</strong>

除了 ONNX Runtime 和 Ollama 參考方法外，我們還可以根據不同廠商提供的模型參考方法，完成量化模型的參考。如 Apple MLX 框架搭配 Apple Metal、高通 QNN 配合 NPU、英特爾 OpenVINO 支援 CPU/GPU 等。您還可以從 [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst) 獲得更多資訊。


## 更多

我們已經學習了 Phi-3/3.5 系列的基礎知識，但想深入了解 SLM，我們需要更多知識。您可以在 Phi-3 Cookbook 找到答案。如欲進一步學習，請造訪 [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->