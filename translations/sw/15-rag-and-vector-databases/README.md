# Uundaji Ulioboreshwa kwa Urejeshaji (RAG) na Hifadhidata za Vector

[![Uundaji Ulioboreshwa kwa Urejeshaji (RAG) na Hifadhidata za Vector](../../../translated_images/sw/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Katika somo la matumizi ya utafutaji, tulijifunza kwa kifupi jinsi ya kuingiza data yako mwenyewe ndani ya Modeli Kubwa za Lugha (LLMs). Katika somo hili, tutaingia zaidi katika dhana za kuweka data yako msingi katika programu yako ya LLM, jinsi mchakato unavyofanya kazi na mbinu za kuhifadhi data, pamoja na embeddings na maandishi.

> **Video Inakuja Hivi Karibuni**

## Utangulizi

Katika somo hili tutashughulikia mambo yafuatayo:

- Utangulizi wa RAG, ni nini na kwa nini inatumiwa katika AI (akili bandia).

- Kuelewa ni nini hifadhidata za vector na jinsi ya kuunda moja kwa ajili ya programu yetu.

- Mfano wa vitendo wa jinsi ya kuingiza RAG katika programu.

## Malengo ya Kujifunza

Baada ya kumaliza somo hili, utaweza:

- Eleza umuhimu wa RAG katika urejeshaji na usindikaji wa data.

- Sanidi programu ya RAG na uweke data zako kama msingi kwa LLM

- Uingizaji mzuri wa RAG na Hifadhidata za Vector katika Programu za LLM.

## Hali Yetu: kuboresha LLM zetu na data zetu binafsi

Kwa somo hili, tunataka kuongeza maelezo yetu binafsi katika huduma ya elimu, ambayo inaruhusu chatbot kupata habari zaidi kuhusu masomo tofauti. Kutumia maelezo tunayayo, wanafunzi wataweza kusoma vizuri na kuelewa mada tofauti, na kufanya iwe rahisi kurudia kwa ajili ya mitihani yao. Kuunda hali yetu, tutatumia:

- `Azure OpenAI:` LLM tutakayotumia kuunda chatbot yetu

- `Somo la AI kwa wanaoanza' juu ya Mtandao wa Neva: hii itakuwa data tunayoweka msingi wa LLM yetu

- `Azure AI Search` na `Azure Cosmos DB:` hifadhidata za vector kuhifadhi data yetu na kuunda index ya utafutaji

Watumiaji wataweza kuunda maswali ya mazoezi kutoka kwa maelezo yao, kadi za maelezo za kurudia na kuzipatia muhtasari mfupi. Ili kuanza, tazama ni nini RAG na jinsi inavyofanya kazi:

## Uundaji Ulioboreshwa kwa Urejeshaji (RAG)

Chatbot inayotumia LLM inashughulikia maelekezo ya mtumiaji kutengeneza majibu. Imetengenezwa kuwa ya kuingiliana na inashirikiana na watumiaji juu ya mada mbalimbali. Hata hivyo, majibu yake yanategemea muktadha uliotolewa na data yake ya msingi ya mafunzo. Kwa mfano, GPT-4 iliwa na ufahamu hadi Septemba 2021, ikimaanisha haijui matukio yaliyotokea baada ya kipindi hicho. Zaidi ya hayo, data inayotumika kufundisha LLM haijumuishi taarifa za siri kama maelezo binafsi au mwongozo wa bidhaa ya kampuni.

### Jinsi RAGs (Uundaji Ulioboreshwa kwa Urejeshaji) unavyofanya kazi

![mchoro unaoonyesha jinsi RAGs inavyofanya kazi](../../../translated_images/sw/how-rag-works.f5d0ff63942bd3a6.webp)

Fikiria unataka kuanzisha chatbot inayotengeneza maswali kutoka kwa maelezo yako, utahitaji uhusiano na hifadhibase ya maarifa. Hapa ndipo RAG inapoingilia. RAGs hufanya kazi kama ifuatavyo:

- **Hifadhibase ya maarifa:** Kabla ya urejeshaji, hati hizi zinapaswa kuingizwa na kusindika awali, kwa kawaida kugawanya hati kubwa katika vidogo vidogo, kugeuza kuwa embeddings za maandishi na kuzihifadhi katika hifadhidata.

- **Swali la Mtumiaji:** mtumiaji anauliza swali

- **Urejeshaji:** Mtindo wa embedding hurudisha taarifa zinazohusiana kutoka hifadhibase yetu ya maarifa kutoa muktadha zaidi utakaoingizwa katika maelekezo.

- **Uundaji Ulioboreshwa:** LLM huongeza jibu hili kulingana na data iliyorejeshwa. Hii inaruhusu jibu kutengenezwa si tu kwa kutumia data ya awali, bali pia taarifa muhimu kutoka kwenye muktadha uliowekwa. Data iliyorejeshwa hutumiwa kuongeza ubora wa majibu ya LLM. Kisha LLM huirudisha jibu kwa swali la mtumiaji.

![mchoro unaoonyesha usanifu wa RAGs](../../../translated_images/sw/encoder-decode.f2658c25d0eadee2.webp)

Usanifu wa RAGs umejengwa kwa kutumia transformers yenye sehemu mbili: encoder na decoder. Kwa mfano, mtumiaji anauliza swali, maandishi ya ingizo yana 'encoded' kuwa vectors zinazoshikilia maana ya maneno, na vectors hizo 'decoded' katika index ya hati na kutoa maandishi mapya kulingana na swali la mtumiaji. LLM hutumia model ya encoder-decoder ili kuzalisha matokeo.

Njia mbili za kutekeleza RAG kulingana na karatasi iliyopewa: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) ni:

- **_RAG-Sequence_** kutumia hati zilizopatikana kutabiri jibu bora kabisa kwa swali la mtumiaji

- **RAG-Token** kutumia hati kuunda token inayofuata, kisha kuzipata tena kutoa jibu kwa swali la mtumiaji

### Kwa nini utumie RAGs? 

- **Utajiri wa taarifa:** kuhakikisha majibu ya maandishi ni ya kisasa na ya sasa. Hii huchangia utendaji bora kwenye kazi maalum kwa kupata taarifa za ndani ya hifadhibase.

- Kupunguza uongo kwa kutumia **data inayothibitishwa** katika hifadhibase kutoa muktadha kwa maswali ya mtumiaji.

- Ni **gharama nafuu** kwa kuwa ni ya bei rahisi ikilinganishwa na kufundisha LLM upya

## Kuunda hifadhibase ya maarifa

Programu yetu itategemea data binafsi ya somo la Mtandao wa Neva katika mtaala wa AI kwa Wanaoanza.

### Hifadhidata za Vector

Hifadhidata ya vector, tofauti na hifadhidata za kawaida, ni hifadhidata maalum iliyotengenezwa kuhifadhi, kusimamia na kutafuta vectors zenye embeddings. Hifadhi inawakilisho wa nambari wa hati. Kugawanya data kuwa embeddings za nambari hurahisisha mfumo wetu wa AI kuelewa na kutambua data.

Tunahifadhi embeddings zetu katika hifadhidata za vector kwani LLM zina kikomo cha idadi ya tokens wanazokubali kama ingizo. Kwa kuwa huwezi kupitisha embeddings zote kwa LLM, tunahitaji kuzivunja katika vipande na mtumiaji anapouliza swali, embeddings zinazofanana zaidi na swali zitarejeshwa pamoja na maelekezo. Ugawaji pia hupunguza gharama za tokens zinazopitishwa kwa LLM.

Baadhi ya hifadhidata maarufu za vector ni Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant na DeepLake. Unaweza kuunda mfano wa Azure Cosmos DB kwa kutumia Azure CLI kwa amri ifuatayo:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Kutoka maandishi kwenda embeddings

Kabla ya kuhifadhi data yetu, tutahitaji kuibadilisha kuwa vector embeddings kabla haijahifadhiwa katika hifadhidata. Ikiwa unafanya kazi na hati kubwa au maandishi marefu, unaweza kuyagawa kulingana na maswali unayoyatarajia. Ugawaji unaweza kufanywa kwenye sentensi au aya. Kwa kuwa ugawaji hutegemea maana ya maneno yanayozunguka, unaweza kuongeza muktadha mwingine kwa kipande, kwa mfano kwa kuongeza kichwa cha hati au maandishi kabla au baada ya kipande. Unaweza kugawa data kama ifuatavyo:

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

    # Ikiwa kipande cha mwisho hakifikii urefu wa chini, ongeza hata hivyo
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Baada ya kugawa, tunaweza kisha kuingiza maandishi yetu kwa kutumia modeli tofauti za embedding. Baadhi ya modeli unazoweza kutumia ni pamoja na: word2vec, ada-002 ya OpenAI, Azure Computer Vision na nyingine nyingi. Kuchagua modeli kutategemea lugha unazotumia, aina ya maudhui yaliyofunikwa (maandishi/picha/sauti), ukubwa wa ingizo unaoweza kufunika na urefu wa matokeo ya embedding.

Mfano wa maandishi yaliyo embedded kwa kutumia modeli ya OpenAI `text-embedding-ada-002` ni:
![embedding ya neno paka](../../../translated_images/sw/cat.74cbd7946bc9ca38.webp)

## Urejeshaji na Utafutaji wa Vector

Mtumiaji anapouliza swali, retriever hugeuza swali hilo kuva vector kwa kutumia query encoder, kisha huita hifadhidata yetu ya hati kwa ajili ya vectors zinazohusiana. Baada ya hapo hubadilisha vector ya ingizo na vectors za hati kuwa maandishi na kupitisha kupitia LLM.

### Urejeshaji

Urejeshaji hutokea wakati mfumo unajaribu haraka kupata hati kutoka kwenye index zinazokidhi vigezo vya utafutaji. Lengo la retriever ni kupata hati zitakazotumika kutoa muktadha na kuweka LLM msingi kwenye data yako.

Kuna njia kadhaa za kufanya utafutaji ndani ya hifadhidata zetu kama:

- **Utafutaji wa maneno muhimu** - hutumika kwa utafutaji wa maandishi

- **Utafutaji wa vector** - hubadilisha hati kutoka maandishi kuwa vectors kwa kutumia modeli za embedding, kuruhusu **utaftaji wa maana** kwa kutumia maana ya maneno. Urejeshaji hufanywa kwa kuuliza hati zenye vectors zinazofanana zaidi na swali la mtumiaji.

- **Mchanganyiko** - mchanganyiko wa utafutaji wa maneno muhimu na vector.

Changamoto kwa urejeshaji ni pale ambapo hakuna jibu linalofanana na swali kwenye hifadhidata, mfumo utaenda kurejesha taarifa bora walizopata, lakini unaweza kutumia mbinu kama kuweka umbali wa juu kwa umuhimu au kutumia utafutaji mchanganyiko unaochanganya maneno muhimu na vector. Katika somo hili tutatumia utafutaji mchanganyiko, mchanganyiko wa utafutaji wa vector na maneno muhimu. Tutahifadhi data zetu katika dataframe yenye safu zinazoonyesha vipande pamoja na embeddings.

### Usanifu wa Vector

Retriever atatafuta katika hifadhibase ya maarifa kwa embeddings zilizosogezana karibu, jirani wa karibu zaidi, kwani maandishi hayo ni sawa. Katika hali mtumiaji aulize swali, kwanza huingizwa na kisha kulinganishwa na embeddings zinazofanana. Kipimo cha kawaida kinachotumika kutafuta kufanana kwa vectors ni cosine similarity ambacho kinategemea pembe kati ya vectors mbili.

Tunaweza kupima ufanana kwa njia nyingine kama umbali wa Euclidean unaoelezea mstari wa moja kwa moja kati ya mwisho wa vectors na dot product inayopima jumla ya mazao ya vipengele vinavyolingana vya vectors mbili.

### Index ya utafutaji

Wakati wa kufanya urejeshaji, tunapaswa kujenga index ya utafutaji ya hifadhibase ya maarifa kabla ya kufanya utafutaji. Index itahifadhi embeddings zetu na inaweza kurejesha haraka vipande vinavyofanana hata katika hifadhidata kubwa. Tunaweza kuunda index yetu kwa mtaa kwa kutumia:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Unda faharasa la utafutaji
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Kuuliza faharasa, unaweza kutumia njia ya kneighbors
distances, indices = nbrs.kneighbors(embeddings)
```

### Upangaji upya (Re-ranking)

Baada ya kuuliza hifadhidata, huenda ukahitaji kupanga matokeo kuanzia yale yenye umuhimu zaidi. Reranking LLM hutumia Kujifunza kwa Mashine kuboresha umuhimu wa matokeo ya utafutaji kwa kuwapangilia kutoka yale ya umuhimu zaidi. Kutumia Azure AI Search, upangaji upya hufanywa kiotomatiki kwa kutumia semantic reranker. Mfano wa jinsi reranking inavyofanya kazi kwa kutumia majirani wa karibu:

```python
# Tafuta hati zinazofanana zaidi
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Chapisha hati zinazofanana zaidi
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Kuunganisha yote pamoja

Hatua ya mwisho ni kuongeza LLM yetu kuweza kupata majibu ya msingi kutoka data yetu. Tunaweza kuitekeleza kama ifuatavyo:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Badilisha swali kuwa vector ya utafutaji
    query_vector = create_embeddings(user_input)

    # Tafuta nyaraka zinazofanana zaidi
    distances, indices = nbrs.kneighbors([query_vector])

    # ongeza nyaraka kwenye utafutaji kutoa muktadha
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # changanya historia na maingizo ya mtumiaji
    history.append(user_input)

    # tengeneza kitu cha ujumbe
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # tumia API ya Majibu kuunda jibu
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

## Kutathmini programu yetu

### Vipimo vya Tathmini

- Ubora wa majibu yanayotolewa kuhakikisha kuwa yanasikika asili, yanasomeka na yanafanana na sauti ya kibinadamu

- Uzingatiaji wa data: kutathmini kama jibu lililotolewa linatokana na hati zilizotolewa

- Umuhimu: kutathmini kama jibu linaendana na swali liloulizwa

- Ufasaha - kama jibu lina mantiki katika sarufi

## Matumizi ya RAG (Uundaji Ulioboreshwa kwa Urejeshaji) na hifadhidata za vector

Kuna matumizi mengi tofauti ambapo function calls zinaweza kuboresha programu yako kama:

- Maswali na Majibu: kuweka data ya kampuni yako kama msingi wa mazungumzo yanayoweza kutumiwa na wafanyakazi kuuliza maswali.

- Mifumo ya Mapendekezo: ambapo unaweza kuunda mfumo unaolingana na thamani zinazofanana zaidi mfano sinema, migahawa na zaidi.

- Huduma za Chatbot: unaweza kuhifadhi historia ya mazungumzo na kubinafsisha mazungumzo kulingana na data ya mtumiaji.

- Utafutaji wa picha kwa kutumia vector embeddings, muhimu kwa utambuzi wa picha na kugundua dosari.

## Muhtasari

Tumefunika maeneo ya msingi ya RAG kutoka kuongeza data yetu kwenye programu, swali la mtumiaji na matokeo. Ili kurahisisha uundaji wa RAG, unaweza kutumia mifumo kama Semanti Kernel, Langchain au Autogen.

## Kazi ya nyumbani

Kuendelea kujifunza Uundaji Ulioboreshwa kwa Urejeshaji (RAG) unaweza kujenga:

- Jenga kiolesura cha mbele cha programu kwa kutumia mfumo unaoupenda

- Tumia mfumo, iwe LangChain au Semantic Kernel, na uendeleze upya programu yako.

Hongera kwa kumaliza somo 👏.

## Kujifunza hakukomi hapa, endelea Safari

Baada ya kumaliza somo hili, angalia mkusanyiko wetu wa [Mafunzo ya AI ya Uundaji](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuinua maarifa yako ya AI ya Uundaji!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->