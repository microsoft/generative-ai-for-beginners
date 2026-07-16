[![Integrácia s volaním funkcie](../../../translated_images/sk/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Životný cyklus generatívnej AI aplikácie

Dôležitou otázkou pre všetky AI aplikácie je relevantnosť AI funkcií, pretože AI je rýchlo sa vyvíjajúca oblasť. Aby vaša aplikácia zostala relevantná, spoľahlivá a robustná, je potrebné ju neustále monitorovať, vyhodnocovať a zlepšovať. Práve tu prichádza na rad životný cyklus generatívnej AI.

Životný cyklus generatívnej AI je rámec, ktorý vás prevedie jednotlivými fázami vývoja, nasadenia a údržby generatívnej AI aplikácie. Pomáha vám definovať ciele, merať výkonnosť, identifikovať výzvy a implementovať riešenia. Tiež vám pomáha zosúladiť vašu aplikáciu s etickými a právnymi normami vo vašej oblasti a pre vašich zainteresovaných strán. Dodržiavaním životného cyklu generatívnej AI môžete zabezpečiť, že vaša aplikácia bude vždy prinášať hodnotu a uspokojovať používateľov.

## Úvod

V tejto kapitole sa naučíte:

- Pochopiť zmenu paradigmy z MLOps na LLMOps
- Životný cyklus LLM
- Nástroje pre životný cyklus
- Metrika a evaluácia životného cyklu

## Pochopiť zmenu paradigmy z MLOps na LLMOps

LLM sú nový nástroj v arzenáli umelej inteligencie, sú mimoriadne výkonné pri úlohách analýzy a generovania pre aplikácie, avšak táto sila prináša určité dôsledky pri zefektívňovaní AI a klasických strojového učenia.

Preto potrebujeme novú paradigmu, aby sme tento nástroj adaptovali dynamicky a so správnymi stimulmi. Staršie AI aplikácie môžeme kategorizovať ako „ML aplikácie“ a novšie AI aplikácie ako „GenAI aplikácie“ alebo jednoducho „AI aplikácie“, čo odráža v danom čase používané technológie a techniky. Toto posúva náš príbeh viacerými smermi, pozrite si nasledujúce porovnanie.

![Porovnanie LLMOps vs. MLOps](../../../translated_images/sk/01-llmops-shift.29bc933cb3bb0080.webp)

Všimnite si, že pri LLMOps sa viac zameriavame na vývojárov aplikácií, používame integrácie ako kľúčový prvok, využívame „modely ako službu“ a uvažujeme o nasledujúcich bodoch pre metriky.

- Kvalita: kvalita odpovede
- Škoda: zodpovedná AI
- Úprimnosť: zakotvenie odpovede (má to zmysel? Je to správne?)
- Náklady: rozpočet riešenia
- Latencia: priemerný čas na odpoveď tokenu

## Životný cyklus LLM

Najprv, aby sme pochopili životný cyklus a zmeny, pozrime sa na nasledujúcu infografiku.

![Infografika LLMOps](../../../translated_images/sk/02-llmops.70a942ead05a7645.webp)

Ako vidíte, toto sa líši od bežných životných cyklov MLOps. LLM majú veľa nových požiadaviek, ako je Prompting, rôzne techniky na zlepšenie kvality (Fine-Tuning, RAG, Meta-Prompts), rôzne hodnotenia a zodpovednosť v rámci zodpovednej AI, a nakoniec nové hodnotiace metriky (kvalita, škoda, úprimnosť, náklady a latencia).

Napríklad si všimnite, ako generujeme nápady. Používame inžinierstvo promptov na experimentovanie s rôznymi LLM, aby sme preskúmali možnosti a otestovali, či ich hypotézy môžu byť správne.

Upozorňujeme, že to nie je lineárny proces, ale integrované slučky, iteratívne a s celkovým cyklom nad nimi.

Ako môžeme preskúmať tieto kroky? Poďme podrobnejšie preskúmať, ako možno zostaviť životný cyklus.

![Pracovný tok LLMOps](../../../translated_images/sk/03-llm-stage-flows.3a1e1c401235a6cf.webp)

Toto môže vyzerať trochu komplikovane, najskôr sa sústreďme na tri veľké kroky.

1. Generovanie nápadov / preskúmavanie: Preskúmanie, tu môžeme skúmať podľa našich obchodných potrieb. Prototypovanie, vytváranie [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) a testovanie, či je dosť efektívne pre našu hypotézu.
1. Budovanie / rozšírenie: Implementácia, teraz začíname vyhodnocovať pre väčšie dataset-y, implementovať techniky ako Fine-Tuning a RAG, aby sme preverili robustnosť riešenia. Ak nie je dostatočne robustné, rerobenie, pridanie nových krokov do nášho toku alebo reštrukturalizácia dát môže pomôcť. Po otestovaní toku a škálovateľnosti, a po kontrole metrík, je pripravené na ďalší krok.
1. Prevádzkovanie: Integrácia, teraz pridávame monitorovacie a výstražné systémy do systému, nasadenie a integráciu aplikácie.

Potom máme celkový cyklus riadenia, zameraný na bezpečnosť, súlad a správu.

Gratulujeme, teraz máte vašu AI aplikáciu pripravenú na prevádzku. Pre praktickú skúsenosť si pozrite [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)

Teraz, aké nástroje môžeme použiť?

## Nástroje pre životný cyklus

Pre nástroje poskytuje Microsoft [Azure AI Platformu](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) a [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst), ktoré uľahčujú a sprístupňujú implementáciu vášho cyklu.

[Azure AI Platforma](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) vám umožňuje používať [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst). Microsoft Foundry (predtým Azure AI Studio) je webový portál, ktorý vám umožňuje objavovať modely, vzory a nástroje, spravovať zdroje a používať UI vývojové toky ako aj SDK/CLI možnosti pre vývoj zameraný na kód.

![Možnosti Azure AI](../../../translated_images/sk/04-azure-ai-platform.80203baf03a12fa8.webp)

Azure AI vám umožní využívať viacero zdrojov na správu prevádzky, služieb, projektov, vyhľadávania vo vektore a potrieb databáz.

![LLMOps s Azure AI](../../../translated_images/sk/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

Konštrukcia, od proof-of-concept (POC) až po veľkorozmerné aplikácie s PromptFlow:

- Navrhujte a budujte aplikácie vo VS Code, pomocou vizuálnych a funkčných nástrojov
- Testujte a dolaďujte aplikácie pre kvalitnú AI jednoducho
- Použite Microsoft Foundry na integráciu a iteráciu s cloudom, push a nasadenie pre rýchlu integráciu

![LLMOps s PromptFlow](../../../translated_images/sk/06-llm-promptflow.a183eba07a3a7fdf.webp)

## Skvelé! Pokračujte v učení!

Úžasné, teraz sa naučte viac o tom, ako štruktúrujeme aplikáciu na použitie týchto konceptov s [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), aby ste videli, ako Cloud Advocacy pridáva tieto koncepty do demonštrácií. Pre viac obsahu si pozrite náš [Ignite breakout session!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Teraz si pozrite Lekciu 15, kde pochopíte, ako [Retrieval Augmented Generation a vektorové databázy](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) ovplyvňujú generatívnu AI a umožňujú tvorbu atraktívnejších aplikácií!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->