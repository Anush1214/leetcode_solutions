class Solution:
    def minimumRecolors(self, s: str, k: int) -> int:
        n=len(s)
        count=0
        for i in range(k):
            if s[i]=="W":
                count+=1
        c=count
        for i in range(k,n):
            if s[i]=="W":
                count+=1
            if s[i-k]=="W":
                count-=1
            c=min(c,count)
        return c
