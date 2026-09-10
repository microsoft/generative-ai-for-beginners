# ローコードAIアプリケーションの構築

[![ローコードAIアプリケーションの構築](../../../translated_images/ja/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(このレッスンのビデオを見るには、上の画像をクリックしてください)_

## はじめに

画像生成アプリケーションの構築方法を学んだので、次はローコードについて話しましょう。生成AIはローコードを含むさまざまな分野で活用できますが、ローコードとは何で、どのようにAIを組み込むことができるのでしょうか？

ローコード開発プラットフォームの利用により、従来の開発者と非開発者の両方がアプリやソリューションをより簡単に作成できるようになりました。ローコード開発プラットフォームは、ほとんどまたは全くコードを書かずにアプリやソリューションを構築することを可能にします。これを実現するのが、コンポーネントをドラッグ＆ドロップしてアプリやソリューションを構築できるビジュアル開発環境です。このため、より少ないリソースで迅速にアプリやソリューションを作成できます。本レッスンでは、ローコードの使い方とPower Platformを使ってAIによるローコード開発の強化方法を詳しく学びます。

Power Platformは、組織が自分たちのチームに直感的なローコードまたはノーコード環境で自分たちのソリューションを構築する力を与える機会を提供します。この環境はソリューション構築のプロセスを簡単にします。Power Platformを使えば、ソリューションを数カ月や数年ではなく、数日または数週間で構築可能です。Power Platformは5つの主要な製品で構成されています：Power Apps、Power Automate、Power BI、Power Pages、そしてCopilot Studioです。

このレッスンでは以下を扱います：

- Power Platformにおける生成AIの紹介
- Copilotの紹介と使い方
- Power Platformで生成AIを使ってアプリやフローを構築する方法
- AI Builderを使ったPower PlatformのAIモデルの理解
- Microsoft Copilot Studioを使ったインテリジェントエージェントの構築

## 学習目標

このレッスンを終える頃には、以下ができるようになります：

- Power PlatformでのCopilotの働き方を理解する。

- 教育系スタートアップのための学生課題追跡アプリを構築する。

- 請求書から情報を抽出するためにAIを使う請求書処理フローを構築する。

- GPT AIモデルを使用した「テキスト作成」時のベストプラクティスを適用する。

- Microsoft Copilot Studioとは何か、そしてそれを使ったインテリジェントエージェントの構築方法を理解する。

このレッスンで使用するツールと技術は以下の通りです：

- **Power Apps**：学生課題追跡アプリ用のローコード開発環境で、データの追跡、管理、操作を行うアプリを構築します。

- **Dataverse**：学生課題追跡アプリのデータを保存するための低コードデータプラットフォームです。

- **Power Automate**：請求書処理フロー用の低コード開発環境で、請求書処理のワークフローを自動化します。

- **AI Builder**：請求書処理AIモデル用の事前構築されたAIモデルを使い、請求書を処理します。

## Power Platformにおける生成AI

生成AIによるローコード開発とアプリケーションの強化は、Power Platformの重要な注力分野です。目標は、誰もがデータサイエンスの専門知識なしで、AI搭載のアプリ、サイト、ダッシュボードを構築し、AIによるプロセス自動化を可能にすることです。この目標は、Power Platformのローコード開発体験にCopilotとAI Builderとして統合された生成AIにより達成されています。

### これはどのように機能するのでしょうか？

Copilotは自然言語による一連の対話ステップで要件を説明することでPower Platformソリューションを構築できるAIアシスタントです。例えば、アプリで使用するフィールドを指定すると、そのアプリと基盤となるデータモデルを作成したり、Power Automateでのフローの設定方法を指示したりできます。

ユーザーが対話的に洞察を得られるように、アプリ画面にCopilot駆動の機能を組み込むことも可能です。

AI BuilderはPower Platformで利用可能なローコードAI機能で、AIモデルを使いプロセスの自動化や結果の予測を支援します。AI Builderにより、DataverseやSharePoint、OneDrive、Azureなどのクラウドデータソースに接続するアプリやフローにAIを組み込めます。

CopilotはPower Apps、Power Automate、Power BI、Power Pages、Copilot Studio（旧Power Virtual Agents）の全製品に搭載されています。AI BuilderはPower AppsとPower Automateで利用可能です。このレッスンでは、教育系スタートアップ向けのソリューション構築でPower AppsとPower AutomateにおけるCopilotとAI Builderの使い方に焦点を当てます。

### Power AppsのCopilot

Power Platformの一部であるPower Appsは、データの追跡、管理、操作を行うアプリを構築するためのローコード開発環境を提供します。これはスケーラブルなデータプラットフォームとクラウドサービスやオンプレミスデータへの接続機能を備えたアプリ開発サービス群で、ブラウザ、タブレット、携帯電話で実行するアプリを構築し、共有できます。操作が簡単なため、ビジネスユーザーもプロ開発者もカスタムアプリを作成可能です。さらにCopilotによる生成AIでアプリ開発体験が強化されています。

Power AppsのCopilot AIアシスタント機能では、どのようなアプリを必要とし、追跡・収集・表示したい情報を記述すると、その説明に基づくレスポンシブなCanvasアプリを生成します。生成後、ニーズに合わせてカスタマイズ可能です。AI Copilotは必要なデータを格納するためのDataverseテーブルのフィールドやサンプルデータも提案し生成します。本レッスンの後半でDataverseとは何か、Power Appsでの使い方を学びます。対話的な手順でCopilotアシスタント機能を通じてテーブルのカスタマイズも可能です。この機能はPower Appsのホーム画面からすぐに利用できます。

### Power AutomateのCopilot

Power Platformの一部であるPower Automateは、アプリやサービス間で自動化されたワークフローを作成するための製品です。通信、データ収集、承認などの反復的な業務プロセスの自動化を支援します。初心者から経験豊富な開発者までの幅広い技術レベルのユーザーがワークタスクを自動化できるシンプルなインターフェイスを備えています。フロー開発体験もCopilotによる生成AIで強化されています。

Power AutomateのCopilot AIアシスタント機能では、必要なフローの内容や実行したいアクションを記述すると、その説明に基づくフローを生成します。生成後、ニーズに合わせカスタマイズ可能です。AI Copilotはタスクを自動化するために必要なアクションも提案し生成します。本レッスンの後半でフローとは何か、Power Automateでの使い方を学びます。対話的な手順でアクションのカスタマイズもCopilotアシスタント機能から可能です。この機能はPower Automateのホーム画面からすぐに利用できます。

## Microsoft Copilot Studioを使ったインテリジェントエージェントの構築

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst)（旧Power Virtual Agents）は、Power Platformのローコード製品であり、**AIエージェント**——ユーザーの質問に答え、操作を行い、タスクを自動化する対話型コパイロットを作成できます。Power Platformの他の製品と同様に、ビジュアルで自然言語中心の体験でこれらのエージェントを構築します。やりたいことを記述すると、Copilot Studioが指示、知識、アクションの枠組み作りを支援します。

教育系スタートアップのために、学生のコースに関する質問に答え、課題の締切を確認し、講師にメールを送るようなエージェントをノーコードで作成できます。

Copilot Studioを強力にする最新の機能には以下が含まれます：

- <strong>知識からの生成的回答</strong>。全ての会話を手作業で作成する代わりに、<strong>知識ソース</strong>（公開サイト、SharePoint、OneDrive、Dataverse、アップロード済みファイル、コネクタ経由の企業データ）を接続し、エージェントがそれらから根拠のある回答を生成します。

- <strong>生成的オーケストレーション</strong>。堅牢なトリガーフレーズに頼らず、要求をAIで理解し、必要な知識、トピック、アクションを動的に組み合わせて遂行、複数ステップを連結することも可能です。

- <strong>アクションとコネクタ</strong>。エージェントはチャットだけでなく行動も可能です。1500以上の事前構築Power Platformコネクタ、Power Automateフロー、カスタムREST API、プロンプト、<strong>モデルコンテキストプロトコル（MCP）</strong>サーバーに支えられたアクションを付与できます。

- <strong>自律エージェント</strong>。エージェントはチャットウィンドウ限定ではありません。新しいメール、Dataverseの新規レコード、ファイルのアップロードなどのイベントでトリガーされ、バックグラウンドでタスクを完了する<strong>自律エージェント</strong>も作れます。

- <strong>マルチエージェントオーケストレーション</strong>。エージェントは他のエージェントを呼び出せます。Copilot Studioエージェントは他のエージェントへの引継ぎや拡張が可能で、Microsoft 365 Copilotに公開されたエージェントやMicrosoft Foundryで構築されたエージェントも含まれます。

- <strong>モデル選択</strong>。組み込みモデルに加え、Microsoft Foundryモデルカタログのモデルを利用して、エージェントの推論や応答の調整が可能です。

- <strong>どこでも公開可能</strong>。構築後、エージェントはMicrosoft Teams、Microsoft 365 Copilot、ウェブサイトやカスタムアプリなど複数チャネルに公開でき、セキュリティ、認証、分析はPower Platform管理画面で管理されます。

[copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst)で最初のエージェント作成を始め、[Microsoft Copilot Studioドキュメント](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst)で詳細を学べます。

## 課題：Copilotを使ってスタートアップの学生課題と請求書を管理する

私たちのスタートアップは学生にオンラインコースを提供しています。急成長によりコースの需要が高まり、対応が難しくなっています。Power Platform開発者として、学生課題管理アプリと請求書処理ワークフローをローコードソリューションで構築する支援を依頼されました。生成AIを使ってソリューションを開発してください。

Copilotを使い始める際は、[Power Platform Copilot Prompt Library](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko)のプロンプト集が役立ちます。このライブラリにはCopilotでアプリやフローを構築するためのプロンプト例が含まれており、要件をどう説明するかのヒントも得られます。

### スタートアップ向け学生課題追跡アプリの構築

スタートアップの教育者は学生課題の管理に苦労しています。課題の追跡にスプレッドシートを使用していましたが、学生数の増加に伴い管理が難しくなっています。彼らから課題を追跡・管理できるアプリの作成依頼がありました。アプリは課題の追加、表示、更新、削除ができ、評価済みと未評価の課題の区別も可能にします。

以下の手順でPower AppsのCopilotを使ってアプリを作ります：

1. [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst)のホーム画面にアクセスします。

1. ホーム画面のテキストエリアに作りたいアプリを説明します。例えば、<strong>_学生課題を追跡・管理するアプリを作りたい_</strong>などです。<strong>送信</strong>ボタンをクリックしてAI Copilotにプロンプトを送ります。

![作りたいアプリを説明する](../../../translated_images/ja/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. AI Copilotは必要なデータを保存するためのDataverseテーブルのフィールドとサンプルデータを提案します。その後、対話ステップを通じてAI Copilotアシスタント機能でテーブルをカスタマイズできます。

   > <strong>重要</strong>：DataverseはPower Platformの基盤となるデータプラットフォームです。アプリのデータを保存するためのローコードデータプラットフォームで、Microsoftクラウド内で安全に管理され、Power Platform環境内にプロビジョニングされます。データ分類、データ系統、詳細なアクセス制御などのデータガバナンス機能も備えています。詳細は[こちら](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko)をご覧ください。

   ![新しいテーブルに提案されたフィールド](../../../translated_images/ja/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. 教育者は課題を提出した学生に進捗状況をメールで伝えたいと考えています。Copilotを使って学生のメールを保存する新しいフィールドをテーブルに追加できます。例えば、<strong>_学生のメールを保存する列を追加したい_</strong>とプロンプトして、<strong>送信</strong>ボタンをクリックします。

![新しいフィールドの追加](../../../translated_images/ja/copilot-new-column.35e15ff21acaf274.webp)

1. AI Copilotが新しいフィールドを生成し、その後あなたのニーズに合わせてフィールドをカスタマイズできます。


1. テーブルの編集が完了したら、**Create app** ボタンをクリックしてアプリを作成します。

1. AI Copilot があなたの説明に基づいてレスポンシブな Canvas アプリを生成します。その後、ニーズに合わせてアプリをカスタマイズできます。

1. 教育者が学生にメールを送るために、Copilot を使ってアプリに新しい画面を追加できます。たとえば、次のプロンプトを使ってアプリに新しい画面を追加できます：**_学生にメールを送る画面を追加したい_**。**Send** ボタンをクリックしてプロンプトを AI Copilot に送信します。

![Adding a new screen via a prompt instruction](../../../translated_images/ja/copilot-new-screen.2e0bef7132a17392.webp)

1. AI Copilot が新しい画面を生成し、その後、あなたのニーズに合わせて画面をカスタマイズできます。

1. アプリの作成が完了したら、**Save** ボタンをクリックしてアプリを保存します。

1. 教育者とアプリを共有するには、**Share** ボタンをクリックし、その後再度 **Share** ボタンをクリックします。次に、教育者のメールアドレスを入力してアプリを共有できます。

> <strong>宿題</strong>: いま作成したアプリは良い出発点ですが、改善の余地があります。メール機能では、教育者が学生のメールアドレスを手入力して手動でメールを送るしかありません。Copilot を使って、学生が課題を提出したときに教育者が自動的にメールを送れるような自動化を構築できますか？ヒントとして、適切なプロンプトを使えば、Power Automate の Copilot でこれを構築できます。

### スタートアップのための請求書情報テーブルの作成

私たちのスタートアップの財務チームは請求書の管理に苦労しています。彼らはいまスプレッドシートを使って請求書を追跡していますが、請求書の数が増えるにつれて管理が難しくなっています。彼らは請求書の情報を保存、追跡、管理するためのテーブルの作成を依頼しました。このテーブルは、すべての請求書情報を抽出して保存する自動化を構築するために使用されるべきです。また、支払い済みの請求書と未払いの請求書を財務チームが閲覧できるようにする必要があります。

Power Platform には Dataverse という基盤データプラットフォームがあり、アプリやソリューションのデータを保存できます。Dataverse は低コードのデータプラットフォームで、アプリのデータを安全にマイクロソフトクラウドに保存し、Power Platform 環境内でプロビジョニングされるフルマネージドサービスです。データ分類、データ系統、細かいアクセス制御などの組み込みのデータガバナンス機能も備えています。[Dataverse についての詳細はこちら](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko)をご覧ください。

なぜスタートアップのために Dataverse を使うべきなのでしょうか？Dataverse の標準およびカスタムテーブルは、安全なクラウドベースのデータ保存オプションを提供します。テーブルは、複数の Excel ワークブックのシートのように、異なるタイプのデータを保存できます。組織やビジネスのニーズに特化したデータを保存するためにテーブルを使えます。スタートアップが Dataverse を使うことで得られるメリットには以下のようなものがありますが、これに限りません：

- <strong>管理が容易</strong>: メタデータもデータもクラウドに保存されるため、保存や管理の細部を気にする必要がありません。アプリやソリューションの構築に集中できます。

- <strong>安全</strong>: Dataverse は安全なクラウドベースの保存オプションを提供します。役割ベースのセキュリティにより、誰がどのようにデータにアクセスできるかを制御できます。

- <strong>リッチなメタデータ</strong>: データ型やリレーションシップが Power Apps 内で直接使われます。

- <strong>論理と検証</strong>: ビジネスルール、計算フィールド、検証ルールを使ってビジネスロジックを適用し、データの正確性を保てます。

Dataverse とは何か、なぜ使うべきかがわかったところで、財務チームの要件を満たすために Copilot を使って Dataverse にテーブルを作成する方法を見てみましょう。

> <strong>注意</strong> : 次のセクションで、このテーブルを使ってすべての請求書情報を抽出しテーブルに保存する自動化を構築します。

Copilot を使って Dataverse にテーブルを作成するには、以下の手順に従います：

1. [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) ホーム画面に移動します。

2. 左のナビゲーションバーで **Tables** を選択し、続いて **Describe the new Table** をクリックします。

![Select new table](../../../translated_images/ja/describe-new-table.0792373eb757281e.webp)

1. **Describe the new Table** 画面で、作成したいテーブルの説明をテキストエリアに入力します。たとえば、**_請求書情報を保存するテーブルを作成したい_** と入力します。**Send** ボタンをクリックしてプロンプトを AI Copilot に送信します。

![Describe the table](../../../translated_images/ja/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. AI Copilot が、追跡したいデータを保存するために必要なフィールドを備えた Dataverse テーブルを提案し、サンプルデータも提供します。その後、対話形式の AI Copilot アシスタント機能を使ってテーブルをカスタマイズできます。

![Suggested Dataverse table](../../../translated_images/ja/copilot-dataverse-table.b3bc936091324d9d.webp)

1. 財務チームはサプライヤーに請求書の状況をメールで通知したいと考えています。Copilot を使って、サプライヤーのメールアドレスを保存する新しいフィールドをテーブルに追加できます。たとえば、次のプロンプトを使います：**_サプライヤーのメールを保存する列を追加したい_**。**Send** ボタンをクリックしてプロンプトを AI Copilot に送信します。

1. AI Copilot が新しいフィールドを生成し、その後、ニーズに応じてフィールドをカスタマイズできます。

1. テーブルの編集が完了したら、**Create** ボタンをクリックしてテーブルを作成します。

## Power Platform における AI モデルと AI Builder

AI Builder は Power Platform で利用できる低コード AI 機能で、AI モデルを使ってプロセスの自動化や結果予測を行えます。AI Builder により、Dataverse や SharePoint、OneDrive、Azure などのクラウドデータソースに接続しているアプリやフローに AI を組み込めます。

## 既製 AI モデルとカスタム AI モデルの違い

AI Builder には 2 種類の AI モデルがあります：既製 AI モデルとカスタム AI モデルです。既製 AI モデルは Microsoft によって訓練され、Power Platform で利用できるすぐに使えるモデルです。これにより、自分でデータを収集し、モデルを構築、訓練、公開することなく、アプリやフローにインテリジェンスを追加できます。自動化や結果予測に利用可能です。

Power Platform で利用可能な既製 AI モデルの例には以下があります：

- <strong>キーフレーズ抽出</strong>: テキストからキーフレーズを抽出します。
- <strong>言語検出</strong>: テキストの言語を検出します。
- <strong>感情分析</strong>: テキストの感情がポジティブ、ネガティブ、ニュートラル、混合のどれかを検出します。
- <strong>名刺リーダー</strong>: 名刺から情報を抽出します。
- <strong>テキスト認識</strong>: 画像からテキストを抽出します。
- <strong>物体検出</strong>: 画像から物体を検出し抽出します。
- <strong>ドキュメント処理</strong>: フォームから情報を抽出します。
- <strong>請求書処理</strong>: 請求書から情報を抽出します。

カスタム AI モデルでは、自分のモデルを AI Builder に導入し、AI Builder のカスタムモデルとして機能させ、自分のデータで訓練できます。これにより、Power Apps や Power Automate でプロセスの自動化や結果予測が可能です。自分のモデルを使う場合はいくつか制限が適用されます。これらの[制限の詳細](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst)を参照してください。

![AI builder models](../../../translated_images/ja/ai-builder-models.8069423b84cfc47f.webp)

## 課題 #2 - スタートアップのための請求書処理フローの構築

財務チームは請求書の処理に苦労しています。請求書を追跡するためにスプレッドシートを使用していましたが、請求書の数が増え管理が難しくなっています。AI を使って請求書処理を支援するワークフローの構築を依頼されました。このワークフローは、請求書から情報を抽出し Dataverse テーブルに保存できるようにする必要があります。また、抽出した情報を含むメールを財務チームに送信できるようにする必要もあります。

AI Builder が何であるか、なぜ使うべきかがわかったので、前述の請求書処理 AI モデルを使って財務チームの請求書処理を支援するワークフローをどのように構築するか見てみましょう。

請求書処理 AI モデルを使ってワークフローを構築するには、以下の手順に従います：

1. [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst) ホーム画面に移動します。

2. ホーム画面のテキストエリアに作成したいワークフローの説明を入力します。例えば、**_受信トレイに請求書が届いたら請求書を処理する_** と入力します。**Send** ボタンをクリックしてプロンプトを AI Copilot に送信します。

   ![Copilot power automate](../../../translated_images/ja/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. AI Copilot は自動化したいタスクを実現するためのアクションを提案します。**Next** ボタンをクリックして次のステップを進めます。

4. 次のステップで Power Automate はフローに必要な接続設定を促します。設定が完了したら、**Create flow** ボタンをクリックしてフローを作成します。

5. AI Copilot によりフローが生成され、その後ニーズに合わせてカスタマイズできます。

6. フローのトリガーを更新し、請求書が保存されるフォルダーを **Folder** に設定します。例えば、**Inbox** に設定します。**Show advanced options** をクリックして **Only with Attachments** を **Yes** に設定します。これにより、添付ファイル付きのメールがフォルダーに届いた時のみフローが動作します。

7. 次のアクションをフローから削除します：**HTML to text**、**Compose**、**Compose 2**、**Compose 3**、**Compose 4**。これらは使用しません。

8. **Condition** アクションもフローから削除してください。以下のスクリーンショットのようになります：

   ![power automate, remove actions](../../../translated_images/ja/powerautomate-remove-actions.7216392fe684ceba.webp)

9. **Add an action** ボタンをクリックし **Dataverse** を検索します。**Add a new row** アクションを選択します。

10. **Extract Information from invoices** アクションで、**Invoice File** をメールの **Attachment Content** を指すように更新します。これにより、請求書の添付ファイルから情報を抽出します。

11. 先ほど作成した **Table** を選択します。例えば **Invoice Information** テーブルを選べます。前のアクションからの動的コンテンツを使い以下のフィールドを設定します：

    - ID
    - Amount
    - Date
    - Name
    - Status - **Status** を **Pending** に設定します。
    - Supplier Email - **When a new email arrives** トリガーの **From** 動的コンテンツを使用します。

    ![power automate add row](../../../translated_images/ja/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. フローの編集が完了したら、**Save** ボタンをクリックしてフローを保存します。トリガーで指定したフォルダーに請求書付きのメールを送信してフローをテストできます。

> <strong>宿題</strong>: 今構築したフローは良い出発点です。次に、財務チームが請求書の現在の状況をサプライヤーにメールで通知できる自動化をどのように作成できるか考えてください。ヒント：請求書のステータスが変わったときにフローが実行される必要があります。

## Power Automate でテキスト生成 AI モデルを使う

AI Builder の GPT テキスト生成 AI モデルは、プロンプトに基づいてテキストを生成し、Microsoft Azure OpenAI サービスを利用しています。この機能により、GPT（Generative Pre-Trained Transformer）技術をアプリやフローに組み込み、さまざまな自動化フローや有益なアプリケーションを構築できます。

GPT モデルは膨大なデータで学習されており、プロンプトに応じて人間の言語に似たテキストを生成できます。ワークフロー自動化と統合することで、GPT のような AI モデルは多様なタスクの効率化と自動化に活用可能です。

例えば、メールの下書きや商品説明など、さまざまな用途向けに自動でテキストを生成するフローを構築できます。また、チャットボットやカスタマーサービスアプリで、顧客の問い合わせに効果的かつ効率的に対応できるようにするためのテキスト生成にも利用可能です。

![create a prompt](../../../translated_images/ja/create-prompt-gpt.69d429300c2e870a.webp)


Power AutomateでこのAIモデルの使い方を学ぶには、[Add intelligence with AI Builder and GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko) モジュールを通して学習してください。

## 素晴らしい！学習を続けましょう

このレッスンを終えたら、[Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) をチェックして、生成AIの知識をさらに高めましょう！

Copilotをカスタマイズしてもっと活用したいですか？GitHub Copilotを最大限に活用するための指示、エージェント、スキル、設定が集まったコミュニティ貢献のコレクション [Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) をご覧ください。

レッスン11に進み、[Function Callingとの統合で生成AIを活用する方法](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst) を見ていきましょう！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->