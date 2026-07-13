[![Integration med funktionsopkald](../../../translated_images/da/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Livscyklussen for Generative AI-applikationer

Et vigtigt spørgsmål for alle AI-applikationer er relevansen af AI-funktioner, da AI er et hurtigt udviklende felt; for at sikre, at din applikation forbliver relevant, pålidelig og robust, skal du overvåge, evaluere og forbedre den kontinuerligt. Det er her, den generative AI-livscyklus kommer ind i billedet.

Den generative AI-livscyklus er en ramme, der guider dig gennem stadierne ved udvikling, implementering og vedligeholdelse af en generativ AI-applikation. Den hjælper dig med at definere dine mål, måle din ydelse, identificere dine udfordringer og implementere dine løsninger. Den hjælper dig også med at tilpasse din applikation med de etiske og juridiske standarder inden for dit område og dine interessenter. Ved at følge den generative AI-livscyklus kan du sikre, at din applikation altid leverer værdi og tilfredsstiller dine brugere.

## Introduktion

I dette kapitel vil du:

- Forstå paradigmeskiftet fra MLOps til LLMOps
- LLM-livscyklussen
- Værktøjer til livscyklus
- Metrificering og evaluering af livscyklus

## Forstå paradigmeskiftet fra MLOps til LLMOps

LLM'er er et nyt værktøj i det kunstige intelligens arsenal; de er utroligt kraftfulde til analyse- og genereringsopgaver for applikationer, men denne kraft har nogle konsekvenser for, hvordan vi strømliner AI og klassiske maskinlæringsopgaver.

Derfor har vi brug for et nyt paradigme for at tilpasse dette værktøj dynamisk med de rigtige incitamenter. Vi kan kategorisere ældre AI-apps som "ML Apps" og nyere AI Apps som "GenAI Apps" eller blot "AI Apps" for at afspejle den dominerende teknologi og de teknikker, der anvendes på det tidspunkt. Dette ændrer vores fortælling på flere måder; se på følgende sammenligning.

![LLMOps vs. MLOps sammenligning](../../../translated_images/da/01-llmops-shift.29bc933cb3bb0080.webp)

Bemærk, at i LLMOps fokuserer vi mere på app-udviklerne, bruger integrationer som en nøglefaktor, anvender "Modeller-som-en-Service" og tænker på følgende punkter for metrics.

- Kvalitet: Svar-kvalitet
- Skade: Ansvarlig AI
- Ærlighed: Svar-basering (Giver det mening? Er det korrekt?)
- Omkostning: Løsningsbudget
- Latens: Gennemsnitlig tid for token-svar

## LLM-livscyklussen

Først, for at forstå livscyklussen og ændringerne, lad os bemærke den næste infografik.

![LLMOps infografik](../../../translated_images/da/02-llmops.70a942ead05a7645.webp)

Som du måske bemærker, er dette forskelligt fra de sædvanlige livscyklusser for MLOps. LLM'er har mange nye krav som prompting, forskellige teknikker til at forbedre kvaliteten (fine-tuning, RAG, meta-prompts), andet ansvar og vurdering med ansvarlig AI, og endelig nye evalueringsmetrikker (kvalitet, skade, ærlighed, omkostning og latens).

For eksempel, se på hvordan vi idéudvikler. Ved brug af prompt engineering eksperimenterer vi med forskellige LLM'er for at udforske muligheder og teste, om deres hypotese kan være korrekt.

Bemærk at dette ikke er lineært, men integrerede loops, iterative og med en overordnet cyklus.

Hvordan kunne vi udforske disse trin? Lad os gå i detaljer om, hvordan vi kunne opbygge en livscyklus.

![LLMOps workflow](../../../translated_images/da/03-llm-stage-flows.3a1e1c401235a6cf.webp)

Dette kan se noget kompliceret ud, lad os først fokusere på de tre store trin.

1. Idéudvikling/udforskning: Udforskning, her kan vi undersøge efter vores forretningsbehov. Prototyping, lave en [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) og teste, om den er effektiv nok til vores hypotese.
1. Opbygning/udvidelse: Implementering, nu begynder vi at evaluere for større datasæt, anvende teknikker som fine-tuning og RAG for at tjekke robustheden af vores løsning. Hvis den ikke er det, kan genimplementering, tilføjelse af nye trin i vores flow eller omstrukturering af data hjælpe. Efter test af flow og skala, hvis det virker og vores metrics godkendes, er det klar til næste trin.
1. Driftssætning: Integration, nu tilføjes overvågnings- og alarmsystemer til vores system, implementering og applikationsintegration til vores applikation.

Derefter har vi den overordnede styringscyklus, der fokuserer på sikkerhed, overholdelse og governance.

Tillykke, nu har du din AI-app klar til at køre og være operationel. Til en praktisk oplevelse, kig på [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)

Hvilke værktøjer kan vi bruge?

## Værktøjer til livscyklus

Til værktøjer tilbyder Microsoft [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) og [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) forenkler og gør din cyklus nem at implementere og klar til brug.

[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) giver dig mulighed for at bruge [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst). Microsoft Foundry (tidligere Azure AI Studio) er en webportal, der lader dig udforske modeller, eksempler og værktøjer, administrere dine ressourcer og bruge UI-udviklingsflows samt SDK/CLI-muligheder til code-first udvikling.

![Azure AI muligheder](../../../translated_images/da/04-azure-ai-platform.80203baf03a12fa8.webp)

Azure AI giver dig mulighed for at bruge flere ressourcer til at styre dine operationer, tjenester, projekter, vektorsøg og databasebehov.

![LLMOps med Azure AI](../../../translated_images/da/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

Byg fra proof-of-concept (POC) til storskalaanvendelser med PromptFlow:

- Design og opbyg applikationer fra VS Code med visuelle og funktionelle værktøjer
- Test og finjuster dine apps for kvalitets-AI, nemt.
- Brug Microsoft Foundry til at integrere og iterere med cloud, push og deploy for hurtig integration.

![LLMOps med PromptFlow](../../../translated_images/da/06-llm-promptflow.a183eba07a3a7fdf.webp)

## Fantastisk! Fortsæt din læring!

Fantastisk, lær nu mere om, hvordan vi strukturerer en applikation til at bruge koncepterne med [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), for at se hvordan Cloud Advocacy tilføjer disse koncepter i demonstrationer. For mere indhold, se vores [Ignite breakout session!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Se nu lektion 15, for at forstå hvordan [Retrieval Augmented Generation og vektordatabaser](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) påvirker Generative AI og for at skabe mere engagerende applikationer!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->