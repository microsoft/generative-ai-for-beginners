# Low Code AI 애플리케이션 개발

[![Building Low Code AI Applications](../../images/10-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson10-gh?WT.mc_id=academic-105485-koreyst)

> _(위 이미지를 클릭하여 이 레슨의 비디오를 시청하세요)_

## 소개

이미지 생성 애플리케이션을 만드는 방법을 배웠으니 이제는 Low Code에 대해 이야기해보겠습니다. 생성형 AI는 low code를 포함한 다양한 영역에 사용될 수 있지만, low code란 무엇이며 어떻게 AI를 추가할 수 있을까요?

Low Code 개발 플랫폼을 사용하면 전통적인 개발자와 비개발자 모두가 쉽게 앱과 솔루션을 구축할 수 있습니다. Low Code 개발 플랫폼은 시각적 개발 환경을 제공하여 컴포넌트를 드래그 앤 드롭하여 앱과 솔루션을 구축할 수 있도록 합니다. 이를 통해 앱과 솔루션을 더 빠르고 적은 리소스로 구축할 수 있습니다. 이 레슨에서는 Low Code의 사용 방법과 Power Platform을 사용하여 low code 개발을 AI로 향상시키는 방법에 대해 자세히 알아보겠습니다.

Power Platform은 조직에게 직관적인 low-code 또는 no-code 환경을 통해 팀이 자체 솔루션을 구축할 수 있는 기회를 제공합니다. 이 환경은 솔루션 구축 프로세스를 간소화하는 데 도움이 됩니다. Power Platform을 사용하면 솔루션을 개월이나 연도가 아닌 몇 일 또는 몇 주 안에 구축할 수 있습니다. Power Platform은 Power Apps, Power Automate, Power BI, Power Pages 및 Power Virtual Agents라는 다섯 가지 주요 제품으로 구성됩니다.

이 레슨에서는 다음 내용을 다룹니다:

- Power Platform에서 생성형 AI 소개
- Copilot 소개 및 사용 방법
- Power Platform에서 생성형 AI를 사용하여 앱과 플로우 구축
- AI Builder를 사용하여 Power Platform의 AI 모델 이해

## 학습 목표

이 레슨을 마치면 다음을 할 수 있습니다:

- Power Platform에서 Copilot의 작동 방식 이해하기.

- 교육 스타트업을 위한 학생 과제 추적 앱 구축하기.

- AI를 사용하여 송장 정보를 추출하는 송장 처리 플로우 구축하기.

- Create Text with GPT AI 모델을 사용할 때 최상의 방법 적용하기.

이 레슨에서 사용할 도구와 기술은 다음과 같습니다:

- **Power Apps**: 데이터를 추적, 관리 및 상호 작용하는 앱을 구축하기 위한 low-code 개발 환경을 제공합니다.

- **Dataverse**: 학생 과제 추적 앱의 데이터를 저장하기 위한 Dataverse는 앱의 데이터를 저장하기 위한 low-code 데이터 플랫폼을 제공합니다.

- **Power Automate**: 송장 처리 플로우를 위한 low-code 개발 환경을 제공합니다. 이를 통해 송장 처리 프로세스를 자동화할 수 있습니다.

- **AI Builder**: 스타트업의 송장을 처리하기 위해 사전 구축된 AI 모델을 사용할 수 있습니다.

## Power Platform의 생성형 AI

생성형 AI를 사용하여 low-code 개발과 애플리케이션을 향상시키는 것은 Power Platform의 주요 관심사입니다. 목표는 데이터 과학 전문 지식이 필요하지 않고 AI를 사용하여 앱, 사이트, 대시보드를 구축하고 프로세스를 자동화할 수 있는 모든 사람을 가능하게 하는 것입니다. 이 목표는 Copilot과 AI Builder의 형태로 생성형 AI를 Power Platform의 low-code 개발 환경에 통합함으로써 달성됩니다.

### 이 작업은 어떻게 이루어질까요?

Copilot은 자연어를 사용하여 대화식 단계로 요구 사항을 설명함으로써 Power Platform 솔루션을 구축할 수 있는 AI 어시스턴트입니다. 예를 들어, 앱에서 사용할 필드를 지정하는 방법을 AI 어시스턴트에게 지시할 수 있으며, 그는 앱과 기본 데이터 모델을 모두 생성할 것입니다. 또는 Power Automate에서 플로우를 설정하는 방법을 지정할 수도 있습니다.

Copilot을 사용하여 사용자가 대화식 상호 작용을 통해 통찰력을 발견할 수 있도록 앱 화면의 기능으로 Copilot 기반 기능을 사용할 수 있습니다.

AI Builder는 Power Platform에서 사용할 수 있는 low-code AI 기능으로, AI 모델을 사용하여 프로세스를 자동화하고 결과를 예측할 수 있습니다. AI Builder를 사용하면 Dataverse나 SharePoint, OneDrive, Azure와 같은 다양한 클라우드 데이터 소스 또는 Dataverse와 같은 데이터에 연결하는 앱과 플로우에 AI를 가져올 수 있습니다.

Copilot은 Power Apps, Power Automate, Power BI, Power Pages 및 Power Virtual Agents의 모든 Power Platform 제품에서 사용할 수 있습니다. AI Builder는 Power Apps와 Power Automate에서 사용할 수 있습니다. 이 레슨에서는 교육 스타트업을 위한 솔루션을 구축하기 위해 Power Apps와 Power Automate에서 Copilot과 AI Builder를 사용하는 방법에 중점을 둘 것입니다.

### Power Apps에서의 Copilot

Power Apps는 Power Platform의 일부로, 데이터를 추적, 관리 및 상호 작용하기 위한 앱을 구축하기 위한 low-code 개발 환경을 제공합니다. 확장 가능한 데이터 플랫폼과 클라우드 서비스 및 온프레미스 데이터에 연결할 수 있는 기능을 갖춘 앱 개발 서비스 모음입니다. Power Apps를 사용하면 브라우저, 태블릿 및 휴대폰에서 실행되는 앱을 구축하고 동료들과 공유할 수 있습니다. Power Apps는 간단한 인터페이스로 사용자를 앱 개발로 안내하여 모든 비즈니스 사용자나 전문 개발자가 사용자 정의 앱을 구축할 수 있습니다. 앱 개발 경험은 또한 생성형 AI를 통해 Copilot과 함께 향상됩니다.

Power Apps의 Copilot AI 어시스턴트 기능을 사용하면 필요한 앱 종류와 앱이 추적, 수집 또는 표시해야 하는 정보를 설명할 수 있습니다. Copilot은 이 설명을 기반으로 반응형 캔버스 앱을 생성합니다. 그런 다음 앱을 사용자의 요구에 맞게 사용자 정의할 수 있습니다. AI Copilot은 또한 데이터를 추적하려는 필드와 일부 샘플 데이터가 포함된 Dataverse 테이블을 생성하고 제안합니다. 이후 대화식 단계를 통해 AI Copilot 어시스턴트 기능을 사용하여 테이블을 사용자의 요구에 맞게 사용자 정의할 수 있습니다. 이 기능은 Power Apps 홈 화면에서 즉시 사용할 수 있습니다.

### Power Automate에서의 Copilot

Power Automate는 Power Platform의 일부로, 응용 프로그램 및 서비스 간에 자동화된 워크플로우를 생성할 수 있도록 도와줍니다. 의사 결정 승인, 커뮤니케이션, 데이터 수집과 같은 반복적인 비즈니스 프로세스를 자동화하는 데 도움이 됩니다. 간단한 인터페이스를 통해 모든 기술 역량을 갖춘 사용자(초보자부터 숙련된 개발자까지)가 작업 작업을 자동화할 수 있습니다. 워크플로우 개발 경험은 또한 생성형 AI를 통해 Copilot과 함께 향상됩니다.

Power Automate의 Copilot AI 어시스턴트 기능을 사용하면 필요한 플로우 종류와 플로우가 수행해야 하는 작업을 설명할 수 있습니다. Copilot은 이 설명을 기반으로 플로우를 생성합니다. 그런 다음 플로우를 사용자의 요구에 맞게 사용자 정의할 수 있습니다. AI Copilot은 또한 자동화하려는 작업을 수행하기 위해 필요한 작업을 생성하고 제안합니다. 이후 대화식 단계를 통해 AI Copilot 어시스턴트 기능을 사용하여 작업을 사용자의 요구에 맞게 사용자 정의할 수 있습니다. 이 기능은 Power Automate 홈 화면에서 즉시 사용할 수 있습니다.

## 과제: Copilot을 사용하여 학생 과제 및 송장을 관리하는 솔루션 구축

우리 스타트업은 학생들에게 온라인 강좌를 제공합니다. 스타트업은 빠르게 성장하여 강좌 수요를 따라가기 어려워졌습니다. 스타트업은 학생 과제와 송장 처리 프로세스를 관리하기 위해 low code 솔루션을 구축하는 데 도움을 받기 위해 Power Platform 개발자로서 여러분을 고용했습니다. 솔루션은 앱을 통해 학생 과제를 추적하고 관리하며, 워크플로우를 통해 송장 처리 프로세스를 자동화해야 합니다. 여러분은 생성형 AI를 사용하여 솔루션을 개발하도록 요청받았습니다.

Copilot 사용을 시작할 때는 [Power Platform Copilot Prompt Library](https://pnp.github.io/powerplatform-prompts/?WT.mc_id=academic-109639-somelezediko)를 사용하여 프롬프트로 시작할 수 있습니다. 이 라이브러리에는 Copilot을 사용하여 앱과 플로우를 구축하는 데 사용할 수 있는 프롬프트 목록이 포함되어 있습니다. 또한 라이브러리의 프롬프트를 사용하여 Copilot에게 요구 사항을 설명하는 방법에 대한 아이디어를 얻을 수 있습니다.

### 학생 과제 추적 앱 구축하기

우리 스타트업의 교육자들은 학생 과제를 추적하는 데 어려움을 겪고 있습니다. 학생 수가 증가함에 따라 스프레드시트를 사용하여 과제를 추적하고 있지만 관리하기 어려워졌습니다. 교육자들은 학생 과제를 추적하고 관리할 수 있는 앱을 구축해 달라고 요청했습니다. 이 앱은 새로운 과제를 추가하고, 과제를 보고, 과제를 업데이트하고, 과제를 삭제할 수 있어야 합니다. 또한 교육자와 학생 모두가 채점된 과제와 채점되지 않은 과제를 볼 수 있어야 합니다.

다음 단계를 따라 Power Apps에서 Copilot을 사용하여 앱을 구축하겠습니다:

1. [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) 홈 화면으로 이동합니다.

2. 왼쪽 탐색 창에서 **Tables**을 선택한 다음 **Describe the new Table**을 클릭합니다.

3. 홈 화면의 텍스트 영역을 사용하여 구축하려는 앱을 설명합니다. 예를 들어, **_학생 과제를 추적하고 관리하기 위한 앱을 구축하고 싶습니다_**. **Send** 버튼을 클릭하여 AI Copilot에게 프롬프트를 전송합니다.

![Describe the app you want to build](../../images/copilot-chat-prompt-powerapps.png?WT.mc_id=academic-105485-koreyst)

4. AI Copilot은 데이터베이스 테이블을 제안하며, 추적하려는 데이터를 저장하기 위해 필요한 필드와 일부 샘플 데이터를 제공합니다. 그런 다음 대화식 단계를 통해 테이블을 사용자 정의하여 요구 사항에 맞게 만들 수 있습니다.

   > **중요**: Dataverse는 Power Platform의 기반이 되는 데이터 플랫폼입니다. 앱의 데이터를 저장하기 위한 low-code 데이터 플랫폼으로, Microsoft Cloud에 안전하게 데이터를 저장하며 Power Platform 환경 내에서 프로비저닝됩니다. 데이터 분류, 데이터 계보, 세밀한 액세스 제어 등과 같은 내장 데이터 거버넌스 기능을 갖추고 있습니다. Dataverse에 대해 자세히 알아보려면 [여기](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko)를 참조하세요.

   ![새로운 테이블에 제안된 필드](../../images/copilot-dataverse-table-powerapps.png?WT.mc_id=academic-105485-koreyst)

5. 교육자들은 과제를 제출한 학생들에게 진행 상황을 알리기 위해 이메일을 보내고 싶어합니다. Copilot을 사용하여 테이블에 학생 이메일을 저장할 새로운 필드를 추가할 수 있습니다. 예를 들어, 다음과 같은 프롬프트를 사용하여 테이블에 새로운 필드를 추가할 수 있습니다: **_학생 이메일을 저장할 열을 추가하고 싶습니다_**. **Send** 버튼을 클릭하여 AI Copilot에게 프롬프트를 전송합니다.

![Adding a new field](../../images/copilot-new-column.png?WT.mc_id=academic-105485-koreyst)

6. AI Copilot은 새로운 필드를 생성하고, 사용자 정의하여 요구 사항에 맞게 만들 수 있습니다.

7. 테이블 작업이 완료되면 **Create app** 버튼을 클릭하여 앱을 생성합니다.

8. AI Copilot은 설명에 기반한 반응형 캔버스 앱을 생성하며, 사용자 정의하여 요구 사항에 맞게 만들 수 있습니다.

9. 교육자가 학생들에게 이메일을 보낼 수 있도록 앱에 새로운 화면을 추가할 수 있습니다. 예를 들어, 다음과 같은 프롬프트를 사용하여 앱에 새로운 화면을 추가할 수 있습니다: **_학생들에게 이메일을 보내기 위한 화면을 추가하고 싶습니다_**. **Send** 버튼을 클릭하여 AI Copilot에게 프롬프트를 전송합니다.

![Adding a new screen via a prompt instruction](../../images/copilot-new-screen.png?WT.mc_id=academic-105485-koreyst)

10. AI Copilot은 새로운 화면을 생성하고, 사용자 정의하여 요구 사항에 맞게 만들 수 있습니다.

11. 앱 작업이 완료되면 **Save** 버튼을 클릭하여 앱을 저장합니다.

12. 교육자와 앱을 공유하려면 **Share** 버튼을 클릭한 다음 **Share** 버튼을 다시 클릭합니다. 그런 다음 교육자의 이메일 주소를 입력하여 앱을 공유할 수 있습니다.

> **과제**: 방금 구축한 앱은 좋은 시작이지만 개선할 수 있습니다. 이메일 기능을 사용하면 교육자는 학생들에게 이메일을 수동으로 보내야 합니다. Copilot을 사용하여 학생들이 과제를 제출할 때 자동으로 교육자에게 이메일을 보낼 수 있는 자동화를 구축할 수 있을까요? 힌트는 적절한 프롬프트를 사용하여 Power Automate에서 Copilot을 사용하여 이를 구축할 수 있다는 것입니다.

### 우리 스타트업을 위한 송장 정보 테이블 구축하기

우리 스타트업의 재무팀은 송장을 처리하는 데 어려움을 겪고 있습니다. 송장을 추적하기 위해 스프레드시트를 사용하고 있지만 송장 수가 증가함에 따라 관리하기 어려워졌습니다. 그들은 송장 정보를 추출하고 해당 정보를 Dataverse 테이블에 저장하는 자동화를 구축할 수 있는 테이블을 만들어 달라고 요청했습니다. 또한 송장이 지불된 것과 미지불된 것을 확인할 수 있는 테이블을 제공해야 합니다.

Power Platform에는 Dataverse라는 데이터 플랫폼이 있어 앱과 솔루션의 데이터를 저장할 수 있습니다. Dataverse는 앱의 데이터를 저장하기 위한 low-code 데이터 플랫폼으로, Microsoft Cloud에 안전하게 데이터를 저장하며 Power Platform 환경 내에서 프로비저닝됩니다. 데이터 분류, 데이터 계보, 세밀한 액세스 제어 등과 같은 내장 데이터 거버넌스 기능을 갖추고 있습니다. Dataverse에 대해 자세히 알아보려면 [여기](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko)를 참조하세요.

우리 스타트업이 Dataverse를 사용해야 하는 이유는 무엇일까요? Dataverse 내의 표준 및 사용자 정의 테이블은 데이터를 위한 안전하고 클라우드 기반의 저장 옵션을 제공합니다. 테이블은 하나의 Excel 워크북에서 여러 개의 워크시트를 사용하는 것과 유사하게 다양한 유형의 데이터를 저장할 수 있습니다. 테이블을 사용하여 조직 또는 비즈니스 요구에 맞는 데이터를 저장할 수 있습니다. 우리 스타트업이 Dataverse를 사용함으로써 얻을 수 있는 이점은 다음과 같습니다.

- **쉬운 관리**: 메타데이터와 데이터 모두 클라우드에 저장되므로 저장 또는 관리 방법에 대해 걱정할 필요가 없습니다. 앱과 솔루션 구축에 집중할 수 있습니다.

- **보안**: Dataverse는 데이터를 위한 안전하고 클라우드 기반의 저장 옵션을 제공합니다. 역할 기반 보안을 사용하여 테이블의 데이터에 액세스할 수 있는 사용자와 액세스 방법을 제어할 수 있습니다.

- **풍부한 메타데이터**: 데이터 유형과 관계를 Power Apps에서 직접 사용할 수 있습니다.

- **로직 및 유효성 검사**: 비즈니스 규칙, 계산 필드 및 유효성 검사 규칙을 사용하여 비즈니스 로직을 강제하고 데이터의 정확성을 유지할 수 있습니다.

이제 Dataverse가 무엇인지 알고 왜 사용해야 하는지 알았으니, AI Copilot을 사용하여 재무팀의 요구 사항을 충족하는 Dataverse 테이블을 생성하는 방법을 살펴보겠습니다.

> **참고**: 이 테이블은 다음 섹션에서 송장 정보를 추출하고 해당 정보를 저장하는 자동화를 구축하는 데 사용됩니다.

Copilot을 사용하여 Dataverse에서 테이블을 생성하려면 다음 단계를 따르세요:

1. [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) 홈 화면으로 이동합니다.

2. 왼쪽 탐색 창에서 **Tables**을 선택한 다음 **Describe the new Table**을 클릭합니다.

![Select new table](../../images/describe-new-table.png?WT.mc_id=academic-105485-koreyst)

3. **Describe the new Table** 화면에서 테이블을 생성할 내용을 텍스트 영역에 설명합니다. 예를 들어, **_송장 정보를 저장하기 위한 테이블을 생성하고 싶습니다_**. **Send** 버튼을 클릭하여 AI Copilot에게 프롬프트를 전송합니다.

![Describe the table](../../images/copilot-chat-prompt-dataverse.png?WT.mc_id=academic-105485-koreyst)

4. AI Copilot은 필요한 필드와 일부 샘플 데이터를 포함한 Dataverse 테이블을 제안합니다. 그런 다음 AI Copilot 도우미 기능을 통해 대화식 단계를 통해 테이블을 사용자 정의하여 요구 사항에 맞게 만들 수 있습니다.

![Suggested Dataverse table](../../images/copilot-dataverse-table.png?WT.mc_id=academic-105485-koreyst)

5. 재무팀은 공급업체에게 송장의 현재 상태를 알리기 위해 이메일을 보내고 싶어합니다. Copilot을 사용하여 테이블에 공급업체 이메일을 저장할 새로운 필드를 추가할 수 있습니다. 예를 들어, 다음과 같은 프롬프트를 사용하여 테이블에 새로운 필드를 추가할 수 있습니다: **_공급업체 이메일을 저장할 열을 추가하고 싶습니다_**. **Send** 버튼을 클릭하여 AI Copilot에게 프롬프트를 전송합니다.

6. AI Copilot은 새로운 필드를 생성하고, 사용자 정의하여 요구 사항에 맞게 만들 수 있습니다.

7. 테이블 작업이 완료되면 **Create** 버튼을 클릭하여 테이블을 생성합니다.

## AI Builder를 사용한 Power Platform의 AI 모델

AI Builder는 Power Platform에서 사용할 수 있는 low-code AI 기능으로, 프로세스 자동화와 결과 예측을 도와주는 AI 모델을 사용할 수 있습니다. AI Builder를 사용하면 Dataverse나 SharePoint, OneDrive, Azure와 같은 다양한 클라우드 데이터 소스 또는 Dataverse 내의 데이터에 연결된 앱과 플로우에 AI를 적용할 수 있습니다.

AI Builder는 두 가지 유형의 AI 모델을 제공합니다: Prebuilt AI 모델과 Custom AI 모델입니다. Prebuilt AI 모델은 Microsoft에서 훈련한 사용 준비가 된 AI 모델로, Power Platform에서 사용할 수 있습니다. 이 모델을 사용하면 데이터를 수집하고 모델을 빌드, 훈련 및 게시할 필요 없이 앱과 플로우에 지능을 추가할 수 있습니다. 이러한 모델을 사용하여 프로세스를 자동화하고 결과를 예측할 수 있습니다.

Power Platform에서 사용할 수 있는 Prebuilt AI 모델 중 일부는 다음과 같습니다:

- **키 구문 추출**: 이 모델은 텍스트에서 키 구문을 추출합니다.
- **언어 감지**: 이 모델은 텍스트의 언어를 감지합니다.
- **감정 분석**: 이 모델은 텍스트의 긍정적, 부정적, 중립적 또는 혼합된 감정을 감지합니다.
- **명함 판독기**: 이 모델은 명함에서 정보를 추출합니다.
- **텍스트 인식**: 이 모델은 이미지에서 텍스트를 추출합니다.
- **객체 감지**: 이 모델은 이미지에서 객체를 감지하고 추출합니다.
- **양식 처리**: 이 모델은 양식에서 정보를 추출합니다.
- **송장 처리**: 이 모델은 송장에서 정보를 추출합니다.

Custom AI 모델을 사용하면 AI Builder에 직접 모델을 가져와서 AI Builder 사용자 정의 모델과 같은 방식으로 작동하도록 할 수 있습니다. 이 모델을 사용하여 Power Apps와 Power Automate에서 프로세스를 자동화하고 결과를 예측할 수 있습니다. 사용자 정의 모델을 사용할 때는 일부 제한 사항이 적용됩니다. 이에 대한 자세한 내용은 [여기](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst)를 참조하세요.

![AI builder models](../../images/ai-builder-models.png?WT.mc_id=academic-105485-koreyst)

## 과제 #2 - 우리 스타트업을 위한 송장 처리 플로우 구축하기

재무팀은 송장 처리에 어려움을 겪고 있습니다. 송장을 추적하기 위해 스프레드시트를 사용하고 있지만 송장 수가 증가함에 따라 관리하기 어려워졌습니다. 그들은 AI를 활용하여 송장을 처리하는 워크플로우를 구축해주길 요청했습니다. 이 워크플로우는 송장에서 정보를 추출하고 해당 정보를 Dataverse 테이블에 저장할 수 있어야 합니다. 또한 추출된 정보를 재무팀에게 이메일로 보낼 수 있어야 합니다.

AI Builder가 무엇이며 왜 사용해야 하는지 알았으니, 앞서 다룬 AI Builder의 송장 처리 AI 모델을 활용하여 재무팀이 송장을 처리하는 데 도움이 되는 워크플로우를 구축하는 방법을 알아보겠습니다.

AI Builder의 송장 처리 AI 모델을 활용하여 재무팀이 송장을 처리하는 워크플로우를 구축하려면 다음 단계를 따르세요:

1. [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst) 홈 화면으로 이동합니다.

2. 홈 화면의 텍스트 영역을 사용하여 구축하려는 워크플로우를 설명합니다. 예를 들어, **_송장이 메일함에 도착했을 때 송장을 처리합니다_**. **Send** 버튼을 클릭하여 AI Copilot에게 프롬프트를 전송합니다.

   ![Copilot power automate](../../images/copilot-chat-prompt-powerautomate.png?WT.mc_id=academic-105485-koreyst)

3. AI Copilot은 자동화하려는 작업을 수행하기 위해 필요한 동작을 제안합니다. 다음 단계를 진행하려면 **Next** 버튼을 클릭할 수 있습니다.

4. 다음 단계에서 Power Automate는 워크플로우에 필요한 연결 설정을 위해 프롬프트를 표시합니다. 설정을 완료한 후 **Create flow** 버튼을 클릭하여 워크플로우를 생성합니다.

5. AI Copilot은 워크플로우를 생성하고, 원하는 대로 워크플로우를 사용자 정의할 수 있습니다.

6. 워크플로우의 트리거를 업데이트하고 **Folder**를 송장이 저장될 폴더로 설정합니다. 예를 들어, **Inbox**로 폴더를 설정할 수 있습니다. **Show advanced options**를 클릭하고 **Only with Attachments**를 **Yes**로 설정합니다. 이렇게 하면 워크플로우가 첨부 파일이 포함된 이메일이 폴더에 도착했을 때만 실행되도록 할 수 있습니다.

7. 워크플로우에서 다음 동작을 제거합니다: **HTML to text**, **Compose**, **Compose 2**, **Compose 3**, **Compose 4**. 이 동작들은 사용하지 않을 것이기 때문에 제거합니다.

8. 워크플로우에서 **Condition** 동작을 제거합니다. 사용하지 않을 것이기 때문에 제거합니다. 다음과 같이 보일 것입니다:

   ![power automate, remove actions](../../images/powerautomate-remove-actions.png?WT.mc_id=academic-105485-koreyst)

9. **Add an action** 버튼을 클릭하고 **Dataverse**를 검색합니다. **Add a new row** 동작을 선택합니다.

10. **송장에서 정보 추출** 동작에서 **Invoice File**을 이메일의 **Attachment Content**로 설정합니다. 이렇게 하면 워크플로우가 송장 첨부 파일에서 정보를 추출할 수 있습니다.

11. 이전에 생성한 **Table**을 선택합니다. 예를 들어, **Invoice Information** 테이블을 선택할 수 있습니다. 이전 동작의 동적 콘텐츠를 사용하여 다음 필드를 채웁니다:

    - ID
    - Amount
    - Date
    - Name
    - Status - **Status**를 **Pending**으로 설정합니다.
    - Supplier Email - **When a new email arrives** 트리거의 **From** 동적 콘텐츠를 사용합니다.

    ![power automate add row](../../images/powerautomate-add-row.png?WT.mc_id=academic-105485-koreyst)

12. 워크플로우 작업이 완료되면 **Save** 버튼을 클릭하여 워크플로우를 저장합니다. 그런 다음 지정한 폴더로 송장 첨부 파일이 포함된 이메일을 보내어 워크플로우를 테스트할 수 있습니다.

> **과제**: 방금 구축한 워크플로우는 좋은 시작입니다. 이제 재무팀이 공급업체에게 송장의 현재 상태를 알리기 위해 이메일을 보낼 수 있는 자동화를 구축하는 방법을 고민해보세요. 힌트: 워크플로우는 송장의 상태가 변경될 때 실행되어야 합니다.

## Power Automate에서 텍스트 생성 AI 모델 사용하기

AI Builder의 Create Text with GPT AI 모델은 Microsoft Azure OpenAI 서비스를 기반으로 프롬프트를 기반으로 텍스트를 생성할 수 있는 기능을 제공합니다. 이 기능을 사용하면 GPT (Generative Pre-Trained Transformer) 기술을 앱과 워크플로우에 통합하여 다양한 자동화 흐름과 통찰력 있는 애플리케이션을 구축할 수 있습니다.

GPT 모델은 방대한 양의 데이터를 기반으로 광범위한 훈련을 거쳐 프롬프트가 제공되면 인간의 언어와 유사한 텍스트를 생성할 수 있습니다. 워크플로우 자동화와 통합되면 GPT와 같은 AI 모델을 활용하여 다양한 작업을 간소화하고 자동화할 수 있습니다.

예를 들어, 다음과 같은 다양한 용도로 텍스트를 자동으로 생성하는 흐름을 구축할 수 있습니다: 이메일 초안, 제품 설명 등. 또한 이 모델을 사용하여 챗봇과 고객 서비스 앱과 같은 다양한 앱에 텍스트를 생성할 수 있으며, 이를 통해 고객 서비스 담당자가 고객 문의에 효과적으로 대응할 수 있습니다.

![create a prompt](../../images/create-prompt-gpt.png?WT.mc_id=academic-105485-koreyst)

Power Automate에서 이 AI 모델을 사용하는 방법에 대해 자세히 알아보려면 [AI Builder와 GPT를 사용하여 지능 추가하기](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko) 모듈을 참조하세요.

## 잘하셨습니다. 학습을 계속하세요!

이 레슨을 완료한 후 [Generative AI 학습 컬렉션](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인하여 생성형 AI 지식을 계속 향상시킬 수 있습니다!

다음 레슨인 [Function Calling과 생성형 AI 통합](../../../11-integrating-with-function-calling/translations/ko/README.md?WT.mc_id=academic-105485-koreyst)을 살펴보세요!
