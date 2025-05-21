<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec385b41ee50579025d50cc03bfb3a25",
  "translation_date": "2025-05-19T21:57:34+00:00",
  "source_file": "12-designing-ux-for-ai-applications/README.md",
  "language_code": "da"
}
-->
# Design af UX til AI-applikationer

Brugeroplevelse er en meget vigtig del af at bygge apps. Brugerne skal kunne bruge din app på en effektiv måde for at udføre opgaver. At være effektiv er én ting, men du skal også designe apps, så de kan bruges af alle, for at gøre dem _tilgængelige_. Dette kapitel vil fokusere på dette område, så du forhåbentlig ender med at designe en app, som folk kan og vil bruge.

## Introduktion

Brugeroplevelse er, hvordan en bruger interagerer med og bruger et specifikt produkt eller en service, det være sig et system, værktøj eller design. Når man udvikler AI-applikationer, fokuserer udviklere ikke kun på at sikre, at brugeroplevelsen er effektiv, men også etisk. I denne lektion dækker vi, hvordan man bygger kunstige intelligens (AI) applikationer, der imødekommer brugerbehov.

Lektion vil dække følgende områder:

- Introduktion til brugeroplevelse og forståelse af brugerbehov
- Design af AI-applikationer til tillid og gennemsigtighed
- Design af AI-applikationer til samarbejde og feedback

## Læringsmål

Efter at have taget denne lektion, vil du være i stand til at:

- Forstå, hvordan man bygger AI-applikationer, der opfylder brugerens behov.
- Designe AI-applikationer, der fremmer tillid og samarbejde.

### Forudsætning

Tag dig tid til at læse mere om [brugeroplevelse og design tænkning.](https://learn.microsoft.com/training/modules/ux-design?WT.mc_id=academic-105485-koreyst)

## Introduktion til brugeroplevelse og forståelse af brugerbehov

I vores fiktive uddannelses-startup har vi to primære brugere, lærere og studerende. Hver af de to brugere har unikke behov. Et brugervenligt design prioriterer brugeren og sikrer, at produkterne er relevante og gavnlige for dem, de er beregnet til.

Applikationen bør være **nyttig, pålidelig, tilgængelig og behagelig** for at give en god brugeroplevelse.

### Brugervenlighed

At være nyttig betyder, at applikationen har funktionalitet, der matcher dens tilsigtede formål, såsom at automatisere karaktergivningsprocessen eller generere flashcards til repetition. En applikation, der automatiserer karaktergivningsprocessen, skal kunne tildele karakterer til elevernes arbejde præcist og effektivt baseret på foruddefinerede kriterier. Tilsvarende bør en applikation, der genererer repetitions-flashcards, kunne skabe relevante og varierede spørgsmål baseret på dens data.

### Pålidelighed

At være pålidelig betyder, at applikationen kan udføre sin opgave konsekvent og uden fejl. Dog er AI ligesom mennesker ikke perfekt og kan være tilbøjelig til fejl. Applikationerne kan støde på fejl eller uventede situationer, der kræver menneskelig indgriben eller korrektion. Hvordan håndterer du fejl? I sidste del af denne lektion vil vi dække, hvordan AI-systemer og applikationer er designet til samarbejde og feedback.

### Tilgængelighed

At være tilgængelig betyder at udvide brugeroplevelsen til brugere med forskellige evner, herunder dem med handicap, og sikre, at ingen bliver udeladt. Ved at følge tilgængelighedsprincipper og retningslinjer bliver AI-løsninger mere inkluderende, brugbare og gavnlige for alle brugere.

### Behagelig

At være behagelig betyder, at applikationen er fornøjelig at bruge. En tiltalende brugeroplevelse kan have en positiv indvirkning på brugeren, opmuntre dem til at vende tilbage til applikationen og øge virksomhedens indtægter.

Ikke alle udfordringer kan løses med AI. AI kommer ind for at forbedre din brugeroplevelse, det være sig ved at automatisere manuelle opgaver eller personalisere brugeroplevelser.

## Design af AI-applikationer til tillid og gennemsigtighed

Opbygning af tillid er afgørende, når man designer AI-applikationer. Tillid sikrer, at en bruger er sikker på, at applikationen vil udføre arbejdet, levere resultater konsekvent, og at resultaterne er, hvad brugeren har brug for. En risiko i dette område er mistillid og overtro. Mistillid opstår, når en bruger har lidt eller ingen tillid til et AI-system, hvilket fører til, at brugeren afviser din applikation. Overtro opstår, når en bruger overvurderer et AI-systems kapacitet, hvilket fører til, at brugerne stoler for meget på AI-systemet. For eksempel kan et automatiseret karaktergivningssystem i tilfælde af overtro føre til, at læreren ikke gennemgår nogle af opgaverne for at sikre, at karaktergivningssystemet fungerer godt. Dette kan resultere i uretfærdige eller unøjagtige karakterer for eleverne eller mistede muligheder for feedback og forbedring.

To måder at sikre, at tillid er centralt i designet, er forklarbarhed og kontrol.

### Forklarbarhed

Når AI hjælper med at informere beslutninger, såsom at give viden til kommende generationer, er det afgørende for lærere og forældre at forstå, hvordan AI-beslutninger træffes. Dette er forklarbarhed - forståelse af, hvordan AI-applikationer træffer beslutninger. Design for forklarbarhed inkluderer at tilføje detaljer om eksempler på, hvad en AI-applikation kan gøre. For eksempel, i stedet for "Kom i gang med AI-lærer", kan systemet bruge: "Opsummer dine noter for lettere repetition ved hjælp af AI."

Et andet eksempel er, hvordan AI bruger bruger- og persondata. For eksempel kan en bruger med personaen student have begrænsninger baseret på deres persona. AI'en kan måske ikke afsløre svarene på spørgsmålene, men kan hjælpe med at guide brugeren til at tænke over, hvordan de kan løse et problem.

En sidste nøgle del af forklarbarhed er forenkling af forklaringer. Elever og lærere er måske ikke AI-eksperter, derfor bør forklaringerne på, hvad applikationen kan eller ikke kan gøre, forenkles og være lette at forstå.

### Kontrol

Generativ AI skaber et samarbejde mellem AI og brugeren, hvor en bruger for eksempel kan ændre prompts for forskellige resultater. Derudover, når et output er genereret, bør brugerne kunne ændre resultaterne og give dem en følelse af kontrol. For eksempel, når du bruger Bing, kan du tilpasse din prompt baseret på format, tone og længde. Derudover kan du tilføje ændringer til dit output og ændre output som vist nedenfor:

En anden funktion i Bing, der giver en bruger kontrol over applikationen, er evnen til at vælge at deltage eller fravælge de data, AI bruger. For en skoleapplikation kan en elev måske bruge deres noter samt lærerens ressourcer som repetitionsmateriale.

> Når man designer AI-applikationer, er intentionen nøglen til at sikre, at brugerne ikke overtror og sætter urealistiske forventninger til dens kapacitet. En måde at gøre dette på er ved at skabe friktion mellem prompts og resultater. Mind brugeren om, at dette er AI og ikke et andet menneske

## Design af AI-applikationer til samarbejde og feedback

Som tidligere nævnt skaber generativ AI et samarbejde mellem brugeren og AI. De fleste interaktioner er med en bruger, der indtaster en prompt, og AI genererer et output. Hvad hvis outputtet er forkert? Hvordan håndterer applikationen fejl, hvis de opstår? Skylder AI brugeren, eller tager det tid til at forklare fejlen?

AI-applikationer bør være bygget til at modtage og give feedback. Dette hjælper ikke kun AI-systemet med at forbedre sig, men opbygger også tillid hos brugerne. En feedback-loop bør inkluderes i designet, et eksempel kan være en simpel tommelfinger op eller ned på outputtet.

En anden måde at håndtere dette på er at kommunikere systemets kapaciteter og begrænsninger klart. Når en bruger laver en fejl ved at anmode om noget ud over AI's kapaciteter, bør der også være en måde at håndtere dette på, som vist nedenfor.

Systemfejl er almindelige med applikationer, hvor brugeren måske har brug for hjælp med information uden for AI's omfang, eller applikationen kan have en grænse for, hvor mange spørgsmål/emner en bruger kan generere resuméer af. For eksempel kan en AI-applikation trænet med data om begrænsede emner, for eksempel historie og matematik, måske ikke kunne håndtere spørgsmål om geografi. For at afhjælpe dette kan AI-systemet give et svar som: "Beklager, vores produkt er blevet trænet med data i følgende emner....., jeg kan ikke svare på det spørgsmål, du stillede."

AI-applikationer er ikke perfekte, derfor er de tilbøjelige til at lave fejl. Når du designer dine applikationer, bør du sikre, at du skaber plads til feedback fra brugere og fejlbehandling på en måde, der er enkel og let at forklare.

## Opgave

Tag de AI-apps, du har bygget indtil nu, og overvej at implementere nedenstående trin i din app:

- **Behagelig:** Overvej, hvordan du kan gøre din app mere behagelig. Tilføjer du forklaringer overalt? Opmuntre du brugeren til at udforske? Hvordan formulerer du dine fejlmeddelelser?

- **Brugervenlighed:** Byg en webapp. Sørg for, at din app kan navigeres med både mus og tastatur.

- **Tillid og gennemsigtighed:** Stol ikke fuldt ud på AI og dens output, overvej hvordan du ville tilføje et menneske til processen for at verificere outputtet. Overvej også og implementer andre måder at opnå tillid og gennemsigtighed.

- **Kontrol:** Giv brugeren kontrol over de data, de giver til applikationen. Implementer en måde, hvorpå en bruger kan vælge at deltage eller fravælge dataindsamling i AI-applikationen.

## Fortsæt din læring!

Efter at have gennemført denne lektion, tjek vores [Generativ AI læringssamling](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at opgradere din viden om generativ AI!

Gå videre til Lektion 13, hvor vi vil se på, hvordan man [sikrer AI-applikationer](../13-securing-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Mens vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.