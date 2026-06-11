class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inn=[0]*(n+1)
        out=[0]*(n+1)

        for a,b in trust:
            inn[b]+=1
            out[a]+=1
        for i in range(1,len(inn)):
            if inn[i]==n-1 and out[i]==0:
                return i
        return -1
    
