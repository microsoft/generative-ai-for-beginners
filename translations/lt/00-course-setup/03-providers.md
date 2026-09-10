# Pasirenkame ir konfigūruojame LLM teikėją 🔑

Užduotys **gali** būti sukonfigūruotos taip, kad veiktų per vieną ar daugiau didelių kalbos modelių (LLM) diegimų per palaikytą paslaugų teikėją, tokį kaip OpenAI, Azure ar Hugging Face. Jie suteikia _hostintą taško prieigos vietą_ (API), prie kurios galime programiškai prisijungti turėdami tinkamus prieigos duomenis (API raktą ar žetoną). Šiame kurse aptariame šiuos teikėjus:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) su įvairiais modeliais, įskaitant pagrindinę GPT seriją.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) OpenAI modeliams, akcentuojant paruošimą verslui.
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) su vienu taško prieigos vietos ir API raktu prieigai prie šimtų modelių iš OpenAI, Meta, Mistral, Cohere, Microsoft ir kt. (pakeičia GitHub Models, kurios bus nutrauktos 2026 m. liepos pabaigoje).
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) atvirojo kodo modeliams ir inferencijos serveriui.
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) arba [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst), jei norite modelius paleisti visiškai neprisijungę savo įrenginyje, be jokios debesų prenumeratos.

**Šioms užduotims reikės naudotis savo paskyromis**. Užduotys yra neprivalomos, tad galite pasirinkti sukonfigūruoti vieną, visus arba nė vieno iš teikėjų pagal savo pomėgius. Štai keletas patarimų registracijai:

| Registracija | Kaina | API raktas | Demonstracija | Pastabos |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Kainodara](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektų pagrindu](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Be kodo, internetinė](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Galima naudotis keletu modelių |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Kainodara](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK pradžiamokslis](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio pradžiamokslis](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Reikia iš anksto kreiptis dėl prieigos](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Kainodara](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Projekto apžvalgos puslapis](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry demonstracija](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Galima nemokama versija; vienas taško prieigos vietos URL + raktas daugeliui modelių teikėjų |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Kainodara](https://huggingface.co/pricing) | [Prieigos žetonai](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat turi ribotą modelių asortimentą](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Nemokama (veikia jūsų įrenginyje) | Nereikalinga | [Vietinis CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Visiškai neprisijungusi, OpenAI suderinama taško prieigos vieta |
| | | | | |

Toliau pateiktos instrukcijos, kaip _konfigūruoti_ šį repozitorijų darbui su skirtingais teikėjais. Užduotys, reikalaujančios konkretaus teikėjo, turės vieną iš šių žymų savo failo pavadinime:

- `aoai` - reikalauja Azure OpenAI taško prieigos vietos ir rakto
- `oai` - reikalauja OpenAI taško prieigos vietos ir rakto
- `hf` - reikalauja Hugging Face žetono
- `githubmodels` - reikalauja Microsoft Foundry Models taško prieigos vietos ir rakto (GitHub Models bus nutrauktos 2026 m. liepos pabaigoje)

Galite konfigūruoti vieną, nė vieno ar visus teikėjus. Susijusios užduotys tiesiog grąžins klaidą pritrūkus leidimų.

## Sukurkite `.env` failą

Darome prielaidą, kad jau perskaitėte aukščiau pateiktas instrukcijas, užsiregistravote pas atitinkamą teikėją ir gavote reikiamus autentifikacijos duomenis (API_RAKTAS arba žetoną). Azure OpenAI atveju taip pat darant prielaidą, kad turite galiojantį Azure OpenAI paslaugos diegimą (taško prieigos vietą) su bent vienu GPT modeliu pokalbių užbaigimui.

Kitas žingsnis yra sukonfigūruoti jūsų **vietinius aplinkos kintamuosius** taip:

1. Pagrindiniame aplanke raskite `.env.copy` failą, kuris turėtų atrodyti taip:

   ```bash
   # OpenAI paslaugų teikėjas
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI Microsoft Foundry platformoje
   ## (Azure OpenAI paslauga dabar yra Microsoft Foundry dalis: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Numatytoji reikšmė nustatyta! (dabar esama stabilioji GA API versija)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry modeliai (daugiau paslaugų teikėjų modelių katalogas, pakeičia GitHub modelius, kurie bus nutraukti 2026 metų liepos pabaigoje)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Nukopijuokite jį į `.env` naudodami žemiau pateiktą komandą. Šis failas yra _gitignore mechanizme_, tad paslaptys išlieka saugios.

   ```bash
   cp .env.copy .env
   ```

3. Užpildykite reikšmes (pakeiskite dešinėje po `=` esančius žymeklius) kaip aprašyta kitame skyriuje.

4. (Pasirinktinai) Jei naudojate GitHub Codespaces, galite išsaugoti aplinkos kintamuosius kaip _Codespaces paslaptis_ susietas su šiuo repozitorium. Tokiu atveju nereikės kurti vietinio .env failo. **Tačiau atkreipkite dėmesį, kad ši galimybė veikia tik naudojant GitHub Codespaces.** Jei naudojate Docker Desktop, .env failą vis tiek reikės sukurti.

## Užpildykite `.env` failą

Pažvelkime greitai į kintamųjų pavadinimus, kad suprastume, ką jie reiškia:

| Kintamasis  | Aprašymas  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Tai vartotojo prieigos žetonas, kurį nustatėte savo profilyje |
| OPENAI_API_KEY | Tai autorizacijos raktas naudojant ne Azure OpenAI taško prieigos vietas |
| AZURE_OPENAI_API_KEY | Tai autorizacijos raktas naudojant Azure OpenAI paslaugą |
| AZURE_OPENAI_ENDPOINT | Tai diegta Azure OpenAI išteklių taško prieigos vieta |
| AZURE_OPENAI_DEPLOYMENT | Tai _teksto generavimo_ modelio diegimo taško prieigos vieta |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Tai _teksto įterpimų_ (embedding) modelio diegimo taško prieigos vieta |
| AZURE_INFERENCE_ENDPOINT | Tai jūsų Microsoft Foundry projekto taško prieigos vieta, naudojama Microsoft Foundry modeliams |
| AZURE_INFERENCE_CREDENTIAL | Tai API raktas jūsų Microsoft Foundry projektui |
| | |

Pastaba: Paskutiniai du Azure OpenAI kintamieji atspindi numatytą modelį pokalbių užbaigimui (teksto generavimui) ir vektorinėms paieškoms (embeddingams). Nurodymai juos nustatyti bus aprašyti atitinkamose užduotyse.

## Konfigūruokite Azure OpenAI: per Portalą

> **Pastaba:** Azure OpenAI paslauga dabar yra [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) dalis. Ištekliai ir diegimai vis dar matomi Azure portale, tačiau kasdienis modelių valdymas (diegimai, demonstracinė aplinka, stebėjimas) vyksta Foundry portale vietoj senojo atskiro "Azure OpenAI Studio".

Azure OpenAI taško prieigos vietos ir rakto reikšmes rasite [Azure Portale](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), tad pradėkime nuo ten.

1. Eikite į [Azure Portalą](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kairiajame meniu spustelėkite **Keys and Endpoint**.
1. Spauskite **Show Keys** – turėtumėte matyti: KEY 1, KEY 2 ir Endpoint.
1. Naudokite KEY 1 reikšmę kaip AZURE_OPENAI_API_KEY
1. Naudokite Endpoint reikšmę kaip AZURE_OPENAI_ENDPOINT

Toliau reikia rasti specifinių diegimų taško prieigos vietas.

1. Kairiajame meniu spauskite **Model deployments** jūsų Azure OpenAI ištekliui.
1. Nukreiptoje puslapio vietoje pasirinkite **Go to Microsoft Foundry portal** (arba **Manage Deployments**, priklausomai nuo jūsų išteklių tipo)

Tai nuves jus į Microsoft Foundry portalą, kur rasime kitus reikalingus duomenis, kaip aprašyta toliau.

## Konfigūruokite Azure OpenAI: per Microsoft Foundry portalą

1. Eikite į [Microsoft Foundry portalą](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **per savo išteklių**, kaip aprašyta aukščiau.
1. Skiltyje **Deployments** (kairiojoje šoninėje juostoje) peržiūrėkite šiuo metu diegiamus modelius.
1. Jei norimas modelis nėra diegiamas, naudokite **Deploy model** ir pasirinkite jį iš [modelių katalogo](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Jums reikės _teksto generavimo_ modelio – rekomenduojame: **gpt-5-mini**
1. Jums reikės _teksto įterpimų_ modelio – rekomenduojame **text-embedding-3-small**

Dabar atnaujinkite aplinkos kintamuosius, kad juose būtų nurodytas _Deployment name_, naudojamas diegimui. Tai paprastai yra tas pats, kas modelio pavadinimas, nebent jį eksplicitiškai pakeitėte. Pavyzdžiui, galite turėti:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Nepamirškite įrašyti .env failo pabaigus.** Dabar galite uždaryti failą ir grįžti prie užduočių vykdymo instrukcijų.

## Konfigūruokite OpenAI: Profile

Jūsų OpenAI API raktą rasite savo [OpenAI paskyroje](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jei neturite, susikurkite paskyrą ir susikurkite API raktą. Gavę raktą, naudokite jį reikšmei `OPENAI_API_KEY` `.env` faile.

## Konfigūruokite Hugging Face: Profile

Jūsų Hugging Face žetoną rasite savo profilyje po [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Neskelbkite jo viešai. Vietoje to susikurkite naują žetoną šiam projektui ir nukopijuokite jį į `.env` failą po kintamuoju `HUGGING_FACE_API_KEY`. _Pastaba:_ techniškai tai nėra API raktas, bet naudojama autentifikacijai, todėl laikome tokią pavadinimų konvenciją dėl nuoseklumo.

## Konfigūruokite Microsoft Foundry Models: per Portalą

> **Pastaba:** GitHub Models bus nutrauktos 2026 m. liepos pabaigoje. Microsoft Foundry Models yra tiesioginis pakeitimas, suteikiantis tokį pat nemokamo bandymo modelių katalogą bei Azure AI Inferencijos SDK / OpenAI SDK patirtį.

1. Eikite į [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) ir sukurkite (arba atidarykite) Foundry projektą.
1. Peržiūrėkite [modelių katalogą](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ir įdiekite modelį, pavyzdžiui `gpt-5-mini`.
1. Projekto **Overview** puslapyje nukopijuokite **taško prieigos vietos URL** ir **API raktą**.
1. Naudokite taško prieigos vietos URL reikšmei `AZURE_INFERENCE_ENDPOINT` ir raktą reikšmei `AZURE_INFERENCE_CREDENTIAL` savo `.env` faile.

## Neprisijungę / Vietiniai teikėjai

Jei nenorite visai naudoti debesų prenumeratos, suderinamus atvirus modelius galite paleisti tiesiogiai savo įrenginyje:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** – Microsoft įrenginio vykdymo aplinka. Ji automatiškai parenka geriausią vykdymo teikėją (NPU, GPU arba CPU) ir pateikia OpenAI suderinamą taško prieigos vietą, tad galite daugumą pavyzdinių šio kurso kodų naudoti beveik be pakeitimų. Pradžiai žiūrėkite [Foundry Local dokumentaciją](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) arba įdiekite naudodami `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** – populiari alternatyva atvirų modelių, tokių kaip Llama, Phi, Mistral ir Gemma, vietiniam paleidimui.


Žr. [19 pamoka: Statyba su SLM](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) praktinius pavyzdžius, kuriuose naudojamos abi galimybės.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->