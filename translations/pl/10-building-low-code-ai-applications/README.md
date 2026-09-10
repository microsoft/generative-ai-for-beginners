# Tworzenie aplikacji AI niskokodowych

[![Tworzenie aplikacji AI niskokodowych](../../../translated_images/pl/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(Kliknij powyższy obraz, aby obejrzeć wideo z tej lekcji)_

## Wprowadzenie

Teraz, gdy nauczyliśmy się tworzyć aplikacje generujące obrazy, porozmawiajmy o niskokodzie. Generatywna sztuczna inteligencja może być wykorzystywana w różnych obszarach, w tym w niskokodzie, ale czym dokładnie jest niskokod i jak możemy dodać do niego AI?

Tworzenie aplikacji i rozwiązań stało się łatwiejsze zarówno dla tradycyjnych programistów, jak i osób bez doświadczenia w programowaniu dzięki platformom Low Code Development. Platformy te umożliwiają tworzenie aplikacji i rozwiązań przy minimalnym lub zerowym użyciu kodu. Osiąga się to poprzez udostępnienie wizualnego środowiska programistycznego, które pozwala przeciągać i upuszczać komponenty do budowy aplikacji i rozwiązań. Dzięki temu można szybciej tworzyć aplikacje, zużywając mniej zasobów. W tej lekcji zagłębimy się w to, jak korzystać z Low Code i jak wzbogacić rozwój niskokodowy o AI za pomocą Power Platform.

Power Platform daje organizacjom możliwość umożliwienia ich zespołom tworzenia własnych rozwiązań dzięki intuicyjnemu środowisku niskokodowemu lub bezkodowemu. To środowisko upraszcza proces tworzenia rozwiązań. Dzięki Power Platform można tworzyć rozwiązania w ciągu dni lub tygodni, zamiast miesięcy lub lat. Power Platform składa się z pięciu kluczowych produktów: Power Apps, Power Automate, Power BI, Power Pages oraz Copilot Studio.

Ta lekcja obejmuje:

- Wprowadzenie do generatywnej AI w Power Platform
- Wprowadzenie do Copilot i jak z niego korzystać
- Wykorzystanie generatywnej AI do tworzenia aplikacji i przepływów w Power Platform
- Zrozumienie modeli AI w Power Platform za pomocą AI Builder
- Tworzenie inteligentnych agentów z Microsoft Copilot Studio

## Cele nauki

Po zakończeniu tej lekcji będziesz potrafił:

- Zrozumieć, jak działa Copilot w Power Platform.

- Stworzyć aplikację Student Assignment Tracker dla naszego startupu edukacyjnego.

- Zbudować przepływ Invoice Processing wykorzystujący AI do wyodrębniania informacji z faktur.

- Stosować najlepsze praktyki przy użyciu modelu AI Create Text with GPT.

- Zrozumieć, czym jest Microsoft Copilot Studio i jak tworzyć inteligentnych agentów za jego pomocą.

Narzędzia i technologie, których użyjesz w tej lekcji, to:

- **Power Apps**, do aplikacji Student Assignment Tracker, która oferuje środowisko niskokodowe do tworzenia aplikacji do śledzenia, zarządzania i interakcji z danymi.

- **Dataverse**, do przechowywania danych aplikacji Student Assignment Tracker, zapewniający niskokodową platformę danych dla przechowywania danych aplikacji.

- **Power Automate**, do przepływu Invoice Processing, gdzie masz środowisko niskokodowe do tworzenia przepływów usprawniających automatyzację procesu fakturowania.

- **AI Builder**, do modelu AI Invoice Processing, gdzie użyjesz gotowych modeli AI do przetwarzania faktur dla naszego startupu.

## Generatywna AI w Power Platform

Wzbogacanie rozwoju niskokodowego i aplikacji generatywną AI jest kluczowym obszarem działań Power Platform. Celem jest umożliwienie każdemu tworzenia aplikacji, stron, pulpitów i automatyzacji procesów wykorzystujących AI, _bez konieczności posiadania wiedzy z zakresu nauki o danych_. Cel ten realizowany jest przez integrację generatywnej AI w doświadczeniu tworzenia niskokodowego w Power Platform w postaci Copilota i AI Builder.

### Jak to działa?

Copilot to asystent AI, który pozwala tworzyć rozwiązania Power Platform, opisując wymagania w serii konwersacyjnych kroków za pomocą języka naturalnego. Możesz na przykład polecić asystentowi AI określenie pól, które Twoja aplikacja będzie wykorzystywać, a on stworzy zarówno aplikację, jak i bazowy model danych lub możesz wskazać, jak ustawić przepływ w Power Automate.

Możesz używać funkcji napędzanych przez Copilot jako elementu w ekranach aplikacji, aby umożliwić użytkownikom odkrywanie informacji przez interakcje konwersacyjne.

AI Builder to funkcja niskokodowa AI dostępna w Power Platform, która umożliwia użycie modeli AI do automatyzacji procesów i przewidywania wyników. Dzięki AI Builder możesz dodać AI do swoich aplikacji i przepływów, które łączą się z danymi w Dataverse lub w różnych źródłach chmurowych, takich jak SharePoint, OneDrive czy Azure.

Copilot jest dostępny we wszystkich produktach Power Platform: Power Apps, Power Automate, Power BI, Power Pages i Copilot Studio (dawniej Power Virtual Agents). AI Builder dostępny jest w Power Apps i Power Automate. W tej lekcji skupimy się na tym, jak korzystać z Copilot i AI Builder w Power Apps i Power Automate, aby stworzyć rozwiązanie dla naszego startupu edukacyjnego.

### Copilot w Power Apps

W ramach Power Platform, Power Apps oferuje niskokodowe środowisko do tworzenia aplikacji do śledzenia, zarządzania i interakcji z danymi. To zestaw usług tworzenia aplikacji z elastyczną platformą danych i możliwością łączenia się z usługami chmurowymi oraz danymi lokalnymi. Power Apps pozwala budować aplikacje działające w przeglądarkach, na tabletach i telefonach oraz udostępniać je współpracownikom. Power Apps ułatwia użytkownikom rozpoczęcie tworzenia aplikacji dzięki prostemu interfejsowi, dzięki czemu każdy użytkownik biznesowy lub doświadczony programista może tworzyć spersonalizowane aplikacje. Doświadczenie tworzenia aplikacji jest również wzbogacone generatywną AI za pośrednictwem Copilota.

Funkcja asystenta AI Copilot w Power Apps pozwala opisać, jakiego rodzaju aplikację potrzebujesz i jakie informacje ma śledzić, zbierać lub wyświetlać Twoja aplikacja. Copilot generuje następnie responsywną aplikację Canvas na podstawie opisu. Możesz potem dostosować aplikację do swoich potrzeb. AI Copilot generuje i sugeruje również tabelę Dataverse z polami potrzebnymi do przechowywania danych, które chcesz śledzić, oraz przykładowymi danymi. Później w tej lekcji przyjrzymy się, czym jest Dataverse i jak możesz z niego korzystać w Power Apps. Następnie możesz dostosować tabelę do swoich potrzeb za pomocą funkcji asystenta AI Copilot w krokach konwersacyjnych. Funkcja ta jest łatwo dostępna z ekranu startowego Power Apps.

### Copilot w Power Automate

W ramach Power Platform, Power Automate pozwala użytkownikom tworzyć automatyczne przepływy między aplikacjami i usługami. Pomaga automatyzować powtarzalne procesy biznesowe, takie jak komunikacja, zbieranie danych i zatwierdzanie decyzji. Prosty interfejs umożliwia użytkownikom o różnym poziomie umiejętności technicznych (od początkujących po doświadczonych programistów) automatyzować zadania w pracy. Doświadczenie tworzenia przepływów jest również wzbogacone generatywną AI za pomocą Copilota.

Funkcja asystenta AI Copilot w Power Automate pozwala opisać, jaki przepływ potrzebujesz i jakie działania ma on wykonywać. Copilot generuje wtedy przepływ na podstawie opisu. Możesz dostosować przepływ do swoich potrzeb. AI Copilot generuje i sugeruje również działania potrzebne do realizacji zadania, które chcesz zautomatyzować. Później w tej lekcji przyjrzymy się, czym są przepływy i jak można ich używać w Power Automate. Możesz dostosować działania do swoich potrzeb, korzystając z funkcji asystenta AI Copilot w krokach konwersacyjnych. Funkcja ta jest łatwo dostępna z ekranu startowego Power Automate.

## Tworzenie inteligentnych agentów z Microsoft Copilot Studio

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst) (dawniej Power Virtual Agents) to niskokodowy członek Power Platform do tworzenia **agentów AI** — konwersacyjnych copilotów, którzy mogą odpowiadać na pytania, podejmować działania i automatyzować zadania w imieniu użytkowników. Podobnie jak reszta Power Platform, tworzysz tych agentów w wizualnym środowisku skoncentrowanym na języku naturalnym: opisujesz, co agent ma robić, a Copilot Studio pomaga w budowie jego instrukcji, wiedzy i działań.

Dla naszego startupu edukacyjnego możesz stworzyć agenta, który odpowiada na pytania studentów dotyczące kursów, sprawdza terminy zadań oraz nawet wysyła e-maile do wykładowcy — wszystko to bez pisania kodu.

Oto niektóre z najnowszych funkcji, które czynią Copilot Studio potężnym narzędziem:

- **Generatywne odpowiedzi z twojej wiedzy**. Zamiast ręcznie tworzyć każdą rozmowę, możesz podłączyć **źródła wiedzy** — publiczne strony internetowe, SharePoint, OneDrive, Dataverse, przesłane pliki lub dane przedsiębiorstwa przez konektory — a agent generuje na ich podstawie ugruntowane odpowiedzi.

- **Generatywna orkiestracja**. Zamiast opierać się na sztywnych frazach wyzwalających, agent korzysta z AI, aby zrozumieć zapytanie i dynamicznie zdecydować, które źródła wiedzy, tematy i działania połączyć, by je zrealizować, włącznie z łączeniem kilku kroków.

- **Działania i konektory**. Agenci mogą *coś robić*, nie tylko rozmawiać. Możesz wyposażyć agenta w działania oparte na ponad 1,500 wbudowanych konektorach Power Platform, przepływach Power Automate, niestandardowych REST API, promptach lub serwerach **Model Context Protocol (MCP)**.

- **Autonomiczne agenty**. Agenci nie ograniczają się do odpowiedzi w oknie czatu. Możesz tworzyć **autonomiczne agenty**, które są wywoływane przez zdarzenia — takie jak nowy e-mail, nowy rekord w Dataverse lub przesłany plik — a następnie działają w tle, aby wykonać zadanie.

- **Orkiestracja wielu agentów**. Agenci mogą wywoływać innych agentów. Agent Copilot Studio może przekazać zadanie lub być rozszerzony przez innych agentów, w tym agentów opublikowanych w Microsoft 365 Copilot oraz tych zbudowanych w Microsoft Foundry.

- **Wybór modelu**. Poza wbudowanymi modelami możesz użyć modeli z katalogu Microsoft Foundry, aby dostosować sposób, w jaki agent rozumie i odpowiada.

- **Publikacja wszędzie**. Po zbudowaniu agent może zostać opublikowany na wielu kanałach — Microsoft Teams, Microsoft 365 Copilot, stronie internetowej lub niestandardowej aplikacji — z zarządzaniem bezpieczeństwem, uwierzytelnianiem i analityką przez doświadczenie administracyjne Power Platform.

Możesz rozpocząć tworzenie pierwszego agenta na [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst) i dowiedzieć się więcej w [dokumentacji Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst).

## Zadanie: Zarządzanie zadaniami uczniów i fakturami dla naszego startupu, z wykorzystaniem Copilot

Nasz startup oferuje kursy online dla studentów. Startup dynamicznie się rozwija i obecnie ma trudności z nadążeniem za zapotrzebowaniem na swoje kursy. Startup zatrudnił Cię jako dewelopera Power Platform, aby pomóc im stworzyć rozwiązanie niskokodowe do zarządzania zadaniami uczniów i fakturami. Ich rozwiązanie powinno umożliwiać śledzenie i zarządzanie zadaniami uczniów za pomocą aplikacji oraz automatyzację procesu fakturowania za pomocą przepływu. Poproszono Cię o wykorzystanie generatywnej AI do opracowania tego rozwiązania.

Na początku korzystania z Copilot możesz skorzystać z [Power Platform Copilot Prompt Library](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko), aby rozpocząć pracę z promptami. Ta biblioteka zawiera listę promptów, które możesz wykorzystać do tworzenia aplikacji i przepływów z Copilot. Możesz także użyć promptów z biblioteki, by zainspirować się, jak opisać swoje wymagania Copilotowi.

### Stwórz aplikację Student Assignment Tracker dla naszego startupu

Edukatorzy w naszym startupie mieli trudności ze śledzeniem zadań uczniów. Korzystali z arkusza kalkulacyjnego do śledzenia zadań, ale zarządzanie tym stało się trudne, gdy liczba studentów wzrosła. Poprosili Cię o stworzenie aplikacji, która pomoże im śledzić i zarządzać zadaniami uczniów. Aplikacja powinna umożliwiać dodawanie nowych zadań, przeglądanie, aktualizowanie i usuwanie zadań. Powinna także umożliwiać edukatorom i uczniom przeglądanie zadań ocenionych i nieocenionych.

Zbudujesz aplikację korzystając z Copilot w Power Apps, wykonując poniższe kroki:

1. Przejdź do ekranu startowego [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

1. Wykorzystaj pole tekstowe na ekranie startowym, aby opisać aplikację, którą chcesz zbudować. Na przykład: **_Chcę zbudować aplikację do śledzenia i zarządzania zadaniami uczniów_**. Kliknij przycisk **Wyślij**, aby przesłać prompt do AI Copilot.

![Opisz aplikację, którą chcesz zbudować](../../../translated_images/pl/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. AI Copilot zasugeruje tabelę Dataverse z polami niezbędnymi do przechowywania danych, które chcesz śledzić, oraz przykładowymi danymi. Możesz potem dostosować tabelę do swoich potrzeb korzystając z funkcji asystenta AI Copilot w krokach konwersacyjnych.

   > **Ważne**: Dataverse to podstawowa platforma danych Power Platform. Jest to niskokodowa platforma danych do przechowywania danych aplikacji. To w pełni zarządzana usługa, która bezpiecznie przechowuje dane w chmurze Microsoft i jest udostępniana w Twoim środowisku Power Platform. Posiada wbudowane funkcje zarządzania danymi, takie jak klasyfikacja danych, pochodzenie danych, szczegółowa kontrola dostępu i inne. Możesz dowiedzieć się więcej o Dataverse [tutaj](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Sugerowane pola w nowej tabeli](../../../translated_images/pl/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. Edukatorzy chcą wysyłać e-maile do studentów, którzy złożyli zadania, aby informować ich o postępach. Możesz użyć Copilot, aby dodać nowe pole do tabeli do przechowywania e-maila studenta. Na przykład możesz użyć promptu: **_Chcę dodać kolumnę do przechowywania e-maila studenta_**. Kliknij przycisk **Wyślij**, aby przesłać prompt do AI Copilot.

![Dodawanie nowego pola](../../../translated_images/pl/copilot-new-column.35e15ff21acaf274.webp)

1. AI Copilot wygeneruje nowe pole, które możesz dostosować do swoich potrzeb.


1. Po zakończeniu pracy z tabelą kliknij przycisk **Create app**, aby utworzyć aplikację.

1. AI Copilot wygeneruje responsywną aplikację Canvas na podstawie Twojego opisu. Następnie możesz dostosować aplikację do swoich potrzeb.

1. Aby nauczyciele mogli wysyłać e-maile do uczniów, możesz użyć Copilota, aby dodać nowy ekran do aplikacji. Na przykład możesz użyć następującej instrukcji, aby dodać nowy ekran do aplikacji: **_Chcę dodać ekran do wysyłania e-maili do uczniów_**. Kliknij przycisk **Send**, aby wysłać instrukcję do AI Copilota.

![Adding a new screen via a prompt instruction](../../../translated_images/pl/copilot-new-screen.2e0bef7132a17392.webp)

1. AI Copilot wygeneruje nowy ekran, a następnie możesz go dostosować do swoich potrzeb.

1. Po zakończeniu pracy z aplikacją kliknij przycisk **Save**, aby zapisać aplikację.

1. Aby udostępnić aplikację nauczycielom, kliknij przycisk **Share**, a następnie ponownie kliknij **Share**. Następnie możesz udostępnić aplikację nauczycielom, wpisując ich adresy e-mail.

> **Twoje zadanie domowe**: Aplikacja, którą właśnie zbudowałeś, to dobry początek, ale można ją ulepszyć. Dzięki funkcji e-mail nauczyciele mogą wysyłać e-maile do uczniów tylko ręcznie, wpisując ich adresy e-mail. Czy możesz użyć Copilota, aby zbudować automatyzację, która umożliwi nauczycielom automatyczne wysyłanie e-maili do uczniów, gdy ci oddadzą swoje zadania? Podpowiedź: używając odpowiedniej instrukcji, możesz wykorzystać Copilota w Power Automate do tego celu.

### Zbuduj tabelę informacji o fakturach dla naszego startupu

Zespół finansowy naszego startupu miał trudności z śledzeniem faktur. Korzystali z arkusza kalkulacyjnego do śledzenia faktur, ale stało się to trudne do zarządzania wraz ze wzrostem liczby faktur. Poprosili Cię o stworzenie tabeli, która pomoże im przechowywać, śledzić i zarządzać informacjami o otrzymanych fakturach. Tabela powinna być używana do budowy automatyzacji, która wyodrębni wszystkie informacje z faktur i zapisze je w tabeli. Tabela powinna również umożliwiać zespołowi finansowemu przeglądanie faktur opłaconych i nieopłaconych.

Power Platform ma wbudowaną platformę danych nazwaną Dataverse, która umożliwia przechowywanie danych dla Twoich aplikacji i rozwiązań. Dataverse zapewnia platformę danych low-code do przechowywania danych aplikacji. Jest to w pełni zarządzana usługa, która bezpiecznie przechowuje dane w chmurze Microsoft i jest prowadzona w środowisku Twojej Power Platform. Posiada wbudowane możliwości zarządzania danymi, takie jak klasyfikacja danych, pochodzenie danych, szczegółowa kontrola dostępu i inne. Możesz dowiedzieć się więcej [o Dataverse tutaj](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Dlaczego powinniśmy korzystać z Dataverse dla naszego startupu? Standardowe i niestandardowe tabele w Dataverse oferują bezpieczną i opartą na chmurze opcję przechowywania danych. Tabele pozwalają przechowywać różne typy danych, podobnie jak używa się wielu arkuszy w jednym skoroszycie Excel. Możesz używać tabel do przechowywania danych specyficznych dla Twojej organizacji lub potrzeb biznesowych. Niektóre z korzyści, jakie nasz startup odniesie z korzystania z Dataverse, to między innymi:

- **Łatwość zarządzania**: Zarówno metadane, jak i dane są przechowywane w chmurze, więc nie musisz martwić się szczegółami ich przechowywania czy zarządzania. Możesz skupić się na tworzeniu swoich aplikacji i rozwiązań.

- **Bezpieczeństwo**: Dataverse zapewnia bezpieczną i opartą na chmurze opcję przechowywania danych. Możesz kontrolować, kto ma dostęp do danych w Twoich tabelach i jak może z nich korzystać, używając zabezpieczeń opartych na rolach.

- **Bogate metadane**: Typy danych i relacje są używane bezpośrednio w Power Apps.

- **Logika i walidacja**: Możesz używać reguł biznesowych, pól obliczeniowych i reguł walidacji, aby egzekwować logikę biznesową i utrzymywać dokładność danych.

Teraz, gdy wiesz, czym jest Dataverse i dlaczego warto go używać, przyjrzyjmy się, jak możesz wykorzystać Copilota do utworzenia tabeli w Dataverse, która spełni wymagania naszego zespołu finansowego.

> **Uwaga**: Tę tabelę wykorzystasz w następnej sekcji do budowy automatyzacji, która wyodrębni wszystkie informacje z faktur i zapisze je w tabeli.

Aby utworzyć tabelę w Dataverse przy użyciu Copilota, wykonaj poniższe kroki:

1. Przejdź do ekranu głównego [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

2. Na lewym pasku nawigacyjnym wybierz **Tables**, a następnie kliknij **Describe the new Table**.

![Select new table](../../../translated_images/pl/describe-new-table.0792373eb757281e.webp)

1. Na ekranie **Describe the new Table** użyj pola tekstowego, aby opisać tabelę, którą chcesz utworzyć. Na przykład, **_Chcę utworzyć tabelę do przechowywania informacji o fakturach_**. Kliknij przycisk **Send**, aby wysłać instrukcję do AI Copilota.

![Describe the table](../../../translated_images/pl/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. AI Copilot zasugeruje tabelę Dataverse z polami potrzebnymi do przechowywania danych, które chcesz śledzić, oraz z przykładowymi danymi. Następnie możesz dostosować tabelę do swoich potrzeb, korzystając z funkcji asystenta AI Copilot przez rozmowę.

![Suggested Dataverse table](../../../translated_images/pl/copilot-dataverse-table.b3bc936091324d9d.webp)

1. Zespół finansowy chce wysłać e-mail do dostawcy, aby poinformować go o aktualnym statusie faktury. Możesz użyć Copilota, aby dodać nowe pole do tabeli, aby przechowywać e-mail dostawcy. Na przykład użyj następującej instrukcji: **_Chcę dodać kolumnę do przechowywania e-maila dostawcy_**. Kliknij **Send**, aby wysłać instrukcję do AI Copilota.

1. AI Copilot wygeneruje nowe pole, które następnie możesz dostosować do swoich potrzeb.

1. Po zakończeniu pracy z tabelą kliknij przycisk **Create**, aby utworzyć tabelę.

## Modele AI w Power Platform z AI Builder

AI Builder to możliwość low-code AI dostępna w Power Platform, która umożliwia korzystanie z modeli AI do automatyzacji procesów i prognozowania wyników. Dzięki AI Builder możesz wprowadzić AI do swoich aplikacji i przepływów, które łączą się z danymi w Dataverse lub w różnych źródłach danych w chmurze, takich jak SharePoint, OneDrive czy Azure.

## Gotowe modele AI kontra modele AI na zamówienie

AI Builder oferuje dwa typy modeli AI: gotowe modele AI oraz modele AI na zamówienie. Gotowe modele AI są gotowymi do użycia modelami wytrenowanymi przez Microsoft i dostępnymi w Power Platform. Pomagają one dodać inteligencję do Twoich aplikacji i przepływów bez konieczności gromadzenia danych i samodzielnego budowania, trenowania oraz publikowania własnych modeli. Możesz używać tych modeli do automatyzacji procesów i prognozowania wyników.

Niektóre z gotowych modeli AI dostępnych w Power Platform to:

- **Wydobycie kluczowych fraz**: Model wyodrębnia kluczowe frazy z tekstu.
- **Wykrywanie języka**: Model wykrywa język tekstu.
- **Analiza nastroju**: Model wykrywa pozytywny, negatywny, neutralny lub mieszany nastrój w tekście.
- **Odczyt wizytówek**: Model wyodrębnia informacje z wizytówek.
- **Rozpoznawanie tekstu**: Model wyodrębnia tekst z obrazów.
- **Wykrywanie obiektów**: Model wykrywa i wyodrębnia obiekty z obrazów.
- **Przetwarzanie dokumentów**: Model wyodrębnia informacje z formularzy.
- **Przetwarzanie faktur**: Model wyodrębnia informacje z faktur.

Z modelami AI na zamówienie możesz wprowadzić swój własny model do AI Builder, dzięki czemu działa on jak dowolny model niestandardowy AI Builder, umożliwiając trenowanie modelu na własnych danych. Możesz używać tych modeli do automatyzacji procesów i prognozowania wyników zarówno w Power Apps, jak i Power Automate. Przy korzystaniu z własnych modeli obowiązują pewne ograniczenia. Więcej o tych [ograniczeniach](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst) dowiesz się tutaj.

![AI builder models](../../../translated_images/pl/ai-builder-models.8069423b84cfc47f.webp)

## Zadanie #2 - Zbuduj przepływ do przetwarzania faktur dla naszego startupu

Zespół finansowy miał trudności z przetwarzaniem faktur. Korzystali z arkusza kalkulacyjnego do śledzenia faktur, ale stało się to trudne do zarządzania wraz ze wzrostem ich liczby. Poprosili Cię o zbudowanie przepływu pracy, który pomoże im przetwarzać faktury z wykorzystaniem sztucznej inteligencji. Przepływ powinien pozwolić na wyodrębnianie informacji z faktur i zapisywanie ich w tabeli Dataverse. Powinien również umożliwiać wysyłanie e-maila do zespołu finansowego z wyodrębnionymi informacjami.

Teraz, gdy wiesz, czym jest AI Builder i dlaczego warto go używać, przyjrzyjmy się, jak możesz wykorzystać model Przetwarzania faktur w AI Builder, omówiony wcześniej, do zbudowania przepływu, który pomoże zespołowi finansowemu przetwarzać faktury.

Aby zbudować przepływ, który pomoże zespołowi finansowemu przetwarzać faktury z wykorzystaniem modelu Przetwarzania faktur w AI Builder, wykonaj poniższe kroki:

1. Przejdź do ekranu głównego [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst).

2. Użyj pola tekstowego na ekranie głównym, aby opisać przepływ, który chcesz zbudować. Na przykład, **_Przetwarzaj fakturę, gdy pojawi się w mojej skrzynce odbiorczej_**. Kliknij przycisk **Send**, aby wysłać instrukcję do AI Copilota.

   ![Copilot power automate](../../../translated_images/pl/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. AI Copilot zasugeruje działania potrzebne do wykonania zadania, które chcesz zautomatyzować. Możesz kliknąć przycisk **Next**, aby przejść do kolejnych kroków.

4. W następnym kroku Power Automate poprosi Cię o skonfigurowanie połączeń niezbędnych do działania przepływu. Po zakończeniu kliknij przycisk **Create flow**, aby utworzyć przepływ.

5. AI Copilot wygeneruje przepływ, który następnie możesz dostosować do swoich potrzeb.

6. Zaktualizuj wyzwalacz przepływu i ustaw **Folder** na folder, w którym będą przechowywane faktury. Na przykład możesz ustawić folder na **Inbox**. Kliknij **Pokaż opcje zaawansowane** i ustaw opcję **Tylko z załącznikami** na **Tak**. Zapewni to, że przepływ uruchomi się tylko wtedy, gdy w folderze pojawi się e-mail z załącznikiem.

7. Usuń następujące akcje z przepływu: **HTML to text**, **Compose**, **Compose 2**, **Compose 3** i **Compose 4**, ponieważ nie będą one potrzebne.

8. Usuń akcję **Condition** z przepływu, gdyż nie będzie używana. Powinno to wyglądać według poniższego zrzutu ekranu:

   ![power automate, remove actions](../../../translated_images/pl/powerautomate-remove-actions.7216392fe684ceba.webp)

9. Kliknij przycisk **Add an action** i wyszukaj **Dataverse**. Wybierz akcję **Add a new row**.

10. W akcji **Extract Information from invoices** zaktualizuj pole **Invoice File**, aby odwoływało się do **Attachment Content** z e-maila. Zapewni to wyodrębnianie informacji z załącznika faktury.

11. Wybierz tabelę, którą utworzyłeś wcześniej. Na przykład możesz wybrać tabelę **Invoice Information**. Wybierz dynamiczne wartości z poprzedniej akcji, aby wypełnić następujące pola:

    - ID
    - Kwota
    - Data
    - Nazwa
    - Status - Ustaw **Status** na **Pending**.
    - E-mail dostawcy - Użyj dynamicznej wartości **From** z wyzwalacza **When a new email arrives**.

    ![power automate add row](../../../translated_images/pl/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. Po zakończeniu pracy z przepływem kliknij przycisk **Save**, aby zapisać przepływ. Możesz przetestować przepływ, wysyłając e-mail z fakturą do folderu, który ustawiłeś w wyzwalaczu.

> **Twoje zadanie domowe**: Przepływ, który właśnie zbudowałeś, to dobry początek, teraz musisz pomyśleć, jak zbudować automatyzację, która pozwoli naszemu zespołowi finansowemu wysyłać e-maile do dostawcy, aby informować go o aktualnym statusie faktury. Podpowiedź: przepływ powinien uruchamiać się, gdy status faktury się zmieni.

## Użyj modelu AI do generowania tekstu w Power Automate

Model AI Create Text with GPT w AI Builder umożliwia generowanie tekstu na podstawie instrukcji i jest zasilany przez usługę Microsoft Azure OpenAI. Dzięki tej funkcji możesz wprowadzić technologię GPT (Generative Pre-Trained Transformer) do swoich aplikacji i przepływów, aby tworzyć różnorodne zautomatyzowane przepływy i aplikacje dostarczające wartościowych informacji.

Modele GPT przechodzą rozległe szkolenia na ogromnych zbiorach danych, co pozwala im generować tekst bardzo przypominający język ludzki po podaniu instrukcji. Po integracji z automatyzacją przepływów pracy, modele AI takie jak GPT mogą być wykorzystywane do usprawniania i automatyzacji wielu zadań.

Na przykład, możesz budować przepływy do automatycznego generowania tekstu dla różnych zastosowań, takich jak: szkice e-maili, opisy produktów i inne. Możesz też używać modelu do tworzenia tekstu dla różnych aplikacji, takich jak chatboty czy aplikacje obsługi klienta, które pomagają agentom obsługi klienta efektywnie i skutecznie odpowiadać na zapytania klientów.

![create a prompt](../../../translated_images/pl/create-prompt-gpt.69d429300c2e870a.webp)


Aby dowiedzieć się, jak używać tego modelu AI w Power Automate, przejdź przez moduł [Dodaj inteligencję za pomocą AI Builder i GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Świetna robota! Kontynuuj naukę

Po ukończeniu tej lekcji sprawdź naszą [kolekcję nauki Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej rozwijać swoją wiedzę o Generative AI!

Chcesz dostosować i wyciągnąć więcej z Copilota? Poznaj [Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) — kolekcję instrukcji, agentów, umiejętności i konfiguracji stworzonych przez społeczność, która pomoże Ci jak najlepiej wykorzystać GitHub Copilot.

Przejdź do Lekcji 11, gdzie przyjrzymy się, jak [zintegrować Generative AI z wywoływaniem funkcji](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->