# बदलनोंची नोंद

Generative AI for Beginners अभ्यासक्रमातील सर्व लक्षणीय बदल या फाईलमध्ये नोंदवले आहेत.

स्वरूप [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) वर आधारित आहे. हे एक आवृत्तीबद्ध सॉफ्टवेअर पॅकेज नसून
हे एक शिकण्याचे अभ्यासक्रम असल्यामुळे नोंदी तारखेनुसार गटबद्ध केल्या आहेत.

## [2026-07-16] — सामग्री सत्यापन + धडा 09 छायाचित्रे साधने

### बदललेले

- **धडा 10 (लो-कोड AI अॅप्स):** दोन निवृत्त झालेले `docs.microsoft.com/powerapps/...` Dataverse दुवे वर्तमान `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro` साठी अद्ययावत केले
  (सजीव तपासलेले).
- **धडा 17 (AI एजंट्स):** जुन्या मॉडेल उदाहरणाचा अद्यतनीकरण (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, and Llama 3.3`) आणि Agent Framework नमुन्यामध्ये प्लेसहोल्डर तैनातीचे नाव
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **रूट `README.md`:** *Microsoft for Startups* लिंकसाठी हरवलेले `?WT.mc_id=academic-105485-koreyst` ट्रॅकिंग ID जोडले.
- **धडा 09 छायाचित्रे साधने** `gpt-image` मॉडेलसह पुनर्जन्मित: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, आणि
  `images/startup.png` (संपादन उदाहरणाचा आधी/नंतरचा जोडी खऱ्या एक
  `client.images.edit` कॉलने तयार केलेला मास्कसह तयार केला गेला).

### सत्यापित

- धडा 01, 03, 05, 12, 14, आणि 16 साठी README तपासले — सगळे वर्तमान (योग्य Microsoft Foundry

- धड्यां 01, 03, 05, 12, 14, आणि 16 साठी READMEs चे ऑडिट केले — सगळे चालू (बरोबर Microsoft Foundry नावाकरण आणि दुवे);
  काही बदल आवश्यक नाहीत.
- संचिका रिपॉझिटरीमधील सर्व ४१ मार्कडाउन फाइल्सवर (अनुवाद वगळून) पूर्ण मार्कडाउन पडताळणी केली
  जुने दस्तऐवज मार्ग, `/en-us/` मायक्रोसॉफ्ट लोकल्स, जुनी उत्पादने/मॉडेल नावे, हरवलेले ट्रॅकिंग
  आयडी, आणि तुटलेले सापेक्ष दुवा/प्रतिमा होण्यासाठी. फक्त एकच *Microsoft for Startups* ट्रॅकिंग-आयडीचा अंतर
  उपयुक्त ठरला; इतर सर्व चिन्हांकने खोटे सकारात्मक असल्याचे सुनिश्चित झाले (स्वयंनिर्मित अनुवाद दुवे,
  टिप्पणी-आउट केलेले प्लेसहोल्डर्स, आणि तृतीय-पक्ष `/en/` संरचनात्मक URLs).

## [२०२६-०७-१५] — धडा ०९ (प्रतिमा अनुप्रयोग) GPT प्रतिमा मॉडेलसाठी पुन्हा लिहिले

### बदलले

- **धडा ०९ "प्रतिमा निर्मिती अनुप्रयोग तयार करणे"** वर्तमान **`gpt-image`**
  मॉडेल कुटुंबाभोवती (डिफॉल्ट **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` देखील GA), जुना
  DALL·E 2/3 सामग्री बदलल्याची नोंद. महत्वाची दुरुस्त्या:
  - `gpt-image` मॉडेल प्रतिमा **base64 (`b64_json`)** स्वरूपात परत करतात, URL नाही. सर्व नमुने अद्ययावत केले
    `base64.b64decode(...)` डाउनलोड करण्याऐवजी `url` सह `requests`.
  - प्रतिमेच्या API ची आवृत्ती `2025-04-01-preview` वर वाढवली.
  - बनावट "temperature" विभाग (प्रतिमा मॉडेल्स `temperature` घेत नाहीत) आणि
    DALL·E-2-फक्त प्रतिमा **विविधता** सामग्रीचे ठिकाणी **प्रतिमा संपादन** (मास्क/इनपेंटिंग) विभाग ठेवला.
  - अद्यतनित केले `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, दोन्ही
    असाईनमेंट नोटबुक्स (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), आणि .NET `.dib` नोटबुक.

### काढून टाकले

- जुने `python/aoai-app-variation.py` आणि `python/oai-app-variation.py` नमुने काढून टाकले
  (`images.create_variation` ही DALL·E-2-फक्त आहे आणि `gpt-image` द्वारे समर्थन केली जात नाही).
- 4 अनावश्यक प्रतिमा स्रोत जे तापमान-संपादने विभागाशी संबंधित होते, काढून टाकले
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- धडा मधील पायथन नमुन्यांमधून आणि आवश्यकतांमधून अनावश्यक `requests` अवलंबित्व काढून टाकले.

### पडताळणी केले

- `aoai-app.py` चे पूर्णपणे एकत्रित चाचणी केले जे एका तैनात `gpt-image-1.5` मॉडेलविरुद्ध आणि पुष्टी केली की base64
  डीकोड/जतन प्रवाह PNG तयार करतो. नोटबुक्स वैध JSON असल्याचे पुष्टी केले.

## [2026-07-14] — डीफॉल्ट मॉडेल अपडेट + कारण-आधारित मॉडेल मार्गदर्शन

### बदलले

- **डीफॉल्ट चॅट मॉडेल `gpt-4o-mini` → `gpt-5-mini`** संपूर्ण अभ्यासक्रमाच्या चालणाऱ्या नमुन्यांमध्ये,
  दस्तऐवज आणि संरचनेत. हे मॉडेलच्या जीवनचक्र स्थितीने प्रेरित होते: मायक्रोसॉफ्ट फाउंड्रीवर,
  `gpt-4o-mini` (2026-10-01 रोजी निवृत्ती होण्यास) आणि संपूर्ण `gpt-4.1` कुटुंब (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, 2026-10-14 रोजी निवृत्ती होणार) **डिप्रिकेट करीत आहेत**, तर **GPT-5 कुटुंब
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) सामान्यतः उपलब्ध आहे** (2027-02-06 रोजी निवृत्ती होणार नाही). अद्ययावत:
  - `.env.copy`, `00-course-setup/03-providers.md` (शिफारस केलेली तैनात आणि `az cognitiveservices`
    तैनात आदेश), आणि धडे 04, 06, 07 आणि 15 च्या README फाइल्स.
  - धडा 06 मधील Python नमुने (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) आणि धडा 08 चे स्क्रिप्ट्स.
  - धडे 06, 07 आणि 11 मधील TypeScript / JavaScript नमुने, आणि `.dib` .NET नोटबुक्स
    धडे 06 आणि 07 साठी.
  - धडा 04, 06, 07, आणि 11 मधील असाइनमेंट नोटबुक (कोड सेल्स), तसेच `shared/python/api_utils.py`
    डॉकस्ट्रिंग उदाहरणे.
- **तर्क-मॉडेल पॅरामीटर मार्गदर्शन (नवीन).** `gpt-5-mini` हा एक *तर्क* मॉडेल आहे: तो **नाही**
  `temperature`/`top_p` ला समर्थन देतो, आणि `max_completion_tokens` (चॅट पूर्णता) /
  `max_output_tokens` (प्रतिसाद API) वापरतो, `max_tokens` च्या ऐवजी. तदनुसार:
  - तापडीतून `temperature`/`top_p`/`max_tokens` काढले गेले जे आता `gpt-5-mini` वर डीफॉल्ट होतात
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, धडा 15 RAG README).
  - धडा 06 मध्ये **"Reasoning models don't use `temperature`"** असा एक नोंद जोडला, ज्यात स्पष्ट करण्यात आले की
    reasoning मॉडेल्सना **prompt engineering + reasoning controls** द्वारे चालवले जाते, बजाय
    sampling knobs, तर `temperature`/`top_p` हे गैर-रेझनिंग मॉडेल्सवर वैध राहतात
    (GPT-4.x, Mistral, Llama, Phi, खुल्या मॉडेल्स).
- **`gpt-5-mini` हा फाईन-ट्युनिंग ट्युटोरियलसाठी (धडा 18) वापरला जात नाही.** GPT-5 फक्त
  reinforcement fine-tuning (RFT) पाठिंबा करतो; धडा 18 मध्ये सुपरवाइज्ड फाईन-ट्युनिंग (SFT) walkthrough मध्ये
  `gpt-4.1-mini` वापरले जाते, जे SFT/DPO ला समर्थन देतो.
- **Temperature डेमोजसाठी Llama मॉडेल वापरला जातो.** जेणेकरून `temperature` शिकवण चालू राहील (जे reasoning मॉडेल्स
  नाकारतात), Foundry Models endpoint द्वारे एक `Llama-3.3-70B-Instruct` मॉडेल वापरले जाते. नवीन
  `AZURE_INFERENCE_CHAT_MODEL` चल `.env.copy` मध्ये जोडले गेले; धडा 04/06 च्या `githubmodels` नोटबुक्स आणि
  `06` च्या `js-githubmodels` नमुन्याने ते वाचले (परत पडणे `Llama-3.3-70B-Instruct` कडे) आणि त्यांचे
  `temperature`/`top_p`/`max_tokens` डेमोज ठेवले.
- **GPT-5 साठी JS / .NET नमुने अपडेट केले आहेत.** GPT-5 नमुन्यांमधून `temperature`/`top_p`/`max_tokens` काढले
  गेले आहेत (`06` `recipe-app` TypeScript, `06` `.dib` .NET - ज्यामुळे `MaxOutputTokenCount` वाढवतो
  जेणेकरून reasoning आउटपुट कट न होईल). `06` चा `js-githubmodels` नमुना आता तापमान डेमो ठेवण्यासाठी Llama वापरतो.
  `.dib` मध्ये नमूद केले आहे की `Azure.AI.Inference` + एक Llama मॉडेल हा मार्ग आहे
  .NET मध्ये `Temperature` दाखविण्याचा.
- जिथे ते अचूक राहतात तिथे `gpt-4o-mini` / `gpt-5-mini` जतन केले आहे: `tiktoken` टोकन-एन्कोडिंग
  संदर्भ, मॉडेल-कॅटलॉग उपलब्धता यादी, आणि धडा 02 भाषण मॉडेल्स (`gpt-4o-transcribe`).
- धडा 20 (Mistral) आणि 21 (Meta) नमुने `temperature`/`max_tokens` ठेवतात कारण ते Mistral/Llama मॉडेल्सवर लक्ष केंद्रित करतात,
  जे त्या पॅरामीटर्सना समर्थन करतात.

## [2026-07-06] — सामग्री आधुनिकरण पुनरावलोकन

2026 साठी अभ्यासक्रम अचूक ठेवण्यासाठी एक व्यापक पुनरावलोकन: आधुनिक API, सध्याच्या उत्पादनांची नावे आणि
मॉडेलांची नावे, अद्ययावत प्रदाता मार्गदर्शन, आणि नवीन विकास अनुभव साधने.

### जोडले

- धडा `17-ai-agents` मध्ये **Microsoft Agent Framework** विभाग, एकल चॅट एजंट्स,
  टूल्स/फंक्शन कॉलिंग, Azure OpenAI (Microsoft Foundry) कॉन्फिगरेशन, आणि मल्टी-एजंट
  वर्कफ्लो ऑर्केस्ट्रेशन (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** ऑफलाइन / ऑन-डिव्हाइस प्रदाता (Ollama सोबत) म्हणून
  `00-course-setup/03-providers.md` आणि धडा `19-slm` मध्ये दस्तऐवजीकृत.
- **सतत समाकलन वर्कफ्लोज**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (मान्य केलेल्या `shared/` मॉड्यूलवर लागू,
    अभ्यासक्रमातील इतर भागात सल्लागार), एक सल्लागार ESLint प्रक्रिया, आणि pytest नोकरी.
  - `.github/workflows/security.yml` — CodeQL विश्लेषण (Python + JavaScript/TypeScript) आणि
    पुल रिक्वेस्टवर अवलंबित्व पुनरावलोकन.
- **टेस्ट सूट** `tests/` अंतर्गत — 41 pytest चाचण्या जे संयुक्त यूटिलिटी मॉड्यूल कव्हर करतात.
- **Azure OpenAI → Responses API स्थलांतर कौशल्य** `.github/skills/azure-openai-to-responses/` अंतर्गत जे API स्थलांतर मार्गदर्शनासाठी वापरले जाते.




  (`client.responses.create(...)` → `response.output_text`), ज्यामध्ये धडे 04, 06, 07, 11,
  15, आणि 18 तसेच त्यांच्या README समाविष्ट आहेत.
- **GitHub Models → Microsoft Foundry Models** सर्व लेख, दुवे, आणि नमुन्यांत बदल. GitHub Models
  जुलै 2026 च्या शेवटी रिटायर होत आहेत; नमुने आता Microsoft Foundry मॉडेल कॅटलॉगकडे निर्देशित करतात आणि
  `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL` एन्व्हायर्नमेंट बदल गोल वापरतात.
- **`.env.copy`, `AGENTS.md`, आणि प्रदाता दस्तऐवज** अद्ययावत झाले आहेत ज्यामुळे Azure OpenAI आता Microsoft Foundry चा भाग आहे,
  आणि डीफॉल्ट API आवृत्ती `2024-10-21` वर वाढवलेली आहे.
- **TypeScript नमुने** (धडे 06, 07, 08, 11) अप्रचलित `@azure/openai`
  बीटा SDK कडून `openai` पॅकेजकडे स्थलांतरित, जेथे चॅट अॅप्स Responses API वापरतात; सर्च अॅप embeddings क्लायंट वापरतो.
- **.NET नोटबुक्स** (`dotnet/*.dib`) वर `Azure.AI.OpenAI` **2.1.0** प्रमाणित: धडा 06 आणि 07
  `ChatClient` API वापरतात, धडा 08 `EmbeddingClient` वापरतो (`GenerateEmbedding` / `ToFloats`), आणि
  धडा 09 `ImageClient` वापरतो (`GenerateImage`) `gpt-image-1` सह, ज्यामध्ये जुन्या
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` बदली केली आहे `1.0.0-beta.9` कडून.
- **उत्पादन-नाव आधुनिकरण**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (धडे 14, 16, 17) आणि "Bing" → **Microsoft Copilot** (धडा 12), जेथे ती सध्याची उत्पादने होती.
- **उत्पादन-नाव आधुनिकीकरण**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (पाठ 14, 16, 17) आणि "Bing" → **Microsoft Copilot** (पाठ 12), जिथे ते
  सध्याच्या उत्पादनांकडे निर्देश करत होते.
- **DevContainer** (`.devcontainer/`) आता Pylance, Black, Ruff, ESLint, Prettier, आणि Copilot
  एक्सटेंशन्स पाठवतो, फॉर्मॅट-ऑन-सेव सक्षम करतो, आणि `ruff`, `black`, `mypy`, आणि `pytest` स्थापित करतो जेणेकरून CI
  तपासणी स्थानिक पातळीवर पुनरुत्पादित केली जाऊ शकतील.
- **इमेज जनरेशन** (धडा ०९) Azure साठी `gpt-image-1` शिफारस करतो (Azure कॅटलॉगने 
  `dall-e-3` काढला).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** पूर्ण झालेल्या कामाचे प्रतिबिंब दर्शविण्यासाठी अद्यतनित केले (API स्थलांतर, CI,
  DevContainer, चाचण्या) आणि सध्याच्या तथ्यांसाठी (भाषांतर स्वयंचलितपणे Azure Co-op Translator कडून तयार केल्या जातात;
  Assistants API ची जागा Responses API ने घेतली आहे).

### दुरुस्त केले

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` आता फक्त whitespace असलेल्या इनपुटसाठी एक रिकामी स्ट्रिंग परत करतो, "too short" त्रुटी उचलण्याऐवजी (जे `None` प्रकरणाशी सुसंगत आहे). नवीन टेस्ट सूटने शोधले आणि कव्हर केले आहे.
  
  
- **Lesson 09 image samples** — सुधारित वास्तविक बग्ज़: `InvalidRequestError` → `BadRequestError`, `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`, आणि एका चराने `openai` मॉड्यूलवर छाया टाकली होती.
  
  
- **Lesson 15 RAG notebook** — क्लायंट सेटअप दुरुस्त केला, काढलेले `DataFrame.append` वगळून `pd.concat` वापरले, आणि जुन्या SDK चा उपयोग आधुनिक केला.
  
- वापरात नसलेले / निवृत्त मॉडेल नावे (`gpt-3.5-turbo`, `gpt-35-turbo`) सक्रिय सॅम्पल्समध्ये `gpt-4o-mini` ला बदलण्यात आली; अध्याय 18 मधील ऐतिहासिक फाइन-ट्यूनिंग आउटपुट जतन केले आणि टिपणी केली गेली, पुनर्लेखन नाही.
  
  

### वापरात नसलेले / नोंदी

- **Microsoft Foundry Models samples** जे `azure-ai-inference` / `@azure-rest/ai-inference` SDK (`client.complete()`) वापरतात — `githubmodels-*` आणि `js-githubmodels` सॅम्पल्स आणि धडे 19, 20, आणि 21 — Model Inference API वर आहेत, जे Responses API ला **समर्थन नाही** देत. हे SDK वर शिल्लक ठेवण्यात आले आहे.
  
  
  
- `AzureOpenAI()` जिथे योग्य तिथे उद्देशाने राखण्यात आले आहे (एम्बेडिंग्ज आणि प्रतिमा निर्मितीसाठी), कारण ते workflows Responses API माइग्रेशनचा भाग नाहीत.
  
- `text-embedding-ada-002` संदर्भ राखले आहेत जिथे पूर्वनिर्धारित एम्बेडिंग निर्देशांक त्यावर अवलंबून आहे.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->