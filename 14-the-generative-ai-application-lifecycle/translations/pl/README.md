# Cykl życia aplikacji generatywnej AI

[![Integracja z wywołaniami funkcji](../../images/14-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson14-gh?WT.mc_id=academic-105485-koreyst)

Ważnym pytaniem dla wszystkich aplikacji AI jest istotność funkcji AI, ponieważ AI to szybko rozwijająca się dziedzina. Aby zapewnić, że Twoja aplikacja pozostanie istotna, niezawodna i odporna, musisz ją stale monitorować, oceniać i ulepszać. Tutaj wkracza cykl życia generatywnej AI.

Cykl życia generatywnej AI to ramy, które prowadzą Cię przez etapy tworzenia, wdrażania i utrzymania aplikacji generatywnej AI. Pomaga Ci zdefiniować cele, mierzyć wydajność, identyfikować wyzwania i wdrażać rozwiązania. Pomaga również dostosować aplikację do standardów etycznych i prawnych Twojej domeny i interesariuszy. Podążając za cyklem życia generatywnej AI, możesz zapewnić, że Twoja aplikacja zawsze dostarcza wartość i satysfakcjonuje użytkowników.

## Wprowadzenie

W tym rozdziale:

- Zrozumiesz zmianę paradygmatu z MLOps na LLMOps
- Cykl życia LLM
- Narzędzia cyklu życia
- Metryki i ocena cyklu życia

## Zrozumienie zmiany paradygmatu z MLOps na LLMOps

LLM są nowym narzędziem w arsenale Sztucznej Inteligencji, są niezwykle potężne w zadaniach analizy i generowania dla aplikacji, jednak ta moc ma pewne konsekwencje w sposobie usprawniania zadań AI i klasycznego uczenia maszynowego.

W związku z tym potrzebujemy nowego paradygmatu, aby dostosować to narzędzie w dynamiczny sposób, z odpowiednimi zachętami. Możemy kategoryzować starsze aplikacje AI jako "Aplikacje ML" i nowsze Aplikacje AI jako "Aplikacje GenAI" lub po prostu "Aplikacje AI", odzwierciedlając dominującą technologię i techniki stosowane w danym czasie. Zmienia to naszą narrację na wiele sposobów, spójrz na poniższe porównanie.

![Porównanie LLMOps vs. MLOps](../../images/01-llmops-shift.png?WT.mc_id=academic-105485-koreys)

Zauważ, że w LLMOps bardziej koncentrujemy się na programistach aplikacji, wykorzystując integracje jako kluczowy punkt, używając "Modele-jako-Usługa" i myśląc o następujących punktach dla metryk.

- Jakość: Jakość odpowiedzi
- Szkoda: Odpowiedzialna AI
- Uczciwość: Ugruntowanie odpowiedzi (Czy ma sens? Czy jest poprawna?)
- Koszt: Budżet rozwiązania
- Opóźnienie: Średni czas odpowiedzi na token

## Cykl życia LLM

Najpierw, aby zrozumieć cykl życia i modyfikacje, zwróć uwagę na następującą infografikę.

![Infografika LLMOps](../../images/02-llmops.png?WT.mc_id=academic-105485-koreys)

Jak możesz zauważyć, różni się to od zwykłych cykli życia z MLOps. LLM mają wiele nowych wymagań, takich jak Inżynieria Promptów, różne techniki poprawy jakości (Dostrajanie, RAG, Meta-Prompty), inna ocena i odpowiedzialność w ramach odpowiedzialnej AI, wreszcie nowe metryki oceny (Jakość, Szkoda, Uczciwość, Koszt i Opóźnienie).

Na przykład, spójrz, jak tworzymy koncepcję. Używając inżynierii promptów do eksperymentowania z różnymi LLM, aby zbadać możliwości sprawdzenia, czy ich hipoteza może być poprawna.

Zauważ, że nie jest to proces liniowy, ale zintegrowane pętle, iteracyjne i z nadrzędnym cyklem.

Jak moglibyśmy zbadać te kroki? Przejdźmy do szczegółów, jak moglibyśmy zbudować cykl życia.

![Przepływ pracy LLMOps](../../images/03-llm-stage-flows.png?WT.mc_id=academic-105485-koreys)

Może to wyglądać nieco skomplikowanie, skupmy się najpierw na trzech dużych krokach.

1. Tworzenie koncepcji/Eksploracja: Eksploracja, tutaj możemy eksplorować zgodnie z naszymi potrzebami biznesowymi. Prototypowanie, tworzenie [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) i testowanie, czy jest wystarczająco wydajny dla naszej Hipotezy.
2. Budowanie/Rozszerzanie: Implementacja, teraz zaczynamy oceniać dla większych zbiorów danych, wdrażać techniki, takie jak Dostrajanie i RAG, aby sprawdzić solidność naszego rozwiązania. Jeśli to nie działa, ponowne wdrożenie, dodanie nowych kroków w naszym przepływie lub restrukturyzacja danych może pomóc. Po przetestowaniu naszego przepływu i skali, jeśli działa i sprawdzimy nasze Metryki, jest gotowe do następnego kroku.
3. Operacjonalizacja: Integracja, teraz dodawanie systemów monitorowania i alertów do naszego systemu, wdrażanie i integracja aplikacji z naszą Aplikacją.

Następnie mamy nadrzędny cykl Zarządzania, koncentrujący się na bezpieczeństwie, zgodności i zarządzaniu.

Gratulacje, teraz masz gotową do użycia i operacyjną aplikację AI. Aby zdobyć praktyczne doświadczenie, spójrz na [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

Teraz, jakich narzędzi moglibyśmy użyć?

## Narzędzia cyklu życia

Jeśli chodzi o narzędzia, Microsoft dostarcza [Platformę Azure AI](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) i [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst), które ułatwiają i przyspieszają implementację cyklu.

[Platforma Azure AI](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) pozwala korzystać z [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys). AI Studio to portal internetowy umożliwiający eksplorację modeli, próbek i narzędzi. Zarządzanie zasobami, przepływami tworzenia interfejsu użytkownika oraz opcje SDK/CLI dla rozwoju Code-First.

![Możliwości Azure AI](../../images/04-azure-ai-platform.png?WT.mc_id=academic-105485-koreys)

Azure AI pozwala korzystać z wielu zasobów do zarządzania operacjami, usługami, projektami, wyszukiwaniem wektorowym i potrzebami bazodanowymi.

![LLMOps z Azure AI](../../images/05-llm-azure-ai-prompt.png?WT.mc_id=academic-105485-koreys)

Konstruuj, od dowodu koncepcji (POC) aż po aplikacje na dużą skalę za pomocą PromptFlow:

- Projektuj i buduj aplikacje z VS Code, za pomocą narzędzi wizualnych i funkcjonalnych
- Testuj i dostrajaj swoje aplikacje dla jakościowej AI, z łatwością.
- Używaj Azure AI Studio do integracji i iteracji z chmurą, wypychaj i wdrażaj dla szybkiej integracji.

![LLMOps z PromptFlow](../../images/06-llm-promptflow.png?WT.mc_id=academic-105485-koreys)

## Świetnie! Kontynuuj naukę!

Niesamowite, teraz dowiedz się więcej o tym, jak strukturyzujemy aplikację, aby wykorzystać te koncepcje w [Aplikacji Contoso Chat](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys), aby sprawdzić, jak Cloud Advocacy dodaje te koncepcje w demonstracjach. Aby uzyskać więcej treści, sprawdź naszą [sesję breakout na Ignite!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Teraz sprawdź Lekcję 15, aby zrozumieć, jak [Retrieval Augmented Generation i Bazy Danych Wektorowe](../../../15-rag-and-vector-databases/translations/pl/README.md?WT.mc_id=academic-105485-koreyst) wpływają na Generatywną AI i jak tworzyć bardziej angażujące aplikacje!
