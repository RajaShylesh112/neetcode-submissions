class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0 
        mc = 0 
        for i in range(len(nums)):
            if nums[i] == 1: 
                count += 1 
            if nums[i] == 0: 
                count = 0 
            mc = max(mc , count)
        return mc 