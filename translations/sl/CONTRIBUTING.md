# Prispevanje

Ta projekt vabi k prispevkom in predlogom. Večina prispevkov zahteva, da
se strinjate z dogovorom o licenci za prispevke (CLA), ki izjavlja, da imate pravico,
in dejansko dajete pravice za uporabo vašega prispevka. Za podrobnosti obiščite
<https://cla.microsoft.com>.

> Pomembno: pri prevajanju besedila v tem repozitoriju, prosim zagotovite, da ne uporabljate strojnega prevajanja. Prevajanja bomo preverili preko skupnosti, zato se prijavite za prevajanja samo za jezike, ki jih obvladate.

Ko oddate pull request, bo bot CLA samodejno določil, ali morate
zagotoviti CLA in ustrezno označiti PR (npr. z nalepko, komentarjem). Preprosto sledite
navodilom bota. To boste morali narediti samo enkrat v vseh repozitorijih, ki uporabljajo naš CLA.

## Kodeks ravnanja

Ta projekt je sprejel [Microsoftov kodeks ravnanja za odprtokodne projekte](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst).
Za več informacij preberite [Pogosta vprašanja o kodeksu ravnanja](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) ali kontaktirajte [opencode@microsoft.com](mailto:opencode@microsoft.com) za dodatna vprašanja ali komentarje.

## Vprašanje ali težava?

Prosim, da ne odpirate GitHub vprašanj za splošna podporna vprašanja, saj naj se GitHub seznam uporablja za zahteve funkcij in prijave napak. Tako bomo lažje spremljali dejanske težave ali napake v kodi in ločili splošno razpravo od dejanske kode.

## Tipkarske napake, težave, napake in prispevki

Kadar koli oddajate spremembe v repozitorij Generative AI for Beginners, upoštevajte naslednja priporočila.

* Vedno najprej forkajte repozitorij v svoj račun, preden naredite spremembe
* Ne združujte več sprememb v en pull request. Na primer, za popravke napak in posodobitve dokumentacije oddajte ločene PR-je
* Če vaš pull request kaže na konflikte združitve, poskrbite, da bo vaš lokalni main posodobljen, da bo zrcalil glavni repozitorij, preden naredite spremembe
* Če oddajate prevod, prosim ustvarite en PR za vse prevedene datoteke, saj ne sprejemamo delnih prevodov vsebine
* Če oddajate popravke tipkarskih napak ali dokumentacije, lahko združite spremembe v en PR, kjer je to primerno

## Uredniški obseg in izdelki tretjih oseb

Ta učni načrt se osredotoča na Microsoftove tehnologije in neodvisne odprte standarde. Prispevki morajo imeti jasen izobraževalni namen in ne smejo biti namenjeni predvsem uvajanju ali promoviranju komercialnega izdelka tretje osebe, gostovane storitve, modela usmerjevalnika, SDK-ja, MCP strežnika ali druge ponudbe specifične za določenega ponudnika.

Odprtokodna programska oprema in odvisnosti tretjih oseb se lahko navezujejo, kadar so potrebni za razlago odprtega standarda ali scenarija interoperabilnosti, so predstavljeni nevtralno in niso osredotočeni na izdelek ali gostujočo točko ponudnika. Če vaš predlagani prispevek vključuje izdelek ali storitev specifično za določeno podjetje, odprite vprašanje in pridobite odobritev vzdrževalca pred oddajo pull requesta.

Prispevalci morajo razkriti kakršno koli ustrezno zaposlitev, lastništvo, sponzorstvo ali drugo povezavo z izdelkom ali storitvijo, na katero se sklicujejo v svojem prispevku. Ne vključujte nepodprtih trditev o cenah, zmogljivostih, varnosti, zasebnosti ali primerjalnih navedb. Izvedljivi primeri ne smejo privzeto prenašati podatkov udeležencev ali izvajati javnih dejanj preko zunanje storitve tretje osebe.

## Splošna navodila za pisanje

- Poskrbite, da so vsi vaši URL-ji oviti v oglate oklepaje, sledijo pa jim okrogli oklepaji brez dodatnih presledkov okoli ali znotraj njih `[]()`.
- Poskrbite, da vsak relativni povezavi (t.j. povezave do drugih datotek in map v repozitoriju) začne z `./`, ki se nanaša na datoteko ali mapo v trenutni delovni mapi, ali z `../`, ki se nanaša na datoteko ali mapo v nadrejeni delovni mapi.
- Poskrbite, da ima vsaka relativna povezava (t.j. povezave do drugih datotek in map v repozitoriju) sledilno oznako (t.j. `?` ali `&` nato `wt.mc_id=` ali `WT.mc_id=`) na koncu.
- Poskrbite, da ima katerikoli URL iz naslednjih domen _github.com, microsoft.com, visualstudio.com, aka.ms, in azure.com_ sledilno oznako (t.j. `?` ali `&` nato `wt.mc_id=` ali `WT.mc_id=`) na koncu.
- Poskrbite, da vaše povezave nimajo v sebi lokalizacije za posamezno državo (t.j. `/en-us/` ali `/en/`).
- Poskrbite, da so vse slike shranjene v mapi `./images`.
- Poskrbite, da imajo slike opisna imena, uporabljajo angleške znake, številke in pomišljaje v imenu slike.

## GitHub delovni poteki

Ko oddate pull request, bodo sproženi štirje različni delovni poteki za preverjanje zgornjih pravil.
Preprosto sledite navodilom tukaj, da opravite preverjanja delovnih tokov.

- [Preveri pokvarjene relativne poti](#check-broken-relative-paths)
- [Preveri, da imajo poti sledilno oznako](#check-paths-have-tracking)
- [Preveri, da imajo URL-ji sledilno oznako](#check-urls-have-tracking)
- [Preveri, da URL-ji nimajo lokalizacije](#check-urls-dont-have-locale)

### Preveri pokvarjene relativne poti

Ta delovni tok zagotavlja, da katerakoli relativna pot v vaših datotekah deluje.
Ta repozitorij je nameščen na GitHub strani, zato morate biti zelo previdni, ko vnašate povezave, da nikogar ne usmerite na napačno mesto.

Da zagotovite, da vaše povezave pravilno delujejo, preprosto uporabite VS code za preverjanje.

Na primer, ko se postavite z miško nad katerokoli povezavo v vaših datotekah, se vam bo ponudila možnost s pritiskom na **ctrl + klik** slediti povezavi

![Posnetek zaslona VS code za sledenje povezavam](../../translated_images/sl/vscode-follow-link.85520ab6a1237adc.webp?WT.mc_id=academic-105485-koreyst "Posnetek zaslona iz vs code poziva za sledenje povezavi, ko se postavite z miško nad povezavo.")

Če kliknete povezavo in ta ne deluje lokalno, bo to zagotovo sprožilo delovni tok in ne bo delovalo na GitHubu.

Za rešitev te težave poskusite povezavo vnesti s pomočjo VS code.

Ko vnesete `./` ali `../`, vam bo VS code ponudil izbiro iz razpoložljivih možnosti glede na to, kar ste vnesli.

![Posnetek zaslona VS code izbire relativne poti](../../translated_images/sl/vscode-select-relative-path.3804eb73c3a9e5f2.webp?WT.mc_id=academic-105485-koreyst "Posnetek zaslona iz vs code poziva za izbiro relativne poti iz pojavnega seznama.")

Sledite poti s klikom na željeno datoteko ali mapo in boste gotovi, da vaša pot ni pokvarjena.

Ko dodate pravilno relativno pot, shranite in potisnite svoje spremembe, delovni tok bo znova sprožen, da preveri spremembe.
Če uspešno prestanete preverjanje, ste pripravljeni za nadaljevanje.

### Preveri, da imajo poti sledilno oznako

Ta delovni tok zagotavlja, da ima katerakoli relativna pot v sebi sledilno oznako.
Ta repozitorij je nameščen na GitHub strani, zato moramo slediti premikanju med različnimi datotekami in mapami.

Da zagotovite, da imajo vaše relativne poti sledilno oznako, preprosto preverite, ali se na koncu poti nahaja besedilo `?wt.mc_id=`.
Če je dodano vašim relativnim potem, boste prestali to preverjanje.

Če ne, boste morda prejeli naslednjo napako.

![Posnetek zaslona github komentarja o manjkajoči sledilni oznaki na relativnih poteh](../../translated_images/sl/github-check-paths-missing-tracking-comment.880d4afe03e898ff.webp?WT.mc_id=academic-105485-koreyst "Posnetek zaslona github komentarja, ki prikazuje manjkajočo sledilno oznako na relativnih poteh")

Za rešitev te težave poskusite odpret datotečno pot, ki jo je delovni tok označil, in dodajte sledilno oznako na koncu relativnih poti.

Ko dodate sledilno oznako, shranite in potisnite svoje spremembe, delovni tok bo znova sprožen, da preveri spremembe.
Če uspešno prestanete preverjanje, ste pripravljeni za nadaljevanje.

### Preveri, da imajo URL-ji sledilno oznako

Ta delovni tok zagotavlja, da ima katerikoli spletni URL v sebi sledilno oznako.
Ta repozitorij je na voljo vsem, zato morate zagotoviti sledenje dostopa, da veste, od kod prihaja promet.

Da zagotovite, da imajo vaši URL-ji sledilno oznako, preprosto preverite, ali se na koncu URL-ja nahaja besedilo `?wt.mc_id=`.
Če je dodano vašim URL-jem, boste prestali to preverjanje.

Če ne, boste morda prejeli naslednjo napako.

![Posnetek zaslona github komentarja o manjkajoči sledilni oznaki na URL-jih](../../translated_images/sl/github-check-urls-missing-tracking-comment.1bd00d20b24a1e2e.webp?WT.mc_id=academic-105485-koreyst "Posnetek zaslona github komentarja, ki prikazuje manjkajočo sledilno oznako na url-jih")

Za rešitev te težave poskusite odpret datotečno pot, ki jo je delovni tok označil, in dodajte sledilno oznako na koncu URL-jev.

Ko dodate sledilno oznako, shranite in potisnite svoje spremembe, delovni tok bo znova sprožen, da preveri spremembe.
Če uspešno prestanete preverjanje, ste pripravljeni za nadaljevanje.

### Preveri, da URL-ji nimajo lokalizacije

Ta delovni tok zagotavlja, da katerikoli spletni URL nima v sebi lokalizacije za posamezno državo.
Ta repozitorij je na voljo vsem po svetu, zato morate paziti, da ne vključite lokalizacije vaše države v URL-je.

Da zagotovite, da vaši URL-ji nimajo lokalizacije države, preprosto preverite, ali se v URL-ju nahaja besedilo `/en-us/` ali `/en/` ali katerakoli druga lokalizacija jezika.
Če v vaših URL-jih ni prisotno, boste prestali to preverjanje.

Če ne, boste morda prejeli naslednjo napako.

![Posnetek zaslona github komentarja o dodani lokalizaciji države v URL-jih](../../translated_images/sl/github-check-country-locale-comment.2f4fe93228161dee.webp?WT.mc_id=academic-105485-koreyst "Posnetek zaslona github komentarja, ki prikazuje dodano lokalizacijo države v url-jih")

Za rešitev te težave poskusite odpret datotečno pot, ki jo je delovni tok označil, in odstranite lokalizacijo države iz URL-jev.

Ko odstranite lokalizacijo države, shranite in potisnite svoje spremembe, delovni tok bo znova sprožen, da preveri spremembe.
Če uspešno prestanete preverjanje, ste pripravljeni za nadaljevanje.

Čestitamo! Oglasili se bomo čim prej s povratnimi informacijami o vašem prispevku.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->