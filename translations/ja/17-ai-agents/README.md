[![Open Source Models](../../../translated_images/17-lesson-banner.png?WT.d223296926e27d95f6b5a748e3f77ab9a1b669d4f9aebe608f926cbb44ea08a8.ja.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson17-gh?WT.mc_id=academic-105485-koreyst)

## はじめに

AIエージェントは、生成AIにおけるエキサイティングな進展を表しており、大規模言語モデル（LLM）がアシスタントからアクションを実行できるエージェントへと進化することを可能にします。AIエージェントフレームワークは、開発者がLLMにツールと状態管理へのアクセスを提供するアプリケーションを作成することを可能にします。これらのフレームワークは、LLMが計画したアクションをユーザーや開発者が監視できるように可視性を向上させ、エクスペリエンス管理を改善します。

このレッスンでは、以下の領域をカバーします：

- AIエージェントとは何かを理解する - AIエージェントとは正確には何なのか？
- 4つの異なるAIエージェントフレームワークを探る - それぞれのユニークな点は何か？
- これらのAIエージェントをさまざまなユースケースに適用する - いつAIエージェントを使用すべきか？

## 学習目標

このレッスンを受けた後、次のことができるようになります：

- AIエージェントが何であり、どのように使用できるかを説明する。
- 一部の人気のあるAIエージェントフレームワークの違いを理解し、それらがどのように異なるかを理解する。
- AIエージェントがどのように機能するかを理解し、それを使ってアプリケーションを構築する。

## AIエージェントとは？

AIエージェントは、生成AIの世界で非常にエキサイティングな分野です。この興奮とともに、用語やその適用に関する混乱が生じることがあります。AIエージェントと呼ばれるツールの大部分を含めてシンプルにするために、次の定義を使用します：

AIエージェントは、大規模言語モデル（LLM）が**状態**と**ツール**へのアクセスを提供することによりタスクを実行できるようにします。

![エージェントモデル](../../../translated_images/what-agent.png?WT.96b2eb171bd613cd0652fb5a2c1f488c80fde8d3405db76d780603041a415cb3.ja.mc_id=academic-105485-koreyst)

これらの用語を定義しましょう：

**大規模言語モデル** - このコース全体で言及されているモデルで、GPT-3.5、GPT-4、Llama-2などです。

**状態** - これは、LLMが作業しているコンテキストを指します。LLMは、過去のアクションと現在のコンテキストを使用して、次のアクションの意思決定を導きます。AIエージェントフレームワークは、開発者がこのコンテキストをより簡単に維持できるようにします。

**ツール** - ユーザーが要求したタスクを完了するために、LLMが計画したタスクを実行するためには、ツールへのアクセスが必要です。ツールの例としては、データベース、API、外部アプリケーション、さらには別のLLMなどがあります！

これらの定義が、これからの学習に役立つ基礎を提供することを願っています。次に、いくつかの異なるAIエージェントフレームワークを探ってみましょう：

## LangChainエージェント

[LangChainエージェント](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst)は、上記の定義の実装です。

**状態**を管理するために、`AgentExecutor`と呼ばれる組み込み関数を使用します。これは、定義された`agent`と利用可能な`tools`を受け入れます。

`Agent Executor`は、チャット履歴を保存して、チャットのコンテキストを提供します。

![Langchainエージェント](../../../translated_images/langchain-agents.png?WT.311575a86262a6e33490477b281688373d96e3392dbfe3094965470531a9f111.ja.mc_id=academic-105485-koreyst)

LangChainは、LLMがアクセスできるようにするためにアプリケーションにインポートできる[ツールのカタログ](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst)を提供しています。これらはコミュニティとLangChainチームによって作成されています。

これらのツールを定義して、`Agent Executor`に渡すことができます。

AIエージェントについて話すときに重要なもう一つの側面は可視性です。アプリケーション開発者にとって、LLMがどのツールを使用しているのか、なぜそれを使用しているのかを理解することが重要です。そのために、LangChainのチームはLangSmithを開発しました。

## AutoGen

次に紹介するAIエージェントフレームワークは[AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst)です。AutoGenの主な焦点は会話です。エージェントは**会話可能**であり、**カスタマイズ可能**です。

**会話可能 -** LLMは、タスクを完了するために別のLLMと会話を開始し、続けることができます。これは、`AssistantAgents`を作成し、特定のシステムメッセージを与えることで実行されます。

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**カスタマイズ可能** - エージェントはLLMとしてだけでなく、ユーザーやツールとしても定義できます。開発者として、タスクを完了するためにフィードバックを受け取る責任を持つ`UserProxyAgent`を定義できます。このフィードバックは、タスクの実行を続行するか停止するかのどちらかです。

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### 状態とツール

状態を変更し管理するために、アシスタントエージェントはPythonコードを生成してタスクを完了します。

プロセスの例を以下に示します：

![AutoGen](../../../translated_images/autogen.png?WT.45c9474fbd6109577f4363559f022554e796000ea2d677b80021b00e6ca0d869.ja.mc_id=academic-105485-koreyst)

#### システムメッセージで定義されたLLM

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

このシステムメッセージは、この特定のLLMに対してタスクに関連する機能を指示します。AutoGenでは、異なるシステムメッセージを持つ複数のAssistantAgentsを定義することができます。

#### ユーザーによってチャットが開始される

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

このuser_proxy（ヒューマン）からのメッセージが、エージェントが実行すべき可能性のある機能を探るプロセスを開始します。

#### 機能が実行される

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

最初のチャットが処理されると、エージェントは呼び出すべきツールを提案します。この場合、それは`get_weather`. Depending on your configuration, this function can be automatically executed and read by the Agent or can be executed based on user input.

You can find a list of [AutoGen code samples](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) to further explore how to get started building.

## Taskweaver

The next agent framework we will explore is [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). It is known as a "code-first" agent because instead of working strictly with `strings` , it can work with DataFrames in Python. This becomes extremely useful for data analysis and generation tasks. This can be things like creating graphs and charts or generating random numbers.

### State and Tools

To manage the state of the conversation, TaskWeaver uses the concept of a `Planner`. The `Planner` is a LLM that takes the request from the users and maps out the tasks that need to be completed to fulfill this request.

To complete the tasks the `Planner` is exposed to the collection of tools called `Plugins`と呼ばれる機能です。これらはPythonクラスまたは一般的なコードインタープリタである可能性があります。これらのプラグインは埋め込みとして保存され、LLMが正しいプラグインをよりよく検索できるようにします。

![Taskweaver](../../../translated_images/taskweaver.png?WT.c5d336793941a5af0d2489ad6d88a03f09557bd5ca68a954f1ddaa3d9f1ecc3b.ja.mc_id=academic-105485-koreyst)

異常検出を処理するプラグインの例を以下に示します：

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

コードは実行前に検証されます。Taskweaverでコンテキストを管理するためのもう一つの機能は、会話の`experience`. Experience allows for the context of a conversation to be stored over to the long term in a YAML file. This can be configured so that the LLM improves over time on certain tasks given that it is exposed to prior conversations.

## JARVIS

The last agent framework we will explore is [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file?WT.mc_id=academic-105485-koreyst). What makes JARVIS unique is that it uses an LLM to manage the `state`と`tools`が他のAIモデルであることです。各AIモデルは、物体検出、転写、画像キャプション生成などの特定のタスクを実行する専門モデルです。

![JARVIS](../../../translated_images/jarvis.png?WT.f12468c52a0c4848aeed51606a0e53a36eb38c65cc6c821597ea4dcaad03d1a3.ja.mc_id=academic-105485-koreyst)

LLMは、一般的な目的のモデルとして、ユーザーからのリクエストを受け取り、特定のタスクとタスクを完了するために必要な引数/データを識別します。

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

その後、LLMはリクエストを、JSONなどの専門AIモデルが解釈できる形式にフォーマットします。AIモデルがタスクに基づいて予測を返した後、LLMはその応答を受け取ります。

タスクを完了するために複数のモデルが必要な場合、それらのモデルからの応答を解釈し、それらを統合してユーザーへの応答を生成します。

以下の例は、ユーザーが画像内の物体の説明と数を要求したときの動作を示しています：

## 課題

AIエージェントの学習を続けるために、AutoGenを使用して以下を構築できます：

- 教育系スタートアップの異なる部門とのビジネス会議をシミュレートするアプリケーション。
- LLMに異なるペルソナと優先事項を理解させるシステムメッセージを作成し、ユーザーが新しい製品アイデアを提案できるようにする。
- LLMは、その後、各部門からのフォローアップ質問を生成し、提案や製品アイデアを洗練し、改善する。

## 学習はここで終わりません。旅を続けましょう

このレッスンを終えた後、[生成AI学習コレクション](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)をチェックして、生成AIの知識をさらに深めてください！

**免責事項**:  
この文書は機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご了承ください。元の言語での文書が権威ある情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤解釈について、当社は一切の責任を負いません。