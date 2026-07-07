# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        d=ListNode(0)
        d.next=head
        p=d
        while p.next and p.next.next:
            f=p.next
            s=f.next
            f.next=s.next
            s.next=f
            p.next=s
            p=f
        return d.next