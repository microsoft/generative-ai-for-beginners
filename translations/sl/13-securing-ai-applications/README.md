<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2faf8ee7a0b851efa647a19788f1e5b",
  "translation_date": "2025-10-18T01:40:12+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "sl"
}
-->
# Zavarovanje vaših aplikacij generativne umetne inteligence

[![Zavarovanje vaših aplikacij generativne umetne inteligence](../../../translated_images/13-lesson-banner.14103e36b4bbf17398b64ed2b0531f6f2c6549e7f7342f797c40bcae5a11862e.sl.png)](https://youtu.be/m0vXwsx5DNg?si=TYkr936GMKz15K0L)

## Uvod

Ta lekcija bo obravnavala:

- Varnost v kontekstu sistemov umetne inteligence.
- Pogoste tveganja in grožnje za sisteme umetne inteligence.
- Metode in vidike za zavarovanje sistemov umetne inteligence.

## Cilji učenja

Po zaključku te lekcije boste razumeli:

- Grožnje in tveganja za sisteme umetne inteligence.
- Pogoste metode in prakse za zavarovanje sistemov umetne inteligence.
- Kako lahko izvajanje varnostnega testiranja prepreči nepričakovane rezultate in izgubo zaupanja uporabnikov.

## Kaj pomeni varnost v kontekstu generativne umetne inteligence?

Ker tehnologije umetne inteligence (UI) in strojnega učenja (SU) vse bolj oblikujejo naše življenje, je ključnega pomena zaščititi ne le podatke strank, temveč tudi same sisteme umetne inteligence. UI/SU se vse pogosteje uporabljata za podporo procesom odločanja z visoko vrednostjo v industrijah, kjer lahko napačna odločitev povzroči resne posledice.

Tu je nekaj ključnih točk, ki jih je treba upoštevati:

- **Vpliv UI/SU**: UI/SU imata velik vpliv na vsakdanje življenje, zato je njihovo varovanje postalo nujno.
- **Izzivi varnosti**: Zaradi tega vpliva je treba ustrezno obravnavati potrebo po zaščiti izdelkov, ki temeljijo na umetni inteligenci, pred sofisticiranimi napadi, bodisi s strani trolov ali organiziranih skupin.
- **Strateški problemi**: Tehnološka industrija mora proaktivno obravnavati strateške izzive, da zagotovi dolgoročno varnost strank in podatkov.

Poleg tega modeli strojnega učenja večinoma ne morejo razlikovati med zlonamernimi vnosi in neškodljivimi anomalnimi podatki. Pomemben vir podatkov za učenje izhaja iz neurejenih, nemoderiranih javnih zbirk podatkov, ki so odprte za prispevke tretjih oseb. Napadalcem ni treba kompromitirati zbirk podatkov, če lahko sami prispevajo k njim. Sčasoma nizko zaupni zlonamerni podatki postanejo visoko zaupni zaupanja vredni podatki, če je struktura/format podatkov pravilna.

Zato je ključnega pomena zagotoviti celovitost in zaščito podatkovnih zbirk, ki jih vaši modeli uporabljajo za sprejemanje odločitev.

## Razumevanje groženj in tveganj umetne inteligence

V kontekstu umetne inteligence in povezanih sistemov je zastrupitev podatkov danes najbolj pomembna varnostna grožnja. Zastrupitev podatkov nastane, ko nekdo namerno spremeni informacije, ki se uporabljajo za učenje umetne inteligence, kar povzroči napake v njenem delovanju. To je posledica pomanjkanja standardiziranih metod za zaznavanje in zmanjševanje tveganj, skupaj z našo odvisnostjo od nezanesljivih ali neurejenih javnih zbirk podatkov za učenje. Da bi ohranili celovitost podatkov in preprečili napačen proces učenja, je ključnega pomena slediti izvoru in poreklu vaših podatkov. V nasprotnem primeru velja star pregovor "smeti noter, smeti ven", kar vodi do kompromitirane zmogljivosti modela.

Tu je nekaj primerov, kako lahko zastrupitev podatkov vpliva na vaše modele:

1. **Obrat oznak**: Pri nalogi binarne klasifikacije napadalec namerno obrne oznake majhnega dela učnih podatkov. Na primer, neškodljivi vzorci so označeni kot zlonamerni, kar vodi do napačnih asociacij modela.\
   **Primer**: Filter za neželeno pošto napačno razvrsti legitimna e-poštna sporočila kot neželeno pošto zaradi manipuliranih oznak.
2. **Zastrupitev značilnosti**: Napadalec subtilno spremeni značilnosti v učnih podatkih, da uvede pristranskost ali zavaja model.\
   **Primer**: Dodajanje nepomembnih ključnih besed opisom izdelkov za manipulacijo sistemov priporočil.
3. **Vbrizgavanje podatkov**: Vbrizgavanje zlonamernih podatkov v učni niz za vplivanje na vedenje modela.\
   **Primer**: Uvajanje lažnih uporabniških ocen za izkrivljanje rezultatov analize sentimenta.
4. **Napadi z zadnjimi vrati**: Napadalec vstavi skriti vzorec (zadnja vrata) v učne podatke. Model se nauči prepoznati ta vzorec in se ob sprožitvi obnaša zlonamerno.\
   **Primer**: Sistem za prepoznavanje obrazov, ki je bil naučen z slikami z zadnjimi vrati, napačno identificira določeno osebo.

MITRE Corporation je ustvaril [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), zbirko znanja o taktikah in tehnikah, ki jih uporabljajo napadalci v resničnih napadih na sisteme umetne inteligence.

> Število ranljivosti v sistemih, ki uporabljajo umetno inteligenco, narašča, saj vključitev umetne inteligence povečuje površino napada obstoječih sistemov, ki presega tradicionalne kibernetske napade. ATLAS smo razvili, da bi povečali ozaveščenost o teh edinstvenih in razvijajočih se ranljivostih, saj globalna skupnost vse bolj vključuje umetno inteligenco v različne sisteme. ATLAS je zasnovan po vzoru MITRE ATT&CK® okvira, njegove taktike, tehnike in postopki (TTP) pa dopolnjujejo tiste v ATT&CK.

Podobno kot MITRE ATT&CK® okvir, ki se obsežno uporablja v tradicionalni kibernetski varnosti za načrtovanje naprednih scenarijev simulacije groženj, ATLAS ponuja enostavno iskalni nabor TTP-jev, ki lahko pomagajo bolje razumeti in se pripraviti na obrambo pred nastajajočimi napadi.

Poleg tega je Open Web Application Security Project (OWASP) ustvaril "[Top 10 seznam](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" najpomembnejših ranljivosti, ki jih najdemo v aplikacijah, ki uporabljajo LLM-je. Seznam izpostavlja tveganja groženj, kot je prej omenjena zastrupitev podatkov, skupaj z drugimi, kot so:

- **Vbrizgavanje ukazov**: tehnika, pri kateri napadalci manipulirajo z velikim jezikovnim modelom (LLM) s skrbno oblikovanimi vnosi, kar povzroči, da se obnaša zunaj svojega predvidenega vedenja.
- **Ranljivosti v dobavni verigi**: Komponente in programska oprema, ki sestavljajo aplikacije, ki jih uporablja LLM, kot so Python moduli ali zunanje zbirke podatkov, so lahko same kompromitirane, kar vodi do nepričakovanih rezultatov, uvedenih pristranskosti in celo ranljivosti v osnovni infrastrukturi.
- **Prekomerna zanašanje**: LLM-ji so zmotljivi in so nagnjeni k halucinacijam, kar vodi do netočnih ali nevarnih rezultatov. V več dokumentiranih primerih so ljudje rezultate sprejeli kot resnične, kar je privedlo do nenamernih negativnih posledic v resničnem svetu.

Microsoftov Cloud Advocate Rod Trent je napisal brezplačno e-knjigo [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), ki podrobno obravnava te in druge nastajajoče grožnje umetne inteligence ter ponuja obsežne smernice, kako se najbolje spopasti s temi scenariji.

## Varnostno testiranje za sisteme umetne inteligence in LLM-je

Umetna inteligenca (UI) spreminja različna področja in industrije ter ponuja nove možnosti in koristi za družbo. Vendar pa UI prinaša tudi pomembne izzive in tveganja, kot so zasebnost podatkov, pristranskost, pomanjkanje razložljivosti in potencialna zloraba. Zato je ključnega pomena zagotoviti, da so sistemi umetne inteligence varni in odgovorni, kar pomeni, da se držijo etičnih in pravnih standardov ter jim lahko zaupajo uporabniki in deležniki.

Varnostno testiranje je proces ocenjevanja varnosti sistema umetne inteligence ali LLM-ja, z identifikacijo in izkoriščanjem njihovih ranljivosti. To lahko izvajajo razvijalci, uporabniki ali tretji revizorji, odvisno od namena in obsega testiranja. Nekatere najpogostejše metode varnostnega testiranja za sisteme umetne inteligence in LLM-je so:

- **Sanitacija podatkov**: To je proces odstranjevanja ali anonimizacije občutljivih ali zasebnih informacij iz učnih podatkov ali vhodov sistema umetne inteligence ali LLM-ja. Sanitacija podatkov lahko pomaga preprečiti uhajanje podatkov in zlonamerno manipulacijo z zmanjšanjem izpostavljenosti zaupnih ali osebnih podatkov.
- **Adversarialno testiranje**: To je proces generiranja in uporabe primerov napadov na vhod ali izhod sistema umetne inteligence ali LLM-ja za oceno njegove robustnosti in odpornosti proti napadom. Adversarialno testiranje lahko pomaga identificirati in zmanjšati ranljivosti in šibkosti sistema umetne inteligence ali LLM-ja, ki jih lahko izkoristijo napadalci.
- **Verifikacija modela**: To je proces preverjanja pravilnosti in popolnosti parametrov ali arhitekture modela sistema umetne inteligence ali LLM-ja. Verifikacija modela lahko pomaga zaznati in preprečiti krajo modela z zagotavljanjem, da je model zaščiten in preverjen.
- **Validacija izhoda**: To je proces validacije kakovosti in zanesljivosti izhoda sistema umetne inteligence ali LLM-ja. Validacija izhoda lahko pomaga zaznati in popraviti zlonamerno manipulacijo z zagotavljanjem, da je izhod dosleden in natančen.

OpenAI, vodilni na področju sistemov umetne inteligence, je vzpostavil serijo _varnostnih ocen_ kot del svoje iniciative za mrežo rdečega timinga, ki je namenjena testiranju izhodov sistemov umetne inteligence z namenom prispevanja k varnosti umetne inteligence.

> Ocene lahko segajo od preprostih testov vprašanj in odgovorov do bolj zapletenih simulacij. Kot konkretni primeri so tukaj vzorčne ocene, ki jih je razvil OpenAI za ocenjevanje vedenja umetne inteligence z različnih vidikov:

#### Prepričevanje

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Kako dobro lahko sistem umetne inteligence prepriča drug sistem umetne inteligence, da izgovori skrivno besedo?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Kako dobro lahko sistem umetne inteligence prepriča drug sistem umetne inteligence, da donira denar?
- [Predlog za glasovanje](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Kako dobro lahko sistem umetne inteligence vpliva na podporo drugega sistema umetne inteligence za politični predlog?

#### Steganografija (skrita sporočila)

- [Steganografija](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Kako dobro lahko sistem umetne inteligence prenese skrita sporočila, ne da bi ga drugi sistem umetne inteligence odkril?
- [Kompresija besedila](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Kako dobro lahko sistem umetne inteligence stisne in razširi sporočila, da omogoči skrivanje skritih sporočil?
- [Schellingova točka](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Kako dobro lahko sistem umetne inteligence sodeluje z drugim sistemom umetne inteligence, brez neposredne komunikacije?

### Varnost umetne inteligence

Ključno je, da si prizadevamo zaščititi sisteme umetne inteligence pred zlonamernimi napadi, zlorabo ali nenamernimi posledicami. To vključuje sprejemanje ukrepov za zagotovitev varnosti, zanesljivosti in zaupanja v sisteme umetne inteligence, kot so:

- Zavarovanje podatkov in algoritmov, ki se uporabljajo za učenje in delovanje modelov umetne inteligence.
- Preprečevanje nepooblaščenega dostopa, manipulacije ali sabotaže sistemov umetne inteligence.
- Zaznavanje in zmanjševanje pristranskosti, diskriminacije ali etičnih vprašanj v sistemih umetne inteligence.
- Zagotavljanje odgovornosti, transparentnosti in razložljivosti odločitev in dejanj umetne inteligence.
- Usklajevanje ciljev in vrednot sistemov umetne inteligence s tistimi ljudi in družbe.

Varnost umetne inteligence je pomembna za zagotavljanje celovitosti, razpoložljivosti in zaupnosti sistemov umetne inteligence in podatkov. Nekateri izzivi in priložnosti varnosti umetne inteligence so:

- Priložnost: Vključitev umetne inteligence v strategije kibernetske varnosti, saj lahko igra ključno vlogo pri prepoznavanju groženj in izboljšanju odzivnih časov. Umetna inteligenca lahko pomaga avtomatizirati in izboljšati zaznavanje ter zmanjšanje kibernetskih napadov, kot so phishing, zlonamerna programska oprema ali ransomware.
- Izziv: Umetno inteligenco lahko uporabljajo tudi napadalci za izvajanje sofisticiranih napadov, kot so generiranje lažne ali zavajajoče vsebine, posnemanje uporabnikov ali izkoriščanje ranljivosti v sistemih umetne inteligence. Zato imajo razvijalci umetne inteligence edinstveno odgovornost za oblikovanje sistemov, ki so robustni in odporni proti zlorabi.

### Zaščita podatkov

LLM-ji lahko predstavljajo tveganje za zasebnost in varnost podatkov, ki jih uporabljajo. Na primer, LLM-ji lahko potencialno zapomnijo in razkrijejo občutljive informacije iz svojih učnih podatkov, kot so osebna imena, naslovi, gesla ali številke kreditnih kartic. Prav tako jih lahko manipulirajo ali napadejo zlonamerni akterji, ki želijo izkoristiti njihove ranljivosti ali pristranskosti. Zato je pomembno, da se zavedamo teh tveganj in sprejmemo ustrezne ukrepe za zaščito podatkov, ki se uporabljajo z LLM-ji. Obstaja več korakov, ki jih lahko sprejmete za zaščito podatkov, ki se uporabljajo z LLM-ji. Ti koraki vključujejo:

- **Omejevanje količine in vrste podatkov, ki jih delite z LLM-ji**: Delite le podatke, ki so potrebni in relevantni za predvidene namene, ter se izogibajte deljenju kakršnih koli podatkov, ki so občutljivi, zaupni ali osebni. Uporabniki naj tudi anonimizirajo ali šifrirajo podatke, ki jih delijo z LLM-ji, na primer z odstranjevanjem ali maskiranjem kakršnih koli identifikacijskih informacij ali z uporabo varnih komunikacijskih kanalov.
- **Preverjanje podatkov, ki jih LLM-ji generirajo**: Vedno preverite natančnost in kakovost izhoda, ki ga generirajo LLM-ji, da zagotovite, da ne vsebujejo neželenih ali neprimernih informacij.
- **Poročanje in opozarjanje na morebitne kršitve podatkov ali incidente**: Bodite pozorni na kakršne koli sumljive ali nenormalne aktivnosti ali vedenja LLM-jev, kot je generiranje besedil, ki so nerelevantna, netočna, žaljiva ali škodljiva. To bi lahko bil znak kršitve podatkov ali varnostnega incidenta.

Varnost podatkov, upravljanje in skladnost so ključni za vsako organizacijo, ki želi izkoristiti moč podatkov in umetne inteligence v večoblačnem okolju. Zavarovanje in upravljanje vseh vaših podatkov je zapleten in večplasten
Posnemanje groženj iz resničnega sveta je zdaj standardna praksa pri gradnji odpornih sistemov umetne inteligence, saj se uporabljajo podobna orodja, taktike in postopki za prepoznavanje tveganj za sisteme ter testiranje odziva branilcev.

> Praksa rdečega timinga za umetno inteligenco se je razvila v širši pomen: ne zajema le iskanja varnostnih ranljivosti, temveč vključuje tudi iskanje drugih sistemskih napak, kot je generiranje potencialno škodljive vsebine. Sistemi umetne inteligence prinašajo nova tveganja, rdeči tim pa je ključen za razumevanje teh novih tveganj, kot so vbrizgavanje ukazov in ustvarjanje vsebine brez podlage. - [Microsoft AI Red Team building future of safer AI](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

[![Navodila in viri za rdeči tim](../../../translated_images/13-AI-red-team.642ed54689d7e8a4d83bdf0635768c4fd8aa41ea539d8e3ffe17514aec4b4824.sl.png)]()

Spodaj so ključni vpogledi, ki so oblikovali Microsoftov program rdečega tima za umetno inteligenco.

1. **Širok obseg rdečega timinga za umetno inteligenco:**
   Rdeči timing za umetno inteligenco zdaj zajema tako varnostne kot odgovorne rezultate umetne inteligence (RAI). Tradicionalno se je rdeči timing osredotočal na varnostne vidike, obravnaval model kot vektor (npr. kraja osnovnega modela). Vendar pa sistemi umetne inteligence uvajajo nove varnostne ranljivosti (npr. vbrizgavanje ukazov, zastrupljanje), ki zahtevajo posebno pozornost. Poleg varnosti rdeči timing za umetno inteligenco preučuje tudi vprašanja pravičnosti (npr. stereotipiziranje) in škodljive vsebine (npr. poveličevanje nasilja). Zgodnje prepoznavanje teh težav omogoča prednostno vlaganje v obrambo.
2. **Zlonamerne in neškodljive napake:**
   Rdeči timing za umetno inteligenco upošteva napake tako z zlonamernega kot neškodljivega vidika. Na primer, pri rdečem timingu novega Binga raziskujemo ne le, kako lahko zlonamerni nasprotniki ogrozijo sistem, temveč tudi, kako lahko običajni uporabniki naletijo na problematično ali škodljivo vsebino. Za razliko od tradicionalnega rdečega timinga, ki se osredotoča predvsem na zlonamerne akterje, rdeči timing za umetno inteligenco upošteva širši spekter osebnosti in potencialnih napak.
3. **Dinamična narava sistemov umetne inteligence:**
   Aplikacije umetne inteligence se nenehno razvijajo. Pri aplikacijah velikih jezikovnih modelov se razvijalci prilagajajo spreminjajočim se zahtevam. Nenehni rdeči timing zagotavlja stalno budnost in prilagajanje spreminjajočim se tveganjem.

Rdeči timing za umetno inteligenco ni vseobsegajoč in ga je treba obravnavati kot dopolnilno gibanje k dodatnim kontrolam, kot so [kontrole dostopa na podlagi vlog (RBAC)](https://learn.microsoft.com/azure/ai-services/openai/how-to/role-based-access-control?WT.mc_id=academic-105485-koreyst) in celovite rešitve za upravljanje podatkov. Namenjen je dopolnjevanju varnostne strategije, ki se osredotoča na uporabo varnih in odgovornih rešitev umetne inteligence, ki upoštevajo zasebnost in varnost, hkrati pa si prizadevajo zmanjšati pristranskost, škodljivo vsebino in dezinformacije, ki lahko zmanjšajo zaupanje uporabnikov.

Tukaj je seznam dodatnega branja, ki vam lahko pomaga bolje razumeti, kako rdeči timing pomaga pri prepoznavanju in zmanjševanju tveganj v vaših sistemih umetne inteligence:

- [Načrtovanje rdečega timinga za velike jezikovne modele (LLM) in njihove aplikacije](https://learn.microsoft.com/azure/ai-services/openai/concepts/red-teaming?WT.mc_id=academic-105485-koreyst)
- [Kaj je mreža OpenAI Red Teaming Network?](https://openai.com/blog/red-teaming-network?WT.mc_id=academic-105485-koreyst)
- [Rdeči timing za umetno inteligenco - Ključna praksa za gradnjo varnejših in bolj odgovornih rešitev umetne inteligence](https://rodtrent.substack.com/p/ai-red-teaming?WT.mc_id=academic-105485-koreyst)
- MITRE [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), baza znanja o taktikah in tehnikah, ki jih uporabljajo nasprotniki pri resničnih napadih na sisteme umetne inteligence.

## Preverjanje znanja

Kaj bi bila dobra metoda za ohranjanje integritete podatkov in preprečevanje zlorab?

1. Uvedite močne kontrole dostopa na podlagi vlog za dostop do podatkov in upravljanje podatkov
1. Izvajajte in preverjajte označevanje podatkov, da preprečite napačno predstavljanje ali zlorabo podatkov
1. Poskrbite, da vaša infrastruktura umetne inteligence podpira filtriranje vsebine

A:1, Čeprav so vse tri priporočila odlična, bo zagotavljanje pravilnih privilegijev za dostop do podatkov uporabnikom močno pripomoglo k preprečevanju manipulacije in napačnega predstavljanja podatkov, ki jih uporabljajo LLM-ji.

## 🚀 Izziv

Preberite več o tem, kako lahko [upravljate in zaščitite občutljive informacije](https://learn.microsoft.com/training/paths/purview-protect-govern-ai/?WT.mc_id=academic-105485-koreyst) v dobi umetne inteligence.

## Odlično delo, nadaljujte z učenjem

Po zaključku te lekcije si oglejte našo [zbirko učenja o generativni umetni inteligenci](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da še naprej nadgrajujete svoje znanje o generativni umetni inteligenci!

Pojdite na lekcijo 14, kjer bomo obravnavali [življenjski cikel aplikacij generativne umetne inteligence](../14-the-generative-ai-application-lifecycle/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj se šteje za avtoritativni vir. Za ključne informacije je priporočljivo profesionalno človeško prevajanje. Ne odgovarjamo za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.