<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-05-20T01:47:36+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "en"
}
-->
# Neural Network Frameworks

As we have learned already, to efficiently train neural networks we need to do two things:

* Operate on tensors, e.g., multiply, add, and compute functions like sigmoid or softmax
* Compute gradients of all expressions to perform gradient descent optimization

While the `numpy` library can handle the first part, we need a mechanism to compute gradients. In the framework we developed in the previous section, we had to manually program all derivative functions inside the `backward` method, which does backpropagation. Ideally, a framework should allow us to compute gradients of *any expression* we define.

Another important aspect is performing computations on GPUs or other specialized compute units like TPUs. Deep neural network training requires *a lot* of computations, and being able to parallelize these computations on GPUs is crucial.

> ✅ The term 'parallelize' means to distribute computations over multiple devices.

Currently, the two most popular neural frameworks are TensorFlow and PyTorch. Both provide a low-level API to work with tensors on both CPU and GPU. On top of the low-level API, there is also a higher-level API, called Keras and PyTorch Lightning, respectively.

Low-Level API | TensorFlow | PyTorch
--------------|------------|--------
High-Level API| Keras      | PyTorch Lightning

**Low-level APIs** in both frameworks allow you to build so-called **computational graphs**. This graph defines how to compute the output (usually the loss function) with given input parameters and can be pushed for computation on GPU if available. There are functions to differentiate this computational graph and compute gradients, which can then be used for optimizing model parameters.

**High-level APIs** generally view neural networks as a **sequence of layers**, making it much easier to construct most neural networks. Training the model usually involves preparing the data and then calling a `fit` function to do the job.

The high-level API allows you to construct typical neural networks quickly without worrying about many details. At the same time, low-level APIs offer much more control over the training process, making them widely used in research when dealing with new neural network architectures.

It is also important to understand that you can use both APIs together. For example, you can develop your own network layer architecture using a low-level API and then use it within a larger network constructed and trained with the high-level API. Or you can define a network using the high-level API as a sequence of layers and then use your own low-level training loop to perform optimization. Both APIs use the same basic underlying concepts and are designed to work well together.

## Learning

In this course, we offer most of the content for both PyTorch and TensorFlow. You can choose your preferred framework and go through the corresponding notebooks. If you are unsure which framework to choose, read some discussions on the internet about **PyTorch vs. TensorFlow**. You can also explore both frameworks to gain a better understanding.

Where possible, we will use High-Level APIs for simplicity. However, we believe it is important to understand how neural networks work from the ground up, so we start by working with low-level API and tensors. However, if you want to get started quickly and do not want to spend a lot of time learning these details, you can skip those and go straight into high-level API notebooks.

## ✍️ Exercises: Frameworks

Continue your learning in the following notebooks:

Low-Level API | TensorFlow+Keras Notebook | PyTorch
--------------|---------------------------|--------
High-Level API| Keras                     | PyTorch Lightning

After mastering the frameworks, let's revisit the concept of overfitting.

# Overfitting

Overfitting is an extremely important concept in machine learning, and it is crucial to get it right!

Consider the following problem of approximating 5 dots (represented by `x` on the graphs below):

!linear | overfit
--------|--------
**Linear model, 2 parameters** | **Non-linear model, 7 parameters**
Training error = 5.3 | Training error = 0
Validation error = 5.1 | Validation error = 20

* On the left, we see a good straight line approximation. Because the number of parameters is adequate, the model captures the idea behind point distribution correctly.
* On the right, the model is too powerful. Since we only have 5 points and the model has 7 parameters, it can adjust to pass through all points, making the training error 0. However, this prevents the model from understanding the correct pattern behind the data, resulting in a very high validation error.

It is very important to strike the right balance between the model's richness (number of parameters) and the number of training samples.

## Why overfitting occurs

  * Not enough training data
  * Too powerful model
  * Too much noise in input data

## How to detect overfitting

As you can see from the graph above, overfitting can be detected by a very low training error and a high validation error. Normally during training, we will see both training and validation errors start to decrease, and then at some point, the validation error might stop decreasing and start rising. This will be a sign of overfitting and an indicator that we should probably stop training at this point (or at least make a snapshot of the model).

## How to prevent overfitting

If you notice that overfitting occurs, you can do one of the following:

 * Increase the amount of training data
 * Decrease the complexity of the model
 * Use some regularization technique, such as Dropout, which we will discuss later.

## Overfitting and Bias-Variance Tradeoff

Overfitting is actually a case of a more generic problem in statistics called Bias-Variance Tradeoff. If we consider the possible sources of error in our model, we can see two types of errors:

* **Bias errors** are caused by our algorithm not being able to capture the relationship between training data correctly. It can result from our model not being powerful enough (**underfitting**).
* **Variance errors**, which are caused by the model approximating noise in the input data instead of a meaningful relationship (**overfitting**).

During training, bias error decreases (as our model learns to approximate the data), and variance error increases. It is important to stop training—either manually (when we detect overfitting) or automatically (by introducing regularization)—to prevent overfitting.

## Conclusion

In this lesson, you learned about the differences between the various APIs for the two most popular AI frameworks, TensorFlow and PyTorch. Additionally, you learned about a very important topic, overfitting.

## 🚀 Challenge

In the accompanying notebooks, you will find 'tasks' at the bottom; work through the notebooks and complete the tasks.

## Review & Self Study

Do some research on the following topics:

- TensorFlow
- PyTorch
- Overfitting

Ask yourself the following questions:

- What is the difference between TensorFlow and PyTorch?
- What is the difference between overfitting and underfitting?

## Assignment

In this lab, you are asked to solve two classification problems using single- and multi-layered fully-connected networks using PyTorch or TensorFlow.

**Disclaimer**:  
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.