class Solution(object):
    def convert(self, s, nr):
        if nr==1 or nr>=len(s):
            return s
        r=[""]*nr
        cr=0
        d=-1
        for c in s:
            r[cr]+=c
            if cr==0 or cr==nr - 1:
                d*=-1
            cr+=d
        return "".join(r)