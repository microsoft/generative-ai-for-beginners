<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-07-09T16:55:19+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "ja"
}
-->
# ニューラルネットワーク入門：パーセプトロン

現代のニューラルネットワークに似たものを初めて実装しようとした試みの一つは、1957年にコーネル航空研究所のフランク・ローゼンブラットによって行われました。これは「Mark-1」と呼ばれるハードウェア実装で、三角形、四角形、円などの原始的な幾何学図形を認識するよう設計されていました。

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> 画像はWikipediaより

入力画像は20×20の光電池アレイで表されていたため、ニューラルネットワークは400の入力と1つの二値出力を持っていました。シンプルなネットワークは1つのニューロン、別名**しきい値論理ユニット**を含んでいました。ニューラルネットワークの重みはポテンショメータのように機能し、トレーニング段階で手動調整が必要でした。

> ✅ ポテンショメータとは、回路の抵抗値を調整できる装置のことです。

> 当時のニューヨーク・タイムズはパーセプトロンについてこう書いています：*海軍が期待する電子計算機の胚胎であり、歩き、話し、見て、書き、自己複製し、自分の存在を意識できるようになるだろう。*

## パーセプトロンモデル

モデルにN個の特徴量があるとすると、入力ベクトルはサイズNのベクトルになります。パーセプトロンは**二値分類**モデルであり、2つのクラスの入力データを区別できます。各入力ベクトルxに対して、パーセプトロンの出力はクラスに応じて+1か-1のいずれかになると仮定します。出力は次の式で計算されます：

y(x) = f(w<sup>T</sup>x)

ここでfはステップ関数（活性化関数）です。

## パーセプトロンの学習

パーセプトロンを学習させるには、ほとんどの値を正しく分類する重みベクトルwを見つける必要があります。つまり、**誤差**を最小にすることが目標です。この誤差は**パーセプトロン基準**によって次のように定義されます：

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

ここで：

* 和は誤分類した訓練データ点iに対して取られます
* x<sub>i</sub>は入力データ、t<sub>i</sub>は負例と正例に応じてそれぞれ-1または+1です

この基準は重みwの関数とみなされ、これを最小化する必要があります。よく使われる方法は**勾配降下法**で、初期重みw<sup>(0)</sup>から始め、各ステップで次の式に従って重みを更新します：

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

ここでηは**学習率**、∇E(w)はEの**勾配**を表します。勾配を計算すると、次のようになります：

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Pythonでのアルゴリズムは以下の通りです：

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # Initialize weights (almost randomly :)
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # compute perceptron output
        if z < 0: # positive example classified as negative
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # negative example classified as positive
            weights = weights - eta*weights.shape

    return weights
```

## まとめ

このレッスンでは、二値分類モデルであるパーセプトロンと、その重みベクトルを使った学習方法について学びました。

## 🚀 チャレンジ

自分でパーセプトロンを作ってみたい方は、Azure MLデザイナーを使ったMicrosoft Learnのこのラボに挑戦してみてください。

## 復習と自主学習

パーセプトロンを使っておもちゃの問題や実際の問題を解く方法を学び続けたい方は、Perceptronノートブックへ進んでください。

パーセプトロンに関する興味深い記事もあります。

## 課題

このレッスンでは、二値分類タスクのためのパーセプトロンを実装し、2つの手書き数字を分類するのに使いました。このラボでは、数字分類の問題を完全に解決すること、つまり与えられた画像に最も適した数字を判定することに挑戦します。

* 指示
* ノートブック

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねます。