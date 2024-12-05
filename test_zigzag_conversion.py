from zigzag_conversion import *

sol = Solution()

def test1():
    assert sol.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"

def test2():
    assert sol.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"

def test3():
    assert sol.convert("A", 1) == "A"