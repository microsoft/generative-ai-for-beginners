<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "807f0d9fc1747e796433534e1be6a98a",
  "translation_date": "2025-10-17T19:55:58+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "nl"
}
-->
[![Open Source Modellen](../../../translated_images/18-lesson-banner.f30176815b1a5074fce9cceba317720586caa99e24001231a92fd04eeb54a121.nl.png)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Het Fijnstemmen van Je LLM

Het gebruik van grote taalmodellen om generatieve AI-toepassingen te bouwen brengt nieuwe uitdagingen met zich mee. Een belangrijk probleem is het waarborgen van de kwaliteit van de antwoorden (nauwkeurigheid en relevantie) in de inhoud die door het model wordt gegenereerd voor een specifieke gebruikersvraag. In eerdere lessen hebben we technieken besproken zoals prompt engineering en retrieval-augmented generation, die proberen het probleem op te lossen door _de invoerprompt van het bestaande model te wijzigen_.

In de les van vandaag bespreken we een derde techniek, **fijnstemmen**, die probeert de uitdaging aan te pakken door _het model zelf opnieuw te trainen_ met aanvullende gegevens. Laten we de details bekijken.

## Leerdoelen

Deze les introduceert het concept van fijnstemmen voor vooraf getrainde taalmodellen, verkent de voordelen en uitdagingen van deze aanpak en biedt richtlijnen over wanneer en hoe je fijnstemmen kunt gebruiken om de prestaties van je generatieve AI-modellen te verbeteren.

Aan het einde van deze les zou je de volgende vragen moeten kunnen beantwoorden:

- Wat is fijnstemmen voor taalmodellen?
- Wanneer en waarom is fijnstemmen nuttig?
- Hoe kan ik een vooraf getraind model fijnstemmen?
- Wat zijn de beperkingen van fijnstemmen?

Klaar? Laten we beginnen.

## Geïllustreerde Gids

Wil je een overzicht van wat we gaan behandelen voordat we erin duiken? Bekijk deze geïllustreerde gids die de leerreis voor deze les beschrijft - van het leren van de kernconcepten en motivatie voor fijnstemmen, tot het begrijpen van het proces en de beste praktijken voor het uitvoeren van de fijnstemtaak. Dit is een fascinerend onderwerp om te verkennen, dus vergeet niet de [Resources](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) pagina te bekijken voor aanvullende links om je zelfgestuurde leerreis te ondersteunen!

![Geïllustreerde Gids voor Fijnstemmen van Taalmodellen](../../../translated_images/18-fine-tuning-sketchnote.11b21f9ec8a703467a120cb79a28b5ac1effc8d8d9d5b31bbbac6b8640432e14.nl.png)

## Wat is fijnstemmen voor taalmodellen?

Grote taalmodellen zijn per definitie _vooraf getraind_ op grote hoeveelheden tekst afkomstig van diverse bronnen, waaronder het internet. Zoals we in eerdere lessen hebben geleerd, hebben we technieken nodig zoals _prompt engineering_ en _retrieval-augmented generation_ om de kwaliteit van de antwoorden van het model op de vragen ("prompts") van de gebruiker te verbeteren.

Een populaire techniek binnen prompt engineering houdt in dat je het model meer richtlijnen geeft over wat er wordt verwacht in het antwoord, door _instructies_ te geven (expliciete richtlijnen) of _een paar voorbeelden te geven_ (impliciete richtlijnen). Dit wordt _few-shot learning_ genoemd, maar het heeft twee beperkingen:

- De tokenlimieten van het model kunnen het aantal voorbeelden dat je kunt geven beperken en daarmee de effectiviteit.
- De kosten van tokens kunnen het duur maken om voorbeelden toe te voegen aan elke prompt, wat de flexibiliteit beperkt.

Fijnstemmen is een gangbare praktijk in machineleersystemen waarbij we een vooraf getraind model nemen en het opnieuw trainen met nieuwe gegevens om de prestaties te verbeteren voor een specifieke taak. In de context van taalmodellen kunnen we het vooraf getrainde model _fijnstemmen met een zorgvuldig samengestelde set voorbeelden voor een specifieke taak of toepassingsdomein_ om een **aangepast model** te creëren dat mogelijk nauwkeuriger en relevanter is voor die specifieke taak of dat domein. Een bijkomend voordeel van fijnstemmen is dat het ook het aantal benodigde voorbeelden voor few-shot learning kan verminderen - wat het gebruik van tokens en de bijbehorende kosten verlaagt.

## Wanneer en waarom zouden we modellen fijnstemmen?

In _deze_ context, wanneer we het hebben over fijnstemmen, verwijzen we naar **supervised** fijnstemmen waarbij het opnieuw trainen wordt gedaan door **nieuwe gegevens toe te voegen** die geen deel uitmaakten van de oorspronkelijke trainingsdataset. Dit verschilt van een unsupervised fijnstemmen aanpak, waarbij het model opnieuw wordt getraind op de oorspronkelijke gegevens, maar met andere hyperparameters.

Het belangrijkste om te onthouden is dat fijnstemmen een geavanceerde techniek is die een bepaald niveau van expertise vereist om de gewenste resultaten te behalen. Als het verkeerd wordt uitgevoerd, kan het mogelijk niet de verwachte verbeteringen opleveren en zelfs de prestaties van het model voor je doelgebied verslechteren.

Voordat je leert "hoe" je taalmodellen kunt fijnstemmen, moet je weten "waarom" je deze route zou moeten nemen en "wanneer" je het proces van fijnstemmen moet starten. Begin met jezelf de volgende vragen te stellen:

- **Gebruiksscenario**: Wat is je _gebruiksscenario_ voor fijnstemmen? Welk aspect van het huidige vooraf getrainde model wil je verbeteren?
- **Alternatieven**: Heb je _andere technieken_ geprobeerd om de gewenste resultaten te bereiken? Gebruik ze om een basislijn voor vergelijking te creëren.
  - Prompt engineering: Probeer technieken zoals few-shot prompting met voorbeelden van relevante promptantwoorden. Evalueer de kwaliteit van de antwoorden.
  - Retrieval Augmented Generation: Probeer prompts te verrijken met zoekresultaten die zijn opgehaald door je gegevens te doorzoeken. Evalueer de kwaliteit van de antwoorden.
- **Kosten**: Heb je de kosten voor fijnstemmen geïdentificeerd?
  - Afstembaarheid - is het vooraf getrainde model beschikbaar voor fijnstemmen?
  - Inspanning - voor het voorbereiden van trainingsgegevens, evalueren en verfijnen van het model.
  - Rekenkracht - voor het uitvoeren van fijnstemjobs en het implementeren van het fijngetunede model.
  - Gegevens - toegang tot voldoende kwalitatieve voorbeelden voor impact van fijnstemmen.
- **Voordelen**: Heb je de voordelen van fijnstemmen bevestigd?
  - Kwaliteit - presteerde het fijngetunede model beter dan de basislijn?
  - Kosten - vermindert het het gebruik van tokens door prompts te vereenvoudigen?
  - Uitbreidbaarheid - kun je het basismodel hergebruiken voor nieuwe domeinen?

Door deze vragen te beantwoorden, zou je moeten kunnen beslissen of fijnstemmen de juiste aanpak is voor jouw gebruiksscenario. Idealiter is de aanpak alleen geldig als de voordelen opwegen tegen de kosten. Zodra je besluit door te gaan, is het tijd om na te denken over _hoe_ je het vooraf getrainde model kunt fijnstemmen.

Wil je meer inzicht in het besluitvormingsproces? Bekijk [To fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Hoe kunnen we een vooraf getraind model fijnstemmen?

Om een vooraf getraind model fijn te stemmen, heb je nodig:

- een vooraf getraind model om fijn te stemmen
- een dataset om te gebruiken voor fijnstemmen
- een trainingsomgeving om de fijnstemtaak uit te voeren
- een hostingomgeving om het fijngetunede model te implementeren

## Fijnstemmen in de praktijk

De volgende bronnen bieden stapsgewijze tutorials om je door een echt voorbeeld te leiden met een geselecteerd model en een zorgvuldig samengestelde dataset. Om deze tutorials te doorlopen, heb je een account nodig bij de specifieke provider, samen met toegang tot het relevante model en de datasets.

| Provider     | Tutorial                                                                                                                                                                       | Beschrijving                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Hoe chatmodellen fijn te stemmen](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)            | Leer een `gpt-35-turbo` fijn te stemmen voor een specifiek domein ("receptassistent") door trainingsgegevens voor te bereiden, de fijnstemtaak uit te voeren en het fijngetunede model te gebruiken voor inferentie.                                                                                                                                                                                                                  |
| Azure OpenAI | [GPT 3.5 Turbo fijnstemmen tutorial](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Leer een `gpt-35-turbo-0613` model **op Azure** fijn te stemmen door stappen te nemen om trainingsgegevens te maken en te uploaden, de fijnstemtaak uit te voeren. Implementeer en gebruik het nieuwe model.                                                                                                                                                                                                                          |
| Hugging Face | [Fijnstemmen van LLMs met Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                             | Deze blogpost begeleidt je bij het fijnstemmen van een _open LLM_ (bijv. `CodeLlama 7B`) met behulp van de [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) bibliotheek & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst]) met open [datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) op Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Fijnstemmen van LLMs met AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                       | AutoTrain (of AutoTrain Advanced) is een Python-bibliotheek ontwikkeld door Hugging Face waarmee fijnstemmen voor veel verschillende taken mogelijk is, inclusief LLM fijnstemmen. AutoTrain is een no-code oplossing en fijnstemmen kan worden gedaan in je eigen cloud, op Hugging Face Spaces of lokaal. Het ondersteunt zowel een webgebaseerde GUI, CLI als training via yaml-configuratiebestanden.                             |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Opdracht

Selecteer een van de bovenstaande tutorials en doorloop deze. _We kunnen een versie van deze tutorials repliceren in Jupyter Notebooks in deze repository, alleen ter referentie. Gebruik de originele bronnen direct om de meest recente versies te verkrijgen_.

## Goed gedaan! Ga door met leren.

Na het voltooien van deze les, bekijk onze [Generative AI Learning collectie](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je kennis over Generatieve AI verder uit te breiden!

Gefeliciteerd!! Je hebt de laatste les van de v2-serie van deze cursus voltooid! Stop niet met leren en bouwen. \*\*Bekijk de [RESOURCES](RESOURCES.md?WT.mc_id=academic-105485-koreyst) pagina voor een lijst met aanvullende suggesties specifiek voor dit onderwerp.

Onze v1-serie lessen is ook bijgewerkt met meer opdrachten en concepten. Neem dus even de tijd om je kennis op te frissen - en deel alsjeblieft [je vragen en feedback](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) om ons te helpen deze lessen voor de community te verbeteren.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.