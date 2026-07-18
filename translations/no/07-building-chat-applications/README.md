# Bygge Generative AI-Drevne Chatapplikasjoner

[![Building Generative AI-Powered Chat Applications](../../../translated_images/no/07-lesson-banner.a279b937f2843833.webp)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Klikk på bildet over for å se video av denne leksjonen)_

Nå som vi har sett hvordan vi kan bygge tekstgenereringsapper, la oss se nærmere på chatapplikasjoner.

Chatapplikasjoner har blitt integrert i våre daglige liv og tilbyr mer enn bare et middel for uformell samtale. De er en integrert del av kundeservice, teknisk support og til og med sofistikerte rådgivningssystemer. Det er sannsynlig at du nylig har fått hjelp fra en chatapplikasjon. Når vi integrerer mer avansert teknologi som generativ AI i disse plattformene, øker kompleksiteten – og det gjør også utfordringene.

Noen spørsmål vi trenger svar på er:

- **Bygge appen**. Hvordan bygger vi effektivt og integrerer sømløst disse AI-drevne applikasjonene for spesifikke bruksområder?
- **Overvåking**. Når appene er implementert, hvordan kan vi overvåke og sikre at applikasjonene opererer på høyeste kvalitetsnivå, både med hensyn til funksjonalitet og overholdelse av [de seks prinsippene for ansvarlig AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

Når vi beveger oss videre inn i en tidsalder preget av automatisering og sømløse menneske-maskin-interaksjoner, blir forståelsen av hvordan generativ AI transformerer omfanget, dybden og tilpasningsevnen til chatapplikasjoner essensiell. Denne leksjonen vil utforske arkitekturens aspekter som støtter disse komplekse systemene, dykke inn i metodologier for å finjustere dem for domene-spesifikke oppgaver, og evaluere måleparametere og hensyn som er relevante for å sikre ansvarlig AI-implementering.

## Introduksjon

Denne leksjonen dekker:

- Teknikker for effektiv bygging og integrasjon av chatapplikasjoner.
- Hvordan bruke tilpasning og finjustering på applikasjoner.
- Strategier og vurderinger for effektiv overvåking av chatapplikasjoner.

## Læringsmål

Innen slutten av denne leksjonen vil du kunne:

- Beskrive hensyn for bygging og integrering av chatapplikasjoner i eksisterende systemer.
- Tilpasse chatapplikasjoner for spesifikke bruksområder.
- Identifisere nøkkelmålinger og hensyn for å effektivt overvåke og opprettholde kvaliteten på AI-drevne chatapplikasjoner.
- Sikre at chatapplikasjoner utnytter AI på en ansvarlig måte.

## Integrering av Generativ AI i Chatapplikasjoner

Å løfte chatapplikasjoner gjennom generativ AI handler ikke bare om å gjøre dem smartere; det handler om å optimalisere arkitektur, ytelse og brukergrensesnitt for å levere en kvalitetsopplevelse til brukeren. Dette innebærer å undersøke arkitektoniske grunnlag, API-integrasjoner, og hensyn rundt brukergrensesnittet. Denne delen har som mål å gi deg en omfattende veikart for å navigere i disse komplekse landskapene, enten du kobler dem til eksisterende systemer eller bygger dem som frittstående plattformer.

Innen slutten av denne delen vil du være utstyrt med ekspertisen som trengs for effektivt å konstruere og inkorporere chatapplikasjoner.

### Chatbot eller Chatapplikasjon?

Før vi dykker inn i byggingen av chatapplikasjoner, la oss sammenligne 'chatbots' med 'AI-drevne chatapplikasjoner', som har ulike roller og funksjonaliteter. En chatbot sin hovedhensikt er å automatisere spesifikke samtaleoppgaver, som å svare på ofte stilte spørsmål eller spore en pakke. Den styres vanligvis av regelbasert logikk eller komplekse AI-algoritmer. I kontrast er en AI-drevet chatapplikasjon et mye mer omfattende miljø designet for å fasilitere ulike former for digital kommunikasjon, slik som tekst-, tale- og videosamtaler blant menneskelige brukere. Dets definerende trekk er integreringen av en generativ AI-modell som simulerer nyanserte, menneskelignende samtaler, og genererer svar basert på et bredt spekter av innspill og kontekstuelle ledetråder. En generativ AI-drevet chatapplikasjon kan delta i åpne diskusjoner, tilpasse seg et utviklende samtalekontekst, og til og med produsere kreative eller komplekse dialoger.

Tabellen nedenfor skisserer nøkkelforskjellene og likhetene for å hjelpe oss å forstå deres unike roller i digital kommunikasjon.

| Chatbot                               | Generativ AI-Drevet Chatapplikasjon   |
| ------------------------------------- | -------------------------------------- |
| Oppgavefokusert og regelbasert       | Kontekstbevisst                        |
| Ofte integrert i større systemer      | Kan huse én eller flere chatboter       |
| Begrenset til programmerte funksjoner| Inkluderer generative AI-modeller       |
| Spesialiserte & strukturerte interaksjoner | Kapabel til åpne diskusjoner            |

### Utnytte ferdigbygde funksjoner med SDK-er og API-er

Når du bygger en chatapplikasjon, er et godt første steg å vurdere hva som allerede finnes. Bruk av SDK-er og API-er for å bygge chatapplikasjoner er en fordelaktig strategi av flere grunner. Ved å integrere veldokumenterte SDK-er og API-er plasserer du applikasjonen strategisk for langsiktig suksess, og adresserer skalerbarhet og vedlikehold.

- **Fremskynder utviklingsprosessen og reduserer overhead**: Å stole på ferdigbygde funksjonaliteter i stedet for den kostbare prosessen med å bygge dem selv, tillater deg å fokusere på andre aspekter ved applikasjonen som du kanskje finner viktigere, slik som forretningslogikk.
- **Bedre ytelse**: Når du bygger funksjonalitet fra bunnen av, vil du etter hvert spørre: "Hvordan skalerer dette? Er denne applikasjonen i stand til å håndtere en plutselig økning i brukere?" Velholdte SDK-er og API-er har ofte innebygde løsninger for slike utfordringer.
- **Enklere vedlikehold**: Oppdateringer og forbedringer er lettere å håndtere da de fleste API-er og SDK-er bare krever oppdatering av et bibliotek når en nyere versjon slippes.
- **Tilgang til banebrytende teknologi**: Å utnytte modeller som er finjustert og trent på omfattende datasett gir applikasjonen dine naturlige språkferdigheter.

Tilgang til funksjonaliteten til en SDK eller API innebærer vanligvis å få tillatelse til å bruke tjenestene som tilbys, ofte gjennom bruk av en unik nøkkel eller autentiseringstoken. Vi vil bruke OpenAI Python-biblioteket for å utforske hvordan dette ser ut. Du kan også prøve det selv i følgende [notatbok for OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) eller [notatbok for Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) for denne leksjonen.

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

Eksemplet over bruker GPT-5 mini-modellen med Responses API for å fullføre prompten, men merk at API-nøkkelen er satt før det. Du vil få en feil hvis du ikke setter nøkkelen.

## Brukeropplevelse (UX)

Generelle UX-prinsipper gjelder for chatapplikasjoner, men her er noen tilleggshensyn som blir spesielt viktige på grunn av maskinlæringskomponentene som er involvert.

- **Mekanisme for å håndtere tvetydighet**: Generative AI-modeller kan av og til generere tvetydige svar. En funksjon som lar brukere be om avklaring kan være nyttig dersom de møter dette problemet.
- **Kontekstbevaring**: Avanserte generative AI-modeller har evnen til å huske kontekst innen en samtale, noe som kan være en nødvendig ressurs for brukeropplevelsen. Å gi brukerne muligheten til å kontrollere og administrere kontekst forbedrer brukeropplevelsen, men introduserer risikoen for lagring av sensitiv brukerinformasjon. Vurderinger rundt hvor lenge denne informasjonen lagres, slik som innføring av en lagringspolicy, kan balansere behovet for kontekst mot personvern.
- **Personalisering**: Med evnen til å lære og tilpasse seg tilbyr AI-modeller en individualisert opplevelse for brukeren. Skreddersying av brukeropplevelsen gjennom funksjoner som brukerprofiler gjør ikke bare at brukeren føler seg forstått, men hjelper også i jakten på å finne spesifikke svar, noe som skaper en mer effektiv og tilfredsstillende interaksjon.

Et eksempel på personalisering er "Custom instructions" (egendefinerte instruksjoner)-innstillingene i OpenAI sin ChatGPT. Den lar deg gi informasjon om deg selv som kan være viktig kontekst for dine prompt. Her er et eksempel på en egendefinert instruksjon.

![Custom Instructions Settings in ChatGPT](../../../translated_images/no/custom-instructions.b96f59aa69356fcf.webp)

Denne "profilen" ber ChatGPT lage en leksjonsplan om lenkede lister. Legg merke til at ChatGPT tar hensyn til at brukeren kan ønske en mer dyptgående leksjonsplan basert på hennes erfaring.

![A prompt in ChatGPT for a lesson plan about linked lists](../../../translated_images/no/lesson-plan-prompt.cc47c488cf1343df.webp)

### Microsofts System Message Framework for Store Språkmodeller

[Microsoft har gitt veiledning](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) for å skrive effektive systemmeldinger når man genererer svar fra LLM-er, delt inn i 4 områder:

1. Definere hvem modellen er for, samt dens evner og begrensninger.
2. Definere modellens utdataformat.
3. Gi konkrete eksempler som demonstrerer modellens ønskede oppførsel.
4. Gi tilleggsguider for oppførsel.

### Tilgjengelighet

Enten en bruker har visuelle, auditive, motoriske eller kognitive funksjonsnedsettelser, bør en godt designet chatapplikasjon kunne brukes av alle. Følgende liste bryter ned spesifikke funksjoner som har som mål å forbedre tilgjengeligheten for ulike brukerbegrensninger.

- **Funksjoner for synshemmede**: Temaer med høy kontrast og justerbar tekststørrelse, kompatibilitet med skjermleser.
- **Funksjoner for hørselshemmede**: Tekst-til-tale og tale-til-tekst-funksjoner, visuelle signaler for lydvarsler.
- **Funksjoner for motoriske funksjonsnedsettelser**: Støtte for tastaturnavigasjon, stemmekommandoer.
- **Funksjoner for kognitive funksjonsnedsettelser**: Forenklede språkvalg.

## Tilpasning og finjustering for domene-spesifikke språkmodeller

Tenk deg en chatapplikasjon som forstår selskapets sjargong og forutser de spesifikke spørsmål brukerne ofte har. Det finnes et par tilnærminger verdt å nevne:

- **Utnytte DSL-modeller**. DSL står for Domain Specific Language (domene-spesifikt språk). Du kan utnytte en såkalt DSL-modell trent på et spesifikt domene for å forstå dets konsepter og scenarioer.
- **Bruke finjustering**. Finjustering er prosessen med å trene modellen ytterligere med spesifikke data.

## Tilpasning: Bruke en DSL

Å utnytte domene-spesifikke språkmodeller (DSL-modeller) kan øke brukerengasjementet ved å tilby spesialiserte, kontekstrelevante interaksjoner. Det er en modell som er trent eller finjustert for å forstå og generere tekst relatert til et spesifikt felt, industri eller emne. Mulighetene for å bruke en DSL-modell kan variere fra å trene en fra bunnen av til å bruke eksisterende gjennom SDK-er og API-er. Et annet alternativ er finjustering, som innebærer å ta en eksisterende forhåndstrent modell og tilpasse den til et spesifikt domene.

## Tilpasning: Anvende finjustering

Finjustering vurderes ofte når en forhåndstrent modell ikke strekker til i et spesialisert domene eller spesifikk oppgave.

For eksempel er medisinske spørsmål komplekse og krever mye kontekst. Når en medisinsk fagperson stiller diagnose, baserer det seg på en rekke faktorer som livsstil eller eksisterende tilstander, og kan til og med basere seg på nyere medisinske tidsskrifter for å validere diagnosen. I slike nyanserte scenarioer kan ikke en AI-chatapplikasjon med generelt formål være en pålitelig kilde.

### Scenario: en medisinsk applikasjon

Tenk på en chatapplikasjon designet for å hjelpe medisinske fagfolk ved å gi raske referanser til behandlingsretningslinjer, legemiddelinteraksjoner eller nylige forskningsresultater.

En generell modell kan være adekvat for å svare på grunnleggende medisinske spørsmål eller gi generell rådgivning, men kan slite med følgende:

- **Svært spesifikke eller komplekse saker**. For eksempel kan en nevrolog spørre applikasjonen: "Hva er dagens beste praksis for håndtering av medikamentresistent epilepsi hos pediatriske pasienter?"
- **Manglende nyere fremskritt**. En generell modell kan slite med å gi et oppdatert svar som inkluderer de nyeste fremskrittene innen nevrologi og farmakologi.

I slike tilfeller kan finjustering av modellen med et spesialisert medisinsk datasett betydelig forbedre dens evne til å håndtere disse intrikate medisinske henvendelsene mer nøyaktig og pålitelig. Dette krever tilgang til et stort og relevant datasett som representerer domene-spesifikke utfordringer og spørsmål som må adresseres.

## Vurderinger for en høy kvalitets AI-drevet chatteopplevelse

Denne delen skisserer kriteriene for «høykvalitets» chatapplikasjoner, som inkluderer innsamling av handlingsrettede måleparametere og overholdelse av et rammeverk som ansvarlig utnytter AI-teknologi.

### Viktige måleparametere

For å opprettholde høy ytelse i en applikasjon er det viktig å holde oversikt over nøkkelmålinger og hensyn. Disse målingene sikrer ikke bare funksjonaliteten i applikasjonen, men vurderer også kvaliteten på AI-modellen og brukeropplevelsen. Nedenfor er en liste som dekker grunnleggende, AI- og brukeropplevelsesmål som bør vurderes.

| Måling                       | Definisjon                                                                                                            | Vurderinger for utvikler av chat                                |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Oppetid**                  | Måler hvor lenge applikasjonen er operativ og tilgjengelig for brukere.                                               | Hvordan vil du minimere nedetid?                                |
| **Responstid**               | Tiden applikasjonen bruker på å svare på en brukers forespørsel.                                                      | Hvordan kan du optimalisere spørringsbehandling for bedre responstid? |
| **Presisjon**                | Forholdet mellom sanne positive prediksjoner og totalt antall positive prediksjoner.                                  | Hvordan vil du validere presisjonen til modellen din?          |
| **Recall (Sensitivitet)**    | Forholdet mellom sanne positive prediksjoner og det faktiske antallet positive.                                       | Hvordan vil du måle og forbedre recall?                        |
| **F1 Score**                | Det harmoniske gjennomsnittet av presisjon og recall, som balanserer kompromisset mellom begge.                      | Hva er ditt mål for F1 Score? Hvordan vil du balansere presisjon og recall? |
| **Perpleksitet**             | Måler hvor godt sannsynlighetsfordelingen som modellen forutsier stemmer overens med den faktiske datafordelingen.   | Hvordan vil du minimere perpleksitet?                          |
| **Brukertilfredshet**        | Måler brukerens oppfatning av applikasjonen. Ofte innhentet gjennom undersøkelser.                                   | Hvor ofte vil du samle inn brukerfeedback? Hvordan vil du tilpasse deg basert på den? |
| **Feilrate**                 | Hvor ofte modellen gjør feil i forståelse eller output.                                                              | Hvilke strategier har du for å redusere feilrater?            |
| **Omtrentingssykluser**      | Hyppigheten modellen oppdateres for å inkludere nye data og innsikter.                                                | Hvor ofte vil du omskolere modellen? Hva utløser en ny opplæringssyklus? |

| **Avviksdeteksjon**         | Verktøy og teknikker for å identifisere uvanlige mønstre som ikke samsvarer med forventet oppførsel.                        | Hvordan vil du svare på avvik?                                        |

### Implementering av Ansvarlige AI-praksiser i Chat-applikasjoner

Microsofts tilnærming til Ansvarlig AI har identifisert seks prinsipper som bør veilede utvikling og bruk av AI. Nedenfor er prinsippene, deres definisjon, og ting en chat-utvikler bør vurdere og hvorfor de bør ta dem på alvor.

| Prinsipper             | Microsofts definisjon                                | Vurderinger for Chat-utvikler                                      | Hvorfor det er viktig                                                                     |
| ---------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Rettferdighet               | AI-systemer bør behandle alle mennesker rettferdig.            | Sørg for at chat-applikasjonen ikke diskriminerer basert på brukerdata.  | For å bygge tillit og inkludering blant brukere; unngår juridiske konsekvenser.                |
| Pålitelighet og sikkerhet | AI-systemer bør fungere pålitelig og sikkert.        | Implementer testing og failsafe-mekanismer for å minimere feil og risiko.         | Sikrer brukertilfredshet og forhindrer potensiell skade.                                 |
| Personvern og sikkerhet   | AI-systemer bør være sikre og respektere personvernet.      | Implementer sterk kryptering og databeskyttelsestiltak.              | For å beskytte sensitiv brukerdata og overholde personvernlovgivning.                         |
| Inkludering          | AI-systemer bør styrke alle og engasjere folk. | Design UI/UX som er tilgjengelig og enkel å bruke for ulike målgrupper. | Sikrer at et bredere spekter av mennesker kan bruke applikasjonen effektivt.                   |
| Åpenhet           | AI-systemer bør være forståelige.                  | Gi klar dokumentasjon og begrunnelse for AI-responsene.            | Brukere er mer tilbøyelige til å stole på et system hvis de kan forstå hvordan beslutninger tas. |
| Ansvarlighet         | Folk bør være ansvarlige for AI-systemer.          | Etabler en klar prosess for revisjon og forbedring av AI-beslutninger.     | Muliggjør kontinuerlig forbedring og korrigerende tiltak ved feil.               |

## Oppgave

Se [assignment](../../../07-building-chat-applications/python). Den vil ta deg gjennom en serie øvelser fra å kjøre dine første chat-prompt, til å klassifisere og oppsummere tekst og mer. Legg merke til at oppgavene er tilgjengelige på forskjellige programmeringsspråk!

## Flott arbeid! Fortsett reisen

Etter å ha fullført denne leksjonen, sjekk ut vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å utvikle din kunnskap om Generativ AI!

Gå videre til Lekse 8 for å se hvordan du kan begynne å [bygge søkeapplikasjoner](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->