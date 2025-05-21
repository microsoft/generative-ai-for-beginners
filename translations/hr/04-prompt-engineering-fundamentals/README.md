<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-05-19T16:26:58+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "hr"
}
-->
# Osnove projektiranja upita

## Uvod

Ovaj modul pokriva osnovne pojmove i tehnike za stvaranje učinkovitih upita u generativnim AI modelima. Način na koji pišete svoj upit za LLM također je važan. Pažljivo osmišljen upit može postići bolju kvalitetu odgovora. Ali što točno znače pojmovi poput _upit_ i _projektiranje upita_? I kako mogu poboljšati _unos_ upita koji šaljem LLM-u? To su pitanja na koja ćemo pokušati odgovoriti u ovom i sljedećem poglavlju.

_Generativna AI_ je sposobna stvarati novi sadržaj (npr. tekst, slike, audio, kod itd.) kao odgovor na zahtjeve korisnika. To postiže koristeći _Velike Jezične Modele_ kao što je OpenAI-jev GPT ("Generative Pre-trained Transformer") serija, koja je trenirana za korištenje prirodnog jezika i koda.

Korisnici sada mogu komunicirati s ovim modelima koristeći poznate paradigme poput chata, bez potrebe za tehničkim znanjem ili obukom. Modeli su _temeljeni na upitima_ - korisnici šalju tekstualni unos (upit) i dobivaju AI odgovor (dovršetak). Tada mogu "razgovarati s AI-jem" iterativno, u višekratnim razgovorima, usavršavajući svoj upit dok odgovor ne zadovolji njihova očekivanja.

"Upiti" sada postaju primarno _programsko sučelje_ za generativne AI aplikacije, govoreći modelima što trebaju raditi i utječući na kvalitetu vraćenih odgovora. "Projektiranje upita" je brzo rastuće područje proučavanja koje se fokusira na _dizajn i optimizaciju_ upita kako bi se isporučili dosljedni i kvalitetni odgovori u velikom obimu.

## Ciljevi učenja

U ovoj lekciji naučit ćemo što je projektiranje upita, zašto je važno i kako možemo oblikovati učinkovitije upite za određeni model i cilj aplikacije. Razumjet ćemo osnovne pojmove i najbolje prakse za projektiranje upita - i saznati više o interaktivnom okruženju "sandbox" u Jupyter Notebooks gdje možemo vidjeti primjenu ovih pojmova na stvarnim primjerima.

Do kraja ove lekcije moći ćemo:

1. Objasniti što je projektiranje upita i zašto je važno.
2. Opisati komponente upita i kako se koriste.
3. Naučiti najbolje prakse i tehnike za projektiranje upita.
4. Primijeniti naučene tehnike na stvarne primjere, koristeći OpenAI endpoint.

## Ključni pojmovi

Projektiranje upita: Praksa dizajniranja i usavršavanja unosa kako bi se AI modeli usmjerili prema proizvodnji željenih izlaza.
Tokenizacija: Proces pretvaranja teksta u manje jedinice, nazvane tokeni, koje model može razumjeti i obraditi.
LLM-ovi usklađeni s uputama: Veliki Jezični Modeli (LLM-ovi) koji su fino podešeni s određenim uputama kako bi poboljšali točnost i relevantnost svojih odgovora.

## Sandbox za učenje

Projektiranje upita trenutno je više umjetnost nego znanost. Najbolji način da poboljšamo našu intuiciju za to je _više vježbati_ i usvojiti pristup pokušaja i pogrešaka koji kombinira stručnost u domeni aplikacije s preporučenim tehnikama i optimizacijama specifičnim za model.

Jupyter Notebook koji prati ovu lekciju pruža _sandbox_ okruženje gdje možete isprobati ono što naučite - kako idete ili kao dio izazova kodiranja na kraju. Za izvođenje vježbi trebat će vam:

1. **Azure OpenAI API ključ** - krajnja točka usluge za implementirani LLM.
2. **Python Runtime** - u kojem se Notebook može izvesti.
3. **Lokalne varijable okoline** - _dovršite korake [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) sada kako biste bili spremni_.

Notebook dolazi s _početnim_ vježbama - ali potiče vas da dodate vlastite _Markdown_ (opis) i _Code_ (zahtjevi za upit) sekcije kako biste isprobali više primjera ili ideja - i izgradili svoju intuiciju za dizajn upita.

## Ilustrirani vodič

Želite li dobiti opću sliku o tome što ova lekcija pokriva prije nego što se upustite? Pogledajte ovaj ilustrirani vodič koji vam daje osjećaj za glavne teme koje se obrađuju i ključne spoznaje o kojima trebate razmišljati u svakoj od njih. Putokaz lekcije vodi vas od razumijevanja osnovnih pojmova i izazova do njihovog rješavanja relevantnim tehnikama projektiranja upita i najboljim praksama. Imajte na umu da se odjeljak "Napredne tehnike" u ovom vodiču odnosi na sadržaj obrađen u _sljedećem_ poglavlju ovog kurikuluma.

## Naš startup

Sada, razgovarajmo o tome kako se _ova tema_ odnosi na našu misiju startupa da [donese AI inovacije u obrazovanje](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Želimo izgraditi AI aplikacije za _personalizirano učenje_ - pa razmislimo o tome kako različiti korisnici naše aplikacije mogu "dizajnirati" upite:

- **Administratori** mogu zamoliti AI da _analizira podatke kurikuluma kako bi identificirao praznine u pokrivenosti_. AI može sažeti rezultate ili ih vizualizirati pomoću koda.
- **Nastavnici** mogu zamoliti AI da _generira plan lekcije za ciljanog korisnika i temu_. AI može izraditi personalizirani plan u specificiranom formatu.
- **Učenici** mogu zamoliti AI da ih _podučava u teškom predmetu_. AI sada može voditi učenike s lekcijama, savjetima i primjerima prilagođenima njihovoj razini.

To je samo vrh ledenog brijega. Pogledajte [Upiti za obrazovanje](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - otvorenu biblioteku upita koju su kreirali stručnjaci za obrazovanje - kako biste dobili širi osjećaj za mogućnosti! _Pokušajte pokrenuti neke od tih upita u sandboxu ili pomoću OpenAI Playground-a da vidite što će se dogoditi!_

## Što je projektiranje upita?

Započeli smo ovu lekciju definiranjem **projektiranja upita** kao procesa _dizajniranja i optimizacije_ tekstualnih unosa (upita) kako bi se isporučili dosljedni i kvalitetni odgovori (dovršetci) za određeni cilj aplikacije i model. Možemo to zamisliti kao dvostupanjski proces:

- _dizajniranje_ početnog upita za određeni model i cilj
- _usavršavanje_ upita iterativno kako bi se poboljšala kvaliteta odgovora

Ovo je nužno proces pokušaja i pogrešaka koji zahtijeva korisničku intuiciju i trud kako bi se postigli optimalni rezultati. Pa zašto je to važno? Da bismo odgovorili na to pitanje, prvo moramo razumjeti tri pojma:

- _Tokenizacija_ = kako model "vidi" upit
- _Osnovni LLM-ovi_ = kako osnovni model "obrađuje" upit
- _LLM-ovi usklađeni s uputama_ = kako model sada može vidjeti "zadake"

### Tokenizacija

LLM vidi upite kao _sekvencu tokena_ gdje različiti modeli (ili verzije modela) mogu tokenizirati isti upit na različite načine. Budući da su LLM-ovi trenirani na tokenima (a ne na sirovom tekstu), način na koji se upiti tokeniziraju ima izravan utjecaj na kvalitetu generiranog odgovora.

Da biste stekli intuiciju o tome kako tokenizacija funkcionira, isprobajte alate poput [OpenAI Tokenizatora](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) prikazanog dolje. Kopirajte svoj upit - i pogledajte kako se to pretvara u tokene, obraćajući pažnju na to kako se rukuje znakovima razmaka i interpunkcijskim znakovima. Imajte na umu da ovaj primjer prikazuje stariji LLM (GPT-3) - pa pokušaj s novijim modelom može dati drugačiji rezultat.

### Koncept: Osnovni modeli

Nakon što je upit tokeniziran, primarna funkcija ["Osnovnog LLM-a"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (ili Osnovnog modela) je predvidjeti token u toj sekvenci. Budući da su LLM-ovi trenirani na masivnim skupovima podataka, imaju dobar osjećaj za statističke odnose između tokena i mogu napraviti to predviđanje s određenim povjerenjem. Imajte na umu da ne razumiju _značenje_ riječi u upitu ili tokenu; oni samo vide uzorak koji mogu "dovršiti" svojim sljedećim predviđanjem. Oni mogu nastaviti predviđati sekvencu dok ih korisnik ne prekine ili dok se ne ispuni neki unaprijed postavljeni uvjet.

Želite li vidjeti kako funkcionira dovršavanje temeljeno na upitu? Unesite gornji upit u Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) s zadanim postavkama. Sustav je konfiguriran da tretira upite kao zahtjeve za informacijama - tako da biste trebali vidjeti dovršetak koji zadovoljava ovaj kontekst.

Ali što ako korisnik želi vidjeti nešto specifično što zadovoljava neke kriterije ili ciljeve zadatka? Tu na scenu stupaju LLM-ovi usklađeni s uputama.

### Koncept: LLM-ovi usklađeni s uputama

[LLM usklađen s uputama](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) započinje s osnovnim modelom i fino ga podešava s primjerima ili parovima ulaz/izlaz (npr. višekratnim "porukama") koji mogu sadržavati jasne upute - i odgovor AI-ja pokušava slijediti tu uputu.

Ovo koristi tehnike poput učenja pojačanja s povratnim informacijama ljudi (RLHF) koje mogu trenirati model da _slijedi upute_ i _uči iz povratnih informacija_ kako bi proizvodio odgovore koji su bolje prilagođeni praktičnim primjenama i relevantniji za korisničke ciljeve.

Isprobajmo - vratite se na gornji upit, ali sada promijenite _sustavsku poruku_ kako biste pružili sljedeću uputu kao kontekst:

> _Sažmi sadržaj koji ti je dostavljen za učenika drugog razreda. Zadrži rezultat na jednom odlomku s 3-5 točaka._

Vidite li kako je rezultat sada usklađen s željenim ciljem i formatom? Nastavnik sada može izravno koristiti ovaj odgovor u svojim prezentacijama za taj razred.

## Zašto nam je potrebno projektiranje upita?

Sada kada znamo kako LLM-ovi obrađuju upite, razgovarajmo o _zašto_ nam je potrebno projektiranje upita. Odgovor leži u činjenici da trenutni LLM-ovi postavljaju niz izazova koji otežavaju _pouzdano i dosljedno dovršavanje_ bez ulaganja truda u konstrukciju i optimizaciju upita. Na primjer:

1. **Odgovori modela su stohastički.** _Isti upit_ vjerojatno će proizvesti različite odgovore s različitim modelima ili verzijama modela. I može čak proizvesti različite rezultate s _istim modelom_ u različitim vremenima. _Tehnike projektiranja upita mogu nam pomoći da minimiziramo te varijacije pružanjem boljih ograda_.

2. **Modeli mogu izmišljati odgovore.** Modeli su unaprijed obučeni s _velikim, ali konačnim_ skupovima podataka, što znači da im nedostaje znanje o pojmovima izvan tog opsega obuke. Kao rezultat toga, mogu proizvesti dovršetke koji su netočni, izmišljeni ili izravno proturječni poznatim činjenicama. _Tehnike projektiranja upita pomažu korisnicima identificirati i ublažiti takve izmišljotine, npr. traženjem AI-ja za citatima ili razlozima_.

3. **Sposobnosti modela će varirati.** Noviji modeli ili generacije modela imat će bogatije sposobnosti, ali također donose jedinstvene hirove i kompromise u troškovima i složenosti. _Projektiranje upita može nam pomoći da razvijemo najbolje prakse i tijekove rada koji apstrahiraju razlike i prilagođavaju se zahtjevima specifičnim za model na skalabilan, besprijekoran način_.

Pogledajmo ovo u akciji u OpenAI ili Azure OpenAI Playground:

- Koristite isti upit s različitim LLM implementacijama (npr. OpenAI, Azure OpenAI, Hugging Face) - jeste li vidjeli varijacije?
- Koristite isti upit više puta s _istom_ LLM implementacijom (npr. Azure OpenAI playground) - kako su se te varijacije razlikovale?

### Primjer izmišljotina

U ovom tečaju koristimo izraz **"izmišljotina"** kako bismo označili fenomen gdje LLM-ovi ponekad generiraju činjenično netočne informacije zbog ograničenja u svojoj obuci ili drugim ograničenjima. Možda ste također čuli da se to naziva _"halucinacijama"_ u popularnim člancima ili istraživačkim radovima. Međutim, snažno preporučujemo korištenje izraza _"izmišljotina"_ kako ne bismo slučajno antropomorfizirali ponašanje pripisujući ljudsku osobinu ishodu koji pokreće stroj. Ovo također pojačava [smjernice za odgovornu AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) iz perspektive terminologije, uklanjajući termine koji se u nekim kontekstima također mogu smatrati uvredljivima ili neinkluzivnima.

Želite li dobiti osjećaj kako izmišljotine funkcioniraju? Zamislite upit koji upućuje AI da generira sadržaj za nepostojeću temu (kako bi se osiguralo da nije pronađena u skupu podataka za obuku). Na primjer - isprobao sam ovaj upit:

> **Upit:** generiraj plan lekcije o Marsovskom ratu 2076.

Web pretraga mi je pokazala da postoje izmišljeni prikazi (npr. televizijske serije ili knjige) o Marsovskim ratovima - ali nijedan 2076. Zdrav razum nam također govori da je 2076. _u budućnosti_ i stoga se ne može povezati s stvarnim događajem.

Pa što se događa kada pokrenemo ovaj upit s različitim pružateljima LLM-a?

Kao što se očekivalo, svaki model (ili verzija modela) proizvodi malo drugačije odgovore zahvaljujući stohastičkom ponašanju i varijacijama u sposobnostima modela. Na primjer, jedan model cilja publiku osmog razreda, dok drugi pretpostavlja srednjoškolskog učenika. Ali svi su modeli generirali odgovore koji bi mogli uvjeriti neinformiranog korisnika da je događaj stvaran.

Tehnike projektiranja upita poput _metapromptiranja_ i _konfiguracije temperature_ mogu smanjiti izmišljotine modela do određene mjere. Nove _arhitekture_ projektiranja upita također besprijekorno integriraju nove alate i tehnike u tijek upita kako bi ublažile ili smanjile neke od ovih efekata.

## Studija slučaja: GitHub Copilot

Završimo ovaj odjeljak dobivanjem osjećaja za to kako se projektiranje upita koristi u stvarnim rješenjima, pogledom na jednu Studiju slučaja: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot je vaš "AI parni programer" - pretvara tekstualne upite u dovršetke koda i integriran je u vaše razvojno okruženje (npr. Visual Studio Code) za besprijekorno korisničko iskustvo. Kao što je dokumentirano u seriji blogova u nastavku, najranija verzija temeljila se na OpenAI Codex modelu - s inženjerima
Konačna vrijednost predložaka leži u sposobnosti stvaranja i objavljivanja _biblioteka promptova_ za vertikalne domene primjene - gdje je predložak prompta sada _optimiziran_ kako bi odražavao kontekst specifičan za aplikaciju ili primjere koji čine odgovore relevantnijima i točnijima za ciljanu publiku korisnika. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) repozitorij je izvrstan primjer ovog pristupa, kreirajući biblioteku promptova za obrazovni domen s naglaskom na ključne ciljeve kao što su planiranje lekcija, dizajn kurikuluma, podučavanje studenata itd.

## Pomoćni Sadržaj

Ako razmišljamo o konstrukciji promptova kao o zadatku (instrukciji) i cilju (primarni sadržaj), tada je _sekundarni sadržaj_ poput dodatnog konteksta koji pružamo kako bismo **na neki način utjecali na ishod**. To mogu biti parametri podešavanja, upute za formatiranje, taksonomije tema itd. koji mogu pomoći modelu da _prilagodi_ svoj odgovor kako bi odgovarao željenim ciljevima ili očekivanjima korisnika.

Na primjer: Dajući katalog tečajeva s opsežnim metapodacima (naziv, opis, razina, oznake metapodataka, instruktor itd.) o svim dostupnim tečajevima u kurikulumu:

- možemo definirati instrukciju za "sažimanje kataloga tečajeva za jesen 2023."
- možemo koristiti primarni sadržaj da pružimo nekoliko primjera željenog ishoda
- možemo koristiti sekundarni sadržaj da identificiramo top 5 "oznaka" od interesa.

Sada, model može pružiti sažetak u formatu prikazanom kroz nekoliko primjera - ali ako rezultat ima više oznaka, može dati prioritet 5 oznaka identificiranih u sekundarnom sadržaju.

---

<!--
PREDLOŽAK LEKCIJE:
Ova jedinica treba pokriti osnovni koncept #1.
Ojačajte koncept s primjerima i referencama.

KONCEPT #3:
Tehnike Inženjeringa Promptova.
Koje su neke osnovne tehnike za inženjering promptova?
Ilustrirajte to s nekim vježbama.
-->

## Najbolje Prakse za Promptiranje

Sada kada znamo kako se promptovi mogu _konstruirati_, možemo početi razmišljati o tome kako ih _dizajnirati_ da odražavaju najbolje prakse. Možemo o tome razmišljati u dva dijela - imati pravi _mentalni sklop_ i primijeniti prave _tehnike_.

### Mentalni Sklop za Inženjering Promptova

Inženjering promptova je proces pokušaja i pogrešaka, pa imajte na umu tri široka čimbenika:

1. **Razumijevanje Domena je važno.** Točnost i relevantnost odgovora funkcija je _domena_ u kojem ta aplikacija ili korisnik djeluje. Primijenite svoju intuiciju i stručnost u domeni kako biste dodatno **prilagodili tehnike**. Na primjer, definirajte _specifične osobnosti za domenu_ u vašim sistemskim promptovima ili koristite _specifične predloške za domenu_ u vašim korisničkim promptovima. Pružite sekundarni sadržaj koji odražava kontekste specifične za domenu ili koristite _specifične znakove i primjere za domenu_ kako biste vodili model prema poznatim obrascima korištenja.

2. **Razumijevanje Modela je važno.** Znamo da su modeli po prirodi stohastički. Ali implementacije modela također mogu varirati u pogledu skupa podataka za obuku koji koriste (prethodno naučeno znanje), mogućnosti koje pružaju (npr. putem API-ja ili SDK-a) i vrste sadržaja za koje su optimizirani (npr. kod vs. slike vs. tekst). Razumijte snage i ograničenja modela koji koristite i koristite to znanje za _prioritizaciju zadataka_ ili izgradnju _prilagođenih predložaka_ optimiziranih za sposobnosti modela.

3. **Iteracija i Validacija su važne.** Modeli se brzo razvijaju, kao i tehnike za inženjering promptova. Kao stručnjak za domenu, možda imate drugi kontekst ili kriterije za _vašu_ specifičnu primjenu, koji možda ne vrijede za širu zajednicu. Koristite alate i tehnike za inženjering promptova da "započnete" konstrukciju promptova, a zatim iterirajte i validirajte rezultate koristeći vlastitu intuiciju i stručnost u domeni. Zabilježite svoje uvide i stvorite **bazu znanja** (npr. biblioteke promptova) koja se može koristiti kao nova osnovica od strane drugih, za brže iteracije u budućnosti.

## Najbolje Prakse

Pogledajmo sada uobičajene najbolje prakse koje preporučuju [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) i [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) praktičari.

| Što                                | Zašto                                                                                                                                                                                                                                             |
| :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Procijenite najnovije modele.      | Nova generacija modela vjerojatno će imati poboljšane značajke i kvalitetu - ali može također donijeti veće troškove. Procijenite ih za utjecaj, a zatim donesite odluke o migraciji.                                                             |
| Odvojite upute i kontekst          | Provjerite definira li vaš model/davatelj _graničnike_ kako bi jasnije razlikovao upute, primarni i sekundarni sadržaj. To može pomoći modelima da točnije dodijele težine tokenima.                                                              |
| Budite specifični i jasni          | Dajte više detalja o željenom kontekstu, ishodu, duljini, formatu, stilu itd. To će poboljšati i kvalitetu i dosljednost odgovora. Uhvatite recepte u ponovno upotrebljivim predlošcima.                                                          |
| Budite opisni, koristite primjere  | Modeli mogu bolje odgovarati na pristup "pokaži i reci". Počnite s `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
| Use cues to jumpstart completions | Nudge it towards a desired outcome by giving it some leading words or phrases that it can use as a starting point for the response.                                                                                                               |
| Double Down                       | Sometimes you may need to repeat yourself to the model. Give instructions before and after your primary content, use an instruction and a cue, etc. Iterate & validate to see what works.                                                         |
| Order Matters                     | The order in which you present information to the model may impact the output, even in the learning examples, thanks to recency bias. Try different options to see what works best.                                                               |
| Give the model an “out”           | Give the model a _fallback_ completion response it can provide if it cannot complete the task for any reason. This can reduce chances of models generating false or fabricated responses.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

As with any best practice, remember that _your mileage may vary_ based on the model, the task and the domain. Use these as a starting point, and iterate to find what works best for you. Constantly re-evaluate your prompt engineering process as new models and tools become available, with a focus on process scalability and response quality.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Assignment

Congratulations! You made it to the end of the lesson! It's time to put some of those concepts and techniques to the test with real examples!

For our assignment, we'll be using a Jupyter Notebook with exercises you can complete interactively. You can also extend the Notebook with your own Markdown and Code cells to explore ideas and techniques on your own.

### To get started, fork the repo, then

- (Recommended) Launch GitHub Codespaces
- (Alternatively) Clone the repo to your local device and use it with Docker Desktop
- (Alternatively) Open the Notebook with your preferred Notebook runtime environment.

### Next, configure your environment variables

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` vrijednostima. Vratite se na [Odjeljak Sandbox za učenje](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) da naučite kako.

### Zatim, otvorite Jupyter Notebook

- Odaberite runtime kernel. Ako koristite opcije 1 ili 2, jednostavno odaberite zadani Python 3.10.x kernel koji pruža razvojni kontejner.

Sve je spremno za izvođenje vježbi. Imajte na umu da ovdje nema _točnih i netočnih_ odgovora - samo istražujemo opcije metodom pokušaja i pogrešaka i gradimo intuiciju za ono što funkcionira za određeni model i domenu primjene.

_Iz tog razloga u ovoj lekciji nema segmenata s rješenjem koda. Umjesto toga, Notebook će imati Markdown ćelije naslovljene "Moje rješenje:" koje prikazuju jedan primjer izlaza za referencu._

 <!--
PREDLOŽAK LEKCIJE:
Završite odjeljak sa sažetkom i resursima za samostalno učenje.
-->

## Provjera Znanja

Koji od sljedećih je dobar prompt koji slijedi neke razumne najbolje prakse?

1. Pokaži mi sliku crvenog automobila
2. Pokaži mi sliku crvenog automobila marke Volvo i modela XC90 parkiranog uz liticu sa zalaskom sunca
3. Pokaži mi sliku crvenog automobila marke Volvo i modela XC90

A: 2, to je najbolji prompt jer pruža detalje o "čemu" i ide u specifičnosti (ne samo bilo koji automobil, već određena marka i model) i također opisuje cjelokupni ambijent. 3 je sljedeći najbolji jer također sadrži puno opisa.

## 🚀 Izazov

Provjerite možete li iskoristiti tehniku "znaka" s promptom: Dovršite rečenicu "Pokaži mi sliku crvenog automobila marke Volvo i ". S čime odgovara i kako biste to poboljšali?

## Odličan Rad! Nastavite Učiti

Želite li saznati više o različitim konceptima Inženjeringa Promptova? Idite na [stranicu za kontinuirano učenje](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste pronašli druge izvrsne resurse o ovoj temi.

Idite na Lekciju 5 gdje ćemo pogledati [napredne tehnike promptiranja](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Odricanje odgovornosti**:
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne odgovaramo za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.