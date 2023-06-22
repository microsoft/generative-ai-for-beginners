# Contribute by translating lessons

We welcome translations for the lessons in this curriculum!
## Guidelines

There are folders in each lesson folder and lesson introduction folder which contain the translated markdown files.

> Note, please do not translate any code in the code sample files; the only things to translate are README, assignments, and the quizzes. Thanks!

Translated files should follow this naming convention:

**README._[language]_.md**

where _[language]_ is a two letter language abbreviation following the ISO 639-1 standard (e.g. `README.es.md` for Spanish and `README.nl.md` for Dutch).

**assignment._[language]_.md**

Similar to Readme's, please translate the assignments as well.

> Important: when translating text in this repo, please ensure that you do not use machine translation. We will verify translations via the community, so please only volunteer for translations in languages where you are proficient.

**Quizzes**

1. Add your translation to the quiz-app by adding a file here: https://github.com/microsoft/ML-For-Beginners/tree/main/quiz-app/src/assets/translations, with proper naming convention (en.json, fr.json). **Please don't localize the words 'true' or 'false' however. thanks!**

2. Add your language code to the dropdown in the quiz-app's App.vue file.

3. Edit the quiz-app's [translations index.js file](https://github.com/microsoft/ML-For-Beginners/blob/main/quiz-app/src/assets/translations/index.js) to add your language.

4. Finally, edit ALL the quiz links in your translated README.md files to point directly to your translated quiz: https://gray-sand-07a10f403.1.azurestaticapps.net/quiz/1 becomes https://gray-sand-07a10f403.1.azurestaticapps.net/quiz/1?loc=id

**THANK YOU**

We truly appreciate your efforts!
