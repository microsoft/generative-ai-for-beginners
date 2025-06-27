<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d46aad0917a1a342d613e2c13d457da5",
  "translation_date": "2025-06-25T16:39:21+00:00",
  "source_file": "08-building-search-applications/README.md",
  "language_code": "sw"
}
-->
# Kujenga Programu za Utafutaji

> > _Bonyeza picha hapo juu kutazama video ya somo hili_

Kuna mengi zaidi kwa LLMs kuliko chatbots na uzalishaji wa maandishi. Inawezekana pia kujenga programu za utafutaji kwa kutumia Embeddings. Embeddings ni uwakilishi wa nambari wa data pia hujulikana kama vectors, na zinaweza kutumika kwa utafutaji wa semantic kwa data.

Katika somo hili, utajenga programu ya utafutaji kwa ajili ya kampuni yetu ya elimu. Kampuni yetu ni shirika lisilo la faida linalotoa elimu ya bure kwa wanafunzi katika nchi zinazoendelea. Kampuni yetu ina idadi kubwa ya video za YouTube ambazo wanafunzi wanaweza kutumia kujifunza kuhusu AI. Kampuni yetu inataka kujenga programu ya utafutaji inayowawezesha wanafunzi kutafuta video ya YouTube kwa kuandika swali.

Kwa mfano, mwanafunzi anaweza kuandika 'Je, Jupyter Notebooks ni nini?' au 'Azure ML ni nini?' na programu ya utafutaji itarudisha orodha ya video za YouTube zinazohusiana na swali hilo, na bora zaidi, programu ya utafutaji itarudisha kiungo mahali ambapo jibu la swali linapatikana katika video.

## Utangulizi

Katika somo hili, tutashughulikia:

- Utafutaji wa semantic dhidi ya utafutaji wa maneno muhimu.
- Embeddings za maandishi ni nini.
- Kuunda Index ya Embeddings za Maandishi.
- Kutafuta Index ya Embeddings za Maandishi.

## Malengo ya Kujifunza

Baada ya kukamilisha somo hili, utaweza:

- Kutofautisha kati ya utafutaji wa semantic na utafutaji wa maneno muhimu.
- Kuelezea Embeddings za Maandishi ni nini.
- Kuunda programu kwa kutumia Embeddings kutafuta data.

## Kwa nini kujenga programu ya utafutaji?

Kuunda programu ya utafutaji kutakusaidia kuelewa jinsi ya kutumia Embeddings kutafuta data. Pia utajifunza jinsi ya kujenga programu ya utafutaji ambayo inaweza kutumiwa na wanafunzi kupata taarifa haraka.

Somo linajumuisha Embedding Index ya maandiko ya YouTube kwa kituo cha Microsoft [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1). AI Show ni kituo cha YouTube kinachokufundisha kuhusu AI na ujifunzaji wa mashine. Embedding Index ina Embeddings za kila moja ya maandiko ya YouTube hadi Oktoba 2023. Utatumia Embedding Index kujenga programu ya utafutaji kwa kampuni yetu. Programu ya utafutaji inarudisha kiungo mahali ambapo jibu la swali linapatikana katika video. Hii ni njia nzuri kwa wanafunzi kupata taarifa wanazohitaji haraka.

Ifuatayo ni mfano wa swali la semantic kwa swali 'unaweza kutumia rstudio na azure ml?'. Angalia url ya YouTube, utaona url ina timestamp inayokupeleka mahali ambapo jibu la swali linapatikana katika video.

## Utafutaji wa semantic ni nini?

Sasa unaweza kujiuliza, utafutaji wa semantic ni nini? Utafutaji wa semantic ni mbinu ya utafutaji inayotumia semantics, au maana, ya maneno katika swali kurudisha matokeo yanayohusiana.

Hapa kuna mfano wa utafutaji wa semantic. Tuseme unatafuta kununua gari, unaweza kutafuta 'gari langu la ndoto', utafutaji wa semantic unaelewa kuwa hauzungumzi `dreaming` kuhusu gari, lakini unatafuta kununua `ideal` gari lako. Utafutaji wa semantic unaelewa nia yako na unarudisha matokeo yanayohusiana. Njia mbadala ni `keyword search` ambayo ingeweza kutafuta ndoto kuhusu magari na mara nyingi kurudisha matokeo yasiyohusiana.

## Embeddings za Maandishi ni nini?

[Embeddings za maandishi](https://en.wikipedia.org/wiki/Word_embedding?WT.mc_id=academic-105485-koreyst) ni mbinu ya uwakilishi wa maandishi inayotumiwa katika [usindikaji wa lugha asilia](https://en.wikipedia.org/wiki/Natural_language_processing?WT.mc_id=academic-105485-koreyst). Embeddings za maandishi ni uwakilishi wa nambari wa semantic wa maandishi. Embeddings zinatumika kuwakilisha data kwa njia ambayo ni rahisi kwa mashine kuelewa. Kuna mifano mingi ya kujenga embeddings za maandishi, katika somo hili, tutazingatia kuzalisha embeddings kwa kutumia OpenAI Embedding Model.

Hapa kuna mfano, fikiria maandishi yafuatayo yako katika maandiko kutoka kwa moja ya vipindi kwenye kituo cha YouTube cha AI Show:

```text
Today we are going to learn about Azure Machine Learning.
```

Tungepitisha maandishi kwa OpenAI Embedding API na ingerudisha embedding ifuatayo inayojumuisha namba 1536 aka vector. Kila namba katika vector inawakilisha kipengele tofauti cha maandishi. Kwa ufupi, hapa kuna namba 10 za kwanza katika vector.

```python
[-0.006655829958617687, 0.0026128944009542465, 0.008792596869170666, -0.02446001023054123, -0.008540431968867779, 0.022071078419685364, -0.010703742504119873, 0.003311325330287218, -0.011632772162556648, -0.02187200076878071, ...]
```

## Jinsi gani Index ya Embedding inaundwa?

Index ya Embedding kwa somo hili iliundwa na mfululizo wa scripts za Python. Utapata scripts pamoja na maelekezo katika [README](./scripts/README.md?WT.mc_id=academic-105485-koreyst) katika folda ya 'scripts' kwa somo hili. Huhitaji kuendesha scripts hizi kukamilisha somo hili kwani Embedding Index imetolewa kwako.

Scripts zinafanya shughuli zifuatazo:

1. Maandishi ya kila video ya YouTube katika orodha ya [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) yanapakuliwa.
2. Kwa kutumia [OpenAI Functions](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling?WT.mc_id=academic-105485-koreyst), jaribio linafanywa kutoa jina la msemaji kutoka kwa dakika 3 za kwanza za maandiko ya YouTube. Jina la msemaji kwa kila video linawekwa katika Embedding Index inayoitwa `embedding_index_3m.json`.
3. Maandishi ya maandiko yanagawanywa katika **vipande vya maandishi vya dakika 3**. Kipande kinajumuisha kuhusu maneno 20 yanayokutana kutoka kipande kinachofuata ili kuhakikisha kuwa Embedding ya kipande haikatiwi na kutoa muktadha bora wa utafutaji.
4. Kila kipande cha maandishi kinapitishwa kwa OpenAI Chat API kusummarize maandishi katika maneno 60. Muhtasari pia umehifadhiwa katika Embedding Index `embedding_index_3m.json`.
5. Hatimaye, maandishi ya kipande yanapitishwa kwa OpenAI Embedding API. Embedding API inarudisha vector ya namba 1536 inayowakilisha maana ya semantic ya kipande. Kipande pamoja na vector ya OpenAI Embedding imehifadhiwa katika Embedding Index `embedding_index_3m.json`.

### Databases za Vector

Kwa urahisi wa somo, Embedding Index imehifadhiwa katika faili ya JSON inayoitwa `embedding_index_3m.json` na kupakiwa katika Pandas DataFrame. Hata hivyo, katika uzalishaji, Embedding Index ingeweza kuhifadhiwa katika database ya vector kama [Azure Cognitive Search](https://learn.microsoft.com/training/modules/improve-search-results-vector-search?WT.mc_id=academic-105485-koreyst), [Redis](https://cookbook.openai.com/examples/vector_databases/redis/readme?WT.mc_id=academic-105485-koreyst), [Pinecone](https://cookbook.openai.com/examples/vector_databases/pinecone/readme?WT.mc_id=academic-105485-koreyst), [Weaviate](https://cookbook.openai.com/examples/vector_databases/weaviate/readme?WT.mc_id=academic-105485-koreyst), kutaja chache.

## Kuelewa cosine similarity

Tumejifunza kuhusu embeddings za maandishi, hatua inayofuata ni kujifunza jinsi ya kutumia embeddings za maandishi kutafuta data na hasa kupata embeddings zinazofanana zaidi kwa swali lililopewa kwa kutumia cosine similarity.

### Cosine similarity ni nini?

Cosine similarity ni kipimo cha ufanano kati ya vectors mbili, pia utasikia hii ikitajwa kama `nearest neighbor search`. Ili kufanya utafutaji wa cosine similarity unahitaji _kuvectorize_ kwa maandishi ya _query_ kwa kutumia OpenAI Embedding API. Kisha hesabu _cosine similarity_ kati ya vector ya query na kila vector katika Embedding Index. Kumbuka, Embedding Index ina vector kwa kila kipande cha maandiko ya YouTube. Hatimaye, panga matokeo kwa cosine similarity na vipande vya maandishi vilivyo na cosine similarity ya juu zaidi ni vile vinavyofanana zaidi na query.

Kutoka mtazamo wa hisabati, cosine similarity hupima cosine ya pembe kati ya vectors mbili zilizoprojekwa katika nafasi ya multidimensional. Kipimo hiki ni cha manufaa, kwa sababu ikiwa hati mbili ziko mbali kwa umbali wa Euclidean kwa sababu ya ukubwa, bado zinaweza kuwa na pembe ndogo kati yao na kwa hivyo cosine similarity ya juu. Kwa habari zaidi kuhusu equations za cosine similarity, angalia [Cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity?WT.mc_id=academic-105485-koreyst).

## Kujenga programu yako ya kwanza ya utafutaji

Ifuatayo, tutajifunza jinsi ya kujenga programu ya utafutaji kwa kutumia Embeddings. Programu ya utafutaji itawawezesha wanafunzi kutafuta video kwa kuandika swali. Programu ya utafutaji itarudisha orodha ya video zinazohusiana na swali. Programu ya utafutaji pia itarudisha kiungo mahali ambapo jibu la swali linapatikana katika video.

Suluhisho hili liliundwa na kupimwa kwenye Windows 11, macOS, na Ubuntu 22.04 kwa kutumia Python 3.10 au baadaye. Unaweza kupakua Python kutoka [python.org](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

## Kazi - kujenga programu ya utafutaji, kuwezesha wanafunzi

Tulianzisha kampuni yetu mwanzoni mwa somo hili. Sasa ni wakati wa kuwezesha wanafunzi kujenga programu ya utafutaji kwa ajili ya tathmini zao.

Katika kazi hii, utaunda Huduma za Azure OpenAI ambazo zitatumika kujenga programu ya utafutaji. Utaunda Huduma za Azure OpenAI zifuatazo. Utahitaji usajili wa Azure kukamilisha kazi hii.

### Anzisha Azure Cloud Shell

1. Ingia kwenye [Azure portal](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst).
2. Chagua ikoni ya Cloud Shell katika kona ya juu-kulia ya Azure portal.
3. Chagua **Bash** kwa aina ya mazingira.

#### Unda kikundi cha rasilimali

> Kwa maelekezo haya, tunatumia kikundi cha rasilimali kinachoitwa "semantic-video-search" katika Mashariki ya Marekani.
> Unaweza kubadilisha jina la kikundi cha rasilimali, lakini unapobadilisha eneo la rasilimali,
> angalia [jedwali la upatikanaji wa modeli](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```shell
az group create --name semantic-video-search --location eastus
```

#### Unda rasilimali ya Huduma ya Azure OpenAI

Kutoka Azure Cloud Shell, endesha amri ifuatayo kuunda rasilimali ya Huduma ya Azure OpenAI.

```shell
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

#### Pata mwisho na funguo za matumizi katika programu hii

Kutoka Azure Cloud Shell, endesha amri zifuatazo kupata mwisho na funguo za rasilimali ya Huduma ya Azure OpenAI.

```shell
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

#### Peleka modeli ya OpenAI Embedding

Kutoka Azure Cloud Shell, endesha amri ifuatayo kupeleka modeli ya OpenAI Embedding.

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

## Suluhisho

Fungua [notebook ya suluhisho](../../../08-building-search-applications/python/aoai-solution.ipynb) katika GitHub Codespaces na fuata maelekezo katika Jupyter Notebook.

Unapoendesha notebook, utahitajika kuingiza swali. Kisanduku cha ingizo kitaonekana kama hiki:

## Kazi Nzuri! Endelea Kujifunza

Baada ya kukamilisha somo hili, angalia [mkusanyiko wetu wa Kujifunza AI ya Kizazi](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuongeza maarifa yako ya AI ya Kizazi!

Nenda kwenye Somo la 9 ambapo tutatazama jinsi ya [kujenga programu za kizazi cha picha](../09-building-image-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Kanusho**: 
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwepo kwa usahihi. Hati asilia katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo chenye mamlaka. Kwa habari muhimu, tafsiri ya kitaalamu ya kibinadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.