# Budowanie Aplikacji AI z Wykorzystaniem Narzędzi Niskokodowych

[![Budowanie Aplikacji AI z Wykorzystaniem Narzędzi Niskokodowych](../../images/10-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson10-gh?WT.mc_id=academic-105485-koreyst)

> _(Kliknij powyższy obraz, aby obejrzeć wideo z tej lekcji)_

## Wprowadzenie

Teraz, gdy nauczyliśmy się budować aplikacje generujące obrazy, porozmawiajmy o podejściu niskokodowym. Generatywna SI może być wykorzystywana w różnych obszarach, w tym w rozwiązaniach niskokodowych, ale czym właściwie jest podejście niskokodowe i jak możemy wzbogacić je o sztuczną inteligencję?

Tworzenie aplikacji i rozwiązań stało się łatwiejsze zarówno dla tradycyjnych programistów, jak i osób nieposiadających umiejętności programowania, dzięki wykorzystaniu Platform Programistycznych Low-Code. Platformy te umożliwiają budowanie aplikacji i rozwiązań przy minimalnej ilości kodu lub całkowicie bez niego. Osiąga się to dzięki wizualnemu środowisku programistycznemu, które pozwala przeciągać i upuszczać komponenty w celu tworzenia aplikacji i rozwiązań. Umożliwia to budowanie aplikacji i rozwiązań szybciej i przy mniejszych zasobach. W tej lekcji zagłębimy się w to, jak korzystać z podejścia Low-Code i jak wzbogacić je o AI za pomocą Power Platform.

Power Platform daje organizacjom możliwość umożliwienia swoim zespołom budowania własnych rozwiązań poprzez intuicyjne środowisko niskokodowe lub bezkodowe. To środowisko pomaga uprościć proces tworzenia rozwiązań. Dzięki Power Platform rozwiązania mogą być budowane w ciągu dni lub tygodni zamiast miesięcy czy lat. Power Platform składa się z pięciu kluczowych produktów: Power Apps, Power Automate, Power BI, Power Pages i Copilot Studio.

Ta lekcja obejmuje:

- Wprowadzenie do Generatywnej SI w Power Platform
- Wprowadzenie do Copilota i jego wykorzystanie
- Korzystanie z Generatywnej SI do budowania aplikacji i przepływów w Power Platform
- Zrozumienie modeli SI w Power Platform z AI Builder

## Cele Nauki

Po zakończeniu tej lekcji będziesz potrafić:

- Zrozumieć, jak działa Copilot w Power Platform.

- Zbudować Aplikację do Śledzenia Zadań Studenckich dla naszego edukacyjnego startupu.

- Zbudować Przepływ Przetwarzania Faktur, który wykorzystuje SI do wyodrębniania informacji z faktur.

- Stosować najlepsze praktyki podczas korzystania z modelu SI Tworzenia Tekstu z GPT.

Narzędzia i technologie, których użyjesz w tej lekcji, to:

- **Power Apps**, do stworzenia aplikacji do śledzenia zadań studenckich, zapewniającej niskokodowe środowisko do tworzenia aplikacji do śledzenia, zarządzania i interakcji z danymi.

- **Dataverse**, do przechowywania danych dla aplikacji do śledzenia zadań studenckich, gdzie Dataverse zapewni niskokodową platformę danych do przechowywania danych aplikacji.

- **Power Automate**, do przepływu przetwarzania faktur, gdzie będziesz mieć niskokodowe środowisko programistyczne do budowania przepływów pracy automatyzujących proces przetwarzania faktur.

- **AI Builder**, do modelu SI przetwarzania faktur, gdzie będziesz używać gotowych modeli SI do przetwarzania faktur dla naszego startupu.

## Generatywna SI w Power Platform

Wzbogacanie niskokodowego tworzenia aplikacji i ich funkcjonalności o generatywną sztuczną inteligencję jest kluczowym obszarem zainteresowania Power Platform. Celem jest umożliwienie każdemu budowania aplikacji, stron, pulpitów i automatyzacji procesów z wykorzystaniem SI, _bez wymagania jakiejkolwiek wiedzy z zakresu nauki o danych_. Ten cel jest osiągany poprzez integrację generatywnej SI z doświadczeniem programistycznym w Power Platform w formie Copilota i AI Builder.

### Jak to działa?

Copilot to asystent SI, który umożliwia tworzenie rozwiązań Power Platform poprzez opisanie wymagań w serii konwersacyjnych kroków przy użyciu języka naturalnego. Możesz na przykład polecić asystentowi SI określenie, jakie pola będzie używać Twoja aplikacja, a on stworzy zarówno aplikację, jak i bazowy model danych, lub możesz określić, jak skonfigurować przepływ w Power Automate.

Możesz używać funkcji napędzanych przez Copilota jako funkcji w ekranach aplikacji, aby umożliwić użytkownikom odkrywanie spostrzeżeń poprzez interakcje konwersacyjne.

AI Builder to niskokodowa możliwość SI dostępna w Power Platform, która umożliwia korzystanie z modeli SI, aby pomóc w automatyzacji procesów i przewidywaniu wyników. Dzięki AI Builder możesz wprowadzić SI do swoich aplikacji i przepływów, które łączą się z Twoimi danymi w Dataverse lub w różnych źródłach danych w chmurze, takich jak SharePoint, OneDrive czy Azure.

Copilot jest dostępny we wszystkich produktach Power Platform: Power Apps, Power Automate, Power BI, Power Pages i Power Virtual Agents. AI Builder jest dostępny w Power Apps i Power Automate. W tej lekcji skupimy się na tym, jak używać Copilota i AI Builder w Power Apps i Power Automate do budowania rozwiązania dla naszego edukacyjnego startupu.

### Copilot w Power Apps

Jako część Power Platform, Power Apps zapewnia niskokodowe środowisko programistyczne do budowania aplikacji do śledzenia, zarządzania i interakcji z danymi. To zestaw usług do tworzenia aplikacji ze skalowalną platformą danych i możliwością łączenia się z usługami w chmurze i danymi lokalnymi. Power Apps pozwala budować aplikacje, które działają w przeglądarkach, na tabletach i telefonach, i mogą być udostępniane współpracownikom. Power Apps ułatwia użytkownikom tworzenie aplikacji dzięki prostemu interfejsowi, dzięki czemu każdy użytkownik biznesowy lub profesjonalny deweloper może tworzyć niestandardowe aplikacje. Doświadczenie tworzenia aplikacji jest również wzbogacone o Generatywną SI dzięki Copilotowi.

Funkcja asystenta SI Copilot w Power Apps umożliwia opisanie, jakiego rodzaju aplikacji potrzebujesz i jakie informacje chcesz, aby Twoja aplikacja śledziła, zbierała lub pokazywała. Copilot następnie generuje responsywną aplikację Canvas na podstawie Twojego opisu. Możesz następnie dostosować aplikację do swoich potrzeb. AI Copilot generuje i sugeruje również tabelę Dataverse z polami, których potrzebujesz do przechowywania danych, które chcesz śledzić, oraz przykładowe dane. Później w tej lekcji przyjrzymy się, czym jest Dataverse i jak możesz go używać w Power Apps. Możesz następnie dostosować tabelę do swoich potrzeb, korzystając z funkcji asystenta AI Copilot poprzez kroki konwersacyjne. Ta funkcja jest łatwo dostępna z ekranu głównego Power Apps.

### Copilot w Power Automate

Jako część Power Platform, Power Automate pozwala użytkownikom tworzyć zautomatyzowane przepływy pracy między aplikacjami i usługami. Pomaga automatyzować powtarzalne procesy biznesowe, takie jak komunikacja, zbieranie danych i zatwierdzanie decyzji. Jego prosty interfejs pozwala użytkownikom o każdej kompetencji technicznej (od początkujących po doświadczonych programistów) automatyzować zadania. Doświadczenie tworzenia przepływów pracy jest również wzbogacone o Generatywną SI dzięki Copilotowi.

Funkcja asystenta SI Copilot w Power Automate umożliwia opisanie, jakiego rodzaju przepływu potrzebujesz i jakie działania chcesz, aby Twój przepływ wykonywał. Copilot następnie generuje przepływ na podstawie Twojego opisu. Możesz następnie dostosować przepływ do swoich potrzeb. AI Copilot generuje i sugeruje również akcje, których potrzebujesz do wykonania zadania, które chcesz zautomatyzować. Później w tej lekcji przyjrzymy się, czym są przepływy i jak możesz ich używać w Power Automate. Możesz następnie dostosować akcje do swoich potrzeb, korzystając z funkcji asystenta AI Copilot poprzez kroki konwersacyjne. Ta funkcja jest łatwo dostępna z ekranu głównego Power Automate.

## Zadanie: Zarządzanie zadaniami studentów i fakturami dla naszego startupu przy użyciu Copilota

Nasz startup oferuje kursy online dla studentów. Startup rozwinął się szybko i teraz ma trudności z nadążeniem za popytem na swoje kursy. Startup zatrudnił Cię jako dewelopera Power Platform, aby pomóc im zbudować niskokodowe rozwiązanie, które pomoże im zarządzać zadaniami studentów i fakturami. Ich rozwiązanie powinno umożliwiać śledzenie i zarządzanie zadaniami studentów poprzez aplikację oraz automatyzować proces przetwarzania faktur poprzez przepływ pracy. Poproszono Cię o wykorzystanie Generatywnej SI do opracowania rozwiązania.

Kiedy zaczynasz korzystać z Copilota, możesz użyć [Biblioteki Promptów Power Platform Copilot](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko), aby rozpocząć pracę z promptami. Ta biblioteka zawiera listę promptów, których możesz użyć do budowania aplikacji i przepływów z Copilotem. Możesz również użyć promptów w bibliotece, aby uzyskać wyobrażenie o tym, jak opisać swoje wymagania Copilotowi.

### Budowanie Aplikacji do Śledzenia Zadań Studenckich dla Naszego Startupu

Edukatorzy w naszym startupie mają trudności z śledzeniem zadań studentów. Używali arkusza kalkulacyjnego do śledzenia zadań, ale stało się to trudne do zarządzania wraz ze wzrostem liczby studentów. Poprosili Cię o zbudowanie aplikacji, która pomoże im śledzić i zarządzać zadaniami studentów. Aplikacja powinna umożliwiać im dodawanie nowych zadań, przeglądanie zadań, aktualizowanie zadań i usuwanie zadań. Aplikacja powinna również umożliwiać edukatorom i studentom przeglądanie zadań, które zostały ocenione i tych, które nie zostały ocenione.

Zbudujesz aplikację używając Copilota w Power Apps, wykonując poniższe kroki:

1. Przejdź do ekranu głównego [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

1. Użyj pola tekstowego na ekranie głównym, aby opisać aplikację, którą chcesz zbudować. Na przykład, **_Chcę zbudować aplikację do śledzenia i zarządzania zadaniami studentów_**. Kliknij przycisk **Wyślij**, aby wysłać prompt do AI Copilot.

![Opisz aplikację, którą chcesz zbudować](../../images/copilot-chat-prompt-powerapps.png?WT.mc_id=academic-105485-koreyst)

1. AI Copilot zasugeruje tabelę Dataverse z polami, których potrzebujesz do przechowywania danych, które chcesz śledzić, oraz przykładowe dane. Możesz następnie dostosować tabelę do swoich potrzeb, korzystając z funkcji asystenta AI Copilot poprzez kroki konwersacyjne.

   > **Ważne**: Dataverse to bazowa platforma danych dla Power Platform. To niskokodowa platforma danych do przechowywania danych aplikacji. Jest w pełni zarządzaną usługą, która bezpiecznie przechowuje dane w chmurze Microsoft i jest dostarczana w ramach Twojego środowiska Power Platform. Zawiera wbudowane możliwości zarządzania danymi, takie jak klasyfikacja danych, linia pochodzenia danych, szczegółowa kontrola dostępu i więcej. Możesz dowiedzieć się więcej o Dataverse [tutaj](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Sugerowane pola w nowej tabeli](../../images/copilot-dataverse-table-powerapps.png?WT.mc_id=academic-105485-koreyst)

1. Edukatorzy chcą wysyłać e-maile do studentów, którzy złożyli swoje zadania, aby informować ich o postępie ich zadań. Możesz użyć Copilota, aby dodać nowe pole do tabeli do przechowywania adresu e-mail studenta. Na przykład, możesz użyć następującego promptu, aby dodać nowe pole do tabeli: **_Chcę dodać kolumnę do przechowywania adresu e-mail studenta_**. Kliknij przycisk **Wyślij**, aby wysłać prompt do AI Copilot.

![Dodawanie nowego pola](../../images/copilot-new-column.png?WT.mc_id=academic-105485-koreyst)

1. AI Copilot wygeneruje nowe pole i możesz następnie dostosować pole do swoich potrzeb.

1. Po zakończeniu pracy z tabelą kliknij przycisk **Utwórz aplikację**, aby utworzyć aplikację.

1. AI Copilot wygeneruje responsywną aplikację Canvas na podstawie Twojego opisu. Możesz następnie dostosować aplikację do swoich potrzeb.

1. Aby edukatorzy mogli wysyłać e-maile do studentów, możesz użyć Copilota, aby dodać nowy ekran do aplikacji. Na przykład, możesz użyć następującego promptu, aby dodać nowy ekran do aplikacji: **_Chcę dodać ekran do wysyłania e-maili do studentów_**. Kliknij przycisk **Wyślij**, aby wysłać prompt do AI Copilot.

![Dodawanie nowego ekranu za pomocą instrukcji promptu](../../images/copilot-new-screen.png?WT.mc_id=academic-105485-koreyst)

1. AI Copilot wygeneruje nowy ekran i możesz następnie dostosować ekran do swoich potrzeb.

1. Po zakończeniu pracy z aplikacją kliknij przycisk **Zapisz**, aby zapisać aplikację.

1. Aby udostępnić aplikację edukatorom, kliknij przycisk **Udostępnij**, a następnie kliknij ponownie przycisk **Udostępnij**. Możesz następnie udostępnić aplikację edukatorom, wprowadzając ich adresy e-mail.

> **Twoje zadanie domowe**: Aplikacja, którą właśnie zbudowałeś, to dobry początek, ale można ją ulepszyć. Z funkcją e-maila edukatorzy mogą wysyłać e-maile do studentów tylko ręcznie, wpisując ich adresy e-mail. Czy możesz użyć Copilota do zbudowania automatyzacji, która umożliwi edukatorom automatyczne wysyłanie e-maili do studentów, gdy złożą swoje zadania? Wskazówka: z odpowiednim promptem możesz użyć Copilota w Power Automate do zbudowania tego.

### Budowanie Tabeli Informacji o Fakturach dla Naszego Startupu

Zespół finansowy naszego startupu ma trudności z śledzeniem faktur. Używali arkusza kalkulacyjnego do śledzenia faktur, ale stało się to trudne do zarządzania wraz ze wzrostem liczby faktur. Poprosili Cię o zbudowanie tabeli, która pomoże im przechowywać, śledzić i zarządzać informacjami o otrzymanych fakturach. Tabela powinna być używana do zbudowania automatyzacji, która wyodrębni wszystkie informacje z faktury i przechowa je w tabeli. Tabela powinna również umożliwiać zespołowi finansowemu przeglądanie faktur, które zostały opłacone i tych, które nie zostały opłacone.

Power Platform posiada bazową platformę danych o nazwie Dataverse, która umożliwia przechowywanie danych dla twoich aplikacji i rozwiązań. Dataverse zapewnia niskokodową platformę danych do przechowywania danych aplikacji. Jest w pełni zarządzaną usługą, która bezpiecznie przechowuje dane w chmurze Microsoft i jest dostarczana w ramach Twojego środowiska Power Platform. Zawiera wbudowane możliwości zarządzania danymi, takie jak klasyfikacja danych, linia pochodzenia danych, szczegółowa kontrola dostępu i więcej. Możesz dowiedzieć się więcej [o Dataverse tutaj](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Dlaczego powinniśmy używać Dataverse dla naszego startupu? Standardowe i niestandardowe tabele w Dataverse zapewniają bezpieczną i opartą na chmurze opcję przechowywania danych. Tabele pozwalają przechowywać różne typy danych, podobnie jak używałbyś wielu arkuszy w jednym skoroszycie Excel. Możesz używać tabel do przechowywania danych, które są specyficzne dla Twojej organizacji lub potrzeb biznesowych. Niektóre korzyści, jakie nasz startup uzyska z używania Dataverse, obejmują, ale nie ograniczają się do:

- **Łatwe zarządzanie**: Zarówno metadane, jak i dane są przechowywane w chmurze, więc nie musisz martwić się o szczegóły dotyczące tego, jak są przechowywane lub zarządzane. Możesz skupić się na budowaniu swoich aplikacji i rozwiązań.

- **Bezpieczeństwo**: Dataverse zapewnia bezpieczną i opartą na chmurze opcję przechowywania danych. Możesz kontrolować, kto ma dostęp do danych w twoich tabelach i jak mogą uzyskać dostęp, używając zabezpieczeń opartych na rolach.

- **Bogate metadane**: Typy danych i relacje są używane bezpośrednio w Power Apps

- **Logika i walidacja**: Możesz używać reguł biznesowych, obliczanych pól i reguł walidacji, aby egzekwować logikę biznesową i utrzymywać dokładność danych.

Teraz, gdy wiesz, czym jest Dataverse i dlaczego powinieneś go używać, przyjrzyjmy się, jak możesz użyć Copilota do utworzenia tabeli w Dataverse, aby spełnić wymagania naszego zespołu finansowego.

> **Uwaga** : Będziesz używać tej tabeli w następnej sekcji do zbudowania automatyzacji, która wyodrębni wszystkie informacje z faktury i przechowa je w tabeli.

Aby utworzyć tabelę w Dataverse za pomocą Copilota, wykonaj poniższe kroki:

1. Przejdź do ekranu głównego [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

2. Na lewym pasku nawigacyjnym wybierz **Tabele**, a następnie kliknij **Opisz nową tabelę**.

![Wybierz nową tabelę](../../images/describe-new-table.png?WT.mc_id=academic-105485-koreyst)

1. Na ekranie **Opisz nową tabelę** użyj pola tekstowego, aby opisać tabelę, którą chcesz utworzyć. Na przykład, **_Chcę utworzyć tabelę do przechowywania informacji o fakturach_**. Kliknij przycisk **Wyślij**, aby wysłać prompt do AI Copilot.

![Opisz tabelę](../../images/copilot-chat-prompt-dataverse.png?WT.mc_id=academic-105485-koreyst)

1. AI Copilot zasugeruje tabelę Dataverse z polami, których potrzebujesz do przechowywania danych, które chcesz śledzić, oraz przykładowe dane. Możesz następnie dostosować tabelę do swoich potrzeb, korzystając z funkcji asystenta AI Copilot poprzez kroki konwersacyjne.

![Sugerowana tabela Dataverse](../../images/copilot-dataverse-table.png?WT.mc_id=academic-105485-koreyst)

1. Zespół finansowy chce wysyłać e-mail do dostawcy, aby informować go o aktualnym statusie ich faktury. Możesz użyć Copilota, aby dodać nowe pole do tabeli do przechowywania adresu e-mail dostawcy. Na przykład, możesz użyć następującego promptu, aby dodać nowe pole do tabeli: **_Chcę dodać kolumnę do przechowywania adresu e-mail dostawcy_**. Kliknij przycisk **Wyślij**, aby wysłać prompt do AI Copilot.

1. AI Copilot wygeneruje nowe pole i możesz następnie dostosować pole do swoich potrzeb.

1. Po zakończeniu pracy z tabelą kliknij przycisk **Utwórz**, aby utworzyć tabelę.

## Modele SI w Power Platform z AI Builder

AI Builder to niskokodowa możliwość SI dostępna w Power Platform, która umożliwia korzystanie z modeli SI, aby pomóc w automatyzacji procesów i przewidywaniu wyników. Dzięki AI Builder możesz wprowadzić SI do swoich aplikacji i przepływów, które łączą się z Twoimi danymi w Dataverse lub w różnych źródłach danych w chmurze, takich jak SharePoint, OneDrive czy Azure.

## Gotowe modele SI vs Niestandardowe modele SI

AI Builder oferuje dwa rodzaje modeli SI: Gotowe modele SI i Niestandardowe modele SI. Gotowe modele SI to modele gotowe do użycia, które są trenowane przez Microsoft i dostępne w Power Platform. Pomagają one dodać inteligencję do Twoich aplikacji i przepływów bez konieczności zbierania danych, a następnie budowania, trenowania i publikowania własnych modeli. Możesz używać tych modeli do automatyzacji procesów i przewidywania wyników.

Niektóre z Gotowych modeli SI dostępnych w Power Platform obejmują:

- **Ekstrakcja kluczowych fraz**: Ten model wyodrębnia kluczowe frazy z tekstu.
- **Wykrywanie języka**: Ten model wykrywa język tekstu.
- **Analiza sentymentu**: Ten model wykrywa pozytywny, negatywny, neutralny lub mieszany sentyment w tekście.
- **Czytnik wizytówek**: Ten model wyodrębnia informacje z wizytówek.
- **Rozpoznawanie tekstu**: Ten model wyodrębnia tekst z obrazów.
- **Wykrywanie obiektów**: Ten model wykrywa i wyodrębnia obiekty z obrazów.
- **Przetwarzanie dokumentów**: Ten model wyodrębnia informacje z formularzy.
- **Przetwarzanie faktur**: Ten model wyodrębnia informacje z faktur.

Dzięki Niestandardowym modelom SI możesz wprowadzić własny model do AI Builder, aby mógł funkcjonować jak każdy niestandardowy model AI Builder, co pozwala na trenowanie modelu przy użyciu własnych danych. Możesz używać tych modeli do automatyzacji procesów i przewidywania wyników zarówno w Power Apps, jak i Power Automate. Podczas korzystania z własnego modelu istnieją pewne ograniczenia. Przeczytaj więcej o tych [ograniczeniach](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

![Modele AI builder](../../images/ai-builder-models.png?WT.mc_id=academic-105485-koreyst)

## Projekt 2: Przepływ Przetwarzania Faktur z AI Builder

## Zadanie 2 - Zbuduj Przepływ Przetwarzania Faktur dla Naszego Startupu

Zespół finansowy ma trudności z przetwarzaniem faktur. Używali arkusza kalkulacyjnego do śledzenia faktur, ale stało się to trudne do zarządzania wraz ze wzrostem liczby faktur. Poprosili Cię o zbudowanie przepływu pracy, który pomoże im przetwarzać faktury przy użyciu SI. Przepływ pracy powinien umożliwiać im wyodrębnianie informacji z faktur i przechowywanie tych informacji w tabeli Dataverse. Przepływ pracy powinien również umożliwiać im wysyłanie e-maila do zespołu finansowego z wyodrębnionymi informacjami.

Teraz, gdy wiesz, czym jest AI Builder i dlaczego powinieneś go używać, przyjrzyjmy się, jak możesz użyć Modelu SI Przetwarzania Faktur w AI Builder, który omówiliśmy wcześniej, do zbudowania przepływu pracy, który pomoże zespołowi finansowemu przetwarzać faktury.

Aby zbudować przepływ pracy, który pomoże zespołowi finansowemu przetwarzać faktury przy użyciu Modelu SI Przetwarzania Faktur w AI Builder, wykonaj poniższe kroki:

1. Przejdź do ekranu głównego [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst).

2. Użyj pola tekstowego na ekranie głównym, aby opisać przepływ pracy, który chcesz zbudować. Na przykład, **_Przetwarzaj fakturę, gdy pojawia się w mojej skrzynce odbiorczej_**. Kliknij przycisk **Wyślij**, aby wysłać prompt do AI Copilot.

   ![Copilot power automate](../../images/copilot-chat-prompt-powerautomate.png?WT.mc_id=academic-105485-koreyst)

3. AI Copilot zasugeruje akcje, których potrzebujesz do wykonania zadania, które chcesz zautomatyzować. Możesz kliknąć przycisk **Dalej**, aby przejść przez kolejne kroki.

4. W następnym kroku Power Automate poprosi Cię o skonfigurowanie połączeń wymaganych dla przepływu. Po zakończeniu kliknij przycisk **Utwórz przepływ**, aby utworzyć przepływ.

5. AI Copilot wygeneruje przepływ i możesz następnie dostosować przepływ do swoich potrzeb.

6. Zaktualizuj wyzwalacz przepływu i ustaw **Folder** na folder, w którym będą przechowywane faktury. Na przykład, możesz ustawić folder na **Odebrane**. Kliknij **Pokaż opcje zaawansowane** i ustaw **Tylko z załącznikami** na **Tak**. Zapewni to, że przepływ uruchomi się tylko wtedy, gdy w folderze zostanie odebrany e-mail z załącznikiem.

7. Usuń następujące akcje z przepływu: **HTML na tekst**, **Utwórz**, **Utwórz 2**, **Utwórz 3** i **Utwórz 4**, ponieważ nie będziesz ich używać.

8. Usuń akcję **Warunek** z przepływu, ponieważ nie będziesz jej używać. Powinno to wyglądać jak na poniższym zrzucie ekranu:

   ![power automate, usuń akcje](../../images/powerautomate-remove-actions.png?WT.mc_id=academic-105485-koreyst)

9. Kliknij przycisk **Dodaj akcję** i wyszukaj **Dataverse**. Wybierz akcję **Dodaj nowy wiersz**.

10. W akcji **Wyodrębnij informacje z faktur** zaktualizuj **Plik faktury**, aby wskazywał na **Zawartość załącznika** z e-maila. Zapewni to, że przepływ wyodrębni informacje z załącznika faktury.

11. Wybierz **Tabelę**, którą utworzyłeś wcześniej. Na przykład, możesz wybrać tabelę **Informacje o fakturze**. Wybierz dynamiczną zawartość z poprzedniej akcji, aby wypełnić następujące pola:

    - ID
    - Kwota
    - Data
    - Nazwa
    - Status - Ustaw **Status** na **Oczekujący**.
    - E-mail dostawcy - Użyj dynamicznej zawartości **Od** z wyzwalacza **Gdy nadejdzie nowy e-mail**.

    ![power automate dodaj wiersz](../../images/powerautomate-add-row.png?WT.mc_id=academic-105485-koreyst)

12. Po zakończeniu pracy z przepływem kliknij przycisk **Zapisz**, aby zapisać przepływ. Możesz następnie przetestować przepływ, wysyłając e-mail z fakturą do folderu, który określiłeś w wyzwalaczu.

> **Twoje zadanie domowe**: Przepływ, który właśnie zbudowałeś, to dobry początek, teraz musisz pomyśleć, jak możesz zbudować automatyzację, która umożliwi naszemu zespołowi finansowemu wysyłanie e-maila do dostawcy, aby informować go o aktualnym statusie ich faktury. Twoja wskazówka: przepływ musi uruchamiać się, gdy status faktury zmienia się.

## Użyj Modelu SI Generowania Tekstu w Power Automate

Model SI Tworzenia Tekstu z GPT w AI Builder umożliwia generowanie tekstu na podstawie promptu i jest zasilany przez usługę Microsoft Azure OpenAI. Dzięki tej możliwości możesz włączyć technologię GPT (Generative Pre-Trained Transformer) do swoich aplikacji i przepływów, aby budować różnorodne zautomatyzowane przepływy i wartościowe aplikacje.

Modele GPT przechodzą rozległe szkolenie na ogromnych ilościach danych, co umożliwia im tworzenie tekstu, który ściśle przypomina język ludzki, gdy podany jest prompt. Gdy są zintegrowane z automatyzacją przepływu pracy, modele SI takie jak GPT mogą być wykorzystane do usprawnienia i automatyzacji szerokiego zakresu zadań.

Na przykład, możesz budować przepływy do automatycznego generowania tekstu dla różnych przypadków użycia, takich jak: szkice e-maili, opisy produktów i więcej. Możesz również użyć modelu do generowania tekstu dla różnych aplikacji, takich jak chatboty i aplikacje obsługi klienta, które umożliwiają agentom obsługi klienta skuteczne i efektywne odpowiadanie na zapytania klientów.

![utwórz prompt](../../images/create-prompt-gpt.png?WT.mc_id=academic-105485-koreyst)

Aby dowiedzieć się, jak używać tego Modelu SI w Power Automate, przejdź przez moduł [Dodaj inteligencję z AI Builder i GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Świetna praca! Kontynuuj naukę

Po ukończeniu tej lekcji sprawdź naszą [Kolekcję nauki Generatywnej SI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby kontynuować pogłębianie wiedzy na temat Generatywnej SI!

Przejdź do Lekcji 11, gdzie przyjrzymy się, jak [integrować Generatywną SI z Wywołaniami Funkcji](../../../11-integrating-with-function-calling/translations/pl/README.md?WT.mc_id=academic-105485-koreyst)!
