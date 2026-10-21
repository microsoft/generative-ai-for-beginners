# Entwicklung von Textgenerierungsanwendungen

[![Entwicklung von Textgenerierungsanwendungen](../../../translated_images/de/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Klicken Sie auf das obige Bild, um das Video zu dieser Lektion anzusehen)_

Sie haben bisher in diesem Lehrplan gesehen, dass es Kernkonzepte wie Prompts gibt und sogar eine ganze Disziplin namens "Prompt Engineering". Viele Tools, mit denen Sie interagieren können, wie ChatGPT, Office 365, Microsoft Power Platform und mehr, unterstützen Sie dabei, durch Eingabeaufforderungen etwas zu erledigen.

Um eine solche Erfahrung in eine App zu integrieren, müssen Sie Konzepte wie Prompts und Completions verstehen und eine Bibliothek auswählen, mit der Sie arbeiten möchten. Genau das werden Sie in diesem Kapitel lernen.

## Einführung

In diesem Kapitel werden Sie:

- Die openai-Bibliothek und ihre Kernkonzepte kennenlernen.
- Eine Textgenerierungs-App mit openai bauen.
- Verstehen, wie man Konzepte wie Prompt, Temperatur und Tokens verwendet, um eine Textgenerierungs-App zu erstellen.

## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:

- Erklären, was eine Textgenerierungs-App ist.
- Eine Textgenerierungs-App mit openai zu bauen.
- Ihre App so zu konfigurieren, dass mehr oder weniger Tokens verwendet werden und auch die Temperatur anzupassen, um variierte Ausgaben zu erzielen.

## Was ist eine Textgenerierungs-App?

Normalerweise hat eine App eine Art Benutzeroberfläche wie die folgende:

- Befehlsbasiert. Konsolenanwendungen sind typische Apps, bei denen Sie einen Befehl eingeben und eine Aufgabe ausgeführt wird. Zum Beispiel ist `git` eine befehlsbasierte App.
- Benutzeroberfläche (UI). Einige Apps haben grafische Benutzeroberflächen (GUIs), bei denen Sie auf Schaltflächen klicken, Text eingeben, Optionen auswählen und mehr.

### Konsolen- und UI-Apps sind eingeschränkt

Vergleichen Sie es mit einer befehlsbasierten App, bei der Sie einen Befehl eingeben:

- **Sie ist eingeschränkt**. Sie können nicht einfach einen beliebigen Befehl eingeben, sondern nur diejenigen, die die App unterstützt.
- **Sprachspezifisch**. Einige Apps unterstützen viele Sprachen, aber standardmäßig ist die App für eine bestimmte Sprache gebaut, auch wenn man Unterstützung für weitere Sprachen hinzufügen kann.

### Vorteile von Textgenerierungs-Apps

Wie unterscheidet sich also eine Textgenerierungs-App?

In einer Textgenerierungs-App haben Sie mehr Flexibilität, Sie sind nicht auf eine festgelegte Menge an Befehlen oder eine bestimmte Eingabesprache beschränkt. Stattdessen können Sie natürliche Sprache verwenden, um mit der App zu interagieren. Ein weiterer Vorteil ist, dass Sie bereits mit einer Datenquelle interagieren, die auf einem riesigen Informationskorpus trainiert wurde, während eine traditionelle App möglicherweise nur auf eine Datenbank beschränkt ist.

### Was kann ich mit einer Textgenerierungs-App bauen?

Sie können viele Dinge bauen. Zum Beispiel:

- **Einen Chatbot**. Ein Chatbot, der Fragen zu Themen wie Ihrem Unternehmen und dessen Produkten beantwortet, könnte eine gute Lösung sein.
- **Assistenten**. LLMs sind großartig bei Dingen wie Textzusammenfassungen, Textanalysen, Erstellung von Texten wie Lebensläufen und mehr.
- **Code-Assistenten**. Abhängig vom verwendeten Sprachmodell können Sie einen Code-Assistenten bauen, der beim Schreiben von Code hilft. Zum Beispiel können Sie Produkte wie GitHub Copilot sowie ChatGPT verwenden, um Code zu schreiben.

## Wie kann ich anfangen?

Nun, Sie müssen einen Weg finden, sich mit einem LLM zu integrieren, was in der Regel die folgenden zwei Ansätze umfasst:

- Verwenden einer API. Hier konstruieren Sie Webanfragen mit Ihrem Prompt und erhalten den generierten Text zurück.
- Verwenden einer Bibliothek. Bibliotheken helfen dabei, API-Aufrufe zu kapseln und die Verwendung zu vereinfachen.

## Bibliotheken/SDKs

Es gibt einige bekannte Bibliotheken für die Arbeit mit LLMs wie:

- **openai**, diese Bibliothek erleichtert die Verbindung mit Ihrem Modell und das Senden von Prompts.

Dann gibt es Bibliotheken, die auf einer höheren Ebene arbeiten, wie:

- **Langchain**. Langchain ist bekannt und unterstützt Python.
- **Semantic Kernel**. Semantic Kernel ist eine Bibliothek von Microsoft, die die Sprachen C#, Python und Java unterstützt.

## Erste App mit openai

Schauen wir uns an, wie wir unsere erste App bauen können, welche Bibliotheken wir benötigen, wie viel erforderlich ist und so weiter.

### openai installieren

Es gibt viele Bibliotheken, um mit OpenAI oder Azure OpenAI zu interagieren. Es ist möglich, viele Programmiersprachen zu verwenden, wie C#, Python, JavaScript, Java und mehr. Wir haben uns entschieden, die Python-Bibliothek `openai` zu verwenden, also werden wir `pip` nutzen, um sie zu installieren.

```bash
pip install openai
```

### Erstellen einer Ressource

Sie müssen die folgenden Schritte durchführen:

- Erstellen Sie ein Konto auf Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Erhalten Sie Zugang zu Azure OpenAI. Gehen Sie zu [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) und beantragen Sie Zugang.

  > [!NOTE]
  > Zum Zeitpunkt des Schreibens müssen Sie den Zugang zu Azure OpenAI beantragen.

- Installieren Sie Python <https://www.python.org/>
- Haben Sie eine Azure OpenAI Service-Ressource erstellt. Sehen Sie diesen Leitfaden, wie Sie eine [Ressource erstellen](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### API-Schlüssel und Endpunkt finden

An diesem Punkt müssen Sie Ihrer `openai`-Bibliothek mitteilen, welchen API-Schlüssel sie verwenden soll. Um Ihren API-Schlüssel zu finden, gehen Sie zum Abschnitt "Schlüssel und Endpunkt" Ihrer Azure OpenAI-Ressource und kopieren Sie den Wert von "Schlüssel 1".

![Schlüssel- und Endpunkt-Ressourcenseite im Azure-Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Nun, da Sie diese Information kopiert haben, lassen Sie uns den Bibliotheken anweisen, sie zu verwenden.

> [!NOTE]
> Es lohnt sich, Ihren API-Schlüssel vom Code zu trennen. Das können Sie mit Umgebungsvariablen tun.
>
> - Setzen Sie die Umgebungsvariable `OPENAI_API_KEY` auf Ihren API-Schlüssel.
>   `export OPENAI_API_KEY='sk-...'`

### Azure-Konfiguration einrichten

Wenn Sie Azure OpenAI verwenden (jetzt Teil von Microsoft Foundry), so richten Sie die Konfiguration ein. Wir verwenden den Standard-`OpenAI`-Client, der auf den Azure OpenAI `/openai/v1/` Endpunkt zeigt, welcher mit der Responses API funktioniert und keine `api_version` benötigt:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Oben setzen wir Folgendes:

- `api_key`, dies ist Ihr API-Schlüssel, den Sie im Azure-Portal oder im Microsoft Foundry Portal finden.
- `base_url`, dies ist Ihr Foundry-Ressourcenendpunkt mit angehängtem `/openai/v1/`. Der stabile v1-Endpunkt funktioniert sowohl für OpenAI als auch Azure OpenAI ohne `api_version`-Verwaltung.

> [!NOTE] > `os.environ` liest Umgebungsvariablen. Sie können es verwenden, um Umgebungsvariablen wie `AZURE_OPENAI_API_KEY` und `AZURE_OPENAI_ENDPOINT` zu lesen. Setzen Sie diese Umgebungsvariablen in Ihrem Terminal oder indem Sie eine Bibliothek wie `dotenv` verwenden.

## Text generieren

Die Art und Weise, Text zu generieren, ist die Verwendung der Responses API über die `responses.create`-Methode. Hier ein Beispiel:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

Im obigen Code erstellen wir eine Antwort und übergeben das Modell, das wir verwenden möchten, und das Prompt. Dann geben wir den generierten Text über `response.output_text` aus.

### Mehrstufige Konversationen

Die Responses API ist sowohl für textgenerierende Einzelschritte als auch mehrstufige Chatbots geeignet – Sie übergeben eine Liste von Nachrichten in `input`, um eine Konversation aufzubauen:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Mehr zu dieser Funktionalität in einem kommenden Kapitel.

## Übung – Ihre erste Textgenerierungs-App

Jetzt, wo wir gelernt haben, wie openai einzurichten und zu konfigurieren ist, ist es Zeit, Ihre erste Textgenerierungs-App zu bauen. Folgen Sie dazu diesen Schritten:

1. Erstellen Sie eine virtuelle Umgebung und installieren Sie openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Wenn Sie Windows verwenden, geben Sie `venv\Scripts\activate` anstelle von `source venv/bin/activate` ein.

   > [!NOTE]
   > Finden Sie Ihren Azure OpenAI-Schlüssel, indem Sie zu [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) gehen, nach `Open AI` suchen, dann `Open AI resource` auswählen und anschließend `Keys and Endpoint` auswählen und den Wert von `Key 1` kopieren.

1. Erstellen Sie eine Datei _app.py_ und geben Sie ihr folgenden Code:

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
   > Wenn Sie OpenAI (nicht Azure) verwenden, nutzen Sie `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (kein `base_url`) und übergeben Sie einen Modellnamen wie `gpt-5-mini` anstelle eines Bereitstellungsnamens.

   Sie sollten eine Ausgabe wie die folgende sehen:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Verschiedene Arten von Prompts, für verschiedene Dinge

Nun haben Sie gesehen, wie Text mit einem Prompt generiert wird. Sie haben sogar ein Programm laufen, das Sie ändern und anpassen können, um verschiedene Arten von Texten zu erzeugen.

Prompts können für alle möglichen Aufgaben verwendet werden. Zum Beispiel:

- **Einen Texttyp generieren**. Zum Beispiel können Sie ein Gedicht, Fragen für ein Quiz usw. generieren.
- **Informationen nachschlagen**. Sie können Prompts verwenden, um Informationen zu suchen, wie zum Beispiel im Beispiel 'Was bedeutet CORS in der Webentwicklung?'.
- **Code generieren**. Sie können Prompts verwenden, um Code zu generieren, z. B. eine reguläre Expression für die E-Mail-Validierung oder sogar ein ganzes Programm wie eine Web-App generieren.

## Ein praxisnaher Anwendungsfall: ein Rezeptgenerator

Stellen Sie sich vor, Sie haben Zutaten zu Hause und möchten etwas kochen. Dazu benötigen Sie ein Rezept. Ein Weg, um Rezepte zu finden, ist eine Suchmaschine oder Sie nutzen ein LLM dafür.

Sie könnten einen Prompt folgendermaßen schreiben:

> "Zeige mir 5 Rezepte für ein Gericht mit den folgenden Zutaten: Huhn, Kartoffeln und Karotten. Für jedes Rezept liste alle verwendeten Zutaten auf."

Bei dem obigen Prompt könnten Sie eine Antwort wie folgt erhalten:

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

Dieses Ergebnis ist großartig, ich weiß, was ich kochen kann. Nun könnten nützliche Verbesserungen sein:

- Filtern von Zutaten, die ich nicht mag oder auf die ich allergisch reagiere.
- Eine Einkaufsliste erstellen, falls ich nicht alle Zutaten zu Hause habe.

Für die obigen Fälle wollen wir einen zusätzlichen Prompt hinzufügen:

> "Bitte entferne Rezepte mit Knoblauch, da ich allergisch darauf reagiere, und ersetze sie durch etwas anderes. Außerdem stelle bitte eine Einkaufsliste für die Rezepte zusammen, da ich bereits Huhn, Kartoffeln und Karotten zu Hause habe."

Jetzt erhalten Sie ein neues Ergebnis, nämlich:

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

Das sind Ihre fünf Rezepte, ohne Erwähnung von Knoblauch und Sie haben auch eine Einkaufsliste unter Berücksichtigung der Zutaten, die Sie bereits zu Hause haben.

## Übung – bauen Sie einen Rezeptgenerator

Jetzt, wo wir ein Szenario gespielt haben, schreiben wir Code, der dem dargestellten Szenario entspricht. Gehen Sie dazu wie folgt vor:

1. Verwenden Sie die existierende Datei _app.py_ als Ausgangspunkt.
1. Suchen Sie die Variable `prompt` und ändern Sie ihren Code wie folgt:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Wenn Sie den Code jetzt ausführen, sollten Sie eine Ausgabe ähnlich der folgenden sehen:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > HINWEIS: Ihr LLM ist nicht deterministisch, Sie könnten bei jedem Ausführen unterschiedliche Ergebnisse erhalten.

   Großartig, sehen wir uns an, wie wir Dinge verbessern können. Dazu wollen wir sicherstellen, dass der Code flexibel ist, sodass Zutaten und Anzahl der Rezepte verbessert und geändert werden können.

1. Ändern wir den Code folgendermaßen:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Einen Testlauf des Codes könnte so aussehen:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Verbesserung durch Filter und Einkaufsliste

Wir haben nun eine funktionierende App, die Rezepte erzeugen kann, und sie ist flexibel, da sie sich auf Eingaben des Nutzers stützt, sowohl hinsichtlich der Anzahl der Rezepte als auch der verwendeten Zutaten.

Um sie weiter zu verbessern, wollen wir Folgendes hinzufügen:

- **Zutaten herausfiltern**. Wir möchten Zutaten herausfiltern können, die wir nicht mögen oder auf die wir allergisch sind. Dazu können wir unseren bestehenden Prompt bearbeiten und am Ende des Prompts eine Filterbedingung hinzufügen, etwa so:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Oben fügen wir `{filter}` ans Ende des Prompts an und erfassen auch den Filterwert vom Nutzer.

  Ein Beispiel für eine Eingabe beim Ausführen des Programms kann nun so aussehen:

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

  Wie Sie sehen können, wurden Rezepte mit Milch herausgefiltert. Wenn Sie laktoseintolerant sind, möchten Sie vielleicht auch Rezepte mit Käse herausfiltern, daher muss die Filterung klar sein.

- **Eine Einkaufsliste erstellen**. Wir wollen eine Einkaufsliste erstellen, die berücksichtigt, was wir bereits zu Hause haben.

  Für diese Funktionalität könnten wir entweder alles in einem Prompt lösen oder wir splitten es in zwei Prompts auf. Versuchen wir Letzteres. Hier schlagen wir vor, einen zusätzlichen Prompt hinzuzufügen, aber dafür müssen wir das Ergebnis des vorherigen Prompts als Kontext für den nachfolgenden Prompt verwenden.

  Suchen Sie im Code die Stelle, an der das Ergebnis des ersten Prompts ausgegeben wird, und fügen Sie darunter folgenden Code hinzu:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Beachten Sie Folgendes:

  1. Wir konstruieren einen neuen Prompt, indem wir das Ergebnis des ersten Prompts zum neuen Prompt hinzufügen:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Wir machen eine neue Anfrage, berücksichtigen dabei aber auch die Anzahl der Tokens, die wir im ersten Prompt verlangt haben, dieses Mal sagen wir zum Beispiel, dass `max_output_tokens` 1200 beträgt.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Wenn wir diesen Code ausführen, erhalten wir nun die folgende Ausgabe:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Verbessern Sie Ihre Einrichtung

Was wir bisher haben, ist funktionierender Code, aber es gibt einige Anpassungen, die wir vornehmen sollten, um die Dinge weiter zu verbessern. Einige Dinge, die wir tun sollten, sind:

- **Trennen Sie Geheimnisse vom Code**, wie z. B. den API-Schlüssel. Geheimnisse gehören nicht in den Code und sollten an einem sicheren Ort gespeichert werden. Um Geheimnisse vom Code zu trennen, können wir Umgebungsvariablen und Bibliotheken wie `python-dotenv` verwenden, um sie aus einer Datei zu laden. So würde das im Code aussehen:

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

     Im Code würden Sie die Umgebungsvariablen so laden:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Ein Wort zur Token-Länge**. Wir sollten überlegen, wie viele Tokens wir benötigen, um den gewünschten Text zu erzeugen. Tokens kosten Geld, daher sollten wir, wo möglich, wirtschaftlich mit der Anzahl der verwendeten Tokens umgehen. Zum Beispiel: Können wir die Eingabeaufforderung so formulieren, dass wir weniger Tokens verwenden?

  Um die verwendeten Tokens zu ändern, können Sie den Parameter `max_output_tokens` verwenden. Wenn Sie z. B. 100 Tokens verwenden möchten, würden Sie Folgendes tun:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Experimentieren mit der Temperatur**. Die Temperatur ist etwas, das wir bisher nicht erwähnt haben, aber ein wichtiger Kontext dafür, wie unser Programm arbeitet. Je höher der Temperaturwert, desto zufälliger ist die Ausgabe. Umgekehrt gilt: Je niedriger der Temperaturwert, desto vorhersehbarer ist die Ausgabe. Überlegen Sie, ob Sie Variation in Ihrer Ausgabe wünschen oder nicht.

  Um die Temperatur zu ändern, können Sie den Parameter `temperature` verwenden. Wenn Sie z. B. eine Temperatur von 0,5 verwenden möchten, würden Sie Folgendes tun:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Hinweis: Je näher bei 1.0, desto variierter die Ausgabe.

- **Reasoning-Modelle verwenden kein `temperature`**. Dies ist eine wichtige Veränderung für 2026. Die aktuellen, nicht veralteten Modelle in Microsoft Foundry sind **Reasoning-Modelle** (die GPT-5-Familie, o-series) – und sie **unterstützen kein `temperature` oder `top_p`** (ebenfalls kein `max_tokens`; verwenden Sie `max_output_tokens`). Wenn Sie `temperature` an `gpt-5-mini` senden, erhalten Sie eine „Parameter nicht unterstützt“-Fehlermeldung. Um also das oben genannte Temperatur-Beispiel auszuprobieren, richten Sie es auf ein Modell, das Sampling-Steuerungen noch unterstützt – zum Beispiel ein offenes **Llama**-Modell wie `Llama-3.3-70B-Instruct` aus dem [Microsoft Foundry Modellkatalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), aufgerufen über den Foundry Models / Azure AI Inference-Endpunkt (genau wie die `githubmodels-*` Beispiele). Für Reasoning-Modelle wie GPT-5 steuern Sie die Ausgabe anders:
  - **Prompt-Engineering** – klare Anweisungen, Beispiele und strukturierte Ausgaben (siehe Lektion [04 – Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) übernehmen die Arbeit, die Sampling-Regler früher erledigten.
  - **Reasoning-Kontrollen** – Parameter wie reasoning effort/verbosity tauschen Tiefe des Reasonings gegen Latenz und Kosten.

  Kurz gesagt: `temperature`/`top_p` sind bei vielen Modellen (Llama, Mistral, Phi und der GPT-4.x-Familie – obwohl GPT-4.x ausläuft) weiterhin gültig, aber der Trend geht zu Prompt-Engineering + Reasoning-Kontrollen bei Reasoning-Modellen wie GPT-5.

## Aufgabe

Für diese Aufgabe können Sie wählen, was Sie bauen möchten.

Hier sind einige Vorschläge:

- Passen Sie die Rezeptgenerator-App weiter an und verbessern Sie sie. Experimentieren Sie mit Temperaturwerten und den Eingabeaufforderungen, um zu sehen, was Sie erreichen können.
- Bauen Sie einen „Study Buddy“. Diese App sollte in der Lage sein, Fragen zu einem Thema zu beantworten, z. B. Python. Sie könnten Eingabeaufforderungen wie „Was ist ein bestimmtes Thema in Python?“ haben oder eine Aufforderung, die sagt: Zeig mir Code zu einem bestimmten Thema usw.
- Geschichte-Bot, lassen Sie Geschichte lebendig werden, weisen Sie den Bot an, eine historische Figur zu spielen und stellen Sie ihm Fragen zu Leben und Zeiten dieser Figur.

## Lösung

### Study Buddy

Unten finden Sie eine Start-Eingabeaufforderung, sehen Sie, wie Sie sie verwenden und nach Ihren Wünschen anpassen können.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Geschichte-Bot

Hier sind einige Eingabeaufforderungen, die Sie verwenden könnten:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Wissenscheck

Was bewirkt das Konzept „Temperature“?

1. Es steuert, wie zufällig die Ausgabe ist.
1. Es steuert, wie groß die Antwort ist.
1. Es steuert, wie viele Tokens verwendet werden.

## 🚀 Herausforderung

Versuchen Sie bei der Bearbeitung der Aufgabe, die Temperatur zu variieren, z. B. auf 0, 0,5 und 1 zu setzen. Denken Sie daran, dass 0 die wenigste Variation und 1 die meiste Variation bedeutet. Welcher Wert funktioniert am besten für Ihre App?

## Toll gemacht! Setzen Sie Ihr Lernen fort

Nach Abschluss dieser Lektion sehen Sie sich unsere [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um Ihr Wissen über Generative KI weiter zu vertiefen!

Gehen Sie zu Lektion 7, in der wir sehen, wie man [Chat-Anwendungen baut](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->