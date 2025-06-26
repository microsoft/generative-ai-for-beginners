<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "57c41f2af71001a2cff9d8eb797cb843",
  "translation_date": "2025-06-25T06:58:25+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "fr"
}
-->
# Contribuer

Ce projet accueille les contributions et suggestions. La plupart des contributions nécessitent que vous acceptiez un Accord de Licence de Contributeur (CLA) déclarant que vous avez le droit de nous accorder les droits d'utiliser votre contribution. Pour plus de détails, visitez <https://cla.microsoft.com>.

> Important : lors de la traduction de texte dans ce dépôt, assurez-vous de ne pas utiliser de traduction automatique. Nous vérifierons les traductions via la communauté, alors veuillez vous proposer uniquement pour les traductions dans les langues que vous maîtrisez.

Lorsque vous soumettez une demande de tirage, un CLA-bot déterminera automatiquement si vous devez fournir un CLA et décorera la PR de manière appropriée (par exemple, étiquette, commentaire). Suivez simplement les instructions fournies par le bot. Vous n'aurez besoin de le faire qu'une seule fois pour tous les dépôts utilisant notre CLA.

## Code de Conduite

Ce projet a adopté le [Code de Conduite Open Source de Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pour plus d'informations, lisez la [FAQ du Code de Conduite](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) ou contactez [opencode@microsoft.com](mailto:opencode@microsoft.com) pour toute question ou commentaire supplémentaire.

## Question ou Problème ?

Veuillez ne pas ouvrir de problèmes GitHub pour des questions de support général car la liste GitHub doit être utilisée pour les demandes de fonctionnalités et les rapports de bogues. De cette façon, nous pouvons plus facilement suivre les problèmes ou les bogues réels du code et séparer la discussion générale du code réel.

## Fautes de frappe, Problèmes, Bogues et contributions

Chaque fois que vous soumettez des modifications au dépôt Generative AI for Beginners, veuillez suivre ces recommandations.

* Forkez toujours le dépôt sur votre propre compte avant de faire vos modifications
* Ne combinez pas plusieurs modifications en une seule demande de tirage. Par exemple, soumettez toute correction de bogue et mise à jour de documentation en utilisant des PR séparées
* Si votre demande de tirage montre des conflits de fusion, assurez-vous de mettre à jour votre branche principale locale pour qu'elle soit un miroir de ce qui est dans le dépôt principal avant de faire vos modifications
* Si vous soumettez une traduction, veuillez créer une PR pour tous les fichiers traduits car nous n'acceptons pas les traductions partielles du contenu
* Si vous soumettez une faute de frappe ou une correction de documentation, vous pouvez combiner les modifications dans une seule PR là où c'est approprié

## Conseils Généraux pour la rédaction

- Assurez-vous que toutes vos URLs sont entourées de crochets suivis d'une parenthèse sans espaces supplémentaires autour ou à l'intérieur `[](../..)`.
- Assurez-vous que tout lien relatif (c'est-à-dire les liens vers d'autres fichiers et dossiers dans le dépôt) commence par un `./` se référant à un fichier ou un dossier situé dans le répertoire de travail actuel ou un `../` se référant à un fichier ou un dossier situé dans un répertoire parent.
- Assurez-vous que tout lien relatif (c'est-à-dire les liens vers d'autres fichiers et dossiers dans le dépôt) a un ID de suivi (c'est-à-dire `?` ou `&` puis `wt.mc_id=` ou `WT.mc_id=`) à la fin.
- Assurez-vous que toute URL des domaines suivants _github.com, microsoft.com, visualstudio.com, aka.ms, et azure.com_ a un ID de suivi (c'est-à-dire `?` ou `&` puis `wt.mc_id=` ou `WT.mc_id=`) à la fin.
- Assurez-vous que vos liens ne contiennent pas de paramètres de localisation spécifiques à un pays (c'est-à-dire `/en-us/` ou `/en/`).
- Assurez-vous que toutes les images sont stockées dans le dossier `./images`.
- Assurez-vous que les images ont des noms descriptifs utilisant des caractères anglais, des chiffres et des tirets dans le nom de votre image.

## Flux de Travail GitHub

Lorsque vous soumettez une demande de tirage, quatre flux de travail différents seront déclenchés pour valider les règles précédentes. Suivez simplement les instructions listées ici pour réussir les vérifications de flux de travail.

- [Vérifier les Chemins Relatifs Cassés](../..)
- [Vérifier que les Chemins ont un Suivi](../..)
- [Vérifier que les URLs ont un Suivi](../..)
- [Vérifier que les URLs n'ont pas de Localisation](../..)

### Vérifier les Chemins Relatifs Cassés

Ce flux de travail s'assure que tout chemin relatif dans vos fichiers fonctionne. Ce dépôt est déployé sur les pages GitHub, vous devez donc être très prudent lorsque vous tapez les liens qui relient tout pour ne pas diriger quelqu'un vers le mauvais endroit.

Pour vous assurer que vos liens fonctionnent correctement, utilisez simplement VS code pour vérifier cela.

Par exemple, lorsque vous survolez un lien dans vos fichiers, vous serez invité à suivre le lien en appuyant sur **ctrl + clic**

![Capture d'écran de VS code suivant les liens](../../translated_images/vscode-follow-link.85520ab6a1237adcf01cc9cd8c228ce7b32ae685a034250bd5109e2682b9dfca.fr.png)

Si vous cliquez sur un lien et qu'il ne fonctionne pas localement, alors, il déclenchera sûrement le flux de travail et ne fonctionnera pas sur GitHub.

Pour résoudre ce problème, essayez de taper le lien avec l'aide de VS code.

Lorsque vous tapez `./` ou `../`, VS code vous invitera à choisir parmi les options disponibles selon ce que vous avez tapé.

![Capture d'écran de VS code sélectionnant le chemin relatif](../../translated_images/vscode-select-relative-path.3804eb73c3a9e5f2d345e3d3288f8173a9e584254d0e505d8bcbc6461dbf1f6c.fr.png)

Suivez le chemin en cliquant sur le fichier ou le dossier souhaité et vous serez sûr que votre chemin n'est pas cassé.

Une fois que vous avez ajouté le bon chemin relatif, enregistrez et poussez vos modifications, le flux de travail sera déclenché à nouveau pour vérifier vos modifications. Si vous réussissez la vérification, alors vous êtes prêt à partir.

### Vérifier que les Chemins ont un Suivi

Ce flux de travail s'assure que tout chemin relatif a un suivi. Ce dépôt est déployé sur les pages GitHub, nous devons donc suivre le mouvement entre les différents fichiers et dossiers.

Pour vous assurer que vos chemins relatifs ont un suivi, vérifiez simplement le texte suivant `?wt.mc_id=` à la fin du chemin. S'il est ajouté à vos chemins relatifs, vous réussirez cette vérification.

Sinon, vous pourriez obtenir l'erreur suivante.

![Capture d'écran du commentaire GitHub vérifiant les chemins manquants de suivi](../../translated_images/github-check-paths-missing-tracking-comment.880d4afe03e898ffadeebe0f61f7fdea7525c25238bead9fecabc81a0a83b1c0.fr.png)

Pour résoudre ce problème, essayez d'ouvrir le chemin de fichier que le flux de travail a mis en évidence et ajoutez l'ID de suivi à la fin des chemins relatifs.

Une fois que vous avez ajouté l'ID de suivi, enregistrez et poussez vos modifications, le flux de travail sera déclenché à nouveau pour vérifier vos modifications. Si vous réussissez la vérification, alors vous êtes prêt à partir.

### Vérifier que les URLs ont un Suivi

Ce flux de travail s'assure que toute URL web a un suivi. Ce dépôt est accessible à tous, vous devez donc vous assurer de suivre l'accès pour savoir d'où vient le trafic.

Pour vous assurer que vos URLs ont un suivi, vérifiez simplement le texte suivant `?wt.mc_id=` à la fin de l'URL. S'il est ajouté à vos URLs, vous réussirez cette vérification.

Sinon, vous pourriez obtenir l'erreur suivante.

![Capture d'écran du commentaire GitHub vérifiant les URLs manquantes de suivi](../../translated_images/github-check-urls-missing-tracking-comment.1bd00d20b24a1e2e3179e59e1bd7d44f16637a1bb1ab265562565251166841ef.fr.png)

Pour résoudre ce problème, essayez d'ouvrir le chemin de fichier que le flux de travail a mis en évidence et ajoutez l'ID de suivi à la fin des URLs.

Une fois que vous avez ajouté l'ID de suivi, enregistrez et poussez vos modifications, le flux de travail sera déclenché à nouveau pour vérifier vos modifications. Si vous réussissez la vérification, alors vous êtes prêt à partir.

### Vérifier que les URLs n'ont pas de Localisation

Ce flux de travail s'assure que toute URL web n'a pas de localisation spécifique à un pays. Ce dépôt est accessible à tous dans le monde entier, vous devez donc vous assurer de ne pas inclure la localisation de votre pays dans les URLs.

Pour vous assurer que vos URLs n'ont pas de localisation de pays, vérifiez simplement le texte suivant `/en-us/` ou `/en/` ou toute autre localisation linguistique n'importe où dans l'URL. S'il n'est pas présent dans vos URLs, vous réussirez cette vérification.

Sinon, vous pourriez obtenir l'erreur suivante.

![Capture d'écran du commentaire GitHub vérifiant la localisation de pays ajoutée aux URLs](../../translated_images/github-check-country-locale-comment.2f4fe93228161dee6ec8210f3d6ccc66af6864f6b178b8d96f30818498fba72a.fr.png)

Pour résoudre ce problème, essayez d'ouvrir le chemin de fichier que le flux de travail a mis en évidence et retirez la localisation de pays des URLs.

Une fois que vous avez retiré la localisation de pays, enregistrez et poussez vos modifications, le flux de travail sera déclenché à nouveau pour vérifier vos modifications. Si vous réussissez la vérification, alors vous êtes prêt à partir.

Félicitations ! Nous vous recontacterons dès que possible avec des retours sur votre contribution.

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.