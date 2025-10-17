<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2faf8ee7a0b851efa647a19788f1e5b",
  "translation_date": "2025-10-17T21:54:43+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "sk"
}
-->
# Zabezpečenie vašich aplikácií generatívnej AI

[![Zabezpečenie vašich aplikácií generatívnej AI](../../../translated_images/13-lesson-banner.14103e36b4bbf17398b64ed2b0531f6f2c6549e7f7342f797c40bcae5a11862e.sk.png)](https://youtu.be/m0vXwsx5DNg?si=TYkr936GMKz15K0L)

## Úvod

Táto lekcia sa zameriava na:

- Bezpečnosť v kontexte AI systémov.
- Bežné riziká a hrozby pre AI systémy.
- Metódy a úvahy na zabezpečenie AI systémov.

## Ciele učenia

Po absolvovaní tejto lekcie budete rozumieť:

- Hrozbám a rizikám pre AI systémy.
- Bežným metódam a postupom na zabezpečenie AI systémov.
- Ako implementácia bezpečnostného testovania môže zabrániť neočakávaným výsledkom a strate dôvery používateľov.

## Čo znamená bezpečnosť v kontexte generatívnej AI?

Keďže technológie umelej inteligencie (AI) a strojového učenia (ML) čoraz viac ovplyvňujú naše životy, je nevyhnutné chrániť nielen údaje zákazníkov, ale aj samotné AI systémy. AI/ML sa čoraz častejšie využíva na podporu rozhodovacích procesov s vysokou hodnotou v odvetviach, kde nesprávne rozhodnutie môže mať vážne následky.

Tu sú kľúčové body, ktoré treba zvážiť:

- **Vplyv AI/ML**: AI/ML majú významný vplyv na každodenný život, a preto sa ich ochrana stáva nevyhnutnou.
- **Bezpečnostné výzvy**: Tento vplyv AI/ML si vyžaduje náležitú pozornosť, aby sa zabezpečila ochrana produktov založených na AI pred sofistikovanými útokmi, či už zo strany trollov alebo organizovaných skupín.
- **Strategické problémy**: Technologický priemysel musí proaktívne riešiť strategické výzvy, aby zabezpečil dlhodobú bezpečnosť zákazníkov a ochranu údajov.

Okrem toho modely strojového učenia vo všeobecnosti nedokážu rozlíšiť medzi škodlivým vstupom a neškodnými anomálnymi údajmi. Významným zdrojom tréningových údajov sú nekurátorské, nemoderované verejné dátové súbory, ktoré sú otvorené príspevkom tretích strán. Útočníci nemusia kompromitovať dátové súbory, keď do nich môžu voľne prispievať. Postupom času sa nízko dôveryhodné škodlivé údaje stávajú vysoko dôveryhodnými údajmi, ak zostane správna štruktúra/formátovanie údajov.

Preto je kritické zabezpečiť integritu a ochranu dátových úložísk, ktoré vaše modely používajú na rozhodovanie.

## Pochopenie hrozieb a rizík AI

V kontexte AI a súvisiacich systémov je dnes najvýznamnejšou bezpečnostnou hrozbou otrava dát. Otrava dát nastáva, keď niekto úmyselne zmení informácie používané na tréning AI, čo spôsobí, že AI robí chyby. Je to spôsobené absenciou štandardizovaných metód detekcie a zmierňovania, spolu s našou závislosťou na nedôveryhodných alebo nekurátorských verejných dátových súboroch na tréning. Na zachovanie integrity údajov a zabránenie chybnému tréningovému procesu je kľúčové sledovať pôvod a rodokmeň vašich údajov. Inak platí staré príslovie „odpad dnu, odpad von“, čo vedie k zhoršeniu výkonu modelu.

Tu sú príklady, ako môže otrava dát ovplyvniť vaše modely:

1. **Prevracanie označení**: Pri úlohe binárnej klasifikácie útočník úmyselne prevráti označenia malej časti tréningových údajov. Napríklad neškodné vzorky sú označené ako škodlivé, čo vedie k tomu, že model sa naučí nesprávne asociácie.\
   **Príklad**: Spamový filter nesprávne klasifikuje legitímne e-maily ako spam kvôli manipulovaným označeniam.
2. **Otrava vlastností**: Útočník jemne upraví vlastnosti v tréningových údajoch, aby zaviedol zaujatosť alebo zavádzal model.\
   **Príklad**: Pridanie irelevantných kľúčových slov do popisov produktov na manipuláciu odporúčacích systémov.
3. **Injekcia dát**: Vloženie škodlivých údajov do tréningového súboru na ovplyvnenie správania modelu.\
   **Príklad**: Zavedenie falošných užívateľských recenzií na skreslenie výsledkov analýzy sentimentu.
4. **Útoky zadných dvierok**: Útočník vloží skrytý vzor (zadné dvierka) do tréningových údajov. Model sa naučí rozpoznávať tento vzor a správa sa škodlivo, keď je aktivovaný.\
   **Príklad**: Systém rozpoznávania tváre trénovaný na obrázkoch so zadnými dvierkami, ktorý nesprávne identifikuje konkrétnu osobu.

Spoločnosť MITRE Corporation vytvorila [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), databázu znalostí o taktikách a technikách používaných protivníkmi pri reálnych útokoch na AI systémy.

> Počet zraniteľností v systémoch podporovaných AI rastie, pretože začlenenie AI zvyšuje povrch útoku existujúcich systémov nad rámec tradičných kybernetických útokov. Vyvinuli sme ATLAS, aby sme zvýšili povedomie o týchto jedinečných a vyvíjajúcich sa zraniteľnostiach, keďže globálna komunita čoraz viac začleňuje AI do rôznych systémov. ATLAS je modelovaný podľa rámca MITRE ATT&CK® a jeho taktiky, techniky a postupy (TTPs) sú doplnkom k tým v ATT&CK.

Podobne ako rámec MITRE ATT&CK®, ktorý sa široko používa v tradičnej kybernetickej bezpečnosti na plánovanie pokročilých scenárov emulácie hrozieb, ATLAS poskytuje ľahko vyhľadávateľnú sadu TTPs, ktoré môžu pomôcť lepšie pochopiť a pripraviť sa na obranu proti vznikajúcim útokom.

Okrem toho projekt Open Web Application Security Project (OWASP) vytvoril "[Top 10 zoznam](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" najkritickejších zraniteľností nájdených v aplikáciách využívajúcich LLMs. Zoznam zdôrazňuje riziká hrozieb, ako je spomínaná otrava dát, spolu s ďalšími, ako napríklad:

- **Injekcia príkazov**: technika, pri ktorej útočníci manipulujú veľký jazykový model (LLM) prostredníctvom starostlivo vytvorených vstupov, čo spôsobí, že sa správa mimo svojho zamýšľaného správania.
- **Zraniteľnosti dodávateľského reťazca**: Komponenty a softvér, ktoré tvoria aplikácie používané LLM, ako napríklad Python moduly alebo externé dátové súbory, môžu byť samy kompromitované, čo vedie k neočakávaným výsledkom, zavedeným zaujatostiam a dokonca zraniteľnostiam v základnej infraštruktúre.
- **Nadmerná dôvera**: LLMs sú omylné a majú tendenciu halucinovať, poskytovať nepresné alebo nebezpečné výsledky. V niekoľkých dokumentovaných prípadoch ľudia brali výsledky ako samozrejmosť, čo viedlo k neúmyselným negatívnym dôsledkom v reálnom svete.

Microsoft Cloud Advocate Rod Trent napísal bezplatnú elektronickú knihu [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), ktorá sa podrobne zaoberá týmito a ďalšími vznikajúcimi hrozbami AI a poskytuje rozsiahle usmernenia, ako najlepšie riešiť tieto scenáre.

## Bezpečnostné testovanie AI systémov a LLMs

Umelá inteligencia (AI) transformuje rôzne oblasti a odvetvia, ponúka nové možnosti a výhody pre spoločnosť. Avšak AI tiež prináša významné výzvy a riziká, ako sú ochrana údajov, zaujatosti, nedostatok vysvetliteľnosti a potenciálne zneužitie. Preto je kľúčové zabezpečiť, aby AI systémy boli bezpečné a zodpovedné, čo znamená, že dodržiavajú etické a právne normy a môžu byť dôveryhodné používateľmi a zainteresovanými stranami.

Bezpečnostné testovanie je proces hodnotenia bezpečnosti AI systému alebo LLM, identifikáciou a využívaním ich zraniteľností. To môže vykonávať vývojári, používatelia alebo nezávislí audítori, v závislosti od účelu a rozsahu testovania. Niektoré z najbežnejších metód bezpečnostného testovania pre AI systémy a LLMs sú:

- **Sanitácia údajov**: Proces odstraňovania alebo anonymizácie citlivých alebo súkromných informácií z tréningových údajov alebo vstupov AI systému alebo LLM. Sanitácia údajov môže pomôcť predchádzať úniku údajov a škodlivej manipulácii znížením expozície dôverných alebo osobných údajov.
- **Adversariálne testovanie**: Proces generovania a aplikácie adversariálnych príkladov na vstupy alebo výstupy AI systému alebo LLM na hodnotenie jeho odolnosti voči adversariálnym útokom. Adversariálne testovanie môže pomôcť identifikovať a zmierniť zraniteľnosti a slabé miesta AI systému alebo LLM, ktoré môžu byť zneužité útočníkmi.
- **Verifikácia modelu**: Proces overovania správnosti a úplnosti parametrov alebo architektúry modelu AI systému alebo LLM. Verifikácia modelu môže pomôcť odhaliť a predchádzať krádeži modelu tým, že zabezpečí ochranu a autentifikáciu modelu.
- **Validácia výstupu**: Proces validácie kvality a spoľahlivosti výstupu AI systému alebo LLM. Validácia výstupu môže pomôcť odhaliť a opraviť škodlivú manipuláciu tým, že zabezpečí konzistentnosť a presnosť výstupu.

OpenAI, líder v oblasti AI systémov, zriadil sériu _hodnotení bezpečnosti_ ako súčasť iniciatívy red teaming siete, zameranej na testovanie výstupov AI systémov s cieľom prispieť k bezpečnosti AI.

> Hodnotenia môžu zahŕňať jednoduché testy otázok a odpovedí až po zložitejšie simulácie. Ako konkrétne príklady, tu sú ukážkové hodnotenia vyvinuté OpenAI na hodnotenie správania AI z rôznych uhlov pohľadu:

#### Presviedčanie

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Ako dobre dokáže AI systém presvedčiť iný AI systém, aby povedal tajné slovo?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Ako dobre dokáže AI systém presvedčiť iný AI systém, aby daroval peniaze?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Ako dobre dokáže AI systém ovplyvniť podporu iného AI systému pre politický návrh?

#### Steganografia (skryté správy)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Ako dobre dokáže AI systém ​​posielať tajné správy bez toho, aby ho odhalil iný AI systém?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Ako dobre dokáže AI systém komprimovať a dekomprimovať správy, aby umožnil skrytie tajných správ?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Ako dobre dokáže AI systém koordinovať s iným AI systémom bez priamej komunikácie?

### Bezpečnosť AI

Je nevyhnutné, aby sme sa snažili chrániť AI systémy pred škodlivými útokmi, zneužitím alebo neúmyselnými dôsledkami. To zahŕňa kroky na zabezpečenie bezpečnosti, spoľahlivosti a dôveryhodnosti AI systémov, ako napríklad:

- Zabezpečenie údajov a algoritmov, ktoré sa používajú na tréning a prevádzku AI modelov
- Predchádzanie neoprávnenému prístupu, manipulácii alebo sabotáži AI systémov
- Detekcia a zmierňovanie zaujatosti, diskriminácie alebo etických problémov v AI systémoch
- Zabezpečenie zodpovednosti, transparentnosti a vysvetliteľnosti rozhodnutí a akcií AI
- Zladenie cieľov a hodnôt AI systémov s cieľmi a hodnotami ľudí a spoločnosti

Bezpečnosť AI je dôležitá pre zabezpečenie integrity, dostupnosti a dôvernosti AI systémov a údajov. Niektoré výzvy a príležitosti bezpečnosti AI sú:

- Príležitosť: Zahrnutie AI do stratégií kybernetickej bezpečnosti, keďže môže zohrávať kľúčovú úlohu pri identifikácii hrozieb a zlepšovaní reakčných časov. AI môže pomôcť automatizovať a zlepšiť detekciu a zmierňovanie kybernetických útokov, ako sú phishing, malware alebo ransomware.
- Výzva: AI môže byť tiež použitá protivníkmi na spustenie sofistikovaných útokov, ako je generovanie falošného alebo zavádzajúceho obsahu, vydávanie sa za používateľov alebo využívanie zraniteľností v AI systémoch. Preto majú vývojári AI jedinečnú zodpovednosť navrhovať systémy, ktoré sú robustné a odolné voči zneužitiu.

### Ochrana údajov

LLMs môžu predstavovať riziká pre súkromie a bezpečnosť údajov, ktoré používajú. Napríklad LLMs môžu potenciálne zapamätať si a zverejniť citlivé informácie zo svojich tréningových údajov, ako sú osobné mená, adresy, heslá alebo čísla kreditných kariet. Môžu byť tiež manipulované alebo napadnuté škodlivými aktérmi, ktorí chcú využiť ich zraniteľnosti alebo zaujatosti. Preto je dôležité byť si vedomý týchto rizík a prijať vhodné opatrenia na ochranu údajov používaných s LLMs. Existuje niekoľko krokov, ktoré môžete podniknúť na ochranu údajov používaných s LLMs. Tieto kroky zahŕňajú:

- **Obmedzenie množstva a typu údajov, ktoré zdieľate s LLMs**: Zdieľajte iba údaje, ktoré sú nevyhnutné a relevantné pre zamýšľané účely, a vyhnite sa zdieľaniu akýchkoľvek údajov, ktoré sú citlivé, dôverné alebo osobné. Používatelia by tiež mali anonymizovať alebo šifrovať údaje, ktoré zdieľajú s LLMs, napríklad odstránením alebo maskovaním akýchkoľvek identifikačných informácií alebo používaním bezpečných komunikačných kanálov.
- **Overenie údajov, ktoré LLMs generujú**: Vždy skontrolujte presnosť a kvalitu výstupu generovaného LLMs, aby ste sa uistili, že neobsahuje žiadne nežiaduce alebo nevhodné informácie.
- **Nahlásenie a upozornenie na akékoľvek narušenie údajov alebo incidenty**: Buďte ostražití
Napodobňovanie hrozieb z reálneho sveta sa teraz považuje za štandardnú prax pri budovaní odolných AI systémov, pričom sa používajú podobné nástroje, taktiky a postupy na identifikáciu rizík pre systémy a testovanie reakcií obrancov.

> Prax AI red teamingu sa vyvinula do rozšíreného významu: nezahŕňa len skúmanie bezpečnostných zraniteľností, ale aj skúmanie iných zlyhaní systému, ako je generovanie potenciálne škodlivého obsahu. AI systémy prinášajú nové riziká a red teaming je kľúčový na pochopenie týchto nových rizík, ako je injekcia promptov a produkcia neodôvodneného obsahu. - [Microsoft AI Red Team buduje budúcnosť bezpečnejšej AI](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

[![Usmernenia a zdroje pre red teaming](../../../translated_images/13-AI-red-team.642ed54689d7e8a4d83bdf0635768c4fd8aa41ea539d8e3ffe17514aec4b4824.sk.png)]()

Nižšie sú uvedené kľúčové poznatky, ktoré formovali program AI Red Team spoločnosti Microsoft.

1. **Rozšírený rozsah AI red teamingu:**
   AI red teaming teraz zahŕňa bezpečnostné aj výsledky zodpovednej AI (RAI). Tradične sa red teaming zameriaval na bezpečnostné aspekty, pričom model bol považovaný za vektor (napr. krádež základného modelu). AI systémy však prinášajú nové bezpečnostné zraniteľnosti (napr. injekcia promptov, otrava), ktoré si vyžadujú osobitnú pozornosť. Okrem bezpečnosti sa AI red teaming zaoberá aj otázkami spravodlivosti (napr. stereotypizácia) a škodlivým obsahom (napr. oslavovanie násilia). Včasná identifikácia týchto problémov umožňuje prioritizáciu investícií do obrany.
2. **Zlomyseľné a neškodné zlyhania:**
   AI red teaming zohľadňuje zlyhania z pohľadu zlomyseľných aj neškodných perspektív. Napríklad pri red teamingu nového Bingu skúmame nielen to, ako môžu zlomyseľní protivníci narušiť systém, ale aj to, ako bežní používatelia môžu naraziť na problematický alebo škodlivý obsah. Na rozdiel od tradičného bezpečnostného red teamingu, ktorý sa zameriava hlavne na zlomyseľných aktérov, AI red teaming berie do úvahy širší rozsah osobností a potenciálnych zlyhaní.
3. **Dynamická povaha AI systémov:**
   AI aplikácie sa neustále vyvíjajú. V aplikáciách veľkých jazykových modelov sa vývojári prispôsobujú meniacim sa požiadavkám. Kontinuálny red teaming zabezpečuje neustálu ostražitosť a prispôsobenie sa vyvíjajúcim sa rizikám.

AI red teaming nie je všezahŕňajúci a mal by sa považovať za doplnkový krok k ďalším kontrolám, ako je [role-based access control (RBAC)](https://learn.microsoft.com/azure/ai-services/openai/how-to/role-based-access-control?WT.mc_id=academic-105485-koreyst) a komplexné riešenia správy dát. Má dopĺňať bezpečnostnú stratégiu, ktorá sa zameriava na používanie bezpečných a zodpovedných AI riešení, ktoré berú do úvahy súkromie a bezpečnosť, pričom sa snažia minimalizovať predsudky, škodlivý obsah a dezinformácie, ktoré môžu narušiť dôveru používateľov.

Tu je zoznam ďalších materiálov na čítanie, ktoré vám môžu pomôcť lepšie pochopiť, ako red teaming môže pomôcť identifikovať a zmierniť riziká vo vašich AI systémoch:

- [Plánovanie red teamingu pre veľké jazykové modely (LLMs) a ich aplikácie](https://learn.microsoft.com/azure/ai-services/openai/concepts/red-teaming?WT.mc_id=academic-105485-koreyst)
- [Čo je OpenAI Red Teaming Network?](https://openai.com/blog/red-teaming-network?WT.mc_id=academic-105485-koreyst)
- [AI Red Teaming - Kľúčová prax pre budovanie bezpečnejších a zodpovednejších AI riešení](https://rodtrent.substack.com/p/ai-red-teaming?WT.mc_id=academic-105485-koreyst)
- MITRE [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), databáza znalostí o taktikách a technikách používaných protivníkmi pri útokoch na AI systémy v reálnom svete.

## Kontrola vedomostí

Aký by mohol byť dobrý prístup k udržaniu integrity dát a prevencii ich zneužitia?

1. Zaviesť silné role-based kontroly pre prístup k dátam a ich správu
1. Implementovať a auditovať označovanie dát na prevenciu ich nesprávneho zobrazenia alebo zneužitia
1. Zabezpečiť, aby vaša AI infraštruktúra podporovala filtrovanie obsahu

A:1, Hoci všetky tri odporúčania sú skvelé, zabezpečenie správnych oprávnení na prístup k dátam pre používateľov výrazne prispeje k prevencii manipulácie a nesprávneho zobrazenia dát používaných LLMs.

## 🚀 Výzva

Prečítajte si viac o tom, ako môžete [spravovať a chrániť citlivé informácie](https://learn.microsoft.com/training/paths/purview-protect-govern-ai/?WT.mc_id=academic-105485-koreyst) v ére AI.

## Skvelá práca, pokračujte v učení

Po dokončení tejto lekcie si pozrite našu [kolekciu učenia o generatívnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste si rozšírili svoje znalosti o generatívnej AI!

Prejdite na lekciu 14, kde sa pozrieme na [životný cyklus aplikácií generatívnej AI](../14-the-generative-ai-application-lifecycle/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.