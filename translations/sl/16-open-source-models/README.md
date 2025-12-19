<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85b754d4dc980f270f264d17116d9a5f",
  "translation_date": "2025-12-19T17:28:36+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "sl"
}
-->
[![Open Source Models](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.sl.png)](https://youtu.be/CuICgfuHFSg?si=x8SpFRUsIxM9dohN)

## Uvod

Svet odprtokodnih LLM-jev je razburljiv in se nenehno razvija. Ta lekcija si prizadeva zagotoviti poglobljen vpogled v odprtokodne modele. Če iščete informacije o tem, kako se lastniški modeli primerjajo z odprtokodnimi modeli, pojdite na lekcijo ["Raziskovanje in primerjava različnih LLM-jev"](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Ta lekcija bo prav tako obravnavala temo fino nastavljanja, vendar lahko podrobnejšo razlago najdete v lekciji ["Fino nastavljanje LLM-jev"](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Cilji učenja

- Pridobiti razumevanje odprtokodnih modelov
- Razumevanje koristi dela z odprtokodnimi modeli
- Raziskovanje odprtih modelov, ki so na voljo na Hugging Face in Azure AI Studio

## Kaj so odprtokodni modeli?

Odprtokodna programska oprema je igrala ključno vlogo pri rasti tehnologije na različnih področjih. Iniciativa za odprto kodo (OSI) je opredelila [10 meril za programsko opremo](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst), da se lahko klasificira kot odprtokodna. Izvorna koda mora biti javno deljena pod licenco, ki jo odobri OSI.

Čeprav ima razvoj LLM-jev podobne elemente kot razvoj programske opreme, postopek ni povsem enak. To je povzročilo veliko razprav v skupnosti o definiciji odprte kode v kontekstu LLM-jev. Da bi bil model usklajen s tradicionalno definicijo odprte kode, bi morale biti javno dostopne naslednje informacije:

- Podatkovni nizi, uporabljeni za usposabljanje modela.
- Polne uteži modela kot del usposabljanja.
- Koda za ocenjevanje.
- Koda za fino nastavljanje.
- Polne uteži modela in metrike usposabljanja.

Trenutno obstaja le nekaj modelov, ki ustrezajo tem merilom. [OLMo model, ki ga je ustvaril Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) je eden izmed njih.

Za to lekcijo bomo modele naprej imenovali "odprti modeli", saj morda v času pisanja ne ustrezajo zgornjim merilom.

## Prednosti odprtih modelov

**Zelo prilagodljivi** - Ker so odprti modeli izdani z podrobnimi informacijami o usposabljanju, lahko raziskovalci in razvijalci spreminjajo notranjost modela. To omogoča ustvarjanje zelo specializiranih modelov, ki so fino nastavljeni za določen nalogo ali področje študija. Nekateri primeri tega so generiranje kode, matematične operacije in biologija.

**Stroški** - Stroški na token za uporabo in uvajanje teh modelov so nižji kot pri lastniških modelih. Pri gradnji aplikacij Generativne AI je treba upoštevati razmerje med zmogljivostjo in ceno pri delu s temi modeli za vaš primer uporabe.

![Model Cost](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.sl.png)
Vir: Artificial Analysis

**Fleksibilnost** - Delo z odprtimi modeli vam omogoča fleksibilnost pri uporabi različnih modelov ali njihovi kombinaciji. Primer tega so [HuggingChat asistenti](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst), kjer lahko uporabnik neposredno v uporabniškem vmesniku izbere model, ki se uporablja:

![Choose Model](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.sl.png)

## Raziskovanje različnih odprtih modelov

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), ki ga je razvil Meta, je odprt model, optimiziran za aplikacije, ki temeljijo na klepetu. To je posledica njegove metode fino nastavljanja, ki je vključevala veliko količino dialoga in povratnih informacij ljudi. S to metodo model proizvaja rezultate, ki so bolj usklajeni s pričakovanji ljudi, kar zagotavlja boljšo uporabniško izkušnjo.

Nekateri primeri fino nastavljenih različic Llama vključujejo [japonski Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), ki je specializiran za japonščino, in [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), ki je izboljšana različica osnovnega modela.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) je odprt model s poudarkom na visoki zmogljivosti in učinkovitosti. Uporablja pristop mešanice strokovnjakov (Mixture-of-Experts), ki združuje skupino specializiranih strokovnih modelov v en sistem, kjer se glede na vhod izberejo določeni modeli za uporabo. To naredi izračun bolj učinkovit, saj modeli obravnavajo le tiste vhode, na katerih so specializirani.

Nekateri primeri fino nastavljenih različic Mistral vključujejo [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), ki je osredotočen na medicinsko področje, in [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), ki izvaja matematične izračune.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) je LLM, ki ga je ustvaril Technology Innovation Institute (**TII**). Falcon-40B je bil usposobljen na 40 milijardah parametrov, kar je pokazalo boljše rezultate kot GPT-3 z manjšo porabo računalniških virov. To je posledica uporabe algoritma FlashAttention in multiquery pozornosti, ki omogočata zmanjšanje zahtev po pomnilniku med izvajanjem. Zaradi skrajšanega časa izvajanja je Falcon-40B primeren za klepetalne aplikacije.

Nekateri primeri fino nastavljenih različic Falcon so [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), asistent zgrajen na odprtih modelih, in [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), ki nudi boljšo zmogljivost kot osnovni model.

## Kako izbrati

Za izbiro odprtega modela ni enega samega odgovora. Dobro izhodišče je uporaba funkcije filtriranja po nalogi v Azure AI Studiu. To vam bo pomagalo razumeti, za katere vrste nalog je bil model usposobljen. Hugging Face prav tako vzdržuje LLM lestvico, ki prikazuje najboljše modele glede na določene metrike.

Če želite primerjati LLM-je med različnimi vrstami, je [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) še en odličen vir:

![Model Quality](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.sl.png)
Vir: Artificial Analysis

Če delate na specifičnem primeru uporabe, je lahko učinkovito iskati fino nastavljene različice, ki so osredotočene na isto področje. Eksperimentiranje z več odprtimi modeli, da vidite, kako delujejo glede na vaša in pričakovanja vaših uporabnikov, je prav tako dobra praksa.

## Naslednji koraki

Najboljše pri odprtih modelih je, da lahko z njimi začnete delati zelo hitro. Oglejte si [Azure AI Foundry Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), ki vsebuje posebno zbirko Hugging Face s temi modeli, o katerih smo tukaj govorili.

## Učenje se tukaj ne konča, nadaljujte pot

Po zaključku te lekcije si oglejte našo [zbirko za učenje Generativne AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadaljujete z nadgradnjo svojega znanja o Generativni AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->