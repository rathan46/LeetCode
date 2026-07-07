class Solution(object):
    def divide(self,dividend,divisor):
        imx=2**31-1
        imn=-2**31
        if dividend==imn and divisor==-1:
            return imx
        nve=(dividend<0)!=(divisor<0)
        dividend=abs(dividend)
        divisor=abs(divisor)
        q=0
        while dividend>=divisor:
            t=divisor
            m=1
            while dividend>=(t<<1):
                t<<=1
                m<<=1
            dividend-=t
            q+=m
        if nve:
            q=-q
        return q