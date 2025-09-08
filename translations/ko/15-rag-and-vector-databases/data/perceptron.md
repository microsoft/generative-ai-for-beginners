<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-07-09T16:55:30+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "ko"
}
-->
# 신경망 소개: 퍼셉트론

현대 신경망과 유사한 것을 구현하려는 최초의 시도 중 하나는 1957년 Cornell Aeronautical Laboratory의 Frank Rosenblatt에 의해 이루어졌습니다. 이것은 "Mark-1"이라는 하드웨어 구현으로, 삼각형, 사각형, 원과 같은 원시적인 기하학적 도형을 인식하도록 설계되었습니다.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> 이미지 출처: Wikipedia

입력 이미지는 20x20 포토셀 배열로 표현되어, 신경망은 400개의 입력과 하나의 이진 출력을 가졌습니다. 간단한 네트워크는 하나의 뉴런, 즉 **임계값 논리 유닛(threshold logic unit)** 으로 구성되었습니다. 신경망의 가중치는 훈련 단계에서 수동으로 조정해야 하는 가변 저항기(potentiometer)처럼 작동했습니다.

> ✅ 가변 저항기(potentiometer)는 사용자가 회로의 저항을 조절할 수 있게 해주는 장치입니다.

> 당시 뉴욕 타임즈는 퍼셉트론에 대해 이렇게 썼습니다: *[해군이] 걷고, 말하고, 보고, 쓰고, 스스로 복제하며 자신의 존재를 인식할 수 있을 것으로 기대하는 전자 컴퓨터의 배아.*

## 퍼셉트론 모델

모델에 N개의 특성이 있다고 가정하면, 입력 벡터는 크기 N의 벡터가 됩니다. 퍼셉트론은 **이진 분류** 모델로, 두 가지 클래스의 입력 데이터를 구분할 수 있습니다. 각 입력 벡터 x에 대해 퍼셉트론의 출력은 클래스에 따라 +1 또는 -1이 될 것입니다. 출력은 다음 공식으로 계산됩니다:

y(x) = f(w<sup>T</sup>x)

여기서 f는 계단 함수(step activation function)입니다.

## 퍼셉트론 훈련

퍼셉트론을 훈련시키려면 대부분의 값을 올바르게 분류하는 가중치 벡터 w를 찾아야 하며, 즉 가장 작은 **오류(error)** 를 만들어야 합니다. 이 오류는 다음과 같이 **퍼셉트론 기준(perceptron criterion)** 으로 정의됩니다:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

여기서:

* 합은 잘못 분류된 훈련 데이터 포인트 i에 대해 계산됩니다.
* x<sub>i</sub>는 입력 데이터이고, t<sub>i</sub>는 음성 예제에 대해 -1, 양성 예제에 대해 +1입니다.

이 기준은 가중치 w의 함수로 간주되며, 이를 최소화해야 합니다. 종종 **경사 하강법(gradient descent)** 이 사용되는데, 초기 가중치 w<sup>(0)</sup>에서 시작하여 각 단계마다 다음 공식에 따라 가중치를 업데이트합니다:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

여기서 η는 **학습률(learning rate)** 이고, ∇E(w)는 E의 **기울기(gradient)** 를 나타냅니다. 기울기를 계산한 후에는 다음과 같이 됩니다:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Python으로 구현한 알고리즘은 다음과 같습니다:

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

## 결론

이번 강의에서는 이진 분류 모델인 퍼셉트론과 가중치 벡터를 사용해 퍼셉트론을 훈련시키는 방법에 대해 배웠습니다.

## 🚀 도전 과제

직접 퍼셉트론을 만들어보고 싶다면, Azure ML 디자이너를 사용하는 Microsoft Learn의 이 실습을 시도해 보세요.

## 복습 및 자기 주도 학습

퍼셉트론을 사용해 간단한 문제와 실제 문제를 해결하는 방법을 보고 더 학습을 이어가려면 Perceptron 노트북을 참고하세요.

퍼셉트론에 관한 흥미로운 기사도 있습니다.

## 과제

이번 강의에서는 이진 분류 작업을 위한 퍼셉트론을 구현하고, 두 개의 손글씨 숫자를 분류하는 데 사용했습니다. 이번 실습에서는 숫자 분류 문제를 완전히 해결하는 것이 목표이며, 주어진 이미지에 가장 적합한 숫자가 무엇인지 결정해야 합니다.

* 지침
* 노트북

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.