<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-06-25T11:31:28+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "cs"
}
-->
# Používání generativní AI zodpovědně

> _Klikněte na obrázek výše pro zhlédnutí videa této lekce_

Je snadné být fascinován umělou inteligencí a zejména generativní AI, ale je třeba zvážit, jak ji používat zodpovědně. Musíte zvážit věci jako zajištění, že výstup je spravedlivý, neškodný a další. Tato kapitola vám má poskytnout zmíněný kontext, co zvážit a jak podniknout aktivní kroky ke zlepšení používání AI.

## Úvod

Tato lekce pokryje:

- Proč byste měli při vytváření aplikací s generativní AI dávat přednost zodpovědné AI.
- Základní principy zodpovědné AI a jak se vztahují ke generativní AI.
- Jak tyto principy zodpovědné AI uvést do praxe prostřednictvím strategie a nástrojů.

## Cíle učení

Po dokončení této lekce budete vědět:

- Důležitost zodpovědné AI při vytváření aplikací s generativní AI.
- Kdy myslet a aplikovat základní principy zodpovědné AI při vytváření aplikací s generativní AI.
- Jaké nástroje a strategie máte k dispozici, abyste koncept zodpovědné AI uvedli do praxe.

## Principy zodpovědné AI

Nadšení pro generativní AI nikdy nebylo větší. Toto nadšení přineslo do této oblasti mnoho nových vývojářů, pozornosti a financí. I když je to velmi pozitivní pro každého, kdo chce vytvářet produkty a firmy pomocí generativní AI, je také důležité postupovat zodpovědně.

V tomto kurzu se zaměřujeme na budování našeho startupu a našeho AI vzdělávacího produktu. Použijeme principy zodpovědné AI: Spravedlnost, Inkluzivnost, Spolehlivost/Bezpečnost, Zabezpečení a Soukromí, Transparentnost a Odpovědnost. S těmito principy prozkoumáme, jak se vztahují k našemu používání generativní AI v našich produktech.

## Proč byste měli dávat přednost zodpovědné AI

Při vytváření produktu vede lidsky orientovaný přístup s ohledem na nejlepší zájem uživatele k nejlepším výsledkům.

Jedinečnost generativní AI spočívá v její schopnosti vytvářet užitečné odpovědi, informace, vedení a obsah pro uživatele. To lze provést bez mnoha manuálních kroků, což může vést k velmi působivým výsledkům. Bez řádného plánování a strategií to však může bohužel vést k některým škodlivým výsledkům pro vaše uživatele, váš produkt a společnost jako celek.

Podívejme se na některé (ale ne všechny) z těchto potenciálně škodlivých výsledků:

### Halucinace

Halucinace je termín používaný k popisu, když LLM produkuje obsah, který je buď zcela nesmyslný, nebo něco, co víme, že je fakticky špatné na základě jiných zdrojů informací.

Představme si například, že vytváříme funkci pro náš startup, která umožňuje studentům klást historické otázky modelu. Student položí otázku `Who was the sole survivor of Titanic?`

Model vytvoří odpověď, jako je ta níže:

![Prompt říkající "Kdo byl jediným přeživším Titaniku"](../../../03-using-generative-ai-responsibly/images/ChatGPT-titanic-survivor-prompt.webp)

Toto je velmi sebevědomá a důkladná odpověď. Bohužel je nesprávná. I s minimálním množstvím výzkumu by někdo zjistil, že z katastrofy Titaniku přežilo více než jeden člověk. Pro studenta, který teprve začíná zkoumat toto téma, může být tato odpověď přesvědčivá natolik, že ji nebude zpochybňovat a bude ji považovat za fakt. Důsledky toho mohou vést k tomu, že AI systém bude nespolehlivý a negativně ovlivní pověst našeho startupu.

S každou iterací jakéhokoli daného LLM jsme viděli zlepšení výkonu v minimalizaci halucinací. I s tímto zlepšením musíme jako tvůrci aplikací a uživatelé zůstat o těchto omezeních informováni.

### Škodlivý obsah

V předchozí části jsme se zabývali, když LLM produkuje nesprávné nebo nesmyslné odpovědi. Dalším rizikem, o kterém musíme být informováni, je, když model reaguje škodlivým obsahem.

Škodlivý obsah může být definován jako:

- Poskytování pokynů nebo podněcování k sebepoškozování nebo poškozování určitých skupin.
- Nenávistný nebo ponižující obsah.
- Vedení plánování jakéhokoli typu útoku nebo násilných činů.
- Poskytování pokynů, jak najít nelegální obsah nebo spáchat nelegální činy.
- Zobrazování sexuálně explicitního obsahu.

Pro náš startup chceme zajistit, že máme správné nástroje a strategie, abychom zabránili tomu, aby tento typ obsahu byl viděn studenty.

### Nedostatek spravedlnosti

Spravedlnost je definována jako "zajištění, že AI systém je bez zaujatosti a diskriminace a že se ke každému chová spravedlivě a rovně". Ve světě generativní AI chceme zajistit, že vylučující světonázory marginalizovaných skupin nejsou posilovány výstupem modelu.

Tyto typy výstupů nejen ničí pozitivní uživatelské zkušenosti pro naše uživatele, ale také způsobují další společenskou újmu. Jako tvůrci aplikací bychom měli vždy mít na paměti širokou a rozmanitou uživatelskou základnu při vytváření řešení s generativní AI.

## Jak používat generativní AI zodpovědně

Nyní, když jsme identifikovali důležitost zodpovědné generativní AI, podívejme se na 4 kroky, které můžeme podniknout, abychom naše AI řešení vytvářeli zodpovědně:

### Měření potenciálních škod

Při testování softwaru testujeme očekávané akce uživatele na aplikaci. Podobně testování různorodé sady podnětů, které uživatelé pravděpodobně použijí, je dobrý způsob, jak měřit potenciální škodu.

Protože náš startup vytváří vzdělávací produkt, bylo by dobré připravit seznam podnětů souvisejících se vzděláním. To by mohlo pokrýt určité téma, historická fakta a podněty o studentském životě.

### Zmírnění potenciálních škod

Nyní je čas najít způsoby, jak můžeme zabránit nebo omezit potenciální škodu způsobenou modelem a jeho odpověďmi. Můžeme se na to podívat ve 4 různých vrstvách:

- **Model**. Výběr správného modelu pro správný případ použití. Větší a složitější modely jako GPT-4 mohou způsobit větší riziko škodlivého obsahu, když jsou aplikovány na menší a specifičtější případy použití. Použití vašich tréninkových dat k doladění také snižuje riziko škodlivého obsahu.

- **Bezpečnostní systém**. Bezpečnostní systém je sada nástrojů a konfigurací na platformě, která slouží modelu a pomáhá zmírnit škody. Příkladem toho je systém filtrování obsahu na službě Azure OpenAI. Systémy by měly také detekovat útoky typu jailbreak a nežádoucí činnosti, jako jsou požadavky od botů.

- **Metaprompt**. Metaprompt a ukotvení jsou způsoby, jak můžeme model řídit nebo omezit na základě určitých chování a informací. To může být pomocí systémových vstupů k definování určitých limitů modelu. Kromě toho poskytování výstupů, které jsou relevantnější k rozsahu nebo doméně systému.

Může to být také pomocí technik jako Retrieval Augmented Generation (RAG), aby model získával informace pouze z výběru důvěryhodných zdrojů. V této kurzu je lekce pro [budování vyhledávacích aplikací](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Uživatelská zkušenost**. Konečná vrstva je místo, kde uživatel přímo interaguje s modelem prostřednictvím rozhraní naší aplikace nějakým způsobem. Tímto způsobem můžeme navrhnout UI/UX tak, aby omezilo uživatele na typy vstupů, které mohou modelu odesílat, stejně jako text nebo obrázky zobrazené uživateli. Při nasazování AI aplikace musíme být také transparentní ohledně toho, co naše generativní AI aplikace může a nemůže dělat.

Máme celou lekci věnovanou [navrhování UX pro AI aplikace](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Hodnocení modelu**. Práce s LLM může být náročná, protože ne vždy máme kontrolu nad daty, na kterých byl model trénován. Bez ohledu na to bychom měli vždy hodnotit výkon a výstupy modelu. Je stále důležité měřit přesnost modelu, podobnost, ukotvení a relevanci výstupu. To pomáhá poskytovat transparentnost a důvěru zainteresovaným stranám a uživatelům.

### Provoz zodpovědného generativního AI řešení

Budování operační praxe kolem vašich AI aplikací je poslední fází. To zahrnuje spolupráci s dalšími částmi našeho startupu, jako je Právní a Bezpečnostní, abychom zajistili, že jsme v souladu se všemi regulačními politikami. Před spuštěním také chceme vybudovat plány kolem dodávky, řešení incidentů a vrácení zpět, abychom zabránili jakékoli újmě našim uživatelům z růstu.

## Nástroje

I když se práce na vývoji zodpovědných AI řešení může zdát jako hodně, je to práce, která stojí za to. Jak oblast generativní AI roste, více nástrojů, které pomáhají vývojářům efektivně integrovat zodpovědnost do jejich pracovních postupů, se bude vyvíjet. Například [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) může pomoci detekovat škodlivý obsah a obrázky prostřednictvím API požadavku.

## Kontrola znalostí

Co jsou některé věci, na které je třeba dbát, abyste zajistili zodpovědné používání AI?

1. Že odpověď je správná.
2. Škodlivé použití, že AI není používána pro kriminální účely.
3. Zajištění, že AI je bez zaujatosti a diskriminace.

A: 2 a 3 jsou správné. Zodpovědná AI vám pomáhá zvážit, jak zmírnit škodlivé účinky a zaujatosti a další.

## 🚀 Výzva

Přečtěte si o [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) a zjistěte, co můžete přijmout pro své použití.

## Skvělá práce, pokračujte ve svém učení

Po dokončení této lekce se podívejte na naši [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), abyste pokračovali ve zvyšování své znalosti generativní AI!

Přejděte na Lekci 4, kde se podíváme na [Základy inženýringu podnětů](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

**Zřeknutí se odpovědnosti**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.