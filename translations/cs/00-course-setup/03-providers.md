<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T18:56:37+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "cs"
}
-->
# Výběr a nastavení poskytovatele LLM 🔑

Úlohy **mohou** být nastaveny tak, aby fungovaly s jedním nebo více nasazeními velkých jazykových modelů (LLM) prostřednictvím podporovaného poskytovatele služeb, jako je OpenAI, Azure nebo Hugging Face. Tyto služby poskytují _hostovaný endpoint_ (API), ke kterému lze přistupovat programově s odpovídajícími přihlašovacími údaji (API klíč nebo token). V tomto kurzu se zaměříme na tyto poskytovatele:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) s různými modely včetně hlavní řady GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) pro OpenAI modely s důrazem na podnikové využití
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) pro open-source modely a inference server

**Pro tyto cvičení budete potřebovat vlastní účty.** Úlohy jsou volitelné, takže si můžete nastavit jednoho, všechny – nebo žádného – poskytovatele podle svých zájmů. Několik tipů k registraci:

| Registrace | Cena | API klíč | Playground | Komentáře |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Ceník](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Podle projektu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | K dispozici více modelů |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Ceník](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Je nutné požádat o přístup předem](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Ceník](https://huggingface.co/pricing) | [Přístupové tokeny](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat má omezený počet modelů](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Postupujte podle níže uvedených pokynů pro _nastavení_ tohoto repozitáře pro použití s různými poskytovateli. Úlohy, které vyžadují konkrétního poskytovatele, budou mít v názvu souboru jeden z těchto tagů:

- `aoai` - vyžaduje Azure OpenAI endpoint a klíč
- `oai` - vyžaduje OpenAI endpoint a klíč
- `hf` - vyžaduje Hugging Face token

Můžete nastavit jednoho, žádného nebo všechny poskytovatele. Související úlohy jednoduše selžou, pokud chybí přihlašovací údaje.

## Vytvoření souboru `.env`

Předpokládáme, že jste si přečetli výše uvedené pokyny, zaregistrovali se u příslušného poskytovatele a získali potřebné autentizační údaje (API_KEY nebo token). V případě Azure OpenAI předpokládáme, že máte platné nasazení služby Azure OpenAI (endpoint) s alespoň jedním GPT modelem nasazeným pro chat completion.

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

2. Zkopírujte tento soubor na `.env` pomocí následujícího příkazu. Tento soubor je _gitignore-d_, takže vaše tajné údaje zůstanou v bezpečí.

   ```bash
   cp .env.copy .env
   ```

3. Doplňte hodnoty (nahraďte zástupné znaky napravo od `=`) podle popisu v další sekci.

4. (Volitelné) Pokud používáte GitHub Codespaces, můžete si uložit proměnné prostředí jako _Codespaces secrets_ spojené s tímto repozitářem. V takovém případě nemusíte nastavovat lokální soubor .env. **Tato možnost však funguje pouze při použití GitHub Codespaces.** Pokud používáte Docker Desktop, musíte soubor .env nastavit ručně.

## Vyplnění souboru `.env`

Podívejme se rychle na názvy proměnných, abychom pochopili, co znamenají:

| Proměnná  | Popis  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Uživatelský přístupový token, který nastavíte ve svém profilu |
| OPENAI_API_KEY | Autorizační klíč pro použití služby pro ne-Azure OpenAI endpointy |
| AZURE_OPENAI_API_KEY | Autorizační klíč pro použití této služby |
| AZURE_OPENAI_ENDPOINT | Nasazený endpoint pro Azure OpenAI resource |
| AZURE_OPENAI_DEPLOYMENT | Endpoint pro nasazení modelu _text generation_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Endpoint pro nasazení modelu _text embeddings_ |
| | |

Poznámka: Poslední dvě proměnné Azure OpenAI odpovídají výchozímu modelu pro chat completion (generování textu) a vektorové vyhledávání (embeddings). Pokyny pro jejich nastavení budou uvedeny v příslušných úlohách.

## Nastavení Azure: Z portálu

Hodnoty endpointu a klíče Azure OpenAI najdete v [Azure Portálu](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), takže začněme tam.

1. Přejděte na [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klikněte na možnost **Keys and Endpoint** v postranním panelu (menu vlevo).
1. Klikněte na **Show Keys** – zobrazí se: KEY 1, KEY 2 a Endpoint.
1. Hodnotu KEY 1 použijte pro AZURE_OPENAI_API_KEY
1. Hodnotu Endpoint použijte pro AZURE_OPENAI_ENDPOINT

Dále potřebujeme endpointy pro konkrétní modely, které jsme nasadili.

1. Klikněte na možnost **Model deployments** v postranním panelu (menu vlevo) pro Azure OpenAI resource.
1. Na cílové stránce klikněte na **Manage Deployments**

Tím se dostanete na web Azure OpenAI Studio, kde najdeme další hodnoty podle popisu níže.

## Nastavení Azure: Ze Studia

1. Přejděte do [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **ze svého resource** podle výše uvedeného postupu.
1. Klikněte na záložku **Deployments** (postranní panel vlevo) pro zobrazení aktuálně nasazených modelů.
1. Pokud požadovaný model není nasazen, použijte **Create new deployment** pro jeho nasazení.
1. Budete potřebovat model pro _generování textu_ – doporučujeme: **gpt-35-turbo**
1. Budete potřebovat model pro _textové embeddingy_ – doporučujeme **text-embedding-ada-002**

Nyní aktualizujte proměnné prostředí podle _Deployment name_, který jste použili. Obvykle bude stejný jako název modelu, pokud jste jej výslovně nezměnili. Například můžete mít:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Nezapomeňte soubor .env po dokončení uložit.** Nyní můžete soubor zavřít a vrátit se k pokynům pro spuštění notebooku.

## Nastavení OpenAI: Z profilu

Váš OpenAI API klíč najdete ve svém [OpenAI účtu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Pokud jej nemáte, můžete si založit účet a vytvořit API klíč. Jakmile klíč získáte, použijte jej pro proměnnou `OPENAI_API_KEY` v souboru `.env`.

## Nastavení Hugging Face: Z profilu

Váš Hugging Face token najdete ve svém profilu pod [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Tyto údaje nikdy nezveřejňujte ani nesdílejte. Vytvořte si nový token pro tento projekt a zkopírujte jej do souboru `.env` pod proměnnou `HUGGING_FACE_API_KEY`. _Poznámka:_ Technicky se nejedná o API klíč, ale používá se pro autentizaci, takže zachováváme tento název pro konzistenci.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Za autoritativní zdroj by měl být považován původní dokument v jeho rodném jazyce. Pro kritické informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné výklady vzniklé použitím tohoto překladu.