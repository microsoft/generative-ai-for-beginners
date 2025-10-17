<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58953c08b8ba7073b836d4270ea0fe86",
  "translation_date": "2025-10-17T21:10:06+00:00",
  "source_file": "08-building-search-applications/README.md",
  "language_code": "sw"
}
-->
# Kujenga Programu za Utafutaji

[![Utangulizi wa AI ya Kizazi na Mifano Mikubwa ya Lugha](../../../translated_images/08-lesson-banner.8fff48c566dad08a1cbb9f4b4a2c16adfdd288a7bbfffdd30770b466fe08c25c.sw.png)](https://youtu.be/W0-nzXjOjr0?si=GcsqiTTvd7RKbo7V)

> > _Bonyeza picha hapo juu kutazama video ya somo hili_

Mifano Mikubwa ya Lugha (LLMs) si kwa ajili ya chatbots na uzalishaji wa maandishi pekee. Inawezekana pia kujenga programu za utafutaji kwa kutumia Embeddings. Embeddings ni uwakilishi wa namba wa data unaojulikana pia kama vectors, na unaweza kutumika kwa utafutaji wa kimaana wa data.

Katika somo hili, utajenga programu ya utafutaji kwa ajili ya kampuni yetu ya elimu. Kampuni yetu ni shirika lisilo la faida linalotoa elimu bure kwa wanafunzi katika nchi zinazoendelea. Kampuni yetu ina idadi kubwa ya video za YouTube ambazo wanafunzi wanaweza kutumia kujifunza kuhusu AI. Kampuni yetu inataka kujenga programu ya utafutaji inayoruhusu wanafunzi kutafuta video za YouTube kwa kuandika swali.

Kwa mfano, mwanafunzi anaweza kuandika 'Jupyter Notebooks ni nini?' au 'Azure ML ni nini?' na programu ya utafutaji itarudisha orodha ya video za YouTube zinazohusiana na swali hilo, na bora zaidi, programu ya utafutaji itarudisha kiungo cha sehemu ya video ambapo jibu la swali linapatikana.

## Utangulizi

Katika somo hili, tutajadili:

- Utafutaji wa Kimaana dhidi ya Utafutaji wa Maneno Muhimu.
- Embeddings za Maandishi ni nini.
- Kuunda Kielezo cha Embeddings za Maandishi.
- Kutafuta katika Kielezo cha Embeddings za Maandishi.

## Malengo ya Kujifunza

Baada ya kukamilisha somo hili, utaweza:

- Kutofautisha kati ya utafutaji wa kimaana na utafutaji wa maneno muhimu.
- Kuelezea Embeddings za Maandishi ni nini.
- Kuunda programu kwa kutumia Embeddings kutafuta data.

## Kwa nini kujenga programu ya utafutaji?

Kuunda programu ya utafutaji kutakusaidia kuelewa jinsi ya kutumia Embeddings kutafuta data. Pia utajifunza jinsi ya kujenga programu ya utafutaji ambayo wanafunzi wanaweza kutumia kupata taarifa haraka.

Somo linajumuisha Kielezo cha Embeddings cha maandishi ya video za YouTube za kituo cha Microsoft [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1). AI Show ni kituo cha YouTube kinachofundisha kuhusu AI na ujifunzaji wa mashine. Kielezo cha Embeddings kina Embeddings za kila maandishi ya video za YouTube hadi Oktoba 2023. Utatumia Kielezo cha Embeddings kujenga programu ya utafutaji kwa kampuni yetu. Programu ya utafutaji itarudisha kiungo cha sehemu ya video ambapo jibu la swali linapatikana. Hii ni njia nzuri kwa wanafunzi kupata taarifa wanazohitaji haraka.

Ifuatayo ni mfano wa swali la kimaana kwa swali 'je, unaweza kutumia rstudio na azure ml?'. Angalia URL ya YouTube, utaona URL ina timestamp inayokupeleka kwenye sehemu ya video ambapo jibu la swali linapatikana.

![Swali la kimaana kwa swali "je, unaweza kutumia rstudio na Azure ML"](../../../translated_images/query-results.bb0480ebf025fac69c5179ad4d53b6627d643046838c857dc9e2b1281f1cdeb7.sw.png)

## Utafutaji wa kimaana ni nini?

Sasa unaweza kuwa unajiuliza, utafutaji wa kimaana ni nini? Utafutaji wa kimaana ni mbinu ya utafutaji inayotumia maana ya maneno katika swali kurudisha matokeo yanayofaa.

Hapa kuna mfano wa utafutaji wa kimaana. Tuseme unatafuta kununua gari, unaweza kutafuta 'gari la ndoto yangu', utafutaji wa kimaana unaelewa kuwa hauko `ndotoni` kuhusu gari, bali unatafuta kununua gari lako `bora`. Utafutaji wa kimaana unaelewa nia yako na kurudisha matokeo yanayofaa. Njia mbadala ni `utafutaji wa maneno muhimu` ambao ungetafuta ndoto kuhusu magari na mara nyingi kurudisha matokeo yasiyofaa.

## Embeddings za Maandishi ni nini?

[Embeddings za maandishi](https://en.wikipedia.org/wiki/Word_embedding?WT.mc_id=academic-105485-koreyst) ni mbinu ya uwakilishi wa maandishi inayotumika katika [usindikaji wa lugha asilia](https://en.wikipedia.org/wiki/Natural_language_processing?WT.mc_id=academic-105485-koreyst). Embeddings za maandishi ni uwakilishi wa namba wa kimaana wa maandishi. Embeddings hutumika kuwakilisha data kwa njia ambayo ni rahisi kwa mashine kuelewa. Kuna mifano mingi ya kujenga embeddings za maandishi, katika somo hili, tutazingatia kuzalisha embeddings kwa kutumia OpenAI Embedding Model.

Hapa kuna mfano, fikiria maandishi yafuatayo yako katika maandishi ya moja ya vipindi vya kituo cha YouTube cha AI Show:

```text
Today we are going to learn about Azure Machine Learning.
```

Tungepitisha maandishi kwa OpenAI Embedding API na ingerudisha embedding ifuatayo yenye namba 1536 inayojulikana kama vector. Kila namba katika vector inawakilisha kipengele tofauti cha maandishi. Kwa ufupi, hapa kuna namba 10 za kwanza katika vector.

```python
[-0.006655829958617687, 0.0026128944009542465, 0.008792596869170666, -0.02446001023054123, -0.008540431968867779, 0.022071078419685364, -0.010703742504119873, 0.003311325330287218, -0.011632772162556648, -0.02187200076878071, ...]
```

## Kielezo cha Embedding kinaundwaje?

Kielezo cha Embedding kwa somo hili kiliundwa kwa mfululizo wa script za Python. Utapata script pamoja na maelekezo katika [README](./scripts/README.md?WT.mc_id=academic-105485-koreyst) katika folda ya 'scripts' ya somo hili. Huna haja ya kuendesha script hizi kukamilisha somo hili kwani Kielezo cha Embedding kimeandaliwa kwa ajili yako.

Script zinafanya kazi zifuatazo:

1. Maandishi ya kila video ya YouTube katika orodha ya nyimbo ya [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) yanapakuliwa.
2. Kwa kutumia [OpenAI Functions](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling?WT.mc_id=academic-105485-koreyst), jaribio linafanywa la kutoa jina la msemaji kutoka dakika 3 za kwanza za maandishi ya YouTube. Jina la msemaji wa kila video linahifadhiwa katika Kielezo cha Embedding kinachoitwa `embedding_index_3m.json`.
3. Maandishi ya maandishi yanagawanywa katika **vipande vya maandishi vya dakika 3**. Kila kipande kinajumuisha maneno 20 yanayofuatana kutoka kipande kinachofuata ili kuhakikisha kuwa Embedding ya kipande haikatwi na kutoa muktadha bora wa utafutaji.
4. Kila kipande cha maandishi kinapitishwa kwa OpenAI Chat API ili kufupishwa kuwa maneno 60. Muhtasari pia unahifadhiwa katika Kielezo cha Embedding `embedding_index_3m.json`.
5. Hatimaye, maandishi ya kipande yanapitishwa kwa OpenAI Embedding API. Embedding API inarudisha vector ya namba 1536 inayowakilisha maana ya kimaana ya kipande. Kipande pamoja na vector ya OpenAI Embedding inahifadhiwa katika Kielezo cha Embedding `embedding_index_3m.json`.

### Maktaba za Vector

Kwa urahisi wa somo, Kielezo cha Embedding kinahifadhiwa katika faili ya JSON inayoitwa `embedding_index_3m.json` na kupakiwa kwenye Pandas DataFrame. Hata hivyo, katika uzalishaji, Kielezo cha Embedding kingehifadhiwa katika maktaba ya vector kama [Azure Cognitive Search](https://learn.microsoft.com/training/modules/improve-search-results-vector-search?WT.mc_id=academic-105485-koreyst), [Redis](https://cookbook.openai.com/examples/vector_databases/redis/readme?WT.mc_id=academic-105485-koreyst), [Pinecone](https://cookbook.openai.com/examples/vector_databases/pinecone/readme?WT.mc_id=academic-105485-koreyst), [Weaviate](https://cookbook.openai.com/examples/vector_databases/weaviate/readme?WT.mc_id=academic-105485-koreyst), na nyinginezo.

## Kuelewa mfanano wa cosine

Tumeelewa kuhusu embeddings za maandishi, hatua inayofuata ni kujifunza jinsi ya kutumia embeddings za maandishi kutafuta data na hasa kupata embeddings zinazofanana zaidi na swali fulani kwa kutumia mfanano wa cosine.

### Mfanano wa cosine ni nini?

Mfanano wa cosine ni kipimo cha kufanana kati ya vectors mbili, pia utasikia ikitajwa kama `utafutaji wa jirani wa karibu`. Ili kufanya utafutaji wa mfanano wa cosine unahitaji _kuweka vector_ kwa maandishi ya _swali_ kwa kutumia OpenAI Embedding API. Kisha hesabu _mfanano wa cosine_ kati ya vector ya swali na kila vector katika Kielezo cha Embedding. Kumbuka, Kielezo cha Embedding kina vector kwa kila kipande cha maandishi ya video ya YouTube. Hatimaye, panga matokeo kwa mfanano wa cosine na vipande vya maandishi vilivyo na mfanano wa juu wa cosine ndivyo vinavyofanana zaidi na swali.

Kwa mtazamo wa hisabati, mfanano wa cosine hupima cosine ya pembe kati ya vectors mbili zilizoprojekwa katika nafasi ya multidimensional. Kipimo hiki ni muhimu, kwa sababu ikiwa hati mbili ziko mbali kwa umbali wa Euclidean kwa sababu ya ukubwa, zinaweza bado kuwa na pembe ndogo kati yao na hivyo mfanano wa juu wa cosine. Kwa maelezo zaidi kuhusu hesabu za mfanano wa cosine, angalia [Cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity?WT.mc_id=academic-105485-koreyst).

## Kujenga programu yako ya kwanza ya utafutaji

Ifuatayo, tutajifunza jinsi ya kujenga programu ya utafutaji kwa kutumia Embeddings. Programu ya utafutaji itaruhusu wanafunzi kutafuta video kwa kuandika swali. Programu ya utafutaji itarudisha orodha ya video zinazohusiana na swali. Programu ya utafutaji pia itarudisha kiungo cha sehemu ya video ambapo jibu la swali linapatikana.

Suluhisho hili lilijengwa na kujaribiwa kwenye Windows 11, macOS, na Ubuntu 22.04 kwa kutumia Python 3.10 au zaidi. Unaweza kupakua Python kutoka [python.org](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

## Kazi - kujenga programu ya utafutaji, kuwawezesha wanafunzi

Tulianzisha kampuni yetu mwanzoni mwa somo hili. Sasa ni wakati wa kuwawezesha wanafunzi kujenga programu ya utafutaji kwa ajili ya tathmini zao.

Katika kazi hii, utaunda Huduma za Azure OpenAI ambazo zitatumika kujenga programu ya utafutaji. Utaunda Huduma zifuatazo za Azure OpenAI. Utahitaji usajili wa Azure kukamilisha kazi hii.

### Anzisha Azure Cloud Shell

1. Ingia kwenye [Azure portal](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst).
2. Chagua ikoni ya Cloud Shell kwenye kona ya juu kulia ya Azure portal.
3. Chagua **Bash** kwa aina ya mazingira.

#### Unda kikundi cha rasilimali

> Kwa maelekezo haya, tunatumia kikundi cha rasilimali kinachoitwa "semantic-video-search" katika East US.
> Unaweza kubadilisha jina la kikundi cha rasilimali, lakini unapobadilisha eneo la rasilimali,
> angalia [jedwali la upatikanaji wa mifano](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```shell
az group create --name semantic-video-search --location eastus
```

#### Unda rasilimali ya Huduma ya Azure OpenAI

Kutoka Azure Cloud Shell, endesha amri ifuatayo kuunda rasilimali ya Huduma ya Azure OpenAI.

```shell
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

#### Pata endpoint na funguo za matumizi katika programu hii

Kutoka Azure Cloud Shell, endesha amri zifuatazo kupata endpoint na funguo za rasilimali ya Huduma ya Azure OpenAI.

```shell
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

#### Peleka mfano wa OpenAI Embedding

Kutoka Azure Cloud Shell, endesha amri ifuatayo kupeleka mfano wa OpenAI Embedding.

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

Fungua [notebook ya suluhisho](./python/aoai-solution.ipynb?WT.mc_id=academic-105485-koreyst) katika GitHub Codespaces na fuata maelekezo katika Jupyter Notebook.

Unapoendesha notebook, utaombwa kuingiza swali. Kisanduku cha kuingiza kitaonekana kama hiki:

![Kisanduku cha kuingiza kwa mtumiaji kuingiza swali](../../../translated_images/notebook-search.1e320b9c7fcbb0bc1436d98ea6ee73b4b54ca47990a1c952b340a2cadf8ac1ca.sw.png)

## Kazi Nzuri! Endelea Kujifunza

Baada ya kukamilisha somo hili, angalia [mkusanyiko wa Kujifunza AI ya Kizazi](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuongeza maarifa yako ya AI ya Kizazi!

Nenda kwenye Somo la 9 ambapo tutatazama jinsi ya [kujenga programu za kizazi cha picha](../09-building-image-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.