# LLM teikėjo pasirinkimas ir konfigūravimas 🔑

Užduotys **taip pat gali būti** nustatytos veikti su vienu ar keliais Didelės kalbos modelio (LLM) diegimais per palaikomą paslaugų teikėją, pavyzdžiui, OpenAI, Azure arba Hugging Face. Šie teikėjai siūlo _talpinamą galinį tašką_ (API), prie kurio galime programiškai prisijungti su tinkamais prisijungimo duomenimis (API raktu arba žetonu). Šiame kurse aptariame šiuos teikėjus:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) su įvairiais modeliais, įskaitant pagrindinę GPT seriją.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI modeliams, orientuotiems į verslo parengtį
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) vienam galiniam taškui ir API raktui, leidžiant prisijungti prie šimtų modelių iš OpenAI, Meta, Mistral, Cohere, Microsoft ir kt. (pakeis GitHub Models, kuris nustos veikti 2026 m. liepos pabaigoje)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) atvirojo kodo modeliams ir išvados serveriui
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) arba [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst), jei norite modelius paleisti visiškai vietoje savo įrenginyje be debesijos prenumeratos

**Šioms užduotims reikės jūsų pačių paskyrų**. Užduotys yra neprivalomos, todėl galite pasirinkti nustatyti vieną, visus ar nė vieno teikėjo paslaugas pagal savo pomėgius. Štai kelios pildymo gairės:

| Registracija | Kaina | API raktas | Žaidimų aikštelė | Pastabos |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Kainodara](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projekto bazėje](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Be kodo, web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Turtingas modelių pasirinkimas |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Kainodara](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK pradžia](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio pradžia](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Reikia iš anksto pateikti paraišką prieigai](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Kainodara](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Projekto apžvalga](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry žaidimų aikštelė](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Nemokamas paketas yra; vienas galinis taškas + raktas daugeliui modelių teikėjų |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Kainodara](https://huggingface.co/pricing) | [Prieigos žetonai](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ribotas modelių pasirinkimas](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Nemokama (veikia jūsų įrenginyje) | Nereikalingas | [Vietinis CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Visiškai offline, OpenAI suderinamas galinis taškas |
| | | | | |

Toliau pateiktos instrukcijos padės _konfigūruoti_ šį repozitoriją darbui su skirtingais teikėjais. Užduotyse, kurioms reikalingas konkretus teikėjas, failo pavadinimuose bus vienas iš šių žymų:

- `aoai` - reikia Azure OpenAI galinio taško, rakto
- `oai` - reikia OpenAI galinio taško, rakto
- `hf` - reikia Hugging Face žetono
- `githubmodels` - reikia Microsoft Foundry Models galinio taško, rakto (GitHub Models nustos veikti 2026 m. liepos pabaigoje)

Galite konfigūruoti vieną, nė vieno ar visus teikėjus. Susijusios užduotys paprasčiausiai sugrąžins klaidą trūkstant prisijungimo duomenų.

## Sukurkite `.env` failą

Manome, kad jau perskaitėte aukščiau pateiktas instrukcijas ir užsiregistravote pas atitinkamą teikėją bei gavote reikalingus autentifikacijos duomenis (API_RAKTAS arba žetoną). Azure OpenAI atveju taip pat turime turėti galiojančią Azure OpenAI paslaugos diegimą (galinį tašką) su bent vienu GPT modeliu pokalbių užbaigimui.

Kitas žingsnis – sukonfigūruoti savo **vietinius aplinkos kintamuosius** taip:

1. Pažiūrėkite į šakninį aplanką, kur turėtų būti `.env.copy` failas su tokio turinio pavyzdžiu:

   ```bash
   # OpenAI tiekėjas
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI Microsoft Foundry
   ## (Azure OpenAI paslauga dabar yra Microsoft Foundry dalis: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Numatytoji reikšmė nustatyta! (dabartinė stabili GA API versija)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry modeliai (daugia-tiekėjo modelių katalogas, pakeičia GitHub modelius, kurie bus nutraukti 2026 m. liepos pabaigoje)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Nukopijuokite šį failą į `.env` naudodami šią komandą. Šis failas yra _gitignore_, todėl saugo jūsų slaptažodžius.

   ```bash
   cp .env.copy .env
   ```

3. Užpildykite reikšmes (pakeiskite dešinėje pusėje esančius laikinuosius simbolius po =), kaip aprašyta kitame skyriuje.

4. (Pasirinktinai) Jei naudojate GitHub Codespaces, galite įrašyti aplinkos kintamuosius kaip _Codespaces secrets_, susietus su šiuo repozitorijumi. Tokiu atveju nereikės kurti vietinio .env failo. **Tačiau atkreipkite dėmesį, kad ši galimybė veikia tik su GitHub Codespaces.** Jei naudojate Docker Desktop, .env failas vis tiek turi būti sukurtas.

## Užpildykite `.env` failą

Pažvelkime į kintamųjų pavadinimus ir supraskime, ką jie reiškia:

| Kintamasis  | Aprašymas  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Tai yra vartotojo prieigos žetonas, kurį nustatėte savo profilyje |
| OPENAI_API_KEY | Tai yra autorizacijos raktas naudojant ne Azure OpenAI galinius taškus |
| AZURE_OPENAI_API_KEY | Tai yra autorizacijos raktas naudojant Azure OpenAI paslaugą |
| AZURE_OPENAI_ENDPOINT | Tai yra Azure OpenAI išdiegto galinio taško adresas |
| AZURE_OPENAI_DEPLOYMENT | Tai yra _teksto generavimo_ modelio diegimo galinis taškas |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Tai yra _teksto įterpimo_ modelio diegimo galinis taškas |
| AZURE_INFERENCE_ENDPOINT | Tai yra Microsoft Foundry projekto galinis taškas, naudojamas Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Tai yra API raktas jūsų Microsoft Foundry projektui |
| | |

Pastaba: Paskutiniai du Azure OpenAI kintamieji atspindi numatytąjį modelį pokalbių užbaigimui (teksto generavimui) ir vektorinėms paieškoms (įterpimams) atitinkamai. Nurodymai, kaip juos nustatyti, bus pateikti atitinkamose užduotyse.

## Azure OpenAI konfigūravimas: per Portalą

> **Pastaba:** Azure OpenAI paslauga dabar yra [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) dalis. Ištekliai ir diegimai vis dar matomi Azure portale, tačiau kasdienis modelio valdymas (diegimai, žaidimų aikštelė, stebėjimas) vyksta Foundry portale, o ne senojoje atskiroje „Azure OpenAI Studio“ aplinkoje.

Azure OpenAI galinio taško ir rakto reikšmes rasite [Azure portale](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), tad pradėkime ten.

1. Eikite į [Azure portalą](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Šoniniame meniu (kaip kairėje) spustelėkite pasirinkimą **Keys and Endpoint**.
1. Spustelėkite **Show Keys** – turėtumėte matyti KEY 1, KEY 2 ir Endpoint.
1. Naudokite KEY 1 reikšmę kaip AZURE_OPENAI_API_KEY
1. Naudokite Endpoint reikšmę kaip AZURE_OPENAI_ENDPOINT

Toliau mums reikės specifinių modelių galinių taškų, kuriuos įdiegėme.

1. Šoniniame meniu (kairėje) Azure OpenAI ištekliui spustelėkite **Model deployments**.
1. Paskirties puslapyje spustelėkite **Eiti į Microsoft Foundry portalą** (arba **Valdyti diegimus**, priklausomai nuo išteklių tipo).

Jums bus atidarytas Microsoft Foundry portalas, kuriame rasime kitas reikšmes, kaip aprašyta žemiau.

## Azure OpenAI konfigūravimas: per Microsoft Foundry portalą

1. Eikite į [Microsoft Foundry portalą](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **per savo išteklių** kaip aprašyta prieš tai.
1. Spustelėkite skirtuką **Deployments** (šoninis meniu kairėje), kad pamatytumėte šiuo metu įdiegtus modelius.
1. Jei norimas modelis nėra įdiegtas, naudokite **Deploy model**, kad diegtumėte jį iš [modelių katalogo](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Jums reikės _teksto generavimo_ modelio – rekomenduojame: **gpt-4o-mini**
1. Jums reikės _teksto įterpimo_ modelio – rekomenduojame **text-embedding-3-small**

Dabar atnaujinkite aplinkos kintamuosius, kad atspindėtumėte naudotą _Deployment name_. Tai paprastai bus toks pat kaip modelio pavadinimas, nebent jūs jį aiškiai pakeitėte. Pavyzdžiui, galite turėti:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Nepamirškite išsaugoti .env failo pabaigus**. Dabar galite uždaryti failą ir grįžti prie tolesnių instrukcijų, kaip paleisti užrašų knygelę.

## OpenAI konfigūravimas: per profilį

Jūsų OpenAI API raktą rasite savo [OpenAI paskyroje](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jei jo neturite, galite užsiregistruoti ir sukurti API raktą. Kai turėsite raktą, jį įrašykite į `OPENAI_API_KEY` kintamąjį `.env` faile.

## Hugging Face konfigūravimas: per profilį

Savo Hugging Face žetoną rasite profilyje skiltyje [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nepublikuokite ar nesidalinkite juo viešai. Vietoje to sukurkite naują žetoną šiam projektui ir nukopijuokite jį į `.env` failą po `HUGGING_FACE_API_KEY` kintamuoju. _Pastaba:_ techniškai tai nėra API raktas, bet naudojamas autentifikacijai, todėl laikomės šios pavadinimo konvencijos dėl nuoseklumo.

## Microsoft Foundry Models konfigūravimas: per Portalą

> **Pastaba:** GitHub Models nustos veikti 2026 m. liepos pabaigoje. Microsoft Foundry Models yra tiesioginis pakeitimas, siūlantis tą patį nemokamą bandomąjį modelių katalogą ir Azure AI Inference SDK / OpenAI SDK patirtį.

1. Eikite į [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) ir sukurkite (arba atidarykite) Foundry projektą.
1. Peržiūrėkite [modelių katalogą](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ir diegkite modelį, pvz., `gpt-4o-mini`.
1. Projekto **Overview** puslapyje nukopijuokite **galinį tašką** ir **API raktą**.
1. Naudokite galinio taško reikšmę `AZURE_INFERENCE_ENDPOINT` ir rakto reikšmę `AZURE_INFERENCE_CREDENTIAL` savo `.env` faile.

## Offline / Vietiniai teikėjai

Jei nenorite naudoti debesijos prenumeratos, galite palaikomus atvirus modelius paleisti tiesiogiai savo įrenginyje:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** – Microsoft vietinis vykdymo variklis. Automatiškai pasirenka geriausią vykdymo teikėją (NPU, GPU arba CPU) ir pateikia OpenAI suderinamą galinį tašką, todėl daugelį pavyzdinių kodo dalių šiame kurse galėsite naudoti su minimaliais pakeitimais. Žr. [Foundry Local dokumentaciją](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) pradėti arba įdiekite su `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** – populiari alternatyva vietoje paleisti atvirus modelius, tokius kaip Llama, Phi, Mistral ir Gemma.


Peržiūrėkite [19 pamoką: Statyba naudojant SLM](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) dėl praktinių pavyzdžių, naudojant abiejus variantus.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->