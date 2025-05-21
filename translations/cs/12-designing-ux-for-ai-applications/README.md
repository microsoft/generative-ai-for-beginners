<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec385b41ee50579025d50cc03bfb3a25",
  "translation_date": "2025-05-19T22:04:07+00:00",
  "source_file": "12-designing-ux-for-ai-applications/README.md",
  "language_code": "cs"
}
-->
# Navrhování uživatelského zážitku pro AI aplikace

> _(Klikněte na obrázek výše a podívejte se na video k této lekci)_

Uživatelský zážitek je velmi důležitý aspekt při tvorbě aplikací. Uživatelé musí být schopni používat vaši aplikaci efektivně, aby mohli plnit úkoly. Být efektivní je jedna věc, ale také je potřeba navrhovat aplikace tak, aby je mohl používat každý, a tím je udělat _přístupné_. Tato kapitola se zaměří na tuto oblast, abyste nakonec navrhli aplikaci, kterou lidé mohou a chtějí používat.

## Úvod

Uživatelský zážitek je způsob, jakým uživatel interaguje a používá konkrétní produkt nebo službu, ať už jde o systém, nástroj nebo design. Při vývoji AI aplikací se vývojáři zaměřují nejen na zajištění efektivního uživatelského zážitku, ale také na etiku. V této lekci se zabýváme tím, jak vytvářet aplikace umělé inteligence (AI), které řeší potřeby uživatelů.

Lekce pokryje následující oblasti:

- Úvod do uživatelského zážitku a porozumění potřebám uživatelů
- Navrhování AI aplikací pro důvěru a transparentnost
- Navrhování AI aplikací pro spolupráci a zpětnou vazbu

## Cíle učení

Po absolvování této lekce budete schopni:

- Pochopit, jak vytvářet AI aplikace, které splňují potřeby uživatelů.
- Navrhovat AI aplikace, které podporují důvěru a spolupráci.

### Předpoklad

Věnujte nějaký čas a přečtěte si více o [uživatelském zážitku a designovém myšlení.](https://learn.microsoft.com/training/modules/ux-design?WT.mc_id=academic-105485-koreyst)

## Úvod do uživatelského zážitku a porozumění potřebám uživatelů

V našem fiktivním vzdělávacím startupu máme dva hlavní uživatele, učitele a studenty. Každý z těchto uživatelů má jedinečné potřeby. Design zaměřený na uživatele upřednostňuje uživatele a zajišťuje, že produkty jsou relevantní a přínosné pro ty, pro které jsou určeny.

Aplikace by měla být **užitečná, spolehlivá, přístupná a příjemná**, aby poskytovala dobrý uživatelský zážitek.

### Použitelnost

Být užitečný znamená, že aplikace má funkce, které odpovídají jejímu zamýšlenému účelu, jako je automatizace procesu hodnocení nebo generování kartiček pro opakování. Aplikace, která automatizuje proces hodnocení, by měla být schopna přesně a efektivně přiřazovat známky studentským pracím na základě předdefinovaných kritérií. Podobně by aplikace, která generuje kartičky pro opakování, měla být schopna vytvářet relevantní a rozmanité otázky na základě svých dat.

### Spolehlivost

Být spolehlivý znamená, že aplikace může plnit svůj úkol konzistentně a bez chyb. Nicméně AI, stejně jako lidé, není dokonalá a může být náchylná k chybám. Aplikace mohou narazit na chyby nebo neočekávané situace, které vyžadují lidský zásah nebo opravu. Jak řešíte chyby? V poslední části této lekce se budeme zabývat tím, jak jsou AI systémy a aplikace navrženy pro spolupráci a zpětnou vazbu.

### Přístupnost

Být přístupný znamená rozšířit uživatelský zážitek na uživatele s různými schopnostmi, včetně těch s postižením, a zajistit, že nikdo nebude vyloučen. Dodržováním pokynů a principů přístupnosti se AI řešení stávají inkluzivnějšími, použitelnějšími a přínosnějšími pro všechny uživatele.

### Příjemnost

Být příjemný znamená, že je aplikace příjemná k používání. Atraktivní uživatelský zážitek může mít pozitivní dopad na uživatele, povzbudit je k návratu k aplikaci a zvýšit obchodní výnosy.

Ne každý problém lze vyřešit pomocí AI. AI přichází, aby doplnila váš uživatelský zážitek, ať už automatizací manuálních úkolů, nebo personalizací uživatelských zážitků.

## Navrhování AI aplikací pro důvěru a transparentnost

Budování důvěry je klíčové při navrhování AI aplikací. Důvěra zajišťuje, že uživatel je přesvědčen, že aplikace zvládne práci, poskytne výsledky konzistentně a že výsledky jsou to, co uživatel potřebuje. Rizikem v této oblasti je nedůvěra a přehnaná důvěra. Nedůvěra nastává, když uživatel má malou nebo žádnou důvěru v AI systém, což vede k tomu, že uživatel vaši aplikaci odmítne. Přehnaná důvěra nastává, když uživatel přeceňuje schopnosti AI systému, což vede k tomu, že uživatelé důvěřují AI systému příliš. Například automatizovaný systém hodnocení v případě přehnané důvěry může vést k tomu, že učitel neprohlédne některé z prací, aby se ujistil, že systém hodnocení funguje správně. To by mohlo vést k nespravedlivým nebo nepřesným známkám pro studenty, nebo k zmeškaným příležitostem pro zpětnou vazbu a zlepšení.

Dva způsoby, jak zajistit, aby důvěra byla středem návrhu, jsou vysvětlitelnost a kontrola.

### Vysvětlitelnost

Když AI pomáhá informovat o rozhodnutích, jako je předávání znalostí budoucím generacím, je pro učitele a rodiče kritické pochopit, jak jsou rozhodnutí AI přijímána. To je vysvětlitelnost - pochopení toho, jak AI aplikace přijímají rozhodnutí. Navrhování pro vysvětlitelnost zahrnuje přidání podrobností o příkladech toho, co může AI aplikace udělat. Například místo "Začněte s AI učitelem" může systém použít: "Shrňte své poznámky pro snadnější opakování pomocí AI."

Dalším příkladem je, jak AI používá uživatelská a osobní data. Například uživatel s personou studenta může mít omezení na základě své persony. AI nemusí být schopna odhalit odpovědi na otázky, ale může pomoci uživateli přemýšlet, jak může problém vyřešit.

Jednou z klíčových částí vysvětlitelnosti je zjednodušení vysvětlení. Studenti a učitelé nemusí být odborníci na AI, proto by vysvětlení toho, co aplikace může nebo nemůže udělat, měla být zjednodušená a snadno pochopitelná.

### Kontrola

Generativní AI vytváří spolupráci mezi AI a uživatelem, kde například uživatel může upravit podněty pro různé výsledky. Kromě toho, jakmile je výstup vygenerován, uživatelé by měli mít možnost upravit výsledky, což jim dává pocit kontroly. Například při použití Bingu můžete přizpůsobit svůj podnět na základě formátu, tónu a délky. Kromě toho můžete přidat změny do svého výstupu a upravit výstup, jak je ukázáno níže:

Další funkcí v Bingu, která umožňuje uživateli mít kontrolu nad aplikací, je možnost zapnout a vypnout data, která AI používá. Pro školní aplikaci může student chtít použít své poznámky i zdroje učitele jako materiál pro opakování.

> Při navrhování AI aplikací je klíčová záměrnost při zajišťování, že uživatelé nepřehánějí důvěru a nestanovují nereálná očekávání ohledně jejich schopností. Jedním způsobem, jak toho dosáhnout, je vytváření tření mezi podněty a výsledky. Připomínání uživateli, že to je AI a ne jiný člověk.

## Navrhování AI aplikací pro spolupráci a zpětnou vazbu

Jak bylo zmíněno dříve, generativní AI vytváří spolupráci mezi uživatelem a AI. Většina interakcí je s uživatelem, který zadává podnět a AI generuje výstup. Co když je výstup nesprávný? Jak aplikace řeší chyby, pokud k nim dojde? Obviňuje AI uživatele nebo si dává čas na vysvětlení chyby?

AI aplikace by měly být navrženy tak, aby přijímaly a poskytovaly zpětnou vazbu. To nejen pomáhá AI systému zlepšovat se, ale také buduje důvěru s uživateli. Zpětná vazba by měla být součástí návrhu, příkladem může být jednoduché palec nahoru nebo dolů na výstupu.

Dalším způsobem, jak to řešit, je jasně komunikovat schopnosti a omezení systému. Když uživatel udělá chybu a požádá o něco nad rámec schopností AI, měla by existovat i možnost, jak to řešit, jak je ukázáno níže.

Systémové chyby jsou běžné u aplikací, kde uživatel může potřebovat pomoc s informacemi mimo rozsah AI nebo aplikace může mít limit na to, kolik otázek/předmětů může uživatel generovat shrnutí. Například AI aplikace trénovaná s daty na omezených předmětech, například historie a matematika, nemusí být schopna řešit otázky týkající se geografie. Aby se tomu předešlo, AI systém může dát odpověď jako: "Omlouvám se, náš produkt byl trénován s daty v následujících předmětech....., nemohu odpovědět na otázku, kterou jste položili."

AI aplikace nejsou dokonalé, a proto jsou náchylné k chybám. Při navrhování svých aplikací byste měli zajistit, abyste vytvořili prostor pro zpětnou vazbu od uživatelů a řešení chyb způsobem, který je jednoduchý a snadno vysvětlitelný.

## Úkol

Vezměte si jakékoliv AI aplikace, které jste dosud vytvořili, a zvažte implementaci níže uvedených kroků do své aplikace:

- **Příjemnost:** Zvažte, jak můžete svou aplikaci udělat příjemnější. Přidáváte vysvětlení všude? Povzbuzujete uživatele k objevování? Jak formulujete své chybové zprávy?

- **Použitelnost:** Stavíte webovou aplikaci. Ujistěte se, že je vaše aplikace ovladatelná jak myší, tak klávesnicí.

- **Důvěra a transparentnost:** Nevěřte AI úplně a jejím výstupům, zvažte, jak byste do procesu přidali člověka pro ověření výstupu. Také zvažte a implementujte další způsoby, jak dosáhnout důvěry a transparentnosti.

- **Kontrola:** Dejte uživateli kontrolu nad daty, která poskytuje aplikaci. Implementujte způsob, jakým může uživatel zapnout a vypnout sběr dat v AI aplikaci.

## Pokračujte ve svém učení!

Po dokončení této lekce se podívejte na naši [Generativní AI Learning kolekci](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), abyste pokračovali v rozšiřování svých znalostí o Generativní AI!

Přejděte na Lekci 13, kde se podíváme na to, jak [zabezpečit AI aplikace](../13-securing-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Upozornění**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože se snažíme o přesnost, uvědomte si prosím, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.