<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-11-12T08:51:38+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "pcm"
}
-->
# Introduction to Neural Networks. Multi-Layered Perceptron

For di last section, you don learn about di simplest neural network model - one-layered perceptron, wey be linear two-class classification model.

For dis section, we go expand dis model to make am more flexible, so e go fit allow us:

* do **multi-class classification** join di two-class one
* solve **regression problems** join di classification
* separate classes wey no fit separate with straight line

We go also build our own modular framework for Python wey go help us create different neural network architectures.

## Formalization of Machine Learning

Make we start with how Machine Learning problem dey work. Imagine say we get training dataset **X** with labels **Y**, and we need build one model *f* wey go give us di most correct predictions. Di quality of di predictions dey measured by **Loss function** &lagran;. Di following loss functions dey common:

* For regression problem, when we need predict number, we fit use **absolute error** &sum;<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, or **squared error** &sum;<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* For classification, we dey use **0-1 loss** (wey be di same as **accuracy** of di model), or **logistic loss**.

For one-level perceptron, function *f* na linear function *f(x)=wx+b* (here *w* na di weight matrix, *x* na di vector of input features, and *b* na bias vector). For different neural network architectures, dis function fit get more complex form.

> For classification, e dey good to get probabilities of di classes as network output. To change random numbers to probabilities (like to normalize di output), we dey use **softmax** function &sigma;, and di function *f* go be *f(x)=&sigma;(wx+b)*

For di definition of *f* wey dey above, *w* and *b* na wetin dem dey call **parameters** &theta;=⟨*w,b*⟩. If we get dataset ⟨**X**,**Y**⟩, we fit calculate di overall error for di whole dataset as function of parameters &theta;.

> ✅ **Di goal of neural network training na to reduce di error by changing di parameters &theta;**

## Gradient Descent Optimization

One popular method wey dem dey use for function optimization na **gradient descent**. Di idea be say we fit calculate di derivative (for multi-dimensional case na **gradient**) of di loss function with respect to di parameters, and change di parameters so dat di error go reduce. E fit look like dis:

* Start di parameters with random values w<sup>(0)</sup>, b<sup>(0)</sup>
* Repeat dis step many times:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-&eta;&part;&lagran;/&part;w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-&eta;&part;&lagran;/&part;b

For training, di optimization steps suppose dey calculate based on di whole dataset (remember say loss dey calculate as sum of all training samples). But for real life, we dey use small parts of di dataset wey dem dey call **minibatches**, and calculate gradients based on di subset of data. Because di subset dey random every time, dis method na **stochastic gradient descent** (SGD).

## Multi-Layered Perceptrons and Backpropagation

One-layer network, as we don see before, fit classify linearly separable classes. To make di model better, we fit join plenty layers for di network. Mathematically, e go mean say di function *f* go get more complex form, and e go dey calculate step by step:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>&alpha;(z<sub>1</sub>)+b<sub>2</sub>
* f = &sigma;(z<sub>2</sub>)

Here, &alpha; na **non-linear activation function**, &sigma; na softmax function, and parameters &theta;=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Di gradient descent algorithm go still remain di same, but e go hard small to calculate gradients. With di chain differentiation rule, we fit calculate di derivatives like dis:

* &part;&lagran;/&part;w<sub>2</sub> = (&part;&lagran;/&part;&sigma;)(&part;&sigma;/&part;z<sub>2</sub>)(&part;z<sub>2</sub>/&part;w<sub>2</sub>)
* &part;&lagran;/&part;w<sub>1</sub> = (&part;&lagran;/&part;&sigma;)(&part;&sigma;/&part;z<sub>2</sub>)(&part;z<sub>2</sub>/&part;&alpha;)(&part;&alpha;/&part;z<sub>1</sub>)(&part;z<sub>1</sub>/&part;w<sub>1</sub>)

> ✅ Di chain differentiation rule na wetin dem dey use to calculate di derivatives of di loss function with respect to di parameters.

Make you notice say di left-most part of all di expressions dey di same, so we fit calculate di derivatives well if we start from di loss function and go "backwards" through di computational graph. So di method wey dem dey use to train multi-layered perceptron na **backpropagation**, or 'backprop'.

> TODO: image citation

> ✅ We go talk about backprop well well for di notebook example.  

## Conclusion

For dis lesson, we don build our own neural network library, and we don use am for one simple two-dimensional classification task.

## 🚀 Challenge

For di notebook wey dey follow, you go build your own framework to create and train multi-layered perceptrons. You go fit see how modern neural networks dey work.

Go di OwnFramework notebook and work through am.

## Review & Self Study

Backpropagation na common algorithm wey dem dey use for AI and ML, e good make you study am well.

## Assignment

For dis lab, dem dey ask you to use di framework wey you build for dis lesson to solve MNIST handwritten digit classification.

* Instructions
* Notebook

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say automated translations fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go trust. For important information, e better make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->