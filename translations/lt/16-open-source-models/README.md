<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85b754d4dc980f270f264d17116d9a5f",
  "translation_date": "2025-12-19T17:52:33+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "lt"
}
-->
[![Atviro kodo modeliai](../../../translated_images/16-lesson-banner.6b56555e8404fda1.lt.png)](https://youtu.be/CuICgfuHFSg?si=x8SpFRUsIxM9dohN)

## Įvadas

Atvirojo kodo LLM pasaulis yra įdomus ir nuolat besikeičiantis. Šios pamokos tikslas – išsamiai apžvelgti atvirojo kodo modelius. Jei ieškote informacijos, kaip savininkiški modeliai lyginami su atvirojo kodo modeliais, eikite į ["Skirtingų LLM tyrinėjimo ir palyginimo" pamoką](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Šioje pamokoje taip pat bus aptariama smulkiojo derinimo tema, tačiau išsamesnį paaiškinimą rasite ["LLM smulkusis derinimas" pamokoje](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Mokymosi tikslai

- Suprasti atvirojo kodo modelius
- Suprasti darbo su atvirojo kodo modeliais privalumus
- Tyrinėti atvirus modelius, prieinamus Hugging Face ir Azure AI Studio platformose

## Kas yra atvirojo kodo modeliai?

Atvirojo kodo programinė įranga vaidino svarbų vaidmenį technologijų augime įvairiose srityse. Atvirojo kodo iniciatyva (OSI) apibrėžė [10 kriterijų programinei įrangai](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst), kad ji būtų priskirta atvirajam kodui. Šaltinio kodas turi būti viešai prieinamas pagal OSI patvirtintą licenciją.

Nors LLM kūrimas turi panašumų su programinės įrangos kūrimu, procesas nėra visiškai tas pats. Tai sukėlė daug diskusijų bendruomenėje apie atvirojo kodo apibrėžimą LLM kontekste. Kad modelis atitiktų tradicinį atvirojo kodo apibrėžimą, turėtų būti viešai prieinama ši informacija:

- Duomenų rinkiniai, naudoti modeliui treniruoti.
- Pilni modelio svoriai kaip treniravimo dalis.
- Vertinimo kodas.
- Smulkiojo derinimo kodas.
- Pilni modelio svoriai ir treniravimo metrika.

Šiuo metu yra tik keletas modelių, atitinkančių šiuos kriterijus. [OLMo modelis, sukurtas Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) yra vienas iš jų.

Šioje pamokoje toliau modelius vadinsime „atvirais modeliais“, nes jie gali neatitikti aukščiau nurodytų kriterijų rašymo metu.

## Atvirų modelių privalumai

**Labai pritaikomi** – Kadangi atviri modeliai išleidžiami su išsamiomis treniravimo detalėmis, tyrėjai ir kūrėjai gali keisti modelio vidinius elementus. Tai leidžia kurti labai specializuotus modelius, smulkiai derintus konkrečiai užduočiai ar sričiai. Pavyzdžiai – kodo generavimas, matematiniai veiksmai ir biologija.

**Kaina** – Kaina už žetoną naudojant ir diegiant šiuos modelius yra mažesnė nei savininkiškų modelių. Kuriant generatyviosios AI programas, svarbu įvertinti našumą ir kainą, dirbant su šiais modeliais savo atveju.

![Modelio kaina](../../../translated_images/model-price.3f5a3e4d32ae00b4.lt.png)
Šaltinis: Artificial Analysis

**Lankstumas** – Darbas su atvirais modeliais leidžia būti lanksčiam renkantis skirtingus modelius arba juos derinant. Pavyzdys – [HuggingChat asistentai](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst), kur vartotojas gali tiesiogiai vartotojo sąsajoje pasirinkti naudojamą modelį:

![Pasirinkite modelį](../../../translated_images/choose-model.f095d15bbac92214.lt.png)

## Skirtingų atvirų modelių tyrinėjimas

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), sukurtas Meta, yra atviras modelis, optimizuotas pokalbių programoms. Tai lemia jo smulkiojo derinimo metodas, apimantis daug dialogų ir žmogaus atsiliepimų. Šiuo metodu modelis generuoja rezultatus, labiau atitinkančius žmogaus lūkesčius, kas suteikia geresnę vartotojo patirtį.

Kai kurie smulkiai derinti Llama versijų pavyzdžiai yra [Japonų Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), specializuotas japonų kalboje, ir [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), kuris yra patobulinta bazinio modelio versija.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) yra atviras modelis, orientuotas į aukštą našumą ir efektyvumą. Jis naudoja ekspertų mišinio (Mixture-of-Experts) metodą, kuris sujungia grupę specializuotų ekspertų modelių į vieną sistemą, kurioje, priklausomai nuo įvesties, pasirenkami tam tikri modeliai. Tai leidžia efektyviau skaičiuoti, nes modeliai apdoroja tik tuos įėjimus, kuriuose yra specializuoti.

Kai kurie smulkiai derinti Mistral versijų pavyzdžiai yra [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), orientuotas į medicinos sritį, ir [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), atliekantis matematinius skaičiavimus.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) yra LLM, sukurtas Technology Innovation Institute (**TII**). Falcon-40B buvo treniruotas su 40 milijardų parametrų ir įrodyta, kad jis veikia geriau nei GPT-3, naudojant mažesnį skaičiavimo biudžetą. Tai pasiekta naudojant FlashAttention algoritmą ir multiquery dėmesį, kurie sumažina atminties poreikius inferencijos metu. Dėl sumažinto inferencijos laiko Falcon-40B tinka pokalbių programoms.

Kai kurie smulkiai derinti Falcon versijų pavyzdžiai yra [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), asistentas, sukurtas ant atvirų modelių, ir [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), kuris pasižymi geresniu našumu nei bazinis modelis.

## Kaip pasirinkti

Nėra vieno atsakymo, kaip pasirinkti atvirą modelį. Geras pradžios taškas – naudoti Azure AI Studio filtrą pagal užduotį. Tai padės suprasti, kokiems uždaviniams modelis buvo treniruotas. Hugging Face taip pat palaiko LLM lyderių lentelę, kurioje rodomi geriausiai veikiančių modelių rezultatai pagal tam tikrus rodiklius.

Ieškant LLM palyginimų tarp skirtingų tipų, [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) yra dar viena puiki priemonė:

![Modelio kokybė](../../../translated_images/model-quality.aaae1c22e00f7ee1.lt.png)
Šaltinis: Artificial Analysis

Dirbant su konkrečiu atveju, efektyvu ieškoti smulkiai derintų versijų, orientuotų į tą pačią sritį. Eksperimentavimas su keliais atvirais modeliais, siekiant įvertinti jų veikimą pagal jūsų ir vartotojų lūkesčius, taip pat yra gera praktika.

## Tolimesni žingsniai

Geriausia atvirų modelių dalis yra ta, kad galite greitai pradėti su jais dirbti. Peržiūrėkite [Azure AI Foundry Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), kuriame yra speciali Hugging Face kolekcija su šiomis čia aptartomis modelių versijomis.

## Mokymasis čia nesibaigia, tęskite kelionę

Baigę šią pamoką, peržiūrėkite mūsų [Generatyvios AI mokymosi kolekciją](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kad toliau gilintumėte savo žinias apie generatyviąją AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingus aiškinimus, kylančius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->