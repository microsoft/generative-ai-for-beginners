<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T15:14:52+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ko"
}
-->
# 이 과정 시작하기

이 과정을 시작하게 되어 정말 기쁩니다! 생성형 AI로 어떤 멋진 것들을 만들어낼지 기대가 됩니다.

여러분의 성공을 위해, 이 페이지에서는 준비 단계, 기술 요구 사항, 그리고 도움이 필요할 때 어디서 도움을 받을 수 있는지 안내합니다.

## 준비 단계

이 과정을 시작하려면 다음 단계를 완료해야 합니다.

### 1. 이 저장소 포크하기

[이 전체 저장소를 포크](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)하여 자신의 GitHub 계정에서 코드를 수정하고 챌린지를 완료할 수 있습니다. 또한 [이 저장소에 별(🌟) 표시](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)를 해두면 이 저장소와 관련 저장소를 더 쉽게 찾을 수 있습니다.

### 2. Codespace 만들기

코드 실행 시 의존성 문제를 피하기 위해, [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)에서 이 과정을 진행하는 것을 추천합니다.

포크한 저장소에서: **Code -> Codespaces -> New on main**

![Codespace 생성 버튼이 있는 대화상자](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 시크릿 추가하기

1. ⚙️ 톱니바퀴 아이콘 -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. 이름은 OPENAI_API_KEY로 하고, 키를 붙여넣은 후 저장하세요.

### 3. 다음 단계는?

| 하고 싶은 것         | 이동할 곳                                                                  |
|---------------------|----------------------------------------------------------------------------|
| 1강 시작하기         | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)         |
| 오프라인으로 작업하기 | [`setup-local.md`](02-setup-local.md)                                      |
| LLM 제공자 설정하기  | [`providers.md`](providers.md)                                             |
| 다른 학습자 만나기   | [Discord 참여하기](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 문제 해결

| 증상                                      | 해결 방법                                                        |
|-------------------------------------------|------------------------------------------------------------------|
| 컨테이너 빌드가 10분 이상 멈춤             | **Codespaces ➜ “Rebuild Container”**                             |
| `python: command not found`               | 터미널이 연결되지 않음; **+** 클릭 ➜ *bash*                      |
| OpenAI에서 `401 Unauthorized`             | 잘못된/만료된 `OPENAI_API_KEY`                                   |
| VS Code에 “Dev container mounting…” 표시  | 브라우저 탭 새로고침—Codespaces가 가끔 연결을 잃을 수 있음       |
| 노트북 커널이 없음                        | 노트북 메뉴 ➜ **Kernel ▸ Select Kernel ▸ Python 3**              |

   유닉스 계열 시스템:

   ```bash
   touch .env
   ```

   윈도우:

   ```cmd
   echo . > .env
   ```

3. **`.env` 파일 수정**: 텍스트 에디터(예: VS Code, Notepad++, 기타)로 `.env` 파일을 열고, 아래 줄을 추가하세요. `your_github_token_here` 부분을 실제 GitHub 토큰으로 바꿔주세요.

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **파일 저장**: 변경 사항을 저장하고 에디터를 닫으세요.

5. **`python-dotenv` 설치**: 아직 설치하지 않았다면, 환경 변수 로드를 위해 `python-dotenv` 패키지를 설치해야 합니다. `pip`로 설치할 수 있습니다.

   ```bash
   pip install python-dotenv
   ```

6. **파이썬 스크립트에서 환경 변수 불러오기**: 파이썬 스크립트에서 `python-dotenv` 패키지를 사용해 `.env` 파일의 환경 변수를 불러오세요.

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

이제 `.env` 파일을 만들고, GitHub 토큰을 추가하고, 파이썬 애플리케이션에서 불러오는 작업이 완료되었습니다!

## 내 컴퓨터에서 로컬로 실행하기

코드를 내 컴퓨터에서 실행하려면 [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)이 설치되어 있어야 합니다.

저장소를 사용하려면 먼저 클론해야 합니다:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

모든 준비가 끝나면 바로 시작할 수 있습니다!

## 선택 사항

### Miniconda 설치하기

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst)는 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, 그리고 몇 가지 패키지를 설치할 수 있는 가벼운 설치 도구입니다.
Conda는 패키지 관리자이며, 다양한 Python [**가상 환경**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)과 패키지들을 쉽게 설정하고 전환할 수 있게 해줍니다. `pip`으로 설치할 수 없는 패키지 설치에도 유용합니다.

[MiniConda 설치 가이드](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst)를 참고해 설치할 수 있습니다.

Miniconda를 설치했다면, [저장소](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)를 클론하세요(아직 하지 않았다면).

다음으로, 가상 환경을 만들어야 합니다. Conda로 하려면 새 환경 파일(_environment.yml_)을 만드세요. Codespaces를 사용 중이라면 `.devcontainer` 디렉터리 안에 `.devcontainer/environment.yml`로 만드세요.

아래 코드로 환경 파일을 채워주세요:

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

conda 사용 중 오류가 발생한다면, 아래 명령어로 Microsoft AI 라이브러리를 수동으로 설치할 수 있습니다.

```
conda install -c microsoft azure-ai-ml
```

환경 파일에는 필요한 의존성이 명시되어 있습니다. `<environment-name>`은 만들고 싶은 Conda 환경의 이름, `<python-version>`은 원하는 Python 버전입니다. 예를 들어, `3`은 최신 메이저 버전입니다.

이제 아래 명령어를 커맨드라인/터미널에 입력해 Conda 환경을 만들 수 있습니다.

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

문제가 생기면 [Conda 환경 가이드](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)를 참고하세요.

### Python 확장 기능이 포함된 Visual Studio Code 사용하기

이 과정에서는 [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) 에디터와 [Python 지원 확장 기능](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 사용을 추천합니다. 필수는 아니지만, 더 편리하게 작업할 수 있습니다.

> **Note**: VS Code에서 과정 저장소를 열면, 프로젝트를 컨테이너 안에서 설정할 수 있습니다. 이는 저장소 내에 [특별한 `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 디렉터리가 있기 때문입니다. 자세한 내용은 뒤에서 다룹니다.

> **Note**: 저장소를 클론해 VS Code에서 열면, Python 지원 확장 기능 설치를 자동으로 제안합니다.

> **Note**: VS Code가 저장소를 컨테이너에서 다시 열라고 제안하면, 로컬에 설치된 Python을 사용하려면 이 요청을 거부하세요.

### 브라우저에서 Jupyter 사용하기

[Jupyter 환경](https://jupyter.org?WT.mc_id=academic-105485-koreyst)에서 브라우저로 프로젝트를 진행할 수도 있습니다. 클래식 Jupyter와 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) 모두 자동 완성, 코드 하이라이팅 등 편리한 개발 환경을 제공합니다.

Jupyter를 로컬에서 시작하려면 터미널/명령줄에서 과정 디렉터리로 이동한 후 다음을 실행하세요:

```bash
jupyter notebook
```

또는

```bash
jupyterhub
```

이렇게 하면 Jupyter 인스턴스가 시작되고, 접속할 수 있는 URL이 명령줄에 표시됩니다.

URL에 접속하면 과정 개요가 보이고, 원하는 `*.ipynb` 파일로 이동할 수 있습니다. 예: `08-building-search-applications/python/oai-solution.ipynb`.

### 컨테이너에서 실행하기

컴퓨터나 Codespace에 직접 설정하는 대신 [컨테이너](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)를 사용할 수도 있습니다. 과정 저장소 내의 특별한 `.devcontainer` 폴더 덕분에 VS Code에서 컨테이너 안에 프로젝트를 설정할 수 있습니다. Codespaces 외에는 Docker 설치가 필요하며, 다소 복잡할 수 있으니 컨테이너 작업 경험이 있는 분께만 추천합니다.

GitHub Codespaces에서 API 키를 안전하게 관리하는 가장 좋은 방법 중 하나는 Codespace Secrets를 사용하는 것입니다. 자세한 내용은 [Codespaces 시크릿 관리 가이드](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst)를 참고하세요.

## 강의 및 기술 요구 사항

이 과정은 6개의 개념 강의와 6개의 코딩 강의로 구성되어 있습니다.

코딩 강의에서는 Azure OpenAI Service를 사용합니다. 코드를 실행하려면 Azure OpenAI 서비스 접근 권한과 API 키가 필요합니다. [이 신청서](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)를 작성해 접근 권한을 신청할 수 있습니다.

신청이 처리되는 동안, 각 코딩 강의의 `README.md` 파일에서 코드와 결과를 확인할 수 있습니다.

## Azure OpenAI Service 처음 사용하기

Azure OpenAI 서비스를 처음 사용하는 경우, [Azure OpenAI Service 리소스 생성 및 배포 방법](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) 가이드를 참고하세요.

## OpenAI API 처음 사용하기

OpenAI API를 처음 사용하는 경우, [인터페이스 생성 및 사용 방법](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) 가이드를 참고하세요.

## 다른 학습자 만나기

공식 [AI 커뮤니티 Discord 서버](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)에 다른 학습자들과 만날 수 있는 채널을 만들었습니다. 비슷한 관심사를 가진 창업가, 개발자, 학생 등과 네트워킹할 수 있는 좋은 기회입니다.

[![디스코드 채널 참여](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

프로젝트 팀도 이 Discord 서버에서 학습자들을 도울 예정입니다.

## 기여하기

이 과정은 오픈소스 프로젝트입니다. 개선할 점이나 문제가 있다면 [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)를 생성하거나 [GitHub 이슈](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)를 남겨주세요.

프로젝트 팀이 모든 기여를 추적합니다. 오픈소스에 기여하는 것은 생성형 AI 분야에서 경력을 쌓는 훌륭한 방법입니다.

대부분의 기여는 Contributor License Agreement (CLA)에 동의해야 하며, 여러분이 기여한 내용을 사용할 권리를 우리에게 부여한다는 것을 명시합니다. 자세한 내용은 [CLA, Contributor License Agreement 웹사이트](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)를 참고하세요.

중요: 이 저장소의 텍스트를 번역할 때는 기계 번역을 사용하지 마세요. 커뮤니티를 통해 번역을 검증할 예정이니, 능숙한 언어만 자원해 주세요.

Pull Request를 제출하면, CLA-bot이 자동으로 CLA 필요 여부를 판단하고 PR에 라벨이나 코멘트를 남깁니다. 안내에 따라 진행해 주세요. CLA는 한 번만 동의하면, 우리 CLA를 사용하는 모든 저장소에 적용됩니다.

이 프로젝트는 [Microsoft 오픈소스 행동 강령](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)을 따릅니다. 자세한 내용은 행동 강령 FAQ를 읽거나, 추가 질문이나 의견이 있으면 [Email opencode](opencode@microsoft.com)로 연락해 주세요.

## 이제 시작해봅시다
이제 이 과정을 완료하는 데 필요한 단계를 모두 마쳤으니, [생성형 AI와 LLM에 대한 소개](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)를 통해 시작해봅시다.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 있을 수 있습니다. 원본 문서(원어)가 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 이 번역의 사용으로 인해 발생하는 오해나 오역에 대해 당사는 책임을 지지 않습니다.