<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a83aac52158c23161046cbd13faa2b",
  "translation_date": "2025-10-17T21:44:50+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "cs"
}
-->
[![Open Source Models](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.cs.png)](https://youtu.be/CuICgfuHFSg?si=x8SpFRUsIxM9dohN)

## Úvod

Svět open-source LLMs je vzrušující a neustále se vyvíjí. Tato lekce si klade za cíl poskytnout podrobný pohled na open-source modely. Pokud hledáte informace o tom, jak se proprietární modely srovnávají s open-source modely, přejděte na lekci ["Zkoumání a porovnávání různých LLMs"](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Tato lekce se také zabývá tématem jemného ladění, ale podrobnější vysvětlení najdete v lekci ["Jemné ladění LLMs"](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Cíle učení

- Získat porozumění open-source modelům
- Pochopit výhody práce s open-source modely
- Prozkoumat dostupné open-source modely na Hugging Face a Azure AI Studio

## Co jsou Open Source Modely?

Open-source software sehrál klíčovou roli v rozvoji technologií napříč různými obory. Open Source Initiative (OSI) definovala [10 kritérií pro software](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst), aby mohl být klasifikován jako open source. Zdrojový kód musí být veřejně sdílen pod licencí schválenou OSI.

Ačkoli vývoj LLMs má podobné prvky jako vývoj softwaru, proces není úplně stejný. To vyvolalo mnoho diskusí v komunitě o definici open source v kontextu LLMs. Aby model odpovídal tradiční definici open source, měly by být veřejně dostupné následující informace:

- Datové sady použité k trénování modelu.
- Kompletní váhy modelu jako součást trénování.
- Kód pro hodnocení.
- Kód pro jemné ladění.
- Kompletní váhy modelu a metriky trénování.

V současné době existuje jen několik modelů, které splňují tato kritéria. [Model OLMo vytvořený Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) je jedním z těch, které odpovídají této kategorii.

Pro tuto lekci budeme modely dále označovat jako "open modely", protože v době psaní nemusí odpovídat výše uvedeným kritériím.

## Výhody Open Modelů

**Vysoce přizpůsobitelné** - Protože open modely jsou vydávány s podrobnými informacemi o trénování, výzkumníci a vývojáři mohou upravovat interní části modelu. To umožňuje vytváření vysoce specializovaných modelů, které jsou jemně laděny pro konkrétní úkol nebo oblast studia. Některé příklady zahrnují generování kódu, matematické operace a biologii.

**Náklady** - Náklady na token při používání a nasazení těchto modelů jsou nižší než u proprietárních modelů. Při budování aplikací generativní AI by mělo být provedeno porovnání výkonu a ceny při práci s těmito modely na vašem konkrétním případu použití.

![Model Cost](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.cs.png)  
Zdroj: Artificial Analysis

**Flexibilita** - Práce s open modely umožňuje flexibilitu při používání různých modelů nebo jejich kombinování. Příkladem je [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst), kde si uživatel může přímo v uživatelském rozhraní vybrat model, který bude použit:

![Choose Model](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.cs.png)

## Prozkoumání různých Open Modelů

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), vyvinutý společností Meta, je open model optimalizovaný pro aplikace založené na chatu. To je způsobeno metodou jemného ladění, která zahrnovala velké množství dialogů a zpětné vazby od lidí. Díky této metodě model produkuje více výsledků, které odpovídají očekáváním lidí, což poskytuje lepší uživatelský zážitek.

Některé příklady jemně laděných verzí Llama zahrnují [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), který se specializuje na japonštinu, a [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), což je vylepšená verze základního modelu.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) je open model s důrazem na vysoký výkon a efektivitu. Používá přístup Mixture-of-Experts, který kombinuje skupinu specializovaných expertních modelů do jednoho systému, kde v závislosti na vstupu jsou vybrány určité modely k použití. To činí výpočet efektivnějším, protože modely se zabývají pouze vstupy, na které jsou specializované.

Některé příklady jemně laděných verzí Mistral zahrnují [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), který se zaměřuje na lékařskou oblast, a [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), který provádí matematické výpočty.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) je LLM vytvořený Technology Innovation Institute (**TII**). Falcon-40B byl trénován na 40 miliardách parametrů, což se ukázalo jako lepší výkon než GPT-3 s menším výpočetním rozpočtem. To je způsobeno použitím algoritmu FlashAttention a multiquery attention, které umožňují snížit požadavky na paměť během doby inferencí. Díky této snížené době inferencí je Falcon-40B vhodný pro aplikace založené na chatu.

Některé příklady jemně laděných verzí Falcon zahrnují [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), asistenta postaveného na open modelech, a [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), který poskytuje vyšší výkon než základní model.

## Jak vybrat

Neexistuje jednoznačná odpověď na otázku, jak vybrat open model. Dobré místo, kde začít, je použití funkce filtrování podle úkolu v Azure AI Studio. To vám pomůže pochopit, pro jaké typy úkolů byl model trénován. Hugging Face také udržuje LLM Leaderboard, který vám ukáže nejlépe hodnocené modely na základě určitých metrik.

Pokud hledáte porovnání LLMs napříč různými typy, [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) je další skvělý zdroj:

![Model Quality](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.cs.png)  
Zdroj: Artificial Analysis

Pokud pracujete na konkrétním případu použití, hledání jemně laděných verzí zaměřených na stejnou oblast může být efektivní. Experimentování s více open modely, abyste zjistili, jak si vedou podle vašich očekávání a očekávání vašich uživatelů, je další dobrá praxe.

## Další kroky

Nejlepší na open modelech je, že s nimi můžete začít pracovat poměrně rychle. Podívejte se na [Azure AI Foundry Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), který obsahuje specifickou kolekci Hugging Face s modely, o kterých jsme zde diskutovali.

## Učení nekončí zde, pokračujte v cestě

Po dokončení této lekce se podívejte na naši [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), abyste pokračovali v rozšiřování svých znalostí o generativní AI!

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.