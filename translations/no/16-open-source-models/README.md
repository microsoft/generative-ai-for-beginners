<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85b754d4dc980f270f264d17116d9a5f",
  "translation_date": "2025-12-19T15:33:15+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "no"
}
-->
[![Open Source Models](../../../translated_images/16-lesson-banner.6b56555e8404fda1.no.png)](https://youtu.be/CuICgfuHFSg?si=x8SpFRUsIxM9dohN)

## Introduksjon

Verden av åpne LLM-er er spennende og i stadig utvikling. Denne leksjonen har som mål å gi en grundig gjennomgang av åpne modeller. Hvis du leter etter informasjon om hvordan proprietære modeller sammenlignes med åpne modeller, gå til ["Utforske og sammenligne forskjellige LLM-er"-leksjonen](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Denne leksjonen vil også dekke temaet finjustering, men en mer detaljert forklaring finnes i ["Finjustering av LLM-er"-leksjonen](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Læringsmål

- Få en forståelse av åpne modeller
- Forstå fordelene ved å jobbe med åpne modeller
- Utforske de åpne modellene som er tilgjengelige på Hugging Face og Azure AI Studio

## Hva er åpne modeller?

Åpen kildekode-programvare har spilt en avgjørende rolle i veksten av teknologi på tvers av ulike felt. Open Source Initiative (OSI) har definert [10 kriterier for programvare](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) for å bli klassifisert som åpen kildekode. Kildekoden må deles åpent under en lisens godkjent av OSI.

Selv om utviklingen av LLM-er har lignende elementer som programvareutvikling, er prosessen ikke helt den samme. Dette har ført til mye diskusjon i miljøet om definisjonen av åpen kildekode i konteksten av LLM-er. For at en modell skal være i tråd med den tradisjonelle definisjonen av åpen kildekode, bør følgende informasjon være offentlig tilgjengelig:

- Datasett brukt til å trene modellen.
- Fullstendige modellvekter som en del av treningen.
- Evalueringskoden.
- Finjusteringskoden.
- Fullstendige modellvekter og treningsmetrikker.

Det finnes for øyeblikket bare noen få modeller som oppfyller disse kriteriene. [OLMo-modellen laget av Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) er en som passer i denne kategorien.

For denne leksjonen vil vi referere til modellene som "åpne modeller" videre, da de kanskje ikke oppfyller kriteriene ovenfor på tidspunktet for skriving.

## Fordeler med åpne modeller

**Høyt tilpassbare** – Siden åpne modeller slippes med detaljert treningsinformasjon, kan forskere og utviklere endre modellens indre. Dette muliggjør opprettelse av høyt spesialiserte modeller som er finjustert for en spesifikk oppgave eller studieområde. Noen eksempler på dette er kodegenerering, matematiske operasjoner og biologi.

**Kostnad** – Kostnaden per token for bruk og distribusjon av disse modellene er lavere enn for proprietære modeller. Når man bygger generative AI-applikasjoner, bør man vurdere ytelse versus pris når man jobber med disse modellene for sitt brukstilfelle.

![Model Cost](../../../translated_images/model-price.3f5a3e4d32ae00b4.no.png)
Kilde: Artificial Analysis

**Fleksibilitet** – Å jobbe med åpne modeller gir deg fleksibilitet når det gjelder å bruke forskjellige modeller eller kombinere dem. Et eksempel på dette er [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst) hvor en bruker kan velge modellen som brukes direkte i brukergrensesnittet:

![Choose Model](../../../translated_images/choose-model.f095d15bbac92214.no.png)

## Utforske forskjellige åpne modeller

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), utviklet av Meta, er en åpen modell som er optimalisert for chattebaserte applikasjoner. Dette skyldes finjusteringsmetoden, som inkluderte en stor mengde dialog og menneskelig tilbakemelding. Med denne metoden produserer modellen flere resultater som er i tråd med menneskelige forventninger, noe som gir en bedre brukeropplevelse.

Noen eksempler på finjusterte versjoner av Llama inkluderer [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), som spesialiserer seg på japansk, og [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), som er en forbedret versjon av basismodellen.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) er en åpen modell med sterkt fokus på høy ytelse og effektivitet. Den bruker Mixture-of-Experts-tilnærmingen som kombinerer en gruppe spesialiserte ekspertmodeller til ett system hvor visse modeller velges ut basert på input. Dette gjør beregningen mer effektiv ettersom modellene kun håndterer de inputtene de er spesialisert på.

Noen eksempler på finjusterte versjoner av Mistral inkluderer [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), som fokuserer på medisinsk domene, og [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), som utfører matematiske beregninger.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) er en LLM laget av Technology Innovation Institute (**TII**). Falcon-40B ble trent på 40 milliarder parametere og har vist seg å prestere bedre enn GPT-3 med lavere beregningsbudsjett. Dette skyldes bruken av FlashAttention-algoritmen og multiquery attention som reduserer minnekravene ved inferenstid. Med denne reduserte inferansetiden er Falcon-40B egnet for chatteapplikasjoner.

Noen eksempler på finjusterte versjoner av Falcon er [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), en assistent bygget på åpne modeller, og [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), som leverer høyere ytelse enn basismodellen.

## Hvordan velge

Det finnes ikke ett svar på hvordan man velger en åpen modell. Et godt sted å starte er å bruke Azure AI Studios filterfunksjon etter oppgave. Dette vil hjelpe deg å forstå hvilke typer oppgaver modellen er trent for. Hugging Face vedlikeholder også en LLM-ledertavle som viser de best presterende modellene basert på visse metrikker.

Når du ønsker å sammenligne LLM-er på tvers av forskjellige typer, er [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) en annen flott ressurs:

![Model Quality](../../../translated_images/model-quality.aaae1c22e00f7ee1.no.png)
Kilde: Artificial Analysis

Hvis du jobber med et spesifikt brukstilfelle, kan det være effektivt å søke etter finjusterte versjoner som fokuserer på samme område. Å eksperimentere med flere åpne modeller for å se hvordan de presterer i henhold til dine og brukernes forventninger er også en god praksis.

## Neste steg

Det beste med åpne modeller er at du kan komme i gang med dem ganske raskt. Sjekk ut [Azure AI Foundry Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), som har en spesifikk Hugging Face-samling med disse modellene vi har diskutert her.

## Læring stopper ikke her, fortsett reisen

Etter å ha fullført denne leksjonen, sjekk ut vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å øke din kunnskap om generativ AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->