# Uvod v Majhne Jezikovne Modele za Generativno AI za Začetnike
Generativna AI je fascinantno področje umetne inteligence, ki se osredotoča na ustvarjanje sistemov, sposobnih generiranja nove vsebine. Ta vsebina lahko segajo od besedila in slik do glasbe in celo celotnih virtualnih okolij. Ena najbolj vznemirljivih uporab generativne AI je na področju jezikovnih modelov.

## Kaj so Majhni Jezikovni Modeli?

Majhen Jezikovni Model (SLM) predstavlja zmanjšano različico velikega jezikovnega modela (LLM), ki uporablja veliko arhitekturnih principov in tehnik LLM-jev, pri čemer ima bistveno manjšo računsko zahtevnost.

SLM-ji so podskupina jezikovnih modelov, zasnovanih za generiranje besedila, ki je podobno človeškemu. Za razliko od njihovih večjih različic, kot je GPT-4, so SLM-ji bolj kompaktni in učinkoviti, zato so idealni za aplikacije, kjer so računski viri omejeni. Kljub manjšim dimenzijam lahko še vedno opravljajo različne naloge. Običajno so SLM-ji ustvarjeni z zgoščevanjem ali destilacijo LLM-jev, s ciljem ohraniti znaten del funkcionalnosti in jezikovnih sposobnosti izvirnega modela. Ta zmanjšana velikost modela zmanjša splošno kompleksnost, zaradi česar so SLM-ji učinkovitejši tako glede uporabe pomnilnika kot računske zahtevnosti. Kljub tem optimizacijam lahko SLM-ji še vedno izvajajo širok nabor nalog obdelave naravnega jezika (NLP):

- Generiranje besedila: ustvarjanje koherentnih in kontekstualno ustreznih stavkov ali odstavkov.
- Dopolnjevanje besedila: napovedovanje in dopolnjevanje stavkov na podlagi podanega poziva.
- Prevajanje: pretvarjanje besedila iz enega jezika v drugega.
- Povzemanje: skrajševanje daljših besedil v krajše, lažje prebavljive povzetke.

Čeprav z nekaterimi kompromisi glede zmogljivosti ali globine razumevanja v primerjavi z njihovimi večjimi različicami.

## Kako Delujejo Majhni Jezikovni Modeli?
SLM-ji se učijo na velikih količinah besedilnih podatkov. Med učenjem spoznavajo vzorce in strukture jezika, kar jim omogoča generiranje besedila, ki je tako slovnično pravilno kot kontekstualno primerno. Postopek učenja vključuje:

- Zbiranje podatkov: pridobivanje velikih zbirk besedila iz različnih virov.
- Predprocesiranje: čiščenje in organizacija podatkov, da so primerni za učenje.
- Učenje: uporaba algoritmov strojnega učenja za učenje modela, kako razumeti in generirati besedilo.
- Izpopolnjevanje: prilagajanje modela za izboljšanje njegove uspešnosti pri specifičnih nalogah.

Razvoj SLM-jev sovpada z naraščajočo potrebo po modelih, ki jih je mogoče namestiti v okolja z omejenimi viri, kot so mobilne naprave ali obrobni računalniški sistemi, kjer so polni LLM-ji pogosto nepraktični zaradi težkih zahtev po virih. S poudarkom na učinkovitosti SLM-ji uravnovešajo zmogljivost in dostopnost, kar omogoča širšo uporabo v različnih domenah.

![slm](../../../translated_images/sl/slm.4058842744d0444a.webp)

## Cilji učenja

V tej lekciji želimo predstaviti znanje o SLM-jih in ga združiti z Microsoft Phi-3 za učenje različnih scenarijev v besedilni vsebini, viziji in MoE.

Ob koncu te lekcije boste morali znati odgovoriti na naslednja vprašanja:

- Kaj je SLM?
- Kakšna je razlika med SLM in LLM?
- Kaj je družina Microsoft Phi-3/3.5?
- Kako izvesti inferenco z družino Microsoft Phi-3/3.5?

Ste pripravljeni? Začnimo.

## Razlike med Velikimi Jezikovnimi Modeli (LLM) in Majhnimi Jezikovnimi Modeli (SLM)

Tako LLM-ji kot SLM-ji temeljijo na osnovnih principih verjetnostnega strojnega učenja, sledijo podobnim pristopom v arhitekturni zasnovi, metodologijah učenja, procesih generiranja podatkov in tehnikah ocenjevanja modelov. Vendar pa jih nekaj ključnih dejavnikov ločuje.

## Uporabe Majhnih Jezikovnih Modelov

SLM-ji imajo širok nabor uporab, vključno z:

- Klepetalni roboti: zagotavljanje podpore strankam in interakcija z uporabniki na pogovorni način.
- Ustvarjanje vsebin: pomoč pisateljem pri generiranju idej ali celo pripravi celotnih člankov.
- Izobraževanje: pomoč študentom pri pisnih nalogah ali učenju novih jezikov.
- Dostopnost: ustvarjanje orodij za osebe z invalidnostjo, na primer sistemi za pretvorbo besedila v govor.

**Velikost**
  
Glavna razlika med LLM in SLM je v obsegu modelov. LLM-ji, kot je ChatGPT (GPT-4), lahko vsebujejo ocenjenih 1,76 bilijona parametrov, medtem ko so odprtokodni SLM-ji, kot je Mistral 7B, zasnovani z bistveno manjšim številom parametrov – približno 7 milijard. Ta razlika izvira predvsem iz razlik v arhitekturi modela in procesih učenja. Na primer, ChatGPT uporablja mehanizem samopozornosti v okvirju kodirnik-dekodirnik, medtem ko Mistral 7B uporablja pozornost s drsno okno, kar omogoča učinkovitejše učenje znotraj modela samo-dekodirnika. Ta arhitekturna razlika ima globoke posledice za kompleksnost in uspešnost teh modelov.

**Razumevanje**

SLM-ji so običajno optimizirani za delovanje v specifičnih domenah, zaradi česar so zelo specializirani, a lahko omejeni v sposobnosti zagotavljanja širšega kontekstualnega razumevanja čez več področij znanja. Nasprotno pa LLM-ji ciljajo na simulacijo človeškega razmišljanja na bolj celoviti ravni. Izurjeni na velikih in raznolikih zbirkah podatkov, so LLM-ji zasnovani za uspešno delovanje v različnih domenah, kar ponuja večjo vsestranskost in prilagodljivost. Posledično so LLM-ji bolj primerni za širši spekter nadaljnjih nalog, kot so obdelava naravnega jezika in programiranje.

**Računalniški viri**

Učenje in uvajanje LLM-jev sta procesa, ki zahtevata veliko virov, pogosto pa obsega velikanske računalniške infrastrukture, vključujoč velike gruče GPU-jev. Na primer, učenje modela, kot je ChatGPT, od začetka lahko zahteva tisoče GPU-jev skozi dolga obdobja. Nasprotno so SLM-ji, z manjšim številom parametrov, bolj dostopni glede računalniških sredstev. Modelle, kot je Mistral 7B, je mogoče usposobiti in zagnati na lokalnih računalnikih z zmerno opremo GPU, čeprav učenje še vedno zahteva nekaj ur na več GPU-jih.

**Pristranskost**

Pristranskost je znan problem pri LLM-jih, predvsem zaradi narave učnih podatkov. Ti modeli pogosto temeljijo na surovih, odprto dostopnih podatkih z interneta, ki lahko premalo ali napačno predstavljajo določene skupine, uvajajo napačno oznake ali odražajo jezikovne pristranskosti zaradi dialekta, geografskih razlik in slovničnih pravil. Poleg tega kompleksnost arhitektur LLM-jev lahko nehote poslabša pristranskost, ki ostane neopažena brez skrbnega izpopolnjevanja. Po drugi strani pa so SLM-ji, usposobljeni na bolj omejenih in domen-specifičnih zbirkah podatkov, manj dovzetni za takšne pristranskosti, čeprav niso imuni.

**Inferenca**

Manjša velikost SLM-jev jim daje pomembno prednost pri hitrosti inferenc, kar jim omogoča učinkovito generiranje izhodov na lokalni strojni opremi, brez potrebe po obsežnem vzporednem procesiranju. Nasprotno pa LLM-ji zaradi svoje velikosti in kompleksnosti pogosto zahtevajo obsežne vzporedne računske vire za dosego sprejemljivih časov inferenc. Prisotnost številnih hkratnih uporabnikov dodatno upočasnjuje odzivne čase LLM-jev, predvsem pri obširni uporabi.

Povzemimo, da kljub skupnim temeljem v strojnem učenju, se LLM in SLM zelo razlikujeta po velikosti modela, zahtevah po virih, kontekstualnem razumevanju, dovzetnosti za pristranskost in hitrosti inferenc. Te razlike odražajo njihovo primernost za različne primere uporabe, pri čemer so LLM-ji bolj vsestranski, a tudi zahtevnejši za vire, SLM-ji pa nudijo večjo učinkovitost v specifičnih domenah z manjšimi računalniškimi zahtevami.

***Opomba: V tej lekciji bomo za predstavitev SLM uporabili Microsoft Phi-3 / 3.5 kot primer.***

## Predstavitev družine Phi-3 / Phi-3.5

Družina Phi-3 / 3.5 je namenjena predvsem scenarijem uporabe, kot so besedilo, vizija in Agent (MoE):

### Phi-3 / 3.5 Navodila

Predvsem za generiranje besedila, dopolnjevanje pogovora in izvleček vsebin itd.

**Phi-3-mini**

Jezikovni model s 3,8 milijardami parametrov je na voljo na Microsoft Foundry, Hugging Face in Ollama. Phi-3 modeli znatno presegajo jezikovne modele enake in večje velikosti na ključnih merilih (glej spodnje številke meril, višje število je boljše). Phi-3-mini presega modele z dvakrat več parametri, medtem ko Phi-3-small in Phi-3-medium presegata večje modele, vključno z GPT-3.5.

**Phi-3-small & medium**

S samo 7 milijardami parametrov Phi-3-small premaga GPT-3.5T na različnih jezikovnih, sklepalnih, kodirnih in matematičnih merilih.

Phi-3-medium s 14 milijardami parametrov nadaljuje to linijo in presega Gemini 1.0 Pro.

**Phi-3.5-mini**

Lahko ga razumemo kot nadgradnjo Phi-3-mini. Medtem ko število parametrov ostaja nespremenjeno, izboljša podporo za več jezikov (podpora za več kot 20 jezikov: arabščina, kitajščina, češčina, danščina, nizozemščina, angleščina, finščina, francoščina, nemščina, hebrejščina, madžarščina, italijanščina, japonščina, korejščina, norveščina, poljščina, portugalščina, ruščina, španščina, švedščina, tajščina, turščina, ukrajinščina) in dodaja močnejšo podporo za dolge kontekste.

Phi-3.5-mini s 3,8 milijardami parametrov presega jezikovne modele enake velikosti in je primerljiv z modeli dvakrat večje velikosti.

### Phi-3 / 3.5 Vizija

Model Instruct družine Phi-3/3.5 lahko dojemamo kot Phi-jevo sposobnost razumevanja, medtem ko Vizija daje Phi-ju oči za razumevanje sveta.


**Phi-3-Vision**

Phi-3-vision, s samo 4,2 milijardami parametrov, nadaljuje to linijo in presega večje modele, kot so Claude-3 Haiku in Gemini 1.0 Pro V, pri splošnih vizualnih sklepalnih nalogah, OCR in razumevanju tabel ter diagramov.


**Phi-3.5-Vision**

Phi-3.5-Vision je tudi nadgradnja Phi-3-Vision, ki dodaja podporo za več slik hkrati. Lahko ga razumemo kot izboljšavo v viziji, saj ne vidi le slik, ampak tudi videoposnetke.

Phi-3.5-vision presega večje modele, kot so Claude-3.5 Sonnet in Gemini 1.5 Flash, pri OCR, razumevanju tabel in grafikonov in je primerljiv pri splošnih nalogah sklepanja o vizualnem znanju. Podpira večslični vhod, tj. sklepa na podlagi več vhodnih slik.


### Phi-3.5-MoE

***Mešanica strokovnjakov (Mixture of Experts, MoE)*** omogoča modelom, da se vnaprej učijo z bistveno manj računske moči, kar pomeni, da lahko z istim proračunom za računske vire bistveno povečate velikost modela ali zbirke podatkov kot pri gostem modelu. Posebej naj bi MoE model dosegel enako kakovost kot njegov gost model veliko hitreje med prednastavitvijo.

Phi-3.5-MoE sestavlja 16 modulov strokovnjakov s po 3,8 milijarde parametrov. Phi-3.5-MoE z le 6,6 milijardami aktivnih parametrov dosega podobno raven sklepanja, jezikovnega razumevanja in matematike kot veliko večji modeli.

Phi-3/3.5 družino modelov lahko uporabimo glede na različne scenarije. Za razliko od LLM-ja, lahko Phi-3/3.5-mini ali Phi-3/3.5-Vision namestite na robne naprave.


## Kako uporabljati družino modelov Phi-3/3.5

Želimo uporabiti Phi-3/3.5 v različnih scenarijih. Nato bomo uporabili Phi-3/3.5 glede na različne scenarije.

![phi3](../../../translated_images/sl/phi3.655208c3186ae381.webp)

### Inferenca preko oblačnih API-jev

**Microsoft Foundry modelov**

> **Opomba:** GitHub modeli se upokojijo konec julija 2026. [Microsoft Foundry modelov](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) je neposredna zamenjava.

Microsoft Foundry modeli so najhitrejši način. Hitro lahko dostopate do Phi-3/3.5-Instruct modela prek kataloga modelov Foundry. V kombinaciji z Azure AI Inference SDK / OpenAI SDK lahko prek kode dostopate do API-ja in zaključite klic za Phi-3/3.5-Instruct. Lahko tudi preizkušate različne učinke prek Playground.

- Demo: Primerjava učinkov Phi-3-mini in Phi-3.5-mini v kitajskih scenarijih

![phi3](../../../translated_images/sl/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/sl/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Ali če želimo uporabiti vizijske in MoE modele, lahko uporabimo Microsoft Foundry za izvedbo klica. Če vas zanima, lahko preberete Phi-3 Cookbook, da se naučite, kako klicati Phi-3/3.5 Instruct, Vision, MoE preko Microsoft Foundry [Kliknite to povezavo](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Poleg kataloga oblačnih Microsoft Foundry modelov lahko za izvedbo povezanih klicev uporabite tudi [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst). Obiščete NVIDIA NIM za izvedbo API klicev družine modelov Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) je skupek pospešenih mikrostoritev za inferenco, zasnovanih za učinkovito uvajanje AI modelov v različnih okoljih, vključno z oblaki, podatkovnimi centri in delovnimi postajami.

Tu je nekaj ključnih značilnosti NVIDIA NIM:

- **Enostavnost namestitve:** NIM omogoča namestitev AI modelov z eno samo ukazno vrstico, kar olajša integracijo v obstoječe delovne tokove.

- **Optimizirana zmogljivost:** Izrablja NVIDIA-jeve vnaprej optimizirane pogone sklepanja, kot sta TensorRT in TensorRT-LLM, da zagotovi nizko zakasnitev in visoko prepustnost.
- **Razširljivost:** NIM podpira samodejno skaliranje na Kubernetesu, kar omogoča učinkovito obvladovanje raznolikih delovnih obremenitev.
- **Varnost in nadzor:** Organizacije lahko ohranijo nadzor nad svojimi podatki in aplikacijami z gostovanjem mikro storitev NIM na lastni upravljani infrastrukturi.
- **Standardni API-ji:** NIM zagotavlja industrijsko standardne API-je, kar olajša ustvarjanje in integracijo AI aplikacij, kot so klepetalniki, AI asistenti in drugo.

NIM je del NVIDIA AI Enterprise, katerega cilj je poenostaviti uvajanje in operativnost AI modelov ter zagotoviti njihovo učinkovito delovanje na NVIDIA GPU-jih.

- Demo: Uporaba NVIDIA NIM za klic Phi-3.5-Vision-API  [[Kliknite ta povezavo](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Lokalno poganjanje Phi-3/3.5
Sklepanje v zvezi s Phi-3 ali katerim koli jezikovnim modelom, kot je GPT-3, pomeni postopek ustvarjanja odgovorov ali napovedi na podlagi prejete vhodne vsebine. Ko Phi-3 podate vprašanje ali poziv, uporabi svoj usposobljeni nevronski model, da na podlagi vzorcev in povezav v podatkih, na katerih je bil treniran, sklepa najbolj verjeten in ustrezen odgovor.

**Hugging Face Transformer**
Hugging Face Transformers je zmogljiva knjižnica, namenjena za obdelavo naravnega jezika (NLP) in druge naloge strojnega učenja. Tukaj je nekaj ključnih točk o njej:

1. **Vnaprej naučeni modeli**: Zagotavlja tisoče vnaprej naučenih modelov, ki se lahko uporabljajo za različna opravila, kot so klasifikacija besedila, prepoznavanje imenovanih entitet, odgovarjanje na vprašanja, povzema, prevajanje in generiranje besedila.

2. **Interoperabilnost okvirov:** Knjižnica podpira več ogrodij globokega učenja, vključno s PyTorch, TensorFlow in JAX. To omogoča, da model trenirate v enem ogrodju in ga uporabljate v drugem.

3. **Multimodalne zmogljivosti:** Poleg NLP knjižnica podpira tudi naloge v računalniškem vidu (npr. klasifikacija slik, zaznavanje objektov) in obdelavi zvoka (npr. prepoznavanje govora, klasifikacija zvoka).

4. **Enostavnost uporabe:** Knjižnica ponuja API-je in orodja za enostavno prenos in prilagajanje modelov, kar jo naredi dostopno tako začetnikom kot strokovnjakom.

5. **Skupnost in viri:** Hugging Face ima živahno skupnost in obsežno dokumentacijo, vodiče in navodila, ki uporabnikom pomagajo začeti in kar najbolje izkoristiti knjižnico.
[uradna dokumentacija](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) ali njihov [GitHub repozitorij](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

To je najpogosteje uporabljena metoda, vendar zahteva pospešitev z GPU. Konec koncev, scenariji, kot sta Vision in MoE, zahtevajo veliko izračunov, ki bodo na CPU-ju zelo počasni, če niso kvantirani.


- Demo: Uporaba Transformerja za klic Phi-3.5-Instruct [Kliknite ta povezavo](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Uporaba Transformerja za klic Phi-3.5-Vision [Kliknite ta povezavo](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Uporaba Transformerja za klic Phi-3.5-MoE [Kliknite ta povezavo](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) je platforma, namenjena olajšanju lokalnega poganjanja velikih jezikovnih modelov (LLM) na vašem računalniku. Podpira različne modele, kot so Llama 3.1, Phi 3, Mistral, in Gemma 2, med drugim. Platforma poenostavi postopek z združevanjem uteži modela, konfiguracije in podatkov v en paket, kar uporabnikom omogoča lažje prilagajanje in ustvarjanje lastnih modelov. Ollama je na voljo za macOS, Linux in Windows. To je odlično orodje, če želite eksperimentirati ali uvajati LLM brez odvisnosti od oblačnih storitev. Ollama je najpreprostejša pot, samo izvedete naslednji ukaz.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) je Microsoftovo brez povezave in lokalno okolje za poganjanje modelov, kot je Phi, popolnoma na lastni strojni opremi – brez naročnine na Azure, API ključa ali povezave v omrežje. Avtomatsko izbere najboljšega razpoložljivega izvajalnega ponudnika (NPU, GPU ali CPU) in ponuja vmesnik, združljiv z OpenAI, tako da lahko obstoječa koda `openai`/Azure AI Inference SDK deluje z minimalnimi spremembami. Za začetek glejte [Foundry Local dokumentacijo](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst).

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Ali pa uporabite SDK neposredno v Pythonu:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime za GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) je večplatformski pospeševalnik sklepanja in učenja strojnega učenja. ONNX Runtime za Generative AI (GENAI) je zmogljivo orodje, ki vam pomaga učinkovito poganjati generativne AI modele na različnih platformah.

## Kaj je ONNX Runtime?
ONNX Runtime je odprtokodni projekt, ki omogoča visoko zmogljivo sklepanje strojnih učnih modelov. Podpira modele v formatu Open Neural Network Exchange (ONNX), ki je standard za predstavitev modelov strojnega učenja. ONNX Runtime sklepanju omogoča hitrejšo uporabniško izkušnjo in nižje stroške, podpira modele iz ogrodij globokega učenja, kot so PyTorch in TensorFlow/Keras, pa tudi klasične knjižnice strojnega učenja, kot so scikit-learn, LightGBM, XGBoost itd. ONNX Runtime je združljiv z različno strojno opremo, gonilniki in operacijskimi sistemi ter zagotavlja optimalno zmogljivost z uporabo strojnih pospeševalnikov, kjer je to mogoče, skupaj z optimizacijami in transformacijami grafov.

## Kaj je generativna AI?
Generativna umetna inteligenca se nanaša na AI sisteme, ki lahko generirajo novo vsebino, kot so besedilo, slike ali glasba, na podlagi podatkov, na katerih so bili usposobljeni. Primeri so jezikovni modeli, kot je GPT-3, in modeli za generiranje slik, kot je Stable Diffusion. Knjižnica ONNX Runtime za GenAI zagotavlja generativni AI zanko za ONNX modele, vključno s sklepanjem z ONNX Runtime, obdelavo logitov, iskanjem in vzorčenjem ter upravljanjem KV predpomnilnika.

## ONNX Runtime za GENAI
ONNX Runtime za GENAI širi zmogljivosti ONNX Runtime za podporo generativnih AI modelov. Tukaj so nekatere ključne lastnosti:

- **Široka podpora platformam:** Deluje na različnih platformah, vključno z Windows, Linux, macOS, Android in iOS.
- **Podpora modelom:** Podpira številne priljubljene generativne AI modele, kot so LLaMA, GPT-Neo, BLOOM in več.
- **Optimizacija zmogljivosti:** Vključuje optimizacije za različne strojne pospeševalnike, kot so NVIDIA GPU-ji, AMD GPU-ji in drugi2.
- **Enostavnost uporabe:** Ponuja API-je za enostavno integracijo v aplikacije, kar omogoča generiranje besedila, slik in druge vsebine z minimalno količino kode.
- Uporabniki lahko kličejo visokonivojsko metodo generate(), ali pa izvajajo vsako iteracijo modela v zanki, pri čemer generirajo en tok po enkrat, z možnostjo posodabljanja parametrov generiranja znotraj zanke.
- ONNX runtime podpira tudi pohlepno / beam iskanje in TopP, TopK vzorčenje za generiranje sekvenc tokenov ter vgrajeno obdelavo logitov, kot so kazni za ponavljanje. Prav tako lahko enostavno dodate lastno ocenjevanje.

## Začetek uporabe
Za začetek z ONNX Runtime za GENAI lahko sledite naslednjim korakom:

### Namestite ONNX Runtime:
```Python
pip install onnxruntime
```
### Namestite razširitve za generativno AI:
```Python
pip install onnxruntime-genai
```

### Zaženite model: Tu je preprost primer v Pythonu:
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

Poleg referenčnih metod ONNX Runtime, Ollama in Foundry Local lahko tudi dopolnimo referenco kvantitativnih modelov na podlagi referenčnih metod modelov, ki jih ponujajo različni proizvajalci. Na primer Apple MLX okvir z Apple Metal, Qualcomm QNN z NPU, Intel OpenVINO s CPU/GPU itd. Več vsebine lahko dobite tudi iz [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Več

Spoznali smo osnove družine Phi-3/3.5, vendar za bolj poglobljeno razumevanje SLM potrebujemo več znanja. Odgovore lahko najdete v Phi-3 Cookbook. Če želite izvedeti več, obiščite [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->