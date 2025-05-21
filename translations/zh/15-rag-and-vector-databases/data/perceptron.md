<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-05-20T02:31:21+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "zh"
}
-->
# 神经网络入门：感知器

1957年，康奈尔航空实验室的Frank Rosenblatt首次尝试实现类似现代神经网络的东西。这是一个名为"Mark-1"的硬件实现，设计用于识别基本几何图形，如三角形、正方形和圆形。

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> 图片来源于维基百科

输入图像由20x20的光电池阵列表示，因此神经网络有400个输入和一个二进制输出。一个简单的网络包含一个神经元，也称为**阈值逻辑单元**。神经网络的权重就像电位器，在训练阶段需要手动调整。

> ✅ 电位器是一种允许用户调整电路电阻的设备。

> 《纽约时报》当时这样写道：*海军期望它能行走、交谈、看见、写作、自我复制并意识到自身存在的电子计算机的雏形。*

## 感知器模型

假设我们的模型中有N个特征，那么输入向量将是一个大小为N的向量。感知器是一个**二分类**模型，即它可以区分两类输入数据。我们将假设对于每个输入向量x，感知器的输出将是+1或-1，具体取决于类别。输出将通过以下公式计算：

y(x) = f(w<sup>T</sup>x)

其中f是阶跃激活函数

## 训练感知器

要训练感知器，我们需要找到一个权重向量w，使得大多数值能被正确分类，即导致最小的**误差**。这个误差由**感知器准则**如下定义：

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

其中：

* 求和是在那些导致错误分类的训练数据点i上进行
* x<sub>i</sub>是输入数据，t<sub>i</sub>对于负例和正例分别为-1或+1。

这个准则被视为权重w的函数，我们需要最小化它。通常使用一种称为**梯度下降**的方法，我们从一些初始权重w<sup>(0)</sup>开始，然后在每一步中根据以下公式更新权重：

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

这里η是所谓的**学习率**，∇E(w)表示E的**梯度**。计算梯度后，我们得到

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Python中的算法如下所示：

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

## 结论

在本课中，您学习了感知器，这是一种二分类模型，以及如何使用权重向量来训练它。

## 🚀 挑战

如果您想尝试构建自己的感知器，请在Microsoft Learn上尝试使用Azure ML设计器的实验。

## 复习与自学

要了解我们如何使用感知器解决玩具问题以及现实生活中的问题，并继续学习，请查看感知器笔记本。

这里还有一篇关于感知器的有趣文章。

## 作业

在本课中，我们实现了一个用于二分类任务的感知器，并使用它来区分两个手写数字。在这个实验中，您需要完全解决数字分类的问题，即确定哪个数字最有可能对应于给定的图像。

* 指导
* 笔记本

**免责声明**：
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。虽然我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原始语言的文档视为权威来源。对于关键信息，建议进行专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担责任。