class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # pr=0
        # for i in range(len(prices)-1):
        #     for j in range(i+1,len(prices)):
        #         if prices[j]-prices[i]>pr:
        #             pr=prices[j]-prices[i]
        # return pr
        min=prices[0]
        max=0
        for i in range(len(prices)):
            if prices[i]<min:
                min=prices[i]
            elif prices[i]-min>max:
                max=prices[i]-min

        return max
