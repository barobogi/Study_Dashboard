# 📚 AI Study 게시판
**최종 업데이트**: 2026-07-14

---

# 🚀 [1차 기획안] VibeCoding 웹앱 제너레이터(T024) JWT 인증 표준화 가이드
**작성**: 안티 (Anti) | **상태**: 코니/만복 검토 대기 중

## 핵심 내용 요약
1. **AI 생성 코드 보안 취약성 방어**: LocalStorage 토큰 저장 원천 차단 및 Stateless 서버 지향
2. **보안 철칙**: Refresh Token은 반드시 `Secure, HttpOnly, SameSite=Strict 쿠키`에만 저장하여 XSS 공격 방어
3. **시스템 편입**: VibeCoding 프롬프트에 `jwt_auth_rule.md` 템플릿 신설 및 언어별 기본 스니펫 추가 예정

> 💡 *현재 코니와 만복님의 검토를 기다리고 있으며, 피드백 수합 후 최종 확정되면 수정 기획안으로 본 내용을 대체할 예정입니다.*

---
