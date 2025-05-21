<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T09:02:14+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "pl"
}
-->
# Konfiguracja środowiska deweloperskiego

Skonfigurowaliśmy to repozytorium i kurs za pomocą [kontenera deweloperskiego](https://containers.dev?WT.mc_id=academic-105485-koreyst), który ma uniwersalne środowisko uruchomieniowe wspierające rozwój w Python3, .NET, Node.js i Java. Powiązana konfiguracja jest zdefiniowana w pliku `devcontainer.json` znajdującym się w folderze `.devcontainer/` na głównym poziomie tego repozytorium.

Aby aktywować kontener deweloperski, uruchom go w [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (dla środowiska uruchomieniowego w chmurze) lub w [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (dla lokalnego środowiska uruchomieniowego). Przeczytaj [tę dokumentację](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) aby uzyskać więcej informacji o działaniu kontenerów deweloperskich w VS Code.

> [!TIP]  
> Zalecamy użycie GitHub Codespaces dla szybkiego startu przy minimalnym wysiłku. Zapewnia on hojny [darmowy limit użytkowania](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) dla kont osobistych. Skonfiguruj [limity czasowe](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) aby zatrzymać lub usunąć nieaktywne przestrzenie kodowe i maksymalnie wykorzystać swój limit.

## 1. Wykonywanie zadań

Każda lekcja będzie miała _opcjonalne_ zadania, które mogą być dostarczone w jednym lub kilku językach programowania, w tym: Python, .NET/C#, Java i JavaScript/TypeScript. Ta sekcja zawiera ogólne wskazówki dotyczące wykonywania tych zadań.

### 1.1 Zadania w Pythonie

Zadania w Pythonie są dostarczane albo jako aplikacje (pliki `.py`) albo notatniki Jupyter (pliki `.ipynb`).
- Aby uruchomić notatnik, otwórz go w Visual Studio Code, a następnie kliknij _Select Kernel_ (w prawym górnym rogu) i wybierz domyślną opcję Python 3. Teraz możesz _Run All_ aby wykonać notatnik.
- Aby uruchomić aplikacje Python z linii poleceń, postępuj zgodnie z instrukcjami specyficznymi dla zadania, aby upewnić się, że wybierasz odpowiednie pliki i dostarczasz wymagane argumenty.

## 2. Konfiguracja dostawców

Zadania **mogą** również być skonfigurowane do pracy z jednym lub więcej wdrożeń dużych modeli językowych (LLM) poprzez obsługiwanego dostawcę usług, takiego jak OpenAI, Azure lub Hugging Face. Zapewniają one _hostowany punkt końcowy_ (API), do którego możemy uzyskać dostęp programowo z odpowiednimi poświadczeniami (klucz API lub token). W tym kursie omawiamy tych dostawców:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) z różnorodnymi modelami, w tym główną serią GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) dla modeli OpenAI z naciskiem na gotowość dla przedsiębiorstw.
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) dla modeli open-source i serwera inferencyjnego.

**Będziesz musiał użyć własnych kont do tych ćwiczeń**. Zadania są opcjonalne, więc możesz zdecydować się na konfigurację jednego, wszystkich - lub żadnego - z dostawców w zależności od swoich zainteresowań. Kilka wskazówek dotyczących rejestracji:

| Rejestracja | Koszt | Klucz API | Plac zabaw | Uwagi |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Cennik](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Na podstawie projektu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Bez kodu, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Dostępne wiele modeli |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Cennik](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Musisz wcześniej aplikować o dostęp](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cennik](https://huggingface.co/pricing) | [Tokeny dostępu](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ma ograniczone modele](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Postępuj zgodnie z poniższymi instrukcjami, aby _skonfigurować_ to repozytorium do użycia z różnymi dostawcami. Zadania, które wymagają konkretnego dostawcy, będą zawierały jeden z tych tagów w nazwie pliku:
 - `aoai` - wymaga punktu końcowego Azure OpenAI, klucza
 - `oai` - wymaga punktu końcowego OpenAI, klucza
 - `hf` - wymaga tokenu Hugging Face

Możesz skonfigurować jednego, żadnego lub wszystkich dostawców. Powiązane zadania po prostu zakończą się błędem przy braku poświadczeń.

### 2.1. Utwórz plik `.env`

Zakładamy, że przeczytałeś już powyższe wskazówki, zarejestrowałeś się u odpowiedniego dostawcy i uzyskałeś wymagane poświadczenia uwierzytelniające (API_KEY lub token). W przypadku Azure OpenAI, zakładamy również, że masz ważne wdrożenie usługi Azure OpenAI (punkt końcowy) z co najmniej jednym modelem GPT wdrożonym do uzupełniania czatu.

Następnym krokiem jest skonfigurowanie **lokalnych zmiennych środowiskowych** w następujący sposób:

1. Poszukaj w głównym folderze pliku `.env.copy`, który powinien mieć zawartość podobną do tej:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Skopiuj ten plik do `.env` używając poniższego polecenia. Ten plik jest _gitignore-d_, co zapewnia bezpieczeństwo sekretów.

   ```bash
   cp .env.copy .env
   ```

3. Wypełnij wartości (zastąpiaj symbole zastępcze po prawej stronie `=`) zgodnie z opisem w następnej sekcji.

3. (Opcja) Jeśli używasz GitHub Codespaces, masz możliwość zapisania zmiennych środowiskowych jako _sekrety Codespaces_ związane z tym repozytorium. W takim przypadku nie będziesz musiał konfigurować lokalnego pliku .env. **Jednakże, pamiętaj, że ta opcja działa tylko wtedy, gdy używasz GitHub Codespaces.** Nadal będziesz musiał skonfigurować plik .env, jeśli używasz Docker Desktop.

### 2.2. Wypełnij plik `.env`

Przyjrzyjmy się szybko nazwom zmiennych, aby zrozumieć, co reprezentują:

| Zmienna  | Opis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | To jest token dostępu użytkownika, który skonfigurowałeś w swoim profilu |
| OPENAI_API_KEY | To jest klucz autoryzacyjny do korzystania z usługi dla punktów końcowych OpenAI, które nie są Azure |
| AZURE_OPENAI_API_KEY | To jest klucz autoryzacyjny do korzystania z tej usługi |
| AZURE_OPENAI_ENDPOINT | To jest wdrożony punkt końcowy dla zasobu Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | To jest punkt końcowy wdrożenia modelu _generacji tekstu_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | To jest punkt końcowy wdrożenia modelu _osadzania tekstu_ |
| | |

Uwaga: Ostatnie dwie zmienne Azure OpenAI odzwierciedlają domyślny model dla uzupełniania czatu (generacji tekstu) i wyszukiwania wektorowego (osadzania) odpowiednio. Instrukcje dotyczące ich ustawienia będą zdefiniowane w odpowiednich zadaniach.

### 2.3 Konfiguracja Azure: Z portalu

Wartości punktu końcowego i klucza Azure OpenAI znajdziesz w [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), więc zacznijmy od tego.

1. Przejdź do [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kliknij opcję **Keys and Endpoint** w pasku bocznym (menu po lewej).
1. Kliknij **Show Keys** - powinieneś zobaczyć następujące: KEY 1, KEY 2 i Endpoint.
1. Użyj wartości KEY 1 dla AZURE_OPENAI_API_KEY
1. Użyj wartości Endpoint dla AZURE_OPENAI_ENDPOINT

Następnie potrzebujemy punktów końcowych dla konkretnych modeli, które wdrożyliśmy.

1. Kliknij opcję **Model deployments** w pasku bocznym (menu po lewej) dla zasobu Azure OpenAI.
1. Na stronie docelowej kliknij **Manage Deployments**

To przeniesie Cię do strony internetowej Azure OpenAI Studio, gdzie znajdziemy pozostałe wartości zgodnie z opisem poniżej.

### 2.4 Konfiguracja Azure: Z Studio

1. Przejdź do [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **z Twojego zasobu** zgodnie z powyższym opisem.
1. Kliknij kartę **Deployments** (pasek boczny, lewo), aby zobaczyć aktualnie wdrożone modele.
1. Jeśli Twój pożądany model nie jest wdrożony, użyj **Create new deployment** aby go wdrożyć.
1. Będziesz potrzebował modelu _generacji tekstu_ - polecamy: **gpt-35-turbo**
1. Będziesz potrzebował modelu _osadzania tekstu_ - polecamy **text-embedding-ada-002**

Teraz zaktualizuj zmienne środowiskowe, aby odzwierciedlały _nazwę wdrożenia_ używaną. Zazwyczaj będzie to to samo co nazwa modelu, chyba że zmieniłeś ją wyraźnie. Tak więc, na przykład, możesz mieć:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Nie zapomnij zapisać pliku .env po zakończeniu**. Teraz możesz wyjść z pliku i wrócić do instrukcji dotyczących uruchamiania notatnika.

### 2.5 Konfiguracja OpenAI: Z profilu

Twój klucz API OpenAI można znaleźć na Twoim [koncie OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jeśli go nie masz, możesz zarejestrować się na konto i utworzyć klucz API. Po uzyskaniu klucza możesz użyć go do wypełnienia zmiennej `OPENAI_API_KEY` w pliku `.env`.

### 2.6 Konfiguracja Hugging Face: Z profilu

Twój token Hugging Face można znaleźć w Twoim profilu w sekcji [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nie publikuj ani nie udostępniaj ich publicznie. Zamiast tego utwórz nowy token do użycia w tym projekcie i skopiuj go do pliku `.env` pod zmienną `HUGGING_FACE_API_KEY`. _Uwaga:_ Technicznie rzecz biorąc, nie jest to klucz API, ale jest używany do uwierzytelniania, więc zachowujemy tę konwencję nazewnictwa dla spójności.

**Zrzeczenie się odpowiedzialności**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się o dokładność, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku ojczystym powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zaleca się profesjonalne tłumaczenie przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.