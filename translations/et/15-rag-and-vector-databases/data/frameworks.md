<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-10-11T11:16:07+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "et"
}
-->
# Neuraalvõrkude raamistikud

Nagu me juba õppisime, on neuraalvõrkude tõhusaks treenimiseks vaja teha kahte asja:

* Töötada tensoritega, näiteks korrutada, liita ja arvutada mõningaid funktsioone nagu sigmoid või softmax
* Arvutada kõigi avaldiste tuletised, et teostada gradientide languse optimeerimist

Kuigi `numpy` teek suudab täita esimest osa, vajame mehhanismi gradientide arvutamiseks. Eelmises osas välja töötatud raamistikus pidime kõik tuletisfunktsioonid käsitsi programmeerima `backward` meetodis, mis teostab tagasipropageerimist. Ideaalis peaks raamistik võimaldama arvutada gradienti *mis tahes avaldise* jaoks, mida suudame defineerida.

Teine oluline aspekt on arvutuste tegemine GPU-l või mõnel muul spetsialiseeritud arvutusüksusel, näiteks TPU-l. Sügavate neuraalvõrkude treenimine nõuab *väga palju* arvutusi, ja nende arvutuste paralleelne teostamine GPU-l on väga oluline.

> ✅ Termin 'paralleelne teostamine' tähendab arvutuste jaotamist mitme seadme vahel.

Praegu on kaks kõige populaarsemat neuraalvõrkude raamistikku: TensorFlow ja PyTorch. Mõlemad pakuvad madala taseme API-d tensoritega töötamiseks nii CPU-l kui GPU-l. Madala taseme API peale on olemas ka kõrgema taseme API, vastavalt Keras ja PyTorch Lightning.

Madala taseme API | TensorFlow | PyTorch
------------------|-----------------------|-----------------------
Kõrgema taseme API | Keras | PyTorch Lightning

**Madala taseme API-d** mõlemas raamistikus võimaldavad luua nn **arvutusgraafikuid**. See graafik määratleb, kuidas arvutada väljundit (tavaliselt kaotuse funktsiooni) antud sisendparameetritega ja seda saab GPU-le arvutamiseks saata, kui see on saadaval. Graafiku diferentseerimiseks ja gradientide arvutamiseks on olemas funktsioonid, mida saab seejärel kasutada mudeli parameetrite optimeerimiseks.

**Kõrgema taseme API-d** käsitlevad neuraalvõrke peamiselt kui **kihtide järjestust** ja muudavad enamiku neuraalvõrkude konstrueerimise palju lihtsamaks. Mudeli treenimine nõuab tavaliselt andmete ettevalmistamist ja seejärel `fit` funktsiooni kutsumist, et töö ära teha.

Kõrgema taseme API võimaldab tüüpilisi neuraalvõrke väga kiiresti konstrueerida, muretsemata paljude detailide pärast. Samal ajal pakub madala taseme API palju rohkem kontrolli treenimisprotsessi üle ja seetõttu kasutatakse seda palju teadustöös, kui tegeletakse uute neuraalvõrkude arhitektuuridega.

Samuti on oluline mõista, et mõlemat API-d saab koos kasutada, näiteks saate madala taseme API abil välja töötada oma võrgu kihi arhitektuuri ja seejärel kasutada seda suuremas võrgus, mis on konstrueeritud ja treenitud kõrgema taseme API abil. Või saate defineerida võrgu kõrgema taseme API abil kihtide järjestusena ja seejärel kasutada oma madala taseme treenimistsüklit optimeerimise teostamiseks. Mõlemad API-d kasutavad samu põhilisi aluskontseptsioone ja on loodud hästi koos töötama.

## Õppimine

Selles kursuses pakume enamikku sisust nii PyTorchile kui TensorFlowle. Saate valida oma eelistatud raamistikku ja läbida ainult vastavad märkmikud. Kui te pole kindel, millist raamistikku valida, lugege internetis arutelusid teemal **PyTorch vs. TensorFlow**. Samuti võite mõlemat raamistikku uurida, et paremini aru saada.

Võimaluse korral kasutame lihtsuse huvides kõrgema taseme API-sid. Kuid usume, et on oluline mõista, kuidas neuraalvõrgud töötavad algtasemel, seega alustame madala taseme API ja tensoritega töötamisest. Kui aga soovite kiiresti alustada ja ei taha nende detailide õppimisele palju aega kulutada, võite need vahele jätta ja minna otse kõrgema taseme API märkmike juurde.

## ✍️ Harjutused: Raamistikud

Jätkake õppimist järgmistes märkmikes:

Madala taseme API | TensorFlow+Keras märkmik | PyTorch
------------------|--------------------------|-----------------------
Kõrgema taseme API | Keras | *PyTorch Lightning*

Pärast raamistikuga tutvumist vaatame üle üleliigse sobitamise (overfitting) mõiste.

# Üleliigne sobitamine

Üleliigne sobitamine on masinõppes äärmiselt oluline mõiste ja on väga tähtis sellest õigesti aru saada!

Vaatleme järgmist probleemi, kus tuleb ligikaudselt määrata 5 punkti (graafikutel tähistatud `x`-ga):

!lineaarne | üleliigne sobitamine
-------------------------|--------------------------
**Lineaarne mudel, 2 parameetrit** | **Mitte-lineaarne mudel, 7 parameetrit**
Treeningu viga = 5.3 | Treeningu viga = 0
Valideerimise viga = 5.1 | Valideerimise viga = 20

* Vasakul näeme head sirgjoonelist ligikaudset määratlust. Kuna parameetrite arv on piisav, saab mudel punktide jaotuse olemusest õigesti aru.
* Paremal on mudel liiga võimas. Kuna meil on ainult 5 punkti ja mudelil on 7 parameetrit, saab see kohanduda nii, et läbib kõik punktid, muutes treeningu vea nulliks. Kuid see takistab mudelil andmete õiget mustrit mõista, mistõttu valideerimise viga on väga suur.

On väga oluline leida õige tasakaal mudeli rikkuse (parameetrite arv) ja treeningnäidiste arvu vahel.

## Miks üleliigne sobitamine tekib

  * Ebapiisav treeningandmete hulk
  * Liiga võimas mudel
  * Liiga palju müra sisendandmetes

## Kuidas üleliigset sobitamist tuvastada

Nagu ülaltoodud graafikult näha, saab üleliigset sobitamist tuvastada väga madala treeningu vea ja kõrge valideerimise vea järgi. Tavaliselt näeme treenimise ajal, et nii treeningu kui valideerimise vead hakkavad vähenema, kuid mingil hetkel valideerimise viga võib lõpetada vähenemise ja hakata suurenema. See on märk üleliigsest sobitamisest ja indikaator, et treenimine tuleks tõenäoliselt lõpetada (või vähemalt mudelist hetkeseis salvestada).

## Kuidas üleliigset sobitamist vältida

Kui näete, et üleliigne sobitamine toimub, saate teha järgmist:

 * Suurendage treeningandmete hulka
 * Vähendage mudeli keerukust
 * Kasutage mõnda regulatsioonitehnikat, näiteks Dropout, mida käsitleme hiljem.

## Üleliigne sobitamine ja Bias-Variance Tradeoff

Üleliigne sobitamine on tegelikult statistikas tuntud üldisema probleemi, Bias-Variance Tradeoff, juhtum. Kui kaalume oma mudeli võimalikke veallikaid, näeme kahte tüüpi vigu:

* **Bias-vead** tekivad siis, kui meie algoritm ei suuda treeningandmete seost õigesti tabada. See võib tuleneda sellest, et meie mudel pole piisavalt võimas (**alaliigne sobitamine**).
* **Variance-vead**, mis tekivad mudeli poolt sisendandmete müra ligikaudse määratlemise asemel tähendusliku seose (**üleliigne sobitamine**) tõttu.

Treeningu ajal bias-vead vähenevad (kuna meie mudel õpib andmeid ligikaudselt määratlema) ja variance-vead suurenevad. On oluline treenimine lõpetada - kas käsitsi (kui tuvastame üleliigse sobitamise) või automaatselt (regulatsiooni kasutuselevõtuga) - et vältida üleliigset sobitamist.

## Kokkuvõte

Selles õppetunnis õppisite erinevusi kahe kõige populaarsema AI-raamistiku, TensorFlow ja PyTorch, erinevate API-de vahel. Lisaks õppisite väga olulist teemat, üleliigset sobitamist.

## 🚀 Väljakutse

Kaasaolevates märkmikes leiate 'ülesanded' allosas; töötage märkmikud läbi ja täitke ülesanded.

## Ülevaade ja iseseisev õppimine

Tehke uurimistööd järgmiste teemade kohta:

- TensorFlow
- PyTorch
- Üleliigne sobitamine

Esitage endale järgmised küsimused:

- Mis vahe on TensorFlow ja PyTorch vahel?
- Mis vahe on üleliigsel sobitamisel ja alaliigsel sobitamisel?

## Ülesanne

Selles laboris palutakse teil lahendada kaks klassifitseerimisprobleemi, kasutades ühe- ja mitmekihilisi täielikult ühendatud võrke PyTorch või TensorFlow abil.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.