# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow

        prev = None
        current = mid
        while current:
            a = current.next
            current.next = prev
            prev = current
            current = a
        l, r = head, prev
        while l != mid:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True
