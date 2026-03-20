# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first we have to split the linked list into two halves

        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # the slow pointer will arrive at the middle when fast reaches the end
        second_half = slow.next
        # we cut off the first half's reference to the second half so we don't run into loops
        slow.next = None

        # now we reverse the second_half
        node = second_half
        prev = None
        while node != None:
            oldNext = node.next
            node.next = prev
            prev = node
            node = oldNext

        tail = prev
        first = head
        second = tail

        # now we lace the two halves into each other
        while second != None:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
