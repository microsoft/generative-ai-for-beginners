# 與函式呼叫整合

[![與函式呼叫整合](../../images/11-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson11-gh?WT.mc_id=academic-105485-koreyst)

你在前面的課程中已經學到了不少。然而，我們還可以進一步改進。我們可以解決的一些問題是如何獲得更一致的回應格式，以便更容易處理後續的回應。此外，我們可能想要添加來自其他來源的數據，以進一步豐富我們的應用程式。

上述提到的問題是本章要解決的。

## 簡介

本課程將涵蓋:

- 解釋什麼是函式呼叫及其使用案例。
- 使用 Azure OpenAI 建立函式呼叫。
- 如何將函式呼叫整合到應用程式中。

## 學習目標

完成此課程後，您將能夠：

- 解釋使用函式呼叫的目的。
- 使用 Azure OpenAI Service 設定函式呼叫。
- 為您的應用程式設計有效的函式呼叫用例。

## 情境: 使用函式改進我們的聊天機器人

這節課中，我們想為我們的教育創業公司建構一個功能，允許用戶使用聊天機器人來查找技術課程。我們將推薦適合他們技能水平、當前角色和感興趣技術的課程。

要完成此情境，我們將使用以下組合:

- `Azure OpenAI` 用來建立使用者的聊天體驗。
- `Microsoft Learn Catalog API` 幫助使用者根據請求找到課程。
- `Function Calling` 接收使用者的查詢並將其發送到函式以進行 API 請求。

要開始，我們先來看看為什麼我們一開始會想要使用函式呼叫:

## 為什麼要呼叫函式

在呼叫函式之前，來自 LLM 的回應是非結構化且不一致的。開發者需要撰寫複雜的驗證程式碼，以確保他們能夠處理每個回應的變化。使用者無法得到像 "斯德哥爾摩目前的天氣如何？" 這樣的答案。這是因為模型僅限於訓練數據的時間。

函式呼叫是 Azure OpenAI 服務的一項功能，用於克服以下限制:

- **一致的回應格式**. 如果我們能更好地控制回應格式，我們可以更容易地將回應整合到其他系統中。
- **外部資料**. 能夠在聊天情境中使用應用程式其他來源的資料。

## 通過情境說明問題

> 我們建議你使用[內建筆記本](/11-integrating-with-function-calling/Lesson11-FunctionCalling.ipynb)如果你想要執行以下場景。你也可以只是閱讀，因為我們正在嘗試說明一個函式可以幫助解決的問題。

讓我們看看說明回應格式問題的範例:

假設我們想要建立一個學生資料的資料庫，以便我們可以向他們推薦合適的課程。以下是兩個學生的描述，它們所包含的資料非常相似。

1. 建立與我們的 Azure OpenAI 資源的連接:

   ```python
   import os
   import json
   from openai import AzureOpenAI
   from dotenv import load_dotenv
   load_dotenv()

   client = AzureOpenAI(
   api_key=os.environ['AZURE_OPENAI_KEY'],  # 這也是預設值，可以省略
   api_version = "2023-07-01-preview"
   )

   deployment=os.environ['AZURE_OPENAI_DEPLOYMENT']
   ```

   下面是一些 Python 程式碼，用於配置我們與 Azure OpenAI 的連接，我們設置了 `api_type`、`api_base`、`api_version` 和 `api_key`。

1. 使用變數 `student_1_description` 和 `student_2_description` 建立兩個學生描述。

   ```python
   student_1_description="Emily Johnson 是杜克大學計算機科學專業的二年級學生。她的 GPA 為 3.7。Emily 是大學國際象棋俱樂部和辯論隊的活躍成員。她希望畢業後從事軟體工程師的職業。"

   student_2_description = "Michael Lee 是史丹佛大學計算機科學專業的二年級學生。他的 GPA 為 3.8。Michael 以他的編程技能聞名，是大學機器人俱樂部的活躍成員。他希望在完成學業後從事人工智慧領域的職業。"
   ```

   我們希望將上述學生描述發送到 LLM 以解析數據。這些數據可以在我們的應用中使用，並發送到 API 或存儲在資料庫中。

1. 讓我們建立兩個相同的提示，其中我們指示 LLM 我們感興趣的資訊:

   ```python
   prompt1 = f'''
   請從給定的文本中提取以下資訊並以 JSON 物件返回:

   name
   major
   school
   grades
   club

   這是要從中提取資訊的文本正文:
   {student_1_description}
   '''

   prompt2 = f'''
   請從給定的文本中提取以下資訊並以 JSON 物件返回:

   name
   major
   school
   grades
   club

   這是要從中提取資訊的文本正文:
   {student_2_description}
   '''
   ```

   上述提示指示 LLM 提取資訊並以 JSON 格式返回響應。

1. 在設定提示和連接到 Azure OpenAI 之後，我們現在將使用 `openai.ChatCompletion` 將提示發送給 LLM。我們將提示存儲在 `messages` 變數中，並將角色分配給 `user`。這是為了模擬用戶向聊天機器人寫消息。

   ```python
   # 提示一的回應
   openai_response1 = client.chat.completions.create(
   model=deployment,
   messages = [{'role': 'user', 'content': prompt1}]
   )
   openai_response1.choices[0].message.content

   # 提示二的回應
   openai_response2 = client.chat.completions.create(
   model=deployment,
   messages = [{'role': 'user', 'content': prompt2}]
   )
   openai_response2.choices[0].message.content
   ```

現在我們可以將兩個請求都發送到 LLM，並通過找到它來檢查我們收到的回應，如此 `openai_response1['choices'][0]['message']['content']`。

1. Lastly, we can convert the response to JSON format by calling `json.loads`:

   ```python
   # Loading the response as a JSON object
   json_response1 = json.loads(openai_response1.choices[0].message.content)
   json_response1
   ```

   Response 1:

   ```json
   {
     "name": "Emily Johnson",
     "major": "computer science",
     "school": "Duke University",
     "grades": "3.7",
     "club": "Chess Club"
   }
   ```

   Response 2:

   ```json
   {
     "name": "Michael Lee",
     "major": "computer science",
     "school": "Stanford University",
     "grades": "3.8 GPA",
     "club": "Robotics Club"
   }
   ```

   Even though the prompts are the same and the descriptions are similar, we see values of the `Grades` property formatted differently as we can sometimes get the format `3.7` or `3.7 GPA` for example.

   This result is because the LLM takes unstructured data in the form of the written prompt and returns also unstructured data. We need to have a structured format so that we know what to expect when storing or using this data

那麼我們如何解決格式問題呢？通過使用函式呼叫，我們可以確保收到結構化的資料。當使用函式呼叫時，LLM 實際上並不會呼叫或執行任何函式。相反，我們為 LLM 建立一個結構來遵循其回應。然後我們使用這些結構化的回應來知道在我們的應用程式中要執行什麼函式。

![函式流程](../../images/Function-Flow.png?WT.mc_id=academic-105485-koreyst)

我們可以將從函式返回的內容傳送回 LLM。然後 LLM 將使用自然語言回應來回答使用者的查詢。

## 使用函式呼叫的用例

在許多不同的使用案例中，函式呼叫可以改善您的應用程式，例如:

- **呼叫外部工具**。聊天機器人非常擅長回答用戶的問題。通過使用函式呼叫，聊天機器人可以使用用戶的消息來完成某些任務。例如，一個學生可以要求聊天機器人「發送電子郵件給我的導師，說我需要更多的幫助」。這可以通過呼叫 `send_email(to: string, body: string)` 函式來實現。

- **建立 API 或資料庫查詢**。用戶可以使用自然語言查找資訊，這些自然語言會轉換成格式化的查詢或 API 請求。這方面的一個範例可能是一位老師請求「誰是完成了最後一個作業的學生」，這可以呼叫一個名為 `get_completed(student_name: string, assignment: int, current_status: string)` 的函式。

- **建立結構化資料**。用戶可以使用 LLM 從一段文字或 CSV 中提取重要資訊。例如，一個學生可以將一篇關於和平協議的維基百科文章轉換成 AI 閃卡。這可以通過使用一個名為 `get_important_facts(agreement_name: string, date_signed: string, parties_involved: list)` 的函式來完成。

## 建立您的第一個函式呼叫

建立函式呼叫的過程包括三個主要步驟:

1. **呼叫** Chat Completions API 並附上你的函式列表和使用者訊息。
2. **閱讀**模型的回應以執行動作，即執行函式或 API 呼叫。
3. **再次呼叫** Chat Completions API 並使用你的函式回應中的資訊來建立對使用者的回應。

![LLM Flow](../../images/LLM-Flow.png?WT.mc_id=academic-105485-koreyst)

### Step 1 - 建立訊息

第一步是建立使用者訊息。這可以透過取得文字輸入的值來動態分配，或者你可以在這裡分配一個值。如果這是你第一次使用 Chat Completions API，我們需要定義訊息的`role`和`content`。

`role` 可以是 `system` (建立規則), `assistant` (模型) 或 `user` (最終使用者)。對於函式呼叫, 我們將其指定為 `user` 和一個範例問題。

```python
messages= [ {"role": "user", "content": "幫我找一個適合初學者學習 Azure 的好課程。"} ]
```

通過分配不同的角色，可以明確地讓LLM知道是系統在說話還是用戶在說話，這有助於建立LLM可以基於此進行建構的對話歷史。

### 步驟 2 - 建立函式

接下來，我們將定義一個函式和該函式的參數。我們將只使用一個名為 `search_courses` 的函式，但你可以建立多個函式。

> **重要** : 函式包含在系統訊息中給 LLM，並將包含在您可用的 token 數量中。

以下，我們將函式建立為一個項目陣列。每個項目都是一個函式，並具有屬性 `name`、`description` 和 `parameters`:

```python
函式 = [
   {
      "name":"search_courses",
      "description":"根據提供的參數從搜尋索引中檢索課程",
      "parameters":{
         "type":"物件",
         "properties":{
            "role":{
               "type":"string",
               "description":"學習者的角色 (例如: 開發者、數據科學家、學生等)"
            },
            "product":{
               "type":"string",
               "description":"課程涵蓋的產品 (例如: Azure、Power BI 等)"
            },
            "level":{
               "type":"string",
               "description":"學習者在參加課程前的經驗水平 (例如: 初學者、中級、高級)"
            }
         },
         "required":[
            "role"
         ]
      }
   }
]
```

讓我們更詳細地描述每個函式實例:

- `name` - 我們希望呼叫的函式名稱。
- `description` - 這是函式如何運作的描述。這裡重要的是要具體和清晰。
- `parameters` - 你希望模型在其回應中產生的值和格式的列表。參數陣列由項目組成，其中項目具有以下屬性:
  1.  `type` - 屬性將存儲的資料類型。
  1.  `properties` - 模型將用於其回應的具體值列表
      1. `name` - 鍵是模型在其格式化回應中使用的屬性名稱，例如, `product`。
      1. `type` - 此屬性的資料類型，例如, `string`。
      1. `description` - 具體屬性的描述。

還有一個可選屬性 `required` - 函式呼叫完成所需的必要屬性。

### 步驟 3 - 進行函式呼叫

在定義了一個函式之後，我們現在需要將它包含在呼叫 Chat Completion API 中。我們通過在請求中添加 `functions` 來完成這個操作。在這種情況下 `functions=functions`。

還有一個選項可以將 `function_call` 設定為 `auto`。這意味著我們將讓 LLM 根據使用者訊息決定應該呼叫哪個函式，而不是由我們自己分配。

以下是一些程式碼，我們呼叫 `ChatCompletion.create`，注意我們如何設定 `functions=functions` 和 `function_call="auto"`，從而讓 LLM 自行選擇何時呼叫我們提供的函式:

```python
response = client.chat.completions.create(model=deployment,
                                        messages=messages,
                                        functions=函式,
                                        function_call="auto")

print(response.choices[0].message)
```

回應現在看起來是這樣的:

```json
{
  "角色": "助手",
  "函式呼叫": {
    "名稱": "search_courses",
    "參數": "{\n  \"角色\": \"學生\",\n  \"產品\": \"Azure\",\n  \"等級\": \"初學者\"\n}"
  }
}
```

在這裡我們可以看到函式 `search_courses` 是如何被呼叫的，以及在 JSON 回應中的 `arguments` 屬性中列出的參數。

結論是 LLM 能夠找到數據來適應函式的參數，因為它是從提供給聊天完成呼叫的 `messages` 參數中的值中提取的。以下是 `messages` 值的提醒:

```python
messages= [ {"role": "user", "content": "幫我找一個適合初學者學習 Azure 的好課程。"} ]
```

如你所見，`student`、`Azure` 和 `beginner` 從 `messages` 中提取並設置為函式的輸入。這樣使用函式是一個從提示中提取資訊的好方法，同時也為 LLM 提供結構並具有可重用的功能。

接下來，我們需要看看如何在我們的應用程式中使用這個。

## 將函式呼叫整合到應用程式中

在我們測試過來自 LLM 的格式化回應後，現在我們可以將其整合到應用程式中。

### 管理流程

要將這個整合到我們的應用程式中，讓我們採取以下步驟:

1. 首先，讓我們呼叫 Open AI 服務並將訊息儲存在一個名為 `response_message` 的變數中。

   ```python
   response_message = response.choices[0].message
   ```

1. 現在我們將定義一個函式來呼叫 Microsoft Learn API 以獲取課程列表:

   ```python
   import requests

   def search_courses(role, product, level):
     url = "https://learn.microsoft.com/api/catalog/"
     params = {
        "role": role,
        "product": product,
        "level": level
     }
     response = requests.get(url, params=params)
     modules = response.json()["modules"]
     results = []
     for module in modules[:5]:
        title = module["title"]
        url = module["url"]
        results.append({"title": title, "url": url})
     return str(results)
   ```

   注意我們現在如何建立一個實際的 Python 函式，並將其對應到 `functions` 變數中引入的函式名稱。我們還進行了真正的外部 API 呼叫來獲取所需的資料。在這個例子中，我們使用 Microsoft Learn API 來搜尋訓練模組。

好的，所以我們建立了 `函式` 變數和相應的 Python 函式，我們如何告訴 LLM 如何將這兩者映射在一起，以便呼叫我們的 Python 函式？

1. 要查看我們是否需要呼叫一個 Python 函式，我們需要查看 LLM 的回應，看看 `function_call` 是否是其中的一部分並呼叫指出的函式。以下是您可以進行檢查的方式：

   ```python
   # 檢查模型是否想要呼叫函式
   if response_message.function_call.name:
    print("推薦的函式呼叫:")
    print(response_message.function_call.name)
    print()

    # 呼叫函式。
    function_name = response_message.function_call.name

    available_functions = {
            "search_courses": search_courses,
    }
    function_to_call = available_functions[function_name]

    function_args = json.loads(response_message.function_call.arguments)
    function_response = function_to_call(**function_args)

    print("函式呼叫的輸出:")
    print(function_response)
    print(type(function_response))


    # 將助手回應和函式回應添加到訊息中
    messages.append( # 將助手回應添加到訊息中
        {
            "role": response_message.role,
            "function_call": {
                "name": function_name,
                "arguments": response_message.function_call.arguments,
            },
            "content": None
        }
    )
    messages.append( # 將函式回應添加到訊息中
        {
            "role": "function",
            "name": function_name,
            "content":function_response,
        }
    )
   ```

   這三行確保我們提取函式名稱、參數並進行呼叫：

   ```python
   function_to_call = available_functions[function_name]

   function_args = json.loads(response_message.function_call.arguments)
   function_response = function_to_call(**function_args)
   ```

   以下是執行我們程式碼的輸出：

   **輸出**

   ```推薦的函式呼叫:
   {
     "name": "search_courses",
     "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
   }

   函式呼叫的輸出:
   [{'title': 'Describe concepts of cryptography', 'url': 'https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?WT.mc_id=api_CatalogApi'}, {'title': 'Introduction to audio classification with TensorFlow', 'url': 'https://learn.microsoft.com/en-us/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi'}, {'title': 'Design a Performant Data Model in Azure SQL Database with Azure Data Studio', 'url': 'https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?WT.mc_id=api_CatalogApi'}, {'title': 'Getting started with the Microsoft Cloud Adoption Framework for Azure', 'url': 'https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi'}, {'title': 'Set up the Rust development environment', 'url': 'https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi'}]
   <class 'str'>
   ```

1. 現在我們將更新的訊息 `messages` 發送給 LLM，以便我們可以收到自然語言回應，而不是 API JSON 格式的回應。

   ```python
   print("下一個請求中的訊息:")
   print(messages)
   print()

   second_response = client.chat.completions.create(
      messages=messages,
      model=deployment,
      function_call="auto",
      functions=functions,
      temperature=0
         )  # 從 GPT 獲取新的回應，它可以看到函式回應


   print(second_response.choices[0].message)
   ```

   **輸出**

   ```python
   {
     "role": "assistant",
     "content": "我找到了一些適合初學者學習 Azure 的好課程:\n\n1. [Describe concepts of cryptography](https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?WT.mc_id=api_CatalogApi)\n2. [Introduction to audio classification with TensorFlow](https://learn.microsoft.com/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi)\n3. [Design a Performant Data Model in Azure SQL Database with Azure Data Studio](https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?WT.mc_id=api_CatalogApi)\n4. [Getting started with the Microsoft Cloud Adoption Framework for Azure](https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi)\n5. [Set up the Rust development environment](https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi)\n\n你可以點擊連結來訪問這些課程。"
   }

   ```

## 作業

為了繼續學習 Azure OpenAI 函式呼叫，你可以建構:

- 更多函式的參數可能幫助學習者找到更多課程。
- 建立另一個函式呼叫，從學習者那裡獲取更多資訊，例如他們的母語
- 當函式呼叫和/或 API 呼叫未返回任何合適的課程時，建立錯誤處理

提示: 請參考[Learn API 參考文件](https://learn.microsoft.com/training/support/catalog-api-developer-reference?WT.mc_id=academic-105485-koreyst)頁面，了解這些資料的可用方式和位置。

## 很棒的工作！繼續這段旅程

完成本課程後，請查看我們的[生成式 AI 學習集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)以繼續提升您的生成式 AI 知識！

前往第12課，我們將探討如何[為 AI 應用設計 UX](../../../12-designing-ux-for-ai-applications/translations/tw/README.md?WT.mc_id=academic-105485-koreyst)！

