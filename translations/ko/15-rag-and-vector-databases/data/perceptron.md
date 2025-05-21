<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-05-20T02:32:42+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "ko"
}
-->
# 신경망 소개: 퍼셉트론

현대 신경망과 유사한 것을 구현하려는 초기 시도 중 하나는 1957년 코넬 항공 연구소의 Frank Rosenblatt에 의해 이루어졌습니다. 이는 "Mark-1"이라는 하드웨어 구현으로, 삼각형, 사각형, 원과 같은 원시 기하학적 도형을 인식하도록 설계되었습니다.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> 이미지 출처: 위키백과

입력 이미지는 20x20 포토셀 배열로 표현되었으며, 따라서 신경망은 400개의 입력과 하나의 이진 출력을 가졌습니다. 간단한 네트워크는 **임계값 논리 유닛**이라고도 불리는 하나의 뉴런을 포함했습니다. 신경망 가중치는 학습 단계에서 수동 조정을 필요로 하는 전위차계처럼 작동했습니다.

> ✅ 전위차계는 사용자가 회로의 저항을 조정할 수 있게 하는 장치입니다.

> 당시 뉴욕 타임스는 퍼셉트론에 대해 이렇게 썼습니다: *[해군]이 걷고, 말하고, 보고, 쓰고, 스스로를 복제하고 자신의 존재를 인식할 수 있기를 기대하는 전자 컴퓨터의 배아.*

## 퍼셉트론 모델

우리 모델에 N개의 특성이 있다고 가정해 봅시다. 이 경우 입력 벡터는 크기 N의 벡터가 됩니다. 퍼셉트론은 **이진 분류** 모델로, 즉 입력 데이터의 두 클래스를 구분할 수 있습니다. 각 입력 벡터 x에 대해 퍼셉트론의 출력이 클래스에 따라 +1 또는 -1이 될 것이라고 가정합니다. 출력은 다음 공식을 사용하여 계산됩니다:

y(x) = f(w<sup>T</sup>x)

여기서 f는 단계 활성화 함수입니다.

## 퍼셉트론 학습

퍼셉트론을 학습시키려면 대부분의 값을 올바르게 분류하는 가중치 벡터 w를 찾아야 하며, 즉 가장 작은 **오류**를 발생시켜야 합니다. 이 오류는 **퍼셉트론 기준**에 의해 다음과 같이 정의됩니다:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

여기서:

* 합은 잘못된 분류를 초래하는 훈련 데이터 지점 i에 대해 수행됩니다.
* x<sub>i</sub>는 입력 데이터이고, t<sub>i</sub>는 각각 음수 및 양수 예제에 대해 -1 또는 +1입니다.

이 기준은 가중치 w의 함수로 간주되며, 이를 최소화해야 합니다. 종종 **경사 하강법**이라는 방법이 사용되며, 이는 초기 가중치 w<sup>(0)</sup>로 시작하여 각 단계에서 다음 공식에 따라 가중치를 업데이트하는 것입니다:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

여기서 η는 **학습률**이라고 불리며, ∇E(w)는 E의 **기울기**를 나타냅니다. 기울기를 계산한 후에는 다음과 같은 결과를 얻습니다:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Python에서의 알고리즘은 다음과 같습니다:

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

이 강의에서는 이진 분류 모델인 퍼셉트론과 가중치 벡터를 사용하여 이를 학습시키는 방법에 대해 배웠습니다.

## 🚀 도전 과제

자신만의 퍼셉트론을 구축해보고 싶다면, Azure ML 디자이너를 사용하는 Microsoft Learn의 이 실습을 시도해보세요.

## 검토 및 자기 학습

퍼셉트론을 사용하여 장난감 문제와 실제 문제를 해결하는 방법을 보고 계속 학습하려면 퍼셉트론 노트북으로 이동하세요.

퍼셉트론에 관한 흥미로운 기사도 있습니다.

## 과제

이 강의에서는 이진 분류 작업을 위한 퍼셉트론을 구현하였으며, 이를 사용하여 두 개의 손으로 쓴 숫자를 분류하였습니다. 이 실습에서는 주어진 이미지와 가장 일치할 가능성이 높은 숫자를 결정하는, 즉 숫자 분류 문제를 완전히 해결해야 합니다.

* 지침
* 노트북

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 우리는 정확성을 위해 노력하지만, 자동 번역에는 오류나 부정확성이 있을 수 있음을 유의하시기 바랍니다. 원어로 작성된 원본 문서를 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 오역에 대해 우리는 책임을 지지 않습니다.