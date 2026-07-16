# 面向初學者的生成式 AI 小型語言模型介紹
生成式 AI 是人工智能的一個迷人領域，專注於建立能夠創造新內容的系統。這些內容可以涵蓋文字、圖像、音樂，甚至整個虛擬環境。生成式 AI 最令人興奮的應用之一就是語言模型領域。

## 什麼是小型語言模型？

小型語言模型（SLM）代表大型語言模型（LLM）的縮小版本，利用了大型語言模型的許多架構原則和技術，同時顯示出顯著降低的運算負荷。

SLM 是設計用來生成類似人類文字的語言模型子集。與其較大的對應模型如 GPT-4 不同，SLM 更為緊湊且高效，適合運算資源有限的應用場合。儘管體積較小，它們仍然能執行多種任務。SLM 通常通過壓縮或蒸餾大型語言模型而構建，目標是保留原始模型的大部分功能和語言能力。模型大小的減少降低了整體複雜度，使得 SLM 在記憶體使用與運算需求兩方面都更有效率。儘管經過這些優化，SLM 仍能執行廣泛的自然語言處理（NLP）任務：

- 文字生成：創建連貫且語境相關的句子或段落。
- 文字補全：根據給定提示預測並補全句子。
- 翻譯：將文字從一種語言轉換為另一種語言。
- 摘要：將長篇文本濃縮成更短、更易消化的摘要。

雖然相比較大型模型，在性能或理解深度上有些許取捨。

## 小型語言模型如何運作？
SLM 在大量文字數據上進行訓練。在訓練過程中，它們學習語言的模式與結構，使其能生成語法正確且語境恰當的文字。訓練過程包括：

- 數據收集：從各種來源蒐集大量文本數據。
- 預處理：清理與組織數據，使其適合訓練。
- 訓練：利用機器學習算法教模型如何理解和生成文字。
- 微調：調整模型以提升其在特定任務上的表現。

SLM 的發展符合日益增長的需求，即能在資源受限的環境中部署模型，比如行動裝置或邊緣計算平台，在這些環境中，完整規模的 LLM 由於龐大的資源需求可能不切實際。SLM 聚焦於效率，平衡性能與可及性，使其可在多個領域中廣泛應用。

![slm](../../../translated_images/zh-MO/slm.4058842744d0444a.webp)

## 學習目標

在本課程中，我們希望介紹 SLM 的知識，並結合 Microsoft Phi-3，學習文本內容、視覺和 MoE 的不同應用場景。

課程結束後，你應該能回答以下問題：

- 什麼是 SLM？
- SLM 與 LLM 有何差異？
- 什麼是 Microsoft Phi-3/3.5 系列？
- 如何運行 Microsoft Phi-3/3.5 系列的推理？

準備好了嗎？讓我們開始吧。

## 大型語言模型（LLMs）與小型語言模型（SLMs）之間的區別

LLM 與 SLM 都建立在機率機器學習的基礎原理之上，在架構設計、訓練方法、數據生成過程和模型評估技術方面遵循相似的路徑。然而，有幾個關鍵因素區分這兩種模型。

## 小型語言模型的應用

SLM 具有廣泛的應用，包括：

- 聊天機器人：提供客戶支持，以對話形式與用戶互動。
- 內容創作：協助作家產生靈感，甚至撰寫整篇文章。
- 教育：幫助學生完成寫作任務或學習新語言。
- 無障礙：為有障礙人士創造工具，例如文字轉語音系統。

<strong>大小</strong>
  
LLM 與 SLM 之間主要區別在於模型規模。LLM，例如 ChatGPT（GPT-4），參數數量估計高達 1.76 兆，而開源 SLM 如 Mistral 7B 則設計為擁有顯著較少的參數，約 70 億。這一差異主要源於模型架構與訓練過程的不同。例如，ChatGPT 採用編碼器-解碼器架構中的自注意力機制，而 Mistral 7B 採用滑動視窗注意力，使得僅解碼器模型的訓練更有效率。架構差異對模型的複雜性與性能有深遠影響。

<strong>理解能力</strong>

SLM 通常針對特定領域進行優化，因而高度專精，但在跨多領域提供廣泛語境理解方面可能有限。相比之下，LLM 致力於模擬更全面的人類智慧。LLM 通過龐大且多樣化的數據集訓練，旨在在多種領域出色表現，提供較大靈活性與適應能力。因此，LLM 更適合用於多種下游任務，如自然語言處理與程式設計。

<strong>計算需求</strong>

LLM 的訓練與部署過程資源密集，通常需要大量計算基礎設施，包括大型 GPU 叢集。例如，從零開始訓練像 ChatGPT 這樣的模型，可能需要數千顆 GPU 持續數週。相比之下，SLM 參數數量較少，在計算資源方面更容易取得。像 Mistral 7B 這類模型可以在具備中等 GPU 能力的本地機器上訓練與執行，雖然訓練仍需數小時並使用多顆 GPU。

<strong>偏見</strong>

偏見是 LLM 的一個已知問題，主要由於訓練資料的來源性質。這些模型通常依賴互聯網上的原始公開資料，這可能會低估或錯誤呈現某些群體，導致錯誤標註，或反映出因方言、地理差異與語法規則而產生的語言偏見。此外，LLM 複雜的架構可能無意中加劇偏見，如果未經細緻微調，這些偏見可能不易察覺。反觀 SLM 由於訓練於更受限、特定領域的數據集，因此相對較少受此類偏見影響，但並非完全免疫。

<strong>推理速度</strong>

SLM 較小的體積使其在推理速度上具有顯著優勢，能夠高效在本地硬件上生成結果，而無需大量並行處理。相比之下，LLM 由於規模與複雜性，常需大量並行計算資源才能實現可接受的推理時間。多使用者同時訪問時，更進一步拖慢 LLM 的反應速度，尤其在大規模部署時尤為明顯。

總結來說，儘管 LLM 與 SLM 均根植於機器學習基礎，但在模型大小、資源需求、語境理解、偏見敏感度與推理速度等方面有明顯差異。這些差異反映了兩者適用於不同場景的特性：LLM 更通用但資源密集，SLM 則提供域專精效率與較低計算需求。

***註：本課程將以 Microsoft Phi-3 / 3.5 為例介紹 SLM。***

## 介紹 Phi-3 / Phi-3.5 系列

Phi-3 / 3.5 系列主要面向文本、視覺和代理（MoE）應用場景：

### Phi-3 / 3.5 指令調教模型

主要用於文本生成、對話完成和內容信息提取等。

**Phi-3-mini**

3.8B 參數的語言模型可在 Microsoft Foundry、Hugging Face 和 Ollama 上獲得。Phi-3 模型在主要基準測試中顯著優於同規模及更大型的語言模型（參見下方基準數據，數字越高越好）。Phi-3-mini 的性能超越兩倍於它的模型，而 Phi-3-small 和 Phi-3-medium 則超越包括 GPT-3.5 在內的更大型模型。

**Phi-3-small 與 medium**

擁有僅 7B 參數的 Phi-3-small，在多種語言、推理、編碼與數學基準中超越 GPT-3.5T。

14B 參數的 Phi-3-medium 延續此趨勢，表現優於 Gemini 1.0 Pro。

**Phi-3.5-mini**

可視為 Phi-3-mini 的升級版本。雖然參數數量不變，但改善了多語言支持能力（支援20+語言：阿拉伯語、中文、捷克語、丹麥語、荷蘭語、英語、芬蘭語、法語、德語、希伯來語、匈牙利語、義大利語、日語、韓語、挪威語、波蘭語、葡萄牙語、俄語、西班牙語、瑞典語、泰語、土耳其語、烏克蘭語），並加強長上下文支持。

擁有 3.8B 參數的 Phi-3.5-mini，在同等規模的語言模型中表現最佳，並可與兩倍規模的模型相匹敵。

### Phi-3 / 3.5 視覺模型

可將 Phi-3/3.5 指令調教模型視為 Phi 的理解能力，而視覺模型則賦予 Phi 觀察世界的「眼睛」。


**Phi-3-Vision**

擁有僅 4.2B 參數的 Phi-3-vision 延續此趨勢，在一般視覺推理任務、光學字符識別（OCR）及表格與圖表理解任務中表現優於更大型模型如 Claude-3 Haiku 和 Gemini 1.0 Pro V。


**Phi-3.5-Vision**

Phi-3.5-Vision 也為 Phi-3-Vision 的升級版本，新增多圖像支持。可理解為視覺能力的提升，不僅能看圖片，還能觀看影片。

Phi-3.5-vision 在 OCR、表格及圖表理解任務上超越了更大型模型如 Claude-3.5 Sonnet 與 Gemini 1.5 Flash，在一般視覺知識推理任務上並駕齊驅。支持多幀輸入，即可對多張輸入圖像進行推理。


### Phi-3.5-MoE

***專家混合模型（Mixture of Experts, MoE）*** 使模型以更少的計算資源預訓練，允許在相同計算預算下大幅擴展模型或數據集規模。尤其是，MoE 模型在預訓練階段能比稠密模型更快達到同等質量。

Phi-3.5-MoE 包含16個3.8B參數的專家模組。Phi-3.5-MoE 活躍參數僅6.6B，卻可在推理、語言理解及數學方面達到與更大型模型相似的水平。

我們可以根據不同場景使用 Phi-3/3.5 系列模型。不同於 LLM，Phi-3/3.5-mini 或 Phi-3/3.5-Vision 可以部署在邊緣設備上。


## 如何使用 Phi-3/3.5 系列模型

我們希望在不同場景中應用 Phi-3/3.5。接下來，我們將根據不同場景展示如何使用 Phi-3/3.5。

![phi3](../../../translated_images/zh-MO/phi3.655208c3186ae381.webp)

### 通過雲端 API 進行推理

**Microsoft Foundry 模型**

> **注意：** GitHub Models 將於 2026 年 7 月底退休。[Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 是直接替代方案。

Microsoft Foundry Models 是最直接的方法。您可以通過 Foundry 模型目錄快速訪問 Phi-3/3.5-Instruct 模型。結合 Azure AI 推理 SDK / OpenAI SDK，您可以通過程式碼訪問 API 來完成 Phi-3/3.5-Instruct 調用。您也可以通過 Playground 測試不同效果。

- 示範：在中文場景中比較 Phi-3-mini 和 Phi-3.5-mini 的效果

![phi3](../../../translated_images/zh-MO/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/zh-MO/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

若要使用視覺和 MoE 模型，亦可透過 Microsoft Foundry 完成交互調用。如果有興趣，可參閱 Phi-3 食譜，學習如何通過 Microsoft Foundry 調用 Phi-3/3.5 Instruct、Vision 及 MoE [點擊此連結](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

除了雲端的 Microsoft Foundry Models 目錄外，您也可以使用 [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) 完成相關調用。您可以造訪 NVIDIA NIM 完成 Phi-3/3.5 系列的 API 調用。NVIDIA NIM（NVIDIA Inference Microservices）是一套加速推理微服務，旨在幫助開發者高效部署 AI 模型於各種環境，包括雲端、數據中心及工作站。

NVIDIA NIM 的一些主要特點：

- **易於部署：** NIM 允許通過單一命令部署 AI 模型，容易整合入現有工作流程。

- **優化效能:** 利用 NVIDIA 預先優化的推理引擎，如 TensorRT 和 TensorRT-LLM，以確保低延遲和高吞吐量。
- **可擴展性:** NIM 支援 Kubernetes 的自動擴展，使其能有效處理不同工作負載。
- **安全與控制:** 組織可透過在自家管理基礎設施上自行部署 NIM 微服務，掌控其數據和應用程式。
- **標準 API:** NIM 提供業界標準 API，方便構建和整合像聊天機器人、AI 助手等人工智能應用。

NIM 是 NVIDIA AI Enterprise 的一部分，旨在簡化 AI 模型的部署與運營，確保其在 NVIDIA GPU 上高效運行。

- 演示：使用 NVIDIA NIM 調用 Phi-3.5-Vision-API  [[點擊此連結](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### 在本地運行 Phi-3/3.5
Phi-3，或任何像 GPT-3 這類語言模型的推理，是指根據所接收的輸入，生成回應或預測的過程。當你向 Phi-3 提供提示或問題時，它會利用其訓練好的神經網絡，透過分析訓練資料中的模式和關聯，推斷出最可能且相關的回答。

**Hugging Face Transformer**
Hugging Face Transformers 是一個強大的庫，專為自然語言處理 (NLP) 及其他機器學習任務設計。以下是它的一些重點說明：

1. <strong>預訓練模型</strong>：提供數千個預訓練模型，可用於文本分類、命名實體識別、問答、摘要、翻譯及文本生成等多種任務。

2. <strong>框架互通性</strong>：該庫支援多種深度學習框架，包括 PyTorch、TensorFlow 及 JAX，允許你在一個框架中訓練模型，並於另一框架中使用它。

3. <strong>多模態能力</strong>：除了 NLP，Hugging Face Transformers 還支援電腦視覺（例如圖像分類、物體檢測）和音頻處理（例如語音識別、音頻分類）等任務。

4. <strong>易用性</strong>：此庫提供 API 和工具，方便用戶輕鬆下載及微調模型，對初學者與專家都非常友善。

5. <strong>社群與資源</strong>：Hugging Face 擁有活躍的社群以及豐富的文檔、教程和指南，協助用戶快速上手並充分利用該庫。
[官方文件](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) 或其 [GitHub 儲存庫](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst)。

這是最常用的方法，但也需要 GPU 加速。畢竟像 Vision 和 MoE 這類場景需要大量計算，如果未量化，CPU 上會很慢。


- 演示：使用 Transformer 調用 Phi-3.5-Instruct [點擊此連結](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- 演示：使用 Transformer 調用 Phi-3.5-Vision [點擊此連結](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- 演示：使用 Transformer 調用 Phi-3.5-MoE [點擊此連結](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) 是一個平台，旨在更簡單地於本機運行大型語言模型 (LLM)。它支援多款模型，如 Llama 3.1、Phi 3、Mistral 和 Gemma 2 等。該平台將模型權重、配置和數據打包成單一套件，讓用戶更輕鬆自訂及創建自己的模型。Ollama 支援 macOS、Linux 和 Windows。如想嘗試或部署 LLM 而不依賴雲端服務，這是一個很好的工具。Ollama 是最直接的方式，只需執行以下命令即可。


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) 是微軟的離線本地執行環境，讓你能完全在自有硬件上運行像 Phi 這類模型 — 不需 Azure 訂閱、API 金鑰或網路連線。它會自動選擇最佳的執行提供者（NPU、GPU 或 CPU），並暴露兼容 OpenAI 的端點，使現有 `openai` / Azure AI 推理 SDK 代碼只需最小變動即可指向此端點。請參閱 [Foundry Local 文件](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) 開始使用。

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

或直接在 Python 中使用 SDK：

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime for GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) 是一個跨平台的推理及訓練機器學習加速器。ONNX Runtime for Generative AI (GENAI) 是一個強大的工具，幫助你高效地在不同平台上運行生成式 AI 模型。

## 什麼是 ONNX Runtime？
ONNX Runtime 是一個開源專案，能實現機器學習模型的高效推理。它支援 Open Neural Network Exchange (ONNX) 格式的模型，這是一種表示機器學習模型的標準。ONNX Runtime 推理能提升客戶體驗速度並降低成本，支援深度學習框架如 PyTorch 和 TensorFlow/Keras 的模型，以及傳統機器學習庫如 scikit-learn、LightGBM、XGBoost 等。ONNX Runtime 與不同硬件、驅動和操作系統相容，並通過結合硬件加速器、圖優化和轉換提供最佳性能。

## 什麼是生成式 AI？
生成式 AI 指的是能根據其所訓練的數據生成新內容的 AI 系統，如文本、圖像或音樂。範例包括語言模型 GPT-3 和圖像生成模型 Stable Diffusion。ONNX Runtime for GenAI 庫為 ONNX 模型提供生成式 AI 的完整工作流程，包括使用 ONNX Runtime 進行推理、logits 處理、搜尋和抽樣，以及 KV 緩存管理。

## ONNX Runtime for GENAI
ONNX Runtime for GENAI 擴展了 ONNX Runtime 的功能，以支援生成式 AI 模型。以下是一些主要特點：

- **廣泛平台支援:** 支援 Windows、Linux、macOS、Android 和 iOS 等多種平台。
- **模型支持:** 支援許多流行的生成式 AI 模型，如 LLaMA、GPT-Neo、BLOOM 等。
- **性能優化:** 包含針對 NVIDIA GPU、AMD GPU 等不同硬件加速器的優化。
- **易用性:** 提供方便集成應用的 API，讓你輕鬆生成文本、圖像和其他內容，只需最少代碼。
- 用戶可呼叫高階的 generate() 方法，或在迴圈中逐一運行模型每次產生一個標記，並可選擇在迴圈中更新生成參數。
- ONNX Runtime 還支援貪婪法/束搜索和 TopP、TopK 抽樣來生成標記序列，以及內建的 logits 處理如重複懲罰。你也可以輕鬆添加自訂評分。

## 入門指南
若要開始使用 ONNX Runtime for GENAI，可依照以下步驟：

### 安裝 ONNX Runtime：
```Python
pip install onnxruntime
```
### 安裝生成式 AI 擴展：
```Python
pip install onnxruntime-genai
```

### 運行模型：以下是 Python 的簡單範例：
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
### 演示：使用 ONNX Runtime GenAI 調用 Phi-3.5-Vision


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

除了 ONNX Runtime、Ollama 和 Foundry Local 參考方法，我們亦可根據不同廠商提供的模型參考方法，完成量化模型參考。例如 Apple MLX 框架配合 Apple Metal、Qualcomm QNN 配合 NPU、Intel OpenVINO 配合 CPU/GPU 等。你亦可從 [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst) 獲取更多內容。


## 更多

我們已學習 Phi-3/3.5 家族的基礎，但要更深入了解 SLM，還需要更多知識。你可以在 Phi-3 Cookbook 找到相關答案。若想了解更多，請造訪 [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->