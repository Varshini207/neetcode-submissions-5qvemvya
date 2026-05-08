class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        a,b=0,0
        while a<len(s) and b<len(t):
            if s[a]==t[b]:
                a,b=a+1,b+1
                continue
            a+=1
        return len(t)-b
