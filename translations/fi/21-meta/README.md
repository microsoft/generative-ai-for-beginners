<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:12:57+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "fi"
}
-->
# Rakentaminen Meta-perheen mallien kanssa

## Johdanto

Tässä oppitunnissa käsitellään:

- Kahden pääasiallisen Meta-perheen mallin, Llama 3.1:n ja Llama 3.2:n, tutkiminen
- Kunkin mallin käyttötapaukset ja skenaariot
- Koodiesimerkki, joka näyttää kunkin mallin ainutlaatuiset ominaisuudet

## Meta-mallien perhe

Tässä oppitunnissa tutkimme kahta mallia Meta-perheestä eli "Llama Herdistä" - Llama 3.1 ja Llama 3.2.

Nämä mallit ovat saatavilla eri muunnelmina GitHub Model -markkinapaikalla. Tässä on lisätietoja GitHub Modelsin käytöstä [prototyyppien luomiseen tekoälymalleilla](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Mallivariantit:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Huom: Llama 3 on myös saatavilla GitHub Modelsissa, mutta sitä ei käsitellä tässä oppitunnissa*

## Llama 3.1

405 miljardilla parametrilla Llama 3.1 kuuluu avoimen lähdekoodin LLM-kategoriaan.

Malli on päivitys aiempaan julkaisuun Llama 3 tarjoamalla:

- Suurempi kontekstin ikkuna - 128k tokenia vs 8k tokenia
- Suurempi maksimiulostulotokenit - 4096 vs 2048
- Parempi monikielinen tuki - johtuen koulutustokenien lisääntymisestä

Nämä mahdollistavat Llama 3.1:n käsitellä monimutkaisempia käyttötapauksia GenAI-sovelluksia rakennettaessa, kuten:
- Alkuperäisten funktiokutsujen tekeminen - kyky kutsua ulkoisia työkaluja ja funktioita LLM-työnkulun ulkopuolella
- Parempi RAG-suorituskyky - suuremman kontekstin ikkunan ansiosta
- Synteettisen datan generointi - kyky luoda tehokasta dataa tehtäviin kuten hienosäätö

### Alkuperäisten funktiokutsujen tekeminen

Llama 3.1 on hienosäädetty tehokkaampaan funktioiden tai työkalujen kutsumiseen. Siinä on myös kaksi sisäänrakennettua työkalua, jotka malli voi tunnistaa tarpeellisiksi käyttää käyttäjän antaman kehotteen perusteella. Nämä työkalut ovat:

- **Brave Search** - Voi käyttää saadakseen ajankohtaista tietoa, kuten säätiedotuksia, suorittamalla verkkohaku
- **Wolfram Alpha** - Voi käyttää monimutkaisempiin matemaattisiin laskutoimituksiin, joten omien funktioiden kirjoittaminen ei ole tarpeen.

Voit myös luoda omia mukautettuja työkaluja, joita LLM voi kutsua.

Alla olevassa koodiesimerkissä:

- Määrittelemme käytettävissä olevat työkalut (brave_search, wolfram_alpha) järjestelmän kehotteessa.
- Lähetämme käyttäjän kehotteen, joka kysyy säästä tietyssä kaupungissa.
- LLM vastaa työkaluhaulla Brave Search -työkaluun, joka näyttää tältä `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Huom: Tämä esimerkki tekee vain työkalukutsun, jos haluat saada tulokset, sinun tulee luoda ilmainen tili Brave API -sivulla ja määritellä funktio itse*

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

Vaikka Llama 3.1 on LLM, sillä on yksi rajoitus, joka on multimodaalisuus. Eli kyky käyttää erilaisia syötteitä, kuten kuvia, kehotteina ja antaa vastauksia. Tämä kyky on yksi Llama 3.2:n pääominaisuuksista. Näihin ominaisuuksiin kuuluvat myös:

- Multimodaalisuus - kyky arvioida sekä teksti- että kuvakehotteita
- Pienet ja keskikokoiset variaatiot (11B ja 90B) - tämä tarjoaa joustavat käyttöönottoasetukset
- Vain teksti -variaatiot (1B ja 3B) - tämä mahdollistaa mallin käyttöönoton reunalla/mobiililaitteilla ja tarjoaa matalan viiveen

Multimodaalituki edustaa suurta askelta avoimen lähdekoodin mallien maailmassa. Alla oleva koodiesimerkki ottaa sekä kuvan että tekstikehotteen saadakseen analyysin kuvasta Llama 3.2 90B:ltä.

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

Tämän oppitunnin suorittamisen jälkeen tutustu [Generatiivisen tekoälyn oppimiskokoelmaan](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi generatiivisen tekoälyn tietämyksesi kehittämistä!

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittistä tietoa varten suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa mahdollisista väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.