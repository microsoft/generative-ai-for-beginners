# Retrieval Augmented Generation (RAG) a vektorové databáze

[![Retrieval Augmented Generation (RAG) a vektorové databáze](../../../translated_images/cs/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

V lekci o vyhledávacích aplikacích jsme se stručně naučili, jak integrovat svá data do Velkých jazykových modelů (LLM). V této lekci se ponoříme hlouběji do konceptů zakotvení vašich dat ve vaší aplikaci LLM, mechaniky procesu a metod ukládání dat, včetně embeddingů a textu.

> **Video brzy k dispozici**

## Úvod

V této lekci pokryjeme následující:

- Úvod do RAG, co to je a proč se používá v AI (umělé inteligenci).

- Porozumění tomu, co jsou vektorové databáze a vytvoření jedné pro naši aplikaci.

- Praktický příklad, jak integrovat RAG do aplikace.

## Cíle učení

Po dokončení této lekce budete schopni:

- Vysvětlit význam RAG při vyhledávání a zpracování dat.

- Nastavit aplikaci RAG a zakotvit svá data do LLM.

- Efektivní integrace RAG a vektorových databází v aplikacích LLM.

## Náš scénář: zlepšení našich LLM vlastním daty

Pro tuto lekci chceme přidat vlastní poznámky do vzdělávacího startupu, který umožní chatbotu získat více informací o různých předmětech. Pomocí našich poznámek budou studenti schopni lépe studovat a pochopit různé tématy, což jim usnadní přípravu na zkoušky. Pro vytvoření našeho scénáře použijeme:

- `Azure OpenAI:` LLM, které použijeme k vytvoření našeho chatbota

- `Lekce AI pro začátečníky o neuronových sítích:` tato data použijeme k zakotvení našeho LLM

- `Azure AI Search` a `Azure Cosmos DB:` vektorová databáze k ukládání dat a vytvoření vyhledávacího indexu

Uživatelé si budou moci vytvářet cvičné kvízy ze svých poznámek, opakovací flashcards a shrnutí do stručných přehledů. Abychom začali, pojďme se podívat, co je RAG a jak funguje:

## Retrieval Augmented Generation (RAG)

Chatbot poháněný LLM zpracovává uživatelské dotazy a generuje odpovědi. Je navržen tak, aby byl interaktivní a komunikoval s uživateli o široké škále témat. Jeho odpovědi jsou však omezeny kontextem, který má k dispozici, a základními tréninkovými daty. Například znalostní hranice GPT-4 je září 2021, což znamená, že nezná události, které se odehrály po tomto datu. Navíc data používaná pro trénink LLM nezahrnují důvěrné informace, jako jsou osobní poznámky nebo firemní produktové příručky.

### Jak fungují RAG (Retrieval Augmented Generation)

![obrázek zobrazující, jak RAG fungují](../../../translated_images/cs/how-rag-works.f5d0ff63942bd3a6.webp)

Představte si, že chcete nasadit chatbota, který vytváří kvízy ze svých poznámek, budete potřebovat připojení ke znalostní databázi. Právě zde přichází na pomoc RAG. RAG fungují takto:

- **Znalostní databáze:** Před vyhledáváním musí být dokumenty ingesovány a předzpracovány, obvykle rozdělením velkých dokumentů na menší části, převedením na textové embeddingy a uložením do databáze.

- **Uživatelský dotaz:** uživatel položí otázku

- **Vyhledávání:** Když uživatel položí otázku, model embeddingu vyhledá relevantní informace ze znalostní databáze, aby poskytl více kontextu, který bude začleněn do promptu.

- **Rozšířená generace:** LLM vylepší svou odpověď na základě retrieved dat. Umožňuje generovat odpověď nejen na základě předtrénovaných dat, ale také na základě relevantních informací z přidaného kontextu. Retrieved data se používají k rozšíření odpovědí LLM. LLM poté vrátí odpověď na uživatelský dotaz.

![obrázek zobrazující architekturu RAG](../../../translated_images/cs/encoder-decode.f2658c25d0eadee2.webp)

Architektura RAG je realizována pomocí transformátorů skládajících se ze dvou částí: enkodéru a dekodéru. Například když uživatel položí otázku, vstupní text je „zakódován“ do vektorů, které zachycují význam slov, a tyto vektory jsou „dekódovány“ do našeho indexu dokumentů a generují nový text na základě uživatelského dotazu. LLM používá model enkodér-dekodér pro generování výstupu.

Dvě přístupy při implementaci RAG podle navrhovaného článku: [Retrieval-Augmented Generation for Knowledge intensive NLP Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) jsou:

- **_RAG-Sequence_** používání retrieved dokumentů k předpovědi nejlepší možné odpovědi na uživatelský dotaz

- **RAG-Token** používání dokumentů k generování dalšího tokenu, poté jejich retrievování k odpovědi na uživatelský dotaz

### Proč používat RAG?

- **Bohatost informací:** zajišťuje, že textové odpovědi jsou aktuální a relevantní. Zlepšuje výkon v doménově specifických úlohách díky přístupu ke znalostní databázi.

- Snižuje fabulaci použitím **ověřitelných dat** ve znalostní databázi k poskytování kontextu uživatelským dotazům.

- Je **nákladově efektivní**, protože je levnější než doladění (fine-tuning) LLM.

## Vytvoření znalostní databáze

Naše aplikace je založena na našich osobních datech, tj. lekci o neuronových sítích z kurikula AI pro začátečníky.

### Vektorové databáze

Vektorová databáze je na rozdíl od tradičních databází specializovaná databáze navržená pro ukládání, správu a vyhledávání embedded vektorů. Ukládá číselné reprezentace dokumentů. Rozložení dat na číselné embeddingy usnadňuje našemu AI systému pochopení a zpracování dat.

Ukládáme naše embeddingy ve vektorových databázích, protože LLM mají limit počtu tokenů, které přijímají jako vstup. Jelikož nelze předat celé embeddingy do LLM, potřebujeme je rozdělit na části, a když uživatel položí otázku, vrátí se embeddingy nejvíce odpovídající dotazu spolu s promptem. Členění také snižuje náklady na počet tokenů zpracovávaných LLM.

Mezi populární vektorové databáze patří Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant a DeepLake. Azure Cosmos DB model lze vytvořit pomocí Azure CLI následujícím příkazem:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Z textu na embeddingy

Než uložíme naše data, musíme je převést na vektorové embeddingy před uložením do databáze. Pokud pracujete s velkými dokumenty nebo dlouhými texty, můžete je rozdělit do částí podle očekávaných dotazů. Rozdělení může být na úrovni vět nebo odstavců. Protože členění odvozuje význam z okolních slov, můžete k části přidat další kontext, například název dokumentu nebo text před nebo po části. Data můžete rozdělit následovně:

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

    # Pokud poslední část nedosáhla minimální délky, přidej ji stejně
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Po rozdělení můžeme embedovat text pomocí různých embeddingových modelů. Některé modely, které můžete použít, zahrnují: word2vec, ada-002 od OpenAI, Azure Computer Vision a další. Výběr modelu závisí na používaných jazycích, typu kódovaného obsahu (text/obrázky/audio), velikosti vstupu, kterou může kódovat, a délce výstupu embeddingu.

Příklad embedded textu pomocí modelu OpenAI `text-embedding-ada-002` je:
![embedding slova cat](../../../translated_images/cs/cat.74cbd7946bc9ca38.webp)

## Retrieval a vektorové vyhledávání

Když uživatel položí otázku, retriever ji převede na vektor pomocí enkodéru dotazu, poté prohledá náš vyhledávací index dokumentů pro relevantní vektory, které souvisejí se vstupem. Poté převede vstupní i dokumentové vektory zpět na text a předá je LLM.

### Retrieval

Retrieval nastává, když systém rychle hledá dokumenty v indexu, které splňují kritéria vyhledávání. Cílem retrieveru je získat dokumenty, které poskytnou kontext a zakotví LLM na vašich datech.

Existuje několik způsobů, jak vyhledávat v naší databázi, například:

- **Vyhledávání podle klíčových slov** - používané pro textové vyhledávání

- **Vektorové vyhledávání** - převádí dokumenty z textu na vektorové reprezentace pomocí embeddingových modelů, umožňující **sémantické vyhledávání** na základě významu slov. Vyhledávání probíhá dotazováním dokumentů s vektorovými reprezentacemi, které jsou nejblíže uživatelské otázce.

- **Hybridní** - kombinace vyhledávání podle klíčových slov a vektorového vyhledávání.

Výzvou při retrieval je, že pokud v databázi není podobná odpověď na dotaz, systém vrátí nejlepší dostupné informace. Můžete však použít taktiky jako nastavení maximální vzdálenosti relevance nebo použít hybridní vyhledávání, které kombinuje klíčová slova a vektorové vyhledávání. V této lekci použijeme hybridní vyhledávání, kombinaci vektorového a klíčového slova. Data uložíme do dataframe se sloupci obsahujícími části a embeddingy.

### Vektorová podobnost

Retriever prohledá databázi znalostí podle embeddingů, které jsou blízko sebe, tj. nejbližší sousedé, protože jsou to podobné texty. V našem scénáři uživatel položí dotaz, který je nejprve embedded a pak porovnán s podobnými embeddingy. Běžnou metrikou pro zjištění podobnosti vektorů je kosinová podobnost založená na úhlu mezi dvěma vektory.

Alternativně můžeme použít jiné metriky, jako eukleidovskou vzdálenost, která je přímková vzdálenost mezi koncovými body vektorů, nebo skalární součin, který měří součet součinů odpovídajících prvků dvou vektorů.

### Vyhledávací index

Při retrieval musíme před vyhledáváním vytvořit vyhledávací index pro naši znalostní databázi. Index uloží naše embeddingy a rychle vrátí nejpodobnější části i ve velké databázi. Index můžeme vytvořit lokálně pomocí:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Vytvořte vyhledávací index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Pro dotazování na index můžete použít metodu kneighbors
distances, indices = nbrs.kneighbors(embeddings)
```

### Přerazení výsledků (Re-ranking)

Po dotazu do databáze může být potřeba výsledky seřadit od nejužitečnějších. Rerankovací LLM využívá strojové učení ke zvýšení relevance výsledků setříděním od nejrelevantnějších. Pomocí Azure AI Search se přerazení provádí automaticky pomocí sémantického přerazovače. Příklad fungování rerankingu pomocí nejbližších sousedů:

```python
# Najděte nejpodobnější dokumenty
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Vytiskněte nejpodobnější dokumenty
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Sloučení všeho dohromady

Posledním krokem je přidání našeho LLM do celku, abychom mohli získat odpovědi, které vycházejí z našich dat. Implementujeme to následovně:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Převést otázku na dotazníkový vektor
    query_vector = create_embeddings(user_input)

    # Najít nejpodobnější dokumenty
    distances, indices = nbrs.kneighbors([query_vector])

    # přidat dokumenty k dotazu, aby poskytly kontext
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # zkombinovat historii a uživatelský vstup
    history.append(user_input)

    # vytvořit objekt zprávy
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # použít API Odpovědi k vygenerování odpovědi
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

## Hodnocení naší aplikace

### Hodnotící metriky

- Kvalita odpovědí, aby zněly přirozeně, plynule a lidsky

- Zakotvenost dat: hodnocení zda odpověď pochází ze zadaných dokumentů

- Relevance: hodnocení, zda odpověď odpovídá a souvisí s položenou otázkou

- Plynulost - zda je odpověď gramaticky správná

## Případy použití RAG a vektorových databází

Existuje mnoho různých případů použití, kde mohou funkční volání vylepšit vaši aplikaci, například:

- Otázky a odpovědi: zakotvení firemních dat do chatu, který mohou používat zaměstnanci k pokládání otázek.

- Doporučovací systémy: kde můžete vytvořit systém, který nalezne nejpodobnější hodnoty, např. filmy, restaurace a další.

- Chatbot služby: lze uložit historii chatů a personalizovat konverzaci podle uživatelských dat.

- Vyhledávání obrázků na základě vektorových embeddingů, užitečné při rozpoznávání obrázků a detekci anomálií.

## Shrnutí

Pokryli jsme základní oblasti RAG, od přidání dat do aplikace přes uživatelský dotaz až po výstup. Pro usnadnění tvorby RAG můžete použít rámce jako Semantic Kernel, Langchain nebo Autogen.

## Zadání

Pro pokračování ve studiu Retrieval Augmented Generation (RAG) můžete vybudovat:

- Vytvořit front-end aplikace pomocí vámi zvoleného frameworku

- Využít framework, buď LangChain nebo Semantic Kernel, a znovu vytvořit aplikaci.

Gratulujeme k dokončení lekce 👏.

## Učení zde nekončí, pokračujte v cestě

Po dokončení této lekce si prohlédněte naši [kolekci Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) a pokračujte ve zvyšování svých znalostí v oblasti Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->