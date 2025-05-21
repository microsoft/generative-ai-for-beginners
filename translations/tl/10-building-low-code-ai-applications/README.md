<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f5ff3b6204a695a117d6f452403c95f7",
  "translation_date": "2025-05-19T20:52:42+00:00",
  "source_file": "10-building-low-code-ai-applications/README.md",
  "language_code": "tl"
}
-->
# Pagbuo ng Low Code AI Applications

## Panimula

Ngayon na natutunan na natin kung paano bumuo ng mga application na nag-generate ng imahe, pag-usapan natin ang low code. Ang Generative AI ay maaaring gamitin sa iba't ibang larangan kabilang ang low code, ngunit ano ang low code at paano natin ito madaragdagan ng AI?

Ang pagbuo ng mga app at solusyon ay naging mas madali para sa mga tradisyonal na developer at hindi developer sa pamamagitan ng paggamit ng Low Code Development Platforms. Ang mga Low Code Development Platforms ay nagbibigay-daan sa iyo na bumuo ng mga app at solusyon na may kaunti o walang code. Ito ay natatamo sa pamamagitan ng pagbibigay ng isang visual na kapaligiran sa pag-develop na nagbibigay-daan sa iyo na i-drag at i-drop ang mga bahagi upang bumuo ng mga app at solusyon. Ito ay nagbibigay-daan sa iyo na bumuo ng mga app at solusyon nang mas mabilis at may mas kaunting mga resources. Sa leksyong ito, masusing tatalakayin natin kung paano gamitin ang Low Code at kung paano pahusayin ang low code development gamit ang AI gamit ang Power Platform.

Ang Power Platform ay nagbibigay sa mga organisasyon ng pagkakataon na bigyang kapangyarihan ang kanilang mga koponan na bumuo ng kanilang sariling mga solusyon sa pamamagitan ng isang intuitive na low-code o no-code na kapaligiran. Ang kapaligirang ito ay tumutulong na gawing simple ang proseso ng pagbuo ng mga solusyon. Sa Power Platform, ang mga solusyon ay maaaring buuin sa loob ng mga araw o linggo sa halip na mga buwan o taon. Ang Power Platform ay binubuo ng limang pangunahing produkto: Power Apps, Power Automate, Power BI, Power Pages at Copilot Studio.

Saklaw ng leksyong ito ang:

- Panimula sa Generative AI sa Power Platform
- Panimula sa Copilot at kung paano ito gamitin
- Paggamit ng Generative AI upang bumuo ng mga app at daloy sa Power Platform
- Pag-unawa sa AI Models sa Power Platform gamit ang AI Builder

## Mga Layunin sa Pag-aaral

Sa pagtatapos ng leksyong ito, magagawa mo:

- Maunawaan kung paano gumagana ang Copilot sa Power Platform.

- Bumuo ng isang Student Assignment Tracker App para sa aming education startup.

- Bumuo ng isang Invoice Processing Flow na gumagamit ng AI upang kunin ang impormasyon mula sa mga invoice.

- Ilapat ang pinakamahusay na mga kasanayan kapag gumagamit ng Create Text with GPT AI Model.

Ang mga kasangkapan at teknolohiya na gagamitin mo sa leksyong ito ay:

- **Power Apps**, para sa Student Assignment Tracker app, na nagbibigay ng low-code development environment para sa pagbuo ng mga app upang subaybayan, pamahalaan at makipag-ugnayan sa data.

- **Dataverse**, para sa pag-iimbak ng data para sa Student Assignment Tracker app kung saan ang Dataverse ay magbibigay ng low-code data platform para sa pag-iimbak ng data ng app.

- **Power Automate**, para sa Invoice Processing flow kung saan magkakaroon ka ng low-code development environment para sa pagbuo ng mga workflows upang awtomatikong maproseso ang Invoice Processing process.

- **AI Builder**, para sa Invoice Processing AI Model kung saan gagamitin mo ang prebuilt AI Models upang maproseso ang mga invoice para sa aming startup.

## Generative AI sa Power Platform

Ang pagpapahusay ng low-code development at application gamit ang generative AI ay isang pangunahing pokus na lugar para sa Power Platform. Ang layunin ay bigyang-daan ang lahat na bumuo ng AI-powered apps, sites, dashboards at awtomatikong mga proseso gamit ang AI, _nang hindi nangangailangan ng anumang data science expertise_. Ang layuning ito ay natatamo sa pamamagitan ng pagsasama ng generative AI sa low-code development experience sa Power Platform sa anyo ng Copilot at AI Builder.

### Paano ito gumagana?

Ang Copilot ay isang AI assistant na nagbibigay-daan sa iyo na bumuo ng Power Platform solutions sa pamamagitan ng paglalarawan ng iyong mga pangangailangan sa isang serye ng mga hakbang na pakikipag-usap gamit ang natural na wika. Maaari mong, halimbawa, utusan ang iyong AI assistant na tukuyin kung ano ang mga field na gagamitin ng iyong app at ito ay lilikha ng parehong app at ang ilalim na data model o maaari mong tukuyin kung paano mag-set up ng flow sa Power Automate.

Maaari mong gamitin ang Copilot driven functionalities bilang isang tampok sa iyong app screens upang bigyang-daan ang mga user na matuklasan ang mga pananaw sa pamamagitan ng pakikipag-usap na interaksyon.

Ang AI Builder ay isang low-code AI capability na magagamit sa Power Platform na nagbibigay-daan sa iyo na gumamit ng AI Models upang makatulong sa iyo na awtomatikong mga proseso at hulaan ang mga kinalabasan. Sa AI Builder maaari mong dalhin ang AI sa iyong mga app at daloy na kumokonekta sa iyong data sa Dataverse o sa iba't ibang cloud data sources, tulad ng SharePoint, OneDrive o Azure.

Ang Copilot ay magagamit sa lahat ng Power Platform products: Power Apps, Power Automate, Power BI, Power Pages at Power Virtual Agents. Ang AI Builder ay magagamit sa Power Apps at Power Automate. Sa leksyong ito, magtutuon tayo kung paano gamitin ang Copilot at AI Builder sa Power Apps at Power Automate upang bumuo ng solusyon para sa aming education startup.

### Copilot sa Power Apps

Bilang bahagi ng Power Platform, ang Power Apps ay nagbibigay ng low-code development environment para sa pagbuo ng mga app upang subaybayan, pamahalaan at makipag-ugnayan sa data. Ito ay isang suite ng mga serbisyo sa pagbuo ng app na may isang scalable data platform at ang kakayahang kumonekta sa cloud services at on-premises data. Ang Power Apps ay nagbibigay-daan sa iyo na bumuo ng mga app na tumatakbo sa mga browser, tablet, at phone, at maaaring ibahagi sa mga kasamahan. Ang Power Apps ay nagpapadali sa mga user sa pagbuo ng app gamit ang isang simpleng interface, upang ang bawat business user o pro developer ay makabuo ng custom na apps. Ang karanasan sa pagbuo ng app ay pinahusay din sa Generative AI sa pamamagitan ng Copilot.

Ang tampok na copilot AI assistant sa Power Apps ay nagbibigay-daan sa iyo na ilarawan kung anong uri ng app ang kailangan mo at kung anong impormasyon ang nais mong subaybayan, kolektahin, o ipakita ng iyong app. Ang Copilot ay bumubuo ng isang responsive Canvas app batay sa iyong paglalarawan. Maaari mo nang i-customize ang app upang matugunan ang iyong mga pangangailangan. Ang AI Copilot ay bumubuo at nagmumungkahi ng isang Dataverse Table na may mga field na kailangan mo upang iimbak ang data na nais mong subaybayan at ilang sample data. Titingnan natin kung ano ang Dataverse at kung paano mo ito magagamit sa Power Apps sa leksyong ito sa susunod. Maaari mo nang i-customize ang table upang matugunan ang iyong mga pangangailangan gamit ang AI Copilot assistant feature sa pamamagitan ng mga hakbang na pakikipag-usap. Ang tampok na ito ay readily available mula sa Power Apps home screen.

### Copilot sa Power Automate

Bilang bahagi ng Power Platform, ang Power Automate ay nagbibigay-daan sa mga user na lumikha ng automated workflows sa pagitan ng mga application at serbisyo. Ito ay tumutulong na awtomatikong mga repetitive business processes tulad ng komunikasyon, pagkuha ng data, at pag-apruba ng desisyon. Ang simpleng interface nito ay nagbibigay-daan sa mga user na may bawat teknikal na kakayahan (mula sa mga baguhan hanggang sa mga bihasang developer) na awtomatikong mga gawain sa trabaho. Ang karanasan sa pagbuo ng workflow ay pinahusay din sa Generative AI sa pamamagitan ng Copilot.

Ang tampok na copilot AI assistant sa Power Automate ay nagbibigay-daan sa iyo na ilarawan kung anong uri ng flow ang kailangan mo at kung anong mga aksyon ang nais mong gawin ng iyong flow. Ang Copilot ay bumubuo ng isang flow batay sa iyong paglalarawan. Maaari mo nang i-customize ang flow upang matugunan ang iyong mga pangangailangan. Ang AI Copilot ay bumubuo at nagmumungkahi ng mga aksyon na kailangan mong gawin ang gawain na nais mong awtomatikong gawin. Titingnan natin kung ano ang mga flows at kung paano mo ito magagamit sa Power Automate sa leksyong ito sa susunod. Maaari mo nang i-customize ang mga aksyon upang matugunan ang iyong mga pangangailangan gamit ang AI Copilot assistant feature sa pamamagitan ng mga hakbang na pakikipag-usap. Ang tampok na ito ay readily available mula sa Power Automate home screen.

## Takdang-aralin: Pamahalaan ang mga assignment ng estudyante at mga invoice para sa aming startup, gamit ang Copilot

Ang aming startup ay nagbibigay ng mga online na kurso sa mga estudyante. Ang startup ay mabilis na lumago at ngayon ay nahihirapan na makasabay sa demand para sa mga kurso nito. Ang startup ay nag-hire sa iyo bilang isang Power Platform developer upang tulungan silang bumuo ng isang low code solution upang tulungan silang pamahalaan ang kanilang mga assignment ng estudyante at mga invoice. Ang kanilang solusyon ay dapat makatulong sa kanila na subaybayan at pamahalaan ang mga assignment ng estudyante sa pamamagitan ng isang app at awtomatikong maproseso ang invoice processing process sa pamamagitan ng isang workflow. Hiniling sa iyo na gamitin ang Generative AI upang bumuo ng solusyon.

Kapag nagsisimula ka sa paggamit ng Copilot, maaari mong gamitin ang [Power Platform Copilot Prompt Library](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) upang makapagsimula sa mga prompt. Ang library na ito ay naglalaman ng listahan ng mga prompt na maaari mong gamitin upang bumuo ng mga app at daloy sa Copilot. Maaari mo ring gamitin ang mga prompt sa library upang makakuha ng ideya kung paano ilarawan ang iyong mga pangangailangan sa Copilot.

### Bumuo ng isang Student Assignment Tracker App para sa Aming Startup

Ang mga guro sa aming startup ay nahihirapan na subaybayan ang mga assignment ng estudyante. Sila ay gumagamit ng isang spreadsheet upang subaybayan ang mga assignment ngunit ito ay naging mahirap na pamahalaan habang dumadami ang bilang ng mga estudyante. Hiniling nila sa iyo na bumuo ng isang app na tutulong sa kanila na subaybayan at pamahalaan ang mga assignment ng estudyante. Ang app ay dapat magbigay-daan sa kanila na magdagdag ng mga bagong assignment, tingnan ang mga assignment, i-update ang mga assignment at burahin ang mga assignment. Ang app ay dapat ding magbigay-daan sa mga guro at estudyante na tingnan ang mga assignment na na-grade at ang mga hindi pa na-grade.

Bubuuin mo ang app gamit ang Copilot sa Power Apps sa pamamagitan ng pagsunod sa mga hakbang sa ibaba:

1. Mag-navigate sa [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) home screen.

2. Gamitin ang text area sa home screen upang ilarawan ang app na nais mong buuin. Halimbawa, **_Nais kong bumuo ng isang app upang subaybayan at pamahalaan ang mga assignment ng estudyante_**. I-click ang **Send** button upang ipadala ang prompt sa AI Copilot.

3. Ang AI Copilot ay magmumungkahi ng isang Dataverse Table na may mga field na kailangan mo upang iimbak ang data na nais mong subaybayan at ilang sample data. Maaari mo nang i-customize ang table upang matugunan ang iyong mga pangangailangan gamit ang AI Copilot assistant feature sa pamamagitan ng mga hakbang na pakikipag-usap.

   > **Mahalaga**: Ang Dataverse ay ang ilalim na data platform para sa Power Platform. Ito ay isang low-code data platform para sa pag-iimbak ng data ng app. Ito ay isang fully managed service na ligtas na nag-iimbak ng data sa Microsoft Cloud at na-provision sa loob ng iyong Power Platform environment. Ito ay may kasamang built-in na data governance capabilities, tulad ng data classification, data lineage, fine-grained access control, at higit pa. Maaari kang matuto nang higit pa tungkol sa Dataverse [dito](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

4. Ang mga guro ay nais na magpadala ng mga email sa mga estudyante na nagsumite ng kanilang mga assignment upang panatilihin silang updated sa progreso ng kanilang mga assignment. Maaari mong gamitin ang Copilot upang magdagdag ng bagong field sa table upang iimbak ang student email. Halimbawa, maaari mong gamitin ang sumusunod na prompt upang magdagdag ng bagong field sa table: **_Nais kong magdagdag ng isang column upang iimbak ang student email_**. I-click ang **Send** button upang ipadala ang prompt sa AI Copilot.

5. Ang AI Copilot ay bubuo ng bagong field at maaari mo nang i-customize ang field upang matugunan ang iyong mga pangangailangan.

6. Kapag tapos ka na sa table, i-click ang **Create app** button upang bumuo ng app.

7. Ang AI Copilot ay bubuo ng isang responsive Canvas app batay sa iyong paglalarawan. Maaari mo nang i-customize ang app upang matugunan ang iyong mga pangangailangan.

8. Para sa mga guro na magpadala ng mga email sa mga estudyante, maaari mong gamitin ang Copilot upang magdagdag ng bagong screen sa app. Halimbawa, maaari mong gamitin ang sumusunod na prompt upang magdagdag ng bagong screen sa app: **_Nais kong magdagdag ng isang screen upang magpadala ng mga email sa mga estudyante_**. I-click ang **Send** button upang ipadala ang prompt sa AI Copilot.

9. Ang AI Copilot ay bubuo ng bagong screen at maaari mo nang i-customize ang screen upang matugunan ang iyong mga pangangailangan.

10. Kapag tapos ka na sa app, i-click ang **Save** button upang i-save ang app.

11. Upang ibahagi ang app sa mga guro, i-click ang **Share** button at pagkatapos ay i-click ang **Share** button muli. Maaari mong ibahagi ang app sa mga guro sa pamamagitan ng pagpasok ng kanilang mga email addresses.

> **Ang iyong takdang-aralin**: Ang app na iyong binuo ay isang magandang simula ngunit maaari pang pagandahin. Sa tampok na email, ang mga guro ay maaari lamang magpadala ng mga email sa mga estudyante nang manu-mano sa pamamagitan ng pag-type ng kanilang mga email. Maaari mo bang gamitin ang Copilot upang bumuo ng automation na magbibigay-daan sa mga guro na magpadala ng mga email sa mga estudyante nang awtomatiko kapag sila ay nagsumite ng kanilang mga assignment? Ang iyong hint ay sa tamang prompt maaari mong gamitin ang Copilot sa Power Automate upang bumuo nito.

### Bumuo ng isang Invoices Information Table para sa Aming Startup

Ang finance team ng aming startup ay nahihirapan na subaybayan ang mga invoice. Sila ay gumagamit ng isang spreadsheet upang subaybayan ang mga invoice ngunit ito ay naging mahirap na pamahalaan habang dumadami ang bilang ng mga invoice. Hiniling nila sa iyo na bumuo ng isang table na tutulong sa kanila na iimbak, subaybayan at pamahalaan ang impormasyon ng mga invoice na kanilang natatanggap. Ang table ay dapat gamitin upang bumuo ng automation na kukunin ang lahat ng impormasyon ng invoice at iimbak ito sa table. Ang table ay dapat ding magbigay-daan sa finance team na tingnan ang mga invoice na nabayaran na at ang mga hindi pa nababayaran.

Ang Power Platform ay may ilalim na data platform na tinatawag na Dataverse na nagbibigay-daan sa iyo na iimbak ang data para sa iyong mga app at solusyon. Ang Dataverse ay nagbibigay ng low-code data platform para sa pag-iimbak ng data ng app. Ito ay isang fully managed service na ligtas na nag-iimbak ng data sa Microsoft Cloud at na-provision sa loob ng iyong Power Platform environment. Ito ay may kasamang built-in na data governance capabilities, tulad ng data classification, data lineage, fine-grained access control, at higit pa. Maaari kang matuto nang higit pa [tungkol sa Dataverse dito](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Bakit natin dapat gamitin ang Dataverse para sa aming startup? Ang standard at custom tables sa loob ng Dataverse ay nagbibigay ng secure at cloud-based na storage option para sa iyong data. Ang mga tables ay nagbibigay-daan sa iyo na iimbak ang iba't ibang uri ng data, katulad ng kung paano mo maaaring gamitin ang maramihang worksheets sa isang Excel workbook. Maaari mong gamitin ang tables upang iimbak ang data na tiyak sa iyong organisasyon o pangangailangan ng negosyo. Ang ilan sa mga benepisyo na makukuha ng aming startup mula sa paggamit ng Dataverse ay kinabibilangan ngunit hindi limitado sa:

- **Madaling pamahalaan**: Ang parehong metadata at data ay nakaimbak sa cloud, kaya hindi mo kailangang mag-alala tungkol sa mga detalye kung paano sila iniimbak o pinamamahalaan. Maaari kang mag-focus sa pagbuo ng iyong mga app at solusyon.

- **Ligtas**: Ang Dataverse ay nagbibigay ng secure at cloud-based na storage option para sa iyong data. Maaari mong kontrolin kung sino ang may access sa data sa iyong mga tables at kung paano nila ito maa-access gamit ang role-based security.

- **Rich metadata**: Ang mga uri ng data at mga relasyon ay direktang ginagamit sa loob ng Power Apps

- **Logic at validation**: Maaari mong gamitin ang mga business rules, calculated fields, at validation rules upang ipatupad ang business logic at mapanatili ang data accuracy.

Ngayon na alam mo kung ano ang Dataverse at bakit mo ito dapat gamitin, tingnan natin kung paano mo magagamit ang Copilot upang lumikha ng isang table sa Dataverse upang matugunan ang mga pangangailangan ng aming finance team.

> **Tandaan**: Gagamitin mo ang table na ito sa susunod na seksyon upang bumuo ng automation na kukunin ang lahat ng impormasyon ng invoice at iimbak ito sa table.


isang teksto. - **Sentiment Analysis**: Ang modelong ito ay nakakatukoy ng positibo, negatibo, neutral, o halo-halong damdamin sa teksto. - **Business Card Reader**: Ang modelong ito ay kumukuha ng impormasyon mula sa mga business card. - **Text Recognition**: Ang modelong ito ay kumukuha ng teksto mula sa mga larawan. - **Object Detection**: Ang modelong ito ay nakakatukoy at kumukuha ng mga bagay mula sa mga larawan. - **Document processing**: Ang modelong ito ay kumukuha ng impormasyon mula sa mga form. - **Invoice Processing**: Ang modelong ito ay kumukuha ng impormasyon mula sa mga invoice. Sa pamamagitan ng Custom AI Models, maaari mong dalhin ang sarili mong modelo sa AI Builder upang ito ay gumana tulad ng anumang AI Builder custom model, na nagpapahintulot sa iyo na sanayin ang modelo gamit ang sarili mong data. Maaari mong gamitin ang mga modelong ito upang i-automate ang mga proseso at hulaan ang mga resulta sa parehong Power Apps at Power Automate. Kapag ginagamit ang sarili mong modelo, may mga limitasyon na dapat isaalang-alang. Basahin pa ang tungkol sa mga [limitasyon](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

## Assignment #2 - Gumawa ng Invoice Processing Flow para sa Aming Startup

Ang finance team ay nahihirapang magproseso ng mga invoice. Gumagamit sila ng spreadsheet upang subaybayan ang mga invoice ngunit ito ay nagiging mahirap pamahalaan habang dumadami ang bilang ng mga invoice. Hiningi nila na gumawa ka ng isang workflow na makakatulong sa kanila sa pagproseso ng mga invoice gamit ang AI. Ang workflow ay dapat magbigay-daan sa kanila na kumuha ng impormasyon mula sa mga invoice at i-store ang impormasyon sa isang Dataverse table. Ang workflow ay dapat din magbigay-daan sa kanila na magpadala ng email sa finance team kasama ang nakuhang impormasyon.

Ngayon na alam mo na kung ano ang AI Builder at kung bakit mo ito dapat gamitin, tingnan natin kung paano mo magagamit ang Invoice Processing AI Model sa AI Builder, na tinalakay natin kanina, upang gumawa ng workflow na makakatulong sa finance team sa pagproseso ng mga invoice. Upang makabuo ng workflow na makakatulong sa finance team sa pagproseso ng mga invoice gamit ang Invoice Processing AI Model sa AI Builder, sundin ang mga hakbang sa ibaba:

1. Pumunta sa [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst) home screen.
2. Gamitin ang text area sa home screen upang ilarawan ang workflow na nais mong buuin. Halimbawa, **_Proseso ng isang invoice kapag dumating ito sa aking mailbox_**. I-click ang **Send** button upang ipadala ang prompt sa AI Copilot.
3. Magmumungkahi ang AI Copilot ng mga aksyon na kailangan mong gawin para sa task na nais mong i-automate. Maaari mong i-click ang **Next** button upang dumaan sa susunod na mga hakbang.
4. Sa susunod na hakbang, hihilingin ng Power Automate na i-set up mo ang mga koneksyon na kinakailangan para sa flow. Kapag tapos ka na, i-click ang **Create flow** button upang lumikha ng flow.
5. Ang AI Copilot ay magbuo ng flow at maaari mo itong i-customize upang umayon sa iyong pangangailangan.
6. I-update ang trigger ng flow at itakda ang **Folder** sa folder kung saan itatago ang mga invoice. Halimbawa, maaari mong itakda ang folder sa **Inbox**. I-click ang **Show advanced options** at itakda ang **Only with Attachments** sa **Yes**. Ito ay titiyak na ang flow ay tatakbo lamang kapag may natanggap na email na may attachment sa folder.
7. Alisin ang sumusunod na mga aksyon mula sa flow: **HTML to text**, **Compose**, **Compose 2**, **Compose 3** at **Compose 4** dahil hindi mo ito gagamitin.
8. Alisin ang **Condition** action mula sa flow dahil hindi mo ito gagamitin. Dapat itong magmukha tulad ng sumusunod na screenshot:
9. I-click ang **Add an action** button at hanapin ang **Dataverse**. Piliin ang **Add a new row** action.
10. Sa **Extract Information from invoices** action, i-update ang **Invoice File** upang ituro sa **Attachment Content** mula sa email. Ito ay titiyak na ang flow ay kukunin ang impormasyon mula sa invoice attachment.
11. Piliin ang **Table** na ginawa mo kanina. Halimbawa, maaari mong piliin ang **Invoice Information** table. Piliin ang dynamic content mula sa nakaraang aksyon upang punan ang sumusunod na mga field:
   - ID
   - Amount
   - Date
   - Name
   - Status
   - Itakda ang **Status** sa **Pending**.
   - Supplier Email
   - Gamitin ang **From** dynamic content mula sa **When a new email arrives** trigger.
12. Kapag tapos ka na sa flow, i-click ang **Save** button upang i-save ang flow. Maaari mo na itong i-test sa pamamagitan ng pagpapadala ng email na may invoice sa folder na iyong tinukoy sa trigger.

> **Ang iyong takdang-aralin**: Ang flow na kakabuo mo lang ay isang magandang simula, ngayon kailangan mong mag-isip kung paano ka makakabuo ng isang automation na magpapahintulot sa aming finance team na magpadala ng email sa supplier upang i-update sila sa kasalukuyang status ng kanilang invoice. Ang iyong pahiwatig: ang flow ay dapat tumakbo kapag nagbago ang status ng invoice.

## Gumamit ng Text Generation AI Model sa Power Automate

Ang Create Text with GPT AI Model sa AI Builder ay nagbibigay-daan sa iyo na bumuo ng teksto base sa isang prompt at pinapagana ng Microsoft Azure OpenAI Service. Sa kakayahang ito, maaari mong isama ang GPT (Generative Pre-Trained Transformer) na teknolohiya sa iyong mga app at flow upang makabuo ng iba't ibang automated flow at insightful na mga aplikasyon.

Ang mga GPT model ay sumasailalim sa malawakang pagsasanay sa malaking dami ng data, na nagbibigay-daan sa kanila na makabuo ng teksto na kahawig ng wika ng tao kapag binigyan ng prompt. Kapag isinama sa workflow automation, ang mga AI model tulad ng GPT ay maaaring magamit upang pasimplehin at i-automate ang malawak na hanay ng mga gawain.

Halimbawa, maaari kang bumuo ng mga flow upang awtomatikong makabuo ng teksto para sa iba't ibang gamit, tulad ng: drafts ng emails, mga paglalarawan ng produkto, at iba pa. Maaari mo ring gamitin ang modelo upang bumuo ng teksto para sa iba't ibang app, tulad ng chatbots at customer service apps na nagpapahintulot sa mga customer service agent na tumugon ng epektibo at mahusay sa mga tanong ng customer.

Upang matutunan kung paano gamitin ang AI Model na ito sa Power Automate, dumaan sa [Add intelligence with AI Builder and GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko) module.

## Mahusay na Trabaho! Ipagpatuloy ang Iyong Pag-aaral

Matapos makumpleto ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang ipagpatuloy ang pagpapalawak ng iyong kaalaman sa Generative AI!

Pumunta sa Lesson 11 kung saan tatalakayin natin kung paano [integrate Generative AI with Function Calling](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI na serbisyo ng pagsasalin [Co-op Translator](https://github.com/Azure/co-op-translator). Habang kami ay nagsusumikap para sa katumpakan, mangyaring tandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga error o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ay dapat ituring na mapagkakatiwalaang pinagmulan. Para sa kritikal na impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot para sa anumang hindi pagkakaintindihan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.