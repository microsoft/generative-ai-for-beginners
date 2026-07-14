# Introduzione ai Modelli Linguistici Piccoli per l'IA Generativa per Principianti
L'IA generativa è un campo affascinante dell'intelligenza artificiale che si concentra sulla creazione di sistemi capaci di generare nuovi contenuti. Questi contenuti possono spaziare da testi e immagini a musica e persino interi ambienti virtuali. Una delle applicazioni più entusiasmanti dell'IA generativa è nel campo dei modelli linguistici.

## Cosa Sono i Modelli Linguistici Piccoli?

Un Modello Linguistico Piccolo (SLM) rappresenta una variante ridotta di un grande modello linguistico (LLM), sfruttando molti dei principi architetturali e delle tecniche degli LLM, pur mostrando un'impronta computazionale significativamente ridotta.

Gli SLM sono un sottoinsieme di modelli linguistici progettati per generare testo simile a quello umano. A differenza dei loro omologhi più grandi, come GPT-4, gli SLM sono più compatti ed efficienti, rendendoli ideali per applicazioni dove le risorse computazionali sono limitate. Nonostante le dimensioni ridotte, possono comunque svolgere una varietà di compiti. Tipicamente, gli SLM sono costruiti comprimendo o distillando gli LLM, con l'obiettivo di conservare una porzione sostanziale delle funzionalità e delle capacità linguistiche del modello originale. Questa riduzione delle dimensioni del modello diminuisce la complessità complessiva, rendendo gli SLM più efficienti in termini di utilizzo della memoria e requisiti computazionali. Nonostante queste ottimizzazioni, gli SLM possono ancora eseguire un'ampia gamma di compiti di elaborazione del linguaggio naturale (NLP):

- Generazione di Testo: Creare frasi o paragrafi coerenti e contestualmente rilevanti.
- Completamento del Testo: Predire e completare frasi basate su un prompt dato.
- Traduzione: Convertire il testo da una lingua all'altra.
- Sintesi: Condensare testi lunghi in riassunti più brevi e digeribili.

Sebbene con qualche compromesso in termini di prestazioni o profondità di comprensione rispetto ai loro omologhi più grandi.

## Come Funzionano i Modelli Linguistici Piccoli?
Gli SLM sono addestrati su grandi quantità di dati testuali. Durante l'addestramento, apprendono i modelli e le strutture del linguaggio, permettendo loro di generare testo grammaticalmente corretto e contestualmente appropriato. Il processo di addestramento prevede:

- Raccolta Dati: Raccogliere grandi set di dati testuali da varie fonti.
- Pre-elaborazione: Pulire e organizzare i dati per renderli adatti all'addestramento.
- Addestramento: Utilizzare algoritmi di machine learning per insegnare al modello come comprendere e generare testo.
- Fine-Tuning: Regolare il modello per migliorare le sue prestazioni in compiti specifici.

Lo sviluppo degli SLM è in linea con la crescente necessità di modelli che possano essere distribuiti in ambienti con risorse limitate, come dispositivi mobili o piattaforme di edge computing, dove gli LLM a piena scala possono essere impraticabili a causa delle loro elevate richieste di risorse. Focalizzandosi sull'efficienza, gli SLM bilanciano prestazioni e accessibilità, consentendo un'applicazione più ampia in vari domini.

![slm](../../../translated_images/it/slm.4058842744d0444a.webp)

## Obiettivi di Apprendimento

In questa lezione, speriamo di introdurre la conoscenza degli SLM e combinarla con Microsoft Phi-3 per apprendere diversi scenari in contenuti testuali, visione e MoE.

Alla fine di questa lezione, dovresti essere in grado di rispondere alle seguenti domande:

- Cos'è un SLM?
- Qual è la differenza tra SLM e LLM?
- Cos'è la famiglia Microsoft Phi-3/3.5?
- Come eseguire inferenza con la famiglia Microsoft Phi-3/3.5?

Pronti? Iniziamo.

## Le Differenze tra Grandi Modelli Linguistici (LLM) e Piccoli Modelli Linguistici (SLM)

Sia gli LLM che gli SLM sono costruiti su principi fondamentali di apprendimento automatico probabilistico, seguendo approcci simili nella progettazione architetturale, nelle metodologie di addestramento, nei processi di generazione dei dati e nelle tecniche di valutazione del modello. Tuttavia, diversi fattori chiave differenziano questi due tipi di modelli.

## Applicazioni dei Modelli Linguistici Piccoli

Gli SLM hanno un'ampia gamma di applicazioni, tra cui:

- Chatbot: Fornire supporto clienti e interagire con gli utenti in modo conversazionale.
- Creazione di Contenuti: Assistere gli scrittori generando idee o persino redigendo interi articoli.
- Educazione: Aiutare gli studenti con compiti di scrittura o nell'apprendimento di nuove lingue.
- Accessibilità: Creare strumenti per persone con disabilità, come sistemi di sintesi vocale.

**Dimensioni**
  
Una distinzione principale tra LLM e SLM risiede nella scala dei modelli. Gli LLM, come ChatGPT (GPT-4), possono comprendere un numero stimato di 1.76 trilioni di parametri, mentre gli SLM open source come Mistral 7B sono progettati con un numero significativamente inferiore di parametri—circa 7 miliardi. Questa disparità è principalmente dovuta alle differenze nell'architettura del modello e nei processi di addestramento. Per esempio, ChatGPT impiega un meccanismo di self-attention all'interno di una struttura encoder-decoder, mentre Mistral 7B utilizza l'attenzione a finestra scorrevole, che consente un addestramento più efficiente all'interno di un modello solo decoder. Questa variazione architetturale ha profonde implicazioni per la complessità e le prestazioni di questi modelli.

**Comprensione**

Gli SLM sono tipicamente ottimizzati per le prestazioni in domini specifici, rendendoli altamente specializzati ma potenzialmente limitati nella loro capacità di fornire una comprensione contestuale ampia su più campi di conoscenza. Al contrario, gli LLM mirano a simulare un'intelligenza simile a quella umana su un livello più comprensivo. Addestrati su vasti e diversificati dataset, gli LLM sono progettati per ottenere buoni risultati in una varietà di domini, offrendo maggiore versatilità e adattabilità. Di conseguenza, gli LLM sono più adatti a una gamma più ampia di compiti a valle, come l'elaborazione del linguaggio naturale e la programmazione.

**Calcolo**

L'addestramento e la distribuzione degli LLM sono processi intensi in termini di risorse, spesso necessitando di infrastrutture computazionali significative, inclusi cluster GPU su larga scala. Per esempio, addestrare un modello come ChatGPT da zero può richiedere migliaia di GPU per periodi prolungati. Al contrario, gli SLM, con il loro numero inferiore di parametri, sono più accessibili in termini di risorse computazionali. Modelli come Mistral 7B possono essere addestrati ed eseguiti su macchine locali dotate di capacità GPU moderate, anche se l'addestramento richiede comunque diverse ore su più GPU.

**Bias**

Il bias è un problema noto negli LLM, principalmente a causa della natura dei dati di addestramento. Questi modelli spesso si basano su dati grezzi, aperti e disponibili su internet, che possono sottorappresentare o rappresentare erroneamente determinati gruppi, introdurre etichettature errate o riflettere bias linguistici influenzati da dialetti, variazioni geografiche e regole grammaticali. Inoltre, la complessità delle architetture LLM può inadvertitamente aggravare il bias, che può passare inosservato senza un accurato fine-tuning. D'altra parte, gli SLM, essendo addestrati su dataset più limitati e specifici per dominio, sono intrinsecamente meno suscettibili a tali bias, anche se non ne sono immuni.

**Inferenza**

Le dimensioni ridotte degli SLM conferiscono loro un vantaggio significativo in termini di velocità di inferenza, permettendo di generare output in modo efficiente su hardware locale senza la necessità di un'elaborazione parallela estesa. Di contro, gli LLM, a causa delle loro dimensioni e complessità, spesso richiedono sostanziose risorse computazionali parallele per ottenere tempi di inferenza accettabili. La presenza di più utenti simultanei rallenta ulteriormente i tempi di risposta degli LLM, specialmente quando distribuiti su larga scala.

In sintesi, mentre sia gli LLM che gli SLM condividono una base fondamentale nel machine learning, differiscono significativamente in termini di dimensione del modello, requisiti di risorse, comprensione contestuale, suscettibilità al bias e velocità di inferenza. Queste distinzioni riflettono la rispettiva idoneità per casi d'uso differenti, con gli LLM più versatili ma esigenti in risorse, e gli SLM che offrono una maggiore efficienza specifica per dominio con richieste computazionali ridotte.

***Nota: in questa lezione introdurremo gli SLM utilizzando come esempio Microsoft Phi-3 / 3.5.***

## Introduzione alla Famiglia Phi-3 / Phi-3.5

La famiglia Phi-3 / 3.5 si rivolge principalmente a scenari applicativi di testo, visione e agente (MoE):

### Phi-3 / 3.5 Instruct

Principalmente per generazione di testo, completamento chat, estrazione di informazioni dai contenuti, ecc.

**Phi-3-mini**

Il modello linguistico da 3.8B è disponibile su Microsoft Foundry, Hugging Face e Ollama. I modelli Phi-3 superano significativamente i modelli linguistici di pari e maggiori dimensioni sui principali benchmark (vedi numeri benchmark sotto, numeri più alti sono migliori). Phi-3-mini supera modelli con il doppio dei parametri, mentre Phi-3-small e Phi-3-medium superano modelli più grandi, inclusi GPT-3.5.

**Phi-3-small e medium**

Con solo 7 miliardi di parametri, Phi-3-small batte GPT-3.5T in una varietà di benchmark linguistici, di ragionamento, coding e matematica.

Phi-3-medium con 14 miliardi di parametri continua questa tendenza e supera Gemini 1.0 Pro.

**Phi-3.5-mini**

Possiamo considerarlo un aggiornamento di Phi-3-mini. Sebbene i parametri rimangano invariati, migliora la capacità di supportare lingue multiple (supporta oltre 20 lingue: arabo, cinese, ceco, danese, olandese, inglese, finlandese, francese, tedesco, ebraico, ungherese, italiano, giapponese, coreano, norvegese, polacco, portoghese, russo, spagnolo, svedese, tailandese, turco, ucraino) e aggiunge un supporto più forte per contesti lunghi.

Phi-3.5-mini con 3.8B parametri supera modelli linguistici della stessa dimensione ed è pari a modelli con il doppio dei parametri.

### Phi-3 / 3.5 Vision

Possiamo considerare il modello Instruct di Phi-3/3.5 come la capacità di Phi di comprendere, mentre Vision è ciò che conferisce a Phi gli occhi per comprendere il mondo.


**Phi-3-Vision**

Phi-3-vision, con solo 4.2B parametri, continua questa tendenza e supera modelli più grandi come Claude-3 Haiku e Gemini 1.0 Pro V in compiti di ragionamento visivo generale, OCR e comprensione di tabelle e diagrammi.


**Phi-3.5-Vision**

Phi-3.5-Vision è anche un aggiornamento di Phi-3-Vision, aggiungendo supporto per immagini multiple. Puoi considerarlo un miglioramento nella visione, non solo puoi vedere immagini, ma anche video.

Phi-3.5-vision supera modelli più grandi come Claude-3.5 Sonnet e Gemini 1.5 Flash in compiti OCR, comprensione di tabelle e grafici ed è pari in compiti di ragionamento sulla conoscenza visiva generale. Supporta input multi-frame, cioè esegue ragionamenti su più immagini input.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** permette ai modelli di essere pre-addestrati con un calcolo molto più ridotto, il che significa che puoi aumentare drasticamente la dimensione del modello o del dataset con lo stesso budget computazionale di un modello denso. In particolare, un modello MoE dovrebbe raggiungere la stessa qualità del suo equivalente denso molto più rapidamente durante il preaddestramento.

Phi-3.5-MoE è composto da 16 moduli esperti da 3.8B ciascuno. Phi-3.5-MoE con solo 6.6B parametri attivi raggiunge un livello simile di ragionamento, comprensione del linguaggio e matematica rispetto a modelli molto più grandi.

Possiamo usare il modello della famiglia Phi-3/3.5 basandoci su diversi scenari. A differenza degli LLM, puoi distribuire Phi-3/3.5-mini o Phi-3/3.5-Vision su dispositivi edge.


## Come usare i modelli della famiglia Phi-3/3.5

Speriamo di usare Phi-3/3.5 in diversi scenari. Di seguito, utilizzeremo Phi-3/3.5 basandoci su diversi scenari.

![phi3](../../../translated_images/it/phi3.655208c3186ae381.webp)

### Inferenza tramite API Cloud

**Modelli Microsoft Foundry**

> **Nota:** GitHub Models sarà ritirato a fine luglio 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) è la sostituzione diretta.

Microsoft Foundry Models è il modo più diretto. Puoi accedere rapidamente al modello Phi-3/3.5-Instruct tramite il catalogo modelli Foundry. In combinazione con Azure AI Inference SDK / OpenAI SDK, puoi accedere all'API tramite codice per completare la chiamata Phi-3/3.5-Instruct. Puoi anche testare diversi effetti tramite il Playground.

- Demo: confronto degli effetti di Phi-3-mini e Phi-3.5-mini in scenari in cinese

![phi3](../../../translated_images/it/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/it/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Oppure, se vogliamo usare i modelli vision e MoE, possiamo utilizzare Microsoft Foundry per completare la chiamata. Se sei interessato, puoi leggere il Phi-3 Cookbook per imparare come chiamare Phi-3/3.5 Instruct, Vision, MoE tramite Microsoft Foundry [Clicca questo link](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Oltre al catalogo dei modelli Microsoft Foundry basato su cloud, puoi anche utilizzare [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) per completare le chiamate correlate. Puoi visitare NVIDIA NIM per completare le chiamate API della famiglia Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) è un insieme di microservizi di inferenza accelerati progettati per aiutare gli sviluppatori a distribuire modelli AI in modo efficiente in vari ambienti, inclusi cloud, data center e workstation.

Ecco alcune caratteristiche principali di NVIDIA NIM:

- **Facilità di Distribuzione:** NIM permette il deployment di modelli AI con un solo comando, rendendo semplice l'integrazione in flussi di lavoro esistenti.

- **Prestazioni Ottimizzate:** Sfrutta i motori di inferenza pre-ottimizzati di NVIDIA, come TensorRT e TensorRT-LLM, per garantire bassa latenza e elevata produttività.
- **Scalabilità:** NIM supporta l'autoscaling su Kubernetes, consentendo di gestire efficacemente carichi di lavoro variabili.
- **Sicurezza e Controllo:** Le organizzazioni possono mantenere il controllo sui propri dati e applicazioni ospitando autonomamente i microservizi NIM sulla propria infrastruttura gestita.
- **API Standard:** NIM fornisce API standard del settore, facilitando la creazione e l'integrazione di applicazioni AI come chatbot, assistenti AI e altro.

NIM fa parte di NVIDIA AI Enterprise, che mira a semplificare il deployment e l'operatività dei modelli AI, assicurando che funzionino in modo efficiente sulle GPU NVIDIA.

- Demo: Utilizzo di NVIDIA NIM per chiamare Phi-3.5-Vision-API  [[Clicca questo link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Esecuzione Locale di Phi-3/3.5
Inferenza in relazione a Phi-3, o a qualsiasi modello linguistico come GPT-3, si riferisce al processo di generazione di risposte o previsioni basate sugli input ricevuti. Quando fornisci un prompt o una domanda a Phi-3, utilizza la sua rete neurale addestrata per inferire la risposta più probabile e pertinente analizzando modelli e correlazioni nei dati su cui è stato addestrato.

**Hugging Face Transformer**
Hugging Face Transformers è una potente libreria progettata per il natural language processing (NLP) e altre attività di machine learning. Ecco alcuni punti chiave a riguardo:

1. **Modelli Preaddestrati**: Fornisce migliaia di modelli preaddestrati utilizzabili per varie attività come classificazione del testo, riconoscimento di entità nominate, question answering, sintesi, traduzione e generazione di testo.

2. **Interoperabilità con Framework**: La libreria supporta diversi framework di deep learning, tra cui PyTorch, TensorFlow e JAX. Ciò consente di addestrare un modello in un framework e usarlo in un altro.

3. **Capacità Multimodali**: Oltre all'NLP, Hugging Face Transformers supporta anche attività di computer vision (ad esempio classificazione delle immagini, rilevamento oggetti) e elaborazione audio (ad esempio riconoscimento vocale, classificazione audio).

4. **Facilità d'Uso**: La libreria offre API e strumenti per scaricare facilmente e affinare i modelli, rendendola accessibile sia ai principianti che agli esperti.

5. **Comunità e Risorse**: Hugging Face dispone di una comunità vivace e di una documentazione estesa, tutorial e guide per aiutare gli utenti a iniziare e sfruttare al massimo la libreria.
[documentazione ufficiale](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) o il loro [repository GitHub](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Questo è il metodo più comunemente utilizzato, ma richiede anche l'accelerazione GPU. Dopotutto, scenari come Vision e MoE richiedono molti calcoli, che sarebbero molto lenti su CPU se non quantizzati.


- Demo: Utilizzo di Transformer per chiamare Phi-3.5-Instruct [Clicca questo link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Utilizzo di Transformer per chiamare Phi-3.5-Vision [Clicca questo link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Utilizzo di Transformer per chiamare Phi-3.5-MoE [Clicca questo link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) è una piattaforma progettata per facilitare l'esecuzione di grandi modelli linguistici (LLM) localmente sul tuo computer. Supporta vari modelli come Llama 3.1, Phi 3, Mistral e Gemma 2, tra gli altri. La piattaforma semplifica il processo raggruppando pesi del modello, configurazioni e dati in un unico pacchetto, rendendo più accessibile per gli utenti la personalizzazione e la creazione dei propri modelli. Ollama è disponibile per macOS, Linux e Windows. È un ottimo strumento se vuoi sperimentare o distribuire LLM senza fare affidamento ai servizi cloud. Ollama è il modo più diretto, devi solo eseguire il seguente comando.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) è l'ambiente di esecuzione offline e su dispositivo di Microsoft per eseguire modelli come Phi interamente sul tuo hardware - non è necessario abbonamento Azure, chiave API o connessione di rete. Seleziona automaticamente il miglior provider di esecuzione disponibile (NPU, GPU o CPU) e espone un endpoint compatibile OpenAI, così il codice esistente `openai`/Azure AI Inference SDK può puntarvi con modifiche minime. Consulta la [documentazione di Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) per iniziare.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Oppure usa direttamente l'SDK in Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime per GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) è un acceleratore cross-platform per inferenza e training di machine learning. ONNX Runtime per Generative AI (GENAI) è uno strumento potente che ti aiuta a eseguire modelli di AI generativa in modo efficiente su diverse piattaforme.

## Cos'è ONNX Runtime?
ONNX Runtime è un progetto open source che permette inferenze ad alte prestazioni di modelli di machine learning. Supporta modelli nel formato Open Neural Network Exchange (ONNX), uno standard per rappresentare modelli di machine learning. L'inferenza con ONNX Runtime può garantire esperienze cliente più veloci e costi inferiori, supportando modelli di framework deep learning come PyTorch e TensorFlow/Keras, così come librerie classiche di machine learning come scikit-learn, LightGBM, XGBoost, ecc. ONNX Runtime è compatibile con diversi hardware, driver e sistemi operativi, fornendo prestazioni ottimali sfruttando gli acceleratori hardware dove applicabile insieme a ottimizzazioni e trasformazioni del grafo.

## Cos'è l'AI generativa?
L'AI generativa si riferisce a sistemi di intelligenza artificiale in grado di generare nuovi contenuti, come testo, immagini o musica, basandosi sui dati su cui sono stati addestrati. Gli esempi includono modelli linguistici come GPT-3 e modelli di generazione di immagini come Stable Diffusion. La libreria ONNX Runtime per GenAI fornisce il ciclo AI generativo per modelli ONNX, inclusa l'inferenza con ONNX Runtime, l'elaborazione dei logits, la ricerca e il campionamento, e la gestione della cache KV.

## ONNX Runtime per GENAI
ONNX Runtime per GENAI estende le capacità di ONNX Runtime per supportare modelli di AI generativa. Ecco alcune funzionalità chiave:

- **Ampio Supporto Piattaforme:** Funziona su varie piattaforme, inclusi Windows, Linux, macOS, Android e iOS.
- **Supporto Modelli:** Supporta molti modelli generativi AI popolari, come LLaMA, GPT-Neo, BLOOM e altri.
- **Ottimizzazione delle Prestazioni:** Include ottimizzazioni per diversi acceleratori hardware come GPU NVIDIA, GPU AMD e altri2.
- **Facilità d'Uso:** Fornisce API per una facile integrazione nelle applicazioni, permettendo di generare testo, immagini e altri contenuti con codice minimo.
- Gli utenti possono chiamare un metodo generate() ad alto livello, o eseguire ogni iterazione del modello in un ciclo, generando un token alla volta, e opzionalmente aggiornando i parametri di generazione all'interno del ciclo.
- ONNX runtime supporta anche la ricerca greedy/beam e il campionamento TopP, TopK per generare sequenze di token e l'elaborazione incorporata dei logits come le penalità di ripetizione. Puoi anche aggiungere facilmente un punteggio personalizzato.

## Per Iniziare
Per iniziare con ONNX Runtime per GENAI, puoi seguire questi passaggi:

### Installa ONNX Runtime:
```Python
pip install onnxruntime
```
### Installa le estensioni di AI generativa:
```Python
pip install onnxruntime-genai
```

### Esegui un Modello: Ecco un semplice esempio in Python:
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
### Demo: Utilizzo di ONNX Runtime GenAI per chiamare Phi-3.5-Vision


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


**Altri**

Oltre ai metodi di riferimento ONNX Runtime, Ollama e Foundry Local, possiamo anche completare il riferimento di modelli quantitativi basati sui metodi di riferimento dei modelli forniti da diversi produttori. Come il framework Apple MLX con Apple Metal, Qualcomm QNN con NPU, Intel OpenVINO con CPU/GPU, ecc. Puoi ottenere ulteriori contenuti da [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Altro

Abbiamo appreso le basi della famiglia Phi-3/3.5, ma per conoscere meglio SLM abbiamo bisogno di ulteriori conoscenze. Puoi trovare le risposte nel Phi-3 Cookbook. Se vuoi approfondire, visita il [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->