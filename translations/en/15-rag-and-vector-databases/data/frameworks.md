<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-07-09T16:24:16+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "en"
}
-->
# Neural Network Frameworks

As we have already learned, to train neural networks efficiently, we need to do two things:

* Work with tensors, for example, to multiply, add, and compute functions like sigmoid or softmax
* Calculate gradients of all expressions to perform gradient descent optimization

While the `numpy` library can handle the first part, we need a way to compute gradients. In the framework we developed in the previous section, we had to manually program all derivative functions inside the `backward` method, which performs backpropagation. Ideally, a framework should allow us to compute gradients of *any expression* we define.

Another key aspect is the ability to run computations on GPUs or other specialized hardware like TPUs. Training deep neural networks requires *a lot* of computation, so being able to parallelize these operations on GPUs is crucial.

> ✅ The term 'parallelize' means distributing computations across multiple devices.

Currently, the two most popular neural network frameworks are TensorFlow and PyTorch. Both provide low-level APIs to work with tensors on CPU and GPU. On top of these low-level APIs, there are higher-level APIs called Keras and PyTorch Lightning, respectively.

Low-Level API | TensorFlow | PyTorch
--------------|------------|---------
High-level API| Keras      | PyTorch Lightning

**Low-level APIs** in both frameworks let you build **computational graphs**. These graphs define how to compute outputs (usually the loss function) from given inputs and can be executed on GPUs if available. There are functions to differentiate these graphs and compute gradients, which are then used to optimize model parameters.

**High-level APIs** treat neural networks as a **sequence of layers**, making it much easier to build most neural networks. Training typically involves preparing the data and then calling a `fit` function to start the process.

The high-level API lets you quickly build typical neural networks without worrying about many details. Meanwhile, the low-level API offers much more control over training, which is why it’s often used in research when experimenting with new network architectures.

It’s also important to know you can combine both APIs. For example, you can create your own network layer architecture using the low-level API and then use it within a larger network built and trained with the high-level API. Or you can define a network with the high-level API as a sequence of layers and then use your own low-level training loop for optimization. Both APIs share the same core concepts and are designed to work well together.

## Learning

In this course, we provide most content for both PyTorch and TensorFlow. You can choose your preferred framework and follow only the corresponding notebooks. If you’re unsure which to pick, check out online discussions about **PyTorch vs. TensorFlow**. You can also explore both frameworks to get a better understanding.

Where possible, we’ll use High-Level APIs for simplicity. However, we believe it’s important to understand how neural networks work from the ground up, so we start by working with low-level APIs and tensors. If you want to get started quickly and don’t want to spend much time on these details, you can skip ahead to the high-level API notebooks.

## ✍️ Exercises: Frameworks

Continue your learning in the following notebooks:

Low-Level API | TensorFlow+Keras Notebook | PyTorch
--------------|----------------------------|---------
High-level API| Keras                      | *PyTorch Lightning*

After mastering the frameworks, let’s review the concept of overfitting.

# Overfitting

Overfitting is a crucial concept in machine learning, and it’s very important to understand it well!

Consider the problem of approximating 5 points (marked as `x` on the graphs below):

!linear | overfit
-------------------------|--------------------------
**Linear model, 2 parameters** | **Non-linear model, 7 parameters**
Training error = 5.3 | Training error = 0
Validation error = 5.1 | Validation error = 20

* On the left, we see a good straight-line approximation. Because the number of parameters is appropriate, the model captures the general pattern behind the points.
* On the right, the model is too complex. With only 5 points but 7 parameters, it can fit all points exactly, resulting in zero training error. However, this prevents the model from learning the true underlying pattern, causing a very high validation error.

It’s essential to find the right balance between the model’s complexity (number of parameters) and the amount of training data.

## Why overfitting happens

  * Not enough training data
  * Model is too complex
  * Too much noise in the input data

## How to detect overfitting

As shown in the graph above, overfitting can be detected by very low training error combined with high validation error. Typically, during training, both training and validation errors decrease at first, but at some point, the validation error stops decreasing and starts to rise. This signals overfitting and indicates that training should probably be stopped at this point (or at least save a snapshot of the model).

overfitting

## How to prevent overfitting

If you notice overfitting, you can try one of the following:

 * Increase the amount of training data
 * Reduce the model’s complexity
 * Use regularization techniques like Dropout, which we will cover later

## Overfitting and the Bias-Variance Tradeoff

Overfitting is a specific case of a broader statistical problem called the Bias-Variance Tradeoff. When considering sources of error in our model, there are two types:

* **Bias errors** occur when the algorithm can’t capture the relationship in the training data properly. This usually happens when the model is too simple (**underfitting**).
* **Variance errors** happen when the model fits noise in the input data instead of the true relationship (**overfitting**).

During training, bias error decreases as the model learns, but variance error increases. It’s important to stop training—either manually (when overfitting is detected) or automatically (using regularization)—to avoid overfitting.

## Conclusion

In this lesson, you learned about the differences between the various APIs in the two most popular AI frameworks, TensorFlow and PyTorch. You also covered an important topic: overfitting.

## 🚀 Challenge

In the accompanying notebooks, you’ll find 'tasks' at the end; work through the notebooks and complete these tasks.

## Review & Self Study

Research the following topics:

- TensorFlow
- PyTorch
- Overfitting

Ask yourself:

- What are the differences between TensorFlow and PyTorch?
- How do overfitting and underfitting differ?

## Assignment

In this lab, you are asked to solve two classification problems using single- and multi-layer fully connected networks with either PyTorch or TensorFlow.

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.