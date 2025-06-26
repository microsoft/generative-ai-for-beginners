<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-06-25T10:09:44+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "sl"
}
-->
# Uvod v Generativno umetno inteligenco in Velike jezikovne modele

Generativna umetna inteligenca (AI) je umetna inteligenca, ki je sposobna ustvarjati besedila, slike in druge vrste vsebin. Kar jo dela fantastično tehnologijo, je to, da demokratizira AI, saj jo lahko uporablja vsak, že s preprostim besednim pozivom, stavkom, napisanim v naravnem jeziku. Ni vam treba naučiti se jezika, kot je Java ali SQL, da bi dosegli nekaj vrednega, vse, kar potrebujete, je uporaba svojega jezika, da izrazite, kaj želite, in AI model vam poda predlog. Aplikacije in vpliv tega so ogromni, lahko pišete ali razumete poročila, pišete aplikacije in še veliko več, vse v nekaj sekundah.

V tem učnem načrtu bomo raziskali, kako naš startup izkorišča generativno AI za odpiranje novih scenarijev v svetu izobraževanja in kako se spopadamo z neizogibnimi izzivi, povezanimi s socialnimi implikacijami njene uporabe in tehnološkimi omejitvami.

## Uvod

Ta lekcija bo zajemala:

- Uvod v poslovni scenarij: naša startup ideja in poslanstvo.
- Generativno AI in kako smo prišli do trenutne tehnološke krajine.
- Notranje delovanje velikega jezikovnega modela.
- Glavne sposobnosti in praktični primeri uporabe Velikih jezikovnih modelov.

## Cilji učenja

Po zaključku te lekcije boste razumeli:

- Kaj je generativna AI in kako delujejo Veliki jezikovni modeli.
- Kako lahko izkoristite velike jezikovne modele za različne primere uporabe, s poudarkom na izobraževalnih scenarijih.

## Scenarij: naš izobraževalni startup

Generativna umetna inteligenca (AI) predstavlja vrh AI tehnologije, ki premika meje tega, kar je bilo nekoč nemogoče. Generativni AI modeli imajo več sposobnosti in aplikacij, vendar bomo za ta učni načrt raziskali, kako revolucionirajo izobraževanje skozi izmišljeni startup. Ta startup bomo imenovali _naš startup_. Naš startup deluje na področju izobraževanja z ambicioznim poslanstvom

> _izboljšati dostopnost učenja na globalni ravni, zagotavljati enakopraven dostop do izobraževanja in omogočati prilagojene učne izkušnje vsakemu učencu glede na njihove potrebe_.

Ekipa našega startupa se zaveda, da tega cilja ne bomo mogli doseči brez uporabe enega najmočnejših orodij sodobnega časa – Velikih jezikovnih modelov (LLM).

Generativna AI naj bi revolucionirala način, kako danes učimo in se učimo, saj imajo študenti na voljo virtualne učitelje 24 ur na dan, ki zagotavljajo ogromno količino informacij in primerov, učitelji pa lahko izkoristijo inovativna orodja za ocenjevanje svojih učencev in podajanje povratnih informacij.

Za začetek definirajmo nekaj osnovnih pojmov in terminologije, ki jih bomo uporabljali skozi celoten učni načrt.

## Kako smo prišli do Generativne AI?

Kljub izjemnemu _navdušenju_, ki ga je v zadnjem času povzročila objava generativnih AI modelov, je ta tehnologija nastajala desetletja, z začetnimi raziskovalnimi prizadevanji, ki segajo v 60. leta. Zdaj smo na točki, ko ima AI človeške kognitivne sposobnosti, kot je pogovor, kar je prikazano na primer z [OpenAI ChatGPT](https://openai.com/chatgpt) ali [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), ki prav tako uporablja GPT model za spletne iskalne pogovore Bing.

Če se nekoliko vrnemo nazaj, so prvi prototipi AI sestavljali pisalni klepetalni roboti, ki so se zanašali na bazo znanja, izvlečeno iz skupine strokovnjakov in predstavljeno v računalniku. Odgovori v bazi znanja so bili sproženi s ključnimi besedami, ki so se pojavile v vnesenem besedilu. Vendar je kmalu postalo jasno, da tak pristop, ki uporablja pisalne klepetalne robote, ni dobro skaliral.

### Statistični pristop k AI: Strojno učenje

Prelomna točka je prišla v 90. letih, z uporabo statističnega pristopa k analizi besedila. To je privedlo do razvoja novih algoritmov – znanih kot strojno učenje – sposobnih učenja vzorcev iz podatkov brez izrecnega programiranja. Ta pristop omogoča strojem simulacijo razumevanja človeškega jezika: statistični model je usposobljen na parih besedilo-oznaka, kar omogoča modelu razvrščanje neznanega vhodnega besedila s predhodno določeno oznako, ki predstavlja namen sporočila.

### Nevronske mreže in sodobni virtualni pomočniki

V zadnjih letih je tehnološki razvoj strojne opreme, ki je sposoben obdelovati večje količine podatkov in bolj zapletene izračune, spodbudil raziskave v AI, kar je privedlo do razvoja naprednih algoritmov strojnega učenja, znanih kot nevronske mreže ali algoritmi globokega učenja.

Nevronske mreže (in zlasti Recurrent Neural Networks – RNN) so bistveno izboljšale obdelavo naravnega jezika, omogočile bolj smiselno predstavitev pomena besedila in vrednotile kontekst besede v stavku.

To je tehnologija, ki je poganjala virtualne pomočnike, rojene v prvem desetletju novega stoletja, zelo spretne pri interpretaciji človeškega jezika, prepoznavanju potreb in izvajanju dejanja za njihovo zadovoljitev – na primer odgovarjanju s predhodno določenim skriptom ali uporabi storitve tretje osebe.

### Danes, Generativna AI

Tako smo prišli do Generativne AI danes, ki jo lahko vidimo kot podskupino globokega učenja.

Po desetletjih raziskav na področju AI je nova arhitektura modela – imenovana _Transformer_ – presegla omejitve RNN, saj je bila sposobna sprejeti veliko daljše zaporedje besedila kot vhod. Transformatorji temeljijo na mehanizmu pozornosti, ki modelu omogoča, da daje različne uteži vhodom, ki jih prejme, 'namenjajoč več pozornosti' tam, kjer je zbrana najbolj relevantna informacija, ne glede na njihov vrstni red v besedilnem zaporedju.

Večina nedavnih generativnih AI modelov – znanih tudi kot Veliki jezikovni modeli (LLM), saj delujejo z besedilnimi vhodi in izhodi – je dejansko temelji na tej arhitekturi. Kar je zanimivo pri teh modelih – usposobljenih na ogromno količino neoznačenih podatkov iz različnih virov, kot so knjige, članki in spletne strani – je, da jih je mogoče prilagoditi za široko paleto nalog in ustvariti slovnično pravilno besedilo s pridihom ustvarjalnosti. Tako niso le izjemno izboljšali sposobnosti stroja za 'razumevanje' vhodnega besedila, temveč so omogočili tudi njihovo sposobnost ustvarjanja izvirnega odziva v človeškem jeziku.

## Kako delujejo veliki jezikovni modeli?

V naslednjem poglavju bomo raziskali različne vrste generativnih AI modelov, vendar si za zdaj oglejmo, kako delujejo veliki jezikovni modeli, s poudarkom na modelih OpenAI GPT (Generative Pre-trained Transformer).

- **Tokenizer, pretvorba besedila v številke**: Veliki jezikovni modeli prejmejo besedilo kot vhod in ustvarijo besedilo kot izhod. Vendar, ker so statistični modeli, delujejo veliko bolje s številkami kot z besedilnimi zaporedji. Zato je vsak vhod v model obdelan s tokenizerjem, preden ga uporabi osnovni model. Token je kos besedila – sestavljen iz spremenljivega števila znakov, zato je glavna naloga tokenizerja razdeliti vhod v niz tokenov. Nato je vsak token preslikan z indeksom tokena, kar je celoštevilčna kodiranje izvirnega besedilnega kosa.

- **Napovedovanje izhodnih tokenov**: Glede na n tokenov kot vhod (z največ n, ki se razlikuje od modela do modela), je model sposoben napovedati en token kot izhod. Ta token je nato vključen v vhod naslednje iteracije, v vzorcu širjenja okna, kar omogoča boljšo uporabniško izkušnjo pridobivanja enega (ali več) stavkov kot odgovora. To pojasnjuje, zakaj, če ste se kdaj igrali s ChatGPT, ste morda opazili, da včasih izgleda, kot da se ustavi sredi stavka.

- **Postopek izbire, porazdelitev verjetnosti**: Izhodni token je izbran s strani modela glede na njegovo verjetnost pojavljanja po trenutnem besedilnem zaporedju. To je zato, ker model napoveduje porazdelitev verjetnosti nad vsemi možnimi 'naslednjimi tokeni', izračunano na podlagi njegovega usposabljanja. Vendar ni vedno izbran token z najvišjo verjetnostjo iz nastale porazdelitve. Stopnja naključnosti je dodana tej izbiri, tako da model deluje na nedeterminističen način - ne dobimo povsem enakega izhoda za isti vhod. Ta stopnja naključnosti je dodana, da simulira proces ustvarjalnega razmišljanja in jo je mogoče prilagoditi z uporabo parametra modela, imenovanega temperatura.

## Kako lahko naš startup izkoristi Velike jezikovne modele?

Zdaj, ko bolje razumemo notranje delovanje velikega jezikovnega modela, poglejmo nekaj praktičnih primerov najpogostejših nalog, ki jih lahko opravljajo zelo dobro, s pogledom na naš poslovni scenarij.
Rekli smo, da je glavna sposobnost velikega jezikovnega modela _generiranje besedila iz nič, izhajajoč iz besedilnega vhoda, napisanega v naravnem jeziku_.

Toda kakšen je besedilni vhod in izhod?
Vhod velikega jezikovnega modela je znan kot poziv, medtem ko je izhod znan kot dokončanje, kar se nanaša na mehanizem modela za generiranje naslednjega tokena, da dokonča trenutni vhod. Podrobno bomo raziskali, kaj je poziv in kako ga zasnovati na način, da iz modela izvlečemo največ. Ampak za zdaj, recimo, da lahko poziv vključuje:

- **Navodilo**, ki določa vrsto izhoda, ki ga pričakujemo od modela. To navodilo včasih lahko vsebuje nekaj primerov ali dodatnih podatkov.

  1. Povzetek članka, knjige, pregledov izdelkov in še več, skupaj z izvlečkom vpogledov iz nestrukturiranih podatkov.
    
  2. Ustvarjalno idejno zasnovo in oblikovanje članka, eseja, naloge ali več.

- **Vprašanje**, postavljeno v obliki pogovora z agentom.

- Kos **besedila za dokončanje**, ki implicitno pomeni prošnjo za pisno pomoč.

- Kos **kode** skupaj z zahtevo za razlago in dokumentiranje ali komentar, ki prosi za generiranje kosa kode, ki izvaja določeno nalogo.

Zgornji primeri so precej preprosti in niso namenjeni kot izčrpen prikaz sposobnosti Velikih jezikovnih modelov. Namenjeni so prikazovanju potenciala uporabe generativne AI, zlasti, vendar ne omejeno na izobraževalne kontekste.

Prav tako izhod generativnega AI modela ni popoln in včasih lahko ustvarjalnost modela deluje proti njemu, kar povzroči izhod, ki je kombinacija besed, ki jih človeški uporabnik lahko interpretira kot mistifikacijo resničnosti, ali pa je lahko žaljiv. Generativna AI ni inteligentna - vsaj v bolj celoviti definiciji inteligence, ki vključuje kritično in ustvarjalno razmišljanje ali čustveno inteligenco; ni deterministična in ni zaupanja vredna, saj lahko kombinira napačne reference, vsebino in izjave s pravilnimi informacijami in jih predstavi na prepričljiv in samozavesten način. V naslednjih lekcijah se bomo ukvarjali z vsemi temi omejitvami in videli, kaj lahko storimo, da jih omilimo.

## Naloga

Vaša naloga je prebrati več o [generativni AI](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) in poskusiti identificirati področje, kjer bi danes dodali generativno AI, ki je še nima. Kako bi bil vpliv drugačen od izvajanja na "stari način", ali lahko storite nekaj, česar prej niste mogli, ali ste hitrejši? Napišite povzetek v 300 besedah o tem, kako bi izgledal vaš sanjski AI startup in vključite naslove kot "Problem", "Kako bi uporabil AI", "Vpliv" in po želji poslovni načrt.

Če ste opravili to nalogo, ste morda celo pripravljeni, da se prijavite na Microsoftov inkubator, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst) kjer ponujamo kredite za Azure, OpenAI, mentorstvo in še veliko več, preverite!

## Preverjanje znanja

Kaj drži o velikih jezikovnih modelih?

1. Vsakič dobite popolnoma enak odgovor.
2. Stvari opravi popolno, odličen pri seštevanju številk, ustvarjanju delujoče kode itd.
3. Odziv se lahko razlikuje kljub uporabi istega poziva. Prav tako je odličen pri dajanju prvega osnutka nečesa, bodisi besedila ali kode. Vendar morate izboljšati rezultate.

A: 3, LLM je nedeterminističen, odziv se razlikuje, vendar lahko njegovo varianco nadzorujete prek nastavitve temperature. Prav tako ne bi smeli pričakovati, da bo stvari opravil popolno, tukaj je, da za vas opravi težko delo, kar pogosto pomeni, da dobite dober prvi poskus nečesa, kar morate postopoma izboljšati.

## Odlično delo! Nadaljujte pot

Po zaključku te lekcije si oglejte našo [kolekcijo učenja o Generativni AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) za nadaljevanje poglabljanja znanja o Generativni AI!

Preusmerite se na Lekcijo 2, kjer bomo raziskali, kako [raziskovati in primerjati različne vrste LLM](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)!

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Medtem ko si prizadevamo za natančnost, vas prosimo, da se zavedate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije je priporočljivo profesionalno človeško prevajanje. Ne odgovarjamo za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.