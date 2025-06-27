<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:32:34+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "fi"
}
-->
# Rakentaminen Meta-perheen mallien avulla

## Johdanto

Tämä oppitunti käsittelee:

- Tutustumista kahteen päämalliin Meta-perheessä - Llama 3.1 ja Llama 3.2
- Ymmärtämistä kunkin mallin käyttötapauksista ja skenaarioista
- Koodiesimerkki, joka näyttää kunkin mallin ainutlaatuiset ominaisuudet

## Meta-perheen mallit

Tässä oppitunnissa tutustumme kahteen malliin Meta-perheestä eli "Llama Herdistä" - Llama 3.1 ja Llama 3.2

Nämä mallit ovat saatavilla eri variantteina GitHub Model -markkinapaikalla. Tässä on lisätietoja GitHub-mallien käyttämisestä [AI-mallien prototypointiin](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Mallivariantit:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Huom: Llama 3 on myös saatavilla GitHub-malleissa, mutta sitä ei käsitellä tässä oppitunnissa*

## Llama 3.1

405 miljardilla parametrilla Llama 3.1 kuuluu avoimen lähdekoodin LLM-kategoriaan.

Malli on päivitys aiempaan Llama 3 -julkaisuun tarjoamalla:

- Suurempi kontekstin ikkuna - 128k tokenia vs 8k tokenia
- Suurempi maksimi ulostulotokenien määrä - 4096 vs 2048
- Parempi monikielinen tuki - johtuen koulutustokenien lisääntymisestä

Nämä mahdollistavat Llama 3.1:n käsitellä monimutkaisempia käyttötapauksia GenAI-sovellusten rakentamisessa, mukaan lukien:
- Alkuperäinen funktiokutsu - kyky kutsua ulkoisia työkaluja ja funktioita LLM-työnkulun ulkopuolella
- Parempi RAG-suorituskyky - korkeamman kontekstin ikkunan ansiosta
- Synteettinen datan luonti - kyky luoda tehokasta dataa tehtäviin, kuten hienosäätöön

### Alkuperäinen funktiokutsu

Llama 3.1 on hienosäädetty olemaan tehokkaampi funktioiden tai työkalujen kutsumisessa. Sillä on myös kaksi sisäänrakennettua työkalua, jotka malli voi tunnistaa tarvittaviksi käyttäjän antaman kehotteen perusteella. Nämä työkalut ovat:

- **Brave Search** - Voidaan käyttää ajan tasalla olevan tiedon saamiseen, kuten sää, tekemällä verkkohaku
- **Wolfram Alpha** - Voidaan käyttää monimutkaisempiin matemaattisiin laskelmiin, joten omien funktioiden kirjoittaminen ei ole tarpeen.

Voit myös luoda omia räätälöityjä työkaluja, joita LLM voi kutsua.

Alla olevassa koodiesimerkissä:

- Määrittelemme käytettävissä olevat työkalut (brave_search, wolfram_alpha) järjestelmäkehotteessa.
- Lähetämme käyttäjäkehotteen, joka kysyy sään tietystä kaupungista.
- LLM vastaa työkalukutsulla Brave Search -työkaluun, joka näyttää tältä `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Huom: Tämä esimerkki tekee vain työkalukutsun, jos haluat saada tulokset, sinun on luotava ilmainen tili Brave API -sivulla ja määriteltävä funktio itse*

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

Vaikka Llama 3.1 on LLM, yksi sen rajoituksista on multimodaalisuus. Eli kyky käyttää erilaisia syötetyyppejä, kuten kuvia kehotteina ja antaa vastauksia. Tämä kyky on yksi Llama 3.2:n pääominaisuuksista. Näihin ominaisuuksiin kuuluu myös:

- Multimodaalisuus - kykenee arvioimaan sekä teksti- että kuvakehotteita
- Pieniä ja keskikokoisia variaatioita (11B ja 90B) - tarjoaa joustavia käyttöönotto vaihtoehtoja
- Vain teksti -variaatiot (1B ja 3B) - mahdollistaa mallin käyttöönoton reunalaitteilla / mobiililaitteilla ja tarjoaa alhaisen viiveen

Multimodaalinen tuki edustaa suurta askelta avoimen lähdekoodin mallien maailmassa. Alla oleva koodiesimerkki ottaa sekä kuvan että tekstikehotteen saadakseen kuvan analyysin Llama 3.2 90B:ltä.

### Multimodaalinen tuki Llama 3.2:n kanssa

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

Kun olet suorittanut tämän oppitunnin, tutustu [Generative AI Learning -kokoelmaan](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi Generative AI -tietämyksesi kehittämistä!

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää auktoritatiivisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.