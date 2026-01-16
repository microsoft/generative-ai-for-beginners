<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df44972d5575ea8cef3c52ee31696d04",
  "translation_date": "2025-12-19T14:41:33+00:00",
  "source_file": "14-the-generative-ai-application-lifecycle/README.md",
  "language_code": "it"
}
-->
[![Integrazione con chiamata di funzione](../../../translated_images/it/14-lesson-banner.066d74a31727ac12.png)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Il Ciclo di Vita delle Applicazioni di AI Generativa

Una domanda importante per tutte le applicazioni di AI è la rilevanza delle funzionalità AI, poiché l'AI è un campo in rapida evoluzione, per garantire che la tua applicazione rimanga rilevante, affidabile e robusta, devi monitorarla, valutarla e migliorarla continuamente. Qui entra in gioco il ciclo di vita dell'AI generativa.

Il ciclo di vita dell'AI generativa è un framework che ti guida attraverso le fasi di sviluppo, distribuzione e manutenzione di un'applicazione di AI generativa. Ti aiuta a definire i tuoi obiettivi, misurare le tue prestazioni, identificare le tue sfide e implementare le tue soluzioni. Ti aiuta anche ad allineare la tua applicazione con gli standard etici e legali del tuo dominio e dei tuoi stakeholder. Seguendo il ciclo di vita dell'AI generativa, puoi assicurarti che la tua applicazione fornisca sempre valore e soddisfi i tuoi utenti.

## Introduzione

In questo capitolo, imparerai a:

- Comprendere il Cambiamento di Paradigma da MLOps a LLMOps
- Il Ciclo di Vita degli LLM
- Strumenti per il Ciclo di Vita
- Metrificazione e Valutazione del Ciclo di Vita

## Comprendere il Cambiamento di Paradigma da MLOps a LLMOps

Gli LLM sono un nuovo strumento nell'arsenale dell'Intelligenza Artificiale, sono incredibilmente potenti nelle attività di analisi e generazione per le applicazioni, tuttavia questo potere ha alcune conseguenze su come semplifichiamo i compiti di AI e Machine Learning Classico.

Con questo, abbiamo bisogno di un nuovo Paradigma per adattare questo strumento in modo dinamico, con gli incentivi corretti. Possiamo categorizzare le vecchie app AI come "App ML" e le nuove app AI come "App GenAI" o semplicemente "App AI", riflettendo la tecnologia e le tecniche mainstream usate al momento. Questo cambia la nostra narrazione in diversi modi, guarda il confronto seguente.

![Confronto LLMOps vs. MLOps](../../../translated_images/it/01-llmops-shift.29bc933cb3bb0080.png)

Nota che in LLMOps, ci concentriamo maggiormente sugli Sviluppatori di App, usando le integrazioni come punto chiave, utilizzando "Modelli come Servizio" e pensando ai seguenti punti per le metriche.

- Qualità: Qualità della risposta
- Danno: AI Responsabile
- Onestà: Fondamento della risposta (Ha senso? È corretto?)
- Costo: Budget della soluzione
- Latenza: Tempo medio per la risposta del token

## Il Ciclo di Vita degli LLM

Per prima cosa, per comprendere il ciclo di vita e le modifiche, osserviamo l'infografica seguente.

![Infografica LLMOps](../../../translated_images/it/02-llmops.70a942ead05a7645.png)

Come puoi notare, questo è diverso dai soliti cicli di vita di MLOps. Gli LLM hanno molti nuovi requisiti, come il Prompting, diverse tecniche per migliorare la qualità (Fine-Tuning, RAG, Meta-Prompts), diverse valutazioni e responsabilità con l'AI responsabile, infine, nuove metriche di valutazione (Qualità, Danno, Onestà, Costo e Latenza).

Ad esempio, guarda come ideiamo. Usando l'ingegneria dei prompt per sperimentare con vari LLM per esplorare possibilità e testare se la loro ipotesi potrebbe essere corretta.

Nota che questo non è lineare, ma cicli integrati, iterativi e con un ciclo generale.

Come potremmo esplorare questi passaggi? Entriamo nel dettaglio di come potremmo costruire un ciclo di vita.

![Flusso di lavoro LLMOps](../../../translated_images/it/03-llm-stage-flows.3a1e1c401235a6cf.png)

Questo può sembrare un po' complicato, concentriamoci prima sui tre grandi passaggi.

1. Ideazione/Esplorazione: Esplorazione, qui possiamo esplorare in base alle nostre esigenze di business. Prototipazione, creazione di un [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) e testare se è abbastanza efficiente per la nostra ipotesi.
1. Costruzione/Aumento: Implementazione, ora iniziamo a valutare per dataset più grandi, implementare tecniche come Fine-tuning e RAG, per verificare la robustezza della nostra soluzione. Se non funziona, reimplementarla, aggiungere nuovi passaggi nel nostro flusso o ristrutturare i dati potrebbe aiutare. Dopo aver testato il nostro flusso e la nostra scala, se funziona e controlla le nostre metriche, è pronto per il passo successivo.
1. Operazionalizzazione: Integrazione, ora aggiungendo sistemi di monitoraggio e allerta al nostro sistema, distribuzione e integrazione dell'applicazione nella nostra applicazione.

Poi, abbiamo il ciclo generale di Gestione, concentrandoci su sicurezza, conformità e governance.

Congratulazioni, ora la tua app AI è pronta e operativa. Per un'esperienza pratica, dai un'occhiata alla [Demo Contoso Chat.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

Ora, quali strumenti potremmo usare?

## Strumenti per il Ciclo di Vita

Per gli strumenti, Microsoft fornisce la [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) e [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) che facilitano e rendono facile implementare il tuo ciclo e pronti all'uso.

La [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys), ti permette di usare [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys). AI Studio è un portale web che ti permette di esplorare modelli, esempi e strumenti. Gestire le tue risorse, flussi di sviluppo UI e opzioni SDK/CLI per uno sviluppo Code-First.

![Possibilità di Azure AI](../../../translated_images/it/04-azure-ai-platform.80203baf03a12fa8.png)

Azure AI ti permette di usare molteplici risorse, per gestire le tue operazioni, servizi, progetti, ricerca vettoriale e necessità di database.

![LLMOps con Azure AI](../../../translated_images/it/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.png)

Costruisci, dal Proof-of-Concept (POC) fino ad applicazioni su larga scala con PromptFlow:

- Progetta e costruisci app da VS Code, con strumenti visivi e funzionali
- Testa e affina le tue app per un'AI di qualità, con facilità.
- Usa Azure AI Studio per integrare e iterare con il cloud, Push e Deploy per un'integrazione rapida.

![LLMOps con PromptFlow](../../../translated_images/it/06-llm-promptflow.a183eba07a3a7fdf.png)

## Ottimo! Continua il tuo apprendimento!

Fantastico, ora impara di più su come strutturiamo un'applicazione per usare i concetti con la [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), per vedere come Cloud Advocacy aggiunge questi concetti nelle dimostrazioni. Per più contenuti, guarda la nostra [sessione breakout di Ignite!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Ora, guarda la Lezione 15, per capire come [Retrieval Augmented Generation e Database Vettoriali](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) impattano l'AI Generativa e per creare applicazioni più coinvolgenti!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->