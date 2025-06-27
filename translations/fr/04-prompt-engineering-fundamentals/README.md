<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-06-25T11:41:30+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "fr"
}
-->
# Fondamentaux de l'Ingénierie des Prompts

## Introduction
Ce module aborde les concepts essentiels et les techniques pour créer des prompts efficaces dans les modèles d'IA générative. La manière dont vous rédigez votre prompt pour un LLM est également importante. Un prompt soigneusement conçu peut obtenir une meilleure qualité de réponse. Mais que signifient exactement les termes _prompt_ et _ingénierie des prompts_? Et comment puis-je améliorer l'input du prompt que j'envoie au LLM? Ce sont les questions auxquelles nous tenterons de répondre dans ce chapitre et le suivant.

L'IA générative est capable de créer du nouveau contenu (par exemple, texte, images, audio, code, etc.) en réponse aux demandes des utilisateurs. Elle y parvient grâce à des _Modèles de Langage de Grande Taille_ comme la série GPT ("Generative Pre-trained Transformer") d'OpenAI, entraînée à utiliser le langage naturel et le code.

Les utilisateurs peuvent désormais interagir avec ces modèles en utilisant des paradigmes familiers comme le chat, sans nécessiter d'expertise technique ou de formation. Les modèles sont basés sur des prompts - les utilisateurs envoient une entrée textuelle (prompt) et reçoivent la réponse de l'IA (complétion). Ils peuvent ensuite "dialoguer avec l'IA" de manière itérative, dans des conversations à plusieurs tours, en affinant leur prompt jusqu'à ce que la réponse corresponde à leurs attentes.

Les "prompts" deviennent maintenant l'interface de programmation principale pour les applications d'IA générative, indiquant aux modèles quoi faire et influençant la qualité des réponses retournées. L'"ingénierie des prompts" est un domaine d'étude en pleine croissance qui se concentre sur la _conception et l'optimisation_ des prompts pour fournir des réponses cohérentes et de qualité à grande échelle.

## Objectifs d'apprentissage

Dans cette leçon, nous apprenons ce qu'est l'ingénierie des prompts, pourquoi elle est importante, et comment nous pouvons concevoir des prompts plus efficaces pour un modèle donné et un objectif d'application. Nous comprendrons les concepts de base et les meilleures pratiques pour l'ingénierie des prompts - et découvrirons un environnement "sandbox" interactif Jupyter Notebooks où nous pourrons voir ces concepts appliqués à des exemples réels.

À la fin de cette leçon, nous serons capables de :

1. Expliquer ce qu'est l'ingénierie des prompts et pourquoi elle est importante.
2. Décrire les composants d'un prompt et comment ils sont utilisés.
3. Apprendre les meilleures pratiques et techniques pour l'ingénierie des prompts.
4. Appliquer les techniques apprises à des exemples réels, en utilisant un point de terminaison OpenAI.

## Termes clés

Ingénierie des Prompts : La pratique de concevoir et de raffiner les entrées pour guider les modèles d'IA vers la production des résultats souhaités.
Tokenisation : Le processus de conversion du texte en unités plus petites, appelées tokens, qu'un modèle peut comprendre et traiter.
LLMs Ajustés par Instruction : Modèles de Langage de Grande Taille (LLMs) qui ont été ajustés avec des instructions spécifiques pour améliorer la précision et la pertinence de leurs réponses.

## Sandbox d'apprentissage

L'ingénierie des prompts est actuellement plus un art qu'une science. La meilleure façon d'améliorer notre intuition à ce sujet est de _pratiquer davantage_ et d'adopter une approche par essais et erreurs qui combine l'expertise du domaine d'application avec des techniques recommandées et des optimisations spécifiques au modèle.

Le Jupyter Notebook accompagnant cette leçon fournit un environnement _sandbox_ où vous pouvez essayer ce que vous apprenez - au fur et à mesure ou dans le cadre du défi de code à la fin. Pour exécuter les exercices, vous aurez besoin de :

1. **Une clé API Azure OpenAI** - le point de terminaison du service pour un LLM déployé.
2. **Un environnement Python** - dans lequel le Notebook peut être exécuté.
3. **Variables d'environnement locales** - _complétez les étapes [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) maintenant pour vous préparer_.

Le notebook est livré avec des exercices _de départ_ - mais vous êtes encouragé à ajouter vos propres sections _Markdown_ (description) et _Code_ (demandes de prompts) pour essayer plus d'exemples ou d'idées - et construire votre intuition pour la conception de prompts.

## Guide Illustré

Vous voulez avoir une vue d'ensemble de ce que couvre cette leçon avant de vous plonger dedans? Consultez ce guide illustré, qui vous donne une idée des principaux sujets abordés et des points clés à considérer pour chacun d'eux. La feuille de route de la leçon vous emmène de la compréhension des concepts de base et des défis à leur traitement avec des techniques d'ingénierie des prompts pertinentes et des meilleures pratiques. Notez que la section "Techniques Avancées" de ce guide fait référence au contenu abordé dans le _prochain_ chapitre de ce programme.

## Notre Startup

Maintenant, parlons de la façon dont _ce sujet_ est lié à notre mission de startup pour [apporter l'innovation de l'IA à l'éducation](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Nous voulons construire des applications d'apprentissage personnalisé alimentées par l'IA - alors réfléchissons à la façon dont différents utilisateurs de notre application pourraient "concevoir" des prompts :

- **Administrateurs** pourraient demander à l'IA d'_analyser les données du programme pour identifier les lacunes dans la couverture_. L'IA peut résumer les résultats ou les visualiser avec du code.
- **Éducateurs** pourraient demander à l'IA de _générer un plan de cours pour un public cible et un sujet_. L'IA peut construire le plan personnalisé dans un format spécifié.
- **Étudiants** pourraient demander à l'IA de _les tutoriser dans un sujet difficile_. L'IA peut maintenant guider les étudiants avec des leçons, des indices et des exemples adaptés à leur niveau.

Ce n'est que la partie émergée de l'iceberg. Consultez [Prompts Pour l'Éducation](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - une bibliothèque de prompts open-source organisée par des experts en éducation - pour avoir une idée plus large des possibilités! _Essayez de lancer certains de ces prompts dans le sandbox ou en utilisant le OpenAI Playground pour voir ce qui se passe!_

## Qu'est-ce que l'Ingénierie des Prompts?

Nous avons commencé cette leçon en définissant **l'Ingénierie des Prompts** comme le processus de _conception et d'optimisation_ des entrées textuelles (prompts) pour fournir des réponses cohérentes et de qualité (complétions) pour un objectif d'application et un modèle donné. Nous pouvons considérer cela comme un processus en deux étapes :

- _concevoir_ le prompt initial pour un modèle et un objectif donnés
- _affiner_ le prompt de manière itérative pour améliorer la qualité de la réponse

Il s'agit nécessairement d'un processus par essais et erreurs qui nécessite l'intuition et l'effort de l'utilisateur pour obtenir des résultats optimaux. Alors pourquoi est-ce important? Pour répondre à cette question, nous devons d'abord comprendre trois concepts :

- _Tokenisation_ = comment le modèle "voit" le prompt
- _Base LLMs_ = comment le modèle de base "traite" un prompt
- _LLMs Ajustés par Instruction_ = comment le modèle peut maintenant voir les "tâches"

### Tokenisation

Un LLM voit les prompts comme une _séquence de tokens_ où différents modèles (ou versions d'un modèle) peuvent tokeniser le même prompt de différentes manières. Étant donné que les LLMs sont entraînés sur des tokens (et non sur du texte brut), la manière dont les prompts sont tokenisés a un impact direct sur la qualité de la réponse générée.

Pour avoir une intuition sur le fonctionnement de la tokenisation, essayez des outils comme le [Tokenizer d'OpenAI](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) montré ci-dessous. Copiez votre prompt - et voyez comment il est converti en tokens, en faisant attention à la façon dont les caractères d'espacement et les signes de ponctuation sont traités. Notez que cet exemple montre un ancien LLM (GPT-3) - donc essayer cela avec un modèle plus récent peut produire un résultat différent.

### Concept : Modèles de Fondation

Une fois qu'un prompt est tokenisé, la fonction principale du ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (ou modèle de fondation) est de prédire le token dans cette séquence. Étant donné que les LLMs sont entraînés sur des ensembles de données textuelles massives, ils ont une bonne compréhension des relations statistiques entre les tokens et peuvent faire cette prédiction avec une certaine confiance. Notez qu'ils ne comprennent pas le _sens_ des mots dans le prompt ou le token; ils voient simplement un motif qu'ils peuvent "compléter" avec leur prochaine prédiction. Ils peuvent continuer à prédire la séquence jusqu'à ce qu'elle soit terminée par une intervention de l'utilisateur ou une condition préétablie.

Vous voulez voir comment la complétion basée sur des prompts fonctionne? Entrez le prompt ci-dessus dans le [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) de l'Azure OpenAI Studio avec les paramètres par défaut. Le système est configuré pour traiter les prompts comme des demandes d'information - vous devriez donc voir une complétion qui satisfait ce contexte.

Mais que se passe-t-il si l'utilisateur souhaite voir quelque chose de spécifique qui répond à certains critères ou objectifs de tâche? C'est là que les LLMs ajustés par instruction entrent en jeu.

### Concept : LLMs Ajustés par Instruction

Un [LLM Ajusté par Instruction](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) commence avec le modèle de fondation et le ajuste avec des exemples ou des paires input/output (par exemple, "messages" à plusieurs tours) qui peuvent contenir des instructions claires - et la réponse de l'IA tente de suivre cette instruction.

Cela utilise des techniques comme l'apprentissage par renforcement avec retour humain (RLHF) qui peuvent entraîner le modèle à _suivre des instructions_ et _apprendre du feedback_ afin qu'il produise des réponses mieux adaptées aux applications pratiques et plus pertinentes pour les objectifs de l'utilisateur.

Essayons cela - revenez au prompt ci-dessus, mais maintenant changez le _message système_ pour fournir l'instruction suivante comme contexte :

> _Résumez le contenu que vous recevez pour un élève de deuxième année. Gardez le résultat à un paragraphe avec 3-5 points à puces._

Voyez comment le résultat est maintenant ajusté pour refléter l'objectif et le format souhaités? Un éducateur peut maintenant utiliser directement cette réponse dans ses diapositives pour cette classe.

## Pourquoi avons-nous besoin de l'Ingénierie des Prompts?

Maintenant que nous savons comment les prompts sont traités par les LLMs, parlons de _pourquoi_ nous avons besoin de l'ingénierie des prompts. La réponse réside dans le fait que les LLMs actuels posent un certain nombre de défis qui rendent _les complétions fiables et cohérentes_ plus difficiles à obtenir sans effort dans la construction et l'optimisation des prompts. Par exemple :

1. **Les réponses du modèle sont stochastiques.** Le _même prompt_ produira probablement des réponses différentes avec différents modèles ou versions de modèles. Et il peut même produire des résultats différents avec le _même modèle_ à différents moments. _Les techniques d'ingénierie des prompts peuvent nous aider à minimiser ces variations en fournissant de meilleures balises_.

2. **Les modèles peuvent fabriquer des réponses.** Les modèles sont pré-entraînés avec des ensembles de données _grands mais finis_, ce qui signifie qu'ils manquent de connaissances sur les concepts en dehors de cette portée de formation. En conséquence, ils peuvent produire des complétions qui sont inexactes, imaginaires ou directement contradictoires avec des faits connus. _Les techniques d'ingénierie des prompts aident les utilisateurs à identifier et à atténuer ces fabrications, par exemple en demandant à l'IA des citations ou des raisonnements_.

3. **Les capacités des modèles varient.** Les modèles ou générations de modèles plus récents auront des capacités plus riches mais apporteront également des particularités uniques et des compromis en termes de coût et de complexité. _L'ingénierie des prompts peut nous aider à développer des meilleures pratiques et des flux de travail qui abstraient les différences et s'adaptent aux exigences spécifiques du modèle de manière évolutive et transparente_.

Voyons cela en action dans le OpenAI ou Azure OpenAI Playground :

- Utilisez le même prompt avec différents déploiements de LLM (par exemple, OpenAI, Azure OpenAI, Hugging Face) - avez-vous vu les variations?
- Utilisez le même prompt à plusieurs reprises avec le _même_ déploiement de LLM (par exemple, Azure OpenAI Playground) - comment ces variations ont-elles différé?

### Exemple de Fabrications

Dans ce cours, nous utilisons le terme **"fabrication"** pour référencer le phénomène où les LLMs génèrent parfois des informations factuellement incorrectes en raison de limitations dans leur formation ou d'autres contraintes. Vous avez peut-être aussi entendu parler de cela comme _"hallucinations"_ dans des articles populaires ou des articles de recherche. Cependant, nous recommandons fortement d'utiliser _"fabrication"_ comme terme afin de ne pas anthropomorphiser accidentellement le comportement en attribuant une caractéristique humaine à un résultat généré par une machine. Cela renforce également les [directives d'IA responsable](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) d'un point de vue terminologique, en supprimant des termes qui pourraient également être considérés comme offensants ou non inclusifs dans certains contextes.

Vous voulez avoir une idée de comment fonctionnent les fabrications? Pensez à un prompt qui demande à l'IA de générer du contenu pour un sujet inexistant (pour s'assurer qu'il ne se trouve pas dans l'ensemble de données d'entraînement). Par exemple - j'ai essayé ce prompt :

> **Prompt :** générez un plan de cours sur la Guerre Martienne de 2076.

Une recherche sur le web m'a montré qu'il y avait des récits fictifs (par exemple, séries télévisées ou livres) sur les guerres martiennes - mais aucun en 2076. Le bon sens nous dit également que 2076 est _dans le futur_ et ne peut donc pas être associé à un événement réel.

Alors que se passe-t-il lorsque nous exécutons ce prompt avec différents fournisseurs de LLM?

> **Réponse 1** : OpenAI Playground (GPT-35)

> **Réponse 2** : Azure OpenAI Playground (GPT-35)

> **Réponse 3** : Hugging Face Chat Playground (LLama-2)

Comme prévu, chaque modèle (ou version de modèle) produit des réponses légèrement différentes grâce à un comportement stochastique et à des variations de capacité du modèle. Par exemple, un modèle cible un public de 8ème année tandis que l'autre suppose un lycéen. Mais tous les trois modèles ont généré des réponses qui pourraient convaincre un utilisateur non informé que l'événement était réel.

Les techniques d'ingénierie des prompts comme _metaprompting_ et _configuration de température_ peuvent réduire les fabrications de modèles dans une certaine mesure. Les nouvelles _architectures_ d'ingénierie des prompts incorporent également de nouveaux outils et techniques de manière transparente dans le flux de prompts, pour atténuer ou réduire certains de ces effets.

## Étude de Cas : GitHub Copilot

Concluons cette section en ayant une idée de la façon dont l'ingénierie des prompts est utilisée dans des solutions réelles en regardant une Étude de Cas : [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot est votre "Programmeur Pair IA" - il convertit les prompts textuels en complétions de code et est intégré dans votre environnement de développement (par exemple, Visual Studio Code) pour une expérience utilisateur transparente. Comme documenté dans la série de blogs ci-dessous, la première version était basée sur le modèle OpenAI Codex - avec des ingénieurs réalisant rapidement la nécessité de peaufiner le modèle et de développer de meilleures techniques d'ingénierie des prompts, pour améliorer la qualité du code. En juillet, ils ont [débuté un modèle d'IA amélioré qui va au-delà de Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) pour des suggestions encore plus rapides.

Lisez les articles dans l'ordre, pour suivre leur parcours d'apprentissage.

- **Mai 2023** | [GitHub Copilot devient meilleur pour comprendre votre code](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mai 2023** | [Inside GitHub : Travailler avec les LLMs derrière GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Juin 2023** | [Comment rédiger de meilleurs prompts pour GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Juillet 2023** | [.. GitHub Copilot va au-delà de Codex avec un modèle d'IA amélioré](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Juillet 2023
La véritable valeur des modèles réside dans la capacité à créer et publier des _bibliothèques de prompts_ pour des domaines d'application spécifiques - où le modèle de prompt est désormais _optimisé_ pour refléter le contexte ou les exemples spécifiques à l'application, rendant les réponses plus pertinentes et précises pour l'audience ciblée. Le dépôt [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) est un excellent exemple de cette approche, organisant une bibliothèque de prompts pour le domaine de l'éducation avec un accent sur des objectifs clés tels que la planification des cours, la conception de programmes, le tutorat des étudiants, etc.

## Contenu de soutien

Si nous pensons à la construction de prompts comme ayant une instruction (tâche) et un objectif (contenu principal), alors le _contenu secondaire_ est comme un contexte supplémentaire que nous fournissons pour **influencer le résultat d'une certaine manière**. Il pourrait s'agir de paramètres de réglage, d'instructions de formatage, de taxonomies de sujets, etc. qui peuvent aider le modèle à _adapter_ sa réponse pour répondre aux objectifs ou aux attentes souhaités de l'utilisateur.

Par exemple : Étant donné un catalogue de cours avec des métadonnées étendues (nom, description, niveau, balises de métadonnées, instructeur, etc.) sur tous les cours disponibles dans le programme :

- nous pouvons définir une instruction pour "résumer le catalogue de cours pour l'automne 2023"
- nous pouvons utiliser le contenu principal pour fournir quelques exemples du résultat souhaité
- nous pouvons utiliser le contenu secondaire pour identifier les 5 principales "balises" d'intérêt.

Maintenant, le modèle peut fournir un résumé dans le format montré par les quelques exemples - mais si un résultat a plusieurs balises, il peut prioriser les 5 balises identifiées dans le contenu secondaire.

---

<!--
MODÈLE DE LEÇON :
Cette unité devrait couvrir le concept clé #1.
Renforcez le concept avec des exemples et des références.

CONCEPT #3 :
Techniques d'ingénierie de prompts.
Quelles sont certaines techniques de base pour l'ingénierie de prompts ?
Illustrer avec des exercices.
-->

## Meilleures pratiques de prompting

Maintenant que nous savons comment les prompts peuvent être _construits_, nous pouvons commencer à réfléchir à la manière de les _concevoir_ pour refléter les meilleures pratiques. Nous pouvons penser à cela en deux parties - avoir le bon _état d'esprit_ et appliquer les bonnes _techniques_.

### État d'esprit de l'ingénierie de prompts

L'ingénierie de prompts est un processus de tâtonnement, donc gardez à l'esprit trois grands facteurs directeurs :

1. **La compréhension du domaine est importante.** La précision et la pertinence des réponses dépendent du _domaine_ dans lequel l'application ou l'utilisateur opère. Appliquez votre intuition et votre expertise du domaine pour **personnaliser davantage les techniques**. Par exemple, définissez des _personnalités spécifiques au domaine_ dans vos prompts système, ou utilisez des _modèles spécifiques au domaine_ dans vos prompts utilisateur. Fournissez du contenu secondaire qui reflète des contextes spécifiques au domaine, ou utilisez des _indices et exemples spécifiques au domaine_ pour guider le modèle vers des schémas d'utilisation familiers.

2. **La compréhension du modèle est importante.** Nous savons que les modèles sont stochastiques par nature. Mais les implémentations de modèles peuvent également varier en termes de jeu de données d'entraînement qu'ils utilisent (connaissances pré-entraînées), les capacités qu'ils fournissent (par exemple, via API ou SDK) et le type de contenu pour lequel ils sont optimisés (par exemple, code vs. images vs. texte). Comprenez les forces et les limites du modèle que vous utilisez, et utilisez ces connaissances pour _prioriser les tâches_ ou construire des _modèles personnalisés_ optimisés pour les capacités du modèle.

3. **L'itération et la validation sont importantes.** Les modèles évoluent rapidement, tout comme les techniques d'ingénierie de prompts. En tant qu'expert du domaine, vous pouvez avoir d'autres contextes ou critères pour _votre_ application spécifique, qui peuvent ne pas s'appliquer à la communauté au sens large. Utilisez les outils et techniques d'ingénierie de prompts pour "démarrer" la construction de prompts, puis itérez et validez les résultats en utilisant votre propre intuition et expertise du domaine. Enregistrez vos idées et créez une **base de connaissances** (par exemple, bibliothèques de prompts) qui peut être utilisée comme nouvelle référence par d'autres, pour des itérations plus rapides à l'avenir.

## Meilleures pratiques

Voyons maintenant les meilleures pratiques courantes recommandées par [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) et les praticiens de [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Quoi                              | Pourquoi                                                                                                                                                                                                                                               |
| :-------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Évaluer les derniers modèles.     | Les nouvelles générations de modèles sont susceptibles d'avoir des fonctionnalités et une qualité améliorées - mais peuvent également entraîner des coûts plus élevés. Évaluez-les pour leur impact, puis prenez des décisions de migration.                                                   |
| Séparer les instructions et le contexte | Vérifiez si votre modèle/fournisseur définit des _délimiteurs_ pour distinguer plus clairement les instructions, le contenu principal et secondaire. Cela peut aider les modèles à attribuer plus précisément des poids aux tokens.                                               |
| Soyez spécifique et clair         | Donnez plus de détails sur le contexte souhaité, le résultat, la longueur, le format, le style, etc. Cela améliorera à la fois la qualité et la cohérence des réponses. Capturez des recettes dans des modèles réutilisables.                                                              |
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

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` valeurs. Revenez à la [section Sandbox d'apprentissage](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) pour apprendre comment.

### Ensuite, ouvrez le Jupyter Notebook

- Sélectionnez le noyau d'exécution. Si vous utilisez les options 1 ou 2, sélectionnez simplement le noyau Python 3.10.x par défaut fourni par le conteneur de développement.

Vous êtes prêt à exécuter les exercices. Notez qu'il n'y a pas de _bonnes ou mauvaises_ réponses ici - juste l'exploration d'options par tâtonnement et la construction d'une intuition pour ce qui fonctionne pour un modèle et un domaine d'application donné.

_Pour cette raison, il n'y a pas de segments de solution de code dans cette leçon. Au lieu de cela, le Notebook aura des cellules Markdown intitulées "Ma solution :" qui montrent un exemple de sortie pour référence._

 <!--
MODÈLE DE LEÇON :
Enveloppez la section avec un résumé et des ressources pour l'apprentissage autonome.
-->

## Vérification des connaissances

Lequel des éléments suivants est un bon prompt suivant quelques bonnes pratiques raisonnables ?

1. Montrez-moi une image de voiture rouge
2. Montrez-moi une image de voiture rouge de marque Volvo et modèle XC90 garée près d'une falaise avec le soleil couchant
3. Montrez-moi une image de voiture rouge de marque Volvo et modèle XC90

A : 2, c'est le meilleur prompt car il fournit des détails sur "quoi" et entre dans les spécificités (pas n'importe quelle voiture mais une marque et un modèle spécifiques) et il décrit également le cadre général. 3 est le suivant meilleur car il contient également beaucoup de description.

## 🚀 Défi

Voyez si vous pouvez tirer parti de la technique "indice" avec le prompt : Complétez la phrase "Montrez-moi une image de voiture rouge de marque Volvo et ". Que répond-il, et comment l'amélioreriez-vous ?

## Excellent travail ! Continuez votre apprentissage

Vous souhaitez en savoir plus sur les différents concepts d'ingénierie de prompts ? Rendez-vous sur la [page d'apprentissage continu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour trouver d'autres ressources intéressantes sur ce sujet.

Dirigez-vous vers la leçon 5 où nous examinerons [les techniques avancées de prompting](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst) !

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue maternelle doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction professionnelle par un humain est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.