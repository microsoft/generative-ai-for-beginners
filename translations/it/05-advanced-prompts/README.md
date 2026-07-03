# Creare prompt avanzati

[![Creare prompt avanzati](../../../translated_images/it/05-lesson-banner.522610fd4a2cd82d.webp)](https://youtu.be/BAjzkaCdRok?si=NmUIyRf7-cDgbjtt)

Ricapitoliamo alcune nozioni dal capitolo precedente:

> Il _prompt engineering_ è il processo con cui **guidiamo il modello verso risposte più pertinenti** fornendo istruzioni o contesti più utili.

Ci sono anche due passaggi nello scrivere prompt: costruire il prompt, fornendo un contesto rilevante, e l’_ottimizzazione_, ovvero come migliorare gradualmente il prompt.

A questo punto, abbiamo una comprensione di base di come scrivere prompt, ma dobbiamo approfondire. In questo capitolo, passerai dal provare vari prompt a comprendere perché un prompt è migliore di un altro. Imparerai come costruire prompt seguendo alcune tecniche di base applicabili a qualsiasi LLM.

## Introduzione

In questo capitolo, tratteremo i seguenti argomenti:

- Estendere la tua conoscenza di prompt engineering applicando diverse tecniche ai tuoi prompt.
- Configurare i tuoi prompt per variare l’output.

## Obiettivi di apprendimento

Dopo aver completato questa lezione, sarai in grado di:

- Applicare tecniche di prompt engineering che migliorano il risultato dei tuoi prompt.
- Eseguire prompting che è variabile o deterministico.

## Prompt engineering

Il prompt engineering è il processo di creazione di prompt che produrranno il risultato desiderato. Il prompt engineering non è solo scrivere un testo. Non è una disciplina ingegneristica, ma piuttosto un insieme di tecniche che puoi applicare per ottenere il risultato desiderato.

### Un esempio di prompt

Prendiamo un prompt semplice come questo:

> Genera 10 domande sulla geografia.

In questo prompt, stai effettivamente applicando una serie di tecniche diverse.

Vediamolo nel dettaglio.

- **Contesto**, specifichi che dovrebbe riguardare la "geografia".
- **Limitare l’output**, vuoi non più di 10 domande.

### Limitazioni del prompting semplice

Potresti ottenere o meno il risultato desiderato. Otterrai le tue domande generate, ma la geografia è un argomento vasto e potresti non ottenere ciò che vuoi per i seguenti motivi:

- **Argomento vasto**, non sai se parlerà di paesi, capitali, fiumi e così via.
- **Formato**, cosa succede se vuoi che le domande siano formattate in un certo modo?

Come vedi, ci sono molte cose da considerare creando i prompt.

Finora abbiamo visto un esempio di prompt semplice, ma l’IA generativa è capace di molto più per aiutare persone in vari ruoli e settori. Esploriamo alcune tecniche di base.

### Tecniche per il prompting

Prima di tutto, dobbiamo capire che il prompting è una proprietà _emergente_ di un LLM, il che significa che non è una funzionalità incorporata nel modello ma qualcosa che scopriamo man mano che usiamo il modello.

Ci sono alcune tecniche di base che possiamo usare per promptare un LLM. Vediamole.

- **Zero-shot prompting**, questa è la forma più semplice di prompting. È un singolo prompt che richiede una risposta dal LLM basata esclusivamente sui suoi dati di addestramento.
- **Few-shot prompting**, questo tipo di prompting guida il LLM fornendo uno o più esempi su cui può basarsi per generare la risposta.
- **Chain-of-thought**, questo tipo di prompting indica al LLM come scomporre un problema in passaggi.
- **Conoscenza generata**, per migliorare la risposta a un prompt, puoi fornire fatti o conoscenze generate in aggiunta al tuo prompt.
- **Least to most**, come chain-of-thought, questa tecnica consiste nello scomporre un problema in una serie di passaggi e poi chiedere che vengano eseguiti in ordine.
- **Self-refine**, questa tecnica riguarda la critica dell’output del LLM e poi la richiesta di migliorarlo.
- **Maieutic prompting**. Qui vuoi assicurarti che la risposta del LLM sia corretta e chiedi di spiegare varie parti della risposta. È una forma di self-refine.

### Zero-shot prompting

Questo stile di prompting è molto semplice, consiste in un singolo prompt. Probabilmente è la tecnica che stai usando iniziando ad apprendere sugli LLM. Ecco un esempio:

- Prompt: "Cos’è l’Algebra?"
- Risposta: "L’algebra è un ramo della matematica che studia i simboli matematici e le regole per manipolare questi simboli."

### Few-shot prompting

Questo stile di prompting aiuta il modello fornendo alcuni esempi insieme alla richiesta. Consiste in un singolo prompt con dati aggiuntivi specifici del compito. Ecco un esempio:

- Prompt: "Scrivi una poesia nello stile di Shakespeare. Ecco alcuni esempi di sonetti shakespeariani:
  Sonetto 18: ‘Devo paragonarti a un giorno d’estate? Tu sei più dolce e più temperato...’
  Sonetto 116: ‘Non opporrò impedimenti al matrimonio delle menti vere. L’amore non è amore Che cambia quando trova cambiamento...’
  Sonetto 132: ‘I tuoi occhi amo, e loro, pietosi, Sapendo che il tuo cuore mi tormenta con disprezzo,...’
  Ora scrivi un sonetto sulla bellezza della luna."
- Risposta: "Nel cielo, la luna splende dolcemente, In luce argentata che diffonde la sua grazia gentile,..."

Gli esempi forniscono al LLM il contesto, il formato o lo stile dell’output desiderato. Aiutano il modello a capire il compito specifico e generare risposte più accurate e pertinenti.

### Chain-of-thought

Chain-of-thought è una tecnica molto interessante perché consiste nel guidare il LLM attraverso una serie di passaggi. L’idea è istruire il LLM in modo che comprenda come fare qualcosa. Considera il seguente esempio, con e senza chain-of-thought:

    - Prompt: "Alice ha 5 mele, ne lancia 3, ne dà 2 a Bob e Bob ne ridà una, quante mele ha Alice?"
    - Risposta: 5

Il LLM risponde 5, che è sbagliato. La risposta corretta è 1 mela, dato il calcolo (5 -3 -2 + 1 = 1).

Come possiamo insegnare al LLM a fare questo correttamente?

Proviamo chain-of-thought. Applicare chain-of-thought significa:

1. Dare al LLM un esempio simile.
2. Mostrare il calcolo, e come calcolarlo correttamente.
3. Fornire il prompt originale.

Ecco come:

- Prompt: "Lisa ha 7 mele, ne lancia 1, dà 4 mele a Bart e Bart ne ridà una:
  7 -1 = 6
  6 -4 = 2
  2 +1 = 3  
  Alice ha 5 mele, ne lancia 3, ne dà 2 a Bob e Bob ne ridà una, quante mele ha Alice?"
  Risposta: 1

Nota come scriviamo prompt sostanzialmente più lunghi con un altro esempio, un calcolo e poi il prompt originale e arriviamo alla risposta corretta 1.

Come puoi vedere chain-of-thought è una tecnica molto potente.

### Conoscenza generata

Molte volte, quando vuoi costruire un prompt, vuoi farlo usando i dati della tua stessa azienda. Vuoi che una parte del prompt venga dall’azienda e l’altra parte sia il prompt effettivo che ti interessa.

Ad esempio, ecco come il tuo prompt può apparire se sei nel settore assicurativo:

```text
{{company}}: {{company_name}}
{{products}}:
{{products_list}}
Please suggest an insurance given the following budget and requirements:
Budget: {{budget}}
Requirements: {{requirements}}
```

Sopra, vedi come il prompt viene costruito usando un template. Nel template ci sono varie variabili, indicate come `{{variable}}`, che saranno sostituite con i valori reali da un API aziendale.

Ecco un esempio di come potrebbe apparire il prompt una volta che le variabili sono state sostituite con contenuti della tua azienda:

```text
Insurance company: ACME Insurance
Insurance products (cost per month):
- Car, cheap, 500 USD
- Car, expensive, 1100 USD
- Home, cheap, 600 USD
- Home, expensive, 1200 USD
- Life, cheap, 100 USD

Please suggest an insurance given the following budget and requirements:
Budget: $1000
Requirements: Car, Home, and Life insurance
```

Eseguire questo prompt tramite un LLM produrrà una risposta come questa:

```output
Given the budget and requirements, we suggest the following insurance package from ACME Insurance:
- Car, cheap, 500 USD
- Home, cheap, 600 USD
- Life, cheap, 100 USD
Total cost: $1,200 USD
```

Come vedi, suggerisce anche l’assicurazione sulla vita, cosa che non dovrebbe fare. Questo risultato indica che dobbiamo ottimizzare il prompt rendendo più chiaro cosa può essere consentito. Dopo qualche _tentativo ed errore_, arriviamo al seguente prompt:

```text
Insurance company: ACME Insurance
Insurance products (cost per month):
- type: Car, cheap, cost: 500 USD
- type: Car, expensive, cost: 1100 USD
- type: Home, cheap, cost: 600 USD
- type: Home, expensive, cost: 1200 USD
- type: Life, cheap, cost: 100 USD

Please suggest an insurance given the following budget and requirements:
Budget: $1000 restrict choice to types: Car, Home
```

Nota come aggiungere _tipo_ e _costo_ e anche usare la parola chiave _restrizione_ aiuta l’LLM a capire cosa vogliamo.

Ora otteniamo questa risposta:

```output
Given the budget and requirements, we suggest the Car, Cheap insurance product which costs 500 USD per month.
```

L’obiettivo di questo esempio era mostrare che anche usando una tecnica base come la _conoscenza generata_, nella maggior parte dei casi dobbiamo ottimizzare il prompt per ottenere il risultato desiderato.

### Least-to-most

L’idea del prompting Least-to-most è di suddividere un problema più grande in sotto-problemi. In questo modo, aiuti a guidare l’LLM su come "conquistare" il problema più grande. Un buon esempio potrebbe essere per la data science, dove puoi chiedere all’LLM di suddividere un problema così:

> Prompt: Come svolgere data science in 5 passaggi?

Con il tuo assistente AI che risponde:

1. Raccogli dati  
2. Pulisci i dati  
3. Analizza i dati  
4. Rappresenta i dati  
5. Presenta i dati

### Self-refine, critica i risultati

Con le AI generative e gli LLM, non puoi fidarti sempre dell’output. Devi verificarlo. Dopotutto, il LLM sta solo presentando quello che è il prossimo elemento più probabile da dire, non quello che è corretto. Quindi, una buona idea è chiedere al LLM di criticare se stesso, il che ci porta alla tecnica self-refine.

Funziona così:

1. Prompt iniziale che chiede al LLM di risolvere un problema  
2. Risposta del LLM  
3. Critichi la risposta e chiedi all’AI di migliorare  
4. Il LLM risponde di nuovo, considerando la critica e suggerendo soluzioni

Puoi ripetere questo processo quante volte vuoi.

Ecco un esempio usando questa tecnica:

> Prompt: "Crea una Web API Python con le rotte products e customers"

Risposta AI:

```python
import flask
app = Flask(__name__)

@app.route('/products')
def products():
    return 'Products'

@app.route('/customers')
def customers():
    return 'Customers'
```

> Prompt: suggerisci 3 miglioramenti al codice sopra

Risposta AI:

```text
Sure, here are three suggestions to improve the code:

Import the correct module: The first line should import Flask instead of flask. The correct import statement should be from flask import Flask.

Add a main function: Add a if __name__ == '__main__': block to the end of the file to run the application when the file is executed.

Use f-strings: Use f-strings to format the return statements in the route functions. For example, return 'Products' can be changed to return f'This is the {request.path} page'.
```

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/products')
def products():
    return f'This is the {request.path} page'

@app.route('/customers')
def customers():
    return f'This is the {request.path} page'

if __name__ == '__main__':
    app.run()
```

Come vedi, la risposta AI sopra migliora il primo codice suggerito grazie alla critica della prima risposta.

### Maieutic prompting

Il maieutic prompting è una tecnica simile al self-refine ma riguarda più il chiedere al LLM di spiegare se stesso. Lo scopo è ridurre le incoerenze nell’output del LLM per garantire che arrivi alla risposta corretta. Il flusso da seguire è:

1. Chiedi al LLM di rispondere a una domanda  
2. Per ogni parte della risposta, chiedi al LLM di spiegare più in dettaglio  
3. Se ci sono incoerenze, scarta le parti incoerenti

Ripeti 2 e 3 finché non hai esaminato tutte le parti e sei soddisfatto della risposta.

Ecco un esempio di prompt:

> prompt: Come posso creare un piano di crisi per mitigare una pandemia in 5 passaggi?  
> Risposta LLM:

```text
1. Identify the risks
1. Identify the stakeholders
1. Identify the resources
1. Identify the actions
1. Identify the communication channels
```

Sono stati identificati 5 passaggi, ma possiamo stabilire se è corretto? Chiediamo al LLM di spiegare ogni passaggio:

> prompt: Spiega il primo passaggio più in dettaglio, quali sono i rischi in dettaglio in una pandemia?

```text
The risks are the following:

- Loss of life
- Loss of business
- Loss of reputation
- Loss of customers
- Loss of employees
```

A questo punto, vogliamo assicurarci che il LLM sia corretto, quindi chiediamo di spiegare il primo rischio più in dettaglio e speriamo sia coerente con la risposta di prima:

> prompt: In una pandemia, qual è il rischio più grande e perché?

```text
The biggest risk is loss of life because it's the most important thing to protect.
```

> Quali sono i due rischi più grandi in una pandemia?

```text
The two biggest risks are loss of life and loss of business.
```

A questo punto il LLM è coerente e menziona "vita" e "affari" come i due maggiori rischi. Ora possiamo passare al passaggio successivo e sentirci abbastanza sicuri. Tuttavia, non dovremmo fidarci ciecamente del LLM, dovremmo sempre verificare l’output.

## Varia il tuo output

Gli LLM sono per natura non deterministici, il che significa che otterrai risultati diversi ogni volta che esegui lo stesso prompt. Prova il seguente prompt, ad esempio:

> "Genera codice per una Web API Python"

```python
# Importa i moduli necessari
import flask
from flask import request, jsonify

# Crea un'app Flask
app = flask.Flask(__name__)

# Crea una rotta per l'API
@app.route('/api', methods=['GET'])
def api():
    # Ottieni i dati dalla richiesta
    data = request.args

    # Elabora i dati
    result = process_data(data)

    # Restituisci il risultato come JSON
    return jsonify(result)

# Funzione per elaborare i dati
def process_data(data):
    # Fai qualcosa con i dati
    result = data + 1

    # Restituisci il risultato
    return result

# Avvia l'app
if __name__ == '__main__':
    app.run()

```

Eseguendo di nuovo lo stesso prompt si genera una risposta leggermente diversa:

```python
#importa i pacchetti necessari
import flask
from flask import request, jsonify

#crea l'applicazione Flask
app = flask.Flask(__name__)
app.config["DEBUG"] = True

#crea una lista di libri
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

#crea un endpoint per l'API
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Books API</h1>
<p>A prototype API for retrieving books.</p>'''

#crea un endpoint per restituire tutti i libri
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

#crea un endpoint per restituire un singolo libro
@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    #verifica se un ID è stato fornito come parte dell'URL
    #se l'ID è fornito, assegnalo a una variabile
    #se nessun ID è fornito, mostra un errore
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    #crea una lista vuota per i nostri risultati
    results = []

    #cicla attraverso i dati e cerca i risultati che corrispondono all'ID richiesto
    #gli ID sono unici, ma altri campi potrebbero restituire molti risultati
    for book in books:
        if book['id'] == id:
            results.append(book)

    #usa la funzione jsonify di Flask per convertire la nostra lista di
    #dizionari Python nel formato JSON
    return jsonify(results)

app.run()
```

> Quindi l’output variato è un problema?

Dipende da quello che stai cercando di fare. Se vuoi una risposta specifica allora è un problema. Se ti va bene un output variabile come "Genera 3 domande sulla geografia qualsiasi", allora non è un problema.

### Usare la temperatura per variare il tuo output

Ok, abbiamo deciso che vogliamo limitare l’output per renderlo più prevedibile, cioè più deterministico. Come si fa?

La temperatura è un valore tra 0 e 1, dove 0 è il più deterministico e 1 il più vario. Il valore predefinito è 0.7. Vediamo cosa succede con due esecuzioni dello stesso prompt con la temperatura impostata a 0.1:

> "Genera codice per una Web API Python"

```python
#importa le librerie necessarie
import flask
from flask import request, jsonify

#crea un'istanza della classe Flask
app = flask.Flask(__name__)

#crea un endpoint per l'API
@app.route('/api/v1/endpoint', methods=['GET'])
def api_endpoint():
    #ottieni i dati della richiesta
    data = request.get_json()

    #elabora i dati
    result = process_data(data)

    #restituisci il risultato
    return jsonify(result)

#funzione per elaborare i dati
def process_data(data):
    #elabora i dati
    result = {'result': 'success'}

    #restituisci il risultato
    return result

#esegui l'app Flask
if __name__ == '__main__':
    app.run()

```

Eseguendo di nuovo il prompt otteniamo questo risultato:

```python
#importa le librerie necessarie
import flask
from flask import request, jsonify

#crea un'app Flask
app = flask.Flask(__name__)

#crea una route per l'API
@app.route('/api', methods=['GET'])
def api_call():
    #ottieni i dati dalla richiesta
    data = request.get_json()

    #elabora i dati
    result = process_data(data)

    #restituisci il risultato
    return jsonify(result)

#definisci la funzione process_data
def process_data(data):
    #fai qualcosa con i dati
    result = data + 1

    #restituisci il risultato
    return result

#esegui l'app
if __name__ == '__main__':
    app.run()

```

C’è solo una differenza minima tra questi due output. Facciamo il contrario stavolta, impostiamo la temperatura a 0.9:

```python
# Importa le librerie necessarie
import flask
from flask import request, jsonify

# Crea un'app Flask
app = flask.Flask(__name__)

# Crea una route per l'API
@app.route('/api', methods=['GET'])
def api_call():
    # Ottieni i dati dalla richiesta
    data = request.args

    # Elabora i dati
    result = process_data(data)

    # Restituisci il risultato
    return jsonify(result)

# Funzione per elaborare i dati
def process_data(data):
    # Fai qualcosa con i dati
    result = data + 1

    # Restituisci il risultato
    return result

# Esegui l'app
if __name__ == '__main__':
    app.run()

```

e il secondo tentativo con temperatura 0.9:

```python
import flask
from flask import request, jsonify

# crea l'app Flask
app = flask.Flask(__name__)
app.config['DEBUG'] = True

# crea alcuni dati di prova
books = [
    {'id': 0, 'title': 'A Fire Upon The Deep', 'author': 'Vernor Vinge', 'first_sentence': 'The coldsleep itself was dreamless.', 'year_published': '1992'},
    {'id': 1, 'title': 'The Ones Who Walk Away From Omelas', 'author': 'Ursula K. Le Guin', 'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.', 'published': '1973'},
    {'id': 2, 'title': 'Dhalgren', 'author': 'Samuel R. Delany', 'first_sentence': 'to wound the autumnal city.', 'published': '1975'}
]

# crea un endpoint
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to our book API!</h1>'''

@app.route('/api/v1/resources/books

```

Come vedi, i risultati non potrebbero essere più vari.
> Nota che ci sono più parametri che puoi modificare per variare l'output, come top-k, top-p, penalità di ripetizione, penalità di lunghezza e penalità di diversità, ma questi sono fuori dal campo di questo curriculum.

## Buone pratiche

Ci sono molte pratiche che puoi applicare per cercare di ottenere ciò che desideri. Troverai il tuo stile personale man mano che utilizzi sempre di più il prompting.

Oltre alle tecniche che abbiamo coperto, ci sono alcune buone pratiche da considerare quando si esegue il prompting di un LLM.

Ecco alcune buone pratiche da considerare:

- **Specifica il contesto**. Il contesto è importante, più puoi specificare come dominio, argomento, ecc., meglio è.
- Limita l’output. Se vuoi un numero specifico di elementi o una lunghezza specifica, specificarlo.
- **Specifica sia cosa che come**. Ricorda di menzionare sia cosa vuoi che come lo vuoi, per esempio "Crea una API Web Python con le rotte products e customers, dividila in 3 file".
- **Usa template**. Spesso vorrai arricchire i tuoi prompt con dati della tua azienda. Usa template per fare questo. I template possono avere variabili che sostituisci con dati reali.
- **Scrivi correttamente**. Gli LLM potrebbero fornirti una risposta corretta, ma se scrivi correttamente otterrai una risposta migliore.

## Compito

Ecco un codice in Python che mostra come costruire una semplice API usando Flask:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run()
```

Usa un assistente AI come GitHub Copilot o ChatGPT e applica la tecnica del "self-refine" per migliorare il codice.

## Soluzione

Prova a risolvere il compito aggiungendo prompt adeguati al codice.

> [!TIP]
> Formula un prompt per chiedere di migliorare, è una buona idea limitare quante migliorie chiedere. Puoi anche chiedere di migliorarlo in un certo modo, per esempio architettura, prestazioni, sicurezza, ecc.

[Solution](../../../05-advanced-prompts/python/aoai-solution.py)

## Verifica della conoscenza

Perché userei il chain-of-thought prompting? Mostrami 1 risposta corretta e 2 risposte errate.

1. Per insegnare all’LLM come risolvere un problema.
1. B, Per insegnare all’LLM a trovare errori nel codice.
1. C, Per istruire l’LLM a trovare soluzioni differenti.

A: 1, perché chain-of-thought serve a mostrare all’LLM come risolvere un problema fornendogli una serie di passaggi e problemi simili e come sono stati risolti.

## 🚀 Sfida

Hai appena usato la tecnica del self-refine nel compito. Prendi un programma che hai scritto e considera quali miglioramenti vorresti applicargli. Ora usa la tecnica del self-refine per applicare i cambiamenti proposti. Cosa pensi del risultato, migliore o peggiore?

## Ottimo lavoro! Continua a imparare

Dopo aver completato questa lezione, dai un’occhiata alla nostra [collezione di apprendimento Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per continuare a migliorare le tue conoscenze su Generative AI!

Passa alla Lezione 6 dove applicheremo la nostra conoscenza di Prompt Engineering costruendo [app di generazione testo](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->