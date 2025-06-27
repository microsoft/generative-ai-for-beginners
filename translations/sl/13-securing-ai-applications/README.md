<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-06-25T21:48:48+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "sl"
}
-->
# Zavarovanje vaših generativnih AI aplikacij

## Uvod

Ta lekcija bo obravnavala:

- Varnost v kontekstu AI sistemov.
- Pogoste tveganja in grožnje AI sistemom.
- Metode in razmisleki za zavarovanje AI sistemov.

## Cilji učenja

Po zaključku te lekcije boste razumeli:

- Grožnje in tveganja za AI sisteme.
- Pogoste metode in prakse za zavarovanje AI sistemov.
- Kako lahko izvajanje varnostnega testiranja prepreči nepričakovane rezultate in erozijo zaupanja uporabnikov.

## Kaj pomeni varnost v kontekstu generativne AI?

Ker tehnologije umetne inteligence (AI) in strojnega učenja (ML) vse bolj oblikujejo naša življenja, je ključno zaščititi ne le podatke strank, ampak tudi same AI sisteme. AI/ML se vse pogosteje uporablja pri podpori odločanja v industrijah, kjer lahko napačna odločitev povzroči resne posledice.

Tukaj so ključne točke za razmislek:

- **Vpliv AI/ML**: AI/ML imata pomemben vpliv na vsakdanje življenje, zato je njihovo varovanje postalo bistveno.
- **Varnostni izzivi**: Ta vpliv AI/ML zahteva ustrezno pozornost, da se zaščiti AI izdelke pred sofisticiranimi napadi, bodisi s strani trolov ali organiziranih skupin.
- **Strateške težave**: Tehnološka industrija mora proaktivno obravnavati strateške izzive za zagotovitev dolgoročne varnosti strank in podatkov.

Poleg tega modeli strojnega učenja večinoma niso sposobni razločiti med zlonamernimi vnosi in benignimi anomalijami. Znatni del podatkov za usposabljanje izhaja iz nekuriranih, nemoderiranih javnih zbirk podatkov, ki so odprte za prispevke tretjih strani. Napadalcem ni treba ogroziti zbirk podatkov, če jih lahko prosto prispevajo. Sčasoma se nizko-zanesljivi zlonamerni podatki spremenijo v visoko-zanesljive zaupanja vredne podatke, če struktura/formatiranje podatkov ostane pravilno.

Zato je ključno zagotoviti integriteto in zaščito podatkovnih skladišč, ki jih vaši modeli uporabljajo za sprejemanje odločitev.

## Razumevanje groženj in tveganj AI

V smislu AI in povezanih sistemov je zastrupitev podatkov danes najbolj izstopajoča varnostna grožnja. Zastrupitev podatkov nastane, ko nekdo namerno spremeni informacije, uporabljene za usposabljanje AI, kar povzroči napake. To je posledica odsotnosti standardiziranih metod za zaznavanje in ublažitev, skupaj z našim zanašanjem na nezaupanja vredne ali nekurirane javne zbirke podatkov za usposabljanje. Za ohranjanje integritete podatkov in preprečitev pomanjkljivega usposabljanja je ključno slediti izvoru in rodovniku vaših podatkov. V nasprotnem primeru se uveljavlja star pregovor "smeti noter, smeti ven", kar vodi do ogroženega delovanja modela.

Tukaj so primeri, kako lahko zastrupitev podatkov vpliva na vaše modele:

1. **Obrat etiket**: Pri nalogi binarne klasifikacije nasprotnik namerno obrne etikete majhnega podsklopa podatkov za usposabljanje. Na primer, benigni vzorci so označeni kot zlonamerni, kar povzroči, da model nauči napačne povezave.\
   **Primer**: Filtriranje neželene pošte, ki napačno razvrsti legitimna e-poštna sporočila kot neželeno pošto zaradi manipuliranih etiket.
2. **Zastrupitev značilnosti**: Napadalec subtilno spremeni značilnosti v podatkih za usposabljanje, da uvede pristranskost ali zavaja model.\
   **Primer**: Dodajanje nepomembnih ključnih besed v opise izdelkov za manipulacijo priporočilnih sistemov.
3. **Vbrizgavanje podatkov**: Vbrizgavanje zlonamernih podatkov v nabor za usposabljanje za vplivanje na vedenje modela.\
   **Primer**: Uvedba lažnih uporabniških ocen za izkrivljanje rezultatov analize sentimenta.
4. **Napadi z zadnjimi vrati**: Nasprotnik vstavi skrit vzorec (zadnja vrata) v podatke za usposabljanje. Model se nauči prepoznati ta vzorec in se ob aktiviranju obnaša zlonamerno.\
   **Primer**: Sistem za prepoznavanje obrazov, usposobljen z slikami z zadnjimi vrati, ki napačno prepozna določeno osebo.

MITRE Corporation je ustvaril [ATLAS (Pokrajina groženj za umetno inteligenco)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), bazo znanja o taktiki in tehnikah, ki jih nasprotniki uporabljajo pri napadih na AI sisteme v realnem svetu.

> Narašča število ranljivosti v sistemih, ki omogočajo AI, saj vključitev AI povečuje površino napada obstoječih sistemov preko tradicionalnih kibernetskih napadov. Razvili smo ATLAS, da bi povečali ozaveščenost o teh edinstvenih in razvijajočih se ranljivostih, saj globalna skupnost vse bolj vključuje AI v različne sisteme. ATLAS je modeliran po okviru MITRE ATT&CK® in njegove taktike, tehnike in postopki (TTP) so dopolnilni tistim v ATT&CK.

Podobno kot MITRE ATT&CK® okvir, ki se obsežno uporablja v tradicionalni kibernetski varnosti za načrtovanje scenarijev napredne grožnje, ATLAS ponuja enostavno iskalne TTP-je, ki lahko pomagajo bolje razumeti in se pripraviti na obrambo pred novimi napadi.

Poleg tega je Open Web Application Security Project (OWASP) ustvaril "[Top 10 seznam](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" najbolj kritičnih ranljivosti, najdenih v aplikacijah, ki uporabljajo LLM-je. Seznam izpostavlja tveganja groženj, kot je prej omenjena zastrupitev podatkov, skupaj z drugimi, kot so:

- **Vbrizgavanje pozivov**: tehnika, pri kateri napadalci manipulirajo z Velikim Jezikovnim Modelom (LLM) preko skrbno oblikovanih vnosov, kar povzroči, da se obnaša zunaj svojega nameravanega vedenja.
- **Ranljivosti dobavne verige**: Komponente in programska oprema, ki sestavljajo aplikacije, ki jih uporablja LLM, kot so Python moduli ali zunanji nabori podatkov, lahko sami postanejo kompromitirani, kar vodi do nepričakovanih rezultatov, uvedenih pristranskosti in celo ranljivosti v osnovni infrastrukturi.
- **Pretirana zanašanje**: LLM-ji so nepopolni in so nagnjeni k halucinacijam, kar zagotavlja netočne ali nevarne rezultate. V več dokumentiranih primerih so ljudje sprejeli rezultate kot samoumevne, kar je vodilo do nenamernih negativnih posledic v resničnem svetu.

Microsoft Cloud Advocate Rod Trent je napisal brezplačno e-knjigo, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), ki se poglablja v te in druge nastajajoče AI grožnje ter ponuja obsežna navodila o tem, kako najbolje obravnavati te scenarije.

## Varnostno testiranje za AI sisteme in LLM-je

Umetna inteligenca (AI) spreminja različne domene in industrije ter ponuja nove možnosti in koristi za družbo. Vendar AI prinaša tudi pomembne izzive in tveganja, kot so zasebnost podatkov, pristranskost, pomanjkanje razložljivosti in potencialna zloraba. Zato je ključno zagotoviti, da so AI sistemi varni in odgovorni, kar pomeni, da se držijo etičnih in pravnih standardov ter jih lahko uporabniki in deležniki zaupajo.

Varnostno testiranje je proces ocenjevanja varnosti AI sistema ali LLM, s prepoznavanjem in izkoriščanjem njihovih ranljivosti. To lahko izvajajo razvijalci, uporabniki ali tretji revizorji, odvisno od namena in obsega testiranja. Nekatere najbolj pogoste metode varnostnega testiranja za AI sisteme in LLM-je so:

- **Sanitacija podatkov**: To je proces odstranjevanja ali anonimizacije občutljivih ali zasebnih informacij iz podatkov za usposabljanje ali vnosa AI sistema ali LLM. Sanitacija podatkov lahko pomaga preprečiti uhajanje podatkov in zlonamerno manipulacijo z zmanjšanjem izpostavljenosti zaupnih ali osebnih podatkov.
- **Adverzalno testiranje**: To je proces generiranja in uporabe adverzalnih primerov na vhodu ali izhodu AI sistema ali LLM za oceno njegove robustnosti in odpornosti proti adverzalnim napadom. Adverzalno testiranje lahko pomaga prepoznati in ublažiti ranljivosti in slabosti AI sistema ali LLM, ki jih lahko napadalci izkoristijo.
- **Verifikacija modela**: To je proces preverjanja pravilnosti in popolnosti parametrov modela ali arhitekture AI sistema ali LLM. Verifikacija modela lahko pomaga zaznati in preprečiti krajo modela z zagotavljanjem, da je model zaščiten in overjen.
- **Validacija izhoda**: To je proces validacije kakovosti in zanesljivosti izhoda AI sistema ali LLM. Validacija izhoda lahko pomaga zaznati in popraviti zlonamerno manipulacijo z zagotavljanjem, da je izhod dosleden in natančen.

OpenAI, vodilni na področju AI sistemov, je vzpostavil serijo _varnostnih evalvacij_ kot del svoje iniciative rdečega timinga, namenjene testiranju izhodov AI sistemov v upanju, da prispevajo k varnosti AI.

> Evalvacije lahko segajo od preprostih Q&A testov do bolj kompleksnih simulacij. Kot konkretni primeri, tukaj so vzorčne evalvacije, ki jih je razvil OpenAI za ocenjevanje vedenja AI iz več vidikov:

#### Prepričevanje

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Kako dobro lahko AI sistem pretenta drug AI sistem, da izreče skrivno besedo?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Kako dobro lahko AI sistem prepriča drug AI sistem, da donira denar?
- [Predlog za glasovanje](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Kako dobro lahko AI sistem vpliva na podporo drugega AI sistema političnemu predlogu?

#### Steganografija (skrita sporočila)

- [Steganografija](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Kako dobro lahko AI sistem ​​posreduje skrita sporočila, ne da bi ga drugi AI sistem odkril?
- [Kompresija besedila](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Kako dobro lahko AI sistem stisne in razstisne sporočila, da omogoči skrivanje skritih sporočil?
- [Schellingova točka](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Kako dobro lahko AI sistem koordinira z drugim AI sistemom, brez neposredne komunikacije?

### AI Varnost

Nujno je, da si prizadevamo zaščititi AI sisteme pred zlonamernimi napadi, zlorabo ali nenamernimi posledicami. To vključuje ukrepe za zagotavljanje varnosti, zanesljivosti in zaupanja vrednosti AI sistemov, kot so:

- Zavarovanje podatkov in algoritmov, ki se uporabljajo za usposabljanje in delovanje AI modelov
- Preprečevanje nepooblaščenega dostopa, manipulacije ali sabotaže AI sistemov
- Zaznavanje in ublažitev pristranskosti, diskriminacije ali etičnih vprašanj v AI sistemih
- Zagotavljanje odgovornosti, preglednosti in razložljivosti AI odločitev in dejanj
- Usmerjanje ciljev in vrednot AI sistemov v skladu s tistimi ljudi in družbe

AI varnost je pomembna za zagotavljanje integritete, razpoložljivosti in zaupnosti AI sistemov in podatkov. Nekateri izzivi in priložnosti AI varnosti so:

- Priložnost: Vključitev AI v strategije kibernetske varnosti, saj lahko igra ključno vlogo pri prepoznavanju groženj in izboljšanju odzivnih časov. AI lahko pomaga avtomatizirati in izboljšati zaznavanje in ublažitev kibernetskih napadov, kot so phishing, zlonamerna programska oprema ali izsiljevalski napadi.
- Izziv: AI lahko nasprotniki uporabljajo tudi za izvajanje sofisticiranih napadov, kot so generiranje lažne ali zavajajoče vsebine, oponašanje uporabnikov ali izkoriščanje ranljivosti v AI sistemih. Zato imajo AI razvijalci edinstveno odgovornost za oblikovanje sistemov, ki so robustni in odporni proti zlorabi.

### Zaščita podatkov

LLM-ji lahko predstavljajo tveganje za zasebnost in varnost podatkov, ki jih uporabljajo. Na primer, LLM-ji lahko potencialno pomnijo in uhajajo občutljive informacije iz svojih podatkov za usposabljanje, kot so osebna imena, naslovi, gesla ali številke kreditnih kartic. Prav tako jih lahko manipulirajo ali napadejo zlonamerni akterji, ki želijo izkoristiti njihove ranljivosti ali pristranskosti. Zato je pomembno, da se zavedamo teh tveganj in sprejmemo ustrezne ukrepe za zaščito podatkov, uporabljenih z LLM-ji. Obstaja več korakov, ki jih lahko sprejmete za zaščito podatkov, ki se uporabljajo z LLM-ji. Ti koraki vključujejo:

- **Omejevanje količine in vrste podatkov, ki jih delite z LLM-ji**: Delite samo podatke, ki so potrebni in relevantni za predvidene namene, ter se izogibajte deljenju kakršnih koli podatkov, ki so občutljivi, zaupni ali osebni. Uporabniki naj tudi anonimizirajo ali šifrirajo podatke, ki jih delijo z LLM-ji, na primer z odstranjevanjem ali maskiranjem kakršnih koli identifikacijskih informacij ali uporabo varnih komunikacijskih kanalov.
- **Preverjanje podatkov, ki jih generirajo LLM-ji**: Vedno preverite natančnost in kakovost izhoda, ki ga generirajo LLM-ji, da zagotovite, da ne vsebujejo nobenih neželenih ali neprimernih informacij.
- **Poročanje in opozarjanje na morebitne kršitve podatkov ali incidente**: Bodite pozorni na kakršne koli sumljive ali nenormalne dejavnosti ali vedenja LLM-jev, kot je generiranje besedil, ki so nerelevantna, netočna, žaljiva ali škodljiva. To bi lahko kazalo na kršitev podatkov ali varnostni incident.

Varnost podatkov, upravljanje in skladnost so ključni za vsako organizacijo, ki želi izkoristiti moč podatkov in AI v okolju z več oblaki. Zavarovanje in upravljanje vseh vaših podatkov je zapleteno in večplastno podjetje. Morate zavarovati in upravljati različne vrste podatkov (strukturirane, nestrukturirane in podatke, ki jih generira AI) na različnih lokacijah preko več oblakov, ter morate upoštevati obstoječe in prihodnje predpise o varnosti podatkov, upravljanju in AI. Za zaščito svojih podatkov morate sprejeti nekaj najboljših praks in previdnostnih ukrepov, kot so:

- Uporabite storitve ali platforme v oblaku, ki ponujajo funkcije zaščite podatkov in zasebnosti.
- Uporabite orodja za preverjanje kakovosti podatkov in validacijo, da preverite svoje podatke za napake, neskladnosti ali anomalije.
- Uporabite okvire za upravljanje podatkov in etiko, da zagotovite, da se vaši podatki uporabljajo na odgovoren in pregleden način.

### Emulacija

**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da se zavedate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj bo obravnavan kot avtoritativni vir. Za kritične informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne interpretacije, ki bi nastale zaradi uporabe tega prevoda.