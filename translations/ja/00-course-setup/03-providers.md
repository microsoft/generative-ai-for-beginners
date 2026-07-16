# LLMプロバイダーの選択と設定 🔑

課題は、OpenAI、Azure、Hugging Faceなどのサポートされたサービスプロバイダーを通じて、1つ以上の大規模言語モデル（LLM）デプロイメントに対して動作するように設定することも<strong>可能です</strong>。これらは、正しい資格情報（APIキーやトークン）を使ってプログラムからアクセスできる_ホストされたエンドポイント_（API）を提供します。このコースでは、以下のプロバイダーについて説明します：

 - 多様なモデルを含むコアGPTシリーズを備えた[OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst)
 - エンタープライズ対応に重点を置いたOpenAIモデルのための[Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)
 - OpenAI、Meta、Mistral、Cohere、Microsoftなど、数百のモデルに単一エンドポイントとAPIキーでアクセス可能な[Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)（2026年7月末で廃止予定のGitHub Modelsを置き換え）
 - オープンソースモデルと推論サーバーのための[Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst)
 - クラウドサブスクリプション不要で完全にオフラインで自分のデバイスでモデルを実行したい場合のための[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)または[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)

<strong>これらの練習にはご自身のアカウントが必要です</strong>。課題は任意なので、興味に応じて一部、全て、または全く設定しなくても構いません。サインアップのガイドラインの一例：

| サインアップ | 費用 | APIキー | プレイグラウンド | コメント |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [料金](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [プロジェクトベース](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [ノーコード、ウェブ](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 複数モデル利用可能 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [料金](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDKクイックスタート](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [スタジオクイックスタート](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [アクセスには事前申請が必要](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [料金](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [プロジェクト概要ページ](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundryプレイグラウンド](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | 無料枠あり；多くのモデルプロバイダーに対して1つのエンドポイント＋キー |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [料金](https://huggingface.co/pricing) | [アクセストークン](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chatは対応モデルが限定的](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | 無料（お使いのデバイス上で動作） | 不要 | [ローカルCLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | 完全オフライン、OpenAI互換エンドポイント |
| | | | | |

下記の手順に従って、このリポジトリを異なるプロバイダーで使用するように_設定_してください。特定のプロバイダーを必要とする課題のファイル名には以下のタグが含まれます：

- `aoai` - Azure OpenAIエンドポイントとキーが必要
- `oai` - OpenAIエンドポイントとキーが必要
- `hf` - Hugging Faceトークンが必要
- `githubmodels` - Microsoft Foundry Modelsエンドポイントとキーが必要（GitHub Modelsは2026年7月末で廃止予定）

いずれか一つ、全て、または無しに設定可能です。関連する課題は資格情報が不足している場合にエラーになります。

## `.env`ファイルの作成

上記の案内を読み、該当プロバイダーにサインアップし、必要な認証資格情報（API_KEYまたはトークン）を取得していることを前提とします。Azure OpenAIの場合は、チャット完了のために少なくとも1つのGPTモデルがデプロイされたAzure OpenAIサービスの有効なデプロイメント（エンドポイント）があることを想定しています。

次に、<strong>ローカル環境変数</strong>を以下のように設定します：

1. ルートフォルダーにある `.env.copy` ファイルを確認してください。以下のような内容です：

   ```bash
   # OpenAIプロバイダー
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Microsoft FoundryのAzure OpenAI
   ## （Azure OpenAIサービスは現在Microsoft Foundryの一部です：https://ai.azure.com）
   AZURE_OPENAI_API_VERSION='2024-10-21' # デフォルトが設定されています！（現在の安定GA APIバージョン）
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundryのモデル（複数プロバイダーモデルカタログ、GitHubモデルに代わるもので、2026年7月末に終了します）
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. 下記コマンドでファイルを `.env` にコピーしてください。このファイルは_gitignore_されており秘密情報の保護に役立ちます。

   ```bash
   cp .env.copy .env
   ```

3. 次のセクションに従って、値（`=`の右側のプレースホルダー）を埋めてください。

4.（オプション）GitHub Codespacesを使う場合は、環境変数をこのリポジトリに関連付けた_Codespaces秘密_として保存できます。その場合はローカルの .env ファイルの設定は不要です。**ただし、この方法はGitHub Codespaces利用時のみ有効です。** Docker Desktopを使う場合は引き続き .env ファイルの設定が必要です。

## `.env` ファイルの内容を埋める

変数名を確認して、それが何を表すか理解してみましょう：

| 変数名  | 説明  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | プロファイルで設定するユーザーアクセストークン |
| OPENAI_API_KEY | 非Azure OpenAIエンドポイント用の認証キー |
| AZURE_OPENAI_API_KEY | Azure OpenAIサービス用の認証キー |
| AZURE_OPENAI_ENDPOINT | Azure OpenAIリソースのデプロイ済みエンドポイント |
| AZURE_OPENAI_DEPLOYMENT | _テキスト生成_モデルのデプロイメント名 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _テキスト埋め込み_モデルのデプロイメント名 |
| AZURE_INFERENCE_ENDPOINT | Microsoft Foundryプロジェクトのエンドポイント（Microsoft Foundry Models用） |
| AZURE_INFERENCE_CREDENTIAL | Microsoft FoundryプロジェクトのAPIキー |
| | |

注意：最後の2つのAzure OpenAI変数は、チャット完了（テキスト生成）とベクトル検索（埋め込み）のそれぞれのデフォルトモデルを反映しています。設定方法は該当課題で指示します。

## Azure OpenAI の設定：ポータルから

> **注意：** Azure OpenAIサービスは現在[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)の一部となっています。リソースやデプロイメントはAzureポータルに引き続き表示されますが、日常的なモデル管理（デプロイメント、プレイグラウンド、監視）は旧独立アプリの「Azure OpenAI Studio」ではなくFoundryポータルで行われます。

Azure OpenAIのエンドポイントとキーは[Azureポータル](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)で取得します。まずはそこへ移動しましょう。

1. [Azureポータル](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)にアクセス
1. サイドバーの<strong>キーとエンドポイント</strong>メニューをクリック
1. <strong>キーを表示</strong>をクリックすると、KEY 1、KEY 2、エンドポイントが表示されます
1. KEY 1の値をAZURE_OPENAI_API_KEYとして利用
1. エンドポイントの値をAZURE_OPENAI_ENDPOINTとして利用

次に、デプロイ済みの特定モデルのエンドポイントを取得します。

1. サイドバーの<strong>モデルデプロイメント</strong>をクリック
1. 表示ページで<strong>Microsoft Foundryポータルへ</strong>（またはリソースタイプにより<strong>デプロイメント管理</strong>）を選択

Microsoft Foundryポータルに移動し、以下の指示でその他の値を見つけます。

## Azure OpenAI の設定：Microsoft Foundryポータルから

1. 上記のようにリソースから[Microsoft Foundryポータル](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)に移動
1. サイドバーの<strong>デプロイメント</strong>タブをクリックし、現状のモデルを確認
1. 望むモデルが未デプロイなら、<strong>モデルのデプロイ</strong>から[モデルカタログ](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)よりデプロイ
1. _テキスト生成_モデルとしては<strong>gpt-4o-mini</strong>を推奨
1. _テキスト埋め込み_モデルとしては<strong>text-embedding-3-small</strong>を推奨

これで、使用している_デプロイメント名_にあわせて環境変数を更新します。通常は明示的に変更していなければモデル名と同じです。例として、

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**設定完了後は必ず .env ファイルを保存してください**。ファイルを閉じてノートブックの実行手順に戻れます。

## OpenAI の設定：プロフィールから

OpenAIのAPIキーは[OpenAIアカウント](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst)で確認可能です。キーをお持ちでなければアカウント登録しAPIキーを作成します。取得後は `.env` ファイルの `OPENAI_API_KEY` に設定してください。

## Hugging Face の設定：プロフィールから

Hugging Faceトークンはプロフィールの[アクセストークン](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst)内で取得できます。これらを公に投稿や共有しないでください。このプロジェクト用の新しいトークンを作成し、`.env` の `HUGGING_FACE_API_KEY` にコピーしてください。_注：技術的にはAPIキーではありませんが、認証に使うため命名規則を統一しています。_

## Microsoft Foundry Models の設定：ポータルから

> **注意：** GitHub Modelsは2026年7月末で廃止されます。Microsoft Foundry Modelsが直接の後継で、同様の無料トライヤル可能なモデルカタログやAzure AI Inference SDK / OpenAI SDK体験を提供します。

1. [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)にアクセスし、Foundryプロジェクトを作成または開きます。
1. [モデルカタログ](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)からモデルを選びデプロイ（例：`gpt-4o-mini`）。
1. プロジェクトの<strong>概要</strong>ページで<strong>エンドポイント</strong>と<strong>APIキー</strong>をコピー。
1. `.env` ファイルの `AZURE_INFERENCE_ENDPOINT` にエンドポイント、`AZURE_INFERENCE_CREDENTIAL` にAPIキーを設定。

## オフライン / ローカルプロバイダー

クラウドサブスクリプションを使いたくない場合は、対応するオープンモデルを直接ご自分のデバイスで実行できます：

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoftのオンデバイスランタイム。最適な実行プロバイダー（NPU、GPU、CPU）を自動選択し、OpenAI互換エンドポイントを公開するため、このコースのサンプルコードの大部分をほぼ変更なしで再利用可能。開始には[Foundry Localドキュメント](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst)を参照、もしくは `winget install Microsoft.FoundryLocal`（Windows）や `brew install microsoft/foundrylocal/foundrylocal`（macOS）でインストール。
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - Llama、Phi、Mistral、Gemmaなどのオープンモデルをローカルで実行するための人気のある代替手段。


両方のオプションを使った実践例は、[Lesson 19: Building with SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) を参照してください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->