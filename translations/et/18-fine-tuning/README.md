<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3772dcd23a98e2010f53ce8b9c583631",
  "translation_date": "2026-01-18T19:40:40+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "et"
}
-->
[![Open Source Models](../../../../../translated_images/et/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Oma LLM-i peenhäälestamine

Suure keelemudelite kasutamine generatiivsete tehisintellekti rakenduste loomiseks toob kaasa uusi väljakutseid. Üks peamisi küsimusi on tagada mudeli poolt kasutaja päringule genereeritud sisu vastuste kvaliteet (täpsus ja asjakohasus). Eelnevates õppetundides käsitlesime tehnikaid nagu promptide inseneritöö ja otsingupõhine generatsioon, mis püüavad seda probleemi lahendada _muutes mudelile sisestatavat prompti_.

Selles õppetunnis arutleme kolmandat tehnikat, **peenhäälestamist**, mis püüab väljakutse lahendada _mudeli enda ümberõppe_ abil täiendava andmestiku peal. Süveneme detailidesse.

## Õpieesmärgid

See õppetund tutvustab etteõpetatud keelemudelite peenhäälestamise mõistet, uurib selle lähenemise eeliseid ja väljakutseid ning annab juhiseid, millal ja kuidas kasutada peenhäälestamist oma generatiivse tehisintellekti mudelite jõudluse parandamiseks.

Selle õppetunni lõpuks peaksid sa oskama vastata järgmistele küsimustele:

- Mis on keelemudelite peenhäälestamine?
- Millal ja miks on peenhäälestamine kasulik?
- Kuidas saan etteõpetatud mudelit peenhäälestada?
- Millised on peenhäälestamise piirangud?

Valmis? Alustame.

## Joonistatud juhend

Tahad saada ülevaadet sellest, mida me õppetunni jooksul käsitleme, enne kui põhjalikumalt süveneme? Vaatle seda joonistatud juhendit, mis kirjeldab õppeprotsessi sellest õppetunnist – alustades peenhäälestamise põhimõtetest ja motiivist kuni protsessi ja parimate tavade mõistmiseni peenhäälestamise ülesande läbiviimisel. See on põnev uurimisvaldkond, nii et ära unusta vaadata ka [ressursside](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) lehte lisalinkide saamiseks iseseisva õppimise toetuseks!

![Illustrated Guide to Fine Tuning Language Models](../../../../../translated_images/et/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Mis on keelemudelite peenhäälestamine?

Sõna otseses mõttes on suured keelemudelid _etteõpetatud_ suurte koguste tekstiga, mis pärineb erinevatest allikatest, sealhulgas internetist. Nagu oleme eelnevates tundides õppinud, vajame me selliseid tehnikaid nagu _promptide inseneritöö_ ja _otsingupõhine generatsioon_, et parandada mudeli vastuste kvaliteeti kasutaja küsimustele („promptidele“).

Populaarne promptide inseneritöö tehnika on anda mudelile rohkem juhiseid selle kohta, mida vastuses oodatakse, kas jagades _juhiseid_ (selgeid suuniseid) või _andmata mõned näited_ (kaudsed suunised). Seda nimetatakse _väheste näidete õppimiseks (few-shot learning)_, kuid see on kahe piiranguga:

- Mudeli tokeni limiidid võivad piirata näidete arvu, mida saad anda, ning vähendada efektiivsust.
- Mudeli tokenite kulud võivad muuta näidete lisamise igale promptile kulukaks ning piirata paindlikkust.

Peenhäälestamine on masinõppes tavapärane praktika, kus võetakse etteõpetatud mudel ja tehakse see uuesti väljaõpetatud uue andmestiku peal, et parandada selle jõudlust konkreetse ülesande täitmisel. Keelemudelite kontekstis saame peenhäälestada etteõpetatud mudeli _hoolikalt valitud näidiste komplektiga antud ülesande või rakenduse valdkonna jaoks_, et luua **kohandatud mudel**, mis võib olla täpsem ja asjakohasem just selle konkreetse ülesande või valdkonna jaoks. Peenhäälestamise kõrvaline kasu on ka see, et see võib vähendada väheste näidete õppimiseks vajalike näidete arvu – vähendades tokeni kasutust ja sellega seotud kulusid.

## Millal ja miks peaksime malle peenhäälestama?

_Just_ siin kontekstis, kui räägime peenhäälestamisest, viitame me **juhendatud** peenhäälestamisele, kus ümberõpe toimub **uue andmestiku lisamisega**, mis ei kuulunud algse treeningandmestiku hulka. See erineb juhendamata peenhäälestamisest, kus mudelit koolitatakse ümber algandmete peal, kuid erinevate hüperparameetritega.

Oluline on meeles pidada, et peenhäälestamine on täiustatud tehnika, mis vajab eduka tulemuse saamiseks teatud oskustaset. Kui seda tehakse valesti, ei pruugi see anda oodatud paranemist ning võib isegi mudeli jõudlust sihtrakenduse valdkonnas halvendada.

Seega, enne kui õpid, "kuidas" keelemudeleid peenhäälestada, pead teadma, "miks" valida see tee ja "millal" alustada peenhäälestamise protsessiga. Alusta nende küsimuste esitamisest endale:

- **Kasutusjuhtum**: Mis on sinu _kasutusjuhtum_ peenhäälestamiseks? Millist mudeli omadust soovid parandada?
- **Alternatiivid**: Kas oled proovinud _teisi tehnikaid_ soovitud tulemuste saavutamiseks? Kasuta neid võrdluspõhja loomiseks.
  - Promptide inseneritöö: Proovi väheste näidete meetodit, lisades asjakohaseid näiteid promptide vastustest. Hinda vastuste kvaliteeti.
  - Otsingupõhine generatsioon: Katseta promptide täiendamist otsingupäringutest saadud tulemustega. Hinda vastuste kvaliteeti.
- **Kulud**: Kas oled määratlenud peenhäälestamise kulud?
  - Häälestatavus – kas etteõpetatud mudel on peenhäälestamiseks saadaval?
  - Pingutus – treeningandmete ettevalmistamine, mudeli hindamine ja täiustamine
  - Arvutusvõimsus – peenhäälestamise tööde käivitamine ja peenhäälestatud mudeli juurutamine
  - Andmed – juurdepääs piisava kvaliteediga näidetele peenhäälestuse mõju saavutamiseks
- **Kasud**: Kas oled kinnitanud peenhäälestamise eelised?
  - Kvaliteet – kas peenhäälestatud mudel ületas võrdluspõhja?
  - Kulud – kas see vähendab tokenite kasutust, lihtsustades promptide struktuuri?
  - Laiendatavus – kas baasmodeli saab taaskasutada uutes valdkondades?

Nendele küsimustele vastates peaksid oskama otsustada, kas peenhäälestamine on sinu kasutusjuhtumi jaoks õige lähenemine. Kõige parem on valida selline lahendus, kus eelised kaaluvad üles kulud. Kui oled otsustanud jätkata, on aeg mõelda, _kuidas_ peenhäälestada etteõpetatud mudelit.

Soovid rohkem teadmisi otsustusprotsessi kohta? Vaata [To fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Kuidas peenhäälestada etteõpetatud mudelit?

Peenhäälestamiseks vajad:

- peenhäälestamiseks etteõpetatud mudelit
- andmestikku peenhäälestamiseks
- treeningkeskkonda peenhäälestamise töö käivitamiseks
- majutuskeskkonda peenhäälestatud mudeli juurutamiseks

## Peenhäälestamine praktikas

Järgmised ressursid annavad samm-sammult juhised reaalse näite jaoks, kasutades valitud mudelit ja hoolikalt koostatud andmestikku. Nende õpetustega töötamiseks vajad vastava teenusepakkuja kontot ning juurdepääsu mudelile ja andmestikule.

| Pakkuja     | Õpetus                                                                                                                                                                        | Kirjeldus                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI      | [How to fine-tune chat models](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)               | Õpi peenhäälestama mudelit `gpt-35-turbo` konkreetseks valdkonnaks („retsepti assistent“) koolitusandmete ettevalmistamise, peenhäälestamise töö teostamise ja peenhäälestatud mudeli kasutamise kaudu järelduste tegemiseks.                                                                                                                                                                                                        |
| Azure OpenAI| [GPT 3.5 Turbo fine-tuning tutorial](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Õpi peenhäälestama mudelit `gpt-35-turbo-0613` **Azure'i platvormil**: loo ja laadi üles koolitusandmed, käivita peenhäälestamise töö, deployeri ning kasuta uut mudelit.                                                                                                                                                                                                                                                      |
| Hugging Face| [Fine-tuning LLMs with Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                              | See blogipostitus juhendab sind peenhäälestama _avatud LLM-i_ (nt `CodeLlama 7B`) [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) teeki ja [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) abil, kasutades avatud [andmestikke](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) Hugging Face’is. |
|             |                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 🤗 AutoTrain| [Fine-tuning LLMs with AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                        | AutoTrain (või AutoTrain Advanced) on Hugging Face’i poolt välja töötatud Python'i teek, mis võimaldab peenhäälestamist paljude erinevate ülesannete jaoks, sealhulgas LLM peenhäälestamine. AutoTrain on koodivaba lahendus ja peenhäälestamist saab teostada oma pilves, Hugging Face Spaces’is või lokaalselt. Toetab nii veebiliidest, käsurea liidest kui koolitust yaml konfiguratsioonifailide abil.                                                                               |
|             |                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 🦥 Unsloth  | [Fine-tuning LLMs with Unsloth](https://github.com/unslothai/unsloth)                                                                                                        | Unsloth on avatud lähtekoodiga raamistik, mis toetab LLM-i peenhäälestamist ja tugevdusõpet (RL). Unsloth lihtsustab kohaliku treeningu, hindamise ja juurutamise protsessi kättevalmis [notebook'ite](https://github.com/unslothai/notebooks) abil. Samuti toetab teksti kõneks teisendust (TTS), BERT-i ja multimodaalseid mudeleid. Alustamiseks loe nende samm-sammult juhendit [Fine-tuning LLMs Guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).             |
|             |                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                 |
## Kodutöö

Vali üks ülaltoodud õpetustest ja läbi selle samm-sammult. _Võimalik, et kopeerime nende õpetuste versiooni Jupyter Notebooki faili sellesse hoidla, ainult viidetena. Palun kasuta otse algallikaid, et saada viimased versioonid_.

## Väga hea töö! Jätka õppimist.

Pärast selle õppetunni lõpetamist vaata meie [Generative AI õppimiskogu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), et jätkata oma generatiivse tehisintellekti teadmiste süvendamist!

Palju õnne!! Sa oled lõpetanud selle kursuse v2 sari viimasel õppetunnil! Ära peatu õppimast ja ehitamast. \*\*Vaata [RESSURSID](RESOURCES.md?WT.mc_id=academic-105485-koreyst) lehte selle teema kohta lisasoovituste saamiseks.

Meie v1 õppetundide sari on samuti uuendatud rohkemate kodutööde ja mõistetega. Võta hetk aega oma teadmiste värskendamiseks – ja palun [jaga oma küsimusi ja tagasisidet](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst), et aidata meil neid õppetunde kogukonna jaoks paremaks muuta.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:  
See dokument on tõlgitud tehisintellekti tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi me püüame tagada täpsust, palun pidage meeles, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Tähtsa teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tingitud arusaamatuste ega vale tõlgenduste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->