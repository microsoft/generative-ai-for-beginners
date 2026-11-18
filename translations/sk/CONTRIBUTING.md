# Prispievanie

Tento projekt víta príspevky a návrhy. Väčšina príspevkov vyžaduje, aby ste
súhlasili s Dohodou o licencii prispievateľa (CLA), v ktorej prehlasujete, že máte právo,
a naozaj udeľujete nám práva na použitie vášho príspevku. Podrobnosti nájdete na
<https://cla.microsoft.com>.

> Dôležité: pri prekladaní textu v tomto repozitári, prosím, nepoužívajte strojový preklad. Preklady budú overené komunitou, preto sa prosím dobrovoľne zapájajte iba do prekladov do jazykov, ktorým dobre rozumiete.

Keď odošlete pull request, bot CLA automaticky zistí, či potrebujete
poskytnúť CLA a vhodne označí PR (napr. štítok, komentár). Jednoducho postupujte podľa
inštrukcií od bota. Toto budete musieť urobiť iba raz pre všetky repozitáre používajúce náš CLA.

## Kódex správania

Tento projekt prijal [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst).
Pre viac informácií si prečítajte [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) alebo kontaktujte [opencode@microsoft.com](mailto:opencode@microsoft.com) s ďalšími otázkami alebo pripomienkami.

## Otázka alebo problém?

Prosím, neotvárajte GitHub issues pre všeobecné otázky podpory, keďže zoznam GitHub by mal slúžiť pre žiadosti o funkcie a hlásenia chýb. Takto môžeme jednoduchšie sledovať skutočné problémy alebo chyby v kóde a udržiavať všeobecnú diskusiu oddelenú od samotného kódu.

## Preklepy, problémy, chyby a príspevky

Kedykoľvek podávate nejaké zmeny do repozitára Generative AI for Beginners, dodržiavajte prosím tieto odporúčania.

* Vždy najprv vytvorte fork repozitára do vlastného účtu pred vykonaním úprav
* Nekombinujte viaceré zmeny do jedného pull requestu. Napríklad podajte opravu chyby a aktualizáciu dokumentácie v samostatných PR
* Ak váš pull request vykazuje konflikty zlúčenia, uistite sa, že ste si lokálny hlavný branch aktualizovali tak, aby bol zrkadlom hlavného repozitára pred vykonaním zmien
* Ak podávate preklad, prosím vytvorte jeden PR pre všetky preložené súbory, pretože neprijímame čiastočné preklady obsahu
* Ak podávate opravu preklepu alebo dokumentácie, môžete vhodné úpravy skombinovať do jedného PR

## Redakčný rozsah a produkty tretích strán

Tento kurz sa zameriava na technológie Microsoft a nezávislé otvorené štandardy. Príspevky by mali slúžiť jasnému vzdelávaciemu účelu a nesmú byť primárne určené na zavedenie alebo propagáciu komerčného produktu tretej strany, hostovanej služby, modelového routera, SDK, MCP servera alebo inej ponuky špecifickej pre dodávateľa.

Open-source softvér a závislosti tretích strán môžu byť uvedené, keď sú nevyhnutné na vysvetlenie otvoreného štandardu alebo scenára interoperability, sú prezentované neutrálne a nie sú zamerané na produkt dodávateľa alebo hostovaný koncový bod. Ak váš navrhovaný príspevok obsahuje produkt alebo službu špecifickú pre dodávateľa, otvorte issue a získajte schválenie správcu pred podaním pull requestu.

Prispievatelia musia uviesť akékoľvek relevantné zamestnanie, vlastníctvo, sponzorstvo alebo inú príslušnosť k produktu alebo službe uvedenej vo svojom príspevku. Nezahŕňajte nepodložené tvrdenia o cenách, výkone, bezpečnosti, súkromí alebo porovnania. Spustiteľné príklady nesmú predvolene prenášať údaje študenta alebo vykonávať verejné akcie cez externú službu tretej strany.

## Všeobecné usmernenia pre písanie

- Zabezpečte, aby všetky vaše URL boli uzavreté v hranatých zátvorkách nasledovaných zátvorkami bez medzier okolo či vo vnútri `[]()`.
- Zabezpečte, aby akýkoľvek relatívny odkaz (t.j. odkazy na iné súbory a priečinky v repozitári) začínal `./` odkazujúcim na súbor alebo priečinok v aktuálnom pracovnom adresári alebo `../` odkazujúcim na súbor alebo priečinok v nadradenom pracovnom adresári.
- Zabezpečte, aby akýkoľvek relatívny odkaz (t.j. odkazy na iné súbory a priečinky v repozitári) mal na konci sledovacie ID (t.j. `?` alebo `&` potom `wt.mc_id=` alebo `WT.mc_id=`).
- Zabezpečte, aby každá URL z týchto domén _github.com, microsoft.com, visualstudio.com, aka.ms, a azure.com_ mala na konci sledovacie ID (t.j. `?` alebo `&` potom `wt.mc_id=` alebo `WT.mc_id=`).
- Zabezpečte, aby vaše odkazy neobsahovali miestne zameranie krajiny (t.j. `/en-us/` alebo `/en/`).
- Zabezpečte, aby všetky obrázky boli uložené v priečinku `./images`.
- Zabezpečte, aby obrázky mali popisné názvy používajúce anglické znaky, čísla a pomlčky v názve.

## GitHub Workflows

Keď odošlete pull request, spustia sa štyri rôzne workflow na overenie predchádzajúcich pravidiel.
Jednoducho postupujte podľa inštrukcií uvedených tu, aby ste prešli kontrolami workflow.

- [Skontrolovať nefunkčné relatívne cesty](#check-broken-relative-paths)
- [Skontrolovať, či cesty majú sledovanie](#check-paths-have-tracking)
- [Skontrolovať, či URL majú sledovanie](#check-urls-have-tracking)
- [Skontrolovať, či URL neobsahujú miestne zameranie](#check-urls-dont-have-locale)

### Skontrolovať nefunkčné relatívne cesty

Tento workflow zabezpečuje, že akákoľvek relatívna cesta vo vašich súboroch funguje.
Tento repozitár je nasadený na GitHub pages, takže musíte byť veľmi opatrní pri písaní odkazov, ktoré všetko spájajú, aby nikto nebol smerovaný na nesprávne miesto.

Ak chcete mať istotu, že vaše odkazy fungujú správne, jednoducho použite VS code na ich kontrolu.

Napríklad, keď umiestnite kurzor nad akýkoľvek odkaz vo vašich súboroch, budete vyzvaní na otvorenie odkazu pomocou **ctrl + kliknutia**

![VS code follow links screenshot](../../translated_images/sk/vscode-follow-link.85520ab6a1237adc.webp?WT.mc_id=academic-105485-koreyst "Screenshot z VS code výzvy na otvorenie odkazu, keď prejdete myšou nad odkaz.")

Ak kliknete na odkaz a lokálne nefunguje, určite to spôsobí chybu vo workflow a nebude fungovať ani na GitHub.

Na opravu tejto chyby sa snažte odkaz správne napísať s pomocou VS code.

Keď napíšete `./` alebo `../`, VS code vám ponúkne možnosť vybrať si zo zoznamu podľa toho, čo ste napísali.

![VS code select relative path screenshot](../../translated_images/sk/vscode-select-relative-path.3804eb73c3a9e5f2.webp?WT.mc_id=academic-105485-koreyst "Screenshot z VS code výzvy na výber relatívnej cesty z rozbaľovacieho zoznamu.")

Postupujte po ceste kliknutím na požadovaný súbor alebo priečinok a budete si istý, že vaša cesta nie je nefunkčná.

Akonáhle pridáte správnu relatívnu cestu, uložte a pošlite zmeny, workflow sa opäť spustí na overenie vašich zmien.
Ak prejdete kontrolou, ste pripravení pokračovať.

### Skontrolovať, či cesty majú sledovanie

Tento workflow zabezpečuje, že každá relatívna cesta má v sebe sledovanie.
Tento repozitár je nasadený na GitHub pages, preto potrebujeme sledovať pohyb medzi rôznymi súbormi a priečinkami.

Ak chcete mať istotu, že vaše relatívne cesty majú sledovanie, jednoducho skontrolujte, či na konci cesty je text `?wt.mc_id=`.
Ak je pripojený k vašim relatívnym cestám, prejdete túto kontrolu.

Ak nie, môžete dostať nasledujúcu chybu.

![GitHub check paths missing tracking comment screenshot](../../translated_images/sk/github-check-paths-missing-tracking-comment.880d4afe03e898ff.webp?WT.mc_id=academic-105485-koreyst "Screenshot z komentára na GitHub, ktorý ukazuje chýbajúce sledovanie v relatívnych cestách")

Na opravu tejto chyby otvorte cestu k súboru, ktorú workflow zvýraznil, a pridajte sledovacie ID na koniec relatívnych ciest.

Akonáhle pridáte sledovacie ID, uložte a odošlite zmeny, workflow sa opäť spustí na overenie vašich zmien.
Ak prejdete kontrolou, ste pripravení pokračovať.

### Skontrolovať, či URL majú sledovanie

Tento workflow zabezpečuje, že každá webová URL má sledovanie.
Tento repozitár je dostupný všetkým, takže je potrebné sledovať prístupy, aby sme vedeli, odkiaľ prúdi návštevnosť.

Ak chcete mať istotu, že vaše URL majú sledovanie, jednoducho skontrolujte, či je na konci URL text `?wt.mc_id=`.
Ak je pripojený k vašim URL, prejdete túto kontrolu.

Ak nie, môžete dostať nasledujúcu chybu.

![GitHub check urls missing tracking comment screenshot](../../translated_images/sk/github-check-urls-missing-tracking-comment.1bd00d20b24a1e2e.webp?WT.mc_id=academic-105485-koreyst "Screenshot z komentára na GitHub, ktorý ukazuje chýbajúce sledovanie v URL")

Na opravu tejto chyby otvorte cestu k súboru, ktorú workflow zvýraznil, a pridajte sledovacie ID na koniec URL.

Akonáhle pridáte sledovacie ID, uložte a odošlite zmeny, workflow sa opäť spustí na overenie vašich zmien.
Ak prejdete kontrolou, ste pripravení pokračovať.

### Skontrolovať, či URL neobsahujú miestne zameranie

Tento workflow zabezpečuje, že žiadna webová URL neobsahuje miestne zameranie špecifické pre krajinu.
Tento repozitár je dostupný ľuďom na celom svete, preto sa uistite, že do URL nezahrnujete miestne zameranie vašej krajiny.

Ak chcete mať istotu, že vaše URL neobsahujú miestne zameranie krajiny, jednoducho skontrolujte, či URL neobsahuje texty `/en-us/` alebo `/en/` alebo akékoľvek iné jazykové zameranie kdekoľvek v URL.
Ak nie sú prítomné vo vašich URL, prejdete túto kontrolu.

Ak nie, môžete dostať nasledujúcu chybu.

![GitHub check country locale comment screenshot](../../translated_images/sk/github-check-country-locale-comment.2f4fe93228161dee.webp?WT.mc_id=academic-105485-koreyst "Screenshot z komentára na GitHub, ktorý ukazuje pridané miestne zameranie do URL")

Na opravu tejto chyby otvorte cestu k súboru, ktorú workflow zvýraznil, a odstráňte miestne zameranie krajiny z URL.

Akonáhle odstránite miestne zameranie krajiny, uložte a odošlite zmeny, workflow sa opäť spustí na overenie vašich zmien.
Ak prejdete kontrolou, ste pripravení pokračovať.

Gratulujeme! Čoskoro vám poskytneme spätnú väzbu k vášmu príspevku.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->