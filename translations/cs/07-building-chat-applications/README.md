# Tvorba chatovacích aplikací poháněných generativní AI

[![Tvorba chatovacích aplikací poháněných generativní AI](../../../translated_images/cs/07-lesson-banner.a279b937f2843833.webp)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Klikněte na obrázek výše pro zhlédnutí videa této lekce)_

Nyní, když jsme viděli, jak můžeme vytvářet aplikace pro generování textu, podívejme se na chatovací aplikace.

Chatovací aplikace se staly součástí našeho každodenního života, nabízejí více než jen prostředek pro běžné konverzace. Jsou integrální součástí zákaznické podpory, technické pomoci a dokonce i sofistikovaných poradenských systémů. Je pravděpodobné, že jste nedávno využili pomoc nějaké chatovací aplikace. Jak do těchto platforem integrujeme pokročilejší technologie, jako je generativní AI, roste i jejich složitost a výzvy.

Některé otázky, na které potřebujeme najít odpovědi, jsou:

- **Tvorba aplikace**. Jak efektivně vybudovat a bezproblémově integrovat tyto AI-poháněné aplikace pro specifické případy použití?
- **Monitorování**. Jak po nasazení sledovat a zajistit, že aplikace fungují na nejvyšší úrovni kvality, jak z hlediska funkčnosti, tak dodržování [šesti zásad odpovědné AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

Jak postupujeme dále do doby definované automatizací a bezproblémovými interakcemi člověk-stroj, stává se nezbytným pochopení, jak generativní AI mění rozsah, hloubku a adaptabilitu chatovacích aplikací. Tato lekce prozkoumá aspekty architektury podporující tyto složité systémy, metodiky jemného doladění na úkoly specifické pro určitou oblast a zhodnotí metriky a úvahy důležité pro odpovědné nasazení AI.

## Úvod

Tato lekce zahrnuje:

- Techniky pro efektivní tvorbu a integraci chatovacích aplikací.
- Jak aplikovat přizpůsobení a jemné doladění aplikací.
- Strategie a úvahy pro efektivní monitorování chatovacích aplikací.

## Výukové cíle

Na konci této lekce budete umět:

- Popsat úvahy při tvorbě a integraci chatovacích aplikací do existujících systémů.
- Přizpůsobit chatovací aplikace pro specifické případy použití.
- Identifikovat klíčové metriky a úvahy pro efektivní monitorování a udržování kvality AI-poháněných chatovacích aplikací.
- Zajistit odpovědné využívání AI v chatovacích aplikacích.

## Integrace generativní AI do chatovacích aplikací

Vylepšení chatovacích aplikací pomocí generativní AI není jen o tom, aby byly chytřejší; jde o optimalizaci jejich architektury, výkonu a uživatelského rozhraní pro poskytování kvalitního uživatelského zážitku. To zahrnuje zkoumání architektonických základů, integraci API a úvahy o uživatelském rozhraní. Tato část má za cíl nabídnout vám komplexní plán pro orientaci v těchto složitých oblastech, ať už je připojujete k existujícím systémům, nebo vytváříte jako samostatné platformy.

Na konci této části budete vybaveni znalostmi potřebnými k efektivnímu sestavení a začlenění chatovacích aplikací.

### Chatbot nebo chatovací aplikace?

Než se pustíme do tvorby chatovacích aplikací, porovnejme 'chatboty' a 'AI-poháněné chatovací aplikace', které mají odlišné role a funkce. Hlavním účelem chatbota je automatizovat specifické konverzační úkoly, například odpovídání na často kladené otázky nebo sledování zásilky. Obvykle je řízen logikou založenou na pravidlech nebo složitými AI algoritmy. Naproti tomu AI-poháněná chatovací aplikace je mnohem rozsáhlejší prostředí určené k usnadnění různých forem digitální komunikace, jako jsou textové, hlasové a video chaty mezi lidmi. Její dominantní vlastností je integrace generativního AI modelu, který simuluje nuancované, lidsky podobné konverzace a generuje odpovědi na základě široké škály vstupů a kontextových vodítek. Chatovací aplikace poháněná generativní AI dokáže vést rozhovory v otevřené oblasti, přizpůsobit se vyvíjejícím se konverzačním kontextům a dokonce vytvářet kreativní či složitý dialog.

Následující tabulka uvádí klíčové rozdíly a podobnosti, které nám pomohou pochopit jejich jedinečné role v digitální komunikaci.

| Chatbot                               | Chatovací aplikace poháněná generativní AI                 |
| ------------------------------------- | -------------------------------------- |
| Zaměřený na úkoly a založený na pravidlech | Kontextově uvědomělý                      |
| Často integrován do větších systémů  | Může hostit jeden nebo více chatbotů      |
| Omezen na naprogramované funkce       | Zahrnuje generativní AI modely      |
| Specializované a strukturované interakce | Schopen vést diskuse v otevřené oblasti     |

### Využití předpřipravených funkcí pomocí SDK a API

Při tvorbě chatovací aplikace je dobrým prvním krokem zhodnotit, co již existuje. Používání SDK a API při stavbě chatovacích aplikací je výhodnou strategií z několika důvodů. Integrací dobře zdokumentovaných SDK a API strategicky pozicionujete svou aplikaci pro dlouhodobý úspěch, řešíte škálovatelnost a údržbu.

- **Zrychluje vývojový proces a snižuje režii**: Spoléhání se na předpřipravené funkce místo nákladného budování vlastních umožňuje zaměřit se na jiné aspekty aplikace, které mohou být důležitější, například obchodní logiku.
- **Lepší výkon**: Při tvorbě funkčnosti od nuly si nakonec položíte otázku "Jak to škáluje? Je tato aplikace schopna zvládnout náhlý příliv uživatelů?" Dobře udržovaná SDK a API často obsahují vestavěná řešení pro tyto problémy.
- **Snazší údržba**: Aktualizace a vylepšení se snáze spravují, protože většina API a SDK pouze vyžaduje aktualizaci knihovny při vydání novější verze.
- **Přístup k nejmodernější technologii**: Využití modelů, které byly jemně doladěny a trénovány na rozsáhlých datových sadách, poskytuje aplikaci schopnosti zpracování přirozeného jazyka.

Přístup k funkčnosti SDK nebo API obvykle zahrnuje získání oprávnění k používání služeb, často pomocí unikátního klíče nebo autentizačního tokenu. Prozkoumáme, jak to vypadá, pomocí knihovny OpenAI pro Python. Můžete si to také vyzkoušet sami v následujícím [notebooku pro OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) nebo [notebooku pro Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) k této lekci.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

response = client.responses.create(model="gpt-4o-mini", input="Suggest two titles for an instructional lesson on chat applications for generative AI.", store=False)
print(response.output_text)
```

Výše uvedený příklad používá model GPT-4o mini s Responses API k dokončení výzvy, ale všimněte si, že API klíč je nastaven před tímto krokem. Bez nastavení klíče byste dostali chybu.

## Uživatelská zkušenost (UX)

Obecné zásady UX platí i pro chatovací aplikace, ale zde jsou některé doplňkové úvahy, které se stávají zvláště důležitými vzhledem k komponentám strojového učení.

- **Mechanismus řešení nejednoznačnosti**: Generativní AI modely občas generují nejednoznačné odpovědi. Funkce umožňující uživatelům požádat o upřesnění může být užitečná, pokud na tento problém narazí.
- **Udržení kontextu**: Pokročilé generativní AI modely mají schopnost si pamatovat kontext během konverzace, což může být nezbytným přínosem pro uživatelský zážitek. Umožnit uživatelům ovládat a spravovat kontext zlepšuje UX, ale zavádí riziko uchovávání citlivých uživatelských informací. Úvahy o tom, jak dlouho jsou tyto informace uchovávány, například zavedením zásad uchovávání, mohou vyvážit potřebu kontextu s ochranou soukromí.
- **Personalizace**: Díky schopnosti učit se a přizpůsobovat se nabízejí AI modely individualizovaný zážitek pro uživatele. Úprava uživatelského zážitku prostřednictvím funkcí, jako jsou uživatelské profily, nejen že uživatele pocitově lépe pochopí, ale také zlepší jeho snahu najít konkrétní odpovědi, což vytváří efektivnější a uspokojivější interakci.

Jedním z příkladů personalizace jsou nastavení „Vlastní pokyny“ v ChatGPT od OpenAI. Umožňují vám poskytnout informace o sobě, které mohou být důležitým kontextem pro vaše výzvy. Zde je příklad vlastního pokynu.

![Nastavení vlastních pokynů v ChatGPT](../../../translated_images/cs/custom-instructions.b96f59aa69356fcf.webp)

Tento „profil“ vybízí ChatGPT k vytvoření plánu lekce o propojených seznamech. Všimněte si, že ChatGPT bere v potaz, že uživatel může chtít podrobnější plán lekce podle svého zkušenostního základu.

![Výzva v ChatGPT pro plán lekce o propojených seznamech](../../../translated_images/cs/lesson-plan-prompt.cc47c488cf1343df.webp)

### Microsoft Framework systému zpráv pro velké jazykové modely

[Microsoft poskytl pokyny](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) pro psaní efektivních systémových zpráv při generování odpovědí z LLM rozdělených do 4 oblastí:

1. Definování pro koho je model určen, stejně jako jeho schopnosti a omezení.
2. Definování výstupního formátu modelu.
3. Poskytnutí konkrétních příkladů, které demonstrují zamýšlené chování modelu.
4. Poskytnutí dalších behaviorálních pojistek.

### Přístupnost

Ať už má uživatel zrakové, sluchové, motorické nebo kognitivní postižení, dobře navržená chatovací aplikace by měla být použitelná pro všechny. Následující seznam rozděluje specifické funkce zaměřené na zlepšení přístupnosti pro různá postižení uživatelů.

- **Funkce pro zrakové postižení**: Vysoké kontrastní motivy a možnost zvětšování textu, kompatibilita s čtecími zařízeními obrazovky.
- **Funkce pro sluchové postižení**: Funkce text-na-řeč a řeč-na-text, vizuální indikátory zvukových upozornění.
- **Funkce pro motorické postižení**: Podpora navigace pomocí klávesnice, hlasové příkazy.
- **Funkce pro kognitivní postižení**: Možnosti zjednodušeného jazyka.

## Přizpůsobení a jemné doladění pro jazykové modely specifické pro danou oblast

Představte si chatovací aplikaci, která rozumí odbornému jazyku vaší firmy a předvídá specifické dotazy, které běžně kladou její uživatelé. Existuje několik přístupů, které stojí za zmínku:

- **Využití DSL modelů**. DSL znamená domain specific language (jazyk specifický pro oblast). Můžete využít tzv. DSL model trénovaný na specifické oblasti, aby rozuměl jejím konceptům a scénářům.
- **Použití jemného doladění**. Jemné doladění je proces dalšího tréninku vašeho modelu s použitím specifických dat.

## Přizpůsobení: Použití DSL

Využití jazykových modelů specifických pro danou oblast (DSL modely) může zvýšit zapojení uživatelů díky poskytování specializovaných, kontextově relevantních interakcí. Jde o model, který je natrénován nebo jemně doladěn k porozumění a generování textu týkajícího se konkrétního oboru, průmyslu nebo tématu. Možnosti použití DSL modelu sahají od tréninku od základu po využívání již existujících prostřednictvím SDK a API. Další možností je jemné doladění, což zahrnuje vzít existující předtrénovaný model a přizpůsobit ho pro specifickou oblast.

## Přizpůsobení: Použití jemného doladění

Jemné doladění se často zvažuje, když předtrénovaný model nedostačuje ve specializované oblasti nebo specifickém úkolu.

Například lékařské dotazy jsou složité a vyžadují mnoho kontextu. Když lékař diagnostikuje pacienta, vychází z různých faktorů, jako je životní styl nebo předchozí onemocnění, a může se dokonce opírat o nedávné lékařské studie, aby svou diagnózu potvrdil. V takto nuancovaných scénářích obecná AI chatovací aplikace nemůže být spolehlivým zdrojem.

### Příklad: lékařská aplikace

Představte si chatovací aplikaci navrženou k pomoci lékařům poskytováním rychlých informací o léčebných protokolech, interakcích léků nebo nejnovějších výzkumech.

Obecný model může být dostačující pro zodpovězení základních lékařských dotazů nebo poskytnutí obecných rad, ale může mít potíže v následujících případech:

- **Vysoce specifické nebo složité případy**. Například neurolog by mohl aplikaci položit otázku: "Jaké jsou současné nejlepší postupy pro zvládání léky rezistentní epilepsie u dětských pacientů?"
- **Nedostatek nejnovějšího pokroku**. Obecný model by mohl mít problém poskytnout aktuální odpověď zahrnující nejnovější poznatky z neurologie a farmakologie.

V takových případech může jemné doladění modelu se specializovanou lékařskou datovou sadou výrazně zlepšit jeho schopnost řešit tyto složité lékařské dotazy přesněji a spolehlivěji. To vyžaduje přístup k velké a relevantní datové sadě, která reprezentuje výzvy a otázky specifické pro danou oblast.

## Úvahy pro vysoce kvalitní zážitek z AI-poháněného chatu

Tato část shrnuje kritéria „vysoce kvalitních“ chatovacích aplikací, která zahrnují sběr významných metrik a dodržování rámce, jenž odpovědně využívá AI technologii.

### Klíčové metriky

K udržení vysoké kvality výkonu aplikace je nezbytné sledovat klíčové metriky a úvahy. Tyto měření nejen zajišťují funkčnost aplikace, ale také hodnotí kvalitu AI modelu a uživatelský zážitek. Níže je seznam základních metrik AI a metrik uživatelského zážitku, které je třeba zvážit.

| Metrika                      | Definice                                                                                                               | Úvahy pro vývojáře chatu                                              |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Dostupnost (Uptime)**       | Měří čas, po který je aplikace provozuschopná a přístupná uživatelům.                                                  | Jak minimalizujete prostoje?                                          |
| **Doba odezvy**               | Čas, který aplikace potřebuje k odpovědi na dotaz uživatele.                                                            | Jak optimalizovat zpracování dotazu ke zlepšení doby odezvy?         |
| **Přesnost (Precision)**       | Poměr pravdivě pozitivních předpovědí k celkovému počtu pozitivních předpovědí.                                         | Jak ověříte přesnost vašeho modelu?                                  |
| **Zachycení (Recall / citlivost)** | Poměr pravdivě pozitivních předpovědí k skutečnému počtu pozitivních případů.                                          | Jak budete měřit a zlepšovat zachycení?                             |
| **F1 skóre**                  | Harmonický průměr přesnosti a zachycení, který vyvažuje kompromis mezi oběma.                                           | Jaké je vaše cílové F1 skóre? Jak vyvážíte přesnost a zachycení?    |
| **Perplexita**                | Měří, jak dobře pravděpodnostní rozdělení předpovězené modelem odpovídá skutečnému rozdělení dat.                        | Jak minimalizujete perplexitu?                                       |
| **Metriky spokojenosti uživatelů** | Měří vnímání aplikace uživatelem, často zaznamenáváno prostřednictvím průzkumů.                                        | Jak často budete sbírat zpětnou vazbu uživatelů? Jak na ni budete reagovat? |
| **Míra chybovosti (Error Rate)** | Míra, s jakou model dělá chyby při porozumění nebo výstupu.                                                             | Jaké strategie máte pro snížení chybovosti?                         |
| **Cyklus přeškolení**          | Frekvence, s jakou se model aktualizuje, aby zahrnoval nová data a poznatky.                                            | Jak často budete model přeškolovat? Co spustí cyklus přeškolení?    |

| **Detekce anomálií**         | Nástroje a techniky pro identifikaci neobvyklých vzorů, které neodpovídají očekávanému chování.                        | Jak budete reagovat na anomálie?                                        |

### Implementace odpovědných AI praktik v chatovacích aplikacích

Přístup Microsoftu k odpovědné AI identifikoval šest principů, které by měly řídit vývoj a používání AI. Níže jsou uvedeny principy, jejich definice a věci, které by měl tvůrce chatu zvážit a proč by je měl brát vážně.

| Principy              | Definice Microsoftu                                   | Přemýšlení pro vývojáře chatu                                      | Proč je to důležité                                                                     |
| ---------------------- | ----------------------------------------------------- | ------------------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| Spravedlnost          | AI systémy by měly zacházet se všemi lidmi spravedlivě.| Zajistit, aby chatovací aplikace nediskriminovala na základě uživatelských údajů. | Aby se vybudovala důvěra a inkluzivita mezi uživateli; vyhnout se právním důsledkům.                |
| Spolehlivost a bezpečnost | AI systémy by měly fungovat spolehlivě a bezpečně.    | Implementovat testování a záložní opatření ke snížení chyb a rizik. | Zajišťuje spokojenost uživatelů a předchází případným škodám.                                 |
| Soukromí a bezpečnost | AI systémy by měly být zabezpečené a respektovat soukromí. | Implementovat silné šifrování a opatření na ochranu dat.           | K ochraně citlivých uživatelských dat a dodržování zákonů o ochraně soukromí.                         |
| Inkluzivita           | AI systémy by měly posilovat každého a zapojovat lidi. | Navrhnout UI/UX, které je přístupné a snadno použitelné pro různorodé publikum. | Zajišťuje, že široké spektrum lidí může aplikaci efektivně využívat.                   |
| Transparentnost       | AI systémy by měly být srozumitelné.                  | Poskytnout jasnou dokumentaci a vysvětlení pro AI odpovědi.        | Uživatelé mají větší důvěru v systém, pokud rozumí, jak jsou rozhodnutí činěna. |
| Odpovědnost           | Lidé by měli být odpovědní za AI systémy.              | Zavést jasný proces auditů a zlepšování AI rozhodnutí.             | Umožňuje průběžné zlepšování a nápravná opatření v případě chyb.               |

## Zadání

Podívejte se na [zadání](../../../07-building-chat-applications/python). Provede vás sérií cvičení od spuštění prvních chatovacích příkazů, přes klasifikaci a shrnutí textu a další. Všimněte si, že zadání jsou dostupná v různých programovacích jazycích!

## Skvělá práce! Pokračujte v cestě

Po dokončení této lekce se podívejte na naši [kolekci pro Generativní AI učení](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), abyste pokračovali ve zvyšování svých znalostí o generativní AI!

Přejděte na lekci 8, kde uvidíte, jak můžete začít [budovat vyhledávací aplikace](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->