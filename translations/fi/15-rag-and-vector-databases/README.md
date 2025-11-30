<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4b0266fbadbba7ded891b6485adc66d",
  "translation_date": "2025-10-17T19:42:08+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "fi"
}
-->
# Tiedonhakuun perustuva generointi (RAG) ja vektoripohjaiset tietokannat

[![Tiedonhakuun perustuva generointi (RAG) ja vektoripohjaiset tietokannat](../../../translated_images/15-lesson-banner.ac49e59506175d4fc6ce521561dab2f9ccc6187410236376cfaed13cde371b90.fi.png)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Hakusovelluksia käsittelevässä oppitunnissa opimme lyhyesti, kuinka omia tietoja voidaan integroida suurten kielimallien (LLM) kanssa. Tässä oppitunnissa syvennymme tarkemmin siihen, miten voit ankkuroida omat tietosi LLM-sovellukseen, prosessin toimintaan ja menetelmiin tietojen tallentamiseksi, mukaan lukien upotukset ja teksti.

> **Video tulossa pian**

## Johdanto

Tässä oppitunnissa käsitellään seuraavia aiheita:

- Johdatus RAG:iin, mitä se on ja miksi sitä käytetään tekoälyssä.

- Ymmärrys vektoripohjaisista tietokannoista ja niiden luominen sovellustamme varten.

- Käytännön esimerkki siitä, miten RAG integroidaan sovellukseen.

## Oppimistavoitteet

Tämän oppitunnin jälkeen osaat:

- Selittää RAG:n merkityksen tiedon haussa ja käsittelyssä.

- Määrittää RAG-sovelluksen ja ankkuroida omat tietosi LLM:ään.

- Tehokkaasti integroida RAG ja vektoripohjaiset tietokannat LLM-sovelluksiin.

## Meidän skenaario: LLM:n parantaminen omilla tiedoillamme

Tässä oppitunnissa haluamme lisätä omat muistiinpanomme koulutusalustaan, mikä mahdollistaa chatbotin tarjoavan enemmän tietoa eri aiheista. Käyttämällä muistiinpanojamme oppijat voivat opiskella paremmin ja ymmärtää eri aiheita, mikä helpottaa kokeisiin valmistautumista. Skenaarion luomiseksi käytämme:

- `Azure OpenAI:` LLM, jota käytämme chatbotin luomiseen.

- `AI for beginners -oppitunti neuroverkoista`: data, johon ankkuroidaan LLM.

- `Azure AI Search` ja `Azure Cosmos DB:` vektoripohjainen tietokanta tietojen tallentamiseen ja hakemistoindeksin luomiseen.

Käyttäjät voivat luoda harjoituskokeita muistiinpanoistaan, kertauskortteja ja tiivistää ne ytimekkäiksi yhteenvedoiksi. Aloitetaan katsomalla, mitä RAG on ja miten se toimii:

## Tiedonhakuun perustuva generointi (RAG)

LLM-pohjainen chatbot käsittelee käyttäjän antamia kyselyitä ja tuottaa vastauksia. Se on suunniteltu vuorovaikutteiseksi ja keskustelee käyttäjien kanssa monista eri aiheista. Sen vastaukset ovat kuitenkin rajallisia sen tarjoaman kontekstin ja perustavanlaatuisen koulutusdatan osalta. Esimerkiksi GPT-4:n tietopohja kattaa tiedot syyskuuhun 2021 asti, mikä tarkoittaa, että se ei tunne tapahtumia tämän ajankohdan jälkeen. Lisäksi LLM:ien koulutuksessa käytetty data ei sisällä luottamuksellisia tietoja, kuten henkilökohtaisia muistiinpanoja tai yrityksen tuotemanuaalia.

### Miten RAG (tiedonhakuun perustuva generointi) toimii

![kuva, joka näyttää miten RAG toimii](../../../translated_images/how-rag-works.f5d0ff63942bd3a638e7efee7a6fce7f0787f6d7a1fca4e43f2a7a4d03cde3e0.fi.png)

Oletetaan, että haluat ottaa käyttöön chatbotin, joka luo kyselyitä muistiinpanoistasi. Tarvitset yhteyden tietopohjaan. Tässä RAG tulee apuun. RAG toimii seuraavasti:

- **Tietopohja:** Ennen hakua dokumentit täytyy syöttää ja esikäsitellä, yleensä jakamalla suuret dokumentit pienempiin osiin, muuntamalla ne tekstin upotuksiksi ja tallentamalla ne tietokantaan.

- **Käyttäjän kysely:** Käyttäjä esittää kysymyksen.

- **Haku:** Kun käyttäjä esittää kysymyksen, upotusmalli hakee asiaankuuluvat tiedot tietopohjasta tarjotakseen enemmän kontekstia, joka sisällytetään kyselyyn.

- **Generointi:** LLM parantaa vastaustaan haettujen tietojen perusteella. Tämä mahdollistaa sen, että vastaus perustuu paitsi ennalta koulutettuun dataan myös lisättyyn kontekstiin. Haettu data käytetään LLM:n vastausten parantamiseen. LLM palauttaa sitten vastauksen käyttäjän kysymykseen.

![kuva, joka näyttää RAG:n arkkitehtuurin](../../../translated_images/encoder-decode.f2658c25d0eadee2377bb28cf3aee8b67aa9249bf64d3d57bb9be077c4bc4e1a.fi.png)

RAG:n arkkitehtuuri toteutetaan transformereilla, jotka koostuvat kahdesta osasta: kooderista ja dekooderista. Esimerkiksi, kun käyttäjä esittää kysymyksen, syötetty teksti "koodataan" vektoreiksi, jotka sisältävät sanojen merkityksen, ja vektorit "dekoodataan" dokumentti-indeksiimme ja luodaan uutta tekstiä käyttäjän kyselyn perusteella. LLM käyttää sekä kooderi-dekooderi-mallia tuottaakseen vastauksen.

Kaksi lähestymistapaa RAG:n toteuttamiseen ehdotetun artikkelin mukaan: [Retrieval-Augmented Generation for Knowledge intensive NLP (luonnollisen kielen käsittelyohjelmisto) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) ovat:

- **_RAG-Sequence_** käyttää haettuja dokumentteja ennustaakseen parhaan mahdollisen vastauksen käyttäjän kyselyyn.

- **RAG-Token** käyttää dokumentteja seuraavan tokenin tuottamiseen ja hakee sitten vastauksen käyttäjän kyselyyn.

### Miksi käyttää RAG:ia?

- **Tietojen rikkaus:** varmistaa, että tekstivastaukset ovat ajan tasalla ja ajankohtaisia. Se parantaa suorituskykyä alakohtaisissa tehtävissä pääsemällä käsiksi sisäiseen tietopohjaan.

- Vähentää virheellistä tietoa käyttämällä **todennettavissa olevaa dataa** tietopohjasta tarjotakseen kontekstia käyttäjän kyselyihin.

- Se on **kustannustehokas**, koska se on taloudellisempi verrattuna LLM:n hienosäätöön.

## Tietopohjan luominen

Sovelluksemme perustuu henkilökohtaisiin tietoihimme, eli AI For Beginners -opetussuunnitelman neuroverkko-oppituntiin.

### Vektoripohjaiset tietokannat

Vektoripohjainen tietokanta, toisin kuin perinteiset tietokannat, on erikoistunut tietokanta, joka on suunniteltu tallentamaan, hallitsemaan ja hakemaan upotettuja vektoreita. Se tallentaa dokumenttien numeeriset esitykset. Datan pilkkominen numeerisiin upotuksiin helpottaa AI-järjestelmän kykyä ymmärtää ja käsitellä dataa.

Tallennamme upotuksemme vektoripohjaisiin tietokantoihin, koska LLM:illä on rajoitus syötteenä hyväksyttyjen tokenien määrässä. Koska et voi välittää kaikkia upotuksia LLM:lle, meidän täytyy pilkkoa ne osiin, ja kun käyttäjä esittää kysymyksen, upotukset, jotka ovat lähimpänä kysymystä, palautetaan yhdessä kyselyn kanssa. Pilkkominen myös vähentää kustannuksia LLM:lle välitettyjen tokenien määrässä.

Joistakin suosituista vektoripohjaisista tietokannoista mainittakoon Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant ja DeepLake. Voit luoda Azure Cosmos DB -mallin käyttämällä Azure CLI:tä seuraavalla komennolla:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Tekstistä upotuksiin

Ennen kuin tallennamme datamme, meidän täytyy muuntaa se vektoripohjaisiksi upotuksiksi ennen sen tallentamista tietokantaan. Jos työskentelet suurten dokumenttien tai pitkien tekstien kanssa, voit pilkkoa ne odotettujen kyselyiden perusteella. Pilkkominen voidaan tehdä lause- tai kappaletasolla. Koska pilkkominen johdetaan sanojen ympärillä olevista merkityksistä, voit lisätä jonkin muun kontekstin pilkottuun osaan, esimerkiksi lisäämällä dokumentin otsikon tai sisällyttämällä tekstiä ennen tai jälkeen pilkotun osan. Voit pilkkoa datan seuraavasti:

```python
def split_text(text, max_length, min_length):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if len(' '.join(current_chunk)) < max_length and len(' '.join(current_chunk)) > min_length:
            chunks.append(' '.join(current_chunk))
            current_chunk = []

    # If the last chunk didn't reach the minimum length, add it anyway
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Kun data on pilkottu, voimme sitten upottaa tekstimme eri upotusmalleilla. Joitakin malleja, joita voit käyttää, ovat: word2vec, ada-002 OpenAI:lta, Azure Computer Vision ja monet muut. Mallin valinta riippuu käyttämistäsi kielistä, koodattavan sisällön tyypistä (teksti/kuvat/ääni), syötteen koosta, jonka se voi koodata, ja upotuksen pituudesta.

Esimerkki upotetusta tekstistä OpenAI:n `text-embedding-ada-002` -mallilla:
![kissan upotus](../../../translated_images/cat.74cbd7946bc9ca380a8894c4de0c706a4f85b16296ffabbf52d6175df6bf841e.fi.png)

## Tiedonhaku ja vektorihaku

Kun käyttäjä esittää kysymyksen, hakija muuntaa sen vektoriksi käyttämällä kyselykooderia, ja etsii sitten dokumentti-indeksistämme asiaankuuluvia vektoreita, jotka liittyvät syötteeseen. Kun haku on tehty, se muuntaa sekä syötevektorin että dokumenttivektorit tekstiksi ja välittää ne LLM:lle.

### Tiedonhaku

Tiedonhaku tapahtuu, kun järjestelmä yrittää nopeasti löytää dokumentit indeksistä, jotka täyttävät hakukriteerit. Hakijan tavoitteena on saada dokumentteja, joita käytetään tarjoamaan konteksti ja ankkuroimaan LLM omiin tietoihisi.

Tietokannassamme voidaan suorittaa hakuja useilla tavoilla, kuten:

- **Avainsanahaku** - käytetään tekstihakuun.

- **Semanttinen haku** - käyttää sanojen semanttista merkitystä.

- **Vektorihaku** - muuntaa dokumentit tekstistä vektoriesityksiksi upotusmallien avulla. Haku tehdään kysymällä dokumentteja, joiden vektoriesitykset ovat lähimpänä käyttäjän kysymystä.

- **Hybridi** - yhdistelmä avainsana- ja vektorihakua.

Haun haasteena on, kun tietokannassa ei ole samanlaista vastausta kyselyyn, järjestelmä palauttaa parhaan mahdollisen tiedon, jonka se voi löytää. Voit kuitenkin käyttää taktiikoita, kuten asettaa maksimietäisyyden relevanssille tai käyttää hybridihakua, joka yhdistää sekä avainsana- että vektorihakua. Tässä oppitunnissa käytämme hybridihakua, joka yhdistää sekä vektori- että avainsanahaun. Tallennamme datamme datafreimiin, jossa sarakkeet sisältävät pilkotut osat sekä upotukset.

### Vektorien samankaltaisuus

Hakija etsii tietopohjasta upotuksia, jotka ovat lähellä toisiaan, lähimmät naapurit, koska ne ovat tekstejä, jotka ovat samankaltaisia. Skenaariossa, jossa käyttäjä esittää kyselyn, se ensin upotetaan ja sitten yhdistetään samankaltaisiin upotuksiin. Yleinen mitta, jota käytetään arvioimaan, kuinka samankaltaisia eri vektorit ovat, on kosinimainen samankaltaisuus, joka perustuu kahden vektorin väliseen kulmaan.

Voimme mitata samankaltaisuutta myös muilla vaihtoehdoilla, kuten euklidisella etäisyydellä, joka on suora viiva vektorien päätepisteiden välillä, ja pistetulolla, joka mittaa kahden vektorin vastaavien elementtien tuotteiden summan.

### Hakemisto

Kun teemme tiedonhakua, meidän täytyy rakentaa hakemisto tietopohjallemme ennen hakua. Hakemisto tallentaa upotuksemme ja voi nopeasti hakea samankaltaisimmat osat jopa suuresta tietokannasta. Voimme luoda hakemiston paikallisesti käyttämällä:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Uudelleenjärjestely

Kun olet tehnyt kyselyn tietokantaan, saatat tarvita tulosten lajittelua relevanssin mukaan. Uudelleenjärjestely LLM hyödyntää koneoppimista parantaakseen hakutulosten relevanssia järjestämällä ne tärkeimmistä alkaen. Azure AI Search -palvelussa uudelleenjärjestely tehdään automaattisesti semanttisen uudelleenjärjestelijän avulla. Esimerkki siitä, miten uudelleenjärjestely toimii lähimpien naapureiden avulla:

```python
# Find the most similar documents
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Print the most similar documents
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Kaiken yhdistäminen

Viimeinen vaihe on lisätä LLM mukaan, jotta voimme saada vastauksia, jotka perustuvat omiin tietoihimme. Voimme toteuttaa sen seuraavasti:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Convert the question to a query vector
    query_vector = create_embeddings(user_input)

    # Find the most similar documents
    distances, indices = nbrs.kneighbors([query_vector])

    # add documents to query  to provide context
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # combine the history and the user input
    history.append(user_input)

    # create a message object
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": history[-1]}
    ]

    # use chat completion to generate a response
    response = openai.chat.completions.create(
        model="gpt-4",
        temperature=0.7,
        max_tokens=800,
        messages=messages
    )

    return response.choices[0].message

chatbot(user_input)
```

## Sovelluksen arviointi

### Arviointikriteerit

- Vastauksien laatu: varmistetaan, että ne kuulostavat luonnollisilta, sujuvilta ja ihmismäisiltä.

- Tietojen ankkurointi: arvioidaan, tuliko vastaus toimitetuista dokumenteista.

- Relevanssi: arvioidaan, vastaako vastaus kysymystä ja liittyykö se siihen.

- Sujuvuus: arvioidaan, onko vastaus kieliopillisesti järkevä.

## Käyttötapaukset RAG:lle ja vektoripohjaisille tietokannoille

RAG:n ja vektoripohjaisten tietokantojen käyttö voi parantaa sovellustasi monin tavoin, kuten:

- Kysymys-vastaus: yrityksesi datan ankkurointi chattiin, jota työntekijät voivat käyttää kysymysten esittämiseen.

- Suositusjärjestelmät: järjestelmä, joka yhdistää samankaltaisimmat arvot, kuten elokuvat, ravintolat ja paljon muuta.

- Chatbot-palvelut: voit tallentaa chat-historian ja personoida keskustelun käyttäjän datan perusteella.

- Kuvahaku vektoripohjaisten upotusten avulla, hyödyllinen kuvantunnistuksessa ja poikkeavuuksien havaitsemisessa.

## Yhteenveto

Olemme käsitelleet RAG:n perusalueet datan lisäämisestä sovellukseen, käyttäjän kyselystä ja vastauksesta. RAG:n luomisen yksinkertaistamiseksi voit käyttää kehyksiä, kuten Semantic Kernel, Langchain tai Autogen.

## Tehtävä

Jatka oppimista tiedonhakuun perustuvasta generoinnista (RAG) rakentamalla:

- Sovellukselle käyttöliittymä valitsemallasi kehysratkaisulla.

- Hyödynnä kehystä, kuten LangChain tai Semantic Kernel, ja luo sovelluksesi uudelleen.

Onnittelut oppitunnin suorittamisesta 👏.

## Oppiminen ei lopu tähän, jatka matkaasi

Oppitunnin jälkeen tutustu [Generative AI Learning -kokoelmaan](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi Generatiivisen AI:n osaamisen kehittämistä!

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi katsoa ensisijaiseksi lähteeksi. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.