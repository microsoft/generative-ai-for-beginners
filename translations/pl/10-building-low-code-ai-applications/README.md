<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f5ff3b6204a695a117d6f452403c95f7",
  "translation_date": "2025-05-19T10:41:39+00:00",
  "source_file": "10-building-low-code-ai-applications/README.md",
  "language_code": "pl"
}
-->
# Budowanie aplikacji AI przy użyciu niskiego kodu

## Wprowadzenie

Teraz, gdy nauczyliśmy się budować aplikacje generujące obrazy, porozmawiajmy o niskim kodzie. Generatywna AI może być używana w różnych dziedzinach, w tym w niskim kodzie, ale czym właściwie jest niski kod i jak możemy dodać do niego AI?

Budowanie aplikacji i rozwiązań stało się łatwiejsze dla tradycyjnych programistów i osób nie będących programistami dzięki platformom niskiego kodu. Platformy te umożliwiają budowanie aplikacji i rozwiązań przy użyciu niewielkiej ilości kodu lub bez niego. Osiąga się to poprzez zapewnienie wizualnego środowiska programistycznego, które umożliwia przeciąganie i upuszczanie komponentów do budowania aplikacji i rozwiązań. Dzięki temu można budować aplikacje i rozwiązania szybciej i z mniejszymi zasobami. W tej lekcji zagłębimy się w to, jak używać niskiego kodu i jak wzbogacić rozwój niskiego kodu o AI za pomocą Power Platform.

Power Platform daje organizacjom możliwość wzmocnienia swoich zespołów poprzez intuicyjne środowisko niskiego kodu lub bez kodu. To środowisko pomaga uprościć proces budowania rozwiązań. Z Power Platform rozwiązania mogą być budowane w ciągu dni lub tygodni zamiast miesięcy czy lat. Power Platform składa się z pięciu kluczowych produktów: Power Apps, Power Automate, Power BI, Power Pages i Copilot Studio.

Ta lekcja obejmuje:

- Wprowadzenie do Generatywnej AI w Power Platform
- Wprowadzenie do Copilot i jak go używać
- Wykorzystanie Generatywnej AI do budowania aplikacji i przepływów w Power Platform
- Zrozumienie modeli AI w Power Platform z AI Builder

## Cele nauki

Pod koniec tej lekcji będziesz w stanie:

- Zrozumieć, jak działa Copilot w Power Platform.

- Zbudować aplikację do śledzenia zadań uczniów dla naszego startupu edukacyjnego.

- Zbudować przepływ przetwarzania faktur, który używa AI do wyodrębniania informacji z faktur.

- Stosować najlepsze praktyki podczas używania modelu AI do tworzenia tekstu z GPT.

Narzędzia i technologie, które będziesz używać w tej lekcji to:

- **Power Apps**, dla aplikacji do śledzenia zadań uczniów, która zapewnia środowisko niskiego kodu do budowania aplikacji do śledzenia, zarządzania i interakcji z danymi.

- **Dataverse**, do przechowywania danych dla aplikacji do śledzenia zadań uczniów, gdzie Dataverse zapewni platformę danych niskiego kodu do przechowywania danych aplikacji.

- **Power Automate**, dla przepływu przetwarzania faktur, gdzie będziesz mieć środowisko niskiego kodu do budowania przepływów pracy do automatyzacji procesu przetwarzania faktur.

- **AI Builder**, dla modelu AI do przetwarzania faktur, gdzie będziesz używać wbudowanych modeli AI do przetwarzania faktur dla naszego startupu.

## Generatywna AI w Power Platform

Wzbogacenie rozwoju i aplikacji niskiego kodu o generatywną AI jest kluczowym obszarem dla Power Platform. Celem jest umożliwienie każdemu budowania aplikacji, stron, pulpitów nawigacyjnych i automatyzowania procesów z wykorzystaniem AI, _bez potrzeby posiadania wiedzy z zakresu data science_. Cel ten osiąga się poprzez integrację generatywnej AI z doświadczeniem niskiego kodu w Power Platform w postaci Copilot i AI Builder.

### Jak to działa?

Copilot to asystent AI, który umożliwia budowanie rozwiązań Power Platform poprzez opisanie swoich wymagań w serii kroków konwersacyjnych przy użyciu języka naturalnego. Możesz na przykład polecić swojemu asystentowi AI określenie, jakie pola będzie używać Twoja aplikacja, a on stworzy zarówno aplikację, jak i model danych. Możesz także określić, jak skonfigurować przepływ w Power Automate.

Funkcje napędzane przez Copilot mogą być używane jako funkcja w ekranach Twojej aplikacji, aby umożliwić użytkownikom odkrywanie wglądów poprzez interakcje konwersacyjne.

AI Builder to funkcjonalność AI niskiego kodu dostępna w Power Platform, która umożliwia użycie modeli AI do automatyzacji procesów i przewidywania wyników. Dzięki AI Builder możesz dodać AI do swoich aplikacji i przepływów, które łączą się z Twoimi danymi w Dataverse lub w różnych źródłach danych w chmurze, takich jak SharePoint, OneDrive czy Azure.

Copilot jest dostępny we wszystkich produktach Power Platform: Power Apps, Power Automate, Power BI, Power Pages i Power Virtual Agents. AI Builder jest dostępny w Power Apps i Power Automate. W tej lekcji skupimy się na tym, jak używać Copilot i AI Builder w Power Apps i Power Automate do budowania rozwiązania dla naszego startupu edukacyjnego.

### Copilot w Power Apps

Jako część Power Platform, Power Apps zapewnia środowisko niskiego kodu do budowania aplikacji do śledzenia, zarządzania i interakcji z danymi. To zestaw usług do tworzenia aplikacji z skalowalną platformą danych i możliwością łączenia się z usługami w chmurze i danymi lokalnymi. Power Apps pozwala na budowanie aplikacji, które działają w przeglądarkach, na tabletach i telefonach, i mogą być udostępniane współpracownikom. Power Apps ułatwia użytkownikom rozwój aplikacji dzięki prostemu interfejsowi, tak aby każdy użytkownik biznesowy lub profesjonalny programista mógł tworzyć aplikacje na zamówienie. Doświadczenie tworzenia aplikacji jest również wzbogacone o Generatywną AI dzięki Copilot.

Funkcja asystenta AI Copilot w Power Apps pozwala opisać, jakiego rodzaju aplikacji potrzebujesz i jakie informacje ma ona śledzić, zbierać lub wyświetlać. Copilot generuje wtedy responsywną aplikację Canvas na podstawie Twojego opisu. Możesz następnie dostosować aplikację do swoich potrzeb. AI Copilot generuje również i sugeruje tabelę Dataverse z polami potrzebnymi do przechowywania danych, które chcesz śledzić, oraz z przykładowymi danymi. W tej lekcji omówimy, czym jest Dataverse i jak można go używać w Power Apps. Możesz następnie dostosować tabelę do swoich potrzeb, używając funkcji asystenta AI Copilot poprzez kroki konwersacyjne. Ta funkcja jest łatwo dostępna z ekranu głównego Power Apps.

### Copilot w Power Automate

Jako część Power Platform, Power Automate pozwala użytkownikom tworzyć zautomatyzowane przepływy pracy między aplikacjami i usługami. Pomaga automatyzować powtarzalne procesy biznesowe, takie jak komunikacja, zbieranie danych i zatwierdzanie decyzji. Jego prosty interfejs pozwala użytkownikom o różnych poziomach kompetencji technicznych (od początkujących po doświadczonych programistów) automatyzować zadania pracy. Doświadczenie tworzenia przepływów pracy jest również wzbogacone o Generatywną AI dzięki Copilot.

Funkcja asystenta AI Copilot w Power Automate pozwala opisać, jakiego rodzaju przepływu potrzebujesz i jakie działania ma wykonywać. Copilot generuje wtedy przepływ na podstawie Twojego opisu. Możesz następnie dostosować przepływ do swoich potrzeb. AI Copilot generuje również i sugeruje działania, które są potrzebne do wykonania zadania, które chcesz zautomatyzować. Omówimy, czym są przepływy i jak można ich używać w Power Automate w tej lekcji. Możesz następnie dostosować działania do swoich potrzeb, używając funkcji asystenta AI Copilot poprzez kroki konwersacyjne. Ta funkcja jest łatwo dostępna z ekranu głównego Power Automate.

## Zadanie: Zarządzanie zadaniami uczniów i fakturami dla naszego startupu, używając Copilot

Nasz startup oferuje kursy online dla uczniów. Startup szybko się rozwija i obecnie ma trudności z nadążaniem za popytem na swoje kursy. Startup zatrudnił Cię jako dewelopera Power Platform, aby pomóc w stworzeniu rozwiązania niskiego kodu, które pomoże zarządzać zadaniami uczniów i fakturami. Rozwiązanie powinno umożliwiać śledzenie i zarządzanie zadaniami uczniów za pomocą aplikacji oraz automatyzację procesu przetwarzania faktur za pomocą przepływu pracy. Poproszono Cię o użycie Generatywnej AI do opracowania rozwiązania.

Zaczynając pracę z Copilot, możesz skorzystać z [Biblioteki Podpowiedzi Copilot Power Platform](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko), aby rozpocząć pracę z podpowiedziami. Ta biblioteka zawiera listę podpowiedzi, które możesz użyć do budowania aplikacji i przepływów z Copilot. Możesz również używać podpowiedzi z biblioteki, aby uzyskać pomysł, jak opisać swoje wymagania dla Copilot.

### Zbuduj aplikację do śledzenia zadań uczniów dla naszego startupu

Nauczyciele w naszym startupie mieli trudności z śledzeniem zadań uczniów. Używali arkusza kalkulacyjnego do śledzenia zadań, ale to stało się trudne do zarządzania, gdy liczba uczniów wzrosła. Poprosili Cię o zbudowanie aplikacji, która pomoże im śledzić i zarządzać zadaniami uczniów. Aplikacja powinna umożliwiać dodawanie nowych zadań, przeglądanie zadań, aktualizowanie zadań i usuwanie zadań. Aplikacja powinna również umożliwiać nauczycielom i uczniom przeglądanie zadań, które zostały ocenione, i tych, które nie zostały ocenione.

Zbudujesz aplikację używając Copilot w Power Apps, postępując zgodnie z poniższymi krokami:

1. Przejdź do ekranu głównego [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

1. Użyj obszaru tekstowego na ekranie głównym, aby opisać aplikację, którą chcesz zbudować. Na przykład, **_Chcę zbudować aplikację do śledzenia i zarządzania zadaniami uczniów_**. Kliknij przycisk **Wyślij**, aby wysłać podpowiedź do AI Copilot.

1. AI Copilot zasugeruje tabelę Dataverse z polami, które są potrzebne do przechowywania danych, które chcesz śledzić, oraz z przykładowymi danymi. Możesz następnie dostosować tabelę do swoich potrzeb, używając funkcji asystenta AI Copilot poprzez kroki konwersacyjne.

   > **Ważne**: Dataverse to podstawowa platforma danych dla Power Platform. Jest to platforma danych niskiego kodu do przechowywania danych aplikacji. Jest to w pełni zarządzana usługa, która bezpiecznie przechowuje dane w chmurze Microsoft i jest udostępniana w Twoim środowisku Power Platform. Oferuje wbudowane możliwości zarządzania danymi, takie jak klasyfikacja danych, pochodzenie danych, kontrola dostępu o wysokiej precyzji i więcej. Możesz dowiedzieć się więcej o Dataverse [tutaj](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

1. Nauczyciele chcą wysyłać e-maile do uczniów, którzy przesłali swoje zadania, aby informować ich o postępach w ich zadaniach. Możesz użyć Copilot, aby dodać nowe pole do tabeli, aby przechowywać e-mail ucznia. Na przykład, możesz użyć następującej podpowiedzi, aby dodać nowe pole do tabeli: **_Chcę dodać kolumnę do przechowywania e-maila ucznia_**. Kliknij przycisk **Wyślij**, aby wysłać podpowiedź do AI Copilot.

1. AI Copilot wygeneruje nowe pole, a Ty możesz następnie dostosować pole do swoich potrzeb.

1. Po zakończeniu pracy nad tabelą kliknij przycisk **Utwórz aplikację**, aby utworzyć aplikację.

1. AI Copilot wygeneruje responsywną aplikację Canvas na podstawie Twojego opisu. Możesz następnie dostosować aplikację do swoich potrzeb.

1. Aby nauczyciele mogli wysyłać e-maile do uczniów, możesz użyć Copilot, aby dodać nowy ekran do aplikacji. Na przykład, możesz użyć następującej podpowiedzi, aby dodać nowy ekran do aplikacji: **_Chcę dodać ekran do wysyłania e-maili do uczniów_**. Kliknij przycisk **Wyślij**, aby wysłać podpowiedź do AI Copilot.

1. AI Copilot wygeneruje nowy ekran, a Ty możesz następnie dostosować ekran do swoich potrzeb.

1. Po zakończeniu pracy nad aplikacją kliknij przycisk **Zapisz**, aby zapisać aplikację.

1. Aby udostępnić aplikację nauczycielom, kliknij przycisk **Udostępnij**, a następnie ponownie kliknij przycisk **Udostępnij**. Możesz następnie udostępnić aplikację nauczycielom, wpisując ich adresy e-mail.

> **Twoje zadanie domowe**: Aplikacja, którą właśnie zbudowałeś, to dobry początek, ale można ją ulepszyć. Dzięki funkcji e-mailowej nauczyciele mogą wysyłać e-maile do uczniów tylko ręcznie, musząc wpisywać ich adresy e-mail. Czy możesz użyć Copilot, aby zbudować automatyzację, która umożliwi nauczycielom automatyczne wysyłanie e-maili do uczniów, gdy przesyłają swoje zadania? Twoja wskazówka to odpowiednia podpowiedź, której możesz użyć w Power Automate, aby to zbudować.

### Zbuduj tabelę informacji o fakturach dla naszego startupu

Zespół finansowy naszego startupu miał trudności z śledzeniem faktur. Używali arkusza kalkulacyjnego do śledzenia faktur, ale to stało się trudne do zarządzania, gdy liczba faktur wzrosła. Poprosili Cię o zbudowanie tabeli, która pomoże im przechowywać, śledzić i zarządzać informacjami o otrzymanych fakturach. Tabela powinna być używana do zbudowania automatyzacji, która wyodrębni wszystkie informacje o fakturach i przechowa je w tabeli. Tabela powinna również umożliwiać zespołowi finansowemu przeglądanie faktur, które zostały opłacone, i tych, które nie zostały opłacone.

Power Platform ma podstawową platformę danych o nazwie Dataverse, która umożliwia przechowywanie danych dla aplikacji i rozwiązań. Dataverse zapewnia platformę danych niskiego kodu do przechowywania danych aplikacji. Jest to w pełni zarządzana usługa, która bezpiecznie przechowuje dane w chmurze Microsoft i jest udostępniana w Twoim środowisku Power Platform. Oferuje wbudowane możliwości zarządzania danymi, takie jak klasyfikacja danych, pochodzenie danych, kontrola dostępu o wysokiej precyzji i więcej. Możesz dowiedzieć się więcej [o Dataverse tutaj](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Dlaczego powinniśmy używać Dataverse dla naszego startupu? Standardowe i niestandardowe tabele w Dataverse zapewniają bezpieczną i opartą na chmurze opcję przechowywania danych. Tabele pozwalają przechowywać różne typy danych, podobnie jak możesz używać wielu arkuszy w jednym skoroszycie Excel. Możesz używać tabel do przechowywania danych specyficznych dla Twojej organizacji lub potrzeb biznesowych. Niektóre z korzyści, jakie nasz startup uzyska z używania Dataverse, to między innymi:

- **Łatwe zarządzanie**: Zarówno metadane, jak i dane są przechowywane w chmurze, więc nie musisz martwić się o szczegóły dotyczące ich przechowywania czy zarządzania. Możesz skupić się na budowaniu swoich aplikacji i rozwiązań.

- **Bezpieczeństwo**: Dataverse zapewnia bezpieczną i opartą na chmurze opcję przechowywania danych. Możesz kontrolować, kto ma dostęp do danych w Twoich tabelach i jak mogą uzyskiwać do nich dostęp, używając zabezpieczeń opartych na rolach.

- **Bogate metadane**: Typy danych i relacje są używane bezpośrednio w Power Apps

- **Logika i walidacja**: Możesz
- **Analiza Sentimentów**: Ten model wykrywa pozytywne, negatywne, neutralne lub mieszane odczucia w tekście.
- **Czytnik Wizytówek**: Ten model wyciąga informacje z wizytówek.
- **Rozpoznawanie Tekstu**: Ten model wyciąga tekst z obrazów.
- **Wykrywanie Obiektów**: Ten model wykrywa i wyciąga obiekty z obrazów.
- **Przetwarzanie Dokumentów**: Ten model wyciąga informacje z formularzy.
- **Przetwarzanie Faktur**: Ten model wyciąga informacje z faktur.

Dzięki niestandardowym modelom AI możesz wprowadzić swój własny model do AI Builder, aby działał jak każdy niestandardowy model AI Builder, pozwalając na trenowanie modelu przy użyciu własnych danych. Możesz używać tych modeli do automatyzacji procesów i przewidywania wyników zarówno w Power Apps, jak i Power Automate. Przy użyciu własnego modelu obowiązują pewne ograniczenia. Przeczytaj więcej o tych [ograniczeniach](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

## Zadanie #2 - Zbuduj przepływ przetwarzania faktur dla naszego startupu

Zespół finansowy ma trudności z przetwarzaniem faktur. Używali arkusza kalkulacyjnego do śledzenia faktur, ale zarządzanie tym stało się trudne, gdy liczba faktur wzrosła. Poprosili Cię o zbudowanie przepływu pracy, który pomoże im w przetwarzaniu faktur przy użyciu AI. Przepływ pracy powinien umożliwić wyciąganie informacji z faktur i przechowywanie ich w tabeli Dataverse. Przepływ pracy powinien również umożliwić wysyłanie e-maila do zespołu finansowego z wyciągniętymi informacjami.

Teraz, gdy wiesz, czym jest AI Builder i dlaczego powinieneś go używać, spójrzmy, jak możesz użyć modelu przetwarzania faktur AI w AI Builder, który omówiliśmy wcześniej, aby zbudować przepływ pracy, który pomoże zespołowi finansowemu w przetwarzaniu faktur.

Aby zbudować przepływ pracy, który pomoże zespołowi finansowemu w przetwarzaniu faktur przy użyciu modelu przetwarzania faktur AI w AI Builder, wykonaj poniższe kroki:

1. Przejdź do ekranu głównego [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst).
2. Użyj obszaru tekstowego na ekranie głównym, aby opisać przepływ pracy, który chcesz zbudować. Na przykład, **_Przetwarzaj fakturę, gdy pojawi się w mojej skrzynce odbiorczej_**. Kliknij przycisk **Wyślij**, aby wysłać podpowiedź do AI Copilot.
3. AI Copilot zasugeruje działania, które musisz wykonać, aby zautomatyzować zadanie. Możesz kliknąć przycisk **Dalej**, aby przejść przez kolejne kroki.
4. W następnym kroku Power Automate poprosi Cię o skonfigurowanie połączeń wymaganych dla przepływu. Po zakończeniu kliknij przycisk **Utwórz przepływ**, aby utworzyć przepływ.
5. AI Copilot wygeneruje przepływ, a Ty możesz go dostosować do swoich potrzeb.
6. Zaktualizuj wyzwalacz przepływu i ustaw **Folder** na folder, w którym będą przechowywane faktury. Na przykład, możesz ustawić folder na **Skrzynka odbiorcza**. Kliknij **Pokaż zaawansowane opcje** i ustaw **Tylko z załącznikami** na **Tak**. To zapewni, że przepływ uruchomi się tylko wtedy, gdy w folderze zostanie odebrany e-mail z załącznikiem.
7. Usuń następujące działania z przepływu: **HTML na tekst**, **Compose**, **Compose 2**, **Compose 3** i **Compose 4**, ponieważ nie będziesz ich używać.
8. Usuń działanie **Condition** z przepływu, ponieważ nie będziesz go używać. Powinno wyglądać to jak na poniższym zrzucie ekranu:
9. Kliknij przycisk **Dodaj działanie** i wyszukaj **Dataverse**. Wybierz działanie **Dodaj nowy wiersz**.
10. W działaniu **Wyciągnij informacje z faktur** zaktualizuj **Plik faktury**, aby wskazywał na **Zawartość załącznika** z e-maila. To zapewni, że przepływ wyciągnie informacje z załącznika faktury.
11. Wybierz **Tabelę**, którą utworzyłeś wcześniej. Na przykład, możesz wybrać tabelę **Informacje o fakturze**. Wybierz dynamiczną zawartość z poprzedniego działania, aby wypełnić następujące pola:
    - ID
    - Kwota
    - Data
    - Nazwa
    - Status
    - Ustaw **Status** na **Oczekujący**.
    - E-mail dostawcy
    - Użyj dynamicznej zawartości **Od** z wyzwalacza **Gdy nadejdzie nowy e-mail**.

12. Po zakończeniu przepływu kliknij przycisk **Zapisz**, aby zapisać przepływ. Możesz wtedy przetestować przepływ, wysyłając e-mail z fakturą do folderu, który określiłeś w wyzwalaczu.

> **Twoje zadanie domowe**: Przepływ, który właśnie zbudowałeś, to dobry początek, teraz musisz pomyśleć, jak możesz zbudować automatyzację, która umożliwi naszemu zespołowi finansowemu wysłanie e-maila do dostawcy, aby zaktualizować go o bieżący status jego faktury. Twoja wskazówka: przepływ musi działać, gdy status faktury się zmieni.

## Użyj modelu AI generującego tekst w Power Automate

Model AI Builder "Create Text with GPT" pozwala generować tekst na podstawie podpowiedzi i jest wspierany przez Microsoft Azure OpenAI Service. Dzięki tej funkcji możesz wprowadzić technologię GPT (Generative Pre-Trained Transformer) do swoich aplikacji i przepływów, aby zbudować różnorodne zautomatyzowane przepływy i wnikliwe aplikacje.

Modele GPT są intensywnie trenowane na ogromnych ilościach danych, co pozwala im tworzyć tekst, który blisko przypomina język ludzki, gdy otrzymają podpowiedź. Kiedy są zintegrowane z automatyzacją przepływów pracy, modele AI takie jak GPT mogą być wykorzystywane do usprawnienia i automatyzacji szerokiego zakresu zadań.

Na przykład, możesz zbudować przepływy do automatycznego generowania tekstu dla różnych zastosowań, takich jak: szkice e-maili, opisy produktów i inne. Możesz także używać modelu do generowania tekstu dla różnych aplikacji, takich jak chatboty i aplikacje obsługi klienta, które umożliwiają agentom obsługi klienta skuteczne i efektywne odpowiadanie na zapytania klientów.

Aby dowiedzieć się, jak używać tego modelu AI w Power Automate, przejdź przez moduł [Dodaj inteligencję za pomocą AI Builder i GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Świetna robota! Kontynuuj naukę

Po ukończeniu tej lekcji, sprawdź naszą [kolekcję nauki o generatywnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby kontynuować pogłębianie wiedzy o generatywnej AI!

Przejdź do Lekcji 11, gdzie przyjrzymy się, jak [zintegrować generatywną AI z wywoływaniem funkcji](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest profesjonalne tłumaczenie przez człowieka. Nie ponosimy odpowiedzialności za wszelkie nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.