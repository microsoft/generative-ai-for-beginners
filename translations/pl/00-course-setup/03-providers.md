# Wybór i Konfiguracja Dostawcy LLM 🔑

Zadania **mogą** być również skonfigurowane tak, aby działać z jednym lub więcej wdrożeniami dużych modeli językowych (LLM) za pośrednictwem obsługiwanego dostawcy usług, takiego jak OpenAI, Azure lub Hugging Face. Dostarczają one _hostowany endpoint_ (API), do którego można programowo uzyskać dostęp za pomocą odpowiednich poświadczeń (klucz API lub token). W tym kursie omawiamy następujących dostawców:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) z różnorodnymi modelami, w tym główną serię GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) dla modeli OpenAI z naciskiem na gotowość korporacyjną
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) dla pojedynczego endpointu i klucza API, umożliwiającego dostęp do setek modeli OpenAI, Meta, Mistral, Cohere, Microsoft i innych (zastępuje GitHub Models, które zostanie wycofane pod koniec lipca 2026 r.)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) dla modeli open-source i serwera inferencji
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) lub [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst), jeśli wolisz uruchamiać modele całkowicie offline na własnym urządzeniu, bez konieczności posiadania subskrypcji w chmurze

**Do tych ćwiczeń będziesz potrzebować własnych kont**. Zadania są opcjonalne, więc możesz zdecydować się na konfigurację jednego, wszystkich lub żadnego z dostawców, w zależności od zainteresowań. Kilka wskazówek dotyczących rejestracji:

| Rejestracja | Koszt | Klucz API | Playground | Komentarze |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Cennik](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Na bazie projektu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Bez kodu, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Dostępnych wiele modeli |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Cennik](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Szybki start SDK](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Szybki start Studio](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Wymagany wcześniejszy wniosek o dostęp](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Cennik](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Strona przeglądu projektu](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Dostępna darmowa warstwa; jeden endpoint + klucz dla wielu dostawców modeli |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cennik](https://huggingface.co/pricing) | [Tokeny dostępu](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ma ograniczoną liczbę modeli](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Za darmo (działa na twoim urządzeniu) | Nie wymagany | [Lokalne CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Całkowicie offline, endpoint kompatybilny z OpenAI |
| | | | | |

Postępuj zgodnie z poniższymi instrukcjami, aby _skonfigurować_ to repozytorium do używania z różnymi dostawcami. Zadania wymagające konkretnego dostawcy będą zawierać jedną z tych etykiet w nazwie pliku:

- `aoai` - wymaga endpointu i klucza Azure OpenAI
- `oai` - wymaga endpointu i klucza OpenAI
- `hf` - wymaga tokena Hugging Face
- `githubmodels` - wymaga endpointu i klucza Microsoft Foundry Models (GitHub Models zostanie wycofany pod koniec lipca 2026 r.)

Możesz skonfigurować jednego, żadnego lub wszystkich dostawców. Powiązane zadania po prostu zgłoszą błąd w przypadku brakujących poświadczeń.

## Utwórz plik `.env`

Zakładamy, że zapoznałeś się już z powyższymi wskazówkami i zarejestrowałeś się u odpowiedniego dostawcy, uzyskując wymagane dane uwierzytelniające (API_KEY lub token). W przypadku Azure OpenAI zakładamy również, że masz ważne wdrożenie usługi Azure OpenAI (endpoint) z co najmniej jednym modelem GPT wdrożonym do uzupełniania rozmów.

Następnym krokiem jest skonfigurowanie **lokalnych zmiennych środowiskowych** w następujący sposób:

1. Poszukaj w folderze głównym pliku `.env.copy`, który powinien zawierać coś takiego:

   ```bash
   # Dostawca OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI w Microsoft Foundry
   ## (Usługa Azure OpenAI jest teraz częścią Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Domyślne ustawienie! (aktualna stabilna wersja GA API)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Modele Microsoft Foundry (katalog modeli wielu dostawców, zastępuje modele GitHub, które zostaną wycofane pod koniec lipca 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Skopiuj ten plik jako `.env` przy pomocy poniższego polecenia. Ten plik jest _ignorowany przez git_, co chroni tajne dane.

   ```bash
   cp .env.copy .env
   ```

3. Uzupełnij wartości (zamień symbole zastępcze po prawej stronie znaku `=`) zgodnie z opisem w następnej sekcji.

4. (Opcja) Jeśli korzystasz z GitHub Codespaces, masz możliwość zapisania zmiennych środowiskowych jako _sekretów Codespaces_ powiązanych z tym repozytorium. W takim przypadku nie musisz konfigurować lokalnego pliku .env. **Zauważ jednak, że ta opcja działa tylko, jeśli używasz GitHub Codespaces.** Nadal będziesz musiał skonfigurować plik .env, jeśli korzystasz z Docker Desktop.

## Wypełnij plik `.env`

Rzućmy szybkie spojrzenie na nazwy zmiennych, aby zrozumieć, co reprezentują:

| Zmienna  | Opis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | To jest token dostępu użytkownika, który ustawiasz w swoim profilu |
| OPENAI_API_KEY | To jest klucz autoryzacyjny do korzystania z usługi dla endpointów OpenAI niezwiązanych z Azure |
| AZURE_OPENAI_API_KEY | To jest klucz autoryzacyjny dla tej usługi |
| AZURE_OPENAI_ENDPOINT | To jest wdrożony endpoint zasobu Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | To jest endpoint wdrożenia modelu _generowania tekstu_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | To jest endpoint wdrożenia modelu _osadzania tekstu_ |
| AZURE_INFERENCE_ENDPOINT | To jest endpoint twojego projektu Microsoft Foundry, używany dla modeli Microsoft Foundry |
| AZURE_INFERENCE_CREDENTIAL | To jest klucz API twojego projektu Microsoft Foundry |
| | |

Uwaga: Ostatnie dwie zmienne Azure OpenAI odpowiadają domyślnemu modelowi do uzupełniania rozmów (generowanie tekstu) i wyszukiwania wektorowego (embeddingi) odpowiednio. Instrukcje ich ustawienia zostaną określone w odpowiednich zadaniach.

## Konfiguracja Azure OpenAI: z Portalu

> **Uwaga:** Usługa Azure OpenAI jest obecnie częścią [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Zasoby i wdrożenia nadal widoczne są w Azure Portal, ale codzienne zarządzanie modelami (wdrożenia, playground, monitoring) odbywa się teraz w portalu Foundry, zamiast starego samodzielnego "Azure OpenAI Studio".

Wartości punktu końcowego Azure OpenAI i klucza znajdziesz w [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), więc zacznijmy stamtąd.

1. Przejdź do [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kliknij opcję **Klucze i Endpoint** w pasku bocznym (menu po lewej).
1. Kliknij **Pokaż klucze** - powinieneś zobaczyć: KLUCZ 1, KLUCZ 2 oraz Endpoint.
1. Użyj wartości KLUCZA 1 dla AZURE_OPENAI_API_KEY
1. Użyj wartości Endpoint dla AZURE_OPENAI_ENDPOINT

Następnie potrzebujemy endpointów dla konkretnych wdrożonych modeli.

1. Kliknij opcję **Wdrożenia modeli** w pasku bocznym (menu po lewej) dla zasobu Azure OpenAI.
1. Na stronie docelowej kliknij **Przejdź do portalu Microsoft Foundry** (lub **Zarządzaj wdrożeniami**, w zależności od typu zasobu)

Przeniesie Cię to do portalu Microsoft Foundry, gdzie znajdziemy pozostałe wartości, jak opisano poniżej.

## Konfiguracja Azure OpenAI: z portalu Microsoft Foundry

1. Przejdź do [portalu Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **z twojego zasobu** jak opisano powyżej.
1. Kliknij zakładkę **Wdrożenia** (pasek boczny, po lewej), aby zobaczyć aktualnie wdrożone modele.
1. Jeśli wybrany model nie jest wdrożony, użyj **Wdróż model**, aby go wdrożyć z [katalogu modeli](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Będziesz potrzebować modelu _generowania tekstu_ – zalecamy: **gpt-5-mini**
1. Będziesz potrzebować modelu _osadzania tekstu_ – zalecamy **text-embedding-3-small**

Teraz zaktualizuj zmienne środowiskowe, aby odzwierciedlały _nazwę wdrożenia_ używaną. Zazwyczaj jest to ta sama nazwa co model, chyba że zmieniłeś ją jawnie. Na przykład możesz mieć:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Nie zapomnij zapisać pliku .env po zakończeniu**. Możesz teraz zamknąć plik i wrócić do instrukcji uruchomienia notatnika.

## Konfiguracja OpenAI: z Profilu

Klucz API OpenAI znajdziesz w swoim [koncie OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jeśli go nie masz, możesz założyć konto i utworzyć klucz API. Po uzyskaniu klucza możesz go wykorzystać do uzupełnienia zmiennej `OPENAI_API_KEY` w pliku `.env`.

## Konfiguracja Hugging Face: z Profilu

Token Hugging Face znajdziesz w swoim profilu pod [Tokenami dostępu](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nie publikuj go ani nie udostępniaj publicznie. Zamiast tego utwórz nowy token do wykorzystania w tym projekcie i skopiuj go do pliku `.env` w zmiennej `HUGGING_FACE_API_KEY`. _Uwaga:_ technicznie nie jest to klucz API, ale jest używany do uwierzytelniania, więc zachowujemy tę konwencję nazewnictwa dla spójności.

## Konfiguracja Microsoft Foundry Models: z Portalu

> **Uwaga:** GitHub Models zostanie wycofany pod koniec lipca 2026 r. Microsoft Foundry Models to jego bezpośredni następca, oferujący ten sam darmowy katalog modeli do testów i doświadczenie z Azure AI Inference SDK / OpenAI SDK.

1. Przejdź do [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) i utwórz (lub otwórz) projekt Foundry.
1. Przeglądaj [katalog modeli](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) i wdroż model, na przykład `gpt-5-mini`.
1. Na stronie **Przegląd** projektu skopiuj **endpoint** i **klucz API**.
1. Użyj wartości endpoint dla `AZURE_INFERENCE_ENDPOINT` oraz wartości klucza dla `AZURE_INFERENCE_CREDENTIAL` w swoim pliku `.env`.

## Dostawcy offline / lokalni

Jeśli wolisz w ogóle nie korzystać z subskrypcji w chmurze, możesz uruchamiać kompatybilne modele otwarte bezpośrednio na własnym urządzeniu:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - środowisko uruchomieniowe Microsoft na urządzeniu. Automatycznie wybiera najlepszy dostawca wykonania (NPU, GPU lub CPU) i udostępnia endpoint kompatybilny z OpenAI, więc możesz używać większości przykładowego kodu z tego kursu z minimalnymi zmianami. Zobacz [dokumentację Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst), aby zacząć, lub zainstaluj poleceniem `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - popularna alternatywa do lokalnego uruchamiania otwartych modeli takich jak Llama, Phi, Mistral oraz Gemma.


Zobacz [Lekcja 19: Budowanie za pomocą SLM](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) dla praktycznych przykładów wykorzystujących obie opcje.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->