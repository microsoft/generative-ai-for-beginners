[![Open Source Models](../../../translated_images/ro/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Reglarea fină a modelului LLM

Utilizarea modelelor mari de limbaj pentru a construi aplicații AI generative vine cu noi provocări. O problemă cheie este asigurarea calității răspunsului (precizie și relevanță) în conținutul generat de model pentru o cerere dată a utilizatorului. În lecțiile anterioare, am discutat tehnici precum ingineria promptului și generarea augmentată cu recuperare, care încearcă să rezolve problema prin _modificarea inputului promptului_ pentru modelul existent.

În lecția de astăzi, discutăm o a treia tehnică, **reglarea fină**, care încearcă să abordeze provocarea prin _retraining-ul modelului în sine_ cu date suplimentare. Să intrăm în detalii.

## Obiectivele de învățare

Această lecție introduce conceptul de reglare fină pentru modelele de limbaj pre-antrenate, explorează beneficiile și provocările acestei abordări și oferă îndrumări despre când și cum să folosești reglarea fină pentru a îmbunătăți performanța modelelor tale AI generative.

Până la finalul acestei lecții, ar trebui să poți răspunde la următoarele întrebări:

- Ce este reglarea fină pentru modelele de limbaj?
- Când și de ce este utilă reglarea fină?
- Cum pot regla fin un model pre-antrenat?
- Care sunt limitările reglării fine?

Ești gata? Hai să începem.

## Ghid ilustrat

Vrei să ai o imagine de ansamblu asupra a ceea ce vom acoperi înainte să intrăm în detalii? Verifică acest ghid ilustrat care descrie călătoria de învățare pentru această lecție – de la înțelegerea conceptelor de bază și a motivației pentru reglarea fină, până la înțelegerea procesului și a celor mai bune practici pentru executarea sarcinii de reglare fină. Acesta este un subiect fascinant pentru explorare, așa că nu uita să verifici pagina [Resurse](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) pentru linkuri suplimentare care să susțină călătoria ta de învățare auto-ghidată!

![Ghid ilustrat pentru reglarea fină a modelelor de limbaj](../../../translated_images/ro/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Ce este reglarea fină pentru modelele de limbaj?

Prin definiție, modelele mari de limbaj sunt _pre-antrenate_ pe cantități mari de text provenind din surse diverse, inclusiv internetul. Așa cum am învățat în lecțiile anterioare, avem nevoie de tehnici precum _ingineria promptului_ și _generarea augmentată cu recuperare_ pentru a îmbunătăți calitatea răspunsurilor modelului la întrebările utilizatorului („prompts”).

O tehnică populară de inginerie a promptului implică să oferi modelului mai multă îndrumare despre ce se așteaptă în răspuns prin furnizarea de _instrucțiuni_ (ghidare explicită) sau _oferindu-i câteva exemple_ (ghidare implicită). Aceasta este denumită _învățare cu puține exemple_ (few-shot learning), dar are două limitări:

- Limitările tokenilor modelului pot restricționa numărul de exemple pe care le poți oferi și pot limita eficacitatea.
- Costurile tokenilor modelului pot face adăugarea de exemple la fiecare prompt costisitoare și pot limita flexibilitatea.

Reglarea fină este o practică comună în sistemele de învățare automată, unde luăm un model pre-antrenat și îl reantrenăm cu date noi pentru a-i îmbunătăți performanța pe o sarcină specifică. În contextul modelelor de limbaj, putem regla fin modelul pre-antrenat _cu un set selectat de exemple pentru o anumită sarcină sau domeniu de aplicație_ pentru a crea un **model personalizat** care poate fi mai precis și relevant pentru acea sarcină sau domeniu specific. Un beneficiu suplimentar al reglării fine este că poate reduce și numărul de exemple necesare pentru învățarea cu puține exemple – reducând utilizarea tokenilor și costurile aferente.

## Când și de ce ar trebui să reglăm fin modelele?

În _acest_ context, când vorbim despre reglarea fină, ne referim la reglarea fină **supravegheată**, unde reantrenarea se face prin **adăugarea de date noi** care nu au făcut parte din setul de date original. Aceasta este diferită de o abordare nesupravegheată a reglării fine, unde modelul este reantrenat pe datele originale, dar cu hiperparametri diferiți.

Lucrul esențial de reținut este că reglarea fină este o tehnică avansată care necesită un anumit nivel de expertiză pentru a obține rezultatele dorite. Dacă este făcută incorect, s-ar putea să nu ofere îmbunătățirile așteptate, și chiar să degradeze performanța modelului pentru domeniul țintă.

Așadar, înainte să înveți „cum” să reglezi fin modelele de limbaj, trebuie să știi „de ce” ar trebui să alegi această cale și „când” să începi procesul de reglare fină. Începe prin a-ți pune aceste întrebări:

- **Caz de utilizare**: Care este _cazul tău de utilizare_ pentru reglarea fină? Ce aspect al modelului pre-antrenat actual vrei să îmbunătățești?
- **Alternative**: Ai încercat _alte tehnici_ pentru a atinge rezultatele dorite? Folosește-le pentru a crea o bază de comparație.
  - Ingineria promptului: Încearcă tehnici precum prompting cu puține exemple cu răspunsuri relevante. Evaluează calitatea răspunsurilor.
  - Generare augmentată cu recuperare: Încearcă să mărești prompturile cu rezultate din căutarea datelor tale. Evaluează calitatea răspunsurilor.
- **Costuri**: Ai identificat costurile pentru reglarea fină?
  - Capacitatea de reglare – este modelul pre-antrenat disponibil pentru reglare fină?
  - Efort – pentru pregătirea datelor de antrenament, evaluarea și rafinarea modelului.
  - Putere de calcul – pentru rularea job-urilor de reglare fină și pentru implementarea modelului reglat.
  - Date – accesul la suficiente exemple de calitate pentru impactul reglării fine.
- **Beneficii**: Ai confirmat beneficiile reglării fine?
  - Calitate – modelul reglat a depășit modelul de bază?
  - Cost – reduce utilizarea tokenilor simplificând prompturile?
  - Extensibilitate – poți reutiliza modelul de bază pentru noi domenii?

Răspunzând acestor întrebări, ar trebui să poți decide dacă reglarea fină este abordarea potrivită pentru cazul tău de utilizare. Ideal, abordarea este valabilă doar dacă beneficiile depășesc costurile. Odată ce decizi să continui, este timpul să te gândești _cum_ poți regla fin modelul pre-antrenat.

Vrei să obții mai multe informații despre procesul decizional? Vizionați [Să reglăm fin sau nu să reglăm fin](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Cum putem regla fin un model pre-antrenat?

Pentru a regla fin un model pre-antrenat, ai nevoie de:

- un model pre-antrenat pe care să-l reglezi fin
- un set de date pentru reglarea fină
- un mediu de antrenament pentru a rula job-ul de reglare fină
- un mediu de găzduire pentru a implementa modelul reglat

## Reglarea fină pe Microsoft Foundry

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) este locul unde poți regla fin, implementa și gestiona modele personalizate pe Azure astăzi (reunește ceea ce anterior era Azure OpenAI Studio și Azure AI Studio). Înainte să începi un job, este util să înțelegi opțiunile pe care ți le oferă Foundry – și bunele practici recomandate de platformă. Under the hood, Foundry folosește **LoRA (adaptare în rang scăzut)** pentru a regla fin modelele eficient, ceea ce menține antrenamentul mai rapid și mai accesibil financiar decât reantrenarea fiecărei ponderi.

### Pasul 1: Alege o tehnică de antrenament

Foundry suportă trei tehnici de reglare fină. **Începe cu SFT** – acoperă cea mai largă gamă de scenarii.

| Tehnică | Ce face | Când să o folosești |
| --- | --- | --- |
| **Reglare fină supravegheată (SFT)** | Antrenează pe perechi exemplu input/output astfel încât modelul să învețe să producă răspunsurile dorite. | Implicit pentru majoritatea sarcinilor: specializarea pe domeniu, performanța sarcinii, stil și ton, urmare a instrucțiunilor și adaptare lingvistică. |
| **Optimizare directă a preferințelor (DPO)** | Învață din perechi de răspunsuri _preferate vs. nepreferate_ pentru a alinia rezultatele cu preferințele umane. | Îmbunătățirea calității răspunsului, siguranței și alinierii atunci când ai feedback comparativ. |
| **Reglare fină cu întărire (RFT)** | Folosește semnale de recompensă de la _evaluatori_ pentru a optimiza comportamente complexe prin învățare cu întărire. | Domenii obiective, cu raționamente complexe (matematică, chimie, fizică) cu răspunsuri clar corecte/greșite. Necesită mai multă expertiză în ML. |

### Pasul 2: Alege un nivel de antrenament

Foundry îți permite să alegi cum și unde rulează antrenamentul:

- **Standard** – antrenează în regiunea resursei tale și garantează rezidența datelor. Utilizează-l când datele trebuie să rămână într-o regiune specifică.
- **Global** – mai ieftin și mai rapid prin utilizarea capacității dincolo de regiunea ta (datele și ponderile sunt copiate în regiunea de antrenament). Implicit bun când rezidența datelor nu este o cerință.
- **Dezvoltator** – cel mai mic cost, folosind capacitate inactivă fără garanții de latență/SLA (job-urile pot fi întrerupte și reluate). Ideal pentru experimentare.

### Pasul 3: Alege un model de bază

Modelele reglabile includ OpenAI `gpt-4o-mini`, `gpt-4o`, `gpt-4.1`, `gpt-4.1-mini` și `gpt-4.1-nano` (SFT; familia 4o/4.1 suportă și DPO), modelele de raționament `o4-mini` și `gpt-5` (RFT), plus modele open-source precum `Ministral-3B`, `Qwen-32B`, `Llama-3.3-70B-Instruct` și `gpt-oss-20b` (SFT pe resurse Foundry). Verifică întotdeauna lista curentă de [modele pentru reglare fină](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) pentru metodele suportate, regiuni și disponibilitate.

> Foundry oferă două modalități: **fără server** (preț bazat pe consum, fără gestionarea cotei GPU, OpenAI și modele selectate) și **calcul gestionat** (utilizează VM-uri proprii prin Azure Machine Learning pentru cea mai largă gamă de modele). Majoritatea ar trebui să înceapă cu fără server.

### Cele mai bune practici în Foundry

- **Măsoară mai întâi baza.** Evaluează modelul de bază folosind inginerie de prompt și RAG _înainte_ de reglarea fină, pentru a putea demonstra câștigul.
- **Începe mic, apoi extinde.** Începe cu 50-100 de exemple de înaltă calitate pentru a valida abordarea, apoi crește la 500+ pentru producție. Calitatea bate cantitatea – elimină exemplele de calitate slabă.
- **Formatează corect datele.** Fișierele de antrenament și validare trebuie să fie JSONL, UTF-8 **cu BOM**, sub 512 MB, folosind formatul mesajelor chat-completions. Include întotdeauna un fișier de validare pentru a monitoriza overfitting-ul.
- **Păstrează promptul sistem pentru inferență.** Folosește același mesaj sistem atunci când apelezi modelul ca cel folosit la antrenament.
- **Evaluează punctele de control - nu implementa orb ultima versiune.** Foundry păstrează ultimele trei epoci ca puncte de control pentru implementare; alege-l pe cel care generalizează cel mai bine urmărind `train_loss` / `valid_loss` și acuratețea tokenilor.
- **Măsoară costul tokenilor împreună cu calitatea** când compari modelul reglat cu baza.
- **Iterează cu reglare fină continuă.** Poți regla fin un model deja reglat pe date noi (suportat pentru modelele OpenAI).
- **Fii atent la costurile de găzduire.** Un model personalizat implementat se facturează pe oră, iar o implementare inactivă este eliminată după 15 zile – curăță ce nu folosești.

Parcurge tutorialul complet în [Personalizează un model cu reglare fină](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) și vezi ghidurile pentru [DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst) și [RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst) când ești pregătit pentru celelalte tehnici.

## Reglarea fină în practică

Resursele următoare oferă tutoriale pas cu pas care te ghidează printr-un exemplu real pe un model suportat în prezent cu un set de date selectat. Pentru a le parcurge, ai nevoie de un cont la furnizorul specific, precum și acces la modelul și seturile de date relevante.

| Furnizor     | Tutorial                                                                                                                                                                       | Descriere                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Cum să reglezi fin modelele de chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Învăță cum să reglezi fin un model recent OpenAI de chat pentru un domeniu specific („asistent de rețete”) pregătind datele de antrenament, rulând job-ul de reglare fină și folosind modelul reglat pentru inferență.                                                                                                                                                                                                                                              |
| Microsoft Foundry | [Personalizează un model cu reglare fină](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Învăță cum să reglezi fin un model suportat în prezent, cum ar fi `gpt-4.1-mini` **pe Azure** cu Microsoft Foundry: pregătește și încarcă datele de antrenament și validare, rulează job-ul de reglare fină, apoi implementează și folosește noul model.                                                                                                                                                                                                                                                                 |

| Hugging Face | [Finisarea ajustării LLM-urilor cu Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Această postare pe blog te ghidează prin ajustarea fină a unui _LLM deschis_ (ex: `CodeLlama 7B`) folosind biblioteca [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) cu [dataset-uri](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) deschise pe Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Finisarea ajustării LLM-urilor cu AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (sau AutoTrain Advanced) este o bibliotecă python dezvoltată de Hugging Face care permite ajustarea fină pentru multe sarcini diferite, inclusiv ajustarea fină a LLM-urilor. AutoTrain este o soluție fără cod și ajustarea fină poate fi făcută în propriul tău cloud, pe Hugging Face Spaces sau local. Suportă atât o interfață grafică web, CLI și antrenare prin fișiere de configurare yaml.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Finisarea ajustării LLM-urilor cu Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth este un cadru open-source care suportă ajustarea fină a LLM-urilor și învățarea prin întărire (RL). Unsloth simplifică antrenamentul local, evaluarea și implementarea cu [notebook-uri](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) gata de folosit. De asemenea, suportă text-to-speech (TTS), modele BERT și multimodale. Pentru a începe, citește ghidul lor pas cu pas [Fine-tuning LLMs Guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Sarcină

Selectează unul dintre tutorialele de mai sus și parcurge-l. _Este posibil să replicăm o versiune a acestor tutoriale în Jupyter Notebooks în acest repo doar ca referință. Te rugăm să folosești sursele originale direct pentru a obține cele mai noi versiuni_.

## Super! Continuă să înveți.

După ce ai terminat această lecție, consultă colecția noastră [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a continua să-ți crești cunoștințele despre AI Generativ!

Felicitări!! Ai terminat lecția finală din seria v2 pentru acest curs! Nu te opri din învățat și construit. \*\*Vezi pagina [RESURSE](RESOURCES.md?WT.mc_id=academic-105485-koreyst) pentru o listă cu sugestii suplimentare doar pentru acest subiect.

Seria noastră de lecții v1 a fost și ea actualizată cu mai multe sarcini și concepte. Așa că ia un moment să-ți reîmprospătezi cunoștințele - și te rugăm [împărtășește întrebările și feedback-ul tău](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) pentru a ne ajuta să îmbunătățim aceste lecții pentru comunitate.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->