# Rakentaminen Meta Family -malleilla

## Johdanto

Tässä oppitunnissa käsitellään:

- Tutustuminen kahteen pääasialliseen Meta-perhemalliin - Llama 3.1 ja Llama 3.2, sekä tällä hetkellä käytössä oleviin vaihtoehtoihin koodiesimerkeissä (Llama 3.3 ja Llama 4) 
- Ymmärtäminen kunkin mallin käyttötarkoituksista ja -tilanteista 
- Koodiesimerkki, joka näyttää kunkin mallin ainutlaatuiset ominaisuudet 


## Meta Family -mallit

Tässä oppitunnissa tutustumme kahteen malliin Meta-perheestä eli "Llama Herd" -sarjasta - Llama 3.1 ja Llama 3.2. Suoritettavat koodiesimerkit käyttävät Llama 3.3:ta ja Llama 4:ää, jotka ovat tällä hetkellä saatavilla Microsoft Foundry Models -katalogissa.

Nämä mallit ovat saatavilla eri versioina [Microsoft Foundry Models -katalogissa](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Huom:** GitHub Models poistuu käytöstä heinäkuun 2026 lopussa. Lisätietoja pienoismallien tekemisestä voit lukea käyttämällä [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst).

> **Huom:** Tämä oppitunti kirjoitettiin alun perin tiettyjen malliversioiden (Llama 3.1 70B/405B Instruct, Llama 3.2 11B/90B Vision Instruct) pohjalta, mutta ne on sittemmin poistettu Microsoft Foundry Models -katalogista. Alla olevat koodiesimerkit käyttävät `Llama-3.3-70B-Instruct` ja `Llama-4-Scout-17B-16E-Instruct`, jotka ovat tällä hetkellä saatavilla olevia vaihtoehtoja Microsoft Foundry Models -katalogissa, joten ne toimivat edelleen.

Mallivariaatiot (kuten alun perin käsitelty tässä oppitunnissa): 
- Llama 3.1 - 70B Instruct (eläköitynyt) 
- Llama 3.1 - 405B Instruct (eläköitynyt) 
- Llama 3.2 - 11B Vision Instruct (eläköitynyt) 
- Llama 3.2 - 90B Vision Instruct (eläköitynyt) 

Tällä hetkellä koodiesimerkeissä käytettävissä olevat vaihtoehdot: 
- Llama 3.3 - 70B Instruct (`Llama-3.3-70B-Instruct`) 
- Llama 4 Scout - 17B 16E Instruct (`Llama-4-Scout-17B-16E-Instruct`) 

*Huomautus: Yllä käsitellyt Llama 3 -variantit on säilytetty historiallisena kontekstina, eikä niitä ole enää saatavilla Microsoft Foundry Modelsissa.*

## Llama 3.1

405 miljardilla parametrillaan Llama 3.1 kuuluu avoimen lähdekoodin LLM-kategoriaan.

Malli on päivitys aiempaan Llama 3 -versioon ja tarjoaa:

- Suuremman konteksti-ikkunan - 128k tokenia vs 8k tokenia
- Suuremman maksimiulostettujen tokenien määrän - 4096 vs 2048
- Parempi monikielinen tuki - johtuen koulutustokeneiden lisääntymisestä

Nämä ominaisuudet antavat Llama 3.1:lle kyvyn käsitellä monimutkaisempia käyttötapauksia GenAI-sovelluksissa, mukaan lukien:
- Natiivitoimintojen kutsuminen - mahdollisuus kutsua ulkoisia työkaluja ja toimintoja LLM-työnkulun ulkopuolella
- Parempi RAG-suorituskyky - johtuen suuremmasta konteksti-ikkunasta
- Syntetisen datan generointi - kyky luoda tehokasta dataa tehtäviin, kuten hienosäätöön

### Natiivitoimintojen kutsuminen

Llama 3.1 on hienosäädetty toimimaan tehokkaammin toimintojen tai työkalujen kutsumisessa. Sillä on myös kaksi sisäänrakennettua työkalua, jotka malli voi tunnistaa käyttäjän kehotteen perusteella tarvittaviksi. Nämä työkalut ovat:

- **Brave Search** - Voidaan käyttää saadakseen ajantasaisia tietoja, kuten sää, tekemällä verkkohaku
- **Wolfram Alpha** - Voidaan käyttää monimutkaisempiin matemaattisiin laskuihin, joten omien funktioiden kirjoittaminen ei ole tarpeen

Voit myös luoda omia räätälöityjä työkaluja, joita LLM voi kutsua.

Seuraavassa koodiesimerkissä:

- Määritämme käytettävissä olevat työkalut (brave_search, wolfram_alpha) järjestelmän kehotteessa.
- Lähetetään käyttäjän kehotus, joka kysyy säätä tietyssä kaupungissa.
- LLM vastaa kutsumalla Brave Search -työkalua, joka näyttää tältä `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Huom: Tämä esimerkki tekee vain työkalukutsun; jos haluat saada tulokset, sinun täytyy luoda ilmainen tili Brave API -sivulla ja määritellä itse funktio.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Meta-Llama-3.1-405B-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-3.3-70B-Instruct, a currently available alternative, instead
model_name = "Llama-3.3-70B-Instruct"

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

Vaikka Llama 3.1 on LLM, sen rajallisuus on multimodaalisuuden puute. Eli kyvyttömyys käyttää erilaisia syötetyyppejä, kuten kuvia kehotteina ja antaa vastauksia. Tämä kyky on yksi Llama 3.2:n pääominaisuuksista. Näihin ominaisuuksiin kuuluu myös:

- Multimodaalisuus - kykenee arvioimaan sekä teksti- että kuvatulosteita
- Pienet ja keskisuuret kokovaihtoehdot (11B ja 90B) - tarjoaa joustavia käyttöönotto vaihtoehtoja,
- Vain tekstiversiot (1B ja 3B) - mahdollistaa mallin käyttöönoton reunalaitteissa/mobiililaitteissa ja tarjoaa pienen viiveen

Monimuotoinen tuki edustaa suurta edistysaskelta avoimen lähdekoodin mallien maailmassa. Alla oleva koodiesimerkki ottaa vastaan sekä kuvan että tekstikyselyn saadakseen analyysin kuvasta. Koska Llama 3.2 90B Vision Instruct on poistettu käytöstä, esimerkissä käytetään `Llama-4-Scout-17B-16E-Instruct`, tällä hetkellä saatavilla olevaa natiivisti monimuotoista vaihtoehtoa. 


### Multimodaalinen tuki Llama 3.2:lla

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

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Llama-3.2-90B-Vision-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-4-Scout-17B-16E-Instruct, a currently available natively multimodal alternative, instead
model_name = "Llama-4-Scout-17B-16E-Instruct"

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

Oppitunnin suorittamisen jälkeen tutustu [Generative AI Learning -kokoelmaamme](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi generatiivisen tekoälyn osaamisesi kehittämistä!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->