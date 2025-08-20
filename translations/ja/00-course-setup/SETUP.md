<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:25:01+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "ja"
}
-->
# 開発環境のセットアップ

このリポジトリとコースは、Python3、.NET、Node.js、Javaの開発をサポートするユニバーサルランタイムを備えた[開発コンテナ](https://containers.dev?WT.mc_id=academic-105485-koreyst)を使って構成されています。関連する設定は、このリポジトリのルートにある `.devcontainer/` フォルダー内の `devcontainer.json` ファイルに定義されています。

開発コンテナを起動するには、[GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst)（クラウドホスト型ランタイム用）または[Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst)（ローカルデバイスホスト型ランタイム用）で起動してください。VS Code内での開発コンテナの動作については、[こちらのドキュメント](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst)を参照してください。

> [!TIP]  
> 最小限の手間で素早く始めるにはGitHub Codespacesの利用をおすすめします。個人アカウント向けに十分な[無料利用枠](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst)が提供されています。利用枠を最大限活用するために、非アクティブなCodespacesを停止または削除する[タイムアウト設定](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst)を行いましょう。

## 1. 課題の実行

各レッスンには、Python、.NET/C#、Java、JavaScript/TypeScriptなど複数のプログラミング言語で提供されることがある_任意の_課題があります。このセクションでは、それらの課題の実行に関する一般的なガイダンスを示します。

### 1.1 Python課題

Pythonの課題は、アプリケーション（`.py`ファイル）またはJupyterノートブック（`.ipynb`ファイル）として提供されます。  
- ノートブックを実行するには、Visual Studio Codeで開き、右上の _Select Kernel_ をクリックして表示されるデフォルトのPython 3を選択します。その後、_Run All_ を実行してノートブック全体を実行できます。  
- コマンドラインからPythonアプリケーションを実行する場合は、課題ごとの指示に従い、正しいファイルを選択し必要な引数を指定してください。

## 2. プロバイダーの設定

課題は、OpenAI、Azure、Hugging Faceなどのサポートされているサービスプロバイダーを通じて、1つ以上の大規模言語モデル（LLM）展開に対して動作するよう設定されている場合があります。これらは、適切な認証情報（APIキーやトークン）を使ってプログラムからアクセス可能な_ホスト型エンドポイント_（API）を提供します。本コースでは以下のプロバイダーについて扱います：

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) ：コアのGPTシリーズを含む多様なモデル  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) ：エンタープライズ対応に重点を置いたOpenAIモデル  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) ：オープンソースモデルと推論サーバー  

**これらの演習にはご自身のアカウントが必要です**。課題は任意なので、興味に応じて1つ、すべて、またはどれも設定しなくても構いません。サインアップの参考情報は以下の通りです：

| サインアップ | 料金 | APIキー | Playground | コメント |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [料金](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [プロジェクトベース](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [ノーコード、Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 複数モデル利用可能 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [料金](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [SDKクイックスタート](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Studioクイックスタート](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [事前申請が必要](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [料金](https://huggingface.co/pricing) | [アクセストークン](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Hugging Chatはモデルが限定的](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

以下の手順に従って、このリポジトリを各プロバイダー用に_設定_してください。特定のプロバイダーが必要な課題は、ファイル名に以下のタグが含まれます：  
 - `aoai` - Azure OpenAIのエンドポイントとキーが必要  
 - `oai` - OpenAIのエンドポイントとキーが必要  
 - `hf` - Hugging Faceのトークンが必要  

1つ、複数、またはすべてのプロバイダーを設定可能です。認証情報が不足している場合は、関連課題はエラーになります。

### 2.1 `.env` ファイルの作成

上記のガイダンスを読み、該当するプロバイダーにサインアップし、必要な認証情報（API_KEYやトークン）を取得済みであることを前提とします。Azure OpenAIの場合は、少なくとも1つのGPTモデルがチャット補完用にデプロイされたAzure OpenAIサービス（エンドポイント）を有効にしていることも前提です。

次に、**ローカルの環境変数**を以下のように設定します：

1. ルートフォルダーに `.env.copy` ファイルがあり、以下のような内容が含まれていることを確認してください：

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

2. 以下のコマンドで `.env.copy` を `.env` にコピーします。このファイルは _gitignore_ に含まれており、秘密情報を安全に保ちます。

   ```bash
   cp .env.copy .env
   ```

3. 次のセクションで説明するように、`=` の右側のプレースホルダーを実際の値に置き換えてください。

3. （オプション）GitHub Codespacesを使う場合は、このリポジトリに関連付けられた_Codespaces secrets_として環境変数を保存することもできます。その場合、ローカルの `.env` ファイルを設定する必要はありません。**ただし、このオプションはGitHub Codespacesを使う場合のみ有効です。** Docker Desktopを使う場合は引き続き `.env` ファイルの設定が必要です。

### 2.2 `.env` ファイルの内容を入力

変数名が何を意味するか簡単に見てみましょう：

| 変数名 | 説明 |
| :--- | :--- |
| HUGGING_FACE_API_KEY | プロフィールで設定したユーザーアクセストークン |
| OPENAI_API_KEY | Azure以外のOpenAIエンドポイントでサービスを利用するための認証キー |
| AZURE_OPENAI_API_KEY | Azure OpenAIサービスを利用するための認証キー |
| AZURE_OPENAI_ENDPOINT | Azure OpenAIリソースのデプロイ済みエンドポイント |
| AZURE_OPENAI_DEPLOYMENT | _テキスト生成_モデルのデプロイメント名 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _テキスト埋め込み_モデルのデプロイメント名 |
| | |

補足：最後の2つのAzure OpenAI変数は、それぞれチャット補完（テキスト生成）用とベクトル検索（埋め込み）用のデフォルトモデルを示します。設定方法は該当する課題で指示されます。

### 2.3 Azureの設定：ポータルから

Azure OpenAIのエンドポイントとキーは[Azureポータル](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)で確認できます。まずはそこから始めましょう。

1. [Azureポータル](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)にアクセスします。  
1. サイドバー（左メニュー）で **Keys and Endpoint** をクリックします。  
1. **Show Keys** をクリックすると、KEY 1、KEY 2、Endpointが表示されます。  
1. KEY 1の値を `AZURE_OPENAI_API_KEY` に設定します。  
1. Endpointの値を `AZURE_OPENAI_ENDPOINT` に設定します。

次に、デプロイ済みのモデルのエンドポイントを取得します。

1. Azure OpenAIリソースのサイドバーで **Model deployments** をクリックします。  
1. 表示されたページで **Manage Deployments** をクリックします。

これによりAzure OpenAI Studioのウェブサイトに移動し、以下の説明にある値を確認できます。

### 2.4 Azureの設定：Studioから

1. 上記の手順でアクセスした[Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst)に移動します。  
1. サイドバーの **Deployments** タブをクリックし、現在デプロイされているモデルを確認します。  
1. 目的のモデルがデプロイされていない場合は、**Create new deployment** で新規デプロイしてください。  
1. _テキスト生成_モデルとしては、**gpt-35-turbo** を推奨します。  
1. _テキスト埋め込み_モデルとしては、**text-embedding-ada-002** を推奨します。

環境変数には、使用している_デプロイメント名_を設定してください。通常はモデル名と同じですが、明示的に変更している場合はその名前を使います。例としては以下のようになります：

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**設定後は必ず .env ファイルを保存してください**。保存したらファイルを閉じ、ノートブック実行の手順に戻ってください。

### 2.5 OpenAIの設定：プロフィールから

OpenAIのAPIキーは、[OpenAIアカウント](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst)で確認できます。アカウントを持っていない場合はサインアップしてAPIキーを作成してください。取得したキーを `.env` ファイルの `OPENAI_API_KEY` に設定します。

### 2.6 Hugging Faceの設定：プロフィールから

Hugging Faceのトークンは、プロフィールの[Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst)で確認できます。これらを公開したり共有したりしないでください。このプロジェクト用に新しいトークンを作成し、`.env` ファイルの `HUGGING_FACE_API_KEY` にコピーしてください。  
_注意：_ これは厳密にはAPIキーではありませんが、認証に使うため一貫性を保つためにこの名前を使っています。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。