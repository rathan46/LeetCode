class Solution(object):
    def first(self, nums, target):
        left,right=0,len(nums)-1
        ans=-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                ans=mid
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return ans
    def last(self,nums,target):
        left,right=0,len(nums)-1
        ans=-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                ans=mid
                left=mid+1
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return ans
    def searchRange(self,nums,target):
        return [self.first(nums,target),self.last(nums,target)]