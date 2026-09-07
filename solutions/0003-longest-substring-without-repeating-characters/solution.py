class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # n=len(s)
        # maxlen=0
        # for i in range(n):
        #     hash_set=[0]*256
        #     for j in range(i,n):
        #         if hash_set[ord(s[j])]==1:
        #             break
        #         hash_set[ord(s[j])]=1
        #         curr=j-i+1
        #         maxlen=max(maxlen,curr)
        # return maxlen

        n=len(s)
        hashlen=256
        hash=[-1]*hashlen

        for i in range(hashlen):
            hash[i]=-1
        l,r,maxlen=0,0,0
        while r<n:
            if hash[ord(s[r])]!=-1:
                l=max(hash[ord(s[r])]+1,l)
            curr=r-l+1
            maxlen=max(maxlen,curr)
            hash[ord(s[r])]=r
            r+=1
        return maxlen
