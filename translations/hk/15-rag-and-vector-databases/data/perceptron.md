<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-07-09T16:54:59+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "hk"
}
-->
# 神經網絡入門：感知器

1957年，康奈爾航空實驗室的Frank Rosenblatt首次嘗試實現類似現代神經網絡的東西。這是一個名為「Mark-1」的硬件實現，設計用來識別基本幾何圖形，如三角形、正方形和圓形。

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> 圖片來自維基百科

輸入圖像由20x20的光電池陣列表示，因此神經網絡有400個輸入和一個二元輸出。簡單的網絡包含一個神經元，也稱為**閾值邏輯單元**。神經網絡的權重就像電位器，在訓練階段需要手動調整。

> ✅ 電位器是一種允許用戶調節電路阻力的裝置。

> 《紐約時報》當時這樣描述感知器：*這是電子計算機的胚胎，[海軍]期望它能行走、說話、看見、書寫、自我複製並意識到自己的存在。*

## 感知器模型

假設我們的模型有N個特徵，輸入向量就是大小為N的向量。感知器是一個**二元分類**模型，即能區分兩類輸入數據。我們假設對每個輸入向量x，感知器的輸出是+1或-1，取決於類別。輸出通過以下公式計算：

y(x) = f(w<sup>T</sup>x)

其中f是階躍激活函數

## 感知器的訓練

要訓練感知器，我們需要找到一個權重向量w，使大多數數據能被正確分類，即使**錯誤**最小。這個錯誤由**感知器準則**定義如下：

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

其中：

* 求和是針對那些被錯誤分類的訓練數據點i
* x<sub>i</sub>是輸入數據，t<sub>i</sub>是對應的標籤，負例為-1，正例為+1。

這個準則被視為權重w的函數，我們需要將其最小化。通常使用一種稱為**梯度下降**的方法，從初始權重w<sup>(0)</sup>開始，然後每一步根據公式更新權重：

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

這裡η是所謂的**學習率**，∇E(w)表示E的**梯度**。計算梯度後，我們得到：

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

## 總結

本課程介紹了感知器，一種二元分類模型，以及如何通過權重向量來訓練它。

## 🚀 挑戰

如果你想嘗試自己建立感知器，可以試試Microsoft Learn上的這個實驗室，使用Azure ML設計器。

## 複習與自學

想了解如何用感知器解決玩具問題和現實問題，並繼續學習，請參考感知器筆記本。

這裡也有一篇關於感知器的有趣文章。

## 作業

本課程中，我們實現了一個用於二元分類任務的感知器，並用它來區分兩個手寫數字。在這個實驗室中，你需要完整解決數字分類問題，即判斷給定圖像最可能對應哪個數字。

* 說明
* 筆記本

**免責聲明**：  
本文件乃使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。