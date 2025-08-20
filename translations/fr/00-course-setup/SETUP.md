<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:20:38+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "fr"
}
-->
# Configurez votre environnement de développement

Nous avons configuré ce dépôt et ce cours avec un [conteneur de développement](https://containers.dev?WT.mc_id=academic-105485-koreyst) qui dispose d’un runtime universel capable de supporter le développement en Python3, .NET, Node.js et Java. La configuration associée est définie dans le fichier `devcontainer.json` situé dans le dossier `.devcontainer/` à la racine de ce dépôt.

Pour activer le conteneur de développement, lancez-le dans [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (pour un runtime hébergé dans le cloud) ou dans [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (pour un runtime hébergé localement). Consultez [cette documentation](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) pour plus de détails sur le fonctionnement des conteneurs de développement dans VS Code.

> [!TIP]  
> Nous recommandons d’utiliser GitHub Codespaces pour un démarrage rapide avec un minimum d’effort. Il offre un généreux [quota d’utilisation gratuite](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) pour les comptes personnels. Configurez les [délai d’inactivité](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) pour arrêter ou supprimer les codespaces inactifs afin d’optimiser l’utilisation de votre quota.

## 1. Exécution des devoirs

Chaque leçon proposera des devoirs _optionnels_ qui peuvent être fournis dans un ou plusieurs langages de programmation, notamment : Python, .NET/C#, Java et JavaScript/TypeScript. Cette section donne des conseils généraux pour exécuter ces devoirs.

### 1.1 Devoirs Python

Les devoirs Python sont fournis soit sous forme d’applications (`.py`), soit de notebooks Jupyter (`.ipynb`).  
- Pour exécuter un notebook, ouvrez-le dans Visual Studio Code, puis cliquez sur _Select Kernel_ (en haut à droite) et choisissez l’option Python 3 par défaut. Vous pouvez ensuite cliquer sur _Run All_ pour lancer l’exécution du notebook.  
- Pour exécuter des applications Python en ligne de commande, suivez les instructions spécifiques à chaque devoir pour sélectionner les bons fichiers et fournir les arguments requis.

## 2. Configuration des fournisseurs

Les devoirs **peuvent** également être configurés pour fonctionner avec un ou plusieurs déploiements de modèles de langage large (LLM) via un fournisseur de service supporté comme OpenAI, Azure ou Hugging Face. Ces fournisseurs offrent un _endpoint hébergé_ (API) accessible de manière programmatique avec les bonnes informations d’authentification (clé API ou token). Dans ce cours, nous abordons ces fournisseurs :

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) avec une variété de modèles dont la série principale GPT.  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) pour les modèles OpenAI avec un focus sur la préparation entreprise.  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) pour les modèles open-source et le serveur d’inférence.

**Vous devrez utiliser vos propres comptes pour ces exercices**. Les devoirs sont optionnels, vous pouvez donc choisir de configurer un, tous ou aucun des fournisseurs selon vos préférences. Voici quelques indications pour l’inscription :

| Inscription | Coût | Clé API | Playground | Commentaires |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [Tarifs](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [Basée sur projet](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Plusieurs modèles disponibles |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [Tarifs](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [Démarrage rapide SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Démarrage rapide Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Accès soumis à approbation préalable](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Tarifs](https://huggingface.co/pricing) | [Tokens d’accès](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Hugging Chat propose un nombre limité de modèles](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Suivez les instructions ci-dessous pour _configurer_ ce dépôt afin d’utiliser différents fournisseurs. Les devoirs nécessitant un fournisseur spécifique contiendront l’un de ces tags dans leur nom de fichier :  
 - `aoai` - nécessite un endpoint et une clé Azure OpenAI  
 - `oai` - nécessite un endpoint et une clé OpenAI  
 - `hf` - nécessite un token Hugging Face

Vous pouvez configurer un, aucun ou tous les fournisseurs. Les devoirs concernés généreront simplement une erreur en cas d’identifiants manquants.

### 2.1. Créer le fichier `.env`

Nous supposons que vous avez déjà lu les indications ci-dessus, créé un compte chez le fournisseur concerné et obtenu les identifiants d’authentification requis (API_KEY ou token). Dans le cas d’Azure OpenAI, nous supposons également que vous disposez d’un déploiement valide d’un service Azure OpenAI (endpoint) avec au moins un modèle GPT déployé pour la complétion de chat.

L’étape suivante consiste à configurer vos **variables d’environnement locales** comme suit :

1. Cherchez dans le dossier racine un fichier `.env.copy` qui devrait contenir quelque chose comme ceci :

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

2. Copiez ce fichier en `.env` avec la commande ci-dessous. Ce fichier est _gitignore-d_, ce qui protège vos secrets.

   ```bash
   cp .env.copy .env
   ```

3. Remplissez les valeurs (remplacez les espaces réservés à droite du `=`) comme décrit dans la section suivante.

3. (Option) Si vous utilisez GitHub Codespaces, vous pouvez enregistrer les variables d’environnement comme _secrets Codespaces_ associés à ce dépôt. Dans ce cas, vous n’aurez pas besoin de configurer un fichier .env local. **Cependant, cette option ne fonctionne que si vous utilisez GitHub Codespaces.** Vous devrez toujours configurer le fichier .env si vous utilisez Docker Desktop.

### 2.2. Remplir le fichier `.env`

Jetons un coup d’œil rapide aux noms des variables pour comprendre ce qu’elles représentent :

| Variable  | Description  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | C’est le token d’accès utilisateur que vous avez configuré dans votre profil |
| OPENAI_API_KEY | C’est la clé d’autorisation pour utiliser le service OpenAI hors Azure |
| AZURE_OPENAI_API_KEY | C’est la clé d’autorisation pour utiliser le service Azure OpenAI |
| AZURE_OPENAI_ENDPOINT | C’est l’endpoint déployé pour une ressource Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | C’est le déploiement du modèle de _génération de texte_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | C’est le déploiement du modèle d’_embeddings de texte_ |
| | |

Note : Les deux dernières variables Azure OpenAI correspondent respectivement à un modèle par défaut pour la complétion de chat (génération de texte) et pour la recherche vectorielle (embeddings). Les instructions pour les configurer seront précisées dans les devoirs concernés.

### 2.3 Configurer Azure : depuis le portail

Les valeurs de l’endpoint et de la clé Azure OpenAI se trouvent dans le [portail Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), commençons donc par là.

1. Rendez-vous sur le [portail Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
1. Cliquez sur l’option **Keys and Endpoint** dans la barre latérale (menu à gauche).  
1. Cliquez sur **Show Keys** – vous devriez voir : KEY 1, KEY 2 et Endpoint.  
1. Utilisez la valeur de KEY 1 pour AZURE_OPENAI_API_KEY  
1. Utilisez la valeur Endpoint pour AZURE_OPENAI_ENDPOINT

Ensuite, nous avons besoin des endpoints pour les modèles spécifiques que nous avons déployés.

1. Cliquez sur l’option **Model deployments** dans la barre latérale (menu à gauche) pour la ressource Azure OpenAI.  
1. Sur la page qui s’ouvre, cliquez sur **Manage Deployments**

Cela vous mènera au site Azure OpenAI Studio, où vous trouverez les autres valeurs comme décrit ci-dessous.

### 2.4 Configurer Azure : depuis Studio

1. Accédez à [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **depuis votre ressource** comme indiqué ci-dessus.  
1. Cliquez sur l’onglet **Deployments** (barre latérale gauche) pour voir les modèles actuellement déployés.  
1. Si le modèle souhaité n’est pas déployé, utilisez **Create new deployment** pour le déployer.  
1. Vous aurez besoin d’un modèle de _génération de texte_ – nous recommandons : **gpt-35-turbo**  
1. Vous aurez besoin d’un modèle d’_embedding de texte_ – nous recommandons **text-embedding-ada-002**

Mettez à jour les variables d’environnement pour refléter le _nom du déploiement_ utilisé. Ce sera généralement le même que le nom du modèle, sauf si vous l’avez changé explicitement. Par exemple, vous pourriez avoir :

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**N’oubliez pas de sauvegarder le fichier .env une fois terminé**. Vous pouvez maintenant fermer le fichier et revenir aux instructions pour exécuter le notebook.

### 2.5 Configurer OpenAI : depuis le profil

Votre clé API OpenAI se trouve dans votre [compte OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Si vous n’en avez pas, vous pouvez créer un compte et générer une clé API. Une fois la clé obtenue, vous pouvez la renseigner dans la variable `OPENAI_API_KEY` du fichier `.env`.

### 2.6 Configurer Hugging Face : depuis le profil

Votre token Hugging Face se trouve dans votre profil sous [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Ne publiez pas ni ne partagez ces tokens publiquement. Créez plutôt un nouveau token pour ce projet et copiez-le dans le fichier `.env` sous la variable `HUGGING_FACE_API_KEY`. _Note :_ Ce n’est techniquement pas une clé API, mais il est utilisé pour l’authentification, nous conservons donc cette convention de nommage pour plus de cohérence.

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.