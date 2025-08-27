<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T16:38:36+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "pl"
}
-->
# Wybór i konfiguracja dostawcy LLM 🔑

Zadania **mogą** być skonfigurowane do pracy z jednym lub kilkoma wdrożeniami Large Language Model (LLM) za pośrednictwem obsługiwanego dostawcy usług, takiego jak OpenAI, Azure czy Hugging Face. Dostawcy ci udostępniają _hostowany endpoint_ (API), do którego można uzyskać dostęp programowo, mając odpowiednie dane uwierzytelniające (klucz API lub token). W tym kursie omawiamy następujących dostawców:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) z różnorodnymi modelami, w tym serią GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) oferujący modele OpenAI z naciskiem na gotowość do zastosowań biznesowych
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) z otwartymi modelami i serwerem inferencyjnym

**Do tych ćwiczeń będziesz potrzebować własnych kont**. Zadania są opcjonalne, więc możesz wybrać konfigurację jednego, wszystkich lub żadnego z dostawców – zależnie od swoich zainteresowań. Kilka wskazówek dotyczących rejestracji:

| Rejestracja | Koszt | Klucz API | Playground | Komentarze |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Cennik](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Na projekt](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Bez kodu, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Dostępne różne modele |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Cennik](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Wymagana wcześniejsza aplikacja o dostęp](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cennik](https://huggingface.co/pricing) | [Tokeny dostępu](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat obsługuje ograniczoną liczbę modeli](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Postępuj zgodnie z poniższymi wskazówkami, aby _skonfigurować_ to repozytorium do pracy z wybranymi dostawcami. Zadania wymagające konkretnego dostawcy będą miały jeden z poniższych tagów w nazwie pliku:

- `aoai` - wymaga endpointu i klucza Azure OpenAI
- `oai` - wymaga endpointu i klucza OpenAI
- `hf` - wymaga tokenu Hugging Face

Możesz skonfigurować jednego, żadnego lub wszystkich dostawców. Powiązane zadania po prostu zgłoszą błąd, jeśli zabraknie danych uwierzytelniających.

## Utwórz plik `.env`

Zakładamy, że zapoznałeś się już z powyższymi wskazówkami, zarejestrowałeś się u wybranego dostawcy i uzyskałeś wymagane dane uwierzytelniające (API_KEY lub token). W przypadku Azure OpenAI zakładamy, że masz już wdrożoną usługę Azure OpenAI (endpoint) z przynajmniej jednym modelem GPT wdrożonym do generowania odpowiedzi w czacie.

Kolejnym krokiem jest skonfigurowanie **lokalnych zmiennych środowiskowych** w następujący sposób:

1. W folderze głównym znajdź plik `.env.copy`, który powinien wyglądać tak:

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

2. Skopiuj ten plik do `.env` za pomocą poniższego polecenia. Ten plik jest _gitignore-owany_, więc Twoje dane pozostają bezpieczne.

   ```bash
   cp .env.copy .env
   ```

3. Uzupełnij wartości (zastąp pola po prawej stronie `=`) zgodnie z opisem w kolejnej sekcji.

4. (Opcjonalnie) Jeśli korzystasz z GitHub Codespaces, możesz zapisać zmienne środowiskowe jako _sekrety Codespaces_ powiązane z tym repozytorium. W takim przypadku nie musisz tworzyć lokalnego pliku .env. **Pamiętaj jednak, że ta opcja działa tylko w GitHub Codespaces.** Jeśli korzystasz z Docker Desktop, nadal musisz skonfigurować plik .env.

## Uzupełnij plik `.env`

Przyjrzyjmy się szybko nazwom zmiennych, aby zrozumieć, co oznaczają:

| Zmienna  | Opis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Token dostępu użytkownika, który ustawiasz w swoim profilu |
| OPENAI_API_KEY | Klucz autoryzacyjny do korzystania z usługi dla endpointów innych niż Azure OpenAI |
| AZURE_OPENAI_API_KEY | Klucz autoryzacyjny do korzystania z tej usługi |
| AZURE_OPENAI_ENDPOINT | Endpoint wdrożonego zasobu Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Endpoint wdrożenia modelu _generowania tekstu_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Endpoint wdrożenia modelu _embeddings tekstowych_ |
| | |

Uwaga: Ostatnie dwie zmienne Azure OpenAI dotyczą domyślnego modelu do generowania odpowiedzi w czacie (generowanie tekstu) oraz wyszukiwania wektorowego (embeddings). Instrukcje ich ustawienia będą podane w odpowiednich zadaniach.

## Konfiguracja Azure: z Portalu

Wartości endpointu i klucza Azure OpenAI znajdziesz w [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), więc zacznijmy od tego.

1. Przejdź do [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kliknij opcję **Keys and Endpoint** w pasku bocznym (menu po lewej).
1. Kliknij **Show Keys** – powinieneś zobaczyć: KEY 1, KEY 2 oraz Endpoint.
1. Wartość KEY 1 wpisz jako AZURE_OPENAI_API_KEY
1. Wartość Endpoint wpisz jako AZURE_OPENAI_ENDPOINT

Następnie potrzebujemy endpointów dla konkretnych wdrożonych modeli.

1. Kliknij opcję **Model deployments** w pasku bocznym (menu po lewej) dla zasobu Azure OpenAI.
1. Na docelowej stronie kliknij **Manage Deployments**

Zostaniesz przekierowany do strony Azure OpenAI Studio, gdzie znajdziesz pozostałe wartości, jak opisano poniżej.

## Konfiguracja Azure: z Studio

1. Przejdź do [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **ze swojego zasobu**, jak opisano powyżej.
1. Kliknij zakładkę **Deployments** (pasek boczny po lewej), aby zobaczyć aktualnie wdrożone modele.
1. Jeśli wybrany model nie jest wdrożony, użyj **Create new deployment**, aby go wdrożyć.
1. Potrzebujesz modelu _generowania tekstu_ – polecamy: **gpt-35-turbo**
1. Potrzebujesz modelu _embeddings tekstowych_ – polecamy **text-embedding-ada-002**

Teraz zaktualizuj zmienne środowiskowe, wpisując _Deployment name_ użyty przy wdrożeniu. Zazwyczaj będzie on taki sam jak nazwa modelu, chyba że zmieniłeś ją ręcznie. Przykładowo możesz mieć:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Pamiętaj, aby zapisać plik .env po zakończeniu**. Teraz możesz zamknąć plik i wrócić do instrukcji uruchamiania notebooka.

## Konfiguracja OpenAI: z Profilu

Twój klucz API OpenAI znajdziesz na swoim [koncie OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jeśli go nie masz, załóż konto i utwórz klucz API. Gdy już go uzyskasz, wpisz go do zmiennej `OPENAI_API_KEY` w pliku `.env`.

## Konfiguracja Hugging Face: z Profilu

Twój token Hugging Face znajdziesz w swoim profilu w sekcji [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nie publikuj ani nie udostępniaj go publicznie. Zamiast tego utwórz nowy token na potrzeby tego projektu i skopiuj go do pliku `.env` w zmiennej `HUGGING_FACE_API_KEY`. _Uwaga:_ Technicznie rzecz biorąc, nie jest to klucz API, ale służy do uwierzytelniania, więc zachowujemy tę nazwę dla spójności.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było dokładne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego ojczystym języku powinien być traktowany jako źródło nadrzędne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnych usług tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za wszelkie nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.