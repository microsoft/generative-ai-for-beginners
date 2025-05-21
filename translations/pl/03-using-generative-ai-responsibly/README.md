<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-05-19T09:25:57+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "pl"
}
-->
# Odpowiedzialne Wykorzystanie Generatywnej AI

> _Kliknij powyższy obrazek, aby obejrzeć wideo tej lekcji_

Łatwo jest zafascynować się sztuczną inteligencją, a szczególnie generatywną AI, ale musisz zastanowić się, jak używać jej odpowiedzialnie. Trzeba rozważyć takie rzeczy, jak zapewnienie, że wyniki są sprawiedliwe, nie szkodzą i inne. Ten rozdział ma na celu dostarczenie kontekstu, co należy rozważyć i jak podjąć aktywne kroki, aby poprawić swoje korzystanie z AI.

## Wprowadzenie

Ta lekcja obejmie:

- Dlaczego powinieneś priorytetowo traktować Odpowiedzialną AI przy tworzeniu aplikacji Generatywnej AI.
- Główne zasady Odpowiedzialnej AI i jak odnoszą się one do Generatywnej AI.
- Jak wdrażać te zasady Odpowiedzialnej AI w praktyce poprzez strategie i narzędzia.

## Cele nauki

Po ukończeniu tej lekcji będziesz wiedzieć:

- Jak ważna jest Odpowiedzialna AI przy tworzeniu aplikacji Generatywnej AI.
- Kiedy myśleć i stosować główne zasady Odpowiedzialnej AI przy tworzeniu aplikacji Generatywnej AI.
- Jakie narzędzia i strategie są dostępne, aby wprowadzić koncepcję Odpowiedzialnej AI w życie.

## Zasady Odpowiedzialnej AI

Ekscytacja Generatywną AI nigdy nie była większa. Ta ekscytacja przyciągnęła wielu nowych deweloperów, uwagę i finansowanie do tej przestrzeni. Chociaż jest to bardzo pozytywne dla każdego, kto chce budować produkty i firmy z wykorzystaniem Generatywnej AI, ważne jest, aby postępować odpowiedzialnie.

W całym tym kursie skupiamy się na budowaniu naszego startupu i naszego produktu edukacyjnego AI. Użyjemy zasad Odpowiedzialnej AI: Sprawiedliwość, Włączanie, Niezawodność/Bezpieczeństwo, Bezpieczeństwo i Prywatność, Przejrzystość i Odpowiedzialność. Dzięki tym zasadom zbadamy, jak odnoszą się one do naszego wykorzystania Generatywnej AI w naszych produktach.

## Dlaczego Powinieneś Priorytetowo Traktować Odpowiedzialną AI

Podczas budowania produktu, podejście zorientowane na człowieka, które uwzględnia najlepsze interesy użytkownika, prowadzi do najlepszych wyników.

Unikalność Generatywnej AI polega na jej mocy tworzenia pomocnych odpowiedzi, informacji, wskazówek i treści dla użytkowników. Można to zrobić bez wielu ręcznych kroków, co może prowadzić do bardzo imponujących wyników. Bez odpowiedniego planowania i strategii, niestety, może to również prowadzić do szkodliwych wyników dla użytkowników, produktu i całego społeczeństwa.

Przyjrzyjmy się niektórym (choć nie wszystkim) z tych potencjalnie szkodliwych wyników:

### Halucynacje

Halucynacje to termin używany do opisania sytuacji, gdy LLM generuje treść, która jest całkowicie bezsensowna lub coś, co wiemy, że jest faktycznie błędne na podstawie innych źródeł informacji.

Weźmy na przykład, że budujemy funkcję dla naszego startupu, która pozwala studentom zadawać modelowi pytania historyczne. Student zadaje pytanie `Who was the sole survivor of Titanic?`

Model generuje odpowiedź taką jak poniżej:

To jest bardzo pewna siebie i szczegółowa odpowiedź. Niestety, jest nieprawidłowa. Nawet przy minimalnym badaniu można by odkryć, że więcej niż jedna osoba przeżyła katastrofę Titanica. Dla studenta, który dopiero zaczyna badać ten temat, ta odpowiedź może być na tyle przekonująca, że nie zostanie zakwestionowana i potraktowana jako fakt. Konsekwencje tego mogą prowadzić do tego, że system AI będzie niewiarygodny i negatywnie wpłynie na reputację naszego startupu.

Z każdą iteracją danego LLM widzimy poprawę wydajności w zakresie minimalizowania halucynacji. Nawet przy tej poprawie, jako twórcy aplikacji i użytkownicy, musimy być świadomi tych ograniczeń.

### Szkodliwe Treści

Omówiliśmy w poprzedniej sekcji, kiedy LLM generuje nieprawidłowe lub bezsensowne odpowiedzi. Innym ryzykiem, które musimy mieć na uwadze, jest sytuacja, gdy model odpowiada szkodliwymi treściami.

Szkodliwe treści można zdefiniować jako:

- Dostarczanie instrukcji lub zachęcanie do samookaleczeń lub krzywdzenia określonych grup.
- Treści nienawistne lub poniżające.
- Kierowanie planowaniem jakiegokolwiek rodzaju ataku lub aktów przemocy.
- Dostarczanie instrukcji, jak znaleźć nielegalne treści lub popełniać nielegalne czyny.
- Wyświetlanie treści o charakterze seksualnym.

Dla naszego startupu chcemy mieć pewność, że mamy odpowiednie narzędzia i strategie, aby zapobiec widoczności tego typu treści przez studentów.

### Brak Sprawiedliwości

Sprawiedliwość definiuje się jako "zapewnienie, że system AI jest wolny od uprzedzeń i dyskryminacji oraz że traktuje wszystkich sprawiedliwie i równo". W świecie Generatywnej AI chcemy upewnić się, że wykluczające światopoglądy marginalizowanych grup nie są wzmacniane przez output modelu.

Tego typu wyniki nie tylko niszczą pozytywne doświadczenia produktowe dla naszych użytkowników, ale także powodują dalsze szkody społeczne. Jako twórcy aplikacji powinniśmy zawsze mieć na uwadze szeroką i zróżnicowaną bazę użytkowników podczas budowania rozwiązań z Generatywną AI.

## Jak Odpowiedzialnie Wykorzystywać Generatywną AI

Teraz, gdy zidentyfikowaliśmy znaczenie Odpowiedzialnej Generatywnej AI, przyjrzyjmy się 4 krokom, które możemy podjąć, aby odpowiedzialnie budować nasze rozwiązania AI:

### Mierzenie Potencjalnych Szkód

W testowaniu oprogramowania testujemy oczekiwane działania użytkownika na aplikacji. Podobnie, testowanie różnorodnego zestawu podpowiedzi, których użytkownicy najprawdopodobniej użyją, jest dobrym sposobem na zmierzenie potencjalnych szkód.

Ponieważ nasz startup buduje produkt edukacyjny, dobrze byłoby przygotować listę podpowiedzi związanych z edukacją. Mogłoby to obejmować pewien przedmiot, fakty historyczne i podpowiedzi dotyczące życia studenckiego.

### Ograniczanie Potencjalnych Szkód

Teraz czas znaleźć sposoby, w jakie możemy zapobiec lub ograniczyć potencjalne szkody spowodowane przez model i jego odpowiedzi. Możemy na to spojrzeć w 4 różnych warstwach:

- **Model**. Wybór odpowiedniego modelu do odpowiedniego przypadku użycia. Większe i bardziej złożone modele, takie jak GPT-4, mogą powodować większe ryzyko szkodliwych treści, gdy są stosowane do mniejszych i bardziej specyficznych przypadków użycia. Używanie danych treningowych do dopasowania również zmniejsza ryzyko szkodliwych treści.

- **System Bezpieczeństwa**. System bezpieczeństwa to zestaw narzędzi i konfiguracji na platformie obsługującej model, które pomagają ograniczać szkody. Przykładem tego jest system filtrowania treści w usłudze Azure OpenAI. Systemy powinny również wykrywać ataki jailbreak i niepożądane działania, takie jak żądania od botów.

- **Metaprompt**. Metaprompt i uzasadnienie to sposoby, w jakie możemy kierować lub ograniczać model w oparciu o pewne zachowania i informacje. Mogłoby to polegać na używaniu danych wejściowych systemu do określenia pewnych ograniczeń modelu. Dodatkowo, dostarczanie wyników bardziej związanych z zakresem lub dziedziną systemu.

Może to również polegać na używaniu technik takich jak Retrieval Augmented Generation (RAG), aby model pobierał informacje tylko z wybranych zaufanych źródeł. Jest później w tym kursie lekcja dotycząca [budowania aplikacji wyszukiwania](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Doświadczenie Użytkownika**. Ostatnia warstwa to miejsce, gdzie użytkownik wchodzi w bezpośrednią interakcję z modelem poprzez interfejs naszej aplikacji w jakiś sposób. W ten sposób możemy zaprojektować UI/UX, aby ograniczyć użytkownika w typach danych wejściowych, które może wysłać do modelu, a także tekstów lub obrazów wyświetlanych użytkownikowi. Podczas wdrażania aplikacji AI musimy również być przejrzystymi na temat tego, co nasza aplikacja Generatywnej AI może i czego nie może zrobić.

Mamy całą lekcję poświęconą [Projektowaniu UX dla Aplikacji AI](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Ewaluacja modelu**. Praca z LLM może być wyzwaniem, ponieważ nie zawsze mamy kontrolę nad danymi, na których model był trenowany. Niemniej jednak, zawsze powinniśmy oceniać wydajność i wyniki modelu. Wciąż ważne jest mierzenie dokładności modelu, podobieństwa, uzasadnienia i trafności wyniku. To pomaga zapewnić przejrzystość i zaufanie dla interesariuszy i użytkowników.

### Operowanie Odpowiedzialnym Rozwiązaniem Generatywnej AI

Budowanie praktyki operacyjnej wokół aplikacji AI to ostatni etap. Obejmuje to współpracę z innymi częściami naszego startupu, takimi jak Dział Prawny i Bezpieczeństwa, aby upewnić się, że jesteśmy zgodni z wszystkimi politykami regulacyjnymi. Przed uruchomieniem chcemy również budować plany dotyczące dostarczania, obsługi incydentów i wycofywania, aby zapobiec jakimkolwiek szkodom dla naszych użytkowników.

## Narzędzia

Chociaż praca nad opracowaniem Odpowiedzialnych Rozwiązań AI może wydawać się trudna, jest to praca warta wysiłku. W miarę jak obszar Generatywnej AI rośnie, więcej narzędzi pomagających deweloperom efektywnie integrować odpowiedzialność w ich przepływy pracy będzie się rozwijać. Na przykład, [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) może pomóc w wykrywaniu szkodliwych treści i obrazów za pomocą żądania API.

## Sprawdzenie wiedzy

Na co musisz zwrócić uwagę, aby zapewnić odpowiedzialne użycie AI?

1. Że odpowiedź jest poprawna.
2. Szkodliwe użycie, że AI nie jest wykorzystywana do celów przestępczych.
3. Zapewnienie, że AI jest wolna od uprzedzeń i dyskryminacji.

Odpowiedź: 2 i 3 są poprawne. Odpowiedzialna AI pomaga rozważyć, jak łagodzić szkodliwe skutki i uprzedzenia oraz więcej.

## 🚀 Wyzwanie

Przeczytaj o [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) i zobacz, co możesz zaadaptować do swojego użycia.

## Świetna Robota, Kontynuuj Nauczanie

Po ukończeniu tej lekcji, sprawdź naszą [Kolekcję Nauki o Generatywnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby kontynuować podnoszenie swojej wiedzy na temat Generatywnej AI!

Przejdź do Lekcji 4, gdzie przyjrzymy się [Podstawom Inżynierii Podpowiedzi](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się o dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku istotnych informacji zaleca się profesjonalne tłumaczenie przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.