# Ehitus Meta pere mudelitega 

## Sissejuhatus 

See õppetund käsitleb: 

- Kaks peamist Meta pere mudelit - Llama 3.1 ja Llama 3.2 avastamine 
- Iga mudeli kasutusjuhtude ja stsenaariumide mõistmine 
- Koodinäide iga mudeli ainulaadsete funktsioonide demonstreerimiseks 


## Meta mudelite perekond 

Selles õppetunnis uurime kahte mudelit Meta perekonnast ehk "Llama karjast" - Llama 3.1 ja Llama 3.2.

Need mudelid on erinevates variatsioonides ning on saadaval [Microsoft Foundry Models kataloogis](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Märkus:** GitHubi mudelid lõpetavad töö 2026. aasta juuli lõpus. Siin on rohkem teavet [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) kasutamise kohta AI mudelite prototüüpimiseks.

Mudeli variandid: 
- Llama 3.1 - 70B juhendatud 
- Llama 3.1 - 405B juhendatud 
- Llama 3.2 - 11B nägemise juhendatud 
- Llama 3.2 - 90B nägemise juhendatud 

*Märkus: Llama 3 on samuti saadaval Microsoft Foundry Models’is, kuid seda õppetundi ei käsitleta*

## Llama 3.1 

405 miljardi parameetriga kuulub Llama 3.1 avatud lähtekoodiga LLM kategooriasse. 

Mudel on täiendatud varasemast Llama 3 väljandest, pakkudes: 

- Suurem kontekstiaken - 128k tokenit versus 8k tokenit 
- Suurem maksimaalne väljundtokenite arv - 4096 vs 2048 
- Parem mitmekeelne tugi - tänu treeningtokenite arvu kasvule 

Need võimaldavad Llama 3.1-l käsitleda keerukamaid kasutusjuhte GenAI rakenduste loomisel, sealhulgas: 
- Looduslik funktsioonide kutsumine - võime kutsuda välistööriistu ja funktsioone väljaspool LLM töövoogu
- Parem RAG sooritus - tänu suuremale kontekstiaknale 
- Sünteetilise andmete genereerimine - võime luua efektiivseid andmeid ülesannete, nagu peenhäälestus, jaoks 

### Looduslik funktsioonide kutsumine 

Llama 3.1 on peenhäälestatud, et olla funktsioonide või tööriistade kutsumise osas tõhusam. Sellel on ka kaks sisseehitatud tööriista, mida mudel saab tuvastada ja mida tuleb kasutada vastavalt kasutaja sisendile. Need tööriistad on: 

- **Brave Search** - saab kasutada ajakohase teabe, näiteks ilma kohta veebipäringuga 
- **Wolfram Alpha** - saab kasutada keerukamate matemaatiliste arvutuste tegemiseks, seega pole vaja oma funktsioone kirjutada. 

Samuti saate luua oma kohandatud tööriistu, mida LLM saab kutsuda. 

Allolevas koodinäites: 

- Määratleme süsteemipõhiselt olemasolevad tööriistad (brave_search, wolfram_alpha). 
- Saadame kasutaja sisendi, mis küsib teatud linna ilma kohta. 
- LLM vastab tööriistakutsena Brave Search tööriistale, mis näeb välja selline `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Märkus: see näide teeb vaid tööriistakutse, kui soovite tulemusi saada, peate looma tasuta konto Brave API lehel ja määratlema funktsiooni ise.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Saate need oma Microsoft Foundry projekti "Ülevaade" lehelt
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

Kuigi Llama 3.1 on LLM, on selle piiranguks mitmemodaalsuse puudumine. See tähendab võimet kasutada erinevat tüüpi sisendeid nagu pildid käsutustele ning pakkuda vastuseid. See võime on üks Llama 3.2 peamistest omadustest. Need omadused hõlmavad ka: 

- Mitmemodaalsus - võime hinnata nii teksti kui ka piltide käske 
- Väike kuni keskmise suurusega variatsioonid (11B ja 90B) - see pakub paindlikke juurutamisvõimalusi, 
- Ainult tekstivariandid (1B ja 3B) - võimaldab mudelit juurutada äärtes / mobiilseadmetes ning tagab madala latentsuse 

Mitmemodaalne tugi tähistab suurt sammu avatud lähtekoodiga mudelite maailmas. Allolev koodinäide võtab nii pildi kui ka tekstikäskluse, et saada analüüs Llama 3.2 90B mudelilt. 


### Mitmemodaalne tugi Llama 3.2-ga

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

# Saate need oma Microsoft Foundry projekti "Ülevaade" lehelt
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

## Õppimine ei peatu siin, jätka teekonda

Pärast selle õppetunni lõpetamist tutvuge meie [Generative AI õppimise kogumikuga](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), et jätkata oma genereeriva AI teadmiste taseme tõstmist!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->