from math import factorial
class Solution(object):
    def getPermutation(self, n, k):
        numbers=[str(i) for i in range(1,n+1)]
        k-=1
        ans=[]
        while numbers:
            fact=factorial(len(numbers)-1)
            index=k//fact
            ans.append(numbers.pop(index))
            k%=fact
        return "".join(ans)