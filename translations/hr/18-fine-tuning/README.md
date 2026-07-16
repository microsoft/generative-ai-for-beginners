[![Open Source Models](../../../translated_images/hr/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Fino podešavanje vašeg LLM-a

Korištenje velikih jezičnih modela za izgradnju generativnih AI aplikacija donosi nove izazove. Ključno pitanje je osigurati kvalitetu odgovora (točnost i relevantnost) u sadržaju koji model generira za određeni korisnički zahtjev. U prethodnim lekcijama raspravljali smo o tehnikama poput inženjeringa prompta i generiranja uz podršku dohvatom koje pokušavaju riješiti problem _modificiranjem ulaznog prompta_ postojećeg modela.

U današnjoj lekciji raspravljamo o trećoj tehnici, **fino podešavanje**, koja pokušava riješiti izazov _ponovnim treniranjem samog modela_ dodatnim podacima. Krenimo u detalje.

## Ciljevi učenja

Ova lekcija uvodi pojam fino podešavanja za prethodno istrenirane jezične modele, istražuje prednosti i izazove ovog pristupa te pruža smjernice o tome kada i kako koristiti fino podešavanje za poboljšanje performansi vaših generativnih AI modela.

Na kraju ove lekcije trebali biste moći odgovoriti na sljedeća pitanja:

- Što je fino podešavanje za jezične modele?
- Kada i zašto je fino podešavanje korisno?
- Kako mogu fino podesiti prethodno istrenirani model?
- Koja su ograničenja fino podešavanja?

Spremni? Krenimo.

## Ilustrirani vodič

Želite li dobiti cjelokupnu sliku onoga što ćemo pokriti prije nego uđemo u detalje? Pogledajte ovaj ilustrirani vodič koji opisuje put učenja za ovu lekciju - od razumijevanja osnovnih pojmova i motivacije za fino podešavanje, do razumijevanja procesa i najboljih praksi za izvođenje zadatka fino podešavanja. Ovo je fascinantna tema za istraživanje, stoga ne zaboravite posjetiti [Resurse](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) za dodatne veze koje podržavaju vaše samostalno učenje!

![Ilustrirani vodič za fino podešavanje jezičnih modela](../../../translated_images/hr/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Što je fino podešavanje za jezične modele?

Po definiciji, veliki jezični modeli su _prethodno istrenirani_ na velikim količinama teksta koji potječu iz raznih izvora, uključujući internet. Kao što smo naučili u prethodnim lekcijama, potrebne su nam tehnike poput _inženjeringa prompta_ i _generiranja uz podršku dohvatom_ kako bismo poboljšali kvalitetu odgovora modela na korisnička pitanja ("prompte").

Popularna tehnika inženjeringa prompta uključuje davanje modelu više smjernica o tome što se očekuje u odgovoru putem _uputa_ (eksplicitne smjernice) ili _davanjem nekoliko primjera_ (implicitne smjernice). To se naziva _učenje s malo primjera (few-shot learning)_, ali ima dva ograničenja:

- Ograničenja tokena modela mogu ograničiti broj primjera koje možete dati i smanjiti učinkovitost.
- Troškovi tokena modela mogu učiniti dodavanje primjera za svaki prompt skupim i smanjiti fleksibilnost.

Fino podešavanje je uobičajena praksa u sustavima strojnog učenja gdje uzmemo prethodno istrenirani model i ponovno ga treniramo s novim podacima kako bismo poboljšali njegove performanse za određeni zadatak. U kontekstu jezičnih modela, možemo fino podesiti prethodno istrenirani model _uz odabrani skup primjera za određeni zadatak ili domen_ kako bismo stvorili **prilagođeni model** koji može biti točniji i relevantniji za taj specifični zadatak ili domenu. Dodatna korist fino podešavanja je što može smanjiti broj potrebnih primjera za učenje s malo primjera - smanjujući upotrebu tokena i povezane troškove.

## Kada i zašto bismo trebali fino podešavati modele?

U _ovom_ kontekstu, kada govorimo o fino podešavanju, mislimo na **nadzorovano** fino podešavanje gdje se ponovno treniranje izvodi dodavanjem **novih podataka** koji nisu bili dio izvornog skupa za treniranje. Ovo se razlikuje od nenadziranog fino podešavanja gdje se model ponovno trenira na izvornim podacima, ali s različitim hiperparametrima.

Ključna stvar koju treba zapamtiti je da je fino podešavanje napredna tehnika koja zahtijeva određeni stupanj stručnosti za postizanje željenih rezultata. Ako se ne izvede ispravno, može ne pružiti očekivana poboljšanja, pa čak i smanjiti performanse modela za vašu ciljanu domenu.

Dakle, prije nego što naučite "kako" fino podesiti jezične modele, morate znati "zašto" biste trebali krenuti tim putem i "kada" započeti proces fino podešavanja. Počnite tako što ćete si postaviti ova pitanja:

- **Primjena**: Koja je vaša _primjena_ za fino podešavanje? Koji aspekt trenutačnog prethodno istreniranog modela želite poboljšati?
- **Alternative**: Jeste li isprobali _druge tehnike_ za postizanje željenih rezultata? Koristite ih kao osnovu za usporedbu.
  - Inženjering prompta: Isprobajte tehnike poput few-shot promptinga s primjerima relevantnih odgovora. Procijenite kvalitetu odgovora.
  - Generiranje uz podršku dohvatom: Pokušajte pojačati promptove rezultatima pretraživanja vaših podataka. Procijenite kvalitetu odgovora.
- **Troškovi**: Jeste li identificirali troškove fino podešavanja?
  - Mogućnost podešavanja - je li prethodno istrenirani model dostupan za fino podešavanje?
  - Napor - za pripremu podataka za treniranje, evaluaciju i dorađivanje modela.
  - Računalna snaga - za izvođenje poslova fino podešavanja i implementaciju fino podešenog modela.
  - Podaci - pristup dovoljnim kvalitetnim primjerima za učinak fino podešavanja.
- **Prednosti**: Jeste li potvrdili prednosti fino podešavanja?
  - Kvaliteta - je li fino podešeni model nadmašio osnovni model?
  - Trošak - smanjuje li upotrebu tokena pojednostavljivanjem promptova?
  - Proširivost - možete li iskoristiti osnovni model za nove domene?

Odgovaranjem na ova pitanja trebali biste moći odlučiti je li fino podešavanje pravi pristup za vašu primjenu. Idealno, pristup je valjan samo ako prednosti nadmašuju troškove. Kad odlučite nastaviti, vrijeme je da razmislite _kako_ možete fino podesiti prethodno istrenirani model.

Želite li dodatne uvide u proces odlučivanja? Pogledajte [Fino podesiti ili ne fino podesiti](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Kako možemo fino podesiti prethodno istrenirani model?

Da biste fino podesili prethodno istrenirani model, morate imati:

- prethodno istrenirani model za fino podešavanje
- skup podataka za fino podešavanje
- okruženje za treniranje za izvođenje posla fino podešavanja
- okruženje za implementaciju fino podešenog modela

## Fino podešavanje u praksi

> **Napomena:** `gpt-35-turbo` / `gpt-3.5-turbo`, referencirani u nekim od donjih tutorijala, povučeni su za inferenciju i fino podešavanje. Ako danas započinjete novi posao fino podešavanja, ciljate model koji je trenutno podržan - na primjer `gpt-4o-mini` ili `gpt-4.1-mini`. Pogledajte [Popis modela za fino podešavanje](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) za trenutačni set modela koji se mogu fino podešavati. Koncepti i koraci u ovim tutorijalima i dalje vrijede.

Sljedeći resursi pružaju korak-po-korak tutorijale koji vas vode kroz stvarni primjer korištenja odabranog modela s odabranim skupom podataka. Za rad s ovim tutorijalima trebate račun kod određenog pružatelja, kao i pristup relevantnom modelu i skupovima podataka.

| Pružatelj | Tutorijal                                                                                                                                                                       | Opis                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI     | [Kako fino podesiti chat modele](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Naučite fino podešavati `gpt-35-turbo` za određenu domenu ("asistent za recepte") pripremajući podatke za treniranje, izvodeći posao fino podešavanja i koristeći fino podešeni model za inferenciju.                                                                                                                                                                                                                                  |
| Azure OpenAI | [Tutorijal fino podešavanja GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst) | Naučite kako fino podesiti model `gpt-35-turbo-0613` **na Azureu** poduzimajući korake za stvaranje i prijenos podataka za treniranje, pokretanje posla fino podešavanja. Implementirajte i koristite novi model.                                                                                                                                                                                                            |
| Hugging Face | [Fino podešavanje LLM-ova s Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Ovaj blog vodi vas kroz fino podešavanje _otvorenog LLM-a_ (npr. `CodeLlama 7B`) koristeći [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) biblioteku i [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) s otvorenim [skupovima podataka](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) na Hugging Face. |
|            |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 🤗 AutoTrain | [Fino podešavanje LLM-ova s AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (ili AutoTrain Advanced) je python biblioteka koju je razvio Hugging Face, a koja omogućuje fino podešavanje za mnoge različite zadatke, uključujući fino podešavanje LLM-ova. AutoTrain je rješenje bez koda i fino podešavanje se može obaviti u vašem oblaku, na Hugging Face Spaces ili lokalno. Podržava web GUI, CLI i treniranje putem yaml konfiguracijskih datoteka.                                                         |
|            |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 🦥 Unsloth | [Fino podešavanje LLM-ova s Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth je open-source okvir koji podržava fino podešavanje LLM-ova i učenje potkrepljenjem (RL). Unsloth pojednostavljuje lokalno treniranje, evaluaciju i implementaciju s gotovim [notebook-ovima](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Podržava i pretvaranje teksta u govor (TTS), BERT i multimodalne modele. Za početak pročitajte njihov korak-po-korak [Vodič za fino podešavanje LLM-ova](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                    |
|            |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
## Zadatak

Odaberite jedan od gore navedenih tutorijala i prođite kroz njega. _Možda ćemo replicirati verziju ovih tutorijala u Jupyter Notebook-ovima u ovom repozitoriju samo za referencu. Molimo koristite izvorne izvore izravno za najnovije verzije_.

## Odličan posao! Nastavite s učenjem.

Nakon što završite ovu lekciju, pogledajte našu [kolekciju za učenje generativne AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) za nastavak usavršavanja vašeg znanja o generativnoj AI!

Čestitamo!! Završili ste posljednju lekciju iz v2 serije ovog tečaja! Nemojte prestati učiti i graditi. \*\*Pogledajte [RESURSE](RESOURCES.md?WT.mc_id=academic-105485-koreyst) stranicu za popis dodatnih prijedloga samo za ovu temu.

Naša v1 serija lekcija također je ažurirana s više zadataka i koncepata. Pa odvojite minutu da osvježite svoje znanje - i molimo vas da [podijelite svoja pitanja i povratne informacije](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) kako bismo poboljšali ove lekcije za zajednicu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->