[![Avatud lähtekoodiga mudelid](../../../translated_images/et/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Oma LLM-i peenhäälestamine

Suurte keelemudelite kasutamine generatiivsete tehisintellekti rakenduste loomiseks toob kaasa uusi väljakutseid. Põhiline probleem on tagada mudeli poolt kasutajapäringule genereeritud sisu kvaliteet (täpsus ja asjakohasus). Eelnevates õppetundides käsitlesime tehnikaid nagu promptide inseneritöö ja tagasiside abil täiendamine, mis üritavad probleemi lahendada _muutes olemasolevale mudelile sisendit_.

Tänases õppetükis arutleme kolmandat tehnikat, **peenhäälestamist**, mis püüdleb väljakutse lahendamise poole _mudeli enda täiendõppega_ täiendavate andmete abil. Sukeldume üksikasjadesse.

## Õppe eesmärgid

See õppetükk tutvustab peenhäälestamise mõistet eelnevalt treenitud keelemudelite puhul, uurib selle lähenemise eeliseid ja väljakutseid ning annab juhiseid, millal ja kuidas kasutada peenhäälestamist oma generatiivsete tehisintellekti mudelite jõudluse parandamiseks.

Õppetüki lõpus peaksid suutma vastata järgmistele küsimustele:

- Mis on peenhäälestamine keelemudelite puhul?
- Millal ja miks on peenhäälestamine kasulik?
- Kuidas ma saan eelnevalt treenitud mudelit peenhäälestada?
- Millised on peenhäälestamise piirangud?

Valmis? Alustame.

## Illustreeritud juhend

Kas soovid enne süvenemist saada ülevaadet sellest, mida me käsitleme? Vaata seda illustreeritud juhendit, mis kirjeldab õppe teekonda — alates peenhäälestamise põhikontseptsioonide ja motivatsiooni õppimisest kuni protsessi ja parimate tavade mõistmiseni selle ülesande täitmisel. See on põnev teema avastamiseks, nii et ära unusta lisalinkide ja iseseisva õppimise toe saamiseks vaadata [ressursside](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) lehte!

![Illustreeritud juhend keelemudelite peenhäälestamiseks](../../../translated_images/et/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Mis on peenhäälestamine keelemudelite puhul?

Suurte keelemudelite definitsiooni järgi on need _ettevõtmise käigus_ treenitud suurel hulgal tekstiandmete põhjal, mis pärinevad mitmesugustest allikatest, sh internetist. Nagu eelmistest õppetundidest õppisime, vajame vastuste kvaliteedi parandamiseks kasutajate küsimustele ("promptidele") selliseid tehnikaid nagu _promptide inseneritöö_ ja _tagasiside abil täiendamine_.

Populaarne promptide inseneritöö tehnika hõlmab mudeli juhendamist, mida vastuses oodatakse, kas andes sellele _juhiseid_ (selged suunised) või _mõned näited_ (kaudsed suunised). Seda nimetatakse _mõnenäiteliseks õppimiseks_, kuid sellel on kaks piirangut:

- Mudeli sümbolite limiidid võivad piirata seda, kui palju näiteid saad anda, ning piirata efektiivsust.
- Mudeli sümboli maksumus võib teha näidete lisamise iga prompti juurde kulukaks ja piirata paindlikkust.

Peenhäälestamine on masinõppes levinud tava, kus me võtame eelnevalt treenitud mudeli ja täiendõpime seda uute andmetega, et parandada selle jõudlust kindlal ülesandel. Keelemudelite kontekstis võime peenhäälestada eelnevalt treenitud mudelit _valitud näidiste komplektiga antud ülesande või rakenduse valdkonna jaoks_, et luua **kohandatud mudel**, mis võib olla täpsem ja asjakohasem antud ülesande või valdkonna jaoks. Peenhäälestamise lisaboonusena võib see vähendada ka mõnenäitelise õppimise jaoks vajalike näidiste hulka — vähendades sümbolite kasutust ja sellega seotud kulusid.

## Millal ja miks peaksime mudeleid peenhäälestama?

_Selles_ kontekstis, kui me räägime peenhäälestamisest, viitame me **juhendatud** peenhäälestamisele, kus mudeli täiendõpe toimub **uute andmete lisamisega**, mida originaalse treeningandmestiku hulka ei kuulunud. See erineb juhendamata peenhäälestamisest, kus mudelit treenitakse originaalandmetel, kuid muudatustega hüperparameetrites.

Peamine asi, mida meeles pidada, on see, et peenhäälestamine on täiustatud tehnika, mis nõuab teatud taseme ekspertiisi, et saavutada soovitud tulemusi. Kui seda tehakse valesti, võib see oodata säravaid tulemusi mitte pakkuda ega isegi mudeli jõudlust sihttööstuses halvendada.

Nii et enne kui õpid, "kuidas" keelemudeleid peenhäälestada, pead teadma "miks" peaksid seda tegema ja "millal" alustama peenhäälestamise protsessi. Alusta endale järgmiste küsimuste esitamist:

- **Kasutusjuhtum**: Mis on sinu _kasutusjuhtum_ peenhäälestamiseks? Millist aspekti olemasolevast eelnevalt treenitud mudelist soovid parandada?
- **Alternatiivid**: Kas oled proovinud _teisi tehnikaid_ soovitud tulemuste saavutamiseks? Kasuta neid võrdlusalusena.
  - Promptide inseneritöö: proovi tehnikaid nagu mõnenäitelised promptid näidetega asjakohastest vastustest. Hinda vastuste kvaliteeti.
  - Tagasiside abil täiendamine: proovi promptide täiendamist päringutulemustega, mis on sinu andmetest otsitud. Hinda vastuste kvaliteeti.
- **Kulud**: Kas oled kindlaks määranud peenhäälestamise kulud?
  - Häälestatavus — kas eelnevalt treenitud mudel on peenhäälestamiseks saadaval?
  - Pingutus — koolitusandmete ettevalmistamine, mudeli hindamine ja täiustamine.
  - Arvutusjõud — peenhäälestustööde jooksutamine ja peenhäälestatud mudeli juurutamine.
  - Andmed — juurdepääs piisava kvaliteediga näidistele peenhäälestamise mõjuks.
- **Tulemused**: Kas oled kinnitanud peenhäälestamise eelised?
  - Kvaliteet — kas peenhäälestatud mudel ületas baasmudeli?
  - Kulu — kas see vähendab sümbolite kasutust, lihtsustades promte?
  - Laiendatavus — kas baasmudelit saab uutes valdkondades ümber kasutada?

Nendele küsimustele vastates peaksid suutma otsustada, kas peenhäälestamine on sinu kasutusjuhtumi jaoks õige lähenemine. Tähtis on, et see oleks mõistlik vaid juhul, kui eelised kaaluvad üles kulud. Kui otsustad jätkata, on aeg mõelda, _kuidas_ saad eelnevalt treenitud mudelit peenhäälestada.

Kas soovid rohkem teavet otsustusprotsessi kohta? Vaata videot [Peenhäälestada või mitte peenhäälestada](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Kuidas saab eelnevalt treenitud mudelit peenhäälestada?

Eelnevalt treenitud mudeli peenhäälestamiseks vajad:

- peenhäälestamiseks mõeldud eelnevalt treenitud mudelit
- peenhäälestamiseks kasutatavat andmestikku
- koolituskeskkonda peenhäälestustöö jooksutamiseks
- majutuskeskkonda peenhäälestatud mudeli juurutamiseks

## Peenhäälestamine Microsoft Foundrys

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) on koht, kus saad täna Azure'is peenhäälestada, juurutada ja hallata kohandatud mudeleid (see ühendab endas senised Azure OpenAI Studio ja Azure AI Studio platvormid). Enne töö alustamist on kasulik mõista Foundry poolt pakutavaid valikuid ja platvormi soovitatud parimaid tavasid. Foundry kasutab peenhäälestamiseks tõhusalt **LoRA-d (madala järgu kohandamist)**, mis hoiab koolituse kiire ja taskukohase, vältides kaalude täielikku ümberõpetamist.

### 1. samm: vali koolitustehnika

Foundry toetab kolme peenhäälestustehnikat. **Alusta SFT-st** — see hõlmab kõige laiemat olukordade spektrit.

| Tehnika | Mida see teeb | Millal kasutada |
| --- | --- | --- |
| **Juhendatud peenhäälestus (SFT)** | Treenib sisendi/väljundi näidise paaride põhjal, nii et mudel õpib tootma soovitud vastuseid. | Enamiku ülesannete vaikimisi valik: domeeni spetsialiseerumine, ülesande tulemuslikkus, stiil ja toon, juhiste järgimine ja keelega kohanemine. |
| **Otsene eelistusoptimeerimine (DPO)** | Õpib _eelistatud vs mitte-eelistatud_ vastusepaaride põhjal, et joondada väljundid inimeste eelistustega. | Vastuste kvaliteedi, ohutuse ja vastavuse parandamine, kui on olemas võrdlev tagasiside. |
| **Tugevdusõppel põhinev peenhäälestus (RFT)** | Kasutab _hindajate_ tasustamissignaale keerukate käitumiste optimeerimiseks tugevdusõppe kaudu. | Eesmärgipõhised, loogiliselt nõudlikud valdkonnad (matemaatika, keemia, füüsika) koos selgete õigete/valede vastustega. Vajab rohkem masinõppe ekspertiisi. |

### 2. samm: vali koolitustase

Foundry võimaldab valida, kuidas ja kus koolitus toimub:

- **Standard** — koolitab sinu ressursi regiooni piires ning tagab andmete asukohatõusu. Kasuta, kui andmed peavad jääma kindlasse regiooni.
- **Globaalne** — odavam ja kiirem järjekorda panna, kasutades ressursse väljaspool sinu regiooni (andmed ja kaalud kopeeritakse koolitusregiooni). Hea vaikimisi valik, kui andmete asukoht pole piiratud.
- **Arendaja** — madalaim hind, kasutades seisvaid ressursside mahtu ilma latentsuse/SLA garantiita (töid võidakse peatada ja jätkata). Ideaalne eksperimenteerimiseks.

### 3. samm: vali baas mudel

Peenhäälestatavad mudelid hõlmavad OpenAI `gpt-4o-mini`, `gpt-4o`, `gpt-4.1`, `gpt-4.1-mini` ja `gpt-4.1-nano` (SFT; 4o/4.1 perekond toetab ka DPO-d), mõtlemismudeleid `o4-mini` ja `gpt-5` (RFT), lisaks avatud lähtekoodiga mudeleid nagu `Ministral-3B`, `Qwen-32B`, `Llama-3.3-70B-Instruct` ja `gpt-oss-20b` (SFT Foundry ressurssidel). Kontrolli alati hetke [peenhäälestatavate mudelite loendit](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) toetatud meetodite, regioonide ja saadavuse osas.

> Foundry pakub kahte modaalust: **serverita** (tarbimisepõhine hinnakujundus, GPU kvoote hallata pole, OpenAI ja valitud mudelid) ja **hallatud arvutus** (oma VMi kasutamine Azure Machine Learningu kaudu kõige laiema mudelivaliku jaoks). Enamik kasutajaid peaks alustama serveritaga.

### Foundry parimad tavad

- **Alusta baasmudelist.** Mõõda baasmudelit promptide inseneritöö ja RAG abil _enne_ peenhäälestamist, et tõestada parandust.
- **Alusta väikesest ja suurenda.** Alusta 50–100 kvaliteetse näitega lähenemise valideerimiseks, kasvata seejärel tootmises 500+ näiteni. Kvaliteet loeb rohkem kui kvantiteet — lõika madala kvaliteediga näited välja.
- **Formateeri andmed õigesti.** Koolitus- ja valideerimisfailid peavad olema JSONL-vormingus, UTF-8 **BOM-iga**, kuni 512 MB, kasutades jutuvastusformaati. Sisalda alati valideerimisfail, et jälgida ületreenimist.
- **Hoia koolitussüsteemi prompti inferentsi ajal.** Kasuta sama süsteemisõnumit mudeli kutsumisel, mida kasutati koolitamisel.
- **Hinda kontrollpunkte — ära paigalda pimesi viimast.** Foundry hoiab viimased kolm epohhi paigaldusvalmis kontrollpunktidena; vali see, mis üldistab kõige paremini, jälgides `train_loss` / `valid_loss` ja sümbolite täpsust.
- **Mõõda tokeni kulu koos kvaliteediga** peenhäälestatud mudelit võrreldes baasmudeliga.
- **Itereeri pideva peenhäälestamisega.** Võid peenhäälestada juba peenhäälestatud mudelit uute andmetega (toetatud OpenAI mudelite puhul).
- **Jälgi majutuskulusid.** Juurutatud kohandatud mudel arveldab tundide kaupa ning kasutamata juurutus eemaldatakse 15 päeva möödumisel — puhasta, mida ei vaja.

Läbi kogu protsessi samm-sammult juhendi [Mudeli kohandamine peenhäälestamisega](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst), ning vaata juhendeid [DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst) ja [RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst) puhul, kui oled valmis teiste tehnikate jaoks.

## Peenhäälestamine praktikas

Järgmised ressursid pakuvad samm-sammulisi õpetusi, mis juhatavad läbi reaalse näite hetkel toetatud mudelil koos hoolikalt valitud andmestikuga. Nende kasutamiseks vajad konkreetse pakkuja kontot ning juurdepääsu vastavatele mudelitele ja andmestikele.

| Pakkuja     | Õpetus                                                                                                                                                                       | Kirjeldus                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Kuidas peenhäälestada jutumudeleid](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Õpi peenhäälestama hiljutist OpenAI jutumudelit kindla domeeni („retsepti assistent“) jaoks, ettevalmistades koolitusandmeid, käivitades peenhäälestustöö ja kasutades peenhäälestatud mudelit inferentsiks.                                                                                                                                                                                                                                              |
| Microsoft Foundry | [Kohanda mudelit peenhäälestusega](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Õpi peenhäälestama hetkel toetatud mudelit nagu `gpt-4.1-mini` **Azure'is** Microsoft Foundry abil: valmista ette ja lae üles koolitus- ja valideerimisandmed, käivita peenhäälestustöö, seejärel juuruta ja kasuta uut mudelit.                                                                                                                                                                                                                                                                 |

| Hugging Face | [LLM-ide peentuneerimine Hugging Face’iga](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | See blogipostitus juhendab sind, kuidas peentuneerida _avatud LLM-i_ (nt `CodeLlama 7B`) kasutades [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) raamatukogu & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) koos avatud [andmestikega](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) Hugging Face’is. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [LLM-ide peentuneerimine AutoTrain’iga](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (või AutoTrain Advanced) on Hugging Face’i poolt arendatud Python’i raamatukogu, mis võimaldab peentuneerida paljude erinevate ülesannete jaoks, sealhulgas LLM-i peentuneerimine. AutoTrain on ilma koodita lahendus ja peentuneerimist saab teha omaenda pilves, Hugging Face Spaces’is või lokaalselt. Toetab nii veebipõhist GUI-d, CLI-d kui ka koolitust yaml konfiguratsioonifailide kaudu.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [LLM-ide peentuneerimine Unsloth’iga](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth on avatud lähtekoodiga raamistik, mis toetab LLM-i peentuneerimist ja tugevdusõpet (RL). Unsloth lihtsustab kohalikku koolitust, hindamist ja kasutuselevõttu kasutusvalmis [märkmetega](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). See toetab ka tekstist kõneks (TTS), BERT-i ja multimodaalseid mudeleid. Alustamiseks loe nende samm-sammult juhendit [LLM-ide peentuneerimise juhend](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Ülesanne

Vali üks ülalmainitud õpetustest ja läbitööta see. _Võime siin repos dubleerida nende õpetuste versiooni Jupyter Märkmikes ainult viitamiseks. Palun kasuta värskeimate versioonide saamiseks otseseid originaallähteid_.

## Suurepärane töö! Jätka õppimist.

Pärast selle õppetunni lõpetamist, vaata meie [Generatiivse tehisintellekti õppematerjalide kogu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), et jätkata oma generatiivse tehisintellekti teadmiste taseme tõstmist!

Palju õnne!! Sa oled lõpetanud selle kursuse v2-seeria viimase õppetunni! Ära lõpeta õppimist ja loomist. \*\*Vaata [RESSURSSE](RESSOURCES.md?WT.mc_id=academic-105485-koreyst), kus on nimekiri täiendavatest soovitustest just selle teema kohta.

Meie v1-seeria õppetunde on samuti täiustatud uute ülesannete ja mõistetega. Võta hetk, et värskendada oma teadmisi – ja palun [jaga oma küsimusi ja tagasisidet](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst), et aidata meil neid õppetunde kogukonna jaoks paremaks muuta.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->