from add_two_numbers import *

sol = Solution()

def test1():
    assert sol._int_to_list(14) == sol._int_to_list(14)
def test2():
    assert sol.addTwoNumbers(sol._int_to_list(342), sol._int_to_list(465)) == sol._int_to_list(807)
def test3():
    assert sol.addTwoNumbers(sol._int_to_list(9999999), sol._int_to_list(9999)) == sol._int_to_list(10009998)
