<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "78bbeed50fd4dc9fdee931f5daf98cb3",
  "translation_date": "2025-10-17T21:36:15+00:00",
  "source_file": "12-designing-ux-for-ai-applications/README.md",
  "language_code": "cs"
}
-->
# Navrhování UX pro AI aplikace

[![Navrhování UX pro AI aplikace](../../../translated_images/12-lesson-banner.c53c3c7c802e8f563953ce388f6a987ca493472c724d924b060be470951c53c8.cs.png)](https://youtu.be/VKbCejSICA8?si=MKj7GQYHfXRZyWW6)

> _(Klikněte na obrázek výše pro zhlédnutí videa této lekce)_

Uživatelská zkušenost je velmi důležitým aspektem při vytváření aplikací. Uživatelé musí být schopni používat vaši aplikaci efektivně k plnění úkolů. Být efektivní je jedna věc, ale je také nutné navrhovat aplikace tak, aby je mohli používat všichni, tedy aby byly _přístupné_. Tato kapitola se zaměří na tuto oblast, abyste nakonec navrhli aplikaci, kterou lidé mohou a chtějí používat.

## Úvod

Uživatelská zkušenost je způsob, jakým uživatel interaguje s konkrétním produktem nebo službou, ať už jde o systém, nástroj nebo design. Při vývoji AI aplikací se vývojáři zaměřují nejen na zajištění efektivní uživatelské zkušenosti, ale také na její etiku. V této lekci se zaměříme na to, jak vytvářet aplikace umělé inteligence (AI), které odpovídají potřebám uživatelů.

Lekce pokryje následující oblasti:

- Úvod do uživatelské zkušenosti a pochopení potřeb uživatelů
- Navrhování AI aplikací pro důvěru a transparentnost
- Navrhování AI aplikací pro spolupráci a zpětnou vazbu

## Cíle učení

Po absolvování této lekce budete schopni:

- Pochopit, jak vytvářet AI aplikace, které odpovídají potřebám uživatelů.
- Navrhovat AI aplikace, které podporují důvěru a spolupráci.

### Předpoklad

Věnujte čas a přečtěte si více o [uživatelské zkušenosti a designovém myšlení.](https://learn.microsoft.com/training/modules/ux-design?WT.mc_id=academic-105485-koreyst)

## Úvod do uživatelské zkušenosti a pochopení potřeb uživatelů

V našem fiktivním vzdělávacím startupu máme dva hlavní typy uživatelů: učitele a studenty. Každý z těchto dvou typů má jedinečné potřeby. Design zaměřený na uživatele upřednostňuje uživatele a zajišťuje, že produkty jsou relevantní a přínosné pro ty, pro které jsou určeny.

Aplikace by měla být **užitečná, spolehlivá, přístupná a příjemná**, aby poskytovala dobrou uživatelskou zkušenost.

### Použitelnost

Být užitečný znamená, že aplikace má funkce odpovídající jejímu zamýšlenému účelu, například automatizaci procesu hodnocení nebo generování kartiček pro opakování. Aplikace, která automatizuje proces hodnocení, by měla být schopna přesně a efektivně přiřazovat známky k práci studentů na základě předem definovaných kritérií. Podobně aplikace, která generuje kartičky pro opakování, by měla být schopna vytvářet relevantní a rozmanité otázky na základě svých dat.

### Spolehlivost

Být spolehlivý znamená, že aplikace dokáže konzistentně a bez chyb plnit svůj úkol. Nicméně AI, stejně jako lidé, není dokonalá a může být náchylná k chybám. Aplikace se mohou setkat s chybami nebo neočekávanými situacemi, které vyžadují lidský zásah nebo opravu. Jak se vypořádáte s chybami? V poslední části této lekce se zaměříme na to, jak jsou AI systémy a aplikace navrženy pro spolupráci a zpětnou vazbu.

### Přístupnost

Být přístupný znamená rozšířit uživatelskou zkušenost na uživatele s různými schopnostmi, včetně těch s postižením, a zajistit, že nikdo nebude vynechán. Dodržováním zásad a pokynů pro přístupnost se AI řešení stávají inkluzivnějšími, použitelnějšími a přínosnějšími pro všechny uživatele.

### Příjemnost

Být příjemný znamená, že je aplikace radost používat. Příjemná uživatelská zkušenost může mít pozitivní dopad na uživatele, povzbudit je k návratu k aplikaci a zvýšit příjmy firmy.

![obrázek ilustrující úvahy o UX v AI](../../../translated_images/uxinai.d5b4ed690f5cefff0c53ffcc01b480cdc1828402e1fdbc980490013a3c50935a.cs.png)

Ne každý problém lze vyřešit pomocí AI. AI přichází na řadu, aby doplnila vaši uživatelskou zkušenost, ať už automatizací manuálních úkolů nebo personalizací uživatelských zkušeností.

## Navrhování AI aplikací pro důvěru a transparentnost

Budování důvěry je klíčové při navrhování AI aplikací. Důvěra zajišťuje, že uživatel má jistotu, že aplikace splní úkol, poskytne konzistentní výsledky a že výsledky odpovídají potřebám uživatele. Rizikem v této oblasti je nedůvěra a přehnaná důvěra. Nedůvěra nastává, když uživatel má malou nebo žádnou důvěru v AI systém, což vede k odmítnutí vaší aplikace. Přehnaná důvěra nastává, když uživatel přeceňuje schopnosti AI systému, což vede k tomu, že uživatel příliš důvěřuje AI systému. Například automatizovaný systém hodnocení v případě přehnané důvěry může vést k tomu, že učitel neprojde některé práce, aby se ujistil, že systém hodnocení funguje správně. To by mohlo vést k nespravedlivým nebo nepřesným známkám pro studenty nebo k přehlédnutí příležitostí pro zpětnou vazbu a zlepšení.

Dva způsoby, jak zajistit, že důvěra je umístěna přímo do středu designu, jsou vysvětlitelnost a kontrola.

### Vysvětlitelnost

Když AI pomáhá informovat rozhodnutí, jako je předávání znalostí budoucím generacím, je důležité, aby učitelé a rodiče rozuměli tomu, jak jsou rozhodnutí AI přijímána. To je vysvětlitelnost - pochopení, jak AI aplikace přijímají rozhodnutí. Navrhování pro vysvětlitelnost zahrnuje přidávání podrobností, které zdůrazňují, jak AI dospěla k výstupu. Publikum musí být informováno, že výstup je generován AI a nikoli člověkem. Například místo "Začněte chatovat se svým učitelem nyní" řekněte "Použijte AI učitele, který se přizpůsobí vašim potřebám a pomůže vám učit se vaším tempem."

![stránka aplikace s jasnou ilustrací vysvětlitelnosti v AI aplikacích](../../../translated_images/explanability-in-ai.134426a96b498fbfdc80c75ae0090aedc0fc97424ae0734fccf7fb00a59a20d9.cs.png)

Dalším příkladem je, jak AI používá uživatelská a osobní data. Například uživatel s personou student může mít omezení na základě své persony. AI nemusí být schopna odhalit odpovědi na otázky, ale může pomoci uživateli přemýšlet o tom, jak může problém vyřešit.

![AI odpovídající na otázky na základě persony](../../../translated_images/solving-questions.b7dea1604de0cbd2e9c5fa00b1a68a0ed77178a035b94b9213196b9d125d0be8.cs.png)

Poslední klíčovou částí vysvětlitelnosti je zjednodušení vysvětlení. Studenti a učitelé nemusí být odborníky na AI, proto by vysvětlení toho, co aplikace může nebo nemůže dělat, měla být zjednodušená a snadno pochopitelná.

![zjednodušená vysvětlení schopností AI](../../../translated_images/simplified-explanations.4679508a406c3621fa22bad4673e717fbff02f8b8d58afcab8cb6f1aa893a82f.cs.png)

### Kontrola

Generativní AI vytváří spolupráci mezi AI a uživatelem, kde například uživatel může upravit podněty pro různé výsledky. Navíc, jakmile je výstup generován, uživatelé by měli být schopni upravit výsledky, což jim dává pocit kontroly. Například při používání Bingu můžete upravit svůj podnět na základě formátu, tónu a délky. Navíc můžete přidat změny do svého výstupu a upravit ho, jak je ukázáno níže:

![Výsledky vyhledávání Bing s možnostmi úpravy podnětu a výstupu](../../../translated_images/bing1.293ae8527dbe2789b675c8591c9fb3cb1aa2ada75c2877f9aa9edc059f7a8b1c.cs.png)

Další funkcí v Bingu, která umožňuje uživateli mít kontrolu nad aplikací, je možnost přihlásit se nebo odhlásit z dat, která AI používá. Pro školní aplikaci může student chtít použít své poznámky i zdroje učitelů jako materiál pro opakování.

![Výsledky vyhledávání Bing s možnostmi úpravy podnětu a výstupu](../../../translated_images/bing2.309f4845528a88c28c1c9739fb61d91fd993dc35ebe6fc92c66791fb04fceb4d.cs.png)

> Při navrhování AI aplikací je klíčová záměrnost, která zajistí, že uživatelé nebudou přehnaně důvěřovat a nastavovat nerealistická očekávání ohledně jejích schopností. Jedním ze způsobů, jak toho dosáhnout, je vytvoření tření mezi podněty a výsledky. Připomínání uživateli, že se jedná o AI a nikoli o jiného člověka.

## Navrhování AI aplikací pro spolupráci a zpětnou vazbu

Jak již bylo zmíněno, generativní AI vytváří spolupráci mezi uživatelem a AI. Většina interakcí spočívá v tom, že uživatel zadá podnět a AI generuje výstup. Co když je výstup nesprávný? Jak aplikace řeší chyby, pokud k nim dojde? Obviňuje AI uživatele nebo si vezme čas na vysvětlení chyby?

AI aplikace by měly být navrženy tak, aby přijímaly a poskytovaly zpětnou vazbu. To nejen pomáhá AI systému zlepšovat se, ale také buduje důvěru s uživateli. Zpětnovazební smyčka by měla být zahrnuta do designu, příkladem může být jednoduché palec nahoru nebo dolů na výstupu.

Dalším způsobem, jak to řešit, je jasně komunikovat schopnosti a omezení systému. Když uživatel udělá chybu při požadavku na něco mimo schopnosti AI, mělo by existovat také způsob, jak to řešit, jak je ukázáno níže.

![Poskytování zpětné vazby a řešení chyb](../../../translated_images/feedback-loops.7955c134429a94663443ad74d59044f8dc4ce354577f5b79b4bd2533f2cafc6f.cs.png)

Systémové chyby jsou běžné u aplikací, kde uživatel může potřebovat pomoc s informacemi mimo rozsah AI nebo aplikace může mít limit na počet otázek/předmětů, které uživatel může generovat souhrny. Například AI aplikace trénovaná na datech z omezených předmětů, například historie a matematiky, nemusí být schopna řešit otázky týkající se geografie. Aby se tomu předešlo, AI systém může dát odpověď jako: "Promiňte, náš produkt byl trénován na datech z následujících předmětů....., nemohu odpovědět na otázku, kterou jste položili."

AI aplikace nejsou dokonalé, proto jsou náchylné k chybám. Při navrhování vašich aplikací byste měli zajistit, že vytvoříte prostor pro zpětnou vazbu od uživatelů a řešení chyb způsobem, který je jednoduchý a snadno vysvětlitelný.

## Úkol

Vezměte jakékoli AI aplikace, které jste dosud vytvořili, a zvažte implementaci níže uvedených kroků do vaší aplikace:

- **Příjemnost:** Zvažte, jak můžete udělat vaši aplikaci příjemnější. Přidáváte vysvětlení všude? Povzbuzujete uživatele k prozkoumání? Jak formulujete své chybové zprávy?

- **Použitelnost:** Vytváříte webovou aplikaci. Ujistěte se, že je vaše aplikace navigovatelná jak myší, tak klávesnicí.

- **Důvěra a transparentnost:** Nevěřte AI úplně a jejímu výstupu, zvažte, jak byste přidali člověka do procesu ověřování výstupu. Také zvažte a implementujte další způsoby, jak dosáhnout důvěry a transparentnosti.

- **Kontrola:** Dejte uživateli kontrolu nad daty, která poskytuje aplikaci. Implementujte způsob, jakým se uživatel může přihlásit nebo odhlásit ze sběru dat v AI aplikaci.

<!-- ## [Kvíz po přednášce](../../../12-designing-ux-for-ai-applications/quiz-url) -->

## Pokračujte ve svém učení!

Po dokončení této lekce se podívejte na naši [kolekci učení o generativní AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), abyste dále rozvíjeli své znalosti o generativní AI!

Přejděte na lekci 13, kde se podíváme na [zabezpečení AI aplikací](../13-securing-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.