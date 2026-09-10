# 建立低程式碼 AI 應用程式

[![建立低程式碼 AI 應用程式](../../../translated_images/zh-TW/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(點擊上方圖片觀看本課程影片)_

## 介紹

現在我們已經學會如何建立影像生成應用程式，接下來來談談低程式碼。生成式 AI 可以用於包括低程式碼在內的多種領域，但什麼是低程式碼，以及我們如何將 AI 加入其中呢？

透過低程式碼開發平台，傳統開發者和非開發者都可以更輕鬆地建立應用和解決方案。低程式碼開發平台讓您能以極少甚至不用程式碼的方式構建應用和解決方案。這是透過提供視覺化的開發環境，讓您拖放元件來建立應用與解決方案來實現的。這使您可以更快速且以更少資源建立應用程式和解決方案。在本課程中，我們將深入探討如何使用低程式碼，以及如何運用 Power Platform 以 AI 強化低程式碼開發。

Power Platform 提供組織機會，透過直覺式的低程式碼或無程式碼環境，讓團隊能自行建立解決方案。此環境簡化了解決方案的構建流程。使用 Power Platform，解決方案可以在數天或數週內完成，而非數月或數年。Power Platform 包含五個關鍵產品：Power Apps、Power Automate、Power BI、Power Pages 和 Copilot Studio。

本課程涵蓋：

- Power Platform 中生成式 AI 介紹
- Copilot 介紹與使用方式
- 使用生成式 AI 建立 Power Platform 中的應用與流程
- 認識 Power Platform 中 AI Builder 的 AI 模型
- 使用 Microsoft Copilot Studio 建立智慧代理

## 學習目標

完成本課程後，您將能：

- 了解 Copilot 在 Power Platform 中的運作方式。

- 為我們的教育新創公司建立學生作業追蹤應用程式。

- 建立使用 AI 從發票中擷取資訊的發票處理流程。

- 運用建立文字（Create Text）GPT AI 模型的最佳實務。

- 了解 Microsoft Copilot Studio 是什麼以及如何用它來建立智慧代理。

您在本課程中將使用的工具與技術有：

- **Power Apps**，用以建立學生作業追蹤應用程式，該平台提供低程式碼開發環境，可構建用於追蹤、管理與互動資料的應用程式。

- **Dataverse**，用以存放學生作業追蹤應用程式的資料，Dataverse 提供低程式碼資料平台以存儲應用程式的資料。

- **Power Automate**，用於發票處理流程，該平台提供低程式碼開發環境以建立自動化發票處理流程。

- **AI Builder**，用於發票處理 AI 模型，您將使用預建的 AI 模型來處理我們新創公司的發票。

## Power Platform 中的生成式 AI

以生成式 AI 強化低程式碼開發與應用是 Power Platform 的重要焦點。目標是讓每個人都能建立 AI 驅動的應用、網站、儀表板，並自動化流程，_不需要任何資料科學專業知識_。此目標是透過在 Power Platform 中以 Copilot 和 AI Builder 將生成式 AI 整合進低程式碼開發體驗來達成。

### 它是怎麼運作的？

Copilot 是一個 AI 助理，讓您透過自然語言的連續對話步驟描述需求，來建立 Power Platform 解決方案。例如，您可以指示 AI 助理說明您的應用將用到哪些欄位，Copilot 便會建立應用及其底層資料模型，或者指定如何在 Power Automate 中設定流程。

您也可以在應用畫面中使用由 Copilot 驅動的功能，讓使用者透過對話互動發掘洞察。

AI Builder 是 Power Platform 中的低程式碼 AI 功能，可使用 AI 模型協助自動化流程與預測結果。使用 AI Builder，您可將 AI 帶入與 Dataverse 或 SharePoint、OneDrive、Azure 等雲端資料來源連接的應用和流程。

Copilot 已在所有 Power Platform 產品中可用：Power Apps、Power Automate、Power BI、Power Pages 及 Copilot Studio（前身為 Power Virtual Agents）。AI Builder 可在 Power Apps 及 Power Automate 中使用。本課程將聚焦如何在 Power Apps 和 Power Automate 中使用 Copilot 與 AI Builder，為我們的教育新創公司建立解決方案。

### Power Apps 中的 Copilot

作為 Power Platform 的一部分，Power Apps 提供低程式碼開發環境，用於構建追蹤、管理和互動資料的應用程式。它是一套應用程式開發服務，具備可擴展資料平台，且能連接雲端服務和本地端資料。Power Apps 允許建立可在瀏覽器、平板和手機上執行並共享給同事的應用程式。Power Apps 透過簡單的介面讓使用者輕鬆入門應用開發，讓每位商業使用者或專業開發者都能建置客製應用。生成式 AI 透過 Copilot 更增強了應用開發體驗。

Power Apps 中的 Copilot AI 助理功能讓您描述您需要什麼樣的應用，以及您想讓應用追蹤、蒐集或顯示什麼資訊。Copilot 會根據您的描述生成響應式 Canvas 應用程式。您之後可自訂該應用以符合需求。AI Copilot 也會生成並建議一個帶有所需欄位的 Dataverse 表格，以存放您要追蹤的資料和一些範例資料。我們稍後將在本課程深入了解 Dataverse 是什麼，以及如何在 Power Apps 中使用它。您接著可利用 AI Copilot 助理功能，透過對話步驟自訂該表格以符合需求。此功能可直接從 Power Apps 首頁擷取使用。

### Power Automate 中的 Copilot

作為 Power Platform 的一部分，Power Automate 讓使用者在應用程式與服務間建立自動化工作流程。它有助自動化重複的商務流程，如溝通、資料收集與決策核准。其簡單的介面讓任何技術程度的使用者（從初學者到資深開發人員）都能自動化工作任務。流程開發體驗也透過 Copilot 的生成式 AI 得到強化。

Power Automate 中的 Copilot AI 助理功能讓您描述需要什麼樣的流程，以及期望流程執行哪些動作。Copilot 會根據您的描述生成一個流程。您之後可自訂該流程以符合需求。AI Copilot 也會生成並建議執行自動化任務所需的動作。我們稍後將在課程中探討流程是什麼以及如何使用它們。您接著可利用 AI Copilot 助理功能，透過對話步驟自訂該動作以符合需求。此功能可直接從 Power Automate 首頁擷取使用。

## 使用 Microsoft Copilot Studio 建立智慧代理

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst)（前身為 Power Virtual Agents）是 Power Platform 中低程式碼成員，用於構建<strong>AI 代理</strong>——可透過對話回答問題、執行動作並代表使用者自動化任務的輔助助理。與 Power Platform 其他產品一樣，您使用視覺化且以自然語言優先的方式建置這些代理：您描述想要代理執行的工作，Copilot Studio 協助搭建其指令、知識和動作。

對於我們的教育新創公司，您可以建構一個代理來回答學生關於課程的問題，檢查作業截止日期，甚至能替老師寄送電子郵件——全部無需撰寫程式碼。

以下是讓 Copilot Studio 強大的部分最新功能：

- <strong>從您的知識中生成答案</strong>。不必手動撰寫每段對話，您可連接<strong>知識來源</strong>——公開網站、SharePoint、OneDrive、Dataverse、上傳檔案或透過連接器接取企業資料——代理由此產生有根據的回答。

- <strong>生成式協調</strong>。代理不是依賴固定觸發詞，而是用 AI 理解請求，動態決定結合哪些知識、主題與動作來完成工作，包含串連多個步驟。

- <strong>動作與連接器</strong>。代理能執行動作，而不只是聊天。您可提供由 1500 多個預建 Power Platform 連接器、Power Automate 流程、自訂 REST API、提示語或<strong>模型上下文協議（MCP）</strong>伺服器支援的動作給代理。

- <strong>自主代理</strong>。代理不限於在聊天視窗回答。您可建立<strong>自主代理</strong>，它們會被事件觸發——如新電子郵件、Dataverse 中的新記錄或檔案上傳——隨後在背景執行任務。

- <strong>多代理協調</strong>。代理可呼叫其他代理。Copilot Studio 代理可將工作交接給或被其他代理擴充，包括發佈至 Microsoft 365 Copilot 的代理與 Microsoft Foundry 建立的代理。

- <strong>模型選擇</strong>。除了內建模型外，您可從 Microsoft Foundry 模型目錄帶入模型，調整代理的推理與回應方式。

- <strong>任意發佈</strong>。代理建立完成後，可發佈至多個通路——Microsoft Teams、Microsoft 365 Copilot、網站或自訂應用程式等——且透過 Power Platform 管理介面控管安全性、認證及分析。

您可在 [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst) 開始建立您的第一個代理，並於 [Microsoft Copilot Studio 文件](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst) 獲得更多資訊。

## 作業：使用 Copilot 管理我們新創公司的學生作業及發票

我們的新創公司提供線上課程給學生。公司迅速成長，目前正努力應對課程需求。我們聘請您作為 Power Platform 開發者，協助建立低程式碼解決方案，幫助管理學生作業與發票。該解決方案需能透過應用程式追蹤和管理學生作業，並透過工作流程自動化發票處理。請運用生成式 AI 來開發此解決方案。

初次使用 Copilot 時，您可參考 [Power Platform Copilot Prompt Library](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) 取得提示語入門。該資料庫內有多組可用於 Copilot 建立應用與流程的提示語。您亦可參考這些提示語了解如何向 Copilot 描述您的需求。

### 為我們的新創公司建立學生作業追蹤應用程式

我們新創公司的教育人員一直難以追蹤學生作業。他們過去用試算表追蹤作業，但隨著學生人數增多，管理變得困難。他們請您建立一個應用程式，協助他們追蹤與管理學生作業。該應用應能新增、檢視、更新及刪除作業，也應允許教育人員與學生查看已評分及未評分的作業。

您將使用 Power Apps 中的 Copilot，依以下步驟建立應用：

1. 前往 [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) 首頁。

1. 在首頁的文字區輸入您想建立的應用描述。例如，**_我想建立一個用於追蹤與管理學生作業的應用_**。點擊<strong>傳送</strong>按鈕將提示送給 AI Copilot。

![描述您想建立的應用](../../../translated_images/zh-TW/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. AI Copilot 會建議一個包含您要追蹤資料所需欄位的 Dataverse 表格，並提供範例資料。您可接著透過對話式步驟使用 AI Copilot 助理功能自訂該表格以符合需求。

   > <strong>重要</strong>：Dataverse 是 Power Platform 底層的資料平台，是一個低程式碼的資料平台，用於存放應用程式的資料。這是一項在 Microsoft 雲端中安全存儲資料並由您的 Power Platform 環境管理的全方位服務。它帶有內建資料治理功能，如資料分類、資料血緣、細微訪問控制等。您可於[此處](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko)了解更多關於 Dataverse 的資訊。

   ![建議您新表格的欄位](../../../translated_images/zh-TW/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. 教育人員希望能寄信給已提交作業的學生，告知作業進度。您可以使用 Copilot 為表格新增一個欄位來存放學生電子郵件。例如可使用下列提示：「**_我想增加一個欄位來存放學生電子郵件_**」。點擊<strong>傳送</strong>按鈕將提示送給 AI Copilot。

![新增欄位](../../../translated_images/zh-TW/copilot-new-column.35e15ff21acaf274.webp)

1. AI Copilot 會產生新的欄位，接著您可自訂該欄位以符合需求。


1. 完成資料表後，點選 **Create app** 按鈕以建立應用程式。

1. AI Copilot 將根據您的描述生成響應式 Canvas 應用程式，之後您可以自訂該應用程式以符合您的需求。

1. 教育工作者若要向學生發送電子郵件，您可以使用 Copilot 為應用程式新增一個畫面。例如，您可以使用以下提示新增一個畫面：**_我想新增一個用於寄送電子郵件給學生的畫面_**。點選 **Send** 按鈕將提示發送給 AI Copilot。

![透過提示指令新增畫面](../../../translated_images/zh-TW/copilot-new-screen.2e0bef7132a17392.webp)

1. AI Copilot 將生成一個新畫面，您之後可以自訂該畫面以符合您的需求。

1. 完成應用程式後，點選 **Save** 按鈕以儲存應用程式。

1. 若要與教育工作者分享應用程式，點選 **Share** 按鈕，然後再次點選 **Share** 按鈕。接著，您可以透過輸入教育工作者的電子郵件地址與他們分享應用程式。

> <strong>你的作業</strong>：您剛建立的應用程式是良好的起點，但仍有改進空間。使用電子郵件功能時，教育工作者必須手動輸入學生的電子郵件地址才能寄送郵件。您能否使用 Copilot 建立一個自動化流程，使教育工作者在學生提交作業時能自動寄送電子郵件？提示是利用適當的提示，您可以在 Power Automate 中使用 Copilot 建立此功能。

### 為我們的創業公司建立發票資訊資料表

我們創業公司的財務團隊一直在努力追蹤發票。他們一直使用試算表來追蹤發票，但隨著發票數量增加，管理變得困難。他們請您建立一個資料表，以協助他們儲存、追蹤和管理所收到發票的資訊。此資料表將用於建立自動化流程，提取所有發票資訊並儲存至資料表中。資料表還應讓財務團隊查看已付款及未付款的發票。

Power Platform 具備一個名為 Dataverse 的底層資料平台，可讓您為應用程式與方案儲存資料。Dataverse 提供一個低程式碼的資料平台來儲存應用程式資料。它是一項完全管理的服務，在 Microsoft 雲端安全儲存資料，且在您的 Power Platform 環境中配置。Dataverse 具備內建的資料治理功能，如資料分類、資料沿襲、細緻的存取控制等。您可以在[此處了解更多有關 Dataverse 的資訊](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko)。

為什麼我們的創業公司應該使用 Dataverse？Dataverse 中的標準與自訂資料表提供安全且基於雲端的資料儲存選項。資料表允許您儲存不同類型的資料，類似於您在單一 Excel 工作簿中使用多個工作表的方式。您可以使用資料表來儲存特定於組織或業務需求的資料。我們的創業公司使用 Dataverse 可獲得的部分優點包括但不限於：

- <strong>易於管理</strong>：元資料與資料皆儲存在雲端，無需擔心其儲存或管理細節，您可專注於構建應用程式與方案。

- <strong>安全性</strong>：Dataverse 提供安全且基於雲端的資料儲存選項。您可以利用基於角色的安全性，控制誰能存取資料表中的資料及存取方式。

- <strong>豐富的元資料</strong>：資料類型與關聯可直接在 Power Apps 中使用。

- <strong>邏輯與驗證</strong>：您可以使用業務規則、計算欄位及驗證規則來強制執行業務邏輯並維持資料準確性。

現在您已了解 Dataverse 是什麼以及為什麼應該使用，接下來我們來看如何使用 Copilot 在 Dataverse 中建立一個資料表，以滿足財務團隊的需求。

> <strong>注意</strong>：您將在下一節使用此資料表來建立一個自動化流程，該流程會提取所有發票資訊並儲存至資料表中。

若要使用 Copilot 在 Dataverse 建立資料表，請遵循以下步驟：

1. 前往 [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) 主頁。

2. 在左側導覽列選擇 **Tables**，然後點選 **Describe the new Table**。

![選擇新增資料表](../../../translated_images/zh-TW/describe-new-table.0792373eb757281e.webp)

1. 在 **Describe the new Table** 頁面，使用文字區描述您想建立的資料表。例如：**_我想建立一個用來儲存發票資訊的資料表_**。點擊 **Send** 按鈕，將提示發送給 AI Copilot。

![描述資料表](../../../translated_images/zh-TW/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. AI Copilot 將建議一個 Dataverse 資料表，包含您需要儲存所追踪資料的欄位及部分範例資料。您可以透過 AI Copilot 助理功能，經由對話式步驟自訂此資料表以符合需求。

![建議的 Dataverse 資料表](../../../translated_images/zh-TW/copilot-dataverse-table.b3bc936091324d9d.webp)

1. 財務團隊想寄電子郵件給供應商，讓其瞭解發票目前狀態。您可以使用 Copilot 為資料表新增一個欄位以儲存供應商電子郵件地址。例如，您可以使用以下提示新增欄位：**_我想新增一個欄位來儲存供應商電子郵件_**。點選 **Send** 按鈕將提示發送至 AI Copilot。

1. AI Copilot 將生成新欄位，您可以自訂欄位以符合需求。

1. 完成資料表後，點選 **Create** 按鈕建立資料表。

## Power Platform 中搭配 AI Builder 的 AI 模型

AI Builder 是 Power Platform 中的低程式碼 AI 功能，可讓您使用 AI 模型協助自動化流程及預測結果。利用 AI Builder，您可以將 AI 結合至連接 Dataverse 或多種雲端資料來源（如 SharePoint、OneDrive 或 Azure）的應用程式與流程中。

## 預建 AI 模型與自訂 AI 模型

AI Builder 提供兩類 AI 模型：預建 AI 模型與自訂 AI 模型。預建 AI 模型是由 Microsoft 訓練完成並在 Power Platform 中可直接使用的模型，幫助您在無需自行收集資料、建置、訓練及發佈模型的情況下，快速為應用程式與流程加入智慧。您可利用這些模型自動執行流程及預測結果。

Power Platform 中可用的部分預建 AI 模型包括：

- <strong>關鍵詞摘取</strong>：此模型用於從文字中摘取關鍵詞。
- <strong>語言偵測</strong>：此模型用於偵測文字的語言。
- <strong>情感分析</strong>：此模型判斷文字的正面、負面、中立或混合情緒。
- <strong>名片辨識器</strong>：此模型從名片中擷取資訊。
- <strong>文字辨識</strong>：此模型從影像中擷取文字。
- <strong>物件偵測</strong>：此模型偵測並擷取影像中的物件。
- <strong>文件處理</strong>：此模型從表單中擷取資料。
- <strong>發票處理</strong>：此模型擷取發票中的資訊。

自訂 AI 模型則允許您將自有模型帶入 AI Builder，使其能像任何 AI Builder 自訂模型一樣運作，並利用您自己的資料進行訓練。您可以在 Power Apps 與 Power Automate 中使用這些模型以自動化流程及預測結果。不過使用自有模型會有一定限制，請詳細閱讀這些[限制](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst)。

![AI builder 模型](../../../translated_images/zh-TW/ai-builder-models.8069423b84cfc47f.webp)

## 作業 #2 - 為我們的創業公司建置發票處理流程

財務團隊在處理發票方面遇到困難。他們使用試算表追蹤發票，但隨著發票數量增加，管理變得更加困難。他們請您建立利用 AI 協助處理發票的工作流程。此工作流程應能從發票中提取資訊，並將資料儲存在 Dataverse 資料表中，同時能寄送電子郵件給財務團隊，附上提取的資訊。

現在您已了解 AI Builder 及其用處，我們來看如何使用先前介紹的 AI Builder 中的「發票處理」AI 模型，來建置協助財務團隊處理發票的工作流程。

若要建立協助財務團隊使用 AI Builder 發票處理模型的工作流程，請依照下列步驟操作：

1. 前往 [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst) 主頁。

2. 使用主頁上的文字區描述您想建立的工作流程。例如：**_當收到新郵件時處理發票_**。點選 **Send** 按鈕，將提示發送至 AI Copilot。

   ![Copilot power automate](../../../translated_images/zh-TW/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. AI Copilot 會建議您執行所需的動作以完成自動化任務。您可以點擊 **Next** 按鈕瀏覽下一步。

4. 下一步，Power Automate 將提示您設置流程所需的連線。完成設定後，點擊 **Create flow** 按鈕建立流程。

5. AI Copilot 將產生一個流程，您之後可以自訂流程以符合需求。

6. 更新流程的觸發條件，並設定 **Folder** 為存放發票的資料夾。例如，可以設定為 **Inbox**。點選 **Show advanced options**，將 **Only with Attachments** 設為 **Yes**。此設定確保流程僅在資料夾收到附有附件的郵件時運作。

7. 從流程中移除以下動作：**HTML to text**、**Compose**、**Compose 2**、**Compose 3** 及 **Compose 4**，因為您不會使用它們。

8. 從流程中移除 **Condition** 動作，因為您不會使用它。流程應如以下截圖所示：

   ![power automate, 移除動作](../../../translated_images/zh-TW/powerautomate-remove-actions.7216392fe684ceba.webp)

9. 點擊 **Add an action** 按鈕並搜尋 **Dataverse**，選擇 **Add a new row** 動作。

10. 在 **Extract Information from invoices** 動作中，將 **Invoice File** 指定為郵件的 **Attachment Content**。此設定可確保流程從發票附件中提取資訊。

11. 選擇您先前建立的資料表。例如，您可以選擇 **Invoice Information** 資料表。選擇前一步驟的動態內容來填充以下欄位：

    - ID
    - 金額 Amount
    - 日期 Date
    - 名稱 Name
    - 狀態 Status - 將 **Status** 設為 **Pending**。
    - 供應商電子郵件 Supplier Email - 使用 **When a new email arrives** 觸發器中的 **From** 動態內容。

    ![power automate 新增列](../../../translated_images/zh-TW/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. 完成流程設定後，點選 **Save** 按鈕儲存流程。接著，您可以透過將附有發票的電子郵件寄到觸發器設定的資料夾來測試流程。

> <strong>你的作業</strong>：您剛建置的流程是良好的開始，現在請思考如何建立一個自動化流程，使財務團隊能在發票狀態變更時，自動寄電子郵件通知供應商更新其發票狀態。提示：流程必須在發票狀態變更時觸發執行。

## 在 Power Automate 中使用文字生成 AI 模型

AI Builder 中的 Create Text with GPT AI 模型能根據提示產生文字，且由 Microsoft Azure OpenAI 服務提供支援，有了此功能，您可以將 GPT（生成式預訓練轉換器）技術整合進您的應用程式及流程，構建多樣的自動流程及洞察力豐富的應用程式。

GPT 模型透過大量資料進行廣泛訓練，使其在收到提示時能產生接近人類語言的文字。結合工作流程自動化，GPT 等 AI 模型可用於簡化和自動化多種任務。

例如，您可以建立流程來自動產生多種用途的文字，如電子郵件草稿、產品描述等。您也可以利用此模型為聊天機器人和客服應用程式生成文字，幫助客服人員有效且迅速地回應客戶查詢。

![建立提示](../../../translated_images/zh-TW/create-prompt-gpt.69d429300c2e870a.webp)


若想了解如何在 Power Automate 中使用此 AI 模型，請參閱 [使用 AI Builder 和 GPT 增強智慧](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko) 模組。

## 很棒的工作！繼續您的學習

完成本課程後，請查看我們的 [生成式 AI 學習收藏](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升您的生成式 AI 知識！

想要自訂並從 Copilot 獲得更多效果？探索 [Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) —— 一個社群貢獻的指令、代理、技能與設定合集，幫助您充分發揮 GitHub Copilot 的功能。

請前往第 11 課，我們將探討如何[結合生成式 AI 與函式呼叫](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->