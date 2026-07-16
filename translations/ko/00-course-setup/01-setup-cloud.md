# 클라우드 설정 ☁️ – GitHub Codespaces

**로컬에 아무 것도 설치하고 싶지 않을 때 이 가이드를 사용하세요.**  
Codespaces는 모든 종속 항목이 미리 설치된 무료 브라우저 기반 VS Code 인스턴스를 제공합니다.

---

## 1. 왜 Codespaces일까요?

| 장점 | 당신에게 의미하는 바 |
|---------|----------------------|
| ✅ 설치 불필요 | 크롬북, 아이패드, 학교 실습용 PC 등에서 작동 |
| ✅ 사전 구축된 개발 컨테이너 | Python 3, Node.js, .NET, Java가 이미 포함되어 있음 |
| ✅ 무료 할당량 | 개인 계정은 한 달에 **120 코어-시간 / 60 GB-시간** 제공 |

> 💡 <strong>팁</strong>  
> 할당량을 건강하게 유지하려면 <strong>유휴 codespaces를 중지</strong>하거나 <strong>삭제</strong>하세요  
> (보기 ▸ 명령 팔레트 ▸ *Codespaces: Stop Codespace*).

---

## 2. Codespace 생성하기 (한 번 클릭)

1. 이 저장소를 <strong>포크</strong>하세요 (우측 상단 **Fork** 버튼).  
2. 포크된 저장소에서 **Code ▸ Codespaces ▸ Create codespace on main** 클릭.  
   ![Dialog showing buttons to create a codespace](../../../translated_images/ko/who-will-pay.4c0609b1c7780f44.webp)

✅ 브라우저 VS Code 창이 열리고 개발 컨테이너가 빌드되기 시작합니다.
처음에는 **약 2분** 정도 걸립니다.

## 3. API 키 추가하기 (안전한 방법)

### 옵션 A Codespaces 시크릿 — 추천함

1. ⚙️ 톱니바퀴 아이콘 -> 명령 팔레트 -> Codespaces : 사용자 시크릿 관리 -> 새 시크릿 추가.
2. 이름: OPENAI_API_KEY
3. 값: 키를 붙여넣기 → 시크릿 추가

끝입니다—코드가 자동으로 이를 인식합니다.

### 옵션 B .env 파일 (정말 필요할 때만)

```bash
cp .env.copy .env
code .env         # OPENAI_API_KEY=your_key_here를 입력하세요
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->