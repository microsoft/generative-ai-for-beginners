# Retrieval Augmented Generation (RAG) at Vector Databases

[![Retrieval Augmented Generation (RAG) at Vector Databases](../../../translated_images/tl/15-lesson-banner.ac49e59506175d4f.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Sa leksyon tungkol sa mga aplikasyon ng paghahanap, bahagyang nating natutunan kung paano isama ang sariling data sa Large Language Models (LLMs). Sa leksyong ito, mas tatalakayin natin ang mga konsepto ng pag-grund ng iyong data sa iyong LLM na aplikasyon, ang mekanismo ng proseso at ang mga pamamaraan para sa pag-iimbak ng data, kabilang ang parehong embeddings at teksto.

> **Video Darating Sa Lalong Panahon**

## Panimula

Sa leksyong ito, tatalakayin natin ang mga sumusunod:

- Isang panimula sa RAG, kung ano ito at bakit ito ginagamit sa AI (artificial intelligence).

- Pag-unawa kung ano ang vector databases at paggawa ng isa para sa ating aplikasyon.

- Isang praktikal na halimbawa kung paano isasama ang RAG sa isang aplikasyon.

## Mga Layunin sa Pagkatuto

Pagkatapos makumpleto ang leksyong ito, magagawa mo:

- Ipaliwanag ang kahalagahan ng RAG sa pagkuha at pagproseso ng data.

- Mag-set up ng isang RAG na aplikasyon at pag-grund ng isang LLM gamit ang iyong data.

- Epektibong isama ang RAG at vector databases sa mga LLM na aplikasyon.

## Ang Ating Senaryo: pagpapahusay ng ating mga LLM gamit ang sariling data

Para sa leksyong ito, nais nating idagdag ang sariling mga tala sa education startup, na nagpapahintulot sa chatbot na kumuha ng higit pang impormasyon tungkol sa iba't ibang paksa. Gamit ang mga tala na mayroon tayo, makakaya ng mga mag-aaral na mag-aral nang mas maayos at maintindihan ang iba't ibang paksa, na nagpapadali sa pag-review para sa kanilang mga pagsusulit. Para likhain ang ating senaryo, gagamit tayo ng:

- `Azure OpenAI:` ang LLM na gagamitin natin upang likhain ang ating chatbot

- `AI for beginners' lesson on Neural Networks`: ito ang data na paggagamitan ng ground sa ating LLM

- `Azure AI Search` at `Azure Cosmos DB:` vector database para mag-imbak ng data at gumawa ng search index

Makakagawa ang mga user ng practice quizzes at revision flashcards mula sa kanilang mga tala at magsagawa ng buod ng mga talang iyon sa mga maikling pangkalahatan. Para magsimula, tingnan muna natin kung ano ang RAG at paano ito gumagana:

## Retrieval Augmented Generation (RAG)

Ang isang LLM na pinalakas ng chatbot ay nagpaproseso ng mga prompt ng user upang makabuo ng mga sagot. Ito ay idinisenyo upang maging interaktibo at nakikipag-ugnayan sa mga user sa malawak na hanay ng mga paksa. Gayunpaman, ang mga sagot nito ay limitado sa ibinigay na konteksto at sa kanyang pundasyong training data. Halimbawa, ang GPT-4 ay may knowledge cutoff noong Setyembre 2021, ibig sabihin, wala itong kaalaman tungkol sa mga pangyayaring naganap pagkatapos ng panahong iyon. Dagdag pa rito, ang data na ginamit sa pag-train ng LLMs ay hindi kasama ang mga kumpidensyal na impormasyon tulad ng personal na mga tala o manwal ng produkto ng isang kumpanya.

### Paano Gumagana ang mga RAG (Retrieval Augmented Generation)

![drawing showing how RAGs work](../../../translated_images/tl/how-rag-works.f5d0ff63942bd3a6.webp?WT.mc_id=academic-105485-koreyst)

Halimbawa, gusto mong mag-deploy ng chatbot na gumagawa ng mga quizzes mula sa iyong mga tala, kakailanganin mo ng koneksyon sa knowledge base. Dito pumapasok ang RAG. Gumagana ang RAG ng ganito:

- **Knowledge base:** Bago ang retrieval, kailangang i-ingest at i-preprocess ang mga dokumentong ito, karaniwang hinahati-hati ang malalaking dokumento sa mas maliliit na bahagi, ginagawang text embedding at iniimbak sa database.

- **User Query:** nagtatanong ang user ng isang katanungan

- **Retrieval:** Kapag may tanong ang user, kinukuha ng embedding model ang mahalagang impormasyon mula sa knowledge base upang magbigay ng karagdagang konteksto na isasama sa prompt.

- **Augmented Generation:** pinapalakas ng LLM ang sagot batay sa data na nakuha. Pinapayagan nito na ang sagot ay hindi lamang batay sa pre-trained data kundi pati na rin sa may kaugnayang impormasyon mula sa dagdag na konteksto. Ginagamit ang nakuha na data upang palakasin ang mga sagot ng LLM. Pagkatapos, ibinabalik ng LLM ang sagot sa tanong ng user.

![Diagram showing RAG architecture](../../../translated_images/tl/encoder-decode.f2658c25d0eadee2.webp?WT.mc_id=academic-105485-koreyst)

Pinagsasama ng RAG ang retriever at generator: kinokonvert ang query sa vector, hinahambing ito sa document index para hanapin ang kaugnay na mga bahagi ng teksto, at ang mga bahaging ito ay ibinibigay bilang konteksto sa isang LLM, na siyang bumubuo ng sagot. Maaaring gumamit ang retriever at generator ng iba't ibang mga modelo; hindi kailangan ng encoder-decoder transformer ang RAG.

Dalawang paraan ng pagpapatupad ng RAG ayon sa panukalang papel: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) ay:

- **_RAG-Sequence_** gamit ang mga dokumentong nakuha para hulaan ang pinakamahusay na posibleng sagot sa tanong ng user

- **RAG-Token** gamit ang mga dokumento upang bumuo ng susunod na token, pagkatapos ay kunin ang mga ito para sagutin ang tanong ng user

### Bakit gagamitin ang mga RAG? 

- **Yaman ng impormasyon:** sinusiguro na ang mga sagot ay napapanahon at kasalukuyan. Pinapalakas nito ang performance sa mga domain specific na gawain sa pamamagitan ng pag-access sa internal knowledge base.

- Binabawasan ang pekeng impormasyon sa pamamagitan ng paggamit ng **verifiable data** mula sa knowledge base upang magbigay ng konteksto sa mga tanong ng user.

- Ito ay **tipid sa gastos** dahil mas mura ito kumpara sa fine-tuning ng isang LLM.

## Paggawa ng knowledge base

Ang ating aplikasyon ay nakabatay sa sariling data, i.e., ang Neural Network na leksyon mula sa AI for Beginners na kurikulum.

### Vector Databases

Ang isang vector database, hindi tulad ng tradisyunal na mga database, ay espesyal na idinisenyo upang mag-imbak, mag-manage at maghanap ng mga embedded vectors. Ito ay nag-iimbak ng numerikal na representasyon ng mga dokumento. Sa paghahati ng data sa numerikal na embeddings, mas madali para sa ating AI system na maunawaan at maproseso ang data.

Dahil ang mga LLM ay may limitasyon sa bilang ng mga input tokens, hinahati natin ang mga dokumento sa maliliit na bahagi bago ang embedding. Kapag may tanong ang user, pinipili ang mga embedding na pinakamalapit sa query para tukuyin ang mga kaugnay na bahagi ng teksto, na ibinabalik kasabay ng prompt. Nakakatulong ang pagchunk para mabawasan ang bilang ng tokens na ipinapasa sa LLM kaya nakakabawas din sa gastos.

Ilan sa mga kilalang vector databases ay ang Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant at DeepLake. Maaari kang gumawa ng Azure Cosmos DB model gamit ang Azure CLI gamit ang sumusunod na utos:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Mula teksto hanggang embeddings

Bago natin iimbak ang data, kailangang i-convert ito sa vector embeddings bago ito maiimbak sa database. Kung nagtatrabaho ka sa malalaking dokumento o mahahabang teksto, maaari mo silang hatiin base sa mga inaasahang query. Ang paghahati ay maaaring gawin sa antas ng pangungusap, o sa antas ng talata. Dahil nakukuha ng paghahati ang mga kahulugan mula sa mga salitang nakapaligid, maaari kang magdagdag ng ibang konteksto sa isang chunk, halimbawa, sa pamamagitan ng pagdagdag ng pamagat ng dokumento o pagsama ng ilang teksto bago o pagkatapos ng chunk. Maaari mong hatiin ang data tulad ng sumusunod:

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

Kapag nahati na, maaari na nating i-embed ang ating teksto gamit ang iba't ibang embedding models. Ilan sa mga modelong maaari mong gamitin ay: word2vec, ada-002 ng OpenAI, Azure Computer Vision at marami pang iba. Ang pagpili ng modelo ay depende sa mga wika na gamit mo, uri ng content na naka-encode (teksto/larawan/audio), laki ng input na kaya nitong i-encode at haba ng embedding output.

Isang halimbawa ng embedded na teksto gamit ang OpenAI na `text-embedding-ada-002` na modelo ay:
![an embedding of the word cat](../../../translated_images/tl/cat.74cbd7946bc9ca38.webp?WT.mc_id=academic-105485-koreyst)

## Retrieval at Vector Search

Kapag nagtatanong ang user, kino-convert ng retriever ito sa vector gamit ang query encoder, pagkatapos ay hahanapin nito sa ating document search index ang mga relevant vectors na kaugnay ng input. Kapag tapos na, kino-convert nito pareho, ang input vector at mga document vectors, sa teksto at ipinapasa sa LLM.

### Retrieval

Nangyayari ang retrieval kapag mabilis na hinahanap ng sistema ang mga dokumento mula sa index na tumutugon sa search criteria. Layunin ng retriever na kumuha ng mga dokumentong gagamitin para magbigay ng konteksto at pag-grund ng LLM sa iyong data.

May ilang paraan para magsagawa ng paghahanap sa loob ng ating database tulad ng:

- **Keyword search** - ginagamit para sa mga paghahanap sa teksto

- **Vector search** - kinokonvert ang mga dokumento mula sa teksto tungo sa vector representations gamit ang embedding models, na nagpapahintulot sa isang **semantic search** gamit ang kahulugan ng mga salita. Ginagawa ang retrieval sa pamamagitan ng pag-query sa mga dokumento na ang vector representations ay pinakamalapit sa tanong ng user.

- **Hybrid** - kombinasyon ng parehong keyword at vector search.

Isang hamon sa retrieval ay kapag walang katulad na sagot sa query sa database, ibinabalik ng sistema ang pinakamagandang impormasyon na makukuha ngunit maaari kang gumamit ng mga taktika tulad ng pag-set ng maximum distance para sa relevance o paggamit ng hybrid search na pinagsasama ang parehong keywords at vector search. Sa leksyong ito gagamit tayo ng hybrid search, kombinasyon ng vector at keyword search. Ipapaloob natin ang data sa isang dataframe na may mga column na naglalaman ng mga chunks pati na embeddings.

### Vector Similarity

Hahanapin ng retriever sa knowledge database ang embeddings na magkalapit—mga pinakamalapit na kapitbahay—dahil sila ay kumakatawan sa magkasimilar na mga teksto. Sa senaryong ito, kapag nag-submit ng query ang user, muna itong i-embed at saka itutugma sa mga kaparehong embeddings. Ang pinakakaraniwang sukatan upang ikumpara ang vector similarity ay cosine similarity, na batay sa anggulo sa pagitan ng dalawang vectors.

Ang iba pang mga metrika na maaari nating gamitin upang sukatin ang similarity ay ang Euclidean distance, ang tuwirang linya sa pagitan ng vector endpoints, at dot product, na sumusukat sa kabuuan ng produkto ng mga katugmang elemento sa dalawang vectors.

### Search index

Sa pag-retrieve, kailangang gumawa muna tayo ng search index para sa ating knowledge base bago maghanap. Mag-iimbak ang index ng ating embeddings at mabilis na makakapag-retrieve ng pinakamalapit na chunks kahit sa isang malaking database. Pwede tayong gumawa ng index locally gamit ang:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Re-ranking

Kapag na-query mo na ang database, baka kailangan mong ayusin ang mga resulta mula sa pinaka-relevant. Gumagamit ang reranking LLM ng Machine Learning upang pagandahin ang relevance ng mga resulta ng paghahanap sa pamamagitan ng pag-aayos ng mga ito mula sa pinaka-nauugnay. Sa paggamit ng Azure AI Search, ang reranking ay awtomatikong ginagawa para sa iyo gamit ang semantic reranker. Isang halimbawa kung paano gumagana ang reranking gamit ang pinakamalapit na kapitbahay:

```python
# Find the most similar documents
distances, indices = nbrs.kneighbors([query_vector])

# Print the three most similar documents with their distance to the question
for distance, index in zip(distances[0][:3], indices[0][:3]):
    print(flattened_df['chunks'].iloc[index])
    print(flattened_df['path'].iloc[index])
    print(distance)
```

## Pagsasama-sama nito

Ang huling hakbang ay idagdag ang ating LLM para makakuha ng mga sagot na grounded sa ating data. Maari nating ipatupad ito tulad ng sumusunod:

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

## Pagsusuri sa ating aplikasyon

### Mga Metric sa Pagsusuri

- Kalidad ng mga sagot na ibinibigay na siguradong natural, matatas at parang tao ang dating

- Groundedness ng data: pagsusuri kung ang sagot ay nanggaling sa mga dokumentong ibinigay

- Relevance: pagsusuri kung tumutugma at kaugnay ang sagot sa tanong

- Fluency - kung ang sagot ay lohikal sa gramatika

## Mga Gamit ng RAG at vector databases

Maraming iba't ibang gamit kung saan mapapabuti ng RAG ang iyong app, tulad ng:

- Question and Answering: pag-grund ng iyong company data sa chat na magagamit ng mga empleyado upang magtanong.

- Recommendation Systems: kung saan maaaring gumawa ng sistema na nagtutugma ng pinaka-similar na values tulad ng mga pelikula, restawran at marami pang iba.

- Chatbot services: maaari mong iimbak ang kasaysayan ng chat at i-personalize ang pag-uusap base sa datos ng user.

- Paghahanap ng larawan batay sa vector embeddings, kapaki-pakinabang sa image recognition at anomaly detection.

## Buod

Natakpan natin ang mga pangunahing bahagi ng RAG mula sa pagdagdag ng data sa aplikasyon, user query at output. Para mapadali ang paggawa ng RAG, maaari kang gumamit ng framework tulad ng Semantic Kernel, LangChain o AutoGen.

## Takdang Aralin

Para ipagpatuloy ang pag-aaral mo sa Retrieval Augmented Generation (RAG), maaari kang gumawa ng:

- Gumawa ng front-end para sa aplikasyon gamit ang framework na pipiliin mo

- Gamitin ang isang framework, alinman sa LangChain o Semantic Kernel, at muling likhain ang iyong aplikasyon.

Binabati kita sa pagkakatapos ng leksyon 👏.

## Hindi Dito Nagtatapos ang Pagkatuto, Ipagpatuloy ang Paglalakbay

Pagkatapos makumpleto ang leksyon, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang ipagpatuloy ang pagpapalawak ng iyong kaalaman sa Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->