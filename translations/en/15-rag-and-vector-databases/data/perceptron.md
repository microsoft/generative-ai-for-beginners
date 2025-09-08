<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-07-09T16:53:09+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "en"
}
-->
# Introduction to Neural Networks: Perceptron

One of the earliest attempts to create something similar to a modern neural network was made by Frank Rosenblatt at the Cornell Aeronautical Laboratory in 1957. It was a hardware implementation called "Mark-1," designed to recognize simple geometric shapes like triangles, squares, and circles.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Images from Wikipedia

An input image was represented by a 20x20 photocell array, so the neural network had 400 inputs and one binary output. The simple network consisted of a single neuron, also known as a **threshold logic unit**. The neural network’s weights acted like potentiometers that had to be manually adjusted during training.

> ✅ A potentiometer is a device that lets the user adjust the resistance in a circuit.

> At the time, The New York Times described the perceptron as *the embryo of an electronic computer that [the Navy] expects will be able to walk, talk, see, write, reproduce itself and be aware of its own existence.*

## Perceptron Model

Let’s say our model has N features, so the input vector is of size N. A perceptron is a **binary classification** model, meaning it can distinguish between two classes of input data. We assume that for each input vector x, the perceptron’s output will be either +1 or -1, depending on the class. The output is calculated using the formula:

y(x) = f(w<sup>T</sup>x)

where f is a step activation function

## Training the Perceptron

To train a perceptron, we need to find a weight vector w that correctly classifies most of the data, minimizing the **error**. This error is defined by the **perceptron criterion** as follows:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

where:

* the sum is taken over those training data points i that are misclassified
* x<sub>i</sub> is the input data, and t<sub>i</sub> is either -1 or +1 for negative and positive examples, respectively.

This criterion is treated as a function of the weights w, and our goal is to minimize it. A common method used is **gradient descent**, where we start with some initial weights w<sup>(0)</sup>, and at each step update the weights using the formula:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Here, η is the **learning rate**, and ∇E(w) is the **gradient** of E. After calculating the gradient, the update rule becomes:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

The Python implementation of this algorithm looks like this:

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

## Conclusion

In this lesson, you learned about the perceptron, a binary classification model, and how to train it by adjusting a weight vector.

## 🚀 Challenge

If you want to try building your own perceptron, check out this lab on Microsoft Learn that uses the Azure ML designer.

## Review & Self Study

To see how perceptrons can be used to solve both simple and real-world problems, and to continue your learning, visit the Perceptron notebook.

Here’s also an interesting article about perceptrons.

## Assignment

In this lesson, we implemented a perceptron for a binary classification task and used it to distinguish between two handwritten digits. In this lab, you will solve the full digit classification problem, determining which digit most likely corresponds to a given image.

* Instructions
* Notebook

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.