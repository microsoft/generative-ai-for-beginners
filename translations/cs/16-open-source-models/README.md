<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85b754d4dc980f270f264d17116d9a5f",
  "translation_date": "2025-12-19T16:43:36+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "cs"
}
-->
[![Open Source Models](../../../translated_images/cs/16-lesson-banner.6b56555e8404fda1.png)](https://youtu.be/CuICgfuHFSg?si=x8SpFRUsIxM9dohN)

## Úvod

Svět open-source LLM je vzrušující a neustále se vyvíjí. Tento kurz si klade za cíl poskytnout podrobný pohled na open source modely. Pokud hledáte informace o tom, jak se proprietární modely srovnávají s open source modely, přejděte na lekci ["Prozkoumání a porovnání různých LLM"](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Tato lekce se také bude věnovat tématu doladění, ale podrobnější vysvětlení najdete v lekci ["Doladění LLM"](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Cíle učení

- Získat porozumění open source modelům
- Pochopit výhody práce s open source modely
- Prozkoumat dostupné open modely na Hugging Face a v Azure AI Studiu

## Co jsou Open Source Modely?

Open source software sehrál klíčovou roli v rozvoji technologií v různých oblastech. Open Source Initiative (OSI) definovala [10 kritérií pro software](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst), aby byl klasifikován jako open source. Zdrojový kód musí být otevřeně sdílen pod licencí schválenou OSI.

Vývoj LLM má podobné prvky jako vývoj softwaru, ale proces není zcela stejný. To vyvolalo mnoho diskuzí v komunitě o definici open source v kontextu LLM. Aby model odpovídal tradiční definici open source, měly by být veřejně dostupné následující informace:

- Datové sady použité k tréninku modelu.
- Kompletní váhy modelu jako součást tréninku.
- Evaluační kód.
- Kód pro doladění.
- Kompletní váhy modelu a metriky tréninku.

V současné době existuje jen několik modelů, které těmto kritériím vyhovují. [Model OLMo vytvořený Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) je jedním z nich.

Pro tuto lekci budeme modely nadále označovat jako "open modely", protože v době psaní nemusí splňovat výše uvedená kritéria.

## Výhody Open Modelů

**Vysoce přizpůsobitelné** – Protože open modely jsou vydávány s podrobnými informacemi o tréninku, výzkumníci a vývojáři mohou upravovat vnitřní strukturu modelu. To umožňuje vytvářet vysoce specializované modely, které jsou doladěné pro konkrétní úkol nebo oblast studia. Některé příklady jsou generování kódu, matematické operace a biologie.

**Cena** – Cena za token při používání a nasazení těchto modelů je nižší než u proprietárních modelů. Při budování aplikací Generativní AI byste měli zvážit poměr výkonu a ceny při práci s těmito modely pro váš konkrétní případ použití.

![Model Cost](../../../translated_images/cs/model-price.3f5a3e4d32ae00b4.png)
Zdroj: Artificial Analysis

**Flexibilita** – Práce s open modely vám umožňuje být flexibilní v používání různých modelů nebo jejich kombinování. Příkladem jsou [HuggingChat asistenti](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst), kde si uživatel může přímo v uživatelském rozhraní vybrat používaný model:

![Choose Model](../../../translated_images/cs/choose-model.f095d15bbac92214.png)

## Prozkoumání různých Open Modelů

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), vyvinutý společností Meta, je open model optimalizovaný pro chatové aplikace. Je to díky metodě doladění, která zahrnovala velké množství dialogů a lidské zpětné vazby. Tato metoda umožňuje modelu produkovat výsledky více odpovídající lidským očekáváním, což zlepšuje uživatelský zážitek.

Některé příklady doladěných verzí Llama zahrnují [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), který se specializuje na japonštinu, a [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), což je vylepšená verze základního modelu.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) je open model se silným zaměřením na vysoký výkon a efektivitu. Používá přístup Mixture-of-Experts, který kombinuje skupinu specializovaných expertních modelů do jednoho systému, kde jsou podle vstupu vybírány určité modely k použití. To činí výpočet efektivnějším, protože modely řeší pouze vstupy, na které jsou specializované.

Některé příklady doladěných verzí Mistral zahrnují [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), který se zaměřuje na lékařskou oblast, a [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), který provádí matematické výpočty.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) je LLM vytvořený Technology Innovation Institute (**TII**). Falcon-40B byl trénován na 40 miliardách parametrů a ukázalo se, že podává lepší výkon než GPT-3 s menším výpočetním rozpočtem. Je to díky použití algoritmu FlashAttention a multiquery attention, které umožňují snížit požadavky na paměť při inferenci. Díky zkrácené době inferenčního zpracování je Falcon-40B vhodný pro chatové aplikace.

Některé příklady doladěných verzí Falcon jsou [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), asistent postavený na open modelech, a [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), který poskytuje vyšší výkon než základní model.

## Jak vybrat

Neexistuje jednoznačná odpověď na výběr open modelu. Dobré místo pro začátek je použití filtru podle úkolu v Azure AI Studiu. To vám pomůže pochopit, pro jaké typy úkolů byl model trénován. Hugging Face také udržuje LLM žebříček, který ukazuje nejlepší modely podle určitých metrik.

Při porovnávání LLM napříč různými typy je dalším skvělým zdrojem [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst):

![Model Quality](../../../translated_images/cs/model-quality.aaae1c22e00f7ee1.png)
Zdroj: Artificial Analysis

Pokud pracujete na konkrétním případu použití, může být efektivní hledat doladěné verze zaměřené na stejnou oblast. Experimentování s více open modely, abyste viděli, jak si vedou podle vašich a uživatelských očekávání, je další dobrá praxe.

## Další kroky

Nejlepší na open modelech je, že s nimi můžete začít pracovat poměrně rychle. Podívejte se na [Azure AI Foundry Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), který obsahuje speciální kolekci Hugging Face s modely, o kterých jsme zde mluvili.

## Učení zde nekončí, pokračujte na cestě

Po dokončení této lekce si prohlédněte naši [kolekci Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) a pokračujte ve zvyšování svých znalostí o Generativní AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->