# Úvod do malých jazykových modelov pre generatívnu AI pre začiatočníkov
Generatívna AI je fascinujúca oblasť umelej inteligencie, ktorá sa zameriava na vytváranie systémov schopných generovať nový obsah. Tento obsah môže zahŕňať texty, obrázky, hudbu až po celé virtuálne prostredia. Jednou z najzaujímavejších aplikácií generatívnej AI sú jazykové modely.

## Čo sú malé jazykové modely?

Malý jazykový model (SLM) predstavuje zmenšenú variantu veľkého jazykového modelu (LLM), ktorý využíva mnohé architektonické princípy a techniky LLM, pričom má výrazne zníženú výpočtovú náročnosť. 

SLM sú podskupinou jazykových modelov navrhnutých na generovanie textu podobného ľudskému. Na rozdiel od ich väčších protějškov, ako je GPT-4, sú SLM kompaktnejšie a efektívnejšie, čo ich robí ideálnymi pre aplikácie s obmedzenými výpočtovými zdrojmi. Napriek menšej veľkosti môžu stále vykonávať rôzne úlohy. Typicky sa SLM vytvárajú kompresiou alebo destiláciou LLM s cieľom zachovať značnú časť pôvodnej funkčnosti a lingvistických schopností modelu. Táto zmena veľkosti modelu znižuje jeho celkovú zložitosť, takže SLM sú efektívnejšie z hľadiska použitia pamäte aj výpočtových požiadaviek. Napriek týmto optimalizáciám môžu SLM vykonávať širokú škálu úloh spracovania prirodzeného jazyka (NLP):

- Generovanie textu: tvorba zmysluplných a kontextovo relevantných viet či odsekov.
- Dokončovanie textu: predikcia a doplnenie viet na základe daného vstupu.
- Preklad: konverzia textu z jedného jazyka do druhého.
- Zhrnutie: skrátenie dlhých textov do kratších, ľahšie stráviteľných súhrnov.

Hoci s určitými kompromismi vo výkone alebo hĺbke porozumenia v porovnaní s väčšími modelmi.

## Ako malé jazykové modely fungujú?
SLM sa trénujú na obrovských množstvách textových dát. Počas tréningu sa učia vzory a štruktúry jazyka, čo im umožňuje generovať text, ktorý je gramaticky správny a kontextovo vhodný. Tréningový proces zahŕňa:

- Zber dát: zhromažďovanie veľkých datasetov textu z rôznych zdrojov.
- Predspracovanie: čistenie a organizovanie dát na vhodnosť na tréning.
- Tréning: použitie strojového učenia na naučenie modelu porozumieť a generovať text.
- Doladenie: úprava modelu na zlepšenie výkonu v konkrétnych úlohách.

Vývoj SLM zodpovedá rastúcej potrebe modelov, ktoré môžu byť nasadené v prostrediach s obmedzenými zdrojmi, ako sú mobilné zariadenia alebo edge computing platformy, kde by plnohodnotné LLM mohli byť nepraktické kvôli svojim vysokým nárokom. Zameraním na efektívnosť SLM vyvažujú výkon s prístupnosťou, čo umožňuje širšiu aplikáciu v rôznych oblastiach.

![slm](../../../translated_images/sk/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Ciele učenia

V tejto lekcii sa snažíme predstaviť vedomosti o SLM a skombinovať ich s Microsoft Phi-3 na naučenie sa rôznych scenárov v textovom obsahu, videní a MoE.

Na konci tejto lekcie by ste mali byť schopní odpovedať na nasledujúce otázky:

- Čo je SLM?
- Aký je rozdiel medzi SLM a LLM?
- Čo je rodina Microsoft Phi-3/3.5?
- Ako spustiť inferenciu s rodinou Microsoft Phi-3/3.5?

Pripravení? Poďme na to.

## Rozdiely medzi veľkými jazykovými modelmi (LLM) a malými jazykovými modelmi (SLM)

LLM aj SLM sú postavené na základných princípoch pravdepodobnostného strojového učenia, nasledujú podobné prístupy v ich architektúre, metódach tréningu, procesoch generovania dát a technikách hodnotenia modelov. Avšak niekoľko kľúčových faktorov tieto dva typy modelov odlišuje.

## Aplikácie malých jazykových modelov

SLM majú široké spektrum využitia, vrátane:

- Chatboty: poskytovanie zákazníckej podpory a interakcia s používateľmi cez konverzačné rozhranie.
- Tvorba obsahu: asistovanie spisovateľom pri generovaní nápadov alebo písaní článkov.
- Vzdelávanie: pomoc študentom pri písaní a učení sa novým jazykom.
- Prístupnosť: vytváranie nástrojov pre osoby so zdravotným postihnutím, napríklad systémy na prevod textu na reč.

**Veľkosť**
  
Hlavný rozdiel medzi LLM a SLM spočíva v rozsahu modelov. LLM, ako je ChatGPT (GPT-4), môže obsahovať odhadovaných 1,76 bilióna parametrov, zatiaľ čo open-source SLM, ako napríklad Mistral 7B, sú navrhnuté s výrazne menším počtom parametrov – približne 7 miliárd. Tento rozdiel je primárne spôsobený architektúrou modelu a procesmi tréningu. Napríklad ChatGPT používa mechanizmus seba-pozornosti v rámci encoder-decoder štruktúry, zatiaľ čo Mistral 7B využíva sliding window attention, čo umožňuje efektívnejší tréning v rámci decoder-only modelu. Táto architektonická odlišnosť má významný dopad na zložitosť a výkon modelov.

**Porozumenie**

SLM sú typicky optimalizované na výkon v špecifických oblastiach, čo ich robí vysoko špecializovanými, ale potenciálne obmedzenými v schopnosti poskytovať všeobecné kontextové porozumenie v rôznych oblastiach vedomostí. Naproti tomu LLM sa snažia simulovať ľudskú inteligenciu na komplexnejšej úrovni. Sú trénované na obrovských, rozmanitých dátach a sú navrhnuté tak, aby dobre fungovali v mnohých oblastiach, ponúkajúc väčšiu všestrannosť a prispôsobivosť. Preto sú LLM vhodnejšie pre širšiu škálu následných úloh, ako sú spracovanie prirodzeného jazyka a programovanie.

**Výpočty**

Tréning a nasadenie LLM sú veľmi náročné na zdroje, často vyžadujú rozsiahlu výpočtovú infraštruktúru vrátane veľkých GPU klastrov. Napríklad trénovanie modelu ako ChatGPT od začiatku môže vyžadovať tisíce GPU počas dlhých časových období. Naopak, SLM, vzhľadom na menší počet parametrov, sú dostupnejšie z hľadiska výpočtových zdrojov. Modely ako Mistral 7B je možné trénovať a spúšťať na lokálnych zariadeniach so strednými GPU možnosťami, hoci tréning stále vyžaduje niekoľko hodín na viacerých GPU.

**Predpojatosť**

Predpojatosť je známy problém LLM, spôsobený najmä povahou tréningových dát. Tieto modely často používajú nespracované, voľne dostupné dáta z internetu, ktoré môžu nedostatočne alebo chybne reprezentovať určité skupiny, zavádzať nesprávne označenia alebo odzrkadľovať jazykové predpojatosťi vyplývajúce z dialektov, geografických variácií či gramatických pravidiel. Okrem toho zložitosť architektúry LLM môže nevhodne zvyšovať predpojatosť, ktorá zostáva nepovšimnutá bez opatrného doladenia. Naopak, SLM, ktoré sú trénované na obmedzenejších, doménovo špecifických datasetoch, sú prirodzene menej náchylné na takéto predsudky, hoci im nie sú úplne imúnne.

**Inferencia**

Menšia veľkosť SLM im poskytuje významnú výhodu v rýchlosti inferencie, čo im umožňuje efektívne generovať výstupy na lokálnom hardvéri bez potreby rozsiahleho paralelného spracovania. Naopak, LLM vzhľadom na veľkosť a náročnosť často vyžadujú značné paralelné výpočtové zdroje na dosiahnutie prijateľných časov inferencie. Prítomnosť viacerých súbežných používateľov ešte viac spomaľuje reakčné časy LLM, najmä pri nasadení vo veľkom meradle.

Zhrnuté, oba LLM aj SLM zdieľajú základný základ v strojovom učení, no výrazne sa líšia vo veľkosti modelu, požiadavkách na zdroje, kontextuálnom porozumení, náchylnosti na predpojatosť a rýchlosti inferencie. Tieto rozdiely odrážajú ich vhodnosť pre rôzne použitia, pričom LLM sú všestrannejšie, ale náročnejšie na zdroje, a SLM ponúkajú špecifickú efektivitu s nižšími výpočtovými požiadavkami.

***Poznámka: V tejto lekcii predstavíme SLM na príklade Microsoft Phi-3 / 3.5.***

## Predstavenie rodiny Phi-3 / Phi-3.5

Rodina Phi-3 / 3.5 sa primárne zameriava na scenáre aplikácií v texte, videní a Agent (MoE):

### Phi-3 / 3.5 Instruct

Hlavne pre generovanie textu, dokončenie chatu a extrakciu informácií z obsahu a podobne.

**Phi-3-mini**

Jazykový model s 3,8 miliardami parametrov je dostupný na Microsoft Foundry, Hugging Face a Ollama. Modely Phi-3 výrazne prekračujú výkon jazykových modelov rovnakej alebo väčšej veľkosti na kľúčových benchmarkoch (pozri čísla benchmarkov nižšie, vyššie čísla sú lepšie). Phi-3-mini prekonáva modely dvojnásobnej veľkosti, zatiaľ čo Phi-3-small a Phi-3-medium prekonávajú väčšie modely, vrátane GPT-3.5.

**Phi-3-small & medium**

S 7 miliardami parametrov Phi-3-small prekonáva GPT-3.5T v rôznych testoch jazyka, uvažovania, kódovania a matematiky.

Phi-3-medium s 14 miliardami parametrov pokračuje v trende a prekonáva Gemini 1.0 Pro.

**Phi-3.5-mini**

Môžeme ho považovať za upgrade Phi-3-mini. Parametre zostávajú nezmenené, no vylepšuje schopnosť podporovať viacero jazykov (podpora viac ako 20 jazykov: arabčina, čínština, čeština, dánčina, holandčina, angličtina, fínčina, francúzština, nemčina, hebrejčina, maďarčina, taliančina, japončina, kórejčina, norčina, poľština, portugalčina, ruština, španielčina, švédčina, thajčina, turečtina, ukrajinčina) a pridáva silnejšiu podporu pre dlhý kontext.

Phi-3.5-mini s 3,8 miliardami parametrov prekonáva jazykové modely rovnakej veľkosti a je porovnateľný s modelmi dvojnásobnej veľkosti.

### Phi-3 / 3.5 Vision

Môžeme si predstaviť model Instruct Phi-3/3.5 ako schopnosť Phi porozumieť, a Vision je to, čo dáva Phi oči na porozumenie sveta.


**Phi-3-Vision**

Phi-3-vision, s iba 4,2 miliardami parametrov, pokračuje v trende a prekonáva väčšie modely ako Claude-3 Haiku a Gemini 1.0 Pro V v úlohách všeobecného vizuálneho uvažovania, OCR a porozumenia tabuliek a diagramov.


**Phi-3.5-Vision**

Phi-3.5-Vision je tiež upgrade Phi-3-Vision, pridáva podporu viacerých obrázkov. Môžete ho vnímať ako vylepšené videnie, nielenže vidí obrázky, ale aj videá.

Phi-3.5-vision prekonáva väčšie modely ako Claude-3.5 Sonnet a Gemini 1.5 Flash v úlohách OCR, porozumenia tabuliek a grafov, a je porovnateľný v úlohách všeobecného vizuálneho uvažovania. Podporuje viacnásobný vstup snímok, teda vykonáva uvažovanie na viacerých vstupných obrázkoch.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** umožňuje, aby modely boli predtrénované pri oveľa nižšom výpočtovom zaťažení, čo znamená, že môžete dramaticky zväčšiť veľkosť modelu alebo datasetu s rovnakým výpočtovým rozpočtom ako hustý (dense) model. Konkrétne, MoE model by mal dosiahnuť rovnakú kvalitu ako jeho hustý ekvivalent oveľa rýchlejšie počas predtrénovania.

Phi-3.5-MoE pozostáva zo 16 modulov expertov s 3,8 miliardami parametrov každý. Phi-3.5-MoE s iba 6,6 miliardami aktívnych parametrov dosahuje podobnú úroveň uvažovania, porozumenia jazyka a matematiky ako oveľa väčšie modely.

Modely z rodiny Phi-3/3.5 môžeme využívať na základe rôznych scenárov. Na rozdiel od LLM je možné nasadiť Phi-3/3.5-mini alebo Phi-3/3.5-Vision na edge zariadeniach.


## Ako používať modely rodiny Phi-3/3.5

Dúfame, že využijeme Phi-3/3.5 v rôznych scenároch. V nasledujúcom texte ukážeme, ako využiť Phi-3/3.5 na rôzne situácie.

![phi3](../../../translated_images/sk/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inferencia cez cloudové API

**Microsoft Foundry Models**

> **Poznámka:** GitHub Models končí na konci júla 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) sú jeho priamou náhradou.

> **Poznámka:** Celá rodina Phi-3/3.5 (Instruct, Vision a MoE varianty) bola stiahnutá z katalógu Microsoft Foundry Models dňa 30. 8. 2025. Používajte tam namiesto nich `Phi-4` (Instruct) alebo `Phi-4-mini-instruct` — príklady Phi-3/3.5 nižšie stále fungujú cez Hugging Face, Ollama, ONNX Runtime a NVIDIA NIM.

Microsoft Foundry Models teraz poskytuje nástupcov Phi-4. Používajte `Phi-4` alebo `Phi-4-mini-instruct` namiesto stiahnutých Phi-3/3.5 modelov, keď nasledujete príklady cloud API.

- Demo: Porovnanie efektov Phi-3-mini a Phi-3.5-mini v čínskych scenároch

![phi3](../../../translated_images/sk/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/sk/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Ak chcete používať vision (multimodálne) modely v cloude, používajte aktuálne dostupný `Phi-4-multimodal-instruct` cez Microsoft Foundry namiesto stiahnutých Phi-3/3.5 Vision modelov; pre textové úlohy používajte `Phi-4` alebo `Phi-4-mini-instruct`. Phi-3.5 MoE model bol zozbieraný z Microsoft Foundry, preto použite iné možnosti popísané v tejto lekcii (napr. Hugging Face), ak chcete experimentovať. Ak máte záujem, môžete si prečítať Phi Cookbook, ako volať Phi modely cez Microsoft Foundry [Kliknite na tento odkaz](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Okrem cloudového katalógu Microsoft Foundry Models môžete použiť tiež [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) na dokončenie súvisiacich volaní. Navštívte NVIDIA NIM pre dokončenie API volaní rodiny Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) je sada akcelerovaných mikroservisov pre inferenciu navrhnutá tak, aby pomohla vývojárom efektívne nasadzovať AI modely v rôznych prostrediach, vrátane cloudu, dátových centier a pracovných staníc.

Tu sú niektoré kľúčové vlastnosti NVIDIA NIM:

- **Jednoduchosť nasadenia:** NIM umožňuje nasadenie AI modelov jedným príkazom, čo zjednodušuje jeho integráciu do existujúcich pracovných tokov.
- **Optimalizovaný výkon:** Využíva predoptimalizované vyhodnocovacie enginy NVIDIA, ako sú TensorRT a TensorRT-LLM, aby zabezpečil nízku latenciu a vysoký priepust.
- **Škálovateľnosť:** NIM podporuje automatické škálovanie na Kubernetes, čo mu umožňuje efektívne zvládať rôzne záťaže.
- **Bezpečnosť a kontrola:** Organizácie môžu udržiavať kontrolu nad svojimi údajmi a aplikáciami prostredníctvom samo-hostovania NIM mikroservisov na svojej vlastnej spravovanej infraštruktúre.
- **Štandardné API:** NIM poskytuje priemyselné štandardné API, čo uľahčuje budovanie a integráciu AI aplikácií, ako sú chatboty, AI asistenti a ďalšie.

NIM je súčasťou NVIDIA AI Enterprise, ktorý má za cieľ zjednodušiť nasadenie a prevádzku AI modelov a zabezpečiť ich efektívne spúšťanie na GPU NVIDIA.

- Demo: Použitie NVIDIA NIM na volanie Phi-3.5-Vision-API [[Kliknite na tento odkaz](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Spustenie Phi-3/3.5 lokálne
Inferencia v súvislosti s Phi-3 alebo s akýmkoľvek jazykovým modelom ako GPT-3 sa vzťahuje na proces generovania odpovedí alebo predpovedí na základe prijatého vstupu. Keď zadáte Phi-3 podnet alebo otázku, využije svoj trénovaný neurónový sieťový model na vyvodenie najpravdepodobnejšej a najrelevantnejšej odpovede analyzovaním vzorov a vzťahov v dátach, na ktorých bol trénovaný.

**Hugging Face Transformer**
Hugging Face Transformers je výkonná knižnica navrhnutá na spracovanie prirodzeného jazyka (NLP) a ďalšie úlohy strojového učenia. Tu sú niektoré kľúčové body:

1. **Predtrénované modely**: Poskytuje tisíce predtrénovaných modelov, ktoré možno použiť na rôzne úlohy, ako sú klasifikácia textu, rozpoznávanie pomenovaných entít, odpovedanie na otázky, zhrnutie, preklad a generovanie textu.

2. **Interoperabilita rámcov**: Knižnica podporuje viacero rámcov hlbokého učenia, vrátane PyTorch, TensorFlow a JAX. To umožňuje trénovať model v jednom rámci a používať ho v inom.

3. **Multimodálne schopnosti**: Okrem NLP Hugging Face Transformers podporuje úlohy v oblasti počítačového videnia (napr. klasifikácia obrázkov, detekcia objektov) a zvukového spracovania (napr. rozpoznávanie reči, klasifikácia audia).

4. **Jednoduchosť použitia**: Knižnica ponúka API a nástroje na ľahké sťahovanie a doladenie modelov, takže je prístupná pre začiatočníkov aj expertov.

5. **Komunita a zdroje**: Hugging Face má živú komunitu a rozsiahlu dokumentáciu, tutoriály a príručky, ktoré pomáhajú používateľom s prvými krokmi a maximálnym využitím knižnice.
[oficiálna dokumentácia](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) alebo ich [GitHub repozitár](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Toto je najčastejšie používaná metóda, ale tiež vyžaduje GPU akceleráciu. Scenáre ako Vision a MoE vyžadujú veľa výpočtov, ktoré budú na CPU veľmi pomalé, ak nebudú kvantizované.


- Demo: Použitie Transformer na volanie Phi-3.5-Instruct [Kliknite na tento odkaz](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Použitie Transformer na volanie Phi-3.5-Vision [Kliknite na tento odkaz](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Použitie Transformer na volanie Phi-3.5-MoE [Kliknite na tento odkaz](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) je platforma navrhnutá tak, aby uľahčila spúšťanie veľkých jazykových modelov (LLM) lokálne na vašom počítači. Podporuje rôzne modely ako Llama 3.1, Phi 3, Mistral a Gemma 2, medzi inými. Platforma zjednodušuje proces tým, že zabalí váhy modelu, konfiguráciu a dáta do jedného balíka, čo prístupnejšie umožňuje používateľom prispôsobovať a vytvárať vlastné modely. Ollama je dostupná pre macOS, Linux a Windows. Je to skvelý nástroj, ak chcete experimentovať alebo nasadiť LLM bez závislosti od cloudových služieb. Ollama je najpriamejší spôsob, stačí vykonať nasledujúci príkaz.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) je Microsoftov offline runtime na zariadení pre spúšťanie modelov ako Phi úplne na vlastnom hardvéri – nie je potrebné predplatné Azure, API kľúč ani sieťové pripojenie. Automaticky vyberá najlepší dostupný vykonávací poskytovateľ (NPU, GPU alebo CPU) a vystavuje OpenAI-kompatibilný endpoint, takže existujúci kód `openai`/Azure AI Inference SDK ho môže použiť s minimálnymi zmenami. Pre začiatok pozrite si [Foundry Local dokumentáciu](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst).

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Alebo použite SDK priamo v Pythone:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime pre GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) je multiplatformový akcelerátor pre inferenciu a trénovanie strojového učenia. ONNX Runtime pre Generative AI (GENAI) je výkonný nástroj, ktorý vám pomáha efektívne spúšťať generatívne AI modely naprieč rôznymi platformami.

## Čo je ONNX Runtime?
ONNX Runtime je open-source projekt, ktorý umožňuje vysoko výkonnú inferenciu modelov strojového učenia. Podporuje modely vo formáte Open Neural Network Exchange (ONNX), ktorý je štandardom na reprezentáciu modelov strojového učenia. Inferencia pomocou ONNX Runtime môže zabezpečiť rýchlejšie používateľské zážitky a nižšie náklady, podporujúc modely z rámcov hlbokého učenia, ako sú PyTorch a TensorFlow/Keras, ako aj klasické knižnice strojového učenia ako scikit-learn, LightGBM, XGBoost atď. ONNX Runtime je kompatibilný s rôznym hardvérom, ovládačmi a operačnými systémami, a poskytuje optimálny výkon využitím hardvérových akcelerátorov spolu s optimalizáciami grafu a transformáciami.

## Čo je Generative AI?
Generative AI sa vzťahuje na AI systémy, ktoré dokážu generovať nový obsah, ako je text, obrázky alebo hudba, na základe dát, na ktorých boli trénované. Príklady zahŕňajú jazykové modely ako GPT-3 a modely na generovanie obrázkov ako Stable Diffusion. Knižnica ONNX Runtime pre GenAI poskytuje generatívnu AI slučku pre ONNX modely, vrátane inferencie pomocou ONNX Runtime, spracovania logitov, vyhľadávania a vzorkovania a správy kešu KV.

## ONNX Runtime pre GENAI
ONNX Runtime pre GENAI rozširuje schopnosti ONNX Runtime na podporu generatívnych AI modelov. Tu sú niektoré kľúčové funkcie:

- **Široká podpora platforiem:** Funguje na rôznych platformách, vrátane Windows, Linux, macOS, Android a iOS.
- **Podpora modelov:** Podporuje mnoho populárnych generatívnych AI modelov, ako sú LLaMA, GPT-Neo, BLOOM a ďalšie.
- **Optimalizácia výkonu:** Obsahuje optimalizácie pre rôzne hardvérové akcelerátory, ako sú NVIDIA GPU, AMD GPU a ďalšie2.
- **Jednoduchosť použitia:** Poskytuje API pre jednoduchú integráciu do aplikácií, umožňujúc generovať text, obrázky a iný obsah s minimálnym kódom.
- Používatelia môžu volať vyššiu metódu generate(), alebo spúšťať každú iteráciu modelu v slučke, generujúc jeden token po jednom, a voliteľne aktualizovať parametre generovania počas slučky.
- ONNX runtime taktiež podporuje greedy/beam search a TopP, TopK sampling na generovanie sekvencií tokenov a vstavané spracovanie logitov ako penalizácie opakovania. Môžete tiež ľahko pridať vlastné skórovanie.

## Začnite
Pre začiatok s ONNX Runtime pre GENAI môžete nasledovať tieto kroky:

### Nainštalujte ONNX Runtime:
```Python
pip install onnxruntime
```
### Nainštalujte Vylepšenia pre Generatívnu AI:
```Python
pip install onnxruntime-genai
```

### Spustite model: Tu je jednoduchý príklad v Pythone:
```Python
import onnxruntime_genai as og

model = og.Model('path_to_your_model.onnx')

tokenizer = og.Tokenizer(model)

input_text = "Hello, how are you?"

input_tokens = tokenizer.encode(input_text)

output_tokens = model.generate(input_tokens)

output_text = tokenizer.decode(output_tokens)

print(output_text) 
```
### Demo: Použitie ONNX Runtime GenAI na volanie Phi-3.5-Vision


```python

import onnxruntime_genai as og

model_path = './Your Phi-3.5-vision-instruct ONNX Path'

img_path = './Your Image Path'

model = og.Model(model_path)

processor = model.create_multimodal_processor()

tokenizer_stream = processor.create_stream()

text = "Your Prompt"

prompt = "<|user|>\n"

prompt += "<|image_1|>\n"

prompt += f"{text}<|end|>\n"

prompt += "<|assistant|>\n"

image = og.Images.open(img_path)

inputs = processor(prompt, images=image)

params = og.GeneratorParams(model)

params.set_inputs(inputs)

params.set_search_options(max_length=3072)

generator = og.Generator(model, params)

while not generator.is_done():

    generator.compute_logits()
    
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    
    output = tokenizer_stream.decode(new_token)
    
    print(tokenizer_stream.decode(new_token), end='', flush=True)

```


**Ďalšie**

Okrem referenčných metód ONNX Runtime, Ollama a Foundry Local môžeme tiež doplniť referenciu kvantitatívnych modelov založených na referenčných metódach modelov poskytnutých rôznymi výrobcami. Napríklad Apple MLX framework s Apple Metal, Qualcomm QNN s NPU, Intel OpenVINO s CPU/GPU atď. Viac obsahu nájdete aj v [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Viac

Osvojili sme si základy Phi-3/3.5 rodiny, ale na naučenie sa viac o SLM potrebujeme väčšie vedomosti. Odpovede môžete nájsť v Phi-3 Cookbook. Ak chcete vedieť viac, navštívte prosím [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->