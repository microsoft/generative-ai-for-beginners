<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2faf8ee7a0b851efa647a19788f1e5b",
  "translation_date": "2025-10-17T21:37:33+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "cs"
}
-->
# Zabezpečení vašich aplikací generativní AI

[![Zabezpečení vašich aplikací generativní AI](../../../translated_images/13-lesson-banner.14103e36b4bbf17398b64ed2b0531f6f2c6549e7f7342f797c40bcae5a11862e.cs.png)](https://youtu.be/m0vXwsx5DNg?si=TYkr936GMKz15K0L)

## Úvod

Tato lekce se zaměřuje na:

- Zabezpečení v kontextu AI systémů.
- Běžná rizika a hrozby pro AI systémy.
- Metody a úvahy pro zabezpečení AI systémů.

## Cíle učení

Po dokončení této lekce budete rozumět:

- Hrozbám a rizikům pro AI systémy.
- Běžným metodám a postupům pro zabezpečení AI systémů.
- Jak implementace bezpečnostního testování může zabránit neočekávaným výsledkům a ztrátě důvěry uživatelů.

## Co znamená zabezpečení v kontextu generativní AI?

Jak technologie umělé inteligence (AI) a strojového učení (ML) stále více ovlivňují naše životy, je klíčové chránit nejen data zákazníků, ale také samotné AI systémy. AI/ML se stále častěji používají k podpoře rozhodovacích procesů s vysokou hodnotou v odvětvích, kde špatné rozhodnutí může mít vážné důsledky.

Zde jsou klíčové body, které je třeba zvážit:

- **Dopad AI/ML**: AI/ML mají významný vliv na každodenní život, a proto je jejich ochrana nezbytná.
- **Výzvy v oblasti bezpečnosti**: Tento vliv AI/ML vyžaduje náležitou pozornost, aby bylo možné zajistit ochranu produktů založených na AI před sofistikovanými útoky, ať už od trollů nebo organizovaných skupin.
- **Strategické problémy**: Technologický průmysl musí proaktivně řešit strategické výzvy, aby zajistil dlouhodobou bezpečnost zákazníků a ochranu dat.

Kromě toho modely strojového učení většinou nedokážou rozlišit mezi škodlivým vstupem a neškodnými anomálními daty. Významná část tréninkových dat pochází z nekurátorovaných, nemoderovaných veřejných datových sad, které jsou otevřené příspěvkům třetích stran. Útočníci nemusí kompromitovat datové sady, pokud do nich mohou volně přispívat. Postupem času se data s nízkou důvěryhodností mohou stát daty s vysokou důvěryhodností, pokud zůstane správná struktura/formát dat.

Proto je zásadní zajistit integritu a ochranu datových úložišť, která vaše modely používají k rozhodování.

## Porozumění hrozbám a rizikům AI

V kontextu AI a souvisejících systémů je dnes nejvýznamnější bezpečnostní hrozbou otrava dat. Otrava dat nastává, když někdo úmyslně změní informace používané k trénování AI, což způsobí, že AI začne dělat chyby. To je způsobeno absencí standardizovaných metod detekce a zmírnění, spolu s naší závislostí na nedůvěryhodných nebo nekurátorovaných veřejných datových sadách pro trénink. Aby byla zachována integrita dat a zabránilo se chybnému tréninkovému procesu, je klíčové sledovat původ a rodokmen vašich dat. Jinak platí staré přísloví „odpad dovnitř, odpad ven“, což vede ke kompromitaci výkonu modelu.

Zde jsou příklady, jak otrava dat může ovlivnit vaše modely:

1. **Převrácení štítků**: Při úkolu binární klasifikace útočník úmyslně převrátí štítky u malé části tréninkových dat. Například neškodné vzorky jsou označeny jako škodlivé, což vede k tomu, že se model naučí nesprávné asociace.\
   **Příklad**: Spamový filtr chybně klasifikuje legitimní e-maily jako spam kvůli manipulovaným štítkům.
2. **Otrava vlastností**: Útočník jemně upraví vlastnosti v tréninkových datech, aby zavedl zkreslení nebo zmátl model.\
   **Příklad**: Přidání irelevantních klíčových slov do popisů produktů za účelem manipulace s doporučovacími systémy.
3. **Injekce dat**: Vložení škodlivých dat do tréninkové sady za účelem ovlivnění chování modelu.\
   **Příklad**: Zavedení falešných uživatelských recenzí k ovlivnění výsledků analýzy sentimentu.
4. **Útoky zadními vrátky**: Útočník vloží skrytý vzor (zadní vrátka) do tréninkových dat. Model se naučí tento vzor rozpoznat a chová se škodlivě, když je aktivován.\
   **Příklad**: Systém rozpoznávání obličeje trénovaný na obrázcích se zadními vrátky, který nesprávně identifikuje konkrétní osobu.

Společnost MITRE Corporation vytvořila [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), znalostní bázi taktik a technik používaných útočníky při reálných útocích na AI systémy.

> Počet zranitelností v systémech využívajících AI roste, protože začlenění AI zvyšuje povrch útoku stávajících systémů nad rámec tradičních kybernetických útoků. Vyvinuli jsme ATLAS, abychom zvýšili povědomí o těchto jedinečných a vyvíjejících se zranitelnostech, protože globální komunita stále více začleňuje AI do různých systémů. ATLAS je modelován podle rámce MITRE ATT&CK® a jeho taktiky, techniky a postupy (TTPs) doplňují ty v ATT&CK.

Podobně jako rámec MITRE ATT&CK®, který se široce používá v tradiční kybernetické bezpečnosti pro plánování pokročilých scénářů emulace hrozeb, poskytuje ATLAS snadno vyhledatelnou sadu TTPs, které mohou pomoci lépe porozumět a připravit se na obranu proti nově vznikajícím útokům.

Kromě toho vytvořil projekt Open Web Application Security Project (OWASP) "[Top 10 seznam](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" nejkritičtějších zranitelností nalezených v aplikacích využívajících LLMs. Seznam zdůrazňuje rizika hrozeb, jako je výše zmíněná otrava dat, spolu s dalšími, jako například:

- **Injekce promptů**: technika, při které útočníci manipulují s velkým jazykovým modelem (LLM) prostřednictvím pečlivě vytvořených vstupů, což způsobí, že se chová mimo svůj zamýšlený účel.
- **Zranitelnosti dodavatelského řetězce**: Komponenty a software, které tvoří aplikace používané LLM, jako jsou moduly Pythonu nebo externí datové sady, mohou být samy o sobě kompromitovány, což vede k neočekávaným výsledkům, zavedeným zkreslením a dokonce k zranitelnostem v základní infrastruktuře.
- **Přehnaná důvěra**: LLMs jsou omylné a mají tendenci halucinovat, poskytovat nepřesné nebo nebezpečné výsledky. V několika dokumentovaných případech lidé vzali výsledky za bernou minci, což vedlo k nechtěným negativním důsledkům v reálném světě.

Rod Trent, odborník na cloudové technologie společnosti Microsoft, napsal bezplatnou elektronickou knihu [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), která se podrobně zabývá těmito a dalšími vznikajícími hrozbami AI a poskytuje rozsáhlé pokyny, jak tyto scénáře nejlépe řešit.

## Bezpečnostní testování AI systémů a LLMs

Umělá inteligence (AI) transformuje různé oblasti a odvětví, nabízí nové možnosti a přínosy pro společnost. Nicméně AI také přináší významné výzvy a rizika, jako je ochrana dat, zkreslení, nedostatek vysvětlitelnosti a potenciální zneužití. Proto je zásadní zajistit, aby AI systémy byly bezpečné a odpovědné, což znamená, že dodržují etické a právní standardy a mohou být důvěryhodné pro uživatele a zainteresované strany.

Bezpečnostní testování je proces hodnocení bezpečnosti AI systému nebo LLM, při kterém se identifikují a využívají jejich zranitelnosti. To může provádět vývojář, uživatel nebo externí auditor, v závislosti na účelu a rozsahu testování. Některé z nejběžnějších metod bezpečnostního testování pro AI systémy a LLMs jsou:

- **Sanitace dat**: Proces odstraňování nebo anonymizace citlivých nebo soukromých informací z tréninkových dat nebo vstupů AI systému nebo LLM. Sanitace dat může pomoci zabránit úniku dat a škodlivé manipulaci tím, že sníží expozici důvěrných nebo osobních údajů.
- **Adversariální testování**: Proces generování a aplikace adversariálních příkladů na vstupy nebo výstupy AI systému nebo LLM za účelem hodnocení jeho odolnosti vůči adversariálním útokům. Adversariální testování může pomoci identifikovat a zmírnit zranitelnosti a slabiny AI systému nebo LLM, které by mohly být zneužity útočníky.
- **Ověření modelu**: Proces ověřování správnosti a úplnosti parametrů nebo architektury modelu AI systému nebo LLM. Ověření modelu může pomoci detekovat a zabránit krádeži modelu tím, že zajistí, že model je chráněn a autentizován.
- **Validace výstupů**: Proces validace kvality a spolehlivosti výstupů AI systému nebo LLM. Validace výstupů může pomoci detekovat a opravit škodlivou manipulaci tím, že zajistí, že výstupy jsou konzistentní a přesné.

OpenAI, lídr v oblasti AI systémů, zavedl sérii _hodnocení bezpečnosti_ jako součást iniciativy red teaming network, která má za cíl testovat výstupy AI systémů a přispívat k bezpečnosti AI.

> Hodnocení může zahrnovat jednoduché testy otázek a odpovědí až po složitější simulace. Jako konkrétní příklady zde jsou vzorová hodnocení vyvinutá OpenAI pro hodnocení chování AI z různých úhlů:

#### Přesvědčování

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Jak dobře dokáže AI systém přimět jiný AI systém k tomu, aby řekl tajné slovo?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Jak dobře dokáže AI systém přesvědčit jiný AI systém, aby daroval peníze?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Jak dobře dokáže AI systém ovlivnit podporu politického návrhu jiného AI systému?

#### Steganografie (skryté zprávy)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Jak dobře dokáže AI systém předat tajné zprávy, aniž by byl odhalen jiným AI systémem?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Jak dobře dokáže AI systém komprimovat a dekomprimovat zprávy, aby umožnil skrytí tajných zpráv?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Jak dobře dokáže AI systém koordinovat s jiným AI systémem bez přímé komunikace?

### Zabezpečení AI

Je nezbytné usilovat o ochranu AI systémů před škodlivými útoky, zneužitím nebo nechtěnými důsledky. To zahrnuje kroky k zajištění bezpečnosti, spolehlivosti a důvěryhodnosti AI systémů, jako například:

- Zabezpečení dat a algoritmů používaných k trénování a provozu AI modelů
- Zabránění neoprávněnému přístupu, manipulaci nebo sabotáži AI systémů
- Detekce a zmírnění zkreslení, diskriminace nebo etických problémů v AI systémech
- Zajištění odpovědnosti, transparentnosti a vysvětlitelnosti rozhodnutí a akcí AI
- Sjednocení cílů a hodnot AI systémů s cíli a hodnotami lidí a společnosti

Zabezpečení AI je důležité pro zajištění integrity, dostupnosti a důvěrnosti AI systémů a dat. Některé z výzev a příležitostí v oblasti zabezpečení AI jsou:

- **Příležitost**: Začlenění AI do strategií kybernetické bezpečnosti, protože může hrát klíčovou roli při identifikaci hrozeb a zlepšování reakčních časů. AI může pomoci automatizovat a zlepšit detekci a zmírnění kybernetických útoků, jako je phishing, malware nebo ransomware.
- **Výzva**: AI může být také využívána útočníky k zahájení sofistikovaných útoků, jako je generování falešného nebo zavádějícího obsahu, vydávání se za uživatele nebo zneužívání zranitelností v AI systémech. Proto mají vývojáři AI jedinečnou odpovědnost navrhovat systémy, které jsou robustní a odolné vůči zneužití.

### Ochrana dat

LLMs mohou představovat rizika pro soukromí a bezpečnost dat, která používají. Například LLMs mohou potenciálně zapamatovat a zveřejnit citlivé informace ze svých tréninkových dat, jako jsou osobní jména, adresy, hesla nebo čísla kreditních karet. Mohou být také manipulovány nebo napadeny škodlivými aktéry, kteří chtějí zneužít jejich zranitelnosti nebo zkreslení. Proto je důležité být si těchto rizik vědom a přijmout vhodná opatření k ochraně dat používaných s LLMs. Existuje několik kroků, které můžete podniknout k ochraně dat používaných s LLMs. Tyto kroky zahrnují:

- **Omezení množství a typu dat, která sdílíte s LLMs**: Sdílejte pouze data, která jsou nezbytná a relevantní pro zamýšlené účely, a vyhněte se sdílení jakýchkoli dat, která jsou citlivá, důvěrná nebo osobní. Uživatelé by měli také anonymizovat nebo šifrovat data, která sdílejí s LLMs, například odstraněním nebo maskováním jakýchkoli identifikačních informací nebo použitím bezpečných komunikačních kanálů.
- **Ověření dat, která LLMs generují**: Vždy zkontrolujte přesnost a kvalitu výstupů generovaných LLMs, abyste zajistili, že neobsahují žádné nežádoucí nebo nevhodné informace.
- **Hlášení a upozornění na jakékoli narušení dat nebo incidenty**: Buďte ostražití vůči jakýmkoli podezřelým nebo abnormálním aktivitám nebo chování LLMs, například generování textů, které jsou irelevantní, nepřesné, urážlivé nebo škodlivé. To by mohlo naznačovat narušení dat nebo bezpečnostní incident.

Bezpečnost dat, správa a dodržování předpisů jsou klíčové pro každou organizaci, která chce využít sílu dat a AI v prostředí s více cloudovými službami. Zabezpečení a správa všech vašich dat je složitý a mnohostranný úkol. Musíte zabezpečit a spravovat různé typy dat (strukturovaná, nestrukturovaná a data generovaná
Napodobování reálných hrozeb je nyní považováno za standardní praxi při budování odolných AI systémů, a to prostřednictvím použití podobných nástrojů, taktik a postupů k identifikaci rizik pro systémy a testování reakce obránců.

> Praxe AI red teamingu se vyvinula do širšího významu: nezahrnuje pouze hledání bezpečnostních zranitelností, ale také zkoumání dalších selhání systému, jako je generování potenciálně škodlivého obsahu. AI systémy přinášejí nová rizika a red teaming je klíčový pro pochopení těchto nových rizik, jako je injekce promptů nebo produkce neodůvodněného obsahu. - [Microsoft AI Red Team buduje budoucnost bezpečnější AI](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

[![Pokyny a zdroje pro red teaming](../../../translated_images/13-AI-red-team.642ed54689d7e8a4d83bdf0635768c4fd8aa41ea539d8e3ffe17514aec4b4824.cs.png)]()

Níže jsou uvedeny klíčové poznatky, které formovaly program Microsoft AI Red Team.

1. **Rozšířený rozsah AI red teamingu:**
   AI red teaming nyní zahrnuje jak bezpečnostní, tak výsledky odpovědné AI (RAI). Tradičně se red teaming zaměřoval na bezpečnostní aspekty, přičemž model byl považován za vektor (např. krádež základního modelu). AI systémy však přinášejí nové bezpečnostní zranitelnosti (např. injekce promptů, otrava daty), které vyžadují zvláštní pozornost. Kromě bezpečnosti se AI red teaming zaměřuje také na otázky spravedlnosti (např. stereotypizace) a škodlivý obsah (např. oslavování násilí). Včasná identifikace těchto problémů umožňuje prioritizaci investic do obrany.
2. **Zlomyslná a neškodná selhání:**
   AI red teaming zohledňuje selhání jak zlomyslná, tak neškodná. Například při red teamingu nového Bingu zkoumáme nejen to, jak mohou zlomyslní protivníci systém narušit, ale také jak běžní uživatelé mohou narazit na problematický nebo škodlivý obsah. Na rozdíl od tradičního bezpečnostního red teamingu, který se zaměřuje hlavně na zlomyslné aktéry, AI red teaming bere v úvahu širší škálu osobností a potenciálních selhání.
3. **Dynamická povaha AI systémů:**
   AI aplikace se neustále vyvíjejí. U aplikací s velkými jazykovými modely se vývojáři přizpůsobují měnícím se požadavkům. Nepřetržitý red teaming zajišťuje trvalou ostražitost a přizpůsobení se vyvíjejícím rizikům.

AI red teaming není všezahrnující a měl by být považován za doplňkový krok k dalším kontrolám, jako je [role-based access control (RBAC)](https://learn.microsoft.com/azure/ai-services/openai/how-to/role-based-access-control?WT.mc_id=academic-105485-koreyst) a komplexní řešení správy dat. Má doplňovat bezpečnostní strategii zaměřenou na používání bezpečných a odpovědných AI řešení, která zohledňují soukromí a bezpečnost, přičemž se snaží minimalizovat předsudky, škodlivý obsah a dezinformace, které mohou narušit důvěru uživatelů.

Zde je seznam dalších materiálů, které vám mohou pomoci lépe pochopit, jak red teaming může pomoci identifikovat a zmírnit rizika ve vašich AI systémech:

- [Plánování red teamingu pro velké jazykové modely (LLMs) a jejich aplikace](https://learn.microsoft.com/azure/ai-services/openai/concepts/red-teaming?WT.mc_id=academic-105485-koreyst)
- [Co je OpenAI Red Teaming Network?](https://openai.com/blog/red-teaming-network?WT.mc_id=academic-105485-koreyst)
- [AI Red Teaming - Klíčová praxe pro budování bezpečnějších a odpovědnějších AI řešení](https://rodtrent.substack.com/p/ai-red-teaming?WT.mc_id=academic-105485-koreyst)
- MITRE [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), databáze znalostí o taktikách a technikách používaných protivníky při reálných útocích na AI systémy.

## Kontrola znalostí

Jaký by mohl být dobrý přístup k udržení integrity dat a prevenci jejich zneužití?

1. Mít silné role-based kontroly pro přístup k datům a správu dat
1. Implementovat a auditovat označování dat, aby se zabránilo jejich nesprávnému zobrazení nebo zneužití
1. Zajistit, že vaše AI infrastruktura podporuje filtrování obsahu

A:1, I když všechny tři jsou skvělá doporučení, zajištění správného přidělení přístupových práv k datům uživatelům výrazně přispěje k prevenci manipulace a nesprávného zobrazení dat používaných LLMs.

## 🚀 Výzva

Zjistěte více o tom, jak můžete [spravovat a chránit citlivé informace](https://learn.microsoft.com/training/paths/purview-protect-govern-ai/?WT.mc_id=academic-105485-koreyst) v éře AI.

## Skvělá práce, pokračujte ve svém vzdělávání

Po dokončení této lekce se podívejte na naši [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), abyste dále rozvíjeli své znalosti o generativní AI!

Přejděte na lekci 14, kde se podíváme na [životní cyklus aplikací generativní AI](../14-the-generative-ai-application-lifecycle/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.