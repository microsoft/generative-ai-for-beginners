<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T09:03:59+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "ja"
}
-->
# 開発環境のセットアップ

このリポジトリとコースは、Python3、.NET、Node.js、Javaの開発をサポートするユニバーサルランタイムを備えた[開発コンテナ](https://containers.dev?WT.mc_id=academic-105485-koreyst)でセットアップされています。関連する設定は、このリポジトリのルートにある`.devcontainer/`フォルダ内の`devcontainer.json`ファイルに定義されています。

開発コンテナをアクティブにするには、[GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst)（クラウドホスト型ランタイムの場合）または[Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst)（ローカルデバイスホスト型ランタイムの場合）で起動します。VS Code内での開発コンテナの動作についての詳細は[このドキュメント](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst)を参照してください。

> [!TIP]  
> 最小限の手間で迅速に開始するためにはGitHub Codespacesの使用をお勧めします。個人アカウントには寛大な[無料使用枠](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst)が提供されます。タイムアウトを設定して、非アクティブなCodespaceを停止または削除し、クォータ使用を最大化します。

## 1. 課題の実行

各レッスンには、Python、.NET/C#、Java、JavaScript/TypeScriptを含む1つ以上のプログラミング言語で提供される_オプションの_課題があります。このセクションでは、それらの課題を実行するための一般的なガイダンスを提供します。

### 1.1 Python課題

Pythonの課題は、アプリケーション（`.py`ファイル）またはJupyterノートブック（`.ipynb`ファイル）として提供されます。
- ノートブックを実行するには、Visual Studio Codeで開き、右上の_カーネルを選択_をクリックし、表示されるデフォルトのPython 3オプションを選択します。これで_すべて実行_を選択してノートブックを実行できます。
- コマンドラインからPythonアプリケーションを実行するには、課題に特化した指示に従って正しいファイルを選択し、必要な引数を提供してください。

## 2. プロバイダーの設定

課題は、OpenAI、Azure、Hugging Faceなどのサポートされているサービスプロバイダーを通じて、1つまたは複数の大規模言語モデル（LLM）デプロイメントに対して動作するように設定されることもあります。これらは、適切な認証情報（APIキーまたはトークン）を使用してプログラム的にアクセスできる_ホストエンドポイント_（API）を提供します。このコースでは、以下のプロバイダーについて説明します：

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst)：GPTシリーズを含む多様なモデルを提供
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)：エンタープライズ対応を重視したOpenAIモデル
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst)：オープンソースモデルと推論サーバー

**これらの演習には自分のアカウントを使用する必要があります**。課題はオプションであるため、興味に応じて1つ、すべて、またはどれも設定しないことができます。サインアップのためのガイダンス：

| サインアップ | コスト | APIキー | プレイグラウンド | コメント |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [価格](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [プロジェクトベース](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [ノーコード、Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 複数のモデルが利用可能 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [価格](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDKクイックスタート](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [スタジオクイックスタート](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [アクセスのために事前申請が必要](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [価格](https://huggingface.co/pricing) | [アクセストークン](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chatは限られたモデルを持つ](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

以下の手順に従って、このリポジトリを異なるプロバイダーで使用するために_設定_します。特定のプロバイダーを必要とする課題は、そのファイル名に次のタグのいずれかを含みます：
 - `aoai` - Azure OpenAIエンドポイント、キーが必要
 - `oai` - OpenAIエンドポイント、キーが必要
 - `hf` - Hugging Faceトークンが必要

1つ、どれも、またはすべてのプロバイダーを設定できます。関連する課題は、認証情報が欠如している場合にエラーを発生させます。

### 2.1. `.env`ファイルの作成

上記のガイダンスを既に読み、関連するプロバイダーにサインアップし、必要な認証情報（API_KEYまたはトークン）を取得したと仮定します。Azure OpenAIの場合、チャット完了のために少なくとも1つのGPTモデルをデプロイしたAzure OpenAIサービス（エンドポイント）の有効なデプロイメントを持っていると仮定します。

次のステップは、以下のように**ローカル環境変数**を設定することです：

1. ルートフォルダで、次のような内容を持つ`.env.copy`ファイルを探します：

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. そのファイルを`.env`にコピーします。このファイルは_gitignore-d_されており、秘密を安全に保ちます。

   ```bash
   cp .env.copy .env
   ```

3. 次のセクションで説明するように、値（`=`の右側のプレースホルダーを置き換える）を記入します。

3. （オプション）GitHub Codespacesを使用する場合、環境変数をこのリポジトリに関連付けられた_Codespaces secrets_として保存するオプションがあります。その場合、ローカルの.envファイルを設定する必要はありません。ただし、このオプションはGitHub Codespacesを使用する場合にのみ機能します。Docker Desktopを使用する場合は、.envファイルを設定する必要があります。

### 2.2. `.env`ファイルの内容を記入

変数名が何を表しているかを理解するために、簡単に見てみましょう：

| 変数 | 説明 |
| :--- | :--- |
| HUGGING_FACE_API_KEY | プロファイルで設定したユーザーアクセストークン |
| OPENAI_API_KEY | 非Azure OpenAIエンドポイントでサービスを使用するための認証キー |
| AZURE_OPENAI_API_KEY | サービスを使用するための認証キー |
| AZURE_OPENAI_ENDPOINT | Azure OpenAIリソースのデプロイされたエンドポイント |
| AZURE_OPENAI_DEPLOYMENT | _テキスト生成_モデルのデプロイメントエンドポイント |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _テキスト埋め込み_モデルのデプロイメントエンドポイント |
| | |

注：最後の2つのAzure OpenAI変数は、チャット完了（テキスト生成）とベクトル検索（埋め込み）のためのデフォルトモデルを反映しています。それらの設定方法は、関連する課題で定義されます。

### 2.3 Azureの設定：ポータルから

Azure OpenAIエンドポイントとキーの値は[Azureポータル](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)にありますので、まずそこから始めましょう。

1. [Azureポータル](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)にアクセスします。
1. サイドバー（左メニュー）で**キーとエンドポイント**オプションをクリックします。
1. **キーを表示**をクリックすると、KEY 1、KEY 2、エンドポイントが表示されます。
1. AZURE_OPENAI_API_KEYにはKEY 1の値を使用します。
1. AZURE_OPENAI_ENDPOINTにはエンドポイントの値を使用します。

次に、デプロイした特定のモデルのエンドポイントが必要です。

1. Azure OpenAIリソースのサイドバー（左メニュー）で**モデルデプロイメント**オプションをクリックします。
1. 目的のページで**デプロイメントを管理**をクリックします。

これにより、Azure OpenAI Studioのウェブサイトに移動し、以下で説明する他の値を見つけることができます。

### 2.4 Azureの設定：スタジオから

1. 上記のように、リソースから[Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst)に移動します。
1. 現在デプロイされているモデルを表示するために**デプロイメント**タブ（サイドバー、左）をクリックします。
1. 望むモデルがデプロイされていない場合、**新しいデプロイメントを作成**を使用してデプロイします。
1. _テキスト生成_モデルが必要です - 推奨：**gpt-35-turbo**
1. _テキスト埋め込み_モデルが必要です - 推奨：**text-embedding-ada-002**

次に、環境変数を使用した_デプロイメント名_を反映するように更新します。通常、これはモデル名と同じになりますが、明示的に変更した場合を除きます。例えば、次のようにすることができます：

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**完了したら.envファイルを保存するのを忘れないでください**。これでファイルを終了し、ノートブックの実行指示に戻ることができます。

### 2.5 OpenAIの設定：プロファイルから

OpenAIのAPIキーは[OpenAIアカウント](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst)で見つけることができます。持っていない場合は、アカウントにサインアップしてAPIキーを作成できます。キーを取得したら、それを`.env`ファイル内の`OPENAI_API_KEY`変数に使用します。

### 2.6 Hugging Faceの設定：プロファイルから

Hugging Faceトークンは、プロファイルの[アクセストークン](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst)の下にあります。これらを公開しないでください。このプロジェクトの使用のために新しいトークンを作成し、それを`.env`ファイル内の`HUGGING_FACE_API_KEY`変数にコピーします。_注：_これは技術的にはAPIキーではありませんが、認証に使用されるため、一貫性のためにその命名規則を維持しています。

**免責事項**:  
このドキュメントはAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確さを期しておりますが、自動翻訳には誤りや不正確さが含まれる可能性がありますのでご注意ください。元の言語によるオリジナルのドキュメントが信頼できる情報源とみなされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用により生じる誤解や誤解釈について、当社は責任を負いません。