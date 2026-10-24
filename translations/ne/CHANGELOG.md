# परिवर्तन विवरण

सबै उल्लेखनीय परिवर्तनहरू जनरेटिभ एआई फर बिगिनर्स पाठ्यक्रममा यस फाइलमा दस्तावेज गरिएको छ।

ढाँचा [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) मा आधारित छ। किनकि यो संस्करण गरिएको सफ्टवेयर प्याकेज होइन, यसैले प्रविष्टिहरू मिति अनुसार समूहीकृत छन्।


## [2026-07-16] — सामग्री प्रमाणीकरण + पाठ 09 छवि सम्पत्ति

### परिवर्तन गरिएको

- **पाठ १० (कम-कोड AI एपहरू):** दुई अवकाशप्राप्त `docs.microsoft.com/powerapps/...` Dataverse लिंकहरू अद्यावधिक गरियो
  हालको `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro` तर्फ
  (सजीव प्रमाणित)।  
- **पाठ १७ (AI एजेन्टहरू):** पुरानो मोडेल उदाहरण आधुनिक बनायो (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, and Llama 3.3`) र एजेन्ट फ्रेमवर्क नमुना मा प्लेसहोल्डर डिप्लोयमेन्ट नाम 
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`)।
- **रुट `README.md`:** *Microsoft for Startups* लिंकमा हराएको `?WT.mc_id=academic-105485-koreyst` ट्र्याकिङ आईडी थपियो।
  
- **पाठ ०९ छवि सम्पत्ति** `gpt-image` मोडेलसहित पुनः सिर्जना गरियो: `images/generated-image.png`,  
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, र   
  `images/startup.png` (सम्पादन उदाहरणको पहिले/पछिको जोडी वास्तविक   
  `client.images.edit` कल मार्फत मास्क सिर्जना गरेर उत्पादन गरियो)।  

### मान्य गरियो  

- पाठ ०१, ०३, ०५, १२, १४, र १६ का READMEs अडिट गरियो — सबै वर्तमान (सही Microsoft Foundry  
  नाम र लिंकहरू); कुनै परिवर्तन आवश्यक थिएन।  
- ४१ इन्गित रि-पोजिटरी मार्कडाउन फाइलहरूमा पूर्ण मार्कडाउन मान्यकरण गरियो (अनुवादहरू बाहेक)  
  अव्यवस्थित डक पथहरू, `/en-us/` Microsoft स्थानीयहरु, पुराना उत्पादन/मोडेल नामहरू, हराएका ट्र्याकिङ  
  आईडीहरू, र टुटेका सापेक्ष लिंक/छविहरूको लागि। केवल एकल *Microsoft for Startups* ट्र्याकिङ-आईडीको   
  अन्तराल कार्यान्वयनयोग्य थियो; बाँकी सबै झण्डाहरू गलत सकारात्मक पुष्टि गरियो (आटो-निर्मित अनुवाद लिंकहरू,  
  टिप्पणी गरिएको प्लेसहोल्डरहरू, र तेस्रो पक्ष `/en/` संरचनागत URLहरू)।  

## [२०२६-०७-१५] — पाठ ०९ (छवि अनुप्रयोगहरू) GPT छवि मोडेलहरूको लागि पुनर्लेखन  

### परिवर्तन गरियो  

- **पाठ 09 "तस्बिर निर्माण कार्यान्वयनहरू" लाई पुनःलेखन गरियो** वर्तमान **`gpt-image`**
  मोडेल परिवार वरिपरि (पूर्वनिर्धारित **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` पनि GA), पुरानो
  DALL·E 2/3 सामग्रीलाई प्रतिस्थापन गर्दै। प्रमुख सुधारहरू:
  - `gpt-image` मोडेलहरू तस्बिरलाई **base64 (`b64_json`)** को रूपमा फर्काउँछन्, URL होइन। सबै नमूनाहरूलाई
    `base64.b64decode(...)` मा अपडेट गरियो, डाउनलोड गरेर `url` सट्टा जुन `requests` प्रयोग गर्थे।
  - तस्बिर API संस्करण `2025-04-01-preview` मा बढाइयो।
  - बनावट गरिएको "तापक्रम" खण्ड (तस्बिर मोडेलहरूले `temperature` लिन्दैनन्) र
    DALL·E-2-विशिष्ट तस्बिर **परिवर्तनहरू** सामग्रीलाई **तस्बिर सम्पादन** (मास्क/इनपेन्टिङ) खण्डले प्रतिस्थापन गरियो।
  - `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py` अपडेट गरियो, दुवै
    असाइनमेन्ट नोटबुकहरू (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), र .NET `.dib` नोटबुक।

### हटाइयो

- पुरानो `python/aoai-app-variation.py` र `python/oai-app-variation.py` नमूनाहरू मेटाइयो
  (`images.create_variation` केवल DALL·E-2 को लागि हो र `gpt-image` द्वारा समर्थन गरिएको छैन)।
- हटाइएको तापक्रम तुलना सेक्सनसँग जोडिएका ४ वटा अनाथ छवि सम्पत्तिहरू मेटाइयो
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`)।
- पाठको Python नमूनाहरू र आवश्यकताहरूबाट अनावश्यक `requests` निर्भरता हटाइयो।

### प्रमाणित गरिएको

- `aoai-app.py` लाई तैनाथ गरिएको `gpt-image-1.5` मोडेल विरुद्ध अन्तसम्म चलाइयो र आधार64
  डिकोड/सेभ प्रवाहले PNG उत्पादन गर्छ भनी पुष्टि गरियो। नोटबुकहरू मान्य JSON हुन पुष्टि गरियो।

## [2026-07-14] — डिफल्ट मोडेल अपडेट + कारण-आधारित मोडेल मार्गदर्शन

### परिवर्तन गरियो

- **डिफल्ट च्याट मोडेल `gpt-4o-mini` → `gpt-5-mini`** पाठ्यक्रमका चलाउन मिल्ने नमूनाहरू,
  कागजातहरू, र कन्फिगरेसन भित्र। यो मोडेल जीवनचक्र स्थिति अनुसार गरिएको हो: Microsoft Foundry मा,
  `gpt-4o-mini` (2026-10-01 मा सेवानिवृत्त) र सम्पूर्ण `gpt-4.1` परिवार (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, 2026-10-14 मा सेवानिवृत्त) **अप्रचलित हुँदैछन्**, जबकि **GPT-5 परिवार
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) सामान्य रूपमा उपलब्ध** छ (2027-02-06 मा सेवानिवृत्त)। अपडेट गरिएको:
  - `.env.copy`, `00-course-setup/03-providers.md` (सिफारिस गरिएका डिप्लोयमेन्ट र `az cognitiveservices`
    डिप्लोय कमाण्डहरू), र पाठ 04, 06, 07, र 15 का README हरू।
  - पाठ 06 का Python नमूनाहरू (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) र पाठ 08 स्क्रिप्टहरू।
  - पाठ 06, 07, र 11 मा TypeScript / JavaScript नमूनाहरू, र पाठ 06 र 07 का `.dib` .NET नोटबुकहरू।
  - पाठ 04, 06, 07, र 11 मा असाइन्मेंट नोटबुकहरू (कोड सेल्लहरू), साथै `shared/python/api_utils.py`
    डकस्ट्रिङ उदाहरणहरू।
- **तर्क-मोडेल प्यारामीटर मार्गनिर्देशन (नयाँ)।** `gpt-5-mini` एक *तर्क* मोडेल हो: यसले **समर्थन गर्दैन**
  `temperature`/`top_p`, र प्रयोग गर्छ `max_completion_tokens` (च्याट पूर्णताहरू) /
  `max_output_tokens` (रिस्पोन्स API) जसको सट्टा `max_tokens`। त्यसैले:
  - नमूनाहरूबाट `temperature`/`top_p`/`max_tokens` हटाइयो जुन अहिले डिफल्ट छन् `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, पाठ 15 RAG README) मा।
  - पाठ 06 मा **"तर्क मोडेलहरूले `temperature` प्रयोग गर्दैनन्"** नोट थपियो,
    जुन बताउँछ कि तर्क मोडेलहरू **प्रम्प्ट इन्जिनियरिङ + तर्क नियन्त्रणहरूले** सञ्चालित हुन्छन् न कि
    स्याम्पल गर्ने घुम्तीहरूले, जबकि `temperature`/`top_p` गैर-तर्क मोडेलहरूमा मान्य रहन्छन्
    (GPT-4.x, Mistral, Llama, Phi, खुला मोडेलहरू) मा।
- **`gpt-5-mini` फाइन-ट्युनिङ ट्युटोरियल (पाठ 18) मा प्रयोग हुँदैन।** GPT-5 मात्र
  रिइन्फोर्समेन्ट फाइन-ट्युनिङ (RFT) लाई समर्थन गर्दछ; पाठ 18 सुपरवाइज्ड फाइन-ट्युनिङ (SFT)
  वाक्थ्रुमा `gpt-4.1-mini` राखिएको छ, जसले SFT/DPO लाई समर्थन गर्दछ।
- **तेमपरचर डेमोहरूका लागि Llama मोडेल प्रयोग गरिन्छ।** `temperature` सिकाउन राख्नलाई (जसलाई तर्क मोडेलहरूले
  अस्विकार गर्छन्), Foundry मोडेल अन्तबिन्दु मार्फत `Llama-3.3-70B-Instruct` मोडेल प्रयोग गरिएको छ। नयाँ
  `AZURE_INFERENCE_CHAT_MODEL` भेरिएबल `.env.copy` मा थपियो; पाठ 04/06 को `githubmodels` नोटबुकहरू र
  `06` `js-githubmodels` नमूनाले यसलाई पढ्छ (`Llama-3.3-70B-Instruct` मा फेलब्याक गर्दै) र आफ्नो
  `temperature`/`top_p`/`max_tokens` डेमोहरू राख्छ।
- **JS / .NET नमूनाहरू GPT-5 का लागि अपडेट गरियो।** GPT-5 नमूनाबाट `temperature`/`top_p`/`max_tokens` हटाइयो
  (`06` `recipe-app` TypeScript, `06` `.dib` .NET - जुनले पनि `MaxOutputTokenCount`
  उठाउँछ जसले तर्क नतिजा कटौती हुँदैन)। `06` `js-githubmodels` नमूनाले अब Llama प्रयोग गर्दछ ताकि
  आफ्नो तापक्रम डेमो राख्न सकोस्। `.dib` नोट्छ कि `Azure.AI.Inference` + Llama मोडेल नै तरिका हो
  .NET मा `Temperature` देखाउन।
- `gpt-4o-mini` / `gpt-5-mini` यथास्थितिमा छोडियो जहाँ तिनीहरू सहि छन्: `tiktoken` टोकन-एन्कोडिङ
  सन्दर्भहरू, मोडेल-केटलोग उपलब्धता सूचीहरू, र पाठ 02 भाषण मोडेलहरू (`gpt-4o-transcribe`) मा।
- पाठ 20 (Mistral) र 21 (Meta) नमूनाहरूले `temperature`/`max_tokens` राख्छन् किनभने तिनीहरूले
  Mistral/Llama मोडेलहरूलाई लक्षित गर्छन्, जसले ती प्यारामीटरहरू समर्थन गर्दछन्।


## [2026-07-06] — सामग्री आधुनिकीकरण रिफ्रेस

२०२६ का लागि पाठ्यक्रमलाई सही राख्न व्यापक रिफ्रेस: आधुनिक API हरु, हालका उत्पादन नाम र
मोडेल नामहरू, अद्यावधिक प्रदायक मार्गनिर्देशन, र नयाँ विकासकर्ता अनुभव उपकरणहरू।

### थपियो

- **Microsoft Agent Framework** सेसन पाठ `17-ai-agents` मा जसले एकल च्याट एजेन्टहरू,
  उपकरण/फङ्शन कलिङ, Azure OpenAI (Microsoft Foundry) कन्फिगरेशन, र बहु-एजेन्ट
  वर्कफ्लो अर्केस्ट्रेसन (`SequentialBuilder` / `ConcurrentBuilder`) समेट्छ।
- **Foundry Local** लाई अफलाइन / डिभाइसमा आधारित प्रदायकको रूपमा कागजात गरिएको (Ollama सँगै)
  `00-course-setup/03-providers.md` र पाठ `19-slm` मा।
- **लगातार एकीकरण वर्कफ्लोहरू**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (मा पाँचतर्फी राखिएको `shared/`
    मोड्युलमा, पाठ्यक्रमको बाँकीमा सल्लाहकार), एक ESLint सल्लाहकार पास, र pytest कार्य।
  - `.github/workflows/security.yml` — CodeQL विश्लेषण (Python + JavaScript/TypeScript) र
    पुल अनुरोधहरूमा निर्भरता समीक्षा।
- **परीक्षण सूट** `tests/` अन्तर्गत — साझा उपयोगिता मोड्युलका लागि ४१ pytest परीक्षणहरूसहित।
- **Azure OpenAI → Responses API माइग्रेसन कौशल** `.github/skills/azure-openai-to-responses/` अन्तर्गत
  API माइग्रेसन गाइडका लागि प्रयोग गरिएको।

### परिवर्तन गरियो

- **Chat Completions API → Responses API** सबै Python र TypeScript च्याट नमूनाहरूमा
  (`client.responses.create(...)` → `response.output_text`), जसमा पाठ ०४, ०६, ०७, ११,
  १५ र १८, र तिनीहरूको README हरू।
- **GitHub मोडेलहरू → Microsoft Foundry मोडेलहरू** पूरा लेख, लिंकहरू, र नमूनाहरूमा। GitHub मोडेलहरू
  जुलाई २०२६ को अन्त्यमा अवकाशमा जानेछन्; नमूनाहरूले अहिले Microsoft Foundry मोडेल क्याटलगलाई जनाउँछन् र
  `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL` वातावरण चरहरू प्रयोग गर्छन्।
- **`.env.copy`, `AGENTS.md`, र प्रदायक कागजातहरू** अद्यावधिक गरी यो प्रतिबिम्बित गरिएको कि Azure OpenAI अब
  Microsoft Foundry को हिस्सा हो, र डिफल्ट API संस्करण `2024-10-21` मा बढाइएको।
- **TypeScript नमूनाहरू** (पाठहरू ०६, ०७, ०८, ११) अवैध घोषित `@azure/openai`
  बीटा SDK बाट `openai` प्याकेजमा सारिएको (च्याट एपहरूले Responses API प्रयोग गर्छन्; खोज एपले
  embeddings क्लायन्ट प्रयोग गर्छ)।
- **.NET नोटबुकहरू** (`dotnet/*.dib`) मा मानकीकृत गरियो `Azure.AI.OpenAI` **2.1.0** मा: पाठहरू ०६ र ०७
  मा `ChatClient` API प्रयोग हुन्छ, पाठ ०८ मा `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`) प्रयोग हुन्छ, र
  पाठ ०९ मा `ImageClient` (`GenerateImage`) साथ `gpt-image-1` प्रयोग गरिन्छ, पुरानो
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` लाई `1.0.0-beta.9` बाट प्रतिस्थापन गर्दै।
- **उत्पादन नाम आधुनिकीकरण**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (पाठहरू १४, १६, १७) र "Bing" → **Microsoft Copilot** (पाठ १२), जहाँ तिनीहरूले
  हालका उत्पादनहरूको उल्लेख गरेका थिए।
- **DevContainer** (`.devcontainer/`) मा अब Pylance, Black, Ruff, ESLint, Prettier, र Copilot
  एक्सटेन्सनहरू सामेल छन्, ढाँचाकरण-सेभमा सक्षम बनाइन्छ, र `ruff`, `black`, `mypy`, र `pytest` इन्स्टल गरेर CI
  जाँचहरू स्थानीय रूपमा पुन: उत्पादन गर्न सकिन्छ।
- **छबि सिर्जना** (पाठ ०९) ले Azure का लागि `gpt-image-1` सिफारिस गर्छ (Azure क्याटलगले
  `dall-e-3` हटाएको छ)।
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** पूरा भइसकेको काम (API माइग्रेसन, CI,
  DevContainer, परीक्षणहरू) र वर्तमान तथ्यहरू (अनुवादहरू स्वतः Azure Co-op Translator द्वारा उत्पादन हुन्छन्;
  Assistants API लाई Responses API द्वारा प्रतिस्थापित गरिएको छ) प्रतिबिम्बित गर्न अद्यावधिक गरिएको।

### समाधान गरियो

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` अब खाली ठाउँ मात्र भएको इनपुटको लागि खाली स्ट्रिङ फर्काउँछ, "धेरै छोटो" त्रुटि उठाउने सट्टा (`None` केससँग सुसंगत)। नयाँ परीक्षण समूहले भेट्टायो र समेट्यो।
 
 
- **Lesson 09 image samples** — ठीक गरिएका वास्तविक बगहरू: `InvalidRequestError` → `BadRequestError`, `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`, र एउटा भेरिएबल जसले `openai` मोड्युललाई छायाँ बनाएको थियो।
 
 
- **Lesson 15 RAG notebook** — क्लाइन्ट सेटअप मर्मत गरिएको, हटाइएको `DataFrame.append` लाई `pd.concat` सँग प्रतिस्थापित गरिएको, र पुरानो SDK प्रयोगलाई आधुनिक बनाइएको।
 
- फालिएका / अवकाश लिइएका मोडल नामहरू (`gpt-3.5-turbo`, `gpt-35-turbo`) सक्रिय नमूनाहरूमा `gpt-4o-mini` सँग बदलिएको; पाठ १८ मा ऐतिहासिक फाइन-ट्यूनिंग नतिजाहरू सुरक्षित राखिएका र टिप्पणी गरिएको थियो, पुनर्लेखन नगरी।
 
 

### फालिएका / नोटहरू

- **Microsoft Foundry मोडेल नमूनाहरू** जुन `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) प्रयोग गर्छन् — `githubmodels-*` र `js-githubmodels` नमूनाहरू र पाठहरू १९, २०,
  र २१ — मोडेल इन्फेरेन्स API मा रहन्छन्, जुन जवाफहरू API समर्थन गर्दैन। यी
  जानाजानी त्यो SDK मा छोडिएका छन्।
- `AzureOpenAI()` जानाजानी जहाँ अझै उपयुक्त छ त्यहाँ राखिएको छ (एम्बेडिंग र छवि उत्पादन),
  किनकि ती कार्यप्रवाहहरू जवाफहरू API माइग्रेशनको हिस्सा होइनन्।
- `text-embedding-ada-002` सन्दर्भहरू राखिएका छन् जहाँ अघिल्लो गणना गरिएको एम्बेडिंग सूची तिनीहरूमा निर्भर छ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->