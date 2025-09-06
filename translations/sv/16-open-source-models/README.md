<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8b2d4bb727c877ebf9edff8623d16b9",
  "translation_date": "2025-09-06T10:18:51+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "sv"
}
-->
[![Open Source Models](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.sv.png)](https://aka.ms/gen-ai-lesson16-gh?WT.mc_id=academic-105485-koreyst)

## Introduktion

Världen av öppna LLM-modeller är spännande och ständigt i förändring. Den här lektionen syftar till att ge en djupgående inblick i öppna modeller. Om du letar efter information om hur proprietära modeller jämförs med öppna modeller, gå till lektionen ["Utforska och jämföra olika LLM-modeller"](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Den här lektionen kommer också att ta upp ämnet finjustering, men en mer detaljerad förklaring finns i lektionen ["Finjustering av LLM-modeller"](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Lärandemål

- Få en förståelse för öppna modeller
- Förstå fördelarna med att arbeta med öppna modeller
- Utforska de öppna modeller som finns tillgängliga på Hugging Face och Azure AI Studio

## Vad är öppna modeller?

Öppen källkod har spelat en avgörande roll i teknikens utveckling inom olika områden. Open Source Initiative (OSI) har definierat [10 kriterier för mjukvara](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) för att klassificeras som öppen källkod. Källkoden måste delas öppet under en licens som är godkänd av OSI.

Även om utvecklingen av LLM-modeller har likheter med mjukvaruutveckling, är processen inte exakt densamma. Detta har lett till mycket diskussion i samhället om definitionen av öppen källkod i LLM-sammanhang. För att en modell ska stämma överens med den traditionella definitionen av öppen källkod bör följande information vara offentligt tillgänglig:

- Dataset som används för att träna modellen.
- Fullständiga modellvikter som en del av träningen.
- Utvärderingskod.
- Kod för finjustering.
- Fullständiga modellvikter och träningsmetrik.

För närvarande finns det bara ett fåtal modeller som uppfyller dessa kriterier. [OLMo-modellen skapad av Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) är en som passar in i denna kategori.

I den här lektionen kommer vi att hänvisa till modellerna som "öppna modeller" framöver, eftersom de kanske inte uppfyller kriterierna ovan vid tidpunkten för skrivandet.

## Fördelar med öppna modeller

**Hög anpassningsbarhet** - Eftersom öppna modeller släpps med detaljerad träningsinformation kan forskare och utvecklare ändra modellens interna funktioner. Detta möjliggör skapandet av mycket specialiserade modeller som är finjusterade för en specifik uppgift eller studieområde. Några exempel på detta är kodgenerering, matematiska operationer och biologi.

**Kostnad** - Kostnaden per token för att använda och implementera dessa modeller är lägre än för proprietära modeller. När du bygger generativa AI-applikationer bör du jämföra prestanda och pris för dessa modeller baserat på ditt användningsområde.

![Model Cost](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.sv.png)  
Källa: Artificial Analysis

**Flexibilitet** - Att arbeta med öppna modeller ger flexibilitet när det gäller att använda olika modeller eller kombinera dem. Ett exempel på detta är [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst), där användaren kan välja vilken modell som används direkt i användargränssnittet:

![Choose Model](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.sv.png)

## Utforska olika öppna modeller

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), utvecklad av Meta, är en öppen modell som är optimerad för chattbaserade applikationer. Detta beror på dess finjusteringsmetod, som inkluderade en stor mängd dialog och mänsklig feedback. Med denna metod producerar modellen fler resultat som är i linje med mänskliga förväntningar, vilket ger en bättre användarupplevelse.

Några exempel på finjusterade versioner av Llama inkluderar [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), som specialiserar sig på japanska, och [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), som är en förbättrad version av basmodellen.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) är en öppen modell med starkt fokus på hög prestanda och effektivitet. Den använder Mixture-of-Experts-metoden, som kombinerar en grupp specialiserade expertmodeller i ett system där vissa modeller väljs ut baserat på input. Detta gör beräkningen mer effektiv eftersom modellerna endast hanterar de inputs de är specialiserade på.

Några exempel på finjusterade versioner av Mistral inkluderar [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), som fokuserar på det medicinska området, och [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), som utför matematiska beräkningar.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) är en LLM skapad av Technology Innovation Institute (**TII**). Falcon-40B tränades med 40 miljarder parametrar och har visat sig prestera bättre än GPT-3 med mindre beräkningsbudget. Detta beror på dess användning av FlashAttention-algoritmen och multiquery attention, vilket minskar minneskraven vid inferenstid. Med denna reducerade inferenstid är Falcon-40B lämplig för chattapplikationer.

Några exempel på finjusterade versioner av Falcon är [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), en assistent byggd på öppna modeller, och [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), som levererar högre prestanda än basmodellen.

## Hur man väljer

Det finns inget enkelt svar på vilken öppen modell man ska välja. Ett bra ställe att börja är att använda Azure AI Studios filterfunktion baserat på uppgifter. Detta hjälper dig att förstå vilka typer av uppgifter modellen har tränats för. Hugging Face upprätthåller också en LLM Leaderboard som visar de bäst presterande modellerna baserat på vissa metrik.

När du vill jämföra LLM-modeller över olika typer är [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) en annan bra resurs:

![Model Quality](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.sv.png)  
Källa: Artificial Analysis

Om du arbetar med ett specifikt användningsområde kan det vara effektivt att söka efter finjusterade versioner som fokuserar på samma område. Att experimentera med flera öppna modeller för att se hur de presterar enligt dina och dina användares förväntningar är också en bra praxis.

## Nästa steg

Det bästa med öppna modeller är att du kan börja arbeta med dem ganska snabbt. Kolla in [Azure AI Foundry Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), som innehåller en specifik Hugging Face-samling med de modeller vi diskuterade här.

## Lärandet slutar inte här, fortsätt resan

Efter att ha avslutat denna lektion, kolla in vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta utveckla din kunskap om generativ AI!

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen notera att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.