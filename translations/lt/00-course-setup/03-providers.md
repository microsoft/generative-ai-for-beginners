<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b5b016b0eb8a1cef2e3097620d8aa23",
  "translation_date": "2025-12-19T17:54:52+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "lt"
}
-->
# LLM tiekėjo pasirinkimas ir konfigūravimas 🔑

Užduotys **gali** būti sukonfigūruotos taip, kad veiktų su vienu ar keliais dideliais kalbos modeliais (LLM) per palaikomą paslaugų tiekėją, pvz., OpenAI, Azure ar Hugging Face. Šie tiekėjai suteikia _hostintą galinį tašką_ (API), prie kurio galime programiškai prisijungti su tinkamais kredencialais (API raktu arba žetonu). Šiame kurse aptariame šiuos tiekėjus:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) su įvairiais modeliais, įskaitant pagrindinę GPT seriją.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI modeliams, orientuotiems į įmonių parengtį
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) atvirojo kodo modeliams ir inferencijos serveriui

**Šiems pratimams reikės naudoti savo paskyras**. Užduotys yra neprivalomos, todėl galite pasirinkti sukonfigūruoti vieną, visus arba nė vieno tiekėjo paslaugas pagal savo interesus. Štai keletas nurodymų registracijai:

| Registracija | Kaina | API raktas | Žaidimų aikštelė | Pastabos |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Kainodara](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektinis](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Be kodo, internetinė](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Galima naudoti kelis modelius |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Kainodara](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK greitas startas](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio greitas startas](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Prieigai būtina išankstinė paraiška](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Kainodara](https://huggingface.co/pricing) | [Prieigos žetonai](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat turi ribotą modelių skaičių](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Vadovaukitės žemiau pateiktomis instrukcijomis, kad _konfigūruotumėte_ šį saugyklą darbui su skirtingais tiekėjais. Užduotys, kurioms reikalingas konkretus tiekėjas, turės vieną iš šių žymų failo pavadinime:

- `aoai` - reikalauja Azure OpenAI galinio taško ir rakto
- `oai` - reikalauja OpenAI galinio taško ir rakto
- `hf` - reikalauja Hugging Face žetono

Galite konfigūruoti vieną, nė vieno arba visus tiekėjus. Susijusios užduotys tiesiog grąžins klaidą, jei trūks kredencialų.

## Sukurkite `.env` failą

Darome prielaidą, kad jau perskaitėte aukščiau pateiktas instrukcijas, užsiregistravote pas atitinkamą tiekėją ir gavote reikiamus autentifikacijos kredencialus (API_RAKTĄ arba žetoną). Azure OpenAI atveju darome prielaidą, kad turite galiojančią Azure OpenAI paslaugos diegimą (galinį tašką) su bent vienu GPT modeliu, skirtu pokalbių užbaigimui.

Kitas žingsnis – sukonfigūruoti savo **vietinius aplinkos kintamuosius** taip:

1. Pažiūrėkite šakninį katalogą, ar yra `.env.copy` failas, kuris turėtų atrodyti maždaug taip:

   ```bash
   # OpenAI tiekėjas
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Numatytoji reikšmė nustatyta!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Nukopijuokite tą failą į `.env` naudodami žemiau pateiktą komandą. Šis failas yra _gitignore_-intas, todėl paslaptys lieka saugios.

   ```bash
   cp .env.copy .env
   ```

3. Užpildykite reikšmes (pakeiskite dešinėje pusėje esančius vietos laikiklius) kaip aprašyta kitame skyriuje.

4. (Pasirinktinai) Jei naudojate GitHub Codespaces, galite išsaugoti aplinkos kintamuosius kaip _Codespaces paslaptis_, susietas su šiuo saugykla. Tokiu atveju jums nereikės kurti vietinio .env failo. **Tačiau atkreipkite dėmesį, kad ši galimybė veikia tik naudojant GitHub Codespaces.** Jei naudojate Docker Desktop, vis tiek reikės sukurti .env failą.

## Užpildykite `.env` failą

Greitai apžvelkime kintamųjų pavadinimus, kad suprastume, ką jie reiškia:

| Kintamasis  | Aprašymas  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Tai vartotojo prieigos žetonas, kurį nustatėte savo profilyje |
| OPENAI_API_KEY | Tai autorizacijos raktas, skirtas naudoti paslaugą ne Azure OpenAI galiniams taškams |
| AZURE_OPENAI_API_KEY | Tai autorizacijos raktas, skirtas naudoti tą paslaugą |
| AZURE_OPENAI_ENDPOINT | Tai diegimo galinis taškas Azure OpenAI ištekliui |
| AZURE_OPENAI_DEPLOYMENT | Tai _teksto generavimo_ modelio diegimo galinis taškas |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Tai _teksto įterpimų_ modelio diegimo galinis taškas |
| | |

Pastaba: Paskutiniai du Azure OpenAI kintamieji atspindi numatytąjį modelį pokalbių užbaigimui (teksto generavimui) ir vektorinėms paieškoms (įterpimams). Nurodymai, kaip juos nustatyti, bus pateikti atitinkamose užduotyse.

## Azure konfigūravimas: iš portalo

Azure OpenAI galinio taško ir rakto reikšmes rasite [Azure portale](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), tad pradėkime nuo ten.

1. Eikite į [Azure portalą](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Kairėje šoninėje juostoje spustelėkite **Keys and Endpoint** (Raktai ir galinis taškas).
1. Spustelėkite **Show Keys** (Rodyti raktus) – turėtumėte matyti: KEY 1, KEY 2 ir Endpoint.
1. Naudokite KEY 1 reikšmę kaip AZURE_OPENAI_API_KEY
1. Naudokite Endpoint reikšmę kaip AZURE_OPENAI_ENDPOINT

Toliau reikia gauti galinius taškus konkretiems mūsų diegtiems modeliams.

1. Kairėje šoninėje juostoje (meniu) Azure OpenAI ištekliui spustelėkite **Model deployments** (Modelių diegimai).
1. Nukreipimo puslapyje spustelėkite **Manage Deployments** (Tvarkyti diegimus)

Tai nukreips jus į Azure OpenAI Studio svetainę, kur rasime kitus reikalingus duomenis, kaip aprašyta žemiau.

## Azure konfigūravimas: iš Studio

1. Eikite į [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **iš savo ištekliaus**, kaip aprašyta aukščiau.
1. Spustelėkite skirtuką **Deployments** (Diegimai) (šoninė juosta, kairėje), kad pamatytumėte šiuo metu diegiamus modelius.
1. Jei norimas modelis nėra įdiegtas, naudokite **Create new deployment** (Sukurti naują diegimą), kad jį įdiegtumėte.
1. Jums reikės _teksto generavimo_ modelio – rekomenduojame: **gpt-35-turbo**
1. Jums reikės _teksto įterpimų_ modelio – rekomenduojame **text-embedding-ada-002**

Dabar atnaujinkite aplinkos kintamuosius, kad atspindėtų naudotą _Deployment name_ (diegimo pavadinimą). Paprastai tai bus tas pats, kas modelio pavadinimas, nebent jį aiškiai pakeitėte. Pavyzdžiui, galite turėti:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Nepamirškite išsaugoti .env failo pabaigus**. Dabar galite išeiti iš failo ir grįžti prie instrukcijų, kaip paleisti užrašų knygelę.

## OpenAI konfigūravimas: iš profilio

Jūsų OpenAI API raktą rasite savo [OpenAI paskyroje](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jei jo neturite, galite užsiregistruoti ir sukurti API raktą. Gavę raktą, galite jį įrašyti į `OPENAI_API_KEY` kintamąjį `.env` faile.

## Hugging Face konfigūravimas: iš profilio

Jūsų Hugging Face žetoną rasite savo profilyje skiltyje [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Neskelbkite ir nedalinkite jo viešai. Vietoje to sukurkite naują žetoną šiam projektui ir nukopijuokite jį į `.env` failą po kintamuoju `HUGGING_FACE_API_KEY`. _Pastaba:_ techniškai tai nėra API raktas, bet naudojamas autentifikacijai, todėl laikomės tokios pavadinimų konvencijos dėl nuoseklumo.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neatsakome už bet kokius nesusipratimus ar neteisingus aiškinimus, kilusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->