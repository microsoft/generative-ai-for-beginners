[![Agenci AI](../../images/17-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson17-gh?WT.mc_id=academic-105485-koreyst)

## Wprowadzenie

Agenci AI stanowią ekscytujący rozwój w dziedzinie Generatywnej AI, umożliwiając Dużym Modelom Językowym (LLM) ewolucję z asystentów w agentów zdolnych do podejmowania działań. Frameworki Agentów AI umożliwiają programistom tworzenie aplikacji, które dają LLM dostęp do narzędzi i zarządzania stanem. Frameworki te zwiększają również widoczność, pozwalając użytkownikom i programistom monitorować działania planowane przez LLM, co poprawia zarządzanie doświadczeniem.

Lekcja obejmie następujące obszary:

- Zrozumienie, czym jest Agent AI - Czym dokładnie jest Agent AI?
- Odkrywanie czterech różnych Frameworków Agentów AI - Co czyni je wyjątkowymi?
- Zastosowanie tych Agentów AI do różnych przypadków użycia - Kiedy powinniśmy używać Agentów AI?

## Cele nauki

Po ukończeniu tej lekcji będziesz potrafił:

- Wyjaśnić, czym są Agenci AI i jak mogą być używani.
- Rozumieć różnice między niektórymi popularnymi Frameworkami Agentów AI i czym się różnią.
- Zrozumieć, jak funkcjonują Agenci AI, aby budować z nimi aplikacje.

## Czym są Agenci AI?

Agenci AI to bardzo ekscytująca dziedzina w świecie Generatywnej AI. Z tym podekscytowaniem wiąże się czasem zamieszanie w terminologii i jej zastosowaniu. Aby uprościć sprawę i objąć większość narzędzi odnoszących się do Agentów AI, będziemy używać następującej definicji:

Agenci AI pozwalają Dużym Modelom Językowym (LLM) wykonywać zadania, dając im dostęp do **stanu** i **narzędzi**.

![Model Agenta](../../images/what-agent.png?WT.mc_id=academic-105485-koreyst)

Zdefiniujmy te terminy:

**Duże Modele Językowe** - Są to modele, o których mowa w całym tym kursie, takie jak GPT-3.5, GPT-4, Llama-2 itp.

**Stan** - Odnosi się do kontekstu, w którym działa LLM. LLM wykorzystuje kontekst swoich przeszłych działań i bieżący kontekst, kierując podejmowaniem decyzji dotyczących kolejnych działań. Frameworki Agentów AI ułatwiają programistom utrzymanie tego kontekstu.

**Narzędzia** - Aby ukończyć zadanie zlecone przez użytkownika i zaplanowane przez LLM, LLM potrzebuje dostępu do narzędzi. Przykładami narzędzi mogą być baza danych, API, zewnętrzna aplikacja, a nawet inny LLM!

Mamy nadzieję, że te definicje dadzą Ci dobre podstawy w dalszej części, gdy przyjrzymy się, jak są one wdrażane. Zbadajmy kilka różnych frameworków Agentów AI:

## Agenci LangChain

[Agenci LangChain](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) to implementacja definicji, które przedstawiliśmy powyżej.

Aby zarządzać **stanem**, używa wbudowanej funkcji o nazwie `AgentExecutor`. Akceptuje ona zdefiniowanego `agenta` i `narzędzia`, które są dla niego dostępne.

`AgentExecutor` przechowuje również historię czatu, aby zapewnić kontekst rozmowy.

![Agenci Langchain](../../images/langchain-agents.png?WT.mc_id=academic-105485-koreyst)

LangChain oferuje [katalog narzędzi](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst), które można zaimportować do aplikacji, do których LLM może uzyskać dostęp. Są one tworzone przez społeczność i zespół LangChain.

Następnie możesz zdefiniować te narzędzia i przekazać je do `AgentExecutor`.

Widoczność to kolejny ważny aspekt, gdy mówimy o Agentach AI. Ważne jest, aby twórcy aplikacji rozumieli, którego narzędzia używa LLM i dlaczego. W tym celu zespół LangChain opracował LangSmith.

## AutoGen

Następnym frameworkiem Agentów AI, który omówimy, jest [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Głównym celem AutoGen są konwersacje. Agenci są zarówno **konwersacyjni**, jak i **konfigurowalni**.

**Konwersacyjni -** LLM mogą rozpoczynać i kontynuować rozmowę z innym LLM w celu ukończenia zadania. Odbywa się to poprzez tworzenie `AssistantAgents` i nadawanie im określonej wiadomości systemowej.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Kreatywny w pomysłach na produkty oprogramowania.", llm_config=llm_config, )

```

**Konfigurowalni** - Agenci mogą być definiowani nie tylko jako LLM, ale także jako użytkownik lub narzędzie. Jako programista możesz zdefiniować `UserProxyAgent`, który jest odpowiedzialny za interakcję z użytkownikiem w celu uzyskania informacji zwrotnej podczas wykonywania zadania. Ta informacja zwrotna może kontynuować wykonywanie zadania lub je zatrzymać.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Stan i Narzędzia

Aby zmienić i zarządzać stanem, Agent Asystent generuje kod Pythona w celu ukończenia zadania.

Oto przykład procesu:

![AutoGen](../../images/autogen.png?WT.mc_id=academic-105485-koreyst)

#### LLM Zdefiniowany za pomocą Wiadomości Systemowej

```python
system_message="W przypadku zadań związanych z pogodą używaj tylko funkcji, które zostały Ci udostępnione. Odpowiedz TERMINATE, gdy zadanie zostanie zakończone."
```

Ta wiadomość systemowa kieruje konkretny LLM do funkcji istotnych dla jego zadania. Pamiętaj, że w AutoGen możesz mieć wiele zdefiniowanych AssistantAgents z różnymi wiadomościami systemowymi.

#### Czat jest Inicjowany przez Użytkownika

```python
user_proxy.initiate_chat( chatbot, message="Planuję wycieczkę do Nowego Jorku w przyszłym tygodniu, czy możesz mi pomóc wybrać ubrania? ", )

```

Ta wiadomość od user_proxy (Człowieka) jest tym, co rozpocznie proces eksploracji przez Agenta możliwych funkcji, które powinien wykonać.

#### Funkcja jest Wykonywana

```bash
chatbot (do user_proxy):

***** Sugerowane wywołanie narzędzia: get_weather ***** Argumenty: {"location":"Nowy Jork, NY","time_periond:"7","temperature_unit":"Celsjusz"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> WYKONYWANIE FUNKCJI get_weather... user_proxy (do chatbot): ***** Odpowiedź z wywołania funkcji "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Po przetworzeniu początkowego czatu Agent wyśle sugerowane narzędzie do wywołania. W tym przypadku jest to funkcja o nazwie `get_weather`. W zależności od konfiguracji, ta funkcja może być automatycznie wykonywana i odczytywana przez Agenta lub może być wykonywana na podstawie danych wejściowych użytkownika.

Listę [próbek kodu AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) znajdziesz, aby dalej eksplorować, jak zacząć budować.

## Taskweaver

Następnym frameworkiem agentów, który zbadamy, jest [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Jest znany jako agent "code-first", ponieważ zamiast pracować wyłącznie z `stringami`, może pracować z DataFrame w Pythonie. Staje się to niezwykle przydatne w zadaniach analizy i generowania danych. Mogą to być rzeczy takie jak tworzenie wykresów i diagramów lub generowanie liczb losowych.

### Stan i Narzędzia

Aby zarządzać stanem konwersacji, TaskWeaver wykorzystuje koncepcję `Plannera`. `Planner` to LLM, który przyjmuje żądanie od użytkowników i planuje zadania, które należy wykonać, aby spełnić to żądanie.

Aby ukończyć zadania, `Planner` ma dostęp do kolekcji narzędzi zwanych `Pluginami`. Mogą to być klasy Pythona lub ogólny interpreter kodu. Te pluginy są przechowywane jako embeddingi, aby LLM mógł lepiej wyszukać odpowiedni plugin.

![Taskweaver](../../images/taskweaver.png?WT.mc_id=academic-105485-koreyst)

Oto przykład pluginu do obsługi wykrywania anomalii:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Kod jest weryfikowany przed wykonaniem. Inną funkcją do zarządzania kontekstem w Taskweaver jest `experience`. Experience pozwala na przechowywanie kontekstu konwersacji długoterminowo w pliku YAML. Można to skonfigurować tak, aby LLM poprawiał się z czasem w określonych zadaniach, biorąc pod uwagę wcześniejsze konwersacje.

## JARVIS

Ostatnim frameworkiem agentów, który zbadamy, jest [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file?WT.mc_id=academic-105485-koreyst). To, co czyni JARVIS wyjątkowym, to fakt, że używa LLM do zarządzania `stanem` konwersacji, a `narzędziami` są inne modele AI. Każdy z modeli AI to wyspecjalizowane modele wykonujące określone zadania, takie jak wykrywanie obiektów, transkrypcja czy tworzenie podpisów pod obrazami.

![JARVIS](../../images/jarvis.png?WT.mc_id=academic-105485-koreyst)

LLM, będąc modelem ogólnego przeznaczenia, odbiera żądanie od użytkownika i identyfikuje konkretne zadanie oraz wszelkie argumenty/dane potrzebne do jego wykonania.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

Następnie LLM formatuje żądanie w sposób, który wyspecjalizowany model AI może zinterpretować, na przykład w formacie JSON. Gdy model AI zwróci swoją predykcję na podstawie zadania, LLM odbiera odpowiedź.

Jeśli do wykonania zadania wymagane jest wiele modeli, zinterpretuje również odpowiedzi z tych modeli, zanim połączy je w celu wygenerowania odpowiedzi dla użytkownika.

Poniższy przykład pokazuje, jak to działa, gdy użytkownik prosi o opis i liczbę obiektów na zdjęciu:

## Zadanie

Aby kontynuować naukę o Agentach AI, możesz zbudować za pomocą AutoGen:

- Aplikację symulującą spotkanie biznesowe z różnymi działami startupu edukacyjnego.
- Stwórz wiadomości systemowe, które kierują LLM w zrozumieniu różnych person i priorytetów, i umożliwiają użytkownikowi przedstawienie nowego pomysłu na produkt.
- Następnie LLM powinien wygenerować pytania uzupełniające z każdego działu, aby dopracować i ulepszyć prezentację oraz pomysł na produkt.

## Nauka się tu nie kończy, kontynuuj Podróż

Po ukończeniu tej lekcji sprawdź naszą [Kolekcję Nauki o Generatywnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej podnosić swoją wiedzę o Generatywnej AI!
