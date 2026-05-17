# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = head
        arr = []
        while head:
            arr.append(head)
            head = head.next
        removeIndex = len(arr)-n
        if removeIndex==0:
            return start.next
        node = arr[removeIndex-1] 
        node.next = arr[removeIndex].next
        return start

        