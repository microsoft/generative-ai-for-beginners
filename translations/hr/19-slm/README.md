# Uvod u male jezične modele za generativnu umjetnu inteligenciju za početnike
Generativna umjetna inteligencija je fascinantno područje umjetne inteligencije koje se fokusira na stvaranje sustava sposobnih za generiranje novog sadržaja. Taj sadržaj može varirati od teksta i slika do glazbe, pa čak i čitavih virtualnih okruženja. Jedna od najuzbudljivijih primjena generativne umjetne inteligencije nalazi se u području jezičnih modela.

## Što su mali jezični modeli?

Mali jezični model (SLM) predstavlja smanjenu varijantu velikog jezičnog modela (LLM), koristeći mnoge arhitektonske principe i tehnike LLM-ova, uz značajno smanjen računalni otisak.

SLM-ovi su podskup jezičnih modela dizajniranih za generiranje teksta nalik ljudskom. Za razliku od njihovih većih kolega, poput GPT-4, SLM-ovi su kompaktniji i učinkovitiji, što ih čini idealnima za aplikacije gdje su računalni resursi ograničeni. Unatoč njihovoj manjoj veličini, oni i dalje mogu obavljati razne zadatke. Tipično se SLM-ovi konstruiraju kompresijom ili destilacijom LLM-ova, s ciljem zadržavanja značajnog dijela funkcionalnosti i jezičnih sposobnosti izvornog modela. Ovo smanjenje veličine modela smanjuje ukupnu složenost, čineći SLM-ove učinkovitijima u pogledu korištenja memorije i računalnih zahtjeva. Unatoč ovim optimizacijama, SLM-ovi i dalje mogu obavljati širok spektar zadataka obrade prirodnog jezika (NLP):

- Generiranje teksta: Stvaranje koherentnih i kontekstualno prikladnih rečenica ili odlomaka.
- Dovršavanje teksta: Predviđanje i dovršavanje rečenica na temelju danog upita.
- Prevođenje: Prevođenje teksta s jednog jezika na drugi.
- Sažimanje: Sažimanje dugih tekstova u kraće, lakše probavljive sažetke.

Iako s određenim kompromisima u izvedbi ili dubini razumijevanja u usporedbi s njihovim većim kolegama.

## Kako mali jezični modeli rade?
SLM-ovi se treniraju na ogromnim količinama tekstualnih podataka. Tijekom treninga uče obrasce i strukture jezika, što im omogućuje generiranje teksta koji je gramatički ispravan i kontekstualno prikladan. Proces treninga uključuje:

- Prikupljanje podataka: Prikupljanje velikih skupova tekstualnih podataka iz različitih izvora.
- Predobrada: Čišćenje i organizaciju podataka kako bi bili prikladni za trening.
- Trening: Korištenje algoritama strojnog učenja za učenje modela kako razumjeti i generirati tekst.
- Fine-tuning: Prilagodbu modela radi poboljšanja izvedbe na specifičnim zadacima.

Razvoj SLM-ova usklađen je s rastućom potrebom za modelima koji se mogu implementirati u okruženjima s ograničenim resursima, poput mobilnih uređaja ili edge računalnih platformi, gdje potpuni LLM-ovi mogu biti nepraktični zbog svojih velikih zahtjeva za resursima. Fokusirajući se na učinkovitost, SLM-ovi balansiraju između izvedbe i pristupačnosti, omogućujući širu primjenu u raznim područjima.

![slm](../../../translated_images/hr/slm.4058842744d0444a.webp)

## Ciljevi učenja

U ovoj lekciji nastojimo predstaviti znanje o SLM-ovima i povezati ga s Microsoft Phi-3 kako bismo naučili različite scenarije u tekstualnom sadržaju, viziji i MoE.

Na kraju ove lekcije trebali biste moći odgovoriti na sljedeća pitanja:

- Što je SLM?
- Koja je razlika između SLM-a i LLM-a?
- Što je Microsoft Phi-3/3.5 obitelj?
- Kako izvršiti inferenciju s Microsoft Phi-3/3.5 obitelji?

Spremni? Krenimo.

## Razlike između velikih jezičnih modela (LLM) i malih jezičnih modela (SLM)

I LLM-ovi i SLM-ovi temelje se na osnovnim principima probabilističkog strojnog učenja, prateći slične pristupe u arhitektonskom dizajnu, metodologiji treninga, procesima generiranja podataka i tehnikama evaluacije modela. Međutim, nekoliko ključnih čimbenika razlikuju ove dvije vrste modela.

## Primjene malih jezičnih modela

SLM-ovi imaju širok spektar primjena, uključujući:

- Chatbotovi: Pružanje korisničke podrške i interakcija s korisnicima na konverzacijski način.
- Kreiranje sadržaja: Pomoć piscima u generiranju ideja ili čak u izradi čitavih članaka.
- Obrazovanje: Pomoć studentima u pisanju zadataka ili učenju novih jezika.
- Pristupačnost: Kreiranje alata za osobe s invaliditetom, poput sustava za pretvaranje teksta u govor.

**Veličina**
  
Primarna razlika između LLM-ova i SLM-ova leži u veličini modela. LLM-ovi, poput ChatGPT-a (GPT-4), mogu sadržavati procijenjenih 1,76 bilijuna parametara, dok su open-source SLM-ovi poput Mistral 7B dizajnirani sa značajno manjim brojem parametara — otprilike 7 milijardi. Ova razlika prvenstveno proizlazi iz razlika u arhitekturi modela i procesima treninga. Na primjer, ChatGPT koristi mehanizam samo-pažnje unutar encoder-decoder okvira, dok Mistral 7B koristi sliding window pažnju koja omogućava učinkovitiji trening unutar modela samo s decoderom. Ova arhitektonska razlika ima duboke implikacije na složenost i izvedbu ovih modela.

**Razumijevanje**

SLM-ovi su tipično optimizirani za izvedbu unutar specifičnih domena, čineći ih vrlo specijaliziranima, ali potencijalno ograničenima u njihovoj sposobnosti pružanja širokog kontekstualnog razumijevanja preko više područja znanja. Nasuprot tome, LLM-ovi nastoje simulirati inteligenciju nalik ljudskoj na sveobuhvatnijoj razini. Trenirani na ogromnim i raznolikim skupovima podataka, LLM-ovi su dizajnirani za dobru izvedbu u raznim domenama, nudeći veću svestranost i prilagodljivost. Posljedično, LLM-ovi su prikladniji za širi spektar zadataka, poput obrade prirodnog jezika i programiranja.

**Računalna snaga**

Trening i implementacija LLM-ova su procesi koji zahtijevaju velike resurse, često uključujući značajnu računalnu infrastrukturu, uključujući velike GPU klastere. Na primjer, treniranje modela poput ChatGPT-a od nule može zahtijevati tisuće GPU-a tijekom dugog vremenskog razdoblja. Nasuprot tome, SLM-ovi s manjim brojem parametara su pristupačniji u smislu računalnih resursa. Modeli poput Mistral 7B mogu se trenirati i koristiti na lokalnim računalima opremljenim umjerenim GPU sposobnostima, iako trening i dalje zahtijeva nekoliko sati preko više GPU-a.

**Pristranost**

Pristranost je poznat problem kod LLM-ova, prvenstveno zbog prirode trening podataka. Ti modeli često se oslanjaju na sirove, javno dostupne podatke s interneta, koji mogu nedovoljno ili pogrešno zastupati određene skupine, uvoditi netočne oznake ili odražavati jezične pristranosti uzrokovane dijalektom, geografskim varijacijama i gramatičkim pravilima. Dodatno, složenost arhitektura LLM-ova može nenamjerno pogoršati pristranost, koja može ostati neprimijećena bez pažljivog podešavanja. S druge strane, SLM-ovi, trenirani na ograničenijim, domenski specifičnim skupovima podataka, inherentno su manje podložni takvim pristranostima, iako nisu potpuno imuni.

**Inferencija**

Smanjena veličina SLM-ova pruža im značajnu prednost u brzini inferencije, omogućujući efikasno generiranje izlaza na lokalnom hardveru bez potrebe za opsežnim paralelnim procesiranjem. Nasuprot tome, LLM-ovi zbog svoje veličine i složenosti često zahtijevaju značajne paralelne računalne resurse za postizanje prihvatljivog vremena inferencije. Prisustvo više istodobnih korisnika dodatno usporava vrijeme odgovora LLM-ova, posebno kada su implementirani u velikom opsegu.

Ukratko, iako LLM-ovi i SLM-ovi dijele temeljnu osnovu u strojnome učenju, značajno se razlikuju u veličini modela, zahtjevima za resursima, razumijevanju konteksta, osjetljivosti na pristranost i brzini inferencije. Te razlike odražavaju njihovu prikladnost za različite upotrebe, pri čemu su LLM-ovi svestraniji ali zahtjevniji za resurse, dok SLM-ovi nude veću učinkovitost usmjerenu na domene uz smanjene računalne zahtjeve.

***Napomena: U ovoj lekciji predstavit ćemo SLM koristeći Microsoft Phi-3 / 3.5 kao primjer.***

## Predstavljanje obitelji Phi-3 / Phi-3.5

Obitelj Phi-3 / 3.5 usmjerena je uglavnom na scenarije primjene u tekstu, viziji i agentima (MoE):

### Phi-3 / 3.5 Instruct

Glavnom za generiranje teksta, dovršavanje razgovora i ekstrakciju informacija iz sadržaja, itd.

**Phi-3-mini**

Jezični model od 3.8 milijardi parametara dostupan je na Microsoft Foundry, Hugging Face i Ollama. Phi-3 modeli značajno nadmašuju jezične modele iste i veće veličine na ključnim testovima (pogledajte brojeve na benchmarku dolje, veći brojevi znače bolju izvedbu). Phi-3-mini nadmašuje modele dvostruke veličine, dok Phi-3-small i Phi-3-medium nadmašuju veće modele, uključujući GPT-3.5.

**Phi-3-small & medium**

Sa samo 7 milijardi parametara, Phi-3-small nadmašuje GPT-3.5T na raznim testovima jezika, rezoniranja, kodiranja i matematike.

Phi-3-medium s 14 milijardi parametara nastavlja ovaj trend i nadmašuje Gemini 1.0 Pro.

**Phi-3.5-mini**

Možemo ga smatrati nadogradnjom Phi-3-mini. Iako broj parametara ostaje nepromijenjen, poboljšava sposobnost podrške za više jezika (podržava više od 20 jezika: arapski, kineski, češki, danski, nizozemski, engleski, finski, francuski, njemački, hebrejski, mađarski, talijanski, japanski, korejski, norveški, poljski, portugalski, ruski, španjolski, švedski, tajlandski, turski, ukrajinski) i dodaje snažniju podršku za dug kontekst.

Phi-3.5-mini s 3.8 milijardi parametara nadmašuje jezične modele iste veličine i usporediv je s modelima dvostruke veličine.

### Phi-3 / 3.5 Vision

Možemo model Instruct Phi-3/3.5 smatrati Phi-ovom sposobnošću razumijevanja, a Vision je ono što daje Phi-ju oči da razumije svijet.


**Phi-3-Vision**

Phi-3-vision, sa samo 4.2 milijarde parametara, nastavlja ovaj trend i nadmašuje veće modele kao što su Claude-3 Haiku i Gemini 1.0 Pro V na zadacima općeg vizualnog rezoniranja, OCR-u te razumijevanju tablica i dijagrama.


**Phi-3.5-Vision**

Phi-3.5-Vision je također nadogradnja Phi-3-Vision, dodajući podršku za višestruke slike. Možete ga smatrati poboljšanjem vida, ne samo da vidi slike, već i videozapise.

Phi-3.5-vision nadmašuje veće modele poput Claude-3.5 Sonnet i Gemini 1.5 Flash u OCR-u, razumijevanju tablica i grafikona te je usporediv na zadacima općeg vizualnog rezoniranja. Podržava višekadarni unos, tj. izvršava rezoniranje na više ulaznih slika.


### Phi-3.5-MoE

***Mišavina stručnjaka (MoE)*** omogućava modelima da budu prethodno trenirani s puno manjim računalnim zahtjevima, što znači da možete dramatično povećati veličinu modela ili skupa podataka s istim računalnim budžetom kao i gusto povezani model. Konkretno, MoE model trebao bi brže tijekom pretreninga postići istu kvalitetu kao i njegov gusto povezani pandan.

Phi-3.5-MoE se sastoji od 16x3.8B stručnjaka modula. Phi-3.5-MoE s samo 6.6 milijardi aktivnih parametara postiže sličnu razinu rezoniranja, razumijevanja jezika i matematike kao značajno veći modeli.

Možemo koristiti model Phi-3/3.5 obitelji temeljen na različitim scenarijima. Za razliku od LLM-a, Phi-3/3.5-mini ili Phi-3/3.5-Vision možete implementirati na edge uređajima.


## Kako koristiti modele Phi-3/3.5 obitelji

Nadamo se da ćemo koristiti Phi-3/3.5 u različitim scenarijima. Sljedeće ćemo koristiti Phi-3/3.5 na temelju različitih scenarija.

![phi3](../../../translated_images/hr/phi3.655208c3186ae381.webp)

### Izvršavanje inferencije putem Cloud API-ja

**Microsoft Foundry modeli**

> **Napomena:** GitHub modeli se ukidaju krajem srpnja 2026. [Microsoft Foundry modeli](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) su izravna zamjena.

Microsoft Foundry modeli su najizravniji način. Brzo možete pristupiti Phi-3/3.5-Instruct modelu putem kataloga Foundry modela. U kombinaciji s Azure AI Inference SDK / OpenAI SDK, možete pristupiti API-ju kroz kod za dovršetak poziva Phi-3/3.5-Instruct. Također možete isprobati različite učinke putem Playground-a.

- Demo: Usporedba učinaka Phi-3-mini i Phi-3.5-mini u kineskim scenarijima

![phi3](../../../translated_images/hr/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/hr/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Ili, ako želimo koristiti modele za vid i MoE, možemo koristiti Microsoft Foundry za dovršetak poziva. Ako ste zainteresirani, možete pročitati Phi-3 Cookbook kako biste naučili kako pozvati Phi-3/3.5 Instruct, Vision, MoE putem Microsoft Foundry [Kliknite ovaj link](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Osim kataloga Microsoft Foundry modela baziranih na oblaku, također možete koristiti [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) za dovršetak povezanih poziva. Možete posjetiti NVIDIA NIM za izvršavanje API poziva obitelji Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) je skup ubrzanih mikrousluga za inferenciju dizajniranih da pomognu programerima učinkovitije implementirati AI modele u različitim okruženjima, uključujući oblak, podatkovne centre i radne stanice.

Evo nekih ključnih značajki NVIDIA NIM-a:

- **Jednostavnost implementacije:** NIM omogućuje implementaciju AI modela jednom naredbom, što ga čini jednostavnim za integraciju u postojeće radne tokove.

- **Optimizirana izvedba:** Iskorištava unaprijed optimizirane NVIDIA inferencijske motore, poput TensorRT i TensorRT-LLM, kako bi osigurala nisko kašnjenje i visok protok.
- **Skalabilnost:** NIM podržava automatsko skaliranje na Kubernetesu, omogućujući učinkovito upravljanje promjenjivim opterećenjima.
- **Sigurnost i kontrola:** Organizacije mogu održavati kontrolu nad svojim podacima i aplikacijama samostalnim hostanjem NIM mikroservisa na svojoj upravljanoj infrastrukturi.
- **Standardni API-jevi:** NIM pruža industrijske standardne API-jeve, što olakšava izgradnju i integraciju AI aplikacija poput chatbota, AI asistenata i drugih.

NIM je dio NVIDIA AI Enterprise, što ima za cilj pojednostaviti implementaciju i operacionalizaciju AI modela, osiguravajući njihovo učinkovito izvođenje na NVIDIA GPU-ima.

- Demo: Korištenje NVIDIA NIM za pozivanje Phi-3.5-Vision-API [[Klikni na ovaj link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Pokretanje Phi-3/3.5 lokalno
Inferencija u vezi s Phi-3, ili bilo kojim jezičnim modelom poput GPT-3, odnosi se na proces generiranja odgovora ili predviđanja na temelju unosa koji prima. Kada Phi-3 date upit ili pitanje, koristi svoj trenirani neuronski mrežni model za zaključivanje najvjerojatnijeg i relevantnog odgovora analizirajući obrasce i odnose u podacima na kojima je treniran.

**Hugging Face Transformer**
Hugging Face Transformers je moćna biblioteka dizajnirana za obradu prirodnog jezika (NLP) i druge zadatke strojnog učenja. Evo nekoliko ključnih točaka:

1. **Prethodno trenirani modeli:** Pruža tisuće prethodno treniranih modela koji se mogu koristiti za različite zadatke poput klasifikacije teksta, prepoznavanja imenovanih entiteta, odgovaranja na pitanja, sažimanja, prevođenja i generiranja teksta.

2. **Interoperabilnost okvira:** Biblioteka podržava više dubokih okvira za učenje, uključujući PyTorch, TensorFlow i JAX. Ovo vam omogućuje treniranje modela u jednom okviru i korištenje u drugom.

3. **Multimodalne sposobnosti:** Osim NLP-a, Hugging Face Transformers također podržava zadatke u računalnom vidu (npr. klasifikacija slika, detekcija objekata) i obradi zvuka (npr. prepoznavanje govora, klasifikacija zvuka).

4. **Jednostavnost upotrebe:** Biblioteka nudi API-je i alate za jednostavno preuzimanje i fino podešavanje modela, čineći ju dostupnom i za početnike i za stručnjake.

5. **Zajednica i resursi:** Hugging Face ima aktivnu zajednicu i opsežnu dokumentaciju, tutorijale i vodiče koji pomažu korisnicima da započnu i maksimalno iskoriste biblioteku.
[službena dokumentacija](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) ili njihov [GitHub repozitorij](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Ovo je najčešće korištena metoda, no također zahtijeva GPU ubrzanje. Uostalom, scenariji poput Vision i MoE zahtijevaju mnogo proračuna, što će biti vrlo sporo na CPU-u ako nisu kvantizirani.


- Demo: Korištenje Transformera za pozivanje Phi-3.5-Instruct [Klikni na ovaj link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Korištenje Transformera za pozivanje Phi-3.5-Vision [Klikni na ovaj link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Korištenje Transformera za pozivanje Phi-3.5-MoE [Klikni na ovaj link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) je platforma dizajnirana da olakša pokretanje velikih jezičnih modela (LLM) lokalno na vašem računalu. Podržava razne modele poput Llama 3.1, Phi 3, Mistral i Gemma 2, među ostalima. Platforma pojednostavljuje proces tako što spaja težine modela, konfiguraciju i podatke u jedan paket, čineći ju dostupnijom korisnicima za prilagodbu i izradu vlastitih modela. Ollama je dostupna za macOS, Linux i Windows. Sjajan je alat ako želite eksperimentirati ili implementirati LLM-ove bez oslanjanja na oblak. Ollama je najizravniji put, samo trebate izvršiti sljedeću naredbu.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) je Microsoftova off-line izvedba na uređaju za pokretanje modela poput Phi u potpunosti na vašem hardveru - nije potrebna pretplata na Azure, API ključ ili mrežna veza. Automatski bira najbolji dostupni izvršni pružatelj (NPU, GPU ili CPU) i izlaže OpenAI-kompatibilnu točku pristupa, tako da postojeći `openai`/Azure AI Inference SDK kod može ciljati na nju uz minimalne promjene. Pogledajte [Foundry Local dokumentaciju](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) za početak.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) je međuplatformski akcelerator za inferenciju i treniranje strojnog učenja. ONNX Runtime za Generative AI (GENAI) je moćan alat koji vam pomaže efikasno pokretati generativne AI modele na raznim platformama.

## Što je ONNX Runtime?
ONNX Runtime je projekt otvorenog koda koji omogućuje visoko-performantnu inferenciju modela strojnog učenja. Podržava modele u Open Neural Network Exchange (ONNX) formatu, koji je standard za predstavljanje modela strojnog učenja. ONNX Runtime inferencija može omogućiti brža korisnička iskustva i niže troškove, podržavajući modele dubokog učenja iz okvira poput PyTorch i TensorFlow/Keras kao i klasične biblioteke strojnog učenja poput scikit-learn, LightGBM, XGBoost, itd. ONNX Runtime je kompatibilan s različitim hardverom, drajverima i operativnim sustavima, te pruža optimalnu izvedbu iskorištavanjem hardverskih akceleratora kad je to moguće, zajedno s optimizacijama i transformacijama grafova.

## Što je Generativna AI?
Generativna AI odnosi se na AI sustave koji mogu generirati novi sadržaj, poput teksta, slika ili glazbe, na temelju podataka na kojima su trenirani. Primjeri uključuju jezične modele poput GPT-3 i modele za generiranje slika poput Stable Diffusion. ONNX Runtime za GenAI biblioteka pruža generativni AI ciklus za ONNX modele, uključujući inferenciju s ONNX Runtime, obradu logita, pretraživanje i uzorkovanje te upravljanje KV kešom.

## ONNX Runtime za GENAI
ONNX Runtime za GENAI proširuje mogućnosti ONNX Runtime-a kako bi podržao generativne AI modele. Evo nekoliko ključnih značajki:

- **Široka podrška platformi:** Radi na raznim platformama, uključujući Windows, Linux, macOS, Android i iOS.
- **Podrška modelima:** Podržava mnoge popularne generativne AI modele, poput LLaMA, GPT-Neo, BLOOM i drugih.
- **Optimizacija izvedbe:** Uključuje optimizacije za različite hardverske akceleratore poput NVIDIA GPU-a, AMD GPU-a i drugih.
- **Jednostavnost upotrebe:** Pruža API-je za jednostavnu integraciju u aplikacije, omogućujući generiranje teksta, slika i drugog sadržaja uz minimalan kod.
- Korisnici mogu pozvati visokonivometod generate(), ili pokretati svaku iteraciju modela u petlji, generirajući jedan token odjednom i po želji ažurirajući parametre generiranja unutar petlje.
- ONNX runtime također podržava greedy/beam search i TopP, TopK uzorkovanje za generiranje niza tokena i ugrađenu obradu logita poput penalizacija ponavljanja. Također se lako može dodati prilagođeno ocjenjivanje.

## Početak
Za početak rada s ONNX Runtime za GENAI slijedite ove korake:

### Instalirajte ONNX Runtime:
```Python
pip install onnxruntime
```
### Instalirajte ekstenzije za Generative AI:
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

Osim referentnih metoda ONNX Runtime, Ollama i Foundry Local, možemo i dopuniti referencu kvantitativnih modela bazirano na referentnim metodama modela koje pružaju različiti proizvođači. Kao što su Apple MLX framework s Apple Metal, Qualcomm QNN s NPU, Intel OpenVINO s CPU/GPU i sl. Više sadržaja možete pronaći u [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Više

Naučili smo osnove Phi-3/3.5 obitelji, ali za dublje razumijevanje SLM-a potrebne su dodatne spoznaje. Odgovore možete pronaći u Phi-3 Cookbook-u. Ako želite saznati više, posjetite [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->