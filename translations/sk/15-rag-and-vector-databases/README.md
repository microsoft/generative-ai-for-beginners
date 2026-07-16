# Retrieval Augmented Generation (RAG) a vektorové databázy

[![Retrieval Augmented Generation (RAG) a vektorové databázy](../../../translated_images/sk/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

V lekcii vyhľadávacích aplikácií sme si stručne ukázali, ako integrovať vlastné dáta do veľkých jazykových modelov (LLM). V tejto lekcii sa podrobnejšie pozrieme na koncept ukotvenia vašich dát vo vašej LLM aplikácii, mechaniku procesu a metódy ukladania dát, vrátane embeddingov a textu.

> **Video čoskoro k dispozícii**

## Úvod

V tejto lekcii sa budeme venovať nasledovnému:

- Úvod do RAG, čo to je a prečo sa používa v AI (umelá inteligencia).

- Pochopenie, čo sú to vektorové databázy a vytvorenie jednej pre našu aplikáciu.

- Praktický príklad, ako integrovať RAG do aplikácie.

## Ciele učenia

Po absolvovaní tejto lekcie budete schopní:

- Vysvetliť význam RAG pri získavaní a spracovaní dát.

- Nastaviť RAG aplikáciu a zakotviť vaše dáta do LLM

- Efektívna integrácia RAG a vektorových databáz v LLM aplikáciách.

## Náš scenár: rozšírenie našich LLM o vlastné dáta

Pre túto lekciu chceme pridať vlastné poznámky do vzdelávacieho startupu, čo umožní chatbotovi získať viac informácií o rôznych témach. Používateľom to umožní lepšie sa učiť a porozumieť rôznym témam, čo im uľahčí prípravu na skúšky. Pre vytvorenie nášho scenára použijeme:

- `Azure OpenAI:` LLM, ktorý použijeme na vytvorenie nášho chatbota

- `Lekcia AI pre začiatočníkov o neurónových sieťach:` to budú dáta, na ktorých zakotvíme náš LLM

- `Azure AI Search` a `Azure Cosmos DB:` vektorová databáza na uloženie našich dát a vytvorenie vyhľadávacieho indexu

Používatelia budú môcť vytvárať cvičné kvízy zo svojich poznámok, opakovacie kartičky a zhrnúť ich do stručných prehľadov. Pre začiatok si pozrime, čo je RAG a ako funguje:

## Retrieval Augmented Generation (RAG)

Chatbot poháňaný LLM spracováva používateľské požiadavky na generovanie odpovedí. Je navrhnutý tak, aby bol interaktívny a komunikoval s používateľmi o širokej škále tém. Jeho odpovede sú však obmedzené kontextom, ktorý mu bol poskytnutý, a základnými trénovacími dátami. Napríklad vedomosti GPT-4 majú hranicu v septembri 2021, čo znamená, že postráda znalosti o udalostiach po tomto období. Navyše, dáta použité na trénovanie LLM nezahŕňajú dôverné informácie ako osobné poznámky alebo príručky spoločnosti.

### Ako fungujú RAG (Retrieval Augmented Generation)

![kresba zobrazujúca, ako fungujú RAG](../../../translated_images/sk/how-rag-works.f5d0ff63942bd3a6.webp)

Predstavme si, že chcete nasadiť chatbota, ktorý tvorí kvízy z vašich poznámok, budete potrebovať spojenie s databázou poznatkov. Tu prichádza na scénu RAG. RAG funguje nasledovne:

- **Databáza poznatkov:** Pred vyhľadávaním je potrebné dokumenty ingestovať a predspracovať, typicky rozložiť veľké dokumenty na menšie časti, transformovať ich do textového embeddingu a uložiť do databázy.

- **Používateľský dopyt:** používateľ položí otázku

- **Vyhľadávanie:** Keď používateľ položí otázku, model embeddingu vyhľadá relevantné informácie z databázy poznatkov, aby poskytol viac kontextu, ktorý bude zapracovaný do promptu.

- **Rozšírená generácia:** LLM vylepší svoju odpoveď na základe získaných dát. Umožňuje, aby odpoveď nebola založená len na predtrénovaných dátach, ale aj na relevantných informáciách z pridaného kontextu. Získané dáta sa používajú na rozšírenie odpovedí LLM. LLM následne vráti odpoveď na otázku používateľa.

![kresba zobrazujúca architektúru RAG](../../../translated_images/sk/encoder-decode.f2658c25d0eadee2.webp)

Architektúra RAG je implementovaná pomocou transformátorov pozostávajúcich z dvoch častí: enkodéra a dekodéra. Napríklad, keď používateľ položí otázku, vstupný text sa "enkóduje" do vektorov zachytávajúcich význam slov a vektory sa "dekódujú" do nášho dokumentového indexu a generujú nový text na základe používateľskej otázky. LLM používa model enkódér-dekódér na generovanie výstupu.

Podľa navrhovaného článku: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) sú dva prístupy implementácie RAG:

- **_RAG-Sequence_** používa získané dokumenty na predikciu najlepšej možnej odpovede na používateľský dopyt

- **RAG-Token** používa dokumenty na generovanie nasledujúceho tokenu, potom ich znovu vyhľadáva na odpoveď na otázku používateľa

### Prečo používať RAG?

- **Bohatosť informácií:** zabezpečuje, že textové odpovede sú aktuálne a súčasné. Tým zlepšuje výkon v špecifických doménach prístupom k internej databáze poznatkov.

- Znižuje tvorbu nepravdivých informácií využitím **verifikovateľných dát** v databáze poznatkov na poskytnutie kontextu používateľským dopytom.

- Je **nákladovo efektívny**, pretože je výhodnejší v porovnaní s doladením LLM

## Vytvorenie databázy poznatkov

Naša aplikácia je založená na našich osobných dátach, tj. lekcii o neurónových sieťach z kurzu AI pre začiatočníkov.

### Vektorové databázy

Vektorová databáza na rozdiel od tradičných databáz je špecializovaná databáza navrhnutá na ukladanie, správu a vyhľadávanie vložených vektorov. Ukladá číselné reprezentácie dokumentov. Rozdelením dát na číselné embeddingy sa nášmu AI systému uľahčí pochopenie a spracovanie dát.

Embeddingy ukladajúme do vektorových databáz, pretože LLM má limit počtu tokenov, ktoré ako vstup akceptuje. Keďže nemôžete poslať celé embeddingy do LLM, je potrebné ich rozdeliť na časti a keď používateľ položí otázku, vrátia sa embeddingy najviac relevantné k otázke spolu s promptom. Chunking tiež znižuje náklady na počet tokenov zaslaných cez LLM.

Medzi populárne vektorové databázy patria Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant a DeepLake. Môžete vytvoriť model Azure Cosmos DB pomocou Azure CLI nasledujúcim príkazom:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Od textu k embeddingom

Predtým, ako uložíme naše dáta, musíme ich konvertovať do vektorových embeddingov skôr, než ich uložíme do databázy. Ak pracujete s veľkými dokumentmi alebo dlhými textami, môžete ich rozdeliť podľa očakávaných dopytov. Chunkovať je možné na úrovni viet alebo odsekov. Keďže chunkovanie vyvodzuje význam zo slov v okolí, môžete pridať ďalší kontext do chunku, napríklad pridaním nadpisu dokumentu alebo zaradením textu pred alebo za chunk. Dáta môžete chunkovať takto:

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

    # Ak posledný blok nedosiahol minimálnu dĺžku, pridaj ho napriek tomu
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Po rozdelení môžeme potom vložiť náš text pomocou rôznych embedding modelov. Niektoré modely, ktoré môžete použiť, sú: word2vec, ada-002 od OpenAI, Azure Computer Vision a mnoho ďalších. Výber modelu závisí od jazykov, ktoré používate, od typu obsahu kódovaného (text/obrázky/audio), veľkosti vstupu, ktorý dokáže kódovať a dĺžky výstupu embeddingu.

Príklad embeddingu textu pomocou modelu OpenAI `text-embedding-ada-002` je:
![embedding slova mačka](../../../translated_images/sk/cat.74cbd7946bc9ca38.webp)

## Vyhľadávanie a vektorové hľadanie

Keď používateľ položí otázku, vyhľadávač ju premení na vektor pomocou query enkodéra, potom prehľadá náš index dokumentov pre relevantné vektory v dokumente, ktoré súvisia s vstupom. Po nájdení ich konvertuje na text a posiela do LLM.

### Vyhľadávanie

Vyhľadávanie nastáva, keď sa systém snaží rýchlo nájsť dokumenty z indexu, ktoré vyhovujú kritériám vyhľadávania. Cieľom vyhľadávača je získať dokumenty, ktoré budú slúžiť na poskytnutie kontextu a ukotvenie LLM na vaše dáta.

Existuje niekoľko spôsobov, ako vyhľadávať v našej databáze, napríklad:

- **Vyhľadávanie podľa kľúčových slov** - používané pre textové vyhľadávania

- **Vektorové vyhľadávanie** - prevádza dokumenty z textu do vektorových reprezentácií pomocou embedding modelov, čo umožňuje **sémantické vyhľadávanie** pomocou významu slov. Vyhľadávanie prebieha dotazovaním dokumentov, ktorých vektorové reprezentácie sú najbližšie k otázke používateľa.

- **Hybridné** - kombinácia vyhľadávania podľa kľúčových slov a vektorového vyhľadávania.

Výzvou pri vyhľadávaní je situácia, keď v databáze nie je podobná odpoveď na dopyt, systém potom vráti najlepšie dostupné informácie, no môžete použiť taktiky ako nastavenie maximálnej vzdialenosti pre relevantnosť alebo použiť hybridné vyhľadávanie kombinujúce kľúčové slová a vektory. V tejto lekcii použijeme hybridné vyhľadávanie, teda kombináciu vektorového a kľúčového vyhľadávania. Dáta uložíme do dataframe s stĺpcami obsahujúcimi chunky a embeddingy.

### Vektorová podobnosť

Vyhľadávač bude hľadať v databáze poznatkov embeddingy, ktoré sú navzájom blízko, najbližší sused, keďže ide o podobné texty. V scenári, keď používateľ položí otázku, tá najprv bude vložená do embeddingu a následne sa porovná s podobnými embeddingami. Bežným meradlom na určenie podobnosti vektorov je kosínusová podobnosť, založená na uhle medzi dvoma vektormi.

Môžeme merať podobnosť aj inými alternatívami, ako sú Eukleidovská vzdialenosť, čo je priamka medzi koncovými bodmi vektorov, a skalárny súčin, ktorý meria súčet súčinov zodpovedajúcich sa elementov dvoch vektorov.

### Index vyhľadávania

Pri vyhľadávaní musíme pred vyhľadávaním vybudovať index pre našu databázu poznatkov. Index bude uchovávať naše embeddingy a môže rýchlo vyhľadať najpodobnejšie chunky aj vo veľkej databáze. Index si môžeme vytvoriť lokálne pomocou:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Vytvorte vyhľadávací index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Na dotazovanie indexu môžete použiť metódu kneighbors
distances, indices = nbrs.kneighbors(embeddings)
```

### Pretriedenie výsledkov

Po vykonaní vyhľadávania môže byť potrebné zoradiť výsledky od najrelevantnejších. Pretriediace LLM využíva strojové učenie na zvýšenie relevantnosti výsledkov usporiadaním od najrelevantnejších. Pri použití Azure AI Search je pretriedenie automatické pomocou sémantického pretriediaceho modulu. Príklad fungovania pretriedenia pomocou najbližších susedov:

```python
# Nájsť najpodobnejšie dokumenty
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Vytlačiť najpodobnejšie dokumenty
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Zhrnutie všetkého

Posledným krokom je pridať náš LLM do procesu, aby sme mohli získavať odpovede ukotvené na našich dátach. Môžeme ho implementovať nasledovne:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Preveďte otázku na vektor dotazu
    query_vector = create_embeddings(user_input)

    # Nájdite najpodobnejšie dokumenty
    distances, indices = nbrs.kneighbors([query_vector])

    # pridajte dokumenty k dotazu na poskytnutie kontextu
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # skombinujte históriu a vstup používateľa
    history.append(user_input)

    # vytvorte objekt správy
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # použite API odpovedí na vygenerovanie odpovede
    response = client.responses.create(
        model="gpt-5-mini",
        max_output_tokens=800,
        input=messages,
        store=False,
    )

    return response.output_text

chatbot(user_input)
```

## Hodnotenie našej aplikácie

### Metódy hodnotenia

- Kvalita dodaných odpovedí, aby zneli prirodzene, plynule a ľudsky

- Ukotvenie dát: hodnotenie, či odpoveď vyšla zo dodaných dokumentov

- Relevantnosť: hodnotenie, či odpoveď zodpovedá a súvisí s položenou otázkou

- Plynulosť - či odpoveď dáva gramaticky zmysel

## Príklady využitia RAG (Retrieval Augmented Generation) a vektorových databáz

Existuje mnoho rôznych prípadov použitia, kde funkčné volania môžu zlepšiť vašu aplikáciu, napríklad:

- Otázky a odpovede: ukotvuje dáta vašej spoločnosti do chatbota, ktorý môžu používať zamestnanci na kladenie otázok.

- Odporúčacie systémy: kde môžete vytvoriť systém vyhľadávajúci najpodobnejšie hodnoty, napr. filmy, reštaurácie a mnoho ďalších.

- Chatbot služby: môžete ukladať históriu chatu a personalizovať konverzáciu na základe dát používateľa.

- Vyhľadávanie obrázkov na základe vektorových embeddingov, užitočné pri rozpoznávaní obrázkov a detekcii anomálií.

## Zhrnutie

Prebrali sme základné oblasti RAG od pridania našich dát do aplikácie, cez používateľský dopyt až po výstup. Na zjednodušenie vytvorenia RAG môžete použiť rámce ako Semantic Kernel, Langchain alebo Autogen.

## Zadanie

Pre pokračovanie vo vašom učení Retrieval Augmented Generation (RAG) môžete vytvoriť:

- Vytvorte front-end aplikácie pomocou rámca podľa vášho výberu

- Využite rámec, či už LangChain alebo Semantic Kernel, a znovu vytvorte vašu aplikáciu.

Blahoželáme k dokončeniu lekcie 👏.

## Učenie sa tu nekončí, pokračujte na ďalšej ceste

Po absolvovaní tejto lekcie si pozrite našu [kolekciu pre Generatívnu AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste naďalej zvyšovali svoje znalosti v oblasti Generatívnej AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->