# Osnove načrtovanja pozivov

[![Osnove načrtovanja pozivov](../../../translated_images/sl/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Uvod
Ta modul pokriva osnovne pojme in tehnike za ustvarjanje učinkovitih pozivov v generativnih modelih umetne inteligence. Tudi način, kako napišete poziv za velik jezikovni model (LLM), je pomemben. Natančno oblikovan poziv lahko zagotovi boljšo kakovost odgovora. Kaj pa natančno pomenita izraza _poziv_ in _načrtovanje pozivov_? In kako lahko izboljšam vhodni _poziv_, ki ga pošljem LLM? Na ta vprašanja bomo poskušali odgovoriti v tem in naslednjem poglavju.

_Generativna umetna inteligenca_ je sposobna ustvarjati novo vsebino (npr. besedilo, slike, zvok, kodo itd.) kot odziv na uporabniške zahteve. To dosega z uporabo _velikih jezikovnih modelov_ kot je serija GPT podjetja OpenAI ("Generative Pre-trained Transformer"), ki so usposobljeni za uporabo naravnega jezika in kode.

Uporabniki lahko zdaj komunicirajo s temi modeli z znanimi paradigmi, kot je klepet, brez tehničnega znanja ali usposabljanja. Modeli temeljijo na _pozivih_ – uporabniki pošljejo besedilni vhod (poziv) in prejmejo odgovor AI (dokončanje). Nato lahko iterativno "klepetajo z AI", v večkročnih pogovorih, pri čemer izboljšujejo svoj poziv, dokler odgovor ne ustreza njihovim pričakovanjem.

"Pozivi" postanejo glavni _programski vmesnik_ za aplikacije generativne AI, saj modelom povedo, kaj naj počnejo, in vplivajo na kakovost vrnjenih odgovorov. "Načrtovanje pozivov" je hitro rastoče področje študija, ki se osredotoča na _oblikovanje in optimizacijo_ pozivov, da zagotovi dosledne in kakovostne odgovore v velikem obsegu.

## Cilji učenja

V tej lekciji se naučimo, kaj je načrtovanje pozivov, zakaj je pomembno in kako lahko za določen model in aplikacijski cilj oblikujemo učinkovitejše pozive. Razumeli bomo osnovne pojme in najboljše prakse načrtovanja pozivov – ter se seznanili z interaktivnim okoljem Jupyter Notebook, kjer lahko vidimo praktično uporabo teh konceptov.

Ob koncu te lekcije bomo znali:

1. Pojasniti, kaj je načrtovanje pozivov in zakaj je pomembno.
2. Opisati sestavne dele poziva in kako se uporabljajo.
3. Naučiti se najboljših praks in tehnik za načrtovanje pozivov.
4. Uporabiti naučene tehnike na resničnih primerih z uporabo OpenAI končne točke.

## Ključni pojmi

Načrtovanje pozivov: Praksa oblikovanja in izpopolnjevanja vhodov za usmerjanje AI modelov k željenim izhodom.
Tokenizacija: Proces spreminjanja besedila v manjše enote, imenovane tokeni, ki jih model lahko razume in obdela.
LLM-i, prilagojeni navodilom: Veliki jezikovni modeli (LLM), ki so bili dodatno prilagojeni z določenimi navodili, da izboljšajo točnost in ustreznost odgovorov.

## Učilnica za učenje

Načrtovanje pozivov je trenutno bolj umetnost kot znanost. Najboljši način za izboljšanje intuicije je _več vadbe_ in uporaba pristopa poskusa in napake, ki združuje strokovno znanje na področju uporabe z priporočenimi tehnikami in optimizacijami, specifičnimi za model.

Jupyter Notebook, ki spremlja to lekcijo, zagotavlja _učilni prostor_, kjer lahko preizkusite, kar ste se naučili – sproti ali kot del izziva na koncu. Za izvajanje vaj boste potrebovali:

1. **Ključ za Azure OpenAI API** – storitveni konec za nameščen LLM.
2. **Python runtime** – v katerem se lahko izvaja zvezek.
3. **Lokalne okoljske spremenljivke** – _za pripravo sledite [NAVODILOM](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst)_.

Notebook vsebuje _izhodiščne_ vaje – a spodbujamo vas, da dodajate lastne odseke _Markdown_ (opis) in _Code_ (zahteve pozivov) za preizkus več primerov ali idej – ter gradite intuicijo za oblikovanje pozivov.

## Ilustriran vodič

Želite dobiti širši pregled, kaj ta lekcija pokriva, preden se poglobite? Oglejte si ta ilustriran vodič, ki vam predstavi glavne teme in ključne poudarke za razmislek v vsakem. Načrt poti lekcije vas vodi od razumevanja osnovnih pojmov in izzivov do njihove rešitve z ustreznimi tehnikami načrtovanja pozivov in najboljšimi praksami. Upoštevajte, da se del "Napredne tehnike" v tem vodiču nanaša na vsebino, obravnavano v _naslednjem_ poglavju tega učnega načrta.

![Ilustriran vodič za načrtovanje pozivov](../../../translated_images/sl/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Naš zagonski projekt

Pogovorimo se zdaj, kako se _ta tema_ povezuje z našo zagonsko nalogo, da [prinesemo inovacije umetne inteligence v izobraževanje](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Želimo graditi aplikacije, podprte z AI, za _personalizirano učenje_ – zato premislimo, kako bi različni uporabniki naše aplikacije lahko "oblikovali" pozive:

- **Administratorji** lahko od AI zahtevajo _analizo podatkov učnih načrtov za ugotavljanje vrzeli v pokritosti_. AI lahko povzame rezultate ali jih vizualizira z uporabo kode.
- **Učitelji** lahko AI prosijo, da _ustvari učni načrt za ciljno publiko in temo_. AI lahko ustvari personaliziran načrt v določenem formatu.
- **Študentje** lahko AI prosijo, da _jih poučuje v zahtevni predmetni temi_. AI lahko vodi študente z lekcijami, namigi in primeri, prilagojenimi njihovi ravni.

To je šele vrh ledene gore. Oglejte si [Pozive za izobraževanje](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – odprtokodno knjižnico pozivov, ki jo urejajo izobraževalni strokovnjaki – da dobite širši vpogled v možnosti! _Poskusite zagnati nekaj teh pozivov v učilnici ali z uporabo OpenAI Playground, da vidite, kaj se zgodi!_

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #1:
Prompt Engineering.
Define it and explain why it is needed.
-->

## Kaj je načrtovanje pozivov?

Lekcijo smo začeli z definicijo **načrtovanja pozivov** kot procesa _oblikovanja in optimizacije_ besedilnih vhodov (pozivov), da zagotovimo dosledne in kakovostne odzive (dokončanja) za določen aplikacijski cilj in model. To lahko razumemo kot dvostopenjski proces:

- _oblikovanje_ začetnega poziva za določen model in cilj
- _izpopolnjevanje_ poziva iterativno za izboljšanje kakovosti odgovora

To je nujno proces poskusa in napake, ki zahteva uporabniško intuicijo in trud za dosego optimalnih rezultatov. Zakaj je torej pomembno? Da bi to odgovorili, moramo najprej razumeti tri pojme:

- _tokenizacija_ = kako model "vidi" poziv
- _osnovni LLM-i_ = kako temeljni model "obdeluje" poziv
- _LLM-i, prilagojeni navodilom_ = kako model zdaj lahko vidi "naloge"

### Tokenizacija

LLM obravnava pozive kot _zaporedje tokenov_, kjer različni modeli (ali različice istega modela) lahko tokenizirajo isti poziv na različne načine. Ker so LLM usposobljeni na tokenih (in ne na surovem besedilu), način tokenizacije poziva neposredno vpliva na kakovost ustvarjenega odgovora.

Da dobite intuitiven občutek, kako tokenizacija deluje, preizkusite orodja, kot je [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst), prikazano spodaj. Kopirajte svoj poziv in si oglejte, kako se pretvori v tokene, bodite pozorni na to, kako se obravnavajo presledki in ločila. Opomba: primer prikazuje starejši LLM (GPT-3), zato lahko pri novejših modelih dobite drugačne rezultate.

![Tokenizacija](../../../translated_images/sl/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Pojem: Temeljni modeli

Ko je poziv tokeniziran, je glavna funkcija ["osnovnega LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (ali temeljnega modela) napovedovati naslednji token v zaporedju. Ker so LLM usposobljeni na ogromnih nizih besedil, imajo dober občutek za statistične odnose med tokeni in lahko s precejšnjo gotovostjo naredijo to napoved. Opomba: ne razumejo _pomena_ besed v pozivu ali tokenu; vidijo le vzorec, ki ga lahko "dokončajo" z naslednjo napovedjo. Napovedujejo zaporedje do prekinitve z uporabniško intervencijo ali vnaprej določenim pogojem.

Želite videti, kako deluje dokončanje na osnovi poziva? Vnesite zgornji poziv v Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) z privzetimi nastavitvami. Sistem je nastavljen, da obravnava pozive kot zahteve za informacije – zato boste dobili odgovor, ki ustreza temu kontekstu.

Kaj pa, če bi uporabnik želel videti nekaj specifičnega, kar ustreza določenim kriterijem ali cilju naloge? Takrat pridejo v igro _LLM-ji, prilagojeni navodilom_.

![Osnovni LLM dokončanje klepeta](../../../translated_images/sl/04-playground-chat-base.65b76fcfde0caa67.webp)

### Pojem: LLM-ji prilagojeni navodilom

[LLM, prilagojen navodilom](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) izhaja iz temeljnega modela in ga dodatno prilagodi z vzorci ali pari vhod/izhod (npr. večkrožni "sporočili"), ki lahko vsebujejo jasna navodila – odgovor AI pa skuša slediti tem navodilom.

Uporabljajo tehnike, kot je okrepljeno učenje z uporabniškim povratnim informacijam (RLHF), ki model usposobijo, da _sledi navodilom_ in _se uči iz povratnih informacij_, da proizvaja odgovore, ki so bolj primerni za praktične aplikacije in bolj relevantni za uporabniške cilje.

Preizkusimo to – ponovite zgornji poziv, a zdaj spremenite _sistemsko sporočilo_, da vključite naslednje navodilo kot kontekst:

> _Povzemite vsebino, ki vam je dana, za učenca drugega razreda osnovne šole. Rezultat naj bo v enem odstavku s 3-5 alinejami._

Vidite, kako je rezultat zdaj prilagojen cilju in formatu? Učitelj lahko ta odgovor direktno uporabi v svojih diapozitivih za ta razred.

![LLM prilagojen navodilom - dokončanje klepeta](../../../translated_images/sl/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Zakaj potrebujemo načrtovanje pozivov?

Ko zdaj razumemo, kako LLM obravnava pozive, lahko govorimo o tem, _zakaj_ je načrtovanje pozivov potrebno. Odgovor je v tem, da trenutni LLM-i postavljajo vrsto izzivov, zaradi katerih je težje doseči _zanesljiva in dosledna dokončanja_ brez truda pri gradnji in optimizaciji pozivov. Na primer:

1. **Odgovori modelov so stohastični.** _Isti poziv_ bo verjetno dal različne odgovore z različnimi modeli ali različicami modela. Prav tako lahko da različne rezultate z _istim modelom_ ob različnih časih. _Tehnike načrtovanja pozivov nam lahko pomagajo zmanjšati te razlike z uporabo boljših varoval_.

1. **Modeli lahko 'izmišljajo' odgovore.** Modeli so predhodno usposobljeni na _velikih, a končnih_ podatkovnih nizih, zato nimajo znanja o konceptih izven tega okvira. Posledično lahko proizvedejo dokončanja, ki so netočna, izmišljena ali neposredno v nasprotju z dejstvi. _Tehnike načrtovanja pozivov pomagajo uporabnikom prepoznati in ublažiti takšne izmišljotine, npr. z zahtevo po citatih ali razmišljanju AI_.

1. **Zmožnosti modelov se razlikujejo.** Novejši modeli ali generacije modelov bodo imeli bogatejše zmogljivosti, a tudi posebne značilnosti ter kompromis med stroški in kompleksnostjo. _Načrtovanje pozivov nam lahko pomaga razviti najboljše prakse in delovne tokove, ki abstraktno odpravijo razlike in se prilagajajo zahtevam posameznih modelov na skalabilen, gladek način_.

Poglejmo to v akciji v OpenAI ali Azure OpenAI Playground:

- Uporabite isti poziv z različnimi LLM namestitvami (npr. OpenAI, Azure OpenAI, Hugging Face) – ali ste opazili razlike?
- Uporabite isti poziv večkrat z _isto_ LLM namestitvijo (npr. Azure OpenAI playground) – kako so se te razlike razlikovale?

### Primer izmišljotin

V tem tečaju uporabljamo izraz **"izmišljotina"** za opis pojava, kjer LLM včasih ustvarjajo dejansko netočne informacije zaradi omejitev svojega usposabljanja ali drugih omejitev. Ta pojav ste morda slišali tudi kot _"halucinacije"_ v priljubljenih člankih ali raziskovalnih prispevkih. Vendar močno priporočamo uporabo izraza _"izmišljotina"_, da ne antropomorfiziramo vedenja z dodelitvijo človeku podobnih lastnosti stroju. To tudi krepi [smernice za odgovorno AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) z vidika terminologije in odstranjuje izraze, ki so lahko žaljivi ali neinkluzivni v določenih kontekstih.

Želite dobiti občutek, kako delujejo izmišljotine? Pomislite na poziv, ki AI naroči, naj ustvari vsebino o neobstoječi temi (da zagotovimo, da je ne najde v podatkih za usposabljanje). Na primer – sam sem preizkusil ta poziv:

> **Poziv:** ustvari učni načrt o marsovski vojni leta 2076.
Spletno iskanje mi je pokazalo, da obstajajo izmišljeni zapisi (npr. televizijske serije ali knjige) o marsovskih vojnah – vendar nobeden ni iz leta 2076. Zdrav razum nam tudi pove, da je leto 2076 _v prihodnosti_ in zato ne more biti povezano z resničnim dogodkom.

Kaj se torej zgodi, ko ta poziv poženemo pri različnih ponudnikih LLM?

> **Odgovor 1**: OpenAI Playground (GPT-35)

![Odgovor 1](../../../translated_images/sl/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Odgovor 2**: Azure OpenAI Playground (GPT-35)

![Odgovor 2](../../../translated_images/sl/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Odgovor 3**: : Hugging Face Chat Playground (LLama-2)

![Odgovor 3](../../../translated_images/sl/04-fabrication-huggingchat.faf82a0a51278956.webp)

Kot smo pričakovali, vsak model (ali različica modela) zaradi stohastičnega vedenja in razlik v sposobnostih modela proizvaja rahlo različne odgovore. Na primer, eden cilja na občinstvo osmih razredov, medtem ko drugi predpostavlja dijaka. Vsi trije modeli pa so ustvarili odgovore, ki bi lahko prepričali neinformiranega uporabnika, da je bil dogodek resničen.

Tehnike oblikovanja pozivov, kot sta _metaprompting_ in _nastavitev temperature_, lahko do neke mere zmanjšajo izdelovanje izmišljenih vsebin s strani modela. Nove arhitekture oblikovanja pozivov prav tako brezhibno vključujejo nova orodja in tehnike v potek poziva, da ublažijo ali zmanjšajo nekaj teh učinkov.

## Študija primera: GitHub Copilot

Zaokrožimo ta razdelek s spoznavanjem, kako se oblikovanje pozivov uporablja v rešitev resničnega sveta, z ogledom ene študije primera: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot je vaš "AI pariški programer" – pretvori besedilne pozive v dokončanja kode in je integriran v vaše razvojno okolje (npr. Visual Studio Code) za brezhibno uporabniško izkušnjo. Kot je dokumentirano v seriji blogov spodaj, je najzgodnejša različica temeljila na modelu OpenAI Codex – inženirji so hitro ugotovili potrebo po dodatni prilagoditvi modela in razvoju boljših tehnik oblikovanja pozivov za izboljšanje kakovosti kode. Julija so [predstavili izboljšan AI model, ki presega Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) za še hitrejša predlogi.

Preberite prispevke zaporedoma, da sledite njihovi učni poti.

- **Maj 2023** | [GitHub Copilot vse bolje razume vašo kodo](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maj 2023** | [Notranjost GitHuba: delo z LLM-ji za GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Junij 2023** | [Kako napisati boljše pozive za GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Julij 2023** | [.. GitHub Copilot presega Codex z izboljšanim AI modelom](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Julij 2023** | [Vodnik za razvijalce o oblikovanju pozivov in LLM-jih](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **September 2023** | [Kako zgraditi aplikacijo LLM za podjetja: Lekcije iz GitHub Copilota](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Lahko pa tudi poiščete njihov [inženirski blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) za več objav, kot je [ta](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), ki prikazuje, kako so ti modeli in tehnike _uporabljeni_ za pogon rešitev v resničnem svetu.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #2.
Reinforce the concept with examples and references.

CONCEPT #2:
Prompt Design.
Illustrated with examples.
-->

## Konstrukcija poziva

Videli smo, zakaj je oblikovanje pozivov pomembno – zdaj pa razumimo, kako so pozivi _sestavljeni_, da lahko ocenimo različne tehnike za bolj učinkovit dizajn pozivov.

### Osnovni poziv

Začnimo z osnovnim pozivom: besedilni vhod, poslan modelu brez drugega konteksta. Tukaj je primer – ko pošljemo prvih nekaj besed ameriške himne na OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), ta takoj _dopolni_ odgovor z naslednjimi vrsticami, kar prikazuje osnovno vedenje napovedi.

| Poziv (Vhod)       | Dopolnilo (Izhod)                                                                                                                           |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Zdi se, da začenjate z besedilom "The Star-Spangled Banner," nacionalne himne Združenih držav. Celotne besedilo so ...                     |

### Kompleksni poziv

Zdaj dodajmo kontekst in navodila k temu osnovnemu pozivu. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) nam omogoča, da sestavimo kompleksni poziv kot zbirko _sporočil_ z:

- pari vhod/izhod, ki odražajo _uporabnikov_ vhod in _pomočnikove_ odgovore.
- sistemsko sporočilo, ki določa kontekst za vedenje ali osebnost pomočnika.

Zahteva je zdaj v spodnji obliki, kjer _tokenizacija_ učinkovito zajame ustrezne informacije iz konteksta in pogovora. Zdaj je spreminjanje sistemskega konteksta lahko enako vplivno na kakovost dopolnitev kot vhodni podatki, ki jih posreduje uporabnik.

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

### Navodilo poziva

V zgornjih primerih je bil uporabniški poziv preprost besedilni poizvedba, ki jo lahko interpretiramo kot zahtevo po informacijah. Z _navodilnimi_ pozivi lahko to besedilo uporabimo za natančnejšo določitev naloge in zagotovimo boljše usmerjanje AI. Tukaj je primer:

| Poziv (Vhod)                                                                                                                                                                                                                         | Dopolnilo (Izhod)                                                                                                        | Vrsta navodila      |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Napiši opis državljanske vojne                                                                                                                                                                                                     | _vrnila preprost odstavek_                                                                                               | Preprosto           |
| Napiši opis državljanske vojne. Navedite ključne datume in dogodke ter opišite njihov pomen                                                                                                                                         | _vrnila odstavek, ki mu sledi seznam ključnih datumov dogodkov z opisi_                                                  | Kompleksno          |
| Napiši opis državljanske vojne v 1 odstavku. Navedite 3 ključne točke s pomembnimi datumi in njihovim pomenom. Navedite še 3 točke s pomembnimi zgodovinskimi osebami in njihovimi prispevki. Izhod vrni kot JSON datoteko          | _vrne bolj obširne podrobnosti v besedilnem polju, formatiranem kot JSON, ki ga lahko prekopirate v datoteko in po potrebi preverite_ | Kompleksno. Formatirano. |

## Primarna vsebina

V zgornjih primerih je bil poziv še vedno precej odprt, kar je modelu omogočilo, da sam odloči, kateri del njegovega predhodno usposobljenega niz podatkov je relevanten. Pri vzorcu oblikovanja _primarne vsebine_ je vhodno besedilo razdeljeno na dva dela:

- navodilo (dejanje)
- relevantna vsebina (ki vpliva na dejanje)

Tukaj je primer, kjer je navodilo "povzemi to v 2 stavkih".

| Poziv (Vhod)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Dopolnilo (Izhod)                                                                                                                                                                                                                                                                              |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter je peti planet od Sonca in največji v Osončju. Je plinski velikan z maso tisočinko mase Sonca, a z dvakrat in pol večjo maso kot vsi drugi planeti Osončja skupaj. Jupiter je eden najsvetlejših objektov, ki so vidni s prostim očesom ponoči, poznan pa je bil starodavnim civilizacijam že pred zapisano zgodovino. Imenovan je po rimskem bogu Jupiterju.[19] Ko ga gledamo z Zemlje, je Jupiter lahko dovolj svetel, da njegova odbita svetloba meče vidne sence,[20] in je povprečno tretji najsvetlejši naravni objekt na nočnem nebu za Luno in Venero. <br/> **Povzemite to v 2 kratkih stavkih**                   | Jupiter, peti planet od Sonca, je največji v Osončju in znan kot eden najsvetlejših predmetov na nočnem nebu. Imenovan po rimskem bogu Jupiterju, je plinski velikan, katerega masa je dvakrat in pol večja od mase vseh drugih planetov Osončja skupaj. |

Segment primarne vsebine je mogoče uporabiti na različne načine za učinkovitejša navodila:

- **Primeri** – namesto da modelu eksplicitno povemo, kaj naj naredi z navodilom, mu damo primere, kaj naj naredi, in naj vzorec sam sklepa.
- **Namigi** – za navodilom sledi "namig", ki vpliva na dokončanje in usmerja model k bolj ustreznim odgovorom.
- **Predloge** – ponovljivi "recepti" za pozive z rezerviranimi mesti (spremenljivkami), ki jih lahko prilagodimo z podatki za posebne primere uporabe.

Raziskujmo to v praksi.

### Uporaba primerov

To je pristop, kjer primarno vsebino uporabimo, da model "nasitimo" z nekaj primeri želenega izhoda za dano nalogo in mu pustimo, da sklepa vzorec željenega izhoda. Glede na število predloženih primerov lahko uporabljamo zero-shot, one-shot, few-shot prompting itd.

Poziv sedaj vsebuje tri sestavine:

- opis naloge
- nekaj primerov želenega izhoda
- začetek novega primera (ki postane implicitni opis naloge)

| Tip učenja   | Poziv (Vhod)                                                                                                                                        | Dopolnilo (Izhod)          |
| :----------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot    | "Sonce sije". Prevedi v španščino                                                                                                                 | "El Sol está brillando".    |
| One-shot     | "Sonce sije" => "El Sol está brillando". <br> "Dan je mrzel in vetroven" =>                                                                        | "Es un día frío y ventoso". |
| Few-shot     | Igralec je pretekel bazo => Baseball <br/> Igralec je zadel as => Tennis <br/> Igralec je zadel šestico => Cricket <br/> Igralec je naredil slam-dunk => | Košarka                    |
|              |                                                                                                                                                     |                            |

Opazite, da smo pri zero-shot prompting morali eksplicitno navesti navodilo ("Prevedi v španščino"), vendar se navodilo izpelje pri one-shot prompting primeru. Primer few-shot pokaže, kako dodajanje več primerov omogoča modelom natančnejše sklepe brez dodatnih navodil.

### Namigi pri pozivu

Druga tehnika uporabe primarne vsebine je, da namesto primerov zagotovimo _namige_. V tem primeru modelu damo rahlo spodbudo s fragmentom, ki odraža želeni format odgovora. Model nato "zgrabi namig" in nadaljuje v tem slogu.

| Število namigov | Poziv (Vhod)                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Dopolnilo (Izhod)                                                                                                                                                                                                                                                                                    |
| :-------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0               | Jupiter je peti planet od Sonca in največji v Osončju. Je plinski velikan z maso tisočinko mase Sonca, a z dvakrat in pol večjo maso kot vsi drugi planeti Osončja skupaj. Jupiter je eden najsvetlejših objektov, ki so vidni s prostim očesom ponoči, poznan pa je bil starodavnim civilizacijam že pred zapisano zgodovino. <br/>**Povzemite to**                                       | Jupiter je največji planet v našem Osončju in peti po vrsti od Sonca. Je plinski velikan z maso 1/1000 mase Sonca, vendar je težji od vseh ostalih planetov skupaj. Starodavne civilizacije poznajo Jupiter že dolgo časa in je lahko viden na nočnem nebu. |
| 1              | Jupiter je peta planeta od Sonca in največja v Osončju. To je plinski velikan z maso, ki je tisočinka mase Sonca, a dva in pol krat večja od mase vseh ostalih planetov v Osončju skupaj. Jupiter je eden najsvetlejših objektov, ki so vidni s prostim očesom na nočnem nebu, poznan pa je bil starodavnim civilizacijam že pred začetkom zapisane zgodovine. <br/>**Povzemite to** <br/> Kar smo se naučili, je, da je Jupiter | peta planeta od Sonca in največja v Osončju. To je plinski velikan z maso, ki je tisočinka mase Sonca, a dva in pol krat večja od mase vseh ostalih planetov skupaj. Je lahko viden s prostim očesom in je poznan že od antičnih časov.                        |
| 2              | Jupiter je peta planeta od Sonca in največja v Osončju. To je plinski velikan z maso, ki je tisočinka mase Sonca, a dva in pol krat večja od mase vseh ostalih planetov v Osončju skupaj. Jupiter je eden najsvetlejših objektov, ki so vidni s prostim očesom na nočnem nebu, poznan pa je bil starodavnim civilizacijam že pred začetkom zapisane zgodovine. <br/>**Povzemite to** <br/> Tri največje dejstva, ki smo jih izvedeli:         | 1. Jupiter je peta planeta od Sonca in največja v Osončju. <br/> 2. To je plinski velikan z maso, ki je tisočinka mase Sonca...<br/> 3. Jupiter je s prostim očesom viden že od antičnih časov ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Predloge pozivov

Predloga poziva je _vnaprej določena receptura za poziv_, ki jo je mogoče shraniti in po potrebi znova uporabiti, da se zagotovi bolj enotna uporabniška izkušnja na obsegu. V najpreprostejši obliki je to zbirka primerov pozivov, kot je [ta od OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst), ki ponuja interaktivne komponente poziva (uporabniška in sistemska sporočila) in format zahteve, ki ga poganja API – za podporo ponovni uporabi.

V bolj kompleksni obliki, kot je [ta primer od LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), vsebuje _zaznamke_, ki jih lahko dinamično nadomestimo z podatki iz različnih virov (uporabniški vnos, sistemski kontekst, zunanji podatkovni viri itd.). To nam omogoča ustvarjanje knjižnice znova uporabnih pozivov, ki jih lahko **programsko** uporabimo za dosledne uporabniške izkušnje na obsegu.

Končno resnična vrednost predlog je v njihovi sposobnosti ustvarjanja in objavljanja _knjižnic pozivov_ za vertikalna področja uporabe – kjer je predloga poziva _optimizirana_ tako, da odraža kontekst in primere, specifične za aplikacijo, kar odgovore naredi bolj relevantne in natančne za ciljno uporabniško publiko. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) je odličen primer tega pristopa, saj kurira knjižnico pozivov za izobraževalno področje s poudarkom na ključnih ciljih, kot so načrtovanje učnih ur, oblikovanje kurikuluma, podpora študentom itd.

## Podporna vsebina

Če razmišljamo o konstrukciji poziva kot o navodilu (nalogi) in cilju (primarni vsebini), potem je _sekundarna vsebina_ kot dodatni kontekst, ki ga zagotovimo za **vplivanje na izhod na določen način**. To so lahko parametri za nastavljanje, navodila za formatiranje, taksonomije tem itd., ki modelu pomagajo _prilagoditi_ odziv tako, da bolje ustreza željencim uporabniškim ciljem ali pričakovanjem.

Na primer: Na voljo imamo katalog tečajev z obsežnimi metapodatki (ime, opis, raven, oznake, predavatelj itd.) za vse tečaje v kurikulumu:

- lahko določimo navodilo, da "povzamemo katalog tečajev za jesen 2023"
- lahko uporabimo primarno vsebino za podajanje nekaj primerov želenega izhoda
- lahko uporabimo sekundarno vsebino, da identificiramo top 5 "oznak" zanimanja.

Zdaj lahko model pripravi povzetek v formatu, ki ga prikazujejo primeri – če ima izhod več oznak, pa lahko prednostno obravnava pet določenih v sekundarni vsebini.

---

<!--
ŠABLONA ZA UČNI NAČRT:
Ta enota naj pokrije osnovni koncept #1.
Poudari koncept z zgledi in referencami.

KONCEPT #3:
Tehnike za izdelavo pozivov.
Kakšne so osnovne tehnike izdelave pozivov?
Prikaži jih z nekaj vajami.
-->

## Najboljše prakse za izdelavo pozivov

Zdaj ko vemo, kako lahko pozive _sestavimo_, lahko začnemo razmišljati, kako jih _zasnovati_, da odražajo najboljše prakse. O tem lahko razmišljamo v dveh delih – imeti pravi _nagrado_ in uporabiti pravilne _tehnike_.

### Miselnost pri izdelavi pozivov

Izdelava pozivov je proces poskusov in napak, zato imejte v mislih tri široke smernice:

1. **Razumevanje domene šteje.** Natančnost in relevantnost odzivov sta funkciji _domena_, kjer aplikacija ali uporabnik deluje. Uporabite intuicijo in strokovno znanje domene, da **nadalje prilagodite tehnike**. Na primer, določite _osebnosti specifične za domeno_ v sistemskih pozivih ali uporabite _predloge specifične za domeno_ v uporabniških pozivih. Zagotovite sekundarno vsebino, ki odraža kontekst domene, ali uporabite _namige in primere specifične za domeno_, da usmerite model k znanim vzorcem uporabe.

2. **Razumevanje modela šteje.** Vemo, da so modeli po naravi stohastični. Implementacije modelov se lahko razlikujejo glede na uporabljene podatkovne nize za učenje (predhodno usposobljeno znanje), zmožnosti (npr. preko API-ja ali SDK) in vrsto vsebine, za katero so optimizirani (koda, slike, besedilo). Razumite prednosti in omejitve modela, ki ga uporabljate, in uporabite to znanje za _prioritizacijo nalog_ ali izdelavo _prilagojenih predlog_, ki so optimizirane za zmožnosti modela.

3. **Ponavljanje in potrjevanje šteje.** Modeli se hitro razvijajo, prav tako tehnike izdelave pozivov. Kot strokovnjak za domeno lahko imate dodaten kontekst ali kriterije za _vašo_ aplikacijo, ki morda niso relevantni za širšo skupnost. Uporabite orodja in tehnike proizvodnje pozivov, da "hitro začnete" z izdelavo poziva, nato ponavljajte in potrjujte rezultate z lastno intuicijo in strokovnim znanjem. Zabeležite svoja spoznanja in naredite **bazo znanja** (npr. knjižnice pozivov), ki jo lahko drugi uporabijo kot novo izhodišče za hitrejše iteracije.

## Najboljše prakse

Oglejmo si skupne najboljše prakse, ki jih priporočajo praktiki pri [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) in [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Kaj                               | Zakaj                                                                                                                                                                                                                                           |
| :-------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Oceni najnovejše modele.           | Nove generacije modelov verjetno prinašajo izboljšane funkcije in kvaliteto – lahko pa povzročijo tudi višje stroške. Ocenite njihov vpliv in sprejmite odločitve o migraciji.                                                                    |
| Loči navodila in kontekst          | Preveri, ali tvoj model oziroma ponudnik definira _mejnike_ za jasnejšo ločitev navodil, primarne in sekundarne vsebine. To lahko modelom pomaga natančneje dodeliti uteži posameznim tokenom.                                                    |
| Bodi specifičen in jasen           | Podaj več podrobnosti o želenem kontekstu, izidu, dolžini, formatu, slogu ipd. To bo izboljšalo tako kakovost kot doslednost odgovorov. Zabeleži recepte v znova uporabnih predlogah.                                                           |
| Bodi opisni, uporabi primere       | Modeli se lahko bolje odzovejo na "pokaži in povej" pristop. Začni z `zero-shot` (brez primerov) in nato poskusi `few-shot` (z nekaj primeri želenega izhoda) za izpopolnitev. Uporabi analogije.                                                    |
| Uporabi namige za zagon odgovorov | Spodbudi model proti želenemu izidu s podajanjem začetnih besed ali fraz, ki jih lahko uporabi kot izhodišče odziva.                                                                                                                          |
| Dvojno preverjanje                 | Včasih je treba modelu nekajkrat ponoviti. Daj navodila pred in po primarni vsebini, uporabi navodilo in namig ipd. Ponavljaj in preverjaj, da vidiš, kaj deluje.                                                                                |
| Redosled je pomemben              | Zaporedje podajanja informacij modelu lahko vpliva na izhod, tudi v učnih primerih, zaradi pristranskosti na sveže informacije. Preizkusi različne možnosti, da vidiš, kaj najbolje deluje.                                                        |
| Modelu daj "izhodno pot"          | Daj modelu _alternativni_ odziv, ki ga lahko ponudi, če iz kakršnegakoli razloga ne more dokončati naloge. To zmanjša možnost, da model ustvari napačne ali izmišljene odgovore.                                                              |
|                                  |                                                                                                                                                                                                                                                |

Kot pri vsaki praksi imej v mislih, da se _tvoja izkušnja lahko razlikuje_ glede na model, nalogo in domeno. Uporabi jih kot izhodišče in ponavljaj, da najdeš, kar najbolje ustreza tebi. Nenehno ponovno ocenjuj svoj proces izdelave pozivov z novimi modeli in orodji z osredotočenostjo na razširljivost procesa in kakovost odgovorov.

<!--
ŠABLONA ZA UČNI NAČRT:
Ta enota naj vključuje izziv s kodo, če je to ustrezno.

IZZIV:
Povezava do Jupyter zvezka, kjer so v navodilih samo komentarji, kode pa niso izpolnjene.

REŠITEV:
Povezava do kopije tega zvezka z izpolnjenimi pozivi in pognanim primerom.
-->

## Naloga

Čestitke! Prišli ste do konca lekcije! Čas je, da nekaj teh konceptov in tehnik preizkusite na resničnih primerih!

Za našo nalogo bomo uporabili Jupyter Notebook z vajami, ki jih lahko izvedete interaktivno. Prav tako lahko razširite zvezek z lastnimi Markdown in kodo, da samostojno raziskujete ideje in tehnike.

### Za začetek, naredi fork repozitorija, nato

- (Priporočeno) Zaženi GitHub Codespaces
- (Alternativno) Kloniraj repozitorij na lokalno napravo in ga uporabi z Docker Desktopom
- (Alternativno) Odpri Notebook v želenem okolju za izvajanje zvezkov.

### Nato nastavi spremenljivke okolja

- Skopiraj datoteko `.env.copy` iz korena repozitorija v `.env` in izpolni vrednosti `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` in `AZURE_OPENAI_DEPLOYMENT`. Nato se vrni na [razdelek Učilni peskovnik](#učilnica-za-učenje) za navodila.

### Nato odpri Jupyter Notebook

- Izberi razpoložljiv jedro runtime. Če uporabljaš možnosti 1 ali 2, izberi privzeto Python 3.10.x jedro, ki ga zagotavlja razvojno okolje v vsebniku.

Pripravljen si za izvajanje vaj. Pomembno je vedeti, da ni pravih ali napačnih odgovorov – gre za raziskovanje možnosti z metodo poskusov in napak ter razvoj intuicije, kaj deluje za določen model in domeno aplikacije.

_Zaradi tega v tej lekciji ni segmentov z rešitvami kode. Namesto tega bodo v notebooku celice Markdown z naslovom "Moja rešitev:", ki prikazujejo en primer izhoda kot referenco._

 <!--
ŠABLONA ZA UČNI NAČRT:
Zaključi razdelek s povzetkom in viri za samostojno učenje.
-->

## Preverjanje znanja

Kateri od naslednjih pozivov je dober in sledi razumni najboljši praksi?

1. Pokaži mi sliko rdečega avtomobila
2. Pokaži mi sliko rdečega avtomobila znamke Volvo in modela XC90, parkiranega ob pečini s sončnim zahodom
3. Pokaži mi sliko rdečega avtomobila znamke Volvo in modela XC90

O: 2, je najboljši poziv, ker poda podrobnosti o "čem" in gre v specifičnosti (ne samo katerikoli avto, ampak določena znamka in model) ter opisuje celoten prizor. 3 je naslednji po kakovosti, saj tudi vsebuje veliko opisov.

## 🚀 Izziv

Preizkusi tehniko "namiga" z pozivom: Dokončaj stavek "Pokaži mi sliko rdečega avtomobila znamke Volvo in ". Kako odgovori in kako bi to izboljšal?

## Odlično delo! Nadaljuj z učenjem

Želiš izvedeti več o različnih konceptih izdelave pozivov? Obišči [stran za nadaljnje učenje](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) in poišči druge odlične vire na to temo.

Pojdi na Lekcijo 5, kjer bomo spoznali [napredne tehnike pozivanja](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->