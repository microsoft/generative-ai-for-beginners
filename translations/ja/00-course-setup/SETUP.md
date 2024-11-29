# 開発環境のセットアップ

このリポジトリとコースは、Python3、.NET、Node.js、Javaの開発をサポートするユニバーサルランタイムを備えた[開発コンテナ](https://containers.dev?WT.mc_id=academic-105485-koreyst)で設定されています。関連する設定は、このリポジトリのルートにある`.devcontainer/`フォルダ内の`devcontainer.json`ファイルに定義されています。

開発コンテナを有効にするには、[GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst)（クラウドホスト型ランタイム用）または[Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst)（ローカルデバイスホスト型ランタイム用）で起動します。VS Code内での開発コンテナの動作についての詳細は[こちらのドキュメント](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst)を参照してください。

> [!TIP]  
> 最小限の労力で素早く始めるために、GitHub Codespacesを使用することをお勧めします。個人アカウントには寛大な[無料使用枠](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst)が提供されます。クォータ使用を最大化するために、非アクティブなコードスペースを停止または削除するための[タイムアウト](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst)を設定します。

## 1. 課題の実行

各レッスンには、Python、.NET/C#、Java、JavaScript/TypeScriptなど、1つ以上のプログラミング言語で提供される_オプション_の課題があります。このセクションでは、それらの課題を実行するための一般的なガイダンスを提供します。

### 1.1 Pythonの課題

Pythonの課題は、アプリケーション（`.py`ファイル）またはJupyterノートブック（`.ipynb`ファイル）として提供されます。
- ノートブックを実行するには、Visual Studio Codeで開き、_Select Kernel_（右上）をクリックして表示されるデフォルトのPython 3オプションを選択します。その後、_Run All_を実行してノートブックを実行できます。
- コマンドラインからPythonアプリケーションを実行するには、課題に特化した指示に従い、正しいファイルを選択し、必要な引数を提供してください。

## 2. プロバイダーの設定

課題は、OpenAI、Azure、Hugging Faceのようなサポートされているサービスプロバイダーを通じて、1つ以上の大規模言語モデル（LLM）デプロイメントに対して動作するように設定される場合もあります。これらは、適切な資格情報（APIキーまたはトークン）でプログラム的にアクセスできる_ホストエンドポイント_（API）を提供します。このコースでは、以下のプロバイダーについて説明します：

 - 多様なモデルを含むコアGPTシリーズを持つ[OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst)。
 - エンタープライズ対応に重点を置いたOpenAIモデルを提供する[Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)。
 - オープンソースモデルと推論サーバーを提供する[Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst)。

**これらの演習には自分のアカウントを使用する必要があります**。課題はオプションなので、興味に応じて1つ、すべて、またはプロバイダーを設定しないことを選択できます。サインアップのためのガイダンスは以下の通りです：

| サインアップ | コスト | APIキー | プレイグラウンド | コメント |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [料金](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [プロジェクトベース](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [ノーコード、Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 複数のモデルが利用可能 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [料金](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDKクイックスタート](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [スタジオクイックスタート](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [アクセスのために事前に申し込む必要あり](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [料金](https://huggingface.co/pricing) | [アクセス トークン](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chatは限られたモデルを持つ](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

以下の指示に従って、このリポジトリを異なるプロバイダーで使用するために_設定_します。特定のプロバイダーを必要とする課題には、ファイル名に以下のタグのいずれかが含まれます：
 - `aoai` - Azure OpenAIエンドポイントとキーが必要
 - `oai` - OpenAIエンドポイントとキーが必要
 - `hf` - Hugging Faceトークンが必要

1つ、すべて、またはプロバイダーを設定しないことができます。関連する課題は、資格情報がない場合にエラーが発生します。

###  2.1. `.env`ファイルを作成

すでに上記のガイダンスを読み、関連するプロバイダーにサインアップし、必要な認証資格情報（API_KEYまたはトークン）を取得したと仮定します。Azure OpenAIの場合、少なくとも1つのGPTモデルがデプロイされたAzure OpenAIサービス（エンドポイント）の有効なデプロイメントを持っていると仮定します。

次のステップは、**ローカル環境変数**を以下のように設定することです：

1. ルートフォルダに、以下のような内容を持つ`.env.copy`ファイルがあるか確認してください：

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

2. 下記のコマンドを使用してそのファイルを`.env`にコピーします。このファイルは_gitignore_されており、秘密を安全に保ちます。

   ```bash
   cp .env.copy .env
   ```

3. 次のセクションで説明するように、値を入力（右側のプレースホルダーを置き換え）します。

3. （オプション）GitHub Codespacesを使用している場合、このリポジトリに関連付けられた_Codespaces secrets_として環境変数を保存するオプションがあります。この場合、ローカルの.envファイルを設定する必要はありません。**ただし、このオプションはGitHub Codespacesを使用している場合にのみ機能します。** Docker Desktopを使用する場合は、.envファイルを設定する必要があります。

### 2.2. `.env`ファイルに値を入力

変数名が何を表しているのかを理解するために、簡単に見てみましょう：

| 変数  | 説明  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | プロファイルで設定したユーザーアクセス トークンです |
| OPENAI_API_KEY | 非Azure OpenAIエンドポイントでサービスを使用するための認証キーです |
| AZURE_OPENAI_API_KEY | そのサービスを使用するための認証キーです |
| AZURE_OPENAI_ENDPOINT | Azure OpenAIリソースのデプロイされたエンドポイントです |
| AZURE_OPENAI_DEPLOYMENT | _テキスト生成_モデルのデプロイメントエンドポイントです |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _テキスト埋め込み_モデルのデプロイメントエンドポイントです |
| | |

注意: 最後の2つのAzure OpenAI変数は、チャットコンプリート（テキスト生成）とベクトル検索（埋め込み）に対するデフォルトモデルを反映しています。それらを設定するための指示は、関連する課題で定義されます。

### 2.3 Azureの設定: ポータルから

Azure OpenAIエンドポイントとキーの値は、[Azureポータル](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)で見つけることができますので、そこから始めましょう。

1. [Azureポータル](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)にアクセスします。
1. サイドバー（左側のメニュー）の**キーとエンドポイント**オプションをクリックします。
1. **キーを表示**をクリックすると、KEY 1、KEY 2、およびエンドポイントが表示されます。
1. KEY 1の値をAZURE_OPENAI_API_KEYとして使用します。
1. エンドポイントの値をAZURE_OPENAI_ENDPOINTとして使用します。

次に、デプロイした特定のモデルのエンドポイントが必要です。

1. Azure OpenAIリソースのサイドバー（左側のメニュー）で**モデルデプロイメント**オプションをクリックします。
1. 目的のページで**デプロイメントの管理**をクリックします。

これにより、Azure OpenAI Studioのウェブサイトに移動し、以下で説明する他の値を見つけます。

### 2.4 Azureの設定: スタジオから

1. 上述のように**リソースから**[Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst)に移動します。
1. 現在デプロイされているモデルを表示するために**デプロイメント**タブ（サイドバー、左）をクリックします。
1. 希望するモデルがデプロイされていない場合は、**新しいデプロイメントを作成**を使用してデプロイします。
1. _テキスト生成_モデルが必要です - **gpt-35-turbo**をお勧めします。
1. _テキスト埋め込み_モデルが必要です - **text-embedding-ada-002**をお勧めします。

環境変数を使用した_デプロイメント名_を反映するように更新します。これは通常、モデル名と同じですが、明示的に変更した場合を除きます。したがって、例えば、次のようになるかもしれません：

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**完了したら.envファイルを保存することを忘れないでください**。ファイルを終了し、ノートブックを実行するための指示に戻ることができます。

### 2.5 OpenAIの設定: プロファイルから

OpenAI APIキーは、[OpenAIアカウント](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst)で見つけることができます。まだ持っていない場合は、アカウントにサインアップしてAPIキーを作成できます。キーを取得したら、それを`.env`ファイルの`OPENAI_API_KEY`変数に入力して使用できます。

### 2.6 Hugging Faceの設定: プロファイルから

Hugging Faceトークンは、[アクセス トークン](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst)の下にあるプロファイルで見つけることができます。これらを公に投稿または共有しないでください。このプロジェクトの使用のために新しいトークンを作成し、それを`.env`ファイルの`HUGGING_FACE_API_KEY`変数にコピーします。_注意:_ これは技術的にはAPIキーではありませんが、認証に使用されるため、一貫性のためにその命名規則を維持しています。

**免責事項**:  
この文書は、機械翻訳AIサービスを使用して翻訳されています。正確さを期すために努力していますが、自動翻訳には誤りや不正確さが含まれる場合があります。元の言語の文書を公式な情報源として考慮してください。重要な情報については、プロの人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当社は責任を負いません。