<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T09:01:31+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "fr"
}
-->
# Configurez votre environnement de développement

Nous avons configuré ce dépôt et ce cours avec un [conteneur de développement](https://containers.dev?WT.mc_id=academic-105485-koreyst) qui dispose d'un environnement d'exécution universel pouvant prendre en charge le développement en Python3, .NET, Node.js et Java. La configuration associée est définie dans le fichier `devcontainer.json` situé dans le dossier `.devcontainer/` à la racine de ce dépôt.

Pour activer le conteneur de développement, lancez-le dans [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (pour un environnement d'exécution hébergé dans le cloud) ou dans [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (pour un environnement d'exécution hébergé localement). Lisez [cette documentation](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) pour plus de détails sur le fonctionnement des conteneurs de développement dans VS Code.

> [!TIP]  
> Nous recommandons d'utiliser GitHub Codespaces pour un démarrage rapide avec un minimum d'effort. Il offre un [quota d'utilisation gratuit](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) généreux pour les comptes personnels. Configurez les [délais d'inactivité](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) pour arrêter ou supprimer les codespaces inactifs afin d'optimiser l'utilisation de votre quota.

## 1. Exécution des devoirs

Chaque leçon comportera des devoirs _optionnels_ qui peuvent être fournis dans une ou plusieurs langues de programmation, notamment : Python, .NET/C#, Java et JavaScript/TypeScript. Cette section fournit des conseils généraux relatifs à l'exécution de ces devoirs.

### 1.1 Devoirs en Python

Les devoirs en Python sont fournis soit sous forme d'applications (fichiers `.py`), soit de notebooks Jupyter (fichiers `.ipynb`).
- Pour exécuter le notebook, ouvrez-le dans Visual Studio Code, puis cliquez sur _Select Kernel_ (en haut à droite) et sélectionnez l'option Python 3 par défaut affichée. Vous pouvez maintenant _Run All_ pour exécuter le notebook.
- Pour exécuter des applications Python depuis la ligne de commande, suivez les instructions spécifiques au devoir pour vous assurer de sélectionner les bons fichiers et de fournir les arguments requis.

## 2. Configuration des fournisseurs

Les devoirs **peuvent** également être configurés pour fonctionner avec un ou plusieurs déploiements de modèles de langage à grande échelle (LLM) via un fournisseur de services pris en charge comme OpenAI, Azure ou Hugging Face. Ceux-ci fournissent un _point de terminaison hébergé_ (API) auquel nous pouvons accéder de manière programmatique avec les bonnes informations d'identification (clé API ou jeton). Dans ce cours, nous discutons de ces fournisseurs :

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) avec divers modèles, y compris la série principale GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) pour les modèles OpenAI avec une orientation sur la préparation à l'entreprise.
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) pour les modèles open-source et le serveur d'inférence.

**Vous devrez utiliser vos propres comptes pour ces exercices**. Les devoirs sont optionnels, vous pouvez donc choisir de configurer un, tous - ou aucun - des fournisseurs en fonction de vos intérêts. Quelques conseils pour l'inscription :

| Inscription | Coût | Clé API | Playground | Commentaires |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Tarification](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Basé sur le projet](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Sans code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Plusieurs modèles disponibles |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Tarification](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Démarrage rapide SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Démarrage rapide Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Doit postuler à l'avance pour l'accès](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Tarification](https://huggingface.co/pricing) | [Jetons d'accès](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat a des modèles limités](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Suivez les instructions ci-dessous pour _configurer_ ce dépôt pour une utilisation avec différents fournisseurs. Les devoirs nécessitant un fournisseur spécifique contiendront l'une de ces balises dans leur nom de fichier :
 - `aoai` - nécessite un point de terminaison Azure OpenAI, clé
 - `oai` - nécessite un point de terminaison OpenAI, clé
 - `hf` - nécessite un jeton Hugging Face

Vous pouvez configurer un, aucun, ou tous les fournisseurs. Les devoirs associés généreront simplement une erreur en cas d'absence de crédentiels.

###  2.1. Créez le fichier `.env`

Nous supposons que vous avez déjà lu les conseils ci-dessus, vous vous êtes inscrit auprès du fournisseur concerné et avez obtenu les informations d'identification d'authentification requises (API_KEY ou jeton). Dans le cas d'Azure OpenAI, nous supposons également que vous avez un déploiement valide d'un service Azure OpenAI (point de terminaison) avec au moins un modèle GPT déployé pour la complétion de chat.

L'étape suivante consiste à configurer vos **variables d'environnement locales** comme suit :

1. Recherchez dans le dossier racine un fichier `.env.copy` qui devrait avoir un contenu comme celui-ci :

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

2. Copiez ce fichier vers `.env` en utilisant la commande ci-dessous. Ce fichier est _gitignore-d_, gardant les secrets en sécurité.

   ```bash
   cp .env.copy .env
   ```

3. Remplissez les valeurs (remplacez les espaces réservés sur le côté droit du `=`) comme décrit dans la section suivante.

3. (Option) Si vous utilisez GitHub Codespaces, vous avez la possibilité d'enregistrer les variables d'environnement en tant que _secrets Codespaces_ associés à ce dépôt. Dans ce cas, vous n'aurez pas besoin de configurer un fichier .env local. **Cependant, notez que cette option fonctionne uniquement si vous utilisez GitHub Codespaces.** Vous devrez toujours configurer le fichier .env si vous utilisez Docker Desktop à la place.

### 2.2. Remplir le fichier `.env`

Jetons un coup d'œil rapide aux noms des variables pour comprendre ce qu'elles représentent :

| Variable  | Description  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | C'est le jeton d'accès utilisateur que vous avez configuré dans votre profil |
| OPENAI_API_KEY | C'est la clé d'autorisation pour utiliser le service pour les points de terminaison OpenAI non-Azure |
| AZURE_OPENAI_API_KEY | C'est la clé d'autorisation pour utiliser ce service |
| AZURE_OPENAI_ENDPOINT | C'est le point de terminaison déployé pour une ressource Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | C'est le point de terminaison de déploiement du modèle _génération de texte_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | C'est le point de terminaison de déploiement du modèle _embeddings de texte_ |
| | |

Note : Les deux dernières variables Azure OpenAI reflètent un modèle par défaut pour la complétion de chat (génération de texte) et la recherche vectorielle (embeddings) respectivement. Les instructions pour les configurer seront définies dans les devoirs pertinents.

### 2.3 Configurer Azure : Depuis le portail

Les valeurs de point de terminaison et de clé Azure OpenAI se trouvent dans le [Portail Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), commençons donc par là.

1. Allez sur le [Portail Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Cliquez sur l'option **Clés et point de terminaison** dans la barre latérale (menu à gauche).
1. Cliquez sur **Afficher les clés** - vous devriez voir les éléments suivants : KEY 1, KEY 2 et Endpoint.
1. Utilisez la valeur de KEY 1 pour AZURE_OPENAI_API_KEY
1. Utilisez la valeur de l'Endpoint pour AZURE_OPENAI_ENDPOINT

Ensuite, nous avons besoin des points de terminaison pour les modèles spécifiques que nous avons déployés.

1. Cliquez sur l'option **Déploiements de modèles** dans la barre latérale (menu de gauche) pour la ressource Azure OpenAI.
1. Dans la page de destination, cliquez sur **Gérer les déploiements**

Cela vous mènera au site web Azure OpenAI Studio, où nous trouverons les autres valeurs comme décrit ci-dessous.

### 2.4 Configurer Azure : Depuis le Studio

1. Accédez à [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **depuis votre ressource** comme décrit ci-dessus.
1. Cliquez sur l'onglet **Déploiements** (barre latérale, à gauche) pour voir les modèles actuellement déployés.
1. Si votre modèle souhaité n'est pas déployé, utilisez **Créer un nouveau déploiement** pour le déployer.
1. Vous aurez besoin d'un modèle _génération de texte_ - nous recommandons : **gpt-35-turbo**
1. Vous aurez besoin d'un modèle _embeddings de texte_ - nous recommandons **text-embedding-ada-002**

Mettez maintenant à jour les variables d'environnement pour refléter le _nom de déploiement_ utilisé. Cela sera généralement identique au nom du modèle à moins que vous ne l'ayez modifié explicitement. Donc, par exemple, vous pourriez avoir :

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**N'oubliez pas de sauvegarder le fichier .env une fois terminé**. Vous pouvez maintenant quitter le fichier et revenir aux instructions pour exécuter le notebook.

### 2.5 Configurer OpenAI : Depuis le profil

Votre clé API OpenAI se trouve dans votre [compte OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Si vous n'en avez pas, vous pouvez créer un compte et créer une clé API. Une fois que vous avez la clé, vous pouvez l'utiliser pour remplir la variable `OPENAI_API_KEY` dans le fichier `.env`.

### 2.6 Configurer Hugging Face : Depuis le profil

Votre jeton Hugging Face se trouve dans votre profil sous [Jetons d'accès](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Ne les publiez pas ou ne les partagez pas publiquement. Créez plutôt un nouveau jeton pour l'utilisation de ce projet et copiez-le dans le fichier `.env` sous la variable `HUGGING_FACE_API_KEY`. _Note:_ Techniquement, ce n'est pas une clé API, mais il est utilisé pour l'authentification, donc nous gardons cette convention de nommage pour la cohérence.

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des mauvaises interprétations résultant de l'utilisation de cette traduction.