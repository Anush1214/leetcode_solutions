class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count+=1
            else:
                result = max(result,count)
                count = 0
        result = max(result,count)
        return result
