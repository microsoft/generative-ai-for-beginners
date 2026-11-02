# Retrieval Augmented Generation (RAG) at Mga Vector Database

[![Retrieval Augmented Generation (RAG) at Mga Vector Database](../../../translated_images/tl/15-lesson-banner.ac49e59506175d4f.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Sa leksyon ng search applications, bahagyang natutunan natin kung paano isama ang iyong sariling data sa Mga Malalaking Modelo ng Wika (LLMs). Sa leksyong ito, lalaliman pa natin ang mga konsepto ng pag-ugat ng iyong data sa iyong LLM application, ang mekanismo ng proseso at mga pamamaraan para sa pag-iimbak ng data, kabilang ang embeddings at teksto.

> **Darating Na Ang Video**

## Panimula

Sa leksyong ito tatalakayin natin ang mga sumusunod:

- Isang panimula sa RAG, kung ano ito at bakit ito ginagamit sa AI (artificial intelligence).

- Pag-unawa kung ano ang mga vector database at paggawa ng isa para sa ating aplikasyon.

- Isang praktikal na halimbawa kung paano isama ang RAG sa isang aplikasyon.

## Mga Layunin sa Pagkatuto

Pagkatapos mong matapos ang leksyong ito, magagawa mong:

- Ipaliwanag ang kahalagahan ng RAG sa pagkuha at pagproseso ng data.

- Mag-setup ng isang RAG application at i-ground ang isang LLM gamit ang iyong data.

- Epektibong isama ang RAG at mga vector database sa mga aplikasyon ng LLM.

## Ang Aming Sitwasyon: pagpapahusay ng aming mga LLM gamit ang sariling data

Para sa leksyong ito, nais naming idagdag ang aming sariling mga tala sa education startup, na nagpapahintulot sa chatbot na makakuha ng mas maraming impormasyon tungkol sa iba't ibang paksa. Gamit ang mga tala na mayroon kami, magkakaroon ng kakayahan ang mga mag-aaral na mag-aral nang mas mahusay at maunawaan ang mga iba't ibang paksa, na nagpapadali sa pagrerebisa para sa kanilang mga pagsusulit. Para likhain ang aming sitwasyon, gagamitin namin ang:

- `Azure OpenAI:` ang LLM na gagamitin namin para likhain ang aming chatbot

- `AI for beginners' lesson on Neural Networks`: ito ang data na paggagalingan ng pag-ugat ng aming LLM

- `Azure AI Search` at `Azure Cosmos DB:` vector database para iimbak ang aming data at gumawa ng search index

Magkakaroon ang mga user ng kakayahang gumawa ng mga practice quiz at mga flashcards para sa pagrerebisa mula sa kanilang mga tala at buodin ang mga talang iyon sa mga maikling buod. Para magsimula, tingnan muna natin kung ano ang RAG at paano ito gumagana:

## Retrieval Augmented Generation (RAG)

Isang chatbot na gumagamit ng LLM ang nagpoproseso ng mga utos ng user upang makalikha ng mga sagot. Ito ay ginawa upang maging interaktibo at nakikipag-ugnayan sa mga user sa iba't ibang paksa. Gayunpaman, ang mga sagot nito ay limitado lamang sa konteksto na ibinigay at sa kanyang foundational training data. Halimbawa, ang cutoff ng kaalaman ng GPT-4 ay Setyembre 2021, ibig sabihin ay wala itong kaalaman tungkol sa mga pangyayari matapos ang panahong iyon. Bukod pa rito, ang data na ginamit para sanayin ang mga LLM ay hindi kasama ang mga kumpidensyal na impormasyon tulad ng personal na tala o manwal ng produkto ng isang kumpanya.

### Paano Gumagana ang Mga RAG (Retrieval Augmented Generation)

![drawing showing how RAGs work](../../../translated_images/tl/how-rag-works.f5d0ff63942bd3a6.webp?WT.mc_id=academic-105485-koreyst)

Halimbawa gusto mong mag-deploy ng chatbot na lumilikha ng mga quiz mula sa iyong mga tala, kakailanganin mo ng koneksyon sa knowledge base. Dito papasok ang RAG. Gumagana ang RAGs sa mga sumusunod:

- **Knowledge base:** Bago ang retrieval, kailangang i-ingest at i-preprocess ang mga dokumentong ito, karaniwang pinaghahati-hati ang malalaking dokumento sa mas maliliit na bahagi, pagkatapos ay itinatala sa text embedding at iniimbak sa database.

- **User Query:** nagtatanong ang user ng isang katanungan

- **Retrieval:** Kapag ang user ay nagtatanong, kinukuha ng embedding model ang kaugnay na impormasyon mula sa ating knowledge base para magbigay ng karagdagang konteksto na isasama sa prompt.

- **Augmented Generation:** pinapaganda ng LLM ang sagot nito base sa retrieved na data. Pinapayagan nitong ang sagot na malikha ay hindi lamang batay sa pre-trained data kundi pati na rin sa kaugnay na impormasyon mula sa idinagdag na konteksto. Ginagamit ang retrieved data para dagdagan ang mga sagot ng LLM. Pagkatapos, ibinabalik ng LLM ang sagot sa tanong ng user.

![Diagram showing RAG architecture](../../../translated_images/tl/encoder-decode.f2658c25d0eadee2.webp?WT.mc_id=academic-105485-koreyst)

Pinagsasama ng RAG ang retriever at generator: kino-convert ang query sa vector, hinahambing ito sa document index para hanapin ang kaugnay na bahagi ng teksto, at ang mga ito ay nagbibigay ng konteksto sa LLM na gagawa ng sagot. Maaaring magkaiba ang mga modelo na ginagamit ng retriever at generator; hindi kailangan ng RAG na encoder-decoder transformer.

Dalawang paraan sa pagsasagawa ng RAG ayon sa iminungkahing papel: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) ay:

- **_RAG-Sequence_** gamit ang mga retrieved na dokumento para hulaan ang pinakamahusay na posibleng sagot sa tanong ng user

- **RAG-Token** gamit ang mga dokumento para gumawa ng susunod na token, tapos kinukuha ito para sagutin ang tanong ng user

### Bakit mo gagamitin ang Mga RAG?

- **Information richness:** tinitiyak na ang mga sagot na teksto ay napapanahon at kasalukuyan. Pinapabuti nito ang pagganap sa mga domain-specific na gawain sa pamamagitan ng pag-access sa internal knowledge base.

- Binabawasan ang peke o imbento sa pamamagitan ng paggamit ng **beripikableng data** sa knowledge base upang magbigay ng konteksto sa mga tanong ng user.

- Ito ay **matipid** dahil mas mura kumpara sa fine-tuning ng isang LLM

## Paglikha ng knowledge base

Ang aming aplikasyon ay batay sa aming personal na data, i.e., ang leksyon tungkol sa Neural Network mula sa AI for Beginners curriculum.

### Mga Vector Database

Ang vector database, hindi tulad ng tradisyunal na mga database, ay isang espesyal na database na idinisenyo upang mag-imbak, mag-manage at mag-search ng embedded vectors. Iniimbak nito ang mga numerikal na representasyon ng mga dokumento. Ang paghahati ng data sa mga numerikal na embeddings ay nagpapadali sa ating AI system na maunawaan at maproseso ang data.

Dahil may limitasyon ang mga LLM sa bilang ng input tokens, hinahati natin ang mga dokumento sa mga chunk bago sila i-embed. Kapag may tanong ang user, ang embeddings na pinaka-katulad sa query ay nagtatakda ng kaugnay na bahagi ng teksto, na ibinabalik kasabay ng prompt. Nakakatulong din ang chunking na mabawasan ang bilang ng tokens na ipapasa sa LLM kaya nakakatipid ito ng gastos.

Ilan sa mga kilalang vector database ay Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant at DeepLake. Maaari kang gumawa ng Azure Cosmos DB model gamit ang Azure CLI sa sumusunod na utos:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Mula teksto papuntang embeddings

Bago natin iimbak ang data, kailangan muna itong i-convert sa vector embeddings bago ito maisave sa database. Kung nagtatrabaho ka sa malalaking dokumento o mahahabang teksto, maaaring hatiin mo ito base sa mga query na inaasahan mo. Maaaring gawin ang chunking sa antas ng pangungusap, o sa antas ng talata. Dahil kumukuha ang chunking ng kahulugan mula sa mga salitang nakapaligid dito, maaaring magdagdag ng ibang konteksto sa isang chunk, halimbawa, sa pagdagdag ng pamagat ng dokumento o pagsama ng ilang teksto bago o pagkatapos ng chunk. Maaari mong hatiin ang data gaya ng:

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

Kapag na-chunk na, maaari nating i-embed ang teksto gamit ang iba't ibang embedding models. Ilan sa mga modelong maaari mong gamitin ay: word2vec, ada-002 ng OpenAI, Azure Computer Vision at marami pang iba. Ang pagpili ng model ay nakadepende sa mga wikang ginagamit mo, uri ng content na i-encode (teksto/larawan/audio), laki ng input na kayang i-encode, at haba ng output ng embedding.

Isang halimbawa ng embedded na teksto gamit ang OpenAI's `text-embedding-ada-002` model ay:
![an embedding of the word cat](../../../translated_images/tl/cat.74cbd7946bc9ca38.webp?WT.mc_id=academic-105485-koreyst)

## Retrieval at Vector Search

Kapag nagtatanong ang user, kino-convert ito ng retriever sa vector gamit ang query encoder, pagkatapos ay naghahanap ito sa document search index para sa mga kaugnay na vectors sa dokumento na may kinalaman sa input. Kapag natapos, kino-convert nito ang input vector at document vectors sa teksto at ipinapasa sa LLM.

### Retrieval

Nangyayari ang retrieval kapag sinubukan ng sistema na mabilis na hanapin ang mga dokumento mula sa index na sumasapat sa criteria ng paghahanap. Ang layunin ng retriever ay kumuha ng mga dokumento na gagamitin para magbigay ng konteksto at i-ground ang LLM sa iyong data.

May ilang paraan upang magsagawa ng paghahanap sa ating database tulad ng:

- **Keyword search** - ginagamit para sa text searches

- **Vector search** - kino-convert ang mga dokumento mula sa texto sa mga vector representations gamit ang embedding models, na pinapayagan ang **semantic search** gamit ang kahulugan ng mga salita. Gagawa ng retrieval sa pamamagitan ng pag-query sa mga dokumento na ang vector representations ay pinakamalapit sa tanong ng user.

- **Hybrid** - kombinasyon ng keyword at vector search.

Isang hamon sa retrieval ay kapag walang kaparehong sagot sa query sa database, magbabalik ang sistema ng pinakamainam na impormasyong makukuha nito, subalit maaari kang gumamit ng taktika tulad ng pagtatakda ng maximum distance para sa relevance o paggamit ng hybrid search na pinagsasama ang keyword at vector search. Sa leksyong ito gagamit tayo ng hybrid search, isang kombinasyon ng vector at keyword search. Itatago natin ang data sa isang dataframe na may mga column para sa chunks pati embeddings.

### Vector Similarity

Maghahanap ang retriever sa knowledge database para sa embeddings na malapit sa isa't isa—ang mga pinakamalapit na kapitbahay—dahil ito ay mga tekstong magkatulad. Sa sitwasyong ito, kapag nag-submit ang user ng query, ito ay unang i-embed at pagkatapos ay iha-hambing sa mga katulad na embeddings. Ang pinaka-karaniwang sukat na ginagamit sa paghahambing ng vector similarity ay cosine similarity, na batay sa anggulo sa pagitan ng dalawang vectors.

Ang iba pang metrics na maaari nating gamitin para sukatin ang similarity ay Euclidean distance, na ang tuwid na linyang nagdudugtong sa mga dulo ng vector, at dot product, na sumusukat sa kabuuan ng mga produkto ng mga katumbas na elemento sa dalawang vectors.

### Search index

Kapag nagsasagawa ng retrieval, kailangan nating gumawa ng search index para sa ating knowledge base bago magsagawa ng paghahanap. Itatago ng index ang ating embeddings at mabilis na makukuha ang mga pinakakahawig na chunks kahit sa malaking database. Maaari nating gawin ang index locally gamit:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Re-ranking

Kapag na-query mo na ang database, maaaring kailanganin mong i-sort ang mga resulta mula sa pinaka-kaugnay. Gumagamit ang reranking LLM ng Machine Learning upang pagbutihin ang kaugnayan ng mga resulta ng paghahanap sa pamamagitan ng pag-aayos ng mga ito mula sa pinaka-kaugnay. Sa paggamit ng Azure AI Search, awtomatikong ginagawa ang reranking gamit ang semantic reranker. Halimbawa kung paano gumagana ang reranking gamit ang pinakamalapit na kapitbahay:

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

## Pagsama-samahin Lahat ito

Ang huling hakbang ay ang pagdagdag ng ating LLM sa proseso upang makakuha ng mga sagot na naka-ground sa ating data. Maaari itong ipatupad tulad ng sumusunod:

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

## Pagsusuri ng aming aplikasyon

### Mga Sukatan sa Pagsusuri

- Kalidad ng mga sagot na ibinibigay na tumutunog na natural, fluent at parang tao

- Groundedness ng data: pagsusuri kung ang sagot ay nagmula sa ibinigay na mga dokumento

- Kaugnayan: pagsusuri kung ang sagot ay tumutugma at may kinalaman sa tanong

- Fluency - kung ang sagot ay grammatikal na tama at may kabuluhan

## Mga Paggamit para sa RAG (Retrieval Augmented Generation) at mga vector database

Maraming iba’t ibang mga gamit kung saan mapapabuti ng RAG ang iyong app, tulad ng:

- Question and Answering: pag-ugat ng data ng kumpanya sa isang chat na maaaring gamitin ng mga empleyado upang magtanong.

- Recommendation Systems: kung saan maaari kang gumawa ng sistema na tumutugma sa pinaka-katulad na mga halaga tulad ng mga pelikula, restaurant at marami pang iba.

- Chatbot services: maaari mong i-store ang history ng chat at i-personalize ang usapan base sa data ng user.

- Paghahanap ng larawan base sa vector embeddings, kapaki-pakinabang sa image recognition at anomaly detection.

## Buod

Natalakay natin ang mga pangunahing aspeto ng RAG mula sa pagdagdag ng data sa aplikasyon, ang user query at output. Para mapadali ang paggawa ng RAG, maaari mong gamitin ang mga framework gaya ng Semantic Kernel, LangChain o AutoGen.

## Takdang-Aralin

Upang ipagpatuloy ang iyong pag-aaral ng Retrieval Augmented Generation (RAG) maaari kang bumuo ng:

- Gumawa ng front-end para sa aplikasyon gamit ang framework na iyong pinili

- Gamitin ang isang framework, alinman sa LangChain o Semantic Kernel, at gawing muli ang iyong aplikasyon.

Binabati kita sa pagtatapos ng leksyon 👏.

## Hindi dito nagtatapos ang pagkatuto, ipagpatuloy ang paglalakbay

Pagkatapos matapos ang leksyong ito, silipin ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para ipagpatuloy ang pag-level up ng iyong kaalaman sa Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->