<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-05-19T16:24:09+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "sr"
}
-->
# Osnovi projektovanja upita

## Uvod
Ovaj modul pokriva osnovne pojmove i tehnike za kreiranje efektivnih upita u generativnim AI modelima. Način na koji pišete svoj upit prema LLM-u je takođe bitan. Pažljivo sastavljen upit može postići bolji kvalitet odgovora. Ali šta tačno znače termini kao što su _upit_ i _projektovanje upita_? I kako mogu poboljšati _ulazni_ upit koji šaljem LLM-u? Ovo su pitanja na koja ćemo pokušati da odgovorimo u ovom poglavlju i sledećem.

_Generativni AI_ je sposoban da stvara novi sadržaj (npr. tekst, slike, zvuk, kod itd.) kao odgovor na zahteve korisnika. To postiže koristeći _velike jezičke modele_ kao što je OpenAI-jev GPT ("Generativni unapred trenirani transformator") serijal koji je obučen za korišćenje prirodnog jezika i koda.

Korisnici sada mogu komunicirati s ovim modelima koristeći poznate paradigme poput četa, bez potrebe za tehničkom ekspertizom ili obukom. Modeli su _bazirani na upitima_ - korisnici šalju tekstualni unos (upit) i dobijaju AI odgovor (kompletiranje). Oni zatim mogu "razgovarati sa AI" iterativno, u višekratnim razgovorima, usavršavajući svoj upit dok odgovor ne odgovara njihovim očekivanjima.

"Upiti" sada postaju primarni _programski interfejs_ za generativne AI aplikacije, govoreći modelima šta da rade i utičući na kvalitet vraćenih odgovora. "Projektovanje upita" je brzo rastuće polje proučavanja koje se fokusira na _dizajn i optimizaciju_ upita kako bi se isporučili dosledni i kvalitetni odgovori u velikom obimu.

## Ciljevi učenja

U ovoj lekciji učimo šta je projektovanje upita, zašto je važno i kako možemo kreirati efikasnije upite za određeni model i ciljeve aplikacije. Razumećemo osnovne pojmove i najbolje prakse za projektovanje upita - i naučiti o interaktivnom Jupyter Notebooks "sandbox" okruženju gde možemo videti ove koncepte primenjene na stvarne primere.

Na kraju ove lekcije moći ćemo da:

1. Objasnimo šta je projektovanje upita i zašto je važno.
2. Opišemo komponente upita i kako se koriste.
3. Naučimo najbolje prakse i tehnike za projektovanje upita.
4. Primijenimo naučene tehnike na stvarne primere, koristeći OpenAI endpoint.

## Ključni pojmovi

Projektovanje upita: Praksa dizajniranja i usavršavanja unosa kako bi se AI modeli usmerili ka proizvodnji željenih izlaza.  
Tokenizacija: Proces pretvaranja teksta u manje jedinice, zvane tokeni, koje model može razumeti i obraditi.  
LLM-ovi podešeni za instrukcije: Veliki jezički modeli (LLM) koji su fino podešeni sa specifičnim instrukcijama kako bi poboljšali tačnost i relevantnost odgovora.

## Sandbox za učenje

Projektovanje upita je trenutno više umetnost nego nauka. Najbolji način da poboljšamo našu intuiciju za to je da _vežbamo više_ i usvojimo pristup pokušaja i grešaka koji kombinuje ekspertizu u domeni primene sa preporučenim tehnikama i optimizacijama specifičnim za model.

Jupyter Notebook koji prati ovu lekciju pruža _sandbox_ okruženje gde možete isprobati ono što učite - dok idete ili kao deo izazova kodiranja na kraju. Da biste izvršili vežbe, biće vam potrebno:

1. **Azure OpenAI API ključ** - krajnja tačka usluge za postavljeni LLM.
2. **Python Runtime** - u kojem se Notebook može izvršiti.
3. **Lokalne promenljive okruženja** - _završite [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) korake sada da biste bili spremni_.

Notebook dolazi sa _početnim_ vežbama - ali se ohrabrujete da dodate svoje _Markdown_ (opis) i _Code_ (zahtevi za upitima) sekcije kako biste isprobali više primera ili ideja - i izgradili svoju intuiciju za dizajn upita.

## Ilustrovani vodič

Želite da dobijete širu sliku o tome šta ova lekcija pokriva pre nego što se upustite u nju? Pogledajte ovaj ilustrovani vodič, koji vam daje osećaj glavnih tema pokrivenih i ključnih zaključaka o kojima treba razmisliti u svakoj od njih. Mapa puta lekcije vodi vas od razumevanja osnovnih koncepata i izazova do njihovog rešavanja relevantnim tehnikama i najboljim praksama projektovanja upita. Imajte na umu da se odeljak "Napredne tehnike" u ovom vodiču odnosi na sadržaj pokriven u _sledećem_ poglavlju ovog kurikuluma.

## Naš startup

Sada, hajde da razgovaramo o tome kako se _ova tema_ odnosi na našu startup misiju da [donesemo AI inovacije u obrazovanje](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Želimo da izgradimo AI aplikacije za _personalizovano učenje_ - pa razmislimo o tome kako bi različiti korisnici naše aplikacije mogli da "dizajniraju" upite:

- **Administratori** bi mogli tražiti od AI da _analizira podatke o kurikulumu kako bi identifikovao praznine u pokrivenosti_. AI može sumirati rezultate ili ih vizualizovati pomoću koda.
- **Nastavnici** bi mogli tražiti od AI da _generiše plan lekcije za ciljnu publiku i temu_. AI može izgraditi personalizovani plan u određenom formatu.
- **Učenici** bi mogli tražiti od AI da ih _podučava u teškom predmetu_. AI sada može voditi učenike kroz lekcije, savete i primere prilagođene njihovom nivou.

To je samo vrh ledenog brega. Pogledajte [Upite za obrazovanje](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - biblioteku upita otvorenog koda koju su kurirali stručnjaci za obrazovanje - da biste dobili širu predstavu o mogućnostima! _Pokušajte pokrenuti neke od tih upita u sandboxu ili koristeći OpenAI Playground da vidite šta se dešava!_

## Šta je projektovanje upita?

Započeli smo ovu lekciju definišući **projektovanje upita** kao proces _dizajniranja i optimizacije_ tekstualnih unosa (upita) kako bi se isporučili dosledni i kvalitetni odgovori (kompletiranja) za određeni cilj aplikacije i model. Možemo misliti o tome kao o procesu u 2 koraka:

- _dizajniranje_ početnog upita za određeni model i cilj
- _usavršavanje_ upita iterativno kako bi se poboljšao kvalitet odgovora

Ovo je nužno proces pokušaja i grešaka koji zahteva intuiciju i trud korisnika kako bi se postigli optimalni rezultati. Zašto je to važno? Da bismo odgovorili na to pitanje, prvo moramo razumeti tri koncepta:

- _Tokenizacija_ = kako model "vidi" upit
- _Osnovni LLM-ovi_ = kako osnovni model "obrađuje" upit
- _LLM-ovi podešeni za instrukcije_ = kako model sada može videti "zadate"

### Tokenizacija

LLM vidi upite kao _niz tokena_ gde različiti modeli (ili verzije modela) mogu tokenizovati isti upit na različite načine. Pošto su LLM-ovi obučeni na tokenima (a ne na sirovom tekstu), način na koji se upiti tokenizuju ima direktan uticaj na kvalitet generisanog odgovora.

Da biste stekli intuiciju o tome kako tokenizacija funkcioniše, isprobajte alate kao što je [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) prikazan ispod. Kopirajte svoj upit - i vidite kako se to pretvara u tokene, obraćajući pažnju na to kako se rukuje belim prostorima i znakovima interpunkcije. Imajte na umu da ovaj primer prikazuje stariji LLM (GPT-3) - pa pokušaj sa novijim modelom može proizvesti drugačiji rezultat.

### Koncept: Osnovni modeli

Kada se upit tokenizuje, primarna funkcija ["Osnovnog LLM-a"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (ili osnovnog modela) je da predvidi token u tom nizu. Pošto su LLM-ovi obučeni na ogromnim skupovima tekstualnih podataka, imaju dobar osećaj za statističke odnose između tokena i mogu napraviti to predviđanje sa određenim stepenom pouzdanosti. Imajte na umu da oni ne razumeju _značenje_ reči u upitu ili tokenu; samo vide obrazac koji mogu "dovršiti" svojim sledećim predviđanjem. Oni mogu nastaviti da predviđaju niz dok ih korisnik ne prekine ili dok se ne ispuni neki unapred utvrđeni uslov.

Želite da vidite kako funkcioniše dovršavanje bazirano na upitima? Unesite gornji upit u Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) sa podrazumevanim postavkama. Sistem je konfigurisana da tretira upite kao zahteve za informacijama - tako da biste trebali videti kompletiranje koje zadovoljava ovaj kontekst.

Ali šta ako korisnik želi da vidi nešto specifično što zadovoljava neke kriterijume ili ciljeve zadatka? Ovo je gde _LLM-ovi podešeni za instrukcije_ dolaze u obzir.

### Koncept: LLM-ovi podešeni za instrukcije

[LLM podešen za instrukcije](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) počinje sa osnovnim modelom i fino ga podešava primerima ili parovima ulaz/izlaz (npr., višekratne "poruke") koje mogu sadržavati jasne instrukcije - i odgovor AI pokušava da sledi tu instrukciju.

Ovo koristi tehnike kao što je Reinforcement Learning with Human Feedback (RLHF) koje mogu trenirati model da _sledi instrukcije_ i _uči iz povratnih informacija_ kako bi proizvodio odgovore koji su bolje prilagođeni praktičnim aplikacijama i relevantniji za ciljeve korisnika.

Hajde da to isprobamo - ponovo posetite gornji upit, ali sada promenite _sistemsku poruku_ da pruži sledeću instrukciju kao kontekst:

> _Sumirajte sadržaj koji vam je dat za učenika drugog razreda. Zadržite rezultat na jedan paragraf sa 3-5 tačaka._

Vidite kako je rezultat sada podešen da odražava željeni cilj i format? Nastavnik sada može direktno koristiti ovaj odgovor u svojim slajdovima za tu klasu.

## Zašto nam je potrebno projektovanje upita?

Sada kada znamo kako se upiti obrađuju od strane LLM-ova, hajde da razgovaramo o tome _zašto_ nam je potrebno projektovanje upita. Odgovor leži u činjenici da trenutni LLM-ovi postavljaju niz izazova koji čine _pouzdana i dosledna kompletiranja_ izazovnijim za postizanje bez truda u konstrukciji i optimizaciji upita. Na primer:

1. **Odgovori modela su stohastički.** _Isti upit_ će verovatno proizvesti različite odgovore sa različitim modelima ili verzijama modela. A može čak i proizvesti različite rezultate sa _istim modelom_ u različito vreme. _Tehnike projektovanja upita mogu nam pomoći da minimiziramo ove varijacije pružanjem boljih ograda_.

1. **Modeli mogu fabrikovati odgovore.** Modeli su prethodno obučeni sa _velikim ali konačnim_ skupovima podataka, što znači da im nedostaje znanje o konceptima izvan tog opsega obuke. Kao rezultat toga, mogu proizvesti kompletiranja koja su netačna, izmišljena ili direktno kontradiktorna poznatim činjenicama. _Tehnike projektovanja upita pomažu korisnicima da identifikuju i ublaže takve fabrikacije npr., traženjem od AI citata ili rezonovanja_.

1. **Sposobnosti modela će varirati.** Noviji modeli ili generacije modela će imati bogatije sposobnosti, ali takođe donose jedinstvene osobenosti i kompromise u troškovima i složenosti. _Projektovanje upita može nam pomoći da razvijemo najbolje prakse i tokove rada koji apstrahuju razlike i prilagođavaju se specifičnim zahtevima modela na skalabilne, besprekorne načine_.

Hajde da to vidimo u akciji u OpenAI ili Azure OpenAI Playground:

- Koristite isti upit sa različitim LLM implementacijama (npr, OpenAI, Azure OpenAI, Hugging Face) - da li ste videli varijacije?
- Koristite isti upit više puta sa _istom_ LLM implementacijom (npr., Azure OpenAI playground) - kako su se ove varijacije razlikovale?

### Primer fabrikacija

U ovom kursu koristimo termin **"fabrikacija"** da se pozovemo na fenomen kada LLM-ovi ponekad generišu činjenično netačne informacije zbog ograničenja u svojoj obuci ili drugim ograničenjima. Možda ste takođe čuli da se ovo naziva _"halucinacije"_ u popularnim člancima ili istraživačkim radovima. Međutim, snažno preporučujemo korišćenje termina _"fabrikacija"_ kako ne bismo slučajno antropomorfizovali ponašanje pripisujući ljudsku osobinu ishodu vođenom mašinom. Ovo takođe pojačava [smernice odgovornog AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) iz perspektive terminologije, uklanjajući termine koji se takođe mogu smatrati uvredljivim ili neuključivim u nekim kontekstima.

Želite da steknete osećaj kako fabrikacije funkcionišu? Razmislite o upitu koji instruira AI da generiše sadržaj za nepostojeću temu (da biste osigurali da se ne nalazi u skupu podataka za obuku). Na primer - pokušao sam ovaj upit:

> **Upit:** generišite plan lekcije o Marsovskom ratu 2076. godine.

Pretraga na vebu mi je pokazala da su postojali fiktivni prikazi (npr., televizijske serije ili knjige) o Marsovskim ratovima - ali nijedan 2076. godine. Zdrav razum nam takođe govori da je 2076. godina _u budućnosti_ i stoga ne može biti povezana sa stvarnim događajem.

Dakle, šta se dešava kada pokrenemo ovaj upit sa različitim LLM provajderima?

Kao što se očekivalo, svaki model (ili verzija modela) proizvodi malo drugačije odgovore zahvaljujući stohastičkom ponašanju i varijacijama sposobnosti modela. Na primer, jedan model cilja publiku 8. razreda, dok drugi pretpostavlja srednjoškolca. Ali sva tri modela su generisala odgovore koji bi mogli uveriti neinformisanog korisnika da je događaj stvaran.

Tehnike projektovanja upita kao što su _metaprompting_ i _konfiguracija temperature_ mogu smanjiti fabrikacije modela do određenog stepena. Nove _arhitekture_ projektovanja upita takođe besprekorno integrišu nove alate i tehnike u tok upita, kako bi ublažile ili smanjile neke od ovih efekata.

## Studija slučaja: GitHub Copilot

Hajde da završimo ovaj deo tako što ćemo steći osećaj kako se projektovanje upita koristi u stvarnim rešenjima gledajući jednu studiju slučaja: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot je vaš "AI par programer" - pretvara tekstualne upite u kompletiranja koda i integrisan je u vaše razvojno okruženje (npr., Visual Studio Code) za besprekorno korisničko iskustvo. Kao što je dokumentovano u seriji blogova ispod, najranija verzija je bila zasnovana na OpenAI Codex modelu - sa inženjerima koji su brzo
Konačna vrednost šablona leži u sposobnosti da se kreiraju i objavljuju _biblioteke promptova_ za vertikalne domene aplikacija - gde je prompt šablon sada _optimizovan_ da odražava kontekst specifičan za aplikaciju ili primere koji čine odgovore relevantnijim i tačnijim za ciljanu korisničku publiku. Repozitorijum [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) je odličan primer ovog pristupa, prikupljajući biblioteku promptova za obrazovni domen sa naglaskom na ključne ciljeve poput planiranja lekcija, dizajna kurikuluma, podučavanja učenika itd.

## Pomoćni sadržaj

Ako razmislimo o konstrukciji prompta kao o zadatku (task) i cilju (primarni sadržaj), onda je _sekundarni sadržaj_ kao dodatni kontekst koji pružamo da **na neki način utičemo na ishod**. To mogu biti parametri podešavanja, uputstva za formatiranje, taksonomije tema itd. koje mogu pomoći modelu da _prilagodi_ svoj odgovor da bude u skladu sa željenim korisničkim ciljevima ili očekivanjima.

Na primer: Dat katalog kurseva sa obimnim metapodacima (ime, opis, nivo, metapodaci, instruktor itd.) o svim dostupnim kursevima u kurikulumu:

- možemo definisati uputstvo da "sumiramo katalog kurseva za jesen 2023"
- možemo koristiti primarni sadržaj da pružimo nekoliko primera željenog izlaza
- možemo koristiti sekundarni sadržaj da identifikujemo top 5 "tagova" od interesa.

Sada, model može pružiti sažetak u formatu prikazanom kroz nekoliko primera - ali ako rezultat ima više tagova, može dati prioritet 5 tagova identifikovanih u sekundarnom sadržaju.

## Najbolje prakse za kreiranje promptova

Sada kada znamo kako se promptovi mogu _konstruisati_, možemo početi da razmišljamo o tome kako ih _dizajnirati_ da odražavaju najbolje prakse. Možemo razmišljati o tome u dva dela - imati pravi _način razmišljanja_ i primeniti prave _tehnike_.

### Način razmišljanja za kreiranje promptova

Kreiranje promptova je proces pokušaja i greške, pa imajte na umu tri široka vodiča:

1. **Razumevanje domena je važno.** Tačnost i relevantnost odgovora je funkcija _domena_ u kojem ta aplikacija ili korisnik deluje. Primeni svoju intuiciju i stručnost u domenu da **dalje prilagodiš tehnike**. Na primer, definiši _ličnosti specifične za domen_ u sistemskim promptovima ili koristi _šablone specifične za domen_ u korisničkim promptovima. Pruži sekundarni sadržaj koji odražava kontekste specifične za domen, ili koristi _signale i primere specifične za domen_ da usmeriš model ka poznatim obrascima korišćenja.

2. **Razumevanje modela je važno.** Znamo da su modeli stohastički po prirodi. Ali implementacije modela takođe mogu varirati u smislu skupa podataka za obuku koji koriste (prethodno naučeno znanje), sposobnosti koje pružaju (npr. putem API-ja ili SDK-a) i tipa sadržaja za koji su optimizovani (npr. kod vs. slike vs. tekst). Razumite prednosti i ograničenja modela koji koristite i koristite to znanje da _dajte prioritet zadacima_ ili izgradite _prilagođene šablone_ koji su optimizovani za sposobnosti modela.

3. **Iteracija i validacija su važni.** Modeli se brzo razvijaju, kao i tehnike za kreiranje promptova. Kao stručnjak za domen, možda imate drugi kontekst ili kriterijume za _vašu_ specifičnu aplikaciju, koji možda ne važe za širu zajednicu. Koristite alate i tehnike za kreiranje promptova da "pokrenete" konstrukciju prompta, a zatim iterirajte i validirajte rezultate koristeći svoju intuiciju i stručnost u domenu. Zabeležite svoja saznanja i kreirajte **bazu znanja** (npr. biblioteke promptova) koja se može koristiti kao nova osnova za brže iteracije u budućnosti.

## Najbolje prakse

Pogledajmo sada uobičajene najbolje prakse koje preporučuju [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) i [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) praktičari.

| Šta                               | Zašto                                                                                                                                                                                                                                               |
| :-------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Proceni najnovije modele.         | Nove generacije modela verovatno imaju poboljšane karakteristike i kvalitet - ali mogu takođe doneti veće troškove. Proceni ih za uticaj, a zatim donesi odluke o migraciji.                                                                          |
| Odvoj instrukcije i kontekst      | Proveri da li tvoj model/provajder definiše _delimitere_ da jasnije razlikuje instrukcije, primarni i sekundarni sadržaj. Ovo može pomoći modelima da tačnije dodeljuju težine tokenima.                                                                 |
| Budi specifičan i jasan           | Daj više detalja o željenom kontekstu, ishodu, dužini, formatu, stilu itd. Ovo će poboljšati i kvalitet i doslednost odgovora. Uhvatite recepte u ponovo upotrebljivim šablonima.                                                                     |
| Budi opisivan, koristi primere    | Modeli mogu bolje reagovati na pristup "pokaži i ispričaj". Počni sa `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
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

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` vrednostima. Vratite se u [Learning Sandbox sekciju](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) da naučite kako.

### Sledeće, otvorite Jupyter Notebook

- Izaberite jezgro za izvršavanje. Ako koristite opcije 1 ili 2, jednostavno izaberite podrazumevano Python 3.10.x jezgro koje pruža dev kontejner.

Sve je spremno za pokretanje vežbi. Imajte na umu da ovde nema _tačnih i netačnih_ odgovora - samo istražujemo opcije putem pokušaja i greške i gradimo intuiciju za ono što funkcioniše za dati model i domen aplikacije.

_Iz tog razloga u ovoj lekciji nema segmenata sa rešenjem koda. Umesto toga, Notebook će imati Markdown ćelije pod nazivom "My Solution:" koje prikazuju jedan primer izlaza za referencu._

## Provera znanja

Koji od sledećih je dobar prompt koji prati neke razumne najbolje prakse?

1. Pokaži mi sliku crvenog automobila
2. Pokaži mi sliku crvenog automobila marke Volvo i modela XC90 parkiranog kraj litice dok sunce zalazi
3. Pokaži mi sliku crvenog automobila marke Volvo i modela XC90

A: 2, to je najbolji prompt jer pruža detalje o "čemu" i ide u specifičnosti (ne samo bilo koji auto već specifična marka i model) i takođe opisuje celokupno okruženje. 3 je sledeći najbolji jer takođe sadrži mnogo opisa.

## 🚀 Izazov

Pogledajte da li možete iskoristiti tehniku "cue" sa promptom: Završite rečenicu "Pokaži mi sliku crvenog automobila marke Volvo i ". Šta odgovara, i kako biste to poboljšali?

## Odlično! Nastavite sa učenjem

Želite li da saznate više o različitim konceptima za kreiranje promptova? Idite na [stranicu za nastavak učenja](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) da pronađete druge sjajne resurse na ovu temu.

Pređite na Lekciju 5 gde ćemo pogledati [napredne tehnike promptovanja](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Одричање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да будемо прецизни, имајте на уму да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални људски превод. Не сносимо одговорност за било каква неспоразума или погрешна тумачења која произилазе из употребе овог превода.