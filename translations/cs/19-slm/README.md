# Úvod do malých jazykových modelů pro generativní umělou inteligenci pro začátečníky
Generativní umělá inteligence je fascinující oblast umělé inteligence, která se zaměřuje na vytváření systémů schopných generovat nový obsah. Tento obsah může sahat od textu a obrázků po hudbu a dokonce celé virtuální prostředí. Jednou z nejzajímavějších aplikací generativní AI je oblast jazykových modelů.

## Co jsou malé jazykové modely?

Malý jazykový model (SLM) představuje zmenšenou variantu velkého jazykového modelu (LLM), využívající mnoho architektonických principů a technik LLM, přičemž má výrazně sníženou výpočetní náročnost.

SLM jsou podmnožinou jazykových modelů navržených k generování textu podobného lidskému. Na rozdíl od svých větších protějšků, jako je GPT-4, jsou SLM kompaktnější a efektivnější, což je činí ideálními pro aplikace, kde jsou výpočetní zdroje omezené. Přestože jsou menší, stále mohou vykonávat různé úkoly. Typicky jsou SLM vytvářeny kompresí nebo destilací LLM s cílem zachovat podstatnou část funkčnosti a jazykových schopností původního modelu. Toto zmenšení velikosti modelu snižuje celkovou složitost, díky čemuž jsou SLM efektivnější jak z hlediska využití paměti, tak výpočetních požadavků. Navzdory těmto optimalizacím mohou SLM stále provádět širokou škálu úkolů zpracování přirozeného jazyka (NLP):

- Generování textu: Vytváření koherentních a kontextově relevantních vět nebo odstavců.
- Dokončování textu: Předpovídání a doplňování vět na základě daného podnětu.
- Překlad: Převod textu z jednoho jazyka do druhého.
- Shrnutí: Zkracování rozsáhlých textů do kratších, snadno stravitelných souhrnů.

Ačkoli s určitými kompromisy ve výkonu nebo hloubce porozumění ve srovnání s jejich většími protějšky.

## Jak malé jazykové modely fungují?
SLM jsou trénovány na obrovském množství textových dat. Během tréninku se učí vzory a struktury jazyka, což jim umožňuje generovat text, který je gramaticky správný a kontextově vhodný. Výcvikový proces zahrnuje:

- Sběr dat: Shromažďování rozsáhlých datasetů textu z různých zdrojů.
- Předzpracování: Čištění a organizaci dat tak, aby byla vhodná pro trénink.
- Trénink: Použití algoritmů strojového učení k naučení modelu, jak rozumět textu a generovat ho.
- Doladění: Úpravu modelu ke zlepšení jeho výkonu na specifických úlohách.

Vývoj SLM odpovídá rostoucí potřebě modelů, které lze nasadit v prostředích s omezenými zdroji, například na mobilních zařízeních nebo edge computing platformách, kde by plnohodnotné LLM mohly být nepraktické kvůli vysokým nárokům na zdroje. Zaměřením na efektivitu SLM vyvažují výkon a dostupnost, což umožňuje širší aplikaci v různých oblastech.

![slm](../../../translated_images/cs/slm.4058842744d0444a.webp)

## Výukové cíle

V této lekci doufáme, že představíme znalosti o SLM a spojíme je s Microsoft Phi-3, abychom se naučili různé scénáře v textovém obsahu, vizuálních datech a MoE.

Na konci této lekce byste měli být schopni odpovědět na následující otázky:

- Co je SLM?
- Jaký je rozdíl mezi SLM a LLM?
- Co je rodina Microsoft Phi-3/3.5?
- Jak spustit inferenci s rodinou Microsoft Phi-3/3.5?

Připraveni? Pojďme začít.

## Rozdíly mezi velkými jazykovými modely (LLM) a malými jazykovými modely (SLM)

Oba, LLM i SLM, jsou postaveny na základních principech pravděpodobnostního strojového učení, následující podobné přístupy ve své architektuře, metodách tréninku, procesech generování dat a technikách vyhodnocování modelů. Nicméně několik klíčových faktorů tyto dva typy modelů odlišuje.

## Aplikace malých jazykových modelů

SLM mají širokou škálu aplikací, včetně:

- Chatboti: Poskytování zákaznické podpory a komunikace s uživateli konverzačním způsobem.
- Tvorba obsahu: Pomoc spisovatelům generovat nápady nebo dokonce vypracovat celé články.
- Vzdělávání: Pomoc studentům s psaním úkolů nebo učením nových jazyků.
- Přístupnost: Vytváření nástrojů pro osoby s postižením, například systémy převodu textu na řeč.

**Velikost**
  
Hlavní odlišnost mezi LLM a SLM spočívá ve velikosti modelů. LLM, jako například ChatGPT (GPT-4), mohou obsahovat odhadovaných 1,76 bilionu parametrů, zatímco open-source SLM jako Mistral 7B jsou navrženy s výrazně menším počtem parametrů — přibližně 7 miliard. Tento rozdíl je primárně způsoben rozdíly v architektuře modelu a tréninkových postupech. Například ChatGPT používá mechanismus sebe-pozornosti v rámci encodér-dekodér frameworku, zatímco Mistral 7B využívá sliding window attention, což umožňuje efektivnější trénink v modelu pouze s dekodérem. Tento architektonický rozdíl má zásadní dopady na složitost a výkon těchto modelů.

**Porozumění**

SLM jsou typicky optimalizovány pro výkon v konkrétních doménách, což je činí vysoce specializovanými, ale potenciálně omezenými ve schopnosti poskytovat široké kontextuální porozumění napříč více oblastmi znalostí. Naopak LLM usilují o simulaci lidské inteligence na širší úrovni. Trénované na rozsáhlých, různorodých datech jsou LLM navrženy tak, aby dosahovaly dobrých výsledků v různých doménách, nabízejí větší všestrannost a přizpůsobivost. Proto jsou LLM vhodnější pro širší spektrum úkolů, jako je zpracování přirozeného jazyka a programování.

**Výpočetní nároky**

Trénink a nasazení LLM jsou procesy náročné na zdroje, často vyžadující rozsáhlou výpočetní infrastrukturu, včetně velkých GPU clusterů. Například trénink modelu jako ChatGPT od začátku může vyžadovat tisíce GPU po dlouhou dobu. Naopak SLM s menším počtem parametrů jsou dostupnější z hlediska výpočetních zdrojů. Modely jako Mistral 7B lze trénovat a spouštět na lokálních strojích vybavených středně výkonnými GPU, i když trénink stále vyžaduje několik hodin pomocí více GPU.

**Bias (předpojatost)**

Bias je známý problém u LLM, primárně kvůli povaze tréninkových dat. Tyto modely často spoléhají na surová, otevřeně dostupná data z internetu, která mohou nedostatečně zastupovat nebo nesprávně zobrazovat určité skupiny, zavádět chybné označení nebo odrážet jazykové předsudky ovlivněné dialekty, geografickými rozdíly a gramatickými pravidly. Navíc složitost architektury LLM může nechtěně zesílit bias, který může zůstat bez povšimnutí bez pečlivého doladění. Naopak SLM, trénované na úzce vymezených, doménově specifických datasetech, jsou přirozeně méně náchylné k takovým předsudkům, i když nejsou zcela imunní.

**Inference (inferenční rychlost)**

Menší velikost SLM jim poskytuje významnou výhodu ve rychlosti inference, což jim umožňuje efektivně generovat výstupy na lokálním hardwaru bez nutnosti rozsáhlého paralelního zpracování. Naopak LLM kvůli své velikosti a složitosti často vyžadují významné paralelní výpočetní zdroje k dosažení přijatelné doby odezvy. Přítomnost více současných uživatelů dále zpomaluje odezvu LLM, zvláště při nasazení ve velkém měřítku.

Shrnutím lze říci, že ačkoliv LLM i SLM sdílejí základní principy strojového učení, liší se výrazně co do velikosti modelu, požadavků na zdroje, kontextového porozumění, náchylnosti k bias a rychlosti inference. Tyto rozdíly odrážejí jejich vhodnost pro různé využití, přičemž LLM jsou univerzálnější, ale náročnější na zdroje, zatímco SLM nabízejí efektivitu zaměřenou na konkrétní domény při snížených výpočetních nárocích.

***Poznámka: V této lekci představíme SLM na příkladu Microsoft Phi-3 / 3.5.***

## Představení rodiny Phi-3 / Phi-3.5

Rodina Phi-3 / 3.5 cílí hlavně na scénáře aplikací v oblasti textu, vidění a agentů (MoE):

### Phi-3 / 3.5 Instruct

Hlavně pro generování textu, dokončování chatu a extrakci informací z obsahu apod.

**Phi-3-mini**

Jazykový model s 3,8 miliardami parametrů je dostupný na Microsoft Foundry, Hugging Face a Ollama. Modely Phi-3 výrazně překonávají jazykové modely stejné nebo větší velikosti na klíčových benchmarkech (viz níže uvedená čísla benchmarků, vyšší čísla jsou lepší). Phi-3-mini překonává modely dvojnásobné velikosti, zatímco Phi-3-small a Phi-3-medium překonávají větší modely včetně GPT-3.5.

**Phi-3-small & medium**

S pouhými 7 miliardami parametrů Phi-3-small poráží GPT-3.5T v různých jazykových, logických, kódovacích a matematických testech.

Phi-3-medium s 14 miliardami parametrů pokračuje v tomto trendu a překonává Gemini 1.0 Pro.

**Phi-3.5-mini**

Můžeme ho považovat za vylepšení Phi-3-mini. Parametry zůstávají stejné, ale zlepšuje schopnost podporovat více jazyků (podpora 20+ jazyků: arabština, čínština, čeština, dánština, nizozemština, angličtina, finština, francouzština, němčina, hebrejština, maďarština, italština, japonština, korejština, norština, polština, portugalština, ruština, španělština, švédština, thajština, turečtina, ukrajinština) ​​a přidává silnější podporu pro dlouhý kontext.

Phi-3.5-mini s 3,8 miliardami parametrů překonává jazykové modely stejné velikosti a je na úrovni modelů dvojnásobné velikosti.

### Phi-3 / 3.5 Vision

Můžeme si Instruct model Phi-3/3.5 představit jako schopnost Phi rozumět, a Vision mu dává oči, aby chápal svět.


**Phi-3-Vision**

Phi-3-vision s pouhými 4,2 miliardami parametrů pokračuje v tomto trendu a překonává větší modely jako Claude-3 Haiku a Gemini 1.0 Pro V v obecných úlohách vizuálního uvažování, OCR a porozumění tabulkám a diagramům.


**Phi-3.5-Vision**

Phi-3.5-Vision je také vylepšením Phi-3-Vision, přidává podporu pro více obrázků. Můžete ho vnímat jako pokrok ve vidění, nejen že vidí obrázky, ale také videa.

Phi-3.5-vision překonává větší modely jako Claude-3.5 Sonnet a Gemini 1.5 Flash v úlohách OCR, porozumění tabulkám a grafům a je na stejné úrovni v obecných úlohách vizuálního znalostního uvažování. Podporuje vstupy z více snímků, tj. provádí uvažování na základě více vstupních obrázků


### Phi-3.5-MoE

***Mix expertů (Mixture of Experts - MoE)*** umožňuje modelům být předtrénované s mnohem menší výpočetní náročností, což znamená, že lze dramaticky zvětšit velikost modelu nebo datasetu se stejným výpočetním rozpočtem jako hustý model. Obzvláště MoE model by měl během předtréninku dosáhnout stejné kvality jako jeho hustý protějšek mnohem rychleji.

Phi-3.5-MoE se skládá ze 16x3,8 miliardy expertních modulů. Phi-3.5-MoE s pouze 6,6 miliardami aktivních parametrů dosahuje podobné úrovně logického uvažování, porozumění jazyku a matematiky jako mnohem větší modely.

Model rodiny Phi-3/3.5 můžeme použít podle různých scénářů. Na rozdíl od LLM lze Phi-3/3.5-mini nebo Phi-3/3.5-Vision nasadit na okrajová zařízení (edge devices).


## Jak používat modely rodiny Phi-3/3.5

Doufáme, že využijeme Phi-3/3.5 v různých scénářích. Dále budeme využívat Phi-3/3.5 podle různých scénářů.

![phi3](../../../translated_images/cs/phi3.655208c3186ae381.webp)

### Inference přes cloudové API

**Microsoft Foundry Models**

> **Poznámka:** GitHub Models bude ukončen na konci července 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) je jejich přímou náhradou.

Microsoft Foundry Models je nejpřímější způsob. Můžete rychle získat přístup k modelu Phi-3/3.5-Instruct přes katalog modelů Foundry. Ve spojení s Azure AI Inference SDK / OpenAI SDK můžete přistupovat k API přes kód ke zpracování volání Phi-3/3.5-Instruct. Také můžete testovat různé efekty pomocí Playgroundu.

- Demo: Porovnání účinků Phi-3-mini a Phi-3.5-mini v čínských scénářích

![phi3](../../../translated_images/cs/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/cs/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Nebo pokud chcete používat vizuální a MoE modely, můžete použít Microsoft Foundry k dokončení volání. Pokud máte zájem, můžete si přečíst Phi-3 Cookbook a naučit se, jak volat Phi-3/3.5 Instruct, Vision, MoE přes Microsoft Foundry [Klikněte na tento odkaz](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Kromě cloudového katalogu Microsoft Foundry Models můžete také využít [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) pro dokončení souvisejících volání. Navštivte NVIDIA NIM, kde můžete dokončit API volání rodiny Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) je sada zrychlených mikroservis pro inferenci, navržena pro efektivní nasazení AI modelů v různých prostředích, včetně cloudů, datových center a pracovních stanic.

Zde jsou některé klíčové vlastnosti NVIDIA NIM:

- **Snadnost nasazení:** NIM umožňuje nasazení AI modelů jediným příkazem, což usnadňuje integraci do stávajících pracovních postupů.

- **Optimalizovaný výkon:** Využívá předoptimalizované inference enginy NVIDIA, jako jsou TensorRT a TensorRT-LLM, aby zajistil nízkou latenci a vysoký průtok.
- **Škálovatelnost:** NIM podporuje autoscaling na Kubernetes, což mu umožňuje efektivně zvládat různé pracovní zátěže.
- **Zabezpečení a kontrola:** Organizace mohou mít kontrolu nad svými daty a aplikacemi tím, že si sami hostují mikroservisy NIM na vlastní spravované infrastruktuře.
- **Standardní API:** NIM poskytuje průmyslově standardní API, díky čemuž je snadné vytvářet a integrovat AI aplikace jako chatboti, AI asistenti a další.

NIM je součástí NVIDIA AI Enterprise, jehož cílem je zjednodušit nasazení a operacionalizaci AI modelů a zajistit jejich efektivní běh na GPU NVIDIA.

- Demo: Použití NVIDIA NIM k volání Phi-3.5-Vision-API  [[Klikněte na tento odkaz](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Spuštění Phi-3/3.5 lokálně
Inference ve vztahu k Phi-3, nebo jakémukoliv jazykovému modelu jako GPT-3, znamená proces generování odpovědí nebo předpovědí na základě přijatého vstupu. Když zadáte prompt nebo otázku Phi-3, využívá svůj natrénovaný neuronový síť k odvození nejpravděpodobnější a nejrelevantnější odpovědi analýzou vzorů a vztahů v datech, na kterých byl trénován.

**Hugging Face Transformer**
Hugging Face Transformers je výkonná knihovna určená pro zpracování přirozeného jazyka (NLP) a další úlohy strojového učení. Zde je několik klíčových bodů:

1. **Předtrénované modely**: Poskytuje tisíce předtrénovaných modelů, které lze použít pro různé úlohy, jako je klasifikace textu, rozpoznávání entit, odpovídání na otázky, shrnování, překlad a generování textu.

2. **Interoperabilita rámců:** Knihovna podporuje více frameworků hlubokého učení, včetně PyTorch, TensorFlow a JAX. To umožňuje trénovat model v jednom frameworku a použít ho v jiném.

3. **Multimodální schopnosti:** Kromě NLP podporuje Hugging Face Transformers také úlohy v počítačovém vidění (např. klasifikaci obrázků, detekci objektů) a zpracování audia (např. rozpoznávání řeči, klasifikaci zvuků).

4. **Snadné použití:** Knihovna nabízí API a nástroje pro snadné stahování a doladění modelů, což ji činí přístupnou jak pro začátečníky, tak pro odborníky.

5. **Komunita a zdroje:** Hugging Face má živou komunitu a rozsáhlou dokumentaci, tutoriály a návody, které pomáhají uživatelům začít a co nejlépe využít knihovnu.
[oficiální dokumentace](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) nebo jejich [GitHub repozitář](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Toto je nejčastěji používaná metoda, ale také vyžaduje GPU akceleraci. Nakonec, scénáře jako Vision a MoE vyžadují spoustu výpočtů, které budou na CPU velmi pomalé, pokud nejsou kvantizované.


- Demo: Použití Transformer k volání Phi-3.5-Instruct [Klikněte na tento odkaz](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Použití Transformer k volání Phi-3.5-Vision [Klikněte na tento odkaz](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Použití Transformer k volání Phi-3.5-MoE [Klikněte na tento odkaz](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) je platforma navržená tak, aby usnadnila spuštění velkých jazykových modelů (LLM) lokálně na vašem počítači. Podporuje různé modely jako Llama 3.1, Phi 3, Mistral a Gemma 2, mezi dalšími. Platforma zjednodušuje proces tím, že kombinuje váhy modelu, konfiguraci a data do jednoho balíčku, což usnadňuje uživatelům přizpůsobení a tvorbu vlastních modelů. Ollama je dostupná pro macOS, Linux a Windows. Je to skvělý nástroj, pokud chcete experimentovat s LLM nebo je nasadit bez závislosti na cloudových službách. Ollama je nejpřímější cesta, stačí spustit následující příkaz.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) je Microsoftův offline runtime běžící na zařízení, který umožňuje spouštět modely jako Phi zcela na vlastním hardwaru - není potřeba Azure předplatné, API klíč ani síťové připojení. Automaticky vybere nejlepší dostupný poskytovatel běhu (NPU, GPU nebo CPU) a vystaví OpenAI-kompatibilní endpoint, takže existující kód s `openai`/Azure AI Inference SDK lze nasměrovat na něj s minimálními úpravami. Viz [Foundry Local dokumentace](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst), jak začít.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) je multiplatformní akcelerátor inference a tréninku strojového učení. ONNX Runtime pro Generative AI (GENAI) je výkonný nástroj, který vám pomůže efektivně provozovat generativní AI modely napříč různými platformami.

## Co je ONNX Runtime?
ONNX Runtime je open-source projekt, který umožňuje vysokovýkonnou inferenci modelů strojového učení. Podporuje modely ve formátu Open Neural Network Exchange (ONNX), což je standard pro reprezentaci modelů strojového učení. Inferenci ONNX Runtime může umožnit rychlejší zákaznické zkušenosti a snížit náklady, podporuje modely z frameworků hlubokého učení jako PyTorch a TensorFlow/Keras stejně jako klasické knihovny strojového učení jako scikit-learn, LightGBM, XGBoost a další. ONNX Runtime je kompatibilní s různým hardwarem, ovladači a operačními systémy, a poskytuje optimální výkon díky využití hardwarových akcelerátorů tam, kde je to možné, spolu s optimalizacemi a transformacemi grafu.

## Co je Generativní AI?
Generativní AI označuje AI systémy, které dokážou generovat nový obsah, například text, obrázky nebo hudbu, na základě dat, na kterých byly trénovány. Příklady zahrnují jazykové modely jako GPT-3 a modely pro generování obrázků jako Stable Diffusion. Knihovna ONNX Runtime pro GenAI poskytuje generativní AI smyčku pro ONNX modely, včetně inference s ONNX Runtime, zpracování logits, vyhledávání a vzorkování a správu KV cache.

## ONNX Runtime pro GENAI
ONNX Runtime pro GENAI rozšiřuje schopnosti ONNX Runtime tak, aby podporoval generativní AI modely. Zde jsou některé klíčové funkce:

- **Široká podpora platforem:** Funguje na různých platformách včetně Windows, Linux, macOS, Android a iOS.
- **Podpora modelů:** Podporuje mnoho populárních generativních AI modelů, jako jsou LLaMA, GPT-Neo, BLOOM a další.
- **Optimalizace výkonu:** Obsahuje optimalizace pro různé hardwarové akcelerátory jako GPU NVIDIA, GPU AMD a další2.
- **Jednoduchost použití:** Poskytuje API pro snadnou integraci do aplikací, umožňující generovat text, obrázky a další obsah s minimem kódu.
- Uživatelé mohou volat vysokou úroveň metody generate(), nebo spouštět každou iteraci modelu v cyklu, generovat jeden token po tokenu a volitelně uvnitř cyklu aktualizovat parametry generování.
- ONNX runtime také podporuje greedy/beam search a TopP, TopK vzorkování pro generování sekvencí tokenů a vestavěné zpracování logits jako penalizace opakování. Můžete také snadno přidat vlastní skórování.

## Začínáme
Pro začátek s ONNX Runtime pro GENAI můžete postupovat následovně:

### Instalace ONNX Runtime:
```Python
pip install onnxruntime
```
### Instalace Generativních AI rozšíření:
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
### Demo: Použití ONNX Runtime GenAI k volání Phi-3.5-Vision


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

Kromě referenčních metod ONNX Runtime, Ollama a Foundry Local můžeme také doplnit referenci kvantitativních modelů založených na referenčních metodách modelů poskytovaných různými výrobci. Například Apple MLX framework s Apple Metal, Qualcomm QNN s NPU, Intel OpenVINO s CPU/GPU atd. Další obsah naleznete také v [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Více

Naučili jsme se základy rodiny Phi-3/3.5, ale pro hlubší znalosti o SLM potřebujeme další informace. Odpovědi najdete v Phi-3 Cookbook. Pokud se chcete dozvědět více, navštivte prosím [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->