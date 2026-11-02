# Pagsasaambag

Tinatanggap ng proyektong ito ang mga pagsasaambag at suhestiyon. Karamihan sa mga pagsasaambag ay nangangailangan ng iyong
pagsang-ayon sa isang Contributor License Agreement (CLA) na nagsasaad na mayroon kang karapatan,
at talagang ginagawa ito, na bigyan kami ng mga karapatan na gamitin ang iyong ambag. Para sa mga detalye, bisitahin
<https://cla.microsoft.com>.

> Mahalaga: kapag nagsasalin ng teksto sa repo na ito, tiyakin na hindi ka gagamit ng machine translation. Susuriin namin ang mga pagsasalin sa pamamagitan ng komunidad, kaya mangyaring magboluntaryo lamang para sa mga pagsasalin sa mga wikang bihasa ka.

Kapag nagsumite ka ng pull request, awtomatikong malalaman ng CLA-bot kung kailangan mong
magbigay ng CLA at lalagyan ng tamang dekorasyon ang PR (hal., label, komento). Sundin lamang ang
mga tagubilin na ibinibigay ng bot. Gagawin mo lang ito nang isang beses sa lahat ng repository na gumagamit ng aming CLA.

## Kodigo ng Pag-uugali

Inampon ng proyektong ito ang [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst).
Para sa karagdagang impormasyon basahin ang [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) o makipag-ugnayan sa [opencode@microsoft.com](mailto:opencode@microsoft.com) para sa mga karagdagang tanong o komento.

## Tanong o Problema?

Mangyaring huwag magbukas ng mga isyu sa GitHub para sa mga pangkalahatang tanong ng suporta dahil ang listahan sa GitHub ay dapat gamitin para sa mga kahilingan ng tampok at mga ulat ng bug. Sa ganitong paraan mas madali naming masusubaybayan ang mga tunay na isyu o bug mula sa code at mapanatili ang pangkalahatang talakayan na hiwalay sa aktwal na code.

## Mga Typo, Isyu, Bug at mga ambag

Kapag nagsusumite ka ng anumang pagbabago sa repository ng Generative AI for Beginners, sundin ang mga mungkahing ito.

* Laging fork-in ang repository papunta sa iyong sariling account bago gawin ang mga pagbabago
* Huwag pagsamahin ang maraming pagbabago sa isang pull request. Halimbawa, isumite ang anumang pag-aayos ng bug at mga update sa dokumentasyon gamit ang hiwalay na mga PR
* Kung nagpapakita ng merge conflicts ang iyong pull request, siguraduhing i-update mo ang iyong lokal na main upang maging repleksyon ng nasa pangunahing repository bago gawin ang mga pagbabago
* Kung nagsusumite ka ng pagsasalin, mangyaring gumawa ng isang PR para sa lahat ng isinalin na files dahil hindi kami tumatanggap ng bahagyang pagsasalin para sa nilalaman
* Kung nagsusumite ka ng typo o pag-aayos sa dokumentasyon, maaari mong pagsamahin ang mga pagbabago sa isang PR kung angkop

## Saklaw ng editoryal at mga produkto ng third-party

Nakatuon ang kurikulum na ito sa mga teknolohiya ng Microsoft at bukas na mga pamantayang vendor-neutral. Ang mga ambag ay dapat maglingkod sa isang malinaw na layunin sa edukasyon at hindi pangunahing nilalayong ipakilala o itaguyod ang isang third-party na produktong komersyal, hosted service, modelo ng router, SDK, MCP server, o iba pang alok na partikular sa vendor.

Maaaring banggitin ang open-source software at mga third-party na dependencies kapag kinakailangan upang ipaliwanag ang isang bukas na pamantayan o senaryo ng interoperability, ay ipinapakita nang neutral, at hindi nakatuon sa produkto o hosted endpoint ng isang vendor. Kung ang iyong iminungkahing ambag ay may kasamang produktong partikular sa vendor o serbisyo, magbukas ng isyu at kumuha ng pahintulot mula sa tagapangasiwa bago magsumite ng pull request.

Dapat ibunyag ng mga tagapag-ambag ang anumang kaugnay na empleyo, pagmamay-ari, sponsorship, o iba pang ugnayan sa isang produktong o serbisyong binanggit sa kanilang ambag. Huwag maglagay ng hindi suportadong mga pahayag tungkol sa presyo, performance, seguridad, privacy, o paghahambing. Ang mga maaaring patakbuhin na halimbawa ay hindi dapat magpadala ng data ng mag-aaral o gumawa ng mga pampublikong aksyon sa pamamagitan ng isang eksternal na third-party service bilang default.

## Pangkalahatang Gabay sa pagsulat

- Siguraduhing lahat ng iyong mga URL ay nakakulong sa mga parisukat na panaklong na sinusundan ng panaklong na walang dagdag na espasyo sa paligid o sa loob nila `[]()`.
- Siguraduhing ang anumang relatibong link (i.e. mga link sa ibang mga file at folder sa repository) ay nagsisimula sa isang `./` na tumutukoy sa isang file o folder na nasa kasalukuyang working directory o isang `../` na tumutukoy sa isang file o folder na nasa parent working directory.
- Tiyaking anumang relative link (i.e. mga link sa ibang mga file at folder sa repository) ay may tracking ID (i.e. `?` o `&` pagkatapos ay `wt.mc_id=` o `WT.mc_id=`) sa dulo nito.
- Tiyaking anumang URL mula sa mga sumusunod na domain _github.com, microsoft.com, visualstudio.com, aka.ms, at azure.com_ ay may tracking ID (i.e. `?` o `&` pagkatapos ay `wt.mc_id=` o `WT.mc_id=`) sa dulo nito.
- Tiyaking ang iyong mga link ay walang partikular na locale ng bansa sa loob nila (i.e. `/en-us/` o `/en/`).
- Tiyaking lahat ng mga imahe ay naka-imbak sa folder na `./images`.
- Tiyaking ang mga imahe ay may mga deskriptibong pangalan gamit ang mga karakter na Ingles, mga numero, at gitling sa pangalan ng iyong imahe.

## Mga Workflow ng GitHub

Kapag nagsumite ka ng pull request, apat na magkakaibang workflow ang mao-trigger upang i-validate ang mga naunang alituntunin.
Sundin lamang ang mga tagubilin na nakalista dito upang pumasa sa mga workflow check.

- [Suriin ang mga Sirang Relative Path](#check-broken-relative-paths)
- [Suriin ang mga Path na may Tracking](#check-paths-have-tracking)
- [Suriin ang mga URL na may Tracking](#check-urls-have-tracking)
- [Suriin na Walang Locale ang mga URL](#check-urls-dont-have-locale)

### Suriin ang mga Sirang Relative Path

Tinitiyak ng workflow na ito na anumang relative path sa iyong mga file ay gumagana.
Ang repositoryong ito ay na-deploy sa GitHub pages kaya kailangan mong maging maingat kapag nagta-type ng mga link na nag-uugnay sa lahat upang hindi madaan ang sinuman sa maling lugar.

Upang matiyak na ang iyong mga link ay gumagana nang maayos, gamitin lamang ang VS code upang suriin iyon.

Halimbawa, kapag nilagyan mo ng hover ang anumang link sa iyong mga file, ipapahiwatig ka na sundan ang link sa pamamagitan ng pagpindot ng **ctrl + click**

![VS code follow links screenshot](../../translated_images/tl/vscode-follow-link.85520ab6a1237adc.webp?WT.mc_id=academic-105485-koreyst "Screenshot mula sa vs code prompt upang sundan ang isang link kapag nilagyan ng hover ang isang link.")

Kapag nag-click ka sa isang link at hindi ito gumana lokal, tiyak na ito ay magt-trigger sa workflow at hindi gagana sa GitHub.

Upang ayusin ang isyung ito, subukang i-type ang link gamit ang tulong ng VS code.

Kapag nag-type ka ng `./` o `../`, ipapahiwatig ng VS code na pumili mula sa mga magagamit na opsyon ayon sa iyong na-type.

![VS code select relative path screenshot](../../translated_images/tl/vscode-select-relative-path.3804eb73c3a9e5f2.webp?WT.mc_id=academic-105485-koreyst "Screenshot mula sa vs code prompt upang pumili ng relative path mula sa isang pop up na listahan.")

Sundan ang path sa pamamagitan ng pag-click sa nais na file o folder at matitiyak mong hindi sirang ang iyong path.

Kapag idinagdag mo na ang tamang relative path, i-save, at ipush ang iyong mga pagbabago, muling mai-trigger ang workflow upang beripikahin ang iyong mga pagbabago.
Kapag nakapasa ka sa check, maaari ka nang magpatuloy.

### Suriin na may Tracking ang mga Path

Tinitiyak ng workflow na ito na anumang relative path ay may tracking sa loob nito.
Ang repositoryong ito ay na-deploy sa GitHub pages kaya kailangan nating subaybayan ang paggalaw sa pagitan ng iba't ibang mga file at folder.

Upang matiyak na ang iyong mga relative path ay may tracking, suriin lamang ang sumusunod na teksto `?wt.mc_id=` sa dulo ng path.
Kung ito ay nakadugtong sa iyong mga relative path, makakapasa ka sa check na ito.

Kung hindi, maaari kang makatanggap ng sumusunod na error.

![GitHub check paths missing tracking comment screenshot](../../translated_images/tl/github-check-paths-missing-tracking-comment.880d4afe03e898ff.webp?WT.mc_id=academic-105485-koreyst "Screenshot mula sa comment sa github na nagpapakita ng nawawalang tracking mula sa mga relative path")

Upang ayusin ang isyung ito, subukang buksan ang file path na tinukoy ng workflow at idagdag ang tracking ID sa dulo ng mga relative path.

Kapag idinagdag mo na ang tracking ID, i-save, at ipush ang iyong mga pagbabago, muling mai-trigger ang workflow upang beripikahin ang mga pagbabago.
Kapag nakapasa ka sa check, maaari ka nang magpatuloy.

### Suriin na may Tracking ang mga URL

Tinitiyak ng workflow na ito na anumang web URL ay may tracking sa loob nito.
Ang repositoryong ito ay available para sa lahat kaya kailangan mong tiyakin na subaybayan ang access upang malaman kung saan nanggagaling ang trapiko.

Upang matiyak na ang iyong mga URL ay may tracking, suriin lamang ang sumusunod na teksto `?wt.mc_id=` sa dulo ng URL.
Kung ito ay nakakabit sa iyong mga URL, makakapasa ka sa check na ito.

Kung hindi, maaari kang makatanggap ng sumusunod na error.

![GitHub check urls missing tracking comment screenshot](../../translated_images/tl/github-check-urls-missing-tracking-comment.1bd00d20b24a1e2e.webp?WT.mc_id=academic-105485-koreyst "Screenshot mula sa comment sa github na nagpapakita ng nawawalang tracking mula sa mga URL")

Upang ayusin ang isyung ito, subukang buksan ang file path na tinukoy ng workflow at idagdag ang tracking ID sa dulo ng mga URL.

Kapag idinagdag mo na ang tracking ID, i-save, at ipush ang iyong mga pagbabago, muling mai-trigger ang workflow upang beripikahin ang mga pagbabago.
Kapag nakapasa ka sa check, maaari ka nang magpatuloy.

### Suriin na Walang Locale ang mga URL

Tinitiyak ng workflow na ito na anumang web URL ay walang partikular na locale ng bansa sa loob nito.
Ang repositoryong ito ay available para sa lahat sa buong mundo kaya kailangan mong tiyakin na hindi isasama ang locale ng iyong bansa sa mga URL.

Upang matiyak na ang iyong mga URL ay walang locale ng bansa, suriin lamang ang sumusunod na teksto `/en-us/` o `/en/` o anumang ibang language locale saanman sa URL.
Kung wala ito sa iyong mga URL, makakapasa ka sa check na ito.

Kung hindi, maaari kang makatanggap ng sumusunod na error.

![GitHub check country locale comment screenshot](../../translated_images/tl/github-check-country-locale-comment.2f4fe93228161dee.webp?WT.mc_id=academic-105485-koreyst "Screenshot mula sa comment sa github na nagpapakita ng idinagdag na country locale sa mga URL")

Upang ayusin ang isyung ito, subukang buksan ang file path na tinukoy ng workflow at alisin ang country locale mula sa mga URL.

Kapag naalis mo na ang country locale, i-save, at ipush ang iyong mga pagbabago, muling mai-trigger ang workflow upang beripikahin ang mga pagbabago.
Kapag nakapasa ka sa check, maaari ka nang magpatuloy.

Binabati kita! Babalikan ka namin sa lalong madaling panahon na may feedback tungkol sa iyong kontribusyon.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->