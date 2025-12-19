<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b5b016b0eb8a1cef2e3097620d8aa23",
  "translation_date": "2025-12-19T15:41:41+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "fi"
}
-->
# LLM-toimittajan valinta ja konfigurointi 🔑

Tehtävät **voivat** myös olla asetettu toimimaan yhtä tai useampaa Suurten Kielen Mallien (LLM) käyttöönottoa vastaan tuetun palveluntarjoajan, kuten OpenAI:n, Azuren tai Hugging Facen kautta. Nämä tarjoavat _isännöidyn päätepisteen_ (API), johon voimme ohjelmallisesti päästä käsiksi oikeilla tunnistetiedoilla (API-avain tai token). Tässä kurssissa käsittelemme näitä palveluntarjoajia:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) monipuolisilla malleilla, mukaan lukien ydinsarja GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI-malleille, joissa painotetaan yritysvalmiutta
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) avoimen lähdekoodin malleille ja päättelypalvelimelle

**Tarvitset omat tilisi näitä harjoituksia varten**. Tehtävät ovat valinnaisia, joten voit valita yhden, kaikki tai ei yhtään palveluntarjoajaa kiinnostuksesi mukaan. Rekisteröitymisohjeita:

| Rekisteröityminen | Hinta | API-avain | Playground | Kommentit |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Hinnoittelu](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektikohtainen](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Ei-koodia, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Useita malleja saatavilla |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Hinnoittelu](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK pika-aloitus](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio pika-aloitus](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Pääsyyn on haettava etukäteen](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Hinnoittelu](https://huggingface.co/pricing) | [Käyttöoikeustokenit](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chatissa on rajattu määrä malleja](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Seuraa alla olevia ohjeita tämän repositorion _konfiguroimiseksi_ eri palveluntarjoajien käyttöön. Tehtävissä, jotka vaativat tietyn palveluntarjoajan, tiedoston nimessä on jokin näistä tunnisteista:

- `aoai` - vaatii Azure OpenAI -päätepisteen ja avaimen
- `oai` - vaatii OpenAI-päätepisteen ja avaimen
- `hf` - vaatii Hugging Face -tokenin

Voit konfiguroida yhden, ei yhtään tai kaikki palveluntarjoajat. Asiaankuuluvat tehtävät antavat virheen puuttuvista tunnistetiedoista.

## Luo `.env`-tiedosto

Oletamme, että olet jo lukenut yllä olevan ohjeistuksen, rekisteröitynyt asianmukaiselle palveluntarjoajalle ja saanut tarvittavat tunnistetiedot (API_KEY tai token). Azuren OpenAI:n tapauksessa oletamme myös, että sinulla on voimassa oleva käyttöönotto Azure OpenAI -palvelusta (päätepiste) ja vähintään yksi GPT-malli on otettu käyttöön keskustelun täydentämistä varten.

Seuraava vaihe on konfiguroida **paikalliset ympäristömuuttujat** seuraavasti:

1. Etsi juurihakemistosta `.env.copy`-tiedosto, jonka sisältö on suunnilleen seuraava:

   ```bash
   # OpenAI-palveluntarjoaja
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Oletus on asetettu!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopioi tiedosto nimellä `.env` alla olevalla komennolla. Tämä tiedosto on _gitignore-merkattu_, joten salaisuudet pysyvät turvassa.

   ```bash
   cp .env.copy .env
   ```

3. Täytä arvot (korvaa oikealla puolella olevat paikkamerkit) seuraavan osion ohjeiden mukaan.

4. (Valinnainen) Jos käytät GitHub Codespacesia, voit tallentaa ympäristömuuttujat _Codespaces-salaisuuksina_ tähän repositorioon liittyen. Tällöin sinun ei tarvitse luoda paikallista .env-tiedostoa. **Huomaa kuitenkin, että tämä vaihtoehto toimii vain GitHub Codespacesin kanssa.** Jos käytät Docker Desktopia, sinun on silti luotava .env-tiedosto.

## Täytä `.env`-tiedosto

Katsotaan nopeasti muuttujien nimet ja mitä ne tarkoittavat:

| Muuttuja  | Kuvaus  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Tämä on käyttäjän käyttöoikeustoken, jonka olet asettanut profiilissasi |
| OPENAI_API_KEY | Tämä on valtuutusavain palvelun käyttöön ei-Azure OpenAI -päätepisteissä |
| AZURE_OPENAI_API_KEY | Tämä on valtuutusavain kyseisen palvelun käyttöön |
| AZURE_OPENAI_ENDPOINT | Tämä on otettu käyttöön oleva päätepiste Azure OpenAI -resurssille |
| AZURE_OPENAI_DEPLOYMENT | Tämä on _tekstin generoinnin_ mallin käyttöönoton päätepiste |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Tämä on _tekstin upotusten_ mallin käyttöönoton päätepiste |
| | |

Huom: Viimeiset kaksi Azure OpenAI -muuttujaa viittaavat oletusmalliin keskustelun täydentämiseen (tekstin generointi) ja vektorihakuihin (upotukset). Niiden asetusohjeet löytyvät asiaankuuluvista tehtävistä.

## Konfiguroi Azure: Portaalista

Azure OpenAI -päätepisteen ja avaimen arvot löytyvät [Azure-portaalista](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), aloitetaan sieltä.

1. Mene [Azure-portaaliin](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klikkaa sivupalkista (vasen valikko) **Keys and Endpoint** -vaihtoehtoa.
1. Klikkaa **Show Keys** -näet seuraavat: KEY 1, KEY 2 ja Endpoint.
1. Käytä KEY 1 -arvoa AZURE_OPENAI_API_KEY:na
1. Käytä Endpoint-arvoa AZURE_OPENAI_ENDPOINT:na

Seuraavaksi tarvitsemme käyttöönotettujen mallien päätepisteet.

1. Klikkaa Azure OpenAI -resurssin sivupalkista (vasen valikko) **Model deployments** -vaihtoehtoa.
1. Kohdesivulla klikkaa **Manage Deployments**

Tämä vie sinut Azure OpenAI Studio -sivustolle, josta löydämme muut arvot alla kuvatulla tavalla.

## Konfiguroi Azure: Studiosta

1. Siirry [Azure OpenAI Studioon](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **resurssiltasi** kuten yllä on kuvattu.
1. Klikkaa vasemman laidan **Deployments**-välilehteä nähdäksesi käytössä olevat mallit.
1. Jos haluamaasi mallia ei ole otettu käyttöön, käytä **Create new deployment** -toimintoa ottaaksesi sen käyttöön.
1. Tarvitset _tekstin generointiin_ mallin - suosittelemme: **gpt-35-turbo**
1. Tarvitset _tekstin upotuksiin_ mallin - suosittelemme **text-embedding-ada-002**

Päivitä nyt ympäristömuuttujat vastaamaan käytettyä _Deployment name_ -arvoa. Tämä on tyypillisesti sama kuin mallin nimi, ellei sitä ole erikseen muutettu. Esimerkiksi:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Muista tallentaa .env-tiedosto, kun olet valmis**. Voit nyt sulkea tiedoston ja palata ohjeisiin muistiokirjan suorittamiseksi.

## Konfiguroi OpenAI: Profiilista

OpenAI API -avaimesi löytyy [OpenAI-tililtäsi](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jos sinulla ei ole avainta, voit rekisteröityä tilille ja luoda API-avaimen. Saatuasi avaimen voit täyttää `OPENAI_API_KEY`-muuttujan `.env`-tiedostossa.

## Konfiguroi Hugging Face: Profiilista

Hugging Face -tokenisi löytyy profiilistasi kohdasta [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Älä julkaise tai jaa näitä julkisesti. Sen sijaan luo uusi token tätä projektia varten ja kopioi se `.env`-tiedostoon `HUGGING_FACE_API_KEY`-muuttujan alle. _Huom:_ Tämä ei teknisesti ole API-avain, mutta sitä käytetään tunnistautumiseen, joten pidämme nimeämiskäytännön johdonmukaisena.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->