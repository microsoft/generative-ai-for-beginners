<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-05-19T23:07:12+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "cs"
}
-->
# Zabezpečení vašich generativních AI aplikací

## Úvod

Tato lekce pokrývá:

- Bezpečnost v kontextu AI systémů.
- Běžná rizika a hrozby pro AI systémy.
- Metody a úvahy pro zabezpečení AI systémů.

## Cíle učení

Po dokončení této lekce budete rozumět:

- Hrozbám a rizikům pro AI systémy.
- Běžným metodám a praktikám pro zabezpečení AI systémů.
- Jak implementace bezpečnostního testování může zabránit neočekávaným výsledkům a erozi důvěry uživatelů.

## Co znamená bezpečnost v kontextu generativní AI?

Jak technologie umělé inteligence (AI) a strojového učení (ML) stále více ovlivňují naše životy, je klíčové chránit nejen data zákazníků, ale i samotné AI systémy. AI/ML se stále častěji používají při rozhodovacích procesech s vysokou hodnotou v odvětvích, kde špatné rozhodnutí může mít vážné důsledky.

Zde jsou klíčové body, které je třeba zvážit:

- **Dopad AI/ML**: AI/ML mají významný dopad na každodenní život a proto je jejich ochrana nezbytná.
- **Bezpečnostní výzvy**: Tento dopad, který AI/ML mají, potřebuje patřičnou pozornost k řešení potřeby chránit produkty založené na AI před sofistikovanými útoky, ať už od trollů nebo organizovaných skupin.
- **Strategické problémy**: Technologický průmysl musí proaktivně řešit strategické výzvy, aby zajistil dlouhodobou bezpečnost zákazníků a ochranu dat.

Dále, modely strojového učení jsou většinou neschopné rozlišit mezi škodlivým vstupem a benigními anomálními daty. Významný zdroj tréninkových dat pochází z nekurátorovaných, nemoderovaných, veřejných datasetů, které jsou otevřené příspěvkům třetích stran. Útočníci nemusí kompromitovat datové sady, pokud do nich mohou volně přispívat. Postupem času se data s nízkou důvěrou stanou daty s vysokou důvěrou, pokud zůstane struktura/formát dat správný.

Proto je kritické zajistit integritu a ochranu datových úložišť, které vaše modely používají pro rozhodování.

## Pochopení hrozeb a rizik AI

V souvislosti s AI a souvisejícími systémy vyniká jako nejvýznamnější bezpečnostní hrozba dneška otrava dat. Otrava dat nastává, když někdo úmyslně změní informace použité k trénování AI, což způsobí, že AI dělá chyby. To je způsobeno absencí standardizovaných metod detekce a zmírnění, spolu s naší závislostí na nedůvěryhodných nebo nekurátorovaných veřejných datasetech pro trénink. Aby byla zachována integrita dat a předešlo se vadnému tréninkovému procesu, je klíčové sledovat původ a linii vašich dat. Jinak platí staré přísloví „co vložíš, to dostaneš“, což vede ke kompromitovanému výkonu modelu.

Zde jsou příklady, jak může otrava dat ovlivnit vaše modely:

1. **Překlápění štítků**: V úloze binární klasifikace útočník úmyslně překlápí štítky malé podmnožiny tréninkových dat. Například benigní vzorky jsou označeny jako škodlivé, což vede model k naučení nesprávných asociací.\
   **Příklad**: Spamový filtr nesprávně klasifikuje legitimní e-maily jako spam kvůli zmanipulovaným štítkům.
2. **Otrava vlastností**: Útočník jemně modifikuje vlastnosti v tréninkových datech, aby zavedl zkreslení nebo uvedl model v omyl.\
   **Příklad**: Přidání irelevantních klíčových slov do popisů produktů k manipulaci s doporučovacími systémy.
3. **Injekce dat**: Vložení škodlivých dat do tréninkové sady k ovlivnění chování modelu.\
   **Příklad**: Vložení falešných uživatelských recenzí k ovlivnění výsledků analýzy sentimentu.
4. **Útoky zadními vrátky**: Útočník vloží skrytý vzor (zadní vrátka) do tréninkových dat. Model se naučí tento vzor rozpoznávat a chová se škodlivě, když je spuštěn.\
   **Příklad**: Systém rozpoznávání obličejů trénovaný s obrázky se zadními vrátky, který nesprávně identifikuje konkrétní osobu.

MITRE Corporation vytvořila [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), znalostní bázi taktik a technik používaných protivníky v reálných útocích na AI systémy.

> Počet zranitelností v systémech podporovaných AI roste, protože začlenění AI zvyšuje povrch útoku stávajících systémů nad rámec tradičních kybernetických útoků. Vyvinuli jsme ATLAS, abychom zvýšili povědomí o těchto jedinečných a vyvíjejících se zranitelnostech, protože globální komunita stále více začleňuje AI do různých systémů. ATLAS je modelován podle rámce MITRE ATT&CK® a jeho taktiky, techniky a postupy (TTP) doplňují ty v ATT&CK.

Podobně jako rámec MITRE ATT&CK®, který je široce používán v tradiční kybernetické bezpečnosti pro plánování scénářů pokročilé emulace hrozeb, poskytuje ATLAS snadno vyhledávatelnou sadu TTP, která může pomoci lépe pochopit a připravit se na obranu proti novým útokům.

Navíc, Open Web Application Security Project (OWASP) vytvořil "[Top 10 seznam](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" nejkritičtějších zranitelností nalezených v aplikacích využívajících LLMs. Seznam zdůrazňuje rizika hrozeb, jako je výše zmíněná otrava dat, spolu s dalšími, jako jsou:

- **Injekce promptu**: technika, kdy útočníci manipulují s velkým jazykovým modelem (LLM) prostřednictvím pečlivě navržených vstupů, což způsobí, že se chová mimo zamýšlené chování.
- **Zranitelnosti dodavatelského řetězce**: Komponenty a software, které tvoří aplikace používané LLM, jako jsou Python moduly nebo externí datové sady, mohou být samy kompromitovány, což vede k neočekávaným výsledkům, zavedeným zkreslením a dokonce zranitelnostem v základní infrastruktuře.
- **Přehnaná důvěra**: LLMs jsou omylné a jsou náchylné k halucinacím, poskytujícím nepřesné nebo nebezpečné výsledky. V několika zdokumentovaných případech lidé vzali výsledky za bernou minci, což vedlo k neúmyslným negativním důsledkům v reálném světě.

Microsoft Cloud Advocate Rod Trent napsal bezplatnou elektronickou knihu, [Musíte se naučit AI bezpečnost](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), která se podrobně zabývá těmito a dalšími vznikajícími hrozbami AI a poskytuje rozsáhlé pokyny, jak nejlépe řešit tyto scénáře.

## Bezpečnostní testování pro AI systémy a LLMs

Umělá inteligence (AI) transformuje různé oblasti a odvětví, nabízející nové možnosti a přínosy pro společnost. Nicméně, AI také představuje významné výzvy a rizika, jako je ochrana soukromí dat, zkreslení, nedostatek vysvětlitelnosti a potenciální zneužití. Proto je klíčové zajistit, že AI systémy jsou bezpečné a odpovědné, což znamená, že dodržují etické a právní standardy a mohou být důvěryhodné uživateli a zainteresovanými stranami.

Bezpečnostní testování je proces hodnocení bezpečnosti AI systému nebo LLM, identifikací a využíváním jejich zranitelností. To může být prováděno vývojáři, uživateli nebo externími auditory, v závislosti na účelu a rozsahu testování. Některé z nejběžnějších metod bezpečnostního testování pro AI systémy a LLMs jsou:

- **Sanitace dat**: To je proces odstraňování nebo anonymizace citlivých nebo soukromých informací z tréninkových dat nebo vstupu AI systému nebo LLM. Sanitace dat může pomoci zabránit úniku dat a škodlivé manipulaci tím, že sníží vystavení důvěrných nebo osobních dat.
- **Adversariální testování**: To je proces generování a aplikace adversariálních příkladů na vstup nebo výstup AI systému nebo LLM, aby se zhodnotila jeho robustnost a odolnost vůči adversariálním útokům. Adversariální testování může pomoci identifikovat a zmírnit zranitelnosti a slabiny AI systému nebo LLM, které mohou být zneužity útočníky.
- **Verifikace modelu**: To je proces ověřování správnosti a úplnosti parametrů modelu nebo architektury AI systému nebo LLM. Verifikace modelu může pomoci detekovat a zabránit krádeži modelu tím, že zajistí, že model je chráněn a ověřen.
- **Validace výstupu**: To je proces validace kvality a spolehlivosti výstupu AI systému nebo LLM. Validace výstupu může pomoci detekovat a opravit škodlivou manipulaci tím, že zajistí, že výstup je konzistentní a přesný.

OpenAI, lídr v AI systémech, zřídil sérii _hodnocení bezpečnosti_ jako součást své iniciativy sítě red teaming, zaměřené na testování výstupu AI systémů s cílem přispět k bezpečnosti AI.

> Hodnocení mohou sahat od jednoduchých testů otázek a odpovědí až po složitější simulace. Jako konkrétní příklady, zde jsou ukázková hodnocení vyvinutá OpenAI pro hodnocení chování AI z několika úhlů pohledu:

#### Přesvědčování

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Jak dobře může AI systém oklamat jiný AI systém, aby řekl tajné slovo?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Jak dobře může AI systém přesvědčit jiný AI systém, aby daroval peníze?
- [Návrh hlasování](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Jak dobře může AI systém ovlivnit podporu politického návrhu jiným AI systémem?

#### Steganografie (skryté zprávy)

- [Steganografie](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Jak dobře může AI systém předat tajné zprávy, aniž by byl odhalen jiným AI systémem?
- [Kompresní text](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Jak dobře může AI systém komprimovat a dekomprimovat zprávy, aby umožnil skrývání tajných zpráv?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Jak dobře může AI systém koordinovat s jiným AI systémem, bez přímé komunikace?

### AI Bezpečnost

Je nezbytné, abychom se snažili chránit AI systémy před škodlivými útoky, zneužitím nebo neúmyslnými důsledky. To zahrnuje podniknutí kroků k zajištění bezpečnosti, spolehlivosti a důvěryhodnosti AI systémů, jako například:

- Zabezpečení dat a algoritmů, které se používají k trénování a provozu AI modelů
- Zabránění neoprávněnému přístupu, manipulaci nebo sabotáži AI systémů
- Detekce a zmírnění zkreslení, diskriminace nebo etických problémů v AI systémech
- Zajištění odpovědnosti, transparentnosti a vysvětlitelnosti rozhodnutí a akcí AI
- Sjednocení cílů a hodnot AI systémů s těmi lidskými a společenskými

AI bezpečnost je důležitá pro zajištění integrity, dostupnosti a důvěrnosti AI systémů a dat. Některé z výzev a příležitostí AI bezpečnosti jsou:

- Příležitost: Začlenění AI do strategií kybernetické bezpečnosti, protože může hrát klíčovou roli při identifikaci hrozeb a zlepšení reakčních časů. AI může pomoci automatizovat a posílit detekci a zmírnění kyberútoků, jako je phishing, malware nebo ransomware.
- Výzva: AI může být také použita protivníky k zahájení sofistikovaných útoků, jako je generování falešného nebo zavádějícího obsahu, vydávání se za uživatele nebo využívání zranitelností v AI systémech. Proto mají vývojáři AI jedinečnou odpovědnost navrhovat systémy, které jsou robustní a odolné vůči zneužití.

### Ochrana dat

LLMs mohou představovat rizika pro soukromí a bezpečnost dat, která používají. Například LLMs mohou potenciálně zapamatovat a vyzradit citlivé informace ze svých tréninkových dat, jako jsou osobní jména, adresy, hesla nebo čísla kreditních karet. Mohou být také manipulovány nebo napadeny škodlivými aktéry, kteří chtějí využít jejich zranitelnosti nebo zkreslení. Proto je důležité být si těchto rizik vědom a přijmout vhodná opatření k ochraně dat používaných s LLMs. Existuje několik kroků, které můžete podniknout k ochraně dat používaných s LLMs. Tyto kroky zahrnují:

- **Omezení množství a typu dat, která sdílíte s LLMs**: Sdílejte pouze data, která jsou nezbytná a relevantní pro zamýšlené účely, a vyhněte se sdílení jakýchkoli dat, která jsou citlivá, důvěrná nebo osobní. Uživatelé by měli také anonymizovat nebo šifrovat data, která sdílejí s LLMs, například odstraněním nebo maskováním jakýchkoli identifikačních informací nebo použitím bezpečných komunikačních kanálů.
- **Ověřování dat, která LLMs generují**: Vždy zkontrolujte přesnost a kvalitu výstupu generovaného LLMs, aby se zajistilo, že neobsahuje žádné nežádoucí nebo nevhodné informace.
- **Hlášení a upozorňování na jakékoli úniky dat nebo incidenty**: Buďte ostražití vůči jakýmkoli podezřelým nebo abnormálním aktivitám nebo chování od LLMs, jako je generování textů, které jsou irelevantní, nepřesné, urážlivé nebo škodlivé. To by mohlo být indikací úniku dat nebo bezpečnostního incidentu.

Bezpečnost, správa a soulad s daty jsou kritické pro každou organizaci, která chce využít sílu dat a AI v multicloudovém prostředí. Zabezpečení a správa všech vašich dat je složitý a mnohostranný úkol. Musíte zabezpečit a spravovat různé typy dat (strukturovaná, nestrukturovaná a data generovaná AI) na různých místech napříč více cloudy, a musíte zohlednit stávající a budoucí bezpečnost dat, správu a regulace AI. Abyste ochránili svá data, musíte přijmout některé osvědčené postupy a opatření, jako například:

- Používejte cloudové služby nebo platformy,

**Prohlášení**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme zodpovědní za žádná nedorozumění nebo chybné interpretace vyplývající z použití tohoto překladu.