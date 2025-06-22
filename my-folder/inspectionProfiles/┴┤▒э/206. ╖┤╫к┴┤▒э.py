# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        current=head
        while current:
            a=current.next #保存下一个节点，因为下一行改结构这个点就没了
            current.next=prev
            prev=current # 把prev赋值到当前节点
            current=a #指针 索引到原链表的下一个节点
        return prev