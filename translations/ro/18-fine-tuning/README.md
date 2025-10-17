<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "807f0d9fc1747e796433534e1be6a98a",
  "translation_date": "2025-10-17T22:09:40+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "ro"
}
-->
[![Modele Open Source](../../../translated_images/18-lesson-banner.f30176815b1a5074fce9cceba317720586caa99e24001231a92fd04eeb54a121.ro.png)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Ajustarea fină a modelului LLM

Utilizarea modelelor lingvistice mari pentru a construi aplicații de AI generativ vine cu noi provocări. O problemă cheie este asigurarea calității răspunsurilor (precizie și relevanță) în conținutul generat de model pentru o cerere specifică a utilizatorului. În lecțiile anterioare, am discutat despre tehnici precum ingineria prompturilor și generarea augmentată prin recuperare, care încearcă să rezolve problema prin _modificarea intrării promptului_ în modelul existent.

În lecția de astăzi, discutăm despre o a treia tehnică, **ajustarea fină**, care încearcă să abordeze provocarea prin _reantrenarea modelului însuși_ cu date suplimentare. Să intrăm în detalii.

## Obiective de învățare

Această lecție introduce conceptul de ajustare fină pentru modelele lingvistice pre-antrenate, explorează beneficiile și provocările acestei abordări și oferă îndrumări despre când și cum să folosiți ajustarea fină pentru a îmbunătăți performanța modelelor voastre de AI generativ.

Până la sfârșitul acestei lecții, ar trebui să puteți răspunde la următoarele întrebări:

- Ce este ajustarea fină pentru modelele lingvistice?
- Când și de ce este utilă ajustarea fină?
- Cum pot ajusta fin un model pre-antrenat?
- Care sunt limitările ajustării fine?

Gata? Să începem.

## Ghid ilustrat

Doriți să aveți o imagine de ansamblu a ceea ce vom acoperi înainte de a intra în detalii? Consultați acest ghid ilustrat care descrie parcursul de învățare pentru această lecție - de la învățarea conceptelor de bază și motivația pentru ajustarea fină, până la înțelegerea procesului și a celor mai bune practici pentru executarea sarcinii de ajustare fină. Este un subiect fascinant de explorat, așa că nu uitați să verificați pagina [Resurse](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) pentru linkuri suplimentare care să vă sprijine parcursul de învățare autodidact!

![Ghid ilustrat pentru ajustarea fină a modelelor lingvistice](../../../translated_images/18-fine-tuning-sketchnote.11b21f9ec8a703467a120cb79a28b5ac1effc8d8d9d5b31bbbac6b8640432e14.ro.png)

## Ce este ajustarea fină pentru modelele lingvistice?

Prin definiție, modelele lingvistice mari sunt _pre-antrenate_ pe cantități mari de text provenit din surse diverse, inclusiv internetul. Așa cum am învățat în lecțiile anterioare, avem nevoie de tehnici precum _ingineria prompturilor_ și _generarea augmentată prin recuperare_ pentru a îmbunătăți calitatea răspunsurilor modelului la întrebările utilizatorului ("prompturi").

O tehnică populară de inginerie a prompturilor implică oferirea modelului mai multă îndrumare cu privire la ceea ce se așteaptă în răspuns, fie prin furnizarea de _instrucțiuni_ (ghidare explicită), fie _oferindu-i câteva exemple_ (ghidare implicită). Aceasta este denumită _învățare cu puține exemple_, dar are două limitări:

- Limitele de token ale modelului pot restricționa numărul de exemple pe care le puteți oferi și pot limita eficiența.
- Costurile token-urilor modelului pot face costisitor adăugarea de exemple la fiecare prompt și pot limita flexibilitatea.

Ajustarea fină este o practică comună în sistemele de învățare automată, unde luăm un model pre-antrenat și îl reantrenăm cu date noi pentru a-i îmbunătăți performanța pe o sarcină specifică. În contextul modelelor lingvistice, putem ajusta fin modelul pre-antrenat _cu un set curat de exemple pentru o sarcină sau un domeniu de aplicație specific_ pentru a crea un **model personalizat** care poate fi mai precis și mai relevant pentru acea sarcină sau domeniu specific. Un beneficiu secundar al ajustării fine este că poate reduce numărul de exemple necesare pentru învățarea cu puține exemple - reducând utilizarea token-urilor și costurile aferente.

## Când și de ce ar trebui să ajustăm fin modelele?

În _acest_ context, când vorbim despre ajustare fină, ne referim la ajustarea fină **supervizată**, unde reantrenarea se face prin **adăugarea de date noi** care nu au făcut parte din setul de date original de antrenament. Acest lucru este diferit de abordarea ajustării fine nesupervizate, unde modelul este reantrenat pe datele originale, dar cu hiperparametri diferiți.

Lucrul esențial de reținut este că ajustarea fină este o tehnică avansată care necesită un anumit nivel de expertiză pentru a obține rezultatele dorite. Dacă este realizată incorect, poate să nu ofere îmbunătățirile așteptate și poate chiar să degradeze performanța modelului pentru domeniul vizat.

Așadar, înainte de a învăța "cum" să ajustați fin modelele lingvistice, trebuie să știți "de ce" ar trebui să urmați această cale și "când" să începeți procesul de ajustare fină. Începeți prin a vă pune aceste întrebări:

- **Caz de utilizare**: Care este _cazul de utilizare_ pentru ajustarea fină? Ce aspect al modelului pre-antrenat actual doriți să îmbunătățiți?
- **Alternative**: Ați încercat _alte tehnici_ pentru a obține rezultatele dorite? Folosiți-le pentru a crea o bază de comparație.
  - Ingineria prompturilor: Încercați tehnici precum prompturi cu puține exemple, cu exemple de răspunsuri relevante. Evaluați calitatea răspunsurilor.
  - Generarea augmentată prin recuperare: Încercați să augmentați prompturile cu rezultate ale interogărilor obținute prin căutarea datelor voastre. Evaluați calitatea răspunsurilor.
- **Costuri**: Ați identificat costurile pentru ajustarea fină?
  - Ajustabilitate - este modelul pre-antrenat disponibil pentru ajustare fină?
  - Efort - pentru pregătirea datelor de antrenament, evaluarea și rafinarea modelului.
  - Resurse de calcul - pentru rularea sarcinilor de ajustare fină și implementarea modelului ajustat fin.
  - Date - acces la suficiente exemple de calitate pentru impactul ajustării fine.
- **Beneficii**: Ați confirmat beneficiile ajustării fine?
  - Calitate - modelul ajustat fin a depășit baza de comparație?
  - Cost - reduce utilizarea token-urilor prin simplificarea prompturilor?
  - Extensibilitate - poate fi reutilizat modelul de bază pentru noi domenii?

Răspunzând la aceste întrebări, ar trebui să puteți decide dacă ajustarea fină este abordarea potrivită pentru cazul vostru de utilizare. Ideal, abordarea este validă doar dacă beneficiile depășesc costurile. Odată ce decideți să continuați, este timpul să vă gândiți _cum_ puteți ajusta fin modelul pre-antrenat.

Doriți mai multe informații despre procesul de luare a deciziilor? Urmăriți [Să ajustăm fin sau nu?](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Cum putem ajusta fin un model pre-antrenat?

Pentru a ajusta fin un model pre-antrenat, aveți nevoie de:

- un model pre-antrenat pentru ajustare fină
- un set de date pentru ajustare fină
- un mediu de antrenament pentru a rula sarcina de ajustare fină
- un mediu de găzduire pentru a implementa modelul ajustat fin

## Ajustarea fină în practică

Următoarele resurse oferă tutoriale pas cu pas pentru a vă ghida printr-un exemplu real folosind un model selectat cu un set de date curat. Pentru a parcurge aceste tutoriale, aveți nevoie de un cont la furnizorul specific, împreună cu acces la modelul și seturile de date relevante.

| Furnizor     | Tutorial                                                                                                                                                                       | Descriere                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Cum să ajustați fin modelele de chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)         | Învățați să ajustați fin un `gpt-35-turbo` pentru un domeniu specific ("asistent de rețete") prin pregătirea datelor de antrenament, rularea sarcinii de ajustare fină și utilizarea modelului ajustat fin pentru inferență.                                                                                                                                                                                                       |
| Azure OpenAI | [Tutorial de ajustare fină GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Învățați să ajustați fin un model `gpt-35-turbo-0613` **pe Azure** parcurgând pașii pentru a crea și încărca datele de antrenament, a rula sarcina de ajustare fină. Implementați și utilizați noul model.                                                                                                                                                                                                                         |
| Hugging Face | [Ajustarea fină a LLM-urilor cu Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                       | Acest articol de blog vă ghidează în ajustarea fină a unui _LLM deschis_ (ex: `CodeLlama 7B`) folosind biblioteca [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) și [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst]) cu seturi de date deschise pe Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Ajustarea fină a LLM-urilor cu AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                 | AutoTrain (sau AutoTrain Advanced) este o bibliotecă Python dezvoltată de Hugging Face care permite ajustarea fină pentru multe sarcini diferite, inclusiv ajustarea fină a LLM-urilor. AutoTrain este o soluție fără cod, iar ajustarea fină poate fi realizată în propriul nor, pe Hugging Face Spaces sau local. Suportă atât o interfață web, CLI, cât și antrenament prin fișiere de configurare yaml.                     |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Temă

Selectați unul dintre tutorialele de mai sus și parcurgeți-l. _Este posibil să replicăm o versiune a acestor tutoriale în Jupyter Notebooks în acest depozit doar pentru referință. Vă rugăm să folosiți sursele originale direct pentru a obține cele mai recente versiuni_.

## Felicitări! Continuați să învățați.

După ce ați finalizat această lecție, consultați [Colecția de învățare AI generativă](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a continua să vă dezvoltați cunoștințele despre AI generativ!

Felicitări!! Ați finalizat ultima lecție din seria v2 a acestui curs! Nu vă opriți din învățare și construire. \*\*Consultați pagina [RESURSE](RESOURCES.md?WT.mc_id=academic-105485-koreyst) pentru o listă de sugestii suplimentare doar pentru acest subiect.

Seria noastră de lecții v1 a fost, de asemenea, actualizată cu mai multe teme și concepte. Așadar, luați un minut pentru a vă reîmprospăta cunoștințele - și vă rugăm să [împărtășiți întrebările și feedback-ul vostru](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) pentru a ne ajuta să îmbunătățim aceste lecții pentru comunitate.

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.