# At retrieval augmentuota generacija (RAG) ir vektorinės duomenų bazės

[![At retrieval augmentuota generacija (RAG) ir vektorinės duomenų bazės](../../../translated_images/lt/15-lesson-banner.ac49e59506175d4f.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Paieškos taikymų pamokoje trumpai sužinojome, kaip integruoti savo duomenis į didelius kalbos modelius (LLM). Šioje pamokoje gilinsimės į jūsų duomenų pagrindimą LLM programoje, proceso mechaniką ir duomenų saugojimo metodus, įskaitant tiek įterpinius, tiek tekstą.

> **Vaizdo įrašas netrukus**

## Įvadas

Šioje pamokoje aptarsime šiuos dalykus:

- Įvadas į RAG, kas tai yra ir kodėl tai naudojama dirbtiniame intelekte (DI).

- Kas yra vektorinės duomenų bazės ir kaip sukurti vieną mūsų programai.

- Praktinis pavyzdys, kaip integruoti RAG į programą.

## Mokymosi tikslai

Baigę šią pamoką, galėsite:

- Paaiškinti RAG svarbą duomenų ieškojime ir apdorojime.

- Sukonfigūruoti RAG programą ir pagrįsti LLM savo duomenimis.

- Efektyviai integruoti RAG ir vektorines duomenų bazes LLM programose.

## Mūsų scenarijus: pageriname savo LLM su savo duomenimis

Šiai pamokai norime pridėti savo užrašus į švietimo startuolį, kuris leidžia pokalbių robotui gauti daugiau informacijos apie įvairias temas. Naudodami savo užrašus, mokiniai galės geriau mokytis ir suprasti įvairias temas, taip palengvindami pasiruošimą egzaminams. Kuriant mūsų scenarijų naudosime:

- `Azure OpenAI:` LLM, kurį naudosime kurdami savo pokalbių robotą

- `AI for beginners' lesson on Neural Networks`: tai bus duomenys, kuriais pagrįsime savo LLM

- `Azure AI Search` ir `Azure Cosmos DB:` vektorinę duomenų bazę duomenims saugoti ir paieškos indeksui sukurti

Vartotojai galės kurti praktikos testus ir peržiūros korteles iš savo užrašų bei apibendrinti tuos užrašus į glaustus santraukas. Pradėkime pažvelgdami, kas yra RAG ir kaip jis veikia:

## Retrieval Augmented Generation (RAG)

LLM pagrįstas pokalbių robotas apdoroja vartotojo užklausas, kad sugeneruotų atsakymus. Jis sukurtas būti interaktyvus ir bendrauti su vartotojais įvairiausiomis temomis. Tačiau jo atsakymai ribojasi tik pateiktu kontekstu ir pagrindiniais mokymosi duomenimis. Pavyzdžiui, GPT-4 žinių užriba yra 2021 m. rugsėjis, o tai reiškia, kad jis neturi žinių apie įvykius po šios datos. Be to, LLM mokymui naudoti duomenys neprisijungia konfidencialios informacijos, tokios kaip asmeniniai užrašai ar įmonės produkto vadovas.

### Kaip veikia RAG (retrieval augmentuota generacija)

![paveikslas, rodantis kaip veikia RAG](../../../translated_images/lt/how-rag-works.f5d0ff63942bd3a6.webp?WT.mc_id=academic-105485-koreyst)

Tarkime, norite įdiegti pokalbių robotą, kuris kuria testus iš jūsų užrašų — jums reikės ryšio su žinių baze. Čia į pagalbą ateina RAG. RAG veikia taip:

- **Žinių bazė:** prieš paiešką šie dokumentai turi būti įkelti ir išankstiniu būdu apdoroti, dažniausiai dideli dokumentai suskaidomi į mažesnes dalis, paverčiami teksto įterpiniais ir saugomi duomenų bazėje.

- **Vartotojo užklausa:** vartotojas užduoda klausimą

- **Paieška:** kai vartotojas užduoda klausimą, įterpimų modelis įtraukdų aktualią informaciją iš mūsų žinių bazės, kad užklausa turėtų daugiau konteksto.

- **Papildoma generacija:** LLM pagerina savo atsakymą remdamasis paieškos metu gautais duomenimis. Tai leidžia sugeneruotam atsakymui būti paremti tiek iš anksto apmokytais duomenimis, tiek atitinkama konteksto informacija. Paieškos duomenys naudojami papildyti LLM atsakymus. LLM tada pateikia atsakymą vartotojo klausimui.

![Diagrama, rodanti RAG architektūrą](../../../translated_images/lt/encoder-decode.f2658c25d0eadee2.webp?WT.mc_id=academic-105485-koreyst)

RAG derina paieškos įrankį su generatoriumi: užklausa paverčiama vektoriumi, palyginama su dokumentų indeksu ieškant atitinkamų teksto dalių, kurios pateikiamos kaip kontekstas LLM, kuris sugeneruoja atsakymą. Paieškos įrankis ir generatorius gali naudoti skirtingus modelius; RAG nereikalauja kodavimo-dekodavimo transformatoriaus.

Du požiūriai į RAG įgyvendinimą pagal siūlomą darbą: [Retrieval-Augmented Generation for Knowledge intensive NLP (natūralios kalbos apdorojimo programinė įranga) užduotys](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) yra:

- **_RAG-Sequencija_** naudojant paimtus dokumentus geriausiam galimam atsakymui į vartotojo užklausą prognozuoti

- **RAG-Token** naudojant dokumentus kitam žodžiui generuoti, tada juos paimant atsakant į vartotojo užklausą

### Kodėl verta naudoti RAG? 

- **Informacijos gausa:** užtikrina, kad tekstiniai atsakymai būtų atnaujinti ir aktualūs. Todėl pagerina našumą domeno specifinėse užduotyse prieigos prie vidinės žinių bazės dėka.

- Mažina išgalvojimą, naudodama **patikimus duomenis** žinių bazėje, kad pateiktų kontekstą vartotojo užklausoms.

- Tai yra **ekonomiška**, nes kainuoja mažiau nei LLM tikslinimas

## Žinių bazės kūrimas

Mūsų programa paremta mūsų asmeniniais duomenimis, t.y., neuroninių tinklų pamoka iš AI pradedantiesiems mokymo plano.

### Vektorinės duomenų bazės

Vektorinė duomenų bazė, priešingai nei tradicinės duomenų bazės, yra specializuota duomenų bazė, skirta saugoti, valdyti ir ieškoti įterptųjų vektorių. Joje laikomi dokumentų skaitmeniniai atvaizdai. Duomenų suskaidymas į skaitmenines įterptis leidžia mūsų DI sistemai lengviau suprasti ir apdoroti duomenis.

Kadangi LLM turi ribą įvesties žodžių skaičiui, mes suskaidome dokumentus į dalis prieš juos įterpiant. Kai vartotojas pateikia užklausą, įterptys, labiausiai panašūs į užklausą, identifikuoja susijusias teksto dalis, kurios pateikiamos su užklausos eilute. Dalijimas taip pat sumažina žodžių skaičių, perduodamą LLM, todėl gali sumažinti išlaidas.

Kai kurios populiarios vektorinių duomenų bazės yra Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant ir DeepLake. Galite sukurti Azure Cosmos DB modelį naudodami Azure CLI tokiu komandiniu sakiniu:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Iš teksto į įterptis

Prieš saugodami duomenis, turėsime juos paversti į vektorines įterptis, kad būtų galima saugoti duomenų bazėje. Jei dirbate su dideliais dokumentais arba ilgesnėmis tekstų dalimis, galite jas suskaldyti pagal numatomas užklausas. Dalijimas gali būti sakinio arba pastraipos lygyje. Kadangi dalijimas gautas prasmes iš žodžių aplinkoje, galite pridėti papildomą kontekstą daliai, pvz., pridėti dokumento pavadinimą arba įtraukti tekstą prieš ar po dalies. Duomenis galite suskaldyti taip:

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

Dalijus, galime įterpti tekstą naudodami įvairius įterpimo modelius. Kai kurie modeliai yra: word2vec, OpenAI ada-002, Azure Computer Vision ir kt. Modelio pasirinkimas priklausys nuo kalbų, kurias naudojate, koks turinys koduojamas (tekstai/vaizdai/garsas), įvesties dydžio, kurį modelis gali koduoti, ir įterpties ilgumo.

Pavyzdys teksto įterpties naudojant OpenAI `text-embedding-ada-002` modelį yra:
![žodžio katė įterpties vaizdas](../../../translated_images/lt/cat.74cbd7946bc9ca38.webp?WT.mc_id=academic-105485-koreyst)

## Duomenų paieška ir vektorinė paieška

Kai vartotojas pateikia užklausą, paimtuvas ją paverčia į vektorių naudodamas užklausos koduotoją, tada ieško dokumentų paieškos indekse tinkamų vektorių, susijusių su įvestimi. Baigęs, jis abu – įvesties vektorių ir dokumentų vektorius – paverčia atgal į tekstą ir perduoda LLM.

### Paėmimas

Paėmimas įvyksta, kai sistema bando greitai rasti dokumentus iš indekso, atitinkančius paieškos kriterijus. Paėmėjo tikslas yra gauti dokumentus, kurie bus naudojami kontekstui suteikti ir įtvirtinti LLM pagal jūsų duomenis.

Paiešką duomenų bazėje galima atlikti keliomis būdais, pvz.:

- **Raktinių žodžių paieška** - naudojama teksto paieškai

- **Vektorinė paieška** - dokumentus paverčia iš teksto į vektorines reprezentacijas naudojant įterpimo modelius, leidžiant atlikti **semantinę paiešką** pagal žodžių reikšmę. Paieška vykdoma užklausų pagal dokumentus, kurių vektorinės reprezentacijos yra arčiausiai vartotojo klausimo.

- **Hibridinis** - derinys tarp raktinių žodžių ir vektorinės paieškos.

Problema kyla, kai duomenų bazėje nėra panašaus atsakymo į užklausą, sistema tada pateiks geriausią turimą informaciją, bet galite naudoti taktiką, pvz., nustatyti maksimalią atstumą svarbai arba naudoti hibridinę paiešką, kombinuojančią raktinius žodžius ir vektorinę paiešką. Šioje pamokoje naudosime hibridinę paiešką, derinant abi paieškas. Mes saugosime duomenis duomenų rėmelyje, kur stulpeliai talpins dalis ir įterptis.

### Vektorinė panašumas

Paėmėjas ieškos žinių bazėje artimų įterpių – artimiausių kaimynų – nes jie atspindi panašius tekstus. Šiuo atveju, kai vartotojas pateikia užklausą, ji pirmiausiai įterpiama ir palyginama su panašiomis įterptimis. Dažniausiai naudojamas vektorinės panašumo matas yra kosinuso panašumas, pagrįstas kampu tarp dviejų vektorių.

Kiti panašumo matavimai yra Euklido atstumas, tiesi linija tarp vektorių galų, ir taškų sandauga, rodanti atitinkamų dviejų vektorių elementų sandaugų sumą.

### Paieškos indeksas

Atlikdami paėmimą, turėsime sukurti paieškos indeksą mūsų žinių bazei prieš atlikdami paiešką. Indeksas saugos mūsų įterptis ir greitai rinks artimiausias dalis net didelėje duomenų bazėje. Indeksą galime sukurti lokaliai naudodami:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Rikiavimas iš naujo

Pateikę užklausą duomenų bazėje galite norėti rūšiuoti rezultatus nuo svarbiausių. Perdirbantis LLM naudoja mašininį mokymąsi, kad pagerintų paieškos rezultatų aktualumą, juos rūšiuodamas nuo svarbiausių. Naudojant Azure AI Search, perrinkimas atliekamas automatiškai, naudojant semantinį perrinkėją. Perrinkimo veikimo pavyzdys naudojant artimiausius kaimynus:

```python
# Find the most similar documents
distances, indices = nbrs.kneighbors([query_vector])

# Print the three most similar documents with their distance to the question
for distance, index in zip(distances[0][:3], indices[0][:3]):
    print(flattened_df['chunks'].iloc[index])
    print(flattened_df['path'].iloc[index])
    print(distance)
```

## Sudėjus viską kartu

Paskutinis žingsnis yra pridėti mūsų LLM, kad gautume atsakymus, grindžiamus mūsų duomenimis. Galime įgyvendinti taip:

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
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # use the Responses API to generate a response
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

- Atsakymų kokybė, užtikrinant, kad jie skambėtų natūraliai, sklandžiai ir kaip žmogaus kalba

- Duomenų pagrįstumas: vertinti, ar atsakymas remiasi pateiktais dokumentais

- Aktualumas: vertinti, ar atsakymas atitinka ir susijęs su užduotu klausimu

- Sklandumas - ar atsakymas yra gramatiškai prasmingas

## RAG (Retrieval Augmented Generation) ir vektorinių duomenų bazių naudojimo atvejai

Yra daug atvejų, kur RAG gali pagerinti jūsų programą, pvz.:

- Klausimų ir atsakymų sistema: pagrindžiant jūsų įmonės duomenimis pokalbių sistemas, kur darbuotojai gali užduoti klausimus.

- Rekomendacijų sistemos: kai kuriate sistemą, kuri suranda panašias reikšmes, pvz., filmus, restoranus ir daug kitų.

- Pokalbių robotų paslaugos: galite saugoti pokalbių istoriją ir personalizuoti pokalbių turinį pagal vartotojo duomenis.

- Vaizdų paieška pagal vektorines įterptis, naudinga atliekant vaizdų atpažinimą ir anomalijų aptikimą.

## Apibendrinimas

Apžvelgėme pagrindinius RAG aspektus nuo duomenų pridėjimo iki programos, vartotojo užklausos ir atsakymo gavimo. Supaprastinti RAG kūrimą galite naudodami sistemas kaip Semantic Kernel, LangChain arba AutoGen.

## Namų darbai

Norėdami tęsti mokymąsi apie Retrieval Augmented Generation (RAG), galite sukurti:

- Sukurkite programos front-endą naudodami pasirinktą sistemą

- Naudokite sistemą, pvz., LangChain arba Semantic Kernel, ir perkurkite savo programą.

Sveikiname su pamokos baigimu 👏.

## Mokymasis čia nesibaigia, tęskite kelionę

Baigę šią pamoką, peržiūrėkite mūsų [Generuojamojo DI mokymosi kolekciją](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kad toliau keliate savo Generuojamojo DI žinias!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->