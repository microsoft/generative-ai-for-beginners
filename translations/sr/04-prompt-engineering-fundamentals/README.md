<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0135e6c271f3ece8699050d4debbce88",
  "translation_date": "2025-10-18T01:26:14+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "sr"
}
-->
# Основе инжењеринга упутстава

[![Основе инжењеринга упутстава](../../../translated_images/04-lesson-banner.a2c90deba7fedacda69f35b41636a8951ec91c2e33f5420b1254534ac85bc18e.sr.png)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Увод
Овај модул покрива основне концепте и технике за креирање ефикасних упутстава у моделима генеративне вештачке интелигенције. Начин на који пишете своје упутство за LLM је такође важан. Пажљиво осмишљено упутство може довести до бољег квалитета одговора. Али шта тачно значе термини као што су _упутство_ и _инжењеринг упутстава_? И како могу побољшати _улазно упутство_ које шаљем LLM-у? Ово су питања на која ћемо покушати да одговоримо у овом и наредном поглављу.

_Генеративна вештачка интелигенција_ је способна да креира нови садржај (нпр. текст, слике, аудио, код итд.) као одговор на захтеве корисника. То постиже коришћењем _великих језичких модела_ као што је серија GPT ("Generative Pre-trained Transformer") компаније OpenAI, који су обучени за коришћење природног језика и кода.

Корисници сада могу да комуницирају са овим моделима користећи познате парадигме као што је чет, без потребе за техничком експертизом или обуком. Модели су _засновани на упутствима_ - корисници шаљу текстуални улаз (упутство) и добијају одговор од вештачке интелигенције (завршетак). Затим могу "разговарати са вештачком интелигенцијом" итеративно, у више кругова разговора, усавршавајући своје упутство док одговор не испуни њихова очекивања.

"Упутства" сада постају примарни _програмски интерфејс_ за апликације генеративне вештачке интелигенције, који моделима говори шта да раде и утиче на квалитет добијених одговора. "Инжењеринг упутстава" је брзо растућа област студија која се фокусира на _дизајн и оптимизацију_ упутстава како би се обезбедили конзистентни и квалитетни одговори у великом обиму.

## Циљеви учења

У овој лекцији ћемо научити шта је инжењеринг упутстава, зашто је важан и како можемо креирати ефикаснија упутства за одређени модел и циљ апликације. Разумећемо основне концепте и најбоље праксе за инжењеринг упутстава - и научити о интерактивном окружењу "sandbox" у Jupyter Notebook-у где можемо применити ове концепте на стварним примерима.

На крају ове лекције бићемо у могућности да:

1. Објаснимо шта је инжењеринг упутстава и зашто је важан.
2. Опишемо компоненте упутства и како се користе.
3. Научимо најбоље праксе и технике за инжењеринг упутстава.
4. Применимо научене технике на стварним примерима, користећи OpenAI endpoint.

## Кључни термини

Инжењеринг упутстава: Практика дизајнирања и усавршавања улазних података ради усмеравања модела вештачке интелигенције ка производњи жељених резултата.
Токенизација: Процес претварања текста у мање јединице, назване токени, које модел може разумети и обрадити.
LLM-ови подешени за инструкције: Велики језички модели (LLM) који су фино подешени са специфичним инструкцијама ради побољшања тачности и релевантности њихових одговора.

## Sandbox за учење

Инжењеринг упутстава је тренутно више уметност него наука. Најбољи начин да побољшамо своју интуицију за то је да _вежбамо више_ и усвојимо приступ проба-грешка који комбинује експертизу у области примене са препорученим техникама и оптимизацијама специфичним за модел.

Jupyter Notebook који прати ову лекцију пружа _sandbox_ окружење где можете испробати оно што сте научили - у ходу или као део изазова кодирања на крају. Да бисте извршили вежбе, биће вам потребно:

1. **Azure OpenAI API кључ** - крајња тачка услуге за распоређени LLM.
2. **Python Runtime** - у којем се Notebook може извршити.
3. **Локалне променљиве окружења** - _завршите кораке [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) сада да бисте се припремили_.

Notebook долази са _почетним_ вежбама - али се охрабрујете да додате своје _Markdown_ (опис) и _Code_ (захтеви за упутства) секције како бисте испробали више примера или идеја - и изградили своју интуицију за дизајн упутстава.

## Илустровани водич

Желите да добијете ширу слику о томе шта ова лекција покрива пре него што се удубите? Погледајте овај илустровани водич, који вам даје осећај о главним темама које се покривају и кључним закључцима о којима треба да размислите у свакој од њих. План лекције вас води од разумевања основних концепата и изазова до њиховог решавања релевантним техникама инжењеринга упутстава и најбољим праксама. Имајте на уму да се одељак "Напредне технике" у овом водичу односи на садржај који је покривен у _следећем_ поглављу овог курикулума.

![Илустровани водич за инжењеринг упутстава](../../../translated_images/04-prompt-engineering-sketchnote.d5f33336957a1e4f623b826195c2146ef4cc49974b72fa373de6929b474e8b70.sr.png)

## Наша стартап идеја

Сада, хајде да разговарамо о томе како се _ова тема_ односи на нашу мисију стартапа да [донесемо иновације вештачке интелигенције у образовање](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Желимо да изградимо апликације засноване на вештачкој интелигенцији за _персонализовано учење_ - па хајде да размислимо о томе како различити корисници наше апликације могу "дизајнирати" упутства:

- **Администратори** могу тражити од вештачке интелигенције да _анализира податке о наставном плану и програму како би идентификовала празнине у покривености_. Вештачка интелигенција може сумирати резултате или их визуализовати помоћу кода.
- **Едукатори** могу тражити од вештачке интелигенције да _генерише план лекције за циљну публику и тему_. Вештачка интелигенција може креирати персонализовани план у одређеном формату.
- **Студенти** могу тражити од вештачке интелигенције да их _подучава у тешком предмету_. Вештачка интелигенција сада може водити студенте кроз лекције, савете и примере прилагођене њиховом нивоу.

То је само врх леденог брега. Погледајте [Упутства за образовање](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - библиотеку упутстава отвореног кода коју су курирали стручњаци за образовање - да бисте добили шири осећај могућности! _Покушајте да покренете нека од тих упутстава у sandbox-у или користећи OpenAI Playground да видите шта се дешава!_

<!--
ШАБЛОН ЛЕКЦИЈЕ:
Ова јединица треба да покрије основни концепт #1.
Ојачајте концепт примерима и референцама.

КОНЦЕПТ #1:
Инжењеринг упутстава.
Дефинишите га и објасните зашто је потребан.
-->

## Шта је инжењеринг упутстава?

Започели смо ову лекцију дефинишући **инжењеринг упутстава** као процес _дизајнирања и оптимизације_ текстуалних улазних података (упутстава) ради постизања конзистентних и квалитетних одговора (завршетака) за одређени циљ апликације и модел. Ово можемо посматрати као процес у 2 корака:

- _дизајнирање_ почетног упутства за одређени модел и циљ
- _усавршавање_ упутства итеративно ради побољшања квалитета одговора

Ово је нужно процес проба-грешка који захтева интуицију корисника и напор да се постигну оптимални резултати. Зашто је то важно? Да бисмо одговорили на то питање, прво морамо разумети три концепта:

- _Токенизација_ = како модел "види" упутство
- _Основни LLM-ови_ = како основни модел "обрађује" упутство
- _LLM-ови подешени за инструкције_ = како модел сада може видети "задатке"

### Токенизација

LLM види упутства као _секвенцу токена_ где различити модели (или верзије модела) могу токенизовати исто упутство на различите начине. Пошто су LLM-ови обучени на токенима (а не на сировом тексту), начин на који се упутства токенизују има директан утицај на квалитет генерисаног одговора.

Да бисте стекли интуицију о томе како токенизација функционише, пробајте алатке као што је [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) приказан испод. Копирајте своје упутство - и видите како се оно претвара у токене, обраћајући пажњу на то како се обрађују знакови размака и интерпункције. Имајте на уму да овај пример приказује старији LLM (GPT-3) - па би покушај са новијим моделом могао произвести другачији резултат.

![Токенизација](../../../translated_images/04-tokenizer-example.e71f0a0f70356c5c7d80b21e8753a28c18a7f6d4aaa1c4b08e65d17625e85642.sr.png)

### Концепт: Основни модели

Када се упутство токенизује, примарна функција ["Основног LLM-а"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (или основног модела) је да предвиди следећи токен у тој секвенци. Пошто су LLM-ови обучени на огромним текстуалним скуповима података, они имају добар осећај за статистичке односе између токена и могу направити ту предвиђање са одређеним степеном сигурности. Имајте на уму да они не разумеју _значење_ речи у упутству или токену; они само виде образац који могу "завршити" својом следећом предвиђањем. Могу наставити да предвиђају секвенцу док их корисник не прекине или док се не испуни неки унапред утврђени услов.

Желите да видите како функционише завршетак заснован на упутствима? Унесите горе наведено упутство у Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) са подразумеваним подешавањима. Систем је конфигурисан да третира упутства као захтеве за информацијама - тако да би требало да видите завршетак који задовољава овај контекст.

Али шта ако корисник жели да види нешто специфично што испуњава одређене критеријуме или циљ задатка? Овде _LLM-ови подешени за инструкције_ долазе у игру.

![Завршетак четовања основног LLM-а](../../../translated_images/04-playground-chat-base.65b76fcfde0caa6738e41d20f1a6123f9078219e6f91a88ee5ea8014f0469bdf.sr.png)

### Концепт: LLM-ови подешени за инструкције

[LLM подешен за инструкције](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) почиње са основним моделом и фино га подешава примерима или паровима улаз/излаз (нпр. порукама у више кругова) који могу садржати јасне инструкције - а одговор вештачке интелигенције покушава да прати те инструкције.

Ово користи технике као што је учење појачања уз повратне информације од људи (RLHF) које могу обучити модел да _прати инструкције_ и _учи из повратних информација_ тако да производи одговоре који су боље прилагођени практичним апликацијама и релевантнији за циљеве корисника.

Хајде да пробамо - поново погледајте горе наведено упутство, али сада промените _системску поруку_ да пружи следећу инструкцију као контекст:

> _Сумирајте садржај који вам је пружен за ученика другог разреда. Задржите резултат на један пасус са 3-5 тачака._

Видите ли како је резултат сада подешен да одражава жељени циљ и формат? Едукатор сада може директно користити овај одговор у својим слајдовима за ту класу.

![Завршетак четовања LLM-а подешеног за инструкције](../../../translated_images/04-playground-chat-instructions.b30bbfbdf92f2d051639c9bc23f74a0e2482f8dc7f0dafc6cc6fda81b2b00534.sr.png)

## Зашто нам је потребан инжењеринг упутстава?

Сада када знамо како LLM-ови обрађују упутства, хајде да разговарамо о _зашто_ нам је потребан инжењеринг упутстава. Одговор лежи у чињеници да тренутни LLM-ови представљају низ изазова који чине _поуздане и конзистентне завршетке_ теже достижним без улагања напора у конструкцију и оптимизацију упутстава. На пример:

1. **Одговори модела су стохастички.** _Исто упутство_ ће вероватно произвести различите одговоре са различитим моделима или верзијама модела. И може чак произвести различите резултате са _истим моделом_ у различито време. _Технике инжењеринга упутстава могу нам помоћи да минимизирамо ове варијације пружањем бољих оквира_.

1. **Модели могу фабриковати одговоре.** Модели су претходно обучени са _великим али коначним_ скуповима података, што значи да им недостаје знање о концептима ван тог обима обуке. Као резултат, могу произвести завршетке који су нетачни, измишљени или директно контрадикторни познатим чињеницама. _Технике инжењеринга упутстава помажу корисницима да идентификују и ублаже такве фабрикације, нпр. тражећи од вешта
Pretraga na internetu pokazala mi je da postoje izmišljeni prikazi (npr. televizijske serije ili knjige) o Marsovskim ratovima - ali nijedan iz 2076. godine. Zdrav razum nam takođe govori da je 2076. _u budućnosti_ i stoga ne može biti povezana sa stvarnim događajem.

Šta se dešava kada pokrenemo ovaj upit sa različitim LLM provajderima?

> **Odgovor 1**: OpenAI Playground (GPT-35)

![Odgovor 1](../../../translated_images/04-fabrication-oai.5818c4e0b2a2678c40e0793bf873ef4a425350dd0063a183fb8ae02cae63aa0c.sr.png)

> **Odgovor 2**: Azure OpenAI Playground (GPT-35)

![Odgovor 2](../../../translated_images/04-fabrication-aoai.b14268e9ecf25caf613b7d424c16e2a0dc5b578f8f960c0c04d4fb3a68e6cf61.sr.png)

> **Odgovor 3**: Hugging Face Chat Playground (LLama-2)

![Odgovor 3](../../../translated_images/04-fabrication-huggingchat.faf82a0a512789565e410568bce1ac911075b943dec59b1ef4080b61723b5bf4.sr.png)

Kao što se očekivalo, svaki model (ili verzija modela) proizvodi malo drugačije odgovore zahvaljujući stohastičkom ponašanju i varijacijama u sposobnostima modela. Na primer, jedan model cilja publiku osmog razreda, dok drugi pretpostavlja da se obraća srednjoškolcima. Ali sva tri modela generisala su odgovore koji bi mogli ubediti neinformisanog korisnika da je događaj stvaran.

Tehnike inženjeringa upita, poput _metapromptinga_ i _konfiguracije temperature_, mogu donekle smanjiti izmišljotine modela. Nove arhitekture inženjeringa upita takođe integrišu nove alate i tehnike u tok upita, kako bi se ublažili ili smanjili neki od ovih efekata.

## Studija slučaja: GitHub Copilot

Završićemo ovaj deo tako što ćemo steći uvid u to kako se inženjering upita koristi u stvarnim rešenjima, analizirajući jednu studiju slučaja: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot je vaš "AI par-programer" - pretvara tekstualne upite u predloge koda i integrisan je u vaše razvojno okruženje (npr. Visual Studio Code) za besprekorno korisničko iskustvo. Kao što je dokumentovano u seriji blogova ispod, najranija verzija bila je zasnovana na OpenAI Codex modelu - sa inženjerima koji su brzo shvatili potrebu za finim podešavanjem modela i razvojem boljih tehnika inženjeringa upita, kako bi poboljšali kvalitet koda. U julu su [predstavili poboljšani AI model koji prevazilazi Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) za još brže predloge.

Pročitajte postove redom kako biste pratili njihov put učenja.

- **Maj 2023** | [GitHub Copilot postaje bolji u razumevanju vašeg koda](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maj 2023** | [Unutar GitHuba: Rad sa LLM-ovima iza GitHub Copilot-a](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jun 2023** | [Kako pisati bolje upite za GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jul 2023** | [.. GitHub Copilot prevazilazi Codex sa poboljšanim AI modelom](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [Vodič za programere o inženjeringu upita i LLM-ovima](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Kako izgraditi LLM aplikaciju za preduzeća: Lekcije iz GitHub Copilot-a](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Takođe možete pregledati njihov [inženjerski blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) za više postova poput [ovog](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) koji pokazuje kako se ovi modeli i tehnike _primenjuju_ za pokretanje stvarnih aplikacija.

---

## Konstrukcija upita

Videli smo zašto je inženjering upita važan - sada ćemo razumeti kako se upiti _konstruiraju_ kako bismo mogli da procenimo različite tehnike za efikasniji dizajn upita.

### Osnovni upit

Počnimo sa osnovnim upitom: tekstualni unos koji se šalje modelu bez dodatnog konteksta. Evo primera - kada pošaljemo prve reči američke nacionalne himne OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), ona odmah _dopunjava_ odgovor sa sledećim redovima, ilustrujući osnovno prediktivno ponašanje.

| Upit (Unos)     | Dopuna (Izlaz)                                                                                                                        |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------------ |
| Oh say can you see | Izgleda da započinjete stihove pesme "The Star-Spangled Banner", nacionalne himne Sjedinjenih Američkih Država. Kompletni stihovi su ... |

### Kompleksan upit

Sada dodajmo kontekst i instrukcije tom osnovnom upitu. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) nam omogućava da konstruiramo kompleksan upit kao kolekciju _poruka_ sa:

- Parovima ulaz/izlaz koji odražavaju _korisnički_ unos i _odgovor asistenta_.
- Sistemskom porukom koja postavlja kontekst za ponašanje ili ličnost asistenta.

Zahtev sada ima oblik prikazan ispod, gde _tokenizacija_ efikasno hvata relevantne informacije iz konteksta i razgovora. Promena sistemskog konteksta može biti jednako uticajna na kvalitet dopuna kao i pruženi korisnički unosi.

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

### Instrukcijski upit

U gore navedenim primerima, korisnički upit je bio jednostavan tekstualni upit koji se može interpretirati kao zahtev za informacijama. Sa _instrukcijskim_ upitima, možemo koristiti taj tekst da preciznije odredimo zadatak, pružajući bolju smernicu za AI. Evo primera:

| Upit (Unos)                                                                                                                                                                                                                         | Dopuna (Izlaz)                                                                                                        | Tip instrukcije     |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Napiši opis Građanskog rata                                                                                                                                                                  | _vraćen jednostavan pasus_                                                                                            | Jednostavan         |
| Napiši opis Građanskog rata. Navedi ključne datume i događaje i opiši njihov značaj                                                                                                          | _vraćen pasus praćen listom ključnih datuma događaja sa opisima_                                                      | Kompleksan          |
| Napiši opis Građanskog rata u jednom pasusu. Navedi 3 ključna datuma sa njihovim značajem. Navedi još 3 ključne istorijske ličnosti i njihove doprinose. Vrati izlaz u formatu JSON datoteke | _vraćeni su detalji u tekstualnom okviru, formatirani kao JSON koji možete kopirati i validirati po potrebi_           | Kompleksan. Formatiran. |

## Primarni sadržaj

U gore navedenim primerima, upit je i dalje bio prilično otvoren, omogućavajući LLM-u da odluči koji deo njegovog unapred treniranog skupa podataka je relevantan. Sa dizajnom obrasca _primarnog sadržaja_, ulazni tekst je podeljen na dva dela:

- instrukciju (akciju)
- relevantan sadržaj (koji utiče na akciju)

Evo primera gde je instrukcija "sumiraj ovo u 2 rečenice".

| Upit (Unos)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Dopuna (Izlaz)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter je peta planeta od Sunca i najveća u Sunčevom sistemu. To je gasni džin sa masom koja je hiljaditi deo mase Sunca, ali dva i po puta veća od mase svih ostalih planeta u Sunčevom sistemu zajedno. Jupiter je jedan od najsvetlijih objekata vidljivih golim okom na noćnom nebu i poznat je drevnim civilizacijama od pre zabeležene istorije. Nazvan je po rimskom bogu Jupiteru.[19] Kada se posmatra sa Zemlje, Jupiter može biti dovoljno svetao da njegova reflektovana svetlost baca vidljive senke,[20] i prosečno je treći najsvetliji prirodni objekat na noćnom nebu posle Meseca i Venere. <br/> **Sumiraj ovo u 2 kratke rečenice** | Jupiter, peta planeta od Sunca, najveća je u Sunčevom sistemu i poznata je kao jedan od najsvetlijih objekata na noćnom nebu. Nazvan po rimskom bogu Jupiteru, to je gasni džin čija je masa dva i po puta veća od mase svih ostalih planeta u Sunčevom sistemu zajedno. |

Segment primarnog sadržaja može se koristiti na različite načine za vođenje efikasnijih instrukcija:

- **Primeri** - umesto da modelu eksplicitno kažete šta da uradi, dajte mu primere onoga što treba da uradi i dozvolite mu da zaključi obrazac.
- **Signali** - pratite instrukciju sa "signalom" koji usmerava dopunu, vodeći model ka relevantnijim odgovorima.
- **Šabloni** - to su ponovljivi 'recepti' za upite sa mestima za popunjavanje (varijablama) koje se mogu prilagoditi podacima za specifične slučajeve upotrebe.

Hajde da istražimo ove primere u praksi.

### Korišćenje primera

Ovo je pristup gde koristite primarni sadržaj da "nahranite model" nekim primerima željenog izlaza za dati zadatak i dozvolite mu da zaključi obrazac za željeni izlaz. Na osnovu broja pruženih primera, možemo imati upite bez primera, sa jednim primerom, sa nekoliko primera itd.

Upit sada sadrži tri komponente:

- Opis zadatka
- Nekoliko primera željenog izlaza
- Početak novog primera (koji postaje implicitni opis zadatka)

| Tip učenja | Upit (Unos)                                                                                                                                        | Dopuna (Izlaz)         |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------- |
| Bez primera | "Sunce sija". Prevedi na španski                                                                                                                  | "El Sol está brillando".    |
| Jedan primer | "Sunce sija" => ""El Sol está brillando". <br> "Hladan je i vetrovit dan" =>                                                                      | "Es un día frío y ventoso". |
| Nekoliko primera | Igrač je trčao po bazama => Bejzbol <br/> Igrač je udario as => Tenis <br/> Igrač je udario šesticu => Kriket <br/> Igrač je zakucao loptu => | Košarka                  |
|               |                                                                                                                                                 |                         |

Primetite kako smo morali da pružimo eksplicitnu instrukciju ("Prevedi na španski") u upitu bez primera, ali se ona zaključuje u primeru sa jednim primerom. Primer sa nekoliko primera pokazuje kako dodavanje više primera omogućava modelima da naprave tačnije zaključke bez dodatnih instrukcija.

### Signali u upitu

Još jedna tehnika za korišćenje primarnog sadržaja je pružanje _signala_ umesto primera. U ovom slučaju, dajemo modelu podsticaj u pravom smeru tako što ga _započinjemo_ sa delićem koji odražava željeni format odgovora. Model tada "prihvata signal" i nastavlja u tom pravcu.

| Broj signala | Upit (Unos)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Dopuna (Izlaz)                                                                                                                                                                                                                                                                                       |
| :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0            | Jupiter je peta planeta od Sunca i najveća u Sunčevom sistemu. To je gasni džin sa masom koja je hiljaditi deo mase Sunca, ali dva i po puta veća od mase svih ostalih planeta u Sunčevom sistemu zajedno. Jupiter je jedan od najsvetlijih objekata vidljivih golim okom na noćnom nebu i poznat je drevnim civilizacijama od pre zabeležene istorije. <br/>**Sumiraj ovo**                                       | Jupiter je najveća planeta u našem Sunčevom sistemu i peta od Sunca. To je gasni džin čija je masa dva i po puta veća od mase svih ostalih planeta zajedno.                                                                                                                                         |
| 1              | Јупитер је пета планета од Сунца и највећа у Сунчевом систему. То је гасовити гигант са масом хиљадити део масе Сунца, али два и по пута већом од свих осталих планета у Сунчевом систему заједно. Јупитер је један од најсјајнијих објеката видљивих голим оком на ноћном небу и познат је древним цивилизацијама још пре записане историје. <br/>**Сажми ово** <br/> Оно што смо научили је да је Јупитер | пета планета од Сунца и највећа у Сунчевом систему. То је гасовити гигант са масом хиљадити део масе Сунца, али два и по пута већом од свих осталих планета заједно. Лако је видљив голим оком и познат је још од давнина.                        |
| 2              | Јупитер је пета планета од Сунца и највећа у Сунчевом систему. То је гасовити гигант са масом хиљадити део масе Сунца, али два и по пута већом од свих осталих планета у Сунчевом систему заједно. Јупитер је један од најсјајнијих објеката видљивих голим оком на ноћном небу и познат је древним цивилизацијама још пре записане историје. <br/>**Сажми ово** <br/> Топ 3 чињенице које смо научили:         | 1. Јупитер је пета планета од Сунца и највећа у Сунчевом систему. <br/> 2. То је гасовити гигант са масом хиљадити део масе Сунца...<br/> 3. Јупитер је видљив голим оком још од давнина ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Шаблони за упите

Шаблон за упите је _унапред дефинисан рецепт за упит_ који се може сачувати и поново користити по потреби, како би се постигло конзистентно корисничко искуство у великом обиму. У најједноставнијем облику, то је само збирка примера упита као [овај из OpenAI](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst) који пружа интерактивне компоненте упита (поруке корисника и система) и формат захтева управљан API-јем - за подршку поновној употреби.

У сложенијем облику, као [овај пример из LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), садржи _заменљиве делове_ који се могу заменити подацима из различитих извора (кориснички унос, контекст система, спољни извори података итд.) како би се упит динамички генерисао. Ово нам омогућава да креирамо библиотеку поновљивих упита који се могу користити за постизање конзистентног корисничког искуства **програмски** у великом обиму.

На крају, права вредност шаблона лежи у могућности креирања и објављивања _библиотека упита_ за вертикалне апликационе домене - где је шаблон упита сада _оптимизован_ да одражава контекст специфичан за апликацију или примере који чине одговоре релевантнијим и тачнијим за циљну публику корисника. Репозиторијум [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) је одличан пример овог приступа, који курира библиотеку упита за образовни домен са нагласком на кључне циљеве као што су планирање лекција, дизајн наставног програма, подучавање ученика итд.

## Подржавајући садржај

Ако размишљамо о конструкцији упита као о задатку (инструкцији) и циљу (примарни садржај), онда је _секундарни садржај_ као додатни контекст који пружамо да **утиче на излаз на неки начин**. То могу бити параметри за подешавање, упутства за форматирање, таксономије тема итд. који могу помоћи моделу да _прилагоди_ свој одговор како би одговарао жељеним циљевима или очекивањима корисника.

На пример: Узимајући каталог курсева са обимним метаподацима (назив, опис, ниво, ознаке метаподатака, инструктор итд.) о свим доступним курсевима у наставном програму:

- можемо дефинисати инструкцију "сажми каталог курсева за јесен 2023."
- можемо користити примарни садржај да пружимо неколико примера жељеног излаза
- можемо користити секундарни садржај да идентификујемо топ 5 "ознака" од интереса.

Сада модел може пружити сажетак у формату приказаном кроз неколико примера - али ако резултат има више ознака, може приоритетно обрадити 5 ознака идентификованих у секундарном садржају.

---

<!--
Шаблон лекције:
Овај део треба да покрије основни концепт #1.
Ојачајте концепт примерима и референцама.

КОНЦЕПТ #3:
Технике инжењеринга упита.
Које су основне технике инжењеринга упита?
Илуструјте их вежбама.
-->

## Најбоље праксе за упите

Сада када знамо како се упити могу _конструисати_, можемо почети да размишљамо о томе како их _дизајнирати_ да одражавају најбоље праксе. Можемо размишљати о овоме у два дела - имајући прави _начин размишљања_ и примењујући праве _технике_.

### Начин размишљања у инжењерингу упита

Инжењеринг упита је процес проба и грешака, па имајте на уму три широка водича:

1. **Разумевање домена је важно.** Тачност и релевантност одговора су функција _домена_ у којем та апликација или корисник делује. Примените своју интуицију и експертизу у домену да **даље прилагодите технике**. На пример, дефинишите _личности специфичне за домен_ у вашим системским упитима, или користите _шаблоне специфичне за домен_ у вашим корисничким упитима. Пружите секундарни садржај који одражава контексте специфичне за домен, или користите _наговештаје и примере специфичне за домен_ да водите модел ка познатим обрасцима употребе.

2. **Разумевање модела је важно.** Знамо да су модели стохастички по природи. Али имплементације модела такође могу варирати у погледу скупа података за обуку који користе (унапред обучено знање), способности које пружају (нпр. преко API-ја или SDK-а) и типа садржаја за који су оптимизовани (нпр. код против слика против текста). Разумите предности и ограничења модела који користите и користите то знање да _приоритетно одредите задатке_ или изградите _прилагођене шаблоне_ који су оптимизовани за способности модела.

3. **Итерација и валидација су важне.** Модели се брзо развијају, као и технике за инжењеринг упита. Као стручњак за домен, можда имате други контекст или критеријуме специфичне за _вашу_ апликацију, који можда не важе за ширу заједницу. Користите алате и технике инжењеринга упита да "започнете" конструкцију упита, затим итеративно проверавајте и валидирајте резултате користећи своју интуицију и експертизу у домену. Забележите своја сазнања и креирајте **базу знања** (нпр. библиотеке упита) која се може користити као нова основа за брже итерације у будућности.

## Најбоље праксе

Сада да погледамо уобичајене најбоље праксе које препоручују [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) и [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) практичари.

| Шта                              | Зашто                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Евалуирајте најновије моделе.       | Нове генерације модела вероватно имају побољшане функције и квалитет - али могу такође изазвати веће трошкове. Евалуирајте их за утицај, а затим донесите одлуке о миграцији.                                                                                |
| Одвојите инструкције и контекст   | Проверите да ли ваш модел/провајдер дефинише _разграничења_ за јасније разликовање инструкција, примарног и секундарног садржаја. Ово може помоћи моделима да тачније доделе тежину токенима.                                                         |
| Будите специфични и јасни             | Дајте више детаља о жељеном контексту, исходу, дужини, формату, стилу итд. Ово ће побољшати и квалитет и конзистентност одговора. Забележите рецепте у поновљивим шаблонима.                                                          |
| Будите описни, користите примере      | Модели могу боље реаговати на приступ "покажи и реци". Почните са `zero-shot` приступом где му дајете инструкцију (али без примера), затим пробајте `few-shot` као усавршавање, пружајући неколико примера жељеног излаза. Користите аналогије. |
| Користите наговештаје за покретање одговора | Наведите га ка жељеном исходу дајући му неке почетне речи или фразе које може користити као полазну тачку за одговор.                                                                                                               |
| Поновите инструкције                       | Понекад је потребно поновити инструкције моделу. Дајте упутства пре и после вашег примарног садржаја, користите инструкцију и наговештај итд. Итеративно проверавајте и валидирајте да видите шта најбоље функционише.                                                         |
| Редослед је важан                     | Редослед у којем представљате информације моделу може утицати на излаз, чак и у примерима учења, захваљујући пристрасности према новијим информацијама. Пробајте различите опције да видите шта најбоље функционише.                                                               |
| Дајте моделу "излаз"           | Дајте моделу _алтернативни_ одговор који може пружити ако из било ког разлога не може да заврши задатак. Ово може смањити шансе да модели генеришу лажне или измишљене одговоре.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

Као и код сваке најбоље праксе, запамтите да _ваше искуство може варирати_ у зависности од модела, задатка и домена. Користите ове смернице као почетну тачку и итеративно истражујте шта најбоље функционише за вас. Константно преиспитујте свој процес инжењеринга упита како нови модели и алати постају доступни, са фокусом на скалабилност процеса и квалитет одговора.

<!--
Шаблон лекције:
Овај део треба да пружи изазов са кодом ако је применљиво

ИЗАЗОВ:
Линк ка Jupyter Notebook-у са само коментарима кода у упутствима (секције кода су празне).

РЕШЕЊЕ:
Линк ка копији тог Notebook-а са попуњеним упитима и покренутим, показујући како један пример може изгледати.
-->

## Задатак

Честитамо! Стигли сте до краја лекције! Време је да примените неке од тих концепата и техника у пракси са стварним примерима!

За наш задатак, користићемо Jupyter Notebook са вежбама које можете интерактивно завршити. Такође можете проширити Notebook са сопственим Markdown и Code ћелијама како бисте истражили идеје и технике на свој начин.

### Да бисте започели, направите fork репозиторијума, затим

- (Препоручено) Покрените GitHub Codespaces
- (Алтернативно) Клонирајте репозиторијум на свој локални уређај и користите га са Docker Desktop
- (Алтернативно) Отворите Notebook са вашим омиљеним окружењем за покретање Notebook-а.

### Затим, конфигуришите своје променљиве окружења

- Копирајте `.env.copy` датотеку у корену репозиторијума у `.env` и попуните вредности за `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` и `AZURE_OPENAI_DEPLOYMENT`. Вратите се на [секцију Learning Sandbox](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) да бисте сазнали како.

### Затим, отворите Jupyter Notebook

- Изаберите језгро за покретање. Ако користите опције 1 или 2, једноставно изаберите подразумевано Python 3.10.x језгро које пружа dev container.

Све је спремно за покретање вежби. Имајте на уму да овде нема _тачних и погрешних_ одговора - само истраживање опција методом проба и грешака и изградња интуиције о томе шта функционише за одређени модел и домен апликације.

_Из тог разлога, у овој лекцији нема сегмената са решењима кода. Уместо тога, Notebook ће имати Markdown ћелије под називом "Моје решење:" које показују један пример излаза за референцу._

 <!--
Шаблон лекције:
Завршите део са резимеом и ресурсима за самостално учење.
-->

## Провера знања

Који од следећих је добар упит који следи неке разумне најбоље праксе?

1. Покажи ми слику црвеног аутомобила
2. Покажи ми слику црвеног аутомобила марке Volvo и модела XC90 паркираног поред литице са заласком сунца
3. Покажи ми слику црвеног аутомобила марке Volvo и модела XC90

О: 2, то је најбољи упит јер пружа детаље о "шта" и иде у специфичности (не било који аутомобил, већ одређена марка и модел) и такође описује целокупно окружење. 3 је следећи најбољи јер такође садржи доста описа.

## 🚀 Изазов

Покушајте да искористите технику "наговештаја" са упитом: Заврши реченицу "Покажи ми слику црвеног аутомобила марке Volvo и ". Шта добијате као одговор и како бисте га побољшали?

## Одличан рад! Наставите са учењем

Желите да научите више о различитим концептима инжењеринга упита? Идите на [страницу за наставак учења](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) да бист

---

**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење уз помоћ вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.