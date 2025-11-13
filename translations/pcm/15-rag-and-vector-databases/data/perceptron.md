<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-11-12T08:51:28+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "pcm"
}
-->
# Introduction to Neural Networks: Perceptron

One of di first try wey dem do to create somtin wey resemble modern neural network na Frank Rosenblatt from Cornell Aeronautical Laboratory for 1957. E be hardware wey dem call "Mark-1", e dey designed to sabi primitive geometric shapes like triangle, square and circle.

|      |      |
|--------------|-----------|
|<img src='../../../../translated_images/Rosenblatt-wikipedia.1d205667acda28c0f97ad594eb6dadfa0485605f3fb2155eca46a0255e98efac.pcm.jpg' alt='Frank Rosenblatt'/> | <img src='../../../../translated_images/Mark_I_perceptron_wikipedia.434e46ca39e2be801976110f8b1b75b13d1197f69e3a5f8b7537b43d35413e6f.pcm.jpg' alt='The Mark 1 Perceptron' />|

> Images from Wikipedia

Di input image na 20x20 photocell array, so di neural network get 400 inputs and one binary output. Di simple network get one neuron, wey dem dey call **threshold logic unit**. Di neural network weights dey act like potentiometers wey dem go need adjust manually during di training phase.

> ✅ Potentiometer na device wey dey allow person adjust di resistance for circuit.

> Di New York Times write about perceptron for dat time: *di embryo of an electronic computer wey [di Navy] dey expect go fit waka, talk, see, write, reproduce itself and sabi say e dey exist.*

## Perceptron Model

Make we assume say we get N features for our model, for dis case di input vector go be vector wey get size N. Perceptron na **binary classification** model, e mean say e fit separate two classes of input data. We go assume say for each input vector x, di output of our perceptron go be either +1 or -1, depending on di class. Di output go dey calculate using dis formula:

y(x) = f(w<sup>T</sup>x)

where f na step activation function

## Training di Perceptron

To train perceptron, we need find weights vector w wey go classify most of di values correct, e mean say e go give di smallest **error**. Dis error dey defined by **perceptron criterion** like dis:

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

where:

* di sum dey for di training data points i wey dey give wrong classification
* x<sub>i</sub> na di input data, and t<sub>i</sub> na either -1 or +1 for negative and positive examples as e dey.

Dis criteria na function of weights w, and we need minimize am. Most times, dem dey use method wey dem dey call **gradient descent**, wey we go start with some initial weights w<sup>(0)</sup>, and then for each step we go update di weights with dis formula:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

Here &eta; na di **learning rate**, and &nabla;E(w) mean di **gradient** of E. After we calculate di gradient, we go get:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

Di algorithm for Python go look like dis:

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

For dis lesson, you don learn about perceptron, wey be binary classification model, and how to train am by using weights vector.

## 🚀 Challenge

If you wan try build your own perceptron, try dis lab for Microsoft Learn wey dey use Azure ML designer.

## Review & Self Study

To see how we fit use perceptron solve toy problem and real-life problems, and to continue di learning - go Perceptron notebook.

Here na one interesting article about perceptrons too.

## Assignment

For dis lesson, we don implement perceptron for binary classification task, and we don use am classify between two handwritten digits. For dis lab, dem dey ask you to solve di problem of digit classification completely, e mean say make you determine which digit dey most likely correspond to di given image.

* Instructions
* Notebook

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say automated translations fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go trust. For important information, e better make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->