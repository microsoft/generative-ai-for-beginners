<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-05-20T02:31:52+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "hk"
}
-->
# 神經網絡簡介：感知器

1957年，康奈爾航空實驗室的Frank Rosenblatt嘗試實現類似於現代神經網絡的東西。他的硬件實現被稱為"Mark-1"，設計用來識別簡單幾何圖形，如三角形、正方形和圓形。

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> 圖片來自維基百科

輸入圖像由20x20光電池陣列表示，因此神經網絡有400個輸入和一個二進制輸出。簡單的網絡包含一個神經元，也被稱為**閾值邏輯單元**。神經網絡的權重像電位器一樣，需要在訓練階段手動調整。

> ✅ 電位器是一種允許用戶調節電路電阻的設備。

> 當時《紐約時報》對感知器的報導：*海軍期望能夠行走、說話、看見、寫作、自我繁殖並意識到自身存在的電子計算機的胚胎。*

## 感知器模型

假設我們的模型有N個特徵，此時輸入向量將是大小為N的向量。感知器是一個**二元分類**模型，即它可以區分兩類輸入數據。我們將假設對於每個輸入向量x，感知器的輸出將是+1或-1，取決於類別。輸出將使用以下公式計算：

y(x) = f(w<sup>T</sup>x)

其中f是階躍激活函數

## 訓練感知器

要訓練感知器，我們需要找到一個權重向量w，使得大多數值能夠正確分類，即結果最小的**錯誤**。這個錯誤由**感知器標準**以以下方式定義：

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

其中：

* 求和是在那些導致錯誤分類的訓練數據點i上進行的
* x<sub>i</sub>是輸入數據，t<sub>i</sub>分別是負例和正例的-1或+1。

這個標準被認為是權重w的函數，我們需要將其最小化。通常使用一種稱為**梯度下降**的方法，我們從一些初始權重w<sup>(0)</sup>開始，然後在每一步根據公式更新權重：

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

這裡η被稱為**學習率**，而∇E(w)表示E的**梯度**。在計算梯度後，我們得到

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

在這節課中，你學到了感知器，這是一個二元分類模型，以及如何通過使用權重向量來訓練它。

## 🚀 挑戰

如果你想嘗試構建自己的感知器，可以在Microsoft Learn上試試這個使用Azure ML設計器的實驗。

## 回顧與自學

要了解我們如何使用感知器解決玩具問題以及實際問題，並繼續學習——請查看感知器筆記本。

這裡還有一篇有趣的文章關於感知器。

## 作業

在這節課中，我們實現了一個二元分類任務的感知器，並用它來區分兩個手寫數字。在這個實驗中，你需要完全解決數字分類問題，即確定哪個數字最有可能對應於給定的圖像。

* 說明
* 筆記本

**免責聲明**：

本文件已使用AI翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)進行翻譯。我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應將原始語言的文件視為權威來源。對於關鍵信息，建議使用專業的人力翻譯。我們對因使用此翻譯而產生的任何誤解或誤讀概不負責。