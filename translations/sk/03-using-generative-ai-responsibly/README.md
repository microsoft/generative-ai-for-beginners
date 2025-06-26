<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-06-25T11:32:06+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "sk"
}
-->
# Zodpovedné používanie generatívnej AI

> _Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie_

Je ľahké byť fascinovaný AI a obzvlášť generatívnou AI, ale je potrebné zvážiť, ako ju používať zodpovedne. Je potrebné premýšľať o tom, ako zabezpečiť, aby bol výstup spravodlivý, neškodný a ďalšie. Táto kapitola vám poskytne kontext, čo zohľadniť a ako podniknúť aktívne kroky na zlepšenie vášho používania AI.

## Úvod

Táto lekcia pokryje:

- Prečo by ste mali uprednostniť Zodpovednú AI pri budovaní aplikácií generatívnej AI.
- Základné princípy Zodpovednej AI a ako súvisia s generatívnou AI.
- Ako uviesť tieto princípy Zodpovednej AI do praxe prostredníctvom stratégie a nástrojov.

## Ciele učenia

Po dokončení tejto lekcie budete vedieť:

- Dôležitosť Zodpovednej AI pri budovaní aplikácií generatívnej AI.
- Kedy premýšľať a aplikovať základné princípy Zodpovednej AI pri budovaní aplikácií generatívnej AI.
- Aké nástroje a stratégie sú vám k dispozícii na zavedenie konceptu Zodpovednej AI do praxe.

## Princípy Zodpovednej AI

Nadšenie z generatívnej AI nikdy nebolo vyššie. Toto nadšenie prinieslo do tohto priestoru množstvo nových vývojárov, pozornosti a financovania. Hoci je to veľmi pozitívne pre kohokoľvek, kto chce budovať produkty a spoločnosti pomocou generatívnej AI, je tiež dôležité postupovať zodpovedne.

Počas tohto kurzu sa zameriavame na budovanie nášho startupu a nášho vzdelávacieho produktu AI. Použijeme princípy Zodpovednej AI: Spravodlivosť, Zahrnutosť, Spoľahlivosť/Bezpečnosť, Bezpečnosť a Súkromie, Transparentnosť a Zodpovednosť. S týmito princípmi preskúmame, ako súvisia s naším používaním generatívnej AI v našich produktoch.

## Prečo by ste mali uprednostniť Zodpovednú AI

Pri budovaní produktu, prijatí prístupu zameraného na človeka, pri ktorom máte na mysli najlepší záujem používateľa, vedie k najlepším výsledkom.

Jedinečnosť generatívnej AI spočíva v jej schopnosti vytvárať užitočné odpovede, informácie, vedenie a obsah pre používateľov. To môže byť dosiahnuté bez mnohých manuálnych krokov, čo môže viesť k veľmi pôsobivým výsledkom. Bez riadneho plánovania a stratégií to však, bohužiaľ, môže viesť k niektorým škodlivým výsledkom pre vašich používateľov, váš produkt a spoločnosť ako celok.

Pozrime sa na niektoré (ale nie všetky) z týchto potenciálne škodlivých výsledkov:

### Halucinácie

Halucinácie sú termín používaný na opis, keď LLM produkuje obsah, ktorý je buď úplne nezmyselný, alebo niečo, o čom vieme, že je fakticky nesprávne na základe iných zdrojov informácií.

Vezmime si napríklad, že vytvoríme funkciu pre náš startup, ktorá umožňuje študentom klásť historické otázky modelu. Študent sa pýta otázku `Who was the sole survivor of Titanic?`

Model vytvorí odpoveď, ako je tá nižšie:

Toto je veľmi sebavedomá a dôkladná odpoveď. Bohužiaľ, je nesprávna. Aj s minimálnym množstvom výskumu by niekto zistil, že z katastrofy Titanicu prežilo viac ako jeden človek. Pre študenta, ktorý práve začína skúmať túto tému, môže byť táto odpoveď dostatočne presvedčivá na to, aby ju nebolo potrebné spochybňovať a považovať za fakt. Dôsledky tohto môžu viesť k tomu, že AI systém bude nespoľahlivý a negatívne ovplyvní povesť nášho startupu.

S každou iteráciou akéhokoľvek daného LLM sme zaznamenali zlepšenie výkonu pri minimalizácii halucinácií. Aj s týmto zlepšením musíme ako tvorcovia aplikácií a používatelia zostať o týchto obmedzeniach informovaní.

### Škodlivý obsah

V predchádzajúcej časti sme sa zaoberali tým, keď LLM produkuje nesprávne alebo nezmyselné odpovede. Ďalším rizikom, o ktorom musíme vedieť, je, keď model reaguje so škodlivým obsahom.

Škodlivý obsah môže byť definovaný ako:

- Poskytovanie inštrukcií alebo povzbudzovanie k sebapoškodzovaniu alebo ubližovaniu určitým skupinám.
- Nenávistný alebo ponižujúci obsah.
- Vedenie plánovania akéhokoľvek typu útoku alebo násilných činov.
- Poskytovanie inštrukcií, ako nájsť nelegálny obsah alebo spáchať nelegálne činy.
- Zobrazovanie sexuálne explicitného obsahu.

Pre náš startup chceme zabezpečiť, aby sme mali správne nástroje a stratégie na zabránenie tomu, aby študenti videli tento typ obsahu.

### Nedostatok spravodlivosti

Spravodlivosť je definovaná ako „zabezpečenie, že AI systém je bez predsudkov a diskriminácie a že zaobchádza so všetkými spravodlivo a rovnako.“ Vo svete generatívnej AI chceme zabezpečiť, aby vylučujúce svetonázory marginalizovaných skupín neboli posilnené výstupom modelu.

Tieto typy výstupov nie sú len deštruktívne pre budovanie pozitívnych produktových skúseností pre našich používateľov, ale tiež spôsobujú ďalšie spoločenské škody. Ako tvorcovia aplikácií by sme mali vždy mať na pamäti širokú a rozmanitú používateľskú základňu pri budovaní riešení s generatívnou AI.

## Ako používať generatívnu AI zodpovedne

Teraz, keď sme identifikovali dôležitosť Zodpovednej generatívnej AI, pozrime sa na 4 kroky, ktoré môžeme podniknúť, aby sme zodpovedne budovali naše AI riešenia:

### Meranie potenciálnych škôd

Pri testovaní softvéru testujeme očakávané akcie používateľa v aplikácii. Podobne testovanie rôznorodého súboru výziev, ktoré používatelia pravdepodobne použijú, je dobrý spôsob, ako merať potenciálne škody.

Keďže náš startup buduje vzdelávací produkt, bolo by dobré pripraviť zoznam výziev súvisiacich so vzdelávaním. To by mohlo zahŕňať pokrytie určitého predmetu, historické fakty a výzvy o študentskom živote.

### Zmiernenie potenciálnych škôd

Teraz je čas nájsť spôsoby, ako môžeme zabrániť alebo obmedziť potenciálnu škodu spôsobenú modelom a jeho odpoveďami. Môžeme sa na to pozrieť v 4 rôznych vrstvách:

- **Model**. Výber správneho modelu pre správny prípad použitia. Väčšie a zložitejšie modely ako GPT-4 môžu spôsobiť väčšie riziko škodlivého obsahu, keď sú aplikované na menšie a špecifickejšie prípady použitia. Používanie vašich tréningových dát na doladenie tiež znižuje riziko škodlivého obsahu.

- **Bezpečnostný systém**. Bezpečnostný systém je súbor nástrojov a konfigurácií na platforme, ktorá slúži modelu, aby pomohol zmierniť škody. Príkladom je systém filtrovania obsahu na službe Azure OpenAI. Systémy by mali tiež detekovať útoky typu jailbreak a nechcené aktivity ako požiadavky od botov.

- **Metaprompt**. Metaprompt a ukotvenie sú spôsoby, ako môžeme model nasmerovať alebo obmedziť na základe určitých správaní a informácií. To by mohlo zahŕňať použitie systémových vstupov na definovanie určitých limitov modelu. Okrem toho poskytovanie výstupov, ktoré sú relevantnejšie pre rozsah alebo doménu systému.

Môže to byť aj použitie techník ako Retrieval Augmented Generation (RAG), aby model čerpal informácie iba z výberu dôveryhodných zdrojov. V tejto lekcii je neskôr lekcia o [budovaní vyhľadávacích aplikácií](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Používateľská skúsenosť**. Posledná vrstva je miesto, kde používateľ priamo interaguje s modelom prostredníctvom rozhrania našej aplikácie. Týmto spôsobom môžeme navrhnúť UI/UX tak, aby obmedzilo používateľa na typy vstupov, ktoré môže modelu poslať, ako aj text alebo obrázky zobrazené používateľovi. Pri nasadzovaní AI aplikácie musíme byť tiež transparentní o tom, čo naša generatívna AI aplikácia môže a nemôže robiť.

Máme celú lekciu venovanú [navrhovaniu UX pre AI aplikácie](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Vyhodnotenie modelu**. Práca s LLM môže byť náročná, pretože nemáme vždy kontrolu nad dátami, na ktorých bol model trénovaný. Napriek tomu by sme mali vždy vyhodnotiť výkon a výstupy modelu. Je stále dôležité merať presnosť, podobnosť, zakotvenie a relevantnosť výstupu modelu. To pomáha poskytovať transparentnosť a dôveru zainteresovaným stranám a používateľom.

### Prevádzka zodpovedného riešenia generatívnej AI

Budovanie operačnej praxe okolo vašich AI aplikácií je poslednou fázou. To zahŕňa spoluprácu s ďalšími časťami nášho startupu, ako sú Právne a Bezpečnosť, aby sme zabezpečili, že sme v súlade so všetkými regulačnými politikami. Pred spustením chceme tiež vytvoriť plány okolo dodávky, riešenia incidentov a rollbacku, aby sme zabránili akýmkoľvek škodám pre našich používateľov.

## Nástroje

Hoci sa práca na vývoji riešení Zodpovednej AI môže zdať ako veľa, je to práca, ktorá stojí za to. Ako oblasť generatívnej AI rastie, viac nástrojov na pomoc vývojárom efektívne integrovať zodpovednosť do ich pracovných postupov bude zrieť. Napríklad [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) môže pomôcť detekovať škodlivý obsah a obrázky prostredníctvom API požiadavky.

## Kontrola vedomostí

Na čo sa musíte starať, aby ste zabezpečili zodpovedné používanie AI?

1. Že odpoveď je správna.
1. Škodlivé používanie, že AI nie je používaná na kriminálne účely.
1. Zabezpečenie, že AI je bez predsudkov a diskriminácie.

A: 2 a 3 sú správne. Zodpovedná AI vám pomáha zvážiť, ako zmierniť škodlivé účinky a predsudky a ďalšie.

## 🚀 Výzva

Prečítajte si o [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) a zistite, čo môžete prijať pre svoje použitie.

## Skvelá práca, pokračujte vo svojom učení

Po dokončení tejto lekcie si pozrite našu [zbierku učenia o generatívnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste pokračovali v zvyšovaní svojej znalosti generatívnej AI!

Prejdite na Lekciu 4, kde sa pozrieme na [základy návrhu výziev](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

**Vylúčenie zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.