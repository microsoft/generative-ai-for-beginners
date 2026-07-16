# Ehitamine Meta perekonna mudelitega 

## Sissejuhatus 

See õppetund käsitleb: 

- Kaht peamist Meta perekonna mudelit uurimine - Llama 3.1 ja Llama 3.2 
- Iga mudeli kasutusjuhtude ja olukordade mõistmine 
- Koodi näidis, mis näitab iga mudeli unikaalseid omadusi 


## Meta perekonna mudelid 

Selles õppetükis uurime kahte Meta perekonna või "Llama karja" mudelit - Llama 3.1 ja Llama 3.2.

Need mudelid on erinevates variantides ja on saadaval [Microsoft Foundry Models kataloogis](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Märkus:** GitHub Models lõpetab tegevuse 2026. aasta juuli lõpus. Lisateavet AI mudelite prototüüpimiseks kasutamise kohta leiate [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) kohta.

Mudeli variandid: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Märkus: Llama 3 on saadaval ka Microsoft Foundry Modelsis, kuid seda õppetundi ei käsitleta*

## Llama 3.1 

405 miljardi parameetriga kuulub Llama 3.1 avatud lähtekoodiga LLM-ide kategooriasse. 

Mudel on varasema väljaande Llama 3 uuendus, pakkudes: 

- Suuremat kontekstiakent - 128k tokenit vs 8k tokenit 
- Suuremat maksimaalset väljundtokenite arvu - 4096 vs 2048 
- Parem mitmekeelne tugi - tänu treeningtokenite arvu suurenemisele 

Need võimaldavad Llama 3.1-l käsitleda keerulisemaid kasutusjuhtumeid GenAI rakenduste loomisel, sealhulgas: 
- Natiivfunktsioonide kutsumine - võimalus kutsuda LLM-i töövoost väljaspool asuvaid tööriistu ja funktsioone 
- Parem RAG-tulemuslikkus - tänu suuremale kontekstiaknale 
- Sünteetiline andmete genereerimine - võime luua efektiivseid andmeid selliste ülesannete jaoks nagu täiendõpe 

### Natiivfunktsioonide kutsumine 

Llama 3.1 on täpsustatud nii, et ta oleks funktsioonide või tööriistakutsete tegemisel tõhusam. Samuti on tal kaks sisseehitatud tööriista, mida mudel saab kasutaja vihje põhjal kasutada. Need tööriistad on: 

- **Brave Search** - saab kasutada ajakohase teabe, nagu ilm, leidmiseks veebipäringu abil 
- **Wolfram Alpha** - saab kasutada keerukamate matemaatiliste arvutuste tegemiseks, seega pole vaja ise funktsioone kirjutada. 

Saate luua ka oma kohandatud tööriistu, mida LLM saab kutsuda. 

Järgmises koodi näites: 

- Määratleme süsteemivihjes olemasolevad tööriistad (brave_search, wolfram_alpha). 
- Saadame kasutajapäringu, mis küsib teatud linna ilmaolude kohta. 
- LLM vastab tööriistakutsega Brave Search tööriistale, mis näeb välja selline `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Märkus: see näide teeb ainult tööriistakutse, kui soovite tulemusi saada, peate looma tasuta konto Brave API lehel ja määratlema funktsiooni ennast.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Hankige need oma Microsoft Foundry projekti "Ülevaade" lehelt
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Meta-Llama-3.1-405B-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)


tool_prompt=f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Environment: ipython
Tools: brave_search, wolfram_alpha
Cutting Knowledge Date: December 2023
Today Date: 23 July 2024

You are a helpful assistant<|eot_id|>
"""

messages = [
    SystemMessage(content=tool_prompt),
    UserMessage(content="What is the weather in Stockholm?"),

]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```

## Llama 3.2 

Kuigi Llama 3.1 on LLM, on sellel üks piirang - puudub mitmemoodilisus. See tähendab, et puudub võime kasutada erinevat tüüpi sisendeid, nagu pildid vihjetena, ning pakkuda vastuseid. See võime on üks peamisi Llama 3.2 omadusi. Nende omaduste hulka kuuluvad ka: 

- Mitmemoodilisus - võimalus hinnata nii teksti kui ka pildipõhiseid vihjeid 
- Väikese ja keskmise suurusega variandid (11B ja 90B) - pakuvad paindlikke paigaldusvõimalusi, 
- Ainult teksti variandid (1B ja 3B) - võimaldavad mudeli juurutamist ääre-/mobiilseadmetes ja pakuvad madalat latentsust 

Mitmemoodiline tugi tähistab suurt sammu avatud lähtekoodiga mudelite maailmas. Järgmine näide võtab nii pildi kui ka teksti vihjena, et saada Llama 3.2 90B-lt pildi analüüs. 


### Mitmemoodiline tugi Llama 3.2-ga

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    SystemMessage,
    UserMessage,
    TextContentItem,
    ImageContentItem,
    ImageUrl,
    ImageDetailLevel,
)
from azure.core.credentials import AzureKeyCredential

# Hankige need oma Microsoft Foundry projekti lehelt "Ülevaade"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Llama-3.2-90B-Vision-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(
            content="You are a helpful assistant that describes images in details."
        ),
        UserMessage(
            content=[
                TextContentItem(text="What's in this image?"),
                ImageContentItem(
                    image_url=ImageUrl.load(
                        image_file="sample.jpg",
                        image_format="jpg",
                        detail=ImageDetailLevel.LOW)
                ),
            ],
        ),
    ],
    model=model_name,
)

print(response.choices[0].message.content)
```

## Õppimine siin ei lõppe, jätka teekonda

Pärast selle õppetunni lõpetamist vaata meie [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), et jätkata oma generatiivse tehisintellekti teadmiste taseme tõstmist!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->