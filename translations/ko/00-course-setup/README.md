# 이 과정 시작하기

이 과정을 시작하고 생성 AI로 무엇을 만들고 영감을 받을지 보는 것에 대해 매우 기대하고 있습니다!

성공을 보장하기 위해 이 페이지에는 설정 단계, 기술 요구 사항, 필요 시 도움을 받을 수 있는 위치가 안내되어 있습니다.

## 설정 단계

이 과정을 시작하려면 다음 단계를 완료해야 합니다.

### 1. 이 저장소를 포크하기

자신의 GitHub 계정으로 [이 저장소 전체를 포크하세요](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst). 그래야 코드를 변경하고 과제를 완료할 수 있습니다. 또한 [이 저장소에 스타(🌟)를 줄 수도 있습니다](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), 그래야 이 저장소와 관련 저장소를 더 쉽게 찾을 수 있습니다.

### 2. 코드스페이스 생성하기

코드 실행 시 의존성 문제를 피하려면 이 과정을 [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)에서 실행하는 것을 권장합니다.

포크한 저장소에서: **Code -> Codespaces -> New on main**

![코드스페이스 생성을 위한 버튼이 보여지는 대화상자](../../../translated_images/ko/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 시크릿 추가하기

1. ⚙️ 톱니바퀴 아이콘 -> 명령 팔레트 -> Codespaces : 사용자 시크릿 관리 -> 새 시크릿 추가.
2. 이름은 OPENAI_API_KEY, 키를 붙여넣고 저장.

### 3. 다음 단계는?

| 하고 싶은 일          | 이동할 곳                                                                 |
|---------------------|-------------------------------------------------------------------------|
| 1과 시작하기         | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| 오프라인 작업하기     | [`setup-local.md`](02-setup-local.md)                                   |
| LLM 공급자 설정하기  | [`providers.md`](03-providers.md)                                        |
| 다른 학습자 만나기    | [우리 Discord 참여하기](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 문제 해결


| 증상                                  | 해결 방법                                                       |
|--------------------------------------|-----------------------------------------------------------------|
| 컨테이너 빌드가 10분 이상 멈춤        | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`            | 터미널이 연결되지 않음; **+** 클릭 ➜ *bash* 선택                  |
| OpenAI에서 `401 Unauthorized` 발생     | 잘못되었거나 만료된 `OPENAI_API_KEY`                            |
| VS Code가 “Dev container mounting…” 표시 | 브라우저 탭 새로 고침—Codespaces가 가끔 연결을 잃음               |
| 노트북 커널 없음                      | 노트북 메뉴 ➜ **Kernel ▸ Select Kernel ▸ Python 3**              |

   유닉스 기반 시스템:

   ```bash
   touch .env
   ```

   윈도우:

   ```cmd
   echo . > .env
   ```

3. **`.env` 파일 편집**: 텍스트 편집기(예: VS Code, Notepad++, 또는 기타 편집기)로 `.env` 파일을 열고, 실제 Microsoft Foundry Models 엔드포인트 및 키로 자리 표시자를 교체하며 다음 줄을 추가하세요 ([`providers.md`](03-providers.md)에서 방법 확인 가능).

   > **참고:** GitHub Models (및 `GITHUB_TOKEN` 변수)은 2026년 7월 말에 종료됩니다. 대신 [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)를 사용하세요.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **파일 저장하기**: 변경사항을 저장하고 텍스트 편집기를 닫으세요.

5. **`python-dotenv` 설치하기**: 아직 설치하지 않았다면 `python-dotenv` 패키지를 설치해 `.env` 파일의 환경 변수를 Python 애플리케이션에 불러올 수 있게 하세요. `pip`로 설치할 수 있습니다:

   ```bash
   pip install python-dotenv
   ```

6. **Python 스크립트에서 환경 변수 불러오기**: Python 스크립트에서 `python-dotenv` 패키지를 이용해 `.env` 파일의 환경 변수를 불러오세요:

   ```python
   from dotenv import load_dotenv
   import os

   # .env 파일에서 환경 변수 로드
   load_dotenv()

   # Microsoft Foundry Models 변수에 접근
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

완료되었습니다! `.env` 파일을 성공적으로 만들고 Microsoft Foundry Models 자격 증명을 추가하며 이를 Python 애플리케이션에 불러왔습니다.

## 컴퓨터에서 로컬로 실행하는 방법

컴퓨터에서 코드를 로컬로 실행하려면 [Python이 설치되어 있어야 합니다](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

그런 다음 저장소를 사용하려면 클론해야 합니다:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

준비가 다 되면 시작할 수 있습니다!

## 선택적 단계

### Miniconda 설치하기

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst)는 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python 및 몇 가지 패키지를 설치하기 위한 경량 설치 프로그램입니다.
Conda 자체는 패키지 관리자이며, 다양한 Python [**가상 환경**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)과 패키지를 쉽게 설정하고 전환할 수 있게 해줍니다. 또한 `pip`으로 설치할 수 없는 패키지를 설치할 때도 유용합니다.

[MiniConda 설치 가이드](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst)를 따라 설정하세요.

Miniconda를 설치한 뒤, 저장소를 클론해야 합니다 (아직 하지 않았다면).

이제 가상 환경을 생성해야 합니다. Conda로 이를 하려면 환경 파일(_environment.yml_)을 새로 만드세요. Codespaces를 사용하는 경우 `.devcontainer` 디렉터리에 만들어야 하므로 파일 경로는 `.devcontainer/environment.yml`입니다.

환경 파일에 아래 스니펫을 채우세요:

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

환경 파일은 필요한 종속성을 지정합니다. `<environment-name>`은 Conda 환경 이름이며 `<python-version>`은 사용하고 싶은 Python 버전입니다. 예를 들어, `3`은 최신 주요 Python 버전입니다.

설정이 완료되면 명령 줄/터미널에서 아래 명령어를 실행해 Conda 환경을 생성할 수 있습니다.

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer 하위 경로는 Codespace 설정에만 적용됩니다
conda activate ai4beg
```

문제 발생 시 [Conda 환경 가이드](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)를 참조하세요.

### Python 지원 확장 프로그램과 함께 Visual Studio Code 사용하기

이 과정에서는 [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) 편집기와 [Python 지원 확장 프로그램](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)을 사용하는 것을 권장합니다. 하지만 필수 사항은 아닙니다.

> <strong>참고</strong>: 과정 저장소를 VS Code에서 열면 프로젝트를 컨테이너 내에서 설정할 수 있습니다. 이는 저장소 내에 있는 [특별한 `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 디렉터리 때문입니다. 자세한 내용은 나중에 다룹니다.

> <strong>참고</strong>: 저장소를 클론해 VS Code에서 열면 Python 지원 확장 프로그램 설치를 자동으로 제안합니다.

> <strong>참고</strong>: VS Code가 저장소를 컨테이너에서 다시 열라고 제안하면, 로컬에 설치된 Python 버전을 사용하기 위해 이 요청을 거절하세요.

### 브라우저에서 Jupyter 사용하기

브라우저 내에서 [Jupyter 환경](https://jupyter.org?WT.mc_id=academic-105485-koreyst)을 사용하여 프로젝트 작업도 가능합니다. 고전적인 Jupyter와 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) 모두 자동 완성, 코드 하이라이팅 등의 기능을 갖춘 쾌적한 개발 환경을 제공합니다.

로컬에서 Jupyter를 시작하려면 터미널/명령 줄에서 과정 디렉터리로 이동한 후 다음을 실행하세요:

```bash
jupyter notebook
```

또는

```bash
jupyterhub
```

Jupyter 인스턴스가 시작되며, 접근할 수 있는 URL이 명령 줄 창에 표시됩니다.

URL에 접속하면 과정 개요를 보고 모든 `*.ipynb` 파일로 이동할 수 있습니다. 예를 들어, `08-building-search-applications/python/oai-solution.ipynb` 등이 있습니다.

### 컨테이너에서 실행하기

모든 것을 컴퓨터나 코드스페이스에 설정하는 대신, [컨테이너](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)를 사용할 수도 있습니다. 과정 저장소 내 특별한 `.devcontainer` 폴더 덕분에 VS Code가 프로젝트를 컨테이너 내에서 설정할 수 있습니다. Codespaces 외부에서는 Docker 설치가 필요하며 다소 작업이 필요하므로, 컨테이너 작업 경험이 있는 사람에게만 권장합니다.

GitHub Codespaces 사용 시 API 키를 안전하게 유지하는 최고의 방법 중 하나는 Codespace Secrets를 사용하는 것입니다. 이에 대해서는 [Codespaces 시크릿 관리](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) 가이드를 따르세요.


## 강의 및 기술 요구 사항

과정은 6개의 개념 강의와 6개의 코딩 강의로 구성되어 있습니다.

코딩 강의에서는 Azure OpenAI 서비스를 사용합니다. 이 코드를 실행하려면 Azure OpenAI 서비스 접근권과 API 키가 필요합니다. [신청서를 작성하여](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) 접근권을 받을 수 있습니다.

신청서가 처리되는 동안, 각 코딩 강의에는 코드와 출력을 볼 수 있는 `README.md` 파일도 포함되어 있습니다.

## Azure OpenAI 서비스를 처음 사용하는 경우

Azure OpenAI 서비스를 처음 사용하는 경우, [리소스 생성 및 배포](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) 가이드를 따라주세요.

## OpenAI API를 처음 사용하는 경우

OpenAI API를 처음 사용하는 경우, [인터페이스 생성 및 사용법](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) 가이드를 따르세요.

## 다른 학습자 만나기

공식 [AI 커뮤니티 Discord 서버](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)에 다른 학습자들과 만날 수 있는 채널을 만들었습니다. 이는 비슷한 생각을 가진 창업자, 개발자, 학생과 네트워크를 형성하고 생성 AI 실력을 키울 수 있는 훌륭한 방법입니다.

[![디스코드 채널 참가](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

프로젝트 팀도 이 Discord 서버에서 학습자들을 도울 예정입니다.

## 기여하기

이 과정은 오픈 소스 프로젝트입니다. 개선할 부분이나 문제가 있으면 [풀 리퀘스트](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)를 생성하거나 [GitHub 이슈](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)를 기록해 주세요.

프로젝트 팀은 모든 기여를 추적할 것입니다. 오픈 소스에 기여하는 것은 생성 AI 분야에서 경력을 쌓는 놀라운 방법입니다.

대부분의 기여는 기여자가 자신의 기여를 사용할 권리를 실제로 부여한다는 것을 선언하는 기여자 라이선스 계약(CLA)에 동의해야 합니다. 자세한 내용은 [CLA, 기여자 라이선스 계약 웹사이트](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)를 방문하세요.

중요: 이 저장소의 텍스트를 번역할 때 기계 번역을 사용하지 마세요. 커뮤니티를 통해 번역을 검증할 것이므로, 능숙한 언어의 번역 자원봉사만 해 주시기 바랍니다.

풀 리퀘스트를 제출하면, CLA-bot이 자동으로 CLA 제출 여부를 판단하고 PR에 적절한 레이블이나 코멘트를 붙입니다. 봇의 지시에 따르기만 하면 됩니다. 모든 저장소에서 CLA를 한 번만 제출하면 됩니다.


이 프로젝트는 [Microsoft 오픈 소스 행동 강령](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)을 채택했습니다. 자세한 내용은 행동 강령 FAQ를 읽거나 추가 질문이나 의견이 있으면 [이메일 opencode](opencode@microsoft.com)로 문의하십시오.

## 시작해 봅시다

이제 이 과정을 완료하는 데 필요한 단계를 마쳤으니, [생성형 AI 및 LLM 소개](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)를 통해 시작해 봅시다.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->