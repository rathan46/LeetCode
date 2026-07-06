class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n=len(nums)
        clst=nums[0]+nums[1]+nums[2]
        for i in range(n-2):
            l=i+1
            r=n-1
            while l<r:
                t=nums[i]+nums[l]+nums[r]
                if abs(t-target)<abs(clst-target):
                    clst=t
                if t<target:
                    l+=1
                elif t>target:
                    r-=1
                else:
                    return t
        return clst