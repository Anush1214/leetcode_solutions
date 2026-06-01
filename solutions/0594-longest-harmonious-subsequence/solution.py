class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1=0
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1
        for i in count:
            if i+1 in count:
                l=count[i]+count[i+1]
                max1=max(max1,l)
        return max1
