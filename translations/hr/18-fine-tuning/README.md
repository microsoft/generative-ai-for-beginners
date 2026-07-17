[![Open Source Models](../../../translated_images/hr/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Fino podešavanje vašeg LLM-a

Korištenje velikih jezičnih modela za izgradnju generativnih AI aplikacija donosi nove izazove. Ključno pitanje je osigurati kvalitetu odgovora (točnost i relevantnost) u sadržaju generiranom modelom za određeni korisnički zahtjev. U prethodnim lekcijama raspravljali smo o tehnikama poput prompt inženjeringa i generacije augmentirane dohvatom koje pokušavaju riješiti problem _modificiranjem ulaza prompta_ postojećem modelu.

U današnjoj lekciji raspravljamo o trećoj tehnici, **fino podešavanju**, koja pokušava riješiti izazov _ponovnim treniranjem samog modela_ s dodatnim podacima. Pogledajmo detalje.

## Ciljevi učenja

Ova lekcija uvodi pojam fino podešavanja za unaprijed trenirane jezične modele, istražuje prednosti i izazove ovog pristupa te daje smjernice kada i kako koristiti fino podešavanje za poboljšanje performansi vaših generativnih AI modela.

Na kraju ove lekcije trebali biste moći odgovoriti na sljedeća pitanja:

- Što je fino podešavanje za jezične modele?
- Kada i zašto je fino podešavanje korisno?
- Kako mogu fino podesiti unaprijed trenirani model?
- Koja su ograničenja fino podešavanja?

Spremni? Krenimo.

## Ilustrirani vodič

Želite li dobiti širu sliku o onome što ćemo pokriti prije nego što krenemo? Pogledajte ovaj ilustrirani vodič koji opisuje put učenja za ovu lekciju – od učenja osnovnih pojmova i motivacije za fino podešavanje do razumijevanja procesa i najboljih praksi za izvršenje zadatka fino podešavanja. Ovo je fascinantna tema za istraživanje, stoga ne zaboravite pogledati [Resurse](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) za dodatne poveznice koje podržavaju vaše samostalno učenje!

![Ilustrirani vodič za fino podešavanje jezičnih modela](../../../translated_images/hr/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Što je fino podešavanje za jezične modele?

Prema definiciji, veliki jezični modeli su _unaprijed trenirani_ na velikim količinama teksta preuzetog iz različitih izvora, uključujući internet. Kao što smo naučili u prethodnim lekcijama, trebamo tehnike poput _prompt inženjeringa_ i _generacije augmentirane dohvatom_ da bismo poboljšali kvalitetu modelovih odgovora na korisnička pitanja ("prompte").

Popularna tehnika prompt inženjeringa uključuje davanje modelu više smjernica o tome što se očekuje u odgovoru bilo davanjem _uputa_ (izravnih smjernica) ili _davanjem nekoliko primjera_ (neizravnih smjernica). Ovo se naziva _few-shot učenje_, ali ima dvije ograničenja:

- Ograničenja broja tokena modela mogu ograničiti broj primjera koje možete dati i ograničiti učinkovitost.
- Troškovi tokena modela mogu učiniti da je skupo dodavati primjere svakom promptu i ograničiti fleksibilnost.

Fino podešavanje je uobičajena praksa u sustavima strojnog učenja gdje uzmemo unaprijed trenirani model i ponovno ga treniramo s novim podacima kako bismo poboljšali njegovu izvedbu na određenom zadatku. U kontekstu jezičnih modela, možemo fino podesiti unaprijed trenirani model _s odabranim skupom primjera za određeni zadatak ili domenu primjene_ kako bismo stvorili **prilagođeni model** koji može biti točniji i relevantniji za taj specifični zadatak ili domenu. Dodatna korist fino podešavanja je što može smanjiti broj potrebnih primjera za few-shot učenje – smanjujući upotrebu tokena i povezane troškove.

## Kada i zašto bismo trebali fino podešavati modele?

U _ovom_ kontekstu, kada govorimo o fino podešavanju, mislimo na **nadzorovani** proces fino podešavanja gdje se ponovno treniranje obavlja **dodavanjem novih podataka** koji nisu bili dio izvornog skupa podataka za treniranje. To se razlikuje od nenadzorovanog pristupa fino podešavanja gdje se model trenira na izvornim podacima, ali s različitim hiperparametrima.

Ključna stvar koju treba zapamtiti je da je fino podešavanje napredna tehnika koja zahtijeva određeni nivo stručnosti da bi se postigli željeni rezultati. Ako se izvodi nepravilno, možda neće donijeti očekivana poboljšanja, pa čak može i pogoršati izvedbu modela za vašu ciljanju domenu.

Dakle, prije nego što naučite "kako" fino podesiti jezične modele, trebate znati "zašto" biste trebali odabrati ovaj put i "kada" započeti proces fino podešavanja. Počnite postavljati sebi ova pitanja:

- **Slučaj upotrebe**: Koji je vaš _slučaj upotrebe_ za fino podešavanje? Koji aspekt trenutnog unaprijed treniranog modela želite poboljšati?
- **Alternative**: Jeste li isprobali _druge tehnike_ za postizanje željenih rezultata? Koristite ih za stvaranje osnovne usporedbe.
  - Prompt inženjering: Isprobajte tehnike poput few-shot promptinga s primjerima relevantnih odgovora prompta. Procijenite kvalitetu odgovora.
  - Generacija augmentirana dohvatom: Isprobajte nadopunjavanje prompta s rezultatima pretraživanja vaših podataka. Procijenite kvalitetu odgovora.
- **Troškovi**: Jeste li identificirali troškove za fino podešavanje?
  - Mogućnost fino podešavanja - je li unaprijed trenirani model dostupan za fino podešavanje?
  - Napor - za pripremu podataka za treniranje, evaluaciju i pročišćavanje modela.
  - Računalni kapacitet - za izvođenje poslova fino podešavanja i postavljanje fino podešenog modela
  - Podaci - pristup dovoljnim kvalitetnim primjerima za utjecaj fino podešavanja
- **Prednosti**: Jeste li potvrdili prednosti fino podešavanja?
  - Kvaliteta - je li fino podešeni model nadmašio osnovni model?
  - Troškovi - smanjuje li se upotreba tokena pojednostavljivanjem prompta?
  - Proširivost - možete li osnovni model upotrijebiti za druge domene?

Odgovarajući na ova pitanja trebali biste moći odlučiti je li fino podešavanje pravi pristup za vašu uporabu. Idealno, pristup je opravdan samo ako prednosti nadmašuju troškove. Kada odlučite nastaviti, vrijeme je da razmislite _kako_ možete fino podesiti unaprijed trenirani model.

Želite li dobiti više uvida u proces odlučivanja? Pogledajte [Fino podesiti ili ne fino podesiti](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Kako možemo fino podesiti unaprijed trenirani model?

Da biste fino podesili unaprijed trenirani model, trebate imati:

- unaprijed trenirani model za fino podešavanje
- skup podataka za fino podešavanje
- okruženje za treniranje za izvođenje posla fino podešavanja
- okruženje za postavljanje kako biste postavili fino podešeni model

## Fino podešavanje na Microsoft Foundry

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) je mjesto gdje danas fino podešavate, postavljate i upravljate prilagođenim modelima na Azureu (objedinjuje ono što je nekad bio Azure OpenAI Studio i Azure AI Studio). Prije nego što započnete posao, korisno je razumjeti izbore koje Foundry pruža – i najbolje prakse koje platforma preporučuje. Ispod haube, Foundry koristi **LoRA (adaptacija niskog ranga)** za učinkovito fino podešavanje modela, što održava treniranje brzim i pristupačnijim nego treniranje svakog parametra.

### Korak 1: Odaberite tehniku treniranja

Foundry podržava tri tehnike fino podešavanja. **Počnite s SFT** - pokriva najširi raspon scenarija.

| Tehnika | Što radi | Kada je upotrijebiti |
| --- | --- | --- |
| **Nadzorovano fino podešavanje (SFT)** | Treninira na parovima ulaz/izlaz primjera kako bi model naučio proizvoditi željene odgovore. | Zadano za većinu zadataka: specijalizacija domene, izvedba zadatka, stil i ton, praćenje uputa i prilagodba jeziku. |
| **Izravna optimizacija preferencija (DPO)** | Uči iz parova _preferiranih i nepreferiranih_ odgovora kako bi uskladio izlaze s ljudskim preferencijama. | Poboljšava kvalitetu odgovora, sigurnost i usklađenost kada imate komparativne povratne informacije. |
| **Fine podešavanje s potkrepljenjem (RFT)** | Koristi nagradne signale od _ocjenjivača_ za optimizaciju složenog ponašanja pomoću učenja s potkrepljenjem. | Objektivne, zahtjevne domene zaključivanja (matematika, kemija, fizika) s jasnim točnim/zglobnim odgovorima. Zahtijeva više stručnosti u strojnome učenju. |

### Korak 2: Odaberite razinu treniranja

Foundry vam omogućuje odabir načina i mjesta izvođenja treniranja:

- **Standardno** - trenira se u regiji vašeg resursa i jamči boravak podataka u toj regiji. Koristite ga kada podaci moraju ostati u određenoj regiji.
- **Globalno** - jeftinije i brže stavljanje u red koristeći kapacitete izvan vaše regije (podatci i parametri se kopiraju u regiju treniranja). Dobro zadano kada boravak podataka nije zahtjev.
- **Razvojno** - najniži trošak, koristi neiskorišteni kapacitet bez jamstva latencije/SLA (poslovi mogu biti prekidani i nastavljeni). Idealno za eksperimentiranje.

### Korak 3: Odaberite osnovni model

Modeli koji se mogu fino podešavati uključuju OpenAI `gpt-4o-mini`, `gpt-4o`, `gpt-4.1`, `gpt-4.1-mini` i `gpt-4.1-nano` (SFT; obitelj 4o/4.1 također podržava DPO), modele za rezoniranje `o4-mini` i `gpt-5` (RFT), plus open-source modele poput `Ministral-3B`, `Qwen-32B`, `Llama-3.3-70B-Instruct` i `gpt-oss-20b` (SFT na Foundry resursima). Uvijek provjerite trenutni [Popis modela za fino podešavanje](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) za podržane metode, regije i dostupnost.

> Foundry nudi dvije modalitete: **serverless** (cijena po potrošnji, nema GPU kvote za upravljanje, OpenAI i odabrani modeli) i **upravljani računarski kapacitet** (donesite vlastite VM-ove preko Azure Machine Learning za najširi raspon modela). Većina korisnika trebala bi početi sa serverless.

### Najbolje prakse za Foundry

- **Prvo baza.** Izmjerite osnovni model s prompt inženjeringom i RAG-om _prije_ nego što fino podesite, kako biste mogli dokazati napredak.
- **Počnite s malim, zatim skalirajte.** Počnite s 50-100 kvalitetnih primjera za potvrdu pristupa, zatim povećajte na 500+ za produkciju. Kvaliteta nadmašuje količinu – odstranjujte primjere loše kvalitete.
- **Ispravno formatirajte podatke.** Datoteke za treniranje i validaciju moraju biti JSONL, UTF-8 **s BOM-om**, manje od 512 MB, koristeći format poruka chat-kompletiranja. Uvijek uključite datoteku za validaciju kako biste pratili prenaučenost.
- **Zadržite sistemski prompt za vrijeme izvođenja.** Koristite istu sistemsku poruku kada pozivate model kao i tijekom treninga.
- **Procijenite kontrolne točke – ne implementirajte slijepo zadnju.** Foundry čuva zadnje tri epohe kao implementabilne kontrolne točke; odaberite onu koja se najbolje generalizira gledajući `train_loss` / `valid_loss` i točnost tokena.
- **Mjerite trošak tokena uz kvalitetu** prilikom usporedbe fino podešenog modela i osnovnog.
- **Iterirajte kontinuiranim fino podešavanjem.** Možete dodatno fino podesiti već fino podešeni model na novim podacima (podržano za OpenAI modele).
- **Pazite na troškove hostinga.** Postavljeni prilagođeni model naplaćuje se po satu, a neaktivan deployment uklanja se nakon 15 dana – očistite što vam ne treba.

Prođite kroz kompletan vodič u [Prilagodba modela fino podešavanjem](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst), i pogledajte vodiče za [DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst) i [RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst) kada budete spremni za druge tehnike.

## Fino podešavanje u praksi

Sljedeći resursi pružaju korak-po-korak vodiče koji vas vode kroz stvarni primjer na trenutno podržanom modelu s odabranim skupom podataka. Da biste ih koristili, trebate račun kod određenog pružatelja usluge, uz pristup relevantnom modelu i skupovima podataka.

| Pružatelj usluge | Vodič                                                                                                                                                                      | Opis                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Kako fino podesiti chat modele](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Naučite kako fino podesiti nedavni OpenAI chat model za određenu domenu ("asistent za recepte") pripremom podataka za treniranje, pokretanjem posla fino podešavanja i korištenjem fino podešenog modela za izvođenje.                                                                                                                                                                                                                 |
| Microsoft Foundry | [Prilagodite model fino podešavanjem](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Naučite kako fino podesiti trenutno podržani model poput `gpt-4.1-mini` **na Azureu** pomoću Microsoft Foundry: pripremite i učitajte podatke za treniranje i validaciju, pokrenite posao fino podešavanja, zatim postavite i koristite novi model.                                                                                                                                                                                           |

| Hugging Face | [Finotuning LLM-ova s Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Ovaj blog vodi vas kroz finotuning _otvorenog LLM-a_ (npr.: `CodeLlama 7B`) koristeći [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) biblioteku i [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) uz otvorene [datasete](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) na Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Finotuning LLM-ova s AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (ili AutoTrain Advanced) je Python biblioteka koju je razvila Hugging Face i koja omogućava finotuning za mnogo različitih zadataka uključujući finotuning LLM-ova. AutoTrain je rješenje bez koda i finotuning se može obaviti u vašem oblaku, na Hugging Face Spaces ili lokalno. Podržava web-based GUI, CLI i treniranje putem YAML konfiguracijskih datoteka.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Finotuning LLM-ova s Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth je open-source okvir koji podržava finotuning LLM-a i reinforcement learning (RL). Unsloth pojednostavljuje lokalno treniranje, evaluaciju i implementaciju uz spremne [notebooke](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Također podržava text-to-speech (TTS), BERT i multimodalne modele. Za početak, pročitajte njihov vodič korak-po-korak [Finotuning LLM-ova](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Zadatak

Odaberite jedan od gore navedenih tutorijala i prođite kroz njih. _Možemo replicirati verziju ovih tutorijala u Jupyter Notebookovima u ovom repozitoriju samo za referencu. Molimo koristite originalne izvore direktno za najnovije verzije_.

## Odlično! Nastavite s učenjem.

Nakon dovršetka ove lekcije, pogledajte naš [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) da nastavite unapređivati svoje znanje o Generativnoj AI!

Čestitamo!! Završili ste završnu lekciju iz v2 serije ovog tečaja! Ne prestajte učiti i graditi. \*\*Pogledajte [RESURSE](RESOURCES.md?WT.mc_id=academic-105485-koreyst) stranicu za dodatne prijedloge samo za ovu temu.

Naša v1 serija lekcija također je ažurirana s više zadataka i koncepata. Ukratko obnovite znanje - i molimo [podijelite svoja pitanja i povratne informacije](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) kako bismo poboljšali ove lekcije za zajednicu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->