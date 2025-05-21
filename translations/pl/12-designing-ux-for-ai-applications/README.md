<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec385b41ee50579025d50cc03bfb3a25",
  "translation_date": "2025-05-19T21:54:28+00:00",
  "source_file": "12-designing-ux-for-ai-applications/README.md",
  "language_code": "pl"
}
-->
# Projektowanie UX dla aplikacji AI

> _(Kliknij obrazek powyżej, aby obejrzeć wideo z tej lekcji)_

Doświadczenie użytkownika jest bardzo ważnym aspektem budowania aplikacji. Użytkownicy muszą być w stanie korzystać z Twojej aplikacji w efektywny sposób, aby wykonywać zadania. Bycie efektywnym to jedno, ale musisz także projektować aplikacje tak, aby były dostępne dla wszystkich, aby uczynić je _dostępnymi_. Ten rozdział skupi się na tym obszarze, abyś ostatecznie zaprojektował aplikację, którą ludzie mogą i chcą używać.

## Wprowadzenie

Doświadczenie użytkownika to sposób, w jaki użytkownik wchodzi w interakcję z konkretnym produktem lub usługą, czy to systemem, narzędziem czy projektem. Podczas tworzenia aplikacji AI, deweloperzy koncentrują się nie tylko na zapewnieniu efektywnego doświadczenia użytkownika, ale także na aspektach etycznych. W tej lekcji omówimy, jak budować aplikacje sztucznej inteligencji (AI), które odpowiadają na potrzeby użytkowników.

Lekcja obejmie następujące obszary:

- Wprowadzenie do doświadczenia użytkownika i zrozumienie potrzeb użytkowników
- Projektowanie aplikacji AI dla zaufania i przejrzystości
- Projektowanie aplikacji AI dla współpracy i informacji zwrotnej

## Cele nauki

Po ukończeniu tej lekcji będziesz w stanie:

- Zrozumieć, jak budować aplikacje AI, które spełniają potrzeby użytkowników.
- Projektować aplikacje AI, które promują zaufanie i współpracę.

### Wymagania wstępne

Poświęć trochę czasu i przeczytaj więcej o [doświadczeniu użytkownika i myśleniu projektowym.](https://learn.microsoft.com/training/modules/ux-design?WT.mc_id=academic-105485-koreyst)

## Wprowadzenie do doświadczenia użytkownika i zrozumienie potrzeb użytkowników

W naszym fikcyjnym startupie edukacyjnym mamy dwóch głównych użytkowników, nauczycieli i uczniów. Każdy z tych użytkowników ma unikalne potrzeby. Projektowanie zorientowane na użytkownika priorytetowo traktuje użytkownika, zapewniając, że produkty są istotne i korzystne dla tych, dla których są przeznaczone.

Aplikacja powinna być **użyteczna, niezawodna, dostępna i przyjemna**, aby zapewnić dobre doświadczenie użytkownika.

### Użyteczność

Bycie użytecznym oznacza, że aplikacja ma funkcjonalność odpowiadającą jej zamierzonemu celowi, taką jak automatyzacja procesu oceniania czy generowanie fiszek do powtórek. Aplikacja, która automatyzuje proces oceniania, powinna być w stanie dokładnie i efektywnie przypisywać oceny pracy uczniów na podstawie wcześniej określonych kryteriów. Podobnie, aplikacja generująca fiszki do powtórek powinna być w stanie tworzyć odpowiednie i różnorodne pytania na podstawie swoich danych.

### Niezawodność

Bycie niezawodnym oznacza, że aplikacja może wykonywać swoje zadanie konsekwentnie i bez błędów. Jednak AI, podobnie jak ludzie, nie jest doskonała i może być podatna na błędy. Aplikacje mogą napotkać błędy lub nieoczekiwane sytuacje, które wymagają interwencji lub korekty ze strony człowieka. Jak radzisz sobie z błędami? W ostatniej sekcji tej lekcji omówimy, jak systemy i aplikacje AI są projektowane dla współpracy i informacji zwrotnej.

### Dostępność

Bycie dostępnym oznacza rozszerzenie doświadczenia użytkownika na użytkowników o różnych zdolnościach, w tym osoby z niepełnosprawnościami, aby zapewnić, że nikt nie zostanie pominięty. Przestrzegając wytycznych i zasad dostępności, rozwiązania AI stają się bardziej inkluzywne, użyteczne i korzystne dla wszystkich użytkowników.

### Przyjemność

Bycie przyjemnym oznacza, że aplikacja jest przyjemna w użyciu. Atrakcyjne doświadczenie użytkownika może mieć pozytywny wpływ na użytkownika, zachęcając go do powrotu do aplikacji i zwiększając przychody firmy.

Nie każde wyzwanie można rozwiązać za pomocą AI. AI wchodzi w grę, aby wzmocnić doświadczenie użytkownika, czy to poprzez automatyzację ręcznych zadań, czy personalizację doświadczeń użytkownika.

## Projektowanie aplikacji AI dla zaufania i przejrzystości

Budowanie zaufania jest kluczowe podczas projektowania aplikacji AI. Zaufanie zapewnia, że użytkownik ma pewność, że aplikacja wykona zadanie, dostarczy wyniki konsekwentnie i że wyniki są tym, czego użytkownik potrzebuje. Ryzyko w tym obszarze to brak zaufania i nadmierne zaufanie. Brak zaufania występuje, gdy użytkownik ma małe lub brak zaufania do systemu AI, co prowadzi do odrzucenia aplikacji przez użytkownika. Nadmierne zaufanie występuje, gdy użytkownik przecenia możliwości systemu AI, co prowadzi do zbyt dużego zaufania do systemu AI. Na przykład, zautomatyzowany system oceniania w przypadku nadmiernego zaufania może prowadzić do tego, że nauczyciel nie sprawdzi niektórych prac, aby upewnić się, że system oceniania działa dobrze. Może to skutkować niesprawiedliwymi lub niedokładnymi ocenami dla uczniów, lub utraconymi okazjami do informacji zwrotnej i poprawy.

Dwa sposoby, aby zapewnić, że zaufanie jest umieszczone w centrum projektu, to wyjaśnialność i kontrola.

### Wyjaśnialność

Kiedy AI pomaga w podejmowaniu decyzji, takich jak przekazywanie wiedzy przyszłym pokoleniom, ważne jest, aby nauczyciele i rodzice rozumieli, jak podejmowane są decyzje AI. To jest wyjaśnialność - zrozumienie, jak aplikacje AI podejmują decyzje. Projektowanie dla wyjaśnialności obejmuje dodawanie szczegółów przykładów tego, co aplikacja AI może zrobić. Na przykład, zamiast "Rozpocznij z nauczycielem AI", system może użyć: "Podsumuj swoje notatki dla łatwiejszej powtórki za pomocą AI."

Innym przykładem jest sposób, w jaki AI wykorzystuje dane użytkowników i dane osobowe. Na przykład, użytkownik z personą ucznia może mieć ograniczenia w oparciu o swoją personę. AI może nie być w stanie ujawnić odpowiedzi na pytania, ale może pomóc użytkownikowi przemyśleć, jak mogą rozwiązać problem.

Ostatnią kluczową częścią wyjaśnialności jest uproszczenie wyjaśnień. Uczniowie i nauczyciele mogą nie być ekspertami w dziedzinie AI, dlatego wyjaśnienia dotyczące tego, co aplikacja może lub nie może zrobić, powinny być uproszczone i łatwe do zrozumienia.

### Kontrola

Generatywna AI tworzy współpracę między AI a użytkownikiem, gdzie na przykład użytkownik może modyfikować polecenia dla różnych wyników. Dodatkowo, gdy wynik jest generowany, użytkownicy powinni mieć możliwość modyfikacji wyników, dając im poczucie kontroli. Na przykład, korzystając z Bing, możesz dostosować swoje polecenie na podstawie formatu, tonu i długości. Dodatkowo, możesz wprowadzać zmiany do swojego wyniku i modyfikować wynik.

Inną funkcją w Bing, która pozwala użytkownikowi mieć kontrolę nad aplikacją, jest możliwość włączenia i wyłączenia danych, które AI wykorzystuje. W przypadku aplikacji szkolnej, uczeń może chcieć użyć swoich notatek oraz zasobów nauczyciela jako materiałów do powtórek.

> Podczas projektowania aplikacji AI, intencjonalność jest kluczowa w zapewnieniu, że użytkownicy nie będą nadmiernie ufać, tworząc nierealistyczne oczekiwania dotyczące jej możliwości. Jednym ze sposobów na to jest tworzenie tarcia między poleceniami a wynikami. Przypominając użytkownikowi, że to jest AI, a nie człowiek.

## Projektowanie aplikacji AI dla współpracy i informacji zwrotnej

Jak wspomniano wcześniej, generatywna AI tworzy współpracę między użytkownikiem a AI. Większość interakcji polega na wprowadzeniu przez użytkownika polecenia i generowaniu przez AI wyniku. Co jeśli wynik jest nieprawidłowy? Jak aplikacja radzi sobie z błędami, jeśli wystąpią? Czy AI obwinia użytkownika, czy poświęca czas na wyjaśnienie błędu?

Aplikacje AI powinny być zbudowane tak, aby przyjmować i dawać informacje zwrotne. To nie tylko pomaga systemowi AI się poprawić, ale także buduje zaufanie użytkowników. W projektowaniu powinien być uwzględniony cykl informacji zwrotnej, przykładem może być proste kciuki w górę lub w dół na wyniku.

Innym sposobem radzenia sobie z tym jest wyraźne komunikowanie możliwości i ograniczeń systemu. Kiedy użytkownik popełnia błąd, prosząc o coś poza możliwościami AI, powinien być również sposób na radzenie sobie z tym.

Błędy systemowe są powszechne w aplikacjach, gdzie użytkownik może potrzebować pomocy w informacji poza zakresem AI lub aplikacja może mieć limit dotyczący liczby pytań/przedmiotów, które użytkownik może generować podsumowania. Na przykład, aplikacja AI wytrenowana na danych dotyczących ograniczonych przedmiotów, na przykład historii i matematyki, może nie być w stanie obsłużyć pytań dotyczących geografii. Aby temu przeciwdziałać, system AI może dać odpowiedź, taką jak: "Przepraszam, nasz produkt został wytrenowany na danych w następujących przedmiotach..., nie jestem w stanie odpowiedzieć na pytanie, które zadałeś."

Aplikacje AI nie są doskonałe, dlatego są podatne na błędy. Podczas projektowania aplikacji powinieneś upewnić się, że tworzysz miejsce na informacje zwrotne od użytkowników i obsługę błędów w sposób prosty i łatwy do wyjaśnienia.

## Zadanie

Weź dowolne aplikacje AI, które zbudowałeś do tej pory, i rozważ wdrożenie poniższych kroków w swojej aplikacji:

- **Przyjemność:** Zastanów się, jak możesz uczynić swoją aplikację bardziej przyjemną. Czy dodajesz wyjaśnienia wszędzie? Czy zachęcasz użytkownika do eksploracji? Jak formułujesz swoje komunikaty o błędach?

- **Użyteczność:** Budowanie aplikacji internetowej. Upewnij się, że Twoja aplikacja jest nawigowalna zarówno za pomocą myszy, jak i klawiatury.

- **Zaufanie i przejrzystość:** Nie ufaj całkowicie AI i jej wynikom, zastanów się, jak dodać człowieka do procesu weryfikacji wyników. Rozważ i wdroż inne sposoby osiągnięcia zaufania i przejrzystości.

- **Kontrola:** Daj użytkownikowi kontrolę nad danymi, które dostarcza aplikacji. Wdróż sposób, w jaki użytkownik może włączyć lub wyłączyć zbieranie danych w aplikacji AI.

## Kontynuuj naukę!

Po ukończeniu tej lekcji, sprawdź naszą [Kolekcję nauki o generatywnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby kontynuować rozwijanie swojej wiedzy o generatywnej AI!

Przejdź do Lekcji 13, gdzie przyjrzymy się, jak [zabezpieczyć aplikacje AI](../13-securing-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Zrzeczenie się odpowiedzialności**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uważany za wiarygodne źródło. W przypadku istotnych informacji zalecane jest skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.