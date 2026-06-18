class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=nums[0]
        maxl=nums[0]
        for i in range(1,len(nums)):
            curr=max(nums[i],curr+nums[i])
            maxl=max(maxl,curr)
        return maxl
