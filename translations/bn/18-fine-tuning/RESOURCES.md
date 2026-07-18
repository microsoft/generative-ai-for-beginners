# স্ব-নির্দেশিত শিক্ষার জন্য রিসোর্সসমূহ

এই পাঠ OpenAI এবং Microsoft Foundry থেকে কোর রিসোর্স ব্যবহার করে নির্মিত হয়েছে যা টার্মিনোলজি এবং টিউটোরিয়ালগুলোর রেফারেন্স হিসেবে ব্যবহৃত হয়েছে। এখানে আপনার নিজস্ব স্ব-নির্দেশিত শেখার যাত্রার জন্য একটি অপুর্ণ তালিকা রয়েছে। নিচের প্রতিটি লিংক বর্তমান, সমর্থিত উপকরণের দিকে নির্দেশ করে।

## ১. প্রাথমিক রিসোর্সসমূহ

| শিরোনাম/লিংক | বর্ণনা |
| :--- | :--- |
| [OpenAI মডেল দিয়ে ফাইন-টিউনিং](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | ফাইন-টিউনিং কম সংখ্যক শট শেখার উন্নতি করে যেহেতু এটি প্রশিক্ষণের জন্য অনেক বেশি উদাহরণ ব্যবহার করে যা প্রম্প্টে ফিট হয় না - খরচ সাশ্রয়, প্রতিক্রিয়ার গুণমান উন্নত করা এবং কম লেটেন্সি অনুরোধ সক্ষম করে। **OpenAI থেকে ফাইন-টিউনিং এর সারমর্ম পান।** |
| [কখন Microsoft Foundry ফাইন-টিউনিং ব্যবহার করবেন](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | **ফাইন-টিউনিং কী (ধারণা)**, কেন এটি বিবেচনা করবেন, কোন ডেটা ব্যবহার করবেন, এবং গুণমান কীভাবে মাপবেন তা বুঝুন - সাথে কখন SFT, DPO বা RFT সঠিক। |
| [ফাইন-টিউনিং সহ একটি মডেল কাস্টমাইজ করা](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | Microsoft Foundry তে ফাইন-টিউনিং-এর জন্য পোর্টাল, OpenAI / Foundry পাইথন SDK, বা REST API ব্যবহার করে সংকলিত প্রক্রিয়া - ডেটা প্রস্তুতি, প্রশিক্ষণ, চেকপয়েন্ট, এবং নিযুক্তিকরণ সহ। |
| [ক্রমাগত ফাইন-টিউনিং](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | ইতিমধ্যে ফাইন-টিউন করা মডেল থেকে বেস মডেল হিসেবে নির্বাচন করে নতুন প্রশিক্ষণ উদাহরণগুলিতে **অধিক ফাইন-টিউনিং করার** পুনরাবৃত্তিমূলক প্রক্রিয়া। |
| [টুল (ফাংশন) কলিং সহ ফাইন-টিউনিং](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | টুল কলিং উদাহরণ ব্যবহার করে আপনার মডেলকে ফাইন-টিউন করা আউটপুট উন্নত করে - আরো সঠিক, ধারাবাহিক, এবং সামঞ্জস্যপূর্ণ ফরম্যাটের প্রতিক্রিয়া কম প্রম্প্ট টোকেন ব্যবহার করে। |
| [ফাইন-টিউনিং মডেল: Microsoft Foundry নির্দেশিকা](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | **কোন মডেল ফাইন-টিউন করা যায়**, তারা কোন পদ্ধতি সমর্থন করে (SFT / DPO / RFT), এবং কোন অঞ্চলগুলোতে উপলব্ধ তা দেখুন। |
| [ফাইন-টিউনিং সারসংক্ষেপ: কৌশল এবং মাধ্যমসমূহ](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | তিনটি প্রশিক্ষণ কৌশল (SFT, DPO, RFT) এবং দুটি মাধ্যম (সার্ভারলেস বনাম ম্যানেজড কম্পিউট) তুলনা করুন, বেস মডেল নির্বাচন ও শুরু করার নির্দেশনা সহ। |
| **টিউটোরিয়াল**: [Microsoft Foundry তে একটি মডেল ফাইন-টিউন করুন](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | একটি নমুনা ডেটাসেট তৈরি করুন, ফাইন-টিউনিং জন্য প্রস্তুতি নিন, বর্তমানে সমর্থিত মডেল যেমন `gpt-4.1-mini` তে ফাইন-টিউনিং কাজ চালান, এবং Azure এ ফাইন-টিউন করা মডেলটি স্থাপন করুন। |
| **টিউটোরিয়াল**: [সার্ভারলেস API ডিপ্লয়মেন্ট সহ মডেল ফাইন-টিউন](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | Microsoft Foundry তে কম-কোড, UI-ভিত্তিক ওয়ার্কফ্লো ব্যবহার করে আপনার ডেটাসেটের জন্য খোলা এবং পার্টনার মডেল (Phi, Llama, Mistral ইত্যাদি) কাস্টমাইজ করুন। |
| **টিউটোরিয়াল**: [Azure Databricks এ Hugging Face মডেল ফাইন-টিউন](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | Azure Databricks এবং Hugging Face Trainer ব্যবহার করে একটি একক GPU তে `transformers` লাইব্রেরি সহ Hugging Face মডেল ফাইন-টিউন করুন। |
| **প্রশিক্ষণ**: [Azure Machine Learning দিয়ে ফাউন্ডেশন মডেল ফাইন-টিউন করুন](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | Azure Machine Learning মডেল ক্যাটালগে অনেক ওপেন সোর্স মডেল রয়েছে যা আপনি ফাইন-টিউন করতে পারবেন। এটি [Azure ML Generative AI Learning Path](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) এর অংশ। |
| **টিউটোরিয়াল**: [Weights & Biases সহ Azure OpenAI ফাইন-টিউনিং](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | W&B দিয়ে Azure তে ফাইন-টিউনিং রান ট্র্যাক এবং বিশ্লেষণ করুন। OpenAI ফাইন-টিউনিং গাইডকে Azure-নির্দিষ্ট ধাপ ও পরীক্ষা ট্র্যাকিং সহ সম্প্রসারিত করা হয়েছে। |

## ২. মাধ্যমিক রিসোর্সসমূহ

এই অংশে অতিরিক্ত রিসোর্স রয়েছে যা আমাদের পাঠে সময়ের অভাবে আলোচনা করা হয়নি। এগুলো ব্যবহার করে এই বিষয়ের উপর নিজের দক্ষতা গড়ে তুলুন।

| শিরোনাম/লিংক | বর্ণনা |
| :--- | :--- |
| **OpenAI কুকবুক**: [চ্যাট মডেল ফাইন-টিউনিং এর জন্য ডেটা প্রস্তুতি এবং বিশ্লেষণ](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | ফাইন-টিউনিং এর আগে একটি চ্যাট ডেটাসেট প্রিপ্রসেস ও বিশ্লেষণ করুন: ফরম্যাট ত্রুটি পরীক্ষা করুন, মৌলিক পরিসংখ্যান পান, এবং টোকেন গণনা (ও খরচ) অনুমান করুন। [OpenAI ফাইন-টিউনিং গাইড](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) এর সাথে জোড়া। |
| **OpenAI কুকবুক**: [Qdrant এর সাথে Retrieval Augmented Generation (RAG) জন্য ফাইন-টিউনিং](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | OpenAI মডেলগুলোর জন্য RAG ফাইন-টিউনিং এর একটি ব্যাপক উদাহরণ, Qdrant এবং কম শট শেখার সমন্বয়ে কর্মক্ষমতা বাড়িয়ে এবং মিথ্যা তথ্য কমিয়ে। |
| **OpenAI কুকবুক**: [Weights & Biases ব্যবহার করে GPT ফাইন-টিউনিং](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | মডেল প্রশিক্ষণ ও ফাইন-টিউনিং ট্র্যাক করতে W&B ব্যবহার করুন। প্রথমে তাদের [OpenAI ফাইন-টিউনিং](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst) গাইড পড়ুন, তারপর কুকবুক অনুশীলন করুন। |
| **Hugging Face টিউটোরিয়াল**: [Hugging Face TRL দিয়ে কিভাবে LLM ফাইন-টিউন করবেন](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | Hugging Face TRL, Transformers, এবং ডেটাসেট ব্যবহার করে খোলা LLM ফাইন-টিউন করুন: একটি ব্যবহারের কেস সংজ্ঞায়িত করুন, ডেভ পরিবেশ সেটআপ করুন, ডেটাসেট প্রস্তুত করুন, ফাইন-টিউন করুন, মূল্যায়ন করুন, এবং নিযুক্ত করুন। |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | Hugging Face থেকে একটি নো-কোড / লো-কোড লাইব্রেরি যা অনেক ধরণের মডেল ফাইন-টিউন করার জন্য। এটি নিজস্ব ক্লাউডে, Hugging Face Spaces এ, অথবা GUI, CLI, বা YAML কনফিগারেশন দ্বারা লোকালেও চালাতে পারেন। |
| **Unsloth**: [LLM ফাইন-টিউনিং গাইড](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | একটি ওপেন-সোর্স ফ্রেমওয়ার্ক যা স্থানীয় LLM ফাইন-টিউনিং এবং রিইনফোর্সমেন্ট লার্নিং সহজ করে তোলে, প্রস্তুত ব্যবহারযোগ্য [নোটবুক](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) সহ। |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->