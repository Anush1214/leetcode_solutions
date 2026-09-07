class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        # ans=[]
        # n=len(intervals)
        # i=0
        # while i<n:
        #     start=intervals[i][0]
        #     end=intervals[i][1]
        #     j=i+1

        #     while j<n and intervals[j][0]<=end:
        #         end=max(end,intervals[j][1])
        #         j+=1

        #     ans.append([start,end])
        #     i=j
        # return ans

        merged=[]
        for interval in intervals:
            if not merged or merged[-1][1]<interval[0]:
                merged.append(interval)
            else:
                merged[-1][1]=max(merged[-1][1],interval[1])
        return merged


