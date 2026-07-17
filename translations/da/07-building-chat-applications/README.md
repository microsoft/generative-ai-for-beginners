# Bygning af generative AI-drevne chatapplikationer

[![Bygning af generative AI-drevne chatapplikationer](../../../translated_images/da/07-lesson-banner.a279b937f2843833.webp)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Klik på billedet ovenfor for at se videoen af denne lektion)_

Nu hvor vi har set, hvordan vi kan bygge tekstgenereringsapps, lad os se nærmere på chatapplikationer.

Chatapplikationer er blevet integreret i vores daglige liv og tilbyder mere end blot en måde til afslappet samtale. De er integrerede dele af kundeservice, teknisk support og endda sofistikerede rådgivningssystemer. Det er sandsynligt, at du for nylig har fået hjælp fra en chatapplikation. Efterhånden som vi integrerer mere avancerede teknologier som generativ AI i disse platforme, øges kompleksiteten, ligesom udfordringerne.

Nogle spørgsmål, vi skal have besvaret, er:

- **Bygning af appen**. Hvordan bygger vi effektivt og integrerer sømløst disse AI-drevne applikationer til specifikke anvendelsestilfælde?
- **Overvågning**. Når de er implementeret, hvordan kan vi overvåge og sikre, at applikationerne fungerer på det højeste kvalitetsniveau, både hvad angår funktionalitet og overholdelse af [de seks principper for ansvarlig AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

Efterhånden som vi bevæger os videre ind i en æra defineret af automatisering og sømløs menneske-maskine-interaktion, bliver det essentielt at forstå, hvordan generativ AI transformerer omfanget, dybden og tilpasningsevnen af chatapplikationer. Denne lektion vil undersøge aspekter af arkitektur, der understøtter disse komplekse systemer, dykke ned i metoder til finjustering af dem til domænespecifikke opgaver samt evaluere målinger og overvejelser relevante for ansvarlig AI-implementering.

## Introduktion

Denne lektion dækker:

- Teknikker til effektivt at bygge og integrere chatapplikationer.
- Hvordan man anvender tilpasning og finjustering til applikationer.
- Strategier og overvejelser for effektiv overvågning af chatapplikationer.

## Læringsmål

Ved afslutningen af denne lektion vil du kunne:

- Beskrive overvejelser for at bygge og integrere chatapplikationer i eksisterende systemer.
- Tilpasse chatapplikationer til specifikke anvendelsestilfælde.
- Identificere nøglemålinger og overvejelser for effektivt at overvåge og opretholde kvaliteten af AI-drevne chatapplikationer.
- Sikre, at chatapplikationer udnytter AI ansvarligt.

## Integration af generativ AI i chatapplikationer

At løfte chatapplikationer gennem generativ AI handler ikke kun om at gøre dem klogere; det drejer sig om at optimere deres arkitektur, ydeevne og brugergrænseflade for at levere en kvalitetsbrugerooplevelse. Det involverer at undersøge de arkitektoniske fundamenter, API-integrationer og brugergrænsefladeovervejelser. Dette afsnit har til formål at give dig et omfattende køreplan til at navigere i disse komplekse landskaber, uanset om du tilslutter dem til eksisterende systemer eller bygger dem som selvstændige platforme.

Ved afslutningen af dette afsnit vil du være udstyret med den ekspertise, der er nødvendig for effektivt at konstruere og inkorporere chatapplikationer.

### Chatbot eller chatapplikation?

Før vi dykker ned i at bygge chatapplikationer, lad os sammenligne 'chatbots' med 'AI-drevne chatapplikationer', som tjener forskellige roller og funktionaliteter. En chatbots hovedformål er at automatisere specifikke samtaleopgaver, såsom at besvare ofte stillede spørgsmål eller spore en pakke. Den styres typisk af regelbaseret logik eller komplekse AI-algoritmer. Til sammenligning er en AI-drevet chatapplikation et langt bredere miljø designet til at facilitere forskellige former for digital kommunikation, såsom tekst-, stemme- og videochats mellem menneskelige brugere. Dets definerende egenskab er integrationen af en generativ AI-model, der simulerer nuancerede, menneskelignende samtaler og genererer svar baseret på en bred variation af input og kontekstuelle signaler. En generativ AI-drevet chatapplikation kan engagere sig i åbne domænediskussioner, tilpasse sig skiftende samtalekontekster og endda producere kreativ eller kompleks dialog.

Tabellen nedenfor skitserer nøgleforskelle og ligheder for at hjælpe os med at forstå deres unikke roller i digital kommunikation.

| Chatbot                               | Generativ AI-drevet chatapplikation |
| ------------------------------------- | -------------------------------------- |
| Opgavefokuseret og regelbaseret       | Kontekstbevidst                        |
| Ofte integreret i større systemer     | Kan indeholde en eller flere chatbots |
| Begrænset til programmerede funktioner | Indeholder generative AI-modeller      |
| Specialiserede og strukturerede interaktioner | I stand til åbne domænediskussioner  |

### Udnyttelse af forudbyggede funktionaliteter med SDK'er og API'er

Når man bygger en chatapplikation, er et godt første skridt at vurdere, hvad der allerede findes. Brug af SDK'er og API'er til at bygge chatapplikationer er en fordelagtig strategi af flere grunde. Ved at integrere veldokumenterede SDK'er og API'er positionerer du din applikation strategisk for langsigtet succes og adresserer skalerbarheds- og vedligeholdelseskoncerner.

- **Fremskynder udviklingsprocessen og reducerer omkostninger**: Ved at stole på forudbyggede funktionaliteter i stedet for den dyre proces at bygge dem selv, kan du fokusere på andre aspekter af din applikation, som du måske finder vigtigere, såsom forretningslogik.
- **Bedre ydelse**: Når man bygger funktionalitet fra bunden, spørger man sig selv "Hvordan skalerer det? Er denne applikation i stand til at håndtere et pludseligt brugeropbud?" Velvedligeholdte SDK'er og API'er har ofte indbyggede løsninger til disse problemstillinger.
- **Nemmere vedligeholdelse**: Opdateringer og forbedringer er lettere at håndtere, da de fleste API'er og SDK'er blot kræver en opdatering af et bibliotek, når en nyere version frigives.
- **Adgang til banebrydende teknologi**: Udnyttelse af modeller, der er finjusteret og trænet på omfattende datasæt, giver din applikation naturlige sprogkapaciteter.

Adgang til funktionaliteten i en SDK eller API involverer typisk at få tilladelse til at bruge de leverede tjenester, hvilket ofte er gennem en unik nøgle eller autentifikationstoken. Vi vil bruge OpenAI Python-biblioteket til at udforske, hvordan dette ser ud. Du kan også prøve det selv i følgende [notebook for OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) eller [notebook for Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) til denne lektion.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

response = client.responses.create(model="gpt-5-mini", input="Suggest two titles for an instructional lesson on chat applications for generative AI.", store=False)
print(response.output_text)
```

Ovenstående eksempel bruger GPT-5 mini-modellen med Responses API til at fuldføre prompten, men læg mærke til, at API-nøglen er sat, inden dette sker. Du ville få en fejl, hvis du ikke satte nøglen.

## Brugeroplevelse (UX)

Generelle UX-principper gælder for chatapplikationer, men her er nogle yderligere overvejelser, der bliver særligt vigtige på grund af de involverede maskinlæringskomponenter.

- **Mekanisme til håndtering af tvetydighed**: Generative AI-modeller genererer lejlighedsvis tvetydige svar. En funktion, der tillader brugere at bede om afklaring, kan være nyttig, hvis de støder på dette problem.
- **Konteksthåndtering**: Avancerede generative AI-modeller har evnen til at huske kontekst inden for en samtale, hvilket kan være en nødvendig fordel for brugeroplevelsen. At give brugerne mulighed for at kontrollere og håndtere kontekst forbedrer brugeroplevelsen, men indebærer risiko for at bevare følsomme brugeroplysninger. Overvejelser om, hvor længe disse oplysninger opbevares, såsom at indføre en retentionspolitik, kan balancere behovet for kontekst mod privatliv.
- **Personalisering**: Med evnen til at lære og tilpasse sig tilbyder AI-modeller en individuel oplevelse for en bruger. At tilpasse brugeroplevelsen gennem funktioner som brugerprofiler får ikke kun brugeren til at føle sig forstået, men hjælper også deres søgen efter specifikke svar og skaber en mere effektiv og tilfredsstillende interaktion.

Et sådant eksempel på personalisering er "Custom instructions"-indstillingerne i OpenAI's ChatGPT. Det tillader dig at give oplysninger om dig selv, som kan være vigtig kontekst for dine prompts. Her er et eksempel på en brugerdefineret instruktion.

![Custom Instructions Settings in ChatGPT](../../../translated_images/da/custom-instructions.b96f59aa69356fcf.webp)

Denne "profil" beder ChatGPT om at lave en lektionsplan om linked lists. Bemærk, at ChatGPT tager hensyn til, at brugeren måske ønsker en mere dybdegående lektionsplan baseret på hendes erfaring.

![A prompt in ChatGPT for a lesson plan about linked lists](../../../translated_images/da/lesson-plan-prompt.cc47c488cf1343df.webp)

### Microsofts systemmeddelelsesramme for store sprogmodeller

[Microsoft har givet vejledning](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) til at skrive effektive systemmeddelelser, når der genereres svar fra LLM'er opdelt i 4 områder:

1. Definere, hvem modellen er til, samt dens kapaciteter og begrænsninger.
2. Definere modellens outputformat.
3. Give specifikke eksempler, der demonstrerer modellens tilsigtede adfærd.
4. Give yderligere adfærdsrige regler.

### Tilgængelighed

Uanset om en bruger har visuelle, auditive, motoriske eller kognitive handicap, bør en veludformet chatapplikation være brugbar for alle. Følgende liste bryder specifikke funktioner ned med det formål at forbedre tilgængeligheden for forskellige brugerhandicap.

- **Funktioner for synshandicap**: Høje kontrasttemaer og justerbar tekststørrelse, skærmlæserkompatibilitet.
- **Funktioner for hørehæmmede**: Tekst-til-tale og tale-til-tekst-funktioner, visuelle signaler til lydmeddelelser.
- **Funktioner for motoriske handicap**: Tastaturnavigation, stemmekommandoer.
- **Funktioner for kognitive handicap**: Forenklede sprogindstillinger.

## Tilpasning og finjustering for domænespecifikke sprogmodeller

Forestil dig en chatapplikation, som forstår dit firmas jargon og forudser de specifikke forespørgsler, som dens brugerbase ofte har. Der er et par tilgange, der er værd at nævne:

- **Udnyttelse af DSL-modeller**. DSL står for domain specific language (domænespecifikt sprog). Du kan udnytte en såkaldt DSL-model, der er trænet på et specifikt domæne, for at forstå dets begreber og scenarier.
- **Anvend finjustering**. Finjustering er processen med yderligere at træne din model med specifikke data.

## Tilpasning: Brug af en DSL

Udnyttelse af domænespecifikke sprogmodeller (DSL-modeller) kan øge brugerengagement ved at tilbyde specialiserede, kontekstuelt relevante interaktioner. Det er en model, der er trænet eller finjusteret til at forstå og generere tekst relateret til et specifikt felt, industri eller emne. Muligheder for at bruge en DSL-model kan variere fra at træne én fra bunden til at bruge eksisterende gennem SDK'er og API'er. En anden mulighed er finjustering, hvilket involverer at tage en eksisterende fortrænet model og tilpasse den til et specifikt domæne.

## Tilpasning: Anvend finjustering

Finjustering overvejes ofte, når en fortrænet model ikke rækker til i et specialiseret domæne eller specifik opgave.

For eksempel er medicinske forespørgsler komplekse og kræver meget kontekst. Når en medicinsk professionel stiller en diagnose, baseres det på en række faktorer såsom livsstil eller eksisterende lidelser og kan endda stole på nyere medicinske tidsskrifter for at bekræfte diagnosen. I sådanne nuancerede scenarier kan en generel AI-chatapplikation ikke være en pålidelig kilde.

### Scenario: en medicinsk applikation

Overvej en chatapplikation designet til at hjælpe medicinske praktikere ved at give hurtige referencer til behandlingsretningslinjer, lægemiddelinteraktioner eller nyeste forskningsresultater.

En generel model kan være tilstrækkelig til at besvare grundlæggende medicinske spørgsmål eller give generelle råd, men den kan have vanskeligheder med følgende:

- **Højt specialiserede eller komplekse tilfælde**. For eksempel kunne en neurolog spørge applikationen: "Hvad er de nuværende bedste praksisser for håndtering af lægemiddelresistent epilepsi hos pædiatriske patienter?"
- **Mangel på nyere fremskridt**. En generel model kan have svært ved at give et aktuelt svar, der inkluderer de seneste fremskridt inden for neurologi og farmakologi.

I sådanne tilfælde kan finjustering af modellen med et specialiseret medicinsk datasæt væsentligt forbedre dens evne til mere præcist og pålideligt at håndtere disse indviklede medicinske forespørgsler. Dette kræver adgang til et stort og relevant datasæt, der repræsenterer domænespecifikke udfordringer og spørgsmål, der skal adresseres.

## Overvejelser for en AI-drevet chatoplevelse af høj kvalitet

Dette afsnit skitserer kriterierne for "højkvalitets" chatapplikationer, som omfatter indsamling af handlingsorienterede målinger og overholdelse af en ramme, der ansvarligt udnytter AI-teknologi.

### Nøglemålinger

For at opretholde applikationens høje ydelseskvalitet er det essentielt at holde styr på nøglemålinger og overvejelser. Disse målinger sikrer ikke kun applikationens funktionalitet, men vurderer også kvaliteten af AI-modellen og brugeroplevelsen. Nedenfor er en liste, der dækker basale, AI-, og brugeroplevelsesmålinger, som bør overvejes.

| Måling                        | Definition                                                                                                             | Overvejelser for chatudvikler                                          |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Oppetid**                  | Måler den tid, applikationen er operationel og tilgængelig for brugere.                                                | Hvordan vil du minimere nedetid?                                        |
| **Responstid**               | Tiden det tager for applikationen at svare på en brugers forespørgsel.                                                  | Hvordan kan du optimere forespørgselsbehandlingen for at forbedre responstiden? |
| **Præcision**                | Forholdet mellem sande positive forudsigelser og det samlede antal positive forudsigelser                              | Hvordan vil du validere præcisionen af din model?                       |
| **Recall (Sensitivitet)**    | Forholdet mellem sande positive forudsigelser og det faktiske antal positive                                          | Hvordan vil du måle og forbedre recall?                                 |
| **F1-score**                | Den harmoniske middelværdi af præcision og recall, som balancerer kompromiset mellem begge                              | Hvad er dit mål for F1-score? Hvordan vil du balancere præcision og recall? |
| **Perplexity**              | Måler, hvor godt sandsynlighedsfordelingen forudsagt af modellen stemmer overens med den faktiske datafordeling.       | Hvordan vil du minimere perplexity?                                     |
| **Brugertilfredshedsmålinger** | Måler brugerens opfattelse af applikationen. Ofte indsamlet gennem undersøgelser.                                      | Hvor ofte vil du indsamle brugerfeedback? Hvordan vil du tilpasse dig ud fra denne? |
| **Fejlrate**                | Raten, hvor modellen laver fejl i forståelse eller output.                                                             | Hvilke strategier har du for at reducere fejlrater?                     |
| **Omtræningscyklusser**     | Hyppigheden, hvormed modellen opdateres for at indarbejde nye data og indsigt.                                         | Hvor ofte vil du omtræne modellen? Hvad udløser en omtræningscyklus?    |

| **Anomali-registrering**     | Værktøjer og teknikker til at identificere usædvanlige mønstre, der ikke stemmer overens med forventet adfærd.                    | Hvordan vil du reagere på anomalier?                                      |

### Implementering af Ansvarlige AI-praksiser i Chatapplikationer

Microsofts tilgang til Ansvarlig AI har identificeret seks principper, der bør styre AI-udvikling og -brug. Nedenfor er principperne, deres definition og ting, som en chatudvikler bør overveje, og hvorfor de skal tages alvorligt.

| Principper             | Microsofts Definition                               | Overvejelser for Chatudvikler                                         | Hvorfor det er vigtigt                                                                 |
| ---------------------- | -------------------------------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Retfærdighed           | AI-systemer skal behandle alle mennesker retfærdigt.| Sørg for, at chatapplikationen ikke diskriminerer baseret på brugerdata.| For at opbygge tillid og inklusivitet blandt brugere; undgår juridiske konsekvenser.   |
| Pålidelighed og Sikkerhed| AI-systemer skal fungere pålideligt og sikkert.   | Implementer test og sikkerhedsforanstaltninger for at minimere fejl og risici. | Sikrer brugerens tilfredshed og forhindrer potentiel skade.                            |
| Privatliv og Sikkerhed | AI-systemer skal være sikre og respektere privatliv.| Implementer stærk kryptering og databeskyttelsesforanstaltninger.     | For at beskytte følsomme brugerdata og overholde privatlivslove.                       |
| Inklusion              | AI-systemer skal styrke alle og engagere mennesker. | Design UI/UX, der er tilgængeligt og nemt at bruge for forskellige målgrupper. | Sikrer, at et bredere spektrum af mennesker effektivt kan bruge applikationen.        |
| Gennemsigtighed        | AI-systemer skal være forståelige.                  | Giv klar dokumentation og begrundelse for AI-svar.                     | Brugere er mere tilbøjelige til at have tillid til et system, hvis de kan forstå, hvordan beslutninger træffes. |
| Ansvarlighed           | Mennesker skal kunne holdes ansvarlige for AI-systemer.| Etabler en klar proces for revision og forbedring af AI-beslutninger. | Muliggør løbende forbedring og korrigerende handlinger i tilfælde af fejl.            |

## Opgave

Se [assignment](../../../07-building-chat-applications/python). Den vil tage dig gennem en række øvelser fra at køre dine første chat-prompter til at klassificere og opsummere tekst og mere. Bemærk, at opgaverne er tilgængelige i forskellige programmeringssprog!

## Godt arbejde! Fortsæt rejsen

Når du har gennemført denne lektion, kan du tjekke vores [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at øge din viden om Generativ AI!

Gå videre til Lektion 8 for at se, hvordan du kan begynde at [bygge søgeapplikationer](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->