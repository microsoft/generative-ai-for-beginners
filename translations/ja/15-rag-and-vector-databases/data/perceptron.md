<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-05-20T02:32:24+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "ja"
}
-->
# ニューラルネットワーク入門: パーセプトロン

現代のニューラルネットワークに似たものを実装しようとした最初の試みの一つは、1957年にコーネル航空研究所のフランク・ローゼンブラットによって行われました。これは「Mark-1」と呼ばれるハードウェア実装で、三角形や四角形、円などの原始的な幾何学的図形を認識するために設計されました。

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> 画像はWikipediaより

入力画像は20x20のフォトセル配列で表現され、ニューラルネットワークは400の入力と1つのバイナリ出力を持っていました。シンプルなネットワークには1つのニューロン、つまり**しきい値論理ユニット**が含まれていました。ニューラルネットワークの重みは、訓練フェーズ中に手動で調整が必要なポテンショメータのように機能しました。

> ✅ ポテンショメータとは、回路の抵抗をユーザーが調整できるデバイスです。

> 当時、ニューヨーク・タイムズはパーセプトロンについてこう書いていました：*海軍が期待するところでは、歩き、話し、見て、書き、自己再生し、自分の存在を意識することができる電子コンピュータの胚である。*

## パーセプトロンモデル

モデルにN個の特徴があると仮定すると、入力ベクトルはサイズNのベクトルになります。パーセプトロンは**バイナリ分類**モデルであり、つまり入力データの2つのクラスを区別することができます。各入力ベクトルxに対して、パーセプトロンの出力がクラスに応じて+1または-1になると仮定します。出力は次の式を用いて計算されます：

y(x) = f(w<sup>T</sup>x)

ここでfはステップ活性化関数です

## パーセプトロンの訓練

パーセプトロンを訓練するためには、多くの値を正しく分類する重みベクトルwを見つける必要があります。つまり、最小の**エラー**をもたらします。このエラーは次のように**パーセプトロン基準**によって定義されます：

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

ここで：

* 和は誤った分類をもたらす訓練データポイントiに対して取られます
* x<sub>i</sub>は入力データで、t<sub>i</sub>は負と正の例に応じてそれぞれ-1または+1です。

この基準は重みwの関数と見なされ、これを最小化する必要があります。しばしば、**勾配降下法**と呼ばれる方法が使用されます。この方法では、いくつかの初期重みw<sup>(0)</sup>から始め、各ステップで次の式に従って重みを更新します：

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

ここでηは**学習率**と呼ばれ、∇E(w)はEの**勾配**を示します。勾配を計算した後、次のようになります：

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Pythonでのアルゴリズムは次のようになります：

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

## 結論

このレッスンでは、バイナリ分類モデルであるパーセプトロンについて学び、重みベクトルを使用して訓練する方法を学びました。

## 🚀 チャレンジ

独自のパーセプトロンを構築してみたい場合は、Azure MLデザイナーを使用したMicrosoft Learnのこのラボに挑戦してみてください。

## 復習と自己学習

パーセプトロンを使用しておもちゃの問題や現実の問題を解決する方法を見て、学習を続けるためには、パーセプトロンノートブックに進んでください。

パーセプトロンについての興味深い記事もあります。

## 課題

このレッスンでは、バイナリ分類タスクのためのパーセプトロンを実装し、2つの手書き数字を分類するために使用しました。このラボでは、数字分類の問題を完全に解決すること、つまり与えられた画像に最も対応する可能性の高い数字を特定することが求められます。

* 指示
* ノートブック

**免責事項**:
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確さを追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることにご注意ください。元の文書をその言語で読むことが正式な情報源とされるべきです。重要な情報については、プロの人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤った解釈について、当社は責任を負いません。