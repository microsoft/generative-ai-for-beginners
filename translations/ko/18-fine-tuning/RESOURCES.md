# 자가 학습을 위한 자료

본 강의는 OpenAI와 Microsoft Foundry의 핵심 자료를 용어와 튜토리얼 참고용으로 사용하여 제작되었습니다. 아래는 자가 학습 여정을 위한 비포괄적 목록입니다. 모든 링크는 현재 지원되는 자료를 가리킵니다.

## 1. 주요 자료

| 제목/링크 | 설명 |
| :--- | :--- |
| [OpenAI 모델로 파인튜닝하기](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | 파인튜닝은 프롬프트에 들어가는 예시보다 훨씬 더 많은 예시로 학습을 진행하여 비용 절감, 응답 품질 향상, 그리고 낮은 지연 시간 요청을 가능하게 합니다. **OpenAI의 파인튜닝 개요를 확인하세요.** |
| [Microsoft Foundry 파인튜닝 사용 시기](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | **파인튜닝이란 무엇인지(개념)**, 왜 고려해야 하는지, 어떤 데이터를 사용하는지, 품질 측정 방법과 SFT, DPO, RFT 중 언제 적합한지 이해하세요. |
| [파인튜닝 모델 맞춤화하기](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | Microsoft Foundry에서 포털, OpenAI / Foundry Python SDK 또는 REST API를 사용하여 데이터 준비, 훈련, 체크포인트 및 배포 등 **파인튜닝의 전 과정을 배우세요.** |
| [연속 파인튜닝](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | 이미 파인튜닝된 모델을 기본 모델로 선택하여 새로운 훈련 예시 세트로 <strong>추가 파인튜닝하는 반복 과정</strong>입니다. |
| [툴(함수) 호출로 파인튜닝하기](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | 툴 호출 예시로 모델을 파인튜닝하면 더 정확하고 일관성 있으며 유사한 형식의 응답이 적은 프롬프트 토큰으로 가능해집니다. |
| [파인튜닝 모델: Microsoft Foundry 가이드](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | **어떤 모델들이 파인튜닝 가능한지**, 지원하는 방법들(SFT / DPO / RFT)과 제공 지역을 확인하세요. |
| [파인튜닝 개요: 기법과 방식](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | 세 가지 훈련 기법(SFT, DPO, RFT)과 두 가지 방식(서버리스 vs. 관리형 컴퓨팅)을 비교하고, 기본 모델 선택과 시작 방법에 대해 안내합니다. |
| <strong>튜토리얼</strong>: [Microsoft Foundry에서 모델 파인튜닝하기](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | 샘플 데이터셋 만들기, 파인튜닝 준비, `gpt-4.1-mini` 같은 현재 지원 모델로 파인튜닝 작업 실행, 그리고 파인튜닝된 모델을 Azure에 배포하기. |
| <strong>튜토리얼</strong>: [서버리스 API 배포와 함께 모델 파인튜닝하기](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | Microsoft Foundry에서 저코드 UI 기반 워크플로우를 이용해 Phi, Llama, Mistral 등 오픈 및 파트너 모델을 데이터셋에 맞게 맞춤화하세요. |
| <strong>튜토리얼</strong>: [Azure Databricks에서 Hugging Face 모델 파인튜닝하기](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | Azure Databricks와 Hugging Face Trainer로 `transformers` 라이브러리를 사용하여 단일 GPU에서 Hugging Face 모델 파인튜닝하기. |
| **교육 자료**: [Azure Machine Learning으로 기초 모델 파인튜닝하기](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | Azure ML 모델 카탈로그에서 파인튜닝 가능한 다수의 오픈 소스 모델 활용하기. [Azure ML 생성 AI 학습 경로](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst)의 일부입니다. |
| <strong>튜토리얼</strong>: [Weights & Biases와 함께하는 Azure OpenAI 파인튜닝](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | W&B로 Azure에서 파인튜닝 실행을 추적 및 분석하세요. OpenAI 파인튜닝 가이드에 Azure에 특화된 단계 및 실험 추적을 추가합니다. |

## 2. 부가 자료

이 섹션은 강의에서 다룰 시간이 없었던 추가로 탐색할 만한 자료들입니다. 이들을 사용해 해당 주제에 대한 본인의 전문 지식을 쌓으세요.

| 제목/링크 | 설명 |
| :--- | :--- |
| **OpenAI Cookbook**: [챗 모델 파인튜닝을 위한 데이터 준비 및 분석](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | 파인튜닝 전에 챗 데이터셋을 전처리하고 분석합니다: 형식 오류 확인, 기본 통계, 토큰 수 및 비용 추정. [OpenAI 파인튜닝 가이드](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst)와 함께 사용합니다. |
| **OpenAI Cookbook**: [Qdrant와 함께 Retrieval Augmented Generation (RAG) 파인튜닝](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | RAG용 OpenAI 모델 파인튜닝의 포괄적 예제. Qdrant와 Few-shot 학습 통합으로 성능 향상과 허위 생성 감소를 목표로 합니다. |
| **OpenAI Cookbook**: [Weights & Biases로 GPT 파인튜닝하기](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | W&B를 활용해 모델 훈련과 파인튜닝을 추적하세요. 먼저 [OpenAI 파인튜닝](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst) 가이드를 읽고 Cookbook 연습을 시도하세요. |
| **Hugging Face 튜토리얼**: [Hugging Face TRL로 LLM 파인튜닝하는 방법](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | Hugging Face TRL, Transformers, 데이터셋을 사용해 오픈 LLM을 파인튜닝합니다: 사용 사례 정의, 개발 환경 구성, 데이터셋 준비, 파인튜닝, 평가, 배포 순서입니다. |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | Hugging Face에서 제공하는 노코드/저코드 라이브러리로 다양한 모델 유형 파인튜닝. 자체 클라우드, Hugging Face Spaces 또는 로컬 GUI, CLI, YAML 설정으로 실행 가능. |
| **Unsloth**: [LLM 파인튜닝 가이드](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | 로컬 LLM 파인튜닝과 강화학습을 간소화하는 오픈소스 프레임워크로, 즉시 사용 가능한 [노트북](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst)을 제공합니다. |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->