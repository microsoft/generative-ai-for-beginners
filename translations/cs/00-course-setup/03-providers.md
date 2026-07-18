# Výběr a konfigurace poskytovatele LLM 🔑

Zadání **mohou** být také nastavena tak, aby fungovala proti jedné nebo více nasazením velkých jazykových modelů (LLM) přes podporovaného poskytovatele služeb jako OpenAI, Azure nebo Hugging Face. Tyto poskytují _hostovaný endpoint_ (API), ke kterému můžeme programově přistupovat s odpovídajícími přihlašovacími údaji (API klíč nebo token). V tomto kurzu se zabýváme těmito poskytovateli:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) s různými modely včetně jádra série GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) pro OpenAI modely s důrazem na připravenost pro podnikání
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) pro jediný endpoint a API klíč pro přístup ke stovkám modelů od OpenAI, Meta, Mistral, Cohere, Microsoft a dalších (nahrazuje GitHub Models, které končí ke konci července 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) pro open-source modely a inference server
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) nebo [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) pokud raději spouštíte modely plně offline na vlastním zařízení, bez nutnosti cloudového předplatného

**Pro tyto cvičení budete potřebovat své vlastní účty**. Zadání jsou volitelná, takže si můžete zvolit nastavení jednoho poskytovatele, všech poskytovatelů nebo žádného podle svých preferencí. Některé tipy pro registraci:

| Registrace | Cena | API klíč | Playground | Komentáře |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Ceník](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektové](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Více dostupných modelů |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Ceník](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Rychlý start SDK](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Rychlý start Studio](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Nutno předem žádat o přístup](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Ceník](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Přehled projektu](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | K dispozici bezplatná úroveň; jeden endpoint + klíč pro více poskytovatelů modelů |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Ceník](https://huggingface.co/pricing) | [Přístupové tokeny](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat má omezené modely](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Zdarma (běží na vašem zařízení) | Nepotřebný | [Lokální CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Plně offline, OpenAI-kompatibilní endpoint |
| | | | | |

Postupujte podle níže uvedených pokynů, jak _konfigurovat_ toto úložiště pro použití s různými poskytovateli. Zadání vyžadující konkrétního poskytovatele budou v názvu souboru obsahovat jednu z těchto značek:

- `aoai` - vyžaduje Azure OpenAI endpoint, klíč
- `oai` - vyžaduje OpenAI endpoint, klíč
- `hf` - vyžaduje Hugging Face token
- `githubmodels` - vyžaduje Microsoft Foundry Models endpoint, klíč (GitHub Models končí ke konci července 2026)

Můžete konfigurovat jednoho, žádného nebo všechny poskytovatele. Příslušná zadání jednoduše vyhodí chybu při chybějících přihlašovacích údajích.

## Vytvoření souboru `.env`

Předpokládáme, že jste již přečetli výše uvedené pokyny, zaregistrovali se u příslušného poskytovatele a získali potřebné autentizační údaje (API_KEY nebo token). V případě Azure OpenAI předpokládáme, že máte také platné nasazení Azure OpenAI služby (endpoint) s nasazeným alespoň jedním GPT modelem pro chatovou dokončovací službu.

Dalším krokem je konfigurace vašich **lokálních proměnných prostředí** takto:

1. Podívejte se v kořenové složce na soubor `.env.copy`, který by měl obsahovat následující:

   ```bash
   # Poskytovatel OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI v Microsoft Foundry
   ## (Služba Azure OpenAI je nyní součástí Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Výchozí je nastaven! (aktuální stabilní GA verze API)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Modely Microsoft Foundry (katalog modelů s více poskytovateli, nahrazuje GitHub Modely, které budou ukončeny koncem července 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Zkopírujte tento soubor do `.env` pomocí příkazu níže. Tento soubor je _gitignore-ován_, aby byly tajné informace v bezpečí.

   ```bash
   cp .env.copy .env
   ```

3. Vyplňte hodnoty (nahraďte zástupce napravo od `=`) jak je popsáno v následující sekci.

4. (Volitelně) Pokud používáte GitHub Codespaces, máte možnost uložit proměnné prostředí jako _Codespaces secrets_ spojené s tímto úložištěm. V takovém případě nemusíte nastavovat lokální `.env` soubor. **Tato možnost však funguje pouze při použití GitHub Codespaces.** Pokud používáte Docker Desktop, budete stále muset nastavit `.env` soubor.

## Vyplnění souboru `.env`

Pojďme se rychle podívat na názvy proměnných, abychom pochopili, co představují:

| Proměnná  | Popis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Toto je uživatelský přístupový token, který nastavíte ve svém profilu |
| OPENAI_API_KEY | Toto je autorizační klíč pro používání služby u ne-Azure OpenAI endpointů |
| AZURE_OPENAI_API_KEY | Toto je autorizační klíč pro používání této služby |
| AZURE_OPENAI_ENDPOINT | Toto je nasazený endpoint pro Azure OpenAI zdroj |
| AZURE_OPENAI_DEPLOYMENT | Toto je endpoint nasazení _text-generujícího_ modelu |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Toto je endpoint nasazení _text embeddings_ modelu |
| AZURE_INFERENCE_ENDPOINT | Toto je endpoint vašeho Microsoft Foundry projektu, používaný pro Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Toto je API klíč pro váš Microsoft Foundry projekt |
| | |

Poznámka: Poslední dvě proměnné Azure OpenAI představují výchozí model pro chatovou dokončovací službu (generování textu) a vyhledávání vektoru (embeddings) v tomto pořadí. Instrukce k jejich nastavení budou definovány v příslušných zadáních.

## Konfigurace Azure OpenAI: z portálu

> **Poznámka:** Azure OpenAI Service je nyní součástí [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Zdroje a nasazení se stále zobrazují v Azure Portálu, ale každodenní správa modelů (nasazení, playground, monitoring) se nyní děje v Foundry portálu místo starého samostatného "Azure OpenAI Studio".

Hodnoty pro Azure OpenAI endpoint a klíč najdete v [Azure Portálu](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), začneme tedy tam.

1. Přejděte do [Azure Portálu](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klikněte na možnost **Klíče a Endpoint** v bočním panelu (menu vlevo).
1. Klikněte na **Zobrazit klíče** - měli byste vidět následující: KLÍČ 1, KLÍČ 2 a Endpoint.
1. Pro `AZURE_OPENAI_API_KEY` použijte hodnotu KLÍČ 1
1. Pro `AZURE_OPENAI_ENDPOINT` použijte hodnotu Endpoint

Dále potřebujeme endpointy pro konkrétní modely, které jsme nasadili.

1. Klikněte na možnost **Nasazení modelu** v bočním panelu (levé menu) vašeho zdroje Azure OpenAI.
1. Na cílové stránce klikněte na **Přejít do Microsoft Foundry portálu** (nebo **Spravovat nasazení**, v závislosti na typu vašeho zdroje)

Tím se dostanete do Microsoft Foundry portálu, kde najdeme ostatní hodnoty, jak je popsáno níže.

## Konfigurace Azure OpenAI: z Microsoft Foundry portálu

1. Přejděte do [Microsoft Foundry portálu](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **ze svého zdroje**, jak je uvedeno výše.
1. Klikněte na záložku **Nasazení** (v bočním panelu vlevo) pro zobrazení aktuálně nasazených modelů.
1. Pokud váš požadovaný model není nasazen, použijte **Nasadit model** a vyberte model z [katalogu modelů](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Budete potřebovat _text-generující_ model - doporučujeme: **gpt-5-mini**
1. Budete potřebovat _text-embedding_ model - doporučujeme **text-embedding-3-small**

Nyní aktualizujte proměnné prostředí tak, aby odrážely použité jméno _nasazení_. Obvykle jde o stejné jméno jako model, pokud jste ho explicitně nezměnili. Například byste mohli mít:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Nezapomeňte soubor `.env` po dokončení uložit**. Nyní můžete soubor opustit a vrátit se k instrukcím k spuštění notebooku.

## Konfigurace OpenAI: z profilu

Váš OpenAI API klíč najdete ve svém [účtu OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Pokud ho nemáte, můžete si vytvořit účet a získat API klíč. Jakmile máte klíč, použijte ho k vyplnění proměnné `OPENAI_API_KEY` v souboru `.env`.

## Konfigurace Hugging Face: z profilu

Váš token Hugging Face najdete ve svém profilu v sekci [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Neposílejte je ani nesdílejte veřejně. Místo toho vytvořte nový token pro použití v tomto projektu a zkopírujte ho do souboru `.env` jako hodnotu proměnné `HUGGING_FACE_API_KEY`. _Poznámka:_ Technicky to není API klíč, ale používá se k autentizaci, proto si zachováváme tento název pro konzistenci.

## Konfigurace Microsoft Foundry Models: z portálu

> **Poznámka:** GitHub Models končí ke konci července 2026. Microsoft Foundry Models je přímou náhradou, která nabízí stejný bezplatný katalog modelů a zkušenost s Azure AI Inference SDK / OpenAI SDK.

1. Přejděte na [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) a vytvořte (nebo otevřete) Foundry projekt.
1. Prohlédněte si [katalog modelů](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) a nasaďte model, například `gpt-5-mini`.
1. Na stránce projektu **Přehled** zkopírujte hodnoty **endpoint** a **API klíč**.
1. Pro proměnnou `AZURE_INFERENCE_ENDPOINT` použijte hodnotu endpoint a pro `AZURE_INFERENCE_CREDENTIAL` hodnotu klíče v souboru `.env`.

## Offline / lokální poskytovatelé

Pokud raději nechcete vůbec používat cloudové předplatné, můžete spouštět kompatibilní otevřené modely přímo na svém vlastním zařízení:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoft runtime na zařízení. Automaticky vybírá nejlepší výkonnostní poskytovatele (NPU, GPU nebo CPU) a nabízí OpenAI-kompatibilní endpoint, takže můžete znovu použít většinu ukázkového kódu v tomto kurzu s minimálními změnami. Viz [Foundry Local dokumentace](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst), nebo nainstalujte pomocí `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - populární alternativa pro místní spuštění otevřených modelů jako Llama, Phi, Mistral a Gemma.


Viz [Lekce 19: Stavba s SLM](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) pro praktické příklady použití obou možností.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->