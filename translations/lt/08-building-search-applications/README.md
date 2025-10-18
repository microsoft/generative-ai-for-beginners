<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58953c08b8ba7073b836d4270ea0fe86",
  "translation_date": "2025-10-18T02:23:11+00:00",
  "source_file": "08-building-search-applications/README.md",
  "language_code": "lt"
}
-->
# Programų paieškai kūrimas

[![Įvadas į generatyvinį dirbtinį intelektą ir didelius kalbos modelius](../../../translated_images/08-lesson-banner.8fff48c566dad08a1cbb9f4b4a2c16adfdd288a7bbfffdd30770b466fe08c25c.lt.png)](https://youtu.be/W0-nzXjOjr0?si=GcsqiTTvd7RKbo7V)

> > _Spustelėkite aukščiau esančią nuotrauką, kad peržiūrėtumėte šios pamokos vaizdo įrašą_

LLM (dideli kalbos modeliai) yra daugiau nei tik pokalbių robotai ir teksto generavimas. Naudojant įterpimus (Embeddings) taip pat galima kurti paieškos programas. Įterpimai yra skaitmeninės duomenų reprezentacijos, dar vadinamos vektoriais, ir gali būti naudojami semantinei duomenų paieškai.

Šioje pamokoje jūs sukursite paieškos programą mūsų švietimo startuoliui. Mūsų startuolis yra ne pelno siekianti organizacija, teikianti nemokamą išsilavinimą studentams besivystančiose šalyse. Startuolis turi daugybę „YouTube“ vaizdo įrašų, kuriuos studentai gali naudoti mokydamiesi apie dirbtinį intelektą. Startuolis nori sukurti paieškos programą, kuri leistų studentams ieškoti „YouTube“ vaizdo įrašo įvedant klausimą.

Pavyzdžiui, studentas gali įvesti „Kas yra Jupyter Notebooks?“ arba „Kas yra Azure ML“, o paieškos programa pateiks sąrašą „YouTube“ vaizdo įrašų, kurie yra susiję su klausimu. Dar geriau, paieškos programa pateiks nuorodą į vietą vaizdo įraše, kurioje yra atsakymas į klausimą.

## Įvadas

Šioje pamokoje aptarsime:

- Semantinę paiešką ir paiešką pagal raktinius žodžius.
- Kas yra teksto įterpimai.
- Teksto įterpimų indekso kūrimą.
- Teksto įterpimų indekso paiešką.

## Mokymosi tikslai

Baigę šią pamoką, galėsite:

- Skirti semantinę paiešką nuo paieškos pagal raktinius žodžius.
- Paaiškinti, kas yra teksto įterpimai.
- Sukurti programą, naudojančią įterpimus duomenų paieškai.

## Kodėl verta kurti paieškos programą?

Paieškos programos kūrimas padės jums suprasti, kaip naudoti įterpimus duomenų paieškai. Taip pat išmoksite sukurti paieškos programą, kurią studentai galės naudoti norėdami greitai rasti informaciją.

Pamokoje pateikiamas „Embedding Index“ su „YouTube“ transkripcijomis iš „Microsoft [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1)“ „YouTube“ kanalo. „AI Show“ yra „YouTube“ kanalas, mokantis apie dirbtinį intelektą ir mašininį mokymąsi. „Embedding Index“ apima įterpimus kiekvienai „YouTube“ transkripcijai iki 2023 m. spalio mėn. Naudosite „Embedding Index“, kad sukurtumėte paieškos programą mūsų startuoliui. Paieškos programa pateikia nuorodą į vietą vaizdo įraše, kurioje yra atsakymas į klausimą. Tai puikus būdas studentams greitai rasti reikalingą informaciją.

Toliau pateikiamas semantinės užklausos pavyzdys klausimui „Ar galite naudoti rstudio su azure ml?“. Pažiūrėkite į „YouTube“ URL, pamatysite, kad URL turi laiko žymą, kuri nukreipia jus į vietą vaizdo įraše, kurioje yra atsakymas į klausimą.

![Semantinė užklausa klausimui „Ar galite naudoti rstudio su Azure ML“](../../../translated_images/query-results.bb0480ebf025fac69c5179ad4d53b6627d643046838c857dc9e2b1281f1cdeb7.lt.png)

## Kas yra semantinė paieška?

Galbūt dabar klausiate, kas yra semantinė paieška? Semantinė paieška yra paieškos technika, kuri naudoja žodžių semantiką arba prasmę užklausoje, kad pateiktų tinkamus rezultatus.

Štai semantinės paieškos pavyzdys. Tarkime, jūs norite nusipirkti automobilį, galite ieškoti „mano svajonių automobilis“. Semantinė paieška supranta, kad jūs ne „svajojate“ apie automobilį, o ieškote savo „idealaus“ automobilio. Semantinė paieška supranta jūsų ketinimus ir pateikia tinkamus rezultatus. Alternatyva yra „paieška pagal raktinius žodžius“, kuri tiesiog ieškotų svajonių apie automobilius ir dažnai pateiktų nesusijusius rezultatus.

## Kas yra teksto įterpimai?

[Teksto įterpimai](https://en.wikipedia.org/wiki/Word_embedding?WT.mc_id=academic-105485-koreyst) yra teksto reprezentavimo technika, naudojama [natūralios kalbos apdorojime](https://en.wikipedia.org/wiki/Natural_language_processing?WT.mc_id=academic-105485-koreyst). Teksto įterpimai yra semantinės skaitmeninės teksto reprezentacijos. Įterpimai naudojami duomenims reprezentuoti taip, kad mašinai būtų lengva suprasti. Yra daug modelių, skirtų teksto įterpimams kurti, šioje pamokoje mes sutelksime dėmesį į įterpimų generavimą naudojant „OpenAI Embedding Model“.

Štai pavyzdys, įsivaizduokite, kad šis tekstas yra transkripcija iš vienos „AI Show“ „YouTube“ kanalo serijos:

```text
Today we are going to learn about Azure Machine Learning.
```

Mes perduotume tekstą „OpenAI Embedding API“ ir jis grąžintų šį įterpimą, sudarytą iš 1536 skaičių, dar vadinamą vektoriumi. Kiekvienas skaičius vektoriuje atspindi skirtingą teksto aspektą. Dėl trumpumo pateikiame pirmuosius 10 skaičių vektoriuje.

```python
[-0.006655829958617687, 0.0026128944009542465, 0.008792596869170666, -0.02446001023054123, -0.008540431968867779, 0.022071078419685364, -0.010703742504119873, 0.003311325330287218, -0.011632772162556648, -0.02187200076878071, ...]
```

## Kaip sukuriamas įterpimų indeksas?

Šios pamokos įterpimų indeksas buvo sukurtas naudojant keletą „Python“ scenarijų. Scenarijus ir instrukcijas rasite [README](./scripts/README.md?WT.mc_id=academic-105485-koreyst) faile „scripts“ aplanke šiai pamokai. Jums nereikia vykdyti šių scenarijų, kad užbaigtumėte pamoką, nes įterpimų indeksas jau pateiktas.

Scenarijai atlieka šiuos veiksmus:

1. Atsisiunčiama kiekvieno „YouTube“ vaizdo įrašo transkripcija iš [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) grojaraščio.
2. Naudojant [OpenAI Functions](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling?WT.mc_id=academic-105485-koreyst), bandoma išgauti kalbėtojo vardą iš pirmųjų 3 minučių „YouTube“ transkripcijos. Kiekvieno vaizdo įrašo kalbėtojo vardas saugomas įterpimų indekse, pavadintame `embedding_index_3m.json`.
3. Transkripcijos tekstas suskaidomas į **3 minučių teksto segmentus**. Segmentas apima apie 20 žodžių, persidengiančių su kitu segmentu, kad įterpimas nebūtų nutrauktas ir būtų geresnis paieškos kontekstas.
4. Kiekvienas teksto segmentas perduodamas „OpenAI Chat API“, kad tekstas būtų apibendrintas iki 60 žodžių. Apibendrinimas taip pat saugomas įterpimų indekse `embedding_index_3m.json`.
5. Galiausiai segmentų tekstas perduodamas „OpenAI Embedding API“. Įterpimų API grąžina vektorių, sudarytą iš 1536 skaičių, kurie atspindi semantinę segmento prasmę. Segmentas kartu su „OpenAI Embedding“ vektoriumi saugomas įterpimų indekse `embedding_index_3m.json`.

### Vektorinės duomenų bazės

Pamokos paprastumui įterpimų indeksas saugomas JSON faile, pavadintame `embedding_index_3m.json`, ir įkeliamas į „Pandas DataFrame“. Tačiau gamyboje įterpimų indeksas būtų saugomas vektorinėje duomenų bazėje, tokioje kaip [Azure Cognitive Search](https://learn.microsoft.com/training/modules/improve-search-results-vector-search?WT.mc_id=academic-105485-koreyst), [Redis](https://cookbook.openai.com/examples/vector_databases/redis/readme?WT.mc_id=academic-105485-koreyst), [Pinecone](https://cookbook.openai.com/examples/vector_databases/pinecone/readme?WT.mc_id=academic-105485-koreyst), [Weaviate](https://cookbook.openai.com/examples/vector_databases/weaviate/readme?WT.mc_id=academic-105485-koreyst), ir kt.

## Kosininio panašumo supratimas

Mes sužinojome apie teksto įterpimus, kitas žingsnis yra išmokti naudoti teksto įterpimus duomenų paieškai, ypač rasti labiausiai panašius įterpimus pagal pateiktą užklausą naudojant kosininį panašumą.

### Kas yra kosininis panašumas?

Kosininis panašumas yra panašumo matas tarp dviejų vektorių, dar vadinamas „artimiausio kaimyno paieška“. Norint atlikti kosininio panašumo paiešką, reikia _vektorizuoti_ užklausos tekstą naudojant „OpenAI Embedding API“. Tada apskaičiuoti _kosininį panašumą_ tarp užklausos vektoriaus ir kiekvieno vektoriaus įterpimų indekse. Atminkite, kad įterpimų indeksas turi vektorių kiekvienam „YouTube“ transkripcijos teksto segmentui. Galiausiai, rezultatai rūšiuojami pagal kosininį panašumą, o teksto segmentai su didžiausiu kosininiu panašumu yra labiausiai panašūs į užklausą.

Matematiškai kosininis panašumas matuoja kampo kosinusą tarp dviejų vektorių, projektuotų daugiamačiame erdvėje. Šis matavimas yra naudingas, nes jei du dokumentai yra toli vienas nuo kito pagal Euklido atstumą dėl dydžio, jie vis tiek gali turėti mažesnį kampą tarp jų ir todėl didesnį kosininį panašumą. Daugiau informacijos apie kosininio panašumo lygtis rasite [Cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity?WT.mc_id=academic-105485-koreyst).

## Pirmosios paieškos programos kūrimas

Toliau mes išmoksime, kaip sukurti paieškos programą naudojant įterpimus. Paieškos programa leis studentams ieškoti vaizdo įrašo įvedant klausimą. Paieškos programa pateiks sąrašą vaizdo įrašų, kurie yra susiję su klausimu. Paieškos programa taip pat pateiks nuorodą į vietą vaizdo įraše, kurioje yra atsakymas į klausimą.

Šis sprendimas buvo sukurtas ir išbandytas „Windows 11“, „macOS“ ir „Ubuntu 22.04“ naudojant „Python 3.10“ ar naujesnę versiją. „Python“ galite atsisiųsti iš [python.org](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

## Užduotis - paieškos programos kūrimas, kad padėtumėte studentams

Pamokos pradžioje pristatėme savo startuolį. Dabar laikas suteikti studentams galimybę sukurti paieškos programą savo užduotims.

Šioje užduotyje jūs sukursite „Azure OpenAI Services“, kurie bus naudojami paieškos programos kūrimui. Jūs sukursite šiuos „Azure OpenAI Services“. Norėdami užbaigti šią užduotį, jums reikės „Azure“ prenumeratos.

### Pradėkite „Azure Cloud Shell“

1. Prisijunkite prie [Azure portalo](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst).
2. Pasirinkite „Cloud Shell“ piktogramą viršutiniame dešiniajame „Azure“ portalo kampe.
3. Pasirinkite **Bash** kaip aplinkos tipą.

#### Sukurkite išteklių grupę

> Šioms instrukcijoms naudojame išteklių grupę, pavadintą „semantic-video-search“, esančią Rytų JAV.
> Galite pakeisti išteklių grupės pavadinimą, tačiau keisdami išteklių vietą,
> patikrinkite [modelių prieinamumo lentelę](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```shell
az group create --name semantic-video-search --location eastus
```

#### Sukurkite „Azure OpenAI Service“ išteklių

Iš „Azure Cloud Shell“ paleiskite šią komandą, kad sukurtumėte „Azure OpenAI Service“ išteklių.

```shell
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

#### Gaukite galutinį tašką ir raktus, skirtus naudoti šioje programoje

Iš „Azure Cloud Shell“ paleiskite šias komandas, kad gautumėte galutinį tašką ir raktus „Azure OpenAI Service“ ištekliui.

```shell
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

#### Įdiekite „OpenAI Embedding“ modelį

Iš „Azure Cloud Shell“ paleiskite šią komandą, kad įdiegtumėte „OpenAI Embedding“ modelį.

```shell
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name text-embedding-ada-002 \
    --model-name text-embedding-ada-002 \
    --model-version "2"  \
    --model-format OpenAI \
    --sku-capacity 100 --sku-name "Standard"
```

## Sprendimas

Atidarykite [sprendimo užrašų knygelę](./python/aoai-solution.ipynb?WT.mc_id=academic-105485-koreyst) „GitHub Codespaces“ ir vykdykite instrukcijas „Jupyter Notebook“.

Kai paleisite užrašų knygelę, jums bus pasiūlyta įvesti užklausą. Įvesties langas atrodys taip:

![Įvesties langas vartotojui įvesti užklausą](../../../translated_images/notebook-search.1e320b9c7fcbb0bc1436d98ea6ee73b4b54ca47990a1c952b340a2cadf8ac1ca.lt.png)

## Puikus darbas! Tęskite mokymąsi

Baigę šią pamoką, peržiūrėkite mūsų [Generatyvinio dirbtinio intelekto mokymosi kolekciją](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kad toliau gilintumėte savo žinias apie generatyvinį dirbtinį intelektą!

Eikite į 9 pamoką, kurioje nagrinėsime, kaip [kurti vaizdų generavimo programas](../09-building-image-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus interpretavimus, atsiradusius naudojant šį vertimą.