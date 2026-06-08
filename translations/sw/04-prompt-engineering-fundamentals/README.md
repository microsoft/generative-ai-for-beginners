# Misingi ya Uhandisi wa Prompt

[![Misingi ya Uhandisi wa Prompt](../../../translated_images/sw/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Utangulizi
Moduli hii inashughulikia dhana na mbinu muhimu za kuunda prompt madhubuti katika mifano ya generative AI. Jinsi unavyoandika prompt yako kwa LLM pia ni muhimu. Prompt iliyoundwa kwa uangalifu inaweza kupata ubora bora wa majibu. Lakini hasa, maneno kama _prompt_ na _uhandisi wa prompt_ yanamaanisha nini? Na ninawezaje kuboresha _kuzalisha prompt_ ninayotuma kwa LLM? Hivi ndivyo maswali tutajaribu kuyajibu ndani ya sura hii na ile inayofuata.

_Generative AI_ ina uwezo wa kuunda maudhui mapya (mfano, maandishi, picha, sauti, msimbo n.k.) kama jibu kwa maombi ya mtumiaji. Hufanikisha hili kwa kutumia _Mifano Mikubwa ya Lugha_ kama mfululizo wa GPT wa OpenAI ("Generative Pre-trained Transformer") ambao wamefundishwa kutumia lugha ya asili na msimbo.

Watumiaji sasa wanaweza kuingiliana na mifano hii kwa kutumia mbinu zinazojulikana kama mazungumzo, bila haja ya ujuzi wa kiufundi au mafunzo. Mifano ni _inayotegemea prompt_ - watumiaji hutuma maingizo ya maandishi (prompt) na kupata jibu la AI (kamilisho). Kisha wanaweza "kuzungumza na AI" kwa mzunguko wa kuendelea, wakiboresha prompt zao hadi jibu lifikishe matarajio yao.

"Prompts" sasa zinakuwa kiolesura kuu cha _kuprograma_ kwa programu za generative AI, zikimwambia mfano nini cha kufanya na kuathiri ubora wa majibu yanayorejeshwa. "Uhandisi wa Prompt" ni uwanja unaokua kwa kasi wa masomo unaojikita katika _usanifu na uboreshaji_ wa prompts ili kutoa majibu yenye ubora na uthabiti kwa kiwango kikubwa.

## Malengo ya Kujifunza

Katika somo hili, tunajifunza nini Uhandisi wa Prompt ni, kwanini ni muhimu, na jinsi tunavyoweza kuunda prompts madhubuti kwa mfano na lengo la matumizi. Tutafahamu dhana za msingi na mbinu bora za uhandisi wa prompt - na kujifunza kuhusu mazingira ya mazoezi ya Jupyter Notebooks "sandbox" ambapo tunaweza kuona dhana hizi zikihusishwa na mifano halisi.

Mwisho wa somo hili tutakuwa na uwezo wa:

1. Kueleza nini uhandisi wa prompt ni na kwanini ni muhimu.
2. Kuelezea vipengele vya prompt na jinsi vinavyotumika.
3. Kujifunza mbinu bora na mbinu za uhandisi wa prompt.
4. Kutumia mbinu zilizojifunza kwenye mifano halisi, kwa kutumia endpoint ya OpenAI.

## Maneno Muhimu

Uhandisi wa Prompt: Mazoezi ya kubuni na kuboresha maingizo ili kuongoza mifano ya AI kutoa matokeo yaliyo yajayo.
Tokenization: Mchakato wa kubadilisha maandishi kuwa vidonge vidogo, vinavyoitwa tokens, ambavyo mfano unaweza kuelewa na kusindika.
Instruction-Tuned LLMs: Mifano Mikubwa ya Lugha (LLMs) ambayo imesanifiwa kwa maagizo maalum ili kuboresha usahihi na umuhimu wa majibu yake.

## Sehemu ya Mazoezi

Uhandisi wa prompt kwa sasa ni sanaa zaidi kuliko sayansi. Njia bora ya kuboresha hisia zetu juu yake ni _kufanya mazoezi zaidi_ na kutumia mbinu ya jaribio-na-kosa inayochanganya utaalamu wa eneo la matumizi na mbinu zilizo pendekezwa na uboreshaji wa mifano maalum.

Jupyter Notebook inayokuja na somo hili hutoa mazingira ya _sandbox_ ambapo unaweza kujaribu unachojifunza - unapopita au sehemu ya changamoto ya msimbo mwishoni. Ili kutekeleza mazoezi, utahitaji:

1. **Kitufe cha API cha Azure OpenAI** - kiunga cha huduma kwa LLM iliyosambazwa.
2. **Mazingira ya Python Runtime** - ambapo Notebook inaweza kuendeshwa.
3. **Mazingira ya Kwenye Kompyuta (Local Env Variables)** - _kamilisha hatua za [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) sasa ili kuwa tayari_.

Notebook inakuja na mazoezi ya _kuanzia_ - lakini unahimizwa kuongeza sehemu zako mwenyewe za _Markdown_ (maelezo) na _Code_ (maombi ya prompt) kujaribu mifano zaidi au mawazo - na kujenga hisia yako ya muundo wa prompt.

## Mwashauri Aliyochora

Unataka kupata picha kubwa ya kile somo hili linashughulikia kabla hujaza ndani? Angalia mwandishi huu aliyechora, unaokupa hisia za mada kuu zinazoshughulikiwa na mambo muhimu ya kuzingatia kila moja. Ramani ya somo inakupeleka kutoka kwa kuelewa dhana za msingi na changamoto hadi kuzitatua kwa mbinu za uhandisi wa prompt zinazofaa na mbinu bora. Kumbuka kuwa sehemu ya "Mbinu Zaidi (Advanced Techniques)" katika mwongozo huu inahusu maudhui yanayoshughulikiwa katika sura _ifuatayo_ ya mtaala huu.

![Mwashauri Aliyochora wa Uhandisi wa Prompt](../../../translated_images/sw/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Kampuni Yetu

Sasa, tuseme kuhusu jinsi _mada hii_ inavyo husiana na dhamira yetu ya kuanzisha kampuni ya kuleta [uvumbuzi wa AI katika elimu](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Tunataka kuunda programu za AI zinazoendeshwa kwa ajili ya _kujifunza binafsi_ - kwa hivyo fikiria jinsi watumiaji tofauti wa programu yetu wanaweza "kubuni" prompts:

- **Wasimamizi** wanaweza kumuomba AI _kuchambua data ya mtaala ili kubaini mapungufu katika upitishaji_. AI inaweza kufupisha matokeo au kuyataja kwa msimbo.
- **Walimu** wanaweza kumuomba AI _kutengeneza mpango wa somo kwa hadhira na mada maalum_. AI inaweza kujenga mpango binafsi kwa muundo uliotajwa.
- **Wanafunzi** wanaweza kumuomba AI _kuwa mwalimu wa somo gumu_. AI inaweza sasa kuwaongoza wanafunzi kwa masomo, vidokezo na mifano inayowafaa kiwango chao.

Hiyo ni kielelezo kidogo tu cha kile kinachoendelea. Angalia [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - maktaba ya prompts iliyo wazi inayosimamiwa na wataalamu wa elimu - kupata hisia pana za uwezekano! _Jaribu kuendesha baadhi ya prompts hizo kwenye sandbox au kutumia OpenAI Playground kuona kinatokea!_

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #1:
Prompt Engineering.
Define it and explain why it is needed.
-->

## Uhandisi wa Prompt ni Nini?

Tulianza somo hili kwa kufafanua **Uhandisi wa Prompt** kama mchakato wa _kubuni na kuboresha_ maingizo ya maandishi (prompts) ili kutoa majibu thabiti na yenye ubora (kamilisho) kwa lengo lililowekwa la programu na mfano. Tunaweza kufikiria hili kama mchakato wa hatua 2:

- _kubuni_ prompt ya awali kwa mfano na lengo fulani
- _kuboresha_ prompt kwa hatua kwa hatua ili kuboresha ubora wa jibu

Huu lazima uwe mchakato wa jaribio-na-kosa unaohitaji hisia za mtumiaji na jitihada kupata matokeo bora. Kwanini ni muhimu? Ili kujibu hiyo, kwanza tunahitaji kuelewa dhana tatu:

- _Tokenization_ = jinsi mfano "unaona" prompt
- _Base LLMs_ = jinsi mfano wa msingi "unasindika" prompt
- _Instruction-Tuned LLMs_ = jinsi mfano unaweza kuona "kazi" sasa

### Tokenization

LLM inaona prompts kama _mlolongo wa tokens_ ambapo mifano tofauti (au matoleo tofauti ya mfano) inaweza kugawanya prompt moja kwa njia tofauti. Kwa kuwa LLMs hufunzwa kwa tokens (na si maandishi ghafi), jinsi prompts zilivyo tokenized ina athari moja kwa moja kwa ubora wa jibu lililotengenezwa.

Ili kupata hisia ya jinsi tokenization inavyofanya kazi, jaribu zana kama [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) zilizoonyeshwa hapa chini. Nakili prompt yako - na uone jinsi inavyogeuzwa kuwa tokens, ukiangalia jinsi tabia za nafasi na alama za uandikishaji zinavyoshughulikiwa. Kumbuka kuwa mfano huu unaonyesha LLM ya zamani (GPT-3) - hivyo kujaribu na mfano mpya kunaweza kutoa matokeo tofauti.

![Tokenization](../../../translated_images/sw/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Dhana: Mifano ya Msingi

Baada ya prompt kugawanywa tokens, kazi kuu ya ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (au mfano wa Msingi) ni kutabiri token inayofuata katika mfululizo huo. Kwa kuwa LLMs zimefundishwa kwenye seti kubwa za maandishi, zina ufahamu mzuri wa uhusiano wa takwimu kati ya tokens na zinaweza kufanya utabiri huo kwa uhakika fulani. Kumbuka kuwa hawaelewi _maana_ ya maneno kwenye prompt au token; wanaona tu mfano ambao wanaweza "kukamilisha" kwa utabiri wao ujao. Wanaweza kuendelea kutabiri mfululizo hadi kuingiliwa na mtumiaji au kufikia masharti yaliyowekwa awali.

Unataka kuona jinsi ukamilisho wa prompt-based unavyofanya kazi? Weka prompt iliyo juu kwenye Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) kwa mipangilio ya chaguo-msingi. Mfumo umeundwa kutumia prompts kama maombi ya maelezo - hivyo utaona jibu linalokidhi muktadha huu.

Lakini mtumiaji angependa kuona kitu maalum kinachokidhi vigezo vya lengo au kazi? Hapa ndipo _Instruction-Tuned_ LLMs huingia picha.

![Base LLM Chat Completion](../../../translated_images/sw/04-playground-chat-base.65b76fcfde0caa67.webp)

### Dhana: Instruction Tuned LLMs

[Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) huanza na mfano wa msingi na huurekebisha kwa kutumia mifano au wingi wa jozi za ingizo/mazao (mfano, "mijadala" ya mizunguko mingi) inayoweza kuwa na maelekezo wazi - na jibu kutoka AI linajaribu kufuata maelekezo hayo.

Hii hutumia mbinu kama Kujifunza kwa Kujisukuma na Maoni ya Binadamu (RLHF) ambayo huweza kufundisha mfano _kufuata maagizo_ na _kujifunza kutokana na maoni_ ili kutoa majibu yanayofaa zaidi kwa matumizi halisi na yenye umuhimu kwa malengo ya mtumiaji.

Tujaribu - rudi kwenye prompt iliyo juu, lakini sasa badilisha _ujumbe wa mfumo_ kutoa maelekezo haya kama muktadha:

> _Fupisha maudhui ambayo umepewa kwa mwanafunzi wa darasa la pili. Wekeza matokeo katika aya moja yenye pointi 3-5._

Tazama jinsi jibu linavyolindwa sasa kuendana na lengo na muundo uliotakikana? Mwalimu sasa anaweza kutumia jibu hili moja kwa moja katika slaidi zao za somo hilo.

![Instruction Tuned LLM Chat Completion](../../../translated_images/sw/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Kwanini Tunahitaji Uhandisi wa Prompt?

Sasa tunapojua jinsi prompts zinavyosindikwa na LLMs, tuseme kuhusu _kwa nini_ tunahitaji uhandisi wa prompt. Jibu lako linapatikana katika ukweli kwamba LLMs za sasa zina changamoto kadhaa zinazofanya _ukamilisho wa kuaminika na thabiti_ kuwa changamoto zaidi bila juhudi za ujenzi na uboreshaji wa prompt. Kwa mfano:

1. **Majibu ya modeli ni ya nasibu.** _Prompt sawa_ huenda ikatoa majibu tofauti na mifano tofauti au matoleo tofauti ya mfano. Na inaweza hata kutoa matokeo tofauti na _mifano sawa_ katika nyakati tofauti. _Mbinu za uhandisi wa prompt zinaweza kutusaidia kupunguza tofauti hizi kwa kutoa miongozo bora_.

1. **Mifano inaweza kubuni majibu.** Mifano imefundishwa awali kwa seti kubwa lakini finyu za data, ambayo inamaanisha haina ufahamu kuhusu dhana zinazotokea nje ya mafunzo hayo. Kwa hivyo inaweza kutoa majibu yasiyo sahihi, ya kubuni, au hata kukanusha ukweli uliojulikana. _Mbinu za uhandisi wa prompt husaidia watumiaji kugundua na kupunguza ubunifu kama huo kwa kumuuliza AI rasilimali au hoja_.

1. **Uwezo wa mifano utabadilika.** Mifano mipya au vizazi vipya vya mfano vitakuwa na uwezo mkubwa lakini pia vina kasoro na mahitaji ya gharama na ugumu. _Uhandisi wa prompt unaweza kutusaidia kuendeleza mbinu bora na michakato inayotenganisha tofauti na kuendana na mahitaji mahususi ya mfano kwa njia zinazoweza kupanuka na laini_.

Tuwone hili likitokea kwenye OpenAI au Azure OpenAI Playground:

- Tumia prompt moja na usambazaji tofauti wa LLM (mfano, OpenAI, Azure OpenAI, Hugging Face) - umepata tofauti gani?
- Tumia prompt moja mara kwa mara na usambazaji mmoja wa LLM (mfano, Azure OpenAI playground) - tofauti hizo zilikuwa tofauti vipi?

### Mfano wa Ubunifu (Fabrications)

Katika kozi hii, tunatumia kifungu **"fabrication"** kurejelea hali ambapo LLMs wakati mwingine hutengeneza habari zisizo sahihi kimsingi kutokana na vikwazo katika mafunzo yao au mahitaji mengine. Pia unaweza kuwa umesikia hii ikitajwa kama _"halusinasheni"_ katika makala maarufu au makala za utafiti. Hata hivyo, tunapendekeza sana kutumia _"fabrication"_ kama neno ili tusidhuru tabia hiyo kwa kuiiga tabia ya binadamu kwa matokeo yanayotokana na mashine. Hii pia inaimarisha [miongozo ya AI Yenye Uwajibikaji](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) kutoka mtazamo wa istilahi, kuondoa maneno ambayo yanaweza pia kuonekana kuwa na matusi au yasiyo na usawa katika muktadha fulani.

Unataka kupata hisia ya jinsi fabrications zinavyofanya kazi? Fikiria prompt inayomuagiza AI kuunda maudhui kwa mada ambayo haipo (ili kuhakikisha haipatikani katika seti ya mafunzo). Kwa mfano - nilijaribu prompt hii:

> **Prompt:** tengeneza mpango wa somo juu ya Vita vya Watu wa Mars ya mwaka 2076.
Utafutaji wa wavuti ulinionesha kuwa kulikuwa na hadithi za kubuni (kwa mfano, mfululizo wa runinga au vitabu) juu ya vita vya Mariani – lakini hakuna hata moja mwaka 2076. Hekima ya kawaida pia inatuambia kuwa 2076 ni _baadaye_ na kwa hivyo, haiwezi kuhusishwa na tukio halisi.

Basi nini hutokea tunapochukua ombi hili kwa watoa huduma tofauti wa LLM?

> **Jibu 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/sw/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Jibu 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/sw/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Jibu 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/sw/04-fabrication-huggingchat.faf82a0a51278956.webp)

Kama inavyotarajiwa, kila mfano (au toleo la mfano) hutoa majibu tofauti kidogo kutokana na tabia ya kutegemea bahati na utofauti wa uwezo wa mfano. Kwa mfano, mfano mmoja unalenga hadhira ya darasa la nane wakati mwingine unadhani ni mwanafunzi wa shule ya upili. Lakini mifano yote mitatu ilizalisha majibu ambayo yangeweza kumshawishi mtumiaji asiye na taarifa kuwa tukio hilo ni halisi.

Mbinu za uhandisi wa ombi kama _metaprompting_ na _usanidi wa joto_ zinaweza kupunguza uvumi wa mfano kwa kiwango fulani. Miundo mipya ya uhandisi wa ombi pia huingiza vyombo na mbinu mpya bila mshono ndani ya mtiririko wa ombi, ili kupunguza au kudhibiti baadhi ya athari hizi.

## Uchunguzi wa Kesi: GitHub Copilot

Tuungeze sehemu hii kwa kupata hisia ya jinsi uhandisi wa ombi unavyotumika katika suluhisho za ulimwengu halisi kwa kuangalia Uchunguzi mmoja wa Kesi: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot ni "Programu-jamaa wa AI" wako - hubadilisha maelekezo ya maandishi kuwa makamilisho ya msimbo na umeunganishwa katika mazingira yako ya maendeleo (mfano, Visual Studio Code) kwa uzoefu wa mtumiaji bila mshono. Kama ilivyoandikwa katika mfululizo wa blogu hapa chini, toleo la mwanzo lilianzishwa kwa mfano wa OpenAI Codex - ambapo wahandisi walitambua haraka hitaji la kuimarisha mfano na kuendeleza mbinu bora za uhandisi wa ombi, ili kuboresha ubora wa msimbo. Mnamo Julai, walitambulisha [mfano bora wa AI unaoshinda Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) kwa mapendekezo ya kasi zaidi.

Soma machapisho kwa mpangilio, kufuatilia safari yao ya kujifunza.

- **Mei 2023** | [GitHub Copilot anaboresha kuelewa msimbo wako](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mei 2023** | [Ndani ya GitHub: Kufanya kazi na LLMs nyuma ya GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jun 2023** | [Jinsi ya kuandika maelekezo mazuri kwa GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jul 2023** | [.. GitHub Copilot unasonga mbele Codex kwa mfano ulioimarishwa wa AI](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [Mwongozo wa Mtaalamu wa Uhandisi wa Ombi na LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Jinsi ya kujenga app ya LLM ya biashara: Mafunzo kutoka GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Unaweza pia kuvinjari [blogu yao ya Uhandisi](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) kwa machapisho zaidi kama [hiki](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) kinachoonyesha jinsi mifano na mbinu hizi _zinavyotumika_ kuendesha programu za ulimwengu wa kweli.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #2.
Reinforce the concept with examples and references.

CONCEPT #2:
Prompt Design.
Illustrated with examples.
-->

## Ujenzi wa Ombi

Tumeona kwa nini uhandisi wa ombi ni muhimu - sasa tuelewe jinsi ombi linavyotengenezwa ili tuweze kutathmini mbinu tofauti kwa ajili ya kubuni ombi lenye ufanisi zaidi.

### Ombi la Msingi

Tuanze na ombi la msingi: maandishi yote yaliyotumwa kwa mfano bila muktadha mwingine. Hapa ni mfano - tunapomtumia OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) maneno machache ya wimbo wa taifa wa Marekani, mara moja _huongeza_ majibu kwa mistari inayofuata, ikionyesha tabia ya msingi ya utabiri.

| Ombi (Ingizo)      | Jibu (Matokeo)                                                                                                                        |
| :----------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Inasikika kama unaanza mistari ya "The Star-Spangled Banner," wimbo wa taifa wa Marekani. Mistari kamili ni ...                       |

### Ombi Tata

Sasa tutaongeza muktadha na maagizo kwa ombi hilo msingi. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) huturuhusu kuunda ombi tata kama mkusanyiko wa _jumbe_ zenye:

- Mifungo ya ingizo/mazao ikionyesha ombi la _mtumiaji_ na jibu la _msaidizi_.
- Ujumbe wa mfumo unaoweka muktadha wa tabia au utu wa msaidizi.

Ombi sasa uko katika muundo huu hapa chini, ambapo _ugawaji wa tokeni_ huchukua taarifa muhimu kutoka kwa muktadha na mazungumzo. Sasa, kubadilisha muktadha wa mfumo kunaweza kuwa na athari kubwa kwa ubora wa makamilisho, kama vile ingizo la mtumiaji lilivyotolewa.

```python
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Ombi la Maagizo

Katika mifano hapo juu, ombi la mtumiaji lilikuwa swali rahisi la maandishi ambalo linaweza kufasiriwa kama ombi la taarifa. Kwa ombi za _maagizo_, tunaweza kutumia maandishi hayo kubainisha kazi kwa undani zaidi, tukitoa mwongozo bora kwa AI. Hapa ni mfano:

| Ombi (Ingizo)                                                                                                                                                                                                                         | Jibu (Matokeo)                                                                                                        | Aina ya Maagizo    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- | :----------------- |
| Andika maelezo ya Vita vya Askari wa Mwenyeji                                                                                                                                                                                        | _ilirudisha aya rahisi_                                                                                              | Rahisi             |
| Andika maelezo ya Vita vya Askari wa Mwenyeji. Toa tarehe kuu na matukio na eleza umuhimu wao                                                                                                                                         | _ilirudisha aya ikifuatiwa na orodha ya tarehe kuu na maelezo_                                                     | Tata               |
| Andika maelezo ya Vita vya Askari wa Mwenyeji kwa aya 1. Toa vidokezo 3 vya tarehe kuu na umuhimu wake. Toa vidokezo 3 zaidi vya watu maarufu wa kihistoria na mchango wao. Rudisha matokeo kama faili la JSON | _hurudisha maelezo ya kina kwenye kisanduku cha maandishi, yamepangwa kama JSON ambayo unaweza kunakili-kwazi na kuhakiki_ | Tata. Imeandaliwa. |

## Mocha Muhimu

Katika mifano hapo juu, ombi bado ulikuwa wazi na huruhusu LLM kuamua sehemu gani ya seti yake ya mafunzo ilikuwa muhimu. Kwa mfano wa _mocha muhimu_, maandishi ya ingizo hugawanywa vipengele viwili:

- maagizo (tendo)
- maudhui muhimu (yanayoathiri tendo)

Hapa ni mfano ambapo maagizo ni "fupisha haya kwa sentensi 2".

| Ombi (Ingizo)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Jibu (Matokeo)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Jupiter ni sayari ya tano kutoka Jua na kubwa zaidi katika Mfumo wa Jua. Ni gasi kubwa yenye wingi wa elfu moja wa Jua, lakini mara mbili na nusu ya uzito wa sayari zote nyingine za Mfumo wa Jua kwa pamoja. Jupiter ni moja ya vitu kung'aa vinavyoonekana kwa jicho la kawaida anga la usiku, na imejulikana na ustaarabu wa kale tangu kabla ya historia kuandikwa. Imeitwa kwa jina la mungu wa Warumi Jupiter.[19] Inapoangaliwa kutoka Dunia, Jupiter inaweza kung'aa vya kutosha kwa mwanga wa kuonyesha vivuli vinavyoonekana,[20] na kwa wastani ni kitu cha tatu kung'aa kwa asili angani baada ya Mwezi na Venus. <br/> **Fupisha hii kwa sentensi 2 fupi** | Jupiter, sayari ya tano kutoka Jua, ni kubwa zaidi katika Mfumo wa Jua na inajulikana kwa kuwa moja ya vitu vinavyoangaza zaidi angani usiku. Imetajwa jina la mungu wa Warumi Jupiter, ni gasi kubwa yenye wingi mara mbili na nusu ya uzito wa sayari zingine zote ndani ya Mfumo wa Jua kwa pamoja. |

Sehemu ya mocha muhimu inaweza kutumika kwa njia mbalimbali kuendesha maagizo yenye ufanisi zaidi:

- **Mifano** - badala ya kusema kwa mfano kile cha kufanya kwa maagizo ya moja kwa moja, toa mifano ya kile cha kufanya na uachie mfano aelewe mtindo.
- **Vidokezo** - fuata maagizo na "kidokezo" kinachochochea makamilisho, kinachoelekeza mfano kuelekea majibu yanayostahili zaidi.
- **Violezo** - hizi ni 'mapishi' yanayoweza kurudiwa ya ombi yenye nafasi za kujaza (mabadiliko) yanayoweza kubinafsishwa kwa data kwa matumizi maalum.

Tuchunguze haya katika vitendo.

### Kutumia Mifano

Hii ni njia ambapo unatumia mocha muhimu ku "kulisha mfano" baadhi ya mifano ya matokeo yanayotakiwa kwa maagizo fulani, na kumruhusu aelewe mtindo wa matokeo yanayohitajika. Kulingana na idadi ya mifano iliyotolewa, tunaweza kuwa na ombi la zero-shot, one-shot, few-shot n.k.

Sasa ombi linajumuisha vipengele vitatu:

- Maelezo ya kazi
- Mifano michache ya matokeo yanayotarajiwa
- Mwanzo wa mfano mpya (ambao unakuwa maelezo ya kazi kwa njia isiyo ya moja kwa moja)

| Aina ya Kujifunza | Ombi (Ingizo)                                                                                                                                              | Jibu (Matokeo)         |
| :---------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| Zero-shot         | "The Sun is Shining". Tafsiri kwa Kihispania                                                                                                              | "El Sol está brillando".|
| One-shot          | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                      | "Es un día frío y ventoso". |
| Few-shot          | Mchezaji alikimbia misingi => Baseball <br/> Mchezaji alipiga ace => Tennis <br/> Mchezaji alipiga six => Cricket <br/> Mchezaji alifanya slam-dunk =>          | Basketball             |
|                   |                                                                                                                                                            |                        |

Angalia jinsi tulivyolazimika kutoa maagizo wazi ("Tafsiri kwa Kihispania") katika zero-shot, lakini linajadiliwa katika mfano wa one-shot. Mfano wa few-shot unaonyesha jinsi kuongeza mifano zaidi inavyowezesha mifano kutoa makadirio sahihi zaidi bila maagizo ya ziada.

### Vidokezo vya Ombi

Mbinu nyingine ya kutumia mocha muhimu ni kutoa _vidokezo_ badala ya mifano. Katika kesi hii, tunampa mfano msukumo kwa njia ya _kuanza_ na kipande kinachoonyesha muundo unaotakiwa wa jibu. Kisha mfano "hutumia kidokezo" kuendelea kwa mtindo huo.

| Idadi ya Vidokezo | Ombi (Ingizo)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Jibu (Matokeo)                                                                                                                                                                                                                                                                                       |
| :---------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                 | Jupiter ni sayari ya tano kutoka Jua na kubwa zaidi katika Mfumo wa Jua. Ni gasi kubwa yenye wingi wa elfu moja wa Jua, lakini mara mbili na nusu ya uzito wa sayari zote nyingine za Mfumo wa Jua kwa pamoja. Jupiter ni moja ya vitu kung'aa vinavyoonekana kwa jicho la kawaida anga la usiku, na imejulikana na ustaarabu wa kale tangu kabla ya historia kuandikwa. <br/>**Fupisha Hii**                                                                                                       | Jupiter ni sayari kubwa zaidi katika Mfumo wetu wa Jua na ni ya tano kutoka Jua. Ni gasi kubwa yenye wingi wa 1/1000 wa Jua, lakini ni nzito zaidi kuliko sayari nyingine zote kwa pamoja. Ustaarabu wa kale umefahamu Jupiter kwa muda mrefu na inaonekana kwa urahisi angani usiku.. |
| 1              | Jupiter ni sayari ya tano kutoka Jua na kubwa zaidi katika Mfumo wa Jua. Ni gasi kubwa yenye wingi wa mara elfu moja wa ule wa Jua, lakini mara mbili na nusu ya zile za sayari zingine zote zilizojumuishwa katika Mfumo wa Jua. Jupiter ni moja ya vitu angavu vinavyoonekana kwa jicho tupu usiku, na imekuwa ikijulikana kwa tamaduni za kale tangu kabla ya historia kurushwa. <br/>**Muhtasari Huu** <br/> Tuliojifunza ni kwamba Jupiter | ni sayari ya tano kutoka Jua na kubwa zaidi katika Mfumo wa Jua. Ni gasi kubwa yenye wingi wa mara elfu moja wa ule wa Jua, lakini mara mbili na nusu ya zile za sayari zingine zote zilizojumuishwa. Inaonekana kwa urahisi kwa jicho tupu na imekuwa ikijulikana tangu enzi za kale.                        |
| 2              | Jupiter ni sayari ya tano kutoka Jua na kubwa zaidi katika Mfumo wa Jua. Ni gasi kubwa yenye wingi wa mara elfu moja wa ule wa Jua, lakini mara mbili na nusu ya zile za sayari zingine zote zilizojumuishwa katika Mfumo wa Jua. Jupiter ni moja ya vitu angavu vinavyoonekana kwa jicho tupu usiku, na imekuwa ikijulikana kwa tamaduni za kale tangu kabla ya historia kurushwa. <br/>**Muhtasari Huu** <br/> Ukweli 3 Juu Tuliojifunza:         | 1. Jupiter ni sayari ya tano kutoka Jua na kubwa zaidi katika Mfumo wa Jua. <br/> 2. Ni gasi kubwa yenye wingi wa mara elfu moja wa ule wa Jua...<br/> 3. Jupiter imeonekana kwa jicho tupu tangu nyakati za kale ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompt Templates

Kiolezo cha mfano ni _mapishi yaliyowekwa awali kwa ajili ya prompt_ ambayo inaweza kuhifadhiwa na kutumiwa tena inapohitajika, ili kuendesha uzoefu mzuri zaidi wa mtumiaji kwa wingi. Kwa muundo wake rahisi zaidi, ni mkusanyiko wa mifano ya prompt kama [hii kutoka OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) inayotoa sehemu za mazungumzo (mjumbe wa mtumiaji na mfumo) na muundo wa ombi unaoendeshwa na API - ili kusaidia matumizi tena.

Kwa muundo wake mgumu zaidi kama [mfano huu kutoka LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) una _vibandiko_ ambavyo vinaweza kubadilishwa na data kutoka vyanzo mbalimbali (kama maingizo ya mtumiaji, muktadha wa mfumo, vyanzo vya data vya nje na kadhalika) kuunda prompt kwa njia ya mpangilio. Hii inatuwezesha kuunda maktaba ya prompts za kutumia tena ambazo zinaweza kutumika kuendesha uzoefu mzuri zaidi wa watumiaji **kivilevi** kwa wingi.

Mwisho kabisa, thamani halisi ya violezo iko katika uwezo wa kuunda na kuchapisha _maktaba za prompt_ kwa maeneo maalum ya matumizi - ambapo kiolezo cha prompt sasa kimeboreshwa kuakisi muktadha wa programu au mifano inayofanya majibu kuwa yenye muunganisho na usahihi kwa hadhira lengwa. Rejesho la [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) ni mfano mzuri wa mbinu hii, likikusanya maktaba ya prompts kwa sekta ya elimu kwa kusisitiza malengo muhimu kama kupanga masomo, kubuni mitaala, kufundisha wanafunzi n.k.

## Supporting Content

Ikiwa tunazingatia uundaji wa prompt kuwa na maelekezo (kazi) na lengo (maudhui makuu), basi _maudhui ya ziada_ ni sawa na muktadha wa ziada tunaotoa ili **kuathiri matokeo kwa namna fulani**. Hii inaweza kuwa parameta za kurekebisha, maagizo ya uwasilishaji, orodha za mada n.k. ambazo zinaweza kusaidia mfano _kubadilisha_ jibu lake kuendana na malengo au matarajio ya mtumiaji yanayohitajika.

Kwa mfano: Tukichukua orodha ya kozi yenye meta-data nyingi (jina, maelezo, ngazi, lebo za metadata, mwalimu n.k.) kwa kozi zote za mitaala:

- tunaweza kuweka maelekezo ya "fupisha orodha ya kozi za Msimu wa Kuanguka 2023"
- tunaweza kutumia maudhui makuu kutoa mifano michache ya jibu linalotakiwa
- tunaweza kutumia maudhui ya ziada kutaja lebo 5 kuu za kuvutia.

Sasa, mfano unaweza kutoa muhtasari kwa muundo unaoonyeshwa na mifano michache - lakini ikiwa matokeo yana lebo nyingi, inaweza kipaisho lebo 5 zilizotajwa katika maudhui ya ziada.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #3:
Prompt Engineering Techniques.
What are some basic techniques for prompt engineering?
Illustrate it with some exercises.
-->

## Prompting Best Practices

Sasa tunapojua jinsi prompts zinavyoweza _kujengwa_, tunaweza kuanza kufikiria jinsi ya _kuzikusanya_ zikiakisi mbinu bora. Tunaweza kufikiria hii katika sehemu mbili - kuwa na _mtazamo_ sahihi na kutumia _mbinu_ sahihi.

### Prompt Engineering Mindset

Uhandisi wa prompt ni mchakato wa majaribio na makosa kwa hivyo kumbuka mambo matatu makubwa:

1. **Uelewa wa Eneo ni Muhimu.** Usahihi na umuhimu wa jibu ni kazi ya _eneo_ ambalo programu au mtumiaji unafanya kazi. Tumia hisia zako na utaalamu wa eneo kwa **kurekebisha mbinu** zaidi. Kwa mfano, weka _inhaesa za eneo maalum_ kwenye prompts za mfumo, au tumia _violezo vya eneo maalum_ kwenye prompts za mtumiaji. Toa maudhui ya ziada yanayoakisi muktadha wa kieneo, au tumia _ishara na mifano ya eneo maalum_ kuongozwa mfano kufuata matumizi yanayotambulika.

2. **Uelewa wa Mfano ni Muhimu.** Tunajua mifano ni ya bahati (stochastic) kwa asili. Lakini utekelezaji wa mfano unaweza kubadilika kulingana na seti ya mafunzo inayotumika (maarifa ya awali), uwezo unaotolewa (mfano kupitia API au SDK) na aina ya maudhui ambayo imeboreshwa (mfano, picha, maandishi n.k.). Fahamu nguvu na udhaifu wa mfano unayotumia, na tumia maarifa hayo kutilia mkazo _kipaumbele cha kazi_ au kuunda _violezo vilivyoandaliwa_ vinavyofaa zaidi kwa uwezo wa mfano huo.

3. **Rudia & Thibitisha ni Muhimu.** Mifano inaendelea kuboreshwa haraka, na pia mbinu za uhandisi wa prompt. Kama mtaalamu wa eneo, unaweza kuwa na muktadha mwingine au vigezo _programu yako_ maalum, ambavyo haviwezi kuwa na maana kwa jamii kubwa. Tumia zana na mbinu za uhandisi wa prompt kuanzia hatua ya kwanza, kisha rudia na thibitisha matokeo kwa kutumia hisia na utaalamu wako. Rekodi mawazo yako na tengeneza **maktaba ya maarifa** (mfano, maktaba za prompts) ambayo inaweza kutumika kama msingi mpya kwa wengine, kwa kurudia haraka huku kibonye.

## Best Practices

Hapa tunatazama mbinu bora zinazopendekezwa na wataalamu wa [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) na [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Nini                              | Kwa Nini                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Tathmini mifano mipya.            | Mifano mipya ina uwezekano wa kuwa na vipengele vya kuboresha na ubora - lakini pia inaweza kuleta gharama kubwa zaidi. Iitathmini kwa athari, kisha chukua maamuzi ya kuhamia.                                                                                |
| Tenganisha maelekezo & muktadha   | Angalia kama mfano/mtengenezaji wako anaweka _vitenganishi_ kutambua maelekezo, maudhui makuu na maudhui ya ziada kwa uwazi zaidi. Hii inaweza kusaidia mifano kuweka uzito sahihi kwa maneno.                                                         |
| Kuwa maalum na wazi               | Toa maelezo zaidi kuhusu muktadha unaotaka, matokeo, urefu, muundo, mtindo n.k. Hii itaboresha ubora na ulinganifu wa majibu. Hifadhi mapishi katika violezo vinavyoweza kutumiwa tena.                                                          |
| Kuwa mwelezo, tumia mifano        | Mifano inaweza kusaidia vyema kwa njia ya "onyesha na eleza". Anza na njia ya `zero-shot` ambapo unatoa maelekezo (bila mifano) kisha jaribu `few-shot` kama maboresho, ukitoa mifano michache ya jibu linalotakiwa. Tumia mifano ya mlinganisho. |
| Tumia ishara kuanzisha majibu     | Mshawishi kuelekea matokeo unayotarajia kwa kutoa maneno au misemo ya kuanza ambayo inaweza kuitumika kama msingi wa jibu.                                                                                                               |
| Rudia mara mbili                   | Wakati mwingine unaweza kuhitaji kujirudia kwa mfano. Toa maelekezo kabla na baada ya maudhui yako kuu, tumia maelekezo na ishara, n.k. Rudia & thibitisha kuona kinachofanya kazi.                                                         |
| Mtapeli muhimu                  | Muktatibu wa habari kwa mpangilio wa utoaji unaweza kuathiri jibu, hata katika mifano ya kujifunza, kwa sababu ya upendeleo wa matukio ya hivi karibuni. Jaribu mbadala mbalimbali kuona kinachofanya kazi zaidi.                                                               |
| Mpe mfano “njia ya kutoka”        | Mpe mfano jibu la _zuburuke_ ambalo anaweza kutoa ikiwa hawezi kutimiza kazi kwa sababu yoyote. Hii inaweza kupunguza nafasi za mifano kutoa majibu ya uongo au yaliyozipikiwa.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

Kama ilivyo kwa mbinu yoyote bora, kumbuka kuwa _matokeo yako yanaweza kutofautiana_ kulingana na mfano, kazi na eneo. Tumia haya kama msingi, kisha rudia kuona kinachofanya kazi zaidi kwako. Endelea kutathmini mchakato wako wa uhandisi wa prompt unapopata mifano na zana mpya, ukilenga upanuzi wa mchakato na ubora wa majibu.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Assignment

Hongera! Umefika mwisho wa somo! Ni wakati wa kujaribu baadhi ya dhana na mbinu hizo kwa mifano halisi!

Kwa kazi yetu, tutatumia Jupyter Notebook yenye mazoezi utakayoweza kuimaliza kwa maingiliano. Unaweza pia kuongeza Notibuki na seli zako za Markdown na Code kuchunguza mawazo na mbinu kwa ajili yako binafsi.

### Kuanza, fanya fork ya repo, kisha

- (Inapendekezwa) Anzisha GitHub Codespaces
- (Kwa mbadala) Nakili repo kwenye kifaa chako na kuitumia na Docker Desktop
- (Kwa mbadala) Fungua Notebook kwa mazingira yako ya runtime unaopendelea.

### Kisha, sanidi mazingira yako ya vigezo

- Nakili faili `.env.copy` iliyopo kwenye mzizi wa repo kwenda `.env` na ujaze thamani za `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` na `AZURE_OPENAI_DEPLOYMENT`. Rudi sehemu ya [Learning Sandbox](#sehemu-ya-mazoezi) kujifunza jinsi.

### Kisha, fungua Jupyter Notebook

- Chagua kiini cha runtime. Ikiwa unatumia chaguo 1 au 2, chagua kiini cha Python 3.10.x kinachotolewa na chombo cha maendeleo.

Uko tayari kuendesha mazoezi. Kumbuka hakuna majibu _sahihi au makosa_ hapa - ni tu kuchunguza chaguzi kwa majaribio na makosa na kujenga hisia ya kile kinachofaa kwa mfano na eneo fulani.

_Sababu hii haina sehemu za suluhisho za code kwenye somo hili. Badala yake, Notebook itakuwa na seli za Markdown zenye kichwa "My Solution:" zinazotumia mfano mmoja wa jibu kwa rejeleo._

 <!--
LESSON TEMPLATE:
Wrap the section with a summary and resources for self-guided learning.
-->

## Knowledge check

Ni ipi kati ya zifuatazo ni prompt nzuri ikifuata baadhi ya mbinu bora?

1. Onyesha picha ya gari jekundu  
2. Onyesha picha ya gari jekundu aina Volvo na modeli XC90 likiweka pembeni kwa mto na jua likizama  
3. Onyesha picha ya gari jekundu aina Volvo na modeli XC90

Jibu: 2, ni prompt bora zaidi kwa kuwa hutoa maelezo ya "nini" na kwenda kwenye maelezo maalum (si gari yeyote bali aina na modeli maalum) na pia inaelezea mazingira kwa ujumla. 3 ni bora pili kwa kuwa pia ina maelezo mengi.

## 🚀 Challenge

Tazama kama unaweza kutumia mbinu ya "ishara" na prompt: Malizia sentensi "Onyesha picha ya gari jekundu aina Volvo na ". Jibu linakwambia nini, na ungeboresha vipi?

## Great Work! Continue Your Learning

Unataka kujifunza zaidi kuhusu dhana mbalimbali za Uhandisi wa Prompt? Nenda kwenye [ukurasa wa masomo endelevu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kupata rasilimali zingine nzuri kuhusu mada hii.

Nenda kwenye Somo la 5 ambapo tutaangalia [mbinu za juu zaidi za kuprompt](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->