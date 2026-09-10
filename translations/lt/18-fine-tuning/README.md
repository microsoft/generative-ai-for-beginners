[![Atviro kodo modeliai](../../../translated_images/lt/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Didžiųjų kalbų modelių (LLM) smulkus perdavimas

Naudojant didelius kalbos modelius generatyvių DI programėlių kūrimui kyla naujų iššūkių. Pagrindinė problema yra užtikrinti atsakymų kokybę (tikslumą ir aktualumą) generuojant turinį pagal vartotojo užklausą. Ankstesnėse pamokose aptarėme tokias technikas kaip užklausų inžinerija ir paiešką integruojančią generaciją, kurios bando spręsti šią problemą _keitimo užklausos įvestį_ esamam modeliui.

Šios pamokos metu aptarsime trečią metodą, **smulkų perdavimą** (fine-tuning), kuris bando išspręsti iššūkį _permokant patį modelį_ su papildomais duomenimis. Panagrinėkime detales.

## Mokymosi tikslai

Ši pamoka pristato smulkaus perdavimo sąvoką išankstiniuose kalbos modeliuose, nagrinėja šio metodo privalumus ir iššūkius bei teikia rekomendacijas, kada ir kaip naudoti smulkų perdavimą generatyvių DI modelių veiklos gerinimui.

Pamokos pabaigoje turėtumėte sugebėti atsakyti į šiuos klausimus:

- Kas yra smulkus perdavimas kalbos modeliams?
- Kada ir kodėl smulkus perdavimas yra naudingas?
- Kaip galiu smulkiai perdaryti išankstinį modelį?
- Kokios smulkaus perdavimo ribos?

Pasiruošę? Pradėkime.

## Iliustruotas vadovas

Norite gauti bendrą vaizdą apie tai, ką aptarsime prieš panirdami giliau? Peržiūrėkite šį iliustruotą vadovą, apibūdinantį mokymosi kelionę šioje pamokoje - nuo pagrindinių smulkaus perdavimo sąvokų ir motyvacijos supratimo iki proceso ir geriausių praktikų vykdymo. Tai įdomi tema tyrinėjimui, todėl nepamirškite apsilankyti [Ištekliai](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) puslapyje dėl papildomų nuorodų, palaikančių jūsų savarankišką mokymosi kelionę!

![Iliustruotas vadovas kaip smulkiai perdaryti kalbos modelius](../../../translated_images/lt/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Kas yra smulkus perdavimas kalbos modeliams?

Apibrėžimu, dideli kalbos modeliai yra _išankstiniame etape apmokyti_ dideliais kiekius teksto iš įvairių šaltinių, įskaitant internetą. Kaip sužinojome ankstesnėse pamokose, mums reikia tokių metodų kaip _užklausų inžinerija_ ir _paiešką integruojanti generacija_, kad pagerintume modelio atsakymų į vartotojo užklausas („užklausas“) kokybę.

Populiari užklausų inžinerijos technika yra suteikti modeliui daugiau nurodymų, ko tikimasi atsakyme, pateikiant _instrukcijas_ (aiškias gaires) arba _pavyzdžius_ (neaiškias gaires). Tai vadinama _mažo pavyzdžių mokymu_ (few-shot learning), tačiau ji turi du apribojimus:

- Modelio žetonų ribos gali apriboti pateikiamų pavyzdžių skaičių ir efektyvumą.
- Modelio žetonų kainos gali padaryti brangų kiekvienos užklausos papildymą pavyzdžiais ir apriboti lankstumą.

Smulkus perdavimas yra įprasta praktika mašininio mokymosi sistemose, kai imame išankstinį modelį ir perkartojame jį su naujais duomenimis, kad pagerintume jo darbą tam tikroje užduotyje. Kalbos modelių atveju galime smulkiai perdaryti išankstinį modelį _su parinktu pavyzdžių rinkiniu tam tikrai užduočiai ar taikymo sričiai_, kad sukurtume **individualų modelį**, kuris gali būti tikslesnis ir aktualesnis konkrečiai užduočiai ar sričiai. Papildomas smulkaus perdavimo privalumas yra tas, kad jis gali sumažinti reikalingų pavyzdžių skaičių mažojo pavyzdžių mokymui – mažinant žetonų naudojimą ir susijusias išlaidas.

## Kada ir kodėl verta smulkiai perdaryti modelius?

Šiuo atžvilgiu kalbėdami apie smulkų perdavimą turime omenyje **prižiūrimą** smulkų perdavimą, kai perkartojimas atliekamas **pridedant naujų duomenų**, kurie nebuvo originalaus treniruočių duomenų rinkinio dalis. Tai skiriasi nuo nepriežiūros (unsupervised) smulkaus perdavimo, kai modelis perkartojamas su originaliais duomenimis, bet keičiant hiperparametrus.

Svarbiausia prisiminti, kad smulkus perdavimas yra pažangi technika, reikalaujanti tam tikrų žinių norint pasiekti pageidaujamus rezultatus. Netinkamai atlikus, tai gali nesuteikti laukiamų patobulinimų ir netgi pabloginti modeliavimo našumą jūsų tikslinėje srityje.

Taigi, prieš išmokdami „kaip“ smulkiai perdaryti kalbos modelius, turite žinoti „kodėl“ turėtumėte tai daryti ir „kada“ pradėti smulkaus perdavimo procesą. Pradėkite nuo šių klausimų sau:

- **Pritaikymo atvejis**: Koks yra jūsų _pritaikymo atvejis_ smulkiajam perdavimui? Kokį aspektą išankstiniame modelyje norite patobulinti?
- **Alternatyvos**: Ar bandėte _kitas technikas_ pasiekti pageidaujamus rezultatus? Naudokite jas kaip pagrindą palyginimui.
  - Užklausų inžinerija: išbandykite tokius metodus kaip mažo pavyzdžių skaičiaus užklausos pateikimas su atitinkamais atsakymų pavyzdžiais. Įvertinkite atsakymų kokybę.
  - Paiešką integruojanti generacija: pabandykite papildyti užklausas užklausų rezultatų paieška jūsų duomenyse. Įvertinkite atsakymų kokybę.
- **Išlaidos**: Ar nustatėte smulkaus perdavimo kaštus?
  - Perdavimo galimybė – ar modelis leidžia smulkų perdavimą?
  - Pastangos – treniruočių duomenų paruošimas, modelio vertinimas ir tobulinimas.
  - Skaičiavimas – smulkaus perdavimo užduočių vykdymas ir smulkiai perduoto modelio diegimas.
  - Duomenys – prieiga prie pakankamai kokybiškų pavyzdžių smulkiai perdavimui.
- **Privalumai**: Ar patvirtinote smulkaus perdavimo naudą?
  - Kokybė – ar smulkiai perduotas modelis pralenkė bazinį?
  - Kaina – ar sumažėjo žetonų naudojimas supaprastinus užklausas?
  - Praplėtimas – ar galite baseinį modelį pritaikyti naujoms sritims?

Atsakydami į šiuos klausimus turėtumėte sugebėti nuspręsti, ar smulkus perdavimas yra tinkamas jūsų atvejui. Idealiu atveju šis metodas yra prasmingas tik tada, kai privalumai viršija išlaidas. Pasirinkus tęsti, laikas pagalvoti, _kaip_ galima smulkiai perdaryti išankstinį modelį.

Norite gauti daugiau įžvalgų sprendimų priėmimo procese? Žiūrėkite [Fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Kaip smulkiai perdaryti išankstinį modelį?

Norint smulkiai perdaryti išankstinį modelį, reikia turėti:

- išankstinį modelį, kurį galima smulkiai perlankstyti
- duomenų rinkinį smulkiajam perdavimui
- treniruočių aplinką smulkiojo perdavimo užduočiai vykdyti
- talpinimo aplinką smulkiai perduoto modelio diegimui

## Smulkus perdavimas Microsoft Foundry platformoje

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) yra vieta, kur šiandien smulkiai perdarote, diegiate ir valdote individualius modelius Azure platformoje (tai apjungia anksčiau buvusius Azure OpenAI Studio ir Azure AI Studio). Prieš pradėdami užduotį, naudinga suprasti Foundry jums suteikiamus pasirinkimus ir platformos rekomenduojamas gerąsias praktikas. Foundry naudoja **LoRA (žemo rango adaptaciją)** efektyviam modelių smulkiam perdavimui, kuris leidžia treniruotes vykdyti greičiau ir pigiau nei perkartojant visus svorius.

### 1 žingsnis: Pasirinkite treniruočių metodą

Foundry palaiko tris smulkaus perdavimo būdus. **Pradėkite nuo SFT** – jis apima plačiausią scenarijų spektrą.

| Metodas | Ką daro | Kada naudoti |
| --- | --- | --- |
| **Prižiūrimas smulkus perdavimas (SFT)** | Treniruojamas pagal poras įvesties/išvesties pavyzdžių, kad modelis išmoktų generuoti pageidaujamus atsakymus. | Numatytoji daugeliui užduočių: domeno specializavimas, užduočių atlikimas, stiliaus ir tono pritaikymas, nurodymų vykdymas ir kalbos adaptacija. |
| **Tiesioginis pageidavimų optimizavimas (DPO)** | Mokosi iš porų _pageidaujami vs. nepageidaujami_ atsakymai, kad išvestys atitiktų žmonių pageidavimus. | Atsakymų kokybės, saugumo ir atitikimo gerinimas, kai turite palyginamą grįžtamąjį ryšį. |
| **Pastiprinamas smulkus perdavimas (RFT)** | Naudoja apdovanojimo signalus iš _vertintojų_, kad optimizuotų sudėtingus elgesio modelio aspektus pastiprinamo mokymosi būdu. | Objektyvūs, intensyviai mąstymui skirti domenai (matematika, chemija, fizika) su aiškiais teisingais/neteisingais atsakymais. Reikia daugiau ML žinių. |

### 2 žingsnis: Pasirinkite treniruočių lygį

Foundry leidžia pasirinkti, kaip ir kur vykdoma treniruotė:

- **Standartinis** – treniruotė vyksta jūsų Regiono ištekliuose ir užtikrinama duomenų lokalizacija. Naudokite, kai duomenys privalo likti tam tikrame regione.
- **Pasaulinis** – pigesnis ir greitesnis eilės sudėjimas naudojant pajėgumus už jūsų regiono ribų (duomenys ir svoriai kopijuojami į treniravimo regioną). Gera numatytoji parinktis, kai duomenų lokalizacija nėra būtina.
- **Vystytojo** – žemiausia kaina, naudojant laisvą pajėgumą be vėlavimų / SLA garantijų (užduotys gali būti sustabdytos ir tęsiamos). Idealus eksperimentavimui.

### 3 žingsnis: Pasirinkite bazinį modelį

Smulkiai perduodami modeliai apima OpenAI `gpt-4o-mini`, `gpt-4o`, `gpt-4.1`, `gpt-4.1-mini` ir `gpt-4.1-nano` (SFT; 4o/4.1 šeimai taip pat palaikomas DPO), samprotavimo modelius `o4-mini` ir `gpt-5` (RFT), bei atviro kodo modelius, pvz., `Ministral-3B`, `Qwen-32B`, `Llama-3.3-70B-Instruct` ir `gpt-oss-20b` (SFT Foundry ištekliuose). Visada tikrinkite dabartinį [Smulkaus perdavimo modelių sąrašą](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) dėl palaikomų metodų, regionų ir prieinamumo.

> Foundry siūlo dvi vietas treniravimui: **serveryje be valdymo** (kainodara pagal vartojimą, nereikia valdyti GPU kvotų, OpenAI ir kai kurie modeliai) ir **valdoma skaičiavimo aplinka** (gaukite savo VM per Azure Machine Learning su plačiausiu modelių asortimentu). Daugelis turėtų pradėti nuo serverio be valdymo.

### Foundry geriausios praktikos

- **Pirmiausia sukurkite pagrindinį rodiklį.** Išmatuokite bazinį modelį su užklausų inžinerija ir RAG _prieš_ smulkų perdavimą, kad galėtumėte įrodyti pelną.
- **Pradėkite su mažais duomenų rinkiniais, tada didinkite.** Pradėkite nuo 50-100 aukštos kokybės pavyzdžių požiūrį patvirtinti, tada auginkite iki 500+ gamybai. Kiekis nesvarbu, svarbu kokybė – šalinate žemos kokybės pavyzdžius.
- **Formatuokite duomenis teisingai.** Treniruočių ir patvirtinimo failai turi būti JSONL, UTF-8 **su BOM**, iki 512 MB, naudojant chat-completions žinučių formatą. Visada įtraukite patvirtinimo failą, kad galėtumėte stebėti pasimokymo perviršį.
- **Išsaugokite sistemos promptą inference metu.** Naudokite tą pačią sistemos žinutę, kuri buvo naudojama treniruočių metu.
- **Vertinkite tarpinius rezultatus – nepradėkite diegti paskutinio epoch rezultato aklai.** Foundry saugo tris paskutines epochs kaip diegimui tinkamus taškus; rinkitės tą, kuris geriausiai generalizuoja stebint `train_loss` / `valid_loss` ir žetonų tikslumą.
- **Vertinkite žetonų kainą kartu su kokybe** lygindami smulkiai perduotą modelį su baze.
- **Iteruokite nuolatiniu smulkiu perdavimu.** Galite smulkiai perdaryti jau smulkiai perduotą modelį su naujais duomenimis (palaikoma OpenAI modeliuose).
- **Atkreipkite dėmesį į talpinimo išlaidas.** Individuliai diegiamas modelis sąskaitojamas kas valandą, o nenaudojamas diegimas pašalinamas po 15 dienų – išvalykite, ko nereikia.

Išbandykite pilną žingsnis po žingsnio vadovą [Individualizuokite modelį smulkiu perdavimu](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) ir peržiūrėkite gaires apie [DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst) ir [RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst), kai būsite pasiruošę kitoms technikoms.

## Smulkus perdavimas praktikoje

Toliau pateikti ištekliai siūlo žingsnis po žingsnio pamokas, kurios veda per realų pavyzdį su šiuo metu palaikomu modeliu ir parinktu duomenų rinkiniu. Norint dirbti su jais, jums reikia paskyros atitinkamame tiekėjo platformoje bei prieigos prie reikiamo modelio bei duomenų rinkinių.

| Tiekėjas     | Mokomoji medžiaga                                                                                                                                                                 | Aprašymas                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Kaip smulkiai perduoti pokalbių modelius](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)       | Išmokite smulkiai perduoti neseniai sukurtą OpenAI pokalbių modelį konkrečiam domenui („receptų asistentas“) paruošiant treniruočių duomenis, vykdant smulkų perdavimą ir naudojant smulkiai perduotą modelį inference.                                                                                                                                                                                                                 |
| Microsoft Foundry | [Individualizuokite modelį smulkiu perdavimu](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst)                      | Išmokite smulkiai perduoti šiuo metu palaikomą modelį, pavyzdžiui, `gpt-4.1-mini` **Azure platformoje** su Microsoft Foundry: paruoškite ir įkelkite treniruočių bei patvirtinimo duomenis, vykdykite smulkaus perdavimo užduotį, tada diegkite ir naudokite naują modelį.                                                                                                                                                            |

| Hugging Face | [LLM modelių tobulinimas su Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Šiame tinklaraščio įraše pristatoma, kaip tobulinti _atvirą LLM_ (pvz., `CodeLlama 7B`) naudojant [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) biblioteką ir [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) kartu su atvirais [duomenų rinkiniais](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) Hugging Face platformoje. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [LLM modelių tobulinimas su AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (arba AutoTrain Advanced) yra python biblioteka sukurta Hugging Face, leidžianti tobulinti modelius įvairioms užduotims, įskaitant LLM tobulinimą. AutoTrain yra be kodo sprendimas, o tobulinimą galima atlikti savo debesyje, Hugging Face Spaces arba lokaliai. Jis palaiko tiek internetinę GUI, tiek komandų eilutę ir mokymą per yaml konfigūracijos failus.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [LLM modelių tobulinimas su Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth yra atvirojo kodo sistema, palaikanti LLM tobulinimą ir stiprinamąjį mokymąsi (RL). Unsloth supaprastina lokalius mokymus, vertinimą ir diegimą su paruoštais naudoti [užrašais](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Ji taip pat palaiko teksto į kalbą (TTS), BERT ir multimodalinius modelius. Norėdami pradėti, perskaitykite jų žingsnis po žingsnio [LLM tobulinimo vadovą](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Užduotis

Pasirinkite vieną iš aukščiau pateiktų mokymų ir juos peržiūrėkite. _Gali būti, kad šių mokymų versijos bus atkartotos Jupyter užrašų knygelėse šiame repozitorijoje tik nuorodai. Prašome naudoti tiesiogiai originalius šaltinius, kad gautumėte naujausias versijas_.

## Puikiai padirbėta! Tęskite mokymąsi.

Baigę šią pamoką, apsilankykite mūsų [Generatyvios AI mokymosi kolekcijoje](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kad toliau gilintumėte žinias apie generatyviąją AI!

Sveikiname!! Jūs baigėte šios kursų serijos v2 paskutinę pamoką! Nesustokite mokytis ir kurti. \*\*Peržiūrėkite [RESURSŲ](RESOURCES.md?WT.mc_id=academic-105485-koreyst) puslapį, kuriame rasite papildomų pasiūlymų šia tema.

Mūsų v1 pamokų serija taip pat buvo atnaujinta su daugiau užduočių ir koncepcijų. Skirkite minutėlę, kad atnaujintumėte savo žinias - ir prašome [pasidalinti savo klausimais ir atsiliepimais](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst), kad padėtumėte mums tobulinti šias pamokas bendruomenei.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->