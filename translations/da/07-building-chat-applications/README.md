<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5308963a56cfbad2d73b0fa99fe84b3",
  "translation_date": "2025-10-17T19:13:39+00:00",
  "source_file": "07-building-chat-applications/README.md",
  "language_code": "da"
}
-->
# Bygning af generative AI-drevne chatapplikationer

[![Bygning af generative AI-drevne chatapplikationer](../../../translated_images/07-lesson-banner.a279b937f2843833fe28b4597f51bdef92d0ad03efee7ba52d0f166dea7574e5.da.png)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Klik på billedet ovenfor for at se videoen til denne lektion)_

Nu hvor vi har set, hvordan vi kan bygge tekstgenereringsapps, lad os kigge nærmere på chatapplikationer.

Chatapplikationer er blevet en integreret del af vores dagligdag og tilbyder mere end blot en måde at føre afslappede samtaler på. De er essentielle i kundeservice, teknisk support og endda avancerede rådgivningssystemer. Det er sandsynligt, at du for nylig har fået hjælp fra en chatapplikation. Når vi integrerer mere avancerede teknologier som generativ AI i disse platforme, øges kompleksiteten, og det samme gør udfordringerne.

Nogle spørgsmål, vi skal have besvaret, er:

- **Bygning af appen**. Hvordan bygger vi effektivt og integrerer disse AI-drevne applikationer problemfrit til specifikke anvendelser?
- **Overvågning**. Når de er implementeret, hvordan kan vi overvåge og sikre, at applikationerne fungerer på det højeste kvalitetsniveau, både med hensyn til funktionalitet og overholdelse af de [seks principper for ansvarlig AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

Efterhånden som vi bevæger os længere ind i en tidsalder præget af automatisering og problemfri interaktioner mellem mennesker og maskiner, bliver det afgørende at forstå, hvordan generativ AI transformerer omfanget, dybden og tilpasningsevnen af chatapplikationer. Denne lektion vil undersøge de arkitektoniske aspekter, der understøtter disse komplekse systemer, dykke ned i metoderne til at finjustere dem til domænespecifikke opgaver og evaluere de metrikker og overvejelser, der er relevante for at sikre ansvarlig AI-implementering.

## Introduktion

Denne lektion dækker:

- Teknikker til effektivt at bygge og integrere chatapplikationer.
- Hvordan man anvender tilpasning og finjustering på applikationer.
- Strategier og overvejelser for effektivt at overvåge chatapplikationer.

## Læringsmål

Ved afslutningen af denne lektion vil du kunne:

- Beskrive overvejelser for at bygge og integrere chatapplikationer i eksisterende systemer.
- Tilpasse chatapplikationer til specifikke anvendelser.
- Identificere nøglemetrikker og overvejelser for effektivt at overvåge og opretholde kvaliteten af AI-drevne chatapplikationer.
- Sikre, at chatapplikationer anvender AI ansvarligt.

## Integration af generativ AI i chatapplikationer

At løfte chatapplikationer gennem generativ AI handler ikke kun om at gøre dem smartere; det handler om at optimere deres arkitektur, ydeevne og brugergrænseflade for at levere en kvalitetsoplevelse. Dette indebærer at undersøge de arkitektoniske fundamenter, API-integrationer og overvejelser om brugergrænsefladen. Dette afsnit har til formål at give dig en omfattende køreplan for at navigere i disse komplekse landskaber, uanset om du integrerer dem i eksisterende systemer eller bygger dem som selvstændige platforme.

Ved afslutningen af dette afsnit vil du være udstyret med ekspertise til effektivt at konstruere og integrere chatapplikationer.

### Chatbot eller chatapplikation?

Før vi dykker ned i opbygningen af chatapplikationer, lad os sammenligne 'chatbots' med 'AI-drevne chatapplikationer', som har forskellige roller og funktioner. En chatbots hovedformål er at automatisere specifikke samtaleopgaver, såsom at besvare ofte stillede spørgsmål eller spore en pakke. Den styres typisk af regelbaseret logik eller komplekse AI-algoritmer. En AI-drevet chatapplikation er derimod et langt mere omfattende miljø designet til at facilitere forskellige former for digital kommunikation, såsom tekst-, tale- og videochats mellem menneskelige brugere. Dens definerende funktion er integrationen af en generativ AI-model, der simulerer nuancerede, menneskelignende samtaler og genererer svar baseret på en bred vifte af input og kontekstuelle signaler. En generativ AI-drevet chatapplikation kan deltage i åbne diskussioner, tilpasse sig udviklende samtalekontekster og endda producere kreative eller komplekse dialoger.

Tabellen nedenfor skitserer de vigtigste forskelle og ligheder for at hjælpe os med at forstå deres unikke roller i digital kommunikation.

| Chatbot                               | Generativ AI-drevet chatapplikation    |
| ------------------------------------- | -------------------------------------- |
| Opgavefokuseret og regelbaseret       | Kontekstbevidst                        |
| Ofte integreret i større systemer     | Kan være vært for en eller flere chatbots |
| Begrænset til programmerede funktioner| Integrerer generative AI-modeller      |
| Specialiserede og strukturerede interaktioner | I stand til åbne diskussioner          |

### Udnyttelse af forudbyggede funktioner med SDK'er og API'er

Når man bygger en chatapplikation, er et godt første skridt at vurdere, hvad der allerede findes. Brug af SDK'er og API'er til at bygge chatapplikationer er en fordelagtig strategi af flere grunde. Ved at integrere veldokumenterede SDK'er og API'er positionerer du strategisk din applikation til langsigtet succes og adresserer bekymringer om skalerbarhed og vedligeholdelse.

- **Fremskynder udviklingsprocessen og reducerer omkostninger**: At stole på forudbyggede funktioner i stedet for den dyre proces med at bygge dem selv giver dig mulighed for at fokusere på andre aspekter af din applikation, som du måske finder vigtigere, såsom forretningslogik.
- **Bedre ydeevne**: Når du bygger funktionalitet fra bunden, vil du på et tidspunkt spørge dig selv "Hvordan skalerer det? Er denne applikation i stand til at håndtere en pludselig tilstrømning af brugere?" Veldrevne SDK'er og API'er har ofte indbyggede løsninger til disse bekymringer.
- **Lettere vedligeholdelse**: Opdateringer og forbedringer er lettere at administrere, da de fleste API'er og SDK'er blot kræver en opdatering af et bibliotek, når en nyere version udgives.
- **Adgang til avanceret teknologi**: Udnyttelse af modeller, der er finjusteret og trænet på omfattende datasæt, giver din applikation naturlige sprogfunktioner.

Adgang til funktionaliteten af en SDK eller API indebærer typisk at få tilladelse til at bruge de leverede tjenester, hvilket ofte sker gennem brug af en unik nøgle eller autentificeringstoken. Vi vil bruge OpenAI Python Library til at udforske, hvordan dette ser ud. Du kan også prøve det selv i følgende [notebook for OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) eller [notebook for Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) til denne lektion.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

chat_completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Suggest two titles for an instructional lesson on chat applications for generative AI."}])
```

Eksemplet ovenfor bruger GPT-3.5 Turbo-modellen til at fuldføre prompten, men bemærk, at API-nøglen er sat før dette. Du vil modtage en fejl, hvis du ikke sætter nøglen.

## Brugeroplevelse (UX)

Generelle UX-principper gælder for chatapplikationer, men her er nogle yderligere overvejelser, der bliver særligt vigtige på grund af de involverede maskinlæringskomponenter.

- **Mekanisme til at adressere tvetydighed**: Generative AI-modeller genererer lejlighedsvis tvetydige svar. En funktion, der giver brugerne mulighed for at bede om afklaring, kan være nyttig, hvis de støder på dette problem.
- **Kontekstbevaring**: Avancerede generative AI-modeller har evnen til at huske kontekst inden for en samtale, hvilket kan være en nødvendig fordel for brugeroplevelsen. At give brugerne mulighed for at kontrollere og administrere konteksten forbedrer brugeroplevelsen, men introducerer risikoen for at bevare følsomme brugeroplysninger. Overvejelser om, hvor længe disse oplysninger opbevares, såsom introduktion af en opbevaringspolitik, kan balancere behovet for kontekst mod privatliv.
- **Personalisering**: Med evnen til at lære og tilpasse sig tilbyder AI-modeller en individualiseret oplevelse for en bruger. At skræddersy brugeroplevelsen gennem funktioner som brugerprofiler får ikke kun brugeren til at føle sig forstået, men hjælper også med at finde specifikke svar, hvilket skaber en mere effektiv og tilfredsstillende interaktion.

Et eksempel på personalisering er indstillingen "Custom instructions" i OpenAI's ChatGPT. Det giver dig mulighed for at give oplysninger om dig selv, der kan være vigtig kontekst for dine prompts. Her er et eksempel på en brugerdefineret instruktion.

![Custom Instructions Settings i ChatGPT](../../../translated_images/custom-instructions.b96f59aa69356fcfed456414221919e8996f93c90c20d0d58d1bc0221e3c909f.da.png)

Denne "profil" beder ChatGPT om at oprette en lektionsplan om linked lists. Bemærk, at ChatGPT tager højde for, at brugeren måske ønsker en mere dybdegående lektionsplan baseret på hendes erfaring.

![En prompt i ChatGPT for en lektionsplan om linked lists](../../../translated_images/lesson-plan-prompt.cc47c488cf1343df5d67aa796a1acabca32c380e5b782971e289f6ab8b21cf5a.da.png)

### Microsofts System Message Framework for store sprogmodeller

[Microsoft har givet vejledning](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) til at skrive effektive systemmeddelelser, når der genereres svar fra LLM'er, opdelt i 4 områder:

1. Definere, hvem modellen er for, samt dens kapaciteter og begrænsninger.
2. Definere modellens outputformat.
3. Give specifikke eksempler, der demonstrerer den ønskede adfærd for modellen.
4. Give yderligere adfærdsbeskyttelsesforanstaltninger.

### Tilgængelighed

Uanset om en bruger har visuelle, auditive, motoriske eller kognitive handicap, bør en veludformet chatapplikation være brugbar for alle. Følgende liste opdeler specifikke funktioner, der sigter mod at forbedre tilgængeligheden for forskellige brugerhandicap.

- **Funktioner for synshandicap**: Højkontrasttemaer og tekst, der kan ændres i størrelse, skærmlæserkompatibilitet.
- **Funktioner for hørehæmning**: Tekst-til-tale og tale-til-tekst funktioner, visuelle signaler for lydmeddelelser.
- **Funktioner for motorisk handicap**: Understøttelse af tastaturnavigation, stemmekommandoer.
- **Funktioner for kognitive handicap**: Forenklede sprogindstillinger.

## Tilpasning og finjustering til domænespecifikke sprogmodeller

Forestil dig en chatapplikation, der forstår din virksomheds jargon og forudser de specifikke forespørgsler, dens brugerbase ofte har. Der er et par tilgange, der er værd at nævne:

- **Udnyttelse af DSL-modeller**. DSL står for domænespecifikke sprog. Du kan udnytte en såkaldt DSL-model, der er trænet på et specifikt domæne, til at forstå dets begreber og scenarier.
- **Anvend finjustering**. Finjustering er processen med yderligere træning af din model med specifikke data.

## Tilpasning: Brug af en DSL

Udnyttelse af domænespecifikke sprogmodeller (DSL-modeller) kan forbedre brugerengagementet ved at levere specialiserede, kontekstuelt relevante interaktioner. Det er en model, der er trænet eller finjusteret til at forstå og generere tekst relateret til et specifikt felt, en industri eller et emne. Mulighederne for at bruge en DSL-model kan variere fra at træne en fra bunden til at bruge allerede eksisterende gennem SDK'er og API'er. En anden mulighed er finjustering, som indebærer at tage en eksisterende forudtrænet model og tilpasse den til et specifikt domæne.

## Tilpasning: Anvend finjustering

Finjustering overvejes ofte, når en forudtrænet model ikke lever op til forventningerne i et specialiseret domæne eller en specifik opgave.

For eksempel er medicinske forespørgsler komplekse og kræver meget kontekst. Når en medicinsk professionel diagnosticerer en patient, er det baseret på en række faktorer såsom livsstil eller eksisterende tilstande og kan endda afhænge af nylige medicinske tidsskrifter for at validere deres diagnose. I sådanne nuancerede scenarier kan en generel AI-chatapplikation ikke være en pålidelig kilde.

### Scenario: en medicinsk applikation

Overvej en chatapplikation designet til at hjælpe medicinske fagfolk ved at give hurtige referencer til behandlingsretningslinjer, lægemiddelinteraktioner eller nylige forskningsresultater.

En generel model kan være tilstrækkelig til at besvare grundlæggende medicinske spørgsmål eller give generelle råd, men den kan have svært ved følgende:

- **Meget specifikke eller komplekse tilfælde**. For eksempel kunne en neurolog spørge applikationen: "Hvad er de nuværende bedste praksisser for håndtering af lægemiddelresistent epilepsi hos pædiatriske patienter?"
- **Manglende nylige fremskridt**. En generel model kunne have svært ved at give et aktuelt svar, der inkorporerer de nyeste fremskridt inden for neurologi og farmakologi.

I sådanne tilfælde kan finjustering af modellen med et specialiseret medicinsk datasæt betydeligt forbedre dens evne til at håndtere disse komplekse medicinske forespørgsler mere præcist og pålideligt. Dette kræver adgang til et stort og relevant datasæt, der repræsenterer de domænespecifikke udfordringer og spørgsmål, der skal adresseres.

## Overvejelser for en AI-drevet chatoplevelse af høj kvalitet

Dette afsnit skitserer kriterierne for "høj kvalitet" chatapplikationer, som inkluderer indsamling af handlingsrettede metrikker og overholdelse af en ramme, der ansvarligt udnytter AI-teknologi.

### Nøglemetrikker

For at opretholde applikationens høje ydeevne er det vigtigt at holde styr på nøglemetrikker og overvejelser. Disse målinger sikrer ikke kun applikationens funktionalitet, men vurderer også kvaliteten af AI-modellen og brugeroplevelsen. Nedenfor er en liste, der dækker grundlæggende, AI- og brugeroplevelsesmetrikker, der skal overvejes.

| Metrik                        | Definition                                                                                                             | Overvejelser for chatudvikler                                             |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Oppetid**                   | Måler den tid, applikationen er operationel og tilgængelig for brugere.                                                | Hvordan vil du minimere nedetid?                                          |
| **Responstid**                | Den tid, applikationen tager for at svare på en brugers forespørgsel.                                                  | Hvordan kan du optimere forespørgselsbehandling for at forbedre responstiden? |
| **Præcision**                 | Forholdet mellem sande positive forudsigelser og det samlede antal positive forudsigelser.                             | Hvordan vil du validere modellens præcision?                              |
| **Recall (Sensitivitet)**     | Forholdet mellem sande positive forudsigelser og det faktiske antal positive.                                          | Hvordan vil du måle og forbedre recall?                                   |
| **F1-score**                  | Det harmoniske gennemsnit af præcision og recall, der balancerer afvejningen mellem begge.                             | Hvad er din mål-F1-score? Hvordan vil du balancere præcision og recall?   |
| **Perpleksitet**              | Måler, hvor godt sandsynlighedsfordelingen forudsagt af modellen stemmer overens med den faktiske fordeling af data.   | Hvordan vil du minimere perpleksitet?                                     |
| **Brugertilfredshedsmålinger**| Måler brugerens opfattelse af applikationen. Ofte indsamlet gennem undersøgelser.                                      | Hvor ofte vil du indsamle brugerfeedback? Hvordan vil du tilpasse dig baseret på det? |
| **Fejlrate**                  | Raten, hvormed modellen laver fejl i forståelse eller output.                                                          | Hvilke strategier har du på plads for at reducere fejlrater?              |
| **Genoptræningscyklusser**    | Frekvensen, hvormed modellen opdateres for at inkorporere nye data og indsigter.                                       | Hvor ofte vil du genoptræne modellen? Hvad udløser en genoptræningscyklus? |
| **Anomalidetektion**         | Værktøjer og teknikker til at identificere usædvanlige mønstre, der ikke stemmer overens med forventet adfærd.                        | Hvordan vil du reagere på anomalier?                                        |

### Implementering af ansvarlige AI-praksisser i chatapplikationer

Microsofts tilgang til Ansvarlig AI har identificeret seks principper, der bør vejlede udvikling og brug af AI. Nedenfor er principperne, deres definition, og ting en chatudvikler bør overveje samt hvorfor de er vigtige.

| Principper             | Microsofts Definition                                | Overvejelser for Chatudvikler                                      | Hvorfor Det Er Vigtigt                                                                     |
| ---------------------- | ----------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| Retfærdighed           | AI-systemer bør behandle alle mennesker retfærdigt.   | Sørg for, at chatapplikationen ikke diskriminerer baseret på brugerdata. | For at opbygge tillid og inklusivitet blandt brugere; undgår juridiske konsekvenser.       |
| Pålidelighed og Sikkerhed | AI-systemer bør fungere pålideligt og sikkert.        | Implementer test og sikkerhedsforanstaltninger for at minimere fejl og risici. | Sikrer brugerens tilfredshed og forhindrer potentiel skade.                               |
| Privatliv og Sikkerhed | AI-systemer bør være sikre og respektere privatliv.   | Implementer stærk kryptering og databeskyttelsesforanstaltninger.  | For at beskytte følsomme brugerdata og overholde privatlivslovgivning.                    |
| Inklusivitet           | AI-systemer bør styrke alle og engagere mennesker.    | Design UI/UX, der er tilgængelig og nem at bruge for forskellige målgrupper. | Sikrer, at en bredere vifte af mennesker kan bruge applikationen effektivt.               |
| Transparens            | AI-systemer bør være forståelige.                     | Giv klar dokumentation og forklaringer på AI-svar.                 | Brugere er mere tilbøjelige til at stole på et system, hvis de kan forstå, hvordan beslutninger træffes. |
| Ansvarlighed           | Mennesker bør være ansvarlige for AI-systemer.        | Etabler en klar proces for revision og forbedring af AI-beslutninger. | Muliggør løbende forbedring og korrigerende handlinger i tilfælde af fejl.                |

## Opgave

Se [opgave](../../../07-building-chat-applications/python). Den vil tage dig igennem en række øvelser fra at køre dine første chatprompter, til klassificering og opsummering af tekst og mere. Bemærk, at opgaverne er tilgængelige på forskellige programmeringssprog!

## Godt Arbejde! Fortsæt Rejsen

Efter at have afsluttet denne lektion, kan du tjekke vores [Generative AI Learning-samling](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at opbygge din viden om Generativ AI!

Gå videre til Lektion 8 for at se, hvordan du kan begynde [at bygge søgeapplikationer](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.