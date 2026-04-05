# Meta perekonna mudelitega ehitamine

## Sissejuhatus

Selles õppetükis käsitletakse:

- Kaht peamist Meta perekonna mudelit - Llama 3.1 ja Llama 3.2
- Iga mudeli kasutusjuhtumite ja stsenaariumide mõistmist
- Koodi näidist, mis demonstreerib iga mudeli unikaalseid omadusi

## Meta perekonna mudelid

Selles õppetükis uurime kahte Meta perekonna ehk "Llama karja" mudelit - Llama 3.1 ja Llama 3.2.

Need mudelid on saadaval erinevates variatsioonides ja on kättesaadavad GitHub Modeli turul. Siit leiad lisateavet GitHubi mudelite kasutamise kohta [AI mudelite prototüüpimiseks](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Mudeli variandid:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Märkus: Llama 3 on samuti saadaval GitHub Models, kuid seda õppetükis ei käsitleta*

## Llama 3.1

405 miljardi parameetriga on Llama 3.1 avatud lähtekoodiga LLM kategoorias.

Mudelit on uuendatud võrreldes varasema Llama 3 versiooniga ning see pakub:

- Suuremat kontekstiakent - 128k märki võrreldes 8k märgiga
- Suuremat maksimaalset väljundmärki - 4096 vs 2048
- Parem-mitmekeelsus - tänu treeningmärksõnade arvu suurenemisele

Need võimaldavad Llama 3.1-l käsitleda keerukamaid kasutusjuhtumeid GenAI rakenduste loomisel, sealhulgas:
- Natiivne funktsioonikõne - võime kutsuda väliseid tööriistu ja funktsioone väljaspool LLM-i töövoogu
- Parem RAG tulemuslikkus - tänu suuremale kontekstiaknale
- Sünteetilise andmete genereerimine - võime luua efektiivseid andmeid ülesannete nagu peenhäälestuse jaoks

### Natiivne funktsioonikõne

Llama 3.1 on peenhäälestatud, et olla efektiivsem funktsioonide või tööriistade kutsmisel. Mudelil on ka kaks sisseehitatud tööriista, mida mudel võib identifitseerida vastavalt kasutaja promptile. Need tööriistad on:

- **Brave Search** - saab kasutada värske info saamiseks näiteks ilma kohta, tehes veebipäringu
- **Wolfram Alpha** - saab kasutada keerukamate matemaatiliste arvutuste tegemiseks, seega pole oma funktsioonide kirjutamine vajalik

Sa võid ka luua oma kohandatud tööriistu, mida LLM saab kutsuda.

Järgmises koodi näites:

- Määratleme süsteempromptis saadaval olevad tööriistad (brave_search, wolfram_alpha).
- Saadame kasutajaprompti, kus küsitakse ilmateadet kindlast linnast.
- LLM vastab tööriistakutsega Brave Search tööriista, mis näeb välja selline `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Märkus: See näide kutsub ainult tööriista, kui soovid tulemusi saada, pead looma tasuta konto Brave API lehel ja määratlema funktsiooni ise.*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "meta-llama-3.1-405b-instruct"

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

Kuigi Llama 3.1 on LLM, on selleks piiranguks multimodaalsuse puudumine. See tähendab, et mudel ei saa kasutada erinevat tüüpi sisendit nagu pildid promptidena ega anda vastuseid. See võimekus on üks peamisi Llama 3.2 omadusi. Need omadused hõlmavad ka:

- Multimodaalsus - suudab töödelda nii teksti kui ka piltide promte
- Väikesed kuni keskmise suurusega variandid (11B ja 90B) - pakuvad paindlikke juurutamisvõimalusi
- Ainult tekstipõhised variandid (1B ja 3B) - võimaldavad mudelit juurutada serva- ja mobiilseadmetes ning tagavad madala latentsuse

Multimodaalne tugi tähistab suurt sammu avatud lähtekoodiga mudelite maailmas. Järgmine koodi näide võtab sisendiks nii pildi kui teksti prompti, et saada Llama 3.2 90B mudelilt pildi analüüs.

### Multimodaalne tugi Llama 3.2-ga

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

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
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

## Õppimine siin ei peatu, jätka teekonda

Pärast selle õppetüki lõpetamist vaata meie [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), et jätkata oma Generative AI teadmiste täiendamist!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palun arvestage, et automatiseeritud tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles peaks olema autoriteetne allikas. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->