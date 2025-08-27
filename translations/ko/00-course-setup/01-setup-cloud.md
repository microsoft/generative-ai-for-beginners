<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T15:13:56+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "ko"
}
-->
# 클라우드 설정 ☁️ – GitHub Codespaces

**로컬에 아무것도 설치하고 싶지 않다면 이 가이드를 따라하세요.**  
Codespaces는 모든 의존성이 미리 설치된 무료 브라우저 기반 VS Code 환경을 제공합니다.

---

## 1.  Codespaces를 사용하는 이유?

| 장점 | 여러분에게 의미하는 것 |
|------|----------------------|
| ✅ 설치 필요 없음 | Chromebook, iPad, 학교 PC 등 어디서든 사용 가능 |
| ✅ 미리 구성된 개발 컨테이너 | Python 3, Node.js, .NET, Java가 이미 포함되어 있음 |
| ✅ 무료 할당량 | 개인 계정은 **월 120 코어-시간 / 60 GB-시간** 제공 |

> 💡 **팁**  
> 사용하지 않는 codespace는 **중지**하거나 **삭제**해서 할당량을 아껴주세요  
> (보기 ▸ 명령 팔레트 ▸ *Codespaces: Stop Codespace*).

---

## 2.  Codespace 만들기 (원클릭)

1. 이 저장소를 **포크**하세요 (오른쪽 상단 **Fork** 버튼).  
2. 포크한 저장소에서 **Code ▸ Codespaces ▸ Create codespace on main**을 클릭하세요.  
   ![Codespace 생성 버튼이 보이는 대화상자](../../../00-course-setup/images/who-will-pay.webp)

✅ 브라우저에서 VS Code 창이 열리고 개발 컨테이너가 빌드됩니다.  
처음에는 **약 2분** 정도 소요됩니다.

## 3. API 키 안전하게 추가하기

### 옵션 A Codespaces Secrets — 추천 방법

1. ⚙️ 톱니바퀴 아이콘 -> 명령 팔레트 -> Codespaces : Manage user secret -> Add a new secret 선택
2. 이름: OPENAI_API_KEY
3. 값: 키를 붙여넣고 → Add secret 클릭

이제 코드가 자동으로 키를 인식합니다.

### 옵션 B .env 파일 (정말 필요한 경우만)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서(원어)가 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 이 번역의 사용으로 인해 발생하는 오해나 오역에 대해 당사는 책임을 지지 않습니다.