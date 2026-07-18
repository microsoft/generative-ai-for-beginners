# Misingi ya Uhandisi wa Prompt

[![Misingi ya Uhandisi wa Prompt](../../../translated_images/sw/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Utangulizi
Moduli hii inashughulikia dhana muhimu na mbinu za kuunda prompt zinazofanya kazi vizuri katika mifano ya AI zinazozalisha. Jinsi unavyoandika prompt kwa LLM inashawishi pia. Prompt iliyoandikwa kwa makini inaweza kupata majibu bora zaidi. Lakini kwa hakika maneno kama _prompt_ na _uhandisi wa prompt_ yanamaanisha nini? Na ninawezaje kuboresha _input_ ya prompt ninayotuma kwa LLM? Hivi ndivyo maswali tutayajibu ndani ya sura hii na inayofuata.

_AI zinazozalisha_ zina uwezo wa kuunda maudhui mapya (mfano, maandishi, picha, sauti, nambari, n.k) kama jibu kwa maombi ya mtumiaji. Hii inafanikishwa kwa kutumia _Mifano Mikubwa ya Lugha_ kama mfululizo wa GPT wa OpenAI ("Generative Pre-trained Transformer") ambao wamefunzwa kutumia lugha asilia na nambari.

Watumiaji sasa wanaweza kuwasiliana na mifano hii kwa njia wanazozijua kama mazungumzo, bila ujuzi wa kiufundi au mafunzo yoyote. Mifano hii hutumia _prompt_ - watumiaji hutuma maandishi (prompt) na kurudishiwa jibu la AI (completion). Kisha wanaweza kuendelea kuzungumza na AI, zikavyokuwa mazungumzo yenye mizunguko mingi, wakiboresha prompt hadi jibu lifanikishe matarajio yao.

"Prompts" sasa zinakuwa kiolesura muhimu cha _programu_ kwa programu za AI zinazozalisha, zikimuambia mfano unachotakiwa kufanya na kuathiri ubora wa majibu yanayorejeshwa. "Uhandisi wa Prompt" ni eneo linalokua kwa kasi linalozingatia _kubuni na kuboresha_ prompts ili kutoa majibu thabiti na bora kwa wingi.

## Malengo ya Kujifunza

Katika somo hili, tunajifunza maana ya Uhandisi wa Prompt, kwa nini ni muhimu, na jinsi ya kuunda prompts bora zaidi kwa mfano na lengo fulani la programu. Tutafahamu dhana za msingi na mbinu bora za uhandisi wa prompt - pia tutajifunza kuhusu mazingira ya mazoezi ya Jupyter Notebooks ambapo tunaweza kuona dhana hizi zikitumika kwenye mifano halisi.

Mwishoni mwa somo hili tutakuwa na uwezo wa:

1. Eleza maana ya uhandisi wa prompt na kwa nini ni muhimu.
2. Eleza vipengele vya prompt na jinsi vinavyotumika.
3. Jifunze mbinu bora na mbinu za uhandisi wa prompt.
4. Tumia mbinu zilizojifunza kwenye mifano halisi, ukitumia OpenAI endpoint.

## Maneno Muhimu

Uhandisi wa Prompt: Mazoezi ya kubuni na kuboresha maingizo ya kuongoza mifano ya AI kutoa matokeo yanayohitajika.
Ugawaji wa Tokeni: Mchakato wa kubadilisha maandishi kuwa vitengo vidogo, vinavyoitwa tokeni, ambavyo mfano unaweza kuelewa na kushughulikia.
LLMs Zinazobinafsishwa kwa Maagizo: Mifano Mikubwa ya Lugha (LLMs) ambayo imeboreshwa kwa maagizo maalum ili kuboresha usahihi wa majibu na uhusiano wake.

## Mazoezi ya Kujifunza

Uhandisi wa prompt kwa sasa ni sanaa zaidi kuliko sayansi. Njia bora ya kuboresha utambuzi wetu ni _kufanya mazoezi zaidi_ na kutumia mbinu ya jaribu-na-kosa inayochanganya utaalamu wa eneo la matumizi na mbinu zilizopendekezwa na usahihishaji wa mfano maalum.

Jupyter Notebook inayokuja pamoja na somo hili hutoa mazingira ya _sandbox_ ambapo unaweza kujaribu unachojifunza - wakati wowote au kama sehemu ya changamoto ya msimbo mwishoni. Ili kufanya mazoezi haya, utahitaji:

1. **Ufunguo wa API wa Azure OpenAI** - sehemu ya huduma kwa LLM iliyosambazwa.
2. **Mazingira ya Python Runtime** – ambapo Notebook inaweza kutekelezwa.
3. **Mazingira ya Kanda za Ndani (Local Env Variables)** - _kamili hatua za [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) sasa kujiandaa_.

Notebook inakuja na mazoezi ya _kuanza_ - lakini unahimizwa kuongeza sehemu zako za _Markdown_ (maelezo) na _Code_ (maombi ya prompt) ili kujaribu mifano au mawazo zaidi - na kujenga utambuzi wako wa kubuni prompt.

## Mwongozo Uliopigwa Picha

Unataka kupata muhtasari wa nini somo hili linashughulikia kabla ya kuanza? Tazama mwongozo huu ulio na picha, ambao unakupa hisia ya mada kuu zinazoshughulikiwa na mambo muhimu ya kuzingatia kila moja. Ramani ya somo inakupeleka kutoka kwenye dhana za msingi na changamoto hadi kuzitatua kwa mbinu zinazohusiana na uhandisi wa prompt na mbinu bora. Kumbuka sehemu ya "Mbinu Zinazoendelea" katika mwongozo huu inahusu maudhui yanayoshughulikiwa katika sura _inayofuata_ ya mtaala huu.

![Mwongozo Uliopigwa Picha wa Uhandisi wa Prompt](../../../translated_images/sw/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Kuanza Kwetu

Sasa, tuzungumzie jinsi _mada hii_ inavyohusiana na dhamira yetu ya kuanzisha kampuni inayolenga [kuleta ubunifu wa AI katika elimu](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Tunataka kujenga programu zinazotumia AI kwa ajili ya _kujifunza kubinafsishwa_ - kwa hiyo, fikiria jinsi watumiaji tofauti wa programu yetu wanaweza "kubuni" prompts:

- **Wasimamizi** wanaweza kuomba AI _kuchambua data ya mtaala ili kubaini mapengo ya mafunzo_. AI inaweza kufupisha matokeo au kuyaonyesha kwa kutumia nambari.
- **Walimu** wanaweza kuomba AI _kutengeneza mpango wa somo kwa hadhira na somo fulani_. AI inaweza kuunda mpango huo binafsi kwa muundo ulioainishwa.
- **Wanafunzi** wanaweza kuomba AI _kuwa walimu wao katika somo gumu_. AI sasa inaweza kuwaongoza wanafunzi kwa masomo, vidokezo na mifano inayowiana na kiwango chao.

Hiyo ni mwanzo tu. Tazama [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - maktaba ya prompts yenye chanzo wazi iliyosimamiwa na wazalishaji wa elimu - ili upate hisia pana ya uwezekano! _Jaribu kuendesha baadhi ya prompts hizo kwenye sandbox au kwa kutumia OpenAI Playground kuona kinachotokea!_

<!--
MFUMO WA SOMO:
Kipindi hiki kinapaswa kufunika dhana kuu #1.
Thibitisha dhana kwa mifano na rejeleo.

DHANA #1:
Uhandisi wa Prompt.
Eleza na kueleza kwa nini unahitajika.
-->

## Uhandisi wa Prompt ni Nini?

Tulianza somo hili kwa kufafanua **Uhandisi wa Prompt** kama mchakato wa _kubuni na kuboresha_ maingizo ya maandishi (prompts) ili kutoa majibu thabiti na bora (completions) kwa lengo na mfano fulani wa programu. Tunaweza kufikiria hii kama mchakato wa hatua 2:

- _kubuni_ prompt ya awali kwa mfano na lengo fulani
- _kuboresha_ prompt kwa mizunguko ya mara kwa mara ili kuongeza ubora wa jibu

Hii ni mchakato wa jaribu-na-kosa unaohitaji utambuzi na jitihada za mtumiaji kupata matokeo bora. Kwa hiyo, ni kwa nini ni muhimu? Ili kujibu swali hilo, kwanza tunahitaji kuelewa dhana tatu:

- _Ugawaji wa Tokeni_ = jinsi mfano "unaona" prompt
- _LLMs za Msingi_ = jinsi mfano wa msingi "unasindika" prompt
- _LLMs Zinazobinafsishwa kwa Maagizo_ = jinsi mfano sasa unaweza kuona "mashitaka"

### Ugawaji wa Tokeni

LLM huwaona prompts kama _mlolongo wa tokeni_ ambapo mifano tofauti (au matoleo ya mfano) inaweza kugawa tokeni moja kwa njia tofauti. Kwa kuwa LLM zimefundishwa kwa tokeni (na sio maandishi ya asili), jinsi prompts zinavyogawanywa tokeni inaathiri moja kwa moja ubora wa jibu linalozalishwa.

Ili kupata hisia ya jinsi ugawaji tokeni unavyofanya kazi, jaribu zana kama [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) zilizoonyeshwa hapa chini. Nakili prompt yako - na angalia jinsi inavyobadilishwa kuwa tokeni, ukiangalia jinsi herufi za wazi na alama za ulinganifu zinavyoendeshwa. Kumbuka mfano huu unaonyesha LLM ya zamani (GPT-3) - kwa hiyo kujaribu na mfano mpya kunaweza kutoa matokeo tofauti.

![Ugawaji wa Tokeni](../../../translated_images/sw/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Dhana: Mifano Msingi

Mara prompt inapogawanywa tokeni, kazi kuu ya ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (au mfano wa msingi) ni kutabiri tokeni inayofuata katika mlolongo huo. Kwa kuwa LLM zimefunzwa kwa mamilioni ya maandishi, zinaelewa uhusiano wa takwimu kati ya tokeni na zinaweza kutabiri kwa hakika fulani. Kumbuka kwamba hazielewi _maana_ ya maneno katika prompt au token; zinaona tu mtindo ambao zinaweza "kukamilisha" kwa mtabiri wao unaofuata. Zinaweza kuendelea kutabiri mlolongo hadi zitakaposimamishwa kwa sababu ya mtumiaji au hali iliyowekwa awali.

Unataka kuona jinsi ukamilishaji wa prompt unavyofanya kazi? Weka prompt hapo juu kwenye [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) na mipangilio ya default. Mfumo umeundwa kutambua prompts kama maombi ya taarifa - kwa hiyo utapata jibu linalokidhi muktadha huu.

Lakini je, mtumiaji angependa kuona kitu maalum kinachokidhi masharti au lengo la kazi? Hapa ndipo LLMs zinazoelekezwa kwa maagizo zinapoingia.

![Misingi ya Chat ya Base LLM](../../../translated_images/sw/04-playground-chat-base.65b76fcfde0caa67.webp)

### Dhana: LLM Zinazoelekezwa kwa Maagizo

[LLM Zinazoelekezwa kwa Maagizo](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) huanza na mfano wa msingi na huboreshwa zaidi kwa kutumia mifano au jozi za ingizo/matokeo (mfano, "mijadala" yenye mizunguko mingi) inayoweza kuwa na maagizo wazi - na jibu la AI linajaribu kufuata maagizo hayo.

Hii hutumia mbinu kama Kujifunza Kwa Kukidhi Maoni ya Binadamu (RLHF) inayoweza kufundisha mfano _kufuata maagizo_ na _kujifunza kutokana na maoni_ ili kutoa majibu yanayofaa zaidi kwa matumizi halisi na yanayohusiana zaidi na malengo ya mtumiaji.

Tujaribu - rudi kwenye prompt hapo juu, lakini sasa badilisha _ujumbe wa mfumo_ kutoa maagizo yafuatayo kama muktadha:

> _Fupisha maudhui uliyopewa kwa mwanafunzi wa darasa la pili. Weka matokeo kuwa aya moja yenye pointi 3-5._

Angalia jinsi matokeo sasa yameelekezwa kufuata lengo na muundo ulioombwa? Mwalimu sasa anaweza kutumia jibu hili moja kwa moja kwenye slaidi zao za somo hilo.

![Ujumbe wa Chat ya LLM Zinazoelekezwa kwa Maagizo](../../../translated_images/sw/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Kwa Nini Tunahitaji Uhandisi wa Prompt?

Sasa tunapojua jinsi prompts zinavyosindikwa na LLMs, tuzungumze kuhusu _kwa nini_ tunahitaji uhandisi wa prompt. Jibu liko katika ukweli kwamba LLMs za sasa zinakabiliwa na changamoto kadhaa zinazofanya _ukuaji wa majibu thabiti na ya kuaminika_ kuwa changamoto zaidi bila jitihada za kujenga na kuboresha prompt. Kwa mfano:

1. **Majibu ya mfano ni ya bahati nasibu.** _Prompt hiyo hiyo_ huenda ikazalisha majibu tofauti kwa mifano au matoleo tofauti ya mfano. Pia inaweza kutoa matokeo tofauti kwa _mfano huo huo_ wakati tofauti. _Mbinu za uhandisi wa prompt zinaweza kusaidia kupunguza tofauti hizi kwa kutoa miongozo bora_.

1. **Mifano inaweza kuunda majibu ya uongo.** Mifano imefunzwa kwa seti kubwa lakini _zilizo na mipaka_ ya data, yaani haina ujuzi wa dhana nje ya mazingira hayo ya mafunzo. Kwa hiyo inaweza kuzalisha majibu ambayo sio sahihi, ni hadithi, au yanapingana na ukweli uliopo. _Mbinu za uhandisi wa prompt husaidia watumiaji kubaini na kupunguza uongo huo kwa mfano, kwa kumuomba AI kutoa vyanzo au hoja_.

1. **Uwezo wa mifano utatofautiana.** Mifano mipya au vizazi vipya vitakuwa na uwezo mkubwa zaidi lakini pia vitaleta vipengele na changamoto za gharama na ugumu wa pekee. _Uhandisi wa prompt unatusaidia kuendeleza mbinu bora na mtiririko wa kazi unaoziba tofauti hizi na kuendana na mahitaji maalum ya mfano kwa njia za kupanuka na laini_.

Tuchukulie mfano huu ukitokea moja kwa moja katika OpenAI au Azure OpenAI Playground:

- Tumia prompt ile ile kwenye usambazaji tofauti wa LLM (mfano, OpenAI, Azure OpenAI, Hugging Face) - je, ulikuwaona tofauti hizo?
- Tumia prompt ile ile kwa mfululizo kwenye usambazaji _mmoja_ wa LLM (mfano, Azure OpenAI playground) - tofauti hizi zilikuwa tofauti vipi?

### Mfano wa Uongozi (Fabrications)

Katika kozi hii, tunatumia neno **"uongozi"** kurejelea tukio ambapo LLM mara nyingine huandika taarifa zisizo sahihi kihistoria kutokana na vizuizi vya mafunzo yao au vikwazo vingine. Huenda pia umeisikia ikiitwa _"ndoto za kipengo"_ katika makala maarufu au karatasi za utafiti. Hata hivyo, tunapendekeza kwa nguvu kutumia _"uongozi"_ kama jina ili kuepuka kumtazama mfano haya kama binadamu kwa kuhusisha tabia za kibinadamu kwenye matokeo ya mashine. Hii pia inahimiza [miongozo ya AI ya Kuwajibika](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) kutoka mtazamo wa istilahi, kwa kuondoa maneno ambayo yanaweza kuonekana kama ya kukera au yasiyoeleweka kwa baadhi ya muktadha.

Unataka kuona jinsi uongozi unavyofanya kazi? Fikiria prompt inayomwelekeza AI kuzalisha maudhui kwa mada isiyopo (ili kuhakikisha haipatikani katika data ya mafunzo). Kwa mfano - nilijaribu prompt hii:

> **Prompt:** tengeneza mpango wa somo kuhusu Vita vya Martian vya mwaka 2076.

Utafutaji mtandaoni ulinionyesha kuwa kuna simulizi za kubuni (mfano, mfululizo wa televisheni au vitabu) kuhusu vita vya Martian - lakini siyo mwaka 2076. Maarifa ya kawaida pia huniambia kuwa 2076 ni _baadaye_ na hivyo, haiwezi kuhusishwa na tukio halisi.


Je, basi nini hutokea tunapochukua tahadhari hii na watoa huduma tofauti wa LLM?

> **Jibu 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/sw/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Jibu 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/sw/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Jibu 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/sw/04-fabrication-huggingchat.faf82a0a51278956.webp)

Kama ilivyotarajiwa, kila mfano (au toleo la mfano) hutengeneza majibu kidogo tofauti kutokana na tabia ya randomness na tofauti za uwezo wa mfano. Kwa mfano, mfano mmoja unalenga hadhira ya darasa la 8 wakati mwingine unadhani mwanafunzi wa sekondari. Lakini mifano yote mitatu ilizalisha majibu ambayo yanaweza kumshawishi mtumiaji ambaye hajatambua kuwa tukio hilo halikuwa la kweli.

Mbinu za uhandisi wa tahadhari kama _metaprompting_ na _usanidi wa joto_ zinaweza kupunguza uongo wa mfano hadi kiwango fulani. Miundo mipya ya uhandisi wa tahadhari pia hujumuisha zana na mbinu mpya kwa urahisi ndani ya mtiririko wa tahadhari, ili kupunguza au kudhibiti baadhi ya athari hizi.

## Utafiti wa Kesi: GitHub Copilot

Tuchukue sehemu hii kwa kupata wazo la jinsi uhandisi wa tahadhari unavyotumika katika suluhisho halisi kwa kuangalia Utafiti wa Kesi moja: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot ni "Mshirika wako wa Mwandishi wa AI" - hubadilisha tahadhari ya maandishi kuwa makamilisho ya msimbo na umejumuishwa katika mazingira yako ya maendeleo (mfano, Visual Studio Code) kwa uzoefu rahisi wa mtumiaji. Kama ilivyoelezwa katika mfululizo wa blogu hapa chini, toleo la awali lilitegemea mfano wa OpenAI Codex - wahandisi walitambua haraka haja ya kurekebisha mfano na kuendeleza mbinu bora za uhandisi wa tahadhari, kuboresha ubora wa msimbo. Mnamo Julai, walitangaza [mfano bora zaidi wa AI unaozidi Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) kwa mapendekezo haraka zaidi.

Soma machapisho kwa mpangilio, kufuatilia safari yao ya kujifunza.

- **Mei 2023** | [GitHub Copilot anakuwa Bora katika Kuelewa Msimbo Wako](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mei 2023** | [Ndani ya GitHub: Kufanya kazi na LLMs nyuma ya GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Juni 2023** | [Jinsi ya kuandika tahadhari bora kwa GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Julai 2023** | [.. GitHub Copilot inaenda zaidi ya Codex na mfano bora wa AI](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Julai 2023** | [Mwongozo wa Mwandishi kwa Uhandisi wa Tahadhari na LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Septemba 2023** | [Jinsi ya kujenga app ya LLM kwa kampuni: Mafunzo kutoka GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Pia unaweza kuvinjari [blogu yao ya Uhandisi](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) kwa machapisho mengine kama [haya](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) yanayoonyesha jinsi mifano na mbinu hizi zinavyotumika kwa kuendesha matumizi halisi.

---

<!--
KIASI CHA SOMO:
Sehemu hii inapaswa kufunika dhana kuu #2.
Thibitisha dhana hiyo kwa mifano na rejea.

DHANA #2:
Muundo wa Tahadhari.
Imeonyeshwa kwa mifano.
-->

## Ujenzi wa Tahadhari

Tumeona kwa nini uhandisi wa tahadhari ni muhimu - sasa tuelewe jinsi tahadhari zinavyotengenezwa ili tuweze kutathmini mbinu tofauti kwa muundo wa tahadhari bora zaidi.

### Tahadhari ya Msingi

Tuanze na tahadhari ya msingi: ingizo la maandishi linalotumwa kwa mfano bila muktadha mwingine. Hapa kuna mfano - tunapotuma maneno machache ya mwanzo ya wimbo wa taifa wa Marekani kwa OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) inakamilisha mara moja jibu na mistari michache inayofuata, ikionyesha tabia ya msingi ya utabiri.

| Tahadhari (Ingia) | Makamilisho (Matokeo)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Inaonekana unaanza maneno ya wimbo "The Star-Spangled Banner," wimbo wa taifa wa Marekani. Maneno kamili ni ...                             |

### Tahadhari Ngumu

Sasa tukae muktadha na maelekezo kwa tahadhari ya msingi. [Chat Completion API](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) inatuwezesha kujenga tahadhari ngumu kama mkusanyiko wa _jumbe_ zenye:

- Pairs za ingizo/mahitimisho zinazoakisi ingizo la _mtumiaji_ na jibu la _msaidizi_.
- Ujumbe wa mfumo unaoweka muktadha wa tabia au utu wa msaidizi.

Ombi sasa ni kama ifuatavyo, ambapo _tokenization_ huchukua taarifa muhimu kutoka muktadha na mazungumzo. Sasa, kubadilisha muktadha wa mfumo inaweza kuwa na athari sawa kwenye ubora wa makamilisho, kama vile ingizo la mtumiaji lililotolewa.

```python
response = client.responses.create(
    model="gpt-5-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Tahadhari ya Maelekezo

Katika mifano hapo juu, tahadhari ya mtumiaji ilikuwa swali rahisi la maandishi ambalo linaweza kueleweka kama ombi la habari. Kwa tahadhari za _maelekezo_, tunaweza kutumia maandishi hayo kufafanua kazi kwa undani zaidi, tukitoa mwongozo bora kwa AI. Hapa kuna mfano:

| Tahadhari (Ingia)                                                                                                                                                                                                                         | Makamilisho (Matokeo)                                                                                                        | Aina ya Maelekezo |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Andika maelezo ya Vita vya Kiraia                                                                                                                                                                                                   | _imirudisha aya rahisi_                                                                                              | Rahisi              |
| Andika maelezo ya Vita vya Kiraia. Toa tarehe muhimu na matukio na eleza umuhimu wao                                                                                                                                     | _imirudisha aya ikifuatiwa na orodha ya tarehe za matukio muhimu na maelezo_                                             | Ngumu             |
| Andika maelezo ya Vita vya Kiraia katika aya 1. Toa pointi 3 za risasi na tarehe muhimu na umuhimu wake. Toa pointi 3 zaidi za watu maarufu wa kihistoria na michango yao. Rudisha matokeo kama faili la JSON | _huturudisha maelezo mengi zaidi ndani ya kisanduku cha maandishi, kimepangwa kama JSON ambacho unaweza kunakili-kubandika kwenye faili na kuthibitisha kama inahitajika_ | Ngumu. Imepangwa. |

## Yaliyomo Msingi

Katika mifano hapo juu, tahadhari bado ilikuwa huru, ikiruhusu LLM kuchagua sehemu ya dataset iliyopangwa awali inayofaa. Kwa muundo wa _yaliyomo msingi_, maandishi ya ingizo hugawanywa katika sehemu mbili:

- maelekezo (hatua)
- yaliyomo yanayohusiana (ambayo huathiri hatua)

Hapa kuna mfano ambapo maelekezo ni "fupisha hii kwa sentensi 2".

| Tahadhari (Ingia)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Makamilisho (Matokeo)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter ni sayari ya tano kutoka Jua na kubwa zaidi katika Mfumo wa Jua. Ni kubwa ya gesi yenye kamba ya wingi wa elfu moja wa Jua, lakini mara mbili na nusu ya sayari zote zingine pamoja katika Mfumo wa Jua. Jupiter ni moja ya vitu vinavyoangaza vinavyoonekana kwa macho bila kipodozi angani usiku, na imejulikana na ustaarabu wa kale kabla ya historia kuandikwa. Imejulikana kwa mungu wa Kirumi Jupiter.[19] Tunapoitazama kutoka Dunia, Jupiter inaweza kuangaza vya kutosha taa iliyorejelewa kutoa kivuli kinachoonekana,[20] na kwa wastani ni kitu cha tatu kinachoangaza angani usiku baada ya Mwezi na Venus. <br/> **Fupisha hii kwa sentensi 2 fupi**      | Jupiter, sayari ya tano kutoka Jua, ni kubwa zaidi katika Mfumo wa Jua na inajulikana kwa kuwa moja ya vitu vinavyoangaza kwa macho usiku. Imejulikana kwa mungu wa Kirumi Jupiter, ni kubwa ya gesi yenye wingi mara mbili na nusu ya sayari zingine zote pamoja katika Mfumo wa Jua.    |

Sehemu ya yaliyomo msingi inaweza kutumika kwa njia mbalimbali kuendesha maelekezo bora zaidi:

- **Mifano** - badala ya kumuambia mfano afanye nini kwa maelekezo wazi, mpatie mifano ya kile cha kufanya na uwaachie agundue muundo.
- **Vidokezo** - fuata maelekezo na "kidokezo" kinachoandaa jibu, kuongoza mfano kuelekea majibu zaidi yanayofaa.
- **Violezo** - hizi ni 'mapishi' yanayorudiwa kwa tahadhari zenye nafasi za vigezo (variables) zinazoweza kubinafsishwa kwa data kwa matumizi maalum.

Hebu tuchunguze haya moja kwa moja.

### Kutumia Mifano

Hii ni mbinu ambapo unatumia yaliyomo msingi "kula mfano" baadhi ya mifano ya matokeo yanayotarajiwa kwa maelekezo fulani, na kumruhusu agundue muundo wa matokeo yanayotarajiwa. Kulingana na idadi ya mifano iliyopewa, tunaweza kuwa na tahadhari ya zero-shot, one-shot, few-shot n.k.

Tahadhari sasa ina vipengele vitatu:

- Maelezo ya kazi
- Mifano michache ya matokeo yanayotarajiwa
- Mwanzo wa mfano mpya (ambao unakuwa maelezo ya kazi kwa kimya)

| Aina ya Kujifunza | Tahadhari (Ingia)                                                                                                                                        | Makamilisho (Matokeo)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "The Sun is Shining". Tafsiri kwa Kihispania                                                                                                            | "El Sol está brillando".    |
| One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot      | Mchezaji alikimbia misingi => Baseball <br/> Mchezaji alipiga ace => Tennis <br/> Mchezaji alipiga sita => Cricket <br/> Mchezaji alifanya slam-dunk => | Basketball                  |
|               |                                                                                                                                                       |                             |

Kumbuka jinsi tuliweka maelekezo wazi ("Tafsiri kwa Kihispania") katika zero-shot prompting, lakini huwaumbia maelekezo kwa mfano wa one-shot. Mfano wa few-shot unaonyesha jinsi kuongeza mifano zaidi hufanya mifano kutoa masharti sahihi zaidi bila maelekezo ya ziada.

### Vidokezo vya Tahadhari

Mbinu nyingine ya kutumia yaliyomo msingi ni kutoa _vidokezo_ badala ya mifano. Katika kesi hii, tunamprovidi mfano mshipu kuelekea mwelekeo sahihi kwa _kuanza_ na kipande kinachoakisi mwonekano wa jibu linalotakiwa. Kisha mfano 'huchukua kidokezo' kuendelea kwa mtindo huo.

| Idadi ya Vidokezo | Tahadhari (Ingia)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Makamilisho (Matokeo)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter ni sayari ya tano kutoka Jua na kubwa zaidi katika Mfumo wa Jua. Ni kubwa ya gesi yenye kamba ya wingi wa elfu moja wa Jua, lakini mara mbili na nusu ya sayari zote zingine pamoja katika Mfumo wa Jua. Jupiter ni moja ya vitu vinavyoangaza vinavyoonekana kwa macho bila kipodozi angani usiku, na imejulikana na ustaarabu wa kale kabla ya historia kuandikwa. <br/>**Fupisha Hii**                                       | Jupiter ni sayari kubwa zaidi katika Mfumo wetu wa Jua na ni ya tano kutoka Jua. Ni kubwa ya gesi yenye wingi wa 1/1000 wa Jua, lakini ni nzito kuliko sayari zote zingine pamoja. Wastaarabu wa kale wameijua Jupiter kwa muda mrefu, na inaonekana kwa urahisi angani usiku.. |
| 1              | Jupiter ni sayari ya tano kutoka Jua na kubwa zaidi katika Mfumo wa Jua. Ni kubwa ya gesi yenye kamba ya wingi wa elfu moja wa Jua, lakini mara mbili na nusu ya sayari zote zingine pamoja katika Mfumo wa Jua. Jupiter ni moja ya vitu vinavyoangaza vinavyoonekana kwa macho bila kipodozi angani usiku, na imejulikana na ustaarabu wa kale kabla ya historia kuandikwa. <br/>**Fupisha Hii** <br/> Tulijifunza ni kwamba Jupiter | ni sayari ya tano kutoka Jua na kubwa zaidi katika Mfumo wa Jua. Ni kubwa ya gesi yenye kamba ya wingi wa elfu moja wa Jua, lakini mara mbili na nusu ya sayari zote zingine pamoja. Inaonekana kwa urahisi kwa macho bila kipodozi na imejulikana tangu nyakati za kale.                        |

| 2              | Jupiter ni sayari ya tano kutoka Jua na kubwa zaidi katika Mfumo wa Jua. Ni jitu la gesi lenye umassa wa elfu moja wa Jua, lakini mara mbili na nusu ya umassa wa sayari nyingine zote katika Mfumo wa Jua zikichanganywa. Jupiter ni moja ya vitu angavu vinavyoonekana kwa jicho la kawaida angani usiku, na imetambuliwa na mila za kale tangu kabla ya historia kuandikwa. <br/>**Muhtasari Huu** <br/> Ukweli 3 Bora Tuliojifunza:         | 1. Jupiter ni sayari ya tano kutoka Jua na kubwa zaidi katika Mfumo wa Jua. <br/> 2. Ni jitu la gesi lenye umassa wa elfu moja wa Jua...<br/> 3. Jupiter imekuwa inaonekana kwa jicho la kawaida tangu nyakati za kale ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Violezo vya Mitoaji

Kiolezo cha mitoaji ni _mapishi yaliyotanguliwa kwa mitoaji_ ambayo yanaweza kuhifadhiwa na kutumika tena inapohitajika, ili kuendesha uzoefu wa mtumiaji wenye uthabiti kwa kiwango kikubwa. Katika aina yake rahisi kabisa, ni mkusanyiko tu wa mifano ya mitoaji kama [hii kutoka OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) inayotoa vipengele vya mitoaji ya maingiliano (jumbe za mtumiaji na mfumo) pamoja na muundo wa ombi unaoendeshwa na API - kusaidia matumizi tena.

Katika muundo wake mgumu zaidi kama [mfano huu kutoka LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) huwa na _vibadilishaji_ ambavyo vinaweza kubadilishwa na data kutoka katika vyanzo mbalimbali (ingizo la mtumiaji, muktadha wa mfumo, vyanzo vya data vya nje n.k.) ili kuunda mitoaji kwa njia ya nguvu. Hii inatuwezesha kuunda maktaba ya mitoaji inayoweza kutumika tena inayoweza kuendesha uzoefu wa mtumiaji wenye uthabiti **kiutaratibu** kwa kiwango kikubwa.

Hatimaye, thamani halisi ya violezo iko katika uwezo wa kuunda na kuchapisha _maktaba za mitoaji_ kwa maeneo maalum ya matumizi - ambapo kiolezo cha mitoaji sasa kiko _bora_ kuakisi muktadha wa programu maalum au mifano inayofanya majibu kuwa muhimu na sahihi zaidi kwa hadhira lengwa ya watumiaji. Hifadhidata ya [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) ni mfano mzuri wa njia hii, ikikusanya maktaba ya mitoaji ya eneo la elimu kwa msisitizo kwenye malengo muhimu kama upangaji wa somo, muundo wa mtaala, kufundisha wanafunzi n.k.

## Maudhui ya Kuunga Mkono

Tukifikiria uundaji wa mitoaji kuwa na maelekezo (kazi) na lengwa (maudhui makuu), basi _maudhui ya sekondari_ ni kama muktadha wa ziada tunaotoa ili **kuathiri matokeo kwa njia fulani**. Hii inaweza kuwa vigezo vya kuimarisha, maagizo ya muundo, aina za mada n.k. ambazo zinaweza kusaidia mfano ku_tengeneza_ jibu linalofaa malengo au matarajio ya mtumiaji.

Kwa mfano: Ikiwa tuna katalogi ya kozi yenye metadata nyingi (jina, maelezo, ngazi, lebo za metadata, mwalimu n.k.) juu ya kozi zote zilizopo katika mtaala:

- tunaweza kuainisha maelekezo ya "fupisha katalogi ya kozi kwa Msimu wa Kuanguka 2023"
- tunaweza kutumia maudhui makuu kutoa mifano michache ya jibu linalotakiwa
- tunaweza kutumia maudhui ya sekondari kubainisha lebo 5 kuu zinazovutia.

Sasa, mfano unaweza kutoa muhtasari katika muundo unaoonyeshwa na mifano michache - lakini ikiwa matokeo yana lebo zaidi, inaweza kuipa kipaumbele lebo 5 zilizoainishwa katika maudhui ya sekondari.

---

<!--
VIPENGELEO VYA SOMO:
Kitengo hiki kinapaswa kufundisha dhana msingi #1.
Thibitisha dhana hiyo kwa mifano na marejeleo.

DHANA #3:
Mbinu za Uhandisi wa Mitoaji.
Ni mbinu zipi za msingi za uhandisi wa mitoaji?
Toa mfano kwa mazoezi.
-->

## Mambo Bora ya Kufanya Kwa Mitoaji

Sasa tunajua jinsi mitoaji inavyoweza _kuundwa_, tunaweza kuanza kufikiria jinsi ya _kuibuni_ kuakisi mambo bora. Tunaweza kuifikiria sehemu mbili - kuwa na _mtazamo_ sahihi na kutumia _mbinu sahihi_.

### Mtazamo wa Uhandisi wa Mitoaji

Uhandisi wa mitoaji ni mchakato wa jaribio na kosa kwa hiyo kumbuka mambo matatu ya mwongozo:

1. **Ufahamu wa Eneo ni Muhimu.** Usahihi na umuhimu wa jibu ni kazi ya _eneo_ ambalo programu au mtumiaji hufanya kazi. Tumia hisia zako na ujuzi wa eneo ili **kubadilishe mbinu** zaidi. Kwa mfano, tafsiri _tabia za eneo maalum_ katika mitoaji ya mfumo wako, au tumia _violezo vya eneo maalum_ katika mitoaji ya mtumiaji. Toa maudhui ya sekondari yanayoakisi muktadha maalum wa eneo, au tumia _ishara na mifano ya eneo_ kumwelekeza mfano kuelekea matumizi yanayojulikana.

2. **Ufahamu wa Mfano ni Muhimu.** Tunajua mifano ni ya kutegemea bahati kwa asili. Lakini utekelezaji wa mfano unaweza kutofautiana kulingana na seti ya mafunzo wanayotumia (maarifa yaliyojifunzwa awali), uwezo wanaotoa (mfano kupitia API au SDK) na aina ya maudhui walioyoboreshwa (mfano, msimbo dhidi ya picha dhidi ya maandishi). Fahamu nguvu na mapungufu ya mfano unaotumia, na tumia maarifa hayo ku _ipa kipaumbele kazi_ au kujenga _violezo maalum_ vilivyo bora kwa uwezo wa mfano.

3. **Mzirikano & Uthibitisho ni Muhimu.** Mifano inabadilika kwa kasi, na pia mbinu za uhandisi wa mitoaji. Kama mtaalamu wa eneo, unaweza kuwa na muktadha au vigezo vingine vya _programu yako_ maalum ambavyo haviwezi kutumika kwa jamii kubwa. Tumia zana na mbinu za uhandisi wa mitoaji kuanza "kuunda" mitoaji, kisha rudia na thibitisha matokeo kwa kutumia hisia zako na ujuzi wa eneo. Rekodi maarifa yako na unda **hifadhidata ya maarifa** (mfano, maktaba za mitoaji) ambayo inaweza kutumika kama msingi mpya na wengine, kwa mrapoko wa haraka zaidi siku za usoni.

## Mambo Bora Zaidi

Sasa tuchunguze mambo bora yanayopendekezwa na wataalamu wa [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) na [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Nini                              | Kwa Nini                                                                                                                                                                                                                                          |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Tathmini mifano mipya.            | Vizazi vipya vya mfano vina uwezekano wa kuwa na vipengele bora na ubora - lakini pia vinaweza kuleta gharama kubwa. Tathmini athari, kisha tokea maamuzi ya kuhama.                                                                               |
| Tofautisha maelekezo & muktadha  | Angalia kama mfano/watoa huduma wanatumia _vitu vinavyojitenga_ kutofautisha maelekezo, maudhui makuu na ya sekondari kwa uwazi zaidi. Hii inaweza kusaidia mifano kutenga uzito kwa usahihi zaidi kwa tokeni.                                        |
| Kuwa maalum na wazi               | Toa maelezo zaidi kuhusu muktadha unaotakiwa, matokeo, urefu, muundo, mtindo n.k. Hii itaboresha ubora na uthabiti wa majibu. Hifadhi mapishi katika violezo vinavyoweza kutumika tena.                                                                |
| Kuwa waelezi, tumia mifano        | Mifano inaweza kujibu vyema zaidi kwa njia ya "onyesha na eleza". Anza kwa njia ya `zero-shot` ambapo unampa maelekezo (bila mifano) kisha jaribu `few-shot` kama marekebisho, ukitoa mifano michache ya jibu linalotakiwa. Tumia mifanananisho.         |
| Tumia ishara kuanzisha majibu    | Mposhe ili kuelekea matokeo inayotakiwa kwa kumpa maneno au misemo ya kuanzia ambayo anaweza kutumia kama msingi kwa jibu.                                                                                                                          |
| Rudia Mafanikio                   | Wakati mwingine unaweza kuhitaji kurudia maelekezo kwa mfano. Toa maelekezo kabla na baada ya maudhui makuu, tumia maelekezo na ishara, n.k. Rudia & thibitisha kuona kinachofanya kazi.                                                               |
| Mpangilio Ni Muhimu              | Mpangilio wa jinsi unavyowasilisha taarifa kwa mfano unaweza kuathiri jibu, hata katika mifano ya kujifunza, kutokana na upendeleo wa usasa. Jaribu njia tofauti kuona ni ipi bora zaidi.                                                                |
| Mpe mfano njia ya “kutoka”       | Mpe mfano jibu la _kubakiza_ ambalo anaweza kutoa ikiwa hawezi kukamilisha kazi kwa sababu yoyote. Hii inaweza kupunguza nafasi ya mifano kuzalisha majibu ya uongo au ya kufikirika.                                                                    |
|                                   |                                                                                                                                                                                                                                                   |

Kama katika mazoea bora yote, kumbuka kuwa _matokeo yako yanaweza kutofautiana_ kulingana na mfano, kazi na eneo. Tumia haya kama msingi, na rudia ili upate kinachofaa zaidi kwako. Endelea kutathmini mchakato wako wa uhandisi wa mitoaji kadri mifano na zana mpya zinavyopatikana, ukiweka mkazo kwenye uwezo wa kusambaza na ubora wa majibu.

<!--
VIPENGELEO VYA SOMO:
Kitengo hiki kinapaswa kutoa changamoto ya msimbo ikiwa inafaa

CHANGAMOTO:
Unganisho la Daftari la Jupyter lenye maoni tu ya msimbo katika maelekezo (sehemu za msimbo zipo tupu).

SULUHISHO:
Unganisho la nakala ya Daftari hilo lenye mitoaji imejazwa na kuendeshwa, ikionyesha mfano mmoja wa matokeo.
-->

## Kazi

Hongera! Umefikia mwisho wa somo! Ni wakati wa kuweka baadhi ya dhana na mbinu hizo kwenye mtihani kwa mifano halisi!

Kwa kazi yetu, tutatumia Daftari la Jupyter lenye mazoezi unaweza kuyatimiza kwa maingiliano. Pia unaweza kuongeza Daftari hilo kwa seli zako za Markdown na Msimbo kuchunguza mawazo na mbinu peke yako.

### Kuanzia, chonga nakala ya repo, kisha

- (Inapendekezwa) Anzisha GitHub Codespaces
- (Mbali na hayo) Nakili repo kwenye kifaa chako cha karibu na uitumie na Docker Desktop
- (Mbali na hayo) Fungua Daftari la Jupyter na mazingira ya utumiaji ya Daftari unayopendelea.

### Ifuatayo, sanidi mabadiliko ya mazingira

- Nakili faili `.env.copy` kwenye mzizi wa repo kuwa `.env` na jaza maadili ya `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` na `AZURE_OPENAI_DEPLOYMENT`. Rudi kwenye [sehemu ya Learning Sandbox](#mazoezi-ya-kujifunza) kujifunza jinsi.

### Ifuatayo, fungua Daftari la Jupyter

- Chagua kernel ya utendaji. Ikiwa unatumia njia 1 au 2, chagua kernel ya Python 3.10.x ya chaguo-msingi iliyotolewa na kontena la programu.

Uko tayari kuendesha mazoezi. Kumbuka hakuna majibu ya _sahihi au makosa_ hapa - ni kuchunguza tu chaguo kwa jaribio na kosa na kujenga hisia ya kinachofanya kazi kwa mfano na eneo la matumizi.

_Kwa sababu hii hakuna sehemu za Suluhisho la Msimbo katika somo hili. Badala yake, Daftari litakuwa na seli za Markdown zilizo na kichwa "Suluhisho Langu:" zinazoonyesha mfano mmoja wa matokeo kwa kumbukumbu._

 <!--
VIPENGELEO VYA SOMO:
Mafupisho na rasilimali za kujifunza kwa msaada wa kujiongoza.
-->

## Kagua Maarifa

Ni ipi kati ya mitoaji ifuatayo ni mitoaji bora ikifuata mazoea ya kawaida?

1. Nionyeshe picha ya gari jekundu
2. Nionyeshe picha ya gari jekundu la chapa Volvo na modeli XC90 likipaki karibu na mlonga wakati jua linapotua
3. Nionyeshe picha ya gari jekundu la chapa Volvo na modeli XC90

A: 2, ni kiolezo bora zaidi kwa kuwa kinatoa maelezo ya "nini" na kinaingia kwa undani (siyo gari wowote bali chapa na modeli maalum) na pia kinaelezea muktadha wa eneo hilo. 3 ni nzuri ifuatayo kwa kuwa pia ina maelezo mengi.

## 🚀 Changamoto

Angalia kama unaweza kutumia mbinu ya "ishara" kwa kiolezo: Kamilisha sentensi "Nionyeshe picha ya gari jekundu la chapa Volvo na ". Inajibu nini, na ungeiboresha vipi?

## Kazi Nzuri! Endelea Kujifunza

Ungependa kujifunza zaidi kuhusu dhana tofauti za Uhandisi wa Mitoaji? Nenda kwenye [ukurasa wa kujifunza unaoendelea](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kupata rasilimali zingine bora kuhusu mada hii.

Elekea somo la 5 ambapo tutaangalia [mbinu za juu za mitoaji](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->