<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2210a0466c812d9defc4df2d9a709ff9",
  "translation_date": "2026-01-18T18:51:10+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "sw"
}
-->
# Kuzalishwa kwa Uboreshaji wa Upataji (RAG) na Hifadhidata za Vector

[![Kuzalishwa kwa Uboreshaji wa Upataji (RAG) na Hifadhidata za Vector](../../../../../translated_images/sw/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Katika somo la matumizi ya utafutaji, tulijifunza kwa kifupi jinsi ya kuingiza data yako mwenyewe ndani ya Mifano Mikubwa ya Lugha (LLMs). Katika somo hili, tutaangazia zaidi dhana za kuimarisha data yako katika programu yako ya LLM, jinsi mchakato unavyofanya kazi na mbinu za kuhifadhi data, ikijumuisha embeddings na maandishi.

> **Video Itakuja Hivi Karibuni**

## Utangulizi

Katika somo hili tutashughulikia yafuatayo:

- Utangulizi wa RAG, ni nini na kwa nini hutumika katika AI (akili bandia).

- Kuelewa ni nini hifadhidata za vector na kuunda moja kwa ajili ya programu yetu.

- Mfano wa vitendo jinsi ya kuingiza RAG katika programu.

## Malengo ya Kujifunza

Baada ya kumaliza somo hili, utaweza:

- Kuelezea umuhimu wa RAG katika upataji na usindikaji wa data.

- Kusanidi programu ya RAG na kuimarisha data yako kwa LLM

- Kuunganisha kwa ufanisi RAG na Hifadhidata za Vector katika Programu za LLM.

## Tukio Letu: kuboresha LLM zetu kwa data yetu mwenyewe

Kwa somo hili, tunataka kuongeza maelezo yetu binafsi katika sekta ya elimu, ambayo inaruhusu chatbot kupata taarifa zaidi kuhusu masomo tofauti. Kutumia maelezo tuliyonayo, wanafunzi wataweza kusoma kwa ufanisi zaidi na kuelewa mada mbalimbali, na kufanya iwe rahisi kurudia kwa ajili ya mitihani yao. Kuunda tukio letu, tutatumia:

- `Azure OpenAI:` LLM tutakayotumia kuunda chatbot yetu

- `Somo la AI kwa wanaoanza juu ya Mitandao ya Neural:` hii itakuwa data tunayoimarisha LLM yetu

- `Azure AI Search` na `Azure Cosmos DB:` hifadhidata za vector kuhifadhi data yetu na kuunda faharasa ya utafutaji

Watumiaji wataweza kuunda maswali ya mazoezi kutoka kwenye maelezo yao, kadi za muhtasari wa ukaguzi na kuyafupisha kuwa muhtasari mfupi. Ili kuanza, tuchunguze ni nini RAG na jinsi inavyofanya kazi:

## Kuzalishwa kwa Uboreshaji wa Upataji (RAG)

Chatbot inayotumia LLM huchakata maagizo ya mtumiaji ili kuzalisha majibu. Imesanifiwa kuwa mwingiliano na inashiriki na watumiaji katika mada mbalimbali. Hata hivyo, majibu yake yanategemea muktadha uliotolewa na data yake kabisa ya mafunzo. Kwa mfano, GPT-4 ilifikia maarifa hadi Septemba 2021, maana yake, haijui matukio yaliyotokea baada ya kipindi hicho. Zaidi ya hayo, data iliyotumika kufunza LLM hazijumuishi taarifa za siri kama maelezo ya binafsi au mwongozo wa bidhaa za kampuni.

### Jinsi RAG (Kuzalishwa kwa Uboreshaji wa Upataji) hufanya kazi

![mchoro unaoonyesha jinsi RAG hufanya kazi](../../../../../translated_images/sw/how-rag-works.f5d0ff63942bd3a6.webp)

Tuseme unataka kuweka chatbot inayounda maswali kutoka maelezo yako, utahitaji kiungo na msingi wa maarifa. Hapa ndipo RAG inakuja kusaidia. RAG hufanya kazi kama ifuatavyo:

- **Msingi wa maarifa:** Kabla ya upataji, nyaraka hizi zinahitaji kusindikwa na kuandaliwa, kawaida kwa kugawanya nyaraka kubwa vipande vidogo, kubadilisha kuwa embeddings za maandishi na kuziweka kwenye hifadhidata.

- **Swali la mtumiaji:** mtumiaji anauliza swali

- **Upataji:** Mtindo wa embedding unatafuta taarifa zinazohusiana kutoka kwenye msingi wa maarifa ili kutoa muktadha zaidi ambao utaingizwa kwenye ombi.

- **Kuzalisha Uboreshaji:** LLM huongeza jibu lake kulingana na data iliyopatikana. Hii inaruhusu jibu linalozalishwa si tu kutoka kwa data iliyofunzwa awali bali pia taarifa muhimu kutoka kwa muktadha uliowekwa. Data iliyorekodiwa hutumiwa kuboresha majibu ya LLM. LLM kisha hurudisha jibu la swali la mtumiaji.

![mchoro unaoonyesha usanifu wa RAG](../../../../../translated_images/sw/encoder-decode.f2658c25d0eadee2.webp)

Usanifu wa RAG umejengwa kwa kutumia transformers zinazojumuisha sehemu mbili: encoder na decoder. Kwa mfano, mtumiaji akiuliza swali, maandishi ya kuingilia 'hulishwa' kuwa vectors zinazoshikilia maana ya maneno na vector hizo 'hutafsiriwa' kwenye faharasa ya nyaraka na kuzalisha maandishi mapya kulingana na swali la mtumiaji. LLM hutumia modeli ya encoder-decoder kuzalisha matokeo.

Mbinu mbili za kutekeleza RAG kulingana na karatasi iliyopendekezwa: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) ni:

- **_RAG-Sequence_** kutumia nyaraka zilizopatikana kutabiri jibu bora zaidi kwa swali la mtumiaji

- **RAG-Token** kutumia nyaraka kuzalisha token inayofuata, kisha zitafute tena ili kujibu swali la mtumiaji

### Kwa nini utumie RAG? 

- **Utajiri wa taarifa:** huhakikisha majibu ya maandishi ni ya sasa na yanayolingana na wakati. Hivyo, huongeza ufanisi katika kazi maalum kwa kupata msingi wa maarifa ndani.

- Hupunguza ubunifu wa uwongo kwa kutumia **data inayothibitishwa** kwenye msingi wa maarifa kutoa muktadha kwa maswali ya watumiaji.

- Ni **gharama nafuu** kwani ni ya kiuchumi zaidi ikilinganishwa na kurekebisha LLM moja kwa moja

## Kuunda msingi wa maarifa

Programu yetu inategemea data binafsi ya somo la Mitandao ya Neural katika mtaala wa AI Kwa Waanza.

### Hifadhidata za Vector

Hifadhidata za vector, tofauti na hifadhidata za kawaida, ni hifadhidata maalum zilizoundwa kuhifadhi, kusimamia na kutafuta vectors zilizo embedded. Huhifadhi uwakilishi wa nambari wa nyaraka. Kugawanya data kuwa embeddings za nambari kunarahisisha mfumo wetu wa AI kuelewa na kusindika data.

Tunahifadhi embeddings zetu katika hifadhidata za vector kwani LLM zina kikomo cha idadi ya tokeni zinazoweza kupokewa kama ingizo. Kwa kuwa huwezi kutoa embeddings zote kwa LLM moja kwa moja, tutahitaji kuzivunja vipande vidogo na mtu anapouliza swali, embeddings zinazofanana zaidi na swali zitarudishwa pamoja na ombi. Kugawanya pia hupunguza gharama kwa idadi ya tokeni zinazopitishwa kwenye LLM.

Baadhi ya hifadhidata maarufu za vector ni pamoja na Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant na DeepLake. Unaweza kuunda modeli ya Azure Cosmos DB kwa kutumia Azure CLI kwa amri ifuatayo:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Kutoka maandishi hadi embeddings

Kabla ya kuhifadhi data yetu, tutahitaji kuibadilisha kuwa embeddings za vector kabla haijahifadhiwa kwenye hifadhidata. Ikiwa unafanya kazi na nyaraka kubwa au maandishi marefu, unaweza kuyagawanya kulingana na maswali unayotarajia. Kugawanya kunaweza kufanywa kwa kiwango cha sentensi, au kiwango cha aya. Kwa kuwa kugawanya kunachukua maana kutoka kwa maneno yanayozunguka, unaweza kuongeza muktadha fulani kwa kipande, kwa mfano, kwa kuongeza kichwa cha nyaraka au kujumuisha baadhi ya maandishi kabla au baada ya kipande. Unaweza kugawa data kama ifuatavyo:

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

    # Ikiwa kipande cha mwisho hakifikii urefu wa chini kabisa, ongeza hata hivyo
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Baada ya kugawanya, tunaweza kisha kuweka maandishi yetu kwa kutumia modeli tofauti za embedding. Baadhi ya modeli unaweza kutumia ni: word2vec, ada-002 na OpenAI, Azure Computer Vision na zingine nyingi. Kuchagua modeli kutategemea lugha unazozitumia, aina ya maudhui yaliyo encoded (maandishi/picha/sauti), ukubwa wa ingizo unaoweza kuweka encoded na urefu wa output ya embedding.

Mfano wa maandishi yaliyo embedded kwa kutumia modeli ya OpenAI `text-embedding-ada-002` ni:
![embedding ya neno paka](../../../../../translated_images/sw/cat.74cbd7946bc9ca38.webp)

## Upataji na Utafutaji wa Vector

Mtumiaji anapouliza swali, retriever hubadilisha swali kuwa vector kwa kutumia query encoder, kisha inatafuta kupitia faharasa yetu ya nyaraka vectors zinazohusiana katika nyaraka zinazohusiana na ingizo. Baada ya hapo, hubadilisha vector zote za ingizo na nyaraka kuwa maandishi na kuzipitisha kwenye LLM.

### Upataji

Upataji hutokea wakati mfumo unajaribu haraka kupata nyaraka kutoka kwenye faharasa zinazokidhi vigezo vya utafutaji. Lengo la retriever ni kupata nyaraka zitakazotumiwa kutoa muktadha na kuimarisha LLM kwenye data yako.

Kuna njia mbalimbali za kufanya utafutaji ndani ya hifadhidata kama:

- **Utafutaji kwa maneno muhimu** - hutumika kwa tafutaji la maandishi

- **Utafutaji wa Vector** - hubadilisha nyaraka kutoka maandishi hadi uwakilishi wa vector kwa kutumia modeli za embedding, kuruhusu **utafutaji wa kisemantiki** kwa maana ya maneno. Upataji utafanyika kwa kuuliza nyaraka ambazo vectors zao ndogo zaidi kwa swali la mtumiaji.

- **Mchanganyiko** - mchanganyiko wa utafutaji wa maneno muhimu na wa vector.

Changamoto ya upataji hutokea pale ambapo hakuna jibu linalofanana na swali kwenye hifadhidata, mfumo kisha utarudisha taarifa bora inayopatikana, lakini unaweza kutumia mbinu kama kuweka umbali wa juu zaidi wa umuhimu au kutumia utafutaji wa mchanganyiko unaojumuisha maneno muhimu na utafutaji wa vector. Katika somo hili tutatumia utafutaji wa mchanganyiko, mchanganyiko wa utafutaji wa vector na maneno muhimu. Tutahifadhi data zetu katika dataframe yenye safu zinazojumuisha vipande pamoja na embeddings.

### Ulinganifu wa Vector

Retriever atatafuta kwenye hifadhidata za maarifa embeddings ambazo ziko karibu, jirani sana, kwa kuwa ni maandishi yanayofanana. Katika tukio mtumiaji akiuliza swali, kwanza huwekwa embedding kisha kulinganishwa na embeddings zinazofanana. Kipimo cha kawaida kinachotumiwa kupima ulinganifu wa vectors tofauti ni cosine similarity ambayo inategemea pembe kati ya vectors mbili.

Tunaweza kupima ulinganifu kwa kutumia mbadala nyingine kama umbali wa Euclidean ambao ni mstari wa moja kwa moja kati ya nukta za mwisho za vector na dot product ambayo hupima jumla ya bidhaa za vipengele vinavyolingana vya vectors mbili.

### Faharasa ya utafutaji

Wakati wa upataji, tutahitaji kujenga faharasa ya utafutaji kwa msingi wa maarifa kabla ya kufanya utafutaji. Faharasa itahifadhi embeddings zetu na inaweza haraka kurudisha vipande vinavyofanana hata kwenye hifadhidata kubwa. Tunaweza kuunda faharasa letu kwa ndani kwa kutumia:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Tengeneza faharasa ya utafutaji
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Kuuliza faharasa, unaweza kutumia njia ya kneighbors
distances, indices = nbrs.kneighbors(embeddings)
```

### Kupangilia upya

Mara tu unapojaribu hifadhidata, unaweza kuhitaji kupangilia matokeo kutoka yale yanayofaa zaidi. Reranking LLM hutumia Machine Learning kuboresha umuhimu wa matokeo ya utafutaji kwa kuyaweka kutoka yanayofaa zaidi. Kutumia Azure AI Search, upangilishaji upya hufanywa kiotomatiki kwa kutumia semantic reranker. Mfano wa jinsi reranking inavyofanya kazi kwa kutumia majirani wa karibu:

```python
# Tafuta nyaraka zinazofanana zaidi
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Chapisha nyaraka zinazofanana zaidi
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Kuja pamoja na yote

Hatua ya mwisho ni kuongeza LLM yetu katika mchanganyiko ili kupata majibu yaliyoimarishwa kwa data yetu. Tunaweza kuitekeleza kama ifuatavyo:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Badilisha swali kuwa vekta ya maswali
    query_vector = create_embeddings(user_input)

    # Tafuta nyaraka zinazofanana zaidi
    distances, indices = nbrs.kneighbors([query_vector])

    # ongeza nyaraka kwenye swali ili kutoa muktadha
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # unganya historia na ingizo la mtumiaji
    history.append(user_input)

    # tengeneza kitu cha ujumbe
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # tumia ukamilishaji wa mazungumzo kuzalisha jibu
    response = openai.chat.completions.create(
        model="gpt-4",
        temperature=0.7,
        max_tokens=800,
        messages=messages
    )

    return response.choices[0].message

chatbot(user_input)
```

## Kutathmini programu yetu

### Vigezo vya Tathmini

- Ubora wa majibu yaliyotolewa kuhakikisha yanasikika kama ya asili, yananenelea kwa ufasaha na kama ya binadamu

- Kuimarishwa kwa data: kutathmini kama jibu lililotoka kwenye nyaraka zilizotolewa

- Umuhimu: kutathmini kama jibu linaendana na linahusiana na swali lililoulizwa

- Ufikiaji sahihi wa lugha - kama jibu linaeleweka kisarufi

## Matumizi ya kutumia RAG (Kuzalishwa kwa Uboreshaji wa Upataji) na hifadhidata za vector

Kuna matumizi mbalimbali ambapo miito ya kazi inaweza kuboresha programu yako kama vile:

- Maswali na Majibu: kuimarisha data ya kampuni yako kwa mazungumzo ambayo yanaweza kutumiwa na wafanyakazi kuuliza maswali.

- Mifumo ya Mapendekezo: ambapo unaweza kuunda mfumo unaolingana na thamani zinazofanana zaidi mfano, sinema, mikahawa na mengine mengi.

- Huduma za Chatbot: unaweza kuhifadhi historia ya mazungumzo na kubinafsisha mazungumzo kulingana na data ya mtumiaji.

- Utafutaji wa picha unaotegemea embeddings za vector, muhimu wakati wa kutambua picha na kugundua kasoro.

## Muhtasari

Tumefunika maeneo muhimu ya RAG kuanzia kuongeza data yetu kwenye programu, swali la mtumiaji na matokeo. Ili kurahisisha uundaji wa RAG, unaweza kutumia fremu kama Semanti Kernel, Langchain au Autogen.

## Kazi ya Nyumbani

Ili kuendelea na kujifunza kwa Kuzalishwa kwa Uboreshaji wa Upataji (RAG) unaweza kujenga:

- Jenga mbele kwa programu kwa kutumia fremu ya chaguo lako

- Tumia fremu, ama LangChain au Semantic Kernel, na uunde tena programu yako.

Hongera kwa kumaliza somo 👏.

## Kujifunza hakukomi hapa, endelea Safari

Baada ya kumaliza somo hili, angalia [Mkusanyiko wetu wa Kujifunza AI za Kizazi](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendeleza maarifa yako ya AI za Kizazi!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tangazo la Kukataa**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya mtaalamu wa binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri isiyo sahihi inayotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->