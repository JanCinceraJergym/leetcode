from lc import *

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def list_to_int(l: ListNode) -> int:
            res = 0
            i = 0
            cl = l
            while cl is not None:
                res += cl.val * 10**i
                i+=1
                cl = cl.next
            return res

        rem = list_to_int(l1) + list_to_int(l2)
        print(rem)
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

