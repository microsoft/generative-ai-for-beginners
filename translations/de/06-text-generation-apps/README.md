# Aufbau von Textgenerierungsanwendungen

[![Aufbau von Textgenerierungsanwendungen](../../../translated_images/de/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Klicke auf das Bild oben, um das Video zu dieser Lektion anzusehen)_

Du hast bisher in diesem Curriculum gesehen, dass es Kernkonzepte wie Prompts gibt und sogar eine ganze Disziplin namens „Prompt Engineering“. Viele Tools, mit denen du interagieren kannst, wie ChatGPT, Office 365, Microsoft Power Platform und mehr, unterstützen dich dabei, mit Prompts etwas zu erreichen.

Um ein solches Erlebnis in eine App einzubauen, musst du Konzepte wie Prompts, Completions verstehen und eine Bibliothek auswählen, mit der du arbeiten möchtest. Genau das wirst du in diesem Kapitel lernen.

## Einführung

In diesem Kapitel wirst du:

- Die openai-Bibliothek und ihre Kernkonzepte kennenlernen.
- Eine Textgenerierungs-App mit openai erstellen.
- Verstehen, wie man Konzepte wie Prompt, Temperatur und Tokens benutzt, um eine Textgenerierungs-App zu bauen.

## Lernziele

Am Ende dieser Lektion wirst du in der Lage sein:

- Erklären, was eine Textgenerierungs-App ist.
- Eine Textgenerierungs-App mit openai zu erstellen.
- Deine App so zu konfigurieren, dass mehr oder weniger Tokens verwendet werden und auch die Temperatur für vielfältigere Ausgaben eingestellt wird.

## Was ist eine Textgenerierungs-App?

Normalerweise hat eine App eine Art Benutzeroberfläche wie die folgende:

- Kommando-basiert. Konsolen-Apps sind typische Apps, bei denen du einen Befehl eintippst und dieser eine Aufgabe ausführt. Zum Beispiel ist `git` eine kommando-basierte App.
- Benutzeroberfläche (UI). Manche Apps haben grafische Benutzeroberflächen (GUIs), bei denen du Buttons klickst, Text eingibst, Optionen auswählst und mehr.

### Konsolen- und UI-Apps sind begrenzt

Vergleiche das mit einer kommando-basierten App, bei der du einen Befehl eingibst:

- **Sie ist begrenzt**. Du kannst nicht einfach jeden beliebigen Befehl eintippen, nur die, die die App unterstützt.
- **Sprachspezifisch**. Manche Apps unterstützen viele Sprachen, aber standardmäßig ist die App für eine bestimmte Sprache gebaut, auch wenn du weitere Sprachunterstützung hinzufügen kannst.

### Vorteile von Textgenerierungs-Apps

Wie unterscheidet sich eine Textgenerierungs-App?

Bei einer Textgenerierungs-App hast du mehr Flexibilität, du bist nicht auf eine Reihe von Befehlen oder eine bestimmte Eingabesprache beschränkt. Stattdessen kannst du natürliche Sprache nutzen, um mit der App zu interagieren. Ein weiterer Vorteil ist, dass du bereits mit einer Datenquelle interagierst, die auf einem großen Korpus von Informationen trainiert wurde, während eine traditionelle App auf den Daten in einer Datenbank beschränkt sein könnte.

### Was kann ich mit einer Textgenerierungs-App bauen?

Es gibt viele Dinge, die du bauen kannst. Zum Beispiel:

- **Einen Chatbot**. Ein Chatbot, der Fragen zu Themen wie deinem Unternehmen und seinen Produkten beantwortet, könnte gut geeignet sein.
- **Helfer**. LLMs sind großartig bei Dingen wie Text zusammenfassen, Auswertungen von Texten erhalten, Texte wie Lebensläufe erstellen und mehr.
- **Code-Assistenten**. Je nach verwendetem Sprachmodell kannst du einen Code-Assistenten bauen, der dir beim Schreiben von Code hilft. Zum Beispiel kannst du ein Produkt wie GitHub Copilot sowie ChatGPT nutzen, um Code zu schreiben.

## Wie kann ich anfangen?

Du musst eine Möglichkeit finden, dich mit einem LLM zu integrieren, was normalerweise zwei Ansätze beinhaltet:

- Eine API verwenden. Hierbei erstellst du Webanfragen mit deinem Prompt und erhältst generierten Text zurück.
- Eine Bibliothek verwenden. Bibliotheken helfen, die API-Aufrufe zu kapseln und einfacher nutzbar zu machen.

## Bibliotheken/SDKs

Es gibt einige bekannte Bibliotheken zum Arbeiten mit LLMs wie:

- **openai**, diese Bibliothek macht es einfach, sich mit deinem Modell zu verbinden und Prompts zu senden.

Dann gibt es Bibliotheken auf höherer Ebene wie:

- **Langchain**. Langchain ist bekannt und unterstützt Python.
- **Semantic Kernel**. Semantic Kernel ist eine Bibliothek von Microsoft und unterstützt die Sprachen C#, Python und Java.

## Erste App mit openai

Lassen wir uns anschauen, wie wir unsere erste App bauen, welche Bibliotheken wir brauchen, wie viel erforderlich ist und so weiter.

### openai installieren

Es gibt viele Bibliotheken, um mit OpenAI oder Azure OpenAI zu interagieren. Es ist auch möglich, verschiedene Programmiersprachen wie C#, Python, JavaScript, Java und mehr zu verwenden. Wir haben uns entschieden, die `openai` Python-Bibliothek zu verwenden, also nutzen wir `pip`, um sie zu installieren.

```bash
pip install openai
```

### Eine Ressource erstellen

Du musst die folgenden Schritte ausführen:

- Erstelle ein Konto bei Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Erhalte Zugriff auf Azure OpenAI. Gehe zu [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) und beantrage Zugriff.

  > [!NOTE]
  > Zum Zeitpunkt des Schreibens musst du den Zugriff auf Azure OpenAI beantragen.

- Installiere Python <https://www.python.org/>
- Habe eine Azure OpenAI Service-Ressource erstellt. Sieh dir diese Anleitung dazu an, wie man eine [Ressource erstellt](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### API-Schlüssel und Endpunkt finden

Jetzt musst du deiner `openai`-Bibliothek mitteilen, welchen API-Schlüssel sie verwenden soll. Um deinen API-Schlüssel zu finden, gehe zu „Keys and Endpoint“ in deiner Azure OpenAI-Ressource und kopiere den Wert von „Key 1“.

![Schlüssel und Endpunkt Ressourcenseite im Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Jetzt, da du diese Informationen kopiert hast, lass uns die Bibliotheken anweisen, sie zu verwenden.

> [!NOTE]
> Es lohnt sich, deinen API-Schlüssel vom Code zu trennen. Das kannst du mit Umgebungsvariablen tun.
>
> - Setze die Umgebungsvariable `OPENAI_API_KEY` auf deinen API-Schlüssel.
>   `export OPENAI_API_KEY='sk-...'`

### Azure-Konfiguration einrichten

Wenn du Azure OpenAI (jetzt Teil von Microsoft Foundry) nutzt, so kannst du die Konfiguration einrichten. Wir verwenden den Standard-`OpenAI`-Client, der auf den Azure OpenAI-`/openai/v1/`-Endpunkt zeigt, welcher mit der Responses API arbeitet und keine `api_version` benötigt:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Oben stellen wir Folgendes ein:

- `api_key`, das ist dein API-Schlüssel, den du im Azure Portal oder im Microsoft Foundry-Portal findest.
- `base_url`, das ist dein Foundry-Ressourcenendpunkt mit `/openai/v1/` angehängt. Der stabile v1-Endpunkt funktioniert sowohl für OpenAI als auch für Azure OpenAI ohne `api_version`-Verwaltung.

> [!NOTE] > `os.environ` liest Umgebungsvariablen aus. Du kannst es verwenden, um Umgebungsvariablen wie `AZURE_OPENAI_API_KEY` und `AZURE_OPENAI_ENDPOINT` zu lesen. Setze diese Umgebungsvariablen in deinem Terminal oder verwende eine Bibliothek wie `dotenv`.

## Text generieren

Um Text zu generieren, nutzt man die Responses API über die `responses.create`-Methode. Hier ein Beispiel:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

Im obigen Code erstellen wir eine Antwort, geben das Modell und den Prompt an. Dann drucken wir den generierten Text über `response.output_text` aus.

### Mehrteilige Unterhaltungen

Die Responses API eignet sich sowohl für Einzelrunden-Textgenerierung als auch für mehrteilige Chatbots – du gibst eine Liste von Nachrichten in `input` an, um eine Unterhaltung aufzubauen:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Mehr zu dieser Funktionalität in einem kommenden Kapitel.

## Übung – deine erste Textgenerierungs-App

Nun, da wir gelernt haben, wie man openai einrichtet und konfiguriert, ist es Zeit, deine erste Textgenerierungs-App zu bauen. Folge diesen Schritten:

1. Erstelle eine virtuelle Umgebung und installiere openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Wenn du Windows verwendest, gib `venv\Scripts\activate` statt `source venv/bin/activate` ein.

   > [!NOTE]
   > Finde deinen Azure OpenAI Schlüssel, indem du zu [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) gehst, nach `Open AI` suchst, dann `Open AI resource` auswählst, anschließend `Keys and Endpoint` und den Wert von `Key 1` kopierst.

1. Erstelle eine Datei _app.py_ und füge diesen Code ein:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"

   # make a request using the Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # print response
   print(response.output_text)
   ```

   > [!NOTE]
   > Wenn du das „reine“ OpenAI (nicht Azure) nutzt, verwende `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (ohne `base_url`) und übergebe einen Modellnamen wie `gpt-5-mini` statt eines Deployment-Namens.

   Du solltest eine Ausgabe wie die folgende sehen:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Verschiedene Arten von Prompts für verschiedene Zwecke

Nun hast du gesehen, wie man mit einem Prompt Text generiert. Du hast sogar ein Programm am Laufen, das du anpassen und ändern kannst, um verschiedene Arten von Text zu erzeugen.

Prompts können für alle möglichen Aufgaben verwendet werden. Zum Beispiel:

- **Eine Art von Text generieren**. Du kannst beispielsweise ein Gedicht, Fragen für ein Quiz usw. generieren.
- **Informationen nachschlagen**. Du kannst Prompts verwenden, um nach Informationen zu suchen, zum Beispiel: „Was bedeutet CORS in der Webentwicklung?“.
- **Code generieren**. Du kannst Prompts verwenden, um Code zu erzeugen, z.B. eine reguläre Ausdruck zur Validierung von E-Mails entwickeln oder sogar ein komplettes Programm wie eine Web-App generieren.

## Ein praktischeres Beispiel: ein Rezeptgenerator

Stell dir vor, du hast Zutaten zu Hause und möchtest etwas kochen. Dafür brauchst du ein Rezept. Du könntest eine Suchmaschine verwenden oder einen LLM nutzen.

Du könntest so einen Prompt schreiben:

> „Zeige mir 5 Rezepte für ein Gericht mit den folgenden Zutaten: Huhn, Kartoffeln und Karotten. Liste pro Rezept alle verwendeten Zutaten auf.“

Aufgrund dieses Prompts könntest du eine Antwort wie diese erhalten:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 2 cloves garlic, minced
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
```

Dieses Ergebnis ist großartig, ich weiß, was ich kochen kann. Nützliche Verbesserungen könnten sein:

- Zutaten filtern, die ich nicht mag oder gegen die ich allergisch bin.
- Eine Einkaufsliste erstellen, falls ich nicht alle Zutaten zu Hause habe.

Für die obigen Fälle fügen wir einen zusätzlichen Prompt hinzu:

> „Bitte entferne Rezepte mit Knoblauch, da ich allergisch darauf reagiere, und ersetze ihn durch etwas anderes. Erstelle außerdem eine Einkaufsliste für die Rezepte, wobei ich bereits Huhn, Kartoffeln und Karotten zu Hause habe.“

Jetzt hast du ein neues Ergebnis, nämlich:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano

Shopping List:
- Olive oil
- Onion
- Thyme
- Oregano
- Salt
- Pepper
```

Das sind deine fünf Rezepte ohne Knoblauch und du hast auch eine Einkaufsliste, die berücksichtigt, was du bereits zu Hause hast.

## Übung – baue einen Rezeptgenerator

Nun, da wir ein Szenario durchgespielt haben, lass uns Code schreiben, der dem gezeigten Szenario entspricht. Folge diesen Schritten:

1. Verwende die bestehende Datei _app.py_ als Ausgangspunkt
1. Finde die Variable `prompt` und ändere deren Code wie folgt:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Wenn du jetzt den Code ausführst, solltest du ungefähr eine solche Ausgabe sehen:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > Hinweis: Dein LLM ist nichtdeterministisch, du kannst daher jedes Mal beim Ausführen des Programms unterschiedliche Ergebnisse erhalten.

   Toll, lass uns sehen, wie wir Dinge verbessern können. Dazu wollen wir sicherstellen, dass der Code flexibel ist, sodass Zutaten und die Anzahl der Rezepte angepasst werden können.

1. Ändere den Code wie folgt:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Zum Testen könnte der Code so aussehen:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Verbesserung durch Filter und Einkaufsliste

Wir haben jetzt eine funktionierende App, die Rezepte erstellen kann, und sie ist flexibel, da sie auf Eingaben des Benutzers reagiert – sowohl bei der Anzahl der Rezepte als auch den verwendeten Zutaten.

Um sie weiter zu verbessern, wollen wir folgendes hinzufügen:

- **Zutaten filtern**. Wir wollen Zutaten aussortieren können, die wir nicht mögen oder gegen die wir allergisch sind. Dazu bearbeiten wir unseren bestehenden Prompt und hängen eine Filterbedingung an das Ende an, wie folgt:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Oben fügen wir `{filter}` ans Ende des Prompts hinzu und erfassen auch den Filterwert vom Benutzer.

  Ein Beispielinput beim Ausführen des Programms könnte nun so aussehen:

  ```output
  No of recipes (for example, 5): 3
  List of ingredients (for example, chicken, potatoes, and carrots): onion,milk
  Filter (for example, vegetarian, vegan, or gluten-free): no milk

  1. French Onion Soup

  Ingredients:

  -1 large onion, sliced
  -3 cups beef broth
  -1 cup milk
  -6 slices french bread
  -1/4 cup shredded Parmesan cheese
  -1 tablespoon butter
  -1 teaspoon dried thyme
  -1/4 teaspoon salt
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add beef broth, milk, thyme, salt, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Place french bread slices on soup bowls.
  5. Ladle soup over bread.
  6. Sprinkle with Parmesan cheese.

  2. Onion and Potato Soup

  Ingredients:

  -1 large onion, chopped
  -2 cups potatoes, diced
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add potatoes, vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Serve hot.

  3. Creamy Onion Soup

  Ingredients:

  -1 large onion, chopped
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper
  -1/4 cup all-purpose flour
  -1/2 cup shredded Parmesan cheese

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. In a small bowl, whisk together flour and Parmesan cheese until smooth.
  5. Add to soup and simmer for an additional 5 minutes, or until soup has thickened.
  ```

  Wie du siehst, wurden Rezepte mit Milch herausgefiltert. Wenn du aber laktoseintolerant bist, möchtest du vielleicht auch Rezepte mit Käse filtern, daher ist Klarheit notwendig.

- **Eine Einkaufsliste erstellen**. Wir wollen eine Einkaufsliste erstellen, die berücksichtigt, was wir bereits zu Hause haben.

  Für diese Funktionalität könnten wir alles in einem Prompt lösen oder es in zwei Prompts aufteilen. Wir versuchen hier Letzteres. Dabei fügen wir das Ergebnis des ersten Prompts als Kontext dem zweiten Prompt hinzu.

  Finde die Stelle im Code, die das Ergebnis des ersten Prompts ausgibt, und füge den folgenden Code darunter ein:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Beachte Folgendes:

  1. Wir konstruieren einen neuen Prompt, indem wir das Ergebnis des ersten Prompts an den neuen Prompt anhängen:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Wir machen eine neue Anfrage und berücksichtigen dabei die Anzahl der Tokens, die wir im ersten Prompt erfragt haben, daher setzen wir diesmal `max_output_tokens` auf 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Wenn wir diesen Code ausführen, erhalten wir folgende Ausgabe:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Verbessere deine Einrichtung

Was wir bisher haben, ist funktionierender Code, aber es gibt einige Anpassungen, die wir vornehmen sollten, um die Dinge weiter zu verbessern. Einige Dinge, die wir tun sollten, sind:

- **Geheimnisse vom Code trennen**, wie den API-Schlüssel. Geheimnisse gehören nicht in den Code und sollten an einem sicheren Ort gespeichert werden. Um Geheimnisse vom Code zu trennen, können wir Umgebungsvariablen und Bibliotheken wie `python-dotenv` verwenden, um sie aus einer Datei zu laden. So würde das im Code aussehen:

  1. Erstellen Sie eine `.env`-Datei mit folgendem Inhalt:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Hinweis: Für Azure OpenAI in Microsoft Foundry müssen Sie stattdessen die folgenden Umgebungsvariablen setzen:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Im Code würden Sie die Umgebungsvariablen wie folgt laden:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Ein Wort zur Token-Länge**. Wir sollten bedenken, wie viele Tokens wir benötigen, um den gewünschten Text zu generieren. Tokens kosten Geld, daher sollten wir nach Möglichkeit sparsam mit der Anzahl der verwendeten Tokens umgehen. Zum Beispiel, können wir den Prompt so formulieren, dass wir weniger Tokens verwenden?

  Um die Anzahl der verwendeten Tokens zu ändern, können Sie den `max_output_tokens`-Parameter verwenden. Zum Beispiel, wenn Sie 100 Tokens verwenden möchten, machen Sie:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Experimentieren mit der Temperatur**. Temperatur ist etwas, das wir bisher nicht erwähnt haben, aber ein wichtiger Kontext dafür, wie unser Programm funktioniert. Je höher der Temperaturwert, desto zufälliger wird die Ausgabe. Umgekehrt gilt: Je niedriger der Temperaturwert, desto vorhersehbarer wird die Ausgabe. Überlegen Sie, ob Sie Variation in Ihrer Ausgabe wünschen oder nicht.

  Um die Temperatur zu ändern, können Sie den `temperature`-Parameter verwenden. Zum Beispiel, wenn Sie eine Temperatur von 0,5 verwenden wollen, machen Sie:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Hinweis: Je näher bei 1,0, desto vielfältiger die Ausgabe.

- **Reasoning-Modelle verwenden keine `temperature`**. Dies ist eine wichtige Veränderung für 2026. Die aktuellen, nicht veralteten Modelle in Microsoft Foundry sind **Reasoning-Modelle** (die GPT-5-Familie, o-Serie) – und sie **unterstützen keine `temperature` oder `top_p`** (ebenfalls nicht `max_tokens`; verwenden Sie stattdessen `max_output_tokens`). Wenn Sie `temperature` an `gpt-5-mini` senden, erhalten Sie einen Fehler „Parameter nicht unterstützt“. Um also das Temperatur-Beispiel oben zu testen, verwenden Sie ein Modell, das Sampling-Steuerungen noch unterstützt – beispielsweise ein offenes **Llama**-Modell wie `Llama-3.3-70B-Instruct` aus dem [Microsoft Foundry Modellkatalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), aufgerufen über den Foundry Models / Azure AI Inference-Endpunkt (genau wie die `githubmodels-*`-Beispiele). Bei Reasoning-Modellen wie GPT-5 steuern Sie die Ausgabe anders:
  - **Prompt Engineering** – klare Anweisungen, Beispiele und strukturierte Ausgabe (siehe Lektion [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) übernehmen die Arbeit, die früher Sampling-Regler erledigt haben.
  - **Reasoning-Steuerungen** – Parameter wie Reasoning-Einsatz/Verbosity balancieren die Tiefe des Reasonings gegen Latenz und Kosten ab.

  Kurz gesagt: `temperature`/`top_p` sind bei vielen Modellen (Llama, Mistral, Phi und der GPT-4.x-Familie – obwohl GPT-4.x ausläuft) weiterhin gültig, aber die Entwicklung geht in Richtung Prompt Engineering + Reasoning-Steuerungen bei Reasoning-Modellen wie GPT-5.

## Aufgabe

Für diese Aufgabe können Sie wählen, was Sie bauen möchten.

Hier einige Vorschläge:

- Verbessern Sie die Rezept-Generator-App weiter. Probieren Sie verschiedene Temperaturwerte und Prompts aus, um zu sehen, was Sie erstellen können.
- Erstellen Sie einen "Lernpartner". Diese App sollte in der Lage sein, Fragen zu einem Thema wie Python zu beantworten, z. B. könnten Prompts sein: „Was ist ein bestimmtes Thema in Python?“ oder „Zeige mir Beispiel-Code zu einem bestimmten Thema“ etc.
- Geschichts-Bot: Lassen Sie Geschichte lebendig werden, instruieren Sie den Bot, eine bestimmte historische Figur zu spielen, und stellen Sie ihm Fragen zu ihrem Leben und ihrer Zeit.

## Lösung

### Lernpartner

Nachfolgend finden Sie einen Starter-Prompt, sehen Sie, wie Sie ihn verwenden und nach Ihrem Geschmack anpassen können.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Geschichts-Bot

Hier sind einige Prompts, die Sie verwenden könnten:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Wissensüberprüfung

Was bewirkt das Konzept der Temperatur?

1. Es steuert, wie zufällig die Ausgabe ist.
1. Es steuert, wie groß die Antwort ist.
1. Es steuert, wie viele Tokens verwendet werden.

## 🚀 Herausforderung

Arbeiten Sie an der Aufgabe und variieren Sie dabei die Temperatur. Versuchen Sie 0, 0,5 und 1. Denken Sie daran, dass 0 am wenigsten variabel ist und 1 am stärksten. Welcher Wert funktioniert am besten für Ihre App?

## Großartige Arbeit! Lernen Sie weiter

Nach Abschluss dieser Lektion sehen Sie sich unsere [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um Ihr Wissen über Generative KI weiter zu vertiefen!

Gehen Sie zu Lektion 7, wo wir uns ansehen, wie man [Chat-Anwendungen baut](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->