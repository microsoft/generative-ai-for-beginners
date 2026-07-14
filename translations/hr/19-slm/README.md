# Uvod u Male Jezične Modele za Generativnu AI za Početnike
Generativna AI je fascinantno polje umjetne inteligencije koje se fokusira na stvaranje sustava sposobnih za generiranje novog sadržaja. Taj sadržaj može biti od teksta i slika do glazbe pa čak i čitavih virtualnih okruženja. Jedna od najuzbudljivijih primjena generativne AI nalazi se u području jezičnih modela.

## Što su Mali Jezični Modeli?

Mali jezični model (SLM) predstavlja smanjenu varijantu velikog jezičnog modela (LLM), koristeći mnoge arhitektonske principe i tehnike LLM-ova, dok pokazuje značajno smanjen računarski otisak.

SLM-ovi su podskup jezičnih modela dizajniranih za generiranje teksta sličnog ljudskom. Za razliku od svojih većih kolega poput GPT-4, SLM-ovi su kompaktniji i učinkovitiji, što ih čini idealnima za primjene gdje su računalni resursi ograničeni. Unatoč manjoj veličini, mogu obavljati razne zadatke. Obično se SLM-ovi konstruiraju komprimirajući ili destilirajući LLM-ove, nastojeći zadržati značajan dio originalne funkcionalnosti i jezičnih sposobnosti modela. Ovo smanjenje veličine modela smanjuje ukupnu složenost, čineći SLM-ove učinkovitijima u pogledu korištenja memorije i računalnih zahtjeva. Unatoč ovim optimizacijama, SLM-ovi mogu obavljati širok spektar zadataka obrade prirodnog jezika (NLP):

- Generiranje teksta: Stvaranje koherentnih i kontekstualno relevantnih rečenica ili odlomaka.
- Dovršavanje teksta: Predviđanje i dovršavanje rečenica na temelju danog upita.
- Prevođenje: Pretvaranje teksta s jednog jezika na drugi.
- Sažimanje: Sažimanje dugih tekstova u kraće, preglednije sažetke.

Iako uz određene kompromise u izvedbi ili dubini razumijevanja u usporedbi s njihovim većim kolegama.

## Kako Male Jezične Modele Funkcioniraju?
SLM-ovi se treniraju na ogromnim količinama tekstualnih podataka. Tijekom treniranja, uče obrasce i strukture jezika, omogućujući im generiranje teksta koji je gramatički ispravan i kontekstualno prikladan. Proces treniranja uključuje:

- Prikupljanje podataka: Sakupljanje velikih skupova tekstualnih podataka iz različitih izvora.
- Predobrada: Čišćenje i organiziranje podataka kako bi bili prikladni za treniranje.
- Treniranje: Korištenje algoritama strojnog učenja za učenje modela razumijevanja i generiranja teksta.
- Fino podešavanje: Prilagođavanje modela radi poboljšanja njegovih performansi na specifičnim zadacima.

Razvoj SLM-ova usklađen je s rastućom potrebom za modelima koji se mogu implementirati u okruženjima s ograničenim resursima, poput mobilnih uređaja ili rubnih računalnih platformi, gdje široki LLM-ovi mogu biti nepraktični zbog svojih velikih zahtjeva za resursima. Fokusujući se na učinkovitost, SLM-ovi uravnotežuju performanse i pristupačnost, omogućujući širu primjenu u različitim područjima.

![slm](../../../translated_images/hr/slm.4058842744d0444a.webp)

## Ciljevi Učenja

U ovom ćemo lekciji predstaviti znanje o SLM-ovima i kombinirati ga s Microsoft Phi-3 kako bismo naučili različite scenarije u tekstualnom sadržaju, viziji i MoE.

Do kraja ove lekcije trebali biste moći odgovoriti na sljedeća pitanja:

- Što je SLM?
- Koja je razlika između SLM i LLM?
- Što je Microsoft Phi-3/3.5 obitelj?
- Kako pokrenuti inferencu s Microsoft Phi-3/3.5 obitelji?

Spremni? Krenimo.

## Razlike između Velikih jezičnih Modela (LLM) i Malih Jezičnih Modela (SLM)

I LLM-ovi i SLM-ovi izgrađeni su na temeljnim principima probabilističkog strojnog učenja, slijedeći slične pristupe u arhitektonskom dizajnu, metodologijama treninga, procesima generiranja podataka i tehnikama evaluacije modela. Međutim, nekoliko ključnih čimbenika razlikuje ove dvije vrste modela.

## Primjene Malih Jezičnih Modela

SLM-ovi imaju širok spektar primjena, uključujući:

- Chatbotovi: Pružanje korisničke podrške i angažiranje korisnika u konverzacijskom obliku.
- Kreiranje sadržaja: Pomoć piscima generiranjem ideja ili čak izradom cijelih članaka.
- Obrazovanje: Pomoć studentima pri pisanju zadataka ili učenju novih jezika.
- Pristupačnost: Izrada alata za osobe s invaliditetom, poput sustava pretvorbe teksta u govor.

**Veličina**
  
Primarna je razlika između LLM-ova i SLM-ova u veličini modela. LLM-ovi, poput ChatGPT-a (GPT-4), mogu sadržavati procijenjenih 1,76 bilijuna parametara, dok open-source SLM-ovi poput Mistral 7B imaju znatno manji broj parametara — oko 7 milijardi. Ova razlika uglavnom proizlazi iz razlika u arhitekturi modela i procesima treniranja. Na primjer, ChatGPT koristi mehanizam samopozornosti unutar okvira enkoder-dekoder, dok Mistral 7B koristi pozornost s pokretnim prozorom, što omogućuje učinkovitije treniranje unutar samo-dekoder modela. Ova arhitektonska varijacija ima duboke implikacije na složenost i performanse ovih modela.

**Razumijevanje**

SLM-ovi su obično optimizirani za izvedbu unutar određenih domena, čineći ih vrlo specijaliziranim, ali potencijalno ograničenim u mogućnosti pružanja širokog kontekstualnog razumijevanja u više područja znanja. Nasuprot tome, LLM-ovi nastoje simulirati ljudsku inteligenciju na sveobuhvatnijoj razini. Osposobljeni na ogromnim, raznolikim skupovima podataka, LLM-ovi su dizajnirani da dobro funkcioniraju u različitim domenama, nudeći veću svestranost i prilagodljivost. Posljedično, LLM-ovi su prikladniji za širi raspon zadataka, poput obrade prirodnog jezika i programiranja.

**Računarstvo**

Treniranje i implementacija LLM-ova zahtijevaju velike resurse, često zahtijevajući značajnu računalnu infrastrukturu, uključujući velike GPU klastere. Na primjer, treniranje modela poput ChatGPT-a od početka može zahtijevati tisuće GPU-a tijekom dugih razdoblja. Nasuprot tome, SLM-ovi, sa svojim manjim brojem parametara, dostupniji su u smislu računalnih resursa. Modeli poput Mistral 7B mogu se trenirati i pokretati na lokalnim računalima opremljenim umjerenim GPU kapacitetima, iako treniranje još uvijek traži nekoliko sati na više GPU-a.

**Pristranost**

Pristranost je poznat problem u LLM-ovima, uglavnom zbog prirode trening podataka. Ovi modeli često se oslanjaju na sirove, otvoreno dostupne podatke s interneta, koji mogu podzastupljivati ili pogrešno predstavljati određene skupine, uvesti pogrešne oznake ili odražavati jezične pristranosti pod utjecajem dijalekata, geografske varijacije i gramatičkih pravila. Nadalje, složenost LLM arhitektura može nenamjerno pojačati pristranost, koja može proći nezapaženo bez pažljivog fino podešavanja. S druge strane, SLM-ovi, budući da su trenirani na ograničenijim, domen-specifičnim skupovima podataka, inherentno su manje podložni takvim pristranostima, iako nisu imuni na njih.

**Inferencija**

Manja veličina SLM-ova pruža im značajnu prednost u brzini inferencije, omogućujući efikasno generiranje izlaza na lokalnom hardveru bez potrebe za opsežnim paralelnim procesiranjem. Nasuprot tome, LLM-ovi zbog svoje veličine i složenosti često zahtijevaju znatne paralelne računalne resurse da bi postigli prihvatljivo vrijeme inferencije. Prisustvo više istodobnih korisnika dodatno usporava vrijeme odziva LLM-ova, osobito kada se implementiraju na velikoj skali.

Ukratko, iako LLM-ovi i SLM-ovi dijele temeljnu osnovu u strojnome učenju, oni se značajno razlikuju po veličini modela, zahtjevima za resursima, razumijevanju konteksta, osjetljivosti na pristranost i brzini inferencije. Te razlike odražavaju njihovu prikladnost za različite slučajeve uporabe, gdje su LLM-ovi svestraniji, ali zahtjevniji za resurse, a SLM-ovi nude veću učinkovitost za specifične domene s manjim računalnim zahtjevima.

***Napomena: U ovoj lekciji ćemo predstaviti SLM koristeći Microsoft Phi-3 / 3.5 kao primjer.***

## Predstavljanje Phi-3 / Phi-3.5 Obitelji

Phi-3 / 3.5 obitelj prvenstveno cilja tekstualne, vizualne i Agent (MoE) aplikacijske scenarije:

### Phi-3 / 3.5 Instruct

Prvenstveno za generiranje teksta, dovršavanje razgovora i izdvajanje informacija iz sadržaja itd.

**Phi-3-mini**

Jezični model od 3,8 milijardi dostupan je na Microsoft Foundry, Hugging Face i Ollama. Phi-3 modeli značajno nadmašuju jezične modele iste ili veće veličine na ključnim mjerilima (vidi brojeve mjerila ispod, veći brojevi su bolji). Phi-3-mini nadmašuje modele dvostruke veličine, dok Phi-3-small i Phi-3-medium nadmašuju veće modele, uključujući GPT-3.5.

**Phi-3-small & medium**

Sa samo 7 milijardi parametara, Phi-3-small pobjeđuje GPT-3.5T na raznim mjerilima za jezik, rezoniranje, kodiranje i matematiku.

Phi-3-medium s 14 milijardi parametara nastavlja ovaj trend i nadmašuje Gemini 1.0 Pro.

**Phi-3.5-mini**

Možemo ga smatrati nadogradnjom Phi-3-mini. Iako parametri ostaju nepromijenjeni, poboljšava sposobnost podrške više jezika (podržava 20+ jezika: arapski, kineski, češki, danski, nizozemski, engleski, finski, francuski, njemački, hebrejski, mađarski, talijanski, japanski, korejski, norveški, poljski, portugalski, ruski, španjolski, švedski, tajlandski, turski, ukrajinski) ​​i dodaje snažniju podršku za dugu kontekstualnost.

Phi-3.5-mini s 3,8 milijardi parametara nadmašuje jezične modele iste veličine i izjednačen je s modelima dvostruke veličine.

### Phi-3 / 3.5 Vision

Možemo promatrati Instruct model Phi-3/3.5 kao sposobnost Phi-ja za razumijevanje, dok je Vision ono što Phi-ju daje oči da razumije svijet.


**Phi-3-Vision**

Phi-3-vision, sa samo 4,2 milijarde parametara, nastavlja ovaj trend i nadmašuje veće modele kao što su Claude-3 Haiku i Gemini 1.0 Pro V na općim zadacima vizualnog rezoniranja, OCR-u te razumijevanju tablica i dijagrama.


**Phi-3.5-Vision**

Phi-3.5-Vision također je nadogradnja Phi-3-Vision, dodajući podršku za više slika. To možemo smatrati poboljšanjem u vidu, sada ne samo da možete vidjeti slike, nego i videozapise.

Phi-3.5-vision nadmašuje veće modele poput Claude-3.5 Sonnet i Gemini 1.5 Flash u zadacima OCR-a, razumijevanju tablica i grafikona, te je na razini u općim zadacima vizualnog znanja i rezoniranja. Podržava ulaz s više okvira, tj. izvršavanje rezoniranja na više ulaznih slika.


### Phi-3.5-MoE

***Mišavina Eksperata (MoE)*** omogućava modelima da se unaprijede s mnogo manje računanja, što znači da možete dramatično povećati veličinu modela ili skupa podataka s istim proračunom za računanje kao i gusti model. Konkretno, MoE model bi trebao postići istu kvalitetu kao njegov gusto povezani pandan mnogo brže tijekom prettreniranja.

Phi-3.5-MoE sastoji se od 16x3.8B ekspertskih modula. Phi-3.5-MoE s samo 6,6 milijardi aktivnih parametara postiže sličan nivo rezoniranja, razumijevanja jezika i matematike kao mnogo veći modeli.

Možemo koristiti Phi-3/3.5 obiteljski model u različitim scenarijima. Za razliku od LLM-a, Phi-3/3.5-mini ili Phi-3/3.5-Vision možete implementirati na rubnim uređajima.


## Kako koristiti modele obitelji Phi-3/3.5

Nadamo se koristiti Phi-3/3.5 u različitim scenarijima. Sljedeće ćemo koristiti Phi-3/3.5 u različitim scenarijima.

![phi3](../../../translated_images/hr/phi3.655208c3186ae381.webp)

### Inference putem Cloud API-ja

**Microsoft Foundry Modeli**

> **Napomena:** GitHub modeli prestaju s radom krajem srpnja 2026. [Microsoft Foundry modeli](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) su njihova izravna zamjena.

Microsoft Foundry modeli su najizravniji način. Možete brzo pristupiti Phi-3/3.5-Instruct modelu putem kataloga Foundry modela. U kombinaciji s Azure AI Inference SDK / OpenAI SDK, možete pristupiti API-ju putem koda za dovršavanje Phi-3/3.5-Instruct poziva. Također možete testirati različite učinke putem Playgrounda.

- Demo: Usporedba učinaka Phi-3-mini i Phi-3.5-mini u kineskim scenarijima

![phi3](../../../translated_images/hr/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/hr/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Ili ako želimo koristiti modele za vid i MoE, možemo koristiti Microsoft Foundry za dovršetak poziva. Ako ste zainteresirani, možete pročitati Phi-3 Cookbook kako biste naučili kako pozivati Phi-3/3.5 Instruct, Vision, MoE kroz Microsoft Foundry [Kliknite ovaj link](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Osim kataloga Microsoft Foundry modela u oblaku, također možete koristiti [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) za dovršetak povezanih poziva. Možete posjetiti NVIDIA NIM za dovršetak API poziva Phi-3/3.5 obitelji. NVIDIA NIM (NVIDIA Inference Microservices) je skup pospješenih mikrousluga za inferenciju dizajniranih da pomognu programerima efikasno implementirati AI modele u različitim okruženjima, uključujući oblake, podatkovne centre i radne stanice.

Evo nekoliko ključnih značajki NVIDIA NIM-a:

- **Jednostavnost implementacije:** NIM omogućava implementaciju AI modela s jednom naredbom, što ga čini jednostavnim za integraciju u postojeće radne tokove.

- **Optimizirana izvedba:** Iskorištava NVIDIA-in unaprijed optimizirani inference engine, kao što su TensorRT i TensorRT-LLM, kako bi osigurao nisku latenciju i visok protok.
- **Skalabilnost:** NIM podržava automatsko skaliranje na Kubernetesu, omogućujući učinkovito upravljanje različitim radnim opterećenjima.
- **Sigurnost i kontrola:** Organizacije mogu zadržati kontrolu nad svojim podacima i aplikacijama samostalnim hostanjem NIM mikroservisa na vlastitoj upravljanoj infrastrukturi.
- **Standardni API-jevi:** NIM pruža industrijske standarde API-ja, što olakšava izgradnju i integraciju AI aplikacija poput chatbotova, AI asistenata i drugih.

NIM je dio NVIDIA AI Enterprise-a, koji ima za cilj pojednostaviti implementaciju i operacionalizaciju AI modela, osiguravajući njihovo učinkovito izvođenje na NVIDIA GPU-ima.

- Demo: Korištenje NVIDIA NIM za pozivanje Phi-3.5-Vision-API  [[Kliknite ovaj link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Pokretanje Phi-3/3.5 lokalno
Inference u odnosu na Phi-3, ili bilo koji jezični model poput GPT-3, odnosi se na proces generiranja odgovora ili predviđanja na temelju unosa koji prima. Kada Phi-3-u date prompt ili pitanje, koristi svoj istrenirani neuronski mrežni model za izvođenje najvjerojatnijeg i relevantnog odgovora analizirajući obrasce i odnose u podacima na kojima je treniran.

**Hugging Face Transformer**
Hugging Face Transformers je moćna biblioteka dizajnirana za obradu prirodnog jezika (NLP) i druge zadatke strojnog učenja. Evo nekoliko ključnih točaka o njoj:

1. **Predtrenirani modeli**: Pruža tisuće predtreneniranih modela za različite zadatke poput klasifikacije teksta, prepoznavanja imenskih entiteta, odgovaranja na pitanja, sažimanja, prevođenja i generiranja teksta.

2. **Interoperabilnost okvira:** Biblioteka podržava više dubokih okvira za učenje, uključujući PyTorch, TensorFlow i JAX. To vam omogućuje treniranje modela u jednom okviru i njegovo korištenje u drugom.

3. **Multimodalne sposobnosti:** Osim NLP-a, Hugging Face Transformers podržava i zadatke iz računalnog vida (npr. klasifikacija slika, detekcija objekata) i obrade zvuka (npr. prepoznavanje govora, klasifikacija zvuka).

4. **Jednostavnost korištenja:** Biblioteka nudi API-je i alate za jednostavno preuzimanje i fino podešavanje modela, čineći je pristupačnom i početnicima i stručnjacima.

5. **Zajednica i resursi:** Hugging Face ima živu zajednicu i opsežnu dokumentaciju, tutorijale i vodiče za pomoć korisnicima u početku i maksimalnom iskorištavanju biblioteke.
[službena dokumentacija](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) ili njihov [GitHub repozitorij](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Ovo je najčešće korištena metoda, ali zahtijeva GPU ubrzanje. Na kraju krajeva, scenariji poput Vision i MoE zahtijevaju mnogo izračuna, što će biti vrlo sporo na CPU-u ako nisu kvantizirani.


- Demo: Korištenje Transformera za pozivanje Phi-3.5-Instruct [Kliknite ovaj link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Korištenje Transformera za pozivanje Phi-3.5-Vision [Kliknite ovaj link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Korištenje Transformera za pozivanje Phi-3.5-MoE [Kliknite ovaj link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) je platforma dizajnirana kako bi olakšala pokretanje velikih jezičnih modela (LLM) lokalno na vašem računalu. Podržava razne modele poput Llama 3.1, Phi 3, Mistral i Gemma 2, između ostalih. Platforma pojednostavljuje proces kombiniranjem težina modela, konfiguracije i podataka u jedan paket, što korisnicima omogućuje prilagođavanje i stvaranje vlastitih modela. Ollama je dostupna za macOS, Linux i Windows. Izvrsno je sredstvo ako želite eksperimentirati ili implementirati LLM bez oslanjanja na cloud usluge. Ollama je najizravniji način, trebate samo izvršiti sljedeću naredbu.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) je Microsoftov offline runtime na uređaju za pokretanje modela poput Phi potpuno na vlastitom hardveru - nije potrebna pretplata na Azure, API ključ ili mrežna veza. Automatski odabire najboljeg dostupnog pružatelja izvođenja (NPU, GPU ili CPU) i izlaže endpoint kompatibilan s OpenAI-jem, tako da postojeći kod za `openai`/Azure AI Inference SDK može na njega pokazivati s minimalnim izmjenama. Pogledajte [Foundry Local dokumentaciju](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) za početak.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) je cross-platformski akcelerator za inference i treniranje strojnog učenja. ONNX Runtime za Generativnu AI (GENAI) je moćan alat koji vam pomaže učinkovito pokretati generativne AI modele na različitim platformama. 

## Što je ONNX Runtime?
ONNX Runtime je open-source projekt koji omogućuje visokoučinkovit inference strojnog učenja. Podržava modele u Open Neural Network Exchange (ONNX) formatu, koji je standard za predstavljanje ML modela. ONNX Runtime inference može omogućiti brža korisnička iskustva i niže troškove, podržavajući modele iz dubokih okvira kao što su PyTorch i TensorFlow/Keras kao i klasične biblioteke strojnog učenja poput scikit-learn, LightGBM, XGBoost itd. ONNX Runtime je kompatibilan s različitim hardverom, upravljačkim programima i operativnim sustavima, i pruža optimalnu izvedbu iskorištavanjem hardverskih akceleratora gdje je primjenjivo, zajedno s optimizacijama i transformacijama grafova.

## Što je Generativna AI?
Generativna AI odnosi se na AI sustave koji mogu generirati novi sadržaj, poput teksta, slika ili glazbe, na temelju podataka na kojima su trenirani. Primjeri uključuju jezične modele poput GPT-3 i modele za generiranje slika poput Stable Diffusion. ONNX Runtime za GenAI biblioteka pruža generativni AI ciklus za ONNX modele, uključujući inference s ONNX Runtime, obradu logitskih vrijednosti, pretragu i uzorkovanje te upravljanje KV kešom.

## ONNX Runtime za GENAI
ONNX Runtime za GENAI proširuje mogućnosti ONNX Runtime-a za podršku generativnim AI modelima. Evo nekoliko ključnih značajki:

- **Široka podrška platformi:** Radi na različitim platformama, uključujući Windows, Linux, macOS, Android i iOS.
- **Podrška modelima:** Podržava mnoge popularne generativne AI modele, poput LLaMA, GPT-Neo, BLOOM i drugih.
- **Optimizacija izvedbe:** Uključuje optimizacije za različite hardverske akceleratore poput NVIDIA GPU-a, AMD GPU-a i ostalih2.
- **Jednostavnost korištenja:** Pruža API-je za jednostavnu integraciju u aplikacije, omogućujući generiranje teksta, slika i drugog sadržaja s minimalnim kodom.
- Korisnici mogu pozvati metodu generiranja na visokoj razini generate(), ili izvršavati svaku iteraciju modela u petlji, generirajući po jedan token, te po želji mijenjati parametre generiranja unutar petlje.
- ONNX runtime također podržava pohlepnu/beam pretragu i TopP, TopK uzorkovanje za generiranje sekvenci tokena i ugrađenu obradu logitskih vrijednosti poput penalizacije ponavljanja. Također je lako dodati prilagođeno ocjenjivanje.

## Početak rada
Za početak rada s ONNX Runtime za GENAI, možete slijediti ove korake:

### Instalirajte ONNX Runtime:
```Python
pip install onnxruntime
```
### Instalirajte Generativne AI ekstenzije:
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

Osim metoda referenci ONNX Runtime, Ollama i Foundry Local, možemo također dovršiti referencu kvantitativnih modela na temelju modela referenci koje pružaju različiti proizvođači. Kao što su Apple MLX okvir s Apple Metal-om, Qualcomm QNN s NPU-om, Intel OpenVINO s CPU/GPU-om i drugi. Više sadržaja možete pronaći i u [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Više

Naučili smo osnove obitelji Phi-3/3.5, ali za detaljnije učenje o SLM trebamo više znanja. Odgovore možete pronaći u Phi-3 Cookbooku. Ako želite saznati više, posjetite [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->