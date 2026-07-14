class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        c=nums1+nums2
        c.sort()
        n=len(c)
        if (len(c)%2)==0:
            return (c[n//2-1]+c[n//2])/2.0
        else:
            return c[n//2]