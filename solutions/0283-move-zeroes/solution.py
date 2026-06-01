class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index=0
        for read in range(len(nums)):
            if nums[read]!=0:
                nums[index],nums[read]=nums[read],nums[index]
                index+=1

