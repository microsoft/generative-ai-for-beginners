<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e2861bbca91c0567ef32bc77fe054f9e",
  "translation_date": "2025-06-25T22:42:43+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "sw"
}
-->
# Utoaji wa Kizazi Ulioboreshwa (RAG) na Mifumo ya Data ya Vector

Katika somo la programu za utafutaji, tulijifunza kwa ufupi jinsi ya kuunganisha data yako kwenye Mifumo Mikubwa ya Lugha (LLMs). Katika somo hili, tutachunguza zaidi dhana za kuimarisha data yako katika programu ya LLM, mbinu za mchakato na njia za kuhifadhi data, ikiwa ni pamoja na embeddings na maandishi.

## Utangulizi

Katika somo hili tutashughulikia yafuatayo:

- Utangulizi wa RAG, ni nini na kwa nini inatumika katika AI (akili bandia).

- Kuelewa mifumo ya data ya vector ni nini na kuunda moja kwa ajili ya programu yetu.

- Mfano wa vitendo juu ya jinsi ya kuunganisha RAG katika programu.

## Malengo ya Kujifunza

Baada ya kukamilisha somo hili, utaweza:

- Eleza umuhimu wa RAG katika upatikanaji wa data na usindikaji.

- Sanidi programu ya RAG na kuimarisha data yako kwa LLM.

- Muunganiko mzuri wa RAG na Mifumo ya Data ya Vector katika Programu za LLM.

## Hali Yetu: kuboresha LLMs zetu na data yetu wenyewe

Kwa somo hili, tunataka kuongeza maelezo yetu katika kampuni ya elimu, ambayo inaruhusu chatbot kupata maelezo zaidi kuhusu masomo tofauti. Kutumia maelezo tuliyo nayo, wanafunzi wataweza kusoma vizuri zaidi na kuelewa mada tofauti, kufanya iwe rahisi kukariri kwa mitihani yao. Ili kuunda hali yetu, tutatumia:

- LLM tutakayoyatumia kuunda chatbot yetu

- Data ambayo tutaimarisha LLM yetu

- Mifumo ya data ya vector kuhifadhi data yetu na kuunda index ya utafutaji

Watumiaji wataweza kuunda mazoezi ya quiz kutoka kwa maelezo yao, kadi za ukariri na kuisummarize kwa muhtasari mfupi. Ili kuanza, hebu tuangalie RAG ni nini na jinsi inavyofanya kazi:

## Utoaji wa Kizazi Ulioboreshwa (RAG)

Chatbot inayotumia LLM inasindika maoni ya mtumiaji ili kutoa majibu. Imeundwa kuwa ya maingiliano na inashughulika na watumiaji juu ya mada mbalimbali. Hata hivyo, majibu yake yanapunguzwa kwa muktadha uliotolewa na data yake ya mafunzo ya msingi. Kwa mfano, ukomo wa maarifa ya GPT-4 ni Septemba 2021, ikimaanisha, inakosa maarifa ya matukio ambayo yametokea baada ya kipindi hiki. Aidha, data iliyotumika kufundisha LLMs haijumuishi taarifa za siri kama maelezo ya kibinafsi au mwongozo wa bidhaa wa kampuni.

### Jinsi RAGs (Utoaji wa Kizazi Ulioboreshwa) unavyofanya kazi

Tuseme unataka kupeleka chatbot inayounda quiz kutoka kwa maelezo yako, utahitaji muunganisho kwa msingi wa maarifa. Hapa ndipo RAG inakuja kusaidia. RAGs hufanya kazi kama ifuatavyo:

- **Msingi wa maarifa:** Kabla ya upatikanaji, hati hizi zinahitaji kuingizwa na kusindika awali, kwa kawaida kuvunja hati kubwa kuwa vipande vidogo, kuzibadilisha kuwa embeddings za maandishi na kuzihifadhi katika mfumo wa data.

- **Swali la mtumiaji:** mtumiaji anauliza swali

- **Upatikanaji:** Wakati mtumiaji anauliza swali, mfano wa embedding unapata maelezo muhimu kutoka kwa msingi wetu wa maarifa ili kutoa muktadha zaidi ambao utaingizwa katika maoni.

- **Utoaji Ulioboreshwa:** LLM inaboresha jibu lake kulingana na data iliyopatikana. Inaruhusu jibu lililotolewa kuwa si tu kulingana na data iliyofundishwa awali bali pia maelezo muhimu kutoka kwa muktadha ulioongezwa. Data iliyopatikana inatumika kuongeza majibu ya LLM. LLM kisha inarudisha jibu kwa swali la mtumiaji.

## Kuunda msingi wa maarifa

Programu yetu inategemea data yetu binafsi yaani, somo la Neural Network katika mtaala wa AI Kwa Kompyuta.

### Mifumo ya Data ya Vector

Mfumo wa data ya vector, tofauti na mifumo ya data ya jadi, ni mfumo maalum ulioundwa kuhifadhi, kusimamia na kutafuta embeddings za vector. Inahifadhi uwakilishi wa nambari wa hati. Kuvunja data kuwa embeddings za nambari hufanya iwe rahisi kwa mfumo wetu wa AI kuelewa na kusindika data.

Tunatunza embeddings zetu katika mifumo ya data ya vector kwani LLMs zina ukomo wa idadi ya tokens wanazokubali kama ingizo. Kwa kuwa huwezi kupitisha embeddings zote kwa LLM, tutahitaji kuvunja vipande na wakati mtumiaji anauliza swali, embeddings zinazofanana zaidi na swali zitarudishwa pamoja na maoni. Kuvunja vipande pia kunapunguza gharama za idadi ya tokens zinazopitishwa kupitia LLM.

Mifumo ya data ya vector maarufu ni pamoja na Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant na DeepLake. Unaweza kuunda mfano wa Azure Cosmos DB kwa kutumia Azure CLI na amri ifuatayo:

### Kutoka maandishi hadi embeddings

Kabla ya kuhifadhi data yetu, tutahitaji kuibadilisha kuwa embeddings za vector kabla ya kuhifadhiwa katika mfumo wa data. Ikiwa unafanya kazi na hati kubwa au maandishi marefu, unaweza kuvunja vipande kulingana na maswali unayotarajia. Kuvunja vipande kunaweza kufanywa katika kiwango cha sentensi, au katika kiwango cha aya. Kwa kuwa kuvunja vipande kunatoa maana kutoka kwa maneno yaliyo karibu nayo, unaweza kuongeza muktadha mwingine kwa kipande, kwa mfano, kwa kuongeza kichwa cha hati au kujumuisha maandishi kabla au baada ya kipande. Unaweza kuvunja data kama ifuatavyo:

Mara baada ya kuvunja vipande, tunaweza kisha kuingiza maandishi yetu kwa kutumia mifano tofauti ya embedding. Baadhi ya mifano unayoweza kutumia ni: word2vec, ada-002 na OpenAI, Azure Computer Vision na mengine mengi. Kuchagua mfano wa kutumia kutategemea lugha unazotumia, aina ya maudhui yanayowekwa (maandishi/picha/sauti), ukubwa wa ingizo inaweza kuweka na urefu wa matokeo ya embedding.

Mfano wa maandishi yaliyoingizwa kwa kutumia mfano wa OpenAI `text-embedding-ada-002` ni:

## Upatikanaji na Utafutaji wa Vector

Wakati mtumiaji anauliza swali, retriever inabadilisha kuwa vector kwa kutumia encoder ya maswali, kisha inatafuta kupitia index ya utafutaji wa hati kwa vectors muhimu katika hati ambazo zinahusiana na ingizo. Mara baada ya kumaliza, inabadilisha vector ya ingizo na vectors za hati kuwa maandishi na kuipitisha kupitia LLM.

### Upatikanaji

Upatikanaji hutokea wakati mfumo unajaribu haraka kupata hati kutoka index ambazo zinakidhi vigezo vya utafutaji. Lengo la retriever ni kupata hati ambazo zitatumika kutoa muktadha na kuimarisha LLM kwenye data yako.

Kuna njia kadhaa za kufanya utafutaji ndani ya mfumo wetu wa data kama:

- **Utafutaji wa maneno** - hutumika kwa utafutaji wa maandishi

- **Utafutaji wa semantiki** - hutumia maana ya semantiki ya maneno

- **Utafutaji wa vector** - hubadilisha hati kutoka maandishi hadi uwakilishi wa vector kwa kutumia mifano ya embedding. Upatikanaji utafanywa kwa kuuliza hati ambazo uwakilishi wa vector ziko karibu zaidi na swali la mtumiaji.

- **Mseto** - mchanganyiko wa utafutaji wa maneno na vector.

Changamoto na upatikanaji inakuja wakati hakuna jibu linalofanana na swali katika mfumo wa data, mfumo utarudisha maelezo bora wanayoweza kupata, hata hivyo, unaweza kutumia mbinu kama kuweka umbali wa juu kwa umuhimu au kutumia utafutaji mseto unaochanganya maneno na utafutaji wa vector. Katika somo hili tutatumia utafutaji mseto, mchanganyiko wa utafutaji wa vector na maneno. Tutahifadhi data yetu kwenye dataframe na safu zilizo na vipande pamoja na embeddings.

### Ufanano wa Vector

Retriever itatafuta kupitia msingi wa maarifa kwa embeddings ambazo ziko karibu, jirani wa karibu zaidi, kwani ni maandishi ambayo ni sawa. Katika hali ambapo mtumiaji anauliza swali, kwanza linaingizwa kisha linapatana na embeddings zinazofanana. Kipimo cha kawaida kinachotumika kutafuta jinsi vectors tofauti zilivyo sawa ni ufanano wa cosine ambao unategemea pembe kati ya vectors mbili.

Tunaweza kupima ufanano kwa kutumia njia mbadala nyingine tunazoweza kutumia ni umbali wa Euclidean ambao ni mstari wa moja kwa moja kati ya mwisho wa vector na bidhaa ya nukta ambayo hupima jumla ya bidhaa za vipengele vinavyolingana vya vectors mbili.

### Index ya Utafutaji

Wakati wa kufanya upatikanaji, tutahitaji kujenga index ya utafutaji kwa msingi wetu wa maarifa kabla ya kufanya utafutaji. Index itahifadhi embeddings zetu na inaweza haraka kupata vipande vilivyo sawa hata katika mfumo wa data kubwa. Tunaweza kuunda index yetu ndani kwa kutumia:

### Kuweka upya

Mara baada ya kuuliza mfumo wa data, unaweza kuhitaji kupanga matokeo kutoka kwa yale yanayofaa zaidi. LLM ya kuweka upya hutumia Machine Learning kuboresha umuhimu wa matokeo ya utafutaji kwa kuyapanga kutoka kwa yale yanayofaa zaidi. Kutumia Azure AI Search, kuweka upya kunafanywa kiotomatiki kwa kutumia mpangilio wa semantiki. Mfano wa jinsi kuweka upya kunavyofanya kazi kwa kutumia majirani wa karibu:

## Kuleta yote pamoja

Hatua ya mwisho ni kuongeza LLM yetu katika mchanganyiko ili kuweza kupata majibu ambayo yameimarishwa kwenye data yetu. Tunaweza kuitekeleza kama ifuatavyo:

## Kutathmini programu yetu

### Viwango vya Tathmini

- Ubora wa majibu yaliyotolewa kuhakikisha inasikika kwa asili, kwa ufasaha na kama binadamu

- Uimarishaji wa data: kutathmini kama jibu lililotoka kwa hati zilizotolewa

- Umuhimu: kutathmini jibu linalingana na linahusiana na swali lililoulizwa

- Ufasaha - kama jibu lina mantiki kisarufi

## Matumizi ya kutumia RAG (Utoaji wa Kizazi Ulioboreshwa) na mifumo ya data ya vector

Kuna matumizi mengi tofauti ambapo miito ya kazi inaweza kuboresha programu yako kama:

- Swali na Kujibu: kuimarisha data ya kampuni yako kwa mazungumzo ambayo yanaweza kutumiwa na wafanyakazi kuuliza maswali.

- Mifumo ya Mapendekezo: ambapo unaweza kuunda mfumo unaolingana na maadili yanayofanana zaidi mfano, filamu, mikahawa na mengine mengi.

- Huduma za Chatbot: unaweza kuhifadhi historia ya mazungumzo na kubinafsisha mazungumzo kulingana na data ya mtumiaji.

- Utafutaji wa picha kulingana na embeddings za vector, muhimu wakati wa kufanya utambuzi wa picha na kugundua hali zisizo za kawaida.

## Muhtasari

Tumeshughulikia maeneo ya msingi ya RAG kutoka kuongeza data yetu kwenye programu, swali la mtumiaji na matokeo. Ili kurahisisha uundaji wa RAG, unaweza kutumia mifumo kama Semanti Kernel, Langchain au Autogen.

## Kazi

Kuendelea kujifunza Utoaji wa Kizazi Ulioboreshwa (RAG) unaweza kujenga:

- Jenga sehemu ya mbele ya programu kwa kutumia mfumo wa chaguo lako

- Tumia mfumo, aidha LangChain au Semantic Kernel, na upya programu yako.

Hongera kwa kukamilisha somo 👏.

## Kujifunza hakuishii hapa, endelea na Safari

Baada ya kukamilisha somo hili, angalia [Mkusanyiko wa Kujifunza AI Inayozalisha](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuongeza maarifa yako ya AI Inayozalisha!

**Kanusho**: 
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatuwajibiki kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.