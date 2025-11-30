<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a83aac52158c23161046cbd13faa2b",
  "translation_date": "2025-10-18T01:37:31+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "hr"
}
-->
[![Open Source Models](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.hr.png)](https://youtu.be/CuICgfuHFSg?si=x8SpFRUsIxM9dohN)

## Uvod

Svijet open-source LLM-ova je uzbudljiv i stalno se razvija. Ova lekcija ima za cilj pružiti detaljan pregled open-source modela. Ako tražite informacije o tome kako se vlasnički modeli uspoređuju s open-source modelima, posjetite lekciju ["Istraživanje i usporedba različitih LLM-ova"](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Ova lekcija također će obuhvatiti temu fine-tuninga, ali detaljnije objašnjenje možete pronaći u lekciji ["Fine-Tuning LLM-ova"](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Ciljevi učenja

- Razumjeti open-source modele
- Shvatiti prednosti rada s open-source modelima
- Istražiti dostupne open-source modele na Hugging Face i Azure AI Studio

## Što su open-source modeli?

Open-source softver igra ključnu ulogu u razvoju tehnologije u raznim područjima. Open Source Initiative (OSI) definirao je [10 kriterija za softver](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) kako bi se klasificirao kao open-source. Izvorni kod mora biti javno dostupan pod licencom koju je odobrio OSI.

Iako razvoj LLM-ova ima slične elemente kao i razvoj softvera, proces nije potpuno isti. To je izazvalo mnogo rasprava u zajednici o definiciji open-sourcea u kontekstu LLM-ova. Da bi model bio usklađen s tradicionalnom definicijom open-sourcea, sljedeće informacije trebale bi biti javno dostupne:

- Skupovi podataka korišteni za treniranje modela.
- Puni težinski parametri modela kao dio treniranja.
- Kod za evaluaciju.
- Kod za fine-tuning.
- Puni težinski parametri modela i metrički podaci o treniranju.

Trenutno postoji samo nekoliko modela koji zadovoljavaju ove kriterije. [OLMo model koji je kreirao Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) jedan je od njih.

Za ovu lekciju, modele ćemo nazivati "otvorenim modelima" jer možda ne zadovoljavaju gore navedene kriterije u trenutku pisanja.

## Prednosti otvorenih modela

**Visoka prilagodljivost** - Budući da su otvoreni modeli objavljeni s detaljnim informacijama o treniranju, istraživači i programeri mogu mijenjati unutarnje dijelove modela. To omogućuje stvaranje visoko specijaliziranih modela koji su prilagođeni za određeni zadatak ili područje istraživanja. Neki primjeri uključuju generiranje koda, matematičke operacije i biologiju.

**Trošak** - Trošak po tokenu za korištenje i implementaciju ovih modela niži je od troška vlasničkih modela. Prilikom izrade aplikacija za generativnu umjetnu inteligenciju, treba razmotriti omjer performansi i cijene u odnosu na vaš slučaj upotrebe.

![Model Cost](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.hr.png)  
Izvor: Artificial Analysis

**Fleksibilnost** - Rad s otvorenim modelima omogućuje fleksibilnost u korištenju različitih modela ili njihovoj kombinaciji. Primjer za to su [HuggingChat asistenti](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst) gdje korisnik može odabrati model koji se koristi izravno u korisničkom sučelju:

![Choose Model](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.hr.png)

## Istraživanje različitih otvorenih modela

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), koji je razvio Meta, otvoreni je model optimiziran za aplikacije temeljene na razgovoru. To je rezultat metode fine-tuninga koja uključuje veliku količinu dijaloga i povratnih informacija od ljudi. Ova metoda omogućuje modelu da proizvodi rezultate koji su više usklađeni s ljudskim očekivanjima, što pruža bolje korisničko iskustvo.

Neki primjeri fine-tuniranih verzija Llama uključuju [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), koji se specijalizira za japanski jezik, i [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), koji je poboljšana verzija osnovnog modela.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) je otvoreni model s naglaskom na visoke performanse i učinkovitost. Koristi pristup Mixture-of-Experts, koji kombinira grupu specijaliziranih ekspertnih modela u jedan sustav gdje se, ovisno o ulazu, odabiru određeni modeli za korištenje. To čini izračun učinkovitijim jer modeli obrađuju samo ulaze u kojima su specijalizirani.

Neki primjeri fine-tuniranih verzija Mistrala uključuju [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), koji je fokusiran na medicinsko područje, i [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), koji obavlja matematičke izračune.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) je LLM koji je kreirao Technology Innovation Institute (**TII**). Falcon-40B treniran je na 40 milijardi parametara, što se pokazalo boljim od GPT-3 uz manji proračunski kapacitet. To je rezultat korištenja algoritma FlashAttention i multiquery attention, koji omogućuju smanjenje zahtjeva za memorijom tijekom vremena izvođenja. S ovim smanjenim vremenom izvođenja, Falcon-40B je prikladan za aplikacije temeljene na razgovoru.

Neki primjeri fine-tuniranih verzija Falcona su [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), asistent izgrađen na otvorenim modelima, i [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), koji pruža bolje performanse od osnovnog modela.

## Kako odabrati

Ne postoji jednoznačan odgovor na pitanje kako odabrati otvoreni model. Dobar početak je korištenje značajke filtriranja prema zadatku u Azure AI Studio. To će vam pomoći da razumijete za koje vrste zadataka je model treniran. Hugging Face također održava LLM Leaderboard koji prikazuje najbolje modele prema određenim metrima.

Ako želite usporediti LLM-ove različitih vrsta, [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) je još jedan odličan resurs:

![Model Quality](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.hr.png)  
Izvor: Artificial Analysis

Ako radite na specifičnom slučaju upotrebe, učinkovito je potražiti fine-tunirane verzije koje su fokusirane na isto područje. Eksperimentiranje s više otvorenih modela kako biste vidjeli kako se ponašaju u skladu s vašim i očekivanjima vaših korisnika također je dobra praksa.

## Sljedeći koraci

Najbolji dio kod otvorenih modela je to što možete brzo započeti rad s njima. Pogledajte [Azure AI Foundry Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), koji sadrži specifičnu kolekciju Hugging Face modela o kojima smo ovdje raspravljali.

## Učenje ne prestaje ovdje, nastavite svoje putovanje

Nakon što završite ovu lekciju, pogledajte našu [Generative AI Learning kolekciju](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili unapređivati svoje znanje o generativnoj umjetnoj inteligenciji!

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne odgovaramo za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.