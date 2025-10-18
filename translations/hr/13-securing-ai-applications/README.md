<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2faf8ee7a0b851efa647a19788f1e5b",
  "translation_date": "2025-10-18T01:30:34+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "hr"
}
-->
# Osiguranje vaših generativnih AI aplikacija

[![Osiguranje vaših generativnih AI aplikacija](../../../translated_images/13-lesson-banner.14103e36b4bbf17398b64ed2b0531f6f2c6549e7f7342f797c40bcae5a11862e.hr.png)](https://youtu.be/m0vXwsx5DNg?si=TYkr936GMKz15K0L)

## Uvod

Ova lekcija obuhvaća:

- Sigurnost u kontekstu AI sustava.
- Uobičajene rizike i prijetnje za AI sustave.
- Metode i razmatranja za osiguranje AI sustava.

## Ciljevi učenja

Nakon završetka ove lekcije, razumjet ćete:

- Prijetnje i rizike za AI sustave.
- Uobičajene metode i prakse za osiguranje AI sustava.
- Kako implementacija sigurnosnog testiranja može spriječiti neočekivane rezultate i gubitak povjerenja korisnika.

## Što znači sigurnost u kontekstu generativne umjetne inteligencije?

Kako tehnologije umjetne inteligencije (AI) i strojnog učenja (ML) sve više oblikuju naše živote, ključno je zaštititi ne samo podatke korisnika, već i same AI sustave. AI/ML se sve više koristi u podršci donošenja odluka od velike važnosti u industrijama gdje pogrešna odluka može imati ozbiljne posljedice.

Evo ključnih točaka koje treba uzeti u obzir:

- **Utjecaj AI/ML-a**: AI/ML imaju značajan utjecaj na svakodnevni život, zbog čega je njihova zaštita postala neophodna.
- **Izazovi sigurnosti**: Zbog tog utjecaja, potrebno je posvetiti odgovarajuću pažnju zaštiti AI proizvoda od sofisticiranih napada, bilo od strane trolova ili organiziranih grupa.
- **Strateški problemi**: Tehnološka industrija mora proaktivno rješavati strateške izazove kako bi osigurala dugoročnu sigurnost korisnika i zaštitu podataka.

Osim toga, modeli strojnog učenja uglavnom nisu sposobni razlikovati zlonamjerne ulaze od bezopasnih anomalnih podataka. Značajan izvor podataka za treniranje dolazi iz neuređenih, nemoderiranih javnih skupova podataka, koji su otvoreni za doprinose trećih strana. Napadači ne moraju kompromitirati skupove podataka kada im je dopušteno da u njih slobodno doprinose. S vremenom, podaci niske pouzdanosti postaju podaci visoke pouzdanosti ako njihova struktura/format ostane ispravan.

Zbog toga je ključno osigurati integritet i zaštitu spremišta podataka koje vaši modeli koriste za donošenje odluka.

## Razumijevanje prijetnji i rizika za AI

U kontekstu AI sustava, trovanje podataka ističe se kao najznačajnija sigurnosna prijetnja danas. Trovanje podataka događa se kada netko namjerno mijenja informacije koje se koriste za treniranje AI-a, uzrokujući da sustav pravi greške. To je posljedica nedostatka standardiziranih metoda za otkrivanje i ublažavanje, u kombinaciji s oslanjanjem na nepouzdane ili neuređene javne skupove podataka za treniranje. Kako bi se održao integritet podataka i spriječio pogrešan proces treniranja, ključno je pratiti podrijetlo i porijeklo vaših podataka. Inače, stara izreka "smeće unutra, smeće van" vrijedi, što dovodi do kompromitiranih performansi modela.

Evo primjera kako trovanje podataka može utjecati na vaše modele:

1. **Preokretanje oznaka**: Kod zadatka binarne klasifikacije, napadač namjerno preokreće oznake malog dijela podataka za treniranje. Na primjer, bezopasni uzorci označeni su kao zlonamjerni, što dovodi do toga da model uči pogrešne asocijacije.\
   **Primjer**: Filter za neželjenu poštu pogrešno klasificira legitimne e-mailove kao neželjene zbog manipuliranih oznaka.
2. **Trovanje značajki**: Napadač suptilno mijenja značajke u podacima za treniranje kako bi uveo pristranost ili zaveo model.\
   **Primjer**: Dodavanje nevažnih ključnih riječi opisima proizvoda kako bi se manipuliralo sustavima preporuka.
3. **Umetanje podataka**: Umetanje zlonamjernih podataka u skup za treniranje kako bi se utjecalo na ponašanje modela.\
   **Primjer**: Uvođenje lažnih korisničkih recenzija kako bi se iskrivili rezultati analize sentimenta.
4. **Napadi stražnjih vrata**: Napadač ubacuje skriveni uzorak (stražnja vrata) u podatke za treniranje. Model uči prepoznati taj uzorak i ponaša se zlonamjerno kada se aktivira.\
   **Primjer**: Sustav prepoznavanja lica treniran s slikama koje sadrže stražnja vrata, što dovodi do pogrešnog prepoznavanja određene osobe.

MITRE Corporation je kreirao [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), bazu znanja o taktikama i tehnikama koje koriste napadači u stvarnim napadima na AI sustave.

> Postoji sve veći broj ranjivosti u sustavima koji koriste AI, jer integracija AI-a povećava površinu napada postojećih sustava izvan tradicionalnih cyber-napada. Razvili smo ATLAS kako bismo podigli svijest o ovim jedinstvenim i evoluirajućim ranjivostima, dok globalna zajednica sve više uključuje AI u različite sustave. ATLAS je modeliran prema MITRE ATT&CK® okviru, a njegove taktike, tehnike i procedure (TTPs) komplementarne su onima u ATT&CK-u.

Slično MITRE ATT&CK® okviru, koji se opsežno koristi u tradicionalnoj kibernetičkoj sigurnosti za planiranje scenarija napredne emulacije prijetnji, ATLAS pruža lako pretraživi skup TTP-ova koji mogu pomoći u boljem razumijevanju i pripremi za obranu od novih napada.

Osim toga, Open Web Application Security Project (OWASP) je kreirao "[Top 10 listu](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" najkritičnijih ranjivosti pronađenih u aplikacijama koje koriste LLM-ove. Lista ističe rizike prijetnji poput spomenutog trovanja podataka, kao i drugih poput:

- **Umetanje upita**: tehnika u kojoj napadači manipuliraju velikim jezičnim modelom (LLM) pažljivo osmišljenim unosima, uzrokujući da se ponaša izvan svoje namjeravane funkcije.
- **Ranjivosti u lancu opskrbe**: Komponente i softver koji čine aplikacije koje koristi LLM, poput Python modula ili vanjskih skupova podataka, mogu biti kompromitirani, što dovodi do neočekivanih rezultata, uvedenih pristranosti pa čak i ranjivosti u osnovnoj infrastrukturi.
- **Pretjerano oslanjanje**: LLM-ovi su podložni greškama i skloni su "halucinacijama", pružajući netočne ili nesigurne rezultate. U nekoliko dokumentiranih slučajeva, ljudi su prihvatili rezultate zdravo za gotovo, što je dovelo do neželjenih negativnih posljedica u stvarnom svijetu.

Microsoft Cloud Advocate Rod Trent napisao je besplatnu e-knjigu, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), koja detaljno istražuje ove i druge nove prijetnje AI-u te pruža opsežne smjernice o tome kako najbolje riješiti ove scenarije.

## Sigurnosno testiranje za AI sustave i LLM-ove

Umjetna inteligencija (AI) transformira različite domene i industrije, nudeći nove mogućnosti i koristi za društvo. Međutim, AI također predstavlja značajne izazove i rizike, poput privatnosti podataka, pristranosti, nedostatka objašnjivosti i potencijalne zloupotrebe. Stoga je ključno osigurati da AI sustavi budu sigurni i odgovorni, što znači da se pridržavaju etičkih i pravnih standarda te da im korisnici i dionici mogu vjerovati.

Sigurnosno testiranje je proces procjene sigurnosti AI sustava ili LLM-a, identificiranjem i iskorištavanjem njihovih ranjivosti. To mogu provoditi programeri, korisnici ili neovisni revizori, ovisno o svrsi i opsegu testiranja. Neke od najčešćih metoda sigurnosnog testiranja za AI sustave i LLM-ove su:

- **Sanitacija podataka**: Proces uklanjanja ili anonimiziranja osjetljivih ili privatnih informacija iz podataka za treniranje ili unosa AI sustava ili LLM-a. Sanitacija podataka može pomoći u sprječavanju curenja podataka i zlonamjerne manipulacije smanjenjem izloženosti povjerljivih ili osobnih podataka.
- **Adversarijalno testiranje**: Proces generiranja i primjene adversarijalnih primjera na unos ili izlaz AI sustava ili LLM-a kako bi se procijenila njihova otpornost na adversarijalne napade. Adversarijalno testiranje može pomoći u identifikaciji i ublažavanju ranjivosti i slabosti AI sustava ili LLM-a koje napadači mogu iskoristiti.
- **Verifikacija modela**: Proces provjere ispravnosti i cjelovitosti parametara ili arhitekture modela AI sustava ili LLM-a. Verifikacija modela može pomoći u otkrivanju i sprječavanju krađe modela osiguravanjem da je model zaštićen i autentificiran.
- **Validacija izlaza**: Proces validacije kvalitete i pouzdanosti izlaza AI sustava ili LLM-a. Validacija izlaza može pomoći u otkrivanju i ispravljanju zlonamjerne manipulacije osiguravanjem da je izlaz dosljedan i točan.

OpenAI, lider u AI sustavima, postavio je niz _evaluacija sigurnosti_ kao dio svoje inicijative za red teaming mrežu, s ciljem testiranja izlaza AI sustava u nadi da će doprinijeti sigurnosti AI-a.

> Evaluacije mogu varirati od jednostavnih Q&A testova do složenijih simulacija. Kao konkretni primjeri, evo uzoraka evaluacija koje je razvio OpenAI za procjenu ponašanja AI-a iz različitih perspektiva:

#### Uvjeravanje

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Koliko dobro AI sustav može navesti drugi AI sustav da izgovori tajnu riječ?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Koliko dobro AI sustav može uvjeriti drugi AI sustav da donira novac?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Koliko dobro AI sustav može utjecati na podršku drugog AI sustava za politički prijedlog?

#### Steganografija (skriveno slanje poruka)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Koliko dobro AI sustav može prenijeti tajne poruke bez da ga drugi AI sustav otkrije?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Koliko dobro AI sustav može komprimirati i dekomprimirati poruke kako bi omogućio skrivanje tajnih poruka?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Koliko dobro AI sustav može koordinirati s drugim AI sustavom bez izravne komunikacije?

### Sigurnost AI-a

Ključno je zaštititi AI sustave od zlonamjernih napada, zloupotrebe ili neželjenih posljedica. To uključuje poduzimanje koraka za osiguranje sigurnosti, pouzdanosti i povjerenja u AI sustave, kao što su:

- Osiguranje podataka i algoritama koji se koriste za treniranje i rad AI modela
- Sprječavanje neovlaštenog pristupa, manipulacije ili sabotaže AI sustava
- Otkrivanje i ublažavanje pristranosti, diskriminacije ili etičkih problema u AI sustavima
- Osiguranje odgovornosti, transparentnosti i objašnjivosti AI odluka i radnji
- Usklađivanje ciljeva i vrijednosti AI sustava s onima ljudi i društva

Sigurnost AI-a važna je za osiguranje integriteta, dostupnosti i povjerljivosti AI sustava i podataka. Neki od izazova i prilika sigurnosti AI-a su:

- Prilika: Uključivanje AI-a u strategije kibernetičke sigurnosti jer može igrati ključnu ulogu u identificiranju prijetnji i poboljšanju vremena reakcije. AI može pomoći u automatizaciji i poboljšanju otkrivanja i ublažavanja kibernetičkih napada, poput phishinga, zlonamjernog softvera ili ransomwarea.
- Izazov: AI također može biti korišten od strane napadača za pokretanje sofisticiranih napada, poput generiranja lažnog ili obmanjujućeg sadržaja, imitacije korisnika ili iskorištavanja ranjivosti u AI sustavima. Stoga, AI programeri imaju jedinstvenu odgovornost dizajnirati sustave koji su robusni i otporni na zloupotrebu.

### Zaštita podataka

LLM-ovi mogu predstavljati rizik za privatnost i sigurnost podataka koje koriste. Na primjer, LLM-ovi mogu potencijalno zapamtiti i otkriti osjetljive informacije iz svojih podataka za treniranje, poput osobnih imena, adresa, lozinki ili brojeva kreditnih kartica. Također mogu biti manipulirani ili napadnuti od strane zlonamjernih aktera koji žele iskoristiti njihove ranjivosti ili pristranosti. Stoga je važno biti svjestan ovih rizika i poduzeti odgovarajuće mjere za zaštitu podataka koji se koriste s LLM-ovima. Postoji nekoliko koraka koje možete poduzeti za zaštitu podataka koji se koriste s LLM-ovima. Ti koraci uključuju:

- **Ograničavanje količine i vrste podataka koje dijelite s LLM-ovima**: Dijelite samo podatke koji su nužni i relevantni za predviđene svrhe, i izbjegavajte dijeljenje bilo kakvih podataka koji su osjetljivi, povjerljivi ili osobni. Korisnici također trebaju anonimizirati ili šifrirati podatke koje dijele s LLM-ovima, poput uklanjanja ili maskiranja bilo kakvih identifikacijskih informacija, ili korištenja sigurnih komunikacijskih kanala.
- **Provjeravanje podataka koje LLM-ovi generiraju**: Uvijek provjerite točnost i kvalitetu izlaza koji generiraju LLM-ovi kako biste osigurali da ne sadrže neželjene ili neprikladne informacije.
- **Prijavljivanje i upozoravanje na bilo kakve povrede podataka ili incidente**: Budite oprezni prema bilo kakvim sumnjivim ili abnormalnim aktivnostima ili ponašanjima LLM-ova, poput generiranja tekstova koji su irelevantni, netočni, uvredljivi ili štetni. To bi moglo biti indikacija povrede podataka ili sigurnosnog incidenta.

Sigurnost podataka, upravljanje i usklađenost ključni su za svaku organizaciju koja želi iskoristiti moć podataka i AI-a u multi-cloud okruženju. Osiguranje i upravljanje svim vašim podacima složen je i višestran zadatak. Potrebno je osigurati i upravljati različitim vrstama podataka (strukturirani, nestrukturirani i podaci generirani AI-om) na različitim lokacijama u više oblaka, te uzeti u obzir postojeće i buduće propise o sigurnosti podataka, upravljanju i AI-u. Kako biste zaštitili svoje podatke, trebate usvojiti neke najbolje prakse i mjere opreza, poput:

- Koristite cloud usluge ili platforme koje nude značajke zaštite podataka i privatnosti.
- Koristite alate za kvalitetu i validaciju podataka kako biste provjerili svoje podatke na pogreške, nedosljednosti ili anomalije.
- Koristite okvire za upravljanje podacima i etiku kako biste osigurali da se vaši podaci koriste na odgovoran i transparentan način.

### Emulacija prijetnji iz stvarnog svijeta - AI
Oponašanje prijetnji iz stvarnog svijeta sada se smatra standardnom praksom u izgradnji otpornijih AI sustava korištenjem sličnih alata, taktika i procedura za identifikaciju rizika za sustave i testiranje odgovora branitelja.

> Praksa AI red teaminga evoluirala je i dobila šire značenje: ne pokriva samo ispitivanje sigurnosnih ranjivosti, već uključuje i ispitivanje drugih neuspjeha sustava, poput generiranja potencijalno štetnog sadržaja. AI sustavi donose nove rizike, a red teaming je ključan za razumijevanje tih novih rizika, poput ubrizgavanja upita i stvaranja neosnovanog sadržaja. - [Microsoft AI Red Team building future of safer AI](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

[![Smjernice i resursi za red teaming](../../../translated_images/13-AI-red-team.642ed54689d7e8a4d83bdf0635768c4fd8aa41ea539d8e3ffe17514aec4b4824.hr.png)]()

Ispod su ključni uvidi koji su oblikovali Microsoftov AI Red Team program.

1. **Širok opseg AI Red Teaminga:**
   AI red teaming sada obuhvaća i sigurnosne i odgovorne AI (RAI) ishode. Tradicionalno, red teaming se fokusirao na sigurnosne aspekte, tretirajući model kao vektor (npr. krađa osnovnog modela). Međutim, AI sustavi uvode nove sigurnosne ranjivosti (npr. ubrizgavanje upita, trovanje), što zahtijeva posebnu pažnju. Osim sigurnosti, AI red teaming također ispituje pitanja pravednosti (npr. stereotipiziranje) i štetnog sadržaja (npr. veličanje nasilja). Rano prepoznavanje ovih problema omogućuje prioritizaciju ulaganja u obranu.
2. **Zlonamjerni i bezazleni neuspjesi:**
   AI red teaming razmatra neuspjehe iz perspektive zlonamjernih i bezazlenih scenarija. Na primjer, prilikom red teaminga novog Binga, istražujemo ne samo kako zlonamjerni protivnici mogu potkopati sustav, već i kako obični korisnici mogu naići na problematičan ili štetan sadržaj. Za razliku od tradicionalnog sigurnosnog red teaminga, koji se uglavnom fokusira na zlonamjerne aktere, AI red teaming uzima u obzir širi raspon persona i potencijalnih neuspjeha.
3. **Dinamična priroda AI sustava:**
   AI aplikacije neprestano evoluiraju. U aplikacijama velikih jezičnih modela, programeri se prilagođavaju promjenjivim zahtjevima. Kontinuirani red teaming osigurava stalnu budnost i prilagodbu evoluirajućim rizicima.

AI red teaming nije sveobuhvatan i treba ga smatrati dopunom dodatnim kontrolama poput [kontrole pristupa temeljenog na ulogama (RBAC)](https://learn.microsoft.com/azure/ai-services/openai/how-to/role-based-access-control?WT.mc_id=academic-105485-koreyst) i sveobuhvatnih rješenja za upravljanje podacima. Namijenjen je dopuni sigurnosne strategije koja se fokusira na primjenu sigurnih i odgovornih AI rješenja koja uzimaju u obzir privatnost i sigurnost, dok nastoje minimizirati pristranosti, štetni sadržaj i dezinformacije koje mogu narušiti povjerenje korisnika.

Evo popisa dodatnih materijala za čitanje koji vam mogu pomoći da bolje razumijete kako red teaming može pomoći u identifikaciji i ublažavanju rizika u vašim AI sustavima:

- [Planiranje red teaminga za velike jezične modele (LLM) i njihove aplikacije](https://learn.microsoft.com/azure/ai-services/openai/concepts/red-teaming?WT.mc_id=academic-105485-koreyst)
- [Što je OpenAI Red Teaming Network?](https://openai.com/blog/red-teaming-network?WT.mc_id=academic-105485-koreyst)
- [AI Red Teaming - Ključna praksa za izgradnju sigurnijih i odgovornijih AI rješenja](https://rodtrent.substack.com/p/ai-red-teaming?WT.mc_id=academic-105485-koreyst)
- MITRE [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), baza znanja o taktikama i tehnikama koje koriste protivnici u stvarnim napadima na AI sustave.

## Provjera znanja

Koji bi mogao biti dobar pristup za održavanje integriteta podataka i sprječavanje zloupotrebe?

1. Imati snažne kontrole pristupa temeljenog na ulogama za upravljanje podacima
1. Provoditi i provjeravati označavanje podataka kako bi se spriječilo pogrešno predstavljanje ili zloupotreba podataka
1. Osigurati da vaša AI infrastruktura podržava filtriranje sadržaja

A:1, Iako su sve tri preporuke odlične, osiguravanje pravilnih privilegija pristupa podacima korisnicima značajno će doprinijeti sprječavanju manipulacije i pogrešnog predstavljanja podataka koje koriste LLM-ovi.

## 🚀 Izazov

Pročitajte više o tome kako možete [upravljati i štititi osjetljive informacije](https://learn.microsoft.com/training/paths/purview-protect-govern-ai/?WT.mc_id=academic-105485-koreyst) u doba AI-a.

## Sjajan posao, nastavite učiti

Nakon što završite ovu lekciju, pogledajte našu [Generative AI Learning kolekciju](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili unapređivati svoje znanje o generativnom AI-u!

Prijeđite na Lekciju 14 gdje ćemo pogledati [Životni ciklus aplikacija generativnog AI-a](../14-the-generative-ai-application-lifecycle/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.