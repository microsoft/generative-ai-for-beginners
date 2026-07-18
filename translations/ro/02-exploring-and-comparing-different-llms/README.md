# Explorarea și compararea diferitelor LLM-uri

[![Explorarea și compararea diferitelor LLM-uri](../../../translated_images/ro/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții_

În lecția precedentă, am văzut cum Generative AI schimbă peisajul tehnologic, cum funcționează Modelele Mari de Limbaj (LLM-uri) și cum o afacere — precum startup-ul nostru — le poate aplica cazurilor sale de utilizare pentru a crește! În acest capitol ne propunem să comparăm și să diferențiem diferitele tipuri de modele mari de limbaj (LLM-uri) pentru a înțelege avantajele și dezavantajele lor.

Pasul următor în călătoria startup-ului nostru este explorarea peisajului actual al LLM-urilor și înțelegerea celor potrivite pentru cazul nostru de utilizare.

## Introducere

Această lecție va acoperi:

- Diferitele tipuri de LLM-uri în peisajul actual.
- Testarea, iterarea și compararea diferitelor modele pentru cazul dvs. de utilizare în Azure.
- Cum să implementați un LLM.

## Obiective de învățare

După finalizarea acestei lecții, veți putea:

- Selecta modelul potrivit pentru cazul dvs. de utilizare.
- Înțelege cum să testați, iterati și să îmbunătățiți performanța modelului.
- Să știți cum implementează modelele afacerile.

## Înțelegerea diferitelor tipuri de LLM-uri

LLM-urile pot avea multiple categorii bazate pe arhitectura lor, datele de instruire și cazul de utilizare. Înțelegerea acestor diferențe ne va ajuta startup-ul să selecteze modelul potrivit pentru scenariu și să înțeleagă cum să testeze, să itereze și să îmbunătățească performanța.

Există multe tipuri diferite de modele LLM, alegerea modelului depinde de scopul pentru care doriți să le folosiți, datele dumneavoastră, cât sunteți dispus să plătiți și altele.

În funcție de faptul dacă doriți să folosiți modelele pentru text, audio, video, generare de imagini și așa mai departe, ați putea opta pentru un tip diferit de model.

- **Recunoaștere audio și vorbire**. Modelele de tip Whisper sunt încă utile ca modele generaliste de recunoaștere a vorbirii, dar opțiunile de producție includ acum modele noi de vorbire în text, cum ar fi `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`, și variante de diarizare. Evaluați acoperirea limbilor, diarizarea, suportul în timp real, latența și costul pentru scenariul dvs. Aflați mai multe în [documentația OpenAI pentru speech-to-text](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst).

- **Generare de imagini**. DALL-E și Midjourney sunt opțiuni cunoscute pentru generarea imaginilor, dar actualele API-uri OpenAI pentru imagini se concentrează pe modelele GPT Image precum `gpt-image-2`, în timp ce Stable Diffusion, Imagen, Flux și alte familii de modele sunt de asemenea opțiuni comune. Comparați aderarea la prompt, suportul pentru editare, controlul stilului, cerințele de siguranță și licențiere. Aflați mai multe în [ghidul OpenAI pentru generarea imaginilor](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) și în Capitolul 9 al acestui curriculum.

- **Generare de text**. Modelele de text acum acoperă modele frontieră, modele de raționament, modele mai mici cu latență redusă și modele open-weight. Exemple actuale includ modelele OpenAI GPT-5.x, modelele Anthropic Claude 4.x, modelele Google Gemini 3.x, modelele Meta Llama 4 și modelele Mistral. Nu alegeți doar după data lansării sau preț; comparați calitatea sarcinii, latența, fereastra de context, folosirea instrumentelor, comportamentul de siguranță, disponibilitatea regională și costul total. [Catalogul de modele Microsoft Foundry](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) este un loc bun pentru a compara modelele disponibile pe Azure.

- **Multi-modalitate**. Multe modele actuale pot procesa mai mult decât text. Unele acceptă inputuri de imagine, audio sau video; unele pot apela instrumente; iar modelele specializate pot genera imagini, audio sau video. De exemplu, modelele OpenAI actuale suportă inputuri text și imagine, modelele Gemini pot suporta texte, cod, imagine, audio și video în funcție de variantă, iar Llama 4 Scout și Maverick sunt modele open-weight nativ multimodale. Verificați întotdeauna fiecare fișă a modelului pentru modalitățile de input și output suportate înainte de a construi un flux de lucru în jurul lui.

Selectarea unui model înseamnă că aveți anumite capabilități de bază, care însă s-ar putea să nu fie suficiente. Adesea aveți date specifice companiei pe care trebuie să le comunicați cumva LLM-ului. Există câteva opțiuni diferite pentru a aborda aceasta, despre care vom discuta în secțiunile următoare.

### Modele fundamentale versus LLM-uri

Termenul de Model Fundamental a fost [inventat de cercetătorii de la Stanford](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) și definit ca un model AI care respectă anumite criterii, cum ar fi:

- **Sunt antrenate folosind învățare nesupravegheată sau învățare auto-supervizată**, ceea ce înseamnă că sunt antrenate pe date multimodale neetichetate și nu necesită etichetare umană a datelor pentru procesul de instruire.
- **Sunt modele foarte mari**, bazate pe rețele neuronale foarte adânci antrenate pe miliarde de parametri.
- **Sunt de obicei destinate să servească ca „fundament” pentru alte modele**, ceea ce înseamnă că pot fi folosite ca punct de plecare pentru construirea altor modele prin ajustare fină.

![Modele fundamentale versus LLM-uri](../../../translated_images/ro/FoundationModel.e4859dbb7a825c94.webp)

Sursa imaginii: [Essential Guide to Foundation Models and Large Language Models | by Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Pentru a clarifica această distincție, să luăm ChatGPT ca exemplu istoric. Versiunile timpurii ale ChatGPT au folosit GPT-3.5 ca model fundamental. OpenAI a folosit apoi date specifice chatului și tehnici de aliniere pentru a crea o versiune ajustată care performa mai bine în scenarii conversaționale, precum chatbots. Serviciile AI moderne adesea rotează între mai multe variante de modele, astfel că numele serviciului și numele modelului de bază nu sunt întotdeauna același lucru.

![Model fundamental](../../../translated_images/ro/Multimodal.2c389c6439e0fc51.webp)

Sursa imaginii: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Modele Open-Weight/Open-Source versus Modele Proprietare

O altă modalitate de a categorisi LLM-urile este dacă sunt open-weight, open-source sau proprietare.

Modelele open-source și open-weight pun la dispoziție artefactele modelului pentru inspecție, descărcare sau personalizare, dar licențele lor diferă. Unele sunt complet open source, în timp ce altele sunt modele open-weight cu restricții de utilizare. Ele pot fi utile când o afacere are nevoie de un control mai mare asupra implementării, localizării datelor, costului sau personalizării. Totuși, echipele trebuie să revizuiască termenii licenței, costurile de servire, întreținerea, actualizările de securitate și calitatea evaluării înainte de a le folosi în producție. Exemple includ [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst), unele [modele Mistral](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst) și multe modele găzduite pe [Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst).

Modelele proprietare sunt deținute și găzduite de un furnizor. Aceste modele sunt adesea optimizate pentru utilizare gestionată în producție și pot oferi suport puternic, sisteme de siguranță, integrare a instrumentelor și scalare. Totuși, clienții de obicei nu pot inspecta sau modifica greutățile modelului și trebuie să revizuiască termenii furnizorului privind confidențialitatea, păstrarea datelor, conformitatea și utilizarea acceptabilă. Exemple includ [modelele OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), [Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst) și [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst).

### Generare de embedding versus imagine versus text și cod

LLM-urile pot fi de asemenea categorizate după tipul de output pe care îl generează.

Embedding-urile sunt un set de modele care pot transforma textul într-o formă numerică, numită embedding, care reprezintă numeric textul de intrare. Embedding-urile facilitează înțelegerea relațiilor dintre cuvinte sau fraze de către mașini și pot fi folosite ca inputuri pentru alte modele, precum modelele de clasificare sau cele de clustering, care au performanțe mai bune pe date numerice. Modelele de embedding sunt frecvent folosite pentru transfer learning, unde un model este construit pentru o sarcină surrogate pentru care există o abundență de date, iar apoi greutățile modelului (embedding-urile) sunt reutilizate pentru alte sarcini ulterioare. Un exemplu al acestei categorii este [embedding-urile OpenAI](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Embedding](../../../translated_images/ro/Embedding.c3708fe988ccf760.webp)

Modelele de generare de imagini sunt modele care generează imagini. Aceste modele sunt adesea folosite pentru editarea imaginilor, sinteza imaginilor și traducerea imaginilor. Modelele de generare de imagini sunt antrenate pe seturi mari de date de imagini, precum [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), și pot fi utilizate pentru a genera imagini noi sau pentru a edita imagini existente folosind tehnici de inpainting, super-rezoluție și colorizare. Exemple includ [modelele GPT Image](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst), [modelele Stable Diffusion](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst) și modelele Imagen.

![Generare de imagini](../../../translated_images/ro/Image.349c080266a763fd.webp)

Modelele de generare de text și cod sunt modele care generează text sau cod. Aceste modele sunt folosite adesea pentru sumarizarea textului, traducere și răspuns la întrebări. Modelele de generare de text sunt antrenate pe seturi mari de date de text, cum ar fi [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), și pot genera text nou sau pot răspunde la întrebări. Modelele de generare a codului, precum [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), sunt antrenate pe seturi mari de date de cod, cum ar fi GitHub, și pot genera cod nou sau pot repara erori în codul existent.

![Generare de text și cod](../../../translated_images/ro/Text.a8c0cf139e5cc2a0.webp)

### Encoder-Decoder versus Decoder-only

Pentru a discuta despre diferitele tipuri de arhitecturi ale LLM-urilor, să folosim o analogie.

Imaginează-ți că managerul tău ți-a dat sarcina să scrii un quiz pentru studenți. Ai doi colegi; unul supraveghează crearea conținutului, iar celălalt supraveghează revizuirea acestuia.

Creatorul de conținut este ca un model doar decoder: poate privi subiectul, vede ce ai scris deja și continuă generarea de conținut pe baza acelui context. Ei sunt foarte buni la scrierea unui conținut captivant și informativ, dar nu sunt întotdeauna cea mai bună alegere când sarcina este doar clasificare, preluare sau codificare a informației. Exemple de familii de modele decoder-only includ modelele GPT și Llama.

Recenzorul este ca un model doar encoder; ei privesc cursul scris și răspunsurile, observând relația dintre ele și înțelegând contextul, dar nu sunt buni la generarea de conținut. Un exemplu de model doar encoder este BERT.

Imaginează-ți că am putea avea pe cineva care să creeze și să revizuiască quizul; acesta este un model Encoder-Decoder. Câteva exemple ar fi BART și T5.

### Serviciu versus Model

Acum, să vorbim despre diferența dintre un serviciu și un model. Un serviciu este un produs oferit de un Furnizor de Servicii Cloud și este adesea o combinație de modele, date și alte componente. Un model este componenta centrală a unui serviciu și este adesea un model fundamental, precum un LLM.

Serviciile sunt adesea optimizate pentru utilizarea în producție și sunt mai ușor de utilizat decât modelele, printr-o interfață grafică. Totuși, serviciile nu sunt întotdeauna disponibile gratuit și pot necesita abonament sau plată în schimbul utilizării echipamentului și resurselor proprietarului de serviciu, optimizând costurile și scalarea facilă. Un exemplu de serviciu este [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-foundry/openai/overview?WT.mc_id=academic-105485-koreyst), care oferă un plan tarifar pay-as-you-go, adică utilizatorii sunt taxați proporțional cu cât folosesc serviciul. Azure OpenAI Service oferă, de asemenea, securitate la nivel enterprise și un cadru AI responsabil pe deasupra capabilităților modelelor.

Modelele sunt artefactele rețelelor neuronale: parametrii, greutățile, arhitectura, tokenizer-ul și configurația suport. Rularea unui model local sau într-un mediu privat necesită hardware adecvat, infrastructură de servire, monitorizare și fie o licență open-source/open-weight compatibilă, fie o licență comercială. Modelele open-weight precum Llama 4 sau modelele Mistral pot fi găzduite independent, dar necesită în continuare putere de calcul și expertiză operațională.

## Cum să testați și să iterați cu diferite modele pentru a înțelege performanța pe Azure


Odată ce echipa noastră a explorat peisajul actual al LLM-urilor și a identificat câțiva candidați buni pentru scenariile lor, următorul pas este testarea lor pe datele și pe volumul lor de lucru. Acesta este un proces iterativ, realizat prin experimente și măsurători.
Majoritatea modelelor menționate în paragrafele precedente (modele OpenAI, modele cu greutate deschisă precum Llama 4 și Mistral și modele Hugging Face) sunt disponibile în [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst).

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst), anterior Azure AI Studio/Azure AI Foundry, este o platformă unificată Azure pentru construirea aplicațiilor și agenților AI. Ajută dezvoltatorii să gestioneze ciclul de viață de la experimentare și evaluare până la implementare, monitorizare și guvernanță. Catalogul de modele din Microsoft Foundry permite utilizatorului să:

- Găsească modelul de bază de interes în catalog, inclusiv modelele vândute de Azure și modelele de la parteneri și furnizori din comunitate. Utilizatorii pot filtra după sarcină, furnizor, licență, opțiune de implementare sau nume.

![Model catalog](../../../translated_images/ro/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- Revizuiască fișa modelului, inclusiv o descriere detaliată a utilizării intenționate și a datelor de antrenament, exemple de cod și rezultate de evaluare în biblioteca internă de evaluări.

![Model card](../../../translated_images/ro/ModelCard.598051692c6e400d.webp)

- Compare benchmark-urile între modele și seturile de date disponibile în industrie pentru a evalua care se potrivește scenariului de afaceri, prin panoul [Model Benchmarks](https://learn.microsoft.com/azure/ai-foundry/concepts/model-benchmarks?WT.mc_id=academic-105485-koreyst).

![Model benchmarks](../../../translated_images/ro/ModelBenchmarks.254cb20fbd06c03a.webp)

- Ajustează fin modelele suportate pe date proprii de antrenament pentru a îmbunătăți performanța modelului într-un volum specific de lucru, valorificând capabilitățile de experimentare și urmărire ale Microsoft Foundry.

![Model fine-tuning](../../../translated_images/ro/FineTuning.aac48f07142e36fd.webp)

- Implementează modelul pre-antrenat original sau versiunea ajustată fin la un punct de inferență real-time la distanță, folosind opțiuni de calcul gestionat sau implementare serverless, pentru a permite aplicațiilor să-l consume.

![Model deployment](../../../translated_images/ro/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> Nu toate modelele din catalog sunt în prezent disponibile pentru fine-tuning și/sau implementare pay-as-you-go. Verificați fișa modelului pentru detalii despre capabilitățile și limitările modelului.

## Îmbunătățirea rezultatelor LLM

Echipa noastră startup a explorat diferite tipuri de LLM-uri și o platformă cloud (Microsoft Foundry) care ne permite să comparăm diferite modele, să le evaluăm pe date de test, să îmbunătățim performanța și să le implementăm pe puncte de inferență.

Dar când ar trebui să ia în considerare ajustarea fină a unui model în loc să folosească unul pre-antrenat? Există alte abordări pentru îmbunătățirea performanței modelului pe volume specifice de lucru?

Există mai multe abordări pe care o afacere le poate folosi pentru a obține rezultatele dorite dintr-un LLM. Poți selecta diferite tipuri de modele cu diferite grade de antrenament atunci când implementezi un LLM în producție, cu niveluri diferite de complexitate, cost și calitate. Iată câteva abordări diferite:

- **Inginerie de prompt cu context**. Ideea este să oferi suficient context când formulezi promptul pentru a te asigura că primești răspunsurile necesare.

- **Retrieval Augmented Generation, RAG**. Datele tale ar putea exista într-o bază de date sau un endpoint web, de exemplu, pentru a te asigura că aceste date, sau un subset al lor, sunt incluse în momentul promptului, poți prelua datele relevante și să le faci parte din prompt-ul utilizatorului.

- **Model ajustat fin**. Aici, ai antrenat modelul mai departe pe propriile tale date, ceea ce a făcut ca modelul să fie mai exact și mai receptiv la nevoile tale, dar poate fi costisitor.

![LLMs deployment](../../../translated_images/ro/Deploy.18b2d27412ec8c02.webp)

Sursă imagine: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Ingineria prompt-ului cu context

LLM-urile pre-antrenate funcționează foarte bine pe task-uri generalizate de limbaj natural, chiar și atunci când sunt apelate cu un prompt scurt, cum ar fi o propoziție de completat sau o întrebare – învățarea numită „zero-shot”.

Totuși, cu cât utilizatorul poate încadra mai bine interogarea, cu o cerere detaliată și exemple – Contextul – cu atât răspunsul va fi mai exact și mai aproape de așteptările utilizatorului. În acest caz, vorbim despre „one-shot” learning dacă promptul include un singur exemplu și „few-shot learning” dacă include mai multe exemple.
Ingineria prompt-ului cu context este cea mai rentabilă metodă pentru a începe.

### Retrieval Augmented Generation (RAG)

LLM-urile au limitarea că pot folosi doar datele folosite în timpul antrenamentului pentru a genera un răspuns. Aceasta înseamnă că nu știu nimic despre faptele care s-au întâmplat după procesul lor de antrenament și nu pot accesa informații non-publice (cum ar fi datele companiei).
Aceasta poate fi depășită prin RAG, o tehnică care completează promptul cu date externe sub formă de bucăți de documente, ținând cont de limitele de lungime ale promptului. Aceasta este susținută de instrumente de baze de date Vector (precum [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) care preiau bucățile utile din surse de date variate și predefinite și le adaugă în Contextul promptului.

Această tehnică este foarte utilă când o afacere nu are suficiente date, timp sau resurse pentru a face fine-tuning unui LLM, dar dorește totuși să îmbunătățească performanța pe un volum specific de lucru și să reducă riscurile răspunsurilor halucinate, depășite sau nesusținute.

### Model ajustat fin

Fine-tuning-ul este un proces care valorifică transferul de învățare pentru a „adapta” modelul la o sarcină ulterioară sau pentru a rezolva o problemă specifică. Spre deosebire de few-shot learning și RAG, rezultă într-un nou model generat, cu greutăți și biasuri actualizate. Necesită un set de exemple de antrenament alcătuit dintr-o singură intrare (promptul) și ieșirea sa asociată (completarea).
Aceasta ar fi abordarea preferată dacă:

- **Folosirea modelelor mai mici, specifice sarcinii**. O afacere ar prefera să ajusteze fin un model mai mic pentru o sarcină restrânsă în loc să apeleze în mod repetat un model frontieră mai mare, rezultând într-o soluție mai eficientă din punct de vedere al costului și mai rapidă.

- **Considerarea latenței**. Latența este importantă pentru un caz de utilizare specific, deci nu este posibil să se folosească prompturi foarte lungi sau numărul de exemple de la care modelul ar trebui să învețe nu se potrivește cu limita de lungime a promptului.

- **Adaptarea unui comportament stabil**. O afacere are multe exemple de înaltă calitate și dorește ca modelul să urmeze constant un șablon de sarcină, un format al ieșirii, un ton sau un stil specific domeniului. Dacă problema principală sunt fapte proaspete sau cunoștințe private care se schimbă des, folosește RAG în loc să te bazezi doar pe fine-tuning.

### Model antrenat

Antrenarea unui LLM de la zero este fără îndoială cea mai dificilă și mai complexă abordare, necesitând cantități masive de date, resurse specializate și putere computațională adecvată. Această opțiune ar trebui considerată doar într-un scenariu în care o afacere are un caz de utilizare specific domeniului și un volum mare de date centrate pe domeniu.

## Verificarea cunoștințelor

Care ar putea fi o abordare bună pentru a îmbunătăți rezultatele completării unui LLM?

1. Ingineria prompt-ului cu context
1. RAG
1. Model ajustat fin

Răspuns: Toate trei pot ajuta. Începe cu ingineria prompt-ului și context pentru îmbunătățiri rapide și folosește RAG când modelul are nevoie de fapte curente sau date private de afaceri. Alege fine-tuning-ul când ai suficiente exemple de înaltă calitate și ai nevoie ca modelul să respecte constant un șablon de sarcină, format, ton sau domeniu.

## 🚀 Provocare

Citește mai mult despre cum poți [folosi RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) pentru afacerea ta.

## Foarte bine, Continuă să înveți

După ce ai finalizat această lecție, consultă colecția noastră [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a continua să-ți îmbunătățești cunoștințele despre AI Generativ!

Mergi la Lecția 3 unde vom vedea cum să [construim cu AI generativ în mod responsabil](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->