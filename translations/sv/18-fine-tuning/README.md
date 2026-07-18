[![Open Source Models](../../../translated_images/sv/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Finjustera din LLM

Att använda stora språkmodeller för att bygga generativa AI-applikationer medför nya utmaningar. En viktig fråga är att säkerställa svarskvalitet (noggrannhet och relevans) i innehållet som genereras av modellen för en given användarförfrågan. I tidigare lektioner har vi diskuterat tekniker som promptteknik och retrieval-augmented generation som försöker lösa problemet genom att _modifiera promptinmatningen_ till den befintliga modellen.

I dagens lektion diskuterar vi en tredje teknik, **finjustering**, som försöker ta itu med utmaningen genom att _träna om modellen själv_ med ytterligare data. Låt oss dyka in i detaljerna.

## Lärandemål

Den här lektionen introducerar begreppet finjustering för förtränade språkmodeller, utforskar fördelarna och utmaningarna med detta tillvägagångssätt och ger vägledning om när och hur man använder finjustering för att förbättra prestandan hos dina generativa AI-modeller.

I slutet av denna lektion bör du kunna svara på följande frågor:

- Vad är finjustering för språkmodeller?
- När, och varför, är finjustering användbart?
- Hur kan jag finjustera en förtränad modell?
- Vilka är begränsningarna med finjustering?

Redo? Låt oss börja.

## Illustrerad guide

Vill du få en överblick över vad vi kommer att täcka innan vi börjar? Kolla in denna illustrerade guide som beskriver läranderesan för denna lektion - från att lära sig kärnbegreppen och motivationen bakom finjustering till att förstå processen och bästa praxis för att utföra finjusteringsuppgiften. Detta är ett fascinerande ämne att utforska, så glöm inte att besöka [Resurser](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) sidan för ytterligare länkar som stödjer din självstyrda läranderesa!

![Illustrerad guide till finjustering av språkmodeller](../../../translated_images/sv/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Vad är finjustering för språkmodeller?

Per definition är stora språkmodeller _förtränade_ på stora mängder text från olika källor inklusive internet. Som vi har lärt oss i tidigare lektioner behöver vi tekniker som _promptteknik_ och _retrieval-augmented generation_ för att förbättra kvaliteten på modellens svar på användarens frågor ("prompter").

En populär promptteknik involverar att ge modellen mer vägledning om vad som förväntas i svaret antingen genom att tillhandahålla _instruktioner_ (explicit vägledning) eller _ge den några exempel_ (implicita anvisningar). Detta kallas för _few-shot learning_ men har två begränsningar:

- Modelltokensgränser kan begränsa antalet exempel du kan ge och minska effektiviteten.
- Kostnader för modelltokens kan göra det dyrt att lägga till exempel i varje prompt och minska flexibiliteten.

Finjustering är en vanlig praxis inom maskininlärningssystem där vi tar en förtränad modell och tränar om den med ny data för att förbättra dess prestanda på en specifik uppgift. I sammanhanget med språkmodeller kan vi finjustera den förtränade modellen _med en kurerad uppsättning exempel för en given uppgift eller applikationsdomän_ för att skapa en **anpassad modell** som kan vara mer exakt och relevant för just den uppgiften eller domänen. En bieffekt av finjustering är att det också kan minska antalet exempel som behövs för few-shot learning - vilket reducerar tokenanvändning och relaterade kostnader.

## När och varför ska vi finjustera modeller?

I _detta_ sammanhang, när vi pratar om finjustering, hänvisar vi till **övervakad** finjustering där omträningen görs genom att **lägga till ny data** som inte var en del av den ursprungliga träningsdatan. Detta skiljer sig från en oövervakad finjusteringsmetod där modellen tränas om på den ursprungliga datan but med olika hyperparametrar.

Det viktiga att komma ihåg är att finjustering är en avancerad teknik som kräver en viss nivå av expertis för att få önskade resultat. Om det görs felaktigt kan det misslyckas att ge de förväntade förbättringarna och kan till och med försämra modellens prestanda för det riktade området.

Så, innan du lär dig "hur" man finjusterar språkmodeller måste du veta "varför" du bör ta den här vägen och "när" du ska starta processen för finjustering. Börja med att ställa dig själv dessa frågor:

- **Användningsfall**: Vad är ditt _användningsfall_ för finjustering? Vilken aspekt av den nuvarande förtränade modellen vill du förbättra?
- **Alternativ**: Har du provat _andra tekniker_ för att uppnå önskade resultat? Använd dem för att skapa en referenspunkt för jämförelse.
  - Promptteknik: Prova tekniker som few-shot prompting med exempel på relevanta promptsvar. Utvärdera svarens kvalitet.
  - Retrieval Augmented Generation: Försök att förstärka prompts med sökresultat hämtade från din data. Utvärdera svarens kvalitet.
- **Kostnader**: Har du identifierat kostnaderna för finjustering?
  - Justerbarhet – är den förtränade modellen tillgänglig för finjustering?
  - Insats – för att förbereda träningsdata, utvärdera & förfina modellen.
  - Beräkning – för att köra finjusteringsjobb och distribuera den finjusterade modellen.
  - Data – tillgång till tillräckligt högkvalitativa exempel för att påverka finjusteringen.
- **Fördelar**: Har du bekräftat fördelarna med finjustering?
  - Kvalitet – presterade den finjusterade modellen bättre än referenspunkten?
  - Kostnad – minskar den tokenanvändningen genom att förenkla prompts?
  - Utbyggbarhet – kan du återanvända basmodellen för nya domäner?

Genom att svara på dessa frågor bör du kunna avgöra om finjustering är rätt tillvägagångssätt för ditt användningsfall. Idealt är tillvägagångssättet giltigt endast om fördelarna överväger kostnaderna. När du beslutat dig för att gå vidare är det dags att fundera på _hur_ du kan finjustera den förtränade modellen.

Vill du få mer insikter om beslutsprocessen? Titta på [Att finjustera eller inte finjustera](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Hur kan vi finjustera en förtränad modell?

För att finjustera en förtränad modell behöver du ha:

- en förtränad modell att finjustera
- en dataset att använda för finjustering
- en träningsmiljö för att köra finjusteringsjobbet
- en värd-miljö för att distribuera den finjusterade modellen

## Finjustering på Microsoft Foundry

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) är där du finjusterar, distribuerar och hanterar anpassade modeller på Azure idag (det samlar vad som tidigare var Azure OpenAI Studio och Azure AI Studio). Innan du startar ett jobb är det hjälpsamt att förstå de val som Foundry ger dig - och de bästa praxis som plattformen rekommenderar. Under huven använder Foundry **LoRA (low-rank adaptation)** för att effektivt finjustera modeller, vilket håller träningen snabbare och mer prisvärd än att träna om varje vikt.

### Steg 1: Välj en träningsmetod

Foundry stöder tre finjusteringstekniker. **Börja med SFT** - den täcker det största spektrumet av scenarier.

| Teknik | Vad den gör | När att använda den |
| --- | --- | --- |
| **Övervakad finjustering (SFT)** | Tränar på in-/ut-exempelpär för att modellen ska lära sig producera svaren du vill ha. | Standard för de flesta uppgifter: domänspecialisering, uppgiftsprestation, stil och ton, följa instruktioner och språkadaption. |
| **Direkt preferensoptimering (DPO)** | Lär sig från _föredragna vs. icke-föredragna_ svarspär för att anpassa utdata till mänskliga preferenser. | Förbättra svarskvalitet, säkerhet och anpassning när du har jämförande feedback. |
| **Förstärkt finjustering (RFT)** | Använder belöningssignaler från _bedömare_ för att optimera komplexa beteenden med förstärkningsinlärning. | Objektiva, resonemangsintensiva domäner (matematik, kemi, fysik) med tydliga rätt/fel-svar. Kräver mer ML-expertis. |

### Steg 2: Välj en träningstjänst

Foundry låter dig välja hur och var träningen körs:

- **Standard** - tränar i din resurs region och garanterar datalagring inom regionen. Använd den när data måste stanna i en specifik region.
- **Global** - billigare och snabbare kötid genom att använda kapacitet utanför din region (data och vikter kopieras till träningsregionen). Ett bra standardval när datalagring inom region inte är ett krav.
- **Utvecklare** - lägsta kostnad, använder inaktiv kapacitet utan latens/SLA-garantier (jobb kan avbrytas och återupptas). Perfekt för experiment.

### Steg 3: Välj en basmodell

Finjusterbara modeller inkluderar OpenAI `gpt-4o-mini`, `gpt-4o`, `gpt-4.1`, `gpt-4.1-mini` och `gpt-4.1-nano` (SFT; 4o/4.1-familjen stöder även DPO), resonemangsmodellerna `o4-mini` och `gpt-5` (RFT), plus öppen källkod-modeller som `Ministral-3B`, `Qwen-32B`, `Llama-3.3-70B-Instruct` och `gpt-oss-20b` (SFT på Foundry-resurser). Kontrollera alltid den aktuella [listan över finjusteringsmodeller](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) för stödda metoder, regioner och tillgänglighet.

> Foundry erbjuder två modaliteter: **serverlös** (förbrukningsbaserad prissättning, ingen GPU-kvot att hantera, OpenAI och utvalda modeller) och **hanterad beräkning** (ta med egna VM:er via Azure Machine Learning för det bredaste modellutbudet). De flesta bör börja med serverlös.

### Foundrys bästa praxis

- **Baslinje först.** Mät basmodellen med promptteknik och RAG _innan_ du finjusterar, så att du kan bevisa förbättringen.
- **Börja smått, skala sedan.** Börja med 50–100 högkvalitativa exempel för att validera tillvägagångssättet, och väx sedan till 500+ för produktion. Kvalitet är viktigare än kvantitet – gallra bort lågkvalitativa exempel.
- **Formatera data korrekt.** Tränings- och valideringsfiler måste vara JSONL, UTF-8 **med BOM**, under 512 MB, med chatt-kompletteringsmeddelande format. Inkludera alltid en valideringsfil så du kan bevaka överanpassning.
- **Behåll systemprompten från träningen vid inferens.** Använd samma systemmeddelande när du anropar modellen som du använde under träningen.
- **Utvärdera kontrollpunkter – distribuera inte blint den sista.** Foundry behåller de tre sista epokerna som deploybara kontrollpunkter; välj den som generaliserar bäst genom att följa `train_loss` / `valid_loss` och token-noggrannhet.
- **Mät tokenkostnad parallellt med kvalitet** när du jämför den finjusterade modellen med baslinjen.
- **Iterera med kontinuerlig finjustering.** Du kan finjustera en redan finjusterad modell på ny data (stöds för OpenAI-modeller).
- **Tänk på värdkostnader.** En distribuerad anpassad modell debiteras per timme, och en inaktiv distribution tas bort efter 15 dagar – rensa bort det du inte behöver.

Följ igenom den steg-för-steg-genomgången i [Anpassa en modell med finjustering](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) och se guiderna för [DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst) och [RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst) när du är redo för de andra teknikerna.

## Finjustering i praktiken

Följande resurser erbjuder steg-för-steg-handledning som går igenom ett verkligt exempel på en för närvarande understödd modell med en kurerad dataset. För att arbeta med dem behöver du ett konto hos den specifika leverantören samt tillgång till den relevanta modellen och datamängderna.

| Leverantör  | Handledning                                                                                                                                                                 | Beskrivning                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Hur man finjusterar chattmodeller](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)    | Lär dig finjustera en nyare OpenAI chattmodell för en specifik domän ("receptassistent") genom att förbereda träningsdata, köra finjusteringsjobbet och använda den finjusterade modellen för inferens.                                                                                                                                                                                                                              |
| Microsoft Foundry | [Anpassa en modell med finjustering](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst)                     | Lär dig finjustera en för närvarande understödd modell som `gpt-4.1-mini` **på Azure** med Microsoft Foundry: förbered & ladda upp tränings- och valideringsdata, kör finjusteringsjobbet, sedan distribuera & använd den nya modellen.                                                                                                                                                                                           |

| Hugging Face | [Finjustera LLM:er med Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Denna bloggpost guidar dig i att finjustera en _öppen LLM_ (ex: `CodeLlama 7B`) med hjälp av [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst)-biblioteket & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) med öppna [datamängder](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) på Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Finjustera LLM:er med AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (eller AutoTrain Advanced) är ett python-bibliotek utvecklat av Hugging Face som möjliggör finjustering för många olika uppgifter inklusive LLM-finjustering. AutoTrain är en kodfri lösning och finjustering kan göras i din egen molnmiljö, på Hugging Face Spaces eller lokalt. Det stödjer både en webbaserad GUI, CLI samt träning via yaml-konfigurationsfiler.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Finjustera LLM:er med Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth är ett open-source ramverk som stödjer LLM-finjustering och förstärkningsinlärning (RL). Unsloth underlättar lokal träning, utvärdering och distribution med färdiga [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Det stödjer även text-till-tal (TTS), BERT och multimodala modeller. För att komma igång, läs deras steg-för-steg [Guide för finjustering av LLMs](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Uppgift

Välj en av handledningarna ovan och följ den. _Vi kan komma att replikera en version av dessa handledningar i Jupyter Notebooks i detta repo som referens endast. Vänligen använd de ursprungliga källorna direkt för att få de senaste versionerna_.

## Bra jobbat! Fortsätt ditt lärande.

Efter att ha slutfört denna lektion, kolla in vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta utveckla din kunskap om Generative AI!

Grattis!! Du har slutfört den sista lektionen från v2-serien för denna kurs! Sluta inte lära och bygga. \*\*Kolla in [RESURSER](RESOURCES.md?WT.mc_id=academic-105485-koreyst)-sidan för en lista med ytterligare förslag för just detta ämne.

Vår v1-serie av lektioner har också uppdaterats med fler uppgifter och koncept. Så ta en minut för att fräscha upp dina kunskaper – och vänligen [dela dina frågor och feedback](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) för att hjälpa oss förbättra dessa lektioner för communityn.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->