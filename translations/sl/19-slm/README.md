# Uvod v Male Jezikovne Modelle za Generativno AI za Začetnike
Generativna AI je fascinantno področje umetne inteligence, ki se osredotoča na ustvarjanje sistemov, sposobnih generiranja nove vsebine. Ta vsebina lahko sega od besedil in slik do glasbe in celo celotnih virtualnih okolij. Ena najzanimivejših aplikacij generativne AI je na področju jezikovnih modelov.

## Kaj so Mali Jezikovni Modeli?

Mali Jezikovni Model (SLM) predstavlja zmanjšano različico velikega jezikovnega modela (LLM), ki uporablja mnoge arhitekturne principe in tehnike LLM-jev, vendar z bistveno zmanjšano računalniško zahtevnostjo. 

SLM-ji so podmnožica jezikovnih modelov, zasnovanih za generiranje besedila, podobnega človeškemu. Za razliko od večjih različic, kot je GPT-4, so SLM-ji bolj kompaktni in učinkoviti, zaradi česar so idealni za uporabe, kjer so računalniški viri omejeni. Kljub manjšimu obsegu lahko izvajajo različne naloge. Običajno so SLM-ji zgrajeni z zgoščevanjem ali destilacijo LLM-jev, pri čemer si prizadevajo ohraniti velik del funkcionalnosti in jezikovnih zmogljivosti originalnega modela. Zmanjšanje velikosti modela zmanjša skupno kompleksnost, zaradi česar so SLM-ji učinkovitejši tako glede uporabe pomnilnika kot tudi računalniških zahtev. Kljub tem optimizacijam lahko SLM-ji še vedno izvajajo širok nabor nalog obdelave naravnega jezika (NLP):

- Generiranje besedila: Ustvarjanje koherentnih in kontekstualno ustreznih stavkov ali odstavkov.
- Dokončanje besedila: Napovedovanje in dokončevanje stavkov na podlagi danega povabila.
- Prevajanje: Pretvarjanje besedila iz enega jezika v drugega.
- Povzemanje: Skrčevanje dolgih besedil v krajše, bolj prebavljive povzetke.

Čeprav z nekaterimi kompromisi v zmogljivosti ali globini razumevanja v primerjavi z njihovimi večjimi različicami. 

## Kako Delujejo Mali Jezikovni Modeli?
SLM-ji so usposobljeni na ogromnih količinah besedilnih podatkov. Med usposabljanjem se naučijo vzorcev in struktur jezika, kar jim omogoča generiranje besedila, ki je tako slovnično pravilno kot kontekstualno primerno. Proces usposabljanja vključuje:

- Zbiranje podatkov: Pridobivanje velikih zbirk besedil iz različnih virov.
- Predobdelava: Čiščenje in organizacija podatkov, da so primerni za usposabljanje.
- Usposabljanje: Uporaba algoritmov strojnega učenja za učenje razumevanja in generiranja besedila.
- Finetuning: Prilagajanje modela za izboljšanje zmogljivosti pri specifičnih nalogah.

Razvoj SLM-jev sovpada z naraščajočo potrebo po modelih, ki jih lahko namestimo v okolja z omejenimi viri, kot so mobilne naprave ali robne računalniške platforme, kjer so polni LLM-ji lahko nepraktični zaradi svojih visokih zahtev po virih. Z osredotočenjem na učinkovitost SLM-ji uravnotežijo zmogljivost z dostopnostjo, kar omogoča širšo uporabo v različnih področjih.

![slm](../../../translated_images/sl/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Cilji učenja

V tem gradivu želimo predstaviti znanje o SLM in ga združiti z Microsoft Phi-3 za učenje različnih scenarijev pri vsebini besedila, viziji in MoE.

Ob koncu te lekcije bi morali biti sposobni odgovoriti na naslednja vprašanja:

- Kaj je SLM?
- Kakšna je razlika med SLM in LLM?
- Kaj je družina Microsoft Phi-3/3.5?
- Kako izvajati sklepanje z družino Microsoft Phi-3/3.5?

Ste pripravljeni? Začnimo.

## Razlike med Velikimi Jezikovnimi Modeli (LLM) in Malimi Jezikovnimi Modeli (SLM)

Tako LLM-ji kot SLM-ji temeljijo na osnovnih principih verjetnostnega strojnega učenja, sledijo podobnim pristopom pri arhitekturni zasnovi, metodah usposabljanja, procesih generiranja podatkov in tehnikah ocenjevanja modelov. Vendar pa jih loči več ključnih dejavnikov.

## Uporabe Malih Jezikovnih Modelov

SLM-ji imajo širok spekter aplikacij, med drugim:

- Klepetalni roboti: Nudenje podpore strankam in komunikacija z uporabniki na pogovorni način.
- Ustvarjanje vsebin: Pomoč pisateljem pri generiranju idej ali celo predlaganju celotnih člankov.
- Izobraževanje: Pomoč učencem pri pisnih nalogah ali učenju novih jezikov.
- Dostopnost: Ustvarjanje orodij za osebe z ovirami, kot so sistemi za pretvorbo besedila v govor.

**Velikost**
  
Primarna razlika med LLM-ji in SLM-ji je v obsegu modelov. LLM-ji, kot je ChatGPT (GPT-4), lahko vsebujejo ocenjenih 1,76 bilijona parametrov, medtem ko imajo odprtokodni SLM-ji, kot je Mistral 7B, znatno manj parametrov — približno 7 milijard. Ta razlika izvira predvsem iz arhitekture modela in procesov usposabljanja. Na primer, ChatGPT uporablja mehanizem samopozornosti v encoder-decoder arhitekturi, medtem ko Mistral 7B uporablja pozornost z drsečim oknom, ki omogoča učinkovitejše usposabljanje znotraj modela samo-decoderja. Ta arhitekturna razlika ima globoke posledice za kompleksnost in zmogljivost teh modelov.

**Razumevanje**

SLM-ji so običajno optimizirani za delovanje znotraj specifičnih domen, zaradi česar so zelo specializirani, a morda omejeni v svoji sposobnosti zagotavljanja širokega kontekstualnega razumevanja na več področjih znanja. Nasprotno si LLM-ji prizadevajo simulirati inteligenco, podobno človekovi, na širšem nivoju. Usposobljeni na ogromnih, raznolikih podatkovnih zbirkah, so LLM-ji namenjeni doseganju dobrih rezultatov na različnih področjih, kar jim daje večjo vsestranskost in prilagodljivost. Zato so LLM-ji primernejši za širši nabor nalog, kot so obdelava naravnega jezika in programiranje.

**Računalniški viri**

Usposabljanje in uvajanje LLM-jev sta procesa z veliko porabo virov, ki pogosto zahtevata obsežno računalniško infrastrukturo, vključno z velikimi GPU grozdi. Na primer, usposabljanje modela, kot je ChatGPT, od začetka, lahko zahteva tisoče GPU-jev za dolga obdobja. Nasprotno so SLM-ji z manjšim številom parametrov bolj dostopni glede računalniških virov. Modeli, kot je Mistral 7B, se lahko usposabljajo in izvajajo na lokalnih računalnikih z zmernimi GPU zmogljivostmi, čeprav usposabljanje še vedno zahteva več ur na več GPU-jih.

**Pristranskost**

Pristranskost je poznan problem pri LLM-jih, predvsem zaradi narave podatkov za usposabljanje. Ti modeli pogosto temeljijo na surovih, javno dostopnih podatkih z interneta, ki lahko premalo predstavljajo ali napačno predstavljajo določene skupine, uvajajo napačno označevanje ali odražajo jezikovne pristranskosti, ki so povezane z dialekti, geografskimi različicami in slovničnimi pravili. Poleg tega lahko kompleksnost arhitektur LLM-jev nehote poveča pristranskost, ki jo je brez skrbne prilagoditve težko zaznati. Po drugi strani pa so SLM-ji, ki so usposobljeni na bolj omejenih, domeno specifičnih podatkovnih zbirkah, inherentno manj dovzetni za takšne pristranskosti, čeprav niso povsem imuni.

**Sklepanje**

Manjša velikost SLM-jev jim omogoča pomembno prednost pri hitrosti sklepanja, saj lahko učinkovito generirajo izhod na lokalni strojni opremi brez potrebe po obsežnem vzporednem procesiranju. Nasprotno pa LLM-ji zaradi svoje velikosti in kompleksnosti pogosto zahtevajo znatne vzporedne računalniške vire za doseganje sprejemljivih časov sklepanja. Pristnost več sočasnih uporabnikov še dodatno upočasni odzivne čase LLM-jev, še posebej pri uvajanju v velikem obsegu.

Povzemimo, čeprav oba, LLM-ji in SLM-ji, temeljita na osnovi strojnega učenja, se bistveno razlikujeta glede velikosti modela, zahtev po virih, razumevanja konteksta, dovzetnosti za pristranskosti in hitrosti sklepanja. Te razlike odražajo njuno primernost za različne primere uporabe, pri čemer so LLM-ji bolj vsestranski, a zahtevajo več virov, SLM-ji pa nudijo domeno specifično učinkovitost z zmanjšanimi računalniškimi zahtevami.

***Opomba: V tej lekciji bomo predstavili SLM z uporabo Microsoft Phi-3 / 3.5 kot primer.***

## Predstavitev družine Phi-3 / Phi-3.5

Družina Phi-3 / 3.5 je usmerjena predvsem v scenarije aplikacij za besedilo, vid in agente (MoE):

### Phi-3 / 3.5 Instruct

Namenjen predvsem generiranju besedila, dokončanju pogovorov in izvlečku informacij iz vsebin itd.

**Phi-3-mini**

3,8-milijardni jezikovni model je na voljo na Microsoft Foundry, Hugging Face in Ollama. Phi-3 modeli znatno presegajo jezikovne modele enake in večje velikosti na ključnih merilih (glej spodnje številke meritev, višje številke so boljše). Phi-3-mini presega modele dvakrat večje velikosti, medtem ko Phi-3-small in Phi-3-medium presegata večje modele, vključno z GPT-3.5.

**Phi-3-small & medium**

Phi-3-small s samo 7 milijardami parametrov premaga GPT-3.5T v različnih merilih za jezik, sklepanje, programiranje in matematiko.

Phi-3-medium s 14 milijardami parametrov nadaljuje ta trend in prekaša Gemini 1.0 Pro.

**Phi-3.5-mini**

Lahko ga obravnavamo kot nadgradnjo Phi-3-mini. Čeprav parametri ostajajo nespremenjeni, izboljša podporo za več jezikov (podpira 20+ jezikov: arabski, kitajski, češki, danski, nizozemski, angleški, finski, francoski, nemški, hebrejski, madžarski, italijanski, japonski, korejski, norveški, poljski, portugalski, ruski, španski, švedski, tajski, turški, ukrajinski) in doda močnejšo podporo za dolg kontekst.

Phi-3.5-mini s 3,8 milijardami parametrov presega jezikovne modele iste velikosti in je primerljiv z modeli dvakrat večje velikosti.

### Phi-3 / 3.5 Vision

Lahko smatrajmo Instruct model Phi-3/3.5 kot sposobnost Phi za razumevanje, medtem ko je Vision tisto, kar Phi-ju daje oči za razumevanje sveta.


**Phi-3-Vision**

Phi-3-vision s samo 4,2 milijardami parametrov nadaljuje ta trend in prekaša večje modele, kot so Claude-3 Haiku in Gemini 1.0 Pro V na splošnih nalogah vizualnega sklepanja, OCR, ter razumevanja tabel in diagramov.


**Phi-3.5-Vision**

Phi-3.5-Vision je tudi nadgradnja Phi-3-Vision, ki dodaja podporo za več slik. Lahko si ga zamislimo kot izboljšavo vida, ki omogoča ne le gledanje slik, ampak tudi videov.

Phi-3.5-vision prekaša večje modele, kot so Claude-3.5 Sonnet in Gemini 1.5 Flash, na OCR, razumevanju tabel in grafikonov ter je primerljiv pri splošnih nalogah vizualnega znanja in sklepanja. Podpira večslični vhod, torej sklepa na podlagi več vhodnih slik.


### Phi-3.5-MoE

***Mikstura strokovnjakov (MoE)*** omogoča modelom predhodno usposabljanje z veliko manj izračunov, kar pomeni, da lahko model ali velikost podatkovnega nabora znatno povečate z enakim proračunom za računalniške vire kot pri gostem modelu. Še posebej bi moral model MoE med predtreniranjem doseči enako kakovost kot njegov gost sorodnik bistveno hitreje.

Phi-3.5-MoE obsega 16x3,8-milijardnih strokovnih modulov. Phi-3.5-MoE z le 6,6 milijardami aktivnih parametrov dosega primerljivo raven sklepanja, razumevanja jezika in matematike kot veliko večji modeli.

Model družine Phi-3/3.5 lahko uporabljamo glede na različne scenarije. Za razliko od LLM-jev lahko na robnih napravah uvedete Phi-3/3.5-mini ali Phi-3/3.5-Vision.


## Kako uporabljati modele družine Phi-3/3.5

Upamo, da bomo Phi-3/3.5 uporabili v različnih scenarijih. Naslednje bomo prikazali uporabo Phi-3/3.5 v različnih scenarijih.

![phi3](../../../translated_images/sl/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Izvedba prek oblačnih API-jih

**Microsoft Foundry modeli**

> **Opomba:** GitHub modeli se upokojijo konec julija 2026. [Microsoft Foundry modeli](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) so neposredna zamenjava.

> **Opomba:** V celotni družini Phi-3/3.5 (Instruct, Vision in MoE različice) so bili na dan 2025-08-30 odstranjeni iz kataloga Microsoft Foundry modelov. Namesto njih uporabite `Phi-4` (Instruct) ali `Phi-4-mini-instruct` — spodnji primeri Phi-3/3.5 še delujejo prek Hugging Face, Ollama, ONNX Runtime in NVIDIA NIM.

Microsoft Foundry modeli zdaj ponujajo naslednike Phi-4. Pri uporabi primerov oblačnih API-jev namesto upokojenih Phi-3/3.5 modelov uporabite `Phi-4` ali `Phi-4-mini-instruct`.

- Demo: Primerjava učinkov Phi-3-mini in Phi-3.5-mini v kitajskih scenarijih

![phi3](../../../translated_images/sl/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/sl/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Če želite uporabiti modele za vid (multimodalne) v oblaku, uporabite trenutno razpoložljive `Phi-4-multimodal-instruct` prek Microsoft Foundry namesto upokojenih Phi-3/3.5 Vision modelov; za besedilne naloge uporabite `Phi-4` ali `Phi-4-mini-instruct`. Phi-3.5 MoE model je bil upokojen v Microsoft Foundry, zato uporabite druge možnosti, opisane v tej lekciji (na primer Hugging Face), če ga želite preizkusiti. Če vas zanima, lahko preberete Phi Kuharsko knjigo o tem, kako klicati Phi modele prek Microsoft Foundry [Kliknite na to povezavo](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Poleg kataloga Microsoft Foundry modelov na oblaku lahko uporabite tudi [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) za dokončanje povezanih klicev. Obiščete lahko NVIDIA NIM za dokončanje API klicev družine Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) je niz pospešenih mikrostoritev sklepanja, zasnovanih za učinkovito uvajanje AI modelov v različnih okoljih, vključno z oblaki, podatkovnimi centri in delovnimi postajami.

Tukaj je nekaj ključnih lastnosti NVIDIA NIM:

- **Enostavnost namestitve:** NIM omogoča namestitev modelov umetne inteligence z eno samo ukazno vrstico, kar omogoča enostavno integracijo v obstoječe delovne procese.
- **Optimizirana zmogljivost:** Izrablja NVIDIA-jeve vnaprej optimizirane pogone za sklepanje, kot sta TensorRT in TensorRT-LLM, da zagotovi nizko latenco in visoko prepustnost.
- **Prilagodljivost:** NIM podpira samodejno prilagajanje velikosti na Kubernetes, kar omogoča učinkovito upravljanje spremenljivih delovnih obremenitev.
- **Varnost in nadzor:** Organizacije lahko ohranijo nadzor nad svojimi podatki in aplikacijami z gostovanjem NIM mikrostoritev na lastni upravljani infrastrukturi.
- **Standardni API-ji:** NIM zagotavlja industrijske standardne API-je, kar olajša gradnjo in integracijo AI aplikacij, kot so klepetalni roboti, AI asistenti in drugo.

NIM je del NVIDIA AI Enterprise, ki si prizadeva poenostaviti namestitev in operacionalizacijo modelov umetne inteligence ter zagotoviti učinkovito delovanje na NVIDIA GPU-jih.

- Demo: Uporaba NVIDIA NIM za klic Phi-3.5-Vision-API [[Kliknite na to povezavo](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Lokalno izvajanje Phi-3/3.5
Sklepanje v povezavi s Phi-3 ali katerim koli jezikovnim modelom, kot je GPT-3, se nanaša na proces ustvarjanja odgovorov ali napovedi na podlagi vhodnih podatkov. Ko Phi-3 zagotovite poziv ali vprašanje, uporabi svoj usposobljeni nevronski model za sklepanja o najbolj verjetnem in ustreznem odgovoru z analizo vzorcev in odnosov v podatkih, na katerih je bil usposobljen.

**Hugging Face Transformer**
Hugging Face Transformers je zmogljiva knjižnica, namenjena obdelavi naravnega jezika (NLP) in drugim nalogam strojnega učenja. Tukaj je nekaj ključnih točk o njej:

1. **Vnaprej usposobljeni modeli**: Ponuja tisoče vnaprej usposobljenih modelov, ki jih lahko uporabite za različne naloge, kot so klasifikacija besedila, prepoznavanje imenovanih entitet, odgovarjanje na vprašanja, povzema, prevajanje in generiranje besedila.

2. **Interoperabilnost okvirov:** Knjižnica podpira več globinskih učnih okvirjev, vključno s PyTorch, TensorFlow in JAX. To vam omogoča usposabljanje modela v enem okviru in njegovo uporabo v drugem.

3. **Multimodalne zmogljivosti:** Poleg NLP podpora Hugging Face Transformers vključuje naloge v računalniškem vidu (npr. klasifikacija slik, zaznavanje objektov) in zvočni obdelavi (npr. prepoznavanje govora, klasifikacija zvoka).

4. **Enostavnost uporabe:** Knjižnica ponuja API-je in orodja za enostavno prenašanje in prilagajanje modelov, kar jo naredi dostopno tako za začetnike kot strokovnjake.

5. **Skupnost in viri:** Hugging Face ima živahno skupnost in obsežno dokumentacijo, vodiče in vodiče za pomoč uporabnikom pri začetku in maksimalni izrabi knjižnice.
[uradna dokumentacija](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) ali njihov [GitHub repozitorij](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

To je najpogosteje uporabljena metoda, a zahteva tudi pospešek GPU. Navsezadnje scenariji, kot sta Vision in MoE, zahtevajo veliko izračunov, ki bodo na CPU zelo počasni, če niso kvantizirani.


- Demo: Uporaba Transformerja za klic Phi-3.5-Instruct [Kliknite na to povezavo](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Uporaba Transformerja za klic Phi-3.5-Vision [Kliknite na to povezavo](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Uporaba Transformerja za klic Phi-3.5-MoE [Kliknite na to povezavo](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) je platforma, zasnovana za enostavnejše lokalno izvajanje velikih jezikovnih modelov (LLM) na vašem računalniku. Podpira različne modele, kot so Llama 3.1, Phi 3, Mistral in Gemma 2, med drugim. Platforma poenostavi postopek z združevanjem teže modela, konfiguracije in podatkov v en paket, zaradi česar je uporabnikom bolj dostopna prilagoditev in ustvarjanje lastnih modelov. Ollama je na voljo za macOS, Linux in Windows. Odlično orodje, če želite eksperimentirati ali uporabljati LLM-je brez odvisnosti od oblačnih storitev. Ollama je najhitrejša pot, samo izvedete naslednji ukaz.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) je Microsoftovo brez povezave, na napravi delujoče izvajanje za modele, kot je Phi, popolnoma na vaši lastni strojni opremi – brez naročnine na Azure, API ključev ali omrežne povezave. Samodejno izbere najboljšega razpoložljivega izvajalnega ponudnika (NPU, GPU ali CPU) in ponuja OpenAI-kompatibilno točko za dostop, tako da obstoječ koda iz `openai`/Azure AI Inference SDK lahko z minimalnimi spremembami kaže nanj. Oglejte si [Foundry Local dokumentacijo](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) za začetek.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Ali neposredno uporabite SDK v Pythonu:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime za GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) je večplatformski pospeševalnik strojnega učenja za sklepanje in usposabljanje. ONNX Runtime za Generative AI (GENAI) je zmogljivo orodje, ki vam pomaga učinkovito izvajati generativne AI modele na različnih platformah.

## Kaj je ONNX Runtime?
ONNX Runtime je odprtokodni projekt, ki omogoča visoko zmogljivo sklepanje modelov strojnega učenja. Podpira modele v formatu Open Neural Network Exchange (ONNX), kar je standard za predstavitev modelov strojnega učenja. ONNX Runtime sklepanje lahko omogoči hitrejše uporabniške izkušnje in nižje stroške, saj podpira modele iz globokih učnih okvirjev, kot so PyTorch in TensorFlow/Keras, pa tudi klasične knjižnice strojnega učenja, kot so scikit-learn, LightGBM, XGBoost itd. ONNX Runtime je združljiv z različnimi strojno opremo, gonilniki in operacijskimi sistemi ter zagotavlja optimalno zmogljivost z izrabo strojnih pospeševalnikov tam, kjer je to mogoče, skupaj z optimizacijami in transformacijami grafov.

## Kaj je Generativna umetna inteligenca?
Generativna umetna inteligenca se nanaša na AI sisteme, ki lahko ustvarjajo novo vsebino, kot so besedilo, slike ali glasba, na podlagi podatkov, na katerih so bili usposobljeni. Primeri vključujejo jezikovne modele, kot je GPT-3, in modele za generiranje slik, kot je Stable Diffusion. Knjižnica ONNX Runtime za GenAI zagotavlja generativno AI zanko za ONNX modele, vključno s sklepanjem preko ONNX Runtime, obdelavo logitov, iskanjem in vzorčenjem ter upravljanjem KV predpomnilnika.

## ONNX Runtime za GENAI
ONNX Runtime za GENAI razširja zmožnosti ONNX Runtime za podporo generativnim AI modelom. Tukaj so nekatere ključne lastnosti:

- **Široka podpora platformam:** Deluje na različnih platformah, vključno z Windows, Linux, macOS, Android in iOS.
- **Podpora modelom:** Podpira številne priljubljene generativne AI modele, kot so LLaMA, GPT-Neo, BLOOM in drugi.
- **Optimizacija zmogljivosti:** Vključuje optimizacije za različne strojne pospeševalnike, kot so NVIDIA GPU-ji, AMD GPU-ji in drugi2.
- **Enostavnost uporabe:** Ponuja API-je za enostavno integracijo v aplikacije, ki vam omogočajo generiranje besedil, slik in druge vsebine z minimalno kodo.
- Uporabniki lahko pokličejo visoko raven metode generate(), ali pa izvajajo vsako ponovitev modela v zanki, generirajoč en žeton naenkrat in po potrebi posodabljajo parametre generiranja znotraj zanke.
- ONNX runtime prav tako podpira pohlepno/žarkovsko iskanje in TopP, TopK vzorčenje za ustvarjanje zaporedij žetonov ter vgrajeno obdelavo logitov, kot so kazni za ponavljanje. Prav tako lahko enostavno dodate lastno ocenjevanje.

## Začetek
Za začetek z ONNX Runtime za GENAI lahko sledite tem korakom:

### Namestite ONNX Runtime:
```Python
pip install onnxruntime
```
### Namestite Generative AI Extensions:
```Python
pip install onnxruntime-genai
```

### Zaženi model: Tukaj je preprost primer v Pythonu:
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
### Demo: Uporaba ONNX Runtime GenAI za klic Phi-3.5-Vision


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


**Drugo**

Poleg referenčnih metod ONNX Runtime, Ollama in Foundry Local lahko zaključimo tudi referenco kvantitativnih modelov glede na metode referenciranja modelov, ki jih zagotavljajo različni proizvajalci. Na primer Apple MLX framework z Apple Metal, Qualcomm QNN z NPU, Intel OpenVINO s CPU/GPU itd. Več vsebin lahko najdete tudi v [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Več

Spoznali smo osnove družine Phi-3/3.5, vendar za več znanja o SLM potrebujemo več informacij. Odgovore lahko poiščete v Phi-3 Cookbook. Če želite izvedeti več, obiščite [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->