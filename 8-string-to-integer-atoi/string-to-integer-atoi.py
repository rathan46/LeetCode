class Solution(object):
    def myAtoi(self,s):
        imx=2**31-1
        imn=-2**31
        i=0
        n=len(s)
        while i<n and s[i]==' ':
            i+=1
        sn=1
        if i<n and (s[i]=='+' or s[i]=='-'):
            if s[i]=='-':
                sn=-1
            i+=1
        r=0
        while i<n and s[i].isdigit():
            d=int(s[i])
            if r>(imx-d)//10:
                return imx if sn==1 else imn
            r=r*10+d
            i+=1
        return sn*r