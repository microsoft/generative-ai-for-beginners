# Pagrindai apie užklausų inžineriją

[![Pagrindai apie užklausų inžineriją](../../../translated_images/lt/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Įvadas
Šis modulis apima pagrindines sąvokas ir technikas, skirtas veiksmingų užklausų kūrimui generatyviuose DI modeliuose. Svarbu ir tai, kaip parašote užklausą LLM. Kruopščiai parengta užklausa gali suteikti geresnės kokybės atsakymą. Bet ką tiksliai reiškia tokie terminai kaip _užklausa_ ir _užklausų inžinerija_? Ir kaip patobulinti įvestį užklausoje, kurią siunčiu LLM? Šiuos klausimus bandysime atsakyti šiame ir kitame skyriuje.

_Generatyvus DI_ geba kurti naują turinį (pvz., tekstą, vaizdus, garsą, kodą ir kt.) pagal vartotojo užklausas. Tai pasiekiama naudojant _Didelius kalbos modelius_ (LLM), tokius kaip OpenAI GPT („Generatyvus iš anksto apmokytas transformatorius“) serija, kurie yra apmokyti naudoti natūralią kalbą ir kodą.

Vartotojai dabar gali bendrauti su šiais modeliais per pažįstamas paradigmas, pvz., pokalbius, nereikalaudami techninės patirties ar mokymų. Modeliai yra _užklausomis paremti_ – vartotojai siunčia teksto įvestį (užklausą) ir gauna DI atsakymą (užbaigimą). Jie gali „pokalbiai su DI“ pasikartojančiai, daugiamenčiuose pokalbiuose, tobulindami užklausą, kol atsakymas atitinka jų lūkesčius.

„Užklausos“ tampa pagrindine _programavimo sąsaja_ generatyvioms DI programoms, nurodančiomis modeliams, ką daryti, ir įtakojančiomis grąžintų atsakymų kokybę. „Užklausų inžinerija“ yra sparčiai auganti studijų sritis, kuri sutelkia dėmesį į _užklausų kūrimą ir optimizavimą_, siekiant užtikrinti nuoseklius ir kokybiškus atsakymus mastu.

## Mokymosi tikslai

Šioje pamokoje sužinosime, kas yra užklausų inžinerija, kodėl ji svarbi ir kaip galime sukurti efektyvesnes užklausas konkrečiam modeliui ir taikymo tikslui. Suprasime pagrindines sąvokas ir gerąsias užklausų inžinerijos praktikas – taip pat susipažinsime su interaktyvia „Jupyter Notebooks“ „smėlio dėže“, kur galėsime matyti šias sąvokas taikomas realiuose pavyzdžiuose.

Pamokos pabaigoje galėsime:

1. Paaiškinti, kas yra užklausų inžinerija ir kodėl ji svarbi.
2. Apibūdinti užklausos komponentus ir kaip jie naudojami.
3. Išmokti gerąsias praktikas ir technikas užklausų inžinerijoje.
4. Pritaikyti įgytas technikas realiuose pavyzdžiuose, naudojant OpenAI pabaigos tašką.

## Pagrindinės sąvokos

Užklausų inžinerija: Praktika, skirta kuriant ir tobulinant įvestis, kurios nukreipia DI modelius generuoti norimus rezultatus.
Tokenizacija: Procesas, kai tekstas verčiamas į mažesnes dalis, vadinamas tokenais, kuriuos modelis gali suprasti ir apdoroti.
Instrukcijomis optimizuoti LLM: Dideli kalbos modeliai, kurie yra papildomai apmokyti su konkrečiomis instrukcijomis, siekiant pagerinti atsakymo tikslumą ir aktualumą.

## Mokymosi smėlio dėžė

Užklausų inžinerija šiuo metu labiau yra menas nei mokslas. Geriausias būdas pagerinti intuiciją yra _daug praktikuotis_ ir taikyti bandymų ir klaidų metodą, derinant taikymo srities žinias su rekomenduojamomis technikomis ir modelio specifiniais optimizavimais.

Kartu su šia pamoka pateikiamas „Jupyter“ užrašų knygos (_notebook_) failas, kuriame yra _smėlio dėžės_ aplinka, kurioje galite išbandyti tai, ką išmokote – ir mokymosi metu, ir užduočių pabaigoje. Norėdami paleisti pratybas, jums reikės:

1. **Azure OpenAI API rakto** – paslaugos pabaigos taško LLM, kuris jau įdiegtas.
2. **Python vykdymo aplinkos** – kur galėsite paleisti užrašų knygą.
3. **Vietinių aplinkos kintamųjų** – _dabar atlikite [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) veiksmus, kad pasiruoštumėte_.

Užrašų knyga yra su pradinėmis užduotimis, tačiau galite laisvai pridėti savo _Markdown_ (aprašymą) ir _Code_ (užklausų užklausas) sekcijas, kad išbandytumėte daugiau pavyzdžių ar idėjų ir ugdytumėte užklausų kūrimo intuiciją.

## Iliustruotas vadovas

Norite geriau suprasti, ką apima ši pamoka, prieš pradedant? Peržvelkite šį iliustruotą vadovą, kuriame apžvelgiamos pagrindinės temos ir pagrindiniai dalykai, kuriuos verta apgalvoti kiekvienoje temoje. Pamokos kelias veda nuo pagrindinių sąvokų ir iššūkių supratimo iki jų sprendimo taikant atitinkamas užklausų inžinerijos technikas ir gerąsias praktikas. Atkreipkite dėmesį, kad šio vadovo „Išplėstiniai metodai“ skyrius nurodo turinį, apimantį _kitame_ šios mokymo programos skyriuje.

![Iliustruotas vadovas apie užklausų inžineriją](../../../translated_images/lt/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Mūsų startuolis

Dabar pakalbėkime, kaip _ši tema_ susijusi su mūsų startuolio misija [atnešti DI inovacijas į švietimą](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Norime kurti DI paremtas _personalizuoto mokymosi_ programas, tad pagalvokime, kaip skirtingi mūsų programos vartotojai gali „kūrybiškai kurti“ užklausas:

- **Administratoriai** gali paprašyti DI _analizuoti mokymo programos duomenis, kad nustatytų dangų spragas_. DI gali apibendrinti rezultatus arba vizualizuoti juos su kodu.
- **Mokytojai** gali paprašyti DI _sukurti pamokos planą tikslinėje auditorijoje ir tema_. DI gali paruošti personalizuotą planą nurodytu formatu.
- **Mokiniai** gali paprašyti DI _mokyti juos sudėtingoje srityje_. DI gali kryptingai vesti mokinius per pamokas, pateikti užuominų ir pavyzdžių, pritaikytų jų lygiui.

Tai tik ledkalnio viršūnė. Peržiūrėkite [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – atvirojo kodo užklausų biblioteką, kurią kuruoja švietimo ekspertai – kad geriau suprastumėte galimybes! _Išbandykite kai kurias užklausas smėlio dėžėje arba naudodami OpenAI Playground ir pažiūrėkite, kas nutiks!_

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #1:
Prompt Engineering.
Define it and explain why it is needed.
-->

## Kas yra užklausų inžinerija?

Pamoką pradėjome apibrėždami **užklausų inžineriją** kaip procesą, kai _kuriamos ir optimizuojamos_ teksto įvestys (užklausos), siekiant nuoseklios ir kokybiškos atsakymų (užbaigimų) generacijos pagal konkretų taikymo tikslą ir modelį. Galime tai laikyti 2 žingsnių procesu:

- _kuriama_ pradinė užklausa konkrečiam modeliui ir tikslui
- _tobulinama_ užklausa iteratyviai, siekiant pagerinti atsakymo kokybę

Tai privalomai bandymų ir klaidų procesas, reikalaujantis vartotojo intuicijos ir pastangų norint pasiekti optimalių rezultatų. Tai kodėl tai svarbu? Atsakymui pirmiausia reikia suprasti tris sąvokas:

- _Tokenizacija_ = kaip modelis „mato“ užklausą
- _Pagrindiniai LLM_ = kaip pamatinis modelis „apdoroja“ užklausą
- _Instrukcijomis optimizuoti LLM_ = kaip modelis dabar „matyti užduotis“

### Tokenizacija

LLM mato užklausas kaip _seką tokenų_, o skirtingi modeliai (ar modelio versijos) gali tokenizuoti tą pačią užklausą skirtingais būdais. Kadangi LLM yra apmokyti dirbti su tokenais (o ne žaliu tekstu), užklausos tokenizacijos būdas tiesiogiai veikia sugeneruoto atsakymo kokybę.

Norėdami sužinoti, kaip veikia tokenizacija, išbandykite priemones, tokias kaip [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst), parodytą žemiau. Nukopijuokite savo užklausą – ir pažiūrėkite, kaip ji paverčiama tokenais, atkreipdami dėmesį, kaip traktuoja tarpų simbolius ir skyrybos ženklus. Atkreipkite dėmesį, kad šis pavyzdys rodo senesnį LLM (GPT-3) – taigi bandymas su naujesniu modeliu gali duoti kitokį rezultatą.

![Tokenizacija](../../../translated_images/lt/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Sąvoka: Pamatiniai modeliai

Kai užklausa tokenizuota, pagrindinė ["Pagrindinio LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (ar Pamatinio modelio) funkcija yra numatyti tokeną toje sekoje. Kadangi LLM yra apmokyti su milžiniškomis teksto duomenų bazėmis, jie gerai supranta statistinius ryšius tarp tokenų ir gali tą numatymą atlikti su tam tikru pasitikėjimu. Atkreipkite dėmesį, jie nesupranta _žodžių reikšmės_ užklausoje ar tokene; jie tiesiog mato modelį, kurį gali „užbaigti“ kitos prognozės reikšme. Jie gali tęsti sekos numatymą tol, kol tai bus nutraukta vartotojo ar kai kuriais iš anksto nustatytais kriterijais.

Norite pamatyti, kaip veikia užklausomis paremta užbaigimas? Įklijuokite aukščiau pateiktą užklausą į Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) su numatytais nustatymais. Sistema sukonfigūruota traktuoti užklausas kaip informacijos prašymus – tad turėtumėte pamatyti atsakymą, atitinkantį šį kontekstą.

Bet kas, jei vartotojas norėtų pamatyti ką nors konkretaus, atitinkančio tam tikrus kriterijus ar užduoties tikslą? Štai kur ateina _instrukcijomis optimizuoti_ LLM.

![Pagrindinio LLM pokalbio užbaigimas](../../../translated_images/lt/04-playground-chat-base.65b76fcfde0caa67.webp)

### Sąvoka: Instrukcijomis optimizuoti LLM

[Instrukcijomis optimizuotas LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) pradeda nuo pamatinio modelio ir papildomai jį apmokina su pavyzdžiais ar įėjimo/išėjimo poromis (pvz., daugiamenčiais „pranešimais“), kurie gali turėti aiškias instrukcijas, o DI atsakymas stengiasi laikytis tų nurodymų.

Tai naudoja technikas, tokias kaip žmogaus grįžtamojo ryšio sustiprinto mokymosi (RLHF), kurios leidžia modelį apmokyti _laikyti instrukcijas_ ir _mokytis iš grįžtamojo ryšio_, kad jis generuotų atsakymus, labiau tinkamus praktiniams taikymams ir aktualius vartotojų tikslams.

Išbandykime – grįžkite prie aukščiau pateiktos užklausos, bet dabar pakeiskite _sistemos pranešimą_ taip, kad jis duotų šią užduotį kaip kontekstą:

> _Apibendrinkite pateiktą turinį antro klasės mokiniui. Rezultatas turi būti vienas paragrafas su 3-5 pagrindiniais punktais._

Matote, kaip rezultatas dabar pritaikytas norimam tikslui ir formatui? Mokytojas gali tiesiogiai naudoti šį atsakymą savo pamokų skaidrėse.

![Instrukcijomis optimizuoto LLM pokalbio užbaigimas](../../../translated_images/lt/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Kodėl mums reikalinga užklausų inžinerija?

Dabar, kai žinome, kaip LLM apdoroja užklausas, pakalbėkime apie tai, _kodėl_ mums reikalinga užklausų inžinerija. Atsakymas slypi tame, kad dabartiniai LLM kelia nemažai iššūkių, dėl kurių sunkiau pasiekti _patikimus ir nuoseklius atsakymus_ be pastangų statant ir optimizuojant užklausą. Pavyzdžiui:

1. **Modelių atsakymai yra stokastiniai.** _Ta pati užklausa_ greičiausiai duos skirtingus atsakymus su skirtingais modeliais ar modelio versijomis. Ir netgi gali duoti skirtingus rezultatus su _tuo pačiu modeliu_ skirtingu metu. _Užklausų inžinerijos technikos gali padėti sumažinti šiuos svyravimus, suteikdamos geresnius apsaugos mechanizmus_.

1. **Modeliai gali išgalvoti atsakymus.** Modeliai yra iš anksto apmokyti su _didelėmis, bet ribotomis_ duomenų rinkiniais, todėl jiems trūksta žinių apie užmokymo ribas viršijančias sąvokas. Todėl jie gali generuoti netikslius, išgalvotus ar tiesiogiai prieštaraujančius žinomoms tiesoms atsakymus. _Užklausų inžinerijos technikos padeda identifikuoti ir mažinti tokius išgalvojimus, pvz., klausiant DI pateikti šaltinius ar argumentaciją_.

1. **Modelių gebėjimai skirsis.** Naujesni modeliai ar jų kartos turės daugiau galimybių, tačiau taip pat turės unikalių ypatybių ir kompromisų kainos bei sudėtingumo atžvilgiu. _Užklausų inžinerija padeda sukurti gerąsias praktikas ir darbo eigas, kurios abstraktina skirtumus ir pritaiko modelių specifinius reikalavimus mastu ir sklandžiai_.

Pamatykime tai praktikoje OpenAI arba Azure OpenAI Playground:

- Išbandykite tą pačią užklausą su skirtingomis LLM diegimo vietomis (pvz., OpenAI, Azure OpenAI, Hugging Face) – ar pastebėjote skirtumus?
- Naudokite tą pačią užklausą keletą kartų su _tokia pačia_ LLM diegimo vieta (pvz., Azure OpenAI playground) – kaip skyrėsi rezultatai?

### Išgalvojimų pavyzdys

Šiame kurse naudojame terminą **„išgalvojimas“** (fabrication) reiškiančią reiškinį, kai LLM kartais generuoja neteisingą faktinę informaciją dėl savo apmokymo apribojimų ar kitų veiksnių. Galbūt esate girdėję apie tai, kaip apie _„haliucinacijas“_ populiariuose straipsniuose ar tyrimuose. Tačiau mes tvirtai rekomenduojame vartoti _„išgalvojimas“_, kad nenatūraliai neatrištume į žmogaus bruožus mašinoje vykdomam procesui. Tai taip pat atitinka [Atsakingo DI gaires](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) ir pašalina terminus, kurie kai kuriose situacijose gali būti laikomi įžeidžiančiais ar neįtraukiantys.

Norite suprasti, kaip veikia išgalvojimai? Pagalvokite apie užklausą, kuri nurodo DI generuoti turinį neegzistuojančia tema (kad įsitikintumėte, jog ją rasti mokymo duomenyse neįmanoma). Pavyzdžiui – aš išbandžiau tokią užklausą:

> **Užklausa:** sukurkite pamokos planą apie Marsiečių karą 2076 metais.
Internetinė paieška parodė, kad buvo menamų atsiskaitymų (pvz., televizijos serialai ar knygos) apie marsietiškus karus – bet ne 2076 metais. Sveikas protas taip pat sako, kad 2076 yra _ateitis_, todėl negali būti susijęs su tikru įvykiu.

Tai kas nutinka, kai paleidžiame šį užklausą su skirtingais LLM paslaugų teikėjais?

> **Atsakymas 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/lt/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Atsakymas 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/lt/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Atsakymas 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/lt/04-fabrication-huggingchat.faf82a0a51278956.webp)

Kaip ir buvo galima tikėtis, kiekvienas modelis (ar modelio versija) generuoja šiek tiek skirtingus atsakymus dėl atsitiktinių elgsenų ir modelio galimybių skirtumų. Pavyzdžiui, vienas modelis orientuojasi į 8 klasės auditoriją, o kitas daro prielaidą, kad tai yra vidurinės mokyklos mokinys. Tačiau visi trys modeliai sugeneravo atsakymus, kurie galėtų įtikinti neinformuotą vartotoją, jog šis įvykis yra tikras.

Užklausų konstravimo technikos, tokios kaip _metaprompting_ ir _temperatūros konfigūravimas_, gali tam tikru mastu sumažinti modelio išgalvotas atsakymų generacijas. Naujos užklausų konstravimo _architektūros_ taip pat sklandžiai integruoja naujus įrankius ir technikas į užklausų srautą, siekdamos sušvelninti arba sumažinti kai kurias iš šių pasekmių.

## Atvejo studija: GitHub Copilot

Apibendrinkime šią dalį pažvelgdami, kaip užklausų konstravimas naudojamas realiuose sprendimuose, analizuojant vieną atvejo studiją: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot yra jūsų „dirbtinio intelekto porinis programuotojas“ – jis paverčia tekstines užklausas į kodo užbaigimus ir yra integruotas į jūsų vystymo aplinką (pvz., Visual Studio Code) tam, kad naudotojo patirtis būtų sklandi. Kaip aprašyta žemiau pateiktoje tinklaraščių serijoje, ankstyviausia versija buvo pagrįsta OpenAI Codex modeliu – inžinieriai greitai suprato, kad reikia tobulinti modelį ir kurti geresnes užklausų konstravimo technikas, siekiant pagerinti kodo kokybę. Liepos mėn. jie [pristatė patobulintą DI modelį, kuris pranoksta Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) ir siūlo dar greitesnius pasiūlymus.

Skaitykite įrašus iš eilės, kad sektumėte jų mokymosi kelią.

- **2023 m. gegužė** | [GitHub Copilot gerėja suprasdamas jūsų kodą](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **2023 m. gegužė** | [GitHub viduje: Darbas su LLM už GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **2023 m. birželis** | [Kaip rašyti geresnes užklausas GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **2023 m. liepa** | [.. GitHub Copilot pranoksta Codex su patobulintu DI modeliu](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **2023 m. liepa** | [Programuotojo vadovas užklausų konstravimui ir LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **2023 m. rugsėjis** | [Kaip sukurti įmonės LLM programėlę: Pamokos iš GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Taip pat galite peržiūrėti jų [Inžinerijos tinklaraštį](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) dėl daugiau straipsnių kaip [šis](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), kuris rodo, kaip šie modeliai ir technikos yra _pritaikomos_ realių programų kūrimui.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #2.
Reinforce the concept with examples and references.

CONCEPT #2:
Prompt Design.
Illustrated with examples.
-->

## Užklausos konstravimas

Matėme, kodėl užklausų konstravimas yra svarbus – dabar supraskime, kaip užklausos yra _kuriamos_, kad galėtume įvertinti skirtingas technikas efektyvesniam užklausų dizainui.

### Pagrindinė užklausa

Pradėkime nuo pagrindinės užklausos: tekstinio įvesties, siunčiamos modeliui be jokio papildomo konteksto. Štai pavyzdys – kai siunčiame keletą pirmųjų JAV nacionalinės giesmės žodžių į OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), jis iš karto _papildo_ atsakymą sekamomis eilutėmis, iliustruodamas pagrindinį prognozavimo elgesį.

| Užklausa (Įvestis)  | Užbaigimas (Išvestis)                                                                                                                      |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Atrodo, kad pradedate dainuoti „The Star-Spangled Banner“ – Jungtinių Amerikos Valstijų nacionalinę giesmę. Visa tekstą sudaro ...           |

### Sudėtinga užklausa

Dabar pridėkime kontekstą ir nurodymus prie šios pagrindinės užklausos. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) leidžia sudaryti sudėtingą užklausą kaip kolekciją _pranešimų_, turinčių:

- Įvesties / išvesties poras, atspindinčias _vartotojo_ įvestį ir _asistento_ atsaką.
- Sistemos pranešimą, nustatantį asistentui kontekstą arba elgesio / asmenybės gaires.

Užklausa dabar yra tokia, kur _tokenizacija_ efektyviai fiksuoja aktualią informaciją iš konteksto ir pokalbio. Keitimas sistemos kontekste gali būti toks pat svarbus užbaigimų kokybei kaip ir vartotojo pateikti įvestys.

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

### Instrukcinė užklausa

Aukščiau pateiktuose pavyzdžiuose vartotojo užklausa buvo paprasta teksto užklausa, kurią galima interpretuoti kaip informacijos užklausimą. Su _instrukcinėmis_ užklausomis galime naudoti tą tekstą tam, kad detalizuotume užduotį ir suteiktume DI geresnes gairias. Štai pavyzdys:

| Užklausa (Įvestis)                                                                                                                                                                                                                         | Užbaigimas (Išvestis)                                                                                                      | Instrukcijos tipas |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------- | :----------------- |
| Parašyk aprašymą apie Pilietinį karą                                                                                                                                                                                                   | _grąžino paprastą paragrafą_                                                                                                | Paprasta           |
| Parašyk aprašymą apie Pilietinį karą. Pateik pagrindines datas ir įvykius bei aprašyk jų reikšmę                                                                                                                                         | _grąžino paragrafą, po kurio seka svarbių įvykių datų su aprašymais sąrašas_                                                 | Sudėtinga          |
| Parašyk aprašymą apie Pilietinį karą 1 pastraipoje. Pateik 3 punktus su pagrindinėmis datomis ir jų reikšme. Pateik dar 3 punktus su svarbiais istoriniais asmenimis ir jų indėliu. Grąžink išvestį JSON faile | _grąžina išsamesnę informaciją teksto lange, suformatuotą JSON, kurią galima nukopijuoti ir, jei reikia, patikrinti_          | Sudėtinga. Formatuota.|

## Pagrindinis turinys

Aukščiau pateiktuose pavyzdžiuose užklausa vis dar buvo gana atvira, leidžianti LLM nuspręsti, kuri duomenų iš anksto apmokyto rinkinio dalis yra aktuali. Naudojant _pagrindinio turinio_ dizaino šabloną, įvesties tekstas padalijamas į dvi dalis:

- instrukcija (veiksmas)
- aktualus turinys (veiksmo įtakojimui)

Štai pavyzdys, kur instrukcija yra „apibendrinti šį tekstą 2 sakiniais“.

| Užklausa (Įvestis)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Užbaigimas (Išvestis)                                                                                                                                                                                                                                                                                     |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiteris yra penktoji planeta nuo Saulės ir didžiausia Saulės sistemoje. Tai dujų milžinas, kurio masė yra tūkstantąji Saulės masės dalis, tačiau dvigubai daugiau nei visų kitų Saulės sistemos planetų masių suma. Jupiteris yra vienas iš ryškiausių objektų, matomų plika akimi naktiniame danguje, ir jis buvo žinomas senosioms civilizacijoms dar prieš rašytinę istoriją. Jis pavadintas Romos dievo Jupiterio vardu.[19] Žiūrint iš Žemės, Jupiteris gali būti pakankamai ryškus, kad jo atspindėta šviesa sukeltų matomas šešėlius,[20] ir yra vidutiniškai trečias ryškiausias natūralus objektas naktiniame danguje po Mėnulio ir Veneros. <br/> **Apibendrink tai 2 trumpais sakiniais** | Jupiteris, penktoji planeta nuo Saulės, yra didžiausia Saulės sistemoje ir žinomas kaip vienas iš ryškiausių objektų naktiniame danguje. Jis pavadintas Romos dievo Jupiterio vardu, yra dujų milžinas, kurio masė yra dvigubai didesnė už visų kitų planetų Saulės sistemoje kartu sudėjus. |

Pagrindinio turinio segmentas gali būti naudojamas įvairiais būdais, siekiant geriau valdyti instrukcijas:

- **Pavyzdžiai** – vietoj to, kad aiškiai nurodytume modeliui, ką daryti, pateikite pavyzdžius ir leiskite jam nuspėti modelį.
- **Signalai** – po instrukcijos pridėkite „signalą“, kuris nudažytų atsakymą, nukreipdamas modelį į aktualius atsakymus.
- **Šablonai** – tai pakartojami užklausų „receptai“ su vietomis (kintamaisiais), kuriuos galima pritaikyti konkretiems atvejams su duomenimis.

Pažiūrėkime, kaip šie metodai veikia praktiškai.

### Pavyzdžių naudojimas

Tai metodas, kai naudojate pagrindinį turinį, kad „pamaitintumėte modelį“ pavyzdžiais norimo rezultato tam tikrai užduočiai, ir leistumėte modeliui nuspėti, koks modelis yra galima išvestis. Priklausomai nuo pateiktų pavyzdžių skaičiaus, turime zero-shot, one-shot, few-shot promptinimą ir kt.

Užklausa dabar susideda iš trijų komponentų:

- Užduoties aprašymo
- Kelių norimo rezultato pavyzdžių
- Naujo pavyzdžio pradžios (kuri tampa netiesioginiu užduoties aprašymu)

| Mokymosi tipas | Užklausa (Įvestis)                                                                                                     | Užbaigimas (Išvestis)       |
| :------------- | :--------------------------------------------------------------------------------------------------------------------- | :--------------------------- |
| Zero-shot      | „The Sun is Shining“. Išverskite į ispanų kalbą                                                                      | „El Sol está brillando“.     |
| One-shot       | „The Sun is Shining“ => „El Sol está brillando“. <br> „It's a Cold and Windy Day“ =>                                   | „Es un día frío y ventoso“.  |
| Few-shot       | Žaidėjas bėgo per bazes => Beisbolas <br/> Žaidėjas pataikė „ace“ => Tenisas <br/> Žaidėjas pataikė „šešis“ => Kriketas <br/> Žaidėjas įkrovė „slam-dunk“ => Krepšinis | Krepšinis                   |
|                |                                                                                                                        |                             |

Pastebėkite, kad pradiniame zero-shot pavyzdyje turėjome aiškiai nurodyti („Išverskite į ispanų kalbą“), o one-shot pavyzdyje tai jau modelis galėjo nuspėti. Few-shot pavyzdys parodo, kaip pridėjus daugiau pavyzdžių, modeliai gali tikslingiau interpretuoti rezultatą be papildomų nurodymų.

### Signalų naudojimas užklausoje

Kita pagrindinio turinio naudojimo technika yra suteikti _signalus_ vietoje pavyzdžių. Šiuo atveju, mes modelį šiek tiek „pastumiame“ teisinga kryptimi, pradėdami nuo ištraukos, kuri atspindi norimą atsakymo formatą. Modelis tuomet „pamato signalą“ ir tęsia atsako rašymą ta linkme.

| Signalų kiekis | Užklausa (Įvestis)                                                                                                                                                                                                                                                                                                                                                                                                         | Užbaigimas (Išvestis)                                                                                                                                                                                                                                                                                     |
| :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiteris yra penktoji planeta nuo Saulės ir didžiausia Saulės sistemoje. Tai dujų milžinas, kurio masė yra tūkstantąji Saulės masės dalis, tačiau dvigubai daugiau nei visų kitų kitų Saulės sistemos planetų suma. Jupiteris yra vienas iš ryškiausių objektų, matomų plika akimi naktiniame danguje, ir jis buvo žinomas senojoms civilizacijoms dar prieš rašytinę istoriją. <br/>**Apibendrink tai**                                      | Jupiteris yra didžiausia planeta Saulės sistemoje ir penktoji pagal nutylėjimą nuo Saulės. Tai dujų milžinas, kurio masė sudaro 1/1000 Saulės masės, tačiau didesnė nei visų kitų planetų suma. Senovės civilizacijos gerai žinojo apie Jupiterį, ir jis lengvai matomas naktiniame danguje.  |
| 1              | Jupiteris yra penktoji planeta nuo Saulės ir didžiausia Saulės sistemoje. Tai dujų milžinas, kurio masė yra tūkstantoji Saulės masės dalis, tačiau dvigubai per pusę didesnė už visų kitų Saulės sistemos planetų masę kartu sudėjus. Jupiteris yra viena iš ryškiausių plika akimi matomų naktinio dangaus objektų ir žinomas senovės civilizacijoms dar prieš rašytinę istoriją. <br/>**Apibendrinkite tai** <br/> Ką sužinojome, tai kad Jupiteris | yra penktoji planeta nuo Saulės ir didžiausia Saulės sistemoje. Tai dujų milžinas, kurio masė yra tūkstantoji Saulės masės dalis, tačiau dvigubai per pusę didesnė už visų kitų planetų kartu sudėjus. Jį lengva matyti plika akimi ir jis žinomas nuo senovės laikų.                        |
| 2              | Jupiteris yra penktoji planeta nuo Saulės ir didžiausia Saulės sistemoje. Tai dujų milžinas, kurio masė yra tūkstantoji Saulės masės dalis, tačiau dvigubai per pusę didesnė už visų kitų Saulės sistemos planetų masę kartu sudėjus. Jupiteris yra viena iš ryškiausių plika akimi matomų naktinio dangaus objektų ir žinomas senovės civilizacijoms dar prieš rašytinę istoriją. <br/>**Apibendrinkite tai** <br/> 3 svarbiausios sužinotos faktai:         | 1. Jupiteris yra penktoji planeta nuo Saulės ir didžiausia Saulės sistemoje. <br/> 2. Tai dujų milžinas, kurio masė yra tūkstantoji Saulės...<br/> 3. Jupiteris nuo senovės laikų buvo matomas plika akimi ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Užklausų šablonai

Užklausų šablonas yra _iš anksto apibrėžtas užklausos receptas_, kurį galima saugoti ir pagal poreikį pakartotinai naudoti, siekiant užtikrinti nuoseklesnę vartotojų patirtį dideliu mastu. Paprasčiausia forma tai yra užklausų pavyzdžių rinkinys, toks kaip [šis iš OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst), kuris apima tiek interaktyvių užklausų komponentus (vartotojo ir sistemos žinutes), tiek API valdomos užklausos formatą - kad būtų lengviau pakartotinai naudoti.

Sudėtingesnėje formoje, kaip [šis pavyzdys iš LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), jis turi _vietas_ (pažymėtas kaip placeholders), kurias galima pakeisti duomenimis iš įvairių šaltinių (vartotojo įvesties, sistemos konteksto, išorinių duomenų šaltinių ir t.t.) automatiškai generuojant užklausą. Tai leidžia sukurti biblioteką pakartotinai naudojamų užklausų, kurios padeda nuosekliai ir **automatizuotai** valdyti vartotojų patirtį dideliu mastu.

Galiausiai, tikroji šablonų vertė yra galimybė kurti ir publikuoti _užklausų bibliotekas_ vertikalioms taikomosioms sritims - kur užklausos šablonai yra _optimizuoti_ atsižvelgiant į specifinį taikymo kontekstą arba pavyzdžius, dėl ko atsakymai tampa tikslesni ir labiau aktualūs tiksliniams vartotojams. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) saugykla yra puikus šios strategijos pavyzdys, kur yra kuruojama užklausų biblioteka švietimo sričiai, su pabrėžtinu dėmesiu svarbiausiems tikslams, kaip pamokų planavimas, mokymo programų kūrimas, mokinių konsultavimas ir pan.

## Papildomas turinys

Jei manome, kad užklausos konstrukcija susideda iš nurodymo (užduoties) ir tikslo (pagrindinio turinio), tuomet _antrinis turinys_ yra kaip papildomas kontekstas, kurį suteikiame, kad **dalytiškai įtakotume išvestį**. Tai gali būti parametrai, formatavimo instrukcijos, teminės taksonomijos ir pan., padedančios modeliui _pritaikyti_ atsakymą taip, kad jis atitiktų norimus vartotojų tikslus ar lūkesčius.

Pvz.: Turint kursų katalogą su plačia metainformacija (pavadinimas, aprašymas, lygis, metaduomenų žymės, dėstytojas ir kt.) visiems galimiems kursams mokymo programoje:

- galime apibrėžti užduotį "apibendrinti rudens 2023 kursų katalogą"
- galime naudoti pagrindinį turinį norimo atsakymo pavyzdžiams pateikti
- galime naudoti antrinį turinį, kad identifikuotume 5 svarbiausias "žymes"

Dabar modelis gali pateikti apibendrinimą pagal parodytus pavyzdžius - bet jei rezultatui priskirta daug žymių, jis prioritetuos antriniame turinyje nurodytas 5 žymes.

---

<!--
PAMOKOS ŠABLONAS:
Ši pamoka turėtų apimti pagrindinę koncepciją nr. 1.
Patvirtinkite koncepciją pavyzdžiais ir nuorodomis.

KONCEPCIJA NR.3:
Užklausų kūrimo technikos.
Kokios yra pagrindinės užklausų kūrimo technikos?
Iliustruokite jas pratimais.
-->

## Užklausų geriausios praktikos

Dabar, kai žinome, kaip užklausos gali būti _kuriamos_, galime pradėti mąstyti, kaip jas _sukurti_ atsižvelgiant į geriausias praktikas. Tai galime analizuoti dviem aspektais – turint tinkamą _mąstyseną_ ir taikant tinkamas _technikas_.

### Užklausų kūrimo mąstysena

Užklausų kūrimas yra bandymų ir klaidų procesas, tad verta atsiminti tris svarbius vadovaujančius principus:

1. **Domenu pagrįstas supratimas yra svarbus.** Atsakymų tikslumas ir aktualumas priklauso nuo _domeno_, kuriame taikoma programa ar veikia vartotojas. Taikykite savo intuiciją ir domeno žinias, kad **tobulintumėte technikas**. Pvz., apibrėžkite _domenui specifines charakteristikas_ savo sistemos užklausose arba naudokite _domeno specifinius šablonus_ vartotojo užklausoms. Pateikite antrinį turinį, atspindintį domeno kontekstą, arba naudokite _domeno specifines užuominas ir pavyzdžius_, kad nukreiptumėte modelį pažįstamų naudojimo modelių link.

2. **Modelio supratimas yra svarbus.** Žinome, kad modeliai pagal savo pobūdį yra stochastiniai. Tačiau jų įgyvendinimas gali skirtis naudojant skirtingus mokymo duomenų rinkinius (iš anksto išmoktas žinias), teikiamas funkcijas (pvz., per API ar SDK) ir optimizuojamas turinio tipus (pvz., kodą, vaizdus ar tekstą). Supraskite naudojamo modelio stipriąsias ir silpnąsias puses ir naudokite šias žinias užduotims prioritetizuoti arba specialiai optimizuotiems šablonams kurti pagal modelio galimybes.

3. **Iteracija ir patikrinimas yra svarbu.** Modeliai greitai tobulėja, kaip ir užklausų kūrimo technikos. Kaip domeno ekspertas, turite savo specifinį kontekstą ar kriterijus, kurie gali būti būdingi būtent jūsų taikymui, bet ne visai bendruomenei. Naudokite užklausų kūrimo įrankius ir technikas, kad „paleistumėte“ užklausos kūrimą, tuomet iteruokite ir tikrinkite rezultatus naudodami savo intuiciją ir domeno ekspertizę. Fiksuokite savo įžvalgas ir kurkite **žinių bazę** (pvz., užklausų bibliotekas), kuri gali tapti nauju etalonu kitiems, kad ateityje būtų galima greičiau tobulinti.

## Geriausios praktikos

Dabar pažvelkime į dažniausiai rekomenduojamas geriausias praktikas, kurias siūlo [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) ir [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) specialistai.

| Kas                              | Kodėl                                                                                                                                                                                                                                               |
| :------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Įvertinkite naujausius modelius. | Naujos modelių kartos greičiausiai turi patobulintų funkcijų ir geresnės kokybės – bet gali būti brangesnės. Įvertinkite poveikį ir priimkite migracijos sprendimus.                                                                                 |
| Atskirkite nurodymus ir kontekstą | Pasitikrinkite, ar jūsų modelis / tiekėjas siūlo _žymeklius_, skirtus aiškiau atskirti nurodymus, pagrindinį ir antrinį turinį. Tai padės modeliams tiksliau sverti žodžius (tokenus).                                                                 |
| Būkite konkretūs ir aiškūs       | Duokite daugiau detalių apie norimą kontekstą, rezultatą, ilgį, formatą, stilių ir pan. Tai pagerins atsakymų kokybę ir nuoseklumą. Užrašykite receptus pakartotinai naudojamuose šablonuose.                                                        |
| Būkite aprašomieji, naudokite pavyzdžius | Modeliai gali geriau reaguoti į „rodyk ir pasakyk“ metodą. Pradėkite nuo `nulinio šūvio` (zero-shot) metodo, kai pateikiate nurodymą (bet be pavyzdžių), tuomet pagerinkite naudodami `keletą pavyzdžių` (few-shot), pateikdami kelis norimus atsakymus. Naudokite analogijas. |
| Naudokite užuominas, kad pradėtumėte | Skatinkite modelį siekti pageidaujamo rezultato pateikdami kai kuriuos pradžios žodžius ar frazes, kurias jis panaudos kaip atsakymo pradžią.                                                                                                         |
| Kartokite, jei reikia             | Kartais reikia pakartoti instrukcijas modeliui. Duokite nurodymus prieš ir po pagrindinio turinio, naudokite tiek nurodymą, tiek užuominą ir t.t. Iteruokite ir tikrinkite, kas veikia.                                                              |
| Eiliškumas svarbus               | Informacijos pateikimo modelio tvarka gali turėti įtakos išvestims, net ir mokymo pavyzdžiuose dėl naujausio informacijos pranašumo (recency bias). Išbandykite skirtingus variantus, kad rastumėte geriausią.                                           |
| Duokite modeliui „išeitį“         | Suteikite modeliui _atsarginį_ atsakymą, kurį jis gali pateikti, jei dėl kokių nors priežasčių negali užbaigti užduoties. Tai sumažina klaidingų ar išgalvotų atsakymų tikimybę.                                                                     |
|                                 |                                                                                                                                                                                                                                                   |

Kaip ir kiekviena geriausia praktika, atminkite, kad _rezultatai gali skirtis_ priklausomai nuo modelio, užduoties ir srities. Naudokite šias taisykles kaip pradžios tašką ir iteruokite, kol rasite tinkamiausią sprendimą. Nuolat vertinkite ir tobulinkite savo užklausų kūrimo procesą, kai pasirodo nauji modeliai ir įrankiai, ypatingą dėmesį skirdami proceso mastelio papildymui ir atsakymų kokybei.

<!--
PAMOKOS ŠABLONAS:
Ši pamoka turėtų pateikti programavimo užduotį, jei taikoma.

IŠŠŪKIS:
Nuoroda į Jupyter Notebook, kur tik komentaruose yra užduoties instrukcijos (kodo dalys tuščios).

SPRENDIMAS:
Nuoroda į tą patį Notebook su užpildytais ir paleistais komentarais, kuriame parodytas vienas pavyzdys.
-->

## Užduotis

Sveikiname! Pasiekėte pamokos pabaigą! Dabar laikas išbandyti kai kurias idėjas ir technikas realiais pavyzdžiais!

Mūsų užduočiai naudosime Jupyter Notebook su pratimais, kuriuos galėsite atlikti interaktyviai. Taip pat galite plėsti šį Notebook pridėdami savo Markdown ir kodo langelius, kad savarankiškai tyrinėtumėte idėjas ir technikas.

### Norėdami pradėti, sukurkite repo kopiją (fork), tada

- (Rekomenduojama) Paleiskite GitHub Codespaces
- (Alternatyviai) Nuklonuokite repozitoriją į savo kompiuterį ir naudokite su Docker Desktop
- (Alternatyviai) Atidarykite Notebook savo pasirinktoje aplinkoje

### Tada sukonfigūruokite aplinkos kintamuosius

- Nukopijuokite `.env.copy` failą repozitorijos šaknyje į `.env` ir užpildykite `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` ir `AZURE_OPENAI_DEPLOYMENT` reikšmes. Grįžkite į [Learning Sandbox skiltį](#mokymosi-smėlio-dėžė) sužinoti, kaip tai padaryti.

### Tada atidarykite Jupyter Notebook

- Pasirinkite vykdymo branduolį (kernel). Jei naudojate variantus 1 arba 2, tiesiog pasirinkite numatytąjį Python 3.10.x branduolį, pateiktą su dev konteineriu.

Jūs pasiruošę paleisti pratimus. Atkreipkite dėmesį, kad nėra čia „teisingų“ ar „neteisingų“ atsakymų – tik bandymas ir klaidos bei intuicijos auginimas, kas geriausiai veikia tam tikram modeliui ir panaudojimo sričiai.

_Dėl šios priežasties ši pamoka neturi programinio sprendimo segmentų. Vietoje to, Notebook turės Markdown langelius su pavadinimu „My Solution:“, kuriuose pateiktas vienas galimas atsakymas kaip pavyzdys._

 <!--
PAMOKOS ŠABLONAS:
Apibendrinkite skiltį su apžvalga ir ištekliais savarankiškam mokymuisi.
-->

## Žinių patikrinimas

Kurios iš šių užklausų atitinka pagrįstas geriausias praktikas?

1. Parodyk man raudono automobilio nuotrauką
2. Parodyk man raudono Volvo XC90 automobilio nuotrauką, stovintį prie skardžio saulėlydžio metu
3. Parodyk man raudono Volvo XC90 automobilio nuotrauką

A: 2, tai geriausia užklausa, nes ji pateikia informaciją apie „ką“ ir detalesnę aprašymo informaciją (ne bet koks automobilis, o konkretus gamintojas ir modelis) bei apibūdina bendrą situaciją. 3 yra antra geriausia, nes irgi turi daug aprašymo.

## 🚀 Iššūkis

Išbandykite "užuominos" techniką su užklausa: Užbaikite sakinį „Parodyk man raudono Volvo automobilio ir...“. Koks yra atsakymas ir kaip jį patobulintumėte?

## Puikiai padirbėta! Toliau mokykitės

Norite sužinoti daugiau apie įvairias užklausų inžinerijos koncepcijas? Eikite į [tolimesnio mokymosi puslapį](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kur rasite kitus puikius šios temos išteklius.

Toliau keliaukite į 5 pamoką, kur nagrinėsime [pažangias užklausų kūrimo technikas](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->