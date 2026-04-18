class Solution:
    def hammingWeight(self, n: int) -> int:
        s=bin(n)[2:]
        c=0
        for i in range(len(s)):
            if s[i]=='1':
                c+=1
        return c