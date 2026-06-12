class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = cnt = j = 0
        for i in range(len(nums)):
            cnt += nums[i] ^ 1
            while cnt > k:
                cnt -= nums[j] ^ 1
                j += 1
            res = max(res, i - j + 1)
        return res
