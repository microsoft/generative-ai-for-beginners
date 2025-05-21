<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-05-19T16:29:33+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "sl"
}
-->
# Osnove načrtovanja pozivov

## Uvod
Ta modul zajema osnovne koncepte in tehnike za ustvarjanje učinkovitih pozivov v generativnih AI modelih. Način, kako napišete svoj poziv LLM, je pomemben. Skrbno oblikovan poziv lahko doseže boljšo kakovost odgovora. Kaj pa pravzaprav pomenijo izrazi, kot sta _poziv_ in _načrtovanje pozivov_? In kako izboljšam poziv _vnos_, ki ga pošljem LLM? To so vprašanja, na katera bomo poskušali odgovoriti v tem poglavju in naslednjem.

_Generativna AI_ je sposobna ustvariti novo vsebino (npr. besedilo, slike, zvok, kodo itd.) kot odziv na zahteve uporabnikov. To dosega z uporabo _Velikih jezikovnih modelov_ kot je serija OpenAI GPT ("Generativni predhodno usposobljeni transformator"), ki so usposobljeni za uporabo naravnega jezika in kode.

Uporabniki lahko zdaj komunicirajo s temi modeli s pomočjo znanih paradigmov, kot je klepet, brez potrebe po tehničnem znanju ali usposabljanju. Modeli so _na osnovi pozivov_ - uporabniki pošljejo besedilni vnos (poziv) in prejmejo AI odgovor (dokončanje). Nato lahko "klepetajo z AI" iterativno, v več zavojih pogovorov, izpopolnjujejo svoj poziv, dokler odgovor ne ustreza njihovim pričakovanjem.

"Pozivi" zdaj postanejo primarni _programski vmesnik_ za generativne AI aplikacije, ki modelom povedo, kaj naj storijo in vplivajo na kakovost vrnjenih odgovorov. "Načrtovanje pozivov" je hitro rastoče področje študija, ki se osredotoča na _oblikovanje in optimizacijo_ pozivov za zagotavljanje doslednih in kakovostnih odgovorov v velikem obsegu.

## Cilji učenja

V tej lekciji se naučimo, kaj je načrtovanje pozivov, zakaj je pomembno, in kako lahko oblikujemo bolj učinkovite pozive za določen model in cilj aplikacije. Razumeli bomo osnovne koncepte in najboljše prakse za načrtovanje pozivov - ter se seznanili z interaktivnim okoljem "sandbox" v Jupyter Notebooks, kjer lahko te koncepte vidimo v resničnih primerih.

Do konca te lekcije bomo sposobni:

1. Pojasniti, kaj je načrtovanje pozivov in zakaj je pomembno.
2. Opisati komponente poziva in kako se uporabljajo.
3. Naučiti se najboljših praks in tehnik za načrtovanje pozivov.
4. Uporabiti naučene tehnike na resničnih primerih, z uporabo OpenAI endpointa.

## Ključni izrazi

Načrtovanje pozivov: Praksa oblikovanja in izpopolnjevanja vnosov za usmerjanje AI modelov k ustvarjanju želenih rezultatov.
Tokenizacija: Proces pretvorbe besedila v manjše enote, imenovane tokeni, ki jih model lahko razume in obdela.
LLM-ji uglašeni z navodili: Veliki jezikovni modeli (LLM-ji), ki so bili fino uglašeni s specifičnimi navodili za izboljšanje natančnosti in ustreznosti njihovih odgovorov.

## Sandbox za učenje

Načrtovanje pozivov je trenutno bolj umetnost kot znanost. Najboljši način za izboljšanje naše intuicije za to je, da _več vadimo_ in sprejmemo pristop poskusov in napak, ki združuje strokovno znanje na področju aplikacij z priporočljivimi tehnikami in modelno specifičnimi optimizacijami.

Jupyter Notebook, ki spremlja to lekcijo, zagotavlja _sandbox_ okolje, kjer lahko preizkusite, kar se naučite - med učenjem ali kot del kode izziva na koncu. Za izvedbo vaj boste potrebovali:

1. **Azure OpenAI API ključ** - storitveni endpoint za uveden LLM.
2. **Python Runtime** - v katerem se lahko izvede Notebook.
3. **Lokalne okoljske spremenljivke** - _izpolnite korake [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst), da se pripravite_.

Notebook vsebuje _začetne_ vaje - vendar ste spodbujeni, da dodate svoje _Markdown_ (opis) in _Code_ (zahteve za poziv) sekcije, da preizkusite več primerov ali idej - in zgradite svojo intuicijo za oblikovanje pozivov.

## Ilustrirani vodnik

Želite dobiti celotno sliko o tem, kaj ta lekcija zajema, preden se potopite vanjo? Oglejte si ta ilustrirani vodnik, ki vam daje občutek glavnih tem, ki jih zajema, in ključne zaključke, o katerih lahko razmislite v vsakem od njih. Načrt lekcije vas vodi od razumevanja osnovnih konceptov in izzivov do njihovega naslavljanja z ustreznimi tehnikami načrtovanja pozivov in najboljšimi praksami. Upoštevajte, da se oddelek "Napredne tehnike" v tem vodniku nanaša na vsebino, zajeto v _naslednjem_ poglavju tega kurikuluma.

## Naš startup

Zdaj pa se pogovorimo o tem, kako _ta tema_ se nanaša na našo startup misijo [prinašanja AI inovacij v izobraževanje](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Želimo zgraditi AI-poganjane aplikacije za _personalizirano učenje_ - zato razmislimo, kako različni uporabniki naše aplikacije lahko "oblikujejo" pozive:

- **Administratorji** bi lahko prosili AI, da _analizira podatke o kurikulu, da identificira vrzeli v pokritosti_. AI lahko povzame rezultate ali jih vizualizira s kodo.
- **Izobraževalci** bi lahko prosili AI, da _ustvari načrt lekcije za ciljno občinstvo in temo_. AI lahko zgradi personaliziran načrt v določenem formatu.
- **Študenti** bi lahko prosili AI, da _jih poučuje v težki temi_. AI lahko zdaj vodi študente z lekcijami, namigi in primeri, prilagojenimi njihovi ravni.

To je le vrh ledene gore. Oglejte si [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - odprtokodno knjižnico pozivov, ki jo kurirajo izobraževalni strokovnjaki - da dobite širši občutek možnosti! _Preizkusite nekaj teh pozivov v sandboxu ali z uporabo OpenAI Playground, da vidite, kaj se zgodi!_

## Kaj je načrtovanje pozivov?

To lekcijo smo začeli z definiranjem **načrtovanja pozivov** kot procesa _oblikovanja in optimizacije_ besedilnih vnosov (pozivov) za zagotavljanje doslednih in kakovostnih odgovorov (dokončanj) za določen cilj aplikacije in model. To lahko mislimo kot 2-stopenjski proces:

- _oblikovanje_ začetnega poziva za določen model in cilj
- _izpopolnjevanje_ poziva iterativno za izboljšanje kakovosti odgovora

To je nujno proces poskusov in napak, ki zahteva intuicijo uporabnika in trud za dosego optimalnih rezultatov. Zakaj je to pomembno? Da odgovorimo na to vprašanje, moramo najprej razumeti tri koncepte:

- _Tokenizacija_ = kako model "vidi" poziv
- _Osnovni LLM-ji_ = kako temeljni model "procesira" poziv
- _LLM-ji uglašeni z navodili_ = kako model lahko zdaj vidi "naloge"

### Tokenizacija

LLM vidi pozive kot _zaporedje tokenov_, kjer lahko različni modeli (ali različice modela) tokenizirajo isti poziv na različne načine. Ker so LLM-ji usposobljeni na tokenih (in ne na surovem besedilu), način, kako se pozivi tokenizirajo, neposredno vpliva na kakovost generiranega odgovora.

Da dobite intuicijo, kako tokenizacija deluje, preizkusite orodja, kot je [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst), prikazano spodaj. Kopirajte svoj poziv - in si oglejte, kako se pretvori v tokene, pri čemer bodite pozorni, kako se obravnavajo znaki praznega prostora in ločila. Upoštevajte, da ta primer prikazuje starejši LLM (GPT-3) - zato lahko poskus s novejšim modelom povzroči drugačen rezultat.

### Koncept: Temeljni modeli

Ko je poziv tokeniziran, je primarna funkcija ["Osnovnega LLM-ja"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (ali temeljnega modela) napovedovanje tokena v tem zaporedju. Ker so LLM-ji usposobljeni na ogromnih besedilnih zbirkah podatkov, imajo dober občutek za statistične odnose med tokeni in lahko to napoved naredijo z določeno stopnjo zaupanja. Upoštevajte, da ne razumejo _pomena_ besed v pozivu ali tokenu; vidijo le vzorec, ki ga lahko "dokončajo" z naslednjo napovedjo. Lahko nadaljujejo napovedovanje zaporedja, dokler ga ne prekine uporabniški poseg ali neka predhodno določena pogoj.

Želite videti, kako deluje dokončanje na osnovi pozivov? Vnesite zgornji poziv v Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) z privzetimi nastavitvami. Sistem je konfiguriran tako, da obravnava pozive kot zahteve za informacije - zato bi morali videti dokončanje, ki ustreza temu kontekstu.

Kaj pa, če bi uporabnik želel videti nekaj specifičnega, kar ustreza nekaterim merilom ali ciljem naloge? Tukaj pridejo v poštev _LLM-ji uglašeni z navodili_.

### Koncept: LLM-ji uglašeni z navodili

[LLM uglašen z navodili](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) začne s temeljnim modelom in ga fino uglašuje z zgledi ali pari vhod/izhod (npr. večzavojnimi "sporočili"), ki lahko vsebujejo jasna navodila - in odgovor AI poskuša slediti tem navodilom.

To uporablja tehnike, kot je krepitev učenja s povratnimi informacijami uporabnikov (RLHF), ki lahko model usposobi za _sledenje navodilom_ in _učenje iz povratnih informacij_, tako da ustvarja odgovore, ki so bolj primerni za praktične aplikacije in bolj relevantni za cilje uporabnikov.

Poskusimo - ponovno preglejte zgornji poziv, vendar zdaj spremenite _sistemsko sporočilo_, da zagotovite naslednje navodilo kot kontekst:

> _Povzemite vsebino, ki vam je dana, za učenca drugega razreda. Rezultat naj bo en odstavek s 3-5 točkami._

Vidite, kako je rezultat zdaj uglašen, da odraža želeni cilj in format? Izobraževalec lahko zdaj neposredno uporabi ta odgovor v svojih diapozitivih za to razred.

## Zakaj potrebujemo načrtovanje pozivov?

Zdaj, ko vemo, kako pozive obdelujejo LLM-ji, se pogovorimo o _zakaj_ potrebujemo načrtovanje pozivov. Odgovor leži v dejstvu, da trenutni LLM-ji postavljajo številne izzive, zaradi katerih je _zanesljivo in dosledno dokončanje_ težje doseči brez truda pri konstrukciji in optimizaciji pozivov. Na primer:

1. **Odgovori modela so stohastični.** _Isti poziv_ bo verjetno ustvaril različne odgovore z različnimi modeli ali različicami modela. In lahko celo ustvari različne rezultate z _istim modelom_ ob različnih časih. _Tehnike načrtovanja pozivov nam lahko pomagajo zmanjšati te variacije z zagotavljanjem boljših varoval_.

2. **Modeli lahko izmišljajo odgovore.** Modeli so predhodno usposobljeni z _velikimi, a končnimi_ zbirkami podatkov, kar pomeni, da jim primanjkuje znanja o konceptih zunaj tega obsega usposabljanja. Posledično lahko ustvarijo dokončanja, ki so netočna, izmišljena ali neposredno nasprotujoča znanim dejstvom. _Tehnike načrtovanja pozivov pomagajo uporabnikom prepoznati in omiliti takšne izmišljotine, npr. z zahtevanjem AI za citate ali razloge_.

3. **Zmožnosti modelov se bodo razlikovale.** Novejši modeli ali generacije modelov bodo imeli bogatejše zmožnosti, vendar bodo prinesli tudi edinstvene posebnosti in kompromise v stroških in kompleksnosti. _Načrtovanje pozivov nam lahko pomaga razviti najboljše prakse in delovne tokove, ki abstrahirajo razlike in se prilagajajo specifičnim zahtevam modela na skalabilne, brezhibne načine_.

Poglejmo to v akciji v OpenAI ali Azure OpenAI Playground:

- Uporabite isti poziv z različnimi LLM uvedbami (npr. OpenAI, Azure OpenAI, Hugging Face) - ste opazili variacije?
- Uporabite isti poziv večkrat z _istim_ LLM uvedbo (npr. Azure OpenAI playground) - kako so se te variacije razlikovale?

### Primer izmišljotin

V tem tečaju uporabljamo izraz **"izmišljotina"** za opis pojava, kjer LLM-ji včasih ustvarijo dejansko napačne informacije zaradi omejitev v njihovem usposabljanju ali drugih omejitev. Morda ste to slišali tudi kot _"halucinacije"_ v popularnih člankih ali raziskovalnih prispevkih. Vendar močno priporočamo uporabo izraza _"izmišljotina"_ kot izraza, da ne bi nenamerno antropomorfizirali vedenja z pripisovanjem človeške lastnosti rezultatu, ki ga poganja stroj. To tudi krepi [smernice za odgovorno AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) z vidika terminologije, odstranjuje izraze, ki bi jih lahko v nekaterih kontekstih obravnavali kot žaljive ali neinkluzivne.

Želite dobiti občutek, kako izmišljotine delujejo? Pomislite na poziv, ki AI naroča, naj ustvari vsebino za neobstoječo temo (da se prepričate, da ni v usposobitvenem naboru podatkov). Na primer - poskusil sem ta poziv:

> **Poziv:** ustvarite načrt lekcije o Marsovski vojni leta 2076.

Spletno iskanje mi je pokazalo, da so obstajali izmišljeni računi (npr. televizijske serije ali knjige) o Marsovskih vojnah - vendar nobena leta 2076. Zdrava pamet nam tudi pove, da je leto 2076 _v prihodnosti_ in zato ne more biti povezano z resničnim dogodkom.

Kaj se zgodi, ko zaženemo ta poziv z različnimi LLM ponudniki?

> **Odgovor 1**: OpenAI Playground (GPT-35)

> **Odgovor 2**: Azure OpenAI Playground (GPT-35)

> **Odgovor 3**: Hugging Face Chat Playground (LLama-2)

Kot pričakovano, vsak model (ali različica modela) ustvari nekoliko različne odgovore zaradi stohastičnega vedenja in variacij zmožnosti modela. Na primer, en model cilja na občinstvo 8. razreda, medtem ko drugi predvideva srednješolskega učenca. Vendar so vsi trije modeli ustvarili odgovore, ki bi lahko prepričali neinformiranega uporabnika, da je dogodek resničen.

Tehnike načrtovanja pozivov, kot sta _metaprompting_ in _konfiguracija temperature_, lahko do neke mere zmanjšajo izmišljotine modelov. Nove arhitekture načrtovanja pozivov prav tako vključujejo nova orodja in tehnike brezhibno v tok poziva, da omilijo ali zmanjšajo nekatere od teh učinkov.

## Študija primera: GitHub Copilot

Zaključimo ta oddelek z občutkom, kako se načrtovanje pozivov uporablja v resničnih rešitvah, tako da
Končno, prava vrednost predlog je v sposobnosti ustvarjanja in objavljanja _knjižnic predlog_ za vertikalna področja uporabe - kjer je predloga sedaj _optimizirana_ tako, da odraža specifičen kontekst ali primere, ki naredijo odgovore bolj relevantne in natančne za ciljno občinstvo. Repozitorij [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) je odličen primer tega pristopa, saj zbira knjižnico predlog za izobraževalno področje s poudarkom na ključnih ciljih, kot so načrtovanje lekcij, oblikovanje kurikuluma, mentorstvo študentov itd.

## Podporna vsebina

Če razmišljamo o konstrukciji predlog kot o navodilu (nalogi) in cilju (primarni vsebini), potem je _sekundarna vsebina_ kot dodatni kontekst, ki ga zagotovimo za **vplivanje na izhod na nek način**. Lahko gre za prilagoditvene parametre, navodila za oblikovanje, taksonomije tem itd., ki lahko pomagajo modelu _prilagoditi_ svoj odgovor, da ustreza želenim ciljem ali pričakovanjem uporabnika.

Na primer: Glede na katalog tečajev z obsežnimi metapodatki (ime, opis, raven, oznake metapodatkov, inštruktor itd.) o vseh razpoložljivih tečajih v kurikulumu:

- lahko definiramo navodilo za "povzetek kataloga tečajev za jesen 2023"
- lahko uporabimo primarno vsebino, da zagotovimo nekaj primerov želenega izhoda
- lahko uporabimo sekundarno vsebino, da identificiramo top 5 "oznak" zanimanja.

Sedaj lahko model zagotovi povzetek v formatu, ki ga prikazujejo primeri - vendar če rezultat vsebuje več oznak, lahko prioritizira 5 oznak, identificiranih v sekundarni vsebini.

## Najboljše prakse pri oblikovanju predlog

Sedaj, ko vemo, kako lahko predloge _konstrukcijsko_, lahko začnemo razmišljati o tem, kako jih _oblikovati_, da odražajo najboljše prakse. O tem lahko razmišljamo v dveh delih - imeti pravo _miselnost_ in uporabiti prave _tehnike_.

### Miselnost pri oblikovanju predlog

Oblikovanje predlog je proces poskusov in napak, zato imejte v mislih tri široke vodilne dejavnike:

1. **Razumevanje domene je pomembno.** Natančnost in relevantnost odgovora sta odvisni od _domene_, v kateri aplikacija ali uporabnik deluje. Uporabite svojo intuicijo in strokovno znanje na področju domene za **nadaljnje prilagajanje tehnik**. Na primer, definirajte _specifične osebnosti domene_ v svojih sistemskih predlogah ali uporabite _specifične predloge domene_ v svojih uporabniških predlogah. Zagotovite sekundarno vsebino, ki odraža kontekste specifične za domeno, ali uporabite _namige in primere specifične za domeno_, da usmerite model k znanim vzorcem uporabe.

2. **Razumevanje modela je pomembno.** Vemo, da so modeli po naravi stohastični. Toda implementacije modelov se lahko razlikujejo tudi glede na podatkovne nize, ki jih uporabljajo za usposabljanje (predhodno znanje), sposobnosti, ki jih zagotavljajo (npr. preko API ali SDK) in vrsto vsebine, za katero so optimizirani (npr. koda proti slikam proti besedilu). Razumite prednosti in omejitve modela, ki ga uporabljate, in uporabite to znanje za _prioritizacijo nalog_ ali gradnjo _prilagojenih predlog_, ki so optimizirane za sposobnosti modela.

3. **Iteracija in validacija sta pomembni.** Modeli se hitro razvijajo, prav tako tudi tehnike za oblikovanje predlog. Kot strokovnjak na področju domene lahko imate drug kontekst ali merila za _vašo_ specifično aplikacijo, ki morda ne veljajo za širšo skupnost. Uporabite orodja in tehnike za oblikovanje predlog, da "začnete" konstrukcijo predlog, nato iterirajte in validirajte rezultate z uporabo lastne intuicije in strokovnega znanja na področju domene. Zabeležite svoje vpoglede in ustvarite **bazo znanja** (npr. knjižnice predlog), ki jo lahko drugi uporabijo kot novo izhodišče za hitrejše iteracije v prihodnosti.

## Najboljše prakse

Sedaj si poglejmo pogoste najboljše prakse, ki jih priporočajo praktiki [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) in [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Kaj                                | Zakaj                                                                                                                                                                                                                                               |
| :--------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ocenite najnovejše modele.         | Nove generacije modelov verjetno ponujajo izboljšane funkcije in kakovost - vendar lahko povzročijo tudi višje stroške. Ocenite jih za vpliv, nato sprejmite odločitve o migraciji.                                                                 |
| Ločite navodila in kontekst        | Preverite, ali vaš model/ponudnik definira _mejnike_ za jasnejše ločevanje navodil, primarne in sekundarne vsebine. To lahko pomaga modelom natančneje dodeliti uteži tokenom.                                                                         |
| Bodite specifični in jasni         | Podajte več podrobnosti o želenem kontekstu, izidu, dolžini, formatu, slogu itd. To bo izboljšalo tako kakovost kot doslednost odgovorov. Zajemite recepte v ponovno uporabnih predlogah.                                                             |
| Bodite opisni, uporabite primere   | Modeli se lahko bolje odzovejo na pristop "pokaži in povej". Začnite z `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
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

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` vrednostmi. Vrnite se na [odsek Učilnica za učenje](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals), da se naučite, kako.

### Nato odprite zvezek Jupyter

- Izberite jedro izvajanja. Če uporabljate možnosti 1 ali 2, preprosto izberite privzeto jedro Python 3.10.x, ki ga zagotavlja razvojna posoda.

Pripravljeni ste za izvajanje vaj. Upoštevajte, da tukaj ni _pravih in napačnih_ odgovorov - samo raziskovanje možnosti s poskusi in napakami ter gradnja intuicije za to, kaj deluje za določen model in področje uporabe.

_Zaradi tega v tej lekciji ni segmentov z rešitvami kode. Namesto tega bo zvezek imel Markdown celice z naslovom "Moja rešitev:", ki prikazuje en primer izhoda za referenco._

## Preverjanje znanja

Kateri od naslednjih je dobra predloga, ki sledi nekaterim razumnim najboljšim praksam?

1. Pokaži mi sliko rdečega avtomobila
2. Pokaži mi sliko rdečega avtomobila znamke Volvo in modela XC90, parkiranega ob pečini ob sončnem zahodu
3. Pokaži mi sliko rdečega avtomobila znamke Volvo in modela XC90

A: 2, to je najboljša predloga, saj nudi podrobnosti o "čem" in gre v specifičnosti (ne samo kateri koli avto, ampak določena znamka in model) in prav tako opisuje celoten kontekst. 3 je naslednja najboljša, saj vsebuje veliko opisov.

## 🚀 Izziv

Preverite, ali lahko izkoristite tehniko "namiga" s predlogo: Dokončajte stavek "Pokaži mi sliko rdečega avtomobila znamke Volvo in ". Kaj odgovori, in kako bi ga izboljšali?

## Odlično delo! Nadaljujte z učenjem

Želite izvedeti več o različnih konceptih oblikovanja predlog? Obiščite [stran za nadaljnje učenje](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kjer boste našli druge odlične vire o tej temi.

Pojdite na Lekcijo 5, kjer bomo pogledali [napredne tehnike oblikovanja predlog](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije se priporoča profesionalni prevod s strani človeka. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.