# 神经网络简介：感知器

1957年，康奈尔航空实验室的Frank Rosenblatt首次尝试实现类似于现代神经网络的东西。这是一个名为“Mark-1”的硬件实现，旨在识别简单的几何图形，如三角形、正方形和圆形。

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> 图片来自维基百科

输入图像由20x20的光电池阵列表示，因此神经网络有400个输入和一个二进制输出。一个简单的网络包含一个神经元，也称为**阈值逻辑单元**。神经网络的权重类似于电位计，在训练阶段需要手动调整。

> ✅ 电位计是一种允许用户调节电路电阻的设备。

> 《纽约时报》当时这样描述感知器：*一种电子计算机的胚胎，[海军]期望它能够行走、说话、看见、写字、自我复制并意识到自己的存在。*

## 感知器模型

假设我们的模型中有N个特征，此时输入向量将是大小为N的向量。感知器是一个**二元分类**模型，即它可以区分输入数据的两类。我们假设对于每个输入向量x，感知器的输出将根据类别为+1或-1。输出将使用以下公式计算：

y(x) = f(w<sup>T</sup>x)

其中f是阶跃激活函数

## 训练感知器

要训练感知器，我们需要找到一个权重向量w，使得大多数值能够被正确分类，即导致最小的**误差**。这种误差通过**感知器准则**定义如下：

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

其中：

* 求和在那些导致错误分类的训练数据点i上进行
* x<sub>i</sub>是输入数据，t<sub>i</sub>分别为负例和正例对应的-1或+1。

这个准则被视为权重w的一个函数，我们需要对其进行最小化。通常使用一种称为**梯度下降**的方法，我们从一些初始权重w<sup>(0)</sup>开始，然后在每一步根据以下公式更新权重：

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

这里η是所谓的**学习率**，∇E(w)表示E的**梯度**。在计算完梯度后，我们得到：

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

在本课中，你学习了关于感知器的知识，它是一个二元分类模型，并了解了如何通过使用权重向量对其进行训练。

## 🚀 挑战

如果你想尝试构建自己的感知器，可以在Microsoft Learn上尝试这个实验室，它使用Azure ML设计器。

## 复习与自学

要了解我们如何使用感知器解决玩具问题以及现实生活中的问题，并继续学习，请参阅感知器笔记本。

这里还有一篇关于感知器的有趣文章。

## 作业

在本课中，我们实现了一个用于二元分类任务的感知器，并使用它来区分两个手写数字。在这个实验室中，你需要完全解决数字分类问题，即确定哪个数字最有可能与给定图像对应。

* 说明
* 笔记本

**免责声明**：  
本文档是使用基于机器的AI翻译服务翻译的。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原始文档的母语版本视为权威来源。对于关键信息，建议进行专业的人类翻译。对于因使用本翻译而引起的任何误解或误释，我们概不负责。