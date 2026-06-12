class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        v = set()
        def dfs(city):
            v.add(city)
            for nei in range(n):
                if isConnected[city][nei] == 1 and nei not in v:
                    dfs(nei)
        prov = 0
        for city in range(n):
            if city not in v:
                prov += 1
                dfs(city)
        return prov
