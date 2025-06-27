<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec385b41ee50579025d50cc03bfb3a25",
  "translation_date": "2025-06-25T20:25:01+00:00",
  "source_file": "12-designing-ux-for-ai-applications/README.md",
  "language_code": "da"
}
-->
# Design af UX til AI-applikationer

> _(Klik på billedet ovenfor for at se videoen af denne lektion)_

Brugeroplevelse er en meget vigtig del af at bygge apps. Brugere skal kunne bruge din app effektivt til at udføre opgaver. At være effektiv er én ting, men du skal også designe apps, så de kan bruges af alle, for at gøre dem _tilgængelige_. Dette kapitel vil fokusere på dette område, så du forhåbentlig ender med at designe en app, som folk kan og vil bruge.

## Introduktion

Brugeroplevelse er, hvordan en bruger interagerer med og bruger et specifikt produkt eller tjeneste, hvad enten det er et system, værktøj eller design. Når man udvikler AI-applikationer, fokuserer udviklere ikke kun på at sikre, at brugeroplevelsen er effektiv, men også etisk. I denne lektion dækker vi, hvordan man bygger kunstige intelligens (AI) applikationer, der imødekommer brugerbehov.

Lektien vil dække følgende områder:

- Introduktion til brugeroplevelse og forståelse af brugerbehov
- Design af AI-applikationer for tillid og gennemsigtighed
- Design af AI-applikationer for samarbejde og feedback

## Læringsmål

Efter at have taget denne lektion, vil du kunne:

- Forstå, hvordan man bygger AI-applikationer, der imødekommer brugerbehov.
- Designe AI-applikationer, der fremmer tillid og samarbejde.

### Forudsætning

Tag dig tid og læs mere om [brugeroplevelse og design tænkning.](https://learn.microsoft.com/training/modules/ux-design?WT.mc_id=academic-105485-koreyst)

## Introduktion til brugeroplevelse og forståelse af brugerbehov

I vores fiktive uddannelsesstartup har vi to primære brugere, lærere og elever. Hver af de to brugere har unikke behov. Et brugercentreret design prioriterer brugeren og sikrer, at produkterne er relevante og gavnlige for dem, det er beregnet til.

Applikationen bør være **nyttig, pålidelig, tilgængelig og behagelig** for at give en god brugeroplevelse.

### Brugervenlighed

At være nyttig betyder, at applikationen har funktionalitet, der matcher dens tilsigtede formål, såsom at automatisere bedømmelsesprocessen eller generere flashcards til repetition. En applikation, der automatiserer bedømmelsesprocessen, bør kunne tildele karakterer til elevernes arbejde præcist og effektivt baseret på foruddefinerede kriterier. På samme måde bør en applikation, der genererer repetitionsflashcards, kunne skabe relevante og varierede spørgsmål baseret på dens data.

### Pålidelighed

At være pålidelig betyder, at applikationen kan udføre sin opgave konsekvent og uden fejl. Men AI, ligesom mennesker, er ikke perfekt og kan være tilbøjelig til fejl. Applikationerne kan støde på fejl eller uventede situationer, der kræver menneskelig indgriben eller korrektion. Hvordan håndterer du fejl? I den sidste del af denne lektion vil vi dække, hvordan AI-systemer og applikationer er designet til samarbejde og feedback.

### Tilgængelighed

At være tilgængelig betyder at udvide brugeroplevelsen til brugere med forskellige evner, herunder dem med handicap, og sikre, at ingen bliver udeladt. Ved at følge tilgængelighedsguidelines og principper bliver AI-løsninger mere inkluderende, brugbare og gavnlige for alle brugere.

### Behagelig

At være behagelig betyder, at applikationen er fornøjelig at bruge. En tiltalende brugeroplevelse kan have en positiv indflydelse på brugeren, opmuntre dem til at vende tilbage til applikationen og øge forretningsindtægten.

Ikke alle udfordringer kan løses med AI. AI kommer ind for at forbedre din brugeroplevelse, hvad enten det er at automatisere manuelle opgaver eller personalisere brugeroplevelser.

## Design af AI-applikationer for tillid og gennemsigtighed

At opbygge tillid er afgørende, når man designer AI-applikationer. Tillid sikrer, at en bruger er sikker på, at applikationen vil få arbejdet gjort, levere resultater konsekvent, og at resultaterne er, hvad brugeren har brug for. En risiko på dette område er mistillid og overtillid. Mistillid opstår, når en bruger har lidt eller ingen tillid til et AI-system, hvilket fører til, at brugeren afviser din applikation. Overtillid opstår, når en bruger overvurderer kapaciteten af et AI-system, hvilket fører til, at brugerne stoler for meget på AI-systemet. For eksempel kan et automatiseret bedømmelsessystem i tilfælde af overtillid føre til, at læreren ikke korrekturlæser nogle af papirerne for at sikre, at bedømmelsessystemet fungerer godt. Dette kunne resultere i uretfærdige eller unøjagtige karakterer for eleverne eller mistede muligheder for feedback og forbedring.

To måder at sikre, at tillid er placeret i centrum af designet, er forklarbarhed og kontrol.

### Forklarbarhed

Når AI hjælper med at informere beslutninger, såsom at videregive viden til fremtidige generationer, er det afgørende for lærere og forældre at forstå, hvordan AI-beslutninger træffes. Dette er forklarbarhed - forståelse af, hvordan AI-applikationer træffer beslutninger. Design for forklarbarhed inkluderer at tilføje detaljer om eksempler på, hvad en AI-applikation kan gøre. For eksempel, i stedet for "Kom i gang med AI-lærer", kan systemet bruge: "Opsummer dine noter for lettere repetition ved hjælp af AI."

Et andet eksempel er, hvordan AI bruger bruger- og personlige data. For eksempel kan en bruger med personaen elev have begrænsninger baseret på deres persona. AI'en kan ikke være i stand til at afsløre svar på spørgsmål, men kan hjælpe med at guide brugeren til at tænke over, hvordan de kan løse et problem.

En sidste vigtig del af forklarbarhed er forenkling af forklaringer. Elever og lærere er måske ikke AI-eksperter, derfor bør forklaringer på, hvad applikationen kan eller ikke kan gøre, være forenklede og lette at forstå.

### Kontrol

Generativ AI skaber et samarbejde mellem AI og brugeren, hvor en bruger for eksempel kan ændre prompts for forskellige resultater. Derudover, når en output er genereret, bør brugerne kunne ændre resultaterne og give dem en følelse af kontrol. For eksempel, når du bruger Bing, kan du tilpasse din prompt baseret på format, tone og længde. Derudover kan du tilføje ændringer til din output og ændre output som vist nedenfor:

En anden funktion i Bing, der giver en bruger kontrol over applikationen, er evnen til at vælge ind og ud af de data, AI bruger. For en skoleapplikation kan en elev ønske at bruge deres noter såvel som lærerens ressourcer som repetitionsmateriale.

> Når du designer AI-applikationer, er intentionalitet nøglen til at sikre, at brugere ikke overtrust sætter urealistiske forventninger til dens kapaciteter. En måde at gøre dette på er ved at skabe friktion mellem prompts og resultater. Påmind brugeren om, at dette er AI og ikke et medmenneske.

## Design af AI-applikationer for samarbejde og feedback

Som tidligere nævnt skaber generativ AI et samarbejde mellem brugeren og AI. De fleste engagementer er med en bruger, der indtaster en prompt, og AI genererer en output. Hvad hvis output er forkert? Hvordan håndterer applikationen fejl, hvis de opstår? Skylder AI brugeren eller tager sig tid til at forklare fejlen?

AI-applikationer bør være bygget til at modtage og give feedback. Dette hjælper ikke kun AI-systemet med at forbedre sig, men bygger også tillid med brugerne. En feedbackloop bør inkluderes i designet, et eksempel kan være en simpel tommelfinger op eller ned på output.

En anden måde at håndtere dette på er at kommunikere systemets kapaciteter og begrænsninger tydeligt. Når en bruger laver en fejl ved at anmode om noget ud over AI-kapaciteterne, bør der også være en måde at håndtere dette på, som vist nedenfor.

Systemfejl er almindelige med applikationer, hvor brugeren måske har brug for hjælp med information uden for AI's rækkevidde, eller applikationen kan have en grænse for, hvor mange spørgsmål/emner en bruger kan generere opsummeringer. For eksempel, en AI-applikation trænet med data på begrænsede emner, for eksempel historie og matematik, kan ikke være i stand til at håndtere spørgsmål omkring geografi. For at afbøde dette kan AI-systemet give et svar som: "Beklager, vores produkt er blevet trænet med data i følgende emner....., jeg kan ikke være i stand til at svare på det spørgsmål, du stillede."

AI-applikationer er ikke perfekte, derfor er de tilbøjelige til at lave fejl. Når du designer dine applikationer, bør du sikre, at du skaber plads til feedback fra brugere og fejlbehandling på en måde, der er enkel og let forklarelig.

## Opgave

Tag eventuelle AI-apps, du har bygget indtil nu, og overvej at implementere nedenstående trin i din app:

- **Behagelig:** Overvej hvordan du kan gøre din app mere behagelig. Tilføjer du forklaringer overalt? Opmuntrer du brugeren til at udforske? Hvordan formulerer du dine fejlmeddelelser?

- **Brugervenlighed:** Byg en webapp. Sørg for, at din app kan navigeres både med mus og tastatur.

- **Tillid og gennemsigtighed:** Stol ikke helt på AI og dens output, overvej hvordan du ville tilføje et menneske til processen for at verificere output. Overvej også og implementer andre måder at opnå tillid og gennemsigtighed.

- **Kontrol:** Giv brugeren kontrol over de data, de leverer til applikationen. Implementer en måde, hvorpå en bruger kan vælge ind og ud af datainnsamling i AI-applikationen.

## Fortsæt din læring!

Efter at have gennemført denne lektion, tjek vores [Generativ AI læringssamling](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at opgradere din viden om generativ AI!

Gå videre til lektion 13, hvor vi vil se på, hvordan man [sikrer AI-applikationer](../13-securing-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.