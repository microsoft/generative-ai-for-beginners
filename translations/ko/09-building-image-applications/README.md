<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T10:31:33+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ko"
}
-->
# 이미지 생성 애플리케이션 구축

[![이미지 생성 애플리케이션 구축](../../../translated_images/09-lesson-banner.d0229c79fda6596b8a678478e20301b74964cb8161e0c2e4a7c203655c623330.ko.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLMs는 텍스트 생성뿐만 아니라, 텍스트 설명으로부터 이미지를 생성할 수도 있습니다. 이미지를 활용하는 것은 MedTech, 건축, 관광, 게임 개발 등 다양한 분야에서 매우 유용할 수 있습니다. 이 장에서는 가장 인기 있는 이미지 생성 모델인 DALL-E와 Midjourney에 대해 알아보겠습니다.

## 소개

이 강의에서는 다음 내용을 다룹니다:

- 이미지 생성과 그 유용성.
- DALL-E와 Midjourney, 그것들이 무엇인지, 그리고 어떻게 작동하는지.
- 이미지 생성 앱을 구축하는 방법.

## 학습 목표

이 강의를 완료한 후, 다음을 할 수 있게 됩니다:

- 이미지 생성 애플리케이션을 구축합니다.
- 메타 프롬프트로 애플리케이션의 경계를 정의합니다.
- DALL-E 및 Midjourney와 함께 작업합니다.

## 왜 이미지 생성 애플리케이션을 구축해야 할까요?

이미지 생성 애플리케이션은 생성 AI의 기능을 탐구할 수 있는 훌륭한 방법입니다. 예를 들어 다음과 같은 용도로 사용할 수 있습니다:

- **이미지 편집 및 합성**. 다양한 사용 사례를 위해 이미지를 생성할 수 있습니다. 예를 들어 이미지 편집 및 합성을 위한 이미지 생성이 가능합니다.

- **다양한 산업에 적용**. Medtech, 관광, 게임 개발 등 다양한 산업을 위해 이미지를 생성하는 데 사용할 수 있습니다.

## 시나리오: Edu4All

이 강의의 일환으로, 우리는 Edu4All이라는 스타트업과 계속해서 작업할 것입니다. 학생들은 자신의 평가를 위해 이미지를 생성할 것입니다. 어떤 이미지를 생성할지는 학생들에게 달려 있지만, 자신만의 동화를 위한 일러스트를 만들거나 이야기의 새로운 캐릭터를 만들거나 자신의 아이디어와 개념을 시각화하는 데 도움을 줄 수 있습니다.

예를 들어, Edu4All의 학생들이 수업에서 기념물에 대해 작업하고 있다면 다음과 같은 이미지를 생성할 수 있습니다:

![Edu4All 스타트업, 기념물 수업, 에펠탑](../../../translated_images/startup.ec211d74fef9f4175010c3334942b715514230415744b9dd0a69a19f4ad68786.ko.png)

다음과 같은 프롬프트를 사용하여

> "이른 아침 햇빛 속 에펠탑 옆의 개"

## DALL-E와 Midjourney란 무엇인가요?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst)와 [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst)는 가장 인기 있는 이미지 생성 모델 중 두 가지로, 프롬프트를 사용하여 이미지를 생성할 수 있습니다.

### DALL-E

DALL-E는 텍스트 설명으로부터 이미지를 생성하는 생성 AI 모델입니다.

> [DALL-E는 두 가지 모델인 CLIP와 diffused attention의 조합입니다](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**은 이미지와 텍스트로부터 데이터를 수치적으로 표현한 임베딩을 생성하는 모델입니다.

- **Diffused attention**은 임베딩으로부터 이미지를 생성하는 모델입니다. DALL-E는 이미지와 텍스트 데이터셋으로 학습되어 텍스트 설명으로부터 이미지를 생성할 수 있습니다. 예를 들어, DALL-E는 모자를 쓴 고양이, 혹은 모히칸 헤어스타일의 개 이미지를 생성할 수 있습니다.

### Midjourney

Midjourney는 DALL-E와 유사하게 텍스트 프롬프트로부터 이미지를 생성합니다. Midjourney는 "모자를 쓴 고양이"나 "모히칸 헤어스타일의 개"와 같은 프롬프트를 사용하여 이미지를 생성할 수 있습니다.

![Midjourney에 의해 생성된 이미지, 기계 비둘기](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_이미지 출처: 위키백과, Midjourney에 의해 생성된 이미지_

## DALL-E와 Midjourney는 어떻게 작동하나요?

먼저, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)입니다. DALL-E는 _자기회귀 트랜스포머_가 포함된 트랜스포머 아키텍처를 기반으로 한 생성 AI 모델입니다.

_자기회귀 트랜스포머_는 모델이 텍스트 설명으로부터 이미지를 생성하는 방법을 정의합니다. 한 번에 한 픽셀씩 생성하고, 생성된 픽셀을 사용하여 다음 픽셀을 생성합니다. 신경망의 여러 계층을 거치면서 이미지가 완성될 때까지 진행됩니다.

이 과정을 통해 DALL-E는 생성된 이미지의 속성, 객체, 특성 등을 제어합니다. 그러나 DALL-E 2와 3는 생성된 이미지에 대한 더 많은 제어를 제공합니다.

## 첫 이미지 생성 애플리케이션 구축

이미지 생성 애플리케이션을 구축하려면 무엇이 필요할까요? 다음과 같은 라이브러리가 필요합니다:

- **python-dotenv**: 이 라이브러리를 사용하여 비밀을 코드와 분리된 _.env_ 파일에 보관하는 것이 권장됩니다.
- **openai**: 이 라이브러리는 OpenAI API와 상호 작용하는 데 사용됩니다.
- **pillow**: Python에서 이미지를 처리하기 위해 사용됩니다.
- **requests**: HTTP 요청을 만드는 데 도움이 됩니다.

1. 다음 내용을 포함한 _.env_ 파일을 생성합니다:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Azure Portal에서 리소스의 "Keys and Endpoint" 섹션에서 이 정보를 찾을 수 있습니다.

1. 위의 라이브러리를 _requirements.txt_라는 파일에 수집합니다:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. 다음으로 가상 환경을 생성하고 라이브러리를 설치합니다:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows의 경우, 가상 환경을 생성하고 활성화하기 위해 다음 명령어를 사용합니다:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_라는 파일에 다음 코드를 추가합니다:

   ```python
   import openai
   import os
   import requests
   from PIL import Image
   import dotenv

   # import dotenv
   dotenv.load_dotenv()

   # Get endpoint and key from environment variables
   openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
   openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

   # Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
   openai.api_version = '2023-06-01-preview'
   openai.api_type = 'azure'


   try:
       # Create an image by using the image generation API
       generation_response = openai.Image.create(
           prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
           size='1024x1024',
           n=2,
           temperature=0,
       )
       # Set the directory for the stored image
       image_dir = os.path.join(os.curdir, 'images')

       # If the directory doesn't exist, create it
       if not os.path.isdir(image_dir):
           os.mkdir(image_dir)

       # Initialize the image path (note the filetype should be png)
       image_path = os.path.join(image_dir, 'generated-image.png')

       # Retrieve the generated image
       image_url = generation_response["data"][0]["url"]  # extract image URL from response
       generated_image = requests.get(image_url).content  # download the image
       with open(image_path, "wb") as image_file:
           image_file.write(generated_image)

       # Display the image in the default image viewer
       image = Image.open(image_path)
       image.show()

   # catch exceptions
   except openai.InvalidRequestError as err:
       print(err)

   ```

이 코드를 설명하겠습니다:

- 먼저, OpenAI 라이브러리, dotenv 라이브러리, requests 라이브러리, Pillow 라이브러리를 포함하여 필요한 라이브러리를 가져옵니다.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- 다음으로, _.env_ 파일에서 환경 변수를 로드합니다.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- 그 후, OpenAI API의 엔드포인트, 키, 버전 및 유형을 설정합니다.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- 다음으로 이미지를 생성합니다:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  위 코드는 생성된 이미지의 URL을 포함하는 JSON 객체로 응답합니다. 우리는 이 URL을 사용하여 이미지를 다운로드하고 파일에 저장할 수 있습니다.

- 마지막으로, 이미지를 열고 표준 이미지 뷰어를 사용하여 표시합니다:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### 이미지 생성에 대한 자세한 내용

이미지를 생성하는 코드를 자세히 살펴보겠습니다:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**는 이미지를 생성하는 데 사용되는 텍스트 프롬프트입니다. 이 경우, "안개 낀 초원에서 말에 올라탄 토끼가 롤리팝을 들고 있는 모습"이라는 프롬프트를 사용하고 있습니다.
- **size**는 생성된 이미지의 크기입니다. 이 경우, 1024x1024 픽셀의 이미지를 생성하고 있습니다.
- **n**은 생성되는 이미지의 수입니다. 이 경우, 두 개의 이미지를 생성하고 있습니다.
- **temperature**는 생성 AI 모델의 출력의 무작위성을 제어하는 매개변수입니다. 온도는 0과 1 사이의 값으로, 0은 출력이 결정적임을 의미하고, 1은 출력이 무작위임을 의미합니다. 기본값은 0.7입니다.

다음 섹션에서는 이미지로 할 수 있는 더 많은 작업에 대해 다룰 것입니다.

## 이미지 생성의 추가 기능

지금까지 Python의 몇 줄로 이미지를 생성할 수 있었습니다. 그러나 이미지로 할 수 있는 더 많은 작업이 있습니다.

다음 작업도 수행할 수 있습니다:

- **편집 수행**. 기존 이미지와 마스크, 프롬프트를 제공하여 이미지를 변경할 수 있습니다. 예를 들어, 이미지의 일부에 무언가를 추가할 수 있습니다. 우리의 토끼 이미지를 상상해보세요. 토끼에 모자를 추가할 수 있습니다. 이렇게 하려면 이미지, 마스크(변경할 부분 식별) 및 텍스트 프롬프트를 제공하여 무엇을 해야 하는지 설명합니다.

  ```python
  response = openai.Image.create_edit(
    image=open("base_image.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="An image of a rabbit with a hat on its head.",
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  기본 이미지는 토끼만 포함하지만 최종 이미지는 토끼에 모자가 추가됩니다.

- **변형 생성**. 기존 이미지를 가져와 변형을 생성하도록 요청하는 것입니다. 변형을 생성하려면 이미지를 제공하고 텍스트 프롬프트와 코드를 다음과 같이 제공합니다:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > 참고: 이는 OpenAI에서만 지원됩니다.

## 온도

온도는 생성 AI 모델의 출력의 무작위성을 제어하는 매개변수입니다. 온도는 0과 1 사이의 값으로, 0은 출력이 결정적임을 의미하고, 1은 출력이 무작위임을 의미합니다. 기본값은 0.7입니다.

온도가 어떻게 작동하는지 예를 들어 보겠습니다. 이 프롬프트를 두 번 실행해보겠습니다:

> 프롬프트: "안개 낀 초원에서 말에 올라탄 토끼가 롤리팝을 들고 있는 모습"

![말에 올라탄 롤리팝을 들고 있는 토끼, 버전 1](../../../translated_images/v1-generated-image.208ba0525ed6ae505504aa852e28d334c0440e9931b7c97f9508176a22d2dd54.ko.png)

이제 동일한 프롬프트를 실행하여 동일한 이미지를 두 번 얻지 않음을 확인해보겠습니다:

![말에 올라탄 토끼의 생성된 이미지](../../../translated_images/v2-generated-image.f0a88c05ef476e95f3682d4b21c9ba2f4807ae71cc29e9c05b42ebbf497cf61b.ko.png)

보시다시피, 이미지는 유사하지만 동일하지 않습니다. 온도 값을 0.1로 변경해 보겠습니다:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### 온도 변경

응답을 더 결정적으로 만들기 위해 시도해 보겠습니다. 두 개의 생성된 이미지를 보면 첫 번째 이미지에는 토끼가 있고 두 번째 이미지에는 말이 있어서 이미지가 크게 다릅니다.

따라서 코드를 변경하여 온도를 0으로 설정해 보겠습니다:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

이 코드를 실행하면 다음 두 이미지를 얻을 수 있습니다:

- ![온도 0, 버전 1](../../../translated_images/v1-temp-generated-image.d8557be792b5c81c2c6d2804cb7b210fe8b340106fe4ffcadf9cf7de1cd7b991.ko.png)
- ![온도 0, 버전 2](../../../translated_images/v2-temp-generated-image.bd412fcfbd43379312b1382212a332aa311ca1a80ea692dea50a8b876a487c61.ko.png)

여기에서 이미지가 서로 더 유사하다는 것을 명확하게 볼 수 있습니다.

## 메타프롬프트로 애플리케이션의 경계를 정의하는 방법

데모를 통해 이미 고객을 위한 이미지를 생성할 수 있습니다. 그러나 애플리케이션에 대한 몇 가지 경계를 만들어야 합니다.

예를 들어, 작업에 부적합하거나 어린이에게 적절하지 않은 이미지를 생성하고 싶지 않습니다.

우리는 이것을 _메타프롬프트_를 사용하여 할 수 있습니다. 메타프롬프트는 생성 AI 모델의 출력을 제어하는 데 사용되는 텍스트 프롬프트입니다. 예를 들어, 메타프롬프트를 사용하여 출력이 작업에 적합하거나 어린이에게 적절한지 확인할 수 있습니다.

### 어떻게 작동하나요?

이제 메타프롬프트가 어떻게 작동하는지 알아보겠습니다.

메타프롬프트는 생성 AI 모델의 출력을 제어하는 데 사용되는 텍스트 프롬프트입니다. 모델의 출력을 제어하기 위해 텍스트 프롬프트 앞에 위치하며, 모델의 출력을 제어하기 위해 애플리케이션에 내장됩니다. 프롬프트 입력과 메타프롬프트 입력을 단일 텍스트 프롬프트에 캡슐화합니다.

메타프롬프트의 한 예는 다음과 같습니다:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

이제 데모에서 메타프롬프트를 어떻게 사용할 수 있는지 보겠습니다.

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

# TODO add request to generate image
```

위의 프롬프트에서 모든 생성된 이미지가 메타프롬프트를 고려하는 것을 볼 수 있습니다.

## 과제 - 학생들을 지원하자

이 강의의 시작에서 Edu4All을 소개했습니다. 이제 학생들이 평가를 위해 이미지를 생성할 수 있도록 지원할 시간입니다.

학생들은 기념물을 포함하는 평가를 위해 이미지를 생성할 것입니다. 어떤 기념물을 선택할지는 학생들에게 달려 있습니다. 학생들은 이 과제에서 창의성을 발휘하여 이러한 기념물을 다양한 맥락에 배치하도록 요청받습니다.

## 해결책

다음은 가능한 해결책 중 하나입니다:

```python
import openai
import os
import requests
from PIL import Image
import dotenv

# import dotenv
dotenv.load_dotenv()

# Get endpoint and key from environment variables
openai.api_base = "<replace with endpoint>"
openai.api_key = "<replace with api key>"

# Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
openai.api_version = '2023-06-01-preview'
openai.api_type = 'azure'

disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}"""

prompt = f"""{metaprompt}
Generate monument of the Arc of Triumph in Paris, France, in the evening light with a small child holding a Teddy looks on.
""""

try:
    # Create an image by using the image generation API
    generation_response = openai.Image.create(
        prompt=prompt,    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    image_url = generation_response["data"][0]["url"]  # extract image URL from response
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
except openai.InvalidRequestError as err:
    print(err)
```

## 훌륭한 작업! 학습을 계속하세요

이 강의를 완료한 후, [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인하여 생성 AI 지식을 계속 향상하세요!

Lesson 10으로 넘어가서 [저코드로 AI 애플리케이션 구축](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)에 대해 알아보세요.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하지만, 자동 번역에는 오류나 부정확한 내용이 포함될 수 있습니다. 원본 문서는 해당 언어로 작성된 문서를 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 오역에 대해 당사는 책임을 지지 않습니다.