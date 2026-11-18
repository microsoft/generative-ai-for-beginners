# Uvod u Male Jezične Modele za Generativnu AI za Početnike
Generativna AI je fascinantno područje umjetne inteligencije koje se fokusira na stvaranje sustava sposobnih za generiranje novog sadržaja. Taj sadržaj može varirati od teksta i slika do glazbe pa čak i cijelih virtualnih okruženja. Jedna od najuzbudljivijih primjena generativne AI je u području jezičnih modela.

## Što su Mali Jezični Modeli?

Mali Jezični Model (SLM) predstavlja smanjenu varijantu velikog jezičnog modela (LLM), koristeći mnoge arhitektonske principe i tehnike LLM-a, a pritom pokazuje znatno smanjen računalni otisak.

SLM-ovi su podskup jezičnih modela dizajniranih za generiranje teksta nalik ljudskom. Za razliku od svojih većih kolega, poput GPT-4, SLM-ovi su kompaktniji i učinkovitiji, što ih čini idealnima za primjene gdje su računalni resursi ograničeni. Unatoč manjoj veličini, i dalje mogu izvršavati različite zadatke. Obično se SLM-ovi konstruiraju komprimiranjem ili destilacijom LLM-ova, s ciljem zadržavanja značajnog dijela funkcionalnosti i jezičnih sposobnosti izvornog modela. Ovo smanjenje veličine modela smanjuje ukupnu složenost, čineći SLM-ove učinkovitijima u pogledu korištenja memorije i računalnih zahtjeva. Unatoč tim optimizacijama, SLM-ovi i dalje mogu obavljati širok raspon zadataka obrade prirodnog jezika (NLP):

- Generiranje teksta: Stvaranje koherentnih i kontekstualno relevantnih rečenica ili odlomaka.
- Dovršavanje teksta: Predviđanje i dovršavanje rečenica na temelju zadanog prompta.
- Prevođenje: Pretvaranje teksta s jednog jezika na drugi.
- Sažimanje: Skraćivanje dugih tekstova u kraće, razumljivije sažetke.

Međutim, s nekim kompromisima u performansama ili dubini razumijevanja u usporedbi s njihovim većim kolegama.

## Kako rade Mali Jezični Modeli?
SLM-ovi se treniraju na golemim količinama tekstualnih podataka. Tijekom treninga uče obrasce i strukture jezika, što im omogućuje generiranje teksta koji je gramatički točan i kontekstualno prikladan. Proces treninga uključuje:

- Prikupljanje podataka: Skupljanje velikih skupova podataka teksta iz različitih izvora.
- Predobrada: Čišćenje i organiziranje podataka kako bi bili pogodni za trening.
- Trening: Korištenje algoritama strojnog učenja za podučavanje modela kako razumjeti i generirati tekst.
- Fino podešavanje: Prilagođavanje modela za poboljšanje performansi na specifičnim zadacima.

Razvoj SLM-ova se usklađuje s rastućom potrebom za modelima koji se mogu implementirati u okruženjima s ograničenim resursima, kao što su mobilni uređaji ili edge computing platforme, gdje je potpuno opsežni LLM nepraktičan zbog svojih velikih zahtjeva za resursima. Fokusiranjem na učinkovitost, SLM-ovi balansiraju performanse i pristupačnost, omogućujući širu primjenu u raznim područjima.

![slm](../../../translated_images/hr/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Ciljevi učenja

U ovoj lekciji nadamo se predstaviti znanje o SLM-ovima i povezati ga s Microsoft Phi-3 kako bismo naučili različite scenarije u tekstualnom sadržaju, vidu i MoE-u.

Do kraja ove lekcije trebali biste moći odgovoriti na sljedeća pitanja:

- Što je SLM?
- Koja je razlika između SLM-a i LLM-a?
- Što je Microsoft Phi-3/3.5 obitelj?
- Kako pokrenuti izvođenje s Microsoft Phi-3/3.5 obitelji?

Spremni? Krenimo.

## Razlike između Velikih Jezičnih Modela (LLM) i Malih Jezičnih Modela (SLM)

I LLM-ovi i SLM-ovi izgrađeni su na osnovnim principima probabilističkog strojnog učenja, slijedeći slične pristupe u arhitektonskom dizajnu, metodologiji treninga, procesima generiranja podataka i tehnikama evaluacije modela. Ipak, nekoliko ključnih faktora razlikuje ove dvije vrste modela.

## Primjene Malih Jezičnih Modela

SLM-ovi imaju širok spektar primjena, uključujući:

- Chatbotovi: Pružanje korisničke podrške i interakcija s korisnicima na konverzacijski način.
- Kreiranje sadržaja: Pomoć piscima u generiranju ideja ili čak sastavljanju cijelih članaka.
- Obrazovanje: Pomoć studentima u pisanju zadataka ili učenju novih jezika.
- Pristupačnost: Izrada alata za osobe s invaliditetom, poput sustava za pretvaranje teksta u govor.

**Veličina**
  
Primarna razlika između LLM-ova i SLM-ova leži u veličini modela. LLM-ovi, poput ChatGPT-a (GPT-4), mogu imati procijenjenih 1,76 bilijuna parametara, dok su open-source SLM-ovi poput Mistral 7B dizajnirani s znatno manjim brojem parametara — otprilike 7 milijardi. Ova razlika prvenstveno je zbog razlika u arhitekturi modela i procesima treninga. Na primjer, ChatGPT koristi mehanizam self-attention u okviru enkoder-dekoder strukture, dok Mistral 7B koristi sliding window attention, što omogućuje učinkovitiji trening unutar modela samo s dekoderom. Ova razlika u arhitekturi ima duboke implikacije na složenost i performanse ovih modela.

**Razumijevanje**

SLM-ovi su obično optimizirani za performanse unutar specifičnih područja, čineći ih vrlo specijaliziranima, ali potencijalno ograničenima u pružanju širokog kontekstualnog razumijevanja različitih područja znanja. Suprotno tome, LLM-ovi nastoje simulirati inteligenciju nalik ljudskoj na sveobuhvatnijoj razini. Trenirani na golemim, raznolikim skupovima podataka, LLM-ovi su dizajnirani za dobre rezultate u raznim područjima, nudeći veću svestranost i prilagodljivost. Posljedično, LLM-ovi su prikladniji za širi raspon zadataka, poput obrade prirodnog jezika i programiranja.

**Računalna snaga**

Trening i implementacija LLM-ova su procesi intenzivni u pogledu resursa, često zahtijevajući značajnu računalnu infrastrukturu, uključujući velike GPU klastere. Na primjer, trening modela poput ChatGPT-a od početka može zahtijevati tisuće GPU-a tijekom dugih razdoblja. Nasuprot tome, SLM-ovi, s manjim brojem parametara, su pristupačniji po pitanju računalnih resursa. Modeli poput Mistral 7B mogu se trenirati i pokretati na lokalnim računalima opremljenim umjerenim GPU sposobnostima, iako trening zahtijeva nekoliko sati na više GPU-a.

**Pristranost**

Pristranost je poznat problem kod LLM-ova, prvenstveno zbog prirode podataka za trening. Ti modeli često se oslanjaju na sirove, javno dostupne podatke s interneta, koji mogu podzastupljivati ili pogrešno predstavljati određene skupine, unositi pogrešne oznake ili odražavati jezične pristranosti koje su posljedica dijalekta, geografskih varijacija i gramatičkih pravila. Osim toga, složenost arhitekture LLM-ova može nenamjerno pogoršati pristranost, koja može proći nezamijećeno bez pažljivog fino podešavanja. S druge strane, SLM-ovi, obučeni na ograničenijim, domen-specifičnim skupovima podataka, inherentno su manje skloni takvim pristranostima, iako nisu potpuno imuni.

**Izvođenje**

Smanjena veličina SLM-ova daje im značajnu prednost u smislu brzine izvođenja, omogućujući im učinkovito generiranje rezultata na lokalnom hardveru bez potrebe za opsežnom paralelnom obradom. Nasuprot tome, LLM-ovi zbog svoje veličine i složenosti često zahtijevaju značajne paralelne računalne resurse za postizanje prihvatljivih vremena izvođenja. Prisutnost više istovremenih korisnika dodatno usporava vrijeme odziva LLM-ova, osobito kada su implementirani u velikim razmjerima.

Ukratko, iako LLM-ovi i SLM-ovi dijele osnovu u strojnome učenju, oni se značajno razlikuju u veličini modela, zahtjevima za resursima, kontekstualnom razumijevanju, osjetljivosti na pristranost i brzini izvođenja. Te razlike odražavaju njihovu prikladnost za različite scenarije, pri čemu su LLM-ovi svestraniji, ali zahtjevniji za resurse, dok SLM-ovi nude učinkovitost prilagođenu domeni s manjim računalnim zahtjevima.

***Napomena: U ovoj lekciji ćemo predstaviti SLM koristeći Microsoft Phi-3 / 3.5 kao primjer.***

## Predstavljanje Phi-3 / Phi-3.5 Obitelji

Phi-3 / 3.5 obitelj prvenstveno cilja na scenarije u tekstu, viziji i Agent (MoE) primjenama:

### Phi-3 / 3.5 Instruct

Prvenstveno za generiranje teksta, dovršavanje razgovora i ekstrakciju informacija iz sadržaja, itd.

**Phi-3-mini**

Jezični model od 3,8 milijardi parametara dostupan je na Microsoft Foundry, Hugging Face i Ollama platformama. Phi-3 modeli značajno nadmašuju jezične modele iste i veće veličine na ključnim mjerilima (pogledajte brojeve na testovima dolje, veći brojevi znače bolje). Phi-3-mini nadmašuje modele dvostruke veličine, dok Phi-3-small i Phi-3-medium nadmašuju veće modele, uključujući GPT-3.5.

**Phi-3-small & medium**

Sa samo 7 milijardi parametara, Phi-3-small nadmašuje GPT-3.5T u raznim jezičnim, razložnim, kodirajućim i matematičkim mjerilima.

Phi-3-medium sa 14 milijardi parametara nastavlja ovaj trend i nadmašuje Gemini 1.0 Pro.

**Phi-3.5-mini**

Možemo ga smatrati nadogradnjom Phi-3-mini. Iako parametri ostaju nepromijenjeni, poboljšava sposobnost podrške za više jezika (podržava 20+ jezika: arapski, kineski, češki, danski, nizozemski, engleski, finski, francuski, njemački, hebrejski, mađarski, talijanski, japanski, korejski, norveški, poljski, portugalski, ruski, španjolski, švedski, tajlandski, turski, ukrajinski) i dodaje snažniju podršku za dugu kontekstualnost.

Phi-3.5-mini s 3,8 milijardi parametara nadmašuje jezične modele iste veličine i usporediv je s modelima dvostruke veličine.

### Phi-3 / 3.5 Vizija

Model Instruct Phi-3/3.5 možemo smatrati Phi-ovom sposobnošću razumijevanja, a Vizija je ono što Phi-u daje oči za razumijevanje svijeta.


**Phi-3-Vision**

Phi-3-vision, s samo 4,2 milijarde parametara, nastavlja ovaj trend i nadmašuje veće modele poput Claude-3 Haiku i Gemini 1.0 Pro V u općim zadacima vizualnog razmišljanja, OCR-u i razumijevanju tablica i dijagrama.


**Phi-3.5-Vision**

Phi-3.5-Vision je također nadogradnja Phi-3-Vision, koja dodaje podršku za višestruke slike. Možete je smatrati poboljšanjem vida; ne može samo vidjeti slike, već i videozapise.

Phi-3.5-vision nadmašuje veće modele poput Claude-3.5 Sonnet i Gemini 1.5 Flash u zadacima OCR-a, razumijevanja tablica i grafikona te je usporediv u općim zadacima razumijevanja vizualnog znanja. Podržava višekadrirani unos, tj. izvođenje razmišljanja na više ulaznih slika.


### Phi-3.5-MoE

***Mješavina stručnjaka (MoE)*** omogućava modelima predtreniranje s mnogo manje računanja, što znači da možete dramatično povećati veličinu modela ili skupa podataka uz isti proračun izračuna kao i gusto povezani modeli. Konkretno, MoE model bi trebao postići istu kvalitetu kao i njegov gusta verzija mnogo brže tijekom predtreninga.

Phi-3.5-MoE sadrži 16x3.8B stručnih modula. Phi-3.5-MoE s samo 6.6 milijardi aktivnih parametara postiže sličnu razinu razmišljanja, razumijevanja jezika i matematike kao mnogo veći modeli.

Možemo koristiti modele iz Phi-3/3.5 obitelji za različite scenarije. Za razliku od LLM-a, Phi-3/3.5-mini ili Phi-3/3.5-Vision možete implementirati na edge uređaje.


## Kako koristiti modele Phi-3/3.5 obitelji

Nadamo se koristiti Phi-3/3.5 u različitim scenarijima. Sljedeće, koristit ćemo Phi-3/3.5 na temelju različitih scenarija.

![phi3](../../../translated_images/hr/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Izvođenje putem Cloud API-ja

**Microsoft Foundry modeli**

> **Napomena:** GitHub modeli se povlače krajem srpnja 2026. [Microsoft Foundry modeli](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) su izravna zamjena.

> **Napomena:** Cijela Phi-3/3.5 obitelj (Instruct, Vision i MoE varijante) povučena je iz Microsoft Foundry Models kataloga 2025-08-30. Umjesto njih koristite tamo `Phi-4` (Instruct) ili `Phi-4-mini-instruct` — primjeri Phi-3/3.5 u nastavku i dalje rade putem Hugging Face, Ollama, ONNX Runtime i NVIDIA NIM.

Microsoft Foundry modeli sada pružaju nasljednike Phi-4. Koristite `Phi-4` ili `Phi-4-mini-instruct` umjesto povučenih Phi-3/3.5 modela kada pratite primjere cloud API-ja.

- Demo: Usporedba učinaka Phi-3-mini i Phi-3.5-mini u kineskim scenarijima

![phi3](../../../translated_images/hr/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/hr/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Ako želite koristiti modele vidljivosti (multimodalne) u oblaku, koristite trenutno dostupni `Phi-4-multimodal-instruct` putem Microsoft Foundry umjesto povučenih Phi-3/3.5 Vision modela; za tekstualne zadatke koristite `Phi-4` ili `Phi-4-mini-instruct`. Phi-3.5 MoE model je povučen iz Microsoft Foundry, pa koristite druge opcije opisane u ovoj lekciji (na primjer Hugging Face) ako želite eksperimentirati s njim. Ako ste zainteresirani, možete pročitati Phi Cookbook kako naučiti kako pozivati Phi modele putem Microsoft Foundry [Kliknite ovaj link](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Osim Microsoft Foundry Models kataloga u oblaku, također možete koristiti [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) za izvršavanje povezanih poziva. Možete posjetiti NVIDIA NIM za izvršavanje API poziva Phi-3/3.5 obitelji. NVIDIA NIM (NVIDIA Inference Microservices) je skup ubrzanih mikroservisa za izvedbu namijenjenih za pomoć developerima u učinkovitom implementiranju AI modela u različitim okruženjima, uključujući oblak, podatkovne centre i radne stanice.

Evo nekoliko ključnih značajki NVIDIA NIM-a:

- **Jednostavnost implementacije:** NIM omogućava implementaciju AI modela jednim naredbom, što olakšava integraciju u postojeće tokove rada.
- **Optimizirana izvedba:** Iskorištava NVIDIA-in unaprijed optimizirani inferencijski motor, poput TensorRT i TensorRT-LLM, kako bi osigurao nisku latenciju i visok protok.
- **Skalabilnost:** NIM podržava automatsko skaliranje na Kubernetesu, omogućujući učinkovito upravljanje promjenjivim opterećenjima.
- **Sigurnost i kontrola:** Organizacije mogu zadržati kontrolu nad svojim podacima i aplikacijama samostalnim hostanjem NIM mikroservisa na vlastitoj upravljanoj infrastrukturi.
- **Standardni API-ji:** NIM pruža industrijski standardizirane API-je, što olakšava izradu i integraciju AI aplikacija poput chatbotova, AI asistenata i slično.

NIM je dio NVIDIA AI Enterprise, koja nastoji pojednostaviti implementaciju i operacionalizaciju AI modela, osiguravajući njihovo učinkovito izvođenje na NVIDIA GPU-ima.

- Demo: Korištenje NVIDIA NIM za pozivanje Phi-3.5-Vision-API [[Kliknite ovaj link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Pokretanje Phi-3/3.5 lokalno
Inferencija u odnosu na Phi-3, ili bilo koji jezični model poput GPT-3, odnosi se na proces generiranja odgovora ili predviđanja temeljenih na unesenom ulazu. Kada Phi-3 unesete upit ili pitanj, on koristi svoju treniranu neuronsku mrežu da zaključi najvjerojatniji i relevantni odgovor analizirajući obrasce i odnose u podacima na kojima je treniran.

**Hugging Face Transformer**
Hugging Face Transformers je moćna biblioteka dizajnirana za obradu prirodnog jezika (NLP) i druge zadatke strojnog učenja. Evo nekoliko ključnih točaka o njoj:

1. **Unaprijed trenirani modeli**: Nudi tisuće unaprijed treniranih modela koji se mogu koristiti za razne zadatke poput klasifikacije teksta, prepoznavanja imenovanih entiteta, odgovaranja na pitanja, sažimanja, prijevoda i generiranja teksta.

2. **Interoperabilnost okvira**: Biblioteka podržava više dubokih učenjačkih okvira, uključujući PyTorch, TensorFlow i JAX. To vam omogućuje da trenirate model u jednom okviru i koristite ga u drugom.

3. **Multimodalne sposobnosti**: Osim NLP-a, Hugging Face Transformers podržava zadatke u računalnom vidu (npr. klasifikacija slika, detekcija objekata) i obradi zvuka (npr. prepoznavanje govora, klasifikacija zvuka).

4. **Jednostavnost korištenja**: Biblioteka nudi API-je i alate za jednostavno preuzimanje i fino podešavanje modela, što je pristupačno i početnicima i stručnjacima.

5. **Zajednica i resursi**: Hugging Face ima živu zajednicu i opsežnu dokumentaciju, tutorijale i vodiče kako bi pomogao korisnicima da započnu i maksimalno iskoriste biblioteku.
[službena dokumentacija](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) ili njihov [GitHub repozitorij](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Ovo je najčešće korištena metoda, ali također zahtijeva GPU ubrzanje. Uostalom, scenariji poput Vision i MoE zahtijevaju puno izračuna, što bi na CPU-u bez kvantizacije bilo vrlo sporo.


- Demo: Korištenje Transformera za pozivanje Phi-3.5-Instruct [Kliknite ovaj link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Korištenje Transformera za pozivanje Phi-3.5-Vision [Kliknite ovaj link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Korištenje Transformera za pozivanje Phi-3.5-MoE [Kliknite ovaj link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) je platforma dizajnirana da olakša pokretanje velikih jezičnih modela (LLM) lokalno na vašem računalu. Podržava razne modele poput Llama 3.1, Phi 3, Mistral i Gemma 2, između ostalih. Platforma pojednostavljuje proces spajanjem težina modela, konfiguracije i podataka u jedan paket, što korisnicima olakšava prilagodbu i stvaranje vlastitih modela. Ollama je dostupna za macOS, Linux i Windows. Sjajan je alat ako želite eksperimentirati ili implementirati LLM bez oslanjanja na oblačne usluge. Ollama je najizravniji način, potrebno je samo izvršiti sljedeću naredbu.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) je Microsoftovo offline, na uređaju radno okruženje za pokretanje modela poput Phi u potpunosti na vlastitom hardveru - bez potrebe za Azure pretplatom, API ključem ili internetskom vezom. Automatski odabire najbolji dostupni izvršni pružatelj (NPU, GPU ili CPU) i izlaže OpenAI-kompatibilnu krajnju točku, tako da postojeći `openai`/Azure AI Inference SDK kod može ciljati na njega uz minimalne promjene. Pogledajte [Foundry Local dokumentaciju](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) za početak.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Ili koristite SDK izravno u Pythonu:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime za GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) je višestruka platforma za ubrzanje inferencije i treniranja strojnog učenja. ONNX Runtime za Generativnu AI (GENAI) je moćan alat koji vam pomaže da učinkovito pokrenete generativne AI modele na različitim platformama.

## Što je ONNX Runtime?
ONNX Runtime je open-source projekt koji omogućuje visoko performansnu inferenciju modela strojnog učenja. Podržava modele u Open Neural Network Exchange (ONNX) formatu, koji je standard za predstavljanje modela strojnog učenja. ONNX Runtime inferencija može omogućiti brža korisnička iskustva i niže troškove, podržavajući modele iz dubokih učenjačkih okvira poput PyTorch i TensorFlow/Keras, kao i klasičnih biblioteka strojnog učenja poput scikit-learn, LightGBM, XGBoost i drugih. ONNX Runtime je kompatibilan s različitim hardverom, upravljačkim programima i operativnim sustavima te pruža optimalne performanse iskorištavanjem hardverskih ubrzivača kad je to moguće, zajedno s optimizacijama i transformacijama grafova.

## Što je Generativna AI?
Generativna AI odnosi se na AI sustave koji mogu generirati novi sadržaj, poput teksta, slika ili glazbe, na temelju podataka na kojima su trenirani. Primjeri uključuju jezične modele poput GPT-3 i modele za generiranje slika poput Stable Diffusion. ONNX Runtime za GenAI biblioteka pruža generativni AI ciklus za ONNX modele, uključujući inferenciju s ONNX Runtime, obradu logits, pretraživanje i uzorkovanje te upravljanje KV predmemorijom.

## ONNX Runtime za GENAI
ONNX Runtime za GENAI proširuje mogućnosti ONNX Runtime za podršku generativnim AI modelima. Evo nekoliko ključnih značajki:

- **Široka podrška platformi:** Radi na raznim platformama, uključujući Windows, Linux, macOS, Android i iOS.
- **Podrška za modele:** Podržava mnoge popularne generativne AI modele, poput LLaMA, GPT-Neo, BLOOM i drugih.
- **Optimizacija izvedbe:** Uključuje optimizacije za različite hardverske ubrzivače poput NVIDIA GPU-a, AMD GPU-a i drugih.
- **Jednostavnost korištenja:** Pruža API-je za jednostavnu integraciju u aplikacije, omogućujući vam generiranje teksta, slika i drugog sadržaja uz minimalan kod.
- Korisnici mogu pozvati visoku razinu metodu generate(), ili pokrenuti svaku iteraciju modela u petlji, generirajući jedan token po jedan i po želji ažurirajući parametre generiranja unutar petlje.
- ONNX runtime također podržava greedy/beam pretraživanje i TopP, TopK uzorkovanje za generiranje sekvenci tokena te ugrađenu obradu logits poput penalizacije ponavljanja. Također je lako dodati vlastito ocjenjivanje.

## Početak rada
Za početak rada s ONNX Runtime za GENAI, možete slijediti ove korake:

### Instalirajte ONNX Runtime:
```Python
pip install onnxruntime
```
### Instalirajte Generative AI Extensions:
```Python
pip install onnxruntime-genai
```

### Pokrenite model: Evo jednostavnog primjera u Pythonu:
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
### Demo:Korištenje ONNX Runtime GenAI za pozivanje Phi-3.5-Vision


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


**Ostalo**

Osim referentnih metoda ONNX Runtime, Ollama i Foundry Local, također možemo dovršiti referencu kvantitativnih modela na temelju referentnih metoda modela koje pružaju različiti proizvođači. Kao što su Apple MLX okvir s Apple Metalom, Qualcomm QNN s NPU-om, Intel OpenVINO s CPU/GPU-om itd. Više sadržaja možete pronaći u [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Više

Naučili smo osnove Phi-3/3.5 obitelji, ali da bismo saznali više o SLM-u, potrebna su nam dodatna znanja. Odgovore možete pronaći u Phi-3 Cookbooku. Ako želite saznati više, molimo posjetite [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->