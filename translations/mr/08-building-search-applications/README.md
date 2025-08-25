<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d46aad0917a1a342d613e2c13d457da5",
  "translation_date": "2025-07-09T12:51:43+00:00",
  "source_file": "08-building-search-applications/README.md",
  "language_code": "mr"
}
-->
# शोध अनुप्रयोग तयार करणे

[![Generative AI आणि Large Language Models परिचय](../../../translated_images/08-lesson-banner.8fff48c566dad08a1cbb9f4b4a2c16adfdd288a7bbfffdd30770b466fe08c25c.mr.png)](https://aka.ms/gen-ai-lesson8-gh?WT.mc_id=academic-105485-koreyst)

> > _या धड्याचा व्हिडिओ पाहण्यासाठी वरील प्रतिमा क्लिक करा_

LLMs म्हणजे फक्त चॅटबॉट्स आणि मजकूर निर्मितीपुरते मर्यादित नाहीत. Embeddings वापरून शोध अनुप्रयोग तयार करणे देखील शक्य आहे. Embeddings म्हणजे डेटा चे संख्यात्मक प्रतिनिधित्व, ज्याला व्हेक्टर देखील म्हणतात, आणि याचा वापर डेटा साठी अर्थपूर्ण शोधासाठी केला जातो.

या धड्यात, आपण आपल्या शिक्षण स्टार्टअपसाठी एक शोध अनुप्रयोग तयार करणार आहोत. आमचा स्टार्टअप हा एक नॉन-प्रॉफिट संस्था आहे जी विकासशील देशांतील विद्यार्थ्यांना मोफत शिक्षण पुरवते. आमच्याकडे AI शिकण्यासाठी वापरता येणाऱ्या अनेक YouTube व्हिडिओंचा संग्रह आहे. आमचा स्टार्टअप असा शोध अनुप्रयोग तयार करू इच्छितो ज्याद्वारे विद्यार्थी प्रश्न टाइप करून YouTube व्हिडिओ शोधू शकतील.

उदाहरणार्थ, एखादा विद्यार्थी 'Jupyter Notebooks म्हणजे काय?' किंवा 'Azure ML म्हणजे काय?' असा प्रश्न टाइप करू शकतो आणि शोध अनुप्रयोग त्या प्रश्नाशी संबंधित YouTube व्हिडिओंची यादी परत करेल, आणि आणखी चांगले म्हणजे, शोध अनुप्रयोग त्या व्हिडिओतील त्या ठिकाणी लिंक देखील परत करेल जिथे प्रश्नाचे उत्तर आहे.

## परिचय

या धड्यात आपण खालील गोष्टी शिकणार आहोत:

- Semantic आणि Keyword शोध यामधील फरक.
- Text Embeddings म्हणजे काय.
- Text Embeddings Index तयार करणे.
- Text Embeddings Index मध्ये शोध घेणे.

## शिकण्याचे उद्दिष्ट

हा धडा पूर्ण केल्यानंतर, तुम्ही सक्षम असाल:

- Semantic आणि Keyword शोध यामधील फरक सांगू शकता.
- Text Embeddings काय आहेत हे समजू शकता.
- Embeddings वापरून डेटा शोधण्यासाठी अनुप्रयोग तयार करू शकता.

## शोध अनुप्रयोग का तयार करायचा?

शोध अनुप्रयोग तयार केल्याने तुम्हाला Embeddings वापरून डेटा कसा शोधायचा हे समजेल. तसेच, तुम्ही असा शोध अनुप्रयोग तयार कराल जो विद्यार्थ्यांना माहिती पटकन शोधण्यात मदत करेल.

या धड्यात Microsoft [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) YouTube चॅनेलच्या ट्रान्सक्रिप्टसाठी Embedding Index दिला आहे. AI Show हा एक YouTube चॅनेल आहे जो तुम्हाला AI आणि मशीन लर्निंग शिकवतो. Embedding Index मध्ये ऑक्टोबर 2023 पर्यंतच्या प्रत्येक YouTube ट्रान्सक्रिप्टसाठी Embeddings आहेत. तुम्ही या Embedding Index चा वापर करून आमच्या स्टार्टअपसाठी शोध अनुप्रयोग तयार कराल. हा शोध अनुप्रयोग त्या व्हिडिओतील त्या ठिकाणी लिंक परत करतो जिथे प्रश्नाचे उत्तर आहे. हे विद्यार्थ्यांसाठी आवश्यक माहिती पटकन शोधण्याचा उत्तम मार्ग आहे.

खालील उदाहरणात 'can you use rstudio with azure ml?' या प्रश्नासाठी semantic क्वेरी दाखवली आहे. YouTube URL मध्ये timestamp आहे जो तुम्हाला त्या व्हिडिओतील त्या ठिकाणी घेऊन जातो जिथे प्रश्नाचे उत्तर आहे.

![Semantic query for the question "can you use rstudio with Azure ML"](../../../translated_images/query-results.bb0480ebf025fac69c5179ad4d53b6627d643046838c857dc9e2b1281f1cdeb7.mr.png)

## Semantic शोध म्हणजे काय?

आता तुम्हाला कदाचित आश्चर्य वाटेल, semantic शोध म्हणजे काय? Semantic शोध ही अशी शोध तंत्र आहे जी क्वेरीतील शब्दांच्या अर्थाचा वापर करून संबंधित निकाल परत करते.

येथे semantic शोधाचे उदाहरण आहे. समजा तुम्हाला कार विकत घ्यायची आहे, तुम्ही 'my dream car' असा शोध घेऊ शकता. Semantic शोध समजतो की तुम्ही कारचे स्वप्न पाहत नाही, तर तुम्ही तुमची 'आदर्श' कार शोधत आहात. Semantic शोध तुमचा हेतू समजून संबंधित निकाल परत करतो. त्याच्या उलट, keyword शोध म्हणजे शब्दशः 'dreams about cars' शोधणे होय, जे अनेकदा असंबंधित निकाल देतो.

## Text Embeddings म्हणजे काय?

[Text embeddings](https://en.wikipedia.org/wiki/Word_embedding?WT.mc_id=academic-105485-koreyst) हे [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing?WT.mc_id=academic-105485-koreyst) मध्ये वापरले जाणारे मजकूराचे प्रतिनिधित्व तंत्र आहे. Text embeddings म्हणजे मजकूराचे अर्थपूर्ण संख्यात्मक प्रतिनिधित्व. Embeddings वापरून डेटा अशा प्रकारे सादर केला जातो की मशीनला तो समजायला सोपा होतो. Text embeddings तयार करण्यासाठी अनेक मॉडेल्स आहेत, या धड्यात आपण OpenAI Embedding Model वापरून embeddings तयार करण्यावर लक्ष केंद्रित करू.

उदाहरणार्थ, समजा खालील मजकूर AI Show YouTube चॅनेलमधील एका एपिसोडच्या ट्रान्सक्रिप्टमधून आहे:

```text
Today we are going to learn about Azure Machine Learning.
```

आपण हा मजकूर OpenAI Embedding API कडे पाठवू आणि तो 1536 संख्यांचा एक embedding (व्हेक्टर) परत करेल. व्हेक्टरमधील प्रत्येक संख्या मजकूराच्या वेगळ्या पैलूचे प्रतिनिधित्व करते. संक्षिप्ततेसाठी, येथे व्हेक्टरमधील पहिले 10 नंबर दिले आहेत.

```python
[-0.006655829958617687, 0.0026128944009542465, 0.008792596869170666, -0.02446001023054123, -0.008540431968867779, 0.022071078419685364, -0.010703742504119873, 0.003311325330287218, -0.011632772162556648, -0.02187200076878071, ...]
```

## Embedding index कसा तयार केला जातो?

या धड्यासाठी Embedding index Python स्क्रिप्ट्सच्या मालिकेने तयार केला गेला आहे. तुम्हाला या स्क्रिप्ट्स आणि सूचना [README](./scripts/README.md?WT.mc_id=academic-105485-koreyst) मध्ये 'scripts' फोल्डरमध्ये सापडतील. या धडा पूर्ण करण्यासाठी तुम्हाला या स्क्रिप्ट्स चालवण्याची गरज नाही कारण Embedding Index आधीच उपलब्ध आहे.

स्क्रिप्ट्स खालील क्रिया करतात:

1. [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) प्लेलिस्टमधील प्रत्येक YouTube व्हिडिओची ट्रान्सक्रिप्ट डाउनलोड केली जाते.
2. [OpenAI Functions](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling?WT.mc_id=academic-105485-koreyst) वापरून, YouTube ट्रान्सक्रिप्टच्या पहिल्या 3 मिनिटांतून स्पीकरचे नाव काढण्याचा प्रयत्न केला जातो. प्रत्येक व्हिडिओसाठी स्पीकरचे नाव `embedding_index_3m.json` नावाच्या Embedding Index मध्ये साठवले जाते.
3. ट्रान्सक्रिप्ट मजकूर नंतर **3 मिनिटांच्या मजकूर विभागांमध्ये** विभागला जातो. प्रत्येक विभागात पुढील विभागातून सुमारे 20 शब्द ओव्हरलॅप केले जातात जेणेकरून विभागाचा Embedding कापला जाऊ नये आणि शोधासाठी चांगला संदर्भ मिळेल.
4. प्रत्येक मजकूर विभाग OpenAI Chat API कडे पाठवून 60 शब्दांमध्ये सारांशित केला जातो. हा सारांश देखील `embedding_index_3m.json` मध्ये साठवला जातो.
5. शेवटी, विभागाचा मजकूर OpenAI Embedding API कडे पाठवला जातो. Embedding API 1536 संख्यांचा व्हेक्टर परत करतो जो विभागाचा अर्थपूर्ण अर्थ दर्शवतो. विभाग आणि OpenAI Embedding व्हेक्टर `embedding_index_3m.json` मध्ये साठवले जातात.

### व्हेक्टर डेटाबेस

सोप्या समजासाठी, Embedding Index `embedding_index_3m.json` नावाच्या JSON फाईलमध्ये साठवलेला आहे आणि Pandas DataFrame मध्ये लोड केला जातो. पण उत्पादनात, Embedding Index अशा व्हेक्टर डेटाबेसमध्ये साठवला जातो जसे की [Azure Cognitive Search](https://learn.microsoft.com/training/modules/improve-search-results-vector-search?WT.mc_id=academic-105485-koreyst), [Redis](https://cookbook.openai.com/examples/vector_databases/redis/readme?WT.mc_id=academic-105485-koreyst), [Pinecone](https://cookbook.openai.com/examples/vector_databases/pinecone/readme?WT.mc_id=academic-105485-koreyst), [Weaviate](https://cookbook.openai.com/examples/vector_databases/weaviate/readme?WT.mc_id=academic-105485-koreyst) इत्यादी.

## कोसाइन सादृश्यता समजून घेणे

आपण text embeddings बद्दल शिकलो, पुढील टप्पा म्हणजे text embeddings वापरून डेटा कसा शोधायचा आणि विशेषतः दिलेल्या क्वेरीसाठी सर्वात सादृश्य embeddings कोसाइन सादृश्यता वापरून कसे शोधायचे हे शिकणे.

### कोसाइन सादृश्यता म्हणजे काय?

कोसाइन सादृश्यता म्हणजे दोन व्हेक्टरमधील सादृश्यतेचे मापन, याला `nearest neighbor search` असेही म्हणतात. कोसाइन सादृश्यता शोध करण्यासाठी तुम्हाला OpenAI Embedding API वापरून क्वेरी मजकूराचे व्हेक्टर तयार करावे लागते. नंतर क्वेरी व्हेक्टर आणि Embedding Index मधील प्रत्येक व्हेक्टर यांच्यात कोसाइन सादृश्यता मोजावी लागते. लक्षात ठेवा, Embedding Index मध्ये प्रत्येक YouTube ट्रान्सक्रिप्ट मजकूर विभागासाठी एक व्हेक्टर असतो. शेवटी, निकाल कोसाइन सादृश्यतेनुसार क्रमवारी लावली जाते आणि सर्वाधिक सादृश्यता असलेले मजकूर विभाग क्वेरीशी सर्वात जास्त सादृश्य असतात.

गणितीय दृष्टिकोनातून, कोसाइन सादृश्यता म्हणजे बहुआयामी जागेत प्रक्षिप्त दोन व्हेक्टरमधील कोनाचा कोसाइन मोजणे. हे मापन उपयुक्त आहे कारण जर दोन दस्तऐवज Euclidean अंतराने दूर असले तरी, त्यांच्यातील कोन लहान असल्यास त्यांची कोसाइन सादृश्यता जास्त असू शकते. कोसाइन सादृश्यता समीकरणांबद्दल अधिक माहितीसाठी, पहा [Cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity?WT.mc_id=academic-105485-koreyst).

## तुमचा पहिला शोध अनुप्रयोग तयार करणे

आता आपण Embeddings वापरून शोध अनुप्रयोग कसा तयार करायचा ते शिकणार आहोत. हा शोध अनुप्रयोग विद्यार्थ्यांना प्रश्न टाइप करून व्हिडिओ शोधण्याची परवानगी देईल. शोध अनुप्रयोग प्रश्नाशी संबंधित व्हिडिओंची यादी परत करेल. तसेच, प्रश्नाचे उत्तर असलेल्या व्हिडिओतील ठिकाणी लिंक देखील परत करेल.

हे समाधान Windows 11, macOS, आणि Ubuntu 22.04 वर Python 3.10 किंवा नंतरच्या आवृत्त्यांसह तयार आणि चाचणी केले गेले आहे. तुम्ही Python [python.org](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) वरून डाउनलोड करू शकता.

## असाइनमेंट - विद्यार्थ्यांसाठी शोध अनुप्रयोग तयार करणे

या धड्याच्या सुरुवातीला आपण आमचा स्टार्टअप ओळख करून दिला. आता विद्यार्थ्यांना त्यांच्या मूल्यांकनासाठी शोध अनुप्रयोग तयार करण्यास सक्षम करण्याची वेळ आली आहे.

या असाइनमेंटमध्ये, तुम्ही Azure OpenAI Services तयार कराल ज्याचा वापर शोध अनुप्रयोग तयार करण्यासाठी होईल. तुम्ही खालील Azure OpenAI Services तयार कराल. या असाइनमेंटसाठी तुम्हाला Azure सदस्यता आवश्यक आहे.

### Azure Cloud Shell सुरू करा

1. [Azure portal](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) मध्ये साइन इन करा.
2. Azure पोर्टलच्या वरच्या उजव्या कोपऱ्यातील Cloud Shell आयकॉन निवडा.
3. पर्यावरण प्रकारासाठी **Bash** निवडा.

#### रिसोर्स ग्रुप तयार करा

> या सूचनांसाठी, आपण "semantic-video-search" नावाचा रिसोर्स ग्रुप East US मध्ये वापरत आहोत.
> तुम्ही रिसोर्स ग्रुपचे नाव बदलू शकता, पण रिसोर्सेससाठी स्थान बदलताना,
> [model availability table](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) तपासा.

```shell
az group create --name semantic-video-search --location eastus
```

#### Azure OpenAI Service रिसोर्स तयार करा

Azure Cloud Shell मधून खालील कमांड चालवून Azure OpenAI Service रिसोर्स तयार करा.

```shell
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

#### या अनुप्रयोगात वापरण्यासाठी endpoint आणि keys मिळवा

Azure Cloud Shell मधून खालील कमांड्स चालवून Azure OpenAI Service रिसोर्ससाठी endpoint आणि keys मिळवा.

```shell
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

#### OpenAI Embedding मॉडेल तैनात करा

Azure Cloud Shell मधून खालील कमांड चालवून OpenAI Embedding मॉडेल तैनात करा.

```shell
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name text-embedding-ada-002 \
    --model-name text-embedding-ada-002 \
    --model-version "2"  \
    --model-format OpenAI \
    --sku-capacity 100 --sku-name "Standard"
```

## समाधान

GitHub Codespaces मध्ये [solution notebook](python/aoai-solution.ipynb) उघडा आणि Jupyter Notebook मधील सूचनांचे पालन करा.

जेव्हा तुम्ही नोटबुक चालवाल, तेव्हा तुम्हाला क्वेरी टाकण्यास सांगितले जाईल. इनपुट बॉक्स असे दिसेल:

![Input box for the user to input a query](../../../translated_images/notebook-search.1e320b9c7fcbb0bc1436d98ea6ee73b4b54ca47990a1c952b340a2cadf8ac1ca.mr.png)

## छान काम! तुमचे शिक्षण सुरू ठेवा

हा धडा पूर्ण केल्यानंतर, आमच्या [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) मध्ये जाऊन तुमचे Generative AI ज्ञान अधिक वाढवा!

पुढील धडा 9 मध्ये चला जिथे आपण [image generation applications कसे तयार करायचे](../09-building-image-applications/README.md?WT.mc_id=academic-105485-koreyst) ते पाहणार आहोत!

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.