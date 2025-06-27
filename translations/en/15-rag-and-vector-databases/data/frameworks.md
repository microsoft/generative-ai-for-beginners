<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-06-25T22:52:01+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "en"
}
-->
# Neural Network Frameworks

As we have learned already, to efficiently train neural networks, we need to do two things:

* Operate on tensors, such as multiplying, adding, and computing functions like sigmoid or softmax.
* Compute gradients of all expressions to perform gradient descent optimization.

While the `numpy` library can handle the first part, we need a mechanism to compute gradients. In our framework developed in the previous section, we had to manually program all derivative functions within the `backward` method, which handles backpropagation. Ideally, a framework should enable us to compute gradients for *any expression* we define.

Another key aspect is the ability to perform computations on GPUs or other specialized compute units like TPUs. Training deep neural networks involves *a lot* of computations, and parallelizing these computations on GPUs is crucial.

> ✅ The term 'parallelize' means distributing computations across multiple devices.

Currently, the two most popular neural frameworks are TensorFlow and PyTorch. Both provide a low-level API for tensor operations on both CPU and GPU. Additionally, there is a higher-level API, known as Keras and PyTorch Lightning, respectively.

Low-Level API | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
High-level API| Keras| PyTorch Lightning

**Low-level APIs** in both frameworks allow you to build **computational graphs**. This graph defines how to compute the output (usually the loss function) with given input parameters and can be executed on a GPU if available. Functions are available to differentiate this computational graph and compute gradients, which can then be used to optimize model parameters.

**High-level APIs** consider neural networks as a **sequence of layers**, making it easier to construct most neural networks. Training the model typically involves preparing the data and then calling a `fit` function to perform the task.

The high-level API enables quick construction of typical neural networks without worrying about many details. Meanwhile, the low-level API provides more control over the training process, making it widely used in research, especially when dealing with new neural network architectures.

It's also important to understand that both APIs can be used together. For example, you can develop your own network layer architecture using the low-level API and then integrate it into a larger network constructed and trained with the high-level API. Alternatively, you can define a network using the high-level API as a sequence of layers and then apply your own low-level training loop for optimization. Both APIs share the same basic underlying concepts and are designed to work well together.

## Learning

In this course, we offer most content for both PyTorch and TensorFlow. You can choose your preferred framework and focus on the corresponding notebooks. If you're unsure which framework to choose, read online discussions about **PyTorch vs. TensorFlow**. You can also explore both frameworks to gain a better understanding.

Where possible, we'll use High-Level APIs for simplicity. However, we believe it's crucial to understand neural networks from the ground up, so we'll start by working with the low-level API and tensors. If you want to get started quickly and avoid spending too much time learning these details, you can skip them and proceed directly to high-level API notebooks.

## ✍️ Exercises: Frameworks

Continue your learning in the following notebooks:

Low-Level API | TensorFlow+Keras Notebook | PyTorch
--------------|-------------------------------------|--------------------------------
High-level API| Keras | *PyTorch Lightning*

After mastering the frameworks, let's revisit the concept of overfitting.

# Overfitting

Overfitting is a crucial concept in machine learning, and it's vital to understand it correctly!

Consider the problem of approximating 5 dots (represented by `x` on the graphs below):

!linear | overfit
-------------------------|--------------------------
**Linear model, 2 parameters** | **Non-linear model, 7 parameters**
Training error = 5.3 | Training error = 0
Validation error = 5.1 | Validation error = 20

* On the left, we see a good straight line approximation. The number of parameters is suitable, allowing the model to correctly interpret the point distribution.
* On the right, the model is too complex. With only 5 points and 7 parameters, it can adjust to pass through all points, resulting in a training error of 0. However, this prevents the model from understanding the correct data pattern, leading to a high validation error.

Striking the right balance between model complexity (number of parameters) and the number of training samples is crucial.

## Why overfitting occurs

  * Insufficient training data
  * Excessively complex model
  * Excessive noise in input data

## How to detect overfitting

As seen from the graph above, overfitting can be identified by a very low training error and a high validation error. Typically, during training, both training and validation errors decrease, but at some point, the validation error may stop decreasing and start increasing. This indicates overfitting and suggests stopping training at this point (or at least taking a snapshot of the model).

## How to prevent overfitting

If overfitting is detected, you can:

 * Increase the amount of training data
 * Decrease the model's complexity
 * Apply regularization techniques like Dropout, which we'll explore later.

## Overfitting and Bias-Variance Tradeoff

Overfitting is actually a specific case of a broader statistical problem known as Bias-Variance Tradeoff. Considering potential sources of error in our model, we identify two types of errors:

* **Bias errors** arise from the algorithm's inability to correctly capture the relationship in training data. This may result from an insufficiently powerful model (**underfitting**).
* **Variance errors** occur when the model approximates noise in input data rather than meaningful relationships (**overfitting**).

During training, bias error decreases (as the model learns to approximate the data), while variance error increases. It's crucial to stop training—either manually (upon detecting overfitting) or automatically (through regularization)—to prevent overfitting.

## Conclusion

In this lesson, you learned about the differences between various APIs for the two most popular AI frameworks, TensorFlow and PyTorch. Additionally, you explored a vital topic, overfitting.

## 🚀 Challenge

In the accompanying notebooks, you'll find 'tasks' at the bottom; work through the notebooks and complete the tasks.

## Review & Self Study

Research the following topics:

- TensorFlow
- PyTorch
- Overfitting

Ask yourself these questions:

- What is the difference between TensorFlow and PyTorch?
- What is the difference between overfitting and underfitting?

## Assignment

In this lab, you'll solve two classification problems using single- and multi-layered fully-connected networks with PyTorch or TensorFlow.

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.