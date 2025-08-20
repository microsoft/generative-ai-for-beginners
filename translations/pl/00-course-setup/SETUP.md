<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:29:29+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "pl"
}
-->
# Skonfiguruj swoje środowisko deweloperskie

Ten repozytorium i kurs zostały przygotowane z użyciem [kontenera deweloperskiego](https://containers.dev?WT.mc_id=academic-105485-koreyst), który zawiera uniwersalne środowisko uruchomieniowe wspierające Python3, .NET, Node.js oraz Java. Odpowiednia konfiguracja znajduje się w pliku `devcontainer.json` w folderze `.devcontainer/` w katalogu głównym tego repozytorium.

Aby uruchomić kontener deweloperski, otwórz go w [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (środowisko w chmurze) lub w [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (środowisko lokalne). Szczegóły dotyczące działania kontenerów deweloperskich w VS Code znajdziesz w [tej dokumentacji](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst).  

> [!TIP]  
> Zalecamy korzystanie z GitHub Codespaces, aby szybko zacząć pracę przy minimalnym wysiłku. Dla kont osobistych dostępna jest hojną [darmowa pula zasobów](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst). Skonfiguruj [limit czasu](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst), aby zatrzymywać lub usuwać nieaktywne codespaces i maksymalnie wykorzystać dostępne zasoby.


## 1. Wykonywanie zadań

Każda lekcja może zawierać _opcjonalne_ zadania dostępne w jednym lub kilku językach programowania, takich jak: Python, .NET/C#, Java oraz JavaScript/TypeScript. W tej sekcji znajdziesz ogólne wskazówki dotyczące uruchamiania tych zadań.

### 1.1 Zadania w Pythonie

Zadania w Pythonie są dostarczane jako aplikacje (`.py`) lub notatniki Jupyter (`.ipynb`).  
- Aby uruchomić notatnik, otwórz go w Visual Studio Code, kliknij _Select Kernel_ (w prawym górnym rogu) i wybierz domyślną opcję Python 3. Następnie możesz wybrać _Run All_, aby wykonać cały notatnik.  
- Aby uruchomić aplikacje Python z linii poleceń, postępuj zgodnie z instrukcjami zawartymi w konkretnym zadaniu, aby wybrać odpowiednie pliki i podać wymagane argumenty.

## 2. Konfiguracja dostawców usług

Zadania **mogą** być również skonfigurowane do pracy z jednym lub kilkoma wdrożeniami dużych modeli językowych (LLM) za pośrednictwem obsługiwanych dostawców usług, takich jak OpenAI, Azure czy Hugging Face. Udostępniają oni _hostowany endpoint_ (API), do którego możemy uzyskać dostęp programowo, używając odpowiednich poświadczeń (klucz API lub token). W tym kursie omawiamy następujących dostawców:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) z różnorodnymi modelami, w tym podstawową serią GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) z modelem OpenAI przygotowanym do zastosowań korporacyjnych.
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) dla modeli open-source i serwera inferencyjnego.

**Do tych ćwiczeń będziesz potrzebować własnych kont**. Zadania są opcjonalne, więc możesz skonfigurować jednego, wszystkich lub żadnego z dostawców, w zależności od swoich zainteresowań. Kilka wskazówek dotyczących rejestracji:

| Rejestracja | Koszt | Klucz API | Playground | Komentarze |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [Cennik](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [Klucze projektowe](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Dostępne różne modele |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [Cennik](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [Szybki start SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Szybki start Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Wymaga wcześniejszej rejestracji](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cennik](https://huggingface.co/pricing) | [Tokeny dostępu](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Hugging Chat ma ograniczoną liczbę modeli](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Postępuj zgodnie z poniższymi wskazówkami, aby _skonfigurować_ to repozytorium do pracy z różnymi dostawcami. Zadania wymagające konkretnego dostawcy będą miały w nazwie pliku jeden z następujących tagów:
 - `aoai` - wymaga endpointu i klucza Azure OpenAI
 - `oai` - wymaga endpointu i klucza OpenAI
 - `hf` - wymaga tokena Hugging Face

Możesz skonfigurować jednego, żadnego lub wszystkich dostawców. Zadania powiązane z brakującymi poświadczeniami po prostu zwrócą błąd.

###  2.1. Utwórz plik `.env`

Zakładamy, że zapoznałeś się z powyższymi wskazówkami, zarejestrowałeś się u odpowiedniego dostawcy i uzyskałeś wymagane dane uwierzytelniające (API_KEY lub token). W przypadku Azure OpenAI zakładamy również, że masz aktywne wdrożenie usługi Azure OpenAI (endpoint) z co najmniej jednym modelem GPT do czatu.

Następny krok to skonfigurowanie **lokalnych zmiennych środowiskowych** w następujący sposób:


1. W katalogu głównym znajdź plik `.env.copy`, który powinien zawierać coś takiego:

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

2. Skopiuj ten plik do `.env` za pomocą poniższego polecenia. Ten plik jest _ignorowany przez git_, co chroni Twoje sekrety.

   ```bash
   cp .env.copy .env
   ```

3. Wypełnij wartości (zamień symbole zastępcze po prawej stronie znaku `=`) zgodnie z opisem w następnej sekcji.

3. (Opcjonalnie) Jeśli korzystasz z GitHub Codespaces, możesz zapisać zmienne środowiskowe jako _sekrety Codespaces_ powiązane z tym repozytorium. W takim przypadku nie musisz tworzyć lokalnego pliku .env. **Pamiętaj jednak, że ta opcja działa tylko w GitHub Codespaces.** Jeśli używasz Docker Desktop, nadal musisz skonfigurować plik .env.


### 2.2. Wypełnij plik `.env`

Przyjrzyjmy się nazwom zmiennych, aby zrozumieć, co oznaczają:

| Zmienna  | Opis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Token dostępu użytkownika, który ustawiasz w swoim profilu |
| OPENAI_API_KEY | Klucz autoryzacyjny do korzystania z usługi OpenAI (poza Azure OpenAI) |
| AZURE_OPENAI_API_KEY | Klucz autoryzacyjny do korzystania z usługi Azure OpenAI |
| AZURE_OPENAI_ENDPOINT | Endpoint wdrożonej usługi Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Endpoint wdrożenia modelu do _generowania tekstu_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Endpoint wdrożenia modelu do _osadzania tekstu_ |
| | |

Uwaga: Ostatnie dwie zmienne Azure OpenAI odpowiadają domyślnemu modelowi do czatu (generowanie tekstu) oraz do wyszukiwania wektorowego (osadzanie). Instrukcje dotyczące ich ustawienia znajdziesz w odpowiednich zadaniach.


### 2.3 Konfiguracja Azure: z poziomu portalu

Wartości endpointu i klucza Azure OpenAI znajdziesz w [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), więc zacznijmy tam.

1. Przejdź do [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kliknij opcję **Keys and Endpoint** w pasku bocznym (menu po lewej).
1. Kliknij **Show Keys** – powinieneś zobaczyć: KEY 1, KEY 2 oraz Endpoint.
1. Użyj wartości KEY 1 jako AZURE_OPENAI_API_KEY
1. Użyj wartości Endpoint jako AZURE_OPENAI_ENDPOINT

Następnie potrzebujemy endpointów dla konkretnych wdrożonych modeli.

1. Kliknij opcję **Model deployments** w pasku bocznym (menu po lewej) dla zasobu Azure OpenAI.
1. Na stronie docelowej kliknij **Manage Deployments**

Zostaniesz przeniesiony do witryny Azure OpenAI Studio, gdzie znajdziesz pozostałe wartości, jak opisano poniżej.

### 2.4 Konfiguracja Azure: z poziomu Studio

1. Przejdź do [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **z poziomu swojego zasobu**, jak opisano powyżej.
1. Kliknij zakładkę **Deployments** (pasek boczny, po lewej), aby zobaczyć aktualnie wdrożone modele.
1. Jeśli wybrany model nie jest wdrożony, użyj opcji **Create new deployment**, aby go wdrożyć.
1. Będziesz potrzebować modelu do _generowania tekstu_ – zalecamy: **gpt-35-turbo**
1. Będziesz potrzebować modelu do _osadzania tekstu_ – zalecamy **text-embedding-ada-002**

Teraz zaktualizuj zmienne środowiskowe, aby odzwierciedlały nazwę _Deployment name_ używaną w wdrożeniu. Zazwyczaj jest to ta sama nazwa co model, chyba że zmieniłeś ją ręcznie. Na przykład, możesz mieć:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Nie zapomnij zapisać pliku .env po zakończeniu**. Możesz teraz zamknąć plik i wrócić do instrukcji uruchamiania notatnika.

### 2.5 Konfiguracja OpenAI: z poziomu profilu

Klucz API OpenAI znajdziesz w swoim [koncie OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jeśli go nie masz, zarejestruj się i utwórz klucz API. Po uzyskaniu klucza wpisz go w zmienną `OPENAI_API_KEY` w pliku `.env`.

### 2.6 Konfiguracja Hugging Face: z poziomu profilu

Token Hugging Face znajdziesz w swoim profilu w sekcji [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nie udostępniaj go publicznie. Zamiast tego utwórz nowy token do użytku w tym projekcie i skopiuj go do pliku `.env` pod zmienną `HUGGING_FACE_API_KEY`. _Uwaga:_ Technicznie nie jest to klucz API, ale służy do uwierzytelniania, dlatego zachowujemy tę nazwę dla spójności.

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.