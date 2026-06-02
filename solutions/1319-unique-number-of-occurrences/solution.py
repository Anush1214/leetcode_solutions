class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        d={}
        for i in arr:
            d[i]=d.get(i,0)+1
        
        freq=d.values()
        uni=set(freq)

        return len(freq)==len(uni)
