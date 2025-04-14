# Projektowanie UX dla aplikacji AI

[![Projektowanie UX dla aplikacji AI](../../images/12-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson12-gh?WT.mc_id=academic-105485-koreyst)

> _(Kliknij powyższy obrazek, aby obejrzeć wideo tej lekcji)_

Doświadczenie użytkownika jest bardzo ważnym aspektem budowania aplikacji. Użytkownicy muszą być w stanie korzystać z Twojej aplikacji w sposób efektywny, aby wykonywać zadania. Bycie efektywnym to jedno, ale musisz również projektować aplikacje tak, aby mogły być używane przez wszystkich, aby uczynić je _dostępnymi_. Ten rozdział skupi się na tym obszarze, abyś ostatecznie zaprojektował aplikację, której ludzie mogą i chcą używać.

## Wprowadzenie

Doświadczenie użytkownika to sposób, w jaki użytkownik wchodzi w interakcję i korzysta z określonego produktu lub usługi, czy to systemu, narzędzia czy projektu. Podczas tworzenia aplikacji AI, programiści koncentrują się nie tylko na zapewnieniu efektywności doświadczenia użytkownika, ale także na etyce. W tej lekcji omówimy, jak budować aplikacje Sztucznej Inteligencji (AI), które odpowiadają na potrzeby użytkowników.

Lekcja obejmie następujące obszary:

- Wprowadzenie do Doświadczenia Użytkownika i Zrozumienia Potrzeb Użytkownika
- Projektowanie Aplikacji AI dla Zaufania i Przejrzystości
- Projektowanie Aplikacji AI dla Współpracy i Informacji Zwrotnej

## Cele nauczania

Po ukończeniu tej lekcji będziesz potrafił:

- Zrozumieć, jak budować aplikacje AI, które spełniają potrzeby użytkownika.
- Projektować aplikacje AI, które promują zaufanie i współpracę.

### Wymagania wstępne

Poświęć trochę czasu i przeczytaj więcej o [doświadczeniu użytkownika i myśleniu projektowym.](https://learn.microsoft.com/training/modules/ux-design?WT.mc_id=academic-105485-koreyst)

## Wprowadzenie do Doświadczenia Użytkownika i Zrozumienia Potrzeb Użytkownika

W naszym fikcyjnym startupie edukacyjnym mamy dwóch głównych użytkowników: nauczycieli i uczniów. Każdy z tych dwóch użytkowników ma unikalne potrzeby. Projektowanie zorientowane na użytkownika stawia użytkownika na pierwszym miejscu, zapewniając, że produkty są istotne i korzystne dla tych, dla których są przeznaczone.

Aplikacja powinna być **użyteczna, niezawodna, dostępna i przyjemna** aby zapewnić dobre doświadczenie użytkownika.

### Użyteczność

Bycie użytecznym oznacza, że aplikacja ma funkcjonalność, która odpowiada jej zamierzonemu celowi, takiemu jak automatyzacja procesu oceniania lub generowanie fiszek do powtórek. Aplikacja, która automatyzuje proces oceniania, powinna być w stanie dokładnie i efektywnie przypisywać oceny pracom uczniów na podstawie wcześniej zdefiniowanych kryteriów. Podobnie, aplikacja generująca fiszki do powtórek powinna tworzyć istotne i różnorodne pytania na podstawie swoich danych.

### Niezawodność

Bycie niezawodnym oznacza, że aplikacja może wykonywać swoje zadanie konsekwentnie i bez błędów. Jednak AI, podobnie jak ludzie, nie jest doskonała i może być podatna na błędy. Aplikacje mogą napotkać błędy lub nieoczekiwane sytuacje, które wymagają interwencji lub korekty człowieka. Jak radzić sobie z błędami? W ostatniej sekcji tej lekcji omówimy, jak systemy i aplikacje AI są projektowane dla współpracy i informacji zwrotnej.

### Dostępność

Bycie dostępnym oznacza rozszerzenie doświadczenia użytkownika na użytkowników o różnych możliwościach, w tym na osoby z niepełnosprawnościami, zapewniając, że nikt nie zostaje pominięty. Stosując wytyczne i zasady dostępności, rozwiązania AI stają się bardziej inkluzywne, użyteczne i korzystne dla wszystkich użytkowników.

### Przyjemność

Bycie przyjemnym oznacza, że korzystanie z aplikacji jest przyjemne. Atrakcyjne doświadczenie użytkownika może mieć pozytywny wpływ na użytkownika, zachęcając go do powrotu do aplikacji i zwiększając przychody biznesowe.

![obraz ilustrujący względy UX w AI](../../images/uxinai.png?WT.mc_id=academic-105485-koreyst)

Nie każde wyzwanie można rozwiązać za pomocą AI. AI wkracza, aby wzbogacić doświadczenie użytkownika, czy to poprzez automatyzację ręcznych zadań, czy personalizację doświadczeń użytkownika.

## Projektowanie Aplikacji AI dla Zaufania i Przejrzystości

Budowanie zaufania jest kluczowe przy projektowaniu aplikacji AI. Zaufanie zapewnia użytkownikowi pewność, że aplikacja wykona zadanie, dostarczy wyniki konsekwentnie, a wyniki są tym, czego użytkownik potrzebuje. Ryzykiem w tym obszarze jest brak zaufania i nadmierne zaufanie. Brak zaufania występuje, gdy użytkownik ma niewielkie zaufanie lub w ogóle nie ma zaufania do systemu AI, co prowadzi do odrzucenia aplikacji przez użytkownika. Nadmierne zaufanie występuje, gdy użytkownik przecenia możliwości systemu AI, co prowadzi do zbyt dużego zaufania użytkowników do systemu AI. Na przykład, zautomatyzowany system oceniania w przypadku nadmiernego zaufania może prowadzić do tego, że nauczyciel nie sprawdzi niektórych prac, aby upewnić się, że system oceniania działa dobrze. Może to skutkować niesprawiedliwymi lub niedokładnymi ocenami dla uczniów lub utratą możliwości uzyskania informacji zwrotnej i poprawy.

Dwa sposoby, aby zapewnić, że zaufanie jest w centrum projektu, to wyjaśnialność i kontrola.

### Wyjaśnialność

Kiedy AI pomaga podejmować decyzje, takie jak przekazywanie wiedzy przyszłym pokoleniom, kluczowe jest, aby nauczyciele i rodzice rozumieli, jak podejmowane są decyzje AI. To jest wyjaśnialność - zrozumienie, jak aplikacje AI podejmują decyzje. Projektowanie z myślą o wyjaśnialności obejmuje dodawanie szczegółów przykładów tego, co aplikacja AI może zrobić. Na przykład, zamiast "Rozpocznij z nauczycielem AI", system może użyć: "Podsumuj swoje notatki dla łatwiejszej rewizji za pomocą AI."

![strona startowa aplikacji z jasną ilustracją wyjaśnialności w aplikacjach AI](../../images/explanability-in-ai.png?WT.mc_id=academic-105485-koreyst)

Innym przykładem jest to, jak AI wykorzystuje dane użytkownika i dane osobowe. Na przykład, użytkownik z personą ucznia może mieć ograniczenia w oparciu o swoją personę. AI może nie być w stanie ujawnić odpowiedzi na pytania, ale może pomóc naprowadzić użytkownika do przemyślenia, jak mogą rozwiązać problem.

![AI odpowiadająca na pytania w oparciu o personę](../../images/solving-questions.png?WT.mc_id=academic-105485-koreyst)

Ostatnim kluczowym elementem wyjaśnialności jest uproszczenie wyjaśnień. Uczniowie i nauczyciele mogą nie być ekspertami w AI, dlatego wyjaśnienia, czego aplikacja może lub nie może zrobić, powinny być uproszczone i łatwe do zrozumienia.

![uproszczone wyjaśnienia dotyczące możliwości AI](../../images/simplified-explanations.png?WT.mc_id=academic-105485-koreyst)

### Kontrola

Generatywna AI tworzy współpracę między AI a użytkownikiem, gdzie na przykład użytkownik może modyfikować prompte dla różnych wyników. Dodatkowo, po wygenerowaniu wyniku, użytkownicy powinni być w stanie modyfikować wyniki, dając im poczucie kontroli. Na przykład, korzystając z Bing, możesz dostosować swój prompt w oparciu o format, ton i długość. Dodatkowo możesz wprowadzać zmiany do swojego wyniku i modyfikować wynik, jak pokazano poniżej:

![Wyniki wyszukiwania Bing z opcjami modyfikacji promptu i wyniku](../../images/bing1.png?WT.mc_id=academic-105485-koreyst "Wyniki wyszukiwania Bing z opcjami modyfikacji promptu i wyniku")

Inną funkcją w Bing, która pozwala użytkownikowi na kontrolę nad aplikacją, jest możliwość wyrażenia zgody i rezygnacji z danych używanych przez AI. W przypadku aplikacji szkolnej, uczeń może chcieć używać swoich notatek, a także zasobów nauczycieli jako materiału do powtórek.

![Wyniki wyszukiwania Bing z opcjami modyfikacji promptu i wyniku](../../images/bing2.png?WT.mc_id=academic-105485-koreyst "Wyniki wyszukiwania Bing z opcjami modyfikacji promptu i wyniku")

> Przy projektowaniu aplikacji AI, celowość jest kluczowa w zapewnieniu, że użytkownicy nie nadmiernie ufają, ustanawiając nierealistyczne oczekiwania dotyczące jej możliwości. Jednym ze sposobów na to jest tworzenie tarcia między promptami a wynikami. Przypominając użytkownikowi, że to jest AI, a nie drugi człowiek.

## Projektowanie Aplikacji AI dla Współpracy i Informacji Zwrotnej

Jak wspomniano wcześniej, generatywna AI tworzy współpracę między użytkownikiem a AI. Większość interakcji polega na tym, że użytkownik wprowadza prompt, a AI generuje wynik. A co, jeśli wynik jest niepoprawny? Jak aplikacja radzi sobie z błędami, jeśli wystąpią? Czy AI obwinia użytkownika, czy też poświęca czas na wyjaśnienie błędu?

Aplikacje AI powinny być budowane w taki sposób, aby otrzymywać i dawać informacje zwrotne. Pomaga to nie tylko systemowi AI się doskonalić, ale także buduje zaufanie wśród użytkowników. Pętla informacji zwrotnej powinna być wbudowana w projekt, przykładem może być prosty kciuk w górę lub w dół przy wyniku.

Innym sposobem na radzenie sobie z tym jest jasne komunikowanie możliwości i ograniczeń systemu. Kiedy użytkownik popełnia błąd, prosząc o coś poza możliwościami AI, powinien również istnieć sposób na radzenie sobie z tym, jak pokazano poniżej.

![Dawanie informacji zwrotnej i radzenie sobie z błędami](../../images/feedback-loops.png?WT.mc_id=academic-105485-koreyst)

Błędy systemowe są powszechne w aplikacjach, gdzie użytkownik może potrzebować pomocy z informacjami wykraczającymi poza zakres AI lub aplikacja może mieć limit liczby pytań/przedmiotów, dla których użytkownik może generować podsumowania. Na przykład, aplikacja AI wytrenowana na danych z ograniczonej liczby przedmiotów, na przykład Historii i Matematyki, może nie być w stanie obsłużyć pytań dotyczących Geografii. Aby złagodzić ten problem, system AI może dać odpowiedź typu: "Przepraszam, nasz produkt został wytrenowany na danych z następujących przedmiotów..., nie jestem w stanie odpowiedzieć na zadane pytanie."

Aplikacje AI nie są doskonałe, dlatego są podatne na błędy. Projektując swoje aplikacje, powinieneś upewnić się, że tworzysz przestrzeń na informacje zwrotne od użytkowników i obsługę błędów w sposób, który jest prosty i łatwy do wyjaśnienia.

## Zadanie

Weź dowolne aplikacje AI, które dotychczas zbudowałeś, rozważ wdrożenie poniższych kroków w swojej aplikacji:

- **Przyjemność:** Zastanów się, jak możesz uczynić swoją aplikację bardziej przyjemną. Czy dodajesz wyjaśnienia wszędzie? Czy zachęcasz użytkownika do eksploracji? Jak formujesz swoje komunikaty o błędach?

- **Użyteczność:** Budując aplikację webową. Upewnij się, że Twoja aplikacja jest nawigowalna zarówno za pomocą myszy, jak i klawiatury.

- **Zaufanie i przejrzystość:** Nie ufaj całkowicie AI i jej wynikom, zastanów się, jak dodałbyś człowieka do procesu weryfikacji wyniku. Rozważ i wdróż również inne sposoby osiągnięcia zaufania i przejrzystości.

- **Kontrola:** Daj użytkownikowi kontrolę nad danymi, które dostarczają aplikacji. Wdróż sposób, w jaki użytkownik może wyrazić zgodę i zrezygnować z gromadzenia danych w aplikacji AI.

<!-- ## [Quiz po wykładzie](quiz-url) -->

## Kontynuuj naukę!

Po ukończeniu tej lekcji, sprawdź naszą [Kolekcję nauki o Generatywnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby kontynuować podnoszenie swojej wiedzy o Generatywnej AI!

Przejdź do Lekcji 13, gdzie przyjrzymy się, jak [zabezpieczać aplikacje AI](../../../13-securing-ai-applications/translations/pl/README.md?WT.mc_id=academic-105485-koreyst)!
