<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b9d32511b27373a1b21b5789d4fda057",
  "translation_date": "2025-10-18T02:28:26+00:00",
  "source_file": "14-the-generative-ai-application-lifecycle/README.md",
  "language_code": "lt"
}
-->
[![Integracija su funkcijų kvietimu](../../../translated_images/14-lesson-banner.066d74a31727ac121eeac06376a068a397d8e335281e63ce94130d11f516e46b.lt.png)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Generatyviosios dirbtinio intelekto programos gyvavimo ciklas

Svarbus klausimas visoms dirbtinio intelekto programoms yra AI funkcijų aktualumas, nes dirbtinio intelekto sritis sparčiai vystosi. Kad jūsų programa išliktų aktuali, patikima ir tvirta, būtina ją nuolat stebėti, vertinti ir tobulinti. Čia ir pasitarnauja generatyviosios dirbtinio intelekto gyvavimo ciklas.

Generatyviosios dirbtinio intelekto gyvavimo ciklas yra struktūra, kuri padeda jums pereiti per generatyviosios dirbtinio intelekto programos kūrimo, diegimo ir palaikymo etapus. Jis padeda apibrėžti tikslus, įvertinti našumą, nustatyti iššūkius ir įgyvendinti sprendimus. Taip pat padeda suderinti jūsų programą su etiniais ir teisiniais jūsų srities bei suinteresuotųjų šalių standartais. Laikydamiesi generatyviosios dirbtinio intelekto gyvavimo ciklo, galite užtikrinti, kad jūsų programa visada teiktų vertę ir patenkintų vartotojų poreikius.

## Įvadas

Šiame skyriuje jūs:

- Suprasite paradigmos pokytį nuo MLOps iki LLMOps
- LLM gyvavimo ciklą
- Gyvavimo ciklo įrankius
- Gyvavimo ciklo metrikaciją ir vertinimą

## Supraskite paradigmos pokytį nuo MLOps iki LLMOps

LLM yra naujas įrankis dirbtinio intelekto arsenale, kuris yra nepaprastai galingas analizei ir generavimo užduotims atlikti programose. Tačiau šis galingumas turi tam tikrų pasekmių, kaip mes optimizuojame dirbtinio intelekto ir klasikinio mašininio mokymosi užduotis.

Dėl to mums reikia naujos paradigmos, kad galėtume pritaikyti šį įrankį dinamiškai, su tinkamais paskatinimais. Senesnes dirbtinio intelekto programas galime kategorizuoti kaip "ML programas", o naujesnes dirbtinio intelekto programas kaip "GenAI programas" arba tiesiog "AI programas", atspindint pagrindines tuo metu naudojamas technologijas ir metodus. Tai keičia mūsų požiūrį įvairiais būdais, pažvelkite į šį palyginimą.

![LLMOps ir MLOps palyginimas](../../../translated_images/01-llmops-shift.29bc933cb3bb0080a562e1655c0c719b71a72c3be6252d5c564b7f598987e602.lt.png)

Pastebėkite, kad LLMOps labiau orientuojasi į programų kūrėjus, naudojant integracijas kaip pagrindinį tašką, naudojant "Modelius kaip paslaugą" ir galvojant apie šiuos metrikos punktus:

- Kokybė: Atsakymų kokybė
- Žala: Atsakingas dirbtinis intelektas
- Sąžiningumas: Atsakymų pagrįstumas (Ar tai logiška? Ar tai teisinga?)
- Kaina: Sprendimo biudžetas
- Vėlavimas: Vidutinis laikas atsakymui į žetoną

## LLM gyvavimo ciklas

Pirmiausia, norint suprasti gyvavimo ciklą ir jo pakeitimus, pažvelkime į šią infografiką.

![LLMOps infografika](../../../translated_images/02-llmops.70a942ead05a7645db740f68727d90160cb438ab71f0fb20548bc7fe5cad83ff.lt.png)

Kaip galite pastebėti, tai skiriasi nuo įprastų MLOps gyvavimo ciklų. LLM turi daug naujų reikalavimų, tokių kaip užklausų kūrimas, skirtingos technikos kokybei gerinti (Fine-Tuning, RAG, Meta-Prompts), skirtingas vertinimas ir atsakomybė su atsakingu dirbtiniu intelektu, galiausiai naujos vertinimo metrikos (Kokybė, Žala, Sąžiningumas, Kaina ir Vėlavimas).

Pavyzdžiui, pažvelkite, kaip mes generuojame idėjas. Naudojame užklausų inžineriją, kad eksperimentuotume su įvairiais LLM ir tyrinėtume galimybes, ar jų hipotezės gali būti teisingos.

Atkreipkite dėmesį, kad tai nėra linijinis procesas, o integruoti ciklai, iteratyvūs ir apimantys bendrą ciklą.

Kaip galėtume išnagrinėti šiuos žingsnius? Pažvelkime į detales, kaip galėtume sukurti gyvavimo ciklą.

![LLMOps darbo eiga](../../../translated_images/03-llm-stage-flows.3a1e1c401235a6cfa886ed6ba04aa52a096a545e1bc44fa54d7d5983a7201892.lt.png)

Tai gali atrodyti šiek tiek sudėtinga, pirmiausia susitelkime į tris pagrindinius žingsnius.

1. Idėjų generavimas/tyrimas: Tyrinėjimas, čia galime tyrinėti pagal mūsų verslo poreikius. Prototipų kūrimas, [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) kūrimas ir testavimas, ar jis pakankamai efektyvus mūsų hipotezei.
2. Kūrimas/tobulinimas: Įgyvendinimas, dabar pradedame vertinti didesnius duomenų rinkinius, taikyti technikas, tokias kaip Fine-tuning ir RAG, kad patikrintume mūsų sprendimo tvirtumą. Jei jis neveikia, perkurti jį, pridėti naujus žingsnius į mūsų eigą arba pertvarkyti duomenis gali padėti. Po to, kai išbandome savo eigą ir mastą, jei tai veikia ir atitinka mūsų metriką, jis pasiruošęs kitam žingsniui.
3. Operatyvinimas: Integracija, dabar pridedame stebėjimo ir įspėjimo sistemas į mūsų sistemą, diegiame ir integruojame programą į mūsų taikomąją programą.

Tada turime bendrą valdymo ciklą, orientuotą į saugumą, atitiktį ir valdymą.

Sveikiname, dabar jūsų dirbtinio intelekto programa yra paruošta naudoti ir veikia. Norėdami praktiškai išbandyti, pažvelkite į [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

Dabar, kokius įrankius galėtume naudoti?

## Gyvavimo ciklo įrankiai

Kalbant apie įrankius, „Microsoft“ siūlo [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) ir [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst), kurie palengvina ir padaro jūsų ciklą lengvai įgyvendinamą bei paruoštą naudoti.

[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) leidžia naudoti [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys). AI Studio yra interneto portalas, leidžiantis tyrinėti modelius, pavyzdžius ir įrankius. Jis padeda valdyti jūsų išteklius, kurti vartotojo sąsajas ir naudoti SDK/CLI galimybes pirmiausia kodavimui.

![Azure AI galimybės](../../../translated_images/04-azure-ai-platform.80203baf03a12fa8b166e194928f057074843d1955177baf0f5b53d50d7b6153.lt.png)

„Azure AI“ leidžia naudoti įvairius išteklius, valdyti operacijas, paslaugas, projektus, vektorinę paiešką ir duomenų bazių poreikius.

![LLMOps su Azure AI](../../../translated_images/05-llm-azure-ai-prompt.a5ce85cdbb494bdf95420668e3464aae70d8b22275a744254e941dd5e73ae0d2.lt.png)

Kurkite nuo koncepcijos įrodymo (POC) iki didelio masto programų su PromptFlow:

- Kurkite ir plėtokite programas naudodami VS Code, vizualinius ir funkcinius įrankius
- Testuokite ir tobulinkite savo programas, kad pasiektumėte aukštos kokybės dirbtinį intelektą, lengvai.
- Naudokite Azure AI Studio integracijai ir iteracijai su debesimi, greitam integravimui ir diegimui.

![LLMOps su PromptFlow](../../../translated_images/06-llm-promptflow.a183eba07a3a7fdf4aa74db92a318b8cbbf4a608671f6b166216358d3203d8d4.lt.png)

## Puiku! Tęskite mokymąsi!

Nuostabu, dabar sužinokite daugiau apie tai, kaip mes struktūrizuojame programą, kad galėtume naudoti šias koncepcijas su [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), kad pamatytumėte, kaip „Cloud Advocacy“ pritaiko šias koncepcijas demonstracijose. Daugiau turinio rasite mūsų [Ignite breakout session!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Dabar peržiūrėkite 15 pamoką, kad suprastumėte, kaip [Retrieval Augmented Generation ir vektorinių duomenų bazės](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) daro įtaką generatyviajam dirbtiniam intelektui ir padeda kurti labiau įtraukiančias programas!

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, atsiradusius naudojant šį vertimą.