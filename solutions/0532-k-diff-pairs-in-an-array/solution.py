class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d={}
        pair=0
        for i in nums:
            d[i]=d.get(i,0)+1
        
        for num in d:
            if k>0:
                if num+k in d:
                    pair+=1
            else:
                if d[num]>1:
                    pair+=1
        return pair
