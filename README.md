# 성적 관리 프로그램

## 무엇을 하나요 (What)
성적 CSV 파일을 읽어서 (이름, 점수) 목록을 돌려주고, 유효하지 않은 줄은 건너뛴 줄로 따로 기록합니다.

## 왜 만들었나요 (Why)
실제 파일에 빈 칸이나, 경계 밖 점수가 있으면 코드를 읽다가 죽기 때문에 만들었습니다.

## 어떻게 쓰나요 (How)
Python 3이 필요합니다.

```
python load_scores.py scores.csv
```

파일 이름을 안 주면 `scores.csv`를 읽습니다.

## 어떻게 테스트하나요
```
pip install pytest pytest-cov
python -m pytest
```

통과 화면: 13 passed in 0.20s

커버리지 확인:
```
python -m pytest --cov=load_scores --cov-report=term-missing
```

## 파일 구성
- `load_scores.py`: 성적 CSV를 읽는 함수와 실행 코드
- `test_load_scores.py`: pytest 테스트 (정상, 예외, 경계값)
- `scores.csv`: 정상 예시 데이터
- `empty.csv`: 헤더만 있는 데이터 (예외 테스트용)
- `LICENSE`: MIT 라이선스

## 만든 사람
- 이름: 백규민
- 학번: 2026100731
- AI를 쓴 곳: 테스트 코드 작성에 사용