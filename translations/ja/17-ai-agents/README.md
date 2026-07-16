[![オープンソースモデル](../../../translated_images/ja/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## はじめに

AIエージェントは、生成AIのエキサイティングな進展を示しており、大規模言語モデル（LLM）が単なるアシスタントから、実際にアクションを起こすことができるエージェントへと進化することを可能にします。AIエージェントフレームワークは、開発者がLLMにツールや状態管理へのアクセスを提供するアプリケーションを作成できるようにします。これらのフレームワークはさらに可視性を高め、ユーザーや開発者がLLMの計画したアクションを監視できるようにして、体験管理を改善します。

本レッスンでは以下の領域をカバーします：

- AIエージェントとは何かを理解する - AIエージェントとは具体的に何か？
- 5つの異なるAIエージェントフレームワークの探求 - それぞれの独自性は？
- さまざまなユースケースへのAIエージェントの応用 - いつAIエージェントを使うべきか？

## 学習目標

このレッスンを終了すると、以下ができるようになります：

- AIエージェントとは何か、そしてどのように使えるかを説明できる。
- 人気のあるいくつかのAIエージェントフレームワークの違いを理解できる。
- AIエージェントの機能を理解し、それを使ってアプリケーションを構築できる。

## AIエージェントとは何か？

AIエージェントは生成AIの分野で非常にエキサイティングな領域です。この興奮とともに用語や適用の混乱も生じることがあります。シンプルにし、AIエージェントと呼ばれるほとんどのツールを包括できるように、次の定義を使います：

AIエージェントは、大規模言語モデル（LLM）に<strong>状態</strong>と<strong>ツール</strong>へのアクセスを与えることで、タスクを実行できるようにします。

![Agent Model](../../../translated_images/ja/what-agent.21f2893bdfd01e6a.webp)

これらの用語を定義しましょう：

<strong>大規模言語モデル</strong> - 本コースで言及されるモデルで、GPT-3.5、GPT-4、Llama-2などが含まれます。

<strong>状態</strong> - これはLLMが動作するコンテキストを指します。LLMは過去のアクションと現在のコンテキストを利用して、その後の行動の意思決定を導きます。AIエージェントフレームワークはこのコンテキストの管理を開発者がしやすくします。

<strong>ツール</strong> - ユーザーが要求し、LLMが計画したタスクを完遂するために、LLMはツールへのアクセスが必要です。例としてはデータベース、API、外部アプリケーション、あるいは別のLLMなどがあります！

これらの定義が、今後実装例を見る際の良い基盤となることを願っています。いくつかの異なるAIエージェントフレームワークを探ってみましょう：

## LangChain Agents

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst)は前述の定義を実装したものです。

<strong>状態</strong>を管理するために、`AgentExecutor`という組み込み関数を使います。これは定義された`agent`と利用可能な`tools`を受け入れます。

`AgentExecutor`はチャット履歴も保存し、チャットのコンテキストを提供します。

![Langchain Agents](../../../translated_images/ja/langchain-agents.edcc55b5d5c43716.webp)

LangChainは、LLMがアクセスできるツールをコミュニティやLangChainチームが作成した[ツールカタログ](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst)として提供しています。

これらのツールを定義し、`AgentExecutor`に渡すことができます。

AIエージェントにおいてもう一つ重要な側面は可視性です。アプリケーション開発者にとって、LLMがどのツールをなぜ使っているのか理解することが重要です。そのためLangChainチームはLangSmithを開発しました。

## AutoGen

次に紹介するAIエージェントフレームワークは[AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst)です。AutoGenは会話に注力しています。エージェントは<strong>会話可能</strong>で<strong>カスタマイズ可能</strong>です。

<strong>会話可能</strong> - LLMは他のLLMと会話を開始し継続して、タスクを完遂できます。これは`AssistantAgents`を作成し特定のシステムメッセージを与えることで行います。

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

<strong>カスタマイズ可能</strong> - エージェントはLLMだけでなくユーザーやツールとしても定義できます。開発者はフィードバックを得るためにユーザーとやり取りする`UserProxyAgent`を定義可能です。このフィードバックはタスクの継続または中止に使われます。

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### 状態とツール

状態を変更・管理するために、アシスタントエージェントはタスクを完了するPythonコードを生成します。

こちらはそのプロセスの例です：

![AutoGen](../../../translated_images/ja/autogen.dee9a25a45fde584.webp)

#### システムメッセージで定義されたLLM

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

このシステムメッセージは特定のLLMにどの関数がタスクに関連するか指示します。AutoGenでは、異なるシステムメッセージで複数のAssistantAgentsを定義できます。

#### ユーザーによってチャットが開始される

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

ユーザープロキシ（人間）からのこのメッセージが、エージェントが実行すべき関数を探り始めるきっかけになります。

#### 関数実行

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

初期チャット処理後、エージェントは呼び出すべきツールを提案します。この例では`get_weather`という関数です。設定によって、この関数は自動で実行され結果をエージェントが受け取るか、またはユーザー入力に応じて実行されます。

[AutoGenのコードサンプル](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst)でさらに開始方法を探ることができます。

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst)はMicrosoftのオープンソースSDKで、<strong>Python</strong>と<strong>.NET</strong>でAIエージェントやマルチエージェントシステムを構築できます。Microsoftの２つのプロジェクトの強みを融合しており、<strong>Semantic Kernel</strong>の企業向け機能と<strong>AutoGen</strong>のマルチエージェント調整機能をひとつにまとめた、今新しいエージェントプロジェクトを始める際の推奨フレームワークです。

このフレームワークは、単一の<strong>チャットエージェント</strong>から複雑な<strong>マルチエージェントワークフロー</strong>までスケールし、Microsoft Foundry、Azure OpenAI、OpenAIと直接統合します。OpenTelemetryによる組み込みの可観測性も提供し、エージェントの動作をトレースできます。

### 状態とツール

<strong>状態</strong> - フレームワークは<strong>スレッド</strong>を通じて対話コンテキストを管理します。エージェントはメッセージ履歴（ユーザーリクエスト、ツール呼び出し、結果）を記録し、それに基づいてターンごとに進めます。スレッドは永続化可能で、会話を一時中断し再開できます。

<strong>ツール</strong> - エージェントにツールを与えるには、単純なPython関数を渡します。型注釈付きのパラメーターはスキーマに変換され、モデルはいつどのように呼び出すかを把握します（関数呼び出し）。フレームワークはModel Context Protocol (MCP)サーバーやコードインタープリターのようなホストされたツールもサポートします。

こちらはカスタムツールを備えた単一エージェントの例です：

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

Microsoft FoundryのAzure OpenAIに接続する場合は、エンドポイントと認証情報をクライアントに渡します：

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### マルチエージェントワークフロー

フレームワークが真に優れているのは複数のエージェントの調整です。例えば、エージェントを順次実行（それぞれコンテキストを次に渡す）したり、複数のエージェントを並列に動かして結果を集約したりできます：

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# 会話のコンテキストをチェーンに沿って渡しながら、エージェントを順番に実行する
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# エージェントに並列で処理を分散し、その応答を集約する
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

インストールして始めるには：

```bash
pip install agent-framework-core
# オプションの統合
pip install agent-framework-openai       # OpenAI と Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

詳しくは[Microsoft Agent Frameworkリポジトリ](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst)と[公式ドキュメント](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst)を参照してください。

## Taskweaver

次に探るエージェントフレームワークは[Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst)です。これは「コードファースト」エージェントとして知られています。単に`文字列`を扱うだけでなく、PythonのDataFrameを扱えるため、データ解析や生成タスクに非常に役立ちます。これはグラフやチャートの作成、乱数生成などが含まれます。

### 状態とツール

会話の状態管理にTaskWeaverは`Planner`の概念を使います。`Planner`はユーザーからのリクエストを受け、完了すべきタスクをマッピングするLLMです。

タスクを完了するために、`Planner`は`Plugins`と呼ばれるツール群にアクセスします。これらはPythonクラスや一般的なコードインタープリターであり、プラグインは埋め込みとして保存され、LLMが適切なプラグインを検索しやすくなっています。

![Taskweaver](../../../translated_images/ja/taskweaver.da8559999267715a.webp)

こちらは異常検知を扱うプラグインの例です：

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

コードは実行前に検証されます。Taskweaverのコンテキスト管理のもうひとつの特徴は`experience`です。Experienceは会話のコンテキストを長期にわたりYAMLファイルに保存でき、これによりLLMが過去の会話を活かして時間をかけて特定のタスクで改善できます。

## JARVIS

最後に探るエージェントフレームワークは[JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst)です。JARVISの特徴は、LLMが会話の`状態`を管理し、`ツール`が他のAIモデルである点です。各AIモデルは物体検出、文字起こし、画像キャプション生成など特定のタスクを専門に実行します。

![JARVIS](../../../translated_images/ja/jarvis.762ddbadbd1a3a33.webp)

汎用モデルであるLLMはユーザーからのリクエストを受け取り、特定のタスクと、タスク完了に必要な引数やデータを特定します。

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLMは専門AIモデルが解釈可能な形式（JSONなど）でリクエストをフォーマットします。AIモデルがタスクに基づく予測を返すと、LLMはその応答を受け取ります。

タスクに複数モデルが必要な場合、LLMはそれらモデルの応答も解釈し、それらを組み合わせてユーザーへの応答を生成します。

以下の例は、ユーザーが画像内の物体の説明と数を要求したときの動作例です：

## 課題

AIエージェントの学習を続けるために、Microsoft Agent Frameworkで次のようなアプリケーションを作成できます：

- 教育系スタートアップの異なる部門が集うビジネスミーティングをシミュレートするアプリケーション
- LLMに異なるペルソナや優先事項を理解させるシステムメッセージを作成し、ユーザーが新しい製品アイデアを提案できるようにする
- 各部門からのフォローアップ質問をLLMが生成し、ピッチや製品アイデアを洗練・改善させる

## 学習はここで終わりません、旅を続けましょう

このレッスンを終えたら、[生成AI学習コレクション](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)をチェックして、生成AIの知識をさらにレベルアップしましょう！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->