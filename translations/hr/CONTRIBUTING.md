# Doprinos

Ovaj projekt pozdravlja doprinose i prijedloge. Većina doprinosa zahtijeva da
se slažete s Ugovorom o licenci za doprinos (CLA) kojim izjavljujete da imate pravo,
i doista dajete, pravo korištenja vašeg doprinosa. Za detalje posjetite
<https://cla.microsoft.com>.

> Važno: prilikom prevođenja teksta u ovom spremištu molimo osigurajte da ne koristite strojno prevođenje. Prevode ćemo provjeravati putem zajednice, stoga volontirajte samo za prijevode jezika kojima dobro upravljate.

Kada pošaljete zahtjev za povlačenje, CLA-bot će automatski utvrditi trebate li
osigurati CLA i prikladno označiti PR (npr. oznakom, komentarom). Jednostavno slijedite
upute koje daje bot. Ovo ćete morati učiniti samo jednom za sva spremišta koja koriste naš CLA.

## Kodeks ponašanja

Ovaj projekt je usvojio [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst).
Za više informacija pročitajte [FAQ o Kodeksu ponašanja](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) ili kontaktirajte [opencode@microsoft.com](mailto:opencode@microsoft.com) za dodatna pitanja ili komentare.

## Pitanje ili problem?

Molimo vas da ne otvarate GitHub probleme za opća pitanja podrške jer GitHub lista treba služiti za zahtjeve za funkcionalnosti i prijave grešaka. Na taj način lakše pratimo stvarne probleme i greške u kodu i držimo opću raspravu odvojeno od samog koda.

## Pravopisne pogreške, problemi, greške i doprinosi

Kad god podnosite bilo kakve promjene u spremištu Generative AI for Beginners, molimo vas da slijedite ove preporuke.

* Uvijek napravi fork spremišta na svoj račun prije nego što napravite izmjene
* Nemoj spajati više promjena u jedan zahtjev za povlačenje. Na primjer, podnesite ispravke grešaka i ažuriranja dokumentacije u zasebnim PR-ovima
* Ako vaš zahtjev za povlačenje prikazuje sukobe pri spajanju, obavezno ažurirajte svoj lokalni main kao zrcalo onoga što je u glavnom spremištu prije izmjena
* Ako podnosite prijevod, molimo napravite jedan PR za sve prevedene datoteke budući da ne prihvaćamo djelomične prijevode sadržaja
* Ako podnosite ispravak pravopisne pogreške ili dokumentacije, možete kombinirati izmjene u jedan PR gdje je prikladno

## Urednički opseg i proizvodi trećih strana

Ovaj kurikulum fokusira se na Microsoftove tehnologije i vendor-neutralne otvorene standarde. Doprinosi trebaju imati jasnu obrazovnu svrhu i ne smiju biti prvenstveno namijenjeni za predstavljanje ili promicanje komercijalnog proizvoda treće strane, hostirane usluge, model routera, SDK-a, MCP servera ili druge ponudbe specifične za prodavača.

Softver otvorenog koda i ovisnosti trećih strana mogu se spominjati kada su potrebni za objašnjenje otvorenog standarda ili scenarija interoperabilnosti, predstavljeni neutralno i ne fokusiraju se na proizvod ili hostiranu točku prodavača. Ako vaš predloženi doprinos uključuje proizvod ili uslugu specifičnu za određenu tvrtku, otvorite problem i zatražite odobrenje održavatelja prije podnošenja zahtjeva za povlačenje.

Doprinositelji moraju otkriti bilo kakav relevantan odnos zaposlenja, vlasništva, sponzorstva ili drugu povezanost s proizvodom ili uslugom spomenutom u njihovom doprinosu. Ne uključujte neutemeljene tvrdnje o cijenama, performansama, sigurnosti, privatnosti ili usporedne tvrdnje. Izvršni primjeri ne smiju prema zadanim postavkama prenositi podatke o polaznicima ili izvršavati javne radnje putem vanjske usluge treće strane.

## Opće smjernice za pisanje

- Osigurajte da svi vaši URL-ovi budu u uglatim zagradama praćenima zagradama bez dodatnih razmaka oko ili unutar njih `[]()`.
- Osigurajte da svaki relativni link (tj. linkovi na druge datoteke i mape u spremištu) započinje s `./` koji se odnosi na datoteku ili mapu u trenutnom radnom direktoriju ili `../` koji se odnosi na datoteku ili mapu u roditeljskom radnom direktoriju.
- Osigurajte da svaki relativni link (tj. linkovi na druge datoteke i mape u spremištu) ima ID za praćenje (tj. `?` ili `&` pa zatim `wt.mc_id=` ili `WT.mc_id=`) na kraju.
- Osigurajte da bilo koji URL s domena _github.com, microsoft.com, visualstudio.com, aka.ms, i azure.com_ ima ID za praćenje (tj. `?` ili `&` pa zatim `wt.mc_id=` ili `WT.mc_id=`) na kraju.
- Osigurajte da vaši linkovi nemaju lokalizaciju specifičnu za državu (tj. `/en-us/` ili `/en/`).
- Osigurajte da su sve slike pohranjene u mapi `./images`.
- Osigurajte da slike imaju opisna imena koristeći engleske znakove, brojeve i crtice u nazivu slike.

## GitHub tijekovi rada

Kada pošaljete zahtjev za povlačenje, pokrenut će se četiri različita tijeka rada za provjeru prethodnih pravila.
Jednostavno slijedite upute navedene ovdje da biste prošli provjere tijeka rada.

- [Provjera slomljenih relativnih putanja](#check-broken-relative-paths)
- [Provjera da putanje imaju praćenje](#check-paths-have-tracking)
- [Provjera da URL-ovi imaju praćenje](#check-urls-have-tracking)
- [Provjera da URL-ovi nemaju lokalizaciju](#check-urls-dont-have-locale)

### Provjera slomljenih relativnih putanja

Ovaj tijek rada osigurava da svaka relativna putanja u vašim datotekama radi ispravno.
Ovo spremište je postavljeno na GitHub pages pa morate biti vrlo pažljivi kada upisujete linkove koji povezuju sve zajedno da ne usmjerite nikoga na pogrešno mjesto.

Da biste bili sigurni da vam linkovi ispravno rade, jednostavno upotrijebite VS code za provjeru.

Na primjer, kada prijeđete mišem preko bilo kojeg linka u datotekama, bit ćete upitani da slijedite link pritiskom na **ctrl + klik**

![VS code screenshot za praćenje linkova](../../translated_images/hr/vscode-follow-link.85520ab6a1237adc.webp?WT.mc_id=academic-105485-koreyst "Prikaz VS code upita za praćenje linka pri prelasku mišem.")

Ako kliknete na link i ne radi lokalno, sigurno će tijek rada prijaviti grešku i neće raditi na GitHubu.

Da biste riješili ovaj problem, pokušajte upisati link pomoću VS code.

Kada upišete `./` ili `../`, VS code će vas potaknuti da odaberete iz dostupnih opcija prema onome što ste upisali.

![VS code screenshot za izbor relativne putanje](../../translated_images/hr/vscode-select-relative-path.3804eb73c3a9e5f2.webp?WT.mc_id=academic-105485-koreyst "Prikaz VS code upita za izbor relativne putanje iz pojavljene liste.")

Slijedite put klikom na željenu datoteku ili mapu i bit ćete sigurni da vaša putanja nije slomljena.

Kad dodate ispravnu relativnu putanju, spremite i gurnite promjene, tijek rada će ponovno biti pokrenut da potvrdi izmjene.
Ako prođete provjeru, možete nastaviti dalje.

### Provjera da putanje imaju praćenje

Ovaj tijek rada osigurava da svaka relativna putanja ima u sebi praćenje.
Ovo spremište je postavljeno na GitHub pages pa moramo pratiti kretanje između različitih datoteka i mapa.

Da biste bili sigurni da vaše relativne putanje imaju praćenje, jednostavno provjerite je li na kraju putanje prisutan tekst `?wt.mc_id=`.
Ako je dodan vašim relativnim putanjama, proći ćete ovu provjeru.

Ako nije, mogli biste dobiti sljedeću pogrešku.

![GitHub komentar provjere putanja bez praćenja](../../translated_images/hr/github-check-paths-missing-tracking-comment.880d4afe03e898ff.webp?WT.mc_id=academic-105485-koreyst "Prikaz GitHub komentara koji pokazuje nedostatak praćenja kod relativnih putanja")

Da biste riješili ovaj problem, otvorite putanju datoteke koju je tijek rada označio i dodajte ID za praćenje na kraj relativnih putanja.

Nakon što dodate ID za praćenje, spremite i gurnite promjene, tijek rada će ponovno biti pokrenut da potvrdi izmjene.
Ako prođete provjeru, možete nastaviti dalje.

### Provjera da URL-ovi imaju praćenje

Ovaj tijek rada osigurava da svaki web URL ima u sebi praćenje.
Ovo spremište je dostupno svima pa morate biti sigurni da pratite pristupe da biste znali odakle promet dolazi.

Da biste bili sigurni da vaši URL-ovi imaju praćenje, jednostavno provjerite je li na kraju URL-a prisutan tekst `?wt.mc_id=`.
Ako je dodan vašim URL-ovima, proći ćete ovu provjeru.

Ako nije, mogli biste dobiti sljedeću pogrešku.

![GitHub komentar provjere URL-ova bez praćenja](../../translated_images/hr/github-check-urls-missing-tracking-comment.1bd00d20b24a1e2e.webp?WT.mc_id=academic-105485-koreyst "Prikaz GitHub komentara koji pokazuje nedostatak praćenja kod URL-ova")

Da biste riješili ovaj problem, otvorite putanju datoteke koju je tijek rada označio i dodajte ID za praćenje na kraj URL-ova.

Nakon što dodate ID za praćenje, spremite i gurnite promjene, tijek rada će ponovno biti pokrenut da potvrdi izmjene.
Ako prođete provjeru, možete nastaviti dalje.

### Provjera da URL-ovi nemaju lokalizaciju

Ovaj tijek rada osigurava da ni jedan web URL nema lokalizaciju specifičnu za državu.
Ovo spremište je dostupno svima u svijetu pa morate biti sigurni da ne uključujete lokalizaciju vaše države u URL-ove.

Da biste bili sigurni da vaši URL-ovi nemaju lokalizaciju države, jednostavno provjerite nema li u URL-u tekst `/en-us/` ili `/en/` ili bilo koju drugu jezičnu lokalizaciju.
Ako nije prisutna u vašim URL-ovima, proći ćete ovu provjeru.

Ako jest, mogli biste dobiti sljedeću pogrešku.

![GitHub komentar provjere URL-a s lokalizacijom države](../../translated_images/hr/github-check-country-locale-comment.2f4fe93228161dee.webp?WT.mc_id=academic-105485-koreyst "Prikaz GitHub komentara koji pokazuje dodanu lokalizaciju države u URL-ovima")

Da biste riješili ovaj problem, otvorite putanju datoteke koju je tijek rada označio i uklonite lokalizaciju države iz URL-ova.

Nakon uklanjanja lokalizacije države, spremite i gurnite promjene, tijek rada će ponovno biti pokrenut da potvrdi izmjene.
Ako prođete provjeru, možete nastaviti dalje.

Čestitamo! Javili ćemo vam se što prije s povratnim informacijama o vašem doprinosu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->