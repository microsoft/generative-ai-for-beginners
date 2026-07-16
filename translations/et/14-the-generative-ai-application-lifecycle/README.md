[![Funktsioonikõne integratsioon](../../../translated_images/et/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Generatiivse tehisintellekti rakenduse elutsükkel

Kõigi tehisintellekti rakenduste oluline küsimus on tehisintellekti funktsioonide asjakohasus, kuna AI on kiiresti arenev valdkond. Selleks, et teie rakendus jääks asjakohaseks, usaldusväärseks ja vastupidavaks, peate seda pidevalt jälgima, hindama ja parendama. Siin tuleb mängu generatiivse tehisintellekti elutsükkel.

Generatiivse tehisintellekti elutsükkel on raamistik, mis juhendab teid generatiivse tehisintellekti rakenduse arendamise, juurutamise ja hooldamise etappidel. See aitab teil määratleda oma eesmärgid, mõõta tulemuslikkust, tuvastada väljakutsed ja rakendada lahendusi. Samuti aitab see joondada teie rakendust teie valdkonna ja sidusrühmade eetiliste ning juriidiliste standarditega. Järgides generatiivse tehisintellekti elutsüklit, saate tagada, et teie rakendus pakub alati väärtust ja rahuldab kasutajate vajadusi.

## Sissejuhatus

Selles peatükis saate:

- Mõista paradigmainet MLOpsi ja LLMOpsi vahel
- LLM-i elutsükkel
- Elutsükli tööriistad
- Elutsükli mõõdikute rakendamine ja hindamine

## Paradigma muutmise mõistmine MLOpsist LLMOpsini

LLM-id on uus tööriist tehisintellekti arsenalis, need on uskumatult võimsad analüüsi- ja genereerimistöödes rakenduste jaoks, kuid see jõud omab mõningaid tagajärgi sellele, kuidas sujuvalt teostada AI ja klassikalise masinõppe ülesandeid.

Selleks vajame uut paradigmat, et kohandada seda tööriista dünaamiliselt õigete stiimulitega. Saame vanemaid AI rakendusi kategoriseerida kui "ML rakendusi" ja uuemaid AI rakendusi kui "GenAI rakendusi" või lihtsalt "AI rakendusi", mis peegeldab sel ajal kasutatud mainstream tehnoloogiaid ja tehnikaid. See muudab meie narratiivi mitmel viisil, vaadake järgmist võrdlust.

![LLMOps võrreldes MLOpsiga](../../../translated_images/et/01-llmops-shift.29bc933cb3bb0080.webp)

Märkige, et LLMOpsis keskendume rohkem rakenduse arendajatele, kasutades integreerimisi võtmeaspektina, kasutades "mudelid teenusena" ja mõtlemisel järgmiste mõõdikute osas.

- Kvaliteet: Vastuse kvaliteet
- Kahju: Vastutustundlik AI
- Ausus: Vastuse põhjendatus (Kas see on loogiline? Kas see on õige?)
- Kulu: Lahenduse eelarve
- Latentsus: Keskmine aeg tokenizeeritud vastuse jaoks

## LLM-i elutsükkel

Esiteks, et mõista elutsüklit ja selle muudatusi, vaadake järgmist infograafikut.

![LLMOps infograafik](../../../translated_images/et/02-llmops.70a942ead05a7645.webp)

Nagu märkasite, erineb see tavapärasest MLOpsi elutsüklist. LLMidel on palju uusi nõudeid, nagu promptimine, erinevad kvaliteedig parandamise tehnikad (peenhäälestamine, RAG, meta-promptid), erinevad hindamis- ja vastutusaspektid vastutustundliku AI jaoks ning lõpuks uued hindamismõõdikud (kvaliteet, kahju, ausus, kulu ja latentsus).

Näiteks vaadake, kuidas me ideid tekitame. Kasutades promptimiseksinseneri tööriistu, eksperimenteerime erinevate LLMidega, et uurida võimalusi testida, kas nende hüpoteesid võivad olla õiged.

Märkige, et see ei ole lineaarne, vaid integreeritud silmused, iteratiivne ja üldine tsükkel.

Kuidas võiksime neid samme uurida? Sukeldugem üksikasjadesse, kuidas elutsüklit üles ehitada.

![LLMOps töövoog](../../../translated_images/et/03-llm-stage-flows.3a1e1c401235a6cf.webp)

See võib tunduda veidi keeruline, keskendume esmalt kolmele suurele sammule.

1. Ideede tekitamine/Uurimine: Uurimine, siin saame uurida vastavalt ärivajadustele. Prototüüpimine, luues [PromptFlow"](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) ja testides, kas see on meie hüpoteesi jaoks piisavalt tõhus.
1. Ehitamine/Lisandite lisamine: Teostamine, nüüd hakkame hindama suuremate andmestike korral ja rakendame tehnikaid nagu peenhäälestamine ja RAG, et kontrollida meie lahenduse vastupidavust. Kui see ei toimi, võib aidata ümberteostamine, uute sammude lisamine meie voogu või andmete ümberkorraldamine. Pärast voolu ja mastaabi testimist, kui see töötab ja vastab meie mõõdikutele, on see järgmise sammu jaoks valmis.
1. Oliineerimine: Integreerimine, nüüd lisame meie süsteemile monitooringu ja häiresüsteemid, juurutuse ja rakenduse integratsiooni meie rakendusesse.

Seejärel on meil halduse üleüldine tsükkel, keskendudes turvalisusele, vastavusele ja juhtimisele.

Palju õnne, teie AI rakendus on nüüd valmis ja töökorras. Praktikakogemuse saamiseks vaadake [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)

Nüüd, milliseid tööriistu saame kasutada?

## Elutsükli tööriistad

Tööriistade jaoks pakub Microsoft [Azure AI platvormi](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) ja [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst), mis muudavad teie tsükli hõlpsasti rakendatavaks ja valmis kasutamiseks.

[Azure AI platvorm](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) võimaldab teil kasutada [Microsoft Foundry't](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst). Microsoft Foundry (endine Azure AI Studio) on veebipõhine portaal, mis võimaldab teil uurida mudeleid, näidiseid ja tööriistu, hallata ressursse ning kasutada kasutajaliidese arendusvooge ning SDK/CLI valikuid kood-eesmärgipõhiseks arenduseks.

![Azure AI võimalused](../../../translated_images/et/04-azure-ai-platform.80203baf03a12fa8.webp)

Azure AI võimaldab teil kasutada mitmesuguseid ressursse, et hallata oma operatsioone, teenuseid, projekte, vektorotsinguid ja andmebaasinõudeid.

![LLMOps Azure AI-ga](../../../translated_images/et/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

Ehitage alates kontseptsiooni tõestusest (POC) kuni suuremahuliste rakendusteni PromptFlow abil:

- Kujundage ja ehitage rakendusi VS Code abil, kasutades visuaalseid ja funktsionaalseid tööriistu
- Testige ja peenhäälestage oma rakendusi kvaliteetse AI jaoks lihtsalt
- Kasutage Microsoft Foundry't pilvega integreerimiseks ja iteratiivsuseks, kiireks juurutamiseks ja integreerimiseks

![LLMOps koos PromptFlowga](../../../translated_images/et/06-llm-promptflow.a183eba07a3a7fdf.webp)

## Suurepärane! Jätkake oma õpinguid!

Hästi, nüüd õppige rohkem selle kohta, kuidas me struktuurime rakendust, et kasutada mõisteid [Contoso Chat rakenduses](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), et näha, kuidas pilvepropageerimine lisab neid mõisteid demonstratsioonidesse. Rohkem sisu leiate meie [Ignite breakout sessioonist!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Nüüd uurige 15. peatükki, et mõista, kuidas [otsingupõhine täiendav genereerimine ja vektorandmebaasid](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) mõjutavad generatiivset tehisintellekti ja muudavad rakendused kaasahaaravamaks!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->