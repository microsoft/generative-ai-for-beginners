<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-06-25T23:11:57+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "hr"
}
-->
# Okviri za neuronske mreže

Kao što smo već naučili, kako bismo mogli učinkovito trenirati neuronske mreže, trebamo učiniti dvije stvari:

* Raditi s tenzorima, npr. množiti, zbrajati i izračunavati neke funkcije kao što su sigmoid ili softmax
* Izračunati gradijente svih izraza kako bismo mogli provesti optimizaciju spuštanjem po gradijentu

Iako knjižnica `numpy` može obaviti prvi dio, trebamo neki mehanizam za izračun gradijenata. U našem okviru koji smo razvili u prethodnom odjeljku morali smo ručno programirati sve funkcije derivacija unutar metode `backward`, koja provodi povratnu propagaciju. Idealno, okvir bi nam trebao omogućiti izračun gradijenata *bilo kojeg izraza* koji možemo definirati.

Druga važna stvar je mogućnost izvođenja izračuna na GPU-u ili bilo kojim drugim specijaliziranim jedinicama za izračun, kao što je TPU. Trening dubokih neuronskih mreža zahtijeva *puno* izračuna, i mogućnost paralelizacije tih izračuna na GPU-ima je vrlo važna.

> ✅ Pojam 'paralelizacija' znači distribuiranje izračuna na više uređaja.

Trenutno su dva najpopularnija okvira za neuronske mreže: TensorFlow i PyTorch. Oba pružaju niskorazinski API za rad s tenzorima na CPU-u i GPU-u. Povrh niskorazinskog API-ja, postoji i visokorazinski API, nazvan Keras i PyTorch Lightning.

Niskorazinski API | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
Visokorazinski API| Keras| Pytorch

**Niskorazinski API-ji** u oba okvira omogućuju vam izgradnju takozvanih **računskih grafova**. Ovaj graf definira kako izračunati izlaz (obično funkciju gubitka) s danim ulaznim parametrima, i može se poslati na izračun na GPU, ako je dostupan. Postoje funkcije za diferenciranje ovog računalnog grafa i izračun gradijenata, koji se zatim mogu koristiti za optimizaciju parametara modela.

**Visokorazinski API-ji** uglavnom smatraju neuronske mreže kao **slijed slojeva**, i čine izgradnju većine neuronskih mreža puno lakšom. Trening modela obično zahtijeva pripremu podataka, a zatim pozivanje funkcije `fit` za obavljanje posla.

Visokorazinski API omogućuje vam vrlo brzo konstruiranje tipičnih neuronskih mreža bez brige o puno detalja. Istovremeno, niskorazinski API nudi puno više kontrole nad procesom treninga, i stoga se često koristi u istraživanju, kada se bavite novim arhitekturama neuronskih mreža.

Također je važno razumjeti da možete koristiti oba API-ja zajedno, npr. možete razviti vlastitu arhitekturu sloja mreže koristeći niskorazinski API, a zatim ga koristiti unutar veće mreže konstruirane i trenirane s visokorazinskim API-jem. Ili možete definirati mrežu koristeći visokorazinski API kao slijed slojeva, a zatim koristiti vlastitu niskorazinsku petlju treninga za izvođenje optimizacije. Oba API-ja koriste iste osnovne koncepte i dizajnirani su da dobro rade zajedno.

## Učenje

U ovom tečaju nudimo većinu sadržaja za PyTorch i TensorFlow. Možete odabrati svoj preferirani okvir i proći samo kroz odgovarajuće bilježnice. Ako niste sigurni koji okvir odabrati, pročitajte neke rasprave na internetu o **PyTorch vs. TensorFlow**. Također možete pogledati oba okvira kako biste dobili bolji uvid.

Gdje god je moguće, koristit ćemo visokorazinske API-je radi jednostavnosti. Međutim, vjerujemo da je važno razumjeti kako neuronske mreže rade od temelja, stoga na početku počinjemo raditi s niskorazinskim API-jem i tenzorima. Međutim, ako želite brzo krenuti i ne želite provoditi puno vremena učeći te detalje, možete ih preskočiti i odmah prijeći na bilježnice s visokorazinskim API-jem.

## ✍️ Vježbe: Okviri

Nastavite svoje učenje u sljedećim bilježnicama:

Niskorazinski API | TensorFlow+Keras Bilježnica | PyTorch
--------------|-------------------------------------|--------------------------------
Visokorazinski API| Keras | *PyTorch Lightning*

Nakon što savladate okvire, ponovimo pojam prenaučenosti.

# Prenaučenost

Prenaučenost je izuzetno važan koncept u strojnom učenju i vrlo je važno pravilno ga razumjeti!

Razmotrite sljedeći problem aproksimacije 5 točaka (predstavljenih s `x` na grafovima dolje):

!linear | prenaučenost
-------------------------|--------------------------
**Linearni model, 2 parametra** | **Nelinearni model, 7 parametara**
Pogreška treninga = 5.3 | Pogreška treninga = 0
Pogreška validacije = 5.1 | Pogreška validacije = 20

* S lijeve strane vidimo dobru aproksimaciju ravnom linijom. Budući da je broj parametara primjeren, model ispravno shvaća raspodjelu točaka.
* S desne strane model je previše moćan. Budući da imamo samo 5 točaka, a model ima 7 parametara, može se prilagoditi tako da prolazi kroz sve točke, čineći pogrešku treninga nula. Međutim, to sprječava model da razumije ispravan uzorak podataka, stoga je pogreška validacije vrlo visoka.

Vrlo je važno postići ispravnu ravnotežu između bogatstva modela (broja parametara) i broja uzoraka treninga.

## Zašto dolazi do prenaučenosti

  * Nedovoljno podataka za trening
  * Previše moćan model
  * Previše šuma u ulaznim podacima

## Kako otkriti prenaučenost

Kao što možete vidjeti iz gornjeg grafa, prenaučenost se može otkriti vrlo niskom pogreškom treninga i visokom pogreškom validacije. Obično tijekom treninga vidimo kako se pogreške treninga i validacije smanjuju, a zatim u nekom trenutku pogreška validacije može prestati opadati i početi rasti. Ovo će biti znak prenaučenosti i pokazatelj da bismo vjerojatno trebali zaustaviti trening u tom trenutku (ili barem napraviti snimku modela).

## Kako spriječiti prenaučenost

Ako primijetite da dolazi do prenaučenosti, možete učiniti jedno od sljedećeg:

 * Povećajte količinu podataka za trening
 * Smanjite složenost modela
 * Koristite neku tehniku regularizacije, kao što je Dropout, koju ćemo kasnije razmotriti.

## Prenaučenost i kompromis pristranosti-varijance

Prenaučenost je zapravo slučaj općenitijeg problema u statistici nazvanog kompromis pristranosti-varijance. Ako razmotrimo moguće izvore pogreške u našem modelu, možemo vidjeti dvije vrste pogrešaka:

* **Pogreške pristranosti** uzrokovane su time što naš algoritam nije u stanju pravilno uhvatiti odnos između podataka za trening. To može biti posljedica činjenice da naš model nije dovoljno moćan (**podnaučenost**).
* **Pogreške varijance**, koje su uzrokovane time što model aproksimira šum u ulaznim podacima umjesto značajnog odnosa (**prenaučenost**).

Tijekom treninga pogreška pristranosti se smanjuje (kako naš model uči aproksimirati podatke), a pogreška varijance se povećava. Važno je zaustaviti trening - bilo ručno (kada otkrijemo prenaučenost) ili automatski (uvođenjem regularizacije) - kako bismo spriječili prenaučenost.

## Zaključak

U ovoj lekciji naučili ste o razlikama između različitih API-ja za dva najpopularnija AI okvira, TensorFlow i PyTorch. Osim toga, naučili ste o vrlo važnoj temi, prenaučenosti.

## 🚀 Izazov

U pratećim bilježnicama pronaći ćete 'zadaci' na dnu; prođite kroz bilježnice i dovršite zadatke.

## Pregled i samostalno učenje

Istražite sljedeće teme:

- TensorFlow
- PyTorch
- Prenaučenost

Postavite si sljedeća pitanja:

- Koja je razlika između TensorFlowa i PyTorcha?
- Koja je razlika između prenaučenosti i podnaučenosti?

## Zadatak

U ovom laboratoriju traži se da riješite dva problema klasifikacije koristeći jednostruke i višeslojne potpuno povezane mreže koristeći PyTorch ili TensorFlow.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako se trudimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne odgovaramo za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.