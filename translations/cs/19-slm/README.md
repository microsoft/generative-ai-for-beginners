# Úvod do malých jazykových modelů pro generativní AI pro začátečníky
Generativní AI je fascinující oblast umělé inteligence, která se zaměřuje na vytváření systémů schopných generovat nový obsah. Tento obsah může zahrnovat texty, obrázky, hudbu nebo dokonce celé virtuální prostředí. Jednou z nejnadšenějších aplikací generativní AI je oblast jazykových modelů.

## Co jsou malé jazykové modely?

Malý jazykový model (SLM) představuje zmenšenou variantu velkého jazykového modelu (LLM), která využívá mnohé architektonické principy a techniky LLM, přičemž vykazuje výrazně snížené výpočetní nároky.

SLM jsou podmnožinou jazykových modelů navržených pro generování textu podobného lidskému projevu. Na rozdíl od svých větších protějšků, jako je GPT-4, jsou SLM kompaktnější a efektivnější, což je činí ideálními pro aplikace, kde jsou omezené výpočetní zdroje. Přesto, že jsou menší, zvládají stále různé úkoly. Typicky jsou SLM konstrukčně vytvářeny kompresí nebo destilací LLM, s cílem uchovat významnou část původní funkčnosti a jazykových schopností modelu. Toto zmenšení velikosti modelu snižuje celkovou složitost a činí SLM efektivnějšími jak z hlediska paměťové náročnosti, tak výpočetních požadavků. Navzdory těmto optimalizacím mohou SLM stále vykonávat širokou škálu úkolů zpracování přirozeného jazyka (NLP):

- Generování textu: Vytváření souvislých a kontextuálně relevantních vět nebo odstavců.
- Dokončování textu: Predikce a doplňování vět na základě daného promptu.
- Překlad: Převod textu z jednoho jazyka do druhého.
- Shrnutí: Zkracování dlouhých textů do kratších, lépe stravitelných souhrnů.

Ačkoli s některými kompromisy v oblasti výkonu nebo hloubky porozumění ve srovnání s většími protějšky.

## Jak malé jazykové modely fungují?
SLM jsou trénovány na obrovských množstvích textových dat. Během tréninku se učí vzory a struktury jazyka, což jim umožňuje generovat text, který je nejen gramaticky správný, ale i kontextuálně vhodný. Proces tréninku zahrnuje:

- Sběr dat: Shromažďování velkých datových sad textů z různých zdrojů.
- Předzpracování: Čištění a organizaci dat tak, aby byla vhodná pro trénink.
- Trénink: Použití algoritmů strojového učení k naučení modelu jak rozumět a generovat text.
- Doladění: Úpravu modelu za účelem zlepšení jeho výkonu na specifických úlohách.

Vývoj SLM odpovídá rostoucí potřebě modelů, které lze nasadit v prostředích s omezenými zdroji, jako jsou mobilní zařízení nebo okrajové výpočetní platformy, kde by plnohodnotné LLM mohly být nepraktické kvůli vysokým nárokům na zdroje. Zaměřením se na efektivitu SLM vyvažují výkon a dostupnost, což umožňuje širší využití v různých oblastech.

![slm](../../../translated_images/cs/slm.4058842744d0444a.webp)

## Cíle výuky

V této lekci máme v plánu představit znalosti o SLM a spojit je s Microsoft Phi-3, abychom se naučili různé scénáře v textovém obsahu, ve vidění a MoE.

Na konci této lekce byste měli být schopni odpovědět na následující otázky:

- Co je SLM?
- Jaký je rozdíl mezi SLM a LLM?
- Co je rodina Microsoft Phi-3/3.5?
- Jak spustit inferenci s rodinou Microsoft Phi-3/3.5?

Připraveni? Pojďme začít.

## Rozdíly mezi velkými jazykovými modely (LLM) a malými jazykovými modely (SLM)

LLM i SLM jsou založeny na základních principech pravděpodobnostního strojového učení, používají obdobný přístup v architektonickém návrhu, metodikách tréninku, procesech generování dat a technikách hodnocení modelů. Nicméně několik klíčových faktorů odlišuje tyto dva typy modelů.

## Aplikace malých jazykových modelů

SLM mají široké spektrum aplikací, včetně:

- Chatboti: Poskytování zákaznické podpory a komunikace s uživateli formou konverzace.
- Tvorba obsahu: Pomoc spisovatelům generováním nápadů nebo dokonce psaním celých článků.
- Vzdělávání: Pomoc studentům při psaní úkolů nebo učení se novým jazykům.
- Přístupnost: Vytváření nástrojů pro osoby s postižením, jako jsou systémy převodu textu na řeč.

**Velikost**
  
Hlavním rozdílem mezi LLM a SLM je měřítko modelu. LLM, jako je ChatGPT (GPT-4), mohou mít odhadovaně 1,76 bilionu parametrů, zatímco open-source SLM jako Mistral 7B jsou navrženy s výrazně menším počtem parametrů—přibližně 7 miliard. Tento rozdíl vyplývá především z odlišností v architektuře modelu a tréninkových postupech. Například ChatGPT používá mechanismus samopozornosti v rámci architektury encoder-decoder, zatímco Mistral 7B využívá sliding window attention, což umožňuje efektivnější trénink v rámci decoder-only modelu. Tento architektonický rozdíl má zásadní dopad na složitost a výkon těchto modelů.

**Porozumění**

SLM jsou obvykle optimalizovány pro výkon v konkrétních doménách, což je činí vysoce specializovanými, ale potenciálně omezenými v poskytování širokého kontextuálního porozumění napříč různými obory. Naproti tomu LLM usilují o simulaci inteligence podobné lidské na komplexnější úrovni. Jsou trénovány na obrovských a rozmanitých datových sadách, aby dobře fungovaly v různých oblastech, což jim poskytuje větší všestrannost a adaptabilitu. Z tohoto důvodu jsou LLM vhodnější pro širší škálu následných úloh, jako je zpracování přirozeného jazyka a programování.

**Výpočetní požadavky**

Trénink a nasazení LLM jsou procesy náročné na zdroje, často vyžadující rozsáhlou výpočetní infrastrukturu, včetně velkých GPU clusterů. Například trénink modelu jako ChatGPT od začátku může vyžadovat tisíce GPU po dlouhou dobu. Naproti tomu SLM, díky menšímu počtu parametrů, jsou dostupnější z hlediska výpočetních zdrojů. Modely jako Mistral 7B lze trénovat a spustit na lokálních strojích s mírnými GPU schopnostmi, i když trénink stále vyžaduje několik hodin na více GPU.

**Bias (zaujatost)**

Zaujatost je známým problémem u LLM, převážně kvůli povaze tréninkových dat. Tyto modely často spoléhají na surová, veřejně dostupná data z internetu, která mohou nedostatečně reprezentovat nebo chybně reprezentovat určité skupiny, zavádět nesprávné označení či odrážet jazykové předsudky ovlivněné dialektem, geografickými variacemi a gramatickými pravidly. Navíc složitost architektury LLM může nechtěně zesilovat zaujatost, která může zůstat bez povšimnutí bez pečlivého doladění. Naopak SLM, trénované na omezenějších, doménově specifických sadách dat, jsou zásadně méně náchylné k takovým zaujatostem, i když zcela se jim nevyhnou.

**Inference (vyvozování)**

Menší velikost SLM jim poskytuje významnou výhodu v rychlosti inferenčního procesu, což jim umožňuje efektivně generovat výstupy na lokálním hardwaru bez potřeby rozsáhlého paralelního zpracování. Naproti tomu LLM často vyžadují značné paralelní výpočetní zdroje, aby dosáhly přijatelné doby odezvy. Přítomnost více současných uživatelů dále zpomaluje odezvu LLM, zejména při jejich nasazení ve velkém měřítku.

Shrnutím, ačkoli LLM i SLM vycházejí z podobných základů strojového učení, liší se výrazně v oblasti velikosti modelu, požadavků na zdroje, kontextuálního porozumění, náchylnosti k zaujatostem a rychlosti inferencí. Tyto rozdíly odrážejí jejich vhodnost pro různé scénáře použití, přičemž LLM jsou všestrannější, ale náročnější na zdroje, zatímco SLM nabízejí efektivitu zaměřenou na konkrétní domény s nižšími výpočetními nároky.

***Poznámka: V této lekci představíme SLM na příkladu Microsoft Phi-3 / 3.5.***

## Představení rodiny Phi-3 / Phi-3.5

Rodina Phi-3 / 3.5 je především určena pro scénáře aplikací v textu, vidění a Agentovi (MoE):

### Phi-3 / 3.5 Instruct

Hlavně pro generování textu, dokončení chatu a extrakci obsahových informací atd.

**Phi-3-mini**

Jazykový model o velikosti 3,8 miliardy parametrů je dostupný na Microsoft Foundry, Hugging Face a Ollama. Modely Phi-3 významně překonávají jazykové modely stejné nebo větší velikosti v klíčových benchmarkech (viz čísla benchmarků níže, vyšší čísla znamenají lepší výsledek). Phi-3-mini překonává modely dvojnásobné velikosti, zatímco Phi-3-small a Phi-3-medium překonávají větší modely, včetně GPT-3.5.

**Phi-3-small & medium**

S pouhými 7 miliardami parametrů Phi-3-small překonává GPT-3.5T v různých benchmarkech jazykových schopností, odvozování, programování a matematiky.

Phi-3-medium s 14 miliardami parametrů pokračuje v tomto trendu a překonává Gemini 1.0 Pro.

**Phi-3.5-mini**

Můžeme jej považovat za vylepšení Phi-3-mini. Parametry zůstávají nezměněny, ale zlepšuje podporu vícejazyčnosti (podpora více než 20 jazyků: arabština, čínština, čeština, dánština, nizozemština, angličtina, finština, francouzština, němčina, hebrejština, maďarština, italština, japonština, korejština, norština, polština, portugalština, ruština, španělština, švédština, thajština, turečtina, ukrajinština) a přidává silnější podporu pro dlouhý kontext.

Phi-3.5-mini s 3,8 miliardy parametrů překonává jazykové modely stejné velikosti a je na úrovni modelů dvojnásobné velikosti.

### Phi-3 / 3.5 Vision

Můžeme si Instruct model Phi-3/3.5 představit jako schopnost Phi porozumět, a Vision je to, co Phi dává oči k porozumění světu.


**Phi-3-Vision**

Phi-3-vision s pouhými 4,2 miliardami parametrů pokračuje tímto trendem a překonává větší modely jako Claude-3 Haiku a Gemini 1.0 Pro V v obecných úlohách vizuálního odvozování, OCR a pochopení tabulek a diagramů.


**Phi-3.5-Vision**

Phi-3.5-Vision je rovněž upgrade Phi-3-Vision, přidávající podporu pro vícenásobné obrázky. Můžete jej vnímat jako vylepšení vidění – nejenže vidíte obrázky, ale také videa.

Phi-3.5-vision překonává větší modely jako Claude-3.5 Sonnet a Gemini 1.5 Flash v OCR, pochopení tabulek a grafů a je vyrovnaný v úlohách obecného vizuálního poznání a odvozování. Podporuje víceramový vstup, tj. odvozování z více vstupních obrázků.


### Phi-3.5-MoE

***Mozaika expertů (Mixture of Experts, MoE)*** umožňuje modelům předtrénovat se s výrazně menším výpočetním zatížením, což znamená, že můžete dramaticky zvětšit velikost modelu nebo datové sady při stejném rozpočtu výpočetních zdrojů jako hustý model. Konkrétně model MoE by měl dosáhnout stejné kvality jako jeho hustý protějšek mnohem rychleji během předtréninku.

Phi-3.5-MoE sestává ze 16x3,8B expertních modulů. Phi-3.5-MoE s pouhými 6,6 miliardami aktivních parametrů dosahuje podobné úrovně odvozování, porozumění jazyku a matematiky jako mnohem větší modely.

Model rodiny Phi-3/3.5 můžeme používat podle různých scénářů. Na rozdíl od LLM lze Phi-3/3.5-mini nebo Phi-3/3.5-Vision nasadit na edge zařízeních.


## Jak používat modely rodiny Phi-3/3.5

Chceme používat Phi-3/3.5 v různých scénářích. Dále ukážeme využití Phi-3/3.5 podle konkrétních scénářů.

![phi3](../../../translated_images/cs/phi3.655208c3186ae381.webp)

### Inference přes cloudová API

**Modely Microsoft Foundry**

> **Poznámka:** GitHub Models bude ukončen koncem července 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) je přímou náhradou.

Modely Microsoft Foundry jsou nejpřímější cestou. Můžete rychle získat přístup k modelu Phi-3/3.5-Instruct přes katalog modelů Foundry. V kombinaci s Azure AI Inference SDK / OpenAI SDK můžete přistupovat k API kódem a dokončit volání Phi-3/3.5-Instruct. Také můžete testovat různé efekty přes Playground.

- Demo: Porovnání efektů Phi-3-mini a Phi-3.5-mini v čínských scénářích

![phi3](../../../translated_images/cs/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/cs/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Nebo pokud chcete použít vidění a MoE modely, můžete použít Microsoft Foundry k dokončení volání. Pokud máte zájem, můžete si přečíst Phi-3 Cookbook, abyste se naučili, jak volat Phi-3/3.5 Instruct, Vision, MoE přes Microsoft Foundry [Klikněte na tento odkaz](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Kromě cloudového katalogu modelů Microsoft Foundry můžete také použít [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) k dokončení souvisejících volání. Můžete navštívit NVIDIA NIM a dokončit API volání rodiny Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) je sada akcelerovaných inferenčních mikroservis, navržených tak, aby pomohla vývojářům efektivně nasadit AI modely v různých prostředích, včetně cloudů, datových center a pracovních stanic.

Zde jsou některé klíčové vlastnosti NVIDIA NIM:

- **Snadnost nasazení:** NIM umožňuje nasazení AI modelů jediným příkazem, což zjednodušuje integraci do existujících pracovních postupů.

- **Optimalizovaný výkon:** Využívá předoptimalizované inferenční enginy NVIDIA, jako jsou TensorRT a TensorRT-LLM, aby zajistil nízkou latenci a vysoký průchod dat.
- **Škálovatelnost:** NIM podporuje autoskalování na Kubernetes, což mu umožňuje efektivně zvládat různé pracovní zatížení.
- **Bezpečnost a kontrola:** Organizace mohou udržovat kontrolu nad svými daty a aplikacemi tím, že si sami hostují NIM mikroservisy na vlastní spravované infrastruktuře.
- **Standardní API:** NIM poskytuje průmyslová standardní API, což usnadňuje vytváření a integraci AI aplikací jako jsou chatboty, AI asistenti a další.

NIM je součástí NVIDIA AI Enterprise, jehož cílem je zjednodušit nasazení a provoz AI modelů a zajistit jejich efektivní běh na NVIDIA GPU.

- Ukázka: Použití NVIDIA NIM k volání Phi-3.5-Vision-API  [[Klikněte na tento odkaz](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Lokální spuštění Phi-3/3.5
Inferování ve vztahu k Phi-3, nebo jakémukoliv jazykovému modelu jako GPT-3, znamená proces generování odpovědí nebo předpovědí na základě vstupu, který obdrží. Když poskytnete prompt nebo otázku Phi-3, použije svou natrénovanou neuronovou síť, aby odvodil nejpravděpodobnější a relevantní odpověď analýzou vzorců a vztahů v datech, na kterých byl učen.

**Hugging Face Transformer**
Hugging Face Transformers je výkonná knihovna určená pro zpracování přirozeného jazyka (NLP) a další úlohy strojového učení. Zde jsou některé klíčové body o ní:

1. **Předtrénované modely**: Poskytuje tisíce předtrénovaných modelů, které lze použít pro různé úlohy, jako je klasifikace textu, rozpoznávání pojmenovaných entit, odpovídání na otázky, shrnutí, překlad a generování textu.

2. **Interoperabilita rámců:** Knihovna podporuje několik deep learning frameworků, včetně PyTorch, TensorFlow a JAX. To umožňuje natrénovat model v jednom frameworku a použít jej v jiném.

3. **Multimodální schopnosti:** Kromě NLP podporuje Hugging Face Transformers také úlohy v počítačovém vidění (např. klasifikace obrázků, detekce objektů) a zpracování zvuku (např. rozpoznávání řeči, klasifikace zvuku).

4. **Snadné použití:** Knihovna nabízí API a nástroje pro snadné stažení a doladění modelů, což ji činí přístupnou jak pro začátečníky, tak pro odborníky.

5. **Komunita a zdroje:** Hugging Face má živou komunitu a rozsáhlou dokumentaci, návody a průvodce, které pomáhají uživatelům začít a co nejlépe využít knihovnu.
[oficiální dokumentace](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) nebo jejich [GitHub repozitář](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Toto je nejčastěji používaná metoda, ale vyžaduje také GPU akceleraci. Scénáře jako Vision a MoE totiž vyžadují mnoho výpočtů, které by na CPU bez kvantizace byly velmi pomalé.


- Ukázka: Použití Transformer k volání Phi-3.5-Instruct [Klikněte na tento odkaz](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Ukázka: Použití Transformer k volání Phi-3.5-Vision [Klikněte na tento odkaz](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Ukázka: Použití Transformer k volání Phi-3.5-MoE [Klikněte na tento odkaz](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) je platforma navržená tak, aby usnadnila spuštění velkých jazykových modelů (LLM) lokálně na vašem zařízení. Podporuje různé modely jako Llama 3.1, Phi 3, Mistral a Gemma 2, mezi jinými. Platforma zjednodušuje proces tím, že balí váhy modelu, konfiguraci a data do jednoho balíčku, což uživatelům usnadňuje přizpůsobení a vytváření vlastních modelů. Ollama je dostupná pro macOS, Linux a Windows. Je to skvělý nástroj, pokud chcete experimentovat s LLM nebo je nasadit bez potřeby cloudových služeb. Ollama je nejpřímější cesta, stačí spustit následující příkaz.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) je Microsoftův offline runtime na zařízení pro spuštění modelů jako Phi kompletně na vlastním hardwaru – není potřeba předplatné Azure, API klíč ani síťové připojení. Automaticky vybírá nejlepší dostupný výkonnostní poskytovatel (NPU, GPU nebo CPU) a poskytuje OpenAI-kompatibilní endpoint, takže stávající kód `openai`/Azure AI Inference SDK může být použit s minimálními změnami. Viz [Foundry Local dokumentace](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) pro začátek.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) je multiplatformní akcelerátor pro inferenci a trénink strojového učení. ONNX Runtime pro Generative AI (GENAI) je výkonný nástroj, který pomáhá efektivně spouštět generativní AI modely na různých platformách.

## Co je ONNX Runtime?
ONNX Runtime je open-source projekt, který umožňuje vysoce výkonnou inferenci modelů strojového učení. Podporuje modely ve formátu Open Neural Network Exchange (ONNX), což je standard pro reprezentaci modelů strojového učení. ONNX Runtime inference může umožnit rychlejší zákaznické zkušenosti a nižší náklady, podporuje modely z deep learning frameworků jako PyTorch a TensorFlow/Keras, stejně jako klasické knihovny strojového učení jako scikit-learn, LightGBM, XGBoost a další. ONNX Runtime je kompatibilní s různým hardwarem, ovladači a operačními systémy a poskytuje optimální výkon využitím hardwarových akcelerátorů tam, kde je to možné, spolu s optimalizacemi a transformacemi grafu.

## Co je Generativní AI?
Generativní AI se vztahuje k AI systémům, které dokážou generovat nový obsah, jako je text, obrázky nebo hudba, na základě dat, na kterých byly natrénovány. Příklady zahrnují jazykové modely jako GPT-3 a modely generování obrázků jako Stable Diffusion. Knihovna ONNX Runtime pro GenAI poskytuje generativní AI smyčku pro ONNX modely, včetně inferování s ONNX Runtime, zpracování logits, vyhledávání a vzorkování a správu KV cache.

## ONNX Runtime pro GENAI
ONNX Runtime pro GENAI rozšiřuje schopnosti ONNX Runtime, aby podporoval generativní AI modely. Zde jsou některé klíčové vlastnosti:

- **Široká podpora platforem:** Funguje na různých platformách, včetně Windows, Linux, macOS, Android a iOS.
- **Podpora modelů:** Podporuje mnoho populárních generativních AI modelů, jako jsou LLaMA, GPT-Neo, BLOOM a další.
- **Optimalizace výkonu:** Obsahuje optimalizace pro různé hardwarové akcelerátory jako NVIDIA GPU, AMD GPU a další.
- **Snadné použití:** Poskytuje API pro snadnou integraci do aplikací, které umožňují generovat text, obrázky a jiný obsah s minimálním množstvím kódu.
- Uživatelé mohou volat vysokou úroveň metody generate(), nebo spouštět každou iteraci modelu v cyklu, generovat jeden token za druhým a volitelně aktualizovat parametry generování uvnitř cyklu.
- ONNX runtime také podporuje greedy/beam search a vzorkování TopP, TopK pro generování sekvencí tokenů a vestavěné zpracování logits jako penalizace opakování. Také můžete snadno přidat vlastní skórování.

## Začínáme
Pro začátek s ONNX Runtime pro GENAI můžete postupovat podle těchto kroků:

### Instalace ONNX Runtime:
```Python
pip install onnxruntime
```
### Instalace rozšíření pro Generativní AI:
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
### Ukázka: Použití ONNX Runtime GenAI k volání Phi-3.5-Vision


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


**Další**

Kromě ONNX Runtime, Ollama a Foundry Local referenčních metod můžeme také dokončit referenci kvantitativních modelů na základě metod modelových referencí poskytovaných různými výrobci. Jako například Apple MLX framework s Apple Metal, Qualcomm QNN s NPU, Intel OpenVINO s CPU/GPU atd. Další obsah najdete v [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Více

Naučili jsme se základy rodiny Phi-3/3.5, ale k tomu, abychom se naučili více o SLM, potřebujeme více znalostí. Odpovědi naleznete v Phi-3 Cookbook. Pokud chcete vědět více, navštivte prosím [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->