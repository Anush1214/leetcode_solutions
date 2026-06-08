class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxs=0
        for row in accounts:
            sums=0
            for i in row:
                sums+=(i)
            maxs=max(maxs,sums)
        return maxs
