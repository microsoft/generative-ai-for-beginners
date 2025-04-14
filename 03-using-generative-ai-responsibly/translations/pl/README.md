# Odpowiedzialne Korzystanie z Generatywnej SI

[![Odpowiedzialne Korzystanie z Generatywnej SI](../../images/03-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson3-gh?WT.mc_id=academic-105485-koreyst)

> _Kliknij powyższy obraz, aby obejrzeć wideo tej lekcji_

Łatwo jest być zafascynowanym sztuczną inteligencją, a w szczególności generatywną SI, ale musisz rozważyć, jak odpowiedzialnie z niej korzystać. Musisz wziąć pod uwagę takie kwestie jak zapewnienie, że rezultat jest sprawiedliwy, nie szkodliwy i więcej. Ten rozdział ma na celu dostarczenie ci wspomnianego kontekstu, co wziąć pod uwagę i jak podjąć aktywne kroki w celu poprawy twojego korzystania z SI.

## Wprowadzenie

Ta lekcja obejmie:

- Dlaczego powinieneś priorytetowo traktować Odpowiedzialną SI podczas budowania aplikacji Generatywnej SI.
- Podstawowe zasady Odpowiedzialnej SI i jak odnoszą się one do Generatywnej SI.
- Jak wprowadzić te zasady Odpowiedzialnej SI w praktyce poprzez strategię i narzędzia.

## Cele Nauki

Po ukończeniu tej lekcji będziesz wiedzieć:

- Znaczenie Odpowiedzialnej SI podczas budowania aplikacji Generatywnej SI.
- Kiedy myśleć i stosować podstawowe zasady Odpowiedzialnej SI podczas budowania aplikacji Generatywnej SI.
- Jakie narzędzia i strategie są dostępne, aby wprowadzić koncepcję Odpowiedzialnej SI w praktyce.

## Zasady Odpowiedzialnej SI

Ekscytacja Generatywną SI nigdy nie była większa. Ta ekscytacja przyciągnęła wielu nowych deweloperów, uwagę i finansowanie do tej przestrzeni. Choć jest to bardzo pozytywne dla każdego, kto chce budować produkty i firmy korzystające z Generatywnej SI, ważne jest również, abyśmy postępowali odpowiedzialnie.

W całym tym kursie skupiamy się na budowaniu naszego startupu i naszego produktu edukacyjnego SI. Będziemy korzystać z zasad Odpowiedzialnej SI: Uczciwość, Inkluzywność, Niezawodność/Bezpieczeństwo, Ochrona i Prywatność, Przejrzystość i Odpowiedzialność. Z tymi zasadami zbadamy, jak odnoszą się one do naszego korzystania z Generatywnej SI w naszych produktach.

## Dlaczego Powinieneś Priorytetowo Traktować Odpowiedzialną SI

Podczas budowania produktu, przyjęcie podejścia skoncentrowanego na człowieku, mając na uwadze najlepszy interes użytkownika, prowadzi do najlepszych rezultatów.

Wyjątkowość Generatywnej SI polega na jej mocy tworzenia pomocnych odpowiedzi, informacji, wskazówek i treści dla użytkowników. Można to zrobić bez wielu ręcznych kroków, co może prowadzić do bardzo imponujących rezultatów. Bez odpowiedniego planowania i strategii może to również niestety prowadzić do pewnych szkodliwych rezultatów dla twoich użytkowników, twojego produktu i społeczeństwa jako całości.

Przyjrzyjmy się niektórym (ale nie wszystkim) z tych potencjalnie szkodliwych rezultatów:

### Halucynacje

Halucynacje to termin używany do opisania sytuacji, gdy LLM produkuje treść, która jest albo całkowicie bezsensowna, albo coś, co wiemy, że jest faktycznie błędne na podstawie innych źródeł informacji.

Weźmy na przykład, że budujemy funkcję dla naszego startupu, która pozwala uczniom zadawać pytania historyczne do modelu. Uczeń zadaje pytanie `Kto był jedynym ocalałym z Titanica?`

Model generuje odpowiedź taką jak poniższa:

![Prompt mówiący "Kto był jedynym ocalałym z Titanica"](../../images/ChatGPT-titanic-survivor-prompt.webp?WT.mc_id=academic-105485-koreyst)

> _(Źródło: [Flying bisons](https://flyingbisons.com?WT.mc_id=academic-105485-koreyst))_

Jest to bardzo pewna i dokładna odpowiedź. Niestety, jest niepoprawna. Nawet przy minimalnej ilości badań odkryłoby się, że było więcej niż jeden ocalały z katastrofy Titanica. Dla ucznia, który dopiero zaczyna badać ten temat, ta odpowiedź może być wystarczająco przekonująca, aby nie być kwestionowana i traktowana jako fakt. Konsekwencje tego mogą prowadzić do tego, że system SI jest niewiarygodny i negatywnie wpływa na reputację naszego startupu.

Z każdą iteracją dowolnego modelu LLM widzieliśmy poprawę wydajności w zakresie minimalizacji halucynacji. Nawet z tą poprawą, my jako twórcy aplikacji i użytkownicy musimy pozostać świadomi tych ograniczeń.

### Szkodliwa Treść

Omówiliśmy w poprzedniej sekcji, kiedy LLM produkuje niepoprawne lub bezsensowne odpowiedzi. Innym ryzykiem, którego musimy być świadomi, jest sytuacja, gdy model odpowiada szkodliwą treścią.

Szkodliwa treść może być zdefiniowana jako:

- Dostarczanie instrukcji lub zachęcanie do samookaleczenia lub szkodzenia określonym grupom.
- Nienawistna lub poniżająca treść.
- Prowadzenie planowania jakiegokolwiek ataku lub aktów przemocy.
- Dostarczanie instrukcji, jak znaleźć nielegalne treści lub popełnić nielegalne czyny.
- Wyświetlanie treści o charakterze seksualnym.

Dla naszego startupu chcemy upewnić się, że mamy odpowiednie narzędzia i strategie, aby zapobiec temu rodzajowi treści przed jej zobaczeniem przez uczniów.

### Brak Uczciwości

Uczciwość jest definiowana jako "zapewnienie, że system SI jest wolny od uprzedzeń i dyskryminacji i że traktuje wszystkich sprawiedliwie i równo." W świecie Generatywnej SI chcemy zapewnić, że wykluczające światopoglądy marginalizowanych grup nie są wzmacniane przez rezultat modelu.

Tego typu rezultaty są nie tylko destrukcyjne dla budowania pozytywnych doświadczeń produktowych dla naszych użytkowników, ale także powodują dalsze szkody społeczne. Jako twórcy aplikacji powinniśmy zawsze mieć na uwadze szeroką i zróżnicowaną bazę użytkowników podczas budowania rozwiązań z Generatywną SI.

## Jak Odpowiedzialnie Korzystać z Generatywnej SI

Teraz, gdy zidentyfikowaliśmy znaczenie Odpowiedzialnej Generatywnej SI, przyjrzyjmy się 4 krokom, które możemy podjąć, aby odpowiedzialnie budować nasze rozwiązania SI:

![Cykl łagodzenia](../../images/mitigate-cycle.png?WT.mc_id=academic-105485-koreyst)

### Mierzenie Potencjalnych Szkód

W testowaniu oprogramowania testujemy oczekiwane działania użytkownika na aplikacji. Podobnie, testowanie różnorodnego zestawu promptów, których użytkownicy najprawdopodobniej będą używać, jest dobrym sposobem na mierzenie potencjalnych szkód.

Ponieważ nasz startup buduje produkt edukacyjny, dobrze byłoby przygotować listę promptów związanych z edukacją. Mogłoby to obejmować określony przedmiot, fakty historyczne i prompty dotyczące życia studenckiego.

### Łagodzenie Potencjalnych Szkód

Teraz czas znaleźć sposoby, w jakie możemy zapobiec lub ograniczyć potencjalne szkody spowodowane przez model i jego odpowiedzi. Możemy spojrzeć na to w 4 różnych warstwach:

![Warstwy łagodzenia](../../images/mitigation-layers.png?WT.mc_id=academic-105485-koreyst)

- **Model**. Wybór odpowiedniego modelu do odpowiedniego przypadku użycia. Większe i bardziej złożone modele, takie jak GPT-4, mogą powodować większe ryzyko szkodliwych treści, gdy są stosowane do mniejszych i bardziej specyficznych przypadków użycia. Używanie danych treningowych do dostrajania również zmniejsza ryzyko szkodliwych treści.

- **System Bezpieczeństwa**. System bezpieczeństwa to zestaw narzędzi i konfiguracji na platformie obsługującej model, które pomagają łagodzić szkody. Przykładem tego jest system filtrowania treści w usłudze Azure OpenAI. Systemy powinny również wykrywać ataki jailbreak i niepożądaną aktywność, taką jak żądania od botów.

- **Metaprompt**. Metaprompty i ugruntowanie są sposobami, w jakie możemy kierować lub ograniczać model na podstawie pewnych zachowań i informacji. Może to być używanie danych wejściowych systemu do definiowania pewnych ograniczeń modelu. Dodatkowo, dostarczanie rezultatów, które są bardziej odpowiednie dla zakresu lub domeny systemu.

Może to być również używanie technik takich jak Retrieval Augmented Generation (RAG), aby model pobierał informacje tylko z wyboru zaufanych źródeł. Jest lekcja później w tym kursie o [budowaniu aplikacji wyszukiwania](../../../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Doświadczenie Użytkownika**. Ostatnia warstwa to miejsce, gdzie użytkownik bezpośrednio wchodzi w interakcję z modelem poprzez interfejs naszej aplikacji w jakiś sposób. W ten sposób możemy zaprojektować UI/UX, aby ograniczyć użytkownika w zakresie rodzajów danych wejściowych, które mogą wysłać do modelu, a także tekstu lub obrazów wyświetlanych użytkownikowi. Podczas wdrażania aplikacji SI musimy również być przejrzyści co do tego, co nasza aplikacja Generatywnej SI może i czego nie może zrobić.

Mamy całą lekcję poświęconą [Projektowaniu UX dla Aplikacji SI](../../../12-designing-ux-for-ai-applications/translations/pl/README.md?WT.mc_id=academic-105485-koreyst)

- **Ocena modelu**. Praca z modelami LLM może być trudna, ponieważ nie zawsze mamy kontrolę nad danymi, na których model był trenowany. Niezależnie od tego, zawsze powinniśmy oceniać wydajność modelu i jego rezultaty. Nadal ważne jest mierzenie dokładności modelu, podobieństwa, ugruntowania i istotności rezultatu. Pomaga to zapewnić przejrzystość i zaufanie dla interesariuszy i użytkowników.

### Prowadzenie Odpowiedzialnego Rozwiązania Generatywnej SI

Budowanie praktyki operacyjnej wokół twoich aplikacji SI jest ostatnim etapem. Obejmuje to partnerstwo z innymi częściami naszego startupu, takimi jak Prawne i Bezpieczeństwo, aby zapewnić, że jesteśmy zgodni ze wszystkimi politykami regulacyjnymi. Przed uruchomieniem chcemy również budować plany dotyczące dostarczania, obsługi incydentów i wycofywania, aby zapobiec narastaniu szkód dla naszych użytkowników.

## Narzędzia

Chociaż praca nad rozwijaniem rozwiązań Odpowiedzialnej SI może wydawać się dużym wysiłkiem, jest to praca warta wysiłku. Wraz z rozwojem obszaru Generatywnej SI, będą dojrzewać narzędzia pomagające deweloperom efektywnie integrować odpowiedzialność w ich przepływach pracy. Na przykład, [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) może pomóc wykryć szkodliwe treści i obrazy poprzez żądanie API.

## Sprawdzenie wiedzy

O co musisz dbać, aby zapewnić odpowiedzialne korzystanie z SI?

1. Że odpowiedź jest poprawna.
1. Szkodliwe użytkowanie, że SI nie jest używana do celów przestępczych.
1. Zapewnienie, że SI jest wolna od uprzedzeń i dyskryminacji.

A: 2 i 3 są poprawne. Odpowiedzialna SI pomaga rozważyć, jak łagodzić szkodliwe efekty i uprzedzenia oraz więcej.

## 🚀 Wyzwanie

Przeczytaj więcej o [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) i zobacz, co możesz adoptować do swojego użytku.

## Świetna Praca, Kontynuuj Naukę

Po ukończeniu tej lekcji, sprawdź naszą [kolekcję materiałów do nauki Generatywnej SI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby kontynuować podnoszenie swojej wiedzy o Generatywnej SI!

Przejdź do Lekcji 4, gdzie przyjrzymy się [Podstawom Inżynierii Promptów](../../../04-prompt-engineering-fundamentals/translations/pl/README.md?WT.mc_id=academic-105485-koreyst)!
