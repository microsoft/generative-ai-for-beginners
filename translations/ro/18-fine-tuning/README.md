[![Open Source Models](../../../translated_images/ro/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Fine-Tuning LLM-ul tău

Utilizarea modelelor mari de limbaj pentru a construi aplicații de AI generativ vine cu provocări noi. O problemă principală este asigurarea calității răspunsului (acuratețe și relevanță) în conținutul generat de model pentru o anumită cerere a utilizatorului. În lecțiile anterioare, am discutat tehnici precum ingineria promptului și generarea augmentată cu recuperare, care încearcă să rezolve problema prin _modificarea inputului promptului_ către modelul existent.

În lecția de astăzi, discutăm a treia tehnică, **fine-tuning**, care încearcă să abordeze provocarea prin _reantrenarea modelului însăși_ cu date adiționale. Hai să explorăm detaliile.

## Obiective de învățare

Această lecție introduce conceptul de fine-tuning pentru modelele de limbaj pre-antrenate, explorează beneficiile și provocările acestei abordări și oferă ghidare despre când și cum să folosești fine-tuning pentru a îmbunătăți performanța modelelor tale AI generative.

La finalul acestei lecții, ar trebui să fii capabil să răspunzi la următoarele întrebări:

- Ce este fine-tuning pentru modelele de limbaj?
- Când și de ce este util fine-tuning-ul?
- Cum pot face fine-tuning unui model pre-antrenat?
- Care sunt limitările fine-tuning-ului?

Pregătit? Să începem.

## Ghid ilustrat

Vrei să ai o imagine de ansamblu despre ce vom parcurge înainte să începem? Consultă acest ghid ilustrat care descrie parcursul de învățare pentru această lecție - de la învățarea conceptelor-cheie și a motivației pentru fine-tuning, până la înțelegerea procesului și a celor mai bune practici pentru execuția sarcinii de fine-tuning. Este un subiect fascinant pentru explorare, așa că nu uita să consulți pagina [Resurse](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) pentru link-uri suplimentare care să sprijine călătoria ta de învățare autoghidată!

![Ghid ilustrat pentru fine-tuning-ul modelelor de limbaj](../../../translated_images/ro/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Ce este fine-tuning-ul pentru modelele de limbaj?

Prin definiție, modelele mari de limbaj sunt _pre-antrenate_ pe cantități mari de text provenind din surse diverse inclusiv internetul. Așa cum am învățat în lecțiile anterioare, avem nevoie de tehnici precum _ingineria promptului_ și _generarea augmentată cu recuperare_ pentru a îmbunătăți calitatea răspunsurilor modelului la întrebările utilizatorului ("prompts").

O tehnică populară de inginerie a promptului implică să-i oferim modelului mai multe indicații despre ce se așteaptă în răspuns, fie prin _instrucțiuni_ (ghidare explicită), fie prin _oferirea unor exemple_ (ghidare implicită). Aceasta se numește _învățare few-shot_, dar are două limitări:

- Limitele de tokeni ale modelului pot restricționa numărul de exemple pe care le poți oferi și pot limita eficacitatea.
- Costurile de tokeni pot face costisitor să adaugi exemple la fiecare prompt și pot limita flexibilitatea.

Fine-tuning-ul este o practică comună în sistemele de învățare automată, unde preluăm un model pre-antrenat și îl reantrenăm cu date noi pentru a-i îmbunătăți performanța într-o sarcină specifică. În contextul modelelor de limbaj, putem face fine-tuning pe modelul pre-antrenat _cu un set selectat de exemple pentru o sarcină sau domeniu specific_ pentru a crea un **model personalizat** care poate fi mai precis și mai relevant pentru acea sarcină sau domeniu. Un beneficiu secundar al fine-tuning-ului este că poate reduce numărul de exemple necesare pentru învățarea few-shot - reducând astfel utilizarea tokenilor și costurile aferente.

## Când și de ce ar trebui să facem fine-tuning modelelor?

În _acest_ context, când vorbim de fine-tuning, ne referim la fine-tuning **supravegheat** unde reantrenarea se face prin **adăugarea de date noi** care nu au făcut parte din setul de antrenament inițial. Acesta este diferit de o abordare de fine-tuning nesupravegheat, unde modelul este reantrenat pe datele originale, dar cu hiperparametri diferiți.

Aspectul-cheie de reținut este că fine-tuning-ul este o tehnică avansată care necesită un anumit nivel de expertiză pentru a obține rezultatele dorite. Dacă este făcut incorect, este posibil să nu ofere îmbunătățirile așteptate și chiar să degradeze performanța modelului pentru domeniul țintă.

Așadar, înainte să înveți "cum" să faci fine-tuning la modele de limbaj, trebuie să știi "de ce" ar trebui să alegi această cale și "când" să începi procesul de fine-tuning. Începe prin a-ți pune următoarele întrebări:

- **Caz de utilizare**: Care este _cazul tău de utilizare_ pentru fine-tuning? Ce aspect al modelului pre-antrenat actual dorești să îl îmbunătățești?
- **Alternative**: Ai încercat _alte tehnici_ pentru a obține rezultatele dorite? Folosește-le pentru a crea o bază de comparație.
  - Ingineria promptului: Încearcă tehnici precum prompting-ul few-shot cu exemple de răspunsuri relevante la prompturi. Evaluează calitatea răspunsurilor.
  - Generare Augmentată cu Recuperare: Încearcă să mărești prompturile cu rezultatele interogărilor obținute prin căutarea în datele tale. Evaluează calitatea răspunsurilor.
- **Costuri**: Ai identificat costurile pentru fine-tuning?
  - Capacitatea de tunare - este modelul pre-antrenat disponibil pentru fine-tuning?
  - Efort - pentru pregătirea datelor de antrenament, evaluarea și rafinarea modelului.
  - Calcul - pentru rularea joburilor de fine-tuning și implementarea modelului fin-tuned
  - Date - acces la exemple de calitate suficiente pentru impactul fine-tuning-ului
- **Beneficii**: Ai confirmat beneficiile fine-tuning-ului?
  - Calitate - a depășit modelul fin-tuned baza de referință?
  - Cost - reduce utilizarea tokenilor prin simplificarea prompturilor?
  - Extensibilitate - poți reutiliza modelul de bază pentru noi domenii?

Răspunzând la aceste întrebări, ar trebui să poți decide dacă fine-tuning-ul este abordarea potrivită pentru cazul tău de utilizare. Ideal, această abordare este validă doar dacă beneficiile depășesc costurile. Odată ce decizi să continui, e timpul să te gândești _cum_ poți face fine tuning modelului pre-antrenat.

Vrei să afli mai multe perspective asupra procesului decizional? Urmărește [To fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Cum putem face fine-tuning unui model pre-antrenat?

Pentru a face fine-tuning unui model pre-antrenat, ai nevoie de:

- un model pre-antrenat pentru fine-tuning
- un set de date pentru fine-tuning
- un mediu de antrenament pentru a rula jobul de fine-tuning
- un mediu de găzduire pentru a implementa modelul fin-tuned

## Fine-Tuning în acțiune

> **Notă:** `gpt-35-turbo` / `gpt-3.5-turbo`, referit în unele tutoriale de mai jos, este retras atât pentru inferență cât și pentru fine-tuning. Dacă începi un nou job de fine-tuning astăzi, țintește un model suportat în prezent - de exemplu `gpt-4o-mini` sau `gpt-4.1-mini`. Vezi lista [Fine-tuning models list](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) pentru setul actual de modele ce pot fi fine-tunate. Conceptele și pașii din aceste tutoriale încă se aplică.

Resursele următoare oferă tutoriale pas cu pas care te ghidează printr-un exemplu real folosind un model selectat cu un set de date curat. Pentru a parcurge aceste tutoriale, ai nevoie de un cont la furnizorul specific, împreună cu acces la modelul și dataseturile relevante.

| Furnizor    | Tutorial                                                                                                                                                                      | Descriere                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Cum să faci fine-tuning la modelele de chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Învață să faci fine-tuning la un `gpt-35-turbo` pentru un domeniu specific ("asistent rețete") pregătind date de antrenament, rulând jobul de fine-tuning și folosind modelul fin-tuned pentru inferență.                                                                                                                                                                                                                           |
| Azure OpenAI | [Tutorial de fine-tuning GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst) | Învață să faci fine-tuning la un model `gpt-35-turbo-0613` **pe Azure** parcurgând pașii de creare & încărcare a datelor de antrenament, rularea jobului de fine-tuning, implementarea și folosirea noului model.                                                                                                                                                                                                                   |
| Hugging Face | [Fine-tuning LLM-uri cu Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Această postare de blog te ghidează să faci fine-tuning la un _LLM deschis_ (ex: `CodeLlama 7B`) folosind biblioteca [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) și [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) cu [dataseturi](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) deschise pe Hugging Face.          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Fine-tuning LLM-uri cu AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (sau AutoTrain Advanced) este o librărie python dezvoltată de Hugging Face care permite fine-tuning pentru multe sarcini diferite inclusiv fine-tuning pentru LLM. AutoTrain este o soluție fără cod și fine-tuning poate fi făcut în propria ta cloud, pe Hugging Face Spaces sau local. Suportă interfață web, CLI și antrenament prin fișiere de configurare yaml.                                                                                 |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Fine-tuning LLM-uri cu Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                          | Unsloth este un cadru open-source care suportă fine-tuning-ul LLM și învățarea prin întărire (RL). Unsloth simplifică antrenamentul local, evaluarea și implementarea cu [notebook-uri gata de folosit](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). De asemenea, suportă text-to-speech (TTS), BERT și modele multimodale. Pentru a începe, citește ghidul lor pas cu pas [Fine-tuning LLMs Guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Tema

Selectează unul dintre tutorialele de mai sus și parcurge-l. _Putem reproduce o versiune a acestor tutoriale în Jupyter Notebooks în acest repository doar ca referință. Te rugăm să folosești sursele originale direct pentru a obține cele mai recente versiuni_.

## Foarte bine! Continuă să înveți.

După ce ai finalizat această lecție, consultă colecția noastră [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a-ți continua progresul în cunoașterea AI generativ!

Felicitări!! Ai terminat lecția finală din seria v2 pentru acest curs! Nu înceta să înveți și să construiești. \*\*Consultă pagina [RESURSE](RESOURCES.md?WT.mc_id=academic-105485-koreyst) pentru o listă suplimentară de sugestii strict pentru acest subiect.

Seria noastră v1 de lecții a fost de asemenea actualizată cu mai multe teme și concepte. Așa că ia-ți un moment să-ți reîmprospătezi cunoștințele - și te rugăm să [împărtășești întrebările și feedback-ul tău](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) pentru a ne ajuta să îmbunătățim aceste lecții pentru comunitate.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->