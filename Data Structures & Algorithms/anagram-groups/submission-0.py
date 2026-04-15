class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            l=list(i)
            l.sort()
            r="".join(l)
            if r not in d:
                d[r]=[i]
            else:
                d[r].append(i)
        return list(d.values())
        
        

       