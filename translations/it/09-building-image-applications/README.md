# Creazione di Applicazioni per la Generazione di Immagini

[![Creazione di Applicazioni per la Generazione di Immagini](../../../translated_images/it/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Gli LLM non servono solo per la generazione di testo. Puoi anche generare immagini da descrizioni testuali. Le immagini come modalità sono utili in MedTech, architettura, turismo, sviluppo di giochi, marketing e altro ancora. In questa lezione esaminiamo i modelli **GPT Image** odierni e costruiamo un'app di generazione di immagini.

## Introduzione

La generazione di immagini ti permette di trasformare un prompt in linguaggio naturale in un'immagine. In questa lezione lavoriamo con la famiglia di modelli **`gpt-image`** di OpenAI - la generazione attuale di modelli di immagini disponibili su **[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)** e sulla piattaforma OpenAI. Questi modelli sostituiscono i vecchi modelli DALL·E (DALL·E 2/3 sono legacy).

Durante tutta la lezione usiamo una startup fittizia, **Edu4All**, che sviluppa strumenti di apprendimento. Il team vuole generare illustrazioni per compiti e materiali di studio.

## Obiettivi di apprendimento

Al termine di questa lezione sarai in grado di:

- Spiegare cos'è la generazione di immagini e dove è utile.
- Comprendere la famiglia di modelli `gpt-image` e come differisce dai modelli legacy DALL·E.
- Creare un'app per la generazione di immagini in Python (e TypeScript / .NET).
- Modificare immagini e applicare barriere di sicurezza con metaprompt.

## Cos'è la generazione di immagini?

I modelli di generazione di immagini creano immagini da un prompt testuale. I modelli moderni come `gpt-image` sono costruiti su tecniche di trasformatori + diffusione: il modello apprende la relazione tra testo e immagini durante l'addestramento, poi, dato un prompt, "denoising" iterativamente un rumore casuale in un'immagine che corrisponde alla descrizione.

Due famiglie ben conosciute di modelli di immagini sono:

- **`gpt-image` (OpenAI)** - la generazione attuale, utilizzata in questa lezione. Supporta la generazione da testo a immagine e la modifica dell'immagine (inpainting con maschera).
- **Midjourney** - un modello di terze parti popolare con servizio proprio e flusso di lavoro basato su Discord.

> I vecchi modelli di immagini OpenAI - **DALL·E 2** e **DALL·E 3** - sono legacy. DALL·E 3 non è più disponibile per nuove distribuzioni e funzionalità come `create_variation` esistevano solo in DALL·E 2. Usa i modelli `gpt-image` per nuove applicazioni.

### Quale modello `gpt-image` dovrei usare?

Su Microsoft Foundry i seguenti sono **Generalmente Disponibili**:

| Modello | Note |
| --- | --- |
| **`gpt-image-2`** | Il modello di immagini più recente e più capace - predefinito consigliato. |
| `gpt-image-1.5` | Generalmente disponibile; qualità forte a costo inferiore. |
| `gpt-image-1-mini` | Generalmente disponibile; più veloce / costo più basso. |
| `gpt-image-1` | Solo anteprima. |

Controlla sempre l'attuale [lista modelli Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst) per disponibilità e regioni.

> **Importante:** i modelli `gpt-image` restituiscono l'immagine generata in **base64** (`b64_json`), non come URL. Il tuo codice decodifica la stringa base64 in byte e la salva - non c'è un URL dell'immagine da scaricare.

## Impostazione

Puoi eseguire gli esempi contro **Azure OpenAI in Microsoft Foundry** (gli esempi `aoai-*`) o la **piattaforma OpenAI** (gli esempi `oai-*`).

### 1. Crea e distribuisci un modello

Segui la guida [crea una risorsa](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) per creare una risorsa Microsoft Foundry, poi distribuisci un modello di immagini - si consiglia **`gpt-image-2`**.

### 2. Configura il tuo `.env`

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

Trova questi valori nella pagina **Distribuzioni** della tua risorsa nel [portale Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst).

### 3. Installa le librerie

Crea un `requirements.txt`:

```text
python-dotenv
openai
pillow
```

Poi crea e attiva un ambiente virtuale e installa:

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Costruisci l'app

Crea `app.py` con il codice seguente. Genera un'immagine e la salva in PNG.

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# Indirizza il client alla tua risorsa Azure OpenAI (Microsoft Foundry).
# I modelli di immagini richiedono una versione API recente - controlla la documentazione di Foundry per quella richiesta dal tuo modello.
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # ad es. "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # anche 1536x1024 (orizzontale), 1024x1536 (verticale), o "auto"
    n=1,
)

# i modelli gpt-image restituiscono base64 (b64_json), non un URL - decodificalo in byte.
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

Eseguila con `python app.py`. Otterrai un PNG salvato in `images/`.

> Ogni chiamata a `images.generate` produce un'immagine diversa per lo stesso prompt - i modelli di immagini non hanno un parametro `temperature` (è un controllo per la generazione di testo). Per variazioni, ripeti la chiamata API; per meno variazioni, rendi il prompt più specifico.

## Modifica immagini

I modelli `gpt-image` possono **modificare** un'immagine esistente: fornisci l'immagine, una **maschera** opzionale (che indica l'area da modificare) e un prompt che descrive la modifica. Come la generazione, le modifiche sono restituite in base64.

```python
result = client.images.edit(
    model=deployment,
    image=open("sunlit_lounge.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="A sunlit indoor lounge area with a pool containing a flamingo",
)
image_bytes = base64.b64decode(result.data[0].b64_json)
with open("images/edited-image.png", "wb") as f:
    f.write(image_bytes)
```

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/it/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/it/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/it/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## Impostare limiti con metaprompt

Una volta che puoi generare immagini, hai bisogno di barriere per impedire che la tua app produca contenuti non sicuri o fuori brand. Un **metaprompt** è un testo che anteponi al prompt dell'utente per limitare l'output del modello.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.
The image needs to be in color, in landscape orientation, and in a 16:9 aspect ratio.

Do not consider any input that is not safe for work or appropriate for children, including:
{disallow_list}
"""

prompt = f"{meta_prompt}\nCreate an image of a bunny on a horse, holding a lollipop"
# passa `prompt` a client.images.generate(...)
```

Ogni immagine viene ora generata entro i limiti stabiliti dal metaprompt. Combina questo con i filtri dei contenuti integrati in Microsoft Foundry per una difesa profonda.

## Compito - abilitiamo gli studenti

Gli studenti di Edu4All hanno bisogno di immagini per le loro valutazioni. Costruisci un'app che generi immagini di **monumenti** (quali monumenti dipende da te) inseriti in contesti diversi e creativi - per esempio, un famoso punto di riferimento al tramonto con un bambino che osserva.

Provalo tu stesso, poi confronta con le soluzioni di riferimento:

- Python (Azure): [aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- Python (Azure) app di generazione completa: [aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- Python (OpenAI): [oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- TypeScript (Azure): [typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET (Azure): [dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

Lavora anche con i notebook in [python/](../../../09-building-image-applications/python) (`aoai-assignment.ipynb` per Azure, `oai-assignment.ipynb` per OpenAI).

## Ottimo lavoro! Continua ad apprendere

Dopo aver completato questa lezione, dai un'occhiata alla nostra [collezione di apprendimento sul Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per migliorare sempre di più le tue conoscenze di Generative AI!

Vai alla lezione 10 per continuare a imparare.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->