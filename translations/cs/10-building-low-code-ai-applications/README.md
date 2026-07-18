# Vytváření AI aplikací s nízkým kódem

[![Vytváření AI aplikací s nízkým kódem](../../../translated_images/cs/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(Klikněte na obrázek výše pro zhlédnutí videa této lekce)_

## Úvod

Teď, když jsme se naučili, jak vytvářet aplikace generující obrázky, pojďme si promluvit o low code. Generativní AI může být využita v různých oblastech, včetně nízkokódového vývoje, ale co je low code a jak do něj můžeme přidat AI?

Vývoj aplikací a řešení se stal jednodušší pro tradiční vývojáře i nevývojáře díky využití nízkokódových vývojových platforem. Tyto platformy umožňují vytvářet aplikace a řešení s minimálním nebo žádným kódem. Toho je dosaženo poskytnutím vizuálního vývojového prostředí, které umožňuje přetahovat komponenty a stavět aplikace a řešení. To umožňuje vytvářet aplikace rychleji a s menšími zdroji. V této lekci se podrobně zaměříme na to, jak používat low code a jak vylepšit vývoj v low code pomocí AI s využitím Power Platform.

Power Platform poskytuje organizacím příležitost posílit jejich týmy, aby si mohly vytvářet vlastní řešení prostřednictvím intuitivního prostředí s nízkým nebo žádným kódem. Toto prostředí pomáhá zjednodušit proces vytváření řešení. S Power Platform lze řešení vytvořit během dnů či týdnů místo měsíců či let. Power Platform se skládá z pěti hlavních produktů: Power Apps, Power Automate, Power BI, Power Pages a Copilot Studio.

Tato lekce zahrnuje:

- Úvod do generativní AI v Power Platform
- Úvod do Copilota a jak jej používat
- Použití generativní AI pro vytváření aplikací a toků v Power Platform
- Pochopení AI modelů v Power Platform s AI Builder
- Vytváření inteligentních agentů pomocí Microsoft Copilot Studio

## Cíle učení

Na konci této lekce budete schopni:

- Pochopit, jak Copilot funguje v Power Platform.

- Vytvořit aplikaci pro sledování studentských úkolů pro naše vzdělávací startup.

- Vytvořit tok pro zpracování faktur, který používá AI pro extrahování informací z faktur.

- Aplikovat osvědčené postupy při používání AI modelu Create Text with GPT.

- Pochopit, co je Microsoft Copilot Studio a jak s ním vytvářet inteligentní agenty.

Nástroje a technologie, které v této lekci použijete, jsou:

- **Power Apps**, pro aplikaci Student Assignment Tracker, poskytující nízkokódové vývojové prostředí pro vytváření aplikací pro sledování, správu a interakci s daty.

- **Dataverse**, pro ukládání dat aplikace Student Assignment Tracker, kde Dataverse poskytuje nízkokódovou datovou platformu pro ukládání dat aplikace.

- **Power Automate**, pro tok zpracování faktur, kde budete mít nízkokódové vývojové prostředí pro tvorbu pracovních toků k automatizaci procesu zpracování faktur.

- **AI Builder**, pro AI model zpracování faktur, kde použijete předpřipravené AI modely k zpracování faktur pro náš startup.

## Generativní AI v Power Platform

Vylepšení nízkokódového vývoje a aplikací generativní AI je klíčovou oblastí zaměření Power Platform. Cílem je umožnit všem vytvářet AI-poháněné aplikace, weby, přehledy a automatizovat procesy pomocí AI, _aniž by bylo třeba odborných znalostí v datové vědě_. Toho je dosaženo integrací generativní AI do prostředí nízkokódového vývoje v Power Platform ve formě Copilota a AI Builderu.

### Jak to funguje?

Copilot je AI asistent, který vám umožní vytvářet řešení v Power Platform tak, že popíšete své požadavky v několika konverzačních krocích pomocí přirozeného jazyka. Můžete například zadat asistentovi, jaká pole má vaše aplikace používat, a on vytvoří jak aplikaci, tak i podkladový datový model, nebo můžete specifikovat, jak nastavit tok v Power Automate.

Funkce řízené Copilotem můžete použít jako prvek na obrazovkách aplikace, který umožní uživatelům získávat poznatky prostřednictvím konverzačních interakcí.

AI Builder je nízkokódová AI kapacita dostupná v Power Platform, která umožňuje používat AI modely k automatizaci procesů a předpovídání výsledků. Pomocí AI Builderu můžete do svých aplikací a toků přinést AI, která se připojuje k vašim datům v Dataverse nebo v různých cloudových datových zdrojích, jako jsou SharePoint, OneDrive nebo Azure.

Copilot je dostupný ve všech produktech Power Platform: Power Apps, Power Automate, Power BI, Power Pages a Copilot Studio (dříve Power Virtual Agents). AI Builder je dostupný v Power Apps a Power Automate. V této lekci se zaměříme na to, jak používat Copilot a AI Builder v Power Apps a Power Automate k vytvoření řešení pro náš vzdělávací startup.

### Copilot v Power Apps

Součástí Power Platform je Power Apps, který poskytuje nízkokódové vývojové prostředí pro vytváření aplikací pro sledování, správu a interakci s daty. Jedná se o sadu služeb pro vývoj aplikací s škálovatelné datovou platformou a schopností připojit se k cloudovým službám a místním datům. Power Apps umožňuje vytvářet aplikace, které běží v prohlížečích, na tabletech a telefonech a lze je sdílet s kolegy. Power Apps usnadňuje uživatelům vstup do vývoje aplikací jednoduchým rozhraním, takže každý podnikový uživatel či zkušený vývojář může vytvářet vlastní aplikace. Zkušenost s vývojem aplikací je rovněž vylepšena generativní AI prostřednictvím Copilota.

Funkce AI asistenta Copilot v Power Apps vám umožní popsat, jaký typ aplikace potřebujete a jaké informace chcete, aby vaše aplikace sledovala, sbírala nebo zobrazovala. Copilot poté vygeneruje responzivní aplikaci Canvas založenou na vašem popisu. Aplikaci můžete následně přizpůsobit svým potřebám. AI Copilot také vygeneruje a navrhne tabulku Dataverse s poli potřebnými k uložení dat, která chcete sledovat, a s některými ukázkovými daty. V této lekci se později podíváme, co je Dataverse a jak ho lze v Power Apps použít. Tabulku poté můžete přizpůsobit svým potřebám pomocí funkce AI Copilot asistenta přes konverzační kroky. Tato funkce je dostupná přímo z úvodní obrazovky Power Apps.

### Copilot v Power Automate

Součástí Power Platform je Power Automate, který umožňuje uživatelům vytvářet automatizované pracovní toky mezi aplikacemi a službami. Pomáhá automatizovat opakující se obchodní procesy, jako jsou komunikace, sběr dat a schvalování rozhodnutí. Jeho jednoduché rozhraní umožňuje uživatelům různé technické úrovně (od začátečníků po zkušené vývojáře) automatizovat pracovní úkoly. Vývoj pracovních toků je rovněž vylepšen generativní AI prostřednictvím Copilota.

Funkce AI asistenta Copilot v Power Automate vám umožňuje popsat, jaký typ toku potřebujete a jaké akce chcete, aby váš tok vykonával. Copilot poté vytvoří tok na základě vašeho popisu. Tok můžete následně přizpůsobit svým potřebám. AI Copilot také vygeneruje a navrhne akce, které jsou potřeba k provedení úkolu, který chcete automatizovat. V této lekci se později podíváme, co jsou to toky a jak je používat v Power Automate. Akce poté můžete přizpůsobit svým potřebám pomocí funkce AI Copilot asistenta přes konverzační kroky. Tato funkce je dostupná přímo z úvodní obrazovky Power Automate.

## Vytváření inteligentních agentů s Microsoft Copilot Studio

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst) (dříve Power Virtual Agents) je nízkokódový člen Power Platform pro vytváření **AI agentů** — konverzačních copilotů, kteří mohou odpovídat na otázky, provádět akce a automatizovat úkoly jménem vašich uživatelů. Stejně jako zbytek Power Platform tyto agenty vytváříte ve vizuálním prostředí orientovaném na přirozený jazyk: popíšete, co chcete, aby agent dělal, a Copilot Studio pomáhá vytvořit jeho instrukce, znalosti a akce.

Pro náš vzdělávací startup byste mohli vytvořit agenta, který odpovídá na otázky studentů o kurzech, kontroluje termíny úkolů a dokonce posílá e-maily instruktorovi — to vše bez psaní kódu.

Zde jsou některé z nejnovějších schopností, které dělají Copilot Studio mocným:

- **Generativní odpovědi z vašich znalostí**. Místo ručního psaní každé konverzace můžete připojit **zdroje znalostí** — veřejné weby, SharePoint, OneDrive, Dataverse, nahrané soubory nebo podniková data přes konektory — a agent z nich tvoří podložené odpovědi.

- **Generativní orchestraci**. Místo spoléhání na pevné spouštěcí fráze agent využívá AI k pochopení požadavku a dynamicky rozhoduje, jaké znalosti, témata a akce zkombinovat k jeho splnění, včetně propojení několika kroků.

- **Akce a konektory**. Agenti umí *dělat* věci, nejen konverzovat. Můžete agentovi přiřadit akce podporované více než 1 500 předpřipravenými konektory Power Platform, toky Power Automate, vlastními REST API, promptami nebo servery **Model Context Protocol (MCP)**.

- **Autonomní agenti**. Agenti nejsou omezeni na odpovědi v okně chatu. Můžete vytvořit **autonomní agenty**, kteří jsou spouštěni událostmi — jako nový e-mail, nový záznam v Dataverse nebo nahrání souboru — a pak jednat na pozadí k dokončení úkolu.

- **Orchestraci několika agentů**. Agenti mohou volat jiné agenty. Agent v Copilot Studio může předat úkol jinému agentovi nebo být rozšířen dalšími agenty, včetně těch publikovaných do Microsoft 365 Copilot a agentů vytvořených v Microsoft Foundry.

- **Volbu modelu**. Kromě vestavěných modelů můžete přinést modely z katalogu modelů Microsoft Foundry, aby váš agent uvažoval a reagoval podle vašich představ.

- **Publikaci kamkoliv**. Jakmile je agent vytvořen, může být publikován na více kanálech — Microsoft Teams, Microsoft 365 Copilot, internetovou stránku nebo vlastní aplikaci a další — se zabezpečením, autentifikací a analytikou spravovanými přes administrativní prostředí Power Platform.

Můžete začít vytvářet svého prvního agenta na [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst) a dozvědět se více v [dokumentaci Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst).

## Zadání: Správa studentských úkolů a faktur pro náš startup pomocí Copilota

Náš startup nabízí studentům online kurzy. Startup rychle rostl a nyní má problém držet krok s poptávkou po kurzech. Najal vás jako vývojáře Power Platform, abyste jim pomohli vytvořit řešení s nízkým kódem pro správu studentských úkolů a faktur. Jejich řešení by mělo pomoci sledovat a spravovat studentské úkoly přes aplikaci a automatizovat proces zpracování faktur přes pracovní tok. Bylo vám řečeno, abyste k vývoji řešení použili generativní AI.

Když začínáte s Copilotem, můžete využít [Power Platform Copilot Prompt Library](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) k získání předloh promptů. Tato knihovna obsahuje seznam promptů, které můžete používat pro tvorbu aplikací a toků s Copilotem. Promptům v knihovně můžete také využít k inspiraci, jak zadávat požadavky Copilotovi.

### Vytvoření aplikace pro sledování studentských úkolů pro náš startup

Vzdělavatelé v našem startupu mají potíže se sledováním studentských úkolů. Používali tabulku v tabulkovém procesoru, ale jak počet studentů rostl, bylo to těžké spravovat. Požádali vás, abyste vytvořili aplikaci, která jim pomůže sledovat a spravovat studentské úkoly. Aplikace by jim měla umožnit přidávat nové úkoly, zobrazovat úkoly, upravovat úkoly a mazat úkoly. Dále by měla umožnit vzdělavatelům a studentům zobrazit úkoly, které byly ohodnoceny, a ty, které ještě ne.

Aplikaci vytvoříte pomocí Copilota v Power Apps podle níže uvedených kroků:

1. Přejděte na [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) úvodní obrazovku.

1. Použijte textové pole na úvodní obrazovce k popisu aplikace, kterou chcete vytvořit. Například **_Chci vytvořit aplikaci na sledování a správu studentských úkolů_**. Klikněte na tlačítko **Odeslat**, aby se prompt poslal AI Copilotovi.

![Popište aplikaci, kterou chcete vytvořit](../../../translated_images/cs/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. AI Copilot navrhne tabulku Dataverse s poli potřebnými k uložení dat, která chcete sledovat, a s některými ukázkovými daty. Tabulku pak můžete přizpůsobit svým potřebám pomocí funkce AI Copilot asistenta v konverzačních krocích.

   > **Důležité**: Dataverse je základní datová platforma pro Power Platform. Je to nízkokódová datová platforma pro ukládání dat aplikace. Jedná se o plně spravovanou službu, která bezpečně ukládá data v Microsoft Cloudu a je zřízena ve vašem prostředí Power Platform. Nabízí vestavěné schopnosti správy dat, jako je klasifikace dat, sledování původu dat, jemně granulovaný přístup a další. Více o Dataverse se můžete dozvědět [zde](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Navrhovaná pole ve vaší nové tabulce](../../../translated_images/cs/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. Vzdělavatelé chtějí posílat e-maily studentům, kteří odevzdali své úkoly, aby je informovali o průběhu jejich úkolů. Můžete použít Copilota k přidání nového pole do tabulky pro uložení e-mailu studenta. Například můžete použít následující prompt: **_Chci přidat sloupec pro uložení e-mailu studenta_**. Klikněte na tlačítko **Odeslat**, abyste prompt poslali AI Copilotovi.

![Přidání nového pole](../../../translated_images/cs/copilot-new-column.35e15ff21acaf274.webp)

1. AI Copilot vygeneruje nové pole a vy ho můžete přizpůsobit svým potřebám.


1. Jakmile dokončíte tabulku, klikněte na tlačítko **Vytvořit aplikaci** pro vytvoření aplikace.

1. AI Copilot vygeneruje responzivní Canvas aplikaci na základě vašeho popisu. Poté můžete aplikaci přizpůsobit podle svých potřeb.

1. Pro pedagogy, kteří chtějí posílat e-maily studentům, můžete použít Copilot k přidání nové obrazovky do aplikace. Například můžete použít následující instrukci k přidání nové obrazovky do aplikace: **_Chci přidat obrazovku pro odesílání e-mailů studentům_**. Klikněte na tlačítko **Odeslat** pro odeslání instrukce AI Copilotovi.

![Přidání nové obrazovky pomocí instrukce](../../../translated_images/cs/copilot-new-screen.2e0bef7132a17392.webp)

1. AI Copilot vygeneruje novou obrazovku a poté ji můžete přizpůsobit podle svých potřeb.

1. Jakmile dokončíte aplikaci, klikněte na tlačítko **Uložit** pro uložení aplikace.

1. Pro sdílení aplikace s pedagogy klikněte na tlačítko **Sdílet** a poté znovu klikněte na tlačítko **Sdílet**. Poté můžete aplikaci sdílet s pedagogy zadáním jejich e-mailových adres.

> **Vaše domácí úloha**: Aplikace, kterou jste právě vytvořili, je dobrý start, ale může být vylepšena. U funkce e-mailů mohou pedagogové posílat e-maily studentům pouze ručně, kdy musí vyťukat jejich e-mailové adresy. Můžete použít Copilot k vytvoření automatizace, která umožní pedagogům odesílat e-maily studentům automaticky, když odevzdají své úkoly? Nápověda: s vhodnou instrukcí můžete použít Copilot v Power Automate k vytvoření toho.

### Vytvořte tabulku informací o fakturách pro náš startup

Finanční tým našeho startupu měl potíže s evidencí faktur. Používali tabulkový procesor k evidenci faktur, ale jak počet faktur rostl, správa se stala obtížnou. Požádali vás, abyste vytvořili tabulku, která jim pomůže ukládat, sledovat a spravovat informace o přijatých fakturách. Tabulka by měla být použita k vytvoření automatizace, která extrahuje všechny informace z faktur a uloží je do tabulky. Tabulka by také měla umožnit finančnímu týmu zobrazit faktury, které již byly zaplaceny, a ty, které zaplaceny nebyly.

Power Platform obsahuje podkladovou datovou platformu nazvanou Dataverse, která umožňuje ukládat data pro vaše aplikace a řešení. Dataverse poskytuje low-code datovou platformu pro ukládání dat aplikací. Je to plně spravovaná služba, která bezpečně ukládá data v Microsoft Cloudu a nasazuje se v rámci vašeho prostředí Power Platform. Obsahuje zabudované funkce řízení dat, jako je klasifikace dat, sledování původu dat, přístupová kontrola na základě rolí a další. Více se dozvíte [o Dataverse zde](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Proč bychom měli použít Dataverse pro náš startup? Standardní a vlastní tabulky v Dataverse poskytují bezpečnou a cloudovou možnost ukládání dat. Tabulky vám umožní ukládat různé typy dat, podobně jako používáte více listů v jediném Excelovém sešitu. Můžete používat tabulky k ukládání dat specifických pro vaši organizaci nebo obchodní potřeby. Některé výhody, které náš startup získá používáním Dataverse, zahrnují, ale nejsou omezeny na:

- **Snadná správa**: Metadata i data jsou uložena v cloudu, takže se nemusíte starat o detaily, jak jsou uložena nebo spravována. Můžete se soustředit na vytváření vašich aplikací a řešení.

- **Bezpečnost**: Dataverse poskytuje bezpečnou a cloudovou možnost ukládání vašich dat. Můžete řídit, kdo má k datům ve vašich tabulkách přístup a jakým způsobem pomocí bezpečnosti založené na rolích.

- **Bohatá metadata**: Datové typy a vztahy se používají přímo v Power Apps.

- **Logika a validace**: Můžete používat podniková pravidla, vypočítaná pole a validační pravidla k uplatnění podnikové logiky a zachování přesnosti dat.

Nyní, když víte, co je Dataverse a proč ho používat, podíváme se, jak můžete použít Copilot k vytvoření tabulky v Dataverse, která splní požadavky našeho finančního týmu.

> **Poznámka** : Tuto tabulku použijete v další části pro vytvoření automatizace, která extrahuje všechny informace z faktur a uloží je do tabulky.

Pro vytvoření tabulky v Dataverse pomocí Copilota postupujte podle následujících kroků:

1. Přejděte na domovskou obrazovku [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

2. V levém navigačním panelu vyberte **Tabulky** a poté klikněte na **Popište novou tabulku**.

![Vyberte novou tabulku](../../../translated_images/cs/describe-new-table.0792373eb757281e.webp)

1. Na obrazovce **Popište novou tabulku** využijte textové pole k popisu tabulky, kterou chcete vytvořit. Například **_Chci vytvořit tabulku pro ukládání informací o fakturách_**. Klikněte na tlačítko **Odeslat** pro odeslání instrukce AI Copilotovi.

![Popište tabulku](../../../translated_images/cs/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. AI Copilot navrhne Dataverse tabulku s poli, která potřebujete k ukládání dat, jež chcete sledovat, a ukázkovými daty. Pak můžete tabulku přizpůsobit podle svých potřeb pomocí asistenta AI Copilot prostřednictvím konverzačních kroků.

![Navržená tabulka Dataverse](../../../translated_images/cs/copilot-dataverse-table.b3bc936091324d9d.webp)

1. Finanční tým chce poslat e-mail dodavateli, aby jej informoval o aktuálním stavu jejich faktury. Můžete použít Copilot k přidání nového pole do tabulky pro uložení e-mailu dodavatele. Například můžete použít následující instrukci pro přidání nového pole do tabulky: **_Chci přidat sloupec pro ukládání e-mailu dodavatele_**. Klikněte na tlačítko **Odeslat** pro odeslání instrukce AI Copilotovi.

1. AI Copilot vygeneruje nové pole a pak jej můžete přizpůsobit podle svých potřeb.

1. Jakmile dokončíte tabulku, klikněte na tlačítko **Vytvořit** pro vytvoření tabulky.

## AI modely v Power Platform s AI Builder

AI Builder je low-code AI funkce dostupná v Power Platform, která vám umožňuje používat AI modely k automatizaci procesů a předpovídání výsledků. S AI Builderem můžete do svých aplikací a toků přidat umělou inteligenci, která se připojuje k datům v Dataverse nebo různým cloudovým zdrojům dat, jako je SharePoint, OneDrive nebo Azure.

## Předpřipravené AI modely vs Vlastní AI modely

AI Builder poskytuje dva typy AI modelů: Předpřipravené AI modely a Vlastní AI modely. Předpřipravené AI modely jsou hotové AI modely, které vyškolil Microsoft a jsou k dispozici v Power Platform. Pomáhají vám přidat inteligenci do vašich aplikací a toků bez nutnosti shromažďovat data a poté vytvářet, trénovat a publikovat vlastní modely. Tyto modely můžete využívat k automatizaci procesů a předpovídání výsledků.

Některé z předpřipravených AI modelů dostupných v Power Platform zahrnují:

- **Extrahování klíčových frází**: Tento model extrahuje klíčové fráze z textu.
- **Detekce jazyka**: Tento model rozpoznává jazyk textu.
- **Analýza sentimentu**: Tento model určuje, zda je text pozitivní, negativní, neutrální nebo smíšený.
- **Čtečka vizitek**: Tento model extrahuje informace z vizitek.
- **Rozpoznávání textu**: Tento model extrahuje text z obrázků.
- **Detekce objektů**: Tento model detekuje a extrahuje objekty z obrázků.
- **Zpracování dokumentů**: Tento model extrahuje informace z formulářů.
- **Zpracování faktur**: Tento model extrahuje informace z faktur.

Pomocí Vlastních AI modelů můžete přinést svůj vlastní model do AI Builderu, aby fungoval jako jakýkoli vlastní model AI Builderu, což vám umožňuje trénovat model s vlastními daty. Tyto modely můžete použít k automatizaci procesů a předpovídání výsledků v Power Apps i Power Automate. Při používání vlastního modelu platí určitá omezení. Více o těchto [omezeních](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

![AI Builder modely](../../../translated_images/cs/ai-builder-models.8069423b84cfc47f.webp)

## Úkol č. 2 - Vytvořte tok zpracování faktur pro náš startup

Finanční tým měl potíže se zpracováním faktur. Používali tabulkový procesor k evidenci faktur, ale s rostoucím počtem to bylo obtížné spravovat. Požádali vás, abyste vytvořili tok, který jim pomůže zpracovávat faktury pomocí AI. Tok by měl umožnit extrahovat informace z faktur a uložit je do tabulky Dataverse. Tok by také měl umožnit odeslat e-mail finančnímu týmu s extrahovanými informacemi.

Nyní, když víte, co je AI Builder a proč jej používat, podíváme se, jak pomocí AI modelu Zpracování faktur v AI Builderu, kterým jsme se již zabývali, vytvořit tok, který pomůže finančnímu týmu zpracovávat faktury.

Pro vytvoření toku, který pomůže finančnímu týmu zpracovávat faktury pomocí AI modelu Zpracování faktur v AI Builderu, postupujte podle níže uvedených kroků:

1. Přejděte na domovskou obrazovku [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst).

2. Použijte textové pole na domovské obrazovce k popisu toku, který chcete vytvořit. Například **_Zpracovat fakturu, když dorazí do mé schránky_**. Klikněte na tlačítko **Odeslat** pro odeslání instrukce AI Copilotovi.

   ![Copilot power automate](../../../translated_images/cs/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. AI Copilot navrhne akce, které potřebujete k provedení úkolu, který chcete automatizovat. Můžete kliknout na tlačítko **Další**, abyste prošli následující kroky.

4. V dalším kroku vás Power Automate vyzve k nastavení konektorů potřebných pro tok. Po dokončení klikněte na tlačítko **Vytvořit tok** pro vytvoření toku.

5. AI Copilot vygeneruje tok, který pak můžete přizpůsobit podle svých potřeb.

6. Aktualizujte spouštěč toku a nastavte **Složku** na složku, kde budou faktury ukládány. Například můžete nastavit složku na **Doručená pošta**. Klikněte na **Zobrazit pokročilé možnosti** a nastavte **Pouze s přílohami** na **Ano**. Tím zajistíte, že tok poběží pouze, když do složky přijde e-mail s přílohou.

7. Odstraňte následující akce z toku: **HTML na text**, **Složit** (Compose), **Složit 2**, **Složit 3** a **Složit 4**, protože je nebudete používat.

8. Odstraňte akci **Podmínka** (Condition) z toku, protože ji nebudete používat. Mělo by to vypadat jako na následujícím screenshotu:

   ![power automate, odebrat akce](../../../translated_images/cs/powerautomate-remove-actions.7216392fe684ceba.webp)

9. Klikněte na tlačítko **Přidat akci** a vyhledejte **Dataverse**. Vyberte akci **Přidat nový řádek**.

10. V akci **Extrahovat informace z faktur** aktualizujte **Složku faktury** (Invoice File), aby ukazovala na **Obsah přílohy** (Attachment Content) z e-mailu. Tím zajistíte, že tok extrahuje informace z přílohy faktury.

11. Vyberte tabulku, kterou jste vytvořili dříve. Například můžete vybrat tabulku **Informace o fakturách**. Vyberte dynamický obsah z předchozí akce k vyplnění následujících polí:

    - ID
    - Částka (Amount)
    - Datum (Date)
    - Název (Name)
    - Status - Nastavte **Status** na **Čeká na vyřízení**.
    - E-mail dodavatele - Použijte dynamický obsah **Od** z triggeru **Když přijde nový e-mail**.

    ![power automate add row](../../../translated_images/cs/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. Jakmile dokončíte tok, klikněte na tlačítko **Uložit** pro uložení toku. Tok můžete otestovat zasláním e-mailu s fakturou do složky, kterou jste nastavili v triggeru.

> **Vaše domácí úloha**: Tok, který jste právě vytvořili je dobrý začátek, nyní musíte vymyslet, jak vytvořit automatizaci, která umožní našemu finančnímu týmu posílat e-mail dodavateli s aktuálním stavem jejich faktury. Nápověda: tok musí běžet, když se změní stav faktury.

## Použijte AI model generování textu v Power Automate

Model Create Text s GPT v AI Builderu vám umožňuje generovat text na základě instrukce a je poháněn službou Microsoft Azure OpenAI. Díky této schopnosti můžete ve svých aplikacích a tocích začlenit technologii GPT (Generative Pre-Trained Transformer) a vytvořit různé automatizované toky a užitečné aplikace.

Modely GPT procházejí rozsáhlým tréninkem na obrovském množství dat, což jim umožňuje produkovat text velmi podobný lidskému jazyku při zadání instrukce. Po integraci s automatizací workflow lze AI modely jako GPT využít ke zefektivnění a automatizaci široké škály úkolů.

Například můžete vytvářet toky, které automaticky generují text pro různé případy použití, jako jsou návrhy e-mailů, popisy produktů a další. Model můžete použít také k tvorbě textu pro různé aplikace, například chatboty a aplikace zákaznické podpory, které umožní agentům zákaznické podpory efektivně a rychle reagovat na dotazy zákazníků.

![vytvořit instrukci](../../../translated_images/cs/create-prompt-gpt.69d429300c2e870a.webp)


Chcete-li se naučit, jak používat tento AI model v Power Automate, projděte si modul [Přidání inteligence pomocí AI Builder a GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Skvělá práce! Pokračujte ve vzdělávání

Po dokončení této lekce si prohlédněte naši [kolekci Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), abyste pokračovali v rozšiřování svých znalostí o generativní AI!

Chcete Copilota více přizpůsobit a využít jeho možnosti naplno? Prozkoumejte [Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) — komunitou přispívanou sbírku instrukcí, agentů, dovedností a konfigurací, která vám pomůže co nejlépe využít GitHub Copilot.

Přejděte k lekci 11, kde se budeme zabývat tím, jak [integrovat Generative AI s Function Calling](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->