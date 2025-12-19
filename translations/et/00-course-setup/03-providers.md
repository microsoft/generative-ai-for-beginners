<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b5b016b0eb8a1cef2e3097620d8aa23",
  "translation_date": "2025-12-19T18:08:41+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "et"
}
-->
# LLM-teenusepakkuja valimine ja seadistamine 🔑

Ülesandeid **võib** seadistada töötama ühe või mitme suure keelemudeli (LLM) juurutusega läbi toetatud teenusepakkuja nagu OpenAI, Azure või Hugging Face. Need pakuvad _hostitud lõpp-punkti_ (API), millele saame programmeerimislikult ligi pääseda õige autentimisandmega (API võti või token). Selles kursuses käsitleme järgmisi pakkujaid:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) mitmekesiste mudelitega, sealhulgas põhine GPT seeria.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI mudelitele, keskendudes ettevõtte valmisolekule
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) avatud lähtekoodiga mudelitele ja inferentsiserverile

**Nende harjutuste jaoks peate kasutama oma kontosid**. Ülesanded on valikulised, nii et saate valida ühe, kõik või mitte ühegi pakkuja seadistamise vastavalt oma huvidele. Mõned juhised registreerumiseks:

| Registreerumine | Hind | API võti | Mänguväljak | Kommentaarid |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Hinnakiri](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektipõhine](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Ilma koodita, veeb](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Mitmed mudelid saadaval |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Hinnakiri](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK kiire algus](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio kiire algus](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Juurdepääsuks tuleb eelnevalt taotleda](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Hinnakiri](https://huggingface.co/pricing) | [Juurdepääsu tokenid](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chatil on piiratud mudelid](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Järgige alltoodud juhiseid, et _seadistada_ see hoidla erinevate pakkujate kasutamiseks. Ülesanded, mis nõuavad konkreetset pakkujat, sisaldavad oma failinimes ühte järgmistest siltidest:

- `aoai` - nõuab Azure OpenAI lõpp-punkti ja võtit
- `oai` - nõuab OpenAI lõpp-punkti ja võtit
- `hf` - nõuab Hugging Face tokenit

Võite seadistada ühe, mitte ühegi või kõik pakkujad. Seotud ülesanded annavad lihtsalt veateate, kui autentimisandmed puuduvad.

## Loo `.env` fail

Eeldame, et olete juba lugenud ülaltoodud juhiseid, registreerunud vastava pakkuja juures ja saanud vajalikud autentimisandmed (API_VÕTI või token). Azure OpenAI puhul eeldame, et teil on ka kehtiv Azure OpenAI teenuse juurutus (lõpp-punkt) vähemalt ühe GPT mudeliga vestluse täitmiseks.

Järgmine samm on seadistada oma **kohalikud keskkonnamuutujad** järgmiselt:

1. Otsige juurkataloogist `.env.copy` fail, mille sisu peaks olema selline:

   ```bash
   # OpenAI pakkuja
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Vaikimisi on seatud!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopeerige see fail `.env`-iks alltoodud käsuga. See fail on _gitignore_-datud, hoides saladused turvaliselt.

   ```bash
   cp .env.copy .env
   ```

3. Täitke väärtused (asendage paremal pool olevad kohatäited) vastavalt järgmises jaotises kirjeldatule.

4. (Valikuline) Kui kasutate GitHub Codespaces, saate keskkonnamuutujad salvestada selle hoidla juurde seotud _Codespaces saladustena_. Sel juhul ei pea kohalikku .env faili seadistama. **Kuid pange tähele, et see valik töötab ainult GitHub Codespaces kasutamisel.** Kui kasutate Docker Desktopi, peate siiski .env faili seadistama.

## Täitke `.env` fail

Vaatame kiiresti muutuja nimesid, et mõista, mida need tähendavad:

| Muutuja  | Kirjeldus  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | See on kasutaja juurdepääsu token, mille seadistasite oma profiilis |
| OPENAI_API_KEY | See on autoriseerimisvõti teenuse kasutamiseks mitte-Azure OpenAI lõpp-punktide puhul |
| AZURE_OPENAI_API_KEY | See on autoriseerimisvõti selle teenuse kasutamiseks |
| AZURE_OPENAI_ENDPOINT | See on juurutatud lõpp-punkt Azure OpenAI ressursile |
| AZURE_OPENAI_DEPLOYMENT | See on _teksti genereerimise_ mudeli juurutuse lõpp-punkt |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | See on _teksti manuste_ mudeli juurutuse lõpp-punkt |
| | |

Märkus: Viimased kaks Azure OpenAI muutujat viitavad vaikimisi mudelile vestluse täitmiseks (teksti genereerimine) ja vektoriotsinguks (manused). Nende seadistamise juhised määratakse vastavates ülesannetes.

## Azure seadistamine: Portaalist

Azure OpenAI lõpp-punkti ja võtme väärtused leiate [Azure portaalist](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), alustame sealt.

1. Minge [Azure portaali](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klõpsake külgribal (vasakul menüüs) valikut **Keys and Endpoint**.
1. Klõpsake **Show Keys** - peaksite nägema järgmist: KEY 1, KEY 2 ja Endpoint.
1. Kasutage KEY 1 väärtust AZURE_OPENAI_API_KEY jaoks
1. Kasutage Endpoint väärtust AZURE_OPENAI_ENDPOINT jaoks

Järgmisena vajame konkreetsete juurutatud mudelite lõpp-punkte.

1. Klõpsake külgribal (vasakul menüüs) valikut **Model deployments** Azure OpenAI ressursi jaoks.
1. Sihtlehel klõpsake **Manage Deployments**

See viib teid Azure OpenAI Studio veebisaidile, kus leiame allpool kirjeldatud muud väärtused.

## Azure seadistamine: Studiost

1. Navigeerige [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **oma ressursist** nagu eespool kirjeldatud.
1. Klõpsake vahekaarti **Deployments** (vasak külgriba), et vaadata praegu juurutatud mudeleid.
1. Kui soovitud mudel pole juurutatud, kasutage **Create new deployment**, et see juurutada.
1. Teil on vaja _teksti genereerimise_ mudelit - soovitame: **gpt-35-turbo**
1. Teil on vaja _teksti manustamise_ mudelit - soovitame **text-embedding-ada-002**

Nüüd uuendage keskkonnamuutujaid, et kajastada kasutatud _Deployment name_. Tavaliselt on see sama mis mudeli nimi, kui te pole seda eksplicitse muutnud. Näiteks võite omada:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Ärge unustage .env faili salvestada, kui olete lõpetanud**. Võite nüüd faili sulgeda ja naasta juhiste juurde, kuidas märkmikku käivitada.

## OpenAI seadistamine: Profiilist

Teie OpenAI API võti on leitav teie [OpenAI kontolt](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Kui teil seda veel pole, saate konto registreerida ja luua API võtme. Kui võtme olete saanud, saate selle sisestada `.env` faili muutujasse `OPENAI_API_KEY`.

## Hugging Face seadistamine: Profiilist

Teie Hugging Face token on leitav teie profiilis jaotises [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Ärge postitage ega jagage neid avalikult. Selle asemel looge selle projekti jaoks uus token ja kopeerige see `.env` faili muutujasse `HUGGING_FACE_API_KEY`. _Märkus:_ See ei ole tehniliselt API võti, kuid seda kasutatakse autentimiseks, seega hoiame selle nimetuse järjepidevuse huvides.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud kasutades tehisintellekti tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->