<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-05-20T02:32:07+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "tw"
}
-->
# 神經網路介紹：感知器

1957年，康奈爾航空實驗室的Frank Rosenblatt首次嘗試實現類似現代神經網路的技術。這是一個名為"Mark-1"的硬體實現，設計用來識別基本幾何圖形，如三角形、正方形和圓形。

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> 圖片來源：維基百科

輸入圖像由20x20的光電池陣列表示，因此神經網路有400個輸入和一個二進制輸出。一個簡單的網路包含一個神經元，也稱為**閾值邏輯單元**。神經網路的權重就像電位器，在訓練階段需要手動調整。

> ✅ 電位器是一種允許用戶調整電路阻抗的裝置。

> 當時《紐約時報》這樣描述感知器：*這是一種電子計算機的胚胎，海軍預期它將能夠行走、說話、看、寫、自我複製並意識到自己的存在。*

## 感知器模型

假設我們的模型中有N個特徵，則輸入向量將是大小為N的向量。感知器是一種**二元分類**模型，即可以區分兩類輸入數據。我們假設對於每個輸入向量x，我們的感知器輸出將是+1或-1，這取決於類別。輸出將使用以下公式計算：

y(x) = f(w<sup>T</sup>x)

其中f是一個階梯激活函數

## 訓練感知器

為了訓練感知器，我們需要找到一個權重向量w，使得大多數值能被正確分類，即導致最小的**誤差**。這個誤差由**感知器準則**定義如下：

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

其中：

* 求和針對那些導致錯誤分類的訓練數據點i
* x<sub>i</sub>是輸入數據，t<sub>i</sub>對於負例和正例分別為-1或+1。

這個準則被認為是權重w的函數，我們需要最小化它。通常使用一種稱為**梯度下降**的方法，我們從一些初始權重w<sup>(0)</sup>開始，然後在每一步中根據以下公式更新權重：

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

這裡η是所謂的**學習率**，∇E(w)表示E的**梯度**。計算完梯度後，我們得到

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Python中的算法如下：

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

在這節課中，你學習了感知器，一種二元分類模型，以及如何通過使用權重向量來訓練它。

## 🚀 挑戰

如果你想嘗試構建自己的感知器，可以嘗試在Microsoft Learn上的這個實驗，使用Azure ML設計器。

## 審查與自學

要了解如何使用感知器解決玩具問題以及現實問題，並繼續學習 - 請參考感知器筆記本。

這裡還有一篇有趣的關於感知器的文章。

## 作業

在這節課中，我們實現了一個用於二元分類任務的感知器，並使用它來區分兩個手寫數字。在這個實驗中，你需要完全解決數字分類問題，即確定哪個數字最有可能對應於給定的圖像。

* 指導說明
* 筆記本

**免責聲明**：

本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯的。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵信息，建議尋求專業的人工作翻譯。我們對於因使用此翻譯而產生的任何誤解或誤讀不承擔責任。