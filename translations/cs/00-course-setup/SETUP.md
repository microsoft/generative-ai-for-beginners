<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T12:58:05+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "cs"
}
-->
# Nastavte své vývojové prostředí

Tento repozitář a kurz jsme nastavili s [vývojovým kontejnerem](https://containers.dev?WT.mc_id=academic-105485-koreyst), který má univerzální runtime podporující vývoj v Python3, .NET, Node.js a Java. Příslušná konfigurace je definována v souboru `devcontainer.json` umístěném ve složce `.devcontainer/` v kořenovém adresáři tohoto repozitáře.

Pro aktivaci vývojového kontejneru jej spusťte v [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (pro cloud-hostovaný runtime) nebo v [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (pro runtime hostovaný na lokálním zařízení). Přečtěte si [tuto dokumentaci](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) pro více podrobností o tom, jak vývojové kontejnery fungují ve VS Code.

> [!TIP]  
> Doporučujeme používat GitHub Codespaces pro rychlý start s minimálním úsilím. Nabízí velkorysý [bezplatný kvótový limit](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) pro osobní účty. Nakonfigurujte [časové limity](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) pro zastavení nebo odstranění neaktivních codespaces, abyste maximalizovali využití kvóty.

## 1. Spouštění úkolů

Každá lekce bude mít _volitelné_ úkoly, které mohou být poskytnuty v jednom nebo více programovacích jazycích, včetně: Python, .NET/C#, Java a JavaScript/TypeScript. Tato sekce poskytuje obecné pokyny související se spouštěním těchto úkolů.

### 1.1 Úkoly v Pythonu

Úkoly v Pythonu jsou poskytovány buď jako aplikace (soubory `.py`) nebo Jupyter notebooky (soubory `.ipynb`). 
- Pro spuštění notebooku jej otevřete ve Visual Studio Code, pak klikněte na _Select Kernel_ (vpravo nahoře) a vyberte výchozí možnost Python 3. Nyní můžete _Run All_ pro spuštění notebooku.
- Pro spuštění Python aplikací z příkazového řádku postupujte podle konkrétních pokynů úkolu, abyste vybrali správné soubory a poskytli potřebné argumenty.

## 2. Konfigurace poskytovatelů

Úkoly **mohou** být také nastaveny tak, aby pracovaly s jedním nebo více nasazeními velkých jazykových modelů (LLM) prostřednictvím podporovaného poskytovatele služeb jako OpenAI, Azure nebo Hugging Face. Tyto poskytují _hostovaný endpoint_ (API), ke kterému můžeme přistupovat programově s příslušnými přihlašovacími údaji (API klíč nebo token). V tomto kurzu diskutujeme o těchto poskytovatelích:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) s různými modely včetně hlavní série GPT.
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) pro OpenAI modely s důrazem na připravenost pro podniky.
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) pro open-source modely a inference server.

**Budete potřebovat použít své vlastní účty pro tyto cvičení**. Úkoly jsou volitelné, takže si můžete vybrat nastavit jednoho, všechny - nebo žádného - z poskytovatelů podle vašich zájmů. Několik pokynů pro registraci:

| Registrace | Cena | API Klíč | Playground | Komentáře |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Ceník](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Na základě projektu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Bez kódu, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | K dispozici více modelů |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Ceník](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Musíte požádat předem o přístup](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Ceník](https://huggingface.co/pricing) | [Přístupové tokeny](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat má omezené modely](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Postupujte podle pokynů níže pro _konfiguraci_ tohoto repozitáře pro použití s různými poskytovateli. Úkoly, které vyžadují konkrétního poskytovatele, budou obsahovat jeden z těchto tagů v názvu souboru:
- `aoai` - vyžaduje Azure OpenAI endpoint, klíč
- `oai` - vyžaduje OpenAI endpoint, klíč
- `hf` - vyžaduje Hugging Face token

Můžete konfigurovat jednoho, žádného, nebo všechny poskytovatele. Související úkoly jednoduše vyhodí chybu při chybějících přihlašovacích údajích.

### 2.1. Vytvořte soubor `.env`

Předpokládáme, že jste si již přečetli výše uvedené pokyny a zaregistrovali se u příslušného poskytovatele, a získali potřebné přihlašovací údaje (API_KEY nebo token). V případě Azure OpenAI předpokládáme, že máte také platné nasazení Azure OpenAI služby (endpoint) s alespoň jedním GPT modelem nasazeným pro dokončení chatu.

Dalším krokem je nakonfigurovat své **lokální proměnné prostředí** následovně:

1. Podívejte se do kořenové složky na soubor `.env.copy`, který by měl mít obsah jako tento:

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

2. Zkopírujte tento soubor do `.env` pomocí níže uvedeného příkazu. Tento soubor je _gitignore-d_, udržující tajemství v bezpečí.

   ```bash
   cp .env.copy .env
   ```

3. Vyplňte hodnoty (nahraďte zástupné znaky na pravé straně `=`) jak je popsáno v následující části.

3. (Volitelné) Pokud používáte GitHub Codespaces, máte možnost uložit proměnné prostředí jako _Codespaces secrets_ spojené s tímto repozitářem. V takovém případě nebudete potřebovat nastavit lokální .env soubor. **Nicméně, všimněte si, že tato možnost funguje pouze pokud používáte GitHub Codespaces.** Stále budete potřebovat nastavit .env soubor, pokud používáte Docker Desktop.

### 2.2. Vyplňte soubor `.env`

Podívejme se rychle na názvy proměnných, abychom pochopili, co představují:

| Proměnná  | Popis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Toto je uživatelský přístupový token, který jste nastavili ve svém profilu |
| OPENAI_API_KEY | Toto je autorizační klíč pro použití služby pro ne-Azure OpenAI endpointy |
| AZURE_OPENAI_API_KEY | Toto je autorizační klíč pro použití této služby |
| AZURE_OPENAI_ENDPOINT | Toto je nasazený endpoint pro Azure OpenAI zdroj |
| AZURE_OPENAI_DEPLOYMENT | Toto je endpoint nasazení modelu pro _generování textu_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Toto je endpoint nasazení modelu pro _text embeddings_ |
| | |

Poznámka: Poslední dvě proměnné Azure OpenAI odrážejí výchozí model pro dokončení chatu (generování textu) a vektorové vyhledávání (embeddings). Pokyny pro jejich nastavení budou definovány v příslušných úkolech.

### 2.3 Konfigurace Azure: Z portálu

Hodnoty endpointu a klíče Azure OpenAI najdete v [Azure portálu](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), takže začněme tam.

1. Přejděte na [Azure portál](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klikněte na možnost **Keys and Endpoint** v postranním panelu (menu vlevo).
1. Klikněte na **Show Keys** - měli byste vidět následující: KEY 1, KEY 2 a Endpoint.
1. Použijte hodnotu KEY 1 pro AZURE_OPENAI_API_KEY
1. Použijte hodnotu Endpoint pro AZURE_OPENAI_ENDPOINT

Dále potřebujeme endpointy pro konkrétní modely, které jsme nasadili.

1. Klikněte na možnost **Model deployments** v postranním panelu (menu vlevo) pro Azure OpenAI zdroj.
1. Na cílové stránce klikněte na **Manage Deployments**

To vás přenese na web Azure OpenAI Studio, kde najdeme další hodnoty, jak je popsáno níže.

### 2.4 Konfigurace Azure: Ze studia

1. Přejděte na [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **ze svého zdroje**, jak je popsáno výše.
1. Klikněte na záložku **Deployments** (postranní panel, vlevo) pro zobrazení aktuálně nasazených modelů.
1. Pokud váš požadovaný model není nasazen, použijte **Create new deployment** pro jeho nasazení.
1. Budete potřebovat model pro _generování textu_ - doporučujeme: **gpt-35-turbo**
1. Budete potřebovat model pro _text embeddings_ - doporučujeme **text-embedding-ada-002**

Nyní aktualizujte proměnné prostředí, aby odrážely _Deployment name_ použité. To bude obvykle stejné jako název modelu, pokud jste jej výslovně nezměnili. Takže například můžete mít:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Nezapomeňte uložit .env soubor, až budete hotovi**. Nyní můžete soubor zavřít a vrátit se k pokynům pro spuštění notebooku.

### 2.5 Konfigurace OpenAI: Z profilu

Váš OpenAI API klíč lze nalézt ve vašem [OpenAI účtu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Pokud jej nemáte, můžete si vytvořit účet a vytvořit API klíč. Jakmile máte klíč, můžete jej použít k vyplnění proměnné `OPENAI_API_KEY` v souboru `.env`.

### 2.6 Konfigurace Hugging Face: Z profilu

Váš Hugging Face token lze nalézt ve vašem profilu pod [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nezveřejňujte ani nesdílejte tyto tokeny veřejně. Místo toho vytvořte nový token pro tento projekt a zkopírujte jej do souboru `.env` pod proměnnou `HUGGING_FACE_API_KEY`. _Poznámka:_ Toto technicky není API klíč, ale používá se pro autentizaci, takže zachováváme tuto konvenci pojmenování pro konzistenci.

**Upozornění**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme zodpovědní za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.