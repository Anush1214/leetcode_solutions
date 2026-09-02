class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1={}
        d2={}
        for i in range(len(s)):
            char_t=s[i]
            char_s=t[i]

            if char_s in d1 and d1[char_s]!=char_t:
                return False
            if char_t in d2 and d2[char_t]!=char_s:
                return False
            d1[char_s]=char_t
            d2[char_t]=char_s
        return True
