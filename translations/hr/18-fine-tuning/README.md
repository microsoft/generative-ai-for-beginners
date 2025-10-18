<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "807f0d9fc1747e796433534e1be6a98a",
  "translation_date": "2025-10-18T01:34:32+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "hr"
}
-->
[![Open Source Models](../../../translated_images/18-lesson-banner.f30176815b1a5074fce9cceba317720586caa99e24001231a92fd04eeb54a121.hr.png)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Fino podešavanje vašeg LLM-a

Korištenje velikih jezičnih modela za izgradnju generativnih AI aplikacija donosi nove izazove. Ključno pitanje je osigurati kvalitetu odgovora (točnost i relevantnost) u sadržaju koji model generira za određeni korisnički zahtjev. U prethodnim lekcijama raspravljali smo o tehnikama poput oblikovanja upita (prompt engineering) i generacije uz prošireno pretraživanje, koje pokušavaju riješiti problem _modificiranjem ulaznog upita_ postojećem modelu.

U današnjoj lekciji raspravljamo o trećoj tehnici, **fino podešavanje**, koja pokušava riješiti izazov _ponovnim treniranjem samog modela_ s dodatnim podacima. Zaronimo u detalje.

## Ciljevi učenja

Ova lekcija uvodi koncept finog podešavanja unaprijed treniranih jezičnih modela, istražuje prednosti i izazove ovog pristupa te pruža smjernice o tome kada i kako koristiti fino podešavanje za poboljšanje performansi vaših generativnih AI modela.

Na kraju ove lekcije trebali biste moći odgovoriti na sljedeća pitanja:

- Što je fino podešavanje jezičnih modela?
- Kada i zašto je fino podešavanje korisno?
- Kako mogu fino podesiti unaprijed trenirani model?
- Koja su ograničenja finog podešavanja?

Spremni? Krenimo.

## Ilustrirani vodič

Želite li dobiti širu sliku o tome što ćemo pokriti prije nego što zaronimo u detalje? Pogledajte ovaj ilustrirani vodič koji opisuje put učenja za ovu lekciju - od učenja osnovnih pojmova i motivacije za fino podešavanje, do razumijevanja procesa i najboljih praksi za izvršavanje zadatka finog podešavanja. Ovo je fascinantna tema za istraživanje, stoga ne zaboravite provjeriti [Resurse](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) za dodatne poveznice koje će podržati vaše samostalno učenje!

![Ilustrirani vodič za fino podešavanje jezičnih modela](../../../translated_images/18-fine-tuning-sketchnote.11b21f9ec8a703467a120cb79a28b5ac1effc8d8d9d5b31bbbac6b8640432e14.hr.png)

## Što je fino podešavanje jezičnih modela?

Po definiciji, veliki jezični modeli su _unaprijed trenirani_ na velikim količinama teksta prikupljenog iz raznih izvora, uključujući internet. Kao što smo naučili u prethodnim lekcijama, potrebne su nam tehnike poput _oblikovanja upita_ i _generacije uz prošireno pretraživanje_ kako bismo poboljšali kvalitetu odgovora modela na korisnička pitanja ("upite").

Popularna tehnika oblikovanja upita uključuje davanje modelu više smjernica o tome što se očekuje u odgovoru, bilo pružanjem _uputa_ (eksplicitne smjernice) ili _davanjem nekoliko primjera_ (implicitne smjernice). To se naziva _učenje s nekoliko primjera_ (few-shot learning), ali ima dva ograničenja:

- Ograničenja broja tokena u modelu mogu ograničiti broj primjera koje možete dati i smanjiti učinkovitost.
- Troškovi tokena mogu učiniti skupo dodavanje primjera svakom upitu i ograničiti fleksibilnost.

Fino podešavanje je uobičajena praksa u sustavima strojnog učenja gdje uzimamo unaprijed trenirani model i ponovno ga treniramo s novim podacima kako bismo poboljšali njegovu izvedbu za određeni zadatak. U kontekstu jezičnih modela, možemo fino podesiti unaprijed trenirani model _s pažljivo odabranim skupom primjera za određeni zadatak ili domenu primjene_ kako bismo stvorili **prilagođeni model** koji može biti precizniji i relevantniji za taj specifični zadatak ili domenu. Dodatna prednost finog podešavanja je da može smanjiti broj potrebnih primjera za učenje s nekoliko primjera - smanjujući korištenje tokena i povezane troškove.

## Kada i zašto bismo trebali fino podešavati modele?

U _ovom_ kontekstu, kada govorimo o finom podešavanju, mislimo na **supervizirano** fino podešavanje gdje se ponovno treniranje provodi **dodavanjem novih podataka** koji nisu bili dio originalnog skupa podataka za treniranje. To se razlikuje od pristupa nesuperviziranog finog podešavanja gdje se model ponovno trenira na originalnim podacima, ali s različitim hiperparametrima.

Ključno je zapamtiti da je fino podešavanje napredna tehnika koja zahtijeva određenu razinu stručnosti kako bi se postigli željeni rezultati. Ako se ne provede ispravno, možda neće pružiti očekivana poboljšanja, pa čak može i pogoršati performanse modela za vašu ciljanu domenu.

Dakle, prije nego što naučite "kako" fino podesiti jezične modele, trebate znati "zašto" biste trebali krenuti tim putem i "kada" započeti proces finog podešavanja. Počnite postavljanjem ovih pitanja:

- **Slučaj upotrebe**: Koji je vaš _slučaj upotrebe_ za fino podešavanje? Koji aspekt trenutnog unaprijed treniranog modela želite poboljšati?
- **Alternative**: Jeste li pokušali _druge tehnike_ za postizanje željenih rezultata? Koristite ih za stvaranje osnovne usporedbe.
  - Oblikovanje upita: Pokušajte s tehnikama poput učenja s nekoliko primjera koristeći primjere relevantnih odgovora na upite. Procijenite kvalitetu odgovora.
  - Generacija uz prošireno pretraživanje: Pokušajte proširiti upite rezultatima pretraživanja vaših podataka. Procijenite kvalitetu odgovora.
- **Troškovi**: Jeste li identificirali troškove finog podešavanja?
  - Mogućnost podešavanja - je li unaprijed trenirani model dostupan za fino podešavanje?
  - Napor - za pripremu podataka za treniranje, evaluaciju i poboljšanje modela.
  - Računalni resursi - za pokretanje poslova finog podešavanja i implementaciju fino podešenog modela.
  - Podaci - pristup dovoljnim kvalitetnim primjerima za utjecaj finog podešavanja.
- **Prednosti**: Jeste li potvrdili prednosti finog podešavanja?
  - Kvaliteta - je li fino podešeni model nadmašio osnovnu usporedbu?
  - Trošak - smanjuje li korištenje tokena pojednostavljivanjem upita?
  - Proširivost - možete li ponovno koristiti osnovni model za nove domene?

Odgovaranjem na ova pitanja trebali biste moći odlučiti je li fino podešavanje pravi pristup za vaš slučaj upotrebe. Idealno, pristup je valjan samo ako prednosti nadmašuju troškove. Kada odlučite nastaviti, vrijeme je da razmislite o tome _kako_ možete fino podesiti unaprijed trenirani model.

Želite li dobiti više uvida u proces donošenja odluka? Pogledajte [Fino podešavanje ili ne fino podešavanje](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Kako možemo fino podesiti unaprijed trenirani model?

Za fino podešavanje unaprijed treniranog modela, trebate imati:

- unaprijed trenirani model za fino podešavanje
- skup podataka za fino podešavanje
- okruženje za treniranje za pokretanje posla finog podešavanja
- okruženje za hosting za implementaciju fino podešenog modela

## Fino podešavanje u praksi

Sljedeći resursi pružaju korak-po-korak vodiče koji vas vode kroz stvarni primjer korištenja odabranog modela s pažljivo odabranim skupom podataka. Za rad kroz ove vodiče, trebate račun na određenom pružatelju usluga, zajedno s pristupom relevantnom modelu i skupovima podataka.

| Pružatelj     | Vodič                                                                                                                                                                       | Opis                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI        | [Kako fino podesiti chat modele](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)           | Naučite fino podesiti `gpt-35-turbo` za određenu domenu ("asistent za recepte") pripremom podataka za treniranje, pokretanjem posla finog podešavanja i korištenjem fino podešenog modela za zaključivanje.                                                                                                                                                                                                                     |
| Azure OpenAI  | [GPT 3.5 Turbo vodič za fino podešavanje](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Naučite fino podesiti model `gpt-35-turbo-0613` **na Azureu** poduzimanjem koraka za kreiranje i učitavanje podataka za treniranje, pokretanje posla finog podešavanja. Implementirajte i koristite novi model.                                                                                                                                                                                                                                                        |
| Hugging Face  | [Fino podešavanje LLM-a s Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                         | Ovaj blog post vodi vas kroz fino podešavanje _otvorenog LLM-a_ (npr. `CodeLlama 7B`) koristeći [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) biblioteku i [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst]) s otvorenim [skupovima podataka](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) na Hugging Face. |
|               |                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain  | [Fino podešavanje LLM-a s AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                   | AutoTrain (ili AutoTrain Advanced) je python biblioteka koju je razvio Hugging Face i omogućuje fino podešavanje za mnoge različite zadatke, uključujući fino podešavanje LLM-a. AutoTrain je rješenje bez koda, a fino podešavanje može se obaviti u vašem vlastitom oblaku, na Hugging Face Spaces ili lokalno. Podržava i web-bazirani GUI, CLI i treniranje putem yaml konfiguracijskih datoteka.                                           |
|               |                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Zadatak

Odaberite jedan od gore navedenih vodiča i prođite kroz njega. _Možda ćemo replicirati verziju ovih vodiča u Jupyter Notebooks u ovom repozitoriju samo za referencu. Molimo koristite izvorne izvore izravno kako biste dobili najnovije verzije_.

## Odlično! Nastavite s učenjem.

Nakon što završite ovu lekciju, pogledajte našu [Generative AI Learning kolekciju](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili unapređivati svoje znanje o generativnoj umjetnoj inteligenciji!

Čestitamo!! Završili ste posljednju lekciju iz v2 serije ovog tečaja! Nemojte prestati učiti i stvarati. \*\*Pogledajte [RESURSE](RESOURCES.md?WT.mc_id=academic-105485-koreyst) stranicu za popis dodatnih prijedloga samo za ovu temu.

Naša v1 serija lekcija također je ažurirana s više zadataka i koncepata. Stoga odvojite trenutak da osvježite svoje znanje - i molimo vas [podijelite svoja pitanja i povratne informacije](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) kako bismo poboljšali ove lekcije za zajednicu.

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.