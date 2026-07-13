# Rakentaminen Meta-perhemalleilla 

## Johdanto 

Tässä oppitunnissa käsitellään: 

- Kaksi pääasiallista Meta-perhemallia - Llama 3.1 ja Llama 3.2 
- Mallien käyttötarkoitukset ja skenaariot 
- Koodiesimerkki, joka näyttää kunkin mallin ainutlaatuiset ominaisuudet 


## Meta-perhemallit 

Tässä oppitunnissa tutustumme kahteen Meta-perheen tai "Llama Herd" -malliin - Llama 3.1 ja Llama 3.2.

Näitä malleja on erilaisina versioina saatavilla [Microsoft Foundry Models -katalogista](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Huom:** GitHub Models lopetetaan heinäkuun 2026 lopussa. Tässä on lisätietoja [Microsoft Foundry Modelsin](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) käytöstä tekoälymallien prototyyppien tekemiseen.

Mallin versiot: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Huom: Llama 3 on myös saatavilla Microsoft Foundry Models -katalogissa, mutta sitä ei käsitellä tässä oppitunnissa*

## Llama 3.1 

Llama 3.1 kuuluu 405 miljardin parametrin avoimen lähdekoodin LLM-mallien luokkaan. 

Malli on päivitys aikaisempaan Llama 3 -versioon tarjoamalla: 

- Suuremman kontekstikkunan - 128k tokenia vs 8k tokenia 
- Suuremman maksimivasteen tokenimäärän - 4096 vs 2048 
- Parempi monikielituki - johtuen koulutustokenien lisääntymisestä 

Nämä mahdollistavat Llama 3.1:n käsitellä monimutkaisempia käyttötapauksia GenAI-sovelluksia rakennettaessa, mukaan lukien: 
- Natiivitoimintojen kutsuminen - kyky kutsua ulkoisia työkaluja ja toimintoja LLM-työnkulun ulkopuolella
- Parempi RAG-suorituskyky - johtuen suuremmasta kontekstikkunasta 
- Synteettinen datan generointi - kyky luoda tehokasta dataa kuten hienosäätöä varten 

### Natiivitoimintojen kutsuminen 

Llama 3.1 on hienosäädetty tehokkaammaksi toiminto- tai työkalukutsujen tekemisessä. Mallissa on myös kaksi sisäänrakennettua työkalua, jotka se voi tunnistaa käyttötilanteen perusteella käyttäjän kehotteesta. Nämä työkalut ovat: 

- **Brave Search** - Voidaan käyttää ajantasaisen tiedon, kuten sään, hakemiseen web-haun avulla 
- **Wolfram Alpha** - Voidaan käyttää monimutkaisempiin matemaattisiin laskutoimituksiin, joten omien funktioiden kirjoittaminen ei ole tarpeen. 

Voit myös luoda omia räätälöityjä työkaluja, joita LLM voi kutsua. 

Seuraavassa esimerkkikoodissa: 

- Määrittelemme järjestelmäkehotteessa käytettävissä olevat työkalut (brave_search, wolfram_alpha). 
- Lähetämme käyttäjäkehotteen, jossa kysytään säätä tietyssä kaupungissa. 
- LLM vastaa työkalukutsulla Brave Search -työkaluun, joka näyttää tältä `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Huom: Tämä esimerkki tekee vain työkalukutsun. Jos haluat saada tulokset, sinun täytyy luoda ilmainen tili Brave API -sivulle ja määritellä funktio itse.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Hanki nämä Microsoft Foundry -projektisi "Yleiskatsaus" -sivulta
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

Vaikka Llama 3.1 onkin LLM, yksi sen rajoituksista on monimuotoisuuden puute. Toisin sanoen kyvyttömyys käyttää erilaisia syötteitä, kuten kuvia kehotteina ja antaa niihin vastauksia. Tämä kyky on yksi Llama 3.2:n pääominaisuuksista. Muita ominaisuuksia ovat:

- Monimuotoisuus - kyky käsitellä sekä teksti- että kuvakehotteita 
- Pienet ja keskisuuret variaatiot (11B ja 90B) - tarjoavat joustavia käyttöönottoasetuksia,
- Vain tekstipohjaiset versiot (1B ja 3B) - mahdollistavat mallin käytön reunalaitteissa / mobiililaitteissa ja tarjoavat alhaisen viiveen 

Monimuotoistuki on merkittävä askel avoimen lähdekoodin mallien maailmassa. Alla oleva koodiesimerkki ottaa sekä kuvan että tekstikehotteen analysoiden kuvaa Llama 3.2 90B:llä. 


### Monimuotoistuki Llama 3.2:lla

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

# Hanki nämä Microsoft Foundry -projektisi "Yleiskatsaus" sivulta
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

## Oppiminen ei lopu tähän, jatka matkaa

Oppitunnin jälkeen tutustu Generative AI Learning -kokoelmaamme osoitteessa [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi generatiivisen tekoälyn osaamisen kehittämistä!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->