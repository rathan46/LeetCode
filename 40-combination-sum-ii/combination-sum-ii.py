class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans=[]
        path=[]
        def backtrack(start,remaining):
            if remaining==0:
                ans.append(path[:])
                return
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>remaining:
                    break
                path.append(candidates[i])
                backtrack(i+1,remaining-candidates[i])
                path.pop()
        backtrack(0,target)
        return ans