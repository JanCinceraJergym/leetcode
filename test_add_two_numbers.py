from add_two_numbers import *

sol = Solution()

def gen_linked_list(n: int) -> Optional[ListNode]:
    rem = n
    node = ListNode()
    root = node
    while rem > 0:
        node.val = rem % 10
        node.next = ListNode()
        print(node)
        node = node.next
        rem //= 10
    node.next = None
    return root

def test1():
    assert sol.addTwoNumbers(gen_linked_list(342), gen_linked_list(465)) == gen_linked_list(807)