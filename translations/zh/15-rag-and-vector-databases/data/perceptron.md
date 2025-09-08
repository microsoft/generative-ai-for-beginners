<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-07-09T16:54:39+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "zh"
}
-->
# 神经网络简介：感知器

1957年，康奈尔航空实验室的Frank Rosenblatt首次尝试实现类似现代神经网络的东西。这是一个名为“Mark-1”的硬件实现，设计用于识别基本的几何图形，如三角形、正方形和圆形。

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> 图片来自维基百科

输入图像由20x20的光电池阵列表示，因此神经网络有400个输入和一个二元输出。一个简单的网络包含一个神经元，也称为**阈值逻辑单元**。神经网络的权重就像电位器，在训练阶段需要手动调整。

> ✅ 电位器是一种允许用户调节电路电阻的装置。

> 《纽约时报》当时这样描述感知器：*这是一个电子计算机的雏形，[海军]期望它能够行走、说话、看见、写作、自我复制并意识到自身的存在。*

## 感知器模型

假设我们的模型有N个特征，那么输入向量就是一个大小为N的向量。感知器是一个**二分类**模型，即它可以区分两类输入数据。我们假设对于每个输入向量x，感知器的输出是+1或-1，取决于类别。输出通过以下公式计算：

y(x) = f(w<sup>T</sup>x)

其中f是阶跃激活函数

## 感知器的训练

训练感知器需要找到一个权重向量w，使其能正确分类大多数样本，即使**误差**最小。该误差由**感知器准则**定义如下：

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

其中：

* 求和仅针对那些分类错误的训练样本i
* x<sub>i</sub>是输入数据，t<sub>i</sub>为-1或+1，分别对应负例和正例。

该准则被视为权重w的函数，我们需要对其进行最小化。通常使用一种称为**梯度下降**的方法，先从初始权重w<sup>(0)</sup>开始，然后每一步根据公式更新权重：

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

这里η是所谓的**学习率**，∇E(w)表示E的**梯度**。计算梯度后，更新公式变为：

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

## 总结

本课中，你了解了感知器——一种二分类模型，以及如何通过权重向量来训练它。

## 🚀 挑战

如果你想尝试自己构建感知器，可以试试Microsoft Learn上的这个实验，使用Azure ML设计器。

## 复习与自学

想了解如何用感知器解决玩具问题和实际问题，并继续学习，请查看感知器笔记本。

这里还有一篇关于感知器的有趣文章。

## 作业

本课中，我们实现了一个用于二分类任务的感知器，并用它对两种手写数字进行了分类。在本实验中，你需要完成整个数字分类问题，即判断给定图像最可能对应哪个数字。

* 说明
* 笔记本

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。