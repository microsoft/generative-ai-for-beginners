# Choisir et configurer un fournisseur LLM 🔑

Les devoirs **peuvent** également être configurés pour fonctionner avec un ou plusieurs déploiements de grands modèles de langage (LLM) via un fournisseur de services pris en charge comme OpenAI, Azure ou Hugging Face. Ceux-ci fournissent un _point de terminaison hébergé_ (API) auquel nous pouvons accéder de manière programmatique avec les bonnes informations d'identification (clé API ou jeton). Dans ce cours, nous abordons ces fournisseurs :

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) avec divers modèles incluant la série principale GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) pour les modèles OpenAI avec un focus sur la préparation entreprise
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) pour les modèles open-source et le serveur d'inférence

**Vous devrez utiliser vos propres comptes pour ces exercices**. Les devoirs sont optionnels, vous pouvez donc choisir de configurer un, tous - ou aucun - des fournisseurs selon vos intérêts. Quelques conseils pour l'inscription :

| Inscription | Coût | Clé API | Playground | Commentaires |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Tarification](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Basée sur projet](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Sans code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Plusieurs modèles disponibles |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Tarification](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Démarrage rapide SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Démarrage rapide Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Doit postuler à l'avance pour l'accès](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Tarification](https://huggingface.co/pricing) | [Jetons d'accès](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat a des modèles limités](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Suivez les instructions ci-dessous pour _configurer_ ce dépôt pour une utilisation avec différents fournisseurs. Les devoirs qui nécessitent un fournisseur spécifique contiendront l’un de ces tags dans leur nom de fichier :

- `aoai` - nécessite un point de terminaison Azure OpenAI, clé
- `oai` - nécessite un point de terminaison OpenAI, clé
- `hf` - nécessite un jeton Hugging Face

Vous pouvez configurer un, aucun ou tous les fournisseurs. Les devoirs associés généreront simplement une erreur en cas d’identifiants manquants.

## Créer le fichier `.env`

Nous supposons que vous avez déjà lu les conseils ci-dessus, vous êtes inscrit auprès du fournisseur concerné, et avez obtenu les informations d’authentification requises (API_KEY ou jeton). Dans le cas d’Azure OpenAI, nous supposons également que vous disposez d’un déploiement valide d’un service Azure OpenAI (point de terminaison) avec au moins un modèle GPT déployé pour la complétion de chat.

L’étape suivante consiste à configurer vos **variables d’environnement locales** comme suit :

1. Cherchez dans le dossier racine un fichier `.env.copy` qui devrait contenir ceci :

   ```bash
   # Fournisseur OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Par défaut est défini !
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Copiez ce fichier en `.env` en utilisant la commande ci-dessous. Ce fichier est _gitignore_, gardant les secrets en sécurité.

   ```bash
   cp .env.copy .env
   ```

3. Remplissez les valeurs (remplacez les espaces réservés à droite du `=`) comme décrit dans la section suivante.

4. (Option) Si vous utilisez GitHub Codespaces, vous avez la possibilité d’enregistrer les variables d’environnement comme _secrets Codespaces_ associés à ce dépôt. Dans ce cas, vous n’aurez pas besoin de configurer un fichier .env local. **Cependant, notez que cette option fonctionne uniquement si vous utilisez GitHub Codespaces.** Vous devrez toujours configurer le fichier .env si vous utilisez Docker Desktop à la place.

## Remplir le fichier `.env`

Jetons un coup d’œil rapide aux noms des variables pour comprendre ce qu’elles représentent :

| Variable  | Description  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | C’est le jeton d’accès utilisateur que vous avez configuré dans votre profil |
| OPENAI_API_KEY | C’est la clé d’autorisation pour utiliser le service pour les points de terminaison non Azure OpenAI |
| AZURE_OPENAI_API_KEY | C’est la clé d’autorisation pour utiliser ce service |
| AZURE_OPENAI_ENDPOINT | C’est le point de terminaison déployé pour une ressource Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | C’est le point de terminaison de déploiement du modèle de _génération de texte_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | C’est le point de terminaison de déploiement du modèle d’_embeddings de texte_ |
| | |

Note : Les deux dernières variables Azure OpenAI correspondent à un modèle par défaut pour la complétion de chat (génération de texte) et la recherche vectorielle (embeddings) respectivement. Les instructions pour les définir seront précisées dans les devoirs concernés.

## Configurer Azure : depuis le portail

Les valeurs du point de terminaison et de la clé Azure OpenAI se trouvent dans le [portail Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), commençons donc par là.

1. Allez sur le [portail Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Cliquez sur l’option **Clés et point de terminaison** dans la barre latérale (menu à gauche).
1. Cliquez sur **Afficher les clés** - vous devriez voir ceci : CLÉ 1, CLÉ 2 et Point de terminaison.
1. Utilisez la valeur de la CLÉ 1 pour AZURE_OPENAI_API_KEY
1. Utilisez la valeur du point de terminaison pour AZURE_OPENAI_ENDPOINT

Ensuite, nous avons besoin des points de terminaison pour les modèles spécifiques que nous avons déployés.

1. Cliquez sur l’option **Déploiements de modèles** dans la barre latérale (menu à gauche) pour la ressource Azure OpenAI.
1. Sur la page de destination, cliquez sur **Gérer les déploiements**

Cela vous mènera au site Azure OpenAI Studio, où nous trouverons les autres valeurs comme décrit ci-dessous.

## Configurer Azure : depuis Studio

1. Naviguez vers [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **depuis votre ressource** comme décrit ci-dessus.
1. Cliquez sur l’onglet **Déploiements** (barre latérale, à gauche) pour voir les modèles actuellement déployés.
1. Si votre modèle désiré n’est pas déployé, utilisez **Créer un nouveau déploiement** pour le déployer.
1. Vous aurez besoin d’un modèle de _génération de texte_ - nous recommandons : **gpt-35-turbo**
1. Vous aurez besoin d’un modèle d’_embedding de texte_ - nous recommandons **text-embedding-ada-002**

Mettez maintenant à jour les variables d’environnement pour refléter le _nom du déploiement_ utilisé. Ce sera typiquement le même que le nom du modèle sauf si vous l’avez changé explicitement. Par exemple, vous pourriez avoir :

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**N’oubliez pas de sauvegarder le fichier .env une fois terminé**. Vous pouvez maintenant quitter le fichier et revenir aux instructions pour exécuter le notebook.

## Configurer OpenAI : depuis le profil

Votre clé API OpenAI se trouve dans votre [compte OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Si vous n’en avez pas, vous pouvez vous inscrire et créer une clé API. Une fois que vous avez la clé, vous pouvez l’utiliser pour remplir la variable `OPENAI_API_KEY` dans le fichier `.env`.

## Configurer Hugging Face : depuis le profil

Votre jeton Hugging Face se trouve dans votre profil sous [Jetons d’accès](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Ne publiez pas ou ne partagez pas ces jetons publiquement. Créez plutôt un nouveau jeton pour l’utilisation de ce projet et copiez-le dans le fichier `.env` sous la variable `HUGGING_FACE_API_KEY`. _Note :_ Ce n’est techniquement pas une clé API mais il est utilisé pour l’authentification, nous conservons donc cette convention de nommage pour la cohérence.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->