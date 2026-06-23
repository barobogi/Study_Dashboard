# CHANGELOG — 바로보기의 공부방

## v1.0 — 2026-06-23

### 추가
- **로드맵 탭**: Stage 1~3 커리큘럼 체크박스 + Firebase 진도 저장 + 단계별 진행률
- **오늘의 발견 탭**: 즉흥 학습 메모 빠른 캡처 (카테고리/출처 태그) + Firebase 날짜별 저장
- **학습일지 탭**: 날짜별 학습 기록 + 학습 시간 + 기분 이모지 + Firebase 저장
- **개념노트 탭**: 카드형 개념 정리 + 카테고리 필터 + Firebase CRUD + 초기 6개 시드 개념
- **프로젝트 탭**: 완료 프로젝트 포트폴리오 (주식대시보드/멀티미디어/Remote Claude/공부방)
- **퀴즈 탭**: 오프라인 기본 퀴즈 + Firebase relay → 데몬 → Claude AI 문제 생성
- **AI 설명 탭**: 개념 설명 요청 → Firebase → desktop_daemon.py → Claude AI → 실시간 표시
- **통계 탭**: 학습 현황 6개 지표 + 주간 학습 시간 / 카테고리별 메모 / 로드맵 달성률 차트
- **desktop_daemon.py v1.5**: quiz_requests + explain_requests Firebase 리스너 추가
- 다크/라이트 모드 토글 (localStorage 유지)
- 시드 개념 6개: BOM, CORS, Firebase Rules, git pull 위험, Tool Use 패턴, 계좌 ID 참조 무결성

### 기술 스택
- HTML/CSS/JS 단일 파일 (GitHub Pages 배포)
- Firebase Realtime DB (remote-claude-358d6 프로젝트)
- Chart.js 4.4 (통계 차트)
- desktop_daemon.py 연동 (Claude AI 퀴즈/설명 생성)
