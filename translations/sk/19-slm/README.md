# Úvod do malých jazykových modelov pre generatívnu AI pre začiatočníkov
Generatívna AI je fascinujúca oblasť umelej inteligencie, ktorá sa zameriava na vytváranie systémov schopných generovať nový obsah. Tento obsah môže byť text, obrázky, hudba, ba dokonca celé virtuálne prostredia. Jednou z najvzrušujúcejších aplikácií generatívnej AI sú jazykové modely.

## Čo sú malé jazykové modely?

Malý jazykový model (SLM) predstavuje zmenšenú variantu veľkého jazykového modelu (LLM), využívajúcu mnohé architektonické princípy a techniky LLM, pričom má výrazne zníženú výpočtovú náročnosť.

SLM sú podmnožinou jazykových modelov navrhnutých na generovanie textu pripomínajúceho ľudskú reč. Na rozdiel od ich väčších náprotivkov, ako je GPT-4, sú SLM kompaktnejšie a efektívnejšie, čo ich robí ideálnymi pre aplikácie s obmedzenými výpočtovými zdrojmi. Napriek menšej veľkosti môžu vykonávať rôzne úlohy. Zvyčajne sa SLM konštruujú kompresiou alebo destiláciou LLM s cieľom zachovať podstatnú časť funkčnosti a jazykových schopností pôvodného modelu. Táto redukcia veľkosti modelu znižuje celkovú zložitosť, čo robí SLM efektívnejšími z hľadiska používania pamäte aj výpočtových požiadaviek. Napriek týmto optimalizáciám môžu SLM vykonávať širokú škálu úloh spracovania prirodzeného jazyka (NLP):

- Generovanie textu: Vytváranie súvislých a kontextovo relevantných viet alebo odstavcov.
- Dokončovanie textu: Predikcia a doplňovanie viet na základe zadaného promptu.
- Preklad: Prevod textu z jedného jazyka do druhého.
- Zhrnutie: Skracovanie dlhého textu na kratšie, ľahšie pochopiteľné zhrnutia.

Aj keď s niektorými kompromismi vo výkone alebo hĺbke porozumenia v porovnaní s väčšími modelmi.

## Ako fungujú malé jazykové modely?
SLM sú trénované na obrovskom množstve textových údajov. Počas tréningu sa naučia vzory a štruktúry jazyka, čo im umožňuje generovať text, ktorý je gramaticky správny a kontextovo vhodný. Proces tréningu zahŕňa:

- Zber údajov: Zhromažďovanie veľkých datasetov textu z rôznych zdrojov.
- Predspracovanie: Čistenie a organizovanie dát, aby boli vhodné na tréning.
- Tréning: Použitie algoritmov strojového učenia na naučenie modelu, ako rozumieť a generovať text.
- Doladenie: Úprava modelu na zlepšenie jeho výkonu v konkrétnych úlohách.

Vývoj SLM korešponduje so zvyšujúcou sa potrebou modelov, ktoré je možné nasadiť v prostrediach s obmedzenými zdrojmi, ako sú mobilné zariadenia alebo edge computing platformy, kde plnohodnotné LLM môžu byť nepraktické kvôli veľkej náročnosti na zdroje. Zameraním sa na efektivitu SLM vyvažujú výkon a dostupnosť, čo umožňuje širšie využitie v rôznych oblastiach.

![slm](../../../translated_images/sk/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Ciele učenia

V tejto lekcii chceme predstaviť poznatky o SLM a spojiť ich s Microsoft Phi-3, aby sme sa naučili rôzne scenáre v textovom obsahu, vízii a MoE.

Na konci tejto lekcie by ste mali vedieť odpovedať na nasledujúce otázky:

- Čo je SLM?
- Aký je rozdiel medzi SLM a LLM?
- Čo je rodina Microsoft Phi-3/3.5?
- Ako spustiť inferenciu s rodinou Microsoft Phi-3/3.5?

Ste pripravení? Poďme na to.

## Rozdiely medzi veľkými jazykovými modelmi (LLM) a malými jazykovými modelmi (SLM)

LLM aj SLM sú postavené na základných princípoch pravdepodobnostného strojového učenia a používajú podobné prístupy v architektúre, tréningových metódach, procesoch generovania dát a hodnotení modelov. Napriek tomu ich odlišuje niekoľko kľúčových faktorov.

## Aplikácie malých jazykových modelov

SLM majú široké spektrum využitia, vrátane:

- Chatboti: Poskytovanie zákazníckej podpory a interakcia s používateľmi konverzačným spôsobom.
- Tvorba obsahu: Pomoc spisovateľom generovaním nápadov alebo dokonca celých článkov.
- Vzdelávanie: Pomoc študentom pri písaní úloh alebo učení sa nových jazykov.
- Prístupnosť: Vytváranie nástrojov pre osoby so zdravotným postihnutím, napríklad systémy prevodu textu na reč.

**Veľkosť**
  
Hlavný rozdiel medzi LLM a SLM spočíva v rozsahu modelov. LLM, ako ChatGPT (GPT-4), môžu obsahovať odhadovaných 1,76 bilióna parametrov, zatiaľ čo open-source SLM ako Mistral 7B majú výrazne menej parametrov – približne 7 miliárd. Tento rozdiel je najmä spôsobený rozdielmi v architektúre modelu a tréningových procesoch. Napríklad ChatGPT používa mechanizmus seba-poznania (self-attention) v rámci encoder-decoder architektúry, zatiaľ čo Mistral 7B využíva sliding window attention, čo umožňuje efektívnejší tréning v rámci decoder-only modelu. Táto architektonická odlišnosť má zásadný dopad na zložitosť a výkon týchto modelov.

**Porozumenie**

SLM sú zvyčajne optimalizované na výkon v špecifických doménach, vďaka čomu sú veľmi špecializované, ale môžu byť obmedzené v schopnosti poskytovať široké kontextové porozumenie naprieč viacerými odbormi. Naopak, LLM cieľom je simulovať ľudskú inteligenciu na komplexnejšej úrovni. Sú trénované na rozsiahlych a rôznorodých dátových súboroch, a sú navrhnuté tak, aby dobre fungovali v širokom spektre oblastí, čo im poskytuje väčšiu všestrannosť a prispôsobivosť. Preto sú LLM vhodnejšie pre širšie spektrum downstream úloh, ako je spracovanie prirodzeného jazyka a programovanie.

**Výpočtové nároky**

Tréning a nasadenie LLM sú procesy náročné na zdroje, často vyžadujúce významnú výpočtovú infraštruktúru, vrátane veľkých GPU klastrov. Napríklad tréning modelu ako ChatGPT od nuly môže vyžadovať tisíce GPU počas dlhých období. Naopak, SLM s menším počtom parametrov sú dostupnejšie z hľadiska výpočtových zdrojov. Modely ako Mistral 7B je možné trénovať a spúšťať na lokálnych strojoch vybavených stredne výkonnými GPU, hoci tréning stále zaberá niekoľko hodín na viacerých GPU.

**Bias (zaujatosti)**

Bias je známym problémom LLM, predovšetkým vzhľadom na povahu tréningových dát. Tieto modely často vychádzajú z surových, verejne dostupných dát z internetu, ktoré môžu podreprerzentovať alebo nesprávne reprezentovať určité skupiny, zavádzať chybné označovanie alebo odrážať jazykové zaujatosti založené na dialektoch, geografických variáciách a gramatických pravidlách. Navyše zložitosť architektúr LLM môže neúmyselne zhoršovať bias, ktorý pri nedostatočnom doladení môže ostať nepovšimnutý. Na druhej strane, SLM, keďže sú trénované na viac obmedzených a špecifických dátových súboroch, sú prirodzene menej náchylné na takéto zaujatosti, hoci úplne im nie sú odolné.

**Inferencia**

Menšia veľkosť SLM prináša významnú výhodu z hľadiska rýchlosti inferencie, čo im umožňuje efektívne generovať výstupy na lokálnom hardvéri bez potreby rozsiahleho paralelného spracovania. Naopak, LLM kvôli svojej veľkosti a zložitosti často vyžadujú značné paralelné výpočtové zdroje na dosiahnutie prijateľnej doby inferencie. Prítomnosť viacerých súbežných používateľov ešte viac spomaľuje reakčné časy LLM, najmä pri nasadení vo veľkom meradle.

Zhrnuté, LLM aj SLM majú spoločný základ v strojovom učení, avšak významne sa líšia v veľkosti modelu, požiadavkách na zdroje, schopnosti chápať kontext, náchylnosti na bias a rýchlosti inferencie. Tieto rozdiely odrážajú ich vhodnosť pre rôzne použitia, pričom LLM sú všestrannejšie, ale náročnejšie na zdroje, zatiaľ čo SLM ponúkajú špecializovanú efektivitu s nižšími výpočtovými nárokmi.

***Poznámka: V tejto lekcii predstavíme SLM na príklade Microsoft Phi-3 / 3.5.***

## Predstavenie rodiny Phi-3 / Phi-3.5

Rodina Phi-3 / 3.5 je primárne zameraná na textové, vizuálne a Agent (MoE) aplikačné scenáre:

### Phi-3 / 3.5 Instruct

Hlavne na generovanie textu, dokončenie rozhovoru a extrakciu informácií z obsahu a podobne.

**Phi-3-mini**

Jazykový model s 3,8 miliardami parametrov je dostupný na Microsoft Foundry, Hugging Face a Ollama. Modely Phi-3 výrazne prevyšujú jazykové modely rovnakej alebo väčšej veľkosti v kľúčových benchmarkoch (pozri nižšie uvedené čísla benchmarkov, vyššie čísla sú lepšie). Phi-3-mini prekonáva modely dvojnásobnej veľkosti, zatiaľ čo Phi-3-small a Phi-3-medium prekonávajú väčšie modely, vrátane GPT-3.5.

**Phi-3-small & medium**

S iba 7 miliardami parametrov Phi-3-small prekonáva GPT-3.5T v rôznych benchmarkoch zameraných na jazyk, uvažovanie, kódovanie a matematiku.

Phi-3-medium s 14 miliardami parametrov pokračuje v tejto línii a prekonáva Gemini 1.0 Pro.

**Phi-3.5-mini**

Môžeme ho považovať za vylepšenie Phi-3-mini. Hoci počet parametrov zostáva nezmenený, zlepšuje schopnosť podporovať viacero jazykov (podpora viac ako 20 jazykov: arabčina, čínština, čeština, dánčina, holandčina, angličtina, fínčina, francúzština, nemčina, hebrejčina, maďarčina, taliančina, japončina, kórejčina, norčina, poľština, portugalčina, ruština, španielčina, švédčina, thajčina, turečtina, ukrajinčina) a pridáva silnejšiu podporu pre dlhý kontext.

Phi-3.5-mini s 3,8 miliardami parametrov prekonáva jazykové modely rovnakej veľkosti a je na úrovni modelov dvojnásobnej veľkosti.

### Phi-3 / 3.5 Vision

Môžeme si predstaviť model Instruct Phi-3/3.5 ako schopnosť Phi rozumieť, a Vision je to, čo Phi dáva oči na pochopenie sveta.


**Phi-3-Vision**

Phi-3-vision, s iba 4,2 miliardami parametrov, pokračuje v tejto línii a prekonáva väčšie modely ako Claude-3 Haiku a Gemini 1.0 Pro V v úlohách všeobecného vizuálneho uvažovania, OCR a porozumení tabuliek a diagramov.


**Phi-3.5-Vision**

Phi-3.5-Vision je tiež vylepšením Phi-3-Vision, pridáva podporu pre viacero obrázkov. Môžete si to predstaviť ako zlepšenie videnia, nielenže vidíte obrázky, ale aj videá.

Phi-3.5-vision prekonáva väčšie modely ako Claude-3.5 Sonnet a Gemini 1.5 Flash v úlohách OCR, porozumenia tabuliek a grafov a je na rovnakej úrovni v úlohách všeobecného vizuálneho uvažovania. Podporuje viacnásobný vstup viacerých snímok, t.j. vykonáva uvažovanie nad viacerými vstupnými obrázkami.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** umožňuje modelom byť predtrénované s oveľa nižšou výpočtovou náročnosťou, čo znamená, že môžete výrazne zväčšiť veľkosť modelu alebo datasetu s rovnakým výpočtovým rozpočtom ako hustý model. Konkrétne, MoE model dosiahne počas predtréningu rovnakú kvalitu ako jeho hustý náprotivok omnoho rýchlejšie.

Phi-3.5-MoE obsahuje 16 modulov expertov po 3,8 miliardy. Phi-3.5-MoE s iba 6,6 miliardami aktívnych parametrov dosahuje podobnú úroveň uvažovania, porozumenia jazyka a matematiky ako omnoho väčšie modely.

Môžeme používať modely rodiny Phi-3/3.5 na základe rôznych scenárov. Na rozdiel od LLM môžete nasadiť Phi-3/3.5-mini alebo Phi-3/3.5-Vision na edge zariadeniach.


## Ako používať modely rodiny Phi-3/3.5

Chceme používať Phi-3/3.5 v rôznych scenároch. Ďalej použijeme Phi-3/3.5 v rôznych situáciách.

![phi3](../../../translated_images/sk/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inference cez Cloud API

**Microsoft Foundry Models**

> **Poznámka:** GitHub Models končia na konci júla 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) je ich priama náhrada.

Microsoft Foundry Models je najpriamejší spôsob. Môžete rýchlo pristúpiť k modelu Phi-3/3.5-Instruct cez katalóg Foundry modelov. V kombinácii so SDK Azure AI Inference / OpenAI SDK môžete API volať cez kód na dokončenie volania Phi-3/3.5-Instruct. Rôzne efekty môžete tiež testovať cez Playground.

- Demo: Porovnanie efektov Phi-3-mini a Phi-3.5-mini v čínskych scenároch

![phi3](../../../translated_images/sk/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/sk/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Alebo ak chcete použiť vizuálne a MoE modely, môžete použiť Microsoft Foundry na dokončenie volania. Ak máte záujem, môžete si prečítať Phi-3 Cookbook, ako volať Phi-3/3.5 Instruct, Vision, MoE cez Microsoft Foundry [Kliknite na tento odkaz](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Okrem cloudového katalógu Microsoft Foundry Models môžete tiež využiť [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) na vykonanie súvisiacich volaní. Môžete navštíviť NVIDIA NIM pre uskutočnenie API volaní rodiny Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) je súbor zrýchlených inferenčných mikroslužieb určených na efektívne nasadenie AI modelov naprieč rôznymi prostrediami vrátane cloudov, dátových centier a pracovných staníc.

Tu sú niektoré kľúčové vlastnosti NVIDIA NIM:

- **Jednoduchosť nasadenia:** NIM umožňuje nasadenie AI modelov jediným príkazom, čo zjednodušuje integráciu do existujúcich pracovných tokov.
- **Optimalizovaný výkon:** Využíva predoptimalizované inferenčné jadrá NVIDIA, ako TensorRT a TensorRT-LLM, pre zabezpečenie nízkej latencie a vysokej priepustnosti.
- **Škálovateľnosť:** NIM podporuje autoskalovanie na Kubernetes, čo umožňuje efektívne spracovanie meniacich sa záťaží.
- **Bezpečnosť a kontrola:** Organizácie môžu zachovať kontrolu nad svojimi dátami a aplikáciami prostredníctvom vlastného hosťovania NIM mikroslužieb na ich spravovanej infraštruktúre.
- **Štandardné API:** NIM poskytuje priemyselne štandardné API, čo uľahčuje vytváranie a integráciu AI aplikácií ako chatboty, AI asistenti a ďalšie.

NIM je súčasťou NVIDIA AI Enterprise, ktorého cieľom je zjednodušiť nasadenie a prevádzkovanie AI modelov, zabezpečujúc ich efektívne spúšťanie na NVIDIA GPU.

- Demo: Použitie NVIDIA NIM na volanie Phi-3.5-Vision-API [[Kliknite na tento odkaz](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Spustenie Phi-3/3.5 lokálne
Inferencia v súvislosti s Phi-3, alebo akýmkoľvek jazykovým modelom ako GPT-3, označuje proces generovania odpovedí alebo predpovedí na základe prijatého vstupu. Keď poskytnete Phi-3 prompt alebo otázku, využije svoj trénovaný neurónový model na odvodenie najpravdepodobnejšej a relevantnej odpovede analyzovaním vzorov a vzťahov v dátach, na ktorých bol trénovaný.

**Hugging Face Transformer**
Hugging Face Transformers je výkonná knižnica určená pre spracovanie prirodzeného jazyka (NLP) a ďalšie úlohy strojového učenia. Tu sú niektoré kľúčové body o nej:

1. **Predtrénované modely**: Poskytuje tisíce predtrénovaných modelov, ktoré možno použiť na rôzne úlohy ako klasifikácia textu, rozpoznávanie pomenovaných entít, odpovedanie na otázky, sumarizácia, preklad a generovanie textu.

2. **Interoperabilita rámcov**: Knižnica podporuje viaceré rámce hlbokého učenia, vrátane PyTorch, TensorFlow a JAX. To umožňuje trénovať model v jednom rámci a použiť ho v inom.

3. **Multimodálne schopnosti**: Okrem NLP Hugging Face Transformers podporuje aj úlohy v počítačovom videní (napr. klasifikácia obrázkov, detekcia objektov) a spracovaní zvuku (napr. rozpoznávanie reči, klasifikácia zvuku).

4. **Jednoduchosť použitia**: Knižnica ponúka API a nástroje na jednoduché stiahnutie a doladenie modelov, vďaka čomu je prístupná pre začiatočníkov aj odborníkov.

5. **Komunita a zdroje**: Hugging Face má živú komunitu a rozsiahlu dokumentáciu, návody a príručky, ktoré pomáhajú používateľom začať a vyťažiť maximum z knižnice.
[oficiálna dokumentácia](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) alebo ich [GitHub úložisko](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Toto je najčastejšie používaná metóda, ale tiež vyžaduje akceleráciu pomocou GPU. Scenáre ako Vision a MoE vyžadujú veľa výpočtov, ktoré budú na CPU veľmi pomalé, ak nie sú kvantizované.


- Demo: Použitie Transformer na volanie Phi-3.5-Instruct [Kliknite na tento odkaz](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Použitie Transformer na volanie Phi-3.5-Vision [Kliknite na tento odkaz](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Použitie Transformer na volanie Phi-3.5-MoE [Kliknite na tento odkaz](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) je platforma navrhnutá na jednoduchšie spúšťanie veľkých jazykových modelov (LLM) lokálne na vašom zariadení. Podporuje rôzne modely ako Llama 3.1, Phi 3, Mistral a Gemma 2, medzi inými. Platforma zjednodušuje proces tým, že spája váhy modelu, konfiguráciu a údaje do jedného balíka, čím je prístupnejšia pre používateľov, ktorí chcú modely prispôsobiť a vytvárať vlastné. Ollama je dostupná pre macOS, Linux a Windows. Je to skvelý nástroj, ak chcete experimentovať s LLM alebo ich nasadiť bez spoliehania sa na cloudové služby. Ollama je najpriamejší spôsob, stačí spustiť nasledujúci príkaz.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) je Microsoftov offline runtime na zariadení pre spúšťanie modelov ako Phi kompletne na vašom hardvéri - nie je potrebné predplatné Azure, API kľúč ani sieťové pripojenie. Automaticky vyberá najlepšie dostupné výkonné zariadenie (NPU, GPU alebo CPU) a vystavuje endpoint kompatibilný s OpenAI, takže existujúci `openai`/Azure AI Inference SDK kód môže naň smerovať s minimálnymi zmenami. Pozrite si [Foundry Local dokumentáciu](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst), aby ste začali.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Alebo používajte SDK priamo v Pythone:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime pre GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) je multiplatformový akcelerátor inferencie a tréningu strojového učenia. ONNX Runtime pre Generative AI (GENAI) je výkonný nástroj, ktorý pomáha efektívne spúšťať generatívne AI modely na rôznych platformách.

## Čo je ONNX Runtime?
ONNX Runtime je open-source projekt, ktorý umožňuje vysokovýkonnú inferenciu strojovo učených modelov. Podporuje modely vo formáte Open Neural Network Exchange (ONNX), ktorý je štandardom pre reprezentáciu modelov strojového učenia. Inferencia v ONNX Runtime môže umožniť rýchlejšie zákaznícke skúsenosti a nižšie náklady, podporujúc modely z rámcov hlbokého učenia ako PyTorch a TensorFlow/Keras, ale aj klasické knižnice strojového učenia ako scikit-learn, LightGBM, XGBoost a pod. ONNX Runtime je kompatibilný s rôznym hardvérom, ovládačmi a operačnými systémami a poskytuje optimálny výkon využívaním hardvérových akcelerátorov, kde je to možné, spolu s optimalizáciami a transformáciami grafu.

## Čo je Generatívna AI?
Generatívna AI označuje AI systémy, ktoré môžu generovať nový obsah, ako text, obrázky alebo hudbu, na základe údajov, na ktorých boli trénované. Príklady zahŕňajú jazykové modely ako GPT-3 a modely generovania obrázkov ako Stable Diffusion. Knižnica ONNX Runtime pre GenAI poskytuje generatívnu AI slučku pre ONNX modely vrátane inferencie s ONNX Runtime, spracovania logitov, vyhľadávania a vzorkovania, a správy KV cache.

## ONNX Runtime pre GENAI
ONNX Runtime pre GENAI rozširuje schopnosti ONNX Runtime na podporu generatívnych AI modelov. Tu sú niektoré kľúčové funkcie:

- **Široká podpora platforiem:** Funguje na rôznych platformách vrátane Windows, Linux, macOS, Android a iOS.
- **Podpora modelov:** Podporuje mnoho populárnych generatívnych AI modelov ako LLaMA, GPT-Neo, BLOOM a ďalšie.
- **Optimalizácia výkonu:** Zahŕňa optimalizácie pre rôzne hardvérové akcelerátory ako NVIDIA GPU, AMD GPU a ďalšie2.
- **Jednoduchosť použitia:** Poskytuje API pre jednoduchú integráciu do aplikácií, čo umožňuje generovať text, obrázky a ďalší obsah s minimálnym kódom
- Používatelia môžu volať vysokú úroveň metódy generate(), alebo spúšťať každú iteráciu modelu v slučke, generujúc jeden token po druhom, s možnosťou aktualizácie parametrov generovania v rámci slučky.
- ONNX Runtime tiež podporuje greedy/beam vyhľadávanie a TopP, TopK vzorkovanie na generovanie sekvencií tokenov a zabudované spracovanie logitov ako penalizácie opakovania. Môžete tiež ľahko pridať vlastné hodnotenie.

## Začíname
Na začiatok s ONNX Runtime pre GENAI môžete postupovať podľa týchto krokov:

### Inštalácia ONNX Runtime:
```Python
pip install onnxruntime
```
### Inštalácia rozšírení Generative AI:
```Python
pip install onnxruntime-genai
```

### Spustenie modelu: Tu je jednoduchý príklad v Pythone:
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

Okrem referenčných metód ONNX Runtime, Ollama a Foundry Local, môžeme tiež doplniť referenciu kvantitatívnych modelov založených na metodách referencie modelov poskytovaných rôznymi výrobcami. Napríklad Apple MLX framework s Apple Metal, Qualcomm QNN s NPU, Intel OpenVINO s CPU/GPU a podobne. Viac informácií nájdete v [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Viac

Naučili sme sa základy rodiny Phi-3/3.5, ale aby sme sa dozvedeli viac o SLM, potrebujeme ďalšie poznatky. Odpovede nájdete v Phi-3 Cookbook. Ak chcete vedieť viac, navštívte prosím [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->