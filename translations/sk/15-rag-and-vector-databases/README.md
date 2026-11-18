# Retrieval Augmented Generation (RAG) a vektorové databázy

[![Retrieval Augmented Generation (RAG) a vektorové databázy](../../../translated_images/sk/15-lesson-banner.ac49e59506175d4f.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

V lekcii o vyhľadávacích aplikáciách sme sa stručne naučili, ako integrovať vlastné dáta do veľkých jazykových modelov (LLM). V tejto lekcii sa bližšie pozrieme na koncept základania vašich dát v aplikácii LLM, mechaniku procesu a metódy ukladania dát, vrátane vektorových reprezentácií a textu.

> **Video čoskoro k dispozícii**

## Úvod

V tejto lekcii sa budeme venovať nasledujúcemu:

- Úvode do RAG, čo to je a prečo sa používa v AI (umelej inteligencii).

- Pochopeniu, čo sú vektorové databázy a vytvoreniu jednej pre našu aplikáciu.

- Praktickému príkladu, ako integrovať RAG do aplikácie.

## Ciele učenia

Po dokončení tejto lekcie budete schopní:

- Vysvetliť význam RAG v získavaní a spracovaní dát.

- Nastaviť RAG aplikáciu a zakotviť LLM pomocou vašich dát.

- Efektívne integrovať RAG a vektorové databázy v LLM aplikáciách.

## Náš scenár: vylepšenie našich LLM pomocou vlastných dát

Pre túto lekciu chceme pridať vlastné poznámky do vzdelávacieho startupu, čo umožní chatbotovi získať viac informácií o rôznych predmetoch. Použitím našich poznámok budú študenti schopní lepšie študovať a pochopiť rôzne témy, čím sa im uľahčí príprava na skúšky. Na vytvorenie nášho scenára použijeme:

- `Azure OpenAI:` LLM, ktorý použijeme na vytvorenie nášho chatbota

- `AI for beginners' lesson on Neural Networks`: toto budú dáta, na ktorých zakotvíme náš LLM

- `Azure AI Search` a `Azure Cosmos DB:` vektorovú databázu na uloženie našich dát a vytvorenie vyhľadávacieho indexu

Používatelia budú môcť vytvárať cvičné kvízy a kartičky na opakovanie zo svojich poznámok a zhrnúť tieto poznámky do stručných prehľadov. Poďme najskôr pozrieť, čo je RAG a ako funguje:

## Retrieval Augmented Generation (RAG)

Chatbot poháňaný LLM spracúva používateľské dotazy na generovanie odpovedí. Je navrhnutý tak, aby bol interaktívny a komunikoval s používateľmi na širokú škálu tém. Jeho odpovede sú však obmedzené na kontext, ktorý mu bol poskytnutý, a na základné tréningové dáta. Napríklad, znalosti GPT-4 sú obmedzené k septembru 2021, čo znamená, že nepozná udalosti po tomto dátume. Okrem toho dáta použité na tréning LLM nezahŕňajú dôverné informácie, ako sú osobné poznámky alebo firemný príručný manuál.

### Ako fungujú RAG (Retrieval Augmented Generation)

![diagram ukazujúci, ako fungujú RAG](../../../translated_images/sk/how-rag-works.f5d0ff63942bd3a6.webp?WT.mc_id=academic-105485-koreyst)

Predstavte si, že chcete nasadiť chatbota, ktorý tvorí kvízy zo svojich poznámok; potrebujete pripojenie k databáze znalostí. Tu prichádza na pomoc RAG. RAG funguje nasledovne:

- **Databáza znalostí:** Pred vyhľadávaním je potrebné tieto dokumenty spracovať a predbežne pripraviť, zvyčajne rozdelením veľkých dokumentov na menšie časti, premenou na textové vektorové reprezentácie a uložením do databázy.

- **Používateľský dotaz:** používateľ položí otázku.

- **Vyhľadávanie:** Keď používateľ položí otázku, embedding model vyhľadá relevantné informácie v databáze znalostí, ktoré poskytnú viac kontextu, ktorý bude začlenený do promptu.

- **Rozšírená generácia:** LLM vylepšuje svoju odpoveď na základe získaných dát. Umožňuje, aby odpoveď bola založená nielen na predtrénovaných dátach, ale aj na relevantných informáciách z pridaného kontextu. Vráti odpoveď na otázku používateľa.

![Diagram zobrazujúci architektúru RAG](../../../translated_images/sk/encoder-decode.f2658c25d0eadee2.webp?WT.mc_id=academic-105485-koreyst)

RAG kombinuje vyhľadávač (retriever) a generátor: dotaz sa prevedie na vektor, porovná sa s indexom dokumentov, aby sa našli relevantné textové časti, ktoré sa poskytnú ako kontext LLM, ktorý vytvorí odpoveď. Vyhľadávač a generátor môžu používať rôzne modely; RAG nevyžaduje encoder-decoder transformer.

Dva prístupy k implementácii RAG podľa navrhovaného článku: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) sú:

- **_RAG-Sequence_** využíva vyhľadané dokumenty na predpovedanie najlepšej odpovede na používateľský dotaz.

- **RAG-Token** používa dokumenty na generovanie ďalšieho tokenu, potom ich vyhľadáva pre odpoveď na dotaz používateľa.

### Prečo používať RAG? 

- **Bohatosť informácií:** zabezpečuje, že textové odpovede sú aktuálne a aktuálne. Tým zlepšuje výkon na úlohách špecifických pre doménu prístupom k vnútornej databáze znalostí.

- Znižuje vymýšľanie odpovedí využitím **overiteľných dát** v databáze znalostí ako kontext k otázkam používateľov.

- Je **nákladovo efektívny**, pretože je lacnejší v porovnaní s dolaďovaním LLM.

## Vytvorenie databázy znalostí

Naša aplikácia je založená na osobných dátach, konkrétne na lekcii o neurónových sieťach z kurikula AI pre začiatočníkov.

### Vektorové databázy

Vektorová databáza, na rozdiel od tradičných databáz, je špecializovaná databáza na ukladanie, správu a vyhľadávanie vložených vektorov. Ukladá číselné reprezentácie dokumentov. Rozkladanie dát na číselné reprezentácie uľahčuje nášmu AI systému pochopenie a spracovanie dát.

Pretože LLM majú limit na počet vstupných tokenov, dokumenty rozdeľujeme na časti pred ich embeddingom. Keď používateľ položí otázku, embeddingy najpodobnejšie dotazu identifikujú relevantné textové časti, ktoré sa vrátia spolu s promptom. Chunkovanie tiež znižuje počet tokenov predaných LLM a teda môže znižovať náklady.

Niektoré populárne vektorové databázy sú Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant a DeepLake. Môžete vytvoriť model Azure Cosmos DB pomocou Azure CLI s nasledujúcim príkazom:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Od textu k embeddingom

Pred uložením dát ich treba previesť na vektorové embeddingy. Ak pracujete s veľkými dokumentmi alebo dlhými textami, môžete ich rozdeliť podľa očakávaných dotazov. Chunkovanie môže byť na úrovni viet alebo odsekov. Keďže význam časti vyplýva zo slov okolo nej, môžete pridať ďalší kontext napríklad názov dokumentu alebo nejaký text pred alebo po danej časti. Dáta môžete členiť takto:

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

Po rozdelení môžeme text vložiť pomocou rôznych modelov embeddingu. Niektoré modely sú word2vec, ada-002 od OpenAI, Azure Computer Vision a mnohé ďalšie. Výber modelu závisí od používaných jazykov, typu kódovaného obsahu (text/obrázky/audio), veľkosti vstupu a dĺžky výstupu embeddingu.

Príklad embedded textu pomocou modelu `text-embedding-ada-002` od OpenAI je:
![embedding slova mačka](../../../translated_images/sk/cat.74cbd7946bc9ca38.webp?WT.mc_id=academic-105485-koreyst)

## Vyhľadávanie a vektorové vyhľadávanie

Keď používateľ položí otázku, vyhľadávač ju premení na vektor pomocou query encoderu a potom vyhľadá v indexe dokumentov relevantné vektory súvisiace s dotazom. Po nájdení konvertuje vstupný vektor a vektory dokumentov späť na text a pošle ich do LLM.

### Vyhľadávanie

Vyhľadávanie nastáva, keď systém rýchlo hľadá dokumenty v indexe spĺňajúce kritériá vyhľadávania. Cieľom vyhľadávača je získať dokumenty, ktoré poskytnú kontext a zakotvia LLM vo vašich dátach.

Existuje niekoľko spôsobov, ako vyhľadávať v našej databáze, napríklad:

- **Vyhľadávanie podľa kľúčových slov** - používa sa pre textové vyhľadávanie

- **Vektorové vyhľadávanie** - konvertuje dokumenty z textu na vektorové reprezentácie pomocou embedding modelov, čo umožňuje **sémantické vyhľadávanie** podľa významu slov. Vyhľadávanie prebieha tak, že sa hľadajú dokumenty s najbližšími vektorovými reprezentáciami k používateľskej otázke.

- **Hybridné** - kombinácia vyhľadávania podľa kľúčových slov a vektorov.

Výzvou pri vyhľadávaní je, keď v databáze neexistuje podobná odpoveď na dotaz, systém vráti najlepšie dostupné informácie. Môžete však použiť taktiky ako nastavenie maximálnej vzdialenosti pre relevantnosť alebo hybridné vyhľadávanie. V tejto lekcii použijeme hybridné vyhľadávanie s kombináciou vektorového a kľúčového vyhľadávania. Dáta uložíme do dátového rámca (dataframe) so stĺpcami obsahujúcimi časti textu aj embeddingy.

### Vektorová podobnosť

Vyhľadávač bude prehľadávať databázu znalostí a hľadať embeddingy, ktoré sú spolu blízko — najbližších susedov — pretože predstavujú podobné texty. Keď používateľ zadá dotaz, ten sa najskôr embeduje a potom sa zhoduje s podobnými embeddingami. Najčastejšie používaným meradlom podobnosti vektorov je kosínusová podobnosť, založená na uhle medzi dvoma vektormi.

Iné metriky na meranie podobnosti sú napríklad euklidovská vzdialenosť - priama línia medzi koncovými bodmi vektorov, a skalárny súčin (dot product), ktorý meria súčet súčinu zodpovedajúcich prvkov v dvoch vektoroch.

### Index pre vyhľadávanie

Pred vykonaním vyhľadávania potrebujeme vytvoriť index pre našu databázu znalostí. Index uloží naše embeddingy a rýchlo vyhľadá najpodobnejšie časti textu aj vo veľkej databáze. Index môžeme vytvoriť lokálne pomocou:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Pretriedenie výsledkov (Re-ranking)

Po vyhľadaní v databáze možno budete chcieť zoradiť výsledky podľa relevantnosti od najrelevantnejších. Pretriedenie LLM využíva strojové učenie na zlepšenie relevantnosti výsledkov zoradením od najpodstatnejších. Pri Azure AI Search sa pretriedenie vykonáva automaticky pomocou sémantického pretriediaceho mechanizmu. Príklad, ako pretriedenie funguje pomocou najbližších susedov:

```python
# Find the most similar documents
distances, indices = nbrs.kneighbors([query_vector])

# Print the three most similar documents with their distance to the question
for distance, index in zip(distances[0][:3], indices[0][:3]):
    print(flattened_df['chunks'].iloc[index])
    print(flattened_df['path'].iloc[index])
    print(distance)
```

## Spojenie všetkého dohromady

Posledným krokom je pridanie nášho LLM do procesu, aby sme získali odpovede založené na našich dátach. Môžeme ho implementovať nasledovne:

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

## Hodnotenie našej aplikácie

### Hodnotiace metriky

- Kvalita odpovedí, zabezpečujúca, že znejú prirodzene, plynulo a ľudsky.

- Zakotvenosť dát: hodnotenie, či odpoveď pochádza zo zaslaných dokumentov.

- Relevantnosť: hodnotenie, či odpoveď súvisí a zodpovedá otázke.

- Plynulosť: či odpoveď dáva gramaticky zmysel.

## Použitie RAG (Retrieval Augmented Generation) a vektorových databáz

Existuje mnoho prípadov použitia, kde RAG môže zlepšiť vašu aplikáciu, napríklad:

- Otázky a odpovede: zakotvenie firemných dát do chatu, ktorý môžu používatelia používať na kladenie otázok.

- Odporúčacie systémy: vytvorenie systému, ktorý zhromažďuje najpodobnejšie hodnoty, napríklad filmy, reštaurácie a iné.

- Chatbotové služby: uloženie histórie chatov a personalizácia rozhovoru na základe používateľských dát.

- Vyhľadávanie obrázkov na základe vektorových embeddingov, užitočné pri rozpoznávaní obrázkov a detekcii anomálií.

## Zhrnutie

Prešli sme základné oblasti RAG od pridávania dát do aplikácie po používateľský dotaz a výstup. Na zjednodušenie tvorby RAG môžete použiť rámce ako Semantic Kernel, LangChain alebo AutoGen.

## Zadanie

Na pokračovanie učenia Retrieval Augmented Generation (RAG) môžete vybudovať:

- Front-end pre aplikáciu pomocou vami zvoleného rámca

- Vyžiť rámec, buď LangChain alebo Semantic Kernel, a znovu vytvoriť vašu aplikáciu.

Gratulujeme k dokončeniu lekcie 👏.

## Učenie nekončí, pokračujte v ceste

Po dokončení tejto lekcie si pozrite našu [kolekciu učenia Generatívnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) a pokračujte vo zvyšovaní vašich znalostí Generatívnej AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->