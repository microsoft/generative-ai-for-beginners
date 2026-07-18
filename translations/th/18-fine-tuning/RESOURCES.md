# แหล่งข้อมูลสำหรับการเรียนรู้ด้วยตนเอง

บทเรียนนี้สร้างขึ้นโดยใช้แหล่งข้อมูลหลักจาก OpenAI และ Microsoft Foundry เป็นเอกสารอ้างอิงสำหรับคำศัพท์และบทแนะนำ ด้านล่างนี้คือรายชื่อที่ไม่ครบถ้วนสำหรับการเรียนรู้ด้วยตนเองของคุณ ลิงก์ทั้งหมดด้านล่างชี้ไปยังเนื้อหาที่ปัจจุบันและได้รับการสนับสนุน

## 1. แหล่งข้อมูลหลัก

| ชื่อ/ลิงก์ | คำอธิบาย |
| :--- | :--- |
| [การปรับแต่งแบบละเอียดด้วยโมเดลของ OpenAI](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | การปรับแต่งแบบละเอียดช่วยปรับปรุงการเรียนรู้แบบ few-shot โดยการฝึกอบรมกับตัวอย่างจำนวนมากกว่าที่จะใส่ใน prompt ได้ - ช่วยประหยัดต้นทุน ปรับปรุงคุณภาพของคำตอบ และช่วยให้คำขอมีความหน่วงต่ำลง **ดูภาพรวมของการปรับแต่งแบบละเอียดจาก OpenAI** |
| [เวลาใช้การปรับแต่งแบบละเอียดของ Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | เข้าใจ **ว่า fine-tuning คืออะไร (แนวคิด)** ทำไมคุณควรพิจารณา ใช้ข้อมูลอะไร และวิธีวัดคุณภาพ - รวมถึงเมื่อไรที่ SFT, DPO หรือ RFT เหมาะสม |
| [ปรับแต่งโมเดลด้วยการปรับแต่งแบบละเอียด](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | ขั้นตอนเริ่มต้นถึงจบ **วิธีการ (process)** สำหรับการปรับแต่งแบบละเอียดใน Microsoft Foundry ผ่านพอร์ทัล, OpenAI / Foundry Python SDK หรือ REST API - ครอบคลุมการเตรียมข้อมูล, การฝึก, การบันทึกสถานะ และการใช้งาน |
| [การปรับแต่งแบบต่อเนื่อง](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | กระบวนการแบบวนรอบในการเลือกโมเดลที่ปรับแต่งแล้วมาเป็นโมเดลฐานและ **ปรับแต่งเพิ่มเติม** กับชุดตัวอย่างการฝึกอบรมใหม่ |
| [การปรับแต่งแบบละเอียดด้วยการเรียกเครื่องมือ (function)](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | การปรับแต่งโมเดลของคุณ **ด้วยตัวอย่างการเรียกใช้เครื่องมือ** ช่วยปรับปรุงผลลัพธ์ - ให้คำตอบที่แม่นยำ สม่ำเสมอ และมีรูปแบบคล้ายกันโดยใช้ prompt tokens น้อยลง |
| [การปรับแต่งโมเดล: แนวทาง Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | ตรวจสอบ **ว่าโมเดลใดสามารถปรับแต่งได้**, วิธีที่รองรับ (SFT / DPO / RFT), และภูมิภาคที่มีให้บริการ |
| [ภาพรวมการปรับแต่งแบบละเอียด: เทคนิคและรูปแบบ](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | เปรียบเทียบเทคนิคการฝึกสามแบบ (SFT, DPO, RFT) และรูปแบบสองแบบ (serverless กับ managed compute) พร้อมคำแนะนำการเลือกโมเดลฐานและเริ่มต้นใช้งาน |
| **บทช่วยสอน**: [ปรับแต่งโมเดลใน Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | สร้างชุดข้อมูลตัวอย่าง เตรียมความพร้อมสำหรับการปรับแต่งแบบละเอียด เรียกใช้งานงานปรับแต่งโมเดลที่ได้รับการสนับสนุนอย่าง `gpt-4.1-mini` และนำโมเดลที่ปรับแต่งแล้วไปใช้งานบน Azure |
| **บทช่วยสอน**: [ปรับแต่งโมเดลด้วยการปรับใช้ API แบบ serverless](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | ปรับแต่งโมเดลเปิดและพันธมิตร (Phi, Llama, Mistral และอื่น ๆ) ให้เหมาะสมกับชุดข้อมูลของคุณ _โดยใช้กระบวนการทำงานแบบ low-code และ UI ใน Microsoft Foundry_ |
| **บทช่วยสอน**: [ปรับแต่งโมเดล Hugging Face บน Azure Databricks](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | ปรับแต่งโมเดล Hugging Face ด้วยไลบรารี `transformers` บน GPU เดียว โดยใช้ Azure Databricks และ Hugging Face Trainer |
| **การฝึกอบรม**: [ปรับแต่งโมเดลฐานด้วย Azure Machine Learning](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | แคตตาล็อกโมเดลของ Azure Machine Learning มีโมเดลโอเพนซอร์สมากมายที่คุณสามารถปรับแต่งได้ เป็นส่วนหนึ่งของ [เส้นทางการเรียนรู้ Azure ML Generative AI](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) |
| **บทช่วยสอน**: [การปรับแต่งแบบละเอียด Azure OpenAI ด้วย Weights & Biases](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | ติดตามและวิเคราะห์การปรับแต่งแบบละเอียดบน Azure ด้วย W&B ขยายคำแนะนำการปรับแต่งของ OpenAI ด้วยขั้นตอนเฉพาะ Azure และการติดตามการทดลอง |

## 2. แหล่งข้อมูลรอง

ส่วนนี้รวบรวมแหล่งข้อมูลเพิ่มเติมที่น่าสนใจซึ่งเราไม่มีเวลาครอบคลุมในบทเรียน ใช้ข้อมูลเหล่านี้เพื่อสร้างความเชี่ยวชาญของคุณเองในหัวข้อนี้

| ชื่อ/ลิงก์ | คำอธิบาย |
| :--- | :--- |
| **OpenAI Cookbook**: [การเตรียมและวิเคราะห์ข้อมูลสำหรับการปรับแต่งโมเดล chat](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | เตรียมและวิเคราะห์ชุดข้อมูล chat ก่อนการปรับแต่ง: ตรวจสอบข้อผิดพลาดรูปแบบ, รับสถิติพื้นฐาน และประเมินจำนวนโทเคน (และค่าใช้จ่าย) คู่กับ [คำแนะนำการปรับแต่ง OpenAI](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) |
| **OpenAI Cookbook**: [การปรับแต่งสำหรับ Retrieval Augmented Generation (RAG) กับ Qdrant](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | ตัวอย่างครบถ้วนของการปรับแต่งโมเดล OpenAI สำหรับ RAG ผสาน Qdrant และ few-shot learning เพื่อเพิ่มประสิทธิภาพและลดการสร้างข้อมูลผิดพลาด |
| **OpenAI Cookbook**: [การปรับแต่ง GPT ด้วย Weights & Biases](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | ใช้ W&B เพื่อติดตามการฝึกและการปรับแต่งโมเดล อ่านคำแนะนำ [OpenAI Fine-Tuning](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst) ก่อน แล้วลองแบบฝึกหัด Cookbook |
| **บทช่วยสอน Hugging Face**: [วิธีปรับแต่ง LLMs ด้วย Hugging Face TRL](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | ปรับแต่ง LLMs แบบเปิดโดยใช้ Hugging Face TRL, Transformers และ datasets: กำหนดกรณีใช้งาน, ตั้งค่าสภาพแวดล้อมการพัฒนา, เตรียมชุดข้อมูล, ปรับแต่ง, ประเมินผล และใช้งาน |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | ไลบรารี no-code / low-code จาก Hugging Face สำหรับการปรับแต่งโมเดลหลายประเภท ใช้งานได้ในคลาวด์ของคุณเอง, บน Hugging Face Spaces หรือในเครื่องผ่าน GUI, CLI หรือ YAML config |
| **Unsloth**: [คู่มือการปรับแต่ง LLMs](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | เฟรมเวิร์คโอเพนซอร์สที่ช่วยให้การปรับแต่ง LLMs ในเครื่องและการเรียนรู้เสริมทำได้ง่ายขึ้น พร้อมมี [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) ที่พร้อมใช้ |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->