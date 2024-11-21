from longest_psubstr import *

sol = Solution()

def test1():
    assert sol.longestPalindrome("babad") in ["bab", "aba"]

def test2():
    assert sol.longestPalindrome("abcba") == "abcba"

def test3():
    assert sol.longestPalindrome("cbbd") == "bb"