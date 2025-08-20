<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T07:04:20+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ko"
}
-->
# 이 과정 시작하기

이 과정을 시작하게 되어 매우 기쁩니다. 생성 AI로 무엇을 만들고 영감을 받을지 기대해 주세요!

성공적인 학습을 위해 이 페이지에서는 설정 단계, 기술 요구 사항, 그리고 필요할 때 도움을 받을 수 있는 곳을 안내합니다.

## 설정 단계

이 과정을 시작하려면 다음 단계를 완료해야 합니다.

### 1. 이 저장소를 포크하기

이 저장소 전체를 [자신의 GitHub 계정으로 포크](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)하여 코드를 변경하고 과제를 완료할 수 있도록 하세요. 또한 이 저장소와 관련 저장소를 더 쉽게 찾기 위해 [별표(🌟)를 추가](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)할 수도 있습니다.

### 2. Codespace 생성하기

코드를 실행할 때 의존성 문제를 피하기 위해, 이 과정을 [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)에서 실행하는 것을 권장합니다.

포크한 저장소에서 `Code` 옵션을 선택한 후 **Codespaces** 옵션을 선택하면 생성할 수 있습니다.

![Codespace 생성 버튼을 보여주는 대화상자](../../../00-course-setup/images/who-will-pay.webp)

### 3. API 키 저장하기

어떤 애플리케이션을 만들 때든 API 키를 안전하게 보관하는 것이 중요합니다. API 키를 코드에 직접 저장하지 않는 것을 권장합니다. 공개 저장소에 키를 커밋하면 보안 문제가 발생할 수 있고, 악의적인 사용자가 사용하면 원치 않는 비용이 발생할 수 있습니다.  
다음은 Python용 `.env` 파일을 만들고 `GITHUB_TOKEN`을 추가하는 단계별 가이드입니다:

1. **프로젝트 디렉터리로 이동하기**: 터미널이나 명령 프롬프트를 열고 `.env` 파일을 만들고자 하는 프로젝트 루트 디렉터리로 이동하세요.

   ```bash
   cd path/to/your/project
   ```

2. **`.env` 파일 만들기**: 선호하는 텍스트 편집기로 `.env`라는 새 파일을 만드세요. 명령줄을 사용할 경우 Unix 기반 시스템에서는 `touch`, Windows에서는 `echo`를 사용할 수 있습니다:

   Unix 기반 시스템:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` 파일 편집하기**: 텍스트 편집기(예: VS Code, Notepad++ 등)로 `.env` 파일을 열고, `your_github_token_here`를 실제 GitHub 토큰으로 바꿔 아래 내용을 추가하세요:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **파일 저장하기**: 변경 사항을 저장하고 편집기를 닫으세요.

5. **`python-dotenv` 설치하기**: 아직 설치하지 않았다면, `.env` 파일에서 환경 변수를 불러오기 위해 `python-dotenv` 패키지를 설치해야 합니다. `pip`로 설치할 수 있습니다:

   ```bash
   pip install python-dotenv
   ```

6. **Python 스크립트에서 환경 변수 불러오기**: Python 스크립트에서 `python-dotenv` 패키지를 사용해 `.env` 파일의 환경 변수를 불러오세요:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

이제 `.env` 파일을 만들고 GitHub 토큰을 추가했으며, Python 애플리케이션에서 불러오는 작업을 성공적으로 완료했습니다.

## 컴퓨터에서 로컬로 실행하는 방법

코드를 로컬에서 실행하려면 [Python이 설치되어 있어야 합니다](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

그 다음 저장소를 클론해야 합니다:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

모든 준비가 완료되면 바로 시작할 수 있습니다!

## 선택적 단계

### Miniconda 설치하기

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst)는 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python 및 몇 가지 패키지를 설치할 수 있는 경량 설치 프로그램입니다.  
Conda는 패키지 관리자이며, 다양한 Python [**가상 환경**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)과 패키지를 쉽게 설정하고 전환할 수 있게 해줍니다. 또한 `pip`로 설치할 수 없는 패키지를 설치할 때도 유용합니다.

[MiniConda 설치 가이드](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst)를 참고해 설치하세요.

Miniconda를 설치한 후, 아직 클론하지 않았다면 [저장소](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)를 클론하세요.

다음으로 가상 환경을 만들어야 합니다. Conda를 사용할 경우 새 환경 파일(_environment.yml_)을 만드세요. Codespaces를 사용 중이라면 `.devcontainer` 디렉터리 내에 `.devcontainer/environment.yml`로 만드시면 됩니다.

아래 스니펫으로 환경 파일을 채우세요:

```yml
name: <environment-name>
channels:
  - defaults
  - microsoft
dependencies:
  - python=<python-version>
  - openai
  - python-dotenv
  - pip
  - pip:
      - azure-ai-ml
```

conda 사용 중 오류가 발생하면 터미널에서 다음 명령어로 Microsoft AI 라이브러리를 수동으로 설치할 수 있습니다.

```
conda install -c microsoft azure-ai-ml
```

환경 파일에는 필요한 의존성이 명시되어 있습니다. `<environment-name>`은 Conda 환경 이름, `<python-version>`은 사용하려는 Python 버전입니다. 예를 들어 `3`은 최신 메이저 버전입니다.

준비가 되면 아래 명령어를 터미널에서 실행해 Conda 환경을 만드세요.

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

문제가 생기면 [Conda 환경 가이드](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)를 참고하세요.

### Python 지원 확장 기능과 함께 Visual Studio Code 사용하기

이 과정에서는 [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) 편집기와 [Python 지원 확장 기능](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 사용을 권장합니다. 다만 필수는 아닙니다.

> **참고**: VS Code에서 과정 저장소를 열면 프로젝트를 컨테이너 내에서 설정할 수 있는 옵션이 있습니다. 이는 과정 저장소 내에 있는 [특별한 `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 디렉터리 덕분입니다. 자세한 내용은 이후에 다룹니다.

> **참고**: 저장소를 클론하고 VS Code에서 열면 Python 지원 확장 기능 설치를 자동으로 제안합니다.

> **참고**: VS Code가 저장소를 컨테이너에서 다시 열도록 제안하면, 로컬에 설치된 Python을 사용하려면 이 요청을 거절하세요.

### 브라우저에서 Jupyter 사용하기

브라우저 내에서 [Jupyter 환경](https://jupyter.org?WT.mc_id=academic-105485-koreyst)을 사용해 프로젝트 작업도 가능합니다. 클래식 Jupyter와 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) 모두 자동 완성, 코드 하이라이트 등 쾌적한 개발 환경을 제공합니다.

로컬에서 Jupyter를 시작하려면 터미널/명령줄에서 과정 디렉터리로 이동한 후 다음을 실행하세요:

```bash
jupyter notebook
```

또는

```bash
jupyterhub
```

이렇게 하면 Jupyter 인스턴스가 시작되고, 접속할 수 있는 URL이 명령줄 창에 표시됩니다.

URL에 접속하면 과정 개요를 볼 수 있고, `*.ipynb` 파일을 탐색할 수 있습니다. 예를 들어 `08-building-search-applications/python/oai-solution.ipynb` 같은 파일입니다.

### 컨테이너에서 실행하기

컴퓨터나 Codespace에 모든 것을 설정하는 대신 [컨테이너](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)를 사용할 수도 있습니다. 과정 저장소 내 특별한 `.devcontainer` 폴더 덕분에 VS Code가 컨테이너 내에서 프로젝트를 설정할 수 있습니다. Codespaces 외부에서는 Docker 설치가 필요하며, 다소 복잡할 수 있으니 컨테이너 작업 경험이 있는 분께만 권장합니다.

GitHub Codespaces에서 API 키를 안전하게 관리하는 가장 좋은 방법 중 하나는 Codespace Secrets를 사용하는 것입니다. 자세한 내용은 [Codespaces 비밀 관리](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) 가이드를 참고하세요.

## 수업 및 기술 요구 사항

이 과정은 6개의 개념 수업과 6개의 코딩 수업으로 구성되어 있습니다.

코딩 수업에서는 Azure OpenAI Service를 사용합니다. 코드를 실행하려면 Azure OpenAI 서비스 접근 권한과 API 키가 필요합니다. [이 신청서를 작성](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)하여 접근 권한을 요청할 수 있습니다.

신청 처리 대기 중에도 각 코딩 수업에는 코드와 출력 결과를 볼 수 있는 `README.md` 파일이 포함되어 있습니다.

## Azure OpenAI Service를 처음 사용하는 경우

Azure OpenAI 서비스를 처음 사용한다면, [Azure OpenAI Service 리소스 생성 및 배포 방법](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) 가이드를 따라 주세요.

## OpenAI API를 처음 사용하는 경우

OpenAI API를 처음 사용한다면, [인터페이스 생성 및 사용 방법](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) 가이드를 참고하세요.

## 다른 학습자 만나기

공식 [AI 커뮤니티 Discord 서버](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)에 다른 학습자들과 만날 수 있는 채널을 만들었습니다. 이는 같은 관심사를 가진 창업자, 개발자, 학생 등과 네트워킹하고 생성 AI 실력을 키우기에 좋은 기회입니다.

[![Discord 채널 참여하기](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

프로젝트 팀도 이 Discord 서버에서 학습자들을 지원할 예정입니다.

## 기여하기

이 과정은 오픈 소스 프로젝트입니다. 개선할 점이나 문제를 발견하면 [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)를 생성하거나 [GitHub 이슈](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)를 남겨 주세요.

프로젝트 팀은 모든 기여를 추적합니다. 오픈 소스에 기여하는 것은 생성 AI 분야에서 경력을 쌓는 훌륭한 방법입니다.

대부분의 기여는 기여자가 해당 기여에 대한 권리를 보유하고 있으며, 실제로 우리에게 사용 권한을 부여한다는 내용을 선언하는 기여자 라이선스 계약(CLA)에 동의해야 합니다. 자세한 내용은 [CLA, Contributor License Agreement 웹사이트](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)를 참고하세요.

중요: 이 저장소 내 텍스트를 번역할 때는 기계 번역을 사용하지 마세요. 커뮤니티를 통해 번역을 검증할 예정이므로, 능숙한 언어에만 자원봉사로 참여해 주세요.

풀 리퀘스트를 제출하면 CLA-bot이 자동으로 CLA 제출 필요 여부를 판단하고 PR에 적절한 라벨이나 코멘트를 추가합니다. 봇의 안내에 따라 진행하면 되며, 모든 저장소에서 한 번만 진행하면 됩니다.

이 프로젝트는 [Microsoft 오픈 소스 행동 강령](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)을 채택했습니다. 자세한 내용은 행동 강령 FAQ를 읽거나 추가 질문이나 의견이 있으면 [Email opencode](opencode@microsoft.com)로 문의하세요.

## 시작해 봅시다

이제 이 과정을 완료하는 데 필요한 단계를 마쳤으니, [생성 AI와 LLM 소개](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)부터 시작해 봅시다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.