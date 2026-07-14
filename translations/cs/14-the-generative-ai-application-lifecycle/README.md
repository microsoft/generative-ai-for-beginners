[![Integrace s voláním funkcí](../../../translated_images/cs/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Životní cyklus generativní AI aplikace

Důležitou otázkou pro všechny AI aplikace je relevance AI funkcí, protože AI je rychle se vyvíjející oblast, a abyste zajistili, že vaše aplikace zůstane relevantní, spolehlivá a robustní, je potřeba ji neustále sledovat, hodnotit a vylepšovat. Právě zde přichází na řadu životní cyklus generativní AI.

Životní cyklus generativní AI je rámec, který vás provází jednotlivými fázemi vývoje, nasazení a údržby generativní AI aplikace. Pomáhá vám definovat vaše cíle, měřit výkon, identifikovat výzvy a zavádět řešení. Také vám pomáhá sladit vaši aplikaci s etickými a právními standardy vaší oblasti a vašich zainteresovaných stran. Díky sledování životního cyklu generativní AI můžete zajistit, že vaše aplikace vždy přináší hodnotu a uspokojuje uživatele.

## Úvod

V této kapitole se naučíte:

- Porozumět změně paradigmatu od MLOps k LLMOps
- Životní cyklus LLM
- Nástroje pro životní cyklus
- Metrifikace a hodnocení životního cyklu

## Porozumět změně paradigmatu od MLOps k LLMOps

LLM jsou novým nástrojem v arzenálu umělé inteligence, jsou nesmírně silné v analytických a generativních úlohách pro aplikace, avšak tato síla má důsledky pro způsob, jakým zefektivňujeme úkoly AI a klasického strojového učení.

S tím potřebujeme nové paradigma, které tento nástroj adaptuje dynamicky, s odpovídajícími pobídkami. Starší AI aplikace můžeme kategorizovat jako "ML aplikace" a novější AI aplikace jako "GenAI aplikace" nebo prostě "AI aplikace", což odráží mainstreamové technologie a techniky používané v dané době. Toto mění náš narativ v několika směrech, podívejte se na následující srovnání.

![Srovnání LLMOps vs. MLOps](../../../translated_images/cs/01-llmops-shift.29bc933cb3bb0080.webp)

Všimněte si, že v LLMOps se více zaměřujeme na vývojáře aplikací, používáme integrace jako klíčový prvek, využíváme „Modely jako službu“ a uvažujeme o následujících bodech pro metriky.

- Kvalita: Kvalita odpovědi
- Škoda: Zodpovědná AI
- Poctivost: Opodstatněnost odpovědi (Dává to smysl? Je to správné?)
- Náklady: Rozpočet řešení
- Latence: Průměrný čas na odpověď tokenu

## Životní cyklus LLM

Nejprve, abychom pochopili životní cyklus a změny, podívejme se na následující infografiku.

![Infografika LLMOps](../../../translated_images/cs/02-llmops.70a942ead05a7645.webp)

Jak si možná všimnete, tento životní cyklus se liší od obvyklých životních cyklů MLOps. LLM mají mnoho nových požadavků, jako je promptování, různé techniky ke zlepšení kvality (Fine-Tuning, RAG, Meta-Prompts), jiné hodnocení a odpovědnost v rámci zodpovědné AI, nakonec nové hodnotící metriky (Kvalita, Škoda, Poctivost, Náklady a Latence).

Například se podívejte, jak vymýšlíme nápady. Používáme prompt engineering k experimentování s různými LLM, abychom prozkoumali možnosti a otestovali, zda by jejich hypotéza mohla být správná.

Upozorňujeme, že to není lineární, ale integrované smyčky, iterativní a s nadřazeným cyklem.

Jak můžeme tyto kroky prozkoumat? Pojďme si podrobněji ukázat, jak lze životní cyklus postavit.

![Pracovní tok LLMOps](../../../translated_images/cs/03-llm-stage-flows.3a1e1c401235a6cf.webp)

Toto může vypadat trochu složitě, zaměřme se nejprve na tři hlavní kroky.

1. Nápad/Průzkum: Průzkum, zde můžeme zkoumat podle našich obchodních potřeb. Prototypování, vytváření [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) a testování, zda je dostatečně efektivní pro naši hypotézu.
1. Budování/Doplňování: Implementace, nyní začínáme hodnotit na větších sadách dat, zavádíme techniky jako fine-tuning a RAG, abychom ověřili robustnost našeho řešení. Pokud nefunguje, přeimplementování, přidání nových kroků do našeho toku nebo restrukturalizace dat může pomoci. Po otestování našeho toku a rozsahu, pokud to funguje a zkontrolujeme metriky, je připraveno na další krok.
1. Provozování: Integrace, nyní přidáme monitorovací a výstražné systémy do našeho systému, nasazení a integraci aplikace do naší aplikace.

Pak máme nadřazený cyklus správy, zaměřený na bezpečnost, soulad a řízení.

Gratulujeme, nyní máte svou AI aplikaci připravenou k provozu. Pro praktickou zkušenost se podívejte na [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)

A jaké nástroje můžeme použít?

## Nástroje životního cyklu

Microsoft poskytuje [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) a [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst), které usnadňují a umožňují snadné zavedení vašeho životního cyklu.

[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) vám umožňuje využívat [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst). Microsoft Foundry (dříve Azure AI Studio) je webový portál, který umožňuje prozkoumávat modely, ukázky a nástroje, spravovat vaše zdroje a používat uživatelské vývojové toky stejně jako SDK/CLI možnosti pro kódování.

![Možnosti Azure AI](../../../translated_images/cs/04-azure-ai-platform.80203baf03a12fa8.webp)

Azure AI umožňuje používat různé zdroje pro správu provozu, služeb, projektů, vyhledávání vektorů a databázových potřeb.

![LLMOps s Azure AI](../../../translated_images/cs/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

Konstrukce od proof-of-concept (POC) až po aplikace ve velkém měřítku pomocí PromptFlow:

- Navrhněte a vytvořte aplikace z VS Code, se vizuálními a funkčními nástroji
- Testujte a dolaďte své aplikace pro kvalitní AI snadno.
- Používejte Microsoft Foundry pro integraci a iteraci s cloudem, push a deploy pro rychlou integraci.

![LLMOps s PromptFlow](../../../translated_images/cs/06-llm-promptflow.a183eba07a3a7fdf.webp)

## Skvělé! Pokračujte ve svém učení!

Úžasné, nyní se naučte více o tom, jak strukturovat aplikaci tak, abyste mohli použít koncepty s [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), a podívejte se, jak Cloud Advocacy začleňuje tyto koncepty do demonstrací. Pro více obsahu se podívejte na naši [Ignite breakout session!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Nyní si prohlédněte Lekci 15, abyste pochopili, jak [Retrieval Augmented Generation and Vector Databases](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) ovlivňují generativní AI a jak vytvářet poutavější aplikace!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->