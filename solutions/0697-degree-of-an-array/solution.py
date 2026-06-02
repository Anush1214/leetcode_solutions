class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq={}
        f={}
        l={}
        for i in range(len(nums)):
            if nums[i] not in freq:
                f[nums[i]]=i
            l[nums[i]]=i
            freq[nums[i]]=freq.get(nums[i],0)+1

        d=max(freq.values())
        ans=len(nums)
        for i in freq:
            if freq[i]==d:
                res=l[i]-f[i]+1
                ans=min(res,ans)
        return ans
