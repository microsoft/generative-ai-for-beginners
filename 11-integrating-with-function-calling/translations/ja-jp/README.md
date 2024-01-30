# Function Calling との統合

![chapter image](../../images/11-lesson-banner.png?WT.mc_id=academic-105485-yoterada)

これまでのレッスンでかなり多くの内容を学びました。しかし、私たちはさらに成長できます。取り組むべき課題の一つは、一貫性のある回答フォーマットの作成です。回答フォーマットが一貫すると後続の処理はスムーズに進められます。また、他のデータ・ソースからデータを追加し、アプリケーションをさらに拡張できます。

上記の問題を、この章で取り扱います。

> **ビデオは近日公開予定**

## はじめに

このレッスンでは、下記の内容について説明します。

- 関数呼び出し (function calling) とは何か、その使用例について説明します。
- Azure OpenAI を使用して関数呼び出しを作成します。
- 関数呼び出しをアプリケーションに統合する方法を学びます。

## 学習目標

このレッスンを修了すると、下記を理解できます：

- 関数呼び出しを使う理由を説明できます。
- Azure Open AI Service を使用して関数呼び出しアプリを構築できます。
- アプリケーションのユースケースに適した効果的な関数呼び出しを設計できます。

## シナリオ：関数を用いてチャットボットを改善する

このレッスンでは、教育スタートアップで、利用者である学生がチャットボットを使用して技術コースを検索できる機能を実装したいと考えています。利用者のスキルレベル、現在の役割、興味のある技術に合わせたコースを推奨します。

このシナリオを実現するために、下記の機能やサービスを使用します：

- `Azure Open AI`：利用者にチャット体験を提供する為に使用します。
- `Microsoft Learn Catalog API`：利用者のリクエストに基づいて、コースを見つける支援を行います。
- `Function Calling`：利用者の問い合わせ内容を取得し、それを関数に送信し API リクエストを作成します。

手始めに、そもそもなぜ関数呼び出しを使用する必要があるのかを見てみましょう。

## 関数呼び出しを行う理由

関数呼び出しを行う前は、LLM からの回答は構造化されておらず、一貫性がありませんでした。開発者は、得られるさまざまな回答に対して処理できるように、複雑な検証コードを記述する必要がありました。例えば、利用者は「今のストックホルムの天気は何ですか？」のような回答を得られませんでした。これは、モデルの学習データをトレーニングした時間が制限されているためです。

「関数呼び出し」は、Azure Open AI Service の機能で、下記ができるようになります：

- **一貫した回答形式**：回答形式をより適切に制御できれば、回答結果を他のシステムに対してより簡単に統合できます。
- **外部データの利用**：アプリケーションは、チャットのコンテキスト(文脈)に、他の外部データ・ソースのデータを使用できます。

## シナリオを通じた問題の説明

> *Notebook.ipynb* というファイルを作成し、下記のコードをコピー＆ペーストしてください。仮に下記のシナリオを実行したい場合は、別のコードセルへの貼り付けをお勧めします。また、下記に記述する関数が、実際の問題に対処するための説明も行っているので、あわせて記述内容をご覧ください。

「一貫した回答フォーマットの取得」に関する問題の例を見てみましょう：

たとえば、学生データのデータベースを作成し、学生に対して適切なコースを提案できるようにしたいと考えています。下記に含まれているデータ中に、2 人の非常によく似た学生の説明があります。

1. Azure Open AI リソースへの接続を作成します。

```python
import os
import json
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()
    
client = AzureOpenAI(
api_key=os.environ['AZURE_OPENAI_KEY'],  # これもデフォルトで省略できます
api_version = "2023-07-01-preview"
)

deployment=os.environ['AZURE_OPENAI_DEPLOYMENT']
```

上記は、Azure Open AI への接続するための　Python　コードで、ここでは `api_version`、`api_key`を設定します。

1. `student_1_description`と`student_2_description`という変数を使用して、2人の学生の説明を記述します。

```python
student_1_description= f'''Emily Johnson は、Duke University の
コンピューターサイエンス専攻の2年生です。彼女の GPA は 3.7 です。
Emily は大学のチェス・クラブとディベート・チームの活動的なメンバーです。
彼女は卒業後、ソフトウェア・エンジニアリングのキャリアに進むのを望んでいます。
'''

student_2_description = f'''Michael Lee は、Stanford University の
コンピューターサイエンス専攻の2年生です。彼の GPA は 3.8 です。
Michael はプログラミングが得意と知られており、大学のロボティクス・クラブの
活動的なメンバーです。
彼は学習を終えた後、人工知能関連のキャリアに進むのを望んでいます。
'''
```

上記の学生の説明を LLM に送信し、データを解析します。このデータは後でアプリケーションで使用したり、API に送信したり、データベースへの保存ができます。

1. 関心のある情報を LLM に指示するため、2 つの同一プロンプトを作成します。

```python
prompt1 = f'''
   以下の情報を指定されたテキストから抽出し、それをJSONオブジェクトとして返してください：
    
   名前
   専攻
   学校
   成績
   クラブ
    
   情報を抽出するためのテキスト本文は以下の通りです：
   {student_1_description}
   '''
    
   prompt2 = f'''
   以下の情報を指定されたテキストから抽出し、それをJSONオブジェクトとして返してください：
    
   名前
   専攻
   学校
   成績
   クラブ
    
   情報を抽出するためのテキスト本文は以下の通りです：
   {student_2_description}
   '''
```

   上記のプロンプトは、LLM に情報を抽出し、応答を JSON 形式で返すように指示しています。

1. プロンプトと Azure Open AI の接続設定を行った後、`openai.ChatCompletion`を使用してプロンプトを LLM に送信します。プロンプトは `messages` 変数に格納し、ロールを `user` に設定します。これはチャット・ボットに対して、利用者からメッセージが書き込まれる様子を模倣するために記載しています。

   ```python
   # プロンプト1からの応答
   openai_response1 = client.chat.completions.create(
   model=deployment,
   messages = [{'role': 'user', 'content': prompt1}]
   )
   openai_response1.choices[0].message.content

   # プロンプト2からの応答
   openai_response2 = client.chat.completions.create(
   model=deployment,
   messages = [{'role': 'user', 'content': prompt2}]
   )
   openai_response2.choices[0].message.content
   ```

これで、両方のリクエストを LLM に送信し、受信した回答を `[openai_response1.choices[0].message.content]` 等で取得できます。

1. 最後に、`json.loads` を呼び出すと、応答を JSON 形式に変換できます：

```python
# 応答を JSON オブジェクトとして読み込む
json_response1 = json.loads(openai_response1.choices[0].message.content)
json_response1
```

応答 1：

```json
{
    "name": "Emily Johnson", 
    "major": "コンピューターサイエンス", 
    "school": "Duke University", 
    "grades": "3.7",
     "club": "チェス・クラブ" 
}
```

応答 2:

```json
{ 
    "name": "Michael Lee", 
    "major": "コンピューターサイエンス", 
    "school": "Stanford University", 
    "grades": "3.8 GPA", 
    "club": "ロボティクス・クラブ" 
}
```

プロンプトは同じで、説明も似ていますが、`grades` プロパティ値の出力形式が異なっています。例えばここでは、`3.7`や`3.8 GPA`のような形式で出力されています。

この結果は、記述したプロンプト内で非構造化のデータを取得し、結果として非構造化データを返しているからです。このデータを保存したり再利用するためには、どのような値を期待するかを把握できるように、構造化データの形式にする必要があります。

それでは上記のような、出力フォーマットの問題をどのように解決すればよいのでしょうか。結論から言うと、関数呼び出しを使用すれば、構造化データを確実に受け取れるようになります。関数呼び出しを使用する場合、LLM は実際には特定の関数を呼び出したり実行したりするわけではありません。代わりに、LLM は構造化した回答（データ）を作成します。その後、この構造化した回答（データ）を使用して、実行すべき関数を決めます。

![function flow](../../images/Function-Flow.png?WT.mc_id=academic-105485-yoterada)

そして関数からの返却値を取得し、それを LLM に送り返します。その後、LLM は自然言語を使用して利用者の問い合わせに対して回答します。

## 関数呼び出しを使用するユースケース

関数呼び出しを使用するとアプリが改善されるユースケースは多岐にわたります：

- **外部ツールの呼び出し**：チャット・ボットは利用者からの質問に回答するのが得意です。関数呼び出しを使用すると、チャット・ボットは利用者からのメッセージを使用して、特定のタスクを完了できます。例えば、学生はチャットボットに「この科目についてさらに支援が必要というメールを、教員に送信してください」と依頼できます。これにより、`send_email(to: string, body: string)`という関数呼び出しを行います。

- **API　またはデータベースクエリの作成**：利用者は、書式設定された問い合わせ、または API 要求に変換される自然言語を使用して、情報を検索できます。例えば、教師が「最後の課題を完了した生徒は誰ですか」と要求すると、`get_completed(student_name: string, assignment: int, current_status: string)`という関数を呼び出します。

- **構造化データの作成**：利用者は、テキストまたは CSV フォーマットのデータを取得し、LLM を使用して、そこから重要な情報を抽出できます。例えば学生は、和平合意に関するウィキペディアの記事を変換して、AI フラッシュカードを作成できます。これは、`get_important_facts(agreement_name: string, date_signed: string, parties_involved: list)`という関数を使用して行います。

## 最初の関数呼び出しの作成

関数呼び出しを作成するプロセスは、以下の3つの主要なステップから構成されています。

1. **呼び出し**：関数リストとユーザー・メッセージを用いて、Chat Completions API を呼び出します。  
2. **読み取り**：モデルからの回答を読み取り、アクションを実行します。つまり、関数を実行したり、API 呼び出しを行ったりします。  
3. **再呼び出し**：関数からの返却値を用いて、Chat Completions API を再度呼び出し、その情報を使用して利用者に対する回答を作成します。

![LLM Flow](../../images/LLM-Flow.png?WT.mc_id=academic-105485-yoterada)

### ステップ1 - メッセージの作成

最初のステップで、ユーザー・メッセージを作成します。これは、テキストの入力値を取得して動的に割り当てるか、もしくはここで直接値を割り当てできます。仮に Chat Completions API を初めて使用するの場合は、メッセージの `role` と `content` を定義してください。

`role` は `system`（ルールを作成）、`assistant`（モデル）、または `user`（エンドユーザー）のいずれかになります。関数呼び出しは、`user` として、質問を割り当てます。

```python
messages= [ {"role": "user", "content": "初心者の学生が Azure を学ぶための良い学習コースを見つけてください。"} ]
```

異なる役割を割り当てると、LLM は、システムが言っているのか、それとも利用者が言っているのかが明確になり、LLM は会話履歴を構築するのに役立ちます。

### ステップ2 - 関数の作成

次に、関数とその関数のパラメータを定義します。ここでは `search_courses` という1つの関数のみを使用しますが、複数の関数も作れます。

> **重要** : 関数は LLM のシステム・メッセージに含まれており、利用可能なトークンの数に含まれます。

下記は、関数を項目の配列として作成しています。各項目は関数であり、`name`、`description`、`parameters` というプロパティを持ちます。

```python
functions = [
   {
      "name":"search_courses",
      "description":"提供されたパラメータに基づいて検索インデックスからコースを取得します",
      "parameters":{
         "type":"object",
         "properties":{
            "role":{
               "type":"string",
               "description":"学習者の役割（例：開発者、データサイエンティスト、学生など）"
            },
            "product":{
               "type":"string",
               "description":"レッスンでカバーしている製品（例：Azure、Power BIなど）"
            },
            "level":{
               "type":"string",
               "description":"コースを受講する学習者のレベル（例：初心者、中級者、上級者）"
            }
         },
         "required":[
            "role"
         ]
      }
   }
]
```

下記に、関数について詳しく説明します。

- `name` - 呼び出したい関数名
- `description` - 関数がどのように動作するかの説明。ここは具体的で明確な説明の記述が必要
- `parameters` - モデルによって回答で生成する値とフォーマットのリスト。`parameters` 配列として構成し、次のプロパティを含む
   1. `type` - プロパティのデータ型
   1. `properties` - 回答に使用する特定の値のリスト
      1. `name` - フォーマットされた回答で使用するプロパティ名。例えば、`product`
      1. `type` - プロパティのデータ型。例えば、`string`
      1. `description` - 特定のプロパティの説明

また、オプションのプロパティとして `required`もあります。これは関数呼び出しが必須かを指定するプロパティです。

### ステップ3 - 関数呼び出しの実行

関数を定義した後、次に Chat Completion API の呼び出しにその関数を含める必要があります。これを行うには、リクエストに `functions` を追加します。この場合、`functions=functions`とします。

また、`function_call` を `auto` に設定するオプションもあります。これは、どの関数を呼び出すか、利用者からのメッセージに基づいて LLM に判断させ、自分で割り当てるのではなく、LLM に選択させます。

以下に、`ChatCompletion.create` を呼び出すコードを示します。`functions=functions` と `function_call="auto"` を設定し、LLM に提供する関数をいつ呼び出すかを選択させる方法に注目してください。

```python
response = client.chat.completions.create(model=deployment,
                                        messages=messages,
                                        functions=functions,
                                        function_call="auto")

print(response.choices[0].message)
```

返される回答は下記のようになります。

```json
{
  "role": "assistant",
  "function_call": {
    "name": "search_courses",
    "arguments": "{\n  \"role\": \"学生\",\n  \"product\": \"Azure\",\n  \"level\": \"初心者\"\n}"
  }
}
```

ここでは、`search_courses` 関数がどのように呼び出され、どのような引数で呼び出されたかを、JSON 形式で返された応答の `arguments` プロパティ・リストから確認できます。

結論として、LLM は Chat Completion 呼び出しの `messages` パラメータで提供した値からデータを抽出し、関数の引数に適合するデータを見つけられました。以下は、`messages` 値の内容です。

```python
messages= [ {"role": "user", "content": "初心者の学生が Azure を学ぶための良い学習コースを見つけてください。"} ]
```

ご覧の通り、`学生`、`Azure`、`初心者`は `messages` から抽出され、関数への入力として設定されました。このように関数を使用すると、プロンプトから情報を抽出するだけでなく、LLM に構造化データを提供し、再利用可能なデータを持てます。

次に、この機能をアプリでどのように使用できるかを確認します。

## アプリケーションの関数呼び出しとの統合

LLM からフォーマットされた応答を取得した後、これをアプリケーションに統合します。

### フローの管理

アプリケーションに統合するためには、下記の手順で行います。

1. まず、Open AI サービスを呼び出し、メッセージを `response_message` という変数に代入します。

```python
response_message = response.choices[0].message
```

1. 次に、Microsoft Learn のカタログ API を呼び出してコースの一覧を取得する関数を定義します。

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

`functions` 変数に記載した関数名にマップする、実際の Python 関数を作成する方法に注目してください。また、必要なデータを取得するために、実際に外部 API 呼び出しも行っています。ここでは、Microsoft Learn API に対してトレーニング モジュールを検索しています。

いま、`functions` 変数とそれに対応する Python 関数を作成しましたが、実際の Python 関数を呼び出すために、これら 2 つをマッピングした内容を、LLM に指示するにはどうすればよいでしょうか？

1. Python 関数を呼び出す必要があるかどうかを確認するためには、LLM からの応答を調べ、 `function_call` が含まれているかを確認し、指摘された関数を呼び出す必要があります。以下のようにしてチェックを行います。

```python
# モデルが関数を呼び出したいかどうかを確認
if response_message.function_call.name:
   print("Recommended Function call:")
   print(response_message.function_call.name)
   print()

   # 関数を呼び出す
   function_name = response_message.function_call.name

   available_functions = {
      "search_courses": search_courses,
   }
   function_to_call = available_functions[function_name]

   function_args = json.loads(response_message.function_call.arguments)
   function_response = function_to_call(**function_args)

   print("関数呼び出しの出力:")
   print(function_response)
   print(type(function_response))


   # アシスタントの応答と関数の応答をメッセージに追加
   messages.append( # アシスタントの応答をメッセージに追加
      {
         "role": response_message.role,
         "function_call": {
             "name": function_name,
             "arguments": response_message.function_call.arguments,
         },
         "content": None
      }
   )
   messages.append( # 関数の応答をメッセージに追加
      {
         "role": "function",
         "name": function_name,
         "content":function_response,
     }
)
```

下記の 3 行は、関数名と引数を抽出し、呼び出しを確認できます。

```python
function_to_call = available_functions[function_name]

function_args = json.loads(response_message.function_call.arguments)
function_response = function_to_call(**function_args)
```

下記は、コードを実行した出力結果です。

**Output**

```output
{
     "name": "search_courses",
     "arguments": "{\n  \"role\": \"学生\",\n  \"product\": \"Azure\",\n  \"level\": \"初心者\"\n}"
}

関数呼び出しの出力:
   [
      {
        "title": "暗号の概念についての説明",
        "url": "https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?WT.mc_id=api_CatalogApi"
      },
      {
        "title": "TensorFlow を使用したオーディオ分類の概要",
        "url": "https://learn.microsoft.com/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi"
      },
      {
        "title": "Azure Data Studio を使って Azure SQL Database でパフォーマンスに優れたデータ モデルを設計する",
        "url": "https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?WT.mc_id=api_CatalogApi"
      },
      {
        "title": "Azure 用の Microsoft クラウド導入フレームワークの概要",
        "url": "https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi"
      },
      {
        "title": "Rust 開発環境を設定する",
        "url": "https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi"
      }
    ]
   <class 'str'>
```

1. 次に、更新したメッセージ `messages` を LLM に送信して、JSON 形式の応答ではなく自然言語の応答を受け取ります。

```python
print("次のリクエストのメッセージ:")
print(messages)
print()

second_response = client.chat.completions.create(
   messages=messages,
   model=deployment,
   function_call="auto",
   functions=functions,
   temperature=0
   )  # 関数からの応答を元にした GPT から新しい応答を取得

print(second_response.choices[0].message)
```

**Output**

```output
{
     "role": "assistant",
     "content": "Azureを学ぶ初心者の学生向けにいくつかの良いコースを見つけました:\n\n
    1. [暗号の概念についての説明] (https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?WT.mc_id=api_CatalogApi)\n
    2. [TensorFlow を使用したオーディオ分類の概要](https://learn.microsoft.com/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi)\n
    3. [Azure Data Studio を使って Azure SQL Database でパフォーマンスに優れたデータ モデルを設計する](https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?WT.mc_id=api_CatalogApi)\n
    4. [Azure 用の Microsoft クラウド導入フレームワークの概要](https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi)\n
    5. [Rust 開発環境を設定する](https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi)\n\n
    リンクをクリックしてコースにアクセスできます。"
}
```

## 課題

Azure Open AI Function Calling の学習を続けるために、以下を試してみてください。

- 学習者がより多くのコースを見つける為に有効な関数のパラメーターを探して増やす。
- 学習者の母国語を聞くなど、学習者からより多くの情報を取得するための別の関数呼び出しを作成する。
- 関数呼び出しや API 呼び出しが、適切なコースを返さない場合のエラー処理を実装する。

ヒント: これらのデータを、どこでどのように利用できるかを確認するために、[Learn API リファレンス ドキュメント](https://learn.microsoft.com/training/support/catalog-api-developer-reference?WT.mc_id=academic-105485-yoterada) をご参照ください。

## お疲れ様でした!　学習を続ける

このレッスン修了後、[生成 AI 学習コレクション](https://aka.ms/genai-collection?WT.mc_id=academic-105485-yoterada) をチェックして、Generative AI の知識をレベルアップさせましょう。

Head over to Lesson 12 where we will look at how to !

次のレッスン 12 では、[AI アプリケーション用の UX デザイン](../../../12-designing-ux-for-ai-applications/translations/ja-jp/README.md?WT.mc_id=academic-105485-yoterada)について学びます！
