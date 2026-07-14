class Solution(object):
    def reverse(self,x):
        imx=2**31-1
        imn=-2**31
        s=-1 if x<0 else 1
        x=abs(x)
        r=0
        while x!=0:
            d=x%10
            x//=10
            if r>(imx-d)//10:
                return 0
            r=r*10+d
        return s*r