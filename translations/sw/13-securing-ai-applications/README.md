<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-06-25T21:35:05+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "sw"
}
-->
# Kulinda Maombi Yako ya AI ya Kizazi

## Utangulizi

Somo hili litajadili:

- Usalama katika muktadha wa mifumo ya AI.
- Hatari na vitisho vya kawaida kwa mifumo ya AI.
- Mbinu na mawazo ya kulinda mifumo ya AI.

## Malengo ya Kujifunza

Baada ya kukamilisha somo hili, utaelewa:

- Vitisho na hatari kwa mifumo ya AI.
- Mbinu na mazoea ya kawaida ya kulinda mifumo ya AI.
- Jinsi utekelezaji wa upimaji wa usalama unaweza kuzuia matokeo yasiyotarajiwa na kupoteza imani ya watumiaji.

## Usalama unamaanisha nini katika muktadha wa AI ya kizazi?

Kadri teknolojia za Akili Bandia (AI) na Kujifunza kwa Mashine (ML) zinavyozidi kuathiri maisha yetu, ni muhimu kulinda sio tu data ya wateja bali pia mifumo ya AI yenyewe. AI/ML inatumika zaidi katika kusaidia mchakato wa kufanya maamuzi yenye thamani kubwa katika tasnia ambapo uamuzi mbaya unaweza kusababisha matokeo mabaya.

Hapa kuna mambo muhimu ya kuzingatia:

- **Athari za AI/ML**: AI/ML zina athari kubwa katika maisha ya kila siku na hivyo kuzilinda imekuwa muhimu.
- **Changamoto za Usalama**: Athari hii ambayo AI/ML inayo inahitaji umakini sahihi ili kushughulikia hitaji la kulinda bidhaa za AI kutoka kwa mashambulizi ya kisasa, iwe na troll au vikundi vilivyopangwa.
- **Matatizo ya Kimkakati**: Sekta ya teknolojia lazima ishughulikie changamoto za kimkakati kwa proaktif ili kuhakikisha usalama wa muda mrefu wa wateja na usalama wa data.

Pia, mifano ya Kujifunza kwa Mashine kwa kiasi kikubwa haiwezi kutofautisha kati ya pembejeo mbaya na data ya kawaida isiyo na madhara. Chanzo kikubwa cha data ya mafunzo kinatokana na hifadhidata za umma zisizopangwa, zisizodhibitiwa, ambazo ziko wazi kwa michango ya watu wengine. Washambuliaji hawahitaji kuharibu hifadhidata wakati wana uhuru wa kuchangia. Kwa muda, data mbaya yenye uaminifu mdogo inakuwa data yenye uaminifu mkubwa, ikiwa muundo wa data/formatting unabaki sahihi.

Ndiyo sababu ni muhimu kuhakikisha uadilifu na ulinzi wa hifadhi za data ambazo mifano yako inatumia kufanya maamuzi.

## Kuelewa vitisho na hatari za AI

Kwa upande wa AI na mifumo inayohusiana, uchafuzi wa data unaonekana kama tishio kubwa zaidi la usalama leo. Uchafuzi wa data ni wakati mtu anabadilisha kwa makusudi taarifa zinazotumiwa kufundisha AI, na kusababisha AI kufanya makosa. Hii ni kutokana na ukosefu wa mbinu za kugundua na kupunguza zilizo sanifu, pamoja na kutegemea kwetu hifadhidata za umma zisizoaminika au zisizopangwa kwa mafunzo. Ili kudumisha uadilifu wa data na kuzuia mchakato wa mafunzo yenye kasoro, ni muhimu kufuatilia asili na mfululizo wa data yako. Vinginevyo, msemo wa zamani "taka ndani, taka nje" unathibitisha kuwa kweli, na kusababisha utendaji wa mfano kuathirika.

Hapa kuna mifano ya jinsi uchafuzi wa data unavyoweza kuathiri mifano yako:

1. **Kubadilisha Lebo**: Katika kazi ya uainishaji wa binary, adui anabadilisha kwa makusudi lebo za sehemu ndogo ya data ya mafunzo. Kwa mfano, sampuli zisizo na madhara zinawekwa lebo kama mbaya, na kusababisha mfano kujifunza miunganiko isiyo sahihi.\
   **Mfano**: Kichujio cha barua taka kinachokosea barua pepe halali kama barua taka kutokana na lebo zilizobadilishwa.
2. **Uchafuzi wa Vipengele**: Mshambuliaji anabadilisha kwa siri vipengele katika data ya mafunzo ili kuanzisha upendeleo au kupotosha mfano.\
   **Mfano**: Kuongeza maneno yasiyo ya lazima kwenye maelezo ya bidhaa ili kudanganya mifumo ya mapendekezo.
3. **Sindano ya Data**: Kuingiza data mbaya kwenye seti ya mafunzo ili kuathiri tabia ya mfano.\
   **Mfano**: Kuanzisha hakiki za watumiaji bandia ili kupotosha matokeo ya uchambuzi wa hisia.
4. **Mashambulizi ya Nyuma**: Adui anaingiza muundo uliofichwa (nyuma) kwenye data ya mafunzo. Mfano unajifunza kutambua muundo huu na kujiendesha vibaya unapochochewa.\
   **Mfano**: Mfumo wa utambuzi wa uso uliopangwa na picha zilizowekwa nyuma ambazo zinakosea kutambua mtu maalum.

Kampuni ya MITRE imeunda [ATLAS (Mandhari ya Vitisho vya Upinzani kwa Mifumo ya Akili Bandia)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), hifadhidata ya maarifa ya mbinu na mbinu zinazotumiwa na wapinzani katika mashambulizi halisi kwenye mifumo ya AI.

> Kuna idadi inayoongezeka ya udhaifu katika mifumo inayowezeshwa na AI, kadri AI inavyozidi kuingizwa huongeza uso wa mashambulizi ya mifumo iliyopo zaidi ya ile ya mashambulizi ya jadi ya mtandao. Tuliunda ATLAS ili kuongeza uelewa wa udhaifu huu wa kipekee na unaoendelea, kadri jamii ya kimataifa inavyozidi kuingiza AI katika mifumo mbalimbali. ATLAS imemodeliwa baada ya mfumo wa MITRE ATT&CK® na mbinu, mbinu, na taratibu zake (TTPs) zinakamilisha zile zilizopo kwenye ATT&CK.

Kama vile mfumo wa MITRE ATT&CK® unavyotumika sana katika usalama wa mtandao wa jadi kwa kupanga hali za kuiga vitisho vya juu, ATLAS hutoa seti ya TTPs inayoweza kutafutwa kwa urahisi ambayo inaweza kusaidia kuelewa vizuri na kujiandaa kwa kujilinda dhidi ya mashambulizi yanayoibuka.

Pia, Mradi wa Usalama wa Programu za Wavuti (OWASP) umeunda "[Orodha ya Juu 10](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" ya udhaifu muhimu zaidi unaopatikana katika maombi yanayotumia LLMs. Orodha inaangazia hatari za vitisho kama vile uchafuzi wa data uliotajwa hapo juu pamoja na vingine kama:

- **Sindano ya Mambo**: mbinu ambapo washambuliaji wanadhibiti Mfano Mkubwa wa Lugha (LLM) kupitia pembejeo zilizotengenezwa kwa uangalifu, na kusababisha kutenda nje ya tabia yake iliyokusudiwa.
- **Udhaifu wa Mnyororo wa Ugavi**: Vipengele na programu zinazounda maombi yanayotumiwa na LLM, kama vile moduli za Python au hifadhidata za nje, zinaweza yenyewe kuathirika na kusababisha matokeo yasiyotarajiwa, kuanzisha upendeleo na hata udhaifu katika miundombinu ya msingi.
- **Kutegemea Kupita Kiasi**: LLMs ni dhaifu na zimekuwa na tabia ya kuota, kutoa matokeo yasiyo sahihi au yasiyo salama. Katika hali kadhaa zilizorekodiwa, watu wamechukua matokeo kama yalivyo na kusababisha matokeo mabaya ya ulimwengu halisi yasiyotarajiwa.

Mshauri wa Wingu wa Microsoft Rod Trent ameandika ebook ya bure, [Lazima Kujifunza Usalama wa AI](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), inayozama kwa kina katika vitisho vya AI vinavyoibuka na inatoa mwongozo wa kina juu ya jinsi ya kukabiliana na hali hizi.

## Upimaji wa Usalama kwa Mifumo ya AI na LLMs

Akili bandia (AI) inabadilisha nyanja na tasnia mbalimbali, ikitoa uwezekano mpya na faida kwa jamii. Hata hivyo, AI pia inaleta changamoto na hatari kubwa, kama vile faragha ya data, upendeleo, ukosefu wa kuelezeka, na matumizi mabaya. Kwa hiyo, ni muhimu kuhakikisha kwamba mifumo ya AI ni salama na inayowajibika, ikimaanisha kuwa inazingatia viwango vya kimaadili na kisheria na inaweza kuaminika na watumiaji na wadau.

Upimaji wa usalama ni mchakato wa kutathmini usalama wa mfumo wa AI au LLM, kwa kutambua na kutumia udhaifu wake. Hii inaweza kufanywa na watengenezaji, watumiaji, au wakaguzi wa watu wa tatu, kulingana na madhumuni na wigo wa upimaji. Baadhi ya mbinu za kawaida za upimaji wa usalama kwa mifumo ya AI na LLMs ni:

- **Usafi wa Data**: Huu ni mchakato wa kuondoa au kufanya data nyeti au ya kibinafsi kuwa isiyo na majina kutoka kwa data ya mafunzo au pembejeo ya mfumo wa AI au LLM. Usafi wa data unaweza kusaidia kuzuia uvujaji wa data na udanganyifu mbaya kwa kupunguza uwezekano wa data ya siri au ya kibinafsi.
- **Upimaji wa Upinzani**: Huu ni mchakato wa kuunda na kutumia mifano ya upinzani kwa pembejeo au pato la mfumo wa AI au LLM ili kutathmini uthabiti na uimara wake dhidi ya mashambulizi ya upinzani. Upimaji wa upinzani unaweza kusaidia kutambua na kupunguza udhaifu na mapungufu ya mfumo wa AI au LLM ambayo yanaweza kutumiwa na washambuliaji.
- **Uthibitishaji wa Mfano**: Huu ni mchakato wa kuthibitisha usahihi na ukamilifu wa vigezo vya mfano au usanifu wa mfumo wa AI au LLM. Uthibitishaji wa mfano unaweza kusaidia kugundua na kuzuia wizi wa mfano kwa kuhakikisha kwamba mfano umelindwa na kuthibitishwa.
- **Uthibitishaji wa Pato**: Huu ni mchakato wa kuthibitisha ubora na uaminifu wa pato la mfumo wa AI au LLM. Uthibitishaji wa pato unaweza kusaidia kugundua na kusahihisha udanganyifu mbaya kwa kuhakikisha kwamba pato ni thabiti na sahihi.

OpenAI, kiongozi katika mifumo ya AI, imeanzisha mfululizo wa _tathmini za usalama_ kama sehemu ya mpango wao wa mtandao wa timu nyekundu, unaolenga kupima mifumo ya AI kwa matumaini ya kuchangia usalama wa AI.

> Tathmini zinaweza kuanzia majaribio rahisi ya maswali na majibu hadi simulizi ngumu zaidi. Kama mifano halisi, hapa kuna tathmini za sampuli zilizotengenezwa na OpenAI kwa kutathmini tabia za AI kutoka pembe nyingi:

#### Usadishaji

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Je, mfumo wa AI unaweza kumdanganya mfumo mwingine wa AI kusema neno la siri kwa ufanisi kiasi gani?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Je, mfumo wa AI unaweza kushawishi mfumo mwingine wa AI kutoa pesa kwa ufanisi kiasi gani?
- [Pendekezo la Kura](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Je, mfumo wa AI unaweza kushawishi mfumo mwingine wa AI kuunga mkono pendekezo la kisiasa kwa ufanisi kiasi gani?

#### Steganografia (ujumbe uliofichwa)

- [Steganografia](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Je, mfumo wa AI unaweza kupitisha ujumbe wa siri bila kukamatwa na mfumo mwingine wa AI kwa ufanisi kiasi gani?
- [Mfinyazo wa Maandishi](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Je, mfumo wa AI unaweza kufinya na kufinyua ujumbe, kuwezesha kuficha ujumbe wa siri kwa ufanisi kiasi gani?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Je, mfumo wa AI unaweza kuratibu na mfumo mwingine wa AI, bila mawasiliano ya moja kwa moja kwa ufanisi kiasi gani?

### Usalama wa AI

Ni muhimu kwamba tuangalie kulinda mifumo ya AI dhidi ya mashambulizi mabaya, matumizi mabaya, au matokeo yasiyotarajiwa. Hii inajumuisha kuchukua hatua za kuhakikisha usalama, uaminifu, na uaminifu wa mifumo ya AI, kama vile:

- Kulinda data na algorithmi zinazotumika kufundisha na kuendesha mifano ya AI
- Kuzuia ufikiaji usioidhinishwa, udanganyifu, au uharibifu wa mifumo ya AI
- Kugundua na kupunguza upendeleo, ubaguzi, au masuala ya kimaadili katika mifumo ya AI
- Kuhakikisha uwajibikaji, uwazi, na kuelezeka kwa maamuzi na vitendo vya AI
- Kuunganisha malengo na maadili ya mifumo ya AI na yale ya wanadamu na jamii

Usalama wa AI ni muhimu kwa kuhakikisha uadilifu, upatikanaji, na usiri wa mifumo na data ya AI. Baadhi ya changamoto na fursa za usalama wa AI ni:

- Fursa: Kuingiza AI katika mikakati ya usalama wa mtandao kwani inaweza kuchukua jukumu muhimu katika kutambua vitisho na kuboresha nyakati za kujibu. AI inaweza kusaidia kuboresha na kuongeza utambuzi na kupunguza mashambulizi ya mtandao, kama vile udukuzi, programu hasidi, au ransomware.
- Changamoto: AI inaweza pia kutumiwa na wapinzani kuzindua mashambulizi ya kisasa, kama vile kuunda maudhui bandia au ya kupotosha, kuiga watumiaji, au kutumia udhaifu katika mifumo ya AI. Kwa hiyo, watengenezaji wa AI wana jukumu la kipekee la kubuni mifumo ambayo ni thabiti na yenye uimara dhidi ya matumizi mabaya.

### Ulinzi wa Data

LLMs zinaweza kusababisha hatari kwa faragha na usalama wa data wanayotumia. Kwa mfano, LLMs zinaweza kukumbuka na kuvuja taarifa nyeti kutoka kwa data yao ya mafunzo, kama vile majina ya kibinafsi, anwani, nywila, au namba za kadi ya mkopo. Pia zinaweza kudanganywa au kushambuliwa na wahusika wabaya wanaotaka kutumia udhaifu wao au upendeleo wao. Kwa hiyo, ni muhimu kuwa na ufahamu wa hatari hizi na kuchukua hatua zinazofaa kulinda data inayotumiwa na LLMs. Kuna hatua kadhaa unazoweza kuchukua kulinda data inayotumiwa na LLMs. Hatua hizi ni pamoja na:

- **Kupunguza kiasi na aina ya data wanayoshiriki na LLMs**: Shiriki tu data ambayo ni muhimu na inayohusiana na madhumuni yaliyokusudiwa, na epuka kushiriki data yoyote ambayo ni nyeti, ya siri, au ya kibinafsi. Watumiaji pia wanapaswa kufanya data wanayoshiriki na LLMs kuwa isiyo na majina au kuisimba, kama vile kwa kuondoa au kuficha taarifa yoyote inayotambulika, au kutumia njia salama za mawasiliano.
- **Kuthibitisha data ambayo LLMs inazalisha**: Kagua daima usahihi na ubora wa pato linalozalishwa na LLMs ili kuhakikisha halina taarifa yoyote isiyotakiwa au isiyofaa.
- **Kuripoti na kutoa tahadhari kuhusu uvunjaji wowote wa data au matukio**: Kuwa makini kwa shughuli au tabia zozote zisizo za kawaida au za kutilia shaka kutoka kwa LLMs, kama vile kuunda maandiko yasiyo ya maana, yasiyo sahihi, yanayokasirisha, au yenye madhara. Hii inaweza kuwa dalili ya uvunjaji wa data au tukio la usalama.

Usalama wa data, utawala, na uzingatiaji ni muhimu kwa shirika lolote linalotaka kutumia nguvu ya data na AI katika mazingira ya wingu la aina nyingi. Kulinda na kusimamia data yako yote ni kazi ngumu na yenye sura nyingi. Unahitaji kulinda na kusimamia aina tofauti za data (iliyojengwa, isiyo na muundo, na data inayozalishwa na AI) katika maeneo tofauti katika wingu nyingi, na unahitaji kuzingatia usalama wa data uliopo na wa baadaye, utawala, na kanuni za AI. Ili kulinda data yako, unahitaji kuchukua mazoea bora na tahadhari, kama vile:

- Tumia huduma za wingu au majukwaa yanayotoa vipengele vya ulinzi wa data na faragha.
- Tumia zana za ubora wa data na uthibitishaji ili kukagua data yako kwa makosa, kutofautiana, au kasoro.
- Tumia mifumo ya utawala wa data na maadili ili kuhakikisha data yako inatumika kwa njia inayowajibika na wazi.

### Kuiga vitisho vya

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwepo kwa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo chenye mamlaka. Kwa habari muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatuwajibiki kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.