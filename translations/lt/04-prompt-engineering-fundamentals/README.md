# Pagrindai apie Promptų Kūrimą

[![Promptų Kūrimo Pagrindai](../../../translated_images/lt/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Įvadas
Šiame modulyje aptariamos svarbios sąvokos ir technikos, skirtos efektyviems promptams generatyviniuose DI modeliuose kurti. Taip pat svarbu, kaip jūs rašote savo promptą LLM modeliui. Kruopščiai sukurtas promptas gali užtikrinti geresnės kokybės atsakymą. Bet ką tiksliai reiškia tokie terminai kaip _promptas_ ir _promptų kūrimas_? Ir kaip patobulinti prompto _įvestį_, kurią siunčiu LLM modeliui? Į šiuos klausimus bandysime atsakyti šiame ir kitame skyriuje.

_Generatyvus DI_ gali kurti naują turinį (pvz., tekstą, vaizdus, garsą, kodą ir pan.) pagal vartotojo užklausas. Tai pasiekiama naudojant _Didelių Kalbos Modelius_ (LLM) kaip OpenAI GPT („Generatyvus Išankstinis Transformeris“) seriją, kurie yra apmokyti naudoti natūralią kalbą ir kodą.

Vartotojai dabar gali bendrauti su šiais modeliais naudodamiesi pažįstamais pokalbių principais, nereikalaujant techninių žinių ar mokymų. Modeliai yra _promptų valdomi_ - vartotojai siunčia teksto įvestį (promptą) ir gauna DI atsakymą (užbaigimą). Jie gali iteratyviai „kalbėtis su DI“ daugiatūrėse pokalbių sesijose, tobulindami promptą, kol atsakymas atitinka jų lūkesčius.

„Promptai“ dabar tampa pagrindine _programavimo sąsaja_ generatyvioms DI programoms, nurodančią modeliams, ką daryti ir įtakojančia grąžinamų atsakymų kokybę. „Promptų Kūrimas“ - sparčiai auganti studijų sritis, kurios tikslas yra _projektuoti ir optimizuoti_ promptus, kad būtų galima tiekti nuoseklius ir aukštos kokybės atsakymus mastu.

## Mokymosi Tikslai

Šioje pamokoje sužinosime, kas yra promptų kūrimas, kodėl tai svarbu ir kaip galime sukurti veiksmingesnius promptus konkrečiam modeliui ir programos tikslui. Suprasime pagrindines sąvokas ir geriausias praktikas promptų kūrimui - taip pat susipažinsime su interaktyvia Jupyter užrašų knyga („sandbox“ aplinka), kurioje galėsime pamatyti šias sąvokas taikomas realiuose pavyzdžiuose.

Baigę šią pamoką gebėsime:

1. Paaiškinti, kas yra promptų kūrimas ir kodėl tai svarbu.
2. Aprašyti prompto komponentus ir kaip jie naudojami.
3. Išmokti geriausias praktikas ir technikas promptų kūrimui.
4. Taikyti išmoktus metodus realiuose pavyzdžiuose, naudojant OpenAI pabaigos tašką.

## Pagrindiniai Terminai

Promptų Kūrimas: Praktika, skirta projektuoti ir tobulinti įvestis, kad DI modeliai galėtų pateikti norimus rezultatus.
Tokenizacija: Teksto pavertimo į mažesnes dalis – vadinamas tokenais – procesas, kurį modelis supranta ir apdoroja.
Instrukcijomis Mokyti LLM: Dideli Kalbos Modeliai, kurie yra papildomai mokyti su konkrečiomis instrukcijomis, siekiant pagerinti atsakymų tikslumą ir aktualumą.

## Mokymosi Sandbox

Promptų kūrimas šiuo metu yra labiau menas nei mokslas. Geriausias būdas tobulinti savo intuiciją - _praktikuotis daugiau_ ir naudoti metodo bandymų ir klaidų derinį, apjungiant programos veiklos srities žinias su rekomenduojamomis technikomis ir modelio specifinėmis optimizacijomis.

Šiai pamokai pridedama Jupyter Užrašų knyga, kuri suteikia _sandbox_ aplinką, kurioje galite išbandyti išmoktas žinias – iš karto arba kaip dalį pabaigos kodo užduoties. Norint vykdyti pratimus, jums reikės:

1. **Azure OpenAI API rakto** – paslaugos pabaigos taško įdiegto LLM modeliui.
2. **Python vykdymo aplinkos** – kur vykdymo Užrašų knyga.
3. **Vietinių aplinkos kintamųjų** – _dabar baigti [PARUOŠIMO](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) veiksmus, kad būtumėte pasiruošę_.

Užrašų knyga turi _pradines_ užduotis, tačiau esate skatinami pridėti savo _Markdown_ (aprašymo) ir _Kodo_ (promptų užklausų) dalis, kad išbandytumėte daugiau pavyzdžių ar idėjų – ir vystytumėte savo intuiciją promptų kūrime.

## Iliustruotas Vadovas

Norite gauti bendrą vaizdą, ką apima ši pamoka, prieš panir-dami į detales? Peržiūrėkite šį iliustruotą vadovą, kuris suteikia supratimą apie pagrindines aptariamas temas ir svarbiausias išvadas, apie kurias verta pagalvoti kiekvienoje. Pamokos kelias jus nuves nuo pagrindinių sąvokų ir iššūkių supratimo iki jų sprendimo taikant susijusias promptų kūrimo technikas ir geriausias praktikas. Atkreipkite dėmesį, kad šio vadovo skyrius „Pažangios Technikos“ nurodo medžiagą, aptariamą kitoje šio mokymo skyriuje.

![Iliustruotas Vadovas apie Promptų Kūrimą](../../../translated_images/lt/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Mūsų Startuolis

Dabar pakalbėkime, kaip _ši tema_ susijusi su mūsų startuolio misija [atsinešti DI inovacijas į švietimą](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Norime kurti DI pagrįstas programas dėl _asmeninio mokymosi_ – tad pagalvokime, kaip skirtingi mūsų programos vartotojai galėtų „sukurti“ promptus:

- **Administratoriai** galėtų paprašyti DI _analizuoti mokymo programos duomenis, kad nustatytų spragas apimtyje_. DI gali apibendrinti rezultatus arba pavaizduoti juos su kodu.
- **Mokytojai** galėtų paprašyti DI _parengti pamokos planą tikslinės auditorijos temai_. DI gali sukurti asmeniniu planą nurodytu formatu.
- **Mokiniai** galėtų paprašyti DI _padėti jiems studijuoti sunkų dalyką_. DI dabar gali vadovauti mokiniams naudojant pamokas, užuominas ir pavyzdžius, pritaikytus jų lygiui.

Tai tik ledkalnio viršūnė. Pažiūrėkite [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – atviro kodo biblioteką, kurią kuruoja švietimo ekspertai – kad suprastumėte platesnes galimybes! _Išbandykite kai kuriuos iš tų promptų sandbox aplinkoje ar naudodami OpenAI Playground ir pamatykite, kas įvyksta!_

<!--
PAMOKOS ŠABLONAS:
Ši dalis turėtų apimti pagrindinę sąvoką #1.
Pagrįskite sąvoką pavyzdžiais ir nuorodomis.

SĄVOKA #1:
Promptų Kūrimas.
Apibrėžkite ją ir paaiškinkite, kodėl to reikia.
-->

## Kas yra Promptų Kūrimas?

Šią pamoką pradedame apibrėždami **Promptų Kūrimą** kaip tekstinių įvesčių (promptų) _projektavimo ir optimizavimo_ procesą, siekiant užtikrinti nuoseklius ir kokybiškus atsakymus (užbaigimus) pagal konkretų taikymo tikslą ir modelį. Galime tai suprasti kaip dviejų žingsnių procesą:

- _projektuoti_ pradinį promptą konkrečiam modeliui ir tikslui
- _tobulinti_ promptą iteratyviai, kad pagerintume atsakymo kokybę

Tai neabejotinai yra bandymų ir klaidų procesas, kuriam reikia vartotojo intuicijos ir pastangų, kad būtų pasiekti optimalūs rezultatai. Tad kodėl tai svarbu? Kad į tai atsakytume, pirmiausia reikia suprasti tris sąvokas:

- _Tokenizacija_ = kaip modelis „mato“ promptą
- _Bazinis LLM_ = kaip pagrindinis modelis „apdoroja“ promptą
- _Instrukcijomis mokytas LLM_ = kaip modelis dabar mato „užduotis“

### Tokenizacija

LLM mato promptus kaip _tokenų seką_, kur skirtingi modeliai (ar modelio versijos) gali tokenizuoti tą patį promptą skirtingais būdais. Kadangi LLM mokomi tokenų pagrindu (o ne žemo lygio teksto), tai, kaip promptas tokenizuojamas, tiesiogiai veikia generuojamo atsakymo kokybę.

Norėdami pajusti, kaip veikia tokenizacija, išbandykite įrankius kaip [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) parodytą žemiau. Nukopijuokite savo promptą ir pamatykite, kaip jis virsta tokenais, atkreipdami dėmesį, kaip apdorojami tarpai ir skyrybos ženklai. Atkreipkite dėmesį, kad šiame pavyzdyje rodomas senesnis LLM (GPT-3), tad bandymas su naujesniu modeliu gali duoti kitokius rezultatus.

![Tokenizacija](../../../translated_images/lt/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Sąvoka: Pagrindiniai Modeliai

Kai promptas yra tokenizuojamas, pagrindinė ["Bazinis LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (ar Pagrindinis modelis) funkcija yra prognozuoti sekos tokeną. Kadangi LLM mokomi masyviuose tekstiniuose rinkiniuose, jie gerai supranta statistinius ryšius tarp tokenų ir gali numatyti seką su tam tikra pasitikėjimo norma. Pastebėkite, kad jie nesupranta _žodžių reikšmės_ promte ar tokene; jie tiesiog mato modelį, kurį gali „užbaigti“ savo kitomis prognozėmis. Jie gali tęsti sekos prognozavimą, kol naudotojas nutraukia arba įvyksta iš anksto numatyta sąlyga.

Norite pamatyti, kaip veikia promptais pagrįstas užbaigimas? Įveskite aukščiau pateiktą promptą į [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) su numatytomis nustatymų reikšmėmis. Sistema sukonfigūruota traktuoti promptus kaip informacijos užklausas – tad turėtumėte matyti atsakymą, kuris atitinka šį kontekstą.

Bet kas, jei naudotojas norėtų matyti ką nors specifinio, atitinkančio tam tikrus reikalavimus ar užduoties tikslą? Čia į pagalbą ateina _instrukcijomis mokyti_ LLM.

![Bazinis LLM Pokalbio Užbaigimas](../../../translated_images/lt/04-playground-chat-base.65b76fcfde0caa67.webp)

### Sąvoka: Instrukcijomis Mokyti LLM

[Instrukcijomis Mokytas LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) prasideda nuo bazinio modelio ir tobulinamas naudojant pavyzdžius ar įvesties/išvesties poras (pvz., daugkartinius „žinučių“ turus), kuriuose gali būti aiškios instrukcijos – ir DI atsakas bando sekti tas instrukcijas.

Tai naudoja tokius metodus kaip sustiprintas mokymasis su žmogaus grįžtamuoju ryšiu (RLHF), kuris gali išmokyti modelį _vykdyti instrukcijas_ ir _mokytis iš atsiliepimų_, kad generuotų atsakymus, tinkamesnius praktinėms programoms ir labiau atitinkančius vartotojo tikslus.

Išbandykime – grįžkite prie ankstesnio prompto, bet dabar pakeiskite _sistemos pranešimą_, kad perteiktumėte šią instrukciją kaip kontekstą:

> _Apibendrinkite pateiktą turinį antrojoje klasėje esančiam mokiniui. Laikykitės vieno pastraipos ilgio su 3-5 punktų sąrašu._

Matote, kaip rezultatas dabar pritaikytas atitikti pageidaujamą tikslą ir formatą? Mokytojas gali tiesiogiai naudoti šį atsakymą savo klasės skaidrėse.

![Instrukcijomis Mokyto LLM Pokalbio Užbaigimas](../../../translated_images/lt/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Kodėl mums reikia Promptų Kūrybos?

Dabar, kai žinome, kaip promptai apdorojami LLM, pakalbėkime apie _kodėl_ mums reikia promptų kūrimo. Atsakymas slypi tame, kad dabartiniai LLM kelia daugybę iššūkių, kurie apsunkina _patikimų ir nuoseklių atsakymų_ gavimą be pastangų kuriant ir optimizuojant promptus. Pavyzdžiui:

1. **Modelių atsakymai yra stokastiniai.** _Tas pats promptas_ greičiausiai duos skirtingus atsakymus skirtingiems modeliams ar jų versijoms. Ir jis gali duoti skirtingus rezultatus su _to paties modelio_ skirtingais laikais. _Promptų kūrimo technikos padeda sumažinti šiuos skirtumus, suteikiant geresnes apsaugas_.

1. **Modeliai gali kurti išgalvotus atsakymus.** Modeliai yra iš anksto mokyti su _dideliais, tačiau ribotais_ duomenų rinkiniais, todėl jie neturi žinių apie sąvokas už mokymo ribų. Todėl jie gali kurti netikslius, išgalvotus ar tiesiogiai prieštaraujančius žinomoms faktams atsakymus. _Promptų kūrimo technikos padeda vartotojams identifikuoti ir sumažinti tokius klaidingus atsakymus, pvz., klausiant DI apie šaltinius ar argumentaciją_.

1. **Modelių galimybės kinta.** Naujesni modeliai ar jų kartos turi daugiau galimybių, bet taip pat atneša unikalių ypatybių, kaštų ir sudėtingumo kompromisus. _Promptų kūrimas gali padėti sukurti geriausias praktikas ir darbo eigas, kurios abstraktina skirtumus ir prisitaiko prie modelio specifinių reikalavimų mastomai bei sklandžiai_.

Pažiūrėkime tai praktiškai OpenAI ar Azure OpenAI Playground:

- Naudokite tą patį promptą su skirtingais LLM įdiegimais (pvz., OpenAI, Azure OpenAI, Hugging Face) – ar pastebėjote skirtumus?
- Naudokite tą patį promptą pakartotinai su _ta pačia_ LLM instaliacija (pvz., Azure OpenAI playground) – kaip šie skirtumai pasiskirstė?

### Išgalvotų Atsakymų Pavyzdys

Šiame kurse vartojame terminą **„išgalvotas atsakymas“** kaip reiškinį, kai LLM kartais generuoja faktine prasme neteisingą informaciją dėl mokymo apribojimų ar kitų veiksnių. Taip pat galėjote girdėti apie tai kaip apie _„haliucinacijas“_ populiariuose straipsniuose ar moksliniuose darbuose. Tačiau mes kategoriškai rekomenduojame naudoti _„išgalvotas atsakymas“_, kad nesuteiktume mašininiam rezultatui žmogaus bruožų ir taip neanthropomorfizuotume elgesio. Tai taip pat sustiprina [Atsakingo DI gaires](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) terminologijos požiūriu, pašalinant žodžius, kurie kai kuriose situacijose gali būti laikomi įžeidžiančiais ar neįtraukiantys.

Norite suprasti, kaip veikia išgalvoti atsakymai? Pagalvokite apie promptą, kuris nurodo DI sukurti turinį neegzistuojančia tema (užtikrinti, kad jos nėra mokymo duomenų rinkinyje). Pavyzdžiui – aš išbandžiau tokį promptą:

> **Promptas:** sukurkite pamokos planą apie Marso karą 2076 metais.

Internetinė paieška parodė, kad yra fantastiniai pasakojimai (pvz., televizijos serialai ar knygos) apie Marso karus – bet ne 2076 metais. Sveikas protas taip pat sako, kad 2076 metai yra _ateityje_ ir todėl negali būti susiję su tikru įvykiu.


Kas nutinka, kai šį užklausą paleidžiame su skirtingais LLM tiekėjais?

> **Atsakymas 1**: OpenAI Playground (GPT-35)

![Atsakymas 1](../../../translated_images/lt/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Atsakymas 2**: Azure OpenAI Playground (GPT-35)

![Atsakymas 2](../../../translated_images/lt/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Atsakymas 3**: : Hugging Face Chat Playground (LLama-2)

![Atsakymas 3](../../../translated_images/lt/04-fabrication-huggingchat.faf82a0a51278956.webp)

Kaip ir tikėtasi, kiekvienas modelis (ar modelio versija) pateikia šiek tiek skirtingus atsakymus dėl stokastinio elgesio ir modelio gebėjimų skirtumų. Pavyzdžiui, vienas modelis skirtas aštuntos klasės auditorijai, o kitas numato vidurinės mokyklos mokinį. Tačiau visi trys modeliai sugeneravo atsakymus, galinčius įtikinti neinformuotą naudotoją, kad įvykis yra tikras.

Užklausų kūrimo technikos, tokios kaip _metaužklausos_ ir _temperatūros konfigūravimas_, gali tam tikra apimtimi sumažinti modelio išradingumą. Naujos užklausų inžinerijos _architektūros_ taip pat sklandžiai įtraukia naujus įrankius bei technikas į užklausos srautą, siekiant sumažinti kai kuriuos šių efektų pasireiškimus.

## Atvejo studija: GitHub Copilot

Užbaigsime šį skyrių pažvelgdami, kaip užklausų inžinerija naudojama tikruose sprendimuose per vieną Atvejo studiją: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot yra jūsų „AI partneris programuotojas“ – jis konvertuoja teksto užklausas į kodo užbaigimus ir integruotas į jūsų kūrimo aplinką (pvz., Visual Studio Code) dėl sklandžios naudotojo patirties. Kaip aprašyta žemiau pateiktoje tinklaraščių serijoje, ankstyviausia versija buvo paremta OpenAI Codex modeliu – inžinieriai greitai suprato, kad reikia tiksliai pakoreguoti modelį ir sukurti geresnes užklausų inžinerijos technikas, kad pagerintų kodo kokybę. Liepos mėnesį jie [pasiūlė patobulintą dirbtinio intelekto modelį, kuris viršija Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst), kad pasiūlymai būtų dar greitesni.

Skaitykite įrašus iš eilės, kad sektumėte jų mokymosi kelią.

- **2023 m. gegužė** | [GitHub Copilot geriau supranta jūsų kodą](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **2023 m. gegužė** | [GitHub vidų: darbas su LLM, kurie veikia GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **2023 m. birželis** | [Kaip rašyti geresnes užklausas GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **2023 m. liepa** | [.. GitHub Copilot viršija Codex su patobulintu DI modeliu](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **2023 m. liepa** | [Kūrėjo vadovas užklausų inžinerijai ir LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **2023 m. rugsėjis** | [Kaip kurti įmonės LLM programą: pamokos iš GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Taip pat galite peržiūrėti jų [Inžinerijos tinklaraštį](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst), kuriame rasite daugiau įrašų, panašių į [šiame](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), rodantį, kaip šie modeliai ir technikos yra _taikomi_ realių programų kūrimui skatinti.

---

<!--
PAMOKOS ŠABLONAS:
Ši dalis turėtų apimti pagrindinę sąvoką #2.
Pagrįskite šią sąvoką pavyzdžiais ir nuorodomis.

SĄVOKA #2:
Užklausos dizainas.
Iliustruota pavyzdžiais.
-->

## Užklausos kūrimas

Matėme, kodėl užklausų inžinerija yra svarbi – dabar supraskime, kaip užklausos yra _kuriamos_, kad galėtume įvertinti skirtingas technikas efektyvesniam užklausų dizainui.

### Pagrindinė užklausa

Pradėkime nuo pagrindinės užklausos: teksto įvesties, pateiktos modeliui be jokio papildomo konteksto. Štai pavyzdys – kai pirmuosius kelis JAV nacionalinės himno žodžius siunčiame OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), jis iš karto _užbaigia_ atsakymą keliais kitais eilutėmis, iliustruodamas pagrindinį prognozavimo elgesį.

| Užklausa (įvestis) | Užbaigimas (išvestis)                                                                                                                                                                   |
| :----------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Skamba, kad pradedate dainuoti „The Star-Spangled Banner“, Jungtinių Amerikos Valstijų nacionalinį himną. Visas tekstas yra ...                                 |

### Kompleksinė užklausa

Dabar pridėkime kontekstą ir instrukcijas prie tos pagrindinės užklausos. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) leidžia sukurti sudėtingą užklausą kaip kolekciją iš _pranešimų_, kuriuose yra:

- įvesties/išvesties poros, atspindinčios _vartotojo_ įvestį ir _padėjėjo_ atsakymą.
- Sistemos pranešimas, nustatantis kontekstą padėjėjo elgesiui ar asmenybei.

Užklausa dabar pateikiama žemiau pateikta forma, kur _tokenizacija_ efektyviai fiksuoja svarbią informaciją iš konteksto ir pokalbio. Dabar sistemos konteksto pakeitimas gali būti toks pat svarbus atsakymų kokybei kaip ir pateikti vartotojo įvesties duomenys.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Instrukcinė užklausa

Aukščiau pateiktuose pavyzdžiuose vartotojo užklausa buvo paprastas teksto užklausimas, kurį galima interpretuoti kaip informacijos prašymą. Su _instrukcinėmis_ užklausomis galime naudoti tą tekstą, kad detaliau apibrėžtume užduotį, suteikdami DI geresnes gaires. Štai pavyzdys:

| Užklausa (įvestis)                                                                                                                                                                                                                              | Užbaigimas (išvestis)                                                                                  | Instrukcijos tipas |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------- | :----------------- |
| Parašyk aprašymą apie Pilietinį karą                                                                                                                                                                                                          | _grąžino paprastą pastraipą_                                                                            | Paprasta           |
| Parašyk aprašymą apie Pilietinį karą. Pateik svarbias datas ir įvykius bei aprašyk jų reikšmę                                                                                                                                                   | _grąžino pastraipą, po kurios seka svarbių įvykių datų sąrašas su aprašymais_                           | Sudėtinga          |
| Parašyk aprašymą apie Pilietinį karą 1 pastraipoje. Pateik 3 punktus su svarbiomis datomis ir jų reikšme. Pateik dar 3 punktus su svarbiais istoriniais asmenimis ir jų indėliu. Grąžink išvestį JSON faile | _grąžina išsamesnę informaciją teksto laukelyje, suformatuotą kaip JSON, kurį galite nukopijuoti ir įklijuoti į failą ir prireikus patikrinti_ | Sudėtinga. Su formatu. |

## Pagrindinis turinys

Aukščiau pateiktuose pavyzdžiuose užklausa vis dar buvo gana atvira, leidžianti LLM nuspręsti, kuri duomenų dalis yra svarbi. Naudojant _pagrindinio turinio_ dizaino modelį, įvesties tekstas yra padalijamas į du segmentus:

- instrukciją (veiksmą)
- svarbų turinį (veikiančią įtaką veiksmui)

Štai pavyzdys, kai instrukcija yra „apibendrinkite tai 2 sakiniai“.

| Užklausa (įvestis)                                                                                                                                                                                                                                                                                                                                                                                    | Užbaigimas (išvestis)                                                                                                                                                                                                                   |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiteris yra penktoji planeta nuo Saulės ir didžiausia Saulės sistemoje. Tai dujų milžinė, kurios masė yra tūkstantąji Saulės masės dalis, bet du su puse karto didesnė už visų kitų planetų masių sumą Saulės sistemoje. Jupiteris yra vienas ryškiausių objektų, matomų plika akimi naktiniame danguje, ir jis buvo žinomas senovės civilizacijoms dar iki rašytinės istorijos. Jis pavadintas Romos dievo Jupiterio vardu.[19] Žvelgiant iš Žemės, Jupiteris gali būti toks ryškus, kad jo atspindėta šviesa meta matomas šešėlius,[20] ir vidutiniškai yra trečias ryškiausias natūralus objektas naktiniame danguje po Mėnulio ir Veneros. <br/> **Apibendrinkite tai 2 trumpais sakiniais** | Jupiteris, penktoji planeta nuo Saulės, yra didžiausia Saulės sistemos planeta ir viena ryškiausių naktinio dangaus objektų. Pavadinta Romos dievo Jupiterio vardu, tai dujų milžinė, kurios masė yra du su puse karto didesnė už visų kitų planetų sumą Saulės sistemoje. |

Pagrindinio turinio segmentą galima naudoti įvairiais būdais, siekiant efektyviau formuluoti instrukcijas:

- **Pavyzdžiai** – vietoje to, kad būtų duota tiesioginė instrukcija, pateikite pavyzdžių, ką daryti, ir leiskite modeliui nuspėti modelį.
- **Užuominos** – po instrukcijos pridėkite „užuominą“, kuri paruošia užbaigimą, nukreipdama modelį į tinkamesnius atsakymus.
- **Šablonai** – tai kartojamos užklausų „receptūros“ su kintamaisiais, kurie gali būti pritaikyti konkrečioms naudotojų reikmėms.

Pažiūrėkime, kaip šie metodai veikia praktiškai.

### Naudojant pavyzdžius

Tai metodas, kai pagrindinis turinys naudojamas „pamaitinti modelį“ keliais pavyzdžiais norimos išvesties tam tikrai instrukcijai, ir leidžiama modeliui nuspėti norimo rezultato modelį. Remdamiesi pateiktų pavyzdžių skaičiumi, galime turėti nulio pavyzdžių užklausą (zero-shot), vieno pavyzdžio užklausą (one-shot), kelių pavyzdžių užklausą (few-shot) ir pan.

Užklausa dabar susideda iš trijų dalių:

- Užduoties aprašymas
- Kelis norimos išvesties pavyzdžius
- Naujai pavyzdžiui pradžia (tapo netiesioginiu užduoties aprašymu)

| Mokymosi tipas | Užklausa (įvestis)                                                                                                                                   | Užbaigimas (išvestis)    |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------- |
| Zero-shot     | „Saulė šviečia“. Išverskite į ispanų kalbą                                                                                                       | „El Sol está brillando“. |
| One-shot      | „Saulė šviečia“ => „El Sol está brillando“. <br> „Šaltas ir vėjuotas oras“ =>                                                                     | „Es un día frío y ventoso“. |
| Few-shot      | Žaidėjas bėgo bazėmis => Beisbolas <br/> Žaidėjas atliko „ace“ => Tenisas <br/> Žaidėjas pataikė „six“ => Kriketas <br/> Žaidėjas atliko „slam-dunk“ => | Krepšinis               |
|               |                                                                                                                                                   |                          |

Atkreipkite dėmesį, kad nulio pavyzdžių užklausoje reikėjo pateikti tiesioginę instrukciją („Išverskite į ispanų kalbą“), tačiau ji nuspėjama vieno pavyzdžio užklausoje. Kelių pavyzdžių pavyzdys rodo, kaip pateikus daugiau pavyzdžių, modeliai tiksliau atspėja be papildomų instrukcijų.

### Užklausų užuominos

Kita pagrindinio turinio naudojimo technika yra teikti ne pavyzdžius, o _užuominas_. Tokiu atveju mes duodame modelio krypties užuominą, _pradėdami_ nuo ištraukos, atitinkančios norimą atsakymo formatą. Modelis tada „priima užuominą“ ir tęsia toliau tokiu būdu.

| Užuominų skaičius | Užklausa (įvestis)                                                                                                                                                                                                                                                                                                                                                             | Užbaigimas (išvestis)                                                                                                                                                                                                                                                                               |
| :--------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                | Jupiteris yra penktoji planeta nuo Saulės ir didžiausia Saulės sistemoje. Tai dujų milžinė, kurios masė yra tūkstantąji Saulės masės dalis, bet du su puse karto didesnė už visų kitų planetų masių sumą Saulės sistemoje. Jupiteris yra vienas ryškiausių objektų, matomų plika akimi naktiniame danguje, ir jis buvo žinomas senovės civilizacijoms dar iki rašytinės istorijos. <br/>**Apibendrinkite tai**                                           | Jupiteris yra didžiausia planeta mūsų Saulės sistemoje ir penktoji nuo Saulės. Tai dujų milžinė, kurios masė yra 1/1000 Saulės masės, bet jis sunkesnis už visas kitas planetas kartu sudėjus. Senovės civilizacijos jau ilgai žino apie Jupiterį, ir jis lengvai matomas naktiniame danguje..           |
| 1                | Jupiteris yra penktoji planeta nuo Saulės ir didžiausia Saulės sistemoje. Tai dujų milžinė, kurios masė yra tūkstantąji Saulės masės dalis, bet du su puse karto didesnė už visų kitų planetų masių sumą Saulės sistemoje. Jupiteris yra vienas ryškiausių objektų, matomų plika akimi naktiniame danguje, ir jis buvo žinomas senovės civilizacijoms dar iki rašytinės istorijos. <br/>**Apibendrinkite tai** <br/> Ko mes sužinojome, yra tai, kad Jupiteris | yra penktoji planeta nuo Saulės ir didžiausia Saulės sistemoje. Tai dujų milžinė, kurios masė yra tūkstantąji Saulės masės dalis, bet du su puse karto didesnė už visų kitų planetų masių sumą kartu sudėjus. Jis lengvai matomas plika akimi ir žinomas nuo senovės laikų.                          |

| 2              | Jupiteris yra penktoji planeta nuo Saulės ir didžiausia Saulės sistemoje. Tai dujų milžinas, kurio masė yra tūkstantąja Saulės dalimi, tačiau dvigubai ir dar pusantro karto didesnė nei visų kitų Saulės sistemos planetų masės kartu sudėjus. Jupiteris yra vienas iš ryškiausių objektų, matomų plika akimi naktiniame danguje ir buvo žinomas senosioms civilizacijoms dar prieš rašytinę istoriją. <br/>**Santrauka** <br/> 3 pagrindiniai faktai, kuriuos sužinojome:         | 1. Jupiteris yra penktoji planeta nuo Saulės ir didžiausia Saulės sistemoje. <br/> 2. Tai dujų milžinas, kurio masė yra tūkstantąja Saulės dalimi...<br/> 3. Jupiteris yra matomas plika akimi nuo seniausių laikų ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Užklausų Šablonai

Užklausų šablonas yra _iš anksto apibrėžtas užklausos receptas_, kurį galima saugoti ir pakartotinai naudoti pagal poreikį, siekiant didesnio nuoseklumo vartotojo patirtyse. Paprasčiausia forma tai yra paprasčiausia užklausų pavyzdžių kolekcija, kaip [ši iš OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst), kuri pateikia tiek interaktyvias užklausos dalis (vartotojo ir sistemos žinutes), tiek API pagrindu veikiantį užklausos formatą – kad būtų galima pakartotinai naudoti.

Sudėtingesnėje formoje, kaip [ši pavyzdys iš LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), jis turi _vietas_, kurias galima pakeisti duomenimis iš įvairių šaltinių (vartotojo įvesties, sistemos konteksto, išorinių duomenų šaltinių ir kt.), taip dinamiškai kuriant užklausą. Tai leidžia kurti pakartotinai naudojamų užklausų biblioteką, kurią galima **programiškai** naudoti vienodai vartotojo patirčiai užtikrinti didelio masto.

Galiausiai, tikroji šablonų vertė slypi gebėjime kurti ir publikuoti _užklausų bibliotekas_ konkrečioms taikymo sritims – kur užklausos šablonas yra _optimizuotas_ taip, kad atspindėtų taikymo srities kontekstą ar pavyzdžius, kurie daro atsakymus labiau aktualius ir tikslius tikslinės vartotojų auditorijos atžvilgiu. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) saugykla yra puikus šio požiūrio pavyzdys – kurianti užklausų biblioteką švietimo sričiai, akcentuojant svarbiausius tikslus, tokius kaip pamokų planavimas, mokymo programų kūrimas, mokinių konsultavimas ir pan.

## Papildomas Turinio Palaikymas

Jei galvosime apie užklausos konstravimą kaip instrukciją (užduotį) ir tikslinį turinį (pagrindinį turinį), tada _antrinis turinys_ yra kaip papildomas kontekstas, kurį pateikiame, kad **kokiu nors būdu paveiktume rezultatą**. Tai gali būti derinimo parametrai, formatavimo nurodymai, temų taksonomijos ir kt., kurie padeda modeliui _prisitaikyti_ prie norimų vartotojo tikslų ar lūkesčių.

Pavyzdžiui: Turint kursų katalogą su išsamia metaduomenų informacija (pavadinimas, aprašymas, lygis, metaduomenų žymos, dėstytojas ir kt.) apie visus turimus kursus mokymo programoje:

- galime apibrėžti instrukciją „apibendrinti 2023 rudens semestro kursų katalogą“
- galime naudoti pagrindinį turinį, kad pateiktume keletą pageidaujamo rezultato pavyzdžių
- galime naudoti antrinį turinį, kad identifikuotume 5 svarbiausias „žymas“

Dabar modelis gali pateikti santrauką formatu, parodytu keliuose pavyzdžiuose – bet jei viename rezultate yra kelių žymų, jis gali prioritetuoti 5 antriniame turinyje identifikuotas žymas.

---

<!--
PAMOKŲ ŠABLONAS:
Ši pamoka turėtų apimti pagrindinę sąvoką Nr. 1.
Sustiprinkite sąvoką pavyzdžiais ir nuorodomis.

SĄVOKA NR. 3:
Užklausos inžinerijos metodai.
Kokie yra pagrindiniai užklausų inžinerijos metodai?
Iliustruokite tai keletu pratimų.
-->

## Užklausų Rengimo Gerosios Praktikos

Dabar, kai žinome, kaip gali būti _kuriamos_ užklausos, galime pradėti galvoti apie jų _kūrimą_ atsižvelgiant į gerąsias praktikas. Galime tai nagrinėti dviem dalimis – turėti tinkamą _mąstyseną_ ir taikyti tinkamus _metodus_.

### Užklausų Inžinerijos Mąstysena

Užklausų inžinerija yra bandymų ir klaidų procesas, tad turėkite omenyje tris plačius pagrindinius veiksnius:

1. **Srities supratimas yra svarbus.** Atsakymų tikslumas ir aktualumas priklauso nuo _srities_, kurioje veikia ta programa ar vartotojas. Taikyti savo intuiciją ir srities ekspertizę, kad **tolesniam technikų pritaikymui**. Pavyzdžiui, apibrėžkite _srities specifines asmenybes_ savo sistemos užklausose arba naudokite _srities specifinius šablonus_ vartotojo užklausose. Pateikite antrinį turinį, atspindintį srities kontekstus, arba naudokite _srities specifinius ženklus ir pavyzdžius_, kad nukreiptumėte modelį į pažįstamus naudojimo modelius.

2. **Modelio suvokimas yra svarbus.** Žinome, kad modeliai iš esmės yra atsitiktiniai. Tačiau modelių įgyvendinimai taip pat gali skirtis pagal mokymo duomenų rinkinį (iš anksto išmokta informacija), suteikiamas galimybes (pvz., per API ar SDK) ir turinio, kuriam optimizuoti, tipą (pvz., kodas vs. vaizdai vs. tekstas). Supraskite modelio, kurį naudojate, privalumus ir apribojimus ir naudokite tą žinią _užduočių prioritizavimui_ arba _individualių šablonų kūrimui_, optimizuotiems modelio galimybėms.

3. **Kartojimas ir patvirtinimas yra svarbūs.** Modeliai sparčiai tobulėja ir taip pat gerėja užklausų inžinerijos metodai. Kaip srities ekspertas, galite turėti papildomą kontekstą ar kriterijus _jūsų_ konkrečiai programai, kurie gali netikti platesnei bendruomenei. Naudokite užklausų inžinerijos įrankius ir metodus, kad „pagreitintumėte“ užklausų konstravimą, tada iteruokite ir tikrinkite rezultatus naudodami savo intuiciją bei srities žinias. Įrašykite savo įžvalgas ir kurkite **žinių bazę** (pvz., užklausų biblioteką), kuri galėtų būti nauju pagrindu kitiems, siekiant greitesnių iteracijų ateityje.

## Gerosios Praktikos

Dabar pažvelkime į bendrąsias gerąsias praktikas, kurias rekomenduoja [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) ir [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) specialistai.

| Kas                                | Kodėl                                                                                                                                                                                                                                             |
| :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Vertinkite naujausius modelius.    | Naujos modelių kartos greičiausiai turi pagerintas savybes ir kokybę – bet gali sukelti ir didesnes kainas. Įvertinkite jų poveikį ir priimkite sprendimus dėl migracijos.                                                                        |
| Atskirti instrukcijas ir kontekstą | Patikrinkite, ar jūsų modelis/tiekėjas apibrėžia _ribas_, kurios aiškiau atskiria instrukcijas, pagrindinį ir antrinį turinį. Tai gali padėti modeliams tiksliau skirti svorius žymoms.                                                             |
| Būkite konkretūs ir aiškūs          | Pateikite daugiau detalių apie pageidaujamą kontekstą, rezultatą, ilgį, formatą, stilių ir kt. Tai pagerins tiek kokybę, tiek atsakymų nuoseklumą. Užfiksuokite receptus pakartotinai naudojamuose šablonuose.                                        |
| Būkite aprašomieji, naudokite pavyzdžius | Modeliai gali geriau reaguoti į „rodyk ir pasakyk“ būdą. Pradėkite nuo `zero-shot` metodo, kai pateikiate tik instrukciją (be pavyzdžių), o po to pabandykite `few-shot` tobulinimą, pateikdami keletą pageidaujamo rezultato pavyzdžių. Naudokite analogijas. |
| Naudokite ženklus užbaigimams pradėti | Skatinkite modelį link pageidaujamo rezultato, suteikdami keletą pradinės frazės žodžių ar posakių, kuriuos modelis gali naudoti pradžiai užbaigti atsakymą.                                                                                         |
| Kartokite                         | Kartais gali tekti modelį pakartotinai nurodyti. Pateikite instrukcijas prieš ir po pagrindinio turinio, naudokite instrukciją ir ženklą, ir pan. Kartokite ir tikrinkite, kas veikia geriausiai.                                                    |
| Tvarka yra svarbi                 | Informacijos pateikimo modeliui tvarka gali paveikti rezultatą, net mokymo pavyzdžiuose, dėl naujumo šališkumo. Išbandykite skirtingas parinktis, kad sužinotumėte, kas veikia geriausiai.                                                        |
| Duokite modeliui „išeitį“         | Pateikite modeliui atsarginį (_fallback_) užbaigimo atsakymą, kurį jis gali pateikti, jei dėl kokių nors priežasčių negali užbaigti užduoties. Tai sumažina netikrų ar suklastotų atsakymų tikimybę.                                                |
|                                   |                                                                                                                                                                                                                                                   |

Kaip ir su bet kokia gera praktika, atminkite, kad _jūsų situacija gali skirtis_ priklausomai nuo modelio, užduoties ir srities. Naudokite šiuos patarimus kaip pradinį tašką ir iteruokite, kad surastumėte, kas jums veikia geriausiai. Nuolat vertinkite savo užklausų inžinerijos procesą, kai atsiranda nauji modeliai ir įrankiai, sutelkdami dėmesį į proceso mastelį ir atsakymų kokybę.

<!--
PAMOKOS ŠABLONAS:
Ši tema turėtų pateikti kodų užduotį, jei taikoma

UŽDUOTIS:
Nuoroda į Jupyter užrašų knygelę, kurioje tik kodų komentarai kaip instrukcijos (kodo sekcijos tuščios).

SPRENDIMAS:
Nuoroda į to paties užrašų knygelės kopiją su užpildytomis užklausomis ir paleistą, rodant vieną pavyzdinį rezultatą.
-->

## Užduotis

Sveikiname! Jūs pasiekėte pamokos pabaigą! Laikas išbandyti keletą šių sąvokų ir metodų su realiais pavyzdžiais!

Mūsų užduočiai naudosime Jupyter užrašų knygelę, kurią galėsite užpildyti interaktyviai. Taip pat galite plėsti užrašų knygelę savo Markdown ir Kodo blokais, kad savarankiškai tyrinėtumėte idėjas ir metodus.

### Norėdami pradėti, padarykite šakojimą (fork) ir tada

- (Rekomenduojama) Paleiskite GitHub Codespaces
- (Alternatyviai) Klonuokite saugyklą į vietinę įrenginį ir naudokite su Docker Desktop
- (Alternatyviai) Atidarykite užrašų knygelę savo mėgstamoje užrašų knygelės vykdymo aplinkoje.

### Toliau sukonfigūruokite aplinkos kintamuosius

- Nukopijuokite `.env.copy` failą saugyklos šaknyje į `.env` ir užpildykite reikšmes `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` ir `AZURE_OPENAI_DEPLOYMENT`. Grįžkite į [Learning Sandbox skiltį](#mokymosi-sandbox), kad sužinotumėte, kaip tai padaryti.

### Toliau atidarykite Jupyter užrašų knygelę

- Pasirinkite vykdymo branduolį. Jei naudojate parinktis 1 arba 2, tiesiog pasirinkite numatytąjį Python 3.10.x branduolį, suteiktą kūrimo konteineryje.

Jūs pasiruošę atlikti pratimus. Atkreipkite dėmesį, kad čia nėra _teisingų ar klaidingų_ atsakymų – tik eksperimentavimas ir intuicijos kūrimas, kas veikia tam tikram modeliui ar taikymo sričiai.

_Todėl šioje pamokoje nėra Kodo sprendimo dalių. Vietoje to Užrašų knygelėje bus Markdown blokai pavadinti „Mano sprendimas:“, kuriuose pateikiamas vieno pavyzdinio rezultato pavyzdys._

 <!--
PAMOKOS ŠABLONAS:
Apibendrinkite skyrių santrauka ir ištekliais savarankiškam mokymuisi.
-->

## Žinių patikrinimas

Kuris iš šių yra gera užklausa, atitinkanti pagrįstas gerąsias praktikas?

1. Parodyk man raudono automobilio paveikslėlį
2. Parodyk man raudono Volvo XC90 automobilio paveikslėlį, stovintį prie skardžio, saulės leidžiantis
3. Parodyk man raudono Volvo XC90 automobilio paveikslėlį

A: 2 yra geriausia užklausa, nes ji pateikia detalių apie „ką“ ir tiksliai nurodo (ne bet kokį automobilį, o konkretų markę ir modelį), taip pat aprašo bendrą aplinką. 3 yra antra geriausia, nes irgi daug aprašymo turi.

## 🚀 Iššūkis

Patikrinkite, ar galite naudoti „ženklų“ techniką užklausoje: Užbaikite sakinį „Parodyk man raudono Volvo automobilio paveikslėlį ir “. Koks bus atsakymas, ir kaip jį patobulintumėte?

## Puikus darbas! Tęskite mokymąsi

Norite sužinoti daugiau apie skirtingas užklausų inžinerijos sąvokas? Eikite į [tolimesnio mokymosi puslapį](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kur rasite kitų puikių šaltinių šia tema.

Kitoje pamokoje – 5 skyriuje – nagrinėsime [pažangias užklausų technikas](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->