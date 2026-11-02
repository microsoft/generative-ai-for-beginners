# Uvod v majhne jezikovne modele za generativno umetno inteligenco za začetnike
Generativna umetna inteligenca je fascinantno področje umetne inteligence, ki se osredotoča na ustvarjanje sistemov, ki so sposobni generirati novo vsebino. Ta vsebina lahko sega od besedila in slik do glasbe in celo celotnih virtualnih okolij. Ena najbolj vznemirljivih uporab generativne umetne inteligence je na področju jezikovnih modelov.

## Kaj so majhni jezikovni modeli?

Majhen jezikovni model (SLM) predstavlja zmanjšano različico velikega jezikovnega modela (LLM), ki uporablja veliko arhitekturnih principov in tehnik LLM-jev, a ima pomembno zmanjšano računalniško zahtevnost. 

SLM-ji so podmnožica jezikovnih modelov, zasnovanih za generiranje besedila, ki je podobno človeškemu. Za razliko od svojih večjih različic, kot je GPT-4, so SLM-ji bolj kompaktni in učinkoviti, kar jih naredi idealne za aplikacije, kjer so računalnični viri omejeni. Kljub manjšim dimenzijam lahko še vedno izvajajo različne naloge. Običajno so SLM-ji zgrajeni z zgostitvijo ali destilacijo LLM-jev, pri čemer si prizadevajo ohraniti znaten del funkcionalnosti izvirnega modela in jezikovne zmogljivosti. Ta zmanjšana velikost modela zmanjša splošno kompleksnost, zaradi česar so SLM-ji učinkovitejši tako glede pomnilniške uporabe kot računalniških zahtev. Kljub tem optimizacijam lahko SLM-ji še vedno izvajajo širok nabor nalog obdelave naravnega jezika (NLP):

- Generiranje besedila: ustvarjanje povezanih in kontekstualno ustreznih stavkov ali odstavkov.
- Dokončanje besedila: napovedovanje in dokončanje stavkov na osnovi danega spodbudnega besedila.
- Prevajanje: pretvarjanje besedila iz enega jezika v drugega.
- Povzemanje: skrajševanje daljših besedil v krajše, bolje razumljive povzetke.

Kljub temu z nekaterimi kompromisi v zmogljivosti ali globini razumevanja v primerjavi z njihovimi večjimi različicami.

## Kako delujejo majhni jezikovni modeli?
SLM-ji so trenirani na ogromnih količinah besedilnih podatkov. Med usposabljanjem se naučijo vzorcev in struktur jezika, kar jim omogoča generiranje besedila, ki je tako slovnično pravilno kot kontekstualno ustrezno. Proces usposabljanja vključuje:

- Zbiranje podatkov: pridobivanje velikih nizov besedila iz različnih virov.
- Predobdelava: čiščenje in organiziranje podatkov, da so primerni za usposabljanje.
- Usposabljanje: uporaba algoritmov strojnega učenja za učenje modela, kako razumeti in generirati besedilo.
- Fino nastavljanje: prilagajanje modela za izboljšanje zmogljivosti na specifičnih nalogah.

Razvoj SLM-jev je v skladu z naraščajočo potrebo po modelih, ki jih je mogoče uvajati v okoljih z omejenimi viri, kot so mobilne naprave ali robne računalniške platforme, kjer so polno zmogljivi LLM-ji zaradi visokih zahtev po virih pogosto nepraktični. Z osredotočanjem na učinkovitost SLM-ji usklajujejo zmogljivost z dostopnostjo, kar omogoča širšo uporabo v različnih domenah.

![slm](../../../translated_images/sl/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Cilji učenja

V tem poglavju želimo uvesti znanje o SLM-jih in ga združiti z Microsoft Phi-3 za spoznanje različnih scenarijev pri vsebini besedila, vidu in MoE.

Ob koncu te lekcije bi morali znati odgovoriti na naslednja vprašanja:

- Kaj je SLM?
- Kakšna je razlika med SLM in LLM?
- Kaj je družina Microsoft Phi-3/3.5?
- Kako izvesti inferenco z družino Microsoft Phi-3/3.5?

Ste pripravljeni? Začnimo.

## Razlike med velikimi jezikovnimi modeli (LLM) in majhnimi jezikovnimi modeli (SLM)

Tako LLM-ji kot SLM-ji so zgrajeni na osnovnih principih verjetnostnega strojnega učenja, sledijo podobnim pristopom pri arhitekturni zasnovi, metodah usposabljanja, procesih generiranja podatkov in tehnikah ocenjevanja modelov. Vendar pa jih loči več ključnih dejavnikov.

## Uporabe majhnih jezikovnih modelov

SLM-ji imajo širok spekter uporab, vključno z:

- Chatboti: zagotavljanje podpore uporabnikom in sodelovanje v pogovorih.
- Ustvarjanje vsebine: pomoč pisateljem pri generiranju idej ali celo osnutkov celotnih člankov.
- Izobraževanje: pomoč študentom pri pisnih nalogah ali učenju novih jezikov.
- Dostopnost: ustvarjanje orodij za osebe z omejitvami, kot so sistemi za pretvorbo besedila v govor.

**Velikost**
  
Glavna razlika med LLM in SLM je v velikosti modelov. LLM-ji, kot je ChatGPT (GPT-4), lahko vsebujejo približno 1,76 bilijona parametrov, medtem ko odprtokodni SLM-ji, kot je Mistral 7B, vsebujejo bistveno manj parametrov — približno 7 milijard. Ta razlika je predvsem posledica razlik v arhitekturi modela in procesih usposabljanja. Na primer, ChatGPT uporablja mehanizem samopozornosti znotraj okvirja encoder-decoder, medtem ko Mistral 7B uporablja pozornost z drsečim oknom, kar omogoča bolj učinkovito usposabljanje znotraj modela, ki deluje le kot decoder. Ta arhitekturna razlika ima pomembne posledice za kompleksnost in zmogljivost teh modelov.

**Razumevanje**

SLM-ji so običajno optimizirani za zmogljivost znotraj specifičnih domen, zaradi česar so zelo specializirani, a morda omejeni pri zagotavljanju širšega kontekstualnega razumevanja na več področjih znanja. Nasprotno pa LLM-ji ciljajo na to, da simulirajo človeško inteligenco na bolj celoviti ravni. Usposobljeni na ogromnih in raznolikih podatkih, so LLM-ji zasnovani za dobro delovanje na različnih domenah, ponujajo večjo vsestranskost in prilagodljivost. Zato so LLM-ji bolj primerni za širši nabor nalog, kot so obdelava naravnega jezika in programiranje.

**Računalniške zahteve**

Usposabljanje in uvajanje LLM-jev sta procesoma, ki zahtevata veliko virov, pogosto z obsežno računsko infrastrukturo, vključno z velikimi GPU grozdi. Na primer, usposabljanje modela, kot je ChatGPT, od začetka lahko zahteva na tisoče GPU-jev daljše obdobje. Nasprotno so SLM-ji, zaradi manjšega števila parametrov, bolj dostopni glede računalniških virov. Modeli, kot je Mistral 7B, se lahko usposabljajo in izvajajo lokalno na napravah z zmernimi GPU zmogljivostmi, čeprav usposabljanje še vedno zahteva več ur na več GPU-jih.

**Pristranskost**

Pristranskost je znan problem pri LLM-jih, predvsem zaradi narave podatkov za usposabljanje. Ti modeli pogosto temeljijo na surovih podatkih, ki so javno dostopni na internetu, kar lahko podzastopa ali napačno predstavlja določene skupine, uvaja napačne oznake ali odraža jezikovne pristranskosti, ki vplivajo dialekti, geografske različice in slovnična pravila. Poleg tega kompleksnost arhitektur LLM-jev lahko nehote poveča pristranskost, ki lahko ostane neopažena brez skrbnega fino nastavlanja. Po drugi strani pa so SLM-ji, ki so usposobljeni na bolj omejenih, domenično specifičnih podatkovnih nizih, manj dovzetni za takšne pristranskosti, čeprav je niso popolnoma imuni.

**Inferenca**

Manjša velikost SLM-jev jim prinaša pomembno prednost na področju hitrosti inferenc, kar jim omogoča učinkovito generiranje izhodov na lokalni strojni opremi brez potrebe po obsežnem vzporednem procesiranju. Za razliko od tega LLM-ji zaradi svoje velikosti in kompleksnosti pogosto zahtevajo znatne vzporedne računalniške vire za dosego sprejemljivih časov inferenc. Prisotnost več vzporednih uporabnikov dodatno upočasni odzivne čase LLM-jev, še posebej pri uvajanju v veliki meri.

Povzetek: čeprav imajo tako LLM-ji kot SLM-ji skupne temelje v strojnem učenju, se pomembno razlikujejo glede velikosti modela, zahtev po virih, razumevanja konteksta, dovzetnosti za pristranskosti in hitrosti inferenc. Te razlike odražajo njihovo primernost za različne scenarije uporabe, pri čemer so LLM-ji bolj vsestranski, a zahtevajo več virov, SLM-ji pa nudijo učinkovitejšo, domenično specifično rešitve z manj računske zahtevnosti.

***Opomba: v tej lekciji bomo SLM predstavili na primeru Microsoft Phi-3 / 3.5.***

## Predstavitev družine Phi-3 / Phi-3.5

Družina Phi-3 / 3.5 je namenjena predvsem scenarijem uporabe na področjih besedila, vida in agentov (MoE):

### Phi-3 / 3.5 Instruct

Namenjen predvsem za generiranje besedila, dokončanje pogovorov in izvlečenje vsebine, itd.

**Phi-3-mini**

Jezikovni model z 3,8 milijarde parametrov je na voljo na Microsoft Foundry, Hugging Face in Ollama. Phi-3 modeli znatno presegajo jezikovne modele enake ali večje velikosti na ključnih preizkusih (glej spodnje primerjalne številke, višje številke so boljše). Phi-3-mini premaga modele, ki so dvakrat večji, medtem ko Phi-3-small in Phi-3-medium presegata večje modele, vključno z GPT-3.5.

**Phi-3-small in medium**

Phi-3-small, ki ima le 7 milijard parametrov, premaga GPT-3.5T na različnih področjih jezika, sklepanja, kodiranja in matematike.

Phi-3-medium z 14 milijardami parametrov nadaljuje ta trend in premaga Gemini 1.0 Pro.

**Phi-3.5-mini**

Lahko ga obravnavamo kot nadgradnjo Phi-3-mini. Čeprav se parametri ne spreminjajo, izboljša sposobnost podpore več jezikom (podpira 20+ jezikov: arabščina, kitajščina, češčina, danščina, nizozemščina, angleščina, finščina, francoščina, nemščina, hebrejščina, madžarščina, italijanščina, japonščina, korejščina, norveščina, poljščina, portugalščina, ruščina, španščina, švedščina, tajščina, turščina, ukrajinščina) in doda močno podporo za dolg kontekst.

Phi-3.5-mini z 3,8 milijarde parametrov presega jezikovne modele enake velikosti in je primerljiv z modeli, ki so dvakrat večji.

### Phi-3 / 3.5 Vision

Lahko si predstavljamo, da je Instruct model Phi-3/3.5 sposobnost Phi, da razume, Vision pa so Phi-jeve oči, da razume svet.


**Phi-3-Vision**

Phi-3-vision, s samo 4,2 milijarde parametrov, nadaljuje ta trend in presega večje modele, kot so Claude-3 Haiku in Gemini 1.0 Pro V pri splošnih vizualnih nalogah sklepanja, OCR ter razumevanju tabel in diagramov.


**Phi-3.5-Vision**

Phi-3.5-Vision je tudi nadgradnja Phi-3-Vision, ki dodaja podporo za več slik hkrati. Lahko si ga predstavljate kot izboljšavo vida, saj ne vidite samo slik, ampak tudi videoposnetke.

Phi-3.5-vision presega večje modele, kot so Claude-3.5 Sonnet in Gemini 1.5 Flash pri OCR, razumevanju tabel in grafikonov ter je primerljiv pri splošnih nalogah sklepanja vizualnega znanja. Podpira večslični vhod, tj. izvajanje sklepanja na več vhodnih slikah.


### Phi-3.5-MoE

***Mešanica strokovnjakov (MoE)*** omogoča modelom, da so predhodno usposobljeni z veliko manj računske moči, kar pomeni, da lahko dramatično povečate velikost modela ali nabora podatkov z istim proračunom za računske vire kot gost model. Zlasti naj bi model MoE dosegel enako kakovost kot njegov gost model veliko hitreje med predpripravo.

Phi-3.5-MoE sestavlja 16 modulov strokovnjakov z 3,8 milijarde parametrov vsak. Phi-3.5-MoE s samo 6,6 milijarde aktivnih parametrov dosega podobno raven sklepanja, razumevanja jezika in matematike kot veliko večji modeli.

Model družine Phi-3/3.5 lahko uporabljamo glede na različne scenarije. Za razliko od LLM lahko Phi-3/3.5-mini ali Phi-3/3.5-Vision uvajate na robnih napravah.


## Kako uporabljati modele družine Phi-3/3.5

Želimo uporabljati Phi-3/3.5 v različnih scenarijih. V nadaljevanju bomo uporabili Phi-3/3.5 glede na različne scenarije.

![phi3](../../../translated_images/sl/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inferenca prek storitev Cloud API

**Microsoft Foundry modeli**

> **Opomba:** GitHub modeli bodo ukinjeni konec julija 2026. [Microsoft Foundry modeli](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) so neposredna zamenjava.

> **Opomba:** Celotna družina Phi-3/3.5 (Instruct, Vision in MoE različice) je bila umaknjena iz kataloga Microsoft Foundry modelov 30.08.2025. Tam uporabite `Phi-4` (Instruct) ali `Phi-4-mini-instruct` — spodnji primeri Phi-3/3.5 še vedno delujejo preko Hugging Face, Ollama, ONNX Runtime in NVIDIA NIM.

Microsoft Foundry modeli zdaj zagotavljajo naslednike Phi-4. Uporabite `Phi-4` ali `Phi-4-mini-instruct` namesto upokojenih modelov Phi-3/3.5 ob sledenju primerom Cloud API.

- Demo: primerjava učinkov Phi-3-mini in Phi-3.5-mini v kitajskih scenarijih

![phi3](../../../translated_images/sl/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/sl/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Če želite uporabljati vidne (multimodalne) modele v oblaku, uporabite trenutno na voljo `Phi-4-multimodal-instruct` prek Microsoft Foundry, namesto upokojenih Phi-3/3.5 Vision modelov; za tekstovne naloge uporabite `Phi-4` ali `Phi-4-mini-instruct`. Model Phi-3.5 MoE je bil umaknjen iz Microsoft Foundry, zato uporabite druge možnosti opisane v tej lekciji (na primer Hugging Face), če ga želite preizkusiti. Če vas zanima, si lahko preberete Phi kuharico, kako klicati Phi modele prek Microsoft Foundry [Kliknite ta povezavo](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Poleg katalogov Microsoft Foundry Modelov na oblaku, lahko uporabite tudi [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) za izvedbo povezanih klicev. Obiščete lahko NVIDIA NIM za izvedbo API klicev družine Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) je niz pospešenih mikro-storitev za inferenco, zasnovan, da pomaga razvijalcem učinkovito uvajati AI modele v različnih okoljih, vključno z oblaki, podatkovnimi centri in delovnimi postajami.

Tukaj so nekatere ključne značilnosti NVIDIA NIM:

- **Enostavnost nameščanja:** NIM omogoča nameščanje AI modelov z eno samo ukazno vrstico, kar olajša integracijo v obstoječe delovne tokove.
- **Optimizirana zmogljivost:** Izrablja vnaprej optimizirane NVIDIA-jeve pogone za sklepanje, kot sta TensorRT in TensorRT-LLM, da zagotovi nizko zakasnitev in visoko prepustnost.
- **Prilagodljivost:** NIM podpira samodejno skaliranje na Kubernetesu, kar mu omogoča učinkovito obvladovanje različnih delovnih obremenitev.
- **Varnost in nadzor:** Organizacije lahko ohranijo nadzor nad svojimi podatki in aplikacijami z lastnim gostovanjem NIM mikroservisov na lastni upravljani infrastrukturi.
- **Standardni API-ji:** NIM zagotavlja industrijsko standardne API-je, kar olajša gradnjo in integracijo AI aplikacij, kot so klepetalniki, AI pomočniki in druge.

NIM je del NVIDIA AI Enterprise, katerega cilj je poenostaviti nameščanje in operacionalizacijo AI modelov ter zagotoviti njihovo učinkovito delovanje na NVIDIA GPU-jih.

- Demo: Uporaba NVIDIA NIM za klic Phi-3.5-Vision-API  [[Kliknite ta povezavo](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Lokalno izvajanje Phi-3/3.5
sklepanje v zvezi s Phi-3 ali katerim koli jezikovnim modelom, kot je GPT-3, pomeni proces ustvarjanja odgovorov ali napovedi na podlagi prejetega vhoda. Ko Phi-3 dobite poziv ali vprašanje, uporablja svoje usposobljeno nevronsko mrežo, da zazna najbolj verjeten in relevanten odgovor z analiziranjem vzorcev in povezav v podatkih, na katerih je bil treniran.

**Hugging Face Transformer**
Hugging Face Transformers je zmogljiva knjižnica, zasnovana za obdelavo naravnega jezika (NLP) in druge naloge strojnega učenja. Tukaj so nekateri ključni poudarki:

1. **Vnaprej naučeni modeli**: Ponuja tisoče vnaprej naučenih modelov, ki jih je mogoče uporabiti za različne naloge, kot so razvrščanje besedil, prepoznavanje imenovanih entitet, odgovarjanje na vprašanja, povzemanje, prevajanje in generiranje besedil.

2. **Združljivost ogrodij:** Knjižnica podpira več ogrodij za globoko učenje, vključno s PyTorch, TensorFlow in JAX. To omogoča usposabljanje modela v enem ogrodju in uporabo v drugem.

3. **Multimodalne zmogljivosti:** Poleg NLP podpira Hugging Face Transformers tudi naloge v računalniškem vidu (npr. razvrščanje slik, zaznavanje objektov) in obdelavi zvoka (npr. prepoznavanje govora, razvrščanje zvoka).

4. **Enostavnost uporabe:** Knjižnica ponuja API-je in orodja za enostavno prenašanje in prilagajanje modelov, zaradi česar je dostopna tako začetnikom kot strokovnjakom.

5. **Skupnost in viri:** Hugging Face ima živahno skupnost ter obsežno dokumentacijo, vodnike in tutorijale, ki pomagajo uporabnikom začeti in kar najbolje izkoristiti knjižnico.
[uradna dokumentacija](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) ali njihov [GitHub repozitorij](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

To je najpogosteje uporabljena metoda, a zahteva tudi pospeševanje z GPU-jem. Še posebej scenariji, kot sta Vision in MoE, zahtevajo veliko izračunov, kar bo na CPU-ju brez kvantizacije zelo počasi.


- Demo: Uporaba Transformerja za klic Phi-3.5-Instruct [Kliknite ta povezavo](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Uporaba Transformerja za klic Phi-3.5-Vision [Kliknite ta povezavo](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Uporaba Transformerja za klic Phi-3.5-MoE [Kliknite ta povezavo](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) je platforma zasnovana za lažje lokalno izvajanje velikih jezikovnih modelov (LLM) na vaši napravi. Podpira različne modele, kot so Llama 3.1, Phi 3, Mistral in Gemma 2, med drugimi. Platforma poenostavi postopek z združevanjem uteži modela, konfiguracije in podatkov v en paket, zaradi česar je za uporabnike bolj dostopna prilagoditev in ustvarjanje lastnih modelov. Ollama je na voljo za macOS, Linux in Windows. Odlično orodje, če želite eksperimentirati ali izvajati LLM brez odvisnosti od oblačnih storitev. Ollama je najbolj neposredna pot, potrebujete samo izvesti naslednji ukaz.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) je Microsoftova off-line, na napravi delujoča izvedbena okolja za izvajanje modelov, kot je Phi, povsem na vaši lastni strojni opremi - brez naročnine na Azure, API ključa ali omrežne povezave. Samodejno izbere najboljši razpoložljivi izvajalec (NPU, GPU ali CPU) in izpostavi OpenAI-kompatibilno končno točko, tako da lahko obstoječa `openai`/Azure AI Inference SDK koda kaže nanj z minimalnimi spremembami. Za začetek si oglejte [Foundry Local dokumentacijo](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst).

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Ali uporabite SDK neposredno v Pythonu:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime za GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) je medplatformni pospeševalnik sklepanja in treniranja strojnega učenja. ONNX Runtime za Generativno AI (GENAI) je zmogljivo orodje, ki vam pomaga učinkovito izvajati generativne AI modele na različnih platformah.

## Kaj je ONNX Runtime?
ONNX Runtime je odprtokodni projekt, ki omogoča visoko zmogljivo sklepanje modelov strojnega učenja. Podpira modele v formatu Open Neural Network Exchange (ONNX), ki je standard za predstavitev modelov strojnega učenja. ONNX Runtime sklepanje omogoča hitrejše uporabniške izkušnje in nižje stroške ter podpira modele iz ogrodij za globoko učenje, kot so PyTorch in TensorFlow/Keras, pa tudi klasične knjižnice strojnega učenja, kot so scikit-learn, LightGBM, XGBoost itd. ONNX Runtime je združljiv z različnimi strojno opremo, gonilniki in operacijskimi sistemi ter zagotavlja optimalno zmogljivost z izrabo strojnih pospeševalnikov, kjer je mogoče, skupaj z optimizacijami in transformacijami grafov.

## Kaj je Generativna AI?
Generativna AI se nanaša na AI sisteme, ki lahko ustvarjajo novo vsebino, kot so besedilo, slike ali glasba, na podlagi podatkov, na katerih so bili usposobljeni. Primeri vključujejo jezikovne modele, kot je GPT-3, in modele za generiranje slik, kot je Stable Diffusion. Knjižnica ONNX Runtime za GenAI zagotavlja generativni AI zanko za ONNX modele, vključno s sklepanje z ONNX Runtime, obdelavo logitov, iskanjem in vzorčenjem ter upravljanjem KV predpomnilnika.

## ONNX Runtime za GENAI
ONNX Runtime za GENAI razširja zmogljivosti ONNX Runtime za podporo generativnim AI modelom. Tukaj je nekaj ključnih funkcij:

- **Široka podpora platformam:** Deluje na različnih platformah, vključno z Windows, Linux, macOS, Android in iOS.
- **Podpora modelom:** Podpira številne priljubljene generativne AI modele, kot so LLaMA, GPT-Neo, BLOOM in drugi.
- **Optimizacija zmogljivosti:** Vključuje optimizacije za različne strojne pospeševalce, kot so NVIDIA GPU-ji, AMD GPU-ji in drugi2.
- **Enostavnost uporabe:** Zagotavlja API-je za enostavno integracijo v aplikacije, ki vam omogočajo generiranje besedila, slik in druge vsebine z minimalno kodo.
- Uporabniki lahko kličejo visoko raven generate() metodo ali izvajajo vsako iteracijo modela v zanki, generirajoč en znak naenkrat in po želji posodabljajo parametre generacije znotraj zanke.
- ONNX runtime prav tako podpira greedy/beam search in TopP, TopK vzorčenje za generiranje zaporedij znakov ter vgrajeno obdelavo logitov, kot so kazni za ponavljanje. Prav tako lahko preprosto dodate lastno ocenjevanje.

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

### Zaženite model: Tukaj je preprost primer v Pythonu:
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

Poleg referenčnih metod ONNX Runtime, Ollama in Foundry Local lahko dopolnimo referenco kvantitativnih modelov na podlagi refenčnih metod modelov različnih proizvajalcev. Kot so Apple MLX ogrodje z Apple Metal, Qualcomm QNN z NPU, Intel OpenVINO z CPU/GPU itd. Več vsebine lahko najdete tudi v [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Več

Naučili smo se osnov Phi-3/3.5 družine, vendar za nadaljnje spoznavanje SLM potrebujemo še več znanja. Odgovore lahko najdete v Phi-3 Cookbook. Če želite več izvedeti, obiščite [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->