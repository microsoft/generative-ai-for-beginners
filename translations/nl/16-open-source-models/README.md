<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8b2d4bb727c877ebf9edff8623d16b9",
  "translation_date": "2025-09-06T10:20:15+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "nl"
}
-->
[![Open Source Models](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.nl.png)](https://aka.ms/gen-ai-lesson16-gh?WT.mc_id=academic-105485-koreyst)

## Introductie

De wereld van open-source LLMs is spannend en voortdurend in ontwikkeling. Deze les biedt een diepgaande kijk op open source modellen. Als je op zoek bent naar informatie over hoe propriëtaire modellen zich verhouden tot open source modellen, ga dan naar de les ["Exploring and Comparing Different LLMs"](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Deze les behandelt ook het onderwerp fine-tuning, maar een meer gedetailleerde uitleg vind je in de les ["Fine-Tuning LLMs"](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Leerdoelen

- Begrip krijgen van open source modellen
- Inzicht krijgen in de voordelen van werken met open source modellen
- Verkennen van de open modellen beschikbaar op Hugging Face en de Azure AI Studio

## Wat zijn Open Source Modellen?

Open source software heeft een cruciale rol gespeeld in de groei van technologie in verschillende vakgebieden. De Open Source Initiative (OSI) heeft [10 criteria voor software](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) gedefinieerd om als open source te worden geclassificeerd. De broncode moet openlijk worden gedeeld onder een door de OSI goedgekeurde licentie.

Hoewel de ontwikkeling van LLMs vergelijkbare elementen heeft als het ontwikkelen van software, is het proces niet exact hetzelfde. Dit heeft geleid tot veel discussie in de gemeenschap over de definitie van open source in de context van LLMs. Voor een model om te voldoen aan de traditionele definitie van open source, moeten de volgende gegevens openbaar beschikbaar zijn:

- Datasets die zijn gebruikt om het model te trainen.
- Volledige modelgewichten als onderdeel van de training.
- De evaluatiecode.
- De fine-tuning code.
- Volledige modelgewichten en trainingsstatistieken.

Er zijn momenteel slechts enkele modellen die aan deze criteria voldoen. Het [OLMo-model, gemaakt door het Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) past binnen deze categorie.

Voor deze les zullen we de modellen voortaan "open modellen" noemen, aangezien ze mogelijk niet aan bovenstaande criteria voldoen op het moment van schrijven.

## Voordelen van Open Modellen

**Sterk aanpasbaar** - Omdat open modellen worden vrijgegeven met gedetailleerde trainingsinformatie, kunnen onderzoekers en ontwikkelaars de interne werking van het model aanpassen. Dit maakt het mogelijk om zeer gespecialiseerde modellen te creëren die zijn afgestemd op een specifieke taak of studiegebied. Enkele voorbeelden hiervan zijn codegeneratie, wiskundige operaties en biologie.

**Kosten** - De kosten per token voor het gebruik en implementeren van deze modellen zijn lager dan die van propriëtaire modellen. Bij het bouwen van Generatieve AI-toepassingen moet je de prestaties versus prijs bekijken in relatie tot je specifieke gebruikssituatie.

![Model Cost](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.nl.png)  
Bron: Artificial Analysis

**Flexibiliteit** - Werken met open modellen biedt flexibiliteit in het gebruik van verschillende modellen of het combineren ervan. Een voorbeeld hiervan is de [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst), waar een gebruiker direct in de gebruikersinterface het model kan selecteren dat wordt gebruikt:

![Choose Model](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.nl.png)

## Verkennen van Verschillende Open Modellen

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), ontwikkeld door Meta, is een open model dat geoptimaliseerd is voor chat-gebaseerde toepassingen. Dit komt door de fine-tuning methode, waarbij een grote hoeveelheid dialoog en menselijke feedback is gebruikt. Met deze methode produceert het model meer resultaten die aansluiten bij menselijke verwachtingen, wat zorgt voor een betere gebruikerservaring.

Enkele voorbeelden van fine-tuned versies van Llama zijn [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), die gespecialiseerd is in Japans, en [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), een verbeterde versie van het basismodel.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) is een open model met een sterke focus op hoge prestaties en efficiëntie. Het maakt gebruik van de Mixture-of-Experts aanpak, waarbij een groep gespecialiseerde expertmodellen wordt gecombineerd in één systeem. Afhankelijk van de input worden bepaalde modellen geselecteerd om te worden gebruikt. Dit maakt de berekening effectiever, omdat modellen alleen de inputs behandelen waarin ze gespecialiseerd zijn.

Enkele voorbeelden van fine-tuned versies van Mistral zijn [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), die zich richt op het medische domein, en [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), die wiskundige berekeningen uitvoert.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) is een LLM gemaakt door het Technology Innovation Institute (**TII**). De Falcon-40B is getraind op 40 miljard parameters en heeft aangetoond beter te presteren dan GPT-3 met een lager compute-budget. Dit komt door het gebruik van het FlashAttention-algoritme en multiquery attention, waardoor het geheugenverbruik tijdens inferentie wordt verminderd. Met deze verminderde inferentietijd is de Falcon-40B geschikt voor chattoepassingen.

Enkele voorbeelden van fine-tuned versies van Falcon zijn de [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), een assistent gebouwd op open modellen, en [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), die betere prestaties levert dan het basismodel.

## Hoe te Kiezen

Er is geen eenduidig antwoord voor het kiezen van een open model. Een goed startpunt is het gebruik van de filterfunctie op taak in de Azure AI Studio. Dit helpt je te begrijpen voor welke soorten taken het model is getraind. Hugging Face onderhoudt ook een LLM Leaderboard, dat de best presterende modellen toont op basis van bepaalde metrics.

Als je LLMs wilt vergelijken, is [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) een andere geweldige bron:

![Model Quality](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.nl.png)  
Bron: Artificial Analysis

Bij het werken aan een specifieke gebruikssituatie kan het effectief zijn om te zoeken naar fine-tuned versies die zich richten op hetzelfde gebied. Experimenteren met meerdere open modellen om te zien hoe ze presteren volgens jouw en je gebruikers' verwachtingen is ook een goede praktijk.

## Volgende Stappen

Het beste van open modellen is dat je er snel mee aan de slag kunt. Bekijk de [Azure AI Foundry Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), die een specifieke Hugging Face-collectie bevat met de modellen die we hier hebben besproken.

## Leren stopt hier niet, ga verder met de reis

Na het voltooien van deze les, bekijk onze [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je kennis over Generatieve AI verder uit te breiden!

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.