<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-05-19T23:16:50+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "sl"
}
-->
# Zavarovanje vaših generativnih AI aplikacij

## Uvod

Ta lekcija bo obravnavala:

- Varnost v kontekstu AI sistemov.
- Pogoste nevarnosti in grožnje AI sistemom.
- Metode in premisleki za zavarovanje AI sistemov.

## Cilji učenja

Po zaključku te lekcije boste razumeli:

- Grožnje in nevarnosti AI sistemom.
- Pogoste metode in prakse za zavarovanje AI sistemov.
- Kako lahko izvajanje varnostnih testov prepreči nepričakovane rezultate in izgubo zaupanja uporabnikov.

## Kaj pomeni varnost v kontekstu generativne AI?

Ker tehnologije umetne inteligence (AI) in strojnega učenja (ML) vse bolj oblikujejo naše življenje, je ključno zaščititi ne le podatke strank, temveč tudi same AI sisteme. AI/ML se vse pogosteje uporabljajo za podporo procesov odločanja z visoko vrednostjo v industrijah, kjer lahko napačna odločitev privede do resnih posledic.

Tukaj so ključne točke, ki jih je treba upoštevati:

- **Vpliv AI/ML**: AI/ML imata velik vpliv na vsakdanje življenje, zato je njihovo varovanje postalo nujno.
- **Izzivi varnosti**: Ta vpliv AI/ML zahteva ustrezno pozornost, da se zaščitijo AI proizvodi pred sofisticiranimi napadi, bodisi s strani trolov ali organiziranih skupin.
- **Strateški problemi**: Tehnološka industrija mora proaktivno reševati strateške izzive za zagotavljanje dolgoročne varnosti strank in podatkov.

Poleg tega modeli strojnega učenja večinoma ne morejo razlikovati med zlonamernimi vnosi in benignimi anomalnimi podatki. Pomemben vir učnih podatkov izhaja iz neurejenih, nemoderiranih javnih zbirk podatkov, ki so odprte za prispevke tretjih oseb. Napadalcem ni treba kompromitirati zbirk podatkov, če lahko svobodno prispevajo vanje. Sčasoma nizko zaupni zlonamerni podatki postanejo visoko zaupni zaupanja vredni podatki, če ostane struktura/formatiranje podatkov pravilno.

Zato je ključno zagotoviti celovitost in zaščito podatkovnih skladišč, ki jih vaši modeli uporabljajo za sprejemanje odločitev.

## Razumevanje groženj in tveganj AI

V smislu AI in povezanih sistemov je zastrupitev podatkov danes najbolj pomembna varnostna grožnja. Zastrupitev podatkov je, ko nekdo namerno spremeni informacije, uporabljene za učenje AI, kar povzroči napake. To je posledica pomanjkanja standardiziranih metod za zaznavanje in ublažitev, skupaj z našim zanašanjem na nezanesljive ali neurejene javne zbirke podatkov za učenje. Za ohranjanje celovitosti podatkov in preprečevanje pomanjkljivega učnega procesa je ključno slediti izvoru in izvoru vaših podatkov. V nasprotnem primeru velja star pregovor "smeti noter, smeti ven", kar vodi do kompromitiranega delovanja modela.

Tukaj so primeri, kako lahko zastrupitev podatkov vpliva na vaše modele:

1. **Obrat oznak**: Pri nalogi binarne klasifikacije nasprotnik namerno obrne oznake majhnega dela učnih podatkov. Na primer, benigne vzorce označi kot zlonamerne, kar vodi do napačnih povezav modela.\
   **Primer**: Filter za neželeno pošto napačno označi legitimna e-poštna sporočila kot neželeno pošto zaradi manipuliranih oznak.
2. **Zastrupitev značilnosti**: Napadalec subtilno spremeni značilnosti v učnih podatkih, da uvede pristranskost ali zavede model.\
   **Primer**: Dodajanje nepomembnih ključnih besed opisom izdelkov za manipulacijo priporočilnih sistemov.
3. **Vbrizgavanje podatkov**: Vbrizgavanje zlonamernih podatkov v učni set za vplivanje na vedenje modela.\
   **Primer**: Uvedba lažnih uporabniških mnenj za izkrivljanje rezultatov analize sentimenta.
4. **Napadi z zadnjimi vrati**: Nasprotnik vstavi skrit vzorec (zadnja vrata) v učne podatke. Model se nauči prepoznati ta vzorec in se ob sprožitvi obnaša zlonamerno.\
   **Primer**: Sistem za prepoznavanje obrazov, naučen z zadnjimi vrati, ki napačno identificira določeno osebo.

MITRE Corporation je ustvarila [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), bazo znanja o taktikah in tehnikah, ki jih nasprotniki uporabljajo v resničnih napadih na AI sisteme.

> V AI sistemih se pojavlja vedno več ranljivosti, saj vključitev AI povečuje površino napada obstoječih sistemov preko tistih tradicionalnih kibernetskih napadov. ATLAS smo razvili za ozaveščanje o teh edinstvenih in spreminjajočih se ranljivostih, saj globalna skupnost vse bolj vključuje AI v različne sisteme. ATLAS je zasnovan po MITRE ATT&CK® okvirju in njegove taktike, tehnike ter postopki (TTP) dopolnjujejo tiste v ATT&CK.

Podobno kot MITRE ATT&CK® okvir, ki se obširno uporablja v tradicionalni kibernetski varnosti za načrtovanje scenarijev emulacije naprednih groženj, ATLAS zagotavlja enostavno iskalni nabor TTP, ki lahko pomaga bolje razumeti in se pripraviti na obrambo pred nastajajočimi napadi.

Poleg tega je projekt Open Web Application Security (OWASP) ustvaril "[Top 10 seznam](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" najbolj kritičnih ranljivosti, ki jih najdemo v aplikacijah, ki uporabljajo LLM. Seznam poudarja tveganja groženj, kot je omenjena zastrupitev podatkov, skupaj z drugimi, kot so:

- **Vbrizgavanje pozivov**: tehnika, kjer napadalci manipulirajo Veliki Jezikovni Model (LLM) skozi skrbno oblikovane vnose, kar povzroči, da se obnaša zunaj svoje predvidene funkcije.
- **Ranljivosti v dobavni verigi**: Komponente in programska oprema, ki sestavljajo aplikacije, ki jih uporablja LLM, kot so Python moduli ali zunanji podatkovni nizi, lahko same postanejo kompromitirane, kar vodi do nepričakovanih rezultatov, uvedenih pristranskosti in celo ranljivosti v osnovni infrastrukturi.
- **Prekomerna zanašanje**: LLM so zmotljivi in so nagnjeni k halucinacijam, kar povzroča netočne ali nevarne rezultate. V več dokumentiranih okoliščinah so ljudje sprejeli rezultate kot resnične, kar je privedlo do nenamernih negativnih posledic v resničnem svetu.

Microsoftov oblačni zagovornik Rod Trent je napisal brezplačno e-knjigo, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), ki se podrobno ukvarja s temi in drugimi nastajajočimi AI grožnjami ter ponuja obsežna navodila o tem, kako najbolje obravnavati te scenarije.

## Varnostno testiranje za AI sisteme in LLM

Umetna inteligenca (AI) spreminja različna področja in industrije ter ponuja nove možnosti in koristi za družbo. Vendar pa AI prinaša tudi pomembne izzive in tveganja, kot so zasebnost podatkov, pristranskost, pomanjkanje razložljivosti in potencialna zloraba. Zato je ključno zagotoviti, da so AI sistemi varni in odgovorni, kar pomeni, da upoštevajo etične in pravne standarde ter jim lahko zaupajo uporabniki in deležniki.

Varnostno testiranje je proces ocenjevanja varnosti AI sistema ali LLM, s prepoznavanjem in izkoriščanjem njihovih ranljivosti. To lahko izvajajo razvijalci, uporabniki ali tretji revizorji, odvisno od namena in obsega testiranja. Nekatere najpogostejše metode varnostnega testiranja za AI sisteme in LLM so:

- **Sanitizacija podatkov**: To je proces odstranjevanja ali anonimizacije občutljivih ali zasebnih informacij iz učnih podatkov ali vnosa AI sistema ali LLM. Sanitizacija podatkov lahko pomaga preprečiti uhajanje podatkov in zlonamerno manipulacijo z zmanjšanjem izpostavljenosti zaupnih ali osebnih podatkov.
- **Adversarialno testiranje**: To je proces generiranja in uporabe nasprotujočih si primerov na vhodu ali izhodu AI sistema ali LLM za oceno njegove odpornosti proti napadom nasprotnikov. Adversarialno testiranje lahko pomaga prepoznati in ublažiti ranljivosti in slabosti AI sistema ali LLM, ki jih lahko izkoristijo napadalci.
- **Verifikacija modela**: To je proces preverjanja pravilnosti in celovitosti parametrov modela ali arhitekture AI sistema ali LLM. Verifikacija modela lahko pomaga zaznati in preprečiti krajo modela z zagotavljanjem, da je model zaščiten in overjen.
- **Validacija izhoda**: To je proces validacije kakovosti in zanesljivosti izhoda AI sistema ali LLM. Validacija izhoda lahko pomaga zaznati in popraviti zlonamerno manipulacijo z zagotavljanjem, da je izhod dosleden in natančen.

OpenAI, vodilni na področju AI sistemov, je vzpostavil vrsto _varnostnih ocen_ kot del njihove pobude za mrežo rdečih ekip, usmerjeno v testiranje izhodov AI sistemov z namenom prispevanja k varnosti AI.

> Ocene lahko segajo od preprostih testov vprašanj in odgovorov do bolj kompleksnih simulacij. Kot konkretni primeri, tukaj so vzorčne ocene, razvite s strani OpenAI za ocenjevanje vedenja AI z različnih vidikov:

#### Prepričevanje

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Kako dobro lahko AI sistem prevara drug AI sistem, da izreče skrivno besedo?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Kako dobro lahko AI sistem prepriča drug AI sistem, da donira denar?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Kako dobro lahko AI sistem vpliva na podporo političnemu predlogu drugega AI sistema?

#### Steganografija (skrito sporočanje)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Kako dobro lahko AI sistem prenese skrivna sporočila, ne da bi ga ujela drug AI sistem?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Kako dobro lahko AI sistem stisne in razstisne sporočila, da omogoči skrivanje skrivnih sporočil?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Kako dobro lahko AI sistem uskladi z drugim AI sistemom, brez neposredne komunikacije?

### Varnost AI

Nujno je, da si prizadevamo zaščititi AI sisteme pred zlonamernimi napadi, zlorabo ali nenamernimi posledicami. To vključuje korake za zagotovitev varnosti, zanesljivosti in zaupanja vrednosti AI sistemov, kot so:

- Zavarovanje podatkov in algoritmov, ki se uporabljajo za učenje in delovanje AI modelov
- Preprečevanje nepooblaščenega dostopa, manipulacije ali sabotaže AI sistemov
- Zaznavanje in ublažitev pristranskosti, diskriminacije ali etičnih vprašanj v AI sistemih
- Zagotavljanje odgovornosti, transparentnosti in razložljivosti AI odločitev in dejanj
- Usmerjanje ciljev in vrednosti AI sistemov s tistimi ljudi in družbe

Varnost AI je pomembna za zagotavljanje celovitosti, razpoložljivosti in zaupnosti AI sistemov in podatkov. Nekateri izzivi in priložnosti varnosti AI so:

- Priložnost: Vključevanje AI v strategije kibernetske varnosti, saj lahko igra ključno vlogo pri prepoznavanju groženj in izboljšanju odzivnih časov. AI lahko pomaga avtomatizirati in izboljšati zaznavanje ter ublažitev kibernetskih napadov, kot so phishing, zlonamerna programska oprema ali ransomware.
- Izziv: AI lahko tudi nasprotniki uporabljajo za izvedbo sofisticiranih napadov, kot so generiranje lažne ali zavajajoče vsebine, imitacija uporabnikov ali izkoriščanje ranljivosti v AI sistemih. Zato imajo razvijalci AI edinstveno odgovornost za oblikovanje sistemov, ki so robustni in odporni proti zlorabi.

### Zaščita podatkov

LLM lahko predstavljajo tveganje za zasebnost in varnost podatkov, ki jih uporabljajo. Na primer, LLM lahko potencialno pomnijo in razkrivajo občutljive informacije iz svojih učnih podatkov, kot so osebna imena, naslovi, gesla ali številke kreditnih kartic. Lahko jih tudi manipulirajo ali napadajo zlonamerni akterji, ki želijo izkoristiti njihove ranljivosti ali pristranskosti. Zato je pomembno biti pozoren na ta tveganja in sprejeti ustrezne ukrepe za zaščito podatkov, ki se uporabljajo z LLM. Obstaja več korakov, ki jih lahko sprejmete za zaščito podatkov, ki se uporabljajo z LLM. Ti koraki vključujejo:

- **Omejevanje količine in vrste podatkov, ki jih delijo z LLM**: Delite le podatke, ki so potrebni in relevantni za predvidene namene, ter se izogibajte deljenju kakršnih koli podatkov, ki so občutljivi, zaupni ali osebni. Uporabniki naj tudi anonimizirajo ali šifrirajo podatke, ki jih delijo z LLM, na primer z odstranjevanjem ali zakrivanjem kakršnih koli identifikacijskih informacij ali z uporabo varnih komunikacijskih kanalov.
- **Preverjanje podatkov, ki jih generirajo LLM**: Vedno preverite natančnost in kakovost izhoda, ki ga generirajo LLM, da zagotovite, da ne vsebujejo neželenih ali neprimernih informacij.
- **Poročanje in opozarjanje o kakršnih koli kršitvah podatkov ali incidentih**: Bodite pozorni na kakršne koli sumljive ali nenormalne aktivnosti ali vedenja LLM, kot je generiranje besedil, ki so nerelevantna, netočna, žaljiva ali škodljiva. To bi lahko bil pokazatelj kršitve podatkov ali varnostnega incidenta.

Varnost podatkov, upravljanje in skladnost so ključnega pomena za vsako organizacijo, ki želi izkoristiti moč podatkov in AI v okolju več oblakov. Zavarovanje in upravljanje vseh vaših podatkov je kompleksna in večplastna naloga. Potrebujete zavarovati in upravljati različne vrste podatkov (strukturirane, nestrukturirane in podatke, ki jih generira AI) na različnih lokacijah v več oblakih, ter morate upoštevati obstoječe in prihodnje predpise o varnosti podatkov, upravljanju in AI. Za zaščito vaših podatkov morate sprejeti nekatere najboljše prakse in previdnostne ukrepe, kot so:

- Uporaba oblačnih storitev ali platform, ki ponujajo funkcije za zaščito podatkov in zasebnost.
- Uporaba orodij za kakovost podatkov in validacijo za preverjanje vaših podatkov glede napak, nedoslednosti ali anomalij.
- Uporaba okvirjev za upravljanje podatkov in etiko za zagotavljanje, da se vaši podatki uporabljajo na odgovoren in transparenten način.

### Emulacija groženj iz resničnega sveta - AI rdeče ekipiranje

Emulacija groženj iz resničnega sveta je zdaj priznana kot standardna praksa pri gradnji odpornih AI sistemov z uporabo podobnih orodij, taktik, postopkov za prepoznavanje tveganj za sisteme in testiranje odziva braniteljev.

> Praksa AI rdečega ekipiranja se je razvila, da prevzame bolj razšir

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI prevajanja [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav se trudimo za natančnost, vas prosimo, da se zavedate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj se šteje za avtoritativni vir. Za ključne informacije se priporoča profesionalni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.