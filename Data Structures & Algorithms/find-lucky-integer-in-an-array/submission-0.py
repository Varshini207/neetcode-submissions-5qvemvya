class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = Counter(arr)
        
        max_lucky = -1
        
        # Step 2: Iterate through the unique numbers and find the largest lucky number
        for num, freq in counts.items():
            if num == freq:
                max_lucky = max(max_lucky, num)
                
        return max_lucky