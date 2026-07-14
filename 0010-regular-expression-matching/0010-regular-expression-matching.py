class Solution(object):
    def isMatch(self, s, p):
        m={}
        def dp(i,j):
            if (i,j) in m:
                return m[(i,j)]
            if j==len(p):
                return i==len(s)
            fm=(i<len(s)and(s[i]==p[j] or p[j]=='.'))
            if j+1<len(p) and p[j+1]=='*':
                a=(dp(i,j+2) or (fm and dp(i+1,j)))
            else:
                a=fm and dp(i+1,j+1)
            m[(i,j)]=a
            return a
        return dp(0,0)