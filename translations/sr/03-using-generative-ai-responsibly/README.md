<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-05-19T14:51:51+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "sr"
}
-->
# Odgovorno korišćenje generativne veštačke inteligencije

> _Kliknite na sliku iznad da biste pogledali video lekciju_

Lako je biti fasciniran veštačkom inteligencijom, a posebno generativnom veštačkom inteligencijom, ali treba razmisliti kako je koristiti odgovorno. Treba uzeti u obzir kako obezbediti da rezultati budu pravični, neštetni i još mnogo toga. Ovo poglavlje ima za cilj da vam pruži kontekst, šta treba uzeti u obzir i kako preduzeti aktivne korake za poboljšanje vašeg korišćenja veštačke inteligencije.

## Uvod

Ova lekcija će pokriti:

- Zašto bi trebalo da prioritizujete Odgovornu veštačku inteligenciju prilikom izgradnje aplikacija sa generativnom veštačkom inteligencijom.
- Osnovne principe Odgovorne veštačke inteligencije i kako se oni odnose na generativnu veštačku inteligenciju.
- Kako primeniti ove principe Odgovorne veštačke inteligencije kroz strategiju i alate.

## Ciljevi učenja

Nakon završetka ove lekcije znaćete:

- Značaj Odgovorne veštačke inteligencije prilikom izgradnje aplikacija sa generativnom veštačkom inteligencijom.
- Kada razmišljati i primeniti osnovne principe Odgovorne veštačke inteligencije prilikom izgradnje aplikacija sa generativnom veštačkom inteligencijom.
- Koji alati i strategije su vam dostupni da biste koncept Odgovorne veštačke inteligencije sproveli u praksu.

## Principi Odgovorne veštačke inteligencije

Uzbuđenje oko generativne veštačke inteligencije nikada nije bilo veće. Ovo uzbuđenje je privuklo mnogo novih programera, pažnje i finansiranja u ovu oblast. Iako je ovo veoma pozitivno za svakoga ko želi da gradi proizvode i kompanije koristeći generativnu veštačku inteligenciju, važno je da postupamo odgovorno.

Tokom ovog kursa, fokusiramo se na izgradnju našeg startapa i našeg proizvoda za edukaciju o veštačkoj inteligenciji. Koristićemo principe Odgovorne veštačke inteligencije: Pravičnost, Uključivost, Pouzdanost/Sigurnost, Bezbednost i Privatnost, Transparentnost i Odgovornost. Sa ovim principima, istražićemo kako se oni odnose na naše korišćenje generativne veštačke inteligencije u našim proizvodima.

## Zašto bi trebalo da prioritizujete Odgovornu veštačku inteligenciju

Prilikom izgradnje proizvoda, pristup usmeren na ljude koji ima u vidu najbolji interes korisnika vodi do najboljih rezultata.

Jedinstvenost generativne veštačke inteligencije je njena moć da stvara korisne odgovore, informacije, smernice i sadržaj za korisnike. Ovo se može postići bez mnogo manuelnih koraka, što može dovesti do veoma impresivnih rezultata. Bez odgovarajućeg planiranja i strategija, to takođe može nažalost dovesti do nekih štetnih rezultata za vaše korisnike, vaš proizvod i društvo u celini.

Pogledajmo neke (ali ne sve) od tih potencijalno štetnih rezultata:

### Halucinacije

Halucinacije su termin koji se koristi da opiše kada LLM proizvodi sadržaj koji je ili potpuno besmislen ili nešto što znamo da je činjenično pogrešno na osnovu drugih izvora informacija.

Uzmimo na primer da gradimo funkciju za naš startap koja omogućava studentima da postavljaju istorijska pitanja modelu. Student postavlja pitanje `Who was the sole survivor of Titanic?`

Model proizvodi odgovor kao što je onaj ispod:

Ovo je veoma samouveren i detaljan odgovor. Nažalost, on je netačan. Čak i sa minimalnom količinom istraživanja, neko bi otkrio da je više od jedne osobe preživelo nesreću Titanika. Za studenta koji tek počinje da istražuje ovu temu, ovaj odgovor može biti dovoljno ubedljiv da ne bude doveden u pitanje i tretiran kao činjenica. Posledice ovoga mogu dovesti do toga da AI sistem bude nepouzdan i negativno utiče na reputaciju našeg startapa.

Sa svakom iteracijom bilo kog datog LLM-a, videli smo poboljšanja u performansama u vezi sa minimizacijom halucinacija. Čak i sa ovim poboljšanjem, mi kao graditelji aplikacija i korisnici i dalje moramo biti svesni ovih ograničenja.

### Štetni sadržaj

Pokrijemo u prethodnom delu kada LLM proizvodi netačne ili besmislene odgovore. Drugi rizik o kojem moramo biti svesni je kada model odgovara štetnim sadržajem.

Štetni sadržaj može biti definisan kao:

- Pružanje uputstava ili podsticanje na samopovređivanje ili povređivanje određenih grupa.
- Mrziteljski ili ponižavajući sadržaj.
- Usmeravanje planiranja bilo kakvih napada ili nasilnih dela.
- Pružanje uputstava o tome kako pronaći ilegalan sadržaj ili počiniti ilegalna dela.
- Prikazivanje seksualno eksplicitnog sadržaja.

Za naš startap, želimo da budemo sigurni da imamo prave alate i strategije na mestu kako bismo sprečili da ovaj tip sadržaja bude viđen od strane studenata.

### Nedostatak pravičnosti

Pravičnost je definisana kao “osiguravanje da je AI sistem slobodan od pristrasnosti i diskriminacije i da se prema svima odnosi pravično i jednako.” U svetu generativne veštačke inteligencije, želimo da osiguramo da isključujući svetski pogledi marginalizovanih grupa nisu ojačani izlazom modela.

Ovi tipovi izlaza nisu samo destruktivni za izgradnju pozitivnih iskustava proizvoda za naše korisnike, već uzrokuju i dalju društvenu štetu. Kao graditelji aplikacija, uvek treba da imamo široku i raznoliku bazu korisnika na umu kada gradimo rešenja sa generativnom veštačkom inteligencijom.

## Kako koristiti generativnu veštačku inteligenciju odgovorno

Sada kada smo identifikovali značaj Odgovorne generativne veštačke inteligencije, hajde da pogledamo 4 koraka koje možemo preduzeti da odgovorno gradimo naša AI rešenja:

### Merenje potencijalnih šteta

U testiranju softvera, testiramo očekivane akcije korisnika na aplikaciji. Slično tome, testiranje raznovrsnog skupa upita koje korisnici najverovatnije koriste je dobar način za merenje potencijalne štete.

Pošto naš startap gradi edukativni proizvod, bilo bi dobro pripremiti listu upita vezanih za edukaciju. Ovo bi moglo pokriti određeni predmet, istorijske činjenice i upite o studentskom životu.

### Ublažavanje potencijalnih šteta

Sada je vreme da pronađemo načine kako možemo sprečiti ili ograničiti potencijalnu štetu uzrokovanu modelom i njegovim odgovorima. Ovo možemo pogledati u 4 različita sloja:

- **Model**. Biranje pravog modela za pravi slučaj upotrebe. Veći i složeniji modeli poput GPT-4 mogu izazvati veći rizik od štetnog sadržaja kada se primenjuju na manje i specifične slučajeve upotrebe. Korišćenje vaših podataka za obuku za fino podešavanje takođe smanjuje rizik od štetnog sadržaja.

- **Sigurnosni sistem**. Sigurnosni sistem je skup alata i konfiguracija na platformi koja služi modelu kako bi pomogla u ublažavanju štete. Primer ovoga je sistem za filtriranje sadržaja na Azure OpenAI servisu. Sistemi takođe treba da detektuju napade iz zatvora i neželjene aktivnosti poput zahteva od strane botova.

- **Metaprompt**. Metaprompts i uzemljenje su načini na koje možemo usmeriti ili ograničiti model na osnovu određenih ponašanja i informacija. Ovo bi moglo biti korišćenje ulaza sistema za definisanje određenih granica modela. Pored toga, pružanje izlaza koji su relevantniji za obim ili domen sistema.

Takođe može biti korišćenje tehnika poput Retrieval Augmented Generation (RAG) kako bi model povlačio informacije samo iz odabranih pouzdanih izvora. Postoji lekcija kasnije u ovom kursu za [izgradnju pretraživačkih aplikacija](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Korisničko iskustvo**. Poslednji sloj je gde korisnik direktno komunicira sa modelom kroz interfejs naše aplikacije na neki način. Na ovaj način možemo dizajnirati UI/UX kako bismo ograničili korisnika na tipove unosa koje mogu poslati modelu, kao i tekst ili slike prikazane korisniku. Kada implementiramo AI aplikaciju, takođe moramo biti transparentni o tome šta naša generativna veštačka inteligencija može i ne može da uradi.

Imamo celu lekciju posvećenu [dizajniranju UX za AI aplikacije](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Evaluacija modela**. Rad sa LLM-ovima može biti izazovno jer nemamo uvek kontrolu nad podacima na kojima je model obučen. Bez obzira na to, uvek treba da procenimo performanse i izlaze modela. I dalje je važno meriti tačnost, sličnost, uzemljenost i relevantnost izlaza modela. Ovo pomaže da se obezbedi transparentnost i poverenje za zainteresovane strane i korisnike.

### Operativno odgovorno generativno AI rešenje

Izgradnja operativne prakse oko vaših AI aplikacija je poslednja faza. Ovo uključuje partnerstvo sa drugim delovima našeg startapa kao što su Pravni i Bezbednosni kako bismo osigurali da smo u skladu sa svim regulatornim politikama. Pre lansiranja, takođe želimo da izgradimo planove oko isporuke, rešavanja incidenata i vraćanja na prethodno stanje kako bismo sprečili bilo kakvu štetu našim korisnicima od rasta.

## Alati

Iako rad na razvoju rešenja za Odgovornu veštačku inteligenciju može izgledati kao mnogo posla, to je posao koji se isplati. Kako oblast generativne veštačke inteligencije raste, sve više alata za pomoć programerima da efikasno integrišu odgovornost u svoje radne tokove će sazrevati. Na primer, [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) može pomoći u otkrivanju štetnog sadržaja i slika putem API zahteva.

## Provera znanja

Na koje stvari treba da obratite pažnju kako biste osigurali odgovorno korišćenje veštačke inteligencije?

1. Da je odgovor tačan.
1. Štetna upotreba, da se AI ne koristi u kriminalne svrhe.
1. Osiguranje da je AI slobodan od pristrasnosti i diskriminacije.

A: 2 i 3 su tačne. Odgovorna veštačka inteligencija pomaže vam da razmislite kako da ublažite štetne efekte i pristrasnosti i još mnogo toga.

## 🚀 Izazov

Pročitajte više o [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) i vidite šta možete usvojiti za svoju upotrebu.

## Odličan rad, nastavite sa učenjem

Nakon završetka ove lekcije, pogledajte našu [kolekciju za učenje o generativnoj veštačkoj inteligenciji](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili sa unapređivanjem svog znanja o generativnoj veštačkoj inteligenciji!

Pređite na Lekciju 4 gde ćemo pogledati [osnove inženjeringa upita](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, имајте на уму да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на свом изворном језику треба сматрати меродавним извором. За критичне информације, препоручује се професионални превод од стране људи. Нисмо одговорни за било каква неспоразума или погрешна тумачења која могу настати коришћењем овог превода.