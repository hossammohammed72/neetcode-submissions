# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = ListNode()
        mergedListHead = mergedList
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        breakFlag=False
        while list1 is not None or list2 is not None:
            if list1 is None:
                mergedList.val = list2.val
                list2 = list2.next
            elif list2 is None:
                mergedList.val = list1.val
                list1 = list1.next
            elif list1.val < list2.val:
                mergedList.val = list1.val
                list1 = list1.next
            elif list1.val > list2.val:
                mergedList.val = list2.val
                list2 = list2.next
            else:
                mergedList.val = list1.val
                mergedList.next = ListNode()
                mergedList = mergedList.next
                mergedList.val = list2.val
                list1 = list1.next
                list2 = list2.next
            mergedList.next = ListNode()
            oldHead = mergedList
            mergedList = mergedList.next
        oldHead.next = None
        return mergedListHead

        