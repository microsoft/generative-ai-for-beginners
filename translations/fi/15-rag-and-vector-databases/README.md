<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2210a0466c812d9defc4df2d9a709ff9",
  "translation_date": "2026-01-18T18:26:12+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "fi"
}
-->
# Hakuavusteinen generointi (Retrieval Augmented Generation, RAG) ja vektoritietokannat

[![Hakuavusteinen generointi (RAG) ja vektoritietokannat](../../../../../translated_images/fi/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Hakusovellusten oppitunnissa opimme lyhyesti, miten omat tietosi voidaan integroida suuriin kielimalleihin (LLM). Tässä oppitunnissa syvennymme lisää siihen, miten data voidaan perustaa LLM-sovelluksessasi, prosessin mekanismeihin ja tapoihin tallentaa tietoa, mukaan lukien sisääntulot ja teksti.

> **Video tulossa pian**

## Johdanto

Tässä oppitunnissa käsittelemme seuraavaa:

- Johdanto RAGiin, mitä se on ja miksi sitä käytetään tekoälyssä (AI).

- Ymmärrys siitä, mitä vektoritietokannat ovat, ja kuinka luoda sellainen sovellustamme varten.

- Käytännön esimerkki siitä, miten RAG integroidaan sovellukseen.

## Oppimistavoitteet

Oppitunnin suorittamisen jälkeen osaat:

- Selittää RAGin merkityksen tiedon haussa ja käsittelyssä.

- Määrittää RAG-sovelluksen ja perustaa datasi LLM:ään.

- Tehokkaasti integroida RAG ja vektoritietokannat LLM-sovelluksiin.

## Tilanteemme: LLM-mallimme rikastaminen omalla datallamme

Tässä oppitunnissa haluamme lisätä omat muistiinpanomme koulutusteknologiayritykseen, jonka avulla chatbot voi saada lisää tietoa eri aiheista. Käyttäen näitä muistiinpanoja oppijat pystyvät opiskelemaan paremmin ja ymmärtämään eri aiheita, mikä helpottaa valmistautumista kokeisiin. Luodaksemme tämän tilanteen käytämme:

- `Azure OpenAI:` LLM, jota käytämme chatbotin luomiseen

- `AI for beginners' lesson on Neural Networks`: tämä toimii datana, johon perustamme LLM:n

- `Azure AI Search` ja `Azure Cosmos DB:` vektoritietokanta datan tallentamiseen ja hakuhakemiston luomiseen

Käyttäjät voivat luoda harjoituskyselyjä muistiinpanoistaan, kertaustikkukortteja ja tiivistää sisältöä ytimekkäiksi yhteenvetoiksi. Aloitetaan katsomalla, mitä RAG on ja miten se toimii:

## Hakuavusteinen generointi (RAG)

LLM-pohjainen chatbot käsittelee käyttäjän kehotteita luodakseen vastauksia. Se on suunniteltu olemaan vuorovaikutteinen ja käsittelemään erilaisia aiheita. Sen vastaukset rajoittuvat kuitenkin annettuun kontekstiin ja sen perustietoihin. Esimerkiksi GPT-4:llä tiedon katkaisu on syyskuussa 2021, joten se ei tunne tämän jälkeen tapahtuneita asioita. Lisäksi LLM:n koulutuksessa käytetty data ei sisällä luottamuksellista tietoa, kuten henkilökohtaisia muistiinpanoja tai yrityksen käyttöohjeita.

### Miten RAG toimii

![kuvaus RAGin toiminnasta](../../../../../translated_images/fi/how-rag-works.f5d0ff63942bd3a6.webp)

Oletetaan, että haluat ottaa käyttöön chatbotin, joka luo kyselyitä muistiinpanoistasi. Tarvitset tällöin yhteyden tietopohjaan. Tässä vaiheessa RAG astuu kuvaan. RAG toimii seuraavasti:

- **Tietopohja:** Ennen hakua dokumentit on syötettävä ja esikäsiteltävä, yleensä suurten dokumenttien pilkkominen pienemmiksi osasiksi, muuttaminen tekstipohjaisiksi upotuksiksi (embedding) ja tallentaminen tietokantaan.

- **Käyttäjän kysymys:** käyttäjä esittää kysymyksen

- **Haku:** Kun käyttäjä kysyy, upotusmalli hakee tietopohjastamme relevanttia tietoa, jolla rikastetaan pyyntöä.

- **Rikastettu generointi:** LLM parantaa vastaustaan haetun tiedon perusteella. Näin vastaus ei perustu pelkästään ennakkoon koulutettuun dataan, vaan myös lisättyyn relevanttiin kontekstiin. Hae data käytetään LLM:n vastausten rikastamiseen. LLM palauttaa vastauksen käyttäjän kysymykseen.

![kuvaus RAG-arkkitehtuurista](../../../../../translated_images/fi/encoder-decode.f2658c25d0eadee2.webp)

RAG-arkkitehtuuri toteutetaan transformer-tekniikalla, joka koostuu kahdesta osasta: kooderista ja purkajasta. Esimerkiksi kun käyttäjä kysyy, syötettävä teksti koodataan vektoreiksi, jotka edustavat sanojen merkitystä, ja vektorit dekoodataan dokumenttihakemistoon ja generoidaan uutta tekstiä käyttäjän kysymyksen pohjalta. LLM käyttää sekä kooderin että purkajan mallia vasteen luomiseen.

Kaksi lähestymistapaa RAGin toteutukseen ehdotetun tutkielman [Retrieval-Augmented Generation for Knowledge intensive NLP Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) mukaan ovat:

- **_RAG-Sequence_**, jossa haetuilla dokumenteilla ennustetaan paras mahdollinen vastaus käyttäjän kyselyyn

- **RAG-Token**, jossa dokumentteja käytetään seuraavan tokenin generointiin, minkä jälkeen haetaan lisätietoja vastauksen muodostamiseksi

### Miksi käyttää RAG:ia?

- **Tiedon rikkaus:** varmistaa, että tekstivastaukset ovat ajantasaisia ja relevantteja. Parantaa siten suorituskykyä toimialakohtaisissa tehtävissä pääsemällä käsiksi sisäiseen tietopohjaan.

- Vähentää virheellisiä tietoja hyödyntämällä **tarkistettavissa olevaa dataa** tietopohjassa käyttäjän kysymyksen kontekstina.

- On **kustannustehokas**, koska se on edullisempaa verrattuna LLM:n hienosäätöön.

## Tutustumme tietopohjan luomiseen

Sovelluksemme perustuu henkilökohtaiseen dataamme eli AI For Beginners -koulutuksen Neuroverkot-oppituntiin.

### Vektoritietokannat

Vektoritietokanta on perinteisestä tietokannasta poiketen erikoistunut tietokanta, joka on suunniteltu tallentamaan, hallinnoimaan ja hakemaan upotettuja vektoreita. Se säilyttää dokumenttien numeeriset esitykset. Datan muuntaminen numeerisiksi upotuksiksi helpottaa tekoälyjärjestelmän tiedon ymmärtämistä ja käsittelyä.

Tallennamme upotuksemme vektoritietokantoihin, koska LLM:illä on rajoitus sille, kuinka monta tokenia se voi vastaanottaa syötteenä. Koska koko upotusta ei voi syöttää kerralla, pilkomme ne osiin ja kun käyttäjä kysyy, ne upotukset, jotka parhaiten vastaavat kysymystä, palautetaan yhdessä kehotteen kanssa. Pilkkominen myös vähentää kustannuksia tokenien määrän suhteen LLM:lle.

Tunnettuja vektoritietokantoja ovat esimerkiksi Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant ja DeepLake. Voit luoda Azure Cosmos DB -mallin Azure CLI:llä seuraavalla komennolla:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Tekstistä upotuksiin

Ennen datan tallentamista meidän tulee muuntaa se vektoriedustuksiin. Jos käsittelet suuria dokumentteja tai pitkiä tekstejä, voit pilkkoa ne kysymysten odotettavissa olevien aiheiden mukaan. Pilkkominen voidaan tehdä lause- tai kappaletasolla. Koska pilkkominen hyödyntää sanojen ympäristöä, voit lisätä pilkkoon myös muuta kontekstia, esimerkiksi dokumentin otsikon tai tekstiä ennen tai jälkeen pilkon. Voit pilkkoa tiedon esimerkiksi näin:

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

    # Jos viimeinen osa ei saavuttanut vähimmäispituutta, lisää se kuitenkin
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Kun data on pilkottu, voimme upottaa sen käyttäen erilaisia upotusmalleja. Joitakin käytettävissä olevia malleja ovat mm. word2vec, OpenAI:n ada-002, Azure Computer Vision ja monet muut. Mallin valinta riippuu kielestä, sisällön tyypistä (teksti/kuva/ääni), koosta ja upotuksen pituudesta.

Esimerkki OpenAI:n `text-embedding-ada-002`-mallilla upotetusta tekstistä on:
![sanasta cat upotuskuva](../../../../../translated_images/fi/cat.74cbd7946bc9ca38.webp)

## Haku ja vektorihaut

Kun käyttäjä esittää kysymyksen, hakualgoritmi muuntaa sen vektoriksi käyttäen kyselyn kooderia, jonka jälkeen se etsii dokumenttihakemistostamme relevantit vektorit, jotka liittyvät syötteeseen. Sen jälkeen sekä syötevektori että dokumenttivektorit muutetaan tekstiksi ja syötetään LLM:lle.

### Haku

Haku tapahtuu, kun järjestelmä yrittää nopeasti löytää hakukriteerit täyttäviä dokumentteja hakemistosta. Haun tavoitteena on saada dokumentteja, joita käytetään kontekstin tarjoamiseen ja LLM:n perustamiseen sinun dataasi vasten.

Tietokantahakuja voidaan tehdä monella tavalla, kuten:

- **Avainsanahaku** – käytetään tekstihauissa

- **Vektorihaku** – muuntaa dokumentit tekstistä vektoriesityksiksi upotusmallien avulla, mahdollistaen **semanttisen haun**, joka hakee sanojen merkityksen perusteella. Haku tapahtuu löytämällä dokumenttien vektoriesitykset, jotka ovat lähimpänä käyttäjän kysymystä.

- **Hybridihaku** – yhdistelmä avainsana- ja vektorihakua.

Haaste hakemisessa syntyy, jos tietokannasta ei löydy samankaltaista vastausta kyselyyn. Järjestelmä palauttaa silloin parhaan mahdollisen tiedon, mutta voit käyttää keinoja, kuten asettaa maksimietäisyys merkitykselle tai tehdä hybridihaku, joka yhdistää avainsana- ja vektorihakutoiminnot. Tässä oppitunnissa käytämme hybridihakua, joka on sekä vektori- että avainsanahaku. Tallennamme datamme tietokehykseen, jossa sarakkeissa on sekä pilkotut osat että upotukset.

### Vektorilähesyyys

Hakualgoritmi etsii tietokannasta upotuksia, jotka ovat lähellä toisiaan, eli lähimmät naapurit, koska ne ovat samankaltaisia tekstejä. Kun käyttäjä tekee kyselyn, se upotetaan ja verrataan samankaltaisiin upotuksiin. Yleisin tapa mitata kahden vektorin samankaltaisuutta on kosinilähesyyteen perustuva mittaus, joka mittaa kulmaa vektorien välillä.

Voimme mitata samankaltaisuutta myös muilla tavoilla, kuten euklidisella etäisyydellä, joka mittaa suorimman suoran pisteiden välillä, tai pistetulolla, joka mittaa kahden vektorin vastaavien alkioiden tulosten summan.

### Hakemisto

Hakua varten meidän tulee rakentaa hakemisto tietopohjalle ennen haun tekemistä. Hakemisto tallentaa upotuksemme ja pystyy nopeasti hakemaan lähimmät osat suuristakin tietokannoista. Voimme luoda hakemistomme paikallisesti näin:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Luo hakemisto
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Indeksin kyselyyn voit käyttää kneighbors-metodia
distances, indices = nbrs.kneighbors(embeddings)
```

### Uudelleenjärjestäminen

Kun olet kysellyt tietokantaa, saatat haluta järjestää tulokset merkityksellisyyden mukaan. Uudelleenjärjestelyssä LLM hyödyntää koneoppimista hakutulosten relevanttiuden parantamiseksi ja järjestää ne arvokkaimmasta eteenpäin. Azure AI Search käyttää automaattista semanttista uudelleenjärjestäjää. Esimerkki uudelleenjärjestelyn toiminnasta käyttäen lähimpiä naapureita:

```python
# Etsi samankaltaisimmat asiakirjat
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Tulosta samankaltaisimmat asiakirjat
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

Viimeinen vaihe on liittää LLM mukaan, jotta saamme vastaukset, jotka perustuvat dataamme. Voimme toteuttaa sen näin:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Muunna kysymys kyselyvektoriksi
    query_vector = create_embeddings(user_input)

    # Etsi samankaltaisimmat asiakirjat
    distances, indices = nbrs.kneighbors([query_vector])

    # lisää asiakirjat kyselyyn kontekstin tarjoamiseksi
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # yhdistä historia ja käyttäjän syöte
    history.append(user_input)

    # luo viestiobjekti
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # käytä keskustelun täydentämistä vastauksen luomiseen
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

### Arviointimittarit

- Vastauksien laatu: varmista, että ne kuulostavat luonnollisilta, sujuvilta ja ihmismäisiltä.

- Datan perusteltavuus: arvioi, onko vastaus peräisin toimitetuista dokumenteista.

- Relevanssi: arvioi, vastaako vastaus esitettyyn kysymykseen ja liittyykö siihen.

- Sujuvuus: tarkastellaan, onko vastaus kieliopillisesti järkevä.

## Käyttötapauksia RAGin ja vektoritietokantojen hyödyntämiseen

Funktiokutsut voivat parantaa sovellustasi monissa eri tilanteissa, kuten:

- Kysymys-vastaus -palvelu: perusta yrityksesi data keskusteluun, johon työntekijät voivat esittää kysymyksiä.

- Suositusjärjestelmät: voit luoda järjestelmän, joka löytää samankaltaisimmat arvot, esimerkiksi elokuvat, ravintolat ja paljon muuta.

- Chatbot-palvelut: voit tallentaa keskusteluhistorian ja personoida keskustelua käyttäjätietoon perustuen.

- Kuvahaku vektoripohjaisten upotusten avulla, hyödyllinen kuvatunnistuksessa ja poikkeamien havaitsemisessa.

## Yhteenveto

Olemme käyneet läpi RAGin perusalueet, oman datan lisäämisestä sovellukseen, käyttäjän kyselyn käsittelyyn ja vastauksen muodostamiseen. RAGin luomisen helpottamiseksi voi käyttää kehyksiä, kuten Semantic Kernel, Langchain tai Autogen.

## Tehtävä

Jatka hakuvahvistetun generoinnin (RAG) opiskelua rakentamalla:

- Luo sovellukselle käyttöliittymä haluamallasi kehitysympäristöllä.

- Hyödynnä kehystä, joko LangChain tai Semantic Kernel, ja tee sovelluksesi uudelleen.

Onnittelut oppitunnin suorittamisesta 👏.

## Oppiminen ei lopu tähän, jatka matkaasi

Oppitunnin jälkeen tutustu [Generatiivisen tekoälyn oppimiskokoelmaamme](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi generatiivisen tekoälyn osaamisesi kehittämistä!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä on virallinen lähde. Tärkeitä tietoja varten suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->