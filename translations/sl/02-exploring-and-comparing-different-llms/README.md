# Raziskovanje in primerjava različnih LLM-jev

[![Raziskovanje in primerjava različnih LLM-jev](../../../translated_images/sl/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Kliknite zgornjo sliko za ogled videa te lekcije_

V prejšnji lekciji smo videli, kako Generativna umetna inteligenca spreminja tehnološko landskape, kako delujejo veliki jezikovni modeli (LLM-ji) in kako jih lahko podjetje – kot naš startup – uporabi za svoje primere rabe in raste! V tem poglavju bomo primerjali in nasprotovali različne vrste velikih jezikovnih modelov (LLM), da bomo razumeli njihove prednosti in slabosti.

Naslednji korak na poti našega startupa je raziskovanje trenutnega stanja LLM-jev in razumevanje, kateri so primerni za naš primer uporabe.

## Uvod

Ta lekcija bo obravnavala:

- Različne vrste LLM-jev v trenutnem okolju.
- Testiranje, ponavljanje in primerjanje različnih modelov za vaš primer uporabe v Azure.
- Kako postaviti LLM.

## Cilji učenja

Po zaključku te lekcije boste lahko:

- Izbrali pravi model za vaš primer uporabe.
- Razumeli, kako testirati, ponavljati in izboljšati zmogljivost vašega modela.
- Spoznali, kako podjetja uvajajo modele.

## Razumevanje različnih vrst LLM-jev

LLM-ji se lahko kategorizirajo na več načinov glede na njihovo arhitekturo, podatke za učenje in primer uporabe. Razumevanje teh razlik bo pomagalo našemu startupu izbrati pravi model za scenarij in razumeti, kako testirati, ponavljati in izboljšati zmogljivost.

Obstaja veliko različnih vrst LLM-jev, izbira modela pa je odvisna od tega, za kaj jih želite uporabiti, vaših podatkov, koliko ste pripravljeni plačati in drugih dejavnikov.

Glede na to, ali želite modele uporabiti za besedilo, zvok, video, generiranje slik in podobno, boste morda izbrali drugačen tip modela.

- **Prepoznavanje zvoka in govora**. Whisper-stilski modeli so še vedno uporabni splošni modeli za prepoznavanje govora, vendar produkcijske možnosti sedaj vključujejo tudi novejše modele za pretvorbo govora v besedilo, kot so `gpt-4o-transcribe`, `gpt-4o-mini-transcribe` in različice za diarizacijo. Ocenite jezikovno pokritost, diarizacijo, podporo v realnem času, zakasnitev in stroške za vaš primer uporabe. Več si preberite v [OpenAI dokumentaciji za pretvorbo govora v besedilo](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst).

- **Generiranje slik**. DALL-E in Midjourney sta znani možnosti za generiranje slik, vendar trenutni OpenAI API-ji za slike temeljijo na GPT Image modelih, kot je `gpt-image-2`, medtem ko so Stable Diffusion, Imagen, Flux in druge družine modelov tudi pogosto izbrane možnosti. Primerjajte zvestobo napotkov, podporo za urejanje, nadzor sloga, varnostne zahteve in licenciranje. Več si preberite v [OpenAI vodiču za generiranje slik](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) in v poglavju 9 tega kurikuluma.

- **Generiranje besedila**. Modeli za besedilo zajemajo modele na robu tehnologije, modele za sklepanje, manjše modele z nizko zakasnitvijo in modele z odprtimi utežmi. Trenutni primeri vključujejo OpenAI GPT-5.x modele, Anthropic Claude 4.x modele, Google Gemini 3.x modele, Meta Llama 4 modele in Mistral modele. Ne izbirajte samo po datumu izida ali ceni; primerjajte kakovost opravljene naloge, zakasnitev, velikost konteksta, uporabo orodij, varnostno vedenje, regionalno razpoložljivost in skupne stroške. [Microsoftov katalog Foundry modelov](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) je dobro mesto za primerjavo modelov, ki so na voljo v Azure.

- **Večmodalnost**. Mnogi trenutni modeli lahko obdelujejo več kot le besedilo. Nekateri sprejemajo vhod v obliki slike, zvoka ali videa; nekateri lahko kličejo orodja; specializirani modeli pa lahko generirajo slike, zvok ali video. Na primer, trenutni OpenAI modeli podpirajo besedilo in slikovne vhode, modeli Gemini lahko podpirajo besedilo, kodo, slike, zvok in video glede na različico, Llama 4 Scout in Maverick pa so nativno večmodalni modeli z odprtimi utežmi. Vedno pred gradnjo poteka preverite kartico vsakega modela glede podprtih vhodnih in izhodnih modalitet.

Izbira modela pomeni, da dobite nekaj osnovnih zmožnosti, vendar morda to ni dovolj. Pogosto imate podatke specifične za podjetje, o katerih morate LLM na nek način obvestiti. Obstaja nekaj različnih možnosti, kako se tega lotiti; o tem več v prihajajočih razdelkih.

### Temeljni modeli versus LLM-ji

Izraz Temeljni model so [kovali raziskovalci iz Stanforda](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) in je opredeljen kot AI model, ki sledi določenim kriterijem, kot so:

- **So usposobljeni z nesupervidiranim ali samosupervidiranim učenjem**, kar pomeni, da so usposobljeni na neoznačenih večmodalnih podatkih in ne potrebujejo človeškega označevanja ali označevanja podatkov za proces učenja.
- **So zelo veliki modeli**, temeljijo na zelo globokih nevronskih mrežah, usposobljenih na milijardah parametrov.
- **So običajno namenjeni kot ‘temelj’ za druge modele**, kar pomeni, da jih je mogoče uporabiti kot izhodišče za druge modele, ki se lahko nato prilagodijo s finim nastavljanjem.

![Temeljni modeli versus LLM-ji](../../../translated_images/sl/FoundationModel.e4859dbb7a825c94.webp)

Vir slike: [Essential Guide to Foundation Models and Large Language Models | avtor Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Za nadaljnjo pojasnitev te razlike vzemimo ChatGPT kot zgodovinski primer. Zgodnje različice ChatGPT so uporabljale GPT-3.5 kot temeljni model. OpenAI je nato uporabil podatke specifične za klepet in tehnike usklajevanja, da je ustvaril prilagojeno različico, ki je bolje delovala v pogovornih situacijah, kot so chatbot-i. Sodobne AI storitve pogosto preklapljajo med več različicami modelov, zato ime storitve in osnovni model nista vedno ista stvar.

![Temeljni model](../../../translated_images/sl/Multimodal.2c389c6439e0fc51.webp)

Vir slike: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Odprti modeli z odprtimi utežmi proti lastniškim modelom

Še en način kategorizacije LLM-jev je, ali so odprti z odprtimi utežmi, odprtokodni ali lastniški.

Odprtokodni in modeli z odprtimi utežmi omogočajo pregled, prenos ali prilagajanje modelnih artefaktov, vendar se njihove licence razlikujejo. Nekateri so popolnoma odprtokodni, medtem ko so drugi modeli z odprtimi utežmi z omejitvami uporabe. Uporabni so lahko, kadar podjetje potrebuje več nadzora nad uvajanjem, lokalnostjo podatkov, stroški ali prilagoditvijo. Kljub temu morajo ekipe pred njihovo uporabo v produkciji pregledati pogoje licenciranja, stroške strežbe, vzdrževanje, varnostne posodobitve in kakovost evalvacije. Primeri vključujejo [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst), nekatere [Mistral modele](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst) in mnoge modele, gostovane na [Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst).

Lastniški modeli so v lasti ponudnika in so pri njem gostovani. Ti modeli so pogosto optimizirani za upravljano produkcijsko uporabo in lahko nudijo močno podporo, varnostne sisteme, integracijo orodij in skalabilnost. Vendar stranke običajno ne morejo pregledovati ali spreminjati uteži modela in morajo pregledati pogoje ponudnika glede zasebnosti, hrambe, skladnosti in sprejemljive uporabe. Primeri vključujejo [OpenAI modele](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), [Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst) in [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst).

### Vdelava proti generiranju slik proti generiranju besedila in kode

LLM-je lahko kategoriziramo tudi glede na izhod, ki ga generirajo.

Vdelave so nabor modelov, ki lahko pretvorijo besedilo v numerično obliko, imenovano vdelava, ki je numerična reprezentacija vhodnega besedila. Vdelave olajšajo strojem razumevanje razmerij med besedami ali stavki in jih lahko uporabljajo kot vhodne podatke za druge modele, kot so klasifikacijski modeli ali klastrirni modeli, ki dobro delujejo s številčnimi podatki. Modeli vdelav se pogosto uporabljajo za prenosno učenje, kjer je model zgrajen za pomožno nalogo, za katero je na voljo obilica podatkov, nato pa se uteži modela (vdelave) ponovno uporabijo za druge naslednje naloge. Primer te kategorije so [OpenAI vdelave](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Vdelava](../../../translated_images/sl/Embedding.c3708fe988ccf760.webp)

Modeli za generiranje slik so modeli, ki ustvarjajo slike. Ti modeli se pogosto uporabljajo za urejanje slik, sintezo slik in prevajanje slik. Modeli za generiranje slik so pogosto učeni na velikih zbirkah slik, kot je [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), in jih je mogoče uporabiti za generiranje novih slik ali za urejanje obstoječih slik z tehnikami vpletenja, super-resolucije in koloriranja. Primeri vključujejo [GPT Image modele](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst), [Stable Diffusion modele](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst) in modele Imagen.

![Generiranje slik](../../../translated_images/sl/Image.349c080266a763fd.webp)

Modeli za generiranje besedila in kode so modeli, ki generirajo besedilo ali kodo. Ti modeli se pogosto uporabljajo za povzemanje besedil, prevajanje in odgovarjanje na vprašanja. Modeli za generiranje besedila so pogosto učeni na velikih zbirkah besedil, kot je [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), in jih je mogoče uporabiti za generiranje novega besedila ali za odgovarjanje na vprašanja. Modeli za generiranje kode, kot je [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), so pogosto učeni na velikih zbirkah kode, kot je GitHub, in jih je mogoče uporabiti za generiranje nove kode ali odpravljanje napak v obstoječi kodi.

![Generiranje besedila in kode](../../../translated_images/sl/Text.a8c0cf139e5cc2a0.webp)

### Enkoderski-dekoderski proti samo dekoderski

Za razpravo o različnih vrstah arhitektur LLM-jev uporabimo analogijo.

Predstavljajte si, da vam je vaš vodja dal nalogo napisati kviz za študente. Imate dva kolega; eden skrbi za ustvarjanje vsebine, drugi pa za pregled.

Ustvarjalec vsebine je kot samo dekoderski model: lahko pogleda temo, vidi, kaj ste že napisali, in nato nadaljuje z ustvarjanjem vsebine na podlagi tega konteksta. So zelo dobri pri pisanju privlačne in informativne vsebine, vendar niso vedno najboljša izbira, ko je naloga samo klasificirati, pridobiti ali kodirati informacije. Primeri družin samo dekoderskih modelov vključujejo GPT in Llama modele.

Pregledovalec je kot samo enkoderski model, pogleda napisani tečaj in odgovore, opazi razmerje med njimi in razume kontekst, vendar ni dober pri generiranju vsebine. Primer samo enkoderskega modela bi bil BERT.

Predstavljajte si, da imamo tudi nekoga, ki bi lahko ustvaril in pregledal kviz, to je enkodersko-dekoderski model. Nekateri primeri so BART in T5.

### Storitev proti modelu

Zdaj pa govorimo o razlikah med storitvijo in modelom. Storitev je produkt, ki ga ponuja ponudnik oblačnih storitev, pogosto gre za kombinacijo modelov, podatkov in drugih komponent. Model je osrednja komponenta storitve in je pogosto temeljni model, kot je LLM.

Storitev je pogosto optimizirana za produkcijsko uporabo in je prek grafičnega uporabniškega vmesnika pogosto lažja za uporabo kot modeli. Vendar storitve niso vedno brezplačne in lahko zahtevajo naročnino ali plačilo za uporabo, v zameno za uporabo opreme in virov lastnika storitve, optimizacijo stroškov in enostavno skaliranje. Primer storitve je [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-foundry/openai/overview?WT.mc_id=academic-105485-koreyst), ki ponuja plačilo glede na uporabo, kar pomeni, da so uporabniki zaračunani sorazmerno s tem, koliko storitve uporabljajo. Azure OpenAI Service prav tako ponuja varnost na ravni podjetja in okvir odgovorne AI nad zmožnostmi modelov.

Modeli so artefakti nevronske mreže: parametri, uteži, arhitektura, tokenizator in podpora konfiguracije. Zagon modela lokalno ali v zasebnem okolju zahteva ustrezno strojno opremo, infrastrukturo za strežbo, spremljanje ter bodisi združljivo odprtokodno/odprto-utežno licenco ali komercialno licenco. Modeli z odprtimi utežmi, kot so Llama 4 ali Mistral modeli, se lahko gostijo sami, a še vedno zahtevajo računską moč in operativno strokovnost.

## Kako testirati in ponavljati z različnimi modeli za razumevanje zmogljivosti v Azure


Ko je naša ekipa raziskala trenutno pokrajino LLM in identificirala nekaj dobrih kandidatov za njihove scenarije, je naslednji korak njihovo testiranje na njihovih podatkih in delovni obremenitvi. To je iterativen proces, ki poteka z eksperimentiranjem in merjenjem.
Večina modelov, ki smo jih omenili v prejšnjih odstavkih (OpenAI modeli, modeli z odprto težo, kot sta Llama 4 in Mistral, ter modeli Hugging Face) je na voljo v [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst).

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst), prej Azure AI Studio/Azure AI Foundry, je združena platforma Azure za gradnjo AI aplikacij in agentov. Pomaga razvijalcem upravljati življenjski cikel od eksperimentiranja in ocenjevanja do uvajanja, nadzora ter upravljanja. Katalog modelov v Microsoft Foundry omogoča uporabniku:

- Iskanje osnovnega modela zanimanja v katalogu, vključno z modeli, ki jih prodaja Azure, ter modeli partnerjev in ponudnikov skupnosti. Uporabniki lahko filtrirajo po nalogi, ponudniku, licenci, možnosti uvajanja ali imenu.

![Model catalog](../../../translated_images/sl/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- Pregled modelne kartice, ki vključuje podroben opis namena uporabe in podatkov za učenje, primere kode ter rezultate ocenjevanja v notranji knjižnici za ocenjevanje.

![Model card](../../../translated_images/sl/ModelCard.598051692c6e400d.webp)

- Primerjava referenc med modeli in podatkovnimi nizi, ki so na voljo v industriji, da se oceni, kateri model ustreza poslovnemu scenariju, preko zavihka [Model Benchmarks](https://learn.microsoft.com/azure/ai-foundry/concepts/model-benchmarks?WT.mc_id=academic-105485-koreyst).

![Model benchmarks](../../../translated_images/sl/ModelBenchmarks.254cb20fbd06c03a.webp)

- Fine-tunanje podprtih modelov na lastnih učnih podatkih za izboljšanje zmogljivosti modela pri specifični delovni obremenitvi, z izkoriščanjem možnosti eksperimentiranja in sledenja v Microsoft Foundry.

![Model fine-tuning](../../../translated_images/sl/FineTuning.aac48f07142e36fd.webp)

- Uvajanje izvirnega predhodno usposobljenega modela ali fine-tunane različice na oddaljeno končno točko za realnočasovne sklepe, z uporabo upravljanih računalniških virov ali strežništva brez strežnika, da aplikacije lahko model uporabljajo.

![Model deployment](../../../translated_images/sl/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> Ne vsi modeli v katalogu so trenutno na voljo za fine-tuning in/ali uvajanje po sistemu plačila po uporabi. Podrobnosti o zmožnostih in omejitvah modela preverite v modelni kartici.

## Izboljšanje rezultatov LLM

Z ekipo startupa smo raziskovali različne vrste LLM in oblačno platformo (Microsoft Foundry), ki nam omogoča primerjavo različnih modelov, njihovo ocenjevanje na testnih podatkih, izboljšanje zmogljivosti ter uvajanje na inferenčne končne točke.

Kdaj pa naj razmislijo o fine-tuningu modela namesto uporabe predhodno usposobljenega? So še drugi pristopi za izboljšanje zmogljivosti modela pri specifičnih delovnih obremenitvah?

Poslovni subjekti lahko uporabijo več pristopov, da dobijo rezultate, ki jih potrebujejo od LLM. Pri uvajanju LLM v produkciji lahko izbirate med različnimi vrstami modelov z različnimi stopnjami učenja, z različnimi stopnjami zapletenosti, stroškov in kvalitete. Tukaj je nekaj različnih pristopov:

- **Inženiring pozivov s kontekstom**. Ideja je zagotoviti dovolj konteksta ob pozivu, da dobite potrebne odgovore.

- **Retrieval Augmented Generation, RAG**. Vaši podatki so lahko na primer v podatkovni bazi ali spletnem končnem točki, da zagotovite, da so ti podatki ali njihov del vključeni ob pozivu, lahko pridobite relevantne podatke in jih vključite v poziv uporabnika.

- **Fine-tunani model**. Tukaj nadalje usposobite model na lastnih podatkih, kar naredi model natančnejši in bolj odziven na vaše potrebe, vendar je lahko stroškovno zahtevno.

![LLMs deployment](../../../translated_images/sl/Deploy.18b2d27412ec8c02.webp)

Vir slike: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Inženiring pozivov s kontekstom

Predhodno usposobljeni LLM zelo dobro delujejo pri splošnih nalogah naravnega jezika, tudi z zelo kratkim pozivom, kot je poved za dokončanje ali vprašanje – t.i. “zero-shot” učenje.

Vendar pa, bolj ko lahko uporabnik oblikuje svoje vprašanje, z natančnim zahtevkom in primeri – Kontekst – bolj natančen in bližje pričakovanjem uporabnika bo odgovor. V tem primeru govorimo o “one-shot” učenju, če poziv vključuje samo en primer, in “few-shot learning”, če vključuje več primerov.
Inženiring pozivov s kontekstom je najbolj stroškovno učinkovit pristop za začetek.

### Retrieval Augmented Generation (RAG)

LLM imajo omejitev, da lahko uporabijo samo podatke, ki so bili uporabljeni med njihovim učenjem za generiranje odgovora. To pomeni, da ne poznajo dejstev, ki so se zgodila po njihovem učnem procesu, in nimajo dostopa do ne-javnih informacij (kot so podatki podjetja).
To je mogoče premagati z RAG, tehniko, ki poziv dopolnjuje z zunanjimi podatki v obliki kosov dokumentov, ob upoštevanju omejitev dolžine poziva. To podpirajo orodja za vektorsko iskanje (kot je [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)), ki poiščejo koristne kose iz različnih vnaprej določenih virov podatkov in jih dodajo v kontekst poziva.

Ta tehnika je zelo uporabna, kadar poslovni subjekt nima dovolj podatkov, časa ali sredstev za fine-tuning LLM, vendar želi izboljšati zmogljivost pri specifični delovni obremenitvi in zmanjšati tveganja zaradi haluciniranih, zastarelih ali nepodprtih odgovorov.

### Fine-tunani model

Fine-tuning je proces, ki izkorišča prenosno učenje za ‘prilagoditev’ modela določeni nalogi ali reševanju specifičnega problema. V nasprotju z few-shot učenjem in RAG, vodi v ustvarjanje novega modela z posodobljenimi utežmi in pristranskostmi. Zahteva niz učnih primerov, ki sestojijo iz enega vhoda (poziva) in pripadajočega izhoda (dopolnitve).
To bi bil prednostni pristop, če:

- **Uporabljate manjše modele, specifične za naloge**. Poslovni subjekt bi raje fine-tunal manjši model za ozko nalogo namesto ponavljajoče uporabe večjega modela roba, kar prinaša bolj stroškovno učinkovito in hitrejšo rešitev.

- **Upoštevate latenco**. Latenca je pomembna za določen primer uporabe, zato ni mogoče uporabiti zelo dolgih pozivov ali števila primerov, ki bi se morali naučiti iz modela, ni skladno z omejitvijo dolžine poziva.

- **Prilagajate stabilno vedenje**. Poslovni subjekt ima veliko kakovostnih primerov in želi, da model dosledno sledi vzorcu naloge, formatu izhoda, tonu ali domensko-specifičnemu slogu. Če je glavni problem sveža dejstva ali zasebno znanje, ki se pogosto spreminja, raje uporabite RAG kot se zanašajte samo na fine-tuning.

### Usposobljeni model

Usposabljanje LLM od začetka je brez dvoma najbolj zahtevna in najsložitnejša pot, ki zahteva ogromne količine podatkov, usposobljene vire in primerno računsko moč. To možnost je smiselno razmisliti le v scenariju, kjer ima poslovni subjekt domeno-specifičen primer uporabe in veliko količino domeno-centriranih podatkov.

## Preverjanje znanja

Kaj bi bil dober pristop za izboljšanje rezultatov dokončanja LLM?

1. Inženiring pozivov s kontekstom
1. RAG
1. Fine-tunani model

A: Vsi trije lahko pomagajo. Začnite z inženiringom pozivov in kontekstom za hitre izboljšave ter uporabite RAG, ko model potrebuje aktualna dejstva ali zasebne poslovne podatke. Izberite fine-tuning, ko imate dovolj kakovostnih primerov in potrebujete, da model dosledno sledi nalogi, formatu, tonu ali domenskemu vzorcu.

## 🚀 Izziv

Preberite več o tem, kako lahko [uporabite RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) za vaše podjetje.

## Odlično delo, nadaljujte z učenjem

Po zaključku tega poglavja si oglejte našo [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadaljujete z nadgrajevanjem znanja o generativni AI!

Pojdite na Lekcijo 3, kjer bomo raziskali, kako [graditi z Generativno AI odgovorno](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->