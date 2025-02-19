# Contribution

Ce projet accueille avec plaisir les contributions et suggestions. La plupart des contributions nécessitent que vous acceptiez un Accord de Licence de Contributeur (CLA) déclarant que vous avez le droit de nous accorder les droits d'utiliser votre contribution. Pour plus de détails, visitez <https://cla.microsoft.com>.

> Important : lors de la traduction de texte dans ce dépôt, assurez-vous de ne pas utiliser de traduction automatique. Nous vérifierons les traductions via la communauté, donc veuillez ne vous proposer que pour des traductions dans les langues que vous maîtrisez.

Lorsque vous soumettez une pull request, un CLA-bot déterminera automatiquement si vous devez fournir un CLA et décorera la PR en conséquence (par exemple, étiquette, commentaire). Suivez simplement les instructions fournies par le bot. Vous n'aurez à le faire qu'une seule fois pour tous les dépôts utilisant notre CLA.

## Code de Conduite

Ce projet a adopté le [Code de Conduite Open Source de Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pour plus d'informations, lisez la [FAQ sur le Code de Conduite](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) ou contactez [opencode@microsoft.com](mailto:opencode@microsoft.com) pour toute question ou commentaire supplémentaire.

## Question ou Problème ?

Veuillez ne pas ouvrir de problèmes GitHub pour des questions générales de support, car la liste GitHub doit être utilisée pour les demandes de fonctionnalités et les rapports de bugs. De cette façon, nous pouvons plus facilement suivre les problèmes ou bugs réels du code et garder la discussion générale séparée du code réel.

## Fautes de frappe, Problèmes, Bugs et contributions

Chaque fois que vous soumettez des modifications au dépôt Generative AI for Beginners, veuillez suivre ces recommandations.

* Toujours forker le dépôt sur votre propre compte avant de faire vos modifications
* Ne pas combiner plusieurs modifications dans une seule pull request. Par exemple, soumettez toute correction de bug et mise à jour de documentation en utilisant des PRs séparées
* Si votre pull request montre des conflits de fusion, assurez-vous de mettre à jour votre main locale pour qu'elle soit un miroir de ce qui est dans le dépôt principal avant de faire vos modifications
* Si vous soumettez une traduction, veuillez créer une PR pour tous les fichiers traduits car nous n'acceptons pas les traductions partielles pour le contenu
* Si vous soumettez une faute de frappe ou une correction de documentation, vous pouvez combiner les modifications en une seule PR là où cela est approprié

## Conseils Généraux pour la rédaction

- Assurez-vous que toutes vos URLs sont entourées de crochets suivis d'une parenthèse sans espaces supplémentaires autour ou à l'intérieur `[](../..)`.
- Assurez-vous que tout lien relatif (c'est-à-dire des liens vers d'autres fichiers et dossiers dans le dépôt) commence par un `./` faisant référence à un fichier ou un dossier situé dans le répertoire de travail actuel ou un `../` faisant référence à un fichier ou un dossier situé dans un répertoire de travail parent.
- Assurez-vous que tout lien relatif (c'est-à-dire des liens vers d'autres fichiers et dossiers dans le dépôt) a un ID de suivi (c'est-à-dire `?` ou `&` puis `wt.mc_id=` ou `WT.mc_id=`) à la fin.
- Assurez-vous que toute URL des domaines suivants _github.com, microsoft.com, visualstudio.com, aka.ms, et azure.com_ a un ID de suivi (c'est-à-dire `?` ou `&` puis `wt.mc_id=` ou `WT.mc_id=`) à la fin.
- Assurez-vous que vos liens n'ont pas de locale spécifique au pays (c'est-à-dire `/en-us/` ou `/en/`).
- Assurez-vous que toutes les images sont stockées dans le dossier `./images`.
- Assurez-vous que les images ont des noms descriptifs utilisant des caractères anglais, des chiffres et des tirets dans le nom de votre image.

## Flux de Travail GitHub

Lorsque vous soumettez une pull request, quatre flux de travail différents seront déclenchés pour valider les règles précédentes. Suivez simplement les instructions listées ici pour réussir les vérifications des flux de travail.

- [Vérifier les Chemins Relatifs Cassés](../..)
- [Vérifier que les Chemins ont un Suivi](../..)
- [Vérifier que les URLs ont un Suivi](../..)
- [Vérifier que les URLs n'ont pas de Locale](../..)

### Vérifier les Chemins Relatifs Cassés

Ce flux de travail s'assure que tout chemin relatif dans vos fichiers fonctionne. Ce dépôt est déployé sur GitHub pages, donc vous devez être très prudent lorsque vous tapez les liens qui relient tout pour ne pas diriger quelqu'un au mauvais endroit.

Pour vous assurer que vos liens fonctionnent correctement, utilisez simplement VS code pour vérifier cela.

Par exemple, lorsque vous survolez un lien dans vos fichiers, vous serez invité à suivre le lien en appuyant sur **ctrl + clic**

![Capture d'écran VS code suivre les liens](../../translated_images/vscode-follow-link.png?WT.mc_id=academic-105485-koreyst "Capture d'écran de l'invite VS code pour suivre un lien lorsque vous survolez un lien.fd96348c7853e06270e566252c9fd64d578b888bf4be87282b7b229351a4ea1b.fr.")

Si vous cliquez sur un lien et qu'il ne fonctionne pas localement, alors, il déclenchera sûrement le flux de travail et ne fonctionnera pas sur GitHub.

Pour résoudre ce problème, essayez de taper le lien avec l'aide de VS code.

Lorsque vous tapez `./` ou `../`, VS code vous invitera à choisir parmi les options disponibles en fonction de ce que vous avez tapé.

![Capture d'écran VS code sélectionner le chemin relatif](../../translated_images/vscode-select-relative-path.png?WT.mc_id=academic-105485-koreyst "Capture d'écran de l'invite VS code pour sélectionner le chemin relatif dans une liste déroulante.22fb42bdd289e691523624bae8bb37bc11a670c81c8bf4b907c8da7e1a91e31d.fr.")

Suivez le chemin en cliquant sur le fichier ou le dossier souhaité et vous serez sûr que votre chemin n'est pas cassé.

Une fois que vous avez ajouté le chemin relatif correct, enregistrez et poussez vos modifications, le flux de travail sera à nouveau déclenché pour vérifier vos modifications. Si vous réussissez la vérification, alors vous êtes prêt.

### Vérifier que les Chemins ont un Suivi

Ce flux de travail s'assure que tout chemin relatif a un suivi. Ce dépôt est déployé sur GitHub pages, donc nous devons suivre le mouvement entre les différents fichiers et dossiers.

Pour vous assurer que vos chemins relatifs ont un suivi, vérifiez simplement le texte suivant `?wt.mc_id=` à la fin du chemin. Si c'est ajouté à vos chemins relatifs, alors vous réussirez cette vérification.

Sinon, vous pourriez obtenir l'erreur suivante.

![Capture d'écran commentaire GitHub vérification des chemins manquant de suivi](../../translated_images/github-check-paths-missing-tracking-comment.png?WT.53205eab9ff5f1865ed6ec15ba755daf8235945bd6398cccf7c547bb2b18fc90.fr.mc_id=academic-105485-koreyst "capture d'écran d'un commentaire github montrant un suivi manquant des chemins relatifs")

Pour résoudre ce problème, essayez d'ouvrir le chemin du fichier que le flux de travail a mis en évidence et ajoutez l'ID de suivi à la fin des chemins relatifs.

Une fois que vous avez ajouté l'ID de suivi, enregistrez et poussez vos modifications, le flux de travail sera à nouveau déclenché pour vérifier vos modifications. Si vous réussissez la vérification, alors vous êtes prêt.

### Vérifier que les URLs ont un Suivi

Ce flux de travail s'assure que toute URL web a un suivi. Ce dépôt est accessible à tous, donc vous devez vous assurer de suivre l'accès pour savoir d'où vient le trafic.

Pour vous assurer que vos URLs ont un suivi, vérifiez simplement le texte suivant `?wt.mc_id=` à la fin de l'URL. Si c'est ajouté à vos URLs, alors vous réussirez cette vérification.

Sinon, vous pourriez obtenir l'erreur suivante.

![Capture d'écran commentaire GitHub vérification des URLs manquant de suivi](../../translated_images/github-check-urls-missing-tracking-comment.png?WT.f4c94600a3d19fa0c3fc9373b7e7dd9cec3d418ede7aa440dabf8fefcd1ff047.fr.mc_id=academic-105485-koreyst "capture d'écran d'un commentaire github montrant un suivi manquant des urls")

Pour résoudre ce problème, essayez d'ouvrir le chemin du fichier que le flux de travail a mis en évidence et ajoutez l'ID de suivi à la fin des URLs.

Une fois que vous avez ajouté l'ID de suivi, enregistrez et poussez vos modifications, le flux de travail sera à nouveau déclenché pour vérifier vos modifications. Si vous réussissez la vérification, alors vous êtes prêt.

### Vérifier que les URLs n'ont pas de Locale

Ce flux de travail s'assure que toute URL web n'a pas de locale spécifique au pays. Ce dépôt est accessible à tous dans le monde entier, donc vous devez vous assurer de ne pas inclure le locale de votre pays dans les URLs.

Pour vous assurer que vos URLs n'ont pas de locale de pays, vérifiez simplement le texte suivant `/en-us/` ou `/en/` ou tout autre locale de langue n'importe où dans l'URL. Si ce n'est pas présent dans vos URLs, alors vous réussirez cette vérification.

Sinon, vous pourriez obtenir l'erreur suivante.

![Capture d'écran commentaire GitHub vérification des locales de pays](../../translated_images/github-check-country-locale-comment.png?WT.e839b98f9eb81b3f1cfe24a37e2232f771964fca1e10ed38f1ecd3d61415efe2.fr.mc_id=academic-105485-koreyst "capture d'écran d'un commentaire github montrant l'ajout de locales de pays aux urls")

Pour résoudre ce problème, essayez d'ouvrir le chemin du fichier que le flux de travail a mis en évidence et supprimez le locale de pays des URLs.

Une fois que vous avez supprimé le locale de pays, enregistrez et poussez vos modifications, le flux de travail sera à nouveau déclenché pour vérifier vos modifications. Si vous réussissez la vérification, alors vous êtes prêt.

Félicitations ! Nous vous recontacterons dès que possible avec des commentaires sur votre contribution.

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatisée par IA. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle humaine. Nous ne sommes pas responsables des malentendus ou des mauvaises interprétations résultant de l'utilisation de cette traduction.