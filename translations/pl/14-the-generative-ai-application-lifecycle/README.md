[![Integracja z wywoływaniem funkcji](../../../translated_images/pl/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Cykl życia aplikacji generatywnej AI

Ważnym pytaniem dla wszystkich aplikacji AI jest znaczenie funkcji AI, ponieważ AI to szybko rozwijająca się dziedzina, aby Twoja aplikacja pozostała aktualna, niezawodna i solidna, musisz ją stale monitorować, oceniać i ulepszać. W tym pomaga cykl życia generatywnej AI.

Cykl życia generatywnej AI to ramy, które prowadzą Cię przez etapy opracowywania, wdrażania i utrzymywania aplikacji generatywnej AI. Pomaga określić cele, mierzyć wyniki, identyfikować wyzwania i wdrażać rozwiązania. Pomaga również dostosować aplikację do etycznych i prawnych standardów Twojej dziedziny i interesariuszy. Przestrzegając cyklu życia generatywnej AI, możesz zapewnić, że aplikacja zawsze dostarcza wartości i zadowala użytkowników.

## Wprowadzenie

W tym rozdziale:

- Zrozumiesz zmianę paradygmatu z MLOps na LLMOps
- Cykl życia LLM
- Narzędzia cyklu życia
- Metrifikacja i ocena cyklu życia

## Zrozum zmianę paradygmatu z MLOps na LLMOps

LLM są nowym narzędziem w arsenale sztucznej inteligencji, są niesamowicie potężne w zadaniach analizy i generowania dla aplikacji, jednak ta moc ma pewne konsekwencje dla optymalizacji zadań AI i klasycznego uczenia maszynowego.

Potrzebujemy nowego paradygmatu, aby dostosować to narzędzie dynamicznie, z odpowiednimi zachętami. Możemy kategoryzować starsze aplikacje AI jako "ML Apps", a nowsze jako "GenAI Apps" lub po prostu "AI Apps", odzwierciedlając mainstreamowe technologie i techniki używane w danym czasie. To zmienia naszą narrację na wiele sposobów, spójrz na poniższe porównanie.

![Porównanie LLMOps vs. MLOps](../../../translated_images/pl/01-llmops-shift.29bc933cb3bb0080.webp)

Zauważ, że w LLMOps bardziej skupiamy się na deweloperach aplikacji, używając integracji jako kluczowego punktu, korzystając z "Modeli jako usługi" i myśląc o następujących punktach metryk.

- Jakość: Jakość odpowiedzi
- Szkoda: Odpowiedzialna AI
- Uczciwość: Podstawy odpowiedzi (Czy ma sens? Czy jest poprawna?)
- Koszt: Budżet rozwiązania
- Opóźnienie: Śr. czas odpowiedzi na token

## Cykl życia LLM

Najpierw, aby zrozumieć cykl życia i zmiany, zwróć uwagę na następującą infografikę.

![Infografika LLMOps](../../../translated_images/pl/02-llmops.70a942ead05a7645.webp)

Jak zauważysz, jest to inne niż zwykłe cykle życia w MLOps. LLM mają wiele nowych wymagań, takich jak promptowanie, różne techniki poprawy jakości (Fine-Tuning, RAG, Meta-Prompts), różnorodna ocena i odpowiedzialność związana z odpowiedzialną AI, a także nowe metryki oceny (Jakość, Szkoda, Uczciwość, Koszt i Opóźnienie).

Na przykład spójrz, jak tworzymy pomysły. Używając inżynierii promptów do eksperymentowania z różnymi LLM, aby badać możliwości i testować, czy ich Hipoteza może być poprawna.

Zauważ, że nie jest to proces liniowy, ale zintegrowane pętle, iteracyjne, z nadrzędnym cyklem.

Jak możemy zbadać te kroki? Prześledźmy szczegóły, jak zbudować cykl życia.

![Workflow LLMOps](../../../translated_images/pl/03-llm-stage-flows.3a1e1c401235a6cf.webp)

Może to wyglądać trochę skomplikowanie, skupmy się najpierw na trzech głównych krokach.

1. Generowanie/Badanie: Eksploracja, tutaj możemy badać zgodnie z naszymi potrzebami biznesowymi. Prototypowanie, tworzenie [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) i testowanie, czy jest wystarczająco wydajny dla naszej Hipotezy.
1. Budowanie/Uzupełnianie: Implementacja, teraz zaczynamy oceniać większe zbiory danych, wdrażać techniki takie jak Fine-tuning i RAG, aby sprawdzić solidność naszego rozwiązania. Jeśli to nie działa, ponowna implementacja, dodanie nowych kroków w naszym procesie lub restrukturyzacja danych mogą pomóc. Po przetestowaniu naszego procesu i skali, jeśli działa i spełnia metryki, jest gotowe do następnego kroku.
1. Operacjonalizacja: Integracja, teraz dodając Systemy Monitoringu i Alertów do naszego systemu, wdrożenie i integrację aplikacji z naszą Aplikacją.

Następnie mamy nadrzędny cykl Zarządzania, skupiający się na bezpieczeństwie, zgodności i zarządzaniu.

Gratulacje, teraz masz swoją aplikację AI gotową do działania i operacyjną. Aby zdobyć praktyczne doświadczenie, sprawdź [Demonstrację czatu Contoso.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)

A jakie narzędzia możemy użyć?

## Narzędzia cyklu życia

Microsoft oferuje [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) i [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst), które ułatwiają i sprawiają, że Twój cykl jest łatwy do wdrożenia i gotowy do pracy.

[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) pozwala korzystać z [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst). Microsoft Foundry (dawniej Azure AI Studio) to portal internetowy, który pozwala eksplorować modele, przykłady i narzędzia, zarządzać zasobami oraz korzystać z przepływów UI i opcji SDK/CLI do rozwoju Code-First.

![Możliwości Azure AI](../../../translated_images/pl/04-azure-ai-platform.80203baf03a12fa8.webp)

Azure AI pozwala korzystać z wielu zasobów do zarządzania operacjami, usługami, projektami, zapytaniami wektorowymi i bazami danych.

![LLMOps z Azure AI](../../../translated_images/pl/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

Twórz od Proof-of-Concept (POC) aż po aplikacje na dużą skalę z PromptFlow:

- Projektuj i twórz aplikacje z VS Code, z narzędziami wizualnymi i funkcjonalnymi
- Testuj i dostrajaj swoje aplikacje dla jakości AI, łatwo i szybko.
- Używaj Microsoft Foundry do integracji i iteracji z chmurą, push i wdrażaniem dla szybkiej integracji.

![LLMOps z PromptFlow](../../../translated_images/pl/06-llm-promptflow.a183eba07a3a7fdf.webp)

## Świetnie! Kontynuuj naukę!

Niesamowite, teraz dowiedz się więcej o tym, jak strukturujemy aplikację, aby użyć tych koncepcji z [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), aby zobaczyć, jak Cloud Advocacy dodaje te koncepcje w demonstracjach. Aby uzyskać więcej treści, sprawdź naszą [sesję Ignite!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Teraz przejdź do lekcji 15, aby zrozumieć, jak [Retrieval Augmented Generation i bazy danych wektorów](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) wpływają na Generatywne AI i tworzą bardziej angażujące aplikacje!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->