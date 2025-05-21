<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T12:52:00+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "fi"
}
-->
# Aseta kehitysympäristösi

Olemme luoneet tämän repositorion ja kurssin [kehityskontin](https://containers.dev?WT.mc_id=academic-105485-koreyst) avulla, joka sisältää universaalin suoritusympäristön, joka tukee Python3-, .NET-, Node.js- ja Java-kehitystä. Asiaan liittyvä konfiguraatio on määritelty `devcontainer.json`-tiedostossa, joka sijaitsee `.devcontainer/`-kansiossa tämän repositorion juurella.

Aktivoidaksesi kehityskontin, käynnistä se [GitHub Codespacesissa](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (pilvipohjainen suoritusympäristö) tai [Docker Desktopissa](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (paikallisesti laitteella). Lue [tämä dokumentaatio](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) saadaksesi lisätietoja kehityskonttien toiminnasta VS Codessa.  

> [!TIP]  
> Suosittelemme käyttämään GitHub Codespacesia nopeaan aloitukseen minimaalisella vaivalla. Se tarjoaa avokätisen [ilmaisen käyttökiintiön](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) henkilökohtaisille tileille. Konfiguroi [aikakatkaisut](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) lopettaaksesi tai poistaaksesi käyttämättömät codespacet maksimoidaksesi kiintiön käyttöä.


## 1. Tehtävien suorittaminen

Jokaisessa oppitunnissa on _valinnaisia_ tehtäviä, jotka voivat olla saatavilla yhdessä tai useammassa ohjelmointikielessä, kuten: Python, .NET/C#, Java ja JavaScript/TypeScript. Tämä osio tarjoaa yleisiä ohjeita tehtävien suorittamiseen.

### 1.1 Python-tehtävät

Python-tehtävät ovat joko sovelluksia (`.py`-tiedostoja) tai Jupyter-notebookeja (`.ipynb`-tiedostoja). 
- Ajaaksesi notebookin, avaa se Visual Studio Codessa, klikkaa _Select Kernel_ (oikealla ylhäällä) ja valitse oletus Python 3 -vaihtoehto. Voit nyt _Run All_ suorittaaksesi notebookin.
- Ajaaksesi Python-sovelluksia komentoriviltä, seuraa tehtäväkohtaisia ohjeita varmistaaksesi, että valitset oikeat tiedostot ja annat tarvittavat argumentit.

## 2. Palveluntarjoajien konfigurointi

Tehtävät **voivat** olla asetettu toimimaan yhden tai useamman suuren kielimallin (LLM) käyttöönoton kanssa tuetun palveluntarjoajan, kuten OpenAI, Azure tai Hugging Face, kautta. Nämä tarjoavat _hostatun päätepisteen_ (API), jota voimme käyttää ohjelmallisesti oikeilla tunnuksilla (API-avain tai token). Tässä kurssissa käsittelemme näitä palveluntarjoajia:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) erilaisilla malleilla, mukaan lukien ydin GPT-sarja.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI-malleille keskittyen yritysvalmiuteen
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) avoimen lähdekoodin malleille ja ennustepalvelimelle

**Sinun tulee käyttää omia tilejäsi näissä harjoituksissa**. Tehtävät ovat valinnaisia, joten voit valita yhden, kaikki - tai ei mitään - palveluntarjoajista kiinnostuksesi mukaan. Jotkin ohjeet rekisteröitymiseen:

| Rekisteröityminen | Kustannus | API-avain | Leikkikenttä | Kommentit |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Hinnoittelu](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektiin perustuva](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Ei-koodia, verkko](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Useita malleja saatavilla |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Hinnoittelu](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK-pikakäynnistys](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio-pikakäynnistys](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Täytyy hakea etukäteen](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Hinnoittelu](https://huggingface.co/pricing) | [Pääsytokenit](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chatilla on rajoitetusti malleja](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Noudata alla olevia ohjeita _konfiguroidaksesi_ tämä repositorio eri palveluntarjoajien käyttöön. Tehtävät, jotka vaativat tietyn palveluntarjoajan, sisältävät jonkin näistä tageista tiedostonimessään:
 - `aoai` - vaatii Azure OpenAI -päätepisteen, avaimen
 - `oai` - vaatii OpenAI -päätepisteen, avaimen
 - `hf` - vaatii Hugging Face -tokenin

Voit konfiguroida yhden, ei mitään tai kaikki palveluntarjoajat. Asiaan liittyvät tehtävät yksinkertaisesti epäonnistuvat, jos tunnuksia puuttuu.

###  2.1. Luo `.env`-tiedosto

Oletamme, että olet jo lukenut yllä olevat ohjeet ja rekisteröitynyt asianmukaisen palveluntarjoajan kanssa sekä saanut tarvittavat tunnukset (API_KEY tai token). Azure OpenAI:n tapauksessa oletamme, että sinulla on myös voimassa oleva Azure OpenAI -palvelun (päätepiste) käyttöönotto, jossa on vähintään yksi GPT-malli otettu käyttöön keskustelun täydentämiseksi.

Seuraava vaihe on konfiguroida **paikalliset ympäristömuuttujasi** seuraavasti:


1. Katso juurikansiosta `.env.copy`-tiedostoa, jonka sisältö on seuraavanlainen:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopioi tiedosto `.env`-tiedostoksi alla olevan komennon avulla. Tämä tiedosto on _gitignore-d_, pitäen salaisuudet turvassa.

   ```bash
   cp .env.copy .env
   ```

3. Täytä arvot (korvaa paikkamerkit oikealla puolella `=`) kuten seuraavassa osiossa kuvataan.

3. (Vaihtoehto) Jos käytät GitHub Codespacesia, sinulla on mahdollisuus tallentaa ympäristömuuttujat _Codespaces-salaisuuksina_ tähän repositorioon liittyen. Tässä tapauksessa sinun ei tarvitse luoda paikallista .env-tiedostoa. **Huomaa kuitenkin, että tämä vaihtoehto toimii vain, jos käytät GitHub Codespacesia.** Sinun on silti luotava .env-tiedosto, jos käytät Docker Desktopia.


### 2.2. Täytä `.env`-tiedosto

Katsotaanpa nopeasti muuttujien nimiä ymmärtääksemme, mitä ne edustavat:

| Muuttuja  | Kuvaus  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Tämä on käyttäjän pääsytoken, jonka asetat profiilissasi |
| OPENAI_API_KEY | Tämä on valtuutusavain palvelun käyttöön ei-Azure OpenAI -päätepisteille |
| AZURE_OPENAI_API_KEY | Tämä on valtuutusavain kyseisen palvelun käyttöön |
| AZURE_OPENAI_ENDPOINT | Tämä on otettu käyttöön Azure OpenAI -resurssin päätepiste |
| AZURE_OPENAI_DEPLOYMENT | Tämä on _tekstin luomisen_ mallin käyttöönottopäätepiste |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Tämä on _tekstin upotusten_ mallin käyttöönottopäätepiste |
| | |

Huomaa: Kaksi viimeistä Azure OpenAI -muuttujaa heijastavat oletusmallia keskustelun täydentämiseen (tekstin luominen) ja vektorihakuun (upotukset) vastaavasti. Ohjeet niiden asettamiseen määritetään asiaan liittyvissä tehtävissä.


### 2.3 Konfiguroi Azure: Portaalista

Azure OpenAI -päätepisteen ja avainarvot löytyvät [Azure-portaalista](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), joten aloitetaan sieltä.

1. Mene [Azure-portaaliin](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klikkaa **Keys and Endpoint** -vaihtoehtoa sivupalkissa (valikossa vasemmalla).
1. Klikkaa **Show Keys** - sinun pitäisi nähdä seuraavat: KEY 1, KEY 2 ja Endpoint.
1. Käytä KEY 1 -arvoa AZURE_OPENAI_API_KEY:lle
1. Käytä Endpoint-arvoa AZURE_OPENAI_ENDPOINT:lle

Seuraavaksi tarvitsemme päätepisteet käyttöönotetuille malleille.

1. Klikkaa **Model deployments** -vaihtoehtoa sivupalkissa (vasemmalla valikossa) Azure OpenAI -resurssille.
1. Kohdesivulla, klikkaa **Manage Deployments**

Tämä vie sinut Azure OpenAI Studio -verkkosivustolle, jossa löydämme muut arvot kuten alla kuvataan.

### 2.4 Konfiguroi Azure: Studiosta

1. Siirry [Azure OpenAI Studioon](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **resurssistasi** kuten yllä kuvattiin.
1. Klikkaa **Deployments**-välilehteä (sivupalkki, vasemmalla) nähdäksesi tällä hetkellä käyttöön otetut mallit.
1. Jos haluttu malli ei ole otettu käyttöön, käytä **Create new deployment** sen käyttöön ottamiseksi.
1. Tarvitset _tekstin luomisen_ mallin - suosittelemme: **gpt-35-turbo**
1. Tarvitset _tekstin upotusten_ mallin - suosittelemme **text-embedding-ada-002**

Päivitä nyt ympäristömuuttujat heijastamaan _käyttöönottotunnusta_, jota käytettiin. Tämä on tyypillisesti sama kuin mallin nimi, ellei sitä muutettu eksplisiittisesti. Joten esimerkiksi sinulla saattaa olla:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Älä unohda tallentaa .env-tiedostoa, kun olet valmis**. Voit nyt sulkea tiedoston ja palata ohjeisiin notebookin suorittamiseksi.

### 2.5 Konfiguroi OpenAI: Profiilista

OpenAI API-avaimesi löytyy [OpenAI-tililtäsi](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jos sinulla ei ole avainta, voit rekisteröityä tilille ja luoda API-avaimen. Kun sinulla on avain, voit käyttää sitä täyttämään `OPENAI_API_KEY`-muuttujan `.env`-tiedostossa.

### 2.6 Konfiguroi Hugging Face: Profiilista

Hugging Face -tokenisi löytyy profiilistasi kohdasta [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Älä julkaise tai jaa näitä julkisesti. Sen sijaan, luo uusi token tämän projektin käyttöön ja kopioi se `.env`-tiedostoon `HUGGING_FACE_API_KEY`-muuttujan alle. _Huom:_ Tämä ei ole teknisesti API-avain, mutta sitä käytetään autentikointiin, joten pidämme nimeämiskäytännön johdonmukaisena.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää auktoriteettina. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskääntäjää. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.