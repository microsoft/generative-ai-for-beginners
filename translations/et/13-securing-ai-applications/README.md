<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-10-11T11:45:03+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "et"
}
-->
# Generatiivse tehisintellekti rakenduste turvamine

[![Generatiivse tehisintellekti rakenduste turvamine](../../../translated_images/13-lesson-banner.14103e36b4bbf17398b64ed2b0531f6f2c6549e7f7342f797c40bcae5a11862e.et.png)](https://aka.ms/gen-ai-lesson13-gh?WT.mc_id=academic-105485-koreyst)

## Sissejuhatus

Selles õppetükis käsitletakse:

- Turvalisust tehisintellekti süsteemide kontekstis.
- Tehisintellekti süsteemide levinud riske ja ohte.
- Meetodeid ja kaalutlusi tehisintellekti süsteemide turvamiseks.

## Õpieesmärgid

Pärast selle õppetüki läbimist mõistate:

- Tehisintellekti süsteemide ohte ja riske.
- Levinud meetodeid ja praktikaid tehisintellekti süsteemide turvamiseks.
- Kuidas turvatestimine aitab vältida ootamatuid tulemusi ja kasutajate usalduse vähenemist.

## Mida tähendab turvalisus generatiivse tehisintellekti kontekstis?

Kuna tehisintellekti (AI) ja masinõppe (ML) tehnoloogiad kujundavad üha enam meie igapäevaelu, on oluline kaitsta mitte ainult klientide andmeid, vaid ka tehisintellekti süsteeme endid. AI/ML kasutatakse üha enam kõrge väärtusega otsustusprotsesside toetamiseks tööstusharudes, kus valed otsused võivad põhjustada tõsiseid tagajärgi.

Siin on olulised punktid, mida arvestada:

- **AI/ML mõju**: AI/ML mõjutavad oluliselt igapäevaelu, mistõttu nende kaitsmine on muutunud hädavajalikuks.
- **Turvalisuse väljakutsed**: AI/ML mõju vajab piisavat tähelepanu, et kaitsta AI-põhiseid tooteid keerukate rünnakute eest, olgu need trollide või organiseeritud gruppide poolt.
- **Strateegilised probleemid**: Tehnoloogiasektor peab proaktiivselt tegelema strateegiliste väljakutsetega, et tagada pikaajaline klientide turvalisus ja andmete kaitse.

Lisaks ei suuda masinõppe mudelid suuresti eristada pahatahtlikku sisendit ja kahjutut anomaalset andmestikku. Märkimisväärne osa treeningandmetest pärineb kureerimata, modereerimata avalikest andmekogumitest, mis on avatud kolmandate osapoolte panustele. Ründajad ei pea andmekogumeid kompromiteerima, kui neil on vabadus neisse panustada. Aja jooksul muutuvad madala usaldusväärsusega pahatahtlikud andmed kõrge usaldusväärsusega usaldusväärseteks andmeteks, kui andmestruktuur ja vorming jäävad korrektseks.

Seetõttu on kriitiline tagada andmekogude terviklikkus ja kaitse, mida teie mudelid otsuste tegemiseks kasutavad.

## Tehisintellekti ohtude ja riskide mõistmine

Tehisintellekti ja sellega seotud süsteemide kontekstis on andmete mürgitamine tänapäeval kõige olulisem turvaoht. Andmete mürgitamine toimub siis, kui keegi tahtlikult muudab teavet, mida kasutatakse tehisintellekti treenimiseks, põhjustades selle eksimusi. See tuleneb standardiseeritud tuvastamis- ja leevendusmeetodite puudumisest ning meie sõltuvusest usaldusväärsetest või kureerimata avalikest andmekogumitest treenimiseks. Andmete terviklikkuse säilitamiseks ja vigase treenimisprotsessi vältimiseks on oluline jälgida oma andmete päritolu ja päritolu. Vastasel juhul kehtib vana ütlus "prügi sisse, prügi välja", mis viib mudeli jõudluse halvenemiseni.

Siin on näited, kuidas andmete mürgitamine võib teie mudeleid mõjutada:

1. **Siltide ümberpööramine**: Kahesuunalise klassifitseerimise ülesandes pöörab vastane tahtlikult väikese osa treeningandmete silte. Näiteks märgistatakse kahjutud näidised pahatahtlikeks, mis viib mudeli valede seoste õppimiseni.\
   **Näide**: Rämpsposti filter klassifitseerib legitiimsed e-kirjad rämpspostiks manipuleeritud siltide tõttu.
2. **Omaduste mürgitamine**: Ründaja muudab treeningandmete omadusi peenelt, et tekitada kallutatust või eksitada mudelit.\
   **Näide**: Lisatakse ebaolulisi märksõnu tootekirjeldustesse, et manipuleerida soovitussüsteemidega.
3. **Andmete süstimine**: Pahatahtlike andmete lisamine treeningkogumisse, et mõjutada mudeli käitumist.\
   **Näide**: Võltsitud kasutajate arvustuste lisamine, et kallutada sentimentanalüüsi tulemusi.
4. **Tagaukse rünnakud**: Vastane lisab treeningandmetesse varjatud mustri (tagaukse). Mudel õpib seda mustrit ära tundma ja käitub pahatahtlikult, kui muster aktiveeritakse.\
   **Näide**: Näotuvastussüsteem, mis on treenitud tagauksega piltidega ja tuvastab konkreetse isiku valesti.

MITRE Corporation on loonud [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), teadmistebaasi taktikatest ja tehnikatest, mida vastased kasutavad tehisintellekti süsteemide reaalsetes rünnakutes.

> Tehisintellekti kasutamine suurendab olemasolevate süsteemide rünnakupinda traditsiooniliste küberrünnakute kõrval, mis toob kaasa kasvava hulga haavatavusi AI-toega süsteemides. Me lõime ATLAS-i, et tõsta teadlikkust nendest unikaalsetest ja arenevatest haavatavustest, kuna globaalne kogukond integreerib tehisintellekti üha enam erinevatesse süsteemidesse. ATLAS on modelleeritud MITRE ATT&CK® raamistikule ja selle taktikad, tehnikad ja protseduurid (TTP-d) täiendavad ATT&CK-i omasid.

Sarnaselt MITRE ATT&CK® raamistikule, mida kasutatakse laialdaselt traditsioonilises küberturvalisuses arenenud ohu emulatsioonistsenaariumide kavandamiseks, pakub ATLAS hõlpsasti otsitavat TTP-de komplekti, mis aitab paremini mõista ja valmistuda kaitseks uute rünnakute vastu.

Lisaks on Open Web Application Security Project (OWASP) loonud "[Top 10 nimekirja](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" kõige kriitilisematest haavatavustest rakendustes, mis kasutavad LLM-e. Nimekiri toob esile selliste ohtude riske nagu eespool mainitud andmete mürgitamine ja teised, näiteks:

- **Käskude süstimine**: tehnika, kus ründajad manipuleerivad suure keelemudeliga (LLM) hoolikalt koostatud sisendite kaudu, põhjustades selle käitumist väljaspool kavandatud funktsionaalsust.
- **Tarneahela haavatavused**: komponendid ja tarkvara, mis moodustavad LLM-i kasutatavad rakendused, nagu Python moodulid või välised andmekogumid, võivad ise olla kompromiteeritud, mis viib ootamatute tulemuste, kallutatuse ja isegi infrastruktuuri haavatavusteni.
- **Liigne sõltuvus**: LLM-id on ekslikud ja kalduvad "hallutsineerima", pakkudes ebatäpseid või ohtlikke tulemusi. Mitmel dokumenteeritud juhul on inimesed võtnud tulemusi tõe pähe, mis on viinud soovimatute negatiivsete tagajärgedeni reaalses maailmas.

Microsofti pilveadvokaat Rod Trent on kirjutanud tasuta e-raamatu, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), mis süveneb nendesse ja teistesse arenevatesse tehisintellekti ohtudesse ning pakub ulatuslikke juhiseid, kuidas neid olukordi kõige paremini lahendada.

## Tehisintellekti süsteemide ja LLM-ide turvatestimine

Tehisintellekt (AI) muudab erinevaid valdkondi ja tööstusharusid, pakkudes uusi võimalusi ja kasu ühiskonnale. Kuid AI toob kaasa ka olulisi väljakutseid ja riske, nagu andmete privaatsus, kallutatus, selguse puudumine ja võimalik väärkasutus. Seetõttu on oluline tagada, et tehisintellekti süsteemid oleksid turvalised ja vastutustundlikud, järgides eetilisi ja õiguslikke standardeid ning olles usaldusväärsed kasutajate ja sidusrühmade jaoks.

Turvatestimine on protsess, mille käigus hinnatakse tehisintellekti süsteemi või LLM-i turvalisust, tuvastades ja kasutades ära nende haavatavusi. Seda võivad läbi viia arendajad, kasutajad või kolmandate osapoolte audiitorid, sõltuvalt testimise eesmärgist ja ulatusest. Mõned levinumad turvatestimise meetodid tehisintellekti süsteemide ja LLM-ide jaoks on:

- **Andmete puhastamine**: protsess, mille käigus eemaldatakse või anonüümseks muudetakse tundlik või privaatne teave treeningandmetest või tehisintellekti süsteemi või LLM-i sisendist. Andmete puhastamine aitab vältida andmete lekkimist ja pahatahtlikku manipuleerimist, vähendades konfidentsiaalsete või isiklike andmete kokkupuudet.
- **Vasturünnakute testimine**: protsess, mille käigus genereeritakse ja rakendatakse vasturünnakute näiteid tehisintellekti süsteemi või LLM-i sisendile või väljundile, et hinnata selle vastupidavust ja vastupanuvõimet vasturünnakute vastu. Vasturünnakute testimine aitab tuvastada ja leevendada tehisintellekti süsteemi või LLM-i haavatavusi ja nõrkusi, mida ründajad võivad ära kasutada.
- **Mudeli verifitseerimine**: protsess, mille käigus kontrollitakse tehisintellekti süsteemi või LLM-i mudeli parameetrite või arhitektuuri õigsust ja täielikkust. Mudeli verifitseerimine aitab tuvastada ja ennetada mudeli varastamist, tagades, et mudel on kaitstud ja autentne.
- **Väljundi valideerimine**: protsess, mille käigus valideeritakse tehisintellekti süsteemi või LLM-i väljundi kvaliteeti ja usaldusväärsust. Väljundi valideerimine aitab tuvastada ja parandada pahatahtlikku manipuleerimist, tagades, et väljund on järjepidev ja täpne.

OpenAI, tehisintellekti süsteemide juhtiv arendaja, on loonud _turvalisuse hindamised_ osana oma punase meeskonna võrgustiku algatusest, mille eesmärk on testida tehisintellekti süsteemide väljundeid, et aidata kaasa tehisintellekti turvalisusele.

> Hindamised võivad ulatuda lihtsatest küsimuste ja vastuste testidest keerukamate simulatsioonideni. Konkreetsete näidetena on siin OpenAI poolt välja töötatud hindamised, mis analüüsivad tehisintellekti käitumist mitmest vaatenurgast:

#### Veenvus

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Kui hästi suudab tehisintellekti süsteem panna teise tehisintellekti süsteemi ütlema salajast sõna?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Kui hästi suudab tehisintellekti süsteem veenda teist tehisintellekti süsteemi annetama raha?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Kui hästi suudab tehisintellekti süsteem mõjutada teise tehisintellekti süsteemi toetust poliitilisele ettepanekule?

#### Steganograafia (varjatud sõnumid)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Kui hästi suudab tehisintellekti süsteem edastada salajasi sõnumeid, ilma et teine tehisintellekti süsteem neid avastaks?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Kui hästi suudab tehisintellekti süsteem tihendada ja dekompresseerida sõnumeid, et võimaldada salajaste sõnumite peitmist?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Kui hästi suudab tehisintellekti süsteem koordineerida teise tehisintellekti süsteemiga, ilma otsese suhtluseta?

### Tehisintellekti turvalisus

On ülioluline kaitsta tehisintellekti süsteeme pahatahtlike rünnakute, väärkasutuse või soovimatute tagajärgede eest. See hõlmab samme, et tagada tehisintellekti süsteemide turvalisus, usaldusväärsus ja usaldusväärsus, näiteks:

- Andmete ja algoritmide turvamine, mida kasutatakse tehisintellekti mudelite treenimiseks ja käitamiseks.
- Tehisintellekti süsteemide volitamata juurdepääsu, manipuleerimise või sabotaaži vältimine.
- Kallutatuse, diskrimineerimise või eetiliste probleemide tuvastamine ja leevendamine tehisintellekti süsteemides.
- Tehisintellekti otsuste ja tegevuste vastutuse, läbipaistvuse ja selgitatavuse tagamine.
- Tehisintellekti süsteemide eesmärkide ja väärtuste kooskõlastamine inimeste ja ühiskonna omadega.

Tehisintellekti turvalisus on oluline tehisintellekti süsteemide ja andmete terviklikkuse, kättesaadavuse ja konfidentsiaalsuse tagamiseks. Mõned tehisintellekti turvalisuse väljakutsed ja võimalused on:

- **Võimalus**: Tehisintellekti integreerimine küberturvalisuse strateegiatesse, kuna see võib mängida olulist rolli ohtude tuvastamisel ja reageerimisaja parandamisel. Tehisintellekt aitab automatiseerida ja täiustada küberrünnakute, nagu andmepüük, pahavara või lunavara, tuvastamist ja leevendamist.
- **Väljakutse**: Tehisintellekti võivad kasutada ka vastased keerukate rünnakute läbiviimiseks, näiteks vale või eksitava sisu genereerimiseks, kasutajate jäljendamiseks või tehisintellekti süsteemide haavatavuste ärakasutamiseks. Seetõttu on tehisintellekti arendajatel ainulaadne vastutus luua süsteeme, mis on robustsed ja vastupidavad väärkasutuse vastu.

### Andmekaitse

LLM-id võivad ohustada nende kasutatavate andmete privaatsust ja turvalisust. Näiteks võivad LLM-id potentsiaalselt meelde jätta ja lekkida tundlikku teavet oma treeningandmetest, nagu isikunimed, aadressid, paroolid või krediitkaardi numbrid. Neid võivad manipuleerida või rünnata pahatahtlikud osapooled, kes soovivad ära kasutada nende haavatavusi või kallutatust. Seetõttu on oluline olla teadlik nendest riskidest ja võtta asjakohaseid meetmeid LLM-idega kasutatavate andmete kaitsmiseks. On mitmeid samme, mida saate astuda LLM-idega kasutatavate andmete kaitsmiseks. Need sammud hõlmavad:

- **Andmete jagamise piiramine**: Jagage ainult neid andmeid, mis on vajalikud ja asjakohased kavandatud eesmärkide jaoks, ning vältige tundlike, konfidentsiaalsete või isiklike andmete jagamist. Kasutajad peaksid ka anonüümseks muutma või krüpteerima andmed, mida nad LLM-idega jagavad, näiteks eemaldades või maskeerides mis tahes tuvastavat teavet või kasutades turvalisi suhtluskanaleid.
- **LLM-ide genereeritud andmete kontrollimine**: Kontrollige alati LLM-ide genereeritud väljundi täpsust ja kvaliteeti, et veenduda, et need ei sisalda soovimatut või sobimatut teavet.
- **Andmelekkest või juhtumitest teatamine ja hoiatamine**: Olge valvas LLM-ide
Reaalse maailma ohtude jäljendamine on nüüd standardne praktika vastupidavate tehisintellektisüsteemide loomisel, kasutades sarnaseid tööriistu, taktikaid ja protseduure, et tuvastada süsteemide riske ja testida kaitsjate reageerimist.

> Tehisintellekti red teamingu praktika on arenenud laiemaks tähenduseks: see ei hõlma ainult turvavigade otsimist, vaid ka teiste süsteemirikkumiste tuvastamist, nagu potentsiaalselt kahjuliku sisu genereerimine. Tehisintellektisüsteemid toovad kaasa uusi riske ning red teaming on oluline nende uute riskide, nagu prompt injection ja põhjendamata sisu loomine, mõistmiseks. - [Microsoft AI Red Team ehitab turvalisema tehisintellekti tulevikku](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

[![Juhised ja ressursid red teamingu jaoks](../../../translated_images/13-AI-red-team.642ed54689d7e8a4d83bdf0635768c4fd8aa41ea539d8e3ffe17514aec4b4824.et.png)]()

Allpool on peamised teadmised, mis on kujundanud Microsofti AI Red Team programmi.

1. **AI Red Teamingu lai ulatus:**
   AI red teaming hõlmab nüüd nii turvalisust kui ka vastutustundliku tehisintellekti (RAI) tulemusi. Traditsiooniliselt keskendus red teaming turvalisuse aspektidele, käsitledes mudelit kui vektorit (nt mudeli varastamine). Kuid tehisintellektisüsteemid toovad kaasa uusi turvavigu (nt prompt injection, mürgitamine), mis vajavad erilist tähelepanu. Turvalisuse kõrval uurib AI red teaming ka õiglust (nt stereotüübid) ja kahjulikku sisu (nt vägivalla ülistamine). Nende probleemide varajane tuvastamine võimaldab kaitseinvesteeringute prioriseerimist.
2. **Pahatahtlikud ja heatahtlikud rikkumised:**
   AI red teaming arvestab rikkumisi nii pahatahtlikust kui ka heatahtlikust vaatenurgast. Näiteks uue Bingi red teamingu puhul uurime mitte ainult seda, kuidas pahatahtlikud vastased võivad süsteemi õõnestada, vaid ka seda, kuidas tavalised kasutajad võivad kokku puutuda probleemse või kahjuliku sisuga. Erinevalt traditsioonilisest turvalisuse red teamingust, mis keskendub peamiselt pahatahtlikele osapooltele, arvestab AI red teaming laiemat valikut isikuid ja võimalikke rikkumisi.
3. **Tehisintellektisüsteemide dünaamiline olemus:**
   Tehisintellekti rakendused arenevad pidevalt. Suurte keelemudelite rakendustes kohandavad arendajad end muutuvate nõuetega. Jätkuv red teaming tagab pideva valvsuse ja kohanemise muutuvate riskidega.

AI red teaming ei ole kõikehõlmav ja seda tuleks käsitleda täiendava meetmena lisakontrollidele, nagu [rollipõhine juurdepääsukontroll (RBAC)](https://learn.microsoft.com/azure/ai-services/openai/how-to/role-based-access-control?WT.mc_id=academic-105485-koreyst) ja terviklikud andmehalduslahendused. See on mõeldud täiendama turvastrateegiat, mis keskendub turvaliste ja vastutustundlike tehisintellektilahenduste kasutamisele, arvestades privaatsust ja turvalisust ning püüdes minimeerida kallutatust, kahjulikku sisu ja väärinfot, mis võivad kasutajate usaldust õõnestada.

Siin on nimekiri lisalugemisest, mis aitab paremini mõista, kuidas red teaming aitab tuvastada ja leevendada riske teie tehisintellektisüsteemides:

- [Red teamingu planeerimine suurte keelemudelite (LLM) ja nende rakenduste jaoks](https://learn.microsoft.com/azure/ai-services/openai/concepts/red-teaming?WT.mc_id=academic-105485-koreyst)
- [Mis on OpenAI Red Teaming Network?](https://openai.com/blog/red-teaming-network?WT.mc_id=academic-105485-koreyst)
- [AI Red Teaming - Oluline praktika turvalisemate ja vastutustundlikumate tehisintellektilahenduste loomiseks](https://rodtrent.substack.com/p/ai-red-teaming?WT.mc_id=academic-105485-koreyst)
- MITRE [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), teadmistebaas taktikatest ja tehnikatest, mida vastased kasutavad reaalse maailma rünnakutes tehisintellektisüsteemide vastu.

## Teadmiste kontroll

Milline võiks olla hea lähenemine andmete terviklikkuse säilitamiseks ja väärkasutuse vältimiseks?

1. Kasutage tugevaid rollipõhiseid kontrollimeetmeid andmete juurdepääsu ja haldamise jaoks
1. Rakendage ja auditeerige andmete märgistamist, et vältida andmete vale esitamist või väärkasutust
1. Veenduge, et teie tehisintellekti infrastruktuur toetab sisufiltreerimist

A:1, Kuigi kõik kolm on suurepärased soovitused, aitab õige andmejuurdepääsuõiguste määramine kasutajatele oluliselt vältida andmete manipuleerimist ja vale esitamist, mida LLM-id kasutavad.

## 🚀 Väljakutse

Lugege rohkem selle kohta, kuidas [hallata ja kaitsta tundlikku teavet](https://learn.microsoft.com/training/paths/purview-protect-govern-ai/?WT.mc_id=academic-105485-koreyst) tehisintellekti ajastul.

## Suurepärane töö, jätkake õppimist

Pärast selle õppetunni läbimist vaadake meie [Generatiivse tehisintellekti õppekollektsiooni](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), et jätkata oma generatiivse tehisintellekti teadmiste arendamist!

Liikuge edasi 14. õppetundi, kus vaatame [Generatiivse tehisintellekti rakenduse elutsüklit](../14-the-generative-ai-application-lifecycle/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.