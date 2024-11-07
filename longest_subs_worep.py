from lc import *

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        l = 0
        for start in range(len(s)-1):
            letters = set()
            for c in s[start:]:
                if c in letters:
                    if len(letters) > l:
                        l = len(letters)
                    letters = set()
                    break
                letters.add(c)
            if len(letters) > l:
                    l = len(letters)
        return l