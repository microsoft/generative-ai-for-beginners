<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:35:55+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "cs"
}
-->
# Nastavení vývojového prostředí

Tento repozitář a kurz jsme nastavili s pomocí [vývojového kontejneru](https://containers.dev?WT.mc_id=academic-105485-koreyst), který obsahuje univerzální runtime podporující vývoj v Python3, .NET, Node.js a Javě. Příslušná konfigurace je definována v souboru `devcontainer.json`, který najdete ve složce `.devcontainer/` v kořenovém adresáři tohoto repozitáře.

Pro aktivaci vývojového kontejneru jej spusťte v [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (pro cloudové runtime) nebo v [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (pro lokální runtime). Více informací o fungování vývojových kontejnerů ve VS Code najdete v [této dokumentaci](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst).  

> [!TIP]  
> Doporučujeme použít GitHub Codespaces pro rychlý start s minimálním úsilím. Nabízí štědrý [bezplatný limit využití](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) pro osobní účty. Nastavte [časové limity](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) pro zastavení nebo smazání neaktivních codespaces, abyste co nejlépe využili svůj limit.


## 1. Spouštění úkolů

Každá lekce může obsahovat _volitelné_ úkoly, které mohou být dostupné v jedné nebo více programovacích jazycích, například Python, .NET/C#, Java a JavaScript/TypeScript. Tato sekce poskytuje obecné pokyny k jejich spouštění.

### 1.1 Python úkoly

Python úkoly jsou poskytovány buď jako aplikace (`.py` soubory) nebo Jupyter notebooky (`.ipynb` soubory).  
- Pro spuštění notebooku jej otevřete ve Visual Studio Code, klikněte na _Select Kernel_ (vpravo nahoře) a vyberte výchozí možnost Python 3. Nyní můžete kliknout na _Run All_ a spustit celý notebook.  
- Pro spuštění Python aplikací z příkazové řádky postupujte podle konkrétních instrukcí úkolu, abyste vybrali správné soubory a zadali požadované argumenty.

## 2. Konfigurace poskytovatelů

Úkoly **mohou** být také nastaveny tak, aby pracovaly s jedním nebo více nasazeními velkých jazykových modelů (LLM) přes podporované poskytovatele služeb jako OpenAI, Azure nebo Hugging Face. Ti poskytují _hostovaný endpoint_ (API), ke kterému můžeme programově přistupovat s použitím správných přihlašovacích údajů (API klíč nebo token). V tomto kurzu se zabýváme těmito poskytovateli:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) s různými modely včetně základní série GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) pro OpenAI modely s důrazem na podnikové nasazení.
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) pro open-source modely a inference server.

**Pro tyto cvičení budete potřebovat vlastní účty**. Úkoly jsou volitelné, takže si můžete vybrat, zda nastavíte jednoho, všechny nebo žádného z poskytovatelů podle svých zájmů. Několik tipů pro registraci:

| Registrace | Cena | API klíč | Playground | Komentáře |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Ceník](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektové klíče](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Více dostupných modelů |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Ceník](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Rychlý start SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Rychlý start Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Přístup je nutné předem požádat](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Ceník](https://huggingface.co/pricing) | [Přístupové tokeny](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat má omezený počet modelů](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Postupujte podle níže uvedených pokynů pro _konfiguraci_ tohoto repozitáře pro použití s různými poskytovateli. Úkoly, které vyžadují konkrétního poskytovatele, budou mít v názvu souboru jednu z těchto značek:
 - `aoai` - vyžaduje Azure OpenAI endpoint a klíč
 - `oai` - vyžaduje OpenAI endpoint a klíč
 - `hf` - vyžaduje Hugging Face token

Můžete nastavit jednoho, žádného nebo všechny poskytovatele. Příslušné úkoly pak při chybějících přihlašovacích údajích jednoduše skončí chybou.

###  2.1. Vytvoření souboru `.env`

Předpokládáme, že jste si přečetli výše uvedené pokyny, zaregistrovali se u příslušného poskytovatele a získali potřebné autentizační údaje (API_KEY nebo token). V případě Azure OpenAI předpokládáme, že máte také platné nasazení služby Azure OpenAI (endpoint) s alespoň jedním GPT modelem nasazeným pro chat completion.

Dalším krokem je nastavení **lokálních proměnných prostředí** následovně:


1. V kořenové složce najděte soubor `.env.copy`, který by měl obsahovat něco jako:

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

2. Zkopírujte tento soubor do `.env` pomocí příkazu níže. Tento soubor je _gitignore-ován_, takže tajné údaje zůstanou v bezpečí.

   ```bash
   cp .env.copy .env
   ```

3. Vyplňte hodnoty (nahraďte zástupné symboly napravo od `=`) podle popisu v další sekci.

3. (Volitelné) Pokud používáte GitHub Codespaces, můžete si nastavit proměnné prostředí jako _Codespaces secrets_ spojené s tímto repozitářem. V takovém případě není potřeba nastavovat lokální `.env` soubor. **Tato možnost však funguje pouze při použití GitHub Codespaces.** Pokud používáte Docker Desktop, stále je potřeba `.env` soubor nastavit.


### 2.2. Vyplnění souboru `.env`

Pojďme si rychle projít názvy proměnných, abychom pochopili, co představují:

| Proměnná  | Popis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Uživatelský přístupový token, který si nastavíte ve svém profilu |
| OPENAI_API_KEY | Autorizační klíč pro použití služby mimo Azure OpenAI endpointy |
| AZURE_OPENAI_API_KEY | Autorizační klíč pro použití Azure OpenAI služby |
| AZURE_OPENAI_ENDPOINT | Nasazený endpoint pro Azure OpenAI zdroj |
| AZURE_OPENAI_DEPLOYMENT | Nasazení modelu pro _generování textu_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Nasazení modelu pro _textové embeddingy_ |
| | |

Poznámka: Poslední dvě proměnné Azure OpenAI odkazují na výchozí model pro chat completion (generování textu) a vyhledávání vektorů (embeddingy). Instrukce k jejich nastavení budou uvedeny v příslušných úkolech.


### 2.3 Konfigurace Azure: z portálu

Hodnoty endpointu a klíče Azure OpenAI najdete v [Azure Portálu](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), začneme tedy tam.

1. Přejděte do [Azure Portálu](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. V levém menu klikněte na možnost **Keys and Endpoint**.
1. Klikněte na **Show Keys** – měli byste vidět: KEY 1, KEY 2 a Endpoint.
1. Pro `AZURE_OPENAI_API_KEY` použijte hodnotu KEY 1.
1. Pro `AZURE_OPENAI_ENDPOINT` použijte hodnotu Endpoint.

Dále potřebujeme endpointy pro konkrétní nasazené modely.

1. V levém menu Azure OpenAI zdroje klikněte na **Model deployments**.
1. Na cílové stránce klikněte na **Manage Deployments**.

Tím se dostanete na web Azure OpenAI Studio, kde najdete další potřebné hodnoty, jak je popsáno níže.

### 2.4 Konfigurace Azure: ze Studia

1. Přejděte do [Azure OpenAI Studia](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **přímo z vašeho zdroje**, jak bylo popsáno výše.
1. Klikněte na záložku **Deployments** (v levém menu) pro zobrazení aktuálně nasazených modelů.
1. Pokud požadovaný model není nasazen, použijte **Create new deployment** pro jeho nasazení.
1. Budete potřebovat model pro _generování textu_ – doporučujeme: **gpt-35-turbo**
1. Budete potřebovat model pro _textové embeddingy_ – doporučujeme **text-embedding-ada-002**

Nyní aktualizujte proměnné prostředí tak, aby odpovídaly názvu _nasazení_ (Deployment name). Obvykle je to stejné jako název modelu, pokud jste jej výslovně nezměnili. Například:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Nezapomeňte soubor `.env` uložit po dokončení**. Poté můžete soubor zavřít a pokračovat v instrukcích pro spuštění notebooku.

### 2.5 Konfigurace OpenAI: z profilu

Váš OpenAI API klíč najdete ve svém [OpenAI účtu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Pokud jej nemáte, můžete si vytvořit účet a vygenerovat API klíč. Jakmile klíč získáte, vložte jej do proměnné `OPENAI_API_KEY` v souboru `.env`.

### 2.6 Konfigurace Hugging Face: z profilu

Váš Hugging Face token najdete ve svém profilu pod [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nezveřejňujte jej ani nesdílejte veřejně. Místo toho si vytvořte nový token pro tento projekt a zkopírujte jej do souboru `.env` pod proměnnou `HUGGING_FACE_API_KEY`. _Poznámka:_ Technicky to není API klíč, ale používá se pro autentizaci, proto jsme zachovali toto pojmenování pro konzistenci.

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.