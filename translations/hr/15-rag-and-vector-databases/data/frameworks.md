<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-05-20T02:09:03+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "hr"
}
-->
# Okviri za neuronske mreže

Kao što smo već naučili, kako bismo mogli učinkovito trenirati neuronske mreže, trebamo učiniti dvije stvari:

* Raditi s tenzorima, npr. množiti, zbrajati i izračunavati neke funkcije poput sigmoida ili softmaxa
* Izračunati gradijente svih izraza kako bismo mogli provesti optimizaciju gradijentnim spuštanjem

Iako biblioteka `numpy` može obaviti prvi dio, trebamo neki mehanizam za izračunavanje gradijenata. U našem okviru koji smo razvili u prethodnom odjeljku morali smo ručno programirati sve funkcije derivacija unutar metode `backward`, koja provodi unazadno širenje pogreške. Idealno, okvir bi nam trebao pružiti mogućnost izračunavanja gradijenata *bilo kojeg izraza* koji možemo definirati.

Još jedna važna stvar je mogućnost izvođenja proračuna na GPU-u ili bilo kojoj drugoj specijaliziranoj jedinici za proračun, kao što je TPU. Trening dubokih neuronskih mreža zahtijeva *puno* proračuna, i mogućnost paraleliziranja tih proračuna na GPU-ima je vrlo važna.

> ✅ Pojam 'paralelizirati' znači raspodijeliti proračune na više uređaja.

Trenutno su dva najpopularnija okvira za neuronske mreže: TensorFlow i PyTorch. Oba pružaju niskorazinski API za rad s tenzorima na CPU-u i GPU-u. Povrh niskorazinskog API-ja, postoji i visokorazinski API, nazvan Keras i PyTorch Lightning.

Niskorazinski API | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
Visokorazinski API| Keras| PyTorch Lightning

**Niskorazinski API-ji** u oba okvira omogućuju vam izgradnju takozvanih **proračunskih grafova**. Ovaj graf definira kako izračunati izlaz (obično funkciju gubitka) s danim ulaznim parametrima i može se poslati na proračun na GPU, ako je dostupan. Postoje funkcije za diferenciranje ovog proračunskog grafa i izračunavanje gradijenata, koji se zatim mogu koristiti za optimizaciju parametara modela.

**Visokorazinski API-ji** uvelike smatraju neuronske mreže **sekvencom slojeva**, i čine konstruiranje većine neuronskih mreža puno lakšim. Trening modela obično zahtijeva pripremu podataka i zatim pozivanje funkcije `fit` da obavi posao.

Visokorazinski API omogućuje vam brzo konstruiranje tipičnih neuronskih mreža bez brige o puno detalja. Istovremeno, niskorazinski API nudi mnogo više kontrole nad procesom treniranja, i stoga se puno koristi u istraživanju, kada se bavite novim arhitekturama neuronskih mreža.

Također je važno razumjeti da možete koristiti oba API-ja zajedno, npr. možete razviti vlastitu arhitekturu slojeva mreže koristeći niskorazinski API, a zatim je koristiti unutar veće mreže konstruirane i trenirane s visokorazinskim API-jem. Ili možete definirati mrežu koristeći visokorazinski API kao sekvencu slojeva, a zatim koristiti vlastitu niskorazinsku petlju treniranja za provođenje optimizacije. Oba API-ja koriste iste osnovne koncepte i dizajnirana su da dobro surađuju.

## Učenje

U ovom tečaju nudimo većinu sadržaja i za PyTorch i za TensorFlow. Možete odabrati svoj preferirani okvir i proći samo odgovarajuće bilježnice. Ako niste sigurni koji okvir odabrati, pročitajte neke rasprave na internetu o **PyTorch vs. TensorFlow**. Također možete pogledati oba okvira kako biste bolje razumjeli.

Gdje god je moguće, koristit ćemo visokorazinske API-je radi jednostavnosti. Međutim, vjerujemo da je važno razumjeti kako neuronske mreže rade od temelja, stoga na početku počinjemo raditi s niskorazinskim API-jem i tenzorima. Međutim, ako želite brzo početi i ne želite trošiti puno vremena na učenje tih detalja, možete ih preskočiti i odmah prijeći na bilježnice s visokorazinskim API-jem.

## ✍️ Vježbe: Okviri

Nastavite svoje učenje u sljedećim bilježnicama:

Niskorazinski API | TensorFlow+Keras Bilježnica | PyTorch
--------------|-------------------------------------|--------------------------------
Visokorazinski API| Keras | *PyTorch Lightning*

Nakon što svladate okvire, ponovimo pojam prenaučenosti.

# Prenaučenost

Prenaučenost je izuzetno važan koncept u strojnom učenju, i vrlo je važno točno ga shvatiti!

Razmotrite sljedeći problem aproksimacije 5 točaka (predstavljenih s `x` na grafovima ispod):

!linear | prenaučenost
-------------------------|--------------------------
**Linearni model, 2 parametra** | **Nelinearni model, 7 parametara**
Greška na treningu = 5.3 | Greška na treningu = 0
Greška na validaciji = 5.1 | Greška na validaciji = 20

* S lijeve strane vidimo dobru aproksimaciju pravom linijom. Budući da je broj parametara adekvatan, model ispravno shvaća distribuciju točaka.
* S desne strane, model je previše moćan. Budući da imamo samo 5 točaka, a model ima 7 parametara, može se prilagoditi tako da prolazi kroz sve točke, čineći grešku na treningu 0. Međutim, to sprječava model da razumije ispravan uzorak podataka, stoga je greška na validaciji vrlo visoka.

Vrlo je važno postići ispravnu ravnotežu između bogatstva modela (broja parametara) i broja uzoraka za trening.

## Zašto dolazi do prenaučenosti

  * Nedovoljno podataka za trening
  * Previše moćan model
  * Previše šuma u ulaznim podacima

## Kako otkriti prenaučenost

Kao što možete vidjeti iz gornjeg grafa, prenaučenost se može otkriti vrlo niskom greškom na treningu i visokom greškom na validaciji. Normalno, tijekom treninga vidjet ćemo kako greške na treningu i validaciji počinju opadati, a zatim u nekom trenutku greška na validaciji može prestati opadati i početi rasti. Ovo će biti znak prenaučenosti i pokazatelj da bismo vjerojatno trebali zaustaviti trening u tom trenutku (ili barem napraviti snimku modela).

## Kako spriječiti prenaučenost

Ako vidite da dolazi do prenaučenosti, možete učiniti jedno od sljedećeg:

 * Povećajte količinu podataka za trening
 * Smanjite složenost modela
 * Koristite neku tehniku regularizacije, kao što je Dropout, koju ćemo razmotriti kasnije.

## Prenaučenost i kompromis pristranosti-varijance

Prenaučenost je zapravo slučaj općenitijeg problema u statistici nazvanog kompromis pristranosti-varijance. Ako razmotrimo moguće izvore pogreške u našem modelu, možemo vidjeti dvije vrste pogrešaka:

* **Pogreške pristranosti** uzrokovane su time što naš algoritam ne može ispravno uhvatiti odnos između podataka za trening. To može biti rezultat činjenice da naš model nije dovoljno moćan (**nedovoljno učenje**).
* **Pogreške varijance**, koje su uzrokovane time što model aproksimira šum u ulaznim podacima umjesto smislenog odnosa (**prenaučenost**).

Tijekom treninga, pogreška pristranosti opada (kako naš model uči aproksimirati podatke), a pogreška varijance raste. Važno je zaustaviti trening - bilo ručno (kada otkrijemo prenaučenost) ili automatski (uvođenjem regularizacije) - kako bismo spriječili prenaučenost.

## Zaključak

U ovoj lekciji naučili ste o razlikama između raznih API-ja za dva najpopularnija AI okvira, TensorFlow i PyTorch. Osim toga, naučili ste o vrlo važnoj temi, prenaučenosti.

## 🚀 Izazov

U pratećim bilježnicama pronaći ćete 'zadaci' na dnu; prođite kroz bilježnice i dovršite zadatke.

## Pregled i samostalno učenje

Istražite sljedeće teme:

- TensorFlow
- PyTorch
- Prenaučenost

Postavite si sljedeća pitanja:

- Koja je razlika između TensorFlow i PyTorch?
- Koja je razlika između prenaučenosti i nedovoljnog učenja?

## Zadatak

U ovom laboratoriju traži se da riješite dva problema klasifikacije koristeći jednostruke i višeslojne potpuno povezane mreže koristeći PyTorch ili TensorFlow.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne odgovaramo za nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.