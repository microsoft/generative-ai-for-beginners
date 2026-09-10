# Δημιουργία Εφαρμογών Γεννήτριας Εικόνας

[![Δημιουργία Εφαρμογών Γεννήτριας Εικόνας](../../../translated_images/el/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Υπάρχει περισσότερα στα LLM πέρα από τη γεννήτρια κειμένου. Μπορείτε επίσης να δημιουργήσετε εικόνες από περιγραφές κειμένου. Οι εικόνες ως μέσο είναι χρήσιμες σε MedTech, αρχιτεκτονική, τουρισμό, ανάπτυξη παιχνιδιών, μάρκετινγκ και άλλα. Σε αυτό το μάθημα εξετάζουμε τα σημερινά μοντέλα **GPT Image** και δημιουργούμε μια εφαρμογή γεννήτριας εικόνας.

## Εισαγωγή

Η γεννήτρια εικόνας σας επιτρέπει να μετατρέψετε ένα φυσικό γλωσσικό αίτημα σε εικόνα. Σε αυτό το μάθημα δουλεύουμε με την οικογένεια μοντέλων **`gpt-image`** της OpenAI - τη σημερινή γενιά μοντέλων εικόνας που διατίθενται στην **[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)** και στην πλατφόρμα OpenAI. Αυτά τα μοντέλα αντικαθιστούν τα παλαιότερα μοντέλα DALL·E (DALL·E 2/3 είναι παλαιάς μορφής).

Καθ’ όλη τη διάρκεια του μαθήματος χρησιμοποιούμε μια φανταστική startup, την **Edu4All**, που δημιουργεί εργαλεία μάθησης. Η ομάδα θέλει να δημιουργήσει εικονογραφήσεις για εργασίες και υλικό μελέτης.

## Στόχοι μάθησης

Μέχρι το τέλος του μαθήματος θα μπορείτε να:

- Εξηγήσετε τι είναι η γεννήτρια εικόνας και πού είναι χρήσιμη.
- Κατανοήσετε την οικογένεια μοντέλων `gpt-image` και πώς διαφέρει από τα παλαιά μοντέλα DALL·E.
- Δημιουργήσετε μια εφαρμογή γεννήτριας εικόνας σε Python (και TypeScript / .NET).
- Επεξεργαστείτε εικόνες και εφαρμόσετε ασφάλεια με metaprompts.

## Τι είναι η γεννήτρια εικόνας;

Τα μοντέλα γεννήτριας εικόνας δημιουργούν εικόνες από κείμενο. Τα σύγχρονα μοντέλα όπως το `gpt-image` βασίζονται σε τεχνικές μετασχηματιστών και διάχυσης: το μοντέλο μαθαίνει τη σχέση μεταξύ κειμένου και εικόνων κατά την εκπαίδευση, μετά, με δεδομένο ένα αίτημα, σταδιακά «καθαρίζει» τον τυχαίο θόρυβο σε μια εικόνα που ταιριάζει με την περιγραφή.

Δύο δημοφιλείς οικογένειες μοντέλων εικόνας είναι:

- **`gpt-image` (OpenAI)** - η τρέχουσα γενιά, που χρησιμοποιείται σε αυτό το μάθημα. Υποστηρίζει γεννήτρια εικόνας από κείμενο και επεξεργασία εικόνων (inpainting με μάσκα).
- **Midjourney** - ένα δημοφιλές τρίτο μοντέλο με τη δική του υπηρεσία και ροή εργασίας στο Discord.

> Παλιότερα μοντέλα εικόνας OpenAI - **DALL·E 2** και **DALL·E 3** - είναι παλαιάς μορφής. Το DALL·E 3 δεν είναι πλέον διαθέσιμο για νέες αναπτύξεις, και λειτουργίες όπως `create_variation` υπήρχαν μόνο στο DALL·E 2. Χρησιμοποιήστε τα μοντέλα `gpt-image` για νέες εφαρμογές.

### Ποιο μοντέλο `gpt-image` να χρησιμοποιήσω;

Στο Microsoft Foundry τα παρακάτω είναι **Γενικά Διαθέσιμα**:

| Μοντέλο | Σημειώσεις |
| --- | --- |
| **`gpt-image-2`** | Το πιο πρόσφατο και ικανό μοντέλο εικόνας - συνιστώμενο προεπιλεγμένο. |
| `gpt-image-1.5` | Γενικά διαθέσιμο; καλή ποιότητα με χαμηλότερο κόστος. |
| `gpt-image-1-mini` | Γενικά διαθέσιμο; ταχύτερο / χαμηλότερο κόστος. |
| `gpt-image-1` | Μόνο για δοκιμή. |

Ελέγχετε πάντα την τρέχουσα [λίστα μοντέλων εικόνας Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst) για διαθεσιμότητα και περιοχές.

> **Σημαντικό:** Τα μοντέλα `gpt-image` επιστρέφουν την παραγόμενη εικόνα ως **base64** (`b64_json`), όχι ως URL. Ο κώδικάς σας αποκωδικοποιεί τη συμβολοσειρά base64 σε bytes και τη σώζει - δεν υπάρχει URL εικόνας για λήψη.

## Ρυθμίσεις

Μπορείτε να τρέξετε τα παραδείγματα στην **Azure OpenAI στο Microsoft Foundry** (τα δείγματα `aoai-*`) ή στην **πλατφόρμα OpenAI** (τα δείγματα `oai-*`).

### 1. Δημιουργία και ανάπτυξη μοντέλου

Ακολουθήστε τον οδηγό [δημιουργίας πόρου](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) για να δημιουργήσετε έναν πόρο Microsoft Foundry, και στη συνέχεια αναπτύξτε ένα μοντέλο εικόνας - συνιστάται το **`gpt-image-2`**.

### 2. Ρυθμίστε το `.env` σας

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

Βρείτε αυτές τις τιμές στη σελίδα **Deployments** του πόρου σας στο [Foundry portal](https://ai.azure.com?WT.mc_id=academic-105485-koreyst).

### 3. Εγκαταστήστε τις βιβλιοθήκες

Δημιουργήστε ένα `requirements.txt`:

```text
python-dotenv
openai
pillow
```

Μετά δημιουργήστε και ενεργοποιήστε ένα virtual environment και εγκαταστήστε:

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Δημιουργία της εφαρμογής

Δημιουργήστε το `app.py` με τον παρακάτω κώδικα. Δημιουργεί μια εικόνα και την αποθηκεύει ως PNG.

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# Κατευθύνετε τον πελάτη στην πηγή Azure OpenAI (Microsoft Foundry) σας.
# Τα μοντέλα εικόνων απαιτούν πρόσφατη έκδοση API - ελέγξτε τα έγγραφα Foundry για την έκδοση που απαιτεί το μοντέλο σας.
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # π.χ. "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # επίσης 1536x1024 (οριζόντιο), 1024x1536 (κατακόρυφο), ή "auto"
    n=1,
)

# τα μοντέλα gpt-image επιστρέφουν base64 (b64_json), όχι URL - αποκωδικοποιήστε το σε bytes.
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

Τρέξτε το με `python app.py`. Θα λάβετε ένα αρχείο PNG αποθηκευμένο στο `images/`.

> Κάθε κλήση στο `images.generate` παράγει διαφορετική εικόνα για το ίδιο αίτημα - τα μοντέλα εικόνας δεν δέχονται παράμετρο `temperature` (που ελέγχει τη γεννήτρια κειμένου). Για ποικιλία καλέστε απλά την API ξανά· για λιγότερη ποικιλία, κάντε το αίτημά σας πιο συγκεκριμένο.

## Επεξεργασία εικόνων

Τα μοντέλα `gpt-image` μπορούν να **επεξεργαστούν** μια υπάρχουσα εικόνα: δώστε την εικόνα, μια προαιρετική **μάσκα** (που σηματοδοτεί την περιοχή προς αλλαγή), και ένα αίτημα που περιγράφει την αλλαγή. Όπως στη δημιουργία, οι επεξεργασίες επιστρέφονται ως base64.

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
  <img src="../../../translated_images/el/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/el/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/el/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## Ορισμός ορίων με metaprompts

Μόλις μπορείτε να δημιουργείτε εικόνες, χρειάζεστε κανόνες ασφάλειας ώστε η εφαρμογή σας να μην παράγει μη ασφαλές ή μη σύμφωνο με την εταιρεία περιεχόμενο. Ένα **metaprompt** είναι κείμενο που προσθέτετε πριν από το αίτημα χρήστη για να περιορίσετε την έξοδο του μοντέλου.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.
The image needs to be in color, in landscape orientation, and in a 16:9 aspect ratio.

Do not consider any input that is not safe for work or appropriate for children, including:
{disallow_list}
"""

prompt = f"{meta_prompt}\nCreate an image of a bunny on a horse, holding a lollipop"
# περάστε το `prompt` στο client.images.generate(...)
```

Κάθε εικόνα παράγεται τώρα εντός των ορίων που θέτει το metaprompt. Συνδυάστε αυτό με τα φίλτρα περιεχομένου που είναι ενσωματωμένα στο Microsoft Foundry για βαθιά προστασία.

## Εργασία - ας υποστηρίξουμε τους μαθητές

Οι μαθητές της Edu4All χρειάζονται εικόνες για τις αξιολογήσεις τους. Δημιουργήστε μια εφαρμογή που παράγει εικόνες **μνημείων** (ποια μνημεία περιλαμβάνονται είναι δική σας επιλογή) τοποθετημένα σε διαφορετικά, δημιουργικά περιβάλλοντα - για παράδειγμα, ένα διάσημο σημείο κατά το ηλιοβασίλεμα με ένα παιδί να κοιτάζει.

Δοκιμάστε το μόνοι σας και μετά συγκρίνετε με τις λύσεις αναφοράς:

- Python (Azure): [aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- Python (Azure) πλήρης εφαρμογή δημιουργίας: [aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- Python (OpenAI): [oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- TypeScript (Azure): [typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET (Azure): [dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

Επίσης επεξεργαστείτε τα σημειωματάρια στο [python/](../../../09-building-image-applications/python) (`aoai-assignment.ipynb` για Azure, `oai-assignment.ipynb` για OpenAI).

## Υπέροχη δουλειά! Συνεχίστε τη μάθησή σας

Μετά την ολοκλήρωση αυτού του μαθήματος, δείτε τη [συλλογή μάθησης Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) για να συνεχίσετε να αναβαθμίζετε τις γνώσεις σας στη Γεννητική AI!

Προχωρήστε στο μάθημα 10 για να συνεχίσετε τη μάθηση.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->