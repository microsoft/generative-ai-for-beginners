<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b5b016b0eb8a1cef2e3097620d8aa23",
  "translation_date": "2025-12-19T14:50:07+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "pl"
}
-->
# Wybór i konfiguracja dostawcy LLM 🔑

Zadania **mogą** być również skonfigurowane do pracy z jednym lub kilkoma wdrożeniami dużych modeli językowych (LLM) za pośrednictwem obsługiwanego dostawcy usług, takiego jak OpenAI, Azure lub Hugging Face. Zapewniają one _hostowany punkt końcowy_ (API), do którego możemy uzyskać dostęp programowo za pomocą odpowiednich poświadczeń (klucz API lub token). W tym kursie omawiamy następujących dostawców:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) z różnorodnymi modelami, w tym podstawową serię GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) dla modeli OpenAI z naciskiem na gotowość przedsiębiorstwa
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) dla modeli open-source i serwera inferencji

**Do tych ćwiczeń będziesz musiał użyć własnych kont**. Zadania są opcjonalne, więc możesz wybrać konfigurację jednego, wszystkich lub żadnego z dostawców w zależności od swoich zainteresowań. Kilka wskazówek dotyczących rejestracji:

| Rejestracja | Koszt | Klucz API | Playground | Komentarze |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Cennik](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Na podstawie projektu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Bez kodu, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Dostępne różne modele |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Cennik](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Szybki start SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Szybki start Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Wymaga wcześniejszego zgłoszenia](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cennik](https://huggingface.co/pricing) | [Tokeny dostępu](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ma ograniczoną liczbę modeli](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Postępuj zgodnie z poniższymi wskazówkami, aby _skonfigurować_ to repozytorium do pracy z różnymi dostawcami. Zadania wymagające konkretnego dostawcy będą zawierać jeden z tych tagów w nazwie pliku:

- `aoai` - wymaga punktu końcowego i klucza Azure OpenAI
- `oai` - wymaga punktu końcowego i klucza OpenAI
- `hf` - wymaga tokena Hugging Face

Możesz skonfigurować jednego, żadnego lub wszystkich dostawców. Zadania powiązane po prostu zgłoszą błąd, jeśli brakuje poświadczeń.

## Utwórz plik `.env`

Zakładamy, że przeczytałeś powyższe wskazówki, zarejestrowałeś się u odpowiedniego dostawcy i uzyskałeś wymagane poświadczenia uwierzytelniające (API_KEY lub token). W przypadku Azure OpenAI zakładamy również, że masz ważne wdrożenie usługi Azure OpenAI (punkt końcowy) z co najmniej jednym modelem GPT wdrożonym do uzupełniania czatu.

Następnym krokiem jest skonfigurowanie **lokalnych zmiennych środowiskowych** w następujący sposób:

1. Sprawdź w katalogu głównym plik `.env.copy`, który powinien zawierać coś takiego:

   ```bash
   # Dostawca OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Domyślne ustawienie!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Skopiuj ten plik do `.env` używając poniższego polecenia. Ten plik jest _gitignore-owany_, co chroni tajne dane.

   ```bash
   cp .env.copy .env
   ```

3. Wypełnij wartości (zamień symbole zastępcze po prawej stronie `=`) zgodnie z opisem w następnej sekcji.

4. (Opcjonalnie) Jeśli korzystasz z GitHub Codespaces, masz możliwość zapisania zmiennych środowiskowych jako _sekretów Codespaces_ powiązanych z tym repozytorium. W takim przypadku nie musisz tworzyć lokalnego pliku .env. **Jednak ta opcja działa tylko, jeśli używasz GitHub Codespaces.** Nadal będziesz musiał skonfigurować plik .env, jeśli używasz Docker Desktop.

## Wypełnij plik `.env`

Przyjrzyjmy się szybko nazwom zmiennych, aby zrozumieć, co reprezentują:

| Zmienna  | Opis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | To jest token dostępu użytkownika, który ustawiasz w swoim profilu |
| OPENAI_API_KEY | To jest klucz autoryzacyjny do korzystania z usługi dla punktów końcowych OpenAI niebędących Azure |
| AZURE_OPENAI_API_KEY | To jest klucz autoryzacyjny do korzystania z tej usługi |
| AZURE_OPENAI_ENDPOINT | To jest wdrożony punkt końcowy zasobu Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | To jest punkt końcowy wdrożenia modelu _generowania tekstu_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | To jest punkt końcowy wdrożenia modelu _osadzania tekstu_ |
| | |

Uwaga: Ostatnie dwie zmienne Azure OpenAI odpowiadają domyślnemu modelowi do uzupełniania czatu (generowanie tekstu) oraz wyszukiwania wektorowego (osadzania) odpowiednio. Instrukcje dotyczące ich ustawienia będą podane w odpowiednich zadaniach.

## Konfiguracja Azure: z portalu

Wartości punktu końcowego i klucza Azure OpenAI znajdziesz w [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), więc zacznijmy tam.

1. Przejdź do [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kliknij opcję **Klucze i punkt końcowy** w pasku bocznym (menu po lewej).
1. Kliknij **Pokaż klucze** - powinieneś zobaczyć: KLUCZ 1, KLUCZ 2 oraz Punkt końcowy.
1. Użyj wartości KLUCZ 1 dla AZURE_OPENAI_API_KEY
1. Użyj wartości Punkt końcowy dla AZURE_OPENAI_ENDPOINT

Następnie potrzebujemy punktów końcowych dla konkretnych wdrożonych modeli.

1. Kliknij opcję **Wdrożenia modeli** w pasku bocznym (menu po lewej) dla zasobu Azure OpenAI.
1. Na stronie docelowej kliknij **Zarządzaj wdrożeniami**

To przeniesie Cię do witryny Azure OpenAI Studio, gdzie znajdziemy pozostałe wartości, jak opisano poniżej.

## Konfiguracja Azure: ze Studio

1. Przejdź do [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **ze swojego zasobu**, jak opisano powyżej.
1. Kliknij kartę **Wdrożenia** (pasek boczny, po lewej), aby zobaczyć aktualnie wdrożone modele.
1. Jeśli żądany model nie jest wdrożony, użyj **Utwórz nowe wdrożenie**, aby go wdrożyć.
1. Będziesz potrzebować modelu _generowania tekstu_ - zalecamy: **gpt-35-turbo**
1. Będziesz potrzebować modelu _osadzania tekstu_ - zalecamy **text-embedding-ada-002**

Teraz zaktualizuj zmienne środowiskowe, aby odzwierciedlały używaną _nazwę wdrożenia_. Zazwyczaj będzie to ta sama nazwa co model, chyba że zmieniłeś ją jawnie. Na przykład możesz mieć:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Nie zapomnij zapisać pliku .env po zakończeniu**. Możesz teraz wyjść z pliku i wrócić do instrukcji uruchamiania notatnika.

## Konfiguracja OpenAI: z profilu

Twój klucz API OpenAI znajdziesz w swoim [koncie OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jeśli go nie masz, możesz zarejestrować się i utworzyć klucz API. Po uzyskaniu klucza możesz użyć go do wypełnienia zmiennej `OPENAI_API_KEY` w pliku `.env`.

## Konfiguracja Hugging Face: z profilu

Twój token Hugging Face znajdziesz w swoim profilu w sekcji [Tokeny dostępu](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nie publikuj ani nie udostępniaj ich publicznie. Zamiast tego utwórz nowy token do użytku w tym projekcie i skopiuj go do pliku `.env` pod zmienną `HUGGING_FACE_API_KEY`. _Uwaga:_ Technicznie nie jest to klucz API, ale służy do uwierzytelniania, więc zachowujemy tę konwencję nazewnictwa dla spójności.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło wiarygodne i autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->