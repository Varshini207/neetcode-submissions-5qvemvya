class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(0,n+1):
            s=bin(i)[2:]
            c=0
            for j in range(len(s)):
                if s[j]=='1':
                    c+=1
            l.append(c)
        

        return l