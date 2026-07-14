[![Integracija s klici funkcij](../../../translated_images/sl/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Življenjski cikel generativne umetne inteligence

Pomembno vprašanje za vse aplikacije umetne inteligence je relevantnost AI funkcij, saj je AI hitro razvijajoče se področje. Da zagotovite, da vaša aplikacija ostane relevantna, zanesljiva in robustna, jo morate nenehno spremljati, ocenjevati in izboljševati. Tu pride do pojava življenjskega cikla generativne AI.

Življenjski cikel generativne AI je okvir, ki vas vodi skozi faze razvoja, uvajanja in vzdrževanja generativne AI aplikacije. Pomaga vam definirati cilje, meriti uspešnost, prepoznavati izzive in uresničevati rešitve. Prav tako vam pomaga uskladiti aplikacijo z etičnimi in pravnimi standardi vašega področja ter deležnikov. Sledenje življenjskemu ciklu generativne AI vam zagotavlja, da vaša aplikacija vedno prinaša vrednost in zadovoljuje uporabnike.

## Uvod

V tem poglavju boste:

- Razumeli prehod paradigme od MLOps do LLMOps
- Življenjski cikel LLM
- Orodja za življenjski cikel
- Merjenje in ocenjevanje življenjskega cikla

## Razumeti prehod paradigme od MLOps do LLMOps

LLM so novo orodje v arzenalu umetne inteligence, izredno močni pri analizi in ustvarjanju nalog za aplikacije, vendar ta moč prinaša določene posledice pri poenostavljanju AI in klasičnih strojno-učenih nalog.

Zato potrebujemo novo paradigmo za prilagoditev tega orodja na dinamičen način in s pravimi spodbudami. Starejše AI aplikacije lahko klasificiramo kot "ML aplikacije", novejše pa kot "GenAI aplikacije" ali preprosto "AI aplikacije", kar odraža tedanjo prevladujočo tehnologijo in uporabljene tehnike. To spreminja naš pogled na več načinov, poglejte naslednjo primerjavo.

![Primerjava LLMOps in MLOps](../../../translated_images/sl/01-llmops-shift.29bc933cb3bb0080.webp)

Opazite, da pri LLMOps bolj ciljno usmerjamo razvoj aplikacij, integracije so ključna točka, uporabljamo "Modeli kot storitev" in razmišljamo o naslednjih meritvah.

- Kakovost: kakovost odgovora
- Škodljivost: Odgovorna AI
- Poštenost: utemeljenost odgovora (Ali ima smisel? Je pravilen?)
- Stroški: proračun rešitve
- Zamuda: povprečni čas za odgovor na token

## Življenjski cikel LLM

Najprej, da razumemo življenjski cikel in spremembe, si oglejmo naslednjo infografiko.

![Infografika LLMOps](../../../translated_images/sl/02-llmops.70a942ead05a7645.webp)

Kot vidite, se to razlikuje od običajnih življenjskih ciklov pri MLOps. LLM imajo številne nove zahteve, kot so Prompting, različne tehnike za izboljšanje kakovosti (fine-tuning, RAG, Meta-Prompti), različne metode ocenjevanja in odgovornosti znotraj odgovorne umetne inteligence ter nove evalvacijske metrike (kakovost, škodljivost, poštenost, stroški in zamuda).

Na primer, poglejte, kako ustvarjamo ideje. Z uporabo promptnega inženiringa eksperimentiramo z različnimi LLM, da raziščemo možnosti in preverimo, ali so naše hipoteze pravilne.

Upoštevajte, da to ni linearno, ampak vključuje integrirane zanke, iterativno in z obsežnim ciklom.

Kako bi raziskali te korake? Poglejmo podrobneje, kako bi lahko zgradili življenjski cikel.

![Potek LLMOps](../../../translated_images/sl/03-llm-stage-flows.3a1e1c401235a6cf.webp)

Morda je videti nekoliko zapleteno, osredotočimo se najprej na tri glavne korake.

1. Ustvarjanje/raziskovanje: Raziskovanje, tukaj lahko odkrivamo glede na poslovne potrebe. Prototipiranje, ustvarjanje [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) in preverjanje, če je dovolj učinkovito za naše hipoteze.
1. Gradnja/izboljševanje: Implementacija, zdaj začnemo ocenjevati na večjih podatkovnih nizih in uvesti tehnike kot fine-tuning in RAG, da preverimo robustnost naše rešitve. Če ne deluje, ponovna implementacija, dodajanje novih korakov ali prestrukturiranje podatkov lahko pomaga. Po testiranju našega poteka in obsega, če deluje in izpolnjuje metrike, je pripravljen za naslednji korak.
1. Operativizacija: Integracija, zdaj dodajanje sistemov za nadzor in opozorila, uvajanje ter integracija aplikacije.

Nato imamo obsežni cikel upravljanja, ki se osredotoča na varnost, skladnost in upravljanje.

Čestitke, vaša AI aplikacija je zdaj pripravljena in operativna. Za praktično izkušnjo si oglejte [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)

Zdaj, katere orodja lahko uporabimo?

## Orodja za življenjski cikel

Microsoft ponuja [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) in [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst), ki olajšata in poenostavita izvajanje vašega cikla.

[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) omogoča uporabo [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst). Microsoft Foundry (prej Azure AI Studio) je spletni portal, kjer lahko raziskujete modele, vzorce in orodja, upravljate vire ter uporabljate UI razvojne tokove, pa tudi SDK/CLI možnosti za razvoj na osnovi kode.

![Možnosti Azure AI](../../../translated_images/sl/04-azure-ai-platform.80203baf03a12fa8.webp)

Azure AI omogoča uporabo več virov za upravljanje vaših operacij, storitev, projektov, iskanja po vektorjih in podatkovnih baz.

![LLMOps z Azure AI](../../../translated_images/sl/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

Od zasnove do aplikacij velikih razsežnosti s PromptFlow:

- Oblikujte in gradite aplikacije iz VS Code z vizualnimi in funkcionalnimi orodji
- Preizkusite in fino nastavljajte aplikacije za kakovostno umetno inteligenco enostavno.
- Uporabite Microsoft Foundry za integracijo in iteracijo v oblaku, pošiljanje in uvajanje za hitro integracijo.

![LLMOps z PromptFlow](../../../translated_images/sl/06-llm-promptflow.a183eba07a3a7fdf.webp)

## Super! Nadaljujte z učenjem!

Odlično, zdaj se naučite več o tem, kako strukturiramo aplikacijo, da uporabimo koncepte s [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst) in preverite, kako Cloud Advocacy prikazuje te koncepte v demonstracijah. Za več vsebin si oglejte našo [Ignite delavnico!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Zdaj si oglejte Lekcijo 15, da spoznate, kako [Retrieval Augmented Generation in vektorske baze podatkov](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) vplivata na generativno AI in omogočata bolj privlačne aplikacije!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->