[![Odprtokodni modeli](../../../translated_images/sl/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Natančna prilagoditev vašega LLM

Uporaba velikih jezikovnih modelov za izdelavo generativnih AI aplikacij prinaša nove izzive. Ključna težava je zagotavljanje kakovosti odzivov (natančnost in relevantnost) v vsebini, ki jo model generira za dano uporabniško zahtevo. V prejšnjih lekcijah smo obravnavali tehnike, kot so oblikovanje pozivov in generacija, dopolnjena z iskanjem, ki poskušajo rešiti problem z _modifikacijo vhodnega poziva_ v obstoječ model.

V današnji lekciji bomo razpravljali o tretji tehniki, **natančni prilagoditvi**, ki poskuša izziv rešiti z _ponovnim usposabljanjem samega modela_ z dodatnimi podatki. Poglobimo se v podrobnosti.

## Cilji učenja

Ta lekcija uvaja koncept natančne prilagoditve za vnaprej naučene jezikovne modele, raziskuje prednosti in izzive tega pristopa ter nudi napotke, kdaj in kako uporabiti natančno prilagoditev za izboljšanje zmogljivosti vaših generativnih AI modelov.

Ob koncu te lekcije boste lahko odgovorili na naslednja vprašanja:

- Kaj je natančna prilagoditev za jezikovne modele?
- Kdaj in zakaj je natančna prilagoditev koristna?
- Kako lahko natančno prilagodim vnaprej naučen model?
- Kakšne so omejitve natančne prilagoditve?

Ste pripravljeni? Začnimo.

## Ilustriran vodnik

Želite najprej dobiti celoten pregled tega, kar bomo pokrili? Oglejte si ta ilustriran vodnik, ki opisuje učni proces za to lekcijo - od učenja osnovnih pojmov in motivacije za natančno prilagajanje do razumevanja procesa in najboljših praks za izvedbo naloge natančne prilagoditve. To je fascinantna tema za raziskovanje, zato ne pozabite obiskati strani [Viri](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) za dodatne povezave, ki bodo podprle vašo samostojno učno pot!

![Ilustriran vodnik za natančno prilagajanje jezikovnih modelov](../../../translated_images/sl/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Kaj je natančna prilagoditev za jezikovne modele?

Po definiciji so veliki jezikovni modeli _vnaprej naučeni_ na velikih količinah besedil, pridobljenih iz različnih virov, vključno z internetom. Kot smo se naučili v prejšnjih lekcijah, potrebujemo tehnike, kot sta _oblikovanje pozivov_ in _generacija, dopolnjena z iskanjem_, za izboljšanje kakovosti odzivov modela na uporabnikova vprašanja ("pozive").

Ena priljubljena tehnika oblikovanja pozivov vključuje usmerjanje modela z več navodili, kaj se pričakuje v odgovoru, bodisi z zagotavljanjem _navodil_ (izrecna usmeritev) bodisi z _dajanjem nekaj primerov_ (implicitna usmeritev). To imenujemo _učenje z nekaj primeri_, vendar ima dve omejitvi:

- Omejitve glede števila tokenov modela lahko omejijo število primerov, ki jih lahko podate, in zmanjšajo učinkovitost.
- Stroški tokenov modela lahko povzročijo visoke stroške pri dodajanju primerov vsakemu pozivu in omejijo prilagodljivost.

Natančna prilagoditev je pogosta praksa v sistemih strojnega učenja, kjer vzamemo vnaprej naučen model in ga ponovno usposobimo z novimi podatki, da izboljšamo njegovo zmogljivost pri določeni nalogi. V kontekstu jezikovnih modelov lahko natančno prilagodimo vnaprej naučen model _z izbrano zbirko primerov za določeno nalogo ali področje uporabe_, da ustvarimo **prilagojen model**, ki je lahko natančnejši in bolj relevanten za to specifično nalogo ali področje. Dodatna prednost natančne prilagoditve je, da lahko zmanjša število primerov, potrebnih za učenje z nekaj primeri - s tem zmanjša porabo tokenov in s tem povezane stroške.

## Kdaj in zakaj naj bi modele natančno prilagajali?

V _tem_ kontekstu, ko govorimo o natančni prilagoditvi, mislimo na **nadzorovano** natančno prilagoditev, kjer se ponovno usposabljanje izvaja z **dodajanjem novih podatkov**, ki niso bili del prvotnega učnega nabora. To se razlikuje od nenadzorovane natančne prilagoditve, kjer je model ponovno usposobljen na originalnih podatkih, a z drugačnimi hiperparametri.

Glavna stvar, ki si jo morate zapomniti, je, da je natančna prilagoditev napredna tehnika, ki zahteva določeno stopnjo strokovnosti, da dosežete želene rezultate. Če je izvedena napačno, morda ne bo prinesla pričakovanih izboljšav in lahko celo poslabša zmogljivost modela za vaše ciljno področje.

Torej, preden se naučite "kako" natančno prilagoditi jezikovne modele, morate vedeti "zakaj" bi morali izbrati to pot in "kdaj" začeti postopek natančne prilagoditve. Začnite z zastavljanjem naslednjih vprašanj:

- **Primer uporabe**: Kakšen je vaš _primer uporabe_ za natančno prilagoditev? Kateri vidik trenutnega vnaprej naučenega modela želite izboljšati?
- **Alternativa**: Ste poskusili _druge tehnike_ za dosego želenih rezultatov? Uporabite jih za ustvarjanje primerjalne osnovne točke.
  - Oblikovanje pozivov: Poskusite tehnike, kot je učenje z nekaj primeri z relevantnimi odzivi na pozive. Ocenite kakovost odgovorov.
  - Generacija, dopolnjena z iskanjem: Poskusite dopolniti pozive z iskalnimi rezultati iz vaših podatkov. Ocenite kakovost odgovorov.
- **Stroški**: Ste ugotovili stroške natančne prilagoditve?
  - Prilagodljivost - ali je vnaprej naučeni model na voljo za natančno prilagoditev?
  - Napor - za pripravo učnih podatkov, ocenjevanje in izboljševanje modela.
  - Računalniški viri - za izvajanje nalog natančne prilagoditve in za nameščanje prilagojenega modela.
  - Podatki - dostop do dovolj kakovostnih primerov za vpliv natančne prilagoditve
- **Koristi**: Ste preverili koristi natančne prilagoditve?
  - Kakovost - ali je prilagojeni model presegel osnovo?
  - Stroški - ali zmanjša porabo tokenov z poenostavitvijo pozivov?
  - Razširljivost - ali lahko osnovni model uporabite za nova področja?

Z odgovori na ta vprašanja bi morali lahko odločiti, ali je natančna prilagoditev prava pot za vaš primer. Idealno je, če je pristop veljaven le, če koristi odtehtajo stroške. Ko se odločite napredovati, je čas, da razmislite, _kako_ lahko natančno prilagodite vnaprej naučen model.

Želite več vpogledov v postopek odločanja? Oglejte si [Natančna prilagoditev ali ne](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Kako lahko natančno prilagodimo vnaprej naučen model?

Za natančno prilagoditev vnaprej naučenega modela potrebujete:

- vnaprej naučen model za natančno prilagoditev
- podatkovni niz za natančno prilagoditev
- učno okolje za izvajanje naloge natančne prilagoditve
- gostiteljsko okolje za nameščanje prilagojenega modela

## Natančna prilagoditev v praksi

> **Opomba:** Model `gpt-35-turbo` / `gpt-3.5-turbo`, na katerega se sklicujejo nekateri spodnji tutoriali, je upokojeni za tako inferenco kot natančno prilagoditev. Če danes začenjate novo nalogo natančne prilagoditve, ciljate na trenutno podprt model, na primer `gpt-4o-mini` ali `gpt-4.1-mini`. Oglejte si [Seznam modelov za natančno prilagoditev](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) za trenutno ponudbo natančno prilagodljivih modelov. Koncepti in koraki v teh tutorialih so še vedno uporabni.

Naslednji viri nudijo tutoriale korak za korakom, ki vas skozi primer vodijo z izbranim modelom in skrbno izbranim podatkovnim nizom. Za delo s temi tutoriali potrebujete račun pri določenem ponudniku ter dostop do ustreznega modela in podatkovnih nizov.

| Ponudnik    | Tutorial                                                                                                                                                                     | Opis                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Kako natančno prilagoditi klepetalne modele](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst) | Naučite se natančno prilagoditi model `gpt-35-turbo` za specifično področje ("pomoč pri receptih") z pripravo učnih podatkov, izvajanjem naloge natančne prilagoditve in uporabo prilagojenega modela za inferenco.                                                                                                                                                                                                               |
| Azure OpenAI | [Tutorial za natančno prilagoditev GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst) | Naučite se natančno prilagoditi model `gpt-35-turbo-0613` **na Azure** z ukrepi ustvarjanja in nalaganja učnih podatkov, izvajanjem naloge natančne prilagoditve. Uporabite in namestite nov model.                                                                                                                                                                                                                                 |
| Hugging Face | [Natančna prilagoditev LLM-jev z Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                       | Ta blog vodi skozi natančno prilagoditev _odprtega LLM-ja_ (npr: `CodeLlama 7B`) z uporabo knjižnice [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) z odprtimi [podatkovnimi nizi](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) na Hugging Face.               |
|              |                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 🤗 AutoTrain | [Natančna prilagoditev LLM-jev z AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                               | AutoTrain (ali AutoTrain Advanced) je pythonova knjižnica, ki jo je razvil Hugging Face in omogoča natančno prilagoditev za različne naloge, vključno z natančno prilagoditvijo LLM-jev. AutoTrain je rešitev brez kode, prilagoditev pa je mogoča v vašem oblaku, na Hugging Face Spaces ali lokalno. Podpira spletni GUI, CLI in učenje preko yaml konfiguracijskih datotek.                                                             |
|              |                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 🦥 Unsloth | [Natančna prilagoditev LLM-jev z Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                               | Unsloth je odprtokodni okvir, ki podpira natančno prilagoditev LLM-jev in okrepljeno učenje (RL). Unsloth poenostavlja lokalno učenje, ocenjevanje in nameščanje s pripravljenimi [zvezki](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Podpira tudi pretvorbo besedila v govor (TTS), BERT in multimodalne modele. Za začetek preberite njihov korak-po-korak [Vodnik za natančno prilagoditev LLM-jev](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide). |
|              |                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
## Naloga

Izberite enega izmed zgornjih tutorialov in ga prehodite. _Morda bomo v tem repozitoriju ustvarili različico teh tutorialov v Jupyter Notesnikih za referenco. Za najnovejše različice pa prosim uporabljajte neposredno izvirne vire_.

## Odlično delo! Nadaljujte z učenjem.

Po opravljeni lekciji si oglejte našo [Zbirko za učenje generativne umetne inteligence](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadaljujete z nadgrajevanjem svojega znanja o generativni AI!

Čestitke!! Zaključili ste zadnjo lekcijo serije v2 tega tečaja! Ne prenehajte z učenjem in ustvarjanjem. \*\*Oglejte si stran z [VIRI](RESOURCES.md?WT.mc_id=academic-105485-koreyst) za seznam dodatnih priporočil prav za to temo.

Naša serija lekcij v1 je bila prav tako posodobljena z več nalogami in koncepti. Vzemite si minuto za obnovo znanja – in prosimo [delite svoja vprašanja in povratne informacije](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst), da nam pomagate izboljšati te lekcije za skupnost.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->