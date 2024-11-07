from longest_subs_worep import *

sol = Solution()

def test1():
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3

def test2():
    assert sol.lengthOfLongestSubstring("bbbbb") == 1

def test3():
    assert sol.lengthOfLongestSubstring("pwwkew") == 3

def test4():
    assert sol.lengthOfLongestSubstring("au") == 2