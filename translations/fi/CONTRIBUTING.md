# Osallistuminen

Tämä projekti toivottaa tervetulleeksi panokset ja ehdotukset. Useimpiin panoksiin vaaditaan, että hyväksyt
osallistujan lisenssisopimuksen (CLA), jossa ilmoitat, että sinulla on oikeus
ja todella annat meille oikeudet käyttää panostasi. Lisätietoja löydät osoitteesta
<https://cla.microsoft.com>.

> Tärkeää: kun käännät tekstiä tässä arkistossa, varmista, että et käytä konekäännöstä. Tarkistamme käännökset yhteisön avulla, joten vapaaehtoiseksi voi ryhtyä vain kielissä, joissa olet taitava.

Kun lähetät pull-pyynnön, CLA-botti määrittää automaattisesti, tarvitsetko
toimittaa CLA:n ja lisää pyynnölle siihen liittyvät merkinnät (esim. tunniste, kommentti). Noudata vain
botin antamia ohjeita. Tämä on tarpeen vain kerran kaikissa CLA:ta käyttävissä arkistoissa.

## Käyttäytymissäännöt

Tämä projekti on ottanut käyttöön [Microsoftin avoimen lähdekoodin käyttäytymissäännöt](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst).
Lisätietoja löydät [käyttäytymissääntöjen UKK:sta](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) tai ota yhteyttä osoitteeseen [opencode@microsoft.com](mailto:opencode@microsoft.com) lisäkysymyksissä tai kommenteissa.

## Kysymys tai ongelma?

Älä avaa GitHub-ongelmia yleisiin tukikysymyksiin, sillä GitHubin lista on tarkoitettu ominaisuuspyyntöihin ja vikaraportteihin. Näin voimme helpommin seurata varsinaisia koodiongelmia tai vikoja ja pitää yleisen keskustelun erillään varsinaisesta koodista.

## Kirjoitusvirheet, ongelmat, virheet ja panokset

Kun toimitat muutoksia Generative AI for Beginners -arkistoon, noudata näitä suosituksia.

* Tee aina haarukka (fork) arkistosta omaan tiliisi ennen muokkausten tekemistä
* Älä yhdistä useita muutoksia yhteen pull-pyyntöön. Esimerkiksi lähetä bugikorjaukset ja dokumentaatiopäivitykset erillisillä PR:llä
* Jos pull-pyyntösi näyttää olevan ristiriidassa yhdistämisen (merge) kanssa, varmista että paikallinen main-haarasi on päivitetty vastaamaan pääarkistoa ennen muokkausten tekemistä
* Jos toimitat käännöstä, tee yksi PR kaikista käännetyistä tiedostoista, sillä emme hyväksy osittaisia käännöksiä sisällöstä
* Jos toimitat kirjoitusvirheen tai dokumentaatiokorjauksen, voit yhdistää muutokset yhteen PR:ään, jos se sopii

## Toiminnallinen laajuus ja kolmannen osapuolen tuotteet

Tämä opetussuunnitelma keskittyy Microsoftin teknologioihin ja toimittajaneutraaleihin avoimiin standardeihin. Panosten tulee palvella selkeää opetustarkoitusta, eikä niiden saa ensisijaisesti olla tarkoitettu kolmannen osapuolen kaupallisen tuotteen, isännöidyn palvelun, mallireitittimen, SDK:n, MCP-palvelimen tai muun toimittajakohtaisen tarjouksen esittelemiseksi tai mainostamiseksi.

Avoimen lähdekoodin ohjelmistoja ja kolmannen osapuolen riippuvuuksia voidaan viitata silloin, kun ne ovat tarpeen avoimen standardin tai yhteentoimivuustilanteen selittämiseksi, ne esitetään neutraalisti eikä keskittyen toimittajan tuotteeseen tai palveluun. Jos ehdotuksesi sisältää toimittajakohtaisen tuotteen tai palvelun, avaa ensin issue ja hanki ylläpitäjän hyväksyntä ennen pull-pyynnön lähettämistä.

Panosten tekijöiden on ilmoitettava mahdolliset merkitykselliset työsuhteet, omistajuudet, sponsoroinnit tai muut yhteydet panoksessa mainittuun tuotteeseen tai palveluun. Älä sisällytä perusteettomia hintaan, suorituskykyyn, turvallisuuteen, yksityisyyteen tai vertailuun liittyviä väitteitä. Suoritettavat esimerkit eivät saa oletuksena lähettää opiskelijadataa tai suorittaa julkisia toimintoja ulkoisen kolmannen osapuolen palvelun kautta.

## Yleisten kirjoitusohjeiden noudattaminen

- Varmista, että kaikki URL-osoitteet ovat hakasulkeissa ja niiden perässä sulut ilman ylimääräisiä välilyöntejä niiden ympärillä tai sisällä `[]()`.
- Varmista, että kaikki suhteelliset linkit (esim. linkit muihin tiedostoihin ja kansioihin arkistossa) alkavat merkinnällä `./`, joka viittaa nykyisessä työhakemistossa olevaan tiedostoon tai kansioon, tai `../`, joka viittaa emohakemiston tiedostoon tai kansioon.
- Varmista, että kaikissa suhteellisissa linkeissä (esim. linkit muihin tiedostoihin ja kansioihin arkistossa) on seuranta-ID (esim. `?` tai `&`, sitten `wt.mc_id=` tai `WT.mc_id=`) linkin lopussa.
- Varmista, että kaikilla seuraavien verkkotunnusten URL-osoitteilla _github.com, microsoft.com, visualstudio.com, aka.ms ja azure.com_ on seuranta-ID (esim. `?` tai `&`, sitten `wt.mc_id=` tai `WT.mc_id=`) linkin lopussa.
- Varmista, ettei linkeissäsi ole maakohtaista alueasetusta (esim. `/en-us/` tai `/en/`).
- Varmista, että kaikki kuvat tallennetaan `./images`-kansioon.
- Varmista, että kuvat nimeät kuvaavasti käyttäen englanninkielisiä merkkejä, numeroita ja viivoja kuvatiedoston nimessä.

## GitHub-työnkulut

Kun lähetät pull-pyynnön, neljä erilaista työnkulkua käynnistyy tarkistamaan yllä olevia sääntöjä.
Noudata yksinkertaisesti täällä annettuja ohjeita työnkulun tarkistusten läpäisemiseksi.

- [Tarkista rikkinäiset suhteelliset polut](#check-broken-relative-paths)
- [Tarkista, että poluissa on seurannan tunniste](#check-paths-have-tracking)
- [Tarkista, että URL-osoitteissa on seuranta](#check-urls-have-tracking)
- [Tarkista, ettei URL-osoitteissa ole alueasetusta](#check-urls-dont-have-locale)

### Tarkista rikkinäiset suhteelliset polut

Tämä työnkulku varmistaa, että tiedostoissasi olevat kaikki suhteelliset polut toimivat.
Tämä arkisto julkaistaan GitHub Pages -sivustolla, joten sinun tulee olla erittäin tarkka, kun kirjoitat linkkejä, jotta kukaan ei ohjaudu väärään paikkaan.

Varmistaaksesi linkkien toimivuuden käytä vain VS Codea tarkistukseen.

Esimerkiksi kun viet hiiren osoittimen minkä tahansa tiedostosi linkin päälle, saat kehotteen seurata linkkiä painamalla **ctrl + klikkaus**

![VS code seuraa linkkejä -kuvakaappaus](../../translated_images/fi/vscode-follow-link.85520ab6a1237adc.webp?WT.mc_id=academic-105485-koreyst "Kuvakaappaus VS Coden kehotteesta seurata linkkiä, kun viet hiiren osoittimen linkin päälle.")

Jos napsautat linkkiä ja se ei toimi paikallisesti, työnkulku varmasti laukaistaan eikä se toimi GitHubissa.

Korjataksesi ongelman, yritä kirjoittaa linkki VS Coden avustuksella.

Kun kirjoitat `./` tai `../`, VS Code ehdottaa valittavia vaihtoehtoja kirjoituksesi perusteella.

![VS code valitse suhteellinen polku -kuvakaappaus](../../translated_images/fi/vscode-select-relative-path.3804eb73c3a9e5f2.webp?WT.mc_id=academic-105485-koreyst "Kuvakaappaus VS Coden kehotteesta valita suhteellinen polku ponnahdusvalikosta.")

Seuraa polkua napsauttamalla haluttua tiedostoa tai kansiota, niin voit olla varma, ettei polkusi ole rikkinäinen.

Kun lisäät oikean suhteellisen polun, tallenna ja lähetä muutoksesi, työnkulku käynnistyy uudelleen tarkistamaan muutokset.
Jos läpäiset tarkistuksen, voit jatkaa.

### Tarkista, että poluissa on seuranta

Tämä työnkulku varmistaa, että kaikissa suhteellisissa poluissa on seuranta.
Tämä arkisto julkaistaan GitHub Pagesissa, joten meidän on seurattava tiedostojen ja kansioiden liikettä.

Varmista, että suhteellisissa poluissasi on seuranta tarkistamalla, että polun lopussa on teksti `?wt.mc_id=`.
Jos se löytyy suhteellisista poluistasi, läpäiset tarkistuksen.

Jos ei, saat todennäköisesti seuraavan virheen.

![GitHub tarkistus polut ilman seurantaa -kommenttikuva](../../translated_images/fi/github-check-paths-missing-tracking-comment.880d4afe03e898ff.webp?WT.mc_id=academic-105485-koreyst "Kuvakaappaus GitHub-kommentista, joka osoittaa, että suhteellisissa poluissa puuttuu seuranta")

Korjataksesi ongelman avaa työnkulun osoittama tiedostopolku ja lisää seurannan tunniste suhteellisten polkujen loppuun.

Kun lisäät seurannan tunnisteen, tallenna ja lähetä muutokset, työnkulku käynnistyy uudelleen tarkistamaan muutokset.
Jos läpäiset tarkistuksen, voit jatkaa.

### Tarkista, että URL-osoitteissa on seuranta

Tämä työnkulku varmistaa, että kaikissa verkko-URL-osoitteissa on seuranta.
Tämä arkisto on kaikille avoin, joten sinun on varmistettava liikenteen lähteen seuranta.

Varmista, että URL-osoitteissasi on seuranta tarkistamalla, että osoitteen lopussa on teksti `?wt.mc_id=`.
Jos se löytyy URL-osoitteistasi, läpäiset tarkistuksen.

Jos ei, saat todennäköisesti seuraavan virheen.

![GitHub tarkistus URL:t ilman seurantaa -kommenttikuva](../../translated_images/fi/github-check-urls-missing-tracking-comment.1bd00d20b24a1e2e.webp?WT.mc_id=academic-105485-koreyst "Kuvakaappaus GitHub-kommentista, joka osoittaa, että URL-osoitteista puuttuu seuranta")

Korjataksesi ongelman avaa työnkulun osoittama tiedostopolku ja lisää seurannan tunniste URL-osoitteiden loppuun.

Kun lisäät seurannan tunnisteen, tallenna ja lähetä muutokset, työnkulku käynnistyy uudelleen tarkistamaan muutokset.
Jos läpäiset tarkistuksen, voit jatkaa.

### Tarkista, ettei URL-osoitteissa ole alueasetusta

Tämä työnkulku varmistaa, että URL-osoitteissa ei ole maakohtaista alueasetusta.
Tämä arkisto on kaikille maailmanlaajuisesti avoin, joten varmista ettet sisällytä maasi alueasetusta URL-osoitteisiin.

Varmista, ettei URL-osoitteissa ole maakohtaista alueasetusta tarkistamalla, etteivät URL-osoitteet sisällä tekstiä `/en-us/`, `/en/` tai muita kielikohtaisia alueasetuksia.
Jos alueasetusta ei ole URL-osoitteissasi, läpäiset tarkistuksen.

Jos alueasetus on mukana, saat todennäköisesti seuraavan virheen.

![GitHub tarkistus maa-aluetasetuksen lisääminen URL-osoitteisiin -kommenttikuva](../../translated_images/fi/github-check-country-locale-comment.2f4fe93228161dee.webp?WT.mc_id=academic-105485-koreyst "Kuvakaappaus GitHub-kommentista, jossa URL-osoitteisiin on lisätty maa-aluetasetus")

Korjataksesi ongelman avaa työnkulun osoittama tiedostopolku ja poista maa-aluetasetus URL-osoitteista.

Kun olet poistanut maa-aluetasetuksen, tallenna ja lähetä muutokset, työnkulku käynnistyy uudelleen tarkistamaan muutokset.
Jos läpäiset tarkistuksen, voit jatkaa.

Onneksi olkoon! Otamme sinuun yhteyttä mahdollisimman pian palautteen antamiseksi panoksestasi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->