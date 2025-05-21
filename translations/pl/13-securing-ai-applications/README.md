<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-05-19T22:42:45+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "pl"
}
-->
# Zabezpieczanie aplikacji generatywnej AI

## Wprowadzenie

Ta lekcja obejmuje:

- Bezpieczeństwo w kontekście systemów AI.
- Typowe zagrożenia i ryzyka dla systemów AI.
- Metody i rozważania dotyczące zabezpieczania systemów AI.

## Cele nauki

Po ukończeniu tej lekcji będziesz mieć zrozumienie:

- Zagrożeń i ryzyk dla systemów AI.
- Typowych metod i praktyk zabezpieczania systemów AI.
- Jak wdrożenie testów bezpieczeństwa może zapobiec nieoczekiwanym wynikom i utracie zaufania użytkowników.

## Co oznacza bezpieczeństwo w kontekście generatywnej AI?

W miarę jak technologie Sztucznej Inteligencji (AI) i Uczenia Maszynowego (ML) coraz bardziej kształtują nasze życie, istotne jest, aby chronić nie tylko dane klientów, ale także same systemy AI. AI/ML jest coraz częściej wykorzystywane w procesach decyzyjnych o wysokiej wartości w branżach, gdzie błędna decyzja może prowadzić do poważnych konsekwencji.

Oto kluczowe punkty do rozważenia:

- **Wpływ AI/ML**: AI/ML mają znaczący wpływ na codzienne życie, a ich ochrona stała się niezbędna.
- **Wyzwania związane z bezpieczeństwem**: Ten wpływ AI/ML wymaga odpowiedniej uwagi, aby chronić produkty oparte na AI przed zaawansowanymi atakami, czy to przez trolle, czy zorganizowane grupy.
- **Problemy strategiczne**: Branża technologiczna musi proaktywnie podejść do wyzwań strategicznych, aby zapewnić długoterminowe bezpieczeństwo klientów i ochronę danych.

Dodatkowo, modele uczenia maszynowego często nie potrafią rozróżnić między złośliwym a łagodnym anomalnym danymi. Znaczna część danych treningowych pochodzi z niekuratorowanych, niemoderowanych, publicznych zbiorów danych, które są otwarte na wkłady stron trzecich. Atakujący nie muszą naruszać zbiorów danych, gdy mogą do nich swobodnie dodawać. Z czasem dane o niskiej pewności siebie stają się zaufanymi danymi o wysokiej pewności, jeśli struktura/formatu danych pozostaje poprawna.

Dlatego kluczowe jest zapewnienie integralności i ochrony zbiorów danych, z których korzystają Twoje modele do podejmowania decyzji.

## Zrozumienie zagrożeń i ryzyk AI

W kontekście AI i systemów z nimi związanych, zatruwanie danych wyróżnia się jako najważniejsze zagrożenie bezpieczeństwa dzisiaj. Zatruwanie danych to sytuacja, gdy ktoś celowo zmienia informacje używane do trenowania AI, co powoduje, że popełnia ona błędy. Dzieje się tak z powodu braku standardowych metod wykrywania i łagodzenia, w połączeniu z naszym poleganiem na nieufnych lub niekuratorowanych publicznych zbiorach danych do treningu. Aby utrzymać integralność danych i zapobiec wadliwemu procesowi treningowemu, kluczowe jest śledzenie pochodzenia i rodowodu danych. W przeciwnym razie, stare powiedzenie „śmieci na wejściu, śmieci na wyjściu” okazuje się prawdziwe, prowadząc do pogorszenia wydajności modelu.

Oto przykłady, jak zatruwanie danych może wpływać na Twoje modele:

1. **Odwracanie etykiet**: W zadaniu klasyfikacji binarnej, przeciwnik celowo zmienia etykiety niewielkiego podzbioru danych treningowych. Na przykład, łagodne próbki są oznaczane jako złośliwe, co prowadzi do tego, że model uczy się nieprawidłowych skojarzeń.\
   **Przykład**: Filtr antyspamowy błędnie klasyfikujący legalne e-maile jako spam z powodu zmanipulowanych etykiet.
2. **Zatruwanie cech**: Atakujący subtelnie modyfikuje cechy w danych treningowych, aby wprowadzić bias lub wprowadzić model w błąd.\
   **Przykład**: Dodawanie nieistotnych słów kluczowych do opisów produktów w celu manipulacji systemami rekomendacji.
3. **Wstrzykiwanie danych**: Wstrzykiwanie złośliwych danych do zestawu treningowego w celu wpłynięcia na zachowanie modelu.\
   **Przykład**: Wprowadzanie fałszywych recenzji użytkowników w celu zniekształcenia wyników analizy sentymentu.
4. **Ataki z tylnymi drzwiami**: Przeciwnik wprowadza ukryty wzór (tylne drzwi) do danych treningowych. Model uczy się rozpoznawać ten wzór i zachowuje się złośliwie, gdy zostanie wyzwolony.\
   **Przykład**: System rozpoznawania twarzy trenowany z obrazami z tylnymi drzwiami, który błędnie identyfikuje konkretną osobę.

MITRE Corporation stworzyła [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), bazę wiedzy o taktykach i technikach stosowanych przez przeciwników w rzeczywistych atakach na systemy AI.

> Coraz większa liczba luk w systemach obsługujących AI, ponieważ włączenie AI zwiększa powierzchnię ataku istniejących systemów poza te tradycyjnych cyberataków. Opracowaliśmy ATLAS, aby zwiększyć świadomość tych unikalnych i ewoluujących luk, ponieważ globalna społeczność coraz bardziej włącza AI do różnych systemów. ATLAS jest wzorowany na frameworku MITRE ATT&CK® i jego taktyki, techniki i procedury (TTP) są komplementarne do tych w ATT&CK.

Podobnie jak framework MITRE ATT&CK®, który jest szeroko stosowany w tradycyjnym bezpieczeństwie cybernetycznym do planowania zaawansowanych scenariuszy emulacji zagrożeń, ATLAS zapewnia łatwo przeszukiwalny zestaw TTP, który może pomóc w lepszym zrozumieniu i przygotowaniu się do obrony przed pojawiającymi się atakami.

Dodatkowo, Open Web Application Security Project (OWASP) stworzyła "[Top 10 listę](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" najważniejszych luk w aplikacjach wykorzystujących LLM. Lista podkreśla ryzyko zagrożeń, takich jak wspomniane zatruwanie danych, a także inne, takie jak:

- **Wstrzykiwanie promptów**: technika, w której atakujący manipulują dużym modelem językowym (LLM) poprzez starannie przygotowane dane wejściowe, powodując, że działa on poza zamierzonym zachowaniem.
- **Luki w łańcuchu dostaw**: Komponenty i oprogramowanie, które tworzą aplikacje używane przez LLM, takie jak moduły Pythona czy zewnętrzne zestawy danych, same mogą być naruszone, prowadząc do nieoczekiwanych wyników, wprowadzonych biasów, a nawet luk w infrastrukturze.
- **Nadmierne poleganie**: LLM są omylne i mają skłonność do halucynacji, dostarczając niedokładne lub niebezpieczne wyniki. W kilku udokumentowanych przypadkach ludzie przyjmowali wyniki za pewnik, co prowadziło do niezamierzonych negatywnych konsekwencji w rzeczywistości.

Microsoft Cloud Advocate Rod Trent napisał darmowy ebook, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), który głęboko zanurza się w te i inne pojawiające się zagrożenia AI i zapewnia obszerne wskazówki, jak najlepiej radzić sobie z tymi scenariuszami.

## Testowanie bezpieczeństwa systemów AI i LLM

Sztuczna inteligencja (AI) przekształca różne dziedziny i branże, oferując nowe możliwości i korzyści dla społeczeństwa. Jednak AI niesie ze sobą również znaczące wyzwania i ryzyka, takie jak prywatność danych, bias, brak wyjaśnialności i potencjalne nadużycia. Dlatego kluczowe jest zapewnienie, że systemy AI są bezpieczne i odpowiedzialne, co oznacza, że przestrzegają standardów etycznych i prawnych i mogą być zaufane przez użytkowników i interesariuszy.

Testowanie bezpieczeństwa to proces oceny bezpieczeństwa systemu AI lub LLM poprzez identyfikację i wykorzystywanie ich luk. Może być przeprowadzane przez deweloperów, użytkowników lub zewnętrznych audytorów, w zależności od celu i zakresu testowania. Niektóre z najczęstszych metod testowania bezpieczeństwa systemów AI i LLM to:

- **Sanityzacja danych**: To proces usuwania lub anonimizowania poufnych lub prywatnych informacji z danych treningowych lub danych wejściowych systemu AI lub LLM. Sanityzacja danych może pomóc w zapobieganiu wyciekowi danych i złośliwej manipulacji poprzez zmniejszenie ekspozycji na poufne lub osobiste dane.
- **Testowanie adwersarialne**: To proces generowania i stosowania przykładów adwersarialnych do danych wejściowych lub wyjściowych systemu AI lub LLM w celu oceny jego odporności i wytrzymałości na ataki adwersarialne. Testowanie adwersarialne może pomóc w identyfikacji i łagodzeniu luk i słabości systemu AI lub LLM, które mogą być wykorzystywane przez atakujących.
- **Weryfikacja modelu**: To proces weryfikacji poprawności i kompletności parametrów modelu lub architektury systemu AI lub LLM. Weryfikacja modelu może pomóc w wykrywaniu i zapobieganiu kradzieży modelu poprzez zapewnienie, że model jest chroniony i uwierzytelniony.
- **Walidacja wyników**: To proces walidacji jakości i wiarygodności wyników systemu AI lub LLM. Walidacja wyników może pomóc w wykrywaniu i korygowaniu złośliwej manipulacji poprzez zapewnienie, że wyniki są spójne i dokładne.

OpenAI, lider w systemach AI, ustanowiło serię _ocen bezpieczeństwa_ w ramach swojej inicjatywy red teaming, mającej na celu testowanie wyników systemów AI w nadziei na przyczynienie się do bezpieczeństwa AI.

> Oceny mogą obejmować proste testy Q&A po bardziej złożone symulacje. Jako konkretne przykłady, oto przykładowe oceny opracowane przez OpenAI do oceny zachowań AI z różnych perspektyw:

#### Perswazja

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Jak dobrze system AI potrafi oszukać inny system AI, by powiedział tajne słowo?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Jak dobrze system AI potrafi przekonać inny system AI do przekazania pieniędzy?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Jak dobrze system AI potrafi wpłynąć na poparcie innego systemu AI dla propozycji politycznej?

#### Steganografia (ukryte wiadomości)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Jak dobrze system AI potrafi przekazywać tajne wiadomości, nie będąc wykrytym przez inny system AI?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Jak dobrze system AI potrafi kompresować i dekompresować wiadomości, aby umożliwić ukrywanie tajnych wiadomości?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Jak dobrze system AI potrafi koordynować się z innym systemem AI bez bezpośredniej komunikacji?

### Bezpieczeństwo AI

To kluczowe, aby dążyć do ochrony systemów AI przed złośliwymi atakami, nadużyciami lub niezamierzonymi konsekwencjami. Obejmuje to podjęcie kroków w celu zapewnienia bezpieczeństwa, niezawodności i zaufania do systemów AI, takich jak:

- Zabezpieczanie danych i algorytmów używanych do trenowania i uruchamiania modeli AI
- Zapobieganie nieautoryzowanemu dostępowi, manipulacji lub sabotażu systemów AI
- Wykrywanie i łagodzenie biasów, dyskryminacji lub problemów etycznych w systemach AI
- Zapewnienie odpowiedzialności, przejrzystości i wyjaśnialności decyzji i działań AI
- Zgodność celów i wartości systemów AI z celami i wartościami ludzi i społeczeństwa

Bezpieczeństwo AI jest ważne dla zapewnienia integralności, dostępności i poufności systemów AI i danych. Niektóre z wyzwań i możliwości związanych z bezpieczeństwem AI to:

- Możliwość: Włączenie AI do strategii cyberbezpieczeństwa, ponieważ może odgrywać kluczową rolę w identyfikacji zagrożeń i poprawie czasów reakcji. AI może pomóc w automatyzacji i wzmocnieniu wykrywania i łagodzenia cyberataków, takich jak phishing, malware czy ransomware.
- Wyzwanie: AI może być również wykorzystywane przez przeciwników do przeprowadzania zaawansowanych ataków, takich jak generowanie fałszywych lub wprowadzających w błąd treści, podszywanie się pod użytkowników lub wykorzystywanie luk w systemach AI. Dlatego deweloperzy AI mają unikalną odpowiedzialność za projektowanie systemów, które są odporne i wytrzymałe na nadużycia.

### Ochrona danych

LLM mogą stanowić zagrożenie dla prywatności i bezpieczeństwa danych, które wykorzystują. Na przykład LLM mogą potencjalnie zapamiętywać i ujawniać poufne informacje z danych treningowych, takie jak imiona, adresy, hasła czy numery kart kredytowych. Mogą być również manipulowane lub atakowane przez złośliwych aktorów, którzy chcą wykorzystać ich luki lub biasy. Dlatego ważne jest, aby być świadomym tych zagrożeń i podjąć odpowiednie środki, aby chronić dane używane z LLM. Istnieje kilka kroków, które można podjąć, aby chronić dane używane z LLM. Te kroki obejmują:

- **Ograniczenie ilości i rodzaju danych, które udostępniają LLM**: Udostępniaj tylko dane, które są niezbędne i istotne dla zamierzonych celów, i unikaj udostępniania danych, które są poufne, tajne lub osobiste. Użytkownicy powinni również anonimizować lub szyfrować dane, które udostępniają LLM, na przykład poprzez usuwanie lub maskowanie wszelkich informacji identyfikujących lub korzystanie z bezpiecznych kanałów komunikacji.
- **Weryfikacja danych generowanych przez LLM**: Zawsze sprawdzaj dokładność i jakość wyników generowanych przez LLM, aby upewnić się, że nie zawierają niepożądanych lub nieodpowiednich informacji.
- **Zgłaszanie i alarmowanie o wszelkich naruszeniach danych lub incydentach**: Bądź czujny na wszelkie podejrzane lub nieprawidłowe działania lub zachowania LLM, takie jak generowanie tekstów, które są nieistotne, niedokładne, obraźliwe lub szkodliwe. Może to być oznaką naruszenia danych lub incydentu bezpieczeństwa.

Bezpieczeństwo danych, zarządzanie i zgodność są kluczowe dla każdej organizacji, która chce wykorzystać moc danych i AI w środowisku wielochmurowym. Zabezpieczenie i zarządzanie wszystkimi danymi to skomplikowane i wieloaspektowe przedsięwzięcie. Musisz zabezpieczyć i zarządzać różnymi rodzajami danych (ustrukturyzowanymi, nieustrukturyzowanymi i generowanymi przez AI) w różnych lokalizacjach w wielu chmurach i musisz uwzględniać istniejące i przyszłe regulacje dotyczące bezpieczeństwa danych, zarządzania i AI. Aby chronić swoje dane, musisz przyjąć najlepsze praktyki i środki ostrożności, takie jak:

- Korzystanie z usług chmurowych lub platform oferujących funkcje ochrony danych i prywatności.
- Korzystanie z narzędzi do zapewnienia jakości danych i walidacji, aby spraw

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest profesjonalne tłumaczenie przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.