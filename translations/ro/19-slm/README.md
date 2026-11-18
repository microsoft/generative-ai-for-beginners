# Introducere în Modelele de Limbaj Mici pentru AI Generativ pentru Începători
AI generativ este un domeniu fascinant al inteligenței artificiale care se concentrează pe crearea de sisteme capabile să genereze conținut nou. Acest conținut poate varia de la text și imagini la muzică și chiar medii virtuale întregi. Una dintre cele mai interesante aplicații ale AI generativ este în domeniul modelelor de limbaj.

## Ce sunt Modelele de Limbaj Mici?

Un Model de Limbaj Mic (SLM) reprezintă o variantă redusă a unui model de limbaj mare (LLM), valorificând multe dintre principiile arhitecturale și tehnicile LLM-urilor, dar având o amprentă computațională semnificativ redusă.

SLM-urile sunt un subset de modele de limbaj concepute pentru a genera text asemănător celui uman. Spre deosebire de omologii lor mai mari, cum ar fi GPT-4, SLM-urile sunt mai compacte și eficiente, ceea ce le face ideale pentru aplicații unde resursele computaționale sunt limitate. În ciuda dimensiunii mai mici, ele pot efectua o varietate de sarcini. De obicei, SLM-urile sunt construite prin comprimarea sau distilarea LLM-urilor, cu scopul de a păstra o parte substanțială din funcționalitatea și capacitățile lingvistice originale ale modelului. Această reducere a dimensiunii modelului scade complexitatea generală, făcând SLM-urile mai eficiente atât în termeni de utilizare a memoriei, cât și de cerințe computaționale. În ciuda acestor optimizări, SLM-urile pot îndeplini încă o gamă largă de sarcini de procesare a limbajului natural (NLP):

- Generare de text: Crearea de propoziții sau paragrafe coerente și contextuale.
- Completare de text: Previziunea și completarea propozițiilor bazate pe un prompt dat.
- Traducere: Conversia textului dintr-o limbă în alta.
- Rezumare: Condensarea textelor lungi în rezumate mai scurte și mai digerabile.

Deși există unele compromisuri în performanță sau profunzimea înțelegerii comparativ cu omologii lor mai mari.

## Cum Funcționează Modelele de Limbaj Mici?
SLM-urile sunt antrenate pe cantități vaste de date text. În timpul antrenamentului, ele învață tiparele și structurile limbajului, permițându-le să genereze text care este atât gramatical corect, cât și contextualmente adecvat. Procesul de antrenament implică:

- Colectarea datelor: Adunarea unor seturi mari de date text din surse diverse.
- Preprocesare: Curățarea și organizarea datelor pentru a le face potrivite pentru antrenament.
- Antrenament: Utilizarea algoritmilor de învățare automată pentru a învăța modelul să înțeleagă și să genereze text.
- Ajustare fină: Reglarea modelului pentru a-i îmbunătăți performanța pe sarcini specifice.

Dezvoltarea SLM-urilor se aliniază cu necesitatea crescândă de modele care pot fi implementate în medii cu resurse limitate, cum ar fi dispozitive mobile sau platforme edge computing, unde LLM-urile pe scară largă pot fi nepractice din cauza cerințelor lor mari de resurse. Prin concentrarea pe eficiență, SLM-urile echilibrează performanța cu accesibilitatea, permițând o aplicare mai largă în diverse domenii.

![slm](../../../translated_images/ro/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Obiective de Învățare

În această lecție, sperăm să introducem cunoștințele despre SLM și să le combinăm cu Microsoft Phi-3 pentru a învăța diferite scenarii în conținut text, viziune și MoE.

La finalul acestei lecții, ar trebui să puteți răspunde la următoarele întrebări:

- Ce este SLM?
- Care este diferența dintre SLM și LLM?
- Ce este Familia Microsoft Phi-3/3.5?
- Cum se realizează inferența cu Familia Microsoft Phi-3/3.5?

Sunteți gata? Să începem.

## Diferențele dintre Modelele de Limbaj Mari (LLM) și Modelele de Limbaj Mici (SLM)

Atât LLM-urile, cât și SLM-urile se bazează pe principii fundamentale ale învățării automate probabilistice, urmând abordări similare în designul arhitectural, metodologiile de antrenament, procesele de generare a datelor și tehnicile de evaluare a modelului. Cu toate acestea, câțiva factori cheie diferențiază aceste două tipuri de modele.

## Aplicații ale Modelelor de Limbaj Mici

SLM-urile au o gamă largă de aplicații, inclusiv:

- Chatbot-uri: Oferirea de suport clienților și interacțiunea cu utilizatorii într-un mod conversațional.
- Crearea de conținut: Asistarea scriitorilor prin generarea de idei sau chiar redactarea unor articole întregi.
- Educație: Ajutor pentru studenți la realizarea temelor sau învățarea de limbi noi.
- Accesibilitate: Crearea de instrumente pentru persoanele cu dizabilități, cum ar fi sistemele text-vorbire.

**Dimensiune**
  
O diferență principală dintre LLM-uri și SLM-uri constă în scala modelelor. LLM-urile, cum ar fi ChatGPT (GPT-4), pot conține aproximativ 1,76 trilioane de parametri, în timp ce SLM-urile open-source precum Mistral 7B sunt proiectate cu mult mai puțini parametri — aproximativ 7 miliarde. Această disparitate se datorează în principal diferențelor în arhitectura modelului și procesele de antrenament. De exemplu, ChatGPT utilizează un mecanism de auto-atenție într-un cadru encoder-decoder, pe când Mistral 7B folosește atenție prin fereastră glisantă, care permite un antrenament mai eficient într-un model decoder-only. Această diferență arhitecturală are implicații profunde asupra complexității și performanței acestor modele.

**Înțelegere**

SLM-urile sunt optimizate de obicei pentru performanță în anumite domenii specifice, devenind astfel foarte specializate, dar potențial limitate în capacitatea lor de a oferi o înțelegere contextuală largă pe multiple domenii ale cunoașterii. În schimb, LLM-urile urmăresc să simuleze inteligența asemănătoare celei umane la un nivel mai cuprinzător. Antrenate pe seturi enorme și diverse de date, LLM-urile sunt concepute să funcționeze bine într-o varietate de domenii, oferind o versatilitate și adaptabilitate superioară. Ca urmare, LLM-urile sunt mai potrivite pentru o gamă mai largă de sarcini, cum ar fi procesarea limbajului natural și programarea.

**Calcul**

Antrenamentul și implementarea LLM-urilor sunt procese intensive din punct de vedere al resurselor, care deseori necesită infrastructură computațională semnificativă, inclusiv clustere GPU la scară largă. De exemplu, antrenarea unui model precum ChatGPT de la zero poate necesita mii de GPU-uri pe perioade extinse. În contrast, SLM-urile, cu număr mai mic de parametri, sunt mai accesibile în termeni de resurse computaționale. Modele precum Mistral 7B pot fi antrenate și rulate pe mașini locale echipate cu GPU-uri moderate, deși antrenamentul încă necesită câteva ore pe mai multe GPU-uri.

**Bias**

Bias-ul este o problemă cunoscută în LLM-uri, în principal din cauza naturii datelor de antrenament. Aceste modele se bazează adesea pe date brute, disponibile deschis pe internet, care pot subreprezenta sau reprezenta greșit anumite grupuri, pot introduce etichetări eronate sau reflectă prejudecăți lingvistice influențate de dialecte, variații geografice și reguli gramaticale. În plus, complexitatea arhitecturii LLM poate agrava involuntar bias-ul, care poate trece neobservat fără o ajustare atentă. Pe de altă parte, SLM-urile, fiind antrenate pe seturi de date mai restrânse, specifice domeniului, sunt inerent mai puțin susceptibile la astfel de bias-uri, deși nu sunt imunizate complet.

**Inferență**

Dimensiunea redusă a SLM-urilor le conferă un avantaj semnificativ în ceea ce privește viteza inferenței, permițându-le să genereze rezultate eficient pe hardware local, fără necesitatea unui proces paralel extins. În contrast, LLM-urile, datorită dimensiunii și complexității lor, necesită adesea resurse computaționale paralele considerabile pentru a obține timpi acceptabili de inferență. Prezența mai multor utilizatori concurenți încetinește și mai mult timpii de răspuns ai LLM-urilor, în special când sunt implementate la scară mare.

În rezumat, deși atât LLM-urile cât și SLM-urile au o bază fundamentală comună în învățarea automată, ele diferă semnificativ în termeni de dimensiune a modelului, cerințe de resurse, înțelegere contextuală, susceptibilitate la bias și viteza inferenței. Aceste diferențe reflectă potrivirea lor pentru diferite cazuri de utilizare, LLM-urile fiind mai versatile dar consumatoare de resurse, iar SLM-urile oferind eficiență specifică domeniului cu cerințe computaționale reduse.

***Notă: În această lecție, vom introduce SLM folosind Microsoft Phi-3 / 3.5 ca exemplu.***

## Introducerea Familiei Phi-3 / Phi-3.5

Familia Phi-3 / 3.5 vizează în principal scenarii de aplicare în text, viziune și Agent (MoE):

### Phi-3 / 3.5 Instruct

În principal pentru generarea de text, completarea conversațiilor și extragerea de informații din conținut, etc.

**Phi-3-mini**

Modelul de limbaj de 3,8B este disponibil pe Microsoft Foundry, Hugging Face și Ollama. Modelele Phi-3 depășesc semnificativ modelele de limbaj de dimensiuni egale și mai mari pe benchmark-uri cheie (vedeți numerele benchmark mai jos, numerele mai mari sunt mai bune). Phi-3-mini depășește modelele de două ori mai mari, în timp ce Phi-3-small și Phi-3-medium depășesc modele mai mari, inclusiv GPT-3.5.

**Phi-3-small & medium**

Cu doar 7B parametri, Phi-3-small îl învinge pe GPT-3.5T pe o varietate de benchmark-uri în limbaj, raționament, programare și matematică.

Phi-3-medium cu 14B parametri continuă această tendință și depășește Gemini 1.0 Pro.

**Phi-3.5-mini**

Ne putem gândi la el ca o actualizare a lui Phi-3-mini. Deși numărul parametrilor rămâne neschimbat, îmbunătățește capacitatea de a susține mai multe limbi (susține peste 20 de limbi: arabă, chineză, cehă, daneză, olandeză, engleză, finlandeză, franceză, germană, ebraică, maghiară, italiană, japoneză, coreeană, norvegiană, poloneză, portugheză, rusă, spaniolă, suedeză, thailandeză, turcă, ucraineană) și adaugă suport mai puternic pentru context lung.

Phi-3.5-mini cu 3,8B parametri depășește modelele de limbaj de aceeași dimensiune și se situează la egalitate cu modelele de două ori mai mari.

### Phi-3 / 3.5 Vision

Ne putem gândi la modelul Instruct al Phi-3/3.5 ca la abilitatea Phi de a înțelege, iar Vision este ceea ce dă lui Phi ochi pentru a înțelege lumea.


**Phi-3-Vision**

Phi-3-vision, cu doar 4,2B parametri, continuă această tendință și depășește modele mai mari precum Claude-3 Haiku și Gemini 1.0 Pro V pe sarcini generale de raționament vizual, OCR și înțelegerea tabelelor și diagramelor.


**Phi-3.5-Vision**

Phi-3.5-Vision este, de asemenea, o actualizare a lui Phi-3-Vision, adăugând suport pentru imagini multiple. Poți să-l consideri o îmbunătățire în vision, nu doar poți vedea poze, dar și videoclipuri.

Phi-3.5-vision depășește modele mai mari precum Claude-3.5 Sonnet și Gemini 1.5 Flash în sarcini OCR, înțelegerea tabelelor și graficelor și este la egalitate în sarcinile generale de raționament vizual. Suportă input multi-frame, adică realizează raționamente pe mai multe imagini de intrare.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** permite modelelor să fie preantrenate cu mult mai puțin calcul, ceea ce înseamnă că poți scala dramatic dimensiunea modelului sau a setului de date cu același buget computațional ca un model dens. În special, un model MoE ar trebui să atingă aceeași calitate ca omologul său dens mult mai rapid în timpul preantrenamentului.

Phi-3.5-MoE cuprinde 16 module de experți de 3,8B. Phi-3.5-MoE cu doar 6,6B parametri activi atinge un nivel similar de raționament, înțelegere a limbajului și matematică ca modele mult mai mari.

Putem folosi modelul din Familia Phi-3/3.5 bazat pe diferite scenarii. Spre deosebire de LLM, poți implementa Phi-3/3.5-mini sau Phi-3/3.5-Vision pe dispozitive edge.


## Cum se folosesc modelele din Familia Phi-3/3.5

Sperăm să folosim Phi-3/3.5 în diferite scenarii. În continuare, vom folosi Phi-3/3.5 bazat pe scenarii diferite.

![phi3](../../../translated_images/ro/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inferență prin API-uri Cloud

**Microsoft Foundry Models**

> **Notă:** GitHub Models se va închide la sfârșitul lunii iulie 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) este înlocuitorul direct.

> **Notă:** Întreaga familie Phi-3/3.5 (variantele Instruct, Vision și MoE) a fost retrasă din catalogul Microsoft Foundry Models pe 2025-08-30. Folosiți `Phi-4` (Instruct) sau `Phi-4-mini-instruct` în schimb — exemplele Phi-3/3.5 de mai jos funcționează încă prin Hugging Face, Ollama, ONNX Runtime și NVIDIA NIM.

Microsoft Foundry Models oferă acum succesorii Phi-4. Folosiți `Phi-4` sau `Phi-4-mini-instruct` în locul modelelor Phi-3/3.5 retrase când urmați exemplele API-urilor cloud.

- Demo: Compararea efectelor lui Phi-3-mini și Phi-3.5-mini în scenarii chinezești

![phi3](../../../translated_images/ro/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/ro/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Dacă doriți să folosiți modele de viziune (multimodale) în cloud, folosiți `Phi-4-multimodal-instruct` disponibil în prezent prin Microsoft Foundry în locul modelelor Phi-3/3.5 Vision retrase; pentru sarcini text folosiți `Phi-4` sau `Phi-4-mini-instruct`. Modelul Phi-3.5 MoE a fost retras din Microsoft Foundry, deci folosiți celelalte opțiuni descrise în această lecție (de exemplu Hugging Face) dacă doriți să experimentați cu el. Dacă sunteți interesați, puteți citi Phi Cookbook pentru a afla cum să apelați modelele Phi prin Microsoft Foundry [Click pe acest link](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Pe lângă catalogul cloud Microsoft Foundry Models, puteți folosi și [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) pentru a completa apelurile aferente. Puteți vizita NVIDIA NIM pentru a realiza apelurile API ale Familiei Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) este un set de microservicii de inferență accelerate, concepute pentru a ajuta dezvoltatorii să implementeze modele AI eficient în diverse medii, inclusiv cloud-uri, centre de date și stații de lucru.

Iată câteva caracteristici cheie ale NVIDIA NIM:

- **Ușurința implementării:** NIM permite implementarea modelelor AI cu o singură comandă, făcând integrarea în fluxurile de lucru existente foarte simplă.
- **Performanță optimizată:** Folosește motoarele de inferență pre-optimizate ale NVIDIA, precum TensorRT și TensorRT-LLM, pentru a asigura o latență scăzută și un debit ridicat.
- **Scalabilitate:** NIM suportă autoscalarea pe Kubernetes, permițând gestionarea eficientă a volumelor de lucru variabile.
- **Securitate și control:** Organizațiile pot menține controlul asupra datelor și aplicațiilor lor prin găzduirea internă a microserviciilor NIM pe infrastructura lor administrată.
- **API-uri standard:** NIM oferă API-uri standard din industrie, ușurând construirea și integrarea aplicațiilor AI precum chatbot-uri, asistenți AI și altele.

NIM face parte din NVIDIA AI Enterprise, care are ca scop simplificarea implementării și operaționalizării modelelor AI, asigurând rularea eficientă pe GPU-urile NVIDIA.

- Demo: Utilizarea NVIDIA NIM pentru a apela Phi-3.5-Vision-API  [[Click this link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Rularea locală Phi-3/3.5
Inferența în legătură cu Phi-3 sau orice model de limbaj precum GPT-3 se referă la procesul de generare a răspunsurilor sau predicțiilor pe baza datelor de intrare primite. Când oferiți un prompt sau o întrebare lui Phi-3, acesta folosește rețeaua sa neuronală antrenată pentru a deduce cel mai probabil și relevant răspuns analizând tiparele și relațiile din datele pe care a fost antrenat.

**Hugging Face Transformer**
Hugging Face Transformers este o bibliotecă puternică concepută pentru procesarea limbajului natural (NLP) și alte sarcini de învățare automată. Iată câteva puncte cheie despre aceasta:

1. **Modele preantrenate**: Oferă mii de modele preantrenate care pot fi folosite pentru diverse sarcini, cum ar fi clasificarea textului, recunoașterea entităților numite, răspuns la întrebări, sumarizare, traducere și generare de text.

2. **Interoperabilitate între framework-uri**: Biblioteca suportă multiple framework-uri de învățare profundă, inclusiv PyTorch, TensorFlow și JAX. Aceasta permite antrenarea modelului într-un framework și utilizarea în altul.

3. **Capabilități multimodale**: În afară de NLP, Hugging Face Transformers suportă și sarcini în viziune computerizată (de exemplu, clasificare imagini, detectare obiecte) și procesare audio (de exemplu, recunoaștere vocală, clasificare audio).

4. **Ușurința utilizării**: Biblioteca oferă API-uri și unelte pentru descărcarea și ajustarea ușoară a modelelor, fiind accesibilă atât pentru începători, cât și pentru experți.

5. **Comunitate și resurse**: Hugging Face dispune de o comunitate activă și o documentație vastă, tutoriale și ghiduri pentru a ajuta utilizatorii să înceapă și să profite la maximum de bibliotecă.
[documentație oficială](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) sau depozitul lor [GitHub](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Aceasta este metoda cea mai des folosită, însă necesită accelerare GPU. Până la urmă, scenariile precum Vision și MoE necesită multe calcule, care vor fi foarte lente pe CPU dacă nu sunt cuantificate.


- Demo: Utilizarea Transformer pentru a apela Phi-3.5-Instruct [Click this link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Utilizarea Transformer pentru a apela Phi-3.5-Vision [Click this link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Utilizarea Transformer pentru a apela Phi-3.5-MoE [Click this link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) este o platformă concepută să faciliteze rularea locală a modelelor mari de limbaj (LLMs) pe mașina ta. Suportă diverse modele precum Llama 3.1, Phi 3, Mistral și Gemma 2, printre altele. Platforma simplifică procesul prin împachetarea greutăților modelului, configurației și datelor într-un singur pachet, făcându-l mai accesibil pentru utilizatori să-și personalizeze și să-și creeze propriile modele. Ollama este disponibil pentru macOS, Linux și Windows. Este un instrument excelent dacă doriți să experimentați sau să implementați LLM-uri fără a depinde de servicii cloud. Ollama este cea mai directă metodă, trebuie doar să executați comanda următoare.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) este mediul runtime offline, pe dispozitiv, al Microsoft, pentru rularea modelelor precum Phi complet pe hardware-ul propriu - nu este necesar abonament Azure, cheie API sau conexiune la rețea. Acesta selectează automat cel mai bun furnizor de execuție disponibil (NPU, GPU sau CPU) și expune un endpoint compatibil OpenAI, astfel încât codul existent `openai`/Azure AI Inference SDK să poată folosi cu modificări minime. Consultați [documentația Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) pentru a începe.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) este un accelerator cross-platform pentru inferență și antrenare în machine learning. ONNX Runtime pentru Generative AI (GENAI) este un instrument puternic care te ajută să rulezi eficient modele AI generative pe diverse platforme.

## Ce este ONNX Runtime?
ONNX Runtime este un proiect open-source ce permite inferență de înaltă performanță pentru modelele de machine learning. Suportă modele în formatul Open Neural Network Exchange (ONNX), un standard pentru reprezentarea modelelor de machine learning. Inferența cu ONNX Runtime poate permite experiențe pentru clienți mai rapide și costuri mai mici, susținând modele din framework-uri de deep learning precum PyTorch și TensorFlow/Keras, precum și biblioteci clasice de machine learning precum scikit-learn, LightGBM, XGBoost, etc. ONNX Runtime este compatibil cu diferite hardware-uri, drivere și sisteme de operare, și oferă performanță optimă prin utilizarea acceleratorilor hardware acolo unde este cazul, împreună cu optimizări și transformări ale grafului.

## Ce este Generative AI?
Generative AI se referă la sistemele AI care pot genera conținut nou, precum text, imagini sau muzică, bazându-se pe datele pe care au fost antrenate. Exemple includ modele de limbaj precum GPT-3 și modele de generare de imagini precum Stable Diffusion. Biblioteca ONNX Runtime pentru GenAI oferă bucla generativă AI pentru modelele ONNX, inclusiv inferența cu ONNX Runtime, procesarea logits-urilor, căutarea și eșantionarea, și managementul cache-ului KV.

## ONNX Runtime pentru GENAI
ONNX Runtime pentru GENAI extinde capacitățile ONNX Runtime pentru a suporta modele AI generative. Iată câteva caracteristici cheie:

- **Suport larg pentru platforme:** Funcționează pe diverse platforme, incluzând Windows, Linux, macOS, Android și iOS.
- **Suport pentru modele:** Susține multe modele populare generative AI, precum LLaMA, GPT-Neo, BLOOM și altele.
- **Optimizare a performanței:** Include optimizări pentru diferiți acceleratori hardware, cum ar fi GPU-urile NVIDIA, GPU-urile AMD și altele2.
- **Ușurință în utilizare:** Oferă API-uri pentru integrare ușoară în aplicații, permițând generarea de text, imagini și alt conținut cu cod minim.
- Utilizatorii pot apela metoda generate() la un nivel înalt sau pot rula fiecare iterare a modelului într-un loop, generând un token pe rând și eventual actualizând parametrii de generare în interiorul loop-ului.
- ONNX runtime oferă și suport pentru căutare greedy/beam și eșantionare TopP, TopK pentru generarea secvențelor de tokeni și procesare built-in a logits-urilor ca penalizări pentru repetiții. Se pot adăuga ușor și scorări personalizate.

## Începem
Pentru a începe cu ONNX Runtime pentru GENAI, urmează acești pași:

### Instalează ONNX Runtime:
```Python
pip install onnxruntime
```
### Instalează Generative AI Extensions:
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

Pe lângă metodele de referință ONNX Runtime, Ollama și Foundry Local, putem completa și referința modelelor cantitative bazate pe metodele de referință ale modelelor furnizate de diverși producători. Cum ar fi cadrul Apple MLX cu Apple Metal, Qualcomm QNN cu NPU, Intel OpenVINO cu CPU/GPU, etc. De asemenea, puteți obține mai mult conținut din [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Mai mult

Am învățat elementele de bază ale familiei Phi-3/3.5, dar pentru a afla mai multe despre SLM avem nevoie de mai multă cunoaștere. Puteți găsi răspunsurile în Phi-3 Cookbook. Dacă doriți să aflați mai multe, vă rugăm să vizitați [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->