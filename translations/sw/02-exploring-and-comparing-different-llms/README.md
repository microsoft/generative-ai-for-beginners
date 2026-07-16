# Kuchunguza na kulinganisha aina tofauti za LLMs

[![Kuchunguza na kulinganisha aina tofauti za LLMs](../../../translated_images/sw/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Bofya picha hapo juu kutazama video ya somo hili_

Kwa somo lililopita, tumeona jinsi AI ya Kizazi inavyobadilisha mazingira ya teknolojia, jinsi Modeli Kubwa za Lugha (LLMs) zinavyofanya kazi na jinsi biashara - kama kampuni yetu ya kuanzisha - inaweza kuzitumia kwa matumizi yao na kukua! Katika sura hii, tunatafuta kulinganisha na kutofautisha aina tofauti za modeli kubwa za lugha (LLMs) ili kuelewa faida na hasara zao.

Hatua inayofuata katika safari ya kuanzisha ni kuchunguza mazingira ya sasa ya LLMs na kuelewa ni zipi zinazofaa kwa matumizi yetu.

## Utangulizi

Somo hili litajumuisha:

- Aina tofauti za LLMs katika mazingira ya sasa.
- Kujaribu, kurudia, na kulinganisha modeli tofauti kwa matumizi yako katika Azure.
- Jinsi ya kupeleka LLM.

## Malengo ya Kujifunza

Baada ya kumaliza somo hili, utaweza:

- Kuchagua modeli sahihi kwa matumizi yako.
- Kuelewa jinsi ya kujaribu, kurudia, na kuboresha utendaji wa modeli yako.
- Kujua jinsi biashara zinavyopunguza modeli.

## Elewa aina tofauti za LLMs

LLMs zinaweza kuwa na aina nyingi kulingana na usanifu wao, data za mafunzo, na matumizi. Kuelewa tofauti hizi kutasaidia kampuni yetu ya kuanzisha kuchagua modeli sahihi kwa tukio, na kuelewa jinsi ya kujaribu, kurudia, na kuboresha utendaji.

Kuna aina nyingi tofauti za modeli za LLM, uchaguzi wako wa modeli unategemea unachotaka kuzitumia kwa, data yako, kiasi unachotaka kulipa na zaidi.

Kulingana na kama unataka kutumia modeli kwa maandishi, sauti, video, uzalishaji picha n.k., unaweza kuchagua aina tofauti ya modeli.

- **Utambuzi wa sauti na kuzungumza**. Modeli za mtindo wa Whisper bado ni muhimu kama modeli za jumla za utambuzi sauti, lakini chaguzi za uzalishaji sasa pia ni pamoja na modeli mpya za sauti-kwenda-maandishi kama `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`, na aina za diarization. Tathmini usambazaji wa lugha, diarization, msaada wa wakati halisi, kuchelewa, na gharama kwa tukio lako. Jifunze zaidi katika [nyaraka za OpenAI za sauti-kwenda-maandishi](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst).

- **Uzalishaji picha**. DALL-E na Midjourney ni chaguzi maarufu za uzalishaji picha, lakini API za picha za OpenAI sasa zinazingatia modeli za Picha za GPT kama `gpt-image-2`, wakati Stable Diffusion, Imagen, Flux, na familia nyingine za modeli pia ni chaguo maarufu. Linganisha ufuataji wa maelekezo, msaada wa uhariri, udhibiti wa mtindo, mahitaji ya usalama, na leseni. Jifunze zaidi katika [mwongozo wa uzalishaji picha wa OpenAI](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) na Sura ya 9 ya mtaala huu.

- **Uzalishaji maandishi**. Modeli za maandishi sasa zina uwanja wa modeli za mbele, modeli za hoja, modeli ndogo za kuleta matokeo haraka, na modeli za uzito wazi. Mifano ya sasa ni pamoja na modeli za OpenAI GPT-5.x, modeli za Anthropic Claude 4.x, modeli za Google Gemini 3.x, modeli za Meta Llama 4, na modeli za Mistral. Usichague tu kwa tarehe ya kutolewa au bei; linganisha ubora wa kazi, ucheleweshaji, dirisha la muktadha, matumizi ya zana, tabia za usalama, upatikanaji wa kanda, na jumla ya gharama. [Orodha ya modeli ya Microsoft Foundry](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) ni mahali pazuri pa kulinganisha modeli zilizopo Azure.

- **Modality nyingi**. Modeli nyingi za sasa zinaweza kushughulikia zaidi ya maandishi. Baadhi hushughulikia picha, sauti, au video; baadhi wanaweza kuita zana; na modeli maalum zinaweza kuzalisha picha, sauti, au video. Kwa mfano, modeli za sasa za OpenAI zinaunga mkono input ya maandishi na picha, modeli za Gemini zinaweza kuunga mkono maandishi, msimbo, picha, sauti, na video kulingana na aina, na Llama 4 Scout na Maverick ni modeli za uzito wazi za asili za modality nyingi. Kila wakati angalia kadi ya modeli kupata modaliti zinazoungwa mkono kwa input na output kabla ya kujenga mtiririko.

Kuchagua modeli kunamaanisha unapata uwezo wa msingi, ingawa huenda hautoshi. Mara nyingi una data maalum za kampuni unazohitaji kumweleza LLM. Kuna chaguzi kadhaa tofauti za kukabiliana na hilo, zaidi hapo katika sehemu zinazofuata.

### Modeli za Msingi dhidi ya LLMs

Neno la Modeli ya Msingi lilitengenezwa na [watafiti wa Stanford](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) na lilifafanuliwa kama modeli ya AI inayofuata vigezo fulani, kama:

- **Zinafundishwa kwa kutumia ujifunzaji usio na msimamizi au ujifunzaji wa kujisimamia**, maana zinafundishwa kwa data zisizo na lebo za modality nyingi, na hazihitaji ufafanuzi au lebo ya binadamu kwa mchakato wa mafunzo yao.
- **Ni modeli kubwa sana**, zinazotegemea mitandao ya neva ya kina sana iliyofundishwa kwa mabilioni ya vigezo.
- **Kwa kawaida zinakusudiwa kutumika kama ‘msingi’ kwa modeli nyingine**, maana zinaweza kutumika kama msingi wa kujengewa modeli nyingine juu yake, ambacho kinaweza kufanyika kwa kusahihisha vipimo.

![Modeli za Msingi dhidi ya LLMs](../../../translated_images/sw/FoundationModel.e4859dbb7a825c94.webp)

Chanzo cha picha: [Mwongozo Muhimu wa Modeli za Msingi na Modeli Kubwa za Lugha | na Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Ili kufafanua zaidi tofauti hii, tuchukue ChatGPT kama mfano wa kihistoria. Toleo za awali za ChatGPT zilitumia GPT-3.5 kama modeli ya msingi. OpenAI kisha ilitumia data maalum ya mazungumzo na mbinu za kulinganisha kuunda toleo lililorekebishwa ambalo lilifanya vyema zaidi katika mazingira ya mazungumzo, kama vile chatbots. Huduma za kisasa za AI mara nyingi zinapita kati ya aina kadhaa za modeli, kwa hivyo jina la huduma na jina la modeli ya msingi si mara zote vitu sawa.

![Modeli ya Msingi](../../../translated_images/sw/Multimodal.2c389c6439e0fc51.webp)

Chanzo cha picha: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Modeli za Uzito-Uwazi/Open-Source dhidi ya Modeli za Mali Binafsi

Njia nyingine ya kukategorisha LLM ni kama ni uzito-uwazi, chanzo-wazi, au mila binafsi.

Modeli za chanzo wazi na uzito wazi hufanya mafaili ya modeli kupatikana kwa uhakiki, kupakua, au kubinafsisha, lakini leseni zao zinatofautiana. Baadhi ni chanzo wazi kabisa, wakati nyingine ni modeli za uzito wazi zilizo na vizuizi vya matumizi. Hizi zinaweza kusaidia wakati biashara inahitaji udhibiti zaidi juu ya utoaji, eneo la data, gharama, au ubinafsishaji. Hata hivyo, timu bado zinahitaji kupitia masharti ya leseni, gharama za kuwasilisha, matengenezo, masasisho ya usalama, na ubora wa tathmini kabla ya kuzitumia uzalishaji. Mifano ni pamoja na [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst), baadhi ya [modeli za Mistral](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst), na modeli nyingi zinazohifadhiwa kwenye [Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst).

Modeli za mali binafsi zinamilikiwa na kuhudumiwa na muuzaji. Modeli hizi mara nyingi zimeboreshwa kwa matumizi ya uzalishaji yaliyoendeshwa na hutoa msaada mzuri, mifumo ya usalama, ujumuishaji wa zana, na upanuzi. Hata hivyo, wateja kawaida hawawezi kuangalia au kubadilisha uzito wa modeli, na wanapaswa kupitia masharti ya muuzaji kuhusu faragha, uhifadhi, ufuatiliaji, na matumizi yanayokubalika. Mifano ni pamoja na [modeli za OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), [Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst), na [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst).

### Uingiliano dhidi ya Uzalishaji Picha dhidi ya Uzalishaji wa Maandishi na Msimbo

LLMs pia zinaweza kukategorishwa kwa mujibu wa matokeo yanayotengeneza.

Uingiliano ni seti ya modeli zinazoweza kubadilisha maandishi kuwa fomu nambari, inayoitwa embedding, ambayo ni uwakilishi wa nambari wa maandishi ya pembejeo. Uingiliano hufanya iwe rahisi kwa mashine kuelewa mahusiano kati ya maneno au sentensi na inaweza kutumika kama pembejeo na modeli nyingine, kama modeli za utambuzi au za upangaji ambazo zina utendaji bora kwenye data ya nambari. Modeli za embedding mara nyingi hutumika kwa ujifunzaji wa uhamisho, ambapo modeli inajengwa kwa kazi mbadala ambayo kuna data nyingi, na kisha uzito wa modeli (embedding) hutumika tena kwa kazi nyingine. Mfano katika kundi hili ni [OpenAI embeddings](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Uingiliano](../../../translated_images/sw/Embedding.c3708fe988ccf760.webp)

Modeli za uzalishaji picha ni modeli zinazozalisha picha. Modeli hizi mara nyingi hutumika kwa uhariri wa picha, usanisi wa picha, na utafsiri wa picha. Modeli za uzalishaji picha mara nyingi hufundishwa kwa seti kubwa za picha, kama [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), na zinaweza kutumika kuzalisha picha mpya au kuhariri picha zilizopo kwa mbinu za kuchora tena, azimio la juu, na kupiga rangi. Mifano ni pamoja na [modeli za GPT Image](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst), [modeli za Stable Diffusion](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst), na modeli za Imagen.

![Uzalishaji picha](../../../translated_images/sw/Image.349c080266a763fd.webp)

Modeli za uzalishaji maandishi na msimbo ni modeli zinazozalisha maandishi au msimbo. Modeli hizi mara nyingi hutumika kwa muhtasari wa maandishi, tafsiri, na kujibu maswali. Modeli za uzalishaji maandishi mara nyingi hufundishwa kwa seti kubwa za maandishi, kama [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), na zinaweza kutumika kuzalisha maandishi mapya, au kujibu maswali. Modeli za uzalishaji msimbo, kama [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), mara nyingi hufundishwa kwa seti kubwa za msimbo, kama GitHub, na zinaweza kutumika kuzalisha msimbo mpya, au kurekebisha hitilafu kwenye msimbo uliopo.

![Uzalishaji maandishi na msimbo](../../../translated_images/sw/Text.a8c0cf139e5cc2a0.webp)

### Encoder-Decoder dhidi ya Decoder-peke yake

Ili kuzungumzia aina tofauti za usanifu wa LLMs, tuchukue mfano.

Fikiria meneja wako alikupa kazi ya kuandika mtihani wa maswali kwa wanafunzi. Una wenzako wawili; mmoja anasimamia uundaji wa maudhui na mwingine anasimamia kupitia hayo.

Mjenzi wa maudhui ni kama modeli ya decoder-peke yake: anaweza kuangalia mada, kuona uliyoiandika tayari, na kisha kuendelea kuunda maudhui kulingana na muktadha huo. Wao ni wazuri sana kuandika maudhui ya kuvutia na yenye taarifa, lakini siyo kila wakati chaguo bora wakati kazi ni kutambua, kupata au kuweka taarifa. Mifano ya familia za modeli za decoder-peke ni GPT na modeli za Llama.

Mkaguzi ni kama modeli ya encoder peke, wanaangalia kozi iliyotengenezwa na majibu, kutambua uhusiano kati yao na kuelewa muktadha, lakini si wazuri katika kuzalisha maudhui. Mfano wa modeli ya encoder peke ni BERT.

Fikiria kwamba tuna mtu pia ambaye anaweza kuunda na kukagua mtihani, hii ni modeli ya Encoder-Decoder. Mifano ni BART na T5.

### Huduma dhidi ya Modeli

Sasa, tuelezee tofauti kati ya huduma na modeli. Huduma ni bidhaa inayotolewa na Mtoa Huduma wa Mawingu, na mara nyingi ni mchanganyiko wa modeli, data, na vipengele vingine. Modeli ni sehemu kuu ya huduma, na mara nyingi ni modeli ya msingi, kama LLM.

Huduma mara nyingi zimeboreshwa kwa matumizi ya uzalishaji na mara nyingi ni rahisi kutumia zaidi kuliko modeli, kupitia interface ya mtumiaji yenye picha. Hata hivyo, huduma si za bure kila wakati, na zinaweza kuhitaji usajili au malipo ili kuzitumia, kwa kubadilishana na kutumia vifaa na rasilimali za mmiliki wa huduma, kuboresha gharama na urahisi wa kupanua. Mfano wa huduma ni [Huduma ya Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), ambayo hutoa mpango wa malipo kwa matumizi, maana watumiaji hulipishwa kulingana na kiasi wanachotumia huduma. Huduma ya Azure OpenAI pia hutoa usalama wa daraja la biashara na mfumo wa AI unaowajibika juu ya uwezo wa modeli.

Modeli ni mafaili ya mtandao wa neva: vigezo, uzito, usanifu, tokenizer, na usanidi unaounga mkono. Kuendesha modeli kwa mtaa au katika mazingira binafsi kunahitaji vifaa vinavyofaa, miundombinu ya utoaji, ufuatiliaji, na leseni inayofaa ya chanzo wazi/uzito-uwazi au leseni ya kibiashara. Modeli za uzito wazi kama Llama 4 au modeli za Mistral zinaweza kuendeshwa binafsi, lakini bado zinahitaji nguvu ya kompyuta na ujuzi wa kiutendakazi.

## Jinsi ya kujaribu na kurudia na modeli tofauti ili kuelewa utendaji katika Azure


Mara timu yetu itakapochunguza mazingira ya LLM za sasa na kubaini wagombea wazuri kwa hali zao, hatua inayofuata ni kuzijaribu kwenye data zao na kwa mzigo wao wa kazi. Huu ni mchakato wa kurudia, unaofanywa kupitia majaribio na vipimo.
Mifano mingi tuliyotaja katika aya za awali (mifano ya OpenAI, mifano yenye uzito wazi kama Llama 4 na Mistral, na mifano ya Hugging Face) inapatikana katika [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst).

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst), hapo awali Azure AI Studio/Azure AI Foundry, ni jukwaa la Azure lililounganishwa kwa ajili ya kujenga programu na mawakala wa AI. Husaidia waendelezaji kusimamia mzunguko wa maisha kutoka kwa majaribio na tathmini hadi utekelezaji, ufuatiliaji, na udhibiti. Katalogi ya modeli katika Microsoft Foundry inamruhusu mtumiaji:

- Kupata mfano wa msingi wa umuhimu katika katalogi, ikijumuisha mifano inayouzwa na Azure na mifano kutoka kwa washirika na watoa huduma wa jamii. Watumiaji wanaweza kuchuja kwa kazi, mtoa huduma, leseni, chaguo la utekelezaji, au jina.

![Katalogi ya mfano](../../../translated_images/sw/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- Pitia kadi ya mfano, ikijumuisha maelezo ya kina ya matumizi yaliyokusudiwa na data ya mafunzo, mifano ya msimbo na matokeo ya tathmini kwenye maktaba ya tathmini za ndani.

![Kadi ya mfano](../../../translated_images/sw/ModelCard.598051692c6e400d.webp)

- Linganisha vikasha vya kumbukumbu kati ya mifano na seti za data zinazopatikana katika sekta ili kutathmini ni ipi inayokidhi hali ya biashara, kupitia jopo la [Model Benchmarks](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst).

![Vikasha vya mfano](../../../translated_images/sw/ModelBenchmarks.254cb20fbd06c03a.webp)

- Rekebisha mifano inayounga mkono kwa data ya mafunzo maalum ili kuboresha utendakazi wa mfano katika mzigo maalum wa kazi, ukitumia uwezo wa majaribio na ufuatiliaji wa Microsoft Foundry.

![Kurekebisha mfano](../../../translated_images/sw/FineTuning.aac48f07142e36fd.webp)

- Tekeleza mfano wa awali uliotengenezwa awali au toleo lililorekebishwa kwenye sehemu ya ufanisi ya wakati halisi ya mbali, ukitumia chaguzi za kompyuta zinazosimamiwa au utekelezaji usio na seva, ili kufanya programu zielewe.

![Utekelezaji wa mfano](../../../translated_images/sw/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> Sio mifano yote katika katalogi inapatikana kwa sasa kwa ajili ya kurekebisha na/au utekelezaji wa malipo-kama-unavyo-tumia. Angalia kadi ya mfano kwa maelezo juu ya uwezo na mipaka ya mfano.

## Kuboresha Matokeo ya LLM

Tumepitia na timu yetu ya kuanzisha aina tofauti za LLMs na jukwaa la wingu (Microsoft Foundry) linalotuwezesha kulinganisha mifano tofauti, kuitathmini kwenye data za majaribio, kuboresha utendakazi, na kuzipeleka kwenye sehemu za kutabiri.

Lakini lini wanapaswa kuzingatia kurekebisha mfano badala ya kutumia ule uliotengenezwa awali? Je, kuna mbinu nyingine za kuboresha utendakazi wa mfano kwenye mzigo maalum wa kazi?

Kuna mbinu kadhaa ambazo biashara inaweza kutumia kupata matokeo wanayohitaji kutoka kwenye LLM. Unaweza kuchagua aina tofauti za mifano zilizo na viwango tofauti vya mafunzo wakati wa kupeleka LLM katika uzalishaji, zikiwa na ngazi tofauti za ugumu, gharama, na ubora. Hapa kuna mbinu tofauti:

- **Uhandisi wa prompt kwa muktadha**. Wazo ni kutoa muktadha wa kutosha unapotoa prompt ili kuhakikisha unapata majibu unayohitaji.

- **Uzazi ulioimarishwa kwa kupata taarifa, RAG**. Data yako inaweza kuwepo katika hifadhidata au sehemu ya mtandao kwa mfano, ili kuhakikisha data hii, au sehemu yake ndogo, inajumuishwa wakati wa kutoa prompt, unaweza kuchukua data husika na kuifanya sehemu ya prompt ya mtumiaji.

- **Mfano uliorekebishwa**. Hapa, umefunza mfano zaidi kwa data yako mwenyewe ambayo ilisababisha mfano kuwa sahihi zaidi na unaojibu mahitaji yako lakini inaweza kuwa na gharama kubwa.

![Utekelezaji wa LLMs](../../../translated_images/sw/Deploy.18b2d27412ec8c02.webp)

Chanzo cha picha: [Njia Nne Ambazo Biashara Zinazoweka LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Uhandisi wa Prompt kwa Muktadha

LLMs zilizotengenezwa awali hufanya kazi vizuri sana kwa kazi za lugha asilia za jumla, hata kwa kuwaita na prompt fupi, kama sentensi ya kukamilisha au swali – inayoitwa kujifunza “zero-shot.”

Hata hivyo, kadri mtumiaji anavyoweza kuweka muktadha kwa maombi yao, kwa ombi la kina na mifano – Muktadha – ndivyo jibu litakavyokuwa sahihi zaidi na karibu zaidi na matarajio ya mtumiaji. Katika kesi hii, tunazungumzia “one-shot” kujifunza ikiwa prompt ina mfano mmoja tu na “few-shot learning” ikiwa ina mifano mingi.
Uhandisi wa prompt kwa muktadha ni njia yenye gharama nafuu zaidi ya kuanza nayo.

### Uzazi ulioimarishwa kwa Kupata Taarifa (RAG)

LLMs zina kikomo cha kutumia data tu ambayo imetumika wakati wa mafunzo yao kutoa jibu. Hii ina maana kwamba hazijui chochote kuhusu matukio yaliyojiri baada ya mchakato wao wa mafunzo, na hawawezi kupata taarifa zisizo za umma (kama data ya kampuni).
Hii inaweza kushughulikiwa kupitia RAG, mbinu inayoongeza prompt kwa data za nje katika sehemu za nyaraka, ikizingatia kikomo cha urefu wa prompt. Hii inasaidiwa na zana za Hifadhidata za Vector (kama [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) ambazo huchukua sehemu muhimu kutoka kwa vyanzo vya data vilivyotangazwa awali na kuviweka kwenye Muktadha wa prompt.

Mbinu hii ni msaada sana wakati biashara haina data ya kutosha, wakati wa kutosha, au rasilimali za kurekebisha LLM, lakini bado inataka kuboresha utendakazi kwenye mzigo maalum wa kazi na kupunguza hatari za majibu yanayodanganya, zamani, au yasiyoungwa mkono.

### Mfano uliorekebishwa

Kurekebisha ni mchakato unaotumia kujifunza kwa uhamisho ‘kurekebisha’ mfano kwa kazi ndogo au kutatua tatizo maalum. Tofauti na few-shot learning na RAG, inasababisha mfano mpya kutengenezwa, wenye uzito na upendeleo uliosasishwa. Inahitaji seti ya mifano ya mafunzo inayojumuisha ingizo moja (prompt) na matokeo yake yaliyoambatana (ukamilishaji).
Hii itakuwa njia inayopendelewa ikiwa:

- **Kutumia mifano midogo ya kazi maalum**. Biashara ingeweza kutaka kurekebisha mfano mdogo kwa kazi nyembamba badala ya kuendelea kutoa prompt kwa mfano mkubwa zaidi, na kusababisha suluhisho zuri zaidi kwa gharama nafuu na kwa haraka.

- **Kuzingatia ucheleweshaji**. Ucheleweshaji ni muhimu kwa matumizi maalum, kwa hivyo siwezi kutumia prompt ndefu sana au idadi ya mifano ambayo inapaswa kujifunzwa na mfano haifai kwa kikomo cha urefu wa prompt.

- **Kurekebisha tabia thabiti**. Biashara ina mifano mingi yenye ubora wa juu na inataka mfano ufuate mfululizo wa kazi, muundo wa uzalishaji, mtindo wa ton, au mtindo maalum wa sekta. Ikiwa tatizo kuu ni ukweli mpya au ujuzi binafsi unaobadilika mara kwa mara, tumia RAG badala ya kutegemea kurekebisha tu.

### Mfano uliotengenezwa

Kufunza LLM kutoka mwanzoni ni bila shaka njia ngumu zaidi na tata zaidi kuchukua, inahitaji kiasi kikubwa cha data, rasilimali zenye ujuzi, na nguvu ya kompyuta inayofaa. Chaguo hili linapaswa kuzingatiwa tu katika hali ambapo biashara ina matumizi maalum ya sekta na data kubwa inayolenga sekta hiyo.

## Angalia maarifa

Je, njia gani inaweza kuwa nzuri ya kuboresha matokeo ya ukamilishaji wa LLM?

1. Uhandisi wa prompt kwa muktadha
1. RAG
1. Mfano uliorekebishwa

J: Zote tatu zinaweza kusaidia. Anza na uhandisi wa prompt na muktadha kwa maboresho ya haraka, na tumia RAG wakati mfano unahitaji ukweli wa sasa au data binafsi ya biashara. Chagua kurekebisha model ikiwa una mifano ya kutosha yenye ubora wa juu na unahitaji mfano ufuate mfululizo wa kazi, muundo, ton, au mtindo wa sekta.

## 🚀 Changamoto

Soma zaidi kuhusu jinsi unavyoweza [kutumia RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) kwa biashara yako.

## Kazi Nzuri, Endelea Kujifunza

Baada ya kumaliza somo hili, tembelea [Mkusanyiko wa Kujifunza AI Inayozalisha](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuongeza maarifa yako juu ya AI Inayozalisha!

Nenda kwenye Sura ya 3 ambapo tutaangalia jinsi ya [kujenga na AI Inayozalisha kwa Uwajibikaji](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->