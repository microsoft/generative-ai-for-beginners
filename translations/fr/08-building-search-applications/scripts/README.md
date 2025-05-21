<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T10:25:55+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "fr"
}
-->
# Préparation des données de transcription

Les scripts de préparation des données de transcription téléchargent les transcriptions de vidéos YouTube et les préparent pour une utilisation avec l'exemple de Recherche Sémantique avec OpenAI Embeddings et Functions.

Les scripts de préparation des données de transcription ont été testés sur les dernières versions de Windows 11, macOS Ventura et Ubuntu 22.04 (et au-delà).

## Créer les ressources nécessaires pour le service Azure OpenAI

> [!IMPORTANT]
> Nous vous suggérons de mettre à jour l'Azure CLI à la dernière version pour garantir la compatibilité avec OpenAI
> Voir [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Créer un groupe de ressources

> [!NOTE]
> Pour ces instructions, nous utilisons le groupe de ressources nommé "semantic-video-search" dans l'Est des États-Unis.
> Vous pouvez changer le nom du groupe de ressources, mais lorsque vous modifiez l'emplacement des ressources,
> vérifiez le [tableau de disponibilité des modèles](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Créer une ressource Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Obtenez le point de terminaison et les clés pour l'utilisation dans cette application

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Déployez les modèles suivants :
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

## Logiciels requis

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ou supérieur

## Variables d'environnement

Les variables d'environnement suivantes sont nécessaires pour exécuter les scripts de préparation des données de transcription YouTube.

### Sur Windows

Il est recommandé d'ajouter les variables à votre `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Sur Linux et macOS

Il est recommandé d'ajouter les exports suivants à votre fichier `~/.bashrc` or `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Installer les bibliothèques Python requises

1. Installez le [client git](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) s'il n'est pas déjà installé.
1. Depuis une fenêtre de `Terminal`, clonez l'exemple dans votre dossier de dépôt préféré.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Accédez au dossier `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Créez un environnement virtuel Python.

    Sur Windows :

    ```powershell
    python -m venv .venv
    ```

    Sur macOS et Linux :

    ```bash
    python3 -m venv .venv
    ```

1. Activez l'environnement virtuel Python.

   Sur Windows :

   ```powershell
   .venv\Scripts\activate
   ```

   Sur macOS et Linux :

   ```bash
   source .venv/bin/activate
   ```

1. Installez les bibliothèques requises.

   Sur Windows :

   ```powershell
   pip install -r requirements.txt
   ```

   Sur macOS et Linux :

   ```bash
   pip3 install -r requirements.txt
   ```

## Exécuter les scripts de préparation des données de transcription YouTube

### Sur Windows

```powershell
.\transcripts_prepare.ps1
```

### Sur macOS et Linux

```bash
./transcripts_prepare.sh
```

**Clause de non-responsabilité** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction professionnelle humaine. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.