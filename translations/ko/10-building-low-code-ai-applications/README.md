# 로우 코드 AI 애플리케이션 구축

[![로우 코드 AI 애플리케이션 구축](../../../translated_images/ko/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(위 이미지를 클릭하여 이 수업의 비디오를 보세요)_

## 소개

이제 이미지 생성 애플리케이션을 구축하는 방법을 배웠으니, 로우 코드에 대해 이야기해 봅시다. 생성 AI는 로우 코드를 포함한 다양한 영역에 사용될 수 있지만, 로우 코드란 무엇이며 어떻게 AI를 추가할 수 있을까요?

로우 코드 개발 플랫폼을 사용함으로써 전통적인 개발자와 비개발자 모두가 앱과 솔루션을 더 쉽게 구축할 수 있게 되었습니다. 로우 코드 개발 플랫폼은 거의 또는 전혀 코딩 없이 앱과 솔루션을 구축할 수 있게 해줍니다. 이는 드래그 앤 드롭 방식으로 구성 요소를 조립해 앱과 솔루션을 구축할 수 있는 시각적 개발 환경을 제공함으로써 실현됩니다. 이로 인해 더 적은 자원으로 빠르게 앱과 솔루션을 구축할 수 있습니다. 이번 수업에서는 로우 코드 사용법과 Power Platform을 사용해 AI로 로우 코드 개발을 향상시키는 방법을 심도 있게 살펴봅니다.

Power Platform은 조직에 팀이 직관적인 로우 코드 또는 노 코드 환경을 통해 스스로 솔루션을 구축할 수 있는 기회를 제공합니다. 이 환경은 솔루션 구축 과정을 단순화합니다. Power Platform을 이용하면 솔루션을 몇 달이 아니라 며칠 또는 몇 주 만에 구축할 수 있습니다. Power Platform은 Power Apps, Power Automate, Power BI, Power Pages, Copilot Studio의 다섯 가지 핵심 제품으로 구성됩니다.

이번 수업에서 다룰 내용은 다음과 같습니다:

- Power Platform에서의 생성 AI 소개
- Copilot 소개 및 사용법
- Power Platform에서 생성 AI를 사용해 앱과 플로우 구축하기
- AI Builder를 통한 Power Platform의 AI 모델 이해
- Microsoft Copilot Studio로 지능형 에이전트 구축하기

## 학습 목표

이 수업을 마치면 다음을 할 수 있습니다:

- Power Platform에서 Copilot이 어떻게 작동하는지 이해하기

- 교육 스타트업을 위한 학생 과제 추적기 앱 구축하기

- AI를 이용해 송장 정보 추출을 자동화하는 송장 처리 플로우 구축하기

- GPT AI 모델인 Create Text 사용 시 모범 사례 적용하기

- Microsoft Copilot Studio가 무엇인지 이해하고 지능형 에이전트 구축 방법 익히기

이번 수업에서 사용할 도구와 기술은 다음과 같습니다:

- **Power Apps**: 학생 과제 추적기 앱을 위한 로우 코드 개발 환경 제공, 데이터를 추적, 관리, 상호작용하는 앱 구축

- **Dataverse**: 학생 과제 추적기 앱의 데이터를 저장하기 위한 로우 코드 데이터 플랫폼 제공

- **Power Automate**: 송장 처리 플로우를 위한 로우 코드 워크플로우 개발 환경 제공

- **AI Builder**: 송장 처리를 위해 사전 구축된 AI 모델 사용

## Power Platform에서의 생성 AI

로우 코드 개발과 애플리케이션에 생성 AI를 접목하는 것은 Power Platform의 주요 집중 영역입니다. 목표는 모든 사람이 데이터 과학 전문 지식 없이도 AI 기반 앱, 사이트, 대시보드 구축과 AI를 이용한 프로세스 자동화를 할 수 있도록 하는 것입니다. 이 목표는 Copilot과 AI Builder 형태로 Power Platform의 로우 코드 개발 환경에 생성 AI를 통합해 달성됩니다.

### 어떻게 작동하나요?

Copilot은 자연어를 사용한 대화형 단계를 통해 요구사항을 설명하면 Power Platform 솔루션을 구축하는 AI 조수입니다. 예를 들어 AI 조수에게 앱에서 사용할 필드를 알려주면, 앱과 기반 데이터 모델을 모두 생성하거나 Power Automate에서 플로우 설정 방법을 지정할 수 있습니다.

Copilot 기반 기능을 앱 화면 내의 기능으로 사용하여 사용자들이 대화형 상호작용을 통해 인사이트를 얻도록 할 수 있습니다.

AI Builder는 Power Platform에서 사용할 수 있는 로우 코드 AI 기능으로, AI 모델을 사용해 프로세스를 자동화하고 결과를 예측하게 도와줍니다. AI Builder를 통해 Dataverse나 SharePoint, OneDrive, Azure 등 다양한 클라우드 데이터 소스와 연결된 앱과 플로우에 AI를 적용할 수 있습니다.

Copilot은 Power Apps, Power Automate, Power BI, Power Pages, Copilot Studio(구 Power Virtual Agents) 등 모든 Power Platform 제품에서 제공됩니다. AI Builder는 Power Apps와 Power Automate에서 사용할 수 있습니다. 이번 수업에서는 교육 스타트업용 솔루션 구축을 위해 Power Apps와 Power Automate에서 Copilot과 AI Builder 사용법에 집중합니다.

### Power Apps에서의 Copilot

Power Platform의 일부로서 Power Apps는 데이터를 추적, 관리, 상호작용하기 위한 앱을 구축할 수 있는 로우 코드 개발 환경을 제공합니다. 이는 확장 가능한 데이터 플랫폼과 클라우드 서비스 및 온프레미스 데이터에 연결할 수 있는 기능을 갖춘 앱 개발 서비스 모음입니다. Power Apps를 통해 웹 브라우저, 태블릿, 휴대폰에서 실행되는 앱을 구축하고 동료와 공유할 수 있습니다. 단순한 인터페이스로 모든 비즈니스 사용자나 전문 개발자가 맞춤형 앱을 쉽게 개발할 수 있도록 합니다. Copilot을 통한 생성 AI로 앱 개발 경험이 더욱 향상됩니다.

Power Apps의 Copilot AI 조수 기능은 필요한 앱의 종류와 추적, 수집, 표시할 정보에 대해 설명하면, 그 설명을 바탕으로 반응형 Canvas 앱을 생성합니다. 이후 필요에 맞게 앱을 맞춤 설정할 수 있습니다. AI Copilot은 데이터를 저장할 필드와 일부 샘플 데이터를 포함한 Dataverse 테이블도 생성하고 제안합니다. 이번 수업의 나중 부분에서 Dataverse가 무엇이며 Power Apps에서 어떻게 사용하는지 살펴봅니다. 이후 대화형 단계를 통해 AI Copilot 조수 기능으로 테이블을 필요에 맞게 맞춤설정할 수 있습니다. 이 기능은 Power Apps 홈 화면에서 바로 이용 가능합니다.

### Power Automate에서의 Copilot

Power Platform의 일부인 Power Automate는 사용자들이 애플리케이션과 서비스 간 자동화된 워크플로우를 만들 수 있도록 합니다. 이는 의사소통, 데이터 수집, 승인 결정과 같은 반복적인 업무 프로세스를 자동화하는 데 도움을 줍니다. 간단한 인터페이스로 초보자부터 숙련 개발자까지 모든 기술 수준의 사용자가 작업을 자동화할 수 있습니다. 생성 AI를 통한 Copilot으로 워크플로우 개발 경험이 향상됩니다.

Power Automate의 Copilot AI 조수 기능은 필요한 플로우의 종류와 수행할 작업을 설명하면 그 설명을 바탕으로 플로우를 생성합니다. 이후 필요에 맞게 플로우를 맞춤 설정할 수 있습니다. AI Copilot은 자동화하려는 작업을 수행할 데 필요한 작업도 생성 및 제안합니다. 이번 수업의 나중 부분에서 플로우가 무엇이며 Power Automate에서 어떻게 사용하는지 살펴봅니다. 대화형 단계를 통해 AI Copilot 조수 기능으로 작업을 맞춤 설정할 수 있습니다. 이 기능은 Power Automate 홈 화면에서 바로 이용 가능합니다.

## Microsoft Copilot Studio로 지능형 에이전트 구축하기

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst)(구 Power Virtual Agents)는 Power Platform의 로우 코드 멤버로, **AI 에이전트** — 질문에 답하고, 조치를 취하며, 사용자 대신 작업을 자동화하는 대화형 코파일럿 — 를 구축할 수 있습니다. Power Platform의 다른 구성원들과 마찬가지로, 시각적이고 자연어 중심의 경험으로 에이전트를 구축합니다: 에이전트가 할 일을 설명하면, Copilot Studio가 명령, 지식, 작업을 스캐폴딩하는 데 도움을 줍니다.

교육 스타트업에서는, 학생들의 코스 관련 질문에 답변하거나, 과제 마감일을 확인하고, 심지어 강사에게 이메일을 보내는 에이전트를 코드 작성 없이 구축할 수 있습니다.

Copilot Studio를 강력하게 만드는 최신 기능 몇 가지는 다음과 같습니다:

- **지식 기반의 생성 답변**. 모든 대화를 직접 작성하는 대신, 공개 웹사이트, SharePoint, OneDrive, Dataverse, 업로드된 파일, 혹은 커넥터를 통한 기업 데이터와 같은 <strong>지식 소스</strong>를 연결해, 그로부터 근거가 있는 답변을 생성합니다.

- **생성식 오케스트레이션**. 엄격한 트리거 구문에 의존하는 대신, AI가 요청을 이해하고 결합할 지식, 주제, 작업을 동적으로 결정하여 여러 단계를 연결해 완수합니다.

- **작업과 커넥터**. 에이전트는 단순히 대화만 하는 게 아니라 <em>작업</em>을 수행할 수 있습니다. 1,500개 이상의 사전 구축된 Power Platform 커넥터, Power Automate 플로우, 맞춤 REST API, 프롬프트, 또는 **Model Context Protocol (MCP)** 서버에 기반한 작업을 에이전트에 제공할 수 있습니다.

- **자율 에이전트**. 에이전트는 채팅 창에서만 반응하지 않습니다. 새 이메일, Dataverse의 새 레코드, 파일 업로드 등 이벤트에 의해 자동으로 작동해 백그라운드에서 작업을 완료하는 <strong>자율 에이전트</strong>를 구축할 수 있습니다.

- **다중 에이전트 오케스트레이션**. 에이전트는 다른 에이전트를 호출할 수 있습니다. Copilot Studio 에이전트는 Microsoft 365 Copilot에 게시된 에이전트, Microsoft Foundry에서 구축된 에이전트를 포함한 다른 에이전트에게 넘기거나 확장될 수 있습니다.

- **모델 선택**. 내장 모델을 넘어서, Microsoft Foundry 모델 카탈로그에서 모델을 가져와 에이전트가 추론하고 반응하는 방식을 맞춤 설정할 수 있습니다.

- **어디서나 게시 가능**. 에이전트를 구축한 후에는 Microsoft Teams, Microsoft 365 Copilot, 웹사이트 또는 맞춤 앱 등 여러 채널에 게시할 수 있으며, 보안, 인증, 분석은 Power Platform 관리 경험을 통해 관리됩니다.

첫 번째 에이전트 구축은 [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst)에서 시작하고, 자세한 내용은 [Microsoft Copilot Studio 문서](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst)에서 확인할 수 있습니다.

## 과제: Copilot을 이용해 스타트업의 학생 과제 및 송장 관리

우리 스타트업은 학생들에게 온라인 강의를 제공합니다. 스타트업이 급성장하며 강의 수요를 따라잡기 어려워졌습니다. Power Platform 개발자로서, 학생 과제 관리 앱과 송장 처리 워크플로우를 자동화하는 로우 코드 솔루션을 구축해 달라는 요청을 받았습니다. 솔루션은 학생 과제를 추적하고 관리할 수 있어야 하며, 송장 처리 과정을 자동화하는 워크플로우도 포함해야 합니다. 생성 AI를 활용하여 솔루션을 개발해야 합니다.

Copilot 사용을 시작할 때, [Power Platform Copilot Prompt Library](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko)를 활용해 프롬프트를 시작할 수 있습니다. 이 라이브러리에는 Copilot으로 앱과 플로우를 구축하는 데 사용할 수 있는 프롬프트 목록이 포함되어 있습니다. 또한 라이브러리의 프롬프트를 참고해 Copilot에 요구사항을 어떻게 설명할지 아이디어를 얻을 수 있습니다.

### 스타트업을 위한 학생 과제 추적기 앱 구축

스타트업 교육자는 학생 과제 추적에 어려움을 겪고 있습니다. 과제 추적을 위해 스프레드시트를 사용해 왔으나 학생 수 증가로 관리하기 어려워졌습니다. 이에 학생 과제를 추적하고 관리하는 앱 구축을 요청받았습니다. 앱은 새로운 과제를 추가하고, 과제를 조회, 업데이트, 삭제할 수 있어야 합니다. 또한 교육자와 학생은 채점된 과제와 채점되지 않은 과제를 볼 수 있어야 합니다.

다음 단계를 따라 Power Apps에서 Copilot을 사용하여 앱을 구축할 것입니다:

1. [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) 홈 화면으로 이동합니다.

1. 홈 화면의 텍스트 입력 영역에 구축할 앱을 설명합니다. 예를 들어, <strong>_학생 과제를 추적하고 관리하는 앱을 구축하고 싶습니다_</strong>라고 입력합니다. <strong>전송</strong> 버튼을 클릭하여 프롬프트를 AI Copilot에 보냅니다.

![구축할 앱 설명하기](../../../translated_images/ko/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. AI Copilot은 저장할 데이터 필드와 일부 샘플 데이터를 포함한 Dataverse 테이블을 제안합니다. 이후 대화형 단계로 AI Copilot 조수 기능을 활용해 테이블을 필요에 맞게 맞춤 설정할 수 있습니다.

   > <strong>중요</strong>: Dataverse는 Power Platform의 기본 데이터 플랫폼으로, 앱 데이터를 저장하는 로우 코드 데이터 플랫폼입니다. 마이크로소프트 클라우드에서 안전하게 데이터를 저장하며, Power Platform 환경 내에서 제공되는 완전 관리형 서비스입니다. 데이터 분류, 데이터 계보, 세분화된 접근 제어 등 내장된 데이터 거버넌스 기능을 포함합니다. Dataverse에 대해 더 알아보려면 [여기](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko)를 참조하세요.

   ![새 테이블에서 제안된 필드](../../../translated_images/ko/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. 교육자는 과제를 제출한 학생에게 진행 상황을 알리는 이메일을 보내고 싶어 합니다. Copilot을 사용하여 학생 이메일을 저장할 새 필드를 테이블에 추가할 수 있습니다. 예를 들어, <strong>_학생 이메일을 저장하는 열을 추가하고 싶습니다_</strong>라는 프롬프트를 사용합니다. <strong>전송</strong> 버튼을 클릭하여 프롬프트를 AI Copilot에 보냅니다.

![새 필드 추가하기](../../../translated_images/ko/copilot-new-column.35e15ff21acaf274.webp)

1. AI Copilot이 새 필드를 생성하면, 필요에 맞게 필드를 맞춤 설정할 수 있습니다.


1. 테이블 작업을 완료하면 **앱 만들기** 버튼을 클릭하여 앱을 만드세요.

1. AI Copilot이 설명을 바탕으로 반응형 Canvas 앱을 생성합니다. 그런 다음 필요에 맞게 앱을 사용자 지정할 수 있습니다.

1. 교육자가 학생들에게 이메일을 보내기 위해 Copilot을 사용해 앱에 새 화면을 추가할 수 있습니다. 예를 들어, 다음 프롬프트를 사용해 앱에 새 화면을 추가할 수 있습니다: **_학생들에게 이메일을 보내는 화면을 추가하고 싶습니다_**. <strong>보내기</strong> 버튼을 클릭하여 프롬프트를 AI Copilot에 전송하세요.

![프롬프트 지시문을 통해 새 화면 추가하기](../../../translated_images/ko/copilot-new-screen.2e0bef7132a17392.webp)

1. AI Copilot이 새 화면을 생성하며, 이후 필요에 맞게 화면을 사용자 지정할 수 있습니다.

1. 앱 작업을 완료한 후 <strong>저장</strong> 버튼을 클릭하여 앱을 저장합니다.

1. 앱을 교육자들과 공유하려면 <strong>공유</strong> 버튼을 클릭하고 다시 한 번 <strong>공유</strong> 버튼을 클릭하세요. 그런 후 그들의 이메일 주소를 입력해 앱을 공유할 수 있습니다.

> <strong>숙제</strong>: 방금 만든 앱은 좋은 시작이지만 개선할 수 있습니다. 이메일 기능으로 교육자는 학생 이메일을 직접 입력해 수동으로 이메일을 보내야만 합니다. 과제를 제출하면 교육자가 자동으로 학생에게 이메일을 보내도록 자동화를 Copilot으로 만들 수 있나요? 힌트: 적절한 프롬프트를 통해 Power Automate에서 Copilot을 사용할 수 있습니다.

### 우리 스타트업을 위한 송장 정보 테이블 구축

우리 스타트업의 재무 팀은 송장을 관리하는 데 어려움을 겪고 있습니다. 그들은 스프레드시트를 사용해 송장을 추적해 왔지만 송장 수가 증가하면서 관리가 어려워졌습니다. 재무 팀이 받은 송장 정보를 저장, 추적, 관리할 수 있는 테이블을 만들어 달라고 요청했습니다. 이 테이블은 송장 정보 전체를 추출하여 저장하는 자동화 구축에 사용되어야 하며, 재무 팀이 결제 완료된 송장과 결제되지 않은 송장을 볼 수 있어야 합니다.

Power Platform에는 Dataverse라는 기본 데이터 플랫폼이 있어 앱과 솔루션의 데이터를 저장할 수 있습니다. Dataverse는 앱 데이터를 저장하기 위한 저코드 데이터 플랫폼이며, 완전히 관리되는 서비스로 Microsoft 클라우드에 데이터를 안전하게 저장하고 Power Platform 환경 내에서 프로비저닝됩니다. 데이터 분류, 데이터 연계, 세부 권한 제어 등 데이터 거버넌스 기능도 내장되어 있습니다. 자세한 내용은 [Dataverse 소개](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko)를 참고하세요.

왜 우리 스타트업에서 Dataverse를 사용해야 할까요? Dataverse 내 표준 및 사용자 지정 테이블은 데이터에 대한 안전하고 클라우드 기반 저장 옵션을 제공합니다. 테이블을 사용하면 Excel 통합 문서 안에 여러 워크시트를 쓰듯이 다양한 데이터를 저장할 수 있습니다. 조직이나 비즈니스 요구에 맞는 데이터를 저장하는 데 사용할 수 있습니다. 우리가 Dataverse 사용 시 얻을 수 있는 이점은 아래와 같습니다:

- **관리 용이**: 메타데이터와 데이터가 모두 클라우드에 저장되어 저장 방식이나 관리 방법에 대해 걱정할 필요 없이 앱과 솔루션 구축에 집중할 수 있습니다.

- <strong>안전함</strong>: Dataverse는 데이터를 위한 안전하고 클라우드 기반 저장 옵션을 제공합니다. 역할 기반 보안을 통해 테이블 데이터 접근 권한과 접근 방식을 제어할 수 있습니다.

- **풍부한 메타데이터**: 데이터 유형과 관계를 Power Apps 안에서 직접 사용할 수 있습니다.

- **비즈니스 논리 및 검증**: 비즈니스 규칙, 계산된 필드, 검증 규칙 등을 사용해 비즈니스 논리를 적용하고 데이터 정확성을 유지할 수 있습니다.

Dataverse가 무엇이고 왜 사용해야 하는지 알았으니, Copilot을 사용해 재무 팀 요구사항에 맞는 Dataverse 테이블을 만드는 방법을 살펴보겠습니다.

> <strong>참고</strong> : 이 테이블은 다음 섹션에서 송장 정보를 추출해 테이블에 저장하는 자동화를 구축하는 데 사용됩니다.

Copilot을 사용해 Dataverse에 테이블을 생성하려면 다음 단계를 따라주세요:

1. [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) 홈 화면으로 이동합니다.

2. 왼쪽 탐색 바에서 <strong>테이블</strong>을 선택한 다음 <strong>새 테이블 설명하기</strong>를 클릭하세요.

![새 테이블 선택](../../../translated_images/ko/describe-new-table.0792373eb757281e.webp)

1. **새 테이블 설명하기** 화면에서 테이블 생성에 관한 설명을 텍스트 영역에 입력하세요. 예: **_송장 정보를 저장할 테이블을 만들고 싶습니다_**. <strong>보내기</strong> 버튼을 클릭해 AI Copilot에 프롬프트를 전송합니다.

![테이블 설명하기](../../../translated_images/ko/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. AI Copilot은 추적하려는 데이터를 저장할 필드가 포함된 Dataverse 테이블과 일부 샘플 데이터를 제안합니다. 대화식 단계를 통해 AI Copilot 지원 기능을 이용해 테이블을 필요에 맞게 사용자 지정할 수 있습니다.

![추천된 Dataverse 테이블](../../../translated_images/ko/copilot-dataverse-table.b3bc936091324d9d.webp)

1. 재무 팀은 송장 상태를 공급자에게 이메일로 알려주고자 합니다. Copilot을 사용해 공급자 이메일을 저장하는 새 필드를 테이블에 추가할 수 있습니다. 예를 들어, 다음 프롬프트를 사용해 새 필드를 추가할 수 있습니다: **_공급자 이메일을 저장하는 열을 추가하고 싶습니다_**. <strong>보내기</strong> 버튼을 클릭해 프롬프트를 AI Copilot에 전송하세요.

1. AI Copilot이 새 필드를 생성하며, 이후 필요에 맞게 필드를 사용자 지정할 수 있습니다.

1. 테이블 작업이 끝나면 <strong>만들기</strong> 버튼을 클릭해 테이블을 생성하세요.

## Power Platform 내 AI Builder의 AI 모델

AI Builder는 Power Platform에서 제공하는 저코드 AI 기능으로, AI 모델을 활용해 프로세스를 자동화하고 결과를 예측할 수 있습니다. AI Builder를 통해 Dataverse 또는 SharePoint, OneDrive, Azure 같은 다양한 클라우드 데이터 소스에 연결된 앱과 플로우에 AI를 도입할 수 있습니다.

## 사전 제작 AI 모델과 맞춤 AI 모델 비교

AI Builder는 두 가지 유형의 AI 모델을 제공합니다: 사전 제작 AI 모델과 맞춤 AI 모델. 사전 제작 AI 모델은 마이크로소프트에서 훈련한 사용 준비가 된 AI 모델로 Power Platform에서 바로 사용할 수 있어, 데이터를 수집하고 직접 모델을 빌드, 훈련, 게시할 필요 없이 앱과 플로우에 인텔리전스를 추가할 수 있습니다. 이 모델로 프로세스를 자동화하거나 결과를 예측할 수 있습니다.

Power Platform에서 사용할 수 있는 사전 제작 AI 모델 일부는 다음과 같습니다:

- **핵심어 추출**: 텍스트에서 핵심 구문을 추출합니다.
- **언어 감지**: 텍스트의 언어를 감지합니다.
- **감정 분석**: 텍스트 내 긍정, 부정, 중립 또는 혼합 감정을 감지합니다.
- **명함 읽기**: 명함에서 정보를 추출합니다.
- **텍스트 인식**: 이미지에서 텍스트를 추출합니다.
- **객체 감지**: 이미지에서 객체를 감지하고 추출합니다.
- **문서 처리**: 양식에서 정보를 추출합니다.
- **송장 처리**: 송장에서 정보를 추출합니다.

맞춤 AI 모델을 사용하면 사용자의 자체 모델을 AI Builder에 도입해 AI Builder 맞춤 모델처럼 작동시키며, 자체 데이터를 사용해 모델을 학습시킬 수 있습니다. 이 모델들은 Power Apps와 Power Automate에서 프로세스를 자동화하고 결과를 예측하는 데 사용됩니다. 자체 모델 사용 시 적용되는 제한 사항이 있습니다. 자세한 내용은 이 [제한 사항](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst)을 참고하세요.

![AI Builder 모델](../../../translated_images/ko/ai-builder-models.8069423b84cfc47f.webp)

## 과제 #2 - 우리 스타트업의 송장 처리 플로우 구축

재무 팀은 송장 처리가 어렵다고 호소하고 있습니다. 그들은 스프레드시트를 이용해 송장을 추적해 왔으나 송장 건수가 늘면서 관리가 어렵게 되었습니다. AI를 이용해 송장을 처리하도록 도와주는 워크플로를 만들어 달라고 요청했습니다. 이 워크플로는 송장으로부터 정보를 추출해 Dataverse 테이블에 저장할 수 있어야 하며, 추출한 정보를 포함해 재무 팀에 이메일을 보낼 수 있도록 해야 합니다.

AI Builder가 무엇인지, 그리고 사용 이유를 알았으니 앞서 살펴본 AI Builder의 송장 처리 AI 모델을 사용해 재무 팀의 송장 처리 업무를 돕는 워크플로를 만드는 방법을 살펴보겠습니다.

AI Builder의 송장 처리 AI 모델을 활용해 재무 팀의 송장 처리를 돕는 워크플로를 구축하려면 다음 단계를 따라 주세요:

1. [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst) 홈 화면으로 이동합니다.

2. 홈 화면의 텍스트 영역에 생성하려는 워크플로를 설명하세요. 예: **_내 메일함에 도착한 송장을 처리한다_**. <strong>보내기</strong> 버튼을 클릭해 프롬프트를 AI Copilot에 전송하세요.

   ![Copilot power automate](../../../translated_images/ko/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. AI Copilot이 작업 수행에 필요한 액션을 제안합니다. <strong>다음</strong> 버튼을 클릭해 다음 단계를 진행할 수 있습니다.

4. 다음 단계에서 Power Automate는 플로우에 필요한 연결 설정을 요청합니다. 완료하면 **플로우 생성** 버튼을 클릭해 플로우를 생성합니다.

5. AI Copilot이 플로우를 생성하며, 필요에 맞게 플로우를 사용자 지정할 수 있습니다.

6. 플로우 트리거를 업데이트하고 송장이 저장될 <strong>폴더</strong>를 설정합니다. 예를 들어 <strong>받은 편지함</strong>으로 설정할 수 있습니다. <strong>고급 옵션 표시</strong>를 클릭하고 <strong>첨부 파일이 있는 경우만</strong>을 <strong>예</strong>로 설정하세요. 이를 통해 첨부 파일이 있는 이메일이 폴더에 도착할 때만 플로우가 실행됩니다.

7. 플로우에서 다음 액션들을 제거하세요: **HTML을 텍스트로 변환**, **Compose**, **Compose 2**, **Compose 3**, **Compose 4**, 이 액션들은 사용하지 않기 때문입니다.

8. 플로우에서 <strong>조건</strong> 액션도 제거하세요. 아래 스크린샷과 같이 보여야 합니다:

   ![power automate, remove actions](../../../translated_images/ko/powerautomate-remove-actions.7216392fe684ceba.webp)

9. **작업 추가** 버튼을 클릭하고 <strong>Dataverse</strong>를 검색하세요. **새 행 추가** 작업을 선택합니다.

10. **송장에서 정보 추출** 작업에서 **송장 파일** 입력란을 이메일의 <strong>첨부 파일 콘텐츠</strong>를 가리키도록 업데이트하세요. 이를 통해 플로우가 송장 첨부 파일에서 정보를 추출합니다.

11. 앞서 만든 <strong>테이블</strong>을 선택하세요. 예: **송장 정보** 테이블을 선택할 수 있습니다. 이전 작업의 동적 콘텐츠를 사용해 다음 필드를 채우세요:

    - ID
    - 금액
    - 날짜
    - 이름
    - 상태 - <strong>상태</strong>를 <strong>대기 중</strong>으로 설정하세요.
    - 공급자 이메일 - **새 이메일 도착 시** 트리거의 **보낸 사람(From)** 동적 콘텐츠를 사용하세요.

    ![power automate add row](../../../translated_images/ko/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. 플로우 작업이 완료되면 <strong>저장</strong> 버튼을 클릭해 플로우를 저장하세요. 그런 후 플로우 트리거에 지정한 폴더로 송장이 포함된 이메일을 보내 플로우를 테스트할 수 있습니다.

> <strong>숙제</strong>: 방금 구축한 플로우는 좋은 시작입니다. 이제 재무 팀이 송장의 현재 상태를 공급자에게 이메일로 업데이트할 수 있도록 하는 자동화를 어떻게 만들지 생각해 보세요. 힌트: 상태가 변경될 때 플로우가 실행되어야 합니다.

## Power Automate에서 텍스트 생성 AI 모델 사용하기

AI Builder의 GPT 텍스트 생성 AI 모델은 프롬프트를 기반으로 텍스트를 생성하며 Microsoft Azure OpenAI 서비스를 기반으로 합니다. 이 기능을 통해 GPT(Generative Pre-Trained Transformer) 기술을 앱과 플로우에 도입해 다양한 자동화 플로우와 유익한 애플리케이션을 구축할 수 있습니다.

GPT 모델은 방대한 데이터로 광범위하게 훈련되어 프롬프트가 제공되면 인간의 언어와 매우 유사한 텍스트를 생성할 수 있습니다. 워크플로 자동화와 통합되면 GPT 같은 AI 모델을 이용해 광범위한 업무를 효율화하고 자동화할 수 있습니다.

예를 들어, 이메일 초안, 제품 설명 등 다양한 용도의 텍스트를 자동으로 생성하는 플로우를 만들 수 있습니다. 또한 챗봇과 같은 앱에서 고객 서비스 담당자가 고객 문의에 효과적이고 신속하게 응답할 수 있도록 텍스트를 생성하는 데도 모델을 사용할 수 있습니다.

![프롬프트 생성](../../../translated_images/ko/create-prompt-gpt.69d429300c2e870a.webp)


Power Automate에서 이 AI 모델을 사용하는 방법을 배우려면 [Add intelligence with AI Builder and GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko) 모듈을 확인하세요.

## 훌륭해요! 학습을 계속하세요

이 수업을 마친 후, [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)에서 생성형 AI 지식을 계속 향상시키세요!

Copilot을 맞춤 설정하고 더 많이 활용하고 싶으신가요? GitHub Copilot을 최대한 활용할 수 있도록 돕는 명령어, 에이전트, 스킬, 구성의 커뮤니티 기여 모음인 [Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst)을 탐색해 보세요.

11과로 이동하여 [Function Calling과 생성형 AI 통합](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst) 방법을 살펴보세요!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->