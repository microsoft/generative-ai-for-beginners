<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df44972d5575ea8cef3c52ee31696d04",
  "translation_date": "2025-12-19T16:22:52+00:00",
  "source_file": "14-the-generative-ai-application-lifecycle/README.md",
  "language_code": "tl"
}
-->
[![Integrating with function calling](../../../translated_images/14-lesson-banner.066d74a31727ac12.tl.png)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Ang Siklo ng Buhay ng Generative AI Application

Isang mahalagang tanong para sa lahat ng AI application ay ang kaugnayan ng mga tampok ng AI, dahil ang AI ay isang mabilis na umuunlad na larangan, upang matiyak na ang iyong aplikasyon ay nananatiling may kaugnayan, maaasahan, at matatag, kailangan mong subaybayan, suriin, at pagbutihin ito nang tuloy-tuloy. Dito pumapasok ang siklo ng buhay ng generative AI.

Ang siklo ng buhay ng generative AI ay isang balangkas na gumagabay sa iyo sa mga yugto ng pagbuo, pag-deploy, at pagpapanatili ng isang generative AI application. Tinutulungan ka nitong tukuyin ang iyong mga layunin, sukatin ang iyong pagganap, tuklasin ang iyong mga hamon, at ipatupad ang iyong mga solusyon. Tinutulungan ka rin nitong iayon ang iyong aplikasyon sa mga etikal at legal na pamantayan ng iyong larangan at mga stakeholder. Sa pagsunod sa siklo ng buhay ng generative AI, masisiguro mong ang iyong aplikasyon ay palaging nagbibigay ng halaga at nasisiyahan ang iyong mga gumagamit.

## Panimula

Sa kabanatang ito, matututuhan mo:

- Maunawaan ang Paradigm Shift mula sa MLOps patungong LLMOps
- Ang Siklo ng Buhay ng LLM
- Mga Kasangkapan sa Siklo ng Buhay
- Metripikasyon at Pagsusuri ng Siklo ng Buhay

## Maunawaan ang Paradigm Shift mula sa MLOps patungong LLMOps

Ang mga LLM ay isang bagong kasangkapan sa arsenal ng Artificial Intelligence, napakalakas nila sa mga gawain ng pagsusuri at paglikha para sa mga aplikasyon, ngunit ang kapangyarihang ito ay may ilang mga kahihinatnan sa kung paano natin pinapasimple ang mga gawain ng AI at Classic Machine Learning.

Dahil dito, kailangan natin ng bagong Paradigm upang iakma ang kasangkapang ito sa isang dinamiko, na may tamang mga insentibo. Maaari nating ikategorya ang mga lumang AI app bilang "ML Apps" at ang mga bagong AI Apps bilang "GenAI Apps" o simpleng "AI Apps", na sumasalamin sa pangunahing teknolohiya at mga teknik na ginamit sa panahon. Binabago nito ang ating kwento sa maraming paraan, tingnan ang sumusunod na paghahambing.

![LLMOps vs. MLOps comparison](../../../translated_images/01-llmops-shift.29bc933cb3bb0080.tl.png)

Pansinin na sa LLMOps, mas nakatuon tayo sa mga App Developer, gamit ang mga integrasyon bilang isang mahalagang punto, gamit ang "Models-as-a-Service" at iniisip ang mga sumusunod na punto para sa mga metriko.

- Kalidad: Kalidad ng tugon
- Pinsala: Responsable na AI
- Katapatan: Pagsang-ayon ng tugon (May katuturan ba? Tama ba ito?)
- Gastos: Badyet ng Solusyon
- Latency: Karaniwang oras para sa tugon ng token

## Ang Siklo ng Buhay ng LLM

Una, upang maunawaan ang siklo ng buhay at ang mga pagbabago, tandaan ang sumusunod na infographic.

![LLMOps infographic](../../../translated_images/02-llmops.70a942ead05a7645.tl.png)

Tulad ng mapapansin mo, ito ay iba sa karaniwang Siklo ng Buhay mula sa MLOps. Ang mga LLM ay may maraming bagong pangangailangan, tulad ng Prompting, iba't ibang teknik upang mapabuti ang kalidad (Fine-Tuning, RAG, Meta-Prompts), iba't ibang pagtatasa at responsibilidad sa responsable na AI, at sa huli, mga bagong metriko ng pagsusuri (Kalidad, Pinsala, Katapatan, Gastos at Latency).

Halimbawa, tingnan kung paano tayo nag-iideya. Gamit ang prompt engineering upang subukan ang iba't ibang LLM upang tuklasin ang mga posibilidad at subukan kung ang kanilang Hypothesis ay maaaring tama.

Tandaan na ito ay hindi linear, kundi mga integrated loops, paulit-ulit at may isang malawak na siklo.

Paano natin maaaring tuklasin ang mga hakbang na iyon? Tingnan natin nang detalyado kung paano tayo makakabuo ng isang siklo ng buhay.

![LLMOps Workflow](../../../translated_images/03-llm-stage-flows.3a1e1c401235a6cf.tl.png)

Maaaring medyo kumplikado ito, magpokus muna tayo sa tatlong malalaking hakbang.

1. Ideating/Exploring: Pagsisiyasat, dito maaari tayong mag-explore ayon sa pangangailangan ng ating negosyo. Prototyping, paggawa ng isang [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) at subukan kung ito ay sapat na epektibo para sa ating Hypothesis.
1. Building/Augmenting: Pagpapatupad, ngayon, sinisimulan nating suriin para sa mas malalaking dataset ang pagpapatupad ng mga teknik, tulad ng Fine-tuning at RAG, upang suriin ang katatagan ng ating solusyon. Kung hindi ito gumana, ang muling pagpapatupad nito, pagdaragdag ng mga bagong hakbang sa ating daloy o muling pag-aayos ng data, ay maaaring makatulong. Pagkatapos subukan ang ating daloy at sukat, kung ito ay gumagana at suriin ang ating mga Metriko, handa na ito para sa susunod na hakbang.
1. Operationalizing: Integrasyon, ngayon ay nagdaragdag ng Monitoring at Alerts Systems sa ating sistema, deployment at integrasyon ng aplikasyon sa ating Application.

Pagkatapos, mayroon tayong malawak na siklo ng Pamamahala, na nakatuon sa seguridad, pagsunod at pamamahala.

Binabati kita, handa na ang iyong AI App para gamitin at maging operational. Para sa isang hands-on na karanasan, tingnan ang [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

Ngayon, anong mga kasangkapan ang maaari nating gamitin?

## Mga Kasangkapan sa Siklo ng Buhay

Para sa mga kasangkapan, nagbibigay ang Microsoft ng [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) at [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) na nagpapadali at ginagawang madali ang iyong siklo na ipatupad at handa nang gamitin.

Ang [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys), ay nagpapahintulot sa iyo na gamitin ang [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys). Ang AI Studio ay isang web portal na nagpapahintulot sa iyo na tuklasin ang mga modelo, mga halimbawa at mga kasangkapan. Pamahalaan ang iyong mga resources, UI development flows at mga opsyon ng SDK/CLI para sa Code-First development.

![Azure AI possibilities](../../../translated_images/04-azure-ai-platform.80203baf03a12fa8.tl.png)

Pinapayagan ka ng Azure AI na gamitin ang maraming resources, upang pamahalaan ang iyong mga operasyon, serbisyo, proyekto, vector search at mga pangangailangan sa database.

![LLMOps with Azure AI](../../../translated_images/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.tl.png)

Bumuo, mula sa Proof-of-Concept(POC) hanggang sa malakihang aplikasyon gamit ang PromptFlow:

- Disenyo at Bumuo ng mga app mula sa VS Code, gamit ang mga visual at functional na kasangkapan
- Subukan at i-fine-tune ang iyong mga app para sa kalidad ng AI, nang madali.
- Gamitin ang Azure AI Studio upang Integrate at Ulitin gamit ang cloud, Push at Deploy para sa mabilis na integrasyon.

![LLMOps with PromptFlow](../../../translated_images/06-llm-promptflow.a183eba07a3a7fdf.tl.png)

## Mahusay! Ipagpatuloy ang Iyong Pag-aaral!

Kahanga-hanga, ngayon alamin pa kung paano natin istruktura ang isang aplikasyon upang gamitin ang mga konsepto sa [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), upang makita kung paano idinadagdag ng Cloud Advocacy ang mga konseptong iyon sa mga demonstrasyon. Para sa karagdagang nilalaman, tingnan ang aming [Ignite breakout session!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Ngayon, tingnan ang Lesson 15, upang maunawaan kung paano nakakaapekto ang [Retrieval Augmented Generation and Vector Databases](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) sa Generative AI at upang makagawa ng mas nakakaengganyong mga Aplikasyon!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paalala**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->