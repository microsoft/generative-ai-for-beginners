<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T17:41:26+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "fi"
}
-->
# LLM-palveluntarjoajan valinta ja konfigurointi 🔑

Tehtävät **voidaan** myös asettaa toimimaan yhden tai useamman suuren kielimallin (LLM) käyttöönoton kanssa tuetun palveluntarjoajan, kuten OpenAI:n, Azuren tai Hugging Facen kautta. Nämä tarjoavat _isännöidyn päätepisteen_ (API), johon pääsemme käsiksi ohjelmallisesti oikeilla tunnuksilla (API-avain tai token). Tässä kurssissa käsittelemme seuraavia palveluntarjoajia:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), jolla on monipuolisia malleja, mukaan lukien ydinsarja GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst), joka tarjoaa OpenAI-malleja yrityskäyttöön painottuen
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) avoimen lähdekoodin malleihin ja inferenssipalvelimeen

**Tarvitset omat tilit näihin harjoituksiin.** Tehtävät ovat vapaaehtoisia, joten voit valita, otatko käyttöön yhden, kaikki tai et yhtään palveluntarjoajaa oman kiinnostuksesi mukaan. Ohjeita rekisteröitymiseen:

| Rekisteröityminen | Hinta | API-avain | Playground | Kommentit |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Hinnoittelu](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektikohtainen](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Useita malleja saatavilla |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Hinnoittelu](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK-pika-aloitus](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio-pika-aloitus](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Pääsyyn pitää hakea etukäteen](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Hinnoittelu](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chatissa rajallinen määrä malleja](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Seuraa alla olevia ohjeita _konfiguroidaksesi_ tämän repostaation eri palveluntarjoajien käyttöön. Tehtävät, jotka vaativat tiettyä palveluntarjoajaa, sisältävät jonkin seuraavista tunnisteista tiedostonimessään:

- `aoai` - vaatii Azure OpenAI -päätepisteen ja avaimen
- `oai` - vaatii OpenAI-päätepisteen ja avaimen
- `hf` - vaatii Hugging Face -tokenin

Voit konfiguroida yhden, ei yhtään tai kaikki palveluntarjoajat. Niihin liittyvät tehtävät antavat virheilmoituksen, jos tunnuksia puuttuu.

## Luo `.env`-tiedosto

Oletamme, että olet jo lukenut yllä olevat ohjeet, rekisteröitynyt sopivalle palveluntarjoajalle ja hankkinut tarvittavat tunnukset (API_KEY tai token). Azuren tapauksessa olet myös ottanut käyttöön Azure OpenAI -palvelun (päätepisteen), jossa on vähintään yksi GPT-malli keskustelun tuottamiseen.

Seuraavaksi konfiguroidaan **paikalliset ympäristömuuttujat** näin:

1. Etsi juurikansiosta `.env.copy`-tiedosto, jonka sisältö näyttää tältä:

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

2. Kopioi tämä tiedosto nimelle `.env` alla olevalla komennolla. Tämä tiedosto on _gitignore_-listalla, joten salaisuudet pysyvät turvassa.

   ```bash
   cp .env.copy .env
   ```

3. Täytä arvot (korvaa oikeanpuoleiset paikkamerkit `=`-merkin jälkeen) seuraavan osion ohjeiden mukaan.

4. (Valinnainen) Jos käytät GitHub Codespacesia, voit tallentaa ympäristömuuttujat _Codespaces secrets_ -toiminnolla tähän repoon liitettynä. Tällöin sinun ei tarvitse luoda paikallista .env-tiedostoa. **Huomaa kuitenkin, että tämä toimii vain, jos käytät GitHub Codespacesia.** Jos käytät Docker Desktopia, .env-tiedosto on silti luotava.

## Täytä `.env`-tiedosto

Katsotaan nopeasti muuttujien nimet ja mitä ne tarkoittavat:

| Muuttuja  | Kuvaus  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Käyttäjätunnus, jonka loit profiiliisi |
| OPENAI_API_KEY | Tunnus, jolla käytät palvelua ei-Azure OpenAI -päätepisteisiin |
| AZURE_OPENAI_API_KEY | Tunnus, jolla käytät kyseistä palvelua |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI -resurssin käyttöönotettu päätepiste |
| AZURE_OPENAI_DEPLOYMENT | _Tekstin generoinnin_ mallin käyttöönoton nimi |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _Tekstin upotusten_ mallin käyttöönoton nimi |
| | |

Huom: Kaksi viimeistä Azure OpenAI -muuttujaa viittaavat oletusmalliin keskustelun tuottamiseen (tekstin generointi) ja vektorihakuun (upotukset). Ohjeet niiden asettamiseen annetaan asiaankuuluvissa tehtävissä.

## Azuren konfigurointi: Portaalista

Azure OpenAI -päätepiste ja avain löytyvät [Azure-portaalista](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), joten aloitetaan sieltä.

1. Mene [Azure-portaaliin](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Valitse sivupalkista **Keys and Endpoint** (Avaimet ja päätepiste).
1. Klikkaa **Show Keys** (Näytä avaimet) – näet KEY 1, KEY 2 ja Endpoint.
1. Käytä KEY 1 -arvoa AZURE_OPENAI_API_KEY:lle
1. Käytä Endpoint-arvoa AZURE_OPENAI_ENDPOINT:lle

Seuraavaksi tarvitsemme käyttöönotettujen mallien päätepisteet.

1. Valitse sivupalkista (vasen valikko) **Model deployments** Azure OpenAI -resurssille.
1. Kohdesivulla klikkaa **Manage Deployments**

Tämä vie sinut Azure OpenAI Studio -sivustolle, josta löydämme muut arvot alla kuvatulla tavalla.

## Azuren konfigurointi: Studiosta

1. Siirry [Azure OpenAI Studioon](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **resurssisi kautta** yllä kuvatusti.
1. Klikkaa **Deployments**-välilehteä (vasen sivupalkki) nähdäksesi käytössä olevat mallit.
1. Jos haluamaasi mallia ei ole otettu käyttöön, käytä **Create new deployment** -toimintoa.
1. Tarvitset _tekstin generointi_ -mallin – suosittelemme: **gpt-35-turbo**
1. Tarvitset _tekstin upotus_ -mallin – suosittelemme **text-embedding-ada-002**

Päivitä nyt ympäristömuuttujat vastaamaan käyttöönoton nimeä. Tämä on yleensä sama kuin mallin nimi, ellei sitä ole erikseen muutettu. Esimerkiksi näin:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Muista tallentaa .env-tiedosto lopuksi.** Voit nyt sulkea tiedoston ja palata ohjeisiin notebookin suorittamista varten.

## OpenAI:n konfigurointi: Profiilista

OpenAI API-avaimesi löytyy [OpenAI-tililtäsi](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jos sinulla ei vielä ole avainta, voit luoda tilin ja luoda API-avaimen. Kun sinulla on avain, voit syöttää sen `.env`-tiedoston `OPENAI_API_KEY`-muuttujaan.

## Hugging Facen konfigurointi: Profiilista

Hugging Face -tokenisi löytyy profiilistasi kohdasta [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Älä julkaise tai jaa näitä julkisesti. Luo sen sijaan uusi token tätä projektia varten ja kopioi se `.env`-tiedostoon `HUGGING_FACE_API_KEY`-muuttujan kohdalle. _Huom:_ Tämä ei teknisesti ole API-avain, mutta sitä käytetään tunnistautumiseen, joten pidämme tämän nimityksen yhtenäisyyden vuoksi.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen omalla kielellä tulee pitää ensisijaisena lähteenä. Kriittisissä tapauksissa suositellaan ammattimaista ihmiskääntäjää. Emme ole vastuussa tämän käännöksen käytöstä mahdollisesti aiheutuvista väärinkäsityksistä tai tulkintavirheistä.