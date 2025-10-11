<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7f8f4c11f8c1cb6e1794442dead414ea",
  "translation_date": "2025-10-11T11:25:49+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "et"
}
-->
# Generatiivse tehisintellekti vastutustundlik kasutamine

[![Generatiivse tehisintellekti vastutustundlik kasutamine](../../../translated_images/03-lesson-banner.1ed56067a452d97709d51f6cc8b6953918b2287132f4909ade2008c936cd4af9.et.png)](https://aka.ms/gen-ai-lesson3-gh?WT.mc_id=academic-105485-koreyst)

> _Klõpsa ülaloleval pildil, et vaadata selle õppetunni videot_

Tehisintellekt, eriti generatiivne tehisintellekt, võib olla väga põnev, kuid oluline on mõelda, kuidas seda vastutustundlikult kasutada. Tuleb arvestada näiteks sellega, kuidas tagada, et väljund oleks õiglane, mitte kahjulik ja palju muud. See peatükk annab teile vajaliku konteksti, mida arvestada ja kuidas astuda aktiivseid samme oma tehisintellekti kasutamise parandamiseks.

## Sissejuhatus

Selles õppetükis käsitletakse:

- Miks peaksite generatiivse tehisintellekti rakenduste loomisel eelistama vastutustundlikku tehisintellekti.
- Vastutustundliku tehisintellekti põhiprintsiipe ja nende seost generatiivse tehisintellektiga.
- Kuidas neid vastutustundliku tehisintellekti põhimõtteid strateegia ja tööriistade abil praktikas rakendada.

## Õppimise eesmärgid

Pärast selle õppetunni läbimist teate:

- Vastutustundliku tehisintellekti olulisust generatiivse tehisintellekti rakenduste loomisel.
- Millal mõelda ja rakendada vastutustundliku tehisintellekti põhiprintsiipe generatiivse tehisintellekti rakenduste loomisel.
- Millised tööriistad ja strateegiad on teile kättesaadavad vastutustundliku tehisintellekti kontseptsiooni rakendamiseks.

## Vastutustundliku tehisintellekti põhimõtted

Generatiivse tehisintellekti populaarsus pole kunagi olnud suurem. See populaarsus on toonud sellesse valdkonda palju uusi arendajaid, tähelepanu ja rahastust. Kuigi see on väga positiivne kõigile, kes soovivad generatiivse tehisintellekti abil tooteid ja ettevõtteid luua, on oluline tegutseda vastutustundlikult.

Selle kursuse jooksul keskendume oma idufirma ja tehisintellekti haridustootega töötamisele. Kasutame vastutustundliku tehisintellekti põhimõtteid: õiglus, kaasatus, usaldusväärsus/turvalisus, turvalisus ja privaatsus, läbipaistvus ja vastutus. Nende põhimõtete abil uurime, kuidas need seostuvad generatiivse tehisintellekti kasutamisega meie toodetes.

## Miks peaksite eelistama vastutustundlikku tehisintellekti

Toote loomisel viib parimate tulemusteni inimkeskne lähenemine, kus peetakse silmas kasutaja parimaid huve.

Generatiivse tehisintellekti ainulaadsus seisneb selle võimes luua kasutajatele kasulikke vastuseid, teavet, juhiseid ja sisu. Seda saab teha ilma paljude manuaalsete sammudeta, mis võib viia väga muljetavaldavate tulemusteni. Ilma korraliku planeerimise ja strateegiateta võib see kahjuks viia ka kahjulike tulemusteni teie kasutajate, toote ja kogu ühiskonna jaoks.

Vaatame mõningaid (kuid mitte kõiki) võimalikke kahjulikke tulemusi:

### Hallutsinatsioonid

Hallutsinatsioonid on termin, mida kasutatakse kirjeldamaks olukorda, kus suur keelemudel (LLM) toodab sisu, mis on kas täiesti mõttetu või faktuaalselt vale teistele allikatele tuginedes.

Näiteks kui loome oma idufirmale funktsiooni, mis võimaldab õpilastel esitada mudelile ajaloolisi küsimusi. Õpilane küsib: `Kes oli Titanicu ainus ellujäänu?`

Mudel annab vastuse, näiteks järgmise:

![Küsimus "Kes oli Titanicu ainus ellujäänu"](../../../03-using-generative-ai-responsibly/images/ChatGPT-titanic-survivor-prompt.webp)

> _(Allikas: [Flying bisons](https://flyingbisons.com?WT.mc_id=academic-105485-koreyst))_

See on väga enesekindel ja põhjalik vastus. Kahjuks on see vale. Isegi minimaalne uurimistöö näitaks, et Titanicu katastroofist oli rohkem kui üks ellujäänu. Õpilase jaoks, kes alles alustab selle teema uurimist, võib see vastus olla piisavalt veenev, et seda mitte kahtluse alla seada ja võtta seda faktina. Selle tagajärjeks võib olla tehisintellekti süsteemi ebausaldusväärsus ja meie idufirma maine kahjustamine.

Iga uue LLM-i versiooniga oleme näinud edusamme hallutsinatsioonide minimeerimisel. Isegi nende edusammude juures peame rakenduste loojate ja kasutajatena olema nende piirangutest teadlikud.

### Kahjulik sisu

Eelmises osas käsitlesime olukordi, kus LLM toodab valesid või mõttetuid vastuseid. Teine risk, millest peame teadlikud olema, on olukorrad, kus mudel vastab kahjuliku sisuga.

Kahjulik sisu võib olla:

- Juhiste andmine või enesevigastamise või teatud rühmade kahjustamise julgustamine.
- Vihkav või alandav sisu.
- Rünnakute või vägivaldsete tegude planeerimise juhendamine.
- Juhiste andmine, kuidas leida ebaseaduslikku sisu või toime panna ebaseaduslikke tegusid.
- Seksuaalselt selgesõnalise sisu kuvamine.

Meie idufirma jaoks tahame veenduda, et meil on olemas õiged tööriistad ja strateegiad, et takistada sellise sisu jõudmist õpilasteni.

### Ebaõiglus

Õiglust defineeritakse kui “tagamist, et tehisintellekti süsteem on vaba eelarvamustest ja diskrimineerimisest ning kohtleb kõiki õiglaselt ja võrdselt.” Generatiivse tehisintellekti maailmas tahame tagada, et mudeli väljund ei tugevdaks marginaliseeritud rühmade välistavaid maailmavaateid.

Sellised väljundid ei kahjusta mitte ainult meie kasutajate jaoks positiivsete tootmiskogemuste loomist, vaid põhjustavad ka täiendavat kahju ühiskonnale. Rakenduste loojatena peaksime alati arvestama laia ja mitmekesise kasutajaskonnaga, kui loome lahendusi generatiivse tehisintellekti abil.

## Kuidas kasutada generatiivset tehisintellekti vastutustundlikult

Nüüd, kui oleme tuvastanud vastutustundliku generatiivse tehisintellekti olulisuse, vaatame nelja sammu, mida saame astuda, et ehitada oma tehisintellekti lahendusi vastutustundlikult:

![Leevendamise tsükkel](../../../translated_images/mitigate-cycle.babcd5a5658e1775d5f2cb47f2ff305cca090400a72d98d0f9e57e9db5637c72.et.png)

### Mõõda võimalikke kahjusid

Tarkvara testimisel testime kasutaja eeldatavaid tegevusi rakenduses. Samamoodi on hea viis võimalike kahjude mõõtmiseks testida mitmekesist komplekti küsimusi, mida kasutajad tõenäoliselt esitavad.

Kuna meie idufirma ehitab haridustoodet, oleks hea koostada nimekiri haridusega seotud küsimustest. See võiks hõlmata teatud teemasid, ajaloolisi fakte ja küsimusi õpilaselu kohta.

### Leevenda võimalikke kahjusid

Nüüd on aeg leida viise, kuidas saaksime mudeli ja selle vastuste põhjustatud kahjusid ennetada või piirata. Seda saab vaadelda neljal erineval tasandil:

![Leevendamise kihid](../../../translated_images/mitigation-layers.377215120b9a1159a8c3982c6bbcf41b6adf8c8fa04ce35cbaeeb13b4979cdfc.et.png)

- **Mudel**. Õige mudeli valimine õige kasutusjuhtumi jaoks. Suuremad ja keerukamad mudelid, nagu GPT-4, võivad väiksemate ja spetsiifilisemate kasutusjuhtumite korral põhjustada suuremat kahjuliku sisu riski. Oma treeningandmete kasutamine mudeli peenhäälestamiseks vähendab samuti kahjuliku sisu riski.

- **Turvasüsteem**. Turvasüsteem on mudelit teenindava platvormi tööriistade ja konfiguratsioonide kogum, mis aitab kahjusid leevendada. Näiteks on olemas Azure OpenAI teenuse sisu filtreerimise süsteem. Süsteemid peaksid tuvastama ka jailbreak-rünnakuid ja soovimatut tegevust, näiteks botide päringuid.

- **Metaprompt**. Metapromptid ja maandamine on viisid, kuidas saame mudelit teatud käitumise ja teabe põhjal suunata või piirata. See võib tähendada süsteemi sisendite kasutamist mudeli teatud piiride määratlemiseks. Lisaks võib see tähendada väljundite pakkumist, mis on süsteemi ulatuse või domeeniga rohkem seotud.

Samuti võib see tähendada selliste tehnikate kasutamist nagu Retrieval Augmented Generation (RAG), et mudel tõmbaks teavet ainult valitud usaldusväärsetest allikatest. Selle kursuse hilisemas osas on õppetund [otsingurakenduste loomisest](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst).

- **Kasutajakogemus**. Viimane kiht on koht, kus kasutaja suhtleb mudeliga otse meie rakenduse liidese kaudu. Sel viisil saame kujundada kasutajaliidese/UX-i nii, et see piiraks kasutajat mudelile saadetavate sisendite tüüpide osas, samuti teksti või pilte, mida kasutajale kuvatakse. Tehisintellekti rakendust juurutades peame olema ka läbipaistvad selle osas, mida meie generatiivne tehisintellekti rakendus suudab ja mida mitte.

Meil on terve õppetund pühendatud [tehisintellekti rakenduste kasutajakogemuse kujundamisele](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst).

- **Mudelihindamine**. Suurte keelemudelitega töötamine võib olla keeruline, kuna me ei oma alati kontrolli mudeli treenimiseks kasutatud andmete üle. Sellest hoolimata peaksime alati hindama mudeli jõudlust ja väljundeid. Oluline on mõõta mudeli täpsust, sarnasust, põhjendatust ja väljundi asjakohasust. See aitab pakkuda läbipaistvust ja usaldust sidusrühmadele ja kasutajatele.

### Vastutustundliku generatiivse tehisintellekti lahenduse haldamine

Tehisintellekti rakenduste ümber operatiivse praktika loomine on viimane etapp. See hõlmab koostööd teiste meie idufirma osakondadega, nagu juriidiline ja turvalisus, et tagada vastavus kõigile regulatiivsetele nõuetele. Enne käivitamist tahame koostada ka plaanid tarnimise, intsidentide käsitlemise ja tagasivõtmise kohta, et vältida meie kasutajatele kahju tekitamist.

## Tööriistad

Kuigi vastutustundlike tehisintellekti lahenduste väljatöötamine võib tunduda keeruline, on see töö vaeva väärt. Kuna generatiivse tehisintellekti valdkond kasvab, arenevad ka tööriistad, mis aitavad arendajatel tõhusalt integreerida vastutustundlikkust oma töövoogudesse. Näiteks [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) aitab API-päringute kaudu tuvastada kahjulikku sisu ja pilte.

## Teadmiste kontroll

Millistele asjadele peate tähelepanu pöörama, et tagada tehisintellekti vastutustundlik kasutamine?

1. Et vastus oleks õige.  
2. Kahjulik kasutus, et tehisintellekti ei kasutataks kuritegelikel eesmärkidel.  
3. Tagada, et tehisintellekt oleks vaba eelarvamustest ja diskrimineerimisest.  

V: 2 ja 3 on õiged. Vastutustundlik tehisintellekt aitab teil kaaluda, kuidas kahjulikke mõjusid ja eelarvamusi leevendada ning palju muud.

## 🚀 Väljakutse

Lugege [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) kohta ja vaadake, mida saate oma kasutuse jaoks rakendada.

## Suurepärane töö, jätkake õppimist

Pärast selle õppetunni läbimist tutvuge meie [Generatiivse tehisintellekti õppekollektsiooniga](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), et jätkata oma teadmiste täiendamist generatiivse tehisintellekti vallas!

Liikuge edasi 4. õppetundi, kus vaatleme [Prompt Engineeringu aluseid](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.