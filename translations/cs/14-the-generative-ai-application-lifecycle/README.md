<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "27a5347a5022d5ef0a72ab029b03526a",
  "translation_date": "2025-05-20T00:55:18+00:00",
  "source_file": "14-the-generative-ai-application-lifecycle/README.md",
  "language_code": "cs"
}
-->
# Životní cyklus generativní AI aplikace

Důležitou otázkou pro všechny AI aplikace je relevance AI funkcí, protože AI je rychle se vyvíjející oblast. Aby vaše aplikace zůstala relevantní, spolehlivá a robustní, je třeba ji neustále monitorovat, vyhodnocovat a zlepšovat. Zde přichází na řadu životní cyklus generativní AI.

Životní cyklus generativní AI je rámec, který vás provede fázemi vývoje, nasazení a údržby generativní AI aplikace. Pomáhá vám definovat vaše cíle, měřit výkon, identifikovat výzvy a implementovat řešení. Také vám pomáhá sladit vaši aplikaci s etickými a právními standardy vašeho oboru a vašich zainteresovaných stran. Dodržováním životního cyklu generativní AI můžete zajistit, že vaše aplikace vždy přináší hodnotu a uspokojuje vaše uživatele.

## Úvod

V této kapitole se naučíte:

- Pochopit posun paradigmatu z MLOps na LLMOps
- Životní cyklus LLM
- Nástroje pro životní cyklus
- Měření a vyhodnocení životního cyklu

## Pochopit posun paradigmatu z MLOps na LLMOps

LLM jsou nový nástroj v arzenálu umělé inteligence, jsou neuvěřitelně silné v úlohách analýzy a generování pro aplikace, avšak tato síla má určité důsledky pro to, jak zefektivňujeme úlohy AI a klasického strojového učení.

K tomu potřebujeme nové paradigma, které přizpůsobí tento nástroj dynamicky a se správnými podněty. Starší AI aplikace můžeme kategorizovat jako "ML aplikace" a novější AI aplikace jako "GenAI aplikace" nebo prostě "AI aplikace", což odráží hlavní technologie a techniky používané v dané době. To posouvá náš příběh v několika ohledech, podívejte se na následující srovnání.

V LLMOps se více zaměřujeme na vývojáře aplikací, používáme integrace jako klíčový bod, využíváme "Modely jako službu" a přemýšlíme o následujících bodech pro metriky.

- Kvalita: Kvalita odpovědí
- Škoda: Odpovědná AI
- Upřímnost: Základ odpovědí (Dává to smysl? Je to správné?)
- Náklady: Rozpočet na řešení
- Latence: Průměrný čas pro odpověď na token

## Životní cyklus LLM

Nejprve, abychom pochopili životní cyklus a úpravy, podívejme se na následující infografiku.

Jak můžete vidět, to se liší od obvyklých životních cyklů MLOps. LLM mají mnoho nových požadavků, jako je Prompting, různé techniky pro zlepšení kvality (Fine-Tuning, RAG, Meta-Prompts), různé hodnocení a zodpovědnost s odpovědnou AI, a nakonec nové metriky hodnocení (Kvalita, Škoda, Upřímnost, Náklady a Latence).

Například se podívejte, jak ideujeme. Používáme návrh podnětů k experimentování s různými LLM, abychom prozkoumali možnosti a ověřili, zda jejich hypotéza může být správná.

Uvědomte si, že to není lineární, ale integrované smyčky, iterativní a s celkovým cyklem.

Jak bychom mohli prozkoumat tyto kroky? Pojďme se podrobněji podívat, jak bychom mohli postavit životní cyklus.

To může vypadat trochu složitě, zaměřme se nejprve na tři velké kroky.

1. Ideace/Průzkum: Průzkum, zde můžeme prozkoumávat podle našich obchodních potřeb. Prototypování, vytváření [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) a testování, zda je dostatečně efektivní pro naši hypotézu.
2. Budování/Rozšiřování: Implementace, nyní začínáme vyhodnocovat pro větší datové sady, implementujeme techniky, jako je Fine-tuning a RAG, abychom ověřili robustnost našeho řešení. Pokud ne, může pomoci opětovná implementace, přidání nových kroků do našeho toku nebo restrukturalizace dat. Po testování našeho toku a naší škály, pokud to funguje a zkontrolujeme naše metriky, je připraveno na další krok.
3. Operationalizace: Integrace, nyní přidáváme monitorovací a výstražné systémy do našeho systému, nasazení a integraci aplikace do naší aplikace.

Pak máme celkový cyklus managementu, zaměřující se na bezpečnost, shodu a řízení.

Gratulujeme, nyní máte svou AI aplikaci připravenou a funkční. Pro praktickou zkušenost se podívejte na [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

Jaké nástroje bychom mohli použít?

## Nástroje pro životní cyklus

Pro nástroje Microsoft poskytuje [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) a [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst), které usnadňují a zjednodušují implementaci vašeho cyklu.

[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) vám umožňuje používat [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys). AI Studio je webový portál, který vám umožňuje prozkoumávat modely, vzorky a nástroje. Spravuje vaše zdroje, UI vývojové toky a SDK/CLI možnosti pro vývoj orientovaný na kód.

Azure AI vám umožňuje používat více zdrojů k řízení vašich operací, služeb, projektů, potřeb pro vyhledávání vektoru a databází.

Vytvářejte od Proof-of-Concept (POC) až po velké aplikace s PromptFlow:

- Navrhujte a vytvářejte aplikace z VS Code s vizuálními a funkčními nástroji
- Testujte a dolaďujte své aplikace pro kvalitní AI snadno.
- Používejte Azure AI Studio k integraci a iteraci s cloudem, nasazujte a integrujte rychle.

## Skvělé! Pokračujte ve svém učení!

Úžasné, nyní se dozvíte více o tom, jak strukturovat aplikaci pro použití konceptů s [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), abyste zjistili, jak Cloud Advocacy přidává tyto koncepty v ukázkách. Pro více obsahu se podívejte na naši [Ignite breakout session!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Nyní se podívejte na Lekci 15, abyste pochopili, jak [Retrieval Augmented Generation a vektorové databáze](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) ovlivňují generativní AI a jak vytvářet více zapojující aplikace!

**Prohlášení**:  
Tento dokument byl přeložen pomocí AI překladové služby [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoliv usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nenese odpovědnost za jakékoli nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.