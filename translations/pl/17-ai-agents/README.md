<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8e8d1f6a63da606af7176a87ff8e92b6",
  "translation_date": "2025-10-18T00:58:48+00:00",
  "source_file": "17-ai-agents/README.md",
  "language_code": "pl"
}
-->
[![Modele Open Source](../../../translated_images/17-lesson-banner.a5b918fb0920e4e6d8d391a100f5cb1d5929f4c2752c937d40392905dec82592.pl.png)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Wprowadzenie

Agent AI to ekscytujący rozwój w dziedzinie Generative AI, który pozwala dużym modelom językowym (LLM) ewoluować z asystentów w agentów zdolnych do podejmowania działań. Frameworki Agentów AI umożliwiają programistom tworzenie aplikacji, które dają LLM dostęp do narzędzi i zarządzania stanem. Te frameworki zwiększają również przejrzystość, umożliwiając użytkownikom i programistom monitorowanie działań planowanych przez LLM, co poprawia zarządzanie doświadczeniem.

Lekcja obejmie następujące obszary:

- Zrozumienie, czym jest Agent AI - Czym dokładnie jest Agent AI?
- Eksploracja czterech różnych frameworków Agentów AI - Co je wyróżnia?
- Zastosowanie tych Agentów AI w różnych przypadkach użycia - Kiedy powinniśmy używać Agentów AI?

## Cele nauki

Po ukończeniu tej lekcji będziesz w stanie:

- Wyjaśnić, czym są Agenci AI i jak można ich używać.
- Zrozumieć różnice między niektórymi popularnymi frameworkami Agentów AI i jak się od siebie różnią.
- Zrozumieć, jak działają Agenci AI, aby móc budować aplikacje z ich wykorzystaniem.

## Czym są Agenci AI?

Agenci AI to bardzo ekscytująca dziedzina w świecie Generative AI. Z tym entuzjazmem czasami wiąże się zamieszanie dotyczące terminów i ich zastosowania. Aby uprościć sprawę i uwzględnić większość narzędzi odnoszących się do Agentów AI, użyjemy następującej definicji:

Agenci AI pozwalają dużym modelom językowym (LLM) wykonywać zadania, dając im dostęp do **stanu** i **narzędzi**.

![Model Agenta](../../../translated_images/what-agent.21f2893bdfd01e6a7fd09b0416c2b15594d97f44bbb2ab5a1ff8bf643d2fcb3d.pl.png)

Zdefiniujmy te terminy:

**Duże modele językowe** - Są to modele, o których mowa w całym kursie, takie jak GPT-3.5, GPT-4, Llama-2 itd.

**Stan** - Odnosi się do kontekstu, w którym działa LLM. LLM wykorzystuje kontekst swoich wcześniejszych działań oraz bieżący kontekst, aby kierować podejmowaniem decyzji w kolejnych działaniach. Frameworki Agentów AI umożliwiają programistom łatwiejsze utrzymanie tego kontekstu.

**Narzędzia** - Aby wykonać zadanie, które użytkownik zlecił, a które LLM zaplanował, LLM potrzebuje dostępu do narzędzi. Przykłady narzędzi to baza danych, API, zewnętrzna aplikacja, a nawet inny LLM!

Te definicje powinny dać Ci solidne podstawy na przyszłość, gdy będziemy badać, jak są one wdrażane. Przyjrzyjmy się kilku różnym frameworkom Agentów AI:

## Agenci LangChain

[Agenci LangChain](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) to implementacja definicji, które podaliśmy powyżej.

Aby zarządzać **stanem**, używa wbudowanej funkcji o nazwie `AgentExecutor`. Akceptuje ona zdefiniowanego `agenta` oraz dostępne dla niego `narzędzia`.

`AgentExecutor` przechowuje również historię czatu, aby zapewnić kontekst rozmowy.

![Agenci LangChain](../../../translated_images/langchain-agents.edcc55b5d5c437169a2037211284154561183c58bcec6d4ac2f8a79046fac9af.pl.png)

LangChain oferuje [katalog narzędzi](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst), które można zaimportować do swojej aplikacji, w której LLM może uzyskać do nich dostęp. Są one tworzone przez społeczność oraz zespół LangChain.

Możesz następnie zdefiniować te narzędzia i przekazać je do `AgentExecutor`.

Widoczność to kolejny ważny aspekt w rozmowach o Agentach AI. Ważne jest, aby programiści aplikacji rozumieli, z którego narzędzia korzysta LLM i dlaczego. W tym celu zespół LangChain opracował LangSmith.

## AutoGen

Kolejny framework Agentów AI, który omówimy, to [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Głównym celem AutoGen są rozmowy. Agenci są zarówno **rozmowni**, jak i **dostosowywalni**.

**Rozmowni -** LLM mogą rozpocząć i kontynuować rozmowę z innym LLM, aby wykonać zadanie. Odbywa się to poprzez tworzenie `AssistantAgents` i nadawanie im określonej wiadomości systemowej.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Dostosowywalni** - Agenci mogą być definiowani nie tylko jako LLM, ale także jako użytkownik lub narzędzie. Jako programista możesz zdefiniować `UserProxyAgent`, który odpowiada za interakcję z użytkownikiem w celu uzyskania informacji zwrotnej potrzebnej do wykonania zadania. Informacja zwrotna może kontynuować wykonanie zadania lub je zatrzymać.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Stan i Narzędzia

Aby zmieniać i zarządzać stanem, asystent Agent generuje kod Python do wykonania zadania.

Oto przykład procesu:

![AutoGen](../../../translated_images/autogen.dee9a25a45fde584fedd84b812a6e31de5a6464687cdb66bb4f2cb7521391856.pl.png)

#### LLM zdefiniowany za pomocą wiadomości systemowej

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Ta wiadomość systemowa kieruje konkretny LLM do funkcji, które są istotne dla jego zadania. Pamiętaj, że w AutoGen możesz mieć wiele zdefiniowanych AssistantAgents z różnymi wiadomościami systemowymi.

#### Rozmowa inicjowana przez użytkownika

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Ta wiadomość od user_proxy (Człowieka) rozpoczyna proces, w którym Agent bada możliwe funkcje, które powinien wykonać.

#### Funkcja jest wykonywana

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Po przetworzeniu początkowej rozmowy Agent zasugeruje narzędzie do użycia. W tym przypadku jest to funkcja o nazwie `get_weather`. W zależności od konfiguracji, funkcja ta może być automatycznie wykonana i odczytana przez Agenta lub wykonana na podstawie danych wejściowych użytkownika.

Możesz znaleźć listę [przykładów kodu AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst), aby dalej zgłębiać, jak rozpocząć budowanie.

## Taskweaver

Kolejny framework agenta, który zbadamy, to [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Jest znany jako agent "code-first", ponieważ zamiast pracować wyłącznie z `ciągami znaków`, może pracować z DataFrames w Pythonie. Jest to niezwykle przydatne w analizie danych i zadaniach generacyjnych, takich jak tworzenie wykresów i diagramów czy generowanie losowych liczb.

### Stan i Narzędzia

Aby zarządzać stanem rozmowy, TaskWeaver używa koncepcji `Plannera`. `Planner` to LLM, który przyjmuje żądanie od użytkowników i planuje zadania, które muszą zostać wykonane, aby je zrealizować.

Aby wykonać zadania, `Planner` ma dostęp do kolekcji narzędzi zwanych `Plugins`. Mogą to być klasy Pythona lub ogólny interpreter kodu. Te pluginy są przechowywane jako osadzenia, aby LLM mógł lepiej wyszukiwać odpowiedni plugin.

![Taskweaver](../../../translated_images/taskweaver.da8559999267715a95b7677cf9b7d7dd8420aee6f3c484ced1833f081988dcd5.pl.png)

Oto przykład pluginu do wykrywania anomalii:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Kod jest weryfikowany przed wykonaniem. Kolejną funkcją zarządzania kontekstem w Taskweaver jest `experience`. Experience pozwala na przechowywanie kontekstu rozmowy w dłuższej perspektywie w pliku YAML. Można to skonfigurować tak, aby LLM poprawiał się z czasem w określonych zadaniach, biorąc pod uwagę wcześniejsze rozmowy.

## JARVIS

Ostatni framework agenta, który zbadamy, to [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file?WT.mc_id=academic-105485-koreyst). To, co wyróżnia JARVIS, to fakt, że używa LLM do zarządzania `stanem` rozmowy, a `narzędzia` to inne modele AI. Każdy z modeli AI to wyspecjalizowany model, który wykonuje określone zadania, takie jak wykrywanie obiektów, transkrypcja czy opisywanie obrazów.

![JARVIS](../../../translated_images/jarvis.762ddbadbd1a3a3364d4ca3db1a7a9c0d2180060c0f8da6f7bd5b5ea2a115aa7.pl.png)

LLM, będąc modelem ogólnego przeznaczenia, otrzymuje żądanie od użytkownika i identyfikuje konkretne zadanie oraz wszelkie argumenty/dane potrzebne do jego wykonania.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM następnie formatuje żądanie w sposób, który wyspecjalizowany model AI może zinterpretować, na przykład w formacie JSON. Po tym, jak model AI zwróci swoją predykcję na podstawie zadania, LLM otrzymuje odpowiedź.

Jeśli do wykonania zadania wymagane są wiele modeli, LLM również interpretuje odpowiedzi od tych modeli, zanim połączy je w jedną odpowiedź dla użytkownika.

Poniższy przykład pokazuje, jak to działa, gdy użytkownik prosi o opis i liczbę obiektów na zdjęciu:

## Zadanie

Aby kontynuować naukę o Agentach AI, możesz zbudować aplikację z AutoGen:

- Aplikację symulującą spotkanie biznesowe różnych działów startupu edukacyjnego.
- Stwórz wiadomości systemowe, które pomogą LLM zrozumieć różne role i priorytety oraz umożliwią użytkownikowi przedstawienie nowego pomysłu na produkt.
- LLM powinien następnie generować pytania uzupełniające od każdego działu, aby dopracować i ulepszyć pomysł na produkt.

## Nauka się nie kończy, kontynuuj podróż

Po ukończeniu tej lekcji, sprawdź naszą [kolekcję nauki o Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej rozwijać swoją wiedzę o Generative AI!

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.