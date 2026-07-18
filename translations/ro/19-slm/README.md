# Introducere în Modelele Mici de Limbaj pentru Inteligența Artificială Generativă pentru Începători
Inteligența Artificială Generativă este un domeniu fascinant al inteligenței artificiale care se concentrează pe crearea sistemelor capabile să genereze conținut nou. Acest conținut poate varia de la text și imagini la muzică și chiar medii virtuale întregi. Una dintre cele mai interesante aplicații ale inteligenței artificiale generative este în domeniul modelelor de limbaj.

## Ce sunt Modelele Mici de Limbaj?

Un Model Mic de Limbaj (SLM) reprezintă o variantă redusă a unui model mare de limbaj (LLM), folosind multe dintre principiile arhitecturale și tehnicile LLM-urilor, în timp ce prezintă o amprentă computațională semnificativ redusă.

SLM-urile sunt un subset de modele de limbaj concepute pentru a genera text asemănător celui uman. Spre deosebire de omologii lor mai mari, precum GPT-4, SLM-urile sunt mai compacte și eficiente, făcându-le ideale pentru aplicații în care resursele computaționale sunt limitate. În ciuda dimensiunii mai mici, ele pot îndeplini încă o varietate de sarcini. De obicei, SLM-urile sunt construite prin comprimarea sau distilarea LLM-urilor, având ca scop păstrarea unei porțiuni substanțiale din funcționalitatea și capacitățile lingvistice ale modelului original. Această reducere a dimensiunii modelului scade complexitatea generală, făcând SLM-urile mai eficiente atât din punct de vedere al utilizării memoriei, cât și al cerințelor computaționale. În ciuda acestor optimizări, SLM-urile pot realiza încă o gamă largă de sarcini de procesare a limbajului natural (NLP):

- Generarea de Text: Crearea de propoziții sau paragrafe coerente și relevante contextual.
- Completarea Textului: Predictarea și completarea propozițiilor pe baza unui prompt dat.
- Traducere: Convertirea textului dintr-o limbă în alta.
- Rezumat: Condensarea unor texte lungi în rezumate mai scurte și mai ușor de digerat.

Deși cu unele compromisuri în performanță sau adâncime a înțelegerii comparativ cu omologii lor mai mari.

## Cum Funcționează Modelele Mici de Limbaj?
SLM-urile sunt antrenate pe cantități vaste de date text. În timpul antrenamentului, ele învață tiparele și structurile limbajului, permițându-le să genereze text atât corect din punct de vedere gramatical, cât și adecvat contextual. Procesul de antrenament implică:

- Colectarea Datelor: Adunarea unor seturi mari de date text din diverse surse.
- Preprocesarea: Curățarea și organizarea datelor pentru a fi adecvate pentru antrenament.
- Antrenamentul: Folosirea algoritmilor de învățare automată pentru a învăța modelul cum să înțeleagă și să genereze text.
- Ajustarea Fină: Reglarea modelului pentru a-i îmbunătăți performanța în sarcini specifice.

Dezvoltarea SLM-urilor se aliniază nevoii crescânde de modele care pot fi implementate în medii cu resurse limitate, cum ar fi dispozitivele mobile sau platformele de calcul la margine, unde LLM-urile de scară completă pot fi nepracticabile din cauza cerințelor lor ridicate de resurse. Concentrându-se pe eficiență, SLM-urile echilibrează performanța cu accesibilitatea, permițând o aplicare mai largă în diverse domenii.

![slm](../../../translated_images/ro/slm.4058842744d0444a.webp)

## Obiective de Învățare

În această lecție, sperăm să introducem cunoștințele despre SLM și să le combinăm cu Microsoft Phi-3 pentru a învăța diferite scenarii în conținut text, viziune și MoE.

Până la sfârșitul acestei lecții, ar trebui să puteți răspunde la următoarele întrebări:

- Ce este SLM?
- Care este diferența dintre SLM și LLM?
- Ce este familia Microsoft Phi-3/3.5?
- Cum se execută inferența cu familia Microsoft Phi-3/3.5?

Sunteți gata? Să începem.

## Diferențele dintre Modelele Mari de Limbaj (LLM) și Modelele Mici de Limbaj (SLM)

Atât LLM-urile, cât și SLM-urile sunt construite pe principii fundamentale de învățare automată probabilistică, urmând abordări similare în designul arhitectural, metodologiile de antrenament, procesele de generare a datelor și tehnicile de evaluare a modelelor. Totuși, există câțiva factori cheie care diferențiază aceste două tipuri de modele.

## Aplicații ale Modelelor Mici de Limbaj

SLM-urile au o gamă largă de aplicații, inclusiv:

- Chatbot-uri: Oferirea de suport clienților și interacționarea cu utilizatorii într-un mod conversațional.
- Crearea de Conținut: Asistarea scriitorilor prin generarea de idei sau chiar redactarea articolelor întregi.
- Educație: Ajutor pentru studenți la temele de scriere sau învățarea de limbi noi.
- Accesibilitate: Crearea de instrumente pentru persoane cu dizabilități, cum ar fi sistemele text-în-vorbire.

**Dimensiunea**

O diferență principală între LLM-uri și SLM-uri constă în scala modelelor. LLM-urile, precum ChatGPT (GPT-4), pot cuprinde aproximativ 1,76 trilioane de parametri, în timp ce SLM-urile open-source precum Mistral 7B sunt proiectate cu semnificativ mai puțini parametri — aproximativ 7 miliarde. Această diferență se datorează în principal diferențelor în arhitectura modelului și proceselor de antrenament. De exemplu, ChatGPT utilizează un mecanism de auto-atenție într-un cadru encoder-decoder, pe când Mistral 7B folosește atenția cu fereastră glisantă, ceea ce permite un antrenament mai eficient într-un model doar decoder. Această variație arhitecturală are implicații profunde asupra complexității și performanței acestor modele.

**Înțelegerea**

SLM-urile sunt de obicei optimizate pentru performanță în domenii specifice, făcându-le foarte specializate, dar potențial limitate în capacitatea lor de a oferi o înțelegere contextuală largă în mai multe domenii de cunoaștere. În contrast, LLM-urile urmăresc să imite inteligența asemănătoare celei umane la un nivel mai cuprinzător. Antrenate pe seturi vaste și diverse de date, LLM-urile sunt concepute să performeze bine în diverse domenii, oferind o versatilitate și adaptabilitate mai mare. Prin urmare, LLM-urile sunt mai potrivite pentru o gamă mai largă de sarcini ulterioare, cum ar fi procesarea limbajului natural și programarea.

**Calculul**

Antrenamentul și implementarea LLM-urilor sunt procese consumatoare de resurse, necesitând adesea infrastructură computațională semnificativă, inclusiv clustere mari de GPU-uri. De exemplu, antrenarea unui model precum ChatGPT de la zero poate necesita mii de GPU-uri pe perioade extinse. În contrast, SLM-urile, cu un număr mai mic de parametri, sunt mai accesibile în termeni de resurse computaționale. Modelele precum Mistral 7B pot fi antrenate și rulate pe mașini locale echipate cu capabilități moderate GPU, deși antrenamentul necesită totuși câteva ore pe mai multe GPU-uri.

**Bias**

Biasul este o problemă cunoscută în LLM-uri, în principal din cauza naturii datelor de antrenament. Aceste modele se bazează adesea pe date brute, disponibile public pe internet, care pot subreprezenta sau reprezenta eronat anumite grupuri, pot introduce etichetări greșite sau reflecta biasuri lingvistice influențate de dialect, variații geografice și reguli gramaticale. În plus, complexitatea arhitecturilor LLM poate accentua involuntar biasul, care poate trece neobservat fără o reglare fină atentă. Pe de altă parte, SLM-urile, fiind antrenate pe seturi de date mai restrânse și specifice domeniului, sunt în mod inerent mai puțin susceptibile la astfel de biasuri, deși nu sunt imune.

**Inferența**

Dimensiunea redusă a SLM-urilor le oferă un avantaj semnificativ în ceea ce privește viteza inferenței, permițând generarea de rezultate eficient pe hardware local fără nevoie de procesare paralelă extinsă. În contrast, LLM-urile, datorită dimensiunii și complexității lor, necesită adesea resurse computaționale paralele considerabile pentru a atinge timpi de inferență acceptabili. Prezența mai multor utilizatori concurenți încetinește și mai mult timpii de răspuns ai LLM-urilor, mai ales când sunt implementate la scară largă.

În rezumat, deși atât LLM-urile, cât și SLM-urile împărtășesc o bază fundamentală în învățarea automată, ele diferă semnificativ în ceea ce privește dimensiunea modelului, cerințele de resurse, înțelegerea contextuală, susceptibilitatea la bias și viteza inferenței. Aceste diferențieri reflectă adecvarea lor respectivă pentru diferite cazuri de utilizare, LLM-urile fiind mai versatile, dar consumatoare de resurse, iar SLM-urile oferind o eficiență mai specifică domeniului cu cerințe computaționale reduse.

***Notă: În această lecție, vom introduce SLM utilizând Microsoft Phi-3 / 3.5 ca exemplu.***

## Prezentarea familiei Phi-3 / Phi-3.5

Familia Phi-3 / 3.5 vizează în principal scenarii de aplicații pentru text, viziune și Agent (MoE):

### Phi-3 / 3.5 Instruct

În principal pentru generare de text, completarea conversațiilor și extragerea de informații din conținut, etc.

**Phi-3-mini**

Modelul de limbaj de 3,8 miliarde este disponibil pe Microsoft Foundry, Hugging Face și Ollama. Modelele Phi-3 depășesc semnificativ modelele de limbaj de dimensiuni egale și mai mari în repere cheie (vezi cifrele benchmark de mai jos, numerele mai mari sunt mai bune). Phi-3-mini depășește modelele de două ori mai mari, iar Phi-3-small și Phi-3-medium depășesc modele mai mari, inclusiv GPT-3.5.

**Phi-3-small & medium**

Cu doar 7 miliarde de parametri, Phi-3-small depășește GPT-3.5T pe o varietate de repere legate de limbaj, raționament, programare și matematică.

Phi-3-medium cu 14 miliarde de parametri continuă această tendință și depășește Gemini 1.0 Pro.

**Phi-3.5-mini**

O putem considera o versiune îmbunătățită a Phi-3-mini. Deși numărul parametrilor rămâne neschimbat, îmbunătățește abilitatea de a susține mai multe limbi (suport pentru peste 20 de limbi: Arabă, Chineză, Cehă, Daneză, Olandeză, Engleză, Finlandeză, Franceză, Germană, Ebraică, Maghiară, Italiană, Japoneză, Coreeană, Norvegiană, Poloneză, Portugheză, Rusă, Spaniolă, Suedeză, Thailandeză, Turcă, Ucraineană) și adaugă suport mai puternic pentru contexte lungi.

Phi-3.5-mini cu 3,8 miliarde de parametri depășește modelele de limbaj de aceeași dimensiune și este la egalitate cu modele de două ori mai mari.

### Phi-3 / 3.5 Vision

Putem considera modelul Instruct al Phi-3/3.5 ca fiind abilitatea Phi de a înțelege, iar Vision este ceea ce îi oferă lui Phi ochi pentru a înțelege lumea.


**Phi-3-Vision**

Phi-3-vision, cu doar 4,2 miliarde de parametri, continuă această tendință și depășește modele mai mari precum Claude-3 Haiku și Gemini 1.0 Pro V pe sarcini generale de raționament vizual, OCR și înțelegerea tabelelor și diagramelor.


**Phi-3.5-Vision**

Phi-3.5-Vision este, de asemenea, o actualizare a Phi-3-Vision, adăugând suport pentru imagini multiple. Poate fi privit ca o îmbunătățire a viziunii, nu doar pentru a vedea imagini, ci și videoclipuri.

Phi-3.5-vision depășește modele mai mari precum Claude-3.5 Sonnet și Gemini 1.5 Flash în sarcinile OCR, înțelegerea tabelelor și diagramelor și este la egalitate în sarcinile generale de raționament vizual. Suportă input multi-frame, adică poate realiza raționamente pe mai multe imagini de intrare.


### Phi-3.5-MoE

***Mixtura de Experți (MoE)*** permite modelelor să fie pre-antrenate cu mult mai puțin calcul, ceea ce înseamnă că poți extinde semnificativ dimensiunea modelului sau a setului de date cu același buget de calcul ca un model dens. În special, un model MoE trebuie să atingă aceeași calitate ca omologul său dens mult mai rapid în timpul pre-antrenamentului.

Phi-3.5-MoE este compus din 16 module experte de câte 3,8 miliarde. Phi-3.5-MoE cu doar 6,6 miliarde de parametri activi atinge un nivel similar de raționament, înțelegere a limbajului și matematică ca modele mult mai mari.

Putem folosi modelul familiei Phi-3/3.5 bazat pe diferite scenarii. Spre deosebire de LLM, poți implementa Phi-3/3.5-mini sau Phi-3/3.5-Vision pe dispozitive edge.


## Cum să folosești modelele familiei Phi-3/3.5

Sperăm să folosim Phi-3/3.5 în diferite scenarii. În continuare, vom folosi Phi-3/3.5 bazat pe diferite scenarii.

![phi3](../../../translated_images/ro/phi3.655208c3186ae381.webp)

### Inferență prin API-urile Cloud

**Modele Microsoft Foundry**

> **Notă:** GitHub Models va fi retras la sfârșitul lunii iulie 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) este înlocuirea directă.

Modelele Microsoft Foundry sunt cea mai directă cale. Poți accesa rapid modelul Phi-3/3.5-Instruct prin catalogul de modele Foundry. Combinat cu Azure AI Inference SDK / OpenAI SDK, poți accesa API-ul prin cod pentru a completa apelul Phi-3/3.5-Instruct. De asemenea, poți testa diferite efecte prin intermediul Playground.

- Demo: Compararea efectelor Phi-3-mini și Phi-3.5-mini în scenarii chinezești

![phi3](../../../translated_images/ro/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/ro/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Sau dacă dorim să folosim modelele de viziune și MoE, poți folosi Microsoft Foundry pentru a completa apelul. Dacă ești interesat, poți citi Phi-3 Cookbook pentru a învăța cum să apelezi Phi-3/3.5 Instruct, Vision, MoE prin Microsoft Foundry [Click pe acest link](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Pe lângă catalogul de modele Microsoft Foundry bazat pe cloud, poți utiliza și [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) pentru a completa apeluri conexe. Poți vizita NVIDIA NIM pentru a completa apelurile API ale familiei Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) este un set de microservicii de inferență accelerate concepute să ajute dezvoltatorii să implementeze modele AI eficient în diverse medii, inclusiv clouduri, centre de date și stații de lucru.

Iată câteva caracteristici cheie ale NVIDIA NIM:

- **Ușurința implementării:** NIM permite implementarea modelelor AI cu o singură comandă, făcând integrarea în fluxurile de lucru existente simplă.

- **Performanță optimizată:** Profită de motoarele de inferență pre-optimizate NVIDIA, cum ar fi TensorRT și TensorRT-LLM, pentru a asigura latență redusă și debit mare.
- **Scalabilitate:** NIM suportă autoscalarea pe Kubernetes, permițând gestionarea eficientă a sarcinilor variabile de lucru.
- **Securitate și control:** Organizațiile pot menține controlul asupra datelor și aplicațiilor lor prin găzduirea internă a microserviciilor NIM pe infrastructura proprie gestionată.
- **API-uri standard:** NIM oferă API-uri standard din industrie, facilitând construirea și integrarea aplicațiilor AI precum chatboți, asistenți AI și altele.

NIM face parte din NVIDIA AI Enterprise, care urmărește să simplifice implementarea și operaționalizarea modelelor AI, asigurând funcționarea eficientă pe GPU-urile NVIDIA.

- Demo: Utilizarea NVIDIA NIM pentru a apela Phi-3.5-Vision-API  [[Faceți clic pe acest link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Rularea locală a Phi-3/3.5
Inferența în raport cu Phi-3, sau orice model de limbaj precum GPT-3, se referă la procesul de generare a răspunsurilor sau previziunilor bazate pe intrarea primită. Atunci când oferi un prompt sau o întrebare lui Phi-3, acesta utilizează rețeaua sa neuronală antrenată pentru a deduce cel mai probabil și relevant răspuns analizând modele și relații în datele pe care a fost antrenat.

**Hugging Face Transformer**
Hugging Face Transformers este o bibliotecă puternică concepută pentru procesarea limbajului natural (NLP) și alte sarcini de învățare automată. Iată câteva puncte cheie despre aceasta:

1. **Modele Pre-antrenate**: Oferă mii de modele pre-antrenate ce pot fi folosite pentru diverse sarcini precum clasificarea textului, recunoașterea entităților numite, răspuns la întrebări, sumarizare, traducere și generare de text.

2. **Interoperabilitate în cadrul framework-urilor**: Biblioteca suportă mai multe framework-uri de învățare profundă, precum PyTorch, TensorFlow și JAX. Acest lucru permite antrenarea unui model într-un framework și utilizarea lui într-altul.

3. **Capabilități multimodale**: Pe lângă NLP, Hugging Face Transformers suportă și sarcini în domeniul viziunii computerizate (de exemplu, clasificarea imaginilor, detectarea obiectelor) și procesarea audio (de exemplu, recunoașterea vorbirii, clasificarea audio).

4. **Ușurință în utilizare**: Biblioteca oferă API-uri și unelte pentru descărcarea și reglarea fină a modelelor, făcând-o accesibilă atât începătorilor, cât și experților.

5. **Comunitate și resurse**: Hugging Face are o comunitate activă și documentație extinsă, tutoriale și ghiduri pentru a ajuta utilizatorii să înceapă și să profite la maxim de bibliotecă.
[documentația oficială](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) sau depozitul lor [GitHub](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Aceasta este metoda cea mai utilizată, dar necesită și accelerare GPU. La urma urmei, scenarii precum Vision și MoE necesită multe calcule, ceea ce va fi foarte lent pe CPU dacă nu sunt cuantificate.


- Demo: Utilizarea Transformer pentru a apela Phi-3.5-Instruct [Faceți clic pe acest link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Utilizarea Transformer pentru a apela Phi-3.5-Vision [Faceți clic pe acest link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Utilizarea Transformer pentru a apela Phi-3.5-MoE [Faceți clic pe acest link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) este o platformă creată pentru a facilita rularea modelelor mari de limbaj (LLM) local, pe mașina ta. Suportă diverse modele precum Llama 3.1, Phi 3, Mistral și Gemma 2, printre altele. Platforma simplifică procesul prin pachetarea greutăților modelului, configurației și datelor într-un singur pachet, făcând-o mai accesibilă pentru utilizatori să personalizeze și să creeze propriile modele. Ollama este disponibil pentru macOS, Linux și Windows. Este un instrument excelent dacă dorești să experimentezi sau să implementezi LLM-uri fără a depinde de servicii cloud. Ollama este cea mai directă cale, trebuie doar să execuți următoarea comandă.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) este mediul offline, local, al Microsoft pentru rularea modelelor precum Phi integral pe hardware-ul propriu - nu necesită abonament Azure, cheie API sau conexiune la rețea. Selectează automat cel mai bun furnizor de execuție disponibil (NPU, GPU sau CPU) și expune un endpoint compatibil OpenAI, astfel încât codul existent folosind SDK-ul `openai`/Azure AI Inference să poată face trimitere la acesta cu schimbări minime. Vedeți [documentația Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) pentru a începe.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Sau folosiți SDK-ul direct în Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime pentru GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) este un accelerator cross-platform pentru inferență și antrenament în învățarea automată. ONNX Runtime pentru AI Generativ (GENAI) este un instrument puternic care ajută la rularea eficientă a modelelor AI generative pe diverse platforme. 

## Ce este ONNX Runtime?
ONNX Runtime este un proiect open-source care permite inferență de înaltă performanță a modelelor de învățare automată. Suportă modele în formatul Open Neural Network Exchange (ONNX), care este un standard pentru reprezentarea modelelor de învățare automată. Inferența cu ONNX Runtime poate asigura experiențe mai rapide pentru clienți și costuri mai reduse, suportând modele din framework-uri de deep learning precum PyTorch și TensorFlow/Keras, precum și biblioteci clasice de machine learning precum scikit-learn, LightGBM, XGBoost, etc. ONNX Runtime este compatibil cu hardware, drivere și sisteme de operare diferite și oferă performanțe optime prin utilizarea acceleratoarelor hardware unde este cazul, combinat cu optimizări și transformări ale grafurilor.

## Ce este AI Generativ?
AI generativ se referă la sistemele AI care pot genera conținut nou, cum ar fi text, imagini sau muzică, pe baza datelor pe care au fost antrenate. Exemple includ modele de limbaj precum GPT-3 și modele de generare a imaginilor precum Stable Diffusion. Biblioteca ONNX Runtime pentru GenAI oferă ciclul AI generativ pentru modelele ONNX, inclusiv inferență cu ONNX Runtime, procesarea logits-urilor, căutare și eșantionare și managementul cache-ului KV.

## ONNX Runtime pentru GENAI
ONNX Runtime pentru GENAI extinde capabilitățile ONNX Runtime pentru a sprijini modelele AI generative. Iată câteva caracteristici cheie:

- **Suport larg pentru platforme:** Funcționează pe diverse platforme, inclusiv Windows, Linux, macOS, Android și iOS.
- **Suport pentru modele:** Suportă multe modele populare de AI generativ, precum LLaMA, GPT-Neo, BLOOM și altele.
- **Optimizare a performanței:** Include optimizări pentru diferite acceleratoare hardware, precum GPU-uri NVIDIA, GPU-uri AMD și altele2.
- **Ușurință în utilizare:** Oferă API-uri pentru integrare ușoară în aplicații, permițând generarea de text, imagini și alt conținut cu un cod minim.
- Utilizatorii pot apela o metodă de nivel înalt generate() sau pot rula fiecare iterație a modelului într-un ciclu, generând câte un token pe rând și, opțional, actualizând parametrii de generare în interiorul buclei.
- ONNX runtime suportă de asemenea căutare greedy/beam și eșantionare TopP, TopK pentru a genera secvențe de tokeni și procesare încorporată a logits-urilor precum penalizările de repetiție. De asemenea, poți adăuga ușor scorare personalizată.

## Începem
Pentru a începe cu ONNX Runtime pentru GENAI, poți urma acești pași:

### Instalează ONNX Runtime:
```Python
pip install onnxruntime
```
### Instalează extensiile pentru AI Generativ:
```Python
pip install onnxruntime-genai
```

### Rulează un model: Iată un exemplu simplu în Python:
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
### Demo: Utilizarea ONNX Runtime GenAI pentru a apela Phi-3.5-Vision


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


**Altele**

Pe lângă metodele de referință ONNX Runtime, Ollama și Foundry Local, putem, de asemenea, completa referința modelelor cantitative bazate pe metodele de referință modele oferite de diferiți producători. Cum ar fi frameworkul MLX de la Apple cu Apple Metal, Qualcomm QNN cu NPU, Intel OpenVINO cu CPU/GPU, etc. Poți găsi mai mult conținut în [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Mai mult

Am învățat elementele de bază ale familiei Phi-3/3.5, dar pentru a afla mai multe despre SLM avem nevoie de mai multe cunoștințe. Poți găsi răspunsurile în Phi-3 Cookbook. Dacă dorești să afli mai multe, te rugăm să vizitezi [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->