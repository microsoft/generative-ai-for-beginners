[![Integrarea cu apelarea funcțiilor](../../../translated_images/ro/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Ciclu de viață al aplicației AI generative

O întrebare importantă pentru toate aplicațiile AI este relevanța caracteristicilor AI, deoarece AI este un domeniu în rapidă evoluție, pentru a asigura că aplicația dvs. rămâne relevantă, de încredere și robustă, trebuie să o monitorizați, evaluați și îmbunătățiți continuu. Aici intervine ciclul de viață al AI generative.

Ciclul de viață al AI generative este un cadru care vă ghidează prin etapele de dezvoltare, implementare și întreținere a unei aplicații AI generative. Acesta vă ajută să vă definiți obiectivele, să vă măsurați performanța, să identificați provocările și să implementați soluțiile. De asemenea, vă ajută să vă aliniați aplicația la standardele etice și legale ale domeniului și ale părților interesate. Urmând ciclul de viață al AI generative, puteți asigura că aplicația dvs. oferă întotdeauna valoare și satisface utilizatorii.

## Introducere

În acest capitol, veți:

- Înțelegeți schimbarea de paradigmă de la MLOps la LLMOps
- Ciclul de viață al LLM-urilor
- Instrumente pentru ciclul de viață
- Metrificarea și evaluarea ciclului de viață

## Înțelegeți schimbarea de paradigmă de la MLOps la LLMOps

LLM-urile sunt un instrument nou în arsenalul Inteligenței Artificiale, sunt extrem de puternice în sarcini de analiză și generare pentru aplicații, totuși această putere are unele consecințe asupra modului în care eficientizăm sarcinile AI și Machine Learning Clasic.

Cu asta, avem nevoie de o nouă paradigmă pentru a adapta acest instrument într-un mod dinamic, cu stimulente corecte. Putem clasifica aplicațiile AI mai vechi ca „Aplicații ML” și aplicațiile AI mai noi ca „Aplicații GenAI” sau pur și simplu „Aplicații AI”, reflectând tehnologia și tehnicile principale folosite la momentul respectiv. Aceasta schimbă narațiunea noastră în mai multe moduri, priviți comparația următoare.

![Comparație LLMOps vs. MLOps](../../../translated_images/ro/01-llmops-shift.29bc933cb3bb0080.webp)

Observați că în LLMOps, ne concentrăm mai mult pe Dezvoltatorii Aplicațiilor, folosind integrările ca punct cheie, utilizând „Modele-ca-Serviciu” și gândind la următorii indicatori pentru metrici.

- Calitate: Calitatea răspunsului
- Daună: AI responsabilă
- Onestitate: Fundamentarea răspunsului (Are sens? Este corect?)
- Cost: Bugetul soluției
- Latență: Timp mediu pentru răspunsul cu tokeni

## Ciclul de viață al LLM-urilor

Mai întâi, pentru a înțelege ciclul de viață și modificările, să notăm următorul infografic.

![Infografic LLMOps](../../../translated_images/ro/02-llmops.70a942ead05a7645.webp)

După cum puteți observa, acesta este diferit de ciclurile obișnuite din MLOps. LLM-urile au multe cerințe noi, cum ar fi promptarea, tehnici diferite pentru îmbunătățirea calității (fine-tuning, RAG, meta-prompturi), evaluare diferită și responsabilitate cu AI responsabilă, în final, metrici noi de evaluare (calitate, daună, onestitate, cost și latență).

De exemplu, aruncați o privire asupra modului în care generăm idei. Folosind ingineria prompturilor pentru a experimenta cu diverse LLM-uri pentru a explora posibilități de a testa dacă ipoteza noastră ar putea fi corectă.

Rețineți că aceasta nu este liniară, ci bucle integrate, iterative și cu un ciclu general de supraveghere.

Cum am putea explora acești pași? Să intrăm în detaliu despre cum am putea construi un ciclu de viață.

![Flux de lucru LLMOps](../../../translated_images/ro/03-llm-stage-flows.3a1e1c401235a6cf.webp)

Aceasta poate părea puțin complicat, să ne concentrăm mai întâi pe cele trei pași mari.

1. Ideare/Explorare: Explorare, aici putem explora conform nevoilor noastre de afaceri. Prototipare, crearea unui [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) și testarea dacă este suficient de eficient pentru ipoteza noastră.
1. Construire/Extindere: Implementare, acum, începem să evaluăm pentru seturi de date mai mari, implementăm tehnici, precum fine-tuning și RAG, pentru a verifica robustețea soluției. Dacă nu funcționează, re-implementarea, adăugarea de noi pași în fluxul nostru sau restructurarea datelor poate ajuta. După testarea fluxului nostru și scalarea lui, dacă funcționează și metricile noastre sunt confirmate, este gata pentru pasul următor.
1. Operaționalizare: Integrare, acum adăugăm sistemele de monitorizare și alerte în sistemul nostru, implementarea și integrarea aplicației în aplicația noastră.

Apoi, avem ciclul general de management, axat pe securitate, conformitate și guvernanță.

Felicitări, acum aveți aplicația AI gata de utilizare și operațională. Pentru o experiență practică, aruncați o privire la [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)

Acum, ce instrumente am putea folosi?

## Instrumente pentru ciclul de viață

Pentru instrumente, Microsoft oferă [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) și [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) care facilitează și face ciclul dumneavoastră ușor de implementat și gata de utilizare.

[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) vă permite să folosiți [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst). Microsoft Foundry (fost Azure AI Studio) este un portal web care vă permite să explorați modele, mostre și instrumente, să vă gestionați resursele și să folosiți fluxuri de dezvoltare UI, precum și opțiuni SDK/CLI pentru dezvoltare Code-First.

![Posibilități Azure AI](../../../translated_images/ro/04-azure-ai-platform.80203baf03a12fa8.webp)

Azure AI vă permite să utilizați multiple resurse pentru a vă gestiona operațiunile, serviciile, proiectele, căutările vectoriale și nevoile de baze de date.

![LLMOps cu Azure AI](../../../translated_images/ro/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

Construiți, de la dovada de concept (POC) până la aplicații la scară largă cu PromptFlow:

- Proiectați și construiți aplicații din VS Code, cu instrumente vizuale și funcționale
- Testați și adaptați aplicațiile pentru AI de calitate, cu ușurință.
- Folosiți Microsoft Foundry pentru integrare și iterație cu cloud-ul, Push și Deploy pentru integrare rapidă.

![LLMOps cu PromptFlow](../../../translated_images/ro/06-llm-promptflow.a183eba07a3a7fdf.webp)

## Minunat! Continuați să învățați!

Minunat, acum învățați mai multe despre cum structurăm o aplicație pentru a folosi conceptele cu [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), pentru a vedea cum Cloud Advocacy adaugă aceste concepte în demonstrații. Pentru mai mult conținut, verificați sesiunea noastră breakout Ignite!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Acum, verificați Lecția 15, pentru a înțelege cum [Retrieval Augmented Generation and Vector Databases](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) influențează AI generativ și pentru a face aplicații mai captivante!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->