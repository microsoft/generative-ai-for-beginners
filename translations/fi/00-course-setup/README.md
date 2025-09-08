<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T17:41:53+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "fi"
}
-->
# Kurssin aloitus

Olemme todella innoissamme, että aloitat tämän kurssin ja näemme, mihin generatiivinen tekoäly sinua inspiroi!

Tällä sivulla kerrotaan asennusvaiheet, tekniset vaatimukset ja mistä saat apua tarvittaessa, jotta onnistut kurssilla.

## Asennusvaiheet

Aloittaaksesi kurssin, sinun tulee käydä läpi seuraavat vaiheet.

### 1. Haarauta tämä repo

[Haarauta koko tämä repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) omaan GitHub-tiliisi, jotta voit muokata koodia ja suorittaa haasteet. Voit myös [merkitä tämän repon suosikiksi (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), jolloin löydät tämän ja muut vastaavat repot helpommin.

### 2. Luo codespace

Välttääksesi riippuvuusongelmat koodia ajaessasi suosittelemme käyttämään [GitHub Codespacesia](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) tämän kurssin suorittamiseen.

Omassa haarassasi: **Code -> Codespaces -> New on main**

![Dialogi, jossa näkyy painikkeet codespacen luomiseen](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Lisää salaisuus

1. ⚙️ Ratasikoni -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Nimeä OPENAI_API_KEY, liitä avain, Tallenna.

### 3.  Mitä seuraavaksi?

| Haluan…             | Siirry…                                                                 |
|---------------------|-------------------------------------------------------------------------|
| Aloittaa ensimmäisen oppitunnin | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Työskennellä offline | [`setup-local.md`](02-setup-local.md)                                   |
| Määrittää LLM-palveluntarjoajan | [`providers.md`](providers.md)                                        |
| Tavata muita oppijoita | [Liity Discordiin](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Vianmääritys

| Oire                                      | Korjaus                                                          |
|-------------------------------------------|------------------------------------------------------------------|
| Containerin rakentaminen jumissa > 10 min | **Codespaces ➜ “Rebuild Container”**                             |
| `python: command not found`               | Terminaali ei yhdistänyt; klikkaa **+** ➜ *bash*                 |
| `401 Unauthorized` OpenAI:lta             | Väärä / vanhentunut `OPENAI_API_KEY`                             |
| VS Code näyttää “Dev container mounting…” | Päivitä selaimen välilehti—Codespaces menettää joskus yhteyden   |
| Notebookin kernel puuttuu                 | Notebook-valikko ➜ **Kernel ▸ Select Kernel ▸ Python 3**         |

   Unix-pohjaiset järjestelmät:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Muokkaa `.env`-tiedostoa**: Avaa `.env`-tiedosto tekstieditorissa (esim. VS Code, Notepad++ tai muu editori). Lisää tiedostoon seuraava rivi, korvaten `your_github_token_here` omalla GitHub-tokenillasi:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Tallenna tiedosto**: Tallenna muutokset ja sulje editori.

5. **Asenna `python-dotenv`**: Jos et ole vielä asentanut, sinun täytyy asentaa `python-dotenv`-paketti, jotta ympäristömuuttujat latautuvat `.env`-tiedostosta Python-sovellukseen. Voit asentaa sen pipillä:

   ```bash
   pip install python-dotenv
   ```

6. **Lataa ympäristömuuttujat Python-skriptissäsi**: Käytä Python-skriptissäsi `python-dotenv`-pakettia ladataksesi ympäristömuuttujat `.env`-tiedostosta:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Siinä kaikki! Olet onnistuneesti luonut `.env`-tiedoston, lisännyt GitHub-tokenin ja ladannut sen Python-sovellukseen.

## Kuinka ajaa koodi paikallisesti omalla koneella

Jos haluat ajaa koodia paikallisesti, tarvitset jonkin version [Pythonista asennettuna](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Käyttääksesi repoa, sinun täytyy kloonata se:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kun kaikki on ladattu, voit aloittaa!

## Valinnaiset vaiheet

### Minicondan asentaminen

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) on kevyt asennusohjelma [Condan](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonin ja muutamien pakettien asentamiseen.
Conda on pakettienhallintaohjelma, jonka avulla on helppo luoda ja vaihtaa eri Pythonin [**virtuaaliympäristöjen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ja pakettien välillä. Se on myös kätevä sellaisten pakettien asentamiseen, joita ei löydy `pip`:n kautta.

Voit seurata [MiniConda-asennusohjetta](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) asentaaksesi sen.

Kun Miniconda on asennettu, sinun täytyy kloonata [repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jos et ole jo tehnyt sitä).

Seuraavaksi sinun täytyy luoda virtuaaliympäristö. Condalla tämä onnistuu luomalla uusi ympäristötiedosto (_environment.yml_). Jos käytät Codespacesia, luo tämä tiedosto `.devcontainer`-kansioon, eli `.devcontainer/environment.yml`.

Lisää ympäristötiedostoon alla oleva koodinpätkä:

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

Jos kohtaat ongelmia conda:n kanssa, voit asentaa Microsoftin AI-kirjastot manuaalisesti seuraavalla komennolla terminaalissa.

```
conda install -c microsoft azure-ai-ml
```

Ympäristötiedosto määrittelee tarvittavat riippuvuudet. `<environment-name>` on nimi, jonka haluat antaa Conda-ympäristöllesi, ja `<python-version>` on haluamasi Pythonin versio, esimerkiksi `3` on uusin pääversio.

Tämän jälkeen voit luoda Conda-ympäristön suorittamalla seuraavat komennot komentorivillä/terminaalissa

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Katso [Conda-ympäristöjen ohje](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) jos kohtaat ongelmia.

### Visual Studio Coden käyttäminen Python-laajennuksen kanssa

Suosittelemme käyttämään [Visual Studio Codea (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) ja siihen asennettua [Python-laajennusta](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) tämän kurssin aikana. Tämä on kuitenkin vain suositus, ei pakollinen vaatimus.

> **Huom**: Kun avaat kurssin repoa VS Codessa, voit halutessasi ottaa projektin käyttöön containerissa. Tämä onnistuu, koska kurssin reposta löytyy [erityinen `.devcontainer`-kansio](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst). Tästä lisää myöhemmin.

> **Huom**: Kun kloonaat ja avaat kansion VS Codessa, ohjelma ehdottaa automaattisesti Python-laajennuksen asentamista.

> **Huom**: Jos VS Code ehdottaa repoa avattavaksi containerissa, hylkää tämä pyyntö, jotta voit käyttää paikallisesti asennettua Pythonia.

### Jupyterin käyttäminen selaimessa

Voit työskennellä projektin parissa myös [Jupyter-ympäristössä](https://jupyter.org?WT.mc_id=academic-105485-koreyst) suoraan selaimessa. Sekä perinteinen Jupyter että [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) tarjoavat mukavan kehitysympäristön, jossa on mm. automaattinen täydennys ja koodin korostus.

Käynnistääksesi Jupyterin paikallisesti, avaa terminaali/komentorivi, siirry kurssin kansioon ja suorita:

```bash
jupyter notebook
```

tai

```bash
jupyterhub
```

Tämä käynnistää Jupyterin ja komentoriville ilmestyy URL-osoite, jonka kautta pääset käyttämään sitä.

Kun avaat URL-osoitteen, näet kurssin sisällön ja voit siirtyä mihin tahansa `*.ipynb`-tiedostoon. Esimerkiksi `08-building-search-applications/python/oai-solution.ipynb`.

### Ajaminen containerissa

Vaihtoehto omalle koneelle tai Codespaceen asentamiselle on käyttää [containeria](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Kurssin reposta löytyvä erityinen `.devcontainer`-kansio mahdollistaa projektin käyttöönoton containerissa VS Codella. Codespacesin ulkopuolella tämä vaatii Dockerin asennuksen ja hieman enemmän työtä, joten suosittelemme tätä vain, jos sinulla on kokemusta containereista.

Yksi parhaista tavoista pitää API-avaimesi turvassa GitHub Codespacesissa on käyttää Codespace Secrets -toimintoa. Lue lisää [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) -ohjeesta.

## Oppitunnit ja tekniset vaatimukset

Kurssilla on 6 teoriaopetusta ja 6 koodausopetusta.

Koodausosioissa käytämme Azure OpenAI Serviceä. Tarvitset pääsyn Azure OpenAI -palveluun ja API-avaimen ajaaksesi koodia. Voit hakea pääsyä [täyttämällä tämän hakemuksen](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Sillä aikaa kun hakemustasi käsitellään, jokaisessa koodausosiossa on myös `README.md`-tiedosto, josta voit katsoa koodin ja tulosteet.

## Azure OpenAI Servicen käyttäminen ensimmäistä kertaa

Jos käytät Azure OpenAI -palvelua ensimmäistä kertaa, seuraa tätä ohjetta [luodaksesi ja käyttöönottaaksesi Azure OpenAI Service -resurssin.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## OpenAI API:n käyttäminen ensimmäistä kertaa

Jos käytät OpenAI API:a ensimmäistä kertaa, seuraa ohjetta [luodaksesi ja käyttääksesi käyttöliittymää.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Tapaa muita oppijoita

Olemme luoneet kanavia viralliselle [AI Community Discord -palvelimellemme](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst), jossa voit tavata muita oppijoita. Tämä on loistava tapa verkostoitua muiden yrittäjien, rakentajien, opiskelijoiden ja generatiivisesta tekoälystä kiinnostuneiden kanssa.

[![Liity Discord-kanavalle](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektitiimi on myös mukana Discordissa auttamassa oppijoita.

## Osallistu

Tämä kurssi on avoimen lähdekoodin projekti. Jos huomaat parannettavaa tai virheitä, tee [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) tai kirjaa [GitHub-issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektitiimi seuraa kaikkia kontribuutioita. Avoimeen lähdekoodiin osallistuminen on erinomainen tapa kehittää uraasi generatiivisen tekoälyn parissa.

Useimmat kontribuutiot vaativat Contributor License Agreementin (CLA) hyväksymisen, jolla vakuutat, että sinulla on oikeus antaa panoksesi ja myönnät meille oikeudet käyttää sitä. Lisätietoja löydät [CLA, Contributor License Agreement -sivulta](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Tärkeää: kun käännät tekstiä tässä repossa, älä käytä konekäännöstä. Yhteisö tarkistaa käännökset, joten tarjoa käännöksiä vain kielille, joissa olet sujuva.

Kun lähetät pull requestin, CLA-bot tarkistaa automaattisesti, tarvitsetko CLA:n ja merkitsee PR:n sen mukaisesti (esim. label, kommentti). Seuraa botin ohjeita. Tämä tarvitsee tehdä vain kerran kaikissa CLA:ta käyttävissä repoisamme.

Tämä projekti noudattaa [Microsoftin Open Source Code of Conductia](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Lisätietoja saat lukemalla Code of Conduct FAQ:n tai ottamalla yhteyttä [Email opencode](opencode@microsoft.com) mahdollisissa kysymyksissä tai kommenteissa.

## Aloitetaan!
Nyt kun olet suorittanut tarvittavat vaiheet tämän kurssin loppuun saattamiseksi, aloitetaan tutustumalla [generatiiviseen tekoälyyn ja LLM-malleihin](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen omalla kielellä tulee pitää ensisijaisena lähteenä. Kriittisissä tapauksissa suositellaan ammattimaista ihmiskääntäjää. Emme ole vastuussa tämän käännöksen käytöstä mahdollisesti aiheutuvista väärinkäsityksistä tai tulkintavirheistä.