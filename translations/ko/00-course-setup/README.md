<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-05-19T08:56:52+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ko"
}
-->
# 이 과정 시작하기

이 과정을 시작하고 생성적 AI로 무엇을 만들어낼지 기대됩니다!

성공적인 학습을 위해 이 페이지에서는 설정 단계, 기술 요구 사항, 그리고 필요 시 도움을 받을 수 있는 곳을 안내합니다.

## 설정 단계

이 과정을 시작하려면 다음 단계를 완료해야 합니다.

### 1. 이 저장소 포크하기

[이 전체 저장소를 포크](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)하여 자신의 GitHub 계정에 복사하면 코드를 변경하고 도전을 완료할 수 있습니다. 또한 [이 저장소를 별표(🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)하여 쉽게 찾을 수 있습니다.

### 2. 코드스페이스 만들기

코드를 실행할 때 발생할 수 있는 종속성 문제를 피하기 위해 [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)에서 이 과정을 실행하는 것을 권장합니다.

포크한 저장소에서 `Code` 옵션을 선택하고 **Codespaces** 옵션을 선택하여 생성할 수 있습니다.

![코드스페이스를 생성하는 버튼이 있는 대화 상자](../../../00-course-setup/images/who-will-pay.webp)

### 3. API 키 저장하기

어떤 유형의 애플리케이션을 만들 때 API 키를 안전하게 보호하는 것이 중요합니다. 코드에 API 키를 직접 저장하지 않는 것이 좋습니다. 이러한 정보를 공개 저장소에 커밋하면 보안 문제를 일으킬 수 있으며 악의적인 사용자가 사용하면 원치 않는 비용이 발생할 수 있습니다. Python을 위한 `.env` 파일을 만들고 `GITHUB_TOKEN`를 추가하는 단계별 가이드는 다음과 같습니다:

1. **프로젝트 디렉토리로 이동**: 터미널이나 명령 프롬프트를 열고 `.env` 파일을 만들고자 하는 프로젝트의 루트 디렉토리로 이동합니다.

   ```bash
   cd path/to/your/project
   ```

2. **`.env` 파일 생성**: 선호하는 텍스트 편집기를 사용하여 `.env`라는 새 파일을 만듭니다. 명령줄을 사용하는 경우 `touch` (on Unix-based systems) or `echo`를 사용할 수 있습니다 (Windows의 경우):

   유닉스 기반 시스템:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **`.env` 파일 편집**: 텍스트 편집기(e.g., VS Code, Notepad++ 또는 기타 편집기)에서 `.env` 파일을 열고, `your_github_token_here`를 실제 GitHub 토큰으로 교체하여 다음 줄을 파일에 추가합니다:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **파일 저장**: 변경 사항을 저장하고 텍스트 편집기를 닫습니다.

5. **`python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` 패키지 설치**: `.env` 파일에서 환경 변수를 Python 애플리케이션으로 로드하기 위해 `pip`을 사용하여 설치할 수 있습니다:

   ```bash
   pip install python-dotenv
   ```

6. **Python 스크립트에서 환경 변수 로드**: Python 스크립트에서 `python-dotenv` 패키지를 사용하여 `.env` 파일에서 환경 변수를 로드합니다:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

이제 완료되었습니다! `.env` 파일을 생성하고, GitHub 토큰을 추가하고, Python 애플리케이션에 로드했습니다.

## 로컬 컴퓨터에서 실행하기

코드를 로컬 컴퓨터에서 실행하려면 [Python의 일부 버전](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)이 설치되어 있어야 합니다.

그런 다음 저장소를 사용하려면 클론해야 합니다:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

모든 것이 체크아웃되면 시작할 수 있습니다!

## 선택적 단계

### Miniconda 설치

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst)는 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python 및 몇 가지 패키지를 설치하는 경량 설치 프로그램입니다. Conda 자체는 패키지 관리자이며, 다양한 Python [**가상 환경**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)과 패키지를 쉽게 설정하고 전환할 수 있도록 합니다. 또한 `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`을 통해 사용할 수 없는 패키지를 설치하는 데 유용합니다.

아래 스니펫을 사용하여 환경 파일을 채우세요:

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

conda를 사용하여 오류가 발생하면 터미널에서 다음 명령을 사용하여 Microsoft AI 라이브러리를 수동으로 설치할 수 있습니다.

```
conda install -c microsoft azure-ai-ml
```

환경 파일은 필요한 종속성을 지정합니다. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3`은 Python의 최신 주요 버전입니다.

이제 명령줄/터미널에서 아래 명령을 실행하여 Conda 환경을 생성할 수 있습니다.

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

문제가 발생하면 [Conda 환경 가이드](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)를 참조하세요.

### Python 지원 확장과 함께 Visual Studio Code 사용

이 과정을 위해 [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) 편집기와 [Python 지원 확장](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)을 사용하는 것을 권장합니다. 그러나 이것은 권장 사항일 뿐 필수 사항은 아닙니다.

> **참고**: VS Code에서 코스 저장소를 열면 프로젝트를 컨테이너 내에서 설정할 수 있는 옵션이 제공됩니다. 이는 코스 저장소 내에 있는 [특수 `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 디렉토리 때문입니다. 이에 대한 자세한 내용은 나중에 설명합니다.

> **참고**: 디렉토리를 클론하고 VS Code에서 열면 Python 지원 확장을 설치하라는 메시지가 자동으로 표시됩니다.

> **참고**: VS Code에서 저장소를 컨테이너에서 다시 열라는 제안을 받을 경우, 로컬에 설치된 Python 버전을 사용하기 위해 이 요청을 거부하세요.

### 브라우저에서 Jupyter 사용

[Jupyter 환경](https://jupyter.org?WT.mc_id=academic-105485-koreyst)에서 브라우저를 통해 프로젝트를 작업할 수도 있습니다. 클래식 Jupyter와 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst)는 자동 완성, 코드 하이라이팅 등과 같은 기능을 갖춘 쾌적한 개발 환경을 제공합니다.

로컬에서 Jupyter를 시작하려면 터미널/명령줄로 이동하여 코스 디렉토리로 이동한 후 다음을 실행하세요:

```bash
jupyter notebook
```

또는

```bash
jupyterhub
```

이렇게 하면 Jupyter 인스턴스가 시작되고, 접근할 URL이 명령줄 창에 표시됩니다.

URL에 접근하면 코스 개요를 볼 수 있고, `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` 파일로 이동하여 코드와 출력을 볼 수 있습니다.

## 처음으로 Azure OpenAI 서비스 사용하기

Azure OpenAI 서비스를 처음 사용하는 경우, [Azure OpenAI 서비스 리소스를 생성하고 배포하는 방법](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)을 안내하는 가이드를 따라주세요.

## 처음으로 OpenAI API 사용하기

OpenAI API를 처음 사용하는 경우, [인터페이스를 생성하고 사용하는 방법](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)을 안내하는 가이드를 따라주세요.

## 다른 학습자 만나기

다른 학습자들과 만날 수 있도록 공식 [AI 커뮤니티 Discord 서버](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)에 채널을 만들었습니다. 이는 비슷한 생각을 가진 기업가, 개발자, 학생, 생성적 AI를 통해 성장하고자 하는 사람들과 네트워크를 형성할 수 있는 좋은 방법입니다.

[![디스코드 채널 가입하기](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

프로젝트 팀도 이 Discord 서버에서 학습자들을 도울 것입니다.

## 기여하기

이 과정은 오픈 소스 이니셔티브입니다. 개선할 부분이나 문제가 있으면 [Pull Request 생성](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)하거나 [GitHub 이슈 기록](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)을 해주세요.

프로젝트 팀은 모든 기여를 추적할 것입니다. 오픈 소스에 기여하는 것은 생성적 AI 분야에서 경력을 쌓는 놀라운 방법입니다.

대부분의 기여는 기여자 라이선스 계약(Contributor License Agreement, CLA)에 동의해야 하며, 귀하가 실제로 권리를 가지고 있으며, 귀하의 기여를 사용할 수 있는 권리를 우리에게 부여한다는 것을 선언해야 합니다. 자세한 내용은 [CLA, Contributor License Agreement 웹사이트](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)를 방문하세요.

중요: 이 저장소의 텍스트를 번역할 때 기계 번역을 사용하지 않도록 하세요. 우리는 커뮤니티를 통해 번역을 검증할 것이므로, 능숙한 언어에만 번역을 자원해 주세요.

Pull Request를 제출하면 CLA-bot이 자동으로 CLA 제공 여부를 결정하고 PR을 적절하게 꾸밀 것입니다 (예: 레이블, 댓글). 봇이 제공하는 지침을 따르기만 하면 됩니다. 모든 저장소에서 CLA를 사용하는 경우 한 번만 하면 됩니다.

이 프로젝트는 [Microsoft 오픈 소스 행동 강령](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)을 채택했습니다. 자세한 정보는 행동 강령 FAQ를 읽거나 [이메일 opencode](opencode@microsoft.com)로 추가 질문이나 의견을 보내주세요.

## 시작합시다

이 과정을 완료하기 위한 필요한 단계를 완료했으니, [생성적 AI 및 LLM에 대한 소개](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)를 시작해 봅시다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 우리는 정확성을 위해 노력하지만, 자동 번역에는 오류나 부정확성이 있을 수 있음을 유의하시기 바랍니다. 원본 문서는 해당 언어로 작성된 문서를 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.