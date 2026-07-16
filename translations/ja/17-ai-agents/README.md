[![オープンソースモデル](../../../translated_images/ja/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## はじめに

AI エージェントは、生成AIのエキサイティングな進展を表しており、大規模言語モデル（LLM）がアシスタントから実際にアクションを起こせるエージェントへと進化することを可能にします。AIエージェントのフレームワークは、開発者がLLMにツールや状態管理へのアクセスを提供できるアプリケーションを作成することを可能にします。また、これらのフレームワークは可視性を高め、ユーザーや開発者がLLMによって計画されたアクションを監視できるようにし、体験管理を改善します。

本レッスンでは以下の内容をカバーします：

- AIエージェントとは何かを理解する - AIエージェントとは正確には何か？
- 5つの異なるAIエージェントフレームワークを探る - それぞれの特徴は？
- これらのAIエージェントを異なるユースケースに適用する - いつAIエージェントを使うべきか？

## 学習目標

本レッスンを修了後には、以下のことができるようになります：

- AIエージェントとは何か、どのように使われるか説明できる。
- 人気のあるAIエージェントフレームワークの違いと特徴を理解する。
- AIエージェントの機能を理解し、それを使ったアプリケーションを構築できる。

## AIエージェントとは？

AIエージェントは生成AIの世界で非常にエキサイティングな分野です。この興奮には用語やその応用の混乱が伴う場合があります。多くのAIエージェントと呼ばれるツールを包括的かつシンプルに扱うために、以下の定義を使用します：

AIエージェントは大規模言語モデル（LLM）に<strong>状態</strong>と<strong>ツール</strong>へのアクセスを与えることでタスクを実行できるようにします。

![エージェントモデル](../../../translated_images/ja/what-agent.21f2893bdfd01e6a.webp)

これらの用語を定義しましょう：

<strong>大規模言語モデル</strong> - 本コースで言及されるモデルで、GPT-5、GPT-4o、Llama 3.3などがあります。

<strong>状態</strong> - LLMが作業しているコンテキストを指します。LLMは過去のアクションの文脈と現在の文脈を利用し、その後のアクションの意思決定を導きます。AIエージェントフレームワークはこのコンテキストの管理を容易にします。

<strong>ツール</strong> - ユーザーが要求しLLMが計画したタスクを完了するために、LLMはツールへアクセスする必要があります。ツールの例としてはデータベース、API、外部アプリケーション、または別のLLMも含まれます。

これらの定義は、これからの実装を理解する上で基礎となるでしょう。さまざまなAIエージェントフレームワークを見てみましょう：

## LangChain エージェント

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) は上記定義の実装例です。

<strong>状態</strong> を管理するために、組み込みの `AgentExecutor` 関数を使用します。これは定義された `agent` と利用可能な `tools` を受け入れます。

`AgentExecutor` はチャット履歴も保存し、チャットの文脈を提供します。

![Langchain エージェント](../../../translated_images/ja/langchain-agents.edcc55b5d5c43716.webp)

LangChainはLLMがアクセスできるコミュニティおよびLangChainチームによる[ツールカタログ](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst)を提供しています。

これらのツールを定義し、`AgentExecutor` に渡すことができます。

可視性はAIエージェントを語る上で重要な要素です。開発者がLLMがどのツールをなぜ使っているのか理解することが重要です。そのためLangChainチームはLangSmithを開発しました。

## AutoGen

次に紹介するAIエージェントフレームワークは [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst)です。AutoGenの主な焦点は会話であり、エージェントは<strong>対話可能</strong>かつ<strong>カスタマイズ可能</strong>です。

<strong>対話可能</strong> - LLMは別のLLMと会話を開始し、継続してタスクを完了できます。これは `AssistantAgents` を作成し、特定のシステムメッセージを与えることで実現します。

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

<strong>カスタマイズ可能</strong> - エージェントはLLMだけでなくユーザーやツールとして定義できます。開発者は `UserProxyAgent` を定義し、ユーザーからのフィードバックを受け取りタスクの進行を継続または停止させることができます。

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### 状態とツール

状態を変更し管理するために、Assistant AgentはPythonコードを生成してタスクを完遂します。

プロセスの例は以下の通りです：

![AutoGen](../../../translated_images/ja/autogen.dee9a25a45fde584.webp)

#### システムメッセージで定義されたLLM

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

このシステムメッセージは特定のLLMにどの機能がタスクに関係しているかを指示します。AutoGenでは異なるシステムメッセージを持つ複数のAssistantAgentsを定義できます。

#### ユーザーによってチャットが開始される

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

user_proxy（人間）からのこのメッセージがAgentが実行すべき関数を探るプロセスを始めます。

#### 関数が実行される

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

初期チャットの処理後、Agentは呼び出す提案ツールを送信します。ここでは `get_weather` という関数です。設定によってはこの関数は自動で実行されAgentに読み取られるか、ユーザーの入力に基づき実行されます。

[AutoGenのコードサンプル](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst)も参照し、構築方法をさらに探索できます。

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) はMicrosoftのオープンソースSDKで、<strong>Python</strong>と<strong>.NET</strong>の両方でAIエージェントやマルチエージェントシステムの構築が可能です。これは以前のMicrosoftプロジェクトの強みである<strong>Semantic Kernel</strong>の企業向け機能と<strong>AutoGen</strong>のマルチエージェントオーケストレーションを統合した単一のサポートされるフレームワークです。新しいエージェントプロジェクトを始めるなら、AutoGenの推奨後継とされています。

フレームワークは単一の<strong>チャットエージェント</strong>から複雑な<strong>マルチエージェントワークフロー</strong>まで拡張可能で、Microsoft Foundry、Azure OpenAI、OpenAIと直接統合します。OpenTelemetryによる組み込みの可観測性も提供し、エージェントの動作を正確に追跡できます。

### 状態とツール

<strong>状態</strong> - フレームワークは<strong>スレッド</strong>を通じて会話のコンテキストを管理します。エージェントはメッセージ履歴（ユーザーの要求、ツール呼び出し、それらの結果）を追跡し、各ターンが前のターンに基づいて積み重なります。スレッドは永続化可能で、会話を中断して再開できます。

<strong>ツール</strong> - エージェントにツールを渡すには、通常のPython関数を渡します。型アノテーションされたパラメーターは自動的にスキーマに変換され、モデルがどのようにいつ呼び出すかを知ることができます（関数呼び出し）。また、Model Context Protocol (MCP) サーバーやコードインタプリタのようなホストされたツールもサポートしています。

カスタムツールを持つ単一エージェントの例はこちらです：

```python
import asyncio
from typing import Annotated

from pydantic import Field
from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient


def get_weather(
    location: Annotated[str, Field(description="The location to get the weather for.")],
) -> str:
    """Get the weather for a given location."""
    return f"The weather in {location} is sunny with a high of 22°C."


async def main():
    agent = Agent(
        client=OpenAIChatClient(),
        instructions="You are a helpful assistant that can answer weather questions.",
        tools=[get_weather],
    )

    response = await agent.run("What's the weather in Amsterdam?")
    print(response)


asyncio.run(main())
```

Microsoft FoundryでAzure OpenAIに接続するには、エンドポイントと資格情報をクライアントに渡します：

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### マルチエージェントワークフロー

フレームワークの真価は複数のエージェントをオーケストレーションする点にあります。例として、エージェントを順番に実行し（それぞれがコンテキストを次に渡す）、または複数のエージェントを並列で実行して結果を集約できます。

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# エージェントを順番に実行し、会話のコンテキストをチェーンに沿って渡す
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# エージェントに並列でファンアウトし、それから彼らの応答を集約する
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

フレームワークのインストールと開始方法：

```bash
pip install agent-framework-core
# オプションの統合
pip install agent-framework-openai       # OpenAI と Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

[Microsoft Agent Frameworkリポジトリ](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst)や[公式ドキュメント](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst)も参照してください。

## Taskweaver

次に紹介するエージェントフレームワークは [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst) です。これは "コードファースト" エージェントとして知られており、`strings` だけでなくPythonのDataFrameを扱えるため、データ分析や生成タスクに非常に有用です。グラフやチャートの作成、乱数生成などが可能です。

### 状態とツール

会話の状態管理には `Planner` の概念を使います。`Planner` はユーザーのリクエストを受け取り、そのリクエストを満たすために完了すべきタスクをマッピングするLLMです。

タスクを完了するために、`Planner` は `Plugins` と呼ばれるツールのコレクションにアクセスします。これはPythonクラスや一般的なコードインタプリタです。プラグインは埋め込み（embeddings）として保存され、LLMが正しいプラグインをより良く検索できるようにしています。

![Taskweaver](../../../translated_images/ja/taskweaver.da8559999267715a.webp)

異常検知を扱うプラグインの例：

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

コードは実行前に検証されます。Taskweaverでコンテキスト管理を助けるもう一つの機能が `experience` です。Experienceは会話のコンテキストをYAMLファイルに長期保存でき、設定によりLLMは過去の会話を通じて特定タスクを時間とともに改善します。

## JARVIS

最後に紹介するエージェントフレームワークは [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst) です。特徴として、JARVISは会話の `state` を管理するのにLLMを使用し、`tools` は他のAIモデルになっています。各AIモデルは物体検出、文字起こし、画像キャプション付けなど特定のタスクを専門的に実行します。

![JARVIS](../../../translated_images/ja/jarvis.762ddbadbd1a3a33.webp)

汎用モデルであるLLMはユーザーのリクエストを受け取り、特定のタスクと完遂に必要な引数／データを特定します。

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

次に、LLMはAIモデルが解釈可能な形式（JSONなど）でリクエストを整形します。AIモデルがタスクに基づく予測を返したら、そのレスポンスをLLMが受け取ります。

複数のモデルがタスク完遂に必要な場合は、それらのレスポンスを解釈しまとめてユーザーへの応答を生成します。

下記の例は、ユーザーが画像内の物体の説明と数を要求した場合の動作例です：

## 課題

AIエージェントの学習を続けるためMicrosoft Agent Frameworkで構築できます：

- 教育系スタートアップの各部門とのビジネス会議をシミュレートするアプリケーション。
- LLMが異なるペルソナや優先事項を理解するためのシステムメッセージを作成し、ユーザーが新商品のアイデアを提案できるようにする。
- その後、LLMが各部門からのフォローアップ質問を生成し、提案や製品アイデアを改良・精緻化する。

## 学びはここで終わりません、学習を続けましょう

本レッスンを修了したら、[Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)をチェックして生成AIの知識レベルをさらに高めましょう！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->