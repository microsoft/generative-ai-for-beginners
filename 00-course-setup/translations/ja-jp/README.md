# このコースを始めるための準備

私たちは、皆様がこのコースを開始して、生成 AI を使ってどのような物を作り出してくださるのか、それを見るのがとても楽しみです！

皆様がこのレッスンを成功できるよう、セットアップ手順と技術要件そして必要な時に必要な情報を得るための方法を、このページにまとめました。  

## セットアップ手順

このコースを始める前に、下記の手順を実施してください。  

### 1. リポジトリのフォーク

コードを修正したり、レッスン課題を終了するため、このリポジトリをご自身の GitHub アカウントに[フォーク](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-yoterada)してください。また後から、簡単にこのリポジトリを見つけられるように、[スター（🌟）をつける](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-yoterada)のもお勧めです。

### 2. Codespaces を作成

コードを実行する際、依存関係の問題を避けるため、GitHub Codespaces で、このコースの実行をお勧めします。  

Codespaces は、フォークしたリポジトリから、下記の緑のボタンの `Code` を選択し、**Codespaces** オプションを選択し作成できます。

![codespaceを作成するボタンを示すダイアログ](../../images/who-will-pay.webp?WT.mc_id=academic-105485-yoterada)

> [!NOTE]
> (訳者追記)：  
Organization に所属しないユーザーが Fork したリポジトリで Codespace を利用する場合、[Codespace の使用料は個人のアカウントに課金されます](https://docs.github.com/ja/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces?WT.mc_id=academic-105485-yoterada#limiting-the-number-of-organization-owned-codespaces)。

### 3. API　キーの保管

アプリケーション開発において、API キーは安全に扱う必要があります。公開リポジトリにこうした機密情報をコミットすると、不正利用による想定外のコストや問題が発生する可能性があります。そこで、作業中のソース・コードに直接 API キーを保存しないようにしてください。  

## ローカルのコンピュータで実行する方法

ローカルのコンピュータ上で、コードを実行するためには、[Python のインストール](https://www.python.org/downloads/?WT.mc_id=academic-105485-yoterada)が必要です。

そして、下記のようにリポジトリをクローンしてください。

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

以上で準備が整ったので、学習と作業を開始できます。

### miniconda　のインストール　（オプションの手順）

下記は省略可能な手順ですが、可能であれば **[miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-yoterada)** のインストールをお勧めします。これは、異なる Python **仮想環境**で `conda` パッケージ・マネージャをサポートする、比較的軽量なインストーラーです。`conda` を利用すると、異なる Python のバージョンやパッケージを簡単にインストールでき、切り替えもできます。さらに、`pip` を利用して公開されているパッケージのインストールもできます。  

miniconda をインストールした後、リポジトリをクローンしてください（まだ行っていない場合）。そして、このレッスン用に下記の手順で新たな仮想環境を作成してください：  

まず 「*environment.yml*」ファイルが存在しているかご確認ください。「*environment.yml*」ファイルは、conda　環境の構築に必要な依存関係を定義した設定ファイルで、下記の内容を記述します：  

```yml
name: <environment-name>
channels:  
 - defaults
dependencies:  
- python=<python-version>  
- openai  
- python-dotenv
```

`<environment-name>` には、この conda 環境名を設定し、`<python-version>` には使用する Python のバージョンを記述してください。作成した「*environment.yml*」ファイルはリポジトリ内の「*.devcontainer*」フォルダ配下に置いてください。  

「*environment.yml*」ファイルを作成した後、下記のコマンドを実行し、conda 環境を作成します：  

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

仮に何らかの問題が発生した場合は、ユーザ・ガイドの [conda 環境](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-yoterada)をご参照ください。  

### Python の拡張機能をインストールした Visual Studio Code の使用

このカリキュラムを進める際には、[Python の拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-yoterada)をインストールした [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-105485-yoterada) の使用を特にお勧めします。

> **ご注意**: クローンした後、VS Code でディレクトリを開くと、自動的に Python 拡張機能のインストールが提案されます。上記で説明したように miniconda もインストールしてください。

> **ご注意**: ローカルにインストールした Python を使いたいと考えている場合は、VS Code からコンテナでリポジトリを開く提案があった際に、その提案を却下してください。

### ブラウザで Jupyter の使用

ご自分のコンピュータの Web ブラウザを利用して直接 Jupyter 環境を利用できます。実際クラシックな Jupyter と Jupyter Hub は、自動補完、コード・ハイライトなどの機能を備えた非常に便利な開発環境を提供します。  

Jupyter をローカルで起動するには、レッスン・コースのディレクトリに移動し、下記のコマンドを実行します：  

```bash
jupyter notebook
```

もしくは

```bash
jupyterhub
```

次に任意の `.ipynb` ファイルに移動し、ファイルを開いて作業を開始します。  

### コンテナでの実行

ローカル環境に Python をインストールする代わりに、コンテナ上でも実行できます。このプロジェクトを fork するとレポジトリ内に、コンテナ・イメージを構築するために必要な設定を含む `.devcontainer` フォルダが存在します。そして VS Code は設定ファイルに記載した内容を元に、コンテナ上での実行を提案します。ローカルでコンテナを実行する為には、事前に Docker のインストールと起動が必要です。ローカルでのコンテナ環境のセットアップは少し複雑になるため経験豊富な利用者にお勧めします。

GitHub Codespaces を使用して API キーを安全に管理するためには、Codespace Secrets の利用をお勧めします。[Ccodespaces のシークレットを管理](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-yoterada)する方法については、リンク先のガイドをご参照ください。  

## レッスンと技術要件

このコースは、6 つの概念レッスンと 6 つのコーディング・レッスンが含まれます。

コーディング・レッスンでは、Azure OpenAI サービスを使用します。コードを実行するには、Azure OpenAI サービスへのアクセス権限と API キーが必要です。[こちらのアプリケーション・フォームに記入](https://go.microsoft.com/fwlink/?linkid=2222006&clcid=0x409?WT.mc_id=academic-105485-yoterada)し Azure OpenAI のアクセス申請を行ってください。  

アプリケーション・フォームの申請処理が完了するまで、何もできないわけでは決してありません。各レッスン中に、`README.md` ファイルとサンプル・コードが含まれていますので、申請処理が完了する前からレッスンの内容をご確認いただけます。

## Azure OpenAI サービスをはじめて使用する場合  

仮に Azure OpenAI サービスをはじめて使用する場合は、[Azure OpenAI サービスのリソースを作成しデプロイする](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-yoterada)必要があります。リソースの作成方法はリンク先のガイドをご参照ください。  

## 他の学習者との交流

他の学習者と交流できるように、私たちは[公式の AI Discord サーバー](https://aka.ms/genai-discord?WT.mc_id=academic-105485-yoterada)にチャンネルを作成しました。生成 AI の技術を向上したいと考える他の方々、たとえば、志の同じ起業家、開発者、学生、そして、どなたとでも交流していただく事が可能です。  

[![Discord チャンネルに参加](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-yoterada)

このプロジェクトを開発したチーム・メンバーも、この Discord サーバーに参加し学習者を支援しています。  

## 貢献

本レッスンはオープンソース・プロジェクトとして公開しています。仮に改善すべき点や問題を発見したら、[プルリクエスト](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-yoterada)をお送りいただくか、もしくは、[GitHub の Issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-yoterada) で報告していただければ誠に幸いです。

このプロジェクトの開発チームは全ての貢献を確認しています。そしてオープン・ソース・プロジェクトに貢献すると、生成 AI の分野で新しいキャリアを築ける可能性もあります。

通常、貢献者にはコントリビューター・ライセンス契約（CLA）へ同意して頂く必要があります。この契約によって、貢献者は自らの権利を私たちに譲渡し、私たちがそのご貢献いただいた成果物を利用する権利を得るための契約を行います。詳細については [CLA、コントリビューターライセンス契約のウェブサイト](https://cla.microsoft.com?WT.mc_id=academic-105485-yoterada)をご覧ください。

重要なお知らせ：  
このリポジトリ内に含まれるテキストを翻訳する場合、機械翻訳の使用は避けてください。翻訳内容はコミュニティで検証するため、ご自身が熟知している言語でのみ翻訳作業にご協力ください。

プル・リクエストを提出すると、CLA-bot が自動的に CLA（コントリビューター・ライセンス契約）の提出が必要かどうかを判断し、プル・リクエストに適切なマーク（例：ラベル、コメント）を付けます。bot の指示にお従いください。この処理は、CLA を使用するすべてのリポジトリで一度だけ行う必要があります。

このプロジェクトは、[Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-yoterada) を採用しています。詳細は、Code of Conduct FAQ をご覧いただくか、追加の質問やコメントがある場合は、 [opencode 宛てにメールで](mailto:opencode@microsoft.com)お問い合わせください。  

## それでは、始めましょう

このレッスンを修了するために必要な手順をすべて完了したので、[生成 AI と大規模言語モデルの紹介](../../../01-introduction-to-genai/translations/ja-jp/README.md?WT.mc_id=academic-105485-yoterada) から始めましょう。
