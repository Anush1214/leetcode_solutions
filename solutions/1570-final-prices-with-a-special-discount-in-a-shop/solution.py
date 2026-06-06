class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # n=len(prices)
        # ans=[]
        # for i in range(n):
        #     disc=0
        #     for j in range(i+1,n):
        #         if prices[j] <= prices[i]:
        #             disc+=prices[j]
        #             break
        #     final=prices[i]-disc
        #     ans.append(final)
        # return ans

        n = len(prices)

        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break

        return prices
