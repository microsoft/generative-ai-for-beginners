<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df44972d5575ea8cef3c52ee31696d04",
  "translation_date": "2025-12-19T16:30:32+00:00",
  "source_file": "14-the-generative-ai-application-lifecycle/README.md",
  "language_code": "sw"
}
-->
[![Kuunganisha na kuitwa kwa kazi](../../../translated_images/sw/14-lesson-banner.066d74a31727ac12.png)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Mzunguko wa Maisha wa Programu ya AI Inayozalisha

Swali muhimu kwa programu zote za AI ni umuhimu wa vipengele vya AI, kwani AI ni uwanja unaobadilika haraka, kuhakikisha kwamba programu yako inabaki kuwa ya maana, ya kuaminika, na imara, unahitaji kuifuatilia, kuipima, na kuiboresha kwa kuendelea. Hapa ndipo mzunguko wa maisha wa AI inayozalisha unapoingia.

Mzunguko wa maisha wa AI inayozalisha ni mfumo unaokuongoza kupitia hatua za kuendeleza, kupeleka, na kudumisha programu ya AI inayozalisha. Inakusaidia kufafanua malengo yako, kupima utendaji wako, kubaini changamoto zako, na kutekeleza suluhisho zako. Pia inakusaidia kuoanisha programu yako na viwango vya maadili na sheria za eneo lako na wadau wako. Kwa kufuata mzunguko wa maisha wa AI inayozalisha, unaweza kuhakikisha kwamba programu yako daima inatoa thamani na kuridhisha watumiaji wako.

## Utangulizi

Katika sura hii, utajifunza:

- Kuelewa Mabadiliko ya Mtazamo kutoka MLOps hadi LLMOps
- Mzunguko wa Maisha wa LLM
- Zana za Mzunguko wa Maisha
- Upimaji na Tathmini ya Mzunguko wa Maisha

## Kuelewa Mabadiliko ya Mtazamo kutoka MLOps hadi LLMOps

LLM ni zana mpya katika silaha ya Akili Bandia, ni zenye nguvu sana katika kazi za uchambuzi na uzalishaji kwa programu, hata hivyo nguvu hii ina matokeo fulani katika jinsi tunavyoratibu kazi za AI na Kujifunza kwa Mashine Kawaida.

Kwa hili, tunahitaji Mtazamo mpya kuoanisha zana hii kwa njia ya mabadiliko, na motisha sahihi. Tunaweza kuainisha programu za AI za zamani kama "Programu za ML" na programu mpya za AI kama "Programu za GenAI" au tu "Programu za AI", zikionyesha teknolojia na mbinu kuu zinazotumika wakati huo. Hii inabadilisha simulizi yetu kwa njia nyingi, angalia kulinganisha ifuatayo.

![Ulinganisho wa LLMOps na MLOps](../../../translated_images/sw/01-llmops-shift.29bc933cb3bb0080.png)

Tambua kwamba katika LLMOps, tunazingatia zaidi Waendelezaji wa Programu, tukitumia muunganiko kama kipengele muhimu, tukitumia "Mifano-kama-Huduma" na kufikiria katika pointi zifuatazo kwa vipimo.

- Ubora: Ubora wa majibu
- Madhara: AI yenye uwajibikaji
- Uaminifu: Msingi wa majibu (Ina maana? Ni sahihi?)
- Gharama: Bajeti ya Suluhisho
- Ucheleweshaji: Muda wa wastani wa jibu la tokeni

## Mzunguko wa Maisha wa LLM

Kwanza, kuelewa mzunguko wa maisha na mabadiliko, tuchukue picha ifuatayo.

![Picha ya LLMOps](../../../translated_images/sw/02-llmops.70a942ead05a7645.png)

Kama unavyoona, hii ni tofauti na Mzunguko wa Maisha wa kawaida wa MLOps. LLM zina mahitaji mapya mengi, kama Kuamsha, mbinu tofauti za kuboresha ubora (Fine-Tuning, RAG, Meta-Prompts), tathmini tofauti na uwajibikaji wa AI yenye uwajibikaji, na mwisho, vipimo vipya vya tathmini (Ubora, Madhara, Uaminifu, Gharama na Ucheleweshaji).

Kwa mfano, angalia jinsi tunavyobuni mawazo. Kutumia uhandisi wa prompt kujaribu LLM mbalimbali kuchunguza uwezekano wa kujaribu kama Nadharia zao zinaweza kuwa sahihi.

Tambua kwamba hii si mfululizo wa moja kwa moja, bali ni mizunguko iliyojumuishwa, ya kurudia na yenye mzunguko mkubwa.

Tunawezaje kuchunguza hatua hizo? Tuchunguze kwa undani jinsi tunavyoweza kujenga mzunguko wa maisha.

![Mtiririko wa Kazi wa LLMOps](../../../translated_images/sw/03-llm-stage-flows.3a1e1c401235a6cf.png)

Hii inaweza kuonekana ngumu kidogo, tuchukulie hatua kubwa tatu kwanza.

1. Kubuni/Kuchunguza: Uchunguzi, hapa tunaweza kuchunguza kulingana na mahitaji ya biashara yetu. Kutengeneza mfano, kuunda [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) na kujaribu kama ni bora vya kutosha kwa Nadharia yetu.
1. Kujenga/Kuongeza: Utekelezaji, sasa, tunaanza kupima kwa seti kubwa za data kutumia mbinu, kama Fine-tuning na RAG, kuangalia uimara wa suluhisho letu. Ikiwa haitafanya kazi, kutekeleza tena, kuongeza hatua mpya katika mtiririko wetu au kuunda upya data, kunaweza kusaidia. Baada ya kujaribu mtiririko wetu na kiwango chetu, ikiwa inafanya kazi na kuangalia Vipimo vyetu, iko tayari kwa hatua inayofuata.
1. Kuendesha: Muunganiko, sasa kuongeza Mfumo wa Ufuatiliaji na Mitoaji ya Tahadhari kwenye mfumo wetu, upeleka na muunganiko wa programu kwenye Programu yetu.

Kisha, tuna mzunguko mkubwa wa Usimamizi, ukizingatia usalama, ufuataji na utawala.

Hongera, sasa una Programu yako ya AI tayari kuanza na kuendesha. Kwa uzoefu wa vitendo, angalia [Demo ya Mazungumzo ya Contoso.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

Sasa, ni zana gani tunaweza kutumia?

## Zana za Mzunguko wa Maisha

Kwa zana, Microsoft hutoa [Jukwaa la AI la Azure](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) na [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) hufanya mzunguko wako uwe rahisi kutekeleza na tayari kuanza.

[Jukwaa la AI la Azure](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys), linakuwezesha kutumia [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys). AI Studio ni lango la wavuti linalokuwezesha Kuchunguza mifano, sampuli na zana. Kusimamia rasilimali zako, mtiririko wa maendeleo ya UI na chaguzi za SDK/CLI kwa maendeleo ya Kwanza-Kodi.

![Muwezekano wa Azure AI](../../../translated_images/sw/04-azure-ai-platform.80203baf03a12fa8.png)

Azure AI, inakuwezesha kutumia rasilimali nyingi, kusimamia shughuli zako, huduma, miradi, utafutaji wa vector na mahitaji ya hifadhidata.

![LLMOps na Azure AI](../../../translated_images/sw/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.png)

Jenga, kutoka kwa Proof-of-Concept(POC) hadi programu za kiwango kikubwa na PromptFlow:

- Tengeneza na Jenga programu kutoka VS Code, kwa zana za kuona na za kazi
- Jaribu na boresha programu zako kwa AI bora, kwa urahisi.
- Tumia Azure AI Studio kuunganisha na kurudia na wingu, Sogeza na Peleka kwa muunganiko wa haraka.

![LLMOps na PromptFlow](../../../translated_images/sw/06-llm-promptflow.a183eba07a3a7fdf.png)

## Nzuri! Endelea Kujifunza!

Ajabu, sasa jifunze zaidi kuhusu jinsi tunavyopanga programu kutumia dhana na [Programu ya Mazungumzo ya Contoso](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), kuangalia jinsi Uhamasishaji wa Wingu unavyoongeza dhana hizo katika maonyesho. Kwa maudhui zaidi, angalia [Kikao cha kuvunja Ignite!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Sasa, angalia Somo la 15, kuelewa jinsi [Uzalishaji Ulioboreshwa kwa Urejeshaji na Hifadhidata za Vector](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) unavyoathiri AI Inayozalisha na kufanya Programu ziwe za kuvutia zaidi!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kiarifu cha Msamaha**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->