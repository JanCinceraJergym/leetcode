from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        next = str(self.next)
        return f"{self.val} -> {next}"
    
    def __len__(self):
        if self == None:
            return 0
        cl = self
        length = 1
        while True:
            cl = cl.next
            if cl == None:
                return length
            length+=1
    
    def __eq__(self, other: Self):
        cl1 = self
        cl2 = other
        print(f"cl1: {cl1}")
        print(f"cl2: {cl2}")
        if cl1 is None and cl2 is None:
            return True
        while cl1 is not None:
            if cl2 is None:
                return False
            if cl1.val != cl2.val:
                return False
            cl1 = cl1.next
            cl2 = cl2.next
        return True
        