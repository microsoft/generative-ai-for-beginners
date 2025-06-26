<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ea4bbe640847aafbbba14dae4625e9af",
  "translation_date": "2025-06-25T15:38:04+00:00",
  "source_file": "07-building-chat-applications/README.md",
  "language_code": "da"
}
-->
# Bygning af generative AI-drevne chatapplikationer

[![Bygning af generative AI-drevne chatapplikationer](../../../translated_images/07-lesson-banner.a279b937f2843833fe28b4597f51bdef92d0ad03efee7ba52d0f166dea7574e5.da.png)](https://aka.ms/gen-ai-lessons7-gh?WT.mc_id=academic-105485-koreyst)

> _(Klik på billedet ovenfor for at se videoen af denne lektion)_

Nu hvor vi har set, hvordan vi kan bygge tekstgenereringsapps, lad os se på chatapplikationer.

Chatapplikationer er blevet integreret i vores dagligdag og tilbyder mere end blot en måde at føre uformelle samtaler på. De er en integreret del af kundeservice, teknisk support og endda sofistikerede rådgivningssystemer. Det er sandsynligt, at du har fået hjælp fra en chatapplikation for ikke så længe siden. Når vi integrerer mere avancerede teknologier som generativ AI i disse platforme, øges kompleksiteten, og det samme gør udfordringerne.

Nogle spørgsmål, vi skal have besvaret, er:

- **Bygning af appen**. Hvordan bygger vi effektivt og integrerer problemfrit disse AI-drevne applikationer til specifikke brugsscenarier?
- **Overvågning**. Når de er implementeret, hvordan kan vi overvåge og sikre, at applikationerne fungerer på det højeste kvalitetsniveau, både med hensyn til funktionalitet og overholdelse af [de seks principper for ansvarlig AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

Efterhånden som vi bevæger os længere ind i en tidsalder præget af automatisering og problemfri interaktioner mellem mennesker og maskiner, bliver forståelsen af, hvordan generativ AI transformerer omfanget, dybden og tilpasningsevnen af chatapplikationer, essentiel. Denne lektion vil undersøge de arkitekturelle aspekter, der understøtter disse komplekse systemer, dykke ned i metoderne til at finjustere dem til domænespecifikke opgaver og evaluere de målinger og overvejelser, der er relevante for at sikre ansvarlig AI-implementering.

## Introduktion

Denne lektion dækker:

- Teknikker til effektivt at bygge og integrere chatapplikationer.
- Hvordan man anvender tilpasning og finjustering på applikationer.
- Strategier og overvejelser for effektivt at overvåge chatapplikationer.

## Læringsmål

Ved slutningen af denne lektion vil du kunne:

- Beskrive overvejelser for at bygge og integrere chatapplikationer i eksisterende systemer.
- Tilpasse chatapplikationer til specifikke brugsscenarier.
- Identificere nøglemålinger og overvejelser for effektivt at overvåge og opretholde kvaliteten af AI-drevne chatapplikationer.
- Sikre, at chatapplikationer udnytter AI ansvarligt.

## Integration af generativ AI i chatapplikationer

At hæve chatapplikationer gennem generativ AI handler ikke kun om at gøre dem klogere; det handler om at optimere deres arkitektur, ydeevne og brugergrænseflade for at levere en kvalitetsoplevelse for brugeren. Dette involverer at undersøge de arkitekturelle fundamenter, API-integrationer og overvejelser om brugergrænsefladen. Denne sektion har til formål at tilbyde dig en omfattende køreplan for at navigere i disse komplekse landskaber, uanset om du integrerer dem i eksisterende systemer eller bygger dem som selvstændige platforme.

Ved slutningen af denne sektion vil du være udstyret med den ekspertise, der er nødvendig for effektivt at konstruere og inkorporere chatapplikationer.

### Chatbot eller chatapplikation?

Før vi dykker ned i at bygge chatapplikationer, lad os sammenligne 'chatbots' med 'AI-drevne chatapplikationer', som tjener forskellige roller og funktionaliteter. En chatbots hovedformål er at automatisere specifikke samtaleopgaver, såsom at besvare ofte stillede spørgsmål eller spore en pakke. Den styres typisk af regelbaseret logik eller komplekse AI-algoritmer. I modsætning hertil er en AI-drevet chatapplikation et langt mere ekspansivt miljø designet til at facilitere forskellige former for digital kommunikation, såsom tekst-, tale- og videochats blandt menneskelige brugere. Dens definerende funktion er integrationen af en generativ AI-model, der simulerer nuancerede, menneskelignende samtaler og genererer svar baseret på en bred vifte af input og kontekstuelle ledetråde. En generativ AI-drevet chatapplikation kan engagere sig i åbne domæne-diskussioner, tilpasse sig udviklende samtalekontekster og endda producere kreativ eller kompleks dialog.

Tabellen nedenfor skitserer de vigtigste forskelle og ligheder for at hjælpe os med at forstå deres unikke roller i digital kommunikation.

| Chatbot                               | Generativ AI-drevet chatapplikation |
| ------------------------------------- | ----------------------------------- |
| Opgavefokuseret og regelbaseret       | Kontekstbevidst                     |
| Ofte integreret i større systemer     | Kan være vært for en eller flere chatbots |
| Begrænset til programmerede funktioner| Inkorporerer generative AI-modeller |
| Specialiserede & strukturerede interaktioner | I stand til åbne domæne-diskussioner |

### Udnytte forudbyggede funktioner med SDK'er og API'er

Når du bygger en chatapplikation, er et godt første skridt at vurdere, hvad der allerede er derude. Brug af SDK'er og API'er til at bygge chatapplikationer er en fordelagtig strategi af forskellige årsager. Ved at integrere veldokumenterede SDK'er og API'er positionerer du strategisk din applikation til langsigtet succes og adresserer skalerbarhed og vedligeholdelsesbekymringer.

- **Fremskynder udviklingsprocessen og reducerer omkostninger**: At stole på forudbyggede funktioner i stedet for den dyre proces med at bygge dem selv giver dig mulighed for at fokusere på andre aspekter af din applikation, som du måske finder mere vigtige, såsom forretningslogik.
- **Bedre ydeevne**: Når du bygger funktionalitet fra bunden, vil du til sidst spørge dig selv "Hvordan skalerer det? Er denne applikation i stand til at håndtere en pludselig tilstrømning af brugere?" Velholdte SDK'er og API'er har ofte indbyggede løsninger til disse bekymringer.
- **Nem vedligeholdelse**: Opdateringer og forbedringer er lettere at administrere, da de fleste API'er og SDK'er simpelthen kræver en opdatering af et bibliotek, når en nyere version frigives.
- **Adgang til banebrydende teknologi**: Udnyttelse af modeller, der er finjusterede og trænet på omfattende datasæt, giver din applikation naturlige sprogfunktioner.

Adgang til funktionaliteten af en SDK eller API involverer typisk at få tilladelse til at bruge de leverede tjenester, hvilket ofte sker gennem brugen af en unik nøgle eller autentificeringstoken. Vi vil bruge OpenAI Python Library til at udforske, hvordan dette ser ud. Du kan også prøve det selv i følgende [notebook for OpenAI](../../../07-building-chat-applications/python/oai-assignment.ipynb) eller [notebook for Azure OpenAI Services](../../../07-building-chat-applications/python/aoai-assignment.ipynb) for denne lektion.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

chat_completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Suggest two titles for an instructional lesson on chat applications for generative AI."}])
```

Ovenstående eksempel bruger GPT-3.5 Turbo-modellen til at fuldføre prompten, men bemærk, at API-nøglen er sat før det gøres. Du ville modtage en fejl, hvis du ikke satte nøglen.

## Brugeroplevelse (UX)

Generelle UX-principper gælder for chatapplikationer, men her er nogle yderligere overvejelser, der bliver særligt vigtige på grund af de maskinlæringskomponenter, der er involveret.

- **Mekanisme til adressere tvetydighed**: Generative AI-modeller genererer lejlighedsvis tvetydige svar. En funktion, der giver brugere mulighed for at bede om afklaring, kan være nyttig, hvis de støder på dette problem.
- **Kontekstbevarelse**: Avancerede generative AI-modeller har evnen til at huske kontekst inden for en samtale, hvilket kan være en nødvendig ressource til brugeroplevelsen. At give brugerne mulighed for at kontrollere og administrere kontekst forbedrer brugeroplevelsen, men introducerer risikoen for at bevare følsomme brugeroplysninger. Overvejelser om, hvor længe denne information er gemt, såsom introduktion af en bevaringspolitik, kan balancere behovet for kontekst mod privatliv.
- **Personalisering**: Med evnen til at lære og tilpasse sig tilbyder AI-modeller en individualiseret oplevelse for en bruger. Tilpasning af brugeroplevelsen gennem funktioner som brugerprofiler får ikke kun brugeren til at føle sig forstået, men hjælper også med deres jagt på at finde specifikke svar, hvilket skaber en mere effektiv og tilfredsstillende interaktion.

Et sådant eksempel på personalisering er "Custom instructions" indstillingerne i OpenAI's ChatGPT. Det giver dig mulighed for at give oplysninger om dig selv, der kan være vigtig kontekst for dine prompts. Her er et eksempel på en tilpasset instruktion.

![Tilpassede instruktionsindstillinger i ChatGPT](../../../translated_images/custom-instructions.b96f59aa69356fcfed456414221919e8996f93c90c20d0d58d1bc0221e3c909f.da.png)

Denne "profil" beder ChatGPT om at skabe en lektionsplan om linked lists. Bemærk, at ChatGPT tager højde for, at brugeren måske ønsker en mere dybdegående lektionsplan baseret på hendes erfaring.

![En prompt i ChatGPT for en lektionsplan om linked lists](../../../translated_images/lesson-plan-prompt.cc47c488cf1343df5d67aa796a1acabca32c380e5b782971e289f6ab8b21cf5a.da.png)

### Microsofts System Message Framework for store sprogmodeller

[Microsoft har leveret vejledning](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) til at skrive effektive systemmeddelelser, når der genereres svar fra LLM'er, opdelt i 4 områder:

1. Definere, hvem modellen er til, samt dens kapaciteter og begrænsninger.
2. Definere modellens outputformat.
3. Give specifikke eksempler, der demonstrerer den tilsigtede adfærd af modellen.
4. Give yderligere adfærdsmæssige sikkerhedsforanstaltninger.

### Tilgængelighed

Uanset om en bruger har visuelle, auditive, motoriske eller kognitive handicap, bør en veldesignet chatapplikation være anvendelig af alle. Følgende liste nedbryder specifikke funktioner, der sigter mod at forbedre tilgængeligheden for forskellige brugerhandicap.

- **Funktioner for synshandicap**: Højkontrast temaer og justerbar tekst, skærmlæser kompatibilitet.
- **Funktioner for hørehæmning**: Tekst-til-tale og tale-til-tekst funktioner, visuelle signaler for lydmeddelelser.
- **Funktioner for motorisk handicap**: Understøttelse af tastaturnavigation, stemmekommandoer.
- **Funktioner for kognitivt handicap**: Forenklede sprogvalg.

## Tilpasning og finjustering til domænespecifikke sprogmodeller

Forestil dig en chatapplikation, der forstår din virksomheds jargon og forudser de specifikke forespørgsler, dens brugerbase ofte har. Der er et par tilgange, der er værd at nævne:

- **Udnytte DSL-modeller**. DSL står for domænespecifikke sprog. Du kan udnytte en såkaldt DSL-model, der er trænet på et specifikt domæne, til at forstå dets begreber og scenarier.
- **Anvend finjustering**. Finjustering er processen med yderligere træning af din model med specifikke data.

## Tilpasning: Brug af en DSL

Udnyttelse af domænespecifikke sprogmodeller (DSL-modeller) kan forbedre brugerengagementet ved at give specialiserede, kontekstuelt relevante interaktioner. Det er en model, der er trænet eller finjusteret til at forstå og generere tekst relateret til et specifikt felt, industri eller emne. Mulighederne for at bruge en DSL-model kan variere fra at træne en fra bunden til at bruge eksisterende gennem SDK'er og API'er. En anden mulighed er finjustering, som involverer at tage en eksisterende fortrænet model og tilpasse den til et specifikt domæne.

## Tilpasning: Anvend finjustering

Finjustering overvejes ofte, når en fortrænet model falder kort i et specialiseret domæne eller specifik opgave.

For eksempel er medicinske forespørgsler komplekse og kræver meget kontekst. Når en medicinsk professionel diagnosticerer en patient, er det baseret på en række faktorer som livsstil eller eksisterende tilstande og kan endda stole på nylige medicinske tidsskrifter for at validere deres diagnose. I sådanne nuancerede scenarier kan en generel AI-chatapplikation ikke være en pålidelig kilde.

### Scenario: en medicinsk applikation

Overvej en chatapplikation designet til at hjælpe medicinske praktiserende ved at give hurtige referencer til behandlingsretningslinjer, lægemiddelinteraktioner eller nylige forskningsresultater.

En generel model kan være tilstrækkelig til at besvare grundlæggende medicinske spørgsmål eller give generelle råd, men den kan have problemer med følgende:

- **Meget specifikke eller komplekse tilfælde**. For eksempel kan en neurolog spørge applikationen: "Hvad er de nuværende bedste praksis for håndtering af lægemiddelresistent epilepsi hos pædiatriske patienter?"
- **Manglende nyere fremskridt**. En generel model kan have svært ved at give et aktuelt svar, der indarbejder de nyeste fremskridt inden for neurologi og farmakologi.

I sådanne tilfælde kan finjustering af modellen med et specialiseret medicinsk datasæt betydeligt forbedre dens evne til at håndtere disse indviklede medicinske forespørgsler mere præcist og pålideligt. Dette kræver adgang til et stort og relevant datasæt, der repræsenterer de domænespecifikke udfordringer og spørgsmål, der skal adresseres.

## Overvejelser for en høj kvalitet AI-drevet chatoplevelse

Denne sektion skitserer kriterierne for "høj kvalitet" chatapplikationer, som inkluderer indfangning af handlingsmæssige målinger og overholdelse af en ramme, der ansvarligt udnytter AI-teknologi.

### Nøglemålinger

For at opretholde den høje ydeevne af en applikation er det essentielt at holde styr på nøglemålinger og overvejelser. Disse målinger sikrer ikke kun applikationens funktionalitet, men vurderer også kvaliteten af AI-modellen og brugeroplevelsen. Nedenfor er en liste, der dækker grundlæggende, AI og brugeroplevelsesmålinger, der skal overvejes.

| Måling                        | Definition                                                                                                            | Overvejelser for chatudvikler                                             |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Oppetid**                   | Måler den tid, applikationen er operationel og tilgængelig for brugere.                                               | Hvordan vil du minimere nedetid?                                          |
| **Responstid**                | Den tid, det tager applikationen at svare på en brugers forespørgsel.                                                 | Hvordan kan du optimere forespørgselsbehandlingen for at forbedre responstiden? |
| **Præcision**                 | Forholdet mellem sande positive forudsigelser og det samlede antal positive forudsigelser                              | Hvordan vil du validere præcisionen af din model?                         |
| **Recall (Følsomhed)**        | Forholdet mellem sande positive forudsigelser og det faktiske antal positive                                          | Hvordan vil du måle og forbedre recall?                                   |
| **F1-score**                  | Det harmoniske gennemsnit af præcision og recall, der balancerer trade-off mellem begge.                              | Hvad er dit mål for F1-score? Hvordan vil du balancere præcision og recall? |
| **Forbløffelse**              | Måler, hvor godt sandsynlighedsfordelingen forudsagt af modellen stemmer overens med den faktiske fordeling af dataene. | Hvordan vil du minimere forbløffelse?                                     |
| **Brugertilfredshedsmålinger**| Måler brugerens opfattelse af applikationen. Ofte indfanget gennem undersøgelser.                                     | Hvor ofte vil du indsamle brugerfeedback? Hvordan vil du tilpasse dig baseret på det? |
| **Fejlrate**                  | Raten, hvormed modellen laver fejl i forståelse eller output.                                                         | Hvilke strategier har du på plads for at reducere fejlrate?               |
| **Retræningscyklusser**       | Hyppigheden, hvormed modellen opdateres for at indarbejde nye data og indsigter.                                     | Hvor ofte vil du retræne modellen? Hvad udløser en retræningscyklus?      |
| **Anomalidetektion**          | Værktøjer og teknikker til at

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at opnå nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for misforståelser eller fejltolkninger, der måtte opstå ved brugen af denne oversættelse.