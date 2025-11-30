<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "807f0d9fc1747e796433534e1be6a98a",
  "translation_date": "2025-10-17T19:03:31+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "sv"
}
-->
[![Open Source Models](../../../translated_images/18-lesson-banner.f30176815b1a5074fce9cceba317720586caa99e24001231a92fd04eeb54a121.sv.png)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Finjustering av din LLM

Att använda stora språkmodeller för att bygga generativa AI-applikationer medför nya utmaningar. En viktig fråga är att säkerställa svarskvalitet (noggrannhet och relevans) i innehållet som genereras av modellen för en given användarförfrågan. I tidigare lektioner diskuterade vi tekniker som promptdesign och retrieval-augmented generation som försöker lösa problemet genom att _modifiera promptinmatningen_ till den befintliga modellen.

I dagens lektion diskuterar vi en tredje teknik, **finjustering**, som försöker hantera utmaningen genom att _träna om själva modellen_ med ytterligare data. Låt oss dyka in i detaljerna.

## Lärandemål

Denna lektion introducerar konceptet finjustering för förtränade språkmodeller, utforskar fördelarna och utmaningarna med detta tillvägagångssätt, och ger vägledning om när och hur man kan använda finjustering för att förbättra prestandan hos dina generativa AI-modeller.

I slutet av denna lektion bör du kunna svara på följande frågor:

- Vad är finjustering för språkmodeller?
- När och varför är finjustering användbart?
- Hur kan jag finjustera en förtränad modell?
- Vilka är begränsningarna med finjustering?

Redo? Låt oss börja.

## Illustrerad guide

Vill du få en överblick över vad vi kommer att täcka innan vi dyker in? Kolla in denna illustrerade guide som beskriver lärandets resa för denna lektion - från att lära sig kärnkoncepten och motivationen för finjustering, till att förstå processen och bästa praxis för att utföra finjusteringsuppgiften. Detta är ett fascinerande ämne att utforska, så glöm inte att kolla in [Resurser](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) för ytterligare länkar som stödjer din självstyrda läranderesa!

![Illustrerad guide till finjustering av språkmodeller](../../../translated_images/18-fine-tuning-sketchnote.11b21f9ec8a703467a120cb79a28b5ac1effc8d8d9d5b31bbbac6b8640432e14.sv.png)

## Vad är finjustering för språkmodeller?

Per definition är stora språkmodeller _förtränade_ på stora mängder text från olika källor, inklusive internet. Som vi har lärt oss i tidigare lektioner behöver vi tekniker som _promptdesign_ och _retrieval-augmented generation_ för att förbättra kvaliteten på modellens svar på användarens frågor ("prompter").

En populär teknik inom promptdesign innebär att ge modellen mer vägledning om vad som förväntas i svaret, antingen genom att ge _instruktioner_ (explicit vägledning) eller _ge den några exempel_ (implicit vägledning). Detta kallas _few-shot learning_, men det har två begränsningar:

- Modellens tokenbegränsningar kan begränsa antalet exempel du kan ge och minska effektiviteten.
- Modellens tokenkostnader kan göra det dyrt att lägga till exempel till varje prompt och begränsa flexibiliteten.

Finjustering är en vanlig praxis inom maskininlärningssystem där vi tar en förtränad modell och tränar om den med ny data för att förbättra dess prestanda för en specifik uppgift. När det gäller språkmodeller kan vi finjustera den förtränade modellen _med en noggrant utvald uppsättning exempel för en given uppgift eller applikationsdomän_ för att skapa en **anpassad modell** som kan vara mer exakt och relevant för just den uppgiften eller domänen. En sidoeffekt av finjustering är att det också kan minska antalet exempel som behövs för few-shot learning - vilket minskar tokenanvändning och relaterade kostnader.

## När och varför ska vi finjustera modeller?

I _detta_ sammanhang, när vi pratar om finjustering, hänvisar vi till **övervakad** finjustering där omträningen görs genom att **lägga till ny data** som inte var en del av den ursprungliga träningsdatamängden. Detta skiljer sig från en oövervakad finjusteringsmetod där modellen tränas om på den ursprungliga datan, men med olika hyperparametrar.

Det viktiga att komma ihåg är att finjustering är en avancerad teknik som kräver en viss nivå av expertis för att uppnå önskade resultat. Om det görs felaktigt kan det hända att det inte ger de förväntade förbättringarna och till och med försämrar modellens prestanda för din målgrupp.

Så innan du lär dig "hur" man finjusterar språkmodeller, behöver du veta "varför" du bör ta denna väg och "när" du ska börja processen med finjustering. Börja med att ställa dig själv dessa frågor:

- **Användningsfall**: Vad är ditt _användningsfall_ för finjustering? Vilken aspekt av den nuvarande förtränade modellen vill du förbättra?
- **Alternativ**: Har du provat _andra tekniker_ för att uppnå önskade resultat? Använd dem för att skapa en baslinje för jämförelse.
  - Promptdesign: Prova tekniker som few-shot prompting med exempel på relevanta promptresponser. Utvärdera svarens kvalitet.
  - Retrieval Augmented Generation: Prova att förstärka prompts med sökresultat från din data. Utvärdera svarens kvalitet.
- **Kostnader**: Har du identifierat kostnaderna för finjustering?
  - Anpassningsbarhet - är den förtränade modellen tillgänglig för finjustering?
  - Arbete - för att förbereda träningsdata, utvärdera och förbättra modellen.
  - Beräkningskraft - för att köra finjusteringsjobb och distribuera den finjusterade modellen.
  - Data - tillgång till tillräckligt många kvalitativa exempel för att påverka finjusteringen.
- **Fördelar**: Har du bekräftat fördelarna med finjustering?
  - Kvalitet - överträffade den finjusterade modellen baslinjen?
  - Kostnad - minskar det tokenanvändningen genom att förenkla prompts?
  - Utbyggbarhet - kan du återanvända basmodellen för nya domäner?

Genom att besvara dessa frågor bör du kunna avgöra om finjustering är rätt tillvägagångssätt för ditt användningsfall. Idealiskt sett är tillvägagångssättet giltigt endast om fördelarna överväger kostnaderna. När du har bestämt dig för att gå vidare är det dags att tänka på _hur_ du kan finjustera den förtränade modellen.

Vill du få fler insikter om beslutsprocessen? Titta på [Att finjustera eller inte finjustera](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Hur kan vi finjustera en förtränad modell?

För att finjustera en förtränad modell behöver du ha:

- en förtränad modell att finjustera
- en datamängd att använda för finjustering
- en träningsmiljö för att köra finjusteringsjobbet
- en hostingmiljö för att distribuera den finjusterade modellen

## Finjustering i praktiken

Följande resurser erbjuder steg-för-steg handledningar för att guida dig genom ett verkligt exempel med en utvald modell och en noggrant utvald datamängd. För att arbeta igenom dessa handledningar behöver du ett konto hos den specifika leverantören, tillsammans med tillgång till relevant modell och datamängder.

| Leverantör   | Handledning                                                                                                                                                                   | Beskrivning                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Hur man finjusterar chattmodeller](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)          | Lär dig att finjustera en `gpt-35-turbo` för en specifik domän ("receptassistent") genom att förbereda träningsdata, köra finjusteringsjobbet och använda den finjusterade modellen för inferens.                                                                                                                                                                                                                                   |
| Azure OpenAI | [GPT 3.5 Turbo finjusteringshandledning](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Lär dig att finjustera en `gpt-35-turbo-0613` modell **på Azure** genom att ta steg för att skapa och ladda upp träningsdata, köra finjusteringsjobbet. Distribuera och använd den nya modellen.                                                                                                                                                                                                                                   |
| Hugging Face | [Finjustering av LLMs med Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                           | Denna bloggpost guidar dig genom finjustering av en _öppen LLM_ (ex: `CodeLlama 7B`) med hjälp av [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) biblioteket & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst]) med öppna [datamängder](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) på Hugging Face. |
|              |                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Finjustering av LLMs med AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                     | AutoTrain (eller AutoTrain Advanced) är ett Python-bibliotek utvecklat av Hugging Face som möjliggör finjustering för många olika uppgifter inklusive finjustering av LLM. AutoTrain är en kodfri lösning och finjustering kan göras i din egen molnmiljö, på Hugging Face Spaces eller lokalt. Det stöder både ett webbaserat GUI, CLI och träning via yaml-konfigurationsfiler.                                                                 |

## Uppgift

Välj en av handledningarna ovan och gå igenom den. _Vi kan replikera en version av dessa handledningar i Jupyter Notebooks i detta repo endast som referens. Använd de ursprungliga källorna direkt för att få de senaste versionerna_.

## Bra jobbat! Fortsätt ditt lärande.

Efter att ha avslutat denna lektion, kolla in vår [Generative AI Learning-samling](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta utveckla din kunskap om generativ AI!

Grattis!! Du har avslutat den sista lektionen från v2-serien för denna kurs! Sluta inte lära dig och bygga. \*\*Kolla in [RESURSER](RESOURCES.md?WT.mc_id=academic-105485-koreyst) för en lista över ytterligare förslag för just detta ämne.

Vår v1-serie av lektioner har också uppdaterats med fler uppgifter och koncept. Så ta en minut för att fräscha upp din kunskap - och vänligen [dela dina frågor och feedback](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) för att hjälpa oss att förbättra dessa lektioner för gemenskapen.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.