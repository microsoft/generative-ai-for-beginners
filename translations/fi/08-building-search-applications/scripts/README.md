<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T18:51:53+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "fi"
}
-->
# Puheentunnistusdatan valmistelu

Puheentunnistusdatan valmisteluskriptit lataavat YouTube-videoiden tekstitykset ja valmistelevat ne käytettäväksi Semantic Search with OpenAI Embeddings and Functions -esimerkin kanssa.

Puheentunnistusdatan valmisteluskriptit on testattu uusimmilla Windows 11, macOS Ventura ja Ubuntu 22.04 (ja uudemmat) julkaisuilla.

## Luo tarvittavat Azure OpenAI Service -resurssit

> [!IMPORTANT]
> Suosittelemme päivittämään Azure CLI:n uusimpaan versioon varmistaaksesi yhteensopivuuden OpenAI:n kanssa
> Katso [dokumentaatio](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Luo resurssiryhmä

> [!NOTE]
> Näissä ohjeissa käytämme resurssiryhmää nimeltä "semantic-video-search" Itäisessä Yhdysvalloissa.
> Voit muuttaa resurssiryhmän nimeä, mutta kun muutat resurssien sijaintia, 
> tarkista [mallien saatavuustaulukko](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Luo Azure OpenAI Service -resurssi.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Hanki päätepiste ja avaimet tämän sovelluksen käyttöön

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Ota käyttöön seuraavat mallit:
   - `text-embedding-ada-002` version `2` or greater, named `text-embedding-ada-002`
   - `gpt-35-turbo` version `0613` or greater, named `gpt-35-turbo`

```console
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name text-embedding-ada-002 \
    --model-name text-embedding-ada-002 \
    --model-version "2"  \
    --model-format OpenAI \
    --scale-settings-scale-type "Standard"
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name gpt-35-turbo \
    --model-name gpt-35-turbo \
    --model-version "0613"  \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## Tarvittava ohjelmisto

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) tai uudempi

## Ympäristömuuttujat

Seuraavat ympäristömuuttujat ovat tarpeen YouTube-puheentunnistusdatan valmisteluskriptien suorittamiseen.

### Windowsissa

Suosittelemme lisäämään muuttujat käyttäjäkohtaisiin `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Linuxissa ja macOS:ssa

Suosittelemme lisäämään seuraavat vientikomentorivit tiedostoon `~/.bashrc` or `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Asenna tarvittavat Python-kirjastot

1. Asenna [git-asiakasohjelma](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), jos se ei ole jo asennettuna.
1. Avaa `Terminal`-ikkuna ja kloonaa esimerkki haluamaasi repo-kansioon.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Siirry `data_prep`-kansioon.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Luo Python-virtuaaliympäristö.

    Windowsissa:

    ```powershell
    python -m venv .venv
    ```

    macOS:ssa ja Linuxissa:

    ```bash
    python3 -m venv .venv
    ```

1. Aktivoi Python-virtuaaliympäristö.

   Windowsissa:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS:ssa ja Linuxissa:

   ```bash
   source .venv/bin/activate
   ```

1. Asenna tarvittavat kirjastot.

   Windowsissa:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS:ssa ja Linuxissa:

   ```bash
   pip3 install -r requirements.txt
   ```

## Suorita YouTube-puheentunnistusdatan valmisteluskriptit

### Windowsissa

```powershell
.\transcripts_prepare.ps1
```

### macOS:ssa ja Linuxissa

```bash
./transcripts_prepare.sh
```

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä AI-käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomaa, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa mahdollisista väärinkäsityksistä tai virheellisistä tulkinnoista, jotka johtuvat tämän käännöksen käytöstä.