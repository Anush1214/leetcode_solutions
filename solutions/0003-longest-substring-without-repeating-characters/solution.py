class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index={}
        maxl=0
        left=0

        for right in range(len(s)):
            char=s[right]
            if char in index and index[char]>=left:
                left=index[char]+1
            index[char]=right
            curr=right-left+1
            maxl=max(maxl,curr)
        return maxl
