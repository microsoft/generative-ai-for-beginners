<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-05-19T14:41:48+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "da"
}
-->
# Brug af Generativ AI Ansvarligt

> _Klik på billedet ovenfor for at se videoen af denne lektion_

Det er nemt at blive fascineret af AI og især generativ AI, men du skal overveje, hvordan du bruger det ansvarligt. Du skal tænke over, hvordan du sikrer, at outputtet er retfærdigt, ikke-skadeligt og mere. Dette kapitel har til formål at give dig den nævnte kontekst, hvad du skal overveje, og hvordan du kan tage aktive skridt til at forbedre din AI-brug.

## Introduktion

Denne lektion vil dække:

- Hvorfor du skal prioritere Ansvarlig AI, når du bygger Generative AI-applikationer.
- Kerneprincipper for Ansvarlig AI og hvordan de relaterer sig til Generative AI.
- Hvordan man omsætter disse Ansvarlige AI-principper i praksis gennem strategi og værktøjer.

## Læringsmål

Efter at have gennemført denne lektion vil du vide:

- Vigtigheden af Ansvarlig AI, når du bygger Generative AI-applikationer.
- Hvornår man skal tænke og anvende kerneprincipperne for Ansvarlig AI, når man bygger Generative AI-applikationer.
- Hvilke værktøjer og strategier der er tilgængelige for dig til at omsætte konceptet for Ansvarlig AI i praksis.

## Ansvarlige AI-principper

Spændingen ved Generativ AI har aldrig været højere. Denne spænding har bragt mange nye udviklere, opmærksomhed og finansiering til dette område. Selvom dette er meget positivt for enhver, der ønsker at bygge produkter og virksomheder ved hjælp af Generativ AI, er det også vigtigt, at vi fortsætter ansvarligt.

Gennem dette kursus fokuserer vi på at bygge vores startup og vores AI-uddannelsesprodukt. Vi vil bruge principperne for Ansvarlig AI: Retfærdighed, Inklusivitet, Pålidelighed/Sikkerhed, Sikkerhed & Privatliv, Gennemsigtighed og Ansvarlighed. Med disse principper vil vi udforske, hvordan de relaterer sig til vores brug af Generativ AI i vores produkter.

## Hvorfor Skal Du Prioritere Ansvarlig AI

Når du bygger et produkt, fører en menneskecentreret tilgang ved at have din brugers bedste interesse i tankerne til de bedste resultater.

Det unikke ved Generativ AI er dens evne til at skabe nyttige svar, information, vejledning og indhold til brugerne. Dette kan gøres uden mange manuelle trin, hvilket kan føre til meget imponerende resultater. Uden ordentlig planlægning og strategier kan det desværre også føre til nogle skadelige resultater for dine brugere, dit produkt og samfundet som helhed.

Lad os se på nogle (men ikke alle) af disse potentielt skadelige resultater:

### Hallucinationer

Hallucinationer er et udtryk, der bruges til at beskrive, når en LLM producerer indhold, der enten er fuldstændig meningsløst eller noget, vi ved er faktuelt forkert baseret på andre informationskilder.

Lad os tage et eksempel, hvor vi bygger en funktion til vores startup, der giver elever mulighed for at stille historiske spørgsmål til en model. En elev stiller spørgsmålet `Who was the sole survivor of Titanic?`

Modellen producerer et svar som det nedenfor:

Dette er et meget selvsikkert og grundigt svar. Desværre er det forkert. Selv med en minimal mængde forskning ville man opdage, at der var mere end én overlevende fra Titanic-katastrofen. For en elev, der lige er begyndt at undersøge dette emne, kan dette svar være overbevisende nok til ikke at blive stillet spørgsmålstegn ved og behandlet som en kendsgerning. Konsekvenserne af dette kan føre til, at AI-systemet er upålideligt og negativt påvirker vores startups omdømme.

Med hver iteration af en given LLM har vi set præstationsforbedringer omkring minimering af hallucinationer. Selv med denne forbedring skal vi som applikationsbyggere og brugere stadig være opmærksomme på disse begrænsninger.

### Skadeligt Indhold

Vi dækkede i det tidligere afsnit, når en LLM producerer forkerte eller meningsløse svar. En anden risiko, vi skal være opmærksomme på, er, når en model reagerer med skadeligt indhold.

Skadeligt indhold kan defineres som:

- At give instruktioner eller opmuntre til selvskade eller skade på bestemte grupper.
- Hadefuldt eller nedgørende indhold.
- At vejlede planlægning af enhver form for angreb eller voldelige handlinger.
- At give instruktioner om, hvordan man finder ulovligt indhold eller begår ulovlige handlinger.
- At vise seksuelt eksplicit indhold.

For vores startup vil vi sikre, at vi har de rigtige værktøjer og strategier på plads for at forhindre, at denne type indhold bliver set af elever.

### Manglende Retfærdighed

Retfærdighed defineres som "at sikre, at et AI-system er fri for bias og diskrimination og at de behandler alle retfærdigt og lige." I Generativ AI's verden ønsker vi at sikre, at ekskluderende verdenssyn af marginaliserede grupper ikke forstærkes af modellens output.

Disse typer af output er ikke kun destruktive for at opbygge positive produktopplevelser for vores brugere, men de forårsager også yderligere samfundsskade. Som applikationsbyggere bør vi altid have en bred og forskelligartet brugerbase i tankerne, når vi bygger løsninger med Generativ AI.

## Hvordan Man Bruger Generativ AI Ansvarligt

Nu hvor vi har identificeret vigtigheden af Ansvarlig Generativ AI, lad os se på 4 trin, vi kan tage for at bygge vores AI-løsninger ansvarligt:

### Mål Potentielle Skader

I softwaretest tester vi de forventede handlinger fra en bruger på en applikation. Tilsvarende er det en god måde at måle potentiel skade ved at teste et mangfoldigt sæt af prompts, som brugerne sandsynligvis vil bruge.

Da vores startup bygger et uddannelsesprodukt, ville det være godt at forberede en liste over uddannelsesrelaterede prompts. Dette kunne være for at dække et bestemt emne, historiske fakta og prompts om studielivet.

### Afbød Potentielle Skader

Det er nu tid til at finde måder, hvor vi kan forhindre eller begrænse den potentielle skade forårsaget af modellen og dens svar. Vi kan se på dette i 4 forskellige lag:

- **Model**. Vælge den rigtige model til den rigtige brugssag. Større og mere komplekse modeller som GPT-4 kan forårsage mere risiko for skadeligt indhold, når de anvendes på mindre og mere specifikke brugssager. Brug af dine træningsdata til at finjustere reducerer også risikoen for skadeligt indhold.

- **Sikkerhedssystem**. Et sikkerhedssystem er et sæt værktøjer og konfigurationer på platformen, der betjener modellen, som hjælper med at afbøde skade. Et eksempel på dette er indholdsfiltreringssystemet på Azure OpenAI-tjenesten. Systemer bør også opdage jailbreak-angreb og uønsket aktivitet som anmodninger fra bots.

- **Metaprompt**. Metaprompts og grounding er måder, vi kan styre eller begrænse modellen baseret på visse adfærdsmønstre og information. Dette kunne være ved at bruge systeminput til at definere visse grænser for modellen. Derudover ved at give output, der er mere relevante for systemets omfang eller domæne.

Det kan også være ved at bruge teknikker som Retrieval Augmented Generation (RAG) for at få modellen til kun at trække information fra et udvalg af betroede kilder. Der er en lektion senere i dette kursus for [opbygning af søgeapplikationer](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Brugeroplevelse**. Det sidste lag er, hvor brugeren interagerer direkte med modellen gennem vores applikationsgrænseflade på en eller anden måde. På denne måde kan vi designe UI/UX for at begrænse brugeren på de typer input, de kan sende til modellen, samt tekst eller billeder vist til brugeren. Når vi implementerer AI-applikationen, skal vi også være gennemsigtige om, hvad vores Generative AI-applikation kan og ikke kan gøre.

Vi har en hel lektion dedikeret til [Designing UX for AI Applications](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Evaluer model**. At arbejde med LLM'er kan være udfordrende, fordi vi ikke altid har kontrol over de data, modellen blev trænet på. Uanset hvad, bør vi altid evaluere modellens ydeevne og output. Det er stadig vigtigt at måle modellens nøjagtighed, lighed, forankring og relevans af output. Dette hjælper med at give gennemsigtighed og tillid til interessenter og brugere.

### Drive en Ansvarlig Generativ AI-løsning

At bygge en operationel praksis omkring dine AI-applikationer er det sidste trin. Dette inkluderer at samarbejde med andre dele af vores startup som Legal og Security for at sikre, at vi overholder alle lovgivningsmæssige politikker. Før lancering vil vi også bygge planer omkring levering, håndtering af hændelser og tilbagerulning for at forhindre enhver skade på vores brugere fra at vokse.

## Værktøjer

Mens arbejdet med at udvikle Ansvarlige AI-løsninger kan virke som meget, er det arbejde, der er værd at gøre. Efterhånden som området for Generativ AI vokser, vil flere værktøjer til at hjælpe udviklere med effektivt at integrere ansvarlighed i deres arbejdsprocesser modnes. For eksempel kan [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) hjælpe med at opdage skadeligt indhold og billeder via en API-anmodning.

## Videnscheck

Hvad er nogle ting, du skal tage dig af for at sikre ansvarlig AI-brug?

1. At svaret er korrekt.
1. Skadelig brug, at AI ikke bruges til kriminelle formål.
1. At sikre, at AI er fri for bias og diskrimination.

A: 2 og 3 er korrekte. Ansvarlig AI hjælper dig med at overveje, hvordan du kan afbøde skadelige effekter og bias og mere.

## 🚀 Udfordring

Læs op på [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) og se, hvad du kan tage i brug til din brug.

## Godt Arbejde, Fortsæt Din Læring

Efter at have gennemført denne lektion, tjek vores [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at forbedre din Generative AI-viden!

Gå videre til Lektion 4, hvor vi vil se på [Prompt Engineering Fundamentals](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå ved brugen af denne oversættelse.