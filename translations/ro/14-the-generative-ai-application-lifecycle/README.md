<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df44972d5575ea8cef3c52ee31696d04",
  "translation_date": "2025-12-19T16:59:34+00:00",
  "source_file": "14-the-generative-ai-application-lifecycle/README.md",
  "language_code": "ro"
}
-->
[![Integrating with function calling](../../../translated_images/14-lesson-banner.066d74a31727ac12.ro.png)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Ciclu de viață al aplicațiilor AI generative

O întrebare importantă pentru toate aplicațiile AI este relevanța caracteristicilor AI, deoarece AI este un domeniu în continuă evoluție rapidă, pentru a asigura că aplicația dvs. rămâne relevantă, fiabilă și robustă, trebuie să o monitorizați, evaluați și îmbunătățiți continuu. Aici intervine ciclul de viață al AI generative.

Ciclul de viață al AI generative este un cadru care vă ghidează prin etapele dezvoltării, implementării și întreținerii unei aplicații AI generative. Vă ajută să vă definiți obiectivele, să vă măsurați performanța, să identificați provocările și să implementați soluțiile. De asemenea, vă ajută să aliniați aplicația cu standardele etice și legale ale domeniului și ale părților interesate. Urmând ciclul de viață al AI generative, puteți asigura că aplicația dvs. oferă întotdeauna valoare și satisface utilizatorii.

## Introducere

În acest capitol, veți:

- Înțelege schimbarea de paradigmă de la MLOps la LLMOps
- Ciclu de viață LLM
- Unelte pentru ciclul de viață
- Metrificarea și evaluarea ciclului de viață

## Înțelege schimbarea de paradigmă de la MLOps la LLMOps

LLM-urile sunt un nou instrument în arsenalul Inteligenței Artificiale, sunt incredibil de puternice în sarcini de analiză și generare pentru aplicații, însă această putere are unele consecințe în modul în care optimizăm sarcinile AI și Machine Learning Clasic.

În acest sens, avem nevoie de o nouă paradigmă pentru a adapta acest instrument într-un mod dinamic, cu stimulente corecte. Putem categorisi aplicațiile AI mai vechi ca „Aplicații ML” și aplicațiile AI mai noi ca „Aplicații GenAI” sau pur și simplu „Aplicații AI”, reflectând tehnologia și tehnicile mainstream folosite la momentul respectiv. Aceasta schimbă narațiunea noastră în mai multe moduri, priviți comparația următoare.

![LLMOps vs. MLOps comparison](../../../translated_images/01-llmops-shift.29bc933cb3bb0080.ro.png)

Observați că în LLMOps, ne concentrăm mai mult pe dezvoltatorii de aplicații, folosind integrări ca punct cheie, utilizând „Modele ca Serviciu” și gândind în următorii termeni pentru metrici.

- Calitate: Calitatea răspunsului
- Rău: AI responsabil
- Onestitate: Fundamentarea răspunsului (Are sens? Este corect?)
- Cost: Bugetul soluției
- Latență: Timp mediu pentru răspunsul tokenului

## Ciclu de viață LLM

Mai întâi, pentru a înțelege ciclul de viață și modificările, să observăm următoarea infografică.

![LLMOps infographic](../../../translated_images/02-llmops.70a942ead05a7645.ro.png)

După cum observați, acesta este diferit de ciclurile obișnuite din MLOps. LLM-urile au multe cerințe noi, cum ar fi Prompting, tehnici diferite pentru îmbunătățirea calității (Fine-Tuning, RAG, Meta-Prompts), evaluare și responsabilitate diferită cu AI responsabil, în final, metrici noi de evaluare (Calitate, Rău, Onestitate, Cost și Latență).

De exemplu, uitați-vă cum ideăm. Folosind ingineria prompturilor pentru a experimenta cu diverse LLM-uri pentru a explora posibilități și a testa dacă ipoteza lor ar putea fi corectă.

Observați că acest proces nu este liniar, ci bucle integrate, iterative și cu un ciclu general.

Cum am putea explora acești pași? Să intrăm în detaliu despre cum am putea construi un ciclu de viață.

![LLMOps Workflow](../../../translated_images/03-llm-stage-flows.3a1e1c401235a6cf.ro.png)

Acesta poate părea puțin complicat, să ne concentrăm mai întâi pe cei trei pași mari.

1. Ideare/Explorare: Explorare, aici putem explora conform nevoilor noastre de afaceri. Prototipare, crearea unui [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) și testarea dacă este suficient de eficient pentru ipoteza noastră.
1. Construire/Augmentare: Implementare, acum începem să evaluăm pentru seturi de date mai mari, implementăm tehnici, cum ar fi Fine-tuning și RAG, pentru a verifica robustețea soluției noastre. Dacă nu funcționează, reimplementarea, adăugarea de noi pași în fluxul nostru sau restructurarea datelor ar putea ajuta. După testarea fluxului și a scalabilității, dacă funcționează și verificăm metricile, este gata pentru pasul următor.
1. Operaționalizare: Integrare, acum adăugăm sisteme de monitorizare și alerte în sistemul nostru, implementare și integrare a aplicației în aplicația noastră.

Apoi, avem ciclul general de management, concentrat pe securitate, conformitate și guvernanță.

Felicitări, acum aveți aplicația AI gata de utilizare și operațională. Pentru o experiență practică, aruncați o privire la [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

Acum, ce unelte am putea folosi?

## Unelte pentru ciclul de viață

Pentru unelte, Microsoft oferă [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) și [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) care facilitează și fac ciclul dvs. ușor de implementat și gata de utilizare.

[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) vă permite să folosiți [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys). AI Studio este un portal web care vă permite să explorați modele, exemple și unelte. Gestionați resursele, fluxurile de dezvoltare UI și opțiunile SDK/CLI pentru dezvoltare Code-First.

![Azure AI possibilities](../../../translated_images/04-azure-ai-platform.80203baf03a12fa8.ro.png)

Azure AI vă permite să folosiți multiple resurse pentru a gestiona operațiunile, serviciile, proiectele, căutarea vectorială și nevoile de baze de date.

![LLMOps with Azure AI](../../../translated_images/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.ro.png)

Construiți, de la Proof-of-Concept (POC) până la aplicații la scară largă cu PromptFlow:

- Proiectați și construiți aplicații din VS Code, cu unelte vizuale și funcționale
- Testați și ajustați aplicațiile pentru AI de calitate, cu ușurință.
- Folosiți Azure AI Studio pentru a integra și itera cu cloud, împingeți și implementați pentru integrare rapidă.

![LLMOps with PromptFlow](../../../translated_images/06-llm-promptflow.a183eba07a3a7fdf.ro.png)

## Grozav! Continuați să învățați!

Minunat, acum învățați mai multe despre cum structurăm o aplicație pentru a folosi conceptele cu [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), pentru a vedea cum Cloud Advocacy adaugă aceste concepte în demonstrații. Pentru mai mult conținut, verificați sesiunea noastră de la [Ignite breakout!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Acum, verificați Lecția 15, pentru a înțelege cum [Retrieval Augmented Generation și bazele de date vectoriale](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) impactează AI generativ și pentru a crea aplicații mai captivante!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->