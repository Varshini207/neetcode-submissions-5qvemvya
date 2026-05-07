class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=""
        l=[]
        w=list(word1)
        x=list(word2)
        a,b=0,0
        while a<len(w) or b<len(x):
            if a<len(w):
                l.append(w[a])
            if b<len(x):
                l.append(x[b])
            a+=1
            b+=1
        return "".join(i for i in l)