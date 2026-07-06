class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        ph={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        a=[]
        def bcktrck(i,p):
            if i==len(digits):
                a.append(p)
                return
            for ch in ph[digits[i]]:
                bcktrck(i+1,p+ch)
        bcktrck(0,"")
        return a