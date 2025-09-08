<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-07-09T16:54:48+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "mo"
}
-->
# 神經網路入門：感知器

1957 年，康乃爾航空實驗室的 Frank Rosenblatt 首次嘗試實現類似現代神經網路的東西。這是一個名為「Mark-1」的硬體實作，設計用來辨識基本幾何圖形，如三角形、正方形和圓形。

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> 圖片來源：Wikipedia

輸入影像由 20x20 的光電池陣列表示，因此神經網路有 400 個輸入和一個二元輸出。簡單的網路包含一個神經元，也稱為**閾值邏輯單元**。神經網路的權重就像電位器，在訓練階段需要手動調整。

> ✅ 電位器是一種讓使用者調整電路阻抗的裝置。

> 《紐約時報》當時報導感知器：「這是電子電腦的胚胎，[海軍]期望它能行走、說話、看見、書寫、自我複製並意識到自己的存在。」

## 感知器模型

假設模型中有 N 個特徵，輸入向量就是大小為 N 的向量。感知器是一種**二元分類**模型，也就是能區分兩類輸入資料。我們假設對每個輸入向量 x，感知器的輸出為 +1 或 -1，取決於類別。輸出透過以下公式計算：

y(x) = f(w<sup>T</sup>x)

其中 f 是階躍激活函數

## 感知器訓練

要訓練感知器，我們需要找到一組權重向量 w，使大多數資料能被正確分類，也就是使**誤差**最小。此誤差由**感知器準則**定義如下：

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

其中：

* 求和是針對那些被錯誤分類的訓練資料點 i
* x<sub>i</sub> 是輸入資料，t<sub>i</sub> 是對應的標籤，負例為 -1，正例為 +1

此準則視為權重 w 的函數，我們需要將其最小化。通常使用一種稱為**梯度下降**的方法，從初始權重 w<sup>(0)</sup> 開始，然後每一步根據以下公式更新權重：

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

其中 η 是所謂的**學習率**，∇E(w) 表示 E 的**梯度**。計算梯度後，我們得到：

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Python 中的演算法如下：

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

本課程介紹了感知器，一種二元分類模型，以及如何透過權重向量來訓練它。

## 🚀 挑戰

如果你想嘗試自己建立感知器，可以試試 Microsoft Learn 上使用 Azure ML designer 的這個實驗室


## 複習與自學

想了解如何用感知器解決玩具問題和實際問題，並繼續學習，請參考 Perceptron 筆記本。

這裡也有一篇關於感知器的有趣文章。

## 作業

本課程中，我們實作了用於二元分類任務的感知器，並用它來區分兩個手寫數字。在這個實驗室中，你需要完整解決數字分類問題，也就是判斷給定影像最可能對應哪個數字。

* 說明
* 筆記本

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。