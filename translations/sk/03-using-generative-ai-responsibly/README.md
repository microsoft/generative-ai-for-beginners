<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d57fad773cbeb69c5dd62e65c34200d",
  "translation_date": "2025-10-17T21:55:24+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "sk"
}
-->
# Používanie generatívnej AI zodpovedne

[![Používanie generatívnej AI zodpovedne](../../../translated_images/03-lesson-banner.1ed56067a452d97709d51f6cc8b6953918b2287132f4909ade2008c936cd4af9.sk.png)](https://youtu.be/YOp-e1GjZdA?si=7Wv4wu3x44L1DCVj)

> _Kliknite na obrázok vyššie a pozrite si video k tejto lekcii_

Je ľahké byť fascinovaný AI, najmä generatívnou AI, ale je potrebné zvážiť, ako ju používať zodpovedne. Musíte premýšľať nad tým, ako zabezpečiť, aby výstupy boli spravodlivé, neškodné a podobne. Táto kapitola má za cieľ poskytnúť vám uvedený kontext, čo zvážiť a ako podniknúť aktívne kroky na zlepšenie vášho používania AI.

## Úvod

Táto lekcia pokryje:

- Prečo by ste mali uprednostniť zodpovednú AI pri budovaní aplikácií generatívnej AI.
- Základné princípy zodpovednej AI a ich vzťah ku generatívnej AI.
- Ako uviesť tieto princípy zodpovednej AI do praxe prostredníctvom stratégie a nástrojov.

## Ciele učenia

Po dokončení tejto lekcie budete vedieť:

- Dôležitosť zodpovednej AI pri budovaní aplikácií generatívnej AI.
- Kedy premýšľať a aplikovať základné princípy zodpovednej AI pri budovaní aplikácií generatívnej AI.
- Aké nástroje a stratégie máte k dispozícii na uvedenie konceptu zodpovednej AI do praxe.

## Princípy zodpovednej AI

Nadšenie z generatívnej AI nikdy nebolo vyššie. Toto nadšenie prinieslo do tejto oblasti veľa nových vývojárov, pozornosti a financovania. Hoci je to veľmi pozitívne pre každého, kto chce budovať produkty a firmy využívajúce generatívnu AI, je tiež dôležité postupovať zodpovedne.

V priebehu tohto kurzu sa zameriavame na budovanie nášho startupu a nášho vzdelávacieho produktu AI. Použijeme princípy zodpovednej AI: spravodlivosť, inkluzívnosť, spoľahlivosť/bezpečnosť, zabezpečenie a súkromie, transparentnosť a zodpovednosť. S týmito princípmi preskúmame, ako sa vzťahujú na naše využívanie generatívnej AI v našich produktoch.

## Prečo by ste mali uprednostniť zodpovednú AI

Pri budovaní produktu dosiahneme najlepšie výsledky, ak zvolíme prístup zameraný na človeka a budeme mať na pamäti najlepšie záujmy našich používateľov.

Jedinečnosť generatívnej AI spočíva v jej schopnosti vytvárať užitočné odpovede, informácie, usmernenia a obsah pre používateľov. To sa dá dosiahnuť bez mnohých manuálnych krokov, čo môže viesť k veľmi pôsobivým výsledkom. Bez správneho plánovania a stratégií to však môže, bohužiaľ, viesť k škodlivým výsledkom pre vašich používateľov, váš produkt a spoločnosť ako celok.

Pozrime sa na niektoré (ale nie všetky) z týchto potenciálne škodlivých výsledkov:

### Halucinácie

Halucinácie sú termín používaný na opis situácie, keď LLM vytvára obsah, ktorý je buď úplne nezmyselný, alebo niečo, čo vieme, že je fakticky nesprávne na základe iných zdrojov informácií.

Predstavme si, že vytvoríme funkciu pre náš startup, ktorá umožní študentom klásť historické otázky modelu. Študent sa opýta otázku `Kto bol jediným preživším Titanicu?`

Model vytvorí odpoveď, ako je tá nižšie:

![Výzva "Kto bol jediným preživším Titanicu"](../../../03-using-generative-ai-responsibly/images/ChatGPT-titanic-survivor-prompt.webp)

> _(Zdroj: [Flying bisons](https://flyingbisons.com?WT.mc_id=academic-105485-koreyst))_

Toto je veľmi sebavedomá a dôkladná odpoveď. Bohužiaľ, je nesprávna. Aj s minimálnym množstvom výskumu by človek zistil, že Titanic mal viac ako jedného preživšieho. Pre študenta, ktorý práve začína skúmať túto tému, môže byť táto odpoveď presvedčivá natoľko, že ju nebude spochybňovať a bude ju považovať za fakt. Dôsledky toho môžu viesť k tomu, že AI systém bude nespoľahlivý a negatívne ovplyvní reputáciu nášho startupu.

S každou iteráciou daného LLM sme zaznamenali zlepšenie výkonu pri minimalizovaní halucinácií. Aj s týmto zlepšením však musíme ako tvorcovia aplikácií a používatelia zostať obozretní voči týmto obmedzeniam.

### Škodlivý obsah

V predchádzajúcej časti sme sa venovali situáciám, keď LLM vytvára nesprávne alebo nezmyselné odpovede. Ďalším rizikom, ktoré musíme mať na pamäti, je, keď model odpovedá škodlivým obsahom.

Škodlivý obsah môže byť definovaný ako:

- Poskytovanie pokynov alebo podpora sebapoškodzovania alebo poškodzovania určitých skupín.
- Nenávistný alebo ponižujúci obsah.
- Usmerňovanie plánovania akéhokoľvek typu útoku alebo násilných činov.
- Poskytovanie pokynov, ako nájsť nelegálny obsah alebo spáchať nelegálne činy.
- Zobrazovanie sexuálne explicitného obsahu.

Pre náš startup chceme zabezpečiť, že máme správne nástroje a stratégie na zabránenie tomu, aby študenti videli tento typ obsahu.

### Nedostatok spravodlivosti

Spravodlivosť je definovaná ako „zabezpečenie, že AI systém je bez predsudkov a diskriminácie a že zaobchádza so všetkými spravodlivo a rovnako.“ Vo svete generatívnej AI chceme zabezpečiť, aby vylučujúce svetonázory marginalizovaných skupín neboli posilňované výstupmi modelu.

Tieto typy výstupov nielenže narúšajú budovanie pozitívnych produktových skúseností pre našich používateľov, ale tiež spôsobujú ďalšie spoločenské škody. Ako tvorcovia aplikácií by sme mali vždy myslieť na širokú a rozmanitú používateľskú základňu pri budovaní riešení s generatívnou AI.

## Ako používať generatívnu AI zodpovedne

Teraz, keď sme identifikovali dôležitosť zodpovednej generatívnej AI, pozrime sa na 4 kroky, ktoré môžeme podniknúť na zodpovedné budovanie našich AI riešení:

![Cyklus zmierňovania](../../../translated_images/mitigate-cycle.babcd5a5658e1775d5f2cb47f2ff305cca090400a72d98d0f9e57e9db5637c72.sk.png)

### Meranie potenciálnych škôd

Pri testovaní softvéru testujeme očakávané akcie používateľa v aplikácii. Podobne je dobré testovať rôznorodú sadu výziev, ktoré používatelia pravdepodobne použijú, aby sme mohli merať potenciálne škody.

Keďže náš startup buduje vzdelávací produkt, bolo by dobré pripraviť zoznam výziev súvisiacich so vzdelávaním. To by mohlo zahŕňať pokrytie určitého predmetu, historických faktov a výziev týkajúcich sa študentského života.

### Zmierňovanie potenciálnych škôd

Teraz je čas nájsť spôsoby, ako môžeme predchádzať alebo obmedziť potenciálne škody spôsobené modelom a jeho odpoveďami. Môžeme sa na to pozrieť v 4 rôznych vrstvách:

![Vrstvy zmierňovania](../../../translated_images/mitigation-layers.377215120b9a1159a8c3982c6bbcf41b6adf8c8fa04ce35cbaeeb13b4979cdfc.sk.png)

- **Model**. Výber správneho modelu pre správny prípad použitia. Väčšie a zložitejšie modely, ako je GPT-4, môžu predstavovať väčšie riziko škodlivého obsahu, keď sa aplikujú na menšie a špecifickejšie prípady použitia. Použitie vašich tréningových údajov na doladenie tiež znižuje riziko škodlivého obsahu.

- **Bezpečnostný systém**. Bezpečnostný systém je súbor nástrojov a konfigurácií na platforme, ktorá slúži modelu, a pomáha zmierňovať škody. Príkladom je systém filtrovania obsahu na Azure OpenAI službe. Systémy by mali tiež detekovať útoky na obídenie ochrany a nežiaducu aktivitu, ako sú požiadavky od botov.

- **Metaprompt**. Metaprompt a ukotvenie sú spôsoby, ako môžeme model usmerniť alebo obmedziť na základe určitých správaní a informácií. To by mohlo zahŕňať použitie systémových vstupov na definovanie určitých limitov modelu. Okrem toho poskytovanie výstupov, ktoré sú relevantnejšie pre rozsah alebo doménu systému.

Môže to zahŕňať aj použitie techník, ako je Retrieval Augmented Generation (RAG), aby model čerpal informácie iba z výberu dôveryhodných zdrojov. Neskôr v tomto kurze je lekcia o [budovaní vyhľadávacích aplikácií](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Používateľská skúsenosť**. Posledná vrstva je miesto, kde používateľ priamo interaguje s modelom prostredníctvom rozhrania našej aplikácie. Týmto spôsobom môžeme navrhnúť UI/UX tak, aby obmedzilo používateľa v typoch vstupov, ktoré môže posielať modelu, ako aj text alebo obrázky zobrazované používateľovi. Pri nasadzovaní AI aplikácie musíme byť tiež transparentní o tom, čo naša generatívna AI aplikácia dokáže a čo nie.

Máme celú lekciu venovanú [Navrhovaniu UX pre AI aplikácie](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Hodnotenie modelu**. Práca s LLM môže byť náročná, pretože nemáme vždy kontrolu nad údajmi, na ktorých bol model trénovaný. Napriek tomu by sme mali vždy hodnotiť výkon a výstupy modelu. Stále je dôležité merať presnosť, podobnosť, ukotvenosť a relevantnosť výstupu modelu. To pomáha poskytovať transparentnosť a dôveru zainteresovaným stranám a používateľom.

### Prevádzkovanie zodpovedného riešenia generatívnej AI

Budovanie operačnej praxe okolo vašich AI aplikácií je posledná fáza. To zahŕňa spoluprácu s inými časťami nášho startupu, ako je právne oddelenie a bezpečnosť, aby sme zabezpečili súlad so všetkými regulačnými politikami. Pred spustením chceme tiež vytvoriť plány okolo dodávky, riešenia incidentov a návratu späť, aby sme zabránili akémukoľvek poškodeniu našich používateľov.

## Nástroje

Hoci sa práca na vývoji zodpovedných AI riešení môže zdať náročná, je to práca, ktorá stojí za námahu. Ako oblasť generatívnej AI rastie, viac nástrojov na pomoc vývojárom efektívne integrovať zodpovednosť do ich pracovných postupov bude dozrievať. Napríklad [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) môže pomôcť detekovať škodlivý obsah a obrázky prostredníctvom API požiadavky.

## Kontrola vedomostí

Na čo by ste mali dbať, aby ste zabezpečili zodpovedné používanie AI?

1. Že odpoveď je správna.
1. Škodlivé použitie, že AI nie je používaná na kriminálne účely.
1. Zabezpečenie, že AI je bez predsudkov a diskriminácie.

A: 2 a 3 sú správne. Zodpovedná AI vám pomáha zvážiť, ako zmierniť škodlivé účinky a predsudky a viac.

## 🚀 Výzva

Prečítajte si o [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) a zistite, čo môžete prijať pre svoje použitie.

## Skvelá práca, pokračujte vo svojom učení

Po dokončení tejto lekcie si pozrite našu [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste pokračovali v rozširovaní svojich vedomostí o generatívnej AI!

Prejdite na lekciu 4, kde sa pozrieme na [Základy inžinierstva výziev](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.