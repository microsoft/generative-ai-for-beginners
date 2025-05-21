<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-05-19T23:03:53+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "sw"
}
-->
# Kuhakikisha Usalama wa Programu Zako za AI Zinazozalisha

## Utangulizi

Somo hili litashughulikia:

- Usalama katika muktadha wa mifumo ya AI.
- Hatari na vitisho vya kawaida kwa mifumo ya AI.
- Mbinu na mambo ya kuzingatia ili kuhakikisha usalama wa mifumo ya AI.

## Malengo ya Kujifunza

Baada ya kukamilisha somo hili, utakuwa na uelewa wa:

- Vitisho na hatari kwa mifumo ya AI.
- Mbinu na mazoea ya kawaida ya kuhakikisha usalama wa mifumo ya AI.
- Jinsi utekelezaji wa majaribio ya usalama unavyoweza kuzuia matokeo yasiyotarajiwa na kupoteza imani ya mtumiaji.

## Usalama unamaanisha nini katika muktadha wa AI inayozalisha?

Kadri teknolojia za Akili Bandia (AI) na Kujifunza kwa Mashine (ML) zinavyozidi kuathiri maisha yetu, ni muhimu kulinda sio tu data ya wateja bali pia mifumo ya AI yenyewe. AI/ML inatumika zaidi katika kusaidia michakato ya kufanya maamuzi ya thamani kubwa katika tasnia ambapo uamuzi mbaya unaweza kusababisha matokeo mabaya.

Hapa kuna mambo muhimu ya kuzingatia:

- **Athari za AI/ML**: AI/ML ina athari kubwa katika maisha ya kila siku na hivyo kuzilinda imekuwa muhimu.
- **Changamoto za Usalama**: Athari hii ya AI/ML inahitaji umakini sahihi ili kushughulikia hitaji la kulinda bidhaa za AI kutokana na mashambulizi ya hali ya juu, iwe na wanyanyasaji au vikundi vilivyopangwa.
- **Matatizo ya Kistratejia**: Sekta ya teknolojia lazima ichukue hatua za kijasiri kushughulikia changamoto za kistratejia ili kuhakikisha usalama wa muda mrefu wa wateja na usalama wa data.

Pia, mifano ya Kujifunza kwa Mashine haiwezi kutofautisha kati ya data yenye nia mbaya na data isiyo ya kawaida. Chanzo kikubwa cha data ya mafunzo kinatokana na seti za data za umma ambazo hazijachujwa, ambazo zinakaribisha michango ya wahusika wa nje. Washambuliaji hawahitaji kuhujumu seti za data wakati wanaruhusiwa kuchangia kwenye hizo. Kwa muda, data yenye nia mbaya yenye uhakika mdogo inakuwa data yenye uhakika mkubwa ikiwa muundo wa data unabaki sahihi.

Hii ndiyo sababu ni muhimu kuhakikisha uadilifu na ulinzi wa hifadhi za data ambazo mifano yako inatumia kufanya maamuzi.

## Kuelewa vitisho na hatari za AI

Kwa upande wa AI na mifumo inayohusiana, uchafuzi wa data ni tishio kubwa la usalama kwa sasa. Uchafuzi wa data ni pale mtu anapobadilisha kwa makusudi habari inayotumiwa kufundisha AI, na kusababisha kufanya makosa. Hii ni kutokana na ukosefu wa mbinu za kugundua na kupunguza zilizowekwa, pamoja na utegemezi wetu kwenye seti za data za umma ambazo hazijachujwa kwa mafunzo. Ili kudumisha uadilifu wa data na kuzuia mchakato wa mafunzo usiofaa, ni muhimu kufuatilia asili na urithi wa data yako. Vinginevyo, msemo wa zamani "taka ndani, taka nje" unakuwa kweli, na kusababisha utendaji wa mfano uliodhoofika.

Hapa kuna mifano ya jinsi uchafuzi wa data unavyoweza kuathiri mifano yako:

1. **Kubadilisha Lebo**: Katika kazi ya uainishaji wa binary, adui hubadilisha lebo za subset ndogo ya data ya mafunzo kwa makusudi. Kwa mfano, sampuli zisizo na madhara zinawekwa alama kama zenye nia mbaya, na kusababisha mfano kujifunza miunganiko isiyo sahihi.\
   **Mfano**: Kichujio cha barua taka kinachokosea barua pepe halali kama barua taka kutokana na lebo zilizobadilishwa.
2. **Uchafuzi wa Sifa**: Mshambuliaji hubadilisha kwa ujanja sifa katika data ya mafunzo ili kuanzisha upendeleo au kupotosha mfano.\
   **Mfano**: Kuongeza maneno yasiyohusiana kwenye maelezo ya bidhaa ili kupotosha mifumo ya mapendekezo.
3. **Uingizaji wa Data**: Kuingiza data yenye nia mbaya kwenye seti ya mafunzo ili kushawishi tabia ya mfano.\
   **Mfano**: Kuanzisha maoni ya watumiaji bandia ili kupotosha matokeo ya uchambuzi wa hisia.
4. **Mashambulizi ya Nyuma ya Mlango**: Adui huingiza muundo uliofichwa (mlango wa nyuma) kwenye data ya mafunzo. Mfano unajifunza kutambua muundo huu na unafanya kwa nia mbaya unapoanzishwa.\
   **Mfano**: Mfumo wa utambuzi wa uso uliofundishwa na picha zilizo na mlango wa nyuma zinazomtambulisha vibaya mtu maalum.

Shirika la MITRE limeunda [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), hazina ya maarifa ya mbinu na mbinu zinazotumiwa na wapinzani katika mashambulizi halisi kwenye mifumo ya AI.

> Kuna idadi inayoongezeka ya udhaifu katika mifumo inayowezeshwa na AI, kwani ushirikishwaji wa AI huongeza uso wa shambulio wa mifumo iliyopo zaidi ya yale ya mashambulizi ya kawaida ya mtandao. Tuliunda ATLAS ili kuongeza ufahamu wa udhaifu huu wa kipekee na unaoendelea, kwani jamii ya kimataifa inavyozidi kuingiza AI katika mifumo mbalimbali. ATLAS imeundwa kufuata mfumo wa MITRE ATT&CK® na mbinu zake ni za ziada kwa zile zilizopo katika ATT&CK.

Kama mfumo wa MITRE ATT&CK®, ambao unatumika sana katika usalama wa mtandao wa jadi kwa kupanga hali za kuiga vitisho vya hali ya juu, ATLAS hutoa seti ya mbinu za TTP zinazoweza kutafutwa kwa urahisi ambazo zinaweza kusaidia kuelewa na kujiandaa vyema kwa ajili ya kujilinda dhidi ya mashambulizi yanayojitokeza.

Pia, Mradi wa Usalama wa Programu za Wavuti wa Wazi (OWASP) umeunda "[Orodha ya 10 Bora](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" ya udhaifu muhimu zaidi unaopatikana katika programu zinazotumia LLMs. Orodha hiyo inaangazia hatari za vitisho kama vile uchafuzi wa data uliotajwa hapo awali pamoja na vingine kama:

- **Uingizaji wa Maagizo**: mbinu ambapo washambuliaji wanadhibiti Mfano wa Lugha Kubwa (LLM) kupitia pembejeo zilizotengenezwa kwa uangalifu, na kuufanya utende kinyume na tabia yake iliyokusudiwa.
- **Udhaifu wa Mnyororo wa Ugavi**: Vipengele na programu zinazounda programu zinazotumiwa na LLM, kama vile moduli za Python au seti za data za nje, zinaweza kuhujumiwa zenyewe na kusababisha matokeo yasiyotarajiwa, upendeleo ulioanzishwa na hata udhaifu katika miundombinu ya msingi.
- **Kutegemea Kupita Kiasi**: LLM zinaweza kukosea na zimekuwa na tabia ya kufikiria mambo yasiyo sahihi, kutoa matokeo yasiyo sahihi au yasiyo salama. Katika hali kadhaa zilizorekodiwa, watu wamechukua matokeo kama yalivyo na kusababisha matokeo hasi yasiyotarajiwa katika ulimwengu halisi.

Mshauri wa Wingu wa Microsoft Rod Trent ameandika kitabu cha bure, [Lazima Ujifunze Usalama wa AI](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), ambacho kinaingia kwa kina katika vitisho hivi na vingine vinavyojitokeza vya AI na kinatoa mwongozo wa kina juu ya jinsi ya kushughulikia hali hizi vyema.

## Kujaribu Usalama wa Mifumo ya AI na LLMs

Akili bandia (AI) inabadilisha nyanja na tasnia mbalimbali, ikitoa uwezekano na faida mpya kwa jamii. Hata hivyo, AI pia inaleta changamoto na hatari kubwa, kama vile faragha ya data, upendeleo, ukosefu wa ufafanuzi, na matumizi mabaya. Kwa hiyo, ni muhimu kuhakikisha kuwa mifumo ya AI ni salama na inayowajibika, ikimaanisha kuwa inafuata viwango vya kimaadili na kisheria na inaweza kuaminiwa na watumiaji na wadau.

Kujaribu usalama ni mchakato wa kutathmini usalama wa mfumo wa AI au LLM, kwa kutambua na kutumia udhaifu wao. Hii inaweza kufanywa na watengenezaji, watumiaji, au wakaguzi wa wahusika wa tatu, kulingana na madhumuni na upeo wa majaribio. Baadhi ya mbinu za kawaida za majaribio ya usalama kwa mifumo ya AI na LLMs ni:

- **Usafishaji wa Data**: Huu ni mchakato wa kuondoa au kuficha taarifa nyeti au za kibinafsi kutoka kwa data ya mafunzo au pembejeo ya mfumo wa AI au LLM. Usafishaji wa data unaweza kusaidia kuzuia uvujaji wa data na udanganyifu kwa kupunguza mfiduo wa data ya siri au ya kibinafsi.
- **Kujaribu kwa Adui**: Huu ni mchakato wa kutengeneza na kutumia mifano ya adui kwa pembejeo au matokeo ya mfumo wa AI au LLM ili kutathmini uimara wake na uwezo wa kustahimili mashambulizi ya adui. Kujaribu kwa adui kunaweza kusaidia kutambua na kupunguza udhaifu na mapungufu ya mfumo wa AI au LLM ambayo yanaweza kutumiwa na washambuliaji.
- **Uthibitishaji wa Mfano**: Huu ni mchakato wa kuthibitisha usahihi na ukamilifu wa vigezo vya mfano au usanifu wa mfumo wa AI au LLM. Uthibitishaji wa mfano unaweza kusaidia kugundua na kuzuia kuiba mfano kwa kuhakikisha kuwa mfano unalindwa na kuthibitishwa.
- **Uthibitishaji wa Matokeo**: Huu ni mchakato wa kuthibitisha ubora na uaminifu wa matokeo ya mfumo wa AI au LLM. Uthibitishaji wa matokeo unaweza kusaidia kugundua na kusahihisha udanganyifu kwa kuhakikisha kuwa matokeo ni thabiti na sahihi.

OpenAI, kiongozi katika mifumo ya AI, imeanzisha mfululizo wa _tathmini za usalama_ kama sehemu ya mpango wao wa mtandao wa timu nyekundu, unaolenga kujaribu matokeo ya mifumo ya AI kwa matumaini ya kuchangia usalama wa AI.

> Tathmini zinaweza kuanzia majaribio rahisi ya maswali na majibu hadi kwenye simulizi tata zaidi. Kama mifano halisi, hapa kuna tathmini za sampuli zilizotengenezwa na OpenAI kwa ajili ya kutathmini tabia za AI kutoka pembejeo mbalimbali:

#### Usadikishaji

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Je, mfumo wa AI unaweza kumdanganya mfumo mwingine wa AI kusema neno la siri kwa kiwango gani?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Je, mfumo wa AI unaweza kumshawishi mfumo mwingine wa AI kutoa pesa kwa kiwango gani?
- [Pendekezo la Kura](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Je, mfumo wa AI unaweza kushawishi mfumo mwingine wa AI kuunga mkono pendekezo la kisiasa kwa kiwango gani?

#### Steganografia (ujumbe uliofichwa)

- [Steganografia](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Je, mfumo wa AI unaweza kupitisha ujumbe wa siri bila kugunduliwa na mfumo mwingine wa AI kwa kiwango gani?
- [Mfinyazo wa Maandishi](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Je, mfumo wa AI unaweza kufinya na kufungua ujumbe, ili kuwezesha kuficha ujumbe wa siri kwa kiwango gani?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Je, mfumo wa AI unaweza kuratibu na mfumo mwingine wa AI, bila mawasiliano ya moja kwa moja kwa kiwango gani?

### Usalama wa AI

Ni muhimu kulenga kulinda mifumo ya AI kutokana na mashambulizi yenye nia mbaya, matumizi mabaya, au matokeo yasiyotarajiwa. Hii inajumuisha kuchukua hatua za kuhakikisha usalama, uaminifu, na kuaminika kwa mifumo ya AI, kama vile:

- Kulinda data na algorithimu zinazotumika kufundisha na kuendesha mifano ya AI
- Kuzuia ufikiaji usioidhinishwa, udanganyifu, au hujuma ya mifumo ya AI
- Kugundua na kupunguza upendeleo, ubaguzi, au masuala ya kimaadili katika mifumo ya AI
- Kuhakikisha uwajibikaji, uwazi, na ufafanuzi wa maamuzi na vitendo vya AI
- Kulinganisha malengo na maadili ya mifumo ya AI na yale ya wanadamu na jamii

Usalama wa AI ni muhimu kwa kuhakikisha uadilifu, upatikanaji, na usiri wa mifumo ya AI na data. Baadhi ya changamoto na fursa za usalama wa AI ni:

- Fursa: Kujumuisha AI katika mikakati ya usalama wa mtandao kwani inaweza kuwa na jukumu muhimu katika kutambua vitisho na kuboresha nyakati za majibu. AI inaweza kusaidia kuboresha na kuongeza otomatiki katika kugundua na kupunguza mashambulizi ya mtandao, kama vile ulaghai, programu hasidi, au fidia.
- Changamoto: AI pia inaweza kutumiwa na wapinzani kuzindua mashambulizi ya hali ya juu, kama vile kutengeneza maudhui bandia au ya kupotosha, kuiga watumiaji, au kutumia udhaifu katika mifumo ya AI. Kwa hiyo, watengenezaji wa AI wana jukumu la kipekee la kubuni mifumo ambayo ni thabiti na inayostahimili matumizi mabaya.

### Ulinzi wa Data

LLMs zinaweza kuleta hatari kwa faragha na usalama wa data wanayotumia. Kwa mfano, LLMs zinaweza kukumbuka na kutoa taarifa nyeti kutoka kwa data zao za mafunzo, kama vile majina ya watu, anwani, nywila, au nambari za kadi za mkopo. Pia zinaweza kudanganywa au kushambuliwa na wahusika wenye nia mbaya wanaotaka kutumia udhaifu au upendeleo wao. Kwa hiyo, ni muhimu kuwa na ufahamu wa hatari hizi na kuchukua hatua zinazofaa kulinda data inayotumiwa na LLMs. Kuna hatua kadhaa unazoweza kuchukua kulinda data inayotumiwa na LLMs. Hatua hizi ni pamoja na:

- **Kuweka mipaka ya kiasi na aina ya data wanayoshiriki na LLMs**: Shiriki tu data ambayo ni muhimu na inayohusiana na madhumuni yaliyokusudiwa, na epuka kushiriki data yoyote ambayo ni nyeti, ya siri, au ya kibinafsi. Watumiaji wanapaswa pia kuficha au kuficha data wanayoshiriki na LLMs, kama vile kwa kuondoa au kuficha taarifa yoyote inayotambulika, au kutumia njia salama za mawasiliano.
- **Kuthibitisha data ambayo LLMs huzalisha**: Kagua kila mara usahihi na ubora wa matokeo yanayozalishwa na LLMs ili kuhakikisha hayana taarifa zisizohitajika au zisizofaa.
- **Kuripoti na kutoa tahadhari yoyote ya uvunjaji wa data au matukio**: Kuwa makini na shughuli au tabia yoyote ya kutilia shaka au isiyo ya kawaida kutoka kwa LLMs, kama vile kuzalisha maandishi yasiyo ya maana, yasiyo sahihi, ya kukera, au yenye madhara. Hii inaweza kuwa ishara ya uvunjaji wa data au tukio la usalama.

Usalama wa data, utawala, na kufuata sheria ni muhimu kwa shirika lolote linalotaka kutumia nguvu ya data na AI katika mazingira ya wingu nyingi. Kulinda na kudhibiti data yako yote ni kazi ngumu na ya pande nyingi. Unahitaji kulinda na kudhibiti aina tofauti za data (iliyopangwa, isiyopangwa, na data inayozalishwa na AI) katika maeneo tofauti kwenye wingu nyingi, na unahitaji kuzingatia sheria za sasa na zijazo za usalama wa data, utawala, na AI. Ili kulinda data yako, unahitaji kuchukua baadhi ya mazoea bora na tahadhari, kama vile:

- Tumia huduma za wingu au majukwaa yanayotoa vipengele vya ulinzi wa data na faragha.
- Tumia zana za ubora wa data na uthibitishaji ili kukagua data yako kwa makosa, kutofautiana, au hali zisizo za kawaida.
- Tumia mifumo ya utawala wa data na maadili ili kuhakikisha data

**Kanusho**: 
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokamilika. Hati asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo rasmi. Kwa habari muhimu, tafsiri ya kitaalamu ya kibinadamu inapendekezwa. Hatuwajibiki kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.