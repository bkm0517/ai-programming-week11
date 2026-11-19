import pytest, runpy, sys
from load_scores import load_scores


# 슬라이드 13쪽의 쓰기() 도우미: 점수 하나짜리 임시 CSV를 만든다
# (tmp_path는 pytest가 주는 임시 폴더라 내 폴더가 지저분해지지 않는다)
def 쓰기(경로, 점수):
    경로.write_text(f"이름,점수\n김하나,{점수}\n", encoding="utf-8")





# ---------- 정상 (기록표① 정상 ①②③) ----------

def test_정상_파일을_읽는다():
    kept, skipped = load_scores("scores.csv")
    assert len(kept) == 5


def test_빈_줄은_건너뛴다(tmp_path):
    f = tmp_path / "빈줄.csv"
    f.write_text("이름,점수\n김하나,88\n\n이둘,75\n", encoding="utf-8")
    kept, skipped = load_scores(str(f))
    assert len(kept) == 2


def test_이름에_쉼표가_있어도_읽는다(tmp_path):
    f = tmp_path / "쉼표.csv"
    f.write_text('이름,점수\n"김, 하나",88\n', encoding="utf-8")
    kept, skipped = load_scores(str(f))
    assert kept == [("김, 하나", 88)]


# ---------- 예외 (슬라이드 12쪽 그대로) ----------

def test_없는_파일이면_오류가_난다():
    with pytest.raises(FileNotFoundError):
        load_scores("없는파일.csv")


def test_헤더만_있으면_빈_결과가_나온다():
    kept, skipped = load_scores("empty.csv")
    assert kept == []
    assert skipped == []


# ---------- 경계값 (슬라이드 13쪽 그대로) ----------

@pytest.mark.parametrize("점수, 유효한가", [
    (-1, False),    # 경계 바로 아래
    (0, True),      # ★ 아래쪽 경계
    (1, True),
    (99, True),
    (100, True),    # ★ 위쪽 경계
    (101, False),   # 경계 바로 위
])
def test_점수_경계값(tmp_path, 점수, 유효한가):
    f = tmp_path / "임시.csv"
    쓰기(f, 점수)
    kept, skipped = load_scores(str(f))
    assert (len(kept) == 1) == 유효한가

def test_이름이_비어_있으면_건너뛴다(tmp_path):
    f = tmp_path / "이름없음.csv"
    f.write_text("이름,점수\n,88\n", encoding="utf-8")
    kept, skipped = load_scores(str(f))
    assert kept == []
    assert len(skipped) == 1
    assert skipped[0][2] == "이름이 비어 있음"


def test_직접_실행하면_결과를_출력한다(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["load_scores.py", "scores.csv"])
    runpy.run_path("load_scores.py", run_name="__main__")
    출력 = capsys.readouterr().out
    assert "읽은 줄" in 출력
