<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4b0266fbadbba7ded891b6485adc66d",
  "translation_date": "2025-10-17T21:39:04+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "cs"
}
-->
# Generování s podporou vyhledávání (RAG) a vektorové databáze

[![Generování s podporou vyhledávání (RAG) a vektorové databáze](../../../translated_images/15-lesson-banner.ac49e59506175d4fc6ce521561dab2f9ccc6187410236376cfaed13cde371b90.cs.png)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

V lekci o vyhledávacích aplikacích jsme se krátce naučili, jak integrovat vlastní data do modelů velkých jazyků (LLMs). V této lekci se podrobněji zaměříme na koncepty zakotvení vašich dat v aplikaci LLM, na mechaniku procesu a na metody ukládání dat, včetně vektorových reprezentací a textu.

> **Video bude brzy dostupné**

## Úvod

V této lekci se budeme zabývat následujícími tématy:

- Úvod do RAG, co to je a proč se používá v oblasti umělé inteligence (AI).

- Porozumění tomu, co jsou vektorové databáze, a vytvoření jedné pro naši aplikaci.

- Praktický příklad, jak integrovat RAG do aplikace.

## Cíle učení

Po dokončení této lekce budete schopni:

- Vysvětlit význam RAG při vyhledávání a zpracování dat.

- Nastavit aplikaci RAG a zakotvit vaše data do LLM.

- Efektivně integrovat RAG a vektorové databáze do aplikací LLM.

## Náš scénář: vylepšení našich LLM pomocí vlastních dat

V této lekci chceme přidat naše vlastní poznámky do vzdělávacího startupu, což umožní chatbotu získat více informací o různých tématech. Díky poznámkám, které máme, budou studenti schopni lépe studovat a porozumět různým tématům, což jim usnadní přípravu na zkoušky. Pro vytvoření našeho scénáře použijeme:

- `Azure OpenAI:` LLM, který použijeme k vytvoření našeho chatbota

- `Lekce pro začátečníky o neuronových sítích:` to budou data, na kterých zakotvíme náš LLM

- `Azure AI Search` a `Azure Cosmos DB:` vektorová databáze pro ukládání našich dat a vytvoření vyhledávacího indexu

Uživatelé budou schopni vytvářet cvičné kvízy ze svých poznámek, studijní kartičky a shrnutí do stručných přehledů. Abychom mohli začít, podívejme se, co je RAG a jak funguje:

## Generování s podporou vyhledávání (RAG)

Chatbot poháněný LLM zpracovává uživatelské dotazy a generuje odpovědi. Je navržen tak, aby byl interaktivní a komunikoval s uživateli na široké škále témat. Jeho odpovědi jsou však omezeny na kontext, který je mu poskytnut, a na jeho základní tréninková data. Například GPT-4 má znalostní limit k září 2021, což znamená, že nemá znalosti o událostech, které se staly po tomto období. Kromě toho data použitá k trénování LLM vylučují důvěrné informace, jako jsou osobní poznámky nebo manuál produktů společnosti.

### Jak fungují RAG (Generování s podporou vyhledávání)

![schéma ukazující, jak fungují RAG](../../../translated_images/how-rag-works.f5d0ff63942bd3a638e7efee7a6fce7f0787f6d7a1fca4e43f2a7a4d03cde3e0.cs.png)

Představte si, že chcete nasadit chatbota, který vytváří kvízy z vašich poznámek, budete potřebovat připojení k databázi znalostí. Zde přichází na řadu RAG. RAG funguje následovně:

- **Databáze znalostí:** Před vyhledáváním je třeba tyto dokumenty nahrát a předzpracovat, obvykle rozdělením velkých dokumentů na menší části, jejich transformací na vektorové reprezentace a uložením do databáze.

- **Dotaz uživatele:** Uživatel položí otázku.

- **Vyhledávání:** Když uživatel položí otázku, model vektorových reprezentací vyhledá relevantní informace v naší databázi znalostí, aby poskytl více kontextu, který bude začleněn do dotazu.

- **Generování s podporou:** LLM vylepší svou odpověď na základě získaných dat. To umožňuje, aby odpověď byla nejen založena na předtrénovaných datech, ale také na relevantních informacích z přidaného kontextu. Získaná data se používají k vylepšení odpovědí LLM. LLM poté vrátí odpověď na otázku uživatele.

![schéma ukazující architekturu RAG](../../../translated_images/encoder-decode.f2658c25d0eadee2377bb28cf3aee8b67aa9249bf64d3d57bb9be077c4bc4e1a.cs.png)

Architektura RAG je implementována pomocí transformátorů, které se skládají ze dvou částí: kodéru a dekodéru. Například když uživatel položí otázku, vstupní text je "zakódován" do vektorů zachycujících význam slov a vektory jsou "dekódovány" do našeho indexu dokumentů a generují nový text na základě dotazu uživatele. LLM používá model kodér-dekodér k vytvoření výstupu.

Dva přístupy při implementaci RAG podle navrhovaného článku: [Generování s podporou vyhledávání pro úkoly NLP (zpracování přirozeného jazyka) náročné na znalosti](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) jsou:

- **_RAG-Sequence_** používá získané dokumenty k předpovědi nejlepší možné odpovědi na dotaz uživatele.

- **RAG-Token** používá dokumenty k vytvoření dalšího tokenu, poté je získá k odpovědi na dotaz uživatele.

### Proč používat RAG? 

- **Bohatost informací:** zajišťuje, že textové odpovědi jsou aktuální a relevantní. Zvyšuje tak výkon při úkolech specifických pro danou oblast díky přístupu k interní databázi znalostí.

- Snižuje zkreslení využitím **ověřitelných dat** v databázi znalostí k poskytnutí kontextu k dotazům uživatelů.

- Je **nákladově efektivní**, protože je ekonomičtější než jemné ladění LLM.

## Vytvoření databáze znalostí

Naše aplikace je založena na našich osobních datech, tj. na lekci o neuronových sítích z kurikula AI pro začátečníky.

### Vektorové databáze

Vektorová databáze, na rozdíl od tradičních databází, je specializovaná databáze navržená k ukládání, správě a vyhledávání vektorových reprezentací. Ukládá číselné reprezentace dokumentů. Rozdělení dat na číselné vektorové reprezentace usnadňuje našemu AI systému porozumění a zpracování dat.

Vektorové reprezentace ukládáme do vektorových databází, protože LLM mají limit počtu tokenů, které přijímají jako vstup. Jelikož nemůžete předat celé vektorové reprezentace LLM, musíme je rozdělit na části a když uživatel položí otázku, vektorové reprezentace nejvíce podobné otázce budou vráceny spolu s dotazem. Rozdělení na části také snižuje náklady na počet tokenů předaných LLM.

Mezi oblíbené vektorové databáze patří Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant a DeepLake. Model Azure Cosmos DB můžete vytvořit pomocí Azure CLI pomocí následujícího příkazu:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Od textu k vektorovým reprezentacím

Než uložíme naše data, budeme je muset převést na vektorové reprezentace, než budou uložena v databázi. Pokud pracujete s velkými dokumenty nebo dlouhými texty, můžete je rozdělit na části na základě očekávaných dotazů. Rozdělení na části může být provedeno na úrovni věty nebo odstavce. Jelikož rozdělení na části odvozuje význam ze slov kolem nich, můžete přidat nějaký další kontext k části, například přidáním názvu dokumentu nebo zahrnutím textu před nebo za část. Data můžete rozdělit na části následujícím způsobem:

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

Jakmile jsou data rozdělena na části, můžeme je poté zakódovat pomocí různých modelů vektorových reprezentací. Některé modely, které můžete použít, zahrnují: word2vec, ada-002 od OpenAI, Azure Computer Vision a mnoho dalších. Výběr modelu závisí na jazycích, které používáte, typu obsahu, který je kódován (text/obrázky/audio), velikosti vstupu, který může být zakódován, a délce výstupu vektorové reprezentace.

Příklad zakódovaného textu pomocí modelu OpenAI `text-embedding-ada-002` je:
![vektorová reprezentace slova kočka](../../../translated_images/cat.74cbd7946bc9ca380a8894c4de0c706a4f85b16296ffabbf52d6175df6bf841e.cs.png)

## Vyhledávání a vektorové hledání

Když uživatel položí otázku, vyhledávač ji transformuje na vektor pomocí kodéru dotazů, poté prohledá náš index dokumentů pro relevantní vektory v dokumentu, které souvisejí se vstupem. Jakmile je to hotovo, převede jak vstupní vektor, tak vektory dokumentů na text a předá je LLM.

### Vyhledávání

Vyhledávání probíhá, když se systém snaží rychle najít dokumenty z indexu, které splňují kritéria vyhledávání. Cílem vyhledávače je získat dokumenty, které budou použity k poskytnutí kontextu a zakotvení LLM na vašich datech.

Existuje několik způsobů, jak provádět vyhledávání v naší databázi, například:

- **Vyhledávání podle klíčových slov** - používá se pro textové vyhledávání.

- **Sémantické vyhledávání** - používá sémantický význam slov.

- **Vektorové vyhledávání** - převádí dokumenty z textu na vektorové reprezentace pomocí modelů vektorových reprezentací. Vyhledávání bude provedeno dotazováním dokumentů, jejichž vektorové reprezentace jsou nejblíže otázce uživatele.

- **Hybridní** - kombinace vyhledávání podle klíčových slov a vektorového vyhledávání.

Výzvou při vyhledávání je situace, kdy v databázi není podobná odpověď na dotaz, systém pak vrátí nejlepší informace, které může získat. Můžete však použít taktiky, jako je nastavení maximální vzdálenosti pro relevanci nebo použití hybridního vyhledávání, které kombinuje vyhledávání podle klíčových slov a vektorové vyhledávání. V této lekci použijeme hybridní vyhledávání, kombinaci vektorového a vyhledávání podle klíčových slov. Naše data uložíme do datového rámce se sloupci obsahujícími části textu i vektorové reprezentace.

### Vektorová podobnost

Vyhledávač prohledá databázi znalostí pro vektorové reprezentace, které jsou blízko sebe, nejbližší sousedé, protože se jedná o texty, které jsou podobné. V případě, že uživatel položí dotaz, je nejprve zakódován a poté porovnán s podobnými vektorovými reprezentacemi. Běžné měření, které se používá k určení, jak podobné jsou různé vektory, je kosinová podobnost, která je založena na úhlu mezi dvěma vektory.

K měření podobnosti můžeme použít i jiné alternativy, například euklidovskou vzdálenost, což je přímá čára mezi koncovými body vektorů, nebo skalární součin, který měří součet součinů odpovídajících prvků dvou vektorů.

### Vyhledávací index

Při vyhledávání budeme muset vytvořit vyhledávací index pro naši databázi znalostí, než provedeme vyhledávání. Index bude ukládat naše vektorové reprezentace a může rychle získat nejpodobnější části i ve velké databázi. Index můžeme vytvořit lokálně pomocí:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Přerovnání

Jakmile dotazujete databázi, možná budete muset seřadit výsledky od nejrelevantnějších. Přerovnávací LLM využívá strojové učení ke zlepšení relevance výsledků vyhledávání tím, že je seřadí od nejrelevantnějších. Pomocí Azure AI Search je přerovnání provedeno automaticky pomocí sémantického přerovnávače. Příklad, jak přerovnání funguje pomocí nejbližších sousedů:

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

## Spojení všeho dohromady

Posledním krokem je přidání našeho LLM do mixu, aby bylo možné získat odpovědi, které jsou zakotveny na našich datech. Můžeme to implementovat následujícím způsobem:

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

## Hodnocení naší aplikace

### Hodnotící metriky

- Kvalita poskytnutých odpovědí, zajištění, že zní přirozeně, plynule a lidsky.

- Zakotvení dat: hodnocení, zda odpověď pochází z poskytnutých dokumentů.

- Relevance: hodnocení, zda odpověď odpovídá a souvisí s položenou otázkou.

- Plynulost - zda odpověď dává smysl gramaticky.

## Případy použití RAG (Generování s podporou vyhledávání) a vektorových databází

Existuje mnoho různých případů použití, kde volání funkcí může zlepšit vaši aplikaci, například:

- Otázky a odpovědi: zakotvení dat vaší společnosti do chatu, který mohou zaměstnanci používat k pokládání otázek.

- Doporučovací systémy: kde můžete vytvořit systém, který odpovídá nejpodobnějším hodnotám, např. filmy, restaurace a mnoho dalších.

- Služby chatbotů: můžete ukládat historii chatu a personalizovat konverzaci na základě uživatelských dat.

- Vyhledávání obrázků na základě vektorových reprezentací, užitečné při rozpoznávání obrázků a detekci anomálií.

## Shrnutí

Pokryli jsme základní oblasti RAG od přidání našich dat do aplikace, přes uživatelský dotaz až po výstup. Pro zjednodušení tvorby RAG můžete použít frameworky jako Semantic Kernel, Langchain nebo Autogen.

## Úkol

Pro pokračování ve studiu Generování s podporou vyhledávání (RAG) můžete vytvořit:

- Vytvořte front-end pro aplikaci pomocí vámi zvoleného frameworku.

- Využijte framework, buď LangChain nebo Semantic Kernel, a znovu vytvořte vaši aplikaci.

Gratulujeme k dokončení lekce 👏.

## Učení zde nekončí, pokračujte v cestě

Po dokončení této lekce se podívejte na naši [sbírku učení o generativní AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), abyste dále rozvíjeli své znalosti o generativní AI!

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.