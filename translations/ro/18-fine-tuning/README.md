<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3772dcd23a98e2010f53ce8b9c583631",
  "translation_date": "2026-01-18T19:04:03+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "ro"
}
-->
[![Open Source Models](../../../../../translated_images/ro/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Ajustarea fină a LLM-ului tău

Utilizarea modelelor mari de limbaj pentru a construi aplicații AI generative vine cu provocări noi. O problemă esențială este asigurarea calității răspunsurilor (acuratețea și relevanța) în conținutul generat de model pentru o cerere specifică a utilizatorului. În lecțiile anterioare, am discutat tehnici precum ingineria promptului și generarea augmentată prin recuperare, care încearcă să rezolve problema prin _modificarea inputului promptului_ către modelul existent.

În lecția de astăzi, discutăm o a treia tehnică, **ajustarea fină**, care încearcă să abordeze această provocare prin _reuținerea modelului în sine_ cu date suplimentare. Să trecem la detalii.

## Obiective de învățare

Această lecție introduce conceptul de ajustare fină pentru modelele pre-antrenate de limbaj, explorează beneficiile și provocările acestei abordări și oferă ghiduri despre când și cum să folosești ajustarea fină pentru a îmbunătăți performanța modelelor tale AI generative.

La finalul acestei lecții, ar trebui să poți răspunde la următoarele întrebări:

- Ce este ajustarea fină pentru modelele de limbaj?
- Când și de ce este utilă ajustarea fină?
- Cum pot ajusta fin un model pre-antrenat?
- Care sunt limitările ajustării fine?

Gata? Să începem.

## Ghid ilustrat

Dorești să ai o privire de ansamblu asupra a ceea ce vom acoperi înainte să intrăm în detalii? Consultă acest ghid ilustrat care descrie traseul de învățare pentru această lecție – de la înțelegerea conceptelor cheie și a motivației pentru ajustarea fină, până la înțelegerea procesului și a celor mai bune practici pentru executarea sarcinii de ajustare fină. Este un subiect fascinant de explorat, așa că nu uita să verifici pagina [Resurse](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) pentru linkuri suplimentare care să susțină călătoria ta de învățare autodirijată!

![Ghid ilustrat pentru ajustarea fină a modelelor de limbaj](../../../../../translated_images/ro/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Ce este ajustarea fină pentru modelele de limbaj?

Prin definiție, modelele mari de limbaj sunt _pre-antrenate_ pe cantități mari de text provenind din surse diverse, inclusiv internetul. Așa cum am învățat în lecțiile anterioare, avem nevoie de tehnici ca _ingineria promptului_ și _generarea augmentată prin recuperare_ pentru a îmbunătăți calitatea răspunsurilor modelului la întrebările ("promptele") utilizatorului.

O tehnică populară de inginerie a promptului implică oferirea modelului mai multă îndrumare despre ce se așteaptă în răspuns fie prin furnizarea de _instrucțiuni_ (ghidaj explicit), fie _oferindu-i câteva exemple_ (ghidaj implicit). Aceasta se numește _învățare cu puține exemple_ (few-shot learning), dar prezintă două limitări:

- Limitările de tokeni ale modelului pot restricționa numărul de exemple pe care le poți oferi și pot limita eficiența.
- Costurile legate de tokeni pot face scumpă adăugarea de exemple la fiecare prompt, limitând flexibilitatea.

Ajustarea fină este o practică comună în sistemele de învățare automată în care preluăm un model pre-antrenat și îl reantrenăm cu date noi pentru a-i îmbunătăți performanța pe o sarcină specifică. În contextul modelelor de limbaj, putem ajusta fin modelul pre-antrenat _cu un set selectat de exemple pentru o anumită sarcină sau domeniu de aplicație_, pentru a crea un **model personalizat** care să fie mai precis și mai relevant pentru acea sarcină sau domeniu specific. Un beneficiu suplimentar al ajustării fine este că aceasta poate reduce și numărul de exemple necesare în învățarea cu puține exemple – reducând consumul de tokeni și costurile asociate.

## Când și de ce ar trebui să ajustăm fin modelele?

În _acest_ context, când vorbim despre ajustarea fină, ne referim la ajustarea fină **supravegheată**, unde reantrenarea se face prin **adăugarea de date noi** care nu au făcut parte din setul de date inițial de antrenament. Aceasta diferă de o abordare neasistată unde modelul este reantrenat pe datele originale, dar cu hiperparametri diferiți.

Aspectul cheie de reținut este că ajustarea fină este o tehnică avansată care necesită un anumit nivel de expertiză pentru a obține rezultatele dorite. Dacă este făcută incorect, aceasta poate să nu ofere îmbunătățirile așteptate și chiar să degradeze performanța modelului pentru domeniul vizat.

Așadar, înainte să înveți „cum” să ajustezi fin modelele de limbaj, trebuie să știi „de ce” ar trebui să alegi această cale și „când” să începi procesul de ajustare fină. Începe prin a-ți pune următoarele întrebări:

- **Cazul de utilizare**: Care este _cazul tău de utilizare_ pentru ajustarea fină? Ce aspect al modelului pre-antrenat actual vrei să îmbunătățești?
- **Alternative**: Ai încercat _alte tehnici_ pentru a obține rezultatele dorite? Folosește-le pentru a crea un punct de referință pentru comparație.
  - Ingineria promptului: Încearcă tehnici precum few-shot prompting cu exemple relevante de răspunsuri la prompturi. Evaluează calitatea răspunsurilor.
  - Generarea augmentată prin recuperare: Încearcă să mărești prompturile cu rezultatele căutărilor în datele tale. Evaluează calitatea răspunsurilor.
- **Costuri**: Ai identificat costurile pentru ajustarea fină?
  - Posibilitatea de ajustare – este modelul pre-antrenat disponibil pentru ajustare fină?
  - Efort – pentru pregătirea datelor de antrenament, evaluarea și rafinarea modelului.
  - Computație – pentru rularea joburilor de ajustare fină și pentru implementarea modelului ajustat.
  - Date – acces la suficiente exemple de calitate pentru impactul ajustării fine.
- **Beneficii**: Ai confirmat beneficiile ajustării fine?
  - Calitate – modelul ajustat fin a depășit baza de referință?
  - Cost – reduce utilizarea tokenilor prin simplificarea prompturilor?
  - Extensibilitate – poți reutiliza modelul de bază pentru noi domenii?

Răspunzând acestor întrebări, ar trebui să poți decide dacă ajustarea fină este abordarea potrivită pentru cazul tău de utilizare. Ideal, abordarea este valabilă numai dacă beneficiile depășesc costurile. Odată ce decizi să continui, este timpul să te gândești _cum_ poți ajusta fin modelul pre-antrenat.

Vrei mai multe insight-uri despre procesul decizional? Vizualizează [To fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Cum putem ajusta fin un model pre-antrenat?

Pentru a ajusta fin un model pre-antrenat, ai nevoie de:

- un model pre-antrenat pentru ajustare fină
- un set de date pentru ajustarea fină
- un mediu de antrenament pentru a rula jobul de ajustare fină
- un mediu de găzduire pentru a implementa modelul ajustat fin

## Ajustarea fină în practică

Resursele următoare oferă tutoriale pas cu pas care te vor ghida printr-un exemplu real folosind un model selectat cu un set de date atent ales. Pentru a parcurge aceste tutoriale, ai nevoie de un cont la furnizorul specific, precum și acces la modelele și seturile de date relevante.

| Furnizor    | Tutorial                                                                                                                                                                      | Descriere                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI      | [Cum să ajustezi fin modelele de chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)         | Învață să ajustezi fin un `gpt-35-turbo` pentru un domeniu specific („asistent de rețete”) prin pregătirea datelor de antrenament, rularea jobului de ajustare fină și folosirea modelului ajustat pentru inferență.                                                                                                                                                                                                              |
| Azure OpenAI| [Tutorial de ajustare fină GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Învață să ajustezi fin un model `gpt-35-turbo-0613` **pe Azure** parcurgând pași pentru crearea și încărcarea datelor de antrenament, rularea jobului de ajustare fină, implementarea și utilizarea noului model.                                                                                                                                                                                                                    |
| Hugging Face| [Ajustarea fină a LLM-urilor cu Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                      | Acest articol explică cum să ajustezi fin un _LLM open source_ (ex: `CodeLlama 7B`) folosind biblioteca [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) și [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst), împreună cu seturi de date deschise ([datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst)) pe Hugging Face. |
|             |                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 🤗 AutoTrain| [Ajustarea fină a LLM-urilor cu AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                | AutoTrain (sau AutoTrain Advanced) este o bibliotecă Python dezvoltată de Hugging Face care permite ajustarea fină pentru multe sarcini diferite, inclusiv ajustarea fină a LLM-urilor. AutoTrain este o soluție fără cod și ajustarea fină poate fi făcută în propriul tău cloud, pe Hugging Face Spaces sau local. Suportă interfață web GUI, CLI și antrenament prin fișiere de configurare yaml.                                                    |
|             |                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 🦥 Unsloth | [Ajustarea fină a LLM-urilor cu Unsloth](https://github.com/unslothai/unsloth)                                                                                                  | Unsloth este un cadru open-source ce sprijină ajustarea fină a LLM-urilor și învățarea prin întărire (RL). Unsloth simplifică antrenamentul local, evaluarea și implementarea cu [notebook-uri](https://github.com/unslothai/notebooks) gata de folosit. Suportă de asemenea text-în-voce (TTS), BERT și modele multimodale. Pentru a începe, citește ghidul lor pas cu pas [Fine-tuning LLMs Guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).     |
|             |                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
## Temă

Selectează unul dintre tutorialele de mai sus și parcurge-l. _Este posibil să replicăm o versiune a acestor tutoriale în Jupyter Notebooks în acest depozit doar pentru referință. Te rugăm să folosești sursele originale direct pentru a obține cele mai recente versiuni_.

## Ai făcut o treabă grozavă! Continuă să înveți.

După ce ai terminat această lecție, consultă colecția noastră de [Învățare AI Generativ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a continua să-ți crești cunoștințele despre AI Generativ!

Felicitări!! Ai finalizat lecția finală din seria v2 a acestui curs! Nu te opri din a învăța și a construi. \*\*Vezi pagina [RESURSE](RESOURCES.md?WT.mc_id=academic-105485-koreyst) pentru o listă de sugestii suplimentare doar pentru acest subiect.

Seria noastră v1 de lecții a fost de asemenea actualizată cu mai multe teme și concepte. Așadar ia-ți un minut pentru a-ți reîmprospăta cunoștințele – și te rugăm [împărtășește întrebările și feedback-ul tău](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) pentru a ne ajuta să îmbunătățim aceste lecții pentru comunitate.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:
Acest document a fost tradus folosind serviciul de traducere automată AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un traducător uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot rezulta din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->