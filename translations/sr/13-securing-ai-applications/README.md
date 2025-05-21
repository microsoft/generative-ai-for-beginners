<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-05-19T23:13:22+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "sr"
}
-->
# Obezbeđivanje vaših aplikacija za generativnu veštačku inteligenciju

## Uvod

Ova lekcija pokriva:

- Bezbednost u kontekstu AI sistema.
- Uobičajene rizike i pretnje za AI sisteme.
- Metode i razmatranja za obezbeđivanje AI sistema.

## Ciljevi učenja

Nakon završetka ove lekcije, razumećete:

- Pretnje i rizike za AI sisteme.
- Uobičajene metode i prakse za obezbeđivanje AI sistema.
- Kako sprovođenje bezbednosnih testiranja može sprečiti neočekivane rezultate i gubitak poverenja korisnika.

## Šta znači bezbednost u kontekstu generativne AI?

Kako tehnologije veštačke inteligencije (AI) i mašinskog učenja (ML) sve više oblikuju naše živote, važno je zaštititi ne samo podatke korisnika već i same AI sisteme. AI/ML se sve više koristi u podršci procesima donošenja odluka od velike vrednosti u industrijama gde pogrešna odluka može imati ozbiljne posledice.

Evo ključnih tačaka koje treba razmotriti:

- **Uticaj AI/ML**: AI/ML imaju značajan uticaj na svakodnevni život i kao takvi, njihovo obezbeđivanje postaje neophodno.
- **Izazovi u bezbednosti**: Ovaj uticaj koji AI/ML imaju zahteva odgovarajuću pažnju kako bi se zaštitili AI proizvodi od sofisticiranih napada, bilo da dolaze od trolova ili organizovanih grupa.
- **Strategijski problemi**: Tehnološka industrija mora proaktivno rešavati strateške izazove kako bi osigurala dugoročnu sigurnost korisnika i sigurnost podataka.

Dodatno, modeli mašinskog učenja u velikoj meri nisu u stanju da razlikuju zlonamerne ulaze od benignih anomalnih podataka. Značajan izvor podataka za obuku potiče iz nekontrolisanih, nemoderiranih javnih skupova podataka, koji su otvoreni za doprinose trećih strana. Napadači ne moraju da kompromituju skupove podataka kada su slobodni da im doprinose. Vremenom, zlonamerni podaci niskog poverenja postaju podaci visokog poverenja, ako struktura/format podataka ostaje ispravan.

Zato je ključno osigurati integritet i zaštitu skladišta podataka koje vaši modeli koriste za donošenje odluka.

## Razumevanje pretnji i rizika AI

U kontekstu AI i povezanih sistema, trovanje podataka je danas najznačajnija pretnja bezbednosti. Trovanje podataka je kada neko namerno menja informacije korišćene za obuku AI, uzrokujući da pravi greške. Ovo je zbog nedostatka standardizovanih metoda detekcije i ublažavanja, u kombinaciji sa našim oslanjanjem na nepouzdane ili nekontrolisane javne skupove podataka za obuku. Da bi se održao integritet podataka i sprečio pogrešan proces obuke, ključno je pratiti poreklo i liniju vaših podataka. U suprotnom, stara izreka "smeće unutra, smeće napolje" ostaje tačna, što dovodi do kompromitovanog učinka modela.

Evo primera kako trovanje podataka može uticati na vaše modele:

1. **Preokretanje oznaka**: U zadatku binarne klasifikacije, protivnik namerno preokreće oznake malog podskupa podataka za obuku. Na primer, benigni uzorci su označeni kao zlonamerni, što dovodi do toga da model nauči pogrešne asocijacije.\
   **Primer**: Filter za spam pogrešno klasifikuje legitimne mejlove kao spam zbog manipulisanih oznaka.
2. **Trovanje karakteristika**: Napadač suptilno menja karakteristike u podacima za obuku kako bi uveo pristrasnost ili zavarao model.\
   **Primer**: Dodavanje nebitnih ključnih reči u opise proizvoda kako bi se manipulisali sistemi preporuka.
3. **Ubacivanje podataka**: Ubacivanje zlonamernih podataka u skup za obuku kako bi se uticalo na ponašanje modela.\
   **Primer**: Uvođenje lažnih korisničkih recenzija kako bi se izmenili rezultati analize sentimenta.
4. **Napadi zadnjih vrata**: Protivnik ubacuje skriveni obrazac (zadnja vrata) u podatke za obuku. Model uči da prepoznaje ovaj obrazac i ponaša se zlonamerno kada se aktivira.\
   **Primer**: Sistem za prepoznavanje lica obučen sa slikama sa zadnjim vratima koji pogrešno identifikuje određenu osobu.

MITRE Corporation je kreirala [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), bazu znanja taktika i tehnika koje koriste protivnici u stvarnim napadima na AI sisteme.

> Postoji sve veći broj ranjivosti u sistemima sa AI, jer uključivanje AI povećava površinu napada postojećih sistema izvan onih tradicionalnih sajber-napada. Razvili smo ATLAS kako bismo podigli svest o ovim jedinstvenim i evoluirajućim ranjivostima, dok globalna zajednica sve više uključuje AI u različite sisteme. ATLAS je modeliran prema MITRE ATT&CK® okviru i njegove taktike, tehnike i procedure (TTPs) su komplementarne onima u ATT&CK.

Slično MITRE ATT&CK® okviru, koji se obimno koristi u tradicionalnoj sajber-bezbednosti za planiranje naprednih scenarija emulacije pretnji, ATLAS pruža lako pretraživi set TTP-ova koji mogu pomoći u boljem razumevanju i pripremi za odbranu od novih napada.

Dodatno, Open Web Application Security Project (OWASP) je kreirao "[Top 10 listu](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" najkritičnijih ranjivosti pronađenih u aplikacijama koje koriste LLM-ove. Lista ističe rizike pretnji kao što je pomenuto trovanje podataka, zajedno sa drugima kao što su:

- **Ubacivanje upita**: tehnika gde napadači manipulišu velikim jezičkim modelom (LLM) kroz pažljivo osmišljene ulaze, uzrokujući da se ponaša izvan svog predviđenog ponašanja.
- **Ranjivosti lanca snabdevanja**: Komponente i softver koji čine aplikacije koje koristi LLM, kao što su Python moduli ili eksterni skupovi podataka, mogu biti kompromitovani, što dovodi do neočekivanih rezultata, uvedenih pristrasnosti i čak ranjivosti u osnovnoj infrastrukturi.
- **Prekomerno oslanjanje**: LLM-ovi su podložni greškama i skloni su halucinacijama, pružajući netačne ili nesigurne rezultate. U nekoliko dokumentovanih okolnosti, ljudi su prihvatili rezultate zdravo za gotovo, što je dovelo do neželjenih negativnih posledica u stvarnom svetu.

Microsoft Cloud Advocate Rod Trent je napisao besplatnu e-knjigu, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), koja duboko istražuje ove i druge nove AI pretnje i pruža opsežne smernice kako najbolje rešiti ove scenarije.

## Bezbednosno testiranje za AI sisteme i LLM-ove

Veštačka inteligencija (AI) transformiše različite domene i industrije, nudeći nove mogućnosti i beneficije za društvo. Međutim, AI takođe predstavlja značajne izazove i rizike, kao što su privatnost podataka, pristrasnost, nedostatak objašnjivosti i potencijalna zloupotreba. Stoga je ključno osigurati da su AI sistemi bezbedni i odgovorni, što znači da se pridržavaju etičkih i pravnih standarda i da im korisnici i zainteresovane strane mogu verovati.

Bezbednosno testiranje je proces procene bezbednosti AI sistema ili LLM-a, identifikovanjem i iskorišćavanjem njihovih ranjivosti. Ovo mogu izvoditi programeri, korisnici ili nezavisni revizori, u zavisnosti od svrhe i obima testiranja. Neke od najčešćih metoda bezbednosnog testiranja za AI sisteme i LLM-ove su:

- **Sanitacija podataka**: Ovo je proces uklanjanja ili anonimizacije osetljivih ili privatnih informacija iz podataka za obuku ili ulaza AI sistema ili LLM-a. Sanitacija podataka može pomoći u sprečavanju curenja podataka i zlonamerne manipulacije smanjenjem izloženosti poverljivih ili ličnih podataka.
- **Adversarialno testiranje**: Ovo je proces generisanja i primene adversarialnih primera na ulaz ili izlaz AI sistema ili LLM-a kako bi se procenila njegova otpornost i izdržljivost protiv adversarialnih napada. Adversarialno testiranje može pomoći u identifikaciji i ublažavanju ranjivosti i slabosti AI sistema ili LLM-a koje napadači mogu iskoristiti.
- **Verifikacija modela**: Ovo je proces verifikacije ispravnosti i potpunosti parametara modela ili arhitekture AI sistema ili LLM-a. Verifikacija modela može pomoći u otkrivanju i sprečavanju krađe modela osiguravajući da je model zaštićen i autentifikovan.
- **Validacija izlaza**: Ovo je proces validacije kvaliteta i pouzdanosti izlaza AI sistema ili LLM-a. Validacija izlaza može pomoći u otkrivanju i ispravljanju zlonamerne manipulacije osiguravajući da je izlaz dosledan i tačan.

OpenAI, lider u AI sistemima, postavio je niz _evaluacija bezbednosti_ kao deo svoje inicijative mreže crvenih timova, usmerenih na testiranje izlaza AI sistema u nadi da će doprineti bezbednosti AI.

> Evaluacije mogu biti od jednostavnih testova pitanja i odgovora do složenijih simulacija. Kao konkretni primeri, evo uzoraka evaluacija koje je razvio OpenAI za procenu ponašanja AI iz različitih uglova:

#### Ubeđivanje

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Koliko dobro AI sistem može prevariti drugi AI sistem da izgovori tajnu reč?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Koliko dobro AI sistem može ubediti drugi AI sistem da donira novac?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Koliko dobro AI sistem može uticati na podršku političkom predlogu drugog AI sistema?

#### Steganografija (skriveno slanje poruka)

- [Steganografija](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Koliko dobro AI sistem može proći tajne poruke bez da ga drugi AI sistem uhvati?
- [Kompresija teksta](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Koliko dobro AI sistem može kompresovati i dekompresovati poruke, kako bi omogućio skrivanje tajnih poruka?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Koliko dobro AI sistem može koordinirati sa drugim AI sistemom, bez direktne komunikacije?

### Bezbednost AI

Neophodno je da težimo zaštiti AI sistema od zlonamernih napada, zloupotrebe ili neželjenih posledica. Ovo uključuje preduzimanje koraka kako bi se osigurala sigurnost, pouzdanost i poverenje AI sistema, kao što su:

- Obezbeđivanje podataka i algoritama koji se koriste za obuku i rad AI modela
- Sprečavanje neovlašćenog pristupa, manipulacije ili sabotaže AI sistema
- Otkrivanje i ublažavanje pristrasnosti, diskriminacije ili etičkih problema u AI sistemima
- Osiguranje odgovornosti, transparentnosti i objašnjivosti AI odluka i akcija
- Usaglašavanje ciljeva i vrednosti AI sistema sa onima ljudi i društva

Bezbednost AI je važna za osiguranje integriteta, dostupnosti i poverljivosti AI sistema i podataka. Neki od izazova i mogućnosti bezbednosti AI su:

- Mogućnost: Uključivanje AI u strategije sajber-bezbednosti jer može igrati ključnu ulogu u identifikaciji pretnji i poboljšanju vremena odgovora. AI može pomoći u automatizaciji i unapređenju detekcije i ublažavanja sajber-napada, kao što su phishing, malware ili ransomware.
- Izazov: AI može biti korišćen od strane protivnika za pokretanje sofisticiranih napada, kao što je generisanje lažnog ili obmanjujućeg sadržaja, lažno predstavljanje korisnika ili iskorišćavanje ranjivosti u AI sistemima. Stoga, programeri AI imaju jedinstvenu odgovornost da dizajniraju sisteme koji su robusni i otporni na zloupotrebu.

### Zaštita podataka

LLM-ovi mogu predstavljati rizike za privatnost i sigurnost podataka koje koriste. Na primer, LLM-ovi mogu potencijalno zapamtiti i otkriti osetljive informacije iz svojih podataka za obuku, kao što su lična imena, adrese, lozinke ili brojevi kreditnih kartica. Oni takođe mogu biti manipulirani ili napadnuti od strane zlonamernih aktera koji žele da iskoriste njihove ranjivosti ili pristrasnosti. Stoga je važno biti svestan ovih rizika i preduzeti odgovarajuće mere za zaštitu podataka korišćenih sa LLM-ovima. Postoji nekoliko koraka koje možete preduzeti za zaštitu podataka korišćenih sa LLM-ovima. Ovi koraci uključuju:

- **Ograničavanje količine i vrste podataka koje dele sa LLM-ovima**: Delite samo podatke koji su neophodni i relevantni za predviđene svrhe i izbegavajte deljenje bilo kojih podataka koji su osetljivi, poverljivi ili lični. Korisnici takođe treba da anonimizuju ili enkriptuju podatke koje dele sa LLM-ovima, kao što je uklanjanje ili maskiranje bilo kojih identifikacionih informacija, ili korišćenje sigurnih komunikacionih kanala.
- **Verifikacija podataka koje LLM-ovi generišu**: Uvek proverite tačnost i kvalitet izlaza koji generišu LLM-ovi kako biste osigurali da ne sadrže neželjene ili neprikladne informacije.
- **Prijavljivanje i upozoravanje na bilo kakve povrede podataka ili incidente**: Budite oprezni prema bilo kakvim sumnjivim ili nenormalnim aktivnostima ili ponašanjima LLM-ova, kao što je generisanje tekstova koji su nerelevantni, netačni, uvredljivi ili štetni. Ovo bi moglo biti indikacija povrede podataka ili sigurnosnog incidenta.

Bezbednost podataka, upravljanje i usklađenost su ključni za svaku organizaciju koja želi da iskoristi moć podataka i AI u više-cloud okruženju. Obezbeđivanje i upravljanje svim vašim podacima je složen i višestruk zadatak. Morate obezbediti i upravljati različitim tipovima podataka (strukturiranim, nestrukturiranim i podacima generisanim od strane AI) na različitim lokacijama preko više cloud-ova, i morate uzeti u obzir postojeće i buduće propise o bezbednosti podataka, upravljanju i AI. Da biste zaštitili svoje podatke, morate usvojiti neke najbolje prakse i mere opreza, kao što su:

- Koristite cloud usluge ili platforme koje nude zaštitu podataka i funkcije privatnosti.
- Koristite alate za proveru kvaliteta i validaciju podataka kako biste proverili svoje podatke na greške, nedoslednosti ili anomalije.
- Koristite okvire za upravljanje podacima i etiku kako biste osigurali da se vaši podaci koriste na odgovoran i transparentan način.

### Emulacija pretnji iz stvarnog sveta - AI crveni timovi

Emulacija pretnji iz stvarnog sveta sada se smatra standardnom praksom u izgradnji otpornijih AI sistema koristeći slične alate, taktike, procedure za identifikaciju rizika za sisteme i testiranje odgovora branilaca.

> Praksa AI crvenog timovanja evoluirala je da preuzme šire značenje: ne

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, молимо вас да будете свесни да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.