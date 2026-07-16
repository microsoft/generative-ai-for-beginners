# Hozzáférés-alapú generálás (RAG) és vektoralapú adatbázisok

[![Hozzáférés-alapú generálás (RAG) és vektoralapú adatbázisok](../../../translated_images/hu/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

A keresési alkalmazások leckében röviden megtanultuk, hogyan integrálhatjuk saját adatainkat a Nagy Nyelvi Modellekbe (LLM-ek). Ebben a leckében mélyebben foglalkozunk az adatok LLM alkalmazásban való megalapozásának fogalmaival, a folyamat mechanikájával és az adatok tárolásának módszereivel, beleértve az beágyazásokat (embedding) és a szöveget egyaránt.

> **Videó hamarosan**

## Bevezetés

Ebben a leckében a következő témákat fogjuk érinteni:

- Bevezetés a RAG-be, hogy mi az, és miért használják a mesterséges intelligenciában (AI).

- Megértjük, mik az vektoralapú adatbázisok és létrehozunk egyet az alkalmazásunkhoz.

- Egy gyakorlati példa arra, hogyan integrálhatjuk a RAG-et egy alkalmazásba.

## Tanulási célok

A lecke elvégzése után képes leszel:

- Elmagyarázni a RAG jelentőségét az adatlekérés és -feldolgozás területén.

- Beállítani egy RAG alkalmazást és megalapozni az adataidat egy LLM-hez.

- Hatékonyan integrálni a RAG-et és a vektoralapú adatbázisokat LLM alkalmazásokban.

## A mi forgatókönyvünk: LLM-jeink fejlesztése saját adatainkkal

Ebben a leckében szeretnénk saját jegyzeteinket hozzáadni az oktatási startuphoz, amely lehetővé teszi, hogy a chatbot több információt kapjon a különböző témákról. A meglévő jegyzetek felhasználásával a tanulók jobban tanulhatnak és megérthetik az egyes témaköröket, így könnyebb a vizsgákra való felkészülés. Forgatókönyvünk elkészítéséhez a következőket fogjuk használni:

- `Azure OpenAI:` a LLM, amellyel a chatbotot készítjük

- `AI for beginners' leckét a Neurális Hálózatokról`: ez lesz az az adat, amihez az LLM-et alapozzuk

- `Azure AI Search` és `Azure Cosmos DB:` vektoralapú adatbázis az adataink tárolására és keresési index létrehozására

A felhasználók képesek lesznek gyakorló kvízeket létrehozni a jegyzeteikből, ismétlő kártyákat készíteni, valamint ezeket tömörített áttekintésekké összegezni. Kezdésként nézzük meg, mi az a RAG és hogyan működik:

## Hozzáférés-alapú generálás (RAG)

Egy LLM-alapú chatbot feldolgozza a felhasználók kéréseit, hogy válaszokat generáljon. Interaktívra tervezték, és széles témakörökben kommunikál a felhasználókkal. Azonban válaszai korlátozottak a rendelkezésre álló kontextusra és az alapul szolgáló betanítási adatokra. Például a GPT-4 tudásvágási pontja 2021 szeptemberében van, vagyis nem ismeri a későbbi eseményeket. Emellett a LLM-ek betanításához használt adatok nem tartalmaznak bizalmas információkat, például személyes jegyzeteket vagy cégtermék kézikönyvet.

### Hogyan működnek a RAG-ek (Hozzáférés-alapú generálás)

![rajz, amely bemutatja a RAG működését](../../../translated_images/hu/how-rag-works.f5d0ff63942bd3a6.webp)

Tegyük fel, hogy chatbotot szeretnél üzemeltetni, amely a jegyzeteidből kvízeket készít, ehhez szükséged lesz egy kapcsolatra a tudásbázishoz. Ekkor jön képbe a RAG. A RAG-ek a következőképpen működnek:

- **Tudásbázis:** A lekérés előtt ezeket a dokumentumokat be kell vinni és elő kell feldolgozni, jellemzően a nagy dokumentumokat kisebb darabokra bontják, alakítják át szövegbeli beágyazássá (embedding), és elmentik egy adatbázisban.

- **Felhasználói kérdés:** a felhasználó kérdez

- **Lekérés:** Amikor a felhasználó kérdez, a beágyazás modell releváns információkat keres a tudásbázisból, hogy több kontextust biztosítson, amelyet beépítenek a kérésszövegbe.

- **Kiegészített generálás:** az LLM a lekért adatokat felhasználva javítja válaszát. Ez lehetővé teszi, hogy a válasz ne csak előzetesen betanított adatokon alapuljon, hanem a hozzáadott kontextus releváns információit is tartalmazza. Az LLM ezt követően visszaadja a választ a felhasználó kérdésére.

![rajz a RAG architektúrájáról](../../../translated_images/hu/encoder-decode.f2658c25d0eadee2.webp)

A RAG architektúráját transzformerek valósítják meg, két részből áll: egy kódolóból (encoder) és egy dekódolóból (decoder). Például amikor a felhasználó kérdez, a bemeneti szöveget vektorokká „kódolják”, amelyek a szavak jelentését rögzítik, majd ezek a vektorok egy dokumentumindexre „dekódolódnak”, és új szöveget generálnak a felhasználói kérés alapján. Az LLM mindkét modellt használja a válasz előállításához.

Két megközelítés létezik a RAG megvalósítására a javasolt tanulmány szerint: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst):

- **_RAG-Sequence_**: a lekért dokumentumokat használja a legjobb válasz előrejelzéséhez egy felhasználói kérdésre

- **RAG-Token**: a dokumentumokat használja a következő token generálásához, majd lekéri őket a felhasználói kérdés megválaszolásához

### Miért használjunk RAG-et? 

- **Információgazdagság:** biztosítja, hogy a szöveges válaszok friss és aktuális információkat tartalmazzanak. Ezáltal javítja a teljesítményt specifikus területeken, azáltal, hogy hozzáfér az belső tudásbázishoz.

- Csökkenti a kitalációt azáltal, hogy **ellenőrizhető adatokat** használ a tudásbázisból a felhasználói kérdések kontextusához.

- **Költséghatékony** megoldás, mivel gazdaságosabb, mint egy LLM finomhangolása.

## Tudásbázis létrehozása

Az alkalmazásunk személyes adatokon alapul, nevezetesen a Neurális Hálózatok leckén az AI for Beginners tananyagból.

### Vektoralapú adatbázisok

Egy vektoralapú adatbázis a hagyományos adatbázisokkal ellentétben egy speciális adatbázis, amely beágyazott vektorok tárolására, kezelésére és keresésére szolgál. Numerikus reprezentációit tárolja a dokumentumoknak. Az adatok numerikus beágyazássá bontása megkönnyíti az AI rendszerünk számára az adatok megértését és feldolgozását.

Az embeddingeket vektoralapú adatbázisban tároljuk, mivel az LLM-eknek van bemeneti token korlátja. Mivel nem lehet az egész beágyazást átadni egy LLM-nek, darabokra kell bontanunk, és amikor a felhasználó kérdez, a kérdéshez legközelebb álló beágyazásokat visszaadja a rendszer a kéréssel együtt. Ez a darabolás csökkenti az LLM-en átadott tokenek számát, ami költségmegtakarítást jelent.

Néhány ismert vektoralapú adatbázis az Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant és DeepLake. Azure Cosmos DB modellt hozhatsz létre Azure CLI-vel a következő paranccsal:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### A szövegből beágyazás (embedding) lesz

Mielőtt eltároljuk adatainkat, először be kell őket alakítani vektor beágyazássá az adatbázisba tárolás előtt. Ha nagy dokumentumokkal vagy hosszú szövegekkel dolgozol, darabolhatod őket az általad várható lekérdezések alapján. A darabolás történhet mondatonként vagy bekezdésenként. Mivel a darabok az őket körülvevő szavakból veszik jelentésüket, hozzáadhatsz más kontextust is egy darabhoz, például a dokumentum címét vagy némi szöveget a darab előtt vagy után. Az adatok darabolása a következőképpen történhet:

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

    # Ha az utolsó darab nem érte el a minimális hosszúságot, akkor is add hozzá
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Miután daraboltuk a szöveget, különböző embedding modellekkel alakíthatjuk át. Használhatók többek között a word2vec, az OpenAI ada-002 modellje, az Azure Computer Vision és még sok más. A modellválasztás a használt nyelvtől, a kódolt tartalom típusától (szöveg/kép/hang), a bevitel méretétől és a kimeneti embedding hosszától függ.

Egy példája az OpenAI `text-embedding-ada-002` modelljével létrehozott beágyazásnak:
![a "cat" szó embeddingje](../../../translated_images/hu/cat.74cbd7946bc9ca38.webp)

## Lekérés és vektorkeresés

Amikor a felhasználó kérdez, a leképező (retriever) átalakítja a kérdést egy vektorrá a lekérdezés kódolójával, majd keres ugyanebben a dokumentum keresési indexben releváns vektorokat, amelyek kapcsolódnak a bemenethez. Ezután a bemeneti vektort és a dokumentum vektorokat szöveggé alakítja, és átadja az LLM-nek.

### Lekérés

A lekérés akkor történik, amikor a rendszer megpróbál gyorsan megtalálni azokat a dokumentumokat az indexben, amelyek megfelelnek a keresési feltételeknek. A lekérő célja, hogy olyan dokumentumokat szerezzen, amelyek kontextust nyújtanak és megalapozzák az LLM-et az adataidon.

Többféle módja van a keresésnek az adatbázisban, például:

- **Kulcsszavas keresés** - szöveges kereséshez használják

- **Vektoralapú keresés** - a dokumentumokat szövegből vektor reprezentációvá alakítja embedding modellek segítségével, lehetővé téve egy **szemantikus keresést**, amely a szavak jelentésén alapul. A lekérés a legközelebbi vektorú dokumentumokat kérdezi le a felhasználói kérdéshez.

- **Hibrid** - kulcsszavas és vektoralapú keresés kombinációja.

A lekérés kihívása, hogy ha nincs hasonló válasz a lekérdezésre az adatbázisban, akkor a rendszer a legjobb elérhető információt adja vissza. Ennek kezelésére beállíthatod a maximális relevancia távolságot, vagy használhatsz hibrid keresést, amely a kulcsszavas és vektoralapú keresést ötvözi. Ebben a leckében hibrid keresést használunk, és az adatokat egy adatkeretben tároljuk, amely oszlopokban tartalmazza a darabokat és a beágyazásokat.

### Vektor hasonlóság

A lekérő a tudásbázisban a közel álló embeddingeket keresi, a legközelebbi szomszédokat, mert ezek a szövegek hasonlóak. Amikor egy felhasználó kérdez, először beágyazást készítünk, majd ehhez hasonló embeddingeket keresünk. A leggyakoribb mérőszám a hasonlóság mérésére a koszinusz hasonlóság, amely két vektor közötti szöget veszi alapul.

Más alternatívák a hasonlóság mérésére: az euklideszi távolság, amely a két vektor végpontjait összekötő egyenes távolsága, illetve a skaláris szorzat, amely a két vektor megfelelő elemeinek szorzatainak összegét méri.

### Keresési index

A lekérés során először keresési indexet kell építenünk a tudásbázisunkhoz. Az index tárolja az embeddingeket, és gyorsan képes a leginkább hasonló darabokat előkeresni még nagy adatbázisban is. Az indexet helyben létrehozhatjuk a következőképpen:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Keresési index létrehozása
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Az index lekérdezéséhez használhatja a kneighbors metódust
distances, indices = nbrs.kneighbors(embeddings)
```

### Átrendezés (re-ranking)

Miután lekérdeztük az adatbázist, szükség lehet az eredmények relevancia szerinti sorrendezésére. Egy újrarendező LLM gépi tanulással javítja a keresési eredmények relevanciáját, úgy hogy a leginkább kapcsolódó találatok kerülnek előre. Azure AI Search használata esetén az átrendezés automatikusan történik egy szemantikus újrarendezővel. Példa az átrendezés működésére legközelebbi szomszédok alapján:

```python
# Keresse meg a leginkább hasonló dokumentumokat
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Írja ki a leginkább hasonló dokumentumokat
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Mindezek összerakva

Az utolsó lépés az LLM integrálása, hogy adatokon alapuló válaszokat kapjunk. Megvalósítása a következőképpen történhet:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Alakítsa át a kérdést lekérdezési vektorrá
    query_vector = create_embeddings(user_input)

    # Keresse meg a leginkább hasonló dokumentumokat
    distances, indices = nbrs.kneighbors([query_vector])

    # Adjon hozzá dokumentumokat a lekérdezéshez a kontextus biztosításához
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # Egyesítse a történetet és a felhasználói bemenetet
    history.append(user_input)

    # Hozzon létre egy üzenet objektumot
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # Használja a Responses API-t a válasz generálásához
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

## Az alkalmazásunk értékelése

### Értékelési mutatók

- A válaszok minősége: biztosítva, hogy természetesnek, folyékonynak és emberinek hangozzanak

- A megalapozottság: értékelve, hogy a válasz az ellátott dokumentumokból ered-e

- A relevancia: értékelve, hogy a válasz illeszkedik-e és kapcsolódik-e a feltett kérdéshez

- A folyékonyság - hogy a válasz grammatikailag értelmes-e

## RAG és vektoralapú adatbázisok felhasználási esetei

Számos különböző felhasználási terület létezik, ahol a funkcióhívások javíthatják alkalmazásodat, például:

- Kérdés-válasz rendszer: céges adatokat alapozhatsz egy chathez, amit az alkalmazottak kérdésekre használhatnak.

- Ajánló rendszerek: olyan rendszert készíthetsz, ami a leginkább hasonló értékeket párosítja, például filmeket, éttermeket és még sok mást.

- Chatbot szolgáltatások: elmentheted a chat előzményeit, és személyre szabhatod a beszélgetést a felhasználói adatok alapján.

- Képkeresés vektorbeli beágyazások alapján, hasznos képfelismerésnél és anomália detektálásnál.

## Összefoglalás

Áttekintettük a RAG alapvető területeit az alkalmazás adatainak hozzáadásától a felhasználói kérdésen át a válaszig. A RAG készítésének egyszerűsítésére keretrendszereket használhatsz, mint a Semanti Kernel, Langchain vagy Autogen.

## Feladat

A Hozzáférés-alapú generálás (RAG) tanulásának folytatásához készítsd el:

- Egy frontendet az alkalmazáshoz a választott keretrendszerrel

- Használj egy keretrendszert, például LangChain vagy Semantic Kernel, és rekonstruáld az alkalmazásodat.

Gratulálunk a lecke elvégzéséhez 👏.

## A tanulás nem ér véget itt, folytasd az utat

A lecke elvégzése után nézd meg a [Generatív AI Learning kollekciónkat](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejleszd generatív AI tudásodat!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->