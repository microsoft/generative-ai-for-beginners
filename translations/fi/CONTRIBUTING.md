# Osallistuminen

Tämä projekti toivottaa tervetulleiksi panokset ja ehdotukset. Useimmat panokset edellyttävät, että
hyväksyt osallistujan lisenssisopimuksen (CLA), jossa vakuutat, että sinulla on oikeus,
ja todella myönnät meille oikeudet käyttää panostasi. Lisätietoja saat osoitteesta
<https://cla.microsoft.com>.

> Tärkeää: kun käännät tekstiä tässä repossa, varmista, ettet käytä konekäännöstä. Varmistamme käännökset yhteisön avulla, joten ilmoittaudu vapaaehtoiseksi vain kielissä, joissa olet taitava.

Kun lähetät koodimuutospyynnön, CLA-botti tarkistaa automaattisesti, tarvitsetko
toimittaa CLA:n ja merkitsee PR:n asianmukaisesti (esim. etiketti, kommentti). Noudata vain
botin antamia ohjeita. Tätä tarvitsee tehdä vain kerran kaikissa CLA:tamme käyttävissä repositorioissa.

## Käyttäytymissäännöt

Tämä projekti on ottanut käyttöön [Microsoftin avoimen lähdekoodin käyttäytymissäännöt](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst).
Lisätietoja saat lukemalla [Käyttäytymissääntöjen UKK:n](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) tai ottamalla yhteyttä [opencode@microsoft.com](mailto:opencode@microsoft.com) mahdollisten lisäkysymysten tai kommenttien osalta.

## Kysymys tai ongelma?

Älä avaa GitHub-ongelmia yleisillä tukikysymyksillä, sillä GitHub-listaa tulisi käyttää ominaisuuspyyntöihin ja bugiraportteihin. Näin voimme helpommin seurata varsinaisia ongelmia tai bugeja koodista ja pitää yleisen keskustelun erillään varsinaisesta koodista.

## Kirjoitusvirheet, ongelmat, bugit ja panokset

Kun lähetät muutoksia Generative AI for Beginners -repositorioihin, noudata näitä suosituksia.

* Tee aina haara omaan tiliisi ennen muokkausten tekemistä
* Älä yhdistä useita muutoksia yhteen koodimuutospyyntöön. Esimerkiksi lähetä bugikorjaukset ja dokumentaatiopäivitykset erillisillä PR:llä
* Jos koodimuutospyyntösi näyttää yhdistämiskonflikteja, varmista, että päivität paikallisen main-oksasi vastaamaan päärepositoriota ennen muokkausten tekemistä
* Jos toimitat käännöstä, tee yksi PR kaikille käännetyille tiedostoille, koska emme hyväksy osittaisia käännöksiä sisällöstä
* Jos toimitat kirjoitusvirheen tai dokumentaatiokorjauksen, voit yhdistää muutokset yhteen sopivaan PR:ään

## Sisällölliset rajaukset ja kolmannen osapuolen tuotteet

Tämä opintokokonaisuus keskittyy Microsoftin teknologioihin ja toimittajasta riippumattomiin avoimiin standardeihin. Panosten tulee palvella selkeää opetustarkoitusta eivätkä saa ensisijaisesti tarkoituksenaan esitellä tai mainostaa kolmannen osapuolen kaupallista tuotetta, hosting-palvelua, mallin reititintä, SDK:ta, MCP-palvelinta tai muuta toimittajakohtaista tarjontaa.

Avoimen lähdekoodin ohjelmistoja ja kolmannen osapuolen riippuvuuksia voidaan mainita, kun ne ovat tarpeen avoimen standardin tai yhteentoimivuustilanteen selittämiseksi, esitetään neutraalisti, eikä keskity toimittajan tuotteeseen tai hostattuun päätepisteeseen. Jos ehdotettu panoksesi sisältää toimittajakohtaisen tuotteen tai palvelun, avaa issue ja hanki ylläpitäjän hyväksyntä ennen koodimuutospyynnön lähettämistä.

Panoksensa antajien tulee ilmoittaa kaikista olennaisista työsuhteista, omistuksista, sponsoroinneista tai muista sidonnaisuuksista tuotteen tai palvelun yhteydessä, jota panoksessa mainitaan. Älä sisällytä tukemattomia hintatietoja, suorituskyky-, turvallisuus-, yksityisyys- tai vertailuväittämiä. Suoritettavat esimerkit eivät saa oletuksena lähettää oppijatietoja tai suorittaa julkisia toimia ulkoisen kolmannen osapuolen palvelun kautta.

## Yleisiä kirjoitusohjeita

- Varmista että kaikki URL-osoitteesi ovat suljettuna hakasulkeisiin ja sen jälkeen sulkeet ilman ylimääräisiä välilyöntejä niiden ympärillä tai sisällä `[]()`.
- Varmista että mikä tahansa suhteellinen linkki (eli linkit muihin tiedostoihin ja kansioihin repositoriossa) alkaa `./`, joka viittaa tiedostoon tai kansioon nykyisessä työhakemistossa tai `../`, joka viittaa tiedostoon tai kansioon ylemmässä työhakemistossa.
- Varmista, että mikä tahansa suhteellinen linkki (eli linkit muihin tiedostoihin ja kansioihin repositoriossa) sisältää seurannan tunnisteen (eli `?` tai `&` ja sitten `wt.mc_id=` tai `WT.mc_id=`) linkin lopussa.
- Varmista, että mikä tahansa URL-osoite seuraavilta domaineilta _github.com, microsoft.com, visualstudio.com, aka.ms ja azure.com_ sisältää seurannan tunnisteen (eli `?` tai `&` ja sitten `wt.mc_id=` tai `WT.mc_id=`) linkin lopussa.
- Varmista, että linkeissäsi ei ole maakohtaista paikallista asetusta (eli `/en-us/` tai `/en/`).
- Varmista, että kaikki kuvat on tallennettu `./images`-kansioon.
- Varmista, että kuvat on nimetty kuvaavasti käyttäen englanninkielisiä merkkejä, numeroita ja väliviivoja kuvien nimissä.

## GitHub-työnkulut

Kun lähetät koodimuutospyynnön, neljä erilaista työnkulkua aktivoituu tarkistamaan edellä mainitut säännöt.
Noudata vain tässä annettuja ohjeita päästäksesi tarkistuksesta läpi.

- [Tarkista rikkoutuneet suhteelliset polut](#check-broken-relative-paths)
- [Tarkista polut sisältävät seurannan](#check-paths-have-tracking)
- [Tarkista URL-osoitteet sisältävät seurannan](#check-urls-have-tracking)
- [Tarkista, ettei URL-osoitteissa ole paikallista asetusta](#check-urls-dont-have-locale)

### Tarkista rikkoutuneet suhteelliset polut

Tämä työnkulku varmistaa, että tiedostoissasi olevat suhteelliset polut toimivat.
Tämä repositorio on julkaistu GitHub-sivuilla, joten sinun tulee olla hyvin huolellinen kirjoittaessasi linkkejä, jotka liittävät kaiken yhteen, etteivät ne ohjaa ketään väärään paikkaan.

Varmistaaksesi, että linkkisi toimivat oikein, käytä esimerkiksi VS Codea tarkistamiseen.

Esimerkiksi, kun viet osoittimen minkä tahansa linkin päälle tiedostoissasi, sinua pyydetään seuraamaan linkkiä painamalla **ctrl + click**

![VS code follow links screenshot](../../translated_images/fi/vscode-follow-link.85520ab6a1237adc.webp?WT.mc_id=academic-105485-koreyst "Kuvakaappaus VS Coden kehotteesta seurata linkkiä, kun viet osoittimen linkin päälle.")

Jos klikkaat linkkiä etkä se toimi paikallisesti, se varmasti aiheuttaa tarkistuksen epäonnistumisen eikä toimi GitHubissa.

Korjataksesi ongelman, yritä kirjoittaa linkki VS Coden avulla.

Kun kirjoitat `./` tai `../` VS Code ehdottaa vaihtoehtoja kirjoittamasi mukaan.

![VS code select relative path screenshot](../../translated_images/fi/vscode-select-relative-path.3804eb73c3a9e5f2.webp?WT.mc_id=academic-105485-koreyst "Kuvakaappaus VS Coden kehotteesta valita suhteellinen polku ponnahdusvalikosta.")

Seuraa polkua klikkaamalla haluttua tiedostoa tai kansiota, niin voit olla varma, että polkusi ei ole rikkinäinen.

Kun olet lisännyt oikean suhteellisen polun, tallenna ja työnnä muutokset, työnkulku aktivoituu uudelleen tarkistamaan muutokset.
Jos tarkistus menee läpi, olet valmis jatkamaan.

### Tarkista polut sisältävät seurannan

Tämä työnkulku varmistaa, että kaikissa suhteellisissa poluissa on seuranta.
Tämä repositorio on julkaistu GitHub-sivuilla, joten meidän täytyy seurata siirtymisiä eri tiedostojen ja kansioiden välillä.

Varmistaaksesi, että suhteellisissa poluissa on seuranta, tarkista, että polun lopussa on teksti `?wt.mc_id=`.
Jos se on lisätty suhteellisiin polkuihin, läpäiset tämän tarkistuksen.

Jos ei, voit saada seuraavan virheilmoituksen.

![GitHub check paths missing tracking comment screenshot](../../translated_images/fi/github-check-paths-missing-tracking-comment.880d4afe03e898ff.webp?WT.mc_id=academic-105485-koreyst "Kuvakaappaus GitHub-kommentista, jossa ilmoitetaan seurannan puuttumisesta suhteellisista poluista")

Korjataksesi ongelman, avaa tiedostopolku, jonka työnkulku korosti, ja lisää seurantanumero suhteellisten polkujen loppuun.

Kun olet lisännyt seurannan, tallenna ja työnnä muutokset, työnkulku käynnistyy uudelleen tarkistamaan muutokset.
Jos tarkistus menee läpi, olet valmis jatkamaan.

### Tarkista URL-osoitteet sisältävät seurannan

Tämä työnkulku varmistaa, että kaikissa verkko-URL-osoitteissa on seuranta.
Tämä repositorio on kaikkien käytettävissä, joten sinun tulee varmistaa, että liikennettä voidaan seurata ja tiedetään, mistä liikenne tulee.

Varmistaaksesi, että URL-osoitteissasi on seuranta, tarkista, että URL:n lopussa on teksti `?wt.mc_id=`.
Jos se on lisätty URL-osoitteisiin, läpäiset tämän tarkistuksen.

Jos ei, voit saada seuraavan virheilmoituksen.

![GitHub check urls missing tracking comment screenshot](../../translated_images/fi/github-check-urls-missing-tracking-comment.1bd00d20b24a1e2e.webp?WT.mc_id=academic-105485-koreyst "Kuvakaappaus GitHub-kommentista, jossa ilmoitetaan seurannan puuttumisesta URL-osoitteista")

Korjataksesi ongelman, avaa tiedostopolku, jonka työnkulku korosti, ja lisää seurantanumero URL-osoitteiden loppuun.

Kun olet lisännyt seurannan, tallenna ja työnnä muutokset, työnkulku aktivoituu uudelleen tarkistamaan muutokset.
Jos tarkistus menee läpi, olet valmis jatkamaan.

### Tarkista, ettei URL-osoitteissa ole paikallista asetusta

Tämä työnkulku varmistaa, ettei verkko-URL-osoitteissa ole maakohtaista paikallista asetusta.
Tämä repositorio on käytettävissä maailmanlaajuisesti, joten sinun tulee varmistaa, ettet sisällytä oman maasi paikallista asetusta URL-osoitteisiin.

Varmistaaksesi, ettei URL-osoitteissasi ole maakohtaista asetusta, tarkista, ettei URL-osoitteissa ole tekstejä `/en-us/` tai `/en/` tai mitään muuta kielikohtaista paikallista asetusta.
Jos niitä ei ole URL-osoitteissa, läpäiset tarkistuksen.

Jos on, saatat saada seuraavan virheilmoituksen.

![GitHub check country locale comment screenshot](../../translated_images/fi/github-check-country-locale-comment.2f4fe93228161dee.webp?WT.mc_id=academic-105485-koreyst "Kuvakaappaus GitHub-kommentista, jossa ilmoitetaan lisääntyneestä maakohtaisesta paikallisasetuksesta URL-osoitteissa")

Korjataksesi ongelman, avaa tiedostopolku, jonka työnkulku korosti, ja poista maakohtainen paikallisasetus URL-osoitteista.

Kun olet poistanut maakohtaisen paikallisasetuksen, tallenna ja työnnä muutokset, työnkulku käynnistyy uudelleen tarkistamaan muutokset.
Jos tarkistus menee läpi, olet valmis jatkamaan.

Onnittelut! Otamme sinuun yhteyttä mahdollisimman pian palautteen antamiseksi panoksestasi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->