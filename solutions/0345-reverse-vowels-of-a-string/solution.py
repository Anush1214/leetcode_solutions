class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss="aeiouAEIOU"
        s=list(s)
        i=0
        j=len(s)-1

        while i<j:
            if s[i] in ss and s[j] in ss :
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            elif s[i] not in ss:
                i+=1
            else:
                j-=1
        l="".join(s)
        return l

