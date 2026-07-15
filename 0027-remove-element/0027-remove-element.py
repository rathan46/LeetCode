class Solution(object):
    def removeElement(self, nums, val):
        l=0
        r=len(nums)
        while l<r:
            if nums[l]==val:
                nums[l]=nums[r-1]
                r-=1
            else:
                l+=1
        return r