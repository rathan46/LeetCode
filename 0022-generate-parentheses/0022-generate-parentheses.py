class Solution(object):
    def generateParenthesis(self, n):
        r=[]
        def bcktrk(c,oc,cc):
            if len(c)==2*n:
                r.append(c)
                return
            if oc<n:
                bcktrk(c+"(",oc+1,cc)
            if cc<oc:
                bcktrk(c+")",oc,cc+1)
        bcktrk("",0,0)
        return r