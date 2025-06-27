<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-06-25T13:15:57+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "sw"
}
-->
# Misingi ya Uhandisi wa Maagizo

## Utangulizi
Moduli hii inashughulikia dhana muhimu na mbinu za kuunda maagizo yenye ufanisi katika mifano ya AI inayozalisha. Jinsi unavyoandika agizo lako kwa LLM pia ni muhimu. Agizo lililotengenezwa kwa uangalifu linaweza kufikia ubora bora wa majibu. Lakini maneno kama _agizo_ na _uhandisi wa maagizo_ yanamaanisha nini hasa? Na ninawezaje kuboresha _ingizo la agizo_ ambalo ninatuma kwa LLM? Haya ni maswali tutakayojaribu kujibu katika sura hii na inayofuata.

AI inayozalisha inaweza kuunda maudhui mapya (mfano, maandishi, picha, sauti, n.k.) kujibu maombi ya watumiaji. Inafanikiwa kufanya hivyo kwa kutumia _Mifano Mikubwa ya Lugha_ kama mfululizo wa GPT wa OpenAI ("Generative Pre-trained Transformer") ambao umefundishwa kutumia lugha ya asili na kanuni.

Watumiaji sasa wanaweza kuingiliana na mifano hii kwa kutumia mitindo ya kawaida kama mazungumzo, bila hitaji la utaalamu wa kiufundi au mafunzo. Mifano hii inategemea _maagizo_ - watumiaji hutuma maandishi ya kuingiza (agizo) na kupata majibu ya AI (ukamilisho). Kisha wanaweza "kuzungumza na AI" kwa kurudia, katika mazungumzo ya zamu nyingi, wakiboresha agizo lao hadi jibu litakapolingana na matarajio yao.

"Maagizo" sasa yanakuwa kiolesura kikuu cha _programu_ kwa programu za AI zinazozalisha, zikieleza mifano nini cha kufanya na kuathiri ubora wa majibu yanayorejeshwa. "Uhandisi wa Maagizo" ni uwanja wa masomo unaokua haraka ambao unalenga katika _kubuni na kuboresha_ maagizo ili kutoa majibu ya ubora na thabiti kwa kiwango kikubwa.

## Malengo ya Kujifunza

Katika somo hili, tunajifunza Uhandisi wa Maagizo ni nini, kwa nini ni muhimu, na jinsi tunavyoweza kuunda maagizo yenye ufanisi zaidi kwa mfano na lengo la maombi lililopewa. Tutaelewa dhana kuu na mbinu bora za uhandisi wa maagizo - na kujifunza kuhusu mazingira ya majaribio ya "sandbox" ya Jupyter Notebooks ambapo tunaweza kuona dhana hizi zikitekelezwa kwa mifano halisi.

Mwisho wa somo hili tutakuwa na uwezo wa:

1. Kueleza uhandisi wa maagizo ni nini na kwa nini ni muhimu.
2. Kufafanua vipengele vya agizo na jinsi vinavyotumika.
3. Kujifunza mbinu bora na mbinu za uhandisi wa maagizo.
4. Kutumia mbinu zilizojifunza kwa mifano halisi, kwa kutumia mwisho wa OpenAI.

## Maneno Muhimu

Uhandisi wa Maagizo: Utaratibu wa kubuni na kuboresha ingizo ili kuongoza mifano ya AI kuelekea kutoa matokeo yaliyohitajika.
Tokenization: Utaratibu wa kubadilisha maandishi kuwa vitengo vidogo, vinavyoitwa tokeni, ambavyo mfano unaweza kuelewa na kushughulikia.
LLMs Zilizotunzwa na Maagizo: Mifano Mikubwa ya Lugha (LLMs) ambazo zimeboreshwa kwa maagizo maalum ili kuboresha usahihi na umuhimu wa majibu yao.

## Mazingira ya Kujifunza

Uhandisi wa maagizo kwa sasa ni zaidi ya sanaa kuliko sayansi. Njia bora ya kuboresha intuisia yetu ni _kufanya mazoezi zaidi_ na kuchukua mbinu ya majaribio na makosa ambayo inachanganya utaalamu wa uwanja wa maombi na mbinu zilizopendekezwa na ubinafsishaji maalum wa mfano.

Jupyter Notebook inayosindikiza somo hili inatoa mazingira ya _sandbox_ ambapo unaweza kujaribu unachojifunza - unapokuwa ukiendelea au kama sehemu ya changamoto ya kanuni mwishoni. Ili kutekeleza mazoezi, utahitaji:

1. **Funguo ya API ya Azure OpenAI** - mwisho wa huduma kwa LLM iliyowekwa.
2. **Muda wa Python** - ambapo Notebook inaweza kutekelezwa.
3. **Mabadiliko ya Mazingira ya Kienyeji** - _kamilisha hatua za [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) sasa ili kujiandaa_.

Notebook inakuja na mazoezi ya _kuanzia_ - lakini unahimizwa kuongeza sehemu zako za _Markdown_ (maelezo) na _Kanuni_ (maombi ya agizo) ili kujaribu mifano zaidi au mawazo - na kujenga intuisia yako kwa kubuni maagizo.

## Mwongozo wa Picha

Unataka kupata picha kubwa ya kile somo hili kinashughulikia kabla ya kuingia ndani? Angalia mwongozo huu wa picha, ambao unakupa hisia ya mada kuu zinazoshughulikiwa na mambo muhimu ya kufikiria katika kila moja. Ramani ya somo inakupeleka kutoka kuelewa dhana kuu na changamoto hadi kuzishughulikia kwa mbinu na mbinu bora za uhandisi wa maagizo. Kumbuka kuwa sehemu ya "Mbinu za Juu" katika mwongozo huu inahusu maudhui yanayoshughulikiwa katika sura _inayofuata_ ya mtaala huu.

## Kuanza kwa Kwanza

Sasa, hebu tuzungumze kuhusu jinsi _mada hii_ inavyohusiana na dhamira yetu ya kuanzisha [kuleta uvumbuzi wa AI katika elimu](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Tunataka kujenga programu zinazotumia AI za _kujifunza kibinafsi_ - kwa hivyo wacha tufikirie jinsi watumiaji tofauti wa programu yetu wanaweza "kubuni" maagizo:

- **Watawala** wanaweza kuuliza AI _kuchambua data ya mtaala ili kubaini mapungufu katika ufunikaji_. AI inaweza kufupisha matokeo au kuyaonyesha kwa kanuni.
- **Walimu** wanaweza kuuliza AI _kuunda mpango wa somo kwa hadhira na mada lengwa_. AI inaweza kujenga mpango wa kibinafsi kwa muundo maalum.
- **Wanafunzi** wanaweza kuuliza AI _kuwafundisha katika somo gumu_. AI sasa inaweza kuwaongoza wanafunzi na masomo, vidokezo na mifano inayolingana na kiwango chao.

Huo ni mwanzo tu wa kile kinachowezekana. Angalia [Maagizo kwa Elimu](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - maktaba ya maagizo ya chanzo wazi yaliyokusanywa na wataalamu wa elimu - kupata hisia pana ya uwezekano! _Jaribu kuendesha baadhi ya maagizo hayo kwenye sandbox au kutumia OpenAI Playground ili kuona kinachotokea!_

## Uhandisi wa Maagizo ni Nini?

Tulianza somo hili kwa kufafanua **Uhandisi wa Maagizo** kama mchakato wa _kubuni na kuboresha_ maandishi ya kuingiza (maagizo) ili kutoa majibu ya ubora na thabiti (ukamilisho) kwa lengo la maombi lililopewa na mfano. Tunaweza kufikiria hii kama mchakato wa hatua mbili:

- _kubuni_ agizo la awali kwa mfano na lengo lililopewa
- _kuboresha_ agizo kwa kurudia ili kuboresha ubora wa jibu

Hii ni lazima iwe mchakato wa majaribio na makosa unaohitaji intuisia ya mtumiaji na juhudi ili kupata matokeo bora. Kwa nini ni muhimu? Ili kujibu swali hilo, kwanza tunahitaji kuelewa dhana tatu:

- _Tokenization_ = jinsi mfano "unaona" agizo
- _Base LLMs_ = jinsi mfano wa msingi "unavyoshughulikia" agizo
- _LLMs Zilizotunzwa na Maagizo_ = jinsi mfano unavyoweza kuona "kazi" sasa

### Tokenization

LLM inaona maagizo kama _mlolongo wa tokeni_ ambapo mifano tofauti (au matoleo ya mfano) inaweza kugawa agizo sawa kwa njia tofauti. Kwa kuwa LLMs zimefundishwa kwenye tokeni (na sio kwenye maandishi asili), jinsi maagizo yanavyogawanywa kwa tokeni ina athari ya moja kwa moja kwenye ubora wa jibu lililotolewa.

Ili kupata intuisia ya jinsi tokenization inavyofanya kazi, jaribu zana kama [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) iliyoonyeshwa hapa chini. Nakili agizo lako - na uone jinsi linavyobadilishwa kuwa tokeni, ukizingatia jinsi herufi za nafasi na alama za uakifishaji zinavyoshughulikiwa. Kumbuka kuwa mfano huu unaonyesha LLM ya zamani (GPT-3) - kwa hivyo kujaribu hii na mfano mpya zaidi kunaweza kutoa matokeo tofauti.

### Dhana: Mifano ya Msingi

Mara agizo linapogawanywa kwa tokeni, kazi kuu ya ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (au mfano wa Msingi) ni kutabiri tokeni katika mlolongo huo. Kwa kuwa LLMs zimefundishwa kwenye seti kubwa za maandishi, zina hisia nzuri ya uhusiano wa kistatistiki kati ya tokeni na zinaweza kufanya utabiri huo kwa ujasiri fulani. Kumbuka kuwa hazielewi _maana_ ya maneno katika agizo au tokeni; zinaona tu muundo ambao zinaweza "kukamilisha" na utabiri wao unaofuata. Zinaweza kuendelea kutabiri mlolongo hadi zimalizike na kuingilia kati kwa mtumiaji au hali fulani iliyowekwa awali.

Unataka kuona jinsi ukamilishaji wa msingi wa agizo unavyofanya kazi? Ingiza agizo hapo juu kwenye [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) ya Azure OpenAI Studio na mipangilio chaguo-msingi. Mfumo umewekwa ili kutibu maagizo kama maombi ya habari - kwa hivyo unapaswa kuona ukamilisho unaoridhisha muktadha huu.

Lakini je, mtumiaji alitaka kuona kitu maalum kinachokidhi vigezo au lengo la kazi? Hapa ndipo _LLMs zilizotunzwa na maagizo_ zinapokuja katika picha.

### Dhana: LLMs Zilizotunzwa na Maagizo

[LLM iliyotunzwa na Maagizo](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) huanza na mfano wa msingi na kuuboreshwa kwa mifano au jozi za ingizo/mahitaji (mfano, "ujumbe" wa zamu nyingi) ambazo zinaweza kuwa na maagizo wazi - na jibu kutoka kwa AI linajaribu kufuata maagizo hayo.

Hii inatumia mbinu kama Kujifunza kwa Kuimarisha na Maoni ya Binadamu (RLHF) ambazo zinaweza kufundisha mfano _kufuata maagizo_ na _kujifunza kutokana na maoni_ ili kwamba inatoa majibu yanayofaa zaidi kwa maombi ya vitendo na yanayohusiana zaidi na malengo ya mtumiaji.

Hebu tujaribu - rejea agizo hapo juu, lakini sasa badilisha _ujumbe wa mfumo_ ili kutoa maagizo yafuatayo kama muktadha:

> _Fupisha maudhui unayopewa kwa mwanafunzi wa darasa la pili. Weka matokeo katika aya moja na pointi 3-5 za risasi._

Ona jinsi matokeo sasa yanavyotunzwa ili kuonyesha lengo na muundo uliotakiwa? Mwalimu sasa anaweza kutumia moja kwa moja jibu hili kwenye slaidi zao kwa darasa hilo.

## Kwa nini tunahitaji Uhandisi wa Maagizo?

Sasa kwa kuwa tunajua jinsi maagizo yanavyoshughulikiwa na LLMs, hebu tuzungumze kuhusu _kwa nini_ tunahitaji uhandisi wa maagizo. Jibu linapatikana katika ukweli kwamba LLMs za sasa zinaweka changamoto kadhaa ambazo zinafanya _ukamilishaji wa kuaminika na thabiti_ kuwa changamoto zaidi kufikia bila kuweka juhudi katika ujenzi na uboreshaji wa maagizo. Kwa mfano:

1. **Majibu ya mfano ni ya kubahatisha.** _Agizo sawa_ litaweza kutoa majibu tofauti na mifano tofauti au matoleo ya mfano. Na linaweza hata kutoa matokeo tofauti na _mfano huo huo_ kwa nyakati tofauti. _Mbinu za uhandisi wa maagizo zinaweza kutusaidia kupunguza tofauti hizi kwa kutoa miongozo bora_.

2. **Mifano inaweza kutengeneza majibu.** Mifano imefundishwa awali na _seti kubwa lakini ndogo_ za data, ikimaanisha hawana ujuzi kuhusu dhana nje ya upeo wa mafunzo hayo. Kama matokeo, zinaweza kutoa ukamilishaji ambao hauko sahihi, wa kufikirika, au unaopingana moja kwa moja na ukweli unaojulikana. _Mbinu za uhandisi wa maagizo husaidia watumiaji kutambua na kupunguza utengenezaji huo kwa mfano, kwa kuomba AI kutoa marejeleo au sababu_.

3. **Uwezo wa mifano utatofautiana.** Mifano mpya au vizazi vya mfano vitakuwa na uwezo zaidi lakini pia huleta quirks na mapungufu ya kipekee katika gharama na ugumu. _Uhandisi wa maagizo unaweza kutusaidia kukuza mbinu bora na mtiririko wa kazi ambao huficha tofauti na kuzoea mahitaji maalum ya mfano kwa njia zinazoweza kupanuliwa na zisizo na mshono_.

Hebu tuone hili likifanyika katika OpenAI au Azure OpenAI Playground:

- Tumia agizo moja na utoaji tofauti wa LLM (mfano, OpenAI, Azure OpenAI, Hugging Face) - je, uliona tofauti?
- Tumia agizo moja mara kwa mara na utoaji _huo huo_ wa LLM (mfano, uwanja wa kucheza wa Azure OpenAI) - tofauti hizi zilikuwa tofauti vipi?

### Mfano wa Utengenezaji

Katika kozi hii, tunatumia neno **"utengenezaji"** kurejelea hali ambapo LLMs wakati mwingine huzalisha taarifa zisizo sahihi kutokana na mapungufu katika mafunzo yao au vikwazo vingine. Unaweza pia kuwa umesikia hii ikirejelewa kama _"maono ya uongo"_ katika makala maarufu au karatasi za utafiti. Hata hivyo, tunapendekeza sana kutumia _"utengenezaji"_ kama neno ili tusijaribu kupeana tabia ya kibinadamu kwa matokeo yanayotokana na mashine. Hii pia inaimarisha miongozo ya [AI inayowajibika](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) kutoka kwa mtazamo wa istilahi, kuondoa maneno ambayo yanaweza pia kuzingatiwa kuwa ya kukera au yasiyo ya kujumuisha katika baadhi ya muktadha.

Unataka kupata hisia ya jinsi utengenezaji unavyofanya kazi? Fikiria agizo linaloelekeza AI kuunda maudhui kwa mada isiyokuwepo (ili kuhakikisha haipatikani katika seti ya mafunzo). Kwa mfano - nilijaribu agizo hili:

> **Agizo:** tengeneza mpango wa somo juu ya Vita vya Mars vya 2076.

Utafutaji wa mtandao ulionyesha kuwa kulikuwa na akaunti za kubuni (mfano, mfululizo wa televisheni au vitabu) juu ya vita vya Mars - lakini hakuna katika 2076. Hisia ya kawaida pia inatuambia kuwa 2076 ni _katika siku zijazo_ na hivyo, haiwezi kuhusishwa na tukio halisi.

Kwa hivyo ni nini kinachotokea tunapokimbia agizo hili na watoa huduma tofauti wa LLM?

> **Jibu 1**: OpenAI Playground (GPT-35)

> **Jibu 2**: Azure OpenAI Playground (GPT-35)

> **Jibu 3**: : Hugging Face Chat Playground (LLama-2)

Kama ilivyotarajiwa, kila mfano (au toleo la mfano) hutoa majibu tofauti kidogo kutokana na tabia ya kubahatisha na tofauti za uwezo wa mfano. Kwa mfano, mfano mmoja unalenga hadhira ya darasa la 8 wakati mwingine unadhani mwanafunzi wa shule ya sekondari. Lakini mifano yote mitatu ilizalisha majibu ambayo yanaweza kumshawishi mtumiaji asiye na taarifa kwamba tukio hilo lilikuwa halisi.

Mbinu za uhandisi wa maagizo kama _metaprompting_ na _usimamizi wa joto_ zinaweza kupunguza utengenezaji wa mfano kwa kiwango fulani. _Miundo_ mipya ya uhandisi wa maagizo pia inajumuisha zana na mbinu mpya kwa urahisi katika mtiririko wa maagizo, ili kupunguza au kupunguza baadhi ya athari hizi.

## Utafiti wa Kesi: GitHub Copilot

Hebu tumalize sehemu hii kwa kupata hisia ya jinsi uhandisi wa maagizo unavyotumika katika suluhisho za ulimwengu halisi kwa kuangalia Utafiti mmoja wa Kesi: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

Git
Mwishowe, thamani halisi ya templeti inapatikana katika uwezo wa kuunda na kuchapisha _maktaba za msukumo_ kwa maeneo ya matumizi wima - ambapo templeti ya msukumo sasa inaboreshwa kuonyesha muktadha maalum wa programu au mifano inayofanya majibu kuwa muhimu zaidi na sahihi kwa hadhira inayolengwa. Rejesta ya [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) ni mfano mzuri wa mbinu hii, ikikusanya maktaba ya misukumo kwa ajili ya elimu yenye mkazo kwenye malengo muhimu kama kupanga masomo, kubuni mtaala, kufundisha wanafunzi n.k.

## Maudhui ya Kusaidia

Tukifikiria kuhusu ujenzi wa msukumo kama kuwa na maagizo (kazi) na lengo (maudhui ya msingi), basi _maudhui ya sekondari_ ni kama muktadha wa ziada tunaotoa ili **kuathiri matokeo kwa namna fulani**. Inaweza kuwa kurekebisha vigezo, maagizo ya muundo, taksonomia za mada n.k. ambazo zinaweza kusaidia mfano _kubinafsisha_ majibu yake kufaa malengo au matarajio ya mtumiaji yaliyokusudiwa.

Kwa mfano: Ukiwa na katalogi ya kozi yenye metadata nyingi (jina, maelezo, kiwango, vitambulisho vya metadata, mwalimu n.k.) kwenye kozi zote zinazopatikana katika mtaala:

- tunaweza kufafanua maagizo ya "kufupisha katalogi ya kozi kwa Msimu wa Kuanguka 2023"
- tunaweza kutumia maudhui ya msingi kutoa mifano michache ya matokeo yanayotakiwa
- tunaweza kutumia maudhui ya sekondari kutambua vitambulisho 5 vya juu vya maslahi.

Sasa, mfano unaweza kutoa muhtasari kwa muundo ulioonyeshwa na mifano michache - lakini ikiwa matokeo yana vitambulisho vingi, inaweza kipaumbele vitambulisho 5 vilivyotambuliwa kwenye maudhui ya sekondari.

---

<!--
MFANO WA SOMO:
Kitengo hiki kinapaswa kufunika dhana ya msingi #1.
Imarisha dhana hiyo kwa mifano na marejeleo.

DHANA #3:
Mbinu za Uhandisi wa Msukumo.
Je, ni mbinu gani za msingi za uhandisi wa msukumo?
Onyesha kwa mazoezi fulani.
-->

## Mazoea Bora ya Msukumo

Sasa kwa kuwa tunajua jinsi misukumo inaweza kujengwa, tunaweza kuanza kufikiria jinsi ya kuibuni ili kuonyesha mazoea bora. Tunaweza kufikiria hili katika sehemu mbili - kuwa na _mtazamo_ sahihi na kutumia _mbinu_ sahihi.

### Mtazamo wa Uhandisi wa Msukumo

Uhandisi wa Msukumo ni mchakato wa majaribio na makosa kwa hivyo kumbuka mambo matatu makubwa ya kuongoza:

1. **Uelewa wa Maeneo ni Muhimu.** Usahihi na umuhimu wa majibu ni kazi ya _eneo_ ambalo programu au mtumiaji anafanya kazi. Tumia intuisheni yako na utaalamu wa eneo lako ili **kubinafsisha mbinu** zaidi. Kwa mfano, fafanua _tabia maalum za eneo_ katika misukumo ya mfumo wako, au tumia _templeti maalum za eneo_ katika misukumo ya mtumiaji wako. Toa maudhui ya sekondari yanayoonyesha muktadha maalum wa eneo, au tumia _vidokezo na mifano maalum ya eneo_ kuongoza mfano kuelekea mifumo ya matumizi inayofahamika.

2. **Uelewa wa Mfano ni Muhimu.** Tunajua mifano ni ya kubahatisha kiasili. Lakini utekelezaji wa mifano unaweza pia kutofautiana kwa mujibu wa seti ya mafunzo wanayotumia (maarifa yaliyofunzwa awali), uwezo wanaotoa (kwa mfano, kupitia API au SDK) na aina ya maudhui wanayoboreshwa kwa ajili yake (kwa mfano, msimbo dhidi ya picha dhidi ya maandishi). Elewa nguvu na mapungufu ya mfano unaotumia, na tumia maarifa hayo _kipaumbele kazi_ au kujenga _templeti zilizobinafsishwa_ ambazo zimeboreshwa kwa ajili ya uwezo wa mfano.

3. **Kurudia & Uthibitishaji ni Muhimu.** Mifano inabadilika haraka, na hivyo ndivyo mbinu za uhandisi wa msukumo. Kama mtaalamu wa eneo, unaweza kuwa na muktadha mwingine au vigezo _programu yako_ maalum, ambavyo vinaweza visitumike kwa jamii pana. Tumia zana za uhandisi wa msukumo na mbinu za "kuanzisha" ujenzi wa msukumo, kisha rudia na thibitisha matokeo kwa kutumia intuisheni yako na utaalamu wa eneo lako. Rekodi maarifa yako na unda **msingi wa maarifa** (kwa mfano, maktaba za msukumo) ambazo zinaweza kutumika kama msingi mpya na wengine, kwa marudio ya haraka katika siku zijazo.

## Mazoea Bora

Sasa tuangalie mazoea bora ya kawaida yanayopendekezwa na [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) na wataalamu wa [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Nini                                | Kwa nini                                                                                                                                                                                                                                              |
| :---------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tathmini mifano mipya zaidi.       | Vizazi vipya vya mifano vina uwezekano wa kuwa na vipengele na ubora ulioboreshwa - lakini pia vinaweza kuwa na gharama kubwa zaidi. Tathmini athari zake, kisha fanya maamuzi ya uhamisho.                                                           |
| Tenganisha maagizo na muktadha     | Angalia ikiwa mfano wako/mtoa huduma anafafanua _vitengele_ ili kutofautisha maagizo, maudhui ya msingi na ya sekondari kwa uwazi zaidi. Hii inaweza kusaidia mifano kugawa uzito kwa usahihi zaidi kwa tokeni.                                        |
| Kuwa maalum na wazi                | Toa maelezo zaidi kuhusu muktadha unaotakiwa, matokeo, urefu, muundo, mtindo n.k. Hii itaboresha ubora na uthabiti wa majibu. Kamatia mapishi katika templeti zinazoweza kutumika tena.                                                               |
| Kuwa na maelezo, tumia mifano      | Mifano inaweza kujibu vizuri zaidi kwa mbinu ya "onyesha na eleza". Anza na `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
| Use cues to jumpstart completions | Nudge it towards a desired outcome by giving it some leading words or phrases that it can use as a starting point for the response.                                                                                                               |
| Double Down                       | Sometimes you may need to repeat yourself to the model. Give instructions before and after your primary content, use an instruction and a cue, etc. Iterate & validate to see what works.                                                         |
| Order Matters                     | The order in which you present information to the model may impact the output, even in the learning examples, thanks to recency bias. Try different options to see what works best.                                                               |
| Give the model an “out”           | Give the model a _fallback_ completion response it can provide if it cannot complete the task for any reason. This can reduce chances of models generating false or fabricated responses.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

As with any best practice, remember that _your mileage may vary_ based on the model, the task and the domain. Use these as a starting point, and iterate to find what works best for you. Constantly re-evaluate your prompt engineering process as new models and tools become available, with a focus on process scalability and response quality.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Assignment

Congratulations! You made it to the end of the lesson! It's time to put some of those concepts and techniques to the test with real examples!

For our assignment, we'll be using a Jupyter Notebook with exercises you can complete interactively. You can also extend the Notebook with your own Markdown and Code cells to explore ideas and techniques on your own.

### To get started, fork the repo, then

- (Recommended) Launch GitHub Codespaces
- (Alternatively) Clone the repo to your local device and use it with Docker Desktop
- (Alternatively) Open the Notebook with your preferred Notebook runtime environment.

### Next, configure your environment variables

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` values. Rejelea [sehemu ya Kujifunza Sandbox](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) ili kujifunza jinsi.

### Kisha, fungua Jupyter Notebook

- Chagua kernel ya wakati wa kukimbia. Ikiwa unatumia chaguo 1 au 2, chagua tu kernel ya Python 3.10.x ya msingi inayotolewa na kontena la maendeleo.

Uko tayari kuendesha mazoezi. Kumbuka kuwa hakuna majibu sahihi na mabaya hapa - ni kuchunguza chaguo kwa majaribio na makosa na kujenga intuisheni kwa kile kinachofanya kazi kwa mfano fulani na eneo la programu.

_Kwa sababu hii hakuna sehemu za Suluhisho la Msimbo katika somo hili. Badala yake, Notebook itakuwa na seli za Markdown zilizoandikwa "Suluhisho Langu:" zinazoonyesha mfano mmoja wa matokeo kwa marejeleo._

 <!--
MFANO WA SOMO:
Funga sehemu hiyo na muhtasari na rasilimali za kujifunza binafsi.
-->

## Ukaguzi wa Maarifa

Ni ipi kati ya zifuatazo ni msukumo mzuri kufuata baadhi ya mazoea bora yanayofaa?

1. Nionyeshe picha ya gari jekundu
2. Nionyeshe picha ya gari jekundu la aina Volvo na mfano XC90 lililopaki kando ya mwamba huku jua likizama
3. Nionyeshe picha ya gari jekundu la aina Volvo na mfano XC90

J: 2, ni msukumo bora zaidi kwani inatoa maelezo kuhusu "nini" na inaenda kwenye maalum (si gari lolote bali aina maalum na mfano) na pia inaelezea mazingira ya jumla. 3 ni bora zaidi kwani pia ina maelezo mengi.

## 🚀 Changamoto

Angalia ikiwa unaweza kutumia mbinu ya "kijisehemu" na msukumo: Kamilisha sentensi "Nionyeshe picha ya gari jekundu la aina Volvo na ". Inajibu nini, na ungeboreshaje?

## Kazi Nzuri! Endelea Kujifunza

Unataka kujifunza zaidi kuhusu dhana tofauti za Uhandisi wa Msukumo? Nenda kwenye [ukurasa wa kuendelea kujifunza](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kupata rasilimali nyingine nzuri juu ya mada hii.

Nenda kwenye Somo la 5 ambapo tutaangalia [mbinu za hali ya juu za msukumo](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuelewana. Hati asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo chenye mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa maelewano mabaya au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.