# Osnove dizajniranja upita

[![Osnove dizajniranja upita](../../../translated_images/hr/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Uvod
Ovaj modul obuhvaća osnovne koncepte i tehnike za izradu učinkovitih upita u generativnim AI modelima. Način na koji napišete svoj upit za LLM također je važan. Pažljivo osmišljen upit može postići bolju kvalitetu odgovora. Ali što točno znače izrazi poput _prompt_ i _prompt engineering_? I kako unaprijediti upit (_input_) koji šaljem LLM-u? To su pitanja na koja ćemo pokušati odgovoriti u ovom i sljedećem poglavlju.

_Generativna umjetna inteligencija_ je sposobna stvarati novi sadržaj (npr. tekst, slike, audio, kod itd.) kao odgovor na korisničke zahtjeve. To postiže upotrebom _Velikih jezičnih modela_ poput OpenAI-jevog GPT ("Generative Pre-trained Transformer") niza, koji su trenirani za rad s prirodnim jezikom i kodom.

Korisnici sada mogu komunicirati s ovim modelima koristeći poznate paradigme poput chat-a, bez potrebe za tehničkom stručnošću ili obukom. Modeli su temeljeni na _promptima_ - korisnici šalju tekstualni unos (prompt) i dobivaju AI odgovor (dovršetak). Zatim mogu „razgovarati s AI-jem“ iterativno, u višekratnim dijalozima, usavršavajući svoj prompt dok odgovor ne zadovolji njihove očekivanja.

"Prompts" sada postaju primarni _programski sučelje_ za generativne AI aplikacije, govoreći modelima što učiniti i utječući na kvalitetu vraćenih odgovora. "Prompt Engineering" je brzo rastuće područje koje se fokusira na _dizajn i optimizaciju_ promptova kako bi se dosljedno dobili kvalitetni odgovori na velikoj skali.

## Ciljevi učenja

U ovoj lekciji naučit ćemo što je Prompt Engineering, zašto je važan i kako možemo izraditi učinkovitije promptove za određeni model i ciljeve aplikacije. Razumjet ćemo osnovne koncepte i najbolje prakse dizajna promptova - i upoznati interaktivno Jupyter Notebook „sandbox“ okruženje u kojem možemo vidjeti primjenu tih koncepata na stvarnim primjerima.

Na kraju ove lekcije moći ćemo:

1. Objasniti što je prompt engineering i zašto je važan.
2. Opišemo komponente prompta i kako se koriste.
3. Naučiti najbolje prakse i tehnike za prompt engineering.
4. Primijeniti naučene tehnike na stvarne primjere uz korištenje OpenAI endpointa.

## Ključni pojmovi

Prompt Engineering: Praksa dizajniranja i usavršavanja unosa za usmjeravanje AI modela prema željenim izlazima.  
Tokenizacija: Proces pretvaranja teksta u manje jedinice, nazvane tokeni, koje model može razumjeti i obraditi.  
Instruction-Tuned LLMs: Veliki jezični modeli koji su dodatno fino podešeni s određenim uputama za poboljšanje točnosti i relevantnosti odgovora.

## Okruženje za učenje ("Sandbox")

Prompt engineering je trenutačno više umjetnost nego znanost. Najbolji način da poboljšamo intuiciju je _više vježbati_ i usvojiti pristup pokušaja i pogrešaka koji kombinira stručnost u domeni primjene s preporučenim tehnikama i optimizacijama specifičnim za model.

Jupyter Notebook koji prati ovu lekciju pruža _sandbox_ okruženje gdje možete isprobati ono što učite - za vrijeme učenja ili kao dio izazova s kodom na kraju. Za izvođenje vježbi trebat će vam:

1. **Azure OpenAI API ključ** - servisna točka za implementirani LLM.  
2. **Python runtime** - u kojem se Notebook može izvršiti.  
3. **Lokalne varijable okoline** - _dovršite [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) korake sada da biste se pripremili_.

Notebook dolazi s _početnim_ vježbama - ali potičemo vas da dodate vlastite odjeljke _Markdown_ (opis) i _Code_ (zahtjevi prompta) kako biste isprobali više primjera ili ideja - i izgradili svoju intuiciju za dizajn promptova.

## Ilustrirani vodič

Želite li prije ulaska u detalje dobiti širu sliku teme koju ova lekcija pokriva? Pogledajte ilustrirani vodič koji daje pregled glavnih tema i ključnih zaključaka koje biste trebali razmotriti u svakoj od njih. Put lekcije vodi vas od razumijevanja osnovnih pojmova i izazova do njihovog rješavanja relevantnim tehnikama prompt engineeringa i najboljim praksama. Napominjemo da se odjeljak "Napredne tehnike" u ovom vodiču odnosi na sadržaj u _sljedećem_ poglavlju ovog kurikuluma.

![Ilustrirani vodič za dizajniranje upita](../../../translated_images/hr/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Naš startup

Sada, razgovarajmo o tome kako se _ova tema_ odnosi na naš startupovu misiju da [donesemo AI inovacije u obrazovanje](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Želimo izgraditi AI-pokretane aplikacije za _personalizirano učenje_ - pa razmislimo kako bi različiti korisnici naše aplikacije mogli „dizajnirati“ promptove:

- **Administratori** mogu tražiti od AI-ja da _analizira podatke o kurikulumu kako bi identificirao praznine u pokrivenosti_. AI može sažeti rezultate ili ih vizualizirati kodom.  
- **Nastavnici** mogu tražiti od AI-ja da _generira plan lekcije za ciljanu publiku i temu_. AI može izraditi personalizirani plan u određenom formatu.  
- **Učenici** mogu tražiti od AI-ja da _ih poduči o teškom predmetu_. AI sada može voditi učenike kroz lekcije, savjete i primjere prilagođene njihovoj razini.

To je samo vrh ledenog brijega. Pogledajte [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - open-source knjižnicu promptova koju su kreirali stručnjaci za obrazovanje - da biste dobili širi dojam o mogućnostima! _Pokušajte pokrenuti neke od tih promptova u sandboxu ili na OpenAI Playgroundu da vidite što se događa!_

<!--  
LESSON TEMPLATE:  
This unit should cover core concept #1.  
Reinforce the concept with examples and references.  

CONCEPT #1:  
Prompt Engineering.  
Define it and explain why it is needed.  
-->

## Što je Prompt Engineering?

Lekciju smo započeli definiranjem **Prompt Engineering** kao procesa _dizajniranja i optimizacije_ tekstualnih unosa (promptova) kako bi se postigli dosljedni i kvalitetni odgovori (dovršetci) za određeni cilj aplikacije i model. To možemo zamisliti kao dvostupanjski proces:

- _dizajniranje_ početnog prompta za određeni model i cilj  
- _usavršavanje_ prompta iterativno radi poboljšanja kvalitete odgovora

To je nužno proces pokušaja i pogreške koji zahtijeva intuiciju korisnika i trud kako bi se postigli optimalni rezultati. Zašto je to važno? Da bismo odgovorili na to pitanje, prvo moramo razumjeti tri koncepta:

- _Tokenizacija_ = kako model "vidi" prompt  
- _Osnovni LLM-ovi_ = kako temeljni model "obrađuje" prompt  
- _Instruction-Tuned LLMs_ = kako model sada može prepoznavati "zadatke"

### Tokenizacija

LLM vidi prompty kao _niz tokena_ gdje različiti modeli (ili verzije istog modela) mogu tokenizirati isti prompt na različite načine. Budući da su LLM-ovi trenirani na tokenima (a ne na sirovom tekstu), način na koji se prompt tokenizira ima izravan utjecaj na kvalitetu generiranog odgovora.

Da biste stekli intuiciju o tokenizaciji, isprobajte alate kao što je [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) prikazan ispod. Zalijepite svoj prompt i pogledajte na koje se tokene pretvara, obratite pažnju na to kako se tretiraju razmaci i interpunkcijski znakovi. Imajte na umu da ovaj primjer prikazuje stariji LLM (GPT-3) - pa isprobavanje na novijem modelu može dati drugačiji rezultat.

![Tokenizacija](../../../translated_images/hr/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Koncept: Temeljni modeli

Kada je prompt tokeniziran, primarna funkcija ["osnovnog LLM-a"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (ili temeljni model) je predviđanje sljedećeg tokena u nizu. Budući da su LLM-ovi trenirani na ogromnim skupovima tekstualnih podataka, dobro poznaju statističke odnose između tokena i mogu to predviđanje izvesti s određenom pouzdanošću. Imajte na umu da oni ne razumiju _značenje_ riječi u promptu ili tokenu; oni samo vide obrazac koji mogu „dovršiti“ s idućim predviđanjem. Mogu nastaviti predviđati niz dok ih korisnik ne zaustavi ili ne nastupe neki unaprijed definirani uvjeti.

Želite li vidjeti kako funkcionira dovršavanje zasnovano na promptu? Unesite gore navedeni prompt u Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) s zadanim postavkama. Sustav je konfiguriran da tretira promptove kao zahtjeve za informacijama - tako da biste trebali vidjeti dovršetak koji zadovoljava ovaj kontekst.

Ali što ako korisnik želi vidjeti nešto specifično što zadovoljava određene kriterije ili cilj zadatka? Tada na scenu stupaju _instruction-tuned_ LLM-ovi.

![Dovršetak chata osnovnog LLM-a](../../../translated_images/hr/04-playground-chat-base.65b76fcfde0caa67.webp)

### Koncept: Instruction-Tuned LLMs

[Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) započinje sa temeljnim modelom i dodatno ga podešava s primjerima ili ulazno-izlaznim parovima (npr. višekratnim „porukama“) koje mogu sadržavati jasne upute - a AI pokušava pratiti te upute u odgovoru.

Ovo koristi tehnike poput učenja pojačanjem s ljudskom povratnom informacijom (RLHF) koje mogu trenirati model da _prati upute_ i _uči iz povratnih informacija_ tako da daje odgovore bolje prilagođene praktičnim primjenama i relevantnije korisničkim ciljevima.

Isprobajmo to - vratite se na gornji prompt, ali sada promijenite _sistemski mesaj_ tako da pruži sljedeću uputu kao kontekst:

> _Sažmi sadržaj koji dobiješ za učenika drugog razreda. Drži rezultat u jednom odlomku s 3-5 nabrajanja._

Vidite kako je rezultat sada prilagođen da odražava željeni cilj i format? Nastavnik sada može izravno koristiti ovaj odgovor u svojim slajdovima za taj sat.

![Dovršetak chata instruction-tuned LLM-a](../../../translated_images/hr/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Zašto trebamo Prompt Engineering?

Sada kada znamo kako LLM obrađuje prompty, razgovarajmo o tome _zašto_ nam treba prompt engineering. Odgovor leži u činjenici da trenutačni LLM-ovi postavljaju niz izazova koji otežavaju _pouzdano i dosljedno dovršavanje_ bez truda uloženog u konstrukciju i optimizaciju prompta. Na primjer:

1. **Odgovori modela su stohastički.** _Isti prompt_ vjerojatno će dati različite odgovore s različitim modelima ili verzijama modela. Moguće je i da isti model u različito vrijeme proizvede različite rezultate. _Tehnike prompt engineeringa mogu nam pomoći smanjiti te varijacije pružajući bolje zaštitne ograde_.

1. **Modeli mogu izmišljati odgovore.** Modeli su unaprijed trenirani na _velikim, ali konačnim_ skupovima podataka, što znači da nemaju znanje o konceptima izvan tog područja obuke. Kao rezultat toga, mogu proizvesti dovršetke koji su netočni, izmišljeni ili čak u izravnoj suprotnosti s poznatim činjenicama. _Tehnike prompt engineeringa pomažu korisnicima da identificiraju i smanje takve izmišljotine, npr. traženjem citata ili obrazloženja od AI-ja_.

1. **Sposobnosti modela varirat će.** Noviji modeli ili generacije modela imat će bogatije sposobnosti, ali i donose jedinstvene posebnosti i kompromise u troškovima i složenosti. _Prompt engineering može pomoći u razvoju najboljih praksi i tijekova rada koji svode na minimum razlike i prilagođavaju se model-specifičnim zahtjevima na skalabilan i besprijekoran način_.

Pogledajmo to u akciji u OpenAI ili Azure OpenAI Playgroundu:

- Koristite isti prompt s različitim implementacijama LLM-a (npr. OpenAI, Azure OpenAI, Hugging Face) - jeste li uočili varijacije?  
- Koristite isti prompt više puta s _istom_ implementacijom LLM-a (npr. Azure OpenAI playground) - kako su se te varijacije razlikovale?

### Primjer izmišljotina

U ovom tečaju koristimo izraz **"izmišljotina"** za označavanje pojave kada LLM-ovi ponekad generiraju factually netočne informacije zbog ograničenja u njihovoj obuci ili drugih faktora. Možda ste ovaj fenomen u popularnim člancima ili znanstvenim radovima vidjeli nazvan i kao _„halucinacije“_. Međutim, mi snažno preporučujemo korištenje termina _„izmišljotina“_ kako ne bismo nenamjerno antropomorfizirali ponašanje pripisujući mašinski izvedenom rezultatu ljudsku osobinu. To također podržava [smjernice za odgovornu AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) iz perspektive terminologije, uklanjajući izraze koji mogu biti uvredljivi ili neinkluzivni u određenim kontekstima.

Želite li osjetiti kako izmišljotine nastaju? Zamislite prompt koji AI-u daje uputu da generira sadržaj o nepostojećoj temi (kako biste bili sigurni da se ona ne nalazi u skupu podataka za učenje). Na primjer - isprobao sam ovaj prompt:

> **Prompt:** generiraj plan lekcije o Marsovskom ratu 2076. godine.
Pretraživanje weba pokazalo mi je da postoje fiktivni prikazi (npr. televizijske serije ili knjige) o ratovima na Marsu - ali nijedan iz 2076. Zdrav razum također nam govori da je 2076. _u budućnosti_ i stoga se ne može povezati sa stvarnim događajem.

Pa što se događa kada ovaj upit pokrenemo s različitim pružateljima LLM usluga?

> **Odgovor 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/hr/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Odgovor 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/hr/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Odgovor 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/hr/04-fabrication-huggingchat.faf82a0a51278956.webp)

Kao što se očekivalo, svaki model (ili verzija modela) proizvodi nešto različite odgovore zahvaljujući slučajnom ponašanju i razlikama u sposobnostima modela. Na primjer, jedan model cilja na publiku osmoga razreda, dok drugi pretpostavlja učenika srednje škole. Ali sva tri modela su generirala odgovore koji bi mogli uvjeriti neupućenog korisnika da je događaj stvaran.

Tehnike inženjeringa upita poput _metapromptinga_ i _konfiguracije temperature_ mogu donekle smanjiti izmišljotine modela. Nove _arhitekture_ inženjeringa upita također besprijekorno uključuju nove alate i tehnike u tok upita, kako bi ublažile ili smanjile neke od ovih efekata.

## Studija slučaja: GitHub Copilot

Završimo ovaj odjeljak uvidom u to kako se inženjering upita koristi u stvarnim rješenjima kroz studiju slučaja: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot je vaš "AI partner programer" - pretvara tekstualne upite u dovršenice koda i integriran je u vaše razvojno okruženje (npr. Visual Studio Code) za besprijekorno korisničko iskustvo. Kao što je dokumentirano u nizu blogova ispod, najranija verzija bila je bazirana na OpenAI Codex modelu - a inženjeri su brzo shvatili potrebu da se model dodatno osposobi i razviju bolje tehnike inženjeringa upita, radi poboljšanja kvalitete koda. U srpnju su [predstavili unaprijeđeni AI model koji nadmašuje Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) za još brže prijedloge.

Pročitajte postove redoslijedom kako biste pratili njihovo učenje.

- **Svibanj 2023** | [GitHub Copilot sve bolje razumije vaš kod](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Svibanj 2023** | [Iznutra GitHub: Rad sa LLM modelima iza GitHub Copilota](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Lipanj 2023** | [Kako pisati bolje upite za GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Srpanj 2023** | [GitHub Copilot nadmašuje Codex uz poboljšani AI model](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Srpanj 2023** | [Vodič za programere za inženjering upita i LLM modele](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Rujan 2023** | [Kako izgraditi enterprise LLM aplikaciju: pouke iz GitHub Copilota](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Također možete pregledavati njihov [inženjerski blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) za više postova poput [ovog](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) koji pokazuje kako se ovi modeli i tehnike _primjenjuju_ za pokretanje stvarnih aplikacija.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #2.
Reinforce the concept with examples and references.

CONCEPT #2:
Prompt Design.
Illustrated with examples.
-->

## Izgradnja upita

Vidjeli smo zašto je inženjering upita važan - sada ćemo razumjeti kako se upiti _izrađuju_ kako bismo mogli procijeniti različite tehnike za učinkovitiji dizajn upita.

### Osnovni upit

Počnimo s osnovnim upitom: tekstualnim unosom poslanim modelu bez dodatnog konteksta. Evo primjera - kada pošaljemo prve riječi američke nacionalne himne OpenAI [Completion API-ju](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), on odmah _dovršava_ odgovor s nekoliko sljedećih redaka, ilustrirajući osnovno ponašanje predviđanja.

| Upit (Unos)       | Dovršetak (Izlaz)                                                                                                                         |
| :---------------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Izgleda kao da započinjete s tekstom pjesme "The Star-Spangled Banner," nacionalne himne Sjedinjenih Država. Cijeli tekst je ...          |

### Složeni upit

Sada dodajmo kontekst i upute tom osnovnom upitu. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) omogućuje nam konstrukciju složenog upita kao zbirku _poruka_ sa:

- Parovima ulaza/izlaza koji odražavaju unos _korisnika_ i odgovor _asimistenta_.
- Porukom sustava koja postavlja kontekst za ponašanje ili osobnost asistenta.

Zahtjev sada izgleda kao u nastavku, gdje _tokenizacija_ učinkovito hvata relevantne informacije iz konteksta i razgovora. Promjena konteksta sustava može biti jednako utjecajna za kvalitetu dovršetaka kao i korisnički unosi.

```python
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Upit s uputom

U gore navedenim primjerima, upit korisnika bio je jednostavan tekstualni upit koji se može protumačiti kao zahtjev za informacijom. Kod _upita s uputom_, možemo iskoristiti taj tekst za detaljnije specificiranje zadatka, pružajući bolju uputu AI-u. Evo primjera:

| Upit (Unos)                                                                                                                                                                                                                          | Dovršetak (Izlaz)                                                                                                        | Vrsta upute       |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------ | :---------------- |
| Napiši opis Građanskog rata                                                                                                                                                                                                         | _vraća jednostavan odlomak_                                                                                              | Jednostavno       |
| Napiši opis Građanskog rata. Navedite ključne datume i događaje te opišite njihov značaj                                                                                                                                           | _vraća odlomak nakon kojeg slijedi popis ključnih datuma događaja sa opisima_                                            | Složeno           |
| Napiši opis Građanskog rata u 1 odlomku. Navedite 3 ključne točke s datumima i njihovim značajem. Navedite još 3 točke s važnim povijesnim osobama i njihovim doprinosima. Vrati izlaz u JSON formatu | _vraća opširnije informacije u tekstualnom okviru, formatirano kao JSON koji možete kopirati i zalijepiti u datoteku i po potrebi validirati_ | Složeno. Formatirano. |

## Primarni sadržaj

U gore navedenim primjerima, upit je još uvijek bio prilično otvoren, dopuštajući LLM-u da odluči koji dio svoje prethodno istrenirane baze podataka je relevantan. S obrascem dizajna _primarnog sadržaja_, ulazni tekst dijeli se u dva dijela:

- uputa (akcija)
- relevantni sadržaj (koji utječe na akciju)

Evo primjera gdje je uputa "sastavi ovo u 2 rečenice".

| Upit (Unos)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Dovršetak (Izlaz)                                                                                                                                                                                                                                                                             |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter je peti planet od Sunca i najveći u Sunčevom sustavu. To je plinoviti div s masom tisućinku one Sunca, ali dva i pol puta većom od mase svih ostalih planeta u Sunčevom sustavu zajedno. Jupiter je jedan od najsvjetlijih objekata vidljivih golim okom na noćnom nebu, poznat drevnim civilizacijama još prije zapisane povijesti. Dobio je ime po rimskom bogu Jupiteru.[19] Kada se promatra sa Zemlje, Jupiter može biti dovoljno svijetao da njegova reflektirana svjetlost baca vidljive sjene,[20] a u prosjeku je treći najsvjetliji prirodni objekt na noćnom nebu nakon Mjeseca i Venere. <br/> **Sažmi ovo u 2 kratke rečenice**  | Jupiter, peti planet od Sunca, najveći je u Sunčevom sustavu i poznat je kao jedan od najsvjetlijih objekata na noćnom nebu. Imenovan po rimskom bogu Jupiteru, to je plinoviti div čija je masa dva i pol puta veća od mase svih ostalih planeta u Sunčevom sustavu zajedno. |

Segment primarnog sadržaja može se koristiti na razne načine za učinkovitije upute:

- **Primjeri** – umjesto da modelu izričito kažemo što treba učiniti, dajemo mu primjere što napraviti i pustimo ga da zaključi uzorak.
- **Načini (Cue-ovi)** – slijede uputu s "nagovještajem" koji priprema dovršetak, usmjeravajući model ka relevantnijim odgovorima.
- **Predlošci** – ponovljivi 'recepti' za upite s rezerviranim mjestima (varijablama) koje se mogu prilagoditi podacima za određene slučajeve upotrebe.

Istražimo ih u praksi.

### Korištenje primjera

Ovo je pristup gdje koristite primarni sadržaj da "hranite model" nekim primjerima željenog izlaza za zadanu uputu i omogućavate mu da zaključi uzorak željenog izlaza. Na temelju broja primjera može biti zero-shot (bez primjera), one-shot (jedan primjer), few-shot (nekoliko primjera) itd.

Sada upit sadrži tri komponente:

- Opis zadatka
- Nekoliko primjera željenog izlaza
- Početak novog primjera (koji postaje implicitni opis zadatka)

| Tip učenja    | Upit (Unos)                                                                                                                                    | Dovršetak (Izlaz)          |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "The Sun is Shining". Prevedi na španjolski                                                                                                  | "El Sol está brillando".    |
| One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                           | "Es un día frío y ventoso". |
| Few-shot      | Igrač je trčao oko baza => Baseball <br/> Igrač je servirao ace => Tenis <br/> Igrač je udario šesticu => Kriket <br/> Igrač je izveo zakucavanje => | Košarka                    |
|               |                                                                                                                                                |                             |

Primijetite kako smo kod zero-shot prompta morali dati izričitu uputu ("Prevedi na španjolski"), ali se ona zaključuje u one-shot primjeru. Primjer few-shot pokazuje kako dodavanje više primjera omogućuje modelima da točnije zaključuju bez dodatnih uputa.

### Načini za upite (Prompt Cues)

Još jedna tehnika za korištenje primarnog sadržaja je davanje _načina_ umjesto primjera. U ovom slučaju, dajemo modelu nagovještaj u pravom smjeru tako da _počnemo_ s isječkom koji odražava željeni format odgovora. Model tada "uzima nagovještaj" i nastavlja u tom stilu.

| Broj načina (Cue-ova) | Upit (Unos)                                                                                                                                                                                                                                                                                                                                                                                                                     | Dovršetak (Izlaz)                                                                                                                                                                                                                                                                         |
| :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                     | Jupiter je peti planet od Sunca i najveći u Sunčevom sustavu. To je plinoviti div s masom tisućinku one Sunca, ali dva i pol puta većom od mase svih ostalih planeta u Sunčevom sustavu zajedno. Jupiter je jedan od najsvjetlijih objekata vidljivih golim okom na noćnom nebu, poznat drevnim civilizacijama još prije zapisane povijesti. <br/>**Sažmi ovo**                                         | Jupiter je najveći planet u našem Sunčevom sustavu i peti po redu od Sunca. To je plinoviti div s masom 1/1000 mase Sunca, ali teži više od svih ostalih planeta zajedno. Drevne civilizacije dugo poznaju Jupiter, a lako je uočljiv na noćnom nebu.                                      |
| 1              | Jupiter je peta planeta od Sunca i najveća u Sunčevom sustavu. To je plinski div s masom tisućinku mase Sunca, ali dvije i pol puta većom od svih ostalih planeta u Sunčevom sustavu zajedno. Jupiter je jedan od najsvjetlijih objekata vidljivih golim okom na noćnom nebu, a poznat je drevnim civilizacijama još prije zapisane povijesti. <br/>**Sažmi ovo** <br/> Ono što smo naučili je da je Jupiter | peta planeta od Sunca i najveća u Sunčevom sustavu. To je plinski div s masom tisućinku mase Sunca, ali dvije i pol puta većom od svih ostalih planeta zajedno. Lako je vidljiv golim okom i poznat je od davnina.                        |
| 2              | Jupiter je peta planeta od Sunca i najveća u Sunčevom sustavu. To je plinski div s masom tisućinku mase Sunca, ali dvije i pol puta većom od svih ostalih planeta u Sunčevom sustavu zajedno. Jupiter je jedan od najsvjetlijih objekata vidljivih golim okom na noćnom nebu, a poznat je drevnim civilizacijama još prije zapisane povijesti. <br/>**Sažmi ovo** <br/> Tri najvažnije činjenice koje smo naučili:         | 1. Jupiter je peta planeta od Sunca i najveća u Sunčevom sustavu. <br/> 2. To je plinski div s masom tisućinku mase Sunca...<br/> 3. Jupiter je golim okom vidljiv od davnina ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Predlošci upita

Predložak upita je _predefinirana "receptura" za upit_ koja se može pohraniti i ponovno koristiti prema potrebi, kako bi se postigli dosljedniji korisnički doživljaji na velikoj skali. U svojem najjednostavnijem obliku, to je jednostavno zbirka primjera upita poput [ovog od OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) koji pruža i interaktivne dijelove upita (poruke korisnika i sustava) i format zahtjeva temeljen na API-ju - za potporu ponovnoj uporabi.

U složenijem obliku, poput [ovog primjera iz LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), sadrži _mjesta za unos_ koja se mogu zamijeniti podacima iz raznih izvora (korisnički unos, kontekst sustava, vanjski izvori podataka itd.) kako bi se dinamički generirao upit. To nam omogućuje stvaranje biblioteke ponovo upotrebljivih upita koje se mogu programatski koristiti za postizanje dosljednih korisničkih doživljaja na velikoj skali.

Na kraju, stvarna vrijednost predložaka leži u mogućnosti stvaranja i objavljivanja _biblioteka upita_ za vertikalne domene primjene - gdje je predložak sada _optimiziran_ da odražava kontekst specifičan za aplikaciju ili primjere koji čine odgovore relevantnijima i točnijima za ciljanu korisničku publiku. Spremište [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) odličan je primjer takvog pristupa, prikupljajući biblioteku upita za obrazovni domen s naglaskom na ključne ciljeve poput planiranja lekcija, dizajna kurikuluma, podučavanja učenika itd.

## Pomoćni sadržaj

Ako razmišljamo o konstrukciji upita kao o instrukciji (zadatku) i cilju (primarnom sadržaju), tada je _sekundarni sadržaj_ poput dodatnog konteksta koji pružamo da bi **na neki način utjecali na izlaz**. To mogu biti parametri podešavanja, upute za formatiranje, taksonomije tema itd. koje pomažu modelu _prilagoditi_ svoj odgovor tako da zadovolji željene korisničke ciljeve ili očekivanja.

Na primjer: Imajući katalog tečajeva s opsežnim metapodacima (naziv, opis, razina, oznake metapodataka, instruktor itd.) za sve dostupne tečajeve u kurikulumu:

- možemo definirati instrukciju da "sažmemo katalog tečajeva za jesen 2023."
- možemo koristiti primarni sadržaj da pružimo nekoliko primjera željenog izlaza
- možemo koristiti sekundarni sadržaj za identificiranje 5 najvažnijih "oznake" interesa.

Sada model može dati sažetak u formatu prikazanom na nekoliko primjera - ali ako rezultat ima više oznaka, može dati prioritet 5 oznaka identificiranih u sekundarnom sadržaju.

---

<!--
LESSON TEMPLATE:
Ova jedinica treba pokriti osnovni koncept #1.
Potkrijepiti koncept primjerima i referencama.

KONCEPT #3:
Tehnike inženjeringa prompta.
Koje su neke osnovne tehnike za inženjering prompta?
Ilustrirajte to nekim vježbama.
-->

## Najbolje prakse za upite

Sada kada znamo kako se upiti mogu _konstruirati_, možemo početi razmišljati o tome kako ih _dizajnirati_ da odražavaju najbolje prakse. Možemo to promatrati u dva dijela – imati pravi _način razmišljanja_ i primijeniti prave _tehnike_.

### Način razmišljanja o inženjeringu upita

Inženjering upita je proces pokušaja i pogrešaka pa imajte na umu tri široka vodiča:

1. **Važno je razumijevanje domene.** Točnost i relevantnost odgovora ovisi o _domeni_ u kojoj aplikacija ili korisnik djeluje. Primijenite svoju intuiciju i stručnost u domeni da biste dodatno **prilagodili tehnike**. Na primjer, definirajte _osobnosti specifične za domenu_ u sustavnim upitima ili koristite _predloške specifične za domenu_ u korisničkim upitima. Pružite sekundarni sadržaj koji odražava kontekste specifične za domenu, ili koristite _znakove i primjere specifične za domenu_ za usmjeravanje modela prema poznatim obrascima korištenja.

2. **Važno je razumijevanje modela.** Znamo da su modeli po svojoj prirodi stohastični. No implementacije modela također se mogu razlikovati po skupu trening-podataka koje koriste (predtrenirano znanje), sposobnostima koje pružaju (npr. preko API-ja ili SDK-a) i vrsti sadržaja za koji su optimizirani (npr. kod naspram slika naspram teksta). Razumite snage i ograničenja modela koji koristite i iskoristite to znanje kako biste _prioritizirali zadatke_ ili izgradili _prilagođene predloške_ koji su optimizirani za mogućnosti modela.

3. **Važna je iteracija i validacija.** Modeli se brzo razvijaju, kao i tehnike inženjeringa upita. Kao stručnjak za domenu, možete imati drugi kontekst ili kriterije za _svoju_ specifičnu primjenu, koji možda nisu primjenjivi za širu zajednicu. Koristite alate i tehnike inženjeringa upita za "startno ubrzanje" konstrukcije upita, zatim iterirajte i validirajte rezultate koristeći vlastitu intuiciju i stručnost u domeni. Zabilježite svoje uvide i izradite **bazu znanja** (npr. biblioteke upita) koje drugi mogu koristiti kao novu osnovu za brže iteracije u budućnosti.

## Najbolje prakse

Pogledajmo sada uobičajene najbolje prakse koje preporučuju [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) i [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) praktičari.

| Što                              | Zašto                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Procijenite najnovije modele.       | Nove generacije modela vjerojatno imaju poboljšane značajke i kvalitetu – ali mogu imati i veće troškove. Procijenite njihov utjecaj, zatim donesite odluke o migraciji.                                                                                |
| Odvojite upute i kontekst   | Provjerite definira li vaš model/dobavljač _razdjelnike_ za jasnije razlikovanje uputa, primarnog i sekundarnog sadržaja. To može pomoći modelima da točnije dodijele težine tokenima.                                                         |
| Budite specifični i jasni             | Dajte više detalja o željenom kontekstu, rezultatu, duljini, formatu, stilu itd. To će poboljšati kvalitetu i dosljednost odgovora. Zabilježite recepte u ponovo upotrebljive predloške.                                                          |
| Budite opisni, koristite primjere      | Modeli bolje reagiraju na pristup "pokaži i ispričaj". Počnite s `zero-shot` pristupom gdje dajete samo uputu (bez primjera), zatim pokušajte `few-shot` kao usavršavanje, dajući nekoliko primjera željenog izlaza. Koristite analogije. |
| Koristite nagovještaje za početak odgovora | Usmjerite ga prema željenom rezultatu dajući početne riječi ili fraze koje može upotrijebiti kao polaznu točku za odgovor.                                                                                                               |
| Pojačajte | Ponekad trebate više puta ponoviti modelu. Dajte upute prije i nakon primarnog sadržaja, koristite uputu i nagovještaj itd. Iterirajte i validirajte da vidite što najbolje funkcionira.                                                         |
| Redoslijed je bitan                     | Redoslijed u kojem iznosite informacije može utjecati na izlaz, čak i u primjerima za učenje, zbog pristranosti nedavnosti. Isprobajte različite opcije da vidite što najbolje radi.                                                               |
| Dajte modelu "izlaz"           | Dajte modelu _rezervnu_ opciju odgovora koju može pružiti ako iz bilo kojeg razloga ne može dovršiti zadatak. To može smanjiti šanse da model generira netočne ili izmišljene odgovore.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

Kao i kod svake najbolje prakse, imajte na umu da _rezultati mogu varirati_ ovisno o modelu, zadatku i domeni. Koristite ih kao polaznu točku i iterirajte da pronađete što najbolje funkcionira za vas. Neprestano preispitivajte svoj proces inženjeringa upita kako se pojavljuju novi modeli i alati, s fokusom na skalabilnost procesa i kvalitetu odgovora.

<!--
LESSON TEMPLATE:
Ova jedinica treba uključivati izazov s kodom ako je primjenjivo

IZAZOV:
Poveznica na Jupyter Notebook s komentarima u kodu kao uputama (sekcije koda su prazne).

RJEŠENJE:
Poveznica na kopiju tog Notebooka s popunjenim upitima koji su pokrenuti, pokazujući jedan primjer kao referencu.
-->

## Zadatak

Čestitamo! Stigli ste do kraja lekcije! Vrijeme je da neke od tih koncepata i tehnika isprobate s pravim primjerima!

Za naš zadatak koristit ćemo Jupyter Notebook s vježbama koje možete interaktivno odrađivati. Također možete proširiti Notebook vlastitim Markdown i kod ćelijama za istraživanje ideja i tehnika na svoj način.

### Za početak, forkajte repo, zatim

- (Preporučeno) Pokrenite GitHub Codespaces
- (Alternativno) Klonirajte repo na lokalno računalo i koristite ga s Docker Desktopom
- (Alternativno) Otvorite Notebook u preferiranom runtime okruženju za Jupyter.

### Zatim konfigurirajte varijable okoline

- Kopirajte datoteku `.env.copy` iz korijena repozitorija u `.env` i popunite vrijednosti `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` i `AZURE_OPENAI_DEPLOYMENT`. Vratite se na [odjeljak Learning Sandbox](#okruženje-za-učenje-sandbox) da naučite kako.

### Nakon toga otvorite Jupyter Notebook

- Odaberite kernel za izvršavanje. Ako koristite opciju 1 ili 2, jednostavno odaberite zadani Python 3.10.x kernel pružen u razvojnome kontejneru.

Sve je spremno za pokretanje vježbi. Napomena da nema _dobrih i loših_ odgovora – radi se o istraživanju opcija metodom pokušaja i pogreške te gradnji intuicije za to što najbolje funkcionira za određeni model i domen.

_Zbog toga u ovoj lekciji nema dijelova s rješenjima koda. Umjesto toga, Notebook će imati Markdown ćelije pod nazivom "Moje rješenje:" koje prikazuju jedan primjer izlaza za referencu._

 <!--
LESSON TEMPLATE:
Ovaj odjeljak završite sažetkom i materijalima za samostalno učenje.
-->

## Provjera znanja

Koji od sljedećih upita je dobar i slijedi neke razumno prihvaćene najbolje prakse?

1. Pokaži mi sliku crvenog auta
2. Pokaži mi sliku crvenog auta marke Volvo i modela XC90 parkiranog na litici pri zalasku sunca
3. Pokaži mi sliku crvenog auta marke Volvo i modela XC90

A: 2, jer je to najbolji upit jer pruža detalje o "što" i ide u specifikacije (ne bilo koji auto, nego određena marka i model) te također opisuje cjelokupni ambijent. 3 je druga najbolja jer također sadrži puno opisa.

## 🚀 Izazov

Pokušajte iskoristiti tehniku "nagovještaja" s upitom: Dovrši rečenicu "Pokaži mi sliku crvenog auta marke Volvo i ". Što odgovara i kako biste poboljšali upit?

## Odlično! Nastavite s učenjem

Želite li saznati više o različitim konceptima inženjeringa prompta? Posjetite [stranicu za daljnje učenje](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) i pronađite druge odlične resurse o ovoj temi.

Uputite se na Lekciju 5 gdje ćemo pogledati [napredne tehnike promptiranja](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->