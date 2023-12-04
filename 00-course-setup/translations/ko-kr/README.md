# 이 강좌 시작하기

여러분이 이 강좌를 시작하고 생성형 AI로 무엇을 만들게 될지 볼 수 있게 되어 매우 기쁩니다!

여러분의 학습이 성공적이 되도록, 이 페이지에 필요한 설정 단계, 기술 요구 사항, 필요할 때 도움을 받는 방법을 정리했습니다.

## 설정 단계

이 강좌를 시작하기 위해 다음 단계들을 완료해야 합니다.

### 1. 이 저장소 포크하기

[이 전체 저장소를 포크](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)해서 어떤 코드든 변경하고 도전 과제를 완료할 수 있습니다. 또한 [이 저장소에 별표(🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)를 해서 관련 저장소들을 더 쉽게 찾을 수도 있습니다.

### 2. 코드스페이스 만들기

코드를 실행할 때 의존성 문제를 피하기 위해, 이 강좌를 GitHub 코드스페이스에서 실행하는 것을 추천합니다.

이는 여러분이 포크한 이 저장소에서 `Code` 옵션을 선택하고 **Codespaces** 옵션을 선택하여 만들 수 있습니다.

### 3. API 키 저장하기

어떤 종료의 어플리케이션을 구축할 때, API 키를 안전하게 보관하는 것은 중요합니다. 어려분이 작업하는 코드 내에 직접 API 키를 저장하는 것은 권장하지 않습니다. 이러한 세부 정보를 공개 저장소에 커밋하면 원치 않는 비용과 문제가 발생할 수 있습니다.


![코드스페이스를 생성하기 위한 버튼을 보여주는 대화상자](../../images/who-will-pay.webp?WT.mc_id=academic-105485-koreyst)

## 컴퓨터에서 로컬로 실행하는 방법

컴퓨터에서 코드를 로컬로 실행하려면, [Python의 어떤 버전이 설치](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)되어 있어야 합니다.

저장소를 사용하려면 다음과 같이 클론해야합니다:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

이제 checkout하고 학습하며 코드화 함께 작업할 수 있습니다.

### 미니콘다 설치하기 (옵션)

**미니콘다**를 설치하는 것은 장점이 있습니다. - 이는 `conda`패키지 관리자를 지원하는 비교적 가볍게 설치할 수 있고, 다양한 Python **가상 환경**에서 유용합니다. `conda`는 다양한 Python 버전과 패키지를 쉽게 설치하고 전환할 수 있게 해주며, `pip`를 통해 사용할 수 없는 패키지도 설치할 수 있습니다.

미니콘다를 설치한 후, 아직 저장소를 클론하지 않았다면 클론하고 이 강좌를 위한 가상 환경을 만들어야 합니다:

아래 단계를 실행하기 전에, 먼저 *environment.yml* 파일이 있는지 확인하세요. *environment.yml* 파일은 필요한 의존성을 가진 conda 환경을 만드는 데 사용되며, 다음과 같습니다:

```yml
name: <environment-name>
channels:  
 - defaults
dependencies:  
- python=<python-version>  
- openai  
- python-dotenv
```

`<environment-name`을 여러분의 conda 환경 이름으로, `<python-version>`을 사용하고자 하는 Python 버전으로 바꿀 수 있습니다. 생성한 *environment.yml* 파일을 여러분의 저장소의 *.devcontainer* 폴더에 넣으세요.

이제 *environment.yml* 파일을 만들었다면, 다음 명령어로 conda 환경을 생성할 수 있습니다:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

문제가 발생할 경우, 이 링크에서 [conda 환경](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) 생성에 대해 참고하세요.

### Python 확장 기능을 찾춘 비주얼 스튜디오 코드 사용하기

이 교육 과정에서 가장 좋은 방법은 [비주얼 스튜디오 코드](http://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst)에서 [Python 확장 기능](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)을 함께 사용하는 것입니다.

> **참고**: 저장소를 클론하고 VS Code에서 디렉토리를 열면, 자동으로 파이썬 확장 기능을 설치하라는 제안을 받게 됩니다. 위에서 설명한대로 미니콘다도 설치해야합니다.

> **참고**: VS Code가 컨테이너에서 저장소를 다시 열라고 제안한다면, 로컬 파이썬 설치를 사용하기 위해 이를 거부해야합니다.

### 브라우저에서 주피터 사용하기

자신의 컴퓨터 브라우저에서 주피터 환경을 사용할 수도 있습니다. 실제로, 고전적인 주피터와 주피터 허브 모두 자동완성, 코드 하이라이트 등 편리한 개발 환경을 제공합니다.

로컬에서 주피터를 시작하려면, 강좌의 디렉토리로 이동하여 다음을 실행하세요:

```bash
jupyter notebook
```

or

```bash
jupyterhub
```

`ipynb` 파일 중 하나를 열고 작업을 시작할 수 있습니다.

### 컨테이너에서 실행하기

파이썬 설치 대안으로, 코드를 컨테이너에서 실행할 수 있습니다. 우리 저장소에는 이 저장소를 위한 컨테이너를 구축하는 방법을 지시한 `.devcontainer` 폴더가 포함되어 있으므로, VS Code는 컨테이너에서 코드를 다시 열라고 제안할 것입니다. 이를 위해 Docker 설치가 필요하며 좀 더 복잡하므로, 경험이 많은 사용자들에게 추천합니다.

GitHub Codespaces를 사용할 때 API 카를 안전하게 유지하는 가장 좋은 방법 중 하나는 Codespaces Secrets를 사용하는 겁니다. [codespaces를 위한 secrets 관리](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst)에 대한 이 안내서를 따라주세요.

## 강좌 및 기술 요구 사항

이 강좌는 6개의 개념 강좌와 6개의 코딩 강좌로 구성되어 있습니다.

코딩 강좌에서 Azure OpenAI 서비스를 사용합니다. 이 코드를 실행하기 위해 Azure OpenAI 서비스에 대한 접근 권한과 API 키가 필요합니다. [이 신청서를 작성하여](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) 접근 권한을 신청할 수 있습니다.

신청서 처리를 기다리는 동안 각 코딩 강좌에는 코드와 출력을 볼 수 있는 ₩README.md` 파일도 포함되어 있습니다.

## Azure OpenAI 서비스를 처음 사용하는 경우

Azure OpenAI 서비스를 처음 사용하는 경우, [Azure OpenAI 서비스 리소스를 만들고 배포하는 방법](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)에 대한 가이드를 따라야 합니다.

## 다른 학습자들 만나기

다른 학습자들을 만날 수 있도록 [AI 커뮤티니 디스코드 서버](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)에 채널을 만들었습니다. 이는 생성형 AI에서 성장하고자 하는 다른 창업자, 개발자, 학생들과 네트워크를 형성하는 좋은 방법입니다.

[![Join discord channel](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

프로젝트 팀도 이 디스코드 서버에 있어서 학습자들을 도울 것입니다.

## 기여하기

이 강좌는 오픈 소스 이니셔티브입니다. 개선의 여지나 문제를 발견한다면, [풀 리퀘스트(Pull Request)](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)를 생성하거나 [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)로 문제를 기록해주세요.

프로젝트 팀은 모든 기여를 추적할 것이며, 오픈소스에 기여하는 것은 생성형 AI 분야에서 경력을 쌓을 수 있는 훌륭한 방법입니다.

대부분의 기여는 여러분이 기여자 라이센스 계약(CLA)에 동의해야 합니다. 이 계약은 여러분이 우리에게 여러분의 기여를 사용할 권리를 부여할 권리가 있으며 실제로 그렇게 할 수 있음을 선언하는 것입니다. 자세한 내용은 [CLA, 기여자 라이센스 계약 웹사이트](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)를 방문하세요.

중요: 이 리포지토리의 텍스트를 번역할 때, 기계 번역을 사용하지 말아 주세요. 번역은 커뮤니티를 통해 검증할 예정이므로, 유창하게 구사할 수 있는 언어에서만 번역을 자원해 주세요.

풀 리퀘스트를 제출하면, CLA-봇이 자동으로 CLA 제공이 필요한지 여부를 결정하고 PR을 적절하게 꾸며줍니다(예: 라벨, 코멘트). 봇이 제공하는 지침을 따르기만 하면 됩니다. CLA를 사용하는 모든 저장소에 대해 이 작업을 한 번만 수행하면 됩니다.

이 프로젝트는 [마이크로소프트 오픈 소스 행동 강령](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)을 채택하였습니다. 자세한 정보는 행동 강령 FAQ를 읽어주시고 추가 질문이나 의견이 있을 경우 [Email opencode](opencode@microsoft.com) 로 연락해주세요.

## 자 그럼, 시작해봅시다

이제 이 강좌를 완료하기 위해 필요한 단계들을 모두 마쳤으니, [생성형 AI 및 대규모 언어 모델(LLMs) 소개](../../../01-introduction-to-genai/translations/ko-kr/README.md?WT.mc_id=academic-105485-koreyst)로 시작합니다.