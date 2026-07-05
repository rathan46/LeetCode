class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        c=nums1+nums2
        c.sort()
        if (len(c)%2)==0:
            return (c[((len(c)//2)-1)]+c[(len(c)//2)])/2.0
        else:
            return c[len(c)//2]