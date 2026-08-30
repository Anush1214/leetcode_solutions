class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=n
        if k!=0:
            array=nums[n-k:]
            del nums[n-k:]
            nums[0:0]=array
        # res=[0]*n
        # for i in range(n):
        #     res[(i+k)%n]=nums[i]
        # nums[:]=res

