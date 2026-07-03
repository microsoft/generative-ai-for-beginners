# Tämä kurssi käynnistyy

Olemme erittäin innoissamme siitä, että aloitat tämän kurssin ja näet, mitä innostut rakentamaan generatiivisen tekoälyn avulla!

Varmistaaksemme onnistumisesi, tämä sivu sisältää asennusohjeet, tekniset vaatimukset ja ohjeet kuinka saat apua tarvittaessa.

## Asentamisohjeet

Kurssin aloittamiseksi sinun tulee suorittaa seuraavat vaiheet.

### 1. Haarauta tämä repo

[Haarauta koko repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) omaan GitHub-tiliisi, jotta voit muokata koodia ja suorittaa haasteet. Voit myös [merkitä tämän repon tähdellä (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) löytääksesi sen ja siihen liittyvät repot helpommin.

### 2. Luo codespace

Välttääksesi riippuvuusongelmat koodia ajettaessa, suosittelemme tämän kurssin suorittamista [GitHub Codespacesissa](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Oman haarautumisesi sisällä: **Code -> Codespaces -> New on main**

![Dialogi, jossa on napit codespacen luomiseksi](../../../translated_images/fi/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Lisää salaisuus

1. ⚙️ Hammasratas-kuvake -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Nimeä se OPENAI_API_KEY, liitä avain, Tallenna.

### 3. Mitä sitten?

| Haluan…              | Mene kohtaan…                                                         |
|----------------------|----------------------------------------------------------------------|
| Aloita oppitunti 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)  |
| Työskennellä offline  | [`setup-local.md`](02-setup-local.md)                                |
| Aseta LLM-palveluntarjoaja | [`providers.md`](03-providers.md)                                   |
| Tapaa muita oppijoita | [Liity Discordiin](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)  |

## Ongelmien ratkaisu


| Oire                                       | Korjaus                                                         |
|--------------------------------------------|-----------------------------------------------------------------|
| Kontin rakennus jumissa yli 10 min         | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`                  | Terminaali ei yhdistänyt; napsauta **+** ➜ *bash*              |
| `401 Unauthorized` OpenAI:lta                | Väärä / vanhentunut `OPENAI_API_KEY`                             |
| VS Code näyttää “Dev container mounting…”    | Päivitä selainikkuna—Codespaces menettää välillä yhteyden       |
| Muistikirjan ydin puuttuu                   | Muistikirjan valikko ➜ **Kernel ▸ Select Kernel ▸ Python 3**   |

   Unix-pohjaiset järjestelmät:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Muokkaa `.env`-tiedostoa**: Avaa `.env`-tiedosto tekstieditorissa (esim. VS Code, Notepad++ tai muu editori). Lisää tiedostoon seuraava rivi korvaten `your_github_token_here` omalla GitHub-tokenillasi:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Tallenna tiedosto**: Tallenna muutokset ja sulje tekstieditori.

5. **Asenna `python-dotenv`**: Jos et ole vielä asentanut, sinun tulee asentaa `python-dotenv`-paketti, jotta voit ladata ympäristömuuttujat `.env`-tiedostosta Python-sovellukseesi. Voit asentaa sen käyttämällä `pip`-komentoa:

   ```bash
   pip install python-dotenv
   ```

6. **Lataa ympäristömuuttujat Python-skriptissä**: Käytä Python-skriptissäsi `python-dotenv`-pakettia lukeaksesi muuttujat `.env`-tiedostosta:

   ```python
   from dotenv import load_dotenv
   import os

   # Lataa ympäristömuuttujat .env-tiedostosta
   load_dotenv()

   # Käytä GITHUB_TOKEN-muuttujaa
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Siinä kaikki! Olet onnistuneesti luonut `.env`-tiedoston, lisännyt siihen GitHub-tokenisi ja ladannut sen Python-sovellukseesi.

## Kuinka suorittaa paikallisesti omalla tietokoneellasi

Koodin suorittaminen paikallisesti edellyttää, että sinulla on asennettuna jokin versio [Pythonista](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Repo täytyy sitten kloonata:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kun kaikki on kloonattu, voit alkaa työstää!

## Valinnaiset vaiheet

### Minicondan asentaminen

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) on kevyt asennustyökalu [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst):n, Pythonin sekä joidenkin pakettien asentamiseen.  
Conda on pakettien hallintaan tarkoitettu työkalu, joka helpottaa eri Python-[**virtuaaliympäristöjen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ja pakettien asentamista ja vaihtoa. Se on myös hyödyllinen, kun asennettavia paketteja ei ole saatavilla `pip`-komennolla.

Voit seurata [Miniconda asennusohjetta](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) asennusta varten.

Miniconda asennettuna, sinun tulee kloonata [repositorio](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jos et ole vielä tehnyt sitä).

Seuraavaksi sinun täytyy luoda virtuaaliympäristö. Condalla tämä tehdään luomalla uusi ympäristötiedosto (_environment.yml_). Jos suoritat Codespacesissa, luo tämä `.devcontainer`-kansioon, eli polku on `.devcontainer/environment.yml`.

Täytä ympäristötiedostosi seuraavalla koodilla:

```yml
name: <environment-name>
channels:
  - defaults
  - microsoft
dependencies:
  - python=<python-version>
  - openai
  - python-dotenv
  - pip
  - pip:
      - azure-ai-ml
```

Jos conda-komentoa käytettäessä tulee virheitä, voit asentaa Microsoft AI Libraries -kirjastot manuaalisesti avaamalla terminaalin ja ajamalla seuraavan komennon:

```
conda install -c microsoft azure-ai-ml
```

Ympäristötiedosto määrittelee tarvittavat riippuvuudet. `<environment-name>` tarkoittaa haluamaasi Conda-ympäristön nimeä ja `<python-version>` on Pythonin versio (esim. `3` on uusin pääversio).

Kun tämä on tehty, voit luoda Conda-ympäristösi suorittamalla seuraavat komennot komentorivillä/terminaalissa:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer-alihakupolku koskee vain Codespace-asetuksia
conda activate ai4beg
```

Katso lisää [Conda environment -oppaasta](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) jos kohtaat ongelmia.

### Visual Studio Coden käyttö Python-tuelle laajennuksella

Suosittelemme käyttämään tähän kurssiin [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) -editoria yhdessä [Python-tuki-laajennuksen](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) kanssa. Tämä on kuitenkin vain suositus, ei pakollinen vaatimus.

> **Huom:** Kun avaat kurssin repositorion VS Codessa, voit halutessasi rakentaa projektin säiliöön. Tämä onnistuu [erikoisella `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) -kansiolla, joka löytyy kurssin reposta. Lisätietoa tästä myöhemmin.

> **Huom:** Kun kloonaat ja avaat kansion VS Codessa, editori ehdottaa automaattisesti Python-tuen asennusta.

> **Huom:** Jos VS Code ehdottaa repositorion avaamista säiliössä, hylkää tämä, jos haluat käyttää tietokoneelle asennettua Python-versiota.

### Jupyterin käyttö selaimessa

Voit myös tehdä projektia [Jupyter-ympäristössä](https://jupyter.org?WT.mc_id=academic-105485-koreyst) suoraan selaimessasi. Sekä klassinen Jupyter että [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) tarjoavat miellyttävän kehitysympäristön ominaisuuksineen, kuten automaattinen täydennys, koodin korostus jne.

Aloittaaksesi Jupyteriä paikallisesti, siirry terminaaliin/komentoriville, mene kurssihakemistoon ja aja:

```bash
jupyter notebook
```

tai

```bash
jupyterhub
```

Tämä käynnistää Jupyter-instanssin, ja pääsylinkin URL tulostetaan komentoriville.

Kun avaat URL-osoitteen, näet kurssin rakenteen ja voit avata `*.ipynb`-tiedostoja, esimerkiksi `08-building-search-applications/python/oai-solution.ipynb`.

### Suoritus säiliössä

Vaihtoehtona kaiken järjestämiselle omalle koneelle tai Codespaceen on käyttää [säiliötä](<https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Kurssirepossa oleva `.devcontainer`-kansio mahdollistaa projektin käynnistämisen säiliössä VS Codessa. Codespacesin ulkopuolella tämä vaatii Dockerin asennuksen ja hieman teknistä osaamista, joten suosittelemme tätä vain kokeneille säiliöiden käyttäjille.

Yksi parhaista tavoista pitää API-avaimesi turvassa GitHub Codespacessa on käyttää Codespace Secrets -toimintoa. Tutustu [Codespaces-salaisuuksien hallintaan](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst).

## Oppitunnit ja tekniset vaatimukset

Kurssi sisältää 6 konseptituntia ja 6 koodausoppituntia.

Koodausoppitunneilla käytämme Azure OpenAI -palvelua. Sinun tarvitsee päästä Azure OpenAI -palveluun ja sinulla tulee olla API-avain tämän koodin suorittamiseen. Voit hakea pääsyä [täyttämällä tämän hakemuksen](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Kun odotat hakemuksesi käsittelyä, jokaisella koodausoppitunnilla on mukana `README.md` -tiedosto, jossa voit tarkastella koodia ja tuloksia.

## Azure OpenAI -palvelun käyttöönotto ensimmäistä kertaa

Jos työskentelet Azure OpenAI -palvelun kanssa ensimmäistä kertaa, seuraa tätä opasta kuinka [luot ja otat käyttöön Azure OpenAI -resurssin.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## OpenAI API:n käyttö ensimmäistä kertaa

Jos työskentelet OpenAI API:n kanssa ensimmäistä kertaa, seuraa opasta kuinka [luot ja käytät rajapintaa.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Tapaa muita oppijoita

Olemme luoneet kanavia viralliselle [AI Community Discord -palvelimellemme](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) muiden oppijoiden tapaamista varten. Tämä on erinomainen tapa verkostoitua muiden samanhenkisten yrittäjien, rakentajien, opiskelijoiden ja kaikkien generatiivisen tekoälyn osaamisen kehittämisestä kiinnostuneiden kanssa.

[![Liity discord-kanavalle](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektitiimi on myös läsnä tässä Discord-palvelimessa auttamassa oppijoita.

## Osallistu

Tämä kurssi on avoimen lähdekoodin hanke. Jos havaitset parannusmahdollisuuksia tai ongelmia, tee [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) tai ilmoita [GitHub-ongelmasta](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektitiimi seuraa kaikkia panostuksia. Osallistuminen avoimen lähdekoodin hankkeisiin on upea tapa kehittää uraasi generatiivisen tekoälyn parissa.

Suurin osa panostuksista vaatii, että allekirjoitat Kontribuuttorisopimuksen (Contributor License Agreement, CLA), jossa vakuutat, että sinulla on oikeus ja että annat meille oikeudet käyttää panostasi. Lisätietoja löytyy [CLA, Contributor License Agreement -sivustolta](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Tärkeää: kun käännät tekstiä tässä repossa, varmista, että et käytä konekäännöksiä. Tarkistamme käännökset yhteisön kautta, joten anna käännöksiä vain kielillä, joissa olet osaaja.

Kun lähetät pull requestin, CLA-botti automaattisesti tarkistaa, tarvitseeko sinun allekirjoittaa CLA, ja merkitsee PR:n asianmukaisesti (esim. tagi, kommentti). Noudata botin ohjeita. Tämä riittää tekemään vain kerran kaikissa CLA-sopimuksia käyttävissä repokoissa.

Tämä projekti on ottanut käyttöön [Microsoft Open Source Code of Conductin](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Lisätietoja saat lukemalla Code of Conductin usein kysytyt kysymykset (FAQ) tai ottamalla yhteyttä [sähköpostitse opencode@microsoft.com](opencode@microsoft.com) lisäkysymyksissä tai palautteessa.

## Aloitetaan!
Nyt kun olet suorittanut kurssin loppuun saattamiseksi tarvittavat vaiheet, aloitetaan perehtymällä [Generatiiviseen tekoälyyn ja suurimallimalleihin](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta otathan huomioon, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen omalla kielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tästä käännöksestä johtuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->