# LLMプロバイダーの選択と設定 🔑

課題は、OpenAI、Azure、Hugging Faceなどのサポートされているサービスプロバイダーを通じて、1つ以上の大規模言語モデル（LLM）展開で動作するように設定することも<strong>できます</strong>。これらは、適切な認証情報（APIキーまたはトークン）を使ってプログラムからアクセスできる_ホスト型エンドポイント_（API）を提供します。このコースでは、以下のプロバイダーについて説明します：

 - コアのGPTシリーズを含む多様なモデルを提供する[OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst)。
 - エンタープライズ対応に重点を置いたOpenAIモデル向けの[Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)。
 - OpenAI、Meta、Mistral、Cohere、Microsoftなど数百のモデルに単一のエンドポイントとAPIキーでアクセス可能な[Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)（2026年7月末に廃止されるGitHub Modelsの代替）。
 - オープンソースモデルと推論サーバーのための[Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst)。
 - クラウドサブスクリプション不要で完全にオフラインでモデルを自分のデバイス上で実行したい場合は、[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)または[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)。

**これらの演習では、ご自身のアカウントを使用する必要があります**。課題は任意なので、ご興味に合わせて1つ、すべて、または全くセットアップしないことも可能です。サインアップのガイダンスは以下のとおりです：

| サインアップ | 費用 | APIキー | プレイグラウンド | コメント |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [価格](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [プロジェクトベース](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [ノーコード、ウェブ](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 複数モデル利用可能 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [価格](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDKクイックスタート](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [スタジオクイックスタート](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [利用に先立って申請が必要](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [価格](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [プロジェクト概要ページ](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundryプレイグラウンド](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | 無料枠あり；多くのモデルプロバイダーに単一のエンドポイント＋キーでアクセス可能 |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [価格](https://huggingface.co/pricing) | [アクセス・トークン](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chatはモデル数が限定的](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | 無料（ご自身のデバイスで動作） | 不要 | [ローカルCLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | 完全オフライン、OpenAI互換エンドポイント |
| | | | | |

以下の手順に従い、このリポジトリを異なるプロバイダーで使用するように_設定_してください。特定のプロバイダーを必要とする課題には、ファイル名に以下のタグが含まれます：

- `aoai` - Azure OpenAIのエンドポイントとキーが必要
- `oai` - OpenAIのエンドポイントとキーが必要
- `hf` - Hugging Faceのトークンが必要
- `githubmodels` - Microsoft Foundry Modelsのエンドポイントとキーが必要（GitHub Modelsは2026年7月末に廃止予定）

1つ、全くなし、またはすべてのプロバイダーを設定可能です。関連する課題は認証情報が不足している場合は単にエラーになります。

## `.env` ファイルの作成

ここまでの案内を読み、該当プロバイダーに登録し、必要な認証情報（API_KEYやトークン）を取得済みであることを前提とします。Azure OpenAIの場合は、少なくとも1つのGPTモデルがチャット完了用に展開されたAzure OpenAIサービス（エンドポイント）が正常にデプロイされていると仮定します。

次に、<strong>ローカル環境変数</strong>を次のように設定します：

1. ルートフォルダーにある `.env.copy` ファイルを確認してください。内容は次のようなものです：

   ```bash
   # OpenAI プロバイダー
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Microsoft Foundry の Azure OpenAI
   ## （Azure OpenAI サービスは現在 Microsoft Foundry の一部です：https://ai.azure.com）
   AZURE_OPENAI_API_VERSION='2024-10-21' # デフォルトが設定されました！（現在の安定版 GA API バージョン）
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry モデル（マルチプロバイダーモデルカタログ、GitHub モデルの代替、2026年7月末で終了）
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. 下記コマンドでファイルを `.env` にコピーしてください。このファイルは _gitignore_ に登録されており、秘密情報の安全が保たれます。

   ```bash
   cp .env.copy .env
   ```

3. 次のセクションで説明するように、値を入力してください（`=` の右側のプレースホルダーを置き換えます）。

4. （オプション）GitHub Codespacesを使う場合、このリポジトリに関連付けられた_Codespaces secrets_として環境変数を保存することも可能です。その場合、ローカルで `.env` ファイルを設定する必要はありません。**ただし、このオプションはGitHub Codespaces使用時のみ機能します。** Docker Desktopを使う場合は引き続き `.env` ファイルの設定が必要です。

## `.env` ファイルの内容を入力する

変数名が何を表すか、簡単に見てみましょう：

| 変数名 | 説明 |
| :--- | :--- |
| HUGGING_FACE_API_KEY | ユーザープロファイルで設定するアクセストークンです |
| OPENAI_API_KEY | 非Azure OpenAIエンドポイント用の認証キーです |
| AZURE_OPENAI_API_KEY | Azure OpenAIサービス用の認証キーです |
| AZURE_OPENAI_ENDPOINT | Azure OpenAIリソースのデプロイ済みエンドポイントです |
| AZURE_OPENAI_DEPLOYMENT | _テキスト生成_モデルのデプロイメント名です |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _テキスト埋め込み_モデルのデプロイメント名です |
| AZURE_INFERENCE_ENDPOINT | Microsoft Foundryプロジェクトのエンドポイントで、Foundry Modelsに使用します |
| AZURE_INFERENCE_CREDENTIAL | Microsoft FoundryプロジェクトのAPIキーです |
| | |

注：最後の2つのAzure OpenAI変数はそれぞれチャット完了用（テキスト生成）とベクトル検索用（埋め込み）のデフォルトモデルを示します。設定手順は該当課題で説明されます。

## Azure OpenAIの設定：ポータルから

> **注意：**Azure OpenAIサービスは現在[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)の一部です。リソースとデプロイメントは依然としてAzureポータルに表示されますが、モデル管理（デプロイ、プレイグラウンド、監視）は旧Azure OpenAI StudioではなくFoundryポータルで行われます。

Azure OpenAIのエンドポイントとキーは[Azureポータル](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)で確認できます。では、そこから始めましょう。

1. [Azureポータル](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)にアクセスします
1. サイドバー（左メニュー）の<strong>キーとエンドポイント</strong>をクリックします
1. <strong>キーを表示</strong>をクリックすると、KEY 1、KEY 2およびエンドポイントが表示されます
1. KEY 1の値を `AZURE_OPENAI_API_KEY` に設定します
1. エンドポイントの値を `AZURE_OPENAI_ENDPOINT` に設定します

次に、デプロイした特定のモデルのエンドポイント情報を取得します。

1. Azure OpenAIリソースのサイドバー（左メニュー）で<strong>モデルデプロイメント</strong>をクリックします
1. 遷移先のページで、**Microsoft Foundryポータルに移動**（またはリソースタイプによっては<strong>デプロイメント管理</strong>）をクリックします

Microsoft Foundryポータルに遷移し、以下のように他の値を取得します。

## Azure OpenAIの設定：Microsoft Foundryポータルから

1. 上記のように、[Microsoft Foundryポータル](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)へ<strong>リソースから</strong>アクセスします。
1. 左サイドバーの<strong>デプロイメント</strong>タブをクリックして現在のモデルを確認します。
1. 希望のモデルが未展開の場合、[モデルカタログ](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)から<strong>モデルをデプロイ</strong>してください。
1. _テキスト生成_モデルとしては、<strong>gpt-5-mini</strong>を推奨します。
1. _テキスト埋め込み_モデルとしては、<strong>text-embedding-3-small</strong>を推奨します。

ここで、環境変数を使用している_Deployment name_に合わせて更新します。通常はモデル名と同じですが、明示的に変更している場合はそちらを使います。例えば：

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**設定後は.envファイルを保存するのを忘れないでください**。ファイルを閉じ、ノートブック実行の手順に戻ってください。

## OpenAIの設定：プロフィールから

OpenAIのAPIキーは[OpenAIアカウント](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst)で確認できます。アカウントがなければ登録し、APIキーを作成してください。取得したキーを `.env` ファイルの `OPENAI_API_KEY` に設定します。

## Hugging Faceの設定：プロフィールから

Hugging Faceのトークンは[アクセストークン](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst)のプロファイルで確認できます。これらは公開しないでください。このプロジェクト用に新しいトークンを作成し、`.env` ファイルの `HUGGING_FACE_API_KEY` にコピーしてください。_注意：_ 技術的にはAPIキーではありませんが、認証に使うため一貫性を保つためにこの名前を使っています。

## Microsoft Foundry Modelsの設定：ポータルから

> **注意：**GitHub Modelsは2026年7月末に廃止されます。Microsoft Foundry Modelsが直接の代替であり、無料トライモデルカタログとAzure AI推論SDK / OpenAI SDKの体験を提供しています。

1. [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)にアクセスし、Foundryプロジェクトを作成または開きます。
1. [モデルカタログ](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)をブラウズし、例として `gpt-5-mini` をデプロイします。
1. プロジェクトの<strong>概要</strong>ページで、<strong>エンドポイント</strong>と<strong>APIキー</strong>をコピーします。
1. `.env` ファイルの `AZURE_INFERENCE_ENDPOINT` にエンドポイント値を、`AZURE_INFERENCE_CREDENTIAL` にキー値を設定します。

## オフライン / ローカルプロバイダー

クラウドサブスクリプションを全く使いたくない場合、ご自身のデバイスで互換性のあるオープンモデルを直接実行できます：

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - マイクロソフトのデバイス上実行環境です。最適な実行プロバイダー（NPU、GPU、CPU）を自動選択し、OpenAI互換のエンドポイントを提供するため、本コースのサンプルコードの多くを最小限の変更で再利用可能です。入門には[Foundry Localドキュメント](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst)を参照、または`winget install Microsoft.FoundryLocal`（Windows）/ `brew install microsoft/foundrylocal/foundrylocal`（macOS）でインストールしてください。
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - Llama、Phi、Mistral、Gemmaなどのオープンモデルをローカルで実行する人気の代替案です。


両方のオプションを使用した実践的な例については、[Lesson 19: Building with SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) を参照してください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->