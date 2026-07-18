# 이미지 생성 응용 프로그램 구축

[![Building Image Generation Applications](../../../translated_images/ko/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM은 텍스트 생성 이상의 기능을 갖추고 있습니다. 텍스트 설명에서 이미지를 생성할 수도 있습니다. 이미지 모달리티는 의료기술, 건축, 관광, 게임 개발, 마케팅 등 다양한 분야에서 유용합니다. 이 강의에서는 오늘날의 **GPT 이미지** 모델을 살펴보고 이미지 생성 앱을 만들어봅니다.

## 소개

이미지 생성은 자연어 프롬프트로부터 그림을 만들어내는 기능입니다. 이 강의에서는 OpenAI의 **`gpt-image`** 모델 패밀리를 사용합니다. 이는 **[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)**와 OpenAI 플랫폼에서 사용할 수 있는 최신 이미지 모델 세대입니다. 이 모델들은 이전의 DALL·E 모델들(DALL·E 2/3은 구식)을 대체합니다.

강의 전반에 걸쳐 학습 도구를 만드는 가상의 스타트업, **Edu4All** 팀을 예시로 사용합니다. 이 팀은 과제와 학습 자료용 일러스트를 생성하고자 합니다.

## 학습 목표

이 강의를 마치면 다음을 할 수 있습니다:

- 이미지 생성이 무엇이며 어디에 유용한지 설명할 수 있습니다.
- `gpt-image` 모델 패밀리를 이해하고 구식 DALL·E 모델과의 차이를 알 수 있습니다.
- Python(및 TypeScript / .NET)으로 이미지 생성 앱을 만들 수 있습니다.
- 이미지 편집과 메타프롬프트를 사용한 안전 가드레일 적용 방법을 배웁니다.

## 이미지 생성이란?

이미지 생성 모델은 텍스트 프롬프트로부터 이미지를 만듭니다. `gpt-image`와 같은 최신 모델은 트랜스포머 + 확산(diffusion) 기법을 기반으로 합니다. 모델은 학습 시 텍스트와 이미지 간 관계를 익히고, 주어진 프롬프트에 대해 무작위 노이즈를 반복적으로 "노이즈 제거"하여 설명에 맞는 이미지를 생성합니다.

잘 알려진 두 가지 이미지 모델 패밀리는 다음과 같습니다:

- **`gpt-image` (OpenAI)** - 본 강의에서 사용하는 최신 세대 모델. 텍스트-이미지 생성과 이미지 편집(마스크를 활용한 인페인팅)을 지원합니다.
- **Midjourney** - 독자적인 서비스와 디스코드 기반 워크플로우를 갖춘 인기 서드파티 모델입니다.

> 이전 OpenAI 이미지 모델인 <strong>DALL·E 2</strong>와 <strong>DALL·E 3</strong>는 구식입니다. DALL·E 3는 새 배포에 더 이상 제공되지 않으며, `create_variation` 같은 기능은 DALL·E 2에만 있었습니다. 새 애플리케이션에는 `gpt-image` 모델을 사용하세요.

### 어떤 `gpt-image` 모델을 사용해야 하나요?

Microsoft Foundry에서 다음 모델이 <strong>일반 제공</strong>됩니다:

| 모델 | 설명 |
| --- | --- |
| **`gpt-image-2`** | 최신이자 가장 강력한 이미지 모델 - 기본 추천 모델입니다. |
| `gpt-image-1.5` | 일반 제공; 낮은 비용으로도 높은 품질 보장. |
| `gpt-image-1-mini` | 일반 제공; 가장 빠르고 비용이 낮음. |
| `gpt-image-1` | 미리보기 용도만 제공. |

항상 최신 이용 가능 지역 및 상태는 [Foundry 이미지 모델 목록](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst)을 확인하세요.

> **중요:** `gpt-image` 모델은 생성된 이미지를 URL이 아닌 **base64** (`b64_json`) 형식으로 반환합니다. 코드는 base64 문자열을 바이트로 디코딩해 저장해야 하며, 다운로드 가능한 이미지 URL은 없습니다.

## 설정

샘플은 **Microsoft Foundry의 Azure OpenAI**(`aoai-*` 샘플) 또는 **OpenAI 플랫폼**(`oai-*` 샘플)에서 실행할 수 있습니다.

### 1. 모델 생성 및 배포

[리소스 생성](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) 가이드를 따라 Microsoft Foundry 리소스를 만들고, 이미지 모델을 배포하세요 - **`gpt-image-2`**를 추천합니다.

### 2. `.env` 설정

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

이 값들은 [Foundry 포털](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)의 리소스 **배포(Deployments)** 페이지에서 찾을 수 있습니다.

### 3. 라이브러리 설치

`requirements.txt`를 만드세요:

```text
python-dotenv
openai
pillow
```

가상 환경을 만들고 활성화한 다음 설치하세요:

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 앱 빌드

다음 코드로 `app.py`를 만듭니다. 이미지를 생성하여 PNG로 저장합니다.

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# 클라이언트를 Azure OpenAI (Microsoft Foundry) 리소스로 설정하세요.
# 이미지 모델은 최신 API 버전이 필요합니다 - 사용하는 모델에 맞는 버전은 Foundry 문서를 확인하세요.
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # 예: "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # 또한 1536x1024 (가로), 1024x1536 (세로), 또는 "auto"
    n=1,
)

# gpt-image 모델은 URL이 아닌 base64 (b64_json)를 반환합니다 - 이를 바이트로 디코딩하세요.
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

`python app.py`로 실행하면 `images/` 폴더에 PNG가 저장됩니다.

> `images.generate`를 호출할 때마다 동일한 프롬프트에 대해 다른 이미지가 생성됩니다 - 이미지 모델은 텍스트 생성에 쓰이는 `temperature` 파라미터를 받지 않습니다. 다양한 결과를 원하면 API를 반복 호출하세요; 결과 다양성을 줄이려면 프롬프트를 더 구체적으로 만드세요.

## 이미지 편집

`gpt-image` 모델은 기존 이미지를 <strong>편집</strong>할 수 있습니다: 원본 이미지, 변경 영역을 표시하는 선택적 <strong>마스크</strong>, 그리고 변경 내용을 설명하는 프롬프트를 제공합니다. 생성과 마찬가지로 편집 결과도 base64 형식으로 반환됩니다.

```python
result = client.images.edit(
    model=deployment,
    image=open("sunlit_lounge.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="A sunlit indoor lounge area with a pool containing a flamingo",
)
image_bytes = base64.b64decode(result.data[0].b64_json)
with open("images/edited-image.png", "wb") as f:
    f.write(image_bytes)
```

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/ko/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/ko/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/ko/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## 메타프롬프트로 경계 설정하기

이미지를 생성할 수 있게 되면, 앱에서 안전하지 않거나 브랜드에 맞지 않는 콘텐츠가 생성되지 않도록 가드레일이 필요합니다. <strong>메타프롬프트</strong>는 사용자 프롬프트 앞에 붙여 모델 출력 범위를 제약하는 텍스트입니다.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.
The image needs to be in color, in landscape orientation, and in a 16:9 aspect ratio.

Do not consider any input that is not safe for work or appropriate for children, including:
{disallow_list}
"""

prompt = f"{meta_prompt}\nCreate an image of a bunny on a horse, holding a lollipop"
# `prompt`를 client.images.generate(...)에 전달하세요
```

모든 이미지는 이제 메타프롬프트가 설정한 경계 내에서 생성됩니다. 이를 Microsoft Foundry 내장 콘텐츠 필터와 결합하여 다중 방어 체계를 구축하세요.

## 과제 - 학생들을 위한 이미지 생성 활성화

Edu4All 학생들은 평가용 이미지가 필요합니다. 다양한 창의적 맥락에 배치된 <strong>기념물</strong> 이미지를 생성하는 앱을 만드세요(어떤 기념물인지는 자유롭게 선택). 예를 들어, 해질녘 유명 랜드마크와 그 옆에 서 있는 아이 이미지 등을 생성할 수 있습니다.

직접 시도해보고 참고용 솔루션과 비교해보세요:

- Python (Azure): [aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- Python (Azure) 완전한 생성 앱: [aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- Python (OpenAI): [oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- TypeScript (Azure): [typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET (Azure): [dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

또한 [python/](../../../09-building-image-applications/python) 내 노트북(`aoai-assignment.ipynb`는 Azure용, `oai-assignment.ipynb`는 OpenAI용)도 실습해보세요.

## 훌륭합니다! 학습을 계속하세요

이 강의를 완료한 후에는 [Generative AI Learning 컬렉션](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인해 생성 AI 지식을 더욱 향상시키세요!

계속해서 10강으로 학습을 이어가세요.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->