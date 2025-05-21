<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-05-20T02:08:29+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "sr"
}
-->
# Okviri neuronskih mreža

Kao što smo već naučili, da bismo mogli efikasno trenirati neuronske mreže, potrebno je da uradimo dve stvari:

* Da radimo sa tenzorima, npr. da množimo, sabiramo i računamo neke funkcije kao što su sigmoid ili softmax
* Da izračunamo gradijente svih izraza, kako bismo izvršili optimizaciju spuštanjem gradijenta

Dok `numpy` biblioteka može da uradi prvi deo, potrebna nam je neka mehanizam za računanje gradijenata. U našem okviru koji smo razvili u prethodnom odeljku morali smo ručno da programiramo sve funkcije derivacija unutar `backward` metode, koja vrši povratnu propagaciju. Idealno, okvir bi trebalo da nam pruži mogućnost da izračunamo gradijente *bilo kog izraza* koji možemo definisati.

Još jedna važna stvar je da možemo da obavljamo proračune na GPU, ili bilo kojim drugim specijalizovanim jedinicama za proračun, kao što je TPU. Trening dubokih neuronskih mreža zahteva *mnogo* proračuna, i mogućnost da se ti proračuni paralelizuju na GPU-ima je veoma važna.

> ✅ Termin 'paralelizacija' znači raspodelu proračuna na više uređaja.

Trenutno, dva najpopularnija okvira za neuronske mreže su: TensorFlow i PyTorch. Oba pružaju API niskog nivoa za rad sa tenzorima na CPU i GPU. Na vrhu API-ja niskog nivoa, postoji i API višeg nivoa, koji se zove Keras i PyTorch Lightning, respektivno.

API niskog nivoa | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
API visokog nivoa| Keras| Pytorch

**API niskog nivoa** u oba okvira omogućavaju vam da gradite takozvane **grafove proračuna**. Ovaj graf definiše kako izračunati izlaz (obično funkciju gubitka) sa datim ulaznim parametrima, i može biti gurnut za proračun na GPU, ako je dostupan. Postoje funkcije za diferencijaciju ovog grafika proračuna i računanje gradijenata, koje se zatim mogu koristiti za optimizaciju parametara modela.

**API visokog nivoa** uglavnom smatraju neuronske mreže kao **sekvencu slojeva**, i čine konstrukciju većine neuronskih mreža mnogo lakšom. Trening modela obično zahteva pripremu podataka i zatim pozivanje `fit` funkcije da obavi posao.

API visokog nivoa omogućava vam da brzo konstruirate tipične neuronske mreže bez brige o mnogim detaljima. Istovremeno, API niskog nivoa pruža mnogo više kontrole nad procesom treninga, i zbog toga se puno koriste u istraživanju, kada se bavite novim arhitekturama neuronskih mreža.

Takođe je važno razumeti da možete koristiti oba API-ja zajedno, npr. možete razviti svoju arhitekturu slojeva mreže koristeći API niskog nivoa, a zatim je koristiti unutar veće mreže konstruisane i trenirane sa API-jem visokog nivoa. Ili možete definisati mrežu koristeći API visokog nivoa kao sekvencu slojeva, a zatim koristiti svoj sopstveni trening loop niskog nivoa da izvršite optimizaciju. Oba API-ja koriste iste osnovne koncepte, i dizajnirani su da dobro rade zajedno.

## Učenje

U ovom kursu, nudimo većinu sadržaja kako za PyTorch, tako i za TensorFlow. Možete izabrati svoj preferirani okvir i proći samo kroz odgovarajuće beležnice. Ako niste sigurni koji okvir da izaberete, pročitajte neke diskusije na internetu o **PyTorch vs. TensorFlow**. Takođe možete pogledati oba okvira da biste stekli bolje razumevanje.

Gde god je moguće, koristićemo API visokog nivoa radi jednostavnosti. Međutim, verujemo da je važno razumeti kako neuronske mreže funkcionišu od temelja, stoga na početku počinjemo sa radom sa API-jem niskog nivoa i tenzorima. Međutim, ako želite brzo da krenete i ne želite da potrošite puno vremena na učenje ovih detalja, možete ih preskočiti i odmah preći na beležnice API-ja visokog nivoa.

## ✍️ Vežbe: Okviri

Nastavite svoje učenje u sledećim beležnicama:

API niskog nivoa | Beležnica TensorFlow+Keras | PyTorch
--------------|-------------------------------------|--------------------------------
API visokog nivoa| Keras | *PyTorch Lightning*

Nakon savladavanja okvira, hajde da ponovimo pojam prekomernog prilagođavanja.

# Prekomerno prilagođavanje

Prekomerno prilagođavanje je izuzetno važan koncept u mašinskom učenju, i veoma je važno da ga pravilno razumemo!

Razmotrite sledeći problem aproksimacije 5 tačaka (predstavljenih sa `x` na grafikonima ispod):

!linear | prekomerno prilagođavanje
-------------------------|--------------------------
**Linearni model, 2 parametra** | **Nelinearni model, 7 parametara**
Greška treninga = 5.3 | Greška treninga = 0
Greška validacije = 5.1 | Greška validacije = 20

* Levo vidimo dobru aproksimaciju pravom linijom. Zato što je broj parametara adekvatan, model pravilno razume distribuciju tačaka.
* Desno, model je previše moćan. Zato što imamo samo 5 tačaka, a model ima 7 parametara, može se prilagoditi na takav način da prođe kroz sve tačke, čineći grešku treninga 0. Međutim, to sprečava model da razume ispravan obrazac podataka, stoga je greška validacije veoma visoka.

Veoma je važno postići pravilan balans između bogatstva modela (broja parametara) i broja uzoraka za trening.

## Zašto dolazi do prekomernog prilagođavanja

  * Nedovoljno podataka za trening
  * Previše moćan model
  * Previše šuma u ulaznim podacima

## Kako otkriti prekomerno prilagođavanje

Kao što možete videti sa grafikona iznad, prekomerno prilagođavanje može se otkriti vrlo niskom greškom treninga i visokom greškom validacije. Obično tokom treninga vidimo da greške treninga i validacije počinju da se smanjuju, a zatim u nekom trenutku greška validacije može prestati da se smanjuje i početi da raste. To će biti znak prekomernog prilagođavanja i indikator da verovatno treba da prestanemo sa treningom u tom trenutku (ili barem da napravimo snimak modela).

## Kako sprečiti prekomerno prilagođavanje

Ako vidite da dolazi do prekomernog prilagođavanja, možete uraditi jedno od sledećeg:

 * Povećajte količinu podataka za trening
 * Smanjite složenost modela
 * Koristite neku tehniku regularizacije, kao što je Dropout, koju ćemo razmotriti kasnije.

## Prekomerno prilagođavanje i kompromis pristrasnosti-varijanse

Prekomerno prilagođavanje je zapravo slučaj opšteg problema u statistici koji se zove kompromis pristrasnosti-varijanse. Ako razmotrimo moguće izvore greške u našem modelu, možemo videti dve vrste grešaka:

* **Greške pristrasnosti** su uzrokovane time što naš algoritam nije u stanju da pravilno uhvati odnos između podataka za trening. To može biti rezultat činjenice da naš model nije dovoljno moćan (**nedovoljno prilagođavanje**).
* **Greške varijanse**, koje su uzrokovane time što model aproksimira šum u ulaznim podacima umesto smislenog odnosa (**prekomerno prilagođavanje**).

Tokom treninga, greška pristrasnosti se smanjuje (kako naš model uči da aproksimira podatke), a greška varijanse se povećava. Važno je prestati sa treningom - ili ručno (kada otkrijemo prekomerno prilagođavanje) ili automatski (uvođenjem regularizacije) - da bismo sprečili prekomerno prilagođavanje.

## Zaključak

U ovoj lekciji ste naučili o razlikama između različitih API-ja za dva najpopularnija AI okvira, TensorFlow i PyTorch. Pored toga, naučili ste o veoma važnoj temi, prekomernom prilagođavanju.

## 🚀 Izazov

U pratećim beležnicama, pronaći ćete 'zadatke' na dnu; prođite kroz beležnice i završite zadatke.

## Pregled i samostalno učenje

Uradite istraživanje o sledećim temama:

- TensorFlow
- PyTorch
- Prekomerno prilagođavanje

Postavite sebi sledeća pitanja:

- Koja je razlika između TensorFlow i PyTorch?
- Koja je razlika između prekomernog prilagođavanja i nedovoljnog prilagođavanja?

## Zadatak

U ovoj laboratoriji, od vas se traži da rešite dva problema klasifikacije koristeći jednostruke i višeslojne potpuno povezane mreže koristeći PyTorch ili TensorFlow.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге превођења вештачком интелигенцијом [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да будете свесни да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације, препоручује се професионални људски превод. Не сносимо одговорност за било каква неспоразумевања или погрешна тумачења која могу произаћи из коришћења овог превода.