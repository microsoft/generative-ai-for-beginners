<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df44972d5575ea8cef3c52ee31696d04",
  "translation_date": "2025-12-19T17:22:50+00:00",
  "source_file": "14-the-generative-ai-application-lifecycle/README.md",
  "language_code": "hr"
}
-->
[![Integracija s pozivanjem funkcija](../../../translated_images/14-lesson-banner.066d74a31727ac12.hr.png)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Životni ciklus generativne AI aplikacije

Važno pitanje za sve AI aplikacije je relevantnost AI značajki, budući da je AI brzo razvijajuće područje, kako biste osigurali da vaša aplikacija ostane relevantna, pouzdana i robusna, morate je kontinuirano pratiti, ocjenjivati i poboljšavati. Tu dolazi do izražaja životni ciklus generativne AI.

Životni ciklus generativne AI je okvir koji vas vodi kroz faze razvoja, implementacije i održavanja generativne AI aplikacije. Pomaže vam definirati ciljeve, mjeriti izvedbu, identificirati izazove i provoditi rješenja. Također vam pomaže uskladiti vašu aplikaciju s etičkim i pravnim standardima vaše domene i dionika. Slijedeći životni ciklus generativne AI, možete osigurati da vaša aplikacija uvijek pruža vrijednost i zadovoljava vaše korisnike.

## Uvod

U ovom poglavlju ćete:

- Razumjeti paradigmu pomaka od MLOps do LLMOps
- Životni ciklus LLM-a
- Alati za životni ciklus
- Metrifikacija i evaluacija životnog ciklusa

## Razumjeti paradigmu pomaka od MLOps do LLMOps

LLM-ovi su novi alat u arsenalu umjetne inteligencije, izuzetno su moćni u zadacima analize i generiranja za aplikacije, no ta moć ima neke posljedice u načinu na koji pojednostavljujemo AI i klasične zadatke strojnog učenja.

S tim nam je potrebna nova paradigma za prilagodbu ovog alata na dinamičan način, s ispravnim poticajima. Možemo starije AI aplikacije kategorizirati kao "ML aplikacije", a novije AI aplikacije kao "GenAI aplikacije" ili jednostavno "AI aplikacije", što odražava glavnu tehnologiju i tehnike korištene u to vrijeme. Ovo pomiče naš narativ na više načina, pogledajte sljedeću usporedbu.

![Usporedba LLMOps i MLOps](../../../translated_images/01-llmops-shift.29bc933cb3bb0080.hr.png)

Primijetite da se u LLMOps više fokusiramo na programere aplikacija, koristeći integracije kao ključnu točku, koristeći "Modeli kao usluga" i razmišljajući o sljedećim točkama za metrike.

- Kvaliteta: Kvaliteta odgovora
- Šteta: Odgovorna AI
- Iskrenost: Utemeljenost odgovora (Ima li smisla? Je li točno?)
- Trošak: Budžet rješenja
- Latencija: Prosječno vrijeme za odgovor tokena

## Životni ciklus LLM-a

Prvo, da bismo razumjeli životni ciklus i izmjene, pogledajmo sljedeću infografiku.

![Infografika LLMOps](../../../translated_images/02-llmops.70a942ead05a7645.hr.png)

Kao što možete primijetiti, ovo je drugačije od uobičajenih životnih ciklusa iz MLOps-a. LLM-ovi imaju mnogo novih zahtjeva, kao što su promptiranje, različite tehnike za poboljšanje kvalitete (fino podešavanje, RAG, meta-promptovi), različita procjena i odgovornost s odgovornom AI, te na kraju nove metrike evaluacije (kvaliteta, šteta, iskrenost, trošak i latencija).

Na primjer, pogledajte kako zamišljamo ideje. Koristeći inženjering promptova za eksperimentiranje s različitim LLM-ovima kako bismo istražili mogućnosti i testirali jesu li njihove hipoteze točne.

Imajte na umu da ovo nije linearno, već integrirani petlje, iterativno i s nadređenim ciklusom.

Kako bismo mogli istražiti te korake? Pogledajmo detaljnije kako bismo mogli izgraditi životni ciklus.

![Radni tijek LLMOps](../../../translated_images/03-llm-stage-flows.3a1e1c401235a6cf.hr.png)

Ovo može izgledati malo komplicirano, usredotočimo se prvo na tri velika koraka.

1. Ideacija/Istraživanje: Istraživanje, ovdje možemo istraživati prema našim poslovnim potrebama. Prototipiranje, stvaranje [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) i testiranje je li dovoljno učinkovit za našu hipotezu.
1. Izgradnja/Proširenje: Implementacija, sada počinjemo ocjenjivati veće skupove podataka, primjenjujemo tehnike poput fino podešavanja i RAG-a kako bismo provjerili robusnost našeg rješenja. Ako ne uspije, ponovna implementacija, dodavanje novih koraka u naš tijek ili restrukturiranje podataka može pomoći. Nakon testiranja našeg tijeka i skaliranja, ako radi i provjerimo naše metrike, spremni smo za sljedeći korak.
1. Operacionalizacija: Integracija, sada dodajemo sustave nadzora i upozorenja u naš sustav, implementaciju i integraciju aplikacije u našu aplikaciju.

Zatim imamo nadređeni ciklus upravljanja, fokusiran na sigurnost, usklađenost i upravljanje.

Čestitamo, sada imate svoju AI aplikaciju spremnu za rad i operativnu. Za praktično iskustvo, pogledajte [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

Sada, koje alate možemo koristiti?

## Alati za životni ciklus

Za alate, Microsoft pruža [Azure AI Platformu](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) i [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) koji olakšavaju i čine vaš ciklus jednostavnim za implementaciju i spremnim za korištenje.

[Azure AI Platforma](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) omogućuje vam korištenje [AI Studija](https://ai.azure.com/?WT.mc_id=academic-105485-koreys). AI Studio je web portal koji vam omogućuje istraživanje modela, primjera i alata. Upravljanje vašim resursima, UI razvojnim tijekovima i SDK/CLI opcijama za razvoj s kodom kao prvim pristupom.

![Mogućnosti Azure AI](../../../translated_images/04-azure-ai-platform.80203baf03a12fa8.hr.png)

Azure AI omogućuje vam korištenje više resursa za upravljanje vašim operacijama, uslugama, projektima, potrebama za vektorskim pretraživanjem i bazama podataka.

![LLMOps s Azure AI](../../../translated_images/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.hr.png)

Izgradite, od dokaza koncepta (POC) do aplikacija velikih razmjera s PromptFlow:

- Dizajnirajte i izgradite aplikacije iz VS Code-a, s vizualnim i funkcionalnim alatima
- Testirajte i fino podesite svoje aplikacije za kvalitetnu AI, s lakoćom.
- Koristite Azure AI Studio za integraciju i iteraciju s oblakom, push i implementaciju za brzu integraciju.

![LLMOps s PromptFlow](../../../translated_images/06-llm-promptflow.a183eba07a3a7fdf.hr.png)

## Odlično! Nastavite s učenjem!

Nevjerojatno, sada saznajte više o tome kako strukturiramo aplikaciju da koristimo koncepte s [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), da provjerite kako Cloud Advocacy dodaje te koncepte u demonstracije. Za više sadržaja, pogledajte našu [Ignite breakout sesiju!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Sada, pogledajte Lekciju 15, da razumijete kako [Retrieval Augmented Generation i vektorske baze podataka](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) utječu na generativnu AI i kako napraviti zanimljivije aplikacije!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->