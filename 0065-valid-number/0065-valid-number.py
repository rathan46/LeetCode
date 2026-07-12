class Solution:
    def isNumber(self, s):
        def isInteger(x):
            if not x:
                return False
            if x[0] in '+-':
                x=x[1:]
            return len(x)>0 and x.isdigit()
        def isDecimal(x):
            if not x:
                return False
            if x[0] in '+-':
                x=x[1:]
            if '.' not in x:
                return False
            left,right=x.split('.',1)
            if left=='' and right=='':
                return False
            if left and not left.isdigit():
                return False
            if right and not right.isdigit():
                return False
            return True
        if 'e' in s:
            base, exp=s.split('e',1)
            return (isInteger(base) or isDecimal(base)) and isInteger(exp)
        if 'E' in s:
            base, exp = s.split('E',1)
            return (isInteger(base) or isDecimal(base)) and isInteger(exp)
        return isInteger(s) or isDecimal(s)