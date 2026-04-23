class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l=0
        for i in range(len(t)):
            if len(s)==0:
                return True
            else:
                if s[l]==t[i]:
                    l+=1
                if l==len(s):
                    return True
        return len(s)==l