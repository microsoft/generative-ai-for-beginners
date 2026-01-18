<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3772dcd23a98e2010f53ce8b9c583631",
  "translation_date": "2026-01-18T18:02:12+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "sv"
}
-->
[![Open Source Models](../../../../../translated_images/sv/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Finjustera din LLM

Att använda stora språkmodeller för att bygga generativa AI-applikationer innebär nya utmaningar. En nyckelfråga är att säkerställa svarskvalitet (noggrannhet och relevans) i innehåll som genereras av modellen för en given användarförfrågan. I tidigare lektioner har vi diskuterat tekniker som prompt-engineering och retrieval-augmented generation som försöker lösa problemet genom att _modifiera prompt-inmatningen_ till den befintliga modellen.

I dagens lektion diskuterar vi en tredje teknik, **finjustering**, som försöker ta itu med utmaningen genom att _omträna själva modellen_ med ytterligare data. Låt oss gå in på detaljerna.

## Lärandemål

Denna lektion introducerar begreppet finjustering för förtränade språkmodeller, utforskar fördelar och utmaningar med detta tillvägagångssätt och ger vägledning om när och hur man använder finjustering för att förbättra prestandan hos dina generativa AI-modeller.

I slutet av denna lektion bör du kunna svara på följande frågor:

- Vad är finjustering för språkmodeller?
- När och varför är finjustering användbart?
- Hur kan jag finjustera en förtränad modell?
- Vilka är begränsningarna med finjustering?

Redo? Låt oss sätta igång.

## Illustrerad guide

Vill du få en övergripande bild av vad vi ska täcka innan vi dyker in? Titta på denna illustrerade guide som beskriver läranderesan för denna lektion – från att lära sig kärnbegrepp och motivation för finjustering till att förstå processen och bästa praxis för att utföra finjusteringsuppgiften. Detta är ett fascinerande ämne att utforska, så glöm inte att kolla in sidan [Resurser](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) för ytterligare länkar som stödjer din självstyrda inlärningsresa!

![Illustrated Guide to Fine Tuning Language Models](../../../../../translated_images/sv/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Vad är finjustering för språkmodeller?

Enligt definition är stora språkmodeller _förtränade_ på stora mängder text hämtad från olika källor inklusive internet. Som vi lärt oss i tidigare lektioner behöver vi tekniker som _prompt-engineering_ och _retrieval-augmented generation_ för att förbättra kvaliteten på modellens svar på användarens frågor ("prompts").

En populär prompt-engineering teknik innebär att ge modellen mer vägledning om vad som förväntas i svaret, antingen genom att ge _instruktioner_ (explicit vägledning) eller _ge den några exempel_ (implicit vägledning). Detta kallas _few-shot learning_ men har två begränsningar:

- Modellens tokenbegränsningar kan begränsa antalet exempel du kan ge och därmed effektiviteten.
- Kostnaden för modellens tokens kan göra det dyrt att lägga till exempel till varje prompt och begränsa flexibiliteten.

Finjustering är en vanlig praxis inom maskininlärningssystem där vi tar en förtränad modell och tränar om den med ny data för att förbättra dess prestanda på en specifik uppgift. I kontexten av språkmodeller kan vi finjustera den förtränade modellen _med en kuraterad uppsättning exempel för en given uppgift eller applikationsdomän_ för att skapa en **anpassad modell** som kan vara mer exakt och relevant för just den uppgiften eller domänen. En ytterligare fördel med finjustering är att det också kan minska antalet exempel som behövs för few-shot learning – vilket minskar tokenanvändning och relaterade kostnader.

## När och varför bör vi finjustera modeller?

I _detta_ sammanhang, när vi pratar om finjustering, avser vi **övervakad** finjustering där omträningen görs genom att **lägga till ny data** som inte var del av den ursprungliga träningsdatamängden. Detta skiljer sig från en oövervakad finjustering där modellen tränas om på ursprungsdata, men med olika hyperparametrar.

Det viktigaste att komma ihåg är att finjustering är en avancerad teknik som kräver en viss nivå av expertis för att uppnå önskade resultat. Om det görs felaktigt kan det kanske inte ge de förväntade förbättringarna och kan till och med försämra modellens prestanda för din målade domän.

Så innan du lär dig "hur" du finjusterar språkmodeller, behöver du veta "varför" du ska ta denna väg och "när" du ska börja finjusteringsprocessen. Börja med att ställa dig själv dessa frågor:

- **Användningsfall**: Vad är ditt _användningsfall_ för finjustering? Vilken aspekt av den nuvarande förtränade modellen vill du förbättra?
- **Alternativ**: Har du provat _andra tekniker_ för att uppnå önskade resultat? Använd dem för att skapa en baslinje för jämförelse.
  - Prompt-engineering: Testa tekniker som few-shot prompting med exempel på relevanta prompt-svar. Utvärdera svarens kvalitet.
  - Retrieval Augmented Generation: Försök att förstärka prompts med sökresultat från dina data. Utvärdera svarens kvalitet.
- **Kostnader**: Har du identifierat kostnaderna för finjustering?
  - Tunbarhet – är den förtränade modellen tillgänglig för finjustering?
  - Insats – för att förbereda träningsdata, utvärdera och förfina modellen.
  - Beräkning – för att köra finjusteringsjobb och distribuera den finjusterade modellen.
  - Data – tillgång till kvalitativa exempel i tillräcklig omfattning för finjusteringspåverkan.
- **Fördelar**: Har du bekräftat fördelarna med finjustering?
  - Kvalitet – presterade den finjusterade modellen bättre än baslinjen?
  - Kostnad – minskar det tokenanvändningen genom att förenkla prompts?
  - Utbyggbarhet – kan du återanvända basmodellen för nya domäner?

Genom att svara på dessa frågor bör du kunna avgöra om finjustering är rätt tillvägagångssätt för ditt användningsfall. Idealiskt är tillvägagångssättet giltigt endast om fördelarna överväger kostnaderna. När du bestämt dig för att gå vidare är det dags att tänka på _hur_ du kan finjustera den förtränade modellen.

Vill du ha fler insikter om beslutsprocessen? Titta på [To fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Hur kan vi finjustera en förtränad modell?

För att finjustera en förtränad modell behöver du:

- en förtränad modell att finjustera
- en dataset att använda för finjusteringen
- en träningsmiljö för att köra finjusteringsjobbet
- en hosting-miljö för att distribuera den finjusterade modellen

## Finjustering i praktiken

Följande resurser erbjuder steg-för-steg tutorials som guidar dig genom ett verkligt exempel med en utvald modell och kuraterad dataset. För att arbeta med dessa tutorials behöver du ett konto hos respektive leverantör samt tillgång till relevanta modeller och datasets.

| Leverantör  | Tutorial                                                                                                                                                                         | Beskrivning                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI      | [Hur man finjusterar chattmodeller](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)             | Lär dig att finjustera en `gpt-35-turbo` för en specifik domän ("receptassistent") genom att förbereda träningsdata, köra finjusteringsjobbet och använda den finjusterade modellen för inferens.                                                                                                                                                                                                                               |
| Azure OpenAI| [GPT 3.5 Turbo finjusteringsguide](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst)      | Lär dig att finjustera en `gpt-35-turbo-0613` modell **på Azure** genom att utföra steg för att skapa och ladda upp träningsdata, köra finjusteringsjobbet. Distribuera och använd den nya modellen.                                                                                                                                                                                                                               |
| Hugging Face| [Finjustera LLMs med Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                                 | Denna bloggpost visar hur du finjusterar en _öppen LLM_ (exempel: `CodeLlama 7B`) med hjälp av [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) biblioteket & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) med öppna [datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) på Hugging Face. |
|             |                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 🤗 AutoTrain| [Finjustera LLMs med AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                             | AutoTrain (eller AutoTrain Advanced) är ett python-bibliotek utvecklat av Hugging Face som tillåter finjustering för många olika uppgifter inklusive LLM finjustering. AutoTrain är en lösning utan kod och finjustering kan göras i din egen moln, på Hugging Face Spaces eller lokalt. Den stöder både webbaserat GUI, CLI och träning via yaml-konfigurationsfiler.                                                                                          |
|             |                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 🦥 Unsloth  | [Finjustera LLMs med Unsloth](https://github.com/unslothai/unsloth)                                                                                                             | Unsloth är ett open-source-ramverk som stödjer finjustering av LLM och förstärkningsinlärning (RL). Unsloth förenklar lokal träning, utvärdering och distribution med färdiga [notebooks](https://github.com/unslothai/notebooks). Det stöder även text-till-tal (TTS), BERT och multimodala modeller. För att komma igång, läs deras steg-för-steg [Finjusteringsguide för LLMs](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                   |
|             |                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
## Uppgift

Välj en av tutorials ovan och gå igenom den. _Vi kan komma att återskapa en version av dessa tutorials i Jupyter Notebooks i detta repo för referens endast. Vänligen använd originalkällorna direkt för att få de senaste versionerna_.

## Bra jobbat! Fortsätt din inlärning.

Efter att ha slutfört denna lektion, kika på vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta utveckla din kunskap om generativ AI!

Grattis!! Du har slutfört den sista lektionen i v2-serien för denna kurs! Sluta inte lära och bygga. \*\*Kolla in sidan [RESURSER](RESOURCES.md?WT.mc_id=academic-105485-koreyst) för en lista på ytterligare förslag för just detta ämne.

Vår v1-serie av lektioner har också uppdaterats med fler uppgifter och koncept. Så ta en minut för att fräscha upp din kunskap – och vänligen [dela dina frågor och feedback](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) för att hjälpa oss förbättra dessa lektioner för communityn.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Trots att vi strävar efter noggrannhet kan automatiska översättningar innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål ska anses vara den auktoritativa källan. För viktig information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->