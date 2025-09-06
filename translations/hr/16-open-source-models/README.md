<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8b2d4bb727c877ebf9edff8623d16b9",
  "translation_date": "2025-09-06T10:25:16+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "hr"
}
-->
[![Open Source Models](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.hr.png)](https://aka.ms/gen-ai-lesson16-gh?WT.mc_id=academic-105485-koreyst)

## Uvod

Svijet open-source LLM-ova je uzbudljiv i stalno se razvija. Ova lekcija ima za cilj pružiti detaljan pregled open-source modela. Ako tražite informacije o tome kako se vlasnički modeli uspoređuju s open-source modelima, posjetite lekciju ["Istraživanje i usporedba različitih LLM-ova"](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Ova lekcija također pokriva temu fine-tuninga, ali detaljnije objašnjenje možete pronaći u lekciji ["Fine-Tuning LLM-ova"](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Ciljevi učenja

- Steći razumijevanje open-source modela
- Razumjeti prednosti rada s open-source modelima
- Istražiti dostupne open modele na Hugging Face i Azure AI Studio

## Što su Open Source modeli?

Open-source softver igra ključnu ulogu u razvoju tehnologije u raznim područjima. Open Source Initiative (OSI) definirao je [10 kriterija za softver](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) kako bi se klasificirao kao open-source. Izvorni kod mora biti javno dostupan pod licencom koju je odobrio OSI.

Iako razvoj LLM-ova ima slične elemente kao razvoj softvera, proces nije potpuno isti. To je dovelo do mnogih rasprava u zajednici o definiciji open-source u kontekstu LLM-ova. Da bi model bio usklađen s tradicionalnom definicijom open-source, sljedeće informacije trebaju biti javno dostupne:

- Skupovi podataka korišteni za treniranje modela.
- Puni težinski parametri modela kao dio treniranja.
- Kod za evaluaciju.
- Kod za fine-tuning.
- Puni težinski parametri modela i metrički podaci o treniranju.

Trenutno postoji samo nekoliko modela koji zadovoljavaju ove kriterije. [OLMo model koji je kreirao Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) jedan je od njih.

Za ovu lekciju, modele ćemo nadalje nazivati "open modeli", jer možda ne zadovoljavaju gore navedene kriterije u trenutku pisanja.

## Prednosti Open modela

**Visoka prilagodljivost** - Budući da su open modeli objavljeni s detaljnim informacijama o treniranju, istraživači i programeri mogu mijenjati unutarnje dijelove modela. To omogućuje stvaranje visoko specijaliziranih modela koji su prilagođeni za određeni zadatak ili područje istraživanja. Neki primjeri uključuju generiranje koda, matematičke operacije i biologiju.

**Trošak** - Trošak po tokenu za korištenje i implementaciju ovih modela niži je od troška vlasničkih modela. Kada gradite aplikacije za generativnu umjetnu inteligenciju, trebali biste razmotriti omjer performansi i cijene u odnosu na vaš slučaj korištenja.

![Model Cost](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.hr.png)  
Izvor: Artificial Analysis

**Fleksibilnost** - Rad s open modelima omogućuje fleksibilnost u korištenju različitih modela ili njihovom kombiniranju. Primjer za to su [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst), gdje korisnik može odabrati model koji se koristi izravno u korisničkom sučelju:

![Choose Model](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.hr.png)

## Istraživanje različitih Open modela

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), koji je razvio Meta, open model je optimiziran za aplikacije temeljene na razgovoru. To je rezultat metode fine-tuninga, koja uključuje veliku količinu dijaloga i povratnih informacija od ljudi. Ova metoda omogućuje modelu da proizvodi rezultate koji su više usklađeni s ljudskim očekivanjima, što pruža bolje korisničko iskustvo.

Neki primjeri fine-tuniranih verzija Llama uključuju [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), koji se specijalizira za japanski jezik, i [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), koji je poboljšana verzija osnovnog modela.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) je open model s naglaskom na visoke performanse i učinkovitost. Koristi pristup Mixture-of-Experts, koji kombinira grupu specijaliziranih ekspertnih modela u jedan sustav, gdje se ovisno o ulazu odabiru određeni modeli za korištenje. To čini izračun učinkovitijim jer modeli obrađuju samo ulaze za koje su specijalizirani.

Neki primjeri fine-tuniranih verzija Mistral uključuju [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), koji je fokusiran na medicinsko područje, i [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), koji obavlja matematičke izračune.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) je LLM koji je kreirao Technology Innovation Institute (**TII**). Falcon-40B treniran je na 40 milijardi parametara, što se pokazalo boljim od GPT-3 uz manji proračunski kapacitet. To je rezultat korištenja FlashAttention algoritma i multiquery attention pristupa, koji omogućuju smanjenje zahtjeva za memorijom tijekom vremena izvođenja. S ovim smanjenim vremenom izvođenja, Falcon-40B je prikladan za aplikacije temeljene na razgovoru.

Neki primjeri fine-tuniranih verzija Falcon uključuju [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), asistenta izgrađenog na open modelima, i [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), koji pruža bolje performanse od osnovnog modela.

## Kako odabrati

Ne postoji jednoznačan odgovor na pitanje kako odabrati open model. Dobro mjesto za početak je korištenje značajke filtriranja po zadatku u Azure AI Studio. To će vam pomoći razumjeti za koje vrste zadataka je model treniran. Hugging Face također održava LLM Leaderboard, koji prikazuje najbolje modele prema određenim metrima.

Ako želite usporediti LLM-ove među različitim vrstama, [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) je još jedan odličan resurs:

![Model Quality](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.hr.png)  
Izvor: Artificial Analysis

Ako radite na specifičnom slučaju korištenja, traženje fine-tuniranih verzija koje su fokusirane na isto područje može biti učinkovito. Eksperimentiranje s više open modela kako biste vidjeli kako se ponašaju prema vašim i očekivanjima vaših korisnika također je dobra praksa.

## Sljedeći koraci

Najbolji dio kod open modela je što možete brzo započeti rad s njima. Pogledajte [Azure AI Foundry Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), koji sadrži specifičnu kolekciju Hugging Face modela koje smo ovdje spomenuli.

## Učenje ne prestaje ovdje, nastavite svoje putovanje

Nakon što završite ovu lekciju, pogledajte našu [Generative AI Learning kolekciju](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili unapređivati svoje znanje o generativnoj umjetnoj inteligenciji!

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.