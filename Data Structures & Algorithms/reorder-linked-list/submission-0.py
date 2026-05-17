# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        first = head
        while head:
            nodes.append(head)
            head = head.next
        i,j=0,len(nodes)
        while len(nodes):
            if len(nodes):
                first.next =nodes.pop(0)
                first = first.next
            if len(nodes):
                first.next = nodes.pop()
                first = first.next
            
        first.next=None