# Introducere în Modelele de Limbaj Mici pentru AI Generativ pentru Începători
AI generativ este un domeniu fascinant al inteligenței artificiale care se concentrează pe crearea de sisteme capabile să genereze conținut nou. Acest conținut poate varia de la text și imagini la muzică și chiar medii virtuale întregi. Una dintre cele mai incitante aplicații ale AI generativ este în domeniul modelelor de limbaj.

## Ce sunt Modelele de Limbaj Mici?

Un Model de Limbaj Mic (SLM) reprezintă o variantă redusă a unui model de limbaj mare (LLM), valorificând multe dintre principiile arhitecturale și tehnicile LLM-urilor, în timp ce prezintă o amprentă computațională semnificativ redusă.

SLM-urile sunt un subset de modele de limbaj concepute pentru a genera text asemănător cu cel al omului. Spre deosebire de omologii lor mai mari, cum ar fi GPT-4, SLM-urile sunt mai compacte și eficiente, ceea ce le face ideale pentru aplicații unde resursele computaționale sunt limitate. În ciuda dimensiunii mai mici, acestea pot îndeplini o varietate de sarcini. De obicei, SLM-urile sunt construite prin comprimarea sau distilarea LLM-urilor, cu scopul de a păstra o porțiune substanțială din funcționalitatea și capabilitățile lingvistice ale modelului original. Această reducere a dimensiunii modelului scade complexitatea generală, făcând SLM-urile mai eficiente atât în termeni de utilizare a memoriei, cât și a cerințelor computaționale. În ciuda acestor optimizări, SLM-urile pot încă realiza o gamă largă de sarcini de procesare a limbajului natural (NLP):

- Generarea de text: Crearea de propoziții sau paragrafe coerente și contextual relevante.
- Completarea textului: Prezicerea și completarea propozițiilor bazate pe un prompt dat.
- Traducerea: Convertirea textului dintr-o limbă în alta.
- Sumare: Condensarea unor texte lungi în rezumate mai scurte și mai digerabile.

Deși cu unele compromisuri în performanță sau profunzimea înțelegerii comparativ cu omologii lor mai mari.

## Cum Funcționează Modelele de Limbaj Mici?
SLM-urile sunt antrenate pe cantități vaste de date text. În timpul antrenamentului, ele învață modele și structuri ale limbii, permițându-le să genereze text care este atât gramatical corect, cât și contextuat corespunzător. Procesul de antrenament implică:

- Colectarea Datelor: Adunarea unor seturi mari de date text din diverse surse.
- Preprocesare: Curățarea și organizarea datelor pentru a fi potrivite pentru antrenament.
- Antrenament: Folosirea algoritmilor de învățare automată pentru a învăța modelul cum să înțeleagă și să genereze text.
- Ajustare Fină: Reglarea modelului pentru a-i îmbunătăți performanța pe sarcini specifice.

Dezvoltarea SLM-urilor este corelată cu nevoia crescută de modele care pot fi implementate în medii cu resurse limitate, cum ar fi dispozitive mobile sau platforme de edge computing, unde LLM-urile pe scară largă pot fi nepractice din cauza cerințelor lor mari de resurse. Concentrându-se pe eficiență, SLM-urile echilibrează performanța cu accesibilitatea, permițând o aplicare mai largă în diverse domenii.

![slm](../../../translated_images/ro/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Obiectivele Învățării

În această lecție, sperăm să introducem cunoștințele despre SLM și să le combinăm cu Microsoft Phi-3 pentru a învăța diferite scenarii în conținut text, viziune și MoE.

Până la finalul acestei lecții, ar trebui să puteți răspunde la următoarele întrebări:

- Ce este SLM?
- Care este diferența între SLM și LLM?
- Ce este Familia Microsoft Phi-3/3.5?
- Cum se face inferența cu Familia Microsoft Phi-3/3.5?

Gata? Să începem.

## Distincțiile dintre Modelele Mari de Limbaj (LLM) și Modelele Mici de Limbaj (SLM)

Atât LLM-urile, cât și SLM-urile sunt construite pe principii fundamentale ale învățării automate probabilistice, urmând abordări similare în designul arhitectural, metodologiile de antrenament, procesele de generare a datelor și tehnicile de evaluare a modelelor. Totuși, mai mulți factori cheie diferențiază aceste două tipuri de modele.

## Aplicații ale Modelelor de Limbaj Mici

SLM-urile au o gamă largă de aplicații, inclusiv:

- Chatbot-uri: Oferirea de suport clienților și interacțiunea cu utilizatorii într-un mod conversational.
- Crearea de Conținut: Asistarea scriitorilor prin generarea de idei sau chiar redactarea unor articole întregi.
- Educație: Ajutarea elevilor la teme de scriere sau la învățarea de limbi noi.
- Accesibilitate: Crearea de instrumente pentru persoanele cu dizabilități, cum ar fi sistemele text-la-vorbire.

**Dimensiune**
  
O distincție principală între LLM-uri și SLM-uri constă în scala modelelor. LLM-urile, cum ar fi ChatGPT (GPT-4), pot cuprinde aproximativ 1,76 trilioane de parametri, în timp ce SLM-urile open-source precum Mistral 7B sunt proiectate cu un număr semnificativ mai mic — aproximativ 7 miliarde. Această disparitate se datorează în principal diferențelor în arhitectura modelului și în procesul de antrenament. De exemplu, ChatGPT folosește un mecanism de auto-atentie într-un cadru encoder-decoder, pe când Mistral 7B utilizează atenția cu fereastră glisantă, ceea ce permite un antrenament mai eficient într-un model doar decoder. Această variație arhitecturală are implicații profunde asupra complexității și performanței acestor modele.

**Înțelegere**

SLM-urile sunt de obicei optimizate pentru performanță în domenii specifice, ceea ce le face foarte specializate, dar potențial limitate în capacitatea lor de a oferi o înțelegere contextuală largă în multiple domenii de cunoaștere. În contrast, LLM-urile urmăresc să simuleze o inteligență asemănătoare celei umane la un nivel mai cuprinzător. Antrenate pe seturi vaste și diverse de date, LLM-urile sunt proiectate să performeze bine în multe domenii, oferind o versatilitate și adaptabilitate mai mare. Prin urmare, LLM-urile sunt mai potrivite pentru o gamă mai largă de sarcini downstream, cum ar fi procesarea limbajului natural și programarea.

**Calcul**

Antrenamentul și implementarea LLM-urilor sunt procese consumatoare de resurse, necesitând adesea infrastructură computațională semnificativă, inclusiv clustere GPU la scară largă. De exemplu, antrenarea unui model ca ChatGPT de la zero poate necesita mii de GPU-uri pe perioade extinse. În contrast, SLM-urile, cu numere mai mici de parametri, sunt mai accesibile în termeni de resurse computaționale. Modele precum Mistral 7B pot fi antrenate și rulate pe mașini locale echipate cu GPU-uri moderate, deși antrenamentul necesită totuși câteva ore pe mai multe GPU-uri.

**Bias**

Biasul este o problemă cunoscută la LLM-uri, în principal din cauza naturii datelor de antrenament. Aceste modele se bazează adesea pe date brute, disponibile liber pe internet, care pot subreprezenta sau reprezenta eronat anumite grupuri, pot introduce etichetări greșite sau reflectă biasuri lingvistice influențate de dialect, variații geografice și reguli gramaticale. De asemenea, complexitatea arhitecturii LLM-urilor poate agrava inadvertent biasul, care poate trece neobservat fără o ajustare atentă. Pe de altă parte, SLM-urile, fiind antrenate pe seturi de date mai restrânse, specifice domeniului, sunt în mod inerent mai puțin susceptibile la astfel de biasuri, deși nu sunt imune.

**Inferență**

Dimensiunea redusă a SLM-urilor le oferă un avantaj semnificativ în ceea ce privește viteza de inferență, permițându-le să genereze rezultate eficient pe hardware local fără necesitatea de procesare paralelă extinsă. În contrast, LLM-urile, datorită dimensiunii și complexității, necesită adesea resurse computaționale paralele substanțiale pentru a obține timpi acceptabili de inferență. Prezența mai multor utilizatori concurenți încetinește și mai mult timpii de răspuns ai LLM-urilor, în special când sunt implementate la scară largă.

În concluzie, deși atât LLM-urile cât și SLM-urile împărtășesc o bază fundamentală în învățarea automată, ele diferă semnificativ în ceea ce privește dimensiunea modelului, cerințele de resurse, înțelegerea contextuală, susceptibilitatea la bias și viteza de inferență. Aceste distincții reflectă potrivirea lor respectivă pentru diferite cazuri de utilizare, LLM-urile fiind mai versatile, dar consumatoare de resurse, iar SLM-urile oferind o eficiență mai specifică domeniului, cu cerințe computaționale reduse.

***Notă: În această lecție, vom introduce SLM folosind Microsoft Phi-3 / 3.5 ca exemplu.***

## Introducerea Familiei Phi-3 / Phi-3.5

Familia Phi-3 / 3.5 vizează în principal scenarii de aplicații în text, viziune și Agent (MoE):

### Phi-3 / 3.5 Instruct

În principal pentru generare de text, completare de chat și extragere de informații din conținut, etc.

**Phi-3-mini**

Modelul de limbaj cu 3,8 miliarde de parametri este disponibil pe Microsoft Foundry, Hugging Face și Ollama. Modelele Phi-3 depășesc semnificativ modelele de limbaj de dimensiuni egale și mai mari pe reperele cheie (vezi numerele de benchmark de mai jos, numerele mai mari sunt mai bune). Phi-3-mini depășește modelele de două ori mai mari, în timp ce Phi-3-small și Phi-3-medium depășesc modele mai mari, inclusiv GPT-3.5.

**Phi-3-small & medium**

Cu doar 7 miliarde de parametri, Phi-3-small depășește GPT-3.5T în diverse repere de limbaj, raționament, programare și matematică.

Phi-3-medium cu 14 miliarde de parametri continuă această tendință și depășește Gemini 1.0 Pro.

**Phi-3.5-mini**

Îl putem considera o versiune îmbunătățită a Phi-3-mini. Deși numărul parametrilor rămâne neschimbat, îmbunătățește capacitatea de a susține mai multe limbi (acceptă peste 20 de limbi: arabă, chineză, cehă, daneză, olandeză, engleză, finlandeză, franceză, germană, ebraică, maghiară, italiană, japoneză, coreeană, norvegiană, poloneză, portugheză, rusă, spaniolă, suedeză, thailandeză, turcă, ucraineană) și adaugă un suport mai puternic pentru context lung.

Phi-3.5-mini cu 3,8 miliarde de parametri depășește modelele de limbaj de aceeași dimensiune și este comparabil cu modele de două ori mai mari.

### Phi-3 / 3.5 Vision

Putem considera modelul Instruct al Phi-3/3.5 ca fiind abilitatea Phi de a înțelege, iar Vision este ceea ce îi oferă lui Phi ochi pentru a înțelege lumea.


**Phi-3-Vision**

Phi-3-vision, cu doar 4,2 miliarde de parametri, continuă această tendință și depășește modele mai mari precum Claude-3 Haiku și Gemini 1.0 Pro V pe sarcini generale de raționament vizual, OCR și înțelegerea tabelelor și diagramelor.


**Phi-3.5-Vision**

Phi-3.5-Vision este, de asemenea, o actualizare a Phi-3-Vision, adăugând suport pentru imagini multiple. Îl puteți considera o îmbunătățire a viziunii, nu doar poate vedea poze, ci și videoclipuri.

Phi-3.5-vision depășește modele mai mari precum Claude-3.5 Sonnet și Gemini 1.5 Flash în sarcini de OCR, înțelegerea tabelelor și diagramelor și este comparabil în sarcini generale de raționament vizual. Suportă input multi-frame, adică poate efectua raționamente pe mai multe imagini de input.


### Phi-3.5-MoE

***Mixtura de Experți (Mixture of Experts, MoE)*** permite modelelor să fie pre-antrenate cu mult mai puțin calcul, ceea ce înseamnă că poți scala dramatic dimensiunea modelului sau a setului de date cu același buget de calcul ca un model dens. În special, un model MoE ar trebui să atingă aceeași calitate ca omologul său dens mult mai rapid în timpul preantrenamentului.

Phi-3.5-MoE cuprinde 16 module de experți de 3,8 miliarde fiecare. Phi-3.5-MoE cu doar 6,6 miliarde de parametri activi atinge un nivel similar de raționament, înțelegere a limbajului și matematică ca modele mult mai mari.

Putem folosi modelul din Familia Phi-3/3.5 în funcție de diferite scenarii. Spre deosebire de LLM, poți implementa Phi-3/3.5-mini sau Phi-3/3.5-Vision pe dispozitive edge.


## Cum să folosești modelele din Familia Phi-3/3.5

Sperăm să folosim Phi-3/3.5 în diferite scenarii. Următorul pas este să folosim Phi-3/3.5 în funcție de aceste scenarii.

![phi3](../../../translated_images/ro/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inferență prin API-uri Cloud

**Modele Microsoft Foundry**

> **Notă:** GitHub Models va fi retras la sfârșitul lunii iulie 2026. [Modelele Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) sunt înlocuirea directă.

Microsoft Foundry Models este cea mai directă cale. Poți accesa rapid modelul Phi-3/3.5-Instruct prin catalogul de modele Foundry. Împreună cu Azure AI Inference SDK / OpenAI SDK, poți accesa API-ul prin cod pentru a realiza apelul către Phi-3/3.5-Instruct. De asemenea, poți testa diferite efecte prin intermediul Playground-ului.

- Demo: Comparație a efectelor dintre Phi-3-mini și Phi-3.5-mini în scenarii chinezești

![phi3](../../../translated_images/ro/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/ro/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Sau dacă dorim să folosim modelele de viziune și MoE, poți folosi Microsoft Foundry pentru a realiza apelul. Dacă ești interesat, poți citi Phi-3 Cookbook pentru a învăța cum să apelezi Phi-3/3.5 Instruct, Vision, MoE prin Microsoft Foundry [Click pe acest link](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Pe lângă catalogul Microsoft Foundry Models bazat pe cloud, poți folosi și [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) pentru a realiza apeluri aferente. Poți vizita NVIDIA NIM pentru a efectua apelurile API ale Familiei Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) este un set de microservicii accelerate pentru inferență concepute să ajute dezvoltatorii să implementeze eficient modele AI în diverse medii, inclusiv cloud-uri, centre de date și stații de lucru.

Iată câteva caracteristici cheie ale NVIDIA NIM:

- **Ușurința implementării:** NIM permite implementarea modelelor AI cu o singură comandă, făcând integrarea în fluxuri de lucru existente simplă.
- **Performanță optimizată:** Folosește motoarele de inferență preoptimizate NVIDIA, cum ar fi TensorRT și TensorRT-LLM, pentru a asigura latență scăzută și debit ridicat.
- **Scalabilitate:** NIM suportă autoscalare pe Kubernetes, permițând gestionarea eficientă a diferitelor încărcări de lucru.
- **Securitate și Control:** Organizațiile pot păstra controlul asupra datelor și aplicațiilor prin găzduirea propriilor microservicii NIM pe infrastructura administrată de ele.
- **API-uri standard:** NIM oferă API-uri conforme cu standardele din industrie, facilitând construirea și integrarea aplicațiilor AI precum chatboți, asistenți AI și altele.

NIM face parte din NVIDIA AI Enterprise, care are ca scop simplificarea implementării și operaționalizării modelelor AI, asigurându-se că acestea rulează eficient pe GPU-urile NVIDIA.

- Demo: Folosirea NVIDIA NIM pentru a apela Phi-3.5-Vision-API [[Click this link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Rularea Phi-3/3.5 Local
Inferența în legătură cu Phi-3, sau orice model de limbaj precum GPT-3, se referă la procesul de generare a răspunsurilor sau predicțiilor bazate pe intrarea primită. Atunci când oferi o prompt sau o întrebare lui Phi-3, acesta folosește rețeaua sa neuronală antrenată pentru a deduce răspunsul cel mai probabil și relevant, analizând tiparele și relațiile din datele pe care a fost antrenat.

**Hugging Face Transformer**
Hugging Face Transformers este o bibliotecă puternică concepută pentru procesarea limbajului natural (NLP) și alte sarcini de învățare automată. Iată câteva puncte cheie despre aceasta:

1. **Modele Pre-antrenate**: Oferă mii de modele pre-antrenate care pot fi utilizate pentru diverse sarcini precum clasificarea textului, recunoașterea entităților denumite, răspunsul la întrebări, sumarizarea, traducerea și generarea de text.

2. **Interoperabilitate între Framework-uri**: Biblioteca suportă multiple framework-uri de deep learning, inclusiv PyTorch, TensorFlow și JAX. Acest lucru permite antrenarea unui model într-un framework și utilizarea lui într-altul.

3. **Capabilități Multimodale**: Pe lângă NLP, Hugging Face Transformers sprijină și sarcini în domeniul viziunii computerizate (de exemplu, clasificarea imaginilor, detectarea obiectelor) și procesarea audio (de exemplu, recunoașterea vorbirii, clasificarea audio).

4. **Ușurință în Utilizare**: Biblioteca oferă API-uri și unelte pentru a descărca și ajusta ușor modelele, făcând-o accesibilă atât pentru începători, cât și pentru experți.

5. **Comunitate și Resurse**: Hugging Face are o comunitate vibrantă și documentație extensivă, tutoriale și ghiduri pentru a ajuta utilizatorii să înceapă și să profite la maximum de bibliotecă.
[documentația oficială](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) sau depozitul lor de pe [GitHub](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Aceasta este metoda cea mai des utilizată, dar de asemenea necesită accelerare GPU. La urma urmei, scenarii precum Vision și MoE necesită multe calcule, care vor fi foarte lente pe CPU dacă nu sunt cuantizate.


- Demo: Folosirea Transformer pentru a apela Phi-3.5-Instruct [Click this link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Folosirea Transformer pentru a apela Phi-3.5-Vision [Click this link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Folosirea Transformer pentru a apela Phi-3.5-MoE [Click this link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) este o platformă concepută pentru a facilita rularea modelelor mari de limbaj (LLM-uri) local pe mașina ta. Suportă diverse modele precum Llama 3.1, Phi 3, Mistral și Gemma 2, printre altele. Platforma simplifică procesul prin gruparea greutăților modelului, a configurării și a datelor într-un singur pachet, făcându-l mai accesibil pentru utilizatori să personalizeze și să creeze propriile modele. Ollama este disponibil pentru macOS, Linux și Windows. Este un instrument excelent dacă dorești să experimentezi sau să implementezi LLM-uri fără a depinde de servicii cloud. Ollama este cea mai directă cale, trebuie doar să execuți următoarea comandă.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) este rularea offline, pe dispozitiv, a Microsoft pentru a rula modele precum Phi complet pe hardware-ul propriu - nu este nevoie de abonament Azure, cheie API sau conexiune la rețea. Selectează automat cel mai bun furnizor de execuție disponibil (NPU, GPU sau CPU) și expune un endpoint compatibil OpenAI, astfel încât codul existent `openai`/Azure AI Inference SDK să poată fi direcționat către acesta cu modificări minimale. Consultă [documentația Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) pentru a începe.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Sau utilizează SDK-ul direct în Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime pentru GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) este un accelerator cross-platform pentru inferență și antrenare în învățarea automată. ONNX Runtime pentru Generative AI (GENAI) este un instrument puternic care ajută la rularea eficientă a modelelor AI generative pe diverse platforme.

## Ce este ONNX Runtime?
ONNX Runtime este un proiect open-source care permite inferența de înaltă performanță a modelelor de învățare automată. Suportă modele în formatul Open Neural Network Exchange (ONNX), care este un standard pentru reprezentarea modelelor de învățare automată. Inferența cu ONNX Runtime poate asigura experiențe mai rapide pentru utilizatori și costuri reduse, suportând modele din framework-uri de deep learning precum PyTorch și TensorFlow/Keras, precum și biblioteci clasice de învățare automată cum ar fi scikit-learn, LightGBM, XGBoost etc. ONNX Runtime este compatibil cu hardware diferit, drivere și sisteme de operare, oferind performanțe optime prin folosirea acceleratorilor hardware acolo unde este cazul, împreună cu optimizări și transformări ale graficului.

## Ce este Generative AI?
Generative AI se referă la sisteme AI care pot genera conținut nou, cum ar fi text, imagini sau muzică, bazându-se pe datele pe care au fost antrenate. Exemple includ modele de limbaj precum GPT-3 și modele de generare a imaginilor precum Stable Diffusion. Biblioteca ONNX Runtime pentru GenAI oferă bucla AI generative pentru modelele ONNX, inclusiv inferența cu ONNX Runtime, procesarea logits, căutarea și eșantionarea, și gestionarea cache-ului KV.

## ONNX Runtime pentru GENAI
ONNX Runtime pentru GENAI extinde capabilitățile ONNX Runtime pentru a susține modele AI generative. Iată câteva caracteristici cheie:

- **Suport larg pentru platforme:** Funcționează pe diverse platforme, inclusiv Windows, Linux, macOS, Android și iOS.
- **Suport pentru modele:** Suportă multe modele generative populare, precum LLaMA, GPT-Neo, BLOOM și altele.
- **Optimizarea performanței:** Include optimizări pentru diferiți acceleratori hardware precum GPU-uri NVIDIA, GPU-uri AMD și altele.
- **Ușurință în utilizare:** Oferă API-uri pentru integrare ușoară în aplicații, permițând generarea de text, imagini și alte conținuturi cu cod minim.
- Utilizatorii pot apela metoda de nivel înalt generate(), sau pot rula fiecare iterație a modelului într-un ciclu, generând un token pe rând, și, opțional, actualizând parametrii de generare în interiorul ciclului.
- ONNX runtime suportă de asemenea căutarea greedy/beam și eșantionarea TopP, TopK pentru a genera secvențe de tokeni și procesarea încorporată a logits precum penalități de repetare. Poți de asemenea să adaugi evaluare personalizată cu ușurință.

## Începeți
Pentru a începe cu ONNX Runtime pentru GENAI, poți urma acești pași:

### Instalează ONNX Runtime:
```Python
pip install onnxruntime
```
### Instalează extensiile Generative AI:
```Python
pip install onnxruntime-genai
```

### Rulează un Model: Iată un exemplu simplu în Python:
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
### Demo: Folosirea ONNX Runtime GenAI pentru a apela Phi-3.5-Vision


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

Pe lângă metodele de referință ONNX Runtime, Ollama și Foundry Local, putem de asemenea să completăm referința modelelor cantitative pe baza metodelor de referință oferite de diferiți producători. De exemplu, cadrul Apple MLX cu Apple Metal, Qualcomm QNN cu NPU, Intel OpenVINO cu CPU/GPU etc. Poți găsi și mai mult conținut în [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Mai mult

Am învățat elementele de bază ale familiei Phi-3/3.5, dar pentru a învăța mai multe despre SLM avem nevoie de mai multe cunoștințe. Poți găsi răspunsurile în Phi-3 Cookbook. Dacă dorești să înveți mai mult, te rugăm să vizitezi [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->