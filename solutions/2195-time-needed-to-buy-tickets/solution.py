class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time=0
        tar=tickets[k]
        for i in range(len(tickets)):
            if i<=k:
                time+=min(tickets[i],tar)
            else:
                time+=min(tickets[i],tar-1)
        return time
