<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-06-25T23:33:31+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "en"
}
-->
# Introduction to Neural Networks: Perceptron

One of the earliest attempts to create something akin to a modern neural network was made by Frank Rosenblatt from Cornell Aeronautical Laboratory in 1957. It was a hardware implementation called "Mark-1", designed to recognize basic geometric shapes like triangles, squares, and circles.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Images from Wikipedia

An input image was represented by a 20x20 photocell array, giving the neural network 400 inputs and one binary output. This simple network contained a single neuron, also known as a **threshold logic unit**. Neural network weights functioned like potentiometers, requiring manual adjustment during the training phase.

> ✅ A potentiometer is a device that allows the user to adjust the resistance of a circuit.

> The New York Times wrote about the perceptron at the time: *the embryo of an electronic computer that [the Navy] expects will be able to walk, talk, see, write, reproduce itself, and be conscious of its existence.*

## Perceptron Model

Imagine we have N features in our model, in which case the input vector would be a vector of size N. A perceptron is a **binary classification** model, meaning it can differentiate between two classes of input data. We'll assume that for each input vector x, the output of our perceptron will be either +1 or -1, depending on the class. The output is calculated using the formula:

y(x) = f(w<sup>T</sup>x)

where f is a step activation function.

## Training the Perceptron

To train a perceptron, we need to find a weights vector w that correctly classifies most values, resulting in the smallest **error**. This error is defined by the **perceptron criterion** as follows:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

where:

* The sum is taken over those training data points i that result in incorrect classification.
* x<sub>i</sub> is the input data, and t<sub>i</sub> is either -1 or +1 for negative and positive examples, respectively.

This criterion is viewed as a function of weights w, and we need to minimize it. Often, a method called **gradient descent** is used, where we start with some initial weights w<sup>(0)</sup>, and then at each step update the weights according to the formula:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Here η is known as the **learning rate**, and ∇E(w) denotes the **gradient** of E. After calculating the gradient, we end up with

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

The algorithm in Python looks like this:

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

In this lesson, you learned about a perceptron, which is a binary classification model, and how to train it using a weights vector.

## 🚀 Challenge

If you're interested in building your own perceptron, try this lab on Microsoft Learn that uses the Azure ML designer.

## Review & Self Study

To explore how we can use a perceptron to solve both toy and real-life problems, and to continue learning, check out the Perceptron notebook.

Here's an interesting article about perceptrons as well.

## Assignment

In this lesson, we implemented a perceptron for a binary classification task, using it to differentiate between two handwritten digits. In this lab, you are tasked with solving the complete problem of digit classification, determining which digit most likely corresponds to a given image.

* Instructions
* Notebook

Certainly! Here is the translated text:

---

**Disclaimer**:  
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.