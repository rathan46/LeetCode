class Solution:
    def intToRoman(self,num):
        values=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        ss=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        a=[]
        for v,s in zip(values,ss):
            while num>=v:
                a.append(s)
                num-=v
        return "".join(a)