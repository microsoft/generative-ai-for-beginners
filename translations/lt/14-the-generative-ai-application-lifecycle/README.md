[![Integracija su funkcijų kvietimu](../../../translated_images/lt/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Generatyvinio DI programos gyvavimo ciklas

Svarbus klausimas visoms DI programoms yra DI funkcijų aktualumas, kadangi DI yra greitai besivystanti sritis, norint užtikrinti, kad jūsų programa išliktų aktuali, patikima ir tvirta, reikia nuolat ją stebėti, vertinti ir tobulinti. Štai kur ateina generatyvinio DI gyvavimo ciklas.

Generatyvinio DI gyvavimo ciklas yra karkasas, kuris veda jus per generatyvinio DI programos kūrimo, diegimo ir palaikymo etapus. Jis padeda jums apibrėžti tikslus, matuoti našumą, nustatyti iššūkius ir įgyvendinti sprendimus. Taip pat padeda suderinti programą su jūsų srities ir suinteresuotųjų šalių etiniais bei teisės standartais. Sekdami generatyvinio DI gyvavimo ciklą, galite užtikrinti, kad jūsų programa visada teikia vertę ir tenkina vartotojus.

## Įvadas

Šiame skyriuje jūs:

- Suprasite perėjimą nuo MLOps prie LLMOps
- LLM gyvavimo ciklas
- Įrankiai gyvavimo ciklui
- Gyvavimo ciklo matavimai ir vertinimas

## Supraskite perėjimą nuo MLOps prie LLMOps

LLM yra naujas įrankis dirbtinio intelekto arsenale, jis yra nepaprastai galingas analizės ir generavimo užduotims programose atlikti, tačiau ši galia turi tam tikras pasekmes, kaip mes supaprastiname DI ir Klasikinio mašininio mokymosi užduotis.

Todėl mums reikia naujo paradigma, kad šis įrankis būtų pritaikytas dinamiškai, su tinkamais paskatinimais. Galime senesnes DI programas vadinti „ML programomis“, o naujesnes DI programas – „GenAI programomis“ arba tiesiog „DI programomis“, atspindinčiomis tuo metu naudojamas pagrindines technologijas ir metodikas. Tai keičia mūsų naratyvą keliais būdais, pažiūrėkite į šį palyginimą.

![LLMOps ir MLOps palyginimas](../../../translated_images/lt/01-llmops-shift.29bc933cb3bb0080.webp)

Pastebėkite, kad LLMOps labiau orientuojamės į programų kūrėjus, naudojant integracijas kaip pagrindinį tašką, „Modeliai kaip paslauga“ ir atsižvelgiant į šiuos metrikų aspektus.

- Kokybė: atsakymo kokybė
- Žala: atsakingas DI
- Sąžiningumas: atsakymo pagrįstumas (Ar tai prasminga? Ar tai teisinga?)
- Kaina: sprendimo biudžetas
- Vėlavimas: vidutinis laikas atsakymui pateikti

## LLM gyvavimo ciklas

Pirmiausia, kad suprastume gyvavimo ciklą ir jo modifikacijas, pažvelkime į šią infografiką.

![LLMOps infografikas](../../../translated_images/lt/02-llmops.70a942ead05a7645.webp)

Kaip matote, tai skiriasi nuo įprastų MLOps gyvavimo ciklų. LLM turi daug naujų reikalavimų, tokių kaip promptų naudojimas, įvairios kokybės gerinimo technikos (Fine-Tuning, RAG, Meta-Prompts), įvairus vertinimas ir atsakomybė su atsakingu DI, galiausiai – nauji vertinimo rodikliai (kokybė, žala, sąžiningumas, kaina ir vėlavimas).

Pavyzdžiui, pažiūrėkite, kaip mes kuriame idėjas. Naudodami promptų inžineriją, eksperimentuojame su įvairiais LLM, kad ištirtume galimybes patikrinti, ar jų hipotezė gali būti teisinga.

Atminkite, kad šis procesas nėra linijinis, o integruotas ciklas, iteratyvus ir su bendru ciklu.

Kaip galėtume ištirti šiuos žingsnius? Pažiūrėkime detaliau, kaip galėtume sukurti gyvavimo ciklą.

![LLMOps darbo eiga](../../../translated_images/lt/03-llm-stage-flows.3a1e1c401235a6cf.webp)

Tai gali atrodyti šiek tiek sudėtinga, pradėkime nuo trijų didelių žingsnių.

1. Idėjų kūrimas/tyrimas: čia galime tyrinėti pagal mūsų verslo poreikius. Prototipavimas, [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) kūrimas ir testavimas, ar pakankamai efektyvus mūsų hipotezei.
1. Kūrimas/plečimas: įgyvendinimas, dabar pradedame vertinti didesnius duomenų rinkinius, taikyti technikas, tokias kaip Fine-tuning ir RAG, patikrinti sprendimo tvirtumą. Jei neefektyvu, pertvarkymas, naujų žingsnių pridėjimas arba duomenų restruktūrizavimas gali padėti. Išbandžius srautą ir mastą, jei viskas veikia ir metrikos yra tinkamos, pasiruošta kitam žingsniui.
1. Eksploatavimas: integracija, dabar pridedame stebėjimo ir įspėjimų sistemas, diegimą ir programų integraciją į mūsų programą.

Tada turime bendrą valdymo ciklą, orientuotą į saugumą, atitiktį ir valdymą.

Sveikiname, dabar jūsų DI programa paruošta veikti. Praktiniam mokymuisi pažiūrėkite [Contoso Chat demonstraciją.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)

O kokius įrankius galime naudoti?

## Gyvavimo ciklo įrankiai

Įrankiams Microsoft teikia [Azure AI platformą](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) ir [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst), kurie palengvina ir padaro jūsų ciklo įgyvendinimą paprastą ir paruoštą naudoti.

[Azure AI platforma](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) leidžia naudotis [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst). Microsoft Foundry (anksčiau Azure AI Studio) yra žiniatinklio portalas, leidžiantis tyrinėti modelius, pavyzdžius ir įrankius, valdyti išteklius, naudoti vartotojo sąsajos kūrimo eigas bei SDK/CLI parinktis kodo pirmojo kūrimo atvejais.

![Azure AI galimybės](../../../translated_images/lt/04-azure-ai-platform.80203baf03a12fa8.webp)

Azure AI leidžia naudoti įvairius išteklius, valdyti operacijas, paslaugas, projektus, vektorinės paieškos ir duomenų bazių poreikius.

![LLMOps su Azure AI](../../../translated_images/lt/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

Kurkite nuo įrodymo koncepcijos (POC) iki didelio masto programų su PromptFlow:

- Projektuokite ir kurkite programas iš VS Code, naudodami vizualinius ir funkciškai įrankius
- Testuokite ir tobulinkite programas dėl kokybiško DI, lengvai.
- Naudokite Microsoft Foundry integracijai ir iteracijai su debesija, Push ir diegimui greitai integracijai.

![LLMOps su PromptFlow](../../../translated_images/lt/06-llm-promptflow.a183eba07a3a7fdf.webp)

## Puiku! Tęskite mokymąsi!

Nuostabu, dabar sužinokite daugiau, kaip struktūruojame programą, kad naudotumėte šias sąvokas su [Contoso Chat programa](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), kad pamatytumėte, kaip Cloud Advocacy įtraukia tas sąvokas demonstracijose. Daugiau turinio galite rasti mūsų [Ignite pranešime!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Dabar peržiūrėkite 15-ąją pamoką, kad suprastumėte, kaip [Retrieval Augmented Generation ir vektorinės duomenų bazės](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) įtakoja generatyvinį DI ir leidžia kurti įdomesnes programas!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->