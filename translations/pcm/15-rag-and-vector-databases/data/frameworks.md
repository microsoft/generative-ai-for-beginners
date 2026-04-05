# Neural Network Frameworks

As we don learn already, to fit train neural networks well well, we need do two things:

* Work with tensors, like multiply, add, and calculate some functions like sigmoid or softmax
* Calculate gradients for all expressions, so we fit use am do gradient descent optimization

Even though `numpy` library fit do the first part, we need one way to calculate gradients. For the framework we don develop for the previous section, we bin dey manually program all the derivative functions inside the `backward` method wey dey do backpropagation. Ideally, framework suppose give us chance to calculate gradients for *any expression* wey we fit define.

Another important thing na to fit run calculations for GPU, or any other special compute units, like TPU. Training deep neural networks dey need *plenty* calculations, and e dey very important to fit share those calculations for GPUs.

> ✅ The word 'parallelize' mean say to share the calculations for plenty devices.

Right now, the two most popular neural frameworks na TensorFlow and PyTorch. Both dey provide low-level API to work with tensors for both CPU and GPU. On top the low-level API, e get higher-level API, wey dem dey call Keras and PyTorch Lightning.

Low-Level API | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
High-level API| Keras| Pytorch

**Low-level APIs** for both frameworks dey allow you build wetin dem dey call **computational graphs**. This graph dey show how to calculate the output (normally na the loss function) with the input parameters wey you give, and e fit run for GPU if e dey available. E get functions to differentiate this computational graph and calculate gradients, wey fit dey used to optimize model parameters.

**High-level APIs** dey see neural networks as **sequence of layers**, and e dey make am easy to build most neural networks. To train the model, you go just prepare the data and call `fit` function to do the work.

High-level API dey allow you build normal neural networks fast fast without stress about plenty details. But low-level API dey give you more control for the training process, so dem dey use am well well for research, especially when you dey work with new neural network architectures.

E dey important to understand say you fit use both APIs together. For example, you fit create your own network layer architecture with low-level API, then use am inside bigger network wey you build and train with high-level API. Or you fit define network with high-level API as sequence of layers, then use your own low-level training loop to do optimization. Both APIs dey use the same basic ideas, and dem dey designed to work well together.

## Learning

For this course, we go provide most of the content for both PyTorch and TensorFlow. You fit choose the framework wey you like and focus on the notebooks for that one. If you no sure which one to choose, you fit read discussions online about **PyTorch vs. TensorFlow**. You fit also check both frameworks to understand dem better.

Where e possible, we go use High-Level APIs to make things simple. But we believe say e dey important to understand how neural networks dey work from scratch, so we go start with low-level API and tensors. But if you wan start fast and no wan spend plenty time to learn all these details, you fit skip am and go straight to high-level API notebooks.

## ✍️ Exercises: Frameworks

Continue your learning for the notebooks wey dey below:

Low-Level API | TensorFlow+Keras Notebook | PyTorch
--------------|-------------------------------------|--------------------------------
High-level API| Keras | *PyTorch Lightning*

After you don master the frameworks, make we talk about overfitting.

# Overfitting

Overfitting na one very important thing for machine learning, and e dey very important make we understand am well!

Look this problem wey dey try to fit 5 dots (we mark am with `x` for the graphs below):

!linear | overfit
-------------------------|--------------------------
**Linear model, 2 parameters** | **Non-linear model, 7 parameters**
Training error = 5.3 | Training error = 0
Validation error = 5.1 | Validation error = 20

* For the left side, we see say the straight line fit the points well. Because the number of parameters dey okay, the model understand the way the points dey.
* For the right side, the model too strong. Because we only get 5 points and the model get 7 parameters, e fit adjust to pass through all the points, making training error be 0. But this one no allow the model understand the correct pattern for the data, so validation error go high.

E dey very important to balance the power of the model (number of parameters) and the number of training samples.

## Why overfitting dey happen

  * Training data no plenty
  * Model too strong
  * Input data get too much noise

## How to detect overfitting

As you see for the graph above, overfitting fit show when training error dey very low, but validation error dey high. Normally, during training, you go see both training and validation errors dey reduce, but at one point validation error fit stop to reduce and start to rise. This one na sign of overfitting, and e mean say we suppose stop training for that point (or at least save the model snapshot).

overfitting

## How to prevent overfitting

If you see say overfitting dey happen, you fit do one of these:

 * Add more training data
 * Reduce the complexity of the model
 * Use regularization techniques like Dropout, wey we go talk about later.

## Overfitting and Bias-Variance Tradeoff

Overfitting na one example of one bigger problem for statistics wey dem dey call Bias-Variance Tradeoff. If we look the possible sources of error for our model, we go see two types of errors:

* **Bias errors** dey happen when our algorithm no fit capture the relationship for training data well. E fit happen because our model no strong enough (**underfitting**).
* **Variance errors**, dey happen when the model dey fit noise for the input data instead of meaningful relationship (**overfitting**).

During training, bias error dey reduce (as our model dey learn to fit the data), and variance error dey increase. E dey important to stop training - either manually (when we see overfitting) or automatically (by using regularization) - to stop overfitting.

## Conclusion

For this lesson, you don learn the difference between the different APIs for the two most popular AI frameworks, TensorFlow and PyTorch. You don also learn about one very important topic, overfitting.

## 🚀 Challenge

For the notebooks wey follow, you go see 'tasks' for the bottom; work through the notebooks and complete the tasks.

## Review & Self Study

Do small research for these topics:

- TensorFlow
- PyTorch
- Overfitting

Ask yourself these questions:

- Wetin be the difference between TensorFlow and PyTorch?
- Wetin be the difference between overfitting and underfitting?

## Assignment

For this lab, dem ask you to solve two classification problems using single- and multi-layered fully-connected networks with PyTorch or TensorFlow.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleto service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am correct, abeg sabi say machine translation fit get mistake or no dey accurate well. Di original dokyument wey dey for im native language na di main source wey you go trust. For important mata, e good make professional human transleto check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->