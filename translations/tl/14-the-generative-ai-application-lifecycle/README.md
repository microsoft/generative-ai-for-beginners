[![Pagsasama sa function calling](../../../translated_images/tl/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Ang Siklo ng Buhay ng Generative AI Application

Isang mahalagang tanong para sa lahat ng AI applications ay ang kabuluhan ng mga AI features, dahil ang AI ay mabilis na umuunlad na larangan, upang matiyak na ang iyong aplikasyon ay nananatiling mahalaga, maaasahan, at matatag, kailangan mong patuloy na subaybayan, suriin, at pagbutihin ito. Dito pumapasok ang siklo ng buhay ng generative AI.

Ang siklo ng buhay ng generative AI ay isang balangkas na gumagabay sa iyo sa mga yugto ng pag-develop, pag-deploy, at pagpapanatili ng isang generative AI na aplikasyon. Tinutulungan ka nitong tukuyin ang iyong mga layunin, sukatin ang iyong pagganap, kilalanin ang iyong mga hamon, at ipatupad ang iyong mga solusyon. Tinutulungan ka rin nitong ihanay ang iyong aplikasyon sa mga etikal at legal na pamantayan ng iyong larangan at mga stakeholder. Sa pagsunod sa siklo ng buhay ng generative AI, masisiguro mong palaging nagbibigay ng halaga ang iyong aplikasyon at nasisiyahan ang iyong mga gumagamit.

## Panimula

Sa kabanatang ito, iyong:

- Mauunawaan ang Paradigm Shift mula MLOps patungo sa LLMOps
- Ang LLM Lifecycle
- Mga Kagamitan sa Siklo ng Buhay
- Pagsukat at Pagsusuri ng Siklo ng Buhay

## Mauunawaan ang Paradigm Shift mula MLOps patungo sa LLMOps

Ang LLMs ay bagong kagamitan sa arsenal ng Artificial Intelligence, napakalakas nila sa mga gawaing pagsusuri at paglikha para sa mga aplikasyon, ngunit ang lakas na ito ay may mga epekto sa kung paano natin pinapasimple ang AI at mga klasikong gawain sa Machine Learning.

Dahil dito, kailangan natin ng bagong Paradigm upang iakma ang kagamitang ito nang dinamiko, gamit ang tamang mga insentibo. Maaari nating ikategorya ang mga lumang AI app bilang "ML Apps" at ang mga bagong AI App bilang "GenAI Apps" o simpleng "AI Apps", na nagpapakita ng pangunahing teknolohiya at mga teknik na ginagamit noong panahon. Binabago nito ang ating naratibo sa maraming paraan, tingnan ang sumusunod na paghahambing.

![Paghahambing ng LLMOps vs. MLOps](../../../translated_images/tl/01-llmops-shift.29bc933cb3bb0080.webp)

Pansinin na sa LLMOps, mas nakatuon tayo sa mga App Developers, gamit ang mga integrations bilang pangunahing punto, gamit ang "Models-as-a-Service" at iniisip ang mga sumusunod na puntos para sa mga metric.

- Kalidad: Kalidad ng tugon
- Pinsala: Responsable na AI
- Katapatan: Pagkaka-groun ng tugon (May katuturan ba? Tama ba ito?)
- Gastos: Budget ng solusyon
- Latency: Karaniwang oras para sa tugon ng token

## Ang LLM Lifecycle

Una, upang maunawaan ang siklo ng buhay at mga pagbabago, pansinin ang sumusunod na infographic.

![LLMOps infographic](../../../translated_images/tl/02-llmops.70a942ead05a7645.webp)

Tulad ng napapansin, ito ay iba sa karaniwang Siklo ng Buhay sa MLOps. Ang LLMs ay may maraming bagong pangangailangan, tulad ng Prompting, iba’t ibang teknik upang mapabuti ang kalidad (Fine-Tuning, RAG, Meta-Prompts), iba’t ibang pagtatasa at responsibilidad sa responsable na AI, at sa huli, mga bagong metric sa pagsusuri (Kalidad, Pinsala, Katapatan, Gastos at Latency).

Halimbawa, tingnan kung paano tayo nag-iisip. Ginagamit ang prompt engineering upang subukan ang iba't ibang LLM upang tuklasin ang mga posibilidad kung tama ang kanilang hypothesis.

Tandaan na ito ay hindi linear, kundi magkakaugnay na mga loop, paulit-ulit at may pangkalahatang siklo.

Paano natin maaaring tuklasin ang mga hakbang na iyon? Tingnan natin nang detalyado kung paano tayo makakagawa ng siklo ng buhay.

![Workflow ng LLMOps](../../../translated_images/tl/03-llm-stage-flows.3a1e1c401235a6cf.webp)

Maaaring mukhang kumplikado ito, pero magpokus muna tayo sa tatlong malalaking hakbang.

1. Pag-iisip/Pagsisiyasat: Eksplorasyon, dito pwede tayong magsiyasat ayon sa pangangailangan ng negosyo. Pagbuo ng prototype, paggawa ng [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) at pagsubok kung sapat ito para sa ating hypothesis.
1. Pagbuo/Pagpapalawak: Pagpapatupad, ngayon, nagsisimula na tayong suriin para sa mas malalaking dataset gamit ang teknik tulad ng Fine-tuning at RAG, upang tuklasin ang tibay ng ating solusyon. Kung hindi ito gumana, ang muling pagpapatupad, pagdagdag ng mga hakbang sa flow o muling pagkaayos ng data ay maaaring makatulong. Pagkatapos ng pagsubok sa ating flow at sa ating sukat, kung ito ay gumagana at na-check ang ating mga metric, handa na ito para sa susunod na hakbang.
1. Pagpa-operationalize: Integrasyon, ngayong idinadagdag ang Monitoring at Alerts Systems sa ating sistema, deployment at application integration sa ating App.

Pagkatapos, mayroon tayong pangkalahatang siklo ng Pamamahala, na nakatuon sa seguridad, pagsunod at pamamahala.

Binabati kita, handa na ang iyong AI App na gumana at operational. Para sa isang hands-on na karanasan, tingnan ang [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)

Ngayon, anong mga kagamitan ang maaari nating gamitin?

## Mga Kagamitan sa Siklo ng Buhay

Para sa mga Kagamitan, ibinibigay ng Microsoft ang [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) at [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) upang gawing madali ang pagtupad ng iyong siklo at handa nang gamitin.

Ang [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst), ay nagbibigay-daan na gamitin ang [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst). Ang Microsoft Foundry (dating Azure AI Studio) ay isang web portal na nagpapahintulot sa iyo na mag-explore ng mga modelo, sample at mga kagamitan, pamahalaan ang iyong mga resources, at gumamit ng UI development flows pati na rin ang SDK/CLI options para sa Code-First development.

![Mga posibilidad ng Azure AI](../../../translated_images/tl/04-azure-ai-platform.80203baf03a12fa8.webp)

Pinapayagan ka ng Azure AI na gumamit ng maraming resources upang pamahalaan ang iyong operasyon, serbisyo, proyekto, vector search at mga pangangailangan sa database.

![LLMOps gamit ang Azure AI](../../../translated_images/tl/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

Gumawa mula Proof-of-Concept (POC) hanggang sa malalaking aplikasyon gamit ang PromptFlow:

- Magdisenyo at bumuo ng apps mula sa VS Code, gamit ang visual at functional tools
- Subukan at i-fine-tune ang iyong mga apps para sa kalidad na AI, nang madali.
- Gamitin ang Microsoft Foundry para sa Integrate at Iterate sa cloud, Push at Deploy para sa mabilisang integrasyon.

![LLMOps gamit ang PromptFlow](../../../translated_images/tl/06-llm-promptflow.a183eba07a3a7fdf.webp)

## Magaling! Ipagpatuloy ang iyong Pag-aaral!

Kamangha-mangha, ngayon alamin pa kung paano namin istrukturahin ang isang aplikasyon upang gamitin ang mga konsepto sa [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), upang tingnan kung paano idinadagdag ng Cloud Advocacy ang mga konseptong ito sa mga demonstrasyon. Para sa higit pang nilalaman, tingnan ang aming [Ignite breakout session!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Ngayon, tingnan ang Leksyon 15, upang maunawaan kung paano nakaapekto ang [Retrieval Augmented Generation at mga Vector Database](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) sa Generative AI at upang makagawa ng mas nakaka-engganyong Aplikasyon!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->