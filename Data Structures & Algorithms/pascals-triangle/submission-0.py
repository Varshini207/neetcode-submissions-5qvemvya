class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[[1]]
        for i in range(numRows-1):
            t=[0]+l[-1]+[0]
            r=[]
            for j in range(len(l[-1])+1):
                r.append(t[j]+t[j+1])
            l.append(r)
        return l