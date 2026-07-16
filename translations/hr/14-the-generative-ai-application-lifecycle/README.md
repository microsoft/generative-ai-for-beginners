[![Integracija s pozivanjem funkcija](../../../translated_images/hr/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Životni ciklus generativne AI aplikacije

Važno pitanje za sve AI aplikacije je relevantnost AI značajki, s obzirom da je AI brzo razvojno područje, kako bi vaša aplikacija ostala relevantna, pouzdana i robusna, potrebno ju je kontinuirano nadzirati, evaluirati i poboljšavati. Tu dolazi u pomoć životni ciklus generativne AI.

Životni ciklus generativne AI je okvir koji vas vodi kroz faze razvoja, implementacije i održavanja generativne AI aplikacije. Pomaže vam definirati ciljeve, mjeriti izvedbu, identificirati izazove i implementirati rješenja. Također pomaže uskladiti vašu aplikaciju s etičkim i pravnim standardima vaše domene i dionika. Slijeđenjem životnog ciklusa generativne AI, možete osigurati da vaša aplikacija uvijek pruža vrijednost i zadovoljava vaše korisnike.

## Uvod

U ovom poglavlju ćete:

- Razumjeti paradigmatični pomak s MLOps na LLMOps
- Životni ciklus LLM-a
- Alati za životni ciklus
- Metrika i evaluacija životnog ciklusa

## Razumjeti paradigmatični pomak s MLOps na LLMOps

LLM-ovi su novi alat u arsenalu umjetne inteligencije, iznimno su moćni u zadacima analize i generiranja za aplikacije, no ta moć donosi određene posljedice u načinu na koji pojednostavljujemo AI i klasične zadatke strojnog učenja.

Zbog toga nam treba novi paradigm za prilagodbu ovog alata u dinamičnom okruženju, s odgovarajućim poticajima. Starije AI aplikacije možemo kategorizirati kao "ML aplikacije", a novije AI aplikacije kao "GenAI aplikacije" ili jednostavno "AI aplikacije", što odražava mainstream tehnologiju i tehnike korištene u tom trenutku. To mijenja naš narativ na više načina, pogledajte sljedeću usporedbu.

![Usporedba LLMOps vs. MLOps](../../../translated_images/hr/01-llmops-shift.29bc933cb3bb0080.webp)

Primijetite da je u LLMOps više usmjereno na programere aplikacija, korištenje integracija kao ključne točke, korištenje "Modela kao usluge" i razmišljanje o sljedećim metrikama.

- Kvaliteta: Kvaliteta odgovora
- Šteta: Odgovoran AI
- Iskrenost: Temeljenost odgovora (Ima li smisla? Je li točno?)
- Trošak: Proračun rješenja
- Latencija: Prosječno vrijeme za odgovor tokena

## Životni ciklus LLM-a

Prvo, da bismo razumjeli životni ciklus i promjene, pogledajmo sljedeću infografiku.

![LLMOps infografika](../../../translated_images/hr/02-llmops.70a942ead05a7645.webp)

Kao što možete primijetiti, ovo je drugačije od uobičajenih životnih ciklusa u MLOps-u. LLM-i imaju mnogo novih zahtjeva, poput promptiranja, različitih tehnika za poboljšanje kvalitete (finog podešavanja, RAG, meta-promptova), različitih ocjena i odgovornosti s odgovornim AI-jem, te novih metrika evaluacije (Kvaliteta, Šteta, Iskrenost, Trošak i Latencija).

Na primjer, pogledajte kako osmišljavamo ideje. Koristeći prompt engineering za eksperimentiranje s različitim LLM-ovima kako bismo istražili mogućnosti i testirali jesu li njihove hipoteze točne.

Napomena, ovo nije linearno, već integrirani petlje, iterativno i s nadređenim ciklusom.

Kako bismo mogli istražiti te korake? Pogledajmo detaljno kako izgraditi životni ciklus.

![Radni tijek LLMOps](../../../translated_images/hr/03-llm-stage-flows.3a1e1c401235a6cf.webp)

Možda izgleda pomalo složeno, usredotočimo se prvo na tri glavna koraka.

1. Ideiranje/istraživanje: Istraživanje, ovdje možemo istražiti prema poslovnim potrebama. Prototipiranje, kreiranje [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) i testiranje je li dovoljno učinkovit za našu hipotezu.
1. Izgradnja/augmentacija: Implementacija, sada počinjemo evaluirati za veće skupove podataka i implementirati tehnike poput finog podešavanja i RAG-a, da provjerimo robusnost našeg rješenja. Ako ne uspije, ponovna implementacija, dodavanje novih koraka u tijek ili restrukturiranje podataka može pomoći. Nakon testiranja tijeka i skaliranja, ako radi i odgovara našim metrikama, spremni smo za sljedeći korak.
1. Operacionalizacija: Integracija, sada dodajemo sustave praćenja i upozorenja u naš sustav, implementaciju i integraciju aplikacije.

Zatim imamo nadređeni ciklus Upravljanja, usredotočen na sigurnost, usklađenost i upravljanje.

Čestitamo, sada imate svoju AI aplikaciju spremnu za rad i operativnu. Za praktično iskustvo, pogledajte [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)

Sada, koje alate možemo koristiti?

## Alati za životni ciklus

Za alate, Microsoft pruža [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) i [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) koji olakšavaju i čine vaš ciklus jednostavnim za implementaciju i spremnim za korištenje.

[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) omogućuje korištenje [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst). Microsoft Foundry (ranije Azure AI Studio) je web portal koji vam omogućava istraživanje modela, primjera i alata, upravljanje resursima te korištenje UI razvojnih tokova kao i SDK/CLI opcija za razvoj s fokusom na kod.

![Mogućnosti Azure AI](../../../translated_images/hr/04-azure-ai-platform.80203baf03a12fa8.webp)

Azure AI vam omogućuje korištenje različitih resursa za upravljanje operacijama, uslugama, projektima, potrebama pretraživanja vektora i baza podataka.

![LLMOps s Azure AI](../../../translated_images/hr/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

Izgradite od Proof-of-Concept (POC) do velikih aplikacija uz PromptFlow:

- Dizajnirajte i gradite aplikacije iz VS Code-a, s vizualnim i funkcionalnim alatima
- Testirajte i fino podesite svoje aplikacije za kvalitetan AI, s lakoćom.
- Koristite Microsoft Foundry za integraciju i iteraciju s cloudom, push i deployment za brzu integraciju.

![LLMOps s PromptFlow](../../../translated_images/hr/06-llm-promptflow.a183eba07a3a7fdf.webp)

## Sjajno! Nastavite s učenjem!

Izvrsno, sada saznajte više o tome kako strukturiramo aplikaciju za korištenje koncepta s [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), da vidite kako Cloud Advocacy dodaje te koncepte u demonstracije. Za više sadržaja, pogledajte našu [Ignite breakout sesiju!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Sada pogledajte Lekciju 15, da biste razumjeli kako [Retrieval Augmented Generation i vektorske baze podataka](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) utječu na Generativnu AI i kako napraviti privlačnije aplikacije!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->