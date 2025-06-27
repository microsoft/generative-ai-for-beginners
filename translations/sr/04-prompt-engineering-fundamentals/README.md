<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-06-25T13:33:06+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "sr"
}
-->
# Основе Инжењеринга Промпта

## Увод
Овај модул обухвата основне концепте и технике за креирање ефикасних промпта у моделима генеративне вештачке интелигенције. Начин на који пишете свој промпт за LLM је такође важан. Пажљиво осмишљен промпт може постићи бољи квалитет одговора. Али шта тачно значе термини као што су _промпт_ и _инжењеринг промпта_? И како да побољшам _улазни промпт_ који шаљем LLM-у? Ово су питања на која ћемо покушати да одговоримо у овом и наредном поглављу.

_Генеративна вештачка интелигенција_ је способна да ствара нови садржај (нпр. текст, слике, звук, код итд.) као одговор на захтеве корисника. Ово постиже коришћењем _великих језичких модела_ као што је серија OpenAI GPT ("Генеративни унапред обучени трансформер") који су обучени за коришћење природног језика и кода.

Корисници сада могу да комуницирају са овим моделима користећи познате парадигме као што је ћаскање, без потребе за било каквом техничком експертизом или обуком. Модели су _засновани на промптовима_ - корисници шаљу текстуални улаз (промпт) и добијају одговор вештачке интелигенције (комплетирање). Затим могу "ћаскати са вештачком интелигенцијом" итеративно, у разговорима са више потеза, префињавајући свој промпт док одговор не одговара њиховим очекивањима.

"Промптови" сада постају примарни _програмски интерфејс_ за генеративне AI апликације, говорећи моделима шта да раде и утичући на квалитет враћених одговора. "Инжењеринг промпта" је брзо растуће поље студија које се фокусира на _дизајн и оптимизацију_ промптова како би се испоручили доследни и квалитетни одговори у великом обиму.

## Циљеви учења

У овој лекцији научићемо шта је инжењеринг промпта, зашто је важан и како можемо креирати ефикасније промптове за дати модел и циљ апликације. Разумећемо основне концепте и најбоље праксе за инжењеринг промпта - и научити о интерактивном окружењу "sandbox" у Jupyter Notebooks где можемо видети како се ови концепти примењују на стварне примере.

До краја ове лекције моћи ћемо да:

1. Објаснимо шта је инжењеринг промпта и зашто је важан.
2. Опиšемо компоненте промпта и како се користе.
3. Научимо најбоље праксе и технике за инжењеринг промпта.
4. Применимо научене технике на стварне примере, користећи OpenAI крајњу тачку.

## Кључни термини

Инжењеринг промпта: Практика дизајнирања и префињавања улаза како би се усмерили AI модели ка производњи жељених излаза.
Токенизација: Процес претварања текста у мање јединице, зване токени, које модел може разумети и обрадити.
Инструкцијски подешени LLM-ови: Велики језички модели (LLM-ови) који су фино подешени са специфичним инструкцијама како би побољшали тачност и релевантност њихових одговора.

## Окружење за учење

Инжењеринг промпта је тренутно више уметност него наука. Најбољи начин да побољшамо интуицију за то је да _више вежбамо_ и усвојимо приступ покушаја и грешке који комбинује експертизу у домену апликације са препорученим техникама и оптимизацијама специфичним за модел.

Jupyter Notebook који прати ову лекцију пружа _sandbox_ окружење где можете испробати оно што учите - како идете или као део изазова кодирања на крају. За извршавање вежби биће вам потребно:

1. **Azure OpenAI API кључ** - крајња тачка услуге за распоређени LLM.
2. **Python Runtime** - у којем се Notebook може извршити.
3. **Локалне променљиве окружења** - _завршите кораке [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) сада да бисте се припремили_.

Notebook долази са _почетним_ вежбама - али се охрабрујете да додате своје _Markdown_ (опис) и _Code_ (захтеви промпта) секције да испробате више примера или идеја - и изградите своју интуицију за дизајн промпта.

## Илустровани водич

Желите да добијете целокупну слику о томе шта ова лекција покрива пре него што се упустите у њу? Погледајте овај илустровани водич, који вам даје осећај главних тема које се покривају и кључних закључака о којима треба размишљати у свакој од њих. Мапа лекције вас води од разумевања основних концепата и изазова до њиховог решавања са релевантним техникама инжењеринга промпта и најбољим праксама. Имајте на уму да се одељак "Напредне технике" у овом водичу односи на садржај покривен у _следећем_ поглављу овог курикулума.

## Наша стартап компанија

Сада, хајде да разговарамо о томе како _ова тема_ се односи на нашу стартап мисију да [донесемо иновације вештачке интелигенције у образовање](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Желимо да изградимо AI-покретане апликације за _персонализовано учење_ - па хајде да размислимо о томе како различити корисници наше апликације могу "дизајнирати" промптове:

- **Администратори** могу тражити од AI да _анализира податке о наставном плану и програму како би идентификовао празнине у покривености_. AI може сумирати резултате или их визуализовати помоћу кода.
- **Едукатори** могу тражити од AI да _генерише план лекције за циљну публику и тему_. AI може изградити персонализовани план у одређеном формату.
- **Студенти** могу тражити од AI да их _поуке у тешком предмету_. AI сада може водити студенте са лекцијама, саветима и примерима прилагођеним њиховом нивоу.

То је само врх леденог брега. Погледајте [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - библиотеку отвореног кода за промптове коју су курирали стручњаци за образовање - да бисте добили шири осећај могућности! _Пробајте да покренете неке од тих промптова у sandbox-у или користећи OpenAI Playground да видите шта се дешава!_

## Шта је инжењеринг промпта?

Почели смо ову лекцију дефинисањем **инжењеринга промпта** као процеса _дизајнирања и оптимизације_ текстуалних улаза (промптова) како би се испоручили доследни и квалитетни одговори (комплетирања) за дати циљ апликације и модел. Можемо размишљати о овоме као о процесу у 2 корака:

- _дизајнирање_ почетног промпта за дати модел и циљ
- _префињавање_ промпта итеративно како би се побољшао квалитет одговора

Ово је нужно процес покушаја и грешке који захтева интуицију корисника и труд да би се постигли оптимални резултати. Зашто је то важно? Да бисмо одговорили на то питање, прво морамо разумети три концепта:

- _Токенизација_ = како модел "види" промпт
- _Основни LLM-ови_ = како основни модел "обрађује" промпт
- _Инструкцијски подешени LLM-ови_ = како модел сада може видети "задатке"

### Токенизација

LLM види промптове као _секвенцу токена_ где различити модели (или верзије модела) могу токенизовати исти промпт на различите начине. Пошто су LLM-ови обучени на токенима (а не на сировом тексту), начин на који се промптови токенизују има директан утицај на квалитет генерисаног одговора.

Да бисте стекли интуицију о томе како токенизација функционише, испробајте алате као што је [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) приказан испод. Копирајте свој промпт - и видите како се он претвара у токене, обраћајући пажњу на то како се обрађују знакови белине и знакови интерпункције. Имајте на уму да овај пример приказује старији LLM (GPT-3) - тако да покушај са новијим моделом може произвести другачији резултат.

### Концепт: Основни модели

Када је промпт токенизован, примарна функција ["Основног LLM-а"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (или основног модела) је да предвиди токен у тој секвенци. Пошто су LLM-ови обучени на масивним текстуалним скуповима података, они имају добар осећај за статистичке односе између токена и могу направити то предвиђање са одређеним степеном сигурности. Имајте на уму да не разумеју _значење_ речи у промпту или токену; они само виде образац који могу "завршити" својим следећим предвиђањем. Могу наставити да предвиђају секвенцу све док их не прекине корисник или неки унапред утврђени услов.

Желите да видите како функционише комплетирање засновано на промпту? Унесите горњи промпт у Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) са подразумеваним подешавањима. Систем је конфигурисан да третира промптове као захтеве за информацијама - тако да би требало да видите комплетирање које задовољава овај контекст.

Али шта ако корисник жели да види нешто специфично што испуњава неке критеријуме или циљ задатка? Овде у слику долазе _инструкцијски подешени_ LLM-ови.

### Концепт: Инструкцијски подешени LLM-ови

[Инструкцијски подешени LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) почиње са основним моделом и фино га подешава примерима или паровима улаз/излаз (нпр. порукама са више потеза) који могу садржати јасне инструкције - а одговор AI покушава да следи ту инструкцију.

Ово користи технике као што је учење појачања са повратним информацијама од људи (RLHF) које могу обучити модел да _следи инструкције_ и _учи из повратних информација_ тако да производи одговоре који су боље прилагођени практичним апликацијама и релевантнији за циљеве корисника.

Хајде да испробамо - поново погледајте горњи промпт, али сада промените _системску поруку_ да пружи следећу инструкцију као контекст:

> _Сумирајте садржај који вам је дат за ученика другог разреда. Држите резултат у једном пасусу са 3-5 тачака._

Видите како је резултат сада подешен да одражава жељени циљ и формат? Едукатор сада може директно користити овај одговор у својим слајдовима за ту класу.

## Зашто нам је потребан инжењеринг промпта?

Сада када знамо како LLM-ови обрађују промптове, хајде да разговарамо о _зашто_ нам је потребан инжењеринг промпта. Одговор лежи у чињеници да тренутни LLM-ови представљају низ изазова који чине _поуздана и доследна комплетирања_ изазовнијим за постизање без улагања напора у конструкцију и оптимизацију промпта. На пример:

1. **Одговори модела су стохастички.** _Исти промпт_ ће вероватно произвести различите одговоре са различитим моделима или верзијама модела. И може чак произвести различите резултате са _истим моделом_ у различито време. _Технике инжењеринга промпта могу нам помоћи да минимизирамо ове варијације пружањем бољих заштитних мера_.

2. **Модели могу фабриковати одговоре.** Модели су предобучени са _великим али коначним_ скуповима података, што значи да им недостаје знање о концептима изван тог обима обуке. Као резултат, могу произвести комплетирања која су нетачна, измишљена или директно контрадикторна познатим чињеницама. _Технике инжењеринга промпта помажу корисницима да идентификују и ублаже такве фабрикације нпр. тражењем цитата или размишљања од AI_.

3. **Способности модела ће се разликовати.** Новији модели или генерације модела имаће богатије способности, али такође доносе јединствене чудности и компромисе у погледу трошкова и сложености. _Инжењеринг промпта може нам помоћи да развијемо најбоље праксе и радне токове који апстрахују разлике и прилагођавају се захтевима специфичним за модел на скалабилан, безболан начин_.

Хајде да видимо ово у акцији у OpenAI или Azure OpenAI Playground-у:

- Користите исти промпт са различитим LLM распоређењима (нпр. OpenAI, Azure OpenAI, Hugging Face) - да ли сте видели варијације?
- Користите исти промпт више пута са _истим_ LLM распоређењем (нпр. Azure OpenAI playground) - како су се ове варијације разликовале?

### Пример фабрикација

У овом курсу користимо термин **"фабрикација"** да се односимо на феномен где LLM-ови понекад генеришу фактички нетачне информације због ограничења у својој обуци или другим ограничењима. Можда сте такође чули да се ово назива _"халуцинације"_ у популарним чланцима или истраж
Na kraju, prava vrednost šablona leži u sposobnosti da se kreiraju i objavljuju _biblioteke promptova_ za vertikalne domene primene - gde je šablon prompta sada _optimizovan_ da odražava kontekst specifičan za aplikaciju ili primere koji čine odgovore relevantnijim i tačnijim za ciljanu korisničku publiku. Repozitorijum [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) je odličan primer ovog pristupa, koji kurira biblioteku promptova za obrazovni domen sa naglaskom na ključne ciljeve kao što su planiranje lekcija, dizajn kurikuluma, podučavanje učenika itd.

## Podrška sadržaju

Ako razmišljamo o konstrukciji prompta kao o zadatku (task) i cilju (primarni sadržaj), onda je _sekundarni sadržaj_ kao dodatni kontekst koji pružamo da **na neki način utičemo na ishod**. To mogu biti parametri podešavanja, uputstva za formatiranje, taksonomije tema itd. koji mogu pomoći modelu da _prilagodi_ svoj odgovor da bude u skladu sa željenim korisničkim ciljevima ili očekivanjima.

Na primer: Dati katalog kurseva sa opsežnim metapodacima (ime, opis, nivo, metapodaci, predavač itd.) o svim dostupnim kursevima u kurikulumu:

- možemo definisati instrukciju da "sumiramo katalog kurseva za jesen 2023."
- možemo koristiti primarni sadržaj da pružimo nekoliko primera željenog ishoda
- možemo koristiti sekundarni sadržaj da identifikujemo 5 najvažnijih "tagova" od interesa.

Sada model može pružiti sažetak u formatu prikazanom kroz nekoliko primera - ali ako rezultat ima više tagova, može dati prioritet 5 tagova identifikovanih u sekundarnom sadržaju.

---

<!--
ŠABLON LEKCIJE:
Ova jedinica treba da pokrije osnovni koncept #1.
Pojačajte koncept primerima i referencama.

KONCEPT #3:
Tehnike inženjeringa promptova.
Koje su osnovne tehnike za inženjering promptova?
Ilustrujte to sa nekim vežbama.
-->

## Najbolje prakse za prompting

Sada kada znamo kako se promptovi mogu _konstruisati_, možemo početi da razmišljamo o tome kako ih _dizajnirati_ da odražavaju najbolje prakse. O tome možemo razmišljati u dva dela - imati pravi _mentalitet_ i primeniti prave _tehnike_.

### Mentalitet inženjeringa promptova

Inženjering promptova je proces pokušaja i greške, pa imajte na umu tri široka faktora:

1. **Razumevanje domena je važno.** Tačnost i relevantnost odgovora je funkcija _domena_ u kojem ta aplikacija ili korisnik deluje. Primeni svoju intuiciju i stručnost iz domena da **dalje prilagodiš tehnike**. Na primer, definiši _ličnosti specifične za domen_ u svojim sistemskim promptovima ili koristi _šablone specifične za domen_ u korisničkim promptovima. Pruži sekundarni sadržaj koji odražava kontekste specifične za domen, ili koristi _signale i primere specifične za domen_ da vodiš model ka poznatim obrascima korišćenja.

2. **Razumevanje modela je važno.** Znamo da su modeli stohastički po prirodi. Ali implementacije modela takođe mogu varirati u smislu skupa podataka za obuku koji koriste (predznanje), sposobnosti koje pružaju (npr. putem API-ja ili SDK-a) i tipa sadržaja za koji su optimizovani (npr. kod protiv slike protiv teksta). Razumite snage i ograničenja modela koji koristite i iskoristite to znanje da _prioritizujete zadatke_ ili izgradite _prilagođene šablone_ koji su optimizovani za sposobnosti modela.

3. **Iteracija i validacija su važni.** Modeli se brzo razvijaju, kao i tehnike za inženjering promptova. Kao stručnjak za domen, možda imate drugi kontekst ili kriterijume _vaše_ specifične aplikacije, koji možda ne važe za širu zajednicu. Koristite alate i tehnike inženjeringa promptova da "ubrzate" konstrukciju prompta, zatim iterirajte i validirajte rezultate koristeći svoju intuiciju i stručnost iz domena. Zabeležite svoja saznanja i kreirajte **bazu znanja** (npr. biblioteke promptova) koja može poslužiti kao nova osnova za druge, za brže iteracije u budućnosti.

## Najbolje prakse

Sada ćemo pogledati uobičajene najbolje prakse koje preporučuju praktikanti [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) i [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Šta                              | Zašto                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Evaluirajte najnovije modele.       | Nove generacije modela verovatno imaju poboljšane funkcije i kvalitet - ali mogu imati i veće troškove. Evaluirajte ih za uticaj, a zatim donesite odluke o migraciji.                                                                                |
| Razdvojite instrukcije i kontekst   | Proverite da li vaš model/provajder definiše _delimitere_ za jasnije razlikovanje instrukcija, primarnog i sekundarnog sadržaja. Ovo može pomoći modelima da tačnije dodeljuju težine tokenima.                                                         |
| Budite specifični i jasni             | Dajte više detalja o željenom kontekstu, ishodu, dužini, formatu, stilu itd. Ovo će poboljšati i kvalitet i doslednost odgovora. Zabeležite recepte u ponovo upotrebljivim šablonima.                                                          |
| Budite opisni, koristite primere      | Modeli mogu bolje odgovoriti na pristup "pokaži i reci". Počnite sa `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
| Use cues to jumpstart completions | Nudge it towards a desired outcome by giving it some leading words or phrases that it can use as a starting point for the response.                                                                                                               |
| Double Down                       | Sometimes you may need to repeat yourself to the model. Give instructions before and after your primary content, use an instruction and a cue, etc. Iterate & validate to see what works.                                                         |
| Order Matters                     | The order in which you present information to the model may impact the output, even in the learning examples, thanks to recency bias. Try different options to see what works best.                                                               |
| Give the model an “out”           | Give the model a _fallback_ completion response it can provide if it cannot complete the task for any reason. This can reduce chances of models generating false or fabricated responses.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

As with any best practice, remember that _your mileage may vary_ based on the model, the task and the domain. Use these as a starting point, and iterate to find what works best for you. Constantly re-evaluate your prompt engineering process as new models and tools become available, with a focus on process scalability and response quality.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Assignment

Congratulations! You made it to the end of the lesson! It's time to put some of those concepts and techniques to the test with real examples!

For our assignment, we'll be using a Jupyter Notebook with exercises you can complete interactively. You can also extend the Notebook with your own Markdown and Code cells to explore ideas and techniques on your own.

### To get started, fork the repo, then

- (Recommended) Launch GitHub Codespaces
- (Alternatively) Clone the repo to your local device and use it with Docker Desktop
- (Alternatively) Open the Notebook with your preferred Notebook runtime environment.

### Next, configure your environment variables

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` vrednostima. Vratite se na [odsek za učenje Sandbox](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) da naučite kako.

### Sledeće, otvorite Jupyter beležnicu

- Izaberite runtime kernel. Ako koristite opcije 1 ili 2, jednostavno izaberite podrazumevani Python 3.10.x kernel koji pruža dev container.

Spremni ste da pokrenete vežbe. Imajte na umu da ovde nema _pravih i pogrešnih_ odgovora - samo istražujemo opcije putem pokušaja i grešaka i gradimo intuiciju za ono što radi za dati model i domen primene.

_Iz tog razloga, u ovoj lekciji nema segmenata Rešenja koda. Umesto toga, beležnica će imati Markdown ćelije naslovljene "Moje rešenje:" koje prikazuju jedan primer izlaza za referencu._

 <!--
ŠABLON LEKCIJE:
Zaključite odeljak sa rezimeom i resursima za samostalno učenje.
-->

## Provera znanja

Koji od sledećih je dobar prompt prateći neke razumne najbolje prakse?

1. Pokaži mi sliku crvenog automobila
2. Pokaži mi sliku crvenog automobila marke Volvo i modela XC90 parkiranog pored litice sa zalaskom sunca
3. Pokaži mi sliku crvenog automobila marke Volvo i modela XC90

A: 2, to je najbolji prompt jer pruža detalje o "čemu" i ide u specifičnosti (ne samo bilo koji automobil već specifična marka i model) i takođe opisuje celokupno okruženje. 3 je sledeći najbolji jer takođe sadrži mnogo opisa.

## 🚀 Izazov

Pogledajte možete li iskoristiti tehniku "signala" sa promptom: Dovršite rečenicu "Pokaži mi sliku crvenog automobila marke Volvo i ". Kako odgovara i kako biste ga poboljšali?

## Odličan rad! Nastavite sa učenjem

Želite da saznate više o različitim konceptima inženjeringa promptova? Idite na [stranicu za nastavak učenja](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) da pronađete druge sjajne resurse na ovu temu.

Pređite na Lekciju 5 gde ćemo pogledati [napredne tehnike promptovanja](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо ка тачности, молимо вас да будете свесни да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације, препоручује се професионални превод од стране људског преводиоца. Не сносимо одговорност за било каква погрешна тумачења или неразумевања настала коришћењем овог превода.