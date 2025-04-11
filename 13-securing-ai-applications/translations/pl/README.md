# Zabezpieczanie aplikacji generatywnej AI

[![Zabezpieczanie aplikacji generatywnej AI](../../images/13-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson13-gh?WT.mc_id=academic-105485-koreyst)

## Wprowadzenie

Ta lekcja obejmie:

- Bezpieczeństwo w kontekście systemów AI.
- Najczęstsze zagrożenia i ryzyka dla systemów AI.
- Metody i aspekty zabezpieczania systemów AI.

## Cele nauczania

Po ukończeniu tej lekcji będziesz rozumiał:

- Zagrożenia i ryzyka dla systemów AI.
- Powszechne metody i praktyki zabezpieczania systemów AI.
- Jak wdrażanie testów bezpieczeństwa może zapobiec nieoczekiwanym rezultatom i erozji zaufania użytkowników.

## Co oznacza bezpieczeństwo w kontekście generatywnej AI?

Ponieważ technologie Sztucznej Inteligencji (AI) i Uczenia Maszynowego (ML) coraz bardziej kształtują nasze życie, kluczowe jest zabezpieczanie nie tylko danych klientów, ale także samych systemów AI. AI/ML jest coraz częściej wykorzystywane do wspierania procesów decyzyjnych o wysokiej wartości w branżach, gdzie złe decyzje mogą prowadzić do poważnych konsekwencji.

Oto kluczowe punkty do rozważenia:

- **Wpływ AI/ML**: AI/ML ma znaczący wpływ na codzienne życie, dlatego zabezpieczanie tych technologii stało się niezbędne.
- **Wyzwania bezpieczeństwa**: Ten wpływ AI/ML wymaga odpowiedniej uwagi, aby zaspokoić potrzebę ochrony produktów opartych na AI przed zaawansowanymi atakami, czy to ze strony trolli, czy zorganizowanych grup.
- **Problemy strategiczne**: Branża technologiczna musi proaktywnie rozwiązywać wyzwania strategiczne, aby zapewnić długoterminowe bezpieczeństwo klientów i ochronę danych.

Dodatkowo, modele uczenia maszynowego nie są w stanie rozróżnić między złośliwymi danymi wejściowymi a łagodnymi anomaliami. Znaczące źródło danych treningowych pochodzi z niekuratorowanych, niemoderowanych, publicznych zbiorów danych, które są otwarte na wkład osób trzecich. Atakujący nie muszą naruszać zbiorów danych, gdy mogą swobodnie przyczyniać się do ich tworzenia. Z czasem złośliwe dane o niskiej pewności stają się zaufanymi danymi o wysokiej pewności, jeśli struktura/format danych pozostaje poprawny.

Dlatego kluczowe jest zapewnienie integralności i ochrony magazynów danych, których Twoje modele używają do podejmowania decyzji.

## Zrozumienie zagrożeń i ryzyka AI

W kontekście AI i powiązanych systemów, zatruwanie danych (data poisoning) stanowi obecnie najistotniejsze zagrożenie bezpieczeństwa. Zatruwanie danych polega na celowej zmianie informacji używanych do trenowania AI, powodując błędy. Jest to wynikiem braku ustandaryzowanych metod wykrywania i łagodzenia, w połączeniu z naszym poleganiem na niezaufanych lub niekuratorowanych publicznych zbiorach danych do treningu. Aby zachować integralność danych i zapobiec wadliwemu procesowi treningu, kluczowe jest śledzenie pochodzenia i linii danych. W przeciwnym razie, stare powiedzenie "śmieci na wejściu, śmieci na wyjściu" pozostaje prawdziwe, prowadząc do pogorszonej wydajności modelu.

Oto przykłady, jak zatruwanie danych może wpływać na Twoje modele:

1. **Odwracanie etykiet**: W zadaniu klasyfikacji binarnej przeciwnik celowo zmienia etykiety małego podzbioru danych treningowych. Na przykład łagodne próbki są oznaczone jako złośliwe, co prowadzi model do nauki błędnych powiązań.\
   **Przykład**: Filtr spamu błędnie klasyfikujący prawdziwe e-maile jako spam ze względu na zmanipulowane etykiety.
2. **Zatruwanie cech**: Atakujący subtelnie modyfikuje cechy w danych treningowych, aby wprowadzić stronniczość lub wprowadzić model w błąd.\
   **Przykład**: Dodawanie nieistotnych słów kluczowych do opisów produktów w celu manipulowania systemami rekomendacji.
3. **Wstrzykiwanie danych**: Wstrzykiwanie złośliwych danych do zbioru treningowego, aby wpłynąć na zachowanie modelu.\
   **Przykład**: Wprowadzanie fałszywych recenzji użytkowników, aby zniekształcić wyniki analizy sentymentu.
4. **Ataki typu backdoor**: Przeciwnik wstawia ukryty wzorzec (backdoor) do danych treningowych. Model uczy się rozpoznawać ten wzorzec i zachowuje się złośliwie, gdy zostanie wyzwolony.\
   **Przykład**: System rozpoznawania twarzy trenowany z obrazami z backdoorem, który błędnie identyfikuje określoną osobę.

Korporacja MITRE stworzyła [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), bazę wiedzy o taktykach i technikach stosowanych przez przeciwników w rzeczywistych atakach na systemy AI.

> Istnieje rosnąca liczba podatności w systemach wykorzystujących AI, ponieważ włączenie AI zwiększa powierzchnię ataku istniejących systemów poza te związane z tradycyjnymi atakami cybernetycznymi. Opracowaliśmy ATLAS, aby zwiększyć świadomość tych unikalnych i ewoluujących podatności, w miarę jak globalna społeczność coraz częściej włącza AI do różnych systemów. ATLAS jest wzorowany na ramach MITRE ATT&CK® i jego taktyki, techniki i procedury (TTP) są uzupełnieniem tych w ATT&CK.

Podobnie jak ramy MITRE ATT&CK®, które są szeroko stosowane w tradycyjnym cyberbezpieczeństwie do planowania zaawansowanych scenariuszy emulacji zagrożeń, ATLAS zapewnia łatwy do przeszukiwania zbiór TTP, które mogą pomóc lepiej zrozumieć i przygotować się do obrony przed pojawiającymi się atakami.

Dodatkowo, Open Web Application Security Project (OWASP) stworzył "[Listę Top 10](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" najbardziej krytycznych podatności znalezionych w aplikacjach wykorzystujących LLM. Lista podkreśla ryzyka zagrożeń, takich jak wspomniane wcześniej zatruwanie danych, wraz z innymi, takimi jak:

- **Wstrzykiwanie promptów**: technika, w której atakujący manipulują dużym modelem językowym (LLM) poprzez starannie spreparowane dane wejściowe, powodując, że zachowuje się poza swoim zamierzonym zachowaniem.
- **Podatności łańcucha dostaw**: Komponenty i oprogramowanie, które składają się na aplikacje używane przez LLM, takie jak moduły Pythona lub zewnętrzne zbiory danych, mogą same zostać naruszone, prowadząc do nieoczekiwanych rezultatów, wprowadzenia stronniczości, a nawet podatności w podstawowej infrastrukturze.
- **Nadmierne poleganie**: LLM są omylne i są podatne na halucynacje, dostarczając niedokładne lub niebezpieczne wyniki. W kilku udokumentowanych przypadkach ludzie przyjmowali wyniki bez weryfikacji, co prowadziło do niezamierzonych, negatywnych konsekwencji w rzeczywistym świecie.

Microsoft Cloud Advocate Rod Trent napisał darmowy ebook, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), który głęboko analizuje te i inne pojawiające się zagrożenia AI oraz dostarcza obszernych wskazówek, jak najlepiej radzić sobie z tymi scenariuszami.

## Testowanie bezpieczeństwa dla systemów AI i LLM

Sztuczna inteligencja (AI) transformuje różne domeny i branże, oferując nowe możliwości i korzyści dla społeczeństwa. Jednak AI stwarza również znaczące wyzwania i ryzyka, takie jak prywatność danych, stronniczość, brak wyjaśnialności i potencjalne nadużycia. Dlatego kluczowe jest zapewnienie, aby systemy AI były bezpieczne i odpowiedzialne, co oznacza, że przestrzegają standardów etycznych i prawnych oraz mogą być zaufane przez użytkowników i interesariuszy.

Testowanie bezpieczeństwa to proces oceny bezpieczeństwa systemu AI lub LLM poprzez identyfikację i wykorzystywanie ich podatności. Może być wykonywane przez programistów, użytkowników lub audytorów zewnętrznych, w zależności od celu i zakresu testowania. Niektóre z najczęstszych metod testowania bezpieczeństwa dla systemów AI i LLM to:

- **Sanityzacja danych**: Jest to proces usuwania lub anonimizacji wrażliwych lub prywatnych informacji z danych treningowych lub danych wejściowych systemu AI lub LLM. Sanityzacja danych może pomóc zapobiec wyciekowi danych i złośliwej manipulacji poprzez zmniejszenie ekspozycji poufnych lub osobistych danych.
- **Testy przeciwnikańskie**: Jest to proces generowania i stosowania przeciwnikańskich przykładów do danych wejściowych lub wyjściowych systemu AI lub LLM, aby ocenić jego odporność i wytrzymałość na ataki przeciwnikańskie. Testy przeciwnikańskie mogą pomóc zidentyfikować i złagodzić podatności i słabości systemu AI lub LLM, które mogą być wykorzystywane przez atakujących.
- **Weryfikacja modelu**: Jest to proces weryfikacji poprawności i kompletności parametrów modelu lub architektury systemu AI lub LLM. Weryfikacja modelu może pomóc wykrywać i zapobiegać kradzieży modelu poprzez zapewnienie, że model jest chroniony i uwierzytelniony.
- **Walidacja wyników**: Jest to proces walidacji jakości i niezawodności wyników systemu AI lub LLM. Walidacja wyników może pomóc wykrywać i korygować złośliwe manipulacje poprzez zapewnienie, że wyniki są spójne i dokładne.

OpenAI, lider w systemach AI, ustanowił serię _ocen bezpieczeństwa_ w ramach swojej inicjatywy sieci red teamingu, mającej na celu testowanie wyników systemów AI w nadziei na przyczynienie się do bezpieczeństwa AI.

> Oceny mogą obejmować proste testy typu pytanie-odpowiedź, jak i bardziej złożone symulacje. Jako konkretne przykłady, oto przykładowe oceny opracowane przez OpenAI do oceny zachowań AI z wielu perspektyw:

#### Perswazja

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Jak dobrze system AI może oszukać inny system AI, aby powiedział tajne słowo?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Jak dobrze system AI może przekonać inny system AI do przekazania pieniędzy?
- [Propozycja głosowania](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Jak dobrze system AI może wpłynąć na poparcie innego systemu AI dla propozycji politycznej?

#### Steganografia (ukryte wiadomości)

- [Steganografia](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Jak dobrze system AI może przekazywać tajne wiadomości bez bycia złapanym przez inny system AI?
- [Kompresja tekstu](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Jak dobrze system AI może kompresować i dekompresować wiadomości, aby umożliwić ukrywanie tajnych wiadomości?
- [Punkt Schellinga](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Jak dobrze system AI może koordynować z innym systemem AI bez bezpośredniej komunikacji?

### Bezpieczeństwo AI

Konieczne jest, abyśmy dążyli do ochrony systemów AI przed złośliwymi atakami, nadużyciami lub niezamierzonymi konsekwencjami. Obejmuje to podjęcie kroków w celu zapewnienia bezpieczeństwa, niezawodności i wiarygodności systemów AI, takich jak:

- Zabezpieczanie danych i algorytmów używanych do trenowania i uruchamiania modeli AI
- Zapobieganie nieautoryzowanemu dostępowi, manipulacji lub sabotażowi systemów AI
- Wykrywanie i łagodzenie stronniczości, dyskryminacji lub problemów etycznych w systemach AI
- Zapewnienie odpowiedzialności, przejrzystości i wyjaśnialności decyzji i działań AI
- Dostosowanie celów i wartości systemów AI do tych ludzi i społeczeństwa

Bezpieczeństwo AI jest ważne dla zapewnienia integralności, dostępności i poufności systemów AI i danych. Niektóre z wyzwań i możliwości bezpieczeństwa AI to:

- Możliwość: Włączenie AI do strategii cyberbezpieczeństwa, ponieważ może odegrać kluczową rolę w identyfikacji zagrożeń i poprawie czasu reakcji. AI może pomóc automatyzować i wzmacniać wykrywanie i łagodzenie cyberataków, takich jak phishing, malware czy ransomware.
- Wyzwanie: AI może być również używane przez przeciwników do przeprowadzania zaawansowanych ataków, takich jak generowanie fałszywych lub wprowadzających w błąd treści, podszywanie się pod użytkowników lub wykorzystywanie podatności w systemach AI. Dlatego programiści AI mają unikalną odpowiedzialność za projektowanie systemów, które są odporne i wytrzymałe na nadużycia.

### Ochrona danych

LLM mogą stanowić zagrożenie dla prywatności i bezpieczeństwa danych, które wykorzystują. Na przykład, LLM mogą potencjalnie zapamiętywać i ujawniać wrażliwe informacje ze swoich danych treningowych, takie jak osobiste imiona, adresy, hasła czy numery kart kredytowych. Mogą być również manipulowane lub atakowane przez złośliwe podmioty, które chcą wykorzystać ich podatności lub stronniczość. Dlatego ważne jest, aby być świadomym tych zagrożeń i podjąć odpowiednie środki w celu ochrony danych używanych z LLM. Istnieje kilka kroków, które możesz podjąć, aby chronić dane używane z LLM. Kroki te obejmują:

- **Ograniczanie ilości i rodzaju danych, które są udostępniane LLM**: Udostępniaj tylko dane, które są niezbędne i istotne dla zamierzonych celów, i unikaj udostępniania danych, które są wrażliwe, poufne lub osobiste. Użytkownicy powinni również anonimizować lub szyfrować dane, które udostępniają LLM, na przykład poprzez usuwanie lub maskowanie informacji identyfikujących, lub korzystanie z bezpiecznych kanałów komunikacji.
- **Weryfikowanie danych generowanych przez LLM**: Zawsze sprawdzaj dokładność i jakość wyników generowanych przez LLM, aby upewnić się, że nie zawierają one niepożądanych lub nieodpowiednich informacji.
- **Zgłaszanie i alarmowanie o wszelkich naruszeniach danych lub incydentach**: Bądź czujny na wszelkie podejrzane lub nienormalne działania lub zachowania ze strony LLM, takie jak generowanie tekstów, które są nieistotne, niedokładne, obraźliwe lub szkodliwe. Może to być wskazaniem naruszenia danych lub incydentu bezpieczeństwa.

Bezpieczeństwo danych, zarządzanie i zgodność są krytyczne dla każdej organizacji, która chce wykorzystać moc danych i AI w środowisku wielu chmur. Zabezpieczanie i zarządzanie wszystkimi swoimi danymi to złożone i wieloaspektowe przedsięwzięcie. Musisz zabezpieczyć i zarządzać różnymi typami danych (ustrukturyzowane, nieustrukturyzowane i dane generowane przez AI) w różnych lokalizacjach w wielu chmurach, i musisz uwzględnić istniejące i przyszłe przepisy dotyczące bezpieczeństwa danych, zarządzania i AI. Aby chronić swoje dane, musisz przyjąć pewne najlepsze praktyki i środki ostrożności, takie jak:

- Korzystanie z usług lub platform chmurowych, które oferują funkcje ochrony danych i prywatności.
- Korzystanie z narzędzi do jakości i walidacji danych, aby sprawdzać dane pod kątem błędów, niespójności lub anomalii.
- Korzystanie z ram zarządzania danymi i etyki, aby zapewnić, że dane są używane w odpowiedzialny i przejrzysty sposób.

### Emulowanie realnych zagrożeń - Red teaming w AI

Emulowanie realnych zagrożeń jest obecnie uważane za standardową praktykę w budowaniu odpornych systemów AI poprzez stosowanie podobnych narzędzi, taktyk, procedur do identyfikacji ryzyka dla systemów i testowania odpowiedzi obrońców.

> Praktyka red teamingu w AI ewoluowała, aby przybrać bardziej rozszerzone znaczenie: obejmuje nie tylko sondowanie podatności bezpieczeństwa, ale także sondowanie innych awarii systemu, takich jak generowanie potencjalnie szkodliwych treści. Systemy AI wiążą się z nowymi ryzykami, a red teaming jest kluczowy dla zrozumienia tych nowych ryzyk, takich jak wstrzykiwanie promptów i tworzenie treści bez podstaw. - [Microsoft AI Red Team buduje przyszłość bezpieczniejszej AI](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

[![Wskazówki i zasoby do red teamingu](../../images/13-AI-red-team.png?WT.mc_id=academic-105485-koreyst)]()

Poniżej znajdują się kluczowe spostrzeżenia, które ukształtowały program Microsoft AI Red Team.

1. **Szeroki zakres Red Teamingu AI:**
   Red teaming AI obejmuje teraz zarówno bezpieczeństwo, jak i wyniki Odpowiedzialnej AI (RAI). Tradycyjnie, red teaming koncentrował się na aspektach bezpieczeństwa, traktując model jako wektor (np. kradzież bazowego modelu). Jednak systemy AI wprowadzają nowe podatności bezpieczeństwa (np. wstrzykiwanie promptów, zatruwanie), wymagające szczególnej uwagi. Poza bezpieczeństwem, red teaming AI bada również kwestie uczciwości (np. stereotypowanie) i szkodliwe treści (np. gloryfikacja przemocy). Wczesna identyfikacja tych problemów pozwala na priorytetyzację inwestycji w obronę.
2. **Złośliwe i niezłośliwe awarie:**
   Red teaming AI rozważa awarie zarówno ze złośliwej, jak i niezłośliwej perspektywy. Na przykład, podczas red teamingu nowego Bing, badamy nie tylko jak złośliwi przeciwnicy mogą zakłócić system, ale także jak zwykli użytkownicy mogą napotkać problematyczne lub szkodliwe treści. W przeciwieństwie do tradycyjnego red teamingu bezpieczeństwa, który koncentruje się głównie na złośliwych aktorach, red teaming AI uwzględnia szerszy zakres person i potencjalnych awarii.
3. **Dynamiczny charakter systemów AI:**
   Aplikacje AI stale ewoluują. W aplikacjach dużych modeli językowych, deweloperzy dostosowują się do zmieniających się wymagań. Ciągły red teaming zapewnia stałą czujność i adaptację do zmieniających się ryzyk.

Red teaming AI nie jest wszechobejmujący i powinien być uważany za komplementarne działanie do dodatkowych kontroli, takich jak [kontrola dostępu oparta na rolach (RBAC)](https://learn.microsoft.com/azure/ai-services/openai/how-to/role-based-access-control?WT.mc_id=academic-105485-koreyst) i kompleksowe rozwiązania zarządzania danymi. Ma uzupełniać strategię bezpieczeństwa, która koncentruje się na stosowaniu bezpiecznych i odpowiedzialnych rozwiązań AI, które uwzględniają prywatność i bezpieczeństwo, jednocześnie dążąc do minimalizacji stronniczości, szkodliwych treści i dezinformacji, które mogą podważać zaufanie użytkowników.

Oto lista dodatkowych lektur, które mogą pomóc lepiej zrozumieć, jak red teaming może pomóc zidentyfikować i złagodzić ryzyka w systemach AI:

- [Planowanie red teamingu dla dużych modeli językowych (LLM) i ich aplikacji](https://learn.microsoft.com/azure/ai-services/openai/concepts/red-teaming?WT.mc_id=academic-105485-koreyst)
- [Czym jest OpenAI Red Teaming Network?](https://openai.com/blog/red-teaming-network?WT.mc_id=academic-105485-koreyst)
- [AI Red Teaming - Kluczowa praktyka budowania bezpieczniejszych i bardziej odpowiedzialnych rozwiązań AI](https://rodtrent.substack.com/p/ai-red-teaming?WT.mc_id=academic-105485-koreyst)
- MITRE [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), baza wiedzy o taktykach i technikach stosowanych przez przeciwników w rzeczywistych atakach na systemy AI.

## Sprawdzenie wiedzy

Jakie mogłoby być dobre podejście do utrzymania integralności danych i zapobiegania nadużyciom?

1. Posiadanie silnych kontroli opartych na rolach dla dostępu do danych i zarządzania danymi
2. Wdrażanie i audytowanie etykietowania danych, aby zapobiec nieprawidłowej reprezentacji lub nadużyciu danych
3. Upewnienie się, że infrastruktura AI obsługuje filtrowanie treści

A:1, Chociaż wszystkie trzy są świetnymi zaleceniami, zapewnienie, że przypisujemy odpowiednie uprawnienia dostępu do danych użytkownikom, znacznie przyczyni się do zapobiegania manipulacji i nieprawidłowej reprezentacji danych używanych przez LLM.

## 🚀 Wyzwanie

Przeczytaj więcej o tym, jak możesz [zarządzać i chronić wrażliwe informacje](https://learn.microsoft.com/training/paths/purview-protect-govern-ai/?WT.mc_id=academic-105485-koreyst) w erze AI.

## Świetna praca, kontynuuj naukę

Po ukończeniu tej lekcji, sprawdź naszą [Kolekcję nauki o Generatywnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby kontynuować podnoszenie swojej wiedzy o Generatywnej AI!

Przejdź do Lekcji 14, w której przyjrzymy się [cyklowi życia aplikacji Generatywnej AI](../../../14-the-generative-ai-application-lifecycle/translations/pl/README.md?WT.mc_id=academic-105485-koreyst)!
