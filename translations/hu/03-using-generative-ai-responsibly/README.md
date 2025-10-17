<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d57fad773cbeb69c5dd62e65c34200d",
  "translation_date": "2025-10-17T21:26:01+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "hu"
}
-->
# Generatív AI felelősségteljes használata

[![Generatív AI felelősségteljes használata](../../../translated_images/03-lesson-banner.1ed56067a452d97709d51f6cc8b6953918b2287132f4909ade2008c936cd4af9.hu.png)](https://youtu.be/YOp-e1GjZdA?si=7Wv4wu3x44L1DCVj)

> _Kattints a fenti képre a leckéhez tartozó videó megtekintéséhez_

Könnyű lenyűgözve lenni az AI-tól, különösen a generatív AI-tól, de fontos, hogy felelősségteljesen használjuk. Figyelembe kell venni például, hogyan biztosíthatjuk, hogy az eredmények igazságosak, ártalmatlanok legyenek, és még sok más szempontot. Ez a fejezet célja, hogy megadja a szükséges kontextust, mit kell figyelembe venni, és hogyan tehetünk aktív lépéseket AI-használatunk javítása érdekében.

## Bevezetés

Ez a lecke az alábbiakat fogja tárgyalni:

- Miért kell prioritásként kezelni a Felelős AI-t generatív AI alkalmazások fejlesztésekor.
- A Felelős AI alapelvei és azok kapcsolata a generatív AI-val.
- Hogyan lehet ezeket a Felelős AI alapelveket gyakorlatba ültetni stratégiák és eszközök segítségével.

## Tanulási célok

A lecke elvégzése után tudni fogod:

- Miért fontos a Felelős AI generatív AI alkalmazások fejlesztésekor.
- Mikor kell gondolkodni és alkalmazni a Felelős AI alapelveit generatív AI alkalmazások fejlesztésekor.
- Milyen eszközök és stratégiák állnak rendelkezésre a Felelős AI koncepciójának gyakorlatba ültetéséhez.

## A Felelős AI alapelvei

A generatív AI iránti lelkesedés soha nem volt még ilyen magas. Ez a lelkesedés rengeteg új fejlesztőt, figyelmet és finanszírozást hozott ebbe a térbe. Bár ez nagyon pozitív azok számára, akik generatív AI-t használó termékeket és vállalatokat szeretnének építeni, fontos, hogy felelősségteljesen haladjunk előre.

A kurzus során arra összpontosítunk, hogy felépítsük startupunkat és AI oktatási termékünket. A Felelős AI alapelveit fogjuk használni: Igazságosság, Befogadás, Megbízhatóság/Biztonság, Adatvédelem és Biztonság, Átláthatóság és Felelősségvállalás. Ezekkel az alapelvekkel fogjuk megvizsgálni, hogyan kapcsolódnak a generatív AI használatához termékeinkben.

## Miért kell prioritásként kezelni a Felelős AI-t?

Amikor terméket fejlesztünk, az emberközpontú megközelítés, amely a felhasználók érdekeit helyezi előtérbe, vezet a legjobb eredményekhez.

A generatív AI egyedisége abban rejlik, hogy képes hasznos válaszokat, információkat, útmutatásokat és tartalmakat létrehozni a felhasználók számára. Mindezt kevés manuális lépéssel, ami nagyon lenyűgöző eredményekhez vezethet. Megfelelő tervezés és stratégiák hiányában azonban sajnos káros eredményekhez is vezethet a felhasználók, a termék és a társadalom számára.

Nézzünk meg néhány (de nem az összes) potenciálisan káros eredményt:

### Hallucinációk

A hallucinációk kifejezés arra utal, amikor egy LLM olyan tartalmat hoz létre, amely teljesen értelmetlen vagy más források alapján téves.

Vegyük például, hogy építünk egy funkciót startupunk számára, amely lehetővé teszi a diákok számára, hogy történelmi kérdéseket tegyenek fel egy modellnek. Egy diák felteszi a kérdést: `Ki volt a Titanic egyetlen túlélője?`

A modell az alábbi választ adja:

![Prompt, amely azt kérdezi: "Ki volt a Titanic egyetlen túlélője"](../../../03-using-generative-ai-responsibly/images/ChatGPT-titanic-survivor-prompt.webp)

> _(Forrás: [Flying bisons](https://flyingbisons.com?WT.mc_id=academic-105485-koreyst))_

Ez egy nagyon magabiztos és alapos válasz. Sajnos téves. Még minimális kutatással is kiderülne, hogy több túlélője volt a Titanic katasztrófának. Egy diák számára, aki éppen elkezdi kutatni ezt a témát, ez a válasz elég meggyőző lehet ahhoz, hogy ne kérdőjelezze meg, és tényként kezelje. Ennek következményei lehetnek, hogy az AI rendszer megbízhatatlanná válik, és negatívan befolyásolja startupunk hírnevét.

Bármely LLM iterációjával láttunk teljesítményjavulást a hallucinációk minimalizálása terén. Még ezzel a javulással is, alkalmazásfejlesztőként és felhasználóként továbbra is tudatában kell lennünk ezeknek a korlátoknak.

### Káros tartalom

Az előző szakaszban tárgyaltuk, amikor egy LLM helytelen vagy értelmetlen válaszokat ad. Egy másik kockázat, amelyet figyelembe kell vennünk, az, amikor egy modell káros tartalommal válaszol.

A káros tartalom meghatározása:

- Utasításokat ad vagy bátorít önkárosításra vagy bizonyos csoportok elleni károkozásra.
- Gyűlöletkeltő vagy lealacsonyító tartalom.
- Támadások vagy erőszakos cselekmények tervezésének irányítása.
- Utasításokat ad arra, hogyan találjunk illegális tartalmat vagy kövessünk el illegális cselekményeket.
- Szexuálisan explicit tartalom megjelenítése.

Startupunk esetében biztosítani szeretnénk, hogy megfelelő eszközök és stratégiák álljanak rendelkezésre az ilyen típusú tartalom diákok számára történő megjelenítésének megelőzésére.

### Igazságtalanság

Az igazságosságot úgy határozzuk meg, mint „biztosítani, hogy az AI rendszer mentes legyen az elfogultságtól és diszkriminációtól, és mindenkit igazságosan és egyenlően kezeljen.” A generatív AI világában biztosítani szeretnénk, hogy a marginalizált csoportok kizáró világképei ne erősödjenek meg a modell kimenete által.

Az ilyen típusú kimenetek nemcsak romboló hatásúak a pozitív termékélmények építésére a felhasználók számára, hanem további társadalmi károkat is okoznak. Alkalmazásfejlesztőként mindig széles és sokszínű felhasználói bázist kell szem előtt tartanunk, amikor generatív AI-t használó megoldásokat építünk.

## Hogyan használjuk felelősségteljesen a generatív AI-t?

Most, hogy azonosítottuk a felelősségteljes generatív AI fontosságát, nézzük meg 4 lépést, amelyet megtehetünk AI megoldásaink felelősségteljes építése érdekében:

![Mitigációs ciklus](../../../translated_images/mitigate-cycle.babcd5a5658e1775d5f2cb47f2ff305cca090400a72d98d0f9e57e9db5637c72.hu.png)

### Potenciális károk mérése

A szoftvertesztelés során teszteljük a felhasználó várható tevékenységeit az alkalmazáson. Hasonlóképpen, a felhasználók által legvalószínűbben használt különféle promptok tesztelése jó módja a potenciális károk mérésének.

Mivel startupunk oktatási terméket épít, érdemes lenne előkészíteni egy listát oktatással kapcsolatos promptokról. Ez magában foglalhat bizonyos tantárgyakat, történelmi tényeket és diákélettel kapcsolatos promptokat.

### Potenciális károk enyhítése

Most eljött az idő, hogy megtaláljuk azokat a módokat, amelyekkel megelőzhetjük vagy korlátozhatjuk a modell és annak válaszai által okozott potenciális károkat. Ezt 4 különböző rétegben vizsgálhatjuk:

![Enyhítési rétegek](../../../translated_images/mitigation-layers.377215120b9a1159a8c3982c6bbcf41b6adf8c8fa04ce35cbaeeb13b4979cdfc.hu.png)

- **Modell**. A megfelelő modell kiválasztása a megfelelő felhasználási esethez. Nagyobb és összetettebb modellek, mint például a GPT-4, nagyobb kockázatot jelenthetnek káros tartalom szempontjából, ha kisebb és specifikusabb felhasználási esetekre alkalmazzák őket. A képzési adatok használata a finomhangoláshoz szintén csökkenti a káros tartalom kockázatát.

- **Biztonsági rendszer**. A biztonsági rendszer olyan eszközök és konfigurációk halmaza a modellt kiszolgáló platformon, amelyek segítenek enyhíteni a károkat. Példa erre az Azure OpenAI szolgáltatás tartalomszűrő rendszere. A rendszereknek képesnek kell lenniük a jailbreak támadások és nem kívánt tevékenységek, például botok kéréseinek észlelésére is.

- **Metaprompt**. A metapromptok és a megalapozás olyan módszerek, amelyekkel irányíthatjuk vagy korlátozhatjuk a modellt bizonyos viselkedések és információk alapján. Ez lehet például rendszerbemenetek használata a modell bizonyos korlátainak meghatározására. Ezenkívül relevánsabb kimenetek biztosítása a rendszer hatóköréhez vagy területéhez.

Ez lehet olyan technikák használata is, mint a Retrieval Augmented Generation (RAG), hogy a modell csak megbízható forrásokból származó információkat használjon. A kurzus későbbi részében lesz egy lecke a [keresési alkalmazások építéséről](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Felhasználói élmény**. Az utolsó réteg az, ahol a felhasználó közvetlenül a modelllel lép kapcsolatba alkalmazásunk felületén keresztül. Ily módon a UI/UX-t úgy tervezhetjük meg, hogy korlátozzuk a felhasználót azokra a bemenetekre, amelyeket a modellnek küldhet, valamint a felhasználónak megjelenített szövegekre vagy képekre. Az AI alkalmazás bevezetésekor átláthatónak kell lennünk azzal kapcsolatban, hogy mit tud és mit nem tud a generatív AI alkalmazásunk.

Egy teljes leckét szenteltünk az [AI alkalmazások UX tervezésének](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Modell értékelése**. Az LLM-ekkel való munka kihívást jelenthet, mivel nem mindig van kontrollunk a modell képzéséhez használt adatok felett. Ennek ellenére mindig értékelni kell a modell teljesítményét és kimeneteit. Fontos mérni a modell pontosságát, hasonlóságát, megalapozottságát és a kimenet relevanciáját. Ez segít átláthatóságot és bizalmat nyújtani az érdekelt feleknek és felhasználóknak.

### Felelős generatív AI megoldás működtetése

Az AI alkalmazások köré épített operatív gyakorlat kialakítása az utolsó szakasz. Ez magában foglalja az együttműködést startupunk más részeivel, például a jogi és biztonsági osztályokkal, hogy biztosítsuk a szabályozási politikáknak való megfelelést. A bevezetés előtt terveket kell készítenünk a szállításról, az incidensek kezeléséről és a visszavonásról, hogy megakadályozzuk a felhasználóinkat érő károk növekedését.

## Eszközök

Bár a Felelős AI megoldások fejlesztése sok munkának tűnhet, ez a munka megéri az erőfeszítést. Ahogy a generatív AI területe növekszik, egyre több eszköz áll rendelkezésre, amelyek segítik a fejlesztőket a felelősségteljes megközelítés hatékony integrálásában a munkafolyamatokba. Például az [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) segíthet káros tartalmak és képek észlelésében API-kérések révén.

## Tudásellenőrzés

Milyen dolgokra kell figyelned, hogy biztosítsd a felelősségteljes AI használatát?

1. Hogy a válasz helyes legyen.  
2. Káros használat, hogy az AI-t ne használják bűncselekmények elkövetésére.  
3. Biztosítani, hogy az AI mentes legyen az elfogultságtól és diszkriminációtól.  

A: A 2-es és 3-as helyes. A Felelős AI segít megfontolni, hogyan lehet enyhíteni a káros hatásokat, elfogultságokat és még sok mást.

## 🚀 Kihívás

Olvass utána az [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) szolgáltatásnak, és nézd meg, mit tudsz alkalmazni a saját használatodhoz.

## Nagyszerű munka, folytasd a tanulást

A lecke elvégzése után nézd meg a [Generatív AI tanulási gyűjteményt](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejleszd generatív AI ismereteidet!

Lépj tovább a 4. leckére, ahol a [Prompt Engineering alapjait](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst) fogjuk megvizsgálni!

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.