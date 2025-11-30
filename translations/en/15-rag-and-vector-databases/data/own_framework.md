<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-07-09T16:39:43+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "en"
}
-->
# Introduction to Neural Networks. Multi-Layered Perceptron

In the previous section, you learned about the simplest neural network model - the one-layer perceptron, a linear two-class classification model.

In this section, we will expand this model into a more flexible framework, allowing us to:

* perform **multi-class classification** in addition to two-class
* solve **regression problems** alongside classification
* separate classes that are not linearly separable

We will also develop our own modular framework in Python that will let us build different neural network architectures.

## Formalization of Machine Learning

Let's begin by formalizing the Machine Learning problem. Suppose we have a training dataset **X** with labels **Y**, and we need to build a model *f* that makes the most accurate predictions. The quality of predictions is measured by the **Loss function** ℒ. The following loss functions are commonly used:

* For regression problems, where we predict a number, we can use **absolute error** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, or **squared error** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* For classification, we use **0-1 loss** (which is essentially the same as the model’s **accuracy**), or **logistic loss**.

For the one-layer perceptron, the function *f* was defined as a linear function *f(x)=wx+b* (where *w* is the weight matrix, *x* is the input feature vector, and *b* is the bias vector). For different neural network architectures, this function can take a more complex form.

> In classification tasks, it’s often useful to get probabilities for each class as the network output. To convert arbitrary numbers into probabilities (e.g., to normalize the output), we often use the **softmax** function σ, so the function *f* becomes *f(x)=σ(wx+b)*

In the definition of *f* above, *w* and *b* are called **parameters** θ=⟨*w,b*⟩. Given the dataset ⟨**X**,**Y**⟩, we can compute the overall error on the entire dataset as a function of parameters θ.

> ✅ **The goal of neural network training is to minimize the error by adjusting parameters θ**

## Gradient Descent Optimization

A well-known method for function optimization is **gradient descent**. The idea is that we can compute the derivative (in the multi-dimensional case called the **gradient**) of the loss function with respect to the parameters, and update the parameters in a way that reduces the error. This can be formalized as:

* Initialize parameters with some random values w<sup>(0)</sup>, b<sup>(0)</sup>
* Repeat the following step many times:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup> - η ∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup> - η ∂ℒ/∂b

During training, these optimization steps are ideally calculated over the entire dataset (remember that the loss is summed over all training samples). However, in practice, we use small portions of the dataset called **minibatches**, and calculate gradients based on these subsets. Since the subsets are randomly selected each time, this method is called **stochastic gradient descent** (SGD).

## Multi-Layered Perceptrons and Backpropagation

As we saw above, a one-layer network can classify linearly separable classes. To build a more powerful model, we can stack several layers. Mathematically, this means the function *f* becomes more complex and is computed in several steps:
* z<sub>1</sub> = w<sub>1</sub>x + b<sub>1</sub>
* z<sub>2</sub> = w<sub>2</sub> α(z<sub>1</sub>) + b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Here, α is a **non-linear activation function**, σ is the softmax function, and parameters θ = ⟨*w<sub>1</sub>, b<sub>1</sub>, w<sub>2</sub>, b<sub>2</sub>*⟩.

The gradient descent algorithm remains the same, but calculating gradients becomes more complex. Using the chain rule for differentiation, we can compute derivatives as:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ The chain rule is used to calculate derivatives of the loss function with respect to parameters.

Note that the left-most part of all these expressions is the same, so we can efficiently compute derivatives starting from the loss function and moving "backwards" through the computational graph. This method of training a multi-layer perceptron is called **backpropagation**, or 'backprop'.

> TODO: image citation

> ✅ We will explore backpropagation in much more detail in our notebook example.

## Conclusion

In this lesson, we built our own neural network library and used it for a simple two-dimensional classification task.

## 🚀 Challenge

In the accompanying notebook, you will implement your own framework for building and training multi-layered perceptrons. This will give you a detailed look at how modern neural networks work.

Proceed to the OwnFramework notebook and work through it.

## Review & Self Study

Backpropagation is a fundamental algorithm in AI and ML, and it’s worth studying in more depth.

## Assignment

In this lab, you are asked to use the framework you built in this lesson to solve the MNIST handwritten digit classification task.

* Instructions
* Notebook

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.