# Vytváranie chatovacích aplikácií poháňaných generatívnou AI

[![Vytváranie chatovacích aplikácií poháňaných generatívnou AI](../../../translated_images/sk/07-lesson-banner.a279b937f2843833.webp)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

Teraz, keď sme videli, ako môžeme vytvárať aplikácie na generovanie textu, pozrime sa na chatovacie aplikácie.

Chatovacie aplikácie sa stali súčasťou nášho každodenného života a ponúkajú viac než len prostriedok na bežné konverzácie. Sú neoddeliteľnou súčasťou zákazníckej podpory, technickej pomoci a dokonca aj sofistikovaných poradenských systémov. Pravdepodobne ste nedávno využili pomoc chatovacej aplikácie. Ako do týchto platforiem integrujeme pokročilejšie technológie, ako je generatívna AI, zvyšuje sa ich zložitosť a zároveň aj výzvy.

Niektoré otázky, na ktoré potrebujeme odpoveď, sú:

- **Vytváranie aplikácie**. Ako efektívne vytvoriť a bez problémov integrovať tieto aplikácie poháňané AI pre konkrétne použitia?
- **Monitoring**. Po nasadení, ako môžeme sledovať a zabezpečiť, že aplikácie fungujú na najvyššej úrovni kvality, či už pokiaľ ide o funkčnosť alebo dodržiavanie [šiestich princípov zodpovednej AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

Ako postupujeme ďalej v dobe definovanej automatizáciou a plynulými interakciami medzi človekom a strojom, je nevyhnutné pochopiť, ako generatívna AI mení rozsah, hĺbku a prispôsobivosť chatovacích aplikácií. Táto lekcia preskúma aspekty architektúry podporujúcej tieto zložité systémy, podrobí sa metodikám ich doladenia pre úlohy špecifické pre dané odvetvie a vyhodnotí metriky a úvahy relevantné pre zabezpečenie zodpovedného využitia AI.

## Úvod

Táto lekcia pokrýva:

- Techniky na efektívne vytváranie a integráciu chatovacích aplikácií.
- Ako aplikovať prispôsobenie a doladenie aplikácií.
- Stratégie a úvahy na efektívny monitoring chatovacích aplikácií.

## Ciele učenia

Na konci tejto lekcie budete schopní:

- Opísať úvahy pri vývoji a integrácii chatovacích aplikácií do existujúcich systémov.
- Prispôsobiť chatovacie aplikácie pre konkrétne použitia.
- Identifikovať kľúčové metriky a úvahy na efektívny monitoring a udržanie kvality chatovacích aplikácií poháňaných AI.
- Zabezpečiť zodpovedné využívanie AI v chatovacích aplikáciách.

## Integrácia generatívnej AI do chatovacích aplikácií

Vylepšenie chatovacích aplikácií pomocou generatívnej AI nie je len o tom, aby boli inteligentnejšie; ide aj o optimalizáciu ich architektúry, výkonu a používateľského rozhrania, aby poskytovali kvalitný používateľský zážitok. To zahŕňa skúmanie architektonických základov, integrácie API a úvahy o používateľskom rozhraní. Táto časť má za cieľ ponúknuť vám komplexnú cestovnú mapu pre navigáciu v týchto zložitých oblastiach, či už ich integrujete do existujúcich systémov, alebo tvoríte samostatné platformy.

Na konci tejto časti budete vybavení odbornými znalosťami potrebnými na efektívnu konštrukciu a zaradenie chatovacích aplikácií.

### Chatbot alebo chatovacia aplikácia?

Skôr než sa pustíme do vytvárania chatovacích aplikácií, porovnajme „chatboty“ a „chatovacie aplikácie poháňané AI“, ktoré plnia odlišné úlohy a funkcie. Hlavným účelom chatbota je automatizovať konkrétne konverzačné úlohy, ako je odpovedanie na často kladené otázky alebo sledovanie balíka. Zvyčajne je riadený pravidlovou logikou alebo komplexnými AI algoritmami. Naopak, chatovacia aplikácia poháňaná AI je oveľa rozsiahlejšie prostredie navrhnuté na uľahčenie rôznych foriem digitálnej komunikácie, napríklad textových, hlasových a video chatov medzi ľudskými používateľmi. Jej charakteristickou črtou je integrácia generatívneho AI modelu, ktorý simuluje nuansované, ľudsky znejúce rozhovory a generuje odpovede na základe širokej škály vstupov a kontextových náznakov. Chatovacia aplikácia poháňaná generatívnou AI môže viesť diskusie v otvorenej doméne, prispôsobovať sa meniacim sa konverzačným kontextom a dokonca produkovať kreatívny alebo komplexný dialóg.

Nasledujúca tabuľka načrtáva kľúčové rozdiely a podobnosti, ktoré nám pomáhajú pochopiť ich jedinečné úlohy v digitálnej komunikácii.

| Chatbot                               | Chatovacia aplikácia poháňaná generatívnou AI |
| ------------------------------------- | ---------------------------------------------- |
| Zameraný na úlohy a pravidlami riadený | Citlivý na kontext                            |
| Často integrovaný do väčších systémov  | Môže hostiť jeden alebo viac chatbotov        |
| Obmedzený na programované funkcie       | Zahŕňa modely generatívnej AI                  |
| Špecializované a štruktúrované interakcie | Schopný diskusie v otvorenej doméne          |

### Využitie predpripravených funkcií cez SDK a API

Pri budovaní chatovacej aplikácie je výborným prvým krokom vyhodnotiť, čo už je dostupné. Používanie SDK a API na tvorbu chatovacích aplikácií je výhodná stratégia z viacerých dôvodov. Integráciou dobre dokumentovaných SDK a API strategicky pozicionujete svoju aplikáciu pre dlhodobý úspech, riešiac zároveň otázky škálovateľnosti a údržby.

- **Uľahčuje vývojový proces a redukuje režijné náklady**: Spoľahnutie sa na predpripravené funkcie namiesto nákladného procesu ich vlastnej tvorby vám umožní sústrediť sa na iné časti aplikácie, ktoré môžu byť pre vás dôležitejšie, napríklad na biznis logiku.
- **Lepší výkon**: Pri budovaní funkcií od základov sa nakoniec spýtate: „Ako sa to škáluje? Je táto aplikácia schopná zvládnuť náhly nárast počtu používateľov?“ Dobre udržiavané SDK a API často obsahujú riešenia pre tieto otázky.
- **Jednoduchšia údržba**: Aktualizácie a vylepšenia sa spravujú ľahšie, pretože väčšina API a SDK vyžaduje len aktualizáciu knižnice pri vydaní novšej verzie.
- **Prístup k najmodernejším technológiám**: Využívanie modelov, ktoré boli doladené a trénované na rozsiahlych datasetoch, poskytuje vašej aplikácii schopnosti spracovania prirodzeného jazyka.

Prístup k funkciám SDK alebo API obvykle vyžaduje získanie povolenia na použitie poskytovaných služieb, často prostredníctvom použitia unikátneho kľúča alebo autentifikačného tokenu. Použijeme Python knižnicu OpenAI, aby sme si ukázali, ako toto vyzerá v praxi. Môžete si to tiež vyskúšať sami v nasledujúcom [notebooku pre OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) alebo [notebooku pre Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) pre túto lekciu.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

response = client.responses.create(model="gpt-5-mini", input="Suggest two titles for an instructional lesson on chat applications for generative AI.", store=False)
print(response.output_text)
```

Vyššie uvedený príklad používa model GPT-5 mini s Responses API na dokončenie výzvy, ale všimnite si, že API kľúč je nastavený pred jej začatím. Ak by ste kľúč nenastavili, dostali by ste chybu.

## Používateľská skúsenosť (UX)

Všeobecné zásady UX platia pre chatovacie aplikácie, no tu sú niektoré ďalšie úvahy, ktoré sa stávajú obzvlášť dôležitými vzhľadom na súčasti strojového učenia.

- **Mechanizmus riešenia nejednoznačnosti**: Generatívne AI modely občas generujú nejasné odpovede. Funkcia umožňujúca používateľom žiadať o objasnenie môže byť užitočná, ak na tento problém narazia.
- **Udržiavanie kontextu**: Pokročilé generatívne AI modely majú schopnosť zapamätať si kontext v rámci konverzácie, čo môže byť pre používateľský zážitok nevyhnutné. Poskytnutie možnosti kontrolovať a spravovať kontext používateľom zlepšuje UX, ale zároveň prináša riziko uchovávania citlivých informácií o používateľovi. Úvahy o tom, ako dlho sa tieto informácie uchovávajú, napríklad zavedenie politiky uchovávania, môžu vyvážiť potrebu kontextu a súkromia.
- **Personalizácia**: Vďaka schopnosti učiť sa a adaptovať sa ponúkajú AI modely individualizovaný zážitok pre používateľa. Prispôsobenie používateľského zážitku cez funkcie, ako sú používateľské profily, nielenže používateľovi dáva pocit, že je pochopený, ale zároveň pomáha efektívnejšie a uspokojivejšie nájsť konkrétne odpovede.

Jedným z príkladov personalizácie sú nastavenia „Custom instructions“ v OpenAI ChatGPT. Umožňujú vám poskytnúť informácie o sebe, ktoré môžu byť dôležitým kontextom pre vaše výzvy. Tu je príklad vlastného pokynu.

![Nastavenia vlastných pokynov v ChatGPT](../../../translated_images/sk/custom-instructions.b96f59aa69356fcf.webp)

Tento „profil“ vyzýva ChatGPT na vytvorenie plánu lekcie o spojových zoznamoch. Všimnite si, že ChatGPT zohľadňuje, že používateľ môže chcieť detailnejší plán lekcie na základe svojich skúseností.

![Výzva v ChatGPT na plán lekcie o spojových zoznamoch](../../../translated_images/sk/lesson-plan-prompt.cc47c488cf1343df.webp)

### Microsoft Framework systémových správ pre veľké jazykové modely

[Microsoft poskytol usmernenia](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) pre tvorbu efektívnych systémových správ pri generovaní odpovedí z veľkých jazykových modelov rozdelené do 4 oblastí:

1. Definovanie, pre koho je model určený, ako aj jeho schopností a obmedzení.
2. Definovanie výstupného formátu modelu.
3. Poskytnutie konkrétnych príkladov, ktoré ilustrujú zamýšľané správanie modelu.
4. Poskytnutie doplnkových ochranných opatrení správania.

### Prístupnosť

Či už užívateľ má zrakové, sluchové, motorické alebo kognitívne postihnutia, dobre navrhnutá chatovacia aplikácia by mala byť pre všetkých použiteľná. Nasledujúci zoznam rozdeľuje konkrétne funkcie zamerané na zlepšenie prístupnosti pre rôzne používateľské postihnutia.

- **Funkcie pre zrakové postihnutie**: Vysokokontrastné témy a možnosť meniť veľkosť textu, kompatibilita so screen reader-ami.
- **Funkcie pre sluchové postihnutie**: Text-to-speech a speech-to-text funkcie, vizuálne upozornenia o zvuku.
- **Funkcie pre motorické postihnutie**: Podpora navigácie pomocou klávesnice, hlasové príkazy.
- **Funkcie pre kognitívne postihnutie**: Jednoduchšie jazykové možnosti.

## Prispôsobenie a doladenie pre doménovo špecifické jazykové modely

Predstavte si chatovaciu aplikáciu, ktorá rozumie jazyku vašej firmy a predvída špecifické otázky používateľov. Existuje niekoľko prístupov, ktoré stojí za to spomenúť:

- **Využitie DSL modelov**. DSL znamená doménovo špecifický jazyk. Môžete využiť takzvaný DSL model trénovaný na konkrétnu doménu, aby rozumel jej konceptom a scenárom.
- **Aplikovať doladenie**. Doladenie je proces ďalšieho trénovania modelu s konkrétnymi dátami.

## Prispôsobenie: Použitie DSL

Využitie doménovo špecifických jazykových modelov (DSL Modely) môže zvýšiť angažovanosť používateľov poskytovaním špecializovaných, kontextovo relevantných interakcií. Je to model, ktorý je trénovaný alebo doladený na porozumenie a generovanie textu týkajúceho sa konkrétnej oblasti, priemyslu alebo témy. Možnosti použitia DSL modelu sa líšia od tréningu úplne nového modelu, až po využitie existujúcich cez SDK a API. Ďalšou možnosťou je doladenie, čo zahŕňa prevzatie existujúceho predtrénovaného modelu a jeho prispôsobenie pre konkrétnu doménu.

## Prispôsobenie: Aplikujte doladenie

Doladenie sa často zvažuje, keď predtrénovaný model nestačí v špecializovanej doméne alebo špecifickej úlohe.

Napríklad lekárske otázky sú komplexné a vyžadujú veľa kontextu. Keď lekár stanovuje diagnózu, vychádza z rôznych faktorov, ako je životný štýl či existujúce ochorenia, a môže sa dokonca spoliehať na nedávne lekárske publikácie na overenie diagnózy. V takýchto jemných situáciách nemožno všeobecnú AI chatovaciu aplikáciu považovať za spoľahlivý zdroj.

### Scenár: lekárska aplikácia

Predstavte si chatovaciu aplikáciu určenú na pomoc lekárom tým, že poskytuje rýchle odkazy na liečebné smernice, interakcie liekov alebo najnovšie výskumné zistenia.

Všeobecný model môže byť postačujúci na odpovede na základné lekárske otázky alebo na poskytnutie všeobecných rád, ale môže mať problém s:

- **Veľmi špecifickými alebo zložitými prípadmi**. Napríklad neurológ by mohol aplikáciu požiadať: „Aké sú aktuálne najlepšie postupy na zvládanie farmakorezistentnej epilepsie u detských pacientov?“
- **Nedostatkom najnovších pokrokov**. Všeobecný model by mohol mať problém poskytnúť aktuálnu odpoveď, ktorá zahŕňa najnovší vývoj v neurológii a farmakológii.

V takýchto prípadoch môže doladenie modelu so špecializovaným lekárskym datasetom výrazne zlepšiť jeho schopnosť presnejšie a spoľahlivejšie spracovať tieto zložité lekárske otázky. To vyžaduje prístup k veľkému a relevantnému datasetu, ktorý reprezentuje doménovo špecifické výzvy a otázky, ktoré je potrebné vyriešiť.

## Úvahy pre vysokokvalitný chat poháňaný AI

Táto časť načrtáva kritériá pre „vysokokvalitné“ chatovacie aplikácie, ktoré zahŕňajú zachytávanie merateľných metrík a dodržiavanie rámca, ktorý zodpovedne využíva AI technológiu.

### Kľúčové metriky

Na udržanie vysokokvalitného výkonu aplikácie je dôležité sledovať kľúčové metriky a úvahy. Tieto merania nielen zabezpečujú funkčnosť aplikácie, ale aj hodnotia kvalitu AI modelu a používateľský zážitok. Nižšie je zoznam základných metrík AI a metrík používateľského zážitku, ktoré treba zvážiť.

| Metrika                      | Definícia                                                                                                               | Úvahy pre vývojára chatu                                              |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Dostupnosť (Uptime)**     | Meria čas, počas ktorého je aplikácia dostupná a funkčná pre používateľov.                                              | Ako minimalizujete prestoje?                                          |
| **Doba odozvy**             | Čas, ktorý aplikácia potrebuje na odpoveď používateľovi.                                                               | Ako môžete optimalizovať spracovanie dopytov pre lepšiu odozvu?      |
| **Presnosť (Precision)**    | Pomer pravdivých pozitívnych predpovedí k celkovému počtu pozitívnych predpovedí.                                        | Ako validujete presnosť svojho modelu?                               |
| **Recall (Citlivosť)**      | Pomer pravdivých pozitívnych predpovedí k skutočnému počtu pozitívnych prípadov.                                        | Ako meriate a zlepšujete recall?                                     |
| **F1 skóre**                | Harmonický priemer presnosti a recall, ktorý vyvažuje kompromis medzi oboma.                                            | Aké je vaše cieľové F1 skóre? Ako vyvažujete presnosť a recall?      |
| **Zmätok (Perplexity)**     | Meria, ako dobre pravdepodobnostné rozdelenie predpovedané modelom korešponduje so skutočným rozdelením dát.             | Ako minimalizujete zmätok?                                           |
| **Metriky spokojnosti používateľov** | Meria vnímanie aplikácie používateľmi, často zaznamenávané prostredníctvom prieskumov.                                  | Ako často budete zbierať spätnú väzbu od používateľov? Ako sa podľa nej prispôsobíte? |
| **Miera chýb**              | Miera, s akou model robí chyby pri porozumení alebo výstupe.                                                            | Aké stratégie máte na zníženie chybovosti?                           |
| **Cykly retrénovania**      | Frekvencia, s akou sa model aktualizuje, aby zahrnul nové dáta a poznatky.                                              | Ako často budete model retrénovať? Čo spúšťa retréning?              |

| **Detekcia anomálií**         | Nástroje a techniky na identifikáciu neobvyklých vzorov, ktoré nezodpovedajú očakávanému správaniu.                  | Ako budete reagovať na anomálie?                                         |

### Implementácia zodpovedných AI praktík v chatových aplikáciách

Prístup Microsoftu k zodpovednej AI identifikoval šesť princípov, ktoré by mali viesť vývoj a používanie AI. Nižšie sú uvedené princípy, ich definícia a veci, ktoré by mal chat vývojár zvážiť a prečo by ich mal brať vážne.

| Princípy              | Definícia Microsoftu                                       | Zváženia pre vývojára chatu                                        | Prečo je to dôležité                                                                 |
| --------------------- | --------------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Spravodlivosť          | AI systémy by mali zaobchádzať so všetkými ľuďmi spravodlivo. | Zabezpečiť, aby chatová aplikácia nediskriminovala na základe údajov o používateľovi. | Budovanie dôvery a inkluzivity medzi používateľmi; zabraňuje právnym dôsledkom.       |
| Spoľahlivosť a bezpečnosť | AI systémy by mali fungovať spoľahlivo a bezpečne.          | Zaviesť testovanie a zábezpeky na minimalizáciu chýb a rizík.       | Zaisťuje spokojnosť používateľov a predchádza možným škodám.                           |
| Súkromie a bezpečnosť  | AI systémy by mali byť bezpečné a rešpektovať súkromie.     | Zaviesť silné šifrovanie a opatrenia na ochranu údajov.             | Na ochranu citlivých údajov používateľov a dodržiavanie zákonov o súkromí.            |
| Inkluzívnosť           | AI systémy by mali posilňovať každého a zapájať ľudí.       | Navrhovať UI/UX, ktoré je prístupné a jednoduché na použitie pre rôzne skupiny. | Zabezpečuje, že širšie spektrum ľudí môže aplikáciu efektívne používať.               |
| Transparentnosť        | AI systémy by mali byť zrozumiteľné.                        | Poskytnúť jasnú dokumentáciu a odôvodnenie AI odpovedí.              | Používatelia budú systému viac dôverovať, ak pochopia, ako sa rozhodnutia prijímajú. |
| Zodpovednosť           | Ľudia by mali byť zodpovední za AI systémy.                  | Zaviesť jasný proces na auditovanie a zlepšovanie rozhodnutí AI.    | Umožňuje priebežné zlepšovanie a korekčné opatrenia v prípade chýb.                  |

## Zadanie

Pozrite si [zadanie](../../../07-building-chat-applications/python). Prevedie vás sériou cvičení od spustenia vašich prvých chatovacích výziev, cez klasifikáciu a zhrnutie textu až po ďalšie úlohy. Všimnite si, že zadania sú dostupné v rôznych programovacích jazykoch!

## Skvelá práca! Pokračujte v ceste

Po dokončení tejto lekcie si pozrite našu [kolekciu Generatívnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kde môžete pokračovať v rozvíjaní svojich znalostí o generatívnej AI!

Prejdite na lekciu 8 a zistite, ako môžete začať [vytvárať vyhľadávacie aplikácie](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->