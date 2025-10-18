<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "846ac8e3b7dcfb697d3309fec05f0fea",
  "translation_date": "2025-10-18T00:54:33+00:00",
  "source_file": "10-building-low-code-ai-applications/README.md",
  "language_code": "pl"
}
-->
# Tworzenie aplikacji AI w technologii low-code

[![Tworzenie aplikacji AI w technologii low-code](../../../translated_images/10-lesson-banner.a01ac8fe3fd86310c2e4065c0b3c584879f33b8ce797311821a636992f8a5b2f.pl.png)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(Kliknij na obrazek powyżej, aby obejrzeć wideo z tej lekcji)_

## Wprowadzenie

Teraz, gdy nauczyliśmy się tworzyć aplikacje generujące obrazy, porozmawiajmy o technologii low-code. Generatywna AI może być wykorzystywana w różnych obszarach, w tym w technologii low-code, ale czym właściwie jest low-code i jak można dodać do niego AI?

Tworzenie aplikacji i rozwiązań stało się łatwiejsze zarówno dla tradycyjnych programistów, jak i osób bez doświadczenia w programowaniu, dzięki platformom do tworzenia aplikacji w technologii low-code. Platformy te umożliwiają budowanie aplikacji i rozwiązań przy minimalnym lub zerowym użyciu kodu. Osiąga się to poprzez udostępnienie wizualnego środowiska programistycznego, które pozwala na przeciąganie i upuszczanie komponentów w celu tworzenia aplikacji i rozwiązań. Dzięki temu proces tworzenia aplikacji i rozwiązań jest szybszy i wymaga mniej zasobów. W tej lekcji zagłębimy się w tematykę technologii low-code oraz w to, jak można wzbogacić jej rozwój o AI, korzystając z Power Platform.

Power Platform daje organizacjom możliwość umożliwienia swoim zespołom tworzenia własnych rozwiązań w intuicyjnym środowisku low-code lub no-code. To środowisko upraszcza proces tworzenia rozwiązań. Dzięki Power Platform rozwiązania mogą być budowane w ciągu dni lub tygodni, zamiast miesięcy czy lat. Power Platform składa się z pięciu kluczowych produktów: Power Apps, Power Automate, Power BI, Power Pages i Copilot Studio.

Ta lekcja obejmuje:

- Wprowadzenie do generatywnej AI w Power Platform
- Wprowadzenie do Copilot i jego zastosowania
- Wykorzystanie generatywnej AI do tworzenia aplikacji i przepływów w Power Platform
- Zrozumienie modeli AI w Power Platform z AI Builder

## Cele nauki

Po ukończeniu tej lekcji będziesz w stanie:

- Zrozumieć, jak działa Copilot w Power Platform.

- Zbudować aplikację do śledzenia zadań uczniów dla naszego startupu edukacyjnego.

- Stworzyć przepływ przetwarzania faktur, który wykorzystuje AI do ekstrakcji informacji z faktur.

- Zastosować najlepsze praktyki podczas korzystania z modelu AI Create Text z GPT.

Narzędzia i technologie, które będziesz używać w tej lekcji, to:

- **Power Apps**, do stworzenia aplikacji do śledzenia zadań uczniów, która zapewnia środowisko programistyczne w technologii low-code do budowania aplikacji umożliwiających śledzenie, zarządzanie i interakcję z danymi.

- **Dataverse**, do przechowywania danych dla aplikacji do śledzenia zadań uczniów, gdzie Dataverse zapewni platformę danych w technologii low-code do przechowywania danych aplikacji.

- **Power Automate**, do przepływu przetwarzania faktur, gdzie będziesz mieć środowisko programistyczne w technologii low-code do budowania przepływów pracy automatyzujących proces przetwarzania faktur.

- **AI Builder**, do modelu AI przetwarzania faktur, gdzie wykorzystasz wbudowane modele AI do przetwarzania faktur dla naszego startupu.

## Generatywna AI w Power Platform

Wzbogacenie rozwoju i aplikacji w technologii low-code o generatywną AI jest kluczowym obszarem zainteresowania Power Platform. Celem jest umożliwienie każdemu tworzenia aplikacji, stron, pulpitów nawigacyjnych i automatyzacji procesów z wykorzystaniem AI, _bez konieczności posiadania wiedzy z zakresu nauki o danych_. Cel ten jest realizowany poprzez integrację generatywnej AI z doświadczeniem programistycznym w technologii low-code w Power Platform w formie Copilot i AI Builder.

### Jak to działa?

Copilot to asystent AI, który umożliwia tworzenie rozwiązań w Power Platform poprzez opisanie swoich wymagań w serii konwersacyjnych kroków za pomocą języka naturalnego. Na przykład możesz polecić swojemu asystentowi AI, jakie pola ma zawierać Twoja aplikacja, a on stworzy zarówno aplikację, jak i podstawowy model danych, lub możesz określić, jak skonfigurować przepływ w Power Automate.

Funkcjonalności oparte na Copilot można wykorzystać jako funkcję w ekranach aplikacji, aby umożliwić użytkownikom odkrywanie wniosków poprzez interakcje konwersacyjne.

AI Builder to funkcja AI w technologii low-code dostępna w Power Platform, która umożliwia korzystanie z modeli AI w celu automatyzacji procesów i przewidywania wyników. Dzięki AI Builder możesz wprowadzić AI do swoich aplikacji i przepływów, które łączą się z Twoimi danymi w Dataverse lub w różnych źródłach danych w chmurze, takich jak SharePoint, OneDrive czy Azure.

Copilot jest dostępny we wszystkich produktach Power Platform: Power Apps, Power Automate, Power BI, Power Pages i Power Virtual Agents. AI Builder jest dostępny w Power Apps i Power Automate. W tej lekcji skupimy się na tym, jak korzystać z Copilot i AI Builder w Power Apps i Power Automate, aby stworzyć rozwiązanie dla naszego startupu edukacyjnego.

### Copilot w Power Apps

W ramach Power Platform, Power Apps oferuje środowisko programistyczne w technologii low-code do tworzenia aplikacji umożliwiających śledzenie, zarządzanie i interakcję z danymi. To zestaw usług do tworzenia aplikacji z skalowalną platformą danych oraz możliwością łączenia się z usługami w chmurze i danymi lokalnymi. Power Apps pozwala na tworzenie aplikacji działających w przeglądarkach, na tabletach i telefonach, które można udostępniać współpracownikom. Power Apps ułatwia użytkownikom tworzenie aplikacji dzięki prostemu interfejsowi, tak aby każdy użytkownik biznesowy lub profesjonalny programista mógł tworzyć aplikacje dostosowane do swoich potrzeb. Doświadczenie w tworzeniu aplikacji jest również wzbogacone o generatywną AI dzięki Copilot.

Funkcja asystenta AI Copilot w Power Apps pozwala opisać, jakiego rodzaju aplikację potrzebujesz i jakie informacje chcesz, aby Twoja aplikacja śledziła, zbierała lub wyświetlała. Copilot generuje responsywną aplikację Canvas na podstawie Twojego opisu. Następnie możesz dostosować aplikację do swoich potrzeb. Copilot AI generuje również i sugeruje tabelę Dataverse z polami potrzebnymi do przechowywania danych, które chcesz śledzić, oraz przykładowymi danymi. W tej lekcji omówimy, czym jest Dataverse i jak można go używać w Power Apps. Następnie możesz dostosować tabelę do swoich potrzeb, korzystając z funkcji asystenta AI Copilot w serii konwersacyjnych kroków. Ta funkcja jest dostępna bezpośrednio z ekranu głównego Power Apps.

### Copilot w Power Automate

W ramach Power Platform, Power Automate pozwala użytkownikom tworzyć zautomatyzowane przepływy pracy między aplikacjami i usługami. Pomaga automatyzować powtarzalne procesy biznesowe, takie jak komunikacja, zbieranie danych i zatwierdzanie decyzji. Jego prosty interfejs umożliwia użytkownikom o różnym poziomie zaawansowania technicznego (od początkujących po doświadczonych programistów) automatyzację zadań. Doświadczenie w tworzeniu przepływów pracy jest również wzbogacone o generatywną AI dzięki Copilot.

Funkcja asystenta AI Copilot w Power Automate pozwala opisać, jakiego rodzaju przepływ potrzebujesz i jakie działania ma wykonywać Twój przepływ. Copilot generuje przepływ na podstawie Twojego opisu. Następnie możesz dostosować przepływ do swoich potrzeb. Copilot AI generuje i sugeruje również działania potrzebne do wykonania zadania, które chcesz zautomatyzować. W tej lekcji omówimy, czym są przepływy i jak można je wykorzystać w Power Automate. Następnie możesz dostosować działania do swoich potrzeb, korzystając z funkcji asystenta AI Copilot w serii konwersacyjnych kroków. Ta funkcja jest dostępna bezpośrednio z ekranu głównego Power Automate.

## Zadanie: Zarządzanie zadaniami uczniów i fakturami dla naszego startupu, korzystając z Copilot

Nasz startup oferuje kursy online dla uczniów. Firma szybko się rozwija i obecnie ma trudności z nadążaniem za rosnącym zapotrzebowaniem na swoje kursy. Startup zatrudnił Cię jako programistę Power Platform, abyś pomógł zbudować rozwiązanie w technologii low-code, które pomoże zarządzać zadaniami uczniów i fakturami. Rozwiązanie powinno umożliwiać śledzenie i zarządzanie zadaniami uczniów za pomocą aplikacji oraz automatyzację procesu przetwarzania faktur za pomocą przepływu pracy. Poproszono Cię o wykorzystanie generatywnej AI do opracowania tego rozwiązania.

Na początek możesz skorzystać z [Biblioteki podpowiedzi Copilot Power Platform](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko), aby zapoznać się z podpowiedziami. Biblioteka zawiera listę podpowiedzi, które możesz wykorzystać do tworzenia aplikacji i przepływów za pomocą Copilot. Możesz również użyć podpowiedzi z biblioteki, aby dowiedzieć się, jak opisać swoje wymagania dla Copilot.

### Zbuduj aplikację do śledzenia zadań uczniów dla naszego startupu

Nauczyciele w naszym startupie mają trudności z śledzeniem zadań uczniów. Korzystali z arkusza kalkulacyjnego do śledzenia zadań, ale zarządzanie tym stało się trudne wraz ze wzrostem liczby uczniów. Poprosili Cię o stworzenie aplikacji, która pomoże im śledzić i zarządzać zadaniami uczniów. Aplikacja powinna umożliwiać dodawanie nowych zadań, przeglądanie zadań, aktualizowanie zadań i usuwanie zadań. Powinna również umożliwiać nauczycielom i uczniom przeglądanie zadań, które zostały ocenione, oraz tych, które jeszcze nie zostały ocenione.

Zbudujesz aplikację, korzystając z Copilot w Power Apps, wykonując poniższe kroki:

1. Przejdź do ekranu głównego [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

1. Użyj pola tekstowego na ekranie głównym, aby opisać aplikację, którą chcesz zbudować. Na przykład: **_Chcę zbudować aplikację do śledzenia i zarządzania zadaniami uczniów_**. Kliknij przycisk **Wyślij**, aby przesłać podpowiedź do AI Copilot.

![Opisz aplikację, którą chcesz zbudować](../../../translated_images/copilot-chat-prompt-powerapps.84250f341d060830a296b68512e6b3b3aa3a4559f4f1c2d7bafeba8ad3fcd17a.pl.png)

1. AI Copilot zasugeruje tabelę Dataverse z polami potrzebnymi do przechowywania danych, które chcesz śledzić, oraz przykładowymi danymi. Następnie możesz dostosować tabelę do swoich potrzeb, korzystając z funkcji asystenta AI Copilot w serii konwersacyjnych kroków.

   > **Ważne**: Dataverse to podstawowa platforma danych dla Power Platform. Jest to platforma danych w technologii low-code do przechowywania danych aplikacji. Jest to w pełni zarządzana usługa, która bezpiecznie przechowuje dane w chmurze Microsoft i jest udostępniana w Twoim środowisku Power Platform. Posiada wbudowane funkcje zarządzania danymi, takie jak klasyfikacja danych, ich pochodzenie, precyzyjna kontrola dostępu i inne. Więcej informacji o Dataverse znajdziesz [tutaj](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Sugerowane pola w nowej tabeli](../../../translated_images/copilot-dataverse-table-powerapps.f4cc07b5d5f9327bd3783dd288debb2a959ce3320107512e235137aebd8a1a4c.pl.png)

1. Nauczyciele chcą wysyłać e-maile do uczniów, którzy przesłali swoje zadania, aby informować ich o postępach w ocenie. Możesz użyć Copilot, aby dodać nowe pole do tabeli do przechowywania adresu e-mail ucznia. Na przykład możesz użyć następującej podpowiedzi, aby dodać nowe pole do tabeli: **_Chcę dodać kolumnę do przechowywania adresu e-mail ucznia_**. Kliknij przycisk **Wyślij**, aby przesłać podpowiedź do AI Copilot.

![Dodawanie nowego pola](../../../translated_images/copilot-new-column.35e15ff21acaf2745965d427b130f2be772f0484835b44fe074d496b1a455f2a.pl.png)

1. AI Copilot wygeneruje nowe pole, które następnie możesz dostosować do swoich potrzeb.

1. Po zakończeniu pracy nad tabelą kliknij przycisk **Utwórz aplikację**, aby ją stworzyć.

1. AI Copilot wygeneruje responsywną aplikację Canvas na podstawie Twojego opisu. Następnie możesz dostosować aplikację do swoich potrzeb.

1. Aby nauczyciele mogli wysyłać e-maile do uczniów, możesz użyć Copilot, aby dodać nowy ekran do aplikacji. Na przykład możesz użyć następującej podpowiedzi, aby dodać nowy ekran do aplikacji: **_Chcę dodać ekran do wysyłania e-maili do uczniów_**. Kliknij przycisk **Wyślij**, aby przesłać podpowiedź do AI Copilot.

![Dodawanie nowego ekranu za pomocą podpowiedzi](../../../translated_images/copilot-new-screen.2e0bef7132a173928bc621780b39799e03982d315cb5a9ff75a34b08054641d4.pl.png)

1. AI Copilot wygeneruje nowy ekran, który następnie możesz dostosować do swoich potrzeb.

1. Po zakończeniu pracy nad aplikacją kliknij przycisk **Zapisz**, aby ją zapisać.

1. Aby udostępnić aplikację nauczycielom, kliknij przycisk **Udostępnij**, a następnie ponownie kliknij **Udostępnij**. Możesz udostępnić aplikację nauczycielom, wpisując ich adresy e-mail.

> **Twoje zadanie domowe**: Aplikacja, którą właśnie stworzyłeś, to dobry początek, ale można ją ulepszyć. Dzięki funkcji wysyłania e-maili nauczyciele mogą wysyłać wiadomości do uczniów tylko ręcznie, wpisując ich adresy e-mail. Czy możesz użyć Copilot, aby stworzyć automatyzację, która umożliwi nauczycielom automatyczne wysyłanie e-maili do uczniów, gdy ci przesyłają swoje zadania? Podpowiedź: z odpowiednią podpowiedzią możesz użyć Copilot w Power Automate, aby to zrobić.

### Zbuduj tabelę informacji o fakturach dla naszego startupu

Zespół finansowy naszego startupu ma trudności z śledzeniem faktur. Korzystali z arkusza kalkulacyjnego do śledzenia faktur, ale zarządzanie tym stało się trudne wraz ze wzrostem liczby faktur. Poprosili Cię o stworzenie tabeli, która pomoże im przechowywać, śledzić i zarządzać informacjami o otrzymanych fakturach. Tabela powinna być używana do stworzenia automatyzacji, która wyodrębni wszystkie informacje z faktur i zapisze je w tabeli. Tabela powinna również umożliwiać zespołowi finansowemu przeglądanie faktur, które zostały opłacone, oraz tych, które jeszcze nie zostały opłacone.

Power Platform posiada podstawową platformę danych o nazwie Dataverse, która umożliwia przechowywanie danych dla Twoich aplikacji i rozwiązań. Dataverse zapewnia platformę danych w technologii low-code do przechowywania danych aplikacji. Jest to w pełni zarządzana usługa, która bezpiecznie przechowuje dane w chmurze Microsoft i jest udostępniana w Twoim środowisku Power Platform. Posiada wbudowane funkcje zarządzania danymi, takie jak klasyfikacja danych, ich pochodzenie, precyzyjna kontrola dostępu i inne. Więcej informacji [o Dataverse znajdziesz tutaj](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).
Dlaczego warto używać Dataverse w naszej firmie startupowej? Standardowe i niestandardowe tabele w Dataverse zapewniają bezpieczne i oparte na chmurze miejsce do przechowywania danych. Tabele pozwalają na przechowywanie różnych typów danych, podobnie jak w przypadku używania wielu arkuszy w jednym skoroszycie Excel. Możesz używać tabel do przechowywania danych specyficznych dla Twojej organizacji lub potrzeb biznesowych. Korzyści, jakie nasz startup może uzyskać dzięki używaniu Dataverse, obejmują, ale nie ograniczają się do:

- **Łatwość zarządzania**: Zarówno metadane, jak i dane są przechowywane w chmurze, więc nie musisz martwić się szczegółami dotyczącymi ich przechowywania czy zarządzania. Możesz skupić się na budowaniu aplikacji i rozwiązań.

- **Bezpieczeństwo**: Dataverse oferuje bezpieczne i oparte na chmurze miejsce do przechowywania danych. Możesz kontrolować, kto ma dostęp do danych w tabelach i w jaki sposób mogą je przeglądać, korzystając z zabezpieczeń opartych na rolach.

- **Bogate metadane**: Typy danych i relacje są używane bezpośrednio w Power Apps.

- **Logika i walidacja**: Możesz używać reguł biznesowych, pól obliczeniowych i reguł walidacji, aby wymuszać logikę biznesową i utrzymywać dokładność danych.

Teraz, gdy wiesz, czym jest Dataverse i dlaczego warto go używać, przyjrzyjmy się, jak możesz użyć Copilot do stworzenia tabeli w Dataverse, aby spełnić wymagania naszego zespołu finansowego.

> **Note**: Tabela ta będzie używana w następnej sekcji do stworzenia automatyzacji, która wyciągnie wszystkie informacje o fakturach i zapisze je w tabeli.

Aby utworzyć tabelę w Dataverse za pomocą Copilot, wykonaj poniższe kroki:

1. Przejdź do ekranu głównego [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

2. Na lewym pasku nawigacyjnym wybierz **Tables**, a następnie kliknij **Describe the new Table**.

![Wybierz nową tabelę](../../../translated_images/describe-new-table.0792373eb757281e3c5f542f84cad3b5208bfe0e5c4a7786dd2bd31aa848a23c.pl.png)

3. Na ekranie **Describe the new Table** użyj pola tekstowego, aby opisać tabelę, którą chcesz utworzyć. Na przykład: **_Chcę utworzyć tabelę do przechowywania informacji o fakturach_**. Kliknij przycisk **Send**, aby wysłać polecenie do AI Copilot.

![Opisz tabelę](../../../translated_images/copilot-chat-prompt-dataverse.feb2f81e5872b9d2b05d45d11bb6830e0f2ef6a2d4742413bc9a1e50a45bbb89.pl.png)

4. AI Copilot zaproponuje tabelę Dataverse z polami potrzebnymi do przechowywania danych, które chcesz śledzić, oraz przykładowymi danymi. Następnie możesz dostosować tabelę do swoich potrzeb, korzystając z funkcji asystenta AI Copilot w ramach rozmowy.

![Proponowana tabela Dataverse](../../../translated_images/copilot-dataverse-table.b3bc936091324d9db1e943d640df1c7a7df598e66d30f5b8a2999048e26a5073.pl.png)

5. Zespół finansowy chce wysłać e-mail do dostawcy, aby poinformować go o aktualnym statusie jego faktury. Możesz użyć Copilot, aby dodać nowe pole do tabeli, w którym będzie przechowywany adres e-mail dostawcy. Na przykład możesz użyć następującego polecenia, aby dodać nowe pole do tabeli: **_Chcę dodać kolumnę do przechowywania adresu e-mail dostawcy_**. Kliknij przycisk **Send**, aby wysłać polecenie do AI Copilot.

6. AI Copilot wygeneruje nowe pole, które następnie możesz dostosować do swoich potrzeb.

7. Po zakończeniu pracy nad tabelą kliknij przycisk **Create**, aby utworzyć tabelę.

## Modele AI w Power Platform z AI Builder

AI Builder to funkcja AI typu low-code dostępna w Power Platform, która umożliwia korzystanie z modeli AI do automatyzacji procesów i przewidywania wyników. Dzięki AI Builder możesz wprowadzić sztuczną inteligencję do swoich aplikacji i przepływów, które łączą się z danymi w Dataverse lub w różnych źródłach danych w chmurze, takich jak SharePoint, OneDrive czy Azure.

## Wbudowane modele AI vs niestandardowe modele AI

AI Builder oferuje dwa rodzaje modeli AI: wbudowane modele AI oraz niestandardowe modele AI. Wbudowane modele AI to gotowe do użycia modele, które zostały wytrenowane przez Microsoft i są dostępne w Power Platform. Pomagają one dodawać inteligencję do aplikacji i przepływów bez konieczności zbierania danych, a następnie budowania, trenowania i publikowania własnych modeli. Możesz używać tych modeli do automatyzacji procesów i przewidywania wyników.

Niektóre z dostępnych w Power Platform wbudowanych modeli AI to:

- **Wyodrębnianie kluczowych fraz**: Model wyodrębnia kluczowe frazy z tekstu.
- **Wykrywanie języka**: Model rozpoznaje język tekstu.
- **Analiza sentymentu**: Model wykrywa pozytywny, negatywny, neutralny lub mieszany sentyment w tekście.
- **Czytnik wizytówek**: Model wyodrębnia informacje z wizytówek.
- **Rozpoznawanie tekstu**: Model wyodrębnia tekst z obrazów.
- **Wykrywanie obiektów**: Model wykrywa i wyodrębnia obiekty z obrazów.
- **Przetwarzanie dokumentów**: Model wyodrębnia informacje z formularzy.
- **Przetwarzanie faktur**: Model wyodrębnia informacje z faktur.

Dzięki niestandardowym modelom AI możesz wprowadzić własny model do AI Builder, aby działał jak każdy niestandardowy model AI Builder, umożliwiając trenowanie modelu za pomocą własnych danych. Możesz używać tych modeli do automatyzacji procesów i przewidywania wyników zarówno w Power Apps, jak i Power Automate. Przy korzystaniu z własnego modelu obowiązują pewne ograniczenia. Przeczytaj więcej o tych [ograniczeniach](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

![Modele AI Builder](../../../translated_images/ai-builder-models.8069423b84cfc47f6bb989bc3cd0584b5b2471c80fad80bf504d356928a08c9c.pl.png)

## Zadanie #2 - Zbuduj przepływ przetwarzania faktur dla naszego startupu

Zespół finansowy ma trudności z przetwarzaniem faktur. Korzystają z arkusza kalkulacyjnego do śledzenia faktur, ale zarządzanie tym staje się coraz trudniejsze wraz ze wzrostem liczby faktur. Poprosili Cię o stworzenie przepływu pracy, który pomoże im przetwarzać faktury za pomocą AI. Przepływ pracy powinien umożliwiać wyodrębnianie informacji z faktur i przechowywanie ich w tabeli Dataverse. Powinien również umożliwiać wysyłanie e-maila do zespołu finansowego z wyodrębnionymi informacjami.

Teraz, gdy wiesz, czym jest AI Builder i dlaczego warto go używać, przyjrzyjmy się, jak możesz użyć modelu AI do przetwarzania faktur w AI Builder, o którym mówiliśmy wcześniej, aby zbudować przepływ pracy, który pomoże zespołowi finansowemu przetwarzać faktury.

Aby zbudować przepływ pracy, który pomoże zespołowi finansowemu przetwarzać faktury za pomocą modelu AI do przetwarzania faktur w AI Builder, wykonaj poniższe kroki:

1. Przejdź do ekranu głównego [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst).

2. Użyj pola tekstowego na ekranie głównym, aby opisać przepływ pracy, który chcesz zbudować. Na przykład: **_Przetwórz fakturę, gdy dotrze do mojej skrzynki odbiorczej_**. Kliknij przycisk **Send**, aby wysłać polecenie do AI Copilot.

   ![Copilot Power Automate](../../../translated_images/copilot-chat-prompt-powerautomate.f377e478cc8412de4394fab09e5b72f97b3fc9312526b516ded426102f51c30d.pl.png)

3. AI Copilot zaproponuje działania potrzebne do wykonania zadania, które chcesz zautomatyzować. Możesz kliknąć przycisk **Next**, aby przejść do kolejnych kroków.

4. W następnym kroku Power Automate poprosi Cię o skonfigurowanie połączeń wymaganych dla przepływu. Po zakończeniu kliknij przycisk **Create flow**, aby utworzyć przepływ.

5. AI Copilot wygeneruje przepływ, który następnie możesz dostosować do swoich potrzeb.

6. Zaktualizuj wyzwalacz przepływu i ustaw **Folder** na folder, w którym będą przechowywane faktury. Na przykład możesz ustawić folder na **Inbox**. Kliknij **Show advanced options** i ustaw **Only with Attachments** na **Yes**. To zapewni, że przepływ uruchomi się tylko wtedy, gdy w folderze zostanie odebrany e-mail z załącznikiem.

7. Usuń następujące działania z przepływu: **HTML to text**, **Compose**, **Compose 2**, **Compose 3** i **Compose 4**, ponieważ nie będziesz ich używać.

8. Usuń działanie **Condition** z przepływu, ponieważ nie będziesz go używać. Powinno to wyglądać jak na poniższym zrzucie ekranu:

   ![Power Automate, usuń działania](../../../translated_images/powerautomate-remove-actions.7216392fe684ceba4b73c6383edd1cc5e7ded11afd0ca812052a11487d049ef8.pl.png)

9. Kliknij przycisk **Add an action** i wyszukaj **Dataverse**. Wybierz działanie **Add a new row**.

10. W działaniu **Extract Information from invoices** zaktualizuj **Invoice File**, aby wskazywał na **Attachment Content** z e-maila. To zapewni, że przepływ wyodrębni informacje z załącznika faktury.

11. Wybierz **Table**, którą utworzyłeś wcześniej. Na przykład możesz wybrać tabelę **Invoice Information**. Wybierz dynamiczną zawartość z poprzedniego działania, aby wypełnić następujące pola:

    - ID
    - Kwota
    - Data
    - Nazwa
    - Status - Ustaw **Status** na **Pending**.
    - E-mail dostawcy - Użyj dynamicznej zawartości **From** z wyzwalacza **When a new email arrives**.

    ![Power Automate dodaj wiersz](../../../translated_images/powerautomate-add-row.5edce45e5dd3d51e5152688dc140ad43e1423e7a9fef9a206f82a7965ea68d73.pl.png)

12. Po zakończeniu pracy nad przepływem kliknij przycisk **Save**, aby zapisać przepływ. Następnie możesz przetestować przepływ, wysyłając e-mail z fakturą do folderu, który określiłeś w wyzwalaczu.

> **Twoje zadanie domowe**: Przepływ, który właśnie stworzyłeś, to dobry początek, teraz musisz pomyśleć, jak zbudować automatyzację, która umożliwi naszemu zespołowi finansowemu wysyłanie e-maila do dostawcy w celu poinformowania go o aktualnym statusie jego faktury. Podpowiedź: przepływ musi uruchamiać się, gdy status faktury się zmienia.

## Użycie modelu AI do generowania tekstu w Power Automate

Model Create Text with GPT w AI Builder umożliwia generowanie tekstu na podstawie polecenia i jest zasilany przez Microsoft Azure OpenAI Service. Dzięki tej funkcji możesz włączyć technologię GPT (Generative Pre-Trained Transformer) do swoich aplikacji i przepływów, aby tworzyć różnorodne zautomatyzowane przepływy i aplikacje pełne wnikliwych informacji.

Modele GPT przechodzą intensywne szkolenie na ogromnych ilościach danych, co pozwala im generować tekst, który bardzo przypomina język ludzki, gdy otrzymają odpowiednie polecenie. Po zintegrowaniu z automatyzacją przepływów, modele AI, takie jak GPT, mogą być wykorzystywane do usprawnienia i automatyzacji szerokiego zakresu zadań.

Na przykład możesz tworzyć przepływy, które automatycznie generują tekst dla różnych zastosowań, takich jak: szkice e-maili, opisy produktów i inne. Możesz również używać modelu do generowania tekstu dla różnych aplikacji, takich jak chatboty i aplikacje obsługi klienta, które umożliwiają agentom obsługi klienta skuteczne i efektywne odpowiadanie na zapytania klientów.

![Utwórz polecenie](../../../translated_images/create-prompt-gpt.69d429300c2e870a12ec95556cda9bacf6a173e452cdca02973c90df5f705cee.pl.png)

Aby dowiedzieć się, jak korzystać z tego modelu AI w Power Automate, przejdź przez moduł [Add intelligence with AI Builder and GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Świetna robota! Kontynuuj naukę

Po ukończeniu tej lekcji zapoznaj się z naszą [kolekcją nauki o generatywnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej rozwijać swoją wiedzę na temat generatywnej AI!

Przejdź do Lekcji 11, gdzie przyjrzymy się, jak [zintegrować generatywną AI z wywoływaniem funkcji](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.