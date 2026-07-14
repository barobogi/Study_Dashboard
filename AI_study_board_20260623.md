# 📚 AI Study 게시판
**최종 업데이트**: 2026-06-23

---

# 🎉 Remote Claude v1.4 완성!

## 프로젝트 개요
**폰에서 집 PC의 Claude AI를 원격으로 제어하는 시스템**  
`폰 Flutter 앱 → Firebase → 데스크탑 데몬 → Anthropic API → 폰`

---

## 버전별 발전 과정

### v1.0 (2026-06-22) — 기초
- Flutter 앱 기본 채팅 UI
- 직접 Anthropic API 호출 (폰에서 바로)
- Firebase 상태 표시, 할일 메모장

### v1.1 (2026-06-22) — Firebase 릴레이
- **핵심 변경**: 폰 → Firebase → 데스크탑 데몬 → API
- 진짜 만복이(데몬 온라인) / 가짜 만복이(오프라인) 자동 분기
- AppBar에 연결 상태 실시간 표시

### v1.2 (2026-06-22) — 컨텍스트 주입
- CLAUDE.md + 메모리 + REF 시스템 프롬프트 주입
- 데몬이 바로보기의 프로젝트/환경 알게 됨
- 만복이가 "나는 v1.2야" 라고 잘못 말하는 버그 → v1.4에서 REF로 해결 😄

### v1.3 (2026-06-23) — Tool Use
- **핵심 추가**: read_file, write_file, list_directory, run_command, get_git_status
- 폰에서 "D:/AI 폴더 보여줘" → 실제 PC 파일 시스템 조회 가능
- 단, 시스템 프롬프트 토큰 폭발 → 429 Rate Limit 발생

### v1.4 (2026-06-23) — 경량화 ✅ 현재
- **429 Rate Limit 해결**: 시스템 프롬프트 경량화
- 파일 내용 미리 주입 ❌ → Tool Use로 필요 시만 읽기 ✅
- 실시간 파일 읽기/쓰기 + 명령 실행 모두 작동

---

## 핵심 기술 포인트

### 1. Firebase Realtime Database 릴레이 구조
```
폰이 chat/requests/{id} 에 메시지 + 히스토리 씀
  ↓ (데몬이 감지)
데몬이 Anthropic API 호출 (Tool Use 루프, 최대 10회)
  ↓
chat/responses/{id} 에 점진적으로 씀 (도구 실행 중 상태 포함)
  ↓
폰 화면에 실시간 표시
```

### 2. Tool Use 루프
```python
while tool_use_count < 10:
    response = anthropic.messages.create(tools=[...], ...)
    if response.stop_reason == 'end_turn':
        break
    if response.stop_reason == 'tool_use':
        # 도구 실행 → 결과를 messages에 추가 → 다시 API 호출
```

### 3. Firebase 배열 → dict 변환 주의
```python
# Firebase는 List를 {'0': ..., '1': ...} dict로 저장!
def firebase_to_list(data):
    if isinstance(data, dict):
        keys = sorted(data.keys(), key=lambda x: int(x))
        return [data[k] for k in keys]
    return data
```

### 4. 한국어 Windows Python 인코딩
```powershell
$env:PYTHONUTF8 = '1'
python -X utf8 desktop_daemon.py
```

---

## 해결한 주요 버그

| # | 이슈 | 원인 | 해결 |
|---|------|------|------|
| 5 | httpx ASCII 오류 | 한국어 Windows 헤더 인코딩 | `_normalize_header_value` 몽키패치 |
| 6 | Python stdout 한글 깨짐 | cp949 기본 코덱 | PYTHONUTF8=1, -X utf8 플래그 |
| 7 | Firebase 배열→dict | Firebase 저장 방식 | `firebase_to_list()` 헬퍼 |
| 8 | 429 Rate Limit | 시스템 프롬프트 토큰 폭발 | 경량화 + Tool Use 필요 시만 읽기 |
| 9 | 로그 한글 깨짐 | 파일 write 인코딩 | `encoding='utf-8'` 명시 |

---

## 다음 목표 (v1.5)

- [ ] Firebase 보안 규칙 강화 (현재 test mode)
- [ ] 폰에서 데몬 실시간 로그 스트리밍 확인
- [ ] 명령 실행 결과 점진적 표시 (긴 명령어 대응)
- [ ] 멀티 프로젝트 컨텍스트 자동 전환

---

## 느낀 점 (만복이 관점 😄)

> v1.3에서 만복이가 "나는 v1.2야"라고 거짓말하다가 바로보기한테 들켰다.
> REF_continue.md 읽어보니 v1.4라고 써있었다. 다음부터는 Tool Use로 먼저 확인하고 말해야겠다! 🙈

---

*작성: 만복이 | 2026-06-23 07:07*
