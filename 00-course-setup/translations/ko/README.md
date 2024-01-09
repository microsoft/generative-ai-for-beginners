# 코스 시작하기

이 코스를 시작하시게 되어 정말 기쁩니다. 여러분이 Generative AI와 함께 무엇을 영감받아 만들어낼지 기대됩니다!

여러분들의 시간을 성공적으로 보내기 위해, 코스 환경 설정, 기술적 요구사항, 도움이 필요한 경우 어떻게 도움을 받을 수 있는지 안내하는 페이지를 만들었습니다.

## 코스 환경 설정하기

이 과정을 시작하려면 다음 단계를 완료해야 합니다.


### 1. 레포지토리 포크하기

[레포지토리를 포크](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) 하여 자신의 Github 계정에 업로드하여 코드를 변경하고 과제를 완료할 수 있습니다. 또한 [레포지토리에 스타 (🌟)를 추가](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) 하여 쉽게 찾아볼 수 있도록 할 수 있습니다.

### 2. Codespace 만들기

코드를 실행하는 동안 의존성 문제를 피하기 위해 Github codepsace를 활용하여 코스를 진행하는 것을 추천합니다.

이를 위해 포크한 레포지토리에서 `Code` 옵션을 선택하고 **Codespaces** 옵션을 선택하여 생성할 수 있습니다.

### 3. API 키 저장하기

어떠한 종류의 어플리케이션을 개발하든지 API 키를 안전하게 보관하는 것은 중요합니다. 코드에 직접 API 키를 저장하지 않는 것을 권장하며, 이들을 public 레포지토리에 커밋하는 것은 예상치 못한 비용 및 문제를 초래할 수 있습니다.

![Dialog showing buttons to create a codespace](../../images/who-will-pay.webp?WT.mc_id=academic-105485-koreyst)

## 로컬 컴퓨터에서 실행하는 방법

컴퓨터에서 로컬로 코드를 실행하려면 [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)이 설치되어 있어야 합니다.

이후 레포지토리를 사용하려면 이를 클론해야 합니다.

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

이제 학습을 시작하고 코드와 작업을 진행할 수 있습니다.

### miniconda 설치하기 (선택)
[miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst)를 설치하면 여러  이점이 있습니다. - 이는 상대적으로 가벼운 설치로 다양한 Python **가상 환경**에 대한 `conda` 패키지 매니저를 지원합니다. `conda`는 다른 Python 버전 및 패키지 간에 쉽게 설치 및 전환할 수 있으며, `pip`를 통해 사용할 수 없는 패키지도 쉽게 설치할 수 있습니다.

miniconda를 설치한 후, 레포지토리를 clone하고, 이 코스에 사용할 가상 환경을 생성해야 합니다. 

아래 단계를 실행하기 전에 먼저 *environment.yml*이 있는지 확인하세요. *environment.yml* 파일은 필요한 의존성이 포함된 conda 환경을 만드는데 사용되며, 다음과 같이 제공될 수 있습니다.

```yml
name: <environment-name>
channels:  
 - defaults
dependencies:  
- python=<python-version>  
- openai  
- python-dotenv
```

`<environment-name>`을 여러분의 conda 환경 이름으로 바꿀 수 있으며, `<python-version>`에는 사용하고 싶은 Python 버전을 기입하면 됩니다. 생성한 *environment.yml* 파일을 레포지토리의 *.devcontainer* 폴더 안에 위치하도록 하세요.

이제 *environment.yml*을 만들었다면, 다음 명령을 사용하여 conda 환경을 생성할 수 있습니다.

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

문제가 발생하면 [conda 환경 생성](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)에 대한 링크를 참고하세요.

### 파이썬 Extension과 함께 Visual Studio Code 사용하기

Probably the best way to use the curriculum is to open it in [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) with [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst).

> **Note**: “VS Code에서 디렉토리를 클론하고 열면 자동으로 Python 확장을 설치하라는 제안이 나타납니다. 또한 위에서 설명한대로 miniconda도 설치해야 합니다.

> **Note**: VS Code가 컨테이너에서 저장소를 다시 열 것을 제안하면, 로컬 파이썬 설치를 사용하기 위해 거절해야 합니다.

### 브라우저에서 Jupyter 사용하기

브라우저에서 직접 자신의 컴퓨터에서 Jupyter 환경을 사용할 수도 있습니다. 기존 Jupyter와 Jupyter Hub 모두 자동 완성, 코드 강조 등을 제공하는 매우 편리한 개발 환경을 제공합니다.

Jupyter를 로컬에서 시작하려면, 코스의 디렉토리로 이동하고 다음을 실행하십시오:

```bash
jupyter notebook
```

또는

```bash
jupyterhub
```

그런 다음 .ipynb 파일 중 어느 것으로든 이동하여 열고 작업을 시작할 수 있습니다.

### 컨테이너에서 실행하기

Python 설치의 대안으로 컨테이너에서 코드를 실행할 수 있습니다. 저장소에는 이 저장소에 대한 컨테이너를 구축할 수 있는 특별한 `.devcontainer` 폴더가 포함되어 있기 때문에, VS Code는 코드를 컨테이너에서 다시 열 것을 제안할 것입니다. 이것은 Docker 설치를 필요로 하며, 또한 더 복잡할 수 있으므로, 우리는 이것을 더 경험 있는 사용자들에게 추천합니다.

GitHub Codespaces를 사용할 때 API 키를 안전하게 유지하는 가장 좋은 방법 중 하나는 Codespace Secrets를 사용하는 것입니다. 해당 가이드를 따라서 [코드스페이스에 대한 secrets을 관리](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst)하는 방법을 알아보세요.

## 수업과 기술 요구 사항

해당 코스에는 6개의 개념 수업와 6개의 코딩 수업이 있습니다.

코딩 수업에서는  Azure OpenAI 서비스를 사용합니다. 이 코드를 실행하려면 Azure OpenAI 서비스에 접근할 수 있어야 하고 API 키가 필요합니다. [양식](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)을 작성하여 접근 권한을 신청할 수 있습니다.

신청이 처리되기를 기다리는 동안, 각 코딩 수업에는 코드와 출력을 볼 수 있는 `README.md` 파일이 포함되어 있습니다.

## 처음으로 Azure OpenAI 서비스를 사용하기

 Azure OpenAI 서비스를 처음 사용하는 경우, [Azure OpenAI 서비스 리소스를 생성하고 배포하는 방법](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)에 대한 가이드를 따라 주세요.

## 다른 학습자들 만나기

[공식 AI 커뮤니티 디스코드 서버](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)에 다른 학습자들과 만날 수 있는 채널을 만들었습니다. 여기서 같은 마음을 가진 창업가, 빌더, 학생, 그리고 생성형 AI에서 한 단계 더 나아가고자 하는 모든 사람들과 네트워킹할 수 있습니다.

[![Join discord channel](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

프로젝트 팀도 해당 디스코드 서버에 있어서 어떤 학습자든 도와드릴 수 있습니다.

## 기여하기

해당 코스는 오픈 소스로 관리됩니다. 개선할 부분이나 문제가 있으면 [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)를 생성하거나 [Github issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)를 기록해 주세요.

프로젝트 팀은 모든 기여를 추적하고 있으며, 오픈 소스에 기여하는 것은 생성형 AI 분야에서 커리어를 구축하는 데 훌륭한 방법입니다.

대부분의 기여는 CLA(Contributor License Agreement)에 동의해야 합니다. CLA는 귀하가 귀하의 기여를 사용할 권리가 있으며 실제로 그렇게 하는 것에 동의한다고 선언하는 것입니다. 자세한 내용은 [CLA, Contributor License Agreement 웹사이트](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)를 방문하세요.

중요: 이 저장소의 텍스트를 번역할 때 기계 번역을 사용하지 마세요. 커뮤니티를 통해 번역을 검증할 것이므로, 귀하가 능숙한 언어로만 번역에 자원해 주세요.

풀 리퀘스트를 제출하면 CLA-bot이 자동으로 귀하가 CLA를 제공해야 하는지 여부를 결정하고 적절하게 PR을 꾸며줍니다(예: 레이블, 코멘트). 봇이 제공하는 지침을 따르기만 하면 됩니다. CLA를 사용하는 모든 저장소에서 한 번만 이 작업을 수행하면 됩니다.

해당 프로젝트는 Microsoft 오픈 소스 행동 강령을 따릅니다. 자세한 내용은 행동 강령 FAQ를 읽거나 추가적인 질문이나 의견이 있으면 [Email opencode](opencode@microsoft.com)으로 연락하세요.

## 시작해봅시다

해당 코스에 필요한 단계를 모두 완료했으니, [생성형 AI와 LLM 소개](../../../01-introduction-to-genai/translations/ko/README.md?WT.mc_id=academic-105485-koreyst)를 통해 시작해 보세요.