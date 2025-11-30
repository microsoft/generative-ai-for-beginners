<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d57fad773cbeb69c5dd62e65c34200d",
  "translation_date": "2025-10-17T21:38:14+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "cs"
}
-->
# Zodpovědné používání generativní AI

[![Zodpovědné používání generativní AI](../../../translated_images/03-lesson-banner.1ed56067a452d97709d51f6cc8b6953918b2287132f4909ade2008c936cd4af9.cs.png)](https://youtu.be/YOp-e1GjZdA?si=7Wv4wu3x44L1DCVj)

> _Klikněte na obrázek výše a podívejte se na video této lekce_

Je snadné být fascinován umělou inteligencí, zejména generativní AI, ale je důležité zvážit, jak ji používat zodpovědně. Je třeba přemýšlet o tom, jak zajistit, aby výstupy byly spravedlivé, neškodné a další aspekty. Tato kapitola vám poskytne potřebný kontext, na co se zaměřit a jak podniknout aktivní kroky ke zlepšení používání AI.

## Úvod

Tato lekce se zaměří na:

- Proč byste měli upřednostnit zodpovědnou AI při vytváření aplikací s generativní AI.
- Základní principy zodpovědné AI a jejich vztah ke generativní AI.
- Jak tyto principy zodpovědné AI uvést do praxe pomocí strategie a nástrojů.

## Cíle učení

Po dokončení této lekce budete vědět:

- Proč je důležité zodpovědné AI při vytváření aplikací s generativní AI.
- Kdy přemýšlet a aplikovat základní principy zodpovědné AI při vytváření aplikací s generativní AI.
- Jaké nástroje a strategie máte k dispozici, abyste mohli koncept zodpovědné AI uvést do praxe.

## Principy zodpovědné AI

Nadšení z generativní AI nikdy nebylo větší. Toto nadšení přivedlo do této oblasti mnoho nových vývojářů, pozornosti a financování. I když je to velmi pozitivní pro každého, kdo chce vytvářet produkty a společnosti využívající generativní AI, je také důležité postupovat zodpovědně.

V celém tomto kurzu se zaměřujeme na budování našeho startupu a našeho vzdělávacího produktu s AI. Použijeme principy zodpovědné AI: spravedlnost, inkluzivitu, spolehlivost/bezpečnost, zabezpečení a soukromí, transparentnost a odpovědnost. S těmito principy prozkoumáme, jak se vztahují k našemu využití generativní AI v našich produktech.

## Proč byste měli upřednostnit zodpovědnou AI

Při vytváření produktu vede přístup zaměřený na člověka, který má na paměti nejlepší zájmy uživatele, k nejlepším výsledkům.

Jedinečnost generativní AI spočívá v její schopnosti vytvářet užitečné odpovědi, informace, rady a obsah pro uživatele. To lze provést bez mnoha manuálních kroků, což může vést k velmi působivým výsledkům. Bez řádného plánování a strategií však může bohužel vést i k některým škodlivým výsledkům pro vaše uživatele, váš produkt a společnost jako celek.

Podívejme se na některé (ale ne všechny) z těchto potenciálně škodlivých výsledků:

### Halucinace

Halucinace je termín používaný k popisu situace, kdy LLM vytvoří obsah, který je buď zcela nesmyslný, nebo něco, co víme, že je fakticky nesprávné na základě jiných zdrojů informací.

Představme si například, že vytvoříme funkci pro náš startup, která umožní studentům klást historické otázky modelu. Student se zeptá: `Kdo byl jediným přeživším z Titaniku?`

Model vytvoří odpověď, jako je ta níže:

![Dotaz "Kdo byl jediným přeživším z Titaniku"](../../../03-using-generative-ai-responsibly/images/ChatGPT-titanic-survivor-prompt.webp)

> _(Zdroj: [Flying bisons](https://flyingbisons.com?WT.mc_id=academic-105485-koreyst))_

Toto je velmi sebevědomá a důkladná odpověď. Bohužel je nesprávná. I s minimálním množstvím výzkumu by člověk zjistil, že z katastrofy Titaniku přežilo více než jeden člověk. Pro studenta, který právě začíná zkoumat toto téma, může být tato odpověď natolik přesvědčivá, že ji nebude zpochybňovat a bude ji považovat za fakt. Důsledky toho mohou vést k tomu, že AI systém bude nespolehlivý a negativně ovlivní pověst našeho startupu.

S každou iterací daného LLM jsme zaznamenali zlepšení výkonu v oblasti minimalizace halucinací. I přes toto zlepšení však jako tvůrci aplikací a uživatelé musíme být stále vědomi těchto omezení.

### Škodlivý obsah

V předchozí části jsme se zabývali situací, kdy LLM vytváří nesprávné nebo nesmyslné odpovědi. Dalším rizikem, které musíme mít na paměti, je, když model odpovídá škodlivým obsahem.

Škodlivý obsah lze definovat jako:

- Poskytování instrukcí nebo podporování sebepoškozování či poškozování určitých skupin.
- Nenávistný nebo ponižující obsah.
- Návody na plánování jakéhokoli typu útoku nebo násilných činů.
- Poskytování instrukcí, jak najít nelegální obsah nebo spáchat nelegální činy.
- Zobrazování sexuálně explicitního obsahu.

Pro náš startup chceme zajistit, že máme správné nástroje a strategie, které zabrání tomu, aby tento typ obsahu byl viděn studenty.

### Nedostatek spravedlnosti

Spravedlnost je definována jako „zajištění, že AI systém je bez předsudků a diskriminace a že se chová ke všem spravedlivě a rovně.“ Ve světě generativní AI chceme zajistit, že vylučující pohledy na marginalizované skupiny nebudou posilovány výstupy modelu.

Tyto typy výstupů nejenže ničí pozitivní zkušenosti uživatelů s našimi produkty, ale také způsobují další společenské škody. Jako tvůrci aplikací bychom měli vždy mít na paměti širokou a rozmanitou uživatelskou základnu při vytváření řešení s generativní AI.

## Jak používat generativní AI zodpovědně

Nyní, když jsme identifikovali důležitost zodpovědné generativní AI, podívejme se na 4 kroky, které můžeme podniknout, abychom naše AI řešení budovali zodpovědně:

![Cyklus zmírnění](../../../translated_images/mitigate-cycle.babcd5a5658e1775d5f2cb47f2ff305cca090400a72d98d0f9e57e9db5637c72.cs.png)

### Měření potenciálních škod

Při testování softwaru testujeme očekávané akce uživatele v aplikaci. Podobně je testování různorodé sady dotazů, které uživatelé pravděpodobně použijí, dobrým způsobem, jak měřit potenciální škody.

Protože náš startup vytváří vzdělávací produkt, bylo by dobré připravit seznam dotazů souvisejících se vzděláváním. To by mohlo zahrnovat určité předměty, historická fakta a dotazy týkající se studentského života.

### Zmírnění potenciálních škod

Nyní je čas najít způsoby, jak můžeme zabránit nebo omezit potenciální škody způsobené modelem a jeho odpověďmi. Můžeme se na to podívat ve 4 různých vrstvách:

![Vrstvy zmírnění](../../../translated_images/mitigation-layers.377215120b9a1159a8c3982c6bbcf41b6adf8c8fa04ce35cbaeeb13b4979cdfc.cs.png)

- **Model**. Výběr správného modelu pro správné použití. Větší a složitější modely, jako je GPT-4, mohou představovat větší riziko škodlivého obsahu, pokud jsou aplikovány na menší a konkrétnější případy použití. Použití vašich tréninkových dat k doladění také snižuje riziko škodlivého obsahu.

- **Bezpečnostní systém**. Bezpečnostní systém je sada nástrojů a konfigurací na platformě, která model obsluhuje, a pomáhá zmírnit škody. Příkladem je systém filtrování obsahu na službě Azure OpenAI. Systémy by měly také detekovat útoky typu jailbreak a nežádoucí aktivity, jako jsou požadavky od botů.

- **Metaprompt**. Metaprompt a ukotvení jsou způsoby, jak můžeme model nasměrovat nebo omezit na základě určitých chování a informací. To by mohlo zahrnovat použití systémových vstupů k definování určitých limitů modelu. Navíc poskytování výstupů, které jsou relevantnější pro rozsah nebo doménu systému.

Může to také zahrnovat použití technik, jako je Retrieval Augmented Generation (RAG), aby model čerpal informace pouze z výběru důvěryhodných zdrojů. Později v tomto kurzu je lekce o [vytváření vyhledávacích aplikací](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst).

- **Uživatelská zkušenost**. Poslední vrstva je místo, kde uživatel přímo interaguje s modelem prostřednictvím rozhraní naší aplikace. Tímto způsobem můžeme navrhnout UI/UX tak, aby omezilo uživatele na typy vstupů, které mohou modelu posílat, stejně jako text nebo obrázky zobrazované uživateli. Při nasazení AI aplikace musíme být také transparentní ohledně toho, co naše generativní AI aplikace může a nemůže dělat.

Máme celou lekci věnovanou [navrhování UX pro AI aplikace](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst).

- **Hodnocení modelu**. Práce s LLM může být náročná, protože nemáme vždy kontrolu nad daty, na kterých byl model trénován. Bez ohledu na to bychom měli vždy hodnotit výkon a výstupy modelu. Je stále důležité měřit přesnost, podobnost, ukotvení a relevanci výstupu modelu. To pomáhá poskytovat transparentnost a důvěru zúčastněným stranám a uživatelům.

### Provozování zodpovědného řešení generativní AI

Budování provozní praxe kolem vašich AI aplikací je poslední fáze. To zahrnuje spolupráci s dalšími částmi našeho startupu, jako je právní oddělení a bezpečnost, aby bylo zajištěno dodržování všech regulačních politik. Před spuštěním také chceme vytvořit plány kolem doručení, řešení incidentů a návratu zpět, abychom zabránili jakékoli škodě na našich uživatelích.

## Nástroje

I když se práce na vývoji zodpovědných AI řešení může zdát náročná, je to práce, která se vyplatí. Jak oblast generativní AI roste, bude se vyvíjet více nástrojů, které pomohou vývojářům efektivně integrovat zodpovědnost do jejich pracovních postupů. Například [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) může pomoci detekovat škodlivý obsah a obrázky prostřednictvím API požadavku.

## Kontrola znalostí

Na co je třeba dbát, abyste zajistili zodpovědné používání AI?

1. Že odpověď je správná.
1. Škodlivé použití, aby AI nebyla využívána k trestným činům.
1. Zajištění, že AI je bez předsudků a diskriminace.

Odpověď: Správné jsou 2 a 3. Zodpovědná AI vám pomáhá zvážit, jak zmírnit škodlivé účinky, předsudky a další.

## 🚀 Výzva

Přečtěte si o [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) a zjistěte, co můžete použít pro své potřeby.

## Skvělá práce, pokračujte ve svém učení

Po dokončení této lekce se podívejte na naši [sbírku vzdělávacích materiálů o generativní AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), abyste si dále rozšířili své znalosti o generativní AI!

Přejděte na lekci 4, kde se podíváme na [základy inženýrství promptů](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.