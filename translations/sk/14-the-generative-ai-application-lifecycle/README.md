<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "27a5347a5022d5ef0a72ab029b03526a",
  "translation_date": "2025-06-25T22:10:07+00:00",
  "source_file": "14-the-generative-ai-application-lifecycle/README.md",
  "language_code": "sk"
}
-->
[![Integrácia s volaním funkcií](../../../translated_images/14-lesson-banner.066d74a31727ac121eeac06376a068a397d8e335281e63ce94130d11f516e46b.sk.png)](https://aka.ms/gen-ai-lesson14-gh?WT.mc_id=academic-105485-koreyst)

# Životný cyklus aplikácie generatívnej AI

Dôležitou otázkou pre všetky AI aplikácie je relevantnosť AI funkcií, keďže AI je rýchlo sa rozvíjajúca oblasť. Aby vaša aplikácia zostala relevantná, spoľahlivá a robustná, musíte ju neustále monitorovať, hodnotiť a zlepšovať. Tu prichádza na rad životný cyklus generatívnej AI.

Životný cyklus generatívnej AI je rámec, ktorý vás sprevádza fázami vývoja, nasadzovania a údržby generatívnej AI aplikácie. Pomáha vám definovať vaše ciele, merať váš výkon, identifikovať vaše výzvy a implementovať vaše riešenia. Tiež vám pomáha zosúladiť vašu aplikáciu s etickými a právnymi normami vášho odvetvia a vašich zainteresovaných strán. Dodržiavaním životného cyklu generatívnej AI môžete zabezpečiť, že vaša aplikácia vždy prináša hodnotu a uspokojuje vašich používateľov.

## Úvod

V tejto kapitole sa dozviete:

- Pochopiť posun paradigmy z MLOps na LLMOps
- Životný cyklus LLM
- Nástroje pre životný cyklus
- Metryfikácia a hodnotenie životného cyklu

## Pochopiť posun paradigmy z MLOps na LLMOps

LLM sú nový nástroj v arzenáli umelej inteligencie, sú neuveriteľne silné v úlohách analýzy a generovania pre aplikácie, avšak táto sila má určité dôsledky na to, ako zjednodušujeme úlohy AI a klasického strojového učenia.

S tým potrebujeme novú paradigmu, aby sme tento nástroj adaptovali dynamicky, so správnymi stimulmi. Staršie AI aplikácie môžeme kategorizovať ako "ML aplikácie" a novšie AI aplikácie ako "GenAI aplikácie" alebo len "AI aplikácie", čo odráža hlavný prúd technológií a techník používaných v danom čase. Toto posúva náš príbeh viacerými spôsobmi, pozrite sa na nasledujúce porovnanie.

![Porovnanie LLMOps vs. MLOps](../../../translated_images/01-llmops-shift.29bc933cb3bb0080a562e1655c0c719b71a72c3be6252d5c564b7f598987e602.sk.png)

Všimnite si, že v LLMOps sa viac zameriavame na vývojárov aplikácií, používame integrácie ako kľúčový bod, používame "Modely ako službu" a premýšľame o nasledujúcich bodoch pre metriky.

- Kvalita: Kvalita odpovede
- Škoda: Zodpovedná AI
- Čestnosť: Opodstatnenosť odpovede (Dáva to zmysel? Je to správne?)
- Náklady: Rozpočet riešenia
- Latencia: Priem. čas pre odpoveď tokenu

## Životný cyklus LLM

Najprv, aby sme pochopili životný cyklus a úpravy, pozrime sa na nasledujúcu infografiku.

![Infografika LLMOps](../../../translated_images/02-llmops.70a942ead05a7645db740f68727d90160cb438ab71f0fb20548bc7fe5cad83ff.sk.png)

Ako si môžete všimnúť, toto je odlišné od bežných životných cyklov MLOps. LLM majú mnoho nových požiadaviek, ako je Prompting, rôzne techniky na zlepšenie kvality (Fine-Tuning, RAG, Meta-Prompts), rôzne hodnotenie a zodpovednosť so zodpovednou AI, a nakoniec nové hodnotiace metriky (Kvalita, Škoda, Čestnosť, Náklady a Latencia).

Napríklad, pozrite sa, ako ideujeme. Používame inžinierstvo promptov na experimentovanie s rôznymi LLM na skúmanie možností, aby sme otestovali, či ich hypotéza môže byť správna.

Všimnite si, že toto nie je lineárne, ale integrované slučky, iteratívne a s celkovým cyklom.

Ako by sme mohli preskúmať tieto kroky? Poďme do detailu, ako by sme mohli vybudovať životný cyklus.

![Pracovný tok LLMOps](../../../translated_images/03-llm-stage-flows.3a1e1c401235a6cfa886ed6ba04aa52a096a545e1bc44fa54d7d5983a7201892.sk.png)

Toto môže vyzerať trochu komplikovane, zamerajme sa najprv na tri veľké kroky.

1. Ideácia/Preskúmavanie: Preskúmavanie, tu môžeme skúmať podľa našich obchodných potrieb. Prototypovanie, vytváranie [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) a testovanie, či je dostatočne efektívne pre našu hypotézu.
2. Budovanie/Posilňovanie: Implementácia, teraz začíname hodnotiť pre väčšie dátové sady, implementovať techniky ako Fine-tuning a RAG, aby sme skontrolovali robustnosť nášho riešenia. Ak nie, preimplementovanie, pridanie nových krokov do nášho toku alebo reštrukturalizácia dát môže pomôcť. Po testovaní nášho toku a našej škály, ak to funguje a skontrolujeme naše metriky, je pripravené na ďalší krok.
3. Operationalizácia: Integrácia, teraz pridávanie monitorovacích a výstražných systémov do nášho systému, nasadzovanie a integrácia aplikácií do našej aplikácie.

Potom máme celkový cyklus riadenia, zameraný na bezpečnosť, dodržiavanie predpisov a správu.

Gratulujeme, teraz máte svoju AI aplikáciu pripravenú a funkčnú. Pre praktickú skúsenosť sa pozrite na [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

Aké nástroje by sme mohli použiť?

## Nástroje pre životný cyklus

Pre nástroje, Microsoft poskytuje [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) a [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst), ktoré uľahčujú a zjednodušujú implementáciu a sú pripravené na použitie.

[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys), vám umožňuje používať [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys). AI Studio je webový portál, ktorý vám umožňuje preskúmavať modely, vzorky a nástroje. Spravovať vaše zdroje, vývojové toky UI a možnosti SDK/CLI pre vývoj orientovaný na kód.

![Možnosti Azure AI](../../../translated_images/04-azure-ai-platform.80203baf03a12fa8b166e194928f057074843d1955177baf0f5b53d50d7b6153.sk.png)

Azure AI vám umožňuje používať viacero zdrojov na správu vašich operácií, služieb, projektov, potrieb vyhľadávania vektorov a databáz.

![LLMOps s Azure AI](../../../translated_images/05-llm-azure-ai-prompt.a5ce85cdbb494bdf95420668e3464aae70d8b22275a744254e941dd5e73ae0d2.sk.png)

Konstrukcia, od Proof-of-Concept (POC) až po veľké aplikácie s PromptFlow:

- Navrhovanie a budovanie aplikácií z VS Code, s vizuálnymi a funkčnými nástrojmi
- Testovanie a dolaďovanie vašich aplikácií pre kvalitnú AI, s ľahkosťou.
- Použitie Azure AI Studio na integráciu a iteráciu s cloudom, Push a nasadenie pre rýchlu integráciu.

![LLMOps s PromptFlow](../../../translated_images/06-llm-promptflow.a183eba07a3a7fdf4aa74db92a318b8cbbf4a608671f6b166216358d3203d8d4.sk.png)

## Skvelé! Pokračujte v učení!

Úžasné, teraz sa dozviete viac o tom, ako štruktúrujeme aplikáciu na použitie konceptov s [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), aby ste zistili, ako Cloud Advocacy pridáva tieto koncepty do ukážok. Pre viac obsahu, pozrite si náš [Ignite breakout session!](https://www.youtube.com/watch?v=DdOylyrTOWg)

Teraz si pozrite Lekciu 15, aby ste pochopili, ako [Retrieval Augmented Generation a Vektorové databázy](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) ovplyvňujú generatívnu AI a ako vytvoriť pútavejšie aplikácie!

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.