# Doprinos

Ovaj projekt prihvaća doprinose i prijedloge. Većina doprinosa zahtijeva da vi
pristajete na Ugovor o licenci za suradnike (CLA) kojim izjavljujete da imate pravo,
i zapravo dajete, prava da koristimo vaš doprinos. Za detalje, posjetite
<https://cla.microsoft.com>.

> Važno: prilikom prevođenja teksta u ovom repozitoriju, molimo vas da ne koristite strojno prevođenje. Prijevode ćemo provjeravati putem zajednice, stoga se volontirajte samo za prijevode na jezicima u kojima ste vješti.

Kada podnesete zahtjev za promjenu (pull request), bot za CLA automatski će utvrditi treba li vam
CLA i prikazat će odgovarajuću oznaku ili komentar na PR. Jednostavno slijedite
upute koje daje bot. Ovo ćete trebati učiniti samo jednom za sve repozitorije koji koriste naš CLA.

## Kodeks ponašanja

Ovaj projekt usvojio je [Microsoft Open Source Kodeks ponašanja](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst).
Za više informacija pročitajte [FAQ o Kodeksu ponašanja](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) ili kontaktirajte [opencode@microsoft.com](mailto:opencode@microsoft.com) za dodatna pitanja ili komentare.

## Pitanje ili problem?

Molimo ne otvarajte pitanja putem GitHub issues za opće podrške jer se popis na GitHubu treba koristiti za zahtjeve za značajkama i prijave bugova. Na ovaj način možemo lakše pratiti stvarne probleme ili bugove u kodu i držati opću raspravu odvojenu od samog koda.

## Pravopisne greške, problemi, bugovi i doprinosi

Kad god podnosite bilo kakve izmjene u repozitoriju Generative AI for Beginners, molimo pridržavajte se ovih preporuka.

* Uvijek prvo forkajte repozitorij na svoj račun prije nego što napravite izmjene
* Nemojte kombinirati više izmjena u jedan pull request. Na primjer, prijavite ispravke bugova i ažuriranja dokumentacije koristeći zasebne PR-ove
* Ako vaš pull request pokazuje sukobe prilikom spajanja, pobrinite se da ažurirate lokalnu glavnu granu da bude ogledalo onoga što je u glavnom repozitoriju prije izvođenja izmjena
* Ako podnosite prijevod, napravite jedan PR za sve prevedene datoteke jer ne prihvaćamo djelomične prijevode sadržaja
* Ako podnosite ispravak pravopisne greške ili dokumentacije, možete kombinirati izmjene u jedan PR gdje je to prikladno

## Urednički opseg i proizvodi trećih strana

Ovaj kurikulum fokusira se na Microsoft tehnologije i neutralne otvorene standarde. Doprinosi trebaju služiti jasnoj edukacijskoj svrsi i ne smiju prvenstveno biti namijenjeni uvođenju ili promicanju proizvoda trećih strana, hostirane usluge, model routera, SDK-a, MCP servera ili druge ponude specifične za dobavljača.

Softver otvorenog koda i ovisnosti trećih strana mogu se spomenuti kada su nužni za objašnjenje otvorenog standarda ili scenarija interoperabilnosti, prikazuju se neutralno te nisu usredotočeni na proizvod ili hostanu točku dobavljača. Ako vaš predloženi doprinos uključuje proizvod ili uslugu specifičnu za dobavljača, otvorite issue i zatražite odobrenje održavatelja prije podnošenja pull requesta.

Suradnici moraju otkriti svaku relevantnu zaposlenost, vlasništvo, sponzorstvo ili drugo povezivanje s proizvodom ili uslugom spomenutom u njihovom doprinosu. Nemojte uključivati nepotvrđene tvrdnje o cijenama, performansama, sigurnosti, privatnosti ili usporedbe. Izvedivi primjeri ne smiju prema zadanim postavkama prenositi podatke učenika niti obavljati javne akcije putem vanjske usluge treće strane.

## Opće smjernice za pisanje

- Osigurajte da su svi vaši URL-ovi obavijeni u uglate zagrade koje slijede obične zagrade bez dodatnih razmaka oko ili unutar njih `[]()`.
- Osigurajte da svaki relativni link (npr. linkovi na druge datoteke i mape u repozitoriju) započinje s `./` koji upućuje na datoteku ili mapu u trenutnom radnom direktoriju ili `../` koji upućuje na datoteku ili mapu u roditeljskom radnom direktoriju.
- Osigurajte da svaki relativni link (npr. linkovi na druge datoteke i mape u repozitoriju) ima ID praćenja (npr. `?` ili `&` zatim `wt.mc_id=` ili `WT.mc_id=`) na njegovom kraju.
- Osigurajte da svaki URL s domena _github.com, microsoft.com, visualstudio.com, aka.ms i azure.com_ ima ID praćenja (npr. `?` ili `&` zatim `wt.mc_id=` ili `WT.mc_id=`) na svom kraju.
- Osigurajte da vaši linkovi nemaju lokalnu oznaku jezika (npr. `/en-us/` ili `/en/`).
- Osigurajte da su sve slike pohranjene u mapu `./images`.
- Osigurajte da slike imaju opisna imena koristeći engleske znakove, brojeve i crtice u nazivu slike.

## GitHub tijekovi rada

Kad podnesete pull request, četiri različita tijeka rada (workflowa) bit će pokrenuta kako bi se provjerila prethodna pravila.
Jednostavno slijedite upute navedene ovdje da biste prošli provjere tijeka rada.

- [Provjeri ispravnost relativnih putanja](#check-broken-relative-paths)
- [Provjeri imaju li putanje ID praćenja](#check-paths-have-tracking)
- [Provjeri imaju li URL-ovi ID praćenja](#check-urls-have-tracking)
- [Provjeri da URL-ovi nemaju lokalnu oznaku](#check-urls-dont-have-locale)

### Provjera ispravnosti relativnih putanja

Ovaj tijek rada osigurava da svaka relativna putanja u vašim datotekama funkcionira.
Ovaj repozitorij je implementiran na GitHub stranicama, stoga morate biti oprezni kada upisujete linkove koji povezuju sve kako nikoga ne biste usmjerili na pogrešnu destinaciju.

Da biste provjerili rade li vaši linkovi ispravno, jednostavno koristite VS Code za provjeru.

Na primjer, kada zadržite pokazivač iznad bilo kojeg linka u vašim datotekama, bit će vam ponuđeno da slijedite link pritiskom na **ctrl + klik**

![VS code follow links screenshot](../../translated_images/hr/vscode-follow-link.85520ab6a1237adc.webp?WT.mc_id=academic-105485-koreyst "Screenshot iz vs code s promptom za praćenje linka kad zadržite pokazivač iznad linka.")

Ako kliknete na link i on ne radi lokalno, sigurno će izazvati grešku u tijeku rada i neće raditi na GitHubu.

Da biste riješili ovaj problem, pokušajte napisati link uz pomoć VS Codea.

Kad upišete `./` ili `../`, VS Code će vam ponuditi izbor prema onome što ste upisali.

![VS code select relative path screenshot](../../translated_images/hr/vscode-select-relative-path.3804eb73c3a9e5f2.webp?WT.mc_id=academic-105485-koreyst "Screenshot iz vs code s promptom za odabir relativne putanje s popisa.")

Slijedite putanju klikom na željenu datoteku ili mapu i bit ćete sigurni da vaša putanja nije prekinuta.

Nakon što dodate ispravnu relativnu putanju, spremite i gurnite promjene, tijek rada će se ponovno pokrenuti da provjeri vaše izmjene.
Ako prođete provjeru, spremni ste za nastavak.

### Provjera imaju li putanje ID praćenja

Ovaj tijek rada osigurava da svaka relativna putanja sadrži ID praćenja.
Ovaj repozitorij je implementiran na GitHub stranicama pa moramo pratiti kretanje između različitih datoteka i mapa.

Da biste osigurali da vaše relativne putanje sadrže ID praćenja, jednostavno provjerite da li imaju sljedeći tekst `?wt.mc_id=` na kraju putanje.
Ako je pridodano vašim relativnim putevima, tada ćete proći ovu provjeru.

Ako nije, može se pojaviti sljedeća pogreška.

![GitHub check paths missing tracking comment screenshot](../../translated_images/hr/github-check-paths-missing-tracking-comment.880d4afe03e898ff.webp?WT.mc_id=academic-105485-koreyst "Screenshot iz komentara na GitHubu koji prikazuje nedostatak praćenja u relativnim putovima")

Da biste riješili ovaj problem, pokušajte otvoriti put do datoteke koju je radni tijek naveo i dodajte ID za praćenje na kraj relativnih putova.

Kada dodate ID za praćenje, spremite i gurnite svoje promjene, radni će se tijek ponovno pokrenuti kako bi verificirao vaše promjene.
Ako prođete provjeru, tada ste spremni za nastavak.

### Provjeri da URL-ovi imaju praćenje

Ovaj radni tijek osigurava da svaki web URL sadrži praćenje.
Ovaj repozitorij je dostupan svima pa morate osigurati praćenje pristupa kako biste znali odakle promet dolazi.

Za provjeru da vaši URL-ovi imaju praćenje, jednostavno provjerite postoji li sljedeći tekst `?wt.mc_id=` na kraju URL-a.
Ako je pridodano vašim URL-ovima, tada ćete proći ovu provjeru.

Ako nije, može se pojaviti sljedeća pogreška.

![GitHub check urls missing tracking comment screenshot](../../translated_images/hr/github-check-urls-missing-tracking-comment.1bd00d20b24a1e2e.webp?WT.mc_id=academic-105485-koreyst "Screenshot iz komentara na GitHubu koji prikazuje nedostatak praćenja u URL-ovima")

Da biste riješili ovaj problem, pokušajte otvoriti put do datoteke koju je radni tijek označio i dodajte ID za praćenje na kraj URL-ova.

Nakon što dodate ID za praćenje, spremite i gurnite svoje promjene, radni će se tijek ponovno pokrenuti kako bi verificirao vaše promjene.
Ako prođete provjeru, tada ste spremni za nastavak.

### Provjeri da URL-ovi nemaju lokaciju

Ovaj radni tijek osigurava da nijedan web URL ne sadrži lokalizaciju specifičnu za zemlju.
Ovaj repozitorij je dostupan svima diljem svijeta, pa morate osigurati da ne uključujete lokalizaciju svoje zemlje u URL-ove.

Za provjeru da vaši URL-ovi nemaju lokalizaciju zemlje, jednostavno provjerite postoji li sljedeći tekst `/en-us/` ili `/en/` ili bilo koja druga jezična lokalizacija bilo gdje u URL-u.
Ako nije prisutna u vašim URL-ovima, tada ćete proći ovu provjeru.

Ako jest, može se pojaviti sljedeća pogreška.

![GitHub check country locale comment screenshot](../../translated_images/hr/github-check-country-locale-comment.2f4fe93228161dee.webp?WT.mc_id=academic-105485-koreyst "Screenshot iz komentara na GitHubu koji prikazuje dodanu lokalizaciju zemlje u URL-ove")

Da biste riješili ovaj problem, pokušajte otvoriti put do datoteke koju je radni tijek označio i uklonite lokalizaciju zemlje iz URL-ova.

Nakon što uklonite lokalizaciju zemlje, spremite i gurnite svoje promjene, radni će se tijek ponovno pokrenuti kako bi verificirao vaše promjene.
Ako prođete provjeru, tada ste spremni za nastavak.

Čestitamo! Javili smo vam se što je prije moguće sa povratnim informacijama o vašem doprinosu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->