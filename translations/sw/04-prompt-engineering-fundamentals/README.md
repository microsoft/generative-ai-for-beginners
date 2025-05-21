<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-05-19T16:07:12+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "sw"
}
-->
# Misingi ya Uhandisi wa Maagizo

## Utangulizi
Moduli hii inashughulikia dhana muhimu na mbinu za kuunda maagizo bora katika mifano ya AI inayozalisha. Jinsi unavyoandika agizo lako kwa LLM pia ni muhimu. Agizo lililotengenezwa kwa uangalifu linaweza kufanikisha majibu bora. Lakini maneno kama _agizo_ na _uhandisi wa maagizo_ yanamaanisha nini hasa? Na ninawezaje kuboresha _ingizo la agizo_ ambalo ninatuma kwa LLM? Haya ndiyo maswali tutakayojaribu kujibu katika sura hii na inayofuata.

_Generative AI_ inaweza kuunda maudhui mapya (mfano, maandishi, picha, sauti, msimbo n.k.) kwa kukabiliana na maombi ya watumiaji. Hii inafanikishwa kwa kutumia _Mifano Mikubwa ya Lugha_ kama mfululizo wa GPT wa OpenAI ("Generative Pre-trained Transformer") ambayo imefundishwa kwa kutumia lugha ya asili na msimbo.

Watumiaji sasa wanaweza kuingiliana na mifano hii kwa kutumia mifumo ya kawaida kama mazungumzo, bila kuhitaji utaalamu wa kiufundi au mafunzo. Mifano ni _inayotegemea maagizo_ - watumiaji hutuma ingizo la maandishi (agizo) na kupata jibu la AI (kukamilika). Kisha wanaweza "kuzungumza na AI" kwa njia ya kurudia, katika mazungumzo ya mzunguko mingi, wakiboresha agizo lao hadi jibu litakapolingana na matarajio yao.

"Maagizo" sasa yanakuwa kiolesura cha msingi cha _programu_ kwa programu za AI zinazozalisha, zikieleza mifano inachotakiwa kufanya na kuathiri ubora wa majibu yanayorejeshwa. "Uhandisi wa Maagizo" ni uwanja unaokua kwa kasi wa masomo unaozingatia _usanifu na uboreshaji_ wa maagizo ili kutoa majibu thabiti na bora kwa kiwango.

## Malengo ya Kujifunza

Katika somo hili, tunajifunza nini Uhandisi wa Maagizo ni, kwa nini ni muhimu, na jinsi tunavyoweza kuunda maagizo bora zaidi kwa mfano na lengo la programu lililotolewa. Tutaelewa dhana kuu na mbinu bora za uhandisi wa maagizo - na kujifunza kuhusu mazingira ya "sandbox" ya Jupyter Notebooks ambapo tunaweza kuona dhana hizi zikitekelezwa kwa mifano halisi.

Mwisho wa somo hili tutaweza:

1. Eleza nini uhandisi wa maagizo ni na kwa nini ni muhimu.
2. Eleza vipengele vya agizo na jinsi vinavyotumika.
3. Jifunze mbinu bora na mbinu za uhandisi wa maagizo.
4. Tumia mbinu zilizojifunza kwa mifano halisi, kwa kutumia mwisho wa OpenAI.

## Maneno Muhimu

Uhandisi wa Maagizo: Mazoezi ya kubuni na kuboresha ingizo ili kuelekeza mifano ya AI kuelekea kutoa matokeo yanayotakiwa.
Tokenization: Mchakato wa kubadilisha maandishi kuwa vitengo vidogo, vinavyoitwa tokeni, ambavyo mfano unaweza kuelewa na kuchakata.
LLM Zilizotunzwa kwa Maagizo: Mifano Mikubwa ya Lugha (LLMs) ambazo zimefanyiwa marekebisho maalum na maagizo ili kuboresha usahihi wa majibu yao na umuhimu.

## Mazingira ya Kujifunza

Uhandisi wa maagizo kwa sasa ni zaidi ya sanaa kuliko sayansi. Njia bora ya kuboresha hisia zetu juu yake ni _kufanya mazoezi zaidi_ na kutumia mbinu ya jaribio-na-kosa inayochanganya utaalamu wa uwanja wa maombi na mbinu zinazopendekezwa na uboreshaji maalum wa mifano.

Notebook ya Jupyter inayosindikiza somo hili inatoa mazingira ya _sandbox_ ambapo unaweza kujaribu unachojifunza - unapoendelea au kama sehemu ya changamoto ya msimbo mwishoni. Ili kutekeleza mazoezi, utahitaji:

1. **Ufunguo wa Azure OpenAI API** - huduma ya mwisho kwa LLM iliyotumika.
2. **Muda wa Python** - ambapo Notebook inaweza kutekelezwa.
3. **Mabadiliko ya Mazingira ya Ndani** - _kamilisha hatua za [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) sasa ili uwe tayari_.

Notebook inakuja na mazoezi ya _kuanzia_ - lakini unahimizwa kuongeza sehemu zako za _Markdown_ (maelezo) na _Msimbo_ (maombi ya maagizo) kujaribu mifano zaidi au mawazo - na kujenga hisia zako za kubuni maagizo.

## Mwongozo Ulioonyeshwa

Unataka kupata picha kubwa ya kile somo hili linashughulikia kabla ya kuzama ndani? Angalia mwongozo huu ulioonyeshwa, ambao unakupa hisia ya mada kuu zinazoshughulikiwa na mambo muhimu ya kuzingatia kwa kila moja. Ramani ya somo inakupeleka kutoka kuelewa dhana kuu na changamoto hadi kuzishughulikia na mbinu za uhandisi wa maagizo zinazofaa na mbinu bora. Kumbuka kwamba sehemu ya "Mbinu za Juu" katika mwongozo huu inahusu maudhui yaliyoshughulikiwa katika sura _inayofuata_ ya mtaala huu.

## Uanzishaji Wetu

Sasa, hebu tuzungumze juu ya jinsi _mada hii_ inavyohusiana na dhamira yetu ya kuanzisha [kuleta ubunifu wa AI katika elimu](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Tunataka kujenga programu za kujifunza zinazotumia AI za _ujifunzaji wa kibinafsi_ - hivyo hebu tufikirie jinsi watumiaji tofauti wa programu yetu wanaweza "kubuni" maagizo:

- **Watawala** wanaweza kuuliza AI _kuchambua data ya mtaala ili kubaini mapungufu katika usambazaji_. AI inaweza kufupisha matokeo au kuyaonyesha kwa msimbo.
- **Waelimishaji** wanaweza kuuliza AI _kuunda mpango wa somo kwa hadhira na mada inayolengwa_. AI inaweza kujenga mpango wa kibinafsi katika muundo uliotajwa.
- **Wanafunzi** wanaweza kuuliza AI _kuwafundisha katika somo gumu_. AI sasa inaweza kuwaongoza wanafunzi na masomo, vidokezo na mifano iliyobinafsishwa kwa kiwango chao.

Hiyo ni sehemu tu ya kile kinachowezekana. Angalia [Maagizo kwa Elimu](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - maktaba ya maagizo ya chanzo wazi iliyokusanywa na wataalamu wa elimu - ili kupata hisia pana ya uwezekano! _Jaribu kuendesha baadhi ya maagizo hayo kwenye sandbox au kwa kutumia OpenAI Playground ili kuona kinachotokea!_

## Uhandisi wa Maagizo ni Nini?

Tulianza somo hili kwa kufafanua **Uhandisi wa Maagizo** kama mchakato wa _kubuni na kuboresha_ ingizo la maandishi (maagizo) ili kutoa majibu thabiti na bora (kukamilika) kwa lengo la programu lililotolewa na mfano. Tunaweza kufikiria hili kama mchakato wa hatua mbili:

- _kubuni_ agizo la awali kwa mfano na lengo lililotolewa
- _kuboresha_ agizo kwa kurudia ili kuboresha ubora wa jibu

Huu ni mchakato wa lazima wa jaribio-na-kosa unaohitaji hisia na jitihada za mtumiaji ili kupata matokeo bora. Kwa nini ni muhimu? Ili kujibu swali hilo, kwanza tunahitaji kuelewa dhana tatu:

- _Tokenization_ = jinsi mfano "unaona" agizo
- _Base LLMs_ = jinsi mfano wa msingi "unachakata" agizo
- _Instruction-Tuned LLMs_ = jinsi mfano unaweza sasa kuona "kazi"

### Tokenization

LLM inaona maagizo kama _mfuatano wa tokeni_ ambapo mifano tofauti (au matoleo ya mfano) inaweza kutengeneza tokeni kwa agizo moja kwa njia tofauti. Kwa kuwa LLMs zimefundishwa kwa tokeni (na si kwa maandishi mabichi), jinsi maagizo yanavyotengeneza tokeni ina athari ya moja kwa moja kwenye ubora wa jibu linalozalishwa.

Ili kupata hisia ya jinsi tokenization inavyofanya kazi, jaribu zana kama [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) inayoonyeshwa hapa chini. Nakili agizo lako - na uone jinsi hilo linavyobadilishwa kuwa tokeni, ukizingatia jinsi herufi za nafasi na alama za uakifishaji zinavyoshughulikiwa. Kumbuka kuwa mfano huu unaonyesha LLM ya zamani (GPT-3) - hivyo kujaribu hii na mfano mpya inaweza kutoa matokeo tofauti.

### Dhana: Mifano ya Msingi

Mara tu agizo linapokuwa na tokeni, kazi ya msingi ya ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (au Mfano wa Msingi) ni kutabiri tokeni katika mfuatano huo. Kwa kuwa LLMs zimefundishwa kwa seti kubwa za data za maandishi, zina uelewa mzuri wa uhusiano wa takwimu kati ya tokeni na zinaweza kufanya utabiri huo kwa ujasiri fulani. Kumbuka kwamba hazielewi _maana_ ya maneno katika agizo au tokeni; zinaona tu muundo ambao zinaweza "kukamilisha" na utabiri wao unaofuata. Zinaweza kuendelea kutabiri mfuatano hadi kusimamishwa na uingiliaji wa mtumiaji au hali fulani iliyowekwa awali.

Unataka kuona jinsi kukamilika kwa agizo kunavyofanya kazi? Ingiza agizo hapo juu kwenye [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) ya Azure OpenAI Studio na mipangilio ya kawaida. Mfumo umewekwa kutibu maagizo kama maombi ya habari - hivyo unapaswa kuona kukamilika kunakotosheleza muktadha huu.

Lakini vipi ikiwa mtumiaji alitaka kuona kitu maalum ambacho kinakidhi baadhi ya vigezo au lengo la kazi? Hapa ndipo LLMs zilizotunzwa kwa maagizo zinapoingia kwenye picha.

### Dhana: LLMs Zilizotunzwa kwa Maagizo

LLM [zilizotunzwa kwa maagizo](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) zinaanza na mfano wa msingi na kuufanyia marekebisho kwa mifano au jozi za ingizo/utoaji (mfano, "ujumbe" wa mzunguko mwingi) ambazo zinaweza kuwa na maagizo wazi - na jibu kutoka kwa AI linajaribu kufuata agizo hilo.

Hii inatumia mbinu kama Kujifunza Kuimarisha na Maoni ya Binadamu (RLHF) ambazo zinaweza kufundisha mfano kufuata maagizo na kujifunza kutoka kwa maoni ili kutoa majibu ambayo yanafaa zaidi kwa matumizi ya vitendo na muhimu zaidi kwa malengo ya mtumiaji.

Hebu tujaribu - rejelea agizo hapo juu, lakini sasa badilisha _ujumbe wa mfumo_ kutoa maagizo yafuatayo kama muktadha:

> _Fupisha maudhui unayopewa kwa mwanafunzi wa darasa la pili. Weka matokeo katika aya moja na pointi 3-5 za risasi._

Ona jinsi matokeo sasa yanavyotunzwa ili kuonyesha lengo na muundo unaotakiwa? Mwalimu sasa anaweza kutumia jibu hili moja kwa moja katika slaidi zao kwa darasa hilo.

## Kwa nini tunahitaji Uhandisi wa Maagizo?

Sasa kwa kuwa tunajua jinsi maagizo yanavyosindikwa na LLMs, hebu tuzungumze kuhusu _kwa nini_ tunahitaji uhandisi wa maagizo. Jibu liko katika ukweli kwamba LLMs za sasa zinakabiliwa na changamoto kadhaa ambazo zinafanya _kukamilika kwa kuaminika na thabiti_ kuwa ngumu zaidi kufanikisha bila kuweka juhudi katika ujenzi na uboreshaji wa maagizo. Kwa mfano:

1. **Majibu ya mfano ni ya nasibu.** _Agizo lilelile_ linaweza kutoa majibu tofauti na mifano tofauti au matoleo ya mfano. Na linaweza hata kutoa matokeo tofauti na _mfano uleule_ kwa nyakati tofauti. _Mbinu za uhandisi wa maagizo zinaweza kutusaidia kupunguza tofauti hizi kwa kutoa ulinzi bora_.

1. **Mifano inaweza kutunga majibu.** Mifano imefundishwa na _seti kubwa lakini finyu_ za data, ikimaanisha hazina ujuzi kuhusu dhana nje ya upeo wa mafunzo hayo. Kama matokeo, zinaweza kutoa kukamilika ambayo si sahihi, ya kufikirika, au inakinzana moja kwa moja na ukweli unaojulikana. _Mbinu za uhandisi wa maagizo zinasaidia watumiaji kutambua na kupunguza utungaji huo mf. kwa kuomba AI kwa marejeleo au mantiki_.

1. **Uwezo wa mifano utatofautiana.** Mifano mpya au vizazi vya mfano vitakuwa na uwezo zaidi lakini pia huleta kasoro za kipekee na biashara za gharama na ugumu. _Uhandisi wa maagizo unaweza kutusaidia kukuza mbinu bora na mikondo ya kazi ambayo inajumuisha tofauti na kuzoea mahitaji maalum ya mfano kwa njia zinazoweza kupimika, na bila mshono_.

Hebu tuone hili likifanya kazi katika OpenAI au Azure OpenAI Playground:

- Tumia agizo lilelile na matoleo tofauti ya LLM (mfano, OpenAI, Azure OpenAI, Hugging Face) - uliona tofauti?
- Tumia agizo lilelile mara kwa mara na _toleo lilelile_ la LLM (mfano, uwanja wa kucheza wa Azure OpenAI) - jinsi tofauti hizi zilivyotofautiana?

### Mfano wa Utungaji

Katika kozi hii, tunatumia neno **"utungaji"** kurejelea hali ambapo LLMs wakati mwingine huzalisha habari zisizo sahihi kutokana na mapungufu katika mafunzo yao au vizuizi vingine. Unaweza pia kuwa umesikia hii ikirejelewa kama _"maono"_ katika makala maarufu au karatasi za utafiti. Hata hivyo, tunapendekeza sana kutumia _"utungaji"_ kama neno ili tusije tukahusisha tabia ya kibinadamu na matokeo yanayosababishwa na mashine. Hii pia inaimarisha [miongozo ya AI inayowajibika](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) kutoka kwa mtazamo wa istilahi, kuondoa maneno ambayo yanaweza pia kuchukuliwa kuwa ya kukera au yasiyojumuisha katika baadhi ya muktadha.

Unataka kupata hisia ya jinsi utungaji unavyofanya kazi? Fikiria agizo linaloelekeza AI kuunda maudhui kwa mada isiyokuwepo (ili kuhakikisha haipatikani katika seti ya data ya mafunzo). Kwa mfano - nilijaribu agizo hili:

> **Agizo:** tengeneza mpango wa somo kuhusu Vita vya Mirihi vya 2076.

Utafutaji wa wavuti ulionyesha kuwa kulikuwa na akaunti za kubuni (mfano, mfululizo wa televisheni au vitabu) juu ya vita vya Mirihi - lakini hakuna katika 2076. Akili ya kawaida pia inatuambia kwamba 2076 ni _katika siku zijazo_ na hivyo, haiwezi kuhusishwa na tukio halisi.

Kwa hivyo ni nini kinachotokea tunapotekeleza agizo hili na watoa huduma tofauti wa LLM?

Kama ilivyotarajiwa, kila mfano (au toleo la mfano) hutoa majibu tofauti kidogo kutokana na tabia ya nasibu na tofauti za uwezo wa mfano. Kwa mfano, mfano mmoja unalenga hadhira ya darasa la 8 huku mwingine ukichukulia mwanafunzi wa shule ya upili. Lakini mifano yote mitatu ilizalisha majibu ambayo yanaweza kumshawishi mtumiaji asiye na habari kwamba tukio hilo lilikuwa la kweli.

Mbinu za uhandisi wa maagizo kama _metaprompting_ na _usanidi wa joto_ zinaweza kupunguza utungaji wa mfano kwa kiasi fulani. Miundo mpya ya uhandisi wa maagizo pia inajumuisha zana na mbinu mpya kwa njia isiyo na mshono katika mtiririko wa maagizo, ili kupunguza au kupunguza baadhi ya athari hizi.

## Uchunguzi wa Kesi: GitHub Copilot

Hebu tuhitimishe sehemu hii kwa kupata hisia ya jinsi uhandisi wa maagizo unavyotumika katika suluhisho za ulimwengu wa kweli kwa kuangalia Uchunguzi mmoja wa Kesi: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot ni "Mwandishi wa Programu wa AI" wako - inabadilisha maagizo ya maandishi kuwa kukamilika kwa msimbo na imeunganishwa katika mazingira yako ya maendeleo (mfano, Visual Studio Code) kwa uzoefu wa mtumiaji bila mshono. Kama ilivyorekodiwa katika mfululizo wa blogi hapa chini, toleo la awali lilitegemea mfano
Hatimaye, thamani halisi ya templeti ni uwezo wa kuunda na kuchapisha _maktaba za maelekezo_ kwa ajili ya matumizi ya wima - ambapo templeti ya maelekezo sasa imeboreshwa ili kuakisi muktadha maalum wa matumizi au mifano inayofanya majibu kuwa muhimu zaidi na sahihi kwa hadhira inayolengwa. Repositori ya [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) ni mfano mzuri wa mbinu hii, ikikusanya maktaba ya maelekezo kwa uwanja wa elimu kwa mkazo kwenye malengo muhimu kama upangaji wa masomo, muundo wa mtaala, ushauri wa wanafunzi n.k.

## Maudhui ya Msaada

Ikiwa tunafikiria kuhusu uundaji wa maelekezo kama kuwa na maagizo (kazi) na lengo (maudhui ya msingi), basi _maudhui ya sekondari_ ni kama muktadha wa ziada tunaotoa ili **kuathiri matokeo kwa namna fulani**. Inaweza kuwa vigezo vya kurekebisha, maagizo ya muundo, taksonomia za mada n.k. zinazoweza kusaidia modeli _kuboresha_ majibu yake ili yafae malengo au matarajio ya mtumiaji.

Kwa mfano: Ukiwa na katalogi ya kozi yenye metadata nyingi (jina, maelezo, kiwango, lebo za metadata, mwalimu n.k.) kwenye kozi zote zinazopatikana katika mtaala:

- tunaweza kufafanua agizo la "kujumlisha katalogi ya kozi kwa Msimu wa Kuanguka 2023"
- tunaweza kutumia maudhui ya msingi kutoa mifano michache ya matokeo yanayotakiwa
- tunaweza kutumia maudhui ya sekondari kutambua lebo 5 za juu za maslahi.

Sasa, modeli inaweza kutoa muhtasari kwa muundo unaoonyeshwa na mifano michache - lakini ikiwa matokeo yana lebo nyingi, inaweza kupa kipaumbele lebo 5 zilizotambuliwa katika maudhui ya sekondari.

---

<!--
TEMPLATE YA SOMO:
Kipengele hiki kinapaswa kufunika dhana ya msingi #1.
Imarisha dhana kwa mifano na marejeleo.

DHANA #3:
Mbinu za Uhandisi wa Maelekezo.
Ni mbinu zipi za msingi za uhandisi wa maelekezo?
Onyesha kwa mazoezi.
-->

## Mazoezi Bora ya Utoaji Maelekezo

Sasa tunajua jinsi maelekezo yanavyoweza _kuundwa_, tunaweza kuanza kufikiria jinsi ya _kuyaunda_ ili kuakisi mazoea bora. Tunaweza kufikiria kuhusu hili kwa sehemu mbili - kuwa na _mtazamo_ sahihi na kutumia _mbinu_ sahihi.

### Mtazamo wa Uhandisi wa Maelekezo

Uhandisi wa Maelekezo ni mchakato wa majaribio na makosa hivyo zingatia mambo matatu ya jumla:

1. **Uelewa wa Uwanja Unaleta Mabadiliko.** Usahihi wa majibu na umuhimu ni kazi ya _uwanja_ ambao matumizi au mtumiaji anafanya kazi. Tumia intuisheni yako na utaalamu wa uwanja ili **kurekebisha mbinu** zaidi. Kwa mfano, fafanua _tabia maalum za uwanja_ katika maelekezo ya mfumo wako, au tumia _templeti maalum za uwanja_ katika maelekezo ya mtumiaji wako. Toa maudhui ya sekondari yanayoakisi muktadha maalum wa uwanja, au tumia _vidokezo na mifano maalum ya uwanja_ kuongoza modeli kuelekea mifumo ya matumizi inayofahamika.

2. **Uelewa wa Modeli Unaleta Mabadiliko.** Tunajua modeli ni za kiukusanyaji kwa asili. Lakini utekelezaji wa modeli unaweza pia kutofautiana kwa suala la seti ya data ya mafunzo wanayotumia (maarifa ya awali), uwezo wanaotoa (mfano, kupitia API au SDK) na aina ya maudhui ambayo yameboreshwa kwa ajili yake (mfano, kodi vs. picha vs. maandishi). Elewa nguvu na mapungufu ya modeli unayotumia, na tumia maarifa hayo _kupa kipaumbele kazi_ au kujenga _templeti maalum_ ambazo zimeboreshwa kwa uwezo wa modeli.

3. **Ukariri na Uthibitishaji Unaleta Mabadiliko.** Modeli zinabadilika haraka, na hivyo ndivyo mbinu za uhandisi wa maelekezo. Kama mtaalamu wa uwanja, unaweza kuwa na muktadha mwingine au vigezo vya _matumizi yako_ maalum, ambavyo huenda havitumiki kwa jamii pana. Tumia zana na mbinu za uhandisi wa maelekezo "kuanzisha" uundaji wa maelekezo, kisha rudia na uthibitishe matokeo kwa kutumia intuisheni yako na utaalamu wa uwanja. Rekodi maarifa yako na unda **msingi wa maarifa** (mfano, maktaba ya maelekezo) ambayo yanaweza kutumika kama msingi mpya na wengine, kwa ukariri wa haraka zaidi katika siku zijazo.

## Mazoezi Bora

Sasa tuangalie mazoea bora yanayopendekezwa na [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) na watendaji wa [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Nini                              | Kwa nini                                                                                                                                                                                                                                               |
| :-------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tathmini modeli za hivi karibuni. | Vizazi vipya vya modeli vina uwezekano wa kuwa na vipengele na ubora ulioboreshwa - lakini vinaweza pia kuhusisha gharama za juu. Tathmini athari zake, kisha fanya maamuzi ya uhamaji.                                                                  |
| Tenganisha maagizo na muktadha    | Angalia ikiwa modeli/mtu anayetoa huduma yako anafafanua _vifupisho_ ili kutofautisha maagizo, maudhui ya msingi na ya sekondari kwa uwazi zaidi. Hii inaweza kusaidia modeli kutoa uzito kwa usahihi zaidi kwa tokeni.                                  |
| Kuwa maalum na wazi               | Toa maelezo zaidi kuhusu muktadha unaotakiwa, matokeo, urefu, muundo, mtindo n.k. Hii itaboresha ubora na uthabiti wa majibu. Kamatia mapishi katika templeti zinazoweza kutumika tena.                                                                 |
| Kuwa na maelezo, tumia mifano     | Modeli zinaweza kujibu vyema zaidi kwa mbinu ya "onyesha na sema". Anza na `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
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

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` values. Rudi kwenye [Sehemu ya Sandbox ya Kujifunza](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) kujifunza jinsi.

### Kisha, fungua Jupyter Notebook

- Chagua kernel ya runtime. Ikiwa unatumia chaguo 1 au 2, chagua tu kernel ya Python 3.10.x iliyotolewa na kontena la maendeleo.

Uko tayari kuendesha mazoezi. Kumbuka kwamba hakuna _sahihi na makosa_ hapa - ni kuchunguza chaguo kwa majaribio na makosa na kujenga intuisheni ya kile kinachofanya kazi kwa modeli na uwanja wa matumizi uliotolewa.

_Kwa sababu hii hakuna sehemu za Suluhisho la Kodi katika somo hili. Badala yake, Notebook itakuwa na seli za Markdown zenye kichwa "Suluhisho Langu:" zinazoonyesha mfano mmoja wa matokeo kwa marejeleo._

<!--
TEMPLATE YA SOMO:
Funga sehemu na muhtasari na rasilimali za kujifunza kwa kujiongoza.
-->

## Ukaguzi wa Maarifa

Ni ipi kati ya zifuatazo ni maelekezo mazuri yanayofuata baadhi ya mazoea bora yanayofaa?

1. Nionyeshe picha ya gari jekundu
2. Nionyeshe picha ya gari jekundu la Volvo na modeli XC90 limeegeshwa karibu na mwamba na jua linapozama
3. Nionyeshe picha ya gari jekundu la Volvo na modeli XC90

A: 2, ni maelekezo bora zaidi kwani yanatoa maelezo kuhusu "nini" na yanaingia katika undani (sio gari lolote bali ni muundo na modeli maalum) na pia inaelezea muktadha wa jumla. 3 ni bora ijayo kwani pia ina maelezo mengi.

## 🚀 Changamoto

Jaribu kutumia mbinu ya "kidokezo" na maelekezo: Kamilisha sentensi "Nionyeshe picha ya gari jekundu la Volvo na ". Inajibu nini, na ungeiboresha vipi?

## Kazi Nzuri! Endelea Kujifunza

Unataka kujifunza zaidi kuhusu dhana tofauti za Uhandisi wa Maelekezo? Nenda kwenye [ukurasa wa kujifunza unaoendelea](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kupata rasilimali nyingine nzuri kuhusu mada hii.

Nenda kwenye Somo la 5 ambapo tutatazama [mbinu za juu za utoaji maelekezo](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Kanusho**: 
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwepo kwa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya kibinadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.