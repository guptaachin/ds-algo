import lc139_word_break
import pytest

@pytest.mark.parametrize(
    ("word", "wordDict", "output"),
    [
        ("leetcode", ["leet","code"], True),
        ("applepenapple", ["apple","pen"], True),
        ("catsandog",  ["cats","dog","sand","and","cat"], False),
    ]
)

# This test will run once per test case
def test_problem(word, wordDict, output):
    s = lc139_word_break.Solution()
    calculated_res = s.wordBreak(word, wordDict)
    assert calculated_res == output
