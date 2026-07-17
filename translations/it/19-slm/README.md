# Introduzione ai Modelli Linguistici Piccoli per l'IA Generativa per Principianti
L'IA generativa è un campo affascinante dell'intelligenza artificiale che si concentra sulla creazione di sistemi in grado di generare nuovi contenuti. Questi contenuti possono spaziare da testi e immagini a musica e persino interi ambienti virtuali. Una delle applicazioni più entusiasmanti dell'IA generativa è nel campo dei modelli linguistici.

## Cosa Sono i Modelli Linguistici Piccoli?

Un Modello Linguistico Piccolo (SLM) rappresenta una variante ridotta di un grande modello linguistico (LLM), sfruttando molti dei principi architetturali e delle tecniche dei LLM, pur presentando un'impronta computazionale significativamente ridotta.

Gli SLM sono un sottoinsieme di modelli linguistici progettati per generare testo simile a quello umano. A differenza dei loro omologhi più grandi, come GPT-4, gli SLM sono più compatti ed efficienti, rendendoli ideali per applicazioni in cui le risorse computazionali sono limitate. Nonostante la loro dimensione ridotta, possono comunque svolgere una varietà di compiti. Tipicamente, gli SLM sono costruiti comprimendo o distillando LLM, con l'obiettivo di mantenere una porzione sostanziale delle funzionalità e delle capacità linguistiche del modello originale. Questa riduzione della dimensione del modello diminuisce la complessità complessiva, rendendo gli SLM più efficienti sia in termini di uso della memoria che di requisiti computazionali. Nonostante queste ottimizzazioni, gli SLM possono comunque svolgere una vasta gamma di compiti di elaborazione del linguaggio naturale (NLP):

- Generazione di Testo: Creare frasi o paragrafi coerenti e contestualmente rilevanti.
- Completamento di Testo: Predire e completare frasi basate su un prompt dato.
- Traduzione: Convertire il testo da una lingua all'altra.
- Sintesi: Condensare lunghi pezzi di testo in riassunti più brevi e digeribili.

Anche se con alcuni compromessi in termini di prestazioni o profondità di comprensione rispetto ai loro omologhi più grandi.

## Come Funzionano i Modelli Linguistici Piccoli?
Gli SLM sono addestrati su enormi quantità di dati testuali. Durante l'addestramento, apprendono i modelli e le strutture della lingua, permettendo loro di generare testo grammaticalmente corretto e contestualmente appropriato. Il processo di addestramento coinvolge:

- Raccolta Dati: Raccogliere grandi dataset di testo da varie fonti.
- Pre-elaborazione: Pulire e organizzare i dati per renderli adatti all'addestramento.
- Addestramento: Utilizzare algoritmi di machine learning per insegnare al modello come comprendere e generare testo.
- Ottimizzazione: Regolare il modello per migliorare le sue prestazioni in compiti specifici.

Lo sviluppo degli SLM è in linea con la crescente esigenza di modelli che possano essere distribuiti in ambienti con risorse limitate, come dispositivi mobili o piattaforme di edge computing, dove i LLM completi potrebbero essere impraticabili a causa delle loro elevate richieste di risorse. Concentrandosi sull'efficienza, gli SLM bilanciano le prestazioni con l'accessibilità, consentendo un'applicazione più ampia in vari domini.

![slm](../../../translated_images/it/slm.4058842744d0444a.webp)

## Obiettivi di Apprendimento

In questa lezione, speriamo di introdurre la conoscenza degli SLM e combinarla con Microsoft Phi-3 per imparare diversi scenari nei contenuti testuali, nella visione e nel MoE.

Alla fine di questa lezione dovresti essere in grado di rispondere alle seguenti domande:

- Che cos'è un SLM?
- Qual è la differenza tra SLM e LLM?
- Cos'è la famiglia Microsoft Phi-3/3.5?
- Come eseguire inferenza con la famiglia Microsoft Phi-3/3.5?

Pronti? Iniziamo.

## Le Differenze tra i Grandi Modelli Linguistici (LLM) e i Modelli Linguistici Piccoli (SLM)

Sia gli LLM che gli SLM sono basati su principi fondamentali del machine learning probabilistico, seguendo approcci simili nel design architetturale, nelle metodologie di addestramento, nei processi di generazione dati e nelle tecniche di valutazione del modello. Tuttavia, diversi fattori chiave differenziano questi due tipi di modelli.

## Applicazioni dei Modelli Linguistici Piccoli

Gli SLM hanno una vasta gamma di applicazioni, tra cui:

- Chatbot: Fornire supporto clienti e interagire con gli utenti in modo conversazionale.
- Creazione di Contenuti: Assistere gli scrittori generando idee o addirittura redigendo articoli completi.
- Educazione: Aiutare gli studenti con compiti di scrittura o nell'apprendimento di nuove lingue.
- Accessibilità: Creare strumenti per persone con disabilità, come sistemi di sintesi vocale.

**Dimensione**
  
Una distinzione primaria tra LLM e SLM risiede nella scala dei modelli. Gli LLM, come ChatGPT (GPT-4), possono comprendere circa 1,76 trilioni di parametri, mentre gli SLM open-source come Mistral 7B sono progettati con un numero significativamente inferiore di parametri—circa 7 miliardi. Questa disparità è dovuta principalmente alle differenze nell'architettura del modello e nei processi di addestramento. Per esempio, ChatGPT utilizza un meccanismo di self-attention all'interno di un framework encoder-decoder, mentre Mistral 7B usa l'attenzione a finestra scorrevole, che consente un addestramento più efficiente all'interno di un modello solo decoder. Questa differenza architetturale ha profonde implicazioni sulla complessità e sulle prestazioni di questi modelli.

**Comprensione**

Gli SLM sono tipicamente ottimizzati per prestazioni all'interno di domini specifici, rendendoli altamente specializzati ma potenzialmente limitati nella capacità di fornire una comprensione contestuale ampia su più campi di conoscenza. Al contrario, gli LLM mirano a simulare un'intelligenza umanoide a un livello più completo. Addestrati su ampi ensemble di dati diversificati, gli LLM sono progettati per performare bene in una varietà di domini, offrendo maggiore versatilità e adattabilità. Di conseguenza, gli LLM sono più adatti a una più ampia gamma di compiti a valle, come l'elaborazione del linguaggio naturale e la programmazione.

**Calcolo**

L'addestramento e la distribuzione degli LLM sono processi intensivi in termini di risorse, che spesso richiedono un'infrastruttura computazionale significativa, inclusi cluster GPU su larga scala. Per esempio, addestrare un modello come ChatGPT da zero può richiedere migliaia di GPU per periodi prolungati. Al contrario, gli SLM, con il loro minor numero di parametri, sono più accessibili in termini di risorse computazionali. Modelli come Mistral 7B possono essere addestrati ed eseguiti su macchine locali dotate di capacità GPU moderate, anche se l'addestramento richiede comunque diverse ore su più GPU.

**Bias**

Il bias è un problema noto negli LLM, dovuto principalmente alla natura dei dati di addestramento. Questi modelli spesso si basano su dati grezzi apertamente disponibili su internet, che possono sottorappresentare o rappresentare erroneamente certi gruppi, introdurre etichettature errate o riflettere bias linguistici influenzati da dialetti, variazioni geografiche e regole grammaticali. Inoltre, la complessità delle architetture LLM può involontariamente esacerbare i bias, che possono passare inosservati senza un'attenta ottimizzazione fine. D'altra parte, gli SLM, essendo addestrati su dataset più ristretti e specifici di dominio, sono intrinsecamente meno suscettibili a tali bias, anche se non immuni.

**Inferenza**

La ridotta dimensione degli SLM conferisce loro un vantaggio significativo in termini di velocità di inferenza, permettendo di generare output in modo efficiente su hardware locale senza la necessità di elaborazione parallela estesa. Al contrario, gli LLM, a causa della loro dimensione e complessità, spesso richiedono risorse computazionali parallele sostanziali per raggiungere tempi di inferenza accettabili. La presenza di più utenti contemporanei rallenta ulteriormente i tempi di risposta degli LLM, specialmente quando distribuiti su larga scala.

In sintesi, mentre sia gli LLM che gli SLM condividono una base fondamentale nel machine learning, differiscono notevolmente in termini di dimensione del modello, requisiti di risorse, comprensione contestuale, suscettibilità ai bias e velocità di inferenza. Queste differenze riflettono la loro idoneità rispettiva a diversi casi d'uso, con gli LLM più versatili ma pesanti in risorse, e gli SLM che offrono maggiore efficienza specifica di dominio con richieste computazionali ridotte.

***Nota: In questa lezione, introdurremo gli SLM usando Microsoft Phi-3 / 3.5 come esempio.***

## Introduzione alla Famiglia Phi-3 / Phi-3.5

La famiglia Phi-3 / 3.5 è principalmente indirizzata a scenari applicativi di testo, visione e Agente (MoE):

### Phi-3 / 3.5 Instruct

Principalmente per generazione di testo, completamento di chat, estrazione di informazioni di contenuto, ecc.

**Phi-3-mini**

Il modello linguistico da 3.8B è disponibile su Microsoft Foundry, Hugging Face e Ollama. I modelli Phi-3 superano significativamente i modelli linguistici di dimensioni uguali o maggiori su benchmark chiave (vedi i numeri del benchmark sotto, numeri più alti sono migliori). Phi-3-mini supera modelli di dimensioni doppie, mentre Phi-3-small e Phi-3-medium superano modelli più grandi, inclusi GPT-3.5.

**Phi-3-small & medium**

Con soli 7B parametri, Phi-3-small supera GPT-3.5T in vari benchmark di lingua, ragionamento, coding e matematica.

Il Phi-3-medium con 14B parametri continua questa tendenza e supera il Gemini 1.0 Pro.

**Phi-3.5-mini**

Lo possiamo considerare un aggiornamento di Phi-3-mini. Pur mantenendo invariati i parametri, migliora la capacità di supportare più lingue (supporta oltre 20 lingue: Arabo, Cinese, Ceco, Danese, Olandese, Inglese, Finlandese, Francese, Tedesco, Ebraico, Ungherese, Italiano, Giapponese, Coreano, Norvegese, Polacco, Portoghese, Russo, Spagnolo, Svedese, Tailandese, Turco, Ucraino) e aggiunge un supporto più robusto per il contesto lungo.

Phi-3.5-mini con 3.8B parametri supera modelli linguistici della stessa dimensione ed è pari a modelli di dimensioni doppie.

### Phi-3 / 3.5 Vision

Possiamo considerare il modello Instruct di Phi-3/3.5 come la capacità di Phi di comprendere, mentre Vision è ciò che dà a Phi gli occhi per comprendere il mondo.


**Phi-3-Vision**

Phi-3-vision, con solo 4.2B parametri, continua questa tendenza e supera modelli più grandi come Claude-3 Haiku e Gemini 1.0 Pro V in compiti generali di ragionamento visivo, OCR e comprensione di tabelle e diagrammi.


**Phi-3.5-Vision**

Phi-3.5-Vision è anche un aggiornamento di Phi-3-Vision, aggiungendo il supporto per immagini multiple. Lo si può considerare un miglioramento nella visione, non solo si possono vedere immagini, ma anche video.

Phi-3.5-vision supera modelli più grandi come Claude-3.5 Sonnet e Gemini 1.5 Flash in OCR, comprensione di tabelle e grafici ed è pari su compiti generali di ragionamento visivo. Supporta input multi-frame, ovvero ragionare su più immagini in input.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** permette ai modelli di essere pre-addestrati con molto meno calcolo, il che significa poter scalare drasticamente la dimensione del modello o del dataset con lo stesso budget computazionale di un modello denso. In particolare, un modello MoE dovrebbe raggiungere la stessa qualità del suo omologo denso molto più rapidamente durante il pre-addestramento.

Phi-3.5-MoE comprende 16 moduli esperti da 3.8B ciascuno. Phi-3.5-MoE con soli 6.6B parametri attivi raggiunge un livello simile di ragionamento, comprensione linguistica e matematica rispetto a modelli molto più grandi.

Possiamo usare il modello della famiglia Phi-3/3.5 in base a diversi scenari. A differenza degli LLM, puoi distribuire Phi-3/3.5-mini o Phi-3/3.5-Vision su dispositivi edge.


## Come usare i modelli della famiglia Phi-3/3.5

Speriamo di usare Phi-3/3.5 in diversi scenari. Successivamente, utilizzeremo Phi-3/3.5 basandoci su diversi scenari.

![phi3](../../../translated_images/it/phi3.655208c3186ae381.webp)

### Inferenza tramite API cloud

**Modelli Microsoft Foundry**

> **Nota:** GitHub Models verrà ritirato alla fine di luglio 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) è il sostituto diretto.

Microsoft Foundry Models è il modo più diretto. Puoi accedere rapidamente al modello Phi-3/3.5-Instruct tramite il catalogo modelli Foundry. Combinato con Azure AI Inference SDK / OpenAI SDK, puoi accedere all'API tramite codice per completare la chiamata Phi-3/3.5-Instruct. Puoi anche testare diversi effetti tramite il Playground.

- Demo: Confronto degli effetti di Phi-3-mini e Phi-3.5-mini in scenari cinesi

![phi3](../../../translated_images/it/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/it/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Oppure, se vogliamo usare i modelli vision e MoE, possiamo usare Microsoft Foundry per completare la chiamata. Se sei interessato, puoi leggere il Phi-3 Cookbook per imparare come chiamare Phi-3/3.5 Instruct, Vision, MoE tramite Microsoft Foundry [Clicca questo link](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Oltre al catalogo Microsoft Foundry Models basato su cloud, puoi anche usare [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) per completare chiamate correlate. Puoi visitare NVIDIA NIM per completare le chiamate API della famiglia Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) è un insieme di microservizi di inferenza accelerata progettati per aiutare gli sviluppatori a distribuire modelli AI in modo efficiente in diversi ambienti, inclusi cloud, data center e workstation.

Ecco alcune caratteristiche chiave di NVIDIA NIM:

- **Facilità di Distribuzione:** NIM consente di distribuire modelli AI con un solo comando, rendendo facile l'integrazione nei flussi di lavoro esistenti.

- **Prestazioni Ottimizzate:** Sfrutta i motori di inferenza pre-ottimizzati di NVIDIA, come TensorRT e TensorRT-LLM, per garantire bassa latenza e alta produttività.
- **Scalabilità:** NIM supporta l'autoscaling su Kubernetes, consentendo di gestire efficacemente carichi di lavoro variabili.
- **Sicurezza e Controllo:** Le organizzazioni possono mantenere il controllo sui propri dati e applicazioni ospitando autonomamente i microservizi NIM nella loro infrastruttura gestita.
- **API Standard:** NIM fornisce API standard del settore, rendendo facile costruire e integrare applicazioni AI come chatbot, assistenti AI e altro.

NIM fa parte di NVIDIA AI Enterprise, che mira a semplificare il deployment e l’operazionalizzazione dei modelli AI, assicurando che funzionino in modo efficiente sulle GPU NVIDIA.

- Demo: Utilizzo di NVIDIA NIM per chiamare Phi-3.5-Vision-API  [[Clicca su questo link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Esecuzione Locale di Phi-3/3.5
L'inferenza in relazione a Phi-3, o a qualsiasi modello linguistico come GPT-3, si riferisce al processo di generazione di risposte o previsioni basate sull'input ricevuto. Quando fornisci un prompt o una domanda a Phi-3, utilizza la sua rete neurale addestrata per dedurre la risposta più probabile e rilevante analizzando pattern e relazioni nei dati su cui è stato addestrato.

**Transformer di Hugging Face**
Hugging Face Transformers è una potente libreria progettata per l'elaborazione del linguaggio naturale (NLP) e altri compiti di machine learning. Ecco alcuni punti chiave a riguardo:

1. **Modelli Preaddestrati**: Fornisce migliaia di modelli preaddestrati utilizzabili per vari compiti come classificazione del testo, riconoscimento di entità nominate, risposta a domande, sintesi, traduzione e generazione di testo.

2. **Interoperabilità tra Framework:** La libreria supporta più framework di deep learning, tra cui PyTorch, TensorFlow e JAX. Questo permette di addestrare un modello in un framework e usarlo in un altro.

3. **Capacità Multimodali:** Oltre all’NLP, Hugging Face Transformers supporta anche compiti in computer vision (es. classificazione immagini, rilevamento oggetti) e elaborazione audio (es. riconoscimento vocale, classificazione audio).

4. **Facilità d'Uso:** La libreria offre API e strumenti per scaricare e adattare facilmente i modelli, rendendola accessibile sia ai principianti che agli esperti.

5. **Comunità e Risorse:** Hugging Face ha una comunità vivace e una vasta documentazione, tutorial e guide per aiutare gli utenti a iniziare e sfruttare al meglio la libreria.
[documentazione ufficiale](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) o il loro [repository GitHub](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Questo è il metodo più comunemente usato, ma richiede anche accelerazione GPU. Dopotutto, scenari come Vision e MoE richiedono molti calcoli, che sarebbero molto lenti su CPU se non quantizzati.


- Demo: Utilizzo di Transformer per chiamare Phi-3.5-Instruct [Clicca su questo link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Utilizzo di Transformer per chiamare Phi-3.5-Vision [Clicca su questo link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Utilizzo di Transformer per chiamare Phi-3.5-MoE [Clicca su questo link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) è una piattaforma progettata per facilitare l’esecuzione locale di grandi modelli linguistici (LLM) sul tuo computer. Supporta vari modelli come Llama 3.1, Phi 3, Mistral e Gemma 2, tra gli altri. La piattaforma semplifica il processo raggruppando pesi dei modelli, configurazioni e dati in un unico pacchetto, rendendolo più accessibile per gli utenti che vogliono personalizzare e creare i propri modelli. Ollama è disponibile per macOS, Linux e Windows. È uno strumento eccellente se vuoi sperimentare o distribuire LLM senza dipendere da servizi cloud. Ollama è il modo più diretto, devi solo eseguire il comando seguente.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) è il runtime offline e on-device di Microsoft per eseguire modelli come Phi interamente sul tuo hardware - senza bisogno di abbonamento Azure, chiave API o connessione di rete. Seleziona automaticamente il miglior provider di esecuzione disponibile (NPU, GPU o CPU) ed espone un endpoint compatibile con OpenAI, quindi il codice esistente per `openai`/Azure AI Inference SDK può puntare ad esso con modifiche minime. Consulta la [documentazione di Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) per iniziare.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Oppure usa direttamente l’SDK in Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime per GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) è un acceleratore cross-platform per inferenza e training di machine learning. ONNX Runtime per Generative AI (GENAI) è uno strumento potente che ti aiuta a eseguire modelli AI generativi in modo efficiente su varie piattaforme.

## Cos’è ONNX Runtime?
ONNX Runtime è un progetto open source che consente un’inferenza ad alte prestazioni di modelli di machine learning. Supporta modelli in formato Open Neural Network Exchange (ONNX), che è uno standard per rappresentare modelli di machine learning. L’inferenza con ONNX Runtime può abilitare esperienze cliente più veloci e costi inferiori, supportando modelli di framework di deep learning come PyTorch e TensorFlow/Keras, così come librerie classiche di machine learning come scikit-learn, LightGBM, XGBoost, ecc. ONNX Runtime è compatibile con diversi hardware, driver e sistemi operativi, e fornisce prestazioni ottimali sfruttando acceleratori hardware dove disponibili assieme a ottimizzazioni e trasformazioni del grafo.

## Cos’è l’Intelligenza Artificiale Generativa?
L’Intelligenza Artificiale Generativa si riferisce a sistemi AI capaci di generare nuovo contenuto, come testo, immagini o musica, basati sui dati su cui sono stati addestrati. Esempi includono modelli linguistici come GPT-3 e modelli di generazione immagini come Stable Diffusion. La libreria ONNX Runtime per GenAI fornisce il ciclo generativo AI per modelli ONNX, inclusi inferenza con ONNX Runtime, elaborazione dei logits, ricerca e campionamento, e gestione della cache KV.

## ONNX Runtime per GENAI
ONNX Runtime per GENAI estende le capacità di ONNX Runtime per supportare modelli di AI generativa. Ecco alcune caratteristiche chiave:

- **Ampio Supporto Piattaforme:** Funziona su varie piattaforme, inclusi Windows, Linux, macOS, Android e iOS.
- **Supporto Modelli:** Supporta molti modelli generativi popolari, come LLaMA, GPT-Neo, BLOOM e altri.
- **Ottimizzazione delle Prestazioni:** Include ottimizzazioni per diversi acceleratori hardware come GPU NVIDIA, GPU AMD e altro2.
- **Facilità d'Uso:** Fornisce API per una facile integrazione nelle applicazioni, permettendo di generare testo, immagini e altri contenuti con codice minimo
- Gli utenti possono chiamare un metodo di alto livello generate(), o eseguire ogni iterazione del modello in un ciclo, generando un token alla volta e aggiornando opzionalmente i parametri di generazione all’interno del ciclo.
- ONNX runtime supporta anche ricerca greedy/beam e campionamento TopP, TopK per generare sequenze di token e l’elaborazione integrata di logits come penalità di ripetizione. Puoi anche facilmente aggiungere scoring personalizzato.

## Per Iniziare
Per iniziare con ONNX Runtime per GENAI, puoi seguire questi passaggi:

### Installa ONNX Runtime:
```Python
pip install onnxruntime
```
### Installa le Estensioni per Intelligenza Artificiale Generativa:
```Python
pip install onnxruntime-genai
```

### Esegui un Modello: Ecco un esempio semplice in Python:
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

Oltre a ONNX Runtime, Ollama e Foundry Local come metodi di riferimento, possiamo completare anche il riferimento di modelli quantitativi basati su metodi di riferimento modello forniti da diversi produttori. Come il framework Apple MLX con Apple Metal, Qualcomm QNN con NPU, Intel OpenVINO con CPU/GPU, ecc. Puoi anche ottenere più contenuti da [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Altro

Abbiamo appreso le basi della Famiglia Phi-3/3.5, ma per approfondire SLM abbiamo bisogno di più conoscenze. Puoi trovare le risposte nel Phi-3 Cookbook. Se vuoi saperne di più, visita il [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->