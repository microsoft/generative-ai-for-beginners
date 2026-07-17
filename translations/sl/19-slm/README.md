# Uvod v majhne jezikovne modele za generativno AI za začetnike
Generativna AI je fascinantno področje umetne inteligence, ki je osredotočeno na ustvarjanje sistemov, ki so sposobni generirati novo vsebino. Ta vsebina lahko sega od besedil in slik do glasbe in celo celotnih virtualnih okolij. Ena najbolj vznemirljivih uporab generativne AI je na področju jezikovnih modelov.

## Kaj so majhni jezikovni modeli?

Majhni jezikovni model (SLM) predstavlja manjšo različico velikega jezikovnega modela (LLM), ki uporablja veliko arhitekturnih principov in tehnik LLM-jev, hkrati pa izkazuje bistveno zmanjšano računalniško zahtevnost.

SLM so podmnožica jezikovnih modelov, zasnovanih za generiranje besedil, ki so podobna človeškemu. V nasprotju z veliko večjimi različicami, kot je GPT-4, so SLM manjši in učinkovitejši, zaradi česar so idealni za aplikacije, kjer so računalniški viri omejeni. Kljub njihovi manjši velikosti lahko opravljajo različne naloge. Običajno so SLM zgrajeni z stiskanjem ali destilacijo LLM-jev, pri čemer je cilj ohraniti pomemben del funkcionalnosti in jezikovnih sposobnosti izvirnega modela. Ta zmanjšana velikost modela zmanjša kompleksnost, zaradi česar so SLM učinkovitejši tako glede porabe spomina kot računalniških zahtev. Kljub tem optimizacijam lahko SLM opravljajo širok nabor nalog obdelave naravnega jezika (NLP):

- Generiranje besedil: ustvarjanje koherentnih in kontekstualno ustreznih stavkov ali odstavkov.
- Dokončanje besedil: napovedovanje in dokončanje stavkov na podlagi danega izhodišča.
- Prevajanje: pretvarjanje besedila iz enega jezika v drugega.
- Povzemanje: krajšanje dolgih besedil v krajše, lažje prebavljive povzetke.

Čeprav z nekaterimi kompromisi v zmogljivosti ali globini razumevanja v primerjavi z večjimi modeli.

## Kako delujejo majhni jezikovni modeli?
SLM so trenirani na ogromnih količinah besedilnih podatkov. Med usposabljanjem se učijo vzorcev in struktur jezika, kar jim omogoča generiranje besedil, ki so tako slovnično pravilna kot kontekstualno primerna. Proces usposabljanja vključuje:

- Zbiranje podatkov: pridobivanje velikih zbirk besedil iz različnih virov.
- Predobdelava: čiščenje in organizacija podatkov, da so primerni za usposabljanje.
- Usposabljanje: uporaba algoritmov strojnega učenja za poučevanje modela razumevanja in generiranja besedila.
- Dopolnjevanje: prilagajanje modela za izboljšanje njegove zmogljivosti pri specifičnih nalogah.

Razvoj SLM je usklajen z naraščajočo potrebo po modelih, ki jih je mogoče uporabljati v okoljih z omejenimi viri, kot so mobilne naprave ali edge computig platforme, kjer so polni LLM-ji zaradi velikih zahtev po virih neprimerni. S poudarkom na učinkovitosti SLM uravnotežujejo zmogljivost z dostopnostjo, kar omogoča širšo uporabo na različnih področjih.

![slm](../../../translated_images/sl/slm.4058842744d0444a.webp)

## Cilji učenja

V tej lekciji želimo predstaviti znanje o SLM in ga povezati z Microsoft Phi-3 za učenje različnih scenarijev v besedilni vsebini, viziji in MoE.

Ob koncu te lekcije bi morali znati odgovoriti na naslednja vprašanja:

- Kaj je SLM?
- Kakšna je razlika med SLM in LLM?
- Kaj je družina Microsoft Phi-3/3.5?
- Kako izvajati inferenco z družino Microsoft Phi-3/3.5?

Pripravljeni? Začnimo.

## Razlike med velikimi jezikovnimi modeli (LLM) in majhnimi jezikovnimi modeli (SLM)

Tako LLM kot SLM temeljijo na osnovnih principih probabilističnega strojnega učenja, sledijo podobnim pristopom pri arhitekturni zasnovi, metodah usposabljanja, procesih generiranja podatkov in tehnikah ocenjevanja modelov. Vendar pa jih ločijo nekatere ključne dejavniki.

## Uporabe majhnih jezikovnih modelov

SLM imajo širok spekter uporab, med drugim:

- Klepetalniki: zagotavljanje podpore strankam in interakcija z uporabniki na pogovoren način.
- Ustvarjanje vsebin: pomoč pisateljem pri generiranju idej ali celo pisanju celotnih člankov.
- Izobraževanje: pomoč študentom pri pisnih nalogah ali učenju novih jezikov.
- Dostopnost: ustvarjanje orodij za osebe z invalidnostjo, npr. sistemi za pretvorbo besedila v govor.

**Velikost**
  
Glavna razlika med LLM in SLM je v obsegu modelov. LLM-ji, kot je ChatGPT (GPT-4), imajo ocenjenih približno 1,76 bilijona parametrov, medtem ko so odprtokodni SLM, kot je Mistral 7B, zasnovani z bistveno manj parametri – približno 7 milijard. To razliko povzročajo predvsem razlike v arhitekturi modelov in procesih usposabljanja. Na primer, ChatGPT uporablja mehanizem samopozornosti v okviru kodirnik-dekodirnik, medtem ko Mistral 7B uporablja pomikajočo se pozornost na oknu, kar omogoča učinkovitejše usposabljanje v modelu samo z dekodnikom. Ta arhitekturna razlika ima pomembne posledice za kompleksnost in zmogljivost modelov.

**Razumevanje**

SLM so običajno optimizirani za učinkovitost znotraj specifičnih področij, kar jih naredi zelo specializirane, a potencialno omejene v sposobnosti zagotavljanja širokega kontekstualnega razumevanja čez več področij znanja. Nasprotno pa LLM ciljajo na simulacijo inteligence na bolj celoviti ravni. Ker so usposobljeni na velikih in raznolikih podatkovnih zbirkah, so zasnovani za dobro delovanje v različnih domenah, kar jim omogoča večjo prilagodljivost in vsestranskost. Zaradi tega so LLM bolj primerni za širši nabor nalog, kot so obdelava naravnega jezika in programiranje.

**Računanje**

Usposabljanje in uporaba LLM sta procesa, ki zahtevata velike računalniške vire, pogosto velike GPU grozde. Na primer, usposabljanje modela, kot je ChatGPT od začetka, lahko zahteva na tisoče GPU-jev več tednov. V primerjavi s tem so SLM, zaradi manjšega števila parametrov, dostopnejši glede računalniških virov. Modele, kot je Mistral 7B, lahko usposabljamo in poganjamo na lokalnih računalnikih, opremljenih z zmerno zmogljivimi GPU-ji, čeprav usposabljanje še vedno zahteva več ur porazdeljenega dela na več GPU-jih.

**Pristranskost**

Pristranskost je znan problem pri LLM, predvsem zaradi narave usposabljajočih podatkov. Ti modeli pogosto temeljijo na surovih, javno dostopnih podatkih z interneta, ki lahko podzastopajo ali napačno predstavljajo določene skupine, uvajajo napačne oznake ali odražajo jezikovne pristranskosti, pogojene z dialekti, geografskimi razlikami in slovničnimi pravili. Poleg tega kompleksnost arhitekture LLM lahko nehote okrepi pristranskost, ki morda ostane neopažena brez skrbnega dopolnjevanja. Po drugi strani so SLM, ker so usposobljeni na bolj omejenih, področju specifičnih zbirkah podatkov, manj dovzetni za takšne pristranskosti, čeprav niso povsem imuni nanje.

**Inferenca**

Zmanjšana velikost SLM jim prinaša pomembno prednost v hitrosti inferenc, kar jim omogoča učinkovito generiranje izhodov na lokalni strojni opremi brez potrebe po obsežnem vzporednem procesiranju. V primerjavi s tem LLM zaradi svoje velikosti in kompleksnosti pogosto potrebujejo obsežne paralelne računalniške vire za dosego sprejemljivih časov inferenc. Prisotnost več sočasnih uporabnikov še dodatno upočasni odzivne čase LLM, še posebej pri obsežni razporeditvi.

Povzemimo, čeprav si LLM in SLM delita osnovo v strojnih učnih metodah, se bistveno razlikujejo v velikosti modela, zahtevah po virih, kontekstualnem razumevanju, dovzetnosti za pristranskost in hitrosti inferenc. Te razlike odražajo njihovo primernost za različne primere uporabe, pri čemer so LLM bolj vsestranski, a zahtevajo več virov, medtem ko SLM ponujajo učinkovitejše delovanje na specifičnih področjih z zmanjšanimi računalniškimi zahtevami.

***Opomba: V tej lekciji bomo SLM predstavili z uporabo Microsoft Phi-3 / 3.5 kot primera.***

## Predstavitev družine Phi-3 / Phi-3.5

Družina Phi-3 / 3.5 je namenjena predvsem tekstu, vidu in aplikacijam agenata (MoE):

### Phi-3 / 3.5 Instruct

Namenjena predvsem generiranju besedil, dokončanju pogovorov in izvlečku informacij iz vsebine itd.

**Phi-3-mini**

Jezikovni model s 3,8 milijardami parametrov je na voljo na Microsoft Foundry, Hugging Face in Ollama. Modeli Phi-3 bistveno presegajo jezikovne modele enake ali večje velikosti na ključnih merilih (glej številke meril spodaj, višje številke so boljše). Phi-3-mini presega modele, ki so dvakrat večji od njega, medtem ko Phi-3-small in Phi-3-medium presegata večje modele, vključno z GPT-3.5.

**Phi-3-small & medium**

S samo 7 milijardami parametrov Phi-3-small premaga GPT-3.5T na različnih merilih za jezik, sklepanje, kodiranje in matematiko.

Phi-3-medium s 14 milijardami parametrov nadaljuje to rast in presega Gemini 1.0 Pro.

**Phi-3.5-mini**

Lahko ga smatramo kot nadgradnjo Phi-3-mini. Medtem ko je število parametrov nespremenjeno, izboljšuje podporo za več jezikov (podpira več kot 20 jezikov: arabščino, kitajščino, češčino, danščino, nizozemščino, angleščino, finščino, francoščino, nemščino, hebrejščino, madžarščino, italijanščino, japonščino, korejščino, norveščino, poljščino, portugalščino, ruščino, španščino, švedščino, tajščino, turščino, ukrajinščino) in dodaja močnejšo podporo za dolg kontekst.

Phi-3.5-mini s 3,8 milijardami parametrov prekaša jezikovne modele iste velikosti in se primerja z modeli, ki so dvakrat večji.

### Phi-3 / 3.5 Vision

Model Instruct Phi-3/3.5 lahko razumemo kot Phi-jevo sposobnost razumevanja, Vision pa je tisto, kar Phi-ju daje "oči" za razumevanje sveta.


**Phi-3-Vision**

Phi-3-vision, s samo 4,2 milijardami parametrov, nadaljuje to rast in presega večje modele, kot sta Claude-3 Haiku in Gemini 1.0 Pro V v nalogah splošnega vizualnega sklepanje, OCR, ter razumevanju tabel in diagramov.


**Phi-3.5-Vision**

Phi-3.5-Vision je prav tako nadgradnja Phi-3-Vision, ki dodaja podporo za več slik. Lahko ga razumemo kot izboljšavo v viziji, saj omogoča gledanje ne samo slik, temveč tudi videov.

Phi-3.5-vision prekaša večje modele, kot so Claude-3.5 Sonnet in Gemini 1.5 Flash, na nalogah OCR, razumevanja tabel in grafikonov ter je primerljiv na nalogah splošnega vizualnega sklepanja. Podpira multiramčni vhod, torej sklepanje na več vhodnih slikah.


### Phi-3.5-MoE

***Mešanica strokovnjakov (MoE)*** omogoča modelom, da se predhodno usposabljajo z veliko manj računalniškega časa, kar pomeni, da lahko dramatično povečate velikost modela ali množico podatkov z enakim proračunom za računalniške vire kot pri gostem modelu. Posebej, MoE model bi moral doseči enako kakovost kot njegov gost model bistveno hitreje med predhodnim usposabljanjem.

Phi-3.5-MoE obsega 16 modulov po 3,8 milijarde parametrov. Phi-3.5-MoE z le 6,6 milijarde aktivnih parametrov doseže podoben nivo sklepanja, razumevanja jezika in matematike kot veliko večji modeli.

Model družine Phi-3/3.5 lahko uporabimo glede na različne scenarije. Za razliko od LLM lahko Phi-3/3.5-mini ali Phi-3/3.5-Vision namestite na edge naprave.


## Kako uporabljati modele družine Phi-3/3.5

Želimo uporabiti Phi-3/3.5 v različnih scenarijih. Naslednje bomo uporabili Phi-3/3.5 glede na različne scenarije.

![phi3](../../../translated_images/sl/phi3.655208c3186ae381.webp)

### Inferenca preko oblačnih API-jev

**Microsoft Foundry modeli**

> **Opomba:** GitHub Models se umika konec julija 2026. [Microsoft Foundry modeli](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) so neposredna zamenjava.

Microsoft Foundry modeli so najhitrejši način. Do modela Phi-3/3.5-Instruct lahko hitro dostopate prek kataloga modelov Foundry. V povezavi z Azure AI Inference SDK / OpenAI SDK lahko prek kode dostopate do API in opravite klic modela Phi-3/3.5-Instruct. Prav tako lahko preizkusite različne učinke preko Playground-a.

- Demo: primerjava učinkov Phi-3-mini in Phi-3.5-mini v kitajskih scenarijih

![phi3](../../../translated_images/sl/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/sl/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Če želite uporabiti tudi modele za vid in MoE, lahko za klice uporabite Microsoft Foundry. Če vas zanima, si lahko preberete Phi-3 Cookbook, da izveste, kako poklicati Phi-3/3.5 Instruct, Vision in MoE prek Microsoft Foundry [Kliknite ta povezavo](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Poleg oblačnega kataloga Microsoft Foundry Models lahko za dokončanje sorodnih klicev uporabite tudi [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst). Obiščete lahko NVIDIA NIM za dokončanje API klicev družine Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) je niz pospešenih mikrostoritev za inferenco, ki razvijalcem pomagajo učinkovito namestiti AI modele v različnih okoljih, vključno z oblači, podatkovnimi centri in delovnimi postajami.

Tukaj je nekaj ključnih lastnosti NVIDIA NIM:

- **Enostavnost namestitve:** NIM omogoča namestitev AI modelov z enim ukazom, zaradi česar je enostavno vključiti v obstoječe delovne procese.

- **Optimizirana zmogljivost:** Izkorišča NVIDIA-jeve vnaprej optimizirane pogone za sklepanje, kot sta TensorRT in TensorRT-LLM, da zagotovi nizko zakasnitev in visoko prepustnost.
- **Razširljivost:** NIM podpira samodejno skaliranje na Kubernetesu, kar omogoča učinkovito upravljanje spremenljivih obremenitev.
- **Varnost in nadzor:** Organizacije lahko ohranijo nadzor nad svojimi podatki in aplikacijami z gostovanjem NIM mikro storitev na lastni upravljani infrastrukturi.
- **Standardni API-ji:** NIM zagotavlja industrijske standardne API-je, ki olajšajo gradnjo in integracijo AI aplikacij, kot so klepetalni roboti, AI pomočniki in več.

NIM je del NVIDIA AI Enterprise, katerega cilj je poenostaviti uvajanje in operativnost AI modelov ter zagotoviti njihovo učinkovito delovanje na NVIDIA GPU-jih.

- Demo: Uporaba NVIDIA NIM za klic Phi-3.5-Vision-API  [[Kliknite to povezavo](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Zagon Phi-3/3.5 lokalno
Inferenca v zvezi s Phi-3, ali katerim koli jezikovnim modelom, kot je GPT-3, se nanaša na proces generiranja odgovorov ali napovedi na podlagi prejete vhodne informacije. Ko podate poziv ali vprašanje Phi-3, uporabi trenirano nevronsko mrežo za sklepanje o najbolj verjetnem in relevantnem odgovoru s analizo vzorcev in odnosov v podatkih, na katerih je bil usposobljen.

**Hugging Face Transformer**
Hugging Face Transformers je zmogljiva knjižnica zasnovana za obdelavo naravnega jezika (NLP) in druge naloge strojnega učenja. Tukaj je nekaj ključnih točk o njej:

1. **Vnaprej usposobljeni modeli**: Ponuja na tisoče vnaprej usposobljenih modelov, ki jih je mogoče uporabiti za različne naloge, kot so klasifikacija besedil, prepoznavanje imenovanih entitet, odgovarjanje na vprašanja, povzema, prevajanje in generiranje besedil.

2. **Interoperabilnost okvirov:** Knjižnica podpira več globokih učnih okvirov, vključno s PyTorch, TensorFlow in JAX. To omogoča usposabljanje modela v enem okviru in njegovo uporabo v drugem.

3. **Večmodalne zmogljivosti:** Poleg NLP podpira Hugging Face Transformers tudi naloge računalniškega vida (npr. klasifikacija slik, zaznavanje objektov) in obdelave zvoka (npr. prepoznavanje govora, klasifikacija zvoka).

4. **Enostavnost uporabe:** Knjižnica ponuja API-je in orodja za enostavno prenašanje in podrobno prilagajanje modelov, kar je dostopno tako za začetnike kot strokovnjake.

5. **Skupnost in viri:** Hugging Face ima živahno skupnost in obsežno dokumentacijo, vodiče ter lekcije, ki pomagajo uporabnikom začeti in kar najbolje izkoristiti knjižnico.
[uradna dokumentacija](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) ali njihov [GitHub repozitorij](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

To je najpogosteje uporabljena metoda, vendar zahteva tudi pospeševanje z GPU. Konec koncev scenariji, kot sta Vision in MoE, zahtevajo veliko računanja, ki bo na CPU zelo počasen, če niso kvantizirani.


- Demo: Uporaba Transformer za klic Phi-3.5-Instruct [Kliknite to povezavo](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Uporaba Transformer za klic Phi-3.5-Vision [Kliknite to povezavo](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Uporaba Transformer za klic Phi-3.5-MoE [Kliknite to povezavo](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) je platforma, zasnovana za lažji zagon velikih jezikovnih modelov (LLM) lokalno na vašem računalniku. Podpira različne modele, kot so Llama 3.1, Phi 3, Mistral in Gemma 2 med drugim. Platforma poenostavlja postopek tako, da združi teže modela, konfiguracijo in podatke v eno samo pakiranje, kar omogoča uporabnikom lažje prilagajanje in ustvarjanje lastnih modelov. Ollama je na voljo za macOS, Linux in Windows. Je odlično orodje, če želite eksperimentirati z LLM ali jih uvajati brez uporabe oblačnih storitev. Ollama je najpreprostejša pot, potrebujete samo zagnati naslednji ukaz.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) je Microsoftov offline, na napravi temelječ čas izvajanja za zagon modelov, kot je Phi, popolnoma na vaši lastni strojni opremi - brez naročnine na Azure, API ključa ali omrežne povezave. Samodejno izbere najboljšega izvajalnega ponudnika (NPU, GPU ali CPU) in zagotavlja OpenAI-združljivo končno točko, tako da lahko obstoječa koda `openai`/Azure AI Inference SDK kaže nanjo z minimalnimi spremembami. Za začetek si oglejte [Foundry Local dokumentacijo](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst).

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) je medplatformni pospeševalnik za sklepanje in usposabljanje modelov strojnega učenja. ONNX Runtime za Generativno AI (GENAI) je zmogljivo orodje, ki vam pomaga učinkovito poganjati generativne AI modele na različnih platformah.

## Kaj je ONNX Runtime?
ONNX Runtime je odprtokodni projekt, ki omogoča visoko zmogljivo sklepanje modelov strojnega učenja. Podpira modele v formatu Open Neural Network Exchange (ONNX), ki je standard za predstavitev modelov strojnega učenja. ONNX Runtime sklepanje lahko omogoči hitrejšo uporabniško izkušnjo in nižje stroške, podpira modele iz globokih učnih okvirov, kot so PyTorch in TensorFlow/Keras, pa tudi klasične knjižnice strojnega učenja, kot sta scikit-learn, LightGBM, XGBoost itd. ONNX Runtime je združljiv z različnimi strojno opremo, gonilniki in operacijskimi sistemi ter zagotavlja optimalno zmogljivost z izkoriščanjem strojnih pospeševalnikov kjer je mogoče skupaj z optimizacijami in transformacijami grafov.

## Kaj je Generativna AI?
Generativna AI se nanaša na AI sisteme, ki lahko ustvarjajo novo vsebino, kot so besedila, slike ali glasba, na podlagi podatkov, na katerih so bili usposobljeni. Primeri vključujejo jezikovne modele, kot je GPT-3, in modele za generiranje slik, kot je Stable Diffusion. Knjižnica ONNX Runtime za GenAI zagotavlja generativno AI zanko za ONNX modele, vključno z izvajanjem z ONNX Runtime, procesiranjem logitov, iskanjem in vzorčenjem ter upravljanjem KV predpomnilnika.

## ONNX Runtime za GENAI
ONNX Runtime za GENAI širi zmožnosti ONNX Runtime za podporo generativnim AI modelom. Tukaj je nekaj ključnih lastnosti:

- **Široka podpora platformam:** Deluje na različnih platformah, vključno z Windows, Linux, macOS, Android in iOS.
- **Podpora modelom:** Podpira številne priljubljene generativne AI modele, kot so LLaMA, GPT-Neo, BLOOM in drugi.
- **Optimizacija zmogljivosti:** Vključuje optimizacije za različne strojne pospeševalce, kot so NVIDIA GPU-ji, AMD GPU-ji in drugi.
- **Enostavnost uporabe:** Ponuja API-je za enostavno integracijo v aplikacije, kar omogoča generiranje besedil, slik in druge vsebine z minimalno količino kode.
- Uporabniki lahko kličejo visoko raven metodo generate(), ali pa zaženete vsako iteracijo modela v zanki, generirajoč en žeton naenkrat in po želji posodabljajo parametre generiranja znotraj zanke.
- ONNX runtime prav tako podpira požrešno/beam iskanje in TopP, TopK vzorčenje za generiranje zaporedij žetonov ter vgrajeno procesiranje logitov, kot so kazni za ponavljanje. Prav tako lahko enostavno dodate lastno ocenjevanje.

## Začetek
Za začetek z ONNX Runtime za GENAI lahko sledite tem korakom:

### Namestite ONNX Runtime:
```Python
pip install onnxruntime
```
### Namestite razširitve za generativno AI:
```Python
pip install onnxruntime-genai
```

### Zaženite model: Tukaj je enostaven primer v Pythonu:
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

Poleg ONNX Runtime, Ollama in Foundry Local referenčnih metod, lahko dokončamo tudi referenco kvantitativnih modelov na podlagi referenčnih metod modelov, ki jih ponujajo različni proizvajalci. Na primer Apple MLX okvir z Apple Metal, Qualcomm QNN z NPU, Intel OpenVINO s CPU/GPU itd. Več vsebine lahko dobite tudi iz [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Več

Naučili smo se osnov družine Phi-3/3.5, vendar za večje poznavanje SLM potrebujemo več znanja. Odgovore lahko najdete v Phi-3 Cookbook. Če želite izvedeti več, obiščite [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->