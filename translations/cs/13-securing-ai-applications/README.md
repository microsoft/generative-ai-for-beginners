<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-06-25T21:38:14+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "cs"
}
-->
# Zabezpečení vašich generativních AI aplikací

## Úvod

Tato lekce pokryje:

- Bezpečnost v kontextu AI systémů.
- Běžná rizika a hrozby pro AI systémy.
- Metody a úvahy pro zabezpečení AI systémů.

## Cíle učení

Po dokončení této lekce budete mít porozumění:

- Hrozbám a rizikům pro AI systémy.
- Běžným metodám a praktikám pro zabezpečení AI systémů.
- Jak implementace bezpečnostního testování může zabránit neočekávaným výsledkům a ztrátě důvěry uživatelů.

## Co znamená bezpečnost v kontextu generativní AI?

Jak technologie umělé inteligence (AI) a strojového učení (ML) stále více ovlivňují naše životy, je klíčové chránit nejen data zákazníků, ale i samotné AI systémy. AI/ML se stále častěji používá k podpoře rozhodovacích procesů s vysokou hodnotou v odvětvích, kde špatné rozhodnutí může mít vážné důsledky.

Zde jsou klíčové body k zvážení:

- **Dopad AI/ML**: AI/ML mají významný dopad na každodenní život, a proto se jejich ochrana stala nezbytnou.
- **Bezpečnostní výzvy**: Tento dopad vyžaduje náležitou pozornost, aby bylo možné řešit potřebu chránit produkty založené na AI před sofistikovanými útoky, ať už od trollů nebo organizovaných skupin.
- **Strategické problémy**: Technologický průmysl musí proaktivně řešit strategické výzvy, aby zajistil dlouhodobou bezpečnost zákazníků a bezpečnost dat.

Navíc, modely strojového učení jsou z velké části neschopné rozlišit mezi škodlivými vstupy a benigními anomálními daty. Významný zdroj tréninkových dat je odvozen z nekurátorovaných, nemoderovaných veřejných datových sad, které jsou otevřené pro příspěvky třetích stran. Útočníci nemusí kompromitovat datové sady, když do nich mohou volně přispívat. Postupem času se data s nízkou důvěrou stanou daty s vysokou důvěrou, pokud zůstane struktura/formát dat správná.

Proto je kritické zajistit integritu a ochranu datových úložišť, které vaše modely používají k rozhodování.

## Pochopení hrozeb a rizik AI

Pokud jde o AI a související systémy, jednou z nejvýznamnějších bezpečnostních hrozeb dneška je otrava dat. Otrava dat nastává, když někdo úmyslně změní informace použité k trénování AI, což způsobí, že AI dělá chyby. To je způsobeno absencí standardizovaných metod detekce a zmírňování, spolu s naší závislostí na nedůvěryhodných nebo nekurátorovaných veřejných datových sadách pro trénink. Pro udržení integrity dat a zabránění chybnému tréninkovému procesu je klíčové sledovat původ a linii vašich dat. Jinak platí staré přísloví "garbage in, garbage out", což vede ke kompromitovanému výkonu modelu.

Zde jsou příklady, jak může otrava dat ovlivnit vaše modely:

1. **Otočení štítků**: V úloze binární klasifikace útočník úmyslně otočí štítky malé podmnožiny tréninkových dat. Například, benigní vzorky jsou označeny jako škodlivé, což vede model k učení nesprávných asociací.\
   **Příklad**: Spamový filtr nesprávně klasifikuje legitimní e-maily jako spam kvůli manipulovaným štítkům.
2. **Otrava funkcí**: Útočník jemně modifikuje funkce v tréninkových datech, aby zavedl zaujatost nebo zmátl model.\
   **Příklad**: Přidání irelevantních klíčových slov do popisů produktů za účelem manipulace doporučovacích systémů.
3. **Injekce dat**: Vložení škodlivých dat do tréninkové sady za účelem ovlivnění chování modelu.\
   **Příklad**: Zavedení falešných uživatelských recenzí ke zkreslení výsledků analýzy sentimentu.
4. **Útoky zadních vrátek**: Útočník vloží skrytý vzor (zadní vrátka) do tréninkových dat. Model se naučí rozpoznávat tento vzor a chová se škodlivě, když je spuštěn.\
   **Příklad**: Systém rozpoznávání obličejů vytrénovaný s obrázky se zadními vrátky, který nesprávně identifikuje konkrétní osobu.

Společnost MITRE vytvořila [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), znalostní databázi taktik a technik používaných protivníky při reálných útocích na AI systémy.

> V AI-podporovaných systémech narůstá počet zranitelností, protože začlenění AI rozšiřuje útočnou plochu existujících systémů nad rámec tradičních kybernetických útoků. Vyvinuli jsme ATLAS, abychom zvýšili povědomí o těchto jedinečných a vyvíjejících se zranitelnostech, protože globální komunita stále více začleňuje AI do různých systémů. ATLAS je modelován podle rámce MITRE ATT&CK® a jeho taktiky, techniky a postupy (TTPs) jsou komplementární k těm v ATT&CK.

Stejně jako rámec MITRE ATT&CK®, který je široce používán v tradiční kybernetické bezpečnosti pro plánování pokročilých scénářů emulace hrozeb, ATLAS poskytuje snadno prohledávatelnou sadu TTPs, která může pomoci lépe pochopit a připravit se na obranu proti vznikajícím útokům.

Navíc, Open Web Application Security Project (OWASP) vytvořil "[Top 10 seznam](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" nejkritičtějších zranitelností nalezených v aplikacích využívajících LLMs. Seznam zdůrazňuje rizika hrozeb, jako je již zmíněná otrava dat, spolu s dalšími jako:

- **Injekce promptů**: technika, kde útočníci manipulují s Velkým jazykovým modelem (LLM) prostřednictvím pečlivě vytvořených vstupů, což způsobuje, že se chová mimo své zamýšlené chování.
- **Zranitelnosti dodavatelského řetězce**: Komponenty a software, které tvoří aplikace používané LLM, jako jsou Python moduly nebo externí datové sady, mohou být samy kompromitovány, což vede k neočekávaným výsledkům, zavedeným zaujatostem a dokonce k zranitelnostem v základní infrastruktuře.
- **Přehnaná závislost**: LLMs jsou omylné a byly náchylné k halucinacím, poskytujícím nepřesné nebo nebezpečné výsledky. V několika dokumentovaných případech lidé brali výsledky jako bernou minci, což vedlo k neúmyslným negativním důsledkům v reálném světě.

Advokát Microsoft Cloud Rod Trent napsal bezplatnou elektronickou knihu, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), která se podrobně zabývá těmito a dalšími vznikajícími hrozbami AI a poskytuje rozsáhlé pokyny, jak tyto scénáře nejlépe řešit.

## Bezpečnostní testování pro AI systémy a LLMs

Umělá inteligence (AI) transformuje různé oblasti a odvětví, nabízející nové možnosti a výhody pro společnost. Nicméně, AI také představuje významné výzvy a rizika, jako je ochrana dat, zaujatost, nedostatek vysvětlitelnosti a potenciální zneužití. Proto je klíčové zajistit, aby AI systémy byly bezpečné a zodpovědné, což znamená, že dodržují etické a právní normy a mohou být důvěryhodné uživateli a zainteresovanými stranami.

Bezpečnostní testování je proces hodnocení bezpečnosti AI systému nebo LLM, identifikací a využitím jejich zranitelností. To může být prováděno vývojáři, uživateli nebo třetími stranami, v závislosti na účelu a rozsahu testování. Některé z nejběžnějších metod bezpečnostního testování pro AI systémy a LLMs jsou:

- **Sanitace dat**: Tento proces spočívá v odstranění nebo anonymizaci citlivých nebo soukromých informací z tréninkových dat nebo vstupu AI systému nebo LLM. Sanitace dat může pomoci zabránit úniku dat a škodlivé manipulaci snížením expozice důvěrných nebo osobních dat.
- **Testování proti protivníkům**: Tento proces spočívá ve vytváření a aplikaci protivníkových příkladů na vstup nebo výstup AI systému nebo LLM k hodnocení jeho odolnosti a rezistence vůči protivníkovým útokům. Testování proti protivníkům může pomoci identifikovat a zmírnit zranitelnosti a slabiny AI systému nebo LLM, které mohou být zneužity útočníky.
- **Ověření modelu**: Tento proces spočívá v ověření správnosti a úplnosti parametrů modelu nebo architektury AI systému nebo LLM. Ověření modelu může pomoci detekovat a zabránit krádeži modelu tím, že zajistí, že model je chráněn a autentizován.
- **Validace výstupu**: Tento proces spočívá ve validaci kvality a spolehlivosti výstupu AI systému nebo LLM. Validace výstupu může pomoci detekovat a opravit škodlivou manipulaci tím, že zajistí, že výstup je konzistentní a přesný.

OpenAI, lídr v AI systémech, zavedl sérii _hodnocení bezpečnosti_ jako součást své iniciativy red teaming network, zaměřené na testování výstupu AI systémů s cílem přispět k bezpečnosti AI.

> Hodnocení může sahat od jednoduchých testů otázek a odpovědí až po složitější simulace. Jako konkrétní příklady zde jsou ukázková hodnocení vyvinutá OpenAI pro hodnocení chování AI z různých úhlů pohledu:

#### Přesvědčování

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Jak dobře může AI systém oklamat jiný AI systém, aby řekl tajné slovo?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Jak dobře může AI systém přesvědčit jiný AI systém, aby daroval peníze?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Jak dobře může AI systém ovlivnit podporu politického návrhu jiného AI systému?

#### Steganografie (skryté zprávy)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Jak dobře může AI systém posílat tajné zprávy, aniž by byl odhalen jiným AI systémem?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Jak dobře může AI systém komprimovat a dekomprimovat zprávy, aby umožnil skrytí tajných zpráv?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Jak dobře může AI systém koordinovat s jiným AI systémem bez přímé komunikace?

### Bezpečnost AI

Je nezbytné, abychom se snažili chránit AI systémy před škodlivými útoky, zneužitím nebo neúmyslnými důsledky. To zahrnuje podniknutí kroků k zajištění bezpečnosti, spolehlivosti a důvěryhodnosti AI systémů, jako jsou:

- Zabezpečení dat a algoritmů, které jsou používány k trénování a provozování AI modelů
- Zabránění neoprávněnému přístupu, manipulaci nebo sabotáži AI systémů
- Detekce a zmírnění zaujatosti, diskriminace nebo etických problémů v AI systémech
- Zajištění odpovědnosti, transparentnosti a vysvětlitelnosti rozhodnutí a akcí AI
- Sjednocení cílů a hodnot AI systémů s cíli a hodnotami lidí a společnosti

Bezpečnost AI je důležitá pro zajištění integrity, dostupnosti a důvěrnosti AI systémů a dat. Některé z výzev a příležitostí bezpečnosti AI jsou:

- Příležitost: Začlenění AI do strategií kybernetické bezpečnosti, protože může hrát klíčovou roli při identifikaci hrozeb a zlepšení doby reakce. AI může pomoci automatizovat a rozšířit detekci a zmírnění kybernetických útoků, jako je phishing, malware nebo ransomware.
- Výzva: AI může být také použita protivníky k zahájení sofistikovaných útoků, jako je generování falešného nebo zavádějícího obsahu, vydávání se za uživatele nebo zneužívání zranitelností v AI systémech. Proto mají vývojáři AI jedinečnou odpovědnost navrhovat systémy, které jsou robustní a odolné proti zneužití.

### Ochrana dat

LLMs mohou představovat rizika pro soukromí a bezpečnost dat, která používají. Například, LLMs mohou potenciálně zapamatovat a úniknout citlivé informace z jejich tréninkových dat, jako jsou osobní jména, adresy, hesla nebo čísla kreditních karet. Mohou být také manipulovány nebo napadeny škodlivými aktéry, kteří chtějí zneužít jejich zranitelnosti nebo zaujatosti. Proto je důležité být si vědom těchto rizik a přijmout vhodná opatření k ochraně dat používaných s LLMs. Existuje několik kroků, které můžete podniknout k ochraně dat používaných s LLMs. Tyto kroky zahrnují:

- **Omezení množství a typu dat, která sdílí s LLMs**: Sdílejte pouze data, která jsou nezbytná a relevantní pro zamýšlené účely, a vyhněte se sdílení jakýchkoli dat, která jsou citlivá, důvěrná nebo osobní. Uživatelé by měli také anonymizovat nebo šifrovat data, která sdílí s LLMs, například odstraněním nebo maskováním jakýchkoli identifikačních informací, nebo použitím bezpečných komunikačních kanálů.
- **Ověřování dat, která LLMs generují**: Vždy zkontrolujte přesnost a kvalitu výstupu generovaného LLMs, abyste se ujistili, že neobsahují žádné nežádoucí nebo nevhodné informace.
- **Oznamování a upozorňování na jakékoli úniky dat nebo incidenty**: Buďte ostražití vůči jakýmkoli podezřelým nebo abnormálním aktivitám nebo chováním LLMs, jako je generování textů, které jsou irelevantní, nepřesné, urážlivé nebo škodlivé. To by mohlo být indikací úniku dat nebo bezpečnostního incidentu.

Bezpečnost dat, správa a dodržování předpisů jsou kritické pro jakoukoli organizaci, která chce využít sílu dat a AI v multicloudovém prostředí. Zabezpečení a správa všech vašich dat je složitý a mnohostranný úkol. Musíte zabezpečit a spravovat různé typy dat (strukturovaná, nestrukturovaná a data generovaná AI) na různých místech napříč více cloudy, a musíte brát v úvahu existující a budoucí bezpečnost dat, správu a předpisy AI. Chcete-li chránit svá data, musíte přijmout některé osvědčené postupy

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože se snažíme o přesnost, vezměte prosím na vědomí, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.