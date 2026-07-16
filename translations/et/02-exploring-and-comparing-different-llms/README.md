# Erinevate LLM-ide uurimine ja võrdlemine

[![Erinevate LLM-ide uurimine ja võrdlemine](../../../translated_images/et/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Klikka ülaloleval pildil, et vaadata selle õppetunni videot_

Eelmises õppetunnis nägime, kuidas Generatiivne tehisintellekt muudab tehnoloogiaalast maastikku, kuidas suured keelemudelid (LLM-id) töötavad ja kuidas ettevõte – näiteks meie idufirma – saab neid oma kasutusjuhtumites rakendada ja kasvada! Selles peatükis vaatame, kuidas erinevat tüüpi suuri keelemudeleid võrrelda ja vastandada, et mõista nende plusse ja miinuseid.

Järgmine samm meie idufirma teekonnal on uurida olemasolevat LLM-ide maastikku ja mõista, millised neist sobivad meie kasutusjuhtumiks.

## Sissejuhatus

See õppetund katab:

- Erinevad LLM-tüübid praegusel maastikul.
- Erinevate mudelite testimine, iteratsioon ja võrdlus teie kasutusjuhtumi jaoks Azure’s.
- Kuidas LLM-i juurutada.

## Õpieesmärgid

Pärast selle õppetunni läbimist oskate:

- Vali oma kasutusjuhtumi jaoks õige mudel.
- Mõista, kuidas mudelit testida, iteratiivselt parendada ja sooritust suurendada.
- Teada, kuidas ettevõtted mudeleid juurutavad.

## Mõista erinevaid LLM-tüüpe

LLM-ide puhul võib esineda mitmeid kategooriaid, mis põhinevad nende arhitektuuril, treeningandmetel ja kasutusjuhtumil. Nende erinevuste mõistmine aitab meie idufirmal valida konkreetse stsenaariumi jaoks õige mudeli ning mõista, kuidas testida, iteratiivselt täiustada ja sooritust parandada.

Olemas on palju erinevat tüüpi LLM-mudeleid, mudeli valik sõltub sellest, milleks te neid kasutada soovite, teie andmetest, valmisolekust maksta ja muudest teguritest.

Sõltuvalt sellest, kas kavatsete kasutada mudeleid teksti, heli, video, pildiloome jaoks või muudeks eesmärkideks, võite valida erinevat tüüpi mudeli.

- **Heli ja kõnetuvastus**. Whisper-tüüpi mudelid on endiselt kasulikud üldotstarbelised kõnetuvastuse mudelid, kuid tootmiskasutuses võivad olla ka uuemad kõne-tekst mudelid nagu `gpt-4o-transcribe`, `gpt-4o-mini-transcribe` ning diariseerimise variandid. Hinnake oma stsenaariumi jaoks keelekatvust, diariseerimist, reaalajas tuge, latency'd ja kulu. Lisateavet leiate [OpenAI kõne-tekst dokumentatsioonist](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst).

- **Pildiloome**. DALL-E ja Midjourney on hästi tuntud pildigeneratsiooni valikud, kuid praegused OpenAI pildi-API-d keskenduvad GPT pildimudelitele nagu `gpt-image-2`, samas on ka Stable Diffusion, Imagen, Flux ja teised mudelifirmad populaarsed valikud. Võrrelge promptide järgimist, redigeerimistuge, stiilijalitust, turvanõudeid ja litsentseerimist. Lisateavet leiate [OpenAI pildiloome juhendist](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) ja selle õppekava 9. peatükist.

- **Teksti generatsioon**. Tekstimudelid katavad nüüd tipptasemel mudeleid, mõtlemismudeleid, väikse latentsusega mudeleid ning avatud kaaludega mudeleid. Praegused näiteks on OpenAI GPT-5.x mudelid, Anthropic Claude 4.x mudelid, Google Gemini 3.x mudelid, Meta Llama 4 mudelid ja Mistral mudelid. Ära vali ainult vabastamise kuupäeva või hinna järgi; võrdle töö kvaliteeti, latentseegi, kontekstiakna suurust, tööriistade kasutust, turvalisuse käitumist, piirkondlikku saadavust ja kogukulusid. [Microsoft Foundry mudelikollektsioon](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) on hea koht Azure'is saadaval olevate mudelite võrdlemiseks.

- **Mitmemodaalsus**. Paljud praegused mudelid suudavad töödelda rohkem kui ainult teksti. Mõned aktsepteerivad pilte, heli või video sisendeid; mõned võivad kasutada tööriistu; ja spetsialiseeritud mudelid võivad genereerida pilte, heli või videot. Näiteks toetavad praegused OpenAI mudelid teksti ja pildi sisestust, Gemini mudelid suudavad mõne variandi puhul toetada teksti, koodi, pilti, heli ja videot ning Llama 4 Scout ja Maverick on avatud kaaludega loomupäraselt mitmemodaalsed mudelid. Enne oma töövoo ehitamist kontrolli alati konkreetse mudelikaarte toetatud sisend- ja väljundmoodaalsusi.

Mudeli valimine tähendab, et saad mõned põhilised võimed, kuid need ei pruugi alati piisavad olla. Tihti on ettevõttel olemas konkreetseid andmeid, millest peate LLM-ile kuidagi rääkima. Selleks on mitu erinevat lähenemist - neist rohkem järgmistes lõikudes.

### Põhimudelite ja LLM-ide võrdlus

Mõistet "Foundation Model" algatasid [Stanfordi teadlased](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) ning defineerisid AI mudelina, mis vastab mõnedele kriteeriumidele, näiteks:

- **Nende treenimine toimub järelevalveta või enesejärelevalvega**, mis tähendab, et nad treenitakse märgistamata mitmemodaalsetel andmetel ning nende treeninguks ei ole vaja inimeste annotatsioone ega märgistamist.
- **Nad on väga suured mudelid**, mis põhinevad väga sügavatel närvivõrkudel, mis on treenitud miljardite parameetrite peal.
- **Neid kasutatakse tavaliselt teiste mudelite ‘põhjana’**, see tähendab, et neid saab kasutada lähtepunktina teiste mudelite loomisel, mida saab peenhäälestada.

![Põhimudelid võrreldes LLM-idega](../../../translated_images/et/FoundationModel.e4859dbb7a825c94.webp)

Pildi allikas: [Essential Guide to Foundation Models and Large Language Models | by Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Selle eristuse võrdlemiseks võtame ajaloolise näitena ChatGPT. Varem kasutasid ChatGPT varased versioonid GPT-3.5 põhimudelit. OpenAI kasutas seejärel vestlusspetsiifilisi andmeid ja joondustehnikaid, et luua häälestatud versioon, mis toimib paremini vestlussituatsioonides, nagu vestlusrobotid. Kaasaegsed AI teenused marsruutivad tihti mitme mudelivariandi vahel, seega teenuse nimi ja aluseks oleva mudeli nimi ei ole alati sama.

![Põhimudel](../../../translated_images/et/Multimodal.2c389c6439e0fc51.webp)

Pildi allikas: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Avatud-kaalude/avatud lähtekoodiga mudelid versus patenteeritud mudelid

Veel üks viis LLM-ide kategoriseerimiseks on see, kas need on avatud-kaalude (open-weight), avatud lähtekoodiga või patenteeritud mudelid.

Avatud lähtekoodiga ja avatud-kaalude mudelid teevad mudeli artefaktid kättesaadavaks ülevaate, allalaadimise või kohandamise jaoks, kuid nende litsentsitingimused erinevad. Mõned on täiesti avatud lähtekoodiga, teised on avatud-kaalude mudelid kasutuspiirangutega. Need võivad olla kasulikud, kui ettevõte vajab suuremat kontrolli juurutuse, andmete lokaalsuse, kulude või kohandamise üle. Kuid meeskonnad peavad siiski enne tootmiskasutusse võtmist üle vaatama litsentsitingimusi, teeninduskulusid, hooldust, turvauuendusi ja hinnangu kvaliteeti. Näitena võib tuua [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst), mõned [Mistral mudelid](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst) ja palju mudeleid, mis on majutatud [Hugging Face’i platvormil](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst).

Patenteeritud mudelid kuuluvad ja neid majutab teenusepakkuja. Need mudelid on tihti optimeeritud hallatuks tootmiskasutuseks ning pakuvad tugevat tuge, turvasüsteeme, tööriistade integratsiooni ja skaleerimist. Kuid kliendid ei saa tavaliselt mudeli kaalusid uurida ega muuta ning peavad üle vaatama pakkuja tingimused privaatsuse, säilitamise, vastavuse ja sobiliku kasutuse osas. Näideteks on [OpenAI mudelid](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), [Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst) ja [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst).

### Manustamine versus pildiloome versus teksti ja koodi generatsioon

LLM-e saab ka kategoriseerida vastavalt väljundile, mida nad genereerivad.

Manustamised on mudeleid, mis suudavad muuta teksti numbriliseks vormiks, mida nimetatakse manustamiseks (embedding), mis on sisendi teksti numbriline esitlus. Manustamised lihtsustavad masinatele sõnade või lausetevaheliste seoste mõistmist ning neid saab kasutada sisenditena teiste mudelite, näiteks klassifitseerimis- või klasterdamismudelite jaoks, mis töötlevad numbrilisi andmeid paremini. Manustamismudeleid kasutatakse sageli ülekandeõppes, kus mudel on ehitatud asendusülesandele, mille jaoks on palju andmeid, ja siis mudeli kaalud (manustused) taaskasutatakse muude ülesannete jaoks. Selle kategooria näide on [OpenAI manustamised](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Manustamine](../../../translated_images/et/Embedding.c3708fe988ccf760.webp)

Pildiloome mudelid on mudelid, mis genereerivad pilte. Neid kasutatakse sageli pildi redigeerimiseks, sünteesiks ja tõlkeks. Pildiloome mudeleid treenitakse sageli suurel hulgal pildistandardeid, nagu [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), ja neid saab kasutada uute piltide loomiseks või olemasolevate piltide redigeerimiseks inpainting’i, super-resolutsiooni ja värvimise tehnikate abil. Näideteks on [GPT pildimudelid](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst), [Stable Diffusion mudelid](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst) ja Imagen mudelid.

![Pildiloome](../../../translated_images/et/Image.349c080266a763fd.webp)

Teksti ja koodi generatsiooni mudelid on mudelid, mis genereerivad teksti või koodi. Neid kasutatakse sageli teksti kokkuvõtmiseks, tõlkimiseks ja küsimustele vastamiseks. Tekstigeneratsiooni mudeleid treenitakse suurel hulgal tekstandmetel, nagu [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), ja neid saab kasutada uue teksti loomiseks või küsimustele vastamiseks. Koodigeneratsioonimudeleid, nagu [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), treenitakse sageli suurel hulgal koodil, näiteks GitHub’is, ja neid saab kasutada uue koodi genereerimiseks või olemasolevate vigade parandamiseks.

![Teksti ja koodi generatsioon](../../../translated_images/et/Text.a8c0cf139e5cc2a0.webp)

### Kodeerija-Dekodeerija versus Ainult dekodeerija

LLM-ide erinevate arhitektuuride selgitamiseks kasutame analoogiat.

Kujutle, et su juht andis sulle ülesandeks koostada viktoriin õpilastele. Sul on kaks kolleegi; üks vastutab sisu loomise eest ja teine ülevaatamise eest.

Sisulooja on nagu ainult dekodeerija mudel: ta suudab vaadata teemat, näha, mida sa oled juba kirjutanud, ja jätkata sisu genereerimist selle põhjal. Nad on väga head kaasahaarava ja informatiivse sisu kirjutamisel, kuid ei ole alati parim valik, kui ülesandeks on vaid klassifitseerimine, andmete tagasivõtmine või kodeerimine. Ainult dekodeerija mudelite perekonda kuuluvad näiteks GPT ja Llama mudelid.

Ülevaataja on nagu ainult kodeerija mudel: nad vaatavad kursust ja vastuseid, märkides nendevahelist seost ja mõistes konteksti, kuid nad ei ole head sisu genereerimisel. Ainult kodeerijate näide on BERT.

Kujutle, et meil on keegi, kes suudab nii viktoriini luua kui ka üle vaadata; see on kodeerija-dekodeerija mudel. Näideteks on BART ja T5.

### Teenus versus Mudel

Räägime nüüd teenuse ja mudeli erinevusest. Teenus on pilveteenuse pakkuja pakutav toode ja see on sageli mudelite, andmete ja muude komponentide kombinatsioon. Mudel on teenuse tuumakomponent ja see on sageli põhimudel, nagu LLM.

Teenused on sageli optimeeritud tootmiskasutuseks ning neid on tavaliselt lihtsam kasutada, näiteks graafilise kasutajaliidese kaudu. Kuid teenused ei ole alati tasuta ning võivad nõuda tellimust või tasu kasutamise eest, vastutasuks teenuse omaniku seadmetele ja ressurssidele juurdepääsu eest, kulude optimeerimise ja skaleerimise hõlbustamiseks. Näiteks on [Azure OpenAI teenus](https://learn.microsoft.com/azure/ai-foundry/openai/overview?WT.mc_id=academic-105485-koreyst), mis pakub kasutuspõhist hinnakava, mis tähendab, et kasutajalt võetakse tasu proportsionaalselt teenuse kasutusmahuga. Azure OpenAI teenus pakub ka ettevõtte tasemel turvalisust ja vastutustundliku tehisintellekti raamistikku mudelite võimete peale.

Mudelid on närvivõrgu artefaktid: parameetrid, kaalud, arhitektuur, tokeniseerija ja toetuskonfiguratsioonid. Mudeli kohalikuks või privaatseks jooksutamiseks on vaja sobivat riistvara, teenindustaristut, monitooringut ning kas ühilduvat avatud lähtekoodi/ava-kaalude litsentsi või ärilitsentsi. Avatud-kaaludega mudelid, nagu Llama 4 või Mistral mudelid, võivad töötada isemajutatult, kuid nõuavad siiski arvutusvõimsust ja operatiivset kompetentsi.

## Kuidas testida ja iteratiivselt parandada erinevaid mudeleid Azure’is, et mõista sooritust


Kui meie meeskond on uurinud praegust LLM-ide maastikku ja tuvastanud mõningad sobivad kandidaadid nende stsenaariumite jaoks, on järgmine samm nende testimine nende andmete ja töökoormuse peal. See on iteratiivne protsess, mida tehakse katsete ja mõõtmiste abil.
Enamik mudeleid, mida mainisime eelnevates lõikudes (OpenAI mudelid, avatud kaaludega mudelid nagu Llama 4 ja Mistral ning Hugging Face mudelid) on saadaval [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst) platvormil.

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst), varem tuntud kui Azure AI Studio/Azure AI Foundry, on ühtne Azure platvorm tehisintellekti rakenduste ja agentide loomiseks. See aitab arendajatel hallata kogu elu tsüklit alates eksperimenteerimisest ja hindamisest kuni juurutamise, jälgimise ja halduseni. Microsoft Foundry mudeliloend võimaldab kasutajal:

- Leida huvipakkuv alustaloenduses olev mudel, sealhulgas Azure'i müüdavad mudelid ja partnerite ning kogukonna pakkujate mudelid. Kasutajad saavad filtreerida ülesande, pakkuja, litsentsi, juurutamise valiku või nime järgi.

![Model catalog](../../../translated_images/et/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- Vaadata mudelikaarti, mis sisaldab põhjalikku kirjeldust kavandatud kasutusest ja koolitusandmetest, koodinäiteid ja hindamistulemusi sisemiste hindamisraamatukogude kohta.

![Model card](../../../translated_images/et/ModelCard.598051692c6e400d.webp)

- Võrrelda tööstuses saadaolevate mudelite ja andmekogude võrdlusaluseid, et hinnata, milline mudel vastab äristsenaariumile, kasutades [Model Benchmarks](https://learn.microsoft.com/azure/ai-foundry/concepts/model-benchmarks?WT.mc_id=academic-105485-koreyst) paneeli.

![Model benchmarks](../../../translated_images/et/ModelBenchmarks.254cb20fbd06c03a.webp)

- Peenhäälestada toetatud mudeleid kohandatud koolitusandmetel, et parandada mudeli tulemuslikkust konkreetse töökoormuse puhul, kasutades Microsoft Foundry eksperimenteerimise ja jälgimise võimalusi.

![Model fine-tuning](../../../translated_images/et/FineTuning.aac48f07142e36fd.webp)

- Juurutada originaalne eel-koolitatud mudel või peenhäälestatud versioon kaugemal reaalajas inference lõpp-punktile, kasutades hallatud arvutusvõimsust või serverivabasid juurutamisvalikuid, et võimaldada rakendustel seda tarbida.

![Model deployment](../../../translated_images/et/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> Kõik loendis olevad mudelid ei ole hetkel saadaval peenhäälestamiseks ja/või tasulise kasutusega juurutamiseks. Vaata mudelikaarti, et saada teavet mudeli võimekuste ja piirangute kohta.

## LLM-tulemuste parandamine

Oleme oma idufirma meeskonnaga uurinud erinevaid LLM-e ja pilveplatvormi (Microsoft Foundry), mis võimaldab meil võrrelda erinevaid mudeleid, hinnata neid testandmetel, parandada tulemuslikkust ning juurutada neid inference lõpp-punktidesse.

Kuid millal tuleks kaaluda mudeli peenhäälestamist, mitte-eel-koolitatud mudeli kasutamist? Kas on veel teisi lähenemisviise, kuidas mudeli tulemuslikkust konkreetsetel töökoormustel parandada?

Ettevõte saab kasutada mitmeid lähenemisviise, et saada LLM-ilt vajalikke tulemusi. LLM-i juurutamisel tootmises saab valida erinevaid mudelitüüpe erineva koolitusastmega, millel on erinev keerukus, kulud ja kvaliteet. Siin on mõned erinevad lähenemised:

- **Konteksti põhine prompti loomine**. Idee on anda piisavalt konteksti prompti juures, et kindlustada vajalike vastuste saamine.

- **Andmete põhine täiendus, Retrieval Augmented Generation, RAG**. Teie andmed võivad näiteks asuda andmebaasis või veebipunktis, et kindlustada nende andmete või selle alamhulga kaasamine prompti ajal, saate hankida asjakohased andmed ja lisada need kasutaja prompti osaks.

- **Peenhäälestatud mudel**. Siin on mudel edasi koolitatud teie enda andmetel, mis teeb mudeli täpsemaks ja vastuvõtlikumaks teie vajadustele, kuid see võib olla kallis.

![LLMs deployment](../../../translated_images/et/Deploy.18b2d27412ec8c02.webp)

Pildiallikas: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Prompti loomine konteksti põhjal

Eel-koolitatud LLM-id töötavad väga hästi üldistatud loomuliku keele ülesannetes, isegi kui neid kutsuda lühikese promptiga, näiteks lause lõpetamiseks või küsimuseks – nn „zero-shot” õppimine.

Kuid mida rohkem kasutaja suudab oma päringut piirata üksikasjaliku taotluse ja näidetega – ehk kontekstiga –, seda täpsem ja ootustele lähem vastus on. Sellel juhul räägime „one-shot” õppimisest, kui prompt sisaldab ainult ühte näidet, ja „few-shot” õppimisest, kui see sisaldab mitut näidet.
Prompti loomine konteksti põhjal on kõige kulutõhusam lähenemine alustamiseks.

### Retrieval Augmented Generation (RAG)

LLM-ide piirang on see, et nad saavad kasutusele võtta ainult koolitusel kasutatud andmeid vastuse genereerimiseks. See tähendab, et nad ei tea midagi faktidest, mis toimusid pärast koolitusprotsessi ning neil puudub juurdepääs mitteavalikele andmetele (näiteks ettevõtte andmed).
Seda saab ületada RAG-iga, tehnika abil, mis täiendab prompti väliste andmetega dokumentide fragmentide vormis, arvestades prompti pikkuse piiranguid. Selle võimaldavad vektorandmebaasi tööriistad (nagu [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)), mis otsivad kasulikke fragmente erinevatest eelmääratletud andmeallikatest ja lisavad need prompti konteksti.

See tehnika on väga kasulik, kui ettevõttel pole piisavalt andmeid, aega või ressursse LLM-i peenhäälestamiseks, kuid soovib siiski parandada tulemuslikkust konkreetse töökoormuse puhul ja vähendada hallutsineeritud, aegunud või toetamatute vastuste riski.

### Peenhäälestatud mudel

Peenhäälestamine on protsess, mis kasutab siirdeõpet mudeli „kohandamiseks“ allülesandeks või konkreetse probleemi lahendamiseks. Erinevalt väheste näidete õppest ja RAG-ist, moodustab see uue mudeli, millel on värskendatud kaalud ja nihked. Selleks on vaja koolitusnäidete komplekti, mis koosneb ühest sisendist (prompt) ja selle vastavast väljundist (täiendamine).
See oleks eelistatud lähenemine juhul, kui:

- **Väiksemate konkreetsete ülesannetega mudelite kasutamine**. Ettevõte sooviks peenhäälestada väiksema mudeli kitsale ülesandele, mitte korduvalt kutsuda suuremat piirimudelit, mis annab kulutõhusama ja kiirem lahenduse.

- **Latentsusajaga arvestamine**. Latentsus on konkreetse kasutusjuhtumi puhul oluline, seega ei saa kasutada väga pikki promte ega ka liiga palju näiteid, mida mudel peaks õppima, kui need ei sobi prompti pikkuse piiranguga.

- **Stabiilse käitumise kohandamine**. Ettevõttel on palju kvaliteetseid näiteid ja nad soovivad, et mudel järjekindlalt järgiks ülesande mustrit, väljundiformaati, tooni või domeenipõhist stiili. Kui peamine probleem on värsked faktid või sageli muutuva privaatteadmise olemasolu, siis kasutage RAG-i selle asemel, et tugineda üksnes peenhäälestamisele.

### Koolitatud mudel

LLM-i nullist koolitamine on kindlasti kõige raskem ja keerulisem lähenemine, mis nõuab tohutuid andmemahte, oskustega ressursse ja sobivat arvutusvõimsust. Seda võimalust tuleks arvestada ainult juhul, kui ettevõttel on domeenipõhine kasutusjuhtum ja suur hulk domeenikeskseid andmeid.

## Teadmiste kontroll

Milline võiks olla hea lähenemine LLM-i täienduste tulemustele?

1. Prompti loomine konteksti põhjal
1. RAG
1. Peenhäälestatud mudel

V: Kõik kolm aitavad. Alustage prompti loomise ja kontekstiga kiirete täiustuste jaoks ning kasutage RAG-i, kui mudel vajab ajakohaseid fakte või privaatseid ärilisi andmeid. Valige peenhäälestamine, kui teil on piisavalt kvaliteetseid näiteid ja soovite, et mudel järjekindlalt järgiks ülesande, vormingu, tooni või domeeni mustrit.

## 🚀 Väljakutse

Loe rohkem sellest, kuidas saad oma äri jaoks [kasutada RAG-i](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst).

## Suurepärane töö, jätka õppimist

Pärast selle õppetunni lõpetamist vaata meie [Generative AI õppekogu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), et jätkata generatiivse tehisintellekti teadmiste arendamist!

Liigu 3. õppetundi, kus vaatleme, kuidas [luua generatiivse tehisintellektiga vastutustundlikult](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->