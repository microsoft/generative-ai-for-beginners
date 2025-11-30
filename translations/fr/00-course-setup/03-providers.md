<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T13:25:11+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "fr"
}
-->
# Choisir et configurer un fournisseur LLM 🔑

Les exercices **peuvent** aussi être configurés pour fonctionner avec un ou plusieurs déploiements de Large Language Model (LLM) via un fournisseur de service pris en charge comme OpenAI, Azure ou Hugging Face. Ces services proposent un _endpoint hébergé_ (API) auquel on peut accéder de façon programmatique avec les bons identifiants (clé API ou token). Dans ce cours, nous abordons ces fournisseurs :

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) avec une variété de modèles dont la série GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) pour les modèles OpenAI avec un accent sur l’usage en entreprise
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) pour les modèles open-source et le serveur d’inférence

**Vous devrez utiliser vos propres comptes pour ces exercices**. Les exercices sont facultatifs, donc vous pouvez choisir de configurer un, tous, ou aucun des fournisseurs selon vos préférences. Quelques conseils pour l’inscription :

| Inscription | Coût | Clé API | Playground | Commentaires |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Tarifs](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Par projet](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Sans code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Plusieurs modèles disponibles |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Tarifs](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Démarrage SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Démarrage Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Demande d’accès préalable requise](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Tarifs](https://huggingface.co/pricing) | [Tokens d’accès](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat propose peu de modèles](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Suivez les instructions ci-dessous pour _configurer_ ce dépôt afin de l’utiliser avec différents fournisseurs. Les exercices qui nécessitent un fournisseur spécifique auront l’un de ces tags dans leur nom de fichier :

- `aoai` - nécessite un endpoint et une clé Azure OpenAI
- `oai` - nécessite un endpoint et une clé OpenAI
- `hf` - nécessite un token Hugging Face

Vous pouvez configurer un, aucun ou tous les fournisseurs. Les exercices associés afficheront simplement une erreur si les identifiants sont manquants.

## Créer le fichier `.env`

On suppose que vous avez lu les instructions ci-dessus, que vous vous êtes inscrit auprès du fournisseur concerné, et que vous avez obtenu les identifiants nécessaires (API_KEY ou token). Pour Azure OpenAI, on suppose aussi que vous avez un déploiement valide du service Azure OpenAI (endpoint) avec au moins un modèle GPT déployé pour la complétion de chat.

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

3. Renseignez les valeurs (remplacez les espaces réservés à droite du `=`) comme indiqué dans la section suivante.

4. (Option) Si vous utilisez GitHub Codespaces, vous pouvez enregistrer les variables d’environnement comme _secrets Codespaces_ associés à ce dépôt. Dans ce cas, vous n’aurez pas besoin de configurer un fichier .env local. **Attention, cette option ne fonctionne que si vous utilisez GitHub Codespaces.** Vous devrez quand même configurer le fichier .env si vous utilisez Docker Desktop.

## Renseigner le fichier `.env`

Jetons un œil rapide aux noms de variables pour comprendre leur signification :

| Variable  | Description  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Il s’agit du token d’accès utilisateur que vous configurez dans votre profil |
| OPENAI_API_KEY | Il s’agit de la clé d’autorisation pour utiliser le service sur les endpoints OpenAI non-Azure |
| AZURE_OPENAI_API_KEY | Il s’agit de la clé d’autorisation pour utiliser ce service |
| AZURE_OPENAI_ENDPOINT | Il s’agit de l’endpoint déployé pour une ressource Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Il s’agit de l’endpoint de déploiement du modèle _génération de texte_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Il s’agit de l’endpoint de déploiement du modèle _embeddings de texte_ |
| | |

Remarque : Les deux dernières variables Azure OpenAI correspondent respectivement au modèle par défaut pour la complétion de chat (génération de texte) et la recherche vectorielle (embeddings). Les instructions pour les renseigner seront données dans les exercices concernés.

## Configurer Azure : depuis le portail

Les valeurs de l’endpoint et de la clé Azure OpenAI se trouvent dans le [Portail Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), commençons donc par là.

1. Rendez-vous sur le [Portail Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Cliquez sur l’option **Clés et endpoint** dans la barre latérale (menu à gauche).
1. Cliquez sur **Afficher les clés** – vous devriez voir : CLÉ 1, CLÉ 2 et Endpoint.
1. Utilisez la valeur de CLÉ 1 pour AZURE_OPENAI_API_KEY
1. Utilisez la valeur Endpoint pour AZURE_OPENAI_ENDPOINT

Ensuite, il nous faut les endpoints des modèles spécifiques que nous avons déployés.

1. Cliquez sur l’option **Déploiements de modèles** dans la barre latérale (menu de gauche) de la ressource Azure OpenAI.
1. Sur la page de destination, cliquez sur **Gérer les déploiements**

Cela vous amènera sur le site Azure OpenAI Studio, où nous trouverons les autres valeurs comme décrit ci-dessous.

## Configurer Azure : depuis Studio

1. Accédez à [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **depuis votre ressource** comme indiqué ci-dessus.
1. Cliquez sur l’onglet **Déploiements** (barre latérale, à gauche) pour voir les modèles actuellement déployés.
1. Si le modèle souhaité n’est pas déployé, utilisez **Créer un nouveau déploiement** pour le déployer.
1. Vous aurez besoin d’un modèle _génération de texte_ – nous recommandons : **gpt-35-turbo**
1. Vous aurez besoin d’un modèle _embeddings de texte_ – nous recommandons **text-embedding-ada-002**

Mettez à jour les variables d’environnement pour refléter le _nom du déploiement_ utilisé. En général, il s’agit du nom du modèle sauf si vous l’avez modifié explicitement. Par exemple, vous pourriez avoir :

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**N’oubliez pas d’enregistrer le fichier .env une fois terminé**. Vous pouvez maintenant quitter le fichier et revenir aux instructions pour exécuter le notebook.

## Configurer OpenAI : depuis le profil

Votre clé API OpenAI se trouve dans votre [compte OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Si vous n’en avez pas, vous pouvez créer un compte et générer une clé API. Une fois la clé obtenue, utilisez-la pour renseigner la variable `OPENAI_API_KEY` dans le fichier `.env`.

## Configurer Hugging Face : depuis le profil

Votre token Hugging Face se trouve dans votre profil sous [Tokens d’accès](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Ne le publiez pas et ne le partagez pas publiquement. Créez plutôt un nouveau token pour ce projet et copiez-le dans le fichier `.env` sous la variable `HUGGING_FACE_API_KEY`. _Remarque :_ Ce n’est techniquement pas une clé API mais elle sert à l’authentification, donc on garde cette convention de nommage pour la cohérence.

---

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatisées peuvent comporter des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.