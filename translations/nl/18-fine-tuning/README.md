[![Open Source Models](../../../translated_images/nl/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Het fijn afstemmen van je LLM

Het gebruik van grote taalmodellen om generatieve AI-toepassingen te bouwen brengt nieuwe uitdagingen met zich mee. Een belangrijk punt is het waarborgen van de responskwaliteit (nauwkeurigheid en relevantie) in door het model gegenereerde inhoud voor een gegeven gebruikersverzoek. In eerdere lessen hebben we technieken besproken zoals prompt engineering en retrieval-augmented generation die proberen het probleem op te lossen door _de promptinvoer_ naar het bestaande model aan te passen.

In de les van vandaag bespreken we een derde techniek, **fijn afstemmen**, die de uitdaging probeert aan te pakken door _het model zelf opnieuw te trainen_ met extra data. Laten we in de details duiken.

## Leerdoelen

Deze les introduceert het concept van fijn afstemmen voor voorgetrainde taalmodellen, verkent de voordelen en uitdagingen van deze aanpak, en biedt richtlijnen over wanneer en hoe je fijn afstemmen kunt gebruiken om de prestaties van je generatieve AI-modellen te verbeteren.

Aan het einde van deze les zou je de volgende vragen moeten kunnen beantwoorden:

- Wat is fijn afstemmen voor taalmodellen?
- Wanneer en waarom is fijn afstemmen nuttig?
- Hoe kan ik een voorgetraind model fijn afstemmen?
- Wat zijn de beperkingen van fijn afstemmen?

Klaar? Laten we beginnen.

## Geïllustreerde gids

Wil je het grote geheel van wat we zullen behandelen begrijpen voordat we beginnen? Bekijk deze geïllustreerde gids die de leerreis voor deze les beschrijft - van het leren van de kernbegrippen en motivatie voor fijn afstemmen tot het begrijpen van het proces en de beste praktijken voor het uitvoeren van de fijnafstemtaken. Dit is een fascinerend onderwerp om te verkennen, dus vergeet niet de [Resources](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) pagina te bekijken voor extra links ter ondersteuning van je zelfgestuurde leertraject!

![Geïllustreerde gids voor het fijn afstemmen van taalmodellen](../../../translated_images/nl/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Wat is fijn afstemmen voor taalmodellen?

Grote taalmodellen zijn per definitie _voorgetraind_ op grote hoeveelheden tekst afkomstig uit diverse bronnen, waaronder het internet. Zoals we in vorige lessen hebben geleerd, hebben we technieken nodig zoals _prompt engineering_ en _retrieval-augmented generation_ om de kwaliteit van de reacties van het model op de vragen van de gebruiker ("prompts") te verbeteren.

Een populaire prompt-engineeringtechniek houdt in dat het model meer begeleiding krijgt over wat er in de reactie wordt verwacht, door het geven van _instructies_ (expliciete begeleiding) of _het geven van een paar voorbeelden_ (impliciete begeleiding). Dit wordt _few-shot learning_ genoemd, maar het kent twee beperkingen:

- Tokenlimieten van het model kunnen het aantal voorbeelden dat je kunt geven beperken en zo de effectiviteit verminderen.
- Tokenkosten van het model kunnen het duur maken om voorbeelden aan elke prompt toe te voegen, en beperken de flexibiliteit.

Fijn afstemmen is een gangbare praktijk in machine learning-systemen waarbij we een voorgetraind model nemen en het opnieuw trainen met nieuwe data om de prestaties op een specifieke taak te verbeteren. In de context van taalmodellen kunnen we het voorgetrainde model fijn afstemmen _met een zorgvuldig samengestelde set voorbeelden voor een bepaalde taak of toepassingsdomein_ om zo een **aangepast model** te creëren dat nauwkeuriger en relevanter is voor die specifieke taak of dat domein. Een bijkomend voordeel van fijn afstemmen is dat het ook het aantal voorbeelden dat nodig is voor few-shot leren kan verminderen - waardoor het tokengebruik en de gerelateerde kosten afnemen.

## Wanneer en waarom zouden we modellen fijn afstemmen?

In _deze_ context, wanneer we het over fijn afstemmen hebben, bedoelen we **gecontroleerd** fijn afstemmen waarbij het opnieuw trainen gebeurt door **nieuwe data toe te voegen** die niet deel uitmaakte van de oorspronkelijke trainingsgegevens. Dit verschilt van een ongecontroleerde fijnafstemanpak waarbij het model opnieuw wordt getraind op de oorspronkelijke data, maar met andere hyperparameters.

Het belangrijkste om te onthouden is dat fijn afstemmen een geavanceerde techniek is die een bepaald niveau van expertise vereist om de gewenste resultaten te bereiken. Als het verkeerd wordt uitgevoerd, kan het de verwachte verbeteringen niet opleveren en zelfs de prestaties van het model voor het beoogde domein verslechteren.

Dus voordat je leert "hoe" je taalmodellen moet fijn afstemmen, moet je weten "waarom" je deze route zou moeten kiezen en "wanneer" je het proces van fijn afstemmen moet starten. Begin door jezelf de volgende vragen te stellen:

- **Gebruikssituatie**: Wat is je _gebruikssituatie_ voor fijn afstemmen? Welk aspect van het huidige voorgetrainde model wil je verbeteren?
- **Alternatieven**: Heb je _andere technieken_ geprobeerd om de gewenste resultaten te bereiken? Gebruik deze om een basislijn te creëren voor vergelijking.
  - Prompt engineering: Probeer technieken zoals few-shot prompting met voorbeelden van relevante promptreacties. Evalueer de kwaliteit van de reacties.
  - Retrieval Augmented Generation: Probeer prompts aan te vullen met resultaten van zoekopdrachten in je data. Evalueer de kwaliteit van de reacties.
- **Kosten**: Heb je de kosten voor fijn afstemmen geïdentificeerd?
  - Afstembaarheid - is het voorgetrainde model beschikbaar voor fijn afstemmen?
  - Inspanning - voor het voorbereiden van trainingsdata, het evalueren & verfijnen van het model.
  - Rekenkracht - voor het uitvoeren van fijnafstem opdrachten en het implementeren van het fijn afgestemde model.
  - Data - toegang tot voldoende kwalitatieve voorbeelden voor impact van fijn afstemmen.
- **Voordelen**: Heb je de voordelen van fijn afstemmen bevestigd?
  - Kwaliteit - presteerde het fijn afgestemde model beter dan de basislijn?
  - Kosten - vermindert het het tokengebruik door het vereenvoudigen van prompts?
  - Uitbreidbaarheid - kun je het basismodel hergebruiken voor nieuwe domeinen?

Door deze vragen te beantwoorden, moet je kunnen beslissen of fijn afstemmen de juiste aanpak is voor je gebruikssituatie. Idealiter is de aanpak alleen geldig als de voordelen opwegen tegen de kosten. Zodra je besluit door te gaan, is het tijd om na te denken over _hoe_ je het voorgetrainde model kunt fijn afstemmen.

Wil je meer inzicht krijgen in het besluitvormingsproces? Bekijk [Fijn afstemmen of niet fijn afstemmen](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Hoe kunnen we een voorgetraind model fijn afstemmen?

Om een voorgetraind model fijn af te stemmen, heb je nodig:

- een voorgetraind model om fijn af te stemmen
- een dataset voor het fijn afstemmen
- een trainingsomgeving om de fijnafstemtaken uit te voeren
- een hostingomgeving om het fijn afgestemde model te implementeren

## Fijn afstemmen in actie

> **Opmerking:** `gpt-35-turbo` / `gpt-3.5-turbo`, genoemd in enkele van de tutorials hieronder, is met pensioen voor zowel inferentie als fijn afstemmen. Als je vandaag een nieuw fijnafstemproces start, richt je dan op een momenteel ondersteund model - bijvoorbeeld `gpt-4o-mini` of `gpt-4.1-mini`. Zie de [Lijst met fijn af te stemmen modellen](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) voor de huidige set fijn af te stemmen modellen. De concepten en stappen in deze tutorials zijn nog steeds van toepassing.

De volgende bronnen bieden stapsgewijze tutorials die je begeleiden met een echt voorbeeld met een geselecteerd model en een zorgvuldig samengestelde dataset. Om deze tutorials te doorlopen, heb je een account nodig bij de specifieke aanbieder, samen met toegang tot het relevante model en datasets.

| Provider     | Tutorial                                                                                                                                                                       | Beschrijving                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Hoe chatmodellen fijn afstemmen](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Leer hoe je een `gpt-35-turbo` fijn afstemt voor een specifiek domein ("receptassistent") door trainingsdata voor te bereiden, de fijnafstemtaken uit te voeren en het fijn afgestemde model te gebruiken voor inferentie.                                                                                                                                                                                                             |
| Azure OpenAI | [GPT 3.5 Turbo fijn afstem tutorial](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst) | Leer hoe je een `gpt-35-turbo-0613` model **op Azure** fijn afstemt door stappen te nemen voor het aanmaken en uploaden van trainingsdata, het uitvoeren van de fijnafstemtaken, en het implementeren & gebruiken van het nieuwe model.                                                                                                                                                                                               |
| Hugging Face | [Fijn afstemmen van LLMs met Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Dit blogartikel begeleidt je bij het fijn afstemmen van een _open LLM_ (bijv. `CodeLlama 7B`) met de [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) bibliotheek & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) met open [datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) op Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 🤗 AutoTrain | [Fijn afstemmen van LLMs met AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (of AutoTrain Advanced) is een python bibliotheek ontwikkeld door Hugging Face die fijn afstemmen voor veel verschillende taken mogelijk maakt, inclusief LLM fijn afstemming. AutoTrain is een no-code oplossing en fijn afstemmen kan worden uitgevoerd in je eigen cloud, op Hugging Face Spaces of lokaal. Het ondersteunt zowel een webgebaseerde GUI, CLI en training via yaml-configuratiebestanden.                                            |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 🦥 Unsloth | [Fijn afstemmen van LLMs met Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth is een open-source framework dat fijn afstemmen van LLMs en reinforcement learning (RL) ondersteunt. Unsloth vereenvoudigt lokaal trainen, evalueren, en implementeren met kant-en-klare [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Het ondersteunt ook text-to-speech (TTS), BERT en multimodale modellen. Om te beginnen, lees hun stapsgewijze [Fijn afstemmen van LLMs gids](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).  |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
## Opdracht

Kies een van de bovenstaande tutorials en doorloop die. _We kunnen een versie van deze tutorials repliceren in Jupyter Notebooks in deze repo als referentie. Gebruik echter direct de originele bronnen om de nieuwste versies te verkrijgen_.

## Goed gedaan! Ga door met leren.

Na het voltooien van deze les, bekijk onze [Generatieve AI Leercollectie](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je kennis van Generatieve AI verder te verdiepen!

Gefeliciteerd!! Je hebt de laatste les uit de v2-serie van deze cursus voltooid! Stop niet met leren en bouwen. \*\*Bekijk de [RESOURCES](RESOURCES.md?WT.mc_id=academic-105485-koreyst) pagina voor een lijst met extra suggesties specifiek over dit onderwerp.

Onze v1-serie lessen is ook bijgewerkt met meer opdrachten en concepten. Neem dus even de tijd om je kennis op te frissen - en deel gerust je [vragen en feedback](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) om ons te helpen deze lessen voor de community te verbeteren.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->