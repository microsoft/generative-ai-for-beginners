<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e2861bbca91c0567ef32bc77fe054f9e",
  "translation_date": "2025-05-20T01:38:54+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "sw"
}
-->
# Uzalishaji Ulioongezwa wa Urejelezaji (RAG) na Hifadhidata za Vector

Katika somo la programu za utafutaji, tulijifunza kwa ufupi jinsi ya kuunganisha data yako kwenye Mifano Mikubwa ya Lugha (LLMs). Katika somo hili, tutachunguza zaidi dhana za kuweka data yako kwenye programu ya LLM, mbinu za mchakato huo na njia za kuhifadhi data, ikiwa ni pamoja na embeddings na maandishi.

> **Video Inakuja Hivi Karibuni**

## Utangulizi

Katika somo hili tutashughulikia yafuatayo:

- Utangulizi wa RAG, ni nini na kwa nini inatumika katika AI (akili bandia).

- Kuelewa hifadhidata za vector ni nini na kuunda moja kwa programu yetu.

- Mfano wa vitendo wa jinsi ya kuunganisha RAG kwenye programu.

## Malengo ya Kujifunza

Baada ya kukamilisha somo hili, utaweza:

- Kuelezea umuhimu wa RAG katika urejelezaji na usindikaji wa data.

- Kuseti programu ya RAG na kuweka data yako kwenye LLM

- Uunganishaji mzuri wa RAG na Hifadhidata za Vector katika Programu za LLM.

## Hali Yetu: kuboresha LLM zetu na data yetu wenyewe

Kwa somo hili, tunataka kuongeza maelezo yetu wenyewe kwenye kampuni ya elimu, ambayo inaruhusu chatbot kupata maelezo zaidi kuhusu masomo mbalimbali. Kwa kutumia maelezo tuliyonayo, wanafunzi wataweza kusoma vizuri na kuelewa mada tofauti, na hivyo kufanya iwe rahisi kufanya mapitio ya mitihani yao. Ili kuunda hali yetu, tutatumia:

- `Azure OpenAI:` LLM tutakayotumia kuunda chatbot yetu

- `AI for beginners' lesson on Neural Networks`: hii itakuwa data tutakayoweka kwenye LLM yetu

- `Azure AI Search` na `Azure Cosmos DB:` hifadhidata za vector kuhifadhi data yetu na kuunda index ya utafutaji

Watumiaji wataweza kuunda majaribio ya mazoezi kutoka kwa maelezo yao, kadi za mapitio na kuyafupisha kwa muhtasari mfupi. Ili kuanza, hebu tuangalie RAG ni nini na jinsi inavyofanya kazi:

## Uzalishaji Ulioongezwa wa Urejelezaji (RAG)

Chatbot inayotumia LLM inachakata maelekezo ya mtumiaji ili kutoa majibu. Imeundwa kuwa shirikishi na inashughulika na watumiaji katika mada mbalimbali. Hata hivyo, majibu yake yanategemea muktadha uliotolewa na data yake ya mafunzo ya msingi. Kwa mfano, ukomo wa maarifa ya GPT-4 ni Septemba 2021, ikimaanisha haina maarifa ya matukio yaliyotokea baada ya kipindi hiki. Zaidi ya hayo, data inayotumika kufundisha LLMs inakosa taarifa za siri kama vile maelezo binafsi au mwongozo wa bidhaa wa kampuni.

### Jinsi RAGs (Uzalishaji Ulioongezwa wa Urejelezaji) zinavyofanya kazi

Fikiria unataka kutumia chatbot inayounda majaribio kutoka kwa maelezo yako, utahitaji muunganisho na msingi wa maarifa. Hapa ndipo RAG inakuja kuokoa. RAGs zinafanya kazi kama ifuatavyo:

- **Msingi wa maarifa:** Kabla ya urejelezaji, nyaraka hizi zinahitaji kusomwa na kusindika, kawaida kuvunja nyaraka kubwa kuwa vipande vidogo, kuzibadilisha kuwa embedding za maandishi na kuzihifadhi kwenye hifadhidata.

- **Swali la Mtumiaji:** mtumiaji anauliza swali

- **Urejelezaji:** Mtumiaji anapouliza swali, mfano wa embedding unarejelea taarifa husika kutoka kwenye msingi wetu wa maarifa ili kutoa muktadha zaidi utakaounganishwa kwenye mwongozo.

- **Uzalishaji Ulioongezwa:** LLM inaboresha jibu lake kulingana na data iliyorejelezwa. Inaruhusu jibu lililotolewa kuwa si tu kwa data ya awali iliyofundishwa bali pia taarifa husika kutoka kwenye muktadha ulioongezwa. Data iliyorejelezwa inatumika kuongeza majibu ya LLM. LLM kisha inarejesha jibu kwa swali la mtumiaji.

Muundo wa RAGs unatekelezwa kwa kutumia transformers zinazojumuisha sehemu mbili: encoder na decoder. Kwa mfano, mtumiaji anapouliza swali, maandishi ya ingizo 'yanakodishwa' kuwa vectors zinazokamata maana ya maneno na vectors zinakodolewa' katika index ya nyaraka zetu na kuzalisha maandishi mapya kulingana na swali la mtumiaji. LLM hutumia mfano wa encoder-decoder kutoa matokeo.

Mbinu mbili wakati wa kutekeleza RAG kulingana na karatasi iliyopendekezwa: [Uzalishaji Ulioongezwa wa Urejelezaji kwa Kazi za NLP (programu ya usindikaji wa lugha asilia) za maarifa ya kina](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) ni:

- **_RAG-Sequence_** kutumia nyaraka zilizorejelezwa kutabiri jibu bora linalowezekana kwa swali la mtumiaji

- **RAG-Token** kutumia nyaraka kuzalisha tokeni inayofuata, kisha kuzirejelea kujibu swali la mtumiaji

### Kwa nini utumie RAGs?

- **Utajiri wa taarifa:** inahakikisha majibu ya maandishi ni ya kisasa na ya sasa. Kwa hivyo, inaboresha utendaji kwenye kazi maalum za kikoa kwa kufikia msingi wa maarifa wa ndani.

- Inapunguza utengenezaji kwa kutumia **data inayothibitishwa** kwenye msingi wa maarifa kutoa muktadha kwa maswali ya mtumiaji.

- Ni **gharama nafuu** kwani ni ya kiuchumi zaidi ikilinganishwa na kurekebisha LLM

## Kuunda msingi wa maarifa

Programu yetu inategemea data yetu binafsi yaani, somo la Mtandao wa Neural kwenye mtaala wa AI Kwa Kompyuta.

### Hifadhidata za Vector

Hifadhidata ya vector, tofauti na hifadhidata za jadi, ni hifadhidata maalum iliyoundwa kuhifadhi, kusimamia na kutafuta vectors zilizowekwa. Inahifadhi uwakilishi wa nambari za nyaraka. Kuvunja data kuwa embeddings za nambari kunarahisisha mfumo wetu wa AI kuelewa na kusindika data.

Tunatunza embeddings zetu kwenye hifadhidata za vector kwani LLMs zina kikomo cha idadi ya tokeni wanazokubali kama ingizo. Kwa kuwa huwezi kupitisha embeddings zote kwa LLM, tutahitaji kuzivunja vipande na mtumiaji anapouliza swali, embeddings zinazofanana zaidi na swali zitarudishwa pamoja na mwongozo. Kuvunja pia kunapunguza gharama za idadi ya tokeni zinazopitishwa kupitia LLM.

Baadhi ya hifadhidata maarufu za vector ni pamoja na Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant na DeepLake. Unaweza kuunda mfano wa Azure Cosmos DB kwa kutumia Azure CLI na amri ifuatayo:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Kutoka maandishi hadi embeddings

Kabla ya kuhifadhi data yetu, tutahitaji kuibadilisha kuwa embeddings za vector kabla ya kuhifadhiwa kwenye hifadhidata. Ikiwa unafanya kazi na nyaraka kubwa au maandishi marefu, unaweza kuyavunja kulingana na maswali unayotarajia. Kuvunja kunaweza kufanywa katika kiwango cha sentensi, au katika kiwango cha aya. Kwa kuwa kuvunja kunatokana na maana kutoka kwa maneno yanayozunguka, unaweza kuongeza muktadha mwingine kwenye kipande, kwa mfano, kwa kuongeza kichwa cha nyaraka au kujumuisha maandishi kabla au baada ya kipande. Unaweza kuvunja data kama ifuatavyo:

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

Mara baada ya kuvunjwa, tunaweza kisha kuweka maandishi yetu kwa kutumia mifano tofauti ya embedding. Baadhi ya mifano unayoweza kutumia ni pamoja na: word2vec, ada-002 na OpenAI, Azure Computer Vision na mengine mengi. Kuchagua mfano wa kutumia kutategemea lugha unazotumia, aina ya maudhui yaliyowekwa (maandishi/picha/sauti), saizi ya ingizo inayoweza kuwekwa na urefu wa matokeo ya embedding.

Mfano wa maandishi yaliyowekwa kwa kutumia mfano wa OpenAI `text-embedding-ada-002` ni:

## Urejelezaji na Utafutaji wa Vector

Mtumiaji anapouliza swali, urejelezaji unalibadilisha kuwa vector kwa kutumia encoder ya swali, kisha inatafuta kupitia index yetu ya utafutaji wa nyaraka kwa vectors husika katika nyaraka zinazohusiana na ingizo. Mara imekamilika, inabadilisha vector ya ingizo na vectors za nyaraka kuwa maandishi na kuyapitisha kupitia LLM.

### Urejelezaji

Urejelezaji hufanyika wakati mfumo unajaribu haraka kupata nyaraka kutoka kwenye index zinazokidhi vigezo vya utafutaji. Lengo la urejelezaji ni kupata nyaraka ambazo zitatumika kutoa muktadha na kuweka LLM kwenye data yako.

Kuna njia kadhaa za kufanya utafutaji ndani ya hifadhidata yetu kama:

- **Utafutaji wa maneno muhimu** - hutumika kwa utafutaji wa maandishi

- **Utafutaji wa semantiki** - hutumia maana ya semantiki ya maneno

- **Utafutaji wa vector** - hubadilisha nyaraka kutoka maandishi kuwa uwakilishi wa vector kwa kutumia mifano ya embedding. Urejelezaji utafanywa kwa kuuliza nyaraka ambazo uwakilishi wa vector ni karibu na swali la mtumiaji.

- **Mseto** - mchanganyiko wa utafutaji wa maneno muhimu na vector.

Changamoto na urejelezaji huja wakati hakuna jibu linalofanana na swali kwenye hifadhidata, mfumo kisha utarejesha taarifa bora wanayoweza kupata, hata hivyo, unaweza kutumia mbinu kama kuweka umbali wa juu kwa umuhimu au kutumia utafutaji mseto unaounganisha maneno muhimu na utafutaji wa vector. Katika somo hili tutatumia utafutaji mseto, mchanganyiko wa utafutaji wa vector na maneno muhimu. Tutahifadhi data yetu kwenye dataframe na safu zilizo na vipande pamoja na embeddings.

### Ufanano wa Vector

Urejelezaji utatafuta kupitia hifadhidata ya maarifa kwa embeddings ambazo ziko karibu, jirani ya karibu, kwani ni maandishi yanayofanana. Katika hali ambayo mtumiaji anauliza swali, kwanza linawekwa kisha linafananishwa na embeddings zinazofanana. Kipimo cha kawaida kinachotumika kupata jinsi vectors tofauti zinavyofanana ni ufanano wa cosine ambao unategemea pembe kati ya vectors mbili.

Tunaweza kupima ufanano kwa kutumia mbadala mwingine tunaoweza kutumia ni umbali wa Euclidean ambao ni mstari wa moja kwa moja kati ya mwisho wa vectors na bidhaa ya nukta ambayo hupima jumla ya bidhaa za vipengele vya vectors mbili.

### Index ya Utafutaji

Wakati wa kufanya urejelezaji, tutahitaji kujenga index ya utafutaji kwa msingi wetu wa maarifa kabla ya kufanya utafutaji. Index itahifadhi embeddings zetu na inaweza kurejea haraka vipande vinavyofanana zaidi hata katika hifadhidata kubwa. Tunaweza kuunda index yetu kwa ndani kwa kutumia:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Kupanga upya

Mara baada ya kuuliza hifadhidata, unaweza kuhitaji kupanga matokeo kutoka kwa yale muhimu zaidi. LLM inayopanga upya hutumia Kujifunza kwa Mashine kuboresha umuhimu wa matokeo ya utafutaji kwa kuyapanga kutoka kwa yale muhimu zaidi. Kwa kutumia Azure AI Search, kupanga upya kunafanywa kiotomatiki kwako kwa kutumia mpangaji wa semantiki. Mfano wa jinsi kupanga upya kunavyofanya kazi kwa kutumia majirani wa karibu zaidi:

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

## Kuweka Yote Pamoja

Hatua ya mwisho ni kuongeza LLM yetu kwenye mchanganyiko ili tuweze kupata majibu ambayo yamewekwa kwenye data yetu. Tunaweza kuitekeleza kama ifuatavyo:

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

## Kutathmini Programu Yetu

### Viwango vya Tathmini

- Ubora wa majibu yaliyotolewa kuhakikisha inasikika kwa kawaida, kwa ufasaha na kama ya kibinadamu

- Uwekaji wa data: kutathmini kama jibu lililotoka kwa nyaraka zilizotolewa

- Umuhimu: kutathmini jibu linafanana na linahusiana na swali lililoulizwa

- Ufasaha - kama jibu lina mantiki kisarufi

## Matumizi ya RAG (Uzalishaji Ulioongezwa wa Urejelezaji) na hifadhidata za vector

Kuna matumizi mengi tofauti ambapo miito ya kazi inaweza kuboresha programu yako kama:

- Maswali na Majibu: kuweka data ya kampuni yako kwenye chat inayoweza kutumiwa na wafanyakazi kuuliza maswali.

- Mifumo ya Mapendekezo: ambapo unaweza kuunda mfumo unaolingana na maadili yanayofanana zaidi mfano filamu, mikahawa na mengi zaidi.

- Huduma za Chatbot: unaweza kuhifadhi historia ya mazungumzo na kubinafsisha mazungumzo kulingana na data ya mtumiaji.

- Utafutaji wa picha kulingana na embeddings za vector, muhimu wakati wa kutambua picha na kugundua hitilafu.

## Muhtasari

Tumeshughulikia maeneo ya msingi ya RAG kutoka kuongeza data yetu kwenye programu, swali la mtumiaji na matokeo. Ili kurahisisha uundaji wa RAG, unaweza kutumia mifumo kama Semanti Kernel, Langchain au Autogen.

## Kazi

Ili kuendelea kujifunza kwako kuhusu Uzalishaji Ulioongezwa wa Urejelezaji (RAG) unaweza kujenga:

- Jenga sehemu ya mbele kwa programu kwa kutumia mfumo wa chaguo lako

- Tumia mfumo, ama LangChain au Semantic Kernel, na uunde upya programu yako.

Hongera kwa kumaliza somo 👏.

## Kujifunza hakuishii hapa, endelea na Safari

Baada ya kukamilisha somo hili, angalia [Mkusanyiko wetu wa Kujifunza AI Inayozalisha](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuongeza maarifa yako ya AI Inayozalisha!

**Kanusho**: 
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asilia katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo chenye mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatuwajibiki kwa kutokuelewana au tafsiri zisizo sahihi zinazoibuka kutokana na matumizi ya tafsiri hii.