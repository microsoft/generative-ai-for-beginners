# Wybór i konfiguracja dostawcy LLM 🔑

Zadania **mogą** także być skonfigurowane do pracy z jednym lub wieloma wdrożeniami dużych modeli językowych (LLM) poprzez obsługiwanego dostawcę usług, takiego jak OpenAI, Azure czy Hugging Face. Dostarczają one _hostowany endpoint_ (API), do którego możemy uzyskać programowy dostęp za pomocą odpowiednich poświadczeń (klucz API lub token). W tym kursie omawiamy następujących dostawców:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) z różnorodnymi modelami, w tym główną serią GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) dla modeli OpenAI z naciskiem na gotowość przedsiębiorstwa
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) dla jednego endpointu i klucza API do dostępu do setek modeli od OpenAI, Meta, Mistral, Cohere, Microsoft i innych (zastępuje GitHub Models, które są wycofywane pod koniec lipca 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) dla modeli open-source i serwera inferencyjnego
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) lub [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst), jeśli wolisz uruchamiać modele całkowicie offline na własnym urządzeniu, bez konieczności subskrypcji w chmurze

**Do tych ćwiczeń będziesz musiał użyć własnych kont**. Zadania są opcjonalne, więc możesz zdecydować, czy skonfigurujesz jednego, wszystkich - albo żadnego - z dostawców, w zależności od swoich zainteresowań. Kilka wskazówek dotyczących rejestracji:

| Rejestracja | Koszt | Klucz API | Playground | Komentarze |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Cennik](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Na podstawie projektu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Wiele dostępnych modeli |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Cennik](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Szybki start SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Szybki start Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Wymagana aplikacja o dostęp](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Cennik](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Strona przeglądu projektu](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Dostępna darmowa warstwa; jeden endpoint + klucz dla wielu dostawców modeli |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Cennik](https://huggingface.co/pricing) | [Tokenu dostępu](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ma ograniczoną liczbę modeli](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Darmowy (działa na twoim urządzeniu) | Nie wymagany | [Lokalny CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Całkowicie offline, endpoint kompatybilny z OpenAI |
| | | | | |

Postępuj zgodnie z instrukcjami poniżej, aby _skonfigurować_ to repozytorium do pracy z różnymi dostawcami. Zadania wymagające konkretnego dostawcy będą zawierać jeden z tych tagów w nazwie pliku:

- `aoai` - wymaga endpointu i klucza Azure OpenAI
- `oai` - wymaga endpointu i klucza OpenAI
- `hf` - wymaga tokenu Hugging Face
- `githubmodels` - wymaga endpointu i klucza Microsoft Foundry Models (GitHub Models zostanie wycofany pod koniec lipca 2026)

Możesz skonfigurować jednego, żadnego lub wszystkich dostawców. Zadania powiązane po prostu zgłoszą błąd przy braku odpowiednich poświadczeń.

## Utwórz plik `.env`

Zakładamy, że przeczytałeś już powyższe wskazówki i zarejestrowałeś się u odpowiedniego dostawcy oraz uzyskałeś wymagane poświadczenia uwierzytelniające (API_KEY lub token). W przypadku Azure OpenAI zakładamy także, że masz ważne wdrożenie usługi Azure OpenAI (endpoint) z co najmniej jednym modelem GPT wdrożonym do chat completion.

Następnym krokiem jest skonfigurowanie twoich **lokalnych zmiennych środowiskowych** w następujący sposób:

1. Sprawdź w folderze głównym plik `.env.copy`, który powinien zawierać coś takiego:

   ```bash
   # Dostawca OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI w Microsoft Foundry
   ## (Usługa Azure OpenAI jest teraz częścią Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Domyślnie ustawione! (aktualna stabilna wersja GA API)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Modele Microsoft Foundry (katalog modeli wielodostawczych, zastępuje modele GitHub, które zostaną wycofane pod koniec lipca 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Skopiuj ten plik do `.env` za pomocą poniższego polecenia. Ten plik jest _ignorowany przez git_, co chroni sekrety.

   ```bash
   cp .env.copy .env
   ```

3. Wypełnij wartości (zamień symbole zastępcze po prawej stronie `=`) zgodnie z opisem w następnej sekcji.

4. (Opcjonalnie) Jeśli korzystasz z GitHub Codespaces, masz opcję zapisania zmiennych środowiskowych jako _sekrety Codespaces_ powiązane z tym repozytorium. W takim przypadku nie musisz tworzyć lokalnego pliku .env. **Należy jednak pamiętać, że ta opcja działa tylko w przypadku używania GitHub Codespaces.** Wciąż będziesz musiał utworzyć plik .env, jeśli używasz Docker Desktop.

## Wypełnij plik `.env`

Przyjrzyjmy się szybko nazwom zmiennych, aby zrozumieć, co reprezentują:

| Zmienna  | Opis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | To jest token dostępu użytkownika, który skonfigurowałeś w swoim profilu |
| OPENAI_API_KEY | To jest klucz autoryzacyjny do korzystania z usługi dla endpointów niebędących Azure OpenAI |
| AZURE_OPENAI_API_KEY | To jest klucz autoryzacyjny do korzystania z tej usługi |
| AZURE_OPENAI_ENDPOINT | To jest endpoint wdrożony dla zasobu Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | To jest endpoint wdrożenia modelu _generowania tekstu_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | To jest endpoint wdrożenia modelu _osadzania tekstu_ |
| AZURE_INFERENCE_ENDPOINT | To jest endpoint twojego projektu Microsoft Foundry, używany dla Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | To jest klucz API twojego projektu Microsoft Foundry |
| | |

Uwaga: Ostatnie dwie zmienne Azure OpenAI odpowiadają domyślnemu modelowi do chat completion (generowanie tekstu) oraz do wektorowego wyszukiwania (osadzanie) odpowiednio. Instrukcje dotyczące ich konfiguracji będą opisane w odpowiednich zadaniach.

## Konfiguracja Azure OpenAI: z Portalu

> **Uwaga:** Usługa Azure OpenAI jest teraz częścią [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Zasoby i wdrożenia wciąż są widoczne w Azure Portal, ale codzienne zarządzanie modelami (wdrożenia, playground, monitorowanie) odbywa się teraz w portalu Foundry, zamiast w starej, samodzielnej aplikacji "Azure OpenAI Studio".

Wartości endpointu i klucza API Azure OpenAI znajdziesz w [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), więc zacznijmy tam.

1. Przejdź do [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kliknij opcję **Klucze i endpoint** w pasku bocznym (menu po lewej stronie).
1. Kliknij **Pokaż klucze** - powinieneś zobaczyć następujące: KLUCZ 1, KLUCZ 2 i Endpoint.
1. Użyj wartości KLUCZ 1 dla zmiennej AZURE_OPENAI_API_KEY
1. Użyj wartości Endpoint dla zmiennej AZURE_OPENAI_ENDPOINT

Następnie potrzebujemy endpointy dla konkretnych wdrożonych modeli.

1. Kliknij opcję **Model deployments** w pasku bocznym (menu po lewej) zasobu Azure OpenAI.
1. Na docelowej stronie kliknij **Przejdź do portalu Microsoft Foundry** (lub **Zarządzaj wdrożeniami**, w zależności od typu zasobu)

To przeniesie Cię do portalu Microsoft Foundry, gdzie znajdziemy pozostałe wartości, jak opisano poniżej.

## Konfiguracja Azure OpenAI: z portalu Microsoft Foundry

1. Przejdź do [portalu Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **ze swojego zasobu**, jak opisano powyżej.
1. Kliknij zakładkę **Deployments** (pasek boczny, po lewej), aby wyświetlić aktualnie wdrożone modele.
1. Jeśli wybrany model nie jest wdrożony, użyj opcji **Deploy model**, aby go wdrożyć z [katalogu modeli](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Będziesz potrzebować modelu _generowania tekstu_ - zalecamy: **gpt-4o-mini**
1. Będziesz potrzebować modelu _osadzania tekstu_ - zalecamy **text-embedding-3-small**

Teraz zaktualizuj zmienne środowiskowe, aby odzwierciedlały używaną nazwę _Wdrożenia_. Zazwyczaj będzie ona taka sama jak nazwa modelu, chyba że zmieniłeś ją jawnie. Na przykład możesz mieć:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Nie zapomnij zapisać pliku .env po zakończeniu**. Teraz możesz zamknąć plik i powrócić do instrukcji uruchamiania notatnika.

## Konfiguracja OpenAI: z profilu

Twój klucz API OpenAI znajdziesz w swoim [koncie OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jeśli go nie masz, możesz się zarejestrować i utworzyć klucz API. Gdy już będziesz mieć klucz, możesz użyć go do wypełnienia zmiennej `OPENAI_API_KEY` w pliku `.env`.

## Konfiguracja Hugging Face: z profilu

Twój token Hugging Face znajdziesz w swoim profilu w sekcji [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nie publikuj ani nie udostępniaj go publicznie. Zamiast tego utwórz nowy token na potrzeby tego projektu i skopiuj go do pliku `.env` pod zmienną `HUGGING_FACE_API_KEY`. _Uwaga:_ Technicznie nie jest to klucz API, ale jest używany do uwierzytelniania, więc zachowujemy tę konwencję nazewnictwa dla spójności.

## Konfiguracja Microsoft Foundry Models: z portalu

> **Uwaga:** GitHub Models zostanie wycofany pod koniec lipca 2026. Microsoft Foundry Models to bezpośredni zamiennik, oferujący ten sam darmowy katalog modeli oraz doświadczenie SDK Azure AI Inference / OpenAI SDK.

1. Wejdź na [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) i utwórz (lub otwórz) projekt Foundry.
1. Przeglądaj [katalog modeli](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) i wdroż model, na przykład `gpt-4o-mini`.
1. Na stronie **Overview** projektu skopiuj **endpoint** i **klucz API**.
1. Użyj wartości endpoint dla `AZURE_INFERENCE_ENDPOINT` oraz wartości klucza dla `AZURE_INFERENCE_CREDENTIAL` w swoim pliku `.env`.

## Dostawcy offline / lokalni

Jeśli wolisz w ogóle nie korzystać z subskrypcji w chmurze, możesz uruchamiać kompatybilne modele otwarte bezpośrednio na własnym urządzeniu:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - środowisko uruchomieniowe Microsoft na urządzeniu. Automatycznie wybiera najlepszy dostawca wykonania (NPU, GPU lub CPU) i udostępnia endpoint kompatybilny z OpenAI, więc możesz ponownie wykorzystać większość kodu przykładowego w tym kursie przy minimalnych zmianach. Zobacz [dokumentację Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) aby zacząć, lub zainstaluj za pomocą `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - popularna alternatywa do uruchamiania otwartych modeli takich jak Llama, Phi, Mistral i Gemma lokalnie.


Zobacz [Lekcję 19: Budowanie z użyciem SLM](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) dla praktycznych przykładów wykorzystujących obie opcje.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->