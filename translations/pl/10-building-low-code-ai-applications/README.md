<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f5ff3b6204a695a117d6f452403c95f7",
  "translation_date": "2025-06-25T18:38:44+00:00",
  "source_file": "10-building-low-code-ai-applications/README.md",
  "language_code": "pl"
}
-->
# Tworzenie aplikacji AI o niskim kodzie

## Wprowadzenie

Teraz, gdy nauczyliśmy się budować aplikacje generujące obrazy, porozmawiajmy o niskim kodzie. Generatywna AI może być używana w różnych obszarach, w tym w niskim kodzie, ale czym jest niski kod i jak można dodać do niego AI?

Tworzenie aplikacji i rozwiązań stało się łatwiejsze zarówno dla tradycyjnych programistów, jak i osób bez doświadczenia programistycznego dzięki platformom rozwoju niskiego kodu. Platformy te umożliwiają budowanie aplikacji i rozwiązań z niewielką ilością kodu lub bez niego, oferując środowisko wizualnego rozwoju, które pozwala na przeciąganie i upuszczanie komponentów w celu tworzenia aplikacji i rozwiązań. Dzięki temu można tworzyć aplikacje i rozwiązania szybciej i z mniejszymi zasobami. W tej lekcji zgłębimy, jak używać niskiego kodu i jak ulepszyć rozwój niskiego kodu za pomocą AI przy użyciu Power Platform.

Power Platform daje organizacjom możliwość umożliwienia zespołom budowania własnych rozwiązań w intuicyjnym środowisku niskiego kodu lub bez kodu. To środowisko pomaga uprościć proces tworzenia rozwiązań. Dzięki Power Platform, rozwiązania można budować w ciągu dni lub tygodni, zamiast miesięcy czy lat. Power Platform składa się z pięciu kluczowych produktów: Power Apps, Power Automate, Power BI, Power Pages i Copilot Studio.

Ta lekcja obejmuje:

- Wprowadzenie do generatywnej AI w Power Platform
- Wprowadzenie do Copilot i jak go używać
- Użycie generatywnej AI do budowy aplikacji i przepływów w Power Platform
- Zrozumienie modeli AI w Power Platform z AI Builder

## Cele nauki

Pod koniec tej lekcji będziesz w stanie:

- Zrozumieć, jak działa Copilot w Power Platform.

- Zbudować aplikację do śledzenia zadań dla studentów dla naszego startupu edukacyjnego.

- Zbudować przepływ przetwarzania faktur, który wykorzystuje AI do wyodrębniania informacji z faktur.

- Stosować najlepsze praktyki podczas korzystania z modelu AI GPT do tworzenia tekstu.

Narzędzia i technologie, które wykorzystasz w tej lekcji, to:

- **Power Apps**, do aplikacji do śledzenia zadań dla studentów, która zapewnia środowisko rozwoju niskiego kodu do tworzenia aplikacji do śledzenia, zarządzania i interakcji z danymi.

- **Dataverse**, do przechowywania danych dla aplikacji do śledzenia zadań dla studentów, gdzie Dataverse zapewni platformę danych niskiego kodu do przechowywania danych aplikacji.

- **Power Automate**, do przepływu przetwarzania faktur, gdzie będziesz mieć środowisko rozwoju niskiego kodu do budowania przepływów pracy w celu automatyzacji procesu przetwarzania faktur.

- **AI Builder**, do modelu AI przetwarzania faktur, gdzie będziesz używać wbudowanych modeli AI do przetwarzania faktur dla naszego startupu.

## Generatywna AI w Power Platform

Ulepszanie rozwoju niskiego kodu i aplikacji za pomocą generatywnej AI to kluczowy obszar dla Power Platform. Celem jest umożliwienie każdemu budowania aplikacji zasilanych AI, stron, pulpitów i automatyzacji procesów z AI, _bez potrzeby posiadania wiedzy z zakresu nauki o danych_. Cel ten jest realizowany poprzez integrację generatywnej AI z doświadczeniem rozwoju niskiego kodu w Power Platform w postaci Copilot i AI Builder.

### Jak to działa?

Copilot to asystent AI, który umożliwia budowanie rozwiązań Power Platform poprzez opisywanie swoich wymagań w serii kroków konwersacyjnych przy użyciu języka naturalnego. Możesz na przykład polecić swojemu asystentowi AI, aby określił, jakie pola będzie używać twoja aplikacja, a on stworzy zarówno aplikację, jak i model danych, lub możesz określić, jak ustawić przepływ w Power Automate.

Możesz używać funkcji opartych na Copilot jako funkcji w ekranach aplikacji, aby umożliwić użytkownikom odkrywanie wglądów poprzez interakcje konwersacyjne.

AI Builder to możliwość AI o niskim kodzie dostępna w Power Platform, która umożliwia używanie modeli AI do automatyzacji procesów i przewidywania wyników. Dzięki AI Builder możesz wprowadzać AI do swoich aplikacji i przepływów, które łączą się z danymi w Dataverse lub w różnych źródłach danych w chmurze, takich jak SharePoint, OneDrive czy Azure.

Copilot jest dostępny we wszystkich produktach Power Platform: Power Apps, Power Automate, Power BI, Power Pages i Power Virtual Agents. AI Builder jest dostępny w Power Apps i Power Automate. W tej lekcji skupimy się na tym, jak używać Copilot i AI Builder w Power Apps i Power Automate do budowania rozwiązania dla naszego startupu edukacyjnego.

### Copilot w Power Apps

Jako część Power Platform, Power Apps zapewnia środowisko rozwoju niskiego kodu do budowania aplikacji do śledzenia, zarządzania i interakcji z danymi. To zestaw usług do tworzenia aplikacji z możliwością skalowania platformy danych i możliwością łączenia się z usługami w chmurze i danymi lokalnymi. Power Apps pozwala na tworzenie aplikacji działających w przeglądarkach, tabletach i telefonach, które można udostępniać współpracownikom. Power Apps ułatwia użytkownikom rozwój aplikacji dzięki prostemu interfejsowi, dzięki czemu każdy użytkownik biznesowy lub profesjonalny programista może tworzyć aplikacje dostosowane do swoich potrzeb. Doświadczenie tworzenia aplikacji jest również ulepszane dzięki Generatywnej AI za pomocą Copilot.

Funkcja asystenta AI Copilot w Power Apps umożliwia opisanie, jakiego rodzaju aplikacji potrzebujesz i jakie informacje chcesz, aby twoja aplikacja śledziła, zbierała lub pokazywała. Copilot generuje wtedy responsywną aplikację Canvas na podstawie twojego opisu. Możesz następnie dostosować aplikację do swoich potrzeb. AI Copilot generuje również i sugeruje tabelę Dataverse z polami, które potrzebujesz do przechowywania danych, które chcesz śledzić, oraz niektórymi danymi przykładowymi. W dalszej części tej lekcji przyjrzymy się, czym jest Dataverse i jak można go używać w Power Apps. Możesz następnie dostosować tabelę do swoich potrzeb, korzystając z funkcji asystenta AI Copilot w ramach kroków konwersacyjnych. Funkcja ta jest łatwo dostępna z ekranu głównego Power Apps.

### Copilot w Power Automate

Jako część Power Platform, Power Automate pozwala użytkownikom tworzyć zautomatyzowane przepływy pracy między aplikacjami i usługami. Pomaga to w automatyzacji powtarzalnych procesów biznesowych, takich jak komunikacja, zbieranie danych i zatwierdzanie decyzji. Jego prosty interfejs pozwala użytkownikom o różnym poziomie kompetencji technicznych (od początkujących po doświadczonych programistów) na automatyzację zadań roboczych. Doświadczenie tworzenia przepływów pracy jest również ulepszane dzięki Generatywnej AI za pomocą Copilot.

Funkcja asystenta AI Copilot w Power Automate umożliwia opisanie, jakiego rodzaju przepływu potrzebujesz i jakie działania chcesz, aby twój przepływ wykonał. Copilot generuje wtedy przepływ na podstawie twojego opisu. Możesz następnie dostosować przepływ do swoich potrzeb. AI Copilot generuje również i sugeruje działania, które musisz wykonać, aby zautomatyzować zadanie, które chcesz zautomatyzować. W dalszej części tej lekcji przyjrzymy się, czym są przepływy i jak można je używać w Power Automate. Możesz następnie dostosować działania do swoich potrzeb, korzystając z funkcji asystenta AI Copilot w ramach kroków konwersacyjnych. Funkcja ta jest łatwo dostępna z ekranu głównego Power Automate.

## Zadanie: Zarządzanie zadaniami studenckimi i fakturami dla naszego startupu, używając Copilot

Nasz startup oferuje kursy online dla studentów. Startup szybko się rozwija i obecnie ma trudności z nadążaniem za zapotrzebowaniem na swoje kursy. Zatrudniono cię jako dewelopera Power Platform, aby pomóc im zbudować rozwiązanie o niskim kodzie, które pomoże im zarządzać zadaniami studenckimi i fakturami. Ich rozwiązanie powinno umożliwiać śledzenie i zarządzanie zadaniami studenckimi za pomocą aplikacji oraz automatyzację procesu przetwarzania faktur za pomocą przepływu pracy. Poproszono cię o użycie Generatywnej AI do opracowania rozwiązania.

Kiedy zaczynasz korzystać z Copilot, możesz skorzystać z [biblioteki promptów Copilot Power Platform](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko), aby zacząć korzystać z promptów. Ta biblioteka zawiera listę promptów, które możesz użyć do budowania aplikacji i przepływów za pomocą Copilot. Możesz również użyć promptów z biblioteki, aby uzyskać pomysł, jak opisać swoje wymagania dla Copilot.

### Zbuduj aplikację do śledzenia zadań studenckich dla naszego startupu

Nauczyciele w naszym startupie mają trudności z śledzeniem zadań studenckich. Używali arkusza kalkulacyjnego do śledzenia zadań, ale to stało się trudne do zarządzania, ponieważ liczba studentów wzrosła. Poprosili cię o zbudowanie aplikacji, która pomoże im śledzić i zarządzać zadaniami studenckimi. Aplikacja powinna umożliwiać dodawanie nowych zadań, przeglądanie zadań, aktualizowanie zadań i usuwanie zadań. Aplikacja powinna również umożliwiać nauczycielom i studentom przeglądanie zadań, które zostały ocenione, i tych, które nie zostały ocenione.

Zbudujesz aplikację używając Copilot w Power Apps, postępując zgodnie z poniższymi krokami:

1. Przejdź do ekranu głównego [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

1. Użyj pola tekstowego na ekranie głównym, aby opisać aplikację, którą chcesz zbudować. Na przykład, **_Chcę zbudować aplikację do śledzenia i zarządzania zadaniami studenckimi_**. Kliknij przycisk **Wyślij**, aby wysłać prompt do AI Copilot.

1. AI Copilot zasugeruje tabelę Dataverse z polami, których potrzebujesz do przechowywania danych, które chcesz śledzić, oraz niektórymi danymi przykładowymi. Możesz następnie dostosować tabelę do swoich potrzeb, korzystając z funkcji asystenta AI Copilot w ramach kroków konwersacyjnych.

   > **Ważne**: Dataverse to podstawowa platforma danych dla Power Platform. Jest to platforma danych o niskim kodzie do przechowywania danych aplikacji. Jest to w pełni zarządzana usługa, która bezpiecznie przechowuje dane w chmurze Microsoft i jest udostępniana w ramach twojego środowiska Power Platform. Posiada wbudowane funkcje zarządzania danymi, takie jak klasyfikacja danych, rodowód danych, precyzyjna kontrola dostępu i wiele innych. Możesz dowiedzieć się więcej o Dataverse [tutaj](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

1. Nauczyciele chcą wysyłać e-maile do studentów, którzy złożyli swoje zadania, aby informować ich o postępach ich zadań. Możesz użyć Copilot, aby dodać nowe pole do tabeli do przechowywania e-maila studenta. Na przykład, możesz użyć następującego promptu, aby dodać nowe pole do tabeli: **_Chcę dodać kolumnę do przechowywania e-maila studenta_**. Kliknij przycisk **Wyślij**, aby wysłać prompt do AI Copilot.

1. AI Copilot wygeneruje nowe pole, a następnie możesz dostosować pole do swoich potrzeb.

1. Po zakończeniu pracy z tabelą kliknij przycisk **Utwórz aplikację**, aby utworzyć aplikację.

1. AI Copilot wygeneruje responsywną aplikację Canvas na podstawie twojego opisu. Możesz następnie dostosować aplikację do swoich potrzeb.

1. Aby nauczyciele mogli wysyłać e-maile do studentów, możesz użyć Copilot, aby dodać nowy ekran do aplikacji. Na przykład, możesz użyć następującego promptu, aby dodać nowy ekran do aplikacji: **_Chcę dodać ekran do wysyłania e-maili do studentów_**. Kliknij przycisk **Wyślij**, aby wysłać prompt do AI Copilot.

1. AI Copilot wygeneruje nowy ekran, a następnie możesz dostosować ekran do swoich potrzeb.

1. Po zakończeniu pracy z aplikacją kliknij przycisk **Zapisz**, aby zapisać aplikację.

1. Aby udostępnić aplikację nauczycielom, kliknij przycisk **Udostępnij**, a następnie ponownie kliknij przycisk **Udostępnij**. Możesz następnie udostępnić aplikację nauczycielom, wpisując ich adresy e-mail.

> **Twoje zadanie domowe**: Aplikacja, którą właśnie zbudowałeś, to dobry początek, ale można ją ulepszyć. Dzięki funkcji e-mailowej nauczyciele mogą wysyłać e-maile do studentów tylko ręcznie, musząc wpisywać ich adresy e-mail. Czy możesz użyć Copilot, aby zbudować automatyzację, która umożliwi nauczycielom automatyczne wysyłanie e-maili do studentów, gdy złożą swoje zadania? Twoja wskazówka: przy odpowiednim promptu możesz użyć Copilot w Power Automate, aby to zbudować.

### Zbuduj tabelę informacji o fakturach dla naszego startupu

Zespół finansowy naszego startupu ma trudności z śledzeniem faktur. Używali arkusza kalkulacyjnego do śledzenia faktur, ale to stało się trudne do zarządzania, ponieważ liczba faktur wzrosła. Poprosili cię o zbudowanie tabeli, która pomoże im przechowywać, śledzić i zarządzać informacjami o otrzymanych fakturach. Tabela powinna być używana do budowania automatyzacji, która wyodrębni wszystkie informacje o fakturach i przechowa je w tabeli. Tabela powinna również umożliwiać zespołowi finansowemu przeglądanie faktur, które zostały opłacone, i tych, które nie zostały opłacone.

Power Platform ma podstawową platformę danych zwaną Dataverse, która umożliwia przechowywanie danych dla twoich aplikacji i rozwiązań. Dataverse zapewnia platformę danych o niskim kodzie do przechowywania danych aplikacji. Jest to w pełni zarządzana usługa, która bezpiecznie przechowuje dane w chmurze Microsoft i jest udostępniana w ramach twojego środowiska Power Platform. Posiada wbudowane funkcje zarządzania danymi, takie jak klasyfikacja danych, rodowód danych, precyzyjna kontrola dostępu i wiele innych. Możesz dowiedzieć się więcej [o Dataverse tutaj](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Dlaczego powinniśmy używać Dataverse dla naszego startupu? Standardowe i niestandardowe tabele w Dataverse zapewniają bezpieczną i opartą na chmurze opcję przechowywania danych. Tabele pozwalają na przechowywanie różnych typów danych, podobnie jak można używać wielu arkuszy w jednym skoroszycie Excel. Możesz używać tabel do przechowywania danych, które są specyficzne dla twojej organizacji lub potrzeb biznesowych. Niektóre z korzyści, jakie nasz startup uzyska z używania Dataverse, to między innymi:

- **Łatwe zarządzanie**: Zarówno metadane, jak i dane są przechowywane w chmurze, więc nie musisz martwić się o szczegóły dotyczące ich przechowywania lub zarządzania. Możesz skupić się na budowaniu swoich aplikacji i rozwiązań.

- **Bezpieczeństwo**: Dataverse zapewnia bezpieczną i opartą na chmurze opcję przechowywania danych. Możesz kontrolować, kto ma dostęp do danych w twoich tabelach i jak mogą z nich korzystać, używając bezpieczeństwa opartego na rolach.

- **Bogate metadane**: Typy danych i
- **Analiza Sentimentu**: Ten model wykrywa pozytywny, negatywny, neutralny lub mieszany nastrój w tekście.  
- **Czytnik Wizytówek**: Ten model wyciąga informacje z wizytówek.  
- **Rozpoznawanie Tekstu**: Ten model wyciąga tekst z obrazów.  
- **Wykrywanie Obiektów**: Ten model wykrywa i wyciąga obiekty z obrazów.  
- **Przetwarzanie Dokumentów**: Ten model wyciąga informacje z formularzy.  
- **Przetwarzanie Faktur**: Ten model wyciąga informacje z faktur.  

Dzięki Własnym Modelom AI możesz wprowadzić swój model do AI Builder, aby działał jak każdy niestandardowy model AI Builder, umożliwiając trenowanie modelu przy użyciu własnych danych. Możesz używać tych modeli do automatyzacji procesów i przewidywania wyników zarówno w Power Apps, jak i Power Automate. Przy używaniu własnego modelu obowiązują pewne ograniczenia. Przeczytaj więcej o tych [ograniczeniach](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

## Zadanie #2 - Zbuduj Przepływ Przetwarzania Faktur dla Naszego Startupu

Zespół finansowy ma trudności z przetwarzaniem faktur. Używali arkusza kalkulacyjnego do śledzenia faktur, ale zarządzanie tym stało się trudne, gdy liczba faktur wzrosła. Poprosili Cię o stworzenie przepływu pracy, który pomoże im przetwarzać faktury za pomocą AI. Przepływ powinien umożliwiać wyciąganie informacji z faktur i przechowywanie ich w tabeli Dataverse. Przepływ powinien także umożliwiać wysyłanie e-maila do zespołu finansowego z wyciągniętymi informacjami.

Teraz, gdy wiesz, czym jest AI Builder i dlaczego warto go używać, przyjrzyjmy się, jak można użyć Modelu Przetwarzania Faktur AI Builder, który omawialiśmy wcześniej, do zbudowania przepływu, który pomoże zespołowi finansowemu w przetwarzaniu faktur.

Aby zbudować przepływ, który pomoże zespołowi finansowemu przetwarzać faktury przy użyciu Modelu Przetwarzania Faktur AI Builder, wykonaj poniższe kroki:

1. Przejdź do ekranu głównego [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst).
2. Użyj obszaru tekstowego na ekranie głównym, aby opisać przepływ, który chcesz zbudować. Na przykład, **_Przetwarzaj fakturę, gdy pojawi się w mojej skrzynce odbiorczej_**. Kliknij przycisk **Wyślij**, aby wysłać polecenie do AI Copilot.
3. AI Copilot zasugeruje działania, które musisz wykonać, aby zautomatyzować zadanie. Możesz kliknąć przycisk **Dalej**, aby przejść przez kolejne kroki.
4. W kolejnym kroku Power Automate poprosi Cię o skonfigurowanie połączeń wymaganych dla przepływu. Po zakończeniu kliknij przycisk **Utwórz przepływ**, aby go utworzyć.
5. AI Copilot wygeneruje przepływ, który możesz następnie dostosować do swoich potrzeb.
6. Zaktualizuj wyzwalacz przepływu i ustaw **Folder** na folder, w którym będą przechowywane faktury. Na przykład możesz ustawić folder na **Skrzynka odbiorcza**. Kliknij **Pokaż opcje zaawansowane** i ustaw **Tylko z załącznikami** na **Tak**. To zapewni, że przepływ będzie działał tylko wtedy, gdy w folderze zostanie odebrany e-mail z załącznikiem.
7. Usuń następujące działania z przepływu: **HTML do tekstu**, **Compose**, **Compose 2**, **Compose 3** i **Compose 4**, ponieważ nie będziesz ich używać.
8. Usuń działanie **Condition** z przepływu, ponieważ nie będziesz go używać. Powinno to wyglądać jak na poniższym zrzucie ekranu:
9. Kliknij przycisk **Dodaj działanie** i wyszukaj **Dataverse**. Wybierz działanie **Dodaj nowy wiersz**.
10. Na działaniu **Wyciągnij informacje z faktur** zaktualizuj **Plik faktury**, aby wskazywał na **Zawartość załącznika** z e-maila. To zapewni, że przepływ wyciągnie informacje z załącznika faktury.
11. Wybierz **Tabelę**, którą utworzyłeś wcześniej. Na przykład możesz wybrać tabelę **Informacje o fakturze**. Wybierz dynamiczną zawartość z poprzedniego działania, aby wypełnić następujące pola:  
    - ID  
    - Kwota  
    - Data  
    - Nazwa  
    - Status  
    - Ustaw **Status** na **Oczekujący**.  
    - E-mail dostawcy  
    - Użyj dynamicznej zawartości **Od** z wyzwalacza **Kiedy przychodzi nowy e-mail**.  
12. Po zakończeniu przepływu kliknij przycisk **Zapisz**, aby go zapisać. Możesz następnie przetestować przepływ, wysyłając e-mail z fakturą do folderu, który określiłeś w wyzwalaczu.

> **Twoje zadanie domowe**: Przepływ, który właśnie zbudowałeś, to dobry początek. Teraz musisz pomyśleć, jak zbudować automatyzację, która umożliwi naszemu zespołowi finansowemu wysłanie e-maila do dostawcy, aby zaktualizować go o bieżący status jego faktury. Twoja wskazówka: przepływ musi działać, gdy status faktury się zmienia.

## Użyj Modelu AI do Generowania Tekstu w Power Automate

Model AI do Tworzenia Tekstu z GPT w AI Builder umożliwia generowanie tekstu na podstawie polecenia i jest zasilany przez Microsoft Azure OpenAI Service. Dzięki tej funkcji możesz włączyć technologię GPT (Generative Pre-Trained Transformer) do swoich aplikacji i przepływów, aby tworzyć różnorodne zautomatyzowane przepływy i aplikacje wnikliwe.

Modele GPT przechodzą intensywne szkolenie na ogromnych ilościach danych, co pozwala im na produkcję tekstu, który blisko przypomina język ludzki, gdy otrzymają polecenie. Po zintegrowaniu z automatyzacją przepływu pracy, modele AI, takie jak GPT, mogą być wykorzystywane do usprawnienia i automatyzacji szerokiego zakresu zadań.

Na przykład, możesz zbudować przepływy do automatycznego generowania tekstu dla różnych zastosowań, takich jak: szkice e-maili, opisy produktów i inne. Możesz także użyć modelu do generowania tekstu dla różnych aplikacji, takich jak chatboty i aplikacje obsługi klienta, które umożliwiają agentom obsługi klienta skuteczne i efektywne odpowiadanie na zapytania klientów.

Aby dowiedzieć się, jak używać tego Modelu AI w Power Automate, przejdź przez moduł [Dodaj inteligencję z AI Builder i GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Świetna Robota! Kontynuuj Nauczanie

Po ukończeniu tej lekcji, zapoznaj się z naszą [kolekcją nauki o Generatywnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej rozwijać swoją wiedzę o Generatywnej AI!

Przejdź do Lekcji 11, gdzie przyjrzymy się, jak [zintegrować Generatywną AI z Wywoływaniem Funkcji](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest profesjonalne tłumaczenie przez człowieka. Nie ponosimy odpowiedzialności za wszelkie nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.