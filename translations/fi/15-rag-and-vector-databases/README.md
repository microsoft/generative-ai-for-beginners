# Hakua täydentävä generointi (RAG) ja vektoritietokannat

[![Hakua täydentävä generointi (RAG) ja vektoritietokannat](../../../translated_images/fi/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Hakusovellusten oppitunnissa opimme lyhyesti, miten omia tietoja voi integroida suurten kielimallien (LLM) käyttöön. Tässä oppitunnissa sukelletaan syvemmälle tietojesi jalkauttamiseen LLM-sovelluksessasi, prosessin mekanismeihin sekä menetelmiin tiedon tallentamiseksi, mukaan lukien upotukset ja teksti.

> **Video pian tulossa**

## Johdanto

Tässä oppitunnissa käsittelemme seuraavia aiheita:

- Johdanto RAGiin, mitä se on ja miksi sitä käytetään tekoälyssä (AI).

- Mikä on vektoritietokanta ja miten sellainen luodaan sovellukseemme.

- Käytännön esimerkki RAGin integroimisesta sovellukseen.

## Oppimistavoitteet

Tässä oppitunnissa opit:

- Selittämään RAGin merkityksen tiedonhankinnassa ja käsittelyssä.

- Miten RAG-sovellus asennetaan ja kuinka tieto jalkautetaan LLMiin.

- Miten RAG ja vektoritietokannat integroidaan tehokkaasti LLM-sovelluksiin.

## Tilanteemme: omien tietojen lisääminen LLM:iin

Tässä oppitunnissa haluamme lisätä omat muistiinpanomme koulutusstartuppiin, jotta chatbot saa enemmän tietoa eri aiheista. Muistiinpanojen avulla oppijat voivat opiskella paremmin ja ymmärtää eri aihepiirejä, mikä helpottaa kokeisiin valmistautumista. Tilanteen luomiseksi käytämme seuraavia komponentteja:

- `Azure OpenAI:` LLM, jota käytämme chatbotin luomiseen

- `AI for beginners' Neural Networks -oppitunti`: tieto, johon LLM perustuu

- `Azure AI Search` ja `Azure Cosmos DB:` vektoritietokanta tietojen tallentamiseen ja hakuhakemiston luomiseen

Käyttäjät voivat luoda harjoituskyselyitä muistiinpanoistaan, kerrata muistikorttien avulla ja tiivistää tiedot ytimekkäiksi yhteenvetoiksi. Aloitetaan katsomalla, mitä RAG on ja miten se toimii:

## Hakua täydentävä generointi (RAG)

LLM-pohjainen chatbot käsittelee käyttäjän kehotteita vastauksien luomiseksi. Se on suunniteltu vuorovaikutteiseksi ja keskustelee käyttäjien kanssa monista eri aiheista. Sen vastaukset rajoittuvat kuitenkin annettuun kontekstiin ja peruskoulutustietoihin. Esimerkiksi GPT-4:llä tiedon katkaisupäivä on syyskuu 2021, eli se ei tunne tätä ajanjakson jälkeen tapahtuneita asioita. Lisäksi LLMien koulutuksessa ei käytetä luottamuksellista tietoa, kuten henkilökohtaisia muistiinpanoja tai yrityksen tuotemanuaalia.

### Miten RAGit (Hakua täydentävä generointi) toimivat

![kuva havainnollistaa miten RAG toimii](../../../translated_images/fi/how-rag-works.f5d0ff63942bd3a6.webp)

Kuvittele haluavasi ottaa käyttöön chatbotin, joka luo kyselyitä muistiinpanoistasi. Tarvitset yhteyden tietopohjaan. Tässä RAG astuu kuvaan. RAGit toimivat seuraavasti:

- **Tietopohja:** Ennen hakua asiakirjat täytyy tuoda järjestelmään ja esikäsitellä, tyypillisesti pilkkomalla suuret asiakirjat pienempiin osiin, muuntamalla ne tekstimuotoisiksi upotuksiksi ja tallentamalla ne tietokantaan.

- **Käyttäjän kysely:** käyttäjä esittää kysymyksen

- **Haku:** Kun käyttäjä kysyy, upotusmalli hakee tietopohjasta oleellista tietoa lisäkontekstiksi, joka liitetään kehotteeseen.

- **Täydennetty generointi:** LLM parantaa vastaustaan haetun tiedon perusteella. Näin vastaus ei perustu vain esikoulutettuun tietoon, vaan myös lisätyn kontekstin tarjoamaan relevanssiin. Haettu tieto auttaa LLMia täydentämään vastauksia. LLM palauttaa käyttäjän kyselyyn vastauksen.

![kuva havainnollistaa RAG-arkkitehtuuria](../../../translated_images/fi/encoder-decode.f2658c25d0eadee2.webp)

RAGin arkkitehtuurissa on kaksi osaa: enkooderi ja dekooderi, jotka toteutetaan transformer-mallilla. Esimerkiksi kun käyttäjä esittää kysymyksen, syötetty teksti enkoodataan vektoreiksi, jotka sisältävät sanojen merkityksen. Vektorit dekoodataan dokumenttihakemistoon ja niistä generoidaan teksti käyttäjän kyselyn perusteella. LLM käyttää molempia malleja vastauksen luomiseen.

Kaksi lähestymistapaa RAGin toteutukseen ehdotetun artikkelin [Retrieval-Augmented Generation for Knowledge intensive NLP Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) mukaan ovat:

- **_RAG-Sequence_** käyttää haettuja dokumentteja parhaan mahdollisen vastauksen ennustamiseen käyttäjän kyselyyn

- **RAG-Token** käyttää dokumentteja seuraavan tokenin generointiin ja hakee ne seuraavaan tokenin generointiin luodakseen vastauksen käyttäjän kyselyyn

### Miksi käyttää RAGia?

- **Tietorikas:** varmistaa, että tekstivastaukset ovat ajan tasalla ja ajankohtaisia. Parantaa suorituskykyä erityisalojen tehtävissä hyödyntämällä sisäistä tietokantaa.

- Vähentää sepittämistä käyttämällä **todennettavissa olevaa dataa** tietopohjassa tarjoamaan kontekstia käyttäjän kysymyksiin.

- On **kustannustehokas**, koska tulee halvemmaksi kuin LLM:n hienosäätö.

## Tietopohjan luominen

Sovelluksemme perustuu henkilökohtaiseen dataan, eli AI For Beginners -koulutuksen Neural Network -oppituntiin.

### Vektoritietokannat

Vektoritietokanta on erikoistunut tietokanta, joka tallentaa, hallinnoi ja hakee upotettuja vektoreita. Se tallentaa asiakirjojen numeeriset esitykset. Tietojen pilkkominen numeerisiin upotuksiin helpottaa tekoälyjärjestelmämme tiedon ymmärtämistä ja käsittelyä.

Tallennamme upotuksemme vektoritietokantoihin, sillä LLM:illä on rajallinen määrä input-tokeneita. Koska kaikkea upotusta ei voi syöttää kerralla, ne täytyy pilkkoa osiin. Kun käyttäjä kysyy, ne upotukset, jotka vastaavat kysymystä parhaiten, palautetaan yhdessä kehotteen kanssa. Pilkkominen myös pienentää tokenien kokonaismäärää ja näin kustannuksia.

Suosittuja vektoritietokantoja ovat mm. Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant ja DeepLake. Voit luoda Azure Cosmos DB -mallin Azure CLI:n avulla seuraavalla komennolla:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Tekstistä upotuksiin

Ennen tietojen tallentamista tulee muuntaa ne vektoriupotuksiksi. Jos käsittelet suuria asiakirjoja tai pitkiä tekstejä, voit pilkkoa ne odotettujen kyselyiden mukaan. Pilkkominen voi tapahtua lause- tai kappaletasoilla. Koska pilkotut osat saavat merkityksensä ympäröivistä sanoista, voit lisätä myös muuta kontekstia, kuten asiakirjan otsikon tai tekstiä ennen tai jälkeen pilkotun osan. Voit pilkkoa datan esimerkiksi näin:

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

    # Jos viimeinen palanen ei saavuttanut vähimmäispituutta, lisää se silti
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Pilkottuasi osat voit upottaa tekstisi eri upotusmalleilla. Joitakin malleja ovat mm. word2vec, OpenAI:n ada-002, Azure Computer Vision ja monet muut. Mallin valinta riippuu käyttämästäsi kielestä, sisällön tyypistä (teksti/kuvat/audio), tuetusta syötteen koosta sekä upotuksen pituudesta.

Esimerkki upotetusta tekstistä käyttäen OpenAI:n `text-embedding-ada-002` -mallia:
![sanalla kissa esitetty upotus](../../../translated_images/fi/cat.74cbd7946bc9ca38.webp)

## Haku ja vektorihaut

Kun käyttäjä kysyy kysymyksen, hakumalli muuntaa sen vektoriksi kyselyenkooderilla, jonka jälkeen se hakee asiakirjahakemiston relevantteja vektoreita, jotka liittyvät syötteeseen. Tämän jälkeen sekä syötevektori että asiakirjavektorit muunnetaan tekstiksi ja syötetään LLM:lle.

### Haku

Haku tapahtuu, kun järjestelmä etsii nopeasti indeksoiduista asiakirjoista hakuvaatimukset täyttäviä dokumentteja. Hakijan tavoitteena on löytää asiakirjat, joita käytetään LLM:n kontekstin muodostamiseen ja tiedon jalkauttamiseen.

Hakua voidaan suorittaa monin tavoin tietokannassamme, esimerkiksi:

- **Avainsanahaku** - käytetään tekstihakuihin

- **Vektorihaku** - muuntaa dokumentit tekstistä vektoriedustuksiin upotusmallien avulla, jolloin haussa hyödynnetään sanojen merkitystä eli **semanttista hakua**. Haku suoritetaan kyselyn vektoriedustusten perusteella löytämällä dokumentit, joiden vektorit ovat lähimpänä käyttäjän kysymystä.

- **Hybridihakua** - yhdistelmää avainsana- ja vektorihakua.

Haaste hakemisessa on, jos tietokannoista ei löydy vastausta, järjestelmä tarjoaa parhaan saatavilla olevan tiedon. Tällöin voi auttaa esimerkiksi maksimi-etäisyyden asettaminen relevanssille tai hybridihaun hyödyntäminen. Tässä oppitunnissa käytämme hybridihakua, joka yhdistää vektori- ja avainsanahaun. Tallennamme datan dataframeen, jossa on sarakkeissa sekä pilkotut osat että niihin liittyvät upotukset.

### Vektoriläheisyys

Hakumalli etsii tietopohjasta lähimpänä olevia upotuksia, eli vektoreita, jotka ovat tekstiltään samankaltaisia. Käyttäjän kysely enkoodataan ensin ja etsitään sitten vastaavat läheiset upotukset. Usein käytetty mittari on kosiniläheisyys, joka perustuu kahden vektorin väliseen kulmaan.

Vaihtoehtoisia läheisyysmittareita ovat Euclidean-etäisyys, joka mittaa suoran linjan kahden vektorin päätepisteen välillä, sekä pistekertolasku (dot product), joka laskee vastaavien elementtien tulon summan.

### Hakemisto

Hakua varten täytyy rakentaa hakemisto tietopohjalle. Hakemisto tallentaa upotukset ja pystyy nopeasti palauttamaan samankaltaisimmat osat suuressa tietokannassa. Voimme luoda hakemistomme paikallisesti esimerkiksi seuraavasti:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Luo hakemisto
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Indeksin kyselyyn voit käyttää kneighbors-metodia
distances, indices = nbrs.kneighbors(embeddings)
```

### Järjestäminen uudelleen (re-ranking)

Kun olet hakenut tietokannasta, sinun täytyy ehkä järjestellä tulokset relevanssin mukaan. Uudelleenjärjestelyssä LLM hyödyntää koneoppimista parantaakseen hakutulosten relevanssia järjestämällä ne parhaista huonoimpiin. Azure AI Search -palvelussa uudelleenjärjestely tapahtuu automaattisesti semanttisella uudelleenjärjestäjällä. Esimerkki uudelleenjärjestelystä lähimpien naapureiden avulla:

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

## Kaikki yhteen

Viimeinen vaihe on lisätä LLM mukaan, jotta saamme vastauksia, jotka perustuvat tietoomme. Voimme toteuttaa sen seuraavasti:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Muunna kysymys kyselyvektoriksi
    query_vector = create_embeddings(user_input)

    # Etsi samankaltaisimmat dokumentit
    distances, indices = nbrs.kneighbors([query_vector])

    # lisää dokumentit kyselyyn tarjotaksesi kontekstia
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

    # käytä Responses-rajapintaa vastauksen luomiseen
    response = client.responses.create(
        model="gpt-4o-mini",
        temperature=0.7,
        max_output_tokens=800,
        input=messages,
        store=False,
    )

    return response.output_text

chatbot(user_input)
```

## Sovelluksen arviointi

### Arviointimittarit

- Vastauksien laatu, että ne kuulostavat luonnollisilta, sujuvilta ja inhimillisiltä

- Tiedon jalkauttaminen: arvioidaan, tuleeko vastaus annetusta dokumentaatiosta

- Relevanssi: arvioidaan, vastaako vastaus kysymykseen ja liittyykö siihen

- Sujuvuus - arvioidaan, onko vastaus kieliopillisesti järkevä

## Käyttötapaukset RAGille (Hakua täydentävä generointi) ja vektoritietokannoille

On monia eri käyttötapauksia, joissa funktiokutsut voivat parantaa sovellustasi kuten:

- Kysymys-vastausjärjestelmät: oman yritystiedon jalkauttaminen keskusteluun, jota työntekijät voivat käyttää kysymyksiin.

- Suositusjärjestelmät: voit luoda järjestelmän, joka vastaa samankaltaisimpiin arvoihin, esim. elokuvat, ravintolat ja paljon muuta.

- Chatbot-palvelut: voit tallentaa keskusteluhistorian ja personoida keskustelun käyttäjätiedon perusteella.

- Kuvahaku vektoriupotusten perusteella, hyödyllinen kuvantunnistuksessa ja poikkeavuuksien havaitsemisessa.

## Yhteenveto

Olemme käsitelleet RAGin keskeiset osa-alueet: datan lisääminen sovellukseen, käyttäjän kyselyn käsittelyn ja ulostulon. RAGin luomisen helpottamiseksi voit käyttää kehyksiä, kuten Semanti Kernel, Langchain tai Autogen.

## Tehtävä

Jatka RAGin oppimista rakentamalla:

- Etupään sovellus käyttämällä valitsemaasi kehystä

- Hyödynnä kehystä, joko LangChain tai Semantic Kernel, ja rakenna sovelluksesi uudestaan.

Onnittelut oppitunnin suorittamisesta 👏.

## Oppiminen ei lopu tähän, jatka matkaa

Oppitunnin jälkeen tutustu [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) -kokoelmaan jatkaaksesi generatiivisen AI:n osaamisen kartuttamista!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->