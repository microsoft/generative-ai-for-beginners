<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4b0266fbadbba7ded891b6485adc66d",
  "translation_date": "2025-10-17T21:56:15+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "sk"
}
-->
# Generovanie s rozšíreným vyhľadávaním (RAG) a vektorové databázy

[![Generovanie s rozšíreným vyhľadávaním (RAG) a vektorové databázy](../../../translated_images/15-lesson-banner.ac49e59506175d4fc6ce521561dab2f9ccc6187410236376cfaed13cde371b90.sk.png)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

V lekcii o vyhľadávacích aplikáciách sme sa stručne naučili, ako integrovať vlastné údaje do veľkých jazykových modelov (LLM). V tejto lekcii sa budeme podrobnejšie zaoberať konceptmi zakotvenia vašich údajov vo vašej aplikácii LLM, mechanizmami procesu a metódami ukladania údajov, vrátane vektorových reprezentácií a textu.

> **Video čoskoro dostupné**

## Úvod

V tejto lekcii sa budeme venovať nasledujúcim témam:

- Úvod do RAG, čo to je a prečo sa používa v AI (umelej inteligencii).

- Pochopenie, čo sú vektorové databázy, a ich vytvorenie pre našu aplikáciu.

- Praktický príklad, ako integrovať RAG do aplikácie.

## Ciele učenia

Po dokončení tejto lekcie budete schopní:

- Vysvetliť význam RAG pri vyhľadávaní a spracovaní údajov.

- Nastaviť aplikáciu RAG a zakotviť vaše údaje do LLM.

- Efektívne integrovať RAG a vektorové databázy do aplikácií LLM.

## Náš scenár: vylepšenie našich LLM vlastnými údajmi

V tejto lekcii chceme pridať naše vlastné poznámky do startupu zameraného na vzdelávanie, čo umožní chatbotovi získať viac informácií o rôznych témach. Použitím našich poznámok budú môcť študenti lepšie študovať a pochopiť rôzne témy, čo im uľahčí prípravu na skúšky. Na vytvorenie nášho scenára použijeme:

- `Azure OpenAI:` LLM, ktorý použijeme na vytvorenie nášho chatbota.

- `Lekcia pre začiatočníkov v AI o neurónových sieťach:` to budú údaje, na ktorých zakotvíme náš LLM.

- `Azure AI Search` a `Azure Cosmos DB:` vektorová databáza na ukladanie našich údajov a vytvorenie indexu vyhľadávania.

Používatelia budú môcť vytvárať cvičné kvízy zo svojich poznámok, kartičky na opakovanie a zhrnutia do stručných prehľadov. Aby sme mohli začať, pozrime sa, čo je RAG a ako funguje:

## Generovanie s rozšíreným vyhľadávaním (RAG)

Chatbot poháňaný LLM spracováva používateľské podnety na generovanie odpovedí. Je navrhnutý tak, aby bol interaktívny a komunikoval s používateľmi na širokej škále tém. Jeho odpovede sú však obmedzené na poskytnutý kontext a jeho základné tréningové údaje. Napríklad, GPT-4 má hranicu znalostí k septembru 2021, čo znamená, že nemá informácie o udalostiach, ktoré sa stali po tomto období. Okrem toho údaje použité na tréning LLM nezahŕňajú dôverné informácie, ako sú osobné poznámky alebo manuál produktov spoločnosti.

### Ako funguje RAG (Generovanie s rozšíreným vyhľadávaním)

![diagram ukazujúci, ako funguje RAG](../../../translated_images/how-rag-works.f5d0ff63942bd3a638e7efee7a6fce7f0787f6d7a1fca4e43f2a7a4d03cde3e0.sk.png)

Predstavte si, že chcete nasadiť chatbota, ktorý vytvára kvízy z vašich poznámok, budete potrebovať spojenie s databázou znalostí. Tu prichádza na pomoc RAG. RAG funguje nasledovne:

- **Databáza znalostí:** Pred vyhľadávaním je potrebné tieto dokumenty spracovať, zvyčajne rozdelením veľkých dokumentov na menšie časti, ich transformáciou na vektorové reprezentácie a uložením do databázy.

- **Dotaz používateľa:** Používateľ položí otázku.

- **Vyhľadávanie:** Keď používateľ položí otázku, model vektorovej reprezentácie vyhľadá relevantné informácie v našej databáze znalostí, aby poskytol viac kontextu, ktorý bude zahrnutý do podnetu.

- **Rozšírené generovanie:** LLM vylepší svoju odpoveď na základe získaných údajov. To umožňuje, aby generovaná odpoveď nebola založená len na predtrénovaných údajoch, ale aj na relevantných informáciách z pridaného kontextu. Získané údaje sa použijú na rozšírenie odpovedí LLM. LLM potom vráti odpoveď na otázku používateľa.

![diagram ukazujúci architektúru RAG](../../../translated_images/encoder-decode.f2658c25d0eadee2377bb28cf3aee8b67aa9249bf64d3d57bb9be077c4bc4e1a.sk.png)

Architektúra RAG je implementovaná pomocou transformátorov, ktoré pozostávajú z dvoch častí: kodéra a dekodéra. Napríklad, keď používateľ položí otázku, vstupný text sa 'zakóduje' do vektorov, ktoré zachytávajú význam slov, a vektory sa 'dekódujú' do indexu dokumentov a generujú nový text na základe používateľského dotazu. LLM používa model kodér-dekodér na generovanie výstupu.

Dva prístupy pri implementácii RAG podľa navrhovaného článku: [Generovanie s rozšíreným vyhľadávaním pre NLP úlohy náročné na znalosti](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) sú:

- **_RAG-Sequence_** používa získané dokumenty na predpovedanie najlepšej možnej odpovede na používateľský dotaz.

- **RAG-Token** používa dokumenty na generovanie ďalšieho tokenu, potom ich získava na odpoveď na používateľský dotaz.

### Prečo používať RAG? 

- **Bohatstvo informácií:** zabezpečuje, že textové odpovede sú aktuálne a aktuálne. Zlepšuje výkon pri úlohách špecifických pre danú oblasť prístupom k internej databáze znalostí.

- Znižuje vymýšľanie využitím **overiteľných údajov** v databáze znalostí na poskytnutie kontextu k používateľským dotazom.

- Je **nákladovo efektívny**, pretože je ekonomickejší v porovnaní s jemným doladením LLM.

## Vytvorenie databázy znalostí

Naša aplikácia je založená na našich osobných údajoch, t.j. lekcii o neurónových sieťach z kurikula AI pre začiatočníkov.

### Vektorové databázy

Vektorová databáza, na rozdiel od tradičných databáz, je špecializovaná databáza navrhnutá na ukladanie, správu a vyhľadávanie vektorových reprezentácií. Ukladá číselné reprezentácie dokumentov. Rozdelenie údajov na číselné vektorové reprezentácie uľahčuje nášmu AI systému pochopenie a spracovanie údajov.

Ukladáme naše vektorové reprezentácie do vektorových databáz, pretože LLM majú limit na počet tokenov, ktoré akceptujú ako vstup. Keďže nemôžete poslať celé vektorové reprezentácie do LLM, budeme ich musieť rozdeliť na časti a keď používateľ položí otázku, vektorové reprezentácie najviac podobné otázke budú vrátené spolu s podnetom. Rozdelenie na časti tiež znižuje náklady na počet tokenov prechádzajúcich cez LLM.

Niektoré populárne vektorové databázy zahŕňajú Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant a DeepLake. Môžete vytvoriť model Azure Cosmos DB pomocou Azure CLI s nasledujúcim príkazom:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Od textu k vektorovým reprezentáciám

Predtým, než uložíme naše údaje, budeme ich musieť konvertovať na vektorové reprezentácie pred ich uložením do databázy. Ak pracujete s veľkými dokumentmi alebo dlhými textami, môžete ich rozdeliť na základe očakávaných dotazov. Rozdelenie na časti môže byť na úrovni vety alebo odseku. Keďže rozdelenie na časti odvodzuje významy zo slov okolo nich, môžete pridať nejaký ďalší kontext k časti, napríklad pridaním názvu dokumentu alebo zahrnutím nejakého textu pred alebo po časti. Údaje môžete rozdeliť na časti nasledovne:

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

Keď sú rozdelené na časti, môžeme potom text zakódovať pomocou rôznych modelov vektorových reprezentácií. Niektoré modely, ktoré môžete použiť, zahŕňajú: word2vec, ada-002 od OpenAI, Azure Computer Vision a mnoho ďalších. Výber modelu závisí od jazykov, ktoré používate, typu obsahu, ktorý kódujete (text/obrázky/audio), veľkosti vstupu, ktorý môže kódovať, a dĺžky výstupu vektorovej reprezentácie.

Príklad zakódovaného textu pomocou modelu OpenAI `text-embedding-ada-002` je:
![vektorová reprezentácia slova mačka](../../../translated_images/cat.74cbd7946bc9ca380a8894c4de0c706a4f85b16296ffabbf52d6175df6bf841e.sk.png)

## Vyhľadávanie a vektorové vyhľadávanie

Keď používateľ položí otázku, vyhľadávač ju transformuje na vektor pomocou kodéra dotazov, potom prehľadáva náš index dokumentov pre relevantné vektory v dokumente, ktoré súvisia s vstupom. Keď je hotovo, konvertuje vstupný vektor aj vektory dokumentov na text a posiela ich cez LLM.

### Vyhľadávanie

Vyhľadávanie nastáva, keď sa systém snaží rýchlo nájsť dokumenty z indexu, ktoré spĺňajú kritériá vyhľadávania. Cieľom vyhľadávača je získať dokumenty, ktoré budú použité na poskytnutie kontextu a zakotvenie LLM na vašich údajoch.

Existuje niekoľko spôsobov, ako vykonať vyhľadávanie v našej databáze, ako napríklad:

- **Vyhľadávanie podľa kľúčových slov** - používa sa na textové vyhľadávanie.

- **Sémantické vyhľadávanie** - používa sémantický význam slov.

- **Vektorové vyhľadávanie** - konvertuje dokumenty z textu na vektorové reprezentácie pomocou modelov vektorových reprezentácií. Vyhľadávanie sa vykonáva dotazovaním dokumentov, ktorých vektorové reprezentácie sú najbližšie k otázke používateľa.

- **Hybridné vyhľadávanie** - kombinácia vyhľadávania podľa kľúčových slov a vektorového vyhľadávania.

Výzvou pri vyhľadávaní je, keď v databáze nie je žiadna podobná odpoveď na dotaz, systém potom vráti najlepšie informácie, ktoré môže získať. Môžete však použiť taktiky ako nastavenie maximálnej vzdialenosti pre relevantnosť alebo použitie hybridného vyhľadávania, ktoré kombinuje vyhľadávanie podľa kľúčových slov a vektorové vyhľadávanie. V tejto lekcii použijeme hybridné vyhľadávanie, kombináciu vektorového a vyhľadávania podľa kľúčových slov. Naše údaje uložíme do dátového rámca so stĺpcami obsahujúcimi časti a vektorové reprezentácie.

### Vektorová podobnosť

Vyhľadávač prehľadáva databázu znalostí pre vektorové reprezentácie, ktoré sú blízko seba, najbližšie susedné, pretože sú to texty, ktoré sú podobné. V prípade, že používateľ položí dotaz, najprv sa zakóduje a potom sa porovná s podobnými vektorovými reprezentáciami. Bežné meranie, ktoré sa používa na zistenie, ako sú si rôzne vektory podobné, je kosínová podobnosť, ktorá je založená na uhle medzi dvoma vektormi.

Na meranie podobnosti môžeme použiť aj alternatívy ako euklidovskú vzdialenosť, ktorá je priamou čiarou medzi koncovými bodmi vektorov, a skalárny súčin, ktorý meria súčet súčinov zodpovedajúcich prvkov dvoch vektorov.

### Index vyhľadávania

Pri vyhľadávaní budeme potrebovať vytvoriť index vyhľadávania pre našu databázu znalostí pred vykonaním vyhľadávania. Index bude ukladať naše vektorové reprezentácie a môže rýchlo vyhľadať najpodobnejšie časti aj vo veľkej databáze. Index môžeme vytvoriť lokálne pomocou:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Preusporiadanie

Keď dotazujete databázu, možno budete potrebovať zoradiť výsledky od najrelevantnejších. LLM na preusporiadanie využíva strojové učenie na zlepšenie relevantnosti výsledkov vyhľadávania ich usporiadaním od najrelevantnejších. Použitím Azure AI Search sa preusporiadanie vykonáva automaticky pomocou sémantického preusporiadania. Príklad, ako funguje preusporiadanie pomocou najbližších susedov:

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

## Spojenie všetkého dohromady

Posledným krokom je pridanie nášho LLM do mixu, aby sme mohli získať odpovede, ktoré sú zakotvené na našich údajoch. Môžeme to implementovať nasledovne:

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

## Hodnotenie našej aplikácie

### Metódy hodnotenia

- Kvalita poskytnutých odpovedí, zabezpečenie, že znejú prirodzene, plynulo a ľudsky.

- Zakotvenie údajov: hodnotenie, či odpoveď pochádza z poskytnutých dokumentov.

- Relevantnosť: hodnotenie, či odpoveď zodpovedá a súvisí s položenou otázkou.

- Plynulosť - či odpoveď dáva zmysel gramaticky.

## Príklady použitia RAG (Generovanie s rozšíreným vyhľadávaním) a vektorových databáz

Existuje mnoho rôznych príkladov použitia, kde funkčné volania môžu zlepšiť vašu aplikáciu, ako napríklad:

- Otázky a odpovede: zakotvenie údajov vašej spoločnosti do chatu, ktorý môžu zamestnanci používať na kladenie otázok.

- Systémy odporúčaní: kde môžete vytvoriť systém, ktorý zodpovedá najpodobnejším hodnotám, napr. filmy, reštaurácie a mnoho ďalších.

- Služby chatbotov: môžete ukladať históriu chatu a personalizovať konverzáciu na základe údajov používateľa.

- Vyhľadávanie obrázkov na základe vektorových reprezentácií, užitočné pri rozpoznávaní obrázkov a detekcii anomálií.

## Zhrnutie

Pokryli sme základné oblasti RAG od pridania našich údajov do aplikácie, používateľského dotazu až po výstup. Na zjednodušenie vytvárania RAG môžete použiť rámce ako Semantic Kernel, Langchain alebo Autogen.

## Zadanie

Na pokračovanie vo vašom učení o Generovaní s rozšíreným vyhľadávaním (RAG) môžete:

- Vytvoriť front-end pre aplikáciu pomocou rámca podľa vášho výberu.

- Využiť rámec, buď LangChain alebo Semantic Kernel, a znovu vytvoriť vašu aplikáciu.

Gratulujeme k dokončeniu lekcie 👏.

## Učenie sa tu nekončí, pokračujte v ceste

Po dokončení tejto lekcie si pozrite našu [kolekciu učenia o generatívnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste pokračovali v zlepšovaní svojich znalostí o generatívnej AI!

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.