# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def getKth(self,c,k):
        while c and k>0:
            c=c.next
            k-=1
        return c
    def reverseKGroup(self, head, k):
        d=ListNode(0)
        d.next=head
        gp=d
        while True:
            kth=self.getKth(gp,k)
            if not kth:
                break
            gn=kth.next
            p=gn
            c=gp.next
            while c!=gn:
                t=c.next
                c.next=p
                p=c
                c=t
            t=gp.next
            gp.next=kth
            gp=t
        return d.next