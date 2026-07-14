# Verkennen en vergelijken van verschillende LLM's

[![Verkennen en vergelijken van verschillende LLM's](../../../translated_images/nl/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Klik op de afbeelding hierboven om de video van deze les te bekijken_

Met de vorige les hebben we gezien hoe Generative AI het technologische landschap verandert, hoe Large Language Models (LLM's) werken en hoe een bedrijf - zoals onze startup - ze kan toepassen voor hun gebruikssituaties en kan groeien! In dit hoofdstuk gaan we verschillende soorten large language models (LLM's) vergelijken en tegen elkaar afzetten om hun voor- en nadelen te begrijpen.

De volgende stap in de reis van onze startup is het verkennen van het huidige landschap van LLM's en het begrijpen welke geschikt zijn voor onze use case.

## Introductie

Deze les behandelt:

- Verschillende soorten LLM's in het huidige landschap.
- Testen, itereren en vergelijken van verschillende modellen voor jouw gebruikssituatie in Azure.
- Hoe je een LLM kunt inzetten.

## Leerdoelen

Na het voltooien van deze les ben je in staat om:

- Het juiste model te selecteren voor jouw gebruikssituatie.
- Te begrijpen hoe je het model test, iteraties uitvoert en de prestaties verbetert.
- Te weten hoe bedrijven modellen inzetten.

## Begrijp verschillende types LLM's

LLM's kunnen meerdere classificaties hebben op basis van hun architectuur, trainingsdata en gebruikssituatie. Het begrijpen van deze verschillen helpt onze startup het juiste model te selecteren voor het scenario, en te begrijpen hoe je het model test, iteraties uitvoert en de prestaties verbetert.

Er zijn veel verschillende soorten LLM modellen, je keuze hangt af van waar je ze voor wilt gebruiken, je data, hoeveel je bereid bent te betalen, en meer.

Afhankelijk van of je de modellen wilt gebruiken voor tekst, audio, video, beeldgeneratie en zo verder, kies je misschien voor een ander type model.

- **Audio en spraakherkenning**. Whisper-achtige modellen zijn nog steeds nuttige algemene spraakherkenningsmodellen, maar productiekeuzes omvatten nu ook nieuwere spraak-naar-tekst modellen zoals `gpt-4o-transcribe`, `gpt-4o-mini-transcribe` en diarization varianten. Evalueer taalondersteuning, diarization, realtime ondersteuning, latentie en kosten voor jouw scenario. Lees meer in de [OpenAI spraak-naar-tekst documentatie](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst).

- **Beeldgeneratie**. DALL-E en Midjourney zijn bekende opties voor beeldgeneratie, maar huidige OpenAI beeld-API's concentreren zich op GPT Image modellen zoals `gpt-image-2`, terwijl Stable Diffusion, Imagen, Flux en andere modelfamilies ook veelvoorkomende keuzes zijn. Vergelijk promptvolging, bewerkingsondersteuning, stijlcontrole, veiligheidsvereisten en licenties. Lees meer in de [OpenAI handleiding voor beeldgeneratie](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) en hoofdstuk 9 van dit curriculum.

- **Tekstgeneratie**. Tekstmodellen omvatten nu frontier modellen, redeneermodellen, kleinere low-latency modellen, en open-gewicht modellen. Voorbeelden zijn OpenAI GPT-5.x modellen, Anthropic Claude 4.x modellen, Google Gemini 3.x modellen, Meta Llama 4 modellen en Mistral modellen. Kies niet alleen op basis van releasedatum of prijs; vergelijk taakkwaliteit, latentie, contextwindow, toolgebruik, veiligheidsgedrag, regionale beschikbaarheid en totaalkosten. De [Microsoft Foundry modelcatalogus](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) is een goede plek om modellen op Azure te vergelijken.

- **Multi-modality**. Veel huidige modellen kunnen meer dan tekst verwerken. Sommige accepteren beeld-, audio- of video-input; sommige kunnen tools aanroepen; en gespecialiseerde modellen kunnen beelden, audio of video genereren. Bijvoorbeeld, huidige OpenAI modellen ondersteunen tekst- en beeldinput, Gemini modellen kunnen afhankelijk van de variant tekst, code, beeld, audio en video inputs ondersteunen, en Llama 4 Scout en Maverick zijn open-gewicht native multimodale modellen. Controleer altijd elke modelkaart op ondersteunde input- en outputmodaliteiten voordat je een workflow opbouwt.

Het selecteren van een model betekent dat je enkele basisvaardigheden krijgt, die echter niet altijd voldoende zijn. Vaak heb je bedrijfsspecifieke data die je op de een of andere manier aan de LLM moet communiceren. Er zijn enkele verschillende keuzes hoe dit aan te pakken, meer daarover in de komende secties.

### Foundation Models versus LLM's

De term Foundation Model werd [gecreëerd door onderzoekers van Stanford](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) en gedefinieerd als een AI-model dat aan enkele criteria voldoet, zoals:

- **Ze worden getraind met ongecontroleerd leren of zelf-gecontroleerd leren**, wat betekent dat ze getraind worden op gelabelde multimodale data, en geen menselijke annotatie of labeling van data nodig hebben voor het trainingsproces.
- **Het zijn erg grote modellen**, gebaseerd op zeer diepe neurale netwerken getraind op miljarden parameters.
- **Ze zijn normaal bedoeld als een ‘fundament’ voor andere modellen**, wat betekent dat ze kunnen worden gebruikt als startpunt waarop andere modellen worden gebouwd, bijvoorbeeld door fine-tuning.

![Foundation Models versus LLMs](../../../translated_images/nl/FoundationModel.e4859dbb7a825c94.webp)

Afbeeldingsbron: [Essentiële gids voor Foundation Models en Large Language Models | door Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Om dit onderscheid verder te verduidelijken, nemen we ChatGPT als historisch voorbeeld. Vroege versies van ChatGPT gebruikten GPT-3.5 als foundation model. OpenAI gebruikte daarna chatspecifieke data en alignment-technieken om een afgestemde versie te creëren die beter presteerde in conversatiescenario's, zoals chatbots. Moderne AI-diensten routeren vaak tussen verschillende modelvarianten, dus de naam van de dienst en het onderliggende model zijn niet altijd hetzelfde.

![Foundation Model](../../../translated_images/nl/Multimodal.2c389c6439e0fc51.webp)

Afbeeldingsbron: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Open-Weight/Open-Source versus Proprietary Models

Een andere manier om LLM's te categoriseren is of ze open-weight, open-source of proprietary zijn.

Open-source en open-weight modellen maken modelartefacten beschikbaar voor inspectie, download of aanpassing, maar hun licenties verschillen. Sommige zijn volledig open source, terwijl anderen open-weight modellen met gebruiksbeperkingen zijn. Ze kunnen nuttig zijn wanneer een bedrijf meer controle nodig heeft over deployment, datalokalisatie, kosten of aanpassing. Teams moeten echter nog steeds licentievoorwaarden, serveerkosten, onderhoud, beveiligingsupdates en evaluatiekwaliteit beoordelen voordat ze ze in productie gebruiken. Voorbeelden zijn [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst), sommige [Mistral modellen](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst) en veel modellen gehost op [Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst).

Proprietary modellen zijn eigendom van en worden gehost door een aanbieder. Deze modellen zijn vaak geoptimaliseerd voor managed productiegebruik en kunnen sterke ondersteuning, veiligheidsmaatregelen, toolintegratie en schaal bieden. Klanten kunnen meestal de modelgewichten niet inspecteren of aanpassen, en ze moeten de voorwaarden voor privacy, retentie, compliance en acceptabel gebruik van de aanbieder controleren. Voorbeelden zijn [OpenAI modellen](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), [Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst) en [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst).

### Embedding versus Image generatie versus Text en Code generatie

LLM's kunnen ook worden gecategoriseerd naar de output die ze genereren.

Embeddings zijn een set modellen die tekst kunnen omzetten in een numerieke vorm, een embedding genoemd, wat een numerieke representatie van de inputtekst is. Embeddings maken het voor machines gemakkelijker om relaties tussen woorden of zinnen te begrijpen en kunnen als input worden gebruikt voor andere modellen, zoals classificatiemodellen of clusteringmodellen die beter presteren op numerieke data. Embeddingmodellen worden vaak gebruikt voor transfer learning, waarbij een model wordt gebouwd voor een surrogaattaak met veel data, waarna de modelgewichten (embeddings) worden hergebruikt voor andere downstream-taken. Een voorbeeld uit deze categorie zijn [OpenAI embeddings](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Embedding](../../../translated_images/nl/Embedding.c3708fe988ccf760.webp)

Beeldgeneratiemodellen zijn modellen die beelden genereren. Deze modellen worden vaak gebruikt voor beeldbewerking, beeldsynthese en beeldvertaling. Beeldgeneratiemodellen worden vaak getraind op grote datasets van beelden, zoals [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), en kunnen worden gebruikt om nieuwe beelden te genereren of bestaande beelden te bewerken met inpainting, superresolutie en kleurtechnieken. Voorbeelden zijn [GPT Image modellen](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst), [Stable Diffusion modellen](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst) en Imagen modellen.

![Image generation](../../../translated_images/nl/Image.349c080266a763fd.webp)

Tekst- en codegeneratiemodellen zijn modellen die tekst of code genereren. Deze modellen worden vaak gebruikt voor tekstsamenvatting, vertaling en vraagbeantwoording. Tekstgeneratiemodellen worden vaak getraind op grote datasets van tekst, zoals [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), en kunnen gebruikt worden om nieuwe tekst te genereren of om vragen te beantwoorden. Codegeneratiemodellen, zoals [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), worden vaak getraind op grote datasets van code, zoals GitHub, en kunnen gebruikt worden om nieuwe code te genereren of om bugs te fixen in bestaande code.

![Text and code generation](../../../translated_images/nl/Text.a8c0cf139e5cc2a0.webp)

### Encoder-Decoder versus Alleen Decoder

Om het te hebben over de verschillende architectuurtypen van LLM's, laten we een analogie gebruiken.

Stel je voor dat je manager je de taak gaf om een quiz te schrijven voor de studenten. Je hebt twee collega’s; de een zorgt voor het maken van de inhoud en de ander kijkt deze na.

De inhoudsmaker is als een alleen-decoder model: ze kunnen naar het onderwerp kijken, zien wat je al geschreven hebt, en dan doorgaan met het genereren van inhoud op basis van die context. Ze zijn heel goed in het schrijven van boeiende en informatieve inhoud, maar ze zijn niet altijd de beste keuze als de taak alleen classificeren, ophalen of coderen van informatie is. Voorbeelden van alleen-decoder modellen zijn GPT en Llama modellen.

De beoordelaar is als een alleen-encoder model, ze kijken naar de geschreven cursus en antwoorden, merken de relatie tussen die op en begrijpen de context, maar zijn niet goed in het genereren van inhoud. Een voorbeeld van een alleen-encoder model is BERT.

Stel je voor dat we ook iemand hebben die de quiz kan maken en beoordelen, dat is een Encoder-Decoder model. Enkele voorbeelden zijn BART en T5.

### Dienst versus Model

Nu, laten we het verschil bespreken tussen een dienst en een model. Een dienst is een product dat wordt aangeboden door een Cloud Service Provider en is vaak een combinatie van modellen, data en andere componenten. Een model is het kerncomponent van een dienst en is vaak een foundation model, zoals een LLM.

Diensten zijn vaak geoptimaliseerd voor productiegebruik en zijn vaak gemakkelijker te gebruiken dan modellen, via een grafische gebruikersinterface. Diensten zijn echter niet altijd gratis beschikbaar en kunnen een abonnement of betaling vereisen in ruil voor het gebruik van de apparatuur en middelen van de dienstverlener, het optimaliseren van kosten en eenvoudige schaalbaarheid. Een voorbeeld van een dienst is [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), die een pay-as-you-go tariefplan aanbiedt, wat betekent dat gebruikers naar rato van gebruik van de dienst worden gefactureerd. Azure OpenAI Service biedt ook beveiliging op ondernemingsniveau en een verantwoordelijk AI-kader bovenop de capaciteiten van de modellen.

Modellen zijn de neurale netwerkartefacten: parameters, gewichten, architectuur, tokenizer en ondersteunende configuratie. Het lokaal draaien van een model of in een privé-omgeving vereist geschikte hardware, serverinfrastructuur, monitoring en een compatibele open-source/open-weight licentie of een commerciële licentie. Open-weight modellen zoals Llama 4 of Mistral modellen kunnen zelf gehost worden, maar ze vereisen nog steeds rekenkracht en operationele expertise.

## Hoe te testen en itereren met verschillende modellen om prestaties te begrijpen op Azure


Zodra ons team het huidige landschap van LLM's heeft verkend en enkele goede kandidaten voor hun scenario's heeft geïdentificeerd, is de volgende stap het testen ervan op hun data en werklast. Dit is een iteratief proces, uitgevoerd door experimenten en metingen.
De meeste modellen die we in eerdere paragrafen noemden (OpenAI-modellen, open-weight modellen zoals Llama 4 en Mistral, en Hugging Face-modellen) zijn beschikbaar in [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst).

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst), voorheen Azure AI Studio/Azure AI Foundry, is een uniform Azure-platform voor het bouwen van AI-apps en -agenten. Het helpt ontwikkelaars bij het beheren van de levenscyclus van experimentatie en evaluatie tot implementatie, monitoring en governance. De modelcatalogus in Microsoft Foundry stelt de gebruiker in staat om:

- Het fundamentmodel van interesse in de catalogus te vinden, inclusief modellen verkocht door Azure en modellen van partners en community-providers. Gebruikers kunnen filteren op taak, aanbieder, licentie, implementatieoptie of naam.

![Model catalog](../../../translated_images/nl/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- De modelkaart te bekijken, inclusief een gedetailleerde beschrijving van het beoogde gebruik en trainingsgegevens, codevoorbeelden en evaluatieresultaten uit de interne evaluatiebibliotheek.

![Model card](../../../translated_images/nl/ModelCard.598051692c6e400d.webp)

- Benchmarks te vergelijken over modellen en datasets beschikbaar in de industrie om te beoordelen welke het beste past bij het businessscenario, via het paneel [Model Benchmarks](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst).

![Model benchmarks](../../../translated_images/nl/ModelBenchmarks.254cb20fbd06c03a.webp)

- Ondersteunde modellen fijn af te stemmen op aangepaste trainingsgegevens om de modelprestaties in een specifieke werklast te verbeteren, gebruikmakend van de experimentatie- en trackingmogelijkheden van Microsoft Foundry.

![Model fine-tuning](../../../translated_images/nl/FineTuning.aac48f07142e36fd.webp)

- Het originele voorgetrainde model of de fijn afgestemde versie te implementeren naar een externe realtime inferentie-eindpunt, met beheerde compute- of serverloze implementatieopties, om toepassingen het model te laten gebruiken.

![Model deployment](../../../translated_images/nl/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> Niet alle modellen in de catalogus zijn momenteel beschikbaar voor fijn afstemmen en/of pay-as-you-go implementatie. Controleer de modelkaart voor details over de mogelijkheden en beperkingen van het model.

## Verbeteren van LLM-resultaten

We hebben met ons startupteam verschillende soorten LLM's en een cloudplatform (Microsoft Foundry) verkend dat ons in staat stelt om verschillende modellen te vergelijken, ze te evalueren op testdata, prestaties te verbeteren en te implementeren op inferentie-eindpunten.

Maar wanneer moeten ze overwegen een model fijn af te stemmen in plaats van een voorgetraind model te gebruiken? Zijn er andere benaderingen om modelprestaties op specifieke werklasten te verbeteren?

Er zijn verschillende benaderingen die een bedrijf kan gebruiken om de resultaten te krijgen die ze nodig hebben van een LLM. Je kunt verschillende soorten modellen selecteren met verschillende gradaties van training bij het inzetten van een LLM in productie, met verschillende niveaus van complexiteit, kosten en kwaliteit. Hier zijn enkele verschillende benaderingen:

- **Prompt engineering met context**. Het idee is om voldoende context te verschaffen wanneer je een prompt geeft om ervoor te zorgen dat je de vaakst gewenste antwoorden krijgt.

- **Retrieval Augmented Generation, RAG**. Je data kan bijvoorbeeld bestaan in een database of webendpoint, om ervoor te zorgen dat deze data, of een subset ervan, wordt meegenomen bij het prompten, kun je relevante data ophalen en dat onderdeel maken van de prompt van de gebruiker.

- **Fijn afgestemd model**. Hier heb je het model verder getraind op je eigen data, wat resulteert in een model dat nauwkeuriger en responsiever is naar je behoeften, maar mogelijk kostbaar is.

![LLMs deployment](../../../translated_images/nl/Deploy.18b2d27412ec8c02.webp)

Afbeeldingsbron: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Prompt Engineering met Context

Voorgetrainde LLM's presteren zeer goed op algemene natuurlijke taalopdrachten, zelfs door ze aan te roepen met een korte prompt, zoals een zin die voltooid moet worden of een vraag – het zogenaamde “zero-shot” leren.

Hoe meer de gebruiker zijn vraag kan kaderen met een gedetailleerd verzoek en voorbeelden – de Context – hoe nauwkeuriger en dichter bij de verwachtingen van de gebruiker het antwoord zal zijn. In dit geval spreken we van “one-shot” leren als de prompt slechts één voorbeeld bevat en “few-shot” leren als het meerdere voorbeelden bevat.
Prompt engineering met context is de meest kosteneffectieve benadering om mee te starten.

### Retrieval Augmented Generation (RAG)

LLM's hebben de beperking dat ze alleen de data kunnen gebruiken die tijdens hun training is gebruikt om een antwoord te genereren. Dit betekent dat ze niets weten over feiten die na het trainingsproces zijn gebeurd, en ze hebben geen toegang tot niet-publieke informatie (zoals bedrijfsdata).
Dit kan worden overwonnen door middel van RAG, een techniek die prompts aanvult met externe data in de vorm van stukken documenten, rekening houdend met beperkingen in de promptlengte. Dit wordt ondersteund door Vector database tools (zoals [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) die de bruikbare stukken ophalen uit verschillende vooraf gedefinieerde gegevensbronnen en toevoegen aan de context van de prompt.

Deze techniek is erg nuttig wanneer een bedrijf niet genoeg data, tijd of middelen heeft om een LLM fijn af te stemmen, maar toch de prestaties op een specifieke werklast wil verbeteren en de risico's op hallucinaties, verouderde of niet-ondersteunde antwoorden wil verminderen.

### Fijn afgestemd model

Fijn afstemmen is een proces dat transfer learning benut om het model aan te passen aan een specifieke taak of om een specifiek probleem op te lossen. In tegenstelling tot few-shot leren en RAG resulteert het in het genereren van een nieuw model met bijgewerkte gewichten en biases. Het vereist een set trainingsvoorbeelden die bestaan uit een enkele input (de prompt) en de bijbehorende output (de voltooiing).
Dit zou de voorkeursbenadering zijn als:

- **Kleine taak-specifieke modellen gebruiken**. Een bedrijf wil een kleiner model fijn afstemmen voor een smalle taak in plaats van herhaaldelijk een groter grensmodel te prompten, wat resulteert in een kosteneffectievere en snellere oplossing.

- **Latency overwegen**. Latency is belangrijk voor een specifiek gebruiksgeval, dus het is niet mogelijk om zeer lange prompts te gebruiken of het aantal voorbeelden dat het model moet leren past niet binnen de promptlengtebeperking.

- **Stabiel gedrag aanpassen**. Een bedrijf heeft veel hoogwaardige voorbeelden en wil dat het model consequent een taakpatroon, uitvoerformaat, toon of domeinspecifieke stijl volgt. Als het belangrijkste probleem recente feiten of private kennis betreft die vaak verandert, gebruik dan RAG in plaats van alleen op fijn afstemmen te vertrouwen.

### Getraind model

Het trainen van een LLM vanaf nul is ongetwijfeld de moeilijkste en complexste benadering om te volgen, wat enorme hoeveelheden data, vakkundige resources en passende rekenkracht vereist. Deze optie moet alleen worden overwogen in een scenario waarin een bedrijf een domeinspecifiek gebruiksgeval heeft en een grote hoeveelheid domeingerichte data.

## Kenniscontrole

Wat zou een goede benadering kunnen zijn om LLM-voltooiingsresultaten te verbeteren?

1. Prompt engineering met context
1. RAG
1. Fijn afgestemd model

A: Alle drie kunnen helpen. Begin met prompt engineering en context voor snelle verbeteringen, en gebruik RAG wanneer het model actuele feiten of privé bedrijfsdata nodig heeft. Kies voor fijn afstemmen als je genoeg hoogwaardige voorbeelden hebt en het model consequent een taak, formaat, toon of domeinpatroon moet volgen.

## 🚀 Uitdaging

Lees meer over hoe je [RAG kunt gebruiken](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) voor je bedrijf.

## Geweldig werk, ga door met leren

Na het voltooien van deze les kun je onze [Generative AI Learning collectie](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) bekijken om je kennis over Generative AI verder te ontwikkelen!

Ga naar Les 3 waar we kijken hoe je [Verantwoord bouwt met Generatieve AI](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->