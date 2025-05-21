<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-05-20T02:10:00+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "en"
}
-->
# Introduction to Neural Networks. Multi-Layered Perceptron

In the previous section, you learned about the simplest neural network model - a one-layered perceptron, which is a linear two-class classification model.

In this section, we will expand this model into a more flexible framework, allowing us to:

* perform **multi-class classification** in addition to two-class
* solve **regression problems** in addition to classification
* separate classes that are not linearly separable

We will also develop our own modular framework in Python that will enable us to construct various neural network architectures.

## Formalization of Machine Learning

Let's begin by formalizing the Machine Learning problem. Suppose we have a training dataset **X** with labels **Y**, and we need to build a model *f* that will make the most accurate predictions. The quality of predictions is measured by the **Loss function** ℒ. The following loss functions are often used:

* For regression problems, when we need to predict a number, we can use **absolute error** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, or **squared error** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* For classification, we use **0-1 loss** (which is essentially the same as the **accuracy** of the model), or **logistic loss**.

For a one-level perceptron, function *f* was defined as a linear function *f(x)=wx+b* (here *w* is the weight matrix, *x* is the vector of input features, and *b* is the bias vector). For different neural network architectures, this function can take a more complex form.

> In the case of classification, it is often desirable to get probabilities of corresponding classes as network output. To convert arbitrary numbers to probabilities (e.g., to normalize the output), we often use the **softmax** function σ, and the function *f* becomes *f(x)=σ(wx+b)*

In the definition of *f* above, *w* and *b* are called **parameters** θ=⟨*w,b*⟩. Given the dataset ⟨**X**,**Y**⟩, we can compute an overall error on the whole dataset as a function of parameters θ.

> ✅ **The goal of neural network training is to minimize the error by varying parameters θ**

## Gradient Descent Optimization

There is a well-known method of function optimization called **gradient descent**. The idea is that we can compute a derivative (in multi-dimensional cases called **gradient**) of the loss function with respect to parameters, and vary parameters in such a way that the error would decrease. This can be formalized as follows:

* Initialize parameters with some random values w<sup>(0)</sup>, b<sup>(0)</sup>
* Repeat the following step many times:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

During training, the optimization steps are supposed to be calculated considering the whole dataset (remember that loss is calculated as a sum through all training samples). However, in real life, we take small portions of the dataset called **minibatches**, and calculate gradients based on a subset of data. Because the subset is taken randomly each time, such a method is called **stochastic gradient descent** (SGD).

## Multi-Layered Perceptrons and Backpropagation

A one-layer network, as we have seen above, is capable of classifying linearly separable classes. To build a richer model, we can combine several layers of the network. Mathematically, it would mean that the function *f* would have a more complex form and will be computed in several steps:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Here, α is a **non-linear activation function**, σ is a softmax function, and parameters θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

The gradient descent algorithm would remain the same, but it would be more difficult to calculate gradients. Given the chain differentiation rule, we can calculate derivatives as:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ The chain differentiation rule is used to calculate derivatives of the loss function with respect to parameters.

Note that the left-most part of all those expressions is the same, and thus we can effectively calculate derivatives starting from the loss function and going "backwards" through the computational graph. Thus the method of training a multi-layered perceptron is called **backpropagation**, or 'backprop'.

> TODO: image citation

> ✅ We will cover backprop in much more detail in our notebook example.

## Conclusion

In this lesson, we have built our own neural network library, and we have used it for a simple two-dimensional classification task.

## 🚀 Challenge

In the accompanying notebook, you will implement your own framework for building and training multi-layered perceptrons. You will be able to see in detail how modern neural networks operate.

Proceed to the OwnFramework notebook and work through it.

## Review & Self Study

Backpropagation is a common algorithm used in AI and ML, worth studying in more detail.

## Assignment

In this lab, you are asked to use the framework you constructed in this lesson to solve MNIST handwritten digit classification.

* Instructions
* Notebook

Certainly! Here's the translation of the text to English:

**Disclaimer**:  
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.