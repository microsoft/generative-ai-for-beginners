# Úvod do malých jazykových modelov pre generatívnu AI pre začiatočníkov
Generatívna AI je fascinujúca oblasť umelej inteligencie, ktorá sa zameriava na tvorbu systémov schopných generovať nový obsah. Tento obsah môže byť od textu a obrázkov až po hudbu a dokonca celé virtuálne prostredia. Jednou z najvzrušujúcejších aplikácií generatívnej AI je oblasť jazykových modelov.

## Čo sú to malé jazykové modely?

Malý jazykový model (SLM) predstavuje zmenšenú variantu veľkého jazykového modelu (LLM), využívajúcu mnohé architektonické princípy a techniky veľkých modelov, pričom má výrazne nižšiu výpočtovú náročnosť. 

SLM sú podmnožinou jazykových modelov navrhnutých na generovanie textu podobného ľudskému prejavu. Na rozdiel od ich väčších prototypov, ako je GPT-4, sú SLM kompaktnejšie a efektívnejšie, čo ich robí ideálnymi pre aplikácie, kde sú výpočtové zdroje obmedzené. Napriek menšej veľkosti však dokážu vykonávať rôzne úlohy. Typicky sú SLM konštruované kompresiou alebo destiláciou LLM, s cieľom zachovať podstatnú časť pôvodnej funkcionality a jazykových schopností modelu. Táto redukcia veľkosti modelu znižuje celkovú zložitosť, vďaka čomu sú SLM efektívnejšie z hľadiska použitia pamäte aj výpočtových požiadaviek. Napriek týmto optimalizáciám môžu SLM vykonávať široké spektrum úloh spracovania prirodzeného jazyka (NLP):

- Generovanie textu: Vytváranie koherentných a kontextovo relevantných viet alebo odsekov.
- Dokončovanie textu: Predpovedanie a dokončovanie viet na základe daného podnetu.
- Preklad: Prevod textu z jedného jazyka do druhého.
- Zhrnutie: Skracovanie dlhých textov na kratšie, ľahšie stráviteľné súhrny.

Aj keď s určitými kompromismi vo výkonu alebo hĺbke porozumenia v porovnaní s väčšími modelmi.

## Ako malé jazykové modely fungujú?
SLM sa trénujú na obrovských množstvách textových dát. Počas tréningu sa učia vzory a štruktúry jazyka, čo im umožňuje generovať text, ktorý je gramaticky správny a kontextovo vhodný. Tréningový proces zahŕňa:

- Zber dát: Zhromažďovanie veľkých datasetov textu z rôznych zdrojov.
- Predspracovanie: Čistenie a organizovanie dát, aby boli vhodné na tréning.
- Tréning: Použitie algoritmov strojového učenia na naučenie modelu, ako rozumieť a generovať text.
- Doladenie: Upravovanie modelu na zlepšenie jeho výkonu v konkrétnych úlohách.

Vývoj SLM korešponduje so zvyšujúcou sa potrebou modelov, ktoré je možné nasadiť v prostrediach s obmedzenými zdrojmi, ako sú mobilné zariadenia alebo edge computing platformy, kde by plnohodnotné LLM mohli byť nepraktické kvôli ich vysokým nárokom na zdroje. Zameraním sa na efektívnosť SLM vyvažujú výkon a dostupnosť, čím umožňujú širšie použitie naprieč rôznymi oblasťami.

![slm](../../../translated_images/sk/slm.4058842744d0444a.webp)

## Ciele učenia

V tejto lekcii sa snažíme predstaviť znalosti o SLM a spojiť ich s Microsoft Phi-3 na štúdium rôznych scenárov v oblasti textového obsahu, videnia a MoE.

Na konci tejto lekcie by ste mali vedieť odpovedať na nasledujúce otázky:

- Čo je SLM?
- Aký je rozdiel medzi SLM a LLM?
- Čo je rodina Microsoft Phi-3/3.5?
- Ako vykonať inferenciu s rodinou Microsoft Phi-3/3.5?

Pripravení? Poďme začať.

## Rozdiely medzi veľkými jazykovými modelmi (LLM) a malými jazykovými modelmi (SLM)

Oba, LLM aj SLM, sú postavené na základných princípoch pravdepodobnostného strojového učenia, nasledujú podobné prístupy v architektonickom dizajne, metódach tréningu, procesoch generovania dát a technikách hodnotenia modelov. Avšak niekoľko kľúčových faktorov odlišuje tieto dva typy modelov.

## Aplikácie malých jazykových modelov

SLM nachádzajú široké využitie, vrátane:

- Chatboty: Poskytovanie zákazníckej podpory a interakcia s užívateľmi konverzačným spôsobom.
- Tvorba obsahu: Pomoc spisovateľom pri generovaní nápadov alebo dokonca pri tvorbe celých článkov.
- Vzdelávanie: Pomoc študentom pri písaní úloh alebo učení sa nových jazykov.
- Dostupnosť: Vytváranie nástrojov pre ľudí so zdravotným postihnutím, ako sú systémy prevodu textu na reč.

**Veľkosť**
  
Hlavný rozdiel medzi LLM a SLM spočíva v rozsahu modelov. LLM, ako ChatGPT (GPT-4), môžu obsahovať odhadovaných 1,76 bilióna parametrov, zatiaľ čo open-source SLM ako Mistral 7B sú navrhnuté s výrazne menším počtom parametrov – približne 7 miliárd. Tento rozdiel je primárne spôsobený rozdielmi v architektúre modelu a tréningových procesoch. Napríklad ChatGPT využíva mechanizmus seba-pozornosti v rámci encoder-decoder architektúry, zatiaľ čo Mistral 7B používa sliding window attention, ktorý umožňuje efektívnejší tréning v decode-only modeli. Táto architektonická variabilita má hlboký vplyv na zložitosť a výkon týchto modelov.

**Porozumenie**

SLM sú zvyčajne optimalizované pre výkon v špecifických doménach, vďaka čomu sú vysoko špecializované, ale potenciálne obmedzené vo svojej schopnosti poskytovať široké kontextové porozumenie naprieč viacerými vednými oblasťami. Naopak, LLM sa snažia simulovať ľudskú inteligenciu na komplexnejšej úrovni. Trénované na obrovských, rozmanitých datasetoch, LLM sú navrhnuté na kvalitný výkon v rôznych oblastiach, čo ponúka väčšiu všestrannosť a prispôsobivosť. Preto sú LLM vhodnejšie pre širšiu škálu downstream úloh, ako sú spracovanie prirodzeného jazyka a programovanie.

**Výpočty**

Tréning a nasadenie LLM sú procesy náročné na zdroje, často vyžadujúce významnú výpočtovú infraštruktúru, vrátane veľkých GPU klastrov. Napríklad tréning modelu ako ChatGPT od základu môže vyžadovať tisíce GPU počas dlhých období. Naopak, SLM, vzhľadom na menší počet parametrov, sú dostupnejšie z hľadiska výpočtových zdrojov. Modely ako Mistral 7B je možné trénovať a používať na lokálnych počítačoch vybavených stredne výkonnými GPU, hoci samotný tréning stále vyžaduje niekoľko hodín na viacerých GPU.

**Predsudky**

Predsudky sú známy problém u LLM, primárne kvôli povahy tréningových dát. Tieto modely často používajú surové, otvorene dostupné dáta z internetu, ktoré môžu podreprezentovať alebo nesprávne zobrazovať určité skupiny, zavádzať chybné označenie alebo odrážať jazykové predsudky ovplyvnené dialektmi, geografickými variantmi a gramatickými pravidlami. Okrem toho zložitosť architektúry LLM môže nevedome zhoršiť predsudky, ktoré nemusia byť bez starostlivého doladenia ľahko viditeľné. Na druhej strane, SLM, trénované na obmedzenejších, doménovo špecifických datasetoch, sú inherentne menej náchylné na takéto predsudky, hoci nie sú proti nim imúnne.

**Inferencia**

Menšia veľkosť SLM im poskytuje výraznú výhodu v rýchlosti inferencie, čo im umožňuje efektívne generovať výstupy na lokálnom hardvéri bez potreby rozsiahleho paralelného spracovania. Naopak, LLM kvôli svojej veľkosti a zložitosti často vyžadujú značné paralelné výpočtové zdroje na dosiahnutie prijateľných časov inferencie. Prítomnosť viacerých súbežných užívateľov ešte ďalej spomaľuje reakčné časy LLM, najmä pri nasadení vo veľkom meradle.

Zhrnuté, oba LLM a SLM majú spoločný základ v strojovom učení, ale výrazne sa líšia veľkosťou modelu, požiadavkami na zdroje, rozsahom kontextového porozumenia, náchylnosťou na predsudky a rýchlosťou inferencie. Tieto rozdiely odrážajú ich vhodnosť pre rôzne použitia, pričom LLM sú univerzálnejšie, ale náročnejšie na zdroje, a SLM ponúkajú efektívnosť v konkrétnych doménach s nižšími výpočtovými nárokmi.

***Poznámka: V tejto lekcii predstavíme SLM na príklade Microsoft Phi-3 / 3.5.***

## Predstavenie rodiny Phi-3 / Phi-3.5

Rodina Phi-3 / 3.5 sa primárne zameriava na scenáre aplikácií v texte, vidění a agentovi (MoE):

### Phi-3 / 3.5 Instruct

Hlavne pre generovanie textu, dokončovanie rozhovorov a extrakciu informácií z obsahu, atď.

**Phi-3-mini**

Jazykový model s 3,8 miliardami parametrov je dostupný na Microsoft Foundry, Hugging Face a Ollama. Modely Phi-3 výrazne prekonávajú jazykové modely rovnakej alebo väčšej veľkosti na kľúčových benchmarkoch (viď čísla benchmarkov nižšie, vyššie čísla znamenajú lepšie výsledky). Phi-3-mini prekonáva modely dvojnásobnej veľkosti, zatiaľ čo Phi-3-small a Phi-3-medium prekonávajú väčšie modely, vrátane GPT-3.5.

**Phi-3-small & medium**

S iba 7 miliardami parametrov Phi-3-small prekonáva GPT-3.5T v rôznych jazykových, logických, kódovacích a matematických benchmarkoch.

Phi-3-medium s 14 miliardami parametrov pokračuje v tomto trende a prekonáva Gemini 1.0 Pro.

**Phi-3.5-mini**

Môžeme ho považovať za upgrade Phi-3-mini. Hoci počet parametrov zostáva nezmenený, zlepšuje schopnosť podpory viacerých jazykov (podporuje 20+ jazykov: arabčina, čínština, čeština, dánčina, holandčina, angličtina, finčina, francúzština, nemčina, hebrejčina, maďarčina, taliančina, japončina, kórejčina, norčina, poľština, portugalčina, ruština, španielčina, švédčina, thajčina, turečtina, ukrajinčina) a pridáva silnejšiu podporu pre dlhý kontext.

Phi-3.5-mini s 3,8 miliardami parametrov prekonáva jazykové modely rovnakej veľkosti a je porovnateľný s modelmi dvojnásobnej veľkosti.

### Phi-3 / 3.5 Vision

Môžeme považovať Instruct model Phi-3/3.5 za schopnosť Phi porozumieť, zatiaľ čo Vision dáva Phi oči na pochopenie sveta.


**Phi-3-Vision**

Phi-3-vision, s len 4,2 miliardami parametrov, pokračuje v tomto trende a prekonáva väčšie modely ako Claude-3 Haiku a Gemini 1.0 Pro V v úlohách všeobecného vizuálneho uvažovania, OCR a porozumenia tabuliek a diagramov.


**Phi-3.5-Vision**

Phi-3.5-Vision je tiež upgrade Phi-3-Vision, pridávajúci podporu pre viacero obrázkov. Môžete ho považovať za zlepšenie vo videní – nielen že vidíte obrázky, ale aj videá.

Phi-3.5-vision prekonáva väčšie modely ako Claude-3.5 Sonnet a Gemini 1.5 Flash naprieč úlohami OCR, porozumenia tabuliek a grafov a je porovnateľný v úlohách všeobecného vizuálneho uvažovania. Podporuje vstup viacerých snímok, teda rozumie a uvažuje na základe viacerých vstupných obrázkov.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** umožňuje modelom byť predtrénované s oveľa menším výpočtovým výkonom, čo znamená, že môžete dramaticky zväčšiť veľkosť modelu alebo datasetu pri rovnakom výpočtovom rozpočte ako pri hustých modeloch. Konkrétne, MoE model by mal dosiahnuť rovnakú kvalitu ako jeho hustý protějšok oveľa rýchlejšie počas predtréningu.

Phi-3.5-MoE obsahuje 16x3,8 miliardových expertných modulov. Phi-3.5-MoE s iba 6,6 miliardami aktívnych parametrov dosahuje úroveň uvažovania, porozumenia jazyka a matematiky porovnateľnú s oveľa väčšími modelmi.

Model rodiny Phi-3/3.5 môžeme používať na rôzne scenáre. Na rozdiel od LLM môžete nasadiť Phi-3/3.5-mini alebo Phi-3/3.5-Vision na edge zariadeniach.


## Ako používať modely rodiny Phi-3/3.5

Chceme používať Phi-3/3.5 v rôznych scenároch. Nasledujúca časť ukáže použitie Phi-3/3.5 v závislosti od scenára.

![phi3](../../../translated_images/sk/phi3.655208c3186ae381.webp)

### Inferencia cez cloudové API

**Microsoft Foundry Models**

> **Poznámka:** GitHub Models bude ukončený koncom júla 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) je priama náhrada.

Microsoft Foundry Models je najpriamejšia cesta. Rýchlo získate prístup k modelu Phi-3/3.5-Instruct cez katalóg Foundry modelov. V kombinácii s Azure AI Inference SDK / OpenAI SDK môžete pristupovať k API cez kód a vykonať volanie Phi-3/3.5-Instruct. Môžete tiež testovať rôzne výsledky cez Playground.

- Demo: Porovnanie účinkov Phi-3-mini a Phi-3.5-mini v čínskych scénach

![phi3](../../../translated_images/sk/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/sk/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Ak chcete používať modely vision a MoE, môžete ich taktiež volať cez Microsoft Foundry. Ak máte záujem, môžete si prečítať Phi-3 Cookbook, ktorý vysvetľuje, ako volat Phi-3/3.5 Instruct, Vision, MoE cez Microsoft Foundry [Kliknite na tento odkaz](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Okrem cloudového katalógu Microsoft Foundry Models môžete tiež použiť [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) na vykonanie súvisiacich volaní. Navštívte NVIDIA NIM pre API volania rodiny Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) je sada zrýchlených mikroservisov inferencie navrhnutých na efektívne nasadenie AI modelov vo viacerých prostrediach, vrátane cloudov, dátových centier a pracovných staníc.

Tu sú niektoré kľúčové funkcie NVIDIA NIM:

- **Jednoduchosť nasadenia:** NIM umožňuje nasadenie AI modelov jediným príkazom, čím je jednoduché ho integrovať do existujúcich pracovných tokov.

- **Optimalizovaný výkon:** Využíva predoptimalizované inferenčné motory NVIDIA, ako sú TensorRT a TensorRT-LLM, aby zabezpečil nízku latenciu a vysokú priepustnosť.
- **Škálovateľnosť:** NIM podporuje automatické škálovanie na Kubernetes, čo mu umožňuje efektívne spracovávať rôzne záťaže.
- **Bezpečnosť a kontrola:** Organizácie môžu udržiavať kontrolu nad svojimi údajmi a aplikáciami tým, že si sami hosťujú NIM mikroslužby na vlastnej spravovanej infraštruktúre.
- **Štandardné API:** NIM poskytuje priemyselne štandardné API, čo uľahčuje budovanie a integráciu AI aplikácií, ako sú chatboty, AI asistenti a ďalšie.

NIM je súčasťou NVIDIA AI Enterprise, ktorý má za cieľ zjednodušiť nasadenie a operacionalizáciu AI modelov, zabezpečiac ich efektívny beh na NVIDIA GPU.

- Demo: Použitie NVIDIA NIM na volanie Phi-3.5-Vision-API  [[Kliknite na tento odkaz](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Spustenie Phi-3/3.5 Lokálne
Inferencia v súvislosti s Phi-3 alebo akýmkoľvek jazykovým modelom ako GPT-3 označuje proces generovania odpovedí alebo predpovedí na základe vstupu, ktorý dostane. Keď zadáte prompt alebo otázku Phi-3, používa svoj vytrénovaný neurónový sieťový model na odvodenie najpravdepodobnejšej a relevantnej odpovede analýzou vzorcov a vzťahov v dátach, na ktorých bol trénovaný.

**Hugging Face Transformer**
Hugging Face Transformers je výkonná knižnica navrhnutá pre spracovanie prirodzeného jazyka (NLP) a ďalšie úlohy strojového učenia. Tu sú niektoré kľúčové body o nej:

1. **Predtrénované modely:** Poskytuje tisíce predtrénovaných modelov, ktoré je možné použiť na rôzne úlohy, ako klasifikácia textu, rozpoznávanie pomenovaných entít, odpovedanie na otázky, sumarizácia, preklad a generovanie textu.

2. **Interoperabilita rámcov:** Knižnica podporuje viacero hlbokých učebných rámcov, vrátane PyTorch, TensorFlow a JAX. To umožňuje trénovať model v jednom rámci a používať ho v inom.

3. **Multimodálne schopnosti:** Okrem NLP podporuje Hugging Face Transformers aj úlohy v oblasti počítačového videnia (napr. klasifikácia obrázkov, detekcia objektov) a spracovania zvuku (napr. rozpoznávanie reči, klasifikácia zvuku).

4. **Jednoduchosť používania:** Knižnica ponúka API a nástroje pre ľahké stiahnutie a doladenie modelov, čím je prístupná pre začiatočníkov aj odborníkov.

5. **Komunita a zdroje:** Hugging Face má živú komunitu a rozsiahlu dokumentáciu, návody a príručky, ktoré pomáhajú používateľom začať a využiť knižnicu na maximum.
[oficiálna dokumentácia](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) alebo ich [GitHub úložisko](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Toto je najbežnejšie používaná metóda, ale vyžaduje aj GPU akceleráciu. Nakoniec scénare ako Vision a MoE vyžadujú veľa výpočtov, ktoré budú na CPU veľmi pomalé, ak nie sú kvantizované.


- Demo: Použitie Transformer na volanie Phi-3.5-Instruct [Kliknite na tento odkaz](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Použitie Transformer na volanie Phi-3.5-Vision [Kliknite na tento odkaz](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Použitie Transformer na volanie Phi-3.5-MoE [Kliknite na tento odkaz](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) je platforma navrhnutá tak, aby uľahčila spúšťanie veľkých jazykových modelov (LLM) lokálne na vašom počítači. Podporuje rôzne modely ako Llama 3.1, Phi 3, Mistral a Gemma 2, medzi ďalšími. Platforma zjednodušuje proces tým, že bundluje váhy modelu, konfiguráciu a dáta do jedného balíka, čo umožňuje používateľom jednoduchšie prispôsobiť a vytvoriť vlastné modely. Ollama je dostupná pre macOS, Linux a Windows. Je to skvelý nástroj, ak chcete experimentovať s LLM alebo ich nasadiť bez závislosti na cloudových službách. Ollama je najpriamejší spôsob, stačí vykonať nasledujúci príkaz.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) je offline runtime spoločnosti Microsoft bežiaci priamo na zariadení pre spúšťanie modelov ako Phi úplne na vašom vlastnom hardvéri - nie je potrebný žiadny Azure predplatný plán, API kľúč ani sieťové pripojenie. Automaticky vyberá najlepší dostupný vykonávací poskytovateľ (NPU, GPU alebo CPU) a poskytuje OpenAI-kompatibilný endpoint, takže existujúci kód `openai`/Azure AI Inference SDK môže smerovať naň s minimálnymi zmenami. Viac informácií nájdete v [Foundry Local dokumentácii](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst).

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) je multiplatformový akcelerátor na inferenciu a trénovanie strojového učenia. ONNX Runtime pre Generačné AI (GENAI) je výkonný nástroj, ktorý vám pomáha efektívne spúšťať modely generačnej AI naprieč rôznymi platformami.

## Čo je ONNX Runtime?
ONNX Runtime je open-source projekt, ktorý umožňuje vysokovýkonnú inferenciu modelov strojového učenia. Podporuje modely v štandarde Open Neural Network Exchange (ONNX), čo je štandard pre reprezentáciu modelov strojového učenia. ONNX Runtime inferencia môže umožniť rýchlejšie zákaznícke zážitky a nižšie náklady, podporujúc modely z hlbokých učebných rámcov ako PyTorch a TensorFlow/Keras, rovnako ako klasické knižnice strojového učenia ako scikit-learn, LightGBM, XGBoost a ďalšie. ONNX Runtime je kompatibilný s rôznym hardvérom, ovládačmi a operačnými systémami a poskytuje optimálny výkon využitím hardvérových akcelerátorov tam, kde je to možné, spolu s optimalizáciami a transformáciami grafov.

## Čo je Generatívna AI?
Generatívna AI sa vzťahuje na AI systémy, ktoré dokážu generovať nový obsah, ako text, obrázky alebo hudbu, na základe dát, na ktorých boli trénované. Príklady zahŕňajú jazykové modely ako GPT-3 a modely na generovanie obrázkov ako Stable Diffusion. ONNX Runtime pre GenAI knižnica poskytuje generačný AI cyklus pre ONNX modely, vrátane inferencie s ONNX Runtime, spracovania logitov, vyhľadávania a vzorkovania a správy KV cache.

## ONNX Runtime pre GENAI
ONNX Runtime pre GENAI rozširuje schopnosti ONNX Runtime o podporu modelov generačnej AI. Tu sú niektoré kľúčové vlastnosti:

- **Široká podpora platforiem:** Funguje na rôznych platformách vrátane Windows, Linux, macOS, Android a iOS.
- **Podpora modelov:** Podporuje mnoho populárnych generačných AI modelov, ako LLaMA, GPT-Neo, BLOOM a ďalšie.
- **Optimalizácia výkonu:** Zahŕňa optimalizácie pre rôzne hardvérové akcelerátory ako NVIDIA GPU, AMD GPU a ďalšie.
- **Jednoduchosť použitia:** Poskytuje API pre ľahkú integráciu do aplikácií, ktoré umožňujú generovať text, obrázky a iný obsah s minimálnym kódom.
- Používatelia môžu volať vysokú úroveň metódy generate() alebo spúšťať každú iteráciu modelu v slučke, generujúc jeden token naraz, a voliteľne aktualizovať parametre generovania v rámci slučky.
- ONNX runtime tiež podporuje greedy/beam hľadanie a TopP, TopK vzorkovanie na generovanie sekvencií tokenov a vstavané spracovanie logitov ako penalizácie opakovania. Môžete tiež ľahko pridať vlastné skórovanie.

## Začínáme
Na začiatok s ONNX Runtime pre GENAI môžete postupovať podľa týchto krokov:

### Inštalujte ONNX Runtime:
```Python
pip install onnxruntime
```
### Inštalujte Generatívne AI rozšírenia:
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


**Iné**

Okrem referenčných metód ONNX Runtime, Ollama a Foundry Local môžeme tiež dokončiť referenciu kvantitatívnych modelov založených na modelových referenčných metódach poskytovaných rôznymi výrobcami. Napríklad Apple MLX framework s Apple Metal, Qualcomm QNN s NPU, Intel OpenVINO s CPU/GPU a ďalšie. Viac obsahu nájdete aj v [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).


## Viac

Naučili sme sa základy rodiny Phi-3/3.5, ale na učenie sa viac o SLM potrebujeme viac znalostí. Odpovede nájdete v Phi-3 Cookbook. Ak chcete vedieť viac, navštívte prosím [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->