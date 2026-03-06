# Rakentaminen Meta-perheen malleilla

## Johdanto

Tämä oppitunti käsittelee:

- Kahden pääasiallisen Meta-perheen mallin tutkimista - Llama 3.1 ja Llama 3.2
- Ymmärtämistä, mihin käyttötarkoituksiin ja tilanteisiin kukin malli sopii
- Koodiesimerkin näyttämistä kunkin mallin ainutlaatuisista ominaisuuksista

## Meta-perheen mallit

Tässä oppitunnissa tutkimme kahta mallia Meta-perheestä eli "Llama Herd" - Llama 3.1 ja Llama 3.2.

Nämä mallit tulevat eri muunnelmissa ja ovat saatavilla GitHub Model -markkinapaikalla. Tässä on lisätietoja GitHub-mallien käyttämisestä [tekoälymallien prototypointiin](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Mallimuunnelmat:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Huomautus: Llama 3 on myös saatavilla GitHub-malleissa, mutta sitä ei käsitellä tässä oppitunnissa*

## Llama 3.1

Llama 3.1, jossa on 405 miljardia parametria, kuuluu avoimen lähdekoodin LLM-kategoriaan.

Malli on päivitys aiempaan julkaisuun Llama 3 verrattuna ja tarjoaa:

- Suuremman kontekstikentän - 128k tokenia vs 8k tokenia
- Suuremman maksimilähtötokenien määrän - 4096 vs 2048
- Parannetun monikielituen - lisääntyneen koulutustokeneiden määrän vuoksi

Nämä mahdollistavat Llama 3.1:n käsittelemään monimutkaisempia käyttötarkoituksia GenAI-sovelluksia rakennettaessa, kuten:
- Natiivinen funktiokutsu - kyky kutsua ulkoisia työkaluja ja toimintoja LLM-työnkulun ulkopuolella
- Parempi RAG-suorituskyky - suuremman kontekstikentän ansiosta
- Synteettisen datan generointi - kyky luoda tehokasta dataa esimerkiksi hienosäätöä varten

### Natiivinen funktiokutsu

Llama 3.1 on hienosäädetty tekemään funktio- tai työkalukutsuja tehokkaammin. Mallissa on myös kaksi sisäänrakennettua työkalua, jotka malli voi tunnistaa käyttäjän kehotteen perusteella tarvittaviksi. Nämä työkalut ovat:

- **Brave Search** - Voidaan käyttää ajankohtaisten tietojen saamiseen, kuten sää, tekemällä verkkohaku
- **Wolfram Alpha** - Voidaan käyttää monimutkaisempiin matemaattisiin laskelmiin, jolloin omia funktioita ei tarvitse kirjoittaa

Voit myös luoda omia mukautettuja työkaluja, joita LLM voi kutsua.

Alla olevassa koodiesimerkissä:

- Määrittelemme käytettävissä olevat työkalut (brave_search, wolfram_alpha) järjestelmäkehotteessa.
- Lähetetään käyttäjän kehotus, jossa kysytään säätä tietyssä kaupungissa.
- LLM vastaa tekemällä työkalukutsun Brave Search -työkaluun, joka näyttää tältä `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Huomautus: Tämä esimerkki tekee vain työkalukutsun, jos haluat saada tulokset, sinun tulee luoda ilmainen tili Brave API -sivulla ja määritellä funktio itse.

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

Vaikka Llama 3.1 on LLM, sen rajoituksena on monimodaalisuuden puute. Tämä tarkoittaa sitä, ettei se kykene käyttämään erilaisia syötetyyppejä, kuten kuvia kehotteina, eikä antamaan vastauksia niiden perusteella. Tämä kyky on yksi Llama 3.2:n pääominaisuuksista. Näihin ominaisuuksiin kuuluvat myös:

- Monimodaalisuus - kyky arvioida sekä teksti- että kuvakehotteita
- Pienet ja keskisuuret variaatiot (11B ja 90B) - tarjoavat joustavia käyttöönotto vaihtoehtoja,
- Vain tekstiversiot (1B ja 3B) - mahdollistavat mallin käyttöönoton reunalaitteissa/mobiililaitteissa ja tarjoavat pienen viiveen

Monimodaalituki on suuri askel avoimen lähdekoodin mallien maailmassa. Alla oleva koodiesimerkki ottaa sekä kuvan että tekstikehotteen saadakseen analyysin kuvasta Llama 3.2 90B -mallilta.

### Monimodaalituki Llama 3.2:lla

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

## Oppiminen ei pääty tähän, jatka matkaa

Oppitunnin suorittamisen jälkeen tutustu [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) -kokoelmaamme jatkaaksesi Generatiivisen tekoälyn taitojesi kehittämistä!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattikäännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeiden tietojen osalta suositellaan ammattilaisen tekemää käännöstä. Emme ole vastuussa tältä käännökseltä mahdollisesti aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->