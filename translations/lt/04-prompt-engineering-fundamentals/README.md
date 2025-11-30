<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0135e6c271f3ece8699050d4debbce88",
  "translation_date": "2025-10-18T02:31:42+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "lt"
}
-->
# Pagrindai apie užklausų kūrimą

[![Pagrindai apie užklausų kūrimą](../../../translated_images/04-lesson-banner.a2c90deba7fedacda69f35b41636a8951ec91c2e33f5420b1254534ac85bc18e.lt.png)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Įvadas
Šiame modulyje aptariami esminiai konceptai ir technikos, kaip kurti efektyvias užklausas generatyviniams dirbtinio intelekto modeliams. Tai, kaip jūs formuluojate savo užklausą LLM (dideliam kalbos modeliui), yra labai svarbu. Kruopščiai suformuluota užklausa gali užtikrinti geresnę atsakymo kokybę. Bet ką iš tikrųjų reiškia tokie terminai kaip _užklausa_ ir _užklausų kūrimas_? Ir kaip galima patobulinti užklausos _įvestį_, kurią siunčiate LLM? Tai yra klausimai, į kuriuos bandysime atsakyti šiame ir kitame skyriuje.

_Generatyvinis dirbtinis intelektas_ gali kurti naują turinį (pvz., tekstą, vaizdus, garsą, kodą ir kt.) reaguodamas į vartotojo užklausas. Tai pasiekiama naudojant _Didelius kalbos modelius_, tokius kaip OpenAI GPT („Generative Pre-trained Transformer“) serija, kurie yra apmokyti naudoti natūralią kalbą ir kodą.

Dabar vartotojai gali bendrauti su šiais modeliais naudodami pažįstamus paradigmus, tokius kaip pokalbiai, nereikalaujant jokių techninių žinių ar mokymų. Modeliai yra _užklausų pagrindu sukurti_ – vartotojai siunčia tekstinę užklausą (prompt) ir gauna dirbtinio intelekto atsakymą (completion). Jie gali „kalbėtis su dirbtiniu intelektu“ iteratyviai, daugiapakopiuose pokalbiuose, tobulindami savo užklausą, kol atsakymas atitiks jų lūkesčius.

„Užklausos“ dabar tampa pagrindine _programavimo sąsaja_ generatyviniams dirbtinio intelekto programoms, nurodant modeliams, ką daryti, ir darant įtaką grąžinamų atsakymų kokybei. „Užklausų kūrimas“ yra sparčiai auganti studijų sritis, kuri orientuojasi į užklausų _dizainą ir optimizavimą_, siekiant užtikrinti nuoseklius ir kokybiškus atsakymus dideliu mastu.

## Mokymosi tikslai

Šioje pamokoje sužinosime, kas yra užklausų kūrimas, kodėl jis svarbus ir kaip galime kurti efektyvesnes užklausas konkrečiam modeliui ir taikymo tikslui. Suprasime pagrindinius užklausų kūrimo konceptus ir geriausias praktikas – ir sužinosime apie interaktyvią Jupyter Notebooks „smėlio dėžės“ aplinką, kurioje galime pritaikyti šiuos konceptus realiuose pavyzdžiuose.

Pamokos pabaigoje mes galėsime:

1. Paaiškinti, kas yra užklausų kūrimas ir kodėl jis svarbus.
2. Apibūdinti užklausos komponentus ir kaip jie naudojami.
3. Išmokti geriausias praktikas ir technikas užklausų kūrimui.
4. Pritaikyti išmoktas technikas realiuose pavyzdžiuose, naudojant OpenAI sąsają.

## Pagrindiniai terminai

Užklausų kūrimas: Praktika, kai kuriamos ir tobulinamos įvestys, siekiant nukreipti dirbtinio intelekto modelius į norimus rezultatus.
Tokenizacija: Teksto pavertimo mažesniais vienetais, vadinamais tokenais, procesas, kurį modelis gali suprasti ir apdoroti.
Instrukcijomis pritaikyti LLM: Dideli kalbos modeliai (LLM), kurie buvo specialiai pritaikyti su konkrečiomis instrukcijomis, siekiant pagerinti jų atsakymų tikslumą ir aktualumą.

## Mokymosi smėlio dėžė

Užklausų kūrimas šiuo metu yra labiau menas nei mokslas. Geriausias būdas pagerinti savo intuiciją šioje srityje yra _praktikuotis daugiau_ ir taikyti bandymų ir klaidų metodą, kuris derina taikymo srities žinias su rekomenduojamomis technikomis ir modelio specifinėmis optimizacijomis.

Pamokai skirtas Jupyter Notebook suteikia _smėlio dėžės_ aplinką, kurioje galite išbandyti tai, ką išmokote – tiek pamokos metu, tiek kaip kodo iššūkio dalį pamokos pabaigoje. Norėdami vykdyti pratimus, jums reikės:

1. **Azure OpenAI API rakto** – paslaugos sąsajos, skirtos įdiegtam LLM.
2. **Python aplinkos** – kurioje galima vykdyti Notebook.
3. **Vietinių aplinkos kintamųjų** – _užbaikite [NUSTATYMO](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) žingsnius dabar, kad pasiruoštumėte_.

Notebook turi _pradinių_ pratimų – tačiau jūs esate skatinami pridėti savo _Markdown_ (aprašymo) ir _Code_ (užklausų) sekcijas, kad išbandytumėte daugiau pavyzdžių ar idėjų – ir ugdytumėte savo intuiciją užklausų dizainui.

## Iliustruotas vadovas

Norite gauti bendrą vaizdą apie tai, ką apima ši pamoka, prieš pradedant gilintis? Peržiūrėkite šį iliustruotą vadovą, kuris suteikia supratimą apie pagrindines aptariamas temas ir svarbiausius dalykus, kuriuos verta apmąstyti kiekvienoje iš jų. Pamokos planas veda jus nuo pagrindinių konceptų ir iššūkių supratimo iki jų sprendimo, taikant atitinkamas užklausų kūrimo technikas ir geriausias praktikas. Atkreipkite dėmesį, kad „Pažangių technikų“ skyrius šiame vadove nurodo turinį, aptariamą _kitame_ šios mokymo programos skyriuje.

![Iliustruotas vadovas apie užklausų kūrimą](../../../translated_images/04-prompt-engineering-sketchnote.d5f33336957a1e4f623b826195c2146ef4cc49974b72fa373de6929b474e8b70.lt.png)

## Mūsų startuolis

Dabar pakalbėkime apie tai, kaip _ši tema_ susijusi su mūsų startuolio misija [įnešti dirbtinio intelekto inovacijas į švietimą](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Mes norime kurti dirbtinio intelekto pagrindu veikiančias _personalizuoto mokymosi_ programas – tad pagalvokime, kaip skirtingi mūsų programos vartotojai galėtų „kurti“ užklausas:

- **Administratoriai** galėtų paprašyti dirbtinio intelekto _analizuoti mokymo programos duomenis, kad būtų nustatytos spragos aprėptyje_. Dirbtinis intelektas galėtų apibendrinti rezultatus arba vizualizuoti juos naudodamas kodą.
- **Mokytojai** galėtų paprašyti dirbtinio intelekto _sukurti pamokos planą tam tikrai auditorijai ir temai_. Dirbtinis intelektas galėtų sukurti personalizuotą planą nurodytu formatu.
- **Mokiniai** galėtų paprašyti dirbtinio intelekto _padėti jiems mokytis sunkios temos_. Dirbtinis intelektas galėtų vesti mokinius per pamokas, pateikti užuominas ir pavyzdžius, pritaikytus jų lygiui.

Tai tik ledkalnio viršūnė. Peržiūrėkite [Užklausos švietimui](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – atvirą šaltinio užklausų biblioteką, kurią sudarė švietimo ekspertai – kad gautumėte platesnį galimybių vaizdą! _Pabandykite paleisti kai kurias iš tų užklausų smėlio dėžėje arba naudodami OpenAI Playground ir pažiūrėkite, kas nutiks!_

## Kas yra užklausų kūrimas?

Pamoką pradėjome apibrėždami **Užklausų kūrimą** kaip procesą, kurio metu _kuriamos ir optimizuojamos_ tekstinės įvestys (užklausos), siekiant užtikrinti nuoseklius ir kokybiškus atsakymus (užbaigimus) konkrečiam taikymo tikslui ir modeliui. Galime tai laikyti dviejų etapų procesu:

- _kuriant_ pradinę užklausą konkrečiam modeliui ir tikslui
- _tobulinant_ užklausą iteratyviai, siekiant pagerinti atsakymo kokybę

Tai neišvengiamai yra bandymų ir klaidų procesas, kuris reikalauja vartotojo intuicijos ir pastangų, kad būtų pasiekti optimalūs rezultatai. Kodėl tai svarbu? Norėdami atsakyti į šį klausimą, pirmiausia turime suprasti tris konceptus:

- _Tokenizacija_ = kaip modelis „mato“ užklausą
- _Bazinis LLM_ = kaip pagrindinis modelis „apdoroja“ užklausą
- _Instrukcijomis pritaikyti LLM_ = kaip modelis dabar mato „užduotis“

### Tokenizacija

LLM mato užklausas kaip _tokenų seką_, kur skirtingi modeliai (arba modelio versijos) gali skirtingai suskaidyti tą pačią užklausą. Kadangi LLM yra apmokyti su tokenais (o ne su neapdorotu tekstu), būdas, kuriuo užklausos yra suskaidomos į tokenus, tiesiogiai veikia generuojamo atsakymo kokybę.

Norėdami geriau suprasti, kaip veikia tokenizacija, išbandykite tokias priemones kaip [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst), parodytą žemiau. Nukopijuokite savo užklausą – ir pažiūrėkite, kaip ji paverčiama į tokenus, atkreipdami dėmesį į tai, kaip tvarkomi tarpai ir skyrybos ženklai. Atkreipkite dėmesį, kad šis pavyzdys rodo senesnį LLM (GPT-3) – todėl bandymas su naujesniu modeliu gali duoti kitokį rezultatą.

![Tokenizacija](../../../translated_images/04-tokenizer-example.e71f0a0f70356c5c7d80b21e8753a28c18a7f6d4aaa1c4b08e65d17625e85642.lt.png)

### Konceptas: Pagrindiniai modeliai

Kai užklausa yra suskaidyta į tokenus, pagrindinė ["Bazinio LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (arba Pagrindinio modelio) funkcija yra numatyti tokeną toje sekoje. Kadangi LLM yra apmokyti su didžiuliais tekstų duomenų rinkiniais, jie gerai supranta statistinius ryšius tarp tokenų ir gali atlikti šią prognozę su tam tikru pasitikėjimu. Atkreipkite dėmesį, kad jie nesupranta _žodžių prasmės_ užklausoje ar tokene; jie tiesiog mato modelį, kurį gali „užbaigti“ savo kita prognoze. Jie gali tęsti sekos prognozavimą, kol vartotojas nutrauks arba bus pasiektos iš anksto nustatytos sąlygos.

Norite pamatyti, kaip veikia užklausų pagrindu sukurtas užbaigimas? Įveskite aukščiau pateiktą užklausą į Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) su numatytaisiais nustatymais. Sistema sukonfigūruota traktuoti užklausas kaip informacijos prašymus – todėl turėtumėte pamatyti užbaigimą, kuris atitinka šį kontekstą.

Bet kas, jei vartotojas norėtų pamatyti kažką konkretaus, kas atitiktų tam tikrus kriterijus ar užduoties tikslą? Čia į pagalbą ateina _instrukcijomis pritaikyti_ LLM.

![Bazinis LLM pokalbio užbaigimas](../../../translated_images/04-playground-chat-base.65b76fcfde0caa6738e41d20f1a6123f9078219e6f91a88ee5ea8014f0469bdf.lt.png)

### Konceptas: Instrukcijomis pritaikyti LLM

[Instrukcijomis pritaikytas LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) prasideda nuo pagrindinio modelio ir yra pritaikytas naudojant pavyzdžius arba įvesties/išvesties poras (pvz., daugiapakopius „pranešimus“), kurie gali turėti aiškias instrukcijas – ir atsakymas iš dirbtinio intelekto bando laikytis tų instrukcijų.

Tai naudoja tokias technikas kaip stiprinamasis mokymasis su žmogaus grįžtamuoju ryšiu (RLHF), kuris gali apmokyti modelį _laikytis instrukcijų_ ir _mokytis iš grįžtamojo ryšio_, kad jis generuotų atsakymus, kurie yra labiau pritaikyti praktiniams taikymams ir labiau atitinka vartotojo tikslus.

Pabandykime – peržiūrėkite aukščiau pateiktą užklausą, tačiau dabar pakeiskite _sistemos pranešimą_, kad pateiktumėte šią instrukciją kaip kontekstą:

> _Apibendrinkite pateiktą turinį antros klasės mokiniui. Rezultatas turėtų būti vienas paragrafas su 3–5 punktų sąrašu._

Pažiūrėkite, kaip rezultatas dabar pritaikytas atspindėti norimą tikslą ir formatą? Mokytojas dabar gali tiesiogiai naudoti šį atsakymą savo klasės skaidrėse.

![Instrukcijomis pritaikytas LLM pokalbio užbaigimas](../../../translated_images/04-playground-chat-instructions.b30bbfbdf92f2d051639c9bc23f74a0e2482f8dc7f0dafc6cc6fda81b2b00534.lt.png)

## Kodėl mums reikia užklausų kūrimo?

Dabar, kai žinome, kaip užklausos yra apdorojamos LLM, pakalbėkime apie _kodėl_ mums reikia užklausų kūrimo. Atsakymas slypi tame, kad dabartiniai LLM kelia daugybę iššūkių, dėl kurių _patikimi ir nuoseklūs užbaigimai_ tampa sunkiau pasiekiami, jei neįdedama pastangų į užklausų konstravimą ir optimizavimą. Pavyzdžiui:

1. **Modelio atsakymai yra stochastiški.** _Ta pati užklausa_ greičiausiai duos skirtingus atsakymus su skirtingais modeliais ar modelio versijomis. Ir ji gali netgi duoti skirtingus rezultatus su _tuo pačiu modeliu_ skirtingu metu. _Užklausų kūrimo technikos gali padėti mums sumažinti šiuos skirtumus, suteikiant geresnes apsaugos priemones_.

1. **Modeliai gali kurti netikrus atsakymus.** Modeliai yra iš anksto apmokyti su _dideliais, bet ribotais_ duomenų rinkiniais, o tai reiškia, kad jie neturi žinių apie konceptus, esančius už šio mokymo ribų. Dėl to jie gali generuoti užbaigimus, kurie yra netikslūs, išgalvoti arba tiesiogiai prieštarauja žinomiems faktams. _Užklausų kūrimo technikos padeda vartotojams identifikuoti ir sumažinti tokius išgalvojimus, pvz., prašant dirbtinio intelekto pateikti citatas ar argumentus_.

1. **Modelių galimybės skiriasi.** Naujesni modeliai ar modelių kartos turės turtingesnes galimybes, tačiau taip pat atneš unikalių keistenybių ir kompromisų dėl kainos ir sudėtingumo. _Užklausų kūrimas gali padėti mums sukurti geriausias praktikas ir darbo eigas, kurios abstra
Interneto paieška parodė, kad yra išgalvotų pasakojimų (pvz., televizijos serialų ar knygų) apie Marso karus, tačiau nė vieno apie 2076 metus. Sveikas protas taip pat sako, kad 2076 metai yra _ateityje_ ir todėl negali būti susiję su realiu įvykiu.

Taigi, kas nutinka, kai šį užklausą pateikiame skirtingiems LLM tiekėjams?

> **Atsakymas 1**: OpenAI Playground (GPT-35)

![Atsakymas 1](../../../translated_images/04-fabrication-oai.5818c4e0b2a2678c40e0793bf873ef4a425350dd0063a183fb8ae02cae63aa0c.lt.png)

> **Atsakymas 2**: Azure OpenAI Playground (GPT-35)

![Atsakymas 2](../../../translated_images/04-fabrication-aoai.b14268e9ecf25caf613b7d424c16e2a0dc5b578f8f960c0c04d4fb3a68e6cf61.lt.png)

> **Atsakymas 3**: Hugging Face Chat Playground (LLama-2)

![Atsakymas 3](../../../translated_images/04-fabrication-huggingchat.faf82a0a512789565e410568bce1ac911075b943dec59b1ef4080b61723b5bf4.lt.png)

Kaip ir tikėtasi, kiekvienas modelis (arba modelio versija) pateikia šiek tiek skirtingus atsakymus dėl stochastinio elgesio ir modelio galimybių skirtumų. Pavyzdžiui, vienas modelis orientuojasi į 8 klasės auditoriją, o kitas - į vidurinės mokyklos mokinius. Tačiau visi trys modeliai pateikė atsakymus, kurie galėtų įtikinti neinformuotą vartotoją, kad įvykis buvo tikras.

Užklausų kūrimo technikos, tokios kaip _metaužklausos_ ir _temperatūros konfigūravimas_, gali tam tikru mastu sumažinti modelio klaidas. Naujos užklausų kūrimo _architektūros_ taip pat sklandžiai integruoja naujus įrankius ir technikas į užklausų srautą, kad sumažintų kai kuriuos šiuos efektus.

## Atvejo analizė: GitHub Copilot

Užbaikime šią dalį, susipažindami su tuo, kaip užklausų kūrimas naudojamas realiame pasaulyje, pažvelgdami į vieną atvejo analizę: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot yra jūsų „AI porinis programuotojas“ – jis paverčia tekstines užklausas kodų užbaigimais ir yra integruotas į jūsų kūrimo aplinką (pvz., Visual Studio Code), kad užtikrintų sklandžią vartotojo patirtį. Kaip dokumentuota žemiau pateiktuose tinklaraščiuose, ankstyviausia versija buvo pagrįsta OpenAI Codex modeliu – inžinieriai greitai suprato poreikį patobulinti modelį ir sukurti geresnes užklausų kūrimo technikas, kad pagerintų kodo kokybę. Liepą jie [pristatė patobulintą AI modelį, kuris pranoksta Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) ir siūlo dar greitesnius pasiūlymus.

Skaitykite įrašus iš eilės, kad galėtumėte sekti jų mokymosi kelionę.

- **2023 m. gegužė** | [GitHub Copilot tampa geresnis suprantant jūsų kodą](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **2023 m. gegužė** | [GitHub viduje: darbas su LLM, esančiais už GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **2023 m. birželis** | [Kaip rašyti geresnes užklausas GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **2023 m. liepa** | [.. GitHub Copilot pranoksta Codex su patobulintu AI modeliu](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **2023 m. liepa** | [Programuotojo vadovas apie užklausų kūrimą ir LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **2023 m. rugsėjis** | [Kaip sukurti įmonės LLM programą: pamokos iš GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Taip pat galite naršyti jų [inžinerijos tinklaraštį](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst), kad rastumėte daugiau įrašų, tokių kaip [šis](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), kuris parodo, kaip šie modeliai ir technikos yra _taikomi_ realioms programoms kurti.

---

## Užklausų kūrimas

Jau supratome, kodėl užklausų kūrimas yra svarbus – dabar išsiaiškinkime, kaip užklausos yra _kuriamos_, kad galėtume įvertinti skirtingas technikas efektyvesniam užklausų dizainui.

### Pagrindinė užklausa

Pradėkime nuo pagrindinės užklausos: teksto įvesties, siunčiamos modeliui be jokio papildomo konteksto. Štai pavyzdys – kai OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) siunčiame pirmuosius JAV nacionalinio himno žodžius, jis iš karto _papildo_ atsakymą kitomis eilutėmis, iliustruodamas pagrindinį prognozavimo elgesį.

| Užklausa (Įvestis) | Papildymas (Išvestis)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Atrodo, kad pradedate dainuoti „The Star-Spangled Banner“, Jungtinių Valstijų nacionalinį himną. Pilnas tekstas yra ...                     |

### Sudėtinga užklausa

Dabar pridėkime kontekstą ir instrukcijas prie pagrindinės užklausos. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) leidžia mums sukurti sudėtingą užklausą kaip _žinučių_ rinkinį su:

- Įvesties/išvesties poromis, atspindinčiomis _vartotojo_ įvestį ir _asistento_ atsakymą.
- Sistemos žinute, nustatančia asistento elgesio ar asmenybės kontekstą.

Užklausa dabar pateikiama žemiau nurodyta forma, kur _tokenizacija_ efektyviai užfiksuoja svarbią informaciją iš konteksto ir pokalbio. Dabar sistemos konteksto pakeitimas gali turėti tokį patį poveikį atsakymų kokybei, kaip ir pateiktos vartotojo įvestys.

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

### Instrukcijos užklausa

Ankstesniuose pavyzdžiuose vartotojo užklausa buvo paprastas tekstinis klausimas, kurį galima interpretuoti kaip informacijos užklausą. Naudojant _instrukcijų_ užklausas, galime naudoti tekstą, kad išsamiau nurodytume užduotį, suteikdami AI geresnes gaires. Štai pavyzdys:

| Užklausa (Įvestis)                                                                                                                                                                                                                         | Papildymas (Išvestis)                                                                                                        | Instrukcijos tipas  |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Parašykite aprašymą apie Pilietinį karą                                                                                                                                                                                                   | _grąžino paprastą pastraipą_                                                                                              | Paprasta            |
| Parašykite aprašymą apie Pilietinį karą. Pateikite pagrindines datas ir įvykius bei apibūdinkite jų reikšmę                                                                                                                                     | _grąžino pastraipą, po kurios pateiktas pagrindinių įvykių datų sąrašas su aprašymais_                                             | Sudėtinga           |
| Parašykite aprašymą apie Pilietinį karą vienoje pastraipoje. Pateikite 3 punktus su pagrindinėmis datomis ir jų reikšme. Pateikite dar 3 punktus su pagrindiniais istoriniais veikėjais ir jų indėliu. Grąžinkite išvestį JSON failo formatu | _grąžino išsamesnę informaciją teksto laukelyje, suformatuotą kaip JSON, kurį galima nukopijuoti ir įklijuoti į failą bei patikrinti_ | Sudėtinga. Su formatu. |

## Pagrindinis turinys

Ankstesniuose pavyzdžiuose užklausa vis dar buvo gana atvira, leidžianti LLM nuspręsti, kuri jo iš anksto apmokyto duomenų rinkinio dalis yra svarbi. Naudojant _pagrindinio turinio_ dizaino modelį, įvesties tekstas yra padalintas į dvi dalis:

- instrukcija (veiksmas)
- svarbus turinys (kuris daro įtaką veiksmui)

Štai pavyzdys, kur instrukcija yra „sutrumpinkite tai į 2 sakinius“.

| Užklausa (Įvestis)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Papildymas (Išvestis)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiteris yra penkta planeta nuo Saulės ir didžiausia Saulės sistemoje. Tai dujų milžinas, kurio masė yra tūkstantąja Saulės masės dalimi, tačiau du su puse karto didesnė už visų kitų planetų masę kartu sudėjus. Jupiteris yra vienas ryškiausių objektų, matomų plika akimi naktiniame danguje, ir buvo žinomas senovės civilizacijoms dar prieš užfiksuojant istoriją. Jis pavadintas Romos dievo Jupiterio vardu.[19] Žiūrint iš Žemės, Jupiteris gali būti pakankamai ryškus, kad jo atspindėta šviesa mestų matomus šešėlius,[20] ir vidutiniškai yra trečias ryškiausias natūralus objektas naktiniame danguje po Mėnulio ir Veneros. <br/> **Sutrumpinkite tai į 2 trumpus sakinius** | Jupiteris, penkta planeta nuo Saulės, yra didžiausia Saulės sistemoje ir žinoma kaip vienas ryškiausių objektų naktiniame danguje. Pavadintas Romos dievo Jupiterio vardu, tai dujų milžinas, kurio masė yra du su puse karto didesnė už visų kitų planetų masę kartu sudėjus. |

Pagrindinio turinio segmentą galima naudoti įvairiais būdais, siekiant efektyvesnių instrukcijų:

- **Pavyzdžiai** - vietoj to, kad modelį nurodytume aiškia instrukcija, pateikiame jam pavyzdžių, ką daryti, ir leidžiame jam pačiam suprasti modelį.
- **Užuominos** - po instrukcijos pateikiame „užuominą“, kuri nukreipia modelį link tinkamesnių atsakymų.
- **Šablonai** - tai pakartojami „receptai“ užklausoms su vietos rezervavimo ženklais (kintamaisiais), kuriuos galima pritaikyti konkretiems naudojimo atvejams.

Pažvelkime, kaip tai veikia praktikoje.

### Naudojant pavyzdžius

Tai metodas, kai naudojate pagrindinį turinį, kad „pamaitintumėte modelį“ keliais norimos išvesties pavyzdžiais pagal pateiktą instrukciją ir leistumėte jam pačiam suprasti norimą išvesties modelį. Atsižvelgiant į pateiktų pavyzdžių skaičių, galime turėti užklausas be pavyzdžių, su vienu pavyzdžiu, su keliais pavyzdžiais ir pan.

Užklausa dabar susideda iš trijų komponentų:

- Užduoties aprašymo
- Kelių norimos išvesties pavyzdžių
- Naujo pavyzdžio pradžios (kuris tampa netiesioginiu užduoties aprašymu)

| Mokymosi tipas | Užklausa (Įvestis)                                                                                                                                        | Papildymas (Išvestis)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Be pavyzdžių  | „The Sun is Shining“. Išverskite į ispanų kalbą                                                                                                            | „El Sol está brillando“.    |
| Su vienu pavyzdžiu | „The Sun is Shining“ => „El Sol está brillando“. <br> „It's a Cold and Windy Day“ =>                                                                 | „Es un día frío y ventoso“. |
| Su keliais pavyzdžiais | Žaidėjas bėgo bazėmis => Beisbolas <br/> Žaidėjas pataikė ace => Tenisas <br/> Žaidėjas pataikė šešis => Kriketas <br/> Žaidėjas atliko slam-dunk => | Krepšinis                  |
|               |                                                                                                                                                       |                             |

Atkreipkite dėmesį, kaip turėjome pateikti aiškią instrukciją („Išverskite į ispanų kalbą“) užklausose be pavyzdžių, tačiau ji tampa suprantama užklausose su vienu pavyzdžiu. Pavyzdys su keliais pavyzdžiais rodo, kaip pridėjus daugiau pavyzdžių modeliai gali tiksliau suprasti be papildomų instrukcijų.

### Užklausų užuominos

Kitas pagrindinio turinio naudojimo būdas yra pateikti _užuominas_, o ne pavyzdžius. Šiuo atveju mes suteikiame modeliui postūmį tinkama kryptimi, _pradėdami_ nuo fragmento, kuris atspindi norimą atsakymo formatą. Tada modelis „pagauna užuominą“ ir tęsia tuo pačiu stiliumi.

| Užuominų skaičius | Užklausa (Įvestis)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Papildymas (Išvestis)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiteris yra penkta planeta nuo Saulės ir didžiausia Saulės sistemoje. Tai dujų milžinas, kurio masė yra tūkstantąja Saulės masės dalimi, tačiau du su puse karto didesnė už visų kitų planetų masę kartu sudėjus. Jupiteris yra vienas ryškiausių objektų, matomų plika akimi naktiniame danguje, ir buvo žinomas senovės civilizacijoms dar prieš užfiksuojant istoriją. <br/>**Sutrumpinkite Tai**                                       | Jupiteris yra didžiausia planeta mūsų Saulės sistemoje ir penkta nuo Saulės. Tai dujų milžinas, kurio masė yra 1/1000 Saulės masės, tačiau jis sunkesnis už visas kitas planetas kartu sudėjus. Senovės civilizacijos jau seniai žinojo apie Jupiterį, ir jis lengvai matomas naktiniame danguje. |
| 1              | Jupiteris yra penkta planeta nuo Saulės ir didžiausia Saulės sistemoje. Tai dujų milžinas, kurio masė yra tūkstantąja Saulės masės dalimi, tačiau du su puse karto didesnė už visų kitų Saulės sistemos planetų masę kartu sudėjus. Jupiteris yra vienas ryškiausių objektų, matomų plika akimi naktiniame danguje, ir buvo žinomas senovės civilizacijoms dar prieš užrašytą istoriją. <br/>**Santrauka** <br/> Sužinojome, kad Jupiteris | yra penkta planeta nuo Saulės ir didžiausia Saulės sistemoje. Tai dujų milžinas, kurio masė yra tūkstantąja Saulės masės dalimi, tačiau du su puse karto didesnė už visų kitų planetų masę kartu sudėjus. Jis lengvai matomas plika akimi ir buvo žinomas nuo senovės laikų.                        |
| 2              | Jupiteris yra penkta planeta nuo Saulės ir didžiausia Saulės sistemoje. Tai dujų milžinas, kurio masė yra tūkstantąja Saulės masės dalimi, tačiau du su puse karto didesnė už visų kitų Saulės sistemos planetų masę kartu sudėjus. Jupiteris yra vienas ryškiausių objektų, matomų plika akimi naktiniame danguje, ir buvo žinomas senovės civilizacijoms dar prieš užrašytą istoriją. <br/>**Santrauka** <br/> 3 pagrindiniai faktai, kuriuos sužinojome:         | 1. Jupiteris yra penkta planeta nuo Saulės ir didžiausia Saulės sistemoje. <br/> 2. Tai dujų milžinas, kurio masė yra tūkstantąja Saulės masės dalimi...<br/> 3. Jupiteris buvo matomas plika akimi nuo senovės laikų ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Šablonai užduotims

Šablonas užduotims yra _iš anksto apibrėžtas šablonas_, kurį galima išsaugoti ir naudoti pagal poreikį, siekiant užtikrinti nuoseklesnę vartotojo patirtį dideliu mastu. Paprasčiausia forma tai yra tiesiog rinkinys pavyzdžių, kaip [šis iš OpenAI](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst), kuris pateikia tiek interaktyvius užduoties komponentus (vartotojo ir sistemos pranešimus), tiek API valdomą užklausos formatą - kad būtų galima pakartotinai naudoti.

Sudėtingesnėje formoje, kaip [šis pavyzdys iš LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), jis turi _vietos rezervavimo ženklus_, kuriuos galima pakeisti duomenimis iš įvairių šaltinių (vartotojo įvestis, sistemos kontekstas, išoriniai duomenų šaltiniai ir kt.), kad būtų galima dinamiškai generuoti užduotį. Tai leidžia sukurti pakartotinai naudojamų užduočių biblioteką, kuri gali būti naudojama nuosekliai vartotojo patirčiai **programiškai** užtikrinti dideliu mastu.

Galiausiai, tikroji šablonų vertė slypi galimybėje kurti ir publikuoti _užduočių bibliotekas_ tam tikroms taikymo sritims - kur užduoties šablonas yra _optimizuotas_ atspindėti taikymo srities kontekstą ar pavyzdžius, kurie daro atsakymus labiau aktualius ir tikslius tikslinės auditorijos atžvilgiu. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) saugykla yra puikus šio požiūrio pavyzdys, kurioje kaupiama užduočių biblioteka švietimo sričiai, akcentuojant pagrindinius tikslus, tokius kaip pamokų planavimas, mokymo programų kūrimas, mokinių konsultavimas ir kt.

## Papildoma informacija

Jei galvojame apie užduoties kūrimą kaip apie instrukcijos (užduoties) ir tikslo (pagrindinio turinio) turėjimą, tada _antrinis turinys_ yra kaip papildomas kontekstas, kurį pateikiame, kad **kažkaip paveiktume rezultatą**. Tai gali būti parametrų derinimas, formatavimo instrukcijos, temų taksonomijos ir kt., kurie gali padėti modeliui _pritaikyti_ savo atsakymą pagal norimus vartotojo tikslus ar lūkesčius.

Pavyzdžiui: Turint kursų katalogą su išsamiais metaduomenimis (pavadinimas, aprašymas, lygis, metaduomenų žymos, dėstytojas ir kt.) apie visus mokymo programos kursus:

- galime apibrėžti instrukciją „sutrumpinkite 2023 m. rudens semestro kursų katalogą“
- galime naudoti pagrindinį turinį, kad pateiktume keletą norimo rezultato pavyzdžių
- galime naudoti antrinį turinį, kad identifikuotume 5 svarbiausias „žymas“.

Dabar modelis gali pateikti santrauką formatu, parodytu keliuose pavyzdžiuose, tačiau jei rezultatas turi kelias žymas, jis gali teikti pirmenybę 5 žymoms, nurodytoms antriniame turinyje.

---

<!--
PAMOKOS ŠABLONAS:
Ši dalis turėtų apimti pagrindinę sąvoką #1.
Sustiprinkite sąvoką su pavyzdžiais ir nuorodomis.

SĄVOKA #3:
Užduočių kūrimo technikos.
Kokios yra pagrindinės užduočių kūrimo technikos?
Iliustruokite tai pratimais.
-->

## Geriausios užduočių kūrimo praktikos

Dabar, kai žinome, kaip užduotys gali būti _kuriamos_, galime pradėti galvoti, kaip jas _projektuoti_, kad jos atspindėtų geriausias praktikas. Galime tai suskirstyti į dvi dalis - turėti tinkamą _mąstyseną_ ir taikyti tinkamas _technikas_.

### Užduočių kūrimo mąstysena

Užduočių kūrimas yra bandymų ir klaidų procesas, todėl atsiminkite tris pagrindinius veiksnius:

1. **Domeno supratimas yra svarbus.** Atsakymo tikslumas ir aktualumas priklauso nuo _domeno_, kuriame veikia taikymas ar vartotojas. Naudokite savo intuiciją ir domeno žinias, kad **pritaikytumėte technikas**. Pavyzdžiui, apibrėžkite _domenui specifines asmenybes_ savo sistemos užduotyse arba naudokite _domenui specifinius šablonus_ vartotojo užduotyse. Pateikite antrinį turinį, kuris atspindi domenui specifinius kontekstus, arba naudokite _domenui specifinius užuominas ir pavyzdžius_, kad nukreiptumėte modelį link pažįstamų naudojimo modelių.

2. **Modelio supratimas yra svarbus.** Žinome, kad modeliai yra stochastiški. Tačiau modelių įgyvendinimas taip pat gali skirtis pagal naudojamą mokymo duomenų rinkinį (iš anksto išmoktas žinias), teikiamas galimybes (pvz., per API ar SDK) ir turinio tipą, kuriam jie yra optimizuoti (pvz., kodas, vaizdai ar tekstas). Supraskite modelio, kurį naudojate, stipriąsias ir silpnąsias puses ir naudokite šias žinias, kad _prioritetizuotumėte užduotis_ arba sukurtumėte _pritaikytus šablonus_, optimizuotus modelio galimybėms.

3. **Iteracija ir validacija yra svarbios.** Modeliai greitai tobulėja, kaip ir užduočių kūrimo technikos. Kaip domeno ekspertas, galite turėti kitą kontekstą ar kriterijus, kurie yra svarbūs _jūsų_ specifinei taikymo sričiai, bet gali būti netaikomi platesnei bendruomenei. Naudokite užduočių kūrimo įrankius ir technikas, kad „pradėtumėte“ užduočių kūrimą, tada iteruokite ir validuokite rezultatus naudodamiesi savo intuicija ir domeno žiniomis. Užfiksuokite savo įžvalgas ir sukurkite **žinių bazę** (pvz., užduočių bibliotekas), kurią kiti galėtų naudoti kaip naują pagrindą greitesnėms iteracijoms ateityje.

## Geriausios praktikos

Dabar pažvelkime į bendras geriausias praktikas, kurias rekomenduoja [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) ir [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) specialistai.

| Kas                               | Kodėl                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Įvertinkite naujausius modelius.  | Naujos modelių kartos greičiausiai turės patobulintas funkcijas ir kokybę, tačiau gali būti brangesnės. Įvertinkite jų poveikį, tada priimkite migracijos sprendimus.                                                                                |
| Atskirkite instrukcijas ir kontekstą | Patikrinkite, ar jūsų modelis/paslaugų teikėjas apibrėžia _skyriklius_, kad aiškiau atskirtų instrukcijas, pagrindinį ir antrinį turinį. Tai gali padėti modeliams tiksliau priskirti svorius žetonams.                                                         |
| Būkite konkretūs ir aiškūs        | Pateikite daugiau detalių apie norimą kontekstą, rezultatą, ilgį, formatą, stilių ir kt. Tai pagerins tiek atsakymų kokybę, tiek nuoseklumą. Užfiksuokite receptus pakartotinai naudojamuose šablonuose.                                                          |
| Būkite aprašomieji, naudokite pavyzdžius | Modeliai gali geriau reaguoti į „parodyk ir pasakyk“ metodą. Pradėkite nuo `zero-shot` metodo, kai pateikiate tik instrukciją (be pavyzdžių), tada išbandykite `few-shot` kaip patobulinimą, pateikdami keletą norimo rezultato pavyzdžių. Naudokite analogijas. |
| Naudokite užuominas, kad pradėtumėte atsakymus | Nukreipkite modelį link norimo rezultato, pateikdami keletą pradinių žodžių ar frazių, kurias jis galėtų naudoti kaip atsakymo pradžią.                                                                                                               |
| Kartokite                        | Kartais gali prireikti pakartoti instrukcijas modeliui. Pateikite instrukcijas prieš ir po pagrindinio turinio, naudokite instrukciją ir užuominą ir pan. Iteruokite ir validuokite, kad pamatytumėte, kas veikia.                                                         |
| Tvarka yra svarbi                | Informacijos pateikimo modelio tvarka gali paveikti rezultatą, net ir mokymosi pavyzdžiuose, dėl recency bias. Išbandykite skirtingas galimybes, kad pamatytumėte, kas veikia geriausiai.                                                               |
| Suteikite modeliui „išeitį“       | Suteikite modeliui _atsarginį_ atsakymą, kurį jis galėtų pateikti, jei dėl kokių nors priežasčių negalėtų užbaigti užduoties. Tai gali sumažinti modelių klaidingų ar išgalvotų atsakymų tikimybę.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

Kaip ir bet kuri geriausia praktika, atsiminkite, kad _jūsų rezultatai gali skirtis_ priklausomai nuo modelio, užduoties ir domeno. Naudokite tai kaip pradinį tašką ir iteruokite, kad rastumėte, kas geriausiai veikia jums. Nuolat peržiūrėkite savo užduočių kūrimo procesą, kai atsiranda nauji modeliai ir įrankiai, sutelkdami dėmesį į proceso mastelį ir atsakymų kokybę.

<!--
PAMOKOS ŠABLONAS:
Ši dalis turėtų pateikti kodo iššūkį, jei taikoma

IŠŠŪKIS:
Nuoroda į Jupyter Notebook su tik kodo komentarais instrukcijose (kodo sekcijos tuščios).

SPRENDIMAS:
Nuoroda į to Notebook kopiją su užpildytais ir paleistais užduotimis, parodant, koks galėtų būti vienas pavyzdys.
-->

## Užduotis

Sveikiname! Jūs pasiekėte pamokos pabaigą! Dabar laikas išbandyti kai kurias iš šių sąvokų ir technikų su realiais pavyzdžiais!

Mūsų užduočiai naudosime Jupyter Notebook su pratimais, kuriuos galėsite atlikti interaktyviai. Taip pat galite išplėsti Notebook, pridėdami savo Markdown ir kodo langelius, kad savarankiškai tyrinėtumėte idėjas ir technikas.

### Norėdami pradėti, fork'inkite saugyklą, tada

- (Rekomenduojama) Paleiskite GitHub Codespaces
- (Alternatyva) Klonuokite saugyklą į savo vietinį įrenginį ir naudokite ją su Docker Desktop
- (Alternatyva) Atidarykite Notebook su savo pasirinkta Notebook vykdymo aplinka.

### Toliau, sukonfigūruokite savo aplinkos kintamuosius

- Nukopijuokite `.env.copy` failą iš saugyklos šaknies į `.env` ir užpildykite `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` ir `AZURE_OPENAI_DEPLOYMENT` reikšmes. Grįžkite į [Mokymosi smėlio dėžės skyrių](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals), kad sužinotumėte, kaip tai padaryti.

### Toliau, atidarykite Jupyter Notebook

- Pasirinkite vykdymo branduolį. Jei naudojate 1 arba 2 variantą, tiesiog pasirinkite numatytąjį Python 3.10.x branduolį, kurį teikia kūrimo konteineris.

Jūs pasiruošę vykdyti pratimus. Atminkite, kad čia nėra _teisingų ar neteisingų_ atsakymų - tiesiog tyrinėkite galimybes bandymų ir klaidų būdu ir kurkite intuiciją, kas veikia tam tikram modeliui ir taikymo sričiai.

_Dėl šios priežasties šioje pamokoje nėra Kodo sprendimų segmentų. Vietoj to, Notebook turės Markdown langelius pavadinimu „Mano sprendimas:“, kuriuose bus parodytas vienas pavyzdinis atsakymas kaip nuoroda._

 <!--
PAMOKOS ŠABLONAS:
Apibendrinkite skyrių ir pateikite išteklius savarankiškam mokymuisi.
-->

## Žinių patikrinimas

Kurie iš šių yra geri užduočių pavyzdžiai, atitinkantys pagrįstas geriausias praktikas?

1. Parodyk man raudono automobilio vaizdą
2. Parodyk man raudono automobilio, Volvo markės ir XC90 modelio, stovinčio prie uolos su besileidžiančia saule, vaizdą
3. Parodyk man raudono automobilio, Volvo markės ir XC90 modelio, vaizdą

A: 2, tai geriausia užduotis, nes ji pateikia detales apie „ką“ ir eina į specifiką (ne bet koks automobilis, o konkretus markės ir modelio) ir taip pat aprašo bendrą aplinką. 3 yra kitas geriausias, nes jame taip pat yra daug aprašymo.

## 🚀 Iššūkis

Pabandykite pasinaudoti „užuominos“ technika su užduotimi: Užbaikite sakinį „Parodyk man raudono automobilio, Volvo markės ir “. Ką jis atsako, ir kaip galėtumėte tai patobulinti?

## Puikus darbas! Tęskite mokymąsi

Norite sužinoti daugiau apie skirtingas užduočių kūrimo sąvokas? Eikite į [tęstinio mokymosi puslapį](https://

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, atsiradusius dėl šio vertimo naudojimo.