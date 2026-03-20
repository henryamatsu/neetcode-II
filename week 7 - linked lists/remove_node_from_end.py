# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # determine the length of list

        curr = head
        length = 0
        while curr != None:
            curr = curr.next
            length += 1
        
        cutoff = length - n

        dummy = ListNode(None, head)
        curr = dummy
        for _ in range(cutoff):
            curr = curr.next
        
        curr.next = curr.next.next

        return dummy.next