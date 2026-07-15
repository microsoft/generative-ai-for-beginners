[![Open Source Models](../../../translated_images/sv/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Finjustera din LLM

Att använda stora språkmodeller för att bygga generativa AI-applikationer innebär nya utmaningar. En nyckelfråga är att säkerställa svarskvalitet (noggrannhet och relevans) i innehåll som genereras av modellen för en given användarförfrågan. I tidigare lektioner har vi diskuterat tekniker som prompt-engineering och retrieval-augmented generation som försöker lösa problemet genom att _modifiera promptens indata_ till den befintliga modellen.

I dagens lektion diskuterar vi en tredje teknik, **finjustering**, som försöker ta itu med utmaningen genom att _träna om själva modellen_ med ytterligare data. Låt oss gå in på detaljerna.

## Lärandemål

Den här lektionen introducerar konceptet finjustering för förtränade språkmodeller, utforskar fördelar och utmaningar med detta tillvägagångssätt och ger vägledning om när och hur du kan använda finjustering för att förbättra prestandan hos dina generativa AI-modeller.

I slutet av denna lektion bör du kunna svara på följande frågor:

- Vad är finjustering för språkmodeller?
- När och varför är finjustering användbart?
- Hur kan jag finjustera en förtränad modell?
- Vilka är begränsningarna med finjustering?

Redo? Låt oss börja.

## Illustrerad guide

Vill du få en överblick över vad vi kommer att behandla innan vi går in på detaljer? Kolla in denna illustrerade guide som beskriver läranderesan för denna lektion – från att lära sig kärnkoncepten och motivationen bakom finjustering, till att förstå processen och bästa praxis för att utföra finjusteringsuppgiften. Detta är ett fascinerande ämne för utforskning, så glöm inte att kolla in sidan [Resurser](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) för ytterligare länkar som stödjer din självstyrda läranderesa!

![Illustrerad guide till finjustering av språkmodeller](../../../translated_images/sv/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Vad är finjustering för språkmodeller?

Per definition är stora språkmodeller _förtränade_ på stora mängder text från olika källor, inklusive internet. Som vi lärt oss i tidigare lektioner behöver vi tekniker som _prompt-engineering_ och _retrieval-augmented generation_ för att förbättra kvaliteten på modellens svar på användarens frågor ("prompter").

En populär teknik inom prompt-engineering innebär att ge modellen mer vägledning om vad som förväntas i svaret antingen genom att tillhandahålla _instruktioner_ (explicit vägledning) eller _ge den några exempel_ (implicit vägledning). Detta kallas _few-shot-learning_ men har två begränsningar:

- Modellens tokenbegränsningar kan begränsa antalet exempel du kan ge och minska effektiviteten.
- Kostnader för modellens tokens kan göra det dyrt att lägga till exempel till varje prompt och begränsa flexibiliteten.

Finjustering är en vanlig praxis inom maskininlärningssystem där vi tar en förtränad modell och tränar om den med ny data för att förbättra dess prestanda på en specifik uppgift. I sammanhanget för språkmodeller kan vi finjustera den förtränade modellen _med en noggrant utvald uppsättning exempel för en given uppgift eller applikationsdomän_ för att skapa en **anpassad modell** som kan vara mer noggrann och relevant för just denna specifika uppgift eller domän. En sidoeffekt av finjustering är att det också kan minska antalet exempel som behövs för few-shot-learning – vilket minskar tokenanvändningen och relaterade kostnader.

## När och varför ska vi finjustera modeller?

I _detta_ sammanhang, när vi pratar om finjustering, syftar vi på **övervakad** finjustering där omskolning utförs genom att **lägga till ny data** som inte var en del av den ursprungliga träningsdatan. Detta skiljer sig från en oövervakad finjusteringsmetod där modellen tränas om på den ursprungliga datan men med andra hyperparametrar.

Det viktigaste att komma ihåg är att finjustering är en avancerad teknik som kräver en viss nivå av expertis för att uppnå önskade resultat. Om det görs felaktigt kan det kanske inte ge de förväntade förbättringarna och kan till och med försämra modellens prestanda för din riktade domän.

Så, innan du lär dig "hur" du finjusterar språkmodeller måste du veta "varför" du ska ta denna väg och "när" du bör börja processen med finjustering. Börja med att ställa dig själv dessa frågor:

- **Användningsfall**: Vad är ditt _användningsfall_ för finjustering? Vilken aspekt av den nuvarande förtränade modellen vill du förbättra?
- **Alternativ**: Har du försökt med _andra tekniker_ för att uppnå de önskade resultaten? Använd dem för att skapa en baslinje för jämförelse.
  - Prompt engineering: Prova tekniker som few-shot prompting med exempel på relevanta promptsvar. Utvärdera svarens kvalitet.
  - Retrieval Augmented Generation: Prova att förstärka prompter med sökresultat från dina data. Utvärdera svarens kvalitet.
- **Kostnader**: Har du identifierat kostnaderna för finjustering?
  - Justerbarhet – är den förtränade modellen tillgänglig för finjustering?
  - Insats – för att förbereda träningsdata, utvärdera och förfina modellen.
  - Beräkning – för att köra finjusteringsjobb och distribuera finjusterad modell.
  - Data – tillgång till tillräckligt kvalitativa exempel för finjusteringspåverkan.
- **Fördelar**: Har du bekräftat fördelarna med finjustering?
  - Kvalitet – överträffade den finjusterade modellen baslinjen?
  - Kostnad – minskar den tokenanvändningen genom att förenkla prompts?
  - Utbyggbarhet – kan du återanvända basmodellen för nya domäner?

Genom att svara på dessa frågor bör du kunna avgöra om finjustering är rätt tillvägagångssätt för ditt användningsfall. Idealisk är metoden endast giltig om fördelarna överväger kostnaderna. När du bestämt dig för att fortsätta är det dags att tänka på _hur_ du kan finjustera den förtränade modellen.

Vill du få fler insikter om beslutsprocessen? Titta på [To fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Hur kan vi finjustera en förtränad modell?

För att finjustera en förtränad modell behöver du:

- en förtränad modell att finjustera
- en dataset att använda för finjustering
- en träningsmiljö för att köra finjusteringsjobbet
- en hostingmiljö för att distribuera finjusterad modell

## Finjustering i praktiken

> **Obs:** `gpt-35-turbo` / `gpt-3.5-turbo`, som refereras i vissa av handledningarna nedan, är pensionerade för både inferens och finjustering. Om du startar ett nytt finjusteringsjobb idag, sikta istället på en för närvarande stödjad modell – till exempel `gpt-4o-mini` eller `gpt-4.1-mini`. Se [Fine-tuning models list](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) för den aktuella uppsättningen av modeller som kan finjusteras. Koncepten och stegen i dessa handledningar gäller fortfarande.

Följande resurser erbjuder steg-för-steg-handlettningar för att guida dig genom ett verkligt exempel med en vald modell och en noggrant utvald dataset. För att arbeta igenom dessa handledningar behöver du ett konto hos den specifika leverantören samt tillgång till den relevanta modellen och datamaterialet.

| Leverantör  | Handledning                                                                                                                                                                            | Beskrivning                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Hur man finjusterar chattmodeller](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Lär dig att finjustera en `gpt-35-turbo` för ett specifikt domänområde ("receptassistent") genom att förbereda träningsdata, köra finjusteringsjobbet och använda den finjusterade modellen för inferens.                                                                                                                                                                                                                       |
| Azure OpenAI | [GPT 3.5 Turbo finjusteringshandledning](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst) | Lär dig att finjustera en `gpt-35-turbo-0613` modell **på Azure** genom att ta steg för att skapa och ladda upp träningsdata, köra finjusteringsjobbet. Distribuera och använd den nya modellen.                                                                                                                                                                                                                                |
| Hugging Face | [Finjustera LLMs med Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Denna bloggpost går igenom finjustering av en _öppen LLM_ (ex: `CodeLlama 7B`) med hjälp av [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) biblioteket och [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) med öppna [datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) på Hugging Face.      |
|              |                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 🤗 AutoTrain | [Finjustera LLMs med AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (eller AutoTrain Advanced) är ett Python-bibliotek utvecklat av Hugging Face som möjliggör finjustering för många olika uppgifter inklusive finjustering av LLMs. AutoTrain är en no-code-lösning och finjustering kan göras i din egen molnmiljö, på Hugging Face Spaces eller lokalt. Det stöder både ett webb-baserat GUI, CLI och träning via yaml-konfigurationsfiler.                                                             |
|              |                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 🦥 Unsloth | [Finjustera LLMs med Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth är ett open source-ramverk som stöder finjustering av LLM och förstärkningsinlärning (RL). Unsloth förenklar lokal träning, utvärdering och distribution med färdiga [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Det stöder även text-till-tal (TTS), BERT och multimodala modeller. För att komma igång, läs deras steg-för-steg [Guide för finjustering av LLM](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).  |
|              |                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                              |
## Uppgift

Välj en av ovanstående handledningar och gå igenom den. _Vi kan replikera en version av dessa handledningar i Jupyter Notebooks i denna repo enbart som referens. Använd gärna de ursprungliga källorna direkt för att få de senaste versionerna_.

## Utmärkt jobb! Fortsätt ditt lärande.

Efter att du slutfört denna lektion, kolla in vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta utveckla dina kunskaper inom Generativ AI!

Grattis!! Du har slutfört den sista lektionen i v2-serien för denna kurs! Sluta inte lära och bygga. \*\*Kolla in sidan [RESURSER](RESOURCES.md?WT.mc_id=academic-105485-koreyst) för en lista med ytterligare förslag just för detta ämne.

Vår v1-serie av lektioner har också uppdaterats med fler uppgifter och koncept. Så ta en minut att fräscha upp din kunskap – och vänligen [dela dina frågor och feedback](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) för att hjälpa oss förbättra dessa lektioner för gemenskapen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->