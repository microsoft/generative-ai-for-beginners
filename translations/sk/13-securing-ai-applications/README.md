<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-06-25T21:40:07+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "sk"
}
-->
# Zabezpečenie vašich generatívnych AI aplikácií

[![Zabezpečenie vašich generatívnych AI aplikácií](../../../translated_images/13-lesson-banner.14103e36b4bbf17398b64ed2b0531f6f2c6549e7f7342f797c40bcae5a11862e.sk.png)](https://aka.ms/gen-ai-lesson13-gh?WT.mc_id=academic-105485-koreyst)

## Úvod

Táto lekcia pokryje:

- Bezpečnosť v kontexte AI systémov.
- Bežné riziká a hrozby pre AI systémy.
- Metódy a úvahy o zabezpečení AI systémov.

## Ciele učenia

Po dokončení tejto lekcie budete rozumieť:

- Hrozbám a rizikám pre AI systémy.
- Bežným metódam a praktikám na zabezpečenie AI systémov.
- Ako implementácia bezpečnostného testovania môže zabrániť neočakávaným výsledkom a erózii dôvery používateľov.

## Čo znamená bezpečnosť v kontexte generatívnej AI?

Keďže technológie umelej inteligencie (AI) a strojového učenia (ML) čoraz viac ovplyvňujú naše životy, je dôležité chrániť nielen údaje zákazníkov, ale aj samotné AI systémy. AI/ML sa čoraz viac používa na podporu rozhodovacích procesov s vysokou hodnotou v odvetviach, kde nesprávne rozhodnutie môže mať vážne následky.

Tu sú kľúčové body na zváženie:

- **Vplyv AI/ML**: AI/ML majú významný vplyv na každodenný život a preto je ich ochrana nevyhnutná.
- **Bezpečnostné výzvy**: Tento vplyv AI/ML si vyžaduje náležitú pozornosť, aby sa zabezpečila ochrana produktov založených na AI pred sofistikovanými útokmi, či už zo strany trollov alebo organizovaných skupín.
- **Strategické problémy**: Technologický priemysel musí proaktívne riešiť strategické výzvy, aby zabezpečil dlhodobú bezpečnosť zákazníkov a bezpečnosť údajov.

Okrem toho, modely strojového učenia sú vo veľkej miere neschopné rozlíšiť medzi škodlivým vstupom a neškodnými anomálnymi údajmi. Významným zdrojom tréningových údajov sú nekurátorské, nemoderované verejné datasety, ktoré sú otvorené pre príspevky tretích strán. Útočníci nemusia kompromitovať datasety, keď sú voľní prispievať do nich. Postupom času sa nízko-dôveryhodné škodlivé údaje stávajú vysoko-dôveryhodnými dôveryhodnými údajmi, ak zostane štruktúra/formát údajov správny.

Preto je kritické zabezpečiť integritu a ochranu úložísk údajov, ktoré vaše modely používajú na rozhodovanie.

## Pochopenie hrozieb a rizík AI

Pokiaľ ide o AI a súvisiace systémy, jedným z najvýznamnejších bezpečnostných hrozieb dnes je otravovanie údajov. Otravovanie údajov nastáva, keď niekto úmyselne zmení informácie použité na tréning AI, čo spôsobí chyby. Je to kvôli absencii štandardizovaných metód detekcie a zmierňovania, spojených s našou závislosťou na nedôveryhodných alebo nekurátorských verejných datasetoch na tréning. Na udržanie integrity údajov a zabránenie chybnému tréningovému procesu je kľúčové sledovať pôvod a rodokmeň vašich údajov. Inak platí staré príslovie „odpad dovnútra, odpad von“, čo vedie k ohrozenému výkonu modelu.

Tu sú príklady, ako môže otravovanie údajov ovplyvniť vaše modely:

1. **Prevracanie štítkov**: Pri binárnej klasifikácii útočník úmyselne prevráti štítky malej časti tréningových údajov. Napríklad, neškodné vzorky sú označené ako škodlivé, čo vedie model k učeniu nesprávnych asociácií.\
   **Príklad**: Spamový filter, ktorý nesprávne klasifikuje legitímne e-maily ako spam kvôli manipulovaným štítkom.
2. **Otravovanie funkcií**: Útočník jemne modifikuje funkcie v tréningových údajoch, aby zaviedol zaujatosť alebo zaviedol model.\
   **Príklad**: Pridanie nerelevantných kľúčových slov do popisov produktov na manipuláciu odporúčacích systémov.
3. **Injekcia údajov**: Vloženie škodlivých údajov do tréningovej sady na ovplyvnenie správania modelu.\
   **Príklad**: Zavedenie falošných užívateľských recenzií na skreslenie výsledkov analýzy sentimentu.
4. **Útoky zadnými dverami**: Útočník vloží skrytý vzor (zadné dvere) do tréningových údajov. Model sa naučí rozpoznávať tento vzor a správa sa škodlivo, keď je spustený.\
   **Príklad**: Systém rozpoznávania tváre trénovaný so zadnými dverami, ktorý nesprávne identifikuje konkrétnu osobu.

MITRE Corporation vytvorila [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), znalostnú základňu taktík a techník používaných protivníkmi pri skutočných útokoch na AI systémy.

> Počet zraniteľností v systémoch umožnených AI rastie, pretože začlenenie AI zvyšuje povrch útoku existujúcich systémov nad rámec tradičných kybernetických útokov. Vyvinuli sme ATLAS, aby sme zvýšili povedomie o týchto jedinečných a vyvíjajúcich sa zraniteľnostiach, pretože globálna komunita čoraz viac začleňuje AI do rôznych systémov. ATLAS je modelovaný po rámci MITRE ATT&CK® a jeho taktiky, techniky a postupy (TTP) sú doplnkové k tým v ATT&CK.

Podobne ako rámec MITRE ATT&CK®, ktorý je široko používaný v tradičnej kybernetickej bezpečnosti na plánovanie pokročilých scenárov emulácie hrozieb, ATLAS poskytuje ľahko prehľadávateľnú sadu TTP, ktoré môžu pomôcť lepšie pochopiť a pripraviť sa na obranu proti vznikajúcim útokom.

Okrem toho, projekt Open Web Application Security Project (OWASP) vytvoril "[Top 10 zoznam](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" najkritickejších zraniteľností nájdených v aplikáciách využívajúcich LLMs. Zoznam zdôrazňuje riziká hrozieb, ako je už spomínané otravovanie údajov spolu s inými, ako sú:

- **Injekcia výzvy**: technika, pri ktorej útočníci manipulujú s Veľkým jazykovým modelom (LLM) prostredníctvom starostlivo vytvorených vstupov, čo spôsobí, že sa správa mimo svojho zamýšľaného správania.
- **Zraniteľnosti dodávateľského reťazca**: Komponenty a softvér, ktoré tvoria aplikácie používané LLM, ako sú Python moduly alebo externé datasety, môžu byť sami ohrozené, čo vedie k neočakávaným výsledkom, zavedeným zaujatosťam a dokonca zraniteľnostiam v základnej infraštruktúre.
- **Nadmerná závislosť**: LLM sú omylné a majú tendenciu halucinovať, poskytujúc nepresné alebo nebezpečné výsledky. V niekoľkých zdokumentovaných prípadoch ľudia prijali výsledky ako samozrejmosť, čo viedlo k neúmyselným negatívnym dôsledkom v reálnom svete.

Microsoft Cloud Advocate Rod Trent napísal bezplatnú e-knihu, [Musíte sa naučiť AI bezpečnosť](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), ktorá sa hlboko ponorí do týchto a iných vznikajúcich AI hrozieb a poskytuje rozsiahle pokyny, ako najlepšie riešiť tieto scenáre.

## Bezpečnostné testovanie pre AI systémy a LLM

Umelá inteligencia (AI) transformuje rôzne oblasti a odvetvia, ponúkajúc nové možnosti a výhody pre spoločnosť. Avšak, AI tiež predstavuje významné výzvy a riziká, ako sú ochrana údajov, zaujatosť, nedostatok vysvetliteľnosti a potenciálne zneužitie. Preto je kľúčové zabezpečiť, aby AI systémy boli bezpečné a zodpovedné, čo znamená, že dodržiavajú etické a právne normy a môžu byť dôveryhodné používateľmi a zainteresovanými stranami.

Bezpečnostné testovanie je proces hodnotenia bezpečnosti AI systému alebo LLM, identifikáciou a využívaním ich zraniteľností. To môže byť vykonané vývojármi, používateľmi alebo tretími stranami audítormi, v závislosti od účelu a rozsahu testovania. Niektoré z najbežnejších metód bezpečnostného testovania pre AI systémy a LLM sú:

- **Sanitácia údajov**: Toto je proces odstránenia alebo anonymizácie citlivých alebo súkromných informácií z tréningových údajov alebo vstupu AI systému alebo LLM. Sanitácia údajov môže pomôcť predchádzať úniku údajov a škodlivej manipulácii znížením vystavenia dôverných alebo osobných údajov.
- **Adversariálne testovanie**: Toto je proces generovania a aplikovania adversariálnych príkladov na vstup alebo výstup AI systému alebo LLM na hodnotenie jeho robustnosti a odolnosti voči adversariálnym útokom. Adversariálne testovanie môže pomôcť identifikovať a zmierniť zraniteľnosti a slabiny AI systému alebo LLM, ktoré môžu byť zneužité útočníkmi.
- **Verifikácia modelu**: Toto je proces overovania správnosti a úplnosti parametrov modelu alebo architektúry AI systému alebo LLM. Verifikácia modelu môže pomôcť odhaliť a zabrániť krádeži modelu zabezpečením, že model je chránený a autentifikovaný.
- **Validácia výstupu**: Toto je proces overovania kvality a spoľahlivosti výstupu AI systému alebo LLM. Validácia výstupu môže pomôcť odhaliť a opraviť škodlivú manipuláciu zabezpečením, že výstup je konzistentný a presný.

OpenAI, líder v AI systémoch, zriadil sériu _bezpečnostných hodnotení_ ako súčasť ich iniciatívy red teaming siete, zameranej na testovanie výstupov AI systémov v nádeji, že prispeje k bezpečnosti AI.

> Hodnotenia môžu siahať od jednoduchých testov otázok a odpovedí po zložitejšie simulácie. Ako konkrétne príklady, tu sú vzorové hodnotenia vyvinuté OpenAI na hodnotenie správania AI z viacerých uhlov pohľadu:

#### Presviedčanie

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Ako dobre môže AI systém oklamať iný AI systém, aby povedal tajné slovo?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Ako dobre môže AI systém presvedčiť iný AI systém, aby daroval peniaze?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Ako dobre môže AI systém ovplyvniť podporu iného AI systému pre politický návrh?

#### Steganografia (skryté správy)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Ako dobre môže AI systém preposlať tajné správy bez toho, aby bol odhalený iným AI systémom?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Ako dobre môže AI systém komprimovať a dekomprimovať správy, aby umožnil skrývanie tajných správ?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Ako dobre môže AI systém koordinovať s iným AI systémom bez priamej komunikácie?

### AI bezpečnosť

Je nevyhnutné, aby sme sa snažili chrániť AI systémy pred škodlivými útokmi, zneužitím alebo neúmyselnými dôsledkami. To zahŕňa podniknutie krokov na zabezpečenie bezpečnosti, spoľahlivosti a dôveryhodnosti AI systémov, ako sú:

- Zabezpečenie údajov a algoritmov, ktoré sa používajú na tréning a prevádzku AI modelov
- Zabránanie neoprávnenému prístupu, manipulácii alebo sabotáži AI systémov
- Detekcia a zmiernenie zaujatosti, diskriminácie alebo etických problémov v AI systémoch
- Zabezpečenie zodpovednosti, transparentnosti a vysvetliteľnosti AI rozhodnutí a akcií
- Zladenie cieľov a hodnôt AI systémov s cieľmi ľudí a spoločnosti

AI bezpečnosť je dôležitá pre zabezpečenie integrity, dostupnosti a dôvernosti AI systémov a údajov. Niektoré z výziev a príležitostí AI bezpečnosti sú:

- Príležitosť: Zahrnutie AI do kybernetických bezpečnostných stratégií, pretože môže zohrávať kľúčovú úlohu pri identifikácii hrozieb a zlepšovaní reakčných časov. AI môže pomôcť automatizovať a posilniť detekciu a zmiernenie kybernetických útokov, ako sú phishing, malware alebo ransomware.
- Výzva: AI môže byť tiež použitá protivníkmi na spustenie sofistikovaných útokov, ako je generovanie falošného alebo zavádzajúceho obsahu, zosobňovanie používateľov alebo využívanie zraniteľností v AI systémoch. Preto majú vývojári AI jedinečnú zodpovednosť navrhovať systémy, ktoré sú robustné a odolné voči zneužitiu.

### Ochrana údajov

LLM môžu predstavovať riziká pre súkromie a bezpečnosť údajov, ktoré používajú. Napríklad, LLM môžu potenciálne zapamätať a uniknúť citlivé informácie zo svojich tréningových údajov, ako sú osobné mená, adresy, heslá alebo čísla kreditných kariet. Môžu byť tiež manipulované alebo napadnuté škodlivými aktérmi, ktorí chcú zneužiť ich zraniteľnosti alebo zaujatosť. Preto je dôležité byť si vedomý týchto rizík a prijať vhodné opatrenia na ochranu údajov používaných s LLM. Existuje niekoľko krokov, ktoré môžete podniknúť na ochranu údajov používaných s LLM. Tieto kroky zahŕňajú:

- **Obmedzenie množstva a typu údajov, ktoré zdieľajú s LLM**: Zdieľajte len údaje, ktoré sú nevyhnutné a relevantné pre zamýšľané účely, a vyhnite sa zdieľaniu akýchkoľvek údajov, ktoré sú citlivé, dôverné alebo osobné. Používatelia by mali tiež anonymizovať alebo šifrovať údaje, ktoré zdieľajú s LLM, napríklad odstránením alebo maskovaním akýchkoľvek identifikačných informácií, alebo používaním zabezpečených komunikačných kanálov.
- **Overovanie údajov, ktoré LLM generujú**: Vždy kontrolujte presnosť a kvalitu výstupu generovaného LLM, aby ste sa uistili, že neobsahujú žiadne nežiaduce alebo nevhodné informácie.
- **Nahlasovanie a upozorňovanie na akékoľvek úniky údajov alebo incidenty**: Buďte ostražití voči akýmkoľvek podozrivým alebo

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladania [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vzniknuté v dôsledku použitia tohto prekladu.