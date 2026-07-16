# Introducere în Modelele de Limbaj Mici pentru AI Generativ destinat Începătorilor
AI generativ este un domeniu fascinant al inteligenței artificiale care se concentrează pe crearea de sisteme capabile să genereze conținut nou. Acest conținut poate varia de la text și imagini la muzică și chiar medii virtuale complete. Una dintre cele mai interesante aplicații ale AI generativ este în domeniul modelelor de limbaj.

## Ce Sunt Modelele de Limbaj Mici?

Un Model de Limbaj Mic (SLM) reprezintă o variantă redusă a unui model de limbaj mare (LLM), folosind multe dintre principiile arhitecturale și tehnicile LLM-urilor, în timp ce prezintă o amprentă computațională semnificativ redusă. 

SLM-urile sunt un subset de modele de limbaj proiectate să genereze text asemănător celui uman. Spre deosebire de omologii lor mai mari, cum ar fi GPT-4, SLM-urile sunt mai compacte și eficiente, fiind ideale pentru aplicații în care resursele computaționale sunt limitate. În ciuda dimensiunii mai mici, ele pot efectua o varietate de sarcini. De obicei, SLM-urile sunt construite prin comprimarea sau distilarea LLM-urilor, cu scopul de a păstra o porțiune semnificativă din funcționalitatea și capacitățile lingvistice ale modelului original. Această reducere a dimensiunii modelului scade complexitatea generală, făcând SLM-urile mai eficiente atât în ceea ce privește utilizarea memoriei, cât și cerințele computaționale. În ciuda acestor optimizări, SLM-urile pot efectua încă o gamă largă de sarcini de procesare a limbajului natural (NLP):

- Generare de text: Crearea de propoziții sau paragrafe coerente și contextual relevante.
- Completarea textului: Prezicerea și completarea propozițiilor pe baza unui prompt dat.
- Traducere: Conversia textului dintr-o limbă în alta.
- Rezumare: Condensarea unor texte lungi în rezumate mai scurte și mai ușor de digerat.

Deși cu unele compromisuri în performanță sau adâncime a înțelegerii în comparație cu omologii lor mai mari. 

## Cum Funcționează Modelele de Limbaj Mici?
SLM-urile sunt antrenate pe cantități vaste de date textuale. În timpul antrenamentului, ele învață pattern-urile și structurile limbajului, permițându-le să genereze text care este atât gramatical corect, cât și contextual adecvat. Procesul de antrenament implică:

- Colectarea datelor: Adunarea unor seturi mari de date textuale din diverse surse.
- Preprocesarea: Curățarea și organizarea datelor pentru a le face potrivite pentru antrenament.
- Antrenarea: Utilizarea algoritmilor de învățare automată pentru a învăța modelul cum să înțeleagă și să genereze text.
- Ajustarea fină: Modificarea modelului pentru a-i îmbunătăți performanța în sarcini specifice.

Dezvoltarea SLM-urilor corespunde nevoii crescânde de modele care pot fi implementate în medii cu resurse limitate, cum ar fi dispozitive mobile sau platforme de edge computing, unde LLM-urile la scară largă pot fi nepracticabile din cauza cererii mari de resurse. Prin concentrarea pe eficiență, SLM-urile echilibrează performanța cu accesibilitatea, permițând o aplicare mai largă în diverse domenii.

![slm](../../../translated_images/ro/slm.4058842744d0444a.webp)

## Obiective de Învățare

În această lecție, ne propunem să introducem cunoștințele despre SLM și să le combinăm cu Microsoft Phi-3 pentru a învăța diferite scenarii în conținut text, viziune și MoE.

La finalul acestei lecții, ar trebui să puteți răspunde la următoarele întrebări:

- Ce este SLM?
- Care este diferența dintre SLM și LLM?
- Ce este Familia Microsoft Phi-3/3.5?
- Cum se execută inferența cu Familia Microsoft Phi-3/3.5?

Sunteți gata? Haideți să începem.

## Distincțiile dintre Modelele de Limbaj Mari (LLM) și Modelele de Limbaj Mici (SLM)

Atât LLM-urile, cât și SLM-urile sunt construite pe principii fundamentale de învățare automată probabilistică, urmând abordări similare în design-ul arhitectural, metodologiile de antrenament, procesele de generare a datelor și tehnicile de evaluare a modelelor. Totuși, câțiva factori cheie diferențiază aceste două tipuri de modele.

## Aplicații ale Modelelor de Limbaj Mici

SLM-urile au o gamă largă de aplicații, inclusiv:

- Chatbots: Oferirea de suport clienților și interacțiune cu utilizatorii într-un mod conversațional.
- Crearea de conținut: Asistență pentru scriitori prin generarea de idei sau chiar redactarea unor articole întregi.
- Educație: Ajutor pentru studenți la temele de scriere sau învățarea unor limbi noi.
- Accesibilitate: Crearea de instrumente pentru persoane cu dizabilități, cum ar fi sistemele de text-la-vorbire.

**Dimensiunea**
  
O diferență principală între LLM și SLM constă în scara modelelor. LLM-urile, precum ChatGPT (GPT-4), pot cuprinde un număr estimat de 1,76 trilioane de parametri, în timp ce SLM-urile open-source precum Mistral 7B sunt proiectate cu un număr semnificativ mai mic de parametri — aproximativ 7 miliarde. Această disparitate este datorată în principal diferențelor în arhitectura modelului și în procesele de antrenament. De exemplu, ChatGPT utilizează un mecanism de auto-atentție în cadrul unei structuri encoder-decoder, pe când Mistral 7B folosește atenția cu fereastră mobilă, care permite un antrenament mai eficient într-un model doar cu decoder. Această variație arhitecturală are implicații profunde asupra complexității și performanței acestor modele.

**Comprehensiunea**

SLM-urile sunt de obicei optimizate pentru performanță în domenii specifice, făcându-le foarte specializate, dar potențial limitate în capacitatea lor de a oferi o înțelegere contextuală extinsă în mai multe domenii de cunoștințe. În contrast, LLM-urile urmăresc să simuleze inteligența asemănătoare celor umane la un nivel mai cuprinzător. Antrenate pe seturi mari și diverse de date, LLM-urile sunt proiectate să performeze bine într-o varietate de domenii, oferind o mai mare versatilitate și adaptabilitate. Drept urmare, LLM-urile sunt mai potrivite pentru o gamă mai largă de sarcini aferente, cum ar fi procesarea limbajului natural și programarea.

**Calculul**

Antrenarea și implementarea LLM-urilor sunt procese consumatoare de resurse, necesitând adesea infrastructură computațională semnificativă, inclusiv clustere GPU la scară largă. De exemplu, antrenarea unui model precum ChatGPT de la zero poate necesita mii de GPU-uri pe perioade extinse. În contrast, SLM-urile, cu un număr mai mic de parametri, sunt mai accesibile din punct de vedere al resurselor computaționale. Modele precum Mistral 7B pot fi antrenate și rulate pe calculatoare locale echipate cu capacități moderate GPU, deși antrenamentul necesită totuși câteva ore pe mai multe GPU-uri.

**Bias**

Biasul este o problemă cunoscută în LLM-uri, în principal datorită naturii datelor de antrenament. Aceste modele se bazează adesea pe date brute disponibile pe internet, care pot subreprezenta sau reprezenta greșit anumite grupuri, pot introduce etichetări eronate sau reflectă biasuri lingvistice influențate de dialect, variații geografice și reguli gramaticale. În plus, complexitatea arhitecturilor LLM poate agrava inadvertent biasul, care poate trece neobservat fără o ajustare atentă. Pe de altă parte, SLM-urile, fiind antrenate pe seturi de date mai restrânse și specifice domeniului, sunt inerent mai puțin susceptibile la astfel de biasuri, deși nu sunt imune la ele.

**Inferența**

Dimensiunea redusă a SLM-urilor le oferă un avantaj semnificativ în ceea ce privește viteza de inferență, permițându-le să genereze rezultate eficient pe hardware local, fără necesitatea procesării paralele extinse. În contrast, LLM-urile, datorită dimensiunii și complexității lor, necesită adesea resurse computaționale paralele substanțiale pentru a atinge timpi acceptabili de inferență. Prezența mai multor utilizatori concurenți încetinește și mai mult timpii de răspuns ai LLM-urilor, în special când sunt implementate la scară largă.

În rezumat, deși atât LLM-urile cât și SLM-urile împărtășesc o bază fundamentală în învățarea automată, ele diferă semnificativ în ceea ce privește dimensiunea modelului, cerințele de resurse, înțelegerea contextuală, susceptibilitatea la bias și viteza de inferență. Aceste distincții reflectă potrivirea lor respectivă pentru cazuri de utilizare diferite, LLM-urile fiind mai versatile, dar consumatoare de resurse, iar SLM-urile oferind eficiență specifică domeniului cu cerințe computaționale reduse.

***Notă: În această lecție, vom introduce SLM folosind Microsoft Phi-3 / 3.5 ca exemplu.***

## Introducerea Familiei Phi-3 / Phi-3.5

Familia Phi-3 / 3.5 targetează în principal scenarii de aplicații pentru text, viziune și agent (MoE):

### Phi-3 / 3.5 Instruct

În principal pentru generarea de text, completarea conversațiilor și extragerea informațiilor din conținut, etc.

**Phi-3-mini**

Modelul de limbaj 3.8B este disponibil pe Microsoft Foundry, Hugging Face și Ollama. Modelele Phi-3 depășesc semnificativ modelele de limbaj de dimensiune egală sau mai mare pe repere cheie (vezi numerele benchmark-urilor mai jos, numerele mai mari sunt mai bune). Phi-3-mini depășește modelele de două ori mai mari, în timp ce Phi-3-small și Phi-3-medium depășesc modele mai mari, inclusiv GPT-3.5.

**Phi-3-small & medium**

Cu doar 7 miliarde de parametri, Phi-3-small îl depășește pe GPT-3.5T pe o varietate de repere de limbaj, raționament, codare și matematică.

Phi-3-medium, cu 14 miliarde de parametri, continuă această tendință și îl depășește pe Gemini 1.0 Pro.

**Phi-3.5-mini**

Putem să-l considerăm o versiune îmbunătățită a Phi-3-mini. Deși numărul parametrilor rămâne neschimbat, îmbunătățește capacitatea de a suporta mai multe limbi (suportă peste 20 de limbi: arabă, chineză, cehă, daneză, olandeză, engleză, finlandeză, franceză, germană, ebraică, maghiară, italiană, japoneză, coreeană, norvegiană, poloneză, portugheză, rusă, spaniolă, suedeză, thailandeză, turcă, ucraineană) și adaugă un suport mai puternic pentru contexte lungi.

Phi-3.5-mini cu 3.8 miliarde de parametri depășește modelele de limbaj de aceeași dimensiune și este comparabil cu modele de două ori mai mari.

### Phi-3 / 3.5 Vision

Putem considera modelul Instruct din Phi-3/3.5 ca abilitatea Phi de a înțelege, iar Vision este ceea ce îi oferă lui Phi ochi pentru a înțelege lumea.


**Phi-3-Vision**

Phi-3-vision, cu doar 4.2 miliarde de parametri, continuă această tendință și depășește modele mai mari precum Claude-3 Haiku și Gemini 1.0 Pro V în sarcini generale de raționament vizual, OCR și înțelegerea tabelelor și diagramelor.


**Phi-3.5-Vision**

Phi-3.5-Vision este, de asemenea, o îmbunătățire a Phi-3-Vision, adăugând suport pentru imagini multiple. Poți să-l consideri o îmbunătățire în viziune, nu doar poate vedea poze, ci și videoclipuri.

Phi-3.5-vision depășește modele mai mari precum Claude-3.5 Sonnet și Gemini 1.5 Flash în sarcini de OCR, înțelegerea tabelelor și graficelor și este comparabil pe sarcini generale de raționament vizual. Suportă intrări multi-frame, adică poate efectua raționamente pe mai multe imagini de intrare.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** permite ca modelele să fie preantrenate cu mult mai puține resurse, ceea ce înseamnă că poți scala dramatic dimensiunea modelului sau a setului de date cu același buget de calcul ca un model dens. În special, un model MoE ar trebui să atingă aceeași calitate ca omologul său dens mult mai rapid în timpul preantrenării.

Phi-3.5-MoE cuprinde 16 module experte de 3.8B fiecare. Phi-3.5-MoE, cu doar 6.6 miliarde de parametri activi, atinge un nivel similar de raționament, înțelegere a limbajului și matematică ca modele mult mai mari.

Putem utiliza modelul Familiei Phi-3/3.5 în funcție de diferite scenarii. Spre deosebire de LLM, poți implementa Phi-3/3.5-mini sau Phi-3/3.5-Vision pe dispozitive edge.


## Cum se folosesc modelele din Familia Phi-3/3.5

Sperăm să folosim Phi-3/3.5 în diverse scenarii. Următorul pas este să folosim Phi-3/3.5 în funcție de diferite scenarii.

![phi3](../../../translated_images/ro/phi3.655208c3186ae381.webp)

### Inferență prin API-uri Cloud

**Modelele Microsoft Foundry**

> **Notă:** GitHub Models se va retrage la sfârșitul lunii iulie 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) este înlocuitorul direct.

Microsoft Foundry Models este cea mai directă metodă. Poți accesa rapid modelul Phi-3/3.5-Instruct prin catalogul de modele Foundry. Combinat cu Azure AI Inference SDK / OpenAI SDK, poți accesa API-ul prin cod pentru a completa apelul Phi-3/3.5-Instruct. De asemenea, poți testa diferite efecte prin intermediul Playground-ului.

- Demo: Compararea efectelor lui Phi-3-mini și Phi-3.5-mini în scenarii în limba chineză

![phi3](../../../translated_images/ro/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/ro/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Sau dacă dorim să utilizăm modelele de viziune și MoE, poți folosi Microsoft Foundry pentru a efectua apelurile. Dacă ești interesat, poți consulta Phi-3 Cookbook pentru a învăța cum să apelezi Phi-3/3.5 Instruct, Vision, MoE prin Microsoft Foundry [Click aici](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Pe lângă catalogul bazat pe cloud Microsoft Foundry Models, poți folosi și [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) pentru a efectua apeluri legate. Poți vizita NVIDIA NIM pentru a efectua apelurile API ale Familiei Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) este un set de microservicii de inferență accelerate, concepute pentru a ajuta dezvoltatorii să implementeze modelele AI eficient în diverse medii, inclusiv în cloud, centre de date și stații de lucru.

Iată câteva caracteristici cheie ale NVIDIA NIM:

- **Ușurință în implementare:** NIM permite implementarea modelelor AI cu o singură comandă, făcând integrarea în fluxurile de lucru existente foarte simplă.

- **Performanță optimizată:** Folosește motoarele de inferență pre-optimizațe NVIDIA, cum ar fi TensorRT și TensorRT-LLM, pentru a asigura latență scăzută și debit ridicat.
- **Scalabilitate:** NIM suportă autoscalarea pe Kubernetes, permițând gestionarea eficientă a volumelor variate de lucru.
- **Securitate și control:** Organizațiile pot păstra controlul asupra datelor și aplicațiilor prin găzduirea propriilor microservicii NIM pe infrastructura administrată de ele.
- **API-uri standard:** NIM oferă API-uri standard din industrie, facilitând construirea și integrarea aplicațiilor AI precum chatboți, asistenți AI și altele.

NIM face parte din NVIDIA AI Enterprise, care își propune să simplifice implementarea și operaționalizarea modelelor AI, asigurând o funcționare eficientă pe GPU-urile NVIDIA.

- Demo: Folosirea NVIDIA NIM pentru a apela Phi-3.5-Vision-API [[Click this link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Rularea Phi-3/3.5 local
Inferența în legătură cu Phi-3, sau orice model de limbaj precum GPT-3, se referă la procesul de generare a răspunsurilor sau predicțiilor bazate pe inputul primit. Când oferi un prompt sau o întrebare către Phi-3, acesta utilizează rețeaua sa neurală antrenată pentru a deduce cel mai probabil și relevant răspuns, analizând tiparele și relațiile din datele pe care a fost antrenat.

**Hugging Face Transformer**
Hugging Face Transformers este o bibliotecă puternică destinată procesării limbajului natural (NLP) și altor sarcini de învățare automată. Iată câteva puncte cheie despre ea:

1. **Modele pre-antrenate**: Oferă mii de modele pre-antrenate ce pot fi utilizate pentru diverse sarcini cum ar fi clasificare text, recunoașterea entităților numite, răspuns la întrebări, sumarizare, traducere și generare de text.

2. **Interoperabilitate a framework-urilor**: Biblioteca suportă mai multe framework-uri de deep learning, inclusiv PyTorch, TensorFlow și JAX. Aceasta permite antrenarea unui model într-un framework și utilizarea lui într-altul.

3. **Capabilități multimodale**: Pe lângă NLP, Hugging Face Transformers suportă și sarcini din domeniul viziunii computerizate (ex: clasificare imagini, detecție obiecte) și procesarea audio (ex: recunoaștere vocală, clasificare audio).

4. **Ușurință în utilizare**: Biblioteca oferă API-uri și unelte pentru a descărca și ajusta modele cu ușurință, fiind accesibilă atât pentru începători, cât și pentru experți.

5. **Comunitate și resurse**: Hugging Face dispune de o comunitate vibrantă și documentație amplă, tutoriale și ghiduri care ajută utilizatorii să înceapă și să profite la maximum de librărie.
[documentația oficială](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) sau depozitul lor de pe [GitHub](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Aceasta este metoda cea mai utilizată, dar necesită și accelerare GPU. În fond, scenarii precum Vision și MoE necesită multe calcule, care vor fi foarte lente pe CPU dacă nu sunt cuantificate.


- Demo: Folosirea Transformer pentru a apela Phi-3.5-Instruct [Click this link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Folosirea Transformer pentru a apela Phi-3.5-Vision [Click this link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Folosirea Transformer pentru a apela Phi-3.5-MoE [Click this link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) este o platformă creată pentru a facilita rularea modelelor mari de limbaj (LLM) local, pe mașina ta. Suportă diverse modele precum Llama 3.1, Phi 3, Mistral și Gemma 2, printre altele. Platforma simplifică procesul prin pachetarea greutăților modelului, configurației și datelor într-un singur pachet, făcând-o mai accesibilă utilizatorilor pentru personalizare și creare de modele proprii. Ollama este disponibil pentru macOS, Linux și Windows. Este un instrument excelent dacă dorești să experimentezi sau să implementezi LLM-uri fără a depinde de servicii cloud. Ollama este cea mai directă cale, trebuie doar să execuți următoarea comandă.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) este mediul de rulare offline, pe dispozitiv, de la Microsoft pentru a rula modele precum Phi integral pe hardware-ul propriu - nu este necesar abonament Azure, cheie API sau conexiune de rețea. Alege automat cel mai bun furnizor de execuție disponibil (NPU, GPU sau CPU) și oferă un endpoint compatibil OpenAI, astfel încât codul existent din `openai`/Azure AI Inference SDK să poată fi folosit cu schimbări minime. Vezi [documentația Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) pentru a începe.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Sau folosește SDK-ul direct în Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime pentru GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) este un accelerator multiplatformă pentru inferență și antrenare de modele de învățare automată. ONNX Runtime pentru Generative AI (GENAI) este un instrument puternic care te ajută să rulezi eficient modele AI generative pe diverse platforme.

## Ce este ONNX Runtime?
ONNX Runtime este un proiect open-source care permite inferențe de înaltă performanță pentru modele de învățare automată. Suportă modele în format Open Neural Network Exchange (ONNX), care este un standard pentru reprezentarea modelelor de machine learning. Inferența ONNX Runtime poate permite experiențe mai rapide pentru utilizatori și costuri mai scăzute, suportând modele din framework-uri de deep learning precum PyTorch și TensorFlow/Keras, precum și librării clasice de machine learning precum scikit-learn, LightGBM, XGBoost etc. ONNX Runtime este compatibil cu diferite hardware-uri, drivere și sisteme de operare, și oferă performanță optimă prin folosirea acceleratoarelor hardware acolo unde este posibil, împreună cu optimizări și transformări ale graficului.

## Ce este AI Generativ?
AI generativ se referă la sisteme AI care pot genera conținut nou, precum text, imagini sau muzică, bazate pe datele pe care au fost antrenate. Exemple includ modele de limbaj precum GPT-3 și modele de generare imagini precum Stable Diffusion. Biblioteca ONNX Runtime pentru GenAI oferă bucla generativă AI pentru modelele ONNX, incluzând inferența cu ONNX Runtime, procesarea logits, căutare și eșantionare, precum și managementul cache-ului KV.

## ONNX Runtime pentru GENAI
ONNX Runtime pentru GENAI extinde capabilitățile ONNX Runtime pentru a suporta modele AI generative. Iată câteva caracteristici cheie:

- **Suport extins pentru platforme:** Funcționează pe diverse platforme, inclusiv Windows, Linux, macOS, Android și iOS.
- **Suport pentru modele:** Suportă multe modele AI generative populare, precum LLaMA, GPT-Neo, BLOOM și altele.
- **Optimizarea performanței:** Include optimizări pentru diferiți acceleratori hardware precum GPU-uri NVIDIA, GPU-uri AMD și altele2.
- **Ușurință în utilizare:** Oferă API-uri pentru integrare facilă în aplicații, permițând generarea de texte, imagini și alte conținuturi cu cod minim.
- Utilizatorii pot apela o metodă de nivel înalt generate(), sau pot rula fiecare iterație a modelului într-un ciclu, generând un token pe rând și opțional actualizând parametrii generației în timpul ciclului.
- ONNX runtime suportă, de asemenea, căutare greedy/beam și sampling TopP, TopK pentru generarea secvențelor de tokeni și procesare internă a logits-urilor precum penalizări pentru repetiții. De asemenea, poți adăuga cu ușurință scorare personalizată.

## Începutul lucrului
Pentru a începe cu ONNX Runtime pentru GENAI, poți urma acești pași:

### Instalează ONNX Runtime:
```Python
pip install onnxruntime
```
### Instalează extensiile Generative AI:
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

Pe lângă metodele de referință ONNX Runtime, Ollama și Foundry Local, putem completa referința modelelor cantitative pe baza metodelor de referință ale producătorilor diferiți. Cum ar fi framework-ul Apple MLX cu Apple Metal, Qualcomm QNN cu NPU, Intel OpenVINO cu CPU/GPU etc. Poți obține mai mult conținut din [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Mai mult

Am învățat bazele familiei Phi-3/3.5, dar pentru a afla mai multe despre SLM avem nevoie de cunoștințe suplimentare. Poți găsi răspunsurile în Phi-3 Cookbook. Dacă dorești să afli mai multe, te rugăm să vizitezi [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->