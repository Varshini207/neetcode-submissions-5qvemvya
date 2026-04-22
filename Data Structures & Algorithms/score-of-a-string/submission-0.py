class Solution:
    def scoreOfString(self, s: str) -> int:
        c=0
        for i in range(len(s)-1):
            a=ord(s[i])
            b=ord(s[i+1])
            if a>=b:
                c+=(a-b)
            else:
                c+=(b-a)
        return c

