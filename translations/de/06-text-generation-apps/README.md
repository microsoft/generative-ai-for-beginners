# Anwendungen zur Texterzeugung entwickeln

[![Anwendungen zur Texterzeugung entwickeln](../../../translated_images/de/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Klicken Sie auf das obige Bild, um das Video zu dieser Lektion anzusehen)_

Sie haben bisher in diesem Lehrplan gesehen, dass es Kernkonzepte wie Prompts gibt und sogar eine ganze Disziplin namens „Prompt Engineering“. Viele Tools, mit denen Sie interagieren können, wie ChatGPT, Office 365, Microsoft Power Platform und mehr, unterstützen Sie durch die Nutzung von Prompts, um etwas zu erreichen.

Um eine solche Erfahrung in eine App einzubauen, müssen Sie Konzepte wie Prompts, Completions verstehen und eine Bibliothek auswählen, mit der Sie arbeiten. Genau das werden Sie in diesem Kapitel lernen.

## Einführung

In diesem Kapitel werden Sie:

- Die openai-Bibliothek und ihre Kernkonzepte kennenlernen.
- Eine App zur Texterzeugung mit openai erstellen.
- Verstehen, wie Konzepte wie Prompt, Temperatur und Tokens genutzt werden, um eine Textgenerierungs-App zu bauen.

## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:

- Zu erklären, was eine Anwendung zur Texterzeugung ist.
- Eine Anwendung zur Texterzeugung mit openai zu erstellen.
- Ihre Anwendung so zu konfigurieren, dass mehr oder weniger Tokens verwendet werden und auch die Temperatur für variierte Ausgaben zu ändern.

## Was ist eine Anwendung zur Texterzeugung?

Normalerweise hat eine App eine Art von Benutzeroberfläche, wie zum Beispiel:

- Kommando-basiert. Konsolenanwendungen sind typische Apps, bei denen Sie einen Befehl eingeben und dieser eine Aufgabe ausführt. Zum Beispiel ist `git` eine kommando-basierte App.
- Benutzeroberfläche (UI). Manche Apps haben grafische Benutzeroberflächen (GUIs), bei denen Sie auf Schaltflächen klicken, Text eingeben, Optionen auswählen und mehr.

### Konsolen- und UI-Anwendungen sind begrenzt

Vergleichen Sie das mit einer Kommando-basierten App, in der Sie einen Befehl eingeben:

- **Sie ist begrenzt**. Sie können nicht beliebige Befehle eingeben, sondern nur die, die die App unterstützt.
- **Sprachspezifisch**. Einige Apps unterstützen viele Sprachen, aber standardmäßig ist die App für eine bestimmte Sprache gebaut, auch wenn Sie weitere Sprachunterstützung hinzufügen können.

### Vorteile von Textgenerierungs-Apps

Wie unterscheidet sich nun eine Texterzeugungs-App?

In einer Texterzeugungs-App haben Sie mehr Flexibilität, Sie sind nicht auf eine feste Menge an Befehlen oder eine bestimmte Eingabesprache beschränkt. Stattdessen können Sie natürliche Sprache verwenden, um mit der App zu interagieren. Ein weiterer Vorteil ist, dass Sie mit einer Datenquelle interagieren, die mit einem riesigen Informationskorpus trainiert wurde, während eine traditionelle App möglicherweise nur auf eine begrenzte Datenbank zugreifen kann.

### Was kann ich mit einer Texterzeugungs-App bauen?

Es gibt viele Möglichkeiten. Zum Beispiel:

- **Ein Chatbot**. Ein Chatbot, der Fragen zu Themen wie Ihrem Unternehmen und seinen Produkten beantwortet, kann sehr nützlich sein.
- **Assistent**. LLMs sind hervorragend geeignet, um Texte zusammenzufassen, Erkenntnisse aus Text zu gewinnen, Texte wie Lebensläufe zu erstellen und mehr.
- **Code-Assistent**. Abhängig vom verwendeten Sprachmodell können Sie einen Code-Assistenten entwickeln, der Ihnen beim Schreiben von Code hilft. Beispielsweise können Sie Produkte wie GitHub Copilot sowie ChatGPT nutzen, um Code zu schreiben.

## Wie fange ich an?

Sie müssen einen Weg finden, sich mit einem LLM zu integrieren, was üblicherweise die folgenden zwei Ansätze bedeutet:

- Eine API verwenden. Dabei bauen Sie Web-Anfragen mit Ihrem Prompt und erhalten generierten Text zurück.
- Eine Bibliothek verwenden. Bibliotheken helfen dabei, die API-Aufrufe zu kapseln und einfacher nutzbar zu machen.

## Bibliotheken/SDKs

Es gibt einige bekannte Bibliotheken für die Arbeit mit LLMs, wie:

- **openai**, diese Bibliothek erleichtert den Anschluss an Ihr Modell und das Senden von Prompts.

Dann gibt es Bibliotheken, die auf einer höheren Ebene agieren, wie:

- **Langchain**. Langchain ist bekannt und unterstützt Python.
- **Semantic Kernel**. Semantic Kernel ist eine Bibliothek von Microsoft, die die Sprachen C#, Python und Java unterstützt.

## Erste App mit openai

Sehen wir uns an, wie wir unsere erste App bauen können, welche Bibliotheken wir brauchen, wie viel Aufwand notwendig ist und so weiter.

### openai installieren

Es gibt viele Bibliotheken für die Interaktion mit OpenAI oder Azure OpenAI. Es ist auch möglich, zahlreiche Programmiersprachen zu nutzen wie C#, Python, JavaScript, Java und mehr. Wir haben uns entschieden, die `openai` Python-Bibliothek zu verwenden, daher installieren wir sie mit `pip`.

```bash
pip install openai
```

### Erstellen einer Ressource

Sie müssen die folgenden Schritte ausführen:

- Erstellen Sie ein Konto bei Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Erhalten Sie Zugang zu Azure OpenAI. Gehen Sie zu [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) und beantragen Sie Zugriff.

  > [!NOTE]
  > Zum Zeitpunkt des Schreibens müssen Sie Zugriff auf Azure OpenAI beantragen.

- Installieren Sie Python <https://www.python.org/>
- Erstellen Sie eine Azure OpenAI Service Ressource. Eine Anleitung zum [Erstellen einer Ressource](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst) finden Sie dort.

### API-Schlüssel und Endpunkt finden

An diesem Punkt müssen Sie der `openai`-Bibliothek mitteilen, welchen API-Schlüssel sie verwenden soll. Um Ihren API-Schlüssel zu finden, gehen Sie zum Abschnitt „Keys and Endpoint“ Ihrer Azure OpenAI-Ressource und kopieren Sie den Wert von „Key 1“.

![Keys and Endpoint resource blade im Azure-Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Nun, da Sie diese Informationen kopiert haben, sagen wir den Bibliotheken, sie sollen diese verwenden.

> [!NOTE]
> Es ist sinnvoll, Ihren API-Schlüssel vom Code zu trennen. Sie können dies über Umgebungsvariablen tun.
>
> - Setzen Sie die Umgebungsvariable `OPENAI_API_KEY` auf Ihren API-Schlüssel.
>   `export OPENAI_API_KEY='sk-...'`

### Konfiguration für Azure einrichten

Wenn Sie Azure OpenAI verwenden (jetzt Teil von Microsoft Foundry), so richten Sie die Konfiguration ein. Wir verwenden den Standard-`OpenAI`-Client, der auf den Azure OpenAI `/openai/v1/` Endpunkt zeigt, der mit der Responses-API arbeitet und keine `api_version` benötigt:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Oben setzen wir Folgendes:

- `api_key`, das ist Ihr API-Schlüssel, den Sie im Azure-Portal oder Microsoft Foundry-Portal finden.
- `base_url`, das ist Ihre Foundry-Ressourcen-URL mit `/openai/v1/` angehängt. Der stabile v1-Endpunkt funktioniert sowohl für OpenAI als auch Azure OpenAI ohne `api_version`-Verwaltung.

> [!NOTE] > `os.environ` liest Umgebungsvariablen aus. Sie können damit Variablen wie `AZURE_OPENAI_API_KEY` und `AZURE_OPENAI_ENDPOINT` auslesen. Setzen Sie diese Umgebungsvariablen in Ihrem Terminal oder nutzen Sie eine Bibliothek wie `dotenv`.

## Text generieren

Text zu generieren erfolgt über die Responses-API mit der Methode `responses.create`. Hier ein Beispiel:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # Dies ist Ihr Modell-Bereitstellungsname
    input=prompt,
    store=False,
)
print(response.output_text)
```

Im obigen Code erzeugen wir eine Antwort und übergeben das Modell, das wir verwenden möchten, und den Prompt. Dann geben wir den generierten Text via `response.output_text` aus.

### Mehrstufige Konversationen

Die Responses-API eignet sich sowohl für einstufige Textgenerierung als auch für mehrstufige Chatbots – Sie übergeben eine Liste von Nachrichten in `input`, um eine Konversation aufzubauen:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Mehr zu dieser Funktionalität in einem kommenden Kapitel.

## Übung – Ihre erste Anwendung zur Texterzeugung

Jetzt, wo wir gelernt haben, wie openai eingerichtet und konfiguriert wird, ist es Zeit, Ihre erste Anwendung zur Texterzeugung zu bauen. Folgen Sie diesen Schritten:

1. Erstellen Sie eine virtuelle Umgebung und installieren Sie openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Wenn Sie Windows verwenden, geben Sie `venv\Scripts\activate` statt `source venv/bin/activate` ein.

   > [!NOTE]
   > Finden Sie Ihren Azure OpenAI-Schlüssel, indem Sie zu [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) gehen, nach `Open AI` suchen, die `Open AI-Ressource` auswählen, dann `Keys and Endpoint` wählen und den Wert von `Key 1` kopieren.

1. Erstellen Sie eine _app.py_-Datei und geben Sie ihr folgenden Code:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # füge deinen Abschlusscode hinzu
   prompt = "Complete the following: Once upon a time there was a"

   # mache eine Anfrage mit der Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # gib die Antwort aus
   print(response.output_text)
   ```

   > [!NOTE]
   > Wenn Sie OpenAI (nicht Azure) verwenden, nutzen Sie `client = OpenAI(api_key="<ersetzen Sie diesen Wert durch Ihren OpenAI-Schlüssel>")` (kein `base_url`) und geben Sie einen Modellnamen wie `gpt-5-mini` statt eines Bereitstellungsnamens an.

   Sie sollten eine Ausgabe wie die folgende sehen:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Verschiedene Arten von Prompts für unterschiedliche Aufgaben

Jetzt haben Sie gesehen, wie man mit einem Prompt Text generiert. Sie haben sogar ein laufendes Programm, das Sie ändern und anpassen können, um verschiedene Arten von Text zu generieren.

Prompts können für alle möglichen Aufgaben verwendet werden. Zum Beispiel:

- **Einen Texttyp generieren**. Beispielsweise können Sie ein Gedicht, Fragen für ein Quiz usw. generieren.
- **Informationen nachschlagen**. Sie können Prompts verwenden, um Informationen zu suchen, wie im Beispiel „Was bedeutet CORS in der Webentwicklung?“.
- **Code generieren**. Sie können Prompts verwenden, um Code zu generieren, beispielsweise einen regulären Ausdruck zum Überprüfen von E-Mails zu entwickeln oder gar ein ganzes Programm wie eine Webanwendung zu erzeugen.

## Ein praktischer Anwendungsfall: Ein Rezeptgenerator

Stellen Sie sich vor, Sie haben Zutaten zu Hause und möchten etwas kochen. Dafür brauchen Sie ein Rezept. Eine Möglichkeit, Rezepte zu finden, ist eine Suchmaschine zu benutzen oder ein LLM, das das für Sie erledigt.

Sie könnten einen Prompt wie diesen schreiben:

> "Zeige mir 5 Rezepte für ein Gericht mit den folgenden Zutaten: Huhn, Kartoffeln und Karotten. Pro Rezept alle verwendeten Zutaten auflisten."

Basierend auf dem obigen Prompt erhalten Sie vielleicht eine Antwort ähnlich der folgenden:

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

Dieses Ergebnis ist großartig, ich weiß, was ich kochen kann. An diesem Punkt wären nützliche Verbesserungen:

- Zutaten herausfiltern, die ich nicht mag oder auf die ich allergisch reagiere.
- Eine Einkaufsliste erstellen, falls ich nicht alle Zutaten zu Hause habe.

Für die oben genannten Fälle fügen wir einen weiteren Prompt hinzu:

> "Bitte entferne Rezepte mit Knoblauch, da ich allergisch bin, und ersetze ihn durch etwas anderes. Erstelle außerdem eine Einkaufsliste für die Rezepte, wobei berücksichtigt wird, dass ich Huhn, Kartoffeln und Karotten zu Hause habe."

Jetzt haben Sie ein neues Ergebnis, nämlich:

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

Das sind Ihre fünf Rezepte, ohne Knoblauch und Sie haben auch eine Einkaufsliste unter Berücksichtigung dessen, was Sie bereits zu Hause haben.

## Übung – einen Rezeptgenerator bauen

Nun, da wir ein Szenario durchgespielt haben, schreiben wir passenden Code dazu. Gehen Sie dabei wie folgt vor:

1. Verwenden Sie die bestehende _app.py_-Datei als Ausgangspunkt.
1. Finden Sie die Variable `prompt` und ändern Sie deren Code wie folgt:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Wenn Sie jetzt das Programm ausführen, sollten Sie eine Ausgabe ähnlich der folgenden sehen:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > HINWEIS: Ihr LLM arbeitet nicht deterministisch, daher können Sie bei jedem Ausführen des Programms unterschiedliche Ergebnisse erhalten.

   Großartig, schauen wir uns an, wie wir die Dinge verbessern können. Wir wollen sicherstellen, dass der Code flexibel ist, damit Zutaten und Anzahl der Rezepte angepasst werden können.

1. Ändern wir den Code folgendermaßen:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolieren Sie die Anzahl der Rezepte in die Aufforderung und Zutaten
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Ein Testlauf des Codes könnte so aussehen:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Verbesserung durch Filtern und Einkaufsliste hinzufügen

Wir haben jetzt eine funktionierende App, die Rezepte erstellen kann und flexibel ist, da sie auf Benutzereingaben beruht, sowohl hinsichtlich der Anzahl der Rezepte als auch der verwendeten Zutaten.

Um das weiter zu verbessern, möchten wir Folgendes hinzufügen:

- **Zutaten filtern**. Wir wollen Zutaten herausfiltern können, die wir nicht mögen oder auf die wir allergisch reagieren. Um diese Änderung zu ermöglichen, können wir unseren bestehenden Prompt bearbeiten und eine Filterbedingung am Ende hinzufügen, so:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Oben fügen wir `{filter}` an das Ende des Prompts hinzu und erfassen auch den Filterwert vom Benutzer.

  Ein Beispiel für eine Eingabe beim Ausführen des Programms könnte jetzt so aussehen:

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

  Wie Sie sehen, wurden Rezepte mit Milch herausgefiltert. Aber wenn Sie laktoseintolerant sind, möchten Sie vielleicht auch Rezepte mit Käse ausschließen – daher muss hier Klarheit herrschen.


- **Erstelle eine Einkaufsliste**. Wir wollen eine Einkaufsliste erstellen, unter Berücksichtigung dessen, was wir bereits zu Hause haben.

  Für diese Funktionalität könnten wir entweder versuchen, alles in einem Prompt zu lösen, oder wir könnten es in zwei Prompts aufteilen. Versuchen wir den letzteren Ansatz. Hier schlagen wir vor, einen zusätzlichen Prompt hinzuzufügen, aber damit das funktioniert, müssen wir das Ergebnis des ersten Prompts als Kontext für den zweiten Prompt hinzufügen.

  Finde die Stelle im Code, die das Ergebnis des ersten Prompts ausgibt, und füge den folgenden Code darunter hinzu:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # Antwort drucken
  print("Shopping list:")
  print(response.output_text)
  ```

  Beachte Folgendes:

  1. Wir konstruieren einen neuen Prompt, indem wir das Ergebnis des ersten Prompts zum neuen Prompt hinzufügen:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Wir machen eine neue Anfrage, berücksichtigen dabei aber auch die Anzahl der Tokens, die wir im ersten Prompt angefordert haben, sodass wir diesmal `max_output_tokens` auf 1200 setzen.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Wenn wir diesen Code ausführen, kommen wir nun zu folgender Ausgabe:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Verbessere dein Setup

Was wir bisher haben, ist Code, der funktioniert, aber es gibt einige Anpassungen, die wir vornehmen sollten, um alles weiter zu verbessern. Einige Dinge, die wir tun sollten, sind:

- **Trenne Geheimnisse vom Code**, wie zum Beispiel den API-Schlüssel. Geheimnisse gehören nicht in den Code und sollten an einem sicheren Ort aufbewahrt werden. Um Geheimnisse vom Code zu trennen, können wir Umgebungsvariablen verwenden und Bibliotheken wie `python-dotenv`, um sie aus einer Datei zu laden. So sieht das im Code aus:

  1. Erstelle eine `.env`-Datei mit folgendem Inhalt:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Hinweis: Für Azure OpenAI in Microsoft Foundry musst du stattdessen folgende Umgebungsvariablen setzen:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Im Code würdest du die Umgebungsvariablen so laden:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Ein Wort zur Token-Länge**. Wir sollten berücksichtigen, wie viele Tokens wir für die Generierung des gewünschten Textes benötigen. Tokens kosten Geld, daher sollten wir möglichst sparsam mit der Anzahl der verwendeten Tokens umgehen. Zum Beispiel, können wir den Prompt so formulieren, dass wir weniger Tokens verwenden?

  Um die verwendeten Tokens zu ändern, kannst du den Parameter `max_output_tokens` verwenden. Wenn du z.B. 100 Tokens verwenden möchtest, würdest du so vorgehen:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Experimentiere mit der Temperatur**. Die Temperatur ist etwas, das wir bisher noch nicht erwähnt haben, aber es ist ein wichtiger Kontext für die Leistung unseres Programms. Je höher der Temperaturwert, desto zufälliger ist die Ausgabe. Je niedriger der Temperaturwert, desto vorhersehbarer ist die Ausgabe. Überlege, ob du Variation in deiner Ausgabe möchtest oder nicht.

  Um die Temperatur zu ändern, kannst du den Parameter `temperature` verwenden. Wenn du z.B. eine Temperatur von 0,5 verwenden möchtest, würdest du so vorgehen:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Hinweis: Je näher an 1,0, desto abwechslungsreicher die Ausgabe.

- **Reasoning-Modelle verwenden keine `temperature`**. Das ist eine wichtige Änderung im Jahr 2026. Die aktuellen, nicht veralteten Modelle auf Microsoft Foundry sind **Reasoning-Modelle** (die GPT-5 Familie, o-Serie) – und sie **unterstützen `temperature` oder `top_p` nicht** (ebenfalls nicht `max_tokens`; benutze `max_output_tokens`). Wenn du `temperature` an `gpt-5-mini` schickst, bekommst du einen "Parameter nicht unterstützt"-Fehler. Um also das Temperature-Beispiel oben zu testen, verwende ein Modell, das Sampling-Kontrollen noch unterstützt – zum Beispiel ein offenes **Llama**-Modell wie `Llama-3.3-70B-Instruct` aus dem [Microsoft Foundry Modellkatalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), aufgerufen über den Foundry Models / Azure AI Inference Endpunkt (wie bei den `githubmodels-*` Beispielen). Für Reasoning-Modelle wie GPT-5 steuerst du die Ausgabe anders:
  - **Prompt Engineering** – klare Anweisungen, Beispiele und strukturierte Ausgabe (siehe Lektion [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) erledigen die Arbeit, die Sampling-Regler früher gemacht haben.
  - **Reasoning-Kontrollen** – Parameter wie reasoning effort/verbosity handeln eine Balance zwischen Tiefe der Überlegung und Latenz & Kosten aus.

  Kurz gesagt: `temperature`/`top_p` sind noch bei vielen Modellen gültig (Llama, Mistral, Phi und die GPT-4.x Familie – wobei GPT-4.x ausläuft), aber der Trend geht zu Prompt Engineering + Reasoning-Kontrollen bei Reasoning-Modellen wie GPT-5.

## Aufgabe

Für diese Aufgabe kannst du selbst entscheiden, was du bauen möchtest.

Hier ein paar Vorschläge:

- Verfeinere die Rezeptgenerator-App, um sie noch besser zu machen. Experimentiere mit Temperaturwerten und den Prompts, um zu sehen, was du erreichen kannst.
- Baue einen "Study Buddy". Diese App sollte in der Lage sein, Fragen zu einem Thema zu beantworten, z.B. Python. Du könntest Prompts verwenden wie "Was ist ein bestimmtes Thema in Python?" oder du könntest einen Prompt haben, der sagt, zeig mir Code zu einem bestimmten Thema, usw.
- Geschichts-Bot, erwecke Geschichte zum Leben, instruierte den Bot, eine bestimmte historische Figur darzustellen und stelle ihm Fragen zu ihrem Leben und ihrer Zeit.

## Lösung

### Study Buddy

Unten findest du einen Start-Prompt, sieh dir an, wie du ihn nutzen und nach Belieben anpassen kannst.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Geschichts-Bot

Hier sind einige Prompts, die du verwenden könntest:

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

Wenn du an der Aufgabe arbeitest, versuche die Temperatur zu variieren, setze sie auf 0, 0,5 und 1. Denke daran, dass 0 die geringste Variation und 1 die größte Variation bedeutet. Welcher Wert funktioniert am besten für deine App?

## Großartige Arbeit! Setze dein Lernen fort

Nachdem du diese Lektion abgeschlossen hast, schau dir unsere [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um dein Wissen über Generative KI weiter zu vertiefen!

Gehe zu Lektion 7, wo wir uns ansehen, wie man [Chat-Anwendungen baut](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->