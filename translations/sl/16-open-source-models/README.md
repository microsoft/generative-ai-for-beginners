<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a83aac52158c23161046cbd13faa2b",
  "translation_date": "2025-10-18T01:47:27+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "sl"
}
-->
[![Open Source Models](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.sl.png)](https://youtu.be/CuICgfuHFSg?si=x8SpFRUsIxM9dohN)

## Uvod

Svet odprtokodnih LLM-jev je vznemirljiv in se nenehno razvija. Namen te lekcije je podrobneje predstaviti odprtokodne modele. Če iščete informacije o primerjavi lastniških modelov z odprtokodnimi modeli, obiščite lekcijo ["Raziskovanje in primerjava različnih LLM-jev"](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Ta lekcija bo obravnavala tudi temo prilagajanja modelov, vendar podrobnejšo razlago najdete v lekciji ["Prilagajanje LLM-jev"](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Cilji učenja

- Razumevanje odprtokodnih modelov
- Razumevanje prednosti dela z odprtokodnimi modeli
- Raziskovanje odprtih modelov, ki so na voljo na platformah Hugging Face in Azure AI Studio

## Kaj so odprtokodni modeli?

Odprtokodna programska oprema je igrala ključno vlogo pri razvoju tehnologije na različnih področjih. Pobuda za odprtokodno programsko opremo (OSI) je določila [10 kriterijev za programsko opremo](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst), da jo lahko klasificiramo kot odprtokodno. Izvorna koda mora biti javno dostopna pod licenco, ki jo odobri OSI.

Čeprav razvoj LLM-jev vključuje podobne elemente kot razvoj programske opreme, proces ni povsem enak. To je v skupnosti sprožilo veliko razprav o definiciji odprtokodnosti v kontekstu LLM-jev. Da bi model ustrezal tradicionalni definiciji odprtokodnosti, morajo biti javno dostopne naslednje informacije:

- Podatkovne zbirke, uporabljene za učenje modela.
- Polne uteži modela kot del učenja.
- Koda za evalvacijo.
- Koda za prilagajanje.
- Polne uteži modela in metrične vrednosti učenja.

Trenutno obstaja le nekaj modelov, ki ustrezajo tem kriterijem. [Model OLMo, ki ga je ustvaril Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst), je eden izmed njih.

V tej lekciji bomo modele v nadaljevanju imenovali "odprti modeli", saj morda ne ustrezajo zgoraj navedenim kriterijem v času pisanja.

## Prednosti odprtih modelov

**Visoka prilagodljivost** - Ker so odprti modeli objavljeni z natančnimi informacijami o učenju, lahko raziskovalci in razvijalci spreminjajo notranjo strukturo modela. To omogoča ustvarjanje zelo specializiranih modelov, ki so prilagojeni za določeno nalogo ali področje raziskovanja. Nekateri primeri vključujejo generiranje kode, matematične operacije in biologijo.

**Stroški** - Stroški na žeton za uporabo in implementacijo teh modelov so nižji kot pri lastniških modelih. Pri gradnji aplikacij za generativno umetno inteligenco je treba upoštevati razmerje med zmogljivostjo in ceno glede na vaš primer uporabe.

![Model Cost](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.sl.png)  
Vir: Artificial Analysis

**Prilagodljivost** - Delo z odprtimi modeli omogoča prilagodljivost pri uporabi različnih modelov ali njihovi kombinaciji. Primer tega je [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst), kjer lahko uporabnik neposredno v uporabniškem vmesniku izbere model, ki se uporablja:

![Choose Model](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.sl.png)

## Raziskovanje različnih odprtih modelov

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), ki ga je razvil Meta, je odprti model, optimiziran za aplikacije, ki temeljijo na klepetu. To je posledica metode prilagajanja, ki je vključevala veliko količino dialogov in povratnih informacij uporabnikov. S to metodo model ustvarja rezultate, ki so bolj usklajeni s pričakovanji ljudi, kar zagotavlja boljšo uporabniško izkušnjo.

Nekateri primeri prilagojenih različic Llama vključujejo [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), ki se specializira za japonščino, in [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), ki je izboljšana različica osnovnega modela.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) je odprti model, ki se osredotoča na visoko zmogljivost in učinkovitost. Uporablja pristop Mixture-of-Experts, ki združuje skupino specializiranih ekspertnih modelov v en sistem, kjer se glede na vhodne podatke izberejo določeni modeli za uporabo. To omogoča bolj učinkovito računalniško obdelavo, saj modeli obravnavajo le vhodne podatke, za katere so specializirani.

Nekateri primeri prilagojenih različic Mistral vključujejo [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), ki se osredotoča na medicinsko področje, in [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), ki izvaja matematične izračune.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) je LLM, ki ga je ustvaril Technology Innovation Institute (**TII**). Falcon-40B je bil usposobljen na 40 milijardah parametrov, kar se je izkazalo za boljše od GPT-3 z manjšo porabo računalniških virov. To je posledica uporabe algoritma FlashAttention in večpoizvedbene pozornosti, ki omogočata zmanjšanje zahtev po pomnilniku med časom sklepanja. Zaradi zmanjšanega časa sklepanja je Falcon-40B primeren za aplikacije za klepet.

Nekateri primeri prilagojenih različic Falcon so [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), asistent, zgrajen na odprtih modelih, in [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), ki zagotavlja boljšo zmogljivost kot osnovni model.

## Kako izbrati

Ni enotnega odgovora na vprašanje, kako izbrati odprti model. Dober začetek je uporaba funkcije filtriranja po nalogah v Azure AI Studio. To vam bo pomagalo razumeti, za katere vrste nalog je bil model usposobljen. Hugging Face prav tako vzdržuje LLM Leaderboard, ki prikazuje najbolje delujoče modele glede na določene metrike.

Če želite primerjati LLM-je med različnimi vrstami, je [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) še en odličen vir:

![Model Quality](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.sl.png)  
Vir: Artificial Analysis

Če delate na specifičnem primeru uporabe, je lahko učinkovito iskati prilagojene različice, ki se osredotočajo na isto področje. Preizkušanje več odprtih modelov, da vidite, kako se obnašajo glede na vaša pričakovanja in pričakovanja vaših uporabnikov, je prav tako dobra praksa.

## Naslednji koraki

Najboljša stvar pri odprtih modelih je, da lahko z njimi začnete delati zelo hitro. Oglejte si [Azure AI Foundry Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), ki vključuje posebno zbirko Hugging Face z modeli, o katerih smo govorili tukaj.

## Učenje se tukaj ne konča, nadaljujte svojo pot

Po zaključku te lekcije si oglejte našo [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da še naprej poglabljate svoje znanje o generativni umetni inteligenci!

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj se šteje za avtoritativni vir. Za ključne informacije je priporočljivo profesionalno človeško prevajanje. Ne odgovarjamo za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.