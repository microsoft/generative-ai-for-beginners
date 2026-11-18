# Contribution

Ce projet accueille volontiers les contributions et suggestions. La plupart des contributions requièrent que vous
acceptiez un Accord de Licence pour Contributeur (CLA) déclarant que vous avez le droit,
et que vous accordez effectivement, les droits de pouvoir utiliser votre contribution. Pour plus de détails, consultez
<https://cla.microsoft.com>.

> Important : lorsque vous traduisez du texte dans ce dépôt, veuillez vous assurer de ne pas utiliser la traduction automatique. Nous vérifierons les traductions via la communauté, alors veuillez ne proposer des traductions que dans les langues que vous maîtrisez.

Lorsque vous soumettez une pull request, un bot CLA déterminera automatiquement si vous devez
fournir un CLA et décorera la PR en conséquence (par exemple, étiquette, commentaire). Il vous suffit de suivre les
instructions fournies par le bot. Vous ne devrez le faire qu'une seule fois pour tous les dépôts utilisant notre CLA.

## Code de Conduite

Ce projet a adopté le [Code de Conduite Open Source Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst).
Pour plus d'informations, consultez la [FAQ sur le Code de Conduite](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) ou contactez [opencode@microsoft.com](mailto:opencode@microsoft.com) pour toute question ou commentaire supplémentaire.

## Question ou Problème ?

Veuillez ne pas ouvrir de problèmes GitHub pour des questions de support général, car la liste GitHub doit être utilisée pour les demandes de fonctionnalités et les rapports de bugs. Cela nous permet de mieux suivre les problèmes ou bugs réels dans le code et de garder la discussion générale séparée du code lui-même.

## Fautes de frappe, problèmes, bugs et contributions

Chaque fois que vous soumettez des modifications au dépôt Generative AI for Beginners, veuillez suivre ces recommandations.

* Forkez toujours le dépôt dans votre propre compte avant de faire vos modifications
* Ne combinez pas plusieurs modifications dans une seule pull request. Par exemple, soumettez toute correction de bug et mises à jour de la documentation dans des PR distinctes
* Si votre pull request montre des conflits de fusion, assurez-vous de mettre à jour votre main local pour qu'il soit un miroir exact du dépôt principal avant de faire vos modifications
* Si vous soumettez une traduction, créez une seule PR pour tous les fichiers traduits car nous n'acceptons pas les traductions partielles du contenu
* Si vous soumettez une faute de frappe ou une correction de documentation, vous pouvez regrouper les modifications dans une seule PR lorsque cela est approprié

## Champ éditorial et produits tiers

Ce programme se concentre sur les technologies Microsoft et les standards ouverts indépendants des fournisseurs. Les contributions doivent avoir un objectif éducatif clair et ne doivent pas être principalement destinées à introduire ou promouvoir un produit commercial tiers, un service hébergé, un routeur de modèles, un SDK, un serveur MCP, ou toute autre offre spécifique à un fournisseur.

Les logiciels open source et les dépendances tierces peuvent être référencés lorsqu'ils sont nécessaires pour expliquer un standard ouvert ou un scénario d'interopérabilité, sont présentés de manière neutre, et ne sont pas centrés sur un produit ou un point de terminaison hébergé d'un fournisseur. Si votre contribution proposée inclut un produit ou service spécifique à un fournisseur, ouvrez un problème et obtenez l'approbation du mainteneur avant de soumettre une pull request.

Les contributeurs doivent divulguer tout emploi, propriété, parrainage, ou autre affiliation pertinent avec un produit ou service mentionné dans leur contribution. N'incluez pas de revendications non supportées concernant les prix, les performances, la sécurité, la confidentialité, ou les comparaisons. Les exemples exécutables ne doivent pas transmettre par défaut les données des apprenants ni effectuer des actions publiques via un service tiers externe.

## Directives générales pour la rédaction

- Assurez-vous que toutes vos URLs sont encadrées par des crochets suivis de parenthèses sans espaces supplémentaires autour ni à l'intérieur `[]()`.
- Assurez-vous que tout lien relatif (c'est-à-dire vers d'autres fichiers et dossiers dans le dépôt) commence par un `./` référant à un fichier ou dossier situé dans le répertoire de travail actuel ou un `../` référant à un fichier ou dossier situé dans un répertoire parent.
- Assurez-vous que tout lien relatif (c'est-à-dire vers d'autres fichiers et dossiers dans le dépôt) comporte un ID de suivi (c'est-à-dire `?` ou `&` puis `wt.mc_id=` ou `WT.mc_id=`) à sa fin.
- Assurez-vous que toute URL provenant des domaines suivants _github.com, microsoft.com, visualstudio.com, aka.ms, et azure.com_ possède un ID de suivi (c'est-à-dire `?` ou `&` puis `wt.mc_id=` ou `WT.mc_id=`) à la fin.
- Assurez-vous que vos liens ne contiennent pas de paramètres de langue spécifiques à un pays (c'est-à-dire `/en-us/` ou `/en/`).
- Assurez-vous que toutes les images sont stockées dans le dossier `./images`.
- Assurez-vous que les images ont des noms descriptifs utilisant des caractères anglais, des chiffres, et des tirets dans le nom de votre image.

## Workflows GitHub

Lorsque vous soumettez une pull request, quatre workflows différents seront déclenchés pour valider les règles précédentes.
Il vous suffit de suivre les instructions listées ici pour réussir les contrôles des workflows.

- [Vérifier les chemins relatifs cassés](#check-broken-relative-paths)
- [Vérifier que les chemins ont un suivi](#check-paths-have-tracking)
- [Vérifier que les URLs ont un suivi](#check-urls-have-tracking)
- [Vérifier que les URLs n'ont pas de paramètre de langue](#check-urls-dont-have-locale)

### Vérifier les chemins relatifs cassés

Ce workflow garantit que tout chemin relatif dans vos fichiers fonctionne.
Ce dépôt est déployé sur GitHub pages donc vous devez être très prudent lorsque vous tapez les liens qui relient tout afin de ne diriger personne vers un mauvais endroit.

Pour vous assurer que vos liens fonctionnent correctement, utilisez simplement VS code pour vérifier cela.

Par exemple, lorsque vous survolez un lien dans vos fichiers, vous serez invité à suivre le lien en appuyant sur **ctrl + clic**

![Capture d'écran VS code suivre les liens](../../translated_images/fr/vscode-follow-link.85520ab6a1237adc.webp?WT.mc_id=academic-105485-koreyst "Capture d'écran de l'invite vs code pour suivre un lien lorsque vous le survolez.")

Si vous cliquez sur un lien et qu'il ne fonctionne pas localement, alors il déclenchera sûrement le workflow et ne fonctionnera pas sur GitHub.

Pour résoudre ce problème, essayez de taper le lien avec l'aide de VS code.

Lorsque vous tapez `./` ou `../`, VS code vous invite à choisir parmi les options disponibles selon ce que vous avez tapé.

![Capture d'écran VS code sélection chemin relatif](../../translated_images/fr/vscode-select-relative-path.3804eb73c3a9e5f2.webp?WT.mc_id=academic-105485-koreyst "Capture d'écran de l'invite vs code pour sélectionner un chemin relatif depuis une liste popup.")

Suivez le chemin en cliquant sur le fichier ou dossier désiré et vous serez sûr que votre chemin n'est pas cassé.

Une fois que vous avez ajouté le chemin relatif correct, sauvegardez et poussez vos modifications, le workflow sera déclenché à nouveau pour vérifier vos changements.
Si vous réussissez la vérification, alors vous êtes prêt à continuer.

### Vérifier que les chemins ont un suivi

Ce workflow garantit que chaque chemin relatif contient un suivi.
Ce dépôt est déployé sur GitHub pages, donc nous devons tracer le déplacement entre les différents fichiers et dossiers.

Pour vous assurer que vos chemins relatifs contiennent un suivi, vérifiez simplement la présence du texte `?wt.mc_id=` à la fin du chemin.
S'il est ajouté à vos chemins relatifs, alors vous passerez ce contrôle.

Sinon, vous pouvez obtenir l'erreur suivante.

![Capture d'écran GitHub vérification chemins sans suivi commentaire](../../translated_images/fr/github-check-paths-missing-tracking-comment.880d4afe03e898ff.webp?WT.mc_id=academic-105485-koreyst "Capture d'écran d'un commentaire github indiquant l'absence de suivi dans les chemins relatifs")

Pour corriger ce problème, essayez d'ouvrir le chemin de fichier que le workflow a mis en évidence et ajoutez l'ID de suivi à la fin des chemins relatifs.

Une fois que vous avez ajouté l'ID de suivi, enregistrez et poussez vos modifications, le workflow sera déclenché de nouveau pour vérifier vos changements.
Si vous réussissez la vérification, alors vous êtes prêt à continuer.

### Vérifier que les URLs ont un suivi

Ce workflow garantit que toute URL web contient un suivi.
Ce dépôt est accessible à tous, donc vous devez vous assurer de tracer l'accès pour savoir d'où provient le trafic.

Pour vous assurer que vos URLs contiennent un suivi, vérifiez simplement la présence du texte `?wt.mc_id=` à la fin de l'URL.
S'il est ajouté à vos URLs, alors vous passerez ce contrôle.

Sinon, vous pouvez obtenir l'erreur suivante.

![Capture d'écran GitHub vérification URLs sans suivi commentaire](../../translated_images/fr/github-check-urls-missing-tracking-comment.1bd00d20b24a1e2e.webp?WT.mc_id=academic-105485-koreyst "Capture d'écran d'un commentaire github indiquant l'absence de suivi dans les URLs")

Pour corriger ce problème, essayez d'ouvrir le chemin de fichier que le workflow a mis en évidence et ajoutez l'ID de suivi à la fin des URLs.

Une fois que vous avez ajouté l'ID de suivi, enregistrez et poussez vos modifications, le workflow sera déclenché de nouveau pour vérifier vos changements.
Si vous réussissez la vérification, alors vous êtes prêt à continuer.

### Vérifier que les URLs n'ont pas de paramètre de langue

Ce workflow garantit que toute URL web ne contient pas de paramètre de langue spécifique à un pays.
Ce dépôt est accessible à tous dans le monde entier, donc vous devez vous assurer de ne pas inclure le paramètre de langue de votre pays dans les URLs.

Pour vous assurer que vos URLs ne contiennent pas de paramètre de langue, vérifiez simplement la présence du texte `/en-us/` ou `/en/` ou de tout autre paramètre de langue dans l'URL.
S'il n'est pas présent dans vos URLs, alors vous passerez ce contrôle.

Sinon, vous pouvez obtenir l'erreur suivante.

![Capture d'écran GitHub vérification paramètre de langue pays commentaire](../../translated_images/fr/github-check-country-locale-comment.2f4fe93228161dee.webp?WT.mc_id=academic-105485-koreyst "Capture d'écran d'un commentaire github montrant un paramètre de langue ajouté aux URLs")

Pour corriger ce problème, essayez d'ouvrir le chemin de fichier que le workflow a mis en évidence et supprimez le paramètre de langue des URLs.

Une fois que vous avez supprimé le paramètre de langue, enregistrez et poussez vos modifications, le workflow sera déclenché de nouveau pour vérifier vos changements.
Si vous réussissez la vérification, alors vous êtes prêt à continuer.

Félicitations ! Nous reviendrons vers vous dès que possible avec des commentaires sur votre contribution.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->