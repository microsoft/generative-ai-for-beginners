# Taastepõhine täiendusgeneratsioon (RAG) ja vektandmebaasid

[![Taastepõhine täiendusgeneratsioon (RAG) ja vektandmebaasid](../../../translated_images/et/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Otsingu rakenduste õppetükis õppisime lühidalt, kuidas integreerida oma andmeid suurtesse keelemudelitesse (LLM). Selles õppetükis süveneme lähemalt andmete mahamaaramisse LLM-rakenduses, protsessi mehhanismidesse ja andmete salvestamise meetoditesse, sealhulgas nii sisendite kui ka teksti osas.

> **Video Peagi Saadaval**

## Sissejuhatus

Selles õppetükis käsitleme järgmist:

- Sissejuhatus RAG-isse, mis see on ja miks seda tehisintellektis kasutatakse.

- Mõistmine, mis on vektandmebaasid ja kuidas luua meie rakenduse jaoks üks.

- Praktiline näide sellest, kuidas integreerida RAG rakendusse.

## Õpieesmärgid

Pärast selle õppetüki läbimist oskad sa:

- Selgitada RAG tähtsust andmete päringus ja töötlemises.

- Seadistada RAG-rakendus ja siduda oma andmed LLM-iga.

- Tõhusalt integreerida RAG ja vektandmebaase LLM-rakendustesse.

## Meie stsenaarium: täiustada oma LLM-e oma andmetega

Selle õppetüki jaoks tahame lisada haridusettevõtte jaoks oma märkmed, mis võimaldavad vestlusrobotil saada rohkem informatsiooni erinevate teemade kohta. Märkmete abil saavad õppijad paremini õppida ja mõista erinevaid teemasid, muutes eksamiteks kordamise lihtsamaks. Me kasutame oma stsenaariumi loomiseks:

- `Azure OpenAI:` LLM, mida kasutame vestlusroboti loomiseks.

- `Algajatele mõeldud tehisintellekti õppetükk närvivõrkudest:` see on andmestik, millele meie LLM tugineb.

- `Azure AI Search` ja `Azure Cosmos DB:` vektandmebaas, kuhu salvestame andmed ja loome otsinguindeksi.

Kasutajad saavad luua harjutusküsimusi oma märkmetest, kordamise kaarte ja kokkuvõtteid lühikestes ülevaadetes. Alustuseks vaatame, mis on RAG ja kuidas see töötab:

## Taastepõhine täiendusgeneratsioon (RAG)

LLM-i jõul töötav vestlusrobot töötleb kasutaja päringuid, et genereerida vastuseid. See on loodud olema interaktiivne ja suhelda kasutajatega paljudel teemadel. Kuid selle vastused on piiratud antud konteksti ja selle baasteadmistega. Näiteks GPT-4 teadmistelõpp on september 2021, mis tähendab, et sellel puudub teadmine sündmustest pärast seda kuupäeva. Lisaks ei sisalda LLM-ide treeningandmed konfidentsiaalset infot nagu isiklikud märkmed või ettevõtte toodete juhendid.

### Kuidas RAG-id (Taastepõhine täiendusgeneratsioon) töötavad

![joonis, mis näitab, kuidas RAG-id töötavad](../../../translated_images/et/how-rag-works.f5d0ff63942bd3a6.webp)

Oletame, et soovid käivitada vestlusroboti, mis loob sinu märkmetest viktoriine, vajab ta ühendust teadmistebaasiga. Siin tulebki appi RAG. RAG-id töötavad järgmiselt:

- **Teadmistebaas:** Enne päringut tuleb dokumendid haarata ja töödelda, tavaliselt suuremad dokumendid jagatakse väiksemateks osadeks, teisendatakse teksti sisenditeks ja salvestatakse andmebaasi.

- **Kasutaja päring:** kasutaja esitab küsimuse.

- **Päringutegemine:** kui kasutaja küsib, saab sisendi mudelist sobivad andmed teadmistebaasist, pakkudes rohkem konteksti, mida lisatakse päringusse.

- **Täiendatud genereerimine:** LLM täiustab oma vastust baasil andmetel, mis päringuga on kaasatud. See võimaldab genereeritaval vastusel põhineda mitte ainult eelnevalt treenitud andmetel, vaid ka asjakohasel kontekstil. Päringutud andmeid kasutatakse LLM vastuste täiustamiseks. LLM tagastab siis vastuse kasutaja küsimusele.

![joonis, mis näitab RAG-i arhitektuuri](../../../translated_images/et/encoder-decode.f2658c25d0eadee2.webp)

RAG-i arhitektuur on rakendatud transformeritel, mis koosnevad kahest osast: kodeerija ja dekodeerija. Näiteks kui kasutaja esitab küsimuse, siis sisestekst kodeeritakse vektoriteks, mis haaravad sõnade tähendust, ning vektorid dekodeeritakse meie dokumendindeksisse ja genereeritakse uus tekst vastavalt kasutaja päringule. LLM kasutab nii kodeerija kui ka dekodeerijamudelit väljundi genereerimiseks.

Kaks lähenemist RAG-i rakendamisel vastavalt ettepanekule: [Taastepõhine täiendusgeneratsioon teadmusintensiivseteks NLP (loomuliku keele töötluse) ülesanneteks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) on:

- **_RAG-Sequence_** kasutab päringuga seotud dokumente parima võimalik vastuse ennustamiseks.

- **RAG-Token** kasutab dokumente järgmise märgi genereerimiseks ja pärib neid vastuseks kasutaja küsimusele.

### Miks kasutada RAG-e?

- **Info rikkus:** tagab, et tekstivastused on ajakohased ja värsked. See parandab tulemuslikkust domeenispetsiifilistes ülesannetes, pääsedes ligi sisemisele teadmistebaasile.

- Vähendab väljamõtlemist, kasutades **kontrollitavat infot** teadmistebaasist, et pakkuda konteksti kasutaja päringutele.

- On **kuluefektiivne**, kuna on majanduslikum võrreldes LLM-i peenhäälestamisega.

## Teadmistebaasi loomine

Meie rakendus põhineb meie isiklikel andmetel, st AI Algajate kursuse närvivõrkude materjalil.

### Vektandmebaasid

Vektandmebaas eristub traditsioonilistest andmebaasidest, kuna on eriline andmebaas sisendvektorite salvestamiseks, haldamiseks ja otsimiseks. See salvestab dokumentide numbrilisi esitlusi. Andmete numeriliseks embedeks muutmine aitab meie AI süsteemil neid paremini mõista ja töödelda.

Me salvestame oma sisendid vektandmebaasidesse, sest LLM-il on piiratud arv sisendesõnu (tokeneid). Kuna kogu embedimist ei saa LLM-ile korraga anda, peame need jagama väiksemateks osadeks ning kasutaja küsimuse korral tagastatakse kasutaja küsimusega kõige rohkem kattuvad sisendid koos päringuga. Osadeks jagamine vähendab ka tokengitteed LLM-is ja seeläbi kulusid.

Mõned populaarsed vektandmebaasid on Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant ja DeepLake. Azure Cosmos DB mudelit saab luua Azure CLI abil järgmise käsuga:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Tekstist sisenditeks (embedding)

Enne andmete salvestamist tuleb need teisendada sisendvektoriteks. Kui töötad suurte dokumentide või pikkade tekstidega, saad need jagada osadeks vastavalt ootuspäringutele. Osadeks jagamine toimub kas lause- või lõigutasemel. Kuna osa tähendus sõltub selle ümber olevatest sõnadest, võid lisada osi täiendavat konteksti, näiteks dokumendi pealkirja või teksti enne või pärast osa. Andmed saab jagada järgmiselt:

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

    # Kui viimane tükk ei saavutanud miinimum pikkust, lisa see siiski
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Pärast osadeks jagamist võime teksti embedida erinevate mudeleid kasutades. Mõned kasutatavad mudelid on word2vec, OpenAI ada-002, Azure Computer Vision ja paljud teised. Mudelit valides tuleb arvestada kasutatavat keelt, kodeeritava sisu tüüpi (tekst/pildid/heli), sisendi suurust ja sisendi väljundi pikkust.

Üks näide OpenAI `text-embedding-ada-002` mudeli kasutatud sisendtekstist on:
![sõna kass embedimine](../../../translated_images/et/cat.74cbd7946bc9ca38.webp)

## Päring ja vektorotsing

Kui kasutaja esitab küsimuse, teisendab päringu kodeerija selle vektoriks ja otsib meie dokumendiindeksist sobivaid vektoreid, mis on seotud sisendiga. Pärast seda teisendatakse nii sisendi- kui dokumendivektorid tekstiks ja saadetakse LLM-ile.

### Päring

Päringu käigus otsib süsteem kiiresti dokumente indeksist, mis vastavad otsingukriteeriumidele. Päringu eesmärk on saada dokumendid, mida kasutatakse konteksti pakkumiseks ja LLM andmetele mahamaaramiseks.

Otsingut andmebaasis saab teha mitmel moel, näiteks:

- **Märksõnaotsing** - kasutatud tekstiotsinguks.

- **Vektorotsing** - teisendab dokumendid tekstist vektoriteks sisendimudelite abil, võimaldades **semantilist otsingut** sõnade tähenduse põhjal. Päring tehakse dokumentide vastu, mille vektorid on kasutaja küsimusega kõige lähemal.

- **Hübriidotsing** - kombinatsioon märksõna- ja vektorotsingust.

Päringu väljakutseks on see, kui andmebaasis puudub sarnane vastus päringule, süsteem tagastab siis parima võimaliku info. Võid kasutada selliseid meetodeid nagu maksimaalse kauguse seadistamine asjakohasuse jaoks või kasutada hübriidotsingut, mis ühendab ära mõlemad otsinguviisid. Selles õppetükis kasutame hübriidotsingut, mis ühendab vektor- ja märksõnaotsingu. Andmed salvestame andmeraamatusse, kus veerud sisaldavad osi ja sisendeid.

### Vektorite sarnasuse leidmine

Päringu tegija otsib teadmistebaasist sisendeid, mis on omavahel lähedased, ehk lähimad naabrid, kuna tegemist on sarnaste tekstidega. Päringu korral tehakse kõigepealt sisendi embedimine ning seejärel leitakse sarnased sisendid. Sarnasust mõõdetakse tavaliselt kosinussarnasuse järgi, mis põhineb kahe vektori vahelisel nurgal.

Muude alternatiivsete mõõtmiste hulka kuuluvad eukleidiline kaugus, mis on kahe vektori lõpp-punktide sirgjooneline kaugus, ja punktkorrutis, mis mõõdab kahte vektorit vastavate elementide korrutiste summana.

### Otsinguindeks

Päringu tegemisel tuleb esmalt luua otsinguindeks teadmistebaasi jaoks. Indeks salvestab meie sisendid ja suudab kiiresti leida kõige sarnasemad osad isegi suure andmebaasi korral. Indeksi saab luua lokaalselt järgmise abil:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Loo otsinguindeks
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Indeksi pärimiseks võite kasutada meetodit kneighbors
distances, indices = nbrs.kneighbors(embeddings)
```

### Tulemite ümberjärjestamine (re-ranking)

Pärast päringut võid vajada tulemite sortimist olulisuse järgi. Ümberjärjestav LLM kasutab masinõpet, et parandada otsingutulemuste asjakohasust, korraldades need tähtsuse järgi. Azure AI Search puhul on ümberjärjestamine automaatne ja põhineb semantilisel ümberjärjestajal. Näide ümberjärjestusest lähimate naabrite abil:

```python
# Leia kõige sarnasemad dokumendid
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Trüki välja kõige sarnasemad dokumendid
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Kõik kokku panemine

Viimane samm on lisada meie LLM, et saada vastuseid, mis tuginevad meie andmetele. Seda saab teha järgmiselt:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Muuda küsimus päringu vektoriks
    query_vector = create_embeddings(user_input)

    # Leia kõige sarnasemad dokumendid
    distances, indices = nbrs.kneighbors([query_vector])

    # lisa dokumendid päringule, et pakkuda konteksti
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # ühenda ajalugu ja kasutaja sisend
    history.append(user_input)

    # loo sõnumi objekt
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # kasuta vastuste API-t, et genereerida vastus
    response = client.responses.create(
        model="gpt-5-mini",
        max_output_tokens=800,
        input=messages,
        store=False,
    )

    return response.output_text

chatbot(user_input)
```

## Rakenduse hindamine

### Hindamismõõdikud

- Vastuste kvaliteet: vastuste loomulik kõla, ladusus ja inimlikkus.

- Andmete mahamaaramine: hindamine, kas vastus pärineb antud dokumentidest.

- Asjakohasus: hindamine, kas vastus vastab ja on seotud esitatud küsimusega.

- Ladusus: kas vastus on grammatilises mõttes loogiline.

## RAG-i (Taastepõhine täiendusgeneratsioon) ja vektandmebaaside kasutusjuhtumid

On palju erinevaid kasutusjuhtumeid, kus funktsioonikutsed võivad sinu rakendust parandada, näiteks:

- Küsimuste ja vastuste süsteemid: ühendades oma ettevõtte andmed vestlusega, mida töötajad saavad kasutada küsimuste esitamiseks.

- Soovitussüsteemid: süsteemi loomine, mis leiab kõige sarnasemad väärtused, nt filmid, restoranid ja palju muud.

- Vestlusrobotite teenused: chatiajaloo salvestamine ja vestluse personaliseerimine kasutaja andmete põhjal.

- Pildituvastus vektorite embedimise põhjal, kasulik pildituvastuses ja anomaalia tuvastamisel.

## Kokkuvõte

Oleme käsitlenud RAG põhialuseid alates andmete lisamisest rakendusse, kasutaja päringust ja väljundist. RAG loomise lihtsustamiseks võid kasutada raamistikke nagu Semanti Kernel, Langchain või Autogen.

## Kodune ülesanne

Jätkamaks oma õppimist Taastepõhise täiendusgeneratsiooni (RAG) teemal, võid järgmise luua:

- Ehita rakendusele front-end raamistiku abil, mida eelistad.

- Kasuta raamistiku, kas LangChain või Semantic Kernel, ja loo ülesanne uuesti.

Palju õnne õppetüki läbimise puhul 👏.

## Õppimine ei peatu siin, jätka teekonda

Peale selle õppetüki lõpetamist vaata meie [Generatiivse AI õppe kollektsiooni](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), et jätkata oma generatiivse AI teadmiste täiendamist!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->