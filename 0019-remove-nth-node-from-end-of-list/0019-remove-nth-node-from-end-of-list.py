# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        l=0
        c=head
        while c:
            l+=1
            c=c.next
        d=ListNode(0)
        d.next=head
        c=d
        for _ in range(l-n):
            c=c.next
        c.next=c.next.next
        return d.next