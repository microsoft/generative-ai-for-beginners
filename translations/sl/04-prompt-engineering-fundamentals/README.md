# Osnove oblikovanja pozivov

[![Osnove oblikovanja pozivov](../../../translated_images/sl/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Uvod
Ta modul pokriva osnovne pojme in tehnike za ustvarjanje učinkovitih pozivov v generativnih modelih AI. Pomemben je tudi način, kako napišete svoj poziv za LLM. Dobro oblikovan poziv lahko doseže boljšo kakovost odgovora. Kaj pa pravzaprav pomenita izraza _poziv_ in _oblikovanje pozivov_? In kako izboljšati vhodni poziv, ki ga pošljem LLM? Na ta vprašanja bomo poskušali odgovoriti v tem in naslednjem poglavju.

_Generativna AI_ je sposobna ustvarjati novo vsebino (npr. besedilo, slike, zvok, kodo itd.) kot odziv na uporabniške zahteve. To doseže z uporabo _velikih jezikovnih modelov_ (LLM), kot je serija GPT podjetja OpenAI ("Generative Pre-trained Transformer"), ki so usposobljeni za uporabo naravnega jezika in kode.

Uporabniki lahko zdaj z modeli komunicirajo z uporabo znanih paradigm, kot je klepet, brez potrebe po kakršnemkoli tehničnem znanju ali usposabljanju. Modeli so _pozivno temelječi_ - uporabniki pošljejo besedilni vhod (poziv) in dobijo AI odgovor (dokončanje). Nato lahko iterativno "klepetajo z AI" v večkrogovnih pogovorih, izboljšujejo svoj poziv, dokler odgovor ne ustreza njihovim pričakovanjem.

"Pozivi" postanejo primarni _programski vmesnik_ za generativne AI aplikacije, saj modelom povedo, kaj naj naredijo, in vplivajo na kakovost vrnjenih odgovorov. "Oblikovanje pozivov" je hitro rastoče področje, ki se osredotoča na _načrtovanje in optimizacijo_ pozivov za zagotavljanje doslednih in kakovostnih odgovorov v obsegu.

## Cilji učenja

V tej lekciji se bomo naučili, kaj je oblikovanje pozivov, zakaj je pomembno in kako lahko ustvarimo učinkovitejše pozive za določen model in namen aplikacije. Spoznali bomo osnovne pojme in dobre prakse oblikovanja pozivov ter spoznali interaktivno okolje Jupyter zvezkov "peskovnik", kjer lahko vidimo to znanje uporabljeno na dejanskih primerih.

Do konca te lekcije bomo znali:

1. Razložiti, kaj je oblikovanje pozivov in zakaj je pomembno.
2. Opisati sestavine poziva in kako se uporabljajo.
3. Spoznati najboljše prakse in tehnike oblikovanja pozivov.
4. Uporabiti naučene tehnike na resničnih primerih z uporabo OpenAI končne točke.

## Ključni izrazi

Oblikovanje pozivov: Postopek načrtovanja in izboljševanja vhodov, ki usmerjajo AI modele k ustvarjanju želenih izhodov.
Tokenizacija: Postopek pretvarjanja besedila v manjše enote, imenovane tokeni, ki jih model lahko razume in obdela.
Modeli LLM s prilagojenimi navodili: Veliki jezikovni modeli (LLM), ki so dodatno prilagojeni z določenimi navodili za izboljšanje natančnosti in relevantnosti odgovorov.

## Okolje za učenje

Oblikovanje pozivov je trenutno bolj umetnost kot znanost. Najboljši način za izboljšanje intuicije je _več vaje_ in sprejetje pristopa poskusov in napak, ki združuje strokovno znanje domene uporabe s priporočenimi tehnikami in optimizacijami, specifičnimi za model.

Jupyter zvezek, ki spremlja to lekcijo, ponuja _peskovnik_, kjer lahko preizkusite, kar se naučite - sproti ali kot del kodnega izziva na koncu. Za izvajanje vaj boste potrebovali:

1. **Azure OpenAI API ključ** - končno točko storitve za nameščeni LLM.
2. **Python izvajalno okolje** - v katerem lahko zaženete zvezek.
3. **Lokalne okoljske spremenljivke** - _zaključite [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) korake zdaj, da boste pripravljeni_.

Zvezek vsebuje _začetne_ vaje - a spodbujamo vas, da dodate lastne _Markdown_ (opisne) in _Kode_ (pozivne zahtevke) razdelke za preizkušanje več primerov ali idej - in si tako zgradite intuicijo za oblikovanje pozivov.

## Ilustriran vodnik

Želite pred začetkom lekcije dobiti velik pregled tem, ki jih ta zajema? Oglejte si ta ilustriran vodnik, ki vam poda občutek glavnih tem in ključnih spoznanj, o katerih razmislite pri vsaki od njih. Načrt lekcije vas vodi od razumevanja osnovnih pojmov in izzivov do njihove obravnave z relevantnimi tehnikami oblikovanja pozivov in najboljšimi praksami. Upoštevajte, da se razdelek "Napredne tehnike" v tem vodniku nanaša na vsebino, zajeto v _naslednjem_ poglavju tega kurikuluma.

![Ilustriran vodnik po oblikovanju pozivov](../../../translated_images/sl/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Naš startup

Pogovorimo se zdaj, kako se _ta tema_ povezuje z našim poslanstvom startup podjetja, da [prinesemo AI inovacije v izobraževanje](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Želimo ustvarjati AI-podprte aplikacije za _personalizirano učenje_ - razmislimo torej, kako bi različni uporabniki naše aplikacije lahko "načrtovali" pozive:

- **Administratorji** lahko AI prosijo, naj _analizira podatke učnih načrtov za ugotavljanje vrzeli v pokritosti_. AI lahko povzame rezultate ali jih prikaže s kodo.
- **Učitelji** lahko AI prosijo, naj _ustvari učni načrt za ciljno skupino in temo_. AI lahko zgradi personaliziran načrt v določenem formatu.
- **Učenci** lahko AI prosijo, naj jih _poučuje v zahtevni snovi_. AI zdaj lahko vodi učence z lekcijami, namigi in primeri, prilagojenimi njihovi ravni.

To je šele vrh ledene gore. Oglejte si [Pozive za izobraževanje](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - odprtokodno knjižnico pozivov, ki jo urejajo strokovnjaki za izobraževanje - da dobite širši vpogled v možnosti! _Poskusite zagnati nekaj teh pozivov v peskovniku ali uporabite OpenAI Playground, da vidite, kaj se zgodi!_

<!--
PREDLOGA LEKCIJE:
Ta enota naj pokriva osnovni pojem #1.
Pojem okrepite s primeri in referencami.

POJEM #1:
Oblikovanje pozivov.
Opredelite in razložite, zakaj je potrebno.
-->

## Kaj je oblikovanje pozivov?

Lekcijo smo začeli z definicijo **oblikovanja pozivov** kot procesa _načrtovanja in optimizacije_ besedilnih vhodov (pozivov) za zagotavljanje doslednih in kakovostnih odgovorov (dokončanj) za določen namen aplikacije in model. Ta postopek lahko razdelimo na 2 koraka:

- _načrtovanje_ začetnega poziva za določen model in namen
- _izboljšave_ poziva iterativno, da se izboljša kakovost odgovora

Gre za proces poskusov in napak, ki zahteva uporabniško intuicijo in trud za dosego optimalnih rezultatov. Zakaj je torej pomembno? Za odgovor najprej moramo razumeti tri pojme:

- _Tokenizacija_ = kako model "vidi" poziv
- _Osnovni LLM_ = kako temeljni model "obdeluje" poziv
- _LLM s prilagojenimi navodili_ = kako model zdaj vidi "naloge"

### Tokenizacija

LLM pozive vidi kot _sekvenco tokenov_, kjer različni modeli (ali različice modela) iste pozive razdelijo na tokene različno. Ker so LLM usposobljeni na tokenih (ne na surovem besedilu), način tokenizacije pozivov neposredno vpliva na kakovost ustvarjenega odgovora.

Za intuitivno razumevanje tokenizacije preizkusite orodja, kot je [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) prikazan spodaj. Vnesite svoj poziv in opazujte, kako se pretvori v tokene, pri tem bodite pozorni na obravnavo presledkov in ločil. Upoštevajte, da ta primer prikazuje starejši LLM (GPT-3) - zato lahko uporaba novejšega modela da drugačen rezultat.

![Tokenizacija](../../../translated_images/sl/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Pojem: Temeljni modeli

Ko je poziv razdeljen na tokene, je glavna funkcija ["Osnovnega LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (temeljnega modela) napovedovanje naslednjega tokena v zaporedju. Ker so LLM trenirani na obsežnih besedilnih podatkih, razumejo statistične zveze med tokeni in lahko napovedujejo z določeno gotovostjo. Opomba: ne razumejo _pomena_ besed v pozivu ali tokenu; vidijo le vzorec, ki ga lahko "dokončajo" z naslednjo napovedjo. Napoved lahko nadaljujejo, dokler jih uporabnik ne prekine ali ne nastopi vnaprej določen pogoj.

Želite videti, kako deluje dokončanje na podlagi poziva? Vnesite zgornji poziv v [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) z privzetimi nastavitvami. Sistem obravnava pozive kot zahteve po informacijah - zato boste dobili odgovor, ki ustreza temu kontekstu.

Kaj pa, če bi uporabnik želel videti nekaj specifičnega, kar ustreza določenim kriterijem ali cilju naloge? Takrat vstopijo na sceno modeli LLM s prilagojenimi navodili.

![Dokončanje klepeta z osnovnim LLM](../../../translated_images/sl/04-playground-chat-base.65b76fcfde0caa67.webp)

### Pojem: LLM s prilagojenimi navodili

[LLM s prilagojenimi navodili](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) začne z osnovnim modelom in ga dodatno prilagodi z uporabo primerov ali vhodno/izhodnih parov (npr. večkrogovnih "sporočil"), ki vsebujejo jasna navodila - in AI skuša slediti temu navodilu.

Uporablja tehnike, kot je okrepljeno učenje z človekovim povratnim informacijam (RLHF), ki model nauči _sledenja navodilom_ in _učenja iz povratnih informacij_, da so odgovori bolje prilagojeni praktičnim aplikacijam in bolj relevantni za uporabniške cilje.

Preizkusimo to - vrnite se k zgornjemu pozivu, a spremenite _sistemsko sporočilo_ in kot kontekst dodajte naslednje navodilo:

> _Povzemite vsebino, ki vam je dana, za učenca drugega razreda. Rezultat naj bo en odstavek s 3-5 ključnimi točkami._

Vidite, kako je rezultat zdaj usklajen z željenim ciljem in formatom? Učitelj lahko ta odgovor neposredno uporabi v svojih diapozitivih za tisti razred.

![Dokončanje klepeta z LLM s prilagojenimi navodili](../../../translated_images/sl/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Zakaj potrebujemo oblikovanje pozivov?

Ko razumemo, kako LLM obdelujejo pozive, se pogovorimo, _zakaj_ potrebujemo oblikovanje pozivov. Odgovor je v tem, da trenutni LLM postavljajo več izzivov, ki otežujejo doseganje _zanesljivih in doslednih dokončanj_ brez truda pri ustvarjanju in optimizaciji pozivov. Na primer:

1. **Odgovori modela so stohastični.** _Isti poziv_ bo verjetno z različnimi modeli ali različicami modela ustvaril različne odgovore. Lahko se zgodi celo, da isti model ob različnih časih poda različne rezultate. _Tehnike oblikovanja pozivov nam lahko pomagajo zmanjšati te variacije z boljšimi varovali_.

1. **Modeli lahko izmišljajo odgovore.** Modeli so predhodno usposobljeni na _velikih, a omejenih_ naborih podatkov, zato nimajo znanja o pojmih zunaj tega obsega usposabljanja. Posledično lahko ustvarijo odgovore, ki so netočni, izmišljeni ali direktno nasprotujoči se znanim dejstvom. _Tehnike oblikovanja pozivov uporabnikom pomagajo prepoznati in blažiti takšne izmišljotine, npr. z zahtevo po navedbah virov ali razlogovanju_.

1. **Zmožnosti modelov se razlikujejo.** Novejši modeli ali generacije modelov imajo bogatejše zmogljivosti, a prinesejo tudi edinstvene posebnosti in kompromis med stroški in kompleksnostjo. _Oblikovanje pozivov nam lahko pomaga razviti najboljše prakse in delovne tokove, ki abstraktno premagujejo razlike in se prilagajajo posebnim zahtevam modelov na načine, ki so razširljivi in nemoteči_.

Poglejmo to v akciji v OpenAI ali Azure OpenAI Playground:

- Uporabite isti poziv z različnimi nameščenimi LLM (npr., OpenAI, Azure OpenAI, Hugging Face) - ste opazili razlike?
- Uporabite isti poziv večkrat z _istim_ nameščenim LLM (npr., Azure OpenAI playground) - kako so se razlikovale variacije?

### Primer izmišljotin

V tem tečaju uporabljamo izraz **"izmišljotina"**, da označimo pojav, ko LLM včasih generirajo dejansko netočne informacije zaradi omejitev usposabljanja ali drugih razlogov. Lahko ste slišali tudi izraz _"halucinacije"_ v popularnih člankih ali raziskovalnih prispevkih. Vendar močno priporočamo uporabo _"izmišljotina"_, da ne antropomorfiziramo vedenja tako, da človeku podobno lastnost pripisujemo strojno generiranemu izidu. To tudi krepi [Smernice odgovorne AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) iz vidika terminologije, saj odstranjuje izraze, ki bi lahko bili v nekaterih kontekstih žaljivi ali neinkluzivni.

Želite razumeti, kako izmišljotine delujejo? Pomislite na poziv, ki AI naroča, naj ustvari vsebino za neobstoječo temo (da zagotovimo, da ni v podatkih za usposabljanje). Na primer - preizkusil sem naslednji poziv:

> **Poziv:** ustvarite učni načrt o Marsovski vojni leta 2076.

Iskanje po spletu mi je pokazalo, da obstajajo fiktivni zapisi (npr., TV serije ali knjige) o marsovskih vojnah - a nobenih za leto 2076. Zdrava pamet nam pove, da je 2076 _v prihodnosti_ in zato ne more biti povezan z resničnim dogodkom.


Kaj se torej zgodi, ko ta poziv zaženemo z različnimi ponudniki LLM?

> **Odgovor 1**: OpenAI Playground (GPT-35)

![Odgovor 1](../../../translated_images/sl/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Odgovor 2**: Azure OpenAI Playground (GPT-35)

![Odgovor 2](../../../translated_images/sl/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Odgovor 3**: : Hugging Face Chat Playground (LLama-2)

![Odgovor 3](../../../translated_images/sl/04-fabrication-huggingchat.faf82a0a51278956.webp)

Kot je pričakovano, vsak model (ali različica modela) nekoliko drugače odgovarja zaradi stohastičnega vedenja in razlik v zmogljivostih modela. Na primer, en model cilja na občinstvo 8. razreda, medtem ko drugi predvideva dijaka srednje šole. Vsi trije modeli pa so ustvarili odgovore, ki lahko prepričajo neinformiranega uporabnika, da je dogodek resničen.

Tehnike oblikovanja poziva, kot so _metapodajanje_ in _nastavitev temperature_, lahko do neke mere zmanjšajo nastajanje lažnih vsebin s strani modela. Novi _arhitekturi_ oblikovanja pozivov tudi brezhibno vključujejo nova orodja in tehnike v potek poziva, da omilijo ali zmanjšajo nekatere od teh učinkov.

## Primer študije primera: GitHub Copilot

Zaključimo ta del s pregledom, kako se oblikovanje pozivov uporablja v rešitvah iz resničnega sveta, z ogledom enega primera študije: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot je vaš "AI partner programer" – pretvarja besedilne pozive v dokončanja kode in je integriran v vaše razvojno okolje (npr. Visual Studio Code) za neprekinjeno uporabniško izkušnjo. Kot je dokumentirano v spodnji seriji blogov, je bila najzgodnejša različica osnovana na modelu OpenAI Codex - inženirji so hitro spoznali potrebo po fino nastavitvi modela in razvoju boljših tehnik oblikovanja pozivov za izboljšanje kakovosti kode. Julija so predstavili [izboljšan AI model, ki presega Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) za še hitrejše predloge.

Berite prispevke po vrstnem redu, da sledite njihovemu učnemu potovanju.

- **maj 2023** | [GitHub Copilot izboljšuje razumevanje vaše kode](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **maj 2023** | [Notranjost GitHub: delo z LLM-ji za GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **jun 2023** | [Kako pisati boljše pozive za GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **jul 2023** | [.. GitHub Copilot presega Codex z izboljšanim AI modelom](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **jul 2023** | [Vodnik za razvijalce o oblikovanju pozivov in LLM-jih](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **sep 2023** | [Kako zgraditi aplikacijo podjetniškega LLM: Lekcije iz GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Lahko si tudi ogledate njihov [inženirski blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) za več prispevkov, kot je [ta](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), ki prikazuje, kako se ti modeli in tehnike _uporabljajo_ za pogon rešitev iz resničnega sveta.

---

<!--
PREDLOGA ZA LEKCIJO:
Ta enota naj pokriva osnovni koncept #2.
Koncept utrdite z zgledi in referencami.

KONCEPT #2:
Oblikovanje pozivov.
Ponazorjeno z zgledi.
-->

## Konstrukcija poziva

Videli smo, zakaj je oblikovanje pozivov pomembno - zdaj pa razumimo, kako so pozivi _konstruirani_, da lahko ocenimo različne tehnike za učinkovitejše oblikovanje poziva.

### Osnovni poziv

Začnimo z osnovnim pozivom: besedilnim vnosom, poslanim modelu brez drugega konteksta. Tukaj je primer - ko pošljemo prvih nekaj besed ameriške himne OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), takoj _dokonča_ odgovor z naslednjimi vrsticami, kar ponazarja osnovno napovedno vedenje.

| Poziv (vhod)      | Dokončanje (izhod)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Zdi se, da ste začeli z besedilom "The Star-Spangled Banner", ameriške nacionalne himne. Polno besedilo je ...                              |

### Kompleksni poziv

Zdaj dodajmo kontekst in navodila osnovnemu pozivu. [Chat Completion API](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) nam omogoča konstrukcijo kompleksnega poziva kot zbirko _sporočil_ z:

- Pari vhod/izhod, ki odražajo _uporabnikov_ vnos in _pomočnikov_ odgovor.
- Sistemskim sporočilom, ki nastavi kontekst za obnašanje ali osebnost asistenta.

Zahteva je sedaj v spodnji obliki, kjer _tokenizacija_ učinkovito zajema relevantne informacije iz konteksta in pogovora. Sprememba sistemskega konteksta je lahko tako vplivna na kakovost dokončanj kot podani uporabniški vnosi.

```python
response = client.responses.create(
    model="gpt-5-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Navodilo poziva

V zgornjih primerih je bil uporabniški poziv preprosto besedilno vprašanje, ki ga je mogoče interpretirati kot zahtevo po informaciji. Z _navodili_ pozivov lahko uporabimo ta tekst za podrobnejšo določitev naloge, kar AI-ju omogoči boljše usmerjanje. Tukaj je primer:

| Poziv (vhod)                                                                                                                                                                                                                         | Dokončanje (izhod)                                                                                                        | Tip navodila        |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Napiši opis Ameriške državljanske vojne                                                                                                                                                                                           | _vrne preprost odstavek_                                                                                                  | Preprosto           |
| Napiši opis Ameriške državljanske vojne. Navedi ključne datume in dogodke ter opiši njihov pomen                                                                                                                                      | _vrne odstavek, sledi pa seznam ključnih datumov dogodkov z opisi_                                                        | Kompleksno          |
| Napiši opis Ameriške državljanske vojne v 1 odstavku. Navedi 3 ključne točke z datumi in njihovim pomenom. Navedi še 3 točke o pomembnih zgodovinskih osebnostih in njihovih prispevkih. Izpis vrni kot JSON datoteko                        | _vrne bolj obsežne podrobnosti v besedilnem polju, formatirano kot JSON, ki ga lahko kopiraš in prilepiš v datoteko ter preveriš_ | Kompleksno. Formatirano. |

## Primarna vsebina

V zgornjih primerih je bil poziv še vedno precej odprt, kar je omogočalo LLM-ju, da sam odloči, kateri del njegovega vnaprej usposobljenega nabora podatkov je relevanten. Z oblikovnim vzorcem _primarna vsebina_ je besedilo vnosa razdeljeno na dve deli:

- navodilo (dejanje)
- relevantna vsebina (ki vpliva na dejanje)

Tukaj je primer, kjer je navodilo "strni to v 2 povedi".

| Poziv (vhod)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Dokončanje (izhod)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter je peti planet od Sonca in največji v Osončju. Je plinski velikan z maso eno tisočinko mase Sonca, a dvakrat in pol večjo od vseh drugih planetov Osončja skupaj. Jupiter je eden najsvetlejših predmetov, ki jih lahko vidimo z golim očesom ponoči, in je bil poznan starodavnim civilizacijam že pred zapisano zgodovino. Ime je dobil po rimskem bogu Jupiterju.[19] Ko ga opazujemo z Zemlje, je Jupiter lahko dovolj svetel, da njegova odbita svetloba meče vidne sence,[20] in je povprečno tretji najsvetlejši naravni predmet na nočnem nebu za Luno in Venero. <br/> **Strni to v 2 kratki povedi** | Jupiter, peti planet od Sonca, je največji v Osončju in je znan kot eden najsvetlejših predmetov na nočnem nebu. Poimenovan po rimskem bogu Jupiterju, je plinski velikan z maso, ki je dvakrat in pol večja od vseh drugih planetov Osončja skupaj. |

Segment primarne vsebine se lahko uporablja na različne načine za učinkovitejša navodila:

- **Primeri** - namesto da modelu izrecno povemo, kaj naj stori, mu damo primere, kaj naj stori in naj sam sklepa vzorec.
- **Namigi** - sledi navodilu "namig", ki pripravlja dokončanje in usmerja model k bolj relevantnim odgovorom.
- **Predloge** - to so ponovljive "recepture" pozivov z držali (spremenljivkami), ki jih lahko prilagodimo z podatki za posebne primere uporabe.

Raziskajmo te primere v praksi.

### Uporaba primerov

To je pristop, kjer uporabimo primarno vsebino, da modelu "nahranimo" nekaj primerov želenega izhoda za dano navodilo in mu dovolimo, da sam sklepa vzorec željenega izhoda. Glede na število danih primerov imamo zero-shot, one-shot, few-shot pozivanje itd.

Poziv zdaj sestoji iz treh komponent:

- Opisa naloge
- Nekaj primerov želenega izhoda
- Začetka novega primera (kar postane implicitni opis naloge)

| Vrsta učenja | Poziv (vhod)                                                                                                                                        | Dokončanje (izhod)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "The Sun is Shining". Prevedi v španščino                                                                                                           | "El Sol está brillando".    |
| One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot      | Igralec je tekel okoli baz => Baseball <br/> Igralec je zadel asa => Tenis <br/> Igralec je zadel šestko => Kriket <br/> Igralec je naredil zabijanje => | Košarka                    |
|               |                                                                                                                                                       |                             |

Opazite, da smo morali pri zero-shot pozivanju navesti izrecno navodilo ("Prevedi v španščino"), medtem ko je to v one-shot primeru dobljeno implicitno. Primer few-shot pokaže, kako dodajanje več primerov omogoča modelom natančnejše sklepe brez dodatnih navodil.

### Namigi pri pozivu

Druga tehnika za uporabo primarne vsebine je dajanje _namigov_ namesto primerov. V tem primeru modelu damo spodbudni _zagon_ z odlomkom, ki odraža željeni format odgovora. Model nato "sprejme namig" in nadaljuje v isti smeri.

| Število namigov | Poziv (vhod)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Dokončanje (izhod)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter je peti planet od Sonca in največji v Osončju. Je plinski velikan z maso eno tisočinko mase Sonca, a dvakrat in pol večjo od vseh drugih planetov Osončja skupaj. Jupiter je eden najsvetlejših predmetov, ki jih lahko vidimo z golim očesom ponoči, in je bil poznan starodavnim civilizacijam že pred zapisano zgodovino. <br/>**Strni to**                                       | Jupiter je največji planet v našem Osončju in peti od Sonca. Je plinski velikan z maso 1/1000 mase Sonca, vendar je težji od vseh drugih planetov skupaj. Stare civilizacije so Jupitra poznale že dolgo, in ga z lahkoto vidimo na nočnem nebu.. |
| 1              | Jupiter je peti planet od Sonca in največji v Osončju. Je plinski velikan z maso eno tisočinko mase Sonca, a dvakrat in pol večjo od vseh drugih planetov Osončja skupaj. Jupiter je eden najsvetlejših predmetov, ki jih lahko vidimo z golim očesom ponoči, in je bil poznan starodavnim civilizacijam že pred zapisano zgodovino. <br/>**Strni to** <br/> Kar smo izvedeli je, da je Jupiter | peti planet od Sonca in največji v Osončju. Je plinski velikan z maso eno tisočinko mase Sonca, a dvakrat in pol večjo od vseh drugih planetov skupaj. Je lahko viden z golim očesom in poznan že od antičnih časov.                        |

| 2              | Jupiter je peti planet od Sonca in največji v Osončju. Je plinski velikanko z maso eno tisočinko Sončeve, a dvakrat in pol večjo kot vsota vseh ostalih planetov v Osončju. Jupiter je eden najsvetlejših objektov, ki so vidni s prostim očesom ponoči na nebu, in je bil znan antičnim civilizacijam že pred zapisano zgodovino. <br/>**Povzetek** <br/> Top 3 dejstva, ki smo jih izvedeli:         | 1. Jupiter je peti planet od Sonca in največji v Osončju. <br/> 2. Je plinski velikanko z maso eno tisočinko Sončeve...<br/> 3. Jupiter je bil s prostim očesom viden že v antičnih časih ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Predloge za pozive

Predloga poziva je _vnaprej določena receptura za poziv_, ki jo je mogoče shraniti in po potrebi ponovno uporabiti, da se zagotovi bolj dosledna uporabniška izkušnja v obsegu. V najpreprostejši obliki je to preprosto zbirka primerov pozivov, kot je [ta od OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst), ki zagotavlja tako interaktivne komponente poziva (uporabniška in sistemska sporočila) kot tudi format zahteve prek API – za podporo ponovni uporabi.

V bolj zapleteni obliki, kot je [ta primer iz LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), vsebuje _rezerve_ (placeholders), ki jih je mogoče zamenjati z podatki iz različnih virov (uporabniški vnos, sistemski kontekst, zunanji viri podatkov itd.) za dinamično ustvarjanje poziva. To nam omogoča ustvarjanje knjižnice ponovnih uporabnih pozivov, ki jih je mogoče **programsko** uporabljati za zagotavljanje doslednih uporabniških izkušenj v obsegu.

Končno je prava vrednost predlog v zmožnosti ustvarjanja in objavljanja _knjižnic pozivov_ za vertikalna področja uporabe – kjer je predloga poziva zdaj _optimizirana_, da odraža kontekst ali primere, specifične za aplikacijo, zaradi česar so odgovori bolj relevantni in natančni za ciljno uporabniško publiko. Repozitorij [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) je odličen primer tega pristopa, saj ureja knjižnico pozivov za področje izobraževanja z osredotočenostjo na ključne cilje, kot so načrtovanje učnih ur, oblikovanje kurikula, študentsko tutorstvo itd.

## Podporna vsebina

Če razmišljamo o konstrukciji poziva kot navodilu (nalogi) in cilju (primarni vsebini), potem je _sekundarna vsebina_ kot dodaten kontekst, ki ga zagotovimo, da **na nek način vplivamo na izhod**. To so lahko nastavitveni parametri, navodila za oblikovanje, taksonomije tem itd., ki lahko pomagajo modelu _prilagoditi_ njegov odgovor tako, da ustreza željenim uporabniškim ciljem ali pričakovanjem.

Na primer: Glede na katalog tečajev z obsežnimi metapodatki (ime, opis, raven, oznake metapodatkov, inštruktor itd.) o vseh razpoložljivih tečajih v kurikulu:

- lahko določimo navodilo, da "povzamemo katalog tečajev za jesen 2023"
- lahko uporabimo primarno vsebino, da zagotovimo nekaj primerov želenega izhoda
- lahko uporabimo sekundarno vsebino za opredelitev top 5 "oznak" zanimanja.

Sedaj lahko model zagotovi povzetek v formatu, ki ga pokaže nekaj primerov – vendar če ima rezultat več oznak, lahko prednostno obravnava teh 5 oznak, določenih v sekundarni vsebini.

---

<!--
PREDLOGA UČNE URE:
Ta enota naj zajema osrednji koncept #1.
Okrepite koncept s primeri in referencami.

KONCEPT #3:
Tehnike za inženiring pozivov.
Katere so osnovne tehnike za inženiring pozivov?
Prikažite z nekaj vajami.
-->

## Najboljše prakse pri pozivanju

Zdaj, ko vemo, kako lahko pozive _konstruiramo_, lahko začnemo razmišljati, kako jih _zasnovati_, da odražajo najboljše prakse. Lahko razmišljamo o tem v dveh delih – imeti pravo _miselnost_ in uporabiti prave _tehnike_.

### Miselnost pri inženiringu pozivov

Inženiring pozivov je proces poskušanja in popravljanja, zato imejte v mislih tri široke vodilne dejavnike:

1. **Razumevanje domene je pomembno.** Natančnost in relevantnost odgovora sta funkciji _domena_, v kateri aplikacija ali uporabnik deluje. Uporabite svojo intuicijo in strokovno znanje domene, da **še bolj prilagodite tehnike**. Na primer, določite _osebnosti, specifične za domeno_ v svojih sistemskih pozivih ali uporabite _predloge, specifične za domeno_ v uporabniških pozivih. Zagotovite sekundarno vsebino, ki odraža kontekste, specifične za domeno, ali uporabite _namige in primere, specifične za domeno_, da usmerite model k znanim vzorcem uporabe.

2. **Razumevanje modela je pomembno.** Vemo, da so modeli po naravi stohastični. Ampak implementacije modelov se lahko razlikujejo glede na učne podatkovne nize, ki jih uporabljajo (predhodno naučeno znanje), zmogljivosti, ki jih nudijo (npr. preko API ali SDK) in tip vsebine, za katero so optimizirani (npr. koda proti slikam proti besedilu). Razumite prednosti in omejitve modela, ki ga uporabljate, in uporabite to znanje, da _prioritizirate naloge_ ali ustvarite _prilagojene predloge_, ki so optimizirane za zmogljivosti modela.

3. **Pomembna je iteracija in validacija.** Modeli se hitro razvijajo, prav tako tehnike za inženiring pozivov. Kot strokovnjak za domeno imate morda dodatne kontekste ali kriterije za _vašo_ specifično aplikacijo, ki morda ne veljajo za širšo skupnost. Uporabite orodja in tehnike inženiringa pozivov za "hitri začetek" konstrukcije poziva, nato iterirajte in validirajte rezultate s svojo intuicijo in strokovnim znanjem domene. Zabeležite svoje ugotovitve in ustvarite **bazo znanja** (npr. knjižnice pozivov), ki jo lahko drugi uporabijo kot novo izhodišče za hitrejše iteracije v prihodnosti.

## Najboljše prakse

Zdaj si ogledajmo običajne najboljše prakse, ki jih priporočajo strokovnjaki [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) in [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Kaj                              | Zakaj                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Ocenite najnovejše modele.       | Nove generacije modelov verjetno prinašajo izboljšane funkcije in kakovost – vendar lahko povzročijo višje stroške. Ocenite jih glede vpliva in se nato odločite o migraciji.                                                                          |
| Ločite navodila in kontekst      | Preverite, ali vaš model/ponudnik določa _ločila_, da bolj jasno loči navodila, primarno in sekundarno vsebino. To lahko pomaga modelom natančneje dodeliti teže nizom (tokenom).                                                                     |
| Bodite specifični in jasni       | Podajte več podrobnosti o želenem kontekstu, rezultatu, dolžini, formatu, slogu itd. To bo izboljšalo tako kakovost kot konsistentnost odgovorov. Zajamčite recepte v ponovnih uporabnih predlogah.                                                 |
| Bodite opisni, uporabite primere  | Modeli morda bolje odgovorijo na pristop "pokaži in povej". Začnite z `zero-shot` pristopom, kjer mu daste navodilo (brez primerov), nato poskusite `few-shot` kot izboljšavo, kjer zagotovite nekaj primerov želenega izhoda. Uporabite analogije.      |
| Uporabite namige za začetek dopolnitev | Spodbudite model k želenemu rezultatu tako, da mu daste nekaj uvodnih besed ali fraz, ki jih lahko uporabi kot izhodišče za odgovor.                                                                                                             |
| Ponovite                        | Včasih boste morali modele nekajkrat ponoviti. Dajte navodila pred in po primarni vsebini, uporabite navodilo in namig itd. Iterirajte in validirajte, da vidite, kaj deluje.                                                                      |
| Pomemben je vrstni red          | Vrstni red, v katerem modelu podate informacije, lahko vpliva na izhod, tudi pri učnih primerih, zaradi pristranskosti na nedavnost. Poskusite različne možnosti, da vidite, kaj najbolje deluje.                                                    |
| Dajte modelu možnost "izhoda"    | Modelu dajte _izhodni_ odgovor, ki ga lahko poda, če iz kakršnega koli razloga ne more dokončati naloge. To lahko zmanjša možnost, da model generira napačne ali izmišljene odgovore.                                                               |
|                                   |                                                                                                                                                                                                                                                   |

Kot pri vsaki najboljši praksi se spomnite, da _se lahko vaša uporabniška izkušnja razlikuje_ glede na model, nalogo in domeno. Uporabite jih kot izhodišče in iterirajte, da najdete, kaj vam najbolj ustreza. Nenehno ponovno ocenjujte svoj proces inženiringa pozivov, ko so na voljo novi modeli in orodja, s poudarkom na razširljivosti procesa in kakovosti odgovorov.

<!--
PREDLOGA UČNE URE:
Ta enota naj ponudi izziv s kodo, če je primerno

IZZIV:
Povezava do Jupyter zvezka, ki vsebuje samo komentarje v kodi v navodilih (delavnice so prazne).

REŠITEV:
Povezava do kopije tega zvezka z izpolnjenimi pozivi in zagonom, ki prikazuje, kaj bi bil lahko en primer.
-->

## Naloga

Čestitamo! Prišli ste do konca lekcije! Čas je, da nekatere koncepte in tehnike preizkusite z resničnimi primeri!

Za našo nalogo bomo uporabili Jupyter zvezek z vajami, ki jih lahko izpolnite interaktivno. Zvezek lahko tudi razširite s svojimi Markdown in Code celicami, da sami raziskujete ideje in tehnike.

### Za začetek, naredite fork repozitorija, nato

- (Priporočeno) Zaženite GitHub Codespaces
- (Alternativno) Klonirajte repozitorij na svoj lokalni računalnik in ga uporabljajte z Docker Desktop
- (Alternativno) Odprite zvezek v vašem priljubljenem okolju za zagon zvezkov.

### Nato konfigurirajte svoje okoljske spremenljivke

- Kopirajte datoteko `.env.copy` iz korena repozitorija v `.env` in izpolnite vrednosti `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` in `AZURE_OPENAI_DEPLOYMENT`. Nato se vrnite na [oddelek Learning Sandbox](#okolje-za-učenje), da izveste kako.

### Nato odprite Jupyter zvezek

- Izberite jedro za zagon. Če uporabljate možnosti 1 ali 2, preprosto izberite privzeto Python 3.10.x jedro, ki ga zagotavlja razvojni kontejner.

Pripravljeni ste za izvajanje vaj. Opozarjamo, da tukaj ni _pravih in napačnih_ odgovorov – gre za raziskovanje možnosti z metodo poskušanja in napake ter razvijanje intuicije, kaj deluje za določen model in domeno uporabe.

_Zato tukaj ni segmentov z rešitvami kode. Namesto tega bo v zvezku nekaj Markdown celic z naslovom "Moja rešitev:", ki prikazujejo en primer izhoda za referenco._

 <!--
PREDLOGA UČNE URE:
Zaključite poglavje s povzetkom in viri za samostojno učenje.
-->

## Preverjanje znanja

Kateri od naslednjih je dober poziv, ki sledi nekaterim razumnim najboljšim praksam?

1. Pokaži mi sliko rdečega avtomobila
2. Pokaži mi sliko rdečega avtomobila znamke Volvo in modela XC90 parkiranega ob pečini med sončnim zahodom
3. Pokaži mi sliko rdečega avtomobila znamke Volvo in modela XC90

Odgovor: 2, ker je najboljši poziv, saj poda podrobnosti o "čemu" in gre v specifičnosti (ne gre samo za katerikoli avto, ampak specifično znamko in model) ter opisuje celotno okolje. Najbližje temu je 3, ki prav tako vsebuje veliko opisov.

## 🚀 Izziv

Poskusite uporabiti tehniko "namiga" s pozivom: Dokončaj stavek "Pokaži mi sliko rdečega avtomobila znamke Volvo in ". Kako odgovori, in kako bi ga izboljšali?

## Odlično delo! Nadaljujte z učenjem

Želite izvedeti več o različnih konceptih inženiringa pozivov? Obiščite [stran za nadaljnje učenje](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kjer najdete druge odlične vire o tej temi.

Nato pojdite na Lekcijo 5, kjer bomo pogledali [napredne tehnike pozivanja](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->