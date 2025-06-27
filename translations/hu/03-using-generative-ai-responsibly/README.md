<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-06-25T11:30:52+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "hu"
}
-->
# Generatív AI felelős használata

> _Kattints a fenti képre a lecke videójának megtekintéséhez_

Könnyű elbűvölve lenni az AI és különösen a generatív AI iránt, de fontos megfontolni, hogyan használhatjuk azt felelősen. Figyelembe kell venni például, hogyan biztosíthatjuk, hogy a kimenet igazságos, ártalmatlan és így tovább. Ez a fejezet célja, hogy megadja a szükséges kontextust, mit kell figyelembe venni, és hogyan tehetünk aktív lépéseket az AI használatunk javítása érdekében.

## Bevezetés

Ez a lecke a következőket fogja lefedni:

- Miért kell prioritásként kezelni a Felelős AI-t generatív AI alkalmazások építésekor.
- A Felelős AI alapelvei és hogyan kapcsolódnak a generatív AI-hoz.
- Hogyan lehet ezeket a Felelős AI alapelveket gyakorlatba ültetni stratégia és eszközök segítségével.

## Tanulási célok

A lecke befejezése után tudni fogod:

- A Felelős AI fontosságát generatív AI alkalmazások építésekor.
- Mikor kell gondolkodni és alkalmazni a Felelős AI alapelveit generatív AI alkalmazások építésekor.
- Milyen eszközök és stratégiák állnak rendelkezésedre a Felelős AI koncepció gyakorlatba ültetéséhez.

## Felelős AI alapelvek

A generatív AI izgalma soha nem volt magasabb. Ez az izgalom sok új fejlesztőt, figyelmet és finanszírozást hozott ebbe a térbe. Bár ez nagyon pozitív mindenki számára, aki generatív AI-t használó termékeket és vállalatokat szeretne építeni, fontos, hogy felelősen haladjunk tovább.

A kurzus során a startupunk és AI oktatási termékünk építésére koncentrálunk. A Felelős AI alapelveit fogjuk használni: Igazságosság, Befogadás, Megbízhatóság/Biztonság, Biztonság és Adatvédelem, Átláthatóság és Felelősség. Ezekkel az alapelvekkel fogjuk felfedezni, hogyan kapcsolódnak a generatív AI használatához a termékeinkben.

## Miért kell prioritásként kezelni a Felelős AI-t

Termék építésekor, ha emberközpontú megközelítést alkalmazunk, és a felhasználó érdekeit tartjuk szem előtt, az vezet a legjobb eredményekhez.

A generatív AI egyedisége abban rejlik, hogy képes hasznos válaszokat, információkat, útmutatást és tartalmat létrehozni a felhasználók számára. Ez sok manuális lépés nélkül megvalósítható, ami nagyon lenyűgöző eredményekhez vezethet. Megfelelő tervezés és stratégiák nélkül sajnos káros eredményekhez is vezethet a felhasználók, a termék és a társadalom számára.

Nézzünk meg néhányat (de nem az összeset) ezek közül a potenciálisan káros eredmények közül:

### Hallucinációk

A hallucinációk olyan kifejezés, amelyet arra használunk, amikor egy LLM olyan tartalmat hoz létre, amely teljesen értelmetlen vagy valami, amit más források alapján tudunk, hogy téves.

Vegyünk például egy funkciót, amelyet a startupunk számára építünk, és amely lehetővé teszi a diákok számára, hogy történelmi kérdéseket tegyenek fel a modellnek. Egy diák felteszi a kérdést `Who was the sole survivor of Titanic?`

A modell olyan választ ad, mint az alábbi:

Ez egy nagyon magabiztos és alapos válasz. Sajnos helytelen. Még minimális kutatással is kiderülne, hogy több mint egy túlélője volt a Titanic katasztrófának. Egy diák számára, aki éppen csak elkezdi kutatni ezt a témát, ez a válasz elég meggyőző lehet ahhoz, hogy ne kérdőjelezzék meg, és tényként kezeljék. Ennek következményei lehetnek, hogy az AI rendszer megbízhatatlan lesz, és negatívan befolyásolja a startupunk hírnevét.

Bármely adott LLM minden iterációjával teljesítményjavulásokat tapasztaltunk a hallucinációk minimalizálása terén. Még ezzel a javulással is, nekünk, mint alkalmazásépítőknek és felhasználóknak továbbra is tisztában kell lennünk ezekkel a korlátozásokkal.

### Káros tartalom

Az előző szakaszban már említettük, amikor egy LLM helytelen vagy értelmetlen válaszokat ad. Egy másik kockázat, amivel tisztában kell lennünk, amikor egy modell káros tartalommal válaszol.

A káros tartalom meghatározása:

- Utasítások adása vagy önkárosítás vagy bizonyos csoportok károsításának ösztönzése.
- Gyűlölködő vagy lealacsonyító tartalom.
- Bármilyen típusú támadás vagy erőszakos cselekmény tervezésének irányítása.
- Utasítások adása arról, hogyan lehet illegális tartalmat találni vagy illegális cselekményeket elkövetni.
- Szexuálisan explicit tartalom megjelenítése.

A startupunk számára biztosítani szeretnénk, hogy megvannak a megfelelő eszközök és stratégiák annak megakadályozására, hogy ilyen típusú tartalom a diákok számára látható legyen.

### Igazságosság hiánya

Az igazságosság úgy definiálható, mint „biztosítani, hogy egy AI rendszer mentes legyen az elfogultságtól és diszkriminációtól, és hogy mindenkit igazságosan és egyenlően kezeljen.” A generatív AI világában biztosítani szeretnénk, hogy a marginalizált csoportok kizáró világnézetei ne erősödjenek meg a modell kimenetében.

Ezek a típusú kimenetek nem csak rombolóak a pozitív terméktapasztalatok építésében a felhasználóink számára, hanem további társadalmi károkat is okoznak. Mint alkalmazásépítők, mindig széles és változatos felhasználói bázist kell szem előtt tartanunk, amikor generatív AI-t használó megoldásokat építünk.

## Hogyan használjuk felelősen a generatív AI-t

Most, hogy azonosítottuk a felelős generatív AI fontosságát, nézzük meg a 4 lépést, amelyet megtehetünk AI megoldásaink felelős építése érdekében:

### Potenciális károk mérése

A szoftvertesztelés során teszteljük a felhasználó várható tevékenységeit egy alkalmazáson. Hasonlóan, a felhasználók által legvalószínűbben használt sokszínű promptok tesztelése jó módja a potenciális károk mérésének.

Mivel startupunk oktatási terméket épít, jó lenne előkészíteni egy listát az oktatással kapcsolatos promptokról. Ez lehet egy bizonyos tantárgy, történelmi tények, és diákélettel kapcsolatos promptok lefedése.

### Potenciális károk mérséklése

Most jött el az ideje, hogy megtaláljuk azokat a módokat, ahol megelőzhetjük vagy korlátozhatjuk a modell és annak válaszai által okozott potenciális károkat. Négy különböző rétegben tekinthetjük ezt át:

- **Modell**. A megfelelő modell kiválasztása a megfelelő felhasználási esethez. Nagyobb és összetettebb modellek, mint a GPT-4, nagyobb kockázatot jelenthetnek káros tartalomra, amikor kisebb és specifikusabb felhasználási esetekre alkalmazzák őket. A képzési adatok használata a finomhangoláshoz szintén csökkenti a káros tartalom kockázatát.

- **Biztonsági rendszer**. A biztonsági rendszer olyan eszközök és konfigurációk halmaza a modellt szolgáltató platformon, amelyek segítenek a károk mérséklésében. Például az Azure OpenAI szolgáltatás tartalomszűrő rendszere. A rendszereknek fel kell ismerniük a jailbreak támadásokat és a nem kívánt tevékenységeket, mint például a botok kérései.

- **Metaprompt**. A metapromptok és a földelés olyan módok, amelyekkel irányíthatjuk vagy korlátozhatjuk a modellt bizonyos viselkedések és információk alapján. Ez lehet a rendszerbemenetek használata a modell bizonyos határainak meghatározására. Emellett relevánsabb kimeneteket nyújtva a rendszer hatóköréhez vagy domainjéhez.

Ez lehet olyan technikák alkalmazása, mint a Retrieval Augmented Generation (RAG), hogy a modell csak megbízható forrásokból származó információkat húzzon le. Van egy későbbi lecke a kurzusban a [keresési alkalmazások építéséről](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst).

- **Felhasználói élmény**. Az utolsó réteg, ahol a felhasználó közvetlenül a modelllel lép kapcsolatba az alkalmazásunk felületén keresztül valamilyen módon. Így tervezhetjük a UI/UX-et, hogy korlátozzuk a felhasználót a modellhez küldhető bemenetek típusain, valamint a felhasználó számára megjelenített szövegek vagy képek. Az AI alkalmazás telepítésekor átláthatónak kell lennünk arról, hogy mit tud és mit nem tud a generatív AI alkalmazásunk.

Van egy teljes lecke, amely [AI alkalmazások UX tervezéséről szól](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst).

- **Modell értékelése**. Az LLM-ekkel való munka kihívást jelenthet, mert nem mindig van kontrollunk a modell képzési adatai felett. Ennek ellenére mindig értékelni kell a modell teljesítményét és kimeneteit. Fontos továbbra is mérni a modell pontosságát, hasonlóságát, földeltségét és a kimenet relevanciáját. Ez segít átláthatóságot és bizalmat nyújtani az érdekelt feleknek és a felhasználóknak.

### Felelős generatív AI megoldás üzemeltetése

Az AI alkalmazásaink körüli operatív gyakorlat kiépítése az utolsó szakasz. Ez magában foglalja az együttműködést a startupunk más részeivel, mint például a Jogi és Biztonsági részlegekkel, hogy biztosítsuk a szabályozási politikáknak való megfelelést. A bevezetés előtt terveket is szeretnénk készíteni a szállításról, az incidensek kezeléséről és a visszaállításról, hogy megakadályozzuk a felhasználóink számára okozott károk növekedését.

## Eszközök

Bár a felelős AI megoldások fejlesztése sok munkának tűnhet, ez a munka megéri az erőfeszítést. Ahogy a generatív AI területe növekszik, egyre több eszköz segíti a fejlesztőket abban, hogy hatékonyan integrálják a felelősséget a munkafolyamataikba. Például az [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) segíthet káros tartalmak és képek felismerésében API kéréseken keresztül.

## Tudásellenőrzés

Mik azok a dolgok, amelyekre oda kell figyelned a felelős AI használatának biztosítása érdekében?

1. Hogy a válasz helyes legyen.
2. Káros használat, hogy az AI-t ne használják bűncselekményekre.
3. Biztosítani, hogy az AI mentes legyen az elfogultságtól és diszkriminációtól.

A: A 2 és 3 helyes. A felelős AI segít abban, hogy mérlegeljük, hogyan lehet mérsékelni a káros hatásokat és az elfogultságokat, és még sok más.

## 🚀 Kihívás

Olvass utána az [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) szolgáltatásnak, és nézd meg, mit tudsz alkalmazni a saját használatodra.

## Nagyszerű munka, folytasd a tanulást

A lecke befejezése után nézd meg a [Generatív AI tanulási gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejleszd generatív AI tudásodat!

Lépj tovább a 4. leckére, ahol a [Prompt Engineering alapjait](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst) fogjuk megvizsgálni!

**Jogi nyilatkozat**:  
Ez a dokumentum AI fordítási szolgáltatással, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekinthető a hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást ajánlunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félremagyarázásokért.