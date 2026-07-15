# Skirting įvairius LLM modelius ir juos lyginant

[![Skirting įvairius LLM modelius ir juos lyginant](../../../translated_images/lt/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Norėdami peržiūrėti šios pamokos vaizdo įrašą, spustelėkite aukščiau esantį vaizdą_

Praėjusioje pamokoje matėme, kaip Generatyvioji dirbtinio intelekto technologija keičia technologinį kraštovaizdį, kaip veikia dideli kalbos modeliai (LLM) ir kaip verslas – toks kaip mūsų startuolis – gali juos pritaikyti savo atvejams ir augti! Šiame skyriuje mes palyginsime ir kontrastuosime skirtingus didelių kalbos modelių tipus (LLM), kad suprastume jų privalumus ir trūkumus.

Kitas žingsnis mūsų startuolio kelionėje yra ištirti dabartinį LLM kraštovaizdį ir suprasti, kurie modeliai yra tinkami mūsų atvejui.

## Įvadas

Ši pamoka apims:

- Skirtingus LLM tipus dabartiniame kraštovaizdyje.
- Kaip išbandyti, tobulinti ir palyginti skirtingus modelius savo atvejui Azure aplinkoje.
- Kaip diegti LLM modelį.

## Mokymosi tikslai

Baigę šią pamoką galėsite:

- Pasirinkti tinkamą modelį savo poreikiams.
- Suprasti, kaip testuoti, tobulinti ir gerinti modelio našumą.
- Sužinoti, kaip verslai diegia modelius.

## Suprasti skirtingų LLM tipus

LLM galima skirstyti pagal jų architektūrą, mokymo duomenis ir panaudojimo atvejį. Šie skirtumai padės mūsų startuoliui pasirinkti tinkamą modelį konkrečiam scenarijui ir suprasti, kaip testuoti, iteruoti bei gerinti našumą.

Yra daug skirtingų LLM modelių tipų, o jūsų modelio pasirinkimas priklauso nuo to, kam jį norite panaudoti, jūsų duomenų, kiek esate pasiruošę mokėti ir kitų veiksnių.

Priklausomai nuo to, ar norite naudoti modelius tekstui, garsui, vaizdo įrašams, vaizdų generavimui ir pan., galite pasirinkti skirtingą modelio tipą.

- **Garsas ir balso atpažinimas**. Whisper tipo modeliai vis dar naudingi kaip bendro pobūdžio balso atpažinimo modeliai, tačiau gamybos pasirinkimai dabar apima ir naujesnius balso į tekstą modelius, tokius kaip `gpt-4o-transcribe`, `gpt-4o-mini-transcribe` ir diarizacijos variantus. Įvertinkite kalbos aprėptį, diarizaciją, realaus laiko palaikymą, delsą ir kainą pagal savo scenarijų. Daugiau skaitykite [OpenAI balso į teksto dokumentacijoje](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst).

- **Vaizdų generavimas**. DALL-E ir Midjourney yra gerai žinomos vaizdų generavimo galimybės, tačiau dabartiniai OpenAI vaizdų API daugiausia remiasi GPT Image modeliais kaip `gpt-image-2`, o taip pat populiarūs yra Stable Diffusion, Imagen, Flux ir kitos modelių šeimos. Lyginkite užklausų atitikimą, redagavimo palaikymą, stiliaus kontrolę, saugumo reikalavimus ir licencijavimą. Daugiau apie tai skaitykite [OpenAI vaizdų generavimo vadove](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) ir šio mokymo plano 9 skyriuje.

- **Teksto generavimas**. Teksto modeliai apima pažangius modelius, loginio mąstymo modelius, mažesnius ir mažo delsos modelius bei atviro svorio modelius. Dabartiniai pavyzdžiai yra OpenAI GPT-5.x modeliai, Anthropic Claude 4.x modeliai, Google Gemini 3.x modeliai, Meta Llama 4 modeliai, ir Mistral modeliai. Neapsiribokite pasirinkimu tik pagal išleidimo datą ar kainą; lyginkite užduoties kokybę, delsą, konteksto langą, įrankių naudojimą, saugumo elgseną, regioninį prieinamumą ir bendras sąnaudas. [Microsoft Foundry modelių katalogas](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) yra gera vieta palyginti modelius, prieinamus Azure.

- **Daugiakryptiškumas**. Daugelis dabartinių modelių gali apdoroti ne tik tekstą. Kai kurie priima vaizdo, garso ar vaizdo įrašo įvestis; kai kurie gali kviesti įrankius; o specializuoti modeliai gali generuoti vaizdus, garsą ar vaizdo įrašus. Pavyzdžiui, dabartiniai OpenAI modeliai palaiko tekstinę ir vaizdinę įvestį, Gemini modeliai gali palaikyti tekstą, kodą, vaizdą, garsą ir vaizdo įrašus priklausomai nuo varianto, o Llama 4 Scout ir Maverick yra atviro svorio natūraliai daugiakryptės modeliai. Visada patikrinkite kiekvieno modelio kortelę dėl palaikomų įvesties ir išvesties modalių prieš kuriant darbo eigą.

Pasirinkus modelį, gaunate pagrindines galimybes, tačiau tai gali būti nepakankama. Dažnai turite įmonės specifinius duomenis, kuriuos turite perduoti LLM. Yra keletas skirtingų būdų, kaip tai padaryti, apie tai plačiau bus tolesniuose skyriuose.

### Pagrindiniai modeliai prieš LLM

Terminas Pagrindinis modelis buvo [sukurtas Stanfordo tyrėjų](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) ir apibūdinamas kaip DI modelis, kuris atitinka tam tikrus kriterijus, tokius kaip:

- **Jie mokomi naudojant nemokytą arba savarankišką mokymąsi**, tai reiškia, kad jie mokomi su nepanaudotais daugiakryptėmis duomenų, ir jiems nereikia žmogaus anotacijų ar žymėjimų mokymo procese.
- **Tai labai dideli modeliai**, paremti giluminiais neuroniniais tinklais, kurie mokomi su milijardais parametrų.
- **Paprastai jie skirti būti „pamatu“ kitiems modeliams**, tai reiškia, kad juos galima naudoti kaip pradinį tašką kitiems modeliams kurti, kuris gali būti atliktas per konfigūravimą (fine-tuning).

![Pagrindiniai modeliai prieš LLM](../../../translated_images/lt/FoundationModel.e4859dbb7a825c94.webp)

Vaizdo šaltinis: [Essential Guide to Foundation Models and Large Language Models | by Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Norėdami dar labiau paaiškinti skirtumą, pažvelkime į ChatGPT kaip istorinį pavyzdį. Ankstyvosios ChatGPT versijos naudojo GPT-3.5 kaip pagrindinį modelį. OpenAI tada naudojo pokalbių specifinius duomenis ir suderinimo technologijas, kad sukurtų geriau veikiančią versiją pokalbių scenarijose, tokiuose kaip chatbot’ai. Šiuolaikinės DI paslaugos dažnai perjungia kelis modelių variantus, todėl paslaugos pavadinimas ir po juo esantis modelio pavadinimas ne visada sutampa.

![Pagrindinis modelis](../../../translated_images/lt/Multimodal.2c389c6439e0fc51.webp)

Vaizdo šaltinis: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Atviro svorio/atviro kodo prieš patentuotus modelius

Kitas būdas kategorizuoti LLM yra pagal tai, ar jie yra atviro svorio, atviro kodo, ar patentuoti.

Atviro kodo ir atviro svorio modeliai leidžia peržiūrėti, atsisiųsti ar pritaikyti modelio artefaktus, bet jų licencijos skiriasi. Kai kurie yra visiškai atviro kodo, o kiti – atviro svorio modeliai su naudojimo apribojimais. Jie gali būti naudingi, kai verslas nori didesnės kontrolės diegiant, duomenų vietos, kainos ar pritaikymo atžvilgiu. Tačiau komandos vis tiek turi peržiūrėti licencijos sąlygas, aptarnavimo kainas, priežiūrą, saugos naujinimus ir vertinimo kokybę prieš naudodamos juos gamyboje. Pavyzdžiai: [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst), kai kurie [Mistral modeliai](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst) ir daugelis modelių, talpinamų [Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst).

Patentiniuose modeliuose jų savininkas ir teikėjas. Šie modeliai dažnai optimizuoti valdomam gamybiniam naudojimui ir gali pasiūlyti stiprią pagalbą, saugumo sistemas, įrankių integraciją ir mastelį. Tačiau klientai paprastai negali peržiūrėti ar keisti modelio svorių ir turi peržiūrėti teikėjo sąlygas dėl privatumo, duomenų saugojimo, atitikties ir priimtino naudojimo. Pavyzdžiai: [OpenAI modeliai](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), [Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst) ir [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst).

### Įterpimas prieš vaizdo generavimą prieš teksto ir kodo generavimą

LLM taip pat galima kategorizuoti pagal generuojamą išvestį.

Įterpimai yra modelių rinkinys, galintis paversti tekstą į skaitmeninę formą, vadinamą įterpimu, kuris yra skaitmeninis įvesties teksto atvaizdavimas. Įterpimai leidžia mašinoms aiškiau suprasti žodžių ar sakinių tarpusavio ryšius, juos galima naudoti kitų modelių įvestims, pavyzdžiui, klasifikacijos ar klasterizacijos modeliams, kurie geriau veikia su skaitmeniniais duomenimis. Įterpimų modeliai dažnai naudojami perdavimo mokymuisi, kai modelis kuriamas pagal tarpinę užduotį, kuriai turima daug duomenų, o vėliau modelio svoriai (įterpimai) naudojami tolimesnėms užduotims. Šios kategorijos pavyzdys – [OpenAI įterpimai](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Įterpimas](../../../translated_images/lt/Embedding.c3708fe988ccf760.webp)

Vaizdų generavimo modeliai yra modeliai, skirti generuoti vaizdus. Šie modeliai dažnai naudojami vaizdų redagavimui, sintezei ir vertimui. Vaizdų generavimo modeliai mokomi dideliais vaizdų duomenų rinkiniais, tokiais kaip [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), ir gali generuoti naujus vaizdus arba redaguoti esamus pritaikant tokius metodus kaip užpildymas, super raiška ir spalvinimas. Pavyzdžiai: [GPT Image modeliai](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst), [Stable Diffusion modeliai](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst) ir Imagen modeliai.

![Vaizdų generavimas](../../../translated_images/lt/Image.349c080266a763fd.webp)

Teksto ir kodo generavimo modeliai generuoja tekstą ar kodą. Šie modeliai dažnai naudojami teksto santraukai, vertimui ir klausimų atsakymui. Teksto generavimo modeliai mokomi dideliais tekstų duomenų rinkiniais, tokiais kaip [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), ir gali generuoti naują tekstą ar atsakyti į klausimus. Kodo generavimo modeliai, tokie kaip [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), mokomi dideliais kodo duomenų rinkiniais, tokiais kaip GitHub, ir gali generuoti naują kodą arba taisyti klaidas esamame kode.

![Teksto ir kodo generavimas](../../../translated_images/lt/Text.a8c0cf139e5cc2a0.webp)

### Encoder-Decoder prieš tik dekoderį modelius

Kalbant apie skirtingas LLM architektūras, naudokime analogiją.

Įsivaizduokite, kad jūsų vadovas davė užduotį parašyti testą studentams. Turite du kolegas; vienas atsakingas už turinio kūrimą, kitas – už peržiūrą.

Turinio kūrėjas yra kaip tik dekoderio modelis: jis gali pažiūrėti į temą, matyti, ką jau parašėte, ir tęsti turinio generavimą remdamasis tuo kontekstu. Jie labai gerai rašo patrauklų ir informatyvų turinį, tačiau ne visada yra geriausias pasirinkimas, kai užduotis yra tik klasifikuoti, atgauti ar koduoti informaciją. Dekoderio modelių šeimos pavyzdžiai yra GPT ir Llama modeliai.

Peržiūros specialistas yra kaip tik enkoderio modelis, jis žiūri į parašytą kursą ir atsakymus, pastebi ryšį tarp jų ir supranta kontekstą, bet nėra geras kuriant turinį. Pavyzdys – tik enkoderio modelis BERT.

Įsivaizduokite, kad turime asmenį, kuris gali tiek kurti, tiek peržiūrėti testą – tai būtų Encoder-Decoder modelis. Pavyzdžiai yra BART ir T5.

### Paslauga prieš modelį

Dabar pakalbėkime apie skirtumą tarp paslaugos ir modelio. Paslauga yra produktas, kurį siūlo Debesų paslaugų tiekėjas, ir dažnai apima kombinuotas modelius, duomenis ir kitus komponentus. Modelis yra paslaugos pagrindinis komponentas, dažnai pagrindinis modelis, toks kaip LLM.

Paslaugos dažnai optimizuotos gamybiniam naudojimui ir dažnai yra lengviau naudojamos nei modeliai per grafinę vartotojo sąsają. Tačiau paslaugos ne visada yra nemokamos ir gali reikalauti prenumeratos ar mokėjimo, mainais už paslaugos savininko įrangos ir išteklių naudojimą, leidžiančio optimizuoti išlaidas ir lengvai keisti mastą. Pavyzdys yra [Azure OpenAI paslauga](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), kuri siūlo mokėjimą pagal naudojimą, tai reiškia, kad vartotojai apmokestinami proporcingai naudojimo apimčiai. Azure OpenAI paslauga taip pat siūlo įmonių klasės saugumą ir atsakingo DI sistemą, papildančią modelių galimybes.

Modeliai yra neuroninio tinklo artefaktai: parametrai, svoriai, architektūra, žodynėlis ir palaikanti konfiguracija. Modelio paleidimas vietoje arba privačioje aplinkoje reikalauja tinkamos aparatūros, aptarnavimo infrastruktūros, stebėjimo ir suderinamos atviro kodo/atviro svorio licencijos arba komercinės licencijos. Atviro svorio modeliai, tokie kaip Llama 4 ar Mistral modeliai, gali būti savarankiškai talpinami, tačiau jiems vis tiek reikia skaičiavimo galios ir operatyvinių žinių.

## Kaip testuoti ir iteruoti su skirtingais modeliais, kad suprastumėte našumą Azure aplinkoje


Kai mūsų komanda ištiria dabartinę LLM aplinką ir identifikuoja keletą tinkamų kandidatų jų scenarijams, kitas žingsnis yra juos išbandyti savo duomenyse ir darbo krūvyje. Tai iteracinis procesas, atliekamas eksperimentų ir matavimų būdu.
Dauguma modelių, apie kuriuos kalbėjome ankstesniuose skyriuose (OpenAI modeliai, atviro svorio modeliai kaip Llama 4 ir Mistral, bei Hugging Face modeliai), yra prieinami [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst).

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst), anksčiau žinomas kaip Azure AI Studio/Azure AI Foundry, yra vieninga Azure platforma AI programoms ir agentams kurti. Ji padeda kūrėjams valdyti gyvavimo ciklą nuo eksperimentavimo ir vertinimo iki diegimo, stebėjimo ir valdymo. Microsoft Foundry modelių katalogas leidžia vartotojui:

- Rasti į katalogą įtrauktą pagrindinį modelį, įskaitant modelius, parduodamus Azure ir partnerių bei bendruomenės teikėjų modelius. Vartotojai gali filtruoti užduotį, tiekėją, licenciją, diegimo parinktį arba pavadinimą.

![Model catalog](../../../translated_images/lt/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- Peržiūrėti modelio kortelę, įskaitant išsamią numatomos paskirties aprašymą ir treniravimo duomenis, kodo pavyzdžius ir įvertinimo rezultatus vidinėje vertinimo bibliotekoje.

![Model card](../../../translated_images/lt/ModelCard.598051692c6e400d.webp)

- Palyginti etalonus tarp modelių ir duomenų rinkinių, prieinamų pramonėje, siekiant įvertinti, kuris geriausiai atitinka verslo scenarijų, per [Model Benchmarks](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst) langą.

![Model benchmarks](../../../translated_images/lt/ModelBenchmarks.254cb20fbd06c03a.webp)

- Tiksliai perduoti palaikomus modelius pagal pasirinktinius treniravimo duomenis, kad pagerintumėte modelio našumą konkrečiame darbo krūvyje, pasinaudodami Microsoft Foundry eksperimentavimo ir stebėjimo galimybėmis.

![Model fine-tuning](../../../translated_images/lt/FineTuning.aac48f07142e36fd.webp)

- Diegti originalų iš anksto apmokytą modelį arba tiksliai perduotą versiją į nuotolinį realaus laiko spėjimo galinį tašką, naudojant valdomas skaičiavimo arba serverio be serverio diegimo parinktis, kad programos galėtų juo naudotis.

![Model deployment](../../../translated_images/lt/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> Ne visi katalogo modeliai šiuo metu yra prieinami tiksliniam perdavimui ir/arba mokėjimo pagal naudojimą diegimui. Patikrinkite modelio kortelę dėl išsamių informacijos apie modelio galimybes ir ribotumus.

## LLM rezultatų gerinimas

Mūsų startuolio komanda ištyrė įvairius LLM tipus ir debesijos platformą (Microsoft Foundry), leidžiančią palyginti skirtingus modelius, įvertinti juos testiniuose duomenyse, pagerinti našumą ir įdiegti spėjimo galiniuose taškuose.

Bet kada jie turėtų apsvarstyti galimybę tiksliai perduoti modelį, o ne naudoti iš anksto apmokytą? Ar yra kitų būdų pagerinti modelio našumą konkrečiuose darbo krūviuose?

Verslas gali naudoti keletą metodų, kad gautų norimus rezultatus iš LLM. Galite pasirinkti skirtingų tipų modelius su skirtingais apmokymo laipsniais diegiant LLM produkcijoje, turint skirtingą sudėtingumo, kainos ir kokybės lygį. Štai keletas požiūrių:

- **Užklausų inžinerija su kontekstu**. Idėja yra pateikti pakankamai konteksto, kai užduodate užklausą, kad gautumėte reikiamus atsakymus.

- **Retrieval Augmented Generation, RAG**. Jūsų duomenys gali būti saugomi duomenų bazėje ar žiniatinklio galiniame taške, pavyzdžiui, tam, kad į užklausą būtų įtraukta ši informacija arba jos dalis, galite parsisiųsti aktualią informaciją ir padaryti ją vartotojo užklausos dalimi.

- **Tiksliai perduotas modelis**. Čia jūs toliau treniravote modelį su savo duomenimis, dėl ko modelis tapo tikslesnis ir labiau atsako į jūsų poreikius, bet tai gali būti brangu.

![LLMs deployment](../../../translated_images/lt/Deploy.18b2d27412ec8c02.webp)

Paveikslėlio šaltinis: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Užklausų inžinerija su kontekstu

Iš anksto apmokyti LLM puikiai dirba su bendrų natūralios kalbos užduotimis, net jei jas kviečiate trumpu užklausimu, pavyzdžiui, sakiniu, kurį reikia užbaigti, arba klausimu – tai vadinama „nulinio šūvio“ mokymusi.

Tačiau kuo geriau vartotojas gali suformuluoti savo užklausą, su išsamiu prašymu ir pavyzdžiais – Kontekstu – tuo tikslesnis ir labiau atitinkantis vartotojo lūkesčius bus atsakymas. Šiuo atveju kalbame apie „vieno šūvio“ mokymąsi, jei užklausoje yra tik vienas pavyzdys, ir „keleto šūvių“ mokymąsi, jei yra keli pavyzdžiai.
Užklausų inžinerija su kontekstu yra ekonomiškai efektyviausias būdas pradėti.

### Retrieval Augmented Generation (RAG)

LLM turi apribojimą, kad gali naudoti tik tuos duomenis, kurie buvo naudojami jų treniravimui atsakymui generuoti. Tai reiškia, kad jie nežino nieko apie faktus, įvykusius po jų treniravimo proceso, ir neturi prieigos prie neviešos informacijos (pvz., įmonės duomenų).
Tai galima įveikti naudojant RAG, techniką, kuri papildo užklausą išoriniais duomenimis dokumentų gabalėlių pavidalu, atsižvelgiant į užklausos ilgio ribas. Tai palaiko vektorinės duomenų bazės įrankiai (kaip [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)), kurie parenka naudingus gabalėlius iš įvairių iš anksto apibrėžtų duomenų šaltinių ir prideda juos prie užklausos konteksto.

Ši technika yra labai naudinga verslams, neturintiems pakankamai duomenų, laiko ar išteklių LLM tiksliniam perdavimui, bet norintiems pagerinti našumą konkrečiame darbo krūvyje ir sumažinti haliucinacijų, pasenusio ar nepalaikomo atsakymo riziką.

### Tiksliai perduotas modelis

Tikslus perdavimas yra procesas, kuris pasinaudoja perdavimo mokymusi, kad „pritaikytų“ modelį konkrečiai užduočiai arba problemai spręsti. Skirtingai nuo kelių šūvių mokymosi ir RAG, tai sukuria naują atnaujintą modelį su atnaujintais svoriais ir biasais. Tam reikalingas treniravimo pavyzdžių rinkinys, kuriame yra vienas įvesties elementas (užklausa) ir susijęs išvesties elementas (užbaigimas).
Tai būtų pageidaujamas požiūris, jei:

- **Naudojami mažesni, konkrečioms užduotims skirti modeliai**. Verslas norėtų tiksliai perduoti mažesnį modelį siaurai užduočiai, o ne kelis kartus užduoti didesniam pagrindiniam modeliui, kas būtų ekonomiškesnis ir greitesnis sprendimas.

- **Atsižvelgiant į delsą**. Delsa yra svarbi konkrečiam naudojimo atvejui, todėl negalima naudoti labai ilgų užklausų arba pavyzdžių kiekis, iš kurio modelis turėtų mokytis, nesutampa su užklausos ilgio riba.

- **Pritaikant stabilų elgesį**. Verslas turi daug aukštos kokybės pavyzdžių ir nori, kad modelis nuosekliai laikytųsi užduoties šablono, išvesties formato, tono ar specifinio domeno stiliaus. Jei pagrindinė problema yra nauji faktai ar dažnai kintanti privati informacija, naudokite RAG vietoje pasikliovimo vien tik tiksliniu perdavimu.

### Apmokytas modelis

Mokyti LLM nuo nulio be jokios abejonės yra sunkiausias ir sudėtingiausias būdas, reikalaujantis milžiniško duomenų kiekio, kvalifikuotų išteklių ir tinkamos skaičiavimo galios. Ši galimybė turėtų būti svarstoma tik situacijoje, kai verslas turi domenui specifinį naudojimo atvejį ir didelį domenui pritaikytų duomenų kiekį.

## Žinių patikrinimas

Koks galėtų būti geras būdas pagerinti LLM užbaigimo rezultatus?

1. Užklausų inžinerija su kontekstu
1. RAG
1. Tiksliai perduotas modelis

A: Visi trys gali padėti. Pradėkite nuo užklausų inžinerijos su kontekstu greitiems patobulinimams, o kai modelis reikalauja naujausių faktų ar privataus verslo duomenų, naudokite RAG. Pasirinkite tikslinį perdavimą, kai turite pakankamai aukštos kokybės pavyzdžių ir jums reikia, kad modelis nuosekliai laikytųsi užduoties, formato, tono arba domeno šablono.

## 🚀 Iššūkis

Sužinokite daugiau apie tai, kaip galite [naudoti RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) savo verslui.

## Puikus darbas, tęskite mokymąsi

Baigę šią pamoką, peržiūrėkite mūsų [Generatyviosios AI mokymosi kolekciją](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ir toliau gilinkite savo žinias apie generatyviąją AI!

Pereikite prie 3 pamokos, kurioje aptarsime, kaip [atsakingai kurti su generatyviąja AI](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->