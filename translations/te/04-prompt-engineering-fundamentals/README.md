# ప్రాంప్ట్ ఇంజనీరింగ్ మూలాధారాలు

[![Prompt Engineering Fundamentals](../../../translated_images/te/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## పరిచయం
ఈ మాడ్యూల్ జనరేటివ్ ఏఐ మోడల్స్‌లో సమర్థవంతమైన ప్రాంప్ట్‌లను రూపొందించడానికి అవసరమైన ముఖ్యమైన ধারণలు మరియు సాంకేతికతలను కవర్ చేస్తుంది. మీరు LLM కి మీరు రాసే ప్రాంప్ట్ కూడా ముఖ్యం. జాగ్రత్తగా రూపొందించిన ప్రాంప్ట్ మెరుగైన ప్రతిస్పందన నాణ్యతను సాధించగలదు. కానీ _ప్రాంప్ట్_ మరియు _ప్రాంప్ట్ ఇంజనీరింగ్_ వంటి పదాలు అర్థం ఏమిటి? నేను LLM కి పంపే ప్రాంప్ట్ _ఇన్‌పుట్_ ను ఎలా మెరుగుపరచగలను? ఈ అధ్యాయంలో మరియు తదుపరి అధ్యాయం లో మనం ఈ ప్రశ్నలకు సమాధానాలు కనుగొనడానికి ప్రయత్నిస్తాము.

_జనరేటివ్ ఏఐ_ వినియోగదారుల అభ్యర్థనలకు ప్రతిస్పందిస్తూ కొత్త కంటెంట్‌ను (ఉదా: టెక్స్ట్, చిత్రాలు, ఆడియో, కోడ్ మొదలయినవి) సృష్టించగలదు. ఇది OpenAI యొక్క GPT ("Generative Pre-trained Transformer") లాంటి _లార్జ్ లాంగ్వేజ్ మోడల్స్_ ఉపయోగించి సాధ్యమవుతుంది, ఇవి సహజ భాష మరియు కోడ్ కోసం శిక్షణ పొందినవి.

వినియోగదారులు ఇప్పుడు చాట్ వంటి పరిచయం ఉన్న విధానాల ద్వారా ఈ మోడల్స్‌తో ఇంటరాక్ట్ చేయవచ్చు, ప్రత్యేక సాంకేతిక నైపుణ్యాలు లేకుండా. ఈ మోడల్స్ _ప్రాంప్ట్ ఆధారిత_ అవి - వినియోగదారులు ఒక టెక్స్ట్ ఇన్‌పుట్ (ప్రాంప్ట్) పంపించి AI ప్రతిస్పందన (కంప్లీషన్) పొందుతారు. వారు ఆ తర్వాత దశల వారీగా "AIతో చాట్" చేసి, తమ ప్రాంప్ట్‌ను మెరుగుపరిచి, ప్రతిస్పందన ఆశించినట్లుగా సాధిస్తారు.

"ప్రాంప్ట్‌లు" ఇప్పుడు జనరేటివ్ AI యాప్ల కోసం ప్రధాన _ప్రోగ్రామింగ్ ఇన్టర్‌ఫేస్_ గా మారాయి, మోడల్స్‌కు ఏమి చేయాలో చెప్పడం మరియు హాజరైన ప్రతిస్పందన నాణ్యతపై ప్రభావం చూపడం. "ప్రాంప్ట్ ఇంజనీరింగ్" అనేది వేగంగా పెరుగుతున్న అధ్యయన రంగం, ఇది ప్రాంప్ట్‌లను _డిజైన్_ చేసి, మెరుగుపరచడంపై కేంద్రీకృతమై ఉంది, తద్వారా నిరంతరం మరియు నాణ్యమైన ప్రతిస్పందనలను వడపోత చేయగలుగుతుంది.

## నేర్చుకునే లక్ష్యాలు

ఈ పాఠంలో, ప్రాంప్ట్ ఇంజనీరింగ్ అంటే ఏమిటి, ఇది ఎందుకు ముఖ్యం, మరియు ఒక ప్రత్యేక మోడల్ మరియు యాప్ లక్ష్యం కోసం సమర్థవంతమైన ప్రాంప్ట్‌లను ఎలా రూపొందించాలో నేర్చుకుంటాము. ప్రాంప్ట్ ఇంజనీరింగ్ యొక్క ప్రాథమిక భావనలు మరియు ఉత్తమ ఆచరణలను అర్థం చేసుకుని, జూపిటర్ నోట్‌బుక్ "సాండ్‌బాక్స్" వాతావరణంలో ఈ భావనలను నిజమైన ఉదాహరణలకు అన్వయించవచ్చు.

ఈ పాఠం చివరిలో మేము చేయగలవు:

1. ప్రాంప్ట్ ఇంజనీరింగ్ అంటే ఏంటి మరియు ఇది ఎందుకు ముఖ్యం అనేది వివరిస్తాము.
2. ఒక ప్రాంప్ట్ యొక్క భాగాలను మరియు వాటి ఉపయోగాన్ని వివరించడము.
3. ప్రాంప్ట్ ఇంజనీరింగ్ కోసం ఉత్తమ ఆచరణలు మరియు సాంకేతికతలను నేర్చుకోవడం.
4. నేర్చుకున్న సాంకేతికతలను నిజమైన ఉదాహరణలకు, OpenAI ఎండ్పాయింట్ ఉపయోగించి వర్తించడం.

## కీలక పదాలు

ప్రాంప్ట్ ఇంజనీరింగ్: AI మోడల్స్‌ను కోరుకున్న అవుట్పుట్‌లను ఉత్పత్తి చేయడానికి మార్గనిర్దేశం చేయడానికి ఇన్‌పుట్‌లను రూపొందించి మెరుగుపరచడం.

టోకెనైజేషన్: టెక్స్ట్‌ను చిన్న యూనిట్లుగా మార్చే ప్రక్రియ, టోకెన్స్ అని పిలవబడును, ఇవి మోడల్ అర్థం చేసుకోగలిగే మరియు ప్రాసెస్ చేయగలిగే యూనిట్లు.

ఇన్‌స్ట్రక్షన్-ట్యూన్ చేసిన LLMs: నిర్దిష్ట సూత్రాలతో మెరుగుపరచబడ్డ లార్జ్ లాంగ్వేజ్ మోడల్స్ (LLMs) ఈ మోడల్స్ వారి ప్రతిస్పందన ఖచ్చితత్వం మరియు సంబంధితతను పెంచుతాయి.

## నేర్చుకునే సాండ్‌బాక్స్

ప్రాంతీయంగా ప్రాంప్ట్ ఇంజనీరింగ్ ప్రస్తుతం శాస్త్రం కంటే ఒక కళగా ఉంటుంది. దీనిపై మన intuఐషన్ మెరుగు పరుచుకోవడానికి ఉత్తమ మార్గం _ఇంకొన్ని సార్లు ప్రాక్టీస్ చేయడం_ మరియు ప్రయోగాత్మక విధానాన్ని అన్నింటినీ అన్వయించాలని ఉంది, దానికి అనువైన అనువర్తన డొమైను నైపుణ్యం మరియు సిఫారసు చేయబడిన సాంకేతికతలు మరియు మోడల్-ప్రత్యేక ఆప్టిమైజేషన్లను కలిపితే.

ఈ పాఠానికి అనుబంధంగా ఇచ్చిన జూపిటర్ నోట్‌బుక్ ఒక _సాండ్‌బాక్స్_ వాతావరణాన్ని అందిస్తుంది, ఇది మీరు నేర్చుకునే విషయాలను పాటిస్తూ, లేదా చివరన ఉన్న కోడ్ సవాలులో భాగంగా ప్రయత్నించి చూడవచ్చు. వ్యాయామాలు అమలు చేయడానికి మీరు కావలసినవి:

1. **ఏజ్యూర్ OpenAI API కీ** - ప్రజెంటెడ్ LLM కోసం సర్వీస్ ఎండ్పాయింట్.
2. **పైథాన్ రన్‌టైం** - ఇందులో నోట్‌బుక్ నడుపవచ్చు.
3. **లోకల్ Env వేరియబుల్స్** - ఇప్పుడు [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) దశలను పూర్తి చేయండి.

నోట్‌బుక్ ప్రారంభ వ్యాయామాలతో వస్తుంది - కానీ మీరు మీ స్వంత _మార్క్డౌన్_ (వివరణ) మరియు _కోడ్_ (ప్రాంప్ట్ అభ్యర్థనల) సెక్షన్లను జోడించి మరిన్ని ఉదాహరణలు లేదా ఆలోచనలను ప్రయత్నించడానికి ప్రోత్సహించబడుతున్నారు - మరియు ప్రాంప్ట్ రూపకల్పనకు మీ intuఐషన్‌ను మరింత పెంచుకోండి.

## చిత్రణాత్మక మార్గదర్శకము

ఈ పాఠం ఏ అంశాలను కవర్ చేస్తుందో పెద్ద దృశ్యాన్ని ముందుగా గుర్తించాలనుకుంటున్నారా? ఈ చిత్రణాత్మక గైడ్ మీకు ప్రధాన విషయాలు మరియు ప్రతి ఒక్కటిలో మీరు ఆలోచించాల్సిన కీలక ఎంపికలను తెలియజేస్తుంది. పాఠం రోడ్‌మ్యాప్ మీరు ప్రాథమిక భావనలు మరియు సవాళ్ళను అర్థం చేసుకుని వాటిని సంబంధిత ప్రాంప్ట్ ఇంజనీరింగ్ సాంకేతికతలు మరియు ఉత్తమ ఆచరణలతో పరిష్కరించిన విధానం చూపిస్తుంది. గమనించండి, ఈ మార్గదర్శకంలో "అధునాతన సాంకేతికతలు" విభాగం ఈ పాఠ్యક્રમం యొక్క _తదుపరి_ అధ్యాయంలో కవర్ అయ్యే విషయాలకు సూచనగా ఉంటుంది.

![Illustrated Guide to Prompt Engineering](../../../translated_images/te/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## మా స్టార్టప్

ఇప్పుడు, _ఈ విషయం_ మా స్టార్టప్ మిషన్‌కు సంబంధించి ఎలా ఉండిందో మాట్లాడుకుందాం, అది [ఏఐ ఇన్నోవేషన్‌ను విద్యార్థులకు తీసుకురావడం](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst) పై ఉంది. మేము _వ్యక్తిగతీకరిన నేర్పుదల_కి ఏఐ ఆధారిత యాప్‌లను నిర్మించాలని చూస్తున్నాం - కాబట్టి మా యాప్ వివిధ వినియోగదారులు ఎలా "ప్రాంప్ట్‌లు" ని "డిజైన్" చేస్తారో ఆలోచిద్దాం:

- **అడ్మినిస్ట్రేటర్లు** ఏఐని _పాఠ్యప్రమాణాల డేటాను విశ్లేషించి కవరేజీ లో కోలాపడిన பகுதியில் గుర్తించును_ అని అడగవచ్చు. ఏఐ ఫలితాలను సారాంశం చేస్తుంది లేదా కోడ్‌తో దృశ్యీకరణ చేస్తుంది.
- **బోధకులు** ఏఐని లక్ష్య ప్రేక్షకులు మరియు అంశం కోసం _పాఠ్య ప్రణాళికను సృష్టించు_ అని అడగవచ్చు. ఏఐ వ్యక్తిగతీకరించిన ప్రణాళికను ప్రత్యేక రూపంలో రూపొందిస్తుంది.
- **విద్యార్థులు** ఏఐని _కష్టమైన విషయాలలో వారిని శిక్షణ ఇస్తూ_ అడగవచ్చు. ఏఐ ఇప్పుడు వారిని వారిది స్థాయికి తగిన పాఠాలు, సూచనలు మరియు ఉదాహరణలతో మార్గనిర్దేశం చేస్తుంది.

ఇది కేవలం మొదటి దశ మాత్రమే. [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) చూడండి - విద్యా నిపుణులు రూపొందించిన ఓపెన్-సోర్సు ప్రాంప్ట్‌ల గ్రంధాలయం - మీరు అవకాశాల గురించి విస్తృత అవగాహన పొందగలుగుతారు! _ఆ ప్రాంప్ట్‌లను సాండ్‌బాక్స్‌లో చూడండి లేదా OpenAI ప్లేగ్రౌండ్లో ప్రయోగించి ఫలితాలను చూడండి!_

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #1:
Prompt Engineering.
Define it and explain why it is needed.
-->

## ప్రాంప్ట్ ఇంజనీరింగ్ అంటే ఏమిటి?

మేము ఈ పాఠాన్ని ప్రారంభించి చెప్పాము **ప్రాంప్ట్ ఇంజనీరింగ్** అంటే ఏమిటంటే ఒక నిర్దిష్ట యాప్ లక్ష్యానికి మరియు మోడల్‌కు సరిపోయే స్థిరమైన మరియు నాణ్యమైన ప్రతిస్పందనలను (కంప్లీషన్స్) అందించేందుకు టెక్స్ట్ ఇన్‌పుట్‌లను (ప్రాంప్ట్‌లు) _డిజైన్_ చేసి, మెరుగుపరచే ప్రక్రియ అని. దీనిని రెండు దశల ప్రక్రియగా పరిగణించవచ్చు:

- ఒక నిర్దిష్ట మోడల్ మరియు లక్ష్యానికి ప్రాథమిక ప్రాంప్ట్‌ను _డిజైన్_ చేయడం
- ప్రాంప్ట్‌ను దశల వారీగా _మెరుగుపరచడం_, ప్రతిస్పందన నాణ్యతను పెంచడం

ఇది తప్పనిసరి గా ప్రయోగాత్మక మరియు తప్పులు సరిదిద్దుకునే ప్రక్రియ, మంచి ఫలితాల కోసం వినియోగదారు intuఐషన్ మరియు ప్రయత్నం అవసరం. కాబట్టి ఇది ఎందుకు ముఖ్యం? ఆ ప్రశ్నకు సమాధానం ఇవ్వడానికి, మనం ముందుగా మూడు భావనలు అర్థం చేసుకోవాలి:

- _టోకెనైజేషన్_ = మోడల్ ప్రాంప్ట్‌ను "ఎలా చూస్తుంది"
- _బేస్ LLMs_ = స్థాపనా మోడల్ ప్రాంప్ట్‌ను "ఎలా ప్రాసెస్ చేస్తుంది"
- _ఇన్‌స్ట్రక్షన్-ట్యూన్ LLMs_ = మోడల్ ఇప్పుడు "పనులను" ఎలా చూడగలదు

### టోకెనైజేషన్

ఒక LLM ఒక ప్రాంప్ట్‌ను _టోకెన్ల వరుసగా_ చూస్తుంది, విభిన్న మోడల్స్ (లేదా ఒక మోడల్ పలు వర్షన్లు) ఒకే ప్రాంప్ట్‌ను వేరే విధంగా టోకెనైజ్ చేయవచ్చు. LLM‌లు టోకెన్లపై శిక్షణ పొందినవగా (కాకుండా రా టెక్స్ట్ పై కాదు), ప్రాంప్ట్‌లు ఎలా టోకెనైజ్ అవుతాయో ఆ ప్రయాణం ఉత్పత్తి ఫలిత నాణ్యతపై ప్రత్యక్ష ప్రభావం ఉంటుంది.

టోకెనైజేషన్ ఎలా పనిచేస్తుందో intuఐషన్ పొందడానికి, దిగువ చూపిన [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) వంటి టూల్‌లను ప్రయత్నించండి. మీ ప్రాంప్ట్‌ను కాపీ చేసి - అది టోకెన్లగా ఎలా మార్చబడుతుందో చూడండి, స్పేస్ క్యారెక్టర్లు మరియు పంక్చ్యుయేషన్ మార్కులు ఎలా పరిగణించబడుతున్నాయో కూడా గమనించండి. ఈ ఉదాహరణ ఒక పాత LLM (GPT-3) చూపిస్తోంది - కాబట్టి కొత్త మోడల్‌తో ప్రయత్నిస్తే వేరే ఫలితం రావచ్చు.

![Tokenization](../../../translated_images/te/04-tokenizer-example.e71f0a0f70356c5c.webp)

### భావన: స్థాపనా మోడల్స్

ప్రాంప్ట్ టోకెనైజ్ అయిన తర్వాత, ["బేస్ LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (లేదా స్థాపనా మోడల్) యొక్క ప్రాధమిక విధానం ఆ వరుసలో తదుపరి టోకెన్‌ను ఊహించడం. LLM‌లు ఫిర్యాదు పదాలకు శిక్షణ పొందిన విధంగా, టోకెన్ల మధ్య సాంఖ్యిక సంబంధాలను బాగా తెలుసుకుని, కొంత విశ్వాసంతో అది ఊహించగలవు. వారు ప్రాంప్ట్ లేదా టోకెన్‌లో మాటల అర్థాన్ని అర్థం చేసుకోరు; వారు కేవలం ఒక నమూనాను ఉంచి, తదుపరి ఊహించగలరు. వారు వినియోగదారు జోక్యం లేదా ముందుగా నిర్ణయించబడిన నిబంధన మేరకు ఆ వరుసను కొనసాగించవచ్చు.

ప్రాంప్ట్ ఆధారిత కంప్లీషన్ ఎలా పనిచేస్తుందో చూడాలనుకుంటున్నారా? పై ప్రాంప్ట్‌ను ఏజ్యూర్ OpenAI స్టూడియో [_చాట్ ప్లేగ్రౌండ్_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) లో డిఫాల్ట్ సెట్టింగ్స్ తో ఎంటర్ చేయండి. ఈ సిస్టమ్ ప్రాంప్ట్‌లను సమాచార అభ్యర్థనలు గా తీసుకుందంటే మీరు ఈ సందర్భానికి సరిపోయే కంప్లీషన్ స్వీకరిస్తారు.

కానీ వాడుకరికి ఏదైనా ప్రత్యేకమైన, నిర్దిష్ట లక్ష్యానుసారమైన అంశం చూడాలనుకుంటే? అప్పుడు _ఇన్‌స్ట్రక్షన్-ట్యూన్_ చేసిన LLMలు చిత్రంలోకి వస్తాయి.

![Base LLM Chat Completion](../../../translated_images/te/04-playground-chat-base.65b76fcfde0caa67.webp)

### భావన: ఇన్‌స్ట్రక్షన్-ట్యూన్ LLMs

[ఇన్‌స్ట్రక్షన్-ట్యూన్ LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) స్థాపనా మోడల్ తీసుకొని, స్పష్టమైన సూచనలు కలిగిన ఉదాహరణలు లేదా ఇన్‌పుట్/ఔట్‌పుట్ జంటలతో (ఉదా: బహు-తిరుగుడు "సందేశాలు") దానిని మెరుగుపరుస్తుంది - AI స్ఫూర్తి వాటిని అనుసరించేలా ప్రతిస్పందన అందించే ప్రయత్నం చేస్తుంది.

ఇది మానవ అభిప్రాయం తో రీఇన్ఫోర్స్‌మెంట్ లెర్నింగ్ (RLHF) వంటి సాంకేతికతలు ఉపయోగిస్తుంది, మోడల్‌ను _సూచనలు అనుసరించేందుకు_ మరియు _అభిప్రాయాల నుంచి నేర్చుకోవడానికి_ శిక్షణ ఇస్తుంది. అందుచేత ఇది ప్రాక్టికల్ అనువర్తనాలకు మరింత సరిపోయే మరియు వినియోగదారు లక్ష్యాలకు సమన్వయం చేయగలిగే ప్రతిస్పందనలను సృష్టిస్తుంది.

ప్రయత్నించండి - పై ప్రాంప్ట్‌కు తిరిగి వెళ్లి, ఇప్పుడు విడుదల సందేశాన్ని క్రింది సూచనగా ఇస్తే: 

> _మీకు అందించిన కంటెంట్‌ను రెండవ తరగతి విద్యార్థికి సారాంశం చేయండి. ఫలితాన్ని ఒక ప్యారాగ్రాఫ్‌లో 3-5 బుల్లెట్ పాయింట్లలో ఉంచండి._

ఫలితం ఇప్పుడు కావలసిన లక్ష్యానికి మరియు ఫార్మాట్‌కు తగినట్టు ఎలా మార్చబడిందో చూడండి? ఒక బోధకుడు ఈ ప్రతిస్పందనని వారి తరగతి స్లైడ్ల కోసం నేరుగా ఉపయోగించవచ్చు.

![Instruction Tuned LLM Chat Completion](../../../translated_images/te/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## ప్రాంప్ట్ ఇంజనీరింగ్ ఎందుకు అవసరం?

ఇప్పుడిప్పుడు మనం ప్రాంప్ట్‌లు LLMలచే ఎలా ప్రాసెస్ అవుతున్నాయో తెలుసుకున్నాము, ఇప్పుడు మనం ప్రాంప్ట్ ఇంజనీరింగ్ ఎందుకు అవసరమని చర్చిద్దాం. సమాధానం: ప్రస్తుత LLMలు కొన్ని సవాళ్ళను ఎదుర్కొంటున్నారు, ఇవి _నమ్మదగిన మరియు స్థిరమైన కంప్లీషన్స్_ పొందుగాక సవాలుగా ఉంటాయి, అందుకే ప్రాంప్ట్ నిర్మాణం మరియు ఆప్టిమైజేషన్ పై శ్రద్ద పెట్టాలి. ఉదాహరణకు:

1. **మోడల్ ప్రతిస్పందనలు స్టోకస్టిక్.** _ఒకే ప్రాంప్ట్_ విందేమోడల్స్ లేదా మోడల్ వర్షన్లతో వేరు వేరు ఫలితాలు ఇస్తుంది. అదే మోడల్ తో కూడా వేరు సమయాల్లో వేరు ఫలితాలు రావచ్చు. _ప్రాంప్ట్ ఇంజనీరింగ్ సాంకేతికతలు ఈ మార్పులను తగ్గించడానికి మెరుగైన రక్షణలను అందిస్తాయి_.

1. **మోడల్స్ కురూపమైన సమాచారం సృష్టించగలవు.** మోడల్స్ _పెద్ద కానీ పరిమిత_ డేటాసెట్‌లపై శిక్షణ పొందినవని అర్థం, కాబట్టి శిక్షణ విస్తృతికి బయటి భావనల గురించి అవగాహన లేకపోవచ్చు. దాంతో, వారు తప్పుగా, కల్పితంగా లేదా నిజాలకు విరుద్ధంగా ఉన్న ఫలితాలను ఇవ్వవచ్చు. _ప్రాంప్ట్ ఇంజనీరింగ్ సాంకేతికతలు ఈ రకాల కల్పనలు గుర్తించి, అడిగి AI మన శ్రేయస్సుకు సారంగం ఇవ్వడానికి సహాయపడతాయి_.

1. **మోడల్స్ సామర్థ్యాలు మారుతూనే ఉంటాయి.** కొత్త లేదా తదుపరి తరహా మోడల్స్ మరింత శక్తివంతమైనవే కానీ ప్రత్యేకమైన చికాకులు మరియు వ్యయ, సంక్లిష్టతలో ఒప్పందాలనూ తీసుకురావచ్చు. _ప్రాంప్ట్ ఇంజనీరింగ్ ఉత్తమ ఆచరణలను అభివృద్ధి చేసి, విస్తారమైన, సున్నితమైన మార్గాల్లో మోడల్-ప్రత్యేక అవసరాలకు అనువుదల కల్పించవచ్చు_.

ఈ వ్యవహారాన్ని OpenAI లేదా Azure OpenAI ప్లేగ్రౌండ్‌లో చూడండి:

- వేర్వేరు LLM డిప్లాయ్‌మెంట్‌ల (ఉదా: OpenAI, Azure OpenAI, Hugging Face) తో ఒకే ప్రాంప్ట్ ఉపయోగించండి - మీరు మార్పులను గమనించారా?
- ఒకే LLM డిప్లాయ్‌మెంట్ (ఉదా: Azure OpenAI ప్లేగ్రౌండ్)లో ఒక్కోసారి ఒకే ప్రాంప్ట్ ఉపయోగించండి - ఈ మార్పులు ఎలా భిన్నంగా ఉంటాయని చూశారు?

### కల్పనలు (Fabrications) ఉదాహరణ

ఈ కోర్సులో, మేము **"కల్పన"** అనే పదాన్ని ఉపయోగిస్తాము, దీని అర్థం LLMలు అప్పుడప్పుడు శిక్షణ పరిమితులు లేదా ఇతర కారణాల వల్ల గమనార్హంగా తప్పు సమాచారం ఉత్పత్తి చేసే పరిణామం. మీరు సాధారణ వ్యాసాలు లేదా పరిశోధనా పత్రాల్లో దీనిని _"హల్యూసినేషన్లు"_ అనే పదంతో వినవచ్చును. కానీ మేము _"కల్పన"_ పదాన్ని ఉపయోగించాలని గట్టిగా సిఫారసు చేస్తున్నాము, ఇది యంత్రం ఉత్పత్తి చేసిన ఫలితానికి మానవుషుల లక్షణాన్ని తప్పుగా ఒప్పించకుండా ఉంటుంది. ఇది [జవాబుదారిత్వం ఉన్న AI మార్గదర్శకాలు](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) ను బలపరిచే విషయంగా ఉంటుంది, కొన్ని సందర్భాల్లో మానవులకు అందని లేదా అసవధాన పదాలను తొలగిస్తుంది.

కల్పన ఎలా పని చేస్తుందో అర్థం చేసుకుందామా? AIని మన శిక్షణ డేటాసెట్‌లో లేకపోయే ఒక లేన్‌పై కంటెంట్ ఉత్పత్తి చేయమని సూచించే ప్రాంప్ట్ గురించి ఆలోచించండి. ఉదాహరణకి - నేను ఈ ప్రాంప్ట్‌ను ప్రయత్నించాను:

> **ప్రాంప్ట్:** 2076 లో మరిషియన్ యుద్ధంపై ఒక పాఠ్య ప్రణాళికను సృష్టించు.
A web search showed me that there were fictional accounts (e.g., television series or books) on Martian wars - but none in 2076. Commonsense also tells us that 2076 is _in the future_ and thus, cannot be associated with a real event.

So what happens when we run this prompt with different LLM providers?

> **Response 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/te/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Response 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/te/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Response 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/te/04-fabrication-huggingchat.faf82a0a51278956.webp)

As expected, each model (or model version) produces slightly different responses thanks to stochastic behavior and model capability variations. For instance, one model targets an 8th grade audience while the other assumes a high-school student. But all three models did generate responses that could convince an uninformed user that the event was real.

Prompt engineering techniques like _metaprompting_ and _temperature configuration_ may reduce model fabrications to some extent. New prompt engineering _architectures_ also incorporate new tools and techniques seamlessly into the prompt flow, to mitigate or reduce some of these effects.

## Case Study: GitHub Copilot

Let's wrap this section by getting a sense of how prompt engineering is used in real-world solutions by looking at one Case Study: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot is your "AI Pair Programmer" - it converts text prompts into code completions and is integrated into your development environment (e.g., Visual Studio Code) for a seamless user experience. As documented in the series of blogs below, the earliest version was based on the OpenAI Codex model - with engineers quickly realizing the need to fine-tune the model and develop better prompt engineering techniques, to improve code quality. In July, they [debuted an improved AI model that goes beyond Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) for even faster suggestions.

Read the posts in order, to follow their learning journey.

- **May 2023** | [GitHub Copilot is Getting Better at Understanding Your Code](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **May 2023** | [Inside GitHub: Working with the LLMs behind GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jun 2023** | [How to write better prompts for GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jul 2023** | [.. GitHub Copilot goes beyond Codex with improved AI model](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [A Developer's Guide to Prompt Engineering and LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [How to build an enterprise LLM app: Lessons from GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

You can also browse their [Engineering blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) for more posts like [this one](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) that shows how these models and techniques are _applied_ for driving real-world applications.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #2.
Reinforce the concept with examples and references.

CONCEPT #2:
Prompt Design.
Illustrated with examples.
-->

## Prompt Construction

We've seen why prompt engineering is important - now let's understand how prompts are _constructed_ so we can evaluate different techniques for more effective prompt design.

### Basic Prompt

Let's start with the basic prompt: a text input sent to the model with no other context. Here's an example - when we send the first few words of the US national anthem to the OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) it instantly _completes_ the response with the next few lines, illustrating the basic prediction behavior.

| Prompt (Input)     | Completion (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | It sounds like you're starting the lyrics to "The Star-Spangled Banner," the national anthem of the United States. The full lyrics are ... |

### Complex Prompt

Now let's add context and instructions to that basic prompt. The [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) lets us construct a complex prompt as a collection of _messages_ with:

- Input/output pairs reflecting _user_ input and _assistant_ response.
- System message setting the context for assistant behavior or personality.

The request is now in the form below, where the _tokenization_ effectively captures relevant information from context and conversation. Now, changing the system context can be as impactful on the quality of completions, as the user inputs provided.

```python
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Instruction Prompt

In the above examples, the user prompt was a simple text query that can be interpreted as a request for information. With _instruction_ prompts, we can use that text to specify a task in more detail, providing better guidance to the AI. Here's an example:

| Prompt (Input)                                                                                                                                                                                                                         | Completion (Output)                                                                                                        | Instruction Type    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Write a description of the Civil War                                                                                                                                                                                                   | _returned a simple paragraph_                                                                                              | Simple              |
| Write a description of the Civil War. Provide key dates and events and describe their significance                                                                                                                                     | _returned a paragraph followed by a list of key event dates with descriptions_                                             | Complex             |
| Write a description of the Civil War in 1 paragraph. Provide 3 bullet points with key dates and their significance. Provide 3 more bullet points with key historical figures and their contributions. Return the output as a JSON file | _returns more extensive details in a text box, formatted as JSON that you can copy-paste to a file and validate as needed_ | Complex. Formatted. |

## Primary Content

In the above examples, the prompt was still fairly open-ended, allowing the LLM to decide what part of its pre-trained dataset was relevant. With the _primary content_ design pattern, the input text is divided into two parts:

- an instruction (action)
- relevant content (that influences action)

Here's an example where the instruction is to "summarize this in 2 sentences".

| Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completion (Output)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus. <br/> **Summarize this in 2 short sentences** | Jupiter, the fifth planet from the Sun, is the largest in the Solar System and is known for being one of the brightest objects in the night sky. Named after the Roman god Jupiter, it's a gas giant whose mass is two-and-a-half times that of all other planets in the Solar System combined. |

The primary content segment can be used in various ways to drive more effective instructions:

- **Examples** - instead of telling the model what to do with an explicit instruction, give it examples of what to do and let it infer the pattern.
- **Cues** - follow the instruction with a "cue" that primes the completion, guiding the model towards more relevant responses.
- **Templates** - these are repeatable 'recipes' for prompts with placeholders (variables) that can be customized with data for specific use cases.

Let's explore these in action.

### Using Examples

This is an approach where you use the primary content to "feed the model" some examples of the desired output for a given instruction, and let it infer the pattern for the desired output. Based on the number of examples provided, we can have zero-shot prompting, one-shot prompting, few-shot prompting etc.

The prompt now consists of three components:

- A task description
- A few examples of the desired output
- The start of a new example (which becomes an implicit task description)

| Learning Type | Prompt (Input)                                                                                                                                        | Completion (Output)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "The Sun is Shining". Translate to Spanish                                                                                                            | "El Sol está brillando".    |
| One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot      | The player ran the bases => Baseball <br/> The player hit an ace => Tennis <br/> The player hit a six => Cricket <br/> The player made a slam-dunk => | Basketball                  |
|               |                                                                                                                                                       |                             |

Note how we had to provide explicit instruction ("Translate to Spanish") in zero-shot prompting, but it gets inferred in the one-shot prompting example. The few-shot example shows how adding more examples allows models to make more accurate inferences with no added instructions.

### Prompt Cues

Another technique for using primary content is to provide _cues_ rather than examples. In this case, we are giving the model a nudge in the right direction by _starting it off_ with a snippet that reflects the desired response format. The model then "takes the cue" to continue in that vein.

| Number of Cues | Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completion (Output)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. <br/>**Summarize This**                                       | Jupiter is the largest planet in our Solar System and the fifth one from the Sun. It is a gas giant with a mass 1/1000th of the Sun's, but it is heavier than all the other planets combined. Ancient civilizations have known about Jupiter for a long time, and it is easily visible in the night sky.. |
| 1              | బుధుడు సూర్యుని నుండి ఐదవ గ్రహం మరియు సౌర వ్యవస్థలో అతిపెద్ద గ్రహం. ఇది గ్యాస్ మహా గ్రహం, దాని బలం సూర్య బలం పైన వందవ భాగం అయినప్పటికీ, అన్ని ఇతర గ్రహాల బలం కలిపితే రెండిరెట్టు మింపుగా ఉంటుంది. బుధుడు రాత్రి ఆకాశంలో కనబడే అత్యుత్తమ వస్తువులలో ఒకటి మరియు ప్రాచీన నాగరికతలకు చరిత్ర రికార్డింగ్‌కు ముందు నుండి తెలుసుకోవబడింది. <br/>**దీనిని సంగ్రహించండి** <br/> మనం నేర్చుకున్నది ఏమిటంటే బుధుడు | సూర్యుని నుండి ఐదవ గ్రహం మరియు సౌర వ్యవస్థలో అతిపెద్ద గ్రహం. ఇది గ్యాస్ మహా గ్రహం, దాని బలం సూర్య బలం పైన వందవ భాగం అయినప్పటికీ, అన్ని ఇతర గ్రహాల బలం కలిపితే రెండిరెట్టు మింపుగా ఉంటుంది. ఇది సులభంగా కనపడుతుంది మరియు ప్రాచీన కాలంనుండి తెలుసుకున్నారు.                        |
| 2              | బుధుడు సూర్యుని నుండి ఐదవ గ్రహం మరియు సౌర వ్యవస్థలో అతిపెద్ద గ్రహం. ఇది గ్యాస్ మహా గ్రహం, దాని బలం సూర్య బలం పైన వందవ భాగం అయినప్పటికీ, అన్ని ఇతర గ్రహాల బలం కలిపితే రెండిరెట్టు మింపుగా ఉంటుంది. బుధుడు రాత్రి ఆకాశంలో కనబడే అత్యుత్తమ వస్తువులలో ఒకటి మరియు ప్రాచీన నాగరికతలకు చరిత్ర రికార్డింగ్‌కు ముందు నుండి తెలుసుకోవబడింది. <br/>**దీనిని సంగ్రహించండి** <br/> మేము నేర్చుకున్న టాప్ 3 విషయాలు:         | 1. బుధుడు సూర్యుని నుండి ఐదవ గ్రహం మరియు సౌర వ్యవస్థలో అతిపెద్ద గ్రహం. <br/> 2. ఇది గ్యాస్ మహా గ్రహం మరియు దాని బలం సూర్య బలం వందవ భాగం ...<br/> 3. బుధుడు ప్రాథమిక కన్నుతో కనిపించేలా ప్రాచీన కాలంనుండి తెలుసుకున్నారు ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### ప్రాంప్ట్ టెంప్లేట్లు

ఒక ప్రాంప్ట్ టెంప్లేట్ అనేది అవసరంపై ఆధారపడి దాన్ని దాచిపెట్టి అవసరమైనప్పుడు పునఃవినియోగించడానికి ఉపయోగించే _ముందుగా నిర్వచించిన ప్రాంప్ట్ రెసిపీ_. ఇది అత్యంత సాధారణ రూపంలో, <a href="https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst">OpenAI నుండి ఈ ఉదాహరణ</a> వంటి ప్రాంప్ట్ ఉదాహరణల సేకరణ మాత్రమే, దీని ద్వారా ఇంటరాక్టివ్ ప్రాంప్ట్ భాగాలు (వాడుకరి మరియు సిస్టమ్ సందేశాలుగా) మరియు API-ప్రేరేపిత అభ్యర్థన ఫార్మాట్ రెండు అందుబాటులో ఉంటాయి - పునఃవినియోగానికి మద్దతు ఇవ్వడానికి.

ఇది మరింత సంక్లిష్ట రూపంలో, <a href="https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst">LangChain నుండి ఈ ఉదాహరణ</a> లాంటి వాటిలో, డేటాను ఉపయోగించి ప్రాంప్ట్‌ను డైనమిక్గా రూపొం చేయడానికి వివిధ వనరుల (వాడుకరి ఇన్పుట్, సిస్టమ్ సందర్భం, బాహ్య డేటా వనరులు) నుండి ప్రాప్తించదగిన _ప్లేస్‌హోల్డర్లు_ ఉంటాయి. ఇది మాకు పునఃవినియోగించే ప్రాంప్ట్‌ల లైబ్రరీని సృష్టించి, స్థాయిలో అనుకూల అనుభవాలను **ప్రోగ్రామేటిక్గా** నడిపించేందుకు సహాయపడుతోంది.

చివరగా, ఫలిత రూపంలో టెంప్లేట్ల నిజమైన విలువ వెర్టికల్ అప్లికేషన్ డొమైన్‌ల కోసం _ప్రాంప్ట్ లైబ్రరీలు_ సృష్టించడం మరియు ప్రచురించడం జరిగేటప్పుడు ఉంటుంది - అప్పుడు ప్రాంప్ట్ టెంప్లేట్ ఇప్పుడు ఆ అప్లికేషన్-స్పెసిఫిక్ సందర్భం లేదా ఉదాహరణలను ప్రతిబింబిస్తుంది, ఇది లక్ష్యంగా పెట్టుకొన్న వాడుకరి ప్రేక్షకుల కొరకు సమాధానాలను ఎక్కువ ప్రామాణికంగా మరియు సరిగా చేస్తుంది. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) రిపోసిటరీ ఈ విధానానికి గొప్ప ఉదాహరణ, విద్యావంతమైన డొమైన్ కోసం ప్రాంప్ట్‌ల లైబ్రరీని సేకరిస్తుంది, ముఖ్యమైన లక్ష్యాలకు అధిక ప్రాధాన్యతతో వంటి పాఠ్య ప్రణాళిక, పాఠ్య విధానం రూపకల్పన, విద్యార్థి మార్గదర్శనం మొదలైనవి.

## మద్దతు ఇవ్వే కంటెంట్

ప్రాంప్ట్ నిర్మాణానికి ఒక సూచన (పని) మరియు లక్ష్య (ప్రధాన కంటెంట్) ఉన్నప్పటికి, _సహాయక కంటెంట్_ అనేది ఫలితాన్ని **ఎటువంటి విధంగా ప్రభావితం చేసే అదనపు సందర్భం** లాగా ఉంటుంది. ఇది ట్యూనింగ్ పారామితులు, ఆకృతి సూచనలు, అంశ వర్గీಕರಣలు మొదలైనవి ఉండవచ్చు, ఇవి మోడల్‌ని యూజర్ లక్ష్యాల లేదా ఆశనలకు అనుగుణంగా సమాధానం ఇవ్వడానికి సహాయపడతాయి.

ఉదాహరణకు: ఒక కోర్సు క్యాటలాగ్‌లో విస్తృత మెటాడేటాతో (పేరు, వివరణ, స్థాయి, మెటాడేటా ట్యాగ్లు, ఉపాధ్యాయుడు మొదలైనవి) అందుబాటులో ఉన్న అన్ని కోర్సులకు:

- "Fall 2023 కోర్సుల కేటలాగ్ సంగ్రహము" అనే సూచనను నిర్వచించవచ్చు
- కొంత ఉదాహరణగా కావలసిన అవుట్పుట్ను ఇవ్వడానికి ప్రధాన కంటెంట్‌ను ఉపయోగించవచ్చు
- ఆసక్తికరమైన ట్యాగ్లలో టాప్ 5 ని గుర్తించడానికి సహాయక కంటెంట్ ను ఉపయోగించవచ్చు

ఇప్పుడు, మోడల్ కొన్ని ఉదాహరణలు చేసిన ఆ ఆకృతిలో ఒక సంగ్రహాన్ని ఇస్తుంది - కాని ఒక ఫలితానికొకటి కంటే ఎక్కువ ట్యాగ్లు ఉంటే, సహాయక కంటెంట్‌లో గుర్తించిన 5 ట్యాగ్లకు ప్రాధాన్యత ఇస్తుంది.

---

<!--
LESSON TEMPLATE:
ఈ యూనిట్ ప్రధాన భావన #1 ను కవర్ చేయాలి.
భావనను ఉదాహరణలు మరియు సూచనలతో బలపరుస్తుంది.

భావన #3:
ప్రాంప్ట్ ఇంజినీరింగ్ సాంకేతికతలు.
ప్రాంప్ట్ ఇంజినీరింగ్ కొరకు కొన్ని మౌలిక సాంకేతికతలు ఏమిటి?
కొన్ని వ్యాయామాలతో వివరించండి.
-->

## ప్రాంప్ట్ బెటర్ చిట్కాలు

ఇప్పుడు మనం తెలుసుకున్నందున ప్రాంప్ట్‌లను _నిర్మించగలిగే విధానం_, వాటిని ఉత్తమంగా _డిజైన్_ చేయడాన్ని ఎలా చేయాలో ఆలోచしまొచ్చు. దీన్ని రెండు భాగాలుగా తీసుకోవచ్చు - సరైన _మనోభావం_ కలిగి ఉండటం మరియు సరైన _సాంకేతికతలను_ ఉపయోగించడం.

### ప్రాంప్ట్ ఇంజినీరింగ్ మనోభావం

ప్రాంప్ట్ ఇంజినీరింగ్ ఒక ప్రయోగాత్మక ప్రక్రియ కాబట్టి, మూడు ప్రధాన మార్గదర్శక అంశాలు పరిగణించండి:

1. **డొమైన్ అవగాహన ముఖ్యం.** సమాధాన ఖచ్చితత్వం మరియు సంబంధితత అనేది ఆ అనువర్తనం లేదా వాడుకరి పనిచేస్తున్న _డొమైన్_-పై ఆధారపడి ఉంటుంది. మీ అవగాహన మరియు డొమైన్లో నైపుణ్యంతో **సాంకేతికతలను అనుకూలీకరించండి**. ఉదాహరణకు, మీ సిస్టమ్ ప్రాంప్ట్‌లలో _డొమైన్-స్పెసిఫిక్ వ్యక్తిత్వాలు_ నిర్వచించండి లేదా వాడుకరి ప్రాంప్ట్‌లలో _డొమైన్-స్పెసిఫిక్ టెంప్లేట్లు_ ఉపయోగించండి. డొమైన్ సంబంధిత సందర్భాలను ప్రతిబింబించే సహాయక కంటెంట్‌ను ఇవ్వండి లేదా మోడల్‌ను పరిచిత ఉపయోగ నమూనాల వైపు నడిపించేందుకు _డొమైన్-స్పెసిఫిక్ సూచనలు మరియు ఉదాహరణలు_ అందించండి.

2. **మోడల్ అవగాహన ముఖ్యం.** మోడల్స్ సహజంగ stochastic (సాంఖ్యిక) గా ఉంటాయని మనం తెలుసు. కానీ ట్రైనింగ్ డేటాసెట్ (మునుపటి జ్ఞానం), అందించే సామర్థ్యాలు (API లేదా SDK ద్వారా) మరియు కంటెంట్ రకానికి (కోడ్, చిత్రం, వచనం) సంబంధించి మోడల్ అమలు భిన్నంగా ఉండొచ్చు. మీరు ఉపయోగిస్తున్న మోడల్ యొక్క బలాలు మరియు పరిమితులను తెలుసుకుని, ఆ జ్ఞానంతో _పనులను ప్రాధాన్యపు క్రమంలో ఉంచండి_ లేదా మోడల్ సామర్థ్యాలకు అనుగుణంగా _అనుకూల టెంప్లేట్లను_ రూపొందించండి.

3. **ఇటరేషన్ మరియు ధృవీకరణ ముఖ్యం.** మోడల్స్ వేగంగా అభివృద్ధి చెందుతున్నాయి అలాగే ప్రాంప్ట్ ఇంజినీరింగ్ సాంకేతికతలు కూడా. ఒక డొమైన్ నిపుణుడిగా, మీకు ఇతర సందర్భాలు లేదా ప్రమాణాలు ఉండొచ్చు, ఇవి సాధారణ కమ్యూనిటీకి వర్తించకపోవచ్చు. ప్రాంప్ట్ ఇంజినీరింగ్ సాధనాలు మరియు సాంకేతికతలను ఉపయోగించి ప్రాంప్ట్ నిర్మాణాన్ని "జంప్ స్టార్ట్" చేయండి, తరువాత మీ స్వంత అవగాహన మరియు క్షేత్ర నైపుణ్యంతో ఫలితాలను పునరావృతం చేసి ధృవీకరించండి. మీ అనుభవాన్ని రికార్డు చేసి ఒక **జ్ఞాన బేస్** (ఉదా., ప్రాంప్ట్ లైబ్రరీలు) సృష్టించండి, తద్వారా ఇతరులు భవిష్యత్తులో వేగంగా పునరావృత కొరకు దీనిని ఉపయోగించగలరు.

## ఉత్తమ పద్ధతులు

ఇప్పుడు [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) మరియు [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) ప్రాచుర్యమున్న నిర్ధేశకులు సూచించే సాధారణ ఉత్తమ పద్ధతులపై ఒక చూపు వెతుకుదాం.

| ఏమి                              | ఎందుకు                                                                                                                                                                                                                                            |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| తాజా మోడల్స్‌ను అంచనా వేయండి.  | పలు సాంకేతిక మెరుగుదలలు ఉన్నాయి మరియు నాణ్యత మెరుగ్గా ఉంటుంది - కానీ ఖర్చులు పెరుగుతాయని కూడా ఉండొచ్చు. వాటి ప్రభావాలను అంచనా వేసి మైగ్రేషన్ నిర్ణయాలు తీసుకోండి.                                                                                  |
| సూచనలు మరియు సందర్భం వేరుగా ఉంచండి       | మీ మోడల్ లేదా ప్రొవైడియర్ సూచనలు, ప్రధాన మరియు సహాయక కంటెంట్‌ మధ్య స్పష్టంగా భేదం చూపడానికోసం _డెలిమిటర్లు_ ఉంటాయా అని చూడండి. ఇది టోకన్లకు సరైన బరువు ఇవ్వడంలో సాయపడుతుంది.                                                                           |
| స్పష్టంగా మరియు నిర్దిష్టంగా ఉండండి             | కావలసిన సందర్భం, ఫలితం, పొడవు, ఆకృతి, శైలి మొదలైన వాటి గురించి మరింత వివరంగా చెప్పండి. ఇది సమాధాన నాణ్యతను మరియు విశ్వసనీయతను పెంచుతుంది. టెంప్లేట్లలో పునఃవినియోగానికి సంబంధించిన రెసిపీలను నమోదు చేయండి.                                                     |
| వివరాలతో, ఉదాహరణలతో నిర్దేశించండి          | మోడల్స్ మంచి ప్రతిస్పందన ఇవ్వడానికి "చూపి చెప్పడం" పద్ధతిని ఇష్టపడతాయి. మీరు సూచన ఇస్తారు (ఉదాహరణలు లేకుండా `zero-shot`), తరువాత ఫలితాన్ని మెరుగుపరచేందుకు కొంత ఉదాహరణలు ఇచ్చి `few-shot` ప్రయత్నం చేయండి. ఉపమానాలు ఉపయోగించండి.                                   |
| పూర్తి చేయుట ప్రారంభించేందుకు సూచనలు ఇవ్వండి | దీని అంచనాని వేయి/ఫలితానికి ముందే కొన్ని పదాలు లేదా పదబంధాలు ఇచ్చి, సమాధానం మొదలుపెట్టేందుకు సహాయపడండి.                                                                                                                                        |
| రెండుసార్లు చెప్పండి                      | కొన్ని సందర్భాల్లో మోడల్‌కు మీరు మీ సూచనను పునరావృతం చేయాల్సి వస్తుంది. ప్రధాన కంటెంట్ ముందు మరియు తర్వాత సూచనలు ఇవ్వండి కానీ అనేక మార్లు ప్రయత్నించి ఏమి పనిచేస్తుందో చూసి ధృవీకరించండి.                                                                                 |
| క్రమం ముఖ్యమైనది                     | మీరు మోడల్‌కు సమాచారాన్ని అందించే క్రమం ఫలితాన్ని ప్రభావితం చేయవచ్చు, ఇది పాఠాలు నేర్చుకునే ఉదాహరణల్లో కూడా ఉంటుంది. సరైన దృశ్యమును కనుగొనటానికి వేరువేరు ఎంపికలు ప్రయత్నించండి.                                                                           |
| మోడల్‌కు “విధేయ” అవకాశమివ్వండి       | పని పూర్తిచేయలేని పక్షంలో మోడల్ ఇచ్చగలిగే ఒక _ఫాల్‌బ్యాక్_ సమాధాను అందించండి. ఇది తప్పు లేదా కల్పిత సమాధానాల సంభావ్యత తగ్గిస్తుంది.                                                                                                                     |
|                                   |                                                                                                                                                                                                                                                   |

ఏ ఉత్తమ పద్ధతిని అనుసరించినా, మోడల్, పని మరియు డొమైన్ ఆధారంగా _మీ ప్రయోజనం వేరుగా ఉండొచ్చు_ అని గుర్తుంచుకోండి. వీటిని ప్రారంభ బిందువుగా ఉపయోగించి మీకు ఏమి మంచి పనిచేస్తుందో నిరంతరం పునఃపరిశీలిస్తూ ప్రయోగించండి. కొత్త మోడళ్లు మరియు సాధనాలు వచ్చినప్పుడు ప్రాంప్ట్ ఇంజినీరింగ్ ప్రాసెస్ scalability మరియు సమాధాన నాణ్యత దృష్ట్యా పునఃమూల్యాంకనం చేయండి.

<!--
LESSON TEMPLATE:
ఈ యాప్‌యోగానికి సంబంధించి కోడ్ ఛాలెంజ్ ఇవ్వండి, అందుబాటులో ఉంటే

చాలెంజ్:
హైదరాబాద్ నోట్బుక్ యందు కేవలం కోడ్ వ్యాఖ్యలతో ఉన్న సూచనలు (కోడ్ భాగాలు ఖాళీగా ఉంటాయి) కలిగి ఉండాలి.

సమాధానం:
ఆ నోట్బుక్ యొక్క ఒక కాపీని ప్రాంప్ట్ తో పూరించి నడుపుతూ ఒక ఉదాహరణ చూపండి.
-->

## అసైన్మెంట్

అభినందనలు! మీరు పాఠ్యాన్ని చివర దాకా చదివారు! ఇప్పుడు ఆ తత్వాలు మరియు సాంకేతికతలను నిఖార్సుగా పరీక్షించడానికి సమయం వచ్చింది!

మా అసైన్మెంట్ కోసం, మీరు ఇన్‌టరాక్టివ్‌గా పూర్తి చేయగల జూపిటర్ నోట్‌బుక్‌ను వాడతారు. మీ స్వంత మార్క్‌డౌన్ మరియు కోడ్ సెల్లులతో నోట్బుక్‌ను విస్తరించి, ఆలోచనలు మరియు సాంకేతికతలను అన్వేషించవచ్చు.

### మొదలు పెట్టడానికి, రిపోను ఫోర్ట్ చేయండి, తరువాత

- (సిఫార్సు) GitHub కోడ్స్‌పేస్‌లను ప్రారంభించండి
- (మరొక ఎంపిక) రిపోను మీ స్థానిక పరికరానికి క్లోన్ చేసి Docker డెస్క్‌టాప్‌తో ఉపయోగించండి
- (మరొక ఎంపిక) ఇష్టమైన నోట్‌బుక్ రన్‌టైమ్ వాతావరణంలో నోట్బుక్‌ను ఓపెన్ చేయండి.

### తరువాత, మీ ఎన్వారిలు వేరియబుల్స్‌ను కాన్ఫిగర్ చేయండి

- రిపోజిటరీ మూలంలో ఉన్న `.env.copy` ఫైల్‌ను `.env` గా కాపీ చేసి `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` మరియు `AZURE_OPENAI_DEPLOYMENT` విలువలు నింపండి. ఎలా చేయాలో [Learning Sandbox విభాగానికి](#నేర్చుకునే-సాండ్‌బాక్స్) వెళ్ళి తెలుసుకోండి.

### తరువాత, జూపిటర్ నోట్‌బుక్‌ను ఓపెన్ చేయండి

- రన్‌టైమ్ కర్నల్‌ను ఎంచుకోండి. 1 లేదా 2 ఎంపికలను వాడితే డెవ్ కంటైనర్ అందించే డిఫాల్ట్ Python 3.10.x కర్నల్‌ను ఎంచుకోండి.

మీరు వ్యాయామాలను నడిపే సిద్దంగా ఉన్నారు. ఇక్కడ _సరైన లేదా తప్పు_ సమాధానాలు ఉండవు - ప్రాయోగికంగా ప్రయత్నిస్తూ, ఒక మోడల్ మరియు అప్లికేషన్ డొమైన్ కోసం పనిచేసే దాన్ని కనుగొనడం ముఖ్యం.

_ఇందుకు బదులుగా ఈ పాఠంలో కోడ్ పరిష్కారం భాగాలు లేవు. బదులు, నోట్బుక్‌లో "నా పరిష్కారం:" అనే టెక్స్ట్ ఉన్న మార్క్‌డౌన్ సెల్లులు ఉంటాయి, అవి ఒక ఉదాహరణ ఫలితాన్ని సూచిస్తాయి._

 <!--
LESSON TEMPLATE:
ఈ విభాగాన్ని ఒక సారాంశంతో మరియు స్వ-గైడ్ నేర్చుకునే వనరులతో పాటు ముగించండి.
-->

## జ్ఞాన పరీక్ష

తగ్గని కొన్ని ఉత్తమ పద్ధతులు అనుసరిస్తూ క్రింద ఇచ్చిన ప్రాంప్ట్‌లలో ఎది మంచి?

1. నాకు ఎర్ర కారును చూపించు
2. నాకు ఎర్ర కారును చూపించు, అది వాల్వో మేక్ XC90 మోడల్, ఒక గుట్ట వద్ద ప్యార్క్ చేసినది, సూర్యాస్తమయం వద్ద
3. నాకు ఎర్ర కారును చూపించు, అది వాల్వో మేక్ XC90 మోడల్

సమాధానం: 2, ఇది ఉత్తమ ప్రాంప్ట్, ఎందుకంటే ఇది "ఏది కావాలి" అనేదానికి వివరాలు ఇస్తుంది, స్పెసిఫిక్ (ఎలాంటి కాదు, ఒక ప్రత్యేక మేక్ మరియు మోడల్) మరియు మొత్తం సన్నివేశాన్ని వివరిస్తుంది. 3 రెండవ ఉత్తమం, ఎందుకంటే ఇది కూడా సరైన వివరణ కలిగి ఉంది.

## 🚀 సవాలు

"cue" సాంకేతికతను ఈ ప్రాంప్ట్‌తో ఉపయోగించగలరా చూడు: వాక్యం పూర్తిచేయి "నాకు ఎర్ర కారును చూపించు, వాల్వో మేక్ మరియు " ఇది ఏమి ప్రత్యుత్తరం ఇస్తుంది? మరియు మీరు దానిని ఎలా మెరుగుపరచుకుంటారు?

## గొప్ప పని! మీ నేర్చుకుందాం కొనసాగించండి

వేరే వివిధ ప్రాంప్ట్ ఇంజినీరింగ్ ధోరణుల గురించి తెలుసుకోవాలనుకుంటే [కొనసాగింపు నేర్చుకునే పేజీకి](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) వెళ్లండి, ఈ అంశంపై మరిన్ని గొప్ప వనరులు అందుబాటులో ఉన్నాయి.

పాఠం 5 కి వెళ్లండి, అక్కడ [అత్యాధునిక ప్రాంప్ట్ సాంకేతికతలను](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst) పరిశీలిస్తాము!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->