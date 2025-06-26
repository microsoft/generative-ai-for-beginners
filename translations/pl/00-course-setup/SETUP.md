<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:17:51+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "pl"
}
-->
# Skonfiguruj swoje środowisko deweloperskie

Skonfigurowaliśmy to repozytorium i kurs z użyciem [kontenera deweloperskiego](https://containers.dev?WT.mc_id=academic-105485-koreyst), który ma uniwersalne środowisko wykonawcze wspierające rozwój w Python3, .NET, Node.js i Java. Odpowiednia konfiguracja jest zdefiniowana w pliku `devcontainer.json` znajdującym się w folderze `.devcontainer/` w głównym katalogu tego repozytorium.

Aby aktywować kontener deweloperski, uruchom go w [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (dla środowiska uruchamianego w chmurze) lub w [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (dla środowiska uruchamianego lokalnie na urządzeniu). Przeczytaj [tę dokumentację](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst), aby uzyskać więcej szczegółów na temat działania kontenerów deweloperskich w VS Code.

> [!TIP]  
> Zalecamy użycie GitHub Codespaces dla szybkiego startu przy minimalnym wysiłku. Oferuje on hojną [darmową kwotę użycia](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) dla kont osobistych. Skonfiguruj [limity czasowe](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst), aby zatrzymać lub usunąć nieaktywne przestrzenie kodu i maksymalnie wykorzystać swoją kwotę.

## 1. Wykonywanie zadań

Każda lekcja będzie zawierać _opcjonalne_ zadania, które mogą być dostarczone w jednym lub kilku językach programowania, w tym: Python, .NET/C#, Java i JavaScript/TypeScript. Ta sekcja zawiera ogólne wskazówki dotyczące wykonywania tych zadań.

### 1.1 Zadania w Pythonie

Zadania w Pythonie są dostarczane albo jako aplikacje (pliki `.py`) albo jako notatniki Jupyter (pliki `.ipynb`). 
- Aby uruchomić notatnik, otwórz go w Visual Studio Code, a następnie kliknij _Select Kernel_ (u góry po prawej) i wybierz domyślną opcję Python 3. Teraz możesz _Run All_, aby wykonać notatnik.
- Aby uruchomić aplikacje Pythona z wiersza poleceń, postępuj zgodnie z instrukcjami specyficznymi dla zadania, aby upewnić się, że wybierasz odpowiednie pliki i dostarczasz wymagane argumenty.

## 2. Konfiguracja dostawców

Zadania **mogą** być również skonfigurowane do pracy z jednym lub kilkoma wdrożeniami Large Language Model (LLM) za pośrednictwem wspieranego dostawcy usług, takiego jak OpenAI, Azure lub Hugging Face. Dostarczają one _hostowany punkt końcowy_ (API), do którego możemy uzyskać dostęp programowo z odpowiednimi poświadczeniami (klucz API lub token). W tym kursie omawiamy tych dostawców:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) z różnorodnymi modelami, w tym z serią GPT.
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) dla modeli OpenAI z naciskiem na gotowość korporacyjną
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) dla modeli open-source i serwera inferencyjnego

**Będziesz musiał użyć własnych kont do tych ćwiczeń**. Zadania są opcjonalne, więc możesz zdecydować się na skonfigurowanie jednego, wszystkich - lub żadnego - z dostawców w zależności od swoich zainteresowań. Kilka wskazówek dotyczących rejestracji:

| Rejestracja | Koszt | Klucz API | Playground | Komentarze |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Cennik](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Na podstawie projektu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Bez kodu, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Dostępne wiele modeli |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Cennik](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Wymagana wcześniejsza aplikacja](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cennik](https://huggingface.co/pricing) | [Tokeny dostępu](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ma ograniczone modele](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Postępuj zgodnie z poniższymi instrukcjami, aby _skonfigurować_ to repozytorium do użytku z różnymi dostawcami. Zadania wymagające konkretnego dostawcy będą zawierać jeden z tych tagów w swojej nazwie pliku:
 - `aoai` - wymaga Azure OpenAI endpoint, klucz
 - `oai` - wymaga OpenAI endpoint, klucz
 - `hf` - wymaga tokenu Hugging Face

Możesz skonfigurować jednego, żadnego lub wszystkich dostawców. Powiązane zadania po prostu zakończą się błędem w przypadku braku poświadczeń.

### 2.1. Utwórz plik `.env`

Zakładamy, że przeczytałeś już powyższe wskazówki i zarejestrowałeś się u odpowiedniego dostawcy oraz uzyskałeś wymagane poświadczenia uwierzytelniające (API_KEY lub token). W przypadku Azure OpenAI zakładamy, że masz również ważne wdrożenie usługi Azure OpenAI (endpoint) z co najmniej jednym modelem GPT wdrożonym do uzupełniania czatu.

Następnym krokiem jest skonfigurowanie **lokalnych zmiennych środowiskowych** w następujący sposób:

1. Poszukaj w głównym folderze pliku `.env.copy`, który powinien mieć zawartość taką jak ta:

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

2. Skopiuj ten plik do `.env`, używając poniższego polecenia. Ten plik jest _gitignore-d_, co utrzymuje tajemnice w bezpiecznym miejscu.

   ```bash
   cp .env.copy .env
   ```

3. Uzupełnij wartości (zastąpiaj miejsca na prawej stronie `=`) zgodnie z opisem w następnej sekcji.

3. (Opcjonalnie) Jeśli używasz GitHub Codespaces, masz możliwość zapisania zmiennych środowiskowych jako _tajemnic Codespaces_ powiązanych z tym repozytorium. W takim przypadku nie będziesz musiał konfigurować lokalnego pliku .env. **Jednak pamiętaj, że ta opcja działa tylko wtedy, gdy używasz GitHub Codespaces.** Nadal będziesz musiał skonfigurować plik .env, jeśli używasz Docker Desktop.

### 2.2. Uzupełnij plik `.env`

Przyjrzyjmy się szybko nazwom zmiennych, aby zrozumieć, co reprezentują:

| Zmienna  | Opis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | To jest token dostępu użytkownika, który ustawiasz w swoim profilu |
| OPENAI_API_KEY | To jest klucz autoryzacyjny do korzystania z usługi dla nie-Azure OpenAI endpoint |
| AZURE_OPENAI_API_KEY | To jest klucz autoryzacyjny do korzystania z tej usługi |
| AZURE_OPENAI_ENDPOINT | To jest wdrożony endpoint dla zasobu Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | To jest endpoint wdrożenia modelu _generowania tekstu_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | To jest endpoint wdrożenia modelu _embeddingów tekstowych_ |
| | |

Uwaga: Ostatnie dwie zmienne Azure OpenAI odzwierciedlają domyślny model do uzupełniania czatu (generowanie tekstu) i wyszukiwania wektorowego (embeddingi) odpowiednio. Instrukcje dotyczące ich ustawienia będą zdefiniowane w odpowiednich zadaniach.

### 2.3 Skonfiguruj Azure: Z Portalu

Wartości endpoint i klucza Azure OpenAI można znaleźć w [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), więc zacznijmy od tego.

1. Przejdź do [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kliknij opcję **Keys and Endpoint** w pasku bocznym (menu po lewej).
1. Kliknij **Show Keys** - powinieneś zobaczyć następujące: KEY 1, KEY 2 i Endpoint.
1. Użyj wartości KEY 1 dla AZURE_OPENAI_API_KEY
1. Użyj wartości Endpoint dla AZURE_OPENAI_ENDPOINT

Następnie potrzebujemy endpointów dla konkretnych modeli, które wdrożyliśmy.

1. Kliknij opcję **Model deployments** w pasku bocznym (menu po lewej) dla zasobu Azure OpenAI.
1. Na stronie docelowej kliknij **Manage Deployments**

To przeniesie cię na stronę Azure OpenAI Studio, gdzie znajdziemy inne wartości opisane poniżej.

### 2.4 Skonfiguruj Azure: Z Studio

1. Przejdź do [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **z twojego zasobu** jak opisano powyżej.
1. Kliknij kartę **Deployments** (pasek boczny, lewa strona), aby zobaczyć aktualnie wdrożone modele.
1. Jeśli twój wybrany model nie jest wdrożony, użyj **Create new deployment**, aby go wdrożyć.
1. Będziesz potrzebować modelu _generowania tekstu_ - polecamy: **gpt-35-turbo**
1. Będziesz potrzebować modelu _embeddingów tekstowych_ - polecamy **text-embedding-ada-002**

Teraz zaktualizuj zmienne środowiskowe, aby odzwierciedlały _Deployment name_ używane. Zazwyczaj będzie to to samo, co nazwa modelu, chyba że zmieniłeś ją wyraźnie. Tak więc, na przykład, możesz mieć:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Nie zapomnij zapisać pliku .env po zakończeniu**. Możesz teraz zamknąć plik i wrócić do instrukcji uruchamiania notatnika.

### 2.5 Skonfiguruj OpenAI: Z profilu

Twój klucz API OpenAI można znaleźć na twoim [koncie OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jeśli go nie masz, możesz założyć konto i utworzyć klucz API. Gdy już masz klucz, możesz go użyć do wypełnienia zmiennej `OPENAI_API_KEY` w pliku `.env`.

### 2.6 Skonfiguruj Hugging Face: Z profilu

Twój token Hugging Face można znaleźć w twoim profilu pod [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nie publikuj ani nie udostępniaj ich publicznie. Zamiast tego utwórz nowy token do użytku w tym projekcie i skopiuj go do pliku `.env` pod zmienną `HUGGING_FACE_API_KEY`. _Uwaga:_ Technicznie nie jest to klucz API, ale jest używany do uwierzytelniania, więc utrzymujemy tę konwencję nazewnictwa dla spójności.

**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się o dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku ojczystym powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zaleca się profesjonalne tłumaczenie przez człowieka. Nie ponosimy odpowiedzialności za wszelkie nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.