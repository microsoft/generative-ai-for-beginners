# Uvod u male jezične modele za generativnu umjetnu inteligenciju za početnike
Generativna umjetna inteligencija je fascinantno područje umjetne inteligencije koje se fokusira na stvaranje sustava sposobnih za generiranje novog sadržaja. Taj sadržaj može varirati od teksta i slika do glazbe pa čak i cijelih virtualnih okruženja. Jedna od najuzbudljivijih primjena generativne umjetne inteligencije je u području jezičnih modela.

## Što su mali jezični modeli?

Mali jezični model (SLM) predstavlja smanjenu varijantu velikog jezičnog modela (LLM), koristeći mnoge arhitektonske principe i tehnike LLM-ova, dok ima značajno smanjen računalni otisak.

SLM su podskup jezičnih modela dizajniranih za generiranje teksta nalik ljudskom. Za razliku od njihovih većih pandana, poput GPT-4, SLM su kompaktniji i učinkovitiji, što ih čini idealnima za primjene gdje su računalni resursi ograničeni. Unatoč manjoj veličini, još uvijek mogu izvršavati razne zadatke. Obično se SLM grade komprimiranjem ili destilacijom LLM-ova, s ciljem zadržavanja značajnog dijela funkcionalnosti i jezičnih sposobnosti izvornog modela. Ovo smanjenje veličine modela smanjuje ukupnu složenost, čineći SLM učinkovitijima u smislu i memorije i računalnih zahtjeva. Unatoč tim optimizacijama, SLM još uvijek mogu izvršavati širok spektar zadataka obrade prirodnog jezika (NLP):

- Generiranje teksta: stvaranje koherentnih i kontekstualno relevantnih rečenica ili odlomaka.
- Dovršavanje teksta: predviđanje i dovršavanje rečenica na temelju danog upita.
- Prevođenje: pretvaranje teksta s jednog jezika na drugi.
- Sažimanje: sažimanje dugih tekstova u kraće, lakše probavljive sažetke.

Iako uz određene kompromise u izvedbi ili dubini razumijevanja u usporedbi s njihovim većim pandamima.

## Kako djeluju mali jezični modeli?
SLM se treniraju na ogromnim količinama tekstualnih podataka. Tijekom treninga, uče obrasce i strukture jezika, što im omogućuje generiranje teksta koji je gramatikalno ispravan i kontekstualno prikladan. Proces treninga uključuje:

- Prikupljanje podataka: skupljanje velikih skupova tekstualnih podataka iz raznih izvora.
- Predobrada: čišćenje i organiziranje podataka kako bi bili pogodni za trening.
- Trening: korištenje algoritama strojnog učenja za podučavanje modela kako razumjeti i generirati tekst.
- Fino podešavanje: prilagodba modela za poboljšanje izvedbe na specifičnim zadacima.

Razvoj SLM-a prati rastuću potrebu za modelima koje je moguće implementirati u okruženjima ograničenih resursa, poput mobilnih uređaja ili platformi za edge computing, gdje bi puni LLM-ovi mogli biti nepraktični zbog velikih zahtjeva za resursima. Fokusirajući se na učinkovitost, SLM balansiraju izvedbu s dostupnošću, omogućujući širu primjenu u različitim domenama.

![slm](../../../translated_images/hr/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Ciljevi učenja

U ovoj lekciji želimo predstaviti znanje o SLM-u i kombinirati ga s Microsoft Phi-3 kako bismo naučili različite scenarije u tekstualnom sadržaju, viziji i MoE.

Do kraja ove lekcije trebali biste moći odgovoriti na sljedeća pitanja:

- Što je SLM?
- Koja je razlika između SLM-a i LLM-a?
- Što je Microsoft Phi-3/3.5 obitelj?
- Kako pokrenuti inferenciju s Microsoft Phi-3/3.5 obitelji?

Spremni? Krenimo.

## Razlike između velikih jezičnih modela (LLM) i malih jezičnih modela (SLM)

I LLM i SLM grade se na temeljnim principima probabilističkog strojnog učenja, slijedeći slične pristupe u arhitektonskom dizajnu, metodologijama treninga, procesima generiranja podataka i tehnikama evaluacije modela. Međutim, nekoliko ključnih faktora razlikuje ove dvije vrste modela.

## Primjene malih jezičnih modela

SLM imaju širok spektar primjena, uključujući:

- Chatbotovi: pružanje korisničke podrške i interakcija s korisnicima na konverzacijalan način.
- Kreiranje sadržaja: pomaganje piscima generiranjem ideja ili čak pisanjem cijelih članaka.
- Obrazovanje: pomoć studentima pri pisanju zadaća ili učenju novih jezika.
- Pristupačnost: stvaranje alata za osobe s invaliditetom, poput sustava pretvorbe teksta u govor.

**Veličina**
  
Temeljna razlika između LLM-a i SLM-a leži u veličini modela. LLM-ovi, poput ChatGPT-a (GPT-4), mogu imati procijenjenih 1,76 bilijuna parametara, dok open-source SLM poput Mistral 7B ima znatno manje parametara — približno 7 milijardi. Ova razlika prvenstveno proizlazi iz razlika u arhitekturi modela i procesima treniranja. Primjerice, ChatGPT koristi mehanizam samopozornosti unutar encoder-decoder okvira, dok Mistral 7B koristi sliding window attention, što omogućuje učinkovitiji trening unutar isključivo decoder modela. Ova arhitektonska razlika ima značajan utjecaj na složenost i performanse ovih modela.

**Razumijevanje**

SLM su obično optimizirani za izvedbu unutar specifičnih domena, čineći ih visoko specijaliziranima, ali potencijalno ograničenima u sposobnosti pružanja širokog kontekstualnog razumijevanja kroz različita područja znanja. Nasuprot tome, LLM-ovi ciljaju simulirati ljudsku inteligenciju na široj razini. Trenirani na ogromnim i raznolikim skupovima podataka, LLM-ovi su dizajnirani za dobru izvedbu u mnogim domenama, nudeći veću svestranost i prilagodljivost. Posljedično, LLM-ovi su prikladniji za širi raspon zadataka, poput obrade prirodnog jezika i programiranja.

**Računalni zahtjevi**

Trening i implementacija LLM-ova su procesi koji zahtijevaju velike resurse, često zahtijevajući značajnu računalnu infrastrukturu, uključujući velike GPU klastere. Na primjer, treniranje modela poput ChatGPT-a od početka može zahtijevati tisuće GPU-ova tijekom dugog razdoblja. Nasuprot tome, SLM, sa znatno manjim brojem parametara, su pristupačniji u smislu računalnih resursa. Modeli poput Mistral 7B mogu se trenirati i koristiti na lokalnim računalima opremljenim umjerenim GPU kapacitetima, iako trening još uvijek zahtijeva nekoliko sati na više GPU-ova.

**Pristranost**

Pristranost je poznati problem kod LLM-ova, prvenstveno zbog prirode podataka za trening. Ti modeli često ovise o sirovim, javno dostupnim podacima s interneta, koji mogu nedovoljno predstavljati ili pogrešno predstavljati određene skupine, uvesti netočno označavanje ili odražavati jezične predrasude uzrokovane dijalektima, geografskim varijacijama i gramatičkim pravilima. Nadalje, složenost arhitektura LLM-a može nenamjerno pojačati pristranost, koja može ostati neprimijećena bez pažljivog fino podešavanja. S druge strane, SLM, koji se treniraju na ograničenijim, domen-specific skupovima podataka, inherentno su manje podložni takvim pristranostima, iako nisu imun.

**Inferencija**

Smanjena veličina SLM-ova daje im značajnu prednost u brzini inferencije, omogućujući im učinkovit izlaz na lokalnom hardveru bez potrebe za opsežnom paralelnom obradom. Nasuprot tome, LLM-ovi, zbog svoje veličine i složenosti, često zahtijevaju značajne paralelne računalne resurse za prihvatljivo vrijeme inferencije. Prisutnost više istodobnih korisnika dodatno usporava vrijeme odgovora LLM-ova, posebno kada su implementirani u velikoj mjeri.

Ukratko, iako LLM i SLM dijele temeljnu bazu u strojnome učenju, značajno se razlikuju po veličini modela, zahtjevima za resursima, kontekstualnom razumijevanju, osjetljivosti na pristranost i brzini inferencije. Te razlike odražavaju njihovu prikladnost za različite slučajeve uporabe, pri čemu su LLM svestraniji ali zahtjevniji za resurse, a SLM nude učinkovitost specifičnu za domenu uz smanjene računalne zahtjeve.

***Napomena: U ovoj lekciji predstavit ćemo SLM na primjeru Microsoft Phi-3 / 3.5.***

## Predstavljanje Phi-3 / Phi-3.5 obitelji

Phi-3 / 3.5 obitelj uglavnom cilja na scenarije primjene u tekstu, viziji i Agentu (MoE):

### Phi-3 / 3.5 Instruct

Uglavnom za generiranje teksta, dovršavanje chata i izdvajanje informacija iz sadržaja itd.

**Phi-3-mini**

Jezični model od 3,8 milijardi parametara dostupan je na Microsoft Foundry-u, Hugging Face-u i Ollama-i. Phi-3 modeli znatno nadmašuju jezične modele jednake i veće veličine na ključnim mjerilima (vidi brojke ispod, veći brojevi su bolji). Phi-3-mini nadmašuje modele dvostruke veličine, dok Phi-3-small i Phi-3-medium nadmašuju veće modele, uključujući GPT-3.5.

**Phi-3-small i medium**

Sa samo 7 milijardi parametara, Phi-3-small pobjeđuje GPT-3.5T na raznim jezičnim, rezonirajućim, kodirajućim i matematičkim mjerilima.

Phi-3-medium s 14 milijardi parametara nastavlja ovaj trend i nadmašuje Gemini 1.0 Pro.

**Phi-3.5-mini**

Možemo ga smatrati nadogradnjom Phi-3-mini. Iako broj parametara ostaje isti, poboljšava sposobnost podrške više jezika (podržava 20+ jezika: arapski, kineski, češki, danski, nizozemski, engleski, finski, francuski, njemački, hebrejski, mađarski, talijanski, japanski, korejski, norveški, poljski, portugalski, ruski, španjolski, švedski, tajlandski, turski, ukrajinski) te dodaje snažniju podršku za duži kontekst.

Phi-3.5-mini s 3,8 milijardi parametara nadmašuje jezične modele iste veličine i usporediv je s modelima dvostruke veličine.

### Phi-3 / 3.5 Vision

Možemo razmišljati o Instruct modelu Phi-3/3.5 kao o Phi-jevoj sposobnosti razumijevanja, a Vision daje Phi-u oči za razumijevanje svijeta.


**Phi-3-Vision**

Phi-3-vision, s samo 4,2 milijarde parametara, nastavlja ovaj trend i nadmašuje veće modele poput Claude-3 Haiku i Gemini 1.0 Pro V na općim vizualnim zadacima rezoniranja, OCR-u i zadacima razumijevanja tablica i dijagrama.


**Phi-3.5-Vision**

Phi-3.5-Vision je također nadogradnja Phi-3-Vision, dodajući podršku za više slika. Možete ga smatrati poboljšanjem vizije, ne vidite samo slike, već i videozapise.

Phi-3.5-vision nadmašuje veće modele poput Claude-3.5 Sonnet i Gemini 1.5 Flash u OCR-u, razumijevanju tablica i grafikona te je usporediv na općim zadacima vizualnog znanja. Podržava višekadarski ulaz, tj. izvođenje rezoniranja na višestrukim ulaznim slikama.


### Phi-3.5-MoE

***Mješavina Eksperata (Mixture of Experts, MoE)*** omogućuje modelima predtreniranje s mnogo manje računalnih resursa, što znači da možete znatno povećati veličinu modela ili skupa podataka s istim proračunom za računsku snagu kao kod gustog modela. Konkretno, MoE model bi trebao postići istu kvalitetu kao i njegov gusti pandan mnogo brže tijekom predtreninga.

Phi-3.5-MoE se sastoji od 16 modula eksperata od po 3,8 milijardi. Phi-3.5-MoE s samo 6,6 milijardi aktivnih parametara postiže sličnu razinu rezoniranja, razumijevanja jezika i matematike kao mnogo veći modeli.

Možemo koristiti Phi-3/3.5 obitelj modela ovisno o različitim scenarijima. Za razliku od LLM, Phi-3/3.5-mini ili Phi-3/3.5-Vision možete implementirati na uređajima na rubu mreže.


## Kako koristiti Phi-3/3.5 obitelj modela

Nadamo se koristiti Phi-3/3.5 u različitim scenarijima. Sljedeće ćemo koristiti Phi-3/3.5 temeljem različitih scenarija.

![phi3](../../../translated_images/hr/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inferencija preko Cloud API-ja

**Microsoft Foundry modeli**

> **Napomena:** GitHub modeli se povlače krajem srpnja 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) je njihov izravan zamjenski izbor.

> **Napomena:** Cijela Phi-3/3.5 obitelj (Instruct, Vision i MoE varijante) povučena je iz Microsoft Foundry Models kataloga 2025-08-30. Koristite tamo `Phi-4` (Instruct) ili `Phi-4-mini-instruct` — primjeri Phi-3/3.5 iz ove lekcije još uvijek rade preko Hugging Face, Ollama, ONNX Runtime i NVIDIA NIM.

Microsoft Foundry modeli sada nude nasljednike Phi-4. Umjesto povučenih Phi-3/3.5 modela koristite `Phi-4` ili `Phi-4-mini-instruct` prateći primjere cloud API-ja.

- Demo: Usporedba učinaka Phi-3-mini i Phi-3.5-mini u kineskim scenarijima

![phi3](../../../translated_images/hr/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/hr/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Ako želite koristiti modele za viziju (multimodalne) u oblaku, koristite trenutno dostupne `Phi-4-multimodal-instruct` putem Microsoft Foundry umjesto povučenih Phi-3/3.5 Vision modela; za tekstualne zadatke koristite `Phi-4` ili `Phi-4-mini-instruct`. Phi-3.5 MoE model je povučen iz Microsoft Foundry, pa koristite druge opise iz ove lekcije (npr. Hugging Face) ako želite eksperimentirati s njim. Ako vas zanima, možete pročitati Phi Cookbook kako naučiti koristiti Phi modele preko Microsoft Foundry [Kliknite ovaj link](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Osim Microsoft Foundry Modela u oblaku, možete koristiti i [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) za dovršavanje relevantnih poziva. Možete posjetiti NVIDIA NIM za dovršavanje API poziva Phi-3/3.5 obitelji. NVIDIA NIM (NVIDIA Inference Microservices) je skup ubrzanih mikroservisa za inferenciju dizajniranih kako bi pomogli programerima efikasno implementirati AI modele u različitim okruženjima, uključujući oblak, podatkovne centre i radne stanice.

Evo nekoliko ključnih značajki NVIDIA NIM-a:

- **Jednostavnost implementacije:** NIM omogućuje implementaciju AI modela jednom naredbom, što olakšava integraciju u postojeće radne tokove.
- **Optimizirana izvedba:** Iskorištava NVIDIA-in prethodno optimizirane inferencijske motore, poput TensorRT i TensorRT-LLM, kako bi osigurao nisku latenciju i visok protok.
- **Skalabilnost:** NIM podržava automatsko skaliranje na Kubernetesu, što mu omogućuje učinkovito rukovanje promjenjivim opterećenjima.
- **Sigurnost i kontrola:** Organizacije mogu zadržati kontrolu nad svojim podacima i aplikacijama samostalnim hostanjem NIM mikrousluga na vlastitoj upravljanoj infrastrukturi.
- **Standardni API-ji:** NIM pruža industrijske standardne API-je, što olakšava izradu i integraciju AI aplikacija poput chatbotova, AI asistenata i više.

NIM je dio NVIDIA AI Enterprise, koji ima za cilj pojednostaviti implementaciju i operacionalizaciju AI modela, osiguravajući njihovo učinkovito izvođenje na NVIDIA GPU-ima.

- Demo: Korištenje NVIDIA NIM za pozivanje Phi-3.5-Vision-API  [[Kliknite ovaj link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Pokretanje Phi-3/3.5 lokalno
Inferencija u vezi s Phi-3, ili bilo kojim jezičnim modelom poput GPT-3, odnosi se na proces generiranja odgovora ili predviđanja na temelju ulaza koji prima. Kada date upit ili pitanje Phi-3, koristi svoj trenirani neuronski mrežni model da zaključi najvjerojatniji i relevantan odgovor analizirajući obrasce i odnose u podacima na kojima je treniran.

**Hugging Face Transformer**
Hugging Face Transformers je moćna biblioteka dizajnirana za obradu prirodnog jezika (NLP) i druge zadatke strojnog učenja. Evo nekoliko ključnih točaka o njoj:

1. **Prethodno trenirani modeli**: Pruža tisuće prethodno treniranih modela koje se može koristiti za različite zadatke kao što su klasifikacija teksta, prepoznavanje imenovanih entiteta, odgovaranje na pitanja, sažimanje, prijevod i generiranje teksta.

2. **Interoperabilnost okvira:** Biblioteka podržava više dubokih učenih okvira, uključujući PyTorch, TensorFlow i JAX. To vam omogućuje da model trenirate u jednom okviru, a koristite ga u drugom.

3. **Višemodalne sposobnosti:** Osim NLP-a, Hugging Face Transformers također podržava zadatke u računalnom vidu (npr. klasifikacija slika, detekcija objekata) i obradi zvuka (npr. prepoznavanje govora, klasifikacija zvuka).

4. **Jednostavnost upotrebe:** Biblioteka nudi API-je i alate za lako preuzimanje i fino podešavanje modela, čineći je dostupnom i za početnike i za stručnjake.

5. **Zajednica i resursi:** Hugging Face ima živahnu zajednicu i opsežnu dokumentaciju, tutorijale i vodiče koji pomažu korisnicima da započnu i iskoriste biblioteku u punoj mjeri.
[službena dokumentacija](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) ili njihov [GitHub repozitorij](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Ovo je najčešće korištena metoda, no također zahtijeva GPU ubrzanje. Scenariji poput Vision i MoE zahtijevaju puno proračuna, što će na CPU-u biti vrlo sporo ako modeli nisu kvantizirani.


- Demo: Korištenje Transformera za pozivanje Phi-3.5-Instruct [Kliknite ovaj link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Korištenje Transformera za pozivanje Phi-3.5-Vision [Kliknite ovaj link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Korištenje Transformera za pozivanje Phi-3.5-MoE [Kliknite ovaj link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) je platforma dizajnirana da olakša pokretanje velikih jezičnih modela (LLM-ova) lokalno na vašem računalu. Podržava različite modele poput Llama 3.1, Phi 3, Mistral i Gemma 2, među ostalima. Platforma pojednostavljuje proces paketiranjem težina modela, konfiguracije i podataka u jedan paket, što korisnicima olakšava prilagodbu i izradu vlastitih modela. Ollama je dostupna za macOS, Linux i Windows. Sjajan je alat ako želite eksperimentirati s LLM-ovima ili ih implementirati bez oslanjanja na oblačne usluge. Ollama je najizravniji način, samo trebate izvršiti sljedeću naredbu.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) je Microsoftovo offline, lokalno okruženje za izvršavanje modela poput Phi potpuno na vlastitom hardveru - nije potrebna pretplata na Azure, API ključ ni mrežna veza. Automatski odabire najbolji dostupni izvršni pružatelj (NPU, GPU ili CPU) i izlaže endpoint kompatibilan s OpenAI-jem, tako da postojeći `openai`/Azure AI Inference SDK kod može ciljati na njega uz minimalne izmjene. Pogledajte [Foundry Local dokumentaciju](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) za početak.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) je multiplatformski akcelerator za izvršavanje inferencije i treniranja modela strojnog učenja. ONNX Runtime za Generativnu AI (GENAI) je moćan alat koji vam pomaže učinkovito pokretati generativne AI modele na različitim platformama.

## Što je ONNX Runtime?
ONNX Runtime je otvoreni projekt koji omogućuje visokoučinkovitu inferenciju modela strojnog učenja. Podržava modele u Open Neural Network Exchange (ONNX) formatu, koji je standard za predstavljanje modela strojnog učenja. ONNX Runtime inferencija može omogućiti brže korisničko iskustvo i niže troškove, podržavajući modele iz dubokih okvira kao što su PyTorch i TensorFlow/Keras, kao i klasične biblioteke strojnog učenja poput scikit-learn, LightGBM, XGBoost itd. ONNX Runtime kompatibilan je s različitim hardverom, upravljačkim programima i operativnim sustavima te osigurava optimalne performanse iskorištavanjem hardverskih akceleratora gdje je moguće zajedno s optimizacijama i transformacijama grafova.

## Što je Generativna AI?
Generativna AI odnosi se na AI sustave koji mogu generirati novi sadržaj, poput teksta, slika ili glazbe, na temelju podataka na kojima su trenirani. Primjeri uključuju jezične modele poput GPT-3 i modele generiranja slika poput Stable Diffusion. ONNX Runtime za GenAI biblioteka pruža generativni AI ciklus za ONNX modele, uključujući inferenciju s ONNX Runtime-om, obradu logita, pretraživanje i uzorkovanje te upravljanje KV cacheom.

## ONNX Runtime za GENAI
ONNX Runtime za GENAI proširuje mogućnosti ONNX Runtime-a kako bi podržao generativne AI modele. Evo nekih ključnih značajki:

- **Široka podrška platformi:** Radi na različitim platformama, uključujući Windows, Linux, macOS, Android i iOS.
- **Podrška za modele:** Podržava mnoge popularne generativne AI modele, poput LLaMA, GPT-Neo, BLOOM i drugih.
- **Optimizacija performansi:** Uključuje optimizacije za različite hardverske akceleratore poput NVIDIA GPU-a, AMD GPU-a i drugih.
- **Jednostavnost upotrebe:** Pruža API-je za lakšu integraciju u aplikacije, omogućujući generiranje teksta, slika i drugog sadržaja s minimalnim kodom.
- Korisnici mogu pozvati visokorazinski generate() metod, ili pokretati svaku iteraciju modela u petlji, generirajući jedan token po token, te opciono ažurirati parametre generiranja unutar petlje.
- ONNX runtime također podržava greedy/beam pretraživanje i TopP, TopK uzorkovanje za generiranje nizova tokena te ugrađenu obradu logita poput penalizacije ponavljanja. Također možete lako dodati prilagođeno bodovanje.

## Početak rada
Za početak rada s ONNX Runtime za GENAI slijedite ove korake:

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


**Ostali**

Osim referentnih metoda ONNX Runtime, Ollama i Foundry Local, možemo također dovršiti referencu kvantitativnih modela temeljenih na metodama referenciranja modela koje pružaju različiti proizvođači. Kao što su Apple MLX framework s Apple Metalom, Qualcomm QNN s NPU-om, Intel OpenVINO s CPU/GPU-om itd. Više sadržaja možete pronaći u [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Više

Naučili smo osnove obitelji Phi-3/3.5, ali za detaljnije učenje o SLM potrebne su dodatne informacije. Odgovore možete pronaći u Phi-3 Cookbooku. Ako želite saznati više, posjetite [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->