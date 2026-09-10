[![Open Source Models](../../../translated_images/sl/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Natančna nastavitev vašega LLM

Uporaba velikih jezikovnih modelov za gradnjo generativnih AI aplikacij prinaša nove izzive. Ključno vprašanje je zagotavljanje kakovosti odziva (natančnost in relevantnost) v vsebini, ki jo model ustvari za določen uporabniški zahtevek. V prejšnjih lekcijah smo obravnavali tehnike, kot sta inženiring pozivov in generacija z izboljšavo pridobivanja, ki skušajo rešiti problem z _modifikacijo vhodnega poziva_ za obstoječi model.

V današnji lekciji bomo obravnavali tretjo tehniko, **natančno nastavitev (fine-tuning)**, ki skuša izziv rešiti z _ponovnim usposabljanjem samega modela_ z dodatnimi podatki. Poglobili se bomo v podrobnosti.

## Cilji učenja

Ta lekcija uvaja koncept natančne nastavitve za vnaprej usposobljene jezikovne modele, raziskuje prednosti in izzive tega pristopa ter ponuja smernice o tem, kdaj in kako uporabiti natančno nastavitev za izboljšanje zmogljivosti vaših generativnih AI modelov.

Ob koncu te lekcije boste lahko odgovorili na naslednja vprašanja:

- Kaj je natančna nastavitev za jezikovne modele?
- Kdaj in zakaj je natančna nastavitev koristna?
- Kako lahko natančno nastavim vnaprej usposobljen model?
- Kakšne so omejitve natančne nastavitve?

Ste pripravljeni? Začnimo.

## Ilustriran vodič

Želite dobiti splošen pregled tega, kar bomo obravnavali, preden se poglobite? Oglejte si ta ilustrirani vodič, ki opisuje pot učenja za to lekcijo - od učenja osnovnih konceptov in motivacije za natančno nastavitev do razumevanja postopka in najboljših praks za izvedbo naloge natančne nastavitve. To je fascinantna tema za raziskovanje, zato ne pozabite obiskati strani z [viri](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) za dodatne povezave, ki podpirajo vaše samostojno učenje!

![Ilustrirani vodič za natančno nastavitev jezikovnih modelov](../../../translated_images/sl/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Kaj je natančna nastavitev za jezikovne modele?

Po definiciji so veliki jezikovni modeli _vnaprej usposobljeni_ na velikih količinah besedil, pridobljenih iz različnih virov, vključno z internetom. Kot smo se naučili v prejšnjih lekcijah, potrebujemo tehnike, kot sta _inženiring pozivov_ in _generacija z izboljšavo pridobivanja_, da izboljšamo kakovost odzivov modela na vprašanja uporabnika ("pozive").

Priljubljena tehnika inženiringa pozivov vključuje dajanje modelu več navodil o tem, kaj se pričakuje v odgovoru, bodisi s posredovanjem _navodil_ (izrecna usmeritev) ali _dajanjem nekaj primerov_ (neizrecna usmeritev). To imenujemo _učenje z nekaj primeri_, vendar ima dve omejitvi:

- Omejitve modelnih tokenov lahko omejijo število primerov, ki jih lahko navedete, in omejijo učinkovitost.
- Stroški tokenov modela lahko povzročijo visoke stroške dodajanja primerov v vsak poziv in omejijo prilagodljivost.

Natančna nastavitev je pogosta praksa v sistemih strojnega učenja, kjer vzamemo vnaprej usposobljen model in ga ponovno usposobimo z novimi podatki, da izboljšamo njegovo zmogljivost za določeno nalogo. V kontekstu jezikovnih modelov lahko natančno nastavimo vnaprej usposobljen model _z izbranim naborom primerov za določeno nalogo ali domeno uporabe_, da ustvarimo **prilagojen model**, ki je lahko bolj natančen in relevanten za to nalogo ali domeno. Vedeti dodatna korist natančne nastavitve je, da lahko zmanjša število primerov, potrebnih za učenje z nekaj primeri - kar zmanjša uporabo tokenov in povezane stroške.

## Kdaj in zakaj naj natančno nastavimo modele?

V _tem_ kontekstu, ko govorimo o natančni nastavitvi, se nanašamo na **nadzorovano** natančno nastavitev, kjer se ponovno usposabljanje izvaja z **dodajanjem novih podatkov**, ki niso bili del izvornega nabora podatkov za usposabljanje. To se razlikuje od nenadzorovanega pristopa k natančni nastavitvi, kjer je model ponovno usposobljen na izvirnih podatkih, vendar z drugačnimi hiperparametri.

Ključna stvar, ki si jo je treba zapomniti, je, da je natančna nastavitev napredna tehnika, ki zahteva določeno stopnjo strokovnega znanja za dosego želenih rezultatov. Če je izvedena nepravilno, morda ne bo prinesla pričakovanih izboljšav in lahko celo poslabša delovanje modela za ciljno domeno.

Zato, preden se naučite "kako" natančno nastaviti jezikovne modele, morate vedeti "zakaj" bi morali iti po tej poti in "kdaj" začeti proces natančne nastavitve. Začnite z zastavljanjem teh vprašanj:

- **Primer uporabe:** Kakšen je vaš _primer uporabe_ za natančno nastavitev? Kateri vidik trenutnega vnaprej usposobljenega modela želite izboljšati?
- **Alternativne metode:** Ste poskusili _druge tehnike_ za dosego želenih rezultatov? Uporabite jih, da ustvarite osnovno primerjavo.
  - Inženiring pozivov: Poskusite tehnike, kot je učenje z nekaj primeri z relevantnimi odgovori na pozive. Ocenite kakovost odgovorov.
  - Generacija z izboljšavo pridobivanja: Poskusite dopolniti pozive z rezultati poizvedb, pridobljenimi z iskanjem v vaših podatkih. Ocenite kakovost odgovorov.
- **Stroški:** Ste določili stroške natančne nastavitve?
  - Prilagodljivost - ali je vnaprej usposobljen model na voljo za natančno nastavitev?
  - Prizadevanje - za pripravo podatkov za usposabljanje, ocenjevanje in izboljševanje modela.
  - Računalniški viri - za izvajanje nalog natančne nastavitve in nameščanje natančno nastavljenega modela.
  - Podatki - dostop do dovolj kakovostnih primerov za vpliv natančne nastavitve.
- **Koristi:** Ste potrdili koristi natančne nastavitve?
  - Kakovost - ali je natančno nastavljen model presegel osnovno raven?
  - Stroški - ali zmanjšuje uporabo tokenov s poenostavitvijo pozivov?
  - Razširljivost - ali lahko osnovni model uporabite za nove domene?

Z odgovori na ta vprašanja bi morali vedeti, ali je natančna nastavitev pravi pristop za vaš primer uporabe. Idealno je, da je pristop veljaven samo, če koristi presegajo stroške. Ko se odločite nadaljevati, je čas, da premislite, _kako_ lahko natančno nastavite vnaprej usposobljen model.

Želite pridobiti več vpogledov v proces odločanja? Oglejte si [Natančna nastavitev ali ne](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Kako lahko natančno nastavimo vnaprej usposobljen model?

Za natančno nastavitev vnaprej usposobljenega modela potrebujete:

- vnaprej usposobljen model za natančno nastavitev
- nabor podatkov za uporabo pri natančni nastavitvi
- okolje za usposabljanje, v katerem boste izvajali nalogo natančne nastavitve
- gostiteljsko okolje za nameščanje natančno nastavljenega modela

## Natančna nastavitev na Microsoft Foundry

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) je mesto, kjer danes natančno nastavljate, nameščate in upravljate prilagojene modele na Azure (združuje prej Azure OpenAI Studio in Azure AI Studio). Pred začetkom naloge je koristno razumeti izbire, ki jih Foundry ponuja – in najboljše prakse, ki jih platforma priporoča. Pod pokrovom uporablja Foundry **LoRA (low-rank adaptation)** za učinkovito natančno nastavitev modelov, kar omogoča hitrejše in cenovno ugodnejše usposabljanje, kot če bi ponastavili vse uteži.

### Korak 1: Izberite metodo usposabljanja

Foundry podpira tri tehnike natančne nastavitve. **Začnite z SFT** - pokriva najs širši nabor scenarijev.

| Tehnika | Kaj počne | Kdaj jo uporabiti |
| --- | --- | --- |
| **Nadzorovana natančna nastavitev (SFT)** | Usposablja na parih vhod/izhoda, da se model nauči proizvajati želene odgovore. | Privzeta za večino nalog: specializacija domene, zmogljivost naloge, slog in ton, sledenje navodilom ter jezikovna prilagoditev. |
| **Neposredna optimizacija preferenc (DPO)** | Uči se na podlagi parov _prednostnih proti nepripravnim_ odgovorov za uskladitev rezultatov s človeškimi preferencami. | Izboljšanje kakovosti odgovorov, varnosti in usklajenosti, kadar imate primerjalne povratne informacije. |
| **Okrepljena natančna nastavitev (RFT)** | Uporablja nagrajevalne signale od _ocenjevalcev_ za optimizacijo kompleksnih vedenj z okrepljenim učenjem. | Objektivne, močno premišljene domene (matematika, kemija, fizika) s jasnimi pravimi/napačnimi odgovori. Zahteva več strokovnega znanja o strojni inteligenci. |

### Korak 2: Izberite raven usposabljanja

Foundry vam omogoča izbiro, kako in kje se izvaja usposabljanje:

- **Standard** – usposablja v regiji vašega vira in zagotavlja rezidentnost podatkov. Uporabite, kadar morajo podatki ostati znotraj določene regije.
- **Globalno** – cenejše in hitrejše v čakalni vrsti, saj izkorišča kapacitete izven vaše regije (podatki in uteži se kopirajo v regijo usposabljanja). Dobra izbira, ko rezidentnost podatkov ni zahteva.
- **Razvijalec** – najnižji stroški, uporablja neaktivne kapacitete brez zagotovil o latenci/SLA-ju (naloge se lahko prekinejo in nadaljujejo). Idealno za eksperimentiranje.

### Korak 3: Izberite osnovni model

Modeli, ki jih je mogoče natančno nastaviti, vključujejo OpenAI `gpt-4o-mini`, `gpt-4o`, `gpt-4.1`, `gpt-4.1-mini` in `gpt-4.1-nano` (SFT; družina 4o/4.1 podpira tudi DPO), modele za razmišljanje `o4-mini` in `gpt-5` (RFT), ter odprtokodne modele, kot so `Ministral-3B`, `Qwen-32B`, `Llama-3.3-70B-Instruct` in `gpt-oss-20b` (SFT na Foundry virov). Vedno preverite aktualni [Seznam modelov za natančno nastavitev](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst) za podprte metode, regije in razpoložljivost.

> Foundry ponuja dve modaliteti: **brez strežnika** (cenik glede na porabo, brez upravljanja kvote GPU, OpenAI in izbrani modeli) in **upravljani računalniški viri** (prinesite svoje VM-je prek Azure Machine Learning za najs širok nabor modelov). Večina naj začne z brez strežnika.

### Najboljše prakse Foundry

- **Najprej baza.** Izmerite osnovni model z inženiringom pozivov in RAG _preden_ ga natančno nastavite, da dokažete napredek.
- **Začnite majhno, nato razširite.** Začnite s 50-100 visokokakovostnimi primeri za potrditev pristopa, nato povečajte na 500+ za proizvodnjo. Kakovost premaga količino - odstranite nizkokakovostne primere.
- **Pravilno oblikujte podatke.** Datoteke za usposabljanje in preverjanje morajo biti JSONL, UTF-8 **z BOM**, manjše od 512 MB, z uporabo formata sporočil za chat completions. Vedno vključite datoteko za preverjanje, da lahko spremljate preučeno prileganje.
- **Ohranjajte sistemski poziv pri inferenci.** Uporabite isti sistemski poziv, kot ste ga uporabili med usposabljanjem, ko kličete model.
- **Ocenjujte kontrolne točke - ne nameščajte slepo zadnje.** Foundry hrani zadnje tri epoh kot kontrolne točke za namestitev; izberite tisto, ki se najbolje generalizira, tako da spremljate `train_loss` / `valid_loss` in natančnost tokenov.
- **Izmerite stroške tokenov skupaj s kakovostjo** pri primerjavi natančno nastavljenega modela z osnovnim.
- **Iterirajte z neprekinjeno natančno nastavitvijo.** Lahko natančno nastavite že natančno nastavljen model z novimi podatki (podprto za OpenAI modele).
- **Bodite pozorni na stroške gostovanja.** Izdelek prilagojen model zaračunava na uro, neaktiven izdelek pa se odstrani po 15 dneh - počistite, česar ne potrebujete.

Sledite celovitemu vodniku v [Prilagodite model z natančno nastavitvijo](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) in si oglejte vodiče za [DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst) in [RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst), ko boste pripravljeni na druge tehnike.

## Natančna nastavitev v praksi

Naslednji viri ponujajo korak-po-koraku vodiče, ki vas vodijo skozi resnični primer na trenutno podprt model z izbranim naborom podatkov. Za delo z njimi potrebujete račun pri določenem ponudniku ter dostop do ustreznega modela in podatkovnih nizov.

| Ponudnik     | Vodič                                                                                                                                                                        | Opis                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Kako natančno nastaviti modele za pogovor](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst) | Naučite se natančno nastaviti nedavni OpenAI model za klepet za specifično domeno ("pomočnik za recepte") s pripravo podatkov za usposabljanje, izvedbo naloge natančne nastavitve in uporabo natančno nastavljenega modela za sklepanje.                                                                                                                                                                                          |
| Microsoft Foundry | [Prilagodite model z natančno nastavitvijo](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Naučite se natančno nastaviti trenutno podprt model, kot je `gpt-4.1-mini`, **na Azure** z Microsoft Foundry: pripravite in naložite podatke za usposabljanje in preverjanje, zaženite nalogo natančne nastavitve, nato namestite in uporabite nov model.                                                                                                                                                                             |

| Hugging Face | [Fino nastavljanje LLM-ov z Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Ta blog zapis vas vodi skozi fino nastavljanje _odprtega LLM-ja_ (npr.: `CodeLlama 7B`) z uporabo knjižnice [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) in [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) z odprtimi [nabori podatkov](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) na Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Fino nastavljanje LLM-ov z AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (ali AutoTrain Advanced) je python knjižnica, ki jo je razvil Hugging Face in omogoča fino nastavljanje za številne različne naloge, vključno s fino nastavitvijo LLM-ov. AutoTrain je rešitev brez kode in fino nastavljanje lahko izvedete v svojem oblaku, na Hugging Face Spaces ali lokalno. Podpira tako spletni GUI, CLI in usposabljanje preko yaml konfiguracijskih datotek.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Fino nastavljanje LLM-ov z Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth je odprtokodni okvir, ki podpira fino nastavljanje LLM-ov in učenje z okrepitvijo (RL). Unsloth poenostavlja lokalno usposabljanje, ocenjevanje in uvajanje z že pripravljenimi [zvezki](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Prav tako podpira pretvorbo besedila v govor (TTS), BERT in multimodalne modele. Za začetek preberite njihov korak-po-korak [Vodnik za fino nastavljanje LLM-ov](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Naloga

Izberite enega od zgornjih vodičev in ga prehodite. _Morda bomo v tem repozitoriju za referenco ustvarili različico teh vodičev v Jupyter Notebooks. Prosimo, uporabite izvirne vire za najnovejše različice_.

## Odlično delo! Nadaljujte z učenjem.

Po zaključku te lekcije si oglejte našo [Generativno AI zbirko za učenje](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadaljujete z nadgrajevanjem svojega znanja o Generativni AI!

Čestitamo!! Zaključili ste zadnjo lekcijo iz serije v2 tega tečaja! Ne prenehajte z učenjem in ustvarjanjem. \*\*Oglejte si stran [VIRI](RESOURCES.md?WT.mc_id=academic-105485-koreyst) za seznam dodatnih predlogov ravno za to temo.

Naša serija lekcij v1 je prav tako posodobljena z več nalogami in koncepti. Vzemite si trenutek za osvežitev znanja - in prosimo, [delite svoja vprašanja in povratne informacije](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst), da nam pomagate izboljšati te lekcije za skupnost.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->