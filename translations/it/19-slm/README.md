# Introduzione ai Modelli Linguistici Piccoli per l'IA Generativa per Principianti
L'IA generativa è un campo affascinante dell'intelligenza artificiale che si concentra sulla creazione di sistemi capaci di generare nuovi contenuti. Questi contenuti possono variare da testo e immagini a musica e persino interi ambienti virtuali. Una delle applicazioni più entusiasmanti dell'IA generativa riguarda i modelli linguistici.

## Cosa Sono i Modelli Linguistici Piccoli?

Un Modello Linguistico Piccolo (SLM) rappresenta una variante ridotta di un grande modello linguistico (LLM), sfruttando molti dei principi architetturali e delle tecniche degli LLM, pur manifestando un'impronta computazionale significativamente ridotta.

Gli SLM sono una sottoclasse di modelli linguistici progettati per generare testo simile a quello umano. A differenza dei loro omologhi più grandi, come GPT-4, gli SLM sono più compatti ed efficienti, rendendoli ideali per applicazioni in cui le risorse computazionali sono limitate. Nonostante le dimensioni ridotte, possono comunque svolgere una varietà di compiti. Tipicamente, gli SLM sono costruiti comprimendo o distillando gli LLM, con l'obiettivo di mantenere una parte sostanziale delle funzionalità e delle capacità linguistiche del modello originale. Questa riduzione delle dimensioni del modello diminuisce la complessità complessiva, rendendo gli SLM più efficienti in termini sia di utilizzo della memoria sia di requisiti computazionali. Nonostante queste ottimizzazioni, gli SLM possono comunque eseguire un'ampia gamma di compiti di elaborazione del linguaggio naturale (NLP):

- Generazione di Testo: Creazione di frasi o paragrafi coerenti e contestualmente rilevanti.
- Completamento del Testo: Predire e completare frasi basate su un prompt fornito.
- Traduzione: Conversione di testo da una lingua all'altra.
- Sintesi: Condensare testi lunghi in riepiloghi più brevi e facilmente comprensibili.

Seppur con alcuni compromessi in termini di prestazioni o profondità di comprensione rispetto ai loro omologhi più grandi.

## Come Funzionano i Modelli Linguistici Piccoli?
Gli SLM sono addestrati su vasti dati di testo. Durante l'addestramento, imparano i modelli e le strutture del linguaggio, permettendo loro di generare testo sia grammaticalmente corretto che contestualmente appropriato. Il processo di addestramento comprende:

- Raccolta Dati: Raccogliere grandi set di dati di testo da varie fonti.
- Preprocessing: Pulire e organizzare i dati per renderli adatti all'addestramento.
- Addestramento: Usare algoritmi di machine learning per insegnare al modello come comprendere e generare testo.
- Messa a Punto: Regolare il modello per migliorare le sue prestazioni su compiti specifici.

Lo sviluppo degli SLM si allinea con la crescente necessità di modelli che possano essere distribuiti in ambienti con risorse limitate, come dispositivi mobili o piattaforme di edge computing, dove i LLM su larga scala possono risultare impraticabili a causa dei loro elevati requisiti di risorse. Concentrandosi sull'efficienza, gli SLM bilanciano prestazioni e accessibilità, permettendo una più ampia applicazione in vari domini.

![slm](../../../translated_images/it/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Obiettivi di Apprendimento

In questa lezione, speriamo di introdurre la conoscenza degli SLM e combinarla con Microsoft Phi-3 per esplorare diversi scenari nel contenuto testuale, nella visione e in MoE.

Alla fine di questa lezione, dovresti essere in grado di rispondere alle seguenti domande:

- Cos'è un SLM?
- Qual è la differenza tra SLM e LLM?
- Cos'è la Famiglia Microsoft Phi-3/3.5?
- Come eseguire l'inferenza con la Famiglia Microsoft Phi-3/3.5?

Pronti? Iniziamo.

## Le Differenze tra Grandi Modelli Linguistici (LLM) e Piccoli Modelli Linguistici (SLM)

Sia gli LLM che gli SLM si basano su principi fondamentali di apprendimento automatico probabilistico, seguendo approcci simili nel loro design architetturale, metodologie di addestramento, processi di generazione dati e tecniche di valutazione del modello. Tuttavia, diversi fattori chiave differenziano questi due tipi di modelli.

## Applicazioni dei Modelli Linguistici Piccoli

Gli SLM hanno una vasta gamma di applicazioni, tra cui:

- Chatbot: Fornire supporto clienti e interagire con gli utenti in modo conversazionale.
- Creazione di Contenuti: Assistere gli scrittori generando idee o addirittura bozze di interi articoli.
- Educazione: Aiutare gli studenti con i compiti di scrittura o nell'apprendimento di nuove lingue.
- Accessibilità: Creare strumenti per persone con disabilità, come sistemi di sintesi vocale.

**Dimensioni**
  
Una distinzione primaria tra LLM e SLM risiede nella scala dei modelli. Gli LLM, come ChatGPT (GPT-4), possono comprendere un numero stimato di 1,76 trilioni di parametri, mentre gli SLM open source come Mistral 7B sono progettati con molti meno parametri—circa 7 miliardi. Questa disparità è principalmente dovuta a differenze nell'architettura del modello e nei processi di addestramento. Ad esempio, ChatGPT impiega un meccanismo di self-attention all'interno di un framework encoder-decoder, mentre Mistral 7B utilizza l'attenzione a finestra scorrevole, che consente un addestramento più efficiente in un modello solo decoder. Questa variazione architetturale ha implicazioni profonde per la complessità e le prestazioni di questi modelli.

**Comprensione**

Gli SLM sono tipicamente ottimizzati per prestazioni in domini specifici, rendendoli altamente specializzati ma potenzialmente limitati nella capacità di fornire una comprensione contestuale ampia su diversi campi di conoscenza. Al contrario, gli LLM mirano a simulare un'intelligenza simile a quella umana su un livello più ampio. Addestrati su vasti e diversificati set di dati, gli LLM sono progettati per funzionare bene in una varietà di domini, offrendo maggiore versatilità e adattabilità. Di conseguenza, gli LLM sono più adatti a un'ampia gamma di compiti a valle, come l'elaborazione del linguaggio naturale e la programmazione.

**Calcolo**

L'addestramento e il deployment degli LLM sono processi che richiedono molte risorse, spesso necessitando di infrastrutture computazionali significative, inclusi grandi cluster di GPU. Ad esempio, l'addestramento di un modello come ChatGPT da zero può richiedere migliaia di GPU per lunghi periodi. Al contrario, gli SLM, con il loro minor numero di parametri, sono più accessibili in termini di risorse computazionali. Modelli come Mistral 7B possono essere addestrati e eseguiti su macchine locali dotate di GPU di capacità moderata, anche se l'addestramento comunque richiede diverse ore su più GPU.

**Bias**

Il bias è un problema conosciuto negli LLM, principalmente a causa della natura dei dati di addestramento. Questi modelli spesso si basano su dati grezzi e disponibili pubblicamente provenienti da internet, che possono sottorappresentare o rappresentare in modo errato certi gruppi, introdurre etichettature errate o riflettere bias linguistici influenzati da dialetti, variazioni geografiche e regole grammaticali. Inoltre, la complessità delle architetture LLM può involontariamente esacerbare il bias, che può passare inosservato senza un'accurata messa a punto. D'altro canto, gli SLM, essendo addestrati su set di dati più limitati e specifici per dominio, sono intrinsecamente meno suscettibili a tali bias, anche se non ne sono immuni.

**Inferenza**

La ridotta dimensione degli SLM conferisce loro un notevole vantaggio in termini di velocità di inferenza, permettendo di generare output efficacemente su hardware locale senza la necessità di elaborazioni parallele estese. Al contrario, gli LLM, a causa delle loro dimensioni e complessità, spesso richiedono risorse computazionali parallele sostanziali per raggiungere tempi di inferenza accettabili. La presenza di più utenti contemporanei rallenta ulteriormente i tempi di risposta degli LLM, specialmente quando distribuiti su larga scala.

In sintesi, mentre sia LLM che SLM condividono una base fondamentale nell'apprendimento automatico, differiscono significativamente in termini di dimensioni del modello, requisiti di risorse, comprensione contestuale, suscettibilità ai bias e velocità di inferenza. Queste distinzioni riflettono la loro rispettiva idoneità a diversi casi d'uso, con gli LLM più versatili ma ad alto consumo di risorse, e gli SLM che offrono maggiore efficienza specifica per dominio con richieste computazionali ridotte.

***Nota: In questa lezione introdurremo gli SLM usando Microsoft Phi-3 / 3.5 come esempio.***

## Introduzione alla Famiglia Phi-3 / Phi-3.5

La Famiglia Phi-3 / 3.5 è principalmente destinata a scenari applicativi di testo, visione e Agent (MoE):

### Phi-3 / 3.5 Instruct

Principalmente per generazione di testo, completamento di chat ed estrazione di informazioni dal contenuto, ecc.

**Phi-3-mini**

Il modello linguistico da 3.8B è disponibile su Microsoft Foundry, Hugging Face e Ollama. I modelli Phi-3 superano significativamente i modelli linguistici di dimensioni uguali o maggiori nei benchmark principali (vedi numeri dei benchmark sotto, numeri più alti sono migliori). Phi-3-mini supera modelli di doppia dimensione, mentre Phi-3-small e Phi-3-medium superano modelli più grandi, inclusi GPT-3.5.

**Phi-3-small & medium**

Con solo 7B parametri, Phi-3-small batte GPT-3.5T in una varietà di benchmark di linguaggio, ragionamento, codifica e matematica.

Il Phi-3-medium con 14B parametri continua questa tendenza e supera il Gemini 1.0 Pro.

**Phi-3.5-mini**

Possiamo considerarlo un upgrade di Phi-3-mini. Pur mantenendo invariati i parametri, migliora la capacità di supportare più lingue (supporta oltre 20 lingue: arabo, cinese, ceco, danese, olandese, inglese, finlandese, francese, tedesco, ebraico, ungherese, italiano, giapponese, coreano, norvegese, polacco, portoghese, russo, spagnolo, svedese, tailandese, turco, ucraino) ​​e aggiunge un supporto più forte per contesti lunghi.

Phi-3.5-mini con 3.8B parametri supera modelli della stessa dimensione ed è alla pari con modelli di dimensioni doppie.

### Phi-3 / 3.5 Vision

Possiamo considerare il modello Instruct di Phi-3/3.5 come la capacità di Phi di comprendere, e Vision è ciò che dà a Phi gli occhi per comprendere il mondo.


**Phi-3-Vision**

Phi-3-vision, con soli 4.2B parametri, continua questa tendenza e supera modelli più grandi come Claude-3 Haiku e Gemini 1.0 Pro V in compiti generali di ragionamento visivo, OCR e comprensione di tabelle e diagrammi.


**Phi-3.5-Vision**

Phi-3.5-Vision è anche un upgrade di Phi-3-Vision, aggiungendo supporto per immagini multiple. Puoi considerarlo come un miglioramento nella visione: non solo puoi vedere immagini, ma anche video.

Phi-3.5-vision supera modelli più grandi come Claude-3.5 Sonnet e Gemini 1.5 Flash in compiti di OCR, comprensione di tabelle e grafici ed è alla pari nei compiti generali di ragionamento visivo. Supporta input multi-frame, cioè esegue ragionamenti su molteplici immagini di input


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** permette ai modelli di essere pre-addestrati con molto meno calcolo, il che significa che puoi aumentare drasticamente la scala del modello o della dimensione del dataset con lo stesso budget computazionale di un modello denso. In particolare, un modello MoE dovrebbe raggiungere la stessa qualità del suo omologo denso molto più rapidamente durante il pre-addestramento.

Phi-3.5-MoE comprende 16 moduli esperti da 3.8B ciascuno. Phi-3.5-MoE con solo 6.6B parametri attivi raggiunge un livello simile di ragionamento, comprensione del linguaggio e matematica rispetto a modelli molto più grandi

Possiamo usare il modello della Famiglia Phi-3/3.5 in base a differenti scenari. A differenza degli LLM, puoi distribuire Phi-3/3.5-mini o Phi-3/3.5-Vision su dispositivi edge.


## Come usare i modelli della Famiglia Phi-3/3.5

Speriamo di usare Phi-3/3.5 in diversi scenari. Di seguito useremo Phi-3/3.5 basandoci su diversi scenari.

![phi3](../../../translated_images/it/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inferenza tramite API Cloud

**Modelli Microsoft Foundry**

> **Nota:** GitHub Models sarà dismesso alla fine di luglio 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) è il sostituto diretto.

Microsoft Foundry Models è il modo più diretto. Puoi accedere rapidamente al modello Phi-3/3.5-Instruct tramite il catalogo dei modelli Foundry. Combinato con Azure AI Inference SDK / OpenAI SDK, puoi accedere all'API tramite codice per completare la chiamata a Phi-3/3.5-Instruct. Puoi anche testare i diversi effetti tramite il Playground.

- Demo: Confronto degli effetti di Phi-3-mini e Phi-3.5-mini in scenari cinesi

![phi3](../../../translated_images/it/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/it/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Oppure, se vogliamo usare i modelli vision e MoE, puoi utilizzare Microsoft Foundry per completare la chiamata. Se sei interessato, puoi leggere il Phi-3 Cookbook per imparare come chiamare Phi-3/3.5 Instruct, Vision, MoE tramite Microsoft Foundry [Clicca questo link](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Oltre al catalogo Microsoft Foundry Models basato sul cloud, puoi anche utilizzare [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) per completare le chiamate correlate. Puoi visitare NVIDIA NIM per completare le chiamate API della Famiglia Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) è un insieme di microservizi di inferenza accelerati progettati per aiutare gli sviluppatori a distribuire modelli AI in modo efficiente attraverso vari ambienti, inclusi cloud, data center e workstation.

Ecco alcune caratteristiche chiave di NVIDIA NIM:

- **Facilità di Deploy:** NIM permette di distribuire modelli AI con un solo comando, rendendo semplice l'integrazione in flussi di lavoro esistenti.
- **Prestazioni Ottimizzate:** Sfrutta i motori di inferenza pre-ottimizzati di NVIDIA, come TensorRT e TensorRT-LLM, per garantire bassa latenza e alto throughput.
- **Scalabilità:** NIM supporta l'autoscaling su Kubernetes, permettendo di gestire efficacemente carichi di lavoro variabili.
- **Sicurezza e Controllo:** Le organizzazioni possono mantenere il controllo sui propri dati e applicazioni ospitando autonomamente i microservizi NIM sulla propria infrastruttura gestita.
- **API standard:** NIM fornisce API standard di settore, rendendo facile costruire e integrare applicazioni AI come chatbot, assistenti AI e altro.

NIM fa parte di NVIDIA AI Enterprise, che mira a semplificare il deploy e l'operazionalizzazione dei modelli AI, garantendo che funzionino in modo efficiente sulle GPU NVIDIA.

- Demo: Uso di NVIDIA NIM per chiamare Phi-3.5-Vision-API  [[Clicca questo link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Esecuzione Locale di Phi-3/3.5
L'inferenza in relazione a Phi-3, o qualsiasi modello linguistico come GPT-3, si riferisce al processo di generazione di risposte o previsioni basate sull'input ricevuto. Quando fornisci un prompt o una domanda a Phi-3, usa la sua rete neurale addestrata per inferire la risposta più probabile e rilevante analizzando schemi e relazioni nei dati su cui è stato addestrato.

**Hugging Face Transformer**
Hugging Face Transformers è una potente libreria progettata per l'elaborazione del linguaggio naturale (NLP) e altri compiti di machine learning. Ecco alcuni punti chiave al riguardo:

1. **Modelli Preaddestrati**: Fornisce migliaia di modelli preaddestrati utilizzabili per vari compiti come classificazione del testo, riconoscimento di entità nominate, risposta a domande, sintesi, traduzione e generazione di testo.

2. **Interoperabilità dei Framework**: La libreria supporta diversi framework di deep learning, inclusi PyTorch, TensorFlow e JAX. Ciò consente di addestrare un modello in un framework e utilizzarlo in un altro.

3. **Capacità Multimodali**: Oltre all'NLP, Hugging Face Transformers supporta anche compiti in visione artificiale (es. classificazione immagini, rilevamento oggetti) e elaborazione audio (es. riconoscimento vocale, classificazione audio).

4. **Facilità d'Uso**: La libreria offre API e strumenti per scaricare e ottimizzare facilmente i modelli, risultando accessibile sia ai principianti che agli esperti.

5. **Comunità e Risorse**: Hugging Face ha una comunità vivace e una documentazione estesa, tutorial e guide per aiutare gli utenti a iniziare e sfruttare al meglio la libreria.
[documentazione ufficiale](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) o il loro [repository GitHub](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Questo è il metodo più comunemente usato, ma richiede anche accelerazione GPU. Dopotutto, scenari come Vision e MoE richiedono molti calcoli, che saranno molto lenti su CPU se non quantizzati.


- Demo: Usare Transformer per chiamare Phi-3.5-Instruct [Clicca questo link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Usare Transformer per chiamare Phi-3.5-Vision [Clicca questo link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Usare Transformer per chiamare Phi-3.5-MoE [Clicca questo link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) è una piattaforma progettata per semplificare l'esecuzione di grandi modelli linguistici (LLM) localmente sulla tua macchina. Supporta vari modelli come Llama 3.1, Phi 3, Mistral e Gemma 2, tra gli altri. La piattaforma semplifica il processo raggruppando pesi del modello, configurazione e dati in un unico pacchetto, rendendo più accessibile agli utenti la personalizzazione e la creazione dei propri modelli. Ollama è disponibile per macOS, Linux e Windows. È uno strumento eccellente se vuoi sperimentare o distribuire LLM senza dipendere dai servizi cloud. Ollama è il metodo più diretto, devi solo eseguire il comando seguente.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) è l'ambiente di runtime offline e on-device di Microsoft per eseguire modelli come Phi interamente sul tuo hardware privato - senza bisogno di abbonamento Azure, chiave API o connessione di rete. Sceglie automaticamente il miglior provider di esecuzione disponibile (NPU, GPU o CPU) ed espone un endpoint compatibile con OpenAI, così il codice esistente `openai`/Azure AI Inference SDK può puntarci con modifiche minime. Consulta la [documentazione di Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) per iniziare.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) è un acceleratore di inferenza e addestramento di machine learning multipiattaforma. ONNX Runtime per Generative AI (GENAI) è uno strumento potente che ti aiuta a eseguire modelli AI generativi in modo efficiente su varie piattaforme.

## Cos'è ONNX Runtime?
ONNX Runtime è un progetto open source che consente inferenze ad alte prestazioni di modelli di machine learning. Supporta modelli nel formato Open Neural Network Exchange (ONNX), uno standard per rappresentare modelli di machine learning. L'inferenza ONNX Runtime può abilitare esperienze cliente più rapide e costi inferiori, supportando modelli da framework di deep learning come PyTorch e TensorFlow/Keras, oltre a librerie classiche di machine learning come scikit-learn, LightGBM, XGBoost, ecc. ONNX Runtime è compatibile con diversi hardware, driver e sistemi operativi, e offre prestazioni ottimali sfruttando acceleratori hardware quando applicabili, insieme a ottimizzazioni e trasformazioni del grafo.

## Cos'è l'Intelligenza Artificiale Generativa?
L'Intelligenza Artificiale Generativa si riferisce a sistemi AI che possono generare nuovi contenuti, come testo, immagini o musica, basandosi sui dati su cui sono stati addestrati. Esempi includono modelli linguistici come GPT-3 e modelli di generazione immagini come Stable Diffusion. La libreria ONNX Runtime per GenAI fornisce il ciclo di intelligenza artificiale generativa per modelli ONNX, inclusi inferenza con ONNX Runtime, elaborazione logits, ricerca e campionamento, e gestione della cache KV.

## ONNX Runtime per GENAI
ONNX Runtime per GENAI estende le capacità di ONNX Runtime per supportare modelli AI generativi. Ecco alcune caratteristiche chiave:

- **Ampio Supporto alla Piattaforma:** Funziona su varie piattaforme, inclusi Windows, Linux, macOS, Android e iOS.
- **Supporto ai Modelli:** Supporta molti modelli AI generativi popolari, come LLaMA, GPT-Neo, BLOOM e altri.
- **Ottimizzazione delle Prestazioni:** Include ottimizzazioni per diversi acceleratori hardware come NVIDIA GPU, AMD GPU, e altro2.
- **Facilità d'Uso:** Fornisce API per una facile integrazione nelle applicazioni, permettendoti di generare testo, immagini e altri contenuti con codice minimo
- Gli utenti possono chiamare un metodo generate() di alto livello o eseguire ogni iterazione del modello in un ciclo, generando un token alla volta e opzionalmente aggiornando i parametri di generazione all'interno del ciclo.
- ONNX runtime supporta anche la ricerca greedy/beam e il campionamento TopP, TopK per generare sequenze di token e l'elaborazione logits integrata come penalità di ripetizione. Puoi anche aggiungere facilmente un punteggio personalizzato.

## Come Iniziare
Per iniziare con ONNX Runtime per GENAI, puoi seguire questi passaggi:

### Installa ONNX Runtime:
```Python
pip install onnxruntime
```
### Installa le Estensioni AI Generative:
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
### Demo: Uso di ONNX Runtime GenAI per chiamare Phi-3.5-Vision


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

Oltre ai metodi di riferimento ONNX Runtime, Ollama e Foundry Local, possiamo anche completare il riferimento ai modelli quantitativi basati sui metodi di riferimento modello forniti dai diversi produttori. Come il framework Apple MLX con Apple Metal, Qualcomm QNN con NPU, Intel OpenVINO con CPU/GPU, ecc. Puoi anche ottenere più contenuti da [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Altro

Abbiamo appreso le basi della Famiglia Phi-3/3.5, ma per saperne di più su SLM abbiamo bisogno di maggiori conoscenze. Puoi trovare le risposte nel Phi-3 Cookbook. Se vuoi approfondire, visita il [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->