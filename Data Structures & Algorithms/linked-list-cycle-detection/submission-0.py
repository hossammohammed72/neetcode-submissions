# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        mem = {}
        while head:
            if head in mem:
                return True
            mem[head] = True
            head = head.next
        return False
