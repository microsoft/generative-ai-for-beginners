<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-10-11T11:35:22+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "et"
}
-->
# Meta perekonna mudelitega töötamine

## Sissejuhatus

Selles õppetükis käsitletakse:

- Kahe peamise Meta perekonna mudeli - Llama 3.1 ja Llama 3.2 - uurimist
- Iga mudeli kasutusjuhtude ja stsenaariumide mõistmist
- Koodinäidet, mis näitab iga mudeli unikaalseid omadusi

## Meta perekonna mudelid

Selles õppetükis uurime kahte Meta perekonna mudelit ehk "Llama karja" - Llama 3.1 ja Llama 3.2.

Need mudelid on saadaval erinevates variantides ja leitavad GitHub Modelsi turul. Siin on rohkem teavet GitHub Models platvormi kasutamise kohta [AI mudelite prototüüpimiseks](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Mudelivariandid:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*NB! Llama 3 on samuti saadaval GitHub Models platvormil, kuid seda selles õppetükis ei käsitleta.*

## Llama 3.1

405 miljardi parameetriga Llama 3.1 kuulub avatud lähtekoodiga LLM-i kategooriasse.

See mudel on täiendus varasemale Llama 3 versioonile, pakkudes:

- Suuremat kontekstiakent - 128k tokenit vs 8k tokenit
- Suuremat maksimaalset väljundtokenite arvu - 4096 vs 2048
- Paremat mitmekeelset tuge - tänu treeningtokenite arvu suurenemisele

Need omadused võimaldavad Llama 3.1-l käsitleda keerukamaid kasutusjuhtumeid GenAI rakenduste loomisel, sealhulgas:
- Natiivne funktsioonikutsumine - võimalus kutsuda väliseid tööriistu ja funktsioone väljaspool LLM-i töövoogu
- Parem RAG jõudlus - tänu suuremale kontekstiaknale
- Sünteetiliste andmete genereerimine - võime luua tõhusaid andmeid näiteks peenhäälestuseks

### Natiivne funktsioonikutsumine

Llama 3.1 on peenhäälestatud, et olla tõhusam funktsioonide või tööriistade kutsumisel. Sellel on ka kaks sisseehitatud tööriista, mida mudel suudab kasutaja sisendi põhjal ära tunda ja kasutada. Need tööriistad on:

- **Brave Search** - saab kasutada ajakohase teabe, näiteks ilma, hankimiseks veebist otsides
- **Wolfram Alpha** - saab kasutada keerukamate matemaatiliste arvutuste tegemiseks, nii et oma funktsioonide kirjutamine pole vajalik

Samuti saate luua oma kohandatud tööriistu, mida LLM saab kutsuda.

Allolevas koodinäites:

- Määratleme süsteemi sisendis saadaval olevad tööriistad (brave_search, wolfram_alpha).
- Saadame kasutaja sisendi, mis küsib ilma kohta teatud linnas.
- LLM vastab tööriistakutsega Brave Search tööriistale, mis näeb välja selline: `<|python_tag|>brave_search.call(query="Stockholmi ilm")`

*NB! See näide teeb ainult tööriistakutse. Kui soovite tulemusi saada, peate looma tasuta konto Brave API lehel ja määratlema funktsiooni.*

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

Kuigi Llama 3.1 on LLM, on sellel üks piirang - multimodaalsus. See tähendab, et erinevat tüüpi sisendite, näiteks piltide, kasutamine koos tekstiga ja vastuste andmine pole võimalik. See võimekus on üks Llama 3.2 peamisi omadusi. Lisaks sisaldab see mudel järgmisi funktsioone:

- Multimodaalsus - suudab hinnata nii teksti- kui ka pildisisendeid
- Väikesed ja keskmise suurusega variandid (11B ja 90B) - pakuvad paindlikke juurutusvõimalusi
- Ainult tekstivariandid (1B ja 3B) - võimaldavad mudelit juurutada serva-/mobiilseadmetes ja tagavad madala latentsuse

Multimodaalne tugi on suur samm avatud lähtekoodiga mudelite maailmas. Allolev koodinäide kasutab nii pilti kui ka tekstisisendit, et saada Llama 3.2 90B mudelilt pildi analüüs.

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


## Õppimine ei lõpe siin – jätka teekonda

Pärast selle õppetüki läbimist tutvu meie [Generatiivse tehisintellekti õppekollektsiooniga](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), et jätkata oma teadmiste arendamist generatiivse tehisintellekti vallas!

---

**Lahtiütlus**:  
See dokument on tõlgitud tehisintellekti tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsuse, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.