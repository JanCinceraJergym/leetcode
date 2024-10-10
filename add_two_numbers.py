from lc import *

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_list_length(l: Optional[ListNode]):
            if l == None:
                return 0
            cl = l
            print(l)
            # A A A -
            length = 1
            while True:
                cl = cl.next
                if cl == None:
                    return length
                length+=1
        
        l1_len = get_list_length(l1)
        l2_len = get_list_length(l2)
        print(l1_len)
        print(l2_len)

