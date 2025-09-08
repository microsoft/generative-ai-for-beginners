<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-07-09T16:38:08+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "hr"
}
-->
# Neural Network Frameworks

Kao što smo već naučili, da bismo mogli učinkovito trenirati neuronske mreže, potrebno je napraviti dvije stvari:

* Raditi s tenzorima, npr. množiti, zbrajati i izračunavati funkcije poput sigmoid ili softmax
* Izračunati gradijente svih izraza kako bismo mogli provesti optimizaciju gradijentnim spustom

Iako `numpy` biblioteka može obaviti prvi dio, potrebna nam je mehanika za izračun gradijenata. U našem okviru koji smo razvili u prethodnom poglavlju morali smo ručno programirati sve funkcije derivacija unutar metode `backward`, koja provodi backpropagation. Idealno bi bilo da nam okvir omogući izračun gradijenata *bilo kojeg izraza* koji definiramo.

Još jedna važna stvar je mogućnost izvođenja izračuna na GPU-u ili drugim specijaliziranim računalnim jedinicama, poput TPU-a. Trening dubokih neuronskih mreža zahtijeva *puno* izračuna, a mogućnost paralelizacije tih izračuna na GPU-ima je vrlo važna.

> ✅ Pojam 'paralelizirati' znači raspodijeliti izračune na više uređaja.

Trenutno su dva najpopularnija okvira za neuronske mreže: TensorFlow i PyTorch. Oba nude niskorazinski API za rad s tenzorima na CPU-u i GPU-u. Iznad niskorazinskog API-ja nalaze se i viši API-ji, nazvani Keras i PyTorch Lightning.

Niskorazinski API | TensorFlow | PyTorch
-----------------|------------|---------
Višerazinski API | Keras      | PyTorch

**Niskorazinski API-ji** u oba okvira omogućuju izgradnju tzv. **računalnih grafova**. Taj graf definira kako izračunati izlaz (obično funkciju gubitka) za zadane ulazne parametre, i može se poslati na izračun na GPU ako je dostupan. Postoje funkcije za diferenciranje tog računalnog grafa i izračun gradijenata, koji se potom koriste za optimizaciju parametara modela.

**Višerazinski API-ji** tretiraju neuronske mreže kao **niz slojeva** i znatno olakšavaju izgradnju većine neuronskih mreža. Trening modela obično zahtijeva pripremu podataka, a zatim pozivanje funkcije `fit` koja obavlja trening.

Višerazinski API omogućuje brzo sastavljanje tipičnih neuronskih mreža bez brige o mnogim detaljima. Istovremeno, niskorazinski API pruža puno veću kontrolu nad procesom treniranja, zbog čega se često koristi u istraživanjima i radu s novim arhitekturama neuronskih mreža.

Važno je razumjeti da se oba API-ja mogu koristiti zajedno, npr. možete razviti vlastitu arhitekturu sloja koristeći niskorazinski API, a zatim je koristiti unutar veće mreže sastavljene i trenirane višerazinskim API-jem. Ili možete definirati mrežu kao niz slojeva višerazinskim API-jem, a zatim koristiti vlastitu niskorazinsku petlju treniranja za optimizaciju. Oba API-ja dijele iste osnovne koncepte i dizajnirani su da dobro surađuju.

## Učenje

U ovom tečaju nudimo većinu sadržaja za PyTorch i TensorFlow. Možete odabrati okvir koji vam više odgovara i pratiti samo pripadajuće bilježnice. Ako niste sigurni koji okvir odabrati, pročitajte rasprave na internetu o **PyTorch vs. TensorFlow**. Također možete pogledati oba okvira kako biste bolje razumjeli razlike.

Kad god je moguće, koristit ćemo višerazinske API-je radi jednostavnosti. No smatramo da je važno razumjeti kako neuronske mreže funkcioniraju od samih početaka, pa stoga u početku radimo s niskorazinskim API-jem i tenzorima. Ako želite brzo krenuti i ne želite trošiti puno vremena na detalje, možete preskočiti taj dio i odmah prijeći na bilježnice s višerazinskim API-jem.

## ✍️ Vježbe: Frameworks

Nastavite s učenjem u sljedećim bilježnicama:

Niskorazinski API | TensorFlow+Keras bilježnica | PyTorch
-----------------|-------------------------------|---------
Višerazinski API | Keras                         | *PyTorch Lightning*

Nakon što savladate okvire, ponovimo pojam overfittinga.

# Overfitting

Overfitting je iznimno važan pojam u strojnome učenju i važno ga je pravilno razumjeti!

Razmotrimo problem aproksimacije 5 točaka (označenih s `x` na donjim grafovima):

!linear | overfit
-------------------------|--------------------------
**Linearni model, 2 parametra** | **Nelinearni model, 7 parametara**
Greška na treningu = 5.3 | Greška na treningu = 0
Greška na validaciji = 5.1 | Greška na validaciji = 20

* S lijeve strane vidimo dobru aproksimaciju pravom linijom. Budući da je broj parametara primjeren, model dobro hvata raspored točaka.
* S desne strane model je premoćan. Budući da imamo samo 5 točaka, a model ima 7 parametara, može se prilagoditi tako da prođe kroz sve točke, čineći grešku na treningu 0. Međutim, to sprječava model da razumije pravi obrazac podataka, zbog čega je greška na validaciji vrlo visoka.

Vrlo je važno pronaći pravi balans između složenosti modela (broja parametara) i broja uzoraka za trening.

## Zašto dolazi do overfittinga

  * Nedovoljno podataka za trening
  * Premoćan model
  * Previše šuma u ulaznim podacima

## Kako otkriti overfitting

Kao što se vidi na gornjem grafu, overfitting se može prepoznati po vrlo niskoj grešci na treningu i visokoj grešci na validaciji. Tijekom treniranja obično vidimo da se greške na treningu i validaciji smanjuju, a zatim u nekom trenutku greška na validaciji prestane padati i počne rasti. To je znak overfittinga i pokazatelj da bismo vjerojatno trebali prekinuti treniranje u tom trenutku (ili barem napraviti snimku modela).

overfitting

## Kako spriječiti overfitting

Ako primijetite da dolazi do overfittinga, možete učiniti jedno od sljedećeg:

 * Povećati količinu podataka za trening
 * Smanjiti složenost modela
 * Koristiti neku tehniku regularizacije, poput Dropout-a, koju ćemo kasnije razmotriti.

## Overfitting i kompromis između pristranosti i varijance

Overfitting je zapravo poseban slučaj općeg problema u statistici nazvanog kompromis između pristranosti i varijance (Bias-Variance Tradeoff). Ako razmotrimo moguće izvore pogreške u našem modelu, možemo razlikovati dvije vrste pogrešaka:

* **Pogreške pristranosti (Bias errors)** nastaju kada naš algoritam ne može pravilno uhvatiti odnos u podacima za trening. To može biti zato što model nije dovoljno moćan (**underfitting**).
* **Pogreške varijance (Variance errors)** nastaju kada model aproksimira šum u ulaznim podacima umjesto stvarnog odnosa (**overfitting**).

Tijekom treniranja, pogreška pristranosti opada (kako model uči podatke), a pogreška varijance raste. Važno je prekinuti treniranje – ručno (kad otkrijemo overfitting) ili automatski (uvođenjem regularizacije) – kako bismo spriječili overfitting.

## Zaključak

U ovoj lekciji ste naučili o razlikama između različitih API-ja za dva najpopularnija AI okvira, TensorFlow i PyTorch. Također ste upoznati s vrlo važnom temom, overfittingom.

## 🚀 Izazov

U pratećim bilježnicama naći ćete 'zadace' na dnu; radite kroz bilježnice i dovršite zadatke.

## Pregled i samostalno učenje

Istražite sljedeće teme:

- TensorFlow
- PyTorch
- Overfitting

Postavite si sljedeća pitanja:

- Koja je razlika između TensorFlow i PyTorch?
- Koja je razlika između overfittinga i underfittinga?

## Zadatak

U ovom laboratoriju trebate riješiti dva problema klasifikacije koristeći jednoslojne i višeslojne potpuno povezane mreže koristeći PyTorch ili TensorFlow.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.