# Uvod v majhne jezikovne modele za generativno AI za začetnike
Generativna AI je fascinantno področje umetne inteligence, ki se osredotoča na ustvarjanje sistemov, ki lahko generirajo novo vsebino. Ta vsebina lahko zajema besedilo, slike, glasbo in celo celotna virtualna okolja. Ena najvznemirljivejših uporab generativne AI je na področju jezikovnih modelov.

## Kaj so majhni jezikovni modeli?

Majhen jezikovni model (SLM) predstavlja zmanjšano različico velikega jezikovnega modela (LLM), ki uporablja mnoge arhitekturne principe in tehnike LLM-jev, hkrati pa ima znatno manjšo računsko obremenitev.

SLM so podskupina jezikovnih modelov, zasnovanih za generiranje besedila, ki je podobno človeškemu. Za razliko od večjih modelov, kot je GPT-4, so SLM kompaktnejši in učinkovitejši, zaradi česar so idealni za aplikacije, kjer so računski viri omejeni. Kljub manjši velikosti lahko opravljajo različne naloge. Običajno so SLM zgrajeni s stiskanjem ali destilacijo LLM-jev, pri čemer cilj ostaja ohraniti znaten del izvirne funkcionalnosti in jezikovnih sposobnosti modela. Ta zmanjšana velikost modela zmanjšuje splošno kompleksnost, kar naredi SLM bolj učinkovite glede porabe pomnilnika in računalniških zahtev. Kljub tem optimizacijam lahko SLM še vedno opravljajo širok nabor nalog obdelave naravnega jezika (NLP):

- Generiranje besedila: ustvarjanje smiselnih in kontekstualno relevantnih stavkov ali odstavkov.
- Dokončanje besedila: napovedovanje in dokončevanje stavkov na podlagi podanega povzetka.
- Prevajanje: pretvorba besedila iz enega jezika v drugega.
- Povzemanje: strnitev dolgih besedil v krajše, bolj prebavljive povzetke.

Čeprav z nekaterimi kompromisi v zmogljivosti ali globini razumevanja v primerjavi z večjimi kolegi.

## Kako delujejo majhni jezikovni modeli?
SLM so usposobljeni na velikih količinah besedilnih podatkov. Med usposabljanjem se naučijo vzorcev in struktur jezika, kar jim omogoča generiranje besedila, ki je tako slovnično pravilno kot kontekstualno ustrezno. Proces usposabljanja vključuje:

- Zbiranje podatkov: pridobivanje velikih zbirk besedil iz različnih virov.
- Predobdelava: čiščenje in organizacija podatkov, da so primerni za usposabljanje.
- Usposabljanje: uporaba algoritmov strojnega učenja za učenje razumevanja in generiranja besedila.
- Fino prilagajanje: nastavitev modela za izboljšanje zmogljivosti pri specifičnih nalogah.

Razvoj SLM sovpada z naraščajočo potrebo po modelih, ki jih je mogoče izvajati v okoljih z omejenimi viri, kot so mobilne naprave ali računalništvo na robu, kjer so lahko polni LLM nepraktični zaradi zahtev po velikih virih. Osredotočenost na učinkovitost omogoča SLM-jem ravnovesje med zmogljivostjo in dostopnostjo, kar omogoča širšo uporabo na različnih področjih.

![slm](../../../translated_images/sl/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Cilji učenja

V tej lekciji želimo predstaviti znanje o SLM in ga kombinirati z Microsoft Phi-3, da se naučimo različnih scenarijev na področju besedilne vsebine, vida in MoE.

Do konca te lekcije bi morali znati odgovoriti na naslednja vprašanja:

- Kaj je SLM?
- Kakšna je razlika med SLM in LLM?
- Kaj je Microsoft Phi-3/3.5 družina?
- Kako izvajati sklepanje z Microsoft Phi-3/3.5 družino?

Ste pripravljeni? Začnimo.

## Razlike med velikimi jezikovnimi modeli (LLM) in majhnimi jezikovnimi modeli (SLM)

Tako LLM kot SLM temeljijo na osnovnih principih verjetnostnega strojnega učenja, sledijo podobnim pristopom v arhitekturni zasnovi, metodologijah usposabljanja, procesih generiranja podatkov in tehnikah ocenjevanja modelov. Vendar pa jih loči več ključnih dejavnikov.

## Uporabe majhnih jezikovnih modelov

SLM imajo širok nabor uporab, vključno z:

- Čatboti: zagotavljanje podpore strankam in interakcija z uporabniki na pogovoren način.
- Ustvarjanje vsebin: pomoč pisateljem z idejami ali celo osnutki celotnih člankov.
- Izobraževanje: pomoč študentom pri pisnih nalogah ali učenju novih jezikov.
- Dostopnost: ustvarjanje orodij za osebe z invalidnostjo, na primer sistemi za pretvorbo besedila v govor.

**Velikost**
  
Osnovna razlika med LLM in SLM je v velikosti modelov. LLM, kot je ChatGPT (GPT-4), lahko vsebuje ocenjenih 1,76 bilijona parametrov, medtem ko so odprtokodni SLM, kot je Mistral 7B, zasnovani z bistveno manj parametri — okoli 7 milijard. Ta razlika izhaja predvsem iz različnih arhitektur in procesov usposabljanja. Na primer, ChatGPT uporablja mehanizem samo-pazljivosti znotraj okvirja kodirnik-dekodirnik, medtem ko Mistral 7B uporablja pozornost s pomičnim oknom, ki omogoča učinkovitejše usposabljanje znotraj dekoderskega modela. Ta arhitekturna razlika ima pomemben vpliv na kompleksnost in zmogljivost teh modelov.

**Razumevanje**

SLM so običajno optimizirani za delovanje znotraj specifičnih področij, zaradi česar so zelo specializirani, a lahko omejeni pri zagotavljanju širokega kontekstualnega razumevanja v več različnih področjih znanja. Nasprotno pa LLM ciljajo na simulacijo človeške inteligence na bolj celostni ravni. Usposobljeni na obsežnih, raznolikih zbirkah podatkov, so LLM zasnovani za dobro delovanje v različnih domenah, kar jim zagotavlja večjo prilagodljivost in vsestranskost. Posledično so LLM primernejši za širši nabor nadaljnjih nalog, kot so obdelava naravnega jezika in programiranje.

**Računalniška zmogljivost**

Usposabljanje in uvajanje LLM-jev sta procesi, ki zahtevata velike računalniške vire, pogosto vključujejo obsežne GPU gruče. Na primer, usposabljanje modela, kot je ChatGPT iz nič, lahko zahteva tisoče GPU-jev skozi dolga obdobja. Nasprotno, SLM, z manjšim številom parametrov, so bolj dostopni glede računalniških virov. Modeli, kot je Mistral 7B, se lahko usposobijo in izvajajo na lokalnih napravah z zmerno GPU opremo, čeprav usposabljanje še vedno zahteva več ur na več GPU-jih.

**Pristranskost**

Pristranskost je znan problem pri LLM, predvsem zaradi narave podatkov za usposabljanje. Ti modeli pogosto temeljijo na surovih, odprto dostopnih podatkih z interneta, ki lahko premalo ali napačno predstavljajo nekatere skupine, uvajajo napačne oznake ali odražajo jezikovne pristranskosti, ki jih vplivajo dialekti, geografske različice in slovnična pravila. Poleg tega lahko zapletenost arhitektur LLM nenamerno povečuje pristranskost, kar lahko ostane neopaženo brez skrbnega fino nastavitev. Po drugi strani pa so SLM, ki so usposobljeni na bolj omejenih, domeno-specifičnih zbirkah podatkov, inherentno manj dovzetni za takšne pristranskosti, čeprav niso popolnoma imuni nanje.

**Sklepanje**

Zmanjšana velikost SLM jim daje pomembno prednost v hitrosti sklepanja, kar jim omogoča učinkovito generiranje izhodov na lokalni strojni opremi brez potrebe po obsežnem vzporednem računanju. Nasprotno pa LLM zaradi svoje velikosti in kompleksnosti pogosto zahtevajo znatne vzporedne računske vire za dosego sprejemljivih časov sklepanja. Prisotnost več sočasnih uporabnikov še dodatno upočasni odzivne čase LLM, še zlasti pri razširjeni uporabi.

Povzamemo lahko, da čeprav imata LLM in SLM skupno osnovo v strojni učenju, se pomembno razlikujeta glede velikosti modela, potrebnih virov, kontekstualnega razumevanja, dovzetnosti za pristranskosti in hitrosti sklepanja. Te razlike odražajo njihovo ustreznost za različne primere uporabe, pri čemer so LLM bolj vsestranski, a zahtevajo več virov, SLM pa nudijo specifično učinkovitost v domenah z zmanjšanimi računalniškimi zahtevami.

***Opomba: V tej lekciji bomo SLM predstavili z uporabo Microsoft Phi-3 / 3.5 kot primera.***

## Predstavitev družine Phi-3 / Phi-3.5

Družina Phi-3 / 3.5 je namenjena predvsem scenarijem uporabe za besedilo, vid in agente (MoE):

### Phi-3 / 3.5 Instruct

Glavno za generiranje besedila, dokončanje pogovora in ekstrakcijo vsebinskih informacij itd.

**Phi-3-mini**

3,8 milijardni jezikovni model je na voljo na Microsoft Foundry, Hugging Face in Ollama. Phi-3 modeli bistveno presegajo jezikovne modele enake in večje velikosti na ključnih merilih (glej spodnje številke meril, višje številke so boljše). Phi-3-mini presega modele, ki so dvakrat večji, medtem ko Phi-3-small in Phi-3-medium presegata večje modele, vključno z GPT-3.5.

**Phi-3-small & medium**

S samo 7 milijardami parametrov Phi-3-small premaga GPT-3.5T na različnih jezikovnih, razlagalnih, kodirnih in matematičnih merilih.

Phi-3-medium s 14 milijardami parametrov nadaljuje ta trend in premaga Gemini 1.0 Pro.

**Phi-3.5-mini**

Lahko ga razumemo kot nadgradnjo Phi-3-mini. Čeprav parametri ostajajo nespremenjeni, izboljša sposobnost podpore več jezikov (podpora 20+ jezikom: arabščina, kitajščina, češčina, danščina, nizozemščina, angleščina, finščina, francoščina, nemščina, hebrejščina, madžarščina, italijanščina, japonščina, korejščina, norveščina, poljščina, portugalščina, ruščina, španščina, švedščina, tajščina, turščina, ukrajinščina) in dodaja močnejšo podporo za dolgi kontekst.

Phi-3.5-mini s 3,8 milijardami parametrov presega jezikovne modele enake velikosti in je primerljiv z modeli, ki so dvakrat večji.

### Phi-3 / 3.5 Vision

Instruct model Phi-3/3.5 lahko razumemo kot Phi-jevo sposobnost razumevanja, Vision pa mu daje oči za razumevanje sveta.


**Phi-3-Vision**

Phi-3-vision, z le 4,2 milijarde parametrov, nadaljuje ta trend in presega večje modele, kot so Claude-3 Haiku in Gemini 1.0 Pro V, pri splošnih nalogah vizualnega sklepanja, OCR-ju ter razumevanju tabel in diagramov.


**Phi-3.5-Vision**

Phi-3.5-Vision je tudi nadgradnja Phi-3-Vision, ki dodaja podporo za več slik. Lahko ga obravnavamo kot izboljšanje vida, saj ne vidite le slik, temveč tudi videoposnetke.

Phi-3.5-vision presega večje modele, kot sta Claude-3.5 Sonnet in Gemini 1.5 Flash v OCR-ju, razumevanju tabel in grafikonov ter je primerljiv pri splošnih nalogah vizualnega sklepanja. Podpira večokvirni vhod, torej sklepa na več vhodnih slikah.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** omogoča modelom predhodno usposabljanje z veliko manj računalniških sredstev, kar pomeni, da lahko drastično povečate velikost modela ali zbirko podatkov z enakim proračunom za računanje kot gost model. Še posebej naj bi MoE model med predhodnim usposabljanjem dosegel enako kakovost kot gost model veliko hitreje.

Phi-3.5-MoE vključuje 16 x 3,8 milijard ekspertnih modulov. Phi-3.5-MoE z le 6,6 milijarde aktivnih parametrov dosega raven razumevanja, jezikovnega razumevanja in matematike, primerljivo z veliko večjimi modeli.

Phi-3/3.5 družinski modeli se lahko uporabljajo glede na različne scenarije. Za razliko od LLM lahko Phi-3/3.5-mini ali Phi-3/3.5-Vision namestite na robne naprave.


## Kako uporabljati modele družine Phi-3/3.5

Želimo uporabljati Phi-3/3.5 v različnih scenarijih. Naslednje bomo uporabili Phi-3/3.5 glede na različne scenarije.

![phi3](../../../translated_images/sl/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Sklepanje preko oblačnih API-jev

**Microsoft Foundry modeli**

> **Opomba:** GitHub Models se bo upokojil konec julija 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) je neposredna zamenjava.

Microsoft Foundry modeli so najhitrejša pot. Hitro lahko dostopate do Phi-3/3.5-Instruct modela prek kataloga Foundry modelov. V kombinaciji z Azure AI Inference SDK / OpenAI SDK lahko dostopate do API-ja prek kode za izvedbo Phi-3/3.5-Instruct klica. Prav tako lahko preizkusite različne učinke preko Playground-a.

- Demo: primerjava učinkov Phi-3-mini in Phi-3.5-mini v kitajskih scenarijih

![phi3](../../../translated_images/sl/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/sl/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Ali pa, če želite uporabiti vision in MoE modele, lahko uporabite Microsoft Foundry za izvedbo klica. Če vas zanima, preberite Phi-3 Cookbook za navodila, kako klicati Phi-3/3.5 Instruct, Vision, MoE prek Microsoft Foundry [Kliknite ta povezavo](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Poleg oblačnega kataloga Microsoft Foundry Models lahko za izvajanje povezanih klicev uporabite tudi [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst). Obiščete lahko NVIDIA NIM za izvedbo API klicev družine Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) je niz pospešenih mikrostoritev za sklepanje, namenjenih olajšanju učinkovitih uvajanj AI modelov v različnih okoljih, vključno z oblaki, podatkovnimi centri in delovnimi postajami.

Tukaj so nekatere ključne značilnosti NVIDIA NIM:

- **Enostavnost uvajanja:** NIM omogoča uvajanje AI modelov z enim ukazom, kar olajša integracijo v obstoječe delovne tokove.
- **Optimizirana zmogljivost:** Izkorišča vnaprej optimizirane sklepalne motorje NVIDIA, kot sta TensorRT in TensorRT-LLM, za zagotovitev nizkih zamud in visoke prepustnosti.
- **Razširljivost:** NIM podpira avtomatsko skaliranje na Kubernetes-u, kar mu omogoča učinkovito obvladovanje različnih obremenitev.
- **Varnost in nadzor:** Organizacije lahko ohranijo nadzor nad svojimi podatki in aplikacijami z samostojnim gostovanjem NIM mikrostoritev na lastni upravljani infrastrukturi.
- **Standardni API-ji:** NIM zagotavlja industrijske standardne API-je, ki olajšajo izdelavo in integracijo AI aplikacij, kot so chatbot-i, AI asistenti in druge.

NIM je del NVIDIA AI Enterprise, katerega cilj je poenostaviti uvajanje in operativnost AI modelov ter zagotoviti, da učinkovito delujejo na NVIDIA GPU-jih.

- Demo: Uporaba NVIDIA NIM za klic Phi-3.5-Vision-API [[Kliknite na to povezavo](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Zagon Phi-3/3.5 lokalno
Inferenca v povezavi s Phi-3 ali katerimkoli jezikovnim modelom, kot je GPT-3, pomeni postopek generiranja odzivov ali napovedi na podlagi prejetega vhodnega podatka. Ko Phi-3 zagotovite poziv ali vprašanje, uporabi svoj naučeni nevronski model, da poda najbolj verjeten in relevanten odgovor tako, da analizira vzorce in odnose v podatkih, na katerih je bil treniran.

**Hugging Face Transformer**
Hugging Face Transformers je zmogljiva knjižnica, zasnovana za obdelavo naravnega jezika (NLP) in druge naloge strojnemu učenju. Tukaj je nekaj ključnih točk o njej:

1. **Prednaučeni modeli**: Ponuja tisoče prednaučenih modelov, ki jih lahko uporabite za različne naloge, kot so klasifikacija besedila, prepoznavanje imenovanih entitet, odgovarjanje na vprašanja, povzemanje, prevajanje in generiranje besedila.

2. **Medsebojna združljivost okvirov**: Knjižnica podpira več globokih učnih okvirov, vključno s PyTorch, TensorFlow in JAX. To vam omogoča, da na enem okviru trenirate model in ga uporabite v drugem.

3. **Večmodalne zmožnosti**: Poleg NLP, Hugging Face Transformers podpira tudi naloge računalniškega vida (npr. klasifikacija slik, zaznavanje predmetov) in obdelavo zvoka (npr. prepoznavanje govora, klasifikacija zvoka).

4. **Enostavnost uporabe**: Knjižnica ponuja API-je in orodja za enostavno prenašanje in prilagajanje modelov, kar je dostopno tako začetnikom kot strokovnjakom.

5. **Skupnost in viri**: Hugging Face ima aktivno skupnost ter obsežno dokumentacijo, tutorijale in vodiče, ki uporabnikom pomagajo začeti in kar najbolje izkoristiti knjižnico.
[uradna dokumentacija](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) ali njihov [GitHub repozitorij](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

To je najpogosteje uporabljena metoda, vendar zahteva tudi GPU pospeševanje. Scenariji, kot so Vision in MoE, namreč zahtevajo veliko izračunov, ki bodo na CPU-ju zelo počasni, če niso kvantizirani.


- Demo: Uporaba Transformerja za klic Phi-3.5-Instruct [Kliknite na to povezavo](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Uporaba Transformerja za klic Phi-3.5-Vision [Kliknite na to povezavo](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Uporaba Transformerja za klic Phi-3.5-MoE [Kliknite na to povezavo](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) je platforma, zasnovana za lažji zagon velikih jezikovnih modelov (LLM) lokalno na vašem računalniku. Podpira različne modele, kot so Llama 3.1, Phi 3, Mistral in Gemma 2, med ostalimi. Platforma poenostavi postopek z združevanjem teže modela, konfiguracije in podatkov v en paket, kar uporabnikom omogoča lažje prilagajanje in ustvarjanje lastnih modelov. Ollama je na voljo za macOS, Linux in Windows. To je odlično orodje, če želite eksperimentirati z LLM-ji ali jih uvajati brez odvisnosti od oblaka. Ollama je najhitrejša pot, potrebno je le zagnati naslednji ukaz.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) je Microsoftovo offline, lokalno izvajalno okolje za modele, kot je Phi, ki deluje popolnoma na vaši strojni opremi – ni potrebna naročnina na Azure, API ključ ali internetna povezava. Samodejno izbere najboljšega razpoložljivega izvajalca (NPU, GPU ali CPU) in razkrije OpenAI združljivo končno točko, tako da lahko obstoječa koda za `openai`/Azure AI Inference SDK usmeri na to z minimalnimi spremembami. Za začetek si oglejte [Foundry Local dokumentacijo](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst).

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) je vzporedni pogon za inferenco in treniranje strojnega učenja. ONNX Runtime za Generativno AI (GENAI) je zmogljivo orodje, ki vam pomaga zagnati generativne AI modele učinkovito na različnih platformah.

## Kaj je ONNX Runtime?
ONNX Runtime je odprtokodni projekt, ki omogoča visokozmogljivo inferenco modelov strojnemu učenju. Podpira modele v formatu Open Neural Network Exchange (ONNX), ki je standard za predstavitev modelov strojnemu učenju. ONNX Runtime inferenca omogoča hitrejše uporabniške izkušnje in nižje stroške, podpira modele iz globokih učnih ogrodij, kot so PyTorch in TensorFlow/Keras, kot tudi klasične knjižnice strojnemu učenju, kot so scikit-learn, LightGBM, XGBoost itd. ONNX Runtime je združljiv z različnimi strojno programsko opremo, gonilniki in operacijskimi sistemi ter zagotavlja optimalno zmogljivost z uporabo strojnih pospeševalnikov, če so na voljo, skupaj z optimizacijami in pretvorbami grafov.

## Kaj je Generativna AI?
Generativna AI označuje AI sisteme, ki lahko generirajo novo vsebino, kot so besedilo, slike ali glasba, na podlagi podatkov, na katerih so bili trenirani. Primeri so jezikovni modeli, kot je GPT-3, in modeli za generiranje slik, kot je Stable Diffusion. Knjižnica ONNX Runtime za GenAI zagotavlja generativni AI cikel za ONNX modele, vključno z inferenco z ONNX Runtime, obdelavo logitov, iskanjem in vzorčenjem ter upravljanjem predpomnilnika KV.

## ONNX Runtime za GENAI
ONNX Runtime za GENAI razširja zmogljivosti ONNX Runtime z podporo generativnim AI modelom. Tukaj so nekatere ključne lastnosti:

- **Široka podpora platformam:** Deluje na različnih platformah, vključno z Windows, Linux, macOS, Android in iOS.
- **Podpora modelom:** Podpira številne priljubljene generativne AI modele, kot so LLaMA, GPT-Neo, BLOOM in drugi.
- **Optimizacija zmogljivosti:** Vključuje optimizacije za različne strojne pospeševalnike, kot so NVIDIA GPU-ji, AMD GPU-ji in drugi2.
- **Enostavnost uporabe:** Ponuja API-je za enostavno integracijo v aplikacije, ki omogočajo generiranje besedila, slik in druge vsebine z minimalno kodo.
- Uporabniki lahko kličejo visoko raven metode generate(), ali pa izvajajo vsako iteracijo modela v zanki, pri čemer generirajo eno samo enoto naenkrat in po želji posodabljajo parametre generiranja znotraj zanke.
- ONNX runtime prav tako podpira greedy/beam search in TopP, TopK vzorčenje za generiranje zaporedij enot ter vgrajeno obdelavo logitov, kot so kazni za ponavljanje. Prav tako lahko enostavno dodate lastno ocenjevanje.

## Začetek
Za začetek z ONNX Runtime za GENAI lahko sledite tem korakom:

### Namestite ONNX Runtime:
```Python
pip install onnxruntime
```
### Namestite razširitve generativne AI:
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

Poleg referenčnih metod ONNX Runtime, Ollama in Foundry Local lahko dopolnimo tudi reference kvantitativnih modelov na osnovi metod, ki jih nudijo različni proizvajalci. Na primer Apple MLX okvir z Apple Metal, Qualcomm QNN z NPU, Intel OpenVINO z CPU/GPU itd. Več vsebine lahko pridobite tudi v [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).


## Več

Osvojili smo osnove družine Phi-3/3.5, vendar za več znanja o SLM potrebujemo dodatne informacije. Odgovore najdete v Phi-3 Cookbook. Če želite izvedeti več, obiščite [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->