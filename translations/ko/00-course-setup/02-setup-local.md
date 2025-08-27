<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T15:14:05+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "ko"
}
-->
# 로컬 환경 설정 🖥️

**모든 작업을 내 노트북에서 직접 실행하고 싶다면 이 가이드를 따라주세요.**  
두 가지 방법이 있습니다: **(A) 기본 Python + 가상 환경** 또는 **(B) VS Code Dev Container와 Docker**.  
둘 중 편한 방법을 선택하세요—결과는 동일합니다.

## 1.  사전 준비

| 도구                | 버전 / 참고사항                                                                      |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 이상 (<https://python.org>에서 다운로드)                                         |
| **Git**            | 최신 버전 (Xcode / Git for Windows / Linux 패키지 매니저에 포함)                      |
| **VS Code**        | 선택 사항이지만 추천 <https://code.visualstudio.com>                                 |
| **Docker Desktop** | *옵션 B*에서만 필요. 무료 설치: <https://docs.docker.com/desktop/>                   |

> 💡 **Tip** – 터미널에서 도구 버전 확인:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  옵션 A – 기본 Python (가장 빠름)

### 1단계  저장소 클론

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### 2단계 가상 환경 생성 및 활성화

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ 프롬프트가 (.venv)로 시작하면 가상 환경에 진입한 것입니다.

### 3단계 의존성 설치

```bash
pip install -r requirements.txt
```

[API 키 추가](../../../00-course-setup) 섹션으로 건너뛰세요.

## 2. 옵션 B – VS Code Dev Container (Docker)

이 저장소와 강의는 [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst)로 구성되어 있습니다. 이 컨테이너는 Python3, .NET, Node.js, Java 개발을 지원하는 범용 런타임을 제공합니다. 관련 설정은 저장소 루트의 `.devcontainer/` 폴더 내 `devcontainer.json` 파일에 정의되어 있습니다.

>**이 방법을 선택하는 이유?**
>Codespaces와 동일한 환경을 제공하며, 의존성 차이가 없습니다.

### 0단계 추가 도구 설치

Docker Desktop – ```docker --version``` 명령이 잘 동작하는지 확인하세요.  
VS Code Remote – Containers 확장(확장 ID: ms-vscode-remote.remote-containers) 설치.

### 1단계 VS Code에서 저장소 열기

파일 ▸ 폴더 열기…  → generative-ai-for-beginners

VS Code가 .devcontainer/를 감지하고 안내 메시지를 띄웁니다.

### 2단계 컨테이너에서 다시 열기

“Reopen in Container”를 클릭하세요. Docker가 이미지를 빌드합니다(처음엔 약 3분 소요).  
터미널 프롬프트가 나타나면 컨테이너 내부에 진입한 것입니다.

## 2.  옵션 C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst)는 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, 그리고 몇 가지 패키지를 설치할 수 있는 가벼운 설치 도구입니다.  
Conda는 다양한 Python [**가상 환경**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)과 패키지를 쉽게 관리하고 전환할 수 있게 해주는 패키지 매니저입니다. pip으로 설치할 수 없는 패키지 설치에도 유용합니다.

### 0단계  Miniconda 설치

[MiniConda 설치 가이드](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst)를 참고해 설치하세요.

```bash
conda --version
```

### 1단계 가상 환경 생성

새 환경 파일(*environment.yml*)을 만드세요. Codespaces를 사용 중이라면 `.devcontainer` 디렉터리 내에 `.devcontainer/environment.yml`로 생성하세요.

### 2단계  환경 파일 내용 추가

아래 코드를 `environment.yml`에 추가하세요.

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

아래 명령어를 커맨드라인/터미널에 입력하세요.

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

문제가 발생하면 [Conda 환경 가이드](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)를 참고하세요.

## 2  옵션 D – 클래식 Jupyter / Jupyter Lab (브라우저에서 실행)

> **누구를 위한 방법인가요?**  
> 클래식 Jupyter 인터페이스를 선호하거나, VS Code 없이 노트북을 실행하고 싶은 분들께 추천합니다.  

### 1단계  Jupyter 설치 확인

Jupyter를 로컬에서 실행하려면 터미널/명령 프롬프트에서 강의 디렉터리로 이동한 후 다음을 실행하세요.

```bash
jupyter notebook
```

또는

```bash
jupyterhub
```

명령어 실행 후 Jupyter 인스턴스가 시작되고, 접속할 수 있는 URL이 명령줄에 표시됩니다.

해당 URL에 접속하면 강의 목차가 보이고, 원하는 `*.ipynb` 파일(예: `08-building-search-applications/python/oai-solution.ipynb`)로 이동할 수 있습니다.

## 3. API 키 추가

API 키를 안전하게 관리하는 것은 모든 애플리케이션 개발에서 매우 중요합니다.  
API 키를 코드에 직접 저장하지 않는 것을 권장합니다. 키가 공개 저장소에 커밋되면 보안 문제나 예기치 않은 비용이 발생할 수 있습니다.  
아래는 Python용 `.env` 파일을 만들고 `GITHUB_TOKEN`을 추가하는 단계별 가이드입니다.

1. **프로젝트 디렉터리로 이동**: 터미널이나 명령 프롬프트를 열고, `.env` 파일을 만들고자 하는 프로젝트 루트 디렉터리로 이동하세요.

   ```bash
   cd path/to/your/project
   ```

2. **`.env` 파일 생성**: 선호하는 텍스트 에디터로 `.env`라는 새 파일을 만드세요. 커맨드라인을 사용할 경우, Unix 계열은 `touch`, Windows는 `echo`를 사용할 수 있습니다.

   Unix 계열:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` 파일 편집**: `.env` 파일을 텍스트 에디터(VS Code, Notepad++ 등)로 열고, 아래 줄을 추가하세요. `your_github_token_here` 부분을 실제 GitHub 토큰으로 바꿔주세요.

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **파일 저장**: 변경 사항을 저장하고 에디터를 닫으세요.

5. **`python-dotenv` 설치**: 아직 설치하지 않았다면, `.env` 파일의 환경 변수를 Python 애플리케이션에서 불러오기 위해 `python-dotenv` 패키지를 설치해야 합니다. pip로 설치할 수 있습니다.

   ```bash
   pip install python-dotenv
   ```

6. **Python 스크립트에서 환경 변수 불러오기**: Python 스크립트에서 `python-dotenv` 패키지를 사용해 `.env` 파일의 환경 변수를 불러오세요.

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

이제 완료입니다! `.env` 파일을 만들고, GitHub 토큰을 추가했으며, 이를 Python 애플리케이션에서 불러올 수 있게 되었습니다.

🔐 .env 파일은 절대 커밋하지 마세요—이미 .gitignore에 포함되어 있습니다.  
자세한 공급자별 안내는 [`providers.md`](03-providers.md)에서 확인하세요.

## 4. 다음 단계는?

| 하고 싶은 일         | 이동 경로                                                                  |
|---------------------|-------------------------------------------------------------------------|
| 1강 시작하기         | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| LLM 공급자 설정      | [`providers.md`](03-providers.md)                                       |
| 다른 학습자 만나기   | [Discord 참여하기](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. 문제 해결

| 증상                                         | 해결 방법                                                         |
|----------------------------------------------|-------------------------------------------------------------------|
| `python not found`                           | Python을 PATH에 추가하거나 설치 후 터미널을 다시 여세요            |
| `pip`이 wheel 빌드 불가 (Windows)            | `pip install --upgrade pip setuptools wheel` 실행 후 재시도        |
| `ModuleNotFoundError: dotenv`                | `pip install -r requirements.txt` 실행 (환경이 설치되지 않음)      |
| Docker 빌드 실패 *No space left*             | Docker Desktop ▸ *Settings* ▸ *Resources* → 디스크 용량 늘리기     |
| VS Code가 계속 컨테이너 재실행 안내          | 두 옵션이 모두 활성화된 경우일 수 있음; 하나만 선택(venv **또는** container)|
| OpenAI 401 / 429 오류                        | `OPENAI_API_KEY` 값 및 요청 속도 제한 확인                        |
| Conda 사용 중 오류                           | `conda install -c microsoft azure-ai-ml`로 Microsoft AI 라이브러리 설치|

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서(원어)가 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 오해나 오역에 대해 당사는 책임을 지지 않습니다.