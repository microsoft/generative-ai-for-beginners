# Préparation des données de transcription

Les scripts de préparation des données de transcription téléchargent les transcriptions vidéo YouTube et les préparent pour une utilisation avec l'exemple Recherche sémantique avec OpenAI Embeddings et Fonctions.

Les scripts de préparation des données de transcription ont été testés sur les dernières versions de Windows 11, macOS Ventura et Ubuntu 22.04 (et versions supérieures).

## Créer les ressources requises pour le service Azure OpenAI

> [!IMPORTANT]
> Nous vous suggérons de mettre à jour l'interface en ligne de commande Azure CLI vers la dernière version pour garantir la compatibilité avec OpenAI
> Voir [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Créez un groupe de ressources

> [!NOTE]
> Pour ces instructions, nous utilisons le groupe de ressources nommé "semantic-video-search" dans East US.
> Vous pouvez changer le nom du groupe de ressources, mais en changeant l'emplacement des ressources,
> vérifiez la [table de disponibilité des modèles](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Créez une ressource Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Obtenez le point de terminaison et les clés pour utilisation dans cette application

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Déployez les modèles suivants :
   - `text-embedding-ada-002` version `2` ou supérieure, nommé `text-embedding-ada-002`
   - `gpt-5-mini` nommé `gpt-5-mini`

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
    --deployment-name gpt-5-mini \
    --model-name gpt-5-mini \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## Logiciels requis

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ou supérieur

## Variables d'environnement

Les variables d'environnement suivantes sont nécessaires pour exécuter les scripts de préparation des données de transcription YouTube.

### Sur Windows

Il est recommandé d'ajouter les variables aux variables d'environnement `utilisateur`.
`Démarrer Windows` > `Modifier les variables d’environnement système` > `Variables d’environnement` > `Variables utilisateur` pour [USER] > `Nouveau`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Vous pouvez ajouter les variables d'environnement à votre profil PowerShell.

```powershell
$env:AZURE_OPENAI_API_KEY = "<votre clé API du service Azure OpenAI>"
$env:AZURE_OPENAI_ENDPOINT = "<votre point de terminaison du service Azure OpenAI>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<votre nom de déploiement du modèle du service Azure OpenAI>"
$env:GOOGLE_DEVELOPER_API_KEY = "<votre clé API développeur Google>"
``` -->

### Sur Linux et macOS

Il est recommandé d'ajouter les exportations suivantes à votre fichier `~/.bashrc` ou `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Installer les bibliothèques Python requises

1. Installez le [client git](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) si ce n'est pas déjà fait.
1. À partir d'une fenêtre `Terminal`, clonez l'exemple dans votre dossier de repo préféré.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Naviguez vers le dossier `data_prep`.

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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->