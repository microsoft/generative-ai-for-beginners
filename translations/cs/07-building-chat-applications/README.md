<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5308963a56cfbad2d73b0fa99fe84b3",
  "translation_date": "2025-10-17T21:42:05+00:00",
  "source_file": "07-building-chat-applications/README.md",
  "language_code": "cs"
}
-->
# Vytváření chatovacích aplikací poháněných generativní AI

[![Vytváření chatovacích aplikací poháněných generativní AI](../../../translated_images/07-lesson-banner.a279b937f2843833fe28b4597f51bdef92d0ad03efee7ba52d0f166dea7574e5.cs.png)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Klikněte na obrázek výše pro zhlédnutí videa této lekce)_

Poté, co jsme si ukázali, jak lze vytvářet aplikace pro generování textu, se nyní podíváme na chatovací aplikace.

Chatovací aplikace se staly nedílnou součástí našich každodenních životů a nabízejí více než jen prostředek pro neformální komunikaci. Jsou klíčovou součástí zákaznického servisu, technické podpory a dokonce i sofistikovaných poradenských systémů. Pravděpodobně jste nedávno využili pomoc nějaké chatovací aplikace. Jakmile do těchto platforem integrujeme pokročilé technologie, jako je generativní AI, zvyšuje se jejich složitost a zároveň i výzvy.

Některé otázky, které je třeba zodpovědět, jsou:

- **Vytvoření aplikace**. Jak efektivně vytvořit a bezproblémově integrovat tyto aplikace poháněné AI pro konkrétní případy použití?
- **Monitorování**. Jak zajistit, že aplikace po nasazení fungují na nejvyšší úrovni kvality, jak z hlediska funkčnosti, tak dodržování [šesti principů odpovědné AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

Jak se posouváme do věku definovaného automatizací a bezproblémovou interakcí mezi člověkem a strojem, je nezbytné pochopit, jak generativní AI mění rozsah, hloubku a přizpůsobivost chatovacích aplikací. Tato lekce se zaměří na aspekty architektury, které podporují tyto složité systémy, prozkoumá metodiky pro jejich přizpůsobení konkrétním úkolům a zhodnotí metriky a úvahy důležité pro zajištění odpovědného nasazení AI.

## Úvod

Tato lekce zahrnuje:

- Techniky pro efektivní vytváření a integraci chatovacích aplikací.
- Jak aplikovat přizpůsobení a doladění aplikací.
- Strategie a úvahy pro efektivní monitorování chatovacích aplikací.

## Cíle učení

Na konci této lekce budete schopni:

- Popsat úvahy při vytváření a integraci chatovacích aplikací do stávajících systémů.
- Přizpůsobit chatovací aplikace pro konkrétní případy použití.
- Identifikovat klíčové metriky a úvahy pro efektivní monitorování a udržování kvality chatovacích aplikací poháněných AI.
- Zajistit, aby chatovací aplikace využívaly AI odpovědně.

## Integrace generativní AI do chatovacích aplikací

Zlepšení chatovacích aplikací pomocí generativní AI není jen o tom, aby byly chytřejší; jde o optimalizaci jejich architektury, výkonu a uživatelského rozhraní za účelem poskytování kvalitního uživatelského zážitku. To zahrnuje zkoumání architektonických základů, integrace API a úvahy o uživatelském rozhraní. Tato část vám nabídne komplexní plán pro orientaci v těchto složitých oblastech, ať už je zapojujete do stávajících systémů, nebo je budujete jako samostatné platformy.

Na konci této části budete vybaveni odbornými znalostmi potřebnými k efektivnímu vytvoření a začlenění chatovacích aplikací.

### Chatbot nebo chatovací aplikace?

Než se pustíme do vytváření chatovacích aplikací, porovnejme „chatboty“ s „chatovacími aplikacemi poháněnými AI“, které plní odlišné role a funkce. Hlavním účelem chatbota je automatizovat specifické konverzační úkoly, jako je odpovídání na často kladené otázky nebo sledování zásilek. Obvykle je řízen logikou založenou na pravidlech nebo složitými algoritmy AI. Naproti tomu chatovací aplikace poháněná AI je mnohem širší prostředí navržené tak, aby usnadňovalo různé formy digitální komunikace, jako je text, hlas a video chat mezi lidskými uživateli. Její charakteristickým rysem je integrace generativního AI modelu, který simuluje nuancované, lidsky podobné konverzace a generuje odpovědi na základě široké škály vstupů a kontextových podnětů. Chatovací aplikace poháněná generativní AI může vést otevřené diskuse, přizpůsobovat se měnícím se konverzačním kontextům a dokonce produkovat kreativní nebo složité dialogy.

Následující tabulka uvádí klíčové rozdíly a podobnosti, které nám pomohou pochopit jejich jedinečné role v digitální komunikaci.

| Chatbot                               | Chatovací aplikace poháněná generativní AI |
| ------------------------------------- | ------------------------------------------ |
| Zaměřený na úkoly a založený na pravidlech | Vědomý kontextu                            |
| Často integrovaný do větších systémů  | Může hostovat jeden nebo více chatbotů     |
| Omezený na naprogramované funkce      | Zahrnuje generativní AI modely             |
| Specializované a strukturované interakce | Schopný vést otevřené diskuse              |

### Využití předem připravených funkcí pomocí SDK a API

Při vytváření chatovací aplikace je dobrým prvním krokem zhodnotit, co již existuje. Použití SDK a API k vytvoření chatovacích aplikací je výhodnou strategií z různých důvodů. Integrací dobře zdokumentovaných SDK a API strategicky umisťujete svou aplikaci pro dlouhodobý úspěch, řešíte problémy se škálovatelností a údržbou.

- **Urychluje proces vývoje a snižuje náklady**: Spoléhání se na předem připravené funkce místo nákladného procesu jejich vlastního vývoje vám umožňuje soustředit se na jiné aspekty vaší aplikace, které mohou být důležitější, například obchodní logiku.
- **Lepší výkon**: Při vytváření funkcí od nuly si nakonec položíte otázku „Jak to škáluje? Je tato aplikace schopna zvládnout náhlý příliv uživatelů?“ Dobře udržované SDK a API často mají vestavěná řešení pro tyto problémy.
- **Snadnější údržba**: Aktualizace a vylepšení se snadněji spravují, protože většina API a SDK vyžaduje pouze aktualizaci knihovny při vydání novější verze.
- **Přístup k nejmodernější technologii**: Využití modelů, které byly doladěny a vyškoleny na rozsáhlých datových sadách, poskytuje vaší aplikaci schopnosti přirozeného jazyka.

Přístup k funkcím SDK nebo API obvykle zahrnuje získání povolení k používání poskytovaných služeb, což se často provádí pomocí jedinečného klíče nebo autentizačního tokenu. K prozkoumání toho, jak to vypadá, použijeme knihovnu OpenAI Python. Můžete si to také sami vyzkoušet v následujícím [notebooku pro OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) nebo [notebooku pro Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) pro tuto lekci.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

chat_completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Suggest two titles for an instructional lesson on chat applications for generative AI."}])
```

Výše uvedený příklad používá model GPT-3.5 Turbo k dokončení výzvy, ale všimněte si, že klíč API je nastaven předem. Pokud byste klíč nenastavili, obdrželi byste chybu.

## Uživatelský zážitek (UX)

Obecné principy UX platí pro chatovací aplikace, ale zde je několik dalších úvah, které se stávají obzvláště důležitými kvůli komponentám strojového učení.

- **Mechanismus pro řešení nejasností**: Generativní AI modely občas generují nejasné odpovědi. Funkce, která umožňuje uživatelům požádat o objasnění, může být užitečná, pokud na tento problém narazí.
- **Udržení kontextu**: Pokročilé generativní AI modely mají schopnost si pamatovat kontext v rámci konverzace, což může být nezbytným přínosem pro uživatelský zážitek. Poskytnutí možnosti uživatelům kontrolovat a spravovat kontext zlepšuje uživatelský zážitek, ale přináší riziko uchovávání citlivých informací o uživateli. Úvahy o tom, jak dlouho by měly být tyto informace uchovávány, například zavedení politiky uchovávání, mohou vyvážit potřebu kontextu vůči ochraně soukromí.
- **Personalizace**: Díky schopnosti učit se a přizpůsobovat se nabízejí AI modely individuální zážitek pro uživatele. Přizpůsobení uživatelského zážitku prostřednictvím funkcí, jako jsou uživatelské profily, nejenže dává uživateli pocit, že je pochopen, ale také mu pomáhá najít konkrétní odpovědi, čímž vytváří efektivnější a uspokojivější interakci.

Jedním z příkladů personalizace je nastavení „Vlastní pokyny“ v ChatGPT od OpenAI. Umožňuje vám poskytnout informace o sobě, které mohou být důležitým kontextem pro vaše výzvy. Zde je příklad vlastních pokynů.

![Nastavení vlastních pokynů v ChatGPT](../../../translated_images/custom-instructions.b96f59aa69356fcfed456414221919e8996f93c90c20d0d58d1bc0221e3c909f.cs.png)

Tento „profil“ vybízí ChatGPT k vytvoření plánu lekce o propojených seznamech. Všimněte si, že ChatGPT bere v úvahu, že uživatel může chtít podrobnější plán lekce na základě svých zkušeností.

![Výzva v ChatGPT pro plán lekce o propojených seznamech](../../../translated_images/lesson-plan-prompt.cc47c488cf1343df5d67aa796a1acabca32c380e5b782971e289f6ab8b21cf5a.cs.png)

### Rámec systémových zpráv Microsoftu pro velké jazykové modely

[Microsoft poskytl pokyny](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) pro psaní efektivních systémových zpráv při generování odpovědí z velkých jazykových modelů, rozdělené do 4 oblastí:

1. Definování, pro koho je model určen, stejně jako jeho schopnosti a omezení.
2. Definování formátu výstupu modelu.
3. Poskytnutí konkrétních příkladů, které demonstrují zamýšlené chování modelu.
4. Poskytnutí dalších pravidel pro chování.

### Přístupnost

Ať už má uživatel zrakové, sluchové, motorické nebo kognitivní postižení, dobře navržená chatovací aplikace by měla být použitelná pro všechny. Následující seznam rozděluje konkrétní funkce zaměřené na zlepšení přístupnosti pro různé typy postižení uživatelů.

- **Funkce pro zrakově postižené**: Témata s vysokým kontrastem a přizpůsobitelný text, kompatibilita se čtečkami obrazovky.
- **Funkce pro sluchově postižené**: Funkce převodu textu na řeč a řeči na text, vizuální signály pro zvuková oznámení.
- **Funkce pro motoricky postižené**: Podpora navigace pomocí klávesnice, hlasové příkazy.
- **Funkce pro kognitivně postižené**: Možnosti zjednodušeného jazyka.

## Přizpůsobení a doladění pro jazykové modely specifické pro danou oblast

Představte si chatovací aplikaci, která rozumí žargonu vaší společnosti a předvídá konkrétní dotazy, které její uživatelé běžně mají. Existuje několik přístupů, které stojí za zmínku:

- **Využití modelů DSL**. DSL znamená jazyk specifický pro danou oblast. Můžete využít takzvaný model DSL, který je vyškolen na konkrétní oblast, aby porozuměl jejím konceptům a scénářům.
- **Aplikace doladění**. Doladění je proces dalšího školení vašeho modelu s konkrétními daty.

## Přizpůsobení: Použití DSL

Využití modelů jazyků specifických pro danou oblast (DSL modely) může zlepšit zapojení uživatelů tím, že poskytuje specializované, kontextově relevantní interakce. Jedná se o model, který je vyškolen nebo doladěn tak, aby rozuměl a generoval text související s konkrétním oborem, průmyslem nebo tématem. Možnosti použití modelu DSL se mohou lišit od školení jednoho od nuly až po použití již existujících prostřednictvím SDK a API. Další možností je doladění, které zahrnuje přizpůsobení existujícího předem vyškoleného modelu pro konkrétní oblast.

## Přizpůsobení: Aplikace doladění

Doladění se často zvažuje, když předem vyškolený model nedostačuje v specializované oblasti nebo konkrétním úkolu.

Například lékařské dotazy jsou složité a vyžadují mnoho kontextu. Když lékař diagnostikuje pacienta, vychází z různých faktorů, jako je životní styl nebo předchozí zdravotní stav, a může se dokonce spoléhat na nedávné lékařské studie, aby svou diagnózu ověřil. V takových nuancovaných situacích nemůže být obecný AI chatovací model spolehlivým zdrojem.

### Scénář: lékařská aplikace

Zvažte chatovací aplikaci navrženou tak, aby pomáhala lékařům poskytováním rychlých odkazů na léčebné postupy, interakce léků nebo nejnovější výzkumy.

Obecný model může být dostatečný pro odpovědi na základní lékařské otázky nebo poskytování obecných rad, ale může mít problémy s následujícím:

- **Velmi specifické nebo složité případy**. Například neurolog může aplikaci položit otázku: „Jaké jsou aktuální nejlepší postupy pro léčbu léků odolné epilepsie u pediatrických pacientů?“
- **Nedostatek aktuálních poznatků**. Obecný model může mít problém poskytnout aktuální odpověď, která zahrnuje nejnovější pokroky v neurologii a farmakologii.

V takových případech může doladění modelu pomocí specializované lékařské datové sady významně zlepšit jeho schopnost přesně a spolehlivě řešit tyto složité lékařské dotazy. To vyžaduje přístup k rozsáhlé a relevantní datové sadě, která reprezentuje výzvy a otázky specifické pro danou oblast, které je třeba řešit.

## Úvahy pro vysoce kvalitní chatovací aplikace poháněné AI

Tato část popisuje kritéria pro „vysoce kvalitní“ chatovací aplikace, která zahrnují zachycení akčních metrik a dodržování rámce, který odpovědně využívá technologii AI.

### Klíčové metriky

Pro udržení vysoké kvality výkonu aplikace je nezbytné sledovat klíčové metriky a úvahy. Tyto měření nejen zajišťují funkčnost aplikace, ale také hodnotí kvalitu AI modelu a uživatelského zážitku. Níže je uveden seznam, který pokrývá základní, AI a uživatelské metriky, které je třeba zvážit.

| Metrika                     | Definice                                                                                  | Úvahy pro vývojáře chatovací aplikace                                     |
| --------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Dostupnost**              | Měří dobu, po kterou je aplikace funkční a přístupná uživatelům.                          | Jak minimalizujete výpadky?                                               |
| **Doba odezvy**             | Doba, kterou aplikace potřebuje na odpověď na dotaz uživatele.                            | Jak optimalizujete zpracování dotazů pro zlepšení doby odezvy?            |
| **Přesnost**
| **Detekce anomálií**          | Nástroje a techniky pro identifikaci neobvyklých vzorců, které neodpovídají očekávanému chování.                     | Jak budete reagovat na anomálie?                                           |

### Implementace odpovědných AI praktik v chatovacích aplikacích

Přístup společnosti Microsoft k odpovědné AI identifikoval šest principů, které by měly vést vývoj a používání AI. Níže jsou uvedeny principy, jejich definice a věci, které by měl vývojář chatovacích aplikací zvážit, a proč by je měl brát vážně.

| Principy               | Definice Microsoftu                                   | Doporučení pro vývojáře chatovacích aplikací                           | Proč je to důležité                                                                     |
| ---------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Spravedlnost           | AI systémy by měly zacházet se všemi lidmi spravedlivě. | Zajistěte, aby chatovací aplikace nediskriminovala na základě uživatelských dat. | Budování důvěry a inkluzivity mezi uživateli; vyhýbání se právním důsledkům.            |
| Spolehlivost a bezpečnost | AI systémy by měly fungovat spolehlivě a bezpečně.    | Implementujte testování a bezpečnostní opatření ke snížení chyb a rizik. | Zajišťuje spokojenost uživatelů a předchází potenciálním škodám.                        |
| Soukromí a bezpečnost  | AI systémy by měly být bezpečné a respektovat soukromí. | Zaveďte silné šifrování a opatření na ochranu dat.                     | Ochrana citlivých uživatelských dat a dodržování zákonů o ochraně soukromí.             |
| Inkluzivita            | AI systémy by měly posilovat všechny a zapojovat lidi. | Navrhněte UI/UX, které je přístupné a snadno použitelné pro různé skupiny uživatelů. | Zajišťuje, že aplikaci může efektivně používat širší spektrum lidí.                     |
| Transparentnost        | AI systémy by měly být srozumitelné.                   | Poskytněte jasnou dokumentaci a vysvětlení odpovědí AI.                | Uživatelé mají větší důvěru v systém, pokud rozumí tomu, jak jsou rozhodnutí přijímána. |
| Odpovědnost            | Lidé by měli být odpovědní za AI systémy.              | Zaveďte jasný proces pro auditování a zlepšování rozhodnutí AI.        | Umožňuje průběžné zlepšování a nápravná opatření v případě chyb.                        |

## Zadání

Podívejte se na [zadání](../../../07-building-chat-applications/python). Provede vás sérií cvičení od spuštění prvních chatovacích příkazů, přes klasifikaci a shrnutí textu a další. Všimněte si, že zadání jsou dostupná v různých programovacích jazycích!

## Skvělá práce! Pokračujte v cestě

Po dokončení této lekce se podívejte na naši [sbírku učení o generativní AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), abyste si dále rozšířili znalosti o generativní AI!

Přejděte na Lekci 8 a zjistěte, jak můžete začít [vytvářet vyhledávací aplikace](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.