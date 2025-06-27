<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-06-25T13:35:49+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "hr"
}
-->
# Osnove inženjeringa prompta

## Uvod
Ovaj modul pokriva osnovne pojmove i tehnike za stvaranje učinkovitih prompta u generativnim AI modelima. Način na koji pišete svoj prompt prema LLM-u također je važan. Pažljivo izrađen prompt može postići bolju kvalitetu odgovora. No, što točno znače pojmovi poput _prompt_ i _inženjering prompta_? I kako mogu poboljšati unos prompta koji šaljem LLM-u? To su pitanja na koja ćemo pokušati odgovoriti u ovom poglavlju i sljedećem.

_Generativni AI_ sposoban je stvarati novi sadržaj (npr. tekst, slike, audio, kod itd.) kao odgovor na korisničke zahtjeve. To postiže korištenjem _velikih jezičnih modela_ poput OpenAI-jevog GPT ("Generative Pre-trained Transformer") serije koji su obučeni za korištenje prirodnog jezika i koda.

Korisnici sada mogu komunicirati s ovim modelima koristeći poznate paradigme poput chata, bez potrebe za tehničkim znanjem ili obukom. Modeli su _temeljeni na promptu_ - korisnici šalju tekstualni unos (prompt) i dobivaju AI odgovor (dovršetak). Oni zatim mogu "razgovarati s AI-jem" iterativno, u višestrukim razgovorima, usavršavajući svoj prompt dok odgovor ne zadovolji njihova očekivanja.

"Prompti" sada postaju primarno _programsko sučelje_ za generativne AI aplikacije, govoreći modelima što trebaju učiniti i utječući na kvalitetu vraćenih odgovora. "Inženjering prompta" je brzo rastuće područje studija koje se fokusira na _dizajn i optimizaciju_ prompta kako bi se isporučili dosljedni i kvalitetni odgovori u velikom obimu.

## Ciljevi učenja

U ovoj lekciji učimo što je inženjering prompta, zašto je važan i kako možemo izraditi učinkovitije prompte za određeni model i cilj aplikacije. Razumjet ćemo osnovne pojmove i najbolje prakse za inženjering prompta - i naučiti o interaktivnom Jupyter Notebooks "sandbox" okruženju gdje možemo vidjeti kako se ovi koncepti primjenjuju na stvarnim primjerima.

Na kraju ove lekcije moći ćemo:

1. Objasniti što je inženjering prompta i zašto je važan.
2. Opisati komponente prompta i kako se koriste.
3. Naučiti najbolje prakse i tehnike za inženjering prompta.
4. Primijeniti naučene tehnike na stvarne primjere, koristeći OpenAI endpoint.

## Ključni pojmovi

Inženjering prompta: Praksa dizajniranja i usavršavanja unosa za usmjeravanje AI modela prema proizvodnji željenih izlaza.
Tokenizacija: Proces pretvaranja teksta u manje jedinice, zvane tokeni, koje model može razumjeti i obraditi.
LLM-ovi prilagođeni instrukcijama: Veliki jezični modeli (LLM-ovi) koji su fino podešeni s posebnim uputama kako bi poboljšali točnost i relevantnost svojih odgovora.

## Sandbox za učenje

Inženjering prompta trenutno je više umjetnost nego znanost. Najbolji način za poboljšanje intuicije za njega je _više vježbati_ i usvojiti pristup pokušaja i pogrešaka koji kombinira stručnost u domeni aplikacije s preporučenim tehnikama i optimizacijama specifičnim za model.

Jupyter Notebook koji prati ovu lekciju pruža _sandbox_ okruženje gdje možete isprobati ono što naučite - dok idete ili kao dio izazova s kodom na kraju. Da biste izvršili vježbe, trebat će vam:

1. **Azure OpenAI API ključ** - krajnja točka usluge za implementirani LLM.
2. **Python Runtime** - u kojem se Notebook može izvršiti.
3. **Lokalne varijable okruženja** - _dovršite [POSTAVKE](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) korake sada da biste se pripremili_.

Notebook dolazi s _početnim_ vježbama - ali potičemo vas da dodate vlastite _Markdown_ (opis) i _Code_ (zahtjevi prompta) sekcije kako biste isprobali više primjera ili ideja - i izgradili svoju intuiciju za dizajn prompta.

## Ilustrirani vodič

Želite li dobiti cjelokupnu sliku o tome što ova lekcija pokriva prije nego što se upustite? Pogledajte ovaj ilustrirani vodič, koji vam daje osjećaj glavnih tema koje se pokrivaju i ključnih zaključaka o kojima trebate razmišljati u svakom od njih. Plan lekcije vodi vas od razumijevanja osnovnih pojmova i izazova do rješavanja istih s relevantnim tehnikama inženjeringa prompta i najboljim praksama. Imajte na umu da se sekcija "Napredne tehnike" u ovom vodiču odnosi na sadržaj obrađen u _sljedećem_ poglavlju ovog kurikuluma.

## Naš startup

Sada, razgovarajmo o tome kako _ova tema_ ima veze s našom misijom startupa da [donesemo AI inovaciju u obrazovanje](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Želimo izgraditi AI-pokretane aplikacije za _personalizirano učenje_ - pa razmislimo o tome kako različiti korisnici naše aplikacije mogu "dizajnirati" prompte:

- **Administratori** mogu tražiti od AI-ja da _analizira podatke kurikuluma kako bi identificirao praznine u pokrivenosti_. AI može sažeti rezultate ili ih vizualizirati s kodom.
- **Edukatori** mogu tražiti od AI-ja da _generira plan lekcije za ciljnu publiku i temu_. AI može izraditi personalizirani plan u određenom formatu.
- **Studenti** mogu tražiti od AI-ja da ih _podučava u teškom predmetu_. AI sada može voditi studente s lekcijama, savjetima i primjerima prilagođenim njihovoj razini.

To je samo vrh ledenog brijega. Pogledajte [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - otvoreni izvorni biblioteku prompta koju su kurirali stručnjaci za obrazovanje - kako biste dobili širi osjećaj mogućnosti! _Pokušajte pokrenuti neke od tih prompta u sandboxu ili koristeći OpenAI Playground da vidite što se događa!_

## Što je inženjering prompta?

Započeli smo ovu lekciju definirajući **inženjering prompta** kao proces _dizajniranja i optimizacije_ tekstualnih unosa (promptova) za isporuku dosljednih i kvalitetnih odgovora (dovršetaka) za određeni cilj aplikacije i model. Možemo to smatrati procesom u dva koraka:

- _dizajniranje_ početnog prompta za određeni model i cilj
- _usavršavanje_ prompta iterativno kako bi se poboljšala kvaliteta odgovora

To je nužno proces pokušaja i pogrešaka koji zahtijeva korisničku intuiciju i trud kako bi se postigli optimalni rezultati. Zašto je to važno? Da bismo odgovorili na to pitanje, prvo moramo razumjeti tri koncepta:

- _Tokenizacija_ = kako model "vidi" prompt
- _Osnovni LLM-ovi_ = kako osnovni model "obrađuje" prompt
- _LLM-ovi prilagođeni instrukcijama_ = kako model sada može vidjeti "zadate"

### Tokenizacija

LLM vidi prompte kao _sekvencu tokena_ gdje različiti modeli (ili verzije modela) mogu tokenizirati isti prompt na različite načine. Budući da su LLM-ovi obučeni na tokenima (a ne na sirovom tekstu), način na koji se prompti tokeniziraju ima izravan utjecaj na kvalitetu generiranog odgovora.

Da biste stekli intuiciju o tome kako tokenizacija funkcionira, isprobajte alate poput [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) prikazanog dolje. Kopirajte svoj prompt - i vidite kako se pretvara u tokene, obraćajući pažnju na to kako se rukuje s bijelim znakovima i interpunkcijskim znakovima. Napomena: ovaj primjer prikazuje stariji LLM (GPT-3) - pa pokušaj s novijim modelom može proizvesti drugačiji rezultat.

### Koncept: Osnovni modeli

Jednom kada je prompt tokeniziran, primarna funkcija ["Osnovnog LLM-a"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (ili Osnovnog modela) je predvidjeti token u toj sekvenci. Budući da su LLM-ovi obučeni na masivnim tekstualnim skupovima podataka, imaju dobar osjećaj za statističke odnose između tokena i mogu napraviti to predviđanje s određenim povjerenjem. Imajte na umu da ne razumiju _značenje_ riječi u promptu ili tokenu; oni samo vide uzorak koji mogu "dovršiti" svojim sljedećim predviđanjem. Oni mogu nastaviti predviđati sekvencu sve dok ih ne prekine korisnička intervencija ili neki unaprijed utvrđeni uvjet.

Želite vidjeti kako funkcionira dovršavanje temeljeno na promptu? Unesite gornji prompt u Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) s zadanim postavkama. Sustav je konfiguriran da tretira prompte kao zahtjeve za informacijama - pa biste trebali vidjeti dovršetak koji zadovoljava ovaj kontekst.

Ali što ako korisnik želi vidjeti nešto specifično što ispunjava neke kriterije ili ciljeve zadatka? Tu dolaze _LLM-ovi prilagođeni instrukcijama_.

### Koncept: LLM-ovi prilagođeni instrukcijama

[LLM prilagođen instrukcijama](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) započinje s osnovnim modelom i fino ga podešava s primjerima ili parovima ulaz/izlaz (npr. višestrukim "porukama") koje mogu sadržavati jasne upute - i AI odgovor pokušava slijediti tu uputu.

Ovo koristi tehnike poput učenja pojačanja s povratnim informacijama od ljudi (RLHF) koje mogu obučiti model da _slijedi upute_ i _uči iz povratnih informacija_ tako da proizvodi odgovore koji su bolje prilagođeni praktičnim primjenama i relevantniji za korisničke ciljeve.

Pokušajmo - ponovite gornji prompt, ali sada promijenite _sustavsku poruku_ da pružite sljedeću uputu kao kontekst:

> _Sažmi sadržaj koji ti je dan za učenika drugog razreda. Zadrži rezultat u jednom odlomku s 3-5 točaka._

Vidite kako je rezultat sada prilagođen da odražava željeni cilj i format? Edukator sada može izravno koristiti ovaj odgovor u svojim slajdovima za taj razred.

## Zašto nam treba inženjering prompta?

Sada kada znamo kako prompti obrađuju LLM-ovi, razgovarajmo o _zašto_ nam treba inženjering prompta. Odgovor leži u činjenici da trenutni LLM-ovi postavljaju niz izazova koji čine _pouzdane i dosljedne dovršetke_ izazovnijima za postizanje bez ulaganja truda u konstrukciju i optimizaciju prompta. Na primjer:

1. **Odgovori modela su stohastički.** _Isti prompt_ vjerojatno će proizvesti različite odgovore s različitim modelima ili verzijama modela. A može čak proizvesti različite rezultate s _istim modelom_ u različitim vremenima. _Tehnike inženjeringa prompta mogu nam pomoći minimizirati te varijacije pružanjem boljih ograda_.

2. **Modeli mogu izmišljati odgovore.** Modeli su unaprijed obučeni s _velikim, ali konačnim_ skupovima podataka, što znači da im nedostaje znanje o konceptima izvan tog obuhvata obuke. Kao rezultat toga, mogu proizvesti dovršetke koji su netočni, izmišljeni ili izravno proturječni poznatim činjenicama. _Tehnike inženjeringa prompta pomažu korisnicima identificirati i ublažiti takve izmišljotine, npr. traženjem AI-ja za citate ili razloge_.

3. **Sposobnosti modela će varirati.** Noviji modeli ili generacije modela imat će bogatije sposobnosti, ali će također donijeti jedinstvene hirove i kompromisi u troškovima i složenosti. _Inženjering prompta može nam pomoći razviti najbolje prakse i radne tokove koji apstrahiraju razlike i prilagođavaju se zahtjevima specifičnim za model na skalabilne, besprijekorne načine_.

Pogledajmo to u akciji u OpenAI ili Azure OpenAI Playgroundu:

- Koristite isti prompt s različitim LLM implementacijama (npr. OpenAI, Azure OpenAI, Hugging Face) - jeste li vidjeli varijacije?
- Koristite isti prompt više puta s _istom_ LLM implementacijom (npr. Azure OpenAI playground) - kako su se te varijacije razlikovale?

### Primjer izmišljotina

U ovom tečaju koristimo pojam **"izmišljotina"** kako bismo se referirali na fenomen gdje LLM-ovi ponekad generiraju činjenično netočne informacije zbog ograničenja u njihovoj obuci ili drugim ograničenjima. Možda ste također čuli da se to naziva _"halucinacijama"_ u popularnim člancima ili istraživačkim radovima. Međutim, snažno preporučujemo korištenje termina _"izmišljotina"_ kako ne bismo slučajno antropomorfizirali ponašanje pripisujući ljudsku osobinu rezultatu vođenom strojem. Ovo također jača [smjernice za odgovorni AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) s terminološke perspektive, uklanjajući termine koji se također mogu smatrati uvredljivima ili neuključivima u nekim kontekstima.

Želite li dobiti osjećaj kako izmišljotine funkcioniraju? Smislite prompt koji instruira AI da generira sadržaj za nepostojeću temu (kako bi se osiguralo da se ne nalazi u skupu podataka za obuku). Na primjer - pokušao sam s ovim promptom:

> **Prompt:** generiraj plan lekcije o Marsovskom ratu 2076.

Web pretraga pokazala mi je da postoje fikcionalni prikazi (npr. televizijske serije ili knjige) o Marsovskim ratovima - ali nijedan u 2076. Zdrav razum nam također govori da je 2076. _u budućnosti_ i stoga ne može biti povezan s stvarnim događajem.

Pa što se događa kada pokrenemo ovaj prompt s različitim LLM pružateljima?

> **Odgovor 1**: OpenAI Playground (GPT-35)

> **Odgovor 2**: Azure OpenAI Playground (GPT-35)

> **Odgovor 3**: : Hugging Face Chat Playground (LLama-2)

Kao što se očekivalo, svaki model (ili verzija modela) proizvodi malo drugačije odgovore zahvaljujući stohastičkom ponašanju i varijacijama sposobnosti modela. Na primjer, jedan model cilja publiku osmog razreda dok drugi pretpostavlja srednjoškolskog učenika. Ali svi tri modela generirali su odgovore koji bi mogli uvjeriti neupućenog korisnika da je događaj stvaran.

Tehnike inženjeringa prompta poput _metapromptiranja_ i _konfiguracije temperature_ mogu donekle smanjiti izmišljotine modela. Nove _arhitekture_ inženjeringa prompta također besprijekorno ugrađuju nove alate i tehnike u tok prompta kako bi ublažile ili smanjile neke od tih učinaka.

## Studija slučaja: GitHub Copilot

Završimo ovaj odjeljak stjecanjem osjećaja kako se inženjering prompta koristi u stvarnim rješenjima gledajući jednu studiju slučaja: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot je vaš "AI par programer" - pretvara tekstualne prompte u kodne dovršetke
Konačna vrijednost predložaka leži u mogućnosti stvaranja i objavljivanja _biblioteka upita_ za vertikalne domene aplikacija - gdje je predložak upita sada _optimiziran_ kako bi odražavao kontekst specifičan za aplikaciju ili primjere koji čine odgovore relevantnijima i točnijima za ciljanu publiku korisnika. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) repozitorij je izvrstan primjer ovog pristupa, koji kurira biblioteku upita za obrazovni sektor s naglaskom na ključne ciljeve poput planiranja lekcija, dizajna kurikuluma, podučavanja studenata itd.

## Podrška sadržaju

Ako razmišljamo o konstrukciji upita kao zadatku (task) i cilju (primarni sadržaj), tada je _sekundarni sadržaj_ poput dodatnog konteksta koji pružamo da **utječemo na izlaz na neki način**. To mogu biti parametri podešavanja, upute za formatiranje, taksonomije tema itd. koje mogu pomoći modelu da _prilagodi_ svoj odgovor kako bi odgovarao željenim ciljevima ili očekivanjima korisnika.

Na primjer: S obzirom na katalog tečajeva s opsežnim metapodacima (ime, opis, razina, oznake metapodataka, instruktor itd.) o svim dostupnim tečajevima u kurikulumu:

- možemo definirati uputu da "sažmemo katalog tečajeva za jesen 2023."
- možemo koristiti primarni sadržaj da pružimo nekoliko primjera željenog izlaza
- možemo koristiti sekundarni sadržaj da identificiramo top 5 "oznaka" interesa.

Sada, model može pružiti sažetak u formatu prikazanom kroz nekoliko primjera - ali ako rezultat ima više oznaka, može prioritizirati 5 oznaka identificiranih u sekundarnom sadržaju.

---

<!--
PREDLOŽAK LEKCIJE:
Ova jedinica treba pokriti osnovni koncept #1.
Ojačajte koncept primjerima i referencama.

KONCEPT #3:
Tehnike inženjeringa upita.
Koje su osnovne tehnike za inženjering upita?
Ilustrirajte to nekim vježbama.
-->

## Najbolje prakse za upite

Sada kada znamo kako se upiti mogu _konstruirati_, možemo početi razmišljati o tome kako ih _dizajnirati_ da odražavaju najbolje prakse. Možemo razmišljati o tome u dva dijela - imati pravi _mentalni sklop_ i primjenjivati prave _tehnike_.

### Mentalni sklop inženjeringa upita

Inženjering upita je proces pokušaja i pogreške, stoga imajte na umu tri široka vodiča:

1. **Razumijevanje domene je važno.** Točnost i relevantnost odgovora funkcija su _domene_ u kojoj ta aplikacija ili korisnik djeluje. Primijenite svoju intuiciju i stručnost u domeni da **prilagodite tehnike** dalje. Na primjer, definirajte _osobnosti specifične za domenu_ u svojim sistemskim upitima ili koristite _predloške specifične za domenu_ u svojim korisničkim upitima. Pružite sekundarni sadržaj koji odražava kontekste specifične za domenu ili koristite _znakove i primjere specifične za domenu_ kako biste vodili model prema poznatim obrascima korištenja.

2. **Razumijevanje modela je važno.** Znamo da su modeli stohastički po prirodi. No, implementacije modela također mogu varirati u smislu skupa podataka za obuku koji koriste (predtrenirano znanje), sposobnosti koje pružaju (npr. putem API-ja ili SDK-a) i vrste sadržaja za koje su optimizirani (npr. kod vs. slike vs. tekst). Razumijte snage i ograničenja modela koji koristite i koristite to znanje da _prioritizirate zadatke_ ili izgradite _prilagođene predloške_ koji su optimizirani za sposobnosti modela.

3. **Iteracija i validacija su važni.** Modeli se brzo razvijaju, kao i tehnike za inženjering upita. Kao stručnjak za domenu, možete imati drugi kontekst ili kriterije _vaše_ specifične aplikacije, koji možda ne vrijede za širu zajednicu. Koristite alate i tehnike inženjeringa upita da "pokrenete" konstrukciju upita, zatim iterirajte i validirajte rezultate koristeći vlastitu intuiciju i stručnost u domeni. Zabilježite svoje uvide i stvorite **bazu znanja** (npr. biblioteke upita) koja može poslužiti kao nova osnova za druge, za brže iteracije u budućnosti.

## Najbolje prakse

Sada pogledajmo uobičajene najbolje prakse koje preporučuju [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) i [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) praktičari.

| Što                                | Zašto                                                                                                                                                                                                                                               |
| :--------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Evaluirajte najnovije modele.      | Nova generacija modela vjerojatno ima poboljšane značajke i kvalitetu - ali može također uzrokovati veće troškove. Evaluirajte ih za utjecaj, zatim donesite odluke o migraciji.                                                                       |
| Odvojite upute i kontekst          | Provjerite definira li vaš model/provajder _graničnike_ za jasnije razlikovanje uputa, primarnog i sekundarnog sadržaja. To može pomoći modelima da točnije dodijele težine tokenima.                                                                    |
| Budite specifični i jasni          | Dajte više detalja o željenom kontekstu, ishodu, duljini, formatu, stilu itd. To će poboljšati kvalitetu i dosljednost odgovora. Zabilježite recepte u predloške koji se mogu ponovno koristiti.                                                        |
| Budite opisni, koristite primjere  | Modeli mogu bolje reagirati na pristup "pokaži i reci". Započnite s `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
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

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` vrijednostima. Vratite se na [sekciju Sandbox za učenje](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) kako biste naučili kako.

### Zatim, otvorite Jupyter Notebook

- Odaberite jezgru za pokretanje. Ako koristite opcije 1 ili 2, jednostavno odaberite zadanu Python 3.10.x jezgru koju pruža razvojni kontejner.

Spremni ste za pokretanje vježbi. Imajte na umu da ovdje nema _ispravnih i pogrešnih_ odgovora - samo istražujemo opcije metodom pokušaja i pogreške i gradimo intuiciju o tome što funkcionira za određeni model i domenu aplikacije.

_Iz tog razloga nema segmenata rješenja koda u ovoj lekciji. Umjesto toga, Notebook će imati Markdown ćelije naslovljene "Moje rješenje:" koje prikazuju jedan primjer izlaza za referencu._

<!--
PREDLOŽAK LEKCIJE:
Završite sekciju sa sažetkom i resursima za samostalno učenje.
-->

## Provjera znanja

Koji od sljedećih je dobar upit koji slijedi neke razumne najbolje prakse?

1. Pokaži mi sliku crvenog automobila
2. Pokaži mi sliku crvenog automobila marke Volvo i modela XC90 parkiranog kraj litice s zalaskom sunca
3. Pokaži mi sliku crvenog automobila marke Volvo i modela XC90

A: 2, to je najbolji upit jer pruža detalje o "čemu" i ulazi u specifičnosti (ne samo bilo koji automobil, već određena marka i model) te također opisuje ukupni ambijent. 3 je sljedeći najbolji jer također sadrži puno opisa.

## 🚀 Izazov

Pogledajte možete li iskoristiti tehniku "znaka" s upitom: Dovrši rečenicu "Pokaži mi sliku crvenog automobila marke Volvo i ". Što odgovara i kako biste to poboljšali?

## Sjajan rad! Nastavite s učenjem

Želite li saznati više o različitim konceptima inženjeringa upita? Idite na [stranicu za nastavak učenja](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste pronašli druge sjajne resurse o ovoj temi.

Uputite se na Lekciju 5 gdje ćemo pogledati [napredne tehnike upita](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden koristeći AI uslugu prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako se trudimo postići točnost, molimo vas da budete svjesni da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na njegovom izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne odgovaramo za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.