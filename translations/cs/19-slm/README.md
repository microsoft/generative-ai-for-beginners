# Úvod do malých jazykových modelů pro generativní AI pro začátečníky
Generativní AI je fascinující oblast umělé inteligence, která se zaměřuje na vytváření systémů schopných generovat nový obsah. Tento obsah může zahrnovat texty, obrázky, hudbu nebo dokonce celé virtuální prostředí. Jednou z nejzajímavějších aplikací generativní AI jsou jazykové modely.

## Co jsou malé jazykové modely?

Malý jazykový model (SLM) představuje zmenšenou variantu velkého jazykového modelu (LLM), přičemž využívá mnoho architektonických principů a technik LLM, ale vykazuje výrazně sníženou výpočetní náročnost.

SLM jsou podmnožinou jazykových modelů navržených k generování textu podobného lidskému. Na rozdíl od svých větších protějšků, jako je GPT-4, jsou SLM kompaktnější a efektivnější, což je činí ideálními pro aplikace, kde jsou omezené výpočetní zdroje. Přestože jsou menší, dokážou vykonávat různé úkoly. Typicky jsou SLM konstruovány kompresí nebo destilací LLM s cílem zachovat podstatnou část původní funkčnosti a jazykových schopností modelu. Tato redukce velikosti modelu snižuje celkovou složitost, což dělá SLM efektivnějšími jak z hlediska paměťové náročnosti, tak výpočetních požadavků. Navzdory těmto optimalizacím mohou SLM vykonávat širokou škálu úloh zpracování přirozeného jazyka (NLP):

- Generování textu: Vytváření koherentních a kontextuálně relevantních vět nebo odstavců.
- Dokončování textu: Predikce a doplňování vět na základě zadaného promptu.
- Překlad: Převod textu z jednoho jazyka do druhého.
- Shrnutí: Zkrácení dlouhých textů do kratších, snáze stravitelných shrnutí.

I když s určitými kompromisy v oblasti výkonu nebo hloubky porozumění ve srovnání s jejich většími protějšky.

## Jak malé jazykové modely fungují?
SLM jsou trénovány na rozsáhlých množstvích textových dat. Během tréninku se učí vzory a struktury jazyka, což jim umožňuje generovat text, který je gramaticky správný a kontextuálně vhodný. Proces tréninku zahrnuje:

- Shromažďování dat: Sběr velkých datasetů textu z různých zdrojů.
- Předzpracování: Čištění a organizace dat tak, aby byla vhodná pro trénink.
- Trénink: Použití algoritmů strojového učení k výuce modelu, jak rozumět a generovat text.
- Doladění: Úprava modelu pro zlepšení jeho výkonu na specifických úlohách.

Vývoj SLM odpovídá rostoucí potřebě modelů, které lze nasadit v prostředích s omezenými zdroji, jako jsou mobilní zařízení nebo edge computing platformy, kde by plnohodnotné LLM bylo neproveditelné kvůli jejich vysokým nárokům na zdroje. Zaměřením na efektivitu SLM vyvažují výkon a dostupnost, což umožňuje širší využití v různých oblastech.

![slm](../../../translated_images/cs/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Cíle učení

V této lekci bychom rádi představili znalosti o SLM a spojili je s Microsoft Phi-3, abychom se naučili různé scénáře v oblasti textového obsahu, vidění a MoE.

Na konci této lekce byste měli být schopni odpovědět na následující otázky:

- Co je SLM?
- Jaký je rozdíl mezi SLM a LLM?
- Co je rodina Microsoft Phi-3/3.5?
- Jak provést inferenci s rodinou Microsoft Phi-3/3.5?

Připraveni? Pojďme začít.

## Rozdíly mezi velkými jazykovými modely (LLM) a malými jazykovými modely (SLM)

Oba, LLM i SLM, jsou postaveny na základech pravděpodobnostního strojového učení a následují podobné přístupy ve své architektonické konstrukci, metodikách tréninku, procesech generování dat a technikách hodnocení modelů. Nicméně několik klíčových faktorů tyto dva typy modelů odlišuje.

## Aplikace malých jazykových modelů

SLM mají široké spektrum aplikací, včetně:

- Chatboti: Poskytování zákaznické podpory a komunikace s uživateli konverzačním způsobem.
- Tvorba obsahu: Pomoc spisovatelům generováním nápadů nebo dokonce psaním celých článků.
- Vzdělávání: Pomoc studentům s psaním úkolů nebo učením se novým jazykům.
- Dostupnost: Vytváření nástrojů pro osoby se zdravotním postižením, jako jsou systémy převodu textu na řeč.

**Velikost**
  
Hlavní rozdíl mezi LLM a SLM spočívá ve velikosti modelů. LLM, jako ChatGPT (GPT-4), může mít odhadovaných 1,76 bilionu parametrů, zatímco open-source SLM jako Mistral 7B je navržen s výrazně menším počtem parametrů – přibližně 7 miliard. Tento rozdíl je primárně způsoben rozdíly v architektuře modelu a tréninkových procesech. Například ChatGPT využívá mechanismus self-attention v rámci frameworku encoder-decoder, zatímco Mistral 7B používá sliding window attention, který umožňuje efektivnější trénink v modelu pouze s dekodérem. Tato architektonická varianta má hluboký vliv na složitost a výkon těchto modelů.

**Porozumění**

SLM jsou typicky optimalizovány pro výkon v konkrétních doménách, což je činí vysoce specializovanými, ale potenciálně omezenými v jejich schopnosti poskytnout široké kontextuální porozumění napříč různými obory. Naopak LLM cílí na simulaci lidské inteligence na komplexnější úrovni. Trénované na rozsáhlých a rozmanitých datech jsou LLM navrženy tak, aby dobře fungovaly v různých oblastech a nabízely větší všestrannost a adaptabilitu. Proto jsou LLM vhodnější pro širší škálu následných úloh, jako je zpracování přirozeného jazyka a programování.

**Výpočetní nároky**

Trénink a nasazení LLM jsou procesy náročné na zdroje, často vyžadující rozsáhlou výpočetní infrastrukturu, včetně rozsáhlých GPU klastrů. Například trénink modelu jako ChatGPT od nuly může vyžadovat tisíce GPU po dlouhou dobu. Naopak SLM, s menším počtem parametrů, jsou dostupnější z hlediska výpočetních zdrojů. Modely jako Mistral 7B lze trénovat a provozovat na lokálních strojích vybavených středními GPU kapacitami, přesto však trénink vyžaduje několik hodin na více GPU.

**Bias**

Bias je známý problém LLM, především kvůli povaze tréninkových dat. Tyto modely často spoléhají na surová, veřejně dostupná data z internetu, která mohou nedostatečně zastupovat nebo nesprávně reprezentovat určité skupiny, zavádět chybné označení či odrážet jazykové předsudky způsobené dialekty, geografickými variacemi a gramatickými pravidly. Navíc komplexita architektur LLM může nechtěně zesilovat bias, který může zůstat nepovšimnut bez pečlivého doladění. Na druhé straně SLM, které jsou trénovány na omezenějších, doménově specifických datech, jsou inherentně méně náchylné k takovým biasům, i když nejsou úplně imunní.

**Inference**

Zmenšená velikost SLM jim poskytuje významnou výhodu v rychlosti inference, což jim umožňuje efektivně generovat výstupy na místním hardwaru bez potřeby rozsáhlého paralelního zpracování. Naopak LLM, kvůli jejich velikosti a složitosti, často vyžadují značné paralelní výpočetní zdroje pro dosažení přijatelné doby odezvy. Přítomnost více současných uživatelů dále zpomaluje dobu odezvy LLM, zejména při nasazení ve velkém měřítku.

Shrnutí, zatímco LLM i SLM mají společný základ ve strojovém učení, výrazně se liší co do velikosti modelu, požadavků na zdroje, kontextuálního porozumění, náchylnosti k biasu a rychlosti inference. Tyto rozdíly odrážejí jejich vhodnost pro různé případy použití, přičemž LLM jsou univerzálnější, ale náročnější na zdroje, a SLM nabízejí efektivitu v konkrétních doménách s nižšími výpočetními nároky.

***Poznámka: V této lekci představíme SLM na příkladu Microsoft Phi-3 / 3.5.***

## Představení rodiny Phi-3 / Phi-3.5

Rodina Phi-3 / 3.5 je primárně určena pro scénáře textu, vidění a aplikace Agent (MoE):

### Phi-3 / 3.5 Instruct

Především pro generování textu, dokončování konverzací a extrakci informací z obsahu atd.

**Phi-3-mini**

Jazykový model s 3,8 miliardami parametrů je dostupný na Microsoft Foundry, Hugging Face a Ollama. Modely Phi-3 výrazně překonávají jazykové modely stejné i větší velikosti na hlavních benchmarkových testech (viz benchmarková čísla níže, vyšší čísla jsou lepší). Phi-3-mini překonává modely dvojnásobné velikosti, zatímco Phi-3-small a Phi-3-medium překonávají větší modely včetně GPT-3.5.

**Phi-3-small & medium**

S pouhými 7 miliardami parametrů Phi-3-small překonává GPT-3.5T v řadě jazykových, logických, programovacích a matematických benchmarků.

Phi-3-medium s 14 miliardami parametrů pokračuje v tomto trendu a překonává Gemini 1.0 Pro.

**Phi-3.5-mini**

Můžeme jej považovat za upgrade Phi-3-mini. Parametry zůstávají nezměněné, ale zlepšuje se schopnost podpory více jazyků (podpora více než 20 jazyků: arabština, čínština, čeština, dánština, holandština, angličtina, finština, francouzština, němčina, hebrejština, maďarština, italština, japonština, korejština, norština, polština, portugalština, ruština, španělština, švédština, thajština, turečtina, ukrajinština) a přidává silnější podporu dlouhých kontextů.

Phi-3.5-mini s 3,8 miliardami parametrů překonává jazykové modely stejné velikosti a je srovnatelný s modely dvojnásobné velikosti.

### Phi-3 / 3.5 Vision

Instruct model Phi-3/3.5 můžeme chápat jako schopnost Phi porozumět, a Vision je to, co Phi dává oči, aby porozuměl světu.


**Phi-3-Vision**

Phi-3-vision s pouhými 4,2 miliardami parametrů pokračuje v tomto trendu a překonává větší modely jako Claude-3 Haiku a Gemini 1.0 Pro V v obecných vizuálních úlohách, OCR, a porozumění tabulkám a diagramům.


**Phi-3.5-Vision**

Phi-3.5-Vision je také upgrade Phi-3-Vision, přidává podporu pro více obrázků. Můžete jej vnímat jako vylepšení vidění, kdy už nevidíte pouze fotografie, ale také videa.

Phi-3.5-vision překonává větší modely jako Claude-3.5 Sonnet a Gemini 1.5 Flash v OCR, porozumění tabulkám a grafům a je na stejné úrovni v obecném vizuálním porozumění. Podporuje více snímkové vstupy, tj. provádí odvozování na více vstupních obrázcích.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** umožňuje modelům být předtrénovány s mnohem menší výpočetní náročností, což znamená, že můžete dramaticky zvětšit velikost modelu nebo datasetu se stejným výpočetním rozpočtem jako hustý model. Konkrétně model MoE by měl dosáhnout stejné kvality jako jeho hustý protějšek mnohem rychleji během předtréninku.

Phi-3.5-MoE obsahuje 16×3,8 miliard expertích modulů. Phi-3.5-MoE s pouze 6,6 miliardami aktivních parametrů dosahuje podobné úrovně důvody, porozumění jazyku a matematiky jako mnohem větší modely.

Model rodiny Phi-3/3.5 můžeme použít podle různých scénářů. Na rozdíl od LLM můžete Phi-3/3.5-mini nebo Phi-3/3.5-Vision nasadit na edge zařízeních.


## Jak používat modely rodiny Phi-3/3.5

Doufáme, že využijeme Phi-3/3.5 v různých scénářích. Dále použijeme Phi-3/3.5 podle různých scénářů.

![phi3](../../../translated_images/cs/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inference přes Cloud API

**Microsoft Foundry Models**

> **Poznámka:** GitHub Models bude ukončeno na konci července 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) je přímou náhradou.

Microsoft Foundry Models je nejpřímější cestou. Můžete rychle přistoupit k modelu Phi-3/3.5-Instruct přes katalog Foundry modelů. Ve spojení se sadou Azure AI Inference SDK / OpenAI SDK máte přístup k API přes kód k dokončení volání Phi-3/3.5-Instruct. Různé efekty můžete také testovat prostřednictvím Playgroundu.

- Demo: Porovnání efektů Phi-3-mini a Phi-3.5-mini v čínských scénářích

![phi3](../../../translated_images/cs/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/cs/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Nebo pokud chceme použít vision a MoE modely, můžeme použít Microsoft Foundry k dokončení volání. Máte-li zájem, můžete si přečíst Phi-3 Cookbook, abyste se naučili, jak volat Phi-3/3.5 Instruct, Vision, MoE přes Microsoft Foundry [Klikněte na tento odkaz](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Kromě cloudového katalogu Microsoft Foundry Models můžete také využít [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) k dokončení souvisejících volání. Název NVIDIA NIM (NVIDIA Inference Microservices) představuje sadu akcelerovaných mikroservis pro inference, které pomáhají vývojářům efektivně nasazovat AI modely napříč různými prostředími, včetně cloudů, datových center a pracovních stanic.

Některé klíčové funkce NVIDIA NIM jsou:

- **Snadné nasazení:** NIM umožňuje nasazení AI modelů jediným příkazem, což usnadňuje integraci do stávajících pracovních postupů.
- **Optimalizovaný výkon:** Využívá předoptimalizované inference enginy NVIDIA, jako jsou TensorRT a TensorRT-LLM, aby zajistil nízkou latenci a vysoký průchod.
- **Škálovatelnost:** NIM podporuje autoskalování na Kubernetes, což umožňuje efektivní zpracování proměnlivých pracovních zátěží.
- **Bezpečnost a kontrola:** Organizace si mohou zachovat kontrolu nad svými daty a aplikacemi tím, že sami hostují NIM mikroservisy na vlastní spravované infrastruktuře.
- **Standardní API:** NIM poskytuje průmyslově standardní API, což usnadňuje vytváření a integraci AI aplikací jako jsou chatboti, AI asistenti a další.

NIM je součástí NVIDIA AI Enterprise, které má za cíl zjednodušit nasazení a provozování AI modelů, zajišťujíc jejich efektivní běh na NVIDIA GPU.

- Demo: Použití NVIDIA NIM k volání Phi-3.5-Vision-API  [[Klikněte na tento odkaz](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Spuštění Phi-3/3.5 lokálně
Inferování ve vztahu k Phi-3, nebo jakémukoliv jazykovému modelu jako GPT-3, se týká procesu generování odpovědí nebo předpovědí na základě vstupu, který obdrží. Když poskytnete modelu Phi-3 podnět nebo otázku, používá svůj vytrénovaný neuronový síť k inferenci nejpravděpodobnější a relevantní odpovědi analyzováním vzorců a vztahů v datech, na kterých byl trénován.

**Hugging Face Transformer**
Hugging Face Transformers je výkonná knihovna navržená pro zpracování přirozeného jazyka (NLP) a další úlohy strojového učení. Zde jsou některé klíčové body o ní:

1. **Předtrénované modely**: Poskytuje tisíce předtrénovaných modelů, které lze použít pro různé úkoly, jako klasifikace textu, rozpoznávání pojmenovaných entit, odpovídání na otázky, shrnutí, překlad a generování textu.

2. **Interoperabilita rámců**: Knihovna podporuje několik frameworků hlubokého učení, včetně PyTorch, TensorFlow a JAX. To umožňuje trénovat model v jednom frameworku a používat ho v jiném.

3. **Multimodální schopnosti**: Kromě NLP podporuje Hugging Face Transformers také úlohy v počítačovém vidění (např. klasifikace obrázků, detekce objektů) a zpracování zvuku (např. rozpoznávání řeči, klasifikace zvuků).

4. **Snadné použití**: Knihovna nabízí API a nástroje k snadnému stahování a doladění modelů, což ji činí přístupnou jak začátečníkům, tak odborníkům.

5. **Komunita a zdroje**: Hugging Face má živou komunitu a rozsáhlou dokumentaci, návody a průvodce, které pomáhají uživatelům začít a co nejlépe využít knihovnu.
[oficiální dokumentace](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) nebo jejich [GitHub repozitář](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Toto je nejběžněji používaný způsob, ale také vyžaduje GPU akceleraci. Vždyť scénáře jako Vision a MoE vyžadují hodně výpočtů, které budou na CPU bez kvantizace velmi pomalé.


- Demo: Použití Transformer k volání Phi-3.5-Instruct [Klikněte na tento odkaz](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Použití Transformer k volání Phi-3.5-Vision [Klikněte na tento odkaz](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Použití Transformer k volání Phi-3.5-MoE [Klikněte na tento odkaz](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) je platforma navržená tak, aby usnadnila provoz velkých jazykových modelů (LLM) lokálně na vašem počítači. Podporuje různé modely, jako Llama 3.1, Phi 3, Mistral a Gemma 2, mezi jinými. Platforma zjednodušuje proces tím, že balí váhy modelu, konfiguraci a data do jednoho balíčku, což uživatelům umožňuje snadněji přizpůsobit a vytvářet vlastní modely. Ollama je dostupná pro macOS, Linux a Windows. Je to skvělý nástroj, pokud chcete experimentovat s LLM nebo je nasadit bez spoléhání se na cloudové služby. Ollama je nejpřímější cesta, stačí pouze spustit následující příkaz.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) je offline runtime Microsoftu, který běží přímo na zařízení a umožňuje spouštět modely jako Phi zcela na vašem vlastním hardwaru - není potřeba žádné předplatné Azure, API klíč ani síťové připojení. Automaticky vybere nejlepší dostupného poskytovatele provádění (NPU, GPU nebo CPU) a vystavuje OpenAI-kompatibilní endpoint, takže stávající `openai`/Azure AI Inference SDK kód může na něj směřovat s minimálními změnami. Podívejte se na [Foundry Local dokumentaci](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) pro začátek.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Nebo použijte SDK přímo v Pythonu:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime pro GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) je multiplatformní akcelerátor pro inferenci a trénink strojového učení. ONNX Runtime pro Generative AI (GENAI) je výkonný nástroj, který vám pomáhá efektivně spouštět generativní AI modely na různých platformách.

## Co je ONNX Runtime?
ONNX Runtime je open-source projekt, který umožňuje vysoce výkonnou inferenci strojových modelů. Podporuje modely ve formátu Open Neural Network Exchange (ONNX), což je standard pro reprezentaci modelů strojového učení. ONNX Runtime inference může umožnit rychlejší zákaznické zkušenosti a snížit náklady, a podporuje modely z frameworků hlubokého učení, jako jsou PyTorch a TensorFlow/Keras, stejně jako klasické knihovny strojového učení jako scikit-learn, LightGBM, XGBoost a další. ONNX Runtime je kompatibilní s různým hardwarem, ovladači a operačními systémy a poskytuje optimální výkon využitím hardwarových akcelerátorů tam, kde je to možné, spolu s optimalizacemi a transformacemi grafů.

## Co je Generativní AI?
Generativní AI se týká AI systémů, které dokáží generovat nový obsah, jako jsou text, obrázky nebo hudba, na základě dat, na kterých byly trénovány. Příklady zahrnují jazykové modely jako GPT-3 a modely pro generování obrázků jako Stable Diffusion. Knihovna ONNX Runtime pro GenAI poskytuje generativní AI smyčku pro ONNX modely, včetně inference s ONNX Runtime, zpracování logits, vyhledávání a vzorkování a správu KV cache.

## ONNX Runtime pro GENAI
ONNX Runtime pro GENAI rozšiřuje možnosti ONNX Runtime tak, aby podporoval generativní AI modely. Zde jsou některé klíčové funkce:

- **Široká podpora platforem:** Funguje na různých platformách, včetně Windows, Linux, macOS, Android a iOS.
- **Podpora modelů:** Podporuje mnoho oblíbených generativních AI modelů, jako jsou LLaMA, GPT-Neo, BLOOM a další.
- **Optimalizace výkonu:** Obsahuje optimalizace pro různé hardwarové akcelerátory jako NVIDIA GPU, AMD GPU a další2.
- **Snadné použití:** Poskytuje API pro snadnou integraci do aplikací, umožňující generovat text, obrázky a další obsah s minimem kódu.
- Uživatelé mohou volat vysoceúrovňovou metodu generate(), nebo spouštět každou iteraci modelu v cyklu, generující jeden token po druhém a volitelně upravovat parametry generování uvnitř smyčky.
- ONNX runtime také podporuje greedy/beam search a TopP, TopK vzorkování pro generování sekvencí tokenů a vestavěné zpracování logits jako penalizace opakování. Můžete také snadno přidat vlastní skórování.

## Začínáme
Pro začátek s ONNX Runtime pro GENAI můžete postupovat takto:

### Instalace ONNX Runtime:
```Python
pip install onnxruntime
```
### Instalace generativních AI rozšíření:
```Python
pip install onnxruntime-genai
```

### Spuštění modelu: Zde je jednoduchý příklad v Pythonu:
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
### Demo:Použití ONNX Runtime GenAI k volání Phi-3.5-Vision


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


**Ostatní**

Kromě ONNX Runtime, Ollama a Foundry Local referenčních metod můžeme také doplnit referenci kvantitativních modelů založených na referenčních metodách modelů poskytovaných různými výrobci. Jako například Apple MLX framework s Apple Metal, Qualcomm QNN s NPU, Intel OpenVINO s CPU/GPU atd. Další obsah naleznete také v [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Více

Naučili jsme se základy rodiny Phi-3/3.5, ale pro hlubší znalosti o SLM potřebujeme více informací. Odpovědi naleznete v Phi-3 Cookbook. Pokud chcete vědět více, navštivte prosím [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->