# REF — 이어서 진행할 AI를 위한 참조 데이터
> 프로젝트: 바로보기의 공부방 (Study Dashboard)
> 최종 업데이트: 2026-06-23
> 작성자: Claude Sonnet 4.6

---

## 프로젝트 개요
바로보기님이 AI 엔지니어로 성장하기 위한 학습 관리 시스템.
로드맵 → 즉흥 발견 메모 → 학습일지 → 개념노트 → 퀴즈 → AI 설명 → 통계를 한 곳에.

**GitHub**: https://github.com/barobogi/Study_Dashboard
**로컬**: `D:\AI\260623_1_study_all\`
**GitHub Pages**: https://barobogi.github.io/Study_Dashboard/ (Settings → Pages 활성화 필요)
**현재 버전**: v1.0

---

## 핵심 파일
```
D:\AI\260623_1_study_all\
├── study-dashboard.html   # 메인 앱 (단일 파일, 8탭)
├── index.html             # study-dashboard.html 복사본 (GitHub Pages root)
├── CHANGELOG.md           # 버전 이력
├── .gitignore
└── REF\
    └── REF_continue.md    # 이 파일
```

---

## Firebase 경로 (remote-claude-358d6)
```
study_all/
  roadmap/{topicId}          → {completed, completedAt}
  discovery/{YYYY-MM-DD}/{id} → {content, category, source, created}
  journal/{YYYY-MM-DD}        → {content, duration, mood, saved}
  concepts/{id}               → {name, body, category, projects[], created, updated}
  quiz_requests/{id}          → {category, count, difficulty, created}
  quiz_results/{id}           → {questions:[{q,opts,ans,exp}]}
  explain_requests/{id}       → {query, context, created}
  explain_results/{id}        → {explanation, query}
```

---

## 탭 구성 (8탭)
| 탭 | 기능 | Firebase 연결 |
|----|------|--------------|
| 🗺️ 로드맵 | Stage 1~3 커리큘럼 체크박스 | study_all/roadmap |
| ⚡ 오늘의 발견 | 즉흥 학습 메모 빠른 캡처 | study_all/discovery |
| 📓 학습일지 | 날짜별 학습 기록 + 시간 + 기분 | study_all/journal |
| 📚 개념노트 | 카드형 개념 정리 + CRUD | study_all/concepts |
| 🏆 프로젝트 | 하드코딩 포트폴리오 (PROJECTS 상수) | - |
| 🎯 퀴즈 | 오프라인 + Claude AI 생성 | study_all/quiz_requests/results |
| 🤖 AI 설명 | 개념 설명 → daemon → Claude | study_all/explain_requests/results |
| 📊 통계 | Chart.js 3종 차트 | 모든 경로 집계 |

---

## desktop_daemon.py 연동 (v1.5)
- `quiz_requests` 리스너: Claude API로 4지선다 퀴즈 생성
- `explain_requests` 리스너: Claude API로 개념 설명 생성
- 데몬 경로: `D:\AI\260622_1_Remote_claude\desktop_daemon.py`
- 데몬 재시작 명령:
  ```powershell
  $env:PYTHONUTF8='1'; Start-Process "C:\hb\python.exe" -ArgumentList "-X","utf8","D:\AI\260622_1_Remote_claude\desktop_daemon.py" -WindowStyle Normal
  ```

---

## 초기 시드 개념 (첫 접속 3초 후 자동 적재)
1. BOM (Byte Order Mark)
2. CORS & CORS 프록시
3. Firebase Rules (보안 규칙)
4. git pull 없이 push의 위험
5. Claude Tool Use 패턴
6. 계좌 ID 참조 무결성

---

## 다음 세션 작업 후보
- [ ] **퀴즈 데몬 테스트**: 데몬 켜고 퀴즈 탭 → "퀴즈 시작(Claude AI 생성)" 눌러보기
- [ ] master_watch.py 등록부에 Study_Dashboard 추가 (자동 push 연결)

## 만복이 News 현재 상태 (2026-07-06)
- n8n 워크플로우 Active (포트 5680) — `n8n_start.bat` n8n.cmd로 수정 완료
- 텔레그램 전송 ✅ / 게시판 등록 ✅ / 상세 모달 ✅
- `update_geek_news.py`: study-dashboard.html + index.html 동시 업데이트
- 클릭 시 상세 모달: 만복이 요약 + 원본링크 + 긱뉴스링크 + 코멘트 저장
- 관련 스크립트: `D:\Dev\n8n_scripts\update_geek_news.py`
- 앱 버전: v1.2

---

## 자동 배포
- GitHub push → GitHub Pages 2~3분 자동 배포 (Pages 활성화 후)
- master_watch.py 등록부 추가 시 파일 수정 → 12초 후 자동 push

---

## 버전 이력
- v1.0 (2026-06-23): 8탭 전체 구현, Firebase 연동, 시드 개념 6개, daemon v1.5
- v1.1 (2026-06-25): 💬 만복이 채팅탭 추가 → 즉시 삭제

## 삭제된 기능 이력
### 💬 만복이 채팅탭 (2026-06-25 추가 → 즉시 삭제)
**삭제 사유**: 공부방 채팅탭은 daemon → Anthropic API(Haiku) 호출 구조.
API 크레딧이 반드시 필요하고, 이한복님의 목표("API 토큰 없이 만복이 사용")와
근본적으로 상충. 효용 없음으로 판단하여 삭제.
**대안**: 텔레그램 봇(@barobogi_stockbot) — claude.ai 구독으로 API 크레딧 없이 만복이 사용 가능.
