# Izgradnja chat aplikacija pokretanih generativnom AI

[![Building Generative AI-Powered Chat Applications](../../../translated_images/hr/07-lesson-banner.a279b937f2843833.webp)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Kliknite na gornju sliku za pregled video lekcije)_

Sada kada smo vidjeli kako možemo graditi aplikacije za generiranje teksta, pogledajmo chat aplikacije.

Chat aplikacije postale su sastavni dio naših svakodnevnih života, nudeći mnogo više od same mogućnosti za ležerni razgovor. One su ključni dijelovi korisničke podrške, tehničke pomoći pa čak i složenih savjetodavnih sustava. Vjerojatno ste nedavno dobili pomoć putem chat aplikacije. Kako u ove platforme integriramo naprednije tehnologije poput generativne AI, složenost se povećava, kao i izazovi.

Neka pitanja na koja trebamo odgovor uključuju:

- **Izgradnja aplikacije**. Kako učinkovito izgraditi i besprijekorno integrirati ove AI-pokretane aplikacije za specifične slučajeve upotrebe?
- **Nadzor**. Nakon implementacije, kako možemo pratiti i osigurati da aplikacije rade na najvišoj razini kvalitete, kako u smislu funkcionalnosti tako i u pridržavanju [šest načela odgovorne AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

Kako ulazimo dublje u doba definirano automatizacijom i besprijekornom interakcijom čovjeka i stroja, postaje ključno razumjeti kako generativna AI transformira opseg, dubinu i prilagodljivost chat aplikacija. Ova lekcija istražit će aspekte arhitekture koji podržavaju ove složene sustave, uroniti u metodologije za fino podešavanje za zadatke specifične za domenu, te procijeniti metrike i razmatranja važna za osiguranje odgovorne primjene AI.

## Uvod

Ova lekcija pokriva:

- Tehnike za učinkovito izgradnju i integraciju chat aplikacija.
- Kako primijeniti prilagodbu i fino podešavanje aplikacija.
- Strategije i razmatranja za učinkovito praćenje chat aplikacija.

## Ciljevi učenja

Do kraja ove lekcije moći ćete:

- Opišite razmatranja za izgradnju i integraciju chat aplikacija u postojeće sustave.
- Prilagoditi chat aplikacije za specifične slučajeve upotrebe.
- Identificirati ključne metrike i razmatranja za učinkovito praćenje i održavanje kvalitete AI-pokretanih chat aplikacija.
- Osigurati da chat aplikacije koriste AI na odgovoran način.

## Integracija generativne AI u chat aplikacije

Podizanje chat aplikacija korištenjem generativne AI nije samo usmjereno na njihovo "pametnije" funkcioniranje; riječ je o optimizaciji njihove arhitekture, performansi i korisničkog sučelja za pružanje kvalitetnog korisničkog iskustva. To uključuje proučavanje arhitektonskih osnova, API integracija i razmatranja vezanih uz korisničko sučelje. Ovaj odjeljak ima za cilj ponuditi vam sveobuhvatnu mapu puta za navigaciju ovim složenim područjima, bilo da ih povezujete s postojećim sustavima ili gradite kao samostalne platforme.

Do kraja ovog odjeljka bit ćete opremljeni stručnošću potrebnom za učinkovitu izgradnju i integraciju chat aplikacija.

### Chatbot ili chat aplikacija?

Prije nego što zaronimo u izgradnju chat aplikacija, usporedimo 'chatbote' s 'AI-pokrenutim chat aplikacijama', koje imaju različite uloge i funkcionalnosti. Glavna svrha chatbota je automatizirati specifične zadatke u razgovoru, poput odgovaranja na često postavljana pitanja ili praćenje paketa. Obično se upravlja pravilima ili složenim AI algoritmima. Nasuprot tome, AI-pokretana chat aplikacija je znatno šire okruženje dizajnirano za facilitaciju različitih oblika digitalne komunikacije, poput tekstualnih, glasovnih i video razgovora među ljudskim korisnicima. Njena karakteristična osobina je integracija generativnog AI modela koji simulira nijansirane, ljudski slične razgovore generiranjem odgovora temeljenih na raznovrsnim ulazima i kontekstualnim naznakama. AI-pokretana chat aplikacija može se uključiti u razgovore otvorenog domena, prilagođavati se promjenjivim kontekstima razgovora, pa čak i stvarati kreativne ili složene dijaloge.

Tablica u nastavku prikazuje ključne razlike i sličnosti kako bismo bolje razumjeli njihove jedinstvene uloge u digitalnoj komunikaciji.

| Chatbot                               | Chat aplikacija pokretana generativnom AI |
| ------------------------------------- | ------------------------------------------ |
| Fokusiran na zadatke i temeljen na pravilima | Svjestan konteksta                         |
| Često integriran u veće sustave          | Može ugostiti jedan ili više chatbotova    |
| Ograničen na programske funkcije        | Uključuje generativne AI modele             |
| Specijalizirane i strukturirane interakcije | Sposoban za razgovore otvorenog domena       |

### Korištenje predgrađenih funkcionalnosti putem SDK-ova i API-ja

Prilikom izgradnje chat aplikacije dobar prvi korak je procjena što je već dostupno. Korištenje SDK-ova i API-ja za izgradnju chat aplikacija je povoljna strategija iz više razloga. Integriranjem dobro dokumentiranih SDK-ova i API-ja strateški pozicionirate svoju aplikaciju za dugoročni uspjeh, rješavajući pitanja skalabilnosti i održavanja.

- **Ubrzava proces razvoja i smanjuje troškove**: Oslanjanje na predgrađene funkcionalnosti umjesto skupog procesa njihovog vlastitog razvoja omogućava vam da se usredotočite na druge aspekte svoje aplikacije koje smatrate važnijima, poput poslovne logike.
- **Bolje performanse**: Kada gradite funkcionalnost od nule, prije ili kasnije ćete se zapitati "Kako se ovo skalira? Može li ova aplikacija podnijeti nagli priljev korisnika?" Dobro održavani SDK i API često imaju ugrađena rješenja za ove brige.
- **Lakše održavanje**: Ažuriranja i poboljšanja je lakše upravljati jer većina API-ja i SDK-ova jednostavno zahtijeva ažuriranje biblioteke kad izađe nova verzija.
- **Pristup vrhunskoj tehnologiji**: Korištenjem modela koji su fino podešeni i trenirani na opsežnim skupovima podataka vaša aplikacija dobiva mogućnosti obrade prirodnog jezika.

Pristup funkcionalnosti SDK-a ili API-ja obično uključuje dobivanje dozvole za korištenje pruženih usluga, često putem jedinstvenog ključa ili tokena za autentifikaciju. Koristit ćemo OpenAI Python biblioteku da istražimo kako to izgleda. Također ga možete isprobati sami u sljedećem [notebooku za OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) ili [notebooku za Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) za ovu lekciju.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

response = client.responses.create(model="gpt-5-mini", input="Suggest two titles for an instructional lesson on chat applications for generative AI.", store=False)
print(response.output_text)
```

Gornji primjer koristi GPT-5 mini model s Responses API-jem za dovršavanje upita, ali primijetite da je API ključ postavljen prije toga. Dobit ćete grešku ako ključ nije postavljen.

## Korisničko iskustvo (UX)

Opća pravila UX-a se primjenjuju na chat aplikacije, ali ovdje su neka dodatna razmatranja koja postaju posebno važna zbog uključenih komponenti strojnog učenja.

- **Mehanizam za rješavanje nejasnoća**: Generativni AI modeli povremeno generiraju dvosmislene odgovore. Značajka koja korisnicima dopušta da zatraže pojašnjenje može biti korisna ako se susretnu s tim problemom.
- **Zadržavanje konteksta**: Napredni generativni AI modeli imaju sposobnost pamćenja konteksta unutar razgovora, što može biti potrebna prednost za korisničko iskustvo. Davanje korisnicima mogućnosti kontrole i upravljanja kontekstom poboljšava iskustvo, ali uvodi rizik zadržavanja osjetljivih korisničkih podataka. Razmatranja poput trajanja pohrane tih podataka, primjerice kroz uvođenje politike zadržavanja, mogu izbalansirati potrebu za kontekstom s privatnošću.
- **Personalizacija**: Sposobnost učenja i adaptacije, AI modeli nude individualizirano iskustvo korisniku. Prilagođavanje korisničkog iskustva kroz značajke poput korisničkih profila ne samo da korisniku pruža osjećaj razumijevanja, već i pomaže u traženju specifičnih odgovora, stvarajući učinkovitiju i zadovoljavajuću interakciju.

Jedan takav primjer personalizacije su "Prilagođene upute" u OpenAI-jevom ChatGPT-u. Omogućuju vam pružanje informacija o sebi koje mogu biti važan kontekst za vaše upite. Evo primjera prilagođene upute.

![Custom Instructions Settings in ChatGPT](../../../translated_images/hr/custom-instructions.b96f59aa69356fcf.webp)

Ovaj "profil" upućuje ChatGPT da kreira plan lekcije o povezanim listama. Primijetite da ChatGPT uzima u obzir da korisnik možda želi detaljniji plan lekcije temeljen na njenom iskustvu.

![A prompt in ChatGPT for a lesson plan about linked lists](../../../translated_images/hr/lesson-plan-prompt.cc47c488cf1343df.webp)

### Microsoftov okvir sustavnih poruka za velike jezične modele

[Microsoft je pružio smjernice](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) za pisanje učinkovitih sustavnih poruka pri generiranju odgovora iz LLM-ova podijeljenih u 4 područja:

1. Definiranje za koga je model, kao i njegovih sposobnosti i ograničenja.
2. Definiranje formata izlaza modela.
3. Pružanje specifičnih primjera koji demonstriraju namjerno ponašanje modela.
4. Pružanje dodatnih ponašajnih zaštita.

### Pristupačnost

Bilo da korisnik ima vidne, slušne, motoričke ili kognitivne smetnje, dobro dizajnirana chat aplikacija trebala bi biti upotrebljiva od strane svih. Sljedeći popis razlaže specifične značajke usmjerene na poboljšanje pristupačnosti za različite korisničke potrebe.

- **Značajke za oštećenje vida**: Tematski visoki kontrasti i tekst prilagodljive veličine, kompatibilnost s čitačima zaslona.
- **Značajke za oštećenje sluha**: Funkcije pretvaranja teksta u govor i govora u tekst, vizualni znakovi za audio obavijesti.
- **Značajke za motoričke smetnje**: Podrška za navigaciju putem tipkovnice, glasovne naredbe.
- **Značajke za kognitivne smetnje**: Jednostavnije jezične mogućnosti.

## Prilagodba i fino podešavanje za modele jezika specifične za domenu

Zamislite chat aplikaciju koja razumije žargon vaše tvrtke i predviđa specifične upite koje korisnička baza često postavlja. Postoji nekoliko pristupa vrijednih spomena:

- **Iskorištavanje DSL modela**. DSL označava specifikum jezika domene. Možete iskoristiti takozvani DSL model treniran na određenoj domeni da razumije njene koncepte i scenarije.
- **Primjena fino podešavanje**. Fino podešavanje je proces daljnjeg treniranja vašeg modela sa specifičnim podacima.

## Prilagodba: Korištenje DSL modela

Korištenje modela jezika specifičnih za domenu (DSL modeli) može poboljšati angažman korisnika pružajući specijalizirane, kontekstualno relevantne interakcije. To je model koji je treniran ili fino podešen za razumijevanje i generiranje teksta vezanog uz određeno područje, industriju ili temu. Opcije za korištenje DSL modela mogu varirati od treniranja potpuno od početka do korištenja postojećih putem SDK-ova i API-ja. Druga opcija je fino podešavanje, što uključuje uzimanje postojećeg prethodno treniranog modela i njegovo prilagođavanje za specifičnu domenu.

## Prilagodba: Primjena fino podešavanja

Fino podešavanje se često razmatra kada prethodno trenirani model nije dovoljan u specijaliziranoj domeni ili za specifične zadatke.

Na primjer, medicinski upiti su složeni i zahtijevaju mnogo konteksta. Kada medicinski stručnjak postavi dijagnozu, ona se temelji na različitim čimbenicima poput životnog stila ili postojećih uvjeta, a može se oslanjati i na nedavne medicinske časopise za potvrdu dijagnoze. U takvim nijansiranim scenarijima, AI chat aplikacija opće namjene ne može biti pouzdan izvor.

### Scenarij: medicinska aplikacija

Razmotrite chat aplikaciju dizajniranu da pomogne medicinskim stručnjacima pružajući brze reference za smjernice liječenja, interakcije lijekova ili najnovija istraživanja.

Model opće namjene može biti prikladan za odgovaranje na osnovna medicinska pitanja ili davanje općih savjeta, ali može imati poteškoća sa sljedećim:

- **Vrlo specifični ili složeni slučajevi**. Na primjer, neurolog bi mogao pitati aplikaciju: "Koje su trenutačne najbolje prakse za upravljanje lijekovima otpornom epilepsijom kod pedijatrijskih pacijenata?"
- **Nedostatak najnovijih dostignuća**. Model opće namjene mogao bi imati poteškoća pružiti aktualan odgovor koji uključuje najnovija dostignuća u neurologiji i farmakologiji.

U slučajevima poput ovih, fino podešavanje modela sa specijaliziranim medicinskim skupom podataka može značajno poboljšati njegovu sposobnost da točnije i pouzdanije rukuje tim složenim medicinskim upitima. To zahtijeva pristup velikom i relevantnom skupu podataka koji predstavlja izazove i pitanja specifična za domenu.

## Razmatranja za visokokvalitetno AI-pokretano chat iskustvo

Ovaj odjeljak izlaže kriterije za "visokokvalitetne" chat aplikacije, koji uključuju prikupljanje mjerljivih pokazatelja i pridržavanje okvira koji odgovorno koriste AI tehnologiju.

### Ključne metrike

Za održavanje visokih performansi aplikacije važno je pratiti ključne metrike i razmatranja. Ove mjere ne samo da osiguravaju funkcionalnost aplikacije, već i procjenjuju kvalitetu AI modela i korisničkog iskustva. Ispod je lista osnovnih, AI i korisničkih metrika koje treba uzeti u obzir.

| Metrika                      | Definicija                                                                                                             | Razmatranja za razvojne programere chat aplikacija                       |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Vrijeme rada (Uptime)**     | Mjeri vrijeme tijekom kojeg je aplikacija funkcionalna i dostupna korisnicima.                                         | Kako ćete minimizirati zastoje?                                           |
| **Vrijeme odgovora**           | Vrijeme potrebno aplikaciji da odgovori na korisnički upit.                                                            | Kako možete optimizirati procesiranje upita za brže vrijeme odgovora?     |
| **Preciznost**                | Omjer istinitih pozitivnih predviđanja prema ukupnom broju pozitivnih predviđanja                                      | Kako ćete validirati preciznost svog modela?                              |
| **Recall (osjetljivost)**      | Omjer istinitih pozitivnih predviđanja prema stvarnom broju pozitivnih slučajeva                                        | Kako ćete mjeriti i poboljšati recall?                                   |
| **F1 rezultat**                | Harmonijska sredina preciznosti i recall-a, koja balansira kompromis između obojega.                                   | Koji je vaš ciljani F1 rezultat? Kako ćete balansirati preciznost i recall?|
| **Zbunjenost (Perplexity)**   | Mjeri koliko dobro distribucija vjerojatnosti koju predviđa model odgovara stvarnoj distribuciji podataka.             | Kako ćete minimizirati zbunjenost?                                       |
| **Metrike zadovoljstva korisnika** | Mjeri percepciju korisnika o aplikaciji. Često se prikuplja putem anketa.                                            | Koliko često ćete prikupljati povratne informacije korisnika? Kako ćete se prilagođavati na temelju njih? |
| **Stopa pogrešaka**            | Stopa kojom model griješi u razumijevanju ili ishodu.                                                                  | Koje strategije imate za smanjenje stope pogrešaka?                       |
| **Ciklus ponovnog treniranja** | Učestalost kojom se model ažurira za uključivanje novih podataka i saznanja.                                           | Koliko često ćete ponovo trenirati model? Što pokreće ciklus ponovnog treniranja? |

| **Otkrivanje anomalija**         | Alati i tehnike za prepoznavanje neuobičajenih obrazaca koji se ne pridržavaju očekivanog ponašanja.                        | Kako ćete reagirati na anomalije?                                        |

### Provođenje odgovorne AI prakse u chat aplikacijama

Microsoftov pristup Odgovornoj AI identificirao je šest načela koja bi trebala voditi razvoj i uporabu AI-a. Ispod su načela, njihova definicija, te stvari koje bi developer chat aplikacije trebao uzeti u obzir i zašto ih treba ozbiljno shvatiti.

| Načela             | Microsoftova definicija                                | Razmatranja za developera chat aplikacije                                      | Zašto je važno                                                                     |
| ---------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Pravednost               | AI sustavi trebaju prema svima postupati pravedno.            | Osigurati da chat aplikacija ne diskriminira na osnovi korisničkih podataka.  | Za izgradnju povjerenja i inkluzivnosti među korisnicima; izbjegavanje pravnih posljedica.                |
| Pouzdanost i sigurnost | AI sustavi trebaju raditi pouzdano i sigurno.        | Provesti testiranja i osigurati sigurnosne mjere za minimiziranje pogrešaka i rizika.         | Osigurava zadovoljstvo korisnika i sprječava potencijalnu štetu.                                 |
| Privatnost i sigurnost   | AI sustavi trebaju biti sigurni i poštivati privatnost.      | Implementirati snažno šifriranje i mjere zaštite podataka.              | Za zaštitu osjetljivih korisničkih podataka i usklađenost sa zakonima o privatnosti.                         |
| Inkluzivnost          | AI sustavi trebaju osnaživati sve i uključivati ljude. | Dizajnirati UI/UX koji je pristupačan i jednostavan za korištenje različitim korisnicima. | Osigurava da širi krug ljudi može učinkovito koristiti aplikaciju.                   |
| Transparentnost           | AI sustavi trebaju biti razumljivi.                  | Osigurati jasnu dokumentaciju i obrazloženja za AI odgovore.            | Korisnici će više vjerovati sustavu ako razumiju kako se donose odluke. |
| Odgovornost         | Ljudi trebaju biti odgovorni za AI sustave.          | Uspostaviti jasan proces za reviziju i poboljšanje AI odluka.     | Omogućuje kontinuirano poboljšavanje i korektivne mjere u slučaju pogrešaka.               |

## Zadavanje

Pogledajte [zadavanje](../../../07-building-chat-applications/python). Provest će vas kroz niz vježbi od pokretanja vaših prvih chat upita, preko klasificiranja i sažimanja teksta i još mnogo toga. Primijetite da su zadaci dostupni u različitim programskim jezicima!

## Odličan posao! Nastavite putovanje

Nakon dovršetka ove lekcije, pogledajte našu [kolekciju za učenje generativne AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili usavršavati svoje znanje o Generativnoj AI!

Krenite na Lekciju 8 da vidite kako možete započeti s [izgradnjom aplikacija za pretraživanje](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->