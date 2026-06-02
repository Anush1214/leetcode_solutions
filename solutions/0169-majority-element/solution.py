class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # d={}
        # n=len(nums)
        # for i in nums:
        #     d[i]=d.get(i,0)+1

        # for i in d:
        #     if d[i]>(n//2):
        #         return i
        # return -1

        count=0
        max=None
        for i in nums:
            if count==0:
                max=i
            if i==max:
                count+=1
            else:
                count-=1
        return max
