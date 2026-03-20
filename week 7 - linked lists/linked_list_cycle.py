# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        slow_index = 0
        while fast != None:
            if slow_index != 0 and slow == fast:
                return True

            slow = slow.next
            if slow == None or slow.next == None:
                return False

            fast = fast.next.next
            slow_index += 1

        return False