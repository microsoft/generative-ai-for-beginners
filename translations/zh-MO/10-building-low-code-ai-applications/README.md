# 建立低代碼 AI 應用程式

[![建立低代碼 AI 應用程式](../../../translated_images/zh-MO/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(點擊上方圖片觀看本課程影片)_

## 簡介

現在我們已經學會如何建立圖像生成應用程式，接下來讓我們談談低代碼。生成式 AI 可用於多個不同領域，包括低代碼，但究竟什麼是低代碼，我們又如何將 AI 添加到低代碼中呢？

傳統開發者和非開發者透過使用低代碼開發平台，建立應用程式和解決方案變得更容易。低代碼開發平台讓您能夠透過極少或完全不需撰寫程式碼來建立應用程式及解決方案。這是透過提供視覺化的開發環境，允許您拖放組件來建立應用程式和解決方案來實現的。這使您能更快速且以較少資源建立應用程式和解決方案。在本課程中，我們將深入探討如何使用低代碼，以及如何利用 Power Platform 以 AI 強化低代碼開發。

Power Platform 提供組織機會，讓他們的團隊能透過直觀的低代碼或無代碼環境建立自己的解決方案。這個環境有助簡化解決方案的建立流程。藉由 Power Platform，解決方案可以在數天或數星期內完成，而非數月或數年。Power Platform 包含五個主要產品：Power Apps、Power Automate、Power BI、Power Pages 和 Copilot Studio。

本課程涵蓋：

- Power Platform 生成式 AI 簡介
- Copilot 簡介以及如何使用
- 使用生成式 AI 在 Power Platform 中建立應用程式與工作流
- 使用 AI Builder 瞭解 Power Platform 中的 AI 模型
- 使用 Microsoft Copilot Studio 建立智能代理人

## 學習目標

到本課程結束時，您將能夠：

- 瞭解 Copilot 在 Power Platform 中的運作方式。

- 為我們的教育新創公司建立學生成績追蹤應用程式。

- 建立使用 AI 從發票中擷取資訊的發票處理流程。

- 套用使用 Create Text with GPT AI 模型的最佳實務。

- 瞭解 Microsoft Copilot Studio 是什麼，以及如何使用它建立智能代理人。

本課程中您將使用的工具與技術包括：

- **Power Apps**，用於建立學生成績追蹤應用程式，提供可低代碼建構應用程式以追蹤、管理及互動資料的開發環境。

- **Dataverse**，用於儲存學生成績追蹤應用程式的資料，Dataverse 提供低代碼資料平台來儲存應用程式資料。

- **Power Automate**，用於發票處理流程，讓您有低代碼的開發環境來建立自動化發票處理的工作流。

- **AI Builder**，用於發票處理的 AI 模型，您將使用預建的 AI 模型來處理我們新創公司的發票。

## Power Platform 中的生成式 AI

強化低代碼開發與應用，並結合生成式 AI 是 Power Platform 的關鍵重點。目標是讓每個人都能建立具 AI 功能的應用程式、網站和儀表板，並使用 AI 自動化流程，_無需任何資料科學專業知識_。這目標是透過在 Power Platform 的低代碼開發體驗中整合生成式 AI，以 Copilot 和 AI Builder 的形式達成。

### 這是如何運作的？

Copilot 是一位 AI 助手，能讓您透過一連串使用自然語言的對話步驟來描述需求，從而建立 Power Platform 解決方案。舉例來說，您可指示 AI 助手說明應用程式將使用哪些欄位，它便會建立應用程式及其底層資料模型，或者您也可以指定如何在 Power Automate 中設定工作流。

您也可以在您的應用程式畫面中使用由 Copilot 驅動的功能，讓使用者透過對話互動來發掘洞見。

AI Builder 是 Power Platform 中的低代碼 AI 功能，讓您能使用 AI 模型來協助自動化流程並預測結果。透過 AI Builder，您可以將 AI 加入連接 Dataverse 或各種雲端資料來源（如 SharePoint、OneDrive 或 Azure）的應用程式和流程中。

Copilot 可用於所有 Power Platform 產品：Power Apps、Power Automate、Power BI、Power Pages 與 Copilot Studio（前身為 Power Virtual Agents）。AI Builder 則可用於 Power Apps 與 Power Automate。在本課程中，我們將著重於如何使用 Power Apps 和 Power Automate 的 Copilot 與 AI Builder 來建構教育新創公司的解決方案。

### Power Apps 中的 Copilot

作為 Power Platform 的一部分，Power Apps 提供低代碼的開發環境，以建立應用程式用來追蹤、管理及互動資料。它是一套具有可擴充資料平台能力，並能連接雲端服務及本地資料的應用程式開發服務。Power Apps 允許您建立能在瀏覽器、平板及手機上運行的應用程式，並可與同事共享。Power Apps 以簡單介面引導使用者進入應用程式開發，使每位商業使用者或專業開發者皆能建置自訂應用程式。生成式 AI 透過 Copilot 進一步提升應用程式開發體驗。

Power Apps 中的 copilot AI 助手功能，讓您描述所需的應用程式類型及應用程式需追蹤、蒐集或顯示的資訊。Copilot 會根據您的描述生成回應式 Canvas 應用程式。您接著可以依需求自訂應用程式。AI Copilot 亦會生成並建議一個 Dataverse 表格，包含您需要的欄位以儲存欲追蹤的資料，並附帶一些範例資料。我們稍後會在本課程中探討 Dataverse 是什麼，以及如何在 Power Apps 中使用它。您還可以透過 AI Copilot 助手功能以對話步驟進行表格自訂。此功能可從 Power Apps 首頁輕鬆取得。

### Power Automate 中的 Copilot

作為 Power Platform 的一部分，Power Automate 讓使用者建立應用程式與服務之間的自動化工作流。它有助於自動化重複的商業流程，如通訊、資料蒐集與決策核准等。其簡單介面讓不同技術程度的使用者（從新手到資深開發者）都能自動化工作任務。生成式 AI 透過 Copilot 也增強了工作流開發體驗。

Power Automate 中的 copilot AI 助手功能，讓您描述所需的工作流類型，以及工作流需執行的動作。Copilot 會根據您的描述生成工作流。您接著可以依需求自訂工作流。AI Copilot 也會生成並建議您執行任務所需的動作。我們稍後會在本課程中探討工作流是什麼，以及如何在 Power Automate 中使用它們。您還可以透過 AI Copilot 助手功能以對話步驟來自訂動作。此功能可從 Power Automate 首頁輕鬆取得。

## 使用 Microsoft Copilot Studio 建立智能代理人

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst)（前身為 Power Virtual Agents）是 Power Platform 的低代碼成員，用於建立 **AI 代理人** —— 可以代表使用者回答問題、採取行動及自動化任務的對話式助理。就像 Power Platform 其他產品一樣，您在視覺化、以自然語言為先的體驗中建立這些代理人：您描述希望代理人做什麼，Copilot Studio 協助構建其指令、知識與行動。

對於我們的教育新創公司，您可以建立一個代理人，回答學生對課程的問題、檢查作業截止日期，甚至替老師發送電子郵件 —— 全部不需要撰寫程式碼。

以下是使 Copilot Studio 強大的部分最新功能：

- <strong>從您的知識產出生成式答案</strong>。您不必手工撰寫每段對話，而是可以連接 <strong>知識來源</strong> —— 公開網站、SharePoint、OneDrive、Dataverse、上傳檔案或透過連接器的企業資料 —— 代理人會從中生成有根據的答案。

- <strong>生成式調度</strong>。代理人不依賴僵硬的觸發語句，而是使用 AI 理解請求，並動態決定結合哪些知識、主題及行動來完成請求，包含串接多步驟程序。

- <strong>行動和連接器</strong>。代理人能 <em>執行</em> 任務，而不僅僅是聊天。您可為代理人配置由 1,500 多個預建 Power Platform 連接器、Power Automate 流程、自訂 REST API、提示語或 **模型上下文協議（MCP）** 伺服器支持的行動。

- <strong>自主代理人</strong>。代理人不限於聊天視窗回應。您可建立 <strong>自主代理人</strong>，當事件觸發（例如收到新電子郵件、Dataverse 新資料記錄或檔案被上傳時）可在背景行動完成任務。

- <strong>多代理人調度</strong>。代理人能調用其他代理人。Copilot Studio 代理人能轉接給其他代理人，或由其他代理人擴充，包括發布至 Microsoft 365 Copilot 的代理人，以及在 Microsoft Foundry 建立的代理人。

- <strong>模型選擇</strong>。除內建模型外，您可匯入 Microsoft Foundry 模型目錄中的模型，調整代理人的推理與回應方式。

- <strong>多處發布</strong>。建立完成後，代理人可發布至多個頻道 —— 包括 Microsoft Teams、Microsoft 365 Copilot、網站或自訂應用程式 —— 並由 Power Platform 管理體驗管理安全、認證及分析。

您可前往 [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst) 開始建立您的首個代理人，並在 [Microsoft Copilot Studio 文件](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst) 瞭解更多。

## 任務：使用 Copilot 為我們的新創公司管理學生作業及發票

我們的新創公司提供線上課程給學生。該新創公司快速成長，現在正在努力應付課程需求。新創公司聘請您作為 Power Platform 開發者，協助他們建立低代碼解決方案來管理學生作業與發票。他們的解決方案應能透過應用程式追蹤與管理學生作業，並透過工作流自動化發票處理流程。您被要求使用生成式 AI 來開發此解決方案。

使用 Copilot 初始階段，您可以使用 [Power Platform Copilot Prompt Library](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) 來開始使用提示語。此庫包含您用 Copilot 建立應用程式和流程時可用的一系列提示語。您也可利用庫中的提示語瞭解如何向 Copilot 描述您的需求。

### 為我們的新創公司建立學生成績追蹤應用程式

我們新創公司的教育者一直難以追蹤學生的作業。他們曾使用試算表來追蹤作業，但隨著學生數量增多，這變得難以管理。他們請您建立一個應用程式，協助他們追蹤與管理學生作業。應用程式應能讓他們新增作業、查看作業、更新作業及刪除作業。應用程式還應允許教育者和學生查看已評分和未評分的作業。

您將依照以下步驟，使用 Power Apps 的 Copilot 建立此應用程式：

1. 前往 [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) 首頁。

1. 使用首頁上的文字區描述您想要建立的應用程式。例如，**_我想建立一個用來追蹤與管理學生作業的應用程式_**。按下 <strong>傳送</strong> 按鈕，將提示發送給 AI Copilot。

![描述您想要建立的應用程式](../../../translated_images/zh-MO/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. AI Copilot 將建議一個 Dataverse 表格，包含您需要的欄位以儲存欲追蹤的資料以及一些範例資料。您可以透過 AI Copilot 助手功能，使用對話步驟來自訂表格，以符合您的需求。

   > <strong>重要</strong>：Dataverse 是 Power Platform 底層的資料平台。它是一個用於儲存應用程式資料的低代碼資料平台。Dataverse 為全託管服務，安全地在 Microsoft 雲端中儲存資料，且部署於您的 Power Platform 環境中。它具備內建資料治理能力，如資料分類、資料血緣、細粒度存取控制等。您可在[此處](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko)進一步瞭解 Dataverse。

   ![您新建立表格中的建議欄位](../../../translated_images/zh-MO/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. 教育者希望向提交作業的學生發送電子郵件，讓他們能隨時了解作業進度。您可以使用 Copilot 為表格新增一個欄位來儲存學生電子郵件。例如，您可以使用以下提示來新增欄位：**_我想新增一欄用來儲存學生電子郵件_**。按下 <strong>傳送</strong> 按鈕將提示發送給 AI Copilot。

![新增欄位](../../../translated_images/zh-MO/copilot-new-column.35e15ff21acaf274.webp)

1. AI Copilot 將生成新欄位，您隨後可以自訂該欄位以符合您的需求。


1. 完成表格後，按一下 **Create app** 按鈕以建立應用程式。

1. AI Copilot 會根據您的描述生成一個響應式 Canvas 應用程式。然後，您可以自訂應用程式以符合您的需求。

1. 對於教育工作者發送電郵給學生，您可以使用 Copilot 為應用程式新增一個畫面。例如，您可以使用以下提示來新增畫面：**_I want to add a screen to send emails to students_**。按一下 **Send** 按鈕向 AI Copilot 傳送提示。

![Adding a new screen via a prompt instruction](../../../translated_images/zh-MO/copilot-new-screen.2e0bef7132a17392.webp)

1. AI Copilot 會生成一個新畫面，然後您可以自訂該畫面以符合您的需求。

1. 完成應用程式後，按一下 **Save** 按鈕以儲存應用程式。

1. 要與教育工作者共享應用程式，按一下 **Share** 按鈕，再次按一下 **Share** 按鈕。然後，您可以透過輸入他們的電郵位址來共享應用程式。

> <strong>你的功課</strong>：你剛建立的應用程式是一個良好的起步，但仍然可以改進。透過電郵功能，教育工作者只能透過手動輸入電郵地址向學生發送電郵。你能否利用 Copilot 建立一個自動化，讓教育工作者在學生提交作業時自動發送電郵給學生？提示是透過適當的提示，你可以在 Power Automate 中使用 Copilot 來建立這個功能。

### 為我們的初創企業建立發票資訊表格

我們初創企業的財務團隊一直難以追蹤發票。他們一直使用電子表格來管理發票，但隨著發票數量增加，變得難以管理。他們請您建立一個表格，幫助他們儲存、追蹤和管理收到的發票資訊。該表格應用於建立自動化，從中提取所有發票資訊並儲存在表格中。表格還應該讓財務團隊能夠查看已付款和未付款的發票。

Power Platform 提供一個名為 Dataverse 的底層資料平台，讓您可以儲存應用程式和解決方案的資料。Dataverse 是一個低代碼資料平台，用於儲存應用程式的資料。這是一個完全託管服務，安全地將資料儲存在 Microsoft Cloud，並在您的 Power Platform 環境中配置。它內建資料治理功能，如資料分類、資料沿襲、細粒度存取控制等。您可以在此處了解更多[關於 Dataverse](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko)。

為什麼我們的初創企業應該使用 Dataverse？Dataverse 中的標準和自訂表格為您的資料提供安全且雲端的儲存選項。表格讓您儲存不同類型的資料，類似您在單一 Excel 工作簿中使用多個工作表。您可以使用表格儲存特定於組織或業務需求的資料。我們的初創企業使用 Dataverse 能享有的部分好處包括但不限於：

- <strong>易於管理</strong>：元資料和資料都儲存在雲端，因此您不必擔心它們如何儲存或管理，可以專注於構建應用程式和解決方案。

- <strong>安全</strong>：Dataverse 提供安全且基於雲端的資料儲存選項。您可以透過基於角色的安全性控管誰可以存取表格中的資料及其存取方式。

- <strong>豐富的元資料</strong>：資料類型和關聯可直接在 Power Apps 中使用。

- <strong>邏輯與驗證</strong>：您可以利用業務規則、計算欄位和驗證規則來執行業務邏輯並保持資料準確。

既然您已了解 Dataverse 是什麼以及為何應使用它，現在讓我們看看您可以如何使用 Copilot 在 Dataverse 中建立符合財務團隊需求的表格。

> <strong>注意</strong> ：您將在下一節中使用該表格來建立一個自動化，該自動化將提取所有發票資訊並儲存在表格中。

使用 Copilot 在 Dataverse 中建立表格，請按照以下步驟：

1. 前往 [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) 主畫面。

2. 在左側導覽欄中，選擇 **Tables**，然後點擊 **Describe the new Table**。

![Select new table](../../../translated_images/zh-MO/describe-new-table.0792373eb757281e.webp)

1. 在 **Describe the new Table** 頁面，使用文字區域描述您想要建立的表格。例如，**_I want to create a table to store invoice information_**。點擊 **Send** 按鈕以向 AI Copilot 傳送提示。

![Describe the table](../../../translated_images/zh-MO/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. AI Copilot 將建議一個 Dataverse 表格，帶有您需要用以追蹤資料的欄位及一些範例資料。您可以透過 AI Copilot 助手功能，以對話方式分步自訂該表格以符合您的需求。

![Suggested Dataverse table](../../../translated_images/zh-MO/copilot-dataverse-table.b3bc936091324d9d.webp)

1. 財務團隊希望發送電郵給供應商，更新他們發票的當前狀態。您可以使用 Copilot 為表格新增欄位來儲存供應商電郵。例如，您可以使用以下提示為表格新增欄位：**_I want to add a column to store supplier email_**。點擊 **Send** 按鈕向 AI Copilot 傳送提示。

1. AI Copilot 會生成一個新欄位，然後您可以自訂該欄位以符合您的需求。

1. 完成表格後，點擊 **Create** 按鈕建立表格。

## Power Platform 中的 AI 模型與 AI Builder

AI Builder 是 Power Platform 中一種低代碼的 AI 功能，讓您可以利用 AI 模型幫助您自動化流程並預測結果。透過 AI Builder，您可以將 AI 引入連接 Dataverse 或各種雲端資料來源（如 SharePoint、OneDrive 或 Azure）的應用程式和流程。

## 預建 AI 模型與自訂 AI 模型

AI Builder 提供兩種 AI 模型類型：預建 AI 模型和自訂 AI 模型。預建 AI 模型是由 Microsoft 訓練並內建於 Power Platform 中的現成模型。它們幫助您在無需收集資料、建立、訓練及發布自有模型的情況下，為應用程式和流程添加智能功能。您可以用這些模型自動化流程並預測結果。

Power Platform 中部分可用的預建 AI 模型包括：

- <strong>關鍵詞提取</strong>：從文字中提取關鍵詞。
- <strong>語言檢測</strong>：檢測文字的語言。
- <strong>情緒分析</strong>：檢測文字中的正面、負面、中立或混合情緒。
- <strong>名片辨識</strong>：從名片中提取資訊。
- <strong>文字識別</strong>：從圖片中提取文字。
- <strong>物件偵測</strong>：從圖片中偵測和提取物件。
- <strong>文件處理</strong>：從表單中提取資訊。
- <strong>發票處理</strong>：從發票中提取資訊。

使用自訂 AI 模型，您可以將自己的模型帶入 AI Builder，使其像任何 AI Builder 自訂模型一樣運作，並使用自己的資料進行訓練。您可以利用這些模型在 Power Apps 和 Power Automate 中自動化流程並預測結果。使用自有模型時會有一些限制，詳情請參閱這些[限制](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst)。

![AI builder models](../../../translated_images/zh-MO/ai-builder-models.8069423b84cfc47f.webp)

## 作業 #2 - 為我們的初創企業建立發票處理流程

財務團隊一直難以處理發票。他們一直使用電子表格來追蹤發票，但發票數量增加後，管理變得困難。他們請您建立一條工作流程，使用 AI 協助處理發票。該流程應能提取發票資訊並將資料儲存在 Dataverse 表格中。流程還應能向財務團隊發送包含提取資訊的電郵。

既然您已了解什麼是 AI Builder 以及為何要使用它，現在讓我們看看如何使用先前介紹的 AI Builder 中的發票處理 AI 模型來建立能幫助財務團隊處理發票的工作流程。

若要使用 AI Builder 中的發票處理 AI 模型建立協助財務團隊處理發票的工作流程，請按照以下步驟：

1. 前往 [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst) 主畫面。

2. 在主畫面的文字區域描述您想建立的流程。例如，**_Process an invoice when it arrives in my mailbox_**。點擊 **Send** 按鈕向 AI Copilot 傳送提示。

   ![Copilot power automate](../../../translated_images/zh-MO/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. AI Copilot 會建議您執行任務所需的動作。您可以按一下 **Next** 按鈕進行下一步。

4. 在下一步中，Power Automate 將提示您設定流程所需的連接。設定完成後，按一下 **Create flow** 按鈕建立流程。

5. AI Copilot 會生成流程，然後您可以自訂流程以符合需求。

6. 更新流程的觸發器，並將 **Folder** 設定為儲存發票的資料夾。例如，您可以設定為 **Inbox**。點選 **Show advanced options**，將 **Only with Attachments** 設定為 **Yes**。這確保流程只會在資料夾中收到帶附件的電郵時運行。

7. 從流程中移除以下動作：**HTML to text**、**Compose**、**Compose 2**、**Compose 3** 和 **Compose 4**，因為您不會使用它們。

8. 從流程中移除 **Condition** 動作，因為您不會使用它。畫面應該如以下截圖所示：

   ![power automate, remove actions](../../../translated_images/zh-MO/powerautomate-remove-actions.7216392fe684ceba.webp)

9. 點擊 **Add an action** 按鈕並搜尋 **Dataverse**。選擇 **Add a new row** 動作。

10. 在 **Extract Information from invoices** 動作中，將 **Invoice File** 更新為來自電郵的 **Attachment Content**。這可確保流程從發票附件中提取資訊。

11. 選擇您先前建立的 **Table**，例如選擇 **Invoice Information** 表格。從前一動作選擇動態內容以填入以下欄位：

    - ID
    - Amount
    - Date
    - Name
    - Status - 將 **Status** 設為 **Pending**。
    - Supplier Email - 使用來自 **When a new email arrives** 觸發器的 **From** 動態內容。

    ![power automate add row](../../../translated_images/zh-MO/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. 完成流程後，點擊 **Save** 按鈕以儲存流程。然後，您可以透過向觸發器指定的資料夾發送含發票的電郵測試流程。

> <strong>你的功課</strong>：你剛建立的流程是一個良好的起點，現在你需要思考如何建立一個自動化，讓我們的財務團隊能在發票狀態變更時自動向供應商發送電郵，更新他們該發票的最新狀態。提示：流程必須在發票狀態變更時執行。

## 在 Power Automate 中使用文字生成 AI 模型

AI Builder 中的 Create Text with GPT AI 模型讓您根據提示生成文字，該模型由 Microsoft Azure OpenAI 服務驅動。此功能讓您能將 GPT（生成式預訓練轉換器）技術整合至應用程式和流程中，以建立各種自動化流程和有洞察力的應用程式。

GPT 模型經過大量資料訓練，在提供提示時能產生與人類語言相似的文字。結合流程自動化，像 GPT 這樣的 AI 模型可用於簡化和自動化各種任務。

例如，您可以建立流程，自動生成各種用途的文字，如電郵草稿、產品描述等。您也可用於多種應用，如聊天機器人和客戶服務應用，幫助客服人員有效且高效回覆客戶詢問。

![create a prompt](../../../translated_images/zh-MO/create-prompt-gpt.69d429300c2e870a.webp)


若要學習如何在 Power Automate 中使用此 AI 模型，請瀏覽[使用 AI Builder 和 GPT 增強智能](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko) 模組。

## 做得好！繼續學習

完成本課程後，請查看我們的[生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)以持續提升您的生成式 AI 知識！

想自訂並更充分利用 Copilot 嗎？探索[Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) — 這是由社群貢獻的說明、代理、技能和設定集，幫助您充分發揮 GitHub Copilot 的功能。

前往第 11 課，我們將探討如何[將生成式 AI 與函式呼叫整合](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->