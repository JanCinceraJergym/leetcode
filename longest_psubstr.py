from lc import *

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s: str) -> bool:
            return s == s[::-1]
        
        if isPalindrome(s):
            return s
        
        a = []
        for i in range(len(s)):
            current = ""
            for c in s[i::]:
                current += c
                a.append(current)

        palindromes = []
        for x in a:
            if isPalindrome(x):
                palindromes.append(x)
        
        palindromes.sort(key=lambda x: -len(x))
        return palindromes[0]