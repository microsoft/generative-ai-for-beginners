<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4b0266fbadbba7ded891b6485adc66d",
  "translation_date": "2025-10-17T21:27:02+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "hu"
}
-->
# Visszakeresésen alapuló generálás (RAG) és vektoralapú adatbázisok

[![Visszakeresésen alapuló generálás (RAG) és vektoralapú adatbázisok](../../../translated_images/15-lesson-banner.ac49e59506175d4fc6ce521561dab2f9ccc6187410236376cfaed13cde371b90.hu.png)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

A keresési alkalmazások leckéjében röviden megismerkedtünk azzal, hogyan integrálhatjuk saját adatainkat a nagy nyelvi modellekbe (LLM-ek). Ebben a leckében mélyebben belemerülünk abba, hogyan alapozhatjuk meg az adatainkat az LLM-alkalmazásunkban, a folyamat mechanikájába, valamint az adatok tárolásának módszereibe, beleértve az embeddingeket és a szövegeket is.

> **Videó hamarosan érkezik**

## Bevezetés

Ebben a leckében az alábbiakat fogjuk áttekinteni:

- Bevezetés a RAG-ba: mi az, és miért használják a mesterséges intelligenciában (AI).

- Megértjük, hogy mik azok a vektoralapú adatbázisok, és létrehozunk egyet az alkalmazásunkhoz.

- Egy gyakorlati példa arra, hogyan integrálhatjuk a RAG-ot egy alkalmazásba.

## Tanulási célok

A lecke elvégzése után képes leszel:

- Elmagyarázni a RAG jelentőségét az adatvisszakeresésben és feldolgozásban.

- Beállítani egy RAG-alkalmazást, és az adataidat egy LLM-hez alapozni.

- Hatékonyan integrálni a RAG-ot és a vektoralapú adatbázisokat LLM-alkalmazásokba.

## Szenáriónk: saját adataink hozzáadása az LLM-hez

Ebben a leckében szeretnénk hozzáadni saját jegyzeteinket az oktatási startuphoz, amely lehetővé teszi a chatbot számára, hogy több információt nyújtson a különböző témákról. A jegyzeteink segítségével a tanulók jobban tanulhatnak, és könnyebben megérthetik a különböző témákat, megkönnyítve ezzel a vizsgákra való felkészülést. A szcenárió létrehozásához az alábbiakat fogjuk használni:

- `Azure OpenAI:` az LLM, amelyet a chatbotunk létrehozásához használunk.

- `AI kezdőknek szóló lecke a neurális hálózatokról:` ez lesz az adat, amelyre az LLM-ünket alapozzuk.

- `Azure AI Search` és `Azure Cosmos DB:` vektoralapú adatbázis az adataink tárolására és keresési index létrehozására.

A felhasználók képesek lesznek gyakorló kvízeket készíteni a jegyzeteikből, tanulókártyákat létrehozni és összefoglalni azokat rövid áttekintésekre. Kezdjük azzal, hogy megnézzük, mi is az a RAG, és hogyan működik:

## Visszakeresésen alapuló generálás (RAG)

Egy LLM-alapú chatbot a felhasználói kérdéseket dolgozza fel, hogy válaszokat generáljon. Interaktív módon működik, és széles körű témákban kommunikál a felhasználókkal. Azonban a válaszai korlátozottak az adott kontextusra és az alapvető tanulási adatokra. Például a GPT-4 tudásának határa 2021 szeptemberére esik, ami azt jelenti, hogy nem rendelkezik ismeretekkel az ezt követően történt eseményekről. Ezenkívül az LLM-ek tanításához használt adatok nem tartalmaznak bizalmas információkat, például személyes jegyzeteket vagy egy vállalat termékkézikönyvét.

### Hogyan működnek a RAG-ok (visszakeresésen alapuló generálás)

![rajz, amely bemutatja, hogyan működnek a RAG-ok](../../../translated_images/how-rag-works.f5d0ff63942bd3a638e7efee7a6fce7f0787f6d7a1fca4e43f2a7a4d03cde3e0.hu.png)

Tegyük fel, hogy egy chatbotot szeretnél telepíteni, amely kvízeket készít a jegyzeteidből. Ehhez szükséged lesz egy kapcsolat létrehozására a tudásbázissal. Itt jön képbe a RAG. A RAG-ok működése a következő:

- **Tudásbázis:** A visszakeresés előtt ezeket a dokumentumokat be kell olvasni és elő kell dolgozni, általában nagy dokumentumokat kisebb részekre bontva, szövegembeddingekké alakítva és adatbázisban tárolva.

- **Felhasználói kérdés:** A felhasználó feltesz egy kérdést.

- **Visszakeresés:** Amikor a felhasználó kérdést tesz fel, az embedding modell releváns információkat keres a tudásbázisunkban, hogy több kontextust biztosítson, amelyet beépítenek a kérdésbe.

- **Kibővített generálás:** Az LLM javítja a válaszát a visszakeresett adatok alapján. Ez lehetővé teszi, hogy a generált válasz ne csak az előre tanított adatokon alapuljon, hanem az adott kontextusból származó releváns információkon is. A visszakeresett adatokat az LLM válaszainak kibővítésére használják. Az LLM ezután választ ad a felhasználó kérdésére.

![rajz, amely bemutatja a RAG-ok architektúráját](../../../translated_images/encoder-decode.f2658c25d0eadee2377bb28cf3aee8b67aa9249bf64d3d57bb9be077c4bc4e1a.hu.png)

A RAG-ok architektúrája transzformerekkel valósul meg, amelyek két részből állnak: egy kódolóból és egy dekódolóból. Például, amikor egy felhasználó kérdést tesz fel, a bemeneti szöveg 'kódolva' lesz vektorokká, amelyek rögzítik a szavak jelentését, majd a vektorok 'dekódolva' lesznek a dokumentumindexünkbe, és új szöveget generálnak a felhasználói kérdés alapján. Az LLM mind kódoló-dekódoló modellt használ az output generálásához.

A RAG megvalósításának két megközelítése a javasolt tanulmány szerint: [Retrieval-Augmented Generation for Knowledge intensive NLP (természetes nyelvi feldolgozó szoftver) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst):

- **_RAG-Sequence_**: visszakeresett dokumentumok használata a legjobb válasz előrejelzésére a felhasználói kérdésre.

- **RAG-Token**: dokumentumok használata a következő token generálására, majd visszakeresésük a felhasználói kérdés megválaszolásához.

### Miért használnád a RAG-okat?

- **Információgazdagság:** biztosítja, hogy a szöveges válaszok naprakészek és aktuálisak legyenek. Ezáltal javítja a teljesítményt a specifikus területeken, hozzáférve a belső tudásbázishoz.

- Csökkenti a kitalálásokat azáltal, hogy **ellenőrizhető adatokat** használ a tudásbázisban, hogy kontextust biztosítson a felhasználói kérdésekhez.

- **Költséghatékony**, mivel gazdaságosabb, mint egy LLM finomhangolása.

## Tudásbázis létrehozása

Az alkalmazásunk a személyes adatainkon alapul, azaz az AI kezdőknek szóló tanterv neurális hálózatokról szóló leckéjén.

### Vektoralapú adatbázisok

A vektoralapú adatbázis, a hagyományos adatbázisoktól eltérően, egy speciális adatbázis, amelyet beágyazott vektorok tárolására, kezelésére és keresésére terveztek. Számértékeket tárol, amelyek a dokumentumokat reprezentálják. Az adatok számértékekre bontása megkönnyíti AI rendszerünk számára az adatok megértését és feldolgozását.

Az embeddingeket vektoralapú adatbázisokban tároljuk, mivel az LLM-ek korlátozott számú tokent képesek bemeneti adatként elfogadni. Mivel nem tudod az összes embeddinget átadni egy LLM-nek, kisebb részekre kell bontanod őket, és amikor a felhasználó kérdést tesz fel, a kérdéshez leginkább hasonló embeddingek kerülnek vissza a kérdéssel együtt. A darabolás csökkenti az LLM-en keresztül átadott tokenek számával kapcsolatos költségeket is.

Népszerű vektoralapú adatbázisok közé tartozik az Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant és DeepLake. Az Azure Cosmos DB modellt létrehozhatod az Azure CLI használatával az alábbi parancs segítségével:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Szövegből embeddingek

Mielőtt tárolnánk az adatainkat, vektor embeddingekké kell alakítanunk őket, mielőtt az adatbázisba kerülnek. Ha nagy dokumentumokkal vagy hosszú szövegekkel dolgozol, darabolhatod őket az elvárt kérdések alapján. A darabolás történhet mondat szinten vagy bekezdés szinten. Mivel a darabolás a környező szavak jelentéséből származtatja a jelentést, hozzáadhatsz némi kontextust a darabhoz, például a dokumentum címét vagy némi szöveget a darab előtt vagy után. Az adatokat az alábbi módon darabolhatod:

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

Miután daraboltuk, különböző embedding modellek segítségével beágyazhatjuk a szöveget. Néhány használható modell: word2vec, ada-002 az OpenAI-tól, Azure Computer Vision és sok más. A választott modell függ a használt nyelvektől, a kódolandó tartalom típusától (szöveg/kép/hang), a kódolható bemenet méretétől és az embedding kimenet hosszától.

Egy példa az OpenAI `text-embedding-ada-002` modelljével beágyazott szövegre:
![a "macska" szó embeddingje](../../../translated_images/cat.74cbd7946bc9ca380a8894c4de0c706a4f85b16296ffabbf52d6175df6bf841e.hu.png)

## Visszakeresés és vektorkeresés

Amikor a felhasználó kérdést tesz fel, a visszakereső vektorrá alakítja azt a lekérdezési kódoló segítségével, majd a dokumentum keresési indexünkben releváns vektorokat keres, amelyek kapcsolódnak a bemenethez. Miután ez megtörtént, mind a bemeneti vektort, mind a dokumentum vektorokat szöveggé alakítja, és átadja az LLM-nek.

### Visszakeresés

A visszakeresés akkor történik, amikor a rendszer gyorsan megpróbálja megtalálni az indexből azokat a dokumentumokat, amelyek megfelelnek a keresési kritériumoknak. A visszakereső célja, hogy olyan dokumentumokat találjon, amelyek kontextust biztosítanak, és az LLM-et az adataidra alapozzák.

Számos módja van az adatbázisunkban történő keresésnek, például:

- **Kulcsszókeresés** - szöveges keresésekhez használják.

- **Szemantikai keresés** - a szavak szemantikai jelentését használja.

- **Vektorkeresés** - a dokumentumokat szövegből vektor reprezentációkká alakítja embedding modellek segítségével. A visszakeresés a dokumentumok lekérdezésével történik, amelyek vektor reprezentációi a legközelebb állnak a felhasználói kérdéshez.

- **Hibrid** - a kulcsszó- és vektorkeresés kombinációja.

A visszakeresés kihívása akkor jelentkezik, amikor nincs hasonló válasz a lekérdezésre az adatbázisban. A rendszer ekkor a legjobb információt adja vissza, amit talál, azonban alkalmazhatsz taktikákat, például beállíthatod a relevancia maximális távolságát, vagy használhatsz hibrid keresést, amely kombinálja a kulcsszó- és vektorkeresést. Ebben a leckében hibrid keresést fogunk használni, amely a vektor- és kulcsszókeresés kombinációja. Az adatainkat egy adatkeretbe fogjuk tárolni, amely oszlopokat tartalmaz a darabokkal és az embeddingekkel.

### Vektorhasonlóság

A visszakereső átnézi a tudásbázist, hogy megtalálja az egymáshoz közel álló embeddingeket, a legközelebbi szomszédokat, mivel ezek hasonló szövegek. Abban az esetben, ha a felhasználó kérdést tesz fel, először beágyazásra kerül, majd hasonló embeddingekkel párosítják. A leggyakrabban használt mérőszám, amely megmutatja, mennyire hasonlóak a különböző vektorok, a koszinusz hasonlóság, amely a két vektor közötti szög alapján működik.

A hasonlóság mérésére más alternatívák is használhatók, például az euklideszi távolság, amely a vektor végpontjai közötti egyenes vonal, és a skalárszorzat, amely a két vektor megfelelő elemeinek szorzatainak összegét méri.

### Keresési index

A visszakeresés során szükségünk lesz egy keresési index létrehozására a tudásbázisunkhoz, mielőtt keresést végeznénk. Az index tárolja az embeddingeket, és gyorsan visszakeresi a leginkább hasonló darabokat még egy nagy adatbázisban is. Az indexet helyben létrehozhatjuk az alábbi módon:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Újrarangsorolás

Miután lekérdezted az adatbázist, előfordulhat, hogy a találatokat a legrelevánsabbtól kezdve kell sorba állítanod. Az újrarangsoroló LLM gépi tanulást használ a keresési eredmények relevanciájának javítására, azokat a legrelevánsabb sorrendbe állítva. Az Azure AI Search automatikusan elvégzi az újrarangsorolást egy szemantikai újrarangsoroló segítségével. Az újrarangsorolás működésének példája a legközelebbi szomszédok használatával:

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

## Minden összekapcsolása

Az utolsó lépés az LLM hozzáadása, hogy olyan válaszokat kapjunk, amelyek az adatainkra alapozottak. Az alábbi módon valósíthatjuk meg:

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

## Az alkalmazásunk értékelése

### Értékelési metrikák

- A válaszok minősége, biztosítva, hogy természetesnek, folyékonynak és emberinek hangozzanak.

- Az adatok alapozottsága: értékelve, hogy a válasz a megadott dokumentumokból származik-e.

- Relevancia: értékelve, hogy a válasz megfelel-e és kapcsolódik-e a feltett kérdéshez.

- Folyékonyság: hogy a válasz nyelvtanilag érthető-e.

## RAG (visszakeresésen alapuló generálás) és vektoralapú adatbázisok használati esetei

Számos különböző használati eset létezik, ahol a funkcióhívások javíthatják az alkalmazásodat, például:

- Kérdés-válasz: a vállalati adatokat egy chathez alapozva, amelyet az alkalmazottak kérdések feltevésére használhatnak.

- Ajánlórendszerek: ahol létrehozhatsz egy rendszert, amely a leginkább hasonló értékeket párosítja, például filmeket, éttermeket és sok mást.

- Chatbot szolgáltatások: tárolhatod a chat történetet, és személyre szabhatod a beszélgetést a felhasználói adatok alapján.

- Képkeresés vektor embeddingek alapján, hasznos kép felismerés és anomália detektálás során.

##

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.