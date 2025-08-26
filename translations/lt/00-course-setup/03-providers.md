<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T20:14:13+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "lt"
}
-->
# LLM tiekėjo pasirinkimas ir konfigūravimas 🔑

Užduotys **gali** būti sukonfigūruotos veikti su vienu ar keliais didžiųjų kalbos modelių (LLM) diegimais per palaikomą paslaugų tiekėją, pvz., OpenAI, Azure ar Hugging Face. Šie tiekėjai suteikia _pateiktą galinį tašką_ (API), prie kurio galime prisijungti programiškai, turėdami tinkamus prisijungimo duomenis (API raktą ar žetoną). Šiame kurse aptariame šiuos tiekėjus:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) su įvairiais modeliais, įskaitant pagrindinę GPT seriją.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) – OpenAI modeliams su verslui pritaikytais sprendimais
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) – atvirojo kodo modeliams ir inferencijos serveriui

**Šiems pratimams reikės naudoti savo paskyras**. Užduotys yra neprivalomos, tad galite pasirinkti, kurį tiekėją norite susikonfigūruoti – vieną, visus arba nė vieno, priklausomai nuo savo poreikių. Keletas patarimų registracijai:

| Registracija | Kaina | API raktas | „Playground“ | Komentarai |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Kainodara](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Pagal projektą](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Be kodo, žiniatinklyje](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Galima rinktis iš kelių modelių |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Kainodara](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK greitoji pradžia](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio greitoji pradžia](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Reikia iš anksto pateikti paraišką dėl prieigos](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Kainodara](https://huggingface.co/pricing) | [Prieigos žetonai](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat turi ribotą modelių pasirinkimą](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Vadovaukitės toliau pateiktomis instrukcijomis, kaip _konfigūruoti_ šį repozitoriją darbui su skirtingais tiekėjais. Užduotys, kurioms reikalingas konkretus tiekėjas, turės vieną iš šių žymų savo faile:

- `aoai` – reikalingas Azure OpenAI galinis taškas ir raktas
- `oai` – reikalingas OpenAI galinis taškas ir raktas
- `hf` – reikalingas Hugging Face žetonas

Galite konfigūruoti vieną, nė vieno arba visus tiekėjus. Susijusios užduotys tiesiog rodys klaidą, jei trūks prisijungimo duomenų.

## Sukurkite `.env` failą

Darome prielaidą, kad jau perskaitėte aukščiau pateiktą informaciją, užsiregistravote pas pasirinktą tiekėją ir gavote reikiamus autentifikacijos duomenis (API_KEY arba žetoną). Jei naudojate Azure OpenAI, taip pat turite turėti veikiantį Azure OpenAI paslaugos diegimą (galinį tašką) su bent vienu GPT modeliu, skirtu pokalbių užbaigimui.

Kitas žingsnis – sukonfigūruoti savo **vietinius aplinkos kintamuosius** taip:

1. Šakniniame aplanke raskite `.env.copy` failą, kuris turėtų atrodyti taip:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Nukopijuokite šį failą į `.env` naudodami žemiau pateiktą komandą. Šis failas yra _gitignore_, todėl jūsų slapti duomenys bus saugūs.

   ```bash
   cp .env.copy .env
   ```

3. Užpildykite reikšmes (pakeiskite dešinėje pusėje esančius šablonus) kaip aprašyta kitame skyriuje.

4. (Pasirinktinai) Jei naudojate GitHub Codespaces, galite išsaugoti aplinkos kintamuosius kaip _Codespaces secrets_, susietus su šiuo repozitoriumi. Tokiu atveju vietinio .env failo kurti nereikės. **Tačiau atkreipkite dėmesį, kad ši galimybė veikia tik naudojant GitHub Codespaces.** Jei vietoje to naudojate Docker Desktop, .env failą vis tiek reikės susikurti.

## Užpildykite `.env` failą

Trumpai apžvelkime kintamųjų pavadinimus, kad suprastume, ką jie reiškia:

| Kintamasis  | Aprašymas  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Tai vartotojo prieigos žetonas, kurį susikūrėte savo profilyje |
| OPENAI_API_KEY | Tai autorizacijos raktas, skirtas naudoti paslaugą ne Azure OpenAI galiniams taškams |
| AZURE_OPENAI_API_KEY | Tai autorizacijos raktas, skirtas naudoti šią paslaugą |
| AZURE_OPENAI_ENDPOINT | Tai diegto Azure OpenAI resurso galinis taškas |
| AZURE_OPENAI_DEPLOYMENT | Tai _teksto generavimo_ modelio diegimo galinis taškas |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Tai _teksto įterpinių_ modelio diegimo galinis taškas |
| | |

Pastaba: Paskutiniai du Azure OpenAI kintamieji nurodo numatytąjį modelį pokalbių užbaigimui (teksto generavimui) ir vektorių paieškai (įterpiniams). Instrukcijos, kaip juos nustatyti, bus pateiktos atitinkamose užduotyse.

## Azure konfigūravimas: per Portalą

Azure OpenAI galinio taško ir rakto reikšmes rasite [Azure portale](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), tad pradėkime nuo to.

1. Eikite į [Azure portalą](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kairiajame meniu pasirinkite **Keys and Endpoint**.
1. Spauskite **Show Keys** – turėtumėte matyti: KEY 1, KEY 2 ir Endpoint.
1. Naudokite KEY 1 reikšmę kaip AZURE_OPENAI_API_KEY
1. Naudokite Endpoint reikšmę kaip AZURE_OPENAI_ENDPOINT

Toliau mums reikės konkrečių diegtų modelių galinių taškų.

1. Kairiajame meniu pasirinkite **Model deployments** savo Azure OpenAI resurse.
1. Atsidariusiame puslapyje spauskite **Manage Deployments**

Tai nuves jus į Azure OpenAI Studio svetainę, kur rasite kitus reikalingus duomenis, kaip aprašyta žemiau.

## Azure konfigūravimas: per Studio

1. Eikite į [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **iš savo resurso**, kaip aprašyta aukščiau.
1. Kairiajame meniu pasirinkite **Deployments** ir matysite šiuo metu diegtus modelius.
1. Jei norimo modelio nėra, naudokite **Create new deployment** ir įdiekite jį.
1. Reikės _teksto generavimo_ modelio – rekomenduojame: **gpt-35-turbo**
1. Reikės _teksto įterpinių_ modelio – rekomenduojame **text-embedding-ada-002**

Dabar atnaujinkite aplinkos kintamuosius pagal _Deployment name_, kurį naudojote. Dažniausiai jis bus toks pat kaip modelio pavadinimas, nebent jį keitėte. Pavyzdžiui, galite turėti:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Nepamirškite išsaugoti .env failo, kai baigsite**. Dabar galite uždaryti failą ir grįžti prie užrašų knygelės paleidimo instrukcijų.

## OpenAI konfigūravimas: per profilį

Savo OpenAI API raktą rasite savo [OpenAI paskyroje](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jei dar neturite, užsiregistruokite ir susikurkite API raktą. Gavę raktą, įrašykite jį į `.env` faile esantį `OPENAI_API_KEY` kintamąjį.

## Hugging Face konfigūravimas: per profilį

Savo Hugging Face žetoną rasite savo profilyje, skiltyje [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Niekada neskelbkite ir nesidalinkite šiais duomenimis viešai. Sukurkite naują žetoną šiam projektui ir nukopijuokite jį į `.env` failą po `HUGGING_FACE_API_KEY` kintamuoju. _Pastaba:_ Technologiškai tai nėra API raktas, tačiau naudojamas autentifikacijai, todėl pavadinimas paliekamas dėl nuoseklumo.

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbios informacijos atveju rekomenduojame profesionalų žmogaus vertimą. Mes neatsakome už nesusipratimus ar neteisingą interpretavimą, kilusį dėl šio vertimo naudojimo.