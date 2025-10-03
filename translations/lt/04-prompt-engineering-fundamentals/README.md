<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8b3cb38518cf4fe7714d2f5e74dfa3eb",
  "translation_date": "2025-10-03T10:46:18+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "lt"
}
-->
# Pagrindai apie užklausų kūrimą

[![Pagrindai apie užklausų kūrimą](../../../translated_images/04-lesson-banner.a2c90deba7fedacda69f35b41636a8951ec91c2e33f5420b1254534ac85bc18e.lt.png)](https://aka.ms/gen-ai-lesson4-gh?WT.mc_id=academic-105485-koreyst)

## Įvadas
Šiame modulyje aptariami esminiai konceptai ir technikos, kaip kurti efektyvias užklausas generatyviniams AI modeliams. Tai, kaip formuluojate savo užklausą LLM, yra labai svarbu. Kruopščiai suformuluota užklausa gali užtikrinti geresnę atsakymo kokybę. Bet ką iš tikrųjų reiškia tokie terminai kaip _užklausa_ ir _užklausų kūrimas_? Ir kaip pagerinti užklausos _įvestį_, kurią siunčiate LLM? Šiuos klausimus bandysime atsakyti šiame ir kitame skyriuje.

_Generatyvinis AI_ gali kurti naują turinį (pvz., tekstą, vaizdus, garsą, kodą ir kt.) pagal vartotojo užklausas. Tai pasiekiama naudojant _Didelius Kalbos Modelius_ (LLM), tokius kaip OpenAI GPT („Generatyvinis Išankstinio Mokymo Transformatorius“) serija, kurie yra apmokyti naudoti natūralią kalbą ir kodą.

Vartotojai dabar gali bendrauti su šiais modeliais naudodami pažįstamus paradigmus, tokius kaip pokalbiai, nereikalaujant techninių žinių ar mokymų. Modeliai yra _užklausų pagrindu_ – vartotojai siunčia tekstinę užklausą ir gauna AI atsakymą (užbaigimą). Jie gali „kalbėtis su AI“ iteratyviai, daugiapakopiuose pokalbiuose, tobulindami savo užklausą, kol atsakymas atitinka jų lūkesčius.

„Užklausos“ dabar tampa pagrindine _programavimo sąsaja_ generatyviniams AI programoms, nurodant modeliams, ką daryti, ir įtakojant grąžinamų atsakymų kokybę. „Užklausų kūrimas“ yra sparčiai auganti studijų sritis, kuri orientuojasi į _užklausų dizainą ir optimizavimą_, siekiant užtikrinti nuoseklius ir kokybiškus atsakymus mastu.

## Mokymosi tikslai

Šioje pamokoje sužinosime, kas yra užklausų kūrimas, kodėl jis svarbus ir kaip galime kurti efektyvesnes užklausas konkrečiam modeliui ir programos tikslui. Suprasime pagrindinius konceptus ir geriausias praktikas užklausų kūrimui – ir sužinosime apie interaktyvią Jupyter Notebook „smėlio dėžės“ aplinką, kurioje galime pritaikyti šiuos konceptus realiuose pavyzdžiuose.

Pamokos pabaigoje galėsime:

1. Paaiškinti, kas yra užklausų kūrimas ir kodėl jis svarbus.
2. Apibūdinti užklausos komponentus ir kaip jie naudojami.
3. Išmokti geriausias praktikas ir technikas užklausų kūrimui.
4. Pritaikyti išmoktas technikas realiuose pavyzdžiuose, naudojant OpenAI galinį tašką.

## Pagrindiniai terminai

Užklausų kūrimas: Praktika, kai kuriamos ir tobulinamos įvestys, siekiant nukreipti AI modelius į norimų rezultatų generavimą.
Tokenizacija: Teksto konvertavimo į mažesnius vienetus, vadinamus tokenais, procesas, kurį modelis gali suprasti ir apdoroti.
Instrukcijomis pritaikyti LLM: Dideli Kalbos Modeliai (LLM), kurie buvo specialiai pritaikyti su konkrečiomis instrukcijomis, siekiant pagerinti atsakymų tikslumą ir aktualumą.

## Mokymosi smėlio dėžė

Užklausų kūrimas šiuo metu yra labiau menas nei mokslas. Geriausias būdas pagerinti savo intuiciją šioje srityje yra _praktikuotis daugiau_ ir taikyti bandymų-klaidų metodą, kuris derina programos srities ekspertizę su rekomenduojamomis technikomis ir modelio specifinėmis optimizacijomis.

Pamoką lydintis Jupyter Notebook suteikia _smėlio dėžės_ aplinką, kurioje galite išbandyti tai, ką išmokote – tiek pamokos metu, tiek kaip dalį kodo iššūkio pabaigoje. Norėdami vykdyti pratimus, jums reikės:

1. **Azure OpenAI API rakto** – paslaugos galinio taško, kuriame įdiegtas LLM.
2. **Python vykdymo aplinkos** – kurioje galima vykdyti Notebook.
3. **Vietinių aplinkos kintamųjų** – _užbaikite [NUSTATYMO](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) veiksmus dabar, kad pasiruoštumėte_.

Notebook pateikiami _pradiniai_ pratimai – tačiau skatiname pridėti savo _Markdown_ (aprašymo) ir _Code_ (užklausų) sekcijas, kad išbandytumėte daugiau pavyzdžių ar idėjų – ir ugdytumėte savo intuiciją užklausų dizainui.

## Iliustruotas vadovas

Norite gauti bendrą vaizdą apie tai, ką apima ši pamoka, prieš pasinerdami į detales? Peržiūrėkite šį iliustruotą vadovą, kuris suteikia supratimą apie pagrindines aptariamas temas ir svarbiausius dalykus, kuriuos verta apmąstyti kiekvienoje iš jų. Pamokos planas veda jus nuo pagrindinių konceptų ir iššūkių supratimo iki jų sprendimo, naudojant atitinkamas užklausų kūrimo technikas ir geriausias praktikas. Atkreipkite dėmesį, kad „Pažangių technikų“ skyrius šiame vadove nurodo turinį, aptariamą _kitame_ šios mokymo programos skyriuje.

![Iliustruotas vadovas apie užklausų kūrimą](../../../translated_images/04-prompt-engineering-sketchnote.d5f33336957a1e4f623b826195c2146ef4cc49974b72fa373de6929b474e8b70.lt.png)

## Mūsų startuolis

Dabar pakalbėkime apie tai, kaip _ši tema_ susijusi su mūsų startuolio misija [atnešti AI inovacijas į švietimą](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Mes norime kurti AI pagrindu veikiančias _personalizuoto mokymosi_ programas – tad pagalvokime, kaip skirtingi mūsų programos vartotojai galėtų „kurti“ užklausas:

- **Administratoriai** galėtų paprašyti AI _analizuoti mokymo programos duomenis, kad nustatytų spragas aprėptyje_. AI galėtų apibendrinti rezultatus arba vizualizuoti juos kodu.
- **Mokytojai** galėtų paprašyti AI _sukurti pamokos planą konkrečiai auditorijai ir temai_. AI galėtų sukurti personalizuotą planą nurodytu formatu.
- **Mokiniai** galėtų paprašyti AI _padėti jiems mokytis sudėtingo dalyko_. AI galėtų dabar mokyti mokinius pamokomis, užuominomis ir pavyzdžiais, pritaikytais jų lygiui.

Tai tik ledkalnio viršūnė. Peržiūrėkite [Užklausos švietimui](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – atvirą šaltinio užklausų biblioteką, kurią sudarė švietimo ekspertai – kad gautumėte platesnį galimybių vaizdą! _Išbandykite kai kurias iš tų užklausų smėlio dėžėje arba naudodami OpenAI Playground ir pažiūrėkite, kas nutiks!_

<!--
PAMOKOS ŠABLONAS:
Ši dalis turėtų apimti pagrindinį konceptą #1.
Sustiprinkite konceptą pavyzdžiais ir nuorodomis.

KONCEPTAS #1:
Užklausų kūrimas.
Apibrėžkite jį ir paaiškinkite, kodėl jis reikalingas.
-->

## Kas yra užklausų kūrimas?

Pamoką pradėjome apibrėždami **Užklausų kūrimą** kaip procesą, kai _kuriamos ir optimizuojamos_ tekstinės įvestys (užklausos), siekiant užtikrinti nuoseklius ir kokybiškus atsakymus (užbaigimus) konkrečiam programos tikslui ir modeliui. Galime tai laikyti 2 žingsnių procesu:

- _kuriant_ pradinę užklausą konkrečiam modeliui ir tikslui
- _tobulinant_ užklausą iteratyviai, siekiant pagerinti atsakymo kokybę

Tai neišvengiamai yra bandymų-klaidų procesas, kuris reikalauja vartotojo intuicijos ir pastangų, kad būtų pasiekti optimalūs rezultatai. Tad kodėl tai svarbu? Norėdami atsakyti į šį klausimą, pirmiausia turime suprasti tris konceptus:

- _Tokenizacija_ = kaip modelis „mato“ užklausą
- _Bazinis LLM_ = kaip pagrindinis modelis „apdoroja“ užklausą
- _Instrukcijomis pritaikyti LLM_ = kaip modelis dabar mato „užduotis“

### Tokenizacija

LLM mato užklausas kaip _tokenų seką_, kur skirtingi modeliai (ar modelio versijos) gali tokenizuoti tą pačią užklausą skirtingais būdais. Kadangi LLM yra apmokyti tokenais (o ne neapdorotu tekstu), tai, kaip užklausos yra tokenizuojamos, tiesiogiai veikia generuojamo atsakymo kokybę.

Norėdami geriau suprasti, kaip veikia tokenizacija, išbandykite tokias priemones kaip [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst), parodytą žemiau. Nukopijuokite savo užklausą – ir pažiūrėkite, kaip ji konvertuojama į tokenus, atkreipdami dėmesį į tai, kaip tvarkomi tarpai ir skyrybos ženklai. Atkreipkite dėmesį, kad šis pavyzdys rodo senesnį LLM (GPT-3) – tad bandymas su naujesniu modeliu gali duoti kitokį rezultatą.

![Tokenizacija](../../../translated_images/04-tokenizer-example.e71f0a0f70356c5c7d80b21e8753a28c18a7f6d4aaa1c4b08e65d17625e85642.lt.png)

### Konceptas: Pagrindiniai modeliai

Kai užklausa yra tokenizuota, pagrindinė ["Bazinio LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (arba Pagrindinio modelio) funkcija yra numatyti tokeną toje sekoje. Kadangi LLM yra apmokyti didžiuliais tekstų duomenų rinkiniais, jie gerai supranta statistinius ryšius tarp tokenų ir gali atlikti šią prognozę su tam tikru pasitikėjimu. Atkreipkite dėmesį, kad jie nesupranta _žodžių prasmės_ užklausoje ar tokene; jie tiesiog mato modelį, kurį gali „užbaigti“ su savo kita prognoze. Jie gali tęsti sekos prognozavimą, kol vartotojas nutraukia arba įvyksta iš anksto nustatyta sąlyga.

Norite pamatyti, kaip veikia užklausų pagrindu atliekamas užbaigimas? Įveskite aukščiau pateiktą užklausą į Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) su numatytaisiais nustatymais. Sistema sukonfigūruota traktuoti užklausas kaip informacijos prašymus – tad turėtumėte matyti užbaigimą, kuris atitinka šį kontekstą.

Bet ką daryti, jei vartotojas norėjo pamatyti kažką konkretaus, kas atitiktų tam tikrus kriterijus ar užduoties tikslą? Čia į pagalbą ateina _instrukcijomis pritaikyti_ LLM.

![Bazinis LLM pokalbio užbaigimas](../../../translated_images/04-playground-chat-base.65b76fcfde0caa6738e41d20f1a6123f9078219e6f91a88ee5ea8014f0469bdf.lt.png)

### Konceptas: Instrukcijomis pritaikyti LLM

[Instrukcijomis pritaikytas LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) prasideda nuo pagrindinio modelio ir yra pritaikomas su pavyzdžiais ar įvesties/išvesties poromis (pvz., daugiapakopėmis „žinutėmis“), kurios gali turėti aiškias instrukcijas – ir AI atsakymas bando laikytis tų instrukcijų.

Tai naudoja tokias technikas kaip stiprinimo mokymasis su žmogaus grįžtamuoju ryšiu (RLHF), kuris gali apmokyti modelį _laikytis instrukcijų_ ir _mokytis iš grįžtamojo ryšio_, kad jis generuotų atsakymus, kurie yra labiau pritaikyti praktinėms programoms ir labiau atitinka vartotojo tikslus.

Išbandykime – grįžkite prie aukščiau pateiktos užklausos, bet dabar pakeiskite _sistemos žinutę_, kad pateiktumėte šią instrukciją kaip kontekstą:

> _Apibendrinkite pateiktą turinį antros klasės mokiniui. Rezultatas turėtų būti vienas paragrafas su 3–5 punktų sąrašu._

Pažiūrėkite, kaip rezultatas dabar pritaikytas atspindėti norimą tikslą ir formatą? Mokytojas dabar gali tiesiogiai naudoti šį atsakymą savo skaidrėse tai klasei.

![Instrukcijomis pritaikytas LLM pokalbio užbaigimas](../../../translated_images/04-playground-chat-instructions.b30bbfbdf92f2d051639c9bc23f74a0e2482f8dc7f0dafc6cc6fda81b2b00534.lt.png)

## Kodėl mums reikia užklausų kūrimo?

Dabar, kai žinome, kaip užklausos yra apdorojamos LLM, pakalbėkime apie _kodėl_ mums reikia užklausų kūrimo. Atsakymas slypi tame, kad dabartiniai LLM kelia daugybę iššūkių, kurie daro _patikimus ir nuoseklius užbaigimus_ sunkiau pasiekiamus be pastangų užklausų kūrime ir optimizavime. Pavyzdžiui:

1. **Modelio atsakymai yra stochastiški.** _Ta pati užklausa_ greičiausiai duos skirtingus atsakymus su skirtingais modeliais ar modelio versijomis. Ir ji gali netgi duoti skirtingus rezultatus su _tuo pačiu modeliu_ skirtingu metu. _Užklausų kūrimo technikos gali padėti mums sumažinti šiuos skirtumus, suteikiant geresnes apsaugos priemones_.

1. **Modeliai gali kurti fiktyvius atsakymus.** Modeliai yra iš anksto apmokyti su _dideliais, bet ribotais_ duomenų rinkiniais, o tai reiškia, kad jie neturi žinių apie konceptus už mokymo ribų. Dėl to jie gali generuoti užbaigimus, kurie yra netikslūs, išgalvoti arba tiesiogiai prieštarauja žinomiems faktams. _Užklausų kūrimo technikos padeda vartotojams identifikuoti ir sumažinti tokias fikcijas, pvz., prašant AI pateikti citatas ar argumentus_.

1. **Modelių galimybės skiriasi.** Naujesni modeliai ar modelių kartos turės turtingesnes galimybes, bet taip pat atneš unikalių keistenybių ir kompromisų dėl kainos ir sudėtingumo. _Užklausų kūrimas gali padėti mums sukurti geriausias praktikas ir darbo eigas, kurios abstrahuoja skirtumus ir prisitaiko prie modelio specifinių reikalavimų mastu ir sklandžiai_.

Pažiūrėkime tai veiksme OpenAI arba Azure OpenAI Playground:

- Naud
Interneto paieška parodė, kad yra išgalvotų pasakojimų (pvz., televizijos serialų ar knygų) apie Marso karus, tačiau nė vienas jų nėra susijęs su 2076 metais. Sveikas protas taip pat sako, kad 2076 metai yra _ateityje_ ir todėl negali būti susiję su tikru įvykiu.

Taigi, kas nutinka, kai šį užklausą pateikiame skirtingiems LLM tiekėjams?

> **Atsakymas 1**: OpenAI Playground (GPT-35)

![Atsakymas 1](../../../translated_images/04-fabrication-oai.5818c4e0b2a2678c40e0793bf873ef4a425350dd0063a183fb8ae02cae63aa0c.lt.png)

> **Atsakymas 2**: Azure OpenAI Playground (GPT-35)

![Atsakymas 2](../../../translated_images/04-fabrication-aoai.b14268e9ecf25caf613b7d424c16e2a0dc5b578f8f960c0c04d4fb3a68e6cf61.lt.png)

> **Atsakymas 3**: Hugging Face Chat Playground (LLama-2)

![Atsakymas 3](../../../translated_images/04-fabrication-huggingchat.faf82a0a512789565e410568bce1ac911075b943dec59b1ef4080b61723b5bf4.lt.png)

Kaip ir tikėtasi, kiekvienas modelis (arba modelio versija) pateikia šiek tiek skirtingus atsakymus dėl stochastinio elgesio ir modelio galimybių skirtumų. Pavyzdžiui, vienas modelis orientuojasi į 8 klasės auditoriją, o kitas – į vidurinės mokyklos mokinius. Tačiau visi trys modeliai pateikė atsakymus, kurie galėtų įtikinti neinformuotą vartotoją, kad įvykis buvo tikras.

Tokios užklausų kūrimo technikos kaip _metaužklausos_ ir _temperatūros konfigūracija_ gali tam tikru mastu sumažinti modelio klaidingus atsakymus. Naujos užklausų kūrimo _architektūros_ taip pat sklandžiai integruoja naujus įrankius ir technikas į užklausų srautą, kad sumažintų arba pašalintų kai kuriuos šiuos efektus.

## Atvejo analizė: GitHub Copilot

Užbaikime šį skyrių, pažvelgdami, kaip užklausų kūrimas naudojamas realiuose sprendimuose, per vieną atvejo analizę: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot yra jūsų „AI porinis programuotojas“ – jis paverčia tekstines užklausas į kodo pasiūlymus ir yra integruotas į jūsų kūrimo aplinką (pvz., Visual Studio Code), kad užtikrintų sklandų vartotojo patirtį. Kaip dokumentuota žemiau pateiktuose tinklaraščiuose, ankstyviausia versija buvo pagrįsta OpenAI Codex modeliu – inžinieriai greitai suprato, kad reikia modelį pritaikyti ir sukurti geresnes užklausų kūrimo technikas, kad pagerintų kodo kokybę. Liepą jie [pristatė patobulintą AI modelį, kuris pranoksta Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst), siūlydamas dar greitesnius pasiūlymus.

Skaitykite įrašus iš eilės, kad galėtumėte sekti jų mokymosi kelią.

- **2023 m. gegužė** | [GitHub Copilot geriau supranta jūsų kodą](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **2023 m. gegužė** | [GitHub viduje: darbas su LLM, kurie yra GitHub Copilot pagrindas](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **2023 m. birželis** | [Kaip rašyti geresnes užklausas GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **2023 m. liepa** | [.. GitHub Copilot pranoksta Codex su patobulintu AI modeliu](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **2023 m. liepa** | [Programuotojo vadovas apie užklausų kūrimą ir LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **2023 m. rugsėjis** | [Kaip sukurti įmonės LLM programą: pamokos iš GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Taip pat galite naršyti jų [inžinerijos tinklaraštį](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) ir rasti daugiau įrašų, tokių kaip [šis](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), kuris parodo, kaip šie modeliai ir technikos _taikomi_ realių programų kūrimui.

---

<!--
LESSON TEMPLATE:
Ši dalis turėtų apimti pagrindinę sąvoką #2.
Sustiprinkite sąvoką pavyzdžiais ir nuorodomis.

SĄVOKA #2:
Užklausų dizainas.
Iliustruota pavyzdžiais.
-->

## Užklausų kūrimas

Jau supratome, kodėl užklausų kūrimas yra svarbus – dabar išsiaiškinkime, kaip užklausos _kuriamos_, kad galėtume įvertinti skirtingas technikas efektyvesniam užklausų dizainui.

### Paprasta užklausa

Pradėkime nuo paprastos užklausos: tekstinis įvestis, pateiktas modeliui be jokio papildomo konteksto. Štai pavyzdys – kai OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) pateikiame pirmuosius JAV nacionalinio himno žodžius, jis iškart _užbaigia_ atsakymą su kitomis eilutėmis, iliustruodamas pagrindinį prognozavimo elgesį.

| Užklausa (Įvestis) | Užbaigimas (Išvestis)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Panašu, kad pradedate JAV nacionalinio himno „The Star-Spangled Banner“ žodžius. Pilni žodžiai yra ... |

### Sudėtinga užklausa

Dabar pridėkime kontekstą ir instrukcijas prie paprastos užklausos. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) leidžia sukurti sudėtingą užklausą kaip _žinučių_ rinkinį su:

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

Ankstesniuose pavyzdžiuose vartotojo užklausa buvo paprasta tekstinė užklausa, kurią galima interpretuoti kaip informacijos prašymą. Naudojant _instrukcijų_ užklausas, galime naudoti tekstą, kad išsamiau nurodytume užduotį, suteikdami AI geresnes gaires. Štai pavyzdys:

| Užklausa (Įvestis)                                                                                                                                                                                                                         | Užbaigimas (Išvestis)                                                                                                        | Instrukcijos tipas  |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Parašykite aprašymą apie Pilietinį karą                                                                                                                                                                                                   | _grąžino paprastą pastraipą_                                                                                              | Paprasta            |
| Parašykite aprašymą apie Pilietinį karą. Pateikite pagrindines datas ir įvykius bei apibūdinkite jų reikšmę                                                                                                                                     | _grąžino pastraipą, po kurios pateiktas pagrindinių įvykių datų sąrašas su aprašymais_                                             | Sudėtinga           |
| Parašykite aprašymą apie Pilietinį karą vienoje pastraipoje. Pateikite 3 punktus su pagrindinėmis datomis ir jų reikšme. Pateikite dar 3 punktus su pagrindiniais istoriniais veikėjais ir jų indėliu. Grąžinkite išvestį JSON formatu | _grąžino išsamesnę informaciją teksto laukelyje, suformatuotą kaip JSON, kurį galite nukopijuoti į failą ir patikrinti pagal poreikį_ | Sudėtinga. Suformatuota. |

## Pagrindinis turinys

Ankstesniuose pavyzdžiuose užklausa vis dar buvo gana atvira, leidžianti LLM nuspręsti, kuri jo iš anksto apmokyto duomenų rinkinio dalis yra svarbi. Naudojant _pagrindinio turinio_ dizaino modelį, įvesties tekstas padalijamas į dvi dalis:

- instrukcija (veiksmas)
- svarbus turinys (kuris daro įtaką veiksmui)

Štai pavyzdys, kur instrukcija yra „apibendrinkite tai 2 sakiniais“.

| Užklausa (Įvestis)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Užbaigimas (Išvestis)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiteris yra penkta planeta nuo Saulės ir didžiausia Saulės sistemoje. Tai dujų milžinas, kurio masė yra tūkstantis kartų mažesnė nei Saulės, tačiau du su puse karto didesnė nei visų kitų planetų Saulės sistemoje kartu sudėjus. Jupiteris yra vienas ryškiausių objektų, matomų plika akimi naktiniame danguje, ir buvo žinomas senovės civilizacijoms dar prieš užrašytą istoriją. Jis pavadintas Romos dievo Jupiterio vardu. Žiūrint iš Žemės, Jupiteris gali būti pakankamai ryškus, kad jo atspindėta šviesa mestų matomus šešėlius, ir vidutiniškai yra trečias ryškiausias natūralus objektas naktiniame danguje po Mėnulio ir Veneros. <br/> **Apibendrinkite tai 2 trumpais sakiniais** | Jupiteris, penkta planeta nuo Saulės, yra didžiausia Saulės sistemoje ir žinoma kaip vienas ryškiausių objektų naktiniame danguje. Pavadintas Romos dievo Jupiterio vardu, tai dujų milžinas, kurio masė yra du su puse karto didesnė nei visų kitų planetų Saulės sistemoje kartu sudėjus. |

Pagrindinio turinio segmentas gali būti naudojamas įvairiais būdais, siekiant efektyvesnių instrukcijų:

- **Pavyzdžiai** – vietoj to, kad aiškiai nurodytumėte modeliui, ką daryti, pateikite jam pavyzdžių, ką daryti, ir leiskite jam išvesti modelį.
- **Užuominos** – po instrukcijos pateikite „užuominą“, kuri nukreipia užbaigimą, nukreipdama modelį į tinkamesnius atsakymus.
- **Šablonai** – tai pakartojami „receptai“ užklausoms su vietos rezervavimo ženklais (kintamaisiais), kuriuos galima pritaikyti duomenims konkretiems naudojimo atvejams.

Pažvelkime, kaip tai veikia praktikoje.

### Naudojant pavyzdžius

Tai metodas, kai naudojate pagrindinį turinį, kad „pamaitintumėte modelį“ keliais norimo atsakymo pavyzdžiais pagal pateiktą instrukciją ir leistumėte jam išvesti norimą atsakymo modelį. Atsižvelgiant į pateiktų pavyzdžių skaičių, galime turėti užklausas be pavyzdžių, su vienu pavyzdžiu, su keliais pavyzdžiais ir pan.

Užklausa dabar susideda iš trijų komponentų:

- Užduoties aprašymas
- Keletas norimo atsakymo pavyzdžių
- Naujo pavyzdžio pradžia (kuri tampa netiesioginiu užduoties aprašymu)

| Mokymosi tipas | Užklausa (Įvestis)                                                                                                                                        | Užbaigimas (Išvestis)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Be pavyzdžių  | „The Sun is Shining“. Išverskite į ispanų kalbą                                                                                                            | „El Sol está brillando“.    |
| Su vienu pavyzdžiu | „The Sun is Shining“ => „El Sol está brillando“. <br> „It's a Cold and Windy Day“ =>                                                                 | „Es un día frío y ventoso“. |
| Su keliais pavyzdžiais | Žaidėjas bėgo bazėmis => Beisbolas <br/> Žaidėjas pataikė į „ace“ => Tenisas <br/> Žaidėjas pataikė į „six“ => Kriketas <br/> Žaidėjas atliko „slam-dunk“ => | Krepšinis                  |
|               |                                                                                                                                                       |                             |

Atkreipkite dėmesį, kaip turėjome pateikti aiškią instrukciją („Išverskite į ispanų kalbą“) užklausose be pavyzdžių, tačiau ji tampa išvedama užklausose su vienu pavyzdžiu. Pavyzdys su keliais pavyzdžiais parodo, kaip pridėjus daugiau pavyzdžių modeliai gali tiksliau išvesti atsakymus be papildomų instrukcijų.

### Užklausų užuominos

Kitas pagrindinio turinio naudojimo būdas yra pateikti _užuominas_ vietoj pavyzdžių. Šiuo atveju mes suteikiame modeliui „postūmį“ tinkama kryptimi, _pradėdami_ atsakymą fragmentu, kuris atspindi norimą atsakymo formatą. Modelis tada „pagauna užuominą“ ir tęsia tuo pačiu stiliumi.

| Užuominų skaičius | Užklausa (Įvestis)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Užbaigimas (Išvestis)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiteris yra penkta planeta nuo Saulės ir didžiausia Saulės sistemoje. Tai dujų milžinas, kurio masė yra tūkstantis kartų mažesnė nei Saulės, tačiau du su puse karto didesnė nei visų kitų planetų Saulės sistemoje kartu sudėjus. Jupiteris yra vienas ryškiausių objektų, matomų plika akimi naktiniame danguje, ir buvo žinomas senovės civilizacijoms dar prieš užrašytą istoriją. <br/>**Apibendrinkite tai**                                       | Jupiteris yra didžiausia planeta mūsų Saulės sistemoje ir penkta nuo Saulės. Tai dujų milžinas, kurio masė yra 1/1000 Saulės masės, tačiau jis yra sunkesnis nei visos kitos planetos kartu sudėjus. Senovės civilizacijos jau seniai žinojo apie Jupiterį, ir jis lengvai matomas naktiniame danguje. |
| 1              | Jupiteris yra penkta planeta nuo Saulės ir didžiausia Saulės sistemoje. Tai dujų milžinas, kurio masė sudaro tik tūkstantąją Saulės masės dalį, tačiau yra du su puse karto didesnė už visų kitų planetų masę kartu sudėjus. Jupiteris yra vienas ryškiausių objektų, matomų plika akimi nakties danguje, ir buvo žinomas senovės civilizacijoms dar prieš užrašytą istoriją. <br/>**Apibendrinkite tai** <br/> Ką sužinojome apie Jupiterį | yra tai, kad jis yra penkta planeta nuo Saulės ir didžiausia Saulės sistemoje. Tai dujų milžinas, kurio masė sudaro tik tūkstantąją Saulės masės dalį, tačiau yra du su puse karto didesnė už visų kitų planetų masę kartu sudėjus. Jis lengvai matomas plika akimi ir buvo žinomas nuo senovės laikų.                        |
| 2              | Jupiteris yra penkta planeta nuo Saulės ir didžiausia Saulės sistemoje. Tai dujų milžinas, kurio masė sudaro tik tūkstantąją Saulės masės dalį, tačiau yra du su puse karto didesnė už visų kitų planetų masę kartu sudėjus. Jupiteris yra vienas ryškiausių objektų, matomų plika akimi nakties danguje, ir buvo žinomas senovės civilizacijoms dar prieš užrašytą istoriją. <br/>**Apibendrinkite tai** <br/> 3 svarbiausi faktai, kuriuos sužinojome:         | 1. Jupiteris yra penkta planeta nuo Saulės ir didžiausia Saulės sistemoje. <br/> 2. Tai dujų milžinas, kurio masė sudaro tik tūkstantąją Saulės masės dalį...<br/> 3. Jupiteris buvo matomas plika akimi nuo senovės laikų ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Šablonai užklausoms

Šablonas užklausai yra _iš anksto apibrėžtas receptas užklausai_, kurį galima išsaugoti ir naudoti pagal poreikį, siekiant užtikrinti nuoseklesnę vartotojo patirtį mastu. Paprasčiausia forma tai yra tiesiog užklausų pavyzdžių rinkinys, kaip [šis iš OpenAI](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst), kuris pateikia interaktyvius užklausos komponentus (vartotojo ir sistemos pranešimus) bei API valdomą užklausos formatą – palaikant pakartotinį naudojimą.

Sudėtingesnėje formoje, kaip [šis pavyzdys iš LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), jis turi _vietos rezervacijas_, kurias galima pakeisti duomenimis iš įvairių šaltinių (vartotojo įvestis, sistemos kontekstas, išoriniai duomenų šaltiniai ir kt.), kad užklausa būtų generuojama dinamiškai. Tai leidžia sukurti biblioteką pakartotinai naudojamų užklausų, kurios gali būti naudojamos nuoseklioms vartotojo patirtims **programiškai** mastu.

Galiausiai, tikroji šablonų vertė slypi galimybėje kurti ir publikuoti _užklausų bibliotekas_ vertikalioms taikymo sritims, kur užklausos šablonas yra _optimizuotas_, kad atspindėtų taikymo specifinį kontekstą ar pavyzdžius, kurie daro atsakymus labiau aktualius ir tikslius tiksliniam vartotojų auditorijai. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) saugykla yra puikus šio požiūrio pavyzdys, kurioje kaupiama užklausų biblioteka švietimo sričiai, akcentuojant pagrindinius tikslus, tokius kaip pamokų planavimas, mokymo programų kūrimas, mokinių konsultavimas ir kt.

## Papildomas turinys

Jei galvojame apie užklausos konstravimą kaip apie užduotį (instrukciją) ir tikslą (pagrindinį turinį), tuomet _antrinis turinys_ yra kaip papildomas kontekstas, kurį pateikiame, kad **paveiktume rezultatą tam tikru būdu**. Tai gali būti parametrų derinimas, formatavimo instrukcijos, temų taksonomijos ir kt., kurie gali padėti modelį _pritaikyti_ atsakymą, kad jis atitiktų norimus vartotojo tikslus ar lūkesčius.

Pavyzdžiui: Turint kursų katalogą su išsamiais metaduomenimis (pavadinimas, aprašymas, lygis, metaduomenų žymos, dėstytojas ir kt.) apie visus mokymo programos kursus:

- galime apibrėžti instrukciją „apibendrinkite kursų katalogą 2023 m. rudens semestrui“
- galime naudoti pagrindinį turinį, kad pateiktume keletą norimo rezultato pavyzdžių
- galime naudoti antrinį turinį, kad identifikuotume 5 svarbiausias „žymas“.

Dabar modelis gali pateikti santrauką formatu, parodytu keliuose pavyzdžiuose – tačiau jei rezultatas turi kelias žymas, jis gali teikti pirmenybę 5 žymoms, identifikuotoms antriniame turinyje.

---

<!--
ŠABLONAS PAMOKAI:
Ši dalis turėtų apimti pagrindinę sąvoką #1.
Sustiprinkite sąvoką pavyzdžiais ir nuorodomis.

SĄVOKA #3:
Užklausų inžinerijos technikos.
Kokios yra pagrindinės užklausų inžinerijos technikos?
Pateikite jas su pratimais.
-->

## Geriausios praktikos užklausoms

Dabar, kai žinome, kaip užklausos gali būti _kuriamos_, galime pradėti galvoti apie tai, kaip jas _projektuoti_, kad atspindėtų geriausias praktikas. Galime tai suskirstyti į dvi dalis – turėti tinkamą _mąstyseną_ ir taikyti tinkamas _technikas_.

### Užklausų inžinerijos mąstysena

Užklausų inžinerija yra bandymų ir klaidų procesas, todėl atkreipkite dėmesį į tris pagrindinius veiksnius:

1. **Domeno supratimas yra svarbus.** Atsakymo tikslumas ir aktualumas priklauso nuo _domeno_, kuriame veikia taikymas ar vartotojas. Taikykite savo intuiciją ir domeno žinias, kad **pritaikytumėte technikas**. Pavyzdžiui, apibrėžkite _domeno specifines asmenybes_ savo sistemos užklausose arba naudokite _domeno specifinius šablonus_ vartotojo užklausose. Pateikite antrinį turinį, kuris atspindi domeno specifinį kontekstą, arba naudokite _domeno specifinius signalus ir pavyzdžius_, kad nukreiptumėte modelį link pažįstamų naudojimo modelių.

2. **Modelio supratimas yra svarbus.** Žinome, kad modeliai yra stochastiški. Tačiau modelio įgyvendinimas gali skirtis pagal naudojamą mokymo duomenų rinkinį (iš anksto apmokėtas žinias), teikiamas galimybes (pvz., per API ar SDK) ir turinio tipą, kuriam jis optimizuotas (pvz., kodas, vaizdai, tekstas). Supraskite modelio, kurį naudojate, stipriąsias ir silpnąsias puses ir naudokite šias žinias, kad _prioritetizuotumėte užduotis_ arba sukurtumėte _pritaikytus šablonus_, optimizuotus modelio galimybėms.

3. **Iteracija ir validacija yra svarbios.** Modeliai greitai tobulėja, kaip ir užklausų inžinerijos technikos. Kaip domeno ekspertas, galite turėti kitą kontekstą ar kriterijus, kurie taikomi _jūsų_ specifinei taikymo sričiai, bet ne platesnei bendruomenei. Naudokite užklausų inžinerijos įrankius ir technikas, kad „pradėtumėte“ užklausų konstravimą, tada iteruokite ir validuokite rezultatus naudodami savo intuiciją ir domeno žinias. Užfiksuokite savo įžvalgas ir sukurkite **žinių bazę** (pvz., užklausų bibliotekas), kurią kiti galėtų naudoti kaip naują pagrindą greitesnėms iteracijoms ateityje.

## Geriausios praktikos

Dabar pažvelkime į bendras geriausias praktikas, kurias rekomenduoja [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) ir [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) specialistai.

| Kas                               | Kodėl                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Įvertinkite naujausius modelius.  | Naujos modelių kartos greičiausiai turės patobulintas funkcijas ir kokybę – tačiau gali būti ir brangesnės. Įvertinkite jų poveikį, tada priimkite migracijos sprendimus.                                                                            |
| Atskirti instrukcijas ir kontekstą| Patikrinkite, ar jūsų modelis/paslaugų teikėjas apibrėžia _skirtukus_, kad aiškiau atskirtų instrukcijas, pagrindinį ir antrinį turinį. Tai gali padėti modeliams tiksliau priskirti svorius žetonams.                                                         |
| Būkite konkretūs ir aiškūs        | Pateikite daugiau detalių apie norimą kontekstą, rezultatą, ilgį, formatą, stilių ir kt. Tai pagerins atsakymų kokybę ir nuoseklumą. Užfiksuokite receptus pakartotinai naudojamuose šablonuose.                                                          |
| Būkite aprašomi, naudokite pavyzdžius | Modeliai gali geriau reaguoti į „parodyk ir pasakyk“ metodą. Pradėkite nuo `zero-shot` metodo, kai pateikiate instrukciją (bet be pavyzdžių), tada pabandykite `few-shot` kaip patobulinimą, pateikdami keletą norimo rezultato pavyzdžių. Naudokite analogijas. |
| Naudokite signalus, kad pradėtumėte užbaigimus | Nukreipkite modelį link norimo rezultato, pateikdami keletą pradinių žodžių ar frazių, kurias jis gali naudoti kaip atsakymo pradžią.                                                                                                               |
| Kartokite                        | Kartais gali tekti pakartoti instrukcijas modeliui. Pateikite instrukcijas prieš ir po pagrindinio turinio, naudokite instrukciją ir signalą ir pan. Iteruokite ir validuokite, kad pamatytumėte, kas veikia.                                                         |
| Tvarka yra svarbi                | Informacijos pateikimo modeliui tvarka gali turėti įtakos rezultatui, net mokymosi pavyzdžiuose, dėl recency bias. Išbandykite skirtingas parinktis, kad pamatytumėte, kas veikia geriausiai.                                                               |
| Suteikite modeliui „išeitį“       | Pateikite modeliui _atsarginį_ atsakymą, kurį jis gali pateikti, jei dėl kokios nors priežasties negali atlikti užduoties. Tai gali sumažinti modelių klaidingų ar išgalvotų atsakymų tikimybę.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

Kaip ir bet kuri geriausia praktika, atminkite, kad _jūsų rezultatai gali skirtis_ priklausomai nuo modelio, užduoties ir domeno. Naudokite tai kaip pradžios tašką ir iteruokite, kad rastumėte, kas veikia geriausiai jums. Nuolat peržiūrėkite savo užklausų inžinerijos procesą, kai atsiranda nauji modeliai ir įrankiai, sutelkdami dėmesį į proceso mastelį ir atsakymų kokybę.

<!--
ŠABLONAS PAMOKAI:
Ši dalis turėtų pateikti kodavimo užduotį, jei taikoma.

UŽDUOTIS:
Nuoroda į Jupyter Notebook su tik kodų komentarais instrukcijose (kodo sekcijos tuščios).

SPRENDIMAS:
Nuoroda į Notebook kopiją su užpildytais ir paleistais užklausomis, parodant, kaip galėtų atrodyti vienas pavyzdys.
-->

## Užduotis

Sveikiname! Jūs pasiekėte pamokos pabaigą! Dabar laikas išbandyti kai kurias iš šių sąvokų ir technikų su realiais pavyzdžiais!

Mūsų užduočiai naudosime Jupyter Notebook su pratimais, kuriuos galite atlikti interaktyviai. Taip pat galite išplėsti Notebook su savo Markdown ir kodo langeliais, kad savarankiškai tyrinėtumėte idėjas ir technikas.

### Norėdami pradėti, fork'inkite saugyklą, tada

- (Rekomenduojama) Paleiskite GitHub Codespaces
- (Alternatyva) Klonuokite saugyklą į savo įrenginį ir naudokite ją su Docker Desktop
- (Alternatyva) Atidarykite Notebook su savo pasirinkta Notebook vykdymo aplinka.

### Toliau, sukonfigūruokite aplinkos kintamuosius

- Nukopijuokite `.env.copy` failą iš saugyklos šaknies į `.env` ir užpildykite `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` ir `AZURE_OPENAI_DEPLOYMENT` reikšmes. Grįžkite į [Mokymosi smėlio dėžės skyrių](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals), kad sužinotumėte, kaip.

### Toliau, atidarykite Jupyter Notebook

- Pasirinkite vykdymo branduolį. Jei naudojate 1 arba 2 parinktis, tiesiog pasirinkite numatytąjį Python 3.10.x branduolį, kurį pateikia kūrimo konteineris.

Jūs pasiruošę vykdyti pratimus. Atkreipkite dėmesį, kad čia nėra _teisingų ir neteisingų_ atsakymų – tiesiog tyrinėjame galimybes bandymų ir klaidų būdu, ugdydami intuiciją, kas veikia tam tikram modeliui ir taikymo sričiai.

_Dėl šios priežasties šioje pamokoje nėra kodų sprendimų segmentų. Vietoj to, Notebook turės Markdown langelius pavadinimu „Mano sprendimas:“, kurie parodys vieną pavyzdinį rezultatą kaip nuorodą._

 <!--
ŠABLONAS PAMOKAI:
Apibendrinkite skyrių ir pateikite išteklius savarankiškam mokymuisi.
-->

## Žinių patikrinimas

Kurios iš šių užklausų yra gera užklausa, atitinkanti pagrįstas geriausias praktikas?

1. Parodyk man raudono automobilio vaizdą
2. Parodyk man raudono automobilio vaizdą, Volvo markės ir XC90 modelio, stovintį prie uolos su besileidžiančia saule
3. Parodyk man raudono automobilio vaizdą, Volvo markės ir XC90 modelio

A: 2, tai geriausia užklausa, nes ji pateikia detales apie „ką“ ir yra konkreti (ne bet koks automobilis, o tam tikra markė ir modelis), taip pat aprašo bendrą aplinką. 3 yra antra geriausia, nes ji taip pat turi daug aprašymo.

## 🚀 Iššūkis

Pabandykite pasinaudoti „signalo“ technika su užklausa: Užbaikite sakinį „Parodyk man raudono automobilio vaizdą, Volvo markės ir “. Ką modelis atsako, ir kaip jūs tai patobulintumėte?

## Puikus darbas! Tęskite mokymąsi

Norite sužinoti daugiau apie skirtingas užklausų inžinerijos sąvokas? Eikite į [mokymosi tęstinumo puslapį](https://aka.ms/genai-collection?WT

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingą interpretaciją, atsiradusią dėl šio vertimo naudojimo.