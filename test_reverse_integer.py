from reverse_integer import *

sol = Solution()

def test1():
    assert sol.reverse(123) == 321

def test2():
    assert sol.reverse(-123) == -321

def test3():
    assert sol.reverse(120) == 21