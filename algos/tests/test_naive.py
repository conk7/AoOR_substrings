from ..naive import naive_search as algo


def test_algo():
    text = "aaabbb"

    pattern = "a"
    pos, _ = algo(text, pattern)
    assert pos == [0, 1, 2]

    pattern = "b"
    pos, _ = algo(text, pattern)
    assert pos == [3, 4, 5]

    pattern = "ab"
    pos, _ = algo(text, pattern)
    assert pos == [2]

    pattern = "aaab"
    pos, _ = algo(text, pattern)
    assert pos == [0]

    text = "123"
    pattern = "1234"
    pos, _ = algo(text, pattern)
    assert pos == []

    text = "Персональные данные"
    pattern = "данные"
    pos, _ = algo(text, pattern)
    assert pos == [13]

    text = "abcaaba"
    pattern = "aba"
    pos, _ = algo(text, pattern)
    assert pos == [4]

    text = "abeccacbadbabbad"
    pattern = "abbad"
    pos, _ = algo(text, pattern)
    assert pos == [11]

    text = "abcabeaabcabd"
    pattern = "abcabd"
    pos, _ = algo(text, pattern)
    assert pos == [7]
