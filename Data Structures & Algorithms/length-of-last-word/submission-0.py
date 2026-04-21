class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r=s.split()
        a=r[::-1]
        return len(a[0])