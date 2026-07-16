# 이 강좌 시작하기

이 강좌를 시작하고 생성형 AI로 무엇을 만들고 싶은지 영감을 받을 여러분께 매우 기대가 큽니다!

성공을 보장하기 위해, 이 페이지에는 설정 단계, 기술 요구 사항, 필요 시 도움받을 곳이 안내되어 있습니다.

## 설정 단계

강좌를 시작하려면 다음 단계를 완료해야 합니다.

### 1. 이 저장소를 포크하세요

모든 코드를 변경하고 과제를 완료할 수 있도록 [이 저장소 전체를 포크하세요](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst). 또한 [이 저장소에 별(🌟) 표시하기](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)로 관련 저장소를 더 쉽게 찾을 수 있습니다.

### 2. 코드스페이스 생성하기

의존성 문제를 피하려면 이 강좌를 [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)에서 실행하는 것을 권장합니다.

포크 저장소에서: **Code -> Codespaces -> New on main**

![코드스페이스 생성 버튼이 표시된 대화상자](../../../translated_images/ko/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 비밀 추가하기

1. ⚙️ 톱니바퀴 아이콘 -> Command Pallete-> Codespaces : 사용자 비밀 관리 -> 새 비밀 추가.
2. 이름: OPENAI_API_KEY, 키를 붙여넣고 저장.

### 3. 다음 단계는?

| 나는…                  | 이동할 곳                                                            |
|------------------------|-------------------------------------------------------------------------|
| 1과 시작하기            | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| 오프라인으로 작업하기   | [`setup-local.md`](02-setup-local.md)                                   |
| LLM 공급자 설정하기     | [`providers.md`](03-providers.md)                                        |
| 다른 학습자 만나기      | [우리 Discord에 참여하기](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 문제 해결


| 증상                                       | 해결책                                                        |
|--------------------------------------------|-----------------------------------------------------------------|
| 컨테이너 빌드가 10분 이상 멈춤             | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found` 오류            | 터미널이 연결되지 않음; **+** 클릭 ➜ *bash* 실행                |
| OpenAI에서 `401 Unauthorized` 오류          | 잘못되었거나 만료된 `OPENAI_API_KEY`                             |
| VS Code가 “Dev container mounting…” 표시   | 브라우저 탭 새로고침—Codespaces가 연결을 잃을 수 있음           |
| 노트북 커널이 없음                           | 노트북 메뉴 ➜ **Kernel ▸ Select Kernel ▸ Python 3**             |

   유닉스 기반 시스템:

   ```bash
   touch .env
   ```

   윈도우즈:

   ```cmd
   echo . > .env
   ```

3. **`.env` 파일 편집하기**: 텍스트 편집기(e.g., VS Code, Notepad++, 기타 편집기)로 `.env` 파일을 열고, 아래 내용을 실제 Microsoft Foundry Models 엔드포인트와 키로 바꿔 추가하세요([`providers.md`](03-providers.md) 참고).

   > **참고:** GitHub Models(`GITHUB_TOKEN` 변수 포함)는 2026년 7월 말에 종료됩니다. 대신 [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)를 사용하세요.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **파일 저장하기**: 변경사항을 저장하고 텍스트 편집기를 닫으세요.

5. **`python-dotenv` 설치하기**: 아직 설치하지 않았다면, `.env` 파일의 환경 변수를 Python 애플리케이션에 불러오기 위해 `python-dotenv` 패키지를 설치해야 합니다. `pip`으로 설치할 수 있습니다:

   ```bash
   pip install python-dotenv
   ```

6. **Python 스크립트에서 환경 변수 불러오기**: Python 스크립트에서 `python-dotenv`를 사용해 `.env` 파일의 환경 변수를 불러오세요:

   ```python
   from dotenv import load_dotenv
   import os

   # .env 파일에서 환경 변수 로드
   load_dotenv()

   # Microsoft Foundry Models 변수를 액세스하기
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

완료되었습니다! `.env` 파일을 만들고, Microsoft Foundry Models 자격 증명을 추가한 후 Python 애플리케이션에서 불러왔습니다.

## 로컬 컴퓨터에서 실행하는 방법

코드를 로컬 컴퓨터에서 실행하려면 [Python이 설치되어 있어야 합니다](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

저장소를 사용하려면, 먼저 클론해야 합니다:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

모든 것을 준비한 후 시작할 수 있습니다!

## 선택적 단계

### Miniconda 설치하기

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst)는 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python 및 몇몇 패키지를 설치하는 경량 설치 프로그램입니다.
Conda는 패키지 관리자이며, 다양한 Python [**가상 환경**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)과 패키지를 쉽게 설정하고 전환할 수 있게 도와줍니다. 또한 `pip`으로 설치할 수 없는 패키지 설치에도 유용합니다.

[MiniConda 설치 가이드](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst)를 따라 설치할 수 있습니다.

Miniconda 설치 후, 저장소를 클론해야 합니다 (아직 하지 않았다면)

다음으로 가상 환경을 만들어야 합니다. Conda로 하려면 새 환경 파일(_environment.yml_)을 만드세요. Codespaces를 따라하는 경우 `.devcontainer` 디렉터리에 만들어 `.devcontainer/environment.yml`가 됩니다.

환경 파일에 아래 스니펫을 채워 넣으세요:

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

Conda 사용 중 오류가 발생하면, 터미널에서 다음 명령어로 Microsoft AI 라이브러리를 수동 설치할 수 있습니다.

```
conda install -c microsoft azure-ai-ml
```

환경 파일에는 필요한 의존성이 명시되어 있습니다. `<environment-name>`은 Conda 환경 이름, `<python-version>`은 원하는 Python 버전이며 예를 들어 `3`이 최신 메이저 버전입니다.

완료되면 아래 명령어로 Conda 환경을 생성하세요.

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer 하위 경로는 Codespace 설정에만 적용됩니다
conda activate ai4beg
```

문제가 있으면 [Conda 환경 가이드](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)를 참조하세요.

### Python 지원 확장과 함께 Visual Studio Code 사용하기

이 강좌에서는 [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) 편집기와 [Python 지원 확장](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 설치를 권장합니다. 이는 권장일 뿐 필수는 아닙니다.

> <strong>참고</strong>: 강좌 저장소를 VS Code에서 열면 프로젝트를 컨테이너 내에서 설정할 수 있는 옵션이 있습니다. 이는 강좌 저장소 내 특별한 [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 디렉터리 덕분입니다. 자세한 내용은 나중에 다룹니다.

> <strong>참고</strong>: 저장소를 클론하고 VS Code에서 열면 Python 지원 확장 설치를 자동으로 제안합니다.

> <strong>참고</strong>: VS Code가 저장소를 컨테이너에서 다시 열라고 제안하면, 로컬 Python 버전을 사용하려면 거절하세요.

### 브라우저에서 Jupyter 사용하기

브라우저 내에서 [Jupyter 환경](https://jupyter.org?WT.mc_id=academic-105485-koreyst)으로도 프로젝트 작업 가능하며, 클래식 Jupyter와 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst)가 자동 완성, 코드 하이라이트 등 쾌적한 개발 환경을 제공합니다.

로컬에서 Jupyter를 시작하려면 터미널/명령줄에서 강좌 디렉터리로 이동해 다음을 실행하세요:

```bash
jupyter notebook
```

또는

```bash
jupyterhub
```

이렇게 하면 Jupyter 인스턴스가 시작되고, 접속 URL이 명령줄에 표시됩니다.

URL에 접속하면 강좌 개요를 볼 수 있으며 모든 `*.ipynb` 파일로 이동할 수 있습니다. 예: `08-building-search-applications/python/oai-solution.ipynb`.

### 컨테이너에서 실행하기

컴퓨터나 코드스페이스에 직접 설정하는 대신 [컨테이너](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)를 사용할 수 있습니다. 강좌 저장소의 `.devcontainer` 폴더가 VS Code가 프로젝트를 컨테이너 내에서 설정할 수 있게 합니다. Codespaces 외부에서는 Docker 설치가 필요하며, 다소 복잡하므로 컨테이너 작업 경험자에게 권장합니다.

GitHub Codespaces 사용 시 API 키를 안전하게 관리하는 최고의 방법 중 하나는 Codespace Secrets 사용입니다. 자세한 내용은 [Codespaces 비밀 관리](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) 가이드를 참고하세요.


## 강좌 및 기술 요구 사항

이 강좌에는 생성형 AI 개념을 설명하는 "학습" 강의와 가능하면 **Python** 및 <strong>TypeScript</strong>의 실제 코드 예제를 다루는 "개발" 강의가 포함되어 있습니다.

코딩 강의에서는 Microsoft Foundry의 Azure OpenAI를 사용합니다. Azure 구독과 API 키가 필요하며, 신청 없이 바로 액세스할 수 있으므로 [Microsoft Foundry 리소스 생성 및 모델 배포](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)를 통해 엔드포인트와 키를 얻을 수 있습니다.

각 코딩 강의는 실행하지 않고도 코드와 결과를 볼 수 있는 `README.md` 파일도 포함합니다.

## Azure OpenAI 서비스 처음 사용하기

Azure OpenAI 서비스를 처음 사용한다면, [Azure OpenAI 서비스 리소스 생성 및 배포 방법](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) 가이드를 따르세요.

## OpenAI API 처음 사용하기

OpenAI API를 처음 사용하는 경우, [인터페이스 생성 및 사용 방법](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) 가이드를 따라주세요.

## 다른 학습자 만나기

우리는 공식 [AI 커뮤니티 Discord 서버](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)에 다른 학습자와 만날 수 있는 채널을 만들었습니다. 이는 비슷한 관심사를 가진 창업자, 개발자, 학생 및 생성형 AI 실력 향상을 원하는 모든 사람과 네트워크를 형성할 수 있는 좋은 방법입니다.

[![Discord 채널 참여하기](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

프로젝트 팀도 이 Discord 서버에 있어 학습자를 도울 것입니다.

## 기여하기

이 강좌는 오픈소스 프로젝트입니다. 개선점이나 문제를 발견하면 [풀 리퀘스트](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)를 생성하거나 [GitHub 이슈](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)를 등록해 주세요.

프로젝트 팀이 모든 기여를 추적할 것입니다. 오픈소스 기여는 생성형 AI 분야 경력을 쌓는 데 훌륭한 방법입니다.

대부분 기여는 기여자 라이선스 계약서(CLA)를 승인해야 하는데, 이는 기여에 대한 권리를 실제로 보유하고 Microsoft에 사용 권리를 부여한다는 선언입니다. 자세한 내용은 [CLA, 기여자 라이선스 계약서 웹사이트](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)를 참조하세요.

중요: 이 저장소의 텍스트 번역 시 기계 번역 사용을 삼가 주세요. 번역은 커뮤니티 검증 대상이므로, 능통한 언어에만 자원봉사 번역을 부탁드립니다.


풀 리퀘스트를 제출하면 CLA-bot이 자동으로 CLA 제출 필요 여부를 판단하고 PR에 적절한 표시(예: 라벨, 댓글)를 합니다. 봇이 제공하는 지침에 따라 진행하기만 하면 됩니다. 당사 CLA를 사용하는 모든 저장소에서 이 작업은 한 번만 수행하면 됩니다.

이 프로젝트는 [Microsoft 오픈 소스 행동 강령](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)을 채택했습니다. 자세한 내용은 행동 강령 FAQ를 읽거나 추가 질문이나 의견이 있으면 [이메일 opencode](opencode@microsoft.com)로 문의하세요.

## 시작해 봅시다

이 과정을 완료하는 데 필요한 단계를 마쳤으니, [생성 AI 및 LLM 소개](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)부터 시작해 봅시다.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->