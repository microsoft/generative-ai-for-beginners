<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2210a0466c812d9defc4df2d9a709ff9",
  "translation_date": "2026-01-18T19:02:22+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "sk"
}
-->
# Retrieval Augmented Generation (RAG) a vektorové databázy

[![Retrieval Augmented Generation (RAG) and Vector Databases](../../../../../translated_images/sk/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

V lekcii o vyhľadávacích aplikáciách sme stručne spoznali, ako integrovať vlastné dáta do veľkých jazykových modelov (LLM). V tejto lekcii sa podrobnejšie pozrieme na koncepty zakladajúce vaše dáta vo vašej LLM aplikácii, mechanizmus tohto procesu a metódy ukladania dát, vrátane vektorových reprezentácií aj textu.

> **Video čoskoro**

## Úvod

V tejto lekcii pokryjeme nasledovné:

- Úvod do RAG, čo to je a prečo sa používa v umelej inteligencii (AI).

- Pochopenie, čo sú to vektorové databázy a vytvorenie jednej pre našu aplikáciu.

- Praktický príklad, ako integrovať RAG do aplikácie.

## Ciele učenia

Po absolvovaní tejto lekcie budete schopní:

- Vysvetliť význam RAG v získavaní a spracovaní dát.

- Nastaviť RAG aplikáciu a zakladať svoje dáta do LLM.

- Efektívne integrovať RAG a vektorové databázy v LLM aplikáciách.

## Náš scenár: vylepšenie našich LLM vlastnými dátami

Pre túto lekciu chceme pridať svoje vlastné poznámky do vzdelávacieho startupu, čo umožní chatbotovi získať viac informácií o rôznych témach. Použitím poznámok, ktoré máme, budú študenti schopní lepšie študovať a porozumieť rôznym témam, čo im uľahčí prípravu na skúšky. Pre vytvorenie nášho scenára použijeme:

- `Azure OpenAI:` LLM, ktorý použijeme na vytvorenie nášho chatbota

- `Lekcia AI pre začiatočníkov o neurónových sieťach`: to budú dáta, na ktorých zakladáme náš LLM

- `Azure AI Search` a `Azure Cosmos DB:` vektorová databáza na uloženie našich dát a vytvorenie vyhľadávacieho indexu

Používatelia budú môcť vytvárať cvičné kvízy z ich poznámok, opakovacie kartičky a zhrnúť ich do stručných prehľadov. Aby sme začali, pozrime sa, čo je RAG a ako funguje:

## Retrieval Augmented Generation (RAG)

Chatbot založený na LLM spracuje používateľské požiadavky na generovanie odpovedí. Je navrhnutý byť interaktívny a komunikovať s používateľmi na rôzne témy. Jeho odpovede sú však limitované kontextom, ktorý má k dispozícii, a základnými trénovacími dátami. Napríklad, dátum ukončenia znalostí GPT-4 je september 2021, čo znamená, že nevie o udalostiach po tomto dátume. Okrem toho dáta použité na trénovanie LLM nezahŕňajú dôverné informácie, ako sú osobné poznámky alebo príručky produktov spoločnosti.

### Ako fungujú RAG (Retrieval Augmented Generation)

![drawing showing how RAGs work](../../../../../translated_images/sk/how-rag-works.f5d0ff63942bd3a6.webp)

Povedzme, že chcete nasadiť chatbota, ktorý vytvára kvízy z vašich poznámok, budete potrebovať pripojenie k databáze znalostí. Tu prichádza RAG na pomoc. RAG funguje nasledovne:

- **Databáza znalostí:** Pred samotným vyhľadávaním musia byť dokumenty ingestované a predspracované, zvyčajne rozdelením veľkých dokumentov na menšie časti, transformáciou na textové embeddingy a uložením do databázy.

- **Používateľský dopyt:** používateľ položí otázku

- **Vyhľadávanie:** Keď používateľ položí otázku, model embeddingu vyhľadá relevantné informácie z databázy znalostí, aby poskytol viac kontextu, ktorý sa zapracuje do promptu.

- **Aumentovaná generácia:** LLM vylepší svoju odpoveď na základe získaných dát. Umožní, aby odpoveď nebola založená len na predtrénovaných dátach, ale aj na relevantných informáciách z pridaného kontextu. Získané dáta sa použijú na zvýšenie kvality odpovedí LLM. Potom LLM vráti odpoveď na používateľovu otázku.

![drawing showing how RAGs architecture](../../../../../translated_images/sk/encoder-decode.f2658c25d0eadee2.webp)

Architektúra RAG sa implementuje pomocou transformerov pozostávajúcich z dvoch častí: enkodéra a dekodéra. Napríklad, keď používateľ položí otázku, vstupný text sa “enkóduje” do vektorov zachytávajúcich význam slov a tieto vektory sa potom “dekódujú” do nášho indexu dokumentov a generuje sa nový text založený na používateľskom dopyte. LLM používa model enkodér-dekodér na generovanie výstupu.

Dva prístupy pri implementácii RAG podľa navrhovaného článku: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) sú:

- **_RAG-Sequence_** využíva vyhľadané dokumenty na predpovedanie najlepšej možnej odpovede na používateľov dopyt

- **RAG-Token** používa dokumenty na generovanie ďalšieho tokenu, potom ich vyhľadáva, aby odpovedal na otázku používateľa

### Prečo používať RAG? 

- **Bohatosť informácií:** zabezpečuje, že textové odpovede sú aktuálne a správne. Tým zvýši výkon v úlohách špecifických pre danú oblasť tým, že pristupuje k internej databáze znalostí.

- Znižuje vymýšľanie odpovedí využitím **overiteľných dát** v databáze znalostí na poskytnutie kontextu ku otázkam používateľa.

- Je **nákladovo efektívny**, pretože je ekonomickejší v porovnaní s dolaďovaním (fine-tuningom) LLM.

## Vytvorenie databázy znalostí

Naša aplikácia je založená na našich osobných dátach, teda lekcii o neurónových sieťach z kurikula AI pre začiatočníkov.

### Vektorové databázy

Vektorová databáza, na rozdiel od tradičných databáz, je špecializovaná databáza navrhnutá na ukladanie, správu a vyhľadávanie vložených vektorov. Ukladá číselné reprezentácie dokumentov. Prevádzanie dát na číselné embeddingy uľahčuje nášmu AI systému pochopenie a spracovanie dát.

Ukladáme naše embeddingy do vektorových databáz, pretože LLM majú limit na počet tokenov, ktoré prijímajú ako vstup. Keďže nemôžete odovzdať celé embeddingy do LLM, je potrebné ich rozdeliť na časti a keď používateľ položí otázku, vrátia sa embeddingy, ktoré sú k nej najbližšie spolu s promptom. Chunkovanie tiež znižuje náklady na počet tokenov prechádzajúcich LLM.

Niektoré populárne vektorové databázy zahŕňajú Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant a DeepLake. Môžete vytvoriť model Azure Cosmos DB pomocou Azure CLI s nasledujúcim príkazom:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Od textu k embeddingom

Pred uložením dát musíme konvertovať text na vektorové embeddingy. Ak pracujete s veľkými dokumentmi alebo dlhými textami, môžete ich rozdeliť na časti podľa očakávaných otázok. Chunkovanie môže byť na úrovni viet alebo odstavcov. Pretože chunkovanie vyvodzuje významy zo slov v okolí, môžete ku chunkom pridať aj ďalší kontext, napríklad názov dokumentu alebo text pred a po chunke. Dáta môžete rozdeliť nasledovne:

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

    # Ak posledný blok nedosiahol minimálnu dĺžku, pridajte ho aj tak
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Keď sú dáta rozdelené, môžeme ich vložiť do embeddingov pomocou rôznych modelov. Niektoré modely, ktoré môžete použiť, sú: word2vec, ada-002 od OpenAI, Azure Computer Vision a ďalšie. Výber modelu závisí od používaných jazykov, typu kódovaného obsahu (text/obrázky/audio), veľkosti vstupu a dĺžky výstupného embeddingu.

Príklad vloženého textu pomocou modelu `text-embedding-ada-002` od OpenAI je:
![an embedding of the word cat](../../../../../translated_images/sk/cat.74cbd7946bc9ca38.webp)

## Vyhľadávanie a vektorové vyhľadávanie

Keď používateľ položí otázku, vyhľadávač ju premení na vektor pomocou enkodéra dotazu, potom prehľadá náš index dokumentov pre relevantné vektory, ktoré súvisia s daným vstupom. Po dokončení konvertuje vstupný vektor a vektory dokumentov späť do textu a odovzdá ich LLM.

### Vyhľadávanie

Vyhľadávanie nastáva, keď systém rýchlo vyhľadá dokumenty v indexe, ktoré spĺňajú kritériá hľadania. Cieľom vyhľadávača je získať dokumenty, ktoré poskytnú kontext a zakotvia LLM vo vašich dátach.

Existuje niekoľko spôsobov, ako vykonať vyhľadávanie v databáze, napríklad:

- **Vyhľadávanie podľa kľúčových slov** - používa sa na textové vyhľadávanie

- **Vektorové vyhľadávanie** - prevádza dokumenty z textu na vektorové reprezentácie pomocou embedding modelov, čo umožňuje **sémantické vyhľadávanie** na základe významu slov. Vyhľadávanie sa uskutoční vyhľadávaním dokumentov, ktorých vektorové reprezentácie sú najbližšie k otázke používateľa.

- **Hybridné** - kombinácia kľúčových slov a vektorového vyhľadávania.

Problém s vyhľadávaním vzniká, keď v databáze nie je odpoveď podobná dopytu, systém potom vráti najlepšie dostupné informácie, no môžete použiť taktiky ako nastavenie maximálnej vzdialenosti pre relevantnosť alebo použiť hybridné vyhľadávanie, ktoré kombinuje kľúčové slová a vektorové vyhľadávanie. V tejto lekcii použijeme hybridné vyhľadávanie, teda kombináciu vektorového a kľúčového slovného vyhľadávania. Dáta budeme ukladať do dátového rámca so stĺpcami obsahujúcimi chunky aj embeddingy.

### Vektorová podobnosť

Vyhľadávač prehľadá databázu znalostí pre embeddingy, ktoré sú k sebe navzájom blízko, teda najbližší susedia, pretože ide o podobné texty. V scenári, keď používateľ položí dopyt, ten sa najskôr premení na embedding a potom sa porovná s podobnými embeddingami. Bežná metrika používaná na zistenie podobnosti vektorov je kosínusová podobnosť, ktorá sa zakladá na uhle medzi dvoma vektormi.

Podobnosť môžeme merať aj inými metódami, napríklad Euklidovskou vzdialenosťou, ktorá meria priamu líniu medzi koncovými bodmi vektorov, alebo skalárnym súčinom, ktorý meria súčet súčinov zodpovedajúcich prvkov dvoch vektorov.

### Vyhľadávací index

Pred vykonaním vyhľadávania musíme vytvoriť vyhľadávací index pre našu databázu znalostí. Index ukladá naše embeddingy a umožňuje rýchlo nájsť najpodobnejšie chunky aj vo veľkej databáze. Index môžeme lokálne vytvoriť pomocou:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Vytvorte vyhľadávací index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Na dotazovanie indexu môžete použiť metódu kneighbors
distances, indices = nbrs.kneighbors(embeddings)
```

### Pretriesenie (re-ranking)

Keď už máte dotaz do databázy, možno budete chcieť výsledky zoradiť od najrelevantnejších po menej relevantné. Pretriesiaci LLM využíva strojové učenie na zlepšenie relevance výsledkov tým, že ich zoradí od najrelevantnejších. Pomocou Azure AI Search sa pretriesenie vykonáva automaticky pomocou sémantického pretriesiavača. Príklad, ako funguje pretriesenie s použitím najbližších susedov:

```python
# Nájdite najpodobnejšie dokumenty
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Vytlačte najpodobnejšie dokumenty
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Zhrnutie dohromady

Posledným krokom je pridať náš LLM do celku, aby sme mohli získať odpovede zakotvené v našich dátach. Implementujeme to takto:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Konvertujte otázku na dotazový vektor
    query_vector = create_embeddings(user_input)

    # Nájdite najpodobnejšie dokumenty
    distances, indices = nbrs.kneighbors([query_vector])

    # pridajte dokumenty k dotazu pre poskytnutie kontextu
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

    # použite chatové dokončenie na generovanie odpovede
    response = openai.chat.completions.create(
        model="gpt-4",
        temperature=0.7,
        max_tokens=800,
        messages=messages
    )

    return response.choices[0].message

chatbot(user_input)
```

## Hodnotenie našej aplikácie

### Metriky hodnotenia

- Kvalita poskytnutých odpovedí, aby zneli prirodzene, plynulo a ľudsky

- Zakorenenosť dát: hodnotenie, či odpoveď vychádza zo zdrojových dokumentov

- Relevantnosť: hodnotenie, či odpoveď zodpovedá a súvisí s položenou otázkou

- Plynulosť – či odpoveď zodpovedá gramatike

## Príklady použitia RAG (Retrieval Augmented Generation) a vektorových databáz

Existuje mnoho rôznych prípadov použitia, kde funkcia volaní môže zlepšiť vašu aplikáciu, napríklad:

- Otázky a odpovede: zakoreníte firemné dáta do chatu, ktorý môžu používať zamestnanci na kladenie otázok.

- Odporúčacie systémy: kde môžete vytvoriť systém, ktorý zodpovedá najpodobnejším hodnotám, napríklad filmy, reštaurácie a mnoho ďalších.

- Chatbot služby: môžete ukladať históriu chatu a personalizovať konverzáciu na základe používateľských dát.

- Vyhľadávanie obrázkov na základe vektorových embeddingov, užitočné pri rozpoznávaní obrázkov a detekcii anomálií.

## Zhrnutie

Prešli sme základné oblasti RAG od pridávania našich dát do aplikácie, používateľského dopytu až po výstup. Pre zjednodušenie tvorby RAG môžete použiť rámce ako Semantic Kernel, Langchain alebo Autogen.

## Zadanie

Pre pokračovanie vo vašom štúdiu Retrieval Augmented Generation (RAG) môžete vytvoriť:

- Vytvorte front-end pre aplikáciu pomocou frameworku podľa vášho výberu

- Využite framework, buď LangChain alebo Semantic Kernel, a zrekonštruujte svoju aplikáciu.

Gratulujeme k absolvovaniu lekcie 👏.

## Učenie nekončí tu, pokračujte v Ceste

Po dokončení tejto lekcie si pozrite našu [kolekciu Generatívneho AI učenia](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste pokračovali vo zdokonaľovaní svojich znalostí o generatívnej AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, vezmite prosím na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->