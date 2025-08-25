<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "27a5347a5022d5ef0a72ab029b03526a",
  "translation_date": "2025-08-25T12:41:07+00:00",
  "source_file": "14-the-generative-ai-application-lifecycle/README.md",
  "language_code": "lt"
}
-->
[![Integravimas su funkcijų kvietimu](../../../translated_images/14-lesson-banner.066d74a31727ac121eeac06376a068a397d8e335281e63ce94130d11f516e46b.lt.png)](https://aka.ms/gen-ai-lesson14-gh?WT.mc_id=academic-105485-koreyst)

# Generatyvinės AI programos gyvavimo ciklas

Svarbus klausimas visoms AI programoms – AI funkcijų aktualumas, nes AI sritis sparčiai vystosi. Kad jūsų programa išliktų aktuali, patikima ir tvirta, ją reikia nuolat stebėti, vertinti ir tobulinti. Tam ir skirtas generatyvinės AI gyvavimo ciklas.

Generatyvinės AI gyvavimo ciklas – tai struktūra, padedanti pereiti visus generatyvinės AI programos kūrimo, diegimo ir palaikymo etapus. Ji padeda aiškiai apibrėžti tikslus, matuoti rezultatus, identifikuoti iššūkius ir įgyvendinti sprendimus. Taip pat padeda užtikrinti, kad programa atitiktų etinius ir teisės reikalavimus, taikomus jūsų sričiai ir suinteresuotoms šalims. Vadovaudamiesi generatyvinės AI gyvavimo ciklu, galite užtikrinti, kad jūsų programa nuolat teiktų vertę ir tenkintų vartotojų poreikius.

## Įvadas

Šiame skyriuje:

- Sužinosite apie paradigmos pokytį nuo MLOps prie LLMOps
- Susipažinsite su LLM gyvavimo ciklu
- Aptarsite gyvavimo ciklo įrankius
- Sužinosite apie gyvavimo ciklo metrikas ir vertinimą

## Supraskite paradigmos pokytį nuo MLOps prie LLMOps

LLM – tai naujas dirbtinio intelekto įrankis, itin galingas analizei ir generavimui programose, tačiau ši galia keičia, kaip optimizuojame AI ir klasikinio mašininio mokymosi užduotis.

Todėl reikia naujos paradigmos, kad šį įrankį galėtume pritaikyti dinamiškai ir su tinkamais paskatinimais. Senesnes AI programas galime vadinti „ML programomis“, o naujesnes – „GenAI programomis“ arba tiesiog „AI programomis“, atspindint naudojamas technologijas ir metodus. Tai keičia mūsų požiūrį įvairiais aspektais, pažiūrėkite į šį palyginimą.

![LLMOps ir MLOps palyginimas](../../../translated_images/01-llmops-shift.29bc933cb3bb0080a562e1655c0c719b71a72c3be6252d5c564b7f598987e602.lt.png)

Pastebėkite, kad LLMOps labiau orientuota į programų kūrėjus, integracijos tampa svarbia dalimi, naudojami „Modeliai kaip paslauga“, o metrikos apima šiuos aspektus:

- Kokybė: atsakymų kokybė
- Žala: atsakingas AI
- Sąžiningumas: atsakymų pagrįstumas (ar logiška? ar teisinga?)
- Kaina: sprendimo biudžetas
- Vėlavimas: vidutinis laikas iki atsakymo

## LLM gyvavimo ciklas

Norėdami suprasti gyvavimo ciklą ir jo pokyčius, pažiūrėkime į šią infografiką.

![LLMOps infografika](../../../translated_images/02-llmops.70a942ead05a7645db740f68727d90160cb438ab71f0fb20548bc7fe5cad83ff.lt.png)

Kaip matote, tai skiriasi nuo įprastų MLOps gyvavimo ciklų. LLM turi daug naujų reikalavimų: promptų kūrimas, įvairios kokybės gerinimo technikos (Fine-Tuning, RAG, Meta-Promptai), kitoks vertinimas ir atsakomybė už atsakingą AI, naujos vertinimo metrikos (kokybė, žala, sąžiningumas, kaina ir vėlavimas).

Pavyzdžiui, pažiūrėkite, kaip generuojame idėjas. Naudojame promptų inžineriją, eksperimentuojame su įvairiais LLM, kad išbandytume, ar mūsų hipotezė gali būti teisinga.

Atkreipkite dėmesį, kad tai nėra linijinis procesas, o integruoti, iteratyvūs ciklai.

Kaip galėtume išnagrinėti šiuos žingsnius? Pažvelkime detaliau, kaip galime sukurti gyvavimo ciklą.

![LLMOps darbo eiga](../../../translated_images/03-llm-stage-flows.3a1e1c401235a6cfa886ed6ba04aa52a096a545e1bc44fa54d7d5983a7201892.lt.png)

Tai gali atrodyti sudėtinga, todėl pirmiausia susitelkime į tris pagrindinius žingsnius.

1. Idėjų generavimas / tyrinėjimas: čia ieškome sprendimų pagal verslo poreikius. Prototipavimas, [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) kūrimas ir testavimas, ar tai efektyvu mūsų hipotezei.
1. Kūrimas / tobulinimas: įgyvendinimas, vertiname su didesniais duomenų rinkiniais, taikome technikas, tokias kaip Fine-tuning ir RAG, tikriname sprendimo tvirtumą. Jei neveikia, perdirbame, pridedame naujų žingsnių arba pertvarkome duomenis. Ištestavus srautą ir mastelį, jei veikia ir atitinka metrikas, pereiname prie kito etapo.
1. Operacionalizavimas: integracija, pridedame stebėsenos ir įspėjimų sistemas, diegiame ir integruojame programą.

Be to, yra bendras valdymo ciklas, orientuotas į saugumą, atitiktį ir valdymą.

Sveikiname, jūsų AI programa paruošta ir veikia! Norėdami išbandyti praktiškai, pažiūrėkite [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

Kokius įrankius galime naudoti?

## Gyvavimo ciklo įrankiai

Įrankiams Microsoft siūlo [Azure AI Platformą](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) ir [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst), kurie palengvina gyvavimo ciklo įgyvendinimą.

[Azure AI Platforma](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) leidžia naudoti [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys). AI Studio – tai interneto portalas, kuriame galite tyrinėti modelius, pavyzdžius ir įrankius. Valdyti resursus, kurti UI, naudoti SDK/CLI galimybes programuojant.

![Azure AI galimybės](../../../translated_images/04-azure-ai-platform.80203baf03a12fa8b166e194928f057074843d1955177baf0f5b53d50d7b6153.lt.png)

Azure AI leidžia naudoti įvairius resursus, valdyti operacijas, paslaugas, projektus, vektorinę paiešką ir duomenų bazes.

![LLMOps su Azure AI](../../../translated_images/05-llm-azure-ai-prompt.a5ce85cdbb494bdf95420668e3464aae70d8b22275a744254e941dd5e73ae0d2.lt.png)

Kurkite nuo Proof-of-Concept (POC) iki didelio masto programų su PromptFlow:

- Kurkite ir projektuokite programas iš VS Code, naudodami vizualius ir funkcinius įrankius
- Testuokite ir tobulinkite programas, kad AI būtų kokybiškas ir lengvai valdomas
- Naudokite Azure AI Studio integracijai ir iteracijai su debesimi, greitam diegimui

![LLMOps su PromptFlow](../../../translated_images/06-llm-promptflow.a183eba07a3a7fdf4aa74db92a318b8cbbf4a608671f6b166216358d3203d8d4.lt.png)

## Puiku! Tęskite mokymąsi!

Puiku, dabar sužinokite daugiau apie tai, kaip struktūruoti programą, kad galėtumėte pritaikyti šias koncepcijas su [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), ir pamatykite, kaip Cloud Advocacy demonstruoja šias idėjas. Daugiau turinio rasite mūsų [Ignite breakout sesijoje!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Dabar pereikite prie 15 pamokos, kad suprastumėte, kaip [Retrieval Augmented Generation ir vektorinės duomenų bazės](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) keičia generatyvinį AI ir padeda kurti įtraukiančias programas!

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už nesusipratimus ar neteisingą interpretaciją, kylančią dėl šio vertimo naudojimo.