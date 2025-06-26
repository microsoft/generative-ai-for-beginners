<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-06-25T13:38:33+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "sl"
}
-->
# Osnove oblikovanja pozivov

## Uvod
Ta modul pokriva osnovne koncepte in tehnike za ustvarjanje učinkovitih pozivov v generativnih AI modelih. Način, kako napišete svoj poziv LLM, je prav tako pomemben. Skrbno oblikovan poziv lahko doseže boljšo kakovost odgovora. Ampak kaj točno pomenijo izrazi, kot so _poziv_ in _oblikovanje pozivov_? In kako izboljšam poziv _vhod_, ki ga pošljem LLM? To so vprašanja, na katera bomo poskušali odgovoriti v tem poglavju in naslednjem.

_Generativna umetna inteligenca_ je sposobna ustvarjati nove vsebine (npr. besedilo, slike, zvok, kodo itd.) kot odgovor na uporabniške zahteve. To doseže z uporabo _Velikih Jezikovnih Modelov_, kot je serija GPT ("Generative Pre-trained Transformer") OpenAI, ki so usposobljeni za uporabo naravnega jezika in kode.

Uporabniki lahko zdaj komunicirajo s temi modeli z uporabo znanih paradigm, kot je klepet, brez potrebe po tehničnem znanju ali usposabljanju. Modeli so _temeljeni na pozivih_ - uporabniki pošljejo besedilni vnos (poziv) in dobijo AI odgovor (dokončanje). Nato lahko iterativno "klepetajo z AI" v večkratnih pogovorih, izpopolnjujejo svoj poziv, dokler odgovor ne ustreza njihovim pričakovanjem.

"Pozivi" zdaj postajajo primarni _programski vmesnik_ za aplikacije generativne umetne inteligence, ki modelom povedo, kaj naj naredijo in vplivajo na kakovost vrnjenih odgovorov. "Oblikovanje pozivov" je hitro rastoče področje študija, ki se osredotoča na _oblikovanje in optimizacijo_ pozivov za zagotavljanje doslednih in kakovostnih odgovorov v velikem obsegu.

## Cilji učenja

V tej lekciji se bomo naučili, kaj je oblikovanje pozivov, zakaj je pomembno in kako lahko oblikujemo bolj učinkovite pozive za določen model in cilj aplikacije. Razumeli bomo osnovne koncepte in najboljše prakse za oblikovanje pozivov - ter spoznali interaktivno okolje "sandbox" Jupyter Notebook, kjer lahko vidimo te koncepte uporabljene na resničnih primerih.

Do konca te lekcije bomo sposobni:

1. Razložiti, kaj je oblikovanje pozivov in zakaj je pomembno.
2. Opisati komponente poziva in kako se uporabljajo.
3. Naučiti se najboljših praks in tehnik za oblikovanje pozivov.
4. Uporabiti naučene tehnike na resničnih primerih, z uporabo OpenAI endpointa.

## Ključni pojmi

Oblikovanje pozivov: Praksa oblikovanja in izpopolnjevanja vnosov za usmerjanje AI modelov k ustvarjanju želenih izhodov.
Tokenizacija: Proces pretvorbe besedila v manjše enote, imenovane tokeni, ki jih model lahko razume in obdela.
Instrukcijsko prilagojeni LLM: Veliki jezikovni modeli (LLM), ki so bili fino prilagojeni s specifičnimi navodili za izboljšanje natančnosti in ustreznosti njihovih odgovorov.

## Učno okolje

Oblikovanje pozivov je trenutno bolj umetnost kot znanost. Najboljši način za izboljšanje naše intuicije za to je _več vaditi_ in sprejeti pristop poskusov in napak, ki združuje strokovno znanje aplikacijskega področja s priporočenimi tehnikami in optimizacijami, specifičnimi za model.

Jupyter Notebook, ki spremlja to lekcijo, zagotavlja _sandbox_ okolje, kjer lahko preizkusite, kar se naučite - medtem ko greste ali kot del kode izziva na koncu. Za izvedbo vaj boste potrebovali:

1. **Azure OpenAI API ključ** - končna točka storitve za nameščen LLM.
2. **Python Runtime** - v katerem lahko zaženete Notebook.
3. **Lokalne okoljske spremenljivke** - _dokončajte korake [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst), da se pripravite_.

Zvezek vsebuje _začetne_ vaje - vendar vas spodbujamo, da dodate svoje _Markdown_ (opisne) in _Code_ (zahteve za poziv) odseke, da preizkusite več primerov ali idej - in zgradite svojo intuicijo za oblikovanje pozivov.

## Ilustrirani vodnik

Želite dobiti širšo sliko o tem, kaj pokriva ta lekcija, preden se potopite vanjo? Oglejte si ta ilustrirani vodnik, ki vam daje občutek za glavne teme, ki jih pokriva, in ključne poudarke, o katerih morate razmišljati pri vsaki izmed njih. Načrt lekcije vas popelje od razumevanja osnovnih konceptov in izzivov do njihovega naslavljanja z ustreznimi tehnikami oblikovanja pozivov in najboljšimi praksami. Upoštevajte, da se oddelek "Napredne tehnike" v tem vodniku nanaša na vsebino, obravnavano v _naslednjem_ poglavju tega učnega načrta.

## Naš startup

Zdaj pa se pogovorimo o tem, kako _ta tema_ povezuje z našo misijo startup podjetja, da [prinesemo AI inovacije v izobraževanje](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Želimo zgraditi AI-podprte aplikacije za _personalizirano učenje_ - zato razmislimo, kako bi različni uporabniki naše aplikacije lahko "oblikovali" pozive:

- **Administratorji** bi lahko prosili AI, da _analizira podatke o učnem načrtu za prepoznavanje vrzeli v pokritosti_. AI lahko povzame rezultate ali jih vizualizira s kodo.
- **Učitelji** bi lahko prosili AI, da _ustvari učni načrt za ciljno občinstvo in temo_. AI lahko zgradi personaliziran načrt v določenem formatu.
- **Študenti** bi lahko prosili AI, da jih _inštruira v težkem predmetu_. AI lahko zdaj vodi študente z lekcijami, namigi in primeri, prilagojenimi njihovi ravni.

To je le vrh ledene gore. Oglejte si [Pozivi za izobraževanje](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - odprtokodno knjižnico pozivov, ki so jo pripravili strokovnjaki za izobraževanje - da dobite širši občutek možnosti! _Poskusite zagnati nekaj teh pozivov v sandboxu ali uporabiti OpenAI Playground, da vidite, kaj se zgodi!_

## Kaj je oblikovanje pozivov?

To lekcijo smo začeli z definicijo **oblikovanja pozivov** kot procesa _oblikovanja in optimizacije_ besedilnih vnosov (pozivov), da zagotovimo dosledne in kakovostne odgovore (dokončanja) za določen cilj aplikacije in modela. To lahko razumemo kot 2-stopenjski proces:

- _oblikovanje_ začetnega poziva za določen model in cilj
- _izpopolnjevanje_ poziva iterativno, da izboljšamo kakovost odgovora

To je nujno proces poskusov in napak, ki zahteva intuicijo uporabnika in trud za dosego optimalnih rezultatov. Zakaj je to pomembno? Da bi odgovorili na to vprašanje, moramo najprej razumeti tri koncepte:

- _Tokenizacija_ = kako model "vidi" poziv
- _Osnovni LLM_ = kako osnovni model "obdeluje" poziv
- _Instrukcijsko prilagojeni LLM_ = kako model zdaj lahko vidi "naloge"

### Tokenizacija

LLM vidi pozive kot _zaporedje tokenov_, kjer lahko različni modeli (ali različice modela) tokenizirajo isti poziv na različne načine. Ker so LLM-ji usposobljeni na tokenih (in ne na surovem besedilu), način, kako se pozivi tokenizirajo, neposredno vpliva na kakovost ustvarjenega odgovora.

Da bi dobili intuicijo za to, kako deluje tokenizacija, poskusite orodja, kot je [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst), prikazano spodaj. Kopirajte svoj poziv - in poglejte, kako se pretvori v tokene, pri čemer bodite pozorni na to, kako so obdelani presledki in ločila. Upoštevajte, da ta primer prikazuje starejši LLM (GPT-3) - tako da lahko poskus s novejšim modelom prinese drugačen rezultat.

### Koncept: Osnovni modeli

Ko je poziv tokeniziran, je glavna funkcija ["Osnovnega LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (ali osnovnega modela) napovedovanje tokena v tem zaporedju. Ker so LLM-ji usposobljeni na ogromnih besedilnih podatkovnih nizih, imajo dober občutek za statistične odnose med tokeni in lahko to napoved naredijo z nekaj zaupanja. Upoštevajte, da ne razumejo _pomena_ besed v pozivu ali tokenu; vidijo le vzorec, ki ga lahko "dopolnijo" s svojo naslednjo napovedjo. Lahko nadaljujejo z napovedovanjem zaporedja, dokler ga ne prekine uporabniška intervencija ali kakšen vnaprej določen pogoj.

Želite videti, kako deluje dokončanje na podlagi pozivov? Vnesite zgornji poziv v Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) z privzetimi nastavitvami. Sistem je konfiguriran tako, da obravnava pozive kot zahteve za informacije - tako bi morali videti dokončanje, ki zadovoljuje ta kontekst.

Kaj pa, če uporabnik želi videti nekaj specifičnega, kar izpolnjuje določena merila ali cilj naloge? Tukaj pridejo v poštev _instrukcijsko prilagojeni_ LLM-ji.

### Koncept: Instrukcijsko prilagojeni LLM-ji

[Instrukcijsko prilagojen LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) začne z osnovnim modelom in ga fino prilagodi s primeri ali pari vhod/izhod (npr. večkratna "sporočila"), ki lahko vsebujejo jasna navodila - in odgovor AI poskuša slediti temu navodilu.

To uporablja tehnike, kot je učenje z okrepitvijo s človeškimi povratnimi informacijami (RLHF), ki lahko model naučijo _slediti navodilom_ in _učiti se iz povratnih informacij_, tako da ustvarja odgovore, ki so bolje prilagojeni praktičnim aplikacijam in bolj ustrezajo ciljem uporabnika.

Poskusimo - ponovno obiščite zgornji poziv, vendar zdaj spremenite _sistemsko sporočilo_, da zagotovite naslednje navodilo kot kontekst:

> _Povzemi vsebino, ki ti je bila dana, za učenca drugega razreda. Rezultat naj bo en odstavek s 3-5 točkami._

Vidite, kako je rezultat zdaj prilagojen, da odraža želeni cilj in format? Učitelj lahko zdaj neposredno uporabi ta odgovor v svojih diapozitivih za ta razred.

## Zakaj potrebujemo oblikovanje pozivov?

Zdaj, ko vemo, kako LLM-ji obdelujejo pozive, se pogovorimo o tem, _zakaj_ potrebujemo oblikovanje pozivov. Odgovor leži v dejstvu, da trenutni LLM-ji predstavljajo številne izzive, zaradi katerih je _zanesljivo in dosledno dokončanje_ težje doseči brez truda pri oblikovanju in optimizaciji pozivov. Na primer:

1. **Odgovori modelov so stohastični.** _Isti poziv_ bo verjetno proizvedel različne odgovore z različnimi modeli ali različicami modelov. In lahko celo proizvede različne rezultate z _istim modelom_ v različnih časih. _Tehnike oblikovanja pozivov nam lahko pomagajo zmanjšati te variacije z zagotavljanjem boljših zaščitnih ukrepov_.

1. **Modeli lahko izmišljajo odgovore.** Modeli so predhodno usposobljeni z _velikimi, a končnimi_ podatkovnimi nizi, kar pomeni, da jim primanjkuje znanja o konceptih zunaj tega obsega usposabljanja. Posledično lahko proizvedejo dokončanja, ki so netočna, izmišljena ali neposredno nasprotujoča se znanim dejstvom. _Tehnike oblikovanja pozivov pomagajo uporabnikom prepoznati in omiliti takšne izmišljotine, npr. z zahtevo po citatih ali razmišljanju AI_.

1. **Zmožnosti modelov se bodo razlikovale.** Novejši modeli ali generacije modelov bodo imeli bogatejše zmožnosti, vendar bodo prinesli tudi edinstvene posebnosti in kompromisi v stroških in kompleksnosti. _Oblikovanje pozivov nam lahko pomaga razviti najboljše prakse in delovne tokove, ki abstrahirajo razlike in se prilagajajo specifičnim zahtevam modelov na skalabilne, brezhibne načine_.

Poglejmo to v akciji v OpenAI ali Azure OpenAI Playground:

- Uporabite isti poziv z različnimi LLM implementacijami (npr. OpenAI, Azure OpenAI, Hugging Face) - ste opazili variacije?
- Uporabite isti poziv večkrat z _isto_ LLM implementacijo (npr. Azure OpenAI playground) - kako so se te variacije razlikovale?

### Primer izmišljotin

V tem tečaju uporabljamo izraz **"izmišljotina"** za poimenovanje pojava, kjer LLM-ji včasih ustvarijo dejansko nepravilne informacije zaradi omejitev v svojem usposabljanju ali drugih omejitev. Morda ste to slišali tudi kot _"halucinacije"_ v priljubljenih člankih ali raziskovalnih člankih. Vendar močno priporočamo uporabo izraza _"izmišljotina"_, da ne bi po nesreči antropomorfizirali vedenja s pripisovanjem človeške lastnosti rezultatu, ki ga poganja stroj. To tudi krepi [smernice za odgovorno AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) z vidika terminologije, odstranjuje izraze, ki bi jih v nekaterih kontekstih lahko šteli za žaljive ali neinkluzivne.

Želite dobiti občutek, kako delujejo izmišljotine? Pomislite na poziv, ki AI naroči, da ustvari vsebino za neobstoječo temo (da zagotovite, da je ne najdemo v podatkovnem nizu za usposabljanje). Na primer - poskusil sem ta poziv:

> **Poziv:** ustvarite učni načrt o Marsovski vojni leta 2076.

Spletno iskanje mi je pokazalo, da obstajajo izmišljeni računi (npr. televizijske serije ali knjige) o Marsovskih vojnah - vendar nobena leta 2076. Zdrava pamet nam tudi pove, da je leto 2076 _v prihodnosti_ in zato ne more biti povezano z resničnim dogodkom.

Kaj se zgodi, ko zaženemo ta poziv z različnimi ponudniki LLM?

> **Odgovor 1**: OpenAI Playground (GPT-35)

> **Odgovor 2**: Azure OpenAI Playground (GPT-35)

> **Odgovor 3**: : Hugging Face Chat Playground (LLama-2)

Kot je bilo pričakovano, vsak model (ali različica modela) proizvede nekoliko drugačne odgovore zaradi stohastičnega vedenja in variacij zmogljivosti modela. Na primer, en model cilja na občinstvo osmega razreda, medtem ko drugi predvideva srednješolskega učenca. Vendar so vsi trije modeli ustvarili odgovore, ki bi lahko prepričali neobveščenega uporabnika, da je dogodek resničen.

Tehnike oblikovanja pozivov, kot sta _metaprompting_ in _konfiguracija temperature_, lahko zmanjšajo izmišljotine modela do neke mere. Nove arhitekture _oblikovanja pozivov_ prav tako vključujejo nova orodja in tehnike brezhibno v tok poziva, da omilijo ali zmanjšajo nekatere od teh učinkov.

## Študija primera: GitHub Copilot

Zaključimo ta odsek z občutkom
Končna vrednost predlog leži v sposobnosti ustvarjanja in objavljanja _knjižnic pozivov_ za vertikalne aplikacijske domene - kjer je predloga poziva zdaj _optimizirana_, da odraža aplikacijsko specifičen kontekst ali primere, ki naredijo odgovore bolj relevantne in natančne za ciljno uporabniško občinstvo. Repozitorij [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) je odličen primer tega pristopa, saj kurira knjižnico pozivov za izobraževalno področje s poudarkom na ključnih ciljih, kot so načrtovanje lekcij, oblikovanje učnega načrta, tutorstvo študentov itd.

## Podporna vsebina

Če razmišljamo o konstrukciji pozivov kot o navodilu (nalogi) in cilju (primarni vsebini), potem je _sekundarna vsebina_ kot dodatni kontekst, ki ga zagotavljamo, da **na nek način vpliva na izhod**. To bi lahko bili parametri nastavitve, navodila za oblikovanje, taksonomije tem itd., ki lahko pomagajo modelu _prilagoditi_ svoj odziv, da ustreza želenim uporabniškim ciljem ali pričakovanjem.

Na primer: Glede na katalog tečajev z obsežnimi metapodatki (ime, opis, raven, oznake metapodatkov, inštruktor itd.) o vseh razpoložljivih tečajih v učnem načrtu:

- lahko določimo navodilo za "povzetek kataloga tečajev za jesen 2023"
- lahko uporabimo primarno vsebino, da zagotovimo nekaj primerov želenega izhoda
- lahko uporabimo sekundarno vsebino, da identificiramo 5 najboljših "oznak" zanimanja.

Zdaj lahko model poda povzetek v formatu, ki ga kažejo nekaj primerov - ampak če ima rezultat več oznak, lahko prioritizira 5 oznak, identificiranih v sekundarni vsebini.

---

<!--
PREDLOGA LEKCIJE:
Ta enota naj pokriva osrednji koncept #1.
Okrepite koncept s primeri in referencami.

KONCEPT #3:
Tehnike inženiringa pozivov.
Katere so nekatere osnovne tehnike za inženiring pozivov?
Ponazorite jih z vajami.
-->

## Najboljše prakse pozivanja

Zdaj, ko vemo, kako se lahko pozivi _konstruirajo_, lahko začnemo razmišljati o tem, kako jih _oblikovati_, da odražajo najboljše prakse. O tem lahko razmišljamo v dveh delih - imeti pravo _miselnost_ in uporabiti prave _tehnike_.

### Miselnost inženiringa pozivov

Inženiring pozivov je proces poskusov in napak, zato imejte v mislih tri široke vodilne dejavnike:

1. **Razumevanje domene je pomembno.** Natančnost in relevantnost odziva je funkcija _domene_, v kateri deluje aplikacija ali uporabnik. Uporabite svojo intuicijo in strokovno znanje na področju, da še dodatno **prilagodite tehnike**. Na primer, definirajte _specifične osebnosti domene_ v sistemskih pozivih ali uporabite _specifične predloge domene_ v uporabniških pozivih. Zagotovite sekundarno vsebino, ki odraža kontekste specifične za domeno, ali uporabite _namige in primere specifične za domeno_, da usmerite model k znanim vzorcem uporabe.

2. **Razumevanje modela je pomembno.** Vemo, da so modeli po naravi stohastični. Toda implementacije modelov se lahko razlikujejo tudi glede na podatkovni sklop za usposabljanje, ki ga uporabljajo (predhodno usposobljeno znanje), zmogljivosti, ki jih zagotavljajo (npr. prek API ali SDK) in vrsto vsebine, za katero so optimizirani (npr. koda proti slikam proti besedilu). Razumite prednosti in omejitve modela, ki ga uporabljate, in uporabite to znanje za _prioritizacijo nalog_ ali gradnjo _prilagojenih predlog_, ki so optimizirane za zmogljivosti modela.

3. **Iteracija in validacija sta pomembni.** Modeli se hitro razvijajo, prav tako pa se razvijajo tudi tehnike za inženiring pozivov. Kot strokovnjak za domeno imate morda druge kontekste ali kriterije za _vašo_ specifično aplikacijo, ki morda ne veljajo za širšo skupnost. Uporabite orodja in tehnike inženiringa pozivov za "hitro začetek" konstrukcije pozivov, nato iterirajte in validirajte rezultate z lastno intuicijo in strokovnim znanjem na področju. Zabeležite svoje vpoglede in ustvarite **bazo znanja** (npr. knjižnice pozivov), ki jih lahko drugi uporabijo kot novo izhodišče za hitrejše iteracije v prihodnosti.

## Najboljše prakse

Zdaj si poglejmo običajne najboljše prakse, ki jih priporočajo praktiki [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) in [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Kaj                              | Zakaj                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Ocenite najnovejše modele.       | Nove generacije modelov verjetno imajo izboljšane funkcije in kakovost - vendar lahko povzročijo tudi višje stroške. Ocenite jih glede na vpliv, nato sprejmite odločitve o migraciji.                                                                                |
| Ločite navodila in kontekst   | Preverite, ali vaš model/provajder definira _delimitatorje_, da jasneje loči navodila, primarno in sekundarno vsebino. To lahko pomaga modelom natančneje dodeliti uteži tokenom.                                                         |
| Bodite specifični in jasni             | Podajte več podrobnosti o želenem kontekstu, izidu, dolžini, formatu, slogu itd. To bo izboljšalo tako kakovost kot doslednost odgovorov. Zajemite recepte v ponovno uporabljivih predlogah.                                                          |
| Bodite opisni, uporabite primere      | Modeli se lahko bolje odzovejo na pristop "pokaži in povej". Začnite z `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
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

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` vrednostmi. Vrnite se na [odsek Learning Sandbox](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) za učenje kako.

### Nato odprite Jupyter Notebook

- Izberite jedro za zagon. Če uporabljate možnosti 1 ali 2, preprosto izberite privzeto jedro Python 3.10.x, ki ga zagotavlja razvojna posoda.

Pripravljeni ste na izvajanje vaj. Upoštevajte, da tukaj ni _pravih in napačnih_ odgovorov - samo raziskovanje možnosti s poskusi in napakami ter gradnja intuicije za to, kar deluje za določen model in aplikacijsko domeno.

_Zaradi tega v tej lekciji ni segmentov Rešitve kode. Namesto tega bo Notebook imel celice Markdown z naslovom "Moja rešitev:", ki prikazuje en primer izhoda za referenco._

 <!--
PREDLOGA LEKCIJE:
Zaključite odsek s povzetkom in viri za samostojno učenje.
-->

## Preverjanje znanja

Kateri od naslednjih je dober poziv, ki sledi nekaterim razumnim najboljšim praksam?

1. Pokaži mi sliko rdečega avtomobila
2. Pokaži mi sliko rdečega avtomobila znamke Volvo in modela XC90 parkiranega ob pečini ob sončnem zahodu
3. Pokaži mi sliko rdečega avtomobila znamke Volvo in modela XC90

A: 2, to je najboljši poziv, saj zagotavlja podrobnosti o "čemu" in gre v specifike (ne samo kateri koli avto, ampak določena znamka in model) ter opisuje celoten kontekst. 3 je naslednji najboljši, saj prav tako vsebuje veliko opisov.

## 🚀 Izziv

Preverite, ali lahko izkoristite tehniko "namiga" s pozivom: Dokončaj stavek "Pokaži mi sliko rdečega avtomobila znamke Volvo in ". Kaj odgovori in kako bi to izboljšali?

## Odlično delo! Nadaljujte z učenjem

Želite izvedeti več o različnih konceptih inženiringa pozivov? Obiščite [stran za nadaljnje učenje](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da najdete druge odlične vire o tej temi.

Pojdite na lekcijo 5, kjer bomo pogledali [napredne tehnike pozivanja](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI prevajanja [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv profesionalni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne razlage, ki bi izhajale iz uporabe tega prevoda.