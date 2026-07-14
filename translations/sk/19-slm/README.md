# Úvod do malých jazykových modelov pre generatívnu AI pre začiatočníkov
Generatívna AI je fascinujúca oblasť umelej inteligencie, ktorá sa zameriava na tvorbu systémov schopných generovať nový obsah. Tento obsah môže zahŕňať texty, obrázky, hudbu a dokonca celé virtuálne prostredia. Jednou z najzaujímavejších aplikácií generatívnej AI sú jazykové modely.

## Čo sú malé jazykové modely?

Malý jazykový model (SLM) predstavuje zmenšenú variantu veľkého jazykového modelu (LLM), ktorá využíva mnohé architektonické princípy a techniky LLM, pričom má výrazne zmenšené výpočtové nároky. 

SLM sú podmnožinou jazykových modelov navrhnutých na generovanie textu podobného ľudskému. Na rozdiel od ich väčších prototypov, ako je GPT-4, sú SLM kompaktné a efektívne, čo ich robí ideálnymi pre aplikácie s obmedzenými výpočtovými zdrojmi. Napriek ich menšej veľkosti dokážu vykonávať rôzne úlohy. SLM sú zvyčajne vytvárané kompresiou alebo destiláciou LLM, s cieľom zachovať podstatnú časť funkčnosti a jazykových schopností pôvodného modelu. Zmenšenie veľkosti modelu znižuje jeho celkovú zložitosť, čím sa SLM stávajú efektívnejšími z hľadiska využitia pamäte aj výpočtových požiadaviek. Napriek týmto optimalizáciám dokážu SLM vykonávať široké spektrum úloh spracovania prirodzeného jazyka (NLP):

- Generovanie textu: Tvorba koherentných a kontextovo relevantných viet alebo odstavcov.
- Dokončovanie textu: Predikcia a dopĺňanie viet na základe zadanej výzvy.
- Preklad: Prevod textu z jedného jazyka do druhého.
- Zhrnutie: Skracovanie dlhých textov na kratšie, ľahšie stráviteľné zhrnutia.

Aj keď s určitými kompromismi v oblasti výkonu alebo hĺbky porozumenia v porovnaní s väčšími modelmi.

## Ako fungujú malé jazykové modely?
SLM sú trénované na obrovskom množstve textových dát. Počas tréningu sa učia vzory a štruktúry jazyka, čo im umožňuje generovať text, ktorý je gramaticky správny a kontextovo vhodný. Tréningový proces zahŕňa:

- Zber dát: Zhromažďovanie veľkých datasetov textov z rôznych zdrojov.
- Predspracovanie: Čistenie a organizovanie dát, aby boli vhodné na tréning.
- Tréning: Použitie algoritmov strojového učenia na výučbu modelu porozumieť a generovať text.
- Doladenie: Nastavenie modelu na zlepšenie jeho výkonu v špecifických úlohách.

Vývoj SLM prispieva k rastúcej potrebe modelov, ktoré je možné nasadiť v prostrediach s obmedzenými zdrojmi, ako sú mobilné zariadenia alebo edge computing platformy, kde plnohodnotné LLM môžu byť nepraktické kvôli veľkým nárokom na zdroje. Zameraním sa na efektivitu dosahujú SLM rovnováhu medzi výkonom a dostupnosťou, čo umožňuje ich širšie uplatnenie v rôznych oblastiach.

![slm](../../../translated_images/sk/slm.4058842744d0444a.webp)

## Ciele učenia

V tejto lekcii chceme predstaviť poznatky o SLM a spojiť ich s Microsoft Phi-3, aby sme sa naučili rôzne scenáre v oblasti textového obsahu, vizuálneho vnímania a MoE.

Na konci tejto lekcie by ste mali byť schopní odpovedať na nasledujúce otázky:

- Čo je SLM?
- Aký je rozdiel medzi SLM a LLM?
- Čo je rodina Microsoft Phi-3/3.5?
- Ako spustiť inferenciu pomocou rodiny Microsoft Phi-3/3.5?

Pripravení? Poďme na to.

## Rozdiely medzi veľkými jazykovými modelmi (LLM) a malými jazykovými modelmi (SLM)

LLM i SLM sú postavené na základných princípoch pravdepodobnostného strojového učenia, využívajú podobné prístupy v architektúre, metódach tréningu, procesoch generovania dát a vyhodnocovania modelov. Napriek tomu niekoľko kľúčových faktorov odlišuje tieto dva typy modelov.

## Aplikácie malých jazykových modelov

SLM majú široké využitie, vrátane:

- Chatboty: Poskytovanie zákazníckej podpory a interakcia s užívateľmi konverzačným spôsobom.
- Tvorba obsahu: Pomoc spisovateľom generovaním nápadov alebo dokonca celých článkov.
- Vzdelávanie: Pomoc študentom s písaním úloh alebo učením sa nových jazykov.
- Prístupnosť: Vytváranie nástrojov pre osoby so zdravotným postihnutím, ako sú systémy na preklad textu na reč.

**Veľkosť**
  
Primárny rozdiel medzi LLM a SLM spočíva v rozsahu modelov. LLM, ako napríklad ChatGPT (GPT-4), môžu mať približne 1,76 bilióna parametrov, zatiaľ čo open-source SLM ako Mistral 7B majú významne menej parametrov – približne 7 miliárd. Tento rozdiel je predovšetkým spôsobený architektúrou modelu a procesmi tréningu. Napríklad ChatGPT používa mechanizmus self-attention v rámci encoder-decoder konštrukcie, zatiaľ čo Mistral 7B využíva sliding window attention, čo umožňuje efektívnejší tréning v rámci modelu s iba dekóderom. Táto architektonická odlišnosť má hlboký vplyv na zložitosť a výkon modelov.

**Porozumenie**

SLM sú zvyčajne optimalizované na výkon v konkrétnych oblastiach, čo ich robí vysoko špecializovanými, ale potenciálne obmedzenými v schopnosti poskytovať široké kontextové porozumenie naprieč viacerými vednými oblasťami. Naopak, LLM sa snažia simulovať ľudskú inteligenciu na komplexnejšej úrovni. Trénované na obrovských, rozmanitých datasetoch, LLM sú navrhnuté na dobrý výkon v rôznych oblastiach, ponúkajú väčšiu všestrannosť a prispôsobivosť. Preto sú LLM vhodnejšie na širšie spektrum následných úloh, ako je spracovanie prirodzeného jazyka a programovanie.

**Počítačové zdroje**

Tréning a nasadenie LLM sú procesy náročné na zdroje, často vyžadujúce rozsiahlu výpočtovú infraštruktúru vrátane veľkých GPU klastrov. Napríklad výcvik modelu ako ChatGPT od základu môže vyžadovať tisíce GPU počas dlhých časových úsekov. Naopak, SLM s menším počtom parametrov sú dostupnejšie z hľadiska výpočtových zdrojov. Modely ako Mistral 7B môžu byť trénované a prevádzkované na lokálnych zariadeniach so strednými GPU, hoci tréning vyžaduje niekoľko hodín na viacerých GPU.

**Zaujatosti**

Zaujatosti sú známy problém LLM, predovšetkým kvôli charakteru tréningových dát. Tieto modely často používajú surové, verejne dostupné údaje z internetu, ktoré môžu nedostatočne alebo nesprávne reprezentovať určité skupiny, obsahovať nesprávne označenia alebo odrážať jazykové zaujatosti ovplyvnené dialektom, geografickými odlišnosťami a gramatickými pravidlami. Okrem toho zložitosť LLM architektúry môže neúmyselne zhoršiť tieto zaujatosti, ktoré môžu zostať nepovšimnuté bez dôkladného doladenia. SLM, ktoré sú trénované na úzke, doménovo špecifické datasety, sú v tomto ohľade prirodzene menej náchylné na takéto zaujatosti, hoci im nie sú úplne imúnne.

**Inferencia**

Zmenšená veľkosť SLM im poskytuje výraznú výhodu v rýchlosti inferencie, čo im umožňuje efektívne generovať výstupy na lokálnom hardvéri bez potreby rozsiahleho paralelného spracovania. Naopak, LLM kvôli svojej veľkosti a zložitosti často vyžadujú značné paralelné výpočtové zdroje na dosiahnutie prijateľného času inferencie. Prítomnosť viacerých súbežných užívateľov navyše spomaľuje reakčný čas LLM, najmä pri nasadení vo veľkom meradle.

Zhrnutím, aj keď LLM a SLM zdieľajú základné princípy strojového učenia, líšia sa výrazne vo veľkosti modelu, požiadavkách na zdroje, schopnosti pochopenia kontextu, náchylnosti na zaujatosti a rýchlosti inferencie. Tieto odlišnosti odrážajú ich vhodnosť pre rôzne použitia, pričom LLM sú všestrannejšie, ale náročné na zdroje, zatiaľ čo SLM ponúkajú efektivitu v konkrétnych oblastiach s nižšími výpočtovými požiadavkami.

***Poznámka: V tejto lekcii predstavíme SLM na príklade Microsoft Phi-3 / 3.5.***

## Predstavenie rodiny Phi-3 / Phi-3.5

Rodina Phi-3 / 3.5 sa zameriava hlavne na scenáre aplikácií textu, videnia a Agenta (MoE):

### Phi-3 / 3.5 Instruct

Hlavne pre generovanie textu, dokončenie rozhovorov a extrakciu obsahu informácií, atď.

**Phi-3-mini**

3,8 miliardový jazykový model je dostupný na Microsoft Foundry, Hugging Face a Ollama. Modely Phi-3 výrazne prekonávajú jazykové modely rovnakej alebo väčšej veľkosti na kľúčových benchmarkoch (pozri nižšie benchmarkové výsledky, vyššie čísla sú lepšie). Phi-3-mini prekonáva modely dvojnásobnej veľkosti, zatiaľ čo Phi-3-small a Phi-3-medium prekonávajú väčšie modely, vrátane GPT-3.5.

**Phi-3-small & medium**

S iba 7 miliardami parametrov Phi-3-small prekonáva GPT-3.5T v rôznych jazykových, úsudkových, kódovacích a matematických benchmarkoch.

Phi-3-medium s 14 miliardami parametrov pokračuje v tomto trende a prekonáva Gemini 1.0 Pro.

**Phi-3.5-mini**

Môžeme ho považovať za upgrade Phi-3-mini. Parametre zostávajú nezmenené, no zlepšuje schopnosť podporovať viacero jazykov (podporuje viac ako 20 jazykov: arabčina, čínština, čeština, dánčina, holandčina, angličtina, finština, francúzština, nemčina, hebrejčina, maďarčina, taliančina, japončina, kórejčina, nórčina, poľština, portugalčina, ruština, španielčina, švédčina, thajčina, turečtina, ukrajinčina) a pridáva silnejšiu podporu dlhých kontextov.

Phi-3.5-mini s 3,8 miliardami parametrov prekonáva jazykové modely rovnakej veľkosti a je na úrovni modelov dvojnásobnej veľkosti.

### Phi-3 / 3.5 Vision

Môžeme si model Instruct Phi-3/3.5 predstaviť ako schopnosť Phi porozumieť, a Vision je to, čo Phi dáva oči, aby rozumel svetu.


**Phi-3-Vision**

Phi-3-vision, s iba 4,2 miliardami parametrov, pokračuje v tomto trende a prekonáva väčšie modely ako Claude-3 Haiku a Gemini 1.0 Pro V v úlohách všeobecného vizuálneho úsudku, OCR a pochopenia tabuliek a diagramov.


**Phi-3.5-Vision**

Phi-3.5-Vision je tiež upgrade Phi-3-Vision, pridávajúci podporu viacerých obrázkov. Môžete si ho predstaviť ako vylepšené videnie, nielenže vidíte obrázky, ale aj videá.

Phi-3.5-vision prekonáva väčšie modely ako Claude-3.5 Sonnet a Gemini 1.5 Flash v úlohách OCR, pochopenia tabuliek a grafov a je na úrovni pri úlohách vizuálneho všeobecného poznania. Podporuje viacnásobné vstupy, t.j. vykonáva úsudok na viacerých vstupných obrázkoch.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** umožňuje trénovanie modelov s oveľa menšou výpočtovou záťažou, čo znamená, že možno dramaticky zväčšiť veľkosť modelu alebo datasetu za rovnaký výpočtový rozpočet ako hustý model. Konkrétne, MoE model by mal dosiahnuť rovnakú kvalitu ako jeho hustý prototyp oveľa rýchlejšie počas predtrénovania.

Phi-3.5-MoE obsahuje 16 modulov expertov s kapacitou 3,8 miliardy parametrov. Phi-3.5-MoE s iba 6,6 miliardou aktívnych parametrov dosahuje podobnú úroveň úsudku, porozumenia jazyka a matematiky ako oveľa väčšie modely.

Môžeme využiť modely rodiny Phi-3/3.5 na rôzne scenáre. Na rozdiel od LLM môžete nasadiť Phi-3/3.5-mini alebo Phi-3/3.5-Vision na edge zariadeniach.


## Ako používať modely rodiny Phi-3/3.5

Dúfame, že využijeme Phi-3/3.5 v rôznych scenároch. Nasledujúca časť ukáže použitie Phi-3/3.5 podľa rôznych scén.

![phi3](../../../translated_images/sk/phi3.655208c3186ae381.webp)

### Inferencia cez cloudové API

**Microsoft Foundry Models**

> **Poznámka:** GitHub Models končí na konci júla 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) je priamou náhradou.

Microsoft Foundry Models je najpriamejšou cestou. Model Phi-3/3.5-Instruct môžete rýchlo vyvolať cez katalóg Foundry modelov. V spojení s Azure AI Inference SDK / OpenAI SDK získate prístup k API kódom na vykonanie volania Phi-3/3.5-Instruct. Rozohrávací priestor (Playground) tiež umožňuje testovať rôzne výsledky.

- Demo: Porovnanie výsledkov Phi-3-mini a Phi-3.5-mini v čínskych scénach

![phi3](../../../translated_images/sk/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/sk/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Ak chcete použiť modely Vision a MoE, môžete využiť Microsoft Foundry na ich vyvolanie. Ak máte záujem, môžete si prečítať Phi-3 Cookbook a naučiť sa, ako volať Phi-3/3.5 Instruct, Vision, MoE cez Microsoft Foundry [Kliknite na tento odkaz](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Okrem cloudového katalógu Microsoft Foundry Models môžete použiť aj [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) na vykonanie súvisiacich volaní. Na NVIDIA NIM môžete vyvolať API modelov rodiny Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) je sada zrýchlených mikroservisov inferencie určených na efektívne nasadenie AI modelov v rôznych prostrediach, vrátane cloudov, dátových centier a pracovných staníc.

Tu sú niektoré kľúčové vlastnosti NVIDIA NIM:

- **Jednoduchosť nasadenia:** NIM umožňuje nasadiť AI modely jedným príkazom, čo zjednodušuje integráciu do existujúcich pracovných tokov.

- **Optimalizovaný výkon:** Využíva predoptimalizované inferenčné jadrá NVIDIA, ako TensorRT a TensorRT-LLM, aby zabezpečil nízku latenciu a vysokú priepustnosť.
- **Škálovateľnosť:** NIM podporuje autoskalovanie v Kubernetes, čo mu umožňuje efektívne zvládať rôzne zaťaženia.
- **Bezpečnosť a kontrola:** Organizácie môžu udržiavať kontrolu nad svojimi dátami a aplikáciami tým, že si sami hosťujú NIM mikroservisy na vlastnej spravovanej infraštruktúre.
- **Štandardné API:** NIM poskytuje priemyselné štandardné API, čo uľahčuje budovanie a integráciu AI aplikácií ako chatboty, AI asistenti a ďalšie.

NIM je súčasťou NVIDIA AI Enterprise, ktorý sa snaží zjednodušiť nasadenie a prevádzkovanie AI modelov, čím zabezpečuje ich efektívny chod na NVIDIA GPU.

- Demo: Použitie NVIDIA NIM na volanie Phi-3.5-Vision-API  [[Kliknite na tento odkaz](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Spúšťanie Phi-3/3.5 lokálne
Inferencia v súvislosti s Phi-3, alebo akýmkoľvek jazykovým modelom ako GPT-3, označuje proces generovania odpovedí alebo predikcií na základe prijatého vstupu. Keď zadáte prompt alebo otázku Phi-3, používa svoj trénovaný neurónový model na odvodenie najpravdepodobnejšej a relevantnej odpovede analýzou vzorov a vzťahov v dátach, na ktorých bol trénovaný.

**Hugging Face Transformer**
Hugging Face Transformers je výkonná knižnica navrhnutá pre spracovanie prirodzeného jazyka (NLP) a ďalšie úlohy strojového učenia. Tu sú niektoré kľúčové body:

1. **Predtrénované modely**: Poskytuje tisíce predtrénovaných modelov, ktoré možno využiť na rôzne úlohy ako klasifikácia textu, rozpoznávanie pomenovaných entít, odpovedanie na otázky, sumarizácia, preklad a generovanie textu.

2. **Interoperabilita frameworkov**: Knižnica podporuje viacero hlbokých učiacich frameworkov, vrátane PyTorch, TensorFlow a JAX. Umožňuje trénovať model v jednom frameworku a použiť ho v inom.

3. **Multimodálne schopnosti**: Okrem NLP Hugging Face Transformers tiež podporuje úlohy v počítačovom videní (napr. klasifikácia obrázkov, detekcia objektov) a spracovanie audiozáznamov (napr. rozpoznávanie reči, klasifikácia zvuku).

4. **Jednoduchosť použitia**: Knižnica ponúka API a nástroje na jednoduché stiahnutie a doladenie modelov, vďaka čomu je prístupná pre začiatočníkov i expertov.

5. **Komunita a zdroje**: Hugging Face má živú komunitu a rozsiahlu dokumentáciu, tutoriály a návody, ktoré pomáhajú používateľom začať a využiť knižnicu naplno.
[oficiálna dokumentácia](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) alebo ich [GitHub repo](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Toto je najbežnejšie používaná metóda, ale tiež vyžaduje GPU akceleráciu. Scenáre ako Vision a MoE vyžadujú veľa výpočtov, ktoré by na CPU boli veľmi pomalé, ak nie sú kvantizované.


- Demo: Použitie Transformer na volanie Phi-3.5-Instruct [Kliknite na tento odkaz](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Použitie Transformer na volanie Phi-3.5-Vision [Kliknite na tento odkaz](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Použitie Transformer na volanie Phi-3.5-MoE [Kliknite na tento odkaz](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) je platforma určená na jednoduchšie spúšťanie veľkých jazykových modelov (LLM) lokálne na vašom zariadení. Podporuje rôzne modely ako Llama 3.1, Phi 3, Mistral a Gemma 2, medzi inými. Platforma zjednodušuje proces tým, že balí hmotnosti modelu, konfiguráciu a dáta do jedného balíka, čím umožňuje používateľom jednoduchšie prispôsobiť a vytvárať vlastné modely. Ollama je dostupná pre macOS, Linux a Windows. Je to skvelý nástroj, ak chcete experimentovať alebo nasadiť LLM bez závislosti na cloudových službách. Ollama je najpriamejší spôsob, stačí spustiť nasledujúci príkaz.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) je Microsoftov offline runtime na zariadení na spúšťanie modelov ako Phi úplne na vašom vlastnom hardvéri – nie je potrebné predplatné Azure, API kľúč ani sieťové pripojenie. Automaticky vyberá najlepší dostupný vykonávací poskytovateľ (NPU, GPU alebo CPU) a sprístupňuje endpoint kompatibilný s OpenAI, takže existujúci kód `openai`/Azure AI Inference SDK môžete smerovať na neho s minimálnymi zmenami. Pre začiatok pozrite [Foundry Local dokumentáciu](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst).

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) je multiplatformový akcelerátor inferencie a trénovania strojového učenia. ONNX Runtime pre Generatívnu AI (GENAI) je výkonný nástroj, ktorý vám pomáha efektívne spúšťať generatívne AI modely na rôznych platformách.

## Čo je ONNX Runtime?
ONNX Runtime je open-source projekt, ktorý umožňuje vysokovýkonnú inferenciu modelov strojového učenia. Podporuje modely vo formáte Open Neural Network Exchange (ONNX), ktorý je štandardom pre reprezentáciu modelov strojového učenia. Inferencia ONNX Runtime môže zabezpečiť rýchlejšie zákaznícke skúsenosti a nižšie náklady, podporujúc modely z hlbokých frameworkov ako PyTorch a TensorFlow/Keras, ako aj klasické knižnice strojového učenia ako scikit-learn, LightGBM, XGBoost a ďalšie. ONNX Runtime je kompatibilný s rôznym hardvérom, ovládačmi a operačnými systémami a poskytuje optimálny výkon využitím hardvérových akcelerátorov tam, kde je to možné, spolu s optimalizáciami a transformáciami grafov.

## Čo je Generatívna AI?
Generatívna AI sa týka AI systémov, ktoré dokážu generovať nový obsah, ako text, obrázky alebo hudbu, na základe dát, na ktorých boli trénované. Príklady zahŕňajú jazykové modely ako GPT-3 a modely generovania obrázkov ako Stable Diffusion. Knižnica ONNX Runtime pre GenAI poskytuje generatívnu AI slučku pre ONNX modely, vrátane inferencie s ONNX Runtime, spracovania logitov, vyhľadávania a vzorkovania a správy KV cache.

## ONNX Runtime pre GENAI
ONNX Runtime pre GENAI rozširuje schopnosti ONNX Runtime na podporu generatívnych AI modelov. Tu sú niektoré kľúčové vlastnosti:

- **Široká podpora platforiem:** Funguje na rôznych platformách vrátane Windows, Linux, macOS, Android a iOS.
- **Podpora modelov:** Podporuje mnoho populárnych generatívnych AI modelov ako LLaMA, GPT-Neo, BLOOM a ďalšie.
- **Optimalizácia výkonu:** Obsahuje optimalizácie pre rôzne hardvérové akcelerátory ako NVIDIA GPU, AMD GPU a ďalšie2.
- **Jednoduché použitie:** Poskytuje API pre jednoduchú integráciu do aplikácií, umožňujúc generovať text, obrázky a iný obsah s minimom kódu
- Používatelia môžu vyvolať vysokú úroveň metódy generate(), alebo spustiť každú iteráciu modelu v slučke, generujúc jeden token naraz, a voliteľne meniť parametre generovania vnútri slučky.
- ONNX runtime tiež podporuje greedy/beam search a TopP, TopK sampling na generovanie sekvencií tokenov a vstavané spracovanie logitov ako penalizácie opakovania. Ľahko si môžete pridať aj vlastné skórovanie.

## Začať
Ak chcete začať s ONNX Runtime pre GENAI, môžete nasledovať tieto kroky:

### Nainštalujte ONNX Runtime:
```Python
pip install onnxruntime
```
### Inštalujte rozšírenia pre Generatívnu AI:
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


**Ostatné**

Okrem referenčných metód ONNX Runtime, Ollama a Foundry Local môžeme tiež doplniť referenciu kvantitatívnych modelov založených na referenčných metódach modelov od rôznych výrobcov. Napríklad Apple MLX framework s Apple Metal, Qualcomm QNN s NPU, Intel OpenVINO s CPU/GPU atď. Viac obsahu nájdete aj v [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Viac

Naučili sme sa základy rodiny Phi-3/3.5, ale pre lepšie pochopenie SLM potrebujeme ďalšie vedomosti. Odpovede nájdete v Phi-3 Cookbook. Ak chcete vedieť viac, navštívte prosím [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->