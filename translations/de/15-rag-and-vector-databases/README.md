<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4b0266fbadbba7ded891b6485adc66d",
  "translation_date": "2025-10-17T22:56:04+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "de"
}
-->
# Retrieval Augmented Generation (RAG) und Vektordatenbanken

[![Retrieval Augmented Generation (RAG) und Vektordatenbanken](../../../translated_images/15-lesson-banner.ac49e59506175d4fc6ce521561dab2f9ccc6187410236376cfaed13cde371b90.de.png)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

In der Lektion zu Suchanwendungen haben wir kurz gelernt, wie man eigene Daten in Large Language Models (LLMs) integriert. In dieser Lektion werden wir die Konzepte der Verankerung Ihrer Daten in Ihrer LLM-Anwendung, die Mechanik des Prozesses und die Methoden zur Speicherung von Daten, einschließlich Embeddings und Text, genauer untersuchen.

> **Video kommt bald**

## Einführung

In dieser Lektion behandeln wir Folgendes:

- Eine Einführung in RAG, was es ist und warum es in der künstlichen Intelligenz (KI) verwendet wird.

- Verständnis von Vektordatenbanken und Erstellung einer für unsere Anwendung.

- Ein praktisches Beispiel, wie man RAG in eine Anwendung integriert.

## Lernziele

Nach Abschluss dieser Lektion können Sie:

- Die Bedeutung von RAG bei der Datenabfrage und -verarbeitung erklären.

- Eine RAG-Anwendung einrichten und Ihre Daten mit einem LLM verankern.

- Effektive Integration von RAG und Vektordatenbanken in LLM-Anwendungen.

## Unser Szenario: Verbesserung unserer LLMs mit eigenen Daten

In dieser Lektion möchten wir unsere eigenen Notizen in das Bildungs-Startup einfügen, damit der Chatbot mehr Informationen zu verschiedenen Themen erhält. Mit den Notizen, die wir haben, können Lernende besser studieren und die verschiedenen Themen verstehen, was das Lernen für Prüfungen erleichtert. Um unser Szenario zu erstellen, verwenden wir:

- `Azure OpenAI:` das LLM, das wir zur Erstellung unseres Chatbots verwenden

- `AI für Anfänger-Lektion über neuronale Netzwerke:` dies sind die Daten, auf denen wir unser LLM verankern

- `Azure AI Search` und `Azure Cosmos DB:` Vektordatenbank zur Speicherung unserer Daten und Erstellung eines Suchindex

Benutzer können aus ihren Notizen Übungsquiz erstellen, Lernkarten für die Wiederholung anfertigen und diese zu prägnanten Übersichten zusammenfassen. Um loszulegen, schauen wir uns an, was RAG ist und wie es funktioniert:

## Retrieval Augmented Generation (RAG)

Ein LLM-basierter Chatbot verarbeitet Benutzeranfragen, um Antworten zu generieren. Er ist interaktiv gestaltet und kann mit Benutzern zu einer Vielzahl von Themen kommunizieren. Seine Antworten sind jedoch auf den bereitgestellten Kontext und die grundlegenden Trainingsdaten beschränkt. Beispielsweise ist der Wissensstand von GPT-4 auf September 2021 begrenzt, was bedeutet, dass ihm Wissen über Ereignisse fehlt, die nach diesem Zeitraum stattgefunden haben. Darüber hinaus schließen die Daten, die zur Schulung von LLMs verwendet werden, vertrauliche Informationen wie persönliche Notizen oder das Produkthandbuch eines Unternehmens aus.

### Wie RAGs (Retrieval Augmented Generation) funktionieren

![Zeichnung, die zeigt, wie RAGs funktionieren](../../../translated_images/how-rag-works.f5d0ff63942bd3a638e7efee7a6fce7f0787f6d7a1fca4e43f2a7a4d03cde3e0.de.png)

Angenommen, Sie möchten einen Chatbot bereitstellen, der Quiz aus Ihren Notizen erstellt, dann benötigen Sie eine Verbindung zur Wissensdatenbank. Hier kommt RAG ins Spiel. RAGs funktionieren wie folgt:

- **Wissensdatenbank:** Vor der Abfrage müssen diese Dokumente aufgenommen und vorverarbeitet werden, indem große Dokumente in kleinere Abschnitte unterteilt, in Text-Embeddings umgewandelt und in einer Datenbank gespeichert werden.

- **Benutzeranfrage:** Der Benutzer stellt eine Frage.

- **Abfrage:** Wenn ein Benutzer eine Frage stellt, ruft das Embedding-Modell relevante Informationen aus unserer Wissensdatenbank ab, um mehr Kontext bereitzustellen, der in die Eingabeaufforderung integriert wird.

- **Erweiterte Generierung:** Das LLM verbessert seine Antwort basierend auf den abgerufenen Daten. Dadurch wird die generierte Antwort nicht nur auf vortrainierten Daten, sondern auch auf relevanten Informationen aus dem hinzugefügten Kontext basieren. Die abgerufenen Daten werden verwendet, um die Antworten des LLM zu erweitern. Das LLM gibt dann eine Antwort auf die Frage des Benutzers zurück.

![Zeichnung, die die Architektur von RAGs zeigt](../../../translated_images/encoder-decode.f2658c25d0eadee2377bb28cf3aee8b67aa9249bf64d3d57bb9be077c4bc4e1a.de.png)

Die Architektur von RAGs wird mithilfe von Transformern implementiert, die aus zwei Teilen bestehen: einem Encoder und einem Decoder. Wenn ein Benutzer beispielsweise eine Frage stellt, wird der Eingabetext in Vektoren „kodiert“, die die Bedeutung der Wörter erfassen, und die Vektoren werden „dekodiert“, um unseren Dokumentenindex zu durchsuchen und neuen Text basierend auf der Benutzeranfrage zu generieren. Das LLM verwendet sowohl ein Encoder- als auch ein Decoder-Modell, um die Ausgabe zu generieren.

Zwei Ansätze bei der Implementierung von RAG gemäß dem vorgeschlagenen Papier: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) sind:

- **_RAG-Sequence_** verwendet abgerufene Dokumente, um die bestmögliche Antwort auf eine Benutzeranfrage vorherzusagen.

- **RAG-Token** verwendet Dokumente, um das nächste Token zu generieren, und ruft sie dann ab, um die Benutzeranfrage zu beantworten.

### Warum sollte man RAGs verwenden?

- **Informationsreichtum:** Stellt sicher, dass Textantworten aktuell und auf dem neuesten Stand sind. Es verbessert daher die Leistung bei domänenspezifischen Aufgaben, indem es auf die interne Wissensdatenbank zugreift.

- Reduziert Fälschungen, indem **überprüfbare Daten** in der Wissensdatenbank verwendet werden, um den Benutzeranfragen Kontext zu geben.

- Es ist **kosteneffektiv**, da sie im Vergleich zur Feinabstimmung eines LLM wirtschaftlicher sind.

## Erstellung einer Wissensdatenbank

Unsere Anwendung basiert auf unseren persönlichen Daten, d. h. der Lektion über neuronale Netzwerke aus dem AI For Beginners-Lehrplan.

### Vektordatenbanken

Eine Vektordatenbank, im Gegensatz zu traditionellen Datenbanken, ist eine spezialisierte Datenbank, die darauf ausgelegt ist, eingebettete Vektoren zu speichern, zu verwalten und zu durchsuchen. Sie speichert numerische Darstellungen von Dokumenten. Das Zerlegen von Daten in numerische Embeddings erleichtert es unserem KI-System, die Daten zu verstehen und zu verarbeiten.

Wir speichern unsere Embeddings in Vektordatenbanken, da LLMs eine Begrenzung der Anzahl der als Eingabe akzeptierten Tokens haben. Da Sie nicht die gesamten Embeddings an ein LLM übergeben können, müssen wir sie in Abschnitte unterteilen, und wenn ein Benutzer eine Frage stellt, werden die Embeddings, die der Frage am ähnlichsten sind, zusammen mit der Eingabeaufforderung zurückgegeben. Das Chunking reduziert auch die Kosten für die Anzahl der durch ein LLM übergebenen Tokens.

Einige beliebte Vektordatenbanken sind Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant und DeepLake. Sie können ein Azure Cosmos DB-Modell mit dem folgenden Befehl über die Azure CLI erstellen:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Von Text zu Embeddings

Bevor wir unsere Daten speichern, müssen wir sie in Vektor-Embeddings umwandeln, bevor sie in der Datenbank gespeichert werden. Wenn Sie mit großen Dokumenten oder langen Texten arbeiten, können Sie sie basierend auf den erwarteten Abfragen in Abschnitte unterteilen. Das Chunking kann auf Satzebene oder auf Absatzebene erfolgen. Da das Chunking Bedeutungen aus den umgebenden Wörtern ableitet, können Sie einem Abschnitt zusätzlichen Kontext hinzufügen, z. B. den Dokumenttitel oder einige Texte vor oder nach dem Abschnitt. Sie können die Daten wie folgt unterteilen:

```python
def split_text(text, max_length, min_length):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if len(' '.join(current_chunk)) < max_length and len(' '.join(current_chunk)) > min_length:
            chunks.append(' '.join(current_chunk))
            current_chunk = []

    # If the last chunk didn't reach the minimum length, add it anyway
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Sobald die Daten unterteilt sind, können wir unseren Text mit verschiedenen Embedding-Modellen einbetten. Einige Modelle, die Sie verwenden können, sind: word2vec, ada-002 von OpenAI, Azure Computer Vision und viele mehr. Die Auswahl eines Modells hängt von den verwendeten Sprachen, der Art des kodierten Inhalts (Text/Bilder/Audio), der Größe der Eingabe, die es kodieren kann, und der Länge der Embedding-Ausgabe ab.

Ein Beispiel für eingebetteten Text mit OpenAIs `text-embedding-ada-002` Modell ist:
![Ein Embedding des Wortes Katze](../../../translated_images/cat.74cbd7946bc9ca380a8894c4de0c706a4f85b16296ffabbf52d6175df6bf841e.de.png)

## Abfrage und Vektorsuche

Wenn ein Benutzer eine Frage stellt, wandelt der Retriever diese mithilfe des Abfrage-Encoders in einen Vektor um, durchsucht dann unseren Dokumentensuchindex nach relevanten Vektoren im Dokument, die mit der Eingabe zusammenhängen. Sobald dies abgeschlossen ist, werden sowohl der Eingabevektor als auch die Dokumentenvektoren in Text umgewandelt und durch das LLM geleitet.

### Abfrage

Die Abfrage erfolgt, wenn das System versucht, schnell die Dokumente aus dem Index zu finden, die die Suchkriterien erfüllen. Ziel des Retrievers ist es, Dokumente zu finden, die verwendet werden können, um Kontext bereitzustellen und das LLM auf Ihre Daten zu verankern.

Es gibt mehrere Möglichkeiten, innerhalb unserer Datenbank zu suchen, wie zum Beispiel:

- **Schlüsselwortsuche** - wird für Textsuchen verwendet.

- **Semantische Suche** - verwendet die semantische Bedeutung von Wörtern.

- **Vektorsuche** - wandelt Dokumente von Text in Vektordarstellungen mithilfe von Embedding-Modellen um. Die Abfrage erfolgt durch die Suche nach Dokumenten, deren Vektordarstellungen der Benutzerfrage am nächsten kommen.

- **Hybrid** - eine Kombination aus Schlüsselwort- und Vektorsuche.

Eine Herausforderung bei der Abfrage tritt auf, wenn es keine ähnliche Antwort auf die Anfrage in der Datenbank gibt. Das System gibt dann die besten Informationen zurück, die es finden kann. Sie können jedoch Taktiken wie das Festlegen der maximalen Relevanzdistanz oder die Verwendung einer hybriden Suche anwenden, die sowohl Schlüsselwörter als auch Vektorsuche kombiniert. In dieser Lektion verwenden wir die hybride Suche, eine Kombination aus Vektor- und Schlüsselwortsuche. Wir speichern unsere Daten in einem Dataframe mit Spalten, die die Abschnitte sowie Embeddings enthalten.

### Vektorähnlichkeit

Der Retriever durchsucht die Wissensdatenbank nach Embeddings, die nahe beieinander liegen, den nächsten Nachbarn, da sie Texte sind, die ähnlich sind. Wenn ein Benutzer eine Anfrage stellt, wird diese zuerst eingebettet und dann mit ähnlichen Embeddings abgeglichen. Die häufigste Messmethode, um die Ähnlichkeit verschiedener Vektoren zu bestimmen, ist die Kosinus-Ähnlichkeit, die auf dem Winkel zwischen zwei Vektoren basiert.

Wir können die Ähnlichkeit auch mit anderen Alternativen messen, wie der euklidischen Distanz, die die gerade Linie zwischen den Endpunkten der Vektoren darstellt, und dem Skalarprodukt, das die Summe der Produkte der entsprechenden Elemente von zwei Vektoren misst.

### Suchindex

Bei der Abfrage müssen wir einen Suchindex für unsere Wissensdatenbank erstellen, bevor wir die Suche durchführen. Ein Index speichert unsere Embeddings und kann auch in einer großen Datenbank schnell die ähnlichsten Abschnitte abrufen. Wir können unseren Index lokal erstellen mit:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Neu-Ranking

Nachdem Sie die Datenbank abgefragt haben, müssen Sie möglicherweise die Ergebnisse nach Relevanz sortieren. Ein Neu-Ranking-LLM nutzt maschinelles Lernen, um die Relevanz der Suchergebnisse zu verbessern, indem es sie von den relevantesten anordnet. Mit Azure AI Search wird das Neu-Ranking automatisch für Sie durchgeführt, indem ein semantischer Neu-Ranker verwendet wird. Ein Beispiel dafür, wie Neu-Ranking mit den nächsten Nachbarn funktioniert:

```python
# Find the most similar documents
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Print the most similar documents
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Alles zusammenbringen

Der letzte Schritt ist das Hinzufügen unseres LLM, um Antworten zu erhalten, die auf unseren Daten basieren. Wir können es wie folgt implementieren:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Convert the question to a query vector
    query_vector = create_embeddings(user_input)

    # Find the most similar documents
    distances, indices = nbrs.kneighbors([query_vector])

    # add documents to query  to provide context
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # combine the history and the user input
    history.append(user_input)

    # create a message object
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": history[-1]}
    ]

    # use chat completion to generate a response
    response = openai.chat.completions.create(
        model="gpt-4",
        temperature=0.7,
        max_tokens=800,
        messages=messages
    )

    return response.choices[0].message

chatbot(user_input)
```

## Bewertung unserer Anwendung

### Bewertungsmetriken

- Qualität der bereitgestellten Antworten, um sicherzustellen, dass sie natürlich, flüssig und menschenähnlich klingen.

- Verankerung der Daten: Bewertung, ob die Antwort aus den bereitgestellten Dokumenten stammt.

- Relevanz: Bewertung, ob die Antwort zur gestellten Frage passt und damit zusammenhängt.

- Flüssigkeit: ob die Antwort grammatikalisch Sinn ergibt.

## Anwendungsfälle für die Verwendung von RAG (Retrieval Augmented Generation) und Vektordatenbanken

Es gibt viele verschiedene Anwendungsfälle, bei denen Funktionsaufrufe Ihre App verbessern können, wie:

- Fragen und Antworten: Verankerung Ihrer Unternehmensdaten in einem Chat, den Mitarbeiter nutzen können, um Fragen zu stellen.

- Empfehlungssysteme: Erstellung eines Systems, das die ähnlichsten Werte wie Filme, Restaurants und vieles mehr abgleicht.

- Chatbot-Dienste: Sie können Chatverläufe speichern und die Konversation basierend auf den Benutzerdaten personalisieren.

- Bildsuche basierend auf Vektor-Embeddings, nützlich bei der Bilderkennung und Anomalieerkennung.

## Zusammenfassung

Wir haben die grundlegenden Bereiche von RAG behandelt, von der Hinzufügung unserer Daten zur Anwendung über die Benutzeranfrage bis hin zur Ausgabe. Um die Erstellung von RAG zu vereinfachen, können Sie Frameworks wie Semantic Kernel, Langchain oder Autogen verwenden.

## Aufgabe

Um Ihr Lernen über Retrieval Augmented Generation (RAG) fortzusetzen, können Sie Folgendes erstellen:

- Erstellen Sie ein Frontend für die Anwendung mit dem Framework Ihrer Wahl.

- Verwenden Sie ein Framework, entweder LangChain oder Semantic Kernel, und erstellen Sie Ihre Anwendung neu.

Herzlichen Glückwunsch zum Abschluss der Lektion 👏.

## Lernen hört hier nicht auf, setzen Sie die Reise fort

Nach Abschluss dieser Lektion schauen Sie sich unsere [Generative AI Learning Collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um Ihr Wissen über generative KI weiter zu vertiefen!

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.