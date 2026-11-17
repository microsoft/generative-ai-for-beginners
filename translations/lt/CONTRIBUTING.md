# Dalyvavimas

Šis projektas džiaugiasi prisidėjimais ir pasiūlymais. Daugumai prisidėjimų reikalinga
sutikti su Bendradarbiautojo licencijos sutartimi (CLA), kurioje patvirtinate, kad turite teisę,
ir iš tiesų suteikiate mums teises naudoti jūsų prisidėjimą. Daugiau informacijos rasite
<https://cla.microsoft.com>.

> Svarbu: verčiant tekstą šiame saugykloje, prašome nenaudoti mašininio vertimo. Vertimus patikrins bendruomenė, todėl prašome savanoriauti tik vertimams kalbomis, kuriose esate įgudę.

Kai pateikiate pull request, CLA-botas automatiškai nustatys, ar jums reikia
pateikti CLA ir tinkamai pažymės PR (pvz., etikete ar komentaru). Tiesiog vykdykite
bot'o nurodymus. Tai reikės padaryti tik vieną kartą visuose mūsų CLA naudojančiuose saugyklose.

## Elgesio kodeksas

Šis projektas priėmė [Microsoft atviro kodo elgesio kodeksą](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst).
Daugiau informacijos rasite [Elgesio kodekso DUK](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) arba susisiekite su [opencode@microsoft.com](mailto:opencode@microsoft.com) dėl papildomų klausimų ar komentarų.

## Klausimas ar problema?

Prašome neatidaryti GitHub problemų bendrosioms pagalbos užklausoms, nes GitHub sąrašas yra skirtas funkcijų prašymams ir klaidų pranešimams. Taip galime lengviau sekti tikras problemas ar klaidas kode ir išlaikyti bendrą diskusiją atskirą nuo tikrojo kodo.

## Rašybos klaidos, problemos, klaidos ir prisidėjimai

Kai pateikiate bet kokius pakeitimus Generative AI for Beginners saugykloje, prašome laikytis šių rekomendacijų.

* Visada forkuokite saugyklą į savo paskyrą prieš darydami pakeitimus
* Nekomplektuokite kelių pakeitimų į vieną pull request. Pavyzdžiui, atskirai pateikite klaidų taisymus ir dokumentacijos atnaujinimus
* Jei jūsų pull request rodo susijungimo konfliktus, įsitikinkite, kad atnaujinote savo vietinę main šaką taip, kad ji atspindėtų pagrindinę saugyklą prieš darydami pakeitimus
* Jei pateikiate vertimą, prašome sukurti vieną PR visiems išverstiems failams, nes nepriimame dalinių vertimų turiniui
* Jei pataisote rašybos klaidą ar dokumentaciją, galite, jei tinka, sujungti pakeitimus į vieną PR

## Redakcijos apimtis ir trečiųjų šalių produktai

Ši programa skirta Microsoft technologijoms ir tiekėjams neutraliesiems atviro standarto sprendimams. Prisidėjimai turi turėti aiškų mokomąjį tikslą ir neturi būti pirminiai tam, kad būtų pristatytas ar reklamintas trečiosios šalies komercinis produktas, talpinama paslauga, modelių maršrutizatorius, SDK, MCP serveris ar kitas tiekėjo pasiūlymas.

Atviro kodo programinė įranga ir trečiųjų šalių priklausomybės gali būti minima, kai jos būtinos paaiškinti atvirą standartą ar sąveikos scenarijų, pateikiamos neutraliai ir nėra skiriamos vien tik tiekėjo produktui ar prieglobos galiniam taškui. Jei jūsų siūlomas prisidėjimas apima tiekėjo produktą ar paslaugą, atidarykite klausimą ir gaukite prižiūrėtojo patvirtinimą prieš pateikdami pull request.

Dalyviai privalo atskleisti bet kokius susijusius darbo santykius, nuosavybę, rėmimą ar kitokį ryšį su produku ar paslauga, paminėta jų prisidėjime. Neįtraukite nepagrįstų kainų, veikimo, saugumo, privatumo ar palyginamųjų teiginių. Veikiantys pavyzdžiai pagal nutylėjimą neturi perduoti mokymosi duomenų ar atlikti viešų veiksmų per išorinę trečiosios šalies paslaugą.

## Bendrosios rašymo gairės

- Užtikrinkite, kad visi jūsų URL būtų įtraukti į kvadratines skliausteles, po kurių eina skliaustai be tarpų aplink arba viduje jų `[]()`.
- Užtikrinkite, kad bet kuris santykinis ryšys (t.y. ryšiai į kitus failus ir aplankus saugykloje) prasidėtų `./`, nurodančiu failą ar aplanką dabartinėje darbinėje aplanko vietoje, arba `../`, nurodančiu failą ar aplanką tėviniame darbinės vietos aplanke.
- Užtikrinkite, kad bet kuris santykinis ryšys (t.y. ryšiai į kitus failus ir aplankus saugykloje) turi turėti sekimo ID (t.y. `?` arba `&`, po kurių eina `wt.mc_id=` arba `WT.mc_id=`) gale.
- Užtikrinkite, kad bet kuris URL iš šių domenų _github.com, microsoft.com, visualstudio.com, aka.ms, ir azure.com_ turi turėti sekimo ID (t.y. `?` arba `&`, po kurių eina `wt.mc_id=` arba `WT.mc_id=`) gale.
- Užtikrinkite, kad jūsų nuorodos neturėtų šalies specifinio lokalės žymėjimo (t.y. `/en-us/` arba `/en/`).
- Užtikrinkite, kad visi paveikslėliai būtų saugomi `./images` aplanke.
- Užtikrinkite, kad paveikslėliai turėtų aprašomuosius pavadinimus, naudodami anglų kalbos simbolius, skaičius ir brūkšnelius savo paveikslėlio pavadinime.

## GitHub darbo procesai

Kai pateikiate pull request, bus paleisti keturi skirtingi darbo procesai, patikrinantys ankstesnes taisykles.
Tiesiog vykdykite čia išvardytas instrukcijas, kad pereitumėte darbo proceso patikrinimus.

- [Patikrinti sugadintus santykinius kelius](#check-broken-relative-paths)
- [Patikrinti, ar keliai turi sekimą](#check-paths-have-tracking)
- [Patikrinti, ar URL turi sekimą](#check-urls-have-tracking)
- [Patikrinti, ar URL neturi lokalės](#check-urls-dont-have-locale)

### Patikrinti sugadintus santykinius kelius

Šis darbo procesas užtikrina, kad bet kuris santykinis kelias jūsų failuose veikia.
Ši saugykla yra išdėstyta GitHub tinklalapiuose, todėl turite būti labai atsargūs rašydami nuorodas, kurios viską sujungia, kad niekas nebūtų nukreiptas klaidingai.

Kad įsitikintumėte, jog jūsų nuorodos veikia, tiesiog naudokite VS kodą, kad tai patikrintumėte.

Pvz., kai užvedate pelės žymeklį ant bet kurios nuorodos savo failuose, jums bus pasiūlyta sekti nuorodą paspaudžiant **ctrl + click**

![VS code follow links screenshot](../../translated_images/lt/vscode-follow-link.85520ab6a1237adc.webp?WT.mc_id=academic-105485-koreyst "Ekrano nuotrauka iš vs code, pasiūlanti sekti nuorodą, kai užvedate pelės žymeklį ant nuorodos.")

Jei paspausite nuorodą ir ji neveikia vietoje, tada tikrai darbo procesas bus įjungtas ir ji neveiks GitHub.

Norėdami išspręsti šią problemą, pabandykite rašyti nuorodą naudodamiesi VS kodu.

Kai įvedate `./` arba `../`, VS kodas pasiūlys pasirinkti iš galimų variantų pagal tai, ką įvedėte.

![VS code select relative path screenshot](../../translated_images/lt/vscode-select-relative-path.3804eb73c3a9e5f2.webp?WT.mc_id=academic-105485-koreyst "Ekrano nuotrauka iš vs code, pasiūlanti pasirinkti santykinį kelią iš iškylančio sąrašo.")

Sekite kelią spustelėdami norimą failą ar aplanką ir būsite tikri, kad jūsų kelias nėra sulaužytas.

Kai pridėsite teisingą santykinį kelią, išsaugokite ir įkelkite savo pakeitimus, darbo procesas vėl bus įjungtas patikrinti jūsų pakeitimus.
Jei patikrinimą išlaikysite, viskas tvarkoje.

### Patikrinti, ar keliai turi sekimą

Šis darbo procesas užtikrina, kad bet kuris santykinis kelias turi sekimą.
Ši saugykla yra paskelbta GitHub tinklalapiuose, todėl turime sekti judėjimą tarp skirtingų failų ir aplankų.

Kad įsitikintumėte, jog jūsų santykiniai keliai turi sekimą, tiesiog patikrinkite šį tekstą `?wt.mc_id=` kelio pabaigoje.
Jei jis pridėtas prie jūsų santykinių kelių, patikrą praeisite.

Jei ne, galite gauti šią klaidą.

![GitHub check paths missing tracking comment screenshot](../../translated_images/lt/github-check-paths-missing-tracking-comment.880d4afe03e898ff.webp?WT.mc_id=academic-105485-koreyst "Ekrano nuotrauka iš github komentaro, rodanti, kad trūksta sekimo santykiniuose keliuose")

Norėdami išspręsti šią problemą, atidarykite darbo proceso pažymėtą failo kelią ir pridėkite sekimo ID prie santykinių kelių pabaigos.

Kai pridėsite sekimo ID, išsaugokite ir įkelkite pakeitimus, darbo procesas vėl bus įjungtas patikrinti jūsų pakeitimus.
Jei patikrinimą išlaikysite, viskas tvarkoje.

### Patikrinti, ar URL turi sekimą

Šis darbo procesas užtikrina, kad bet kuris interneto URL turi sekimą.
Ši saugykla yra prieinama visiems, todėl turite užtikrinti prieigos sekimą, kad žinotumėte, iš kur ateina srautas.

Kad įsitikintumėte, jog jūsų URL turi sekimą, tiesiog patikrinkite šį tekstą `?wt.mc_id=` URL pabaigoje.
Jei jis pridėtas prie jūsų URL, patikrą praeisite.

Jei ne, galite gauti šią klaidą.

![GitHub check urls missing tracking comment screenshot](../../translated_images/lt/github-check-urls-missing-tracking-comment.1bd00d20b24a1e2e.webp?WT.mc_id=academic-105485-koreyst "Ekrano nuotrauka iš github komentaro, rodanti, kad trūksta sekimo URL")

Norėdami išspręsti šią problemą, atidarykite darbo proceso pažymėtą failo kelią ir pridėkite sekimo ID prie URL pabaigos.

Kai pridėsite sekimo ID, išsaugokite ir įkelkite pakeitimus, darbo procesas vėl bus įjungtas patikrinti jūsų pakeitimus.
Jei patikrinimą išlaikysite, viskas tvarkoje.

### Patikrinti, ar URL neturi lokalės

Šis darbo procesas užtikrina, kad bet kuris interneto URL neturi šalies specifinio lokalės žymėjimo.
Ši saugykla yra prieinama visiems pasaulyje, todėl turite užtikrinti, kad URL nepatektų jūsų šalies lokalės.

Kad įsitikintumėte, jog URL neturi šalies lokalės, patikrinkite, ar nėra šio teksto `/en-us/` arba `/en/` ar bet kuri kita kalbos lokalė URL bet kurioje vietoje.
Jei tai nerasta jūsų URL, patikrą praeisite.

Jei yra, galite gauti šią klaidą.

![GitHub check country locale comment screenshot](../../translated_images/lt/github-check-country-locale-comment.2f4fe93228161dee.webp?WT.mc_id=academic-105485-koreyst "Ekrano nuotrauka iš github komentaro, rodanti pridėtą šalies lokalę į URL")

Norėdami išspręsti šią problemą, atidarykite darbo proceso pažymėtą failo kelią ir pašalinkite šalies lokalę iš URL.

Kai pašalinsite šalies lokalę, išsaugokite ir įkelkite pakeitimus, darbo procesas vėl bus įjungtas patikrinti jūsų pakeitimus.
Jei patikrinimą išlaikysite, viskas tvarkoje.

Sveikiname! Mes su jumis susisieksime kuo greičiau su atsiliepimais apie jūsų prisidėjimą.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->