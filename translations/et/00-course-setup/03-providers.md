<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-10-11T11:42:24+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "et"
}
-->
# LLM-teenusepakkuja valimine ja seadistamine 🔑

Ülesanded **võivad** olla seadistatud töötama ühe või mitme suure keelemudeli (LLM) juurutusega, kasutades toetatud teenusepakkujat nagu OpenAI, Azure või Hugging Face. Need pakuvad _hostitud lõpp-punkti_ (API), millele saame õigete volitustega (API-võti või token) programmiliselt ligi pääseda. Selles kursuses käsitleme järgmisi teenusepakkujaid:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) mitmekesiste mudelitega, sealhulgas GPT-seeria põhiversioonid.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI mudelitega, keskendudes ettevõttevalmidusele.
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) avatud lähtekoodiga mudelite ja järeldusserveri jaoks.

**Nende harjutuste jaoks peate kasutama oma kontosid**. Ülesanded on valikulised, seega saate vastavalt oma huvidele seadistada ühe, kõik või mitte ühtegi teenusepakkujat. Mõned juhised registreerumiseks:

| Registreerumine | Hind | API-võti | Mänguväljak | Kommentaarid |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Hinnakiri](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projekti põhine](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, veeb](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Saadaval mitmed mudelid |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Hinnakiri](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK kiirstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio kiirstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Ligipääsuks tuleb eelnevalt taotleda](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Hinnakiri](https://huggingface.co/pricing) | [Ligipääsu tokenid](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chatil on piiratud mudelivalik](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Järgige allolevaid juhiseid, et _seadistada_ see repositoorium erinevate teenusepakkujate kasutamiseks. Ülesanded, mis nõuavad konkreetset teenusepakkujat, sisaldavad ühte järgmistest märgenditest oma failinimes:

- `aoai` - nõuab Azure OpenAI lõpp-punkti ja võtit
- `oai` - nõuab OpenAI lõpp-punkti ja võtit
- `hf` - nõuab Hugging Face tokenit

Võite seadistada ühe, mitte ühegi või kõik teenusepakkujad. Seotud ülesanded annavad lihtsalt veateate, kui volitused puuduvad.

## Loo `.env` fail

Eeldame, et olete juba lugenud ülaltoodud juhiseid, registreerunud vastava teenusepakkuja juures ja hankinud vajalikud autentimisvolitused (API_KEY või token). Azure OpenAI puhul eeldame, et teil on ka kehtiv Azure OpenAI teenuse juurutus (lõpp-punkt), kus on vähemalt üks GPT-mudel vestluse lõpetamiseks juurutatud.

Järgmine samm on **kohalike keskkonnamuutujate** seadistamine järgmiselt:

1. Otsige juurkaustast `.env.copy` fail, mille sisu peaks olema järgmine:

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

2. Kopeerige see fail `.env` failiks, kasutades allolevat käsku. See fail on _gitignore-d_, hoides saladusi turvaliselt.

   ```bash
   cp .env.copy .env
   ```

3. Täitke väärtused (asendage kohatäited `=` paremal küljel) nagu kirjeldatud järgmises jaotises.

4. (Valikuline) Kui kasutate GitHub Codespaces'i, on teil võimalus salvestada keskkonnamuutujad _Codespaces'i saladustena_, mis on seotud selle repositooriumiga. Sel juhul ei pea te kohalikku .env faili seadistama. **Pange siiski tähele, et see valik töötab ainult GitHub Codespaces'i kasutamisel.** Kui kasutate Docker Desktopi, peate siiski seadistama .env faili.

## Täida `.env` fail

Vaatame kiiresti muutujate nimesid, et mõista, mida need tähistavad:

| Muutuja  | Kirjeldus  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | See on kasutaja ligipääsu token, mille seadistate oma profiilis |
| OPENAI_API_KEY | See on autoriseerimisvõti teenuse kasutamiseks mitte-Azure OpenAI lõpp-punktide jaoks |
| AZURE_OPENAI_API_KEY | See on autoriseerimisvõti selle teenuse kasutamiseks |
| AZURE_OPENAI_ENDPOINT | See on juurutatud lõpp-punkt Azure OpenAI ressursi jaoks |
| AZURE_OPENAI_DEPLOYMENT | See on _teksti genereerimise_ mudeli juurutuse lõpp-punkt |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | See on _teksti sisestuste_ mudeli juurutuse lõpp-punkt |
| | |

Märkus: Kaks viimast Azure OpenAI muutujat kajastavad vaikimisi mudelit vestluse lõpetamiseks (teksti genereerimine) ja vektoriotsinguks (sisestused). Juhised nende seadistamiseks antakse vastavates ülesannetes.

## Azure'i seadistamine: portaalist

Azure OpenAI lõpp-punkti ja võtme väärtused leiate [Azure'i portaalist](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), seega alustame sealt.

1. Minge [Azure'i portaalile](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klõpsake külgribal (vasak menüü) valikut **Keys and Endpoint**.
1. Klõpsake **Show Keys** - peaksite nägema järgmist: KEY 1, KEY 2 ja Endpoint.
1. Kasutage KEY 1 väärtust AZURE_OPENAI_API_KEY jaoks.
1. Kasutage Endpoint väärtust AZURE_OPENAI_ENDPOINT jaoks.

Järgmisena vajame konkreetsete juurutatud mudelite lõpp-punkte.

1. Klõpsake Azure OpenAI ressursi külgribal (vasak menüü) valikut **Model deployments**.
1. Sihtlehel klõpsake **Manage Deployments**.

See viib teid Azure OpenAI Studio veebisaidile, kus leiame muud väärtused, nagu allpool kirjeldatud.

## Azure'i seadistamine: Studio kaudu

1. Navigeerige [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **oma ressursist**, nagu eespool kirjeldatud.
1. Klõpsake külgribal (vasakul) vahekaarti **Deployments**, et näha praegu juurutatud mudeleid.
1. Kui teie soovitud mudel pole juurutatud, kasutage **Create new deployment**, et see juurutada.
1. Teil on vaja _teksti genereerimise_ mudelit - soovitame: **gpt-35-turbo**.
1. Teil on vaja _teksti sisestuste_ mudelit - soovitame **text-embedding-ada-002**.

Nüüd värskendage keskkonnamuutujaid, et kajastada kasutatud _Deployment name_. See on tavaliselt sama mis mudeli nimi, kui te seda spetsiaalselt ei muutnud. Näiteks võib teil olla:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Ärge unustage .env faili salvestada, kui olete valmis**. Nüüd saate failist väljuda ja naasta juhiste juurde, et märkmikku käivitada.

## OpenAI seadistamine: profiilist

Teie OpenAI API-võti on leitav teie [OpenAI kontolt](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Kui teil seda pole, saate registreeruda kontole ja luua API-võtme. Kui teil on võti, saate selle kasutada `.env` failis `OPENAI_API_KEY` muutuja täitmiseks.

## Hugging Face seadistamine: profiilist

Teie Hugging Face token on leitav teie profiilis [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) all. Ärge postitage ega jagage neid avalikult. Selle asemel looge selle projekti jaoks uus token ja kopeerige see `.env` faili `HUGGING_FACE_API_KEY` muutuja alla. _Märkus:_ See ei ole tehniliselt API-võti, kuid seda kasutatakse autentimiseks, seega säilitame selle nimetamise konventsiooni järjepidevuse huvides.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.