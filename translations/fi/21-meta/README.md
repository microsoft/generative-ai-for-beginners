<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:11:01+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "fi"
}
-->
# Rakentaminen Meta Family -malleilla

## Johdanto

Tässä oppitunnissa käsitellään:

- Kaksi pääasiallista Meta Family -mallia – Llama 3.1 ja Llama 3.2
- Mallien käyttötarkoitukset ja tilanteet
- Koodiesimerkki, joka esittelee mallien ainutlaatuiset ominaisuudet

## Meta Family -mallit

Tässä oppitunnissa tutustumme kahteen Meta Family -malliin eli "Llama Herd" -perheen malleihin: Llama 3.1 ja Llama 3.2.

Nämä mallit ovat saatavilla eri versioina GitHub Model -markkinapaikalla. Lisätietoja GitHub-mallien käytöstä [prototyyppien tekemiseen AI-malleilla](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) löytyy linkistä.

Malliversiot:  
- Llama 3.1 – 70B Instruct  
- Llama 3.1 – 405B Instruct  
- Llama 3.2 – 11B Vision Instruct  
- Llama 3.2 – 90B Vision Instruct  

*Huom: Llama 3 on myös saatavilla GitHub-malleissa, mutta sitä ei käsitellä tässä oppitunnissa*

## Llama 3.1

405 miljardin parametrin Llama 3.1 kuuluu avoimen lähdekoodin LLM-malleihin.

Mallissa on parannuksia aiempaan Llama 3 -versioon verrattuna, kuten:

- Suurempi kontekstin ikkuna – 128k tokenia vs. 8k tokenia  
- Suurempi maksimivastaustokenien määrä – 4096 vs. 2048  
- Parempi monikielinen tuki – johtuen lisääntyneestä koulutustokenien määrästä  

Nämä parannukset mahdollistavat Llama 3.1:n käytön monimutkaisemmissa käyttötapauksissa GenAI-sovelluksia rakennettaessa, kuten:  
- Native Function Calling – kyky kutsua ulkoisia työkaluja ja funktioita LLM-työnkulun ulkopuolelta  
- Parempi RAG-suorituskyky – suuremman kontekstin ikkunan ansiosta  
- Synteettinen datan generointi – kyky luoda tehokasta dataa esimerkiksi hienosäätöä varten  

### Native Function Calling

Llama 3.1 on hienosäädetty toimimaan tehokkaammin funktio- tai työkalukutsujen tekemisessä. Mallissa on myös kaksi sisäänrakennettua työkalua, jotka se tunnistaa käytettäväksi käyttäjän kehotteen perusteella. Nämä työkalut ovat:

- **Brave Search** – voi hakea ajankohtaista tietoa, kuten säätä, tekemällä verkkohakuja  
- **Wolfram Alpha** – voi suorittaa monimutkaisempia matemaattisia laskelmia, joten omien funktioiden kirjoittaminen ei ole tarpeen  

Voit myös luoda omia mukautettuja työkaluja, joita LLM voi kutsua.

Alla olevassa koodiesimerkissä:

- Määrittelemme käytettävissä olevat työkalut (brave_search, wolfram_alpha) system-promptissa.  
- Lähetämme käyttäjän kehotteen, joka kysyy tietyn kaupungin säästä.  
- LLM vastaa työkalukutsulla Brave Search -työkaluun, joka näyttää tältä: `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*Huom: Tämä esimerkki tekee vain työkalukutsun. Jos haluat saada tulokset, sinun tulee luoda ilmainen tili Brave API -sivulla ja määritellä funktio itse.*

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

Vaikka Llama 3.1 on LLM, sen rajoituksena on multimodaalisuus, eli kyky käyttää erilaisia syötteitä, kuten kuvia kehotteina ja antaa vastauksia niiden perusteella. Tämä kyky on yksi Llama 3.2:n pääominaisuuksista. Muita ominaisuuksia ovat:

- Multimodaalisuus – kykenee käsittelemään sekä teksti- että kuvasyötteitä  
- Pienet ja keskisuuret versiot (11B ja 90B) – tarjoavat joustavia käyttöönotto vaihtoehtoja  
- Vain tekstiä tukevat versiot (1B ja 3B) – mahdollistavat mallin käytön reunalaitteissa/mobiililaitteissa ja tarjoavat pienen viiveen  

Multimodaalituki on merkittävä askel avoimen lähdekoodin mallien maailmassa. Alla oleva koodiesimerkki käyttää sekä kuva- että tekstikehotetta saadakseen analyysin Llama 3.2 90B -mallilta.

### Multimodaalituki Llama 3.2:lla

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

## Oppiminen ei lopu tähän, jatka matkaa

Oppitunnin jälkeen tutustu [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) -kokoelmaamme ja jatka Generative AI -osaamisesi kehittämistä!

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.