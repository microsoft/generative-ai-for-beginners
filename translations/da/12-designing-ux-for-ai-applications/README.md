<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "78bbeed50fd4dc9fdee931f5daf98cb3",
  "translation_date": "2025-10-17T19:08:19+00:00",
  "source_file": "12-designing-ux-for-ai-applications/README.md",
  "language_code": "da"
}
-->
# Design af UX til AI-applikationer

[![Design af UX til AI-applikationer](../../../translated_images/12-lesson-banner.c53c3c7c802e8f563953ce388f6a987ca493472c724d924b060be470951c53c8.da.png)](https://youtu.be/VKbCejSICA8?si=MKj7GQYHfXRZyWW6)

> _(Klik på billedet ovenfor for at se videoen til denne lektion)_

Brugeroplevelse er en meget vigtig del af at bygge apps. Brugere skal kunne bruge din app på en effektiv måde for at udføre opgaver. Effektivitet er én ting, men du skal også designe apps, så de kan bruges af alle og dermed gøre dem _tilgængelige_. Dette kapitel vil fokusere på dette område, så du forhåbentlig ender med at designe en app, som folk kan og vil bruge.

## Introduktion

Brugeroplevelse handler om, hvordan en bruger interagerer med og anvender et specifikt produkt eller en tjeneste, hvad enten det er et system, værktøj eller design. Når man udvikler AI-applikationer, fokuserer udviklere ikke kun på at sikre, at brugeroplevelsen er effektiv, men også etisk. I denne lektion dækker vi, hvordan man bygger kunstige intelligens (AI) applikationer, der opfylder brugerens behov.

Lektionens indhold vil omfatte følgende områder:

- Introduktion til brugeroplevelse og forståelse af brugerens behov
- Design af AI-applikationer med fokus på tillid og gennemsigtighed
- Design af AI-applikationer med fokus på samarbejde og feedback

## Læringsmål

Efter denne lektion vil du kunne:

- Forstå, hvordan man bygger AI-applikationer, der opfylder brugerens behov.
- Designe AI-applikationer, der fremmer tillid og samarbejde.

### Forudsætning

Tag dig tid til at læse mere om [brugeroplevelse og design thinking.](https://learn.microsoft.com/training/modules/ux-design?WT.mc_id=academic-105485-koreyst)

## Introduktion til brugeroplevelse og forståelse af brugerens behov

I vores fiktive uddannelses-startup har vi to primære brugere, lærere og elever. Hver af de to brugere har unikke behov. Et brugercentreret design prioriterer brugeren og sikrer, at produkterne er relevante og gavnlige for dem, de er beregnet til.

Applikationen bør være **nyttig, pålidelig, tilgængelig og behagelig** for at give en god brugeroplevelse.

### Brugervenlighed

At være nyttig betyder, at applikationen har funktionalitet, der matcher dens tilsigtede formål, såsom at automatisere bedømmelsesprocessen eller generere flashcards til repetition. En applikation, der automatiserer bedømmelsesprocessen, bør kunne tildele karakterer til elevernes arbejde nøjagtigt og effektivt baseret på foruddefinerede kriterier. Tilsvarende bør en applikation, der genererer repetitions-flashcards, kunne skabe relevante og varierede spørgsmål baseret på dens data.

### Pålidelighed

At være pålidelig betyder, at applikationen kan udføre sin opgave konsekvent og uden fejl. Men AI, ligesom mennesker, er ikke perfekt og kan være tilbøjelig til fejl. Applikationerne kan støde på fejl eller uventede situationer, der kræver menneskelig indgriben eller korrektion. Hvordan håndterer du fejl? I den sidste del af denne lektion vil vi dække, hvordan AI-systemer og applikationer designes til samarbejde og feedback.

### Tilgængelighed

At være tilgængelig betyder at udvide brugeroplevelsen til brugere med forskellige evner, herunder dem med handicap, og sikre, at ingen bliver udeladt. Ved at følge retningslinjer og principper for tilgængelighed bliver AI-løsninger mere inkluderende, brugbare og gavnlige for alle brugere.

### Behagelig

At være behagelig betyder, at applikationen er fornøjelig at bruge. En tiltalende brugeroplevelse kan have en positiv indvirkning på brugeren, opmuntre dem til at vende tilbage til applikationen og øge virksomhedens indtægter.

![billede der illustrerer UX-overvejelser i AI](../../../translated_images/uxinai.d5b4ed690f5cefff0c53ffcc01b480cdc1828402e1fdbc980490013a3c50935a.da.png)

Ikke alle udfordringer kan løses med AI. AI kommer ind for at supplere din brugeroplevelse, hvad enten det er ved at automatisere manuelle opgaver eller personalisere brugeroplevelser.

## Design af AI-applikationer med fokus på tillid og gennemsigtighed

At opbygge tillid er afgørende, når man designer AI-applikationer. Tillid sikrer, at en bruger er sikker på, at applikationen vil udføre arbejdet, levere resultater konsekvent, og at resultaterne er, hvad brugeren har brug for. En risiko på dette område er mistillid og overdrevet tillid. Mistillid opstår, når en bruger har lidt eller ingen tillid til et AI-system, hvilket fører til, at brugeren afviser din applikation. Overdrevet tillid opstår, når en bruger overvurderer et AI-systems kapacitet, hvilket fører til, at brugeren stoler for meget på AI-systemet. For eksempel kan et automatiseret bedømmelsessystem i tilfælde af overdrevet tillid føre til, at læreren ikke gennemgår nogle af opgaverne for at sikre, at bedømmelsessystemet fungerer korrekt. Dette kan resultere i uretfærdige eller unøjagtige karakterer for eleverne eller mistede muligheder for feedback og forbedring.

To måder at sikre, at tillid er centralt i designet, er forklarbarhed og kontrol.

### Forklarbarhed

Når AI hjælper med at informere beslutninger, såsom at formidle viden til fremtidige generationer, er det afgørende for lærere og forældre at forstå, hvordan AI-beslutninger træffes. Dette er forklarbarhed - forståelse af, hvordan AI-applikationer træffer beslutninger. Design for forklarbarhed inkluderer at tilføje detaljer, der fremhæver, hvordan AI nåede frem til outputtet. Publikum skal være opmærksom på, at outputtet er genereret af AI og ikke af et menneske. For eksempel, i stedet for at sige "Start med at chatte med din tutor nu", sig "Brug AI-tutor, der tilpasser sig dine behov og hjælper dig med at lære i dit eget tempo."

![en app landingsside med klar illustration af forklarbarhed i AI-applikationer](../../../translated_images/explanability-in-ai.134426a96b498fbfdc80c75ae0090aedc0fc97424ae0734fccf7fb00a59a20d9.da.png)

Et andet eksempel er, hvordan AI bruger bruger- og persondata. For eksempel kan en bruger med personaen elev have begrænsninger baseret på deres persona. AI kan muligvis ikke afsløre svar på spørgsmål, men kan hjælpe med at guide brugeren til at tænke over, hvordan de kan løse et problem.

![AI svarer på spørgsmål baseret på persona](../../../translated_images/solving-questions.b7dea1604de0cbd2e9c5fa00b1a68a0ed77178a035b94b9213196b9d125d0be8.da.png)

En sidste vigtig del af forklarbarhed er forenkling af forklaringer. Elever og lærere er måske ikke AI-eksperter, derfor bør forklaringer på, hvad applikationen kan eller ikke kan gøre, være enkle og lette at forstå.

![forenklede forklaringer på AI-kapaciteter](../../../translated_images/simplified-explanations.4679508a406c3621fa22bad4673e717fbff02f8b8d58afcab8cb6f1aa893a82f.da.png)

### Kontrol

Generativ AI skaber et samarbejde mellem AI og brugeren, hvor en bruger for eksempel kan ændre prompts for forskellige resultater. Derudover, når et output er genereret, bør brugere kunne ændre resultaterne, hvilket giver dem en følelse af kontrol. For eksempel, når man bruger Bing, kan du tilpasse din prompt baseret på format, tone og længde. Derudover kan du tilføje ændringer til dit output og modificere resultatet som vist nedenfor:

![Bing søgeresultater med muligheder for at ændre prompt og output](../../../translated_images/bing1.293ae8527dbe2789b675c8591c9fb3cb1aa2ada75c2877f9aa9edc059f7a8b1c.da.png)

En anden funktion i Bing, der giver en bruger kontrol over applikationen, er muligheden for at vælge til og fra i forhold til de data, AI bruger. For en skoleapplikation kan en elev ønske at bruge sine noter såvel som lærerens ressourcer som repetitionsmateriale.

![Bing søgeresultater med muligheder for at ændre prompt og output](../../../translated_images/bing2.309f4845528a88c28c1c9739fb61d91fd993dc35ebe6fc92c66791fb04fceb4d.da.png)

> Når man designer AI-applikationer, er det vigtigt at være intentionel for at sikre, at brugere ikke overtror og sætter urealistiske forventninger til dens kapaciteter. En måde at gøre dette på er ved at skabe friktion mellem prompts og resultater. Mind brugeren om, at dette er AI og ikke et andet menneske.

## Design af AI-applikationer med fokus på samarbejde og feedback

Som tidligere nævnt skaber generativ AI et samarbejde mellem brugeren og AI. De fleste interaktioner sker ved, at en bruger indtaster en prompt, og AI genererer et output. Hvad hvis outputtet er forkert? Hvordan håndterer applikationen fejl, hvis de opstår? Skylder AI skylden på brugeren, eller tager den sig tid til at forklare fejlen?

AI-applikationer bør bygges til at modtage og give feedback. Dette hjælper ikke kun AI-systemet med at forbedre sig, men opbygger også tillid hos brugerne. En feedback-loop bør inkluderes i designet, et eksempel kan være en simpel tommelfinger op eller ned på outputtet.

En anden måde at håndtere dette på er at kommunikere systemets kapaciteter og begrænsninger tydeligt. Når en bruger laver en fejl ved at anmode om noget, der ligger uden for AI's kapaciteter, bør der også være en måde at håndtere dette på, som vist nedenfor.

![Giv feedback og håndter fejl](../../../translated_images/feedback-loops.7955c134429a94663443ad74d59044f8dc4ce354577f5b79b4bd2533f2cafc6f.da.png)

Systemfejl er almindelige med applikationer, hvor brugeren måske har brug for hjælp med information uden for AI's rækkevidde, eller applikationen kan have en grænse for, hvor mange spørgsmål/emner en bruger kan generere resuméer af. For eksempel kan en AI-applikation, der er trænet med data om begrænsede emner, for eksempel Historie og Matematik, muligvis ikke håndtere spørgsmål om Geografi. For at afhjælpe dette kan AI-systemet give et svar som: "Beklager, vores produkt er blevet trænet med data inden for følgende emner....., jeg kan ikke svare på det spørgsmål, du stillede."

AI-applikationer er ikke perfekte, og derfor er de tilbøjelige til at lave fejl. Når du designer dine applikationer, bør du sikre, at du skaber plads til feedback fra brugere og fejlbehandling på en måde, der er enkel og let at forklare.

## Opgave

Tag enhver AI-app, du har bygget indtil videre, og overvej at implementere nedenstående trin i din app:

- **Behagelig:** Overvej, hvordan du kan gøre din app mere behagelig. Tilføjer du forklaringer overalt? Opmuntrer du brugeren til at udforske? Hvordan formulerer du dine fejlmeddelelser?

- **Brugervenlighed:** Byg en webapp. Sørg for, at din app kan navigeres med både mus og tastatur.

- **Tillid og gennemsigtighed:** Stol ikke fuldstændigt på AI og dens output, overvej hvordan du kan tilføje et menneske til processen for at verificere outputtet. Overvej også og implementer andre måder at opnå tillid og gennemsigtighed.

- **Kontrol:** Giv brugeren kontrol over de data, de giver til applikationen. Implementer en måde, hvorpå en bruger kan vælge til og fra i forhold til dataindsamling i AI-applikationen.

<!-- ## [Post-lecture quiz](../../../12-designing-ux-for-ai-applications/quiz-url) -->

## Fortsæt din læring!

Efter at have gennemført denne lektion, kan du tjekke vores [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at opbygge din viden om generativ AI!

Gå videre til Lektion 13, hvor vi vil se på, hvordan man [sikrer AI-applikationer](../13-securing-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.