# LLM-teenuse pakkuja valimine ja seadistamine 🔑

Ülesandeid **vähemalt** on võimalik seadistada töötama ühe või mitme Suure Keelemudeli (LLM) jaotuse vastu toetatud teenusepakkuja kaudu nagu OpenAI, Azure või Hugging Face. Need pakuvad _majutatavat lõpp-punkti_ (API), millele pääseme programmeerimiselt ligi õige volitusega (API-võti või token). Selles kursuses käsitleme neid pakkujaid:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) mitmesuguste mudelitega, sealhulgas põhilise GPT seeriaga.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) OpenAI mudelite jaoks, keskendudes ettevõttesisesele valmidusele
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ühe lõpp-punkti ja API-võtmega, et pääseda sadadele mudelitele OpenAI, Meta, Mistral, Cohere, Microsoft jt juures (asendab GitHub Modelsi, mis lõpetab töösu juulis 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) avatud lähtekoodiga mudelite ja järeldusteenuse jaoks
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) või [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst), kui soovid mudelid täielikult võrguühenduseta enda seadmes käivitada ilma pilveteenuse tellimuseta

**Nende harjutuste jaoks pead kasutama oma kontosid**. Ülesanded on vabatahtlikud, nii et saad valikuliselt seadistada ühe, kõigi või ühegi pakkuja vastavalt oma huvidele. Mõni juhend registreerumiseks:

| Registreerumine | Hind | API võti | Testikeskkond | Kommentaarid |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Hindamine](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektipõhine](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Lihtne veebikeskkond](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Mitmed mudelid saadaval |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Hindamine](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK algusjuhend](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio algusjuhend](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Juurdepääsuks tuleb eelnevalt taotleda](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Hindamine](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Projekti ülevaate leht](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Testikeskkond](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Tasuta tase saadaval; üks lõpp-punkt ja võti mitme mudelipakkuja jaoks |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Hind](https://huggingface.co/pricing) | [Juurdepääsu tokenid](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat toetab piiratud mudelite valikut](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Tasuta (jookseb sinu seadmes) | Ei ole vajalik | [Kohalik CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Täielikult võrguühenduseta, OpenAI-ga ühilduv lõpp-punkt |
| | | | | |

Järgi alljärgnevaid juhiseid selle hoidla _konfigureerimiseks_ erinevate pakkujatega kasutamiseks. Ülesanded, mis vajavad kindlat pakkujat, sisaldavad vastavat märgendit faili nimes:

- `aoai` - nõuab Azure OpenAI lõpp-punkti ja võtit
- `oai` - nõuab OpenAI lõpp-punkti ja võtit
- `hf` - nõuab Hugging Face tokenit
- `githubmodels` - nõuab Microsoft Foundry Models lõpp-punkti ja võtit (GitHub Models lõpetab juulis 2026)

Sa võid konfigureerida ühe, mitme või ühegi pakkuja. Seotud ülesanded annavad vigadega vastuse, kui volitusi ei ole.

## Loo `.env` fail

Eeldame, et oled eelnevalt lugenud ülaltoodud juhiseid ja registreerunud sobiva pakkuja juurde ning saanud vajalikud autentimismärgid (API_VÕTI või token). Azure OpenAI puhul eeldame ka, et sul on kehtiv Azure OpenAI teenuse jaotus (lõpp-punkt), kus üks GPT mudel on vestluskompletsiooni jaoks kasutusele võetud.

Järgmine samm on seadistada oma **kohalikud keskkonnamuutujad** järgmiselt:

1. Otsi juurkataloogist faili `.env.copy`, mille sisu peaks olema selline:

   ```bash
   # OpenAI pakkuja
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI Microsoft Foundrys
   ## (Azure OpenAI teenus on nüüd osa Microsoft Foundry'st: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Vaikimisi on seadistatud! (praegune stabiilne GA API versioon)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry mudelid (mitme pakkuja mudelikataloog, asendab GitHub mudelid, mis lõpetatakse 2026. aasta juuli lõpus)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopeeri see fail nimega `.env` alljärgneva käsuga. See fail on _gitignore-s_, hoides saladused turvaliselt.

   ```bash
   cp .env.copy .env
   ```

3. Täida väärtused (asenda parempoolsed kohatäited) alljärgnevatel juhistel.

4. (Valikuline) Kui kasutad GitHub Codespaces’i, võid salvestada keskkonnamuutujad kui _Codespaces’i saladused_ seoses selle hoidlaga. Sellisel juhul pole vaja kohalikku .env faili seadistada. **Kuid märgi, et see võimalus toimib ainult GitHub Codespaces’i kasutamisel.** Docker Desktopi puhul pead siiski .env faili seadistama.

## Täida `.env` fail

Vaatame kiiresti üle muutuja nimed, et aru saada, mida need tähendavad:

| Muutuja  | Kirjeldus  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Kasutaja juurdepääsu token, mille seadistad oma profiilis |
| OPENAI_API_KEY | Autoriseerimisvõti teenuse kasutamiseks ilma Azure OpenAI lõpp-punktita |
| AZURE_OPENAI_API_KEY | Autoriseerimisvõti selle teenuse kasutamiseks |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI ressursi kasutusel olev lõpp-punkt |
| AZURE_OPENAI_DEPLOYMENT | _Teksti genereerimise_ mudeli jaotuste lõpp-punkt |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _Teksti sissekandjate_ mudeli jaotuste lõpp-punkt |
| AZURE_INFERENCE_ENDPOINT | Microsoft Foundry projekti lõpp-punkt Microsoft Foundry mudelite jaoks |
| AZURE_INFERENCE_CREDENTIAL | Microsoft Foundry projekti API võti |
| | |

Märkus: Viimased kaks Azure OpenAI muutujat peegeldavad vaikimisi mudelit vestluskompletsiooni (tekstimudel) ja vektoripäringu (sissekanded) jaoks vastavalt. Juhised nende seadistamiseks antakse seotud ülesannetes.

## Azure OpenAI seadistamine: Portaalist

> **Märkus:** Azure OpenAI teenus on nüüd osa [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) platvormist. Ressursid ja jaotused on endiselt nähtavad Azure Portaalis, kuid igapäevane mudelite haldus (jaotused, testikeskkond, järelevalve) toimub nüüd Foundry portaalis, mitte vanas eraldi "Azure OpenAI Studio" keskkonnas.

Azure OpenAI lõpp-punkt ja võti leitakse [Azure Portaalist](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), alustame sealt.

1. Mine aadressile [Azure Portaal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Vali vasakpoolsest menüüst **Keys and Endpoint** valik.
1. Klõpsa **Show Keys** - peaksid nägema: KEY 1, KEY 2 ja Endpoint.
1. Kasuta KEY 1 väärtust `AZURE_OPENAI_API_KEY` jaoks.
1. Kasuta Endpoint väärtust `AZURE_OPENAI_ENDPOINT` jaoks.

Järgmine samm on meie paigaldatud konkreetsete mudelite lõpp-punktide leidmine.

1. Vali Azure OpenAI ressursi vasakpoolsest menüüst **Model deployments**.
1. Sihtlehel vali **Go to Microsoft Foundry portal** (või **Manage Deployments**, olenevalt ressursti tüübist)

See viib sind Microsoft Foundry portaalisse, kust otsime teised vajalikud väärtused.

## Azure OpenAI seadistamine: Microsoft Foundry portaalist

1. Liigu [Microsoft Foundry portaali](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **oma ressursi kaudu**, nagu eespool kirjeldatud.
1. Vali vasakul **Deployments** sakk, et näha hetkel kasutusel olevaid mudeleid.
1. Kui sinu soovitud mudel pole paigaldatud, kasuta **Deploy model** valikut mudeli lisamiseks [mudelite kataloogist](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Sul on vaja _teksti genereerimise_ mudelit - soovitame: **gpt-5-mini**
1. Sul on vaja _teksti sissekandjate_ mudelit - soovitame **text-embedding-3-small**

Uuenda keskkonnamuutujad, et kajastada _Deployment name_ kasutatut. Tavaliselt on see sama mis mudeli nimi, kui seda pole eraldi muudetud. Näiteks võiks olla:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Ära unusta .env faili salvestada peale muudatuste tegemist**. Võid faili sulgeda ja jätkata mälestustöö raamistiku järgimist.

## OpenAI seadistamine: Profiiilist

Oma OpenAI API võtit leiad oma [OpenAI kontol](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Kui võtit veel pole, registreeru ja loo see API võti. Seejärel aseta `OPENAI_API_KEY` muutujasse `.env` failis.

## Hugging Face seadistamine: Profiiilist

Oma Hugging Face tokeni leiad profiili juures [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) alt. Ära avalikusta ega jaga neid avalikult. Selle projekti jaoks loo uus token ja kopeeri see `.env` faili `HUGGING_FACE_API_KEY` muutujasse. _Märkus:_ See pole tehniliselt API võti, kuid kasutatakse autentimiseks, seega kasutame samas nimetust ühtsuse huvides.

## Microsoft Foundry Models seadistamine: Portaalist

> **Märkus:** GitHub Models lõpetab juulis 2026. Microsoft Foundry Models on otseasendus, pakkudes sama tasuta proovimiseks mõeldud mudelivalikut ja Azure AI Inference SDK / OpenAI SDK kogemust.

1. Mine aadressile [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) ja loo (või ava) Foundry projekt.
1. Sirvi [mudelite kataloogi](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ja paigalda mudel, näiteks `gpt-5-mini`.
1. Projekti **ülevaate** lehel kopeeri **lõpp-punkt** ja **API võti** väärtused.
1. Kasuta endpointi väärtust `AZURE_INFERENCE_ENDPOINT` ja võtit `AZURE_INFERENCE_CREDENTIAL` muutuja väärtustena `.env` failis.

## Võrguühenduseta / kohalike pakkujate seadistamine

Kui sa ei soovi üldse pilveteenuse tellimust kasutada, võid käivitada ühilduvaid avatud mudeleid otse oma seadmes:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsofti seadmepõhine käituskeskkond. Valib automaatselt parima käituskeskkonna (NPU, GPU või CPU) ja pakub OpenAI-ga ühilduvat lõpp-punkti, nii et saad selle kursuse näidiskoodi suuresti muutmata kasutada. Vaata [Foundry Local dokumentatsiooni](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) alustamiseks või paigalda käsuga `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - populaarne alternatiiv avatud mudelite nagu Llama, Phi, Mistral ja Gemma kohalikuks käivitamiseks.


Vaadake [Õppetund 19: SLM-idega ehitamine](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) praktiliste näidete jaoks, kasutades mõlemat valikut.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->