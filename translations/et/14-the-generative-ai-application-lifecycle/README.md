<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df44972d5575ea8cef3c52ee31696d04",
  "translation_date": "2025-12-19T18:07:45+00:00",
  "source_file": "14-the-generative-ai-application-lifecycle/README.md",
  "language_code": "et"
}
-->
[![Funktsioonikõnede integreerimine](../../../translated_images/et/14-lesson-banner.066d74a31727ac12.png)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Generatiivse tehisintellekti rakenduse elutsükkel

Kõigi tehisintellekti rakenduste jaoks on oluline küsimus AI funktsioonide asjakohasus, kuna AI on kiiresti arenev valdkond. Selleks, et teie rakendus jääks asjakohaseks, usaldusväärseks ja vastupidavaks, peate seda pidevalt jälgima, hindama ja parandama. Siin tuleb mängu generatiivse AI elutsükkel.

Generatiivse AI elutsükkel on raamistik, mis juhendab teid generatiivse AI rakenduse arendamise, juurutamise ja hooldamise etappides. See aitab teil määratleda oma eesmärgid, mõõta oma tulemuslikkust, tuvastada väljakutsed ja rakendada lahendusi. Samuti aitab see joondada teie rakenduse eetiliste ja õiguslike standarditega teie valdkonnas ja sidusrühmade seas. Järgides generatiivse AI elutsüklit, saate tagada, et teie rakendus pakub alati väärtust ja rahuldab kasutajaid.

## Sissejuhatus

Selles peatükis õpite:

- Mõistma paradigmanihket MLOps-ist LLMOps-i
- LLM elutsüklit
- Elutsükli tööriistu
- Elutsükli mõõdikuid ja hindamist

## Mõistma paradigmanihket MLOps-ist LLMOps-i

LLMid on uus tööriist tehisintellekti arsenalis, need on äärmiselt võimsad analüüsi- ja genereerimistöödel rakenduste jaoks, kuid see võimsus toob kaasa ka tagajärgi, kuidas me AI ja klassikalisi masinõppe ülesandeid sujuvamaks muudame.

Selleks vajame uut paradigmat, et seda tööriista dünaamiliselt kohandada õige stiimuli abil. Võime vanemaid AI rakendusi kategoriseerida kui "ML rakendused" ja uuemaid AI rakendusi kui "GenAI rakendused" või lihtsalt "AI rakendused", peegeldades tolleaegset peavoolutehnoloogiat ja -meetodeid. See nihutab meie narratiivi mitmel moel, vaadake järgmist võrdlust.

![LLMOps vs. MLOps võrdlus](../../../translated_images/et/01-llmops-shift.29bc933cb3bb0080.png)

Pange tähele, et LLMOps-is keskendume rohkem rakenduste arendajatele, kasutades integratsioone võtmetähtsusega punktina, kasutades "Mudelit teenusena" ja mõeldes järgmistele mõõdikutele.

- Kvaliteet: vastuse kvaliteet
- Kahju: vastutustundlik AI
- Ausus: vastuse põhjendatus (Kas see on mõistlik? Kas see on õige?)
- Kulu: lahenduse eelarve
- Latentsus: keskmine aeg tokeni vastuseks

## LLM elutsükkel

Esmalt, et mõista elutsüklit ja selle muudatusi, vaatame järgmist infograafikat.

![LLMOps infograafik](../../../translated_images/et/02-llmops.70a942ead05a7645.png)

Nagu võite märgata, erineb see tavapärastest MLOps elutsüklitest. LLMidel on palju uusi nõudeid, nagu promptimine, erinevad tehnikad kvaliteedi parandamiseks (peenhäälestamine, RAG, meta-promptid), erinev hindamine ja vastutus vastutustundliku AI raames ning lõpuks uued hindamismõõdikud (kvaliteet, kahju, ausus, kulu ja latentsus).

Näiteks vaadake, kuidas me ideid genereerime. Kasutades promptide inseneritehnikat, et katsetada erinevaid LLM-e ja uurida võimalusi, kas nende hüpotees võib olla õige.

Pange tähele, et see ei ole lineaarne, vaid integreeritud tsüklid, iteratiivne ja üleüldise tsükliga.

Kuidas saaksime neid samme uurida? Vaatame üksikasjalikumalt, kuidas elutsüklit üles ehitada.

![LLMOps töövoog](../../../translated_images/et/03-llm-stage-flows.3a1e1c401235a6cf.png)

See võib tunduda veidi keeruline, keskendume esmalt kolmele suurele etapile.

1. Ideede genereerimine/uurimine: Uurimine, siin saame uurida vastavalt oma ärivajadustele. Prototüüpimine, [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) loomine ja testimine, kas see on meie hüpoteesi jaoks piisavalt tõhus.
1. Ehitamine/täiendamine: Rakendamine, nüüd hakkame hindama suuremate andmekogumite jaoks, rakendades tehnikaid nagu peenhäälestamine ja RAG, et kontrollida meie lahenduse vastupidavust. Kui see ei toimi, võib aidata selle uuesti rakendamine, uute sammude lisamine meie voogu või andmete ümberstruktureerimine. Pärast voolu ja skaleerimise testimist, kui see töötab ja mõõdikud on korras, on see valmis järgmise sammu jaoks.
1. Operatsionaliseerimine: Integratsioon, nüüd lisades meie süsteemile jälgimise ja hoiatussüsteemid, juurutamine ja rakenduse integreerimine meie rakendusse.

Seejärel on meil üleüldine haldus tsükkel, keskendudes turvalisusele, vastavusele ja haldusele.

Palju õnne, nüüd on teie AI rakendus valmis ja töökorras. Käed-külge kogemuse saamiseks vaadake [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

Milliseid tööriistu saaksime nüüd kasutada?

## Elutsükli tööriistad

Tööriistade jaoks pakub Microsoft [Azure AI platvormi](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) ja [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst), mis hõlbustavad ja muudavad teie tsükli lihtsaks rakendamiseks ja kasutamiseks.

[Azure AI platvorm](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) võimaldab teil kasutada [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys). AI Studio on veebipõhine portaal, mis võimaldab teil uurida mudeleid, näidiseid ja tööriistu. Haldate oma ressursse, kasutajaliidese arendusvooge ning SDK/CLI valikuid koodipõhiseks arenduseks.

![Azure AI võimalused](../../../translated_images/et/04-azure-ai-platform.80203baf03a12fa8.png)

Azure AI võimaldab teil kasutada mitmeid ressursse oma operatsioonide, teenuste, projektide, vektorotsingu ja andmebaaside haldamiseks.

![LLMOps Azure AI-ga](../../../translated_images/et/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.png)

Ehitage alates kontseptsiooni tõestusest (POC) kuni suuremahuliste rakendusteni PromptFlow abil:

- Kujundage ja ehitage rakendusi VS Code'ist, kasutades visuaalseid ja funktsionaalseid tööriistu
- Testige ja peenhäälestage oma rakendusi kvaliteetse AI jaoks lihtsalt.
- Kasutage Azure AI Studio't pilvega integreerimiseks ja iteratsiooniks, kiireks integreerimiseks lükake ja juurutage.

![LLMOps PromptFlow-ga](../../../translated_images/et/06-llm-promptflow.a183eba07a3a7fdf.png)

## Suurepärane! Jätkake õppimist!

Vinge, nüüd õppige rohkem, kuidas me struktureerime rakendust, et kasutada kontseptsioone [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst) abil, et näha, kuidas Cloud Advocacy neid kontseptsioone demonstratsioonides lisab. Rohkem sisu leiate meie [Ignite breakout sessioonist!](https://www.youtube.com/watch?v=DdOylyrTOWg)

Nüüd vaadake 15. õppetundi, et mõista, kuidas [Retrieval Augmented Generation ja vektoriandmebaasid](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) mõjutavad generatiivset AI-d ja muudavad rakendused kaasahaaravamaks!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud kasutades tehisintellektil põhinevat tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->