<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "063a2ac57d6b71bea0eaa880c68770d2",
  "translation_date": "2025-09-29T21:34:00+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ko"
}
-->
# 이미지 생성 애플리케이션 구축하기

[![이미지 생성 애플리케이션 구축하기](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.ko.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM은 텍스트 생성만이 아닙니다. 텍스트 설명을 기반으로 이미지를 생성하는 것도 가능합니다. 이미지를 활용하는 것은 MedTech, 건축, 관광, 게임 개발 등 다양한 분야에서 매우 유용할 수 있습니다. 이 장에서는 가장 인기 있는 이미지 생성 모델인 DALL-E와 Midjourney를 살펴보겠습니다.

## 소개

이 강의에서는 다음 내용을 다룹니다:

- 이미지 생성과 그 유용성.
- DALL-E와 Midjourney가 무엇이며, 어떻게 작동하는지.
- 이미지 생성 애플리케이션을 구축하는 방법.

## 학습 목표

이 강의를 완료한 후, 여러분은 다음을 할 수 있습니다:

- 이미지 생성 애플리케이션을 구축하기.
- 메타 프롬프트를 사용하여 애플리케이션의 경계를 정의하기.
- DALL-E와 Midjourney를 활용하기.

## 왜 이미지 생성 애플리케이션을 구축해야 할까요?

이미지 생성 애플리케이션은 생성형 AI의 가능성을 탐구하는 훌륭한 방법입니다. 예를 들어, 다음과 같은 용도로 사용할 수 있습니다:

- **이미지 편집 및 합성**. 다양한 사용 사례를 위해 이미지를 생성할 수 있습니다. 예를 들어 이미지 편집 및 합성.

- **다양한 산업에 적용**. MedTech, 관광, 게임 개발 등 다양한 산업에서 이미지를 생성하는 데 사용할 수 있습니다.

## 시나리오: Edu4All

이 강의의 일환으로, 우리는 Edu4All이라는 스타트업과 계속 작업할 것입니다. 학생들은 자신의 평가를 위해 이미지를 생성할 것입니다. 어떤 이미지를 생성할지는 학생들에게 달려 있지만, 자신의 동화에 대한 삽화를 만들거나 새로운 캐릭터를 창조하거나 아이디어와 개념을 시각화하는 데 도움을 줄 수 있습니다.

예를 들어, Edu4All의 학생들이 기념물에 대한 수업을 진행 중이라면 다음과 같은 이미지를 생성할 수 있습니다:

![Edu4All 스타트업, 기념물 수업, 에펠탑](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.ko.png)

다음과 같은 프롬프트를 사용하여:

> "이른 아침 햇빛 속에서 에펠탑 옆에 있는 개"

## DALL-E와 Midjourney란 무엇인가요?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst)와 [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst)는 가장 인기 있는 이미지 생성 모델 중 두 가지로, 프롬프트를 사용하여 이미지를 생성할 수 있습니다.

### DALL-E

먼저 DALL-E를 살펴보겠습니다. DALL-E는 텍스트 설명을 기반으로 이미지를 생성하는 생성형 AI 모델입니다.

> [DALL-E는 CLIP과 확산 주의(diffused attention)라는 두 가지 모델의 조합입니다](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**은 이미지와 텍스트에서 데이터의 수치적 표현인 임베딩을 생성하는 모델입니다.

- **확산 주의(diffused attention)**는 임베딩을 기반으로 이미지를 생성하는 모델입니다. DALL-E는 이미지와 텍스트 데이터셋으로 학습되었으며, 텍스트 설명을 기반으로 이미지를 생성하는 데 사용할 수 있습니다. 예를 들어, DALL-E는 모자를 쓴 고양이 또는 모호크 헤어스타일을 한 개의 이미지를 생성할 수 있습니다.

### Midjourney

Midjourney는 DALL-E와 유사하게 텍스트 프롬프트를 사용하여 이미지를 생성합니다. Midjourney는 "모자를 쓴 고양이" 또는 "모호크 헤어스타일을 한 개"와 같은 프롬프트를 사용하여 이미지를 생성할 수 있습니다.

![Midjourney로 생성된 이미지, 기계 비둘기](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_이미지 출처: Wikipedia, Midjourney로 생성된 이미지_

## DALL-E와 Midjourney는 어떻게 작동하나요?

먼저 [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)를 살펴보겠습니다. DALL-E는 _자동회귀 변환기(autoregressive transformer)_를 사용하는 변환기 아키텍처를 기반으로 한 생성형 AI 모델입니다.

_자동회귀 변환기_는 모델이 텍스트 설명에서 이미지를 생성하는 방식을 정의합니다. 한 번에 한 픽셀을 생성하고, 생성된 픽셀을 사용하여 다음 픽셀을 생성합니다. 신경망의 여러 레이어를 통과하여 이미지가 완성될 때까지 이 과정을 반복합니다.

이 과정을 통해 DALL-E는 생성된 이미지에서 속성, 객체, 특성 등을 제어합니다. 그러나 DALL-E 2와 3은 생성된 이미지를 더 세밀하게 제어할 수 있습니다.

## 첫 번째 이미지 생성 애플리케이션 구축하기

이미지 생성 애플리케이션을 구축하려면 다음 라이브러리가 필요합니다:

- **python-dotenv**: 비밀 정보를 코드에서 분리하여 _.env_ 파일에 저장하는 데 권장되는 라이브러리입니다.
- **openai**: OpenAI API와 상호작용하는 데 사용하는 라이브러리입니다.
- **pillow**: Python에서 이미지를 처리하는 데 사용하는 라이브러리입니다.
- **requests**: HTTP 요청을 수행하는 데 도움을 주는 라이브러리입니다.

## Azure OpenAI 모델 생성 및 배포

아직 완료하지 않았다면, [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) 페이지의 지침을 따라 Azure OpenAI 리소스와 모델을 생성하세요. 모델로 DALL-E 3을 선택합니다.

## 애플리케이션 생성하기

1. 다음 내용을 포함하는 _.env_ 파일을 생성하세요:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   이 정보를 Azure OpenAI Foundry Portal의 "배포" 섹션에서 찾을 수 있습니다.

1. 위의 라이브러리를 _requirements.txt_ 파일에 다음과 같이 수집하세요:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. 다음으로, 가상 환경을 생성하고 라이브러리를 설치하세요:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows에서는 다음 명령어를 사용하여 가상 환경을 생성하고 활성화하세요:

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
    
    # configure Azure OpenAI service client 
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
    try:
        # Create an image by using the image generation API
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # Set the directory for the stored image
        image_dir = os.path.join(os.curdir, 'images')

        # If the directory doesn't exist, create it
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Initialize the image path (note the filetype should be png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Retrieve the generated image
        image_url = generation_response.data[0].url  # extract image URL from response
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

- 그 후, Azure OpenAI 서비스 클라이언트를 구성합니다.

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- 다음으로, 이미지를 생성합니다:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  위 코드는 생성된 이미지의 URL을 포함하는 JSON 객체로 응답합니다. 이 URL을 사용하여 이미지를 다운로드하고 파일로 저장할 수 있습니다.

- 마지막으로, 이미지를 열고 표준 이미지 뷰어를 사용하여 표시합니다:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### 이미지 생성에 대한 자세한 내용

이미지를 생성하는 코드를 자세히 살펴보겠습니다:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**: 이미지를 생성하는 데 사용되는 텍스트 프롬프트입니다. 여기서는 "안개 낀 초원에서 수선화가 자라는 곳에 말 위에 앉아 막대사탕을 들고 있는 토끼"라는 프롬프트를 사용하고 있습니다.
- **size**: 생성된 이미지의 크기입니다. 여기서는 1024x1024 픽셀 크기의 이미지를 생성합니다.
- **n**: 생성된 이미지의 수입니다. 여기서는 두 개의 이미지를 생성합니다.
- **temperature**: 생성형 AI 모델의 출력의 무작위성을 제어하는 매개변수입니다. 온도는 0에서 1 사이의 값으로, 0은 출력이 결정적이고 1은 출력이 무작위임을 의미합니다. 기본값은 0.7입니다.

이미지로 할 수 있는 더 많은 작업은 다음 섹션에서 다루겠습니다.

## 이미지 생성의 추가 기능

지금까지 Python에서 몇 줄의 코드로 이미지를 생성하는 방법을 살펴보았습니다. 그러나 이미지로 할 수 있는 더 많은 작업이 있습니다.

다음 작업도 수행할 수 있습니다:

- **편집 수행**. 기존 이미지, 마스크 및 프롬프트를 제공하여 이미지를 변경할 수 있습니다. 예를 들어, 이미지의 일부에 무언가를 추가할 수 있습니다. 우리의 토끼 이미지에서 토끼에게 모자를 추가할 수 있습니다. 이를 수행하려면 이미지, 마스크(변경할 영역 식별) 및 텍스트 프롬프트를 제공하여 작업을 지정합니다.
> 참고: DALL-E 3에서는 지원되지 않습니다.

다음은 GPT Image를 사용하는 예입니다:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  기본 이미지는 수영장이 있는 라운지만 포함하지만 최종 이미지는 플라밍고를 포함합니다:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.ko.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.ko.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.ko.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **변형 생성**. 기존 이미지를 가져와 변형을 생성하도록 요청할 수 있습니다. 변형을 생성하려면 이미지와 텍스트 프롬프트를 제공하고 다음과 같은 코드를 사용합니다:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > 참고: OpenAI에서만 지원됩니다.

## 온도

온도는 생성형 AI 모델의 출력의 무작위성을 제어하는 매개변수입니다. 온도는 0에서 1 사이의 값으로, 0은 출력이 결정적이고 1은 출력이 무작위임을 의미합니다. 기본값은 0.7입니다.

온도가 어떻게 작동하는지 예제를 통해 살펴보겠습니다. 다음 프롬프트를 두 번 실행합니다:

> 프롬프트: "안개 낀 초원에서 수선화가 자라는 곳에 말 위에 앉아 막대사탕을 들고 있는 토끼"

![말 위에 앉아 막대사탕을 들고 있는 토끼, 버전 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.ko.png)

이제 동일한 프롬프트를 실행하여 동일한 이미지를 두 번 생성하지 않는다는 것을 확인해보겠습니다:

![말 위에 앉아 있는 토끼가 있는 생성된 이미지](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.ko.png)

보시다시피, 이미지는 비슷하지만 동일하지 않습니다. 이제 온도 값을 0.1로 변경해보겠습니다:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### 온도 변경하기

응답을 더 결정적으로 만들기 위해 코드를 변경해보겠습니다. 첫 번째 이미지에서는 토끼가 있고 두 번째 이미지에서는 말이 있는 것을 관찰할 수 있으므로, 이미지가 크게 다릅니다.

따라서 코드를 변경하여 온도를 0으로 설정합니다:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

이제 이 코드를 실행하면 다음 두 이미지를 얻을 수 있습니다:

- ![온도 0, 버전 1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.ko.png)
- ![온도 0, 버전 2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.ko.png)

여기서 두 이미지가 더 비슷해진 것을 명확히 볼 수 있습니다.

## 메타 프롬프트로 애플리케이션의 경계를 정의하는 방법

데모를 통해 이미 고객을 위한 이미지를 생성할 수 있습니다. 그러나 애플리케이션에 몇 가지 경계를 설정해야 합니다.

예를 들어, 작업 환경에 적합하지 않거나 어린이에게 적합하지 않은 이미지를 생성하지 않도록 해야 합니다.

이를 _메타 프롬프트_를 사용하여 수행할 수 있습니다. 메타 프롬프트는 생성형 AI 모델의 출력을 제어하는 데 사용되는 텍스트 프롬프트입니다. 예를 들어, 메타 프롬프트를 사용하여 출력이 작업 환경에 적합하거나 어린이에게 적합하도록 제어할 수 있습니다.

### 어떻게 작동하나요?

메타 프롬프트는 생성형 AI 모델의 출력을 제어하는 데 사용되는 텍스트 프롬프트입니다. 텍스트 프롬프트 앞에 위치하며, 모델의 출력을 제어하고 애플리케이션에 포함되어 모델의 출력을 제어합니다. 프롬프트 입력과 메타 프롬프트 입력을 단일 텍스트 프롬프트로 캡슐화합니다.

메타 프롬프트의 한 예는 다음과 같습니다:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

이제 데모에서 메타 프롬프트를 사용하는 방법을 살펴보겠습니다.

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

위의 프롬프트에서 모든 생성된 이미지가 메타 프롬프트를 고려하는 것을 볼 수 있습니다.

## 과제 - 학생들을 지원해봅시다

이 강의 초반에 Edu4All을 소개했습니다. 이제 학생들이 자신의 평가를 위해 이미지를 생성할 수 있도록 지원할 때입니다.

학생들은 기념물을 포함하는 평가 이미지를 생성할 것입니다. 어떤 기념물을 선택할지는 학생들에게 달려 있습니다. 학생들은 이 과제에서 창의력을 발휘하여 이러한 기념물을 다양한 맥락에 배치하도록 요청받습니다.

## 솔루션

다음은 가능한 솔루션 중 하나입니다:
```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# import dotenv
dotenv.load_dotenv()

# Get endpoint and key from environment variables
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
  api_key=os.environ['AZURE_OPENAI_API_KEY'],
  api_version = "2024-02-01"
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
""""

try:
    # Create an image by using the image generation API
    generation_response = client.images.generate(
        prompt=prompt,    # Enter your prompt text here
        size='1024x1024',
        n=1,
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    image_url = generation_response.data[0].url  # extract image URL from response
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
except openai.BadRequestError as err:
    print(err)
```

## 훌륭합니다! 학습을 계속하세요

이 강의를 완료한 후, [Generative AI 학습 컬렉션](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인하여 생성형 AI 지식을 더욱 향상시켜 보세요!

Lesson 10으로 이동하여 [저코드로 AI 애플리케이션을 구축하는 방법](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)을 살펴보겠습니다.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.