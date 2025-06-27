<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-06-25T23:36:17+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "tw"
}
-->
# 神經網路簡介：感知器

最早嘗試實現類似現代神經網路的嘗試之一是由康奈爾航空實驗室的 Frank Rosenblatt 在 1957 年進行的。他設計了一個名為 "Mark-1" 的硬體，旨在識別基本的幾何圖形，如三角形、正方形和圓形。

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> 圖片來自維基百科

輸入影像由 20x20 的光電陣列表示，因此神經網路有 400 個輸入和一個二進制輸出。一個簡單的網路包含一個神經元，也稱為**閾值邏輯單元**。神經網路的權重像電位器一樣，需要在訓練階段進行手動調整。

> ✅ 電位器是一種允許使用者調整電路阻力的裝置。

> 紐約時報當時寫道：*電子計算機的胚胎，[海軍]期望它能夠行走、交談、看見、寫作、繁殖並意識到自己的存在。*

## 感知器模型

假設我們的模型中有 N 個特徵，這樣輸入向量就是一個大小為 N 的向量。感知器是一種**二元分類**模型，即它可以區分兩類輸入數據。我們假設對於每個輸入向量 x，感知器的輸出將是 +1 或 -1，這取決於類別。輸出將使用以下公式計算：

y(x) = f(w<sup>T</sup>x)

其中 f 是一個階梯激活函數

## 訓練感知器

要訓練感知器，我們需要找到一個權重向量 w，使得大多數值都能正確分類，即結果**誤差**最小。這個誤差由**感知器準則**以下述方式定義：

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

其中：

* 和是對那些導致錯誤分類的訓練數據點 i 進行的
* x<sub>i</sub> 是輸入數據，t<sub>i</sub> 對應於負面和正面例子分別是 -1 或 +1。

這個準則被視為權重 w 的函數，我們需要最小化它。通常使用一種叫做**梯度下降**的方法，其中我們從一些初始權重 w<sup>(0)</sup> 開始，然後在每一步中根據公式更新權重：

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

這裡 η 是所謂的**學習率**，∇E(w) 表示 E 的**梯度**。計算梯度後，我們得到

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Python 中的算法如下：

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

在這節課中，你學到了感知器，它是一種二元分類模型，以及如何使用權重向量來訓練它。

## 🚀 挑戰

如果你想嘗試構建自己的感知器，請嘗試在 Microsoft Learn 上使用 Azure ML 設計器進行這個實驗。

## 回顧與自學

要了解我們如何使用感知器來解決玩具問題以及現實生活中的問題，並繼續學習，請參考感知器筆記本。

這裡還有一篇關於感知器的有趣文章。

## 作業

在這節課中，我們實現了一個用於二元分類任務的感知器，並使用它來區分兩個手寫數字。在這個實驗中，你需要完全解決數字分類問題，即確定哪個數字最有可能對應於給定的圖像。

* 指導
* 筆記本

**免責聲明**：  
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯的。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應將原始文件的母語版本視為權威來源。對於關鍵信息，建議尋求專業的人類翻譯。我們對因使用本翻譯而引起的任何誤解或誤釋不承擔責任。