# Retrieval Augmented Generation (RAG) at Mga Vector Database

[![Retrieval Augmented Generation (RAG) at Mga Vector Database](../../../translated_images/tl/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Sa aralin tungkol sa mga aplikasyon ng paghahanap, bahagya nating natutunan kung paano isama ang iyong sariling data sa Malalaking Language Models (LLMs). Sa araling ito, hihimayin pa natin ang mga konsepto ng pag-ground ng iyong data sa iyong aplikasyon ng LLM, ang mekaniks ng proseso, at mga pamamaraan para sa pag-iimbak ng data, kabilang ang mga embeddings at teksto.

> **Malapit nang Ilabas ang Video**

## Panimula

Sa araling ito, tatalakayin natin ang mga sumusunod:

- Isang panimula sa RAG, kung ano ito at bakit ito ginagamit sa AI (artificial intelligence).

- Pag-unawa kung ano ang mga vector database at paggawa ng isa para sa ating aplikasyon.

- Isang praktikal na halimbawa kung paano isasama ang RAG sa isang aplikasyon.

## Mga Layunin sa Pagkatuto

Pagkatapos makumpleto ang araling ito, magagawa mong:

- Ipaliwanag ang kahalagahan ng RAG sa pagkuha at pagproseso ng data.

- I-set up ang aplikasyon ng RAG at i-ground ang iyong data sa isang LLM

- Mabisang pagsasama ng RAG at Mga Vector Database sa Mga Aplikasyon ng LLM.

## Ang Ating Senaryo: pagpapahusay ng ating mga LLM gamit ang sariling data

Para sa araling ito, nais nating idagdag ang sariling mga tala sa edukasyong startup, na nagpapahintulot sa chatbot na makakuha ng mas maraming impormasyon tungkol sa iba't ibang paksa. Gamit ang mga tala na mayroon tayo, mas mapag-aaralan ng mga mag-aaral nang mas mabuti at maiintindihan ang iba't ibang paksa, na nagpapadali ng pag-uulit para sa kanilang mga pagsusulit. Para likhain ang ating senaryo, gagamitin natin ang:

- `Azure OpenAI:` ang LLM na gagamitin natin para likhain ang chatbot

- `Aralin ng AI para sa mga baguhan sa Neural Networks` : ito ang magiging data na pag-uugatang ng ating LLM

- `Azure AI Search` at `Azure Cosmos DB:` vector database para itago ang ating data at gumawa ng search index

Magagawa ng mga user na gumawa ng mga practice quiz mula sa kanilang mga tala, revision flash cards at buodin ito sa mga maigsi at kontekstuwal na buod. Upang magsimula, tingnan muna natin kung ano ang RAG at paano ito gumagana:

## Retrieval Augmented Generation (RAG)

Ang chatbot na pinalakas ng LLM ay nagpoproseso ng mga prompt ng user upang bumuo ng mga sagot. Ito ay dinisenyo upang maging interactive at nakikipag-ugnayan sa mga user sa malawak na hanay ng mga paksa. Gayunpaman, ang mga sagot nito ay limitado sa kontekstong ibinigay at batay sa pundasyong data ng pagsasanay. Halimbawa, ang cutoff ng kaalaman ng GPT-4 ay Setyembre 2021, nangangahulugang kulang ito sa kaalaman tungkol sa mga pangyayaring naganap pagkatapos ng panahong iyon. Bukod dito, ang data na ginamit para sanayin ang mga LLM ay hindi kasama ang mga kumpidensyal na impormasyon tulad ng personal na mga tala o manu-manong gamit ng kumpanya.

### Paano Gumagana ang mga RAG (Retrieval Augmented Generation)

![drawing showing how RAGs work](../../../translated_images/tl/how-rag-works.f5d0ff63942bd3a6.webp)

Ipagpalagay na nais mong mag-deploy ng chatbot na lumilikha ng mga quiz mula sa iyong mga tala, kakailanganin mo ng koneksyon sa knowledge base. Dito pumapasok ang RAG bilang solusyon. Ang mga RAG ay gumagana sa mga sumusunod:

- **Knowledge base:** Bago ang retrieval, kailangang ma-ingest at ma-preprocess ang mga dokumentong ito, karaniwang hinahati ang malalaking dokumento sa mas maliliit na bahagi, binabago ito sa text embedding at iniimbak sa database.

- **User Query:** nagtatanong ang user ng isang katanungan

- **Retrieval:** Kapag may tanong ang user, kinukuha ng embedding model ang kaugnay na impormasyon mula sa ating knowledge base upang magbigay ng karagdagang konteksto na isasama sa prompt.

- **Augmented Generation:** pinahusay ng LLM ang sagot nito base sa nakuhang data. Pinapayagan nito na ang sagot na mabubuo ay hindi lamang batay sa pre-trained na data kundi pati na rin sa relevanteng impormasyon mula sa dagdag na konteksto. Ginagamit ang nakuha na data upang dagdagan ang mga sagot ng LLM. Pagkatapos, ibinabalik ng LLM ang sagot sa tanong ng user.

![drawing showing how RAGs architecture](../../../translated_images/tl/encoder-decode.f2658c25d0eadee2.webp)

Ang arkitektura ng mga RAG ay ipinatutupad gamit ang transformers na binubuo ng dalawang bahagi: isang encoder at isang decoder. Halimbawa, kapag nagtatanong ang user, ang input na teksto ay ‘encoded’ sa mga vector na kumakatawan sa kahulugan ng mga salita at ang mga vector ay ‘decoded’ sa index ng dokumento at bumubuo ng bagong teksto base sa tanong ng user. Ginagamit ng LLM ang parehong encoder-decoder model para bumuo ng output.

Dalawang pamamaraan sa pagpapatupad ng RAG ayon sa inilahad na papel: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) ay:

- **_RAG-Sequence_** gamit ang nakuha na dokumento upang hulaan ang pinakamahusay na posibleng sagot sa tanong ng user

- **RAG-Token** gamit ang mga dokumento upang bumuo ng susunod na token, pagkatapos ay kunin ang mga ito upang sagutin ang tanong ng user

### Bakit gagamit ng RAG? 

- **Yamang impormasyon:** tinitiyak na ang mga sagot na teksto ay napapanahon at kasalukuyan. Pinapahusay nito ang performans sa mga domain specific tasks sa pamamagitan ng pag-access sa internal na knowledge base.

- Binabawasan ang paggawa ng imbento sa pamamagitan ng paggamit ng **mapapatunayang data** sa knowledge base upang magbigay ng konteksto sa mga tanong ng user.

- Ito ay **matiwasay na gastusin** dahil mas mura ito kumpara sa pag-fine tune ng LLM.

## Paggawa ng knowledge base

Ang ating aplikasyon ay batay sa ating personal na data i.e., ang Aralin sa Neural Network sa kurikulum ng AI Para sa Mga Baguhan.

### Mga Vector Database

Ang vector database, hindi tulad ng mga tradisyunal na database, ay isang espesyal na database na disenyo para mag-imbak, mag-manage at maghanap ng embedded vectors. Iniimbak nito ang numerikal na representasyon ng mga dokumento. Ang paghahati ng data sa mga numerikal na embedding ay nagpapadali para sa ating AI system na maunawaan at maproseso ang data.

Iniimbak natin ang ating mga embedding sa vector database dahil may limitasyon ang mga LLM sa bilang ng mga token na tinatanggap bilang input. Dahil hindi mo maipapasa ang buong embedding sa isang LLM, kailangan nating hatiin ito sa mga bahagi at kapag nagtatanong ang user, ibabalik ang mga embedding na pinaka-akma sa tanong kasama ang prompt. Nakakatulong din ang paghahati upang mabawasan ang gastos sa bilang ng token na ipinapadaan sa LLM.

Ilan sa mga kilalang vector database ay ang Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant at DeepLake. Maaari kang gumawa ng Azure Cosmos DB model gamit ang Azure CLI sa pamamagitan ng sumusunod na utos:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Mula sa teksto patungo sa embeddings

Bago tayo mag-imbak ng data, kailangan muna itong i-convert sa vector embeddings bago ito maiimbak sa database. Kung nagtatrabaho ka sa malalaki o mahahabang teksto, maaari mong hatiin ito ayon sa mga tanong na inaasahan mo. Maaaring hatiin ang mga ito sa antas ng pangungusap o talata. Dahil ang paghahati ay nagmula sa kahulugan ng mga salita sa paligid, maaari kang magdagdag ng iba pang konteksto sa isang chunk, halimbawa, sa pamamagitan ng pagdagdag ng pamagat ng dokumento o paglakip ng ilang teksto bago o pagkatapos ng chunk. Maaari mong hatiin ang data tulad ng sumusunod:

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

    # Kung ang huling bahagi ay hindi umabot sa pinakamababang haba, idagdag pa rin ito
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Kapag nahati na, maaari nating i-embed ang ating teksto gamit ang iba't ibang embedding model. Ilan sa mga modelong maaaring gamitin ay: word2vec, ada-002 ng OpenAI, Azure Computer Vision at marami pang iba. Ang pagpili ng modelong gagamitin ay depende sa wika na ginagamit mo, uri ng content (teksto/larawan/audio), laki ng input na kaya nitong i-encode at haba ng embedding output.

Isang halimbawa ng naka-embed na teksto gamit ang OpenAI na `text-embedding-ada-002` na modelo ay:
![an embedding of the word cat](../../../translated_images/tl/cat.74cbd7946bc9ca38.webp)

## Pagkuha at Paghahanap gamit ang Vector

Kapag nagtatanong ang user, ini-transform ng retriever ito sa vector gamit ang query encoder, pagkatapos ay hahanapin nito sa dokumento sa index ng paghahanap ang mga vector na may kaugnayan sa input. Kapag tapos na, iko-convert nito parehong ang input vector at mga document vector sa teksto at ipapasa ito sa LLM.

### Pagkuha (Retrieval)

Nangyayari ang retrieval kapag sinusubukan ng sistema na mabilis mahanap ang mga dokumento mula sa index na tumutugma sa criteria ng paghahanap. Layunin ng retriever na makuha ang mga dokumento na gagamitin upang magbigay ng konteksto at i-ground ang LLM sa iyong data.

Mayroong ilang paraan upang magsagawa ng paghahanap sa ating database katulad ng:

- **Keyword search** - ginagamit para sa paghahanap sa teksto

- **Vector search** - nagko-convert ng mga dokumento mula sa teksto patungong vector representations gamit ang embedding models, na nagpapahintulot ng **semantic search** gamit ang kahulugan ng mga salita. Ang retrieval ay gagawin sa pamamagitan ng pag-query sa mga dokumentong ang vector representation ay pinakamalapit sa tanong ng user.

- **Hybrid** - kumbinasyon ng keyword at vector search.

Isang hamon sa retrieval ay kapag walang kaparehong sagot sa query sa database, ibabalik ng sistema ang pinakamainam na impormasyong nakuha, subalit maaaring gumamit ng mga taktika tulad ng pagtatakda ng maximum distance para sa relevance o paggamit ng hybrid search na pinagsasama ang keyword at vector search. Sa araling ito gagamit tayo ng hybrid search, isang kumbinasyon ng vector at keyword search. Iimbak natin ang data sa isang dataframe na may mga kolum para sa mga chunks kasama ang embedding.

### Vector Similarity

Hahanapin ng retriever sa knowledge database ang mga embedding na magkalapit, ang pinakamalapit na kapitbahay, dahil ito ay mga teksto na magkatulad. Kapag nagtanong ang user, unang ni-embed ito at pagkatapos ay tinutugma sa mga magkaparehong embedding. Ang karaniwang sukat na ginagamit upang matukoy kung gaano kasimilar ang dalawang vector ay cosine similarity na batay sa anggulo sa pagitan ng dalawang vector.

Maaari rin nating sukatin ang similarity gamit ang ibang alternatibo katulad ng Euclidean distance na siyang tuwid na linya sa pagitan ng mga dulo ng vector at dot product na sumusukat sa kabuuan ng produkto ng mga kaugnay na elemento ng dalawang vector.

### Search index

Kapag gumagawa ng retrieval, kailangan nating bumuo ng search index para sa knowledge base bago tayo magsagawa ng paghahanap. Ang isang index ay nagsasave ng ating mga embedding at mabilis na nakakakuha ng mga pinaka-magkaparehong chunks kahit sa malalaking database. Maaari nating gawin ang ating index nang lokal gamit ang:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Lumikha ng search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Upang mag-query sa index, maaari mong gamitin ang kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Pag-re-rank

Kapag nag-query ka sa database, maaaring kailanganin mong isalansan ang mga resulta mula sa pinaka-kaugnay. Ang isang reranking LLM ay gumagamit ng Machine Learning upang pagandahin ang kaugnayan ng mga resulta ng paghahanap sa pamamagitan ng pagsasaayos mula sa pinaka-kaugnay. Sa paggamit ng Azure AI Search, awtomatikong ginagawa ang reranking gamit ang semantic reranker. Halimbawa ng pag-re-rank gamit ang nearest neighbours:

```python
# Hanapin ang mga pinakaparehong dokumento
distances, indices = nbrs.kneighbors([query_vector])

index = []
# I-print ang mga pinakaparehong dokumento
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Pagbubuo ng kabuuan

Ang huling hakbang ay ang pagdaragdag ng ating LLM sa halo upang makakuha ng mga sagot na naka-ground sa ating data. Maaari natin itong ipatupad tulad ng sumusunod:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # I-convert ang tanong sa query vector
    query_vector = create_embeddings(user_input)

    # Hanapin ang pinaka-magkakatulad na mga dokumento
    distances, indices = nbrs.kneighbors([query_vector])

    # idagdag ang mga dokumento sa query upang magbigay ng konteksto
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # pagsamahin ang kasaysayan at ang input ng user
    history.append(user_input)

    # gumawa ng isang message object
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # gamitin ang Responses API upang gumawa ng sagot
    response = client.responses.create(
        model="gpt-5-mini",
        max_output_tokens=800,
        input=messages,
        store=False,
    )

    return response.output_text

chatbot(user_input)
```

## Pagsusuri ng ating aplikasyon

### Mga Sukatan ng Pagsusuri

- Kalidad ng mga sagot na ibinigay, na tinitiyak na ito ay natural, malinis magsalita at parang tao

- Kakatakan ng data: pagsusuri kung ang sagot ay nagmula sa ibinigay na mga dokumento

- Kaugnayan: pagsusuri kung ang sagot ay tumutugma at may kaugnayan sa tanong na tinanong

- Daloy ng pagsasalita - kung ang sagot ay grammatikal na makatwiran

## Mga Gamit ng RAG (Retrieval Augmented Generation) at mga vector database

Maraming mga iba't ibang gamit kung saan mapapabuti ng function calls ang iyong app katulad ng:

- Tanong at Sagot: paga-ground ng data ng iyong kumpanya para sa chat na magagamit ng mga empleyado sa pagtatanong.

- Recommendation Systems: kung saan maaari kang gumawa ng sistema na tumutugma sa pinakakahawig na mga halaga halimbawa mga pelikula, mga restawran at marami pa.

- Serbisyo ng chatbot: maaari kang mag-imbak ng kasaysayan ng chat at personalisahin ang pag-uusap base sa data ng user.

- Paghahanap ng larawan base sa vector embeddings, kapaki-pakinabang sa pagkilala ng larawan at pagtuklas ng anomalya.

## Buod

Natakpan natin ang mga pangunahing bahagi ng RAG mula sa pagdagdag ng ating data sa aplikasyon, ang query ng user at output. Upang mapadali ang paggawa ng RAG, maaari mong gamitin ang mga framework tulad ng Semanti Kernel, Langchain o Autogen.

## Takdang-Aralin

Para ipagpatuloy ang iyong pag-aaral sa Retrieval Augmented Generation (RAG), maaari kang bumuo ng:

- Gumawa ng front-end para sa aplikasyon gamit ang framework na iyong napili

- Gamitin ang isang framework, alinman sa LangChain o Semantic Kernel, at gawin muli ang iyong aplikasyon.

Binabati kita sa pagkumpleto ng aralin 👏.

## Hindi dito nagtatapos ang pagkatuto, ipagpatuloy ang Paglalakbay

Pagkatapos makumpleto ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang ipagpatuloy ang pag-level up ng iyong kaalaman sa Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->