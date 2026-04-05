# 로컬 설정 🖥️

**모든 것을 자신의 노트북에서 실행하고 싶다면 이 가이드를 사용하세요.**  
두 가지 경로가 있습니다: **(A) 네이티브 Python + 가상 환경** 또는 **(B) Docker가 포함된 VS Code 개발 컨테이너**.  
더 쉬운 방법을 선택하세요—두 방법 모두 동일한 수업으로 이어집니다.

## 1.  사전 준비 사항

| 도구               | 버전 / 참고사항                                                                      |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 이상 (<https://python.org>에서 다운로드)                                        |
| **Git**            | 최신 버전 (Xcode / Windows용 Git / Linux 패키지 관리자에 포함)                        |
| **VS Code**        | 선택 사항이지만 권장 <https://code.visualstudio.com>                                 |
| **Docker Desktop** | *옵션 B에만 필요*. 무료 설치: <https://docs.docker.com/desktop/>                     |

> 💡 **팁** – 터미널에서 도구 확인:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  옵션 A – 네이티브 Python (가장 빠름)

### 1단계  이 저장소 복제

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### 2단계 가상 환경 생성 및 활성화

```bash
python -m venv .venv          # 하나 만들기
source .venv/bin/activate     # macOS / 리눅스
.\.venv\Scripts\activate      # 윈도우 파워셸
```

✅ 프롬프트가 (.venv)로 시작하면 가상 환경 안에 있는 것입니다.

### 3단계 의존성 설치

```bash
pip install -r requirements.txt
```

[API 키 추가](../../../00-course-setup) 섹션 3으로 건너뛰세요.

## 2. 옵션 B – VS Code 개발 컨테이너 (Docker)

이 저장소와 강의는 Python3, .NET, Node.js, Java 개발을 지원하는 범용 런타임이 포함된 [개발 컨테이너](https://containers.dev?WT.mc_id=academic-105485-koreyst)로 설정되어 있습니다. 관련 구성은 이 저장소 루트의 `.devcontainer/` 폴더 내 `devcontainer.json` 파일에 정의되어 있습니다.

>**왜 이걸 선택하나요?**  
>Codespaces와 동일한 환경; 의존성 변동 없음.

### 0단계 추가 도구 설치

Docker Desktop – ```docker --version``` 명령어가 작동하는지 확인하세요.  
VS Code Remote – Containers 확장 (ID: ms-vscode-remote.remote-containers).

### 1단계 VS Code에서 저장소 열기

파일 ▸ 폴더 열기… → generative-ai-for-beginners

VS Code가 .devcontainer/를 감지하고 프롬프트를 표시합니다.

### 2단계 컨테이너에서 다시 열기

“Reopen in Container”를 클릭하세요. Docker가 이미지를 빌드합니다 (첫 실행 약 3분).  
터미널 프롬프트가 나타나면 컨테이너 안에 있는 것입니다.

## 2.  옵션 C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst)는 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python 및 몇 가지 패키지를 설치하는 경량 설치 프로그램입니다.  
Conda는 패키지 관리자이며, 다양한 Python [**가상 환경**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)과 패키지를 쉽게 설정하고 전환할 수 있게 해줍니다. 또한 `pip`로 설치할 수 없는 패키지 설치에도 유용합니다.

### 0단계  Miniconda 설치

[MiniConda 설치 가이드](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst)를 따라 설치하세요.

```bash
conda --version
```

### 1단계 가상 환경 생성

새 환경 파일(*environment.yml*)을 만드세요. Codespaces를 사용하는 경우 `.devcontainer` 디렉터리 내에 생성하여 `.devcontainer/environment.yml`로 만드세요.

### 2단계 환경 파일 내용 작성

다음 스니펫을 `environment.yml`에 추가하세요.

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

### 3단계 Conda 환경 생성

명령줄/터미널에서 아래 명령어를 실행하세요.

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer 하위 경로는 Codespace 설정에만 적용됩니다
conda activate ai4beg
```

문제가 발생하면 [Conda 환경 가이드](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)를 참고하세요.

## 2  옵션 D – 클래식 Jupyter / Jupyter Lab (브라우저에서)

> **누구를 위한 것인가요?**  
> 클래식 Jupyter 인터페이스를 좋아하거나 VS Code 없이 노트북을 실행하고 싶은 분.

### 1단계 Jupyter 설치 확인

로컬에서 Jupyter를 시작하려면 터미널/명령줄에서 강의 디렉터리로 이동한 후 다음을 실행하세요:

```bash
jupyter notebook
```

또는

```bash
jupyterhub
```

이 명령어는 Jupyter 인스턴스를 시작하며, 접속할 URL이 명령줄 창에 표시됩니다.

URL에 접속하면 강의 개요를 보고 `*.ipynb` 파일을 탐색할 수 있습니다. 예: `08-building-search-applications/python/oai-solution.ipynb`.

## 3. API 키 추가하기

API 키를 안전하게 보관하는 것은 어떤 애플리케이션을 만들 때도 중요합니다. API 키를 코드에 직접 저장하지 않는 것을 권장합니다. 공개 저장소에 키를 커밋하면 보안 문제나 악의적 사용으로 인한 원치 않는 비용이 발생할 수 있습니다.  
Python용 `.env` 파일을 만들고 `GITHUB_TOKEN`을 추가하는 단계별 가이드는 다음과 같습니다:

1. **프로젝트 디렉터리로 이동**: 터미널 또는 명령 프롬프트를 열고 `.env` 파일을 만들고자 하는 프로젝트 루트 디렉터리로 이동하세요.

   ```bash
   cd path/to/your/project
   ```

2. **`.env` 파일 생성**: 선호하는 텍스트 편집기로 `.env`라는 새 파일을 만드세요. 명령줄을 사용하는 경우 Unix 기반 시스템에서는 `touch`, Windows에서는 `echo`를 사용할 수 있습니다:

   Unix 기반 시스템:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` 파일 편집**: 텍스트 편집기(예: VS Code, Notepad++ 등)로 `.env` 파일을 열고 다음 줄을 추가하세요. `your_github_token_here`를 실제 GitHub 토큰으로 바꾸세요:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **파일 저장**: 변경 사항을 저장하고 편집기를 닫으세요.

5. **`python-dotenv` 설치**: 아직 설치하지 않았다면, `.env` 파일에서 환경 변수를 Python 애플리케이션으로 불러오기 위해 `python-dotenv` 패키지를 설치해야 합니다. `pip`로 설치할 수 있습니다:

   ```bash
   pip install python-dotenv
   ```

6. **Python 스크립트에서 환경 변수 불러오기**: Python 스크립트에서 `python-dotenv` 패키지를 사용해 `.env` 파일의 환경 변수를 불러오세요:

   ```python
   from dotenv import load_dotenv
   import os

   # .env 파일에서 환경 변수를 로드합니다
   load_dotenv()

   # GITHUB_TOKEN 변수를 접근합니다
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

이제 완료되었습니다! `.env` 파일을 만들고 GitHub 토큰을 추가했으며 Python 애플리케이션에서 불러왔습니다.

🔐 `.env` 파일은 절대 커밋하지 마세요—이미 `.gitignore`에 포함되어 있습니다.  
전체 제공자 지침은 [`providers.md`](03-providers.md)에 있습니다.

## 4. 다음 단계는?

| 하고 싶은 일          | 이동할 곳                                                               |
|---------------------|-------------------------------------------------------------------------|
| 1과 시작하기         | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| LLM 제공자 설정하기  | [`providers.md`](03-providers.md)                                       |
| 다른 학습자 만나기   | [Discord 참여하기](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. 문제 해결

| 증상                                   | 해결 방법                                                        |
|---------------------------------------|-----------------------------------------------------------------|
| `python not found`                    | Python을 PATH에 추가하거나 설치 후 터미널을 다시 열기           |
| `pip`이 휠을 빌드할 수 없음 (Windows) | `pip install --upgrade pip setuptools wheel` 실행 후 재시도     |
| `ModuleNotFoundError: dotenv`         | `pip install -r requirements.txt` 실행 (환경이 설치되지 않음)    |
| Docker 빌드 실패 *No space left*      | Docker Desktop ▸ *설정* ▸ *리소스* → 디스크 크기 증가           |
| VS Code가 계속 다시 열기 요청         | 두 옵션이 모두 활성화된 경우; 하나만 선택 (venv **또는** 컨테이너) |
| OpenAI 401 / 429 오류                 | `OPENAI_API_KEY` 값 확인 / 요청 속도 제한 확인                   |
| Conda 사용 시 오류                    | `conda install -c microsoft azure-ai-ml`로 Microsoft AI 라이브러리 설치 |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의해 주시기 바랍니다. 원문 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인한 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->