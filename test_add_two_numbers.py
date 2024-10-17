from add_two_numbers import *

sol = Solution()

def gen_linked_list(n: int) -> Optional[ListNode]:
    rem = n
    node = ListNode()
    root = node
    while rem > 0:
        node.val = rem % 10
        if rem > 10:
            node.next = ListNode()
            node = node.next
        else:
            node.next = None
        rem //= 10
    return root

def test1():
    assert gen_linked_list(14) == gen_linked_list(14)
def test2():
    assert sol.addTwoNumbers(gen_linked_list(342), gen_linked_list(465)) == gen_linked_list(807)
def test3():
    assert sol.addTwoNumbers(gen_linked_list(9999999), gen_linked_list(9999)) == gen_linked_list(10009998)