class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        total=0
        minl=float('inf')
        for right in range(len(nums)):
            total+=nums[right]
            while total>=target:
                minl=min(minl,right-left+1)
                total-=nums[left]
                left+=1
        return minl if minl!=float('inf') else 0
