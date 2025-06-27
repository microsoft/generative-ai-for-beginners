<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-06-25T23:36:02+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "hk"
}
-->
# 神經網絡簡介：感知器

1957年，康奈爾航空實驗室的 Frank Rosenblatt 首次嘗試實現類似現代神經網絡的東西。這是一個名為 "Mark-1" 的硬件實現，設計用來識別基本的幾何圖形，如三角形、正方形和圓形。

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> 圖片來源：維基百科

輸入圖像由 20x20 的光電池陣列表示，因此神經網絡有 400 個輸入和一個二元輸出。簡單的網絡包含一個神經元，也被稱為**閾值邏輯單元**。神經網絡的權重就像電位計，在訓練階段需要手動調整。

> ✅ 電位計是一種允許用戶調整電路電阻的設備。

> 《紐約時報》當時這樣寫道：*這是一種電子計算機的胚胎，[海軍] 期望它能夠行走、說話、看見、寫作、自我複製並意識到自己的存在。*

## 感知器模型

假設我們的模型中有 N 個特徵，在這種情況下，輸入向量將是一個大小為 N 的向量。感知器是一種**二元分類**模型，即可以區分兩類輸入數據。我們假設對於每個輸入向量 x，感知器的輸出將根據類別為 +1 或 -1。輸出將使用以下公式計算：

y(x) = f(w<sup>T</sup>x)

其中 f 是一個階躍激活函數

## 訓練感知器

為了訓練感知器，我們需要找到一個權重向量 w，使其能夠正確分類大多數值，即產生最小的**錯誤**。這個錯誤由**感知器準則**定義如下：

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

其中：

* 和是針對那些導致錯誤分類的訓練數據點 i
* x<sub>i</sub> 是輸入數據，t<sub>i</sub> 對於負例和正例分別為 -1 或 +1。

這個準則被視為權重 w 的一個函數，我們需要將其最小化。通常使用一種稱為**梯度下降**的方法，我們從一些初始權重 w<sup>(0)</sup> 開始，然後在每一步根據以下公式更新權重：

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

這裡 η 被稱為**學習率**，∇E(w) 表示 E 的**梯度**。計算梯度後，我們得到：

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Python 中的算法如下所示：

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

在本課中，您學習了感知器，一種二元分類模型，以及如何使用權重向量來訓練它。

## 🚀 挑戰

如果您想嘗試建立自己的感知器，請嘗試 Microsoft Learn 上的這個實驗室，該實驗室使用 Azure ML 設計器

## 回顧與自學

要了解我們如何使用感知器來解決玩具問題以及現實生活中的問題，並繼續學習 - 請參考感知器筆記本。

這裡還有一篇有關感知器的有趣文章。

## 作業

在本課中，我們實現了一個用於二元分類任務的感知器，並使用它來區分兩個手寫數字。在這個實驗室中，您需要完全解決數字分類問題，即確定哪個數字最有可能對應於給定的圖像。

* 指示
* 筆記本

**免責聲明**：
本文件已使用AI翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)進行翻譯。儘管我們努力確保準確性，請注意自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。