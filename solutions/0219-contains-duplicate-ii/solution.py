class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        r=set()
        for i in range(len(nums)):
            if nums[i] in r:
                return True
            r.add(nums[i])
            if len(r)>k:
                r.remove(nums[i-k])
        return False
