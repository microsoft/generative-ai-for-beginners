# Choisir et configurer un fournisseur LLM 🔑

Les travaux **peuvent** également être configurés pour fonctionner avec un ou plusieurs déploiements de Large Language Model (LLM) via un fournisseur de services supporté comme OpenAI, Azure ou Hugging Face. Ceux-ci fournissent un _point de terminaison hébergé_ (API) auquel nous pouvons accéder de manière programmatique avec les bonnes informations d'identification (clé API ou jeton). Dans ce cours, nous discutons de ces fournisseurs :

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) avec divers modèles y compris la série principale GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) pour les modèles OpenAI avec une orientation sur la préparation entreprise
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) pour un point de terminaison unique et une clé API permettant d’accéder à des centaines de modèles d’OpenAI, Meta, Mistral, Cohere, Microsoft et plus encore (remplace GitHub Models, qui sera retiré à la fin de juillet 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) pour des modèles open source et un serveur d’inférence
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ou [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) si vous préférez exécuter des modèles entièrement hors ligne sur votre propre appareil, sans abonnement cloud nécessaire

**Vous devrez utiliser vos propres comptes pour ces exercices**. Les travaux sont optionnels pour que vous puissiez choisir d’en configurer un, tous ou aucun des fournisseurs selon vos intérêts. Voici quelques conseils pour l’inscription :

| Inscription | Coût | Clé API | Terrain de jeu | Commentaires |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Tarification](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Basée sur projet](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Sans code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Plusieurs modèles disponibles |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Tarification](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Démarrage rapide SDK](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Démarrage rapide Studio](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Doit postuler en avance pour accès](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Tarification](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Page d’aperçu du projet](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Terrain de jeu Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Offre gratuite disponible ; un point de terminaison + clé pour plusieurs fournisseurs de modèles |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Tarification](https://huggingface.co/pricing) | [Jetons d’accès](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat a des modèles limités](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Gratuit (s’exécute sur votre appareil) | Non requis | [CLI/SDK local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Point de terminaison compatible OpenAI complètement hors ligne |
| | | | | |

Suivez les instructions ci-dessous pour _configurer_ ce dépôt pour une utilisation avec différents fournisseurs. Les travaux nécessitant un fournisseur spécifique contiendront l’une de ces balises dans leur nom de fichier :

- `aoai` - nécessite un point de terminaison Azure OpenAI, clé
- `oai` - nécessite un point de terminaison OpenAI, clé
- `hf` - nécessite un jeton Hugging Face
- `githubmodels` - nécessite un point de terminaison Microsoft Foundry Models, clé (GitHub Models sera retiré à la fin de juillet 2026)

Vous pouvez configurer un, aucun ou tous les fournisseurs. Les travaux associés généreront simplement une erreur en cas d’identifiants manquants.

## Créer le fichier `.env`

Nous supposons que vous avez déjà lu les instructions ci-dessus, créé un compte chez le fournisseur concerné, et obtenu les informations d’authentification nécessaires (API_KEY ou jeton). Dans le cas d’Azure OpenAI, nous supposons également que vous avez un déploiement valide d’un service Azure OpenAI (point de terminaison) avec au moins un modèle GPT déployé pour la complétion de chat.

L’étape suivante consiste à configurer vos **variables d’environnement locales** comme suit :

1. Cherchez dans le dossier racine un fichier `.env.copy` qui devrait contenir ce type de contenu :

   ```bash
   # Fournisseur OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI dans Microsoft Foundry
   ## (Le service Azure OpenAI fait désormais partie de Microsoft Foundry : https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Par défaut est défini ! (version API GA stable actuelle)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Modèles Microsoft Foundry (catalogue de modèles multi-fournisseurs, remplace les modèles GitHub, qui seront retirés fin juillet 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Copiez ce fichier en `.env` avec la commande ci-dessous. Ce fichier est _ignoré par git_, protégeant ainsi les secrets.

   ```bash
   cp .env.copy .env
   ```

3. Remplissez les valeurs (remplacez les espaces réservés à droite du `=`) comme décrit dans la section suivante.

4. (Optionnel) Si vous utilisez GitHub Codespaces, vous pouvez sauvegarder les variables d’environnement comme _secrets Codespaces_ associés à ce dépôt. Dans ce cas, vous n’aurez pas besoin de configurer un fichier .env local. **Cependant, cette option ne fonctionne que si vous utilisez GitHub Codespaces.** Vous devrez quand même configurer le fichier .env si vous utilisez Docker Desktop à la place.

## Remplir le fichier `.env`

Regardons rapidement les noms des variables pour comprendre ce qu’elles représentent :

| Variable  | Description  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | C’est le jeton d’accès utilisateur que vous configurez dans votre profil |
| OPENAI_API_KEY | C’est la clé d’autorisation pour utiliser le service des points de terminaison OpenAI non Azure |
| AZURE_OPENAI_API_KEY | C’est la clé d’autorisation pour utiliser ce service |
| AZURE_OPENAI_ENDPOINT | C’est le point de terminaison déployé pour une ressource Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | C’est le point de terminaison de déploiement du modèle de _génération de texte_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | C’est le point de terminaison de déploiement du modèle de _vecteurs de texte_ |
| AZURE_INFERENCE_ENDPOINT | C’est le point de terminaison pour votre projet Microsoft Foundry, utilisé pour Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | C’est la clé API pour votre projet Microsoft Foundry |
| | |

Note : Les deux dernières variables Azure OpenAI reflètent un modèle par défaut pour la complétion de chat (génération de texte) et la recherche vectorielle (embeddings) respectivement. Les instructions de configuration seront définies dans les travaux concernés.

## Configurer Azure OpenAI : depuis le portail

> **Note :** Le service Azure OpenAI fait maintenant partie de [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Les ressources et déploiements apparaissent toujours dans le portail Azure, mais la gestion quotidienne des modèles (déploiements, terrain de jeu, surveillance) se fait désormais dans le portail Foundry au lieu de l’ancien "Azure OpenAI Studio" autonome.

Les valeurs du point de terminaison et de la clé Azure OpenAI se trouvent dans le [portail Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), commençons donc par là.

1. Allez sur le [portail Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Cliquez sur l’option **Clés et point de terminaison** dans la barre latérale (menu à gauche).
1. Cliquez sur **Afficher les clés** - vous devriez voir : CLÉ 1, CLÉ 2 et Point de terminaison.
1. Utilisez la valeur de la CLÉ 1 pour AZURE_OPENAI_API_KEY
1. Utilisez la valeur du point de terminaison pour AZURE_OPENAI_ENDPOINT

Ensuite, nous avons besoin des points de terminaison pour les modèles spécifiques que nous avons déployés.

1. Cliquez sur l’option **Déploiements de modèles** dans la barre latérale (menu à gauche) pour la ressource Azure OpenAI.
1. Sur la page de destination, cliquez sur **Aller au portail Microsoft Foundry** (ou **Gérer les déploiements**, selon votre type de ressource)

Cela vous mènera au portail Microsoft Foundry, où vous trouverez les autres valeurs comme décrit ci-dessous.

## Configurer Azure OpenAI : depuis le portail Microsoft Foundry

1. Accédez au [portail Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **depuis votre ressource** comme décrit ci-dessus.
1. Cliquez sur l’onglet **Déploiements** (barre latérale, gauche) pour voir les modèles actuellement déployés.
1. Si le modèle souhaité n’est pas déployé, utilisez **Déployer un modèle** pour le déployer à partir du [catalogue de modèles](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Vous aurez besoin d’un modèle de _génération de texte_ - nous recommandons : **gpt-5-mini**
1. Vous aurez besoin d’un modèle de _vecteurs de texte_ - nous recommandons **text-embedding-3-small**

Mettez maintenant à jour les variables d’environnement pour refléter le _nom du déploiement_ utilisé. Ceci sera généralement le même que le nom du modèle sauf si vous l’avez explicitement changé. Par exemple, vous pourriez avoir :

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**N’oubliez pas de sauvegarder le fichier .env une fois terminé**. Vous pouvez maintenant fermer le fichier et revenir aux instructions pour exécuter le notebook.

## Configurer OpenAI : depuis le profil

Votre clé API OpenAI se trouve dans votre [compte OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Si vous n’en avez pas, vous pouvez créer un compte et générer une clé API. Une fois que vous avez la clé, utilisez-la pour remplir la variable `OPENAI_API_KEY` dans le fichier `.env`.

## Configurer Hugging Face : depuis le profil

Votre jeton Hugging Face se trouve dans votre profil sous [Jetons d’accès](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Ne publiez pas ou ne partagez pas ceux-ci publiquement. Créez plutôt un nouveau jeton pour l’usage de ce projet et copiez-le dans le fichier `.env` sous la variable `HUGGING_FACE_API_KEY`. _Note :_ Ce n’est techniquement pas une clé API mais elle est utilisée pour l’authentification, donc nous gardons cette convention de nommage pour la cohérence.

## Configurer Microsoft Foundry Models : depuis le portail

> **Note :** GitHub Models sera retiré à la fin de juillet 2026. Microsoft Foundry Models est le remplaçant direct, offrant le même catalogue de modèles gratuit à essayer et l’expérience SDK d’Azure AI Inference / SDK OpenAI.

1. Allez sur [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) et créez (ou ouvrez) un projet Foundry.
1. Parcourez le [catalogue de modèles](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) et déployez un modèle, par exemple `gpt-5-mini`.
1. Sur la page **Aperçu** du projet, copiez le **point de terminaison** et la **clé API**.
1. Utilisez la valeur du point de terminaison pour `AZURE_INFERENCE_ENDPOINT` et la valeur de la clé pour `AZURE_INFERENCE_CREDENTIAL` dans votre fichier `.env`.

## Fournisseurs hors ligne / locaux

Si vous préférez ne pas utiliser d’abonnement cloud du tout, vous pouvez exécuter des modèles ouverts compatibles directement sur votre propre appareil :

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - l’environnement d’exécution local de Microsoft. Il sélectionne automatiquement le meilleur fournisseur d’exécution (NPU, GPU ou CPU) et expose un point de terminaison compatible OpenAI, vous permettant de réutiliser la plupart du code d’exemple de ce cours avec un minimum de modifications. Consultez la [documentation Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) pour démarrer, ou installez-le via `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - une alternative populaire pour exécuter localement des modèles ouverts tels que Llama, Phi, Mistral et Gemma.


Voir [Leçon 19 : Construire avec des SLM](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) pour des exemples pratiques utilisant les deux options.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->