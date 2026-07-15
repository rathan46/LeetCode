class Solution(object):
    def combinationSum(self, candidates, target):
        ans=[]
        path=[]
        def dfs(index,remaining):
            if remaining==0:
                ans.append(path[:])
                return
            if remaining<0 or index==len(candidates):
                return
            path.append(candidates[index])
            dfs(index,remaining-candidates[index])
            path.pop()
            dfs(index+1,remaining)
        dfs(0,target)
        return ans