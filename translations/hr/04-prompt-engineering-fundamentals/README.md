# Osnove projektiranja prompta

[![Osnove projektiranja prompta](../../../translated_images/hr/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Uvod
Ovaj modul pokriva osnovne pojmove i tehnike za izradu učinkovitih promptova u modelima generativne umjetne inteligencije. Način na koji napišete svoj prompt za LLM također je važan. Pažljivo izrađen prompt može postići bolju kvalitetu odgovora. Ali što zapravo znače pojmovi poput _prompt_ i _projektiranje prompta_? I kako mogu poboljšati prompt _unosa_ koji šaljem LLM-u? To su pitanja na koja ćemo pokušati odgovoriti u ovom i sljedećem poglavlju.

_Generativna AI_ sposobna je stvarati novi sadržaj (npr. tekst, slike, zvuk, kod itd.) kao odgovor na korisničke zahtjeve. Postiže to korištenjem _velikih jezičnih modela_ poput OpenAI-jeve GPT ("Generative Pre-trained Transformer") serije koji su trenirani za rad s prirodnim jezikom i kodom.

Korisnici sada mogu komunicirati s tim modelima koristeći poznate paradigme poput chata, bez potrebe za tehničkim znanjem ili treningom. Modeli su _temeljeni na promptovima_ - korisnici šalju tekstualni unos (prompt) i dobivaju AI odgovor (dovršetak). Potom mogu "razgovarati s AI-jem" iterativno, u višekratnim krugovima konverzacije, usavršavajući svoj prompt dok odgovor ne zadovolji njihova očekivanja.

"Promptovi" sada postaju primarno _programersko sučelje_ za aplikacije generativne AI, govoreći modelima što da rade i utječući na kvalitetu dobivenih odgovora. "Projektiranje prompta" je brzo rastuće područje proučavanja koje se fokusira na _dizajn i optimizaciju_ promptova kako bi se isporučivali dosljedni i kvalitetni odgovori u velikom opsegu.

## Ciljevi učenja

U ovoj lekciji učimo što je projektiranje prompta, zašto je važno i kako možemo napraviti učinkovitije promptove za određeni model i cilj aplikacije. Razumjet ćemo osnovne pojmove i najbolje prakse za projektiranje prompta - te upoznati interaktivno Jupyter Notebook "sandbox" okruženje u kojem možemo vidjeti primjenu tih pojmova na stvarnim primjerima.

Do kraja ove lekcije moći ćemo:

1. Objasniti što je projektiranje prompta i zašto je važno.
2. Opisati komponente prompta i kako se koriste.
3. Naučiti najbolje prakse i tehnike za projektiranje prompta.
4. Primijeniti naučene tehnike na stvarne primjere, koristeći OpenAI endpoint.

## Ključni pojmovi

Projektiranje prompta: Praksa dizajniranja i usavršavanja unosa za usmjerenje AI modela prema željenim izlazima.
Tokenizacija: Proces pretvaranja teksta u manje jedinice, zvane tokeni, koje model može razumjeti i obraditi.
Instrukcijski podešeni LLM-ovi: Veliki jezični modeli koji su dodatno podešeni posebnim uputama za poboljšanje točnosti i relevantnosti njihovih odgovora.

## Okruženje za učenje

Projektiranje prompta trenutačno je više umjetnost nego znanost. Najbolji način da poboljšamo intuiciju za to je _vježbati više_ i usvojiti pristup pokušaja i pogreške koji kombinira stručnost iz područja primjene s preporučenim tehnikama i optimizacijama specifičnim za model.

Jupyter Notebook koji prati ovu lekciju pruža _sandbox_ okruženje gdje možete isprobati naučeno – tijekom rada ili kao dio izazova na kraju. Za izvođenje vježbi trebate:

1. **API ključ za Azure OpenAI** – servisni endpoint za implementirani LLM.
2. **Python Runtime** – u kojem Notebook može biti izvršen.
3. **Lokalne varijable okoline** – _sada dovršite korake [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) da se pripremite_.

Notebook dolazi s _početnim_ vježbama – ali potičemo vas da dodate vlastite _Markdown_ (opisne) i _Kod_ (zahtjeve prompta) dijelove za isprobavanje više primjera ili ideja – kako biste izgradili intuiciju za dizajn prompta.

## Ilustrirani vodič

Želite li dobiti širu sliku onoga što ova lekcija pokriva prije nego što se upustite u detalje? Pogledajte ovaj ilustrirani vodič, koji vam daje osjećaj glavnih tema i ključnih spoznaja o kojima treba razmisliti u svakoj. Putokaz lekcije vodi vas od razumijevanja osnovnih pojmova i izazova do njihova rješavanja relevantnim tehnikama i najboljim praksama projektiranja prompta. Napomena da odjeljak "Napredne tehnike" u ovom vodiču odnosi se na sadržaj obrađen u _sljedećem_ poglavlju ovog kurikuluma.

![Ilustrirani vodič za projektiranje prompta](../../../translated_images/hr/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Naš startup

Sada razgovarajmo o tome kako se _ova tema_ odnosi na našu misiju startupa da [donesemo AI inovacije u obrazovanje](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Želimo izgraditi AI-pokretane aplikacije za _personalizirano učenje_ – pa razmislimo o tome kako različiti korisnici naše aplikacije mogu "dizajnirati" promptove:

- **Administratori** mogu tražiti od AI-ja da _analizira podatke o kurikulumu kako bi identificirao praznine u pokrivenosti_. AI može sažeti rezultate ili ih vizualizirati uz pomoć koda.
- **Nastavnici** mogu tražiti od AI-ja da _generira plan lekcije za ciljanu publiku i temu_. AI može izraditi personalizirani plan u određenom formatu.
- **Učenici** mogu tražiti od AI-ja da _ih podučava o složenom predmetu_. AI sada može voditi učenike s lekcijama, uputama i primjerima prilagođenima njihovoj razini.

To je samo vrh sante leda. Pogledajte [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – otvorenu biblioteku promptova koju su pripremili stručnjaci za obrazovanje – za širi dojam mogućnosti! _Pokušajte pokrenuti neke od tih promptova u sandboxu ili koristite OpenAI Playground da vidite što se događa!_

<!--
ŠABLON LEKCIJE:
Ovaj dio treba obuhvatiti osnovni pojam #1.
Ojačajte pojam primjerima i referencama.

POJAM #1:
Projektiranje prompta.
Definirajte ga i objasnite zašto je potreban.
-->

## Što je projektiranje prompta?

Lekciju smo započeli definiranjem **projektiranja prompta** kao procesa _dizajniranja i optimiziranja_ tekstualnih unosa (promptova) kako bi se isporučili dosljedni i kvalitetni odgovori (dovršetci) za određeni cilj aplikacije i model. Možemo to smatrati dvostupanjskim procesom:

- _dizajniranje_ početnog prompta za određeni model i cilj
- _usavršavanje_ prompta iterativno radi poboljšanja kvalitete odgovora

To je nužno proces pokušaja i pogreške koji zahtijeva korisničku intuiciju i trud za postizanje optimalnih rezultata. Zašto je to važno? Da bismo odgovorili na to pitanje, prvo trebamo razumjeti tri pojma:

- _Tokenizacija_ = kako model "vidi" prompt
- _Osnovni LLM-ovi_ = kako temeljni model "obrađuje" prompt
- _Instrukcijski podešeni LLM-ovi_ = kako model sada može vidjeti "zadatke"

### Tokenizacija

LLM vidi promtove kao _sekvencu tokena_ gdje različiti modeli (ili verzije modela) mogu tokenizirati isti prompt na različite načine. Budući da su LLM-i trenirani na tokenima (a ne na sirovom tekstu), način na koji su promptovi tokenizirani ima izravan utjecaj na kvalitetu generiranog odgovora.

Da biste stekli intuiciju kako tokenizacija funkcionira, isprobajte alate poput [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) prikazanog ispod. Zalijepite svoj prompt – i vidite kako se pretvara u tokene, obraćajući pažnju na to kako se tretiraju razmaci i interpunkcijski znakovi. Napomena: ovaj primjer pokazuje stariji LLM (GPT-3) – pa isprobavanje s novijim modelom može dati drugačiji rezultat.

![Tokenizacija](../../../translated_images/hr/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Pojam: Temeljni modeli

Nakon što je prompt tokeniziran, glavna funkcija ["Osnovnog LLM-a"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (ili temeljni model) je predvidjeti sljedeći token u toj sekvenci. Budući da su LLM-ovi trenirani na ogromnim skupovima podataka teksta, dobro poznaju statističke veze između tokena i mogu tu predikciju napraviti s određenim stupnjem sigurnosti. Napomena, oni ne razumiju _značenje_ riječi u promptu ili tokenu; oni samo vide obrazac koji mogu "dovršiti" sljedećom predikcijom. Mogu nastaviti predviđati sekvencu dok ih korisnik ne zaustavi ili se neka unaprijed utvrđena uvjet zadovolji.

Želite li vidjeti kako funkcionira dovršetak temeljen na promptu? Unesite gore navedeni prompt u [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) s zadanim postavkama. Sustav je konfiguriran da tretira promptove kao zahtjeve za informacijama – pa biste trebali vidjeti dovršetak koji zadovoljava taj kontekst.

Ali što ako korisnik želi vidjeti nešto specifično što zadovoljava neke kriterije ili cilj zadatka? Tada na scenu stupaju _instrukcijski podešeni_ LLM-ovi.

![Dovršetak chata osnovnog LLM-a](../../../translated_images/hr/04-playground-chat-base.65b76fcfde0caa67.webp)

### Pojam: Instrukcijski podešeni LLM-ovi

[Instrukcijski podešeni LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) počinje s temeljnim modelom i dodatno ga podešava s primjerima ili ulazno-izlaznim parovima (npr. višekratnim "porukama") koje mogu sadržavati jasne upute – a odgovor AI-ja pokušava slijediti tu uputu.

Koriste se tehnike poput učenja pojačanog povratnom informacijom od ljudi (RLHF) koje mogu trenirati model da _sluša upute_ i _uči iz povratnih informacija_ tako da proizvodi odgovore prikladnije za praktične primjene i relevantnije za korisničke ciljeve.

Isprobajmo – vratite se na prethodni prompt, ali sada promijenite _poruku sustava_ da pružite sljedeću uputu kao kontekst:

> _Sažmi sadržaj koji ti se da za učenika drugog razreda. Zadrži rezultat u jednom odlomku s 3-5 točaka._

Vidite li kako je rezultat sada usklađen s željenim ciljem i formatom? Nastavnik sada može izravno koristiti ovaj odgovor u svojim prezentacijama za tu nastavu.

![Dovršetak chata instrukcijski podešenog LLM-a](../../../translated_images/hr/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Zašto nam treba projektiranje prompta?

Sad kad znamo kako LLM-ovi obrađuju promptove, razgovarajmo o _zašto_ nam treba projektiranje prompta. Odgovor leži u činjenici da trenutačni LLM-ovi predstavljaju niz izazova koji otežavaju postizanje _pouzdanih i dosljednih dovršetaka_ bez truda uloženog u konstrukciju i optimizaciju prompta. Na primjer:

1. **Odgovori modela su stohastički.** _Isti prompt_ vjerojatno će proizvesti različite odgovore s različitim modelima ili verzijama modela. Može također proizvesti različite rezultate s _istim modelom_ u različito vrijeme. _Tehnike projektiranja prompta mogu nam pomoći smanjiti te varijacije pružajući bolje smjernice_.

1. **Modeli mogu izmišljati odgovore.** Modeli su prethodno trenirani na _velikim, ali ograničenim_ skupovima podataka, što znači da nemaju znanje o konceptima izvan tog područja treniranja. Kao rezultat, mogu proizvesti dovršetke koji su netočni, izmišljeni ili izravno proturječe poznatim činjenicama. _Tehnike projektiranja prompta pomažu korisnicima da prepoznaju i smanje takve izmišljotine, npr. traženjem od AI-ja da navede izvore ili obrazloženje_.

1. **Sposobnosti modela variraju.** Noviji modeli ili generacije modela imat će bogatije sposobnosti, ali i jedinstvene specifičnosti i kompromise u troškovima i složenosti. _Projektiranje prompta može nam pomoći razviti najbolje prakse i radne tokove koji apstrahiraju razlike i prilagođavaju se zahtjevima specifičnim za model na skalabilan i besprijekoran način_.

Pogledajmo to u praksi u OpenAI ili Azure OpenAI Playgroundu:

- Koristite isti prompt s različitim implementacijama LLM-a (npr. OpenAI, Azure OpenAI, Hugging Face) – jeste li vidjeli varijacije?
- Koristite isti prompt ponovo i ponovo s _istom_ implementacijom LLM-a (npr. Azure OpenAI playground) – kako su se te varijacije razlikovale?

### Primjer izmišljotina

U ovom tečaju koristimo izraz **"izmišljotina"** za fenomen gdje LLM-ovi ponekad generiraju činjenicama netočne informacije zbog ograničenja u njihovom treningu ili drugim uvjetima. Možda ste ovaj fenomen čuli i pod nazivom _"halucinacije"_ u popularnim člancima ili znanstvenim radovima. Međutim, snažno preporučujemo korištenje termina _"izmišljotina"_ kako bismo izbjegli antropomorfiziranje ponašanja davanjem ljudske osobine stroju. Ovo također pojačava [smjernice za odgovornu AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) s perspektive terminologije, uklanjajući izraze koji se mogu smatrati uvredljivima ili neinkluzivnima u nekim kontekstima.

Želite li dobiti dojam kako izmišljotine funkcioniraju? Zamislite prompt koji upućuje AI da generira sadržaj za nepostojeću temu (kako biste osigurali da je nema u trening skupu podataka). Primjerice – probao sam ovaj prompt:

> **Prompt:** generiraj plan lekcije o Martijskoj ratu 2076.

Pretraživanje na webu pokazalo mi je da postoje fikcionalni prikazi (npr. televizijske serije ili knjige) o martijanskim ratovima – ali nijedan iz 2076. Zdrav razum također nalaže da je 2076. _u budućnosti_ te stoga ne može biti povezan s nekim stvarnim događajem.


Što se događa kada pokrenemo ovaj upit s različitim pružateljima LLM-a?

> **Odgovor 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/hr/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Odgovor 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/hr/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Odgovor 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/hr/04-fabrication-huggingchat.faf82a0a51278956.webp)

Kao što se i očekivalo, svaki model (ili verzija modela) daje malo drugačije odgovore zahvaljujući stohastičkom ponašanju i varijacijama sposobnosti modela. Na primjer, jedan model cilja na publiku osmog razreda, dok drugi pretpostavlja srednjoškolca. No sva tri modela su generirala odgovore koji bi mogli uvjeriti neupućenog korisnika da je događaj stvaran.

Tehnike inženjerstva upita poput _metapromptinga_ i _konfiguracije temperature_ mogu donekle smanjiti izmišljotine modela. Nove _arhitekture_ inženjerstva upita također neprimjetno uključuju nove alate i tehnike u tijek upita, kako bi ublažile ili smanjile neke od ovih učinaka.

## Studija slučaja: GitHub Copilot

Završimo ovaj odjeljak dobivanjem uvida u to kako se inženjerstvo upita koristi u stvarnim rješenjima proučavanjem jedne studije slučaja: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot je vaš "AI par programer" – pretvara tekstualne upite u kompletiranja koda i integriran je u vaše razvojno okruženje (npr. Visual Studio Code) za neprimjetno korisničko iskustvo. Kao što je dokumentirano u nizu blogova ispod, najranija verzija temeljila se na OpenAI Codex modelu – a inženjeri su brzo shvatili potrebu za dodatnim podešavanjem modela i razvojem boljih tehnika inženjerstva upita kako bi poboljšali kvalitetu koda. U srpnju su [predstavili poboljšani AI model koji ide dalje od Codexa](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) za još brže prijedloge.

Pročitajte objave redom kako biste pratili njihov put učenja.

- **Svibanj 2023.** | [GitHub Copilot postaje bolji u razumijevanju vašeg koda](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Svibanj 2023.** | [Unutar GitHuba: Rad s LLM-ovima iza GitHub Copilota](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Lipanj 2023.** | [Kako pisati bolje upite za GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Srpanj 2023.** | [.. GitHub Copilot ide dalje od Codexa s poboljšanim AI modelom](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Srpanj 2023.** | [Vodič za programere za inženjerstvo upita i LLM-e](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Rujan 2023.** | [Kako izgraditi enterprise LLM aplikaciju: Lekcije iz GitHub Copilota](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Također možete pregledavati njihov [Inženjerski blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) za još postova poput [ovog](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) koji pokazuje kako se ovi modeli i tehnike _primjenjuju_ za pokretanje stvarnih aplikacija.

---

<!--
LESSON TEMPLATE:
Ova jedinica bi trebala pokriti osnovni pojam #2.
Ojačajte pojam primjerima i referencama.

Pojam #2:
Dizajn upita.
Ilustrirano primjerima.
-->

## Konstrukcija upita

Vidjeli smo zašto je inženjerstvo upita važno – sada razumimo kako se upiti _konstruiraju_ kako bismo mogli procijeniti različite tehnike za učinkovitiji dizajn upita.

### Osnovni upit

Počnimo s osnovnim upitom: unosom teksta poslanim modelu bez dodatnog konteksta. Evo primjera – kada pošaljemo prve riječi američke himne na OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), on odmah _dovršava_ odgovor s nekoliko sljedećih redaka, ilustrirajući osnovno ponašanje predviđanja.

| Upit (Unos)       | Dovršetak (Izlaz)                                                                                                                         |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Čini se da započinjete stihove "The Star-Spangled Banner," američke himne. Cijeli tekst glasi ...                                        |

### Složeni upit

Sada dodajmo kontekst i upute tom osnovnom upitu. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) dopušta nam konstruiranje složenog upita kao zbirke _poruka_ s:

- Parovima unosa/izlaza koji odražavaju unos _korisnika_ i odgovor _pomoćnika_.
- Porukom sustava koja postavlja kontekst ponašanja ili osobnosti pomoćnika.

Zahtjev je sada u obliku ispod, gdje _tokenizacija_ efektivno hvata relevantne informacije iz konteksta i razgovora. Promjena sustavnog konteksta može biti jednako utjecajna na kvalitetu dovršetaka kao i korisnički unosi.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Uputa u upitu

U gore navedenim primjerima, korisnički upit bio je jednostavan tekstualni zahtjev koji se može interpretirati kao zahtjev za informacijama. S _uputama_ u upitima možemo koristiti taj tekst za detaljnije specificiranje zadatka, pružajući bolju smjernicu AI-u. Evo primjera:

| Upit (Unos)                                                                                                                                                                                                                         | Dovršetak (Izlaz)                                                                                                        | Tip upute          |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Napiši opis građanskog rata                                                                                                                                                                                                      | _vratio je jednostavan paragraf_                                                                                          | Jednostavno         |
| Napiši opis građanskog rata. Navedi ključne datume i događaje te opiši njihov značaj                                                                                                                                                 | _vratio je paragraf praćen popisom ključnih datuma događaja s opisima_                                                   | Složeno              |
| Napiši opis građanskog rata u jednom paragrafu. Navedi 3 točke s ključnim datumima i njihovim značajima. Navedi još 3 točke s ključnim povijesnim osobama i njihovim doprinosima. Vrati ishod u JSON datoteci | _vraća detaljnije informacije u tekstualnom okviru, formatiranom kao JSON koji možete kopirati i zalijepiti u datoteku i prema potrebi provjeriti valjanost_ | Složeno. Formatirano. |

## Primarni sadržaj

U gore navedenim primjerima, upit je bio prilično otvoren, dopuštajući LLM-u da odluči koji dio svog unaprijed naučenog skupa podataka je relevantan. S dizajnom _primarnog sadržaja_, ulazni tekst je podijeljen u dva dijela:

- uputu (akciju)
- relevantni sadržaj (koji utječe na akciju)

Evo primjera gdje je uputa "sažmi ovo u 2 rečenice".

| Upit (Unos)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Dovršetak (Izlaz)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter je peta planeta od Sunca i najveća u Sunčevom sustavu. To je plinski div s masom tisuću puta manjom od Sunca, ali dva i pol puta većom od svih ostalih planeta u Sunčevom sustavu zajedno. Jupiter je jedan od najsvjetlijih objekata vidljivih golim okom na noćnom nebu i poznat je drevnim civilizacijama još prije zapisane povijesti. Ime je dobio po rimskom bogu Jupiteru.[19] Kada se gleda sa Zemlje, Jupiter može biti dovoljno svijetao da njegova reflektirajuća svjetlost baca vidljive sjene,[20] i u prosjeku je treći najsvjetliji prirodni objekt na noćnom nebu nakon Mjeseca i Venere. <br/> **Sažmi ovo u 2 kratke rečenice** | Jupiter, peta planeta od Sunca, je najveća u Sunčevom sustavu i poznata je po tome što je jedan od najsvjetlijih objekata na noćnom nebu. Ime je dobio po rimskom bogu Jupiteru, a to je plinski div čija je masa dva i pol puta veća od mase svih ostalih planeta u Sunčevom sustavu zajedno. |

Segment primarnog sadržaja može se koristiti na različite načine za učinkovitije upute:

- **Primjeri** - umjesto da se modelu eksplicitno kaže što treba napraviti, dajte mu primjere što treba raditi i neka izvuče obrazac.
- **Nagovještaji** - slijedi uputa s "nagovještajem" koji priprema dovršetak, usmjeravajući model ka relevantnijim odgovorima.
- **Predlošci** - to su ponovljivi 'recepti' za upite s rezerviranim mjestima (varijablama) koje se mogu prilagođavati podacima za specifične slučajeve.

Pogledajmo ih u praksi.

### Korištenje primjera

Ovo je pristup u kojem koristite primarni sadržaj da "hranite model" nekim primjerima željenog ishoda za zadanu uputu, i dajte mu da izvuče obrazac željenog izlaza. Na temelju broja pruženih primjera, možemo imati zero-shot upite, one-shot upite, few-shot upite itd.

Upit sada sadrži tri komponente:

- Opis zadatka
- Nekoliko primjera željenog izlaza
- Početak novog primjera (koji postaje implicitni opis zadatka)

| Tip učenja | Upit (Unos)                                                                                                                                        | Dovršetak (Izlaz)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "The Sun is Shining". Prevedi na španjolski                                                                                                         | "El Sol está brillando".    |
| One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot      | Igrač je pretrčao baze => Baseball <br/> Igrač je odigrao as => Tenis <br/> Igrač je postigao šest => Kriket <br/> Igrač je napravio zakucavanje =>     | Košarka                   |
|               |                                                                                                                                                       |                             |

Primijetite kako smo morali dati eksplicitnu uputu ("Prevedi na španjolski") u zero-shot upitu, ali to se izvuče u primjeru one-shot upita. Few-shot primjer pokazuje kako dodavanje više primjera omogućava modelima točnije zaključke bez dodatnih uputa.

### Nagovještaji u upitu

Druga tehnika za korištenje primarnog sadržaja je davanje _nagovještaja_ umjesto primjera. U ovom slučaju dajemo modelu poticaj u pravom smjeru tako što ga _početno pokrećemo_ s odlomkom koji odražava željeni format odgovora. Model tada "uzima nagovještaj" da nastavi u tom smjeru.

| Broj nagovještaja | Upit (Unos)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Dovršetak (Izlaz)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter je peta planeta od Sunca i najveća u Sunčevom sustavu. To je plinski div s masom tisuću puta manjom od Sunca, ali dva i pol puta većom od svih ostalih planeta u Sunčevom sustavu zajedno. Jupiter je jedan od najsvjetlijih objekata vidljivih golim okom na noćnom nebu i poznat je drevnim civilizacijama još prije zapisane povijesti. <br/>**Sažmi ovo**                                       | Jupiter je najveća planeta u našem Sunčevom sustavu i peta po redu od Sunca. To je plinski div s masom 1/1000 mase Sunca, ali teži od svih ostalih planeta zajedno. Drevne civilizacije poznaju Jupiter dugo vremena i lako je vidljiv na noćnom nebu. |
| 1              | Jupiter je peta planeta od Sunca i najveća u Sunčevom sustavu. To je plinski div s masom tisuću puta manjom od Sunca, ali dva i pol puta većom od svih ostalih planeta u Sunčevom sustavu zajedno. Jupiter je jedan od najsvjetlijih objekata vidljivih golim okom na noćnom nebu i poznat je drevnim civilizacijama još prije zapisane povijesti. <br/>**Sažmi ovo** <br/> Ono što smo naučili je da je Jupiter | peta planeta od Sunca i najveća u Sunčevom sustavu. To je plinski div s masom tisuću puta manjom od Sunca, ali dva i pol puta većom od mase svih ostalih planeta zajedno. Lako je vidljiv golim okom i poznat je od davnina.                       |

| 2              | Jupiter je peta planeta od Sunca i najveća u Sunčevom sustavu. To je plinski div s masom tisuću puta manjom od mase Sunca, ali dva i pol puta većom od mase svih ostalih planeta u Sunčevom sustavu zajedno. Jupiter je jedan od najsjajnijih objekata vidljivih golim okom na noćnom nebu, i poznat je drevnim civilizacijama još od prije zapisanih povijesnih zapisa. <br/>**Sažetak** <br/> Top 3 činjenice koje smo naučili:         | 1. Jupiter je peta planeta od Sunca i najveća u Sunčevom sustavu. <br/> 2. To je plinski div s masom tisuću puta manjom od mase Sunca...<br/> 3. Jupiter je vidljiv golim okom od davnina ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Predlošci upita

Predložak upita je _preddefinirani recept za upit_ koji se može pohraniti i ponovno koristiti prema potrebi, kako bi se osigurala dosljednija iskustva korisnika u većem opsegu. U svom najjednostavnijem obliku, to je samo zbirka primjera upita poput [ovog od OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) koji pruža interaktivne komponente upita (poruke korisnika i sustava) i format zahtjeva vođen API-jem - kako bi se podržala njihova ponovna upotreba.

U složenijem obliku poput [ovog primjera od LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), sadrži _zamjenske oznake_ koje se mogu zamijeniti podacima iz različitih izvora (korisnički unos, kontekst sustava, vanjski izvori podataka itd.) kako bi se dinamički generirao upit. To nam omogućuje stvaranje knjižnice ponovo upotrebljivih upita koje se mogu koristiti za dosljedna korisnička iskustva **programatski** u skali.

Konačno, prava vrijednost predložaka leži u mogućnosti stvaranja i objavljivanja _knjižnica upita_ za vertikalne domene aplikacija - gdje je predložak upita sada _optimiziran_ da odražava kontekst ili primjere specifične za aplikaciju koji čine odgovore relevantnijima i točnijima za ciljanu publiku korisnika. Spremište [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) je odličan primjer ovog pristupa, kurirajući knjižnicu upita za obrazovni sektor s naglaskom na ključne ciljeve poput planiranja lekcija, dizajna nastavnog plana, poduke učenika itd.

## Podržani sadržaj

Ako razmišljamo o konstrukciji upita kao sastavljenoj od uputa (zadatka) i cilja (primarni sadržaj), tada je _sekundarni sadržaj_ poput dodatnog konteksta koji pružamo da **na neki način utječemo na ishod**. To mogu biti parametri podešavanja, upute za formatiranje, taksonomije tema itd. koje mogu pomoći modelu da _prilagodi_ svoj odgovor kako bi odgovarao željenim ciljevima ili očekivanjima korisnika.

Na primjer: S obzirom na katalog tečajeva s opsežnim metapodacima (naziv, opis, razina, oznake metapodataka, instruktor itd.) za sve dostupne tečajeve u nastavnom planu:

- možemo definirati uputu za "sažetak kataloga tečajeva za jesen 2023."
- možemo koristiti primarni sadržaj da pružimo nekoliko primjera željenog izlaza
- možemo koristiti sekundarni sadržaj da identificiramo 5 najvažnijih "oznaka".

Sada model može pružiti sažetak u formatu prikazanom na nekoliko primjera - ali ako rezultat sadrži više oznaka, može dati prednost 5 oznaka identificiranih u sekundarnom sadržaju.

---

<!--
PREDLOŽAK LEKCIJE:
Ova sesija treba obuhvatiti osnovni pojam #1.
Potkrijepiti pojam primjerima i referencama.

POJAM #3:
Tehnike inženjerstva upita.
Koje su osnovne tehnike za inženjerstvo upita?
Ilustrirati to s nekoliko vježbi.
-->

## Najbolje prakse za upite

Sada kada znamo kako se upiti mogu _konstruirati_, možemo početi razmišljati o tome kako ih _dizajnirati_ da odražavaju najbolje prakse. Možemo to razdvojiti na dva dijela – posjedovanje pravog _načina razmišljanja_ i primjena pravih _tehnika_.

### Način razmišljanja o inženjerstvu upita

Inženjerstvo upita je proces pokušaja i pogreške pa imajte na umu tri široka vodeća faktora:

1. **Razumijevanje domena je važno.** Točnost i relevantnost odgovora ovisi o _domeni_ u kojoj ta aplikacija ili korisnik djeluju. Primijenite intuiciju i stručnost iz domene za daljnju **prilagodbu tehnika**. Na primjer, definirajte _osobnosti specifične za domenu_ u sustavnim upitima, ili koristite _predloške specifične za domenu_ u korisničkim upitima. Pružite sekundarni sadržaj koji odražava kontekste specifične za domenu, ili koristite _znakove i primjere specifične za domenu_ kako biste usmjerili model prema poznatim obrazcima upotrebe.

2. **Razumijevanje modela je važno.** Znamo da su modeli prirodno stokastički. Ali implementacije modela mogu varirati u smislu skupa podataka za obuku koji koriste (predtrenirano znanje), sposobnosti koje nude (npr. preko API-ja ili SDK-a) i vrste sadržaja za koji su optimizirani (npr. kod, slike, tekst). Razumite prednosti i ograničenja modela koji koristite i upotrijebite to znanje da _prioritizirate zadatke_ ili napravite _prilagođene predloške_ optimizirane za mogućnosti modela.

3. **Iteracija i validacija su važni.** Modeli se brzo razvijaju, kao i tehnike za inženjerstvo upita. Kao stručnjak u domeni, možda imate dodatni kontekst ili kriterije za _vašu_ specifičnu aplikaciju, koji možda ne vrijede za širu zajednicu. Koristite alate i tehnike inženjerstva upita za "brzi početak" konstrukcije upita, zatim iterirajte i validirajte rezultate koristeći vlastitu intuiciju i stručnost iz domene. Zabilježite svoja saznanja i stvorite **bazom znanja** (npr. knjižnice upita) koja drugi mogu koristiti kao novu osnovu za brže iteracije u budućnosti.

## Najbolje prakse

Pogledajmo sada uobičajene najbolje prakse koje preporučuju praktičari iz [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) i [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Što                              | Zašto                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Procijenite najnovije modele.      | Nove generacije modela vjerojatno imaju poboljšane značajke i kvalitetu - ali mogu donijeti i veće troškove. Procijenite njihov utjecaj, zatim donesite odluke o migraciji.                                                                                |
| Razdvojite upute i kontekst       | Provjerite definiraju li vaš model/izdavač _graničnike_ za jasnije razlikovanje uputa, primarnog i sekundarnog sadržaja. To može pomoći modelima da točnije dodijele težinu tokenima.                                                         |
| Budite konkretni i jasni           | Dajte više detalja o željenom kontekstu, ishodu, duljini, formatu, stilu itd. To će poboljšati kvalitetu i dosljednost odgovora. Zabilježite recepte u ponovo upotrebljive predloške.                                                          |
| Budite opisni, koristite primjere  | Modeli mogu bolje odgovoriti na pristup "pokaži i reci". Počnite s `zero-shot` pristupom gdje date uputu (bez primjera), zatim isprobajte `few-shot` kao doradu, dajući nekoliko primjera željenog izlaza. Koristite analogije. |
| Koristite poticaje za pokretanje ispuna | Usmjerite model prema željenom ishodu dajući mu neke vodeće riječi ili izraze koje može koristiti kao početnu točku za odgovor.                                                                                                               |
| Ponavljajte                        | Ponekad je potrebno ponoviti upute modelu. Dajte upute prije i poslije primarnog sadržaja, koristite uputu i poticaj itd. Iterirajte i validirajte da biste vidjeli što najbolje funkcionira.                                                         |
| Redoslijed je važan               | Redoslijed u kojem prezentirate informacije modelu može utjecati na ishod, čak i u učnim primjerima, zahvaljujući sklonom povijesti (recency bias). Isprobajte različite opcije da vidite što najbolje radi.                                                               |
| Dajte modelu "izlaznu strategiju"           | Dajte modelu _rezervni_ odgovor koji može pružiti ako iz bilo kojeg razloga ne može dovršiti zadatak. Ovo može smanjiti mogućnost da modeli generiraju netočne ili izmišljene odgovore.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

Kao i kod svake najbolje prakse, imajte na umu da _rezultati mogu varirati_ ovisno o modelu, zadatku i domeni. Koristite ove smjernice kao početnu točku i iterirajte da pronađete što najbolje funkcionira za vas. Stalno preispitujte svoj proces inženjerstva upita kako se pojavljuju novi modeli i alati, s fokusom na skalabilnost procesa i kvalitetu odgovora.

<!--
PREDLOŽAK LEKCIJE:
Ovaj odjeljak treba pružiti izazov u kodiranju ako je primjenjivo

IZAZOV:
Poveznica na Jupyter bilježnicu s komentarima u kodu u uputama (odjeljci koda su prazni).

RIJEŠENJE:
Poveznica na kopiju te bilježnice gdje su upiti popunjeni i izvršeni, pokazujući jedan mogući primjer.
-->

## Zadatak

Čestitamo! Stigli ste do kraja lekcije! Vrijeme je da neke od tih koncepata i tehnika isprobate na stvarnim primjerima!

Za naš zadatak koristit ćemo Jupyter bilježnicu s vježbama koje možete interaktivno dovršavati. Također možete proširiti bilježnicu vlastitim Markdown i kod ćelijama kako biste istražili ideje i tehnike samostalno.

### Za početak, raskopirajte repozitorij, zatim

- (Preporučeno) Pokrenite GitHub Codespaces
- (Alternativno) Klonirajte repozitorij na svoj lokalni uređaj i koristite ga s Docker Desktopom
- (Alternativno) Otvorite bilježnicu u željenom okruženju za pokretanje bilježnica.

### Zatim konfigurirajte svoje varijable okoline

- Kopirajte datoteku `.env.copy` u korijenu repozitorija u `.env` i unesite vrijednosti za `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` i `AZURE_OPENAI_DEPLOYMENT`. Vratite se na [Learning Sandbox odjeljak](#okruženje-za-učenje) za upute kako.

### Zatim otvorite Jupyter bilježnicu

- Odaberite runtime kernel. Ako koristite opciju 1 ili 2, jednostavno odaberite zadani Python 3.10.x kernel koji pruža razvojno okruženje kontejnera.

Spremni ste za pokretanje vježbi. Imajte na umu da ovdje nema _pravih ili pogrešnih_ odgovora - samo istraživanje opcija metodom pokušaja i pogreške te razvoj intuicije što funkcionira za određeni model i domen.

_Iz tog razloga u ovoj lekciji nema segmenata s rješenjima koda. Umjesto toga, bilježnica će imati Markdown ćelije pod nazivom "Moje rješenje:" koje prikazuju jedan primjer izlaza kao referencu._

 <!--
PREDLOŽAK LEKCIJE:
Zaokružite odjeljak sa sažetkom i resursima za samostalno učenje.
-->

## Provjera znanja

Koji od sljedećih upita je dobar i slijedi neke razumne najbolje prakse?

1. Pokaži mi sliku crvenog auta
2. Pokaži mi sliku crvenog auta marke Volvo i modela XC90 parkiranog kraj litice uz zalazak sunca
3. Pokaži mi sliku crvenog auta marke Volvo i modela XC90

A: 2, to je najbolji upit jer daje detalje o "što" i ide u pojedinosti (ne bilo koji auto već specifičnu marku i model) te također opisuje cjelokupni ambijent. 3 je sljedeći najbolji jer sadrži puno opisa.

## 🚀 Izazov

Pokušajte iskoristiti tehniku "poticaja" s upitom: Dovrši rečenicu "Pokaži mi sliku crvenog auta marke Volvo i ". Što odgovara i kako biste to poboljšali?

## Odličan posao! Nastavite s učenjem

Želite li saznati više o različitim konceptima inženjerstva upita? Posjetite [stranicu za daljnje učenje](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) za ostale odlične resurse na ovu temu.

Idite na Lekciju 5 gdje ćemo pogledati [napredne tehnike upita](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->