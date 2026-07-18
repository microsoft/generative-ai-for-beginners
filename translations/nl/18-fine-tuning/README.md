[![Open Source Models](../../../translated_images/nl/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Het Fijn Afstellen van Je LLM

Het gebruik van grote taalmodellen om generatieve AI-toepassingen te bouwen brengt nieuwe uitdagingen met zich mee. Een belangrijk punt is het waarborgen van de kwaliteit van de reacties (nauwkeurigheid en relevantie) in de inhoud die door het model wordt gegenereerd voor een specifieke gebruikersvraag. In eerdere lessen hebben we technieken besproken zoals prompt engineering en retrieval-augmented generation die proberen het probleem op te lossen door _de promptinput_ naar het bestaande model te _wijzigen_.

In de les van vandaag bespreken we een derde techniek, **fijn afstellen**, die probeert de uitdaging aan te pakken door _het model zelf opnieuw te trainen_ met extra data. Laten we de details induiken.

## Leerdoelen

Deze les introduceert het concept van fijn afstellen voor vooraf getrainde taalmodellen, verkent de voordelen en uitdagingen van deze aanpak, en biedt richtlijnen over wanneer en hoe je fijn afstellen kunt gebruiken om de prestaties van je generatieve AI-modellen te verbeteren.

Aan het einde van deze les zou je de volgende vragen moeten kunnen beantwoorden:

- Wat is fijn afstellen voor taalmodellen?
- Wanneer en waarom is fijn afstellen nuttig?
- Hoe kan ik een vooraf getraind model fijn afstellen?
- Wat zijn de beperkingen van fijn afstellen?

Klaar? Laten we beginnen.

## Geïllustreerde Gids

Wil je een overzicht krijgen van wat we gaan behandelen voordat we echt beginnen? Bekijk deze geïllustreerde gids die de leerreis voor deze les beschrijft - van de kernconcepten en motivatie voor fijn afstellen, tot het begrijpen van het proces en de beste praktijken voor het uitvoeren van de fijn afsteltaak. Dit is een fascinerend onderwerp om te verkennen, vergeet dus niet de [Resources](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) pagina te bekijken voor extra links ter ondersteuning van je zelfgestuurde leertraject!

![Geïllustreerde Gids voor Fijn Afstellen van Taalmodellen](../../../translated_images/nl/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Wat is fijn afstellen voor taalmodellen?

Grote taalmodellen zijn per definitie _vooraf getraind_ op grote hoeveelheden tekst afkomstig uit diverse bronnen, waaronder het internet. Zoals we in eerdere lessen hebben geleerd, hebben we technieken nodig zoals _prompt engineering_ en _retrieval-augmented generation_ om de kwaliteit van de reacties van het model op de vragen van de gebruiker ("prompts") te verbeteren.

Een populaire techniek voor prompt engineering houdt in dat het model meer begeleiding krijgt over wat er in het antwoord verwacht wordt, hetzij door _instructies te geven_ (expliciete begeleiding), hetzij door _enkele voorbeelden te geven_ (impliciete begeleiding). Dit wordt aangeduid als _few-shot learning_, maar het kent twee beperkingen:

- Model token limieten kunnen het aantal voorbeelden dat je kunt geven beperken en verminderen daarmee de effectiviteit.
- Model token kosten kunnen het duur maken om bij elke prompt voorbeelden toe te voegen en beperken de flexibiliteit.

Fijn afstellen is een veelgebruikte praktijk in machine learning systemen waarmee een vooraf getraind model opnieuw wordt getraind met nieuwe data om de prestaties voor een specifieke taak te verbeteren. In de context van taalmodellen kunnen we het vooraf getrainde model fijn afstellen _met een samengestelde set voorbeelden voor een gegeven taak of toepassingsgebied_ om een **aangepast model** te creëren dat mogelijk nauwkeuriger en relevanter is voor die specifieke taak of dat domein. Een bijkomend voordeel van fijn afstellen is dat het ook het aantal voorbeelden dat nodig is voor few-shot learning kan verminderen - wat het tokengebruik en de daaraan verbonden kosten verlaagt.

## Wanneer en waarom zouden we modellen fijn afstellen?

In _deze_ context, als we het hebben over fijn afstellen, bedoelen we **supervised** fijn afstellen waarbij de hertraining wordt gedaan door **nieuwe data toe te voegen** die geen onderdeel was van de oorspronkelijke trainingsdataset. Dit verschilt van een onbewaakte fijn afstelmethode waarbij het model opnieuw wordt getraind op de originele data, maar met andere hyperparameters.

Het belangrijkste om te onthouden is dat fijn afstellen een geavanceerde techniek is die een bepaald niveau van expertise vereist om de gewenste resultaten te bereiken. Als het verkeerd wordt gedaan, kan het de verwachte verbeteringen uitblijven en zelfs de prestaties van het model voor je beoogde domein verslechteren.

Dus voordat je leert "hoe" je taalmodellen fijn afstelt, moet je weten "waarom" je deze weg zou moeten nemen, en "wanneer" je het proces van fijn afstellen moet starten. Begin met het stellen van deze vragen aan jezelf:

- **Use Case**: Wat is je _gebruikssituatie_ voor fijn afstellen? Welk aspect van het huidige vooraf getrainde model wil je verbeteren?
- **Alternatieven**: Heb je _andere technieken_ geprobeerd om het gewenste resultaat te bereiken? Gebruik deze om een basislijn voor vergelijking te creëren.
  - Prompt engineering: Probeer technieken zoals few-shot prompting met voorbeelden van relevante promptantwoorden. Beoordeel de kwaliteit van de antwoorden.
  - Retrieval Augmented Generation: Probeer prompts aan te vullen met queryresultaten die uit je data zijn opgehaald. Beoordeel de kwaliteit van de antwoorden.
- **Kosten**: Heb je de kosten van fijn afstellen geïdentificeerd?
  - Afstembaarheid - is het vooraf getrainde model beschikbaar voor fijn afstellen?
  - Inspanning - voor het voorbereiden van trainingsdata, evalueren & verfijnen van het model.
  - Rekencapaciteit - voor het uitvoeren van fijnstel taken en het inzetten van het fijn afgestelde model
  - Data - toegang tot voldoende kwalitatieve voorbeelden voor de impact van fijn afstellen
- **Voordelen**: Heb je de voordelen van fijn afstellen bevestigd?
  - Kwaliteit - presteerde het fijn afgestelde model beter dan de basislijn?
  - Kosten - vermindert het het tokengebruik door prompts te vereenvoudigen?
  - Uitbreidbaarheid - kun je het basismodel hergebruiken voor nieuwe domeinen?

Door deze vragen te beantwoorden, zou je moeten kunnen bepalen of fijn afstellen de juiste aanpak is voor jouw gebruikssituatie. Idealiter is de aanpak alleen geldig als de voordelen opwegen tegen de kosten. Zodra je beslist om door te gaan, is het tijd om na te denken over _hoe_ je het vooraf getrainde model kunt fijn afstellen.

Wil je meer inzicht in het besluitvormingsproces? Bekijk [Fijn afstellen of niet fijn afstellen](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Hoe kunnen we een vooraf getraind model fijn afstellen?

Om een vooraf getraind model fijn af te stellen, heb je nodig:

- een vooraf getraind model om fijn af te stellen
- een dataset om te gebruiken voor fijn afstellen
- een trainingsomgeving om de fijnsteltaak uit te voeren
- een hostingomgeving om het fijn afgestelde model te implementeren

## Fijn afstellen op Microsoft Foundry

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) is tegenwoordig de plek waar je fijn afgestemde, geïmplementeerde en beheerde aangepaste modellen op Azure kunt maken (het brengt samen wat voorheen Azure OpenAI Studio en Azure AI Studio was). Voordat je een taak start, is het handig de keuzes die Foundry biedt te begrijpen - en de beste praktijken die het platform aanbeveelt. Onder de motorkap gebruikt Foundry **LoRA (low-rank adaptation)** om modellen efficiënt fijn af te stellen, wat de training sneller en betaalbaarder houdt dan het opnieuw trainen van elk gewicht.

### Stap 1: Kies een trainingstechniek

Foundry ondersteunt drie fijn afsteltechnieken. **Begin met SFT** - het bestrijkt de breedste reeks scenario’s.

| Techniek | Wat het doet | Wanneer te gebruiken |
| --- | --- | --- |
| **Supervised Fine-Tuning (SFT)** | Traint op input/output voorbeeldparen zodat het model leert de antwoorden te geven die je wilt. | De standaard voor de meeste taken: domeinspecialisatie, taakprestatie, stijl en toon, instructievolging, en taaladaptatie. |
| **Direct Preference Optimization (DPO)** | Leert van _geprefereerde versus niet-geprefereerde_ antwoordparen om uitvoer in lijn te brengen met menselijke voorkeuren. | Verbetering van reactiekwaliteit, veiligheid en afstemming wanneer je vergelijkende feedback hebt. |
| **Reinforcement Fine-Tuning (RFT)** | Gebruikt beloningssignalen van _beoordelaars_ om complexe gedragingen te optimaliseren met reinforcement learning. | Objectieve, redeneerrijke domeinen (wiskunde, scheikunde, fysica) met duidelijke juiste/verkeerde antwoorden. Vereist meer ML-expertise. |

### Stap 2: Kies een trainingsklasse

Foundry laat je kiezen hoe en waar de training plaatsvindt:

- **Standaard** - traint in de regio van je resource en garandeert datagebondenheid. Gebruik dit wanneer data in een specifieke regio moet blijven.
- **Globaal** - goedkoper en sneller om in de wachtrij te zetten door capaciteit buiten je regio te gebruiken (data en gewichten worden naar de trainingsregio gekopieerd). Een goede standaardoptie wanneer datagebondenheid geen vereiste is.
- **Ontwikkelaar** - de laagste kosten, gebruikmakend van ongebruikte capaciteit zonder latentie/SLA-garanties (taken kunnen worden onderbroken en hervat). Ideaal voor experimenteren.

### Stap 3: Kies een basismodel

Fijn af te stellen modellen zijn onder meer OpenAI `gpt-4o-mini`, `gpt-4o`, `gpt-4.1`, `gpt-4.1-mini` en `gpt-4.1-nano` (SFT; de 4o/4.1 familie ondersteunt ook DPO), de redeneringsmodellen `o4-mini` en `gpt-5` (RFT), plus open-source modellen zoals `Ministral-3B`, `Qwen-32B`, `Llama-3.3-70B-Instruct` en `gpt-oss-20b` (SFT op Foundry resources). Controleer altijd de actuele [Lijst van fijn afstelmodellen](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst) voor ondersteunde methodes, regio's en beschikbaarheid.

> Foundry biedt twee modaliteiten: **serverless** (consumptie-gebaseerde prijsstelling, geen GPU-quotumbeheer, OpenAI en geselecteerde modellen) en **managed compute** (bring-your-own VM's via Azure Machine Learning voor het breedste modelassortiment). De meeste mensen zouden met serverless moeten beginnen.

### Foundry beste praktijken

- **Begin met de basislijn.** Meet het basismodel met prompt engineering en RAG _voordat_ je fijn afstelt, zodat je de winst kunt aantonen.
- **Begin klein, groepeer daarna.** Start met 50-100 hoogwaardige voorbeelden om de aanpak te valideren, breid daarna uit naar 500+ voor productie. Kwaliteit gaat boven kwantiteit - verwijder voorbeelden van lage kwaliteit.
- **Formatteer data correct.** Trainings- en validatiebestanden moeten JSONL zijn, UTF-8 **met BOM**, onder 512 MB, in het chat-completions berichtformaat. Voeg altijd een validatiebestand toe zodat je overfitting kunt monitoren.
- **Houd de trainingssysteem prompt aan bij inferentie.** Gebruik hetzelfde systembericht wanneer je het model aanroept als tijdens het trainen.
- **Evalueer checkpoints - zet niet blindelings de laatste in productie.** Foundry bewaart de laatste drie epochs als inzetbare checkpoints; kies degene die het beste generaliseert door `train_loss` / `valid_loss` en tokennauwkeurigheid te bekijken.
- **Meet tokenkosten naast kwaliteit** bij het vergelijken van het fijn afgestelde model met de basislijn.
- **Itereer met continue fijn afstelling.** Je kunt een al fijn afgestemd model opnieuw fijn afstellen met nieuwe data (ondersteund voor OpenAI-modellen).
- **Let op hostingkosten.** Een ingezet aangepast model brengt per uur kosten in rekening, en een inactieve inzet wordt na 15 dagen verwijderd - ruim op wat je niet nodig hebt.

Volg de stap-voor-stap instructies in [Een model aanpassen met fijn afstellen](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst), en bekijk de gidsen voor [DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst) en [RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst) wanneer je klaar bent voor de andere technieken.

## Fijn Afstellen in de Praktijk

De volgende bronnen bieden stapsgewijze tutorials die je door een reëel voorbeeld leiden op een momenteel ondersteund model met een samengestelde dataset. Om hiermee te werken heb je een account nodig bij de specifieke aanbieder, samen met toegang tot het relevante model en datasets.

| Aanbieder     | Tutorial                                                                                                                                                                       | Beschrijving                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Hoe chatmodellen fijn af te stellen](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)        | Leer hoe je een recent OpenAI chatmodel kunt fijn afstellen voor een specifiek domein ("receptassistent") door trainingsdata voor te bereiden, de fijnsteltaak uit te voeren, en het fijn afgestelde model voor inferentie te gebruiken.                                                                                                                                                                                                   |
| Microsoft Foundry | [Een model aanpassen met fijn afstellen](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst)                      | Leer hoe je een momenteel ondersteund model zoals `gpt-4.1-mini` **op Azure** kunt fijn afstellen met Microsoft Foundry: train & upload trainings- en validatiegegevens, voer de fijnsteltaak uit, en zet het nieuwe model in.                                                                                                                                                                                                                         |

| Hugging Face | [Fijn afstemmen van LLM's met Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Deze blogpost leidt je door het fijn afstemmen van een _open LLM_ (bijv.: `CodeLlama 7B`) met behulp van de [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) bibliotheek & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) met open [datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) op Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Fijn afstemmen van LLM's met AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (of AutoTrain Advanced) is een Python-bibliotheek ontwikkeld door Hugging Face die fijn afstemmen mogelijk maakt voor veel verschillende taken, inclusief LLM fijn afstemmen. AutoTrain is een no-code oplossing en fijn afstemmen kan plaats vinden in je eigen cloud, op Hugging Face Spaces of lokaal. Het ondersteunt zowel een web-gebaseerde GUI, CLI als training via yaml-configuratiebestanden.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Fijn afstemmen van LLM's met Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth is een open-source framework dat fijn afstemmen van LLM's en reinforcement learning (RL) ondersteunt. Unsloth stroomlijnt lokale training, evaluatie en uitrol met kant-en-klare [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Het ondersteunt ook tekst-naar-spraak (TTS), BERT en multimodale modellen. Om te beginnen, lees hun stapsgewijze [Handleiding voor fijn afstemmen van LLM's](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Opdracht

Kies een van de bovenstaande tutorials en doorloop deze. _We kunnen een versie van deze tutorials in Jupyter Notebooks in deze repo repliceren voor referentie. Gebruik voor de meest actuele versies direct de originele bronnen_.

## Goed gedaan! Ga door met leren.

Na het voltooien van deze les, bekijk onze [Generatieve AI Leercollectie](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je kennis van Generatieve AI verder te vergroten!

Gefeliciteerd!! Je hebt de laatste les uit de v2-serie van deze cursus afgerond! Blijf leren en bouwen. \*\*Bekijk de [BRONNEN](RESOURCES.md?WT.mc_id=academic-105485-koreyst) pagina voor een lijst met aanvullende suggesties over dit onderwerp.

Onze v1-serie lessen is ook bijgewerkt met meer opdrachten en concepten. Neem dus even de tijd om je kennis op te frissen - en deel alsjeblieft [je vragen en feedback](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) om ons te helpen deze lessen voor de community te verbeteren.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->