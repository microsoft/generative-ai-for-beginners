# Uvod u Male Jezične Modele za Generativnu AI za Početnike
Generativna AI je fascinantno područje umjetne inteligencije koje se fokusira na stvaranje sustava sposobnih za generiranje novog sadržaja. Taj sadržaj može varirati od teksta i slika do glazbe pa čak i cjelokupnih virtualnih okruženja. Jedna od najuzbudljivijih primjena generativne AI je u području jezičnih modela.

## Što su Mali Jezični Modeli?

Mali Jezični Model (SLM) predstavlja smanjenu varijantu velikog jezičnog modela (LLM), koristeći mnoge arhitektonske principe i tehnike LLM-ova, dok istovremeno pokazuje značajno manji računalni otisak. 

SLM-ovi su podskup jezičnih modela dizajniranih za generiranje teksta sličnog čovjeku. Za razliku od svojih većih kolega, poput GPT-4, SLM-ovi su kompaktniji i učinkovitiji, što ih čini idealnima za primjene gdje su računalni resursi ograničeni. Unatoč njihovoj manjoj veličini, i dalje mogu obavljati razne zadatke. Uobičajeno, SLM-ovi se konstruiraju kompresijom ili destilacijom LLM-ova, s ciljem zadržavanja značajnog dijela izvorne funkcionalnosti i jezičnih sposobnosti modela. Ovo smanjenje veličine modela smanjuje ukupnu složenost, čineći SLM-ove učinkovitijima u pogledu memorijske upotrebe i računalnih zahtjeva. Unatoč tim optimizacijama, SLM-ovi i dalje mogu obavljati širok raspon zadataka obrade prirodnog jezika (NLP):

- Generiranje teksta: Stvaranje koherentnih i kontekstualno relevantnih rečenica ili odlomaka.
- Dovršavanje teksta: Predviđanje i dovršavanje rečenica na temelju zadanog upita.
- Prijevod: Pretvaranje teksta s jednog jezika na drugi.
- Sažimanje: Sažimanje dugih tekstova u kraće i razumljivije sažetke.

Iako s određenim kompromisima u pogledu performansi ili dubine razumijevanja u odnosu na njihove veće kolege. 

## Kako Male Jezične Modele Funkcioniraju?
SLM-ovi se treniraju na ogromnim količinama tekstualnih podataka. Tijekom treninga, oni uče obrasce i strukture jezika, što im omogućuje generiranje teksta koji je gramatički točan i kontekstualno prikladan. Proces treninga uključuje:

- Prikupljanje podataka: Sakupljanje velikih skupova podataka s teksta iz različitih izvora.
- Predobrada: Čišćenje i organiziranje podataka kako bi bili prikladni za trening.
- Trening: Korištenje algoritama strojnog učenja za podučavanje modela kako razumjeti i generirati tekst.
- Fino podešavanje: Prilagođavanje modela za poboljšanje njegovih performansi na specifičnim zadacima.

Razvoj SLM-ova usklađen je s rastućom potrebom za modelima koji se mogu implementirati u okruženjima s ograničenim resursima, kao što su mobilni uređaji ili edge računalne platforme, gdje su LLM-ovi pune veličine nepraktični zbog velikih zahtjeva za resursima. Fokusom na učinkovitost, SLM-ovi balansiraju performanse i pristupačnost, omogućavajući širu primjenu u različitim domenama.

![slm](../../../translated_images/hr/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Ciljevi učenja

U ovom ćemo se času upoznati s konceptom SLM-a i povezati ga s Microsoft Phi-3 kako bismo naučili različite scenarije u tekstualnom sadržaju, viziji i MoE.

Na kraju ovog časa trebali biste moći odgovoriti na sljedeća pitanja:

- Što je SLM?
- Koja je razlika između SLM-a i LLM-a?
- Što je Microsoft Phi-3/3.5 obitelj?
- Kako izvršiti inferenciju s Microsoft Phi-3/3.5 obitelji?

Spremni? Krenimo.

## Razlike između Velikih Jezičnih Modela (LLM) i Malih Jezičnih Modela (SLM)

I LLM-ovi i SLM-ovi izgrađeni su na temeljnim principima probabilističkog strojnog učenja, slijedeći slične pristupe u arhitektonskom dizajnu, metodologijama treninga, procesima generiranja podataka i tehnikama evaluacije modela. Međutim, nekoliko ključnih faktora razlikuje ova dva tipa modela.

## Primjene Malih Jezičnih Modela

SLM-ovi imaju širok spektar primjena, uključujući:

- Chatboti: Pružanje korisničke podrške i interakcija s korisnicima na konverzacijski način.
- Kreiranje sadržaja: Pomoć piscima generiranjem ideja ili čak pisanjem čitavih članaka.
- Obrazovanje: Pomoć studentima s pisanjem zadataka ili učenjem novih jezika.
- Pristupačnost: Stvaranje alata za osobe s invaliditetom, poput sustava za pretvaranje teksta u govor.

**Veličina**
  
Primarna razlika između LLM-ova i SLM-ova leži u veličini modela. LLM-ovi, poput ChatGPT-a (GPT-4), mogu sadržavati procijenjenih 1,76 bilijuna parametara, dok su open-source SLM-ovi poput Mistral 7B dizajnirani sa značajno manjim brojem parametara—otprilike 7 milijardi. Ova razlika prvenstveno proizlazi iz razlika u arhitekturi modela i procesima treninga. Na primjer, ChatGPT koristi mehanizam samopozornosti unutar okvira kodera-dekodera, dok Mistral 7B koristi pozornost s pomičnim prozorom, što omogućava učinkovitiji trening unutar modela temeljenog samo na dekoderu. Ova arhitektonska razlika ima duboke implikacije na složenost i performanse ovih modela.

**Razumijevanje**

SLM-ovi su obično optimizirani za performanse unutar specifičnih područja, čineći ih vrlo specijaliziranim, ali potencijalno ograničenim u sposobnosti pružanja širokog kontekstualnog razumijevanja kroz više područja znanja. Nasuprot tome, LLM-ovi nastoje simulirati ljudsku inteligenciju na sveobuhvatnijoj razini. Trenirani na golemim i različitim skupovima podataka, LLM-ovi su dizajnirani da se dobro snalaze u raznim domenama, nudeći veću svestranost i prilagodljivost. Posljedično, LLM-ovi su prikladniji za širi spektar zadataka, poput obrade prirodnog jezika i programiranja.

**Računalna snaga**

Trening i implementacija LLM-ova su procesi koji zahtijevaju velike resurse, često uključujući značajnu računalnu infrastrukturu, uključujući velike GPU grupe. Na primjer, treniranje modela poput ChatGPT-a iz početka može zahtijevati tisuće GPU-a tijekom dugih razdoblja. Suprotno tome, SLM-ovi, sa svojim manjim brojem parametara, dostupniji su u pogledu računalnih resursa. Modeli poput Mistral 7B mogu se trenirati i pokretati na lokalnim strojevima opremljenim umjerenim GPU mogućnostima, iako trening i dalje zahtijeva nekoliko sati na više GPU-a.

**Pristranost**

Pristranost je poznat problem u LLM-ovima, prvenstveno zbog prirode podataka za trening. Ti modeli često se oslanjaju na sirove, javno dostupne podatke s interneta, koji mogu nedovoljno reprezentirati ili krivo predstavljati određene skupine, uvoditi pogrešne oznake ili odražavati jezične pristranosti uzrokovane dijalektima, geografskim varijacijama i gramatičkim pravilima. Osim toga, složenost LLM arhitektura može nenamjerno pogoršati pristranost, što može proći nezapaženo bez pažljivog fino podešavanja. S druge strane, SLM-ovi, trenirani na ograničenijim, domen-specifičnim skupovima podataka, inherentno su manje podložni takvim pristranostima, iako nisu potpuno imuni.

**Inferencija**

Smanjena veličina SLM-ova daje im značajnu prednost u brzini inferencije, omogućujući efikasno generiranje izlaza na lokalnom hardveru bez potrebe za obimnom paralelnom obradom. Nasuprot tome, LLM-ovi zbog svoje veličine i složenosti često zahtijevaju velike paralelne računalne resurse kako bi postigli prihvatljive vremenske okvire za inferenciju. Prisutnost više usporednih korisnika dodatno usporava vrijeme odziva LLM-ova, osobito kada su implementirani u velikim razmjerima.

Ukratko, iako LLM-ovi i SLM-ovi dijele temelj u strojnome učenju, značajno se razlikuju po veličini modela, zahtjevima za resursima, kontekstualnom razumijevanju, podložnosti pristranosti i brzini inferencije. Te razlike odražavaju njihovu prikladnost za različite slučajeve upotrebe, pri čemu su LLM-ovi svestraniji, ali zahtjevniji za resurse, dok SLM-ovi nude veću učinkovitost usmjerenu na specifične domene s nižim računalnim zahtjevima.

***Napomena: U ovom ćemo času predstaviti SLM koristeći Microsoft Phi-3 / 3.5 kao primjer.***

## Predstavljanje Phi-3 / Phi-3.5 obitelji

Phi-3 / 3.5 obitelj uglavnom cilja na primjene u tekstu, viziji i Agentu (MoE):

### Phi-3 / 3.5 Instruct

Uglavnom za generiranje teksta, dovršavanje chata i izvlačenje informacija iz sadržaja itd.

**Phi-3-mini**

Jezični model od 3.8B dostupan je na Microsoft Foundry, Hugging Face i Ollama. Phi-3 modeli značajno nadmašuju jezične modele iste i veće veličine na ključnim pokazateljima (pogledajte brojeve benchmarka dolje, veći su brojevi bolji). Phi-3-mini nadmašuje modele dvostruke veličine, dok Phi-3-small i Phi-3-medium nadmašuju veće modele, uključujući GPT-3.5.

**Phi-3-small & medium**

S samo 7B parametara, Phi-3-small pobjeđuje GPT-3.5T na raznim jezičnim, rezonirajućim, programerskim i matematičkim testovima.

Phi-3-medium sa 14B parametara nastavlja taj trend i nadmašuje Gemini 1.0 Pro.

**Phi-3.5-mini**

Možemo ga smatrati nadogradnjom Phi-3-mini. Iako parametri ostaju nepromijenjeni, poboljšava sposobnost podrške za više jezika (podržava 20+ jezika: arapski, kineski, češki, danski, nizozemski, engleski, finski, francuski, njemački, hebrejski, mađarski, talijanski, japanski, korejski, norveški, poljski, portugalski, ruski, španjolski, švedski, tajlandski, turski, ukrajinski) i dodaje jaču podršku za dugi kontekst.

Phi-3.5-mini s 3.8B parametara nadmašuje jezične modele iste veličine i usporediv je s modelima dvostruke veličine.

### Phi-3 / 3.5 Vision

Možemo zamisliti Instruct model Phi-3/3.5 kao Phi-ovu sposobnost razumijevanja, a Vision je ono što Phi-u daje oči za razumijevanje svijeta.


**Phi-3-Vision**

Phi-3-vision, s samo 4.2B parametara, nastavlja ovaj trend i nadmašuje veće modele poput Claude-3 Haiku i Gemini 1.0 Pro V na zadacima općeg vizualnog rezoniranja, OCR-u, te razumijevanju tablica i dijagrama.


**Phi-3.5-Vision**

Phi-3.5-Vision je također nadogradnja Phi-3-Vision, dodajući podršku za više slika. Možete ga smatrati poboljšanjem vida, ne samo da možete vidjeti slike, već i videozapise.

Phi-3.5-vision nadmašuje veće modele poput Claude-3.5 Sonnet i Gemini 1.5 Flash u zadacima OCR-a, razumijevanja tablica i grafikona te je izjednačen na zadacima općeg vizualnog znanja i rezoniranja. Podržava višeframe ulaze, tj. izvođenje rezoniranja na više ulaznih slika.


### Phi-3.5-MoE

***Mješavina stručnjaka (Mixture of Experts - MoE)*** omogućuje modelima pred-trening s puno manjim računalnim zahtjevima, što znači da možete znatno povećati veličinu modela ili skupa podataka s istim računalnim proračunom kao kod gustog modela. Konkretno, MoE model bi trebao brže postići istu kvalitetu kao njegov gusti pandan tijekom pred-treninga.

Phi-3.5-MoE sastoji se od 16x3.8B stručnih modula. Phi-3.5-MoE sa samo 6.6B aktivnih parametara postiže sličnu razinu rezoniranja, razumijevanja jezika i matematike kao i mnogo veći modeli.

Phi-3/3.5 obitelj modela možemo koristiti u različitim scenarijima. Za razliku od LLM-ova, Phi-3/3.5-mini ili Phi-3/3.5-Vision možete implementirati na edge uređajima.


## Kako koristiti Phi-3/3.5 obiteljske modele

Nadamo se koristiti Phi-3/3.5 u različitim scenarijima. Sljedeće ćemo koristiti Phi-3/3.5 ovisno o različitim scenarijima.

![phi3](../../../translated_images/hr/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inferencija putem Cloud API-ja

**Microsoft Foundry modeli**

> **Napomena:** GitHub Models se povlači krajem srpnja 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) su direktna zamjena.

Microsoft Foundry modeli su najdirektniji način. Možete brzo pristupiti Phi-3/3.5-Instruct modelu kroz Foundry katalog modela. U kombinaciji s Azure AI Inference SDK / OpenAI SDK, možete pristupiti API-ju putem koda za dovršetak poziva Phi-3/3.5-Instruct. Također možete testirati različite učinke putem Playground-a.

- Demo: Usporedba učinaka Phi-3-mini i Phi-3.5-mini u kineskim scenarijima

![phi3](../../../translated_images/hr/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/hr/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Ili ako želimo koristiti modele za viziju i MoE, možete koristiti Microsoft Foundry za dovršetak poziva. Ako ste zainteresirani, možete pročitati Phi-3 Cookbook da naučite kako pozivati Phi-3/3.5 Instruct, Vision, MoE putem Microsoft Foundry [Kliknite ovaj link](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst).


**NVIDIA NIM**

Osim cloud-based Microsoft Foundry Models kataloga, također možete koristiti [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) za dovršetak povezanih poziva. Možete posjetiti NVIDIA NIM za dovršetak API poziva Phi-3/3.5 obitelji. NVIDIA NIM (NVIDIA Inference Microservices) je skup ubrzanih mikroservisa za inferenciju dizajniranih da pomognu developerima učinkovito implementirati AI modele preko raznih okruženja, uključujući cloudove, podatkovne centre i radne stanice.

Evo nekoliko ključnih karakteristika NVIDIA NIM-a:

- **Jednostavnost implementacije:** NIM omogućuje implementaciju AI modela jednom naredbom, čineći lako integriranje u postojeće tokove rada.
- **Optimizirane performanse:** Koristi NVIDIA-in unaprijed optimizirane inferencijske motore, poput TensorRT i TensorRT-LLM, za osiguranje niske latencije i visokog protoka.
- **Skalabilnost:** NIM podržava autoskaliranje na Kubernetesu, omogućujući učinkovito rukovanje promjenjivim opterećenjima.
- **Sigurnost i kontrola:** Organizacije mogu održavati kontrolu nad svojim podacima i aplikacijama samostalnim hostanjem NIM mikroservisa na svojoj upravljanoj infrastrukturi.
- **Standardni API-ji:** NIM pruža industrijske standardne API-je, što olakšava izgradnju i integraciju AI aplikacija poput chatbota, AI asistenata i drugih.

NIM je dio NVIDIA AI Enterprise, koji ima za cilj pojednostaviti implementaciju i operacionalizaciju AI modela, osiguravajući njihovo učinkovito izvođenje na NVIDIA GPU-ima.

- Demo: Korištenje NVIDIA NIM za pozivanje Phi-3.5-Vision-API  [[Kliknite ovaj link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Pokretanje Phi-3/3.5 lokalno
Inferencija u vezi s Phi-3, ili bilo kojim jezičnim modelom poput GPT-3, odnosi se na proces generiranja odgovora ili predviđanja na temelju unosa koji prima. Kada date upit ili pitanje Phi-3, on koristi svoju treniranu neuronsku mrežu da izvede najvjerojatniji i relevantan odgovor analizirajući obrasce i odnose u podacima na kojima je treniran.

**Hugging Face Transformer**
Hugging Face Transformers je moćna biblioteka dizajnirana za obradu prirodnog jezika (NLP) i druge zadatke strojnog učenja. Evo nekih ključnih značajki:

1. **Unaprijed trenirani modeli**: Pruža tisuće unaprijed treniranih modela koji se mogu koristiti za različite zadatke poput klasifikacije teksta, prepoznavanja imenovanih entiteta, odgovaranja na pitanja, sažimanja, prevođenja i generiranja teksta.

2. **Interoperabilnost okvira**: Biblioteka podržava više okvira dubokog učenja, uključujući PyTorch, TensorFlow i JAX. To vam omogućuje treniranje modela u jednom okviru i korištenje u drugom.

3. **Multimodalne mogućnosti**: Osim NLP-a, Hugging Face Transformers podržava zadatke u računalnom vidu (npr. klasifikacija slika, detekcija objekata) i obradi zvuka (npr. prepoznavanje govora, klasifikacija zvuka).

4. **Jednostavnost korištenja**: Biblioteka nudi API-je i alate za lako preuzimanje i fino podešavanje modela, čineći je dostupnom i početnicima i stručnjacima.

5. **Zajednica i resursi**: Hugging Face ima živu zajednicu i opsežnu dokumentaciju, tutorijale i vodiče koji pomažu korisnicima da započnu i maksimalno iskoriste biblioteku.
[službena dokumentacija](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) ili njihov [GitHub repozitorij](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Ovo je najčešće korištena metoda, ali zahtijeva ubrzanje pomoću GPU-a. Na kraju krajeva, scenariji poput Vision i MoE zahtijevaju mnogo izračuna, što će na CPU-u biti vrlo sporo ako nisu kvantizirani.


- Demo: Korištenje Transformer za pozivanje Phi-3.5-Instruct [Kliknite ovaj link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Korištenje Transformer za pozivanje Phi-3.5-Vision [Kliknite ovaj link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Korištenje Transformer za pozivanje Phi-3.5-MoE [Kliknite ovaj link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) je platforma dizajnirana da olakša pokretanje velikih jezičnih modela (LLM) lokalno na vašem računalu. Podržava različite modele poput Llama 3.1, Phi 3, Mistral i Gemma 2, između ostalih. Platforma pojednostavljuje proces pakiranjem težina modela, konfiguracije i podataka u jedinstvenu cjelinu, čineći je pristupačnijom korisnicima za prilagodbu i stvaranje vlastitih modela. Ollama je dostupna za macOS, Linux i Windows. To je izvrstan alat ako želite eksperimentirati s LLM-ovima ili ih implementirati bez oslanjanja na oblačne usluge. Ollama je najizravniji način, samo trebate izvršiti sljedeću naredbu.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) je Microsoftov offline runtime na uređaju za pokretanje modela poput Phija u potpunosti na vašem hardveru - nije potrebna Azure pretplata, API ključ ni mrežna veza. Automatski odabire najbolji dostupan izvršni provider (NPU, GPU ili CPU) i pruža endpoint kompatibilan s OpenAI-jem, tako da postojeći `openai`/Azure AI Inference SDK kod može na njega usmjeriti s minimalnim promjenama. Pogledajte [Foundry Local dokumentaciju](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) za početak.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) je višekratni akcelerator za izvođenje i treniranje strojnog učenja. ONNX Runtime za Generative AI (GENAI) je moćan alat koji vam pomaže u učinkovitoj izvođenju generativnih AI modela na različitim platformama.

## Što je ONNX Runtime?
ONNX Runtime je open-source projekt koji omogućuje visokoučinkovitu inferenciju modela strojnog učenja. Podržava modele u Open Neural Network Exchange (ONNX) formatu, koji je standard za predstavljanje modela strojnog učenja. ONNX Runtime inference može omogućiti brža korisnička iskustva i niže troškove, podržavajući modele iz okvira dubokog učenja poput PyTorch i TensorFlow/Keras te klasične biblioteke strojnog učenja poput scikit-learn, LightGBM, XGBoost itd. ONNX Runtime je kompatibilan s različitim hardverom, upravljačkim programima i operativnim sustavima, i osigurava optimalne performanse koristeći hardverske akceleratore gdje je primjenjivo, uz optimizacije i transformacije grafova.

## Što je Generativna AI?
Generativna AI odnosi se na AI sustave koji mogu generirati novi sadržaj, poput teksta, slika ili glazbe, na temelju podataka na kojima su trenirani. Primjeri su jezični modeli poput GPT-3 i modeli za generiranje slika poput Stable Diffusion. ONNX Runtime za GenAI biblioteka pruža generativni AI ciklus za ONNX modele, uključujući inferenciju s ONNX Runtime-om, obradu logita, pretraživanje i uzorkovanje, te upravljanje KV cache-om.

## ONNX Runtime za GENAI
ONNX Runtime za GENAI proširuje mogućnosti ONNX Runtime-a kako bi podržao generativne AI modele. Evo nekih ključnih značajki:

- **Široka podrška platformi:** Radi na raznim platformama, uključujući Windows, Linux, macOS, Android i iOS.
- **Podrška modela:** Podržava mnoge popularne generativne AI modele, poput LLaMA, GPT-Neo, BLOOM i drugih.
- **Optimizacija performansi:** Uključuje optimizacije za različite hardverske akceleratore poput NVIDIA GPU-ova, AMD GPU-ova i više2.
- **Jednostavnost uporabe:** Pruža API-je za lako integriranje u aplikacije, omogućujući generiranje teksta, slika i drugog sadržaja uz minimalan kod.
- Korisnici mogu pozvati metodu generate() na visokoj razini ili pokrenuti svaku iteraciju modela u petlji, generirajući jedan token u isto vrijeme, te po želji ažurirati parametre generiranja unutar petlje.
- ONNX runtime također podržava greedy/beam pretraživanje i TopP, TopK uzorkovanje za generiranje nizova tokena i ugrađenu obradu logita poput penalizacija ponavljanja. Također lako možete dodati prilagođeno ocjenjivanje.

## Početak rada
Da biste započeli s ONNX Runtime za GENAI, možete slijediti ove korake:

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
### Demo: Korištenje ONNX Runtime GenAI za pozivanje Phi-3.5-Vision


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

Uz ONNX Runtime, Ollama i Foundry Local referentne metode, također možemo dovršiti referencu kvantitativnih modela na temelju referentnih metoda modela koje pružaju različiti proizvođači. Kao što su Apple MLX okvir s Apple Metal, Qualcomm QNN s NPU, Intel OpenVINO s CPU/GPU i drugi. Više sadržaja možete pronaći u [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Više

Naučili smo osnove obitelji Phi-3/3.5, ali za učenje više o SLM-u potrebna su dodatna znanja. Odgovore možete pronaći u Phi-3 Cookbook-u. Ako želite saznati više, posjetite [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->