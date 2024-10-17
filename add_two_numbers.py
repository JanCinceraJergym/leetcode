from lc import *

class Solution:
    @staticmethod
    def _list_to_int(l: ListNode) -> int:
        res = 0
        i = 0
        cl = l
        while cl is not None:
            res += cl.val * 10**i
            i+=1
            cl = cl.next
        return res

    @staticmethod
    def _int_to_list(n: int) -> ListNode:
        rem = n
        node = ListNode()
        root = node
        while rem > 0:
            node.val = rem % 10
            if rem < 10:
                node.next = None
            else:
                node.next = ListNode()
            node = node.next
            rem //= 10
        return root

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self._int_to_list(self._list_to_int(l1) + self._list_to_int(l2))
        

