# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        if head == None:
            return head
        while head.next != None:
            arr.append(head.val)
            print(head.val)
            head = head.next
        arr.append(head.val)
        print(arr)
        top = head
        while len(arr) > 0 :
            print(arr)
            head.val = arr.pop()
            head.next = ListNode(None)
            oldHead = head
            head = head.next
        oldHead.next = None
        
        return top
            
        