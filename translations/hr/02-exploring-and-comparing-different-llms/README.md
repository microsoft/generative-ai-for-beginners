# Istraživanje i usporedba različitih LLM-ova

[![Istraživanje i usporedba različitih LLM-ova](../../../translated_images/hr/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Kliknite na sliku iznad za prikaz videozapisa ove lekcije_

U prethodnoj lekciji vidjeli smo kako Generativna AI mijenja tehnološki krajolik, kako rade veliki jezični modeli (LLM) i kako ih posao - poput naše start-up tvrtke - može primijeniti na svoje slučajeve korištenja i rasti! U ovom poglavlju želimo usporediti i kontrastirati različite vrste velikih jezičnih modela (LLM) kako bismo razumjeli njihove prednosti i nedostatke.

Sljedeći korak u putovanju našeg startupa je istraživanje trenutnog krajolika LLM-ova i razumijevanje koji su prikladni za naš slučaj upotrebe.

## Uvod

Ova lekcija će obuhvatiti:

- Različite vrste LLM-ova u trenutnom krajoliku.
- Testiranje, iteraciju i usporedbu različitih modela za vaš slučaj upotrebe u Azure-u.
- Kako postaviti LLM.

## Ciljevi učenja

Nakon završetka ove lekcije moći ćete:

- Odabrati pravi model za vaš slučaj upotrebe.
- Razumjeti kako testirati, iterirati i poboljšati performanse vašeg modela.
- Znati kako tvrtke postavljaju modele.

## Razumjeti različite vrste LLM-ova

LLM-ovi se mogu kategorizirati na više načina, ovisno o njihovoj arhitekturi, podacima za treniranje i svrsi uporabe. Razumijevanje ovih razlika pomoći će našem startupu odabrati pravi model za scenarij i shvatiti kako testirati, iterirati i poboljšati performanse.

Postoji mnogo različitih vrsta LLM modela, vaš izbor modela ovisi o tome za što ih namjeravate koristiti, vašim podacima, koliko ste spremni platiti i više.

Ovisno o tome želite li koristiti modele za tekst, audio, video, generiranje slika i slično, možda ćete odabrati drugačiju vrstu modela.

- **Audio i prepoznavanje govora**. Whisper-stil modeli još uvijek su korisni općeniti modeli za prepoznavanje govora, ali produkcijski izbori sada uključuju i novije modele za govor u tekst kao što su `gpt-4o-transcribe`, `gpt-4o-mini-transcribe` i varijante za diarizaciju. Procijenite pokrivenost jezika, diarizaciju, podršku u stvarnom vremenu, latenciju i troškove za vaš scenarij. Saznajte više u [OpenAI dokumentaciji za govor u tekst](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst).

- **Generiranje slika**. DALL-E i Midjourney su poznate opcije za generiranje slika, ali trenutni OpenAI API za slike fokusira se na GPT Image modele poput `gpt-image-2`, dok su Stable Diffusion, Imagen, Flux i druge obitelji modela također česti izbori. Usporedite pridržavanje upita, podršku za uređivanje, kontrolu stila, sigurnosne zahtjeve i licenciranje. Naučite više u [OpenAI vodiču za generiranje slika](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) i Poglavlju 9 ovog kurikuluma.

- **Generiranje teksta**. Tekstualni modeli sada uključuju najnovije modele, modele za rezoniranje, manje niskolatencijske modele i otvorene modele s otvorenim težinama. Trenutni primjeri uključuju OpenAI GPT-5.x modele, Anthropic Claude 4.x modele, Google Gemini 3.x modele, Meta Llama 4 modele i Mistral modele. Nemojte birati isključivo po datumu izdanja ili cijeni; usporedite kvalitetu zadataka, latenciju, kontekstni prozor, korištenje alata, sigurnosno ponašanje, regionalnu dostupnost i ukupne troškove. [Microsoft Foundry katalog modela](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) je dobro mjesto za usporedbu modela dostupnih na Azure-u.

- **Višemodalnost**. Mnogi trenutačni modeli mogu obrađivati više od teksta. Neki prihvaćaju slike, audio ili video ulaze; neki mogu pozivati alate; a specijalizirani modeli mogu generirati slike, audio ili video. Na primjer, trenutačni OpenAI modeli podržavaju unos teksta i slike, Gemini modeli mogu podržavati unos teksta, koda, slike, zvuka i videa ovisno o varijanti, a Llama 4 Scout i Maverick su modeli s otvorenim težinama koji su izvorno višemodalni. Uvijek provjerite svaku karticu modela za podržane ulazne i izlazne modalitete prije nego što izgradite radni tijek oko njih.

Odabirom modela dobivate osnovne mogućnosti koje možda nisu dovoljne. Često imate podatke specifične za tvrtku koje morate na neki način prenijeti LLM-u. Postoji nekoliko različitih pristupa tome, a više o tome slijedi u nadolazećim odjeljcima.

### Temeljni modeli nasuprot LLM-ovima

Pojam Temeljni model (Foundation Model) [skovala su istraživači sa Stanforda](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) i definiran je kao AI model koji zadovoljava određene kriterije, poput:

- **Treniraju se korištenjem neneziranog učenja ili samo-nadziranog učenja**, što znači da su trenirani na nelabeliranim višemodalnim podacima i ne zahtijevaju ljudsku anotaciju ili označavanje podataka tijekom procesa treniranja.
- **Vrlo su veliki modeli**, bazirani na vrlo dubokim neuronskim mrežama treniranim na milijardama parametara.
- **Obično služe kao ‘temelj’ za izgradnju drugih modela**, što znači da se mogu koristiti kao polazna osnova za izgradnju drugih modela, što se može postići finim podešavanjem.

![Temeljni modeli nasuprot LLM-ovima](../../../translated_images/hr/FoundationModel.e4859dbb7a825c94.webp)

Izvor slike: [Essential Guide to Foundation Models and Large Language Models | by Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Da dodatno pojasnimo ovu razliku, uzmimo ChatGPT kao povijesni primjer. Rane verzije ChatGPT-a koristile su GPT-3.5 kao temeljni model. OpenAI je zatim koristio podatke specifične za chat i tehnike usklađivanja kako bi stvorio podešenu verziju koja bolje funkcionira u konverzacijskim scenarijima, poput chatbota. Moderni AI servisi često preusmjeravaju pozive između nekoliko varijanti modela, pa ime servisa i osnovni model nisu uvijek ista stvar.

![Temeljni model](../../../translated_images/hr/Multimodal.2c389c6439e0fc51.webp)

Izvor slike: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Otvoreni modeli s otvorenim težinama naspram vlasničkih modela

Još jedan način kategorizacije LLM-ova je jesu li modeli otvorenih težina, otvorenog koda ili vlasnički.

Otvoreni modeli i modeli s otvorenim težinama omogućuju pregledavanje, preuzimanje ili prilagodbu artefakata modela, ali njihove licence se razlikuju. Neki su potpuno otvoreni izvor, dok su drugi otvoreni modeli s ograničenjima korištenja. Korisni su kad posao treba veću kontrolu nad postavljanjem, lokalizacijom podataka, troškovima ili prilagodbom. Međutim, timovi još uvijek moraju pregledati uvjete licenciranja, troškove poslužitelja, održavanje, sigurnosna ažuriranja i kvalitetu evaluacije prije upotrebe u produkciji. Primjeri uključuju [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst), neke [Mistral modele](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst) i mnoge modele hostane na [Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst).

Vlasnički modeli su u vlasništvu i hostani od strane pružatelja usluga. Ti su modeli često optimizirani za upravljanje produkcijskom uporabom i mogu nuditi snažnu podršku, sigurnosne sustave, integraciju alata i skalabilnost. Međutim, korisnici obično ne mogu pregledavati ili modificirati težine modela i moraju pregledati uvjete pružatelja za privatnost, zadržavanje, usklađenost i prihvatljivu upotrebu. Primjeri uključuju [OpenAI modele](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), [Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst) i [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst).

### Generiranje ugrađenih značajki naspram generiranje slika naspram generiranja teksta i koda

LLM-ove također možemo kategorizirati prema izlazu koji generiraju.

Ugrađene značajke su skup modela koji mogu pretvoriti tekst u numerički oblik, nazvan embedding, što je numerički prikaz ulaznog teksta. Embedding modeli olakšavaju strojevima razumijevanje odnosa između riječi ili rečenica i mogu se koristiti kao ulazi za druge modele, poput modela za klasifikaciju ili modele za grupiranje koji bolje funkcioniraju na numeričkim podacima. Embedding modeli se često koriste za prijenos učenja, gdje se model gradi za zadatak za koji postoji obilje podataka, a zatim se težine modela (embedding) ponovno koriste za druge zadatke. Primjer ove kategorije su [OpenAI embeddings](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Ugrađene značajke](../../../translated_images/hr/Embedding.c3708fe988ccf760.webp)

Modeli za generiranje slika su modeli koji generiraju slike. Ti se modeli često koriste za uređivanje slika, sintezu slika i prijevod slika. Modeli za generiranje slika često se treniraju na velikim skupovima podataka slika, poput [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), i mogu se koristiti za generiranje novih slika ili za uređivanje postojećih slika tehnikama poput inpainting, super rezolucije i koloriranja. Primjeri uključuju [GPT Image modele](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst), [Stable Diffusion modele](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst) i Imagen modele.

![Generiranje slika](../../../translated_images/hr/Image.349c080266a763fd.webp)

Modeli za generiranje teksta i koda su modeli koji generiraju tekst ili kod. Ti modeli se često koriste za sažimanje teksta, prevođenje i odgovaranje na pitanja. Modeli za generiranje teksta često se treniraju na velikim skupovima tekstualnih podataka, poput [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), i mogu se koristiti za generiranje novog teksta ili za odgovore na pitanja. Modeli za generiranje koda, poput [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), često se treniraju na velikim skupovima podataka koda, poput GitHuba, i mogu se koristiti za generiranje novog koda ili za ispravljanje pogrešaka u postojećem kodu.

![Generiranje teksta i koda](../../../translated_images/hr/Text.a8c0cf139e5cc2a0.webp)

### Encoder-Decoder naspram samo Decoder

Za razgovor o različitim vrstama arhitektura LLM-ova, upotrijebimo analogiju.

Zamislite da vam je upravitelj dao zadatak da napišete kviz za studente. Imate dvoje kolega; jedan nadzire izradu sadržaja, a drugi pregled njihovih odgovora.

Tvorac sadržaja je poput modela samo s decoderom: može gledati temu, vidjeti što ste već napisali i potom nastaviti generirati sadržaj na temelju tog konteksta. Vrlo su dobri u pisanju zanimljivog i informativnog sadržaja, ali nisu uvijek najbolji izbor kada je zadatak samo klasifikacija, dohvat ili kodiranje informacija. Primjeri modela samo s decoderom uključuju GPT i Llama modele.

Preglednik je poput modela samo s encoderom, gleda napisani sadržaj i odgovore, primjećujući odnos između njih i razumijevajući kontekst, ali nije dobar u generiranju sadržaja. Primjer modela samo s encoderom bio bi BERT.

Zamislite da također možemo imati nekoga tko bi mogao i stvarati i pregledavati kviz, to je model Encoder-Decoder. Neki primjeri su BART i T5.

### Usluga naspram modela

Sada, razgovarajmo o razlici između usluge i modela. Usluga je proizvod koji nudi pružatelj usluga u oblaku i često je kombinacija modela, podataka i drugih komponenti. Model je temeljna komponenta usluge i često je temeljni model, poput LLM-a.

Usluge su često optimizirane za produkcijsku uporabu i često su lakše za korištenje nego modeli, putem grafičkog korisničkog sučelja. Međutim, usluge nisu uvijek besplatne i mogu zahtijevati pretplatu ili plaćanje za korištenje, u zamjenu za korištenje opreme i resursa vlasnika usluge, optimizaciju troškova i lako skaliranje. Primjer usluge je [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), koji nudi model plaćanja po korištenju, što znači da korisnici plaćaju proporcionalno koliko koriste uslugu. Azure OpenAI Service također nudi sigurnost na razini poduzeća i okvir odgovorne AI na vrhu mogućnosti modela.

Modeli su neuronske mreže: parametri, težine, arhitektura, tokenizer i pripadajuća konfiguracija. Pokretanje modela lokalno ili u privatnom okruženju zahtijeva odgovarajuću hardversku infrastrukturu, infrastrukturu za serviranje, nadzor i kompatibilnu open-source/open-weight licencu ili komercijalnu licencu. Otvoreni modeli poput Llama 4 ili Mistral modela mogu se samostalno hostati, ali i dalje zahtijevaju računalnu snagu i operativnu stručnost.

## Kako testirati i iterirati s različitim modelima za razumijevanje performansi na Azure-u


Nakon što je naš tim istražio trenutni krajolik LLM-ova i identificirao nekoliko dobrih kandidata za njihove scenarije, sljedeći korak je testiranje na njihovim podacima i radnim opterećenjima. To je iterativni proces, proveden eksperimentima i mjerama.
Većina modela o kojima smo govorili u prethodnim odlomcima (OpenAI modeli, modeli s otvorenim težinama poput Llama 4 i Mistral, te Hugging Face modeli) dostupni su u [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst).

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst), prethodno Azure AI Studio/Azure AI Foundry, jedinstvena je Azure platforma za izgradnju AI aplikacija i agenata. Pomaže programerima upravljati životnim ciklusom od eksperimentiranja i evaluacije do implementacije, nadzora i upravljanja. Katalog modela u Microsoft Foundry omogućuje korisniku:

- Pronalaženje temeljnih modela od interesa u katalogu, uključujući modele koje prodaje Azure i modele partnera i pružatelja iz zajednice. Korisnici mogu filtrirati po zadatku, pružatelju, licenci, opciji implementacije ili imenu.

![Model catalog](../../../translated_images/hr/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- Pregled kartice modela, uključujući detaljan opis namjeravane upotrebe i podataka za treniranje, primjere koda i rezultate evaluacije u internoj biblioteci evaluacija.

![Model card](../../../translated_images/hr/ModelCard.598051692c6e400d.webp)

- Usporedbu referentnih vrijednosti modela i skupova podataka dostupnih u industriji kako bi se procijenilo koji najbolje odgovara poslovnom scenariju, putem [Model Benchmarks](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst) panela.

![Model benchmarks](../../../translated_images/hr/ModelBenchmarks.254cb20fbd06c03a.webp)

- Fino podešavanje podržanih modela na prilagođenim podacima za treniranje radi poboljšanja performansi modela u specifičnom radnom opterećenju, iskorištavajući mogućnosti eksperimentiranja i praćenja Microsoft Foundry-a.

![Model fine-tuning](../../../translated_images/hr/FineTuning.aac48f07142e36fd.webp)

- Implementaciju originalnog prethodno treniranog modela ili verzije s finim podešavanjem na udaljeni krajnji punkt za inferenciju u stvarnom vremenu, koristeći upravljane računalne ili serverless opcije implementacije, kako bi aplikacije mogle koristiti model.

![Model deployment](../../../translated_images/hr/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> Nisu svi modeli u katalogu trenutno dostupni za fino podešavanje i/ili implementaciju po korištenju. Provjerite karticu modela za detalje o mogućnostima i ograničenjima modela.

## Poboljšanje rezultata LLM-a

Istražili smo s našim startup timom različite vrste LLM-ova i cloud platformu (Microsoft Foundry) koja nam omogućuje usporedbu različitih modela, evaluaciju na testnim podacima, poboljšanje performansi i implementaciju na inferencijske krajnje točke.

Ali kada bi trebali razmotriti fino podešavanje modela umjesto upotrebe prethodno treniranog? Postoje li drugi pristupi za poboljšanje performansi modela na specifičnim radnim opterećenjima?

Poslovanje može koristiti nekoliko pristupa da dobije potrebne rezultate od LLM-a. Možete odabrati različite vrste modela s različitim stupnjevima treninga prilikom implementacije LLM-a u produkciji, s različitim razinama složenosti, troškova i kvalitete. Evo nekoliko različitih pristupa:

- **Inženjering upita s kontekstom**. Ideja je pružiti dovoljno konteksta prilikom postavljanja upita kako biste dobili odgovore koji su vam potrebni.

- **Retrieval Augmented Generation, RAG**. Vaši podaci mogu postojati u bazi podataka ili na web endpointu, na primjer, a kako bi se ti podaci ili njihov dio uključili u vrijeme postavljanja upita, možete dohvatiti relevantne podatke i učiniti ih dijelom korisničkog upita.

- **Fino podešeni model**. Ovdje ste dodatno trenirali model na vlastitim podacima što je rezultiralo da model bude precizniji i odgovoreni na vaše potrebe, ali to može biti skupo.

![LLMs deployment](../../../translated_images/hr/Deploy.18b2d27412ec8c02.webp)

Izvor slike: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Inženjering upita s kontekstom

Prethodno trenirani LLM-ovi vrlo dobro rade na općenitim zadacima prirodnog jezika, čak i samo pozivom s kratkim upitom, poput rečenice za dovršavanje ili pitanja – tzv. "zero-shot" učenje.

Međutim, što korisnik više može oblikovati svoj upit, s detaljnim zahtjevom i primjerima – Kontekstom – to će odgovor biti točniji i bliži očekivanjima korisnika. U ovom slučaju govorimo o "one-shot" učenju ako upit sadrži samo jedan primjer i "few-shot" učenju ako uključuje više primjera.
Inženjering upita s kontekstom je najučinkovitiji pristup za početak.

### Retrieval Augmented Generation (RAG)

LLM-ovi imaju ograničenje da mogu koristiti samo podatke koji su korišteni tijekom njihovog treninga za generiranje odgovora. To znači da ne znaju ništa o činjenicama koje su se dogodile nakon procesa treninga i nemaju pristup ne-javnim informacijama (kao što su podaci tvrtke).
To se može nadvladati pomoću RAG tehnike, koja nadopunjuje upit vanjskim podacima u obliku odlomaka dokumenata, uzimajući u obzir ograničenja duljine upita. To podržavaju alati vektorske baze podataka (kao što je [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) koji dohvaćaju korisne odlomke iz raznih unaprijed definiranih izvora podataka i dodaju ih u kontekst upita.

Ova tehnika je vrlo korisna kada poslovanje nema dovoljno podataka, vremena ili resursa za fino podešavanje LLM-a, ali još uvijek želi poboljšati performanse u specifičnom radnom opterećenju i smanjiti rizik od haluciniranih, zastarjelih ili nepodržanih odgovora.

### Fino podešeni model

Fino podešavanje je proces koji koristi transfer učenja za 'prilagodbu' modela za određeni zadatak ili rješavanje specifičnog problema. Za razliku od few-shot učenja i RAG-a, rezultira generiranjem novog modela s ažuriranim težinama i pomacima. Zahtijeva skup primjera za treniranje koji se sastoje od jednog unosa (upita) i njegovog pripadajućeg izlaza (zavrsetka).
Ovo bi bio preferirani pristup ako:

- **Korištenje manjih modela specifičnih za zadatak**. Poslovanje bi htjelo fino podešavati manji model za uski zadatak umjesto ponavljanog postavljanja upita većem modelu, što dovodi do isplativijeg i bržeg rješenja.

- **Uzimajući u obzir latenciju**. Latencija je važna za određeni slučaj upotrebe, pa nije moguće koristiti vrlo dugačke upite ili broj primjera koje model treba naučiti ne odgovara ograničenju duljine upita.

- **Prilagodbu stabilnog ponašanja**. Poslovanje ima mnogo visokokvalitetnih primjera i želi da model dosljedno slijedi obrazac zadatka, format izlaza, ton ili stil specifičan za određenu domenu. Ako je glavni problem svježe činjenice ili privatno znanje koje se često mijenja, koristite RAG umjesto oslanjanja samo na fino podešavanje.

### Treniran model

Treniranje LLM-a od nule je bez sumnje najteži i najsloženiji pristup za usvajanje, zahtijevajući ogromne količine podataka, vješte resurse i prikladnu računalnu snagu. Ova opcija treba se razmotriti samo u scenariju gdje poslovanje ima domensku upotrebu i veliku količinu podatka specifičnog za domenu.

## Provjera znanja

Koji bi bio dobar pristup za poboljšanje rezultata dovršenja LLM-a?

1. Inženjering upita s kontekstom
1. RAG
1. Fino podešeni model

O: Sva tri mogu pomoći. Počnite s inženjeringom upita i kontekstom za brza poboljšanja, te koristite RAG kada model treba aktualne činjenice ili privatne poslovne podatke. Odaberite fino podešavanje kada imate dovoljno visokokvalitetnih primjera i trebate da model dosljedno slijedi zadatak, format, ton ili uzorak domene.

## 🚀 Izazov

Pročitajte više o tome kako možete [koristiti RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) za svoje poslovanje.

## Odličan rad, nastavite s učenjem

Nakon završetka ove lekcije, pogledajte našu [kolekciju za učenje o Generativnoj AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili unapređivati svoje znanje o Generativnoj AI!

Krenite na Lekciju 3 gdje ćemo pogledati kako [izgraditi s Generativnom AI odgovorno](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->