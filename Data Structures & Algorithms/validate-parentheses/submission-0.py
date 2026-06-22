class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d={'}':'{',']':'[',')':'('}
        l=[]
        for i in s:
            if i in "({[":
                l.append(i)
            else:
                if len(l)==0:
                    return False
                else:
                    if l.pop()!=d[i]:
                        return False
        return len(l)==0