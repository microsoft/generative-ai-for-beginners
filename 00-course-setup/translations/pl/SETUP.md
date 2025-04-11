# Konfiguracja Środowiska Deweloperskiego

Skonfigurowaliśmy to repozytorium i kurs z [kontenerem deweloperskim](https://containers.dev?WT.mc_id=academic-105485-koreyst), który posiada środowisko uniwersalne wspierające rozwój w Python3, .NET, Node.js i Java. Powiązana konfiguracja jest zdefiniowana w pliku `devcontainer.json` znajdującym się w folderze `.devcontainer/` w głównym katalogu tego repozytorium.

Aby aktywować kontener deweloperski, uruchom go w [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (dla środowiska hostowanego w chmurze) lub w [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (dla środowiska hostowanego lokalnie na urządzeniu). Przeczytaj [tę dokumentację](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst), aby uzyskać więcej szczegółów na temat działania kontenerów deweloperskich w VS Code.

> [!PORADA]
> Zalecamy korzystanie z GitHub Codespaces, aby szybko rozpocząć pracę przy minimalnym wysiłku. Zapewnia hojny [darmowy limit użycia](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) dla kont osobistych. Skonfiguruj [limity czasowe](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst), aby zatrzymać lub usunąć nieaktywne przestrzenie kodu i zmaksymalizować wykorzystanie limitu.

## 1. Wykonywanie Zadań

Każda lekcja będzie zawierać _opcjonalne_ zadania, które mogą być dostarczone w jednym lub kilku językach programowania, w tym: Python, .NET/C#, Java i JavaScript/TypeScript. Ta sekcja zawiera ogólne wskazówki dotyczące wykonywania tych zadań.

### 1.1 Zadania w Pythonie

Zadania w Pythonie są dostarczane jako aplikacje (pliki `.py`) lub notebooki Jupyter (pliki `.ipynb`).

- Aby uruchomić notebook, otwórz go w Visual Studio Code, a następnie kliknij _Wybierz Kernel_ (w prawym górnym rogu) i wybierz domyślną opcję Python 3. Teraz możesz wybrać _Uruchom Wszystko_, aby wykonać notebook.
- Aby uruchomić aplikacje Python z linii poleceń, postępuj zgodnie z instrukcjami specyficznymi dla danego zadania, aby upewnić się, że wybierasz odpowiednie pliki i podajesz wymagane argumenty.

## 2. Konfiguracja Dostawców

Zadania **mogą** być również skonfigurowane do pracy z jednym lub wieloma wdrożeniami Large Language Model (LLM) za pośrednictwem wspieranego dostawcy usług, takiego jak OpenAI, Azure lub Hugging Face. Zapewniają one _hostowany punkt końcowy_ (API), do którego możemy uzyskać dostęp programistycznie przy użyciu odpowiednich poświadczeń (klucza API lub tokenu). W tym kursie omawiamy następujących dostawców:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) z różnorodnymi modelami, w tym podstawową serią GPT.
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) dla modeli OpenAI z naciskiem na gotowość dla przedsiębiorstw
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) dla modeli open-source i serwera wnioskowania

**Będziesz musiał użyć własnych kont dla tych ćwiczeń**. Zadania są opcjonalne, więc możesz wybrać konfigurację jednego, wszystkich - lub żadnego - dostawców w zależności od twoich zainteresowań. Niektóre wskazówki dotyczące rejestracji:

| Rejestracja                                                                   | Koszt                                                                                                                     | Klucz API                                                                                                            | Plac zabaw                                                                                                              | Komentarze                                                                                                                               |
| :---------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [Cennik](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)                                     | [Oparty na projekcie](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst)                         | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst)                                 | Dostępne wiele modeli                                                                                                                    |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)           | [Cennik](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [Szybki start SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Szybki start Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Musisz złożyć wniosek o dostęp z wyprzedzeniem](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst)  | [Cennik](https://huggingface.co/pricing)                                                                                  | [Tokeny dostępu](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst)                   | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)                                           | [Hugging Chat ma ograniczoną liczbę modeli](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst)                         |
|                                                                               |                                                                                                                           |                                                                                                                      |                                                                                                                         |                                                                                                                                          |

Postępuj zgodnie z poniższymi instrukcjami, aby _skonfigurować_ to repozytorium do użytku z różnymi dostawcami. Zadania, które wymagają konkretnego dostawcy, będą zawierać jeden z tych znaczników w nazwie pliku:

- `aoai` - wymaga punktu końcowego Azure OpenAI, klucza
- `oai` - wymaga punktu końcowego OpenAI, klucza
- `hf` - wymaga tokenu Hugging Face

Możesz skonfigurować jednego, żadnego lub wszystkich dostawców. Powiązane zadania po prostu zgłoszą błąd w przypadku braku poświadczeń.

### 2.1. Utworzenie pliku `.env`

Zakładamy, że już przeczytałeś powyższe wskazówki i zarejestrowałeś się u odpowiedniego dostawcy oraz uzyskałeś wymagane dane uwierzytelniające (API_KEY lub token). W przypadku Azure OpenAI zakładamy, że masz również prawidłowe wdrożenie usługi Azure OpenAI (punkt końcowy) z co najmniej jednym modelem GPT wdrożonym do uzupełniania czatu.

Następnym krokiem jest skonfigurowanie **lokalnych zmiennych środowiskowych** w następujący sposób:

1. Poszukaj w głównym folderze pliku `.env.copy`, który powinien mieć zawartość podobną do tej:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<dodaj tutaj swój klucz API OpenAI>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Domyślnie ustawione!
   AZURE_OPENAI_API_KEY='<dodaj tutaj swój klucz AOAI>'
   AZURE_OPENAI_ENDPOINT='<dodaj tutaj punkt końcowy usługi AOIA>'
   AZURE_OPENAI_DEPLOYMENT='<dodaj tutaj nazwę modelu uzupełniania czatu>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<dodaj tutaj nazwę modelu embeddingów>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<dodaj tutaj swój API lub token HuggingFace>'
   ```

2. Skopiuj ten plik do `.env` używając poniższego polecenia. Ten plik jest _ignorowany przez git_, co zapewnia bezpieczeństwo tajnych danych.

   ```bash
   cp .env.copy .env
   ```

3. Wypełnij wartości (zastąp elementy zastępcze po prawej stronie `=`) zgodnie z opisem w następnej sekcji.

4. (Opcja) Jeśli korzystasz z GitHub Codespaces, masz możliwość zapisania zmiennych środowiskowych jako _sekrety Codespaces_ powiązane z tym repozytorium. W tym przypadku nie będziesz musiał konfigurować lokalnego pliku .env. **Jednak pamiętaj, że ta opcja działa tylko wtedy, gdy korzystasz z GitHub Codespaces.** Nadal będziesz musiał skonfigurować plik .env, jeśli zamiast tego używasz Docker Desktop.

### 2.2. Wypełnianie pliku `.env`

Przyjrzyjmy się nazwom zmiennych, aby zrozumieć, co reprezentują:

| Zmienna                            | Opis                                                                                              |
| :--------------------------------- | :------------------------------------------------------------------------------------------------ |
| HUGGING_FACE_API_KEY               | To jest token dostępu użytkownika, który konfigurujesz w swoim profilu                            |
| OPENAI_API_KEY                     | To jest klucz autoryzacyjny do korzystania z usługi dla punktów końcowych OpenAI innych niż Azure |
| AZURE_OPENAI_API_KEY               | To jest klucz autoryzacyjny do korzystania z tej usługi                                           |
| AZURE_OPENAI_ENDPOINT              | To jest wdrożony punkt końcowy dla zasobu Azure OpenAI                                            |
| AZURE_OPENAI_DEPLOYMENT            | To jest punkt końcowy wdrożenia modelu _generowania tekstu_                                       |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | To jest punkt końcowy wdrożenia modelu _embeddingów tekstu_                                       |
|                                    |                                                                                                   |

Uwaga: Ostatnie dwie zmienne Azure OpenAI odzwierciedlają domyślny model dla uzupełniania czatu (generowanie tekstu) i wyszukiwania wektorowego (embeddingi). Instrukcje dotyczące ich ustawienia będą zdefiniowane w odpowiednich zadaniach.

### 2.3 Konfiguracja Azure: Z Portalu

Wartości punktu końcowego i klucza Azure OpenAI można znaleźć w [Portalu Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), więc zacznijmy od tego.

1. Przejdź do [Portalu Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kliknij opcję **Klucze i punkt końcowy** w pasku bocznym (menu po lewej stronie).
1. Kliknij **Pokaż klucze** - powinieneś zobaczyć następujące informacje: KLUCZ 1, KLUCZ 2 i Punkt końcowy.
1. Użyj wartości KLUCZ 1 dla AZURE_OPENAI_API_KEY
1. Użyj wartości Punkt końcowy dla AZURE_OPENAI_ENDPOINT

Następnie potrzebujemy punktów końcowych dla konkretnych modeli, które wdrożyliśmy.

1. Kliknij opcję **Wdrożenia modeli** w pasku bocznym (menu po lewej) dla zasobu Azure OpenAI.
1. Na stronie docelowej kliknij **Zarządzaj wdrożeniami**

Przeniesie Cię to do witryny Azure OpenAI Studio, gdzie znajdziesz pozostałe wartości opisane poniżej.

### 2.4 Konfiguracja Azure: Ze Studio

1. Przejdź do [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **ze swojego zasobu**, jak opisano powyżej.
1. Kliknij zakładkę **Wdrożenia** (pasek boczny, po lewej), aby zobaczyć aktualnie wdrożone modele.
1. Jeśli twój pożądany model nie jest wdrożony, użyj **Utwórz nowe wdrożenie**, aby go wdrożyć.
1. Będziesz potrzebować modelu _generowania tekstu_ - zalecamy: **gpt-35-turbo**
1. Będziesz potrzebować modelu _embeddingów tekstu_ - zalecamy **text-embedding-ada-002**

Teraz zaktualizuj zmienne środowiskowe, aby odzwierciedlały użytą _nazwę wdrożenia_. Zazwyczaj będzie ona taka sama jak nazwa modelu, chyba że wyraźnie ją zmieniłeś. Więc, jako przykład, możesz mieć:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Nie zapomnij zapisać pliku .env po zakończeniu**. Możesz teraz wyjść z pliku i wrócić do instrukcji dotyczących uruchamiania notebooka.

### 2.5 Konfiguracja OpenAI: Z Profilu

Twój klucz API OpenAI można znaleźć na twoim [koncie OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jeśli go nie masz, możesz zarejestrować konto i utworzyć klucz API. Po uzyskaniu klucza możesz użyć go do wypełnienia zmiennej `OPENAI_API_KEY` w pliku `.env`.

### 2.6 Konfiguracja Hugging Face: Z Profilu

Twój token Hugging Face można znaleźć w twoim profilu w sekcji [Tokeny dostępu](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nie publikuj ani nie udostępniaj ich publicznie. Zamiast tego utwórz nowy token do użytku w tym projekcie i skopiuj go do pliku `.env` w zmiennej `HUGGING_FACE_API_KEY`. _Uwaga:_ Technicznie nie jest to klucz API, ale służy do uwierzytelniania, więc zachowujemy tę konwencję nazewnictwa dla spójności.
