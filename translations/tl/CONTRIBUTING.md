# Pag-aambag

Tinatanggap ng proyektong ito ang mga kontribusyon at mungkahi. Karamihan sa mga kontribusyon ay nangangailangan sa iyo na
sumang-ayon sa isang Contributor License Agreement (CLA) na nagdedeklara na may karapatan ka,
at tunay na ginagawa, na ipagkaloob sa amin ang mga karapatan na gamitin ang iyong kontribusyon. Para sa mga detalye, bisitahin ang
<https://cla.microsoft.com>.

> Mahalaga: kapag nagsasalin ng teksto sa repo na ito, tiyakin na hindi ka gagamit ng machine translation. Susuriin namin ang mga pagsasalin sa pamamagitan ng komunidad, kaya mangyaring magboluntaryo lamang para sa mga pagsasalin sa mga wikang iyong bihasa.

Kapag nagsumite ka ng pull request, awtomatikong tutukuyin ng CLA-bot kung kailangan mong magbigay ng CLA at lagyan ng angkop na dekorasyon ang PR (hal., label, komento). Sundin lamang ang mga tagubiling ibinigay ng bot. Kailangan mo lamang gawin ito isang beses para sa lahat ng mga repository na gumagamit ng aming CLA.



## Kodigo ng Pag-uugali

Inampon ng proyektong ito ang [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst).
Para sa karagdagang impormasyon, basahin ang [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) o kontakin ang [opencode@microsoft.com](mailto:opencode@microsoft.com) para sa anumang dagdag na mga tanong o komento.

## May tanong o problema?

Mangyaring huwag magbukas ng mga isyu sa GitHub para sa mga pangkalahatang tanong ng suporta dahil ang listahan sa GitHub ay dapat gamitin para sa mga kahilingan ng tampok at mga ulat ng bug. Sa ganitong paraan, mas madaling ma-track ang mga aktwal na isyu o bug mula sa code at mapanatili ang pangkalahatang talakayan na hiwalay sa aktwal na code.

## Mga Typo, Isyu, Bug, at mga kontribusyon

Kapag nagsusumite ka ng anumang pagbabago sa repository ng Generative AI for Beginners, sundin ang mga rekomendasyong ito.

* Palaging i-fork ang repository sa iyong sariling account bago gumawa ng mga pagbabago
* Huwag pagsamahin ang maraming pagbabago sa isang pull request. Halimbawa, isumite ang anumang pag-aayos ng bug at mga update sa dokumentasyon gamit ang magkahiwalay na PR
* Kung nagpapakita ng merge conflicts ang iyong pull request, siguraduhing i-update ang iyong lokal na main upang maging salamin ng nasa main repository bago gumawa ng mga pagbabago
* Kung nagsusumite ka ng pagsasalin, mangyaring gumawa ng isang PR para sa lahat ng mga isinalin na file dahil hindi kami tumatanggap ng bahagyang pagsasalin para sa nilalaman
* Kung nagsusumite ka ng typo o pag-aayos ng dokumentasyon, maaari mong pagsamahin ang mga pagbabago sa isang PR kung saan naaangkop

## Saklaw ng redaksiyon at mga produktong galing sa ikatlong partido

Nakatuon ang kurikulum na ito sa mga teknolohiya ng Microsoft at vendor-neutral na mga bukas na pamantayan. Dapat may malinaw na layuning pang-edukasyon ang mga kontribusyon at hindi dapat pangunahing nilayong ipakilala o itaguyod ang isang komersyal na produkto ng ikatlong partido, hosted service, modelo ng router, SDK, MCP server, o iba pang vendor-specific na alok.

Maaaring banggitin ang open-source software at mga dependency ng ikatlong partido kapag kinakailangan upang ipaliwanag ang isang bukas na pamantayan o senaryo ng interoperability, ipinapakita nang neutral, at hindi nakatuon sa isang produkto ng vendor o hosted endpoint. Kung kasama sa iyong iminungkahing kontribusyon ang produkto o serbisyo ng vendor, magbukas ng isyu at kumuha ng pag-apruba mula sa tagapangasiwa bago magsumite ng pull request.

Kailangang ipahayag ng mga nag-aambag ang anumang may kaugnayang empleyo, pag-aari, pagsuporta, o iba pang kaugnayan sa isang produkto o serbisyong nabanggit sa kanilang kontribusyon. Huwag maglagay ng mga hindi suportadong pahayag tungkol sa presyo, pagganap, seguridad, privacy, o paghahambing. Ang mga runnable na halimbawa ay hindi dapat magpadala ng data ng mag-aaral o magsagawa ng pampublikong aksyon sa pamamagitan ng panlabas na third-party service bilang default.

## Pangkalahatang Gabay sa pagsulat

- Tiyakin na lahat ng iyong mga URL ay naka-wrap sa square brackets na sinusundan ng panaklong na walang dagdag na spaces sa paligid o loob nito `[]()`.
- Tiyakin na anumang relative link (ibig sabihin, mga link sa ibang mga file at folder sa repository) ay nagsisimula sa isang `./` na tumutukoy sa isang file o folder na nasa kasalukuyang working directory o isang `../` na tumutukoy sa file o folder na nasa parent working directory.
- Tiyakin na anumang relative link (ibig sabihin, mga link sa ibang mga file at folder sa repository) ay may tracking ID (ibig sabihin, `?` o `&` kasunod ang `wt.mc_id=` o `WT.mc_id=`) sa dulo nito.
- Tiyakin na anumang URL mula sa mga sumusunod na domain _github.com, microsoft.com, visualstudio.com, aka.ms, at azure.com_ ay may tracking ID (ibig sabihin, `?` o `&` kasunod ang `wt.mc_id=` o `WT.mc_id=`) sa dulo nito.
- Tiyakin na ang iyong mga link ay walang partikular na lokal na bansa (hal., `/en-us/` o `/en/`).
- Tiyakin na lahat ng mga imahe ay nakaimbak sa `./images` folder.
- Tiyakin na ang mga imahe ay may mga pangalan na naglalarawan gamit ang mga character sa Ingles, numero, at mga gitling sa pangalan ng iyong imahe.

## Mga Workflow ng GitHub

Kapag nagsumite ka ng pull request, apat na iba't ibang workflow ang gagana upang patotohanan ang mga naunang patakaran.
Sundin lamang ang mga tagubiling nakalista dito upang makapasa sa mga workflow check.

- [Check Broken Relative Paths](#check-broken-relative-paths)
- [Check Paths Have Tracking](#check-paths-have-tracking)
- [Check URLs Have Tracking](#check-urls-have-tracking)
- [Check URLs Don't Have Locale](#check-urls-dont-have-locale)

### Check Broken Relative Paths

Sinisigurado ng workflow na ito na ang anumang relative path sa iyong mga file ay gumagana.
Ang repository na ito ay naka-deploy sa GitHub pages kaya kailangan mong maging maingat sa pagta-type ng mga link na nagdudugtong sa lahat upang hindi ma-direkta ang sino man sa maling lugar.

Para matiyak na gumagana nang maayos ang iyong mga link, gamitin lamang ang VS code upang i-check iyon.

Halimbawa, kapag nag-hover ka sa anumang link sa iyong mga file, ipapakita sa iyo ang prompt para sundan ang link sa pamamagitan ng pag-click ng **ctrl + click**

![VS code follow links screenshot](../../translated_images/tl/vscode-follow-link.85520ab6a1237adc.webp?WT.mc_id=academic-105485-koreyst "Screenshot mula sa vs code prompt upang sundan ang isang link kapag nag-hover ka sa isang link.")

Kung nag-click ka sa isang link at hindi ito gumagana nang lokal, siguradong magti-trigger ito ng workflow at hindi gagana sa GitHub.

Upang ayusin ang isyung ito, subukang i-type ang link gamit ang tulong ng VS code.

Kapag nag-type ka ng `./` o `../`, ipapakita ng VS code sa iyo ang mga available na opsyon base sa iyong na-type.

![VS code select relative path screenshot](../../translated_images/tl/vscode-select-relative-path.3804eb73c3a9e5f2.webp?WT.mc_id=academic-105485-koreyst "Screenshot mula sa vs code prompt upang pumili ng relative path mula sa pop up list.")

Sundan ang path sa pamamagitan ng pag-click sa nais na file o folder at makakatiyak ka na hindi sira ang iyong path.

Kapag naidagdag mo na ang tamang relative path, i-save, at i-push ang iyong mga pagbabago, muling magti-trigger ang workflow upang suriin ang iyong mga pagbabago.
Kung makakapasa ka sa check, maaari ka nang magpatuloy.

### Check Paths Have Tracking

Sinisigurado ng workflow na ito na ang anumang relative path ay may tracking dito.
Ang repository na ito ay naka-deploy sa GitHub pages kaya kailangan nating subaybayan ang galaw sa pagitan ng iba't ibang mga file at folder.

Para matiyak na may tracking ang iyong mga relative path, i-check lamang ang sumusunod na teksto `?wt.mc_id=` sa dulo ng path.
Kung ito ay idinaragdag sa iyong mga relative paths, ipapasa mo ang tsek na ito.

Kung hindi, maaaring makakuha ka ng sumusunod na error.

![GitHub check paths missing tracking comment screenshot](../../translated_images/tl/github-check-paths-missing-tracking-comment.880d4afe03e898ff.webp?WT.mc_id=academic-105485-koreyst "Screenshot mula sa github comment na nagpapakita ng nawawalang tracking mula sa relative paths")

Upang ayusin ang isyung ito, subukang buksan ang file path na tinuturo ng workflow at idagdag ang tracking ID sa dulo ng relative paths.

Kapag naidagdag mo na ang tracking ID, i-save, at i-push ang iyong mga pagbabago, muling tatakbo ang workflow upang beripikahin ang iyong mga pagbabago.
Kung maipasa mo ang tsek, handa ka nang magpatuloy.

### Suriin Kung May Tracking ang URLs

Tinitiyak ng workflow na ito na ang anumang web URL ay may tracking sa loob.
Ang repositoryong ito ay bukas sa lahat kaya kailangan mong siguraduhin na naitatala ang pag-access upang malaman kung saan nanggagaling ang trapiko.

Upang matiyak na may tracking ang iyong mga URL, basta tingnan ang sumusunod na teksto `?wt.mc_id=` sa dulo ng URL.
Kung ito ay naka-append sa iyong mga URL, ipapasa mo ang tsek na ito.

Kung hindi, maaaring makakuha ka ng sumusunod na error.

![GitHub check urls missing tracking comment screenshot](../../translated_images/tl/github-check-urls-missing-tracking-comment.1bd00d20b24a1e2e.webp?WT.mc_id=academic-105485-koreyst "Screenshot mula sa github comment na nagpapakita ng nawawalang tracking mula sa mga url")

Upang ayusin ang isyung ito, subukang buksan ang file path na tinuturo ng workflow at idagdag ang tracking ID sa dulo ng mga URL.

Kapag naidagdag mo na ang tracking ID, i-save, at i-push ang iyong mga pagbabago, muling tatakbo ang workflow upang beripikahin ang iyong mga pagbabago.
Kung maipasa mo ang tsek, handa ka nang magpatuloy.

### Suriin Kung Walang Locale ang URLs

Tinitiyak ng workflow na ito na walang country specific locale sa anumang web URL.
Ang repositoryong ito ay bukas sa lahat sa buong mundo kaya kailangan mong siguraduhin na hindi isasama ang locale ng iyong bansa sa mga URL.

Upang matiyak na walang country locale ang iyong mga URL, basta hanapin ang sumusunod na teksto `/en-us/` o `/en/` o anumang iba pang language locale kahit saan sa URL.
Kung wala ito sa iyong mga URL, ipapasa mo ang tsek na ito.

Kung hindi, maaaring makakuha ka ng sumusunod na error.

![GitHub check country locale comment screenshot](../../translated_images/tl/github-check-country-locale-comment.2f4fe93228161dee.webp?WT.mc_id=academic-105485-koreyst "Screenshot mula sa github comment na nagpapakita ng naidagdag na country locale sa mga urls")

Upang ayusin ang isyung ito, subukang buksan ang file path na tinuturo ng workflow at alisin ang country locale mula sa mga URL.

Kapag naalis mo na ang country locale, i-save, at i-push ang iyong mga pagbabago, muling tatakbo ang workflow upang beripikahin ang iyong mga pagbabago.
Kung maipasa mo ang tsek, handa ka nang magpatuloy.

Binabati kita! Makikipag-ugnayan kami sa iyo sa lalong madaling panahon na may feedback tungkol sa iyong kontribusyon.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->