<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-05-19T22:23:05+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "mo"
}
-->
# Hifz e Aap ke Generative AI Applications

## Taaruf

Is sabaq mein hum cover kareinge:

- AI systems ke tanazur mein security.
- AI systems ke aam khatarat aur dhamkiyan.
- AI systems ko mehfooz banane ke tareeqe aur soch.

## Seekhne ke Maqsad

Is sabaq ko mukammal karne ke baad, aap samajh sakeinge:

- AI systems ke khatarat aur dhamkiyan.
- AI systems ko mehfooz banane ke aam tareeqe aur amal.
- Kaise security testing ka amal unexpected natayij aur user ka trust kam hone se bacha sakta hai.

## Generative AI ke tanazur mein security ka kya matlab hai?

Jab ke Artificial Intelligence (AI) aur Machine Learning (ML) technologies hamari zindagiyon ko zyada se zyada shaakal dene lage hain, ye na sirf customer data balki AI systems ko bhi mehfooz rakhna zaroori hai. AI/ML ko ab un industries mein zyada se zyada istamal kiya ja raha hai jahan ghalat faisla sanjeeda natayij ka sabab ban sakta hai.

Yahan kuch ahem points hain jo sochne laayak hain:

- **AI/ML ka asar**: AI/ML ka roz marra ki zindagi par ahem asar hota hai aur isliye inka mehfooz hona zaroori hai.
- **Security Challenges**: AI/ML ke is asar ko sahi tawajju dena zaroori hai taake AI-based products ko trolls ya organized groups ki sophisticated attacks se mehfooz rakha ja sake.
- **Strategic Problems**: Tech industry ko proactive approach apnani chahiye taake customer ki lambay arse tak safety aur data security ko ensure kiya ja sake.

Iske ilawa, Machine Learning models aksar malicious input aur benign anomalous data ke darmiyan farq nahi kar sakte. Training data ka ahem hissa uncurated, unmoderated, public datasets se aata hai, jo 3rd-party contributions ke liye khula hai. Attackers ko datasets ko compromise karne ki zaroorat nahi hoti jab woh in datasets mein freely contribute kar sakte hain. Waqt ke saath, low-confidence malicious data high-confidence trusted data ban jata hai, agar data structure/formatting sahi rahe.

Yehi wajah hai ke aapke models jo faislay karte hain un data stores ki integrity aur protection ko ensure karna intahi zaroori hai.

## AI ke khatarat aur risks ko samajhna

AI aur related systems ke tanazur mein, data poisoning aaj ka sabse bara security threat hai. Data poisoning tab hota hai jab koi shakhs jaan bujh kar AI ko train karne ke liye istamal hone wale maaloomat ko badal deta hai, jisse AI ghalatiyan karne lagta hai. Ye isliye hota hai kyunki standardized detection aur mitigation methods ka fukdan hota hai, aur hamara reliance untrusted ya uncurated public datasets par hota hai training ke liye. Data integrity ko maintain karne aur flawed training process se bachne ke liye, aapke data ke asal aur lineage ko track karna intahi ahem hai. Warna purani kahawat “garbage in, garbage out” sahi sabit hoti hai, jisse model performance compromised ho jati hai.

Yahan kuch misalay hain ke data poisoning aapke models ko kaise asar kar sakti hai:

1. **Label Flipping**: Binary classification task mein, ek dushman jaan bujh kar training data ke chhote subset ke labels ko flip kar deta hai. Misal ke taur par, benign samples ko malicious label kiya jata hai, jisse model ghalat associations seekhta hai.\
   **Misal**: Spam filter jo legitimate emails ko spam ke taur par misclassify karta hai labels ko manipulate karne ki wajah se.
2. **Feature Poisoning**: Ek attacker training data mein features ko subtle tor par modify karta hai taake bias introduce ya model ko mislead kar sake.\
   **Misal**: Product descriptions mein irrelevant keywords add karna taake recommendation systems ko manipulate kiya ja sake.
3. **Data Injection**: Training set mein malicious data inject karna taake model ke behavior ko influence kiya ja sake.\
   **Misal**: Fake user reviews introduce karna taake sentiment analysis results ko skew kiya ja sake.
4. **Backdoor Attacks**: Ek dushman training data mein hidden pattern (backdoor) insert karta hai. Model is pattern ko seekhta hai aur trigger hone par malicious behavior karta hai.\
   **Misal**: Face recognition system jo backdoored images ke sath train kiya gaya ho jo specific shakhs ko misidentify karta hai.

MITRE Corporation ne [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst) banaya hai, ek knowledgebase tactics aur techniques ka jo adversaries ne real-world attacks mein AI systems par istamal kiya hai.

> AI-enabled systems mein vulnerabilities ki taadaad mein izafa ho raha hai, kyunki AI ka incorporation existing systems ke attack surface ko traditional cyber-attacks se aage barhata hai. Hamne ATLAS ko banaya taake in unique aur evolving vulnerabilities ke baare mein awareness barh sake, kyunki global community zyada se zyada AI ko mukhtalif systems mein incorporate kar rahi hai. ATLAS ko MITRE ATT&CK® framework ke baad model kiya gaya hai aur iske tactics, techniques, aur procedures (TTPs) ATT&CK ke sath complementary hain.

Bilkul MITRE ATT&CK® framework ki tarah, jo traditional cybersecurity mein extensively istamal hota hai advanced threat emulation scenarios plan karne ke liye, ATLAS ek easily searchable set TTPs provide karta hai jo emerging attacks se defend karne ke liye behtar samajh aur tayyari mein madad kar sakta hai.

Iske ilawa, Open Web Application Security Project (OWASP) ne "[Top 10 list](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" banaya hai jo applications jo LLMs ko utilize karte hain unmein paaye jane wale sabse critical vulnerabilities ko highlight karta hai. Ye list un khatarat ko highlight karti hai jaise ke aforementioned data poisoning aur doosre khatarat jaise:

- **Prompt Injection**: Ek technique jahan attackers Large Language Model (LLM) ko carefully crafted inputs ke zariye manipulate karte hain, jisse ye apne intended behavior se bahar ho jata hai.
- **Supply Chain Vulnerabilities**: Woh components aur software jo LLM ke applications ko banate hain, jaise ke Python modules ya external datasets, khud compromised ho sakte hain jisse unexpected results, introduced biases aur hatta ke underlying infrastructure mein vulnerabilities aa sakti hain.
- **Overreliance**: LLMs fallible hain aur hallucinate karne ke prone rahe hain, inaccurate ya unsafe results provide karte hain. Kai documented circumstances mein, log results ko face value par le lete hain jisse unintended real-world negative consequences hote hain.

Microsoft Cloud Advocate Rod Trent ne ek free ebook likhi hai, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), jo in aur doosri emerging AI threats mein deeply dive karti hai aur ye scenarios best tackle karne ke extensive guidance provide karti hai.

## AI Systems aur LLMs ke liye Security Testing

Artificial intelligence (AI) mukhtalif domains aur industries ko transform kar raha hai, society ke liye naye possibilities aur benefits offer kar raha hai. Magar, AI significant challenges aur risks bhi pose karta hai, jaise ke data privacy, bias, lack of explainability, aur potential misuse. Isliye, ye zaroori hai ke AI systems secure aur responsible hon, matlab ye ethical aur legal standards ko adhere karte hon aur users aur stakeholders ke liye trusted hon.

Security testing ek AI system ya LLM ke security ko evaluate karne ka process hai, jo unke vulnerabilities ko identify aur exploit karne ke zariye kiya jata hai. Ye developers, users, ya third-party auditors ke zariye kiya ja sakta hai, depending on testing ka purpose aur scope. AI systems aur LLMs ke liye sabse aam security testing methods kuch ye hain:

- **Data sanitization**: Ye sensitive ya private information ko training data ya AI system ya LLM ke input se remove ya anonymize karne ka process hai. Data sanitization data leakage aur malicious manipulation ko prevent karne mein madad kar sakta hai confidential ya personal data ki exposure ko kam karke.
- **Adversarial testing**: Ye adversarial examples ko AI system ya LLM ke input ya output par generate aur apply karne ka process hai taake uski robustness aur resilience ko adversarial attacks ke against evaluate kiya ja sake. Adversarial testing AI system ya LLM ki vulnerabilities aur weaknesses ko identify aur mitigate karne mein madad kar sakta hai jo attackers exploit kar sakte hain.
- **Model verification**: Ye AI system ya LLM ke model parameters ya architecture ki correctness aur completeness ko verify karne ka process hai. Model verification model stealing ko detect aur prevent karne mein madad kar sakta hai ye ensure karke ke model protected aur authenticated hai.
- **Output validation**: Ye AI system ya LLM ke output ki quality aur reliability ko validate karne ka process hai. Output validation malicious manipulation ko detect aur correct karne mein madad kar sakta hai ye ensure karke ke output consistent aur accurate hai.

OpenAI, AI systems mein leader, ne _safety evaluations_ ka silsila setup kiya hai jo unke red teaming network initiative ka hissa hai, jo AI systems ke output ko test karne ke liye hai taake AI safety mein contribute kiya ja sake.

> Evaluations simple Q&A tests se lekar more-complex simulations tak range kar sakti hain. Yahan kuch concrete examples hain jo OpenAI ne AI behaviors ko mukhtalif angles se evaluate karne ke liye develop kiye hain:

#### Persuasion

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Ek AI system doosri AI system ko secret word kehne mein kitna achha trick kar sakta hai?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Ek AI system doosri AI system ko paise donate karne mein kitna achha convince kar sakta hai?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Ek AI system doosri AI system ki political proposition ki support ko kitna achha influence kar sakta hai?

#### Steganography (hidden messaging)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Ek AI system secret messages ko doosri AI system ke zariye bina pakde jaaye pass karne mein kitna achha hai?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Ek AI system messages ko compress aur decompress karne mein kitna achha hai, taake secret messages ko chhupaya ja sake?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Ek AI system doosri AI system ke sath bina direct communication ke coordinate karne mein kitna achha hai?

### AI Security

Ye intahi zaroori hai ke ham AI systems ko malicious attacks, misuse, ya unintended consequences se mehfooz rakhne ki koshish karein. Isme ye steps lena shamil hai taake AI systems ki safety, reliability, aur trustworthiness ko ensure kiya ja sake, jaise:

- AI models ko train aur run karne ke liye istamal hone wale data aur algorithms ko secure karna
- AI systems ki unauthorized access, manipulation, ya sabotage ko prevent karna
- AI systems mein bias, discrimination, ya ethical issues ko detect aur mitigate karna
- AI decisions aur actions ki accountability, transparency, aur explainability ko ensure karna
- AI systems ke goals aur values ko insano aur society ke sath align karna

AI security AI systems aur data ki integrity, availability, aur confidentiality ko ensure karne ke liye ahem hai. AI security ke kuch challenges aur opportunities hain:

- Opportunity: AI ko cybersecurity strategies mein incorporate karna kyunki ye threats ko identify aur response times ko improve karne mein crucial role play kar sakta hai. AI cyberattacks jaise phishing, malware, ya ransomware ki detection aur mitigation ko automate aur augment karne mein madad kar sakta hai.
- Challenge: AI ko adversaries sophisticated attacks launch karne ke liye bhi istamal kar sakte hain, jaise fake ya misleading content generate karna, users ko impersonate karna, ya AI systems mein vulnerabilities ko exploit karna. Isliye, AI developers ki unique responsibility hai ke wo systems ko design karein jo misuse ke against robust aur resilient hon.

### Data Protection

LLMs un data ki privacy aur security ke liye risks pose kar sakte hain jo wo istamal karte hain. Misal ke taur par, LLMs apne training data se sensitive information jaise personal names, addresses, passwords, ya credit card numbers ko memorize aur leak kar sakte hain. Ye malicious actors ke zariye manipulate ya attack bhi ho sakte hain jo unke vulnerabilities ya biases ko exploit karna chahte hain. Isliye, ye risks se waqif hona aur LLMs ke sath istamal hone wale data ko protect karne ke liye munasib iqdamat lena ahem hai. LLMs ke sath istamal hone wale data ko protect karne ke liye kuch steps hain jo aap le sakte hain. Ye steps shamil hain:

- **LLMs ke sath share hone wale data ki amount aur type ko limit karna**: Sirf wo data share karein jo intended purposes ke liye zaroori aur relevant hai, aur koi sensitive, confidential, ya personal data share karne se gurez karein. Users ko LLMs ke sath share hone wale data ko anonymize ya encrypt bhi karna chahiye, jaise ke kisi identifying information ko remove ya mask karna, ya secure communication channels ko istamal karna.
- **LLMs ke generate kiye gaye data ko verify karna**: LLMs ke generate kiye gaye output ki accuracy aur quality ko hamesha check karein taake ye unwanted ya inappropriate information na contain kare.
- **Kisi bhi data breach ya incident ko report aur alert karna**: LLMs se kisi bhi suspicious ya abnormal activities ya behaviors ke liye hoshiyar rahein, jaise irrelevant, inaccurate, offensive, ya harmful texts generate karna. Ye data breach ya security incident ki indication ho sakta hai.

Data security, governance, aur compliance kisi bhi organization ke liye critical hain jo multi-cloud environment mein data aur AI ki power ko leverage karna chahti hai. Apne data ko secure aur govern karna ek complex aur multifaceted undertaking hai. Aapko mukhtalif types ke data (structured, unstructured, aur AI ke zariye generate kiya gaya data) ko mukhtalif locations mein across multiple clouds secure aur govern karna hai, aur aapko existing aur future data security, governance, aur AI regulations ko account karna hai. Apne data ko protect karne ke liye, aapko kuch best practices aur precautions adopt karna hoga, jaise:

- Cloud services ya platforms ko istamal karna jo data protection aur privacy features offer karte hain.
- Data quality aur validation tools ko istamal karna taake apne data ko errors, inconsistencies, ya anomalies ke liye check kar sakein.
- Data governance aur ethics frameworks ko istamal karna taake apne data ko responsible aur transparent manner mein istamal karna ensure kiya ja sake.

### Real-world threats ko emulate karna - AI red teaming

Real-world threats ko emulate karna resilient AI systems banane mein ab ek standard practice maana jata hai jo similar tools, tactics, procedures ko employ karte hain taake systems ke risks ko identify kiya ja sake aur defenders ki response ko test kiya ja sake.

> AI red teaming ka practice ab ek expanded meaning le chuka hai: ye sirf security vulnerabilities ke liye probing ko cover nahi karta, balki doosre system failures ke liye probing ko bhi shamil karta hai, jaise potentially harmful content ka generation. AI systems naye risks ke sath aate hain, aur red teaming un novel risks ko samajhne mein core hai, jaise prompt injection aur ungrounded content ka production. - [Microsoft AI Red Team building future of safer AI](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

Neeche kuch key insights hain jo Microsoft ke AI Red Team program ko shape kar chuke hain.

1. **AI Red Teaming ka Expansive Scope:**
   AI red teaming ab security aur Responsible AI (RAI) outcomes dono ko encompass karta hai. Traditionally, red teaming security aspects par focus karta tha, model ko ek vector ke taur par treat karta tha (misal ke taur par, underlying model ko steal karna). Magar, AI systems naye security vulnerabilities (misal ke taur par, prompt injection, poisoning) introduce karte hain, jo special attention ka talabb karte hain. Security ke ilawa, AI red teaming fairness issues (misal ke taur par, stereotyping) aur harmful content (misal ke taur par, violence ki glorification) ko bhi probe karta hai. In issues ka early identification defense investments ko prioritize karne ki ijazat deta hai.
2. **Malicious aur Benign Failures:**
   AI red teaming failures ko malicious aur benign perspectives se consider karta hai. Misal ke taur par, jab new Bing ko red team kiya jata hai, ham na sirf ye explore karte hain ke malicious adversaries kaise system ko subvert kar sakte hain balki regular users kaise problematic ya harmful content ka samna kar sakte hain. Traditional security red teaming jo mainly malicious actors par focus karta hai, AI red teaming broader range of personas aur potential failures ko account karta hai.
3. **AI Systems

I'm sorry, but it seems there might be a typo in your request as "mo" is not a recognized language code. Could you please specify the language you would like the text to be translated into?