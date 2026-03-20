# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2

        result = None

        while curr1 != None and curr2 != None:
            if curr1.val <= curr2.val:
                self.addToList(result, curr1)
                curr1 = curr1.next
            else:
                self.addToList(result, curr2)
                curr2 = curr2.next
        
        return result

    def addToList(self, head, node):
        curr = head
        if head == None:
            head = node
        else:
            while curr.next != None:
                curr = curr.next
            
            curr.next = node