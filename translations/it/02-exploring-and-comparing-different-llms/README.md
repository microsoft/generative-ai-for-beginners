# Esplorare e confrontare diversi LLM

[![Esplorare e confrontare diversi LLM](../../../translated_images/it/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Clicca sull'immagine sopra per vedere il video di questa lezione_

Con la lezione precedente, abbiamo visto come l'AI Generativa stia cambiando il panorama tecnologico, come funzionano i Large Language Models (LLM) e come un'azienda - come la nostra startup - possa applicarli ai propri casi d'uso e crescere! In questo capitolo, cercheremo di confrontare e mettere a confronto diversi tipi di modelli linguistici di grandi dimensioni (LLM) per capire i loro pro e contro.

Il prossimo passo nel viaggio della nostra startup è esplorare il panorama attuale degli LLM e capire quali siano adatti al nostro caso d'uso.

## Introduzione

Questa lezione coprirà:

- Diversi tipi di LLM nel panorama attuale.
- Testare, iterare e confrontare diversi modelli per il tuo caso d'uso su Azure.
- Come distribuire un LLM.

## Obiettivi di apprendimento

Dopo aver completato questa lezione, sarai in grado di:

- Selezionare il modello giusto per il tuo caso d'uso.
- Capire come testare, iterare e migliorare le prestazioni del modello.
- Sapere come le aziende distribuiscono i modelli.

## Capire i diversi tipi di LLM

Gli LLM possono avere molteplici categorizzazioni basate sulla loro architettura, dati di addestramento e caso d'uso. Capire queste differenze aiuterà la nostra startup a selezionare il modello giusto per lo scenario e comprendere come testare, iterare e migliorare le prestazioni.

Esistono molti tipi diversi di modelli LLM, la scelta del modello dipende da cosa si intende usarli, dai tuoi dati, da quanto sei disposto a pagare e altro.

A seconda se intendi usare i modelli per testo, audio, video, generazione di immagini e così via, potresti optare per un tipo diverso di modello.

- **Riconoscimento audio e vocale**. I modelli in stile Whisper sono ancora modelli per il riconoscimento vocale a scopo generale utili, ma le scelte di produzione includono ora anche modelli più nuovi di speech-to-text come `gpt-4o-transcribe`, `gpt-4o-mini-transcribe` e varianti di diarizzazione. Valuta la copertura linguistica, la diarizzazione, il supporto in tempo reale, la latenza e il costo per il tuo scenario. Per saperne di più, consulta la [documentazione OpenAI speech-to-text](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst).

- **Generazione di immagini**. DALL-E e Midjourney sono opzioni ben note per la generazione di immagini, ma le attuali API di immagini OpenAI si concentrano su modelli GPT Image come `gpt-image-2`, mentre Stable Diffusion, Imagen, Flux e altre famiglie di modelli sono anche scelte comuni. Confronta aderenza al prompt, supporto per editing, controllo dello stile, requisiti di sicurezza e licenze. Scopri di più nella [guida OpenAI alla generazione di immagini](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) e nel Capitolo 9 di questo curriculum.

- **Generazione di testo**. I modelli testuali ora coprono modelli d'avanguardia, modelli di ragionamento, modelli più piccoli a bassa latenza e modelli open-weight. Esempi attuali includono modelli OpenAI GPT-5.x, modelli Anthropic Claude 4.x, modelli Google Gemini 3.x, modelli Meta Llama 4 e modelli Mistral. Non scegliere solo in base alla data di rilascio o al prezzo; confronta la qualità del compito, latenza, finestra contestuale, uso di strumenti, comportamento di sicurezza, disponibilità regionale e costo totale. Il [catalogo dei modelli Microsoft Foundry](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) è un buon posto per confrontare i modelli disponibili su Azure.

- **Multi-modalità**. Molti modelli attuali possono elaborare più del solo testo. Alcuni accettano input immagine, audio o video; alcuni possono richiamare strumenti; modelli specializzati possono generare immagini, audio o video. Ad esempio, i modelli OpenAI attuali supportano input testuali e immagini, i modelli Gemini possono supportare input di testo, codice, immagine, audio e video a seconda della variante, e Llama 4 Scout e Maverick sono modelli open-weight nativamente multimodali. Controlla sempre la scheda modello per le modalità di input e output supportate prima di costruire un flusso di lavoro attorno ad esso.

Selezionare un modello significa ottenere alcune capacità di base, che però potrebbero non essere sufficienti. Spesso si dispone di dati specifici dell'azienda di cui è necessario in qualche modo informare l’LLM. Ci sono diverse opzioni su come affrontare questo, di cui parleremo nelle prossime sezioni.

### Modelli Foundation versus LLM

Il termine Foundation Model è stato [coniato dai ricercatori di Stanford](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) e definito come un modello AI che segue alcuni criteri, come:

- **Sono addestrati usando l’apprendimento non supervisionato o auto-supervisionato**, il che significa che sono addestrati su dati multimodali non etichettati e non richiedono annotazioni o etichettature umane per il loro processo di addestramento.
- **Sono modelli molto grandi**, basati su reti neurali molto profonde addestrate su miliardi di parametri.
- **Sono normalmente destinati a servire come ‘fondazione’ per altri modelli**, il che significa che possono essere usati come punto di partenza per costruire altri modelli sovrapposti, tramite fine-tuning.

![Modelli Foundation versus LLM](../../../translated_images/it/FoundationModel.e4859dbb7a825c94.webp)

Fonte immagine: [Guida essenziale ai Modelli Foundation e ai Large Language Models | di Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Per chiarire ulteriormente questa distinzione, prendiamo ChatGPT come esempio storico. Le versioni iniziali di ChatGPT utilizzavano GPT-3.5 come modello foundation. OpenAI ha poi usato dati specifici per chat e tecniche di allineamento per creare una versione ottimizzata che aveva migliori prestazioni in scenari conversazionali come i chatbot. I servizi AI moderni spesso instradano tra varie varianti di modello, quindi il nome del servizio e del modello sottostante non corrispondono sempre.

![Modello Foundation](../../../translated_images/it/Multimodal.2c389c6439e0fc51.webp)

Fonte immagine: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Modelli Open-Weight/Open-Source versus Proprietari

Un altro modo per categorizzare gli LLM è se sono open-weight, open-source o proprietari.

I modelli open-source e open-weight rendono disponibili gli artefatti modello per ispezione, download o personalizzazione, ma le loro licenze variano. Alcuni sono pienamente open source, mentre altri sono modelli open-weight con restrizioni d'uso. Possono essere utili quando un'azienda necessita di più controllo su distribuzione, localizzazione dati, costo o personalizzazione. Tuttavia, i team devono comunque rivedere termini di licenza, costi di erogazione, manutenzione, aggiornamenti di sicurezza e qualità della valutazione prima di usarli in produzione. Esempi includono [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst), alcuni [modelli Mistral](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst) e molti modelli ospitati su [Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst).

I modelli proprietari sono di proprietà e ospitati da un fornitore. Questi modelli sono spesso ottimizzati per l'uso in produzione gestita e possono offrire supporto forte, sistemi di sicurezza, integrazione di strumenti e scalabilità. Tuttavia, i clienti di solito non possono ispezionare o modificare i pesi del modello e devono rivedere i termini del fornitore per privacy, conservazione, conformità e uso accettabile. Esempi includono [modelli OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), [Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst) e [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst).

### Embedding versus generazione di immagini versus generazione di testo e codice

Gli LLM possono anche essere categorizzati in base all'output che generano.

Gli embeddings sono un insieme di modelli che possono convertire il testo in una forma numerica, chiamata embedding, che è una rappresentazione numerica del testo di input. Gli embeddings facilitano la comprensione da parte delle macchine delle relazioni tra parole o frasi e possono essere usati come input da altri modelli, come modelli di classificazione o clustering che hanno migliori prestazioni su dati numerici. I modelli embedding sono spesso usati per il transfer learning, dove un modello è costruito per un compito surrogato per cui esiste abbondanza di dati, e poi i pesi del modello (embedding) sono riutilizzati per altri compiti downstream. Un esempio di questa categoria è [OpenAI embeddings](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Embedding](../../../translated_images/it/Embedding.c3708fe988ccf760.webp)

I modelli di generazione di immagini sono modelli che generano immagini. Questi modelli sono spesso usati per editing di immagini, sintesi di immagini e traduzione di immagini. I modelli di generazione di immagini sono spesso addestrati su grandi dataset di immagini, come [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), e possono essere usati per generare immagini nuove o per modificare immagini esistenti con tecniche di inpainting, super-risoluzione e colorazione. Esempi includono [modelli GPT Image](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst), [modelli Stable Diffusion](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst) e modelli Imagen.

![Generazione di immagini](../../../translated_images/it/Image.349c080266a763fd.webp)

I modelli di generazione di testo e codice sono modelli che generano testo o codice. Questi modelli sono spesso usati per sommari di testo, traduzioni e risposte a domande. I modelli di generazione di testo sono spesso addestrati su grandi dataset di testo, come [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), e possono generare testo nuovo o rispondere a domande. I modelli di generazione di codice, come [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), sono spesso addestrati su grandi dataset di codice, come GitHub, e possono generare codice nuovo o correggere bug in codice esistente.

![Generazione di testo e codice](../../../translated_images/it/Text.a8c0cf139e5cc2a0.webp)

### Encoder-Decoder versus solo Decoder

Per parlare dei diversi tipi di architetture degli LLM, usiamo un'analogia.

Immagina che il tuo responsabile ti abbia dato il compito di scrivere un quiz per gli studenti. Hai due colleghi; uno si occupa di creare i contenuti e l'altro di revisarli.

Il creatore di contenuti è come un modello solo decoder: può guardare l'argomento, vedere cosa hai già scritto, e poi continuare a generare contenuti basandosi su quel contesto. Sono molto bravi a scrivere contenuti coinvolgenti e informativi, ma non sono sempre la scelta migliore quando il compito è solo classificare, recuperare o codificare informazioni. Esempi di famiglie di modelli solo decoder includono GPT e Llama.

Il revisore è come un modello solo Encoder, guarda il corso scritto e le risposte, notando la relazione tra essi e comprendendo il contesto, ma non è bravo a generare contenuti. Un esempio di modello solo Encoder sarebbe BERT.

Immagina che possiamo anche avere qualcuno che possa creare e revisionare il quiz; questo è un modello Encoder-Decoder. Alcuni esempi sarebbero BART e T5.

### Servizio versus Modello

Ora, parliamo della differenza tra un servizio e un modello. Un servizio è un prodotto offerto da un Fornitore di Servizi Cloud, ed è spesso una combinazione di modelli, dati e altri componenti. Un modello è il componente centrale di un servizio, ed è spesso un modello foundation, come un LLM.

I servizi sono spesso ottimizzati per l'uso in produzione e sono spesso più facili da usare rispetto ai modelli, tramite un'interfaccia grafica. Tuttavia, i servizi non sono sempre disponibili gratuitamente e possono richiedere un abbonamento o un pagamento per l'uso, in cambio dell’uso dell’attrezzatura e delle risorse del proprietario del servizio, ottimizzando le spese e scalando facilmente. Un esempio di servizio è [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-foundry/openai/overview?WT.mc_id=academic-105485-koreyst), che offre un piano tariffario pay-as-you-go, il che significa che gli utenti sono addebitati proporzionalmente a quanto utilizzano il servizio. Azure OpenAI Service offre anche sicurezza di livello enterprise e un framework di AI responsabile integrato nelle capacità dei modelli.

I modelli sono gli artefatti della rete neurale: parametri, pesi, architettura, tokenizer e configurazione di supporto. Eseguire un modello localmente o in un ambiente privato richiede hardware adatto, infrastruttura di erogazione, monitoraggio, e una licenza open-source/open-weight compatibile o una licenza commerciale. I modelli open-weight come Llama 4 o i modelli Mistral possono essere ospitati autonomamente, ma richiedono comunque potenza di calcolo ed esperienza operativa.

## Come testare e iterare con diversi modelli per comprendere le prestazioni su Azure


Una volta che il nostro team ha esplorato l'attuale panorama degli LLM e identificato alcuni buoni candidati per i loro scenari, il passaggio successivo è testarli sui loro dati e sul loro carico di lavoro. Questo è un processo iterativo, effettuato tramite esperimenti e misurazioni.
La maggior parte dei modelli che abbiamo menzionato nei paragrafi precedenti (modelli OpenAI, modelli open-weight come Llama 4 e Mistral, e modelli Hugging Face) sono disponibili in [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst).

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst), in precedenza Azure AI Studio/Azure AI Foundry, è una piattaforma Azure unificata per costruire app e agenti AI. Aiuta gli sviluppatori a gestire il ciclo di vita dalla sperimentazione e valutazione al deployment, monitoraggio e governance. Il catalogo dei modelli in Microsoft Foundry consente all'utente di:

- Trovare il modello di base di interesse nel catalogo, inclusi modelli venduti da Azure e modelli di partner e fornitori della community. Gli utenti possono filtrare per task, fornitore, licenza, opzione di deployment o nome.

![Model catalog](../../../translated_images/it/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- Esaminare la scheda del modello, inclusa una descrizione dettagliata dell'uso previsto e dei dati di addestramento, esempi di codice e risultati di valutazione sulla libreria di valutazioni interne.

![Model card](../../../translated_images/it/ModelCard.598051692c6e400d.webp)

- Confrontare benchmark tra modelli e dataset disponibili nel settore per valutare quale soddisfa lo scenario aziendale, attraverso il pannello [Model Benchmarks](https://learn.microsoft.com/azure/ai-foundry/concepts/model-benchmarks?WT.mc_id=academic-105485-koreyst).

![Model benchmarks](../../../translated_images/it/ModelBenchmarks.254cb20fbd06c03a.webp)

- Effettuare il fine-tuning dei modelli supportati su dati di addestramento personalizzati per migliorare le prestazioni del modello in uno specifico carico di lavoro, sfruttando le capacità di sperimentazione e tracciamento di Microsoft Foundry.

![Model fine-tuning](../../../translated_images/it/FineTuning.aac48f07142e36fd.webp)

- Distribuire il modello pre-addestrato originale o la versione fine-tuned a un endpoint di inferenza remota in tempo reale, utilizzando opzioni di calcolo gestito o serverless, per permettere alle applicazioni di consumarlo.

![Model deployment](../../../translated_images/it/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> Non tutti i modelli nel catalogo sono attualmente disponibili per il fine-tuning e/o il deployment a consumo. Controlla la scheda del modello per dettagli sulle capacità e limitazioni del modello.

## Migliorare i risultati degli LLM

Abbiamo esplorato con il nostro team startup diversi tipi di LLM e una piattaforma cloud (Microsoft Foundry) che ci permette di confrontare diversi modelli, valutarli su dati di test, migliorare le prestazioni e distribuirli su endpoint di inferenza.

Ma quando dovrebbero considerare di effettuare il fine-tuning di un modello invece di usare uno pre-addestrato? Ci sono altri approcci per migliorare le prestazioni del modello su carichi di lavoro specifici?

Ci sono diversi approcci che un'azienda può utilizzare per ottenere i risultati desiderati da un LLM. Puoi selezionare diversi tipi di modelli con diversi gradi di addestramento quando distribuisci un LLM in produzione, con diversi livelli di complessità, costo e qualità. Ecco alcuni approcci diversi:

- **Prompt engineering con contesto**. L'idea è fornire sufficiente contesto quando si invia il prompt per assicurarsi di ottenere le risposte necessarie.

- **Retrieval Augmented Generation, RAG**. I tuoi dati potrebbero esistere in un database o endpoint web per esempio, per assicurarti che questi dati, o un loro sottoinsieme, siano inclusi al momento del prompt, puoi recuperare i dati rilevanti e farne parte del prompt dell'utente.

- **Modello fine-tuned**. Qui, hai addestrato ulteriormente il modello sui tuoi dati, il che porta il modello a essere più preciso e reattivo alle tue esigenze ma potrebbe essere costoso.

![LLMs deployment](../../../translated_images/it/Deploy.18b2d27412ec8c02.webp)

Fonte immagine: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Prompt Engineering con Contesto

Gli LLM pre-addestrati funzionano molto bene su task di linguaggio naturale generalizzati, anche semplicemente chiamandoli con un prompt breve, come una frase da completare o una domanda – il cosiddetto apprendimento “zero-shot”.

Tuttavia, più l'utente è in grado di inquadrare la propria query, con una richiesta dettagliata ed esempi – il Contesto – più la risposta sarà accurata e vicina alle aspettative dell'utente. In questo caso, si parla di apprendimento “one-shot” se il prompt include solo un esempio e di “few-shot learning” se ne include più di uno.
Il prompt engineering con contesto è l'approccio più conveniente da cui iniziare.

### Retrieval Augmented Generation (RAG)

Gli LLM hanno la limitazione di poter usare solo i dati usati durante il loro addestramento per generare una risposta. Questo significa che non sanno nulla sui fatti accaduti dopo il processo di addestramento e non possono accedere a informazioni non pubbliche (come dati aziendali).
Questo può essere superato tramite RAG, una tecnica che arricchisce il prompt con dati esterni sotto forma di pezzi di documenti, considerando i limiti di lunghezza del prompt. Questo è supportato da strumenti di database vettoriali (come [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) che recuperano i pezzi utili da varie fonti di dati predefinite e li aggiungono al Contesto del prompt.

Questa tecnica è molto utile quando un'azienda non ha abbastanza dati, tempo o risorse per effettuare il fine-tuning di un LLM, ma desidera comunque migliorare le prestazioni su un carico di lavoro specifico e ridurre i rischi di risposte allucinatorie, obsolete o non supportate.

### Modello fine-tuned

Il fine-tuning è un processo che sfrutta il transfer learning per “adattare” il modello a un task specifico o per risolvere un problema particolare. Diversamente dal few-shot learning e dal RAG, si ottiene un nuovo modello generato, con pesi e bias aggiornati. Richiede un insieme di esempi di addestramento costituiti da un singolo input (il prompt) e dalla relativa uscita associata (il completamento).
Questo sarebbe l'approccio preferito se:

- **Utilizzo di modelli più piccoli specifici per il task**. Un'azienda preferirebbe effettuare il fine-tuning di un modello più piccolo per un compito ristretto piuttosto che richiamare ripetutamente un modello più grande di frontiera, ottenendo una soluzione più economica e veloce.

- **Considerazione della latenza**. La latenza è importante per un caso d'uso specifico, quindi non è possibile usare prompt molto lunghi o il numero di esempi da cui il modello dovrebbe apprendere non si adatta al limite di lunghezza del prompt.

- **Adattamento di un comportamento stabile**. Un'azienda ha molti esempi di alta qualità e vuole che il modello segua costantemente uno schema di task, formato di output, tono o stile specifico del dominio. Se il problema principale sono fatti recenti o conoscenze private che cambiano spesso, usa RAG invece di affidarti solo al fine-tuning.

### Modello addestrato

Addestrare un LLM da zero è senza dubbio l'approccio più difficile e complesso da adottare, richiedendo enormi quantità di dati, risorse specializzate e potenza computazionale adeguata. Questa opzione dovrebbe essere considerata solo in uno scenario dove un'azienda ha un caso d'uso specifico di dominio e una grande quantità di dati centrati su quel dominio.

## Verifica della conoscenza

Quale potrebbe essere un buon approccio per migliorare i risultati di completamento di un LLM?

1. Prompt engineering con contesto
1. RAG
1. Modello fine-tuned

R: Tutti e tre possono aiutare. Inizia con il prompt engineering e il contesto per miglioramenti rapidi, e usa RAG quando il modello necessita di fatti attuali o dati aziendali privati. Scegli il fine-tuning quando hai abbastanza esempi di alta qualità e vuoi che il modello segua costantemente un task, formato, tono o schema di dominio.

## 🚀 Sfida

Approfondisci come puoi [usare RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) per la tua azienda.

## Ottimo lavoro, continua il tuo apprendimento

Dopo aver completato questa lezione, consulta la nostra [collezione di apprendimento sull'AI Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per continuare a migliorare le tue conoscenze sull'AI Generativa!

Vai alla Lezione 3 dove vedremo come [costruire con l'AI Generativa in modo responsabile](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->