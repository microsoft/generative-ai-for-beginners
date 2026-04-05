# Kūrimas su Meta šeimos modeliais

## Įvadas

Ši pamoka apims:

- Du pagrindinius Meta šeimos modelius - Llama 3.1 ir Llama 3.2
- Kiekvieno modelio naudojimo atvejų ir scenarijų supratimą
- Kodo pavyzdį, rodantį kiekvieno modelio unikalias savybes

## Meta šeimos modeliai

Šioje pamokoje nagrinėsime 2 modelius iš Meta šeimos arba „Llama Herd“ – Llama 3.1 ir Llama 3.2.

Šie modeliai yra įvairių variantų ir yra prieinami GitHub Modelių rinkoje. Daugiau informacijos apie GitHub modelių naudojimą norint [prototipuoti su DI modeliais](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Modelių variantai:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Pastaba: Llama 3 taip pat yra prieinama GitHub modeliuose, tačiau ši pamoka jos neapims*

## Llama 3.1

Turint 405 milijardus parametrų, Llama 3.1 priskiriama atviro kodo LLM kategorijai.

Modelis yra atnaujinimas ankstesnės versijos Llama 3, kurio privalumai yra:

- Didesnė konteksto sritis - 128k žodžių vietoje 8k žodžių
- Didžiausias išeinančių žodžių skaičius - 4096 vietoje 2048
- Geresnė daugiakalbė palaikymas - dėl didesnio apmokymo žodžių kiekio

Tai leidžia Llama 3.1 tvarkyti sudėtingesnius naudojimo atvejus kuriant GenAI programas, įskaitant:
- Vietinis funkcijų kvietimas - galimybė kviesti išorinius įrankius ir funkcijas už LLM darbo eigos ribų
- Geresnį RAG veikimą - dėl didesnės konteksto srities
- Sintetinį duomenų generavimą - galimybė kurti efektyvius duomenis tokioms užduotims kaip fino reguliavimas

### Vietinis funkcijų kvietimas

Llama 3.1 buvo pritaikytas atlikti funkcijų ar įrankių kvietimus efektyviau. Ji taip pat turi du įmontuotus įrankius, kuriuos modelis gali identifikuoti kaip naudojamus pagal vartotojo užklausą. Šie įrankiai yra:

- **Brave Search** - gali būti naudojamas norint gauti atnaujintą informaciją, pvz., apie orą, atliekant internetinę paiešką
- **Wolfram Alpha** - naudojamas sudėtingesniems matematiniams skaičiavimams, todėl nereikia rašyti savo funkcijų

Taip pat galite sukurti savo pasirinktinius įrankius, kuriuos LLM gali kviesti.

Žemiau pateiktame kodo pavyzdyje:

- Apibrėžiame turimus įrankius (brave_search, wolfram_alpha) sistemos užklausoje.
- Siunčiame vartotojo užklausą, klausdami apie tam tikro miesto orą.
- LLM atsakys kviesdamas Brave Search įrankį, kuris atrodys taip: `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Pastaba: Šis pavyzdys tik atlieka įrankio kvietimą, jei norite gauti rezultatus, turėsite susikurti nemokamą paskyrą Brave API puslapyje ir apibrėžti pačią funkciją.

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

Nors Llama 3.1 yra LLM, viena jo ribojimų yra daugiaplanoniškumo nebuvimas. Kitaip tariant, negalėjimas naudoti skirtingų įvesties tipų, pvz., paveikslėlių kaip užklausų ir pateikti atsakymus. Ši savybė yra viena pagrindinių Llama 3.2 ypatybių. Kitos funkcijos apima:

- Daugiaplanoniškumas - gebėjimas vertinti tiek teksto, tiek paveikslėlių užklausas
- Mažo ir vidutinio dydžio variantai (11B ir 90B) - suteikia lanksčias diegimo galimybes,
- Tik tekstui skirti variantai (1B ir 3B) - leidžia modelį naudoti krašto / mobiliuosiuose įrenginiuose ir suteikia mažą delsą

Daugiaplanoniškumo palaikymas yra didelis žingsnis atvirojo kodo modelių pasaulyje. Žemiau pateiktas kodo pavyzdys naudoja tiek paveikslėlį, tiek teksto užklausą, norint gauti Llama 3.2 90B paveikslėlio analizę.

### Daugiaplanoniškumo palaikymas su Llama 3.2

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

## Mokymasis čia nesibaigia, tęskite kelionę

Baigę šią pamoką, apsilankykite mūsų [Generatyvus DI mokymosi kolekcijoje](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ir toliau gilinkite savo žinias apie generatyvų DI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba laikomas autoritetingu šaltiniu. Esant kritinei informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojant šį vertimą.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->