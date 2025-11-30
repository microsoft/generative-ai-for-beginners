<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b9d32511b27373a1b21b5789d4fda057",
  "translation_date": "2025-10-17T21:58:42+00:00",
  "source_file": "14-the-generative-ai-application-lifecycle/README.md",
  "language_code": "sk"
}
-->
[![Integrácia s volaním funkcií](../../../translated_images/14-lesson-banner.066d74a31727ac121eeac06376a068a397d8e335281e63ce94130d11f516e46b.sk.png)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Životný cyklus aplikácií generatívnej AI

Dôležitou otázkou pre všetky AI aplikácie je relevantnosť ich funkcií, pretože AI je rýchlo sa vyvíjajúca oblasť. Aby vaša aplikácia zostala relevantná, spoľahlivá a robustná, je potrebné ju neustále monitorovať, hodnotiť a zlepšovať. Práve tu prichádza na rad životný cyklus generatívnej AI.

Životný cyklus generatívnej AI je rámec, ktorý vás sprevádza fázami vývoja, nasadenia a údržby generatívnej AI aplikácie. Pomáha vám definovať ciele, merať výkon, identifikovať výzvy a implementovať riešenia. Taktiež vám pomáha zosúladiť vašu aplikáciu s etickými a právnymi normami vášho odvetvia a vašich zainteresovaných strán. Dodržiavaním životného cyklu generatívnej AI môžete zabezpečiť, že vaša aplikácia bude vždy prinášať hodnotu a uspokojovať potreby používateľov.

## Úvod

V tejto kapitole sa naučíte:

- Pochopiť posun paradigmy z MLOps na LLMOps
- Životný cyklus LLM
- Nástroje pre životný cyklus
- Metodika a hodnotenie životného cyklu

## Pochopenie posunu paradigmy z MLOps na LLMOps

LLM sú nový nástroj v arzenáli umelej inteligencie, ktorý je neuveriteľne silný pri analýze a generovaní úloh pre aplikácie. Táto sila však prináša určité dôsledky na to, ako zefektívňujeme úlohy AI a klasického strojového učenia.

Na základe toho potrebujeme novú paradigmu, aby sme tento nástroj adaptovali dynamicky a s vhodnými stimulmi. Staršie AI aplikácie môžeme kategorizovať ako "ML aplikácie" a novšie AI aplikácie ako "GenAI aplikácie" alebo jednoducho "AI aplikácie", čo odráža hlavné technológie a techniky používané v danom čase. Tento posun mení náš pohľad na veci v mnohých ohľadoch, pozrite si nasledujúce porovnanie.

![Porovnanie LLMOps vs. MLOps](../../../translated_images/01-llmops-shift.29bc933cb3bb0080a562e1655c0c719b71a72c3be6252d5c564b7f598987e602.sk.png)

Všimnite si, že v LLMOps sa viac zameriavame na vývojárov aplikácií, pričom integrácie sú kľúčovým bodom, používame "Modely ako službu" a zameriavame sa na nasledujúce body pre metriky:

- Kvalita: Kvalita odpovede
- Škodlivosť: Zodpovedná AI
- Pravdivosť: Základ odpovede (Má to zmysel? Je to správne?)
- Náklady: Rozpočet riešenia
- Latencia: Priemerný čas na odpoveď tokenu

## Životný cyklus LLM

Najprv, aby sme pochopili životný cyklus a jeho úpravy, pozrime sa na nasledujúcu infografiku.

![Infografika LLMOps](../../../translated_images/02-llmops.70a942ead05a7645db740f68727d90160cb438ab71f0fb20548bc7fe5cad83ff.sk.png)

Ako si môžete všimnúť, toto sa líši od bežných životných cyklov MLOps. LLM majú mnoho nových požiadaviek, ako je Prompting, rôzne techniky na zlepšenie kvality (Fine-Tuning, RAG, Meta-Prompts), rôzne hodnotenie a zodpovednosť so zodpovednou AI, a nakoniec nové metriky hodnotenia (Kvalita, Škodlivosť, Pravdivosť, Náklady a Latencia).

Napríklad, pozrite sa na to, ako ideujeme. Používame prompt engineering na experimentovanie s rôznymi LLM, aby sme preskúmali možnosti a otestovali, či by ich hypotéza mohla byť správna.

Všimnite si, že toto nie je lineárne, ale integrované cykly, iteratívne a s celkovým cyklom.

Ako by sme mohli preskúmať tieto kroky? Poďme sa podrobne pozrieť na to, ako by sme mohli vybudovať životný cyklus.

![Pracovný tok LLMOps](../../../translated_images/03-llm-stage-flows.3a1e1c401235a6cfa886ed6ba04aa52a096a545e1bc44fa54d7d5983a7201892.sk.png)

Toto môže vyzerať trochu komplikovane, zamerajme sa najprv na tri veľké kroky.

1. Ideovanie/Preskúmanie: Preskúmanie, tu môžeme preskúmať podľa našich obchodných potrieb. Prototypovanie, vytvorenie [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) a testovanie, či je dostatočne efektívne pre našu hypotézu.
2. Budovanie/Zlepšovanie: Implementácia, teraz začíname hodnotiť pre väčšie datasety, implementovať techniky, ako Fine-tuning a RAG, aby sme overili robustnosť nášho riešenia. Ak to nefunguje, opätovná implementácia, pridanie nových krokov do nášho toku alebo reštrukturalizácia dát môže pomôcť. Po testovaní nášho toku a našej škály, ak to funguje a splní naše metriky, je pripravené na ďalší krok.
3. Prevádzkovanie: Integrácia, teraz pridávame monitorovacie a výstražné systémy do nášho systému, nasadenie a integráciu aplikácie do našej aplikácie.

Potom máme celkový cyklus riadenia, zameraný na bezpečnosť, súlad a správu.

Gratulujeme, teraz máte svoju AI aplikáciu pripravenú na prevádzku. Pre praktickú skúsenosť sa pozrite na [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

Aké nástroje by sme mohli použiť?

## Nástroje pre životný cyklus

Pre nástroje Microsoft poskytuje [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) a [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst), ktoré uľahčujú a umožňujú jednoduchú implementáciu vášho cyklu.

[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) vám umožňuje používať [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys). AI Studio je webový portál, ktorý vám umožňuje preskúmať modely, vzorky a nástroje. Spravovať vaše zdroje, vývojové toky UI a SDK/CLI možnosti pre vývoj orientovaný na kód.

![Možnosti Azure AI](../../../translated_images/04-azure-ai-platform.80203baf03a12fa8b166e194928f057074843d1955177baf0f5b53d50d7b6153.sk.png)

Azure AI vám umožňuje používať viacero zdrojov na správu vašich operácií, služieb, projektov, vyhľadávania vektorov a databázových potrieb.

![LLMOps s Azure AI](../../../translated_images/05-llm-azure-ai-prompt.a5ce85cdbb494bdf95420668e3464aae70d8b22275a744254e941dd5e73ae0d2.sk.png)

Vytvárajte od Proof-of-Concept (POC) až po aplikácie vo veľkom meradle s PromptFlow:

- Navrhujte a budujte aplikácie z VS Code, s vizuálnymi a funkčnými nástrojmi
- Testujte a dolaďujte svoje aplikácie pre kvalitnú AI, jednoducho.
- Používajte Azure AI Studio na integráciu a iteráciu s cloudom, nasadzujte a implementujte pre rýchlu integráciu.

![LLMOps s PromptFlow](../../../translated_images/06-llm-promptflow.a183eba07a3a7fdf4aa74db92a318b8cbbf4a608671f6b166216358d3203d8d4.sk.png)

## Skvelé! Pokračujte v učení!

Úžasné, teraz sa naučte viac o tom, ako štruktúrujeme aplikáciu na použitie konceptov s [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), aby ste videli, ako Cloud Advocacy pridáva tieto koncepty do demonštrácií. Pre viac obsahu si pozrite našu [Ignite breakout session!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Teraz si pozrite lekciu 15, aby ste pochopili, ako [Retrieval Augmented Generation a vektorové databázy](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) ovplyvňujú generatívnu AI a umožňujú vytvárať viac pútavé aplikácie!

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.