<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef74ad58fc01f7ad80788f79505f9816",
  "translation_date": "2025-08-26T15:21:22+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ko"
}
-->
# 이미지 생성 애플리케이션 만들기

[![이미지 생성 애플리케이션 만들기](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.ko.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM은 텍스트 생성만 가능한 것이 아닙니다. 텍스트 설명을 기반으로 이미지를 생성할 수도 있습니다. 이미지를 활용하는 것은 MedTech, 건축, 관광, 게임 개발 등 다양한 분야에서 매우 유용하게 쓰일 수 있습니다. 이번 챕터에서는 가장 인기 있는 이미지 생성 모델인 DALL-E와 Midjourney에 대해 알아보겠습니다.

## 소개

이번 레슨에서는 다음 내용을 다룹니다:

- 이미지 생성이 무엇이고 왜 유용한지
- DALL-E와 Midjourney가 무엇이고 어떻게 동작하는지
- 이미지 생성 앱을 어떻게 만드는지

## 학습 목표

이 레슨을 마치면 다음을 할 수 있습니다:

- 이미지 생성 애플리케이션을 만들 수 있다.
- 메타 프롬프트로 앱의 경계를 정의할 수 있다.
- DALL-E와 Midjourney를 활용할 수 있다.

## 왜 이미지 생성 애플리케이션을 만들어야 할까요?

이미지 생성 애플리케이션은 생성형 AI의 가능성을 탐구하는 훌륭한 방법입니다. 예를 들어 다음과 같이 활용할 수 있습니다:

- **이미지 편집 및 합성**. 다양한 용도로 이미지를 생성할 수 있습니다. 예를 들어 이미지 편집이나 합성에 사용할 수 있습니다.

- **다양한 산업에 적용**. MedTech, 관광, 게임 개발 등 여러 산업에서 이미지를 생성하는 데 활용할 수 있습니다.

## 시나리오: Edu4All

이번 레슨에서는 스타트업 Edu4All과 함께 계속 작업합니다. 학생들은 자신의 평가를 위해 이미지를 만들게 됩니다. 어떤 이미지를 만들지는 학생들에게 달려 있지만, 동화의 삽화나 새로운 캐릭터를 만들거나 자신의 아이디어와 개념을 시각화하는 데 활용할 수 있습니다.

예를 들어, Edu4All의 학생들이 수업에서 기념물에 대해 작업한다면 다음과 같은 이미지를 생성할 수 있습니다:

![Edu4All 스타트업, 기념물 수업, 에펠탑](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.ko.png)

아래와 같은 프롬프트를 사용해서요.

> "이른 아침 햇살 속 에펠탑 옆에 있는 강아지"

## DALL-E와 Midjourney란?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst)와 [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst)는 가장 인기 있는 이미지 생성 모델입니다. 프롬프트를 입력해 이미지를 만들 수 있습니다.

### DALL-E

먼저 DALL-E부터 살펴보겠습니다. DALL-E는 텍스트 설명을 기반으로 이미지를 생성하는 생성형 AI 모델입니다.

> [DALL-E는 두 가지 모델, CLIP과 diffused attention의 조합입니다](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**은 이미지와 텍스트에서 임베딩(데이터의 수치적 표현)을 생성하는 모델입니다.

- **Diffused attention**은 임베딩을 기반으로 이미지를 생성하는 모델입니다. DALL-E는 이미지와 텍스트 데이터셋으로 학습되어 텍스트 설명을 기반으로 이미지를 만들 수 있습니다. 예를 들어, 모자를 쓴 고양이나 모호크 머리를 한 강아지 이미지를 생성할 수 있습니다.

### Midjourney

Midjourney도 DALL-E와 비슷하게 텍스트 프롬프트로 이미지를 생성합니다. 예를 들어 “모자를 쓴 고양이”나 “모호크 머리를 한 강아지” 같은 프롬프트로 이미지를 만들 수 있습니다.

![Midjourney로 생성된 이미지, 기계 비둘기](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_이미지 출처: Wikipedia, Midjourney로 생성된 이미지_

## DALL-E와 Midjourney는 어떻게 동작할까

먼저 [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)를 살펴보면, DALL-E는 트랜스포머 아키텍처 기반의 생성형 AI 모델로, _오토리그레시브 트랜스포머_를 사용합니다.

_오토리그레시브 트랜스포머_는 모델이 텍스트 설명을 기반으로 이미지를 생성하는 방식을 정의합니다. 한 번에 한 픽셀씩 이미지를 만들고, 생성된 픽셀을 바탕으로 다음 픽셀을 만듭니다. 신경망의 여러 레이어를 거치면서 이미지가 완성됩니다.

이 과정을 통해 DALL-E는 이미지 내의 속성, 객체, 특징 등을 제어할 수 있습니다. DALL-E 2와 3은 생성된 이미지를 더 세밀하게 제어할 수 있습니다.

## 첫 이미지 생성 애플리케이션 만들기

이미지 생성 애플리케이션을 만들려면 다음 라이브러리가 필요합니다:

- **python-dotenv**: 비밀 정보를 코드와 분리된 _.env_ 파일에 저장할 때 추천되는 라이브러리입니다.
- **openai**: OpenAI API와 상호작용할 때 사용하는 라이브러리입니다.
- **pillow**: 파이썬에서 이미지를 다룰 때 사용합니다.
- **requests**: HTTP 요청을 보낼 때 사용합니다.

## Azure OpenAI 모델 생성 및 배포

아직 하지 않았다면, [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) 페이지의 안내를 따라
Azure OpenAI 리소스와 모델을 생성하세요. 모델로 DALL-E 3을 선택합니다.  

## 앱 만들기

1. _.env_ 파일을 만들고 다음 내용을 입력하세요:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   이 정보는 Azure OpenAI Foundry Portal의 "Deployments" 섹션에서 확인할 수 있습니다.

1. 위 라이브러리들을 _requirements.txt_ 파일에 다음과 같이 정리하세요:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. 다음으로, 가상 환경을 만들고 라이브러리를 설치하세요:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows에서는 다음 명령어로 가상 환경을 만들고 활성화할 수 있습니다:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ 파일에 다음 코드를 추가하세요:

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

이 코드를 설명해보겠습니다:

- 먼저 필요한 라이브러리들을 import합니다. OpenAI, dotenv, requests, Pillow 등이 포함됩니다.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- 다음으로 _.env_ 파일에서 환경 변수를 불러옵니다.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- 그 다음 Azure OpenAI 서비스 클라이언트를 설정합니다.

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- 이제 이미지를 생성합니다:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  위 코드는 생성된 이미지의 URL이 담긴 JSON 객체를 반환합니다. 이 URL을 사용해 이미지를 다운로드하고 파일로 저장할 수 있습니다.

- 마지막으로 이미지를 열어서 기본 이미지 뷰어로 보여줍니다:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### 이미지 생성 코드 더 자세히 살펴보기

이미지를 생성하는 코드를 좀 더 자세히 살펴보겠습니다:

    ```python
      generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                            )
    ```

- **prompt**는 이미지를 생성할 때 사용하는 텍스트 프롬프트입니다. 여기서는 "말 위에 있는 토끼, 롤리팝을 들고, 안개 낀 초원에 수선화가 자라는 곳"이라는 프롬프트를 사용했습니다.
- **size**는 생성되는 이미지의 크기입니다. 여기서는 1024x1024 픽셀 이미지를 만듭니다.
- **n**은 생성할 이미지의 개수입니다. 여기서는 두 개의 이미지를 만듭니다.
- **temperature**는 생성형 AI 모델의 출력의 무작위성을 조절하는 파라미터입니다. 0은 결정적, 1은 무작위적 결과를 의미합니다. 기본값은 0.7입니다.

이미지로 할 수 있는 더 많은 기능은 다음 섹션에서 다룹니다.

## 이미지 생성의 추가 기능

지금까지 파이썬 몇 줄로 이미지를 생성하는 방법을 살펴봤습니다. 하지만 이미지로 할 수 있는 일이 더 많습니다.

다음과 같은 작업도 가능합니다:

- **이미지 편집**. 기존 이미지, 마스크, 프롬프트를 제공해 이미지를 변경할 수 있습니다. 예를 들어 이미지의 일부에 무언가를 추가할 수 있습니다. 예를 들어 토끼 이미지에 모자를 씌우고 싶다면, 이미지와 마스크(변경할 영역 지정), 그리고 텍스트 프롬프트를 제공하면 됩니다.
> 참고: DALL-E 3에서는 지원되지 않습니다.
 
아래는 GPT Image를 활용한 예시입니다:

    ```python
    response = client.images.edit(
        model="gpt-image-1",
        image=open("sunlit_lounge.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt="A sunlit indoor lounge area with a pool containing a flamingo"
    )
    image_url = response.data[0].url
    ```

  기본 이미지는 수영장이 있는 라운지이고, 최종 이미지는 플라밍고가 추가됩니다:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="./images/sunlit_lounge.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/mask.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/sunlit_lounge_result.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **변형 만들기**. 기존 이미지를 바탕으로 변형 이미지를 만들 수 있습니다. 이미지를 제공하고 텍스트 프롬프트와 코드를 사용하면 됩니다:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > 참고: 이 기능은 OpenAI에서만 지원됩니다.

## Temperature

Temperature는 생성형 AI 모델의 출력의 무작위성을 조절하는 파라미터입니다. 0은 결정적, 1은 무작위적 결과를 의미합니다. 기본값은 0.7입니다.

Temperature가 어떻게 동작하는지 예시를 살펴보겠습니다. 아래 프롬프트를 두 번 실행해봅니다:

> 프롬프트 : "말 위에 있는 토끼, 롤리팝을 들고, 안개 낀 초원에 수선화가 자라는 곳"

![말 위에 롤리팝을 든 토끼, 버전 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.ko.png)

같은 프롬프트를 다시 실행하면, 똑같은 이미지는 나오지 않습니다:

![말 위에 있는 토끼 이미지](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.ko.png)

이미지가 비슷하지만 완전히 같지는 않다는 것을 볼 수 있습니다. 이제 temperature 값을 0.1로 바꿔보겠습니다:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Temperature 값 변경하기

응답을 더 결정적으로 만들고 싶다면 어떻게 해야 할까요? 앞서 생성한 두 이미지를 보면 첫 번째에는 토끼가, 두 번째에는 말이 강조되어 이미지가 꽤 다릅니다.

그래서 코드를 수정해 temperature를 0으로 설정해봅니다:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

이제 코드를 실행하면 다음 두 이미지를 얻을 수 있습니다:

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.ko.png)
- ![Temperature 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.ko.png)

두 이미지가 훨씬 더 닮아 있는 것을 확인할 수 있습니다.

## 메타프롬프트로 앱의 경계 정의하기

데모를 통해 이미 클라이언트를 위한 이미지를 생성할 수 있습니다. 하지만 애플리케이션에 경계를 설정할 필요가 있습니다.

예를 들어, 업무에 적합하지 않거나 어린이에게 부적절한 이미지는 생성하지 않도록 해야 합니다.

이럴 때 _메타프롬프트_를 사용할 수 있습니다. 메타프롬프트는 생성형 AI 모델의 출력을 제어하는 텍스트 프롬프트입니다. 예를 들어, 메타프롬프트를 활용해 생성되는 이미지가 업무에 적합하거나 어린이에게 적합하도록 할 수 있습니다.

### 어떻게 동작할까?

메타프롬프트는 생성형 AI 모델의 출력을 제어하는 텍스트 프롬프트입니다. 프롬프트 앞에 위치하며, 모델의 출력을 제어하는 역할을 합니다. 애플리케이션에 내장되어 프롬프트 입력과 메타프롬프트 입력을 하나의 텍스트 프롬프트로 캡슐화합니다.

메타프롬프트의 예시는 다음과 같습니다:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

이제 데모에서 메타프롬프트를 어떻게 활용할 수 있는지 살펴보겠습니다.

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

위 프롬프트를 보면, 생성되는 모든 이미지가 메타프롬프트를 고려하게 됩니다.

## 과제 - 학생들에게 이미지 생성 기능 제공하기

이번 레슨의 시작에서 Edu4All을 소개했습니다. 이제 학생들이 자신의 평가를 위해 이미지를 생성할 수 있도록 해봅시다.

학생들은 기념물이 포함된 이미지를 만들게 됩니다. 어떤 기념물을 선택할지는 학생들에게 달려 있습니다. 학생들은 창의력을 발휘해 다양한 맥락에서 기념물을 배치해보세요.

## 해결 방법

가능한 해결 방법 예시는 다음과 같습니다:

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

## 수고하셨습니다! 계속해서 학습을 이어가세요
이 강의를 마친 후에는 [생성형 AI 학습 컬렉션](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인하여 생성형 AI에 대한 지식을 계속 쌓아보세요!

다음 10강에서는 [로우코드로 AI 애플리케이션을 만드는 방법](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)에 대해 알아봅니다.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서(원어)가 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 오해나 오역에 대해 당사는 책임을 지지 않습니다.