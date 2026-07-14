[![Integrazione con function calling](../../../translated_images/it/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Il Ciclo di Vita delle Applicazioni di Intelligenza Artificiale Generativa

Una domanda importante per tutte le applicazioni AI è la rilevanza delle funzionalità AI, poiché l'AI è un campo in rapida evoluzione; per garantire che la tua applicazione rimanga rilevante, affidabile e robusta, devi monitorarla, valutarla e migliorarla continuamente. Qui entra in gioco il ciclo di vita dell'AI generativa.

Il ciclo di vita dell'AI generativa è un framework che ti guida attraverso le fasi di sviluppo, distribuzione e manutenzione di un'applicazione AI generativa. Ti aiuta a definire i tuoi obiettivi, misurare le tue prestazioni, identificare le tue sfide e implementare le tue soluzioni. Ti aiuta anche ad allineare la tua applicazione agli standard etici e legali del tuo dominio e dei tuoi stakeholder. Seguendo il ciclo di vita dell'AI generativa, puoi assicurarti che la tua applicazione fornisca sempre valore e soddisfi i tuoi utenti.

## Introduzione

In questo capitolo, imparerai a:

- Comprendere il Cambiamento di Paradigma da MLOps a LLMOps
- Il Ciclo di Vita del LLM
- Strumenti per il Ciclo di Vita
- Metrificazione e Valutazione del Ciclo di Vita

## Comprendere il Cambiamento di Paradigma da MLOps a LLMOps

Gli LLM sono un nuovo strumento nell'arsenale dell'Intelligenza Artificiale, sono incredibilmente potenti nei compiti di analisi e generazione per le applicazioni, tuttavia questo potere ha alcune conseguenze su come semplifichiamo i compiti di AI e Machine Learning classico.

Per questo, abbiamo bisogno di un nuovo paradigma per adattare questo strumento in modo dinamico, con gli incentivi corretti. Possiamo categorizzare le vecchie app AI come "App ML" e le nuove app AI come "App GenAI" o semplicemente "App AI", riflettendo la tecnologia e le tecniche prevalenti del momento. Questo cambia la nostra narrativa in vari modi; guarda il seguente confronto.

![Confronto LLMOps vs. MLOps](../../../translated_images/it/01-llmops-shift.29bc933cb3bb0080.webp)

Nota che in LLMOps, ci concentriamo maggiormente sugli sviluppatori di app, usando le integrazioni come punto chiave, adottando "Modelli come Servizio" e considerando i seguenti punti per le metriche.

- Qualità: qualità della risposta
- Danno: AI responsabile
- Onestà: fondatezza della risposta (Ha senso? È corretta?)
- Costo: budget della soluzione
- Latenza: tempo medio di risposta del token

## Il Ciclo di Vita del LLM

Per prima cosa, per capire il ciclo di vita e le modifiche, osserviamo la seguente infografica.

![Infografica LLMOps](../../../translated_images/it/02-llmops.70a942ead05a7645.webp)

Come puoi notare, questo è diverso dai soliti cicli di vita di MLOps. Gli LLM hanno molte nuove esigenze, come il Prompting, diverse tecniche per migliorare la qualità (Fine-Tuning, RAG, Meta-Prompt), diverse modalità di valutazione e responsabilità con l'AI responsabile, infine nuove metriche di valutazione (Qualità, Danno, Onestà, Costo e Latenza).

Per esempio, osserva come ideiamo. Usando il prompt engineering per sperimentare con vari LLM esploriamo possibilità per testare se la loro ipotesi potrebbe essere corretta.

Nota che questo non è lineare, ma anelli integrati, iterativi e con un ciclo generale sovrastante.

Come potremmo esplorare questi passaggi? Esaminiamo in dettaglio come costruire un ciclo di vita.

![Flusso di lavoro LLMOps](../../../translated_images/it/03-llm-stage-flows.3a1e1c401235a6cf.webp)

Questo potrebbe sembrare un po' complicato, concentriamoci prima sui tre grandi passaggi.

1. Ideazione/Esplorazione: Esplorazione, qui possiamo esplorare in base alle esigenze aziendali. Prototipazione, creando un [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) e testando se è abbastanza efficiente per la nostra ipotesi.
1. Costruzione/Aumento: Implementazione, ora iniziamo a valutare per dataset più grandi e implementare tecniche come Fine-Tuning e RAG, per verificarne la robustezza. Se non funziona, reimplementarlo, aggiungere nuovi passaggi nel nostro flusso o ristrutturare i dati potrebbe aiutare. Dopo aver testato il nostro flusso e la sua scalabilità, se funziona e verifica le metriche, è pronto per il passaggio successivo.
1. Operazionalizzazione: Integrazione, ora aggiungendo sistemi di monitoraggio e allerta al nostro sistema, distribuzione e integrazione dell'applicazione con la nostra app.

Poi, abbiamo il ciclo generale di gestione, focalizzato su sicurezza, conformità e governance.

Congratulazioni, ora la tua app AI è pronta e operativa. Per un'esperienza pratica, dai un'occhiata alla [demo Contoso Chat.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)

Ora, quali strumenti potremmo usare?

## Strumenti per il Ciclo di Vita

Per gli strumenti, Microsoft fornisce la [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) e [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) per facilitare e semplificare l'implementazione del ciclo di vita.

La [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst), ti permette di usare [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst). Microsoft Foundry (ex Azure AI Studio) è un portale web che ti consente di esplorare modelli, esempi e strumenti, gestire le tue risorse e utilizzare flussi di sviluppo UI oltre a opzioni SDK/CLI per uno sviluppo Code-First.

![Possibilità di Azure AI](../../../translated_images/it/04-azure-ai-platform.80203baf03a12fa8.webp)

Azure AI ti permette di utilizzare molteplici risorse per gestire le tue operazioni, servizi, progetti, ricerche vettoriali e bisogni di database.

![LLMOps con Azure AI](../../../translated_images/it/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

Costruisci, dal Proof-of-Concept(POC) fino alle applicazioni su larga scala con PromptFlow:

- Progetta e costruisci app da VS Code, con strumenti visivi e funzionali
- Testa e affina le tue app per un'AI di qualità, con facilità.
- Usa Microsoft Foundry per integrare e iterare con il cloud, Push e Deploy per un'integrazione rapida.

![LLMOps con PromptFlow](../../../translated_images/it/06-llm-promptflow.a183eba07a3a7fdf.webp)

## Ottimo! Continua ad imparare!

Fantastico, ora impara di più su come strutturiamo un'applicazione per utilizzare i concetti con la [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), per vedere come Cloud Advocacy aggiunge questi concetti nelle dimostrazioni. Per più contenuti, guarda la nostra sessione breakout di [Ignite!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Ora, guarda la Lezione 15, per capire come [Retrieval Augmented Generation e Vector Databases](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) influenzano l'AI generativa e rendono le applicazioni più coinvolgenti!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->