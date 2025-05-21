<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-05-19T14:42:24+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "no"
}
-->
# Bruke generativ AI på en ansvarlig måte

> _Klikk på bildet over for å se videoen av denne leksjonen_

Det er lett å bli fascinert av AI og spesielt generativ AI, men du må vurdere hvordan du bruker det ansvarlig. Du må tenke på ting som hvordan du sikrer at resultatene er rettferdige, ikke-skadelige og mer. Dette kapittelet har som mål å gi deg den nevnte konteksten, hva du bør vurdere, og hvordan du kan ta aktive steg for å forbedre din AI-bruk.

## Introduksjon

Denne leksjonen vil dekke:

- Hvorfor du bør prioritere ansvarlig AI når du bygger generative AI-applikasjoner.
- Kjerneprinsippene for ansvarlig AI og hvordan de relaterer seg til generativ AI.
- Hvordan sette disse prinsippene for ansvarlig AI ut i praksis gjennom strategi og verktøy.

## Læringsmål

Etter å ha fullført denne leksjonen vil du vite:

- Viktigheten av ansvarlig AI når du bygger generative AI-applikasjoner.
- Når du skal tenke på og anvende kjerneprinsippene for ansvarlig AI når du bygger generative AI-applikasjoner.
- Hvilke verktøy og strategier som er tilgjengelige for deg for å sette konseptet ansvarlig AI ut i praksis.

## Prinsipper for ansvarlig AI

Spenningsnivået rundt generativ AI har aldri vært høyere. Denne spenningen har brakt mange nye utviklere, oppmerksomhet og finansiering til dette området. Selv om dette er veldig positivt for alle som ønsker å bygge produkter og selskaper ved hjelp av generativ AI, er det også viktig at vi går frem på en ansvarlig måte.

Gjennom dette kurset fokuserer vi på å bygge vår oppstart og vårt AI-utdanningsprodukt. Vi vil bruke prinsippene for ansvarlig AI: Rettferdighet, Inkludering, Pålitelighet/Sikkerhet, Sikkerhet og Personvern, Åpenhet og Ansvarlighet. Med disse prinsippene vil vi utforske hvordan de relaterer seg til vår bruk av generativ AI i våre produkter.

## Hvorfor bør du prioritere ansvarlig AI

Når du bygger et produkt, vil det å ta en menneskesentrert tilnærming ved å ha brukerens beste interesse i tankene føre til de beste resultatene.

Det unike ved generativ AI er dens evne til å skape nyttige svar, informasjon, veiledning og innhold for brukerne. Dette kan gjøres uten mange manuelle steg som kan føre til svært imponerende resultater. Uten riktig planlegging og strategier kan det dessverre også føre til noen skadelige resultater for brukerne dine, produktet ditt og samfunnet som helhet.

La oss se på noen (men ikke alle) av disse potensielt skadelige resultatene:

### Hallusinasjoner

Hallusinasjoner er et begrep som brukes for å beskrive når en LLM produserer innhold som enten er helt meningsløst eller noe vi vet er faktuelt feil basert på andre informasjonskilder.

La oss for eksempel si at vi bygger en funksjon for vår oppstart som lar studenter stille historiske spørsmål til en modell. En student stiller spørsmålet `Who was the sole survivor of Titanic?`

Modellen produserer et svar som det nedenfor:

Dette er et veldig selvsikkert og grundig svar. Dessverre er det feil. Selv med en minimal mengde forskning, ville man oppdage at det var mer enn én overlevende fra Titanic-katastrofen. For en student som nettopp begynner å forske på dette emnet, kan dette svaret være overbevisende nok til å ikke bli stilt spørsmål ved og behandlet som en fakta. Konsekvensene av dette kan føre til at AI-systemet blir upålitelig og påvirker oppstartens omdømme negativt.

Med hver iterasjon av en gitt LLM, har vi sett ytelsesforbedringer rundt å minimere hallusinasjoner. Selv med denne forbedringen, må vi som applikasjonsbyggere og brukere fortsatt være oppmerksomme på disse begrensningene.

### Skadelig innhold

Vi dekket i den tidligere delen når en LLM produserer feil eller meningsløse svar. En annen risiko vi må være klar over er når en modell svarer med skadelig innhold.

Skadelig innhold kan defineres som:

- Å gi instruksjoner eller oppmuntre til selvskading eller skade på visse grupper.
- Hatefulle eller nedsettende innhold.
- Veiledning i planlegging av angrep eller voldelige handlinger.
- Å gi instruksjoner om hvordan man finner ulovlig innhold eller begår ulovlige handlinger.
- Vise seksuelt eksplisitt innhold.

For vår oppstart, ønsker vi å sikre at vi har de riktige verktøyene og strategiene på plass for å forhindre at denne typen innhold blir sett av studenter.

### Mangel på rettferdighet

Rettferdighet er definert som "å sikre at et AI-system er fritt for skjevhet og diskriminering og at de behandler alle rettferdig og likt." I verden av generativ AI ønsker vi å sikre at ekskluderende verdenssyn av marginaliserte grupper ikke blir forsterket av modellens output.

Disse typer output er ikke bare destruktive for å bygge positive produktopplevelser for brukerne våre, men de forårsaker også ytterligere samfunnsskader. Som applikasjonsbyggere bør vi alltid ha et bredt og mangfoldig brukergrunnlag i tankene når vi bygger løsninger med generativ AI.

## Hvordan bruke generativ AI ansvarlig

Nå som vi har identifisert viktigheten av ansvarlig generativ AI, la oss se på 4 steg vi kan ta for å bygge våre AI-løsninger ansvarlig:

### Måle potensielle skader

I programvaretesting tester vi de forventede handlingene til en bruker på en applikasjon. Tilsvarende er det å teste et mangfoldig sett med forespørsler brukere mest sannsynlig vil bruke en god måte å måle potensielle skader på.

Siden vår oppstart bygger et utdanningsprodukt, ville det være bra å forberede en liste over utdanningsrelaterte forespørsler. Dette kan være for å dekke et bestemt emne, historiske fakta, og forespørsler om studentlivet.

### Begrense potensielle skader

Det er nå på tide å finne måter hvor vi kan forhindre eller begrense den potensielle skaden forårsaket av modellen og dens svar. Vi kan se på dette i 4 forskjellige lag:

- **Modell**. Velge riktig modell for riktig brukstilfelle. Større og mer komplekse modeller som GPT-4 kan forårsake mer risiko for skadelig innhold når de brukes på mindre og mer spesifikke brukstilfeller. Å bruke treningsdataene dine til finjustering reduserer også risikoen for skadelig innhold.

- **Sikkerhetssystem**. Et sikkerhetssystem er et sett med verktøy og konfigurasjoner på plattformen som serverer modellen som hjelper til med å begrense skade. Et eksempel på dette er innholdsfiltreringssystemet på Azure OpenAI-tjenesten. Systemer bør også oppdage jailbreak-angrep og uønsket aktivitet som forespørsler fra roboter.

- **Metaprompt**. Metaprompts og grunnlag er måter vi kan dirigere eller begrense modellen basert på visse atferder og informasjon. Dette kan være å bruke systeminnganger til å definere visse grenser for modellen. I tillegg kan det være å gi output som er mer relevant for omfanget eller domenet til systemet.

Det kan også være å bruke teknikker som Retrieval Augmented Generation (RAG) for å få modellen til å kun hente informasjon fra et utvalg av pålitelige kilder. Det er en leksjon senere i dette kurset for [å bygge søkeapplikasjoner](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Brukeropplevelse**. Det siste laget er der brukeren samhandler direkte med modellen gjennom vår applikasjonsgrensesnitt på en eller annen måte. På denne måten kan vi designe UI/UX for å begrense brukeren på typene input de kan sende til modellen, samt tekst eller bilder vist til brukeren. Når vi distribuerer AI-applikasjonen, må vi også være transparente om hva vår generative AI-applikasjon kan og ikke kan gjøre.

Vi har en hel leksjon dedikert til [å designe UX for AI-applikasjoner](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Evaluere modell**. Å jobbe med LLM-er kan være utfordrende fordi vi ikke alltid har kontroll over dataene modellen ble trent på. Uansett bør vi alltid evaluere modellens ytelse og output. Det er fortsatt viktig å måle modellens nøyaktighet, likhet, jordnærhet og relevans av output. Dette bidrar til å gi åpenhet og tillit til interessenter og brukere.

### Drifte en ansvarlig generativ AI-løsning

Å bygge en operasjonell praksis rundt dine AI-applikasjoner er det siste stadiet. Dette inkluderer å samarbeide med andre deler av vår oppstart som juridisk og sikkerhet for å sikre at vi er i samsvar med alle regulatoriske retningslinjer. Før lansering ønsker vi også å bygge planer rundt levering, håndtering av hendelser og tilbakeføring for å forhindre enhver skade for våre brukere fra å vokse.

## Verktøy

Selv om arbeidet med å utvikle ansvarlige AI-løsninger kan virke som mye, er det arbeid vel verdt innsatsen. Etter hvert som området generativ AI vokser, vil flere verktøy for å hjelpe utviklere med å effektivt integrere ansvarlighet i sine arbeidsflyter modnes. For eksempel kan [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) hjelpe med å oppdage skadelig innhold og bilder via en API-forespørsel.

## Kunnskapssjekk

Hva er noen ting du må bry deg om for å sikre ansvarlig AI-bruk?

1. At svaret er riktig.
1. Skadelig bruk, at AI ikke brukes til kriminelle formål.
1. Sikre at AI er fri for skjevhet og diskriminering.

A: 2 og 3 er riktige. Ansvarlig AI hjelper deg med å vurdere hvordan du kan begrense skadelige effekter og skjevheter og mer.

## 🚀 Utfordring

Les om [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) og se hva du kan ta i bruk for din bruk.

## Flott arbeid, fortsett læringen din

Etter å ha fullført denne leksjonen, sjekk ut vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å heve din kunnskap om generativ AI!

Gå videre til leksjon 4 hvor vi vil se på [Grunnleggende om prompt engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

**Ansvarsfraskrivelse**:  
Dette dokumentet har blitt oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.