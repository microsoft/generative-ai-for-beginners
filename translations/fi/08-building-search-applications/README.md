<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58953c08b8ba7073b836d4270ea0fe86",
  "translation_date": "2025-10-17T19:39:33+00:00",
  "source_file": "08-building-search-applications/README.md",
  "language_code": "fi"
}
-->
# Hakusovellusten rakentaminen

[![Johdatus generatiiviseen tekoälyyn ja suuriin kielimalleihin](../../../translated_images/08-lesson-banner.8fff48c566dad08a1cbb9f4b4a2c16adfdd288a7bbfffdd30770b466fe08c25c.fi.png)](https://youtu.be/W0-nzXjOjr0?si=GcsqiTTvd7RKbo7V)

> > _Klikkaa yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon_

Suuret kielimallit (LLM) tarjoavat paljon enemmän kuin chatbotit ja tekstin generointi. Niiden avulla voidaan myös rakentaa hakusovelluksia käyttämällä upotuksia. Upotukset ovat numeerisia esityksiä datasta, joita kutsutaan myös vektoreiksi, ja niitä voidaan käyttää semanttiseen hakuun.

Tässä oppitunnissa rakennat hakusovelluksen koulutusstartupillemme. Startupimme on voittoa tavoittelematon organisaatio, joka tarjoaa ilmaista koulutusta opiskelijoille kehittyvissä maissa. Startupillamme on suuri määrä YouTube-videoita, joita opiskelijat voivat käyttää oppiakseen tekoälystä. Startup haluaa rakentaa hakusovelluksen, jonka avulla opiskelijat voivat etsiä YouTube-videoita kirjoittamalla kysymyksen.

Esimerkiksi opiskelija voisi kirjoittaa 'Mitä ovat Jupyter Notebooks?' tai 'Mikä on Azure ML', ja hakusovellus palauttaa listan YouTube-videoista, jotka liittyvät kysymykseen. Vielä parempaa, hakusovellus palauttaa linkin kohtaan videossa, jossa kysymykseen annetaan vastaus.

## Johdanto

Tässä oppitunnissa käsitellään:

- Semanttinen vs avainsanahaku.
- Mitä ovat tekstin upotukset.
- Tekstin upotusten indeksin luominen.
- Tekstin upotusten indeksin hakeminen.

## Oppimistavoitteet

Kun olet suorittanut tämän oppitunnin, osaat:

- Erottaa semanttisen haun ja avainsanahaun toisistaan.
- Selittää, mitä tekstin upotukset ovat.
- Luoda sovelluksen, joka käyttää upotuksia datan hakemiseen.

## Miksi rakentaa hakusovellus?

Hakusovelluksen luominen auttaa sinua ymmärtämään, miten upotuksia käytetään datan hakemiseen. Opit myös rakentamaan hakusovelluksen, jota opiskelijat voivat käyttää tiedon löytämiseen nopeasti.

Oppitunnin mukana tulee upotusindeksi Microsoftin [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) YouTube-kanavan transkriptioista. AI Show on YouTube-kanava, joka opettaa tekoälystä ja koneoppimisesta. Upotusindeksi sisältää upotukset kaikista YouTube-transkriptioista lokakuuhun 2023 asti. Käytät upotusindeksiä rakentaaksesi hakusovelluksen startupillemme. Hakusovellus palauttaa linkin kohtaan videossa, jossa kysymykseen annetaan vastaus. Tämä on loistava tapa opiskelijoille löytää tarvitsemansa tieto nopeasti.

Alla on esimerkki semanttisesta kyselystä kysymykselle 'voiko rstudioa käyttää azure ml:n kanssa?'. Katso YouTube-URL, huomaat, että URL sisältää aikaleiman, joka vie sinut kohtaan videossa, jossa kysymykseen annetaan vastaus.

![Semanttinen kysely kysymykselle "voiko rstudioa käyttää Azure ML:n kanssa"](../../../translated_images/query-results.bb0480ebf025fac69c5179ad4d53b6627d643046838c857dc9e2b1281f1cdeb7.fi.png)

## Mitä on semanttinen haku?

Saatat nyt miettiä, mitä semanttinen haku tarkoittaa. Semanttinen haku on hakutekniikka, joka käyttää sanojen merkitystä kyselyssä palauttaakseen relevantteja tuloksia.

Tässä on esimerkki semanttisesta hausta. Oletetaan, että haluat ostaa auton ja haet 'unelma-autoni'. Semanttinen haku ymmärtää, että et `unelmoi` autosta, vaan etsit `ihanteellista` autoa. Semanttinen haku ymmärtää tarkoituksesi ja palauttaa relevantteja tuloksia. Vaihtoehtona on `avainsanahaku`, joka kirjaimellisesti etsisi unelmia autoista ja usein palauttaisi epäolennaisia tuloksia.

## Mitä ovat tekstin upotukset?

[Tekstin upotukset](https://en.wikipedia.org/wiki/Word_embedding?WT.mc_id=academic-105485-koreyst) ovat tekstin esitystekniikka, jota käytetään [luonnollisen kielen käsittelyssä](https://en.wikipedia.org/wiki/Natural_language_processing?WT.mc_id=academic-105485-koreyst). Tekstin upotukset ovat semanttisia numeerisia esityksiä tekstistä. Upotuksia käytetään esittämään dataa tavalla, joka on koneelle helppo ymmärtää. Tekstin upotusten luomiseen on monia malleja, mutta tässä oppitunnissa keskitymme upotusten luomiseen OpenAI:n upotusmallilla.

Tässä on esimerkki: Kuvittele, että seuraava teksti on transkriptio yhdestä AI Show YouTube-kanavan jaksosta:

```text
Today we are going to learn about Azure Machine Learning.
```

Syötämme tekstin OpenAI:n upotus-API:lle, ja se palauttaa seuraavan upotuksen, joka koostuu 1536 numerosta eli vektorista. Jokainen numero vektorissa edustaa eri puolta tekstistä. Lyhyyden vuoksi tässä on vektorin ensimmäiset 10 numeroa.

```python
[-0.006655829958617687, 0.0026128944009542465, 0.008792596869170666, -0.02446001023054123, -0.008540431968867779, 0.022071078419685364, -0.010703742504119873, 0.003311325330287218, -0.011632772162556648, -0.02187200076878071, ...]
```

## Miten upotusindeksi luodaan?

Tämän oppitunnin upotusindeksi luotiin sarjalla Python-skriptejä. Löydät skriptit ja ohjeet [README-tiedostosta](./scripts/README.md?WT.mc_id=academic-105485-koreyst) oppitunnin 'scripts'-kansiosta. Sinun ei tarvitse suorittaa näitä skriptejä tämän oppitunnin suorittamiseksi, sillä upotusindeksi on jo tarjolla.

Skriptit suorittavat seuraavat toiminnot:

1. Jokaisen YouTube-videon transkriptio [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) -soittolistalta ladataan.
2. Käyttämällä [OpenAI-toimintoja](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling?WT.mc_id=academic-105485-koreyst) yritetään tunnistaa puhujan nimi YouTube-transkription ensimmäisten kolmen minuutin aikana. Puhujan nimi tallennetaan upotusindeksiin nimeltä `embedding_index_3m.json`.
3. Transkription teksti jaetaan **kolmen minuutin tekstisegmentteihin**. Segmentti sisältää noin 20 sanaa, jotka menevät päällekkäin seuraavan segmentin kanssa, jotta segmentin upotus ei katkea ja hakukonteksti säilyy paremmin.
4. Jokainen tekstisegmentti syötetään OpenAI:n Chat-API:lle, joka tiivistää tekstin 60 sanaan. Tiivistelmä tallennetaan myös upotusindeksiin `embedding_index_3m.json`.
5. Lopuksi segmenttiteksti syötetään OpenAI:n upotus-API:lle. Upotus-API palauttaa vektorin, joka koostuu 1536 numerosta ja edustaa segmentin semanttista merkitystä. Segmentti ja OpenAI:n upotusvektori tallennetaan upotusindeksiin `embedding_index_3m.json`.

### Vektoripohjaiset tietokannat

Oppitunnin yksinkertaisuuden vuoksi upotusindeksi tallennetaan JSON-tiedostoon nimeltä `embedding_index_3m.json` ja ladataan Pandas DataFrameen. Tuotantokäytössä upotusindeksi tallennettaisiin vektoripohjaiseen tietokantaan, kuten [Azure Cognitive Search](https://learn.microsoft.com/training/modules/improve-search-results-vector-search?WT.mc_id=academic-105485-koreyst), [Redis](https://cookbook.openai.com/examples/vector_databases/redis/readme?WT.mc_id=academic-105485-koreyst), [Pinecone](https://cookbook.openai.com/examples/vector_databases/pinecone/readme?WT.mc_id=academic-105485-koreyst), [Weaviate](https://cookbook.openai.com/examples/vector_databases/weaviate/readme?WT.mc_id=academic-105485-koreyst), vain muutamia mainitakseni.

## Kosinisimilaarisuuden ymmärtäminen

Olemme oppineet tekstin upotuksista, ja seuraava askel on oppia käyttämään tekstin upotuksia datan hakemiseen, erityisesti löytämään kyselyä lähimpänä olevat upotukset kosinisimilaarisuuden avulla.

### Mitä on kosinisimilaarisuus?

Kosinisimilaarisuus on kahden vektorin välinen samankaltaisuuden mitta, jota kutsutaan myös `lähimmän naapurin hauksi`. Kosinisimilaarisuushakua varten sinun täytyy _vektorisoida_ kyselyteksti OpenAI:n upotus-API:lla. Sitten lasketaan _kosinisimilaarisuus_ kyselyvektorin ja upotusindeksin jokaisen vektorin välillä. Muista, että upotusindeksissä on vektori jokaiselle YouTube-transkription tekstisegmentille. Lopuksi tulokset järjestetään kosinisimilaarisuuden mukaan, ja tekstisegmentit, joilla on korkein kosinisimilaarisuus, ovat kyselyä lähimpänä.

Matemaattisesta näkökulmasta kosinisimilaarisuus mittaa kahden vektorin välisen kulman kosinia monidimensioisessa tilassa. Tämä mittaus on hyödyllinen, koska jos kaksi dokumenttia ovat kaukana toisistaan euklidisella etäisyydellä koon vuoksi, niillä voi silti olla pienempi kulma niiden välillä ja siten korkeampi kosinisimilaarisuus. Lisätietoja kosinisimilaarisuusyhtälöistä löydät [Kosinisimilaarisuus](https://en.wikipedia.org/wiki/Cosine_similarity?WT.mc_id=academic-105485-koreyst).

## Ensimmäisen hakusovelluksen rakentaminen

Seuraavaksi opimme rakentamaan hakusovelluksen käyttämällä upotuksia. Hakusovellus mahdollistaa opiskelijoiden videoiden etsimisen kirjoittamalla kysymyksen. Hakusovellus palauttaa listan videoista, jotka liittyvät kysymykseen. Hakusovellus palauttaa myös linkin kohtaan videossa, jossa kysymykseen annetaan vastaus.

Tämä ratkaisu on rakennettu ja testattu Windows 11:llä, macOS:llä ja Ubuntu 22.04:llä käyttäen Python 3.10:ä tai uudempaa. Voit ladata Pythonin [python.org](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

## Tehtävä - hakusovelluksen rakentaminen opiskelijoiden avuksi

Esittelimme startupimme tämän oppitunnin alussa. Nyt on aika mahdollistaa opiskelijoiden hakusovelluksen rakentaminen heidän arviointejaan varten.

Tässä tehtävässä luot Azure OpenAI -palvelut, joita käytetään hakusovelluksen rakentamiseen. Luot seuraavat Azure OpenAI -palvelut. Tarvitset Azure-tilauksen tämän tehtävän suorittamiseen.

### Käynnistä Azure Cloud Shell

1. Kirjaudu [Azure-portaaliin](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst).
2. Valitse Azure-portaalin oikeasta yläkulmasta Cloud Shell -kuvake.
3. Valitse ympäristötyypiksi **Bash**.

#### Luo resurssiryhmä

> Näissä ohjeissa käytämme resurssiryhmää nimeltä "semantic-video-search" East US -alueella.
> Voit muuttaa resurssiryhmän nimeä, mutta kun muutat resurssien sijaintia,
> tarkista [mallien saatavuustaulukko](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```shell
az group create --name semantic-video-search --location eastus
```

#### Luo Azure OpenAI -palveluresurssi

Suorita seuraava komento Azure Cloud Shellissä luodaksesi Azure OpenAI -palveluresurssin.

```shell
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

#### Hae päätepiste ja avaimet tämän sovelluksen käyttöä varten

Suorita seuraavat komennot Azure Cloud Shellissä hakeaksesi päätepisteen ja avaimet Azure OpenAI -palveluresurssille.

```shell
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

#### Ota käyttöön OpenAI:n upotusmalli

Suorita seuraava komento Azure Cloud Shellissä ottaaksesi käyttöön OpenAI:n upotusmallin.

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

## Ratkaisu

Avaa [ratkaisun Jupyter Notebook](./python/aoai-solution.ipynb?WT.mc_id=academic-105485-koreyst) GitHub Codespacesissa ja seuraa ohjeita Jupyter Notebookissa.

Kun suoritat Notebookin, sinua pyydetään syöttämään kysely. Syöttökenttä näyttää tältä:

![Syöttökenttä käyttäjälle kyselyn syöttämistä varten](../../../translated_images/notebook-search.1e320b9c7fcbb0bc1436d98ea6ee73b4b54ca47990a1c952b340a2cadf8ac1ca.fi.png)

## Hienoa työtä! Jatka oppimista

Kun olet suorittanut tämän oppitunnin, tutustu [Generatiivisen tekoälyn oppimiskokoelmaamme](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi generatiivisen tekoälyn osaamisesi kehittämistä!

Siirry oppituntiin 9, jossa tarkastelemme, miten [rakentaa kuvien generointisovelluksia](../09-building-image-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi katsoa ensisijaiseksi lähteeksi. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.