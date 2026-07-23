
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        first=strs[0]
        for i in range(len(first)):
            char=first[i]
            for j in range(1,len(strs)):
                curr=strs[j]
                if i==len(curr)or curr[i]!=char:
                    return first[:i]
        return first
