# Výběr a konfigurace poskytovatele LLM 🔑

Zadání **mohou** být také nastavena tak, aby fungovala s jedním nebo více nasazeními velkých jazykových modelů (LLM) prostřednictvím podporovaného poskytovatele služeb, jako jsou OpenAI, Azure nebo Hugging Face. Ti poskytují _hostovaný endpoint_ (API), ke kterému můžeme programově přistupovat s příslušnými přihlašovacími údaji (API klíč nebo token). V tomto kurzu se zabýváme těmito poskytovateli:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) s různorodými modely včetně hlavní řady GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) pro modely OpenAI s důrazem na připravenost pro podnikové použití
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) pro jeden endpoint a API klíč k přístupu ke stovkám modelů od OpenAI, Meta, Mistral, Cohere, Microsoft a dalších (nahrazuje GitHub Models, které budou ukončeny ke konci července 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) pro open-source modely a inference server
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) nebo [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst), pokud chcete modely provozovat zcela offline na vlastním zařízení bez nutnosti předplatného v cloudu

**Pro tato cvičení budete potřebovat vlastní účty**. Zadání jsou volitelná, takže si můžete vybrat nastavení jednoho, všech nebo žádného z poskytovatelů podle zájmu. Několik tipů pro registraci:

| Registrace | Cena | API klíč | Playground | Komentáře |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Ceník](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Na projekt](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Dostupné různé modely |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Ceník](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Rychlý start SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Rychlý start Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Přihlásit se předem pro přístup](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Ceník](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Stránka přehledu projektu](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Zdarma dostupná úroveň; jeden endpoint + klíč pro mnoho poskytovatelů modelů |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Ceník](https://huggingface.co/pricing) | [Přístupové tokeny](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat má omezený počet modelů](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Zdarma (běží na vašem zařízení) | Není potřeba | [Lokální CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Plně offline, endpoint kompatibilní s OpenAI |
| | | | | |

Postupujte podle pokynů níže, jak _konfigurovat_ toto repozitář pro použití s různými poskytovateli. Zadání, která vyžadují specifického poskytovatele, budou mít v názvu souboru některou z těchto značek:

- `aoai` - vyžaduje Azure OpenAI endpoint a klíč
- `oai` - vyžaduje OpenAI endpoint a klíč
- `hf` - vyžaduje Hugging Face token
- `githubmodels` - vyžaduje Microsoft Foundry Models endpoint a klíč (GitHub Models bude ukončeno ke konci července 2026)

Můžete nastavit jednoho, žádného nebo všechny poskytovatele. Příslušná zadání jednoduše skončí chybou při chybějících přihlašovacích údajích.

## Vytvoření souboru `.env`

Předpokládáme, že jste již přečetli výše uvedené pokyny, zaregistrovali se u příslušného poskytovatele a získali požadované autentizační údaje (API_KEY nebo token). V případě Azure OpenAI předpokládáme také platné nasazení služby Azure OpenAI (endpoint) s alespoň jedním GPT modelem nasazeným pro chatovací dokončování.

Dalším krokem je konfigurace vašich **místních proměnných prostředí** následovně:

1. V kořenové složce hledejte soubor `.env.copy`, který by měl obsahovat něco takového:

   ```bash
   # OpenAI Poskytovatel
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI v Microsoft Foundry
   ## (Azure OpenAI služba je nyní součástí Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Výchozí je nastaveno! (aktuální stabilní GA verze API)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry Modely (katalog modelů s více poskytovateli, nahrazuje GitHub Modely, které končí na konci července 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Zkopírujte tento soubor do `.env` pomocí následujícího příkazu. Tento soubor je _gitignore-ován_, aby byly tajné údaje v bezpečí.

   ```bash
   cp .env.copy .env
   ```

3. Vyplňte hodnoty (nahraďte zástupce napravo od `=`) podle popisu v další části.

4. (Volitelné) Pokud používáte GitHub Codespaces, můžete uložit proměnné prostředí jako _Codespaces secrets_ spojené s tímto repozitářem. V takovém případě nemusíte nastavovat lokální .env soubor. **Tato možnost ale funguje pouze při použití GitHub Codespaces.** Pokud používáte místo toho Docker Desktop, budete muset .env soubor nastavit.

## Vyplnění souboru `.env`

Rychle si projděme názvy proměnných, abychom pochopili, co představují:

| Proměnná  | Popis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Toto je uživatelský přístupový token, který nastavíte ve svém profilu |
| OPENAI_API_KEY | Toto je autorizační klíč pro použití služby mimo Azure OpenAI endpointy |
| AZURE_OPENAI_API_KEY | Toto je autorizační klíč pro použití této služby |
| AZURE_OPENAI_ENDPOINT | Toto je nasazený endpoint pro Azure OpenAI zdroj |
| AZURE_OPENAI_DEPLOYMENT | Toto je endpoint nasazení modelu pro _generování textu_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Toto je endpoint nasazení modelu pro _textová embeddingy_ |
| AZURE_INFERENCE_ENDPOINT | Toto je endpoint pro váš Microsoft Foundry projekt, používá se u Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Toto je API klíč pro váš Microsoft Foundry projekt |
| | |

Pozn.: Poslední dvě proměnné Azure OpenAI odrážejí výchozí model pro chatovací dokončování (generování textu) a vyhledávání vektoru (embeddingy). Pokyny pro jejich nastavení budou definovány v příslušných zadáních.

## Konfigurace Azure OpenAI: Z portálu

> **Poznámka:** Azure OpenAI Service je nyní součástí [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Zdroje a nasazení se stále zobrazují v Azure portálu, ale každodenní správa modelů (nasazení, playground, monitoring) nyní probíhá v Foundry portálu místo starého samostatného "Azure OpenAI Studio".

Hodnoty endpointu a klíče Azure OpenAI najdete na [Azure portálu](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), začněme tedy tam.

1. Přejděte na [Azure portál](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. V postranním panelu (levé menu) klikněte na možnost **Keys and Endpoint**.
1. Klikněte na **Show Keys** - měli byste vidět: KLÍČ 1, KLÍČ 2 a Endpoint.
1. Použijte hodnotu KLÍČ 1 jako AZURE_OPENAI_API_KEY
1. Použijte hodnotu Endpoint jako AZURE_OPENAI_ENDPOINT

Dále potřebujeme endpointy pro konkrétní nasazené modely.

1. Klikněte na možnost **Model deployments** v postranním panelu (levém menu) u Azure OpenAI zdroje.
1. Na cílové stránce klikněte na **Přejít do Microsoft Foundry portálu** (nebo **Spravovat nasazení**, v závislosti na typu zdroje)

To vás zavede do Microsoft Foundry portálu, kde najdeme ostatní hodnoty uvedené níže.

## Konfigurace Azure OpenAI: Z Microsoft Foundry portálu

1. Přejděte do [Microsoft Foundry portálu](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **z vašeho zdroje**, jak bylo popsáno výše.
1. Klikněte na záložku **Deployments** (postranní panel, vlevo) pro zobrazení aktuálně nasazených modelů.
1. Pokud požadovaný model není nasazen, použijte **Deploy model** pro nasazení z [katalogu modelů](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Potřebujete model pro _generování textu_ – doporučujeme: **gpt-4o-mini**
1. Potřebujete model pro _embeddingy textu_ – doporučujeme **text-embedding-3-small**

Nyní aktualizujte proměnné prostředí tak, aby odrážely _název nasazení_ používaný. Obvykle to bude stejné jako název modelu, pokud jste jej explicitně nezměnili. Například můžete mít:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Nezapomeňte po úpravách soubor .env uložit**. Nyní můžete zavřít soubor a vrátit se k pokynům pro spuštění notebooku.

## Konfigurace OpenAI: Z profilu

Váš OpenAI API klíč najdete ve svém [OpenAI účtu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Pokud ho nemáte, můžete si vytvořit účet a vytvořit API klíč. Jakmile máte klíč, můžete ho vložit do proměnné `OPENAI_API_KEY` v souboru `.env`.

## Konfigurace Hugging Face: Z profilu

Váš token Hugging Face najdete ve svém profilu pod [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nezveřejňujte ani nesdílejte ho veřejně. Místo toho vytvořte nový token pro použití v tomto projektu a vložte ho do souboru `.env` pod proměnnou `HUGGING_FACE_API_KEY`. _Poznámka:_ Technicky se nejedná o API klíč, ale používá se pro autentizaci, proto zachováváme toto pojmenování kvůli konzistenci.

## Konfigurace Microsoft Foundry Models: Z portálu

> **Poznámka:** GitHub Models bude ukončeno ke konci července 2026. Microsoft Foundry Models je přímou náhradou, která nabízí stejný katalog modelů zdarma k vyzkoušení a zkušenost SDK Azure AI Inference / OpenAI SDK.

1. Přejděte na [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) a vytvořte (nebo otevřete) Foundry projekt.
1. Prohlédněte si [katalog modelů](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) a nasaďte model, například `gpt-4o-mini`.
1. Na stránce **Overview** projektu zkopírujte **endpoint** a **API klíč**.
1. Použijte hodnotu endpoint pro `AZURE_INFERENCE_ENDPOINT` a hodnotu klíče pro `AZURE_INFERENCE_CREDENTIAL` ve vašem souboru `.env`.

## Offline / Lokální poskytovatelé

Pokud nechcete vůbec používat cloudové předplatné, můžete spustit kompatibilní otevřené modely přímo na svém vlastním zařízení:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoft runtime přímo na zařízení. Automaticky vybere nejlepší běhové prostředí (NPU, GPU nebo CPU) a poskytuje endpoint kompatibilní s OpenAI, takže můžete znovu použít většinu ukázkového kódu z tohoto kurzu s minimálními úpravami. Viz [Foundry Local dokumentace](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) pro začátek, nebo nainstalujte pomocí `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - oblíbená alternativa pro lokální spuštění otevřených modelů jako Llama, Phi, Mistral a Gemma.


Podívejte se na [Lekce 19: Stavba s SLM](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) pro praktické příklady využití obou možností.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->