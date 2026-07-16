[![Atviro Kodo Modeliai](../../../translated_images/lt/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Didelio kalbos modelio (LLM) derinimas

Naudojant didelius kalbos modelius generatyvioms AI programėlėms kurti atsiranda naujų iššūkių. Pagrindinė problema yra užtikrinti atsakymų kokybę (tikslumą ir aktualumą) modelio generuotame turinyje pagal vartotojo užklausą. Ankstesnėse pamokose aptarėme tokias technikas kaip užklausų kūrimas (prompt engineering) ir atsakymų gavimas su papildoma paieška (retrieval-augmented generation), kurios bando išspręsti šią problemą *keitinėjant užklausos įvestį* esamam modeliui.

Šios pamokos tema yra trečioji technika – **derinimas (fine-tuning)**, kuri siekia spręsti iššūkį *perkvalifikuojant patį modelį* su papildomais duomenimis. Panagrinėkime detaliau.

## Mokymosi tikslai

Šioje pamokoje supažindinsime su derinimo sąvoka išankstinio apmokymo kalbos modeliams, aptarsime šio metodo privalumus ir iššūkius, bei pateiksime rekomendacijas, kada ir kaip naudoti derinimą, kad pagerintumėte savo generatyvių AI modelių veikimą.

Pamokos pabaigoje turėtumėte sugebėti atsakyti į šiuos klausimus:

- Kas yra kalbos modelių derinimas?
- Kada ir kodėl derinimas yra naudingas?
- Kaip galima atlikti išankstinio apmokymo modelio derinimą?
- Kokios yra derinimo ribotybės?

Pasiruošę? Pradėkime.

## Iliustruota apžvalga

Norite geriau suprasti, ką aptarsime, prieš kibdami į detalės? Peržiūrėkite šį iliustruotą gidą, kuris apibūdina mokymosi kelionę šiai pamokai – nuo pagrindinių derinimo sąvokų ir motyvacijos iki proceso supratimo ir geriausių praktikų atlikti derinimo užduotį. Tai intriguojanti tema, todėl nepamirškite apsilankyti [Resursų](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) puslapyje, kur rasite papildomų nuorodų savarankiškam mokymuisi!

![Iliustruotas kalbos modelių derinimo vadovas](../../../translated_images/lt/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Kas yra kalbos modelių derinimas?

Pagal apibrėžimą, dideli kalbos modeliai yra *išankstinio apmokymo* (pre-trained) su didele kiekių tekstų iš įvairių šaltinių, įskaitant internetą. Kaip išmokome ankstesnėse pamokose, mums reikia technikų, tokių kaip *užklausų kūrimas* ir *atsakymų gavimas su papildoma paieška*, kad pagerintume modelio atsakymų kokybę vartotojo klausimams („užklausoms“).

Populiari užklausų kūrimo technika – suteikti modeliui daugiau nurodymų, ko tikimasi atsakyme, pateikiant *instrukcijas* (aiškias gaires) arba *keleto pavyzdžių* (netiesiogines gaires). Tai vadinama *keleto pavyzdžių mokymu* (few-shot learning), tačiau ji turi dvi ribas:

- Modelio simbolių limitai gali apriboti pateikiamų pavyzdžių kiekį ir sumažinti efektyvumą.
- Modelio simbolių sąnaudos gali pabranginti pavyzdžių pridėjimą prie kiekvienos užklausos ir sumažinti lankstumą.

Derinimas yra įprasta mašininio mokymosi praktika, kai išankstinį apmokytą modelį perkvalifikuojame su naujais duomenimis, kad pagerintume jo veikimą konkrečioje užduotyje. Kalbos modelių kontekste galime derinti išankstinį modelį *su atrinktu pavyzdžių rinkiniu konkrečiai užduočiai ar taikymo sričiai* ir sukurti **individualiai pritaikytą modelį**, kuris gali būti tikslesnis ir aktualesnis tam tikroje srityje. Papildomas derinimo privalumas – sumažėti keletą pavyzdžių, reikalingų keletos pavyzdžių mokymuisi – mažinama simbolių naudojimo ir su tuo susijusios išlaidos.

## Kada ir kodėl reikėtų derinti modelius?

Šiame kontekste derinimas reiškia **prižiūrimą (supervised) derinimą**, kuomet perkvalifikavimas atliekamas **pridedant naujų duomenų**, kurie nebuvo originaliame mokymosi rinkinyje. Tai skiriasi nuo neprižiūrimo derinimo, kai modelis perkvalifikuojamas pagal originalius duomenis, bet naudojant kitus hiperparametrus.

Svarbiausia prisiminti, kad derinimas yra pažangi technika, reikalaujanti tam tikro lygio kompetencijos norint pasiekti norimus rezultatus. Jei atliktas neteisingai, jis gali nesuteikti laukiamų patobulinimų ir netgi pabloginti modelio veikimą jūsų pasirinktoje srityje.

Todėl prieš mokydamiesi „kaip“ derinti kalbos modelius, turite suprasti „kodėl“ verta tai daryti ir „kada“ pradėti derinimo procesą. Paklauskite savęs šiuos klausimus:

- **Naudojimo atvejis**: Koks jūsų *naudos atvejis* dėl derinimo? Ką norite patobulinti dabartiniame išankstinio apmokymo modelyje?
- **Alternatyvos**: Ar bandėte *kitas technikas* norint pasiekti norimų rezultatų? Naudokite jas kaip palyginimo pagrindą.
  - Užklausų kūrimas: Išbandykite technikas kaip keletos pavyzdžių užklausos su tinkamais atsakymo pavyzdžiais. Įvertinkite atsakymų kokybę.
  - Atsakymų gavimas su papildoma paieška: Išbandykite užklausų papildymą rezultatų įtraukimu ieškant jūsų duomenų. Įvertinkite atsakymų kokybę.
- **Išlaidos**: Ar įvertinote derinimo išlaidas?
  - Derinamumas – ar išankstinis modelis prieinamas derinimui?
  - Pastangos – mokymo duomenų paruošimas, modelio vertinimas ir tobulinimas.
  - Skaičiavimai – derinimo užduočių vykdymas ir derinto modelio diegimas.
  - Duomenys – prieiga prie pakankamos kokybės pavyzdžių derinimo poveikiui.
- **Privalumai**: Ar patvirtinote derinimo naudą?
  - Kokybė – ar derintas modelis viršijo lyginamąjį pagrindą?
  - Kaina – ar sumažina simbolių naudojimą supaprastindamas užklausas?
  - Išplėstinumą – ar galite pritaikyti bazinį modelį naujoms sritims?

Atsakydami į šiuos klausimus, turėtumėte gebėti nuspręsti, ar derinimas yra tinkamas jūsų atvejui. Idealiu atveju šis metodas prasmingas tik tada, kai privalumai viršija išlaidas. Pasirinkę tęsti, pradėkite galvoti *kaip* galėtumėte derinti išankstinį modelį.

Norite daugiau įžvalgų priimant sprendimą? Peržiūrėkite [Derinti ar nederinti?](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Kaip galime derinti išankstinį modelį?

Norėdami atlikti modelio derinimą, jums reikia turėti:

- išankstinį modelį derinimui
- duomenų rinkinį naudojimui derinant
- mokymo aplinką derinimo užduočiai vykdyti
- talpinimo aplinką derintam modeliui diegti

## Derinimas praktikoje

> **Pastaba:** `gpt-35-turbo` / `gpt-3.5-turbo`, minimi kai kuriuose toliau pateiktuose mokymuose, yra pašalinti tiek inferencijai, tiek derinimui. Jei šiandien pradedate naują derinimo darbą, pasirinkite šiuo metu palaikomą modelį – pavyzdžiui, `gpt-4o-mini` ar `gpt-4.1-mini`. Žr. [Derinamų modelių sąrašą](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) dėl dabartinio derinimui tinkančių modelių rinkinio. Šių mokymų koncepcijos ir žingsniai vis tiek taikomi.

Toliau pateikti šaltiniai siūlo žingsnis po žingsnio mokymus, kuriais galėsite atlikti realų pavyzdį su pasirinktiniu modeliu ir atrinktu duomenų rinkiniu. Norėdami dirbti su šiais mokymais, jums reikia paskyros pas konkrečią tiekėją bei prieigos prie atitinkamų modelių ir duomenų rinkinių.

| Tiekėjas    | Mokymas                                                                                                                                                                       | Aprašymas                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Kaip derinti pokalbių modelius](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)             | Išmokite derinti `gpt-35-turbo` konkrečiam domenui („receptų asistentas“) paruošiant mokymo duomenis, vykdant derinimo užduotį ir naudoti derintą modelį inferencijai.                                                                                                                                                                                                                                                             |
| Azure OpenAI | [GPT 3.5 Turbo derinimo pamoka](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst)     | Išmokite derinti `gpt-35-turbo-0613` modelį **Azure aplinkoje** atlikdami žingsnius nuo mokymo duomenų kūrimo ir įkėlimo iki derinimo užduoties vykdymo. Diegiama ir naudojama naujasis modelis.                                                                                                                                                                                                                                      |
| Hugging Face | [Derinimas su Hugging Face LLM](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                                  | Šiame tinklaraščio įraše aprašyta, kaip derinti *atvirą LLM* (pvz., `CodeLlama 7B`) naudojant [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) biblioteką ir [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) su atvirais [duomenų rinkiniais](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) Hugging Face platformoje. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 🤗 AutoTrain | [Derinimas su AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                                  | AutoTrain (arba AutoTrain Advanced) yra Hugging Face sukurta python biblioteka, leidžianti derinti daugybei skirtingų užduočių įskaitant LLM derinimą. AutoTrain yra programavimo nereikalaujantis sprendimas ir derinimas gali būti atliekamas jūsų pačių debesyje, Hugging Face Spaces arba vietoje. Jis palaiko tiek žiniatinklio GUI, tiek CLI ir mokymą per yaml konfigūracijų failus.                                                                                  |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 🦥 Unsloth | [Derinimas su Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                                                    | Unsloth yra atviro kodo karkasas, remiantis LLM derinimu ir stiprinamuoju mokymusi (RL). Unsloth supaprastina vietinį mokymą, vertinimą ir diegimą su paruoštais [užrašų knygelės](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Taip pat palaiko teksto ir kalbos (TTS), BERT ir multimodalinius modelius. Norėdami pradėti, perskaitykite jų žingsnis po žingsnio [LLM Derinimo Vadovą](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                                      |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
## Priskyrimas

Pasirinkite vieną iš aukščiau pateiktų mokymų ir juos išbandykite. _Mes galbūt pakartosime tam tikrą šių mokymų versiją Jupyter užrašų knygutėse šiame repo tik kaip pavyzdį. Prašome naudotis originaliais šaltiniais, kad gautumėte naujausias versijas_.

## Puikus darbas! Tęskite mokymąsi.

Baigę šią pamoką, peržiūrėkite mūsų [Generatyvios AI mokymosi kolekciją](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kad toliau gilintumėte savo žinias apie generatyvią AI!

Sveikiname!! Jūs baigėte paskutinę šio kurso v2 serijos pamoką! Nesustokite mokytis ir kurti. **Peržiūrėkite [RESURSŲ](RESOURCES.md?WT.mc_id=academic-105485-koreyst) puslapį, kuriame rasite papildomų pasiūlymų šiai temai.**

Mūsų v1 serija taip pat atnaujinta su daugiau priskyrimų ir koncepcijų. Taigi skirkite minutę žinių atnaujinimui – ir prašome [pasidalinti savo klausimais bei atsiliepimais](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst), kad padėtumėte mums patobulinti šias pamokas bendruomenei.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->