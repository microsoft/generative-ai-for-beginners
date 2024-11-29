# Fondamentaux de l'Ingénierie des Prompts

[![Fondamentaux de l'Ingénierie des Prompts](../../../translated_images/04-lesson-banner.png?WT.d904d510033d5f0283f2caff5f735050f929dd196a1fc25fefa18433347fe463.fr.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson4-gh?WT.mc_id=academic-105485-koreyst)

## Introduction
Ce module couvre les concepts et techniques essentiels pour créer des prompts efficaces dans les modèles d'IA générative. La façon dont vous rédigez votre prompt pour un LLM compte également. Un prompt soigneusement élaboré peut améliorer la qualité de la réponse. Mais que signifient exactement des termes comme _prompt_ et _ingénierie des prompts_? Et comment améliorer l'_entrée_ du prompt que j'envoie au LLM? Ce sont les questions auxquelles nous essaierons de répondre dans ce chapitre et le suivant.

L'_IA générative_ est capable de créer de nouveaux contenus (par exemple, texte, images, audio, code, etc.) en réponse aux demandes des utilisateurs. Elle y parvient en utilisant des _modèles de langage de grande taille_ comme la série GPT ("Generative Pre-trained Transformer") d'OpenAI, entraînés à utiliser le langage naturel et le code.

Les utilisateurs peuvent désormais interagir avec ces modèles en utilisant des paradigmes familiers comme le chat, sans nécessiter d'expertise technique ou de formation. Les modèles sont basés sur des _prompts_ - les utilisateurs envoient une entrée textuelle (prompt) et obtiennent une réponse de l'IA (complétion). Ils peuvent ensuite "discuter avec l'IA" de manière itérative, dans des conversations à plusieurs tours, en affinant leur prompt jusqu'à ce que la réponse corresponde à leurs attentes.

Les "prompts" deviennent désormais l'interface de _programmation_ principale pour les applications d'IA générative, indiquant aux modèles ce qu'il faut faire et influençant la qualité des réponses retournées. L'"Ingénierie des Prompts" est un domaine d'étude en pleine croissance qui se concentre sur la _conception et l'optimisation_ des prompts pour fournir des réponses cohérentes et de qualité à grande échelle.

## Objectifs d'apprentissage

Dans cette leçon, nous apprenons ce qu'est l'Ingénierie des Prompts, pourquoi elle est importante, et comment nous pouvons créer des prompts plus efficaces pour un modèle et un objectif d'application donnés. Nous comprendrons les concepts de base et les meilleures pratiques pour l'ingénierie des prompts - et découvrirons un environnement interactif de "bac à sable" Jupyter Notebooks où nous pourrons voir ces concepts appliqués à des exemples réels.

À la fin de cette leçon, nous serons capables de :

1. Expliquer ce qu'est l'ingénierie des prompts et pourquoi elle est importante.
2. Décrire les composants d'un prompt et comment ils sont utilisés.
3. Apprendre les meilleures pratiques et techniques pour l'ingénierie des prompts.
4. Appliquer les techniques apprises à des exemples réels, en utilisant un point de terminaison OpenAI.

## Termes clés

Ingénierie des Prompts : La pratique de concevoir et affiner les entrées pour guider les modèles d'IA vers la production des sorties souhaitées.
Tokenisation : Le processus de conversion du texte en unités plus petites, appelées tokens, qu'un modèle peut comprendre et traiter.
LLMs ajustés par instruction : Modèles de Langage de Grande Taille (LLMs) qui ont été ajustés avec des instructions spécifiques pour améliorer la précision et la pertinence de leurs réponses.

## Bac à sable d'apprentissage

L'ingénierie des prompts est actuellement plus un art qu'une science. La meilleure façon d'améliorer notre intuition est de _pratiquer davantage_ et d'adopter une approche d'essais et d'erreurs qui combine expertise du domaine d'application avec techniques recommandées et optimisations spécifiques au modèle.

Le Jupyter Notebook accompagnant cette leçon fournit un environnement de _bac à sable_ où vous pouvez essayer ce que vous apprenez - au fur et à mesure ou dans le cadre du défi de code à la fin. Pour exécuter les exercices, vous aurez besoin de :

1. **Une clé API Azure OpenAI** - le point de terminaison de service pour un LLM déployé.
2. **Un environnement d'exécution Python** - dans lequel le Notebook peut être exécuté.
3. **Variables d'environnement locales** - _complétez les étapes de [CONFIGURATION](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) maintenant pour être prêt_.

Le notebook est livré avec des exercices _de démarrage_ - mais vous êtes encouragé à ajouter vos propres sections _Markdown_ (description) et _Code_ (demandes de prompts) pour essayer plus d'exemples ou d'idées - et développer votre intuition pour la conception de prompts.

## Guide illustré

Vous voulez avoir une vue d'ensemble de ce que cette leçon couvre avant de vous lancer? Consultez ce guide illustré, qui vous donne une idée des principaux sujets abordés et des points clés à garder à l'esprit pour chacun d'eux. La feuille de route de la leçon vous emmène de la compréhension des concepts de base et des défis à leur résolution avec des techniques d'ingénierie des prompts pertinentes et des meilleures pratiques. Notez que la section "Techniques Avancées" de ce guide fait référence à un contenu couvert dans le _prochain_ chapitre de ce programme.

![Guide illustré de l'ingénierie des prompts](../../../translated_images/04-prompt-engineering-sketchnote.png?WT.a936f69bc33c7a783015f6747ea56d0f0071349644cd9031f9b8d20a3eec8696.fr.mc_id=academic-105485-koreyst)

## Notre startup

Parlons maintenant de la façon dont _ce sujet_ est lié à notre mission de startup pour [apporter l'innovation de l'IA à l'éducation](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Nous voulons construire des applications d'apprentissage personnalisé alimentées par l'IA - alors réfléchissons à la façon dont différents utilisateurs de notre application pourraient "concevoir" des prompts :

- **Les administrateurs** pourraient demander à l'IA d'_analyser les données du programme pour identifier les lacunes de couverture_. L'IA peut résumer les résultats ou les visualiser avec du code.
- **Les éducateurs** pourraient demander à l'IA de _générer un plan de leçon pour un public cible et un sujet_. L'IA peut construire le plan personnalisé dans un format spécifié.
- **Les étudiants** pourraient demander à l'IA de les _tutorier dans un sujet difficile_. L'IA peut désormais guider les étudiants avec des leçons, des indices et des exemples adaptés à leur niveau.

Ce n'est que la partie émergée de l'iceberg. Consultez [Prompts Pour l'Éducation](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - une bibliothèque de prompts open-source organisée par des experts en éducation - pour avoir une idée plus large des possibilités! _Essayez d'exécuter certains de ces prompts dans le bac à sable ou en utilisant le OpenAI Playground pour voir ce qui se passe!_

## Qu'est-ce que l'ingénierie des prompts?

Nous avons commencé cette leçon en définissant **l'Ingénierie des Prompts** comme le processus de _conception et d'optimisation_ des entrées textuelles (prompts) pour fournir des réponses cohérentes et de qualité (complétions) pour un objectif d'application et un modèle donnés. Nous pouvons considérer cela comme un processus en deux étapes :

- _concevoir_ le prompt initial pour un modèle et un objectif donnés
- _affiner_ le prompt de manière itérative pour améliorer la qualité de la réponse

C'est nécessairement un processus d'essais et d'erreurs qui nécessite de l'intuition et des efforts de la part de l'utilisateur pour obtenir des résultats optimaux. Alors pourquoi est-ce important? Pour répondre à cette question, nous devons d'abord comprendre trois concepts :

- _Tokenisation_ = comment le modèle "voit" le prompt
- _Base LLMs_ = comment le modèle de base "traite" un prompt
- _LLMs ajustés par instruction_ = comment le modèle peut maintenant voir les "tâches"

### Tokenisation

Un LLM voit les prompts comme une _séquence de tokens_ où différents modèles (ou versions d'un modèle) peuvent tokeniser le même prompt de différentes manières. Étant donné que les LLMs sont entraînés sur des tokens (et non sur du texte brut), la façon dont les prompts sont tokenisés a un impact direct sur la qualité de la réponse générée.

Pour avoir une intuition sur le fonctionnement de la tokenisation, essayez des outils comme le [Tokeniseur OpenAI](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) montré ci-dessous. Copiez votre prompt - et voyez comment il est converti en tokens, en prêtant attention à la façon dont les caractères d'espace et les signes de ponctuation sont traités. Notez que cet exemple montre un ancien LLM (GPT-3) - donc l'essayer avec un modèle plus récent peut produire un résultat différent.

![Tokenisation](../../../translated_images/04-tokenizer-example.png?WT.f5399316da400747ffe3af9c95e61dc1a85508d57378da23a77538270c4cabf1.fr.mc_id=academic-105485-koreyst)

### Concept : Modèles de base

Une fois qu'un prompt est tokenisé, la fonction principale du ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (ou modèle de base) est de prédire le token dans cette séquence. Étant donné que les LLMs sont entraînés sur d'énormes ensembles de données textuelles, ils ont une bonne idée des relations statistiques entre les tokens et peuvent faire cette prédiction avec une certaine confiance. Notez qu'ils ne comprennent pas le _sens_ des mots dans le prompt ou le token; ils voient juste un modèle qu'ils peuvent "compléter" avec leur prochaine prédiction. Ils peuvent continuer à prédire la séquence jusqu'à ce qu'elle soit terminée par l'intervention de l'utilisateur ou une condition préétablie.

Vous voulez voir comment fonctionne la complétion basée sur les prompts? Entrez le prompt ci-dessus dans le [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) de l'Azure OpenAI Studio avec les paramètres par défaut. Le système est configuré pour traiter les prompts comme des demandes d'information - vous devriez donc voir une complétion qui satisfait ce contexte.

Mais que se passe-t-il si l'utilisateur voulait voir quelque chose de spécifique qui répondait à certains critères ou objectifs de tâche? C'est là que les LLMs _ajustés par instruction_ entrent en jeu.

![Base LLM Chat Completion](../../../translated_images/04-playground-chat-base.png?WT.7645a03d7989b1c410f2e9e6b503d18e4624f82d9cbf108dac999b8c8988f0ad.fr.mc_id=academic-105485-koreyst)

### Concept : LLMs ajustés par instruction

Un [LLM ajusté par instruction](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) commence par le modèle de base et le peaufine avec des exemples ou des paires d'entrée/sortie (par exemple, des "messages" à plusieurs tours) qui peuvent contenir des instructions claires - et la réponse de l'IA tente de suivre cette instruction.

Cela utilise des techniques comme l'Apprentissage par Renforcement avec Feedback Humain (RLHF) qui peuvent entraîner le modèle à _suivre des instructions_ et _apprendre du feedback_ afin qu'il produise des réponses mieux adaptées aux applications pratiques et plus pertinentes pour les objectifs des utilisateurs.

Essayons-le - revisitez le prompt ci-dessus, mais changez maintenant le _message système_ pour fournir l'instruction suivante comme contexte :

> _Résumez le contenu qui vous est fourni pour un élève de deuxième année. Gardez le résultat à un paragraphe avec 3-5 puces._

Voyez comment le résultat est maintenant ajusté pour refléter l'objectif et le format souhaités? Un éducateur peut désormais utiliser directement cette réponse dans ses diapositives pour cette classe.

![Instruction Tuned LLM Chat Completion](../../../translated_images/04-playground-chat-instructions.png?WT.d9c80b15e90815a83ce665bf4418e70205d30318a5a5bcf407b2c92769743593.fr.mc_id=academic-105485-koreyst)

## Pourquoi avons-nous besoin de l'ingénierie des prompts?

Maintenant que nous savons comment les prompts sont traités par les LLMs, parlons de _pourquoi_ nous avons besoin de l'ingénierie des prompts. La réponse réside dans le fait que les LLMs actuels posent un certain nombre de défis qui rendent plus difficile d'obtenir des _complétions fiables et cohérentes_ sans investir dans la construction et l'optimisation des prompts. Par exemple :

1. **Les réponses des modèles sont stochastiques.** Le _même prompt_ produira probablement des réponses différentes avec différents modèles ou versions de modèles. Et il peut même produire des résultats différents avec le _même modèle_ à différents moments. _Les techniques d'ingénierie des prompts peuvent nous aider à minimiser ces variations en fournissant de meilleures garde-fous_.

1. **Les modèles peuvent fabriquer des réponses.** Les modèles sont pré-entraînés avec des ensembles de données _grands mais finis_, ce qui signifie qu'ils manquent de connaissances sur les concepts en dehors de ce cadre d'entraînement. En conséquence, ils peuvent produire des complétions qui sont inexactes, imaginaires ou directement contradictoires avec des faits connus. _Les techniques d'ingénierie des prompts aident les utilisateurs à identifier et à atténuer ces fabrications, par exemple, en demandant à l'IA des citations ou un raisonnement_.

1. **Les capacités des modèles varieront.** Les modèles plus récents ou les générations de modèles auront des capacités plus riches mais apporteront également des particularités uniques et des compromis en termes de coût et de complexité. _L'ingénierie des prompts peut nous aider à développer des meilleures pratiques et des workflows qui abstraient les différences et s'adaptent aux exigences spécifiques des modèles de manière évolutive et transparente_.

Voyons cela en action dans le OpenAI ou Azure OpenAI Playground :

- Utilisez le même prompt avec différents déploiements de LLM (par exemple, OpenAI, Azure OpenAI, Hugging Face) - avez-vous vu les variations?
- Utilisez le même prompt à plusieurs reprises avec le _même_ déploiement de LLM (par exemple, le playground Azure OpenAI) - comment ces variations ont-elles différé?

### Exemple de fabrications

Dans ce cours, nous utilisons le terme **"fabrication"** pour faire référence au phénomène où les LLMs génèrent parfois des informations factuellement incorrectes en raison de limitations dans leur entraînement ou d'autres contraintes. Vous avez peut-être aussi entendu cela désigné sous le nom d'_hallucinations_ dans des articles populaires ou des articles de recherche. Cependant, nous recommandons fortement d'utiliser le terme _"fabrication"_ pour ne pas anthropomorphiser accidentellement le comportement en attribuant un trait humain à un résultat piloté par une machine. Cela renforce également les [lignes directrices de l'IA Responsable](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) d'un point de vue terminologique, en supprimant les termes qui pourraient également être considérés comme offensants ou non inclusifs dans certains contextes.

Vous voulez avoir une idée de comment fonctionnent les fabrications? Pensez à un prompt qui demande à l'IA de générer du contenu pour un sujet inexistant (pour s'assurer qu'il ne se trouve pas dans l'ensemble de données d'entraînement). Par exemple - j'ai essayé ce prompt :

> **Prompt :** générez un plan de leçon sur la Guerre Martienne de 2076.

Une recherche sur le web m'a montré qu'il existait des récits fictifs (par exemple, des séries télévisées ou des livres) sur des guerres martiennes - mais aucune en 2076. Le bon sens nous dit également que 2076 est _dans le futur_ et ne peut donc pas être associé à un événement réel.

Alors que se passe-t-il lorsque nous exécutons ce prompt avec différents fournisseurs de LLM?

> **Réponse 1** : OpenAI Playground (GPT-35)

![Réponse 1](../../../translated_images/04-fabrication-oai.png?WT.08cc3e01259a6b46725a800e67de50c37b7fdd6b1f932f027881cbe32f80bcf1.fr.mc_id=academic-105485-koreyst)

> **Réponse 2** : Azure OpenAI Playground (GPT-35)

![Réponse 2](../../../translated_images/04-fabrication-aoai.png?WT.81e0d286a351c87c804aaca6e5f8251a6deed5105d11bca035f8cead8c52d299.fr.mc_id=academic-105485-koreyst)

> **Réponse 3** : Hugging Face Chat Playground (LLama-2)

![Réponse 3](../../../translated_images/04-fabrication-huggingchat.png?WT.992b3a675cc7ed0dbe53e308b93df8165048fb7c4516e6bb00611d05c92e8fd5.fr.mc_id=academic-105485-koreyst)

Comme prévu, chaque modèle (ou version de modèle) produit des réponses légèrement différentes grâce au comportement stochastique et aux variations des capacités du modèle. Par exemple, un modèle cible un public de 8e année tandis qu'un autre suppose un lycéen. Mais les trois modèles ont généré des réponses qui pourraient convaincre un utilisateur non informé que l'événement était réel.

Les techniques d'ingénierie des prompts comme le _métaprompting_ et la _configuration de température_ peuvent réduire les fabrications de modèles dans une certaine mesure. Les nouvelles _architectures_ d'ingénierie des prompts intègrent également de nouveaux outils et techniques de manière transparente dans le flux de prompts, pour atténuer ou réduire certains de ces effets.

## Étude de cas : GitHub Copilot

Concluons cette section en comprenant comment l'ingénierie des prompts est utilisée dans des solutions du monde réel en examinant une étude de cas : [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot est votre "programmeur en duo avec IA" - il convertit les prompts textuels en complétions de code et est intégré dans votre environnement de développement (par exemple, Visual Studio Code) pour une expérience utilisateur fluide. Comme documenté dans la série de blogs ci-dessous, la première version était basée sur le modèle OpenAI Codex - avec des ingénieurs réalisant rapidement la nécessité de peaufiner le modèle et de développer de meilleures techniques d'ingénierie des prompts pour améliorer la qualité du code. En juillet, ils ont [dévoilé un modèle d'IA amélioré qui va au-delà de Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-cop
La véritable valeur des modèles réside dans la capacité de créer et publier des _bibliothèques de prompts_ pour des domaines d'application verticaux - où le modèle de prompt est maintenant _optimisé_ pour refléter le contexte ou des exemples spécifiques à l'application, rendant les réponses plus pertinentes et précises pour le public cible. Le dépôt [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) est un excellent exemple de cette approche, en proposant une bibliothèque de prompts pour le domaine de l'éducation avec un accent sur des objectifs clés tels que la planification des cours, la conception de programmes, le tutorat des étudiants, etc.

## Contenu de soutien

Si nous considérons la construction de prompts comme ayant une instruction (tâche) et un objectif (contenu principal), alors le _contenu secondaire_ est comme un contexte supplémentaire que nous fournissons pour **influencer la sortie d'une certaine manière**. Il pourrait s'agir de paramètres de réglage, d'instructions de formatage, de taxonomies de sujets, etc., qui peuvent aider le modèle à _adapter_ sa réponse pour convenir aux objectifs ou attentes souhaités de l'utilisateur.

Par exemple : Étant donné un catalogue de cours avec des métadonnées étendues (nom, description, niveau, balises de métadonnées, instructeur, etc.) sur tous les cours disponibles dans le programme :

- nous pouvons définir une instruction pour "résumer le catalogue de cours pour l'automne 2023"
- nous pouvons utiliser le contenu principal pour fournir quelques exemples du résultat souhaité
- nous pouvons utiliser le contenu secondaire pour identifier les 5 principales "balises" d'intérêt.

Maintenant, le modèle peut fournir un résumé dans le format montré par les quelques exemples - mais si un résultat a plusieurs balises, il peut prioriser les 5 balises identifiées dans le contenu secondaire.

---

<!--
MODÈLE DE LEÇON :
Cette unité doit couvrir le concept de base #1.
Renforcez le concept avec des exemples et des références.

CONCEPT #3 :
Techniques d'ingénierie des prompts.
Quelles sont quelques techniques de base pour l'ingénierie des prompts ?
Illustrez-le avec quelques exercices.
-->

## Bonnes pratiques de création de prompts

Maintenant que nous savons comment les prompts peuvent être _construits_, nous pouvons commencer à réfléchir à comment les _concevoir_ pour refléter les meilleures pratiques. Nous pouvons penser à cela en deux parties - avoir le bon _état d'esprit_ et appliquer les bonnes _techniques_.

### État d'esprit pour l'ingénierie des prompts

L'ingénierie des prompts est un processus d'essais et d'erreurs, alors gardez trois facteurs directeurs à l'esprit :

1. **La compréhension du domaine est importante.** La précision et la pertinence des réponses dépendent du _domaine_ dans lequel cette application ou cet utilisateur opère. Appliquez votre intuition et votre expertise du domaine pour **personnaliser davantage les techniques**. Par exemple, définissez des _personnalités spécifiques au domaine_ dans vos prompts système, ou utilisez des _modèles spécifiques au domaine_ dans vos prompts utilisateur. Fournissez un contenu secondaire qui reflète les contextes spécifiques au domaine, ou utilisez des _indices et exemples spécifiques au domaine_ pour guider le modèle vers des modèles d'utilisation familiers.

2. **La compréhension du modèle est importante.** Nous savons que les modèles sont par nature stochastiques. Mais les implémentations de modèles peuvent également varier en termes de jeu de données d'entraînement qu'ils utilisent (connaissances pré-entraînées), des capacités qu'ils offrent (par exemple, via API ou SDK) et du type de contenu pour lequel ils sont optimisés (par exemple, code vs. images vs. texte). Comprenez les forces et les limitations du modèle que vous utilisez, et utilisez ces connaissances pour _prioriser les tâches_ ou créer des _modèles personnalisés_ qui sont optimisés pour les capacités du modèle.

3. **L'itération et la validation sont importantes.** Les modèles évoluent rapidement, tout comme les techniques d'ingénierie des prompts. En tant qu'expert du domaine, vous pouvez avoir d'autres contextes ou critères pour _votre_ application spécifique, qui peuvent ne pas s'appliquer à la communauté plus large. Utilisez des outils et techniques d'ingénierie des prompts pour "accélérer" la construction de prompts, puis itérez et validez les résultats en utilisant votre propre intuition et expertise du domaine. Enregistrez vos insights et créez une **base de connaissances** (par exemple, des bibliothèques de prompts) qui peuvent être utilisées comme nouvelle référence par d'autres, pour des itérations plus rapides à l'avenir.

## Meilleures pratiques

Voyons maintenant les meilleures pratiques courantes recommandées par les praticiens de [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) et [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Quoi                             | Pourquoi                                                                                                                                                                                                                                               |
| :------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Évaluer les derniers modèles.    | Les nouvelles générations de modèles sont susceptibles d'avoir des fonctionnalités et une qualité améliorées - mais peuvent aussi entraîner des coûts plus élevés. Évaluez-les pour leur impact, puis prenez des décisions de migration.                                                       |
| Séparer instructions & contexte  | Vérifiez si votre modèle/fournisseur définit des _délimiteurs_ pour distinguer plus clairement les instructions, le contenu principal et secondaire. Cela peut aider les modèles à attribuer des poids plus précis aux tokens.                                                                |
| Soyez spécifique et clair        | Donnez plus de détails sur le contexte souhaité, le résultat, la longueur, le format, le style, etc. Cela améliorera à la fois la qualité et la cohérence des réponses. Capturez les recettes dans des modèles réutilisables.                                                                |
| Soyez descriptif, utilisez des exemples | Les modèles peuvent mieux répondre à une approche "montrer et raconter". Commencez par une `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
| Use cues to jumpstart completions | Nudge it towards a desired outcome by giving it some leading words or phrases that it can use as a starting point for the response.                                                                                                               |
| Double Down                       | Sometimes you may need to repeat yourself to the model. Give instructions before and after your primary content, use an instruction and a cue, etc. Iterate & validate to see what works.                                                         |
| Order Matters                     | The order in which you present information to the model may impact the output, even in the learning examples, thanks to recency bias. Try different options to see what works best.                                                               |
| Give the model an “out”           | Give the model a _fallback_ completion response it can provide if it cannot complete the task for any reason. This can reduce chances of models generating false or fabricated responses.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

As with any best practice, remember that _your mileage may vary_ based on the model, the task and the domain. Use these as a starting point, and iterate to find what works best for you. Constantly re-evaluate your prompt engineering process as new models and tools become available, with a focus on process scalability and response quality.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Assignment

Congratulations! You made it to the end of the lesson! It's time to put some of those concepts and techniques to the test with real examples!

For our assignment, we'll be using a Jupyter Notebook with exercises you can complete interactively. You can also extend the Notebook with your own Markdown and Code cells to explore ideas and techniques on your own.

### To get started, fork the repo, then

- (Recommended) Launch GitHub Codespaces
- (Alternatively) Clone the repo to your local device and use it with Docker Desktop
- (Alternatively) Open the Notebook with your preferred Notebook runtime environment.

### Next, configure your environment variables

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` valeurs. Revenez à la [section Learning Sandbox](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) pour apprendre comment.

### Ensuite, ouvrez le Jupyter Notebook

- Sélectionnez le noyau d'exécution. Si vous utilisez les options 1 ou 2, sélectionnez simplement le noyau Python 3.10.x par défaut fourni par le conteneur de développement.

Vous êtes prêt à exécuter les exercices. Notez qu'il n'y a pas de bonnes ou mauvaises réponses ici - juste l'exploration d'options par essais et erreurs et la construction d'une intuition pour ce qui fonctionne pour un modèle et un domaine d'application donnés.

_Pour cette raison, il n'y a pas de segments de solution de code dans cette leçon. Au lieu de cela, le Notebook aura des cellules Markdown intitulées "Ma solution :" qui montrent un exemple de sortie pour référence._

 <!--
MODÈLE DE LEÇON :
Concluez la section par un résumé et des ressources pour un apprentissage autonome.
-->

## Vérification des connaissances

Lequel des éléments suivants est un bon prompt suivant certaines bonnes pratiques raisonnables ?

1. Montrez-moi une image de voiture rouge
2. Montrez-moi une image de voiture rouge de marque Volvo et modèle XC90 garée près d'une falaise avec le soleil couchant
3. Montrez-moi une image de voiture rouge de marque Volvo et modèle XC90

R : 2, c'est le meilleur prompt car il donne des détails sur "quoi" et va dans les spécificités (pas n'importe quelle voiture mais une marque et un modèle spécifiques) et il décrit également le cadre général. 3 est le suivant car il contient également beaucoup de descriptions.

## 🚀 Défi

Voyez si vous pouvez tirer parti de la technique de "l'indice" avec le prompt : Complétez la phrase "Montrez-moi une image de voiture rouge de marque Volvo et ". Que répond-il, et comment l'amélioreriez-vous ?

## Excellent travail ! Continuez votre apprentissage

Vous voulez en savoir plus sur les différents concepts d'ingénierie des prompts ? Allez sur la [page d'apprentissage continu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour trouver d'autres ressources intéressantes sur ce sujet.

Rendez-vous à la leçon 5 où nous examinerons [des techniques avancées de prompting](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst) !

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle humaine. Nous ne sommes pas responsables des malentendus ou des mauvaises interprétations résultant de l'utilisation de cette traduction.