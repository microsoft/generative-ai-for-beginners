<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d57fad773cbeb69c5dd62e65c34200d",
  "translation_date": "2025-10-18T01:31:11+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "hr"
}
-->
# Odgovorno korištenje generativne umjetne inteligencije

[![Odgovorno korištenje generativne umjetne inteligencije](../../../translated_images/03-lesson-banner.1ed56067a452d97709d51f6cc8b6953918b2287132f4909ade2008c936cd4af9.hr.png)](https://youtu.be/YOp-e1GjZdA?si=7Wv4wu3x44L1DCVj)

> _Kliknite na sliku iznad za pregled videa ove lekcije_

Lako je biti fasciniran umjetnom inteligencijom, posebno generativnom umjetnom inteligencijom, ali važno je razmisliti o tome kako je odgovorno koristiti. Treba razmotriti stvari poput osiguravanja da je izlaz pravedan, neškodljiv i još mnogo toga. Ovaj će vam poglavlje pružiti kontekst, na što obratiti pažnju i kako poduzeti aktivne korake za poboljšanje korištenja umjetne inteligencije.

## Uvod

Ova lekcija obuhvaća:

- Zašto biste trebali dati prednost odgovornoj umjetnoj inteligenciji prilikom izrade aplikacija temeljenih na generativnoj umjetnoj inteligenciji.
- Temeljna načela odgovorne umjetne inteligencije i njihovu povezanost s generativnom umjetnom inteligencijom.
- Kako primijeniti ova načela odgovorne umjetne inteligencije kroz strategiju i alate.

## Ciljevi učenja

Nakon završetka ove lekcije znat ćete:

- Važnost odgovorne umjetne inteligencije prilikom izrade aplikacija temeljenih na generativnoj umjetnoj inteligenciji.
- Kada razmišljati i primijeniti temeljna načela odgovorne umjetne inteligencije prilikom izrade aplikacija temeljenih na generativnoj umjetnoj inteligenciji.
- Koji su alati i strategije dostupni za primjenu koncepta odgovorne umjetne inteligencije.

## Načela odgovorne umjetne inteligencije

Uzbuđenje oko generativne umjetne inteligencije nikada nije bilo veće. Ovo uzbuđenje privuklo je mnoge nove programere, pažnju i financiranje u ovom području. Iako je to vrlo pozitivno za svakoga tko želi graditi proizvode i tvrtke koristeći generativnu umjetnu inteligenciju, također je važno postupati odgovorno.

Kroz ovaj tečaj fokusiramo se na izgradnju našeg startupa i našeg edukacijskog AI proizvoda. Koristit ćemo načela odgovorne umjetne inteligencije: pravednost, inkluzivnost, pouzdanost/sigurnost, sigurnost i privatnost, transparentnost i odgovornost. Pomoću ovih načela istražit ćemo kako se ona odnose na našu upotrebu generativne umjetne inteligencije u našim proizvodima.

## Zašto biste trebali dati prednost odgovornoj umjetnoj inteligenciji

Prilikom izrade proizvoda, pristup usmjeren na ljude, koji uzima u obzir najbolje interese korisnika, dovodi do najboljih rezultata.

Jedinstvenost generativne umjetne inteligencije leži u njezinoj sposobnosti stvaranja korisnih odgovora, informacija, smjernica i sadržaja za korisnike. To se može učiniti bez mnogo ručnih koraka, što može dovesti do vrlo impresivnih rezultata. Bez odgovarajućeg planiranja i strategija, to također može, nažalost, dovesti do štetnih rezultata za vaše korisnike, vaš proizvod i društvo u cjelini.

Pogledajmo neke (ali ne sve) od potencijalno štetnih rezultata:

### Halucinacije

Halucinacije su pojam koji se koristi za opisivanje situacija kada LLM generira sadržaj koji je ili potpuno besmislen ili nešto za što znamo da je činjenično netočno na temelju drugih izvora informacija.

Primjerice, zamislimo da gradimo funkciju za naš startup koja omogućuje studentima da postavljaju povijesna pitanja modelu. Student postavi pitanje `Tko je bio jedini preživjeli s Titanica?`

Model generira odgovor poput sljedećeg:

![Upit "Tko je bio jedini preživjeli s Titanica"](../../../03-using-generative-ai-responsibly/images/ChatGPT-titanic-survivor-prompt.webp)

> _(Izvor: [Flying bisons](https://flyingbisons.com?WT.mc_id=academic-105485-koreyst))_

Ovo je vrlo samouvjeren i detaljan odgovor. Nažalost, netočan je. Čak i uz minimalno istraživanje, otkrilo bi se da je više od jedne osobe preživjelo katastrofu Titanica. Za studenta koji tek počinje istraživati ovu temu, ovaj odgovor može biti dovoljno uvjerljiv da ga ne dovede u pitanje i da ga prihvati kao činjenicu. Posljedice toga mogu dovesti do nepouzdanosti AI sustava i negativno utjecati na reputaciju našeg startupa.

Svakom iteracijom bilo kojeg LLM-a vidimo poboljšanja u smanjenju halucinacija. Čak i uz ovo poboljšanje, mi kao graditelji aplikacija i korisnici i dalje moramo biti svjesni ovih ograničenja.

### Štetni sadržaj

Ranije smo pokrili situacije kada LLM generira netočne ili besmislene odgovore. Drugi rizik kojeg moramo biti svjesni je kada model odgovara štetnim sadržajem.

Štetni sadržaj može se definirati kao:

- Davanje uputa ili poticanje na samoozljeđivanje ili ozljeđivanje određenih skupina.
- Mrzilački ili ponižavajući sadržaj.
- Pomoć u planiranju bilo koje vrste napada ili nasilnih radnji.
- Davanje uputa o tome kako pronaći ilegalni sadržaj ili počiniti ilegalne radnje.
- Prikazivanje seksualno eksplicitnog sadržaja.

Za naš startup, želimo osigurati da imamo prave alate i strategije kako bismo spriječili da ovakav sadržaj bude dostupan studentima.

### Nedostatak pravednosti

Pravednost se definira kao "osiguranje da je AI sustav slobodan od pristranosti i diskriminacije te da sve tretira pravedno i jednako." U svijetu generativne umjetne inteligencije, želimo osigurati da isključujući svjetonazori marginaliziranih skupina nisu pojačani izlazom modela.

Ove vrste izlaza ne samo da su destruktivne za izgradnju pozitivnog iskustva proizvoda za naše korisnike, već također uzrokuju daljnju društvenu štetu. Kao graditelji aplikacija, uvijek bismo trebali imati na umu široku i raznoliku bazu korisnika prilikom izrade rješenja s generativnom umjetnom inteligencijom.

## Kako odgovorno koristiti generativnu umjetnu inteligenciju

Sada kada smo identificirali važnost odgovorne generativne umjetne inteligencije, pogledajmo 4 koraka koje možemo poduzeti kako bismo odgovorno izgradili naše AI rješenja:

![Ciklus ublažavanja](../../../translated_images/mitigate-cycle.babcd5a5658e1775d5f2cb47f2ff305cca090400a72d98d0f9e57e9db5637c72.hr.png)

### Mjerenje potencijalnih šteta

U testiranju softvera testiramo očekivane radnje korisnika na aplikaciji. Slično tome, testiranje raznolikog skupa upita koje će korisnici najvjerojatnije koristiti dobar je način za mjerenje potencijalne štete.

Budući da naš startup gradi edukacijski proizvod, bilo bi dobro pripremiti popis upita vezanih uz obrazovanje. To bi moglo uključivati određene predmete, povijesne činjenice i upite o studentskom životu.

### Ublažavanje potencijalnih šteta

Sada je vrijeme da pronađemo načine kako možemo spriječiti ili ograničiti potencijalnu štetu uzrokovanu modelom i njegovim odgovorima. Na to možemo gledati kroz 4 različita sloja:

![Slojevi ublažavanja](../../../translated_images/mitigation-layers.377215120b9a1159a8c3982c6bbcf41b6adf8c8fa04ce35cbaeeb13b4979cdfc.hr.png)

- **Model**. Odabir pravog modela za pravi slučaj upotrebe. Veći i složeniji modeli poput GPT-4 mogu predstavljati veći rizik od štetnog sadržaja kada se primjenjuju na manje i specifične slučajeve upotrebe. Korištenje vaših podataka za treniranje modela također smanjuje rizik od štetnog sadržaja.

- **Sigurnosni sustav**. Sigurnosni sustav je skup alata i konfiguracija na platformi koja poslužuje model i pomaže u ublažavanju štete. Primjer toga je sustav za filtriranje sadržaja na Azure OpenAI usluzi. Sustavi također trebaju otkriti napade na sustav i neželjene aktivnosti poput zahtjeva od strane botova.

- **Metaprompt**. Metapromptovi i uzemljenje su načini na koje možemo usmjeriti ili ograničiti model na temelju određenih ponašanja i informacija. To može uključivati korištenje ulaza sustava za definiranje određenih ograničenja modela. Osim toga, pružanje izlaza koji su relevantniji za opseg ili područje sustava.

Također se mogu koristiti tehnike poput Retrieval Augmented Generation (RAG) kako bi model povlačio informacije samo iz odabranih pouzdanih izvora. Postoji lekcija kasnije u ovom tečaju o [izradi aplikacija za pretraživanje](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Korisničko iskustvo**. Završni sloj je mjesto gdje korisnik izravno komunicira s modelom putem sučelja naše aplikacije na neki način. Na taj način možemo dizajnirati UI/UX kako bismo ograničili korisnika u vrstama unosa koje može poslati modelu, kao i tekst ili slike prikazane korisniku. Prilikom implementacije AI aplikacije, također moramo biti transparentni o tome što naša generativna AI aplikacija može, a što ne može učiniti.

Imamo cijelu lekciju posvećenu [Dizajniranju UX-a za AI aplikacije](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Procjena modela**. Rad s LLM-ovima može biti izazovan jer nemamo uvijek kontrolu nad podacima na kojima je model treniran. Bez obzira na to, uvijek bismo trebali procijeniti performanse i izlaze modela. I dalje je važno mjeriti točnost modela, sličnost, uzemljenost i relevantnost izlaza. To pomaže pružiti transparentnost i povjerenje dionicima i korisnicima.

### Upravljanje odgovornim generativnim AI rješenjem

Izgradnja operativne prakse oko vaših AI aplikacija je završna faza. To uključuje suradnju s drugim dijelovima našeg startupa, poput pravnog i sigurnosnog odjela, kako bismo osigurali usklađenost sa svim regulatornim politikama. Prije lansiranja također želimo izraditi planove oko isporuke, rješavanja incidenata i povlačenja kako bismo spriječili bilo kakvu štetu za naše korisnike.

## Alati

Iako se rad na razvoju rješenja odgovorne umjetne inteligencije može činiti zahtjevnim, to je trud koji se itekako isplati. Kako područje generativne umjetne inteligencije raste, sve više alata koji pomažu programerima da učinkovito integriraju odgovornost u svoje radne procese će se razvijati. Na primjer, [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) može pomoći u otkrivanju štetnog sadržaja i slika putem API zahtjeva.

## Provjera znanja

Na što trebate obratiti pažnju kako biste osigurali odgovorno korištenje umjetne inteligencije?

1. Da je odgovor točan.
1. Štetna upotreba, da se AI ne koristi za kriminalne svrhe.
1. Osiguranje da AI nije pristrana i diskriminirajuća.

A: 2 i 3 su točni. Odgovorna umjetna inteligencija pomaže vam razmotriti kako ublažiti štetne učinke i pristranosti i još mnogo toga.

## 🚀 Izazov

Pročitajte o [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) i istražite što možete primijeniti za svoju upotrebu.

## Odlično obavljeno, nastavite učiti

Nakon završetka ove lekcije, pogledajte našu [Generative AI Learning kolekciju](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili unapređivati svoje znanje o generativnoj umjetnoj inteligenciji!

Prijeđite na lekciju 4 gdje ćemo proučiti [Osnove inženjeringa upita](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.