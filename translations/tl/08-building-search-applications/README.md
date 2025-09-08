<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d46aad0917a1a342d613e2c13d457da5",
  "translation_date": "2025-07-09T12:59:51+00:00",
  "source_file": "08-building-search-applications/README.md",
  "language_code": "tl"
}
-->
# Paggawa ng Mga Search Application

[![Introduction to Generative AI and Large Language Models](../../../translated_images/08-lesson-banner.8fff48c566dad08a1cbb9f4b4a2c16adfdd288a7bbfffdd30770b466fe08c25c.tl.png)](https://aka.ms/gen-ai-lesson8-gh?WT.mc_id=academic-105485-koreyst)

> > _I-click ang larawan sa itaas para mapanood ang video ng araling ito_

Hindi lang chatbot at text generation ang kaya ng LLMs. Posible ring gumawa ng mga search application gamit ang Embeddings. Ang Embeddings ay mga numerikal na representasyon ng data na kilala rin bilang mga vector, at maaaring gamitin para sa semantic search ng data.

Sa araling ito, gagawa ka ng isang search application para sa aming education startup. Ang aming startup ay isang non-profit na organisasyon na nagbibigay ng libreng edukasyon sa mga estudyante sa mga umuunlad na bansa. Mayroon kaming maraming YouTube videos na maaaring gamitin ng mga estudyante para matuto tungkol sa AI. Nais ng aming startup na gumawa ng search application na magpapahintulot sa mga estudyante na maghanap ng YouTube video sa pamamagitan ng pag-type ng tanong.

Halimbawa, maaaring mag-type ang isang estudyante ng 'Ano ang Jupyter Notebooks?' o 'Ano ang Azure ML' at ibabalik ng search application ang listahan ng mga YouTube videos na may kaugnayan sa tanong, at higit pa rito, ibabalik ng search application ang link sa bahagi ng video kung saan matatagpuan ang sagot sa tanong.

## Panimula

Sa araling ito, tatalakayin natin ang:

- Semantic vs Keyword search.
- Ano ang Text Embeddings.
- Paggawa ng Text Embeddings Index.
- Paghahanap sa Text Embeddings Index.

## Mga Layunin sa Pagkatuto

Pagkatapos matapos ang araling ito, magagawa mong:

- Ipagkaiba ang semantic at keyword search.
- Ipaliwanag kung ano ang Text Embeddings.
- Gumawa ng application gamit ang Embeddings para maghanap ng data.

## Bakit gumawa ng search application?

Makakatulong ang paggawa ng search application para maintindihan mo kung paano gamitin ang Embeddings sa paghahanap ng data. Matututuhan mo rin kung paano gumawa ng search application na magagamit ng mga estudyante para mabilis makahanap ng impormasyon.

Kasama sa aralin ang Embedding Index ng mga YouTube transcripts para sa Microsoft [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) YouTube channel. Ang AI Show ay isang YouTube channel na nagtuturo tungkol sa AI at machine learning. Ang Embedding Index ay naglalaman ng Embeddings para sa bawat YouTube transcript hanggang Oktubre 2023. Gagamitin mo ang Embedding Index para gumawa ng search application para sa aming startup. Ang search application ay magbabalik ng link sa bahagi ng video kung saan matatagpuan ang sagot sa tanong. Magandang paraan ito para mabilis makahanap ng impormasyon ang mga estudyante.

Narito ang halimbawa ng semantic query para sa tanong na 'maaari mo bang gamitin ang rstudio sa azure ml?'. Tingnan ang YouTube url, makikita mo na may timestamp ito na magdadala sa iyo sa bahagi ng video kung saan matatagpuan ang sagot sa tanong.

![Semantic query for the question "can you use rstudio with Azure ML"](../../../translated_images/query-results.bb0480ebf025fac69c5179ad4d53b6627d643046838c857dc9e2b1281f1cdeb7.tl.png)

## Ano ang semantic search?

Maaaring nagtatanong ka, ano nga ba ang semantic search? Ang semantic search ay isang paraan ng paghahanap na gumagamit ng kahulugan o ibig sabihin ng mga salita sa query para magbalik ng mga kaugnay na resulta.

Narito ang halimbawa ng semantic search. Sabihin nating naghahanap ka ng sasakyan, maaaring maghanap ka ng 'aking pangarap na sasakyan', naiintindihan ng semantic search na hindi ka `nangangarap` lang ng sasakyan, kundi naghahanap ka ng iyong `ideal` na sasakyan. Naiintindihan ng semantic search ang iyong intensyon at nagbabalik ng mga kaugnay na resulta. Ang alternatibo ay `keyword search` na literal na hahanapin ang mga pangarap tungkol sa sasakyan at madalas ay nagbabalik ng mga hindi kaugnay na resulta.

## Ano ang Text Embeddings?

[Text embeddings](https://en.wikipedia.org/wiki/Word_embedding?WT.mc_id=academic-105485-koreyst) ay isang paraan ng representasyon ng teksto na ginagamit sa [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing?WT.mc_id=academic-105485-koreyst). Ang Text embeddings ay mga numerikal na representasyon ng teksto na may kahulugan. Ginagamit ang Embeddings para ipakita ang data sa paraang madaling maintindihan ng makina. Maraming modelo para gumawa ng text embeddings, sa araling ito, tututok tayo sa paggawa ng embeddings gamit ang OpenAI Embedding Model.

Narito ang halimbawa, isipin na ang sumusunod na teksto ay mula sa transcript ng isa sa mga episode ng AI Show YouTube channel:

```text
Today we are going to learn about Azure Machine Learning.
```

Ipapasa natin ang teksto sa OpenAI Embedding API at ibabalik nito ang sumusunod na embedding na binubuo ng 1536 na numero o vector. Bawat numero sa vector ay kumakatawan sa ibang aspeto ng teksto. Para sa maikling pagpapakita, narito ang unang 10 numero sa vector.

```python
[-0.006655829958617687, 0.0026128944009542465, 0.008792596869170666, -0.02446001023054123, -0.008540431968867779, 0.022071078419685364, -0.010703742504119873, 0.003311325330287218, -0.011632772162556648, -0.02187200076878071, ...]
```

## Paano ginagawa ang Embedding index?

Ang Embedding index para sa araling ito ay ginawa gamit ang serye ng mga Python script. Makikita mo ang mga script kasama ang mga tagubilin sa [README](./scripts/README.md?WT.mc_id=academic-105485-koreyst) sa folder na 'scripts' para sa araling ito. Hindi mo kailangang patakbuhin ang mga script na ito para matapos ang aralin dahil ibinibigay na ang Embedding Index.

Ginagawa ng mga script ang mga sumusunod:

1. Dina-download ang transcript para sa bawat YouTube video sa [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) playlist.
2. Gamit ang [OpenAI Functions](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling?WT.mc_id=academic-105485-koreyst), sinusubukang kunin ang pangalan ng tagapagsalita mula sa unang 3 minuto ng YouTube transcript. Ang pangalan ng tagapagsalita para sa bawat video ay iniimbak sa Embedding Index na pinangalanang `embedding_index_3m.json`.
3. Hinahati ang transcript text sa **3 minutong mga segment ng teksto**. Kasama sa segment ang humigit-kumulang 20 salita na nag-o-overlap mula sa susunod na segment para matiyak na hindi mapuputol ang Embedding ng segment at para magkaroon ng mas magandang konteksto sa paghahanap.
4. Ang bawat segment ng teksto ay ipinapasa sa OpenAI Chat API para ibuod ang teksto sa 60 salita. Ang buod ay iniimbak din sa Embedding Index `embedding_index_3m.json`.
5. Sa huli, ang segment ng teksto ay ipinapasa sa OpenAI Embedding API. Ang Embedding API ay nagbabalik ng vector na may 1536 na numero na kumakatawan sa kahulugang semantiko ng segment. Ang segment kasama ang OpenAI Embedding vector ay iniimbak sa Embedding Index `embedding_index_3m.json`.

### Vector Databases

Para sa pagiging simple ng aralin, ang Embedding Index ay iniimbak sa isang JSON file na pinangalanang `embedding_index_3m.json` at niloload sa isang Pandas DataFrame. Ngunit sa production, ang Embedding Index ay iniimbak sa isang vector database tulad ng [Azure Cognitive Search](https://learn.microsoft.com/training/modules/improve-search-results-vector-search?WT.mc_id=academic-105485-koreyst), [Redis](https://cookbook.openai.com/examples/vector_databases/redis/readme?WT.mc_id=academic-105485-koreyst), [Pinecone](https://cookbook.openai.com/examples/vector_databases/pinecone/readme?WT.mc_id=academic-105485-koreyst), [Weaviate](https://cookbook.openai.com/examples/vector_databases/weaviate/readme?WT.mc_id=academic-105485-koreyst), at iba pa.

## Pag-unawa sa cosine similarity

Natutunan na natin ang tungkol sa text embeddings, ang susunod na hakbang ay matutunan kung paano gamitin ang text embeddings para maghanap ng data at partikular na hanapin ang pinaka-katulad na embeddings sa isang query gamit ang cosine similarity.

### Ano ang cosine similarity?

Ang cosine similarity ay isang sukatan ng pagkakatulad sa pagitan ng dalawang vector, madalas itong tinatawag na `nearest neighbor search`. Para magsagawa ng cosine similarity search, kailangan mong _i-vectorize_ ang _query_ na teksto gamit ang OpenAI Embedding API. Pagkatapos, kalkulahin ang _cosine similarity_ sa pagitan ng query vector at bawat vector sa Embedding Index. Tandaan, ang Embedding Index ay may vector para sa bawat segment ng YouTube transcript. Sa huli, ayusin ang mga resulta ayon sa cosine similarity at ang mga segment ng teksto na may pinakamataas na cosine similarity ang pinaka-katulad sa query.

Mula sa pananaw ng matematika, sinusukat ng cosine similarity ang cosine ng anggulo sa pagitan ng dalawang vector na ipinroject sa multidimensional na espasyo. Kapaki-pakinabang ang sukat na ito dahil kahit malayo ang dalawang dokumento sa Euclidean distance dahil sa laki, maaari pa rin silang magkaroon ng mas maliit na anggulo sa pagitan nila at kaya mas mataas na cosine similarity. Para sa karagdagang impormasyon tungkol sa mga equation ng cosine similarity, tingnan ang [Cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity?WT.mc_id=academic-105485-koreyst).

## Paggawa ng iyong unang search application

Susunod, matututuhan natin kung paano gumawa ng search application gamit ang Embeddings. Papayagan ng search application ang mga estudyante na maghanap ng video sa pamamagitan ng pag-type ng tanong. Magbabalik ang search application ng listahan ng mga video na may kaugnayan sa tanong. Magbabalik din ito ng link sa bahagi ng video kung saan matatagpuan ang sagot sa tanong.

Ang solusyong ito ay ginawa at nasubukan sa Windows 11, macOS, at Ubuntu 22.04 gamit ang Python 3.10 o mas bago. Maaari mong i-download ang Python mula sa [python.org](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

## Takdang-Aralin - paggawa ng search application para sa mga estudyante

Ipinakilala namin ang aming startup sa simula ng araling ito. Ngayon ay panahon na para bigyan ng kakayahan ang mga estudyante na gumawa ng search application para sa kanilang mga pagsusulit.

Sa takdang-aralin na ito, gagawa ka ng Azure OpenAI Services na gagamitin para sa paggawa ng search application. Gagawa ka ng mga sumusunod na Azure OpenAI Services. Kailangan mo ng Azure subscription para matapos ang takdang-aralin na ito.

### Simulan ang Azure Cloud Shell

1. Mag-sign in sa [Azure portal](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst).
2. Piliin ang Cloud Shell icon sa kanang itaas ng Azure portal.
3. Piliin ang **Bash** para sa uri ng environment.

#### Gumawa ng resource group

> Para sa mga tagubiling ito, ginagamit namin ang resource group na pinangalanang "semantic-video-search" sa East US.
> Maaari mong palitan ang pangalan ng resource group, ngunit kapag pinalitan ang lokasyon ng mga resources,
> tingnan ang [model availability table](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```shell
az group create --name semantic-video-search --location eastus
```

#### Gumawa ng Azure OpenAI Service resource

Mula sa Azure Cloud Shell, patakbuhin ang sumusunod na utos para gumawa ng Azure OpenAI Service resource.

```shell
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

#### Kuhanin ang endpoint at mga key para gamitin sa application na ito

Mula sa Azure Cloud Shell, patakbuhin ang mga sumusunod na utos para makuha ang endpoint at mga key para sa Azure OpenAI Service resource.

```shell
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

#### I-deploy ang OpenAI Embedding model

Mula sa Azure Cloud Shell, patakbuhin ang sumusunod na utos para i-deploy ang OpenAI Embedding model.

```shell
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name text-embedding-ada-002 \
    --model-name text-embedding-ada-002 \
    --model-version "2"  \
    --model-format OpenAI \
    --sku-capacity 100 --sku-name "Standard"
```

## Solusyon

Buksan ang [solution notebook](python/aoai-solution.ipynb) sa GitHub Codespaces at sundin ang mga tagubilin sa Jupyter Notebook.

Kapag pinatakbo mo ang notebook, hihilingin kang maglagay ng query. Ganito ang itsura ng input box:

![Input box for the user to input a query](../../../translated_images/notebook-search.1e320b9c7fcbb0bc1436d98ea6ee73b4b54ca47990a1c952b340a2cadf8ac1ca.tl.png)

## Magaling! Ipagpatuloy ang Iyong Pag-aaral

Pagkatapos matapos ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para ipagpatuloy ang pag-level up ng iyong kaalaman sa Generative AI!

Pumunta sa Lesson 9 kung saan titingnan natin kung paano [gumawa ng mga image generation application](../09-building-image-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.