[![Avatud lähtekoodiga mudelid](../../../translated_images/et/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Oma LLM-i peenhäälestamine

Suurte keelemudelite kasutamine generatiivsete tehisintellekti rakenduste loomiseks toob kaasa uusi väljakutseid. Peamine küsimus on tagada mudeli poolt kasutajapäringu põhjal loodava sisu vastuste kvaliteet (täpsus ja asjakohasus). Eelnevates õppetundides rääkisime tehnikaid nagu promptide inseneriteadus ja päringupõhine generatsioon, mis püüavad probleemi lahendada, _muutes sisendprompti_ olemasolevale mudelile.

Tänases õppetükis käsitleme kolmandat tehnikat, **peenhäälestamist**, mis püüab väljakutsega toime tulla, _muddeli enda täiendkoolitusega_ lisanduvate andmete abil. Sukeldume üksikasjadesse.

## Õpieesmärgid

See õppetund tutvustab peenhäälestamise kontseptsiooni eelõpetatud keelemudelite jaoks, uurib selle lähenemise eeliseid ja väljakutseid ning annab juhiseid, millal ja kuidas peenhäälestust kasutada generatiivsete tehisintellekti mudelite jõudluse parandamiseks.

Selle õppetunni lõpuks peaksid olema võimelised vastama järgmistele küsimustele:

- Mis on peenhäälestus keelemudelite jaoks?
- Millal ja miks on peenhäälestus kasulik?
- Kuidas ma saan eelõpetatud mudelit peenhäälestada?
- Millised on peenhäälestuse piirangud?

Oled valmis? Alustame.

## Joonistatud juhend

Tahad saada ülevaadet, mida me käsitleme enne süvenemist? Vaata seda joonistatud juhendit, mis kirjeldab õppeprotsessi selle õppetunni jaoks – alates põhikontseptsioonide ja motivatsiooni õppimisest peenhäälestuse jaoks kuni protsessi ja parimate tavade mõistmiseni peenhäälestust teostades. See on põnev uurimisteema, nii et ära unusta vaadata [ressursse](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) täiendavate linkide saamiseks iseseisva õppimise toetamiseks!

![Illustratsioon peenhäälestusest keelemudelitele](../../../translated_images/et/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Mis on peenhäälestus keelemudelite jaoks?

Definitsiooni kohaselt on suured keelemudelid _eelõpetatud_ suurtes tekstikogustes, mis pärinevad mitmekesistest allikatest, sealhulgas internetist. Nagu oleme eelnevates õppetundides õppinud, vajame tehnikaid nagu _promptide inseneriteadus_ ja _päringupõhine generatsioon_, et parandada mudeli vastuste kvaliteeti kasutajate küsimustele ("promptidele").

Populaarne promptide inseneriteaduse tehnika hõlmab mudelile rohkem juhiseid selle kohta, mida vastuses oodatakse, kas siis pakkudes _juhiseid_ (selged juhendid) või _andmata mõned näited_ (kaudsed juhised). Seda nimetatakse _vähese proovi õppimiseks_ (few-shot learning), kuid sel on kaks piirangut:

- Mudeli tokeni piirangud võivad piirata antavate näidete arvu ja mõjuvust.
- Mudeli tokenite maksumus võib muuta iga prompti jaoks näidete lisamise kulukaks ja piirata paindlikkust.

Peenhäälestus on masinõppes levinud praktika, kus me võtame eelõpetatud mudeli ja koolitame seda uute andmetega uuesti, et parandada selle jõudlust konkreetsel ülesandel. Keelemudelite kontekstis saame eelõpetatud mudelit peenhäälestada _valiku näidetega antud ülesande või rakenduse domeeni jaoks_, et luua **kohandatud mudel**, mis võib olla täpsem ja asjakohasem nende konkreetsete ülesannete või domeenide jaoks. Peenhäälestuse kõrvaltootena võib see vähendada ka vajadust vähese proovi õppimise jaoks vajalike näidete arvu järele – vähendades tokeni kasutust ja sellega seotud kulusid.

## Millal ja miks peaksime mudeleid peenhäälestama?

_Selles_ kontekstis, kui räägime peenhäälestusest, siis peame silmas **juhendatud** peenhäälestust, kus koolitus toimub, lisades **uusandmeid**, mis ei olnud algses koolitusandmestikus. See erineb juhendamata peenhäälestusest, kus mudel koolitatakse ümber algandmete põhjal, kuid erinevate hüperparameetritega.

Peamine asi, mida meeles pidada, on see, et peenhäälestus on täiustatud tehnika, mis nõuab teatud tasemel ekspertiisi soovitud tulemuste saavutamiseks. Kui seda tehakse valesti, ei pruugi see tuua oodatud paranemisi ja võib isegi mudeli jõudlust teie suunatud domeenis halvendada.

Nii et enne kui õpid "kuidas" peenhäälestada keelemudeleid, pead teadma "miks" valida see tee ja "millal" alustada peenhäälestusprotsessi. Alusta nendest küsimustest:

- **Kasutusjuhtum**: Mis on sinu _kasutusjuhtum_ peenhäälestamiseks? Millist aspekti olemasolevast eelõpetatud mudelist soovid parandada?
- **Alternatiivid**: Kas oled katsetanud _teisi tehnikaid_, et saavutada soovitud tulemusi? Kasuta neid võrdlusbaasina.
  - Promptide inseneriteadus: Proovi tehnikaid nagu vähese proovi prompting koos vastavate promptivastuste näidetega. Hinda vastuste kvaliteeti.
  - Päringu põhine genereerimine: Proovi täiendada prompti päringu tulemustega, mida sa leidud oma andmetest. Hinda vastuste kvaliteeti.
- **Kulud**: Kas oled kindlaks teinud peenhäälestuse kulud?
  - Kohandatavus - kas eelõpetatud mudel on peenhäälestamiseks saadaval?
  - Pingutus - koolitusandmete ettevalmistamise, mudeli hindamise ja täiendamise pingutus.
  - Arvutusressursid - peenhäälestustööde käivitamiseks ja peenhäälestatud mudeli juurutamiseks vajalik ressursikasutus.
  - Andmed - juurdepääs piisava kvaliteediga näidetele peenhäälestuse mõju jaoks.
- **Eelised**: Kas oled kinnitanud peenhäälestuse eelised?
  - Kvaliteet - kas peenhäälestatud mudel ületas baasmudeli?
  - Kulu - kas see vähendab tokeni kasutust, lihtsustades prompti?
  - Laiendatavus - kas saad alusmudelit kasutada uutes domeenides?

Nendele küsimustele vastates peaksid suutma otsustada, kas peenhäälestus on sinu kasutusjuhtumi jaoks õige lähenemine. Ideaalis on lähenemine kehtiv ainult siis, kui eelised kaaluvad üles kulud. Kui otsustad jätkata, on aeg mõelda, _kuidas_ saad eelõpetatud mudelit peenhäälestada.

Kas soovid saada rohkem ülevaadet otsustusprotsessist? Vaata videot [Fine-häälestada või mitte fine-häälestada](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Kuidas saab eelõpetatud mudelit peenhäälestada?

Eelõpetatud mudeli peenhäälestamiseks vajad:

- peenhäälestamiseks eelõpetatud mudelit
- peenhäälestuseks kasutatavat andmestikku
- koolituskeskkonda peenhäälestuse töö käivitamiseks
- majutuskeskkonda peenhäälestatud mudeli juurutamiseks

## Peenhäälestus praktikas

> **Märkus:** `gpt-35-turbo` / `gpt-3.5-turbo`, mida mõnedes allpool toodud õpetustes viidatakse, on nii päringu tegemiseks kui peenhäälestamiseks pensionile saadetud. Kui alustad täna uut peenhäälestustööd, sihi mõnele praegusel ajal toetatavale mudelile – näiteks `gpt-4o-mini` või `gpt-4.1-mini`. Vaata [Peenhäälestatavate mudelite nimekirja](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) praeguse toetatud mudelite komplekti kohta. Nendes õpetustes toodud kontseptsioonid ja sammud kehtivad endiselt.

Järgmised ressursid pakuvad samm-sammult õpetusi, mis juhendavad sind läbi reaalse näite, kasutades valitud mudelit kureeritud andmestikuga. Nende õpetuste läbimiseks on sul vaja konkreetse teenusepakkuja kontot, koos juurdepääsuga vastavale mudelile ja andmestikule.

| Teenusepakkuja | Õpetus                                                                                                                                                                       | Kirjeldus                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Kuidas peenhäälestada vestluse mudeleid](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Õpi peenhäälestama `gpt-35-turbo` mudelit kindla domeeni (“retsepti assistent”) jaoks, valmistades ette koolitusandmestiku, käivitades peenhäälestuse töö ja kasutades peenhäälestatud mudelit päringutes.                                                                                                                                                                                                                                             |
| Azure OpenAI | [GPT 3.5 Turbo peenhäälestuse õpetus](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst) | Õpi peenhäälestama `gpt-35-turbo-0613` mudelit **Azure’is**, võttes samme koolitusandmete loomiseks & üleslaadimiseks, peenhäälestuse töö käivitamiseks. Juurutamiseks & uue mudeli kasutamiseks.                                                                                                                                                                                                                                                                 |
| Hugging Face | [Peenhäälestamine LLM-idega Hugging Face abil](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | See blogipostitus juhendab sind avatud LLM-i (näiteks `CodeLlama 7B`) peenhäälestamises kasutades [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) teeki ja [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) koos avatud [andmestikega](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) Hugging Face'is. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Peenhäälestamine LLM-idega AutoTrain’iga](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (või AutoTrain Advanced) on Hugging Face’i poolt arendatud Pythoni teek, mis võimaldab peenhäälestust mitmetel erinevatel ülesannetel, sealhulgas LLM-i peenhäälestust. AutoTrain on mittetöötluslahendus ja peenhäälestust saab teha oma pilves, Hugging Face Spaces’is või kohapeal. Toetab veebipõhist GUI-d, CLI-d ja koolitust yaml konfiguratsioonifailide kaudu.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Peenhäälestamine LLM-idega Unsloth’iga](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth on avatud lähtekoodiga raamistik, mis toetab LLM-i peenhäälestust ja tugevdamisõpet (RL). Unsloth lihtsustab kohalikku treeningut, hindamist ja juurutamist valmis kasutatavate [märkmikega](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Toetab ka teksti kõneks (TTS), BERT- ja multimodaalseid mudeleid. Alustamiseks loe nende samm-sammult [Peenhäälestamise juhendit](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Kodune ülesanne

Vali ülaltoodud õpetustest üks ja käi see läbi. _Võime kopeerida mõningaid neist õpetustest Jupyteri märkmikutesse selles repo’s ainult viitamiseks. Palun kasuta originaallinke, et saada uusimad versioonid_.

## Suurepärane töö! Jätka õppimist.

Pärast selle õppetunni lõpetamist vaata meie [Generatiivse tehisintellekti õppematerjalide kogumikku](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), et oma generatiivse tehisintellekti teadmisi veelgi täiendada!

Palju õnne!! Sa oled lõpetanud selle kursuse v2 sarja viimase õppetunni! Ära peatu õppimisel ja loomisel. \*\*Vaata [RESSURSSE](RESOURCES.md?WT.mc_id=academic-105485-koreyst) lehte, kus on toodud täiendavaid soovitusi just selle teema kohta.

Meie v1 õppetundide sari on samuti uuendatud, lisades rohkem ülesandeid ja kontseptsioone. Võta hetk, et oma teadmisi värskendada – ja palun [jaga oma küsimusi ja tagasisidet](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst), et aidata meil neid õppetunde kogukonnale parandada.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->