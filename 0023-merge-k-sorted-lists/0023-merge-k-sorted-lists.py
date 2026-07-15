import heapq
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        h=[]
        for i,n in enumerate(lists):
            if n:
                heapq.heappush(h,(n.val,i,n))
        d=ListNode(-1)
        t=d
        while h:
            value,i,n=heapq.heappop(h)
            t.next=n
            t=t.next
            if n.next:
                heapq.heappush(h,(n.next.val,i,n.next))
        return d.next