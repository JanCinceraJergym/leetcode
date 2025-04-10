from lc import *

class Solution:
    def reverse(self, x: int) -> int:
        a = abs(x)
        res = 0
        m = a
        digits = []
        for n in range(9):
            d = m % 10**n
            digits.append(d//10**(n-1) if n > 0 else d)
            m -= d
            if m == 0:
                break
        digits.reverse()
        leading_zeros = 0
        for d in digits:
            if d == 0:
                leading_zeros += 1
            else:
                break

        for i, d in enumerate(digits[leading_zeros:]):
            print(d)
            res += d*10**i

        return res*a/x
