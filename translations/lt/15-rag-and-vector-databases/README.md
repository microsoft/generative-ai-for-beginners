# Papildytas informacijos gavimas (RAG) ir vektorinių duomenų bazės

[![Papildytas informacijos gavimas (RAG) ir vektorinių duomenų bazės](../../../translated_images/lt/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Paieškos programų pamokoje trumpai sužinojome, kaip integruoti savo duomenis į didelius kalbos modelius (LLM). Šioje pamokoje gilinsimės į duomenų pagrindimą jūsų LLM programoje, proceso mechaniką ir duomenų saugojimo metodus, įskaitant tiek įterpimus, tiek tekstą.

> **Vaizdo įrašas greitai pasirodys**

## Įvadas

Šioje pamokoje aptarsime šiuos dalykus:

- Įvadas į RAG, kas tai yra ir kodėl jis naudojamas dirbtiniame intelekte (DI).

- Suprasti, kas yra vektorinės duomenų bazės ir kaip sukurti vieną mūsų programai.

- Praktinis pavyzdys, kaip integruoti RAG į programą.

## Mokymosi tikslai

Baigę šią pamoką, galėsite:

- Paaiškinti RAG reikšmę duomenų paieškoje ir apdorojime.

- Konfigūruoti RAG programą ir pagrįsti savo duomenis LLM

- Efektyviai integruoti RAG ir vektorines duomenų bazes LLM programose.

## Mūsų scenarijus: patobulinti mūsų LLM su mūsų duomenimis

Šiai pamokai norime pridėti savo užrašus į švietimo startuolį, kas leis pokalbių robotui gauti daugiau informacijos apie skirtingas temas. Naudodamiesi užrašais, mokiniai galės geriau mokytis ir suprasti įvairius dalykus, kas palengvins pasiruošimą egzaminams. Scenarijui sukurti naudosime:

- `Azure OpenAI:` LLM, kurį naudosime savo pokalbių robotui kurti

- `AI pradedantiesiems pamoka apie neuroninius tinklus:` tai bus duomenys, kuriais pagrįsime mūsų LLM

- `Azure AI Search` ir `Azure Cosmos DB:` vektorinė duomenų bazė duomenims saugoti ir paieškos indeksui kurti

Vartotojai galės kurti praktikos testus iš savo užrašų, peržiūros korteles ir apibendrinti jas į glaustus apžvalginius tekstus. Pradėkime nuo to, kas yra RAG ir kaip jis veikia:

## Papildytas informacijos gavimas (RAG)

LLM pagrįstas pokalbių robotas apdoroja vartotojo užklausas ir generuoja atsakymus. Jis skirtas būti interaktyvus ir bendrauti su vartotojais įvairiomis temomis. Tačiau jo atsakymai apriboti pateiktu kontekstu ir pagrindiniais mokymo duomenimis. Pvz., GPT-4 žinių ribojimosi data yra 2021 m. rugsėjis, reiškianti, kad trūksta žinių apie įvykius po šios datos. Be to, LLM mokymo duomenys neįtraukia konfidencialios informacijos, tokios kaip asmeniniai užrašai ar įmonės produkto vadovas.

### Kaip veikia RAG (Papildytas informacijos gavimas)

![piešinys, rodantis, kaip veikia RAG](../../../translated_images/lt/how-rag-works.f5d0ff63942bd3a6.webp)

Tarkime, norite sukurti pokalbių robotą, kuris kuria testus iš jūsų užrašų, jums reikės ryšio su žinių baze. Čia RAG padeda. RAG veikia taip:

- **Žinių bazė:** Prieš paiešką šie dokumentai turi būti įkelti ir apdoroti, dažniausiai suskaidant didelius dokumentus į mažesnes dalis, transformuojant juos į teksto įterpimus ir saugant duomenų bazėje.

- **Vartotojo užklausa:** vartotojas užduoda klausimą

- **Paieška:** kai vartotojas užduoda klausimą, įterpimo modelis suranda susijusią informaciją iš žinių bazės ir pateikia daugiau konteksto, kuris bus įtrauktas į užklausą.

- **Papildyta generacija:** LLM pagerina savo atsakymą remdamasis gautais duomenimis. Tai leidžia atsakymui būti ne tik pagrįstam iš anksto apmokytais duomenimis, bet ir aktualia informacija iš pridėto konteksto. Gautieji duomenys naudojami LLM atsakymams papildyti. Tada LLM grąžina atsakymą vartotojo klausimui.

![piešinys, rodantis RAG architektūrą](../../../translated_images/lt/encoder-decode.f2658c25d0eadee2.webp)

RAG architektūra įgyvendinama naudojant transformerius, susidedančius iš dviejų dalių: kodavimo ir dekodavimo. Pavyzdžiui, kai vartotojas užduoda klausimą, įvesties tekstas 'užkoduojamas' į vektorius, kurie atspindi žodžių reikšmę, o vektoriai 'dekoduojami' į mūsų dokumentų indeksą ir sugeneruoja naują tekstą pagal vartotojo užklausą. LLM naudojasi kodavimo-dekodavimo modeliu, kad sugeneruotų rezultatą.

Du RAG įgyvendinimo metodai pagal pasiūlytą straipsnį: [Retrieval-Augmented Generation for Knowledge intensive NLP Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) yra:

- **_RAG-Eilutė_** naudojant rastus dokumentus geriausio galimo atsakymo į vartotojo užklausą prognozavimui

- **RAG-Žodis** naudojant dokumentus kitam žodžiui generuoti, tada juos surenkant atsakyti į vartotojo užklausą

### Kodėl verta naudoti RAG? 

- **Informacijos gausa:** užtikrina, kad tekstiniai atsakymai būtų atnaujinti ir aktualūs. Tai pagerina našumą specifinėse srityse, pasiekiant vidinę žinių bazę.

- Mažina klaidų sklaidą, naudodamas **patikrinamus duomenis** žinių bazėje, kad suteiktų kontekstą vartotojo užklausoms.

- Tai yra **ekonomiška**, nes yra pigesnė nei LLM detalus perdavimas

## Žinių bazės kūrimas

Mūsų programa remiasi asmeniniais duomenimis, t.y., Neuroninių tinklų pamoka AI pradedantiesiems kurse.

### Vektorinės duomenų bazės

Vektorinė duomenų bazė, skirtingai nei tradicinės, yra speciali duomenų bazė, skirta saugoti, valdyti ir ieškoti įterptų vektorių. Ji saugo skaitmenines dokumentų reprezentacijas. Duomenų suskaidymas į skaitmeninius įterpimus leidžia mūsų DI sistemai lengviau suprasti ir apdoroti duomenis.

Mes saugome įterpimus vektorinių duomenų bazėse, nes LLM turi apribojimą, kiek žetonų gali priimti įvestyje. Kadangi negalima perduoti visų įterpimų LLM, juos teks skaidyti į dalis, o kai vartotojas užduoda klausimą, bus pateikiami labiausiai tinkantys įterpimai kartu su užklausa. Dalyvimas taip pat sumažina išlaidas dėl perduodamų žetonų kiekio per LLM.

Populiarios vektorinės duomenų bazės: Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant ir DeepLake. Azure Cosmos DB modelį galite sukurti naudodami Azure CLI su šia komanda:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Iš teksto į įterpimus

Prieš saugodami duomenis, turėsime juos paversti vektoriniais įterpimais. Dirbdami su dideliais dokumentais ar ilgu tekstu, galite juos suskaidyti pagal numatomas užklausas. Skaldymas gali būti sakinio ar pastraipos lygiu. Kadangi skaldymas išskiria reikšmes iš aplinkinių žodžių, galite pridėti papildomą kontekstą, pvz., pavadinimą ar tekstą prieš ar po dalies. Duomenis galite skaidyti taip:

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

    # Jei paskutinė dalis nepasiekė minimalios ilgio, vis tiek ją pridėkite
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Sukūrus dalis, galime įterpti tekstą naudodami skirtingus įterpimo modelius. Kai kurie modeliai, kuriuos galite naudoti, yra: word2vec, ada-002 iš OpenAI, Azure Computer Vision ir daugelis kitų. Modelio pasirinkimas priklausys nuo naudojamų kalbų, koduojamo turinio tipo (tekstas/vaizdai/garsas), įvesties dydžio bei įterpimo išėjimo ilgio.

Pavyzdys, kaip atrodo įterptas tekstas, naudojant OpenAI `text-embedding-ada-002` modelį:
![įterpto žodžio katė vaizdas](../../../translated_images/lt/cat.74cbd7946bc9ca38.webp)

## Paieška ir vektorinė paieška

Kai vartotojas užduoda klausimą, paieškos modulis paverčia jį vektoriumi naudodamas užklausos kodavimo modelį, tada ieško mūsų dokumentų paieškos indekse atitinkančių vektorių. Baigęs, paverčia tiek įvesties, tiek dokumentų vektorius į tekstą ir perduoda per LLM.

### Paieška

Paieška vyksta tada, kai sistema bando greitai rasti dokumentus indekse, atitinkančius paieškos kriterijus. Paieškos tikslo yra gauti dokumentus, kurie bus naudojami pateikti kontekstą ir pagrįsti LLM jūsų duomenimis.

Yra keletas būdų ieškoti mūsų duomenų bazėje, pavyzdžiui:

- **Raktinių žodžių paieška** - naudojama teksto paieškai

- **Vektorinė paieška** - paverčia dokumentus iš teksto į vektorių reprezentacijas naudodama įterpimo modelius, leidžiančius vykdyti **semantinę paiešką** apskaičiuojant žodžių reikšmę. Paieška vykdoma užklausus dokumentus, kurių vektorinės reprezentacijos yra artimiausios vartotojo klausimui.

- **Hibridinė** - derinys iš raktinių žodžių ir vektorinės paieškos.

Paieškos iššūkis kyla, jei duomenų bazėje nėra panašaus atsakymo į užklausą, sistema pateiks geriausią turimą informaciją, tačiau galite naudoti taktikas, pvz., nustatyti maksimalų atstumo ribą aktualumui ar naudoti hibridinę paiešką, kuri sujungia abiejų tipų paieškas. Šioje pamokoje naudosime hibridinę paiešką, derinį iš vektorinės ir raktinių žodžių paieškos. Duomenis saugosime į lentelę su stulpeliais, kur yra dalys bei įterpimai.

### Vektorinė panašumas

Paieškos modulis ieškos žinių bazėje įterpimų, kurie yra arti vienas kito – artimiausių kaimynų, nes tai panašūs tekstai. Scenarijuje vartotojas pateikia užklausą, ji paverčiama įterpimu ir suderinama su panašiais įterpimais. Dažniausiai naudojamas panašumo matas - kosinuso panašumas, pagrįstas kampu tarp dviejų vektorių.

Galime matuoti panašumą ir kitais būdais, pavyzdžiui, Eiklido atstumu, kuris yra tiesi linija tarp vektorių galų, ir taškiniu sandauga, kuri matuoja atitinkamų elementų sandaugos sumą dviejuose vektoriumiose.

### Paieškos indeksas

Atlikdami paiešką, turėsime sukurti paieškos indeksą mūsų žinių bazei prieš pradėdami paiešką. Indeksas saugos mūsų įterpimus ir leis greitai rasti artimiausias dalis net ir didelėje duomenų bazėje. Indeksą galime sukurti lokaliai naudodami:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Sukurkite paieškos indeksą
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Norėdami užklausti indeksą, galite naudoti metodą kneighbors
distances, indices = nbrs.kneighbors(embeddings)
```

### Rezultatų pertvarkymas

Užklausus duomenų bazės, gali prireikti rūšiuoti rezultatus nuo aktualiausių. Perreitingavimo LLM naudoja mašiną mokymąsi, kad pagerintų paieškos rezultatų aktualumą, juos išdėstydamas nuo svarbiausio. Naudojant Azure AI Search, pertvarkymas atliekamas automatiškai naudojant semantinį perreitinguotoją. Pavyzdys, kaip veikia pertvarkymas naudojant artimiausius kaimynus:

```python
# Rasti panašiausius dokumentus
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Atspausdinti panašiausius dokumentus
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Apibendrinimas

Paskutinis žingsnis yra pridėti mūsų LLM, kad galėtume gauti atsakymus, pagrįstus mūsų duomenimis. Galime tai įgyvendinti taip:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Paversti klausimą į užklausos vektorių
    query_vector = create_embeddings(user_input)

    # Rasti panašiausius dokumentus
    distances, indices = nbrs.kneighbors([query_vector])

    # pridėti dokumentus prie užklausos, kad būtų suteikta konteksto
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # sujungti istoriją ir vartotojo įvestį
    history.append(user_input)

    # sukurti žinutės objektą
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # naudoti Responses API atsakymui sugeneruoti
    response = client.responses.create(
        model="gpt-5-mini",
        max_output_tokens=800,
        input=messages,
        store=False,
    )

    return response.output_text

chatbot(user_input)
```

## Mūsų programos vertinimas

### Vertinimo metrika

- Atsakymų kokybė: įsitikinti, kad jie skamba natūraliai, sklandžiai ir žmogaus kalbos pavidalu

- Duomenų pagrįstumas: vertinti, ar atsakymas atitinka pateiktus dokumentus

- Aktualumas: vertinti, ar atsakymas atitinka ir susijęs su užduotu klausimu

- Sklandumas: ar atsakymas gramatiškai prasmingas

## RAG (Papildytas informacijos gavimas) ir vektorinės duomenų bazės naudojimo atvejai

Yra daug įvairių atvejų, kai funkcijų kvietimai gali pagerinti jūsų programą, pavyzdžiui:

- Klausimų ir atsakymų sistema: pagrįskite savo įmonės duomenis pokalbių robotu, kurį darbuotojai gali naudoti klausimams užduoti.

- Rekomendacijų sistemos: galite sukurti sistemą, kuri randa panašiausias vertes, pavyzdžiui, filmus, restoranus ir daugelį kitų.

- Pokalbių robotų paslaugos: galite saugoti pokalbių istoriją ir suasmeninti pokalbį pagal vartotojo duomenis.

- Vaizdų paieška pagal vektorinius įterpimus, naudinga atliekant vaizdų atpažinimą ir anomalijų aptikimą.

## Santrauka

Apžvelgėme pagrindines RAG sritis: duomenų pridėjimą prie programos, vartotojo užklausą ir išvestį. Siekiant supaprastinti RAG kūrimą, galite naudoti frameworks, pvz., Semanti Kernel, Langchain ar Autogen.

## Užduotis

Norėdami toliau gilinti žinias apie Papildytą informacijos gavimą (RAG), galite sukurti:

- Priekį programai naudodamiesi pasirinktu framework'u

- Naudodamiesi framework'u, pvz., LangChain arba Semantic Kernel, iš naujo sukurti savo programą.

Sveikiname baigus pamoką 👏.

## Mokslas nesibaigia čia, tęskite kelionę

Baigę šią pamoką, pasižiūrėkite mūsų [Generatyvinio DI mokymosi kolekciją](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kad tęstumėte savo žinių lygį generatyvinio DI srityje!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->