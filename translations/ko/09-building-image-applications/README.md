<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-06-25T17:10:28+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ko"
}
-->
# 이미지 생성 애플리케이션 구축하기

텍스트 생성 외에도 LLM에는 더 많은 기능이 있습니다. 텍스트 설명으로부터 이미지를 생성하는 것도 가능합니다. 이미지를 모달리티로 활용하는 것은 MedTech, 건축, 관광, 게임 개발 등 여러 분야에서 매우 유용할 수 있습니다. 이 장에서는 가장 인기 있는 이미지 생성 모델인 DALL-E와 Midjourney에 대해 살펴보겠습니다.

## 소개

이 강의에서 다룰 내용은 다음과 같습니다:

- 이미지 생성 및 그 유용성
- DALL-E와 Midjourney, 이들이 무엇인지 그리고 어떻게 작동하는지
- 이미지 생성 앱을 구축하는 방법

## 학습 목표

이 강의를 완료하면 다음을 할 수 있습니다:

- 이미지 생성 애플리케이션 구축하기
- 메타 프롬프트로 애플리케이션의 경계를 정의하기
- DALL-E와 Midjourney 사용하기

## 왜 이미지 생성 애플리케이션을 구축해야 할까요?

이미지 생성 애플리케이션은 생성적 AI의 가능성을 탐구하는 훌륭한 방법입니다. 예를 들어, 다음과 같은 용도로 사용할 수 있습니다:

- **이미지 편집 및 합성**. 다양한 사용 사례를 위한 이미지를 생성할 수 있습니다. 예를 들어 이미지 편집 및 이미지 합성.

- **다양한 산업에 적용**. MedTech, 관광, 게임 개발 등 다양한 산업에서 이미지를 생성하는 데 사용할 수 있습니다.

## 시나리오: Edu4All

이 강의의 일환으로, 우리는 Edu4All이라는 스타트업과 계속 작업할 것입니다. 학생들은 평가를 위한 이미지를 생성할 것이며, 어떤 이미지를 만들지는 학생들에게 달려 있습니다. 그들은 자신의 동화에 대한 삽화를 만들거나 이야기의 새로운 캐릭터를 만들거나 아이디어와 개념을 시각화하는 데 도움을 받을 수 있습니다.

예를 들어, 학생들이 기념물에 대한 수업을 진행 중이라면 Edu4All의 학생들이 생성할 수 있는 것은 다음과 같습니다:

"아침 햇살 속 에펠탑 옆의 개"

## DALL-E와 Midjourney란 무엇인가요?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst)와 [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst)는 가장 인기 있는 이미지 생성 모델 중 두 가지로, 프롬프트를 사용하여 이미지를 생성할 수 있습니다.

### DALL-E

DALL-E는 텍스트 설명으로부터 이미지를 생성하는 생성적 AI 모델입니다.

- **CLIP**은 이미지와 텍스트로부터 데이터의 수치적 표현인 임베딩을 생성하는 모델입니다.

- **Diffused attention**은 임베딩으로부터 이미지를 생성하는 모델입니다. DALL-E는 이미지와 텍스트 데이터셋으로 훈련되어 텍스트 설명으로부터 이미지를 생성할 수 있습니다. 예를 들어, DALL-E는 모자를 쓴 고양이 또는 모히칸 헤어스타일을 한 개의 이미지를 생성할 수 있습니다.

### Midjourney

Midjourney는 DALL-E와 유사하게 텍스트 프롬프트로부터 이미지를 생성합니다. "모자를 쓴 고양이" 또는 "모히칸 헤어스타일을 한 개"와 같은 프롬프트를 사용하여 이미지를 생성할 수 있습니다.

## DALL-E와 Midjourney의 작동 원리

[DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)는 _오토리그레시브 트랜스포머_ 아키텍처를 기반으로 한 생성적 AI 모델입니다.

오토리그레시브 트랜스포머는 텍스트 설명으로부터 이미지를 생성하는 방식을 정의하며, 한 번에 한 픽셀씩 생성하고 생성된 픽셀을 사용하여 다음 픽셀을 생성합니다. 신경망의 여러 계층을 통과하여 이미지가 완성됩니다.

이 과정에서 DALL-E는 생성하는 이미지의 속성, 객체, 특성 등을 제어합니다. 하지만 DALL-E 2와 3은 생성된 이미지에 대해 더 많은 제어가 가능합니다.

## 첫 번째 이미지 생성 애플리케이션 구축하기

이미지 생성 애플리케이션을 구축하려면 다음 라이브러리가 필요합니다:

- **python-dotenv**, 비밀 정보를 코드에서 분리하여 _.env_ 파일에 저장하는 것을 권장합니다.
- **openai**, OpenAI API와 상호 작용하는 데 사용할 라이브러리입니다.
- **pillow**, Python에서 이미지를 다루기 위한 라이브러리입니다.
- **requests**, HTTP 요청을 쉽게 수행할 수 있도록 도와주는 라이브러리입니다.

1. 다음 내용으로 _.env_ 파일을 생성합니다:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Azure Portal에서 리소스의 "Keys and Endpoint" 섹션에서 이 정보를 찾을 수 있습니다.

1. 위의 라이브러리를 _requirements.txt_ 파일에 수집합니다:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. 가상 환경을 생성하고 라이브러리를 설치합니다:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows의 경우 다음 명령어를 사용하여 가상 환경을 생성하고 활성화합니다:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ 파일에 다음 코드를 추가합니다:

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

이 코드를 설명해보겠습니다:

- 먼저, 필요한 라이브러리를 import합니다. OpenAI 라이브러리, dotenv 라이브러리, requests 라이브러리, Pillow 라이브러리를 포함합니다.

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

- 다음으로, 이미지를 생성합니다:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  위의 코드는 생성된 이미지의 URL을 포함하는 JSON 객체로 응답합니다. 이 URL을 사용하여 이미지를 다운로드하고 파일에 저장할 수 있습니다.

- 마지막으로, 이미지를 열고 표준 이미지 뷰어를 사용하여 표시합니다:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### 이미지 생성에 대한 자세한 설명

이미지를 생성하는 코드를 자세히 살펴보겠습니다:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**는 이미지를 생성하는 데 사용되는 텍스트 프롬프트입니다. 이 경우 "안개 낀 초원에서 사탕을 들고 있는 말 위의 토끼"라는 프롬프트를 사용하고 있습니다.
- **size**는 생성된 이미지의 크기입니다. 이 경우 1024x1024 픽셀의 이미지를 생성합니다.
- **n**은 생성되는 이미지의 수입니다. 이 경우 두 개의 이미지를 생성합니다.
- **temperature**는 생성적 AI 모델의 출력의 무작위성을 제어하는 매개변수입니다. 온도는 0에서 1 사이의 값으로, 0은 출력이 결정적이고 1은 출력이 무작위임을 의미합니다. 기본값은 0.7입니다.

이미지와 관련하여 할 수 있는 더 많은 작업은 다음 섹션에서 다룰 것입니다.

## 이미지 생성의 추가 기능

지금까지 Python의 몇 줄을 사용하여 이미지를 생성하는 방법을 살펴보았습니다. 하지만 이미지와 관련하여 할 수 있는 더 많은 작업이 있습니다.

다음과 같은 작업도 가능합니다:

- **편집 수행**. 기존 이미지에 마스크와 프롬프트를 제공하여 이미지를 변경할 수 있습니다. 예를 들어, 이미지의 일부에 무언가를 추가할 수 있습니다. 예를 들어, 토끼 이미지에 모자를 추가할 수 있습니다. 이미지를 제공하고, 마스크(변경할 영역을 식별하는)와 텍스트 프롬프트를 제공하여 수행합니다.

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

  기본 이미지는 토끼만 포함되지만 최종 이미지는 토끼 위에 모자가 있습니다.

- **변형 생성**. 기존 이미지를 사용하여 변형을 생성합니다. 변형을 생성하려면 이미지를 제공하고 텍스트 프롬프트와 코드를 제공합니다:

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

온도는 생성적 AI 모델의 출력의 무작위성을 제어하는 매개변수입니다. 온도는 0에서 1 사이의 값으로, 0은 출력이 결정적이고 1은 출력이 무작위임을 의미합니다. 기본값은 0.7입니다.

온도가 어떻게 작동하는지 예를 들어 보겠습니다. 다음 프롬프트를 두 번 실행해 보겠습니다:

> 프롬프트: "안개 낀 초원에서 사탕을 들고 있는 말 위의 토끼"

이제 동일한 프롬프트를 실행하여 동일한 이미지를 두 번 얻을 수 없음을 확인해 보겠습니다:

이미지가 유사하지만 동일하지 않습니다. 온도 값을 0.1로 변경하고 어떤 일이 일어나는지 보겠습니다:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### 온도 변경

반응을 더 결정적으로 만들기 위해 코드를 변경하고 온도를 0으로 설정해 보겠습니다:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

이제 이 코드를 실행하면 다음 두 이미지를 얻을 수 있습니다:

여기서 이미지를 더 많이 닮았다는 것을 명확히 알 수 있습니다.

## 메타프롬프트로 애플리케이션의 경계를 정의하는 방법

데모를 통해 우리는 이미 고객을 위한 이미지를 생성할 수 있습니다. 그러나 애플리케이션의 경계를 설정해야 합니다.

예를 들어, 작업에 적합하지 않거나 어린이에게 적절하지 않은 이미지를 생성하고 싶지 않습니다.

이것을 _메타프롬프트_로 해결할 수 있습니다. 메타프롬프트는 생성적 AI 모델의 출력을 제어하는 데 사용되는 텍스트 프롬프트입니다. 예를 들어, 메타프롬프트를 사용하여 출력이 작업에 적합하거나 어린이에게 적절한지 확인할 수 있습니다.

### 어떻게 작동하나요?

메타프롬프트는 생성적 AI 모델의 출력을 제어하는 데 사용되는 텍스트 프롬프트입니다. 이들은 텍스트 프롬프트 앞에 위치하며, 모델의 출력을 제어하고 애플리케이션에 포함되어 모델의 출력을 제어하는 데 사용됩니다. 프롬프트 입력과 메타프롬프트 입력을 단일 텍스트 프롬프트에 캡슐화합니다.

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

이제 데모에서 메타프롬프트를 사용하는 방법을 살펴보겠습니다.

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

위의 프롬프트에서 모든 생성된 이미지가 메타프롬프트를 고려하고 있음을 알 수 있습니다.

## 과제 - 학생들을 지원하자

이 강의의 시작 부분에서 Edu4All을 소개했습니다. 이제 학생들이 평가를 위한 이미지를 생성할 수 있도록 지원할 때입니다.

학생들은 평가에 포함될 기념물의 이미지를 생성할 것입니다. 어떤 기념물을 생성할지는 학생들에게 달려 있습니다. 학생들은 이 작업에서 창의력을 발휘하여 다양한 맥락에서 이 기념물을 배치하도록 요청받았습니다.

## 솔루션

다음은 가능한 솔루션 중 하나입니다:

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

이 강의를 완료한 후, [Generative AI 학습 컬렉션](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인하여 Generative AI 지식을 계속 향상시키세요!

다음은 [저코드로 AI 애플리케이션 구축하기](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)에 대해 알아볼 수 있는 10번째 강의로 이동하세요.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 우리는 정확성을 위해 노력하지만, 자동 번역에는 오류나 부정확성이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 본래 언어 버전이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인한 오해나 잘못된 해석에 대해서는 책임을 지지 않습니다.