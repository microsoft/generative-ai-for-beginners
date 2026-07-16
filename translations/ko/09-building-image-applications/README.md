# 이미지 생성 애플리케이션 구축

[![이미지 생성 애플리케이션 구축](../../../translated_images/ko/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLM은 텍스트 생성 이상의 기능을 가집니다. 텍스트 설명에서 이미지를 생성하는 것도 가능합니다. 이미지라는 모달리티는 MedTech, 건축, 관광, 게임 개발 등 여러 분야에서 매우 유용할 수 있습니다. 이 장에서는 가장 인기 있는 두 이미지 생성 모델, DALL-E와 Midjourney를 살펴보겠습니다.

## 소개

이 수업에서는 다음 내용을 다룹니다:

- 이미지 생성과 그 유용성.
- DALL-E와 Midjourney가 무엇이고, 어떻게 작동하는지.
- 이미지 생성 애플리케이션을 구축하는 방법.

## 학습 목표

이 수업을 완료하면 다음을 할 수 있습니다:

- 이미지 생성 애플리케이션을 구축합니다.
- 메타 프롬프트로 애플리케이션의 경계를 정의합니다.
- DALL-E와 Midjourney를 활용합니다.

## 왜 이미지 생성 애플리케이션을 구축해야 하나요?

이미지 생성 애플리케이션은 생성 AI의 기능을 탐구하는 훌륭한 방법입니다. 예를 들어 다음과 같이 사용할 수 있습니다:

- **이미지 편집 및 합성**. 이미지는 편집과 합성 등 다양한 용도로 생성할 수 있습니다.

- **다양한 산업에 적용 가능**. Medtech, 관광, 게임 개발 등 여러 산업에서 이미지 생성에 사용할 수 있습니다.

## 시나리오: Edu4All

이 수업의 일환으로 우리는 스타트업 Edu4All과 계속 작업할 것입니다. 학생들은 평가를 위해 이미지를 생성할 것인데, 구체적인 이미지 내용은 학생들이 결정합니다. 예를 들어 자신의 동화 삽화를 만들거나 이야기의 새 캐릭터를 생성하거나 아이디어와 개념을 시각화하는 데 도움을 줄 수 있습니다.

예를 들어, 만약 학생들이 수업에서 기념물에 대해 작업한다면 Edu4All 학생들이 생성할 수 있는 예시는 다음과 같습니다:

![Edu4All 스타트업, 기념물 수업, 에펠탑](../../../translated_images/ko/startup.94d6b79cc4bb3f5a.webp)

프롬프트 예시는 다음과 같습니다

> "초승달 아침 햇빛에 비친 에펠탑 옆의 개"

## DALL-E와 Midjourney란 무엇인가요?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst)와 [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst)는 가장 인기 있는 두 이미지 생성 모델로, 프롬프트를 사용하여 이미지를 생성할 수 있게 해줍니다.

### DALL-E

먼저 DALL-E는 텍스트 설명에서 이미지를 생성하는 생성 AI 모델입니다.

> [DALL-E는 CLIP와 diffused attention 두 모델의 결합입니다](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- <strong>CLIP</strong>은 이미지와 텍스트에서 데이터의 수치적 표현인 임베딩을 생성하는 모델입니다.


- <strong>Diffused attention</strong>는 임베딩으로부터 이미지를 생성하는 모델입니다. DALL-E는 이미지와 텍스트 데이터셋을 기반으로 학습되었으며, 텍스트 설명으로부터 이미지를 생성하는 데 사용될 수 있습니다. 예를 들어, DALL-E는 모자를 쓴 고양이나 모호크 헤어스타일의 개 이미지를 생성하는 데 사용될 수 있습니다.

### Midjourney

Midjourney는 DALL-E와 유사한 방식으로 작동하며, 텍스트 프롬프트로부터 이미지를 생성합니다. Midjourney는 “모자를 쓴 고양이” 또는 “모호크 헤어스타일의 개”와 같은 프롬프트를 사용하여 이미지를 생성하는 데에도 사용할 수 있습니다.

![Midjourney가 생성한 이미지, 기계 비둘기](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_출처 위키피디아, Midjourney가 생성한 이미지_

## DALL-E와 Midjourney는 어떻게 작동하나요

먼저, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E는 _autoregressive transformer_를 사용하는 트랜스포머 아키텍처 기반 생성 AI 모델입니다.

_autoregressive transformer_는 모델이 텍스트 설명으로부터 이미지를 생성하는 방식을 정의합니다. 이 모델은 한 번에 한 픽셀씩 생성하며, 생성된 픽셀을 활용해 다음 픽셀을 생성합니다. 여러 신경망 층을 거치면서 이미지가 완성됩니다.

이 과정을 통해 DALL-E는 생성하는 이미지의 속성, 객체, 특징 등을 제어합니다. 다만, DALL-E 2와 3은 더 높은 수준의 이미지 생성 제어가 가능합니다.

## 첫 번째 이미지 생성 애플리케이션 만들기

이미지 생성 애플리케이션을 만들려면 무엇이 필요할까요? 다음 라이브러리가 필요합니다:

- **python-dotenv**: 코드를 벗어나 비밀 키를 _.env_ 파일에 안전하게 보관하기 위해 이 라이브러리를 적극 권장합니다.
- **openai**: OpenAI API와 상호 작용하기 위해 이 라이브러리를 사용합니다.
- **pillow**: Python에서 이미지를 다루기 위한 라이브러리입니다.
- **requests**: HTTP 요청을 수행하는 데 도움을 줍니다.

## Azure OpenAI 모델 생성 및 배포하기

아직 하지 않았다면, [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) 페이지의 안내를 따라
Azure OpenAI 리소스와 모델을 생성하세요. 현재 세대 Azure OpenAI 이미지 모델인 <strong>gpt-image-1</strong>을 선택하세요(DALL-E 3는 구버전으로, 새로운 배포에 더 이상 제공되지 않습니다).

## 앱 만들기

1. _.env_ 파일을 다음과 같이 생성하세요:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   이 정보는 Azure OpenAI Foundry 포털의 “Deployments” 섹션에서 리소스를 확인하면 찾을 수 있습니다.

1. 위 라이브러리를 모두 모아 _requirements.txt_ 파일을 다음과 같이 만드세요:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. 다음으로 가상환경을 만들고 라이브러리를 설치하세요:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```


   Windows에서 가상 환경을 생성하고 활성화하려면 다음 명령어를 사용하세요:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_라는 파일에 다음 코드를 추가하세요:


    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # import dotenv
    dotenv.load_dotenv()
    
    # Azure OpenAI 서비스 클라이언트 구성
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # 이미지 생성 API를 사용하여 이미지 생성
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # 저장된 이미지의 디렉토리 설정
        image_dir = os.path.join(os.curdir, 'images')

        # 디렉토리가 없으면 생성
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # 이미지 경로 초기화(파일 형식은 png여야 함)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # 생성된 이미지 가져오기
        image_url = generation_response.data[0].url  # 응답에서 이미지 URL 추출
        generated_image = requests.get(image_url).content  # 이미지 다운로드
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # 기본 이미지 뷰어에서 이미지 표시
        image = Image.open(image_path)
        image.show()

    # 예외 처리
    except openai.BadRequestError as err:
        print(err)
   ```

이 코드를 설명해 봅시다:

- 먼저, OpenAI 라이브러리, dotenv 라이브러리, requests 라이브러리, 그리고 Pillow 라이브러리를 포함하여 필요한 라이브러리를 가져옵니다.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- 다음으로, _.env_ 파일에서 환경 변수를 로드합니다.

  ```python
  # dotenv 가져오기
  dotenv.load_dotenv()
  ```

- 그 후, Azure OpenAI 서비스 클라이언트를 구성합니다

  ```python
  # 환경 변수에서 엔드포인트와 키를 가져옵니다
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- 다음으로, 이미지를 생성합니다:

  ```python
  # 이미지 생성 API를 사용하여 이미지를 만드세요
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  위 코드는 생성된 이미지의 URL을 포함하는 JSON 객체를 응답합니다. URL을 사용하여 이미지를 다운로드하고 파일로 저장할 수 있습니다.

- 마지막으로, 이미지를 열고 표준 이미지 뷰어로 표시합니다:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### 이미지 생성에 대한 추가 세부 정보

이미지 생성 코드를 좀 더 자세히 살펴보겠습니다:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- <strong>prompt</strong>는 이미지를 생성하는 데 사용되는 텍스트 프롬프트입니다. 이 경우 프롬프트는 "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"입니다.
- <strong>size</strong>는 생성되는 이미지의 크기입니다. 이 경우 1024x1024 픽셀 이미지를 생성합니다.
- <strong>n</strong>은 생성되는 이미지의 수입니다. 이 경우 두 장의 이미지를 생성합니다.
- <strong>temperature</strong>는 생성 AI 모델 출력의 무작위성을 제어하는 매개변수입니다. 0과 1 사이의 값이며, 0은 출력이 결정적이고 1은 출력이 무작위임을 의미합니다. 기본값은 0.7입니다.

다음 섹션에서 이미지로 할 수 있는 더 많은 작업을 다룰 예정입니다.

## 이미지 생성의 추가 기능

지금까지 Python 몇 줄로 이미지를 생성하는 방법을 보셨습니다. 그러나 이미지로 할 수 있는 더 많은 일이 있습니다.

다음과 같은 작업도 할 수 있습니다:

- **편집 수행하기**. 기존 이미지와 마스크, 프롬프트를 제공하여 이미지를 변경할 수 있습니다. 예를 들어, 이미지 일부분에 무언가를 추가할 수 있습니다. 예를 들어 우리 토끼 이미지에 모자를 씌우는 식입니다. 이미지를 제공하고, 변경할 영역을 나타내는 마스크와 어떤 작업을 할지 설명하는 텍스트 프롬프트를 제공하면 됩니다.
> 참고: 이는 DALL-E 3에서는 지원되지 않습니다.
 
GPT Image를 사용한 예는 다음과 같습니다:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  기본 이미지는 오직 라운지와 수영장만 포함하지만 최종 이미지에는 플라밍고가 추가됩니다:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/ko/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/ko/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/ko/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **변형 생성**. 기존 이미지를 가져와 변형을 생성하도록 요청하는 개념입니다. 변형을 생성하려면 이미지와 텍스트 프롬프트를 제공하고 다음과 같이 코딩합니다:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > 참고, 이는 OpenAI의 DALL-E 2 모델에서만 지원되며 gpt-image-1에서는 지원되지 않습니다.

## 온도(Temperature)

온도는 생성 AI 모델 출력의 무작위성을 조절하는 매개변수입니다. 0과 1 사이의 값이며, 0은 결정적 출력, 1은 무작위 출력을 의미합니다. 기본값은 0.7입니다.

온도가 어떻게 작동하는지 이해하기 위해, 동일한 프롬프트를 두 번 실행해봅시다:

> 프롬프트 : "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![막대사탕을 들고 있는 말 위 토끼, 버전 1](../../../translated_images/ko/v1-generated-image.a295cfcffa3c13c2.webp)

이제 같은 프롬프트를 다시 실행해서 동일한 이미지를 두 번 얻지 못함을 확인해봅시다:

![말 위 토끼가 생성된 이미지](../../../translated_images/ko/v2-generated-image.33f55a3714efe61d.webp)

보시다시피 이미지들은 비슷하지만 동일하지 않습니다. 이제 온도 값을 0.1로 바꿔서 어떻게 되는지 봅시다:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # 여기에 프롬프트 텍스트를 입력하세요
        size='1024x1024',
        n=2
    )
```

### 온도 변경하기

이제 출력이 더 결정적이도록 만들어 봅시다. 앞서 생성한 두 이미지를 보면 첫 번째는 토끼이고 두 번째는 말이므로 이미지가 크게 달랐습니다.

따라서 코드를 변경하여 온도를 0으로 설정해 봅시다:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # 여기에 프롬프트 텍스트를 입력하세요
        size='1024x1024',
        n=2,
        temperature=0
    )
```

이 코드를 실행하면 다음 두 이미지를 얻을 수 있습니다:

- ![온도 0, v1](../../../translated_images/ko/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![온도 0 , v2](../../../translated_images/ko/v2-temp-generated-image.871d0c920dbfb0f1.webp)

여기서 이미지들이 서로 훨씬 더 닮았다는 것을 명확히 알 수 있습니다.

## 메타프롬프트를 사용해 애플리케이션 경계 정의하기

우리 데모로 이미 클라이언트용 이미지를 생성할 수 있습니다. 하지만 애플리케이션에 대한 경계를 만들어야 합니다.

예를 들어, 작업에 부적절하거나 어린이에게 적합하지 않은 이미지를 생성하지 않도록 해야 합니다.

이를 _메타프롬프트_로 할 수 있습니다. 메타프롬프트는 생성 AI 모델의 출력을 제어하는 텍스트 프롬프트입니다. 예를 들어, 작업에 안전하고 어린이에게 적합한 이미지를 생성하도록 출력을 제어할 때 사용합니다.

### 작동 원리는?

이제 메타프롬프트가 어떻게 작동하는지 봅시다.

메타프롬프트는 생성 AI 모델 출력을 제어하는 텍스트 프롬프트로, 텍스트 프롬프트 앞에 위치하여 모델 출력을 제어합니다. 애플리케이션에 포함되어 입력 프롬프트와 메타프롬프트를 하나의 텍스트 프롬프트로 캡슐화합니다.

메타프롬프트의 예는 다음과 같습니다:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

이제 데모에서 메타프롬프트를 어떻게 사용하는지 살펴봅시다.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt =f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"{meta_prompt}
Create an image of a bunny on a horse, holding a lollipop"

# TODO 이미지 생성을 위한 요청 추가하기
```

위의 프롬프트에서 모든 생성된 이미지가 메타프롬프트를 고려함을 볼 수 있습니다.

## 과제 - 학생들에게 권한 부여하기

이 수업 처음에 Edu4All을 소개했습니다. 이제 학생들이 평가를 위해 이미지를 생성할 수 있도록 권한을 부여할 시간입니다.


학생들은 기념물을 포함하는 평가용 이미지를 만들 것입니다. 어떤 기념물을 선택할지는 학생들의 몫입니다. 학생들은 이 과제에서 창의력을 발휘하여 이러한 기념물을 다양한 맥락 속에 배치하도록 요청받았습니다.

## 해결 방법

다음은 하나의 가능한 해결책입니다:

```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# dotenv를 가져옵니다
dotenv.load_dotenv()

# 환경 변수에서 엔드포인트와 키를 가져옵니다
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
  api_key=os.environ['AZURE_OPENAI_API_KEY'],
  api_version = "2024-10-21"
  )


disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"""{meta_prompt}
Generate monument of the Arc of Triumph in Paris, France, in the evening light with a small child holding a Teddy looks on.
"""

try:
    # 이미지 생성 API를 사용하여 이미지를 만듭니다
    generation_response = client.images.generate(
        prompt=prompt,    # 여기에 프롬프트 텍스트를 입력하세요
        size='1024x1024',
        n=1,
    )
    # 저장된 이미지의 디렉토리를 설정합니다
    image_dir = os.path.join(os.curdir, 'images')

    # 디렉토리가 없으면 생성합니다
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # 이미지 경로를 초기화합니다 (파일 형식은 png여야 합니다)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # 생성된 이미지를 가져옵니다
    image_url = generation_response.data[0].url  # 응답에서 이미지 URL을 추출합니다
    generated_image = requests.get(image_url).content  # 이미지를 다운로드합니다
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # 기본 이미지 뷰어에서 이미지를 표시합니다
    image = Image.open(image_path)
    image.show()

# 예외를 처리합니다
except openai.BadRequestError as err:
    print(err)
```

## 훌륭한 작업! 학습을 계속하세요

이 수업을 완료한 후, [Generative AI Learning 컬렉션](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인하여 생성 AI 지식을 계속 향상시키세요!

10강으로 이동하여 [로우코드로 AI 애플리케이션을 구축하는 방법](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)을 살펴보겠습니다.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->