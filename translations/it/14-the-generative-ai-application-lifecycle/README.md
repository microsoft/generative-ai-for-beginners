<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b9d32511b27373a1b21b5789d4fda057",
  "translation_date": "2025-10-17T16:10:36+00:00",
  "source_file": "14-the-generative-ai-application-lifecycle/README.md",
  "language_code": "it"
}
-->
[![Integrazione con chiamata di funzione](../../../translated_images/14-lesson-banner.066d74a31727ac121eeac06376a068a397d8e335281e63ce94130d11f516e46b.it.png)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Il ciclo di vita delle applicazioni di AI generativa

Una domanda importante per tutte le applicazioni di AI è la rilevanza delle funzionalità di AI, poiché l'AI è un campo in rapida evoluzione. Per garantire che la tua applicazione rimanga rilevante, affidabile e robusta, è necessario monitorarla, valutarla e migliorarla continuamente. Ed è qui che entra in gioco il ciclo di vita dell'AI generativa.

Il ciclo di vita dell'AI generativa è un framework che ti guida attraverso le fasi di sviluppo, distribuzione e manutenzione di un'applicazione di AI generativa. Ti aiuta a definire i tuoi obiettivi, misurare le prestazioni, identificare le sfide e implementare le soluzioni. Inoltre, ti consente di allineare la tua applicazione agli standard etici e legali del tuo settore e dei tuoi stakeholder. Seguendo il ciclo di vita dell'AI generativa, puoi garantire che la tua applicazione continui a fornire valore e soddisfare gli utenti.

## Introduzione

In questo capitolo, imparerai:

- A comprendere il cambiamento di paradigma da MLOps a LLMOps
- Il ciclo di vita degli LLM
- Strumenti per il ciclo di vita
- Metriche e valutazione del ciclo di vita

## Comprendere il cambiamento di paradigma da MLOps a LLMOps

Gli LLM sono un nuovo strumento nell'arsenale dell'Intelligenza Artificiale, estremamente potenti per compiti di analisi e generazione nelle applicazioni. Tuttavia, questa potenza comporta alcune conseguenze su come ottimizziamo le attività di AI e Machine Learning classico.

Per questo motivo, abbiamo bisogno di un nuovo paradigma per adattare questo strumento in modo dinamico, con gli incentivi corretti. Possiamo categorizzare le vecchie applicazioni di AI come "App ML" e le nuove applicazioni di AI come "App GenAI" o semplicemente "App AI", riflettendo la tecnologia e le tecniche principali utilizzate al momento. Questo cambia la nostra narrativa in diversi modi, guarda il seguente confronto.

![Confronto tra LLMOps e MLOps](../../../translated_images/01-llmops-shift.29bc933cb3bb0080a562e1655c0c719b71a72c3be6252d5c564b7f598987e602.it.png)

Nota che in LLMOps ci concentriamo maggiormente sugli sviluppatori di applicazioni, utilizzando le integrazioni come punto chiave, sfruttando "Modelli come Servizio" e considerando i seguenti punti per le metriche:

- Qualità: Qualità delle risposte
- Danno: AI responsabile
- Onestà: Fondamento delle risposte (Ha senso? È corretto?)
- Costo: Budget della soluzione
- Latenza: Tempo medio di risposta per token

## Il ciclo di vita degli LLM

Per prima cosa, per comprendere il ciclo di vita e le modifiche, osserviamo la seguente infografica.

![Infografica LLMOps](../../../translated_images/02-llmops.70a942ead05a7645db740f68727d90160cb438ab71f0fb20548bc7fe5cad83ff.it.png)

Come puoi notare, questo è diverso dai cicli di vita usuali di MLOps. Gli LLM hanno molte nuove esigenze, come il Prompting, tecniche diverse per migliorare la qualità (Fine-Tuning, RAG, Meta-Prompts), valutazioni e responsabilità con AI responsabile, e infine nuove metriche di valutazione (Qualità, Danno, Onestà, Costo e Latenza).

Ad esempio, osserva come ideiamo. Utilizzando l'ingegneria dei prompt per sperimentare con vari LLM e esplorare possibilità per testare se le loro ipotesi potrebbero essere corrette.

Nota che questo non è lineare, ma costituito da cicli integrati, iterativi e con un ciclo generale.

Come possiamo esplorare questi passaggi? Approfondiamo i dettagli su come costruire un ciclo di vita.

![Flusso di lavoro LLMOps](../../../translated_images/03-llm-stage-flows.3a1e1c401235a6cfa886ed6ba04aa52a096a545e1bc44fa54d7d5983a7201892.it.png)

Questo potrebbe sembrare un po' complicato, concentriamoci prima sui tre grandi passaggi.

1. Ideazione/Esplorazione: Esplorazione, qui possiamo esplorare in base alle esigenze aziendali. Prototipazione, creazione di un [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) e testare se è abbastanza efficiente per la nostra ipotesi.
2. Costruzione/Aumento: Implementazione, ora iniziamo a valutare per dataset più grandi, implementando tecniche come Fine-Tuning e RAG, per verificare la robustezza della nostra soluzione. Se non funziona, reimplementare, aggiungere nuovi passaggi nel nostro flusso o ristrutturare i dati potrebbe aiutare. Dopo aver testato il nostro flusso e la nostra scala, se funziona e verifica le nostre metriche, è pronto per il passaggio successivo.
3. Operativizzazione: Integrazione, ora aggiungendo sistemi di monitoraggio e avvisi al nostro sistema, distribuzione e integrazione dell'applicazione alla nostra applicazione.

Poi, abbiamo il ciclo generale di gestione, concentrandoci su sicurezza, conformità e governance.

Congratulazioni, ora la tua App AI è pronta per essere operativa. Per un'esperienza pratica, dai un'occhiata alla [Demo Contoso Chat.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

Ora, quali strumenti possiamo utilizzare?

## Strumenti per il ciclo di vita

Per gli strumenti, Microsoft offre la [Piattaforma Azure AI](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) e [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) per facilitare e rendere il tuo ciclo facile da implementare e pronto all'uso.

La [Piattaforma Azure AI](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) ti consente di utilizzare [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys). AI Studio è un portale web che ti permette di esplorare modelli, esempi e strumenti. Gestire le tue risorse, flussi di sviluppo UI e opzioni SDK/CLI per lo sviluppo orientato al codice.

![Possibilità di Azure AI](../../../translated_images/04-azure-ai-platform.80203baf03a12fa8b166e194928f057074843d1955177baf0f5b53d50d7b6153.it.png)

Azure AI ti consente di utilizzare molte risorse per gestire le tue operazioni, servizi, progetti, ricerca vettoriale e esigenze di database.

![LLMOps con Azure AI](../../../translated_images/05-llm-azure-ai-prompt.a5ce85cdbb494bdf95420668e3464aae70d8b22275a744254e941dd5e73ae0d2.it.png)

Costruisci, dal Proof-of-Concept (POC) fino ad applicazioni su larga scala con PromptFlow:

- Progetta e costruisci app da VS Code, con strumenti visivi e funzionali
- Testa e perfeziona le tue app per una AI di qualità, con facilità.
- Usa Azure AI Studio per integrare e iterare con il cloud, pubblica e distribuisci per una rapida integrazione.

![LLMOps con PromptFlow](../../../translated_images/06-llm-promptflow.a183eba07a3a7fdf4aa74db92a318b8cbbf4a608671f6b166216358d3203d8d4.it.png)

## Ottimo! Continua a imparare!

Fantastico, ora scopri di più su come strutturiamo un'applicazione per utilizzare i concetti con l'[App Contoso Chat](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), per vedere come Cloud Advocacy integra questi concetti nelle dimostrazioni. Per ulteriori contenuti, dai un'occhiata alla nostra [sessione breakout di Ignite!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Ora, consulta la Lezione 15 per comprendere come [Retrieval Augmented Generation e i database vettoriali](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) influenzano l'AI generativa e rendono le applicazioni più coinvolgenti!

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.