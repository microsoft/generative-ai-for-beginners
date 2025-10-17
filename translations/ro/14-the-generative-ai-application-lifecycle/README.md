<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b9d32511b27373a1b21b5789d4fda057",
  "translation_date": "2025-10-17T22:09:24+00:00",
  "source_file": "14-the-generative-ai-application-lifecycle/README.md",
  "language_code": "ro"
}
-->
[![Integrarea cu apelarea funcțiilor](../../../translated_images/14-lesson-banner.066d74a31727ac121eeac06376a068a397d8e335281e63ce94130d11f516e46b.ro.png)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Ciclu de viață al aplicațiilor AI generative

O întrebare importantă pentru toate aplicațiile AI este relevanța funcțiilor AI, deoarece domeniul AI evoluează rapid. Pentru a asigura că aplicația ta rămâne relevantă, fiabilă și robustă, trebuie să o monitorizezi, evaluezi și îmbunătățești continuu. Aici intervine ciclul de viață al AI generative.

Ciclul de viață al AI generative este un cadru care te ghidează prin etapele de dezvoltare, implementare și întreținere a unei aplicații AI generative. Te ajută să îți definești obiectivele, să îți măsori performanța, să identifici provocările și să implementezi soluțiile. De asemenea, te ajută să aliniezi aplicația la standardele etice și legale ale domeniului tău și ale părților interesate. Urmând ciclul de viață al AI generative, poți asigura că aplicația ta oferă mereu valoare și satisface utilizatorii.

## Introducere

În acest capitol, vei:

- Înțelege schimbarea de paradigmă de la MLOps la LLMOps
- Ciclul de viață al LLM
- Instrumente pentru ciclul de viață
- Metodologia și evaluarea ciclului de viață

## Înțelege schimbarea de paradigmă de la MLOps la LLMOps

LLM-urile sunt un nou instrument în arsenalul Inteligenței Artificiale, fiind extrem de puternice în sarcinile de analiză și generare pentru aplicații. Totuși, această putere are consecințe asupra modului în care optimizăm sarcinile AI și de învățare automată clasică.

Astfel, avem nevoie de o nouă paradigmă pentru a adapta acest instrument într-un mod dinamic, cu stimulentele corecte. Putem categoriza aplicațiile AI mai vechi drept "Aplicații ML" și aplicațiile AI mai noi drept "Aplicații GenAI" sau pur și simplu "Aplicații AI", reflectând tehnologia și tehnicile predominante ale momentului. Această schimbare ne influențează în mai multe moduri, după cum se poate observa în comparația de mai jos.

![Comparație LLMOps vs. MLOps](../../../translated_images/01-llmops-shift.29bc933cb3bb0080a562e1655c0c719b71a72c3be6252d5c564b7f598987e602.ro.png)

Observă că în LLMOps ne concentrăm mai mult pe dezvoltatorii de aplicații, folosind integrarea ca punct cheie, utilizând "Modele-ca-Serviciu" și luând în considerare următoarele puncte pentru metrici:

- Calitate: Calitatea răspunsului
- Daune: AI responsabil
- Onestitate: Fundamentarea răspunsului (Are sens? Este corect?)
- Cost: Bugetul soluției
- Latență: Timpul mediu pentru răspunsul token

## Ciclul de viață al LLM

Pentru început, pentru a înțelege ciclul de viață și modificările, să analizăm următorul infografic.

![Infografic LLMOps](../../../translated_images/02-llmops.70a942ead05a7645db740f68727d90160cb438ab71f0fb20548bc7fe5cad83ff.ro.png)

După cum se poate observa, acesta este diferit de ciclurile de viață obișnuite din MLOps. LLM-urile au multe cerințe noi, cum ar fi Prompting, tehnici diferite pentru îmbunătățirea calității (Fine-Tuning, RAG, Meta-Prompts), evaluări diferite și responsabilitate cu AI responsabil, și, în final, noi metrici de evaluare (Calitate, Daune, Onestitate, Cost și Latență).

De exemplu, să analizăm cum ideăm. Folosim ingineria de prompturi pentru a experimenta cu diverse LLM-uri, explorând posibilități pentru a testa dacă ipoteza lor ar putea fi corectă.

Observă că acest proces nu este liniar, ci constă în bucle integrate, iterative și cu un ciclu general.

Cum putem explora acești pași? Să intrăm în detalii despre cum putem construi un ciclu de viață.

![Flux de lucru LLMOps](../../../translated_images/03-llm-stage-flows.3a1e1c401235a6cfa886ed6ba04aa52a096a545e1bc44fa54d7d5983a7201892.ro.png)

Acest lucru poate părea puțin complicat, așa că să ne concentrăm mai întâi pe cele trei etape principale.

1. Ideare/Explorare: Explorare, aici putem explora în funcție de nevoile noastre de afaceri. Prototipare, crearea unui [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) și testarea eficienței ipotezei noastre.
2. Construire/Îmbunătățire: Implementare, acum începem să evaluăm seturi de date mai mari, să implementăm tehnici precum Fine-tuning și RAG pentru a verifica robustețea soluției noastre. Dacă nu funcționează, reimplementarea, adăugarea de noi pași în fluxul nostru sau restructurarea datelor ar putea ajuta. După testarea fluxului și a scalabilității, dacă funcționează și metricile sunt verificate, este gata pentru pasul următor.
3. Operaționalizare: Integrare, acum adăugăm sisteme de monitorizare și alerte, implementare și integrare a aplicației în sistemul nostru.

Apoi, avem ciclul general de Management, concentrându-ne pe securitate, conformitate și guvernanță.

Felicitări, acum aplicația ta AI este gata de utilizare și operațională. Pentru o experiență practică, aruncă o privire la [Demo-ul Contoso Chat.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

Acum, ce instrumente putem folosi?

## Instrumente pentru ciclul de viață

Pentru instrumente, Microsoft oferă [Platforma Azure AI](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) și [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) pentru a facilita și a face ciclul ușor de implementat și gata de utilizare.

[Platforma Azure AI](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) îți permite să folosești [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys). AI Studio este un portal web care îți permite să explorezi modele, exemple și instrumente. Gestionarea resurselor, fluxurile de dezvoltare UI și opțiunile SDK/CLI pentru dezvoltarea orientată pe cod.

![Posibilități Azure AI](../../../translated_images/04-azure-ai-platform.80203baf03a12fa8b166e194928f057074843d1955177baf0f5b53d50d7b6153.ro.png)

Azure AI îți permite să folosești multiple resurse pentru a gestiona operațiunile, serviciile, proiectele, căutările vectoriale și nevoile de baze de date.

![LLMOps cu Azure AI](../../../translated_images/05-llm-azure-ai-prompt.a5ce85cdbb494bdf95420668e3464aae70d8b22275a744254e941dd5e73ae0d2.ro.png)

Construiește, de la conceptul inițial (POC) până la aplicații la scară largă, cu PromptFlow:

- Proiectează și construiește aplicații din VS Code, cu instrumente vizuale și funcționale
- Testează și ajustează aplicațiile pentru AI de calitate, cu ușurință.
- Folosește Azure AI Studio pentru a integra și itera cu cloud-ul, pentru implementare rapidă.

![LLMOps cu PromptFlow](../../../translated_images/06-llm-promptflow.a183eba07a3a7fdf4aa74db92a318b8cbbf4a608671f6b166216358d3203d8d4.ro.png)

## Grozav! Continuă să înveți!

Minunat, acum află mai multe despre cum structurăm o aplicație pentru a folosi conceptele cu [Aplicația Contoso Chat](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), pentru a vedea cum Advocacy Cloud adaugă aceste concepte în demonstrații. Pentru mai mult conținut, verifică [sesiunea noastră de la Ignite!](https://www.youtube.com/watch?v=DdOylyrTOWg)

Acum, verifică Lecția 15, pentru a înțelege cum [Generarea Augmentată prin Recuperare și Bazele de Date Vectoriale](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) influențează AI generativă și pentru a crea aplicații mai captivante!

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.