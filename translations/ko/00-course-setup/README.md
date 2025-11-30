<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-18T00:02:16+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ko"
}
-->
# 이 과정 시작하기

이 과정을 시작하고 생성형 AI로 무엇을 만들게 될지 기대됩니다!

성공적인 학습을 위해, 이 페이지에서는 설정 단계, 기술 요구 사항, 그리고 필요할 때 도움을 받을 수 있는 방법을 안내합니다.

## 설정 단계

이 과정을 시작하려면 다음 단계를 완료해야 합니다.

### 1. 이 저장소 포크하기

[이 전체 저장소를 포크하세요](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst). 이를 통해 코드를 변경하고 챌린지를 완료할 수 있습니다. 또한 [이 저장소를 스타(🌟)로 표시](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)하여 관련 저장소를 더 쉽게 찾을 수 있습니다.

### 2. Codespace 생성하기

코드를 실행할 때 발생할 수 있는 종속성 문제를 피하기 위해, 이 과정을 [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)에서 실행하는 것을 권장합니다.

포크한 저장소에서: **Code -> Codespaces -> New on main**

![Codespace 생성 버튼을 보여주는 대화 상자](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 비밀 추가하기

1. ⚙️ 기어 아이콘 -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. 이름을 OPENAI_API_KEY로 설정하고, 키를 붙여넣고 저장하세요.

### 3. 다음 단계는?

| 내가 하고 싶은 것       | 이동할 곳                                                              |
|---------------------|-------------------------------------------------------------------------|
| 1강 시작하기         | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| 오프라인으로 작업하기   | [`setup-local.md`](02-setup-local.md)                                   |
| LLM 제공자 설정하기    | [`providers.md`](03-providers.md)                                        |
| 다른 학습자 만나기     | [Discord에 참여하기](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 문제 해결

| 증상                                     | 해결 방법                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| 컨테이너 빌드가 10분 이상 걸림            | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | 터미널이 연결되지 않음; **+** ➜ *bash* 클릭                     |
| OpenAI에서 `401 Unauthorized` 오류 발생   | 잘못된 / 만료된 `OPENAI_API_KEY`                                |
| VS Code에서 “Dev container mounting…” 표시 | 브라우저 탭 새로고침—Codespaces가 가끔 연결을 잃음              |
| Notebook 커널 누락                        | Notebook 메뉴 ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix 기반 시스템:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` 파일 편집하기**: `.env` 파일을 텍스트 편집기(e.g., VS Code, Notepad++)에서 열고, 아래 줄을 추가하세요. `your_github_token_here`를 실제 GitHub 토큰으로 바꾸세요:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **파일 저장하기**: 변경 사항을 저장하고 텍스트 편집기를 닫으세요.

5. **`python-dotenv` 설치하기**: 아직 설치하지 않았다면, `.env` 파일에서 환경 변수를 Python 애플리케이션으로 로드하기 위해 `python-dotenv` 패키지를 설치해야 합니다. `pip`을 사용하여 설치할 수 있습니다:

   ```bash
   pip install python-dotenv
   ```

6. **Python 스크립트에서 환경 변수 로드하기**: Python 스크립트에서 `python-dotenv` 패키지를 사용하여 `.env` 파일에서 환경 변수를 로드하세요:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

이제 완료되었습니다! `.env` 파일을 성공적으로 생성하고 GitHub 토큰을 추가했으며 이를 Python 애플리케이션에 로드했습니다.

## 컴퓨터에서 로컬로 실행하기

코드를 로컬 컴퓨터에서 실행하려면 [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)의 일부 버전을 설치해야 합니다.

그런 다음 저장소를 사용하려면 클론해야 합니다:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

모든 것을 체크아웃한 후 시작할 수 있습니다!

## 선택적 단계

### Miniconda 설치하기

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst)는 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, 그리고 몇 가지 패키지를 설치하기 위한 경량 설치 프로그램입니다. Conda는 패키지 관리자로, 다양한 Python [**가상 환경**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)과 패키지를 쉽게 설정하고 전환할 수 있게 해줍니다. 또한 `pip`으로 설치할 수 없는 패키지를 설치할 때 유용합니다.

[MiniConda 설치 가이드](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst)를 따라 설치하세요.

Miniconda를 설치한 후, [저장소](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)를 클론하세요(아직 클론하지 않았다면).

다음으로 가상 환경을 생성해야 합니다. Conda를 사용하여 새 환경 파일(_environment.yml_)을 생성하세요. Codespaces를 사용하는 경우, `.devcontainer` 디렉토리 내에 생성하여 `.devcontainer/environment.yml`로 저장하세요.

환경 파일을 아래 코드 스니펫으로 채우세요:

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

Conda를 사용하는 동안 오류가 발생하면 터미널에서 아래 명령어를 사용하여 Microsoft AI 라이브러리를 수동으로 설치할 수 있습니다.

```
conda install -c microsoft azure-ai-ml
```

환경 파일은 필요한 종속성을 지정합니다. `<environment-name>`은 Conda 환경에 사용할 이름을 나타내며, `<python-version>`은 사용할 Python 버전을 나타냅니다. 예를 들어, `3`은 Python의 최신 주요 버전입니다.

이제 아래 명령어를 실행하여 Conda 환경을 생성하세요:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

문제가 발생하면 [Conda 환경 가이드](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)를 참조하세요.

### Python 지원 확장 기능이 포함된 Visual Studio Code 사용하기

이 과정에서는 [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) 편집기와 [Python 지원 확장 기능](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)을 사용하는 것을 추천합니다. 하지만 이는 권장 사항일 뿐 필수는 아닙니다.

> **참고**: VS Code에서 과정 저장소를 열면 컨테이너 내에서 프로젝트를 설정할 옵션이 제공됩니다. 이는 과정 저장소 내에 있는 [특별한 `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 디렉토리 때문입니다. 이에 대한 자세한 내용은 나중에 다룹니다.

> **참고**: 저장소를 클론하고 VS Code에서 디렉토리를 열면 Python 지원 확장 기능 설치를 자동으로 제안합니다.

> **참고**: VS Code가 저장소를 컨테이너에서 다시 열 것을 제안하면, 로컬에 설치된 Python 버전을 사용하기 위해 이를 거부하세요.

### 브라우저에서 Jupyter 사용하기

[Jupyter 환경](https://jupyter.org?WT.mc_id=academic-105485-koreyst)을 브라우저에서 바로 사용하여 프로젝트를 진행할 수도 있습니다. 클래식 Jupyter와 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst)는 자동 완성, 코드 하이라이트 등과 같은 쾌적한 개발 환경을 제공합니다.

Jupyter를 로컬에서 시작하려면 터미널/명령줄로 이동하여 과정 디렉토리로 이동한 후 다음 명령어를 실행하세요:

```bash
jupyter notebook
```

또는

```bash
jupyterhub
```

이 명령어는 Jupyter 인스턴스를 시작하며, 액세스할 수 있는 URL이 명령줄 창에 표시됩니다.

URL에 액세스하면 과정 개요를 확인할 수 있으며, `*.ipynb` 파일로 이동할 수 있습니다. 예를 들어, `08-building-search-applications/python/oai-solution.ipynb`.

### 컨테이너에서 실행하기

컴퓨터나 Codespace에서 모든 것을 설정하는 대신 [컨테이너](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)를 사용할 수도 있습니다. 과정 저장소 내의 특별한 `.devcontainer` 폴더를 통해 VS Code에서 프로젝트를 컨테이너 내에 설정할 수 있습니다. Codespaces 외부에서는 Docker 설치가 필요하며, 약간의 추가 작업이 필요하므로 컨테이너 작업 경험이 있는 경우에만 추천합니다.

GitHub Codespaces를 사용할 때 API 키를 안전하게 유지하는 가장 좋은 방법 중 하나는 Codespace Secrets를 사용하는 것입니다. [Codespaces 비밀 관리](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) 가이드를 따라 자세히 알아보세요.

## 강의 및 기술 요구 사항

이 과정은 6개의 개념 강의와 6개의 코딩 강의로 구성되어 있습니다.

코딩 강의에서는 Azure OpenAI 서비스를 사용합니다. 이 코드를 실행하려면 Azure OpenAI 서비스와 API 키에 대한 액세스 권한이 필요합니다. [이 신청서](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)를 작성하여 액세스를 신청할 수 있습니다.

신청서가 처리되는 동안, 각 코딩 강의에는 코드와 결과를 볼 수 있는 `README.md` 파일이 포함되어 있습니다.

## Azure OpenAI 서비스 처음 사용하기

Azure OpenAI 서비스를 처음 사용하는 경우, [Azure OpenAI 서비스 리소스를 생성하고 배포하는 방법](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)에 대한 가이드를 따라주세요.

## OpenAI API 처음 사용하기

OpenAI API를 처음 사용하는 경우, [인터페이스 생성 및 사용 방법](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)에 대한 가이드를 따라주세요.

## 다른 학습자 만나기

공식 [AI 커뮤니티 Discord 서버](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)에 다른 학습자들을 만날 수 있는 채널을 만들었습니다. 이는 생성형 AI에서 실력을 키우고자 하는 다른 창업가, 개발자, 학생들과 네트워크를 형성할 수 있는 훌륭한 방법입니다.

[![Discord 채널 참여하기](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

프로젝트 팀도 이 Discord 서버에 있어 학습자들을 도울 것입니다.

## 기여하기

이 과정은 오픈 소스 프로젝트입니다. 개선이 필요한 부분이나 문제가 보이면 [Pull Request 생성](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)하거나 [GitHub 이슈 등록](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)하세요.

프로젝트 팀은 모든 기여를 추적할 것입니다. 오픈 소스에 기여하는 것은 생성형 AI에서 경력을 쌓는 놀라운 방법입니다.

대부분의 기여는 Contributor License Agreement (CLA)에 동의해야 하며, 이를 통해 기여할 권리가 있고 실제로 기여를 사용할 권리를 부여한다는 것을 선언해야 합니다. 자세한 내용은 [CLA, Contributor License Agreement 웹사이트](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)를 방문하세요.

중요: 이 저장소의 텍스트를 번역할 때 기계 번역을 사용하지 않도록 하세요. 커뮤니티를 통해 번역을 검증할 것이므로, 능숙한 언어로만 번역을 자원하세요.

Pull Request를 제출하면 CLA-bot이 자동으로 CLA 제공 여부를 결정하고 PR에 적절히 표시(예: 라벨, 댓글)합니다. 봇이 제공하는 지침을 따르세요. 모든 저장소에서 CLA를 사용하는 경우 한 번만 이를 수행하면 됩니다.

이 프로젝트는 [Microsoft 오픈 소스 행동 강령](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)을 채택했습니다. 자세한 내용은 행동 강령 FAQ를 읽거나 [Email opencode](opencode@microsoft.com)로 추가 질문이나 의견을 보내주세요.

## 시작해봅시다!
이제 이 과정을 완료하기 위한 필요한 단계를 마쳤으니, [생성형 AI와 LLM에 대한 소개](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)를 통해 시작해 봅시다.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어를 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.