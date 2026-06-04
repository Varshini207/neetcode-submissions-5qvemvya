class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for i in digits:
            s += str(i)  # Fix 1: Properly concatenate to the string
            
        num = int(s) + 1  # Fix 2: Convert to int and add 1
        
        # Fix 3: Iterate through the string representation of the new number
        # and convert each character back to an integer.
        l = []
        for j in str(num):
            l.append(int(j))
            
        return l