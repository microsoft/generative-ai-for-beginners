[![Integrering med funksjonskalling](../../../translated_images/no/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Livssyklusen for generative AI-applikasjoner

Et viktig spørsmål for alle AI-applikasjoner er relevansen av AI-funksjoner, siden AI er et raskt utviklende felt. For å sikre at applikasjonen din forblir relevant, pålitelig og robust, må du kontinuerlig overvåke, evaluere og forbedre den. Her kommer livssyklusen for generativ AI inn.

Livssyklusen for generativ AI er et rammeverk som guider deg gjennom stadiene for å utvikle, distribuere og vedlikeholde en generativ AI-applikasjon. Det hjelper deg å definere dine mål, måle ytelsen, identifisere utfordringer og implementere løsninger. Det hjelper deg også å tilpasse applikasjonen til de etiske og juridiske standardene i ditt domene og hos dine interessenter. Ved å følge livssyklusen for generativ AI kan du sikre at applikasjonen alltid leverer verdi og tilfredsstiller brukerne dine.

## Introduksjon

I dette kapittelet vil du:

- Forstå paradigmeskiftet fra MLOps til LLMOps
- LLMs livssyklus
- Verktøy for livssyklusen
- Metrifisering og evaluering i livssyklusen

## Forstå paradigmeskiftet fra MLOps til LLMOps

LLM-er er et nytt verktøy i arsenalet til kunstig intelligens. De er utrolig kraftige i analyse- og generasjonsoppgaver for applikasjoner, men denne kraften har noen konsekvenser for hvordan vi effektiviserer AI og klassiske maskinlæringsoppgaver.

Med dette trenger vi et nytt paradigme for å tilpasse dette verktøyet på en dynamisk måte med de riktige incentivene. Vi kan kategorisere eldre AI-apper som «ML-apper» og nyere AI-apper som «GenAI-apper» eller bare «AI-apper», noe som gjenspeiler den dominerende teknologien og teknikkene som ble brukt på det tidspunktet. Dette endrer vår fortelling på flere måter; se på følgende sammenligning.

![LLMOps vs. MLOps sammenligning](../../../translated_images/no/01-llmops-shift.29bc933cb3bb0080.webp)

Legg merke til at i LLMOps fokuserer vi mer på apputviklerne, bruker integrasjoner som et nøkkelpunkt, bruker «Models-as-a-Service» og tenker på følgende punkter for målinger.

- Kvalitet: Responskvalitet
- Skade: Ansvarlig AI
- Ærlighet: Responsgrunnlag (Gir det mening? Er det korrekt?)
- Kostnad: Løsningsbudsjett
- Forsinkelse: Gjennomsnittlig tid til tokenrespons

## LLMs livssyklus

Først, for å forstå livssyklusen og endringene, la oss se på den neste infografikken.

![LLMOps infografikk](../../../translated_images/no/02-llmops.70a942ead05a7645.webp)

Som du kanskje legger merke til, er dette forskjellig fra de vanlige livssyklusene i MLOps. LLM-er har mange nye krav som prompting, forskjellige teknikker for å forbedre kvalitet (Finjustering, RAG, Meta-prompter), forskjellig vurdering og ansvar med ansvarlig AI, og til slutt nye evalueringsmetrikker (Kvalitet, Skade, Ærlighet, Kostnad og Forsinkelse).

For eksempel, ta en titt på hvordan vi kommer på ideer. Vi bruker promptteknikk for å eksperimentere med ulike LLM-er for å utforske muligheter og teste om hypotesen kan være riktig.

Merk at dette ikke er lineært, men integrerte sløyfer, iterative og med en overordnet syklus.

Hvordan kan vi utforske disse stegene? La oss gå i detalj på hvordan vi kan bygge en livssyklus.

![LLMOps arbeidsflyt](../../../translated_images/no/03-llm-stage-flows.3a1e1c401235a6cf.webp)

Dette kan se litt komplisert ut, la oss fokusere på de tre store stegene først.

1. Idéutvikling/Utforskning: Utforskning, her kan vi utforske etter våre forretningsbehov. Prototyping, lage en [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) og teste om den er effektiv nok for vår hypotese.
1. Bygging/Forbedring: Implementering, nå begynner vi å evaluere for større datasett og implementere teknikker som finjustering og RAG for å sjekke robustheten i løsningen vår. Hvis den ikke fungerer, kan reimplementering, legge til nye steg i flyten eller omstrukturere dataene hjelpe. Etter å ha testet flyten og skalaen, hvis det fungerer og tallene våre ser bra ut, er det klart for neste steg.
1. Operasjonalisering: Integrasjon, nå legger vi til overvåking og varsling til systemet vårt, distribusjon og applikasjonsintegrasjon med appen vår.

Så har vi den overordnede styringssyklusen, med fokus på sikkerhet, samsvar og styring.

Gratulerer, nå har du AI-appen din klar til bruk og drift. For praktisk erfaring, ta en titt på [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)

Nå, hvilke verktøy kan vi bruke?

## Verktøy for livssyklusen

For verktøy tilbyr Microsoft [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) og [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) som gjør syklusen enkel å implementere og klar til bruk.

[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) lar deg bruke [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst). Microsoft Foundry (tidligere Azure AI Studio) er en nettportal som lar deg utforske modeller, eksempler og verktøy, administrere ressursene dine, og bruke UI-utviklingsflyter samt SDK/CLI-alternativer for kodeførst utvikling.

![Muligheter med Azure AI](../../../translated_images/no/04-azure-ai-platform.80203baf03a12fa8.webp)

Azure AI lar deg bruke flere ressurser for å administrere operasjoner, tjenester, prosjekter, vektorsøk og databaser.

![LLMOps med Azure AI](../../../translated_images/no/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

Bygg fra Proof-of-Concept (POC) til storskala applikasjoner med PromptFlow:

- Design og bygg apper fra VS Code, med visuelle og funksjonelle verktøy
- Test og finjuster appene dine for kvalitets-AI, enkelt og greit.
- Bruk Microsoft Foundry for å integrere og iterere med skyen, push og deploy for rask integrasjon.

![LLMOps med PromptFlow](../../../translated_images/no/06-llm-promptflow.a183eba07a3a7fdf.webp)

## Flott! Fortsett læringen din!

Fantastisk, lær nå mer om hvordan vi strukturerer en applikasjon for å bruke konseptene med [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), for å sjekke hvordan Cloud Advocacy legger til disse konseptene i demonstrasjoner. For mer innhold, se vår [Ignite breakout session!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Nå, gå videre til leksjon 15 for å forstå hvordan [Retrieval Augmented Generation og vektordatabaser](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) påvirker generativ AI og for å lage mer engasjerende applikasjoner!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->