<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b5b016b0eb8a1cef2e3097620d8aa23",
  "translation_date": "2025-12-19T16:45:52+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "cs"
}
-->
# Výběr a konfigurace poskytovatele LLM 🔑

Úkoly **mohou** být také nastaveny tak, aby pracovaly s jedním nebo více nasazeními velkých jazykových modelů (LLM) prostřednictvím podporovaného poskytovatele služeb, jako jsou OpenAI, Azure nebo Hugging Face. Tyto poskytují _hostovaný endpoint_ (API), ke kterému můžeme programově přistupovat s příslušnými přihlašovacími údaji (API klíč nebo token). V tomto kurzu diskutujeme tyto poskytovatele:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) s různými modely včetně základní série GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) pro modely OpenAI s důrazem na připravenost pro podnikové použití
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) pro open-source modely a inference server

**Pro tyto cvičení budete potřebovat vlastní účty**. Úkoly jsou nepovinné, takže si můžete vybrat nastavení jednoho, všech nebo žádného z poskytovatelů podle svých zájmů. Několik rad pro registraci:

| Registrace | Cena | API klíč | Playground | Komentáře |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Ceník](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektově založené](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Bez kódu, web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Více dostupných modelů |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Ceník](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Rychlý start SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Rychlý start Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Přístup je nutné předem požádat](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Ceník](https://huggingface.co/pricing) | [Přístupové tokeny](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat má omezené modely](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Postupujte podle níže uvedených pokynů pro _konfiguraci_ tohoto repozitáře pro použití s různými poskytovateli. Úkoly, které vyžadují konkrétního poskytovatele, budou mít v názvu souboru jednu z těchto značek:

- `aoai` - vyžaduje Azure OpenAI endpoint, klíč
- `oai` - vyžaduje OpenAI endpoint, klíč
- `hf` - vyžaduje Hugging Face token

Můžete nakonfigurovat jednoho, žádného nebo všechny poskytovatele. Příslušné úkoly jednoduše skončí chybou při chybějících přihlašovacích údajích.

## Vytvoření souboru `.env`

Předpokládáme, že jste již přečetli výše uvedené pokyny, zaregistrovali se u příslušného poskytovatele a získali požadované autentizační údaje (API_KEY nebo token). V případě Azure OpenAI předpokládáme, že máte také platné nasazení služby Azure OpenAI (endpoint) s alespoň jedním GPT modelem nasazeným pro chat completion.

Dalším krokem je nastavení vašich **lokálních proměnných prostředí** následovně:

1. Podívejte se v kořenové složce na soubor `.env.copy`, který by měl obsahovat něco takového:

   ```bash
   # Poskytovatel OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Výchozí je nastaven!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Zkopírujte tento soubor do `.env` pomocí níže uvedeného příkazu. Tento soubor je _gitignore-ován_, aby byly tajné údaje v bezpečí.

   ```bash
   cp .env.copy .env
   ```

3. Vyplňte hodnoty (nahraďte zástupné symboly napravo od `=`) podle popisu v další sekci.

4. (Volitelné) Pokud používáte GitHub Codespaces, máte možnost uložit proměnné prostředí jako _Codespaces secrets_ spojené s tímto repozitářem. V takovém případě nebudete muset nastavovat lokální soubor .env. **Poznámka: tato možnost funguje pouze pokud používáte GitHub Codespaces.** Pokud používáte Docker Desktop, stále budete muset nastavit soubor .env.

## Vyplnění souboru `.env`

Podívejme se rychle na názvy proměnných, abychom pochopili, co představují:

| Proměnná  | Popis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Toto je uživatelský přístupový token, který nastavíte ve svém profilu |
| OPENAI_API_KEY | Toto je autorizační klíč pro použití služby mimo Azure OpenAI endpointy |
| AZURE_OPENAI_API_KEY | Toto je autorizační klíč pro použití této služby |
| AZURE_OPENAI_ENDPOINT | Toto je nasazený endpoint pro zdroj Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Toto je endpoint nasazení modelu pro _generování textu_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Toto je endpoint nasazení modelu pro _textové embeddingy_ |
| | |

Poznámka: Poslední dvě proměnné Azure OpenAI odrážejí výchozí model pro chat completion (generování textu) a vyhledávání vektorů (embeddingy). Pokyny k jejich nastavení budou definovány v příslušných úkolech.

## Konfigurace Azure: z portálu

Hodnoty endpointu a klíče Azure OpenAI najdete v [Azure Portálu](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), začněme tedy tam.

1. Přejděte na [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klikněte na možnost **Keys and Endpoint** v postranním panelu (menu vlevo).
1. Klikněte na **Show Keys** - měli byste vidět následující: KEY 1, KEY 2 a Endpoint.
1. Použijte hodnotu KEY 1 pro AZURE_OPENAI_API_KEY
1. Použijte hodnotu Endpoint pro AZURE_OPENAI_ENDPOINT

Dále potřebujeme endpointy pro konkrétní nasazené modely.

1. Klikněte na možnost **Model deployments** v postranním panelu (levé menu) pro zdroj Azure OpenAI.
1. Na cílové stránce klikněte na **Manage Deployments**

Tím se dostanete na web Azure OpenAI Studio, kde najdeme další hodnoty, jak je popsáno níže.

## Konfigurace Azure: ze Studia

1. Přejděte na [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **ze svého zdroje**, jak je popsáno výše.
1. Klikněte na záložku **Deployments** (postranní panel, vlevo) pro zobrazení aktuálně nasazených modelů.
1. Pokud váš požadovaný model není nasazen, použijte **Create new deployment** k jeho nasazení.
1. Budete potřebovat model pro _generování textu_ - doporučujeme: **gpt-35-turbo**
1. Budete potřebovat model pro _textové embeddingy_ - doporučujeme **text-embedding-ada-002**

Nyní aktualizujte proměnné prostředí tak, aby odrážely použité _Deployment name_. Obvykle to bude stejné jako název modelu, pokud jste jej explicitně nezměnili. Například můžete mít:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Nezapomeňte soubor .env po úpravě uložit**. Nyní můžete soubor zavřít a vrátit se k pokynům pro spuštění notebooku.

## Konfigurace OpenAI: z profilu

Váš OpenAI API klíč najdete ve svém [OpenAI účtu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Pokud jej nemáte, můžete si vytvořit účet a vytvořit API klíč. Jakmile klíč máte, můžete jej použít k vyplnění proměnné `OPENAI_API_KEY` v souboru `.env`.

## Konfigurace Hugging Face: z profilu

Váš Hugging Face token najdete ve svém profilu pod [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nezveřejňujte je ani nesdílejte veřejně. Místo toho si vytvořte nový token pro použití v tomto projektu a zkopírujte jej do souboru `.env` pod proměnnou `HUGGING_FACE_API_KEY`. _Poznámka:_ Technicky to není API klíč, ale používá se pro autentizaci, proto zachováváme toto pojmenování pro konzistenci.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->