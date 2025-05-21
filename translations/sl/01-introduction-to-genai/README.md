<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-05-19T13:41:13+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "sl"
}
-->
# Uvod v generativno umetno inteligenco in velike jezikovne modele

_(Kliknite zgornjo sliko, da si ogledate video te lekcije)_

Generativna umetna inteligenca je umetna inteligenca, sposobna ustvarjanja besedila, slik in drugih vrst vsebin. Kaj jo naredi izjemno tehnologijo, je, da demokratizira umetno inteligenco; vsakdo jo lahko uporabi z le nekaj besedilnimi ukazi, stavkom, napisanim v naravnem jeziku. Ni vam treba naučiti se jezika, kot sta Java ali SQL, da bi dosegli nekaj vrednega; vse, kar potrebujete, je uporaba vašega jezika, navedete, kaj želite, in AI model poda predlog. Aplikacije in vpliv tega so ogromni, lahko pišete ali razumete poročila, pišete aplikacije in še veliko več, vse v nekaj sekundah.

V tem učnem načrtu bomo raziskali, kako naš startup izkorišča generativno umetno inteligenco za odpiranje novih scenarijev v svetu izobraževanja ter kako se spopadamo z neizogibnimi izzivi, povezanimi s socialnimi posledicami njene uporabe in tehnološkimi omejitvami.

## Uvod

Ta lekcija bo zajemala:

- Uvod v poslovni scenarij: ideja našega startupa in poslanstvo.
- Generativna umetna inteligenca in kako smo pristali na trenutni tehnološki pokrajini.
- Notranje delovanje velikega jezikovnega modela.
- Glavne sposobnosti in praktični primeri uporabe velikih jezikovnih modelov.

## Cilji učenja

Po zaključku te lekcije boste razumeli:

- Kaj je generativna umetna inteligenca in kako delujejo veliki jezikovni modeli.
- Kako lahko izkoristite velike jezikovne modele za različne primere uporabe, s poudarkom na izobraževalnih scenarijih.

## Scenarij: naš izobraževalni startup

Generativna umetna inteligenca (AI) predstavlja vrhunec tehnologije AI, ki premika meje, ki so bile nekoč mišljene kot nemogoče. Generativni AI modeli imajo več sposobnosti in aplikacij, vendar bomo za ta učni načrt raziskali, kako revolucionira izobraževanje prek izmišljenega startupa. Ta startup bomo imenovali _naš startup_. Naš startup deluje na področju izobraževanja z ambicioznim poslanstvom

> _izboljšati dostopnost do učenja na globalni ravni, zagotoviti enakopraven dostop do izobraževanja in ponuditi prilagojene učne izkušnje vsakemu učencu, glede na njegove potrebe_.

Ekipa našega startupa se zaveda, da tega cilja ne bomo mogli doseči brez izkoriščanja enega najmočnejših orodij sodobnega časa – velikih jezikovnih modelov (LLMs).

Generativna umetna inteligenca naj bi revolucionirala način, kako se danes učimo in poučujemo, s študenti, ki imajo na voljo virtualne učitelje 24 ur na dan, ki ponujajo velike količine informacij in primerov, ter učitelji, ki lahko izkoristijo inovativna orodja za ocenjevanje svojih študentov in podajanje povratnih informacij.

Za začetek opredelimo nekaj osnovnih konceptov in terminologije, ki jih bomo uporabljali skozi celoten učni načrt.

## Kako smo dobili generativno umetno inteligenco?

Kljub izjemnemu _hypeu_, ki ga je v zadnjem času ustvarila napoved generativnih AI modelov, je ta tehnologija nastajala desetletja, pri čemer segajo prvi raziskovalni napori v 60. leta. Zdaj smo na točki, ko ima AI človeške kognitivne sposobnosti, kot je pogovor, kar je razvidno na primer iz [OpenAI ChatGPT](https://openai.com/chatgpt) ali [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), ki prav tako uporablja GPT model za spletno iskanje Bing pogovorov.

Če se nekoliko vrnemo nazaj, so prvi prototipi AI sestavljali pisalni chatbot-i, ki so se zanašali na bazo znanja, pridobljeno od skupine strokovnjakov in predstavljeno v računalniku. Odgovori v bazi znanja so bili sproženi s ključnimi besedami, ki so se pojavile v vnosnem besedilu. Vendar je kmalu postalo jasno, da takšen pristop, ki uporablja pisalne chatbot-e, ni dobro skaliran.

### Statistični pristop k AI: strojno učenje

Prelomnica je nastopila v 90-ih letih, z uporabo statističnega pristopa k analizi besedila. To je pripeljalo do razvoja novih algoritmov – znanih kot strojno učenje – sposobnih učenja vzorcev iz podatkov brez eksplicitnega programiranja. Ta pristop omogoča strojem simulacijo razumevanja človeškega jezika: statistični model je usposobljen na parih besedilo-oznaka, kar omogoča modelu klasifikacijo neznanega vhodnega besedila s predhodno določeno oznako, ki predstavlja namen sporočila.

### Nevronske mreže in sodobni virtualni asistenti

V zadnjih letih je tehnološka evolucija strojne opreme, sposobna obdelave večjih količin podatkov in bolj zapletenih izračunov, spodbudila raziskave v AI, kar je privedlo do razvoja naprednih algoritmov strojnega učenja, znanih kot nevronske mreže ali algoritmi globokega učenja.

Nevronske mreže (in zlasti Recurrent Neural Networks – RNNs) so znatno izboljšale obdelavo naravnega jezika, omogočajoč reprezentacijo pomena besedila na bolj smiseln način, vrednotenje konteksta besede v stavku.

To je tehnologija, ki je poganjala virtualne asistente, rojene v prvem desetletju novega stoletja, zelo spretne pri interpretaciji človeškega jezika, prepoznavanju potrebe in izvedbi dejanja, da jo zadovoljijo – kot je odgovor z vnaprej določenim skriptom ali uporaba storitve tretje osebe.

### Današnji dan, generativna umetna inteligenca

Tako smo prišli do generativne umetne inteligence danes, ki jo lahko vidimo kot podskupino globokega učenja.

Po desetletjih raziskav na področju umetne inteligence je nova arhitektura modelov – imenovana _Transformer_ – presegla omejitve RNNs, saj je sposobna sprejemati veliko daljše sekvence besedila kot vhod. Transformatorji temeljijo na mehanizmu pozornosti, kar omogoča modelu, da daje različne teže vhodom, ki jih prejme, 'posveča več pozornosti' tam, kjer je najbolj relevantna informacija skoncentrirana, ne glede na njihov vrstni red v besedilni sekvenci.

Večina nedavnih generativnih AI modelov – znanih tudi kot veliki jezikovni modeli (LLMs), saj delujejo z besedilnimi vhodnimi in izhodnimi podatki – je dejansko temelji na tej arhitekturi. Kar je zanimivo pri teh modelih – usposobljenih na ogromni količini neoznačenih podatkov iz različnih virov, kot so knjige, članki in spletne strani – je, da jih je mogoče prilagoditi za široko paleto nalog in generirati slovnično pravilno besedilo z videzom ustvarjalnosti. Torej, ne le da so neverjetno izboljšali sposobnost stroja, da 'razume' vhodno besedilo, ampak so omogočili njihovo sposobnost generiranja izvirnega odziva v človeškem jeziku.

## Kako delujejo veliki jezikovni modeli?

V naslednjem poglavju bomo raziskali različne vrste generativnih AI modelov, vendar za zdaj poglejmo, kako delujejo veliki jezikovni modeli, s poudarkom na modelih OpenAI GPT (Generative Pre-trained Transformer).

- **Tokenizator, besedilo v številke**: Veliki jezikovni modeli prejmejo besedilo kot vhod in generirajo besedilo kot izhod. Vendar, ker so statistični modeli, delujejo veliko bolje s številkami kot z besedilnimi sekvencami. Zato se vsak vhod v model obdeluje s tokenizatorjem, preden ga uporabi jedro modela. Token je kos besedila – sestavljen iz spremenljivega števila znakov, zato je glavna naloga tokenizatorja razdelitev vhoda v niz tokenov. Nato se vsak token preslika z indeksom tokena, kar je celoštevilčno kodiranje izvirnega dela besedila.

- **Napovedovanje izhodnih tokenov**: Glede na n tokenov kot vhod (z največ n, ki se razlikuje od modela do modela), model lahko napove en token kot izhod. Ta token je nato vključen v vhod naslednje iteracije, v vzorcu razširjajočega se okna, kar omogoča boljšo uporabniško izkušnjo pridobivanja ene (ali več) stavkov kot odgovora. To pojasnjuje, zakaj, če ste se kdaj igrali z ChatGPT, ste morda opazili, da se včasih zdi, da se ustavi sredi stavka.

- **Postopek izbire, porazdelitev verjetnosti**: Izhodni token izbere model glede na verjetnost njegovega pojavljanja po trenutni besedilni sekvenci. To je zato, ker model napoveduje porazdelitev verjetnosti za vse možne 'naslednje tokene', izračunano na podlagi njegovega usposabljanja. Vendar ni vedno izbran token z najvišjo verjetnostjo iz rezultatne porazdelitve. Stopnja naključnosti je dodana tej izbiri, na način, da model deluje na nedeterminističen način - ne dobimo popolnoma enakega izhoda za isti vhod. Ta stopnja naključnosti je dodana, da simulira proces ustvarjalnega razmišljanja in jo je mogoče prilagoditi z uporabo parametra modela, imenovanega temperatura.

## Kako lahko naš startup izkoristi velike jezikovne modele?

Zdaj, ko bolje razumemo notranje delovanje velikega jezikovnega modela, si oglejmo nekaj praktičnih primerov najpogostejših nalog, ki jih lahko opravljajo zelo dobro, s pogledom na naš poslovni scenarij.
Rekli smo, da je glavna sposobnost velikega jezikovnega modela _generiranje besedila iz nič, izhajajoč iz besedilnega vhoda, napisanega v naravnem jeziku_.

Toda kakšen je lahko besedilni vhod in izhod?
Vhod velikega jezikovnega modela je znan kot poziv, medtem ko je izhod znan kot dokončanje, izraz, ki se nanaša na mehanizem modela za generiranje naslednjega tokena za dokončanje trenutnega vhoda. Poglobili se bomo v to, kaj je poziv in kako ga oblikovati na način, da iz modela dobimo največ. Toda za zdaj recimo, da poziv lahko vključuje:

- **Navodilo**, ki določa vrsto izhoda, ki ga pričakujemo od modela. To navodilo včasih lahko vključuje nekaj primerov ali dodatnih podatkov.

  1. Povzetek članka, knjige, pregledov izdelkov in več, skupaj z izluščitvijo vpogledov iz nestrukturiranih podatkov.
  
  2. Ustvarjalno snovanje in oblikovanje članka, eseja, naloge ali več.
  
- **Vprašanje**, zastavljeno v obliki pogovora z agentom.

- Kos **besedila za dokončanje**, kar implicitno pomeni zahtevo za pomoč pri pisanju.

- Kos **kode** skupaj z zahtevo za razlago in dokumentiranje, ali komentar, ki zahteva generiranje kosa kode, ki opravlja določeno nalogo.

Zgornji primeri so precej preprosti in niso namenjeni kot izčrpna demonstracija sposobnosti velikih jezikovnih modelov. Namenjeni so prikazu potenciala uporabe generativne umetne inteligence, zlasti, vendar ne omejeno na izobraževalne kontekste.

Poleg tega izhod generativnega AI modela ni popoln in včasih lahko ustvarjalnost modela deluje proti njemu, kar povzroči izhod, ki je kombinacija besed, ki jih lahko človeški uporabnik interpretira kot izkrivljanje resničnosti, ali je lahko žaljiv. Generativna umetna inteligenca ni inteligentna - vsaj v bolj celoviti definiciji inteligence, ki vključuje kritično in ustvarjalno razmišljanje ali čustveno inteligenco; ni deterministična in ni zanesljiva, saj lahko napačne reference, vsebina in izjave kombinira s pravilnimi informacijami in jih predstavi na prepričljiv in samozavesten način. V naslednjih lekcijah se bomo ukvarjali z vsemi temi omejitvami in videli, kaj lahko storimo za njihovo zmanjšanje.

## Naloga

Vaša naloga je, da preberete več o [generativni umetni inteligenci](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) in poskusite identificirati področje, kjer bi danes dodali generativno umetno inteligenco, ki je še nima. Kako bi bil vpliv drugačen od izvajanja na "star način", ali lahko storite nekaj, česar prej niste mogli, ali ste hitrejši? Napišite 300-besedno povzetek o tem, kako bi izgledal vaš sanjski AI startup in vključite naslove, kot so "Problem", "Kako bi uporabil AI", "Vpliv" in po želji poslovni načrt.

Če ste opravili to nalogo, ste morda celo pripravljeni za prijavo v Microsoftov inkubator, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst), kjer ponujamo kredite za Azure, OpenAI, mentorstvo in še veliko več, preverite!

## Preverjanje znanja

Kaj drži o velikih jezikovnih modelih?

1. Vsakič dobite popolnoma enak odgovor.
1. Stvari opravi popolno, odlično pri seštevanju številk, ustvarjanju delujoče kode itd.
1. Odziv se lahko razlikuje kljub uporabi istega poziva. Prav tako je odličen pri podajanju prvega osnutka nečesa, naj bo to besedilo ali koda. Vendar morate izboljšati rezultate.

A: 3, LLM je nedeterminističen, odziv se razlikuje, vendar lahko nadzorujete njegovo variabilnost z nastavitvijo temperature. Prav tako ne bi smeli pričakovati, da bo stvari opravil popolno, tukaj je, da opravi težko delo za vas, kar pogosto pomeni, da dobite dober prvi poskus nečesa, kar morate postopoma izboljšati.

## Odlično delo! Nadaljujte potovanje

Po zaključku te lekcije si oglejte našo [kolekcijo učenja o generativni umetni inteligenci](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadaljujete z dvigovanjem vašega znanja o generativni umetni inteligenci!

Pojdite na Lekcijo 2, kjer bomo raziskali in primerjali različne vrste LLMs!

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da se zavedate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije se priporoča profesionalni prevod s strani človeka. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.