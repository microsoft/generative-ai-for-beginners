# Prispevanje

Ta projekt sprejema prispevke in predloge. Večina prispevkov od vas zahteva,
da se strinjate z dogovorom o licenci za sodelovanje (CLA), ki izjavi, da imate pravico,
in dejansko podelite pravice za uporabo vašega prispevka. Za podrobnosti obiščite
<https://cla.microsoft.com>.

> Pomembno: pri prevajanju besedila v tem repozitoriju prosimo, da ne uporabljate strojnega prevajanja. Prevode bomo preverili s pomočjo skupnosti, zato prosimo, da se prevajanja lotite le v jezikih, v katerih ste usposobljeni.

Ko oddate pull request, bo CLA-bot samodejno ugotovil, ali morate
predložiti CLA, in primerno označil PR (npr. oznaka, komentar). Preprosto sledite
navodilom, ki jih zagotovi bot. To boste morali narediti samo enkrat za vse repozitorije, ki uporabljajo naš CLA.

## Kodeks ravnanja

Ta projekt je sprejel [Microsoftov odpiralni kodeks ravnanja](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst).
Za več informacij preberite [Pogosta vprašanja o kodeksu ravnanja](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) ali kontaktirajte [opencode@microsoft.com](mailto:opencode@microsoft.com) za dodatna vprašanja ali pripombe.

## Vprašanje ali težava?

Prosimo, da za splošna vprašanja o podpori ne odpirate težav (issues) na GitHubu, saj je GitHub seznam namenjen funkcijskim zahtevam in poročilom o napakah. Tako lahko lažje sledimo dejanskim težavam ali napakam v kodi in ločimo splošno razpravo od dejanske kode.

## Tipkarske napake, težave, napake in prispevki

Ko oddajate kakršnekoli spremembe v repozitorij Generative AI for Beginners, upoštevajte naslednja priporočila.

* Vedno pred spremembami naredite fork repozitorija na svoj račun
* Ne združujte več sprememb v en pull request. Na primer, za popravke napak in posodobitve dokumentacije pošljite ločene PR-je
* Če vaš pull request kaže konflikte združevanja, poskrbite, da bo vaš lokalni main odsev vsebine glavnega repozitorija, preden naredite spremembe
* Če oddajate prevod, ustvarite en PR za vse prevedene datoteke, saj ne sprejemamo delnih prevodov vsebine
* Če oddajate popravke tipkarskih napak ali dokumentacije, lahko po potrebi združite spremembe v en PR

## Uredniški obseg in izdelki tretjih oseb

Ta učni načrt se osredotoča na Microsoftove tehnologije in nevtralne odprte standarde. Prispevki morajo imeti jasen izobraževalni namen in ne smejo biti namenjeni predvsem uvajanju ali promociji komercialnega izdelka tretje osebe, gostujoče storitve, modelskega usmerjevalnika, SDK-ja, MCP strežnika ali drugega ponudnika.

Programska oprema z odprto kodo in odvisnosti tretjih oseb so lahko omenjene, kadar so potrebne za pojasnitev odprtega standarda ali scenarija interoperabilnosti, predstavljene nevtralno in ne osredotočeno na izdelke ali storitve določenega ponudnika. Če vaš predlagani prispevek vključuje izdelek ali storitev določenega ponudnika, odprite temo in pridobite odobritev vzdrževalca pred oddajo pull requesta.

Prispevki morajo razkriti vse ustrezne zaposlitve, lastništvo, sponzorstvo ali druge povezave z izdelkom ali storitvijo, omenjenimi v njihovem prispevku. Ne vključujte nepodprtih trditev o cenah, zmogljivosti, varnosti, zasebnosti ali primerjavah. Zaželeni primeri ne smejo privzeto prenašati podatkov uporabnikov ali izvajati javnih dejanj prek zunanjih storitev tretjih oseb.

## Splošna navodila za pisanje

- Poskrbite, da so vsi vaši URL-ji zaviti v oglate oklepaje, za njimi pa sledi okrogla oklepaja brez dodatnih presledkov okoli ali znotraj njih `[]()`.
- Zagotovite, da se vsaka relativna povezava (tj. povezave do drugih datotek in map v repozitoriju) začne z `./`, ki se nanaša na datoteko ali mapo, ki se nahaja v trenutni delovni mapi, ali `../`, ki se nanaša na datoteko ali mapo, ki se nahaja v nadrejeni delovni mapi.
- Zagotovite, da ima vsaka relativna povezava (tj. povezave do drugih datotek in map v repozitoriju) na koncu svoje sledilni ID (tj. `?` ali `&` nato `wt.mc_id=` ali `WT.mc_id=`).
- Zagotovite, da ima vsak URL iz naslednjih domen _github.com, microsoft.com, visualstudio.com, aka.ms in azure.com_ na koncu svoje sledilni ID (tj. `?` ali `&` nato `wt.mc_id=` ali `WT.mc_id=`).
- Zagotovite, da vaše povezave nimajo lokalizacije, specifične za državo (tj. `/en-us/` ali `/en/`).
- Zagotovite, da so vse slike shranjene v mapi `./images`.
- Zagotovite, da imajo slike opisna imena z uporabo angleških črk, številk in vezajev v imenu vaše slike.

## GitHub delovni tokovi

Ko oddate pull request, se sprožijo štirje različni delovni tokovi za preverjanje prejšnjih pravil.
Preprosto sledite navodilom, navedenim tukaj, da opravite preverjanja delovnega toka.

- [Check Broken Relative Paths](#check-broken-relative-paths)
- [Check Paths Have Tracking](#check-paths-have-tracking)
- [Check URLs Have Tracking](#check-urls-have-tracking)
- [Check URLs Don't Have Locale](#check-urls-dont-have-locale)

### Preveri pokvarjene relativne poti

Ta delovni tok zagotavlja, da vsaka relativna pot v vaših datotekah deluje.
Ta repozitorij je nameščen na GitHub pages, zato morate biti zelo previdni, ko vnašate povezave, ki vse skupaj povezujejo, da nikogar ne usmerite na napačno mesto.

Za zagotovitev, da vaše povezave pravilno delujejo, preprosto uporabite VS code za preverjanje.

Na primer, ko premaknete kazalec miške nad katero koli povezavo v vaših datotekah, boste pozvani, da sledite povezavi z **ctrl + klikom**.

![VS code follow links screenshot](../../translated_images/sl/vscode-follow-link.85520ab6a1237adc.webp?WT.mc_id=academic-105485-koreyst "Posnetek zaslona iz vs code poziva, da sledite povezavi, ko se premaknete nad povezavo.")

Če kliknete povezavo in ne deluje lokalno, bo delovni tok zagotovo sprožen in ne bo deloval na GitHubu.

Za odpravo te težave poskusite povezavo vnesti s pomočjo VS code.

Ko vnesete `./` ali `../`, vas bo VS code pozval, da izberete med razpoložljivimi možnostmi glede na to, kar ste vnesli.

![VS code select relative path screenshot](../../translated_images/sl/vscode-select-relative-path.3804eb73c3a9e5f2.webp?WT.mc_id=academic-105485-koreyst "Posnetek zaslona iz vs code poziva, da izberete relativno pot iz pojavnega seznama.")

Sledite poti s klikom na želeno datoteko ali mapo in boste prepričani, da vaša pot ni pokvarjena.

Ko dodate pravilno relativno pot, shranite in potisnete spremembe, bo delovni tok znova sprožen, da preveri vaše spremembe.
Če opravite preverjanje, ste pripravljeni za nadaljevanje.

### Preveri, da poti imajo sledilni ID

Ta delovni tok zagotavlja, da ima vsaka relativna pot v sebi sledilni ID.
Ta repozitorij je nameščen na GitHub Pages, zato moramo slediti premikom med različnimi datotekami in mapami.

Da zagotovite, da imajo vaše relativne poti v sebi sledenje, preprosto preverite naslednje besedilo `?wt.mc_id=` na koncu poti.
Če je dodano vašim relativnim potezam, boste opravili ta pregled.

Če ne, boste morda dobili naslednjo napako.

![GitHub check paths missing tracking comment screenshot](../../translated_images/sl/github-check-paths-missing-tracking-comment.880d4afe03e898ff.webp?WT.mc_id=academic-105485-koreyst "Posnetek zaslona iz komentarja na githubu, ki prikazuje manjkajoče sledenje pri relativnih potezah")

Za odpravo te težave poskusite odpreti pot do datoteke, ki jo je delovni tok označil, in dodajte ID sledenja na konec relativnih poti.

Ko dodate ID sledenja, shranite in potisnite svoje spremembe, delovni tok bo znova sprožen, da preveri vaše spremembe.
Če opravite pregled, ste pripravljeni za nadaljevanje.

### Preverite, ali URL-ji vsebujejo sledenje

Ta delovni tok zagotavlja, da vsak spletni URL vsebuje sledenje.
Ta repozitorij je dostopen vsem, zato morate zagotoviti, da sledite dostopom, da boste vedeli, od kod prihaja promet.

Da zagotovite, da imajo vaši URL-ji sledenje, preprosto preverite za naslednje besedilo `?wt.mc_id=` na koncu URL-ja.
Če je dodano vašim URL-jem, boste opravili ta pregled.

Če ne, boste morda dobili naslednjo napako.

![GitHub check urls missing tracking comment screenshot](../../translated_images/sl/github-check-urls-missing-tracking-comment.1bd00d20b24a1e2e.webp?WT.mc_id=academic-105485-koreyst "Posnetek zaslona iz komentarja na githubu, ki prikazuje manjkajoče sledenje pri URL-jih")

Za odpravo te težave poskusite odpreti pot do datoteke, ki jo je delovni tok označil, in dodajte ID sledenja na konec URL-jev.

Ko dodate ID sledenja, shranite in potisnite svoje spremembe, delovni tok bo znova sprožen, da preveri vaše spremembe.
Če opravite pregled, ste pripravljeni za nadaljevanje.

### Preverite, ali URL-ji nimajo lokalizacije države

Ta delovni tok zagotavlja, da noben spletni URL ne vsebuje lokalizacije specifične za državo.
Ta repozitorij je dostopen vsem po svetu, zato morate zagotoviti, da v URL-jih ni lokalizacije vaše države.

Da zagotovite, da vaš URL nima lokalizacije države, preprosto preverite za naslednje besedilo `/en-us/` ali `/en/` ali katerokoli drugo jezikovno lokalizacijo kjerkoli v URL-ju.
Če tega ni v vaših URL-jih, boste opravili ta pregled.

Če ne, boste morda dobili naslednjo napako.

![GitHub check country locale comment screenshot](../../translated_images/sl/github-check-country-locale-comment.2f4fe93228161dee.webp?WT.mc_id=academic-105485-koreyst "Posnetek zaslona iz komentarja na githubu, ki prikazuje dodano lokalizacijo države v URL-jih")

Za odpravo te težave poskusite odpreti pot do datoteke, ki jo je delovni tok označil, in odstranite lokalizacijo države iz URL-jev.

Ko odstranite lokalizacijo države, shranite in potisnite svoje spremembe, delovni tok bo znova sprožen, da preveri vaše spremembe.
Če opravite pregled, ste pripravljeni za nadaljevanje.

Čestitamo! Odzvali se bomo takoj, ko bo mogoče, s povratnimi informacijami o vašem prispevku.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->