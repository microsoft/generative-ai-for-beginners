[![Integrointi funktiokutsuihin](../../../translated_images/fi/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Generatiivisen tekoälyn sovelluskehityksen elinkaari

Tärkeä kysymys kaikille tekoälysovelluksille on tekoälyominaisuuksien merkityksellisyys, koska tekoäly on nopeasti kehittyvä ala. Jotta sovelluksesi pysyy merkityksellisenä, luotettavana ja vankkana, on sitä seurattava, arvioitava ja parannettava jatkuvasti. Tässä genAI-elinkaari tulee mukaan.

Generatiivisen tekoälyn elinkaari on kehys, joka ohjaa sinua generatiivisen tekoälysovelluksen kehitys-, käyttöönotto- ja ylläpitovaiheiden läpi. Se auttaa määrittelemään tavoitteesi, mittaamaan suorituskykysi, tunnistamaan haasteesi sekä toteuttamaan ratkaisusi. Se auttaa myös sovittamaan sovelluksesi eettisiin ja laillisiin standardeihin toimialallasi ja sidosryhmilläsi. Noudattamalla generatiivisen tekoälyn elinkaarta voit varmistaa, että sovelluksesi tuottaa aina arvoa ja tyydyttää käyttäjäsi.

## Johdanto

Tässä luvussa opit:

- MLOpsin ja LLMOpsin paradigman muutoksen ymmärtämisen
- LLM-elinkaaren
- Elinkaarityökalut
- Elinkaaren mittaaminen ja arviointi

## MLOpsin ja LLMOpsin paradigman muutoksen ymmärtäminen

LLM:t ovat uusi työkalu tekoälyn arsenaalissa, ne ovat uskomattoman tehokkaita analyysi- ja generointitehtävissä sovelluksissa, mutta tällä voimalla on seurauksia siinä, miten virtaviivaistamme tekoäly- ja perinteisiä koneoppimistehtäviä.

Tarvitsemme uuden paradigman tämän työkalun mukauttamiseksi dynaamisesti, oikeilla kannustimilla. Voimme luokitella vanhemmat tekoälysovellukset "ML-sovelluksiksi" ja uudemmat "GenAI-sovelluksiksi" tai vain "tekoälysovelluksiksi", heijastaen aikakauden valtavirran teknologiaa ja tekniikoita. Tämä muuttaa kertomustamme monin tavoin, katso seuraavaa vertailua.

![LLMOps vs. MLOps vertailu](../../../translated_images/fi/01-llmops-shift.29bc933cb3bb0080.webp)

Huomaa, että LLMOpsissa keskitymme enemmän sovelluskehittäjiin, käyttämällä integraatioita keskeisenä pisteenä, hyödyntäen "Mallipalveluina" ja ajatellen seuraavia mittareita.

- Laatu: Vastauksen laatu
- Vahinko: Vastuullinen tekoäly
- Rehellisyys: Vastauksen perusteltavuus (Onko järkevää? Onko se oikea?)
- Kustannukset: Ratkaisun budjetti
- Viive: Keskimääräinen aika token-vastaukseen

## LLM-elinkaari

Ensin, elinkaaren ja muutosten ymmärtämiseksi, tarkastellaan seuraavaa infographic-kuvaa.

![LLMOps infographic](../../../translated_images/fi/02-llmops.70a942ead05a7645.webp)

Kuten huomaat, tämä eroaa tavallisista MLOpsin elinkaareista. LLM:illä on monia uusia vaatimuksia, kuten Prompting, erilaisia tekniikoita laadun parantamiseksi (Fine-Tuning, RAG, Meta-Promptit), erilaiset arvioinnit ja vastuu vastuullisen tekoälyn kanssa, lopuksi uudet arviointimittarit (Laadukas, Vahinko, Rehellisyys, Kustannus ja Viive).

Otetaan esimerkiksi ajattelutapamme ideointi. Käytämme promptteja kokeillaksemme erilaisia LLM:iä tutkiaksemme mahdollisuuksia testata hypoteesien oikeellisuutta.

Huomaa, että tämä ei ole lineaarista, vaan integroitua silmukkaa, iteratiivista ja kaikuporras.

Miten voisimme tutkia näitä vaiheita? Tarkastellaan yksityiskohtaisesti, miten voisimme rakentaa elinkaaren.

![LLMOps Workflow](../../../translated_images/fi/03-llm-stage-flows.3a1e1c401235a6cf.webp)

Tämä saattaa näyttää hieman monimutkaiselta, keskitytään ensin kolmeen isoon vaiheeseen.

1. Ideointi/Tutkiminen: Tutkimusvaiheessa voimme tutkia liiketoiminnan tarpeiden mukaan. Prototypointi, [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) luominen ja testaaminen, onko se riittävän tehokas hypoteesillemme.
1. Rakentaminen/Lisäys: Toteutusvaiheessa aloitamme arvioinnin isommille tietoaineistoille, käytämme tekniikoita kuten Fine-tuning ja RAG, tarkistaaksemme ratkaisumme vakauden. Jos ei toimi, uudelleen toteutus, uusien vaiheiden lisääminen tai tiedon uudelleen jäsentely voi auttaa. Testattuamme virtamme ja mittakaavamme ja varmistettuamme mittarit, voimme edetä seuraavaan vaiheeseen.
1. Operatiivistaminen: Integrointivaiheessa lisätään valvonta- ja hälytysjärjestelmät järjestelmään, käyttöönotto ja sovelluksen integrointi sovellukseen.

Sitten on hallintakierros, keskittyen turvallisuuteen, noudattamiseen ja hallintoon.

Onnittelut, nyt sinulla on tekoälysovellus valmiina käyttöön ja toiminnassa. Käytännön kokemusta varten tutustu [Contoso Chat Demo](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst) -sovellukseen.

Mitä työkaluja voimme käyttää?

## Elinkaarityökalut

Microsoft tarjoaa [Azure AI Platformin](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) ja [PromptFlow'n](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst), jotka helpottavat ja tekevät elinkaaren toteutuksesta helppoa ja valmista.

[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) antaa sinun käyttää [Microsoft Foundrya](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst). Microsoft Foundry (entinen Azure AI Studio) on verkkosivusto, jossa voit tutkia malleja, esimerkkejä ja työkaluja, hallita resurssiasi sekä käyttää UI-kehitysvirtauksia sekä SDK/CLI vaihtoehtoja koodipohjaiseen kehitykseen.

![Azure AI mahdollisuudet](../../../translated_images/fi/04-azure-ai-platform.80203baf03a12fa8.webp)

Azure AI mahdollistaa useiden resurssien käytön operaatioidesi, palveluidesi, projektiesi, vektorihaun ja tietokantatarpeidesi hallintaan.

![LLMOps Azure AI:lla](../../../translated_images/fi/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

Rakenna Proof-of-Conceptistä (POC) suuriin mittakaavasovelluksiin PromptFlow'lla:

- Suunnittele ja rakenna sovelluksia VS Codessa visuaalisilla ja toiminnallisilla työkaluilla
- Testaa ja jalosta sovelluksiasi laadukkaaksi tekoälyksi vaivattomasti.
- Käytä Microsoft Foundrya pilven kanssa integraatioon ja iterointiin, puskuun ja käyttöönottoon nopeaa integraatiota varten.

![LLMOps PromptFlow'lla](../../../translated_images/fi/06-llm-promptflow.a183eba07a3a7fdf.webp)

## Hienoa! Jatka oppimista!

Upea homma, opi nyt lisää sovelluksen rakenteesta käyttämään näitä käsitteitä [Contoso Chat Appissa](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), jossa Cloud Advocacy esittelee nämä konseptit demoillaan. Lisää sisältöä löydät [Ignite breakout -sessiossamme!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Tarkista nyt Luku 15, ymmärtääksesi miten [Retrieval Augmented Generation ja vektoritietokannat](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) vaikuttavat generatiiviseen tekoälyyn ja tekevät sovelluksista kiinnostavampia!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->