# 이 코스 시작하기

생성 AI로 무엇을 만들지 영감을 받고 이 코스를 시작하게 되어 매우 기쁩니다!

성공을 위해 이 페이지는 설정 단계, 기술 요구 사항, 그리고 필요 시 도움을 받을 수 있는 곳을 안내합니다.

## 설정 단계

이 코스를 시작하기 위해 다음 단계를 완료해야 합니다.

### 1. 이 저장소 포크하기

[이 저장소 전체를 포크](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)하여 GitHub 계정에 복사 후 코드를 변경하고 챌린지를 완료할 수 있습니다. 또한, [이 저장소에 별 (🌟) 표시](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)를 해두면 관련 저장소를 더 쉽게 찾을 수 있습니다.

### 2. 코드스페이스 만들기

코드를 실행할 때 의존성 문제를 피하기 위해, 이 코스를 [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)에서 실행하는 것을 권장합니다.

포크한 저장소에서: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/ko/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 비밀 키 추가하기

1. ⚙️ 톱니바퀴 아이콘 -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. 이름에 OPENAI_API_KEY 입력, 키를 붙여넣고 저장.

### 3. 다음 단계는?

| 하고 싶은 일          | 이동할 위치                                                                  |
|---------------------|-------------------------------------------------------------------------|
| 레슨 1 시작         | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| 오프라인에서 작업   | [`setup-local.md`](02-setup-local.md)                                   |
| LLM 제공자 설정     | [`providers.md`](03-providers.md)                                        |
| 다른 학습자 만나기 | [우리 Discord 참여하기](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 문제 해결


| 증상                                       | 해결 방법                                                       |
|-------------------------------------------|-----------------------------------------------------------------|
| 컨테이너 빌드가 10분 이상 멈춤            | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | 터미널이 붙지 않았음; **+** 클릭한 후 *bash* 선택                |
| OpenAI에서 `401 Unauthorized` 오류 발생   | 잘못되었거나 만료된 `OPENAI_API_KEY`                             |
| VS Code에 “Dev container mounting…” 표시   | 브라우저 탭 새로고침—Codespaces가 가끔 연결을 잃음               |
| 노트북 커널 없음                          | 노트북 메뉴 ➜ **Kernel ▸ Select Kernel ▸ Python 3**              |

   유닉스 기반 시스템:

   ```bash
   touch .env
   ```

   윈도우:

   ```cmd
   echo . > .env
   ```

3. **`.env` 파일 편집**: 텍스트 편집기 (예: VS Code, Notepad++ 또는 기타 편집기)에서 `.env` 파일을 열고, 다음 줄을 추가하세요. `your_github_token_here`를 실제 GitHub 토큰으로 바꾸세요:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **파일 저장**: 변경 사항을 저장하고 편집기를 닫으세요.

5. **`python-dotenv` 설치**: `.env` 파일의 환경 변수를 파이썬 애플리케이션에서 불러오기 위해 `python-dotenv` 패키지를 설치해야 합니다. `pip`로 설치할 수 있습니다:

   ```bash
   pip install python-dotenv
   ```

6. **파이썬 스크립트에서 환경 변수 불러오기**: 파이썬 스크립트에서 `python-dotenv` 패키지를 사용해 `.env` 파일의 환경 변수를 불러옵니다:

   ```python
   from dotenv import load_dotenv
   import os

   # .env 파일에서 환경 변수 로드
   load_dotenv()

   # GITHUB_TOKEN 변수에 접근
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

이제 `.env` 파일을 성공적으로 만들고 GitHub 토큰을 추가했으며 파이썬 애플리케이션에 불러왔습니다.

## 컴퓨터에서 로컬 실행하는 방법

코드를 로컬 컴퓨터에서 실행하려면 [Python이 설치되어 있어야 합니다](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

그다음 저장소를 사용하려면 다음 명령어로 클론해야 합니다:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

모든 준비가 완료되면 시작할 수 있습니다!

## 선택 사항 단계

### Miniconda 설치

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst)는 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), 파이썬, 몇 가지 패키지를 설치하는 경량 설치 프로그램입니다.
Conda는 파이썬 [가상 환경](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)과 패키지를 쉽게 설정하고 전환할 수 있게 하는 패키지 관리자입니다. 또한 `pip`로 설치할 수 없는 패키지 설치에도 유용합니다.

[MiniConda 설치 가이드](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst)를 따라 설치할 수 있습니다.

Miniconda가 설치되면 [저장소](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)를 클론해야 합니다 (아직 하지 않은 경우).

다음으로 가상 환경을 만들어야 합니다. Conda를 사용한다면 새 환경 파일(_environment.yml_)을 만드세요. Codespaces를 사용한다면 `.devcontainer` 폴더 내에 `.devcontainer/environment.yml`로 만듭니다.

환경 파일에 아래 코드를 추가하세요:

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

conda 사용 시 오류가 발생하면, 터미널에서 다음 명령어로 Microsoft AI 라이브러리를 수동 설치할 수 있습니다.

```
conda install -c microsoft azure-ai-ml
```

환경 파일은 필요한 종속성을 명시합니다. `<environment-name>`는 Conda 환경 이름, `<python-version>`은 사용할 파이썬 버전입니다. 예를 들어 `3`은 최신 메이저 버전입니다.

이제 아래 명령어로 Conda 환경을 만드세요:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer 하위 경로는 Codespace 설정에만 적용됩니다
conda activate ai4beg
```

문제가 발생하면 [Conda 환경 가이드](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)를 참고하세요.

### Visual Studio Code에서 Python 지원 확장 사용하기

이 코스는 [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst)와 [Python 지원 확장](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)을 사용하는 것을 권장합니다. 이는 권장 사항이지 반드시 필수는 아닙니다.

> **참고**: VS Code에서 이 저장소를 열면 프로젝트를 컨테이너 안에 설정할 수 있습니다. 이유는 코스 저장소 내 [특별한 `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 디렉토리가 있기 때문입니다. 자세한 내용은 나중에 다룹니다.

> **참고**: 저장소를 클론하여 VS Code에서 열면 Python 지원 확장 설치를 자동으로 권장합니다.

> **참고**: VS Code에서 저장소를 컨테이너 내에서 다시 열라는 제안이 나오면, 로컬에 설치된 Python 버전 사용을 위해 이 요청을 거부하세요.

### 브라우저에서 Jupyter 사용하기

브라우저 내에서 [Jupyter 환경](https://jupyter.org?WT.mc_id=academic-105485-koreyst)을 통해 프로젝트 작업도 가능합니다. 클래식 Jupyter 및 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst)는 자동 완성, 코드 하이라이팅 등 편리한 기능을 제공합니다.

로컬에서 Jupyter를 시작하려면 터미널/명령 창을 열고, 코스 디렉토리로 이동한 뒤 다음을 실행하세요:

```bash
jupyter notebook
```

또는

```bash
jupyterhub
```

이 명령을 실행하면 Jupyter 인스턴스가 시작되고, 접근할 수 있는 URL이 화면에 표시됩니다.

URL에 접근하면 코스 개요가 나타나고 `*.ipynb` 파일들을 탐색할 수 있습니다. 예를 들어 `08-building-search-applications/python/oai-solution.ipynb`.

### 컨테이너 안에서 실행하기

컴퓨터나 코드스페이스에 직접 모든 걸 설치하는 대신 [컨테이너](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)를 사용하는 방법도 있습니다. 코스 저장소 내 특별한 `.devcontainer` 폴더는 VS Code가 프로젝트를 컨테이너 내에서 설정하도록 돕습니다. Codespaces가 아닌 경우 Docker 설치가 필요하며, 다소 작업이 복잡할 수 있어 컨테이너 경험이 있는 분께만 권장합니다.

GitHub Codespaces에서 API 키를 안전하게 관리하는 가장 좋은 방법 중 하나는 Codespace Secrets 사용입니다. 자세한 내용은 [Codespaces 비밀 관리](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) 가이드를 참고하세요.


## 레슨 및 기술 요구 사항

이 코스는 개념 레슨 6개와 코딩 레슨 6개로 구성되어 있습니다.

코딩 레슨에서 Azure OpenAI 서비스를 사용합니다. 코드를 실행하려면 Azure OpenAI 서비스 접근 권한과 API 키가 필요합니다. [이 신청서를 작성](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)하여 접근 권한을 받을 수 있습니다.

신청 처리 중인 동안, 모든 코딩 레슨에는 코드를 보고 결과를 확인할 수 있는 `README.md` 파일도 포함되어 있습니다.

## 처음 Azure OpenAI 서비스 사용하기

Azure OpenAI 서비스를 처음 사용한다면, [Azure OpenAI 서비스 리소스 생성 및 배포 방법](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) 가이드를 따라주세요.

## 처음 OpenAI API 사용하기

OpenAI API를 처음 사용한다면, 인터페이스 생성 및 사용법에 대한 [가이드](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)를 참고하세요.

## 다른 학습자 만나기

공식 [AI 커뮤니티 Discord 서버](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)에 학습자들이 모일 수 있는 채널을 만들었습니다. 같은 관심사를 가진 기업가, 개발자, 학생 등과 네트워킹하기 좋은 장소입니다.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

프로젝트 팀도 이 Discord 서버에서 학습자들을 지원합니다.

## 기여하기

이 코스는 오픈 소스 프로젝트입니다. 개선점이나 문제를 발견하면 [풀 리퀘스트](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)를 만들거나 [GitHub 이슈](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)를 남겨주세요.

프로젝트 팀은 모든 기여를 추적합니다. 오픈 소스에 기여하는 것은 생성 AI 분야에서 경력을 쌓는 훌륭한 방법입니다.

대부분의 기여는 권리 보유와 기여 사용 권한을 공식화하는 기여자 라이선스 계약(CLA)을 요구합니다. 자세한 내용은 [CLA, 기여자 라이선스 계약 웹사이트](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)를 참고하세요.

중요: 저장소 내 텍스트를 번역할 때는 기계 번역을 사용하지 마세요. 커뮤니티가 번역을 검증하므로, 숙련된 언어에서만 자원봉사로 번역을 해주시기 바랍니다.

풀 리퀘스트 제출 시 CLA 봇이 자동으로 CLA 제출 필요 여부를 판단하고, PR에 라벨이나 코멘트를 달아줍니다. 봇의 안내에 따라 한 번만 처리하면 됩니다.

이 프로젝트는 [Microsoft 오픈 소스 행동 강령](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)을 채택했습니다. 자세한 내용은 행동 강령 FAQ를 읽거나 추가 질문/의견이 있으면 [Email opencode](opencode@microsoft.com)으로 문의하세요.

## 시작해봅시다!
이 과정을 완료하는 데 필요한 단계를 마쳤으니, [생성형 AI와 LLM 소개](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)를 통해 시작해 보겠습니다.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 내용이 포함될 수 있음을 유의하시기 바랍니다. 원문은 해당 문서의 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 오해나 오해의 소지에 대해 당사는 책임지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->