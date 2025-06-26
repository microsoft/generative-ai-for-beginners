<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11f03c81f190d9cbafd0f977dcbede6c",
  "translation_date": "2025-06-26T00:25:10+00:00",
  "source_file": "17-ai-agents/README.md",
  "language_code": "ro"
}
-->
[![Open Source Models](../../../translated_images/17-lesson-banner.a5b918fb0920e4e6d8d391a100f5cb1d5929f4c2752c937d40392905dec82592.ro.png)](https://aka.ms/gen-ai-lesson17-gh?WT.mc_id=academic-105485-koreyst)

## Introducere

Agenții AI reprezintă o dezvoltare interesantă în domeniul AI Generativ, permițând modelelor lingvistice mari (LLMs) să evolueze de la asistenți la agenți capabili să ia acțiuni. Framework-urile pentru agenți AI permit dezvoltatorilor să creeze aplicații care oferă LLM-urilor acces la instrumente și gestionarea stării. Aceste framework-uri îmbunătățesc vizibilitatea, permițând utilizatorilor și dezvoltatorilor să monitorizeze acțiunile planificate de LLM-uri, îmbunătățind astfel gestionarea experienței.

Lecția va acoperi următoarele aspecte:

- Înțelegerea a ceea ce este un Agent AI - Ce este exact un Agent AI?
- Explorarea a patru diferite framework-uri pentru Agenți AI - Ce le face unice?
- Aplicarea acestor Agenți AI la diferite cazuri de utilizare - Când ar trebui să folosim Agenți AI?

## Obiective de învățare

După parcurgerea acestei lecții, vei putea:

- Explica ce sunt Agenții AI și cum pot fi folosiți.
- Avea o înțelegere a diferențelor dintre unele dintre cele mai populare framework-uri pentru Agenți AI și cum diferă acestea.
- Înțelege cum funcționează Agenții AI pentru a construi aplicații cu ei.

## Ce sunt Agenții AI?

Agenții AI sunt un domeniu foarte interesant în lumea AI Generativ. Cu această entuziasm vine uneori o confuzie de termeni și aplicarea lor. Pentru a păstra lucrurile simple și incluzive pentru majoritatea instrumentelor care se referă la Agenți AI, vom folosi această definiție:

Agenții AI permit modelelor lingvistice mari (LLMs) să îndeplinească sarcini oferindu-le acces la o **stare** și **instrumente**.

![Agent Model](../../../translated_images/what-agent.21f2893bdfd01e6a7fd09b0416c2b15594d97f44bbb2ab5a1ff8bf643d2fcb3d.ro.png)

Să definim acești termeni:

**Modele lingvistice mari** - Acestea sunt modelele menționate pe parcursul acestui curs, cum ar fi GPT-3.5, GPT-4, Llama-2, etc.

**Stare** - Acesta se referă la contextul în care LLM-ul lucrează. LLM-ul folosește contextul acțiunilor sale anterioare și contextul actual, ghidându-și luarea deciziilor pentru acțiunile ulterioare. Framework-urile pentru Agenți AI permit dezvoltatorilor să mențină acest context mai ușor.

**Instrumente** - Pentru a finaliza sarcina pe care utilizatorul a solicitat-o și pe care LLM-ul a planificat-o, LLM-ul are nevoie de acces la instrumente. Câteva exemple de instrumente pot fi o bază de date, un API, o aplicație externă sau chiar un alt LLM!

Aceste definiții sper să îți ofere o bază bună pe măsură ce explorăm cum sunt implementate. Să explorăm câteva diferite framework-uri pentru Agenți AI:

## Agenții LangChain

[Agenții LangChain](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) reprezintă o implementare a definițiilor oferite mai sus.

Pentru a gestiona **starea**, folosește o funcție încorporată numită `AgentExecutor`. Aceasta acceptă `agent` definit și `tools` disponibile.

`Agent Executor` stochează, de asemenea, istoricul chatului pentru a oferi contextul conversației.

![Langchain Agents](../../../translated_images/langchain-agents.edcc55b5d5c437169a2037211284154561183c58bcec6d4ac2f8a79046fac9af.ro.png)

LangChain oferă un [catalog de instrumente](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) care pot fi importate în aplicația ta, la care LLM-ul poate avea acces. Acestea sunt realizate de comunitate și de echipa LangChain.

Poți defini apoi aceste instrumente și să le transmiți către `Agent Executor`.

Vizibilitatea este un alt aspect important când vorbim despre Agenți AI. Este important pentru dezvoltatorii de aplicații să înțeleagă ce instrument folosește LLM-ul și de ce. Pentru asta, echipa de la LangChain a dezvoltat LangSmith.

## AutoGen

Următorul framework pentru Agenți AI pe care îl vom discuta este [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Principala concentrare a AutoGen este conversațiile. Agenții sunt atât **conversabili** cât și **personalizabili**.

**Conversabil -** LLM-urile pot începe și continua o conversație cu un alt LLM pentru a finaliza o sarcină. Acest lucru se realizează prin crearea de `AssistantAgents` și oferindu-le un mesaj specific de sistem.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Personalizabil** - Agenții pot fi definiți nu doar ca LLM-uri, ci și ca utilizatori sau instrumente. Ca dezvoltator, poți defini un `UserProxyAgent` care este responsabil pentru interacțiunea cu utilizatorul pentru feedback în completarea unei sarcini. Acest feedback poate continua executarea sarcinii sau o poate opri.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Stare și Instrumente

Pentru a schimba și gestiona starea, un agent asistent generează cod Python pentru a finaliza sarcina.

Iată un exemplu al procesului:

![AutoGen](../../../translated_images/autogen.dee9a25a45fde584fedd84b812a6e31de5a6464687cdb66bb4f2cb7521391856.ro.png)

#### LLM definit cu un mesaj de sistem

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Aceste mesaje de sistem direcționează acest LLM specific către funcțiile relevante pentru sarcina sa. Amintește-ți, cu AutoGen poți avea mai mulți AssistantAgents definiți cu mesaje de sistem diferite.

#### Chatul este inițiat de utilizator

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Acest mesaj de la user_proxy (Human) este ceea ce va începe procesul agentului de a explora funcțiile posibile pe care ar trebui să le execute.

#### Funcția este executată

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Odată ce chatul inițial este procesat, agentul va trimite instrumentul sugerat pentru a fi apelat. În acest caz, este o funcție numită `get_weather`. Depending on your configuration, this function can be automatically executed and read by the Agent or can be executed based on user input.

You can find a list of [AutoGen code samples](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) to further explore how to get started building.

## Taskweaver

The next agent framework we will explore is [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). It is known as a "code-first" agent because instead of working strictly with `strings` , it can work with DataFrames in Python. This becomes extremely useful for data analysis and generation tasks. This can be things like creating graphs and charts or generating random numbers.

### State and Tools

To manage the state of the conversation, TaskWeaver uses the concept of a `Planner`. The `Planner` is a LLM that takes the request from the users and maps out the tasks that need to be completed to fulfill this request.

To complete the tasks the `Planner` is exposed to the collection of tools called `Plugins`. Acestea pot fi clase Python sau un interpret de cod general. Aceste plugin-uri sunt stocate ca embeddings pentru ca LLM-ul să poată căuta mai bine pluginul corect.

![Taskweaver](../../../translated_images/taskweaver.da8559999267715a95b7677cf9b7d7dd8420aee6f3c484ced1833f081988dcd5.ro.png)

Iată un exemplu de plugin pentru gestionarea detectării anomaliilor:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Codul este verificat înainte de a fi executat. O altă caracteristică pentru gestionarea contextului în Taskweaver este `experience`. Experience allows for the context of a conversation to be stored over to the long term in a YAML file. This can be configured so that the LLM improves over time on certain tasks given that it is exposed to prior conversations.

## JARVIS

The last agent framework we will explore is [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file?WT.mc_id=academic-105485-koreyst). What makes JARVIS unique is that it uses an LLM to manage the `state` al conversației și `tools` sunt alte modele AI. Fiecare dintre modelele AI sunt modele specializate care îndeplinesc anumite sarcini, cum ar fi detectarea obiectelor, transcrierea sau descrierea imaginilor.

![JARVIS](../../../translated_images/jarvis.762ddbadbd1a3a3364d4ca3db1a7a9c0d2180060c0f8da6f7bd5b5ea2a115aa7.ro.png)

LLM-ul, fiind un model cu scop general, primește cererea de la utilizator și identifică sarcina specifică și orice argumente/date necesare pentru a finaliza sarcina.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM-ul apoi formatează cererea într-un mod pe care modelul AI specializat îl poate interpreta, cum ar fi JSON. Odată ce modelul AI a returnat predicția sa bazată pe sarcină, LLM-ul primește răspunsul.

Dacă sunt necesare mai multe modele pentru a finaliza sarcina, va interpreta și răspunsul de la acele modele înainte de a le aduce împreună pentru a genera răspunsul către utilizator.

Exemplul de mai jos arată cum ar funcționa acest lucru când un utilizator solicită o descriere și numărul obiectelor dintr-o imagine:

## Temă

Pentru a continua învățarea despre Agenții AI, poți construi cu AutoGen:

- O aplicație care simulează o întâlnire de afaceri cu diferite departamente ale unei startup-uri din domeniul educației.
- Creează mesaje de sistem care ghidează LLM-urile în înțelegerea diferitelor persoane și priorități și permit utilizatorului să propună o idee de produs nou.
- LLM-ul ar trebui apoi să genereze întrebări de urmărire din fiecare departament pentru a rafina și îmbunătăți propunerea și ideea de produs.

## Învățarea nu se oprește aici, continuă călătoria

După ce ai finalizat această lecție, verifică colecția noastră [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a continua să îți îmbunătățești cunoștințele despre AI Generativ!

**Declinări de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți de faptul că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa de autoritate. Pentru informații critice, se recomandă traducerea umană profesională. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.