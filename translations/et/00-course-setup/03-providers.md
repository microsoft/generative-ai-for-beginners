# LLM-teenusepakkuja valimine ja seadistamine 🔑

Ülesandeid **võib** olla ka seadistatud töötama ühe või mitme suurkeele mudeliga (LLM) läbi toetatud teenusepakkuja nagu OpenAI, Azure või Hugging Face. Need pakuvad _hostitud lõpp-punkti_ (API), millele pääseme programmipõhiselt ligi koos õige autentimisandmetega (API võti või token). Selles kursuses käsitleme järgmisi pakkujaid:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) mitmekesiste mudelitega, kaasa arvatud põhiline GPT seeria.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI mudelite jaoks, mis on keskendunud ettevõtte valmisolekutele
 - [Microsoft Foundry mudelid](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ühe lõpp-punkti ja API võtmega sadade mudelite kasutamiseks OpenAI, Meta, Mistral, Cohere, Microsofti jt poolt (asendab GitHub Models, mis lõpetab teenuse 2026. aasta juuli lõpus)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) avatud lähtekoodiga mudelite ja järeldamisteenuse jaoks
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) või [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst), kui soovite mudelid täielikult offline'is oma seadmes käivitada, ilma pilve tellimuseta

**Nende harjutuste jaoks peate kasutama oma kontosid**. Ülesanded on vabatahtlikud, nii et võite valida ühe, kõik või mitte ühegi pakkuja seadistamise vastavalt oma eelistustele. Mõned juhised registreerimiseks:

| Registreeru | Hind | API võti | Mänguväljak | Kommentaarid |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Hinnakiri](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projekti-põhine](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Kodeerimata, veeb](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Mitmeid mudeleid saadaval |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Hinnakiri](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK kiire algus](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio kiire algus](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Juurdepääsu taotlemine eelnevalt vajalik](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Hinnakiri](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Projekt Ülevaate leht](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry mänguväljak](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Tasuta tase saadaval; üks lõpp-punkt + võti mitme mudeli pakkuja jaoks |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Hinnakiri](https://huggingface.co/pricing) | [Juurdepääsu tokenid](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chatis on piiratud mudelid](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Tasuta (töötab teie seadmes) | Ei ole vaja | [Kohalik CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Täielikult offline, OpenAI-ga ühilduv lõpp-punkt |
| | | | | |

Järgige allolevaid juhiseid, et _seadistada_ see hoidla erinevate pakkujatega kasutamiseks. Ülesanded, mis nõuavad konkreetset pakkujat, sisaldavad oma failinimes ühte nendest siltidest:

- `aoai` - nõuab Azure OpenAI lõpp-punkti, võtit
- `oai` - nõuab OpenAI lõpp-punkti, võtit
- `hf` - nõuab Hugging Face tokenit
- `githubmodels` - nõuab Microsoft Foundry mudelite lõpp-punkti, võtit (GitHub Models lõpetab teenuse 2026. aasta juuli lõpus)

Võite seadistada ühe, mitte ühegi või kõik pakkujad. Seotud ülesanded viskavad lihtsalt tõrkeid puuduvate autentimisandmete korral.

## Loo `.env` fail

Eeldame, et olete juba lugenud ülaltoodud juhiseid, registreerunud vastava pakkuja juures ja saanud vajalikud autentimisandmed (API_VÕTI või token). Azure OpenAI puhul eeldame, et teil on olemas ka kehtiv Azure OpenAI teenuse (lõpp-punkt) juurutus vähemalt ühe GPT mudeliga vestluse lõpetamiseks.

Järgmiseks seadistage oma **kohalikud keskkonnamuutujad** järgmiselt:

1. Otsige juurkataloogist `.env.copy` fail, mis sisaldab umbes sellist sisu:

   ```bash
   # OpenAI pakkuja
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI Microsoft Foundry's
   ## (Azure OpenAI teenus on nüüd osa Microsoft Foundryst: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Vaikimisi on seatud! (praegune stabiilne GA API versioon)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry mudelid (mitme pakkuja mudelikeerang, asendab GitHub mudelid, mis lõpetatakse 2026. aasta juuli lõpus)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopeerige see fail `.env` nime all järgmise käsuga. See fail on _gitignore-itud_, hoides saladused turvaliselt.

   ```bash
   cp .env.copy .env
   ```

3. Täitke väärtused (asendage kohatäitjad `=` parempoolsel poolel) järgmiselt kirjeldatud juhiste järgi.

4. (Valikuline) Kui kasutate GitHub Codespaces keskkonda, saate keskkonnamuutujad salvestada selle hoidla _Codespaces saladustena_. Sellisel juhul pole teil kohalikku .env faili vaja. **Kuid pange tähele, et see võimalus töötab ainult GitHub Codespaces kasutamisel.** Kui kasutate Docker Desktopi, peate siiski .env faili seadistama.

## Täitke `.env` fail

Vaatame üle muutujate nimed, et mõista, mida need tähendavad:

| Muutuja | Kirjeldus |
| :--- | :--- |
| HUGGING_FACE_API_KEY | See on kasutaja juurdepääsu token, mille seadistate oma profiilis |
| OPENAI_API_KEY | See on autoriseerimisvõti mitte-Azure OpenAI teenuste kasutamiseks |
| AZURE_OPENAI_API_KEY | See on autoriseerimisvõti selle teenuse kasutamiseks |
| AZURE_OPENAI_ENDPOINT | See on juurutatud Azure OpenAI ressursi lõpp-punkt |
| AZURE_OPENAI_DEPLOYMENT | See on _tekstigeneratsiooni_ mudeli juurutuse lõpp-punkt |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | See on _tekstilisandite_ mudeli juurutuse lõpp-punkt |
| AZURE_INFERENCE_ENDPOINT | See on teie Microsoft Foundry projekti lõpp-punkt Microsoft Foundry mudelite jaoks |
| AZURE_INFERENCE_CREDENTIAL | See on teie Microsoft Foundry projekti API võti |
| | |

Märkus: Viimased kaks Azure OpenAI muutujat viitavad vaikimisi mudelile vestluse lõpetamiseks (teksti genereerimine) ja vektoriotsinguks (lisandid) vastavalt. Nende seadistamise juhised määratakse ära asjakohastes ülesannetes.

## Azure OpenAI seadistamine: Portaalist

> **Märkus:** Azure OpenAI teenus on nüüd osa [Microsoft Foundry'st](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Ressursid ja juurutused kuvatakse endiselt Azure portaalis, kuid igapäevane mudelite haldamine (juurutused, mänguväljak, järelevalve) toimub nüüd Foundry portaalis, mitte vanas eraldiseisvas "Azure OpenAI Studio"-s.

Azure OpenAI lõpp-punkti ja võtit leiate [Azure portaalist](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), alustame sealt.

1. Minge [Azure portaali](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klõpsake küljeribal (vasakul menüüs) valikut **Keys and Endpoint**.
1. Klõpsake **Show Keys** - näete järgmist: KEY 1, KEY 2 ja Endpoint.
1. Kasutage KEY 1 väärtust AZURE_OPENAI_API_KEY jaoks
1. Kasutage Endpoint väärtust AZURE_OPENAI_ENDPOINT jaoks

Järgmisena vajame konkreetselt juurutatud mudelite lõpp-punkte.

1. Klõpsake sidebaris (vasakul menüüs) Azure OpenAI ressursi valikul **Model deployments**.
1. Sihtlehel klõpsake **Go to Microsoft Foundry portal** (või **Manage Deployments** sõltuvalt teie ressursi tüübist)

See viib teid Microsoft Foundry portaali, kust leiame ülejäänud väärtused, nagu allpool kirjeldatud.

## Azure OpenAI seadistamine: Microsoft Foundry portaalist

1. Minge [Microsoft Foundry portaalis](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **oma ressursi kaudu**, nagu ülalpool kirjeldatud.
1. Klõpsake vasakul küljeribal **Deployments** vahekaarti, et näha praegu juurutatud mudeleid.
1. Kui soovitud mudelit pole juurutatud, kasutage **Deploy model** selle juurutamiseks [mudelikataloogist](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Teil on vaja _tekstigeneratsiooni_ mudelit - soovitame: **gpt-4o-mini**
1. Teil on vaja _tekstilisandite_ mudelit - soovitame **text-embedding-3-small**

Nüüd uuendage keskkonnamuutujaid, et kajastada kasutatavat _Juurutuse nime_. Tavaliselt on see sama mis mudeli nimi, kui te seda eraldi ei muutnud. Näiteks võib teil olla:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Ärge unustage .env faili salvestada, kui valmis**. Võite nüüd failist väljuda ja jätkata märkmiku käivitamise juhistega.

## OpenAI seadistamine: Profiilist

Oma OpenAI API võtit leiate oma [OpenAI kontolt](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Kui teil seda veel pole, saate konto registreerida ja luua API võtme. Kui võtme olete saanud, kasutage seda `OPENAI_API_KEY` muutujasse `.env` failis.

## Hugging Face seadistamine: Profiilist

Oma Hugging Face tokenit leiate oma profiilis alajaotisest [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Ärge jagage neid avalikult. Selle asemel looge selle projekti jaoks uus token ja kopeerige see `.env` faili `HUGGING_FACE_API_KEY` muutujasse. _Märkus:_ See ei ole tehniliselt API võti, kuid kasutatakse autentimiseks, seega kasutame selleks sama nimetust järjepidevuse tagamiseks.

## Microsoft Foundry mudelite seadistamine: Portaalist

> **Märkus:** GitHub Models lõpetab teenuse 2026. aasta juuli lõpus. Microsoft Foundry mudelid on otsene asendus, pakkudes sama tasuta katsetatav mudelikataloogi ning Azure AI Inference SDK / OpenAI SDK kogemust.

1. Minge [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) ja looge (või avage) Foundry projekt.
1. Sirvige [mudelikataloogi](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ja juurutage mudel, näiteks `gpt-4o-mini`.
1. Kopeerige projekti **Overview** lehelt **lõpp-punkt** ja **API võti**.
1. Kasutage lõpp-punkti väärtust `AZURE_INFERENCE_ENDPOINT` ja võtit väärtust `AZURE_INFERENCE_CREDENTIAL` muutujates oma `.env` failis.

## Offline / kohalikud pakkujad

Kui te ei soovi üldse pilve tellimust kasutada, võite ühildub avatud mudeleid käivitada otse oma seadmes:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsofti seadmel lokaliseeritud käituskeskkond. See valib automaatselt parima käitusteenuse (NPU, GPU või CPU) ning pakub OpenAI-ga ühilduvat lõpp-punkti, nii et saate selles kursuses olevaid näidiskoodis kasutada minimaalseid muudatusi. Alustamiseks vaadake [Foundry Local dokumentatsiooni](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) või installige käskudega `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - populaarne alternatiiv avatud mudelite, nagu Llama, Phi, Mistral ja Gemma kohapealseks käitamiseks.


Vaadake [Õppetund 19: Ehitamine SLM-idega](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) praktiliste näidete jaoks, mis kasutavad mõlemat võimalust.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->