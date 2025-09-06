<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8b2d4bb727c877ebf9edff8623d16b9",
  "translation_date": "2025-09-06T10:24:01+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "ro"
}
-->
[![Open Source Models](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.ro.png)](https://aka.ms/gen-ai-lesson16-gh?WT.mc_id=academic-105485-koreyst)

## Introducere

Lumea LLM-urilor open-source este captivantă și în continuă evoluție. Această lecție își propune să ofere o privire detaliată asupra modelelor open-source. Dacă dorești informații despre cum se compară modelele proprietare cu cele open-source, accesează lecția ["Explorarea și Compararea Diferitelor LLM-uri"](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Această lecție va aborda și subiectul ajustării fine, dar o explicație mai detaliată poate fi găsită în lecția ["Ajustarea Fină a LLM-urilor"](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Obiective de învățare

- Înțelegerea modelelor open-source
- Înțelegerea beneficiilor lucrului cu modele open-source
- Explorarea modelelor open disponibile pe Hugging Face și Azure AI Studio

## Ce sunt Modelele Open Source?

Software-ul open-source a jucat un rol crucial în creșterea tehnologiei în diverse domenii. Open Source Initiative (OSI) a definit [10 criterii pentru software](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) pentru a fi clasificat ca open-source. Codul sursă trebuie să fie distribuit public sub o licență aprobată de OSI.

Deși dezvoltarea LLM-urilor are elemente similare cu dezvoltarea software-ului, procesul nu este exact același. Acest lucru a generat multe discuții în comunitate despre definiția open-source în contextul LLM-urilor. Pentru ca un model să fie aliniat cu definiția tradițională de open-source, următoarele informații ar trebui să fie disponibile public:

- Seturile de date utilizate pentru antrenarea modelului.
- Greutățile complete ale modelului ca parte a antrenamentului.
- Codul de evaluare.
- Codul de ajustare fină.
- Greutățile complete ale modelului și metricele de antrenament.

În prezent, există doar câteva modele care îndeplinesc aceste criterii. [Modelul OLMo creat de Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) se încadrează în această categorie.

Pentru această lecție, vom face referire la modele ca "modele open" de acum înainte, deoarece este posibil să nu îndeplinească criteriile de mai sus la momentul redactării.

## Beneficiile Modelelor Open

**Foarte personalizabile** - Deoarece modelele open sunt lansate cu informații detaliate despre antrenament, cercetătorii și dezvoltatorii pot modifica structura internă a modelului. Acest lucru permite crearea de modele extrem de specializate, ajustate fin pentru o anumită sarcină sau domeniu de studiu. Unele exemple includ generarea de cod, operații matematice și biologie.

**Cost** - Costul per token pentru utilizarea și implementarea acestor modele este mai mic decât cel al modelelor proprietare. Când construiești aplicații Generative AI, ar trebui să analizezi performanța versus prețul în funcție de cazul tău de utilizare.

![Model Cost](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.ro.png)  
Sursa: Artificial Analysis

**Flexibilitate** - Lucrul cu modele open îți permite să fii flexibil în utilizarea diferitelor modele sau combinarea lor. Un exemplu este [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst), unde utilizatorul poate selecta modelul utilizat direct din interfața utilizatorului:

![Choose Model](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.ro.png)

## Explorarea Diferitelor Modele Open

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), dezvoltat de Meta, este un model open optimizat pentru aplicații bazate pe chat. Acest lucru se datorează metodei de ajustare fină, care a inclus o cantitate mare de dialoguri și feedback uman. Prin această metodă, modelul produce mai multe rezultate aliniate așteptărilor umane, oferind o experiență mai bună utilizatorului.

Unele exemple de versiuni ajustate fin ale Llama includ [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), care se specializează în japoneză, și [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), care este o versiune îmbunătățită a modelului de bază.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) este un model open cu un accent puternic pe performanță și eficiență. Utilizează abordarea Mixture-of-Experts, care combină un grup de modele experte specializate într-un singur sistem, unde, în funcție de input, anumite modele sunt selectate pentru utilizare. Acest lucru face calculul mai eficient, deoarece modelele abordează doar inputurile în care sunt specializate.

Unele exemple de versiuni ajustate fin ale Mistral includ [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), care se concentrează pe domeniul medical, și [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), care efectuează calcule matematice.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) este un LLM creat de Technology Innovation Institute (**TII**). Falcon-40B a fost antrenat pe 40 de miliarde de parametri, ceea ce s-a demonstrat că oferă performanțe mai bune decât GPT-3 cu un buget de calcul mai mic. Acest lucru se datorează utilizării algoritmului FlashAttention și atenției multiquery, care îi permite să reducă cerințele de memorie în timpul inferenței. Cu acest timp redus de inferență, Falcon-40B este potrivit pentru aplicații de chat.

Unele exemple de versiuni ajustate fin ale Falcon sunt [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), un asistent construit pe modele open, și [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), care oferă performanțe mai ridicate decât modelul de bază.

## Cum să Alegi

Nu există un răspuns unic pentru alegerea unui model open. Un loc bun pentru a începe este utilizarea funcției de filtrare după sarcină din Azure AI Studio. Acest lucru te va ajuta să înțelegi ce tipuri de sarcini au fost antrenate modelele. Hugging Face menține, de asemenea, un LLM Leaderboard care îți arată cele mai performante modele pe baza anumitor metrici.

Când dorești să compari LLM-uri între diferite tipuri, [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) este o altă resursă excelentă:

![Model Quality](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.ro.png)  
Sursa: Artificial Analysis

Dacă lucrezi la un caz de utilizare specific, căutarea versiunilor ajustate fin care se concentrează pe același domeniu poate fi eficientă. Experimentarea cu mai multe modele open pentru a vedea cum performează în funcție de așteptările tale și ale utilizatorilor este o altă practică bună.

## Pași Următori

Partea cea mai bună despre modelele open este că poți începe să lucrezi cu ele destul de rapid. Consultă [Catalogul de Modele Azure AI Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), care include o colecție specifică Hugging Face cu modelele discutate aici.

## Învățarea nu se oprește aici, continuă călătoria

După finalizarea acestei lecții, consultă [Colecția de Învățare Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a continua să îți dezvolți cunoștințele despre Generative AI!

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.