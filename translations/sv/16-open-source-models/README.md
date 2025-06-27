<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0bba96e53ab841d99db731892a51fab8",
  "translation_date": "2025-06-25T23:57:42+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "sv"
}
-->
[![Open Source Models](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.sv.png)](https://aka.ms/gen-ai-lesson16-gh?WT.mc_id=academic-105485-koreyst)

## Introduktion

Världen av open source LLMs är spännande och ständigt utvecklande. Denna lektion syftar till att ge en djupgående inblick i open source-modeller. Om du letar efter information om hur proprietära modeller jämförs med open source-modeller, gå till lektionen ["Utforska och jämföra olika LLMs"](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Denna lektion kommer också att täcka ämnet finjustering, men en mer detaljerad förklaring kan hittas i lektionen ["Finjustera LLMs"](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Lärandemål

- Få en förståelse för open source-modeller
- Förstå fördelarna med att arbeta med open source-modeller
- Utforska de öppna modellerna som finns tillgängliga på Hugging Face och Azure AI Studio

## Vad är Open Source-modeller?

Open source-programvara har spelat en avgörande roll i teknologins utveckling över olika områden. Open Source Initiative (OSI) har definierat [10 kriterier för programvara](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) för att klassificeras som open source. Källkoden måste delas öppet under en licens godkänd av OSI.

Även om utvecklingen av LLMs har liknande element som att utveckla programvara, är processen inte exakt densamma. Detta har lett till mycket diskussion i gemenskapen om definitionen av open source i sammanhanget av LLMs. För att en modell ska vara i linje med den traditionella definitionen av open source bör följande information vara offentligt tillgänglig:

- Dataset som används för att träna modellen.
- Fulla modellvikter som en del av träningen.
- Utvärderingskoden.
- Finjusteringskoden.
- Fulla modellvikter och träningsmetrik.

Det finns för närvarande bara ett fåtal modeller som matchar dessa kriterier. [OLMo-modellen skapad av Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) är en som passar denna kategori.

För denna lektion kommer vi att hänvisa till modellerna som "öppna modeller" framöver eftersom de kanske inte matchar kriterierna ovan vid skrivandets tidpunkt.

## Fördelar med öppna modeller

**Hög anpassningsbarhet** - Eftersom öppna modeller släpps med detaljerad träningsinformation kan forskare och utvecklare modifiera modellens interna delar. Detta möjliggör skapandet av mycket specialiserade modeller som är finjusterade för en specifik uppgift eller studieområde. Några exempel på detta är kodgenerering, matematiska operationer och biologi.

**Kostnad** - Kostnaden per token för att använda och distribuera dessa modeller är lägre än för proprietära modeller. När man bygger Generativ AI-applikationer bör man se på prestanda kontra pris när man arbetar med dessa modeller för sitt användningsfall.

![Model Cost](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.sv.png)  
Källa: Artificial Analysis

**Flexibilitet** - Att arbeta med öppna modeller gör det möjligt att vara flexibel när det gäller att använda olika modeller eller kombinera dem. Ett exempel på detta är [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst) där en användare kan välja vilken modell som används direkt i användargränssnittet:

![Choose Model](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.sv.png)

## Utforska olika öppna modeller

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), utvecklad av Meta, är en öppen modell som är optimerad för chattbaserade applikationer. Detta beror på dess finjusteringsmetod, som inkluderade en stor mängd dialog och mänsklig feedback. Med denna metod producerar modellen fler resultat som är i linje med mänskliga förväntningar vilket ger en bättre användarupplevelse.

Några exempel på finjusterade versioner av Llama inkluderar [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), som specialiserar sig på japanska och [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), som är en förbättrad version av basmodellen.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) är en öppen modell med starkt fokus på hög prestanda och effektivitet. Den använder Mixture-of-Experts-metoden som kombinerar en grupp specialiserade expertmodeller till ett system där beroende på input, vissa modeller väljs att användas. Detta gör beräkningen mer effektiv eftersom modellerna endast hanterar de inputs de är specialiserade på.

Några exempel på finjusterade versioner av Mistral inkluderar [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), som är fokuserad på det medicinska området och [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), som utför matematiska beräkningar.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) är en LLM skapad av Technology Innovation Institute (**TII**). Falcon-40B tränades på 40 miljarder parametrar vilket har visat sig prestera bättre än GPT-3 med mindre beräkningsbudget. Detta beror på dess användning av FlashAttention-algoritmen och multiquery attention som gör det möjligt att minska minneskraven vid inferenstid. Med denna reducerade inferenstid är Falcon-40B lämplig för chattapplikationer.

Några exempel på finjusterade versioner av Falcon är [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), en assistent byggd på öppna modeller och [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), som levererar högre prestanda än basmodellen.

## Hur man väljer

Det finns inget enkelt svar för att välja en öppen modell. En bra startpunkt är att använda Azure AI Studios filter efter uppgift-funktion. Detta hjälper dig att förstå vilka typer av uppgifter modellen har tränats för. Hugging Face upprätthåller också en LLM Leaderboard som visar de bäst presterande modellerna baserat på vissa metrik.

När du vill jämföra LLMs över de olika typerna, [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) är en annan bra resurs:

![Model Quality](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.sv.png)  
Källa: Artificial Analysis

Om du arbetar med ett specifikt användningsfall kan det vara effektivt att söka efter finjusterade versioner som är fokuserade på samma område. Att experimentera med flera öppna modeller för att se hur de presterar enligt dina och dina användares förväntningar är en annan bra praxis.

## Nästa steg

Det bästa med öppna modeller är att du kan börja arbeta med dem ganska snabbt. Kolla in [Azure AI Studio Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), som har en specifik Hugging Face-samling med dessa modeller vi diskuterade här.

## Lärandet slutar inte här, fortsätt resan

Efter att ha avslutat denna lektion, kolla in vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta höja din kunskap inom Generativ AI!

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller misstolkningar som uppstår från användningen av denna översättning.